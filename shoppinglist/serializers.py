from rest_framework import serializers
from .models import Item

class ItemSerializer(serializers.ModelSerializer):
    """Serializer for the Item model."""
    class Meta:
        model = Item
        fields = ['id', 'name', 'quantity', 'created_at', 'updated_at']

class ItemDetailSerializer(serializers.ModelSerializer):
    """Serializer for the detailed Item model."""
    class Meta:
        model = Item
        fields = ['id', 'name', 'quantity', 'created_at', 'updated_at']
