from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=300)
    price = models.DecimalField(max_digits=10,decimal_places=2)
    stock = models.PositiveIntegerField()
    description = models.TextField()

    def __str__(self):
        return self.name

class Order(models.Model):
    user_info = models.CharField(max_length=300)
    product = models.ManyToManyField(Product)
    total_price = models.DecimalField(max_digits=10,decimal_places=2)

    def __str__(self):
        return self.user_info
