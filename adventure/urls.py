from django.conf.urls import url
from django.urls import path
from . import api, views

urlpatterns = [
    url('init', api.initialize),
    url('move', api.move),
    url('say', api.say),
    path('rooms', views.allRooms),
    path('rooms/<int:pk>/', views.singleRoom),
]