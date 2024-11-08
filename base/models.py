from django.db import models

# Create your models here.
class Item(models.Model):
    name = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    description = models.TextField()
    image = models.ImageField(upload_to='items/images/')
    def __str__(self):
        return self.name
