# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Campionato(models.Model):
    id = models.IntegerField(primary_key=True)
    nome = models.TextField()

    class Meta:
        managed = False
        db_table = 'Campionato'


class Giornata(models.Model):
    id = models.IntegerField(primary_key=True)
    nome = models.TextField()
    num_giornata = models.IntegerField()
    campionato = models.ForeignKey(Campionato, models.DO_NOTHING, db_column="campionato")

    class Meta:
        managed = False
        db_table = 'Giornata'

class Squadra(models.Model):
    id = models.IntegerField(primary_key=True)
    nome = models.TextField()
    codice = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Squadra'

class Partita(models.Model):
    id = models.IntegerField(primary_key=True)
    data = models.TextField()
    giornata = models.ForeignKey(Giornata, models.DO_NOTHING, db_column="giornata")
    squadra_casa = models.ForeignKey(Squadra, models.DO_NOTHING, related_name="squadra_casa", db_column="squadra_casa")
    squadra_ospite = models.ForeignKey(Squadra, models.DO_NOTHING, related_name="squadra_ospite", db_column="squadra_ospite")
    risultato_casa = models.IntegerField(blank=True, null=True)
    risultato_ospite = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Partita'

