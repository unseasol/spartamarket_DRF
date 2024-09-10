from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticatedOrReadOnly
from .models import Product
from .serializers import ProductSerializer
from rest_framework.generics import ListAPIView
from rest_framework.pagination import PageNumberPagination

# Create your views here.
class ProductListView(APIView):
    permission_classes = [IsAuthenticatedOrReadOnly]
    pagenation_classes = PageNumberPagination
    # serializer_classes = 
    
    def post(self, request):
        title = request.data.get("title")
        content = request.data.get("content")
        image = request.data.get("image")
        product = Product.objects.create(
            title = title,
            content = content,
            image = image,
        )
        serializer = ProductSerializer(product)
        return Response(serializer.data)
    
    def get(self, request):
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)
    
# class ProductListAPIView(ListAPIView):