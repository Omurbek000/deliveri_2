from django.db import models
from django.contrib.auth.models import AbstractUser
from phonenumber_field.modelfields import PhoneNumberField
from django.core.validators import MinValueValidator, MaxValueValidator

class UserProfile(AbstractUser):
    phone_number = PhoneNumberField(null=True, blank=True)
    profile_image = models.ImageField(upload_to='profile_images/', null=True, blank=True)
    
    ROLE_CHOICES = (
        ('client', 'Client'),
        ('driver', 'Driver'),
        ('admin', 'Admin'),
        ('owner', 'Owner')
    )
    role = models.CharField(choices=ROLE_CHOICES, default='client', max_length=15)
    created_date = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f'{self.first_name} - {self.last_name} - {self.role}'
    


class Category(models.Model):
    category_name = models.CharField(max_length=32, unique=True)
    
    def __str__(self):
        return f'{self.category_name}'
    



class Store(models.Model):
    store_name = models.CharField(max_length=32)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='stores')
    store_image = models.ImageField(upload_to='stores/', null=True, blank=True)
    address = models.CharField(max_length=100)
    description = models.TextField()
    owner = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    
    
    def __str__(self):
        return f'{self.store_name}'
    


class Contact(models.Model):
    store = models.ForeignKey(Store, on_delete=models.CASCADE, related_name='contact_store')
    title = models.CharField(max_length=32)
    phone_number = PhoneNumberField()
    social_network = models.URLField(null=True, blank=True)
    
    def __str__(self):
        return f'{self.title} - {self.phone_number}'
    
 


class Product(models.Model):
   store = models.ForeignKey(Store, on_delete=models.CASCADE, related_name='store_product')
   product_name = models.CharField(max_length=32)
   description = models.TextField()
   product_image = models.ImageField(upload_to='products/', null=True, blank=True)
   price = models.DecimalField(max_digits=7, decimal_places=2)

class Combo(models.Model):
    store = models.ForeignKey(Store, on_delete=models.CASCADE, related_name='store_combo')
    combo_name = models.CharField(max_length=32)
    description = models.TextField()
    combo_image = models.ImageField(upload_to='combo/', null=True, blank=True)
    price = models.DecimalField(max_digits=7, decimal_places=2)
    
    def __str__(self):
        return f'{self.combo_name} - {self.price}'
    

# class Review(models.Model):
#     store = models.ForeignKey(Store, on_delete=models.CASCADE, related_name='reviews')
#     user = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='reviews')
#     stars = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
#     created_date = models.DateTimeField(auto_now_add=True)
    
#     def __str__(self):
#         return f'{self.stars} - {self.user} - {self.store}'
    


class Cart(models.Model):
    user = models.OneToOneField(UserProfile, on_delete=models.CASCADE, related_name='cart')
    
    def __str__(self):
        return f'{self.user}'
    


class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, related_name='items')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True , blank=True)
    combo = models.ForeignKey(Combo, on_delete=models.CASCADE, null=True , blank=True)
    quantity = models.PositiveIntegerField(default=1)
    
    def __str__(self):
        return f'{self.cart} - {self.product} - {self.quantity}'
    


class Order(models.Model):
    client = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='client_profile')
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, related_name='orders')
    ORDER_STATUS_CHOICES = (
     ('в ожидании', 'В ожидании'),
     ('в процессе', 'В процессе'),
     ('доставлено', 'Доставлено'),
     ('отменено',   'Отменено')
                
    )
    order_status = models.CharField(max_length=64, choices=ORDER_STATUS_CHOICES, default='в ожидании')
    delivery_address = models.CharField(max_length=128)
    courier = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='courier_profile')
    created_date = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f'{self.order_status}'
    

class Courier(models.Model):
    courier = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    courier_order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='orders')
    COURIER_STATUS_CHOICES = (
        ('Доступен', 'Доступен'),
        ('Занят', 'Занят'),
    )
    courier_status = models.CharField(max_length=64, choices=COURIER_STATUS_CHOICES)
    
    def __str__(self):
        return f'{self.courier} - {self.courier_status}'



class StoreReview(models.Model):
    client = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    store = models.ForeignKey(Store, on_delete=models.CASCADE)
    text = models.TextField()
    stars = models.PositiveIntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    created_date = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f'{self.client} - {self.store}'


class CourierRating(models.Model):
    client = models.ForeignKey(UserProfile,on_delete=models.CASCADE, related_name='clients')
    courier = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='couriers')
    rating = models.IntegerField(choices=[(i, str(i)) for i in range(1,6)])
    created_date = models.DateTimeField(auto_now_add=True)    
    
    def __str__(self):
        return f'{self.courier} - {self.rating}'