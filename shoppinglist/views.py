from rest_framework import generics
from .models import ShoppingList, ShoppingListItem
from .serializers import ShoppingListSerializer, ShoppingListItemSerializer
from garden_diary.permissions import IsOwnerOrReadOnly
from django.shortcuts import get_object_or_404

class ShoppingListView(generics.ListCreateAPIView):
    queryset = ShoppingList.objects.all()
    serializer_class = ShoppingListSerializer
    permission_classes = [IsOwnerOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class ShoppingListDetailedView(generics.RetrieveUpdateDestroyAPIView):
    queryset = ShoppingList.objects.all()
    serializer_class = ShoppingListSerializer
    permission_classes = [IsOwnerOrReadOnly]


class ShoppingListCreateItemView(generics.CreateAPIView):
    queryset = ShoppingListItem.objects.all()
    serializer_class = ShoppingListItemSerializer
    permission_classes = [IsOwnerOrReadOnly]

    def perform_create(self, serializer):
        shopping_list_id = self.kwargs.get('list_id')
        shopping_list = get_object_or_404(ShoppingList, id=shopping_list_id)
        serializer.save(owner=self.request.user, shopping_list=shopping_list)


class ShoppingListItemDetailedView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ShoppingListItemSerializer

    def get_queryset(self):
        shopping_list_id = self.kwargs['list_id']
        return ShoppingListItem.objects.filter(shopping_list_id=shopping_list_id)

    def get_object(self):
        queryset = self.get_queryset()
        item_id = self.kwargs['item_id']
        item = get_object_or_404(queryset, id=item_id)
        return item