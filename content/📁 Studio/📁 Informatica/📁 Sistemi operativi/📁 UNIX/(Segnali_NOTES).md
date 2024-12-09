---
draft: true
---

```
17 SIGSTOP - stop process - stop (cannot be caught or ignored)
15 SIGTERM - terminate process - software termination signal
```
- SIGSTOP. Segnale per il blocco (stop) sicuro. Non può essere bloccato, ignorato, o intercettato da un handler; quindi questo segnale blocca sempre un processo.
- SIGTERM. Segnale standard utilizzato per terminare un processo; segnale inviato di default dai comandi kill e killall. Gli utenti a volte inviano esplicitamente il segnale SIGKILL a un processo, usando `kill –KILL` or `kill –9`.
	- In generale, questo è un errore. Un'applicazione ben progettata deve avere un handler per SIGTERM che consenta una 'graceful' exit, che consenta di pulire i file temporanei e di rilasciare le altre risorse. L'uccisione di un processo con SIGKILL bypassa l'handler di SIGTERM, e quindi si dovrebbe sempre prima cercare di terminare un processo con SIGTERM, e tenere SIGKILL come ultima scelta per terminare i processi che non rispondono a SIGTERM.
```
5 SIGTRAP create core image trace trap
18 SIGTSTP stop process stop signal generated from
```
- SIGTRAP. Segnale utilizzato per implementare i breakpoint in fase di debugging e per la tracciatura delle system call.
	- Cercare ptrace() sul manuale per ulteriori informazioni.
- SIGTSTP. Segnale per lo stop, inviato per bloccare il gruppo di processi in foreground quando l'utente digita il carattere di sospensione (Control-Z) sulla tastiera.
	- il nome di questo segnale deriva da "terminal stop".
```
30 SIGUSR1 terminate process User defined signal 1
31 SIGUSR2 terminate process User defined signal 2
```
- SIGUSR1. Questo segnale e SIGUSR2 sono disponibili per fini specificati dal programmatore. Il kernel non genera mai questi segnali per un processo.
	- I processi possono utilizzare questi segnali per notificarsi a vicenda eventi, o per sincronizzarsi

# Invio di segnali `kill()`, `raise()` e `alarm()`

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

## La system call `kill()`

```c
#include <signal.h>

int kill(pid_t pid, int sig);

// Returns 0 on success, or –1 on error
```

L'argomento `pid` identifica uno o più processi a cui inviare il segnale; `pid` può essere interpretato in 4 modi:
- `pid > 0`: il segnale è inviato al processo identificato da pid.
- `pid == 0`: il segnale è inviato a ogni processo nello stesso gruppo del chiamante, chiamante incluso.
- `pid < –1`: il segnale è inviato a tutti i processi nel gruppo del processo il cui ID è uguale al valore assoluto di pid. Inviare un segnale a tutti i processi nel gruppo di un processo è utile nel controllo dei job effettuato con la shell.
- `pid == –1`: (broadcast signal) il segnale è inviato a tutti i processi per i quali il processo ha i permessi di inviare un segnale, eccetto init (che ha pid 1) ed il chiamante. Se l'utente non è super user, il segnale è inviato a tutti i processi con stesso uid dell'utente, escluso il processo che invia il segnale.

Se nessun processo corrisponde al pid predefinito, `kill()` fallisce e setta `errno` a `ESRCH` (“No such process”). Se il processo esiste, ma non si hanno i permessi per inviare un segnale, allora `errno = EPERM`.
Verifica dell'esistenza di un processo. Se l'argomento sig è settato a 0 (detto null signal), non è inviato alcun segnale. In questo caso kill() esegue unicamente un controllo degli errori per vedere se è possibile inviare segnali al processo: il null signal può essere utilizzato per testare se un processo con un certo pid esiste. Se la chiamata va a buon fine, sappiamo che il processo esiste.

## La system call `raise()`

```c
#include <signal.h>

int raise(int sig);

//Returns 0 on success, or nonzero on error
```

Permette di inviare un segnale al processo stesso che invoca la system call

## La system call `alarm()`

```
#include <unistd.h>

unsigned int alarm (unsigned int sec);
```

Permette di inviare un segnale `SIGALRM` al processo stesso che invoca la system call dopo un numero di secondi
Valore di ritorno:
- 0 se non ci sono precedenti invocazioni di alarm pendenti
- il numero di secondi che mancano alla scadenza dell’allarme precedente

# Cambiare l’handler dei segnali

I sistemi UNIX forniscono due modi per cambiare l’handler di un segnale: signal() e sigaction().
La system call signal() è l'API originale per assegnare l’handler di un signal, e fornisce un'interfaccia più semplice di sigaction().
NB: vi sono differenze nel comportamento di signal() fra le varie implementazioni di UNIX -> da evitare!

