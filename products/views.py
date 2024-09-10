from django.shortcuts import render
from rest_framework.views import APIView
from .models import Product
from rest_framework.response import Response

# Create your views here.
class ProductListView(APIView):
    def post(self, request):
        title = request.data.get("title")
        content = request.data.get("content")
        image = request.data.get("image")
        
        product = Product.objects.create(
            title = title,
            content = content,
            image = image,
        )
        
        return Response()