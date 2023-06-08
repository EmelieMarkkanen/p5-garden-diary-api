from rest_framework import generics
from .models import ShoppingList, ShoppingListItem
from .serializers import ShoppingListSerializer, ShoppingListItemSerializer
from garden_diary.permissions import IsOwnerOrReadOnly

class ShoppingListView(generics.ListCreateAPIView):
    queryset = ShoppingList.objects.all()
    serializer_class = ShoppingListSerializer
    permissions = [IsOwnerOrReadOnly]

class ShoppingListDetailedView(generics.RetrieveUpdateDestroyAPIView):
    queryset = ShoppingList.objects.all()
    serializer_class = ShoppingListSerializer
    permissions = [IsOwnerOrReadOnly]

class ShoppingListItemView(generics.RetrieveUpdateDestroyAPIView):
    queryset = ShoppingListItem.objects.all()
    serializer_class = ShoppingListItemSerializer
    permissions = [IsOwnerOrReadOnly]
