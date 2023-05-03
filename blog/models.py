from django.db import models
from django.contrib.auth.models import User
from rules.text_validators import BLOG_COMMENT_PATTERN


# Create your models here.


class Blog(models.Model):
    id = models.AutoField(primary_key=True, null=False, blank=False)
    user_id = models.ForeignKey(User, null=False, blank=False, on_delete=models.CASCADE)
    name = models.CharField(max_length=50, null=False, blank=False)
    email = models.EmailField(max_length=100, null=False, blank=False)
    comment = models.TextField(max_length=1000, null=False, blank=False, validators=[BLOG_COMMENT_PATTERN,])
    date_time = models.DateTimeField(auto_created=True, null=False, blank=False)
    def __str__(self):
        return f'id = {self.id}, user = {self.user_id.username}, comment = {self.comment[:20]}...'

