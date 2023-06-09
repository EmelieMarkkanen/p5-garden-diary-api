from rest_framework import generics
from .models import ShoppingList
from .serializers import ShoppingListSerializer, ShoppingListDetailedSerializer
from garden_diary.permissions import IsOwnerOrReadOnly

class ShoppingListView(generics.ListCreateAPIView):
    queryset = ShoppingList.objects.all()
    serializer_class = ShoppingListSerializer
    permissions = [IsOwnerOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class ShoppingListDetailedView(generics.RetrieveUpdateDestroyAPIView):
    queryset = ShoppingList.objects.all()
    serializer_class = ShoppingListDetailedSerializer
    permissions = [IsOwnerOrReadOnly]
