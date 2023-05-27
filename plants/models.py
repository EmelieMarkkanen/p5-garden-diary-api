from django.db import models
from django.contrib.auth.models import User

class Plants(models.Model):

    YES = 'Yes'
    NO = 'No'
    YES_NO_CHOICES = [
        (True, YES),
        (False, NO),
    ]

    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    type = models.CharField(max_length=255)
    planted = models.DateField(null=True, blank=True)
    perennial = models.BooleanField(default=False, choices=YES_NO_CHOICES)
    care_instructions = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    image = models.ImageField(
        upload_to='images/', default='../default_upload_wck8zz', blank=True
    )

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f'{self.id} {self.name}'