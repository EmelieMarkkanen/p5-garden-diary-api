from rest_framework import generics
from .models import ShoppingList, ShoppingListItem
from .serializers import ShoppingListSerializer, ShoppingListItemSerializer
from garden_diary.permissions import IsOwnerOrReadOnly

class ShoppingListView(generics.ListCreateAPIView):
    queryset = ShoppingList.objects.all()
    serializer_class = ShoppingListSerializer
    permissions = [IsOwnerOrReadOnly]
    
    def get_queryset(self):
        user = self.request.user
        return ShoppingList.objects.filter(owner=user)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class ShoppingListDetailedView(generics.RetrieveUpdateDestroyAPIView):
    queryset = ShoppingList.objects.all()
    serializer_class = ShoppingListSerializer
    permissions = [IsOwnerOrReadOnly]
    
    def get_queryset(self):
        user = self.request.user
        return ShoppingList.objects.filter(owner=user)

class ShoppingListItemView(generics.RetrieveUpdateDestroyAPIView):
    queryset = ShoppingListItem.objects.all()
    serializer_class = ShoppingListItemSerializer
    permissions = [IsOwnerOrReadOnly]

    def get_queryset(self):
        user = self.request.user
        return ShoppingListItem.objects.filter(owner=user)