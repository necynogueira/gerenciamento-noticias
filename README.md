
# Noticia API - Django Rest Framework

Esta API permite a criação, edição, visualização e remoção de notícias. A API foi construída usando Django e Django Rest Framework (DRF).

## Requisitos

- Python 3.x
- Django 3.x+
- Django Rest Framework 3.x+

## Instalação

1. Clone o repositório:

   ```bash
   git clone https://github.com/necynogueira/gerenciamento-noticias.git
   cd gerenciamento-noticias
   ```

2. Crie um ambiente virtual e ative-o:

   ```bash
   python -m venv venv
   source venv/bin/activate  # No Windows: venv\Scripts\activate
   ```

3. Instale as dependências:

   ```bash
   pip install -r requirements.txt
   ```

4. Aplique as migrações do banco de dados:

   ```bash
   python manage.py migrate
   ```

5. Inicie o servidor de desenvolvimento:

   ```bash
   python manage.py runserver
   ```

---

# Se preferer você pode subir o projeto com o Dev Container

Este guia explica como configurar e usar um Dev Container no Visual Studio Code (VS Code) para subir seu projeto no ambiente local.

## Pré-requisitos

Antes de começar, certifique-se de ter o seguinte instalado:

- [Visual Studio Code (VS Code)](https://code.visualstudio.com/)
- [Docker](https://www.docker.com/) (necessário para rodar containers)
- Extensão **Remote - Containers** no VS Code

## Passos para Usar o Dev Container

1. **Instale a Extensão Remote - Containers**  
   No VS Code, vá para o Marketplace de extensões e instale a extensão **Remote - Containers**.

2. **Abra o Projeto no VS Code**  
   Navegue até o diretório do seu projeto e abra-o no VS Code.

3. **Abra o Projeto no Dev Container**  
   Pressione `F1` no VS Code para abrir o painel de comandos e selecione a opção **Remote-Containers: Reopen in Container**. O VS Code abrirá o projeto dentro de um Dev Container, onde você terá um ambiente de desenvolvimento isolado e configurado conforme definido no arquivo `devcontainer.json`.

A API estará disponível em `http://127.0.0.1:8000/`.

## Endpoints

### Listar todas as notícias

- **URL:** `/noticias/`
- **Método:** `GET`
- **Descrição:** Retorna todas as notícias cadastradas.

#### Exemplo de Resposta:

```json
[
  {
    "id": 1,
    "titulo": "Título da Notícia",
    "conteudo": "Conteúdo da notícia",
    "publicado": true,
    "autor": "Autor da notícia",
    "data_criacao": "2024-09-18T15:30:00Z"
  }
]
```

---

### Obter uma notícia específica

- **URL:** `/noticias/:id/`
- **Método:** `GET`
- **Descrição:** Retorna uma notícia específica com base no ID.

#### Parâmetros:

- `id` (obrigatório): ID da notícia a ser buscada.

#### Exemplo de Resposta:

```json
{
  "id": 1,
  "titulo": "Título da Notícia",
  "conteudo": "Conteúdo da notícia",
  "publicado": true,
  "autor": "Autor da notícia",
  "data_criacao": "2024-09-18T15:30:00Z"
}
```

---

### Criar uma nova notícia

- **URL:** `/noticias/`
- **Método:** `POST`
- **Descrição:** Cria uma nova notícia.

#### Corpo da Requisição (JSON):

```json
{
  "titulo": "Novo título",
  "conteudo": "Conteúdo da notícia",
  "publicado": true,
  "autor": "Autor da notícia"
}
```

#### Exemplo de Resposta:

```json
{
  "id": 2,
  "titulo": "Novo título",
  "conteudo": "Conteúdo da notícia",
  "publicado": true,
  "autor": "Autor da notícia",
  "data_criacao": "2024-09-18T16:00:00Z"
}
```

---

### Atualizar uma notícia

- **URL:** `/noticias/:id/`
- **Método:** `PUT`
- **Descrição:** Atualiza uma notícia existente.

#### Parâmetros:

- `id` (obrigatório): ID da notícia a ser atualizada.

#### Corpo da Requisição (JSON):

```json
{
  "titulo": "Título atualizado",
  "conteudo": "Conteúdo atualizado",
  "publicado": false,
  "autor": "Novo autor"
}
```

#### Exemplo de Resposta:

```json
{
  "id": 1,
  "titulo": "Título atualizado",
  "conteudo": "Conteúdo atualizado",
  "publicado": false,
  "autor": "Novo autor",
  "data_criacao": "2024-09-18T15:30:00Z"
}
```

---

### Remover uma notícia

- **URL:** `/noticias/:id/`
- **Método:** `DELETE`
- **Descrição:** Remove uma notícia existente.

#### Parâmetros:

- `id` (obrigatório): ID da notícia a ser removida.

#### Exemplo de Resposta:

```json
{
  "message": "Notícia removida com sucesso"
}
```

---

## Variáveis de Ambiente

Você pode configurar a URL base da API, se necessário, utilizando variáveis de ambiente.

- `BASE_URL`: URL base da API (exemplo: `http://127.0.0.1:8000`)

---



## Licença

Este projeto está licenciado sob a licença MIT - consulte o arquivo [LICENSE](LICENSE) para obter mais detalhes.

