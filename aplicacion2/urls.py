from django.urls import path
from . import views

urlpatterns = [
    path('', views.vista_inicio, name='inicio'),
    path('vista2/', views.vista_servicios, name='vista2'),
]