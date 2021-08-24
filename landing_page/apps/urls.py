from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.apps_index, name='apps_index'),
    path('app/<str:name>/', views.app, name='app'),
]