from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.first_app, name='first_app'),
    path('<int:jewel_id>/', views.jewel_detail, name='jewel_detail'),
]