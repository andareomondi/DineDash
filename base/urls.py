from django.urls import path
from .views import *
urlpatterns = [
    path('add-to-cart/', add_to_cart, name='add'),
    path('remove-from-cart/', remove_from_cart, name='remove'),
    path('checkout/', checkout, name='checkout'),
    path('register/', register, name='register'),
    path('login/', login, name='login'),
]