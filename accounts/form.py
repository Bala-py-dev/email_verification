from django import forms
from .models import RegistrationModel

# Create your form here.

class CustomUserCreationForm(forms.ModelForm):

    class Meta:
        model = RegistrationModel
        fields = ('name', 'email', 'password')
