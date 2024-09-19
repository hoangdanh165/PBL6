from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from user.models import User


class ServiceResponse(models.Model):
    customer = models.ForeignKey(User, related_name="responses", on_delete=models.CASCADE)
    coach = models.ForeignKey(User, related_name="ratings", on_delete=models.CASCADE)
    comment = models.TextField()
    score = models.IntegerField(
        validators=[
            MinValueValidator(1),
            MaxValueValidator(5)
        ]
    )

    class Meta:
        db_table = 'service_response'

