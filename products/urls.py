from products import views
from django.urls import path


urlpatterns = [
    path('products', views.ProductAPIView.as_view()),
    path('demo', views.DemoAPIView.as_view())
]
