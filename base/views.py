from django.shortcuts import render
from django.views import View
from django.http import JsonResponse, HttpResponse
from .models import *
# Create your views here.
class Home(View):
    def get(self, request):
        if request.user.is_authenticated:
                
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
            return render(request, 'base/home.html', context=context)
        else:
            items = Product.objects.all()
            context = {
                'items':items
            }
            return render(request, 'base/home2.html', context=context)

# function based views to handle the crud operations and serve them using ajax
def add_to_cart(request):
    pass

def remove_from_cart(request):
    pass

def checkout(request):
    pass

def login(request):
    pass

def register(request):
    pass


