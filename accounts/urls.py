from django.urls import path, include
from .views import signup_view, login_view

urlpatterns = [
    path('register/', signup_view, name='sign-up'),
    path('register/login/', login_view, name='login'),
]
