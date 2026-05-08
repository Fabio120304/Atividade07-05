import sqlite3

def conectar():

    conexao = sqlite3.connect("cinema.db")

    return conexao