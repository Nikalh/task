from django.urls import path, include

from task.network import views

""" Конфигурация URL для Network"""
urlpatterns = [
    path('create', views.SupplierListCreateView.as_view(),name='create-supplier'),
    path('list', views.SupplierListCreateView.as_view(),name='supplier-list'),
    path('<int:pk>', views.SupplierView.as_view(),name='supplier'),

]
