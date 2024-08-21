from django.contrib import admin
from .models import Brand,Category,Inflow,Outflow,Product,Supplier

# Classe base para configurar propriedades comuns
class ModelAdminBase(admin.ModelAdmin):
    list_per_page = 20

@admin.register(Brand)
class BrandAdmin(ModelAdminBase):
    list_display = (
        'name',
        'description',
    )
    search_fields = (
        'name',
    )

@admin.register(Category)
class CategoryAdmin(ModelAdminBase):
    list_display = (
        'name',
        'description',
    )
    search_fields = (
        'name',
    )

@admin.register(Inflow)
class InflowAdmin(ModelAdminBase):
    list_display = (
        'supplier', 
        'product', 
        'quantity', 
        'created_at', 
        'updated_at',
    )
    search_fields = (
        'supplier__name',
        'product__title',
    )

@admin.register(Outflow)
class OutflowAdmin(ModelAdminBase):
    list_display = (
        'product',
        'quantity',
        'created_at',
        'updated_at',
    )
    search_fields = (
        'product__title',
    )

class ModelAdminBase(admin.ModelAdmin):
    list_per_page = 20

@admin.register(Product)
class ProductAdmin(ModelAdminBase):
    list_display = (
        'title',
        'serie_number',
    )
    search_fields = (
        'title',
    )

@admin.register(Supplier)
class SupplierAdmin(ModelAdminBase):
    list_display = (
        'name',
        'description',
    )
    search_fields = (
        'name',
    )