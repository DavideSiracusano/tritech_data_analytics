# Task 5 — Merge

# Costruisci a mano un DataFrame budget_regioni con colonne Region e Budget_Annuale (inventalo tu, con valori plausibili)
# Fai un LEFT JOIN tra il DataFrame originale e budget_regioni
# Crea una colonna % Budget Usato: Sales / Budget_Annuale * 100
# Raggruppa per Region e calcola la percentuale media di budget utilizzato

import pandas as pd
# Caricamento del dataset con gestione delle date e dell'encoding
df = pd.read_csv("C:\\Users\\david\\OneDrive\\Desktop\\esercizi python\\lez2\\Superstore.csv", parse_dates=["Order Date", "Ship Date"], encoding="latin-1")

# Creazione del DataFrame budget_regioni con colonne Region e Budget_Annuale
budget_regioni = pd.DataFrame({
    "Region": ["East", "West", "Central", "South"],
    "Budget_Annuale": [500000, 600000, 550000, 450000]  # Valori inventati
})

# LEFT JOIN tra il DataFrame originale e budget_regioni
merged_df = pd.merge(df, budget_regioni, on="Region", how="left")

# crea una colonna % budget usato
merged_df = merged_df.assign(budget_usato = merged_df["Sales"] / merged_df["Budget_Annuale"] * 100)

# raggruppamento per Region
used_budget = merged_df.groupby("Region").agg(media_budget_usato = ("budget_usato", "mean"))
print(merged_df.head())

# Task 6 — Export
# Salva il DataFrame finale (con tutte le colonne derivate) in un file superstore_enriched.csv.
merged_df.to_csv("superstore_enriched.csv", index=False, encoding="latin-1")
