from rest_framework import serializers
from .models import ShoppingList, ShoppingListItem

class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = ShoppingListItem
        fields = ('id', 'name', 'quantity')

class ShoppingListSerializer(serializers.ModelSerializer):
    items = ItemSerializer(many=True, read_only=True)

    class Meta:
        model = ShoppingList
        fields = ('id', 'owner', 'title', 'created_at', 'updated_at', 'items')
        read_only_fields = ('owner', 'created_at', 'updated_at')

class ShoppingListDetailSerializer(serializers.ModelSerializer):
    items = ItemSerializer(many=True)

    class Meta:
        model = ShoppingList
        fields = ('id', 'owner', 'title', 'created_at', 'updated_at', 'items')

    def to_representation(self, instance):
        data = super().to_representation(instance)
        items = instance.items.all()
        data['items'] = ItemSerializer(items, many=True).data
        return data

