# 🏥 Sistema de Gestão - Clínica Médica | Python + MySQL

Sistema de terminal para gestão completa de uma clínica médica.
Projeto de portfólio com CRUD + 8 Relatórios de BI usando Window Functions e CTEs.

## 🛠️ Tecnologias Utilizadas
- **Linguagem:** Python 3.10
- **Banco de Dados:** MySQL 8.0
- **Biblioteca:** `mysql-connector-python`
- **Ferramentas:** VS Code, MySQL Workbench

## 📂 Estrutura do Projeto

CLINICA_MEDICA_PYTHON/
├── db/
│   └── script.sql              # Script para criar todas as tabelas
├── conexao.py                  # Conexão com o banco de dados
├── crud.py                     # Funções de CRUD: Pacientes, Médicos, Consultas
├── menu.py                     # Menu interativo do sistema
├── relatorios.py               # 8 Relatórios e Consultas de BI
├── main.py                     # Arquivo principal - Execução do sistema
├── requirements.txt            # Dependências do projeto
└── README.md                   # Documentação

## 🎯 O que aprendi com o projeto
- Conexão segura Python com MySQL usando `mysql-connector`
- Modelagem de Banco de Dados Relacional com Chaves Estrangeiras
- Organização de código em módulos: `conexao`, `crud`, `relatorios`
- Uso de Window Functions: `RANK()`, `DENSE_RANK()`, `LAG()`, `ROW_NUMBER()`
- Criação de CTEs para relatórios e análises complexas
- Tratamento de erros com `try/except` no banco de dados

## 📝 requirements.txt
mysql-connector-python

## 👨‍💻 Autor

Feito por **Silas Barbosa da Silva**

[![LinkedIn](https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/silas-barbosa-1885ab3a0/)
[![GitHub](https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white)](https://github.com/SilasBarbosa44)