import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# tkinter è una libreria grafica built-in di Python, la si usa SOLO per leggere
# la risoluzione del monitor
import tkinter as tk

# --- Caricamento dati ---
# parse_dates: converte automaticamente quelle colonne da testo a oggetti datetime
# encoding latin-1: necessario per leggere caratteri speciali (accenti, simboli) nel CSV
df = pd.read_csv("C:\\Users\\david\\OneDrive\\Desktop\\esercizi python\\charts\\superstore_enriched.csv", parse_dates=["Order Date", "Ship Date"], encoding="latin-1")

# --- Rilevamento risoluzione schermo ---
root = tk.Tk()                          # crea una finestra tkinter invisibile temporanea
screen_w = root.winfo_screenwidth()     # legge la larghezza dello schermo in pixel (es. 1920)
screen_h = root.winfo_screenheight()   # legge l'altezza dello schermo in pixel (es. 1080)
root.destroy()                          # distrugge subito la finestra, non serve più

# matplotlib usa i POLLICI per le dimensioni, non i pixel
# dividiamo per 96 perché 96 DPI è lo standard dei monitor moderni (1 pollice = 96 pixel)
fig_w = screen_w / 96   # es. 1920 / 96 = 20 pollici di larghezza
fig_h = screen_h / 96   # es. 1080 / 96 = 11.25 pollici di altezza

# --- Creazione figura principale con subplots ---
# subplots(3, 2) = griglia di 3 righe e 2 colonne → 6 grafici totali
# figsize usa i pollici calcolati sopra → si adatta allo schermo
# axes è una matrice 3x2: axes[0,0] è in alto a sinistra, axes[2,1] in basso a destra
fig, axes = plt.subplots(3, 2, figsize=(fig_w, fig_h))

# Titolo generale della figura, sopra tutti i grafici
# fig_w * 0.9 scala il font proporzionalmente alla larghezza → più grande lo schermo, più grande il titolo
fig.suptitle("Superstore — Full Report", fontsize=fig_w * 0.9, fontweight="bold")

# --- Variabili di scala per i font ---
# Tutti i testi della figura usano queste variabili invece di valori fissi
# Così se lo schermo è piccolo i font restano leggibili, se è grande non sembrano microscopici
fs_title = fig_w * 0.7    # dimensione font per i titoli dei singoli grafici
fs_label = fig_w * 0.55   # dimensione font per le etichette degli assi (xlabel, ylabel)
fs_tick  = fig_w * 0.45   # dimensione font per i valori sui tick (numeri sugli assi) e legenda

# -------------------------------------------------------
# --- 01: Distribuzione del Profitto ---
# -------------------------------------------------------

# mean() calcola la media aritmetica di tutti i valori della colonna Profit
profit_mean = df["Profit"].mean()

# median() calcola il valore centrale: metà dei profitti sono sotto, metà sopra
profit_median = df["Profit"].median()

# histplot disegna l'istogramma (barre) + kde=True aggiunge la curva di densità morbida sopra
# bins=100: divide il range dei dati in 100 colonne verticali
# ax=axes[0,0]: disegna su questo specifico subplot (riga 0, colonna 0)
sns.histplot(df["Profit"], kde=True, bins=100, color="skyblue", ax=axes[0, 0])

# axvline disegna una linea verticale sull'asse x nel punto indicato (profit_mean)
# linestyle="--": linea tratteggiata
# label: testo che apparirà nella legenda con il valore formattato a 2 decimali
axes[0, 0].axvline(profit_mean, color="red", linestyle="--", label=f"Media: {profit_mean:.2f}")
axes[0, 0].axvline(profit_median, color="blue", linestyle="--", label=f"Mediana: {profit_median:.2f}")

# xlim limita la visualizzazione tra -400 e 400 per tagliare gli outlier estremi
# senza questo, pochi valori anomali molto alti/bassi "schiaccerebbero" tutto il grafico al centro
axes[0, 0].set_xlim(-400, 400)

# Titolo e label degli assi con font scalato
axes[0, 0].set_title("01 — Distribuzione del Profitto", fontsize=fs_title)
axes[0, 0].set_xlabel("Profitto", fontsize=fs_label)
axes[0, 0].set_ylabel("Frequenza", fontsize=fs_label)

# tick_params imposta la dimensione dei numeri sui due assi
axes[0, 0].tick_params(labelsize=fs_tick)

# legend() mostra il riquadro con le etichette delle linee verticali
axes[0, 0].legend(fontsize=fs_tick)

# -------------------------------------------------------
# --- 02: Boxplot Giorni di Spedizione ---
# -------------------------------------------------------

# boxplot mostra per ogni categoria: mediana, quartili, outlier
# x="Ship Mode": le 4 modalità di spedizione sull'asse orizzontale
# y="Shipping_Days": i giorni di spedizione sull'asse verticale
# hue="Ship Mode" + legend=False: colora le box per categoria senza mostrare legenda duplicata
sns.boxplot(x="Ship Mode", y="Shipping_Days", data=df, palette="Set1", hue="Ship Mode", legend=False, ax=axes[0, 1])

axes[0, 1].set_title("02 — Giorni di Spedizione per Modalità", fontsize=fs_title)
axes[0, 1].set_xlabel("Modalità di Spedizione", fontsize=fs_label)
axes[0, 1].set_ylabel("Giorni di Spedizione", fontsize=fs_label)
axes[0, 1].tick_params(labelsize=fs_tick)

# -------------------------------------------------------
# --- 03: Heatmap di Correlazione ---
# -------------------------------------------------------

# Selezioniamo solo le colonne numeriche su cui calcolare la correlazione
cols = ["Sales", "Profit", "Discount", "Quantity", "Shipping_Days", "Profit_Margin_Pct"]

