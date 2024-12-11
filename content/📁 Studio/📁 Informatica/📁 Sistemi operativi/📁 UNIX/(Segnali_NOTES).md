---
draft: true
---

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
