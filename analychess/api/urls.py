from django.urls import path
from . import views

urlpatterns = [
    path('user', views.UserList.as_view(), name='user-list'),
    path('user/<int:pk>', views.UserDetail.as_view()),
    path('game', views.GameList.as_view(), name='game-list'),
    path('game/<int:pk>', views.GameDetail.as_view()),
    path('', views.api_root),
    
]