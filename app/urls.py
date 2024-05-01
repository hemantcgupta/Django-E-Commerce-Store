from django.urls import path
from .views import (RegisterView, LoginView, ProductView, ProductDetailView, CategoryView, CategoryDetailView)

urlpatterns = [
    # Auth Views
    path('register/', RegisterView.as_view(), name='user-register'),
    path('login/', LoginView.as_view(), name='user-login'),

    path('products/', ProductView.as_view(), name='product-list'),
    path('products/<int:pk>/', ProductDetailView.as_view(), name='product-detail'),
    path('categories/', CategoryView.as_view(), name='category-list'),
    path('categories/<int:pk>/', CategoryDetailView.as_view(), name='category-detail'),
]
