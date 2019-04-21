from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='manager-main'),
    path('add_people/', views.add_people, name='manager-add_people'),
    path('rooms/', views.rooms, name='rooms'),
]
