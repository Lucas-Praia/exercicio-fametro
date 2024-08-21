import django_filters
from .models import Brand,Category,Inflow,Outflow,Product,Supplier

class BrandFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = Brand
        fields = ['name']
        

class CategoryFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(field_name='name', lookup_expr='icontains')

    class Meta:
        model = Category
        fields = ['name','description']
        

class InflowFilter(django_filters.FilterSet):
    product = django_filters.CharFilter(field_name='product__title', lookup_expr='icontains')
    supplier = django_filters.CharFilter(field_name='supplier__name', lookup_expr='icontains')
    created_at = django_filters.DateFilter(field_name='created_at')

    class Meta:
        model = Inflow
        fields = ['product', 'supplier', 'created_at']
        

class OutflowFilter(django_filters.FilterSet):
    product = django_filters.CharFilter(field_name='product__title', lookup_expr='icontains')
    quantity = django_filters.NumberFilter(field_name='quantity')
    description = django_filters.CharFilter(field_name='description', lookup_expr='icontains')
    created_at = django_filters.DateTimeFilter(field_name='created_at')
    updated_at = django_filters.DateTimeFilter(field_name='updated_at')

    class Meta:
        model = Outflow
        fields = ['product']
        

class ProductFilter(django_filters.FilterSet):
    title = django_filters.CharFilter(field_name='title', lookup_expr='icontains')
    serie_number = django_filters.CharFilter(field_name='serie_number', lookup_expr='icontains')
    category = django_filters.NumberFilter(field_name='category_id')
    brand = django_filters.NumberFilter(field_name='brand__id')

    class Meta:
        model = Product
        fields = ['title', 'serie_number', 'category', 'brand']


class SupplierFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(field_name='name', lookup_expr='icontains')

    class Meta:
        model = Supplier
        fields = ['name']