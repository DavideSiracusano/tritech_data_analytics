# Task 1 — Caricamento e ispezione

# Carica il CSV con pd.read_csv, usando parse_dates per le colonne data e gestendo correttamente l'encoding
# Esegui un'analisi esplorativa completa: shape, dtypes, null per colonna, duplicati
# Scrivi un commento nel codice che descrive in 3 righe "lo stato di salute" del dataset

import pandas as pd
# Caricamento del dataset con gestione delle date e dell'encoding
df = pd.read_csv("C:\\Users\\david\\OneDrive\\Desktop\\esercizi python\\lez2\\Superstore.csv", parse_dates=["Order Date", "Ship Date"], encoding="latin-1")
# Analisi esplorativa
print("Shape del dataset:", df.shape)  # Dimensioni del dataset
print("tipi di dati delle colonne:", df.dtypes)  # Tipi di dati delle colonne
print("Null values per colonna:", df.isnull().sum())  # Conta i valori null
print("Duplicati:", df.duplicated().sum())  # Conta i duplicati

# Stato di salute del dataset:
# Il dataset contiene 9994 righe e 21 colonne, con una varietà di tipi di dati tra cui numerici, stringhe e date, non presenta valori nulli
# e non ci sono duplicati, il che indica che i dati sono completi e unici, pronto per l'analisi.
