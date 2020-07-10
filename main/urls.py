"""main URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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

from game import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.show_home, name='home'),
    path('new_game/<str:session_id>/', views.new_game, name='new_game'),
    path('game_created/<int:game_id>/', views.game_created, name='game_created'),
    path('games_list/', views.games_list, name='games_list'),
    path('games_list/<int:game_id>/', views.game, name='game'),
    path('games_finished/', views.games_finished, name='games_finished'),
    path('games_finished/<int:game_id>/', views.game_finished, name='game_finished'),
]
