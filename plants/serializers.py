from rest_framework import serializers
from .models import Plants

class PlantsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Plants
        fields = ['id', 'name', 'type', 'planted', 'perennial', 'care_instructions', 'created_at', 'updated_at', 'image']

class PlantsDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Plants
        fields = ['id', 'name', 'type', 'planted', 'perennial', 'care_instructions', 'created_at', 'updated_at', 'image']
