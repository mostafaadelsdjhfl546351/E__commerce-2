from django.shortcuts import render,redirect
from .models import category,product,order
from django.contrib.auth.decorators import login_required
# Create your views here.
from . import views

def home(request):
    allcategory = category.objects.all()
    allproducts = product.objects.all()
    return render(request,'pages/home.html',{"allproducts":allproducts,"allcategory":allcategory})

def Category(request,categoryid):
    allcategory = category.objects.all()
    mycategory = category.objects.get(id=categoryid)
    allproducts = product.objects.all().filter(category_id = categoryid )
    return render(request,'pages/product_list.html',{"allproducts":allproducts,"allcategory":allcategory,"mycategory":mycategory})

def Product(request,productid):
    allcategory = category.objects.all()
    myproduct = product.objects.get(id=productid)
    return render(request,'pages/product.html',{"allcategory":allcategory,"myproduct":myproduct})

def AllCategories(request):
    allcategory = category.objects.all().order_by("-id")
    return render(request,'pages/category.html',{"allcategory":allcategory})

@login_required(login_url='/login/')
def addcart(request,proid):
    quantity=int(order.objects.filter(productid=proid).count())
    if quantity >= 1:
        ca=order.objects.get(productid=proid)
        order.objects.filter(productid=proid).update(num=int(ca.num)+1)
    else:
        id = request.user.id
        carts=order(productid=proid,user_id=id,num=1)
        carts.save()
    return redirect("/cartitem/")

@login_required(login_url='/login/')
def deleteitem(request,proid):
    item=order.objects.get(id=proid)
    item.delete()
    return redirect("/cartitem/")

@login_required(login_url='/login/')
def cartitem(request):
    quantity = 0
    price =0
    products = product.objects.all()
    orderss = order.objects.filter(user_id=request.user.id)
    for v in orderss:
        quantity=quantity+int(v.num)
        for f in product.objects.all():
            if v.productid ==f.id:
                price =price +(int(f.price)*int(v.num))
    return render(request, 'pages/cartitem.html',{"products":products,'quantity':quantity,"price":price,"orders":orderss})
