# Generated by Django 4.2 on 2023-05-02 13:52

from django.db import migrations, models
import rules.file_uploder


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='productimage',
            name='image',
            field=models.ImageField(default=1, upload_to=rules.file_uploder.wrapper),
            preserve_default=False,
        ),
    ]
