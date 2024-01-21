from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.contrib import messages
from accounts.form import CustomUserCreationForm
from .models import RegistrationModel

# Create your views here.

def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = False
            user.save()

            subject = 'Verify Your Email'
            message = render_to_string('verification_email.html', {
                'user': user,
                'domain': request.get_host(),
                'uid': user.id,
            })
            plain_message = strip_tags(message)
            from_email = 'balababa01@gmail.com'
            to_email = form.cleaned_data.get('email')
            send_mail(subject, plain_message, from_email, [to_email], html_message=message)

            messages.success(request, 'Account created successfully. Please check your email to verify your account.')
            return redirect('login')
    else:
        form = CustomUserCreationForm()

    return render(request, 'register.html', {'form': form})

@login_required
def home(request):
    return render(request, 'home.html')


def verify_email(request, uid):
    user = get_object_or_404(RegistrationModel, id=uid)
    if not user.is_verified:
        user.is_verified = True
        user.save()
        messages.success(request, 'Email verified. You can now log in.')
    else:
        messages.warning(request, 'Email already verified.')

    return redirect('login')

