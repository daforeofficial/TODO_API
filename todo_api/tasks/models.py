from django.db import models
from django.contrib.auth.models import User

# Model for the task yahan hy
class Task(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    deadline = models.DateTimeField()
    priority = models.CharField(max_length=10, choices=(('low', 'Low'), ('medium', 'Medium'), ('high', 'High')))
    is_completed = models.BooleanField(default=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
