from django.db import models
from user.models.user import User


class CoachProfile(models.Model):
    coach = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.TextField()
    last_name = models.TextField()
    phone = models.TextField()
    address = models.TextField()
    gender = models.IntegerField()
    birthday = models.DateField()
    height = models.FloatField()
    weight = models.FloatField()
    start_date = models.DateField()
    extra_data = models.JSONField()
