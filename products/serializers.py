from .models import *
from rest_framework import serializers


class QuantitySerializers(serializers.ModelSerializer):
    class Meta:
        model = QuantityVariant
        fields = "__all__"


class CategorySerializers(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"


class ProductSerializers(serializers.ModelSerializer):
    category = CategorySerializers()
    quantity_type = QuantitySerializers()

    class Meta:
        model = Product
        fields = '__all__'
        # exclude = ['id', 'product_name']
