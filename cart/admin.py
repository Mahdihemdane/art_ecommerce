# cart/admin.py

from django.contrib import admin
from .models import Cart, CartItem, Payment

@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    list_display = ('user', 'created_at')
    search_fields = ('user__username',)
    ordering = ('-created_at',)

@admin.register(CartItem)
class CartItemAdmin(admin.ModelAdmin):
    list_display = ('cart', 'artwork', 'quantity')
    list_filter = ('cart',)
    search_fields = ('artwork__title',)  # Assuming Artwork model has a title field

@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_display = ('user', 'amount', 'created_at', 'success')
    list_filter = ('success',)
    search_fields = ('user__username',)
    ordering = ('-created_at',)
