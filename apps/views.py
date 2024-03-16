# Create your views here.
from rest_framework import viewsets
from rest_framework.viewsets import ModelViewSet

from apps.models import Category, Product
from apps.serializers import CategorySerializer, ProductSerializer


class CategoryViewSet(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
