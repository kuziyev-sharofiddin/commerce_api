from django.shortcuts import render
from .serializers import *
from .models import *
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import BasePermission, IsAuthenticated
# Create your views here.


class DemoAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        return Response({"success": "Admin You are authenticated"})


class ProductAPIView(APIView):
    def get(self, request):
        category = self.request.query_params.get('category')
        if category:
            queryset = Product.objects.filter(category__category_name=category)
            print(queryset)
        else:
            print(category)
            queryset = Product.objects.all()
        serializer = ProductSerializers(queryset, many=True)
        return Response({'count': len(serializer.data), 'data': serializer.data})
