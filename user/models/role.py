from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

class Role(models.Model):
    id = models.AutoField(primary_key=True)
    role_name = models.CharField(max_length=255)
    permission = models.JSONField()

    def __str__(self):
        return self.role_name

    class Meta:
        db_table = 'role'
