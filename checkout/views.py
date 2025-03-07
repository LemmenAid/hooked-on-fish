from django.shortcuts import (
    render, redirect, reverse, get_object_or_404, HttpResponse
)
from django.views.decorators.http import require_POST
from django.contrib import messages
from django.conf import settings

from .forms import OrderForm
from .models import Order, OrderLineItem

from products.models import Product
from profiles.models import UserProfile
from profiles.forms import UserProfileForm
from bag.contexts import bag_contents

import stripe
import json


@require_POST
def cache_checkout_data(request):
    """
    Stores checkout-related data in the Stripe PaymentIntent metadata.

    Updates an instance of :model:`stripe.PaymentIntent` with metadata
    containing the user's shopping bag and save-info preference.

    **Context**
    - ``bag``: The contents of the shopping bag stored in the session.
    - ``save_info``: The user's preference for saving checkout details.
    - ``username``: The authenticated user making the request.

    **Returns**
    - :status:`200` if the metadata update is successful.
    - :status:`400` with an error message if an exception occurs.
    """
    try:
        pid = request.POST.get('client_secret').split('_secret')[0]
        stripe.api_key = settings.STRIPE_SECRET_KEY
        stripe.PaymentIntent.modify(pid, metadata={
            'bag': json.dumps(request.session.get('bag', {})),
            'save_info': request.POST.get('save_info'),
            'username': request.user,
        })
        return HttpResponse(status=200)
    except Exception as e:
        messages.error(request, 'Sorry, your payment cannot be \
            processed right now. Please try again later.')
        return HttpResponse(content=e, status=400)


def checkout(request):
    """
    Handles the checkout process, including order creation, payment intent,
    and form validation.

    Processes an instance of :model:`orders.Order` with its associated
    :model:`orders.OrderLineItem` based on the user's shopping bag.

    **Context**
    - ``order_form``: An instance of :form:`orders.OrderForm` pre-filled with
      user details if authenticated.
    - ``stripe_public_key``: The public Stripe API key for payment processing.
    - ``client_secret``: The client secret for the Stripe PaymentIntent.

    **POST Request**
    - Validates order form data and creates an order.
    - Saves order details, including bag contents and Stripe payment ID.
    - Creates order line items for each product in the shopping bag.
    - Redirects to the checkout success page upon completion.
    - Displays error messages if form validation or product lookup fails.

    **GET Request**
    - Retrieves shopping bag contents and calculates the total amount.
    - Initializes a Stripe PaymentIntent.
    - Pre-fills order form with user profile data if authenticated.
    - Redirects to the products page if the shopping bag is empty.

    **Returns**
    - Renders :template:`checkout/checkout.html` with order form & Stripe.
    - Redirects to :view:`checkout_success` upon successful order placement.
    - Redirects to :view:`view_bag` if an issue occurs with a product.
    - Redirects to :view:`products` if the shopping bag is empty.
    """
    stripe_public_key = settings.STRIPE_PUBLIC_KEY
    stripe_secret_key = settings.STRIPE_SECRET_KEY

    if request.method == 'POST':
        bag = request.session.get('bag', {})

        form_data = {
            'full_name': request.POST['full_name'],
            'email': request.POST['email'],
            'phone_number': request.POST['phone_number'],
            'country': request.POST['country'],
            'postcode': request.POST['postcode'],
            'town_or_city': request.POST['town_or_city'],
            'street_address1': request.POST['street_address1'],
            'street_address2': request.POST['street_address2'],
            'county': request.POST['county'],
        }
        order_form = OrderForm(form_data)
        if order_form.is_valid():
            order = order_form.save(commit=False)
            pid = request.POST.get('client_secret').split('_secret')[0]
            order.stripe_pid = pid
            order.original_bag = json.dumps(bag)
            order.save()
            for item_id, quantity in bag.items():
                try:
                    product = Product.objects.get(id=item_id)
                    order_line_item = OrderLineItem(
                        order=order,
                        product=product,
                        quantity=quantity,
                    )
                    order_line_item.save()
                except Product.DoesNotExist:
                    messages.error(request, "One of the products in your bag \
                                   wasn't found in our database. \
                                   Please call us for assistance!")
                    order.delete()
                    return redirect(reverse('view_bag'))

            request.session['save_info'] = 'save-info' in request.POST
            return redirect(
                reverse('checkout_success', args=[order.order_number]))
        else:
            messages.error(request, 'There was an error with your form. \
                Please double-check your information.')
    else:
        bag = request.session.get('bag', {})
        if not bag:
            messages.error(request, "Your bag is empty at the moment.")
            return redirect(reverse('products'))

        current_bag = bag_contents(request)
        total = current_bag['grand_total']
        stripe_total = round(total * 100)
        stripe.api_key = stripe_secret_key
        intent = stripe.PaymentIntent.create(
            amount=stripe_total,
            currency=settings.STRIPE_CURRENCY,
        )

        if request.user.is_authenticated:
            try:
                profile = UserProfile.objects.get(user=request.user)
                order_form = OrderForm(initial={
                    'full_name': profile.user.get_full_name(),
                    'email': profile.user.email,
                    'phone_number': profile.default_phone_number,
                    'country': profile.default_country,
                    'postcode': profile.default_postcode,
                    'town_or_city': profile.default_town_or_city,
                    'street_address1': profile.default_street_address1,
                    'street_address2': profile.default_street_address2,
                    'county': profile.default_county,
                })
            except UserProfile.DoesNotExist:
                order_form = OrderForm()
        else:
            order_form = OrderForm()

    if not stripe_public_key:
        messages.warning(request, 'Stripe public key is missing. \
            Did you forget to set it in your environment?')

    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': stripe_public_key,
        'client_secret': intent.client_secret,
    }

    return render(request, template, context)


def checkout_success(request, order_number):
    """
    Handles successful order completion and updates user profile information.

    Retrieves an instance of :model:`orders.Order` based on the order number
    and, if the user is authenticated, associates it with their
    :model:`profiles.UserProfile`.

    **Context**
    - ``order``: The successfully processed instance of :model:`orders.Order`.

    **Functionality**
    - Fetches the completed order using the provided order number.
    - If the user is authenticated, links the order to their profile.
    - If `save_info` is enabled, updates the user's default shipping details.
    - Displays a success message with the order number and confirmation email.
    - Clears the shopping bag from the session after checkout.

    **Returns**
    - Renders :template:`checkout/checkout_success.html` with order details.
    """
    save_info = request.session.get('save_info')
    order = get_object_or_404(Order, order_number=order_number)

    if request.user.is_authenticated:
        profile = UserProfile.objects.get(user=request.user)
        # Attach the user's profile to the order
        order.user_profile = profile
        order.save()

        # Save the user's info
        if save_info:
            profile_data = {
                'default_phone_number': order.phone_number,
                'default_country': order.country,
                'default_postcode': order.postcode,
                'default_town_or_city': order.town_or_city,
                'default_street_address1': order.street_address1,
                'default_street_address2': order.street_address2,
                'default_county': order.county,
            }
            user_profile_form = UserProfileForm(profile_data, instance=profile)
            if user_profile_form.is_valid():
                user_profile_form.save()

    messages.success(request, f'Order successfully processed! \
        Your order number is {order_number}. A confirmation \
        email will be sent to {order.email}.')

    if 'bag' in request.session:
        del request.session['bag']

    template = 'checkout/checkout_success.html'
    context = {
        'order': order,
    }

    return render(request, template, context)
