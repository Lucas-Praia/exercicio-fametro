from rest_framework import serializers
from .models import Brand, Category, Inflow, Outflow, Product, Supplier

class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = '__all__'

    def validate_name(self, value):
        if Brand.objects.filter(name=value).exists():
            raise serializers.ValidationError('Marca já cadastrada.')
        return value

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

    def validate_name(self, value):
        if Category.objects.filter(name=value).exists():
            raise serializers.ValidationError('Categoria já está cadastrada.')
        return value

class InflowSerializer(serializers.ModelSerializer):
    class Meta:
        model = Inflow
        fields = '__all__'

class OutflowSerializer(serializers.ModelSerializer):
    class Meta:
        model = Outflow
        fields = '__all__'

class ProductSerializer(serializers.ModelSerializer):
    brand = serializers.SlugRelatedField(
        read_only=False,
        queryset=Brand.objects.all(),
        slug_field='name'
    )
    category = serializers.SlugRelatedField(
        read_only=False,
        queryset=Category.objects.all(),
        slug_field='name'
    )

    class Meta:
        model = Product
        fields = '__all__'
        
class SupplierSerializer(serializers.ModelSerializer):
    class Meta:
        model = Supplier
        fields = '__all__'
