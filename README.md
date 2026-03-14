<div align="center">
  <h1>📊 Sales Analytics & Management System</h1>
  <p>
    <strong>A complete Full-Stack solution combining CRUD operations and an ETL pipeline using modern Python tools.</strong>
  </p>
  <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white" />
  <img src="https://img.shields.io/badge/Pandas-150458?style=for-the-badge&logo=pandas&logoColor=white" />
  <img src="https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white" />
  <img src="https://img.shields.io/badge/SQLite-003B57?style=for-the-badge&logo=sqlite&logoColor=white" />
</div>

<br>

## 📖 Overview

This project was built from the ground up as a robust exercise in **Data Engineering** and **Software Engineering**. It abstracts the complexity of raw sales data into a beautiful, interactive web interface, while maintaining a rigorous, production-ready backend flow.

### ✨ Key Features
* **ETL Pipeline (Drag & Drop):** You do not need to deal with the terminal. Drag a raw CSV into the *Carga de Dados* tab and the Pandas engine will Extract, Transform (`fillna`, column normalization) and Bulk Load (`to_sql`) thousands of lines instantly.
* **Full CRUD Operations:** Create, Read, Update, and Delete individual sales records directly through the intuitive Streamlit UI via a local SQLite memory-mapped database.
* **Managerial Dashboard:** A dynamic analytics tab that aggregates sales in real-time, calculating Gross Revenue and ranking Sales Representatives through interactive Bar Charts.
* **Production-Ready Code:** The backend uses Type Hinting, Context Managers for database lifecycle (`with sqlite3`), PEP 8 formatting, and `try-except` blocks with standard Python `logging`.

---

## 🛠️ Architecture

* **Frontend:** `app.py` (Streamlit MVC modularized application)
* **Backend (Data Access):** `crud.py` (SQLite operations, Parameterized queries for SQL Injection prevention)
* **Backend (Data Engineering):** `carga.py` & `setup_db.py` (Pandas Analytics Engine & DB schemas)
* **Database:** SQLite (`vendas.db`)

---

## 🚀 How to Run Locally

### 1. Clone the repository
```bash
git clone https://github.com/your-username/crud-etl-sales.git
cd crud-etl-sales
```

### 2. Create and Activate a Virtual Environment
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

### 3. Install the specific dependencies
```bash
pip install -r requirements.txt
```

### 4. Initialize the Database
Before running the app, we need to create the table schemas inside the `data/` folder.
```bash
python src/database/setup_db.py
```

### 5. Launch the Application!
```bash
streamlit run src/app.py
```

---

## 📉 Sample Data

If you want to test the ETL pipeline, a sample dirty dataset is included in `data/vendas_historico.csv`. Drag and drop it into the "📥 Carga de Dados" tab inside the Streamlit App to see the `Pandas` engine clean and load the data.

---
*Developed during an intensive Data Engineering Mentorship.*
