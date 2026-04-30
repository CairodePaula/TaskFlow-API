# 🚀 TaskFlow API

API RESTful para gerenciamento de tarefas (To-Do List), construída com foco em performance, organização e boas práticas de desenvolvimento backend.

Desenvolvida com FastAPI, utilizando SQLAlchemy para ORM, PostgreSQL como banco de dados e Alembic para versionamento e migrações.

---

## 🧠 Visão Geral

O TaskFlow API permite criar, listar, atualizar e deletar tarefas de forma eficiente, seguindo o padrão CRUD.  
O projeto foi estruturado para ser escalável, com separação clara de responsabilidades entre camadas.

---

## 🛠️ Tecnologias Utilizadas

- FastAPI → Framework web moderno e rápido
- SQLAlchemy → ORM para manipulação do banco
- Alembic → Migrações e versionamento do banco
- PostgreSQL → Banco de dados relacional
- Docker & Docker Compose → Containerização
- Pydantic → Validação de dados

---

## 📋 Pré-requisitos

- Python 3.10+
- Docker
- Docker Compose
- Git

---

## ⚙️ Instalação e Configuração

### 1. Clone o repositório
git clone https://github.com/seu-usuario/taskflow-api.git
cd taskflow-api

### 2. Crie e ative o ambiente virtual
python -m venv venv

# Linux / Mac
source venv/bin/activate

# Windows
venv\Scripts\activate

### 3. Instale as dependências
pip install -r requirements.txt

### 4. Suba o banco de dados com Docker
docker-compose up -d

### 5. Execute as migrações
alembic revision --autogenerate -m "create tasks table"
alembic upgrade head

### 6. Inicie a aplicação
uvicorn main:app --reload

---

## 🚀 Uso da API

Acesse a documentação interativa:

http://127.0.0.1:8000/docs

---

## 🔌 Endpoints Principais

POST   /tasks       → Criar tarefa  
GET    /tasks       → Listar tarefas  
GET    /tasks/{id}  → Buscar por ID  
PUT    /tasks/{id}  → Atualizar  
DELETE /tasks/{id}  → Deletar  

---

## 📁 Estrutura do Projeto

taskflow-api/
│
├── main.py
├── models.py
├── schemas.py
├── database.py
│
├── alembic/
├── .env
├── requirements.txt
└── docker-compose.yml

---

## 🔒 Variáveis de Ambiente

Crie um arquivo .env:

DATABASE_URL=postgresql://user:password@localhost:5433/taskflow

---

## 📌 Melhorias Futuras

- Autenticação JWT
- Paginação
- Filtros avançados
- Testes automatizados
- Deploy em cloud

---

## 👨‍💻 Autor

Desenvolvido por Cairo
