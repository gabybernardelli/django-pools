from django.urls import path

# importar da pasta atual o arquivo views.py
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('sobre/', views.sobre, name='sobre'),
    path('perguntas', views.ultimas_perguntas, name='ultimas_perguntas')
]

