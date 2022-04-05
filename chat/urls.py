from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('chat/<str:room_name>/', views.room, name='room'),
    # path('<str:room_name>/', views.room, name='room'),
    # path('chat/hg/', views.room, name='room'),
]


