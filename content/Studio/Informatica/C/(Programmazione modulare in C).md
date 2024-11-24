---
draft: true
---
Al giorno d’oggi, i progetti software sono complessi e composti da moltissime righe di codice e si basano sul riuso di funzionalità (librerie) scritte da altri programmatori.

Avere quindi il codice di un programma scritto su un unico file è impraticabile. Una piccola modifica in un unico punto non può obbligare ad una ricompilazione di tutto il progetto

Ecco quindi la necessità di raggruppare le funzioni che si occupano di una specifica funzionalità in un unico file sorgente, detto _modulo_. Un modulo è composto da:
- Interfaccia (header file, file di intestazione, con estensione `.h`)
	- Lista delle funzioni e dei tipi di dato del modulo
	- Viene incluso in ogni modulo/applicazione che lo usa (con la direttiva `#include`%%link%%)
	- Non deve essere mai compilato
- Implementazione (file con estensione `.c`)
	- Codice che implementa le funzioni contenute nell’header file
	- Codice che implementa le funzioni interne che non sono esposte nell’interfaccia
	- Non contiene la funzione `main()`
	- Compilato con `gcc –c` e produce un file oggetto `.o`

Applicazione dei moduli:
- Utilizza uno o più moduli includendo i corrispondenti header file
- Deve contenere la funzione `main()`
- Compilato e linkato con il file oggetto dei moduli

# Esempio

File `applicazione.c`:
```c
#include “operations.h”

int main(void) {

	int i = 3;
	int j = 5;
	
	printf("i + j = %d\n", add(i, j));
	printf("i * j = %d\n", multiply(i, j));
}
```

File `operations.h`:
```c
int add(int addend1, int addend2);
int multiply(int factor1, int factor2);
```

File `operations.c`:
```c
#include "operations.h"

int add(int addend1, int addend2) {
	return addend1 + addend2;
}

int multiply(int factor1, int factor2) {
	return factor1 * factor2;
}
```

# Esercizio

Scrivere un programma che dati due numeri interi passati come argomenti, restituisca la loro somma e la loro moltiplicazione

Organizzare il codice in tre componenti separati:
• Modulo che contiene la funzione per la somma
• Modulo che contiene la funzione per la moltiplicazione
• Applicazione che contiene il main e sfrutta le funzioni dei primi due moduli

Soluzione:

![](Soluzione.png)

# Compilazione dei moduli

I singoli moduli, cioè i file `.c` possono essere compilati in file oggetto specificando il parametro `-c`.

Esiste una dipendenza fra i file `.h` e il file `.c` che li include: se un file di intestazione (header) cambia, allora i moduli dipendenti devono essere ricompilati.

```bash
gcc -c somma.c
gcc -c prodotto.c
gcc -c applicazione.c
gcc somma.o prodotto.o allicazione.o -o applicazione
```

# Ciclicità delle dipendenze

![](Ciclicità%20delle%20dipendenze.png)

Soluzione:

![](Soluzione%20ciclicità.png)

# Utility make

Se il progetto consiste di centinaia di files, può tuttavia essere utile la compilazione separata: ma come determinare quali moduli ricompilare?

Dimenticando di ricompilarne qualcuno, può capitare che il linker generi errori nel tentare di utilizzare un file oggetto obsoleto; peggio, se la signature non cambia, l’errore non sarà segnalato preventivamente, provocando errori a runtime.

Possiamo risolvere tali problemi con l’utility make.%%link%%

# Fonti

- Slide del Prof. Schifanella Claudio del corso di Laboratorio di Sistemi Operativi (canale B, turno T4), Corso di Laurea in Informatica presso l'Università di Torino, A.A. 2024-25:
	- [Slide: ripasso su direttive, programmazione modulare, utility make](https://informatica.i-learn.unito.it/mod/resource/view.php?id=253526)