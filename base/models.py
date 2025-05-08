from django.db import models
from django.contrib.auth.models import User, AbstractUser

# model for customers or users
class Customer(models.Model):
    name = models.CharField(max_length=150, blank=False, null=False, unique=False)
    email = models.EmailField(max_length=150, unique=False, blank=False, null=False)
    phone_number =models.IntegerField( unique=True, blank=True, null=True)
    address =models.TextField(max_length=1000, blank=True)

# creating a customuser class

class CustomUser(AbstractUser):
    email = models.EmailField(('Email Address'), unique=True, blank=False, null= False)

    # custom fileds
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    address = models.TextField(null=True, blank=True)

    # both email and username as required fields which will be used later to authenticate user
    REQUIRED_FIELDS = ['email']

    def __str__(self):
        return self.email
        