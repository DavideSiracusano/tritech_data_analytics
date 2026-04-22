
import pandas as pd

# Caricamento dati
df = pd.read_csv("sales.csv", encoding="latin-1")

# 1. Analisi esplorativa
print(f"Shape: {df.shape}")
print(f"Data types:\n{df.dtypes}")
print(f"Null values:\n{df.isnull().sum()}")

# 2. Tabella Pivot Vendite Globali per Genere/Piattaforma
# Usiamo fill_value=0 direttamente nella pivot per pulizia sostituendo i NaN con 0
pivot = pd.pivot_table(df, values="Global_Sales", index="Genre", columns="Platform", aggfunc="sum", fill_value=0)

pivot["Total_Sales"] = pivot.sum(axis=1)

# Ordinamento per il nuovo totale creato
pivot = pivot.sort_values(by="Total_Sales", ascending=False)
print("\nPrime 10 righe vendite globali per piattaforma e generi (ordinate per Totale):")
print(pivot.head(10))

# 3. Percentuale vendite Giappone per Genere sul totale globale
genere_sales = df.groupby("Genre")[["JP_Sales", "Global_Sales"]].sum().reset_index()
genere_sales["JP_Pct"] = (genere_sales["JP_Sales"] / genere_sales["Global_Sales"]) * 100
genere_sales = genere_sales.sort_values(by="JP_Pct", ascending=False).round(2)
print("\nPercentuale reale vendite Giappone sul totale per genere:")
print(genere_sales.head(10))

# 4. Media vendite per anno (Analisi temporale)
# media copie vendute per regione ogni anno con gestione dei NaN (il dataset è vecchio e potrebbe avere anni con dati mancanti)
pivot_year_sales = pd.pivot_table(df, values=["EU_Sales", "NA_Sales", "JP_Sales"], index="Year", aggfunc="mean").fillna(0)
pivot_year_sales = pivot_year_sales.sort_values(by="Year", ascending=False).round(2)
print("\nMedia vendite regionali per anno (Prime 10 righe):")
print(pivot_year_sales.head(10))

# 5. Trovare il gioco che ha venduto di più per ogni anno in base alle vendite in Nord America (NA_Sales)
# idxmax() restituisce l'indice della riga con il valore massimo
idx = df.groupby('Year')['NA_Sales'].idxmax()

# si usano quegli indici per estrarre le righe complete dal dataframe originale
record_per_anno = df.loc[idx, ['Year', 'Name', 'Genre', 'NA_Sales']]
# pulizia dei dati: se ci sono anni con più record (es. stesso NA_Sales) 
record_per_anno = record_per_anno.sort_values(by="Year", ascending=False).set_index('Year')
print("\nVeri record per anno (basati sul successo in Nord America):")
print(record_per_anno.head(10))
