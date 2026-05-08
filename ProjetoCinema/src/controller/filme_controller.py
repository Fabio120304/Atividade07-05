from src.service.filme_service import FilmeService

class FilmeController:

    def __init__(self):

        self.service = FilmeService()

    def cadastrar_filme(self, filme):

        self.service.cadastrar(filme)