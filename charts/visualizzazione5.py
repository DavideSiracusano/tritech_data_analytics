# Task 5 — Trend mensile delle vendite
# Crea un lineplot dell'andamento mensile delle vendite usando resample('M'). Salva come charts/05_trend_mensile.png.

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# carica i dati assicurandosi che la colonna data sia riconosciuta correttamente
df = pd.read_csv("C:\\Users\\david\\OneDrive\\Desktop\\esercizi python\\charts\\superstore_enriched.csv", parse_dates=["Order Date"], encoding="latin-1")

# prepara il DataFrame per l'analisi temporale
# Il resample richiede che la data sia l'indice della tabella
df.set_index("Order Date", inplace=True)

# esegue il raggruppamento mensile
# 'ME' sta per Month End (fine mese). si sommano le vendite (.sum()) 
# e si usa .reset_index() per far tornare la data una colonna normale
monthly_sales = df["Sales"].resample("ME").sum().reset_index()

# --- IL PASSAGGIO CHIAVE PER VEDERE TUTTI I MESI ---
# si trasforma l'oggetto Data in una stringa di testo semplice (es: "2023-01")
# Matplotlib, vedendo del testo e non una linea temporale, 
# sarà costretto a mostrare un'etichetta per ogni singola riga.
monthly_sales["Order Date"] = monthly_sales["Order Date"].dt.strftime('%Y-%m')

# Configurazione del grafico
plt.figure(figsize=(15, 6)) # aumentando a 15 pollici la larghezza per far stare tutti i mesi

# si crea il grafico a linee
# x="Order Date": ora contiene stringhe (es. "2023-01", "2023-02", ...)
# marker="o": aggiunge il pallino su ogni mese per chiarezza visiva
sns.lineplot(x="Order Date", y="Sales", data=monthly_sales, marker="o", color="royalblue")

# Abbellimento e Leggibilità
plt.title("Andamento Mensile delle Vendite (Dettaglio Totale)", fontsize=14)
plt.xlabel("Mese (Anno-Mese)")
plt.ylabel("Vendite Totali ($)")

# Ruota le etichette di 90 gradi per evitare che si scontrino tra loro
plt.xticks(rotation=90, fontsize=9)

# aggiunge una griglia leggera per seguire meglio i punti
plt.grid(True, axis='y', linestyle='--', alpha=0.5)

# Ottimizza lo spazio per non tagliare le scritte in basso
plt.tight_layout()

# 6. Salvataggio e chiusura
plt.savefig("05_trend_mensile.png")
plt.show()