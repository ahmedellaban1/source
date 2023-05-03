from django.db import models
from django.contrib.auth.models import User
from product.models import Product
from rules.choices_tuples import (
    STATUS_TUPLE,
)
from rules.numbers_validators import (
    ZIP_CODE_VALIDATOR,
)

# Create your models here.

class Order(models.Model):
    id = models.AutoField(primary_key=True, null=False, blank=False)
    user_id = models.ForeignKey(User, null=False, blank=False, on_delete=models.CASCADE)
    product_id = models.ForeignKey(Product, null=False, blank=False, on_delete=models.CASCADE)
    date = models.DateField(auto_created=True ,null=False, blank=False)
    repetition = models.IntegerField(null=False, blank=False)
    total_price = models.DecimalField(decimal_places=2, max_digits=7, null=False, blank=False)
    status = models.CharField(max_length=15, choices=STATUS_TUPLE, default=STATUS_TUPLE[0][0])

    def __str__(self):
        return f'id = {self.id}, user_id = {self.user_id.username}, status = {self.status}'


class Billing(models.Model):
    id = models.AutoField(primary_key=True, null=False, blank=False)
    user_id = models.ForeignKey(User, null=False, blank=False, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=60, null=False, blank=False)
    address = models.CharField(max_length=120, null=False, blank=False)
    ZIP_code = models.CharField(max_length=5,null=False, blank=False, validators=[ZIP_CODE_VALIDATOR, ])
    card_number = models.IntegerField(null=False, blank=False)
    card_expiry = models.DateField(null=False, blank=False)
    card_CVC = models.CharField(max_length=20, null=False, blank=False)

    def __str__(self):
        return f'id = {self.id}, user_id = {self.user_id.username}, full_name = {self.full_name}'
    

class OrderBilling(models.Model):
    id = models.AutoField(primary_key=True, null=False, blank=False)
    oreder_id = models.ForeignKey('Order', on_delete=models.SET_NULL, null=True)
    billing_id = models.ForeignKey('Billing', on_delete=models.CASCADE)

    def __str__(self):
        return f'id = {self.id}, oreder_id = {self.oreder_id}, billing_id = {self.billing_id}'

