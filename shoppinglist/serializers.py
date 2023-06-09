from rest_framework import serializers
from .models import Item

class ItemSerializer(serializers.ModelSerializer):
    """Serializer for the Item model."""
    class Meta:
        model = Item
        fields = ['name', 'quantity']


class ItemDetailSerializer(serializers.ModelSerializer):
    """Serializer for the detailed Item model."""
    class Meta:
        model = Item
        fields = ['item', 'quantity', 'owner', 'created_at', 'updated_at']
