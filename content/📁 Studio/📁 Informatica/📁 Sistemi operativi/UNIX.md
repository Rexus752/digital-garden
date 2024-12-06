UNIX%% ([pronuncia]: `/ˈjuːnɪks/`)%% è un [sistema operativo](Sistemi%20operativi.md) sviluppato originariamente nei laboratori Bell di AT&T, una delle più grandi aziende di telecomunicazioni al mondo, tra gli anni '60 e '70. UNIX ha influenzato profondamente lo sviluppo di molti altri sistemi operativi, come Linux%%link%%, BSD%%link%% e macOS%%link%%. Le sue caratteristiche principali includono un design modulare, in cui ogni programma esegue una funzione specifica e può essere combinato con altri programmi tramite la riga di comando.

# 1 - Terminologia di UNIX

Oggi, molto più spesso, con il termine _UNIX_ si fa riferimento non più al sistema operativo UNIX sviluppato da AT&T, ma a una famiglia di sistemi operativi certificati per essere conformi agli standard ufficiali POSIX, stabiliti per mantenere una certa compatibilità con l'originale UNIX. Alcuni esempi di questi sistemi sono macOS%%link%% e AIX (di IBM).

Il termine _UNIX-like_ (in italiano _"simile a UNIX"_), invece, si riferisce a sistemi operativi che condividono caratteristiche, principi di design e comportamenti simili a quelli del sistema operativo UNIX originale, ma che non sono necessariamente derivati direttamente dal codice UNIX. Alcuni esempi di UNIX-like sono BSD e Linux%%link%%, il quale non deriva direttamente da UNIX, ma è stato progettato per essere compatibile e simile a UNIX.

%%
Il sistema operativo UNIX è basato su una struttura a livelli: a livello più basso c'è il kernel, che gestisce le risorse hardware e la sicurezza del sistema; al livello superiore ci sono programmi e strumenti utilizzati dagli utenti. Unix ha anche una filosofia orientata alla semplicità e alla riusabilità dei componenti, un approccio che ha reso il sistema molto versatile e ancora popolare.

# Cronologia

