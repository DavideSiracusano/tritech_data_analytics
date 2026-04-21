# Task 3 — Top e Bottom performer

# Trova le top 10 città per fatturato totale (Sales)
# Trova le bottom 5 sotto-categorie per margine medio (Profit_Margin_Pct)
# Per entrambe, il risultato deve essere un DataFrame ordinato e leggibile

import pandas as pd
# Caricamento del dataset con gestione delle date e dell'encoding
df = pd.read_csv("C:\\Users\\david\\OneDrive\\Desktop\\esercizi python\\lez2\\Superstore.csv", parse_dates=["Order Date", "Ship Date"], encoding="latin-1")

#top 10 città per fatturato totale
sales_tot = df.groupby("City").agg(total_sales = ("Sales", "sum"))
print(sales_tot)
top10_sales_tot = sales_tot.sort_values(by="total_sales",ascending=False).head(10)
print(top10_sales_tot)

#trova le bottom 5 sotto categorie per margine medio
df["Profit_Margin_Pct"] = (df["Profit"] / df["Sales"]) * 100
margin_sub_cat = df.groupby("Sub-Category").agg(avg_margin = ("Profit_Margin_Pct", "mean"))
bottom5 = margin_sub_cat.sort_values(by = "avg_margin", ascending= True).head(5)
print(bottom5)