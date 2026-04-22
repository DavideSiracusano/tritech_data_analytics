# 📊 Tri Tech Academy — Data Analytics Track

> Percorso formativo intensivo in **Python · SQL · Machine Learning**  
> Formazione pratica e orientata al lavoro nel cuore dell'intelligenza artificiale applicata.

---

## 🎯 Obiettivi del Percorso

Questo repository raccoglie i materiali, gli esercizi, i progetti e le risorse del tracciato **Data Analytics** di Tri Tech Academy. Il percorso è progettato per trasformare studenti con background eterogenei in professionisti capaci di lavorare con i dati in contesti reali: dall'estrazione e pulizia, all'analisi statistica, fino alla modellazione predittiva con il Machine Learning.

---


## 🛠️ Stack Tecnologico

| Area | Tecnologie |
|------|-----------|
| **Linguaggio** | Python 3.11+ |
| **Data Wrangling** | Pandas, Matplot, Seaborn |
| **Database** | PostgreSQL, SQL standard |
| **Versionamento** | Git, GitHub |
| **Ambiente** | VS Code, Docker (opzionale) |

---

## 🚀 Setup dell'Ambiente

### 1. Clona il repository

```bash
git clone https://github.com/tritech-academy/data-analytics.git
cd data-analytics
```

### 2. Crea un virtual environment

```bash
python -m venv .venv

# Windows
.venv\Scripts\activate

# macOS / Linux
source .venv/bin/activate
```

### 3. Installa le dipendenze

```bash
pip install -r requirements.txt
```

### 4. Avvia Jupyter

```bash
jupyter lab
```

### 5. Configura il database PostgreSQL

```bash
# Assicurati che PostgreSQL sia in esecuzione sulla porta 5432
# Crea il database di esercitazione
psql -U postgres -c "CREATE DATABASE tritech_analytics;"
```

---

## 📚 Moduli del Percorso

### 🗄️ Modulo 1 — SQL e Database

Fondamenta solide in Python con focus immediato sull'ecosistema dati.

- Strutture dati native (list, dict, set, tuple)
- Programmazione orientata agli oggetti (OOP)
- **NumPy**: operazioni su array N-dimensionali
- **Pandas**: DataFrames, Series, merge, groupby, pivot
- **Visualizzazione**: grafici statistici ed esplorativi
- Gestione di file CSV, JSON, Excel

 ### 🐍 Modulo 2 — Python per i Dati

Dal SQL fondamentale alla progettazione avanzata di database analitici.

- Query fondamentali: `SELECT`, `WHERE`, `JOIN`, `GROUP BY`
- Subquery, CTE (Common Table Expressions)
- Window Functions: `RANK()`, `LAG()`, `PARTITION BY`
- **PostgreSQL**: tipi di dato, indici, schema design
- **Data Warehousing**: star schema, fact table, dimension table
- Slowly Changing Dimensions (SCD Tipo 1, 2, 3)
- Query analitiche per KPI: ticket volume, CSAT

### 🤖 Modulo 3 — Machine Learning

Apprendimento automatico applicato a problemi reali.

---


## 🎓 Struttura del Programma Tri Tech

```
Fase : Formazione intensiva in aula     →  ~3 mesi
```

Il percorso combina teoria, laboratori pratici e progetti reali in un ambiente che simula il lavoro in team su prodotti dati professionali.

## 📄 Licenza

Questo repository è a uso didattico interno di Tri Tech Academy.  
I contenuti sono riservati agli studenti iscritti al programma.
