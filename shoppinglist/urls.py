from django.urls import path
from .views import ShoppingListView, ShoppingListDetailedView

urlpatterns = [
    path('shoppinglist/', ShoppingListView.as_view()),
    path('shoppinglist/<int:pk>/', ShoppingListDetailedView.as_view()),
]
