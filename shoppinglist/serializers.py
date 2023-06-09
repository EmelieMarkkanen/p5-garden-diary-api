from rest_framework import serializers
from .models import Item

class ItemSerializer(serializers.ModelSerializer):
    item = serializers.CharField(source='name')
    quantity = serializers.IntegerField()

    class Meta:
        model = Item
        fields = ['item', 'quantity']


class ItemDetailSerializer(serializers.ModelSerializer):
    item = serializers.CharField(source='name')
    quantity = serializers.IntegerField()

    class Meta:
        model = Item
        fields = ['item', 'quantity', 'owner', 'created_at', 'updated_at']
