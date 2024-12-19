---
icon: LiMessagesSquare
iconColor: "#88FFFF"
---
Le **code di messaggi** (in inglese _**message queues**_) sono un meccanismo di [comunicazione tra processi](Processi.md#7%20-%20Comunicazione%20tra%20processi%20(IPC)) che permette a più processi di inviare e ricevere messaggi in maniera asincrona: un processo può inserire un messaggio in una coda, e un altro processo (o più processi) può leggerlo in un momento successivo, senza che i processi debbano sincronizzarsi perfettamente.

# 1 - Caratteristiche principali

- **Asincronia**: un processo può inviare un messaggio senza aspettare che l'altro processo lo legga immediatamente.
- **Ordinamento**: i messaggi sono normalmente gestiti secondo la politica FIFO (First In, First Out), cioè il primo messaggio inserito è il primo a essere letto.
- **Identificatori**: i messaggi possono avere identificatori o tipi per permettere ai processi di filtrare quelli di interesse.
- **Persistenza temporanea**: i messaggi rimangono nella coda fino a quando non vengono letti o cancellati.

# 2 - Funzionamento delle code di messaggi

In un sistema operativo come UNIX o Linux, le code di messaggi sono implementate usando una serie di chiamate di sistema%%link%%:
- `msgget()`: crea o accede a una coda di messaggi esistente.
- `msgsnd()`: invia un messaggio a una coda.
- `msgrcv()`: riceve un messaggio da una coda.
- `msgctl()`: esegue operazioni di controllo sulla coda, come eliminarla.

## 2.1 - Esempio di codice in linguaggio C

Ecco un esempio di uso delle code di messaggi in linguaggio C%%link%%, in cui un processo invia un messaggio a una coda e un altro lo legge.

Ecco il codice per scrivere in una coda:

```c
#include <stdio.h>
#include <sys/ipc.h>
#include <sys/msg.h>
#include <string.h>

// Definizione della struttura del messaggio
struct msg_buffer {
    long msg_type;
    char msg_text[100];
} message;

int main() {

    // Generazione di una chiave univoca
    key_t key = ftok("progfile", 65);

    // Creazione di una coda di messaggi e ottenimento del suo ID
    int msgid = msgget(key, 0666 | IPC_CREAT);

    message.msg_type = 1;

    printf("Inserisci un messaggio: ");
    fgets(message.msg_text, sizeof(message.msg_text), stdin);

    // Invio del messaggio nella coda
    msgsnd(msgid, &message, sizeof(message), 0);

    printf("Messaggio inviato: %s\n", message.msg_text);

    return 0;
}
```

Ecco il codice per leggere dalla coda:

```c
#include <stdio.h>
#include <sys/ipc.h>
#include <sys/msg.h>

// Definizione della struttura del messaggio
struct msg_buffer {
    long msg_type;
    char msg_text[100];
} message;

int main() {

    // Generazione di una chiave univoca
    key_t key = ftok("progfile", 65);

    // Accesso alla coda di messaggi esistente
    int msgid = msgget(key, 0666 | IPC_CREAT);

    // Ricezione del messaggio dalla coda
    msgrcv(msgid, &message, sizeof(message), 1, 0);

    // Stampa del messaggio ricevuto
    printf("Messaggio ricevuto: %s\n", message.msg_text);

    // Rimozione della coda di messaggi
    msgctl(msgid, IPC_RMID, NULL);

    return 0;
}
```

Spiegazione del codice:
- `key_t key = ftok("progfile", 65);`: genera una chiave univoca, utilizzata per identificare la coda di messaggi.
- `msgget()`: crea (o accede, se esiste già) a una coda di messaggi associata a quella chiave.
- `msgsnd()`: invia un messaggio a quella coda. Il messaggio è contenuto nella struttura `msg_buffer`, dove `msg_type` indica il tipo di messaggio e `msg_text` contiene il testo.
- `msgrcv()`: riceve un messaggio dalla coda. È possibile specificare un tipo di messaggio (`msg_type`) per filtrare i messaggi da leggere.
- `msgctl()`: rimuove la coda di messaggi quando non è più necessaria.

# 3 - Vantaggi e svantaggi delle code di messaggi

I principali vantaggi delle code di messaggi sono:
- **Comunicazione asincrona**: i processi non devono essere eseguiti contemporaneamente per scambiarsi dati. Un processo può inviare un messaggio e terminare, mentre il destinatario può ricevere il messaggio in un secondo momento.
- **Decoupling tra processi**: i processi non devono essere direttamente collegati o conoscere l'identità l'uno dell'altro. Questo rende i sistemi più flessibili e modulari, poiché è possibile aggiungere o rimuovere processi senza influenzare gli altri.
- **Ordine dei messaggi**: i messaggi vengono normalmente gestiti secondo la politica FIFO (First In, First Out). Questo garantisce che i messaggi vengano elaborati nell'ordine in cui sono stati inviati, il che è utile per mantenere la coerenza temporale.
- **Supporto per messaggi di diversi tipi e filtri**: è possibile associare a ciascun messaggio un "tipo" o identificatore. Questo permette ai processi di filtrare e leggere solo i messaggi di un certo tipo, migliorando la flessibilità nella gestione di diverse categorie di messaggi.
- **Persistenza temporanea dei messaggi**: i messaggi rimangono nella coda fino a quando non vengono letti, rendendo possibile la comunicazione anche se i processi sono avviati o terminano in momenti diversi.
- **Semplicità di implementazione**: le code di messaggi offrono un'interfaccia relativamente semplice per inviare e ricevere dati rispetto ad altre tecniche di comunicazione tra processi più complesse come [socket](Socket.md) o [memoria condivisa](Memoria%20condivisa.md).

I principali svantaggi delle code di messaggi sono:
- **Dimensione limitata della coda**: le code di messaggi hanno una dimensione massima limitata. Se la coda si riempie e non viene letta in tempo, i nuovi messaggi non possono essere inviati, causando un blocco o un ritardo nei processi di invio.
- **Performance**: le operazioni sulle code di messaggi possono introdurre overhead, poiché ogni operazione di invio e ricezione richiede il passaggio attraverso il kernel del sistema operativo. Questo rende le code di messaggi meno efficienti rispetto a metodi come la [memoria condivisa](Memoria%20condivisa.md), che permette accesso diretto ai dati.
- **Possibile perdita di messaggi**: se la coda viene eliminata o se un processo termina bruscamente senza leggere i messaggi, questi possono essere persi, a meno che non venga implementato un meccanismo di persistenza.
- **Sincronizzazione non garantita**: anche se la comunicazione è asincrona, i processi che devono essere strettamente sincronizzati richiederanno meccanismi aggiuntivi (es. semafori%%link%%) per evitare condizioni di gara (race conditions%%link%%) o accessi concorrenti ai messaggi.
- **Meno adatte per grandi quantità di dati**: le code di messaggi sono più adatte per scambiare piccoli messaggi, piuttosto che grandi blocchi di dati. Per grandi quantità di dati, la [memoria condivisa](Memoria%20condivisa.md) è più efficiente.
- **Gestione complessa di timeout**: la gestione dei timeout (attesa di un messaggio per un certo tempo prima di rinunciare) può richiedere logica aggiuntiva, rendendo la programmazione più complessa in scenari che necessitano di risposte rapide o certe.

# Fonti

- Abraham Silberschatz, Peter Baer Galvin, Greg Gagne - [Sistemi Operativi (10ᵃ Edizione)](https://he.pearson.it/catalogo/1099) - Pearson, 2019 - ISBN: `9788891904560`.
- Slide del Prof. Aldinucci Marco del corso di Sistemi Operativi (canale B), Corso di Laurea in Informatica presso l'Università di Torino, A.A. 2024-25:
	- [Cap_03](https://informatica.i-learn.unito.it/mod/resource/view.php?id=253884)
