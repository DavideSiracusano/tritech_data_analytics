# Task 3 — Heatmap di correlazione
# Calcola e visualizza la matrice di correlazione tra: Sales, Profit, Discount, Quantity, Shipping_Days, Profit_Margin_Pct. Salva come charts/03_heatmap_correlazione.png.
# Domanda: "Quale coppia di variabili ha la correlazione negativa più forte? Ha senso economicamente?"

import pandas as pd      # Carica la libreria per gestire il dataset (DataFrame)
import matplotlib.pyplot as plt  # Carica il modulo per gestire la visualizzazione finale e il salvataggio
import seaborn as sns    # Carica la libreria per creare grafici statistici complessi in modo semplice

# Caricamento del file CSV arricchito con le colonne calcolate (Shipping_Days, ecc.)
# L'encoding 'latin-1' serve a gestire correttamente eventuali caratteri speciali nel testo
df = pd.read_csv("C:\\Users\\david\\OneDrive\\Desktop\\esercizi python\\charts\\superstore_enriched.csv",
parse_dates=["Order Date", "Ship Date"], encoding="latin-1")

# Seleziona solo le colonne di interesse per la correlazione
correlation_data = df[["Sales", "Profit", "Discount", "Quantity", "Shipping_Days", "Profit_Margin_Pct"]]
# Calcola la matrice di correlazione (valori tra -1 e 1 che indicano forza e direzione della relazione)
correlation_matrix = correlation_data.corr()
# Inizializza la dimensione della tela del grafico (10 pollici di larghezza, 8 di altezza)
plt.figure(figsize=(10, 8))
# Crea la heatmap usando Seaborn
# annot=True: mostra i valori di correlazione all'interno delle celle
# cmap="coolwarm": usa una scala di colori che va dal blu (negativo) al rosso (positivo)
# vmin=-1, vmax=1: fissa i limiti della scala dei colori per una migliore interpretazione
sns.heatmap(correlation_matrix, annot=True, cmap="coolwarm", vmin=-1, vmax=1)
# Aggiunge il titolo al grafico
plt.title("Matrice di Correlazione tra Variabili")
# Salva l'immagine prodotta nel file specificato
plt.savefig("03_heatmap_correlazione.png")
# Mostra il grafico a schermo
plt.show()

# Domanda: "Quale coppia di variabili ha la correlazione negativa più forte? Ha senso economicamente?"
# La coppia di variabili con la correlazione negativa più forte è "Discount" e "Profit_Margin_Pct" con un valore di circa -0.85.
# Ha senso economicamente perché un aumento dello sconto (Discount) riduce il margine di profitto percentuale (Profit_Margin_Pct), 
# poiché offrire sconti più elevati diminuisce la quantità di profitto guadagnato su ogni vendita. 