---
icon: BoBxNotification
iconColor: "#88FF88"
---
%%
- specificare che le funzioni sono chiamate di sistema
- controllare i valori specificati da errno quando le chiamate di sistema falliscono
- comandi da terminale per gestire i processi, oltre alle chiamate di sistema (es. `kill()` funzione e `kill` comando da terminale)
- per i parametri delle funzioni, scegliere se mettere "`pid`: indica il PID del processo" o "`pid`: PID del processo"
%%

Nei sistemi [UNIX](UNIX.md), i **segnali** sono un meccanismo di [comunicazione tra processi](Processi.md#7%20-%20Comunicazione%20tra%20processi%20(IPC)) utilizzato per notificare a un processo l'occorrenza di un evento specifico, come un errore, un'interruzione dell'utente o un'operazione speciale.

%%

- SIGTERM. Segnale standard utilizzato per terminare un processo; segnale inviato di default dai comandi kill e killall. Gli utenti a volte inviano esplicitamente il segnale SIGKILL a un processo, usando `kill –KILL` or `kill –9`.
	- In generale, questo è un errore. Un'applicazione ben progettata deve avere un handler per SIGTERM che consenta una 'graceful' exit, che consenta di pulire i file temporanei e di rilasciare le altre risorse. L'uccisione di un processo con SIGKILL bypassa l'handler di SIGTERM, e quindi si dovrebbe sempre prima cercare di terminare un processo con SIGTERM, e tenere SIGKILL come ultima scelta per terminare i processi che non rispondono a SIGTERM.
%%

# 1 - Nomi simbolici dei segnali

Ogni segnale è associato univocamente a:
- Un **intero**, a partire dall'`1`.
- Un **nome simbolico**, della forma `SIG***`.

Poiché gli effettivi interi assegnati a ogni segnale variano a seconda delle implementazioni nei vari [sistemi operativi](Sistema%20operativo.md), all'interno dei programmi è meglio utilizzare direttamente i nomi simbolici.

> [!consiglio] Consiglio
> È possibile verificare la numerazione dei segnali nel proprio sistema operativo eseguendo il comando:
> ```shell
> kill -l
> ```

# 2 - Tipi di segnali in UNIX

I **segnali in [UNIX](UNIX.md)** si dividono nelle seguenti categorie:
- **Trap**: segnali generati da un processo e inviati al processo stesso.
- **Interrupt**: segnali generati da un agente esterno (es. utente, altro processo) a un processo.
%%siamo sicuri sia questa la definizione di trap e interrupt?%%

## 2.1 - Trap

In [UNIX](UNIX.md), le **trap** sono segnali generati da eventi prodotti da un processo e inviati al processo stesso. Alcune trap sono causate da comportamenti errati del processo stesso, e immediatamente inviate al processo che normalmente reagisce terminando.

Sono esempi di trap i tentativi di divisione per zero (`SIGFPE`), indirizzamento errato degli array (`SIGSEGV`), tentativo di eseguire istruzioni privilegiate (`SIGILL`), ecc.

## 2.2 - Interrupt

In [UNIX](UNIX.md), gli **interrupt** sono segnali inviati ad un processo da un agente esterno (come l'utente o un altro processo).

Esempi di interrupt inviati dall'utente sono la pressione delle combinazione di tasti `Ctrl + C` (`SIGINT`) o `Ctrl + Z` (`SIGSTOP`) durante l'esecuzione di un processo, mentre un interrupt inviato da un altro processo può essere la system call `kill()`%%link%%.

# 3 - Ciclo di vita dei segnali in UNIX

In [UNIX](UNIX.md), i segnali hanno il seguente ciclo di vita:

```mermaid
graph LR
    A[Generazione] --> B[Blocco] --> C[Consegna] --> D[Gestione] --> E[Conclusione]
    B --> B

```

1. [**Generazione del segnale**](Segnali%20in%20UNIX.md#4%20-%20Generazione%20di%20un%20segnale): il segnale viene creato come risultato di un evento specifico e viene posto in una  associata al processo destinatario.
2. [**Blocco del segnale**](Segnali%20in%20UNIX.md#5%20-%20Blocco%20del%20segnale): dopo la sua generazione, si può impedire temporaneamente che un segnale venga consegnato a un processo. Invece di essere immediatamente gestito, il segnale rimane in uno stato di pendenza finché non viene sbloccato.
3. **Consegna del segnale**: quando il processo destinatario è attivo, il kernel controlla se ci sono segnali pendenti per quel processo. Se il segnale non è bloccato, allora viene recapitato, altrimenti rimane in stato pendente fino a quando non può essere gestito. Alcuni segnali, come `SIGKILL`, vengono consegnati immediatamente e non possono essere bloccati o ignorati.
4. [**Gestione del segnale**](Segnali%20in%20UNIX.md#7%20-%20Gestione%20del%20segnale): una volta consegnato, il segnale viene gestito dal processo a cui è stato recapitato. 
5. **Conclusione del segnale**: una volta gestito, il segnale esce dalla [coda dei segnali pendenti](Segnali%20in%20UNIX.md#6%20-%20Coda%20dei%20segnali%20pendenti). Se il segnale ha attivato un'azione (ad esempio, la terminazione del processo), il ciclo di vita del segnale termina con l'esecuzione dell'azione predefinita o personalizzata.

# 4 - Generazione di un segnale

Durante la **generazione del segnale**, il segnale viene creato come risultato di un evento specifico e  viene posto in una [coda dei segnali pendenti](Segnali%20in%20UNIX.md#6%20-%20Coda%20dei%20segnali%20pendenti) associata al processo destinatario.

## 4.1 - Fonti di generazione di un segnale

La **generazione di un segnale** può essere causato da diversi eventi o sorgenti:
- **Evento hardware**: l'hardware ha verificato una condizione di errore che è stata notificata al kernel%%link%%, il quale a propria volta ha inviato un segnale corrispondente al processo in questione. Per esempio, l'esecuzione di istruzioni di linguaggio macchina malformate (`SIGILL`), divisioni per $0$ (`SIGFPE`), o riferimenti a parti di memoria inaccessibili (`SIGSEGV`).
- [**Evento software**](Segnali%20in%20UNIX.md#4.2%20-%20Generazione%20di%20un%20segnale%20tramite%20eventi%20software): eventi che non derivano direttamente dall'hardware ma sono causati da azioni compiute da processi, dal kernel o da altre operazioni software. Per esempio, l'input è divenuto disponibile su un descrittore di file (`SIGIO`), un timer è arrivato a $0$ (`SIGALRM`), il tempo di processore per il processo è stato superato (`SIGXCPU`) o un figlio del processo è terminato (`SIGCHLD`).
- **Azione dell'utente**: l'utente ha digitato sul terminale combinazioni di tasti che generano i segnali, per esempio `Ctrl + C` (`SIGINT`) o `Ctrl + Z` (`SIGTSTP`).

## 4.2 - Generazione di un segnale tramite eventi software

La **generazione di un segnale tramite eventi software** avviene tramite azioni compiute da processi, dal kernel o da altre operazioni software. In particolare, si può ottenere usando le seguenti chiamate di sistema%%link%%:
- [**`kill()`**](Segnali%20in%20UNIX.md#4.2.1%20-%20Invio%20di%20un%20segnale%20tramite%20`kill()`): invia un segnale a un processo o a un gruppo di processi.
- [**`raise()`**](Segnali%20in%20UNIX.md#4.2.2%20-%20Invio%20di%20un%20segnale%20allo%20stesso%20processo%20chiamante%20tramite%20`raise()`): invia un segnale allo stesso processo chiamante.
- [**`alarm()`**](Segnali%20in%20UNIX.md#4.2.3%20-%20Impostazione%20di%20un%20timer%20di%20sistema%20con%20`alarm()`): imposta un timer di sistema al termine del quale invia il segnale `SIGALRM`.

### 4.2.1 - Invio di un segnale tramite `kill()`

La **funzione `kill()`** è una chiamata di sistema%%link%% utilizzata per inviare segnali a un processo o gruppo di processi.

Il suo prototipo è il seguente:

```c
#include <signal.h>

int kill(pid_t pid, int sig);
```

con:
- **`pid`**: processo o gruppo di processi a cui inviare il segnale, in particolare:
    - **`pid > 0`**: invia il segnale al processo specifico con ID `pid`.
    - **`pid == 0`**: invia il segnale a tutti i processi nel gruppo di processi del chiamante.
    - **`pid < 0`**: invia il segnale a tutti i processi nel gruppo di processi specificato dal valore assoluto `pid` (cioè `-pid`).
    - **`pid == -1` (detto _broadcast signal_)**: invia il segnale a tutti i processi che l'utente può controllare (tranne i processi di sistema%%esempi?%% e il processo chiamante stesso).
- **`sig`**: segnale da inviare.
- **`int` restituito**: può assumere i seguenti valori:
	- **`0`**: la funzione ha eseguito correttamente l'operazione.
	- **`-1`**: c'è stato un errore durante l'esecuzione della funzione ed `errno`%%link%% viene impostato%%con che valori?%%.

%%
Se nessun processo corrisponde al pid predefinito, `kill()` fallisce e setta `errno` a `ESRCH` (“No such process”). Se il processo esiste, ma non si hanno i permessi per inviare un segnale, allora `errno = EPERM`.
Verifica dell'esistenza di un processo. Se l'argomento sig è settato a 0 (detto null signal), non è inviato alcun segnale. In questo caso kill() esegue unicamente un controllo degli errori per vedere se è possibile inviare segnali al processo: il null signal può essere utilizzato per testare se un processo con un certo pid esiste. Se la chiamata va a buon fine, sappiamo che il processo esiste.
%%

> [!attenzione] Attenzione!
> La funzione `kill()` **non termina necessariamente** un processo, ma semplicemente invia un segnale che attiverà l'azione predefinita o, se possibile e se specificato, il relativo signal handler.

%%
## Inviare un segnale da linea di comando

Si usa il comando kill
```
kill –INT <PID>
kill –SIGINT <PID>
kill -2 <PID>
```
Se il segnale non è specificato, allora viene inviato il segnale SIGTERM

Evitate di provare a eseguire….
```
sudo kill -9 -1
```
%%

### 4.2.2 - Invio di un segnale allo stesso processo chiamante tramite `raise()`

La **funzione `raise()`** è una chiamata di sistema%%link%% utilizzata per inviare un segnale allo stesso processo chiamante. È una forma semplificata per generare segnali all'interno di un programma, senza dover usare [`kill()`](Segnali%20in%20UNIX.md#4.2.1%20-%20Invio%20di%20un%20segnale%20tramite%20`kill()`) o identificare esplicitamente il processo.

Il suo prototipo è il seguente:

```c
#include <signal.h>

int raise(int sig);
```

con:
- **`sig`**: segnale da inviare.
- **`int` restituito**:
	- **`0`**: la funzione ha eseguito correttamente l'operazione.
	- **`-1`**: c'è stato un errore durante l'esecuzione della funzione ed `errno`%%link%% viene impostato%%con che valori?%%.

### 4.2.3 - Impostazione di un timer di sistema con `alarm()`

La **funzione `alarm()`** è una chiamata di sistema%%link%% usata per impostare un timer di sistema al termine del quale viene inviato il segnale `SIGALRM`. È utile per gestire eventi basati sul tempo, come timeout per operazioni o esecuzioni periodiche.

Il suo prototipo è il seguente:

```c
#include <unistd.h>

unsigned int alarm(unsigned int seconds);
```

con:
- **`seconds`**: numero di secondi dopo il quale il segnale `SIGALRM` sarà inviato. Se `seconds` viene impostato a `0`, l'allarme già esistente (se presente) viene annullato.
- **`unsigned int` restituito**: numero di secondi rimanenti del precedente timer impostato, se esisteva. Altrimenti, restituisce `0` se non era impostato alcun timer.

## 4.3 - Segnali `SIGUSR1` e `SIGUSR2`

I segnali `SIGUSR1` e `SIGUSR2` sono segnali definiti dall'utente. Sono segnali generici che non hanno un'azione predefinita specifica (a parte la terminazione del processo, se non gestiti) e vengono solitamente utilizzati per notifiche o comunicazioni personalizzate tra processi.

I numeri assegnati a `SIGUSR1` e `SIGUSR2` possono variare tra i sistemi, ma tipicamente sono rispettivamente `10` e `12`.

### 4.3.1 - Uso tipico

- **Notifiche personalizzate**: segnalare eventi specifici tra processi.
- [**Comunicazione tra processi (IPC)**](Processi.md#7%20-%20Comunicazione%20tra%20processi%20(IPC)): permettere ai [processi](Processi.md) di scambiarsi informazioni senza passare per meccanismi complessi come [pipe](Pipe.md) o [socket](Socket.md).
- **Debugging**: utilizzati per notificare lo stato interno di un'applicazione durante il debug.

# 5 - Blocco del segnale

Il **blocco di un segnale** è una tecnica usata per impedire temporaneamente che un segnale venga consegnato a un processo, memorizzandolo all'interno della [coda dei segnali pendenti](Segnali%20in%20UNIX.md#6%20-%20Coda%20dei%20segnali%20pendenti).

## 5.1 - Uso tipico

- **Protezione delle sezioni critiche**: durante l'esecuzione di una sezione di codice critico, un segnale può causare interruzioni indesiderate che portano a comportamenti errati, come la generazione di dati incoerenti, la corruzione di strutture dati condivise od operazioni incomplete. Bloccando i segnali, si garantisce che il codice critico venga eseguito senza interferenze.
- **Coordinamento in applicazioni multithreading**%%link per "multithreading"%%: in programmi multithreading, è importante evitare che più thread gestiscano lo stesso segnale contemporaneamente. Bloccando i segnali, si può sincronizzare la gestione a livello di thread o di processo.
- **Posticipare la gestione di segnali non prioritari**: un segnale potrebbe essere generato in un momento inopportuno, ad esempio mentre il processo sta elaborando un'altra richiesta importante. Bloccarlo consente di gestirlo successivamente, quando il processo è pronto.
- **Debug e testing**: durante il debugging o il testing di applicazioni, è utile bloccare alcuni segnali per evitare che interferiscano con l'esecuzione o per analizzare il loro comportamento una volta sbloccati.

## 5.2 - Maschera dei segnali

La **maschera dei segnali** è un meccanismo che consente di specificare quali segnali un [processo](Processi.md) desidera bloccare temporaneamente. È una struttura cruciale per la gestione dei segnali, utilizzata per impedire che determinati segnali vengano consegnati al processo finché la maschera non viene modificata.

Viene rappresentata da un oggetto di tipo `sigset_t`, che è una struttura dati per definire un set di segnali. Quando un segnale è "mascherato" (cioè bloccato), non viene consegnato immediatamente al processo, ma viene messo nella [coda dei segnali pendenti](Segnali%20in%20UNIX.md#6%20-%20Coda%20dei%20segnali%20pendenti).

Le funzioni tipicamente usate per gestire una maschera dei segnali sono:
- [**`sigemptyset()`**](Segnali%20in%20UNIX.md#5.2.1%20-%20Inizializzazione%20di%20una%20maschera%20vuota%20con%20`sigemptyset()`): inizializza una nuova maschera vuota.
- [**`sigfillset()`**](Segnali%20in%20UNIX.md#5.2.2%20-%20Inizializzazione%20di%20una%20maschera%20piena%20con%20`sigfillset()`): inizializza una maschera contenente tutti i segnali dichiarati dal sistema.
- [**`sigismember()`**](Segnali%20in%20UNIX.md#5.2.3%20-%20Verifica%20di%20un%20segnale%20nella%20maschera%20con%20`sigismember()`): verifica se un determinato segnale è presente nella maschera.
- [**`sigaddset()`**](Segnali%20in%20UNIX.md#5.2.4%20-%20Aggiunta%20di%20un%20segnale%20con%20`sigaddset()`): aggiunge un determinato segnale alla maschera.
- [**`sigdelset()`**](Segnali%20in%20UNIX.md#5.2.5%20-%20Rimozione%20di%20un%20segnale%20con%20`sigdelset()`): rimuove un determinato segnale dalla maschera.
- [**`sigprocmask()`**](Segnali%20in%20UNIX.md#5.2.6%20-%20Applicazione%20di%20una%20maschera%20al%20processo%20con%20`sigprocmask()`): associa una maschera a un determinato processo.

### 5.2.1 - Inizializzazione di una maschera vuota con `sigemptyset()`

La **funzione `sigemptyset()`** permette di inizializzare una maschera vuota, rappresentata da un set di segnali. È spesso usata come primo passo per configurare una maschera di segnali o per costruire un set di segnali specifici.

Il suo prototipo è il seguente:

```c
#include <signal.h>

int sigemptyset(sigset_t *set);
```

con:
- **`set`**: puntatore a una variabile di tipo `sigset_t` (struttura dati che rappresenta un insieme di segnali). Questa variabile viene inizializzata come vuota dalla funzione.
- **`int` restituito**:
	- **`0`**: la funzione ha eseguito correttamente l'operazione.
	- **`-1`**: c'è stato un errore durante l'esecuzione della funzione ed `errno`%%link%% viene impostato%%con che valori?%% (anche se nella pratica questa funzione non fallisce mai).

> [!esempio]
> 
> ```c
> #include <stdio.h>
> #include <signal.h>
> 
> int main() {
>     sigset_t set;
> 
>     // Inizializzazione del set vuoto
>     if (sigemptyset(&set) == -1) {
>         perror("Errore nell'inizializzazione del set");
>         return 1;
>     }
> 
> 	// Uso della maschera
> 
>     return 0;
> }
> ```

### 5.2.2 - Inizializzazione di una maschera piena con `sigfillset()`

La **funzione `sigfillset()`** permette di inizializzare una maschera contenente tutti i segnali definiti dal sistema. È l'opposto di [`sigemptyset()`](Segnali%20in%20UNIX.md#5.2.1%20-%20Inizializzazione%20di%20una%20maschera%20vuota%20con%20`sigemptyset()`), che invece crea un set vuoto.

Il suo prototipo è il seguente:

```c
#include <signal.h>

int sigfillset(sigset_t *set);
```

con:
- **`set`**: puntatore a una variabile di tipo `sigset_t` (struttura dati che rappresenta un insieme di segnali). La funzione riempie questa struttura con tutti i segnali supportati dal sistema.
- **`int` restituito**:
	- **`0`**: la funzione ha eseguito correttamente l'operazione.
	- **`-1`**: c'è stato un errore durante l'esecuzione della funzione ed `errno`%%link%% viene impostato%%con che valori?%% (anche se nella pratica questa funzione non fallisce mai).

> [!esempio]
> 
> ```c
> #include <stdio.h>
> #include <signal.h>
> 
> int main() {
>     sigset_t set;
> 
>     // Inizializzazione del set con tutti i segnali
>     if (sigfillset(&set) == -1) {
>         perror("Errore nell'inizializzazione del set");
>         return 1;
>     }
> 
> 	// Uso della maschera
> 
>     return 0;
> }
> ```

### 5.2.3 - Verifica di un segnale nella maschera con `sigismember()`

La **funzione `sigismember()`** verifica se un segnale specifico è presente in un set di segnali (di tipo `sigset_t`). È comunemente utilizzata per controllare la composizione di un set prima di applicare una maschera di segnali o eseguire altre operazioni.

Il suo prototipo è il seguente:

```c
#include <signal.h>

int sigismember(const sigset_t *set, int signum);
```

con:
- **`set`**: puntatore a un oggetto di tipo `sigset_t` che rappresenta un set di segnali.
- **`signum`**: intero che rappresenta il numero del segnale da aggiungere al set (es. `SIGINT`, `SIGTERM`).
- **`int` restituito**:
	- **`1`**: il segnale è presente nel set.
	- **`0`**: il segnale non è presente nel set.
	- **`-1`**: c'è stato un errore durante l'esecuzione della funzione ed `errno`%%link%% viene impostato con codice di errore `EINVAL`%%link%% (che indica un argomento non valido).

> [!esempio]
> 
> ```c
> #include <stdio.h>
> #include <signal.h>
> 
> int main() {
>     sigset_t set;
> 
>     // Inizializzazione di un set vuoto
>     if (sigemptyset(&set) == -1) {
>         perror("Errore nell'inizializzazione del set");
>         return 1;
>     }
> 
>     // Aggiunta di SIGINT al set
>     if (sigaddset(&set, SIGINT) == -1) {
>         perror("Errore nell'aggiunta di SIGINT");
>         return 1;
>     }
> 
>     // Verifica di SIGINT nel set
>     if (sigismember(&set, SIGINT)) {
>         printf("SIGINT è presente nel set.\n");
>     } else {
>         printf("SIGINT non è presente nel set.\n");
>     }
> 
>     // Verifica di SIGTERM nel set
>     if (sigismember(&set, SIGTERM)) {
>         printf("SIGTERM è presente nel set.\n");
>     } else {
>         printf("SIGTERM non è presente nel set.\n");
>     }
> 
>     return 0;
> }
> ```

### 5.2.4 - Aggiunta di un segnale con `sigaddset()`

La **funzione `sigaddset()`** permette di aggiungere un segnale specifico a un set di segnali (di tipo `sigset_t`). Il suo prototipo è il seguente:

```c
#include <signal.h>

int sigaddset(sigset_t *set, int signum);
```

con:
- **`set`**: puntatore a un oggetto di tipo `sigset_t` che rappresenta un set di segnali.
- **`signum`**: intero che rappresenta il numero del segnale da aggiungere al set (es. `SIGINT`, `SIGTERM`).
- **`int` restituito**:
	- **`0`**: la funzione ha eseguito correttamente l'operazione.
	- **`-1`**: c'è stato un errore durante l'esecuzione della funzione ed `errno`%%link%% viene impostato con codice di errore `EINVAL`%%link%% (che indica un argomento non valido).

> [!esempio]
> 
> ```c
> #include <stdio.h>
> #include <signal.h>
> 
> int main() {
>     sigset_t set;
> 
>     // Inizializzazione del set vuoto
>     if (sigemptyset(&set) == -1) {
>         perror("Errore nell'inizializzazione del set");
>         return 1;
>     }
> 
>     // Aggiunta di SIGINT al set
>     if (sigaddset(&set, SIGINT) == -1) {
>         perror("Errore nell'aggiunta di SIGINT");
>         return 1;
>     }
> 
>     // Verifica di SIGINT nel set
>     if (sigismember(&set, SIGINT)) {
>         printf("SIGINT è stato aggiunto al set.\n");
>     } else {
>         printf("SIGINT non è nel set.\n");
>     }
> 
>     return 0;
> }
> ```

### 5.2.5 - Rimozione di un segnale con `sigdelset()`

La **funzione `sigdelset()`** permette di rimuovere un segnale specifico da un set di segnali (di tipo `sigset_t`). Il suo prototipo è il seguente:

```c
#include <signal.h>

int sigdelset(sigset_t *set, int signum);
```

con:
- **`set`**: puntatore a un oggetto di tipo `sigset_t` che rappresenta un set di segnali.
- **`signum`**: intero che rappresenta il numero del segnale da rimuovere dal set.
- **`int` restituito**:
	- **`0`**: la funzione ha eseguito correttamente l'operazione.
	- **`-1`**: c'è stato un errore durante l'esecuzione della funzione ed `errno`%%link%% viene impostato con codice di errore `EINVAL`%%link%% (che indica un argomento non valido).

> [!esempio]
> 
> ```c
> #include <stdio.h>
> #include <signal.h>
> 
> int main() {
>     sigset_t set;
> 
>     // Inizializzazione del set con tutti i segnali
>     if (sigfillset(&set) == -1) {
>         perror("Errore nell'inizializzazione del set");
>         return 1;
>     }
> 
>     // Rimozione di SIGINT dal set
>     if (sigdelset(&set, SIGINT) == -1) {
>         perror("Errore nella rimozione di SIGINT");
>         return 1;
>     }
> 
>     // Verifica di SIGINT nel set
>     if (sigismember(&set, SIGINT)) {
>         printf("SIGINT è ancora nel set.\n");
>     } else {
>         printf("SIGINT è stato rimosso dal set.\n");
>     }
> 
>     return 0;
> }
> ```

### 5.2.6 - Applicazione di una maschera al processo con `sigprocmask()`

La **funzione `sigprocmask()`** viene utilizzata per modificare la maschera associata a un processo.

Il suo prototipo è il seguente:

```c
#include <signal.h>

int sigprocmask(int how, const sigset_t *set, sigset_t *oldset);
```

con:
- **`how`**: intero che specifica come modificare la maschera esistente (quella correntemente applicata al processo) e può assumere i seguenti valori:
    - **`SIG_BLOCK`**: aggiunge i segnali specificati alla maschera già esistente.
    - **`SIG_UNBLOCK`**: rimuove i segnali specificati dalla maschera esistente.
    - **`SIG_SETMASK`**: sostituisce la maschera esistente con quella specificata.
- **`set`**: puntatore alla nuova maschera da applicare.
- **`oldset` (opzionale)**: puntatore alla maschera precedente (utile per poterla salvare prima di sostituirla con la nuova).
- **`int` restituito**:
	- **`0`**: la funzione ha eseguito correttamente l'operazione.
	- **`-1`**: c'è stato un errore durante l'esecuzione della funzione ed `errno`%%link%% viene impostato%%con che valore?%%.

> [!esempio]
> 
> ```c
> #include <stdio.h>
> #include <signal.h>
> #include <unistd.h>
> 
> int main() {
>     sigset_t set, oldset;
> 
>     // Inizializzazione di una maschera vuota
>     sigemptyset(&set);
>     sigaddset(&set, SIGINT); // Aggiunta di SIGINT alla maschera
> 
>     // Blocco di SIGINT
>     if (sigprocmask(SIG_BLOCK, &set, &oldset) == -1) {
>         perror("Errore nel blocco di SIGINT");
>         return 1;
>     }
> 
>     printf("SIGINT bloccato. Genera segnali con Ctrl + C.\n");
>     sleep(10);
> 
>     // Ripristino della maschera originale
>     if (sigprocmask(SIG_SETMASK, &oldset, NULL) == -1) {
>         perror("Errore nel ripristino della maschera");
>         return 1;
>     }
> 
>     printf("SIGINT sbloccato.\n");
>     sleep(10);
> 
>     return 0;
> }
> ```

## 5.3 - Segnali non bloccabili (`SIGKILL` e `SIGSTOP`)

Nei sistemi [UNIX](UNIX.md)/Linux%%link%%, esistono **segnali non bloccabili**, ignorabili o gestibili da un processo tramite un [signal handler](Segnali%20in%20UNIX.md#7.2%20-%20Assegnazione%20di%20un%20signal%20handler%20con%20`signal()`%20e%20`sigaction()`). Questi segnali hanno comportamenti predefiniti che il sistema operativo applica sempre, indipendentemente dalle richieste del processo. Gli unici due segnali non bloccabili sono:
- **`SIGKILL`**: termina immediatamente un processo, viene usato dal sistema operativo o dagli utenti per forzare la terminazione di un processo che non risponde a segnali ordinari.
- **`SIGSTOP`**: sospende immediatamente l'esecuzione di un process, viene utilizzato per mettere in pausa un processo (ad esempio con `Ctrl + Z` o comandi come `kill -STOP`).

Rendere questi segnali non bloccabili assicura che il sistema operativo mantenga un controllo minimo indispensabile sui processi, evitando situazioni in cui un processo malintenzionato o malfunzionante possa eludere la gestione dei segnali.

# 6 - Coda dei segnali pendenti

La **coda dei segnali pendenti** è una struttura utilizzata dal kernel%%link%% per mantenere traccia dei segnali che sono stati generati ma non ancora consegnati a un processo. Questo avviene quando:
- Un segnale è bloccato, cioè il processo ha indicato di non volerlo gestire immediatamente).
- Il processo è temporaneamente incapace di riceverlo (ad esempio, è in uno stato di pausa o attesa).

## 6.1 - Caratteristiche principali

- **Un segnale per tipo**: la coda non accumula più istanze dello stesso segnale. Se un segnale è già pendente, ulteriori generazioni dello stesso segnale vengono ignorate.
- **Gestione dei [segnali bloccati](Segnali%20in%20UNIX.md#5%20-%20Blocco%20del%20segnale)**: i segnali bloccati vengono aggiunti alla coda invece di essere immediatamente consegnati. Quando un segnale viene sbloccato (es. tramite [`sigprocmask()`](Segnali%20in%20UNIX.md#5.2.6%20-%20Applicazione%20di%20una%20maschera%20al%20processo%20con%20`sigprocmask()`)), esso viene prelevato dalla coda e consegnato.
- **Priorità dei segnali**: la priorità dei segnali non viene determinata in base al tempo di generazione, ma dipende dal tipo del segnale, assegnando ad alcuni segnali una priorità più alta se necessario.
- [**Segnali non bloccabili**](Segnali%20in%20UNIX.md#5.3%20-%20Segnali%20non%20bloccabili%20(`SIGKILL`%20e%20`SIGSTOP`)): alcuni segnali non possono essere messi nella coda dei segnali pendenti, come `SIGKILL`%%link%% e `SIGSTOP`%%link%%, che vengono gestiti immediatamente dal kernel%%link%%.
- **Compatibilità con i [thread](Thread.md)**: nei programmi multithreading%%link%%, ogni thread ha la propria coda dei segnali pendenti, ma alcuni segnali (es. segnali diretti al [processo](Processi.md)) possono essere condivisi e devono essere gestiti con coordinamento.
- **Non persistenza**: i segnali pendenti non vengono conservati se il processo a cui si riferiscono termina prima di riceverli.
- **Sicurezza nelle sezioni critiche**: permette di proteggere sezioni critiche di codice bloccando temporaneamente i segnali, senza rischiare di perdere notifiche importanti.

## 6.2 - Verifica dei segnali pendenti con `sigpending()`

La **funzione `sigpending()`** permette di controllare quali segnali sono attualmente pendenti per il processo.

Il suo prototipo è il seguente:

```c
#include <signal.h>

int sigpending(sigset_t *set);
```

con:
- **`set`**: puntatore a un oggetto `sigset_t` che verrà popolato con l'elenco dei segnali pendenti.
- **`int` restituito**:
	- **`0`**: la funzione ha eseguito correttamente l'operazione.
	- **`-1`**: c'è stato un errore durante l'esecuzione della funzione ed `errno`%%link%% viene impostato con codice di errore `EINVAL`%%link%% (che indica un argomento non valido).

> [!esempio]
> ```c
> #include <stdio.h>
> #include <stdlib.h>
> #include <signal.h>
> 
> int main() {
>     sigset_t set;
> 
>     // Controlla i segnali pendenti
>     if (sigpending(&set) == -1) {
>         perror("Errore nel recupero dei segnali pendenti");
>         exit(EXIT_FAILURE);
>     }
> 
>     // Verifica se SIGINT è pendente
>     if (sigismember(&set, SIGINT)) {
>         printf("SIGINT è pendente.\n");
>     } else {
>         printf("SIGINT non è pendente.\n");
>     }
> 
>     return 0;
> }
> ```

# 7 - Gestione del segnale

Al momento della ricezione di un segnale, il [processo](Processi.md) può decidere come gestirlo in uno dei seguenti modi:
- [**Eseguire l'azione predefinita**](Segnali%20in%20UNIX.md#7.1%20-%20Esecuzione%20dell'azione%20predefinita): se il segnale non è stato configurato diversamente, il processo esegue l'azione predefinita associata al segnale. 
- [**Assegnare un _signal handler_**](Segnali%20in%20UNIX.md#7.2%20-%20Assegnazione%20di%20un%20signal%20handler%20con%20`signal()`%20e%20`sigaction()`): il processo può assegnare una funzione (detta _signal handler_) per gestire un segnale specifico tramite le funzioni `signal()` e `sigaction()` anziché eseguire l'azione predefinita.

> [!nota] Nota
> I [segnali non bloccabili (`SIGKILL` e `SIGSTOP`)](Segnali%20in%20UNIX.md#5.3%20-%20Segnali%20non%20bloccabili%20(`SIGKILL`%20e%20`SIGSTOP`)) possono solamente eseguire l'azione predefinita.

## 7.1 - Esecuzione dell'azione predefinita

Alla ricezione del segnale, se non è stato configurato diversamente, il processo esegue l'**azione predefinita** associata al segnale. Ogni segnale ha un proprio comportamento preimpostato, che varia in base alla sua natura e scopo. Le principali azioni predefinite sono:
- **Terminazione del processo**: il processo termina immediatamente e il sistema libera le risorse allocate. Esempi di segnali con questa azione includono `SIGTERM` (terminazione ordinata) e `SIGINT` (interruzione da tastiera, azionabile con la combinazione di tasti `Ctrl + C`).
- **Terminazione con generazione di un core dump**: il processo termina e il sistema crea un _file di core dump_, utile per analizzare lo stato del programma al momento del crash. Esempi di segnali con questa azione sono `SIGSEGV` (violazione di segmentazione) e `SIGABRT` (interruzione forzata).
- **Ignorazione del segnale**: il processo non intraprende alcuna azione e continua la sua esecuzione. Esempi di segnali ignorati per impostazione predefinita includono `SIGCHLD`, che notifica la terminazione di un processo figlio.
- **Sospensione del processo**: il processo viene messo in stato di stop e rimane sospeso fino a quando non riceve un segnale per riprendere. Un esempio di segnali con questa azione è `SIGSTOP` (sospensione forzata, azionabile con la combinazione di tasti `Ctrl + Z`), che sospende il processo senza possibilità di blocco o gestione finché non riceve il segnale di ripresa `SIGCONT`.
- **Ripresa del processo**: il processo sospeso riprende la sua esecuzione. Un esempio è `SIGCONT`, utilizzato per continuare un processo precedentemente sospeso con `SIGSTOP`.

## 7.2 - Assegnazione di un signal handler con `signal()` e `sigaction()`

Le **funzioni `signal()` e `sigaction()`** sono utilizzate per gestire i segnali attraverso funzioni specificate dall'utente, dette _signal handler_.

La funzione `signal()` è una maniera più semplice per associare un gestore a un segnale.

Il suo prototipo è il seguente:

```c
#include <signal.h>

void (*signal(int sig, void (*handler)(int)))(int);
```

con:
- **`sig`**: segnale che si vuole gestire.
- **`handler`**: puntatore alla funzione che gestirà il segnale, la quale prende un parametro di tipo `int` (tipicamente il numero del segnale).

> [!esempio]
> ```c
> #include <stdio.h>
> #include <signal.h>
> 
> void handler(int sig) {
>     printf("Ricevuto segnale %d\n", sig);
> }
> 
> int main() {
>     signal(SIGINT, handler);  // Associa il gestore per SIGINT
>     return 0;
> }
> ```

> [!attenzione] Attenzione!
> Vi sono differenze nel comportamento della funzione `signal()` fra le varie implementazioni di [UNIX](UNIX.md); se possibile, quindi, va evitato il suo uso in programmi complessi.

La funzione `sigaction()` è una versione più potente e sicura per gestire i segnali. Permette un controllo più fine, come il blocco temporaneo dei segnali durante l'esecuzione del gestore.

Il suo prototipo è il seguente:

```c
#include <signal.h>

int sigaction(int sig, const struct sigaction *act, struct sigaction *oldact);
```

con:
- **`sig`**: segnale che si vuole gestire.
- **`act`**: puntatore a una struttura `sigaction` che descrive come deve essere gestito il segnale.
- **`oldact`**: puntatore a una struttura `sigaction` in cui verrà memorizzato il gestore precedente (può essere `NULL`).
- **`int` restituito**:
	- **`0`**: la funzione ha eseguito correttamente l'operazione.
	- **`-1`**: c'è stato un errore durante l'esecuzione della funzione ed `errno`%%link%% viene impostato con codice di errore `EINVAL`%%link%% (che indica un argomento non valido).

### 7.2.1 - Struttura `sigaction`

La **struttura `sigaction`** è così definita:

```c
struct sigaction {
    void (*sa_handler)(int);
    sigset_t sa_mask;
    int sa_flags;
    void (*sa_restorer)(void);
};
```

con:
- **`sa_handler`**: funzione che definisce il comportamento da adottare all'attivazione del segnale (_signal handler_).
- **`sa_mask`**: [maschera dei segnali](Segnali%20in%20UNIX.md#5.2%20-%20Maschera%20dei%20segnali) temporanea applicata durante l'esecuzione dell'handler che sostituisce quella legata al processo in esecuzione. Insieme ai segnali specificati in questa maschera, viene automaticamente bloccato anche il segnale che ha attivato l'handler.
- **`sa_flags`**: flag per personalizzare il comportamento dell'handler.
- **`sa_restorer` (obsoleto)**: puntatore a una funzione che il kernel%%link%% potrebbe utilizzare per ripristinare il contesto del programma dopo l'esecuzione di un signal handler. Era usato in implementazioni storiche per specificare una routine di "pulizia" che riportava il processo al suo stato normale dopo che il signal handler terminava.

> [!esempio]
> ```c
> #include <stdio.h>
> #include <signal.h>
> 
> void handler(int sig) {
>     printf("Ricevuto segnale %d\n", sig);
> }
> 
> int main() {
>     struct sigaction sa;
>     sa.sa_handler = handler;  // Imposta il gestore
>     sigemptyset(&sa.sa_mask);  // Nessun segnale è bloccato durante l'esecuzione
>     sa.sa_flags = 0;  // Nessun flag particolare
>     sigaction(SIGINT, &sa, NULL);  // Associa il gestore a SIGINT
>     return 0;
> }
> ```

%%
**Esempio Pratico**

Supponiamo che:

- La **signal mask del processo** blocchi i segnali `SIGUSR1` e `SIGUSR2`.
- Un handler per `SIGINT` ha `sa_mask` configurata per bloccare `SIGTERM` e `SIGQUIT`.

Se il processo riceve `SIGINT`:

1. La signal mask globale viene temporaneamente aggiornata:
    - Blocca `SIGTERM`, `SIGQUIT` (da `sa_mask`) e `SIGINT` stesso (blocco automatico).
2. Durante l'esecuzione del handler, questi segnali saranno bloccati.
3. Quando il handler termina, la mask del processo ritorna a bloccare solo `SIGUSR1` e `SIGUSR2`.
%%

### 7.2.2 - Meglio usare `signal()` o `sigaction()`?

Solitamente, **`sigaction()` è preferita** rispetto a `signal()` per i seguenti motivi:
- **Flessibilità**: `sigaction()` permette di bloccare temporaneamente altri segnali durante l'esecuzione del gestore e offre maggiore controllo sui segnali.
- **Compatibilità**: `signal()` può avere un comportamento imprevisto su alcune piattaforme, mentre `sigaction()` è più robusta e portabile.
- **Controllo avanzato**: con `sigaction()` è possibile specificare una maschera di segnali da bloccare durante l'esecuzione del gestore e altre opzioni, mentre `signal()` è più semplice ma meno potente.

### 7.2.3 - Interruzione del signal handler

Il **signal handler**, durante la sua esecuzione, può comunque essere **interrotto** da altri segnali (o dallo stesso segnale, nel caso la flag `SA_NODEFER` sia settata nella [struttura `sigaction`](Segnali%20in%20UNIX.md#7.2.1%20-%20Struttura%20`sigaction`) in modo da evitare il blocco automatico del segnale che attiva l'handler).

Quando l’handler termina, la [maschera dei segnali](Segnali%20in%20UNIX.md#5.2%20-%20Maschera%20dei%20segnali) viene reimpostata al valore precedente la sua esecuzione, indipendentemente dalle possibili manipolazioni dei segnali bloccati eventualmente presenti nell'handler.

%%
### 7.2.4 - Ereditarietà del signal handler

In seguito a un'operazione di [`fork()`](Processi.md#5.2%20-%20`fork()`%20in%20Unix/Linux), il **signal handler viene ereditato** dal processo figlio.

Le funzioni di gestione degli handler vengono ereditate dai processi figli dopo una fork
Le variabili globali definite nel programma sono visibili sia dalle funzioni handler che dal resto del programma

Questo può essere utile per modificare il valore di una variabile globale simulando un cambio di stato del programma che verrà poi utilizzato durante l’esecuzione “normale” del codice
Ma… Le variabili globali possono essere utili, ma cosa succede quando un hadler modifica il valore di una variabile globale il cui valore non dovrebbe essere modificato?
Alcune system call utilizzano strutture dati globali e quindi il loro utilizzo all’interno di un handler può generare problemi
	Esempio: printf
Cosa succede se un segnale interrompe l’esecuzione di una printf, che poi viene anche utilizzata all’interno dell’handler?
```
man signal-safety
```

Fortunatamente ci sono funzioni che sono definite in libc ”AS-Safe” (Asynchronous Signal-Safe)
	Esempio: write()
Consiglio: ogni volta che si vuole utilizzare una system call in un handler, controllare se è AS-safe nella documentazione.
`errno` è una variabile globale e il suo valore potrebbe essere sovrascritto durante l’esecuzione di un handler. Consiglio: salvare e ripristinare il valore di errno nell’handler
%%

# 8 - Lista dei segnali più comuni

| **Segnale**                                                                  | **Numero** | **Quando viene generato**                                                        | **Azione predefinita**                                                                                                                            |
| ---------------------------------------------------------------------------- | ---------- | -------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------- |
| `SIGHUP`<br>(_**h**ang **up**_)                                              | `1`        | Disconnessione del terminale%%link%% o chiusura della shell%%link%%.             | Termina o ricarica il processo, spesso usato per configurazioni.                                                                                  |
| `SIGINT`<br>(_**int**errupt_)                                                | `2`        | Interruzione da tastiera (`Ctrl + C`).                                             | Termina il processo.                                                                                                                              |
| `SIGQUIT`<br>(_**quit**_)                                                    | `3`        | Interruzione da tastiera con dump (`Ctrl+\`).                                    | Termina il processo e genera un core dump.                                                                                                        |
| `SIGILL`<br>(_**ill**egal instruction_)                                      | `4`        | Istruzione illegale eseguita dal processo.                                       | Termina il processo segnalando un errore critico.                                                                                                 |
| `SIGTRAP`<br>(_**trap**_)                                                    | `5`        | Breakpoint impostato da un debugger (es. GDB%%link%%) o sollevata un'eccezione.  | Termina il processo con generazione di un core dump.                                                                                              |
| `SIGABRT`<br>(_**ab**o**rt**_)                                               | `6`        | Invocazione della funzione `abort()`%%link%%.                                    | Termina il processo e genera un core dump.                                                                                                        |
| `SIGBUS`<br>(_**bus** error_)                                                | `7`        | Accesso a memoria non allineato o errore su memoria mappata.                     | Termina il processo con generazione di un core dump.                                                                                              |
| `SIGFPE`<br>(_**f**loating **p**oint **e**xception_)                         | `8`        | Errore aritmetico (es. divisione per zero).                                      | Termina il processo e segnala un errore matematico.                                                                                               |
| `SIGKILL`<br>(_**kill**_)                                                    | `9`        | Inviato dal kernel o da un comando `kill -9`%%link%%.                            | Termina immediatamente il processo ([non bloccabile](Segnali%20in%20UNIX.md#5.3%20-%20Segnali%20non%20bloccabili%20(`SIGKILL`%20e%20`SIGSTOP`))). |
| `SIGUSR1`<br>(_**us**e**r** defined **1**_)                                  | `10`       | Generato da altri processi per scopi personalizzati.                             | Usato per notifiche o segnali definiti dall'utente.                                                                                               |
| `SIGSEGV`<br>(_**seg**mentation **v**iolation_)                              | `11`       | Accesso a memoria non valida (es. dereferenziamento nullo).                      | Termina il processo e genera un core dump.                                                                                                        |
| `SIGUSR2`<br>(_**us**e**r** defined **2**_)                                  | `12`       | Generato da altri processi per scopi personalizzati.                             | Usato per notifiche o segnali definiti dall'utente.                                                                                               |
| `SIGPIPE`<br>(_**pipe**_)                                                    | `13`       | Scrittura su una [pipe](Pipe.md) chiusa o lettura non valida.                    | Termina il processo o gestisce l'errore.                                                                                                          |
| `SIGALRM`<br>(_**al**a**rm**_)                                               | `14`       | Timer scaduto generato da una funzione `alarm()`%%link%% o `settimer()`%%link%%. | Utilizzato per gestire timeout nei processi.                                                                                                      |
| `SIGTERM`<br>(_**term**inate_)                                               | `15`       | Richiesta di terminazione ordinata tramite comando `kill`%%link%%.               | Termina il processo in modo ordinato.                                                                                                             |
| `SIGSTKFLT`<br>(_**st**ac**k** **f**au**lt**_)                               | `16`       | Errore relativo alla gestione dello stack (segnale obsoleto).                    | Termina il processo.                                                                                                                              |
| `SIGCHLD`<br>(_**ch**i**ld**_)                                               | `17`       | Processo figlio terminato o sospeso.                                             | Notifica al processo padre della terminazione di un figlio.                                                                                       |
| `SIGCONT`<br>(_**cont**inue_)                                                | `18`       | Ripresa di un processo sospeso.                                                  | Riprende l'esecuzione di un processo sospeso precedentemente con `SIGSTOP`.                                                                       |
| `SIGSTOP`<br>(_**stop**_)                                                    | `19`       | Sospensione forzata di un processo.                                              | Sospende il processo ([non bloccabile](Segnali%20in%20UNIX.md#5.3%20-%20Segnali%20non%20bloccabili%20(`SIGKILL`%20e%20`SIGSTOP`))).               |
| `SIGTSTP`<br>(_**t**erminal **st**o**p**_)                                   | `20`       | Sospensione da tastiera (`Ctrl + Z`).                                              | Sospende il processo, modificabile dal processo.                                                                                                  |
| `SIGTTIN`<br>(_**t**erminal **in**put_)                                      | `21`       | Processo in background tenta di leggere dall'input.                              | Sospende il processo fino a che non è in primo piano.                                                                                             |
| `SIGTTOU`<br>(_**t**erminal **ou**tput_)                                     | `22`       | Processo in background tenta di scrivere sull'output.                            | Sospende il processo fino a che non è in primo piano.                                                                                             |
| `SIGPOLL`<br>(_**poll**able event_)<br>o `SIGIO`<br>(_**i**nput/**o**utput_) | `29`       | Evento su un descrittore di file monitorato.                                     | Notifica un input/output disponibile (POSIX%%link%%).                                                                                             |

# Fonti

- Slide del Prof. Schifanella Claudio del corso di Laboratorio di Sistemi Operativi (canale B, turno T4), Corso di Laurea in Informatica presso l'Università di Torino, A.A. 2024-25:
	- [Slide: i segnali](https://informatica.i-learn.unito.it/mod/resource/view.php?id=254494)
%%
da vedere:
- https://didawiki.di.unipi.it/lib/exe/fetch.php/lcs/lcs06/esercitazioni/11segnali.pdf
%%


