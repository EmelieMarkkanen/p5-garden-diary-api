from django.urls import path
from .views import ShoppingListView, ShoppingListDetailedView, ItemView

urlpatterns = [
    path('shoppinglist/', ShoppingListView.as_view()),
    path('shoppinglist/<int:pk>/', ShoppingListDetailedView.as_view()),
    path('shoppinglist/<int:pk>/items/', ItemView.as_view()),
]
