from rest_framework import serializers
from .models import Plants

class PlantsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Plants
        fields = ['id', 'name', 'type', 'care_instructions', 'created_at', 'updated_at', 'planted', 'perennial', 'image']
