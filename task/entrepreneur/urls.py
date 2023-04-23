from django.urls import path, include

from task.entrepreneur import views

""" Конфигурация URL для Entrepreneur"""
urlpatterns = [
    path('create', views.IndividualEntrepreneurListCreateView.as_view(),name='create-entrepreneur'),
    path('list', views.IndividualEntrepreneurListCreateView.as_view(),name='entrepreneur-list'),
    path('<int:pk>', views.IndividualEntrepreneurView.as_view(),name='entrepreneur'),

]