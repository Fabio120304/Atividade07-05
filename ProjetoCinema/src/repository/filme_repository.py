import sqlite3

class FilmeRepository:

    def salvar(self, filme):

        conexao = sqlite3.connect("cinema.db")

        cursor = conexao.cursor()

        sql = """

        INSERT INTO filme
        (titulo, duracao, genero, diretor)

        VALUES (?, ?, ?, ?)

        """

        cursor.execute(sql, (

            filme.titulo,

            filme.duracao,

            filme.genero,

            filme.diretor

        ))

        conexao.commit()

        conexao.close()

        print("Filme salvo com sucesso!")