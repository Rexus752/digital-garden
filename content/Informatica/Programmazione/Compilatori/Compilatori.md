---
aliases:
  - Compilatori
---

> [!premessa]+ Premessa
> 
> Ciao! Se è la prima volta che capiti su questo sito, ti consiglio di consultare la [pagina principale](index.md) di questo _Giardino Digitale_ per scoprire meglio cos'è e come navigarlo.
> 
> Lo stato di questa nota è al momento: 🔴 <font color="#FF7F7F">_Bozza_</font>.

%% 
https://it.wikipedia.org/wiki/Ricompilazione_dinamica
%%

---

All'alba dei tempi della [programmazione](Programmazione.md#^definizione-programmazione) (ossia intorno agli anni '40/'50), i [programmi](Informatica.md#^definizione-programma) venivano scritti direttamente in linguaggio macchina%% Link %% poiché non esistevano ancora i [linguaggi di programmazione](Programmazione.md#^definizione-linguaggio-di-programmazione): la [programmazione](Programmazione.md#^definizione-programmazione) era ovviamente molto difficile perché per noi umani non è semplice dover tradurre le [istruzioni](Informatica.md#^definizione-istruzione) che vogliamo far eseguire a un [computer](Informatica.md#^definizione-computer) in una sequenza di zeri e uno, tenendo anche conto del fatto che ogni [computer](Informatica.md#^definizione-computer) ha una propria architettura%% Link %% e, di conseguenza, un programma scritto per una determinata architettura non funzionerà su ogni computer.

