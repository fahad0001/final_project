from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import NewStore
from .models import Store


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
    my_stores = Store.objects.all().filter(user=request.user)
    print(my_stores)
    return render(request, "default/stores_list.html", {'my_list': my_stores})


@login_required()
def store_details(request):
    return render(request, "default/store_details.html")
