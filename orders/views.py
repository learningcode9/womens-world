from django.shortcuts import render,redirect
from django.urls import reverse
from .models import OrderItem
from .forms import OrderCreateForm
from cart.cart import Cart

from django.contrib.auth.decorators import login_required 
from shop.forms import signupForm,loginForm
from shop.views import Signup,login
import json
# Create your views here.
@login_required
def order_create(request):
    cart = Cart(request)
   
    if request.method == 'POST':
        form = OrderCreateForm(request.POST)
        if form.is_valid():
            order = form.save()
            for item in cart:
                OrderItem.objects.create(
                    order=order,
                    product=item['product'],
                    price=item['price'],
                    quantity=item['quantity']
                )
            cart.clear()
        # return render(request, 'shop/product/created.html', {'order': order})
            #launch asynchronous task
            # order_created.delay(order.id)
            #set the order in the session
            request.session['order_id']=order.id
            #redirect to the payment
            return redirect (reverse('payments:process'))
    else:
        form = OrderCreateForm()
    return render(request, 'shop/product/create.html', {'form': form})


