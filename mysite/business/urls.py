from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('redirect/', views.redirect, name='passing'),
    path('dashboard/', views.dashboard, name='reached'),
    path('redirect/<str:room_name>/', views.make_board, name='room'),
]