````markdown
# 🎬 Sistema de Rede de Cinemas

## 📖 Sobre o Projeto

Este projeto foi desenvolvido para a disciplina de Engenharia de Software com o objetivo de criar um sistema de gerenciamento para uma rede de cinemas.

O sistema permite o cadastro de cinemas, filmes e sessões, além do controle de público e consultas de informações relacionadas aos filmes em cartaz.

O projeto foi desenvolvido utilizando:

- Python
- SQLite
- Arquitetura MVC
- Service Layer
- Repository Pattern
- VS Code

---

# 🎯 Objetivo do Sistema

O sistema foi criado para centralizar e organizar informações relacionadas às unidades da rede de cinemas, facilitando:

- Controle de filmes em exibição
- Organização das sessões
- Registro do público
- Consultas de relatórios
- Gerenciamento dos cinemas

---

# 🚀 Tecnologias Utilizadas

| Tecnologia | Finalidade |
|---|---|
| Python | Linguagem principal |
| SQLite | Banco de dados |
| VS Code | Ambiente de desenvolvimento |
| MVC | Organização da aplicação |
| Repository Pattern | Persistência de dados |
| Service Layer | Regras de negócio |

---

# 📂 Estrutura do Projeto

```text
ProjetoCinema
│
├── src
│   │
│   ├── controller
│   │   └── filme_controller.py
│   │
│   ├── database
│   │   ├── conexao.py
│   │   └── criar_tabelas.py
│   │
│   ├── model
│   │   └── filme.py
│   │
│   ├── repository
│   │   └── filme_repository.py
│   │
│   ├── service
│   │   └── filme_service.py
│   │
│   └── view
│
├── cinema.db
│
├── main.py
│
└── README.md
```

---

# 📋 Levantamento de Requisitos

## Requisitos Funcionais (RF)

| Código | Descrição |
|---|---|
| RF01 | Cadastrar cinemas da rede |
| RF02 | Cadastrar filmes |
| RF03 | Cadastrar sessões dos filmes |
| RF04 | Registrar público de cada sessão |
| RF05 | Consultar filmes em cartaz por cinema |
| RF06 | Consultar total de público por sessão |
| RF07 | Consultar total de público por filme |
| RF08 | Consultar total de público por cinema |
| RF09 | Consultar informações de elenco, diretor e gênero dos filmes |
| RF10 | Permitir que espectadores consultem sessões disponíveis |

---

# 📌 Regras de Negócio

| Código | Descrição |
|---|---|
| RN01 | Cada cinema pertence a uma única cidade e estado |
| RN02 | Um cinema pode possuir várias sessões simultaneamente |
| RN03 | Cada sessão exibe apenas um filme |
| RN04 | O horário das sessões deve respeitar a duração do filme e o intervalo mínimo entre exibições |
| RN05 | O público registrado em uma sessão não pode ultrapassar a capacidade do cinema |
| RN06 | Filmes devem possuir pelo menos um gênero cadastrado |
| RN07 | Apenas funcionários ou administradores podem cadastrar filmes e sessões |

---

# 👥 Atores do Sistema

## 🎟️ Espectador

O espectador poderá:

- Consultar filmes em cartaz
- Consultar sessões disponíveis
- Consultar informações dos filmes

---

## 🧑‍💼 Funcionário/Administrador

O administrador poderá:

- Cadastrar cinemas
- Cadastrar filmes
- Cadastrar sessões
- Registrar público
- Consultar relatórios de público

---

# 🏗️ Diagrama de Classes do Domínio

## Classe Cinema

### Atributos

- idCinema
- nome
- endereco
- cidade
- estado
- capacidade

---

## Classe Filme

### Atributos

- idFilme
- titulo
- duracao
- genero
- diretor
- elenco

---

## Classe Sessao

### Atributos

- idSessao
- horario
- publico

---

## Relacionamentos

```text
Cinema 1 -------- * Sessao

Filme 1 -------- * Sessao
```

---

# 🔄 Arquitetura do Sistema

O sistema foi desenvolvido utilizando arquitetura em camadas.

```text
View
 ↓
Controller
 ↓
Service
 ↓
Repository
 ↓
SQLite
```

---

# 🗄️ Banco de Dados SQLite

## Tabela Filme

```sql
CREATE TABLE filme (

    id INTEGER PRIMARY KEY AUTOINCREMENT,

    titulo TEXT,

    duracao INTEGER,

    genero TEXT,

    diretor TEXT

);
```

---

# 💻 Implementação do Sistema

## Classe Filme

```python
class Filme:

    def __init__(self, titulo, duracao, genero, diretor):

        self.titulo = titulo
        self.duracao = duracao
        self.genero = genero
        self.diretor = diretor
```

---

## Repository

```python
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
```

---

## Service

```python
from src.repository.filme_repository import FilmeRepository

class FilmeService:

    def __init__(self):

        self.repository = FilmeRepository()

    def cadastrar(self, filme):

        self.repository.salvar(filme)
```

---

## Controller

```python
from src.service.filme_service import FilmeService

class FilmeController:

    def __init__(self):

        self.service = FilmeService()

    def cadastrar_filme(self, filme):

        self.service.cadastrar(filme)
```

---

## Main

```python
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
```

---

# ▶️ Como Executar o Projeto

## 1. Instalar Python

Baixe:

https://www.python.org/downloads/

---

## 2. Clonar o Repositório

```bash
git clone URL_DO_REPOSITORIO
```

---

## 3. Abrir o Projeto

```bash
cd ProjetoCinema
```

---

## 4. Criar Banco de Dados

```bash
python src/database/criar_tabelas.py
```

---

## 5. Executar o Sistema

```bash
python main.py
```

---

# ✅ Resultado Esperado

Ao executar o projeto, o sistema deverá:

- Criar o banco SQLite
- Criar a tabela filme
- Inserir um filme no banco
- Exibir a mensagem:

```text
Filme salvo com sucesso!
```

---

# 📚 Conceitos Aplicados

- Engenharia de Software
- UML
- MVC
- Repository Pattern
- Service Layer
- Persistência de Dados
- SQLite
- Programação Orientada a Objetos

---

# 👨‍💻 Autor

Projeto acadêmico desenvolvido para fins educacionais na disciplina de Engenharia de Software.
````

