from django.shortcuts import render, redirect
from django.contrib.auth import login
from .forms import SignUpForm


# Create your views here.


def index(request):
    return render(request, 'default/index.html')


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            selected_opt = form.cleaned_data.get('is_buyer')
            if selected_opt:
                user.is_Buyer = True
                user.is_Seller = False

            else:
                user.is_Seller = True
                user.is_Buyer = False

            user.save()
            login(request, user)

            return redirect('index')
    else:
        form = SignUpForm()
    return render(request, 'default/signup.html', {'form': form})