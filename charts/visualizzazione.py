# Task 1 — Distribuzione del Profitto
# Crea un histplot con KDE della colonna Profit. Aggiungi linee verticali per media e mediana. Salva come charts/01_distribuzione_profitto.png.
# Domanda da rispondere nel commento: "Cosa noti tra media e mediana? Cosa suggerisce sulla distribuzione?"


import pandas as pd      # Importa pandas per manipolare i dati (tabelle/DataFrame)
import matplotlib.pyplot as plt  # Importa il motore grafico per creare la finestra del grafico
import seaborn as sns    # Importa seaborn per rendere il grafico statisticamente avanzato e bello

# Carica il file CSV specificando il percorso assoluto sul tuo computer
# parse_dates: converte automaticamente le colonne indicate in oggetti "Data" (non semplice testo)
# encoding: necessario per leggere simboli speciali (come l'euro o lettere accentate) presenti nel file
df = pd.read_csv("C:\\Users\\david\\OneDrive\\Desktop\\esercizi python\\charts\\superstore_enriched.csv",
parse_dates=["Order Date", "Ship Date"], encoding="latin-1")

# Calcola il valore medio (somma di tutto / numero di ordini)
profit_mean = df["Profit"].mean()

# Calcola il valore mediano (il valore che sta esattamente a metà se ordiniamo tutti i profitti)
profit_median = df["Profit"].median()

# Stampa i risultati nel terminale (f indica una f-string per inserire variabili nel testo)
print(f"Media del Profitto: {profit_mean}")
print(f"Mediana del Profitto: {profit_median}")

# Crea una figura (la tela del grafico) di dimensioni 10x6 pollici
plt.figure(figsize=(10, 6))

# Disegna l'istogramma (le barre) + la curva KDE (la linea morbida della densità)
# bins=1000: divide i dati in 1000 "colonne" per vedere micro-variazioni (molto granulare)
# color="skyblue": imposta il colore azzurro chiaro
sns.histplot(df["Profit"], kde=True, bins=1000, color="skyblue")

# Disegna una linea verticale (axvline) rossa tratteggiata per la Media
# label: il testo che apparirà nella legenda
plt.axvline(profit_mean, color="red", linestyle="--", label=f"Media: {profit_mean:.2f}")

# Disegna una linea verticale blu tratteggiata per la Mediana
plt.axvline(profit_median, color="blue", linestyle="--", label=f"Mediana: {profit_median:.2f}")

# Aggiunge il titolo principale in alto
plt.title("Distribuzione del Profitto")

# Etichetta l'asse X (valori del profitto) e l'asse Y (quante volte appaiono)
plt.xlabel("Profitto")
plt.ylabel("Frequenza")

# Mostra il riquadro della legenda con le etichette impostate sopra
plt.legend()

# Limita la visualizzazione tra -400 e +400 per evitare che outlier estremi schiaccino il grafico
plt.xlim(-400, 400)

# Mostra il grafico
plt.show()
#"Cosa noti tra media e mediana? Cosa suggerisce sulla distribuzione?"
# la media è molto più alta della mediana, il che suggerisce che ci sono molti valori di profitto molto alti (outlier) 
# che stanno spingendo la media verso l'alto, mentre la maggior parte dei profitti è concentrata intorno a valori più bassi (la mediana). 
# Questo indica una distribuzione asimmetrica con una coda a destra (positiva) dovuta agli outlier di profitto elevato.


