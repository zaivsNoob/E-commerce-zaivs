from django.shortcuts import render,redirect

from django.http import JsonResponse,HttpResponse
from .models import *
import json
from .forms import ShippingForm,RegistrationForm
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from .decoretors import *

# Things to do next
#style the pages and test
@Authenticated
def registerView(request):
    if request.method=="POST":
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        if password1 ==password2:
                
            # Create the new user
            user = User.objects.create_user(username=username, email=email, password=password1)
            
            # Create the associated Customer object
            customer = Customer.objects.create(user=user, name=username, email=email)

            # Redirect to the homepage or login page
            user=authenticate(request,username=username,password=password1)
            login(request,user)
            return redirect('/')
        else:
           messages.error(request, 'Passwords do not match. Please try again.')
           return render(request,"store/register.html")

    else:

        form=RegistrationForm()
        
        context={'form':form}
        return render(request,"store/register.html",context)
    

@Authenticated
def loginUser(request):
    
    if request.method=="POST":
        username=request.POST.get('username')
        password=request.POST.get('password')
        user=authenticate(request,username=username,password=password)
       
        if user is not None:
            
            login(request,user)
            return redirect('/')
        else:
            print("2")
            render("login")
        
    return render(request,'store/login_user.html')

def logoutUser(request):
    logout(request)
    return redirect('login')


def storeView(request):
    search_query = request.GET.get('search', '')
    products = Product.objects.filter(name__icontains=search_query)
    
    context = {
        'products': products,
        'search': search_query,
    }
    return render(request, 'store/store.html', context)


@login_required(login_url="store")
def cartView(request):
    
    if request.user.is_authenticated:
        customer=request.user.customer
        order,created=Order.objects.get_or_create(customer=customer,completed=False)

        items=order.orderitem_set.all()

            
        
        context={
            'items':items
        }
        
    else:
        items=[]
    context={'items':items}        
    return render(request,'store/cart.html',context)

def checkoutView(request):
    if request.user.is_authenticated:
        customer=request.user.customer
        order,created=Order.objects.get_or_create(customer=customer,completed=False)
        
        items=order.orderitem_set.all()
        total = sum(item.get_total() for item in items)
        
        form=ShippingForm(request.user,order.id)

    if request.method=="POST":
       
        form=ShippingForm(request.user,order.id,request.POST)
        if form.is_valid():
            form.save()
            order.completed=True
            order.save()
            return redirect("/")

    context={
            'items':items,
            'form':form,
            'total':total
        }
       
        
    return render(request,'store/checkout.html',context)


def updateItem(request):
    data=json.loads(request.body)
    productId=data['product id']
    action=data['action']

   
    customer=request.user.customer
    product=Product.objects.get(id=productId)
    order,created=Order.objects.get_or_create(customer=customer,completed=False)
    orderItem,created=OrderItem.objects.get_or_create(order=order,product=product)
    
    if action=='add':
        orderItem.quantity=(orderItem.quantity+1)
    elif action=='remove':
         orderItem.quantity=(orderItem.quantity-1)
    orderItem.save()
    if orderItem.quantity<=0 :
        orderItem.delete()       
    return JsonResponse('item has been updated',safe=False)