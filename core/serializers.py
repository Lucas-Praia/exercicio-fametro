from rest_framework import serializers
from .models import Brand, Category, Inflow, Outflow, Product, Supplier

class ProductSerializer(serializers.ModelSerializer):
    brand_name = serializers.SerializerMethodField()
    category_title = serializers.SerializerMethodField()
    
    class Meta:
        model = Product
        fields = ['id', 'title', 'category', 'brand', 'description', 'serie_number', 'cost_price', 'selling_price', 'quantity', 'created_at', 'updated_at', 'brand_name', 'category_title']

    def get_brand_name(self, obj):
        return obj.brand.name

    def get_category_title(self, obj):
        return obj.category.name

    def validate(self, data):
        # Checa se existe produto com o mesmo nome e o mesmo número de série
        if Product.objects.filter(title=data.get('title')).exists() and Product.objects.filter(serie_number=data.get('serie_number')).exists():
            raise serializers.ValidationError('Produto já cadastrado.')
        return data

class SupplierSerializer(serializers.ModelSerializer):
    class Meta:
        model = Supplier
        fields = '__all__'

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
    supplier = serializers.PrimaryKeyRelatedField(queryset=Supplier.objects.all())
    product = serializers.PrimaryKeyRelatedField(queryset=Product.objects.all())
    
    supplier_name = serializers.SerializerMethodField()
    product_title = serializers.SerializerMethodField()

    class Meta:
        model = Inflow
        fields = ['id', 'quantity', 'description', 'created_at', 'updated_at', 'supplier', 'product', 'supplier_name', 'product_title']

    def get_supplier_name(self, obj):
        return obj.supplier.name

    def get_product_title(self, obj):
        return obj.product.title

class OutflowSerializer(serializers.ModelSerializer):
    product_title = serializers.SerializerMethodField()  # Traz o nome do produto

    class Meta:
        model = Outflow
        fields = ['id', 'quantity', 'description', 'created_at', 'updated_at', 'product', 'product_title'] 

    def get_product_title(self, obj):  # Lógica que traz o nome do produto
        return obj.product.title


