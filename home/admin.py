from django.contrib import admin
from home.models import *


class ProductImageInline(admin.TabularInline):
    model = ImageItem


class ProductAdmin(admin.ModelAdmin):
    list_display = ['title', 'price']
    inlines = [ProductImageInline]


admin.site.register(Product, ProductAdmin)
