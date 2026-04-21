# Task 2 — Colonne derivate

# Crea una colonna Shipping_Days: numero di giorni tra Order Date e Ship Date
# Crea una colonna Profit_Margin_Pct: (Profit / Sales) * 100, arrotondata a 2 decimali
# Crea una colonna Is_Loss: booleana, True se Profit < 0

import pandas as pd
# Caricamento del dataset con gestione delle date e dell'encoding
df = pd.read_csv("C:\\Users\\david\\OneDrive\\Desktop\\esercizi python\\lez2\\Superstore.csv", parse_dates=["Order Date", "Ship Date"], encoding="latin-1")

# Creazione della colonna Shipping_Days con dt.days per calcolare i giorni tra Ship Date e Order Date
df = df.assign(Shipping_Days =  (df["Ship Date"] - df["Order Date"]).dt.days)
print(df.head()) # Visualizza le prime righe per verificare la nuova colonna Shipping_Days

# Creazione della colonna Profit_Margin_Pct, gestendo divisioni per zero e arrotondando a 2 decimali
df = df.assign(Profit_Margin_Pct =  round((df["Profit"] / df["Sales"]),2))
print(df.head())

# Creazione della colonna Is_Loss se profit minore di zero
df = df.assign(Is_loss = df["Profit"] < 0 )
print(df.head())