rimuovere gli `\` dalla seconda riga nel diagramma

```mermaid
%\%{init: { 'logLevel': 'debug', 'theme': 'base' } }%\%
    timeline
        title UNIX
	        1965: MIT + AT&T Bell Labs + GE stanno lavorando a MULTICS (Multiplexed Information and Computing Service)
	        1969: Thompson e Ritchie rilasciano la prima versione di UNICS (Uniplexed Information and Computing Service (sotto licenza di AT&T)
	        1980: Berkley University ha acquistato i sorgenti 10 anni prima e sta ancora lavorando alla sua versione del SO. Pubblicano BSD (Berkley Software Distribution)
	        1980: AT&T comincia a vendere una propria versione di UNIX chiamata SystemV. Numerosi fork, come Solaris, FreeBSD, ecc.
	        1985: Tanenbaum (Università di Amsterdam) ha creato un SO «UNIX like» chiamato MINIX, per motivi didattici
		        : Stallman fonda la Free Software Foundation (diritto di avere a disposizione il codice sorgente del software). Inizia lo sviluppo di un clone di UNIX
			1988: Standard POSIX
			1989: Stallman crea la licenza GPL e rilascia la prima versione del progetto GNU (GNU is Not UNIX), clone di UNI
			1991: Linus Torvalds, partendo da MINIX, inizia lo sviluppo del kernel LINUX. Rilascia il codice sotto licenza GPL (1992)
			1992: Orest Zborowski porta X window system su LINUX
			1993/95: Apache Web Server
```
%%

# 2 - Filosofia di UNIX

La filosofia di UNIX comprende un insieme di principi e idee che guidano il design e l'uso dei sistemi operativi della famiglia UNIX, caratterizzati da semplicità, modularità e potenza. Questi principi, emersi negli anni '70 con lo sviluppo del sistema UNIX nei Bell Labs, hanno influenzato non solo i sistemi UNIX-like (come Linux e BSD) ma anche la progettazione del software in generale.

Nonostante le diverse riformulazioni fornite nel corso degli anni, i principi fondamentali della filosofia di UNIX si possono riassumere in:
1. _**"Write programs that do one thing and do it well"**_: ogni programma dovrebbe svolgere un compito specifico in modo efficace. Questo approccio minimalista favorisce la semplicità e la modularità, infatti programmi piccoli e specializzati possono essere combinati per ottenere funzionalità più complesse.
2. _**"Write programs to work together"**_: i programmi dovrebbero essere progettati per essere concatenati tra di loro tramite meccanismi come le [pipe](#Pipe), in modo che l'output di un programma diventi l'input di un altro. È importante quindi evitare di riempire l'output con informazioni non necessarie.
3. _**"Write programs to handle text streams, because that is a universal interface"**_: i file di testo sono il formato standard per archiviare e trasferire informazioni. Sono semplici da creare, leggere, modificare e analizzare sia manualmente che con script.
%%
- Simplicity: Many of the most useful UNIX utilities are very simple and, as a result, small and easy to understand.
	- “Small and Simple” is a good technique to learn.
- Focus: It’s often better to make a program perform one task well than to throw in every feature along with the kitchen sink.
	- Programs with a single purpose are easier to improve as better algorithms or interfaces are developed
- Reusable Components: Make the core of your application available as a library. Well-documented libraries with simple but flexible programming interfaces can help others to develop variations or apply the techniques to new application areas.
- Filters: Many UNIX applications can be used as filters. That is, they transform their input and produce output.
	- UNIX provides facilities that allow quite complex applications to be developed from other UNIX programs by combining them in novel ways.
- Open File Formats: The more successful and popular UNIX programs use configuration files and data files that are plain ASCII text.
	- It enables users to use standard tools to change and search for configuration items and to develop new tools for performing new functions on the data files.
- Flexibility: You can’t anticipate exactly how ingeniously users will use your program.
	- Try to be as flexible as possible in your programming.
	- Try to avoid arbitrary limits on field sizes or number of records.
	- Never assume that you know everything that the user might want to do.
%%

%%
**4. Costruisci prototipi velocemente**
Lo sviluppo iterativo è incoraggiato. Gli strumenti possono essere creati e migliorati rapidamente grazie alla semplicità del sistema.

**5. Semplicità e trasparenza**
L'interfaccia utente e i processi interni dovrebbero essere semplici da capire e modificare. Un sistema ben progettato è chiaro e leggibile, favorendo la manutenzione e la collaborazione.

**6. Ogni cosa è un file**
In Unix, tutto è rappresentato come un file o uno stream. Questo include dispositivi hardware, directory, socket, e file tradizionali. Ciò semplifica l'interazione con il sistema.
Esempio:
- `/dev/null`: dispositivo speciale che "scarta" tutti i dati.
- `/proc`: file system virtuale che rappresenta i processi in esecuzione.

**7. Evita le interfacce grafiche complesse**
Unix privilegia l'uso della riga di comando. I comandi testuali sono più potenti, scriptabili e adatti a operazioni automatizzate rispetto a interfacce grafiche complesse.

**8. Scrivi programmi che tollerino errori**
Gli strumenti Unix seguono la filosofia di gestire gli errori in modo elegante, notificando l'utente senza interrompere inutilmente il sistema.

**9. Progetta per essere riusabile**
Ogni programma dovrebbe essere scritto in modo che possa essere utilizzato come componente in altri contesti. La riusabilità riduce la duplicazione e aumenta l'efficienza.

**10. Fai crescere il sistema organicamente**
Invece di progettare un sistema monolitico, Unix si basa sull'evoluzione incrementale: si aggiungono solo le funzionalità strettamente necessarie.
%%

# 3 - POSIX

**POSIX** (acronimo di _**P**ortable **O**perating **S**ystem **I**nterface for UNI**X**_) è una famiglia di standard definiti dall'IEEE%%link%% (denominati formalmente _IEEE 1003_) per definire un'interfaccia standard per i sistemi della famiglia UNIX, permettendo agli sviluppatori di scrivere software che può essere facilmente eseguito su piattaforme diverse.

# Fonti

- Slide del Prof. Schifanella Claudio del corso di Laboratorio di Sistemi Operativi (canale B, turno T4), Corso di Laurea in Informatica presso l'Università di Torino, A.A. 2024-25:
	- [Slide: introduzione al corso e introduzione a UNIX](https://informatica.i-learn.unito.it/pluginfile.php/422768/mod_resource/content/2/01_introduzione_UNIX.pdf)

%%
Da vedere:
- Filosofia di UNIX:
	- https://en.wikipedia.org/wiki/Unix_philosophy
	- http://www.catb.org/esr/writings/taoup/html/ch01s06.html
%%
