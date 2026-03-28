from django.shortcuts import render

from rest_framework.decorators import api_view, action
from rest_framework.response import Response
from rest_framework import status, viewsets
from unicodedata import category

from .models import Category, Product
from .serializers import ProductSerializer, CategorySerializer

#api/products
#
# @api_view(['GET'])
# def product_list(request):
#     products = Product.objects.all()
#     serializer = ProductSerializer(products, many=True)
#     return Response(serializer.data)
#
#
# # /api/products/<int:id>/
# @api_view(['GET'])
# def product_detail(request, id):
#     try:
#         product = Product.objects.get(id=id)
#     except Product.DoesNotExist:
#         return Response(status=status.HTTP_404_NOT_FOUND)
#
#     serializer = ProductSerializer(product)
#     return Response(serializer.data)
#
#
# #/api/categories/
#
# @api_view(['GET'])
# def category_list(request):
#     category = Category.objects.all()
#     serializer = CategorySerializer(category, many=True)
#     return Response(serializer.data)
#
# #/api/categories/<int:id>/
# @api_view(['GET'])
# def category_detail(request, id):
#     try:
#         category = Category.objects.get(id=id)
#     except Category.DoesNotFound:
#         return Response(status=status.HTTP_404_NOT_FOUND)
#
#     serializer = CategorySerializer(category)
#     return Response(serializer.data)
#
# #/api/categories/<int:id>/products/
#
# @api_view(['GET'])
# def category_products(request, id):
#     try:
#         category = Category.objects.get(id=id)
#     except Category.DoesNotFound:
#         return Response(status=status.HTTP_404_NOT_FOUND)
#
#     products = Product.objects.filter(category=category)
#     serializer = ProductSerializer(products, many=True)
#     return Response(serializer.data)



class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

    @action(detail=True, methods=['get'])
    def products(self, request, pk=None):
        category = self.get_object()
        products = Product.objects.filter(category=category)
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer



