from django.db import models


class Notification(models.Model):
    message = models.TextField()
    create_date = models.DateTimeField()
    params = models.JSONField()
    create_url = models.TextField()

    class Meta:
        db_table = 'notification'



