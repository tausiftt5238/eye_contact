from django.urls import path 

from . import views 

urlpatterns = [
    path('', views.index, name='index'),
    path('move_machine/', views.move_machine, name='move_machine'),
]