Per questo motivo sono stati inventati i [_linguaggi di programmazione_](Programmazione.md#^definizione-linguaggio-di-programmazione), ossia linguaggi che ci permettono di scrivere [programmi](Informatica.md#^definizione-programma) in un formato più _leggibile_ a noi umani (usando parole inglesi al posto di `0` e `1`).

Tuttavia c'è un problema: un [computer](Informatica.md#^definizione-computer) è in grado di comprendere solo il proprio linguaggio macchina%% Link %% e non capisce i [linguaggi di programmazione](Programmazione.md#^definizione-linguaggio-di-programmazione). Ecco che allora serve un "traduttore" che prenda i [programmi](Informatica.md#^definizione-programma) scritti in un determinato [linguaggio di programmazione](Programmazione.md#^definizione-linguaggio-di-programmazione) e li trasformi in un altro [linguaggio](Programmazione.md#^definizione-linguaggio-di-programmazione) (per esempio il linguaggio macchina%% Link %%): questi "traduttori" sono detti [_compilatori_](Compilatori.md#^definizione-compilatore).

%% 
Introdurre in questa definizione "codice sorgente" e "codice macchina"
%%

> [!definizione]+ Definizione: compilatore
> 
> Un **compilatore** è un [programma](Informatica.md#^definizione-programma) che traduce del codice%% link %% scritto in un certo [linguaggio di programmazione](Programmazione.md#^definizione-linguaggio-di-programmazione) in un altro [linguaggio di programmazione](Programmazione.md#^definizione-linguaggio-di-programmazione).
^definizione-compilatore

%% 
codice = sequenza di [istruzioni](Informatica.md#^definizione-istruzione)
%%

> [!osservazione]+ Osservazione: a cosa serve studiare i compilatori?
> 
> Al giorno d'oggi (quasi) nessuno realizza più [compilatori](Compilatori.md#^definizione-compilatore) (eccetto se si sta inventando un nuovo [linguaggio di programmazione](Programmazione.md#^definizione-linguaggio-di-programmazione)), ma allora a cosa serve studiarli?
> 
> Innanzitutto, come per qualsiasi altra cosa nel mondo dell'[informatica](Informatica.md#^definizione-informatica) (e non solo), concetti e metodi studiati qua possono essere applicati anche in altri ambiti, come la lettura e l'analisi di [dati](Informatica.md#^definizione-dato) organizzati in strutture dati%% link %%, lo studio di linguaggi formali%% link %%, ecc.

# 1 - Dal sorgente all'eseguibile

Oltre ai compilatori, molti altri programmi possono essere necessari per ottenere un eseguibile:
- Un programma sorgente può essere diviso in moduli conservati in file separati e chi riordina questi file è il preprocessore, che per esempio può anche risolvere macro
- Il codice sorgente modificato dal preprocessore viene dato in pasto al compilatore che produce l'assembly
- L'assembly viene processato dall'assembler che produce _relocatable machine code_
- Il linker risolve gli indirizzi di memoria esterna che nel codice fa riferimento a librerie esterne
- Il loader monta insieme i pezzi di  _relocatable machine code_ e librerie in un unico eseguibile

# 2 - Fasi della compilazione

Un compilatore non è un unico, ma diviso in due parti principali: analisi e sintesi.

Nella parte di analisi spezzetta il codice sorgente in più pezzi su cui fa controlli della correttezza della sua scrittura (e nel caso segnalare eventuali errori così che l'utente possa risolverli) e crea una _symbol table_ in cui conserva i dati iniziali.

Nella parte di sintesi costruisce il programma destinazione dai risultati della parte di analisi.

Un [compilatore](Compilatori.md#^definizione-compilatore) è diviso in più fasi:
1. Fa l'analisi lessicale, generando i token
2. Fa l'analisi sintattica, generando AST
3. Fa l'analisi semantica, generando AST
4. Genera il codice intermedio
5. Ottimizza il codice intermedio
6. Genera il codice oggetto

Alcuni compilatori distinguono l'ottimizzazione tra machine-independent (cioè ottimizzazione che riguarda unicamente il codice in sè) e machine-dependent (cioè ottimizzazione specifica per la macchina su cui sta venendo eseguito).

## 2.1 - Analisi lessicale

%% 
https://en.wikipedia.org/wiki/Lexical_analysis
%%

> [!definizione]+ Definizione: analisi lessicale
> 
> L'**analisi lessicale** è una delle fasi della [compilazione](Compilatori.md#^definizione-compilatore) in cui il codice%% link %% viene convertito in blocchi chiamati [token](Compilatori.md#^definizione-token). Il [programma](Informatica.md#^definizione-programma) che effettua questa operazione è detto **analizzatore lessicale** (in inglese **lexer** o **scanner**).
^definizione-analisi-lessicale

> [!definizione]+ Definizione: token
> 
> Un **token** è una struttura dati%% link %% prodotta dall'[analisi lessicale](Compilatori.md#^definizione-analisi-lessicale) composta da una **categoria lessicale**, che identifica il tipo di elemento riconosciuto, e da un eventuale **lessema**, ovvero la sequenza specifica di caratteri%% link %% del codice sorgente%% link %% che corrisponde al token, sotto forma di riferimento alla relativa entry%% Link %% nella [tabella dei simboli](Compilatori.md#^definizione-tabella-dei-simboli).
^definizione-token

> [!osservazione]+ Osservazione: facoltatività dei lessemi
> 
> Nella [definizione di _token_](Compilatori.md#^definizione-token) c'è scritto "eventuale lessema" perché, a seconda dell'implementazione, un [token](Compilatori.md#^definizione-token) può non conservare esplicitamente la sequenza originale di caratteri: per esempio, un [token](Compilatori.md#^definizione-token) che nel linguaggio C%% link %% ha come [categoria](Compilatori.md#^definizione-token) "operatore di assegnazione" non può avere un [lessema](Compilatori.md#^definizione-token) diverso da `=`, motivo per cui quest'ultimo può essere omesso.

> [!definizione]+ Definizione: tabella dei simboli
> 
> La **tabella dei simboli** (in inglese **symbol table**) è una struttura dati%% link %% utilizzata dal [compilatore](Compilatori.md#^definizione-compilatore) per memorizzare i [lessemi](Compilatori.md#^definizione-token) dell'[analisi lessicale](Compilatori.md#^definizione-analisi-lessicale) e associarli ai corrispettivi [token](Compilatori.md#^definizione-token).
^definizione-tabella-dei-simboli

Per capire esattamente come sono collegati tra loro i concetti di [_token_](Compilatori.md#^definizione-token), [_lessemi_](Compilatori.md#^definizione-token) e [_tabella dei simboli_](Compilatori.md#^definizione-tabella-dei-simboli), vediamo un esempio.

> [!esempio]- Esempio di analisi lessicale
> 
> Prendiamo per esempio un codice sorgente%% link %% in C%% link %% che contiene la seguente assegnazione%% Link %%:
> 
> ```c
> position = initial + rate * 60
> ```
> 
> L'[analizzatore lessicale](Compilatori.md#^definizione-analisi-lessicale) spezzetterà questo codice%% link %% nei [lessemi](Compilatori.md#^definizione-token) `position`, `=`, `initial`, `+`, `rate`, `*` e `60` e farà le seguenti valutazioni, tenendo in mente che i nomi usati per le [categorie](Compilatori.md#^definizione-token) sono puramente arbitrari e potrebbero non corrispondere a reali implementazioni di [analizzatori](Compilatori.md#^definizione-analisi-lessicale):
> - **`position`** è un [lessema](Compilatori.md#^definizione-token) che verrà associato al [token](Compilatori.md#^definizione-token) $\langle \texttt{id}, 0 \rangle$ dove $\texttt{id}$ indica la [categoria](Compilatori.md#^definizione-token) degli _identificatori_%% link %% e $0$ è la posizione a cui è memorizzata l'entry%% Link %% `position` nella [tabella dei simboli](Compilatori.md#^definizione-tabella-dei-simboli).
> - **`=`** è un [lessema](Compilatori.md#^definizione-token) che verrà associato al [token](Compilatori.md#^definizione-token) $\langle \texttt{=} \rangle$ ma, dal momento che il [token](Compilatori.md#^definizione-token) non può avere altri valori%% link %% al di fuori di `=`, non è necessario associarci un'entry%% link %% nella [tabella dei simboli](Compilatori.md#^definizione-tabella-dei-simboli).
> - **`initial`** è un [lessema](Compilatori.md#^definizione-token) che verrà associato al [token](Compilatori.md#^definizione-token) $\langle \texttt{id}, 1 \rangle$ dove $1$ è la posizione a cui è memorizzata l'entry%% Link %% `initial` nella [tabella dei simboli](Compilatori.md#^definizione-tabella-dei-simboli).
> - **`+`** è un [lessema](Compilatori.md#^definizione-token) che verrà associato al [token](Compilatori.md#^definizione-token) $\langle \texttt{+} \rangle$.
> - **`rate`** è un [lessema](Compilatori.md#^definizione-token) che verrà associato al [token](Compilatori.md#^definizione-token) $\langle \texttt{id}, 2 \rangle$ dove $2$ è la posizione a cui è memorizzata l'entry%% Link %% `rate` nella [tabella dei simboli](Compilatori.md#^definizione-tabella-dei-simboli).
> - **`*`** è un [lessema](Compilatori.md#^definizione-token) che verrà associato al [token](Compilatori.md#^definizione-token) $\langle \texttt{*} \rangle$.
> - **`60`** è un [lessema](Compilatori.md#^definizione-token) che verrà associato al [token](Compilatori.md#^definizione-token) $\langle \texttt{num}, 3 \rangle$ dove $\texttt{num}$ indica la [categoria](Compilatori.md#^definizione-token) dei _numeri_%% link %% e $2$ è la posizione a cui è memorizzata l'entry%% Link %% `60` nella [tabella dei simboli](Compilatori.md#^definizione-tabella-dei-simboli).
> 
> Potremmo rappresentare graficamente questa [analisi lessicale](Compilatori.md#^definizione-analisi-lessicale) così:
> 
> ![Esempio di analisi lessicale.drawio](Esempio%20di%20analisi%20lessicale.drawio.svg)

%% 
per il [lessema](Compilatori.md#^definizione-token) `60` vedere nota a fine capitolo 1 di Aho e capire cosa vuol dire
%%

# 3 - Interpreti

Un altro tipo di [programmi](Informatica.md#^definizione-programma) che manipolano il codice%% link %% sono gli [_interpreti_](Compilatori.md#^definizione-interprete).

> [!definizione]+ Definizione: interprete
> 
> Un **interprete** è un [programma](Informatica.md#^definizione-programma) che, dato un codice%% link %%, lo esegue%% link %% direttamente senza doverlo [compilare](Compilatori.md#^definizione-compilatore).
^definizione-interprete

Il codice macchina%% link %% prodotto da un [compilatore](Compilatori.md#^definizione-compilatore) è spesso molto più veloce da eseguire%% link %% rispetto a un [interprete](Compilatori.md#^definizione-interprete) che lo esegue%% link %% direttamente, ma quest'ultimo può essere in grado di rilevare errori molto meglio di un [compilatore](Compilatori.md#^definizione-compilatore) perché esegue le [istruzioni](Informatica.md#^definizione-istruzione) del codice sorgente%% Link %% una per volta.

> [!esempio]- Esempio: compilazione e interpretazione di Java
> 
> Gli elaboratori%% Link %% per il [linguaggio](Programmazione.md#^definizione-linguaggio-di-programmazione) Java%% link %% combinano [compilatori](Compilatori.md#^definizione-compilatore) e [interpreti](Compilatori.md#^definizione-interprete): un codice sorgente%% Link %% scritto in Java viene prima [compilato](Compilatori.md#^definizione-compilatore) in un formato intermedio chiamato _bytecode_%% link %% e poi quest'ultimo viene [interpretato](Compilatori.md#^definizione-interprete) da una macchina virtuale%% link %%.
> 
> Il vantaggio di ciò è che il bytecode%% link %% [compilato](Compilatori.md#^definizione-compilatore) su una [macchina](Informatica.md#^definizione-computer) può essere [interpretato](Compilatori.md#^definizione-interprete) su una [macchina](Informatica.md#^definizione-computer) diversa.

%% 
mettere nell'esempio schemino 1.4 del libro Compilers
%%

# 4 - Compilatori just-in-time

> [!definizione]+ Definizione: compilatore just-in-time (JIT)
> 
> Un [compilatore](Compilatori.md#^definizione-compilatore) è detto **just-in-time (JIT)** se compila durante l'esecuzione%% link %% del [programma](Informatica.md#^definizione-programma) anziché precedentemente.
^definizione-compilatore-just-in-time-jit

%% L'obiettivo finale è combinare i vantaggi della compilazione del bytecode a quelli della compilazione nativa, aumentando le prestazioni quasi al pari di una compilazione direttamente in linguaggio macchina. %%

---

> [!fonti]+ Fonti
> 
> - 🏫 Corso di Laurea in Informatica (`L-31 R`) presso l'Università di Torino:
>     - Corso di _Linguaggi Formali e Traduttori_ (`INF0344`), A.A. 2026-27 ([pagina Moodle](https://informatica.i-learn.unito.it/course/view.php?id=3735)):
> 		- Prof. Jeremy James Sproston, slide del corso:
> 			- [1.1 - _Motivazione_](https://informatica.i-learn.unito.it/pluginfile.php/510313/mod_folder/content/0/1-1_motivazione.pdf).
> 			- [1.2 - _Organizzazione_](https://informatica.i-learn.unito.it/pluginfile.php/510313/mod_folder/content/0/1-2_organizzazione.pdf).
> - 📚 Alfred V. Aho, Monica S. Lam, Ravi Sethi, Jeffrey D. Ullman, [_Compilers - Principles, Techniques, and Tools_](https://openlibrary.org/books/OL59750369M/Compilers), Pearson India, 2023 (ISBN: `9789357054119`):
> 	- Chapter 1 - _Introduction_.
> 		- Paragraph 1.1 - _Language Processors_.
> 		- Paragraph 1.2 - _The Structure of a Compiler_:
> 			- Paragraph 1.2.1 - _Lexical Analysis_.
