from django.shortcuts import render
from rest_framework import viewsets, generics
from .models import *
from .serializers import *


class UserProfileViewSet(viewsets.ModelViewSet):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class StoreViewSet(viewsets.ModelViewSet):
    queryset = Store.objects.all()
    serializer_class = StoreSerializer

class StoreListApiView(generics.ListAPIView):
    queryset = Store.objects.all()
    serializer_class = StoreListSerializer

class StoreDetailApiView(generics.RetrieveAPIView):
    queryset = Store.objects.all()
    serializer_class = StoreDetailSerializer


class ContactViewSet(viewsets.ModelViewSet):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer

class ContactListApiView(generics.ListAPIView):
    queryset = Contact.objects.all()
    serializer_class = ContactListSerializer


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class ProductListApiView(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductListSerializer


class ComboViewSet(viewsets.ModelViewSet):
    queryset = Combo.objects.all()
    serializer_class = ComboSerializer


class ComboListApiView(generics.ListAPIView):
    queryset = Combo.objects.all()
    serializer_class = ComboListSerializer

class ComboDetailApiView(generics.RetrieveAPIView):
    queryset = Combo.objects.all()
    serializer_class = ComboDetailSerializer


class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer


class CartViewSet(viewsets.ModelViewSet):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer


class CartItemViewSet(viewsets.ModelViewSet):
    queryset = CartItem.objects.all()
    serializer_class = CartItemSerializer


class CourierViewSet(viewsets.ModelViewSet):
    queryset = Courier.objects.all()
    serializer_class = CourierSerializer


class CourierRatingViewSet(viewsets.ModelViewSet):
    queryset = CourierRating.objects.all()
    serializer_class = CourierRatingSerializer


class StoreReviewViewSet(viewsets.ModelViewSet):
    queryset = StoreReview.objects.all()
    serializer_class = StoreReviewSerializer

class StoreReviewListApiView(generics.ListAPIView):
    queryset = StoreReview.objects.all()
    serializer_class =  StoreReviewListSerializer

class StoreReviewDetailAPIView(generics.RetrieveAPIView):
    queryset = StoreReview.objects.all()
    serializer_class = StoreDetailReviewSerializer
