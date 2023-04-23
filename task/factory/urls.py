from django.urls import path
from task.factory import views

""" Конфигурация URL для Factory"""
urlpatterns = [
    path('create', views.FactoryListCreateView.as_view(),name='create-factory'),
    path('list', views.FactoryListCreateView.as_view(),name='factory-list'),
    path('<int:pk>', views.FactoryView.as_view(),name='factory'),
    ]