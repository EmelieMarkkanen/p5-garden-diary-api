from django.db import models
from django.contrib.auth.models import User

class Task(models.Model):
    """
    Task model, owner relates to the user model, used to 
    associate each task with a specific user.
    Set created at and updated at date, task can be set as over due.
    """
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    title = models.CharField(max_length=255)
    content = models.TextField(max_length=600, blank=True)
    due_date = models.DateField(null=True, blank=True)
    overdue = models.BooleanField(default=False)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.name