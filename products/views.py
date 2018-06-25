from django.shortcuts import render, redirect
from .forms import NewPro
# Create your views here


def pro(request):
    form = NewPro()
    if request.method == 'POST':
        form = NewPro(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('stores_list')

        else:
            form = NewPro()
    return render(request, "default/add_product.html", {'form': form})


def product_list(request):
    return render(request, 'default/product_list.html')