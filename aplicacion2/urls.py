from django.urls import path
from . import views

urlpatterns = [
    path('', views.vista_inicio, name='app2_inicio'),
    path('vista2/', views.vista_servicios, name='app2_vista2'),
]