# Modulo 6: Il "Garante dell'Unicità" (30 min)
# Obiettivo: Gestire l'integrità dei dati ed evitare duplicati (fondamentale per le Surrogate Key).
# Scenario: Hai una lista di nuovi customer_id che arrivano da un sistema esterno, ma sospetti che ci siano dei duplicati che potrebbero sporcare il tuo Data Warehouse.
# Task:
# 1. Crea una lista chiamata nuovi_id con questi valori: [101, 102, 101, 103, 104, 102, 105].
# 2. Scrivi una funzione verifica_duplicati(lista_id) che:
# - Conti quanti ID ci sono in totale.
# - Usi un Set per trovare quanti ID "unici" esistono.
# - Calcoli la differenza per dire all'utente quanti duplicati sono stati trovati.
# Output atteso: "Trovati 7 ID, di cui 2 duplicati. Caricamento di 5 record unici."

nuovi_id = [101, 102, 101, 103, 104, 102, 105]



def verifica_duplicati(lista_id):
    # lunghezza lista intera
    lunghezza_lista = len(lista_id)
    # id unici con set
    unique_id = set(lista_id)
    # lunghezza id unici
    unique_id_lunghezza = len(unique_id)

    differenza =  lunghezza_lista - unique_id_lunghezza
    
    print("id totali: ", lunghezza_lista)
    print("id unici: ", unique_id_lunghezza)
    print("id duplicati: ", differenza)


      

verifica_duplicati(nuovi_id)