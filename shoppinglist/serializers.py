from rest_framework import serializers
<<<<<<< HEAD
from .models import ShoppingList, Item, ShoppingListItem

class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = ('id', 'name')

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

class ShoppingListSerializer(serializers.ModelSerializer):
    items = serializers.SerializerMethodField()
=======
from .models import Item
>>>>>>> dcc3008 (Rework shoppinglist app, decided to make the lists based on individual items instead for simplicity)

class ItemSerializer(serializers.ModelSerializer):
    class Meta:
<<<<<<< HEAD
        model = ShoppingList
        fields = ('id', 'owner', 'title', 'created_at', 'updated_at', 'items')

    def get_items(self, obj):
        shopping_list_items = ShoppingListItem.objects.filter(shopping_list=obj)
        serializer = ShoppingListItemSerializer(shopping_list_items, many=True)
        return serializer.data

    def create(self, validated_data):
        items_data = validated_data.pop('items')
        shopping_list = ShoppingList.objects.create(**validated_data)
        for item_data in items_data:
            item = Item.objects.create(**item_data)
            ShoppingListItem.objects.create(
                shopping_list=shopping_list,
                item=item,
                quantity=item_data['quantity']
            )
        return shopping_list

class ShoppingListDetailedSerializer(serializers.ModelSerializer):
    items = serializers.SerializerMethodField()
=======
        model = Item
        fields = '__all__'
>>>>>>> dcc3008 (Rework shoppinglist app, decided to make the lists based on individual items instead for simplicity)

class ItemDetailSerializer(serializers.ModelSerializer):
    
    class Meta:
<<<<<<< HEAD
        model = ShoppingList
        fields = ('id', 'owner', 'title', 'created_at', 'updated_at', 'items')

    def get_items(self, obj):
        shopping_list_items = ShoppingListItem.objects.filter(shopping_list=obj)
        serializer = ShoppingListItemSerializer(shopping_list_items, many=True)
        return serializer.data



=======
        model = Item
        fields = '__all__'
>>>>>>> dcc3008 (Rework shoppinglist app, decided to make the lists based on individual items instead for simplicity)
