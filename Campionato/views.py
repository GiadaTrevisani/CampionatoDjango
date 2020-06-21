from django.shortcuts import render
from django.db import models
from .models import *
from django.http import HttpResponse 
from operator import itemgetter, attrgetter

def home_view(request):
	# setta l'anno di default al 2015
	anno = '2015'
	if 'dropanni' in  request.GET:
		anno = request.GET['dropanni']
		if anno == '2015':
			id_campionato = 1
		elif anno == '2016':
			id_campionato = 2
		else :
			id_campionato = 1
	else:
		id_campionato = 1


	partite = Partita.objects.all()
	partite = [p for p in partite if p.giornata.campionato.id == id_campionato]
	giornate = Giornata.objects.all()
	giornate = [g for g in giornate if g.campionato.id == id_campionato]
	num_campionati = Campionato.objects.all().count()
	num_goal = 0

	squadre = set()
	for p in partite:
		squadre.add(p.squadra_casa.nome)
		squadre.add(p.squadra_ospite.nome)
		num_goal = num_goal + p.risultato_ospite + p.risultato_casa

	num_partite = len(partite)
	num_giornate = len(giornate)
	num_squadre = len(squadre)

	
	context = {
		'num_partite': num_partite,
		'num_campionati': num_campionati,
		'num_giornate': num_giornate,
		'num_squadre': num_squadre,
		'num_goal': num_goal,
		'anno': anno,
		'id_campionato' : id_campionato,
		'home_active': "active",
		'title': "Home - Campionato"
	}
	return render(request, "home_view.html", context)

def calendario_view(request):
	anno = '2015'
	if 'dropanni' in  request.GET:
		anno = request.GET['dropanni']
		if anno == '2015':
			id_campionato = 1
		elif anno == '2016':
			id_campionato = 2
		else :
			id_campionato = 1
	else:
		id_campionato = 1


	if 'id' in request.GET:
		id = request.GET['id']
	else:
		id = -1

	partite = Partita.objects.all()
	# list comprehention che salva solo le partite di un dato anno
	partite = [p for p in partite if p.giornata.campionato.id == id_campionato]
	# calcolo il numero di giornate per poter calcolare il numero di partite di andata e quelle di ritorno ritorno
	maxg = max([g.num_giornata for g in Giornata.objects.all() if g.campionato.id == id_campionato])

	context = {
		'anno': anno,
		'ritorno': maxg // 2,
		'Partite': partite,
		'calendario_active': "active",
		'title': "Calendario - Campionato",
		'id': int(id)
	}
	return render(request, "calendario_view.html", context)

def risultati_view(request):
	anno = '2015'
	if 'dropanni' in  request.GET:
		anno = request.GET['dropanni']
		if anno == '2015':
			id_campionato = 1
		elif anno == '2016':
			id_campionato = 2
		else :
			id_campionato = 1
	else:
		id_campionato = 1


	if 'id' in request.GET:
		id = request.GET['id']
	else:
		id = -1

	partite = Partita.objects.all()
	# list comprehention che prende solo le parite per un anno specifico
	partite = [p for p in partite if p.giornata.campionato.id == id_campionato]
	# list comprehention che divide le partite per giornate 
	set_giornate = set([g.num_giornata for g in Giornata.objects.all() if g.campionato.id == id_campionato])
	
	# per ogni giornata rilevata faccio una lista dei risultati per quel giorno
	lista_per_giornate = [[p for p in partite if p.giornata.num_giornata == g] for g in set_giornate]	
	context = {
		'anno': anno,
		'Risultati': lista_per_giornate,
		'risultati_active': "active",
		'title': "Risultati - Campionato",
		'id': int(id)
	}
	return render(request, "risultati_view.html", context)

