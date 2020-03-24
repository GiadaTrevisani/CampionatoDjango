#file mysite/urls.py
from django.urls import path
from . import views 

urlpatterns = [
	path('', views.home_view, name='index'),
	path('Calendario/', views.calendario_view, name='Calendario'),
	path('Risultati/', views.risultati_view, name = 'Risultati'),
	path('Schedina/', views.schedina_view, name = 'Schedina'),
	path('Classifica/', views.classifica_view, name = 'Classifica'),
	path('Statistiche/', views.statistiche_view, name = 'Statistiche'), 
]
