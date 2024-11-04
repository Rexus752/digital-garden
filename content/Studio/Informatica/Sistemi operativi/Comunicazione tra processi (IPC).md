Spesso, i processi hanno bisogno di comunicare e collaborare tra di loro scambiandosi dati. La **comunicazione tra processi** (IPC, Inter-Process Communication) riguarda le tecniche e i meccanismi attraverso cui i processi di un sistema operativo, che possono essere eseguiti in parallelo o separatamente, scambiano informazioni tra loro. Ogni metodo di comunicazione tra processi ha vantaggi e svantaggi, ed è scelto in base alle esigenze specifiche di sincronizzazione, latenza, throughput e complessità dell'applicazione.

Le principali tecniche di comunicazione tra processi sono:
- [**Pipe**](Comunicazione%20tra%20processi%20(IPC).md#1%20-%20Pipe): permettono la comunicazione unidirezionale tra processi, tipicamente tra un processo padre e i suoi processi figli, trasferendo dati in modo sequenziale.
- [**Code di messaggi**](Comunicazione%20tra%20processi%20(IPC).md#2%20-%20Code%20di%20messaggi): consentono a più processi di scambiarsi informazioni tramite messaggi strutturati, inviati a una coda condivisa; questa tecnica è particolarmente adatta per la comunicazione asincrona.
- [**Memoria condivisa**](Comunicazione%20tra%20processi%20(IPC).md#3%20-%20Memoria%20condivisa): permette a più processi di accedere a un'area di memoria comune per scambiare dati in modo molto rapido, anche se richiede un sistema di sincronizzazione per evitare conflitti di accesso.
- [**Socket**](Comunicazione%20tra%20processi%20(IPC).md#4%20-%20Socket): utilizzati per la comunicazione tra processi su sistemi diversi (o anche sullo stesso sistema), sfruttano la rete per il trasferimento di dati e sono alla base della comunicazione in rete, sia locale che remota.
- [**Chiamate di procedure remote (RPC)**](Comunicazione%20tra%20processi%20(IPC).md#5%20-%20Chiamate%20di%20procedure%20remote%20(RPC)): consentono a un processo di richiedere l'esecuzione di una funzione su un sistema remoto, come se fosse locale, semplificando la programmazione distribuita nascondendo i dettagli della comunicazione di rete.

# 1 - Pipe

Le **pipe** %%([pronuncia]: `/paɪp/`)%%sono un meccanismo di comunicazione tra processi che permette a uno o più processi di condividere dati tramite un canale unidirezionale. In sostanza, una pipe crea un collegamento tra due processi: uno scrive dati nella pipe e l'altro legge quei dati.

## 1.1 - Principali caratteristiche delle pipe

Le principali caratteristiche delle pipe sono:
- **Unidirezionali**: i dati fluiscono in una sola direzione (dal processo scrivente a quello leggente).
- **Anonime**: sono tipicamente usate tra processi che hanno una relazione gerarchica (padre-figlio). In genere, il processo padre crea una pipe e poi genera il processo figlio che la usa.
- **Comunicazione in memoria**: la pipe si comporta come un buffer circolare tra i due processi, memorizzando temporaneamente i dati fino a quando non vengono letti.

## 1.2 - Funzionamento delle pipe

Una pipe in UNIX o Linux può essere creata con la chiamata di sistema%%link%% `pipe()`. Questa funzione genera due file descriptor:
- Il file descriptor per la lettura (`fd[0]`);
- Il file descriptor per la scrittura (`fd[1]`).

Un processo può scrivere dati nel file descriptor `fd[1]` e un altro processo può leggerli dal file descriptor `fd[0]`.

%%mettere link ai file descriptor%%

### 1.2.1 - Esempio di codice in linguaggio C

Ecco un esempio di uso delle pipe in linguaggio C%%link%%, in cui un processo padre invia un messaggio al processo figlio usando una pipe.

```c
#include <stdio.h>
#include <unistd.h>
#include <string.h>

int main() {
    int fd[2]; // fd[0] per lettura, fd[1] per scrittura
    pid_t pid;
    char buffer[100];
    
    // Creazione della pipe
    if (pipe(fd) == -1) {
        perror("pipe");
        return 1;
    }

    // Creazione del processo figlio
    pid = fork();

    if (pid < 0) {
        perror("fork");
        return 1;
    }

    if (pid > 0) {
        // Processo padre
        close(fd[0]); // Chiudiamo l'estremità di lettura nel padre

        // Scriviamo un messaggio nella pipe
        char msg[] = "Ciao dal processo padre!";
        write(fd[1], msg, strlen(msg) + 1);

        close(fd[1]); // Chiudiamo l'estremità di scrittura dopo aver scritto
    } else {
        // Processo figlio
        close(fd[1]); // Chiudiamo l'estremità di scrittura nel figlio

        // Leggiamo il messaggio dalla pipe
        read(fd[0], buffer, sizeof(buffer));
        printf("Messaggio ricevuto dal figlio: %s\n", buffer);

        close(fd[0]); // Chiudiamo l'estremità di lettura dopo aver letto
    }

    return 0;
}
```

Spiegazione del codice:
- `pipe(fd)` crea una pipe. `fd[0]` è usato per la lettura e `fd[1]` per la scrittura.
- `fork()` crea un nuovo processo figlio.
	- Nel processo padre, chiudiamo l'estremità di lettura (`fd[0]`) e scriviamo il messaggio nella pipe tramite `write()`.
	- Nel processo figlio, chiudiamo l'estremità di scrittura (`fd[1]`) e leggiamo il messaggio tramite `read()`.
- Dopo la comunicazione, ogni processo chiude l'estremità della pipe che non è più necessaria.
%%nel codice e nella sua spiegazione scrivere tutto in modo impersonale, non in prima persona plurale%%

## 1.3 - Vantaggi e svantaggi delle pipe

I principali vantaggi delle pipe sono:
- **Semplicità**: le pipe sono facili da usare e implementare, soprattutto per la comunicazione tra processi con una relazione gerarchica (ad esempio, un processo padre e un processo figlio). Sono supportate direttamente a livello del sistema operativo, con chiamate di sistema semplici come `pipe()` per creare una pipe e `read()`/`write()` per leggere e scrivere dati.
- **Comunicazione unidirezionale**: le pipe forniscono un canale di comunicazione unidirezionale, utile in situazioni in cui i dati devono fluire solo in una direzione (da un processo produttore a un processo consumatore).
- **Buffering automatico**: le pipe utilizzano un buffer interno gestito dal sistema operativo, che rende la gestione dei dati tra i processi più semplice, senza necessità di gestire manualmente il buffering dei dati.
- **Sincronizzazione implicita**: le pipe assicurano una forma di sincronizzazione implicita, in quanto se un processo tenta di leggere da una pipe vuota, verrà bloccato fino a quando non ci saranno dati disponibili. Allo stesso modo, se la pipe è piena, il processo che scrive attenderà fino a quando c'è spazio libero.
- **Indipendenza dalla rete**: le pipe funzionano a livello locale tra processi sullo stesso sistema, senza necessità di connessioni di rete, il che le rende efficienti in termini di prestazioni per la comunicazione tra processi locali.

I principali svantaggi delle pipe sono:
- **Unidirezionalità**: i dati nelle pipe possono fluire in una sola direzione. Se è necessaria la comunicazione bidirezionale (andata e ritorno), bisogna creare due pipe, aumentando la complessità della gestione dei dati.
- **Uso limitato tra processi correlati**: le pipe, dette anche _pipe anonime_ o _pipe convenzionali_, funzionano solo tra processi che hanno una relazione gerarchica (ad esempio, un processo padre che comunica con il figlio). Per comunicare tra processi non correlati, è necessario usare le [named pipe](Comunicazione%20tra%20processi%20(IPC).md#1.4%20-%20Named%20pipe), che sono più complesse da gestire rispetto alle pipe anonime.
- **Capacità limitata**: le pipe hanno una capacità limitata (tipicamente qualche kilobyte%%link%%). Se il buffer si riempie, il processo scrivente viene bloccato finché il buffer non viene svuotato. Allo stesso modo, se non ci sono dati, il processo leggente viene bloccato.
- **Accesso sequenziale**: le pipe operano in modo sequenziale secondo la politica FIFO (First In, First Out). Questo è ideale per flussi semplici di dati, ma in scenari complessi, in cui è richiesta una gestione avanzata dei messaggi, le pipe possono risultare limitate.
- **No persistenza dei dati**: i dati nelle pipe sono transienti, cioè una volta che i dati vengono letti, vengono rimossi dalla pipe. Se un processo legge i dati ma non li elabora correttamente, non è possibile rileggere il messaggio. Inoltre, se un processo termina senza leggere i dati, questi vengono persi.
- **Sincronizzazione manuale nei processi complessi**: sebbene ci sia sincronizzazione implicita, in scenari complessi potrebbe essere necessario gestire manualmente la sincronizzazione tra processi per evitare race condition%%link%% o blocchi inutili.
- **Non adatte per grandi quantità di dati**: le pipe sono ideali per il passaggio di piccoli blocchi di dati. Quando è necessario trasferire grandi quantità di dati o file complessi, l'uso delle pipe diventa inefficiente rispetto ad altri metodi di comunicazione tra processi come la [memoria condivisa](Comunicazione%20tra%20processi%20(IPC).md#3%20-%20Memoria%20condivisa).

## 1.4 - Named pipe

Le **named pipe** (anche chiamate _FIFO_ per il loro comportamento) sono una versione più avanzata delle cosiddette _pipe anonime_ o _pipe convenzionali_, cioè le pipe ordinarie: a differenza di quest'ultime, infatti, le named pipe possono essere utilizzate anche tra processi non legati da una relazione padre-figlio e sono bidirezionali. Vengono create con il comando `mkfifo` o la chiamata di sistema `mkfifo()`.

Ecco un esempio in bash di named pipe:

```bash
mkfifo mypipe
```

Dopo aver creato una named pipe, due processi distinti possono usarla per scambiarsi dati:
- Un processo può scrivere nella pipe con `echo "Hello" > mypipe`;
- Un altro processo può leggere da essa con `cat < mypipe`.

%% approfondire le named pipe (magari con un esempio fatto meglio) %%

%%
\#### Pipe nella shell

Esempi: `pipe()` in UNIX/Linux, pipe nei comandi shell (`|`).
%%

# 2 - Code di messaggi

Le **code di messaggi** (message queues) sono un meccanismo di comunicazione tra processi che permette a più processi di inviare e ricevere messaggi in maniera asincrona: un processo può inserire un messaggio in una coda, e un altro processo (o più processi) può leggerlo in un momento successivo, senza che i processi debbano sincronizzarsi perfettamente.

## 2.1 - Principali caratteristiche delle code di messaggi

Le principali caratteristiche delle code di messaggi sono:
- **Asincronia**: un processo può inviare un messaggio senza aspettare che l'altro processo lo legga immediatamente.
- **Ordinamento**: i messaggi sono normalmente gestiti secondo la politica FIFO (First In, First Out), cioè il primo messaggio inserito è il primo a essere letto.
- **Identificatori**: i messaggi possono avere identificatori o tipi per permettere ai processi di filtrare quelli di interesse.
- **Persistenza temporanea**: i messaggi rimangono nella coda fino a quando non vengono letti o cancellati.

## 2.2 - Funzionamento delle code di messaggi

In un sistema operativo come UNIX o Linux, le code di messaggi sono implementate usando una serie di chiamate di sistema%%link%%:
- `msgget()`: crea o accede a una coda di messaggi esistente.
- `msgsnd()`: invia un messaggio a una coda.
- `msgrcv()`: riceve un messaggio da una coda.
- `msgctl()`: esegue operazioni di controllo sulla coda, come eliminarla.

### 2.2.1 - Esempio di codice in linguaggio C

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

## 2.3 - Vantaggi e svantaggi delle code di messaggi

I principali vantaggi delle code di messaggi sono:
- **Comunicazione asincrona**: i processi non devono essere eseguiti contemporaneamente per scambiarsi dati. Un processo può inviare un messaggio e terminare, mentre il destinatario può ricevere il messaggio in un secondo momento.
- **Decoupling tra processi**: i processi non devono essere direttamente collegati o conoscere l'identità l'uno dell'altro. Questo rende i sistemi più flessibili e modulari, poiché è possibile aggiungere o rimuovere processi senza influenzare gli altri.
- **Ordine dei messaggi**: i messaggi vengono normalmente gestiti secondo la politica FIFO (First In, First Out). Questo garantisce che i messaggi vengano elaborati nell'ordine in cui sono stati inviati, il che è utile per mantenere la coerenza temporale.
- **Supporto per messaggi di diversi tipi e filtri**: è possibile associare a ciascun messaggio un "tipo" o identificatore. Questo permette ai processi di filtrare e leggere solo i messaggi di un certo tipo, migliorando la flessibilità nella gestione di diverse categorie di messaggi.
- **Persistenza temporanea dei messaggi**: i messaggi rimangono nella coda fino a quando non vengono letti, rendendo possibile la comunicazione anche se i processi sono avviati o terminano in momenti diversi.
- **Semplicità di implementazione**: le code di messaggi offrono un'interfaccia relativamente semplice per inviare e ricevere dati rispetto ad altre tecniche di comunicazione tra processi più complesse come [socket](Comunicazione%20tra%20processi%20(IPC).md#4%20-%20Socket) o [memoria condivisa](Comunicazione%20tra%20processi%20(IPC).md#3%20-%20Memoria%20condivisa).

I principali svantaggi delle code di messaggi sono:
- **Dimensione limitata della coda**: le code di messaggi hanno una dimensione massima limitata. Se la coda si riempie e non viene letta in tempo, i nuovi messaggi non possono essere inviati, causando un blocco o un ritardo nei processi di invio.
- **Performance**: le operazioni sulle code di messaggi possono introdurre overhead, poiché ogni operazione di invio e ricezione richiede il passaggio attraverso il kernel del sistema operativo. Questo rende le code di messaggi meno efficienti rispetto a metodi come la [memoria condivisa](Comunicazione%20tra%20processi%20(IPC).md#3%20-%20Memoria%20condivisa), che permette accesso diretto ai dati.
- **Possibile perdita di messaggi**: se la coda viene eliminata o se un processo termina bruscamente senza leggere i messaggi, questi possono essere persi, a meno che non venga implementato un meccanismo di persistenza.
- **Sincronizzazione non garantita**: anche se la comunicazione è asincrona, i processi che devono essere strettamente sincronizzati richiederanno meccanismi aggiuntivi (es. semafori%%link%%) per evitare condizioni di gara (race conditions%%link%%) o accessi concorrenti ai messaggi.
- **Meno adatte per grandi quantità di dati**: le code di messaggi sono più adatte per scambiare piccoli messaggi, piuttosto che grandi blocchi di dati. Per grandi quantità di dati, la [memoria condivisa](Comunicazione%20tra%20processi%20(IPC).md#3%20-%20Memoria%20condivisa) è più efficiente.
- **Gestione complessa di timeout**: la gestione dei timeout (attesa di un messaggio per un certo tempo prima di rinunciare) può richiedere logica aggiuntiva, rendendo la programmazione più complessa in scenari che necessitano di risposte rapide o certe.

# 3 - Memoria condivisa

La **memoria condivisa** (shared memory) è un meccanismo di comunicazione tra processi che consente a più processi di accedere alla stessa area di memoria. Questo metodo è molto veloce poiché non richiede copie di dati tra processi, ma i processi devono coordinarsi per evitare conflitti di accesso.

## 3.1 - Principali caratteristiche della memoria condivisa

Le principali caratteristiche della memoria condivisa sono:
- **Accesso diretto ai dati**: la memoria condivisa consente a più processi di accedere allo stesso segmento di memoria fisica senza necessità di trasferire dati tra processi. Questo avviene mappando lo stesso spazio di memoria nello spazio di indirizzi virtuale di ciascun processo.
- **Elevata velocità di comunicazione**: poiché i dati non devono essere copiati o trasferiti, l'accesso alla memoria condivisa è estremamente rapido rispetto ad altri metodi di comunicazione tra processi, come le [code di messaggi](Comunicazione%20tra%20processi%20(IPC).md#2%20-%20Code%20di%20messaggi) o i [socket](Comunicazione%20tra%20processi%20(IPC).md#4%20-%20Socket).
- **Dipendenza dalla sincronizzazione**: la memoria condivisa non fornisce un meccanismo di sincronizzazione integrato. I processi devono gestire autonomamente l'accesso alla memoria per evitare condizioni di gara%%link%% e inconsistenze. Si utilizzano spesso semafori%%link%% o mutex%%link%% per garantire l'accesso ordinato.
- **Persistenza temporanea dei dati**: il segmento di memoria condivisa esiste fino a quando almeno un processo è collegato ad esso. Una volta che tutti i processi si scollegano, la memoria può essere rilasciata dal sistema operativo, oppure può essere rimossa esplicitamente con una chiamata di sistema%%link per "chiamata di sistema"%% come `shmctl()`.
- **Efficienza per grandi volumi di dati**: è particolarmente vantaggiosa per gestire dati di grandi dimensioni, poiché non richiede la duplicazione dei dati in ciascun processo che deve accedervi. Tutti i processi accedono alla stessa copia dei dati, riducendo l'uso di memoria e migliorando l'efficienza.
- **Accesso locale**: la memoria condivisa funziona meglio per la comunicazione tra processi sullo stesso sistema. Per la comunicazione tra processi su sistemi diversi, occorre usare un altro meccanismo come i socket%%link%%.
- **Utilizzo di chiavi IPC**: nei sistemi UNIX/Linux%%link%%, ogni segmento di memoria condivisa è identificato da una chiave (usata con `shmget()`), permettendo ai processi di connettersi alla stessa area. Questo ID deve essere noto ai processi per poter accedere alla memoria. %%rendere più chiaro questo punto%%

La memoria condivisa funziona consentendo a più processi di accedere alla stessa area di memoria fisica. Di seguito sono illustrati i principali passaggi e concetti necessari per il funzionamento di una memoria condivisa in un sistema operativo come UNIX/Linux.

## 3.2 - Funzionamento della memoria condivisa

In un sistema operativo come UNIX o Linux, la memoria condivisa viene implementata usando una serie di chiamate di sistema%%link%%:
1. **Creazione dell'area di memoria**: un processo crea un'area di memoria condivisa con una chiamata di sistema%%link%% come `shmget()`. Questa funzione assegna un segmento di memoria e restituisce un ID per accedere alla memoria.
2. **Mappatura nello spazio di indirizzi**: una volta creata, l'area di memoria deve essere _mappata_, cioè collegata, allo spazio di indirizzi virtuale del processo, utilizzando `shmat()`. Questo permette al processo di accedere alla memoria come se fosse una variabile o un array ordinario.
3. **Accesso alla memoria**: dopo la mappatura, il processo può leggere e scrivere nella memoria condivisa. I dati scritti sono immediatamente visibili agli altri processi che accedono alla stessa area, a condizione che anch'essi abbiano mappato il segmento con `shmat()`.
4. **Sincronizzazione**: poiché più processi possono accedere contemporaneamente alla memoria, è necessario usare semafori%%link%%, mutex%%link%% o altri meccanismi di sincronizzazione. Questi impediscono che i processi modifichino la stessa area di memoria nello stesso momento, evitando condizioni di stallo o errori di dati incoerenti.
5. **Scollegamento dalla memoria**: quando un processo ha terminato l'uso della memoria condivisa, la "scollega" usando `shmdt()`. Tuttavia, la memoria non viene liberata fino a quando tutti i processi che vi sono connessi non si sono scollegati.
6. **Rimozione dell'area di memoria**: dopo lo scollegamento, il segmento di memoria condivisa può essere rimosso definitivamente con `shmctl()`, che libera la memoria.

### 3.2.1 - Esempio di codice in linguaggio C

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

## 3.3 - Vantaggi e svantaggi della memoria condivisa

I principali vantaggi della memoria condivisa sono:
- **Elevata velocità di comunicazione**: l'accesso diretto alla stessa area di memoria elimina la necessità di copiare dati tra processi, garantendo una comunicazione molto rapida. Questo è particolarmente utile in applicazioni ad alte prestazioni, come la grafica, il calcolo scientifico, o i sistemi di trading.
- **Efficienza per grandi quantità di dati**: la memoria condivisa è ideale per scambiare grandi volumi di dati tra processi, poiché riduce il consumo di memoria rispetto alla duplicazione dei dati. Tutti i processi accedono allo stesso blocco di dati, quindi è molto efficiente in termini di utilizzo della memoria.
- **Flessibilità nel formato dei dati**: a differenza di altri metodi di comunicazione tra processi (come le [code di messaggi](Comunicazione%20tra%20processi%20(IPC).md#2%20-%20Code%20di%20messaggi)), la memoria condivisa non impone un formato specifico dei dati, permettendo una grande flessibilità nella struttura dei dati da condividere.
- **Accesso simultaneo ai dati**: più processi possono accedere ai dati contemporaneamente, cosa che può ridurre il tempo di latenza in applicazioni real-time. Ciò è utile per operazioni di lettura parallela di dati comuni o aggiornamenti a bassa frequenza.

I principali svantaggi della memoria condivisa sono:
- **Necessità di sincronizzazione esplicita**: la memoria condivisa non include un meccanismo di sincronizzazione integrato. I processi devono coordinarsi manualmente per evitare condizioni di gara%%link%% o accessi incoerenti. Questo può complicare lo sviluppo e richiede l'uso di semafori%%link%% o mutex%%link%% per coordinare gli accessi.
- **Problemi di sicurezza e isolamento**: dal momento che la memoria condivisa è accessibile a più processi, un errore in uno di essi può influire su tutti gli altri. Il controllo degli accessi deve essere gestito correttamente per prevenire modifiche accidentali o non autorizzate, specialmente nei sistemi multiutente.
- **Debug complesso**: il debug della memoria condivisa è più complicato rispetto ad altri metodi di comunicazione tra processi, poiché le condizioni di gara%%link%% e i problemi di sincronizzazione possono essere difficili da rilevare. Gli errori di accesso concorrente possono portare a comportamenti non deterministici difficili da riprodurre.
- **Dipendenza dal sistema operativo**: l'implementazione della memoria condivisa varia tra sistemi operativi, quindi il codice potrebbe non essere portabile. Nei sistemi UNIX-like%%link%%, l'API POSIX%%link%% standardizza alcune chiamate di memoria condivisa, ma Windows%%link%% utilizza un set di API diverso (ad esempio `CreateFileMapping` e `MapViewOfFile`), creando complicazioni di portabilità.
- **Rimozione manuale della memoria**: la memoria condivisa non viene automaticamente rimossa se un processo termina senza scollegarla correttamente. Questo può portare a perdite di memoria (memory leak) nel sistema, rendendo necessaria la rimozione esplicita della memoria condivisa quando non è più utilizzata.

# 4 - Socket

I **socket** sono un meccanismo di comunicazione tra processi che consentono a due o più processi di comunicare tra loro sia all'interno dello stesso sistema sia su sistemi diversi tramite rete. Nella comunicazione tra processi, i socket più utilizzati sono quelli di [dominio UNIX](Comunicazione%20tra%20processi%20(IPC).md#4.1.2%20-%20Famiglie%20di%20socket) %%cambiare link poi quando farò sezione specifica per dominio UNiX%%e quelli di [dominio Internet (IPv4 o IPv6)](Comunicazione%20tra%20processi%20(IPC).md#4.3%20-%20Internet%20socket), e l'uso varia a seconda del tipo di applicazione e delle esigenze di comunicazione.

## 4.1 - Principali caratteristiche dei socket

Le principali caratteristiche dei socket sono:
- [**Half-duplex e full-duplex**](Comunicazione%20tra%20processi%20(IPC).md#4.1.1%20-%20Half-duplex%20e%20full-duplex): i socket possono supportare la comunicazione o monodirezionale ([half-duplex](Comunicazione%20tra%20processi%20(IPC).md#4.1.1.1%20-%20Half-duplex)) o bidirezionale ([full-duplex](Comunicazione%20tra%20processi%20(IPC).md#4.1.1.2%20-%20Full-duplex)), in cui i dati possono essere inviati e ricevuti simultaneamente o solo in una direzione alla volta.%%half-duplex non è monodirezionale in realtà%%
- [**Famiglia di socket**](Comunicazione%20tra%20processi%20(IPC).md#4.1.2%20-%20Famiglie%20di%20socket): è un raggruppamento di socket che utilizzano gli stessi protocolli sottostanti, supporta un sottoinsieme di stili di comunicazione e possiede un proprio formato di indirizzamento.
- [**Tipo di socket**](Comunicazione%20tra%20processi%20(IPC).md#4.1.3%20-%20Tipo%20di%20socket): definisce come i dati vengono trasmessi attraverso il socket e determina le modalità di comunicazione tra i dispositivi.
- [**Orientamento alla connessione**](Comunicazione%20tra%20processi%20(IPC).md#4.1.4%20-%20Orientamento%20alla%20connessione): il tipo di collegamento stabilito tra due dispositivi che comunicano in rete che si distingue tra [connection-oriented](Comunicazione%20tra%20processi%20(IPC).md#4.1.4.1%20-%20Connection-oriented%20(orientato%20alla%20connessione)) (in cui prima di iniziare la trasmissione dei dati, viene stabilita una connessione stabile e affidabile tra i dispositivi) e [connectionless](Comunicazione%20tra%20processi%20(IPC).md#4.1.4.2%20-%20Connectionless%20(senza%20connessione)) (in cui non è necessario stabilire una connessione continua prima di inviare i dati).
- **Bloccanti e non-bloccanti**: possono essere configurati per operare in modalità bloccante (attesa di una risposta prima di procedere) o non-bloccante (eseguono altre operazioni in attesa della risposta).%%sistemare questo punto%%

### 4.1.1 - Half-duplex e full-duplex

I dati nei socket possono essere trasferiti in due modalità:
- [**Half-duplex**](Comunicazione%20tra%20processi%20(IPC).md#4.1.1.1%20-%20Half-duplex): i dati possono essere trasmessi in entrambe le direzioni tra due dispositivi, ma non contemporaneamente.
- [**Full-duplex**](Comunicazione%20tra%20processi%20(IPC).md#4.1.1.2%20-%20Full-duplex): i dati possono essere trasmessi simultaneamente in entrambe le direzioni tra due dispositivi.

#### 4.1.1.1 - Half-duplex

Nella comunicazione **half-duplex**, i dati possono essere trasmessi in entrambe le direzioni tra due dispositivi, ma non contemporaneamente. Ciò significa che, in un dato momento, solo un dispositivo può inviare i dati mentre l'altro riceve.

Le principali caratteristiche delle comunicazioni half-duplex sono:
- **Comunicazione alternata**: se un dispositivo sta inviando, l'altro deve attendere prima di poter trasmettere.
- **Ritardo**: a causa della trasmissione alternata, possono verificarsi ritardi quando il controllo passa da un dispositivo all'altro.

Esempi di utilizzo delle comunicazioni half-duplex sono:
- **Walkie-talkie**: in un walkie-talkie, solo una persona alla volta può parlare mentre l'altra ascolta.
- **Reti wireless**: alcune reti Wi-Fi possono utilizzare modalità half-duplex per gestire il traffico.

#### 4.1.1.2 - Full-duplex

Nella comunicazione full-duplex, i dati possono essere trasmessi simultaneamente in entrambe le direzioni tra due dispositivi, permettendo così una comunicazione bidirezionale continua.

Le principali caratteristiche delle comunicazioni full-duplex sono:
- **Trasmissione simultanea**: entrambi i dispositivi possono inviare e ricevere dati contemporaneamente.
- **Maggiore efficienza**: riduce il ritardo poiché non è necessario alternare tra invio e ricezione.

Esempi di utilizzo delle comunicazioni full-duplex sono:
- **Telefonia**: durante una chiamata telefonica, entrambi gli interlocutori possono parlare e ascoltare simultaneamente.
- **Ethernet**: molti cavi Ethernet supportano la comunicazione full-duplex, migliorando la velocità di trasferimento dei dati.

#### 4.1.1.3 - Tabella riassuntiva delle differenze

Ecco una tabella riassuntiva che confronta la modalità [half-duplex](Comunicazione%20tra%20processi%20(IPC).md#4.1.1.1%20-%20Half-duplex) e la modalità [full-duplex](Comunicazione%20tra%20processi%20(IPC).md#4.1.1.2%20-%20Full-duplex):
%% controllare se la tabella nel rendering su Quartz ha i link in grassetto%%

| Caratteristica         | [Half-duplex](Comunicazione%20tra%20processi%20(IPC).md#4.1.1.1%20-%20Half-duplex) | [Full-duplex](Comunicazione%20tra%20processi%20(IPC).md#4.1.1.2%20-%20Full-duplex)   |
| ---------------------- | ---------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------ |
| **Direzione dei dati** | Bidirezionale, ma non simultanea (un solo dispositivo trasmette alla volta)              | Bidirezionale e simultanea (entrambi i dispositivi possono trasmettere contemporaneamente) |
| **Efficienza**         | Minore, per via dell'alternanza                                                          | Maggiore, grazie alla trasmissione simultanea                                              |
| **Ritardo**            | Potenziale ritardo dovuto all'attesa                                                     | Ridotto, poiché non c'è attesa                                                             |
| **Esempi**             | Walkie-talkie, alcune reti Wi-Fi                                                         | Telefonia, Ethernet                                                                        |

### 4.1.2 - Famiglie di socket

Le **famiglie di socket** sono i raggruppamenti in cui vengono divisi i vari tipi di socket in base al tipo di protocollo di rete e il metodo di indirizzamento utilizzato per la comunicazione. Le principali famiglie di socket sono:
- **UNIX domain socket (`AF_UNIX` o `AF_LOCAL`)**: permette la comunicazione tra processi sullo stesso sistema operativo e utilizza file di sistema come punto di connessione, infatti il nome del socket è identificato dal percorso del file%%link%% (`/<path>/<filename>`).
- **[Internet socket](Comunicazione%20tra%20processi%20(IPC).md#4.3%20-%20Internet%20socket) (`AF_INET` e `AF_INET6`)**: permette la comunicazione su reti IP%%link%%, sia locale che su Internet e usa indirizzi IP%%link%% (IPv4 e IPv6 rispettivamente per `AF_INET` e `AF_INET6`) e numeri di porta%%link%% per identificare i dispositivi, infatti il nome del socket è identificato dalla coppia indirizzo-porta (`<indirizzo IP>:<porta>`).
- **Bluetooth socket (`AF_BLUETOOTH`)**: viene utilizzato per la comunicazione su reti Bluetooth%%link%% e supporta connessioni wireless a corto raggio, ad esempio tra dispositivi mobili e periferiche. Per identificare i dispositivi, usa indirizzi MAC Bluetooth%%link%%, che sono identificatori unici per dispositivi Bluetooth (simili agli indirizzi MAC Ethernet%%link%%).
- **Packet socket (`AF_PACKET`)**: disponibile solo su Linux, permette l'accesso diretto ai pacchetti a livello di rete, senza passare per un protocollo specifico (come l'IP%%link%%). Usato per operazioni a basso livello come sniffing di rete e diagnostica.

### 4.1.3 - Tipo di socket

Il **tipo di socket** definisce come i dati vengono trasmessi attraverso il socket e determina le modalità di comunicazione tra i dispositivi. I principali tipi di socket sono:
- **`SOCK_STREAM`**: utilizza il TCP (Transmission Control Protocol)%%link%% e fornisce una connessione affidabile ([connection-oriented](Comunicazione%20tra%20processi%20(IPC).md#4.1.4.1%20-%20Connection-oriented%20(orientato%20alla%20connessione))), cioè i dati vengono trasmessi in modo sequenziale e senza errori, garantendo che arrivino nell'ordine giusto.
- **`SOCK_DGRAM`**: utilizza l'UDP (User Datagram Protocol)%%link%% e non richiede una connessione ([connectionless](Comunicazione%20tra%20processi%20(IPC).md#4.1.4.2%20-%20Connectionless%20(senza%20connessione))), cioè i pacchetti possono essere persi o arrivare in ordine diverso, poiché non ci sono garanzie di consegna.
- **`SOCK_RAW`**: permette l'accesso diretto ai pacchetti a livello di rete, senza passare per un protocollo specifico (come TCP%%link%% o UDP%%link%%). Viene utilizzato per operazioni a basso livello, come il monitoraggio del traffico di rete e l'analisi dei pacchetti.
- **`SOCK_SEQPACKET`**: fornisce una connessione orientata ai pacchetti, simile a `SOCK_STREAM` ma con messaggi di lunghezza fissa. Garantisce la consegna dei pacchetti e mantiene l'ordine.

### 4.1.4 - Orientamento alla connessione

L'**orientamento alla connessione** si riferisce al modo in cui le applicazioni comunicano tra loro attraverso una rete, specificando se una connessione deve essere stabilita e mantenuta prima del trasferimento dei dati. Questa modalità è particolarmente importante nel contesto dei socket e dei protocolli di comunicazione. Esistono due modalità di orientamento alla connessione: [connection-oriented](Comunicazione%20tra%20processi%20(IPC).md#4.1.4.1%20-%20Connection-oriented%20(orientato%20alla%20connessione)) e [connectionless](Comunicazione%20tra%20processi%20(IPC).md#4.1.4.2%20-%20Connectionless%20(senza%20connessione)).

#### 4.1.4.1 - Connection-oriented (orientato alla connessione)

In un sistema **connection-oriented (orientato alla connessione)**, è necessario stabilire una connessione affidabile tra due dispositivi (come client e server) prima che avvenga qualsiasi scambio di dati. Questo processo assicura che i dati vengano trasmessi in modo ordinato e senza perdite. Il protocollo più comune associato a questa modalità è il TCP (Transmission Control Protocol)%%link%% che garantisce che i pacchetti di dati arrivino nella sequenza corretta e senza errori.

Le principali caratteristiche dei sistemi connection-oriented sono:
- **Handshake iniziale**: prima di iniziare a inviare dati, il TCP%%link%% esegue un processo di handshake a tre vie per stabilire la connessione. Durante questo processo, il client e il server scambiano messaggi per confermare che sono pronti a comunicare.
- **Affidabilità**: il TCP%%link%% include meccanismi per garantire la consegna dei pacchetti, il controllo degli errori e la correzione degli errori. Se un pacchetto viene perso, il TCP si assicura che venga ritrasmesso.
- **Flusso di dati**: garantisce che i dati vengano inviati e ricevuti in un ordine preciso. Questa caratteristica è fondamentale per applicazioni come il trasferimento di file o le comunicazioni web, in cui la trasmissione dei dati in ordine casuale potrebbe creare problemi.

Esempi di utilizzo dei sistemi connection-oriented sono:
- **Web Browsing**: quando un browser si connette a un server web, stabilisce una connessione TCP%%link%% per garantire che tutte le informazioni vengano ricevute correttamente e nell'ordine giusto.
- **Email**: i protocolli come SMTP%%link%% (per inviare email) e POP3/IMAP%%link%% (per ricevere email) utilizzano connessioni TCP%%link%%.

#### 4.1.4.2 - Connectionless (senza connessione)

In un sistema **connectionless (senza connessione)**, i dati possono essere inviati senza stabilire una connessione permanente. Non è necessario alcun processo di handshake iniziale e i pacchetti possono viaggiare indipendentemente. Il protocollo più comune associato a questa modalità è l'UDP (User Datagram Protocol)%%link%% che non garantisce che i pacchetti vengano consegnati o che arrivino nell'ordine corretto.

Le principali caratteristiche dei sistemi connectionless sono:
- **Nessun handshake**: l'UDP%%link%% non richiede un processo di stabilimento della connessione, il che rende il trasferimento di dati più veloce.
- **Meno overhead**: non ci sono controlli di errore e riconoscimenti, il che riduce l'overhead e aumenta la velocità di trasmissione.
- **Inaffidabilità**: non c'è garanzia che i dati arrivino o che vengano ricevuti nell'ordine corretto. Questo può essere accettabile per alcune applicazioni, come streaming audio o video, dove la velocità è più importante della completezza.

Esempi di utilizzo dei sistemi connectionless sono:
- **Streaming**: i servizi di streaming video e audio utilizzano l'UDP%%link%% per trasmettere dati in tempo reale, dove è più importante ricevere i dati rapidamente piuttosto che garantirne l'integrità%%esempio dirette quando mancano qualche pixel o frame%%.
- **Giochi online**: molti giochi online usano l'UDP%%link%% per inviare rapidamente aggiornamenti di stato ai giocatori senza l'onere di garantire l'affidabilità.

#### 4.1.4.3 - Tabella riassuntiva delle differenze

Ecco una tabella riassuntiva che confronta la modalità [connection-oriented](Comunicazione%20tra%20processi%20(IPC).md#4.1.4.1%20-%20Connection-oriented%20(orientato%20alla%20connessione)) e la modalità [connectionless](Comunicazione%20tra%20processi%20(IPC).md#4.1.4.2%20-%20Connectionless%20(senza%20connessione)):

| Caratteristica                     | [Connection-oriented (orientato alla connessione)](Comunicazione%20tra%20processi%20(IPC).md#4.1.4.1%20-%20Connection-oriented%20(orientato%20alla%20connessione)) | [Connectionless (senza connessione)](Comunicazione%20tra%20processi%20(IPC).md#4.1.4.2%20-%20Connectionless%20(senza%20connessione)) |
| ---------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------ |
| **Protocollo comune**              | TCP (Transmission Control Protocol)%%link%%                                                                                                                              | UDP (User Datagram Protocol)%%link%%                                                                                                       |
| **Stabilimento della connessione** | Richiede un handshake iniziale a 3 vie                                                                                                                                   | Nessun handshake necessario                                                                                                                |
| **Affidabilità**                   | Garantita (controlla la consegna e l'ordine dei dati)                                                                                                                    | Non garantita (i dati possono andare persi o arrivare fuori ordine)                                                                        |
| **Overhead**                       | Maggiore (a causa di controlli di errore e ritrasmissione)                                                                                                               | Minore (poiché non ci sono controlli di errore)                                                                                            |
| **Velocità**                       | Più lenta (a causa dell'overhead e della gestione della connessione)                                                                                                     | Più veloce (grazie all'assenza di overhead)                                                                                                |
| **Esempi di utilizzo**             | Browsing web, email, trasferimento di file                                                                                                                               | Streaming video/audio, giochi online                                                                                                       |
| **Flusso di dati**                 | Ordinato (i dati vengono ricevuti nell'ordine corretto)                                                                                                                  | Non ordinato (i dati possono arrivare in ordine casuale)                                                                                   |
| **Gestione degli errori**          | Inclusa (ritrasmissione automatica in caso di errore)                                                                                                                    | Assente (l'applicazione deve gestire eventuali errori)                                                                                     |
| **Uso di risorse**                 | Maggiore uso di risorse di rete e CPU                                                                                                                                    | Minore uso di risorse, poiché non ci sono controlli                                                                                        |

## 4.2 - Vantaggi e svantaggi dei socket

I principali vantaggi dei socket sono:
- **Flessibilità**: permettono una varietà di protocolli di trasporto%%link%% (TCP%%link%%/UDP%%link%%) e [orientamento alla connessione](Comunicazione%20tra%20processi%20(IPC).md#4.1.4%20-%20Orientamento%20alla%20connessione) ([connection-oriented](Comunicazione%20tra%20processi%20(IPC).md#4.1.4.1%20-%20Connection-oriented%20(orientato%20alla%20connessione))/[connectionless](Comunicazione%20tra%20processi%20(IPC).md#4.1.4.2%20-%20Connectionless%20(senza%20connessione))), adattandosi a diverse esigenze di comunicazione.
- **Efficienza nella comunicazione**: offrono un metodo standard per lo scambio di dati tra dispositivi, consentendo connessioni rapide tra applicazioni su macchine differenti.
- **Compatibilità cross-platform**: le API dei socket sono disponibili e relativamente simili su molti sistemi operativi, facilitando lo sviluppo di applicazioni distribuite.
- **Affidabilità con il TCP**: con il TCP%%link%%, i socket garantiscono che i dati arrivino in modo sicuro, ordinato e senza perdite. È quindi ideale per applicazioni critiche come web server, trasferimento di file e posta elettronica.
- **Supporto alla comunicazione in tempo reale con l'UDP**: con l'UDP%%link%%, i socket permettono una comunicazione veloce, poiché non hanno overhead di connessione, rendendoli ideali per streaming, giochi online, e applicazioni dove la velocità è più importante della precisione.
- **Multithreading e scalabilità**: i socket possono essere gestiti in modo asincrono o su più [thread](Thread.md), permettendo a un singolo server di gestire più connessioni contemporaneamente, aumentando così la scalabilità dell'applicazione.

I principali svantaggi dei socket sono:
- **Complessità di gestione**: richiedono una gestione accurata dei processi di connessione e chiusura, con il rischio di problemi come il blocco dei socket, connessioni non terminate correttamente, o errori di timeout.
- **Overhead con il TCP**: le connessioni che usano il TCP%%link%% implicano un certo overhead per il controllo di errori e la garanzia di consegna, aumentando la latenza. Non è ideale per applicazioni che richiedono un trasferimento estremamente rapido di piccoli pacchetti di dati.
- **Limitata sicurezza intrinseca**: di per sé, i socket non offrono cifratura o autenticazione dei dati. Per garantire sicurezza, è necessario implementare soluzioni aggiuntive come TLS/SSL%%link%%.
- **Vulnerabilità a attacchi**: i socket sono esposti ad attacchi come DDoS (Distributed Denial of Service) e hijacking, in cui malintenzionati possono sfruttare le connessioni aperte.
- **Supporto limitato per la trasmissione multicast**: sebbene l'UDP%%link%% supporti il multicast, cioè l'invio di dati a più destinatari, i socket TCP%%link%% non lo fanno nativamente, limitando la comunicazione a un solo client per connessione.
- **Problemi di firewall e NAT**: i firewall e i router NAT possono bloccare o ostacolare la connessione dei socket, causando problemi di accesso e richiedendo configurazioni aggiuntive.

## 4.3 - Internet socket

Gli **Internet socket** sono una [famiglia di socket](Comunicazione%20tra%20processi%20(IPC).md#4.1.2%20-%20Famiglie%20di%20socket) utilizzati per la comunicazione su reti basate su IP, come Internet. Questi socket possono essere utilizzati per stabilire connessioni tra dispositivi che si trovano anche in posizioni geografiche diverse.

Gli internet socket hanno le seguenti principali caratteristiche:
- **Indirizzamento**: ogni socket è identificato univocamente da un indirizzo IP%%link%% e da una porta%%link%%, che consentono ai dispositivi di indirizzare correttamente i dati.
- **Protocollo**: i socket utilizzano protocolli di trasporto che determinano come vengono trasferiti i dati. I due protocolli più usati sono il TCP (Transmission Control Protocol)%%link%%, che crea una connessione stabile e affidabile e garantisce la consegna dei dati in modo ordinato e senza perdite, e l'UDP (User Datagram Protocol)%%link%%, che crea una connessione più leggera e veloce, ma non garantisce affidabilità, sequenzialità o controllo della perdita di pacchetti.

### 4.3.1 - Funzionamento degli internet socket

Il funzionamento base di un socket è il seguente:
1. **Creazione di un socket**: un'applicazione crea un socket, specificando il tipo di protocollo%%link%% (come TCP%%link%% o UDP%%link%%) e altre opzioni (ad esempio, indirizzo IP%%link%% e porta%%link%%). Nei sistemi basati su UNIX, questo avviene tipicamente con la funzione `socket()`, che restituisce un identificatore%%ID?%% del socket.
2. **Associazione (binding)**: nel caso di un server, il socket viene "associato" a un indirizzo IP%%link%% e una porta%%link%% con l'operazione di binding. Questo assicura che il socket ascolti su uno specifico indirizzo e sia accessibile per le connessioni in entrata. Ad esempio, in un server web, il socket è spesso associato alla porta 80 (HTTP%%link%%) o 443 (HTTPS%%link%%). %%Perché proprio questi due numeri specifici di porta?%%
3. **Modalità d'ascolto e connessione**: server e client svolgono funzioni diverse.
	- **Server**: il socket entra in modalità d'ascolto con la funzione `listen()`, in attesa di connessioni in entrata. Quando un client tenta di connettersi, il server accetta la connessione con la funzione `accept()`, che restituisce un nuovo socket per gestire la comunicazione con il client.
	- **Client**: il client richiede una connessione con il server attraverso il socket e la funzione `connect()`, specificando l'indirizzo IP%%link%% e la porta%%link%% del server.
4. **Trasferimento dei dati**: una volta stabilita la connessione, il client e il server possono scambiarsi dati. I dati sono inviati e ricevuti (in pacchetti) tramite funzioni di lettura e scrittura, come `send()` e `recv()` in TCP%%link%%, che garantiscono la consegna, oppure `sendto()` e `recvfrom()` in UDP%%link%%, dove non è garantita.
5. **Chiusura della connessione**: al termine della comunicazione, il socket viene chiuso. Nel TCP%%link%%, entrambe le parti devono chiudere il socket per terminare la connessione (half-close), garantendo che non ci siano dati persi. Nell'UDP%%link%%, che è senza connessione, la chiusura non ha bisogno di un processo specifico.

# 5 - Chiamate di procedure remote (RPC)

Le **chiamate di procedure remote** (RPC, Remote Procedure Calls) sono un meccanismo di comunicazione tra processi che consente a un programma di eseguire una procedura (funzione o subroutine) in un altro indirizzo di rete, come se fosse una funzione locale. Questo tipo di comunicazione è usato frequentemente in sistemi distribuiti per facilitare l'interazione tra componenti che risiedono su macchine diverse.

## 5.1 - Principali caratteristiche delle RPC

Le principali caratteristiche delle RPC sono:
- **Trasparenza della rete**: le RPC nascondono i dettagli di rete, permettendo agli sviluppatori di chiamare funzioni remote come funzioni locali, semplificando il codice e la logica applicativa. La comunicazione tra client e server avviene senza che il chiamante debba preoccuparsi di dettagli come indirizzi IP%%link%%, porte%%link%% o protocolli%%link%%.
- **Indipendenza dalla piattaforma e dal linguaggio**: molti sistemi di RPC sono progettati per essere indipendenti dal linguaggio di programmazione e dalla piattaforma, consentendo la comunicazione tra componenti eterogenei (ad esempio, un'app Java su Linux può chiamare una procedura C# su Windows).
- **Modello client-server**: le RPC si basano su un'architettura client-server, in cui il client richiede l'esecuzione della procedura e il server la esegue e restituisce il risultato.
- **Gestione degli errori e delle condizioni di guasto**: in un ambiente di rete, possono verificarsi guasti come timeout, interruzioni di connessione o server non raggiungibili, quindi le RPC devono implementare meccanismi per gestire questi errori, come ritentativi automatici, gestione delle eccezioni e timeout configurabili.
- **Sicurezza**: le RPC spesso includono meccanismi di autenticazione, autorizzazione e crittografia per proteggere la comunicazione tra client e server e garantire che solo gli utenti autorizzati possano accedere ai servizi.
- **Efficienza**: le RPC devono essere efficienti e leggere per poter supportare una vasta gamma di applicazioni distribuite.
- **Asincronia e synchronous calls**: sebbene le RPC tradizionali siano sincrone (il client attende la risposta dal server), alcune implementazioni supportano anche chiamate asincrone per evitare il blocco del client. Le chiamate asincrone sono particolarmente utili in applicazioni ad alte prestazioni e in ambienti distribuiti complessi.

## 5.2 - Funzionamento delle RPC

Il **funzionamento delle RPC** si basa su un meccanismo che permette a un programma di richiedere l'esecuzione di una funzione su un sistema remoto, come se fosse una normale chiamata a una funzione locale.

Ecco i principali passaggi e i componenti chiave di questo processo:
1. **Chiamata del client**: con un programma client che desidera utilizzare una funzione specifica disponibile su un server remoto, il client non deve preoccuparsi di come inviare la richiesta al server; al contrario, invoca semplicemente la funzione come se fosse una funzione locale.
2. **Stub del client**: quando il client invoca la funzione, questa chiamata non parte direttamente verso il server. Invece, viene intercettata da un componente chiamato _stub del client_: esso agisce come un "proxy" per la funzione remota, preparandosi a inviare la richiesta al server.
3. **Marshalling dello stub**: per inviare la richiesta al server, lo stub raccoglie i dati necessari (i parametri della funzione) e li serializza in un formato standard compatibile con la trasmissione su rete: questo processo è chiamato _marshalling_ e assicura che i dati possano essere compresi dall'altro lato della comunicazione, indipendentemente dal sistema operativo o dal linguaggio di programmazione.
4. **Invio della richiesta alla rete**: dopo aver effettuato il marshalling, lo stub del client invia i dati attraverso la rete verso il server. In questa fase, il sistema di comunicazione di rete (tipicamente utilizzando il protocollo TCP/IP%%link%%) si occupa di consegnare i dati al server remoto.
5. **Skeleton del server**: sul lato del server, un componente chiamato _skeleton_ riceve la richiesta. Questo skeleton è, in un certo senso, il "gemello" dello stub, e ha il compito di agire come rappresentante della funzione remota. Una volta ricevuta la richiesta, lo skeleton esegue il processo inverso al marshalling, chiamato _demarshalling_, col quale i dati vengono deserializzati e convertiti in un formato che può essere interpretato e utilizzato dal server.
6. **Esecuzione della funzione remota**: una volta completato il demarshalling, lo skeleton chiama la funzione effettiva sul server (la stessa invocata dal client) e passa i parametri originali. La funzione viene quindi eseguita localmente sul server e produce un risultato.
7. **Restituzione del risultato**: il risultato ottenuto dall'esecuzione della funzione viene quindi restituito dallo skeleton, che si occupa di trasformarlo di nuovo in un formato standard, facendo il marshalling del risultato per prepararlo alla trasmissione. I dati vengono inviati indietro attraverso la rete, tornando verso lo stub del client.
8. **Riconversione e risultato finale**: quando i dati tornano al client, lo stub del client esegue di nuovo il demarshalling per trasformare i dati ricevuti in un formato comprensibile dall'applicazione client. Infine, lo stub restituisce il risultato al client, che lo riceve come se fosse stato prodotto da una funzione locale.

## 5.3 - Vantaggi e svantaggi delle RPC

I principali vantaggi delle RPC sono:
- **Trasparenza della rete**: le RPC nascondono i dettagli di rete, permettendo agli sviluppatori di invocare funzioni remote con una sintassi simile a quella locale. Questo riduce la complessità e facilita lo sviluppo di applicazioni distribuite.
- **Astrazione della comunicazione**: il client non deve preoccuparsi di gestire le connessioni di rete, il formato dei dati o i protocolli di comunicazione. Lo stub e lo skeleton si occupano di tutti i dettagli tecnici, semplificando il codice applicativo.
- **Riusabilità e modularità**: con le RPC, le funzioni server possono essere utilizzate da diverse applicazioni e client. Questo migliora la modularità, rendendo i componenti del sistema più riutilizzabili e facilitando lo sviluppo di architetture distribuite.
- **Indipendenza dalla piattaforma e dal linguaggio**: alcune implementazioni RPC, come gRPC%%link%%, permettono di creare servizi compatibili tra diversi linguaggi di programmazione e sistemi operativi, rendendo le RPC adatte a progetti complessi ed eterogenei.
- **Supporto per sistemi distribuiti**: le RPC sono progettate per sistemi distribuiti e favoriscono una struttura client-server, spesso essenziale per applicazioni come microservizi, in cui diversi componenti comunicano tra loro in rete.

I principali svantaggi delle RPC sono:
- **Dipendenza dalla rete**: la performance delle RPC dipende fortemente dalla rete, in quanto eventuali problemi di connessione, come latenza o instabilità, possono rallentare le chiamate o provocare errori, riducendo l'affidabilità del sistema.
- **Gestione complessa degli errori**: gestire errori di rete, timeout, o guasti dei server può essere difficile. Le RPC devono implementare meccanismi di gestione dei guasti, ma questi aggiungono complessità al sistema e richiedono un'accurata gestione degli errori.
- **Overhead di marshalling e demarshalling**: il processo di serializzazione e deserializzazione dei dati per adattarli al formato di rete introduce un overhead. In scenari ad alte prestazioni, questo può essere un collo di bottiglia.
- **Limiti sui tipi di dati complessi**: il marshalling di dati complessi (come oggetti, strutture nidificate o referenze) può essere difficile e non sempre supportato, a meno di utilizzare strumenti avanzati di serializzazione, che però aumentano la complessità.
- **Sicurezza e autenticazione**: poiché i dati viaggiano sulla rete, le RPC devono spesso implementare meccanismi di autenticazione, autorizzazione e crittografia, aggiungendo ulteriore complessità e possibili punti deboli alla sicurezza.
- **Costi di nanutenzione e debug**: diagnosticare e risolvere i problemi in un sistema distribuito è più difficile rispetto a un'applicazione locale. Tracciamento e monitoraggio diventano essenziali, ma introducono un ulteriore livello di complessità e richiedono strumenti dedicati.

%%

\### 5. **Segnali (Signals)**
   - I **segnali** sono un metodo per inviare notifiche asincrone a un processo. Un processo può ricevere segnali che indicano la necessità di eseguire qualche azione (es. terminazione, interruzione).
   - Esempi: `kill()`, `signal()`.

\### 6. **Semafori (Semaphores)**
   - I **semafori** sono variabili che vengono utilizzate per gestire l'accesso concorrente alle risorse condivise, come la memoria condivisa. Aiutano a evitare situazioni come il **race condition**.
   - Esempi: `semget()`, `semop()`.

\### 7. **File temporanei**
   - I **file temporanei** possono essere usati per lo scambio di dati tra processi. I dati vengono scritti su file e letti da altri processi.

\### 9. **Database e Sistemi di File**
   - Un processo può scrivere dati in un database o file, e un altro processo può leggerli. Questo metodo è meno efficiente rispetto ad altri, ma può essere utile per la persistenza e condivisione di grandi quantità di dati.
%%

%%
\### 6. **Coordinamento e sincronizzazione tra processi**
   Nei sistemi con **processi concorrenti**, è necessario coordinare l'esecuzione di più processi per evitare problemi come **race conditions** (condizioni di corsa) o **deadlock** (stallo). Le operazioni per la sincronizzazione includono:

   - **Mutua esclusione**: Garantisce che un solo processo possa accedere a una risorsa condivisa alla volta (utilizzando semafori o mutex).
   - **Semafori**: I **semafori** sono variabili utilizzate per controllare l'accesso a risorse condivise, permettendo ai processi di attendere in modo sicuro l'accesso a una risorsa.
   - **Monitor**: I **monitor** sono costrutti di alto livello per gestire la mutua esclusione e la sincronizzazione dei processi.

\### 7. **Forking e clonazione di processi**
   Alcuni sistemi operativi (come Unix/Linux) permettono a un processo di creare una **copia di se stesso** tramite l'operazione di **fork**. Il processo figlio risultante è una replica del processo padre, con la stessa memoria, ma con un diverso **PID**.

\### 8. **Gestione dei segnali (Signals)**
   I processi possono inviare e ricevere **segnali**, che sono notifiche asincrone inviate dal sistema operativo o da altri processi per segnalare eventi come errori, richieste di terminazione o altri eventi specifici. Ad esempio, in Unix/Linux, il comando **kill** invia segnali a un processo (ad esempio, **SIGTERM** per richiedere la terminazione del processo).

\### 9. **Esecuzione di processi in foreground e background**
   Nei sistemi multiutente, è possibile eseguire un processo in **foreground** (in primo piano) o in **background** (sullo sfondo). Un processo in background può continuare a essere eseguito mentre l'utente esegue altre attività.

%%

