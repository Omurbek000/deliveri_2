from django.db import models
from django.contrib.auth.models import AbstractUser
from phonenumber_field.modelfields import PhoneNumberField
from django.core.validators import MinValueValidator, MaxValueValidator

class UserProfile(AbstractUser):
    phone_number = PhoneNumberField(null=True, blank=True)
    
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
    
    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'


class Category(models.Model):
    category_name = models.CharField(max_length=32, unique=True)
    
    def __str__(self):
        return f'{self.category_name}'
    
    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class Store(models.Model):
    store_name = models.CharField(max_length=32)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='stores')
    store_image = models.ImageField(upload_to='stores/', blank=True)
    address = models.CharField(max_length=100)
    description = models.TextField()
    owner = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='stores')
    free = models.BooleanField()
    
    def __str__(self):
        return f'{self.store_name}'
    
    class Meta:
        verbose_name = 'Магазин'
        verbose_name_plural = 'Магазины'


class Contact(models.Model):
    store = models.ForeignKey(Store, on_delete=models.CASCADE, related_name='contacts')
    title = models.CharField(max_length=32)
    phone_number = PhoneNumberField()
    
    def __str__(self):
        return f'{self.title} - {self.phone_number}'
    
    class Meta:
        verbose_name = 'Контакт'
        verbose_name_plural = 'Контакты'


class ProductCategory(models.Model):
    product_category_name = models.CharField(max_length=32, unique=True)
    
    def __str__(self):
        return f'{self.product_category_name}'
    
    class Meta:
        verbose_name = 'Категория товара'
        verbose_name_plural = 'Категории товаров'


class Product(models.Model):
    store = models.ForeignKey(Store, on_delete=models.CASCADE, related_name='products')
    product_category = models.ForeignKey(ProductCategory, on_delete=models.CASCADE, related_name='products')
    product_name = models.CharField(max_length=32)
    description = models.TextField()
    product_image = models.ImageField(upload_to='products/', blank=True)
    price = models.DecimalField(max_digits=7, decimal_places=2)
    
    def __str__(self):
        return f'{self.product_name} - {self.price}'
    
    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'


class Review(models.Model):
    store = models.ForeignKey(Store, on_delete=models.CASCADE, related_name='reviews')
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='reviews')
    stars = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    created_date = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f'{self.stars} - {self.user} - {self.store}'
    
    class Meta:
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'


class Cart(models.Model):
    user = models.OneToOneField(UserProfile, on_delete=models.CASCADE, related_name='cart')
    
    def __str__(self):
        return f'{self.user}'
    
    class Meta:
        verbose_name = 'Корзина'
        verbose_name_plural = 'Корзины'


class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, related_name='items')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='cart_items')
    quantity = models.PositiveIntegerField(default=1)
    
    def __str__(self):
        return f'{self.cart} - {self.product} - {self.quantity}'
    
    class Meta:
        verbose_name = 'Элемент корзины'
        verbose_name_plural = 'Элементы корзины'