# Task 4 — Tabella pivot
# Crea una pivot table con:

# Righe: Region
# Colonne: Segment
# Valori: somma di Sales
# Valori NaN sostituiti con 0
# Aggiungi una colonna Totale che somma le tre colonne Segment

import pandas as pd
# Caricamento del dataset con gestione delle date e dell'encoding
df = pd.read_csv("Superstore.csv", parse_dates=["Order Date", "Ship Date"], encoding="latin-1")

# Creazione della pivot table con righe Region, colonne Segment (presi dal dataset) e valori somma di Sales, sostituendo i NaN con 0
pivot_table = df.pivot_table(values="Sales", index= "Sales", columns="Segment", aggfunc="sum", fill_value=0)
# Aggiunta della colonna Totale
pivot_table["Totale"] = pivot_table.sum(axis=1)
print(pivot_table)

# Task 4 — Tabella pivot
# Crea una pivot table con:

# Righe: Region
# Colonne: Segment
# Valori: somma di Sales
# Valori NaN sostituiti con 0
# Aggiungi una colonna Totale che somma le tre colonne Segment

import pandas as pd
# Caricamento del dataset con gestione delle date e dell'encoding
df = pd.read_csv("Superstore.csv", parse_dates=["Order Date", "Ship Date"], encoding="latin-1")

# Creazione della pivot table con righe Region, colonne Segment (presi dal dataset) e valori somma di Sales, sostituendo i NaN con 0
pivot_table = df.pivot_table(values="Sales", index= "Sales", columns="Segment", aggfunc="sum", fill_value=0)
# Aggiunta della colonna Totale
pivot_table["Totale"] = pivot_table.sum(axis=1)
print(pivot_table)