Un signal handler è una funzione chiamata quando un processo riceve uno specifico segnale.
L'invocazione di un handler può interrompere il flusso principale del programma in qualsiasi momento; il kernel chiama l'handler da parte del processo, e quando l'handler restituisce, l'esecuzione del programma riprende dal punto in cui l'handler lo aveva interrotto.

## Gestione dei segnali con sigaction

Gestione dei segnali più completa e robusta rispetto all’uso di `signal()` (che tra l’altro non va usata).

Parametri:
- signum: segnale che deve essere gestito
- act: nuovo handler per il segnale (se NULL, nessun cambiamento)
- oldact: puntatore al vecchio handler

```
#define _GNU_SOURCE
#include <signal.h>

int sigaction(int signum, const struct sigaction *act, struct sigaction *oldact);
```

```
struct sigaction new, old;

// set new handler to new
sigaction(signum, new, NULL);

// current handler in old
sigaction(signum, NULL, old);

// do both
sigaction(signum, new, old);
```

## Sigaction structure

Principali elementi:
- sa_handler: puntatore alla funzione di handling
- sa_mask: maschera per indicare i segnali bloccati durante l’esecuzione dell’handler
- sa_flags: maschera bitwise (or-style) che modifica il comportamento del gestore del segnale
```
#define _GNU_SOURCE
#include <signal.h>

struct sigaction {
	void (*sa_handler)(int signum);
	sigset_t sa_mask;
	int sa_flags;
	// plus others (for advanced users)
};
```

Il costrutto switch può essere utilizzato per discriminare il tipo di segnale che l’handler ottiene come argomento:
```
void handle_signal(int signum) {
	/* signal signum triggered the handler */
	switch (signum) {
		case SIGINT:
			/* handle SIGINT */
			break;
		case SIGALRM:
			/* handle SIGALRM */
			break;
		/* other signals */
	}
}
```

# Handler definiti dall’utente

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

# sigaction structure: signal mask

Quando un segnale signum è consegnato ad un processo, durante l’esecuzione del suo handler, il segnale signum è bloccato. A meno che il flag SA_NODEFER è settato nella sigaction:
```
struct sigaction sa;
sigset_t my_mask;

sa.sa_handler = handle_signal;
sa.sa_flags = SA_NODEFER; // allow nested invocations
sigemptyset(&my_mask); // do not mask any signal
sa.sa_mask = my_mask;
sigaction(SIGUSR1, &sa, NULL); // set the handler
```

# Signal mask

La maschera è la collezione di segnali attualmente blocked. Ogni processo ha la propria maschera di segnali: un nuovo processo eredita la maschera del genitore
- Le maschere sono di tipo sigset_t
- Le funzioni per la manipolazione dei set sono (`man sigsetops` per dettagli):
```c
int sigemptyset(sigset_t *set);
int sigfillset(sigset_t *set);
int sigaddset(sigset_t *set, int signum);
int sigdelset(sigset_t *set, int signum);
int sigismember(const sigset_t *set, int signum);
```

## Impostare la maschera dei segnali di un processo

```c
#include <signal.h>
int sigprocmask(int how, const sigset_t *set, sigset_t *oldset);
Returns 0 if successful; otherwise the value -1 is returned and the global variable errno is set.
```

Per impostare la maschera di segnali bloccati durante l’esecuzione dei processi si usa la system call sigprocmask(). L’argomento how può assumere i seguenti valori:
- SIG_BLOCK: i segnali nel set sono aggiunti a quelli bloccati;
- SIG_UNBLOCK: i segnali nel set sono rimossi dalla maschera esistente;
- SIG_SETMASK: il set diventa la nuova maschera del segnale.
`oldset` è la vecchia maschera

```
static int segnale_ricevuto = 0;
int main (int argc, char *argv[]) {
	sigset_t orig_mask;
	sigset_t mask;
	struct sigaction act;
	
	printf("process pid: %d\n", getpid());
	memset (&act, 0, sizeof(act));
	act.sa_handler = mio_handler;
	
	if (sigaction(SIGTERM, &act, 0))
		; // gestione errore
	sigemptyset (&mask);
	sigaddset (&mask, SIGTERM);
	if (sigprocmask(SIG_BLOCK, &mask, &orig_mask) < 0)
		; // gestione errore
	sleep (20);
	if (sigprocmask(SIG_SETMASK, &orig_mask, NULL) < 0)
		; // gestione errore
	sleep (1);
	if (segnale_ricevuto) puts (“signal ricevuto!!!”);
	return 0;
}
```

## Signal mask during a handler

