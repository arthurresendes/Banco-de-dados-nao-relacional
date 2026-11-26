# 📚 Banco de Dados Não Relacional

Repositório de estudos e projetos práticos sobre bancos de dados NoSQL, com foco em **MongoDB** e **Python**. O principal projeto é o **StreamFlux**, uma aplicação web para consultar e gerenciar um catálogo de filmes e séries.

## 🎬 StreamFlux

O StreamFlux reúne uma API REST desenvolvida com **FastAPI** e uma interface feita com **React + Vite**. A aplicação consulta e modifica dados em uma coleção do **MongoDB Atlas**.

### Acesse

- **Aplicação web:** [streamingmongo.vercel.app](https://streamingmongo.vercel.app)

### Funcionalidades

- Buscar filmes e séries pelo título.
- Encontrar produções em que um ator ou atriz participou.
- Consultar títulos lançados antes do ano 2000, com uma opção de paginação.
- Listar categorias e consultar até cinco títulos de uma categoria.
- Cadastrar títulos no catálogo.
- Adicionar um ator ao elenco de um título.
- Remover títulos pelo nome.

### Tecnologias

| Camada | Tecnologias |
| --- | --- |
| Front-end | React, React Router, Vite, JavaScript e CSS |
| Back-end | Python, FastAPI, Uvicorn, Pydantic e SlowAPI |
| Banco de dados | MongoDB Atlas e PyMongo |
| Hospedagem | Vercel (front-end) e Render (API) |
| Automação | GitHub Actions |

### Estrutura do projeto

```text
Dados/netflix/
├── netflix_titles.csv              # Dataset de filmes e séries
├── Script/                         # API FastAPI
│   ├── main.py                     # Inicialização da API, CORS e rate limiting
│   ├── rotas.py                    # Endpoints REST
│   ├── query.py                    # Consultas e operações no MongoDB
│   ├── Schemas.py                  # Modelos de entrada com Pydantic
│   ├── limitador.py                # Configuração do limite de requisições
│   ├── requirements.txt            # Dependências Python
│   └── Dockerfile
└── netflix-front/                  # Aplicação React + Vite
    ├── src/
    │   ├── api/                    # Chamadas para a API
    │   ├── components/             # Componentes reutilizáveis
    │   ├── context/                # Contextos da aplicação
    │   └── pages/                  # Páginas da interface
    ├── package.json
    ├── vite.config.js
    ├── vercel.json
    └── Dockerfile
```

### Endpoints da API

As rotas do StreamFlux usam o prefixo `/api/v1`.

| Método | Rota | Descrição |
| --- | --- | --- |
| `GET` | `/` | Verifica se a API está disponível |
| `GET` | `/see_especific/{title}` | Busca um título pelo nome |
| `GET` | `/netflix_lt_2000` | Lista títulos lançados até 1999 |
| `GET` | `/netflix_lt_2000_page?pagina=1` | Lista títulos anteriores a 2000 com paginação |
| `GET` | `/especifics_types/{type}` | Consulta até cinco títulos de uma categoria |
| `GET` | `/see_actor_especific/{name}` | Busca produções pelo nome de um ator ou atriz |
| `GET` | `/see_all_types` | Lista as categorias disponíveis |
| `POST` | `/adicionando_novo` | Cadastra um filme ou uma série |
| `PATCH` | `/atualizando` | Adiciona um ator ao elenco de um título |
| `DELETE` | `/delete_per_name/{name}` | Remove um título pelo nome |

Acesse `/docs` para testar os endpoints e conferir os modelos de requisição e as respostas.

## 🚀 Executar o StreamFlux localmente

### Pré-requisitos

- Python 3.11 ou compatível com as dependências do projeto.
- Node.js e npm. O workflow de CI utiliza Node.js 24.
- Uma instância MongoDB acessível, com a base e a coleção utilizadas pela API.

### Configurar o MongoDB

A API usa a variável de ambiente `MONGO_ATLAS_URI` e acessa a base `Netflix`, coleção `informations`.

Configure a variável no ambiente ou em um arquivo `.env` dentro de `Dados/netflix/Script/`:

```dotenv
MONGO_ATLAS_URI=sua_uri_do_mongodb
```

Não compartilhe nem versione credenciais ou URIs que contenham senhas.

### Iniciar o back-end

```bash
cd Dados/netflix/Script
python -m venv .venv
```

Ative o ambiente virtual:

```bash
# Linux ou macOS
source .venv/bin/activate
```

```powershell
# Windows PowerShell
.venv\Scripts\Activate.ps1
```

Instale as dependências e inicie a API:

```bash
pip install -r requirements.txt
python -m uvicorn main:app --reload
```

A API ficará disponível em `http://localhost:8000`. A documentação interativa ficará em `http://localhost:8000/docs`.

### Iniciar o front-end

Em outro terminal:

```bash
cd Dados/netflix/netflix-front
npm ci
npm run dev
```

Por padrão, o front-end usa `http://localhost:8000` para acessar a API. Para usar outra URL, defina `VITE_API_URL` no ambiente ou em `Dados/netflix/netflix-front/.env`:

```dotenv
VITE_API_URL=http://localhost:8000
```

## ⚙️ CI/CD

O workflow [`.github/workflows/ci-cd.yml`](.github/workflows/ci-cd.yml) valida o front-end e o back-end quando há alterações em `Dados/netflix/**` ou no próprio workflow, em `push` e `pull_request` direcionados à branch `main`.

As verificações incluem:

- **Front-end:** instalação com `npm ci`, lint com Oxlint e build com Vite.
- **Back-end:** instalação das dependências Python e validação da sintaxe.
- **Deploy:** em um `push` para `main`, após as verificações, o workflow aciona os deploy hooks da Vercel e do Render.

Configure os seguintes GitHub Secrets para habilitar o deploy automatizado:

- `VERCEL_DEPLOY_HOOK_URL`
- `RENDER_DEPLOY_HOOK_URL`

## 🧭 Outros conteúdos do repositório

### `Aprendizado/` — exemplos de MongoDB

Exercícios em Python/PyMongo organizados por assunto:

- Operações CRUD, criação e inserção de documentos.
- Atualização e exclusão de documentos.
- Filtragem com operadores lógicos e de comparação.
- Contagem, limite e ordenação de resultados.
- Relacionamentos um-para-um, um-para-muitos e muitos-para-muitos.
- Schemas e validação de documentos.

### `Dados/` — datasets e consultas

- **`Dados/netflix/`** contém o dataset CSV e o projeto StreamFlux.
- **`Dados/pokemon/`** contém datasets de Pokémon e combates, além de exemplos de consultas com filtros, atualizações, índices, agregações e relacionamentos.
- **`Dados/data/`** reúne arquivos JSON e CSV utilizados nos estudos, incluindo dados de Netflix e Pokémon.

### `Projeto_Estoque/` — exercício de estoque

O arquivo `main.py` demonstra operações em uma coleção de produtos: inserção, consulta, atualização, exclusão, contagem, ordenação, limite e filtros. A conexão usa a variável de ambiente `MONGO_URI`.

### `Projeto_Financas/` — exercício de finanças

Aplicação de terminal para consultar e manter registros de pessoas, salários e investimentos em MongoDB:

- `main.py` contém o menu da aplicação.
- `querys.py` concentra as operações de banco de dados, filtros por faixa salarial e consultas de investimentos.

A conexão também usa a variável de ambiente `MONGO_URI`.
