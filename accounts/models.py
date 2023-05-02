from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

# TODO: RegexValidator 
# Create your models here.


class Profile(models.Model):
    id = models.AutoField(primary_key=True, null=False, blank=False)
    user_id = models.OneToOneField(User, on_delete=models.CASCADE)
    country = models.CharField(max_length=20, blank=False, null=False)
    phone = models.CharField(max_length=11, blank=False, null=False)
    date_of_birth = models.DateField(blank=True, null=True)
    slug = models.SlugField()  #TODO: slugify user_id.username and id from profile

    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user_id=instance)

    def __str__(self):
        return f"id={self.id}, user = {self.user_id.username}"


class Address(models.Model):
    id = models.AutoField(primary_key=True, null=False, blank=False)
    user_id = models.OneToOneField(User, on_delete=models.CASCADE)
    company = models.CharField(max_length=20, null=False, blank=False)

    def __str__(self):
        return f"id={self.id}, user = {self.user_id.username}, company = {self.company}"

