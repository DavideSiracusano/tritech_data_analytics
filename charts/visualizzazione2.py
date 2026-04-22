import pandas as pd      # Carica la libreria per gestire il dataset (DataFrame)
import matplotlib.pyplot as plt  # Carica il modulo per gestire la visualizzazione finale e il salvataggio
import seaborn as sns    # Carica la libreria per creare grafici statistici complessi in modo semplice

# Caricamento del file CSV arricchito con le colonne calcolate (Shipping_Days, ecc.)
# L'encoding 'latin-1' serve a gestire correttamente eventuali caratteri speciali nel testo
df = pd.read_csv("C:\\Users\\david\\OneDrive\\Desktop\\esercizi python\\charts\\superstore_enriched.csv",
parse_dates=["Order Date", "Ship Date"], encoding="latin-1")

# Inizializza la dimensione della tela del grafico (10 pollici di larghezza, 6 di altezza)
plt.figure(figsize=(10, 6))

# Crea il Boxplot:
# x="Ship Mode": mette le categorie (Standard, First Class, ecc.) sull'asse orizzontale
# y="Shipping_Days": mette il numero di giorni sull'asse verticale per confrontarne la distribuzione
# data=df: indica a Seaborn di prendere i dati dal DataFrame caricato sopra
# palette="Set1": assegna automaticamente colori diversi alle categorie per distinguerle meglio
sns.boxplot(x="Ship Mode", y="Shipping_Days", data=df, palette="Set1", hue="Ship Mode", legend=False)

# Aggiunge il titolo e le etichette agli assi per rendere il grafico leggibile a terzi
plt.title("Giorni di Spedizione per Modalità di Spedizione")
plt.xlabel("Modalità di Spedizione")
plt.ylabel("Giorni di Spedizione")

# Salva l'immagine prodotta nel file specificato (se vuoi metterlo nella cartella charts, aggiungi 'charts/')
plt.savefig("02_spedizione_per_modalita.png")

# Mostra il grafico a schermo
plt.show()

# 1. Quale modalità ha la maggiore variabilità?
# RISPOSTA: La "Second Class" e la "Standard Class". Visivamente sono le scatole con più "alta" variabilità e con i baffi più lunghi.
# Questo indica che i tempi di consegna sono meno prevedibili rispetto alle altre modalità.

# 2. Ci sono outlier?
# Sì, è presente un outlier nella modalità "Same Day". Il punto isolato sopra il box indica un ordine che ha impiegato più giorni del previsto
# mentre tutti gli altri ordini di "Same Day" sono stati consegnati subito.