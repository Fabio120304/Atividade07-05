from src.model.filme import Filme
from src.controller.filme_controller import FilmeController

filme = Filme(
    "Batman",
    120,
    "Ação",
    "Matt Reeves"
)

controller = FilmeController()

controller.cadastrar_filme(filme)