<div align="center">
  <h1>📊 Sistema de Gerenciamento e Análise de Vendas</h1>
  <p>
    <strong>Uma solução Full-Stack completa combinando operações CRUD e um pipeline ETL usando ferramentas modernas em Python.</strong>
  </p>
  <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white" />
  <img src="https://img.shields.io/badge/Pandas-150458?style=for-the-badge&logo=pandas&logoColor=white" />
  <img src="https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white" />
  <img src="https://img.shields.io/badge/SQLite-003B57?style=for-the-badge&logo=sqlite&logoColor=white" />
</div>

<br>

## 📖 Visão Geral

Este projeto foi construído do zero como um exercício robusto de **Engenharia de Dados** e **Engenharia de Software**. Ele abstrai a complexidade dos dados brutos de vendas em uma interface web bonita e interativa, mantendo um fluxo de backend rigoroso e pronto para produção.

### ✨ Principais Funcionalidades
* **Pipeline ETL (Drag & Drop):** Você não precisa lidar com o terminal. Arraste um arquivo CSV bruto para a guia *Carga de Dados* e o mecanismo do Pandas irá Extrair, Transformar (normalização de colunas) e Carregar em massa (`to_sql`) milhares de linhas instantaneamente.
* **Operações CRUD Completas:** Crie, Leia, Atualize e Exclua registros de vendas individuais diretamente pela interface intuitiva do Streamlit por meio de um banco de dados SQLite local na memória.
* **Painel Gerencial (Dashboard):** Uma aba de análise dinâmica que agrega vendas em tempo real, calculando a Receita Bruta e ranqueando os Representantes de Vendas por meio de gráficos de barras interativos.
* **Código Pronto para Produção:** O backend usa tipagem forte (Type Hinting), Gerenciadores de Contexto (Context Managers) para o ciclo de vida do banco de dados (`with sqlite3`), formatação PEP 8 e blocos `try-except` com logs (Python `logging`).

---

## 🛠️ Arquitetura

* **Frontend:** `app.py` (Aplicação Streamlit MVC modularizada)
* **Backend (Acesso a Dados):** `crud.py` (Operações SQLite, Consultas parametrizadas para prevenção contra SQL Injection)
* **Backend (Engenharia de Dados):** `carga.py` & `setup_db.py` (Carga via Pandas Pandas E schemas de DB)
* **Banco de Dados:** SQLite (`vendas.db`)

---

## 🚀 Como Rodar Localmente

### 1. Clonar o repositório
```bash
git clone https://github.com/SeuUsuario/sales-analytics-dashboard.git
cd sales-analytics-dashboard
```

### 2. Criar e Ativar um Ambiente Virtual
**Windows:**
```bash
python -m venv .venv
source .venv/Scripts/activate
```

**Linux/Mac:**
```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Instalar as dependências específicas
```bash
pip install -r requirements.txt
```

### 4. Inicializar o Banco de Dados
Antes de rodar o aplicativo, precisamos criar os schemas da tabela dentro da pasta `data/`.
```bash
python src/database/setup_db.py
```

### 5. Iniciar a Aplicação!
```bash
streamlit run src/app.py
```

---

## 📉 Dados de Exemplo (Sample)

Se você quiser testar o pipeline ETL, um dataset sujo de exemplo está incluído em `data/vendas_historico.csv`. Arraste e solte-o na aba "📥 Carga de Dados" no Streamlit App para ver o motor do `Pandas` limpando e carregando os dados.

---
*Desenvolvido durante uma Mentoria Intensiva de Engenharia de Dados.*
