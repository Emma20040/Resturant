from django.db import models
from django.contrib.auth.models import User


# model for customers or users
class Customer(models.Model):
    name = models.CharField(max_length=150, blank=False, null=False, unique=False)
    email = models.EmailField(max_length=150, unique=False, blank=False, null=False)
    phone_number =models.IntegerField( unique=True, blank=True, null=True)
    address =models.TextField(max_length=1000, blank=True)