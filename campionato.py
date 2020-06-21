import json
import sqlite3
import sys
import argparse
import os

def create_connection(db_file):
	# prende in ingresso il nome del database e eprova a creare una connessione, altrimenti lancia una exception.
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Error as e:
        print(e)

    return conn

def create_tables(conn):
	# questa funzione prende in ingresso la connessione al database e crea le tabelle se non esistono.
    create_campionato = """ CREATE TABLE IF NOT EXISTS Campionato (
                                id INTEGER PRIMARY KEY AUTOINCREMENT,
                                nome TEXT NOT NULL
                            ); """

    create_giornata = """ CREATE TABLE IF NOT EXISTS Giornata (
                            id INTEGER PRIMARY KEY AUTOINCREMENT,
                            nome TEXT NOT NULL,
                            num_giornata INTEGER NOT NULL,
                            campionato INTEGER NOT NULL,
                            FOREIGN KEY(campionato) REFERENCES Campionato(id)
                        ); """

    create_squadra = """ CREATE TABLE IF NOT EXISTS Squadra (
                            id INTEGER PRIMARY KEY AUTOINCREMENT,
                            nome TEXT NOT NULL,
                            codice TEXT
                        ); """

    create_partita = """ CREATE TABLE IF NOT EXISTS Partita (
                            id INTEGER PRIMARY KEY AUTOINCREMENT,
                            data TEXT NOT NULL,
                            giornata INTEGER NOT NULL,
                            squadra_casa INTEGER NOT NULL,
                            squadra_ospite INTEGER NOT NULL,
                            risultato_casa INTEGER,
                            risultato_ospite INTEGER,
                            FOREIGN KEY(giornata) REFERENCES Giornata(id),
                            FOREIGN KEY(squadra_casa) REFERENCES Squadra(id),
                            FOREIGN KEY(squadra_ospite) REFERENCES Squadra(id)
                        ); """
    #prendiamo un cursore dalla connessione per esegure le query con la funzone execute (che prende in ingresso una stringa)
    c = conn.cursor()
    c.execute(create_campionato)
    c.execute(create_giornata)
    c.execute(create_squadra)
    c.execute(create_partita)

    # la funzione commit mi salva nel file tutti gli inserimenti fatti nella ram dal comando execute
    conn.commit()

def insert_campionato(campionato, conn):
    c = conn.cursor()
    name = campionato['name']

    c.execute("SELECT * FROM Campionato WHERE nome='{}'".format(name))
    row = c.fetchone()

    if row is not None:
        print("Campionato già inserito")
        sys.exit(-3)

    c.execute("INSERT INTO Campionato (nome) VALUES('{}')".format(name))

    # recupero l'id del campionato che ho appena inserito.
    id_campionato = c.lastrowid

    conn.commit()

    print("Campionato registrato nel database.")

    # serve per leggere tutto il file e trovare tutti i nomi delle squadre che partecipano al campionato.
    squadre = set() # set è una struttura dati che rappresenta un insieme e quidi effettua lui i controlli di elementi duplicati.

    for giornata in campionato['rounds']:
        for match in giornata['matches']:
            squadra1 = match['team1']
            squadra2 = match['team2']

            # non posso aggiungere un dizionario perchè set non li accetta, allora prendo una tupla dei valori.
            squadre.add(tuple(squadra1.values()))
            squadre.add(tuple(squadra2.values()))

    squadre = list(squadre)

    # in s[0] c'è la chiave (key), in s[1] c'è il nome e in s[2] c'è il codice della squadra
    for s in squadre:
        c.execute("SELECT * FROM Squadra WHERE nome='{}'".format(s[1]))
        row = c.fetchone()

        if row is None:
            c.execute("INSERT INTO Squadra (nome, codice) VALUES ('{}', '{}')".format(s[1], s[2]))

    conn.commit()

    c.execute("SELECT * FROM Squadra;")

    db_squadre = c.fetchall()

    # dict comprehention che ad ogni nome di squadra associa l'id
    db_squadre_dict = {row[1]: row[0] for row in db_squadre}

    for giornata in campionato['rounds']:
        nome_giornata = giornata['name']
        num_giornata = int(nome_giornata.split('^')[0])
        c.execute("INSERT INTO Giornata (nome, num_giornata, campionato) VALUES ('{}', {}, {})".format(nome_giornata, num_giornata, id_campionato))
        id_giornata = c.lastrowid

        for partita in giornata["matches"]:
            data_partita = partita["date"]
            squadra_casa_name = partita["team1"]["name"]
            squadra_ospite_name = partita["team2"]["name"]
            squadra_casa_id = db_squadre_dict[squadra_casa_name]
            squadra_ospite_id = db_squadre_dict[squadra_ospite_name]
            risultato_casa = partita["score1"]
            risultato_ospite = partita["score2"]
            c.execute("INSERT INTO Partita (data, giornata, squadra_casa, squadra_ospite, risultato_casa, risultato_ospite) VALUES ('{}', {}, {}, {}, {}, {})".format(data_partita, id_giornata, squadra_casa_id, squadra_ospite_id, risultato_casa, risultato_ospite))
        conn.commit()


if __name__ == "__main__":
	# uso argparse per leggere il nome del file json da linea di comando.
    parser = argparse.ArgumentParser(
        description='Importa JSON nel database.')
    parser.add_argument(
        '--file',
        type=str,
        help='Percorso del file JSON da importare.')

    args = parser.parse_args()

    filename = args.file

    if not os.path.exists(filename):
        print("File non esistente")
        sys.exit(-1)

    with open(filename) as f:
    	#legge il file json e trasforma quello che c'è scritto nel file in tipi di dato python, in questo caso un dizionario.
        campionato = json.load(f)

    # apro la connessione con il database e se non esiste sqlite3 me lo crea.
    conn = create_connection('campionato.db')

    if conn is None:
        print("Errore")
        sys.exit(-2)

    create_tables(conn)

    insert_campionato(campionato, conn)

    conn.close()
    