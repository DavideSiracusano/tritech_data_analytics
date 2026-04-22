# Task 4 — Top 10 prodotti per vendite
# Crea un barplot orizzontale (barh) dei top 10 prodotti per vendite totali. Salva come charts/04_top10_prodotti.png.
# Attenzione al layout: i nomi dei prodotti sono lunghi, gestire la leggibilità.

import pandas as pd      # Carica la libreria per gestire il dataset (DataFrame)
import matplotlib.pyplot as plt  # Carica il modulo per gestire la visualizzazione finale e il salvataggio
import seaborn as sns    # Carica la libreria per creare grafici statistici complessi in modo semplice

# Caricamento del file CSV arricchito con le colonne calcolate (Shipping_Days, ecc.)
# L'encoding 'latin-1' serve a gestire correttamente eventuali caratteri speciali nel testo
df = pd.read_csv("C:\\Users\\david\\OneDrive\\Desktop\\esercizi python\\charts\\superstore_enriched.csv", parse_dates=["Order Date", "Ship Date"], encoding="latin-1")

# Raggruppa i dati per "Product Name" e somma le vendite, poi ordina e prendi i primi 10
top_products = df.groupby("Product Name").agg(total_sales=("Sales", "sum")).reset_index().sort_values(by="total_sales", ascending=False).head(10)

# Inizializza la dimensione della tela del grafico (12 pollici di larghezza, 8 di altezza)
plt.figure(figsize=(12, 8))
# Crea un barplot orizzontale con Seaborn
# y="Product Name": mette le vendite totali sull'asse orizzontale
# x="total_sales": mette i nomi dei prodotti sull'asse verticale
# data=top_products: indica a Seaborn di prendere i dati dal DataFrame top_products
sns.barplot(y="Product Name", x="total_sales", data=top_products, palette="viridis")
# Aggiunge il titolo al grafico
plt.title("Top 10 Prodotti per Vendite Totali")
# Etichetta l'asse X (vendite totali) e l'asse Y (nomi dei prodotti)
plt.xlabel("Vendite Totali")
plt.ylabel("Nome del Prodotto")
plt.tight_layout()  # Migliora il layout per evitare sovrapposizioni
# Salva l'immagine prodotta nel file specificato
plt.savefig("04_top10_prodotti.png")
# Mostra il grafico a schermo
plt.show()