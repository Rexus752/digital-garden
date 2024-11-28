---
draft: false
---
Tutte le variabili e le funzioni del C hanno 2 attributi: il tipo e la classe di memorizzazione.

Le 4 classi di memorizzazione possibili sono le seguenti:
- `auto`
- `extern`
- `register`
- `static`

# Classe `auto`

È la classe di memorizzazione di default e quindi può essere omessa.

All’ingresso in un blocco il sistema alloca memoria per le variabili automatiche; pertanto tali variabili sono considerate locali al blocco.
All’uscita dal blocco, il sistema libera la memoria assegnata alle variabili automatiche, causando la perdita dei loro valori.
Al rientro nel blocco, il sistema alloca nuovamente la memoria senza però recuperare i valori precedenti.

# Classe `extern`

Variabili definite e allocate in altri file:
• Un altro programma
• Il Sistema Operativo
• altro
Anche le funzioni possono essere definite `extern`.

Esempio: `extern int var`: il compilatore assume che questa variabile esiste (e non alloca spazio
per essa)

Il linker può generare un errore

# Classe `register`

Classe di memorizzazione che ha come obiettivo l’aumento della velocità di esecuzione.

Segnala al compilatore che la variabile corrispondente dovrebbe essere memorizzata in registri di memoria ad alta velocità: qualora il compilatore non possa allocare un registro fisico, viene utilizzata la classe `auto`%%link%% (il compilatore dispone solo di una parte dei registri, che possono invece essere utilizzati dal sistema).

Quando la velocità è importante, il programmatore può scegliere poche variabili alle quali viene fatto più frequentemente accesso (per esempio, variabili di ciclo e parametri delle funzioni).

La variabile di classe `register` è di norma dichiarata nel punto più vicino possibile al punto in cui viene utilizzata, per consentire la massima disponibilità di registri fisici, utilizzati solo quando necessario.

Esempio:

```c
register int i;

for(i = 0; i < LIMIT; ++i) {
	/* codice */
}
```

# Classe `static`

Servono per permettere a una variabile locale di mantenere il valore precedente al rientro in un blocco

Esempio:

```c
void counter() {
	static int count = 0;
	++count;
}
```

Alla prima chiamata della funzione `counter`, la variabile `count` viene inizializzata a `0`, ma alle chiamate successive non viene più inizializzata, ma mantiene il valore che aveva alla precedente chiamata di funzione

# Classe `static extern`

Questo tipo di classe di memorizzazione fornisce meccanismo di "privatezza" (insieme di restrizioni sulla visibilità di variabili o funzioni che sarebbero altrimenti accessibili) fondamentale per la modularità dei programmi.

Le variabili statiche esterne sono variabili esterne con visibilità ristretta: sono accessibili dal resto del file in cui sono dichiarate, ma non sono disponibili:
- alle funzioni precedentemente definite all’interno del file
- alle funzioni definite all’interno di file differenti

```c
void function1() {
	// v non disponibile
}

static int v;

void function2() {
	// v disponibile
}
```

L’idea è cioè di disporre di una variabile globale per una famiglia di funzioni, e al contempo privata per il file

# Classi di memorizzazione e valore di default

Sia le variabili statiche (di classe `static`%%link%%) sia quelle esterne (di classe `extern`%%link%%) non inizializzate esplicitamente vengono inizializzate a zero dal sistema. Anche array, stringhe, puntatori, strutture e union subiscono lo stesso trattamento: per array e stringhe ogni elemento viene posto a zero.

Al contrario, normalmente le variabili automatiche (di classe `auto`%%link%%) e variabili registro (du classe `register`%%link%%) non vengono inizializzate dal sistema, e quindi contengono inizialmente valori «sporchi»%%specificare cosa si intende per "sporchi"%%

# Allocazione delle variabili

Normalmente, le variabili sono salvate in memoria
• BSS (Block Standard by Symbol)
• Stack
• Heap

Inoltre, possono essere salvate nei registri (come nel caso delle variabili di classe `register`%%link%%)

![](Pasted%20image%2020241117182747.png)

## I segmenti di memoria

Il sistema operativo è responsabile dell’assegnamento di alcuni segmenti di memoria ad ogni processo.
I segmenti di memoria sono mappati nello spazio di indirizzamento del processo. Ogni segmento ha:

• Indirizzo di inizio e di fine
• Flags che determinano le modalità di accesso (es. read, write, execute (contiene il codice), privato/condiviso)

%%
```
ps –aux | grep <nome_processo>
cat /proc/<pid>/maps
```
%%

## Variabili nel BSS

Segmento di memoria read/write. Dimensione decisa a tempo di compilazione. Vi sono memorizzate:
• Variabili globali
• Variabili locali static

Allocate all’inizio del programma, deallocate alla fine del programma

## Variabili nello stack

Variabili dichiarate all’interno di una funzione (compresi i parametri). Viene modificato lo stack pointer

Allocate all’inizio della funzione, deallocate quando la funzione termina

%%collegamento con architetture%%

## Variabili nello heap

Allocazione dinamica, decisa a runtime. Utilizzato quando si richiede uno spazio di memoria per una variabile attraverso le primitive come

```c
void *malloc(size_t size);
```

```c
void *calloc(size_t nmemb, size_t size);
```

```c
void *realloc(void *ptr, size_t size);
```
%%vedere online se i nomi dei parametri sono corretti%%

NB: la memoria allocata dinamicamente va deallocata con
```c
void free(void *ptr);
```

# Fonti

- Slide del Prof. Schifanella Claudio del corso di Laboratorio di Sistemi Operativi (canale B, turno T4), Corso di Laurea in Informatica presso l'Università di Torino, A.A. 2024-25:
	- [Slide: ripasso su direttive, programmazione modulare, utility make](https://informatica.i-learn.unito.it/mod/resource/view.php?id=253526)