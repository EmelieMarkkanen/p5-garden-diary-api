from rest_framework import generics
from .models import Item
from .serializers import ItemSerializer, ItemDetailSerializer
from garden_diary.permissions import IsOwnerOrReadOnly
from django.shortcuts import get_object_or_404
from rest_framework.response import Response


class ItemListView(generics.ListCreateAPIView):
    """View for listing and creating items."""
    queryset = Item.objects.all()
    serializer_class = ItemSerializer
    permission_classes = [IsOwnerOrReadOnly]
    
    def get_queryset(self):
        user = self.request.user
        return Item.objects.filter(owner=user)
    
    def perform_create(self, serializer):
        """Save the owner of the item as the current user."""
        serializer.save(owner=self.request.user)


class ItemDetailedView(generics.RetrieveUpdateDestroyAPIView):
    """View for retrieving, updating, and deleting an item."""
    queryset = Item.objects.all()
    serializer_class =ItemDetailSerializer
    permission_classes =[IsOwnerOrReadOnly]

    def get_queryset(self):
        user = self.request.user
        return Item.objects.filter(owner=user)