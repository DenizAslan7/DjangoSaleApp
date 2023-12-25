from django.shortcuts import render , redirect
from . import models
from django.urls import reverse , reverse_lazy
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import CreateView


class SignUpView(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"



    
def listsale(request):
    sales = models.Sale.objects.all()
    return render(request , "storeapp/listsale.html" , context={"sales":sales} )


@login_required(login_url="/login")
def addsale(request):
    if request.POST:
        title = request.POST["title"]
        description = request.POST["description"]
        price = request.POST["price"]
        models.Sale.objects.create(username=request.user,title=title,description=description,price=price)
        return redirect(reverse("listsale"))
    else:
   
        return render(request, "storeapp/addsale.html" )
    
@login_required(login_url="/login")
def deletesale(request,id):
    sale = models.Sale.objects.get(pk=id)
    if request.user == sale.username:
        models.Sale.objects.filter(id=id).delete()
        return redirect(reverse("listsale"),)
    
@login_required(login_url="/login")
def addcart(request,id):
    sale = models.Sale.objects.get(pk=id)
    models.shop.objects.create(username=request.user,saler=sale.username,title=sale.title,description=sale.description,price=sale.price)
    return redirect(reverse("mycart"))
    
@login_required(login_url="/login")
def mycart(request):
    username = request.user
    items = models.shop.objects.filter(username=username).all()
    total_price = sum(item.price for item in items)
    return render(request,"storeapp/mycart.html",context={"items":items,"total_price":total_price})


@login_required(login_url="/login")
def deleteshop(request,id):
    sale = models.shop.objects.get(pk=id)
    if request.user == sale.username:
        models.shop.objects.filter(id=id).delete()
        return redirect(reverse("mycart"),)