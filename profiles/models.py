from django.db import models
from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.core.files.base import ContentFile
from django.core.files import File
from django.dispatch import receiver


class Profile(models.Model):
    owner = models.OneToOneField(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    name = models.CharField(max_length=255, blank=True)
    content = models.TextField(blank=True)
    image = models.ImageField(upload_to='images/', default='../default_profile_c36wy0')

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.owner}'s profile"


@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        profile = Profile.objects.create(owner=instance)
        if instance.profileImage:
            if profile.image.name != '../default_profile_c36wy0': 
                profile.image.delete()
            profile.image.save(
                instance.profileImage.name,
                instance.profileImage,
            )
        profile.save()