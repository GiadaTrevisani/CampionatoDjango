# Generated by Django 3.0.2 on 2020-05-17 17:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Campionato',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('nome', models.TextField()),
            ],
            options={
                'db_table': 'Campionato',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Giornata',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('nome', models.TextField()),
                ('num_giornata', models.IntegerField()),
            ],
            options={
                'db_table': 'Giornata',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Partita',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('data', models.TextField()),
                ('risultato_casa', models.IntegerField(blank=True, null=True)),
                ('risultato_ospite', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'Partita',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Squadra',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('nome', models.TextField()),
                ('codice', models.TextField(blank=True, null=True)),
            ],
            options={
                'db_table': 'Squadra',
                'managed': False,
            },
        ),
    ]
