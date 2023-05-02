from django.contrib import admin
from .models import (
    Order,
    Billing,
    OrderBilling,
)
# Register your models here.

admin.site.register(Order)
admin.site.register(Billing)
admin.site.register(OrderBilling)
