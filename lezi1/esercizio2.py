# Esercizio 1: La Calcolatrice Statistica (30 min)
# Invece di una calcolatrice standard, creiamone una utile per un analista.
# Obiettivo: Creare una funzione chiamata calcolatrice_kpi che accetti tre parametri: valore1, valore2 e operazione.
# 1. Operazioni ammesse:
# - "somma": restituisce la somma dei due valori.
# * "delta": restituisce la differenza percentuale tra valore1 (nuovo) e valore2 (vecchio). Formula: $\frac{(v1 - v2)}{v2}$.
# * "rapporto": restituisce valore1 / valore
# 2. Gestione Errori: Usa un blocco try-except per gestire la divisione per zero se valore2 è 0. 

def calcolatrice_kpi(valore1, valore2, operazione):
    try:
        if operazione == "somma":
            return valore1 + valore2
        elif operazione == "delta": 
            return (valore1 - valore2) / valore2
        elif operazione == "rapporto": 
            return valore1 / valore2
        else : 
            return "Operazione non valida"
    except ZeroDivisionError:
        return "Errore: Divisione per zero non consentita"
input_operazione = input("Inserisci l'operazione (somma, delta, rapporto): ")
input_valore1 = float(input("Inserisci il primo valore: "))
input_valore2 = float(input("Inserisci il secondo valore: "))
risultato = calcolatrice_kpi(input_valore1, input_valore2, input_operazione)
print(f"Il risultato dell'operazione {input_operazione} è: {risultato}")


# Esercizio 2: Digital Menù "CloudSub Bistrot" (30 min)
# In questo esercizio applichiamo i Dizionari e i Cicli.
# Obiettivo: Gestire il menù di un ristorante tramite un dizionario Python.
# - Creazione: Crea un dizionario chiamato menu dove le chiavi sono i nomi dei piatti e i valori sono i prezzi (es. 
# {"Pennette": 8.50, "Pollo": 12.00}).
# - Funzione mostra_menu: Crea una funzione che stampi ogni piatto con il relativo prezzo.
# - Funzione applica_sconto: Crea una funzione che accetti il dizionario menu e una percentuale di sconto, 
# aggiornando tutti i prezzi nel dizionario (Simulazione di un SCD Tipo 1, dove sovrascrivi il dato vecchio con il nuovo).

menu = {"Pennette": 8.50, "Pollo": 12.00, "Insalata": 6.00, "Pizza": 10.00, "Tiramisù": 5.00}
def mostra_menu(menu):
    for piatto in menu:
        print(f"piatto: {piatto}, prezzo: {menu[piatto]}")

def applica_sconto(menu, sconto):
    for piatto in menu:
       menu[piatto] = menu[piatto] * (1 - sconto / 100) #applica lo sconto al prezzo del piatto, sottraendo la percentuale di sconto dal prezzo originale
print(" Menù originale: ")
mostra_menu(menu)
print(" Menù con sconto del 10%: ")
applica_sconto(menu, 10)  # Applica un sconto del 10%
mostra_menu(menu)


