import sqlite3

class main:

    def __init__(self):
        conn = sqlite3.connect('database.sqlite')
        cursor = conn.cursor()
        print("Opened database successfully")

        cursor.execute('''CREATE TABLE SONGS IF NOT EXISTS
                (ID INT PRIMARY KEY     NOT NULL AUTO_INCREMENT,
                NAME           TEXT    NOT NULL)''')

        cursor.execute('''CREATE TABLE ARTISTS IF NOT EXISTS
                (ID INT PRIMARY KEY     NOT NULL AUTO_INCREMENT,
                NAME           TEXT    NOT NULL)''')

        cursor.execute('''CREATE TABLE FEATURES IF NOT EXISTS
                (ID INT PRIMARY KEY     NOT NULL AUTO_INCREMENT,
                SONG           INT      NOT NULL,
                ARTIST         INT     NOT NULL)''')

        cursor.execute('''CREATE TABLE SINGERS IF NOT EXISTS
                (ID INT PRIMARY KEY     NOT NULL AUTO_INCREMENT,
                SONG           INT      NOT NULL,
                ARTIST         INT     NOT NULL)''')


    def saveSong(self,tittle,artist,featuring,producer):
        print(tittle)
        conn = sqlite3.connect('my_database.sqlite')
        cursor = conn.cursor()
        cursor.execute("INSERT INTO SONGS (NAME) VALUES ('"+tittle+"')")
        conn.commit()
        conn.close()