Un **sistema operativo** (OS, Operating System) è il software di base che gestisce l'hardware di un computer (in particolare la memoria primaria e secondaria, le periferiche, e la stessa CPU) e fornisce i servizi fondamentali per l'esecuzione di tutti gli altri software applicativi. È l'intermediario tra l'hardware e l'utente, permettendo l'interazione tra l'utente e il dispositivo e rendendo il sistema semplice da usare.

%%
\## 2. Interfaccia di Programmazione (API)

Le **API (Application Programming Interfaces)** offrono agli sviluppatori un insieme di comandi e funzioni per interagire con il sistema operativo senza accedere direttamente al kernel. Ad esempio, un'applicazione può usare le API per aprire file, eseguire operazioni di rete, o interagire con la memoria.
%%

# 1 - Funzioni principali di un sistema operativo

Le funzioni principali di un sistema operativo sono:
- **Gestione della CPU e del multitasking**: assegna la CPU%%link%% ai vari [processi](Processi.md) in esecuzione, permettendo il [multitasking](Processi.md#7%20-%20Multitasking), cioè l'esecuzione (apparentemente) simultanea di più attività, e garantendo che ogni processo abbia il giusto tempo di elaborazione.
- **Gestione della memoria**: tiene traccia dell'uso della memoria principale (RAM)%%link%% e assegna spazio ai vari processi, ottimizzando l'uso delle risorse e prevenendo conflitti di accesso alla memoria.
- **Gestione delle risorse hardware**: controlla e coordina l'uso delle risorse hardware, come dischi, stampanti e schede di rete, assicurando che i vari programmi possano accedere alle risorse necessarie senza interferenze.
- **Gestione dei file**: fornisce un sistema di gestione dei file che organizza i dati su supporti di memoria (dischi rigidi, SSD) e facilita operazioni come creare, leggere, scrivere, e cancellare file e directory.
- **Interfaccia utente**: può offrire un'interfaccia grafica (GUI, Graphical User Interface) o a riga di comando (CLI, Command Line Interface), che consente agli utenti di interagire facilmente con il sistema.
- **Gestione della sicurezza e dei permessi**: protegge i dati e le risorse del sistema tramite meccanismi di sicurezza, come autorizzazioni e autenticazione, e limita l'accesso ai file e alle risorse sensibili.
- **Gestione della rete**: permette la comunicazione tra computer attraverso reti, gestendo protocolli di rete e assicurando la condivisione delle risorse tra i dispositivi collegati.

# 2 - Tipi di sistemi operativi

I principali tipi di sistemi operativi sono:
- **Sistemi operativi desktop**: sono progettati per essere utilizzati su computer desktop e laptop. Esempi: Windows, macOS, Linux.
- **Sistemi operativi per dispositivi mobili**: sono progettati per essere utilizzati su smartphone e tablet. Esempi: Android, iOS.
- **Sistemi operativi per server**: sono ottimizzati per la gestione di reti, servizi web e database. Esempi: Linux, Windows Server.
- **Sistemi operativi embedded**: sono progettati per dispositivi specifici come router, elettrodomestici e dispositivi IoT (Internet of Things)%%link%%, con funzionalità limitate e adattate all'hardware specifico.

# 3 - Struttura di un sistema operativo

Un sistema operativo è generalmente organizzato in livelli o moduli, ciascuno con funzioni specifiche, che lavorano insieme per gestire l'hardware e fornire servizi agli utenti e alle applicazioni. Generalmente, le componenti di un sistema operativo sono le seguenti:
- **Kernel**%%link%%: è il cuore del sistema operativo, gestisce le risorse hardware e fornisce un'interfaccia tra l'hardware e gli altri livelli del sistema.
- **Shell**%%link%%: è la componente del sistema operativo visibile all'utente, quella con cui si possono impartire comandi e richiedere l'avvio di altri programmi.
- **File system**%%link%%: si occupa di organizzare i dati sui dispositivi di archiviazione e fornisce una struttura per la gestione dei file e delle directory. Gestisce anche i permessi per la sicurezza e la condivisione dei dati.
- **Gestore dei processi**%%link%%: si occupa della [creazione](Processi.md#5%20-%20Creazione%20di%20un%20processo), gestione (monitora gli stati) e [terminazione](Processi.md#6%20-%20Terminazione%20di%20un%20processo) dei processi. È responsabile del [multitasking](Processi.md#7%20-%20Multitasking), ovvero della possibilità di eseguire più [processi](Processi.md) o [thread](Thread.md) contemporaneamente, e dell'allocazione dei tempi di CPU ai processi.
- **Gestore della memoria**%%link%%: oltre alla gestione della memoria%%link%% a livello del kernel%%link%%, il sistema operativo può implementare funzioni aggiuntive per ottimizzare l'uso della RAM e gestire la memoria virtuale%%link%% (spazio su disco che funge da memoria aggiuntiva). Le strategie includono la segmentazione%%link%% e la paginazione%%link%%.
- **Gestore dei dispositivi I/O**%%link%%: si occupa di controllare, monitorare e coordinare tutte le comunicazioni tra il sistema e le periferiche di input e output, come tastiere, mouse, stampanti, dischi rigidi, monitor, schede di rete, ecc.
- **Gestore della rete**%%link%%: gestisce le connessioni di rete, permettendo al computer di connettersi a reti locali o a Internet. Comprende protocolli di rete, sicurezza, e gestione degli indirizzi IP%%link%%.
- **Gestore della sicurezza**%%link%%: il sistema operativo fornisce meccanismi di sicurezza per proteggere i dati e le risorse da accessi non autorizzati, tramite un meccanismo di controllo e di autenticazione.

In molti sistemi operativi, questi moduli sono organizzati in una **struttura a livelli**, dal kernel (livello più basso) all'interfaccia utente (livello più alto), semplificando la gestione del sistema operativo e aumentando la sicurezza e l'affidabilità.

## 3.1 - Kernel

%%descrizione kernel%%

%%sistemare%%

%%
È responsabile di:
   - **Gestione della CPU**: Gestisce la schedulazione della CPU e il multitasking, assegnando tempo di elaborazione ai vari processi.
   - **Gestione della Memoria**: Tiene traccia della memoria in uso e distribuisce lo spazio ai processi, usando tecniche come la memoria virtuale per ottimizzare le risorse.
   - **Gestione dei Dispositivi**: Coordina l'uso di dispositivi come dischi, tastiere, schermi, stampanti e altri componenti hardware.
   - **Gestione del File System**: Implementa il file system, che organizza i dati sui supporti di memoria e consente l'accesso sicuro e strutturato ai file.

Il kernel può essere **monolitico** (come Linux), con tutte le funzioni principali racchiuse in un unico modulo, o **microkernel** (come MINIX o HURD), in cui le funzioni sono divise in moduli separati per una maggiore modularità e stabilità.

Il kernel può essere suddiviso in diversi tipi a seconda della sua architettura:
- **Kernel monolitico**: Tutte le funzionalità del sistema operativo sono integrate in un unico nucleo, come in Linux. È più veloce ma più complesso da gestire.
- **Microkernel**: Solo le funzionalità di base sono incluse nel kernel, come la gestione della memoria e della CPU, mentre altre funzionalità sono spostate in moduli separati (ad esempio, Minix).
- **Kernel ibrido**: Combina aspetti dei kernel monolitici e dei microkernel. È utilizzato in sistemi come Windows e macOS.
%%

## 3.2 - Shell

%%
Può essere una GUI, cioè un'interfaccia grafica che offre finestre, icone, pulsanti, e altri elementi visivi, o una CLI, cioè un'interfaccia a riga di comando che consente l'interazione attraverso comandi testuali, o una TUI.
%%

## 3.3 - File system

## 3.4 - Gestore dei processi

%%
Una parte specifica del gestore dei processi è lo scheduler
- **Scheduler**: è il componente fondamentale dei sistemi operativi [multitasking](Processi.md#7%20-%20Multitasking), cioè quelli in grado di eseguire più [processi](Processi.md) contemporaneamente, e si occupa di fare avanzare un processo interrompendone temporaneamente un altro, realizzando così un [cambio di contesto](Processi.md#3.4%20-%20Il%20cambio%20di%20contesto) (context switch).
%%

### 3.4.1 - Scheduler

%%
No, il **gestore dei processi** e lo **scheduler** non sono la stessa cosa, anche se lavorano a stretto contatto nella gestione dei processi in un sistema operativo.

### 3.4.2 - Differenza tra Gestore dei Processi e Scheduler

1. **Gestore dei Processi**:
   - È il componente del sistema operativo che si occupa di **creare, gestire e terminare i processi**.
   - Gestisce il **ciclo di vita dei processi**, monitorando stati come "pronto", "in esecuzione", "in attesa" e "terminato".
   - Fornisce **meccanismi di comunicazione** tra processi e risorse per la gestione della memoria per ogni processo.
   - È responsabile della creazione di processi (spesso tramite chiamate di sistema come `fork` o `exec` in Unix) e della loro distruzione una volta terminati.
   - È, in sostanza, il "supervisore" dei processi.

2. **Scheduler**:
   - È una **parte specifica del gestore dei processi** che decide **quale processo eseguire e quando**.
   - Ha l'obiettivo di **ottimizzare l'uso della CPU** e garantire che tutti i processi ricevano un tempo di esecuzione equo.
   - L'algoritmo di scheduling può variare a seconda degli obiettivi del sistema (per esempio, *Round Robin*, *First Come First Served*, *Priority Scheduling*, ecc.).
   - L'**algoritmo di scheduling** decide la sequenza dei processi, la durata e il momento in cui passare da un processo all'altro, in base a criteri come priorità, utilizzo della CPU, e altri fattori.

In sintesi, il **gestore dei processi** è responsabile della gestione complessiva e della supervisione dei processi nel sistema, mentre lo **scheduler** è specificamente incaricato di selezionare e programmare l'ordine di esecuzione dei processi sulla CPU.

---

\### 3. **Gestione dei Processi e Thread**

Questo modulo gestisce la creazione, esecuzione e terminazione dei processi e thread, gestendo anche la comunicazione e la sincronizzazione tra di essi. Queste funzionalità sono cruciali per il multitasking e per sfruttare al massimo la CPU, garantendo che i processi non interferiscano tra loro.

%%

## 3.5 - Gestore della memoria

## 3.6 - Gestore dei dispositivi I/O

%%
Il modulo di **gestione dei dispositivi I/O** e i **driver** di periferica consentono al sistema operativo di comunicare con hardware specifico (come stampanti, schede di rete, e dischi). I driver traducono i comandi generali del sistema operativo in istruzioni specifiche per i dispositivi.
%%

## 3.7 - Gestore della rete

%%
Gestisce la connessione e comunicazione tra computer, implementando protocolli di rete come TCP/IP. Supporta le operazioni di rete come la trasmissione di dati e l'accesso a risorse remote, fondamentale per internet e le reti locali.
%%

## 3.8 - Gestore della sicurezza

# 4 - Definizione universale di "sistema operativo"

Non esiste una definizione universalmente accettata di che cosa faccia parte o meno di un sistema operativo: il confine tra il SO e le altre componenti software non è sempre ben definibile.

Per esempio, l'interfaccia grafica non fa sempre parte del SO: nel passaggio da MS-DOS a Windows, l'interfaccia grafica si è integrata nel SO, ma inizialmente non ne faceva parte, mentre in UNIX i comandi a disposizione dell'utente non sono parte del SO, come pure le varie interfacce grafiche a disposizione.

Il problema di definire esattamente quali siano i componenti di un sistema operativo sembra avere poca importanza, ma da un punto di vista commerciale/economico può avere una rilevanza fondamentale.

