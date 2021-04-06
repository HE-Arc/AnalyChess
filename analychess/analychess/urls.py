"""analychess URL Configuration

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
from django.conf import settings
from django.conf.urls import include, url
from django.contrib import admin
from .views import LogoutView, TestView
from django.urls import path, include
from django.contrib.auth.models import User
from rest_framework import routers, serializers, viewsets
from rest_framework.authtoken.views import obtain_auth_token
import debug_toolbar

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)

urlpatterns = [
    path('api/admin/', admin.site.urls),
    path("api/", include('api.urls')),
    path('__debug__/', include(debug_toolbar.urls)),
    path('api/auth-api/', include('rest_framework.urls', namespace='rest_framework')),
    path('api/login', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/login/refresh', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/login/verify/', TokenVerifyView.as_view(), name='token_verify'),
    path('api/logout', LogoutView.as_view(), name='auth_logout'),
    path('api/test', TestView.as_view(), name='test'),
    
]   

