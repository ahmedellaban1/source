# Generated by Django 4.2 on 2023-05-03 00:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0009_alter_product_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False, unique=True),
        ),
    ]