# Generated by Django 4.2 on 2023-07-09 14:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0006_profile_verified'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='code',
            field=models.CharField(blank=True, default='', max_length=6, null=True),
        ),
    ]
