from rest_framework import generics, status
from .models import ShoppingList, ShoppingListItem
from .serializers import ShoppingListSerializer, ItemSerializer, ShoppingListDetailSerializer
from garden_diary.permissions import IsOwnerOrReadOnly, IsOwnerOfList, IsOwnerOfListItem
from django.shortcuts import get_object_or_404
from rest_framework.response import Response


class ShoppingListView(generics.ListCreateAPIView):
    queryset = ShoppingList.objects.all()
    serializer_class = ShoppingListSerializer
    permission_classes = [IsOwnerOrReadOnly, IsOwnerOfList]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
        

class ShoppingListDetailedView(generics.RetrieveAPIView):
    queryset = ShoppingList.objects.all()
    serializer_class = ShoppingListDetailSerializer

class ItemView(generics.RetrieveUpdateDestroyAPIView):
    queryset = ShoppingListItem.objects.all()
    serializer_class = ItemSerializer
    permission_classes = [IsOwnerOrReadOnly, IsOwnerOfListItem]
