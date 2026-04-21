# Modulo 1: Quiz di Verifica
# 1. In Python, cosa succede se assegni un numero a una variabile che prima conteneva una stringa?
variabile = "Ciao"
variabile = 5
print(variabile)  # Output: 5 #cambia il tipo di dato della variabile da stringa a intero


# 2. Quale parola chiave Python corrisponde al NULL di SQL per indicare l'assenza di un dato?
# A) None


# 3. Quale struttura dati useresti per rappresentare una singola riga di un cliente con ID, Nome e MRR?
# A) Dizionario perché permette di associare chiavi (ID, Nome, MRR) a valori specifici per ogni cliente


# 4. A cosa serve l'istruzione continue in un ciclo for?
# L'istruzione continue viene utilizzata per saltare l'iterazione corrente del ciclo e passare alla successiva. 
# In altre parole, quando il programma incontra un continue, salta il resto del codice all'interno del ciclo per quella 
# iterazione e procede con la prossima iterazione del ciclo.


# 5. Se un attributo di un cliente (es. il piano) cambia e vogliamo mantenere la storia completa aggiungendo una nuova riga e "chiudendo" quella vecchia, quale strategia stiamo usando?
#stiamo usando la strategia di "Slowly Changing Dimension" (SCD) di tipo 2, 
# che prevede l'aggiunta di una nuova riga per ogni cambiamento di attributo, mantenendo così la storia completa dei dati.


# 6. Perché un analista usa il blocco try-except durante un processo ETL?
# Un analista usa il blocco try-except durante un processo ETL per gestire eventuali errori o eccezioni che possono verificarsi
#  durante l'esecuzione del processo.


# 7. Quale tra questi nomi di variabile è valido in Python?
# A) 2_mrr_cliente
# B) total-mrr
# C) total_mrr    i nomi delle variabili non possono inziare con un numero e devono contenere underscores invece di trattini come standard.