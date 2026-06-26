
> [!premessa]+ Premessa
> 
> Ciao! Se è la prima volta che capiti su questo sito, ti consiglio di consultare la [pagina principale](index.md) di questo cosiddetto _Giardino Digitale_ per scoprire meglio cos'è e come navigarlo.
> 
> Lo stato di questa nota è al momento: 🔴 <font color="#FF7F7F">_Bozza_</font>.

---

%% 
https://it.wikipedia.org/wiki/Template:Paradigmi_di_programmazione
%%

3 paradigmi principali:
- Imperativo: un programma è una sequenza di azioni che modificano lo stato del calcolatore quando vengono eseguite (es. C, Pascal)
- Orientato agli oggetti: programma = insieme di oggetti che comunicando tra loro, scambiando messaggi (terminologia originale scelta per descrivere questo paradigma, comunicazione = invocazione di metodi), modificano il loro stato interno (capostipite: Smalltalk, da cui deriva questa terminologia)
- Funzionale: programma = grande espressione in cui compaiono funzioni composte e applicate a determinati argomenti, più che di esecuzione si parla di "valutazione" del programma (= espressione) per ottenerne un risultato (es. Haskell)

Quasi tutti i linguaggi oggi sono multi-paradigma, pochi di essi sono esclusivi a uno solo di questi paradigmi (es. C++, principalmente a oggetti ma è derivato dal C che comunque è imperativo, oppure OCaml che nasce funzionale ma diventato poi anche a oggetti e imperativo)

# 1 - Storia

## 1.1 - Anni '50

Dopo la costruzione dei primi calcolatori elettronici, linguaggi di programmazione poco sofisticati perché si programmava direttamente in linguaggio macchina, con sforzi significativi, c'era un generale pessimismo che prima o poi si sarebbe riuscito a scrivere programmi più complessi

Grande novità arriva col FORTRAN, primo linguaggio per cui venne scritto un compilatore (che fu uno sforzo immane perché doveva essere scritto necessariamente in linguaggio macchina), FORTRAN = FORmula TRANslator proprio perché questo con FORTRAN si potevano scrivere formule come si fa normalmente con notazione infissa, parentesi, ecc. ed era focalizzato sul calcolo numerico

col FORTRAN si introducono le procedure (ma ricorsione non ammessa) e i cicli, I/O formattato, ecc.

COBOL: linguaggio per gestione aziendale, precursore dei linguaggi attuali di query dei database, introdotto il concetto di _record_

## 1.2 - Anni '60

Applicate le prime nozioni di teoria dei linguaggi, linguaggi scritti con grammatiche con semantica formale, in particolare ALGOL la cui grammatica è scritto in BNF, primo linguaggio indipendente dall'architettura e introduce i blocchi con variabili locali e ricorsione

BASIC: idea della programmazione facile da utilizzare per chiunque, al punto che il compilatore era integrato nei primi PC (IBM e Apple) 20 anni dopo, facile ma poco strutturato (uso dei `goto` che oggi è visto come una bestemmia)

In questi anni sviluppato Simula 67 come linguaggio Object Oriented, introduce i concetti di classi, oggetti ed ereditarietà

## 1.3 - Anni '70

Pascal: linguaggio che incoraggia la programmazione strutturata (per evitare l'uso di `goto`), introduce l'uso dei tipi per evitare certi errori di programmazione, ideale per imparare a programmare

Dopo i primi successi di Simula 67, continua l'evoluzione degli OOP con Smalltalk che porta questo paradigma all'estremo: **tutto è un oggetto** (numeri, classi, ecc.) e l'unica operazione possibile è l'invio di un messaggio (invocazione di un metodo)

Negli stessi anni nasce il C che nasce come linguaggio di medio/basso livello per facilitare l'accesso all'hardware e implementazione di sistemi operativi, ottenendo risultati storici: UNIX e successivamente LINUX

## 1.4 - Anni '80

Comincia a svilupparsi la programmazione concorrente e distribuita (programmi distribuiti su più unità di calcolo che possono procedere più o meno indipendentemente) con lo sviluppo di Ada, evoluzione del Pascal sviluppato dal ministero della difesa USA per la concorrenza e l'introduzione dei tipi astratti (comincia a crearsi l'idea che un tipo di dato deve possedere una parte "pubblica" visibile a tutti i suoi utilizzatori e una parte "privata" che deve essere esclusiva a chi lo implementa), concetto trasportato poi nell'OOP

C++: estensione del C con classi e oggetti, introduce i template (classi generiche ottenute per astrazione da uno o più tipi di dato) e l'overloading di operatori e metodi

Primi PC hanno prestazioni più performative, si diffondono i primi linguaggi di scripting (linguaggi di programmazione non compilati ma interpretati), in particolare:
- PostScript: linguaggio simile alla JVM, usato per descrivere documenti, creato da Adobe, si è evoluto in quello che oggi è il PDF
- Perl: per sistemisti (per manipolare file di testo, configurazione SO, find/replace di stringhe con l'uso di regex), questi programmi tipicamente diventano write-only (cioè facili da scrivere ma poi diventa difficile da leggere e quindi modificarli)

## 1.5 - Anni '90

Python: linguaggio di scripting "della domenica", creato da Van Rossum perché lui stesso ha detto che si annoiava nelle vacanze di natale, versione a oggetti di Perl

Java: doveva essere una versione ripulita e robusta di C++, inizialmente era pubblicizzato per sistemi embedded, esempio classico: impiego per la programmazione di lavatrici e per applet (piccole applicazioni) scaricate tramite il web ed eseguite tramite il proprio browser. Alla fine Java è diventato mainstream e usato per tutt'altro

PHP: linguaggio di scripting per produzione di pagine Web da database

JavaScript: produzione di pagine Web interattive, nato per sopperire alle carenze dell'HTML

## 1.6 - Anni '00

Ulteriore sviluppo dell'OOP

C#: vuole essere C++ "fatto bene", è un linguaggio sviluppato da Microsoft ma con l'aiuto di esperti anche da università con l'intento di ottenere un linguaggio elegante

Scala: OOP con sintassi "flessibile", incorpora caratteristiche dai linguaggi funzionali e si appoggia sempre sulla JVM per compilare

Go: uno dei linguaggi di successo più recenti, sviluppato da Google, programmazione concorrente e distribuita su scala globale, contiene costrutti specifici per la comunicazione su canali e abbandona alcune delle complessità tipiche dell'OOP (come la nozione di "classe") per fornire al programmatore costrutti più efficienti (_intefacce_)

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
