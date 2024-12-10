---
icon: FasNetworkWired
iconColor: "#FF88FF"
---
Le **pipe** %%([pronuncia]: `/paɪp/`)%%sono un meccanismo di [comunicazione tra processi](Processi.md#7%20-%20Comunicazione%20tra%20processi%20(IPC)) che permettono a uno o più processi di condividere dati tramite un canale unidirezionale. In sostanza, una pipe crea un collegamento tra due processi: uno scrive dati nella pipe e l'altro legge quei dati.

# 1 - Caratteristiche principali

- **Unidirezionali**: i dati fluiscono in una sola direzione (dal processo scrivente a quello leggente).
- **Anonime**: sono tipicamente usate tra processi che hanno una relazione gerarchica (padre-figlio). In genere, il processo padre crea una pipe e poi genera il processo figlio che la usa.
- **Comunicazione in memoria**: la pipe si comporta come un buffer circolare tra i due processi, memorizzando temporaneamente i dati fino a quando non vengono letti.

# 2 - Funzionamento delle pipe

Una pipe in UNIX o Linux può essere creata con la chiamata di sistema%%link%% `pipe()`. Questa funzione genera due file descriptor:
- Il file descriptor per la lettura (`fd[0]`);
- Il file descriptor per la scrittura (`fd[1]`).

Un processo può scrivere dati nel file descriptor `fd[1]` e un altro processo può leggerli dal file descriptor `fd[0]`.

%%mettere link ai file descriptor%%

## 2.1 - Esempio di codice in linguaggio C

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

# 3 - Vantaggi e svantaggi delle pipe

I principali vantaggi delle pipe sono:
- **Semplicità**: le pipe sono facili da usare e implementare, soprattutto per la comunicazione tra processi con una relazione gerarchica (ad esempio, un processo padre e un processo figlio). Sono supportate direttamente a livello del sistema operativo, con chiamate di sistema semplici come `pipe()` per creare una pipe e `read()`/`write()` per leggere e scrivere dati.
- **Comunicazione unidirezionale**: le pipe forniscono un canale di comunicazione unidirezionale, utile in situazioni in cui i dati devono fluire solo in una direzione (da un processo produttore a un processo consumatore).
- **Buffering automatico**: le pipe utilizzano un buffer interno gestito dal sistema operativo, che rende la gestione dei dati tra i processi più semplice, senza necessità di gestire manualmente il buffering dei dati.
- **Sincronizzazione implicita**: le pipe assicurano una forma di sincronizzazione implicita, in quanto se un processo tenta di leggere da una pipe vuota, verrà bloccato fino a quando non ci saranno dati disponibili. Allo stesso modo, se la pipe è piena, il processo che scrive attenderà fino a quando c'è spazio libero.
- **Indipendenza dalla rete**: le pipe funzionano a livello locale tra processi sullo stesso sistema, senza necessità di connessioni di rete, il che le rende efficienti in termini di prestazioni per la comunicazione tra processi locali.

I principali svantaggi delle pipe sono:
- **Unidirezionalità**: i dati nelle pipe possono fluire in una sola direzione. Se è necessaria la comunicazione bidirezionale (andata e ritorno), bisogna creare due pipe, aumentando la complessità della gestione dei dati.
- **Uso limitato tra processi correlati**: le pipe, dette anche _pipe anonime_ o _pipe convenzionali_, funzionano solo tra processi che hanno una relazione gerarchica (ad esempio, un processo padre che comunica con il figlio). Per comunicare tra processi non correlati, è necessario usare le [named pipe](#4%20-%20Named%20pipe), che sono più complesse da gestire rispetto alle pipe anonime.
- **Capacità limitata**: le pipe hanno una capacità limitata (tipicamente qualche kilobyte%%link%%). Se il buffer si riempie, il processo scrivente viene bloccato finché il buffer non viene svuotato. Allo stesso modo, se non ci sono dati, il processo leggente viene bloccato.
- **Accesso sequenziale**: le pipe operano in modo sequenziale secondo la politica FIFO (First In, First Out). Questo è ideale per flussi semplici di dati, ma in scenari complessi, in cui è richiesta una gestione avanzata dei messaggi, le pipe possono risultare limitate.
- **No persistenza dei dati**: i dati nelle pipe sono transienti, cioè una volta che i dati vengono letti, vengono rimossi dalla pipe. Se un processo legge i dati ma non li elabora correttamente, non è possibile rileggere il messaggio. Inoltre, se un processo termina senza leggere i dati, questi vengono persi.
- **Sincronizzazione manuale nei processi complessi**: sebbene ci sia sincronizzazione implicita, in scenari complessi potrebbe essere necessario gestire manualmente la sincronizzazione tra processi per evitare race condition%%link%% o blocchi inutili.
- **Non adatte per grandi quantità di dati**: le pipe sono ideali per il passaggio di piccoli blocchi di dati. Quando è necessario trasferire grandi quantità di dati o file complessi, l'uso delle pipe diventa inefficiente rispetto ad altri metodi di comunicazione tra processi come la [memoria condivisa](Memoria%20condivisa.md).

# 4 - Named pipe

Le **named pipe** (anche chiamate _**FIFO**_ per il loro comportamento) sono una versione più avanzata delle cosiddette _pipe anonime_ o _pipe convenzionali_, cioè le pipe ordinarie: a differenza di quest'ultime, infatti, le named pipe possono essere utilizzate anche tra processi non legati da una relazione padre-figlio e sono bidirezionali. Vengono create con il comando `mkfifo` o la chiamata di sistema `mkfifo()`.

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

# Fonti

- Abraham Silberschatz, Peter Baer Galvin, Greg Gagne - [Sistemi Operativi (10ᵃ Edizione)](https://he.pearson.it/catalogo/1099) - Pearson, 2019 - ISBN: `9788891904560`.
- Slide del Prof. Aldinucci Marco del corso di Sistemi Operativi (canale B), Corso di Laurea in Informatica presso l'Università di Torino, A.A. 2024-25:
	- [Cap_03](https://informatica.i-learn.unito.it/mod/resource/view.php?id=253884)
