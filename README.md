# API - Gerenciamento de Notícias

Esta é uma API simples para gerenciar notícias. A API permite adicionar, editar, remover e listar notícias específicas. Cada notícia tem um identificador único, um título, um conteúdo, um autor, um status de publicação e uma data de criação.


## Endpoints Disponíveis para a API

### 1. Adicionar Notícia

- **URL:** `/adicionar-noticia/`
- **Método HTTP:** `POST`
- **Descrição:** Adiciona uma nova notícia ao banco de dados.
- **Corpo da Requisição:**
  ```json
  {
    "titulo": "Título da Notícia",
    "conteudo": "Conteúdo detalhado da notícia.",
    "publicado": true,
    "autor": "Nome do Autor"
  }
  ```
- **Exemplo de Resposta:**
  ```json
  {
    "id": "d41d8cd98f00b204e9800998ecf8427e",
    "titulo": "Título da Notícia",
    "conteudo": "Conteúdo detalhado da notícia.",
    "autor": "Nome do Autor",
    "publicado": true,
    "data_criacao": "2024-09-12 12:00:00"
  }
  ```
- **Observação:** Todos os campos são obrigatórios.

### 2. Editar Notícia

- **URL:** `/editar-noticia/`
- **Método HTTP:** `PUT`
- **Descrição:** Edita uma notícia existente no banco de dados.
- **Corpo da Requisição:**
  ```json
  {
    "id": "d41d8cd98f00b204e9800998ecf8427e",
    "titulo": "Novo Título da Notícia",
    "conteudo": "Novo conteúdo da notícia.",
    "publicado": false,
    "autor": "Novo Nome do Autor"
  }
  ```
- **Exemplo de Resposta:**
  ```json
  {
    "id": "d41d8cd98f00b204e9800998ecf8427e",
    "titulo": "Novo Título da Notícia",
    "conteudo": "Novo conteúdo da notícia.",
    "autor": "Novo Nome do Autor",
    "publicado": false,
    "data_criacao": "2024-09-12 12:00:00"
  }
  ```
- **Observação:** O `id` da notícia deve existir no banco de dados.

### 3. Remover Notícia

- **URL:** `/remover-noticia/<identificador>/`
- **Método HTTP:** `DELETE`
- **Descrição:** Remove uma notícia do banco de dados com base no seu identificador.
- **Exemplo de Requisição:**
  ```bash
  curl -X DELETE http://localhost:8000/remover-noticia/d41d8cd98f00b204e9800998ecf8427e/
  ```
- **Exemplo de Resposta:**
  ```json
  {
    "message": "Notícia removida com sucesso"
  }
  ```
- **Observação:** O `<identificador>` é o ID da notícia que deve ser removida.

### 4. Listar Notícia

- **URL:** `/listar-noticia/<identificador>/`
- **Método HTTP:** `GET`
- **Descrição:** Retorna os detalhes de uma notícia específica com base no seu identificador.
- **Exemplo de Requisição:**
  ```bash
  curl -X GET http://localhost:8000/listar-noticia/d41d8cd98f00b204e9800998ecf8427e/
  ```
- **Exemplo de Resposta:**
  ```json
  {
    "id": "d41d8cd98f00b204e9800998ecf8427e",
    "titulo": "Título da Notícia",
    "conteudo": "Conteúdo detalhado da notícia.",
    "autor": "Nome do Autor",
    "publicado": true,
    "data_criacao": "2024-09-12 12:00:00"
  }
  ```
- **Observação:** O `<identificador>` é o ID da notícia a ser listada.


### 5. Listar Notícias

- **URL:** `/listar-noticias/`
- **Método HTTP:** `GET`
- **Descrição:** Retorna os detalhes de todas as notícias.
- **Exemplo de Requisição:**
  ```bash
  curl -X GET http://localhost:8000/listar-noticias/
  ```
- **Exemplo de Resposta:**
  ```json
  [
    {
        "id": "d41d8cd98f00b204e9800998ecf8427e",
        "titulo": "Título da Notícia",
        "conteudo": "Conteúdo detalhado da notícia.",
        "autor": "Nome do Autor",
        "publicado": true,
        "data_criacao": "2024-09-12 12:00:00"
    }
  ]
  ```

## Como Executar

1. Certifique-se de ter o Django instalado no seu ambiente.
2. Clone o repositório e navegue até o diretório do projeto.
3. Execute as migrações do Django:
   ```bash
   python manage.py migrate
   ```
4. Inicie o servidor de desenvolvimento do Django:
   ```bash
   python manage.py runserver
   ```
5. Use uma ferramenta como `curl`, `Postman` ou seu navegador para interagir com a API.

## Considerações Finais

- Esta é uma API de exemplo e não deve ser usada em produção sem considerar aspectos de segurança, como autenticação, autorização e validação de entrada.
- Recomendamos adicionar validações adicionais e configurações de segurança para ambientes de produção.

# Guia para subir o projeto com o Dev Container

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

## Licença

Este projeto está licenciado sob os termos da [Licença MIT](LICENSE).