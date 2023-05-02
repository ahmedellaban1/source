from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify
from rules.choices_tuples import (
    SIZE_TUPLE,
)
from rules.file_uploder import (
    image_uploder,
)
# from django.core.validators import RegexValidator
# TODO: RegexValidator 
# Create your models here.



class Category(models.Model):
    id = models.AutoField(primary_key=True, null=False, blank=False)
    title = models.CharField(max_length=50, null=False, blank=False)

    def __str__(self):
        return f'id = {self.id}, title = {self.title}'
    


class Product(models.Model):
    id = models.AutoField(primary_key=True, null=False, blank=False)
    title = models.CharField(max_length=50, null=False, blank=False)
    description = models.TextField(null=False, blank=False)
    price = models.DecimalField(max_digits=7, decimal_places=2)
    color = models.CharField(max_length=7, null=False, blank=False)
    size = models.CharField(max_length=3, choices=SIZE_TUPLE, default=SIZE_TUPLE[0][0])
    slug = models.SlugField(null=True, blank=True)
    category_id = models.ForeignKey('Category', null=False, blank=False, on_delete=models.DO_NOTHING)

    def save(self, *args, **kwargs):
        self.slug = ''
        text = f'{self.category_id.title} {self.title} {self.description[:20]} {self.id}'
        self.slug = slugify(text)
        super(Product, self).save(*args, **kwargs)

    def __str__(self):
        return f'id = {self.id}, title = {self.title}, description = {self.description[:20]}...'
    

class ProductImage(models.Model):
    id = models.AutoField(primary_key=True, null=False, blank=False)
    product_id = models.ForeignKey(Product, null=False, blank=False, on_delete=models.CASCADE)
    image = models.ImageField(upload_to=image_uploder(class_name='product'), null=False, blank=False)

    def __str__(self):
        return f'id = {self.id}, product = {self.product_id.title}'


class Review(models.Model):
    id = models.AutoField(primary_key=True, null=False, blank=False)
    product_id = models.ForeignKey(Product, null=False, blank=False, on_delete=models.CASCADE)
    user_id = models.ForeignKey(User, null=False, blank=False, on_delete=models.CASCADE)
    date_time = models.DateTimeField(auto_created=True, null=False, blank=False)
    review = models.TextField(max_length=200, null=False, blank=False)

    def __str__(self):
        return_review = f'id = {self.id}, product_id = {self.product_id.id}, '
        return return_review + f' user = {self.user_id.username}, review = {self.review[:20]}...'