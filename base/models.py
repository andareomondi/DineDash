from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.contrib.auth.base_user import BaseUserManager

# ------------------------------------

# creating a custom user model inheriting from the baseusermodel
# model to handle the properties of the user
class CustomerUserManager(BaseUserManager):
    def create_user(self, first_name, second_name, email, password=None):
        if not email:
            raise ValueError('User should have a email')
        if not first_name or not second_name:
            raise ValueError('User should have a first and second name')
        user = self.model(
            first_name=first_name,
            second_name=second_name,
            email=email,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, first_name, second_name, email, password=None):
        if not first_name or not second_name:
            raise ValueError('Superuser should have a first and second name')
        user = self.create_user(
            first_name=first_name,
            second_name=second_name,
            email=email,
            password=password,
        )
        user.is_admin = True
        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)
        return user

class Customer(AbstractBaseUser, PermissionsMixin):
    first_name = models.CharField(max_length=255)
    second_name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    is_superadmin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)

    objects = CustomerUserManager()
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'second_name']

    def __str__(self):
        return f'Customer#{self.id}: {self.first_name} {self.second_name}'

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
    user = models.OneToOneField(Customer, on_delete=models.CASCADE)
    items = models.ManyToManyField(Product, through='CartItem')
    total_price = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)

    def update_total_price(self):
        self.total_price = sum(item.product.price * item.quantity for item in self.cartitem_set.all())
        self.save()
    
    def total_unique_products(self): 
        return self.cartitem_set.count()
    
    def __str__(self):
        return f'Cart #{self.id}'
