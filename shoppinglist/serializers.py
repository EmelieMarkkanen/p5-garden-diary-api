class ShoppingListItemSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = ShoppingListItem
        fields = ['id', 'name', 'quantity', 'owner']


class ShoppingListSerializer(serializers.ModelSerializer):
    items = ShoppingListItemSerializer(many=True, read_only=True, source='items')
    items_count = serializers.SerializerMethodField()

    def get_items(self, obj):
        items = obj.items.all()
        return [{"id": item.id, "name": item.name} for item in items]

    class Meta:
        model = ShoppingList
        fields = ['id', 'title', 'items_count', 'items', 'created_at', 'updated_at']

