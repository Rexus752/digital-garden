I **segnali** sono un meccanismo di [comunicazione tra processi](Processi.md#7%20-%20Comunicazione%20tra%20processi%20(IPC)) utilizzato per notificare a un processo l'occorrenza di un evento specifico, come un errore, un'interruzione dell'utente o un'operazione speciale.

# 1 - Nomi simbolici dei segnali

Ogni segnale è associato univocamente a:
- Un **intero**, a partire dall'`1`.
- Un **nome simbolico**, della forma `SIG***`.

Poiché gli effettivi interi assegnati a ogni segnale variano a seconda delle implementazioni nei vari [sistemi operativi](Sistema%20operativo.md), all'interno dei programmi è meglio utilizzare direttamente i nomi simbolici.

# 2 - Gestione dei segnali

Un processo può decidere come gestire i segnali che riceve. Le opzioni di gestione sono:
- **Azione predefinita**: ogni segnale ha un'azione predefinita, che può includere la terminazione, la sospensione o l'ignorazione del processo.
- **Cattura del segnale**: un processo può registrare una funzione per gestire un segnale specifico tramite le funzioni `signal()` o `sigaction()` in C%%link%%.
- **Ignorare un segnale**: un processo può decidere di ignorare alcuni segnali, come `SIGINT`, usando una funzione di gestione personalizzata (quando ciò è possibile).

## 2.1 - Funzioni `signal()` e `sigaction()` in C

In C, le **funzioni `signal()` e `sigaction()`** sono utilizzate per gestire i segnali.

La funzione `signal()` è una maniera più semplice per associare un gestore a un segnale. La sua dichiarazione è la seguente:
```c
void (*signal(int sig, void (*handler)(int)))(int);
```
dove:
- **`sig`**: è il numero del segnale (ad esempio, `SIGINT` per l'interruzione da tastiera).
- **`handler`**: è il puntatore alla funzione che gestirà il segnale, la quale prende un parametro di tipo `int` (tipicamente il numero del segnale).

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

Tuttavia, `signal()` ha delle limitazioni (come un comportamento meno prevedibile su alcune piattaforme) e non è raccomandata per un uso robusto in programmi complessi.

La funzione `sigaction()` è una versione più potente e sicura per gestire i segnali. Permette un controllo più fine, come il blocco temporaneo dei segnali durante l'esecuzione del gestore. La sua dichiarazione è la seguente:
```c
int sigaction(int sig, const struct sigaction *act, struct sigaction *oldact);
```
dove:
- **`sig`**: il segnale che si vuole gestire.
- **`act`**: un puntatore a una struttura `sigaction` che descrive come deve essere gestito il segnale.
- **`oldact`**: un puntatore a una struttura `sigaction` in cui verrà memorizzato il gestore precedente (può essere `NULL`).

### 2.1.1 - Struttura `sigaction`

La **struttura `sigaction`** è così definita:
```c
struct sigaction {
    void (*sa_handler)(int);
    sigset_t sa_mask;
    int sa_flags;
    void (*sa_restorer)(void);
};
```
dove:
- **`sa_handler`**: è la funzione gestore.
- **`sa_mask`**: maschera di segnali%%cazzo è una maschera di segnali?%%%%link%% da bloccare durante il gestore.
- **`sa_flags`**: flag per personalizzare il comportamento dell'handler.
- **`sa_restorer`**: tradizionalmente, questo campo poteva essere usato per restituire il controllo al sistema operativo dopo l'esecuzione del gestore del segnale. Tuttavia, oggi è obsoleto e non viene utilizzato in molte implementazioni.

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

### 2.1.2 - Meglio usare `signal()` o `sigaction()`?

Solitamente, `sigaction()` è preferita rispetto a `signal()` per i seguenti motivi:
- **Flessibilità**: `sigaction()` permette di bloccare temporaneamente altri segnali durante l'esecuzione del gestore e offre maggiore controllo sui segnali.
- **Compatibilità**: `signal()` può avere un comportamento imprevisto su alcune piattaforme, mentre `sigaction()` è più robusta e portabile.
- **Controllo avanzato**: Con `sigaction()` puoi specificare una maschera di segnali da bloccare durante l'esecuzione del gestore e altre opzioni, mentre `signal()` è più semplice ma meno potente.

# 3- Segnali in UNIX

I **segnali in [UNIX](UNIX.md)** si dividono nelle seguenti categorie:
- **Trap**: segnali generati da un processo e inviati al processo stesso.
- **Interrupt**: segnali generati da un agente esterno (es. utente, altro processo) a un processo.
%%siamo sicuri sia questa la definizione di trap e interrupt?%%

## 3.1 - Trap

In [UNIX](UNIX.md), le **trap** sono segnali generati da eventi prodotti da un processo e inviati al processo stesso. Alcune trap sono causate da comportamenti errati del processo stesso, e immediatamente inviate al processo che normalmente reagisce terminando.

Sono esempi di trap i tentativi di divisione per zero (`SIGFPE`), indirizzamento errato degli array (`SIGSEGV`), tentativo di eseguire istruzioni privilegiate (`SIGILL`), ecc.

## 3.2 - Interrupt

In [UNIX](UNIX.md), gli **interrupt** sono segnali inviati ad un processo da un agente esterno (come l'utente o un altro processo).

Esempi di interrupt inviati dall'utente sono la pressione delle combinazione di tasti `CTRL+C` (`SIGINT`) o `CTRL+Z` (`SIGSTOP`) durante l'esecuzione di un processo, mentre un interrupt inviato da un altro processo può essere la system call `kill()`%%link%%.

# Fonti

- Slide del Prof. Schifanella Claudio del corso di Laboratorio di Sistemi Operativi (canale B, turno T4), Corso di Laurea in Informatica presso l'Università di Torino, A.A. 2024-25:
	- [Slide: i segnali](https://informatica.i-learn.unito.it/mod/resource/view.php?id=254494)