from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Product
from .forms import ProductForm


def global_context(request):
    """ Context processor to make products available in all templates """
    products = Product.objects.all()
    return {'nav_products': products}


def all_products(request):
    """ A view to show all products, including sorting and search queries """

    products = Product.objects.all().order_by("sku")

    context = {
        'products': products,
    }

    return render(request, 'products/products.html', context)


def product_detail(request, product_id):
    """ A view to show individual product details """

    product = get_object_or_404(Product, pk=product_id)

    context = {
        'product': product,
    }

    return render(request, 'products/product_detail.html', context)


@login_required
def add_product(request):
    """
    Allows a store owner to add a new product to the store.

    **Access Restrictions:**
    - Only superusers can access this view.
      Non-superusers are redirected to the home page with an error message.

    **Behavior:**
    - Displays a blank `ProductForm` for GET requests.
    - Processes the submitted form on POST requests:
    - If valid, saves the new product and redirects to its
      detail page with a success message.
    - If invalid, re-renders the form with an error message.

    **Template:**
    - `products/add_product.html`
    """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save()
            messages.success(request, 'Successfully added product!')
            return redirect(reverse('product_detail', args=[product.id]))
        else:
            messages.error(
                request,
                'Failed to add product. Please ensure the form is valid.'
            )
    else:
        form = ProductForm()

    template = 'products/add_product.html'
    context = {
        'form': form,
    }

    return render(request, template, context)


@login_required
def edit_product(request, product_id):
    """
    Allows a store owner to edit an existing product in the store.

    **Access Restrictions:**
    - Only superusers can access this view.
      Non-superusers are redirected to the home page with an error message.

    **Behavior:**
    - Retrieves the product by its ID. If not found, returns a 404 error.
    - For GET requests:
    - Displays a pre-filled `ProductForm` with the product's details.
    - Shows an info message indicating the product being edited.
    - For POST requests:
    - If the form is valid, updates the product and redirects to its
      detail page with a success message.
    - If invalid, re-renders the form with an error message.

    **Template:**
    - `products/edit_product.html`
    """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    product = get_object_or_404(Product, pk=product_id)
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully updated product!')
            return redirect(reverse('product_detail', args=[product.id]))
        else:
            messages.error(
                request,
                'Failed to update product. Please ensure the form is valid.'
            )
    else:
        form = ProductForm(instance=product)
        messages.info(request, f'You are editing {product.name}')

    template = 'products/edit_product.html'
    context = {
        'form': form,
        'product': product,
    }

    return render(request, template, context)


@login_required
def delete_product(request, product_id):
    """
    Deletes a product from the store.

    **Access Restrictions:**
    - Only superusers can delete products.
      Non-superusers are redirected to the home page with an error message.

    **Behavior:**
    - Retrieves the product by its ID. If not found, returns a 404 error.
    - Deletes the product from the database.
    - Displays a success message confirming the deletion.
    - Redirects to the products page after deletion.

    **Redirects:**
    - If the user is unauthorized → Redirects to home with an error message.
    - After successful deletion → Redirects to the products page.
    """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    product = get_object_or_404(Product, pk=product_id)
    product.delete()
    messages.success(request, 'Product deleted!')
    return redirect(reverse('products'))
