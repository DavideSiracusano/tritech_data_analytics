# Modulo 3: Manipolazione Dati e Strutture (45 min)
# Esercizio A: Il simulatore OLTP
# Crea una lista chiamata raw_data contenente 5 dizionari. Ogni dizionario deve rappresentare un cliente con: id, company, plan (Starter, Pro, Enterprise)
#  mrr e country.
# - Aggiungi un sesto cliente usando .append().
# - Usa lo slicing per creare una nuova lista top_3 con i primi tre clienti della lista
# - Crea un Set chiamato unique_countries partendo dalla lista per ottenere l'elenco dei paesi senza duplicati (simile a SELECT DISTINCT).
# Esercizio B: Accesso e Trasformazione
# - Stampa il nome della company del secondo cliente nella lista.
# - Modifica il plan del terzo cliente da "Starter" a "Pro" (Simulazione SCD Tipo 1 ).

raw_data = [{
    "id" : 1,
    "company" : "Azienda1",
    "plan" : "Starter",
    "country" : "Roma",
    "mrr" : 500
},
{
    "id" : 2,
    "company" : "Azienda2",
    "plan" : "Pro",
    "country" : "Palermo",
    "mrr" : 500
},
{
    "id" : 3,
    "company" : "Azienda3",
    "plan" : "Starter",
    "country" : "Milano",
    "mrr" : 100
},
{
    "id" : 4,
    "company" : "Azienda4",
    "plan" : "Enterprise",
    "country" : "Napoli",
    "mrr" : 50
},
{
    "id" : 5,
    "company" : "Azienda5",
    "plan" : "Pro",
    "country" : "Roma",
    "mrr" : 45
}]

raw_data.append({
    "id" : 6,
    "company" : "Azienda6",
    "plan" : "Starter",
    "country" : "Torino",
    "mrr" : 500
})

top_3 = raw_data[:3]

print("top_3", top_3)



unique_countries = set(cliente["country"] for cliente in raw_data)

print("unique_countries", unique_countries)

print("company of second customer:", raw_data[1]["company"])

raw_data[2]["plan"] = "Pro" 
print("piano cliente aggiornato: ", raw_data[2])


# Modulo 4: Controllo del Flusso e KPI (1 Ora)
# Esercizio C: Logica di Segmentazione
# Scrivi un ciclo for che iteri su raw_data e:
# - Calcoli il MRR Totale della compagnia.
# - Applichi una logica if-elif-else per stampare:
# 1. "High Value" se l'MRR è > 100.
# 2. "Mid Value" se l'MRR è tra 50 e 100.
# 3. "Low Value" se l'MRR è < 50.
# Esercizio D: Simulazione SCD Tipo 2
# Crea una variabile new_plan = "Enterprise". Scrivi una logica che confronti il piano attuale di un cliente con new_plan:
# - Se sono diversi, stampa "Azione: Chiudi record vecchio e inserisci nuovo".
# - Se sono uguali, usa pass o stampa "Nessun cambiamento".

def calcola_mrr_totale(raw_data):
    mrr_totale = 0
    for cliente in raw_data:
        mrr_totale += cliente["mrr"]
        if mrr_totale > 100:
            print("High value")
        elif mrr_totale >= 50  and mrr_totale <= 100: 
            print("Mid Value")
        elif mrr_totale < 50:
            print("Low value")
        return mrr_totale


calcola_mrr_totale(raw_data)

# new_plan = "Enterprise"

# def confronto_piano(piano_attuale):
#         if piano_attuale == new_plan:
#             print("nessun cambiamento")
#         else:
#             print("Azione: Chiudi record vecchio e inserisci nuovo")

# confronto_piano(raw_data[0]["plan"])

new_plan = "Enterprise"

# 1. Chiediamo l'indice all'utente
scelta_utente = int(input("Inserisci l'indice del cliente (da 0 a 5): "))

# 2. Recuperiamo il dizionario completo del cliente
cliente_vecchio = raw_data[scelta_utente]

# 3. Funzione corretta
def confronti(cliente_aggiornato, nuovo_piano): 
    # Usiamo 'cliente' come parametro per accedere alle sue chiavi
    if cliente_aggiornato["plan"] == new_plan:
        print(f"Piano attuale: {cliente_aggiornato['plan']} -> nessun cambiamento")
    else: 
        print(f"Piano attuale: {cliente_aggiornato['plan']} -> Azione: Chiudi record vecchio e inserisci nuovo")
        nuovo_record = cliente_aggiornato.copy()
        max_id = max(cliente["id"] for cliente in raw_data)
        nuovo_id = max_id + 1
        nuovo_record["id"] = nuovo_id
        nuovo_record["plan"] = nuovo_piano

        raw_data.append(nuovo_record)
        print("cliente aggiornato", nuovo_record)

# 4. Chiamata alla funzione
confronti(cliente_vecchio, new_plan)
for clienti in raw_data:
    print(raw_data)
  



