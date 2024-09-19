from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('message/', include('message.urls')),
    path('notification/', include('notification.urls')),
    path('payment/', include('payment.urls')),
    path('service/', include('service.urls')),
    path('user/', include('user.urls')),
    path('user-profile/', include('user_profile.urls')),
    path('workout/', include('workout.urls')),

]
