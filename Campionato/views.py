from django.shortcuts import render
from django.db import models
from .models import *
from django.http import HttpResponse 

def home_view(request):
	context = {
		'home_active': "active",
		'title': "Home - Campionato"
	}
	return render(request, "home_view.html", context)

def calendario_view(request):
	obj = Calendario.objects.all()
	context = {
		'Calendario': obj,
		'calendario_active': "active",
		'title': "Calendario - Campionato"
	}
	return render(request, "calendario_view.html", context)

def risultati_view(request):
	obj = Calendario.objects.all()
	#prendo tutte le giornate con la list comprehension e poi ne faccio un set (lista senza doppioni)
	set_giornate = set([c.giornata for c in obj])
	# per ogni giornata rilevata faccio una lista dei risultati per quel giorno
	lista_per_giornate = [[c for c in obj if c.giornata == g] for g in set_giornate]
	context = {
		'Risultati': lista_per_giornate,
		'risultati_active': "active",
		'title': "Risultati - Campionato"
	}
	return render(request, "risultati_view.html", context)

def schedina_view(request):
	obj = Schedina.objects.all()
	context = {
		'Schedina': obj,
		'schedina_active': "active",
		'title': "Schedina - Campionato"
	}
	return render(request, "schedina_view.html", context)

def classifica_view(request):
	obj = Classifica.objects.all()
	context = {
		'Classifica': obj,
		'classifica_active': "active",
		'title': "Classifica - Campionato"
	}
	return render(request, "classifica_view.html", context)

def statistiche_view(request):
	obj = Statistiche.objects.all()
	context = {
		'Statistiche': obj,
		'statistiche_active': "active",
		'title': "Statistiche - Campionato"
	}
	return render(request, "statistiche_view.html", context)