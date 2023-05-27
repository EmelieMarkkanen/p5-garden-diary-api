from django.urls import path
from .views import (
    ShoppingListView,
    ShoppingListDetailedView,
    ShoppingListItemDetailedView,
)

urlpatterns = [
    path('shoppinglist/', ShoppingListView.as_view()),
    path('shoppinglist/<int:pk>/', ShoppingListDetailedView.as_view()),
    path('shoppinglist/<int:list_id>/item/<int:item_id>/', ShoppingListItemDetailedView.as_view()),
]