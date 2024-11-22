from django.shortcuts import render
from django.views import View
from .models import Product
from django.http import JsonResponse
from .models import *
# Create your views here.
class Home(View):
    def get(self, request):
        items = Product.objects.all()
        if not hasattr(request.user, 'cart'):
            cart = Cart.objects.create(user = request.user)
            print(cart.id)
        else:
            cart = request.user.cart
            print(cart.id)
            # Assuming you have a cart instance
            cart = Cart.objects.get(id=cart.id)
            cart.update_total_price()
            print(cart.total_price) 
             # This will print the updated total price
            total_unique_items = cart.total_unique_products()
        context = {
            'items':items,
            'cart': cart,
            'total_items': total_unique_items,
        }
        return render(request, 'base/index.html', context=context)
    def post(self, request):
        value = request.POST.get('value')
        cart = Cart.objects.get(id=cart.id)
        print(value)
        return render(request, 'base/index.html')
    
class Test(View):
    def get(self, request):
        data = {
            'name': 'John',
        }
        return JsonResponse(data)