L’handler può comunque essere interrotto da altri segnali (o dallo stesso segnale, nel caso SA_NODEFER sia settato). Quando l’handler termina, l’insieme di segnali bloccati è reimpostato al suo valore precedente la sua esecuzione, indipendentemente dalle possibili manipolazioni dei segnali bloccati eventualmente presenti nell’handler.
L’handler può comunque essere interrotto da altri segnali (o dallo stesso segnale, nel caso SA_NODEFER sia settato):
```c
struct sigaction sa;
sigset_t my_mask;

sa.sa_handler = &handle_signal; // handler
sa.sa_flags = 0; // No special behaviour

// Create an empty mask
sigemptyset(&my_mask); // Do not mask any signal
sigaddset(&my_mask, signal_to_mask_in_handler);
sa.sa_mask = my_mask;

sigaction(SIGINT, &sa, NULL); // Set the handler
```

## Merged signals

Se un segnale viene generato mentre un altro segnale (stesso segnale) è in stato pending, il nuovo segnale e quello pending sono accorpati in uno; la presenza di un segnale pending è gestita solo con un flag, non da un numero (di segnali in stato pending). Un gestore di segnali non può essere utilizzato per contare il numero di segnali ricevuti.

## Delivery di segnali a processi sospesi

pause(), sleep() e nanosleep()

```c
#include <unistd.h>

int pause(void);
```

```c
#include <unistd.h>

unsigned int sleep(unsigned int seconds);
```

```c
#include <time.h>

struct timespec my_time;
my_time.tv_sec = 1;
my_time.tv_nsec = 234567000;
nanosleep(&my_time, NULL);
```

All’arrivo (asincrono) di un segnale
1. Lo stato del processo è salvato (registers, etc.)
2. La funzione di handler è eseguita
3. Lo stato iniziale del processo è ripristinato

Quando un processo è in attesa su wait() (o altre system call), o sospeso con pause()o sleep():
1. il processo non è in esecuzione (è sospeso su qualche system call)
2. la funzione dell’handler è eseguita normalmente
3. quando l’handler ritorna:
	A. la syscall restituisce un errore, con errno settato a EINTR; o
	B. la syscall viene automaticamente ripresa.

A o B? dipende dal sistema operativo, e dal flag SA_RESTART nella syscall sigaction(). Il comportamento di default è A (aborting).
Se il flag SA_RESTART è settato in sa_flags, si ha invece un restart della system call che aveva generato l’attesa. Il comportamento dipende dalla system call, purtroppo. Nella sezione «Interruption of system calls and library functions by signal handlers» di «man 7 signal» ci sono le indicazioni puntuali

# Gestione sincrona dei segnali

Non utilizzata durante il corso
La gestione sincrona dei segnali è possibile. Un processo può attendere la ricezione di un particolare segnale
Se interessati, approfondire le system call sigwaitinfo(), sigtimedwait(), sigwait()

Esercizio:
- Scrivere un programma che realizzi un semplice gioco. Il programma seleziona un numero intero casuale tra 0 e argv[1] (il primo argomento passato a riga di comando), e l’utente deve indovinare questo numero. Per fare questo, viene realizzato un ciclo in cui il programma legge da tastiera un numero inserito dall’utente:
	- se il numero è stato indovinato, il gioco finisce;
	- se il numero è maggiore o minore di quello estratto casualmente, viene stampato a video la scritta “maggiore” o “minore”, rispettivamente.
- Se il giocatore non indovina entro argv[2] secondi (da realizzare con alarm e gestendo il segnale SIGALRM), il programma stampa a video “tempo scaduto”, ed esce.

---

### Caratteristiche principali:

1. **Asincronia**: I segnali possono essere inviati a un processo in qualsiasi momento.
2. **Gestione**:
    - Un processo può **ignorare** un segnale.
    - Può definire un **gestore personalizzato** (signal handler) per eseguire un'azione specifica.
    - Oppure può lasciare che il sistema esegua l'azione di default per quel segnale.
3. **Origine**: I segnali possono essere generati dal kernel, da altri processi, o dall'utente tramite comandi come `kill`.

### Esempi di segnali comuni:

- **SIGINT**: Interruzione da tastiera (Ctrl+C).
- **SIGKILL**: Termine immediato del processo (non ignorabile).
- **SIGTERM**: Richiesta di terminazione (può essere gestita).
- **SIGHUP**: Segnale di "hang-up" (ad esempio, quando si chiude un terminale).
- **SIGSEGV**: Accesso a memoria non valida (es. segment fault).
- **SIGSTOP** e **SIGCONT**: Sospensione e ripresa di un processo.

### Programmazione con segnali (C come esempio):

La libreria standard di C offre funzioni per gestire i segnali, come:

- `signal()`: Per associare un gestore personalizzato a un segnale.
- `kill()`: Per inviare segnali a un processo.
- `raise()`: Per inviare segnali al processo corrente.
- `sigaction()`: Per configurazioni più avanzate.

### Applicazioni:

- Interruzione o controllo dei processi.
- Sincronizzazione tra processi.
- Gestione degli errori (es. chiusura di risorse su errore).
- Debugging (es. gestione di segfault con SIGSEGV).
