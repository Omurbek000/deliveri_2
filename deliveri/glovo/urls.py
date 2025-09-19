from django.urls import path, include
from .views import *
from rest_framework import routers

router = routers.DefaultRouter()

router.register(r'userprofile', UserProfileViewSet, basename='userprofiles')
router.register(r'category', CategoryViewSet, basename='categories')
router.register(r'store', StoreViewSet, basename='stores')
# router.register(r'store/list', StoreListApiView.as_view(), basename='stores-list')
# router.register(r'store/<int:pk>/', StoreDetailApiView.as_view(), basename='stores-detail')
router.register(r'contact', ContactViewSet, basename='contacts')
router.register(r'product', ProductViewSet, basename='products')
router.register(r'combo', ComboViewSet, basename='combos')
router.register(r'order', OrderViewSet, basename='orders')
router.register(r'cart', CartViewSet, basename='carts')
router.register(r'cart-item', CartItemViewSet, basename='cartitems')
router.register(r'courier', CourierViewSet, basename='couriers')
router.register(r'courier-rating', CourierRatingViewSet, basename='courier-ratings')
router.register(r'store-review', StoreReviewViewSet, basename='store-reviews')

urlpatterns = [
    path('', include(router.urls)),
]