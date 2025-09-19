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

    
class StoreListSerializer(serializers.ModelSerializer):
  class Meta:
    model = Store
    fields = "store_name, category"
    

class StoreDetailSerializer(serializers.ModelSerializer):
  class Meta:
    model = Store
    fields = "store_name, category, address, description, owner"
    


class ContactSerializer(serializers.ModelSerializer):
  class Meta:
    model = Contact
    fields = "__all__"


class ContactListSerializer(serializers.ModelSerializer):
  class Meta:
    model = Contact
    fields = "title, phone_number,store, social_network"



class ProductSerializer(serializers.ModelSerializer):
  class Meta:
    model = Product
    fields = "__all__"


class ProductListSerializer(serializers.ModelSerializer):
  class Meta:
    model = Product
    fields = "product_name, price, category, store, image"


class CartSerializer(serializers.ModelSerializer):
  class Meta:
    model = Cart
    fields = "__all__"

class CartItemSerializer(serializers.ModelSerializer):
  class Meta:
    model = CartItem
    fields = "__all__"


class ComboSerializer(serializers.ModelSerializer):
  class Meta:
    model = Combo
    fields = "__all__"

class ComboListSerializer(serializers.ModelSerializer):
  class Meta:
    model = Combo
    fields = "combo_name, description"

class ComboDetailSerializer(serializers.ModelSerializer):
  class Meta:
    model = Combo
    fields = "combo_name, description, product_name, image"


class OrderSerializer(serializers.ModelSerializer):
  class Meta:
    model = Order
    fields = "__all__"


class CourierSerializer(serializers.ModelSerializer):
  class Meta:
    model = Courier
    fields = "__all__"


class CourierRatingSerializer(serializers.ModelSerializer):
  class Meta:
    model = CourierRating
    fields = "__all__"


class StoreReviewSerializer(serializers.ModelSerializer):
  class Meta:
    model = StoreReview
    fields = "__all__"

class StoreReviewListSerializer(serializers.ModelSerializer):
  class Meta:
    model = StoreReview
    fields = "client, stars"

class StoreDetailReviewSerializer(serializers.ModelSerializer):
  class Meta:
    model = StoreReview
    fields = "client, stars, text, created_date"