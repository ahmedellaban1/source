from django.shortcuts import render, redirect
from .forms import (
    SignUpForm,
    LoginForm,
)
# Create your views here.
# TODO: each function must have app_name variable sent in context cause it appear in title



def signup_view(request):
    form = SignUpForm(request.POST)
    if form.is_valid():
        form.save()
        return True  #TODO: this must redirect user to home page
    else:
        form = SignUpForm()

    context = {
        'form': form,
        'app_name': 'SignUp',
    }
    return render(request, 'register/signup.html', context=context)


def login_view(request):
    form = LoginForm(request.POST)
    if form.is_valid():
        form.save()
        return True  #TODO: this must redirect user to home page
    else:
        form = LoginForm()
    context = {
        'form': form,
        'app_name': 'Login',
    }
    return render(request, 'register/login.html', context=context)
    