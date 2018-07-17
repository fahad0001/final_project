from django.core.paginator import  Paginator
from django.shortcuts import render, redirect
from django.contrib.auth import login
from .forms import SignUpForm, ContactUsForm
from products.models import Product
from .models import Contact


# Create your views here.


def index(request):
    return render(request, 'default/index.html')


def home(request):
    main_products = Product.objects.all()
    paginator = Paginator(main_products, 9)

    page = request.GET.get('page')
    products = paginator.get_page(page)
    query = request.GET.get("q")
    if query:
        main_products = main_products.filter(name__icontains=query)
    return render(request, 'Index/home.html', {'main_products': main_products, 'products': products})


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

            return redirect('home')
    else:
        form = SignUpForm()
    return render(request, 'Index/signup.html', {'form': form})


def contact_us(request):
    form = ContactUsForm()
    if request.method == 'POST':
        form = ContactUsForm(request.POST)
        if form.is_valid():
            form.save()

            return redirect('home')

        else:
            form = ContactUsForm()
    return render(request, 'Index/contact_us.html', {'form': form})


def view_contacts(request):
    contacts = Contact.objects.all()
    return render(request,'default/contact_us.html',{'contacts': contacts})