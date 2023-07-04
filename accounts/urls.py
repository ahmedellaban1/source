from django.urls import path
from .views import signup_view, login_view, email_verification
app_name = 'accounts'
urlpatterns = [
    path('register/', signup_view, name='sign-up'),
    path('register/login/', login_view, name='login'),
    path('register/email_verification/<str:email>', email_verification, name='email_verification'),
]
