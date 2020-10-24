from django.urls import path
from .views import *

urlpatterns = [
    path('', tasksList, name='tasksList'),
    path('ingresar', login, name='login'),
    path('salir', logout, name='logout'),
]
