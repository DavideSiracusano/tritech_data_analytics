# Modulo 5: Challenge Finale: Mini-ETL (1 Ora)
# Scenario: Hai ricevuto una lista di MRR "sporca" dal sistema sorgente: dirty_mrr = [120, "80", 0, "N/A", 50, None].
# Obiettivo: Calcolare la media MRR evitando che lo script vada in crash.
# - Inizializza total_mrr = 0 e count = 0.
# - Usa un ciclo for con un blocco try-except all'interno.
# - Tenta di convertire ogni elemento in float().
# - Se la conversione riesce, sommalo a total_mrr e incrementa count.
# - Se incontri un errore (es. ValueError per "N/A"), usa continue per saltare il record e stampare un avviso.
# - Gestisci il caso in cui count sia zero (per evitare ZeroDivisionError) usando un if finale per stampare la media.


print("-------dati puliti---------")
dirty_mrr = [120, "80", 0, "N/A", 50, None]
total_mrr = 0
count = 0

def pulizia_valori(value):
    try: 
        return float(value)
    except(ValueError, TypeError):
        return 0.0
    
clean_mrr = [pulizia_valori(value) for value in dirty_mrr]

print(clean_mrr)

for n in clean_mrr:
    total_mrr += n
    count += 1
    print(total_mrr)
    print(count)

average = total_mrr/count
media_arrotondata = round(average)
print(media_arrotondata)


print("-------dati sporchi---------")
dirty_mrr = [120, "80", 0, "N/A", 50, None]
total_mrr = 0
count = 0

for n in dirty_mrr:
    try: 
        valore_pulito = float(n)
        total_mrr += valore_pulito
        count += 1
    except(ValueError, TypeError):
        print("errore, salto di numero")
        continue
   
if count == 0: 
    print("nessun dato trovato")
else:
    average = total_mrr/count
    print(average)
