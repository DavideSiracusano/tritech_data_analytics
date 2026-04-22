import pandas as pd

# Caricamento
df = pd.read_csv("C:\\Users\\david\\OneDrive\\Desktop\\esercizi python\\lez2\\Superstore.csv", 
                 parse_dates=["Order Date", "Ship Date"], encoding="latin-1")

# Colonne derivate (Task 2)
df = df.assign(
    Shipping_Days=(df["Ship Date"] - df["Order Date"]).dt.days,
    Profit_Margin_Pct=round((df["Profit"] / df["Sales"]) * 100, 2),
    Is_Loss=df["Profit"] < 0
)

# Merge con budget_regioni (Task 5)
budget_regioni = pd.DataFrame({
    "Region": ["East", "West", "Central", "South"],
    "Budget_Annuale": [500000, 600000, 550000, 450000]
})

merged_df = pd.merge(df, budget_regioni, on="Region", how="left")
merged_df = merged_df.assign(
    budget_usato=merged_df["Sales"] / merged_df["Budget_Annuale"] * 100
)

# Export (Task 6)
merged_df.to_csv("superstore_enriched.csv", index=False, encoding="latin-1")
print("Export completato! Shape:", merged_df.shape)
print(merged_df[["Shipping_Days", "Profit_Margin_Pct", "Is_Loss", "Budget_Annuale", "budget_usato"]].head())