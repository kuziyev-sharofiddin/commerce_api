from .models import *
from rest_framework import serializers
from products.serializers import *


class CartSerializers(serializers.ModelSerializer):
    class Meta:
        model = Cart
        fields = "__all__"


class CartItemsSerializers(serializers.ModelSerializer):
    product = ProductSerializers()

    class Meta:
        model = CartItems
        fields = "__all__"
