from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework import status
from .serializers import CategorySerializer, ProductSerializer
from products import serializers
from .models import Product, Category
from rest_framework import viewsets, generics
from rest_framework.views import APIView
# Create your views here.


class ProductViewSet(generics.ListCreateAPIView):
    queryset= Product.objects.all()
    serializer_class = ProductSerializer
    # parser_classes = (MultiPartParser, FormParser)
    # search_fields=['name', 'description']


class CategoryViewSet(viewsets.ModelViewSet):
    queryset= Category.objects.all()
    serializer_class = CategorySerializer

