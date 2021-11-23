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
from LITReview.views import create_user, delete_view, home_view, flux_view, abos_view, log_user, logout_user, \
    modify_view, posts_view, unfollow_view
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('user/', include('django.contrib.auth.urls')),
    path('', home_view, name='home'),
    path('flux/', flux_view, name='flux'),
    path('abos/', abos_view, name='abos'),
    path('posts/', posts_view, name='posts'),
    path('flux/create_ticket/', include('ticket.urls', namespace='ticket')),
    path('flux/create_user', create_user, name='create_user'),
    path('flux/log_user', log_user, name='log_user'),
    path('logout_user/', logout_user, name='logout_user'),
    path('flux/create_review/', include('review.urls', namespace='review')),
    path('posts/modify/<str:content_type>/<int:content_id>', modify_view, name='modify'),
    path('posts/delete/<str:content_type>/<int:content_id>', delete_view, name='delete'),
    path('abos/unfollow/<str:username>', unfollow_view, name='unfollow')


] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
