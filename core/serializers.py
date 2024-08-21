from rest_framework import serializers
from .models import Brand,Category,Inflow,Outflow,Product,Supplier

class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = '__all__'

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class InflowSerializer(serializers.ModelSerializer):
    class Meta:
        model = Inflow
        fields = '__all__'

class OutflowSerializer(serializers.ModelSerializer):
    class Meta:
        model = Outflow
        fields = '__all__'


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'


class SupplierSerializer(serializers.ModelSerializer):
    class Meta:
        model = Supplier
        fields = '__all__'