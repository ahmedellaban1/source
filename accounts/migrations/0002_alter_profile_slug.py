# Generated by Django 4.2 on 2023-05-02 14:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='slug',
            field=models.SlugField(blank=True, null=True),
        ),
    ]
