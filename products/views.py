from django.shortcuts import render, redirect
from .forms import NewPro, Product
from django.contrib.auth.decorators import login_required
# Create your views here


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
    return render(request, "default/add_product.html", {'form': form})


@login_required()
def product(request):
    return render(request, "default/product_details.html")