"""
URL configuration for bookstore project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from bookstore_app.views import home, about, search_book, insert_author, insert_book, insert_publisher, search_results

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home),
    path('nosotros/', about),
    path('buscar/libro/', search_book),
    path('insertar/autor/', insert_author),
    path('insertar/libro/', insert_book),
    path('insertar/editorial/', insert_publisher),
    path('busqueda/resultados/', search_results),
]
