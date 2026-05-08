import sqlite3

conexao = sqlite3.connect("cinema.db")

cursor = conexao.cursor()

cursor.execute("""

CREATE TABLE IF NOT EXISTS filme (

    id INTEGER PRIMARY KEY AUTOINCREMENT,

    titulo TEXT,

    duracao INTEGER,

    genero TEXT,

    diretor TEXT

)

""")

conexao.commit()

print("Tabela criada com sucesso!")