# Generated by Django 3.0.2 on 2020-01-28 09:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Calendario',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('campionato', models.IntegerField(blank=True, null=True)),
                ('giornata', models.IntegerField(blank=True, null=True)),
                ('ar', models.CharField(blank=True, db_column='AR', max_length=150, null=True)),
                ('data', models.IntegerField(blank=True, null=True)),
                ('locali', models.TextField(blank=True, null=True)),
                ('ospiti', models.TextField(blank=True, null=True)),
                ('retilocali', models.IntegerField(blank=True, db_column='retiLocali', null=True)),
                ('retiospiti', models.IntegerField(blank=True, db_column='retiOspiti', null=True)),
            ],
            options={
                'db_table': 'Calendario',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Campionati',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.TextField(blank=True, null=True)),
            ],
            options={
                'db_table': 'Campionati',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Classifica',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('squadra', models.TextField(blank=True, null=True)),
                ('punti', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'Classifica',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Risultati',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('partita', models.IntegerField(blank=True, null=True)),
                ('giornata', models.IntegerField(blank=True, null=True)),
                ('retilocali', models.IntegerField(blank=True, db_column='retiLocali', null=True)),
                ('retiospiti', models.IntegerField(blank=True, db_column='retiOspiti', null=True)),
            ],
            options={
                'db_table': 'Risultati',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Schedina',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('giornata', models.TextField(blank=True, null=True)),
                ('locali', models.TextField(blank=True, null=True)),
                ('ospiti', models.TextField(blank=True, null=True)),
                ('risultato', models.TextField(blank=True, null=True)),
            ],
            options={
                'db_table': 'Schedina',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Squadre',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.TextField(blank=True, null=True)),
            ],
            options={
                'db_table': 'Squadre',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Statistiche',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('squadra', models.TextField(blank=True, null=True)),
                ('partite', models.IntegerField(blank=True, null=True)),
                ('vinte', models.IntegerField(blank=True, null=True)),
                ('perse', models.IntegerField(blank=True, null=True)),
                ('pareggiate', models.IntegerField(blank=True, null=True)),
                ('punti', models.IntegerField(blank=True, null=True)),
                ('golfatti', models.IntegerField(blank=True, db_column='golFatti', null=True)),
                ('golsubiti', models.IntegerField(blank=True, db_column='golSubiti', null=True)),
            ],
            options={
                'db_table': 'Statistiche',
                'managed': False,
            },
        ),
    ]
