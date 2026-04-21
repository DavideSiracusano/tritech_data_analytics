import pandas as pd

# Creiamo un piccolo set di dati di prova
data = {
    'Prodotto': ['Laptop', 'Mouse', 'Monitor'],
    'Prezzo': [1200, 25, 200],
    'Quantità': [5, 50, 10]
}

# Creiamo un DataFrame
df = pd.DataFrame(data)

# Calcoliamo il totale per riga
df['Totale_Stock'] = df['Prezzo'] * df['Quantità']

print("--- Test Pandas riuscito! ---")
print(df)
print("\nMedia prezzi:", df['Prezzo'].mean())