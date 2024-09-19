from django.db import models
from user.models.user import User

class CustomerProfile(models.Model):
    customer = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    phone = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    gender = models.IntegerField()
    birthday = models.DateField()

    class Meta:
        db_table = 'customer_profile'

