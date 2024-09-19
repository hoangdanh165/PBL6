from django.db import models

class Exercise(models.Model):
    name = models.CharField(max_length=255)
    duration = models.IntegerField()
    repetitions = models.CharField(max_length=255)
    image_url = models.TextField()

    class Meta:
        db_table = 'exercise'

