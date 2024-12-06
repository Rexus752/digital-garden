**GDB** (acronimo di _**G**NU **D**e**b**ugger_) è un software sviluppato come parte del progetto GNU%%link%% che permette di eseguire il **debugging** di altri programmi, aiutando i programmatori a identificare e correggere errori nel loro codice. È progettato principalmente per linguaggi come C e C++, ma supporta anche altri linguaggi come Fortran, Assembly e Rust.

# 1 - Caratteristiche principali di GDB

Le caratteristiche principali di GDB sono:
- **Debugging interattivo**: è possibile seguire passo-passo l'esecuzione di un programma per comprendere il flusso del codice e identificare gli errori.
- **Breakpoints**: si possono impostare punti di interruzione nel codice detti _breakpoints_ per fermare l'esecuzione in punti specifici.
- **Analisi e modifica delle variabili**: con GDB si può esaminare il contenuto di variabili e strutture dati durante l'esecuzione, ma anche modificare il valore delle variabili mentre il programma è in esecuzione.
- **Backtrace e analisi dello stack**: è possibile visualizzare la sequenza delle chiamate di funzione attive (detta _call stack_) per risalire facilmente all'origine di un errore nel programma.
- **Core dump**: GDB permette di caricare un core dump per analizzare il motivo del crash del programma e fornisce informazioni come lo stato della memoria e i registri al momento del crash.

# 2 - Come usare GDB%% per il c (?)%%

## 2.1 - Compilazione di un programma in C con supporto al debugging

Per usare GDB, nella compilazione del codice sorgente di un programma scritto in C con GCC%%link%% è consigliato:
- Usare l'opzione `-g` per includere informazioni di debug nel file eseguibile generato durante la compilazione, in modo che GDB sia in grado di interpretare meglio il codice sorgente e di collegare le istruzioni eseguibili alle righe di codice originali
- Usare l'opzione `-O0` per disabilitare tutte le ottimizzazioni del compilatore durante la compilazione del codice: il codice viene compilato "così com'è" e ogni istruzione corrisponde direttamente a una riga del codice sorgente.

Quindi, per compilare un file di codice sorgente in C con il supporto al debugging per GDB, si dovrà usare il seguente comando:

```shell
gcc -g -O0 <nome-file-sorgente> -o <nome-eseguibile>
```

Una volta compilato il programma, per eseguirlo usare il comando:

```shell
gdb <nome-eseguibile>
```

In questo comando non vanno specificati gli argomenti%%link%% con cui eseguire il programma, perché verranno dichiarati successivamente durante l'esecuzione del programma all'interno del GDB.

A questo punto, verrà avviato il prompt interattivo di GDB in cui inserire i comandi.

## 2.2 - Principali comandi di GDB

- **`help` (alias: `h`)**: elenca i comandi a disposizione.
	- **`help all`**: elenca la lista completa di tutti i comandi a disposizione.
	- **`help <nome-comando>`**: illustra la documentazione completa di un singolo comando.
- **`list` (alias: `l`)**: mostra una porzione del codice sorgente del programma. Eseguendolo più volte, mostra porzioni successive.
	- **`list <numero-riga>`**: mostra il codice sorgente attorno alla riga specificata.
	- **`list <nome-funzione>`**: mostra il codice della funzione specificata.
	- **`list .`**: mostra le prime righe del codice sorgente.
- **`info <sotto-comando>` (alias: `i <sotto-comando>`)**: mostra informazioni sul programma che si sta debuggando, in particolare su ciò che viene specificato nel `<sotto-comando>`.
- **`quit` (alias: `q`)**: termina l’esecuzione di GDB.

### 2.2.1 - Avvio ed esecuzione di un programma

- **`run` (alias: `r`)**: avvia il programma e lo esegue al primo breakpoint (se ce ne sono).
	- **`run <argomenti>`**: avvia il programma e lo esegue con gli argomenti%%link%% specificati.
