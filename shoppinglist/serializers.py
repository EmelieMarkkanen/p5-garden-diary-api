from rest_framework import serializers
from .models import ShoppingList, Item, ShoppingListItem

class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = ('id', 'name')

class ShoppingListSerializer(serializers.ModelSerializer):
    class Meta:
        model = ShoppingList
        fields = ('id', 'owner', 'title', 'created_at', 'updated_at')

class ShoppingListDetailedSerializer(serializers.ModelSerializer):
    items = serializers.SerializerMethodField()

    class Meta:
        model = ShoppingList
        fields = ('id', 'owner', 'title', 'created_at', 'updated_at', 'items')

    def get_items(self, obj):
        shopping_list_items = ShoppingListItem.objects.filter(shopping_list=obj)
        serializer = ShoppingListItemSerializer(shopping_list_items, many=True)
        return serializer.data

class ShoppingListItemSerializer(serializers.ModelSerializer):
    item = ItemSerializer()

    class Meta:
        model = ShoppingListItem
        fields = ('id', 'shopping_list', 'item', 'quantity')

    def create(self, validated_data):
        item_data = validated_data.pop('item')
        item, _ = Item.objects.get_or_create(**item_data)
        validated_data['item'] = item
        return super().create(validated_data)
