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
def edit_store(request, store_id):
    edit = get_object_or_404(Store, pk=store_id)
    form = NewStore(instance=edit)
    if request.method == 'POST':
        form = NewStore(request.POST, request.FILES, instance=edit)
        if form.is_valid():
            form.save()

            return redirect('store_details', store_id)
        else:
            form = NewStore(instance=edit)
    return render(request, "default/edit_store.html", {'form': form, 'edit': edit})



@login_required()
def delete_product(request, store_id):
    delete = get_object_or_404(Store, pk=store_id)
    form = NewStore(instance=delete)
    if request.method == 'POST':
        form = NewStore(request.POST, instance=delete)
        if form.is_valid():
            delete.delete()

            return redirect('stores_list')
    else:
            form = NewStore(instance=delete)
    return render(request, "default/delete_store.html", {'form': form, 'delete': delete})


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
    list_stores=Store.objects.all()
    return render(request, 'Index/store_list.html',{'list_stores': list_stores})


def details_store(request, store_id):
    store = get_object_or_404(Store, id=store_id)
    store_detail = store.products.all()
    get_store = Store.objects.get(id=store_id)
    return render(request, 'Index/store.html', {'store': store, 'store_detail': store_detail, 'get_store': get_store})