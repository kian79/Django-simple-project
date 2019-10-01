from django.urls import path, include
from . import views

urlpatterns = [
    path('index/', views.index_render, name='index'),
    path('', views.base_render, name='base'),
    path('register/', views.register_render, name='register'),
    path('logout/', views.user_logout, name='logout'),
    # path('login/',views.user_login,name='login'),
    path('special/', views.special, name='special'),
]
