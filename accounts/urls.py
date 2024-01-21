from django.urls import path
from .views import register, home, verify_email

urlpatterns = [
    path('register/', register, name='register'),
    path('home/', home, name='home'),
    path('verify-email/<int:uid>/', verify_email, name='verify_email'),
]