def schedina_view(request):
	''' i valori della schedina vengono assegnati: 
			1 --> vittoria squadra casa
			2 --> vittoria squadra ospite
			x --> pareggio
	'''
	anno = '2015'
	if 'dropanni' in  request.GET:
		anno = request.GET['dropanni']
		if anno == '2015':
			id_campionato = 1
		elif anno == '2016':
			id_campionato = 2
		else :
			id_campionato = 1
	else:
		id_campionato = 1


	partite = Partita.objects.all()
	partite = [p for p in partite if p.giornata.campionato.id == id_campionato]
	schedina = []

	for p in partite:
		if p.risultato_casa > p.risultato_ospite:
			schedina.append({
				'giornata': p.giornata.num_giornata,
				'casa': p.squadra_casa.nome,
				'ospite': p.squadra_ospite.nome,
				'risultato': 1,
				'id': p.id
			})

		elif p.risultato_ospite > p.risultato_casa:
			schedina.append({
				'giornata': p.giornata.num_giornata,
				'casa': p.squadra_casa.nome,
				'ospite': p.squadra_ospite.nome,
				'risultato': 2,
				'id': p.id
			})

		else:
			schedina.append({
				'giornata': p.giornata.num_giornata,
				'casa': p.squadra_casa.nome,
				'ospite': p.squadra_ospite.nome,
				'risultato': 'X',
				'id': p.id
			})


	context = {
		'anno': anno,
		'Schedina': schedina,
		'schedina_active': "active",
		'title': "Schedina - Campionato",
	}
	return render(request, "schedina_view.html", context)

def classifica_view(request):
	anno = '2015'
	if 'dropanni' in  request.GET:
		anno = request.GET['dropanni']
		if anno == '2015':
			id_campionato = 1
		elif anno == '2016':
			id_campionato = 2
		else :
			id_campionato = 1
	else:
		id_campionato = 1


	partite = Partita.objects.all()
	partite = [p for p in partite if p.giornata.campionato.id == id_campionato]
	classifica = {}

	for p in partite:

		if p.squadra_casa.nome in classifica:

			if p.risultato_casa > p.risultato_ospite :
				classifica[p.squadra_casa.nome] = classifica[p.squadra_casa.nome] + 3

			if p.risultato_casa == p.risultato_ospite :
				classifica[p.squadra_casa.nome] = classifica[p.squadra_casa.nome] + 1
		else:

			if p.risultato_casa > p.risultato_ospite :
				classifica[p.squadra_casa.nome] = 3

			elif p.risultato_casa == p.risultato_ospite :
				classifica[p.squadra_casa.nome] = 1

			else:
				classifica[p.squadra_casa.nome] = 0

		if p.squadra_ospite.nome in classifica:
			
			if p.risultato_ospite > p.risultato_casa:
				classifica[p.squadra_ospite.nome] = classifica[p.squadra_ospite.nome] + 3

			if p.risultato_ospite == p.risultato_casa:
				classifica[p.squadra_ospite.nome] = classifica[p.squadra_ospite.nome] + 1

		else:

			if p.risultato_ospite > p.risultato_casa :
				classifica[p.squadra_ospite.nome] = 3

			elif p.risultato_casa == p.risultato_ospite :
				classifica[p.squadra_ospite.nome] = 1

			else:
				classifica[p.squadra_ospite.nome] = 0

	classifica_list = []

	for key, value in classifica.items():
		temp = [key,value]
		classifica_list.append(temp)
	
	# crea la lista delle squadre per la classifica e le ordina in base al numero di punti ottenuti
	classifica_list = sorted(classifica_list, key=itemgetter(1), reverse = True)
	classifica_list = [[i+1, x[0], x[1]] for i,x in enumerate(classifica_list)]

	context = {
		'anno': anno,
		'Classifica': classifica_list,
		'classifica_active': "active",
		'title': "Classifica - Campionato"
	}
	return render(request, "classifica_view.html", context)

def statistiche_view(request):
	anno = '2015'
	if 'dropanni' in  request.GET:
		anno = request.GET['dropanni']
		if anno == '2015':
			id_campionato = 1
		elif anno == '2016':
			id_campionato = 2
		else :
			id_campionato = 1
	else:
		id_campionato = 1


	partite = Partita.objects.all()
	partite = [p for p in partite if p.giornata.campionato.id == id_campionato]
	statistica = {}

	for p in partite:
		
		if p.risultato_casa == p.risultato_ospite:

			if p.squadra_casa.nome in statistica:
				statistica[p.squadra_casa.nome]['punti'] = statistica[p.squadra_casa.nome]['punti'] + 1
				statistica[p.squadra_casa.nome]['giocate'] = statistica[p.squadra_casa.nome]['giocate'] + 1
				statistica[p.squadra_casa.nome]['vinte'] = statistica[p.squadra_casa.nome]['vinte'] + 0
				statistica[p.squadra_casa.nome]['perse'] = statistica[p.squadra_casa.nome]['perse'] + 0
				statistica[p.squadra_casa.nome]['pareggiate'] = statistica[p.squadra_casa.nome]['pareggiate'] + 1
				statistica[p.squadra_casa.nome]['goal_fatti'] = statistica[p.squadra_casa.nome]['goal_fatti'] + p.risultato_casa
				statistica[p.squadra_casa.nome]['goal_subiti'] = statistica[p.squadra_casa.nome]['goal_subiti'] + p.risultato_ospite

			else:
				statistica[p.squadra_casa.nome] = {
					'nome': p.squadra_casa.nome,
					'punti': 1,
					'giocate': 1,
					'vinte': 0,
					'perse': 0,
					'pareggiate': 1,
					'goal_fatti': p.risultato_casa,
					'goal_subiti': p.risultato_ospite
				}

			if p.squadra_ospite.nome in statistica:
				statistica[p.squadra_ospite.nome]['punti'] = statistica[p.squadra_ospite.nome]['punti'] + 1
				statistica[p.squadra_ospite.nome]['giocate'] = statistica[p.squadra_ospite.nome]['giocate'] + 1
				statistica[p.squadra_ospite.nome]['vinte'] = statistica[p.squadra_ospite.nome]['vinte'] + 0
				statistica[p.squadra_ospite.nome]['perse'] = statistica[p.squadra_ospite.nome]['perse'] + 0
				statistica[p.squadra_ospite.nome]['pareggiate'] = statistica[p.squadra_ospite.nome]['pareggiate'] + 1
				statistica[p.squadra_ospite.nome]['goal_fatti'] = statistica[p.squadra_ospite.nome]['goal_fatti'] + p.risultato_ospite
				statistica[p.squadra_ospite.nome]['goal_subiti'] = statistica[p.squadra_ospite.nome]['goal_subiti'] + p.risultato_casa

			else:
				statistica[p.squadra_ospite.nome] = {
					'nome': p.squadra_ospite.nome,
					'punti': 1,
					'giocate': 1,
					'vinte': 0,
					'perse': 0,
					'pareggiate': 1,
					'goal_fatti': p.risultato_ospite,
					'goal_subiti': p.risultato_casa
				}

		elif p.risultato_casa > p.risultato_ospite:

			if p.squadra_casa.nome in statistica:
				statistica[p.squadra_casa.nome]['punti'] = statistica[p.squadra_casa.nome]['punti'] + 3
				statistica[p.squadra_casa.nome]['giocate'] = statistica[p.squadra_casa.nome]['giocate'] + 1
				statistica[p.squadra_casa.nome]['vinte'] = statistica[p.squadra_casa.nome]['vinte'] + 1
				statistica[p.squadra_casa.nome]['perse'] = statistica[p.squadra_casa.nome]['perse'] + 0
				statistica[p.squadra_casa.nome]['pareggiate'] = statistica[p.squadra_casa.nome]['pareggiate'] + 0
				statistica[p.squadra_casa.nome]['goal_fatti'] = statistica[p.squadra_casa.nome]['goal_fatti'] + p.risultato_casa
				statistica[p.squadra_casa.nome]['goal_subiti'] = statistica[p.squadra_casa.nome]['goal_subiti'] + p.risultato_ospite

			else:
				statistica[p.squadra_casa.nome] = {
					'nome': p.squadra_casa.nome,
					'punti': 3,
					'giocate': 1,
					'vinte': 1,
					'perse': 0,
					'pareggiate': 0,
					'goal_fatti': p.risultato_casa,
					'goal_subiti': p.risultato_ospite
				}

			if p.squadra_ospite.nome in statistica:
				statistica[p.squadra_ospite.nome]['punti'] = statistica[p.squadra_ospite.nome]['punti'] + 0
				statistica[p.squadra_ospite.nome]['giocate'] = statistica[p.squadra_ospite.nome]['giocate'] + 1
				statistica[p.squadra_ospite.nome]['vinte'] = statistica[p.squadra_ospite.nome]['vinte'] + 0
				statistica[p.squadra_ospite.nome]['perse'] = statistica[p.squadra_ospite.nome]['perse'] + 1
				statistica[p.squadra_ospite.nome]['pareggiate'] = statistica[p.squadra_ospite.nome]['pareggiate'] + 0
				statistica[p.squadra_ospite.nome]['goal_fatti'] = statistica[p.squadra_ospite.nome]['goal_fatti'] + p.risultato_ospite
				statistica[p.squadra_ospite.nome]['goal_subiti'] = statistica[p.squadra_ospite.nome]['goal_subiti'] + p.risultato_casa

			else:
				statistica[p.squadra_ospite.nome] = {
					'nome': p.squadra_ospite.nome,
					'punti': 0,
					'giocate': 1,
					'vinte': 0,
					'perse': 1,
					'pareggiate': 0,
					'goal_fatti': p.risultato_ospite,
					'goal_subiti': p.risultato_casa
				}

		else:

			if p.squadra_casa.nome in statistica:
				statistica[p.squadra_casa.nome]['punti'] = statistica[p.squadra_casa.nome]['punti'] + 0
				statistica[p.squadra_casa.nome]['giocate'] = statistica[p.squadra_casa.nome]['giocate'] + 1
				statistica[p.squadra_casa.nome]['vinte'] = statistica[p.squadra_casa.nome]['vinte'] + 0
				statistica[p.squadra_casa.nome]['perse'] = statistica[p.squadra_casa.nome]['perse'] + 1
				statistica[p.squadra_casa.nome]['pareggiate'] = statistica[p.squadra_casa.nome]['pareggiate'] + 0
				statistica[p.squadra_casa.nome]['goal_fatti'] = statistica[p.squadra_casa.nome]['goal_fatti'] + p.risultato_casa
				statistica[p.squadra_casa.nome]['goal_subiti'] = statistica[p.squadra_casa.nome]['goal_subiti'] + p.risultato_ospite

			else:
				statistica[p.squadra_casa.nome] = {
					'nome': p.squadra_casa.nome,
					'punti': 0,
					'giocate': 1,
					'vinte': 0,
					'perse': 1,
					'pareggiate': 0,
					'goal_fatti': p.risultato_casa,
					'goal_subiti': p.risultato_ospite
				}

			if p.squadra_ospite.nome in statistica:
				statistica[p.squadra_ospite.nome]['punti'] = statistica[p.squadra_ospite.nome]['punti'] + 3
				statistica[p.squadra_ospite.nome]['giocate'] = statistica[p.squadra_ospite.nome]['giocate'] + 1
				statistica[p.squadra_ospite.nome]['vinte'] = statistica[p.squadra_ospite.nome]['vinte'] + 1
				statistica[p.squadra_ospite.nome]['perse'] = statistica[p.squadra_ospite.nome]['perse'] + 0
				statistica[p.squadra_ospite.nome]['pareggiate'] = statistica[p.squadra_ospite.nome]['pareggiate'] + 0
				statistica[p.squadra_ospite.nome]['goal_fatti'] = statistica[p.squadra_ospite.nome]['goal_fatti'] + p.risultato_ospite
				statistica[p.squadra_ospite.nome]['goal_subiti'] = statistica[p.squadra_ospite.nome]['goal_subiti'] + p.risultato_casa

			else:
				statistica[p.squadra_ospite.nome] = {
					'nome': p.squadra_ospite.nome,
					'punti': 3,
					'giocate': 1,
					'vinte': 1,
					'perse': 0,
					'pareggiate': 0,
					'goal_fatti': p.risultato_ospite,
					'goal_subiti': p.risultato_casa
				}

	statistica = list(statistica.values())

	statistica.sort(key=lambda x:x['punti'], reverse=True)

	context = {
		'anno': anno,
		'Statistiche': statistica,
		'statistiche_active': "active",
		'title': "Statistiche - Campionato"
	}
	return render(request, "statistiche_view.html", context)