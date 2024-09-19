from django.db import models
from user.models.user import User

class CustomerProfile(models.Model):
    customer = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.TextField()
    last_name = models.TextField()
    phone = models.TextField()
    address = models.TextField()
    gender = models.IntegerField()
    birthday = models.DateField()

