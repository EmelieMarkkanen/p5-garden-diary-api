from rest_framework import serializers
from .models import ShoppingList, ShoppingListItem

class ShoppingListItemSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = ShoppingListItem
        fields = ['id', 'shopping_list', 'owner', 'name', 'quantity']

class ShoppingListSerializer(serializers.ModelSerializer):
    items = ShoppingListItemSerializer(many=True, read_only=True, source='shoppinglistitem_set')

    class Meta:
        model = ShoppingList
        fields = ['id', 'title', 'items', 'created_at', 'updated_at']
