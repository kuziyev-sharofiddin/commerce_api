from carts.views import *
from django.urls import path


urlpatterns = [
    path('cart', CartAPIView.as_view()),
]
