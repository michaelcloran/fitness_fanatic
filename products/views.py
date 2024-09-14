from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.db.models.functions import Lower
from .models import Product, Category, WorkoutProgram
from trainers.models import TrainerProfile

from .forms import ProductForm, WorkoutProgramForm

# Create your views here.
def all_products(request):
    """ A view to show all products, including sorting and search queries """

    query = None
    categories = None
    sort = None
    direction = None
    products = Product.objects.all()

    if request.GET:
        if 'sort' in request.GET:
            sortkey = request.GET['sort']
            sort = sortkey
            if sortkey == 'name':
                sortkey = 'lower_name'
                products = products.annotate(lower_name=Lower('name'))
            if sortkey == 'category':
                sortkey = 'category__name'

            if 'direction' in request.GET:
                direction = request.GET['direction']
                if direction == 'desc':
                    sortkey = f'-{sortkey}'

            products = products.order_by(sortkey)

        if 'category' in request.GET:
            categories = request.GET['category'].split(',')
            products = products.filter(category__name__in=categories)
            categories = Category.objects.filter(name__in=categories)

        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request, "You didn't enter any search criteria!")
                return redirect(reverse('products'))
            
            queries = Q(name__icontains=query) | Q(description__icontains=query)
            products = products.filter(queries)

    current_sorting = f'{sort}_{direction}'

    context = {
        'products': products,
        'search_term': query,
        'current_categories': categories,
        'current_sorting': current_sorting,
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
    """ Add a product to the store """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))
    temp_category_int = 0
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        workout_form = WorkoutProgramForm(request.POST)

        temp_category_int = request.POST.get('category')
        print(temp_category_int)

        if temp_category_int == '7': # workout program
            if form.is_valid() and workout_form.is_valid():
                product = form.save()

                wo_model = WorkoutProgram()

                trainer = get_object_or_404(TrainerProfile, pk=request.POST.get('trainer'))

                wo_model.trainer = trainer
                wo_model.product = product
                wo_model.class_size = request.POST.get('class_size')
                wo_model.start_date = request.POST.get('start_date')
                wo_model.number_weeks = request.POST.get('number_weeks')
                wo_model.end_date = request.POST.get('end_date')

                wo_model.save()
                
                messages.success(request, 'Successfully added workout!')
                return redirect(reverse('product_details', args=[product.id]))
            else:
                messages.error(request, 'Failed to add product. Please ensure the form is valid.')
        else:
            if form.is_valid():
                product = form.save()
                messages.success(request, 'Successfully added product!')
                return redirect(reverse('product_details', args=[product.id]))
            else:
                messages.error(request, 'Failed to add product. Please ensure the form is valid.')
    else:
        form = ProductForm()
        workout_form = WorkoutProgramForm()

    template = 'products/add_product.html'
    context = {
        'form': form,
        'workout_form': workout_form,
    }

    return render(request, template, context)

@login_required
def edit_product(request, product_id):
    """ Edit a product in the store """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    product = get_object_or_404(Product, pk=product_id)
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully updated product!')
            return redirect(reverse('product_details', args=[product.id]))
        else:
            messages.error(request, 'Failed to update product. Please ensure the form is valid.')
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
    """ Delete a product from the store """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    product = get_object_or_404(Product, pk=product_id)
    product.delete()
    messages.success(request, 'Product deleted!')
    return redirect(reverse('products'))