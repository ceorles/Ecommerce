from django.contrib import admin
from .models import Product

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'stock')

    @admin.display(description='Stock')
    def is_available_display(self, obj):
        return obj.get_stock_display()