# Task 6 — Scatterplot Sales vs Profit
# Crea uno scatterplot Sales vs Profit con hue=Category. Aggiungi una linea orizzontale a Profit=0. Salva come charts/06_scatter_sales_profit.png.
# Domanda: "Ci sono categorie che generano molte vendite ma scarso profitto? Quali?"

import pandas as pd      # Importa pandas per manipolare i dati (tabelle/DataFrame)
import matplotlib.pyplot as plt  # Importa il motore grafico per creare la finestra del grafico
import seaborn as sns    # Importa seaborn per rendere il grafico statisticamente avanzato e bello

# Carica il file CSV specificando il percorso assoluto sul tuo computer
# parse_dates: converte automaticamente le colonne indicate in oggetti "Data" (non semplice testo)
# encoding: necessario per leggere simboli speciali (come l'euro o lettere accentate) presenti nel file
df = pd.read_csv("C:\\Users\\david\\OneDrive\\Desktop\\esercizi python\\charts\\superstore_enriched.csv",
parse_dates=["Order Date", "Ship Date"], encoding="latin-1")

# Crea una figura (la tela del grafico) di dimensioni 10x6 pollici
plt.figure(figsize=(10, 6))
# Disegna lo scatterplot con Seaborn
# x="Sales": mette le vendite sull'asse orizzontale
# y="Profit": mette il profitto sull'asse verticale
# hue="Category": colora i punti in base alla categoria (Furniture, Office Supplies, Technology)
# data=df: indica a Seaborn di prendere i dati dal DataFrame caricato sopra
# alpha=0.7: rende i punti leggermente trasparenti per vedere meglio le sovrapposizioni
sns.scatterplot(x="Sales", y="Profit", hue="Category", data=df, palette="Set2", alpha=0.7)
# Aggiunge una linea orizzontale a Profit=0 per distinguere vendite profittevoli da quelle in perdita
plt.axhline(0, color="red", linestyle="--", label="Profitto = 0")
# Aggiunge il titolo al grafico
plt.title("Scatterplot Vendite vs Profitto per Categoria")
# Etichetta l'asse X (vendite) e l'asse Y (profitto)
plt.xlabel("Vendite ($)")
plt.ylabel("Profitto ($)")
# Mostra la legenda per identificare le categorie e la linea del profitto
plt.legend()
# Salva l'immagine prodotta nel file specificato
plt.savefig("06_scatter_sales_profit.png")
# Mostra il grafico a schermo
plt.show()

# Domanda: "Ci sono categorie che generano molte vendite ma scarso profitto? Quali?"
# Sì, la categoria "Technology" mostra molti punti con vendite elevate ma profitto vicino a zero o negativo, indicando che alcuni prodotti 
# tecnologici vendono molto ma generano scarso profitto, probabilmente a causa di sconti elevati
