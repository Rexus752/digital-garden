---
draft: true
---
Ogni processo%%link%% ha associato un array di stringhe che contiene l’elenco delle variabili d'ambiente.
Ogni elemento dell’array ha la forma `nome=valore` (esempi: HOME, LOGNAME, PATH, ...)
Ogni volta che un processo%%link%% viene creato%%link alla creazione del processo%%, eredita le variabili di ambiente del processo padre.

# Accesso alle variabili di ambiente

## Variabile `environ`

All’interno di un programma C, la lista delle variabili di ambiente può essere consultato usando la variabile globale

```c
char **environ
```

La variabile `environ` è un `NULL`-terminated array: è cioè un array di stringhe (che sono a loro volta array di caratteri), in cui l'ultimo elemento dell'array non è una stringa ma un puntatore a `NULL`.

Per usarlo:
```c
#include <unistd.h>

extern char **environ;

// di qui in poi è possibile utilizzare
// environ
```

## Funzione `getenv`

La funzione
```c
char *getenv(const char *name)
```

Restituisce la stringa della variabile di ambiente passata come parametro

# Fonti

- Slide del Prof. Schifanella Claudio del corso di Laboratorio di Sistemi Operativi (canale B, turno T4), Corso di Laurea in Informatica presso l'Università di Torino, A.A. 2024-25:
	- [Slide: ripasso su direttive, programmazione modulare, utility make](https://informatica.i-learn.unito.it/mod/resource/view.php?id=253526)