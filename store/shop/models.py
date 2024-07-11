from django.db import models

class Product(models.Model):
    title = models.CharField(max_length=255)#varchar255
    description = models.TextField()
    price = models.DecimalField(max_digits=6,decimal_places=2)
    inventory = models.IntegerField()
    last_update = models.DateTimeField(auto_now=True)


class Customer(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    #phone = models.harField(max_length=255)
    birth_date = models.DateField(null=True)