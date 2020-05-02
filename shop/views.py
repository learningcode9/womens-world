from django.shortcuts import render,redirect, get_object_or_404
from .models import Category, Product
from cart.forms import CartAddProductForm
from django.conf import settings
from shop.forms import signupForm,loginForm
from django.contrib import messages
from django.contrib.auth.models import User,auth


# Create your views here.

def home(request):
    return render(request,'shop/product/home.html')

def dresses(request):

    categories = Category.objects.filter(name='dresses')
    products = Product.objects.filter(category_id=1)
    
  
    context = {
        'categories': categories,
        'products': products
    }

#    if 'customer' in request.session:
        # request.session[settings.CUSTOMER_SESSION_ID]['isLoggedin']=True
        # request.session.modified=True
    # else:
        #  request.session[settings.CUSTOMER_SESSION_ID]={}
        #  request.session[settings.CUSTOMER_SESSION_ID]['isLoggedin']=True
    
   


    return render(request, 'shop/product/dresses.html', context)


def product_detail(request, id, slug):
    product = get_object_or_404(Product, id=id, slug=slug, available=True)
    cart_product_form = CartAddProductForm()
    context = {
        'product': product,
        'cart_product_form': cart_product_form
    }
    return render(request, 'shop/product/detail.html', context)


def sarees(request):
    
    categories = Category.objects.filter(name='sarees')
    products = Product.objects.filter(category_id=2)
    
 
    context = {
        
        'categories': categories,
        'products': products
    }
    # if 'customer' in request.session:
        # request.session[settings.CUSTOMER_SESSION_ID]['isLoggedin']=True
        # request.session[settings.CUSTOMER_SESSION_ID]['isLoyal']=True
        # request.session.modified=True
    # else:
        # request.session[settings.CUSTOMER_SESSION_ID]={}
        #  request.session[settings.CUSTOMER_SESSION_ID]['isLoggedin']=True
        # request.session[settings.CUSTOMER_SESSION_ID]['isLoyal']=True
    
    # print('sarees',request.session.values())'''
    return render(request,'shop/product/sarees.html',context)
    
    

def lehangas(request):
    categories = Category.objects.filter(name='lehangas')
    products = Product.objects.filter(category_id=3)
    context = {
        
        'categories': categories,
        'products': products
    }
    return render(request,'shop/product/lehangas.html',context)

def Signup(request):
    if request.method == 'POST':
       
        form=signupForm(request.POST)#with the form data creating an object,when ever form submits then only this if part works.
        if  form.is_valid():#if form values are valid ,means without any errors
            
            first_name=form.cleaned_data['first_name'] #capturing the data from the form fields
            last_name=form.cleaned_data['last_name']
            username=form.cleaned_data['username']
            email=form.cleaned_data['email']
            password=form.cleaned_data['password']
            confirm_password=form.cleaned_data['confirm_password']
            user=User.objects.create_user(username=username,first_name=first_name,last_name=last_name,email=email,password=password)
            user.save()
            return redirect('/login')
            
    else:
        form=signupForm()
        response=render(request,'shop/product/signup.html',{'form':form})
        response.set_cookie('firstname','bellam')
        return response

def login(request):
    if request.method=='POST':
        form=loginForm(request.POST)
       
        if form.is_valid():
            username=form.cleaned_data['username']
            password=form.cleaned_data['password']
            
            user = auth.authenticate(username=username, password=password)
            
            if user is not None:
                auth.login(request,user)
                #messages.info(request, f"You are now logged in as {username}")
                return redirect('/')
            else: 
                messages.error(request, "Invalid username or password.")
                return redirect('login')
        
    else:
        form = loginForm()
        return render(request,"registration/login.html",{"form":form})


def Logout(request):
    auth.logout(request)
    return redirect("/")