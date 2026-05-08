from src.repository.filme_repository import FilmeRepository

class FilmeService:

    def __init__(self):

        self.repository = FilmeRepository()

    def cadastrar(self, filme):

        self.repository.salvar(filme)