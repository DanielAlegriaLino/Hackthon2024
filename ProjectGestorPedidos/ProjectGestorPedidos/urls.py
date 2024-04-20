"""
URL configuration for ProjectGestorPedidos project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.urls import path
from AppPedidos import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name="home"),
    path('registro/', views.formulario_registro, name="formulario_registro"),
    path('get_best_n_products', views.get_best_n_products, name="get_n_most_related"),
    path('get_user_score', views.get_user_score, name="get_user_score"),
    path('registro/', views.formulario_registro, name="registro"),
    path('clientes/', views.clientes, name="clientes"),
    path('mensajes/', views.mensajes, name="mensajes"),
    path('metricas/', views.metricas, name="metricas"),
    path('landing/', views.lading, name="landing"),
    ]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
