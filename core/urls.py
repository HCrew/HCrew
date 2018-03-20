from django.urls import path
from . import views

urlpatterns = [
    path('', views.login, name='login'),
    path('contato/', views.contato, name='contato'),
    path('index/', views.index, name='index'),
]
