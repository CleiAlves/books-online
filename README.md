# Books Online

Books Online é uma aplicação web desenvolvida com Django para gerenciar livros e autores. O sistema permite cadastrar, editar, visualizar e excluir livros e autores, além de realizar buscas e filtros.

## Funcionalidades

### Gerenciamento de Livros
- Cadastro de livros com título, autor, ano de publicação, gênero, capa e sinopse.
- Edição de informações dos livros.
- Exclusão de livros.
- Visualização detalhada de cada livro.

### Gerenciamento de Autores
- Cadastro de autores com nome, sobrenome e foto.
- Edição de informações dos autores.
- Exclusão de autores.

### Busca e Filtros
- Busca de livros por título.
- Filtro de livros por autor.

## Tecnologias Utilizadas

- **Backend**: Django 5.1.6, Python 3.10+, PostgreSQL.
- **Frontend**: Bootstrap 5, JavaScript.
- **Outras Dependências**: Pillow, python-decouple.

## Como Executar o Projeto

1. Clone o repositório e navegue para o diretório do projeto:
   ```bash
   git clone https://github.com/CleiAlves/books-online
   cd books-online
   ```

2. Crie e ative um ambiente virtual:
    ```bash
    python -m venv venv
    source venv/bin/activate  # Linux/Mac
    venv\Scripts\activate     # Windows
    ```

3. Instale as dependências:
    ```bash
    pip install -r requirements.txt
    ```

4. Crie um arquivo chamado **.env** na raiz do projeto e configure as variáveis de ambiente:
    ```python
    DB_NAME=seu_banco
    DB_USER=seu_usuario
    DB_PASSWORD=sua_senha
    DB_HOST=localhost
    DB_PORT=5432 # Porta padrão do PostgreSQL
    ```

5. Realize as migrações do banco de dados:
    ```bash
    python manage.py migrate
    ```

6. Inicie o servidor de desenvolvimento:
    ```bash
    python manage.py runserver
    ```

7. Acesse a aplicação em [http://localhost:8000](http://localhost:8000).
