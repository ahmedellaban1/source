from django.shortcuts import render, redirect, reverse
from .forms import (
    SignUpForm,
    LoginForm,
    VerificationCode,
    User
)
from rules.validator_functions import verification_code
# Create your views here.
# TODO: each function must have app_name variable sent in context cause it appear in title



def signup_view(request):
    form = SignUpForm(request.POST)
    if form.is_valid():
        form.save(commit=False)
        form.is_active = False
        email = form.data['email']
        form.save()
        return True
        # return redirect(reverse('accounts:email_verification',kwargs={'email':email} ))
    else:
        form = SignUpForm()

    context = {
        'form': form,
        'app_name': 'SignUp',
    }
    return render(request, 'register/signup.html', context=context)


# def email_verification(request,email):
#     user = User.objects.get(email=email)
#     code = verification_code(email)
#     form = VerificationCode(request.POST)
#     print(form.data['code'])
#     if form.is_valid():
#         if form.data['code'] == code:
#             print(f"code- form = {form.data['code']} ----- {code}")
#             user.objects.update(is_active=True)
#             return redirect(reverse('accounts:login'))
#     else:
#         form = VerificationCode()

#     context = {
#         'form': form,
#         'app_name': 'Verification Code',
#     }

#     return render(request, 'register/verification_code.html', context=context)


def login_view(request):
    form = LoginForm(request.POST)
    if form.is_valid():
        return True  #TODO: this must redirect user to home page
    else:
        form = LoginForm()
    context = {
        'form': form,
        'app_name': 'Login',
    }
    return render(request, 'register/login.html', context=context)
