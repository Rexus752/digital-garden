
> [!premessa]+ Premessa
> 
> Ciao! Se è la prima volta che capiti su questo sito, ti consiglio di consultare la [pagina principale](index.md) di questo cosiddetto _Giardino Digitale_ per scoprire meglio cos'è e come navigarlo.
> 
> Lo stato di questa nota è al momento: 🔴 <font color="#FF7F7F">_Bozza_</font>.

---

> [!definizione]+ Definizione: paradigma funzionale
> 
^definizione-paradigma-funzionale

# 1 - Programmazione funzionale

Ha le sue basi negli anni '30, ancor prima che venissero creati i primi calcolatori elettronici.

Il lambda calcolo piccolissimo linguaggio di programmazione che permette di "calcolare" con le funzioni così come si calcola con i numeri

Visione estrema: qualsiasi cosa è una funzione

## 1.1 - LISP

Negli anni '50 viene sviluppato il primo vero e proprio linguaggio di programmazione funzionale, cioè eseguibile effettivamente da un compilatore: il LISP (LISt Processor), dà importanza al ruolo chiave delle liste nella programmazione funzionale

Inizialmente concepito per elaborazione non-numerica (ed era una novità, perché i primi linguaggi come FORTRAN erano proprio basati sul calcolo numerico). Primo linguaggio dotato di garbage collector (quindi il programmatore non deve gestire la memoria) e usa la notazione prefissa (con abbondante uso di parentesi) perché è facile da implementare nei parser

## 1.2 - FP

Anni '70 avviene un fatto importantissimo: il sior Backus (lo stesso tizio della BNF, anche uno dei principali sviluppatori e ideatori del FORTRAN, il cui compilatore è un primo esempio di linguaggio imperativo) vince il premio Turing nel 1977 per lo sviluppo del FORTRAN

Dopo la vittoria del premio Turing solitamente si viene invitati a dare una lezione d'onore a un convegno, in cui racconta la genesi o fatti riguardanti il motivo per cui ha vinto il premio: Backus, invece, anziché parlare bene del FORTRAN che gli ha permesso di vincere il premio Turing, critica il paradigma imperativo (che lui definisce "word-at-a-time programming" perché le singole istruzioni fanno poche cose ognuna) e propone in un articolo l'FP, nuovo linguaggio di programmazione funzionale

FP non avrà mai successo ma accende l'interesse per i linguaggi funzionali

## 1.3 - ML

Primo linguaggio funzionale moderno: ML (Meta-Language), inizialmente ideato come strumento ausiliario per un sistema logico, il LCF (Logic for Computable Functions), e poi diventa un linguaggio a se stante

OCaml si fonda su ML aggiungendoci le caratteristiche a oggetti

ML era un linguaggio con inferenza di tipi: il compilatore capisce i tipi da solo senza che il rpogrammatore debba specificarli

Primo linguaggio con polimorfismo parametrico, 30 anni prima dei Java generics

È possibile definire nuovi tipi dal punto di vista del programmatore

Fornisce un meccanismo per analizzare la struttura di liste e altre strutture dati, il _pattern matching_, poi espanso a tutti i linguaggi funzionali successivi

Dotato anche di un sistema di moduli per scomporre i programmi in più sotto-programmi

## 1.4 - Anni '80

Fino agli anni '80 arriva un filone parallelo di linguaggi funzionali detti "lazy", ovvero pigri: questi linguaggi, a differenza dei precedenti, sono linguaggi in cui gli argomenti non vengono valutati finché la funzione non ne ha bisogno:
- SASL introduce guardie e currying
- KRC introduce il costrutto precursore delle list comprehension, ossia una notazione con la quale è possibile costruire liste in modo simile alla notazione di un insieme per caratteristica (es. in KRC `[x^2 | x <- [1..100], odd(x)]` quadrati dei dispari tra 1 e 100)
- Miranda introduce le sezioni, ossia funzioni applicate parzialmente con operatori binari (es. `/ 2` rappresenta la funzione che, dato un argomento `x`, calcola `x` diviso 2)

## 1.5 - Anni '90

Per "istituzionalizzare" questi linguaggi "lazy" viene istituito un comitato scientifico tra i cui membri compare Phil Wadler%% foto di lambda-man %%, per ottenere un linguaggio "lazy" standard: nasce l'Haskell, linguaggio di programmazione puro in cui si usa il sistema di tipi per separare le parti del programma che hanno a che fare con lo stato (ossia l'I/O) dalle parti del programma che rappresentano la computazione pura

L'inferenza dei tipi in Haskell si riconcilia con l'overloading degli operatori e ciò è reso possibile dalle classi di tipo

Nel 2005 riacquista una seconda vita per il suo impatto sul calcolo parallelo, perché in quegli anni ci si rende conto che si stanno raggiungendo i limiti fisici della velocità dei microprocessori e si sposta l'attenzione dall'avere sempre più veloci all'avere microprocessori multi-core con più unità di calcolo parallele tra di loro%% perché? come aiuta l'uso di Haskell qua? %%.

---

> [!fonti]+ Fonti
> 
> - 🏫 Corso di Laurea in Informatica (`L-31 R`) presso l'Università di Torino:
>     - Corso di _Linguaggi e Paradigmi di Programmazione_, A.A. 2020-21 ([pagina Moodle](https://informatica.i-learn.unito.it/enrol/index.php?id=1987)):
> 		- Prof. Luca Padovani, slide del corso:
> 			- [_Introduzione ai paradigmi di programmazione e breve storia dei linguaggi funzionali_](https://informatica.i-learn.unito.it/pluginfile.php/466243/mod_resource/content/0/storia.pdf).
> 		- Prof. Luca Padovani, videoregistrazioni del corso:
> 			- [_Introduzione ai paradigmi di programmazione e breve storia dei linguaggi funzionali_](https://informatica.i-learn.unito.it/mod/url/view.php?id=271963).
>     - Corso di _Linguaggi e Paradigmi di Programmazione_, A.A. 2025-26 ([pagina Moodle](https://informatica.i-learn.unito.it/course/view.php?id=3475)):
> 		- Prof. Viviana Bono, lezioni del corso.
