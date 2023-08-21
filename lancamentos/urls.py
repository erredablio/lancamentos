"""
URL configuration for lancamentos project.

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
from fluxo import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('categoria/', views.select_categoria, name='select_categoria'),
    path('categoria/insert/', views.insert_categoria, name='insert_categoria'),
    path('categoria/update/<int:id>', views.update_categoria, name='update_categoria'),
    path('categoria/delete/<int:id>', views.delete_categoria, name='delete_categoria'),
    path('ator/', views.select_ator, name='select_ator'),
    path('ator/insert/', views.insert_ator, name='insert_ator'),
    path('ator/update/<int:id>', views.update_ator, name='update_ator'),
    path('ator/delete/<int:id>', views.delete_ator, name='delete_ator'),
    path('lancamento/', views.select_lancamento, name='select_lancamento'),
    path('lancamento/insert/', views.insert_lancamento, name='insert_lancamento'),
]
