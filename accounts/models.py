from django.db import models
from datetime import datetime

# Create your models here.

class RegistrationModel(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=255)
    is_verified = models.BooleanField(default=False)
    created_at = models.DateTimeField(default=datetime.now, blank=True)

    class Meta:
        db_table = 'signup_tbl'

    def __str__(self):
        return f"{self.name}"
