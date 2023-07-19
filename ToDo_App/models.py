from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Task(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True) # null=True, blank=True allows for no user to be assigned to a task
    title = models.CharField(max_length=200) # max_length is required
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    completed = models.BooleanField(default=False)