from django.db import models
from user.models.user import User


class CoachProfile(models.Model):
    coach = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    phone = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    gender = models.IntegerField()
    birthday = models.DateField()
    height = models.FloatField()
    weight = models.FloatField()
    start_date = models.DateField()
    extra_data = models.JSONField()

    class Meta:
        db_table = 'coach_profile'

