from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    description = models.TextField()
    image = models.ImageField(upload_to='items/images/')
    def __str__(self):
        return self.name

class CartItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    cart = models.ForeignKey('Cart', on_delete=models.CASCADE)
    def __str__(self):
        return f'Product #{self.product.id}'
    
class Cart(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, default='')
    items = models.ManyToManyField(Product, through='CartItem')
    total_price = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)

    def update_total_price(self):
        self.total_price = sum(item.product.price * item.quantity for item in self.cartitem_set.all())
        self.save()
    
    def total_unique_products(self): 
        return self.cartitem_set.count()
    
    def __str__(self):
        return f'Cart #{self.id}'
