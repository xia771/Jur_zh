from django.urls import path
from . import views

urlpatterns = [
    path('shouye', views.shouye, name='shouye'),
    path('users/', views.users, name='users'),
    path('login/', views.login, name='login'),
    path('zhuce/', views.user_rgb, name='user_rgb'),
    path('', views.index, name='index'),
]
