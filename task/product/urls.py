from django.urls import path, include

from task.product import views

""" Конфигурация URL для Product"""
urlpatterns = [
    path('create', views.ProductListCreateView.as_view(),name='create-product'),
    path('list', views.ProductListCreateView.as_view(),name='product-list'),
    path('<int:pk>', views.ProductView.as_view(),name='product'),

]
