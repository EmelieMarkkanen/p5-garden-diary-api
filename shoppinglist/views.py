from rest_framework import generics
<<<<<<< HEAD
from .models import ShoppingList, Item, ShoppingListItem
from .serializers import (
    ShoppingListSerializer,
    ShoppingListDetailedSerializer,
    ItemSerializer,
    ShoppingListItemSerializer,
)
=======
from .models import Item
from .serializers import ItemSerializer, ItemDetailSerializer
>>>>>>> dcc3008 (Rework shoppinglist app, decided to make the lists based on individual items instead for simplicity)
from garden_diary.permissions import IsOwnerOrReadOnly
from django.shortcuts import get_object_or_404
from rest_framework.response import Response

<<<<<<< HEAD
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
=======

class ItemListView(generics.ListCreateAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer
    permission_classes = [IsOwnerOrReadOnly]
    
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class ItemDetailedView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Item.objects.all()
    serializer_class =ItemDetailSerializer
    permission_classes =[IsOwnerOrReadOnly]
>>>>>>> dcc3008 (Rework shoppinglist app, decided to make the lists based on individual items instead for simplicity)
