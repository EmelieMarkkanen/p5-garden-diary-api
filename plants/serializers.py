from rest_framework import serializers
from .models import Plants


class PlantsSerializer(serializers.ModelSerializer):
    """Serializer for the Plant model."""
    class Meta:
        model = Plants
        fields = [
            'id',
            'name',
            'plant_type',
            'planted_at',
            'care_instructions',
            'created_at',
            'updated_at',
            'image']


class PlantsDetailSerializer(serializers.ModelSerializer):
    """Serializer for the detailed Plant model."""
    class Meta:
        model = Plants
        fields = [
            'id',
            'name',
            'plant_type',
            'planted_at',
            'care_instructions',
            'created_at',
            'updated_at',
            'image']
