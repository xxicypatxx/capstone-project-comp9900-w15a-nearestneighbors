"""filmfinder URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from login.views import index_view, login_view, register_view, logout_view
from movies.views import search_view


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth', include('rest_framework.urls')),
    path('index/', index_view),
    path('login/', login_view),
    path('register/', register_view),
    path('logout/', logout_view),
    path('search/', search_view),
    
    #URL for showing all movies, movies detail,
    #add to wishlist, view all reviews for a specific movie,
    #create a new review for a specific movie
    path('movies/', include('movies.urls')),
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)  #movies poster images

urlpatterns += staticfiles_urlpatterns()