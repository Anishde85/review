from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
class MyModelName(models.Model):
    title = models.CharField(max_length=100)
    content=models.TextField(max_length=200)
    date_posted=models.DateTimeField(default=timezone.now)
    author=models.ForeignKey(User, on_delete=models.CASCADE)
    class Meta:
        ordering = ['title']
    def __str__(self):
        return self.title