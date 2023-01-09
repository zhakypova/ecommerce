from django.urls import path, include
from rest_framework.routers import DefaultRouter

from . import views



urlpatterns = [
    path('category/', views.CategoryListCreateView.as_view(), name='category_list'),
    path('category/<int:pk>/', views.CategoryDetail.as_view(), name='category_detail'),
    path('category/<int:pk>/item/', views.ItemListCreateView.as_view(), name='item_list'),
    path('category/<int:pk>/item/<int:id>/', views.ItemDetail.as_view(), name='item_detail'),
]