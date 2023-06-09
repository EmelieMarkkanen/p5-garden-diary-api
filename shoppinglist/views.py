from rest_framework import generics
from .models import ShoppingList, Item, ShoppingListItem
from .serializers import (
    ShoppingListSerializer,
    ShoppingListDetailedSerializer,
    ItemSerializer,
    ShoppingListItemSerializer,
)
from garden_diary.permissions import IsOwnerOrReadOnly

class ShoppingListView(generics.ListCreateAPIView):
    queryset = ShoppingList.objects.all()
    serializer_class = ShoppingListSerializer
    permission_classes = [IsOwnerOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class ShoppingListDetailedView(generics.RetrieveUpdateDestroyAPIView):
    queryset = ShoppingList.objects.all()
    serializer_class = ShoppingListDetailedSerializer
    permission_classes = [IsOwnerOrReadOnly]

class ItemListView(generics.ListCreateAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer

class ItemDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer

class ShoppingListItemListView(generics.ListCreateAPIView):
    queryset = ShoppingListItem.objects.all()
    serializer_class = ShoppingListItemSerializer

class ShoppingListItemDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = ShoppingListItem.objects.all()
    serializer_class = ShoppingListItemSerializer
