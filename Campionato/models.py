# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Calendario(models.Model):
    #id = models.AutoField()
    campionato = models.IntegerField(blank=True, null=True)
    giornata = models.IntegerField(blank=True, null=True)
    ar = models.CharField(db_column='AR', blank=True, null=True, max_length = 150)  # Field name made lowercase.
    data = models.IntegerField(blank=True, null=True)
    locali = models.TextField(blank=True, null=True)
    ospiti = models.TextField(blank=True, null=True)
    retilocali = models.IntegerField(db_column='retiLocali', blank=True, null=True)  # Field name made lowercase.
    retiospiti = models.IntegerField(db_column='retiOspiti', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Calendario'


class Campionati(models.Model):
    #id = models.AutoField()
    nome = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Campionati'


class Classifica(models.Model):
    #id = models.AutoField()
    squadra = models.TextField(blank=True, null=True)
    punti = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Classifica'


class Risultati(models.Model):
    #id = models.AutoField()
    partita = models.IntegerField(blank=True, null=True)
    giornata = models.IntegerField(blank=True, null=True)
    retilocali = models.IntegerField(db_column='retiLocali', blank=True, null=True)  # Field name made lowercase.
    retiospiti = models.IntegerField(db_column='retiOspiti', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Risultati'


class Schedina(models.Model):
    #id = models.AutoField()
    giornata = models.TextField(blank=True, null=True)
    locali = models.TextField(blank=True, null=True)
    ospiti = models.TextField(blank=True, null=True)
    risultato = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Schedina'


class Squadre(models.Model):
    #id = models.AutoField()
    nome = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Squadre'


class Statistiche(models.Model):
    #id = models.AutoField()
    squadra = models.TextField(blank=True, null=True)
    partite = models.IntegerField(blank=True, null=True)
    vinte = models.IntegerField(blank=True, null=True)
    perse = models.IntegerField(blank=True, null=True)
    pareggiate = models.IntegerField(blank=True, null=True)
    punti = models.IntegerField(blank=True, null=True)
    golfatti = models.IntegerField(db_column='golFatti', blank=True, null=True)  # Field name made lowercase.
    golsubiti = models.IntegerField(db_column='golSubiti', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Statistiche'
