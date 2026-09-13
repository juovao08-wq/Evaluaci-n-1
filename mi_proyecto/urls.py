"""
URL configuration for mi_proyecto project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponse

def inicio_general(request):
    return HttpResponse("""
        <div style="font-family: sans-serif; text-align: center; padding: 40px;">
            <h1>Proyecto Django - Menú Principal</h1>
            <p>Selecciona la aplicación a la que deseas acceder:</p>
            <div style="margin-top: 20px;">
                <a href="/app1/" style="display: inline-block; margin: 10px; padding: 12px 24px; background: #2563eb; color: white; text-decoration: none; border-radius: 6px;">Ir a Vista 1 (Aplicación 1)</a>
                <a href="/app2/" style="display: inline-block; margin: 10px; padding: 12px 24px; background: #0284c7; color: white; text-decoration: none; border-radius: 6px;">Ir a Vista 1 (Aplicación 2)</a>
            </div>
        </div>
    """)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', inicio_general, name='home'),
    path('app1/', include('aplicacion1.urls')),
    path('app2/', include('aplicacion2.urls')),
]