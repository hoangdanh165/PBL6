from django.db import models
from user.models import User


class WorkoutGoal(models.Model):
    customer = models.OneToOneField(User, on_delete=models.CASCADE)
    coach = models.ForeignKey(User, related_name="customer_workout_goal", on_delete=models.CASCADE)
    weight = models.FloatField()
    extra_data = models.JSONField()

    class Meta:
        db_table = 'workout_goal'