# corr() calcola la matrice di correlazione: ogni cella vale tra -1 (inversa totale) e +1 (diretta totale)
# 0 significa nessuna correlazione lineare
corr = df[cols].corr()

# heatmap disegna la matrice come griglia colorata
# annot=True: scrive il valore numerico dentro ogni cella
# cmap="coolwarm": blu per valori negativi, rosso per positivi, bianco per zero
# vmin/vmax: fissa i limiti della scala colori a -1 e +1
# annot_kws: imposta la dimensione del font dei numeri nelle celle con la variabile scalata
sns.heatmap(corr, annot=True, cmap="coolwarm", vmin=-1, vmax=1, fmt=".2f", ax=axes[1, 0], annot_kws={"size": fs_tick})

axes[1, 0].set_title("03 — Matrice di Correlazione", fontsize=fs_title)
axes[1, 0].tick_params(labelsize=fs_tick)

# -------------------------------------------------------
# --- 04: Top 10 Prodotti per Vendite ---
# -------------------------------------------------------

# groupby raggruppa le righe per nome prodotto
# agg somma le vendite di ogni prodotto in una nuova colonna "total_sales"
# reset_index: riporta "Product Name" da indice a colonna normale
# sort_values + head(10): ordina dal più venduto e prende i primi 10
top_products = (df.groupby("Product Name").agg(total_sales=("Sales", "sum")).reset_index().sort_values("total_sales", ascending=False).head(10))

# barplot orizzontale: y=nomi prodotti (asse verticale), x=vendite (asse orizzontale)
# palette="viridis": scala di colori dal viola al giallo
sns.barplot(y="Product Name", x="total_sales", data=top_products, palette="viridis", ax=axes[1, 1])

axes[1, 1].set_title("04 — Top 10 Prodotti per Vendite", fontsize=fs_title)
axes[1, 1].set_xlabel("Vendite Totali", fontsize=fs_label)
axes[1, 1].set_ylabel("", fontsize=fs_label)  # ylabel vuoto: i nomi prodotto sono già sull'asse
axes[1, 1].tick_params(labelsize=fs_tick)

# -------------------------------------------------------
# --- 05: Trend Mensile delle Vendite ---
# -------------------------------------------------------

# Lavoriamo su una copia per non modificare il DataFrame originale
# (il set_index che segue cambierebbe df per tutti i grafici successivi)
df_temp = df.copy()

# resample richiede che la data sia l'indice del DataFrame
df_temp.set_index("Order Date", inplace=True)

# resample("ME"): raggruppa per fine mese (Month End)
# .sum(): somma le vendite di ogni mese
# .reset_index(): riporta la data da indice a colonna
monthly_sales = df_temp["Sales"].resample("ME").sum().reset_index()

# Convertiamo la data in stringa "YYYY-MM" (es. "2023-01")
# Matplotlib tratta le stringhe come categorie discrete → mostra un tick per ogni mese
# Se lasciassimo datetime, potrebbe raggruppare o saltare mesi con pochi dati
monthly_sales["Order Date"] = monthly_sales["Order Date"].dt.strftime("%Y-%m")

# lineplot con marker="o": linea continua con un pallino su ogni punto mensile
sns.lineplot(x="Order Date", y="Sales", data=monthly_sales, marker="o", color="royalblue", ax=axes[2, 0])

axes[2, 0].set_title("05 — Trend Mensile delle Vendite", fontsize=fs_title)
axes[2, 0].set_xlabel("Mese", fontsize=fs_label)
axes[2, 0].set_ylabel("Vendite Totali ($)", fontsize=fs_label)

# rotation=90: ruota le etichette dei mesi verticalmente per evitare sovrapposizioni
axes[2, 0].tick_params(axis="x", rotation=90, labelsize=fs_tick)
axes[2, 0].tick_params(axis="y", labelsize=fs_tick)

# -------------------------------------------------------
# --- 06: Scatterplot Sales vs Profit ---
# -------------------------------------------------------

# scatterplot: ogni punto è un ordine, posizionato in base a vendite (x) e profitto (y)
# hue="Category": colora i punti in base alla categoria merceologica
# alpha=0.7: trasparenza al 70% → dove i punti si sovrappongono si vede la densità
sns.scatterplot(x="Sales", y="Profit", hue="Category", data=df, palette="Set2", alpha=0.7, ax=axes[2, 1])

# axhline disegna una linea orizzontale a y=0 (Profit=0)
# Tutto sotto questa linea è in perdita, tutto sopra è in guadagno
axes[2, 1].axhline(0, color="red", linestyle="--", label="Profitto = 0")

axes[2, 1].set_title("06 — Scatterplot Vendite vs Profitto", fontsize=fs_title)
axes[2, 1].set_xlabel("Vendite ($)", fontsize=fs_label)
axes[2, 1].set_ylabel("Profitto ($)", fontsize=fs_label)
axes[2, 1].tick_params(labelsize=fs_tick)
axes[2, 1].legend(fontsize=fs_tick)

# -------------------------------------------------------
# --- Salvataggio e visualizzazione ---
# -------------------------------------------------------

# tight_layout: aggiusta automaticamente gli spazi tra i subplot
# per evitare che titoli e label si sovrappongano tra grafici adiacenti
plt.tight_layout()

# dpi=150: risoluzione del file PNG salvato (più alto = immagine più nitida ma file più pesante)
# bbox_inches="tight": include tutto nella figura senza tagliare nulla ai bordi
plt.savefig("00_full_report.png", dpi=150, bbox_inches="tight")

# mostra la figura nella finestra interattiva di matplotlib
plt.show()