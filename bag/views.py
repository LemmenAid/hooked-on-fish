from django.shortcuts import (
    render, redirect, reverse, HttpResponse, get_object_or_404
)
from django.contrib import messages
from products.models import Product


def view_bag(request):
    """ A view that renders the bag contents page """

    return render(request, 'bag/bag.html')


def add_to_bag(request, item_id):
    """ Add a quantity of the specified product to the shopping bag """

    product = get_object_or_404(Product, pk=item_id)
    redirect_url = request.POST.get('redirect_url')
    bag = request.session.get('bag', {})

    try:
        quantity = int(request.POST.get('quantity'))
    except ValueError:
        messages.error(request, "Invalid quantity entered.")
        return redirect('view_bag')

    if item_id in list(bag.keys()):
        new_quantity = bag[item_id] + quantity
        if new_quantity > 20:
            bag[item_id] = 20  # Cap at 20
            messages.warning(
                request,
                f"Maximum quantity for {product.name} =20. Quantity set to 20."
            )
        else:
            bag[item_id] = new_quantity
            messages.success(
                request,
                f"Updated {product.name} quantity to {bag[item_id]}."
            )
    else:
        if quantity > 20:
            bag[item_id] = 20
            messages.warning(
                request,
                f"Maximum quantity for {product.name} =20. Quantity set to 20."
            )
        else:
            bag[item_id] = quantity
            messages.success(request, f"Added {product.name} to your bag.")

    request.session['bag'] = bag
    return redirect(redirect_url)


def adjust_bag(request, item_id):
    """Adjust the quantity of the specified product to the specified amount"""

    product = get_object_or_404(Product, pk=item_id)
    bag = request.session.get('bag', {})

    try:
        quantity = int(request.POST.get('quantity'))
    except ValueError:
        messages.error(request, "Invalid quantity entered.")
        return redirect(reverse('view_bag'))

    if quantity > 0:
        bag[item_id] = quantity
        messages.success(
            request,
            f'Updated {product.name} quantity to {bag[item_id]}'
        )
    else:
        bag.pop(item_id, None)  # Use .pop with default to avoid KeyError
        messages.success(request, f'Removed {product.name} from your bag')

    request.session['bag'] = bag
    return redirect(reverse('view_bag'))


def remove_from_bag(request, item_id):
    """Remove the item from the shopping bag"""

    try:
        product = get_object_or_404(Product, pk=item_id)
        bag = request.session.get('bag', {})
        bag.pop(item_id)
        messages.success(request, f'Removed {product.name} from your bag')

        request.session['bag'] = bag
        return HttpResponse(status=200)

    except Exception as e:
        messages.error(request, f'Error removing item: {e}')
        return HttpResponse(status=500)
