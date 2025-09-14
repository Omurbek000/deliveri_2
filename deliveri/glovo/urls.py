from django.urls import path, include
from .views import *
from rest_framework import routers

router = routers.DefaultRouter()

urlpatterns = [
    path('', include(router.urls)),
    path('userprofile', UserProfileViewSet, basename='userprofiles'),
    path('category', CategoryViewSet, basename='categories'),
    path('store', StoreViewSet, basename='stores'),
    path('contact', ContactViewSet, basename='contacts'),
    path('productcategory', ProductCategoryViewSet, basename='productcategories'),
    path('product', ProductViewSet, basename='products'),
    path('review', ReviewViewSet, basename='reviews'),
    path('cart', CartViewSet, basename='carts'),
    path('cart-item', CartItemViewSet, basename='cartitems'),
  
