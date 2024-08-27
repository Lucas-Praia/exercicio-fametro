from rest_framework import viewsets,status
from rest_framework.response import Response

from .serializers import BrandSerializer,CategorySerializer,InflowSerializer,OutflowSerializer,ProductSerializer,SupplierSerializer
from .filters import BrandFilter,CategoryFilter,InflowFilter,OutflowFilter,ProductFilter,SupplierFilter
from .models import Brand,Category,Inflow,Outflow,Product,Supplier

class BrandViewSet(viewsets.ModelViewSet):
    queryset = Brand.objects.all()
    serializer_class = BrandSerializer
    filterset_class = BrandFilter
    ordering_fields = '__all__'
    ordering = '-id'
    
    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.serializer_class(instance, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    filterset_class = CategoryFilter
    ordering_fields = '__all__'
    ordering = '-id'
    
    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.serializer_class(instance, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class InflowViewSet(viewsets.ModelViewSet):
    queryset = Inflow.objects.all()
    serializer_class = InflowSerializer
    filterset_class = InflowFilter
    ordering_fields = '__all__'
    ordering = '-id'

class OutflowViewSet(viewsets.ModelViewSet):
    queryset = Outflow.objects.all()
    serializer_class = OutflowSerializer
    filterset_class = OutflowFilter
    ordering_fields = '__all__'
    ordering = '-id'

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filterset_class = ProductFilter
    ordering_fields = '__all__'
    ordering = '-id'

    def update(self, request, *args, **kwargs):
         instance = self.get_object()
         serializer = self.serializer_class(instance, data=request.data)
         if serializer.is_valid():
             serializer.save()
             return Response(serializer.data)
         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class SupplierViewSet(viewsets.ModelViewSet):
    queryset = Supplier.objects.all()
    serializer_class = SupplierSerializer
    filterset_class = SupplierFilter
    ordering_fields = '__all__'
    ordering = '-id'





