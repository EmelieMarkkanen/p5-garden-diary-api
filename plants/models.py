from django.db import models
from django.contrib.auth.models import User

class Plants(models.Model):
    
    plant_type_choices = [
        ('unknown', 'Unknown'),
        ('berry_bush', 'Berry bush'),
        ('herb', 'Herb'),
        ('bulb', 'Bulb'),
        ('cacti', 'Cacti'),
        ('fern', 'Fern'),
        ('grass', 'Grass'),
        ('shrub', 'Shrub'),
        ('tree', 'Tree'),
        ('annual', 'Annual'),
        ('biennial', 'Biennial'),
        ('perennial', 'Perennial'),
        ('vegetable', 'Vegetable'),
        ('fruit_tree', 'Fruit tree'),
        ('succulent', 'Succulent'),
    ]

    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    plant_type = models.CharField(max_length=255, choices=plant_type_choices, null=True, blank=True, default='')
    planted_at = models.DateField(null=True, blank=True)
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