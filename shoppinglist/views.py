from rest_framework import generics
from .models import Item
from .serializers import ItemSerializer, ItemDetailSerializer
from garden_diary.permissions import IsOwnerOrReadOnly
from django.shortcuts import get_object_or_404
from rest_framework.response import Response


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
