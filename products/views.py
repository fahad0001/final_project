from django.shortcuts import render, redirect, get_object_or_404
from .forms import NewPro, Product
from django.contrib.auth.decorators import login_required
# Create your views here


@login_required()
def pro(request):
    form = NewPro()
    if request.method == 'POST':
        form = NewPro(request.POST, request.FILES)
        if form.is_valid():
            entry = form.save(commit=False)
            entry.user = request.user
            entry.save()

            return redirect('add_products')

        else:
            form = NewPro()
    return render(request, "default/../templates/add_product.html", {'form': form})


@login_required()
def product(request, product_id):
    print(product_id)
    details = get_object_or_404(Product, id=product_id)
    product_details = Product.objects.get(id=product_id)
    print(product_details)
    return render(request, "default/product_details.html", {'details': details, 'product_details': product_details})


def index_products(request):
    return render(request, "Index/Products.html")