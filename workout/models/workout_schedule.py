from django.db import models
from user.models import User
from .exercise import Exercise


class WorkoutSchedule(models.Model):
    customer = models.OneToOneField(User, on_delete=models.CASCADE)
    coach = models.ForeignKey(User, related_name='workout_coach', on_delete=models.CASCADE)
    exercise = models.ForeignKey(Exercise, related_name='exercise', on_delete=models.CASCADE)
    date = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()
    duration = models.IntegerField()
    overview = models.TextField()

