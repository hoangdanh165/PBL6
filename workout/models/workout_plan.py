from django.db import models
from user.models import User


class WorkoutPlan(models.Model):
    customer = models.ForeignKey(User, related_name="workout_plans", on_delete=models.CASCADE)
    coach = models.ForeignKey(User, related_name="working_on", on_delete=models.CASCADE)
    start_date = models.DateField()
    expire_date = models.DateField()
    details = models.JSONField()
