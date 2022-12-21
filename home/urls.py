from . import views
from django.urls import path

urlpatterns = [
    path('', views.homes, name='homes')
]
