"""LITReview URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.conf.urls import include
from django.contrib import admin
from django.urls import path
from LITReview.views import home_view, flux_view, abos_view, posts_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('user/', include('django.contrib.auth.urls')),
    path('', home_view, name= 'home'),
    path('flux/', flux_view, name= 'flux'),
    path('abos/', abos_view, name= 'abos'),
    path('posts/', posts_view, name= 'posts'),
    path('flux/create_ticket/', include('ticket.urls',namespace='ticket')),
    path('flux/', posts_view, name= 'posts'),


]
