from rest_framework import serializers
from .models import ShoppingList, ShoppingListItem

class ShoppingListItemSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = ShoppingListItem
        fields = ['id', 'shopping_list', 'owner', 'name', 'quantity']
        

class ShoppingListSerializer(serializers.ModelSerializer):
    items = ShoppingListItemSerializer(many=True, read_only=True)
    items_count = serializers.SerializerMethodField()

    def get_items_count(self, obj):
        return obj.items.count()

    class Meta:
        model = ShoppingList
        fields = ['id', 'title', 'items_count', 'items', 'created_at', 'updated_at']