- **`start`**: avvia il programma, ma si ferma alla prima istruzione eseguibile.
- **`continue` (alias: `c`)**: prosegue l’esecuzione del programma fino al breakpoint successivo (se ce ne sono).
- **`kill` (alias: `k`)**: termina il programma in esecuzione.

### 2.2.2 - Navigazione nel codice

- **`next` (alias: `n`)**: esegue una linea di codice e, se si tratta di una chiamata di una funzione, la esegue interamente.
- **`step` (alias: `s`)**: esegue una linea di codice e, se si tratta di una chiamata di una funzione, entra nel codice della funzione senza eseguirla interamente.
- **`finish`**: finisce di eseguire la funzione corrente.
- **`jump <numero-riga>` (alias: `j <numero-riga>`)**: salta a una specifica riga di codice e prosegue l’esecuzione del programma fino al breakpoint successivo (se ce ne sono).

### 2.2.3 - Breakpoints

- **`break <numero-riga>` (alias: `b <numero-riga>`)**: inserisce un breakpoint alla riga indicata.
	- **`break <nome-file-sorgente>:<numero-riga>`**: inserisce un breakpoint alla riga specificata all'interno del file `<nome-file-sorgente>` (utile nel caso in cui si stia debuggando un programma composto da più file sorgente).
- **`info breakpoints` (alias: `i b`)**: mostra la lista dei breakpoint definiti, a ognuno dei quali è stato associato un ID (visibile nella colonna `Num`).
- **`clear <numero-riga>` (alias: `cl <numero-riga>`)**: elimina il breakpoint alla riga specificata.
- **`delete <id>` (alias: `d <id>`)**: elimina il breakpoint con ID `<id>`.
- **`disable <id>` (alias: `dis <id>`) ed `enable <id>` (alias: `en <id>`)**: disattiva (senza eliminarlo) o riattiva il breakpoint con ID `<id>`.

### 2.2.4 - Variabili e stato del programma

- **`print <espressione>` (alias: `p <espressione>`)**: valuta l’espressione e ne stampa il valore.
- **`set <variabile> = <valore>`**: modifica il valore di una variabile.
- **`display <espressione>`**: valuta l’espressione e ne stampa il valore ad ogni step che verrà eseguito.
- **`info display`**: mostra la lista dei display definiti, a ognuno dei quali è stato associato un ID (visibile nella colonna `Num`).
- **`undisplay <id>`**: rimuove il display con ID `<id>`.
- **`info locals`**: mostra tutte le variabili locali e i loro relativi valori.

### 2.2.5 - Call stack e funzioni

- **`backtrace` (alias: `bt`, `where`)**: mostra la sequenza delle chiamate attive (detta _call stack_).
- **`frame <id>` (alias: `f <id>`)**: passa al frame con ID `<id>` nel call stack.
- **`up` e `down`**: per muoversi su o giù all'interno del call stack.

%%
# Fork e gdb

È possibile connettere gdb ad un processo in esecuzione:
```shell
gdb –p <PID>
```

Se il processo sta eseguendo una system call, potrebbe essere necessario eseguire come superuser con sudo
```shell
sudo gdb –p <PID>
```

Domanda: se sto facendo debug di un processo che successivamente esegue una fork, quale dei due processi sarà oggetto di debug?
Risposta: In gdb utilizzare uno dei due comandi
- `set follow-fork-mode parent`
- `set follow-fork-mode child`
%%

# Fonti

- Slide del Prof. Schifanella Claudio del corso di Laboratorio di Sistemi Operativi (canale B, turno T4), Corso di Laurea in Informatica presso l'Università di Torino, A.A. 2024-25:
	- [Slide: gdb](https://informatica.i-learn.unito.it/mod/resource/view.php?id=254492
%%
Da vedere:
- https://en.wikipedia.org/wiki/GNU_Debugger
- https://didawiki.cli.di.unipi.it/lib/exe/fetch.php/informatica/sol/laboratorio18/esercitazionib/gdb_valgrind.pdf
%%
