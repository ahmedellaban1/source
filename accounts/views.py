from django.shortcuts import render, redirect, reverse
from .forms import SignUpForm, LoginForm,VerificationCode
from .models import Profile
# from rules.validator_functions import verification_code, verify_email
from django.contrib.auth import authenticate


def signup_view(request):
    form = SignUpForm(request.POST)
    if form.is_valid():
        form.save()
        return redirect(reverse('accounts:login'))
    else:
        form = SignUpForm()
    context = {
        'form': form,
        'app_name': 'SignUp',
    }
    return render(request, 'registration/signup.html', context=context)


def email_verification(request):
    code_form = VerificationCode(request.POST)
    if code_form.is_valid():
        return redirect(reverse('accounts:login'))
    else:
        code_form = VerificationCode()
    context = {
        "form": code_form,
        "app_name": 'register | validate your email'
    }
    return render(request, 'registration/verification_code.html', context=context)



# def login_view(request):
#     form = LoginForm(request.POST)
#     if form.is_valid():
#         authenticate(username=form.data['username'], password=form.data['password'])
#         return redirect(reverse('accounts:login'))
#     else:
#         form = LoginForm()
#     context = {
#         'form': form,
#         'app_name': 'Login',
#     }
#     return render(request, 'registration/login.html', context=context)
