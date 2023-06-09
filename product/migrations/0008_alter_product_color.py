# Generated by Django 4.2 on 2023-05-03 00:36

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0007_alter_product_color'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='color',
            field=models.CharField(max_length=23, validators=[django.core.validators.RegexValidator(code='ivalid_hexa_number', message='This field must contain at least one color and at most 3 colors in hexa format #XXXXXX', regex='^(#([A-Fa-f0-9]{6}|[A-Fa-f0-9]{3})(,|$))+')]),
        ),
    ]
