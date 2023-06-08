from rest_framework import serializers
from .models import ShoppingList, ShoppingListItem

class ShoppingListItemSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = ShoppingListItem
        fields = ['id', 'shopping_list', 'owner', 'name', 'quantity']
        

class ShoppingListSerializer(serializers.ModelSerializer):
    items = serializers.SerializerMethodField()

    def get_items(self, obj):
        items = obj.items.all()
        return [{"id": item.id, "name": item.name} for item in items]

    class Meta:
        model = ShoppingList
        fields = ['id', 'title', 'items', 'created_at', 'updated_at']


