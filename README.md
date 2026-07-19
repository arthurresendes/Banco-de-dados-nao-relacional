# 📚 Banco de Dados Não Relacional

Uma coleção completa de estudos, aprendizados e projetos práticos sobre bancos de dados não relacionais, com implementações em Python utilizando MongoDB.

---

## 📑 Estrutura do Repositório

### 📖 **Aprendizado**
Pasta dedicada ao estudo e aprendizado de conceitos fundamentais de bancos de dados não relacionais.

#### Subdirectórios:

- **Atualizando** - Exemplos e exercícios sobre operações de atualização (UPDATE)
- **Contagem** - Técnicas de contagem e agregação de dados
- **Criacao_Insercao_Banco** - Criação de bancos de dados e inserção de registros
- **Deletar** - Operações de exclusão (DELETE) de documentos
- **Filtragem** - Métodos de filtragem e consultas avançadas
- **Limite** - Uso de limites em consultas (LIMIT)
- **Ordenação** - Ordenação de resultados (SORT)
- **Indexes** - Criação de índices para otimizar na pesquisa
- **Aggregation** - Resultado de múltiplas tabelas com campos em comum

---

### 🎬 **StreamFlux**
API REST completa integrada a um front-end React, simulando um catálogo de streaming com dados reais da Netflix, utilizando FastAPI + MongoDB Atlas.

**Deploy:**
- 🔗 Front-end: [streamingmongo.vercel.app](https://streamingmongo.vercel.app)
- 🔗 Back-end: [banco-de-dados-nao-relacional.onrender.com/docs](https://banco-de-dados-nao-relacional.onrender.com/docs)

**Funcionalidades do Front-end:**
- 🎯 **Top 5** — Seleciona uma categoria via selectbox e retorna os 5 títulos ordenados
- 🕰️ **Século Passado** — Lista filmes e séries lançados antes do ano 2000
- 🔍 **Buscar por Título** — Busca exata de um filme ou série pelo nome
- 🎭 **Buscar por Ator** — Exibe todas as produções em que um ator esteve presente
- ✏️ **Atualizar Cast** — Adiciona um ator ao elenco de um título existente
- ❌ **Deletar por nome** = Deletar filme/série
- ➕ **Adicionar Filme/Série** — Cadastra um novo título no catálogo

**Endpoints da API:**
| Método | Rota | Descrição |
|--------|------|-----------|
| GET | `/api/v1/see_especific/{title}` | Busca por título |
| GET | `/api/v1/netflix_lt_2000` | Títulos antes de 2000 |
| GET | `/api/v1/especifics_types/{type}` | Top 5 por categoria |
| GET | `/api/v1/see_actor_especific/{name}` | Busca por ator |
| GET | `/api/v1/see_all_types` | Lista todas as categorias |
| POST | `/api/v1/adicionando_novo` | Adiciona novo título |
| PATCH | `/api/v1/atualizando` | Atualiza elenco |
| DELETE | `/api/v1/delete_per_name/{name}` | Remove por nome |

**Stack:**
- Back-end: Python, FastAPI, Uvicorn
- Banco: MongoDB Atlas
- Front-end: React + Vite
- Deploy: Render (back-end) + Vercel (front-end)

---

### 🏪 **Projeto_Estoque**

Sistema de gerenciamento de estoque implementado com bancos de dados não relacionais.

**Arquivos:**
- `main.py` - Aplicação principal do sistema de estoque com funcionalidades CRUD

**Funcionalidades:**
- Criar, ler, atualizar e deletar produtos
- Controlar quantidade em estoque
- Consultas avançadas sobre inventário

---

### 💰 **Projeto_Financas**

Sistema de gerenciamento financeiro com operações complexas em bancos de dados não relacionais.

**Arquivos:**
- `main.py` - Aplicação principal do sistema financeiro
- `querys.py` - Módulo com queries e operações de banco de dados

**Funcionalidades:**
- Gerenciamento de transações financeiras
- Relatórios e agregações
- Consultas otimizadas para análise financeira

---


## 🚀 Como Usar

### Pré-requisitos
- Python 3.7+
- MongoDB instalado e configurado
- Bibliotecas Python necessárias (pymongo, etc)
