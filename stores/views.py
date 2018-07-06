from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .forms import NewStore
from .models import Store


@login_required()
def store(request):
    form = NewStore()
    if request.method == 'POST':
        form = NewStore(request.POST)
        if form.is_valid():
            entry = form.save(commit=False)
            entry.user = request.user
            entry.save()

            return redirect('stores_list')

        else:
            form = NewStore()
    return render(request, "default/store.html", {'form': form})


@login_required()
def stores_list(request):
    stores = Store.objects.all().filter(user=request.user)
    return render(request, "default/stores_list.html", {'stores': stores})


@login_required
def store_details(request, store_id):
    print(store_id)
    store = get_object_or_404(Store, id=store_id)
    store_products = store.products.all()
    return render(request, 'default/store_details.html', {'store': store, 'store_products': store_products})


def index_stores(request):
    return render(request, 'Index/Stores.html')