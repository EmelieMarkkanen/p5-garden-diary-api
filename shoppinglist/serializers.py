from rest_framework import serializers
from .models import ShoppingList


class ShoppingListSerializer(serializers.ModelSerializer):

    class Meta:
        model = ShoppingList
        fields = ('id', 'owner', 'title', 'created_at', 'updated_at', 'item', 'quantity')
        
class ShoppingListDetailedSerializer(serializers.ModelSerializer):

    class Meta:
        model = ShoppingList
        fields = ('id', 'owner', 'title', 'created_at', 'updated_at','item', 'quantity')


