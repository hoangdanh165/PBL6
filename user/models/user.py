from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from .role import Role

class UserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(email, password, **extra_fields)

class User(AbstractBaseUser):
    class Status(models.IntegerChoices):
        ACTIVE = 1, 'Active'
        BLOCKED = 2, 'Blocked'
        INVITED = 3, 'Invited'

    email = models.EmailField(max_length=100, unique=True)
    password = models.CharField(max_length=255)
    role = models.ForeignKey(Role, on_delete=models.CASCADE)
    status = models.IntegerField(choices=Status.choices, default=Status.ACTIVE)
    email_verified = models.BooleanField(default=False)
    avatar_url = models.TextField(null=True, blank=True)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email
    
    class Meta:
        db_table = 'user'


