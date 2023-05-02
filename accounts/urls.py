from django.urls import path, include
from .views import signup_view

urlpatterns = [
    path('register/', signup_view, name='sign-up'),
]
