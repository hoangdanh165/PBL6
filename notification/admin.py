from django.contrib import admin
from models.notification import Notification
from models.notification_user import NotificationUser


admin.register(Notification)
admin.register(NotificationUser)