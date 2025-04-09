from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Country(models.Model):

    country_name = models.CharField()


class Address(models.Model):
    street_number = models.CharField(max_length=100)
    address_line1 = models.CharField(max_length=100)
    address_line2 = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    region = models.CharField()
    postal_code = models.CharField(max_length=100)
    country_id = models.ForeignKey(Country, on_delete=models.CASCADE)


class UserAddress(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    address_id = models.ForeignKey(Address, on_delete=models.CASCADE)
    is_defult = models.BooleanField(default=False)

    
