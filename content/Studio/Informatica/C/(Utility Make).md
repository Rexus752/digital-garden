---
draft: true
---
La Make utility è uno strumento che può essere utilizzato per automatizzare il processo di compilazione.

In generale è più flessibile degli ambienti integrati (IDE, integrated development environments) e si basa sull’utilizzo di un file (chiamato makefile) che descrive le dipendenze presenti nel progetto.

È quindi possibile utilizzare il comando make che si avvale della marcatura temporale dei files e ricompila i target file che sono più vecchi dei sorgenti, cioè ricompila solo file aggiornati.

# Regole implicite

Se non vi sono regole esplicite definite (vedi slide successive), make tenta di creare un eseguibile cercando il file «test.c» oppure «test.o»

```bash
gcc test.c –o test
```

Possibile anche solamente la compilazione senza il linking con

```bash
make test.o
```

# Regole esplicite

Il makefile elenca un insieme di target rules: regole per la compilazione e l’istruzione da eseguire per compilare a partire dai sorgenti

```makefile
nome_target: file1.o file2.o filen.o
	gcc -o nome_target file1.o file2.o filen.o

file1.o: file1.c file1.h
	gcc -c file1.c
...
filen.o: filen.c filen.h
	gcc -c filen.c

clean:
	rm –f *.o
```

e si esegue con `make nome_target`

Nell’invocare make da linea di comando è possibile specificare quale target compilare es.

```bash
make file1.o
```

Se viene invocato senza opzione dalla linea di comando, utilizza il target di default, il primo specificato nel makefile

Nell’esempio qua sotto, per cancellare tutti i file oggetto usare `make clean`

```makefile
nome_target: file1.o file2.o filen.o
	gcc -o nome_target file1.o file2.o filen.o
...
clean:
	rm –f *.o
run:
	./nome_target
```

# Variabili d'ambiente

Si possono definire alcune variabili di ambiente (anche internamente al makefile) per definire:
- CC: il comando da usare per il compilatore (`export CC="gcc"`)
- CFLAGS: i flags da usare durante la compilazione (`export CFLAGS= "-std=c89 -pedantic"`)
- LDFLAGS: i flags per la fase di linking (`export LDFLAGS= "-lm"`)

# Esercizio

- Creare un makefile per l’esercizio precedente
- Verificare che su invocazioni consecutive di make, vengono compilati solamente i file effettivamente modificati
- Per modificare un file in maniera «fittizia» usare il comando
```
touch <nomefile>
```

# Esercizio

Creare un programma che:
- Stampa la lista delle variabili di ambiente definite
- prende in input il nome di una variabile di ambiente e stampa a video il suo valore
- Il programma deve anche controllare la presenza del parametro prima di procedere con la ricerca della variabile di ambiente

# Fonti

- Slide del Prof. Schifanella Claudio del corso di Laboratorio di Sistemi Operativi (canale B, turno T4), Corso di Laurea in Informatica presso l'Università di Torino, A.A. 2024-25:
	- [Slide: ripasso su direttive, programmazione modulare, utility make](https://informatica.i-learn.unito.it/mod/resource/view.php?id=253526)