from django.urls import path
from . import views


urlpatterns = [
    path('', views.index),
    path('new/', views.new),
    path('cart/', views.cart),
    path('cart/end/', views.end),
    path('create/product', views.create_view, name='create')
]
