# Generated by Django 4.2 on 2023-05-02 13:43

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='OrderBilling',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('date', models.DateField(auto_created=True)),
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('repetition', models.IntegerField()),
                ('total_price', models.DecimalField(decimal_places=2, max_digits=7)),
                ('status', models.CharField(choices=[('Pending', 'Pending'), ('Processing', 'Processing'), ('Completed', 'Completed'), ('Canceled', 'Canceled'), ('On Hold', 'On Hold')], default='Pending', max_length=15)),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Billing',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('full_name', models.CharField(max_length=60)),
                ('address', models.CharField(max_length=120)),
                ('ZIP_code', models.CharField(max_length=5)),
                ('card_number', models.IntegerField()),
                ('card_expiry', models.DateField()),
                ('card_CVC', models.CharField(max_length=20)),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]