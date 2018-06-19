# from django.shortcuts import render, redirect, get_object_or_404
# from django.contrib.auth.decorators import login_required
# from django.core.exceptions import PermissionDenied

# from product.models import Products
# from .forms import InvitationForm
# from .models import Invitation

from django.http import HttpResponse


def index(request):
    return HttpResponse("This is store")


# @login_required
# def home(request):
#     import pdb
#     pdb.set_trace()
#     my_products = Products.objects.product_for_user(request)
#     active_products = my_products.active()
#     invitations = request.user.invitations_received.all()
#     return render(request, "store/index.html",
#                   {'products': active_products,
#                    'invitations': invitations})
#
#
# @login_required
# def new_invitation(request):
#     if request.method == "POST":
#         invitation = Invitation(from_user=request.user)
#         form = InvitationForm(instance=invitation, data=request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('store_home')
#     else:
#         form = InvitationForm()
#     return render(request,"store/new_invitation_form.html",{'form':form})
#
#
# @login_required()
# def accept_invitation(request, id):
#     invitation = get_object_or_404(Invitation, pk=id)
#     if not request.user == invitation.to_user:
#         raise PermissionDenied
