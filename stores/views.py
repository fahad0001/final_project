from django.shortcuts import render, redirect
from .forms import NewStore


def store(request):
    form = NewStore()
    if request.method == 'POST':
        form = NewStore(request.POST)
        if form.is_valid():
            form = form.save()

            return redirect('stores_list')

        else:
            form = NewStore()
    return render(request, "default/store.html", {'form': form})


def stores_list(request):
    return render(request, "default/stores_list.html")


