from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.db.models import F

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
    image = models.ImageField(
        upload_to='images/', default='../default_upload_wck8zz', blank=True
    )
    class Meta:
        ordering = [F('due_date').asc(nulls_last=True)]

    def __str__(self):
        return f'{self.id} {self.title}'

    def is_overdue(self):
        return self.due_date and self.due_date < timezone.now().date()
    
    def save(self, *args, **kwargs):
        if not self.image:
            self.image = '../default_upload_wck8zz'
        self.overdue = self.is_overdue()
        super().save(*args, **kwargs)