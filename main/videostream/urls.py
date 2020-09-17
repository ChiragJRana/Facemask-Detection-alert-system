from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.index, name = 'index'),
    path('video_render', views.video_render, name = 'video_render'),
]