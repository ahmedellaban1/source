from django.urls import path, include
from .views import index, product_shop

app_name = "product"
urlpatterns = [
    path('',index, name='home-page'),
    path('shop',product_shop, name='shop'),
]
