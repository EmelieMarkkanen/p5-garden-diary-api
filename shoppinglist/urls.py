from django.urls import path
from .views import (
    ShoppingListView,
    ShoppingListDetailedView,
    ItemListView,
    ItemDetailView,
    ShoppingListItemListView,
    ShoppingListItemDetailView,
)

urlpatterns = [
    path('shoppinglists/', ShoppingListView.as_view()),
    path('shoppinglists/<int:pk>/', ShoppingListDetailedView.as_view()),
    path('items/', ItemListView.as_view()),
    path('items/<int:pk>/', ItemDetailView.as_view()),
    path('shoppinglistitems/', ShoppingListItemListView.as_view()),
    path('shoppinglistitems/<int:pk>/', ShoppingListItemDetailView.as_view()),
]