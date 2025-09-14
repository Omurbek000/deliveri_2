from rest_framework import serializers
from .models import *


class UserProfileSerializer(serializers.ModelSerializer):
  class Meta:
    model = UserProfile
    fields = "__all__"


class CategorySerializer(serializers.ModelSerializer):
  class Meta:
    model = Category
    fields = "__all__"


class StoreSerializer(serializers.ModelSerializer):
  class Meta:
    model = Store
    fields = "__all__"


class ContactSerializer(serializers.ModelSerializer):
  class Meta:
    model = Contact
    fields = "__all__"


class ProductCategorySerializer(serializers.ModelSerializer):
  class Meta:
    model = ProductCategory
    fields = "__all__"


class ProductSerializer(serializers.ModelSerializer):
  class Meta:
    model = Product
    fields = "__all__"

class ReviewSerializer(serializers.ModelSerializer):
  class Meta:
    model = Review
    fields = "__all__"

class CartSerializer(serializers.ModelSerializer):
  class Meta:
    model = Cart
    fields = "__all__"

class CartItemSerializer(serializers.ModelSerializer):
  class Meta:
    model = CartItem
    fields = "__all__"