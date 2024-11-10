from django.db import models

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
    
class Cart(models.Model):
    items = models.ManyToManyField(Product, through=CartItem)
    total_price = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)
    def update_total_price(self):
        self.total_price = sum(item.product.price * item.quantity for item in self.cartitem_set.all)
        self.save()