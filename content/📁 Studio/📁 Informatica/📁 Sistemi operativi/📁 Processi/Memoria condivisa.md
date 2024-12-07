La **memoria condivisa** (in inglese _**shared memory**_) è un meccanismo di [comunicazione tra processi](Processi.md#7%20-%20Comunicazione%20tra%20processi%20(IPC)) che consente a più processi di accedere alla stessa area di memoria. Questo metodo è molto veloce poiché non richiede copie di dati tra processi, ma i processi devono coordinarsi per evitare conflitti di accesso.

# 1 - Caratteristiche principali

- **Accesso diretto ai dati**: la memoria condivisa consente a più processi di accedere allo stesso segmento di memoria fisica senza necessità di trasferire dati tra processi. Questo avviene mappando lo stesso spazio di memoria nello spazio di indirizzi virtuale di ciascun processo.
- **Elevata velocità di comunicazione**: poiché i dati non devono essere copiati o trasferiti, l'accesso alla memoria condivisa è estremamente rapido rispetto ad altri metodi di comunicazione tra processi, come le [code di messaggi](Code%20di%20messaggi.md) o i [socket](Socket.md).
- **Dipendenza dalla sincronizzazione**: la memoria condivisa non fornisce un meccanismo di sincronizzazione integrato. I processi devono gestire autonomamente l'accesso alla memoria per evitare condizioni di gara%%link%% e inconsistenze. Si utilizzano spesso semafori%%link%% o mutex%%link%% per garantire l'accesso ordinato.
- **Persistenza temporanea dei dati**: il segmento di memoria condivisa esiste fino a quando almeno un processo è collegato ad esso. Una volta che tutti i processi si scollegano, la memoria può essere rilasciata dal sistema operativo, oppure può essere rimossa esplicitamente con una chiamata di sistema%%link per "chiamata di sistema"%% come `shmctl()`.
- **Efficienza per grandi volumi di dati**: è particolarmente vantaggiosa per gestire dati di grandi dimensioni, poiché non richiede la duplicazione dei dati in ciascun processo che deve accedervi. Tutti i processi accedono alla stessa copia dei dati, riducendo l'uso di memoria e migliorando l'efficienza.
- **Accesso locale**: la memoria condivisa funziona meglio per la comunicazione tra processi sullo stesso sistema. Per la comunicazione tra processi su sistemi diversi, occorre usare un altro meccanismo come i socket%%link%%.
- **Utilizzo di chiavi IPC**: nei sistemi UNIX/Linux%%link%%, ogni segmento di memoria condivisa è identificato da una chiave (usata con `shmget()`), permettendo ai processi di connettersi alla stessa area. Questo ID deve essere noto ai processi per poter accedere alla memoria. %%rendere più chiaro questo punto%%

La memoria condivisa funziona consentendo a più processi di accedere alla stessa area di memoria fisica. Di seguito sono illustrati i principali passaggi e concetti necessari per il funzionamento di una memoria condivisa in un sistema operativo come UNIX/Linux.

# 2 - Funzionamento della memoria condivisa

In un sistema operativo come UNIX o Linux, la memoria condivisa viene implementata usando una serie di chiamate di sistema%%link%%:
1. **Creazione dell'area di memoria**: un processo crea un'area di memoria condivisa con una chiamata di sistema%%link%% come `shmget()`. Questa funzione assegna un segmento di memoria e restituisce un ID per accedere alla memoria.
2. **Mappatura nello spazio di indirizzi**: una volta creata, l'area di memoria deve essere _mappata_, cioè collegata, allo spazio di indirizzi virtuale del processo, utilizzando `shmat()`. Questo permette al processo di accedere alla memoria come se fosse una variabile o un array ordinario.
3. **Accesso alla memoria**: dopo la mappatura, il processo può leggere e scrivere nella memoria condivisa. I dati scritti sono immediatamente visibili agli altri processi che accedono alla stessa area, a condizione che anch'essi abbiano mappato il segmento con `shmat()`.
4. **Sincronizzazione**: poiché più processi possono accedere contemporaneamente alla memoria, è necessario usare semafori%%link%%, mutex%%link%% o altri meccanismi di sincronizzazione. Questi impediscono che i processi modifichino la stessa area di memoria nello stesso momento, evitando condizioni di stallo o errori di dati incoerenti.
5. **Scollegamento dalla memoria**: quando un processo ha terminato l'uso della memoria condivisa, la "scollega" usando `shmdt()`. Tuttavia, la memoria non viene liberata fino a quando tutti i processi che vi sono connessi non si sono scollegati.
6. **Rimozione dell'area di memoria**: dopo lo scollegamento, il segmento di memoria condivisa può essere rimosso definitivamente con `shmctl()`, che libera la memoria.

## 2.1 - Esempio di codice in linguaggio C

Ecco un esempio di uso della memoria condivisa in linguaggio C%%link%% che illustra come due processi possano utilizzare la memoria condivisa per scambiarsi informazioni.

```c
#include <stdio.h>
#include <stdlib.h>
#include <sys/ipc.h>
#include <sys/shm.h>
#include <sys/types.h>

int main() {
    // Chiave IPC e dimensione della memoria
    key_t key = ftok("shmfile", 65); // Genera una chiave unica
    int shmid = shmget(key, 1024, 0666|IPC_CREAT); // Crea memoria condivisa

    // Mappa la memoria nello spazio di indirizzi
    char *data = (char*) shmat(shmid, (void*)0, 0);

    // Scrive nella memoria condivisa
    printf("Scrivo 'Hello World' nella memoria condivisa\n");
    sprintf(data, "Hello World");

    // Stacca la memoria
    shmdt(data);

    return 0;
}
```

Un secondo programma potrebbe collegarsi alla stessa area di memoria con lo stesso `key_t` e leggere il messaggio.

# 3 - Vantaggi e svantaggi della memoria condivisa

I principali vantaggi della memoria condivisa sono:
- **Elevata velocità di comunicazione**: l'accesso diretto alla stessa area di memoria elimina la necessità di copiare dati tra processi, garantendo una comunicazione molto rapida. Questo è particolarmente utile in applicazioni ad alte prestazioni, come la grafica, il calcolo scientifico, o i sistemi di trading.
- **Efficienza per grandi quantità di dati**: la memoria condivisa è ideale per scambiare grandi volumi di dati tra processi, poiché riduce il consumo di memoria rispetto alla duplicazione dei dati. Tutti i processi accedono allo stesso blocco di dati, quindi è molto efficiente in termini di utilizzo della memoria.
- **Flessibilità nel formato dei dati**: a differenza di altri metodi di comunicazione tra processi (come le [code di messaggi](Code%20di%20messaggi.md)), la memoria condivisa non impone un formato specifico dei dati, permettendo una grande flessibilità nella struttura dei dati da condividere.
- **Accesso simultaneo ai dati**: più processi possono accedere ai dati contemporaneamente, cosa che può ridurre il tempo di latenza in applicazioni real-time. Ciò è utile per operazioni di lettura parallela di dati comuni o aggiornamenti a bassa frequenza.

I principali svantaggi della memoria condivisa sono:
- **Necessità di sincronizzazione esplicita**: la memoria condivisa non include un meccanismo di sincronizzazione integrato. I processi devono coordinarsi manualmente per evitare condizioni di gara%%link%% o accessi incoerenti. Questo può complicare lo sviluppo e richiede l'uso di semafori%%link%% o mutex%%link%% per coordinare gli accessi.
- **Problemi di sicurezza e isolamento**: dal momento che la memoria condivisa è accessibile a più processi, un errore in uno di essi può influire su tutti gli altri. Il controllo degli accessi deve essere gestito correttamente per prevenire modifiche accidentali o non autorizzate, specialmente nei sistemi multiutente.
- **Debug complesso**: il debug della memoria condivisa è più complicato rispetto ad altri metodi di comunicazione tra processi, poiché le condizioni di gara%%link%% e i problemi di sincronizzazione possono essere difficili da rilevare. Gli errori di accesso concorrente possono portare a comportamenti non deterministici difficili da riprodurre.
- **Dipendenza dal sistema operativo**: l'implementazione della memoria condivisa varia tra sistemi operativi, quindi il codice potrebbe non essere portabile. Nei sistemi UNIX-like%%link%%, l'API POSIX%%link%% standardizza alcune chiamate di memoria condivisa, ma Windows%%link%% utilizza un set di API diverso (ad esempio `CreateFileMapping` e `MapViewOfFile`), creando complicazioni di portabilità.
- **Rimozione manuale della memoria**: la memoria condivisa non viene automaticamente rimossa se un processo termina senza scollegarla correttamente. Questo può portare a perdite di memoria (memory leak) nel sistema, rendendo necessaria la rimozione esplicita della memoria condivisa quando non è più utilizzata.

# Fonti

- Abraham Silberschatz, Peter Baer Galvin, Greg Gagne - [Sistemi Operativi (10ᵃ Edizione)](https://he.pearson.it/catalogo/1099) - Pearson, 2019 - ISBN: `9788891904560`.
- Slide del Prof. Aldinucci Marco del corso di Sistemi Operativi (canale B), Corso di Laurea in Informatica presso l'Università di Torino, A.A. 2024-25:
	- [Cap_03](https://informatica.i-learn.unito.it/mod/resource/view.php?id=253884)
