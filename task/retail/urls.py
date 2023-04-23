from django.urls import path

from task.retail import views

""" Конфигурация URL для RetailNetwork"""
urlpatterns = [
    path('create', views.RetailNetworkListCreateView.as_view(),name='create-retailnet'),
    path('list', views.RetailNetworkListCreateView.as_view(),name='retailnet-list'),
    path('<int:pk>', views.RetailNetworkView.as_view(),name='retailnet'),

]
