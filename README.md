# 🩰 Escola de Ballet - Sistema de Gestão

Sistema desenvolvido como trabalho final da disciplina de Banco de Dados, com foco na construção de um sistema completo utilizando **Python, Flask, HTML/CSS (Bootstrap)** e **SQLite** com **SQL puro**.

## 📌 Objetivo

Gerenciar informações de uma escola de ballet, incluindo alunos, professores, turmas, apresentações e avaliações. O sistema permite:

- Cadastro, listagem e remoção de alunos, professores e turmas
- Atribuição de participações em turmas (relacionamento ternário)
- Registro de avaliações
- Acompanhamento de apresentações e eventos
- Consulta de dados com filtros e agregações

## 🛠️ Tecnologias utilizadas

- Python 3
- Flask
- SQLite
- SQL puro
- HTML5 / CSS3
- Bootstrap 5

## 🧩 Estrutura do Projeto

ballet_app/
├── backend/
│ ├── app.py
│ ├── db/
│ │ ├── schema.sql
│ ├── models/
│ │ ├── aluno.py
│ │ ├── professor.py
│ │ ├── turma.py
│ │ ├── avaliacao.py
│ │ ├── apresentacao.py
│ │ ├── participacao.py
│ └── templates/
│ ├── alunos.html
│ ├── professores.html
│ ├── turmas.html
│ ├── participacoes.html
│ └── ...
├── static/
│ └── style.css
└── README.md

## 🗃️ Banco de Dados

- Todas as **tabelas foram criadas com SQL nativo**
- Relacionamentos implementados:
  - 1:1 → Avaliação e Aluno
  - 1:N → Turma para Apresentação
  - N:N ternário → Participação (Aluno, Professor, Turma)
- Valor padrão aplicado: `nivel DEFAULT 'iniciante'` em `Turma`
- **Trigger implementado**: log de atualização em `Professor`
- Arquivo `schema.sql` inclui:
  - Criação de tabelas
  - Inserts fictícios
  - Comandos `SELECT`, `UPDATE`, `DELETE`
  - Consultas avançadas: `JOIN`, `GROUP BY`, `ANY`, `LIKE`

## 🖥️ Executando o Projeto

1. Clone o repositório:
   ```bash
   git clone https://github.com/CaririLeticia/Escola_Ballet.git
   cd Escola_Ballet/backend
   python app.py
   http://localhost:5000


Projeto desenvolvido por:
Letícia, Marília, Marina e Olga
Universidade Estadual do Ceará (UECE)
Curso: Ciência da Computação – Banco de Dados
