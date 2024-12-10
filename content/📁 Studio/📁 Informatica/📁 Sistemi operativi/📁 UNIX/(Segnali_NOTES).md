---
draft: true
---
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
