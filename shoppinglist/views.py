from rest_framework import generics
from .models import ShoppingList, ShoppingListItem
from .serializers import ShoppingListSerializer, ShoppingListItemSerializer
from garden_diary.permissions import IsOwnerOrReadOnly, IsOwnerOfList, IsOwnerOfListItem
from django.shortcuts import get_object_or_404

class ShoppingListView(generics.ListCreateAPIView):
    queryset = ShoppingList.objects.all().prefetch_related('items')
    serializer_class = ShoppingListSerializer
    permission_classes = [IsOwnerOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class ShoppingListDetailedView(generics.RetrieveUpdateDestroyAPIView):
    queryset = ShoppingList.objects.all()
    serializer_class = ShoppingListSerializer
    permission_classes = [IsOwnerOfList]


class ShoppingListItemDetailedView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ShoppingListItemSerializer
    permission_classes = [IsOwnerOfListItem]

    def get_queryset(self):
        shopping_list_id = self.kwargs['list_id']
        return ShoppingListItem.objects.filter(shopping_list_id=shopping_list_id)

    def get_object(self):
        queryset = self.get_queryset()
        item_id = self.kwargs['item_id']
        item = get_object_or_404(queryset, id=item_id)
        return item
