---
icon: RiComputerLine
iconColor: "#8888FF"
---
Il **sistema operativo** (abbreviato in **_SO_**, in inglese **_OS_**, _**O**perating **S**ystem_) è il software di base che gestisce l'hardware di un computer (in particolare la memoria primaria e secondaria, le periferiche, e la stessa CPU) e fornisce i servizi fondamentali per l'esecuzione di tutti gli altri software applicativi. È l'intermediario tra l'hardware e l'utente, permettendo l'interazione tra l'utente e il dispositivo e rendendo il sistema semplice da usare.

%%
\## 2. Interfaccia di Programmazione (API)

Le **API (Application Programming Interfaces)** offrono agli sviluppatori un insieme di comandi e funzioni per interagire con il sistema operativo senza accedere direttamente al kernel. Ad esempio, un'applicazione può usare le API per aprire file, eseguire operazioni di rete, o interagire con la memoria.
%%

# 1 - Funzioni principali di un sistema operativo

Le funzioni principali di un sistema operativo sono:
- **Gestione della CPU e del multitasking**: assegna la CPU%%link%% ai vari [processi](Processi.md) in esecuzione, permettendo il [multitasking](Processi.md#8%20-%20Multitasking), cioè l'esecuzione (apparentemente) simultanea di più attività, e garantendo che ogni processo abbia il giusto tempo di elaborazione.
- **Gestione della memoria**: tiene traccia dell'uso della memoria principale (RAM)%%link%% e assegna spazio ai vari processi, ottimizzando l'uso delle risorse e prevenendo conflitti di accesso alla memoria.
- **Gestione delle risorse hardware**: controlla e coordina l'uso delle risorse hardware, come dischi, stampanti e schede di rete, assicurando che i vari programmi possano accedere alle risorse necessarie senza interferenze.
- **Gestione dei file**: fornisce un sistema di gestione dei file che organizza i dati su supporti di memoria (dischi rigidi, SSD) e facilita operazioni come creare, leggere, scrivere, e cancellare file e directory.
- **Interfaccia utente**: può offrire un'interfaccia grafica (_**GUI**_, _**G**raphical **U**ser **I**nterface_) o a riga di comando (_**CLI**_, _**C**ommand **L**ine **I**nterface_), che consente agli utenti di interagire facilmente con il sistema.
- **Gestione della sicurezza e dei permessi**: protegge i dati e le risorse del sistema tramite meccanismi di sicurezza, come autorizzazioni e autenticazione, e limita l'accesso ai file e alle risorse sensibili.
- **Gestione della rete**: permette la comunicazione tra computer attraverso reti, gestendo protocolli di rete e assicurando la condivisione delle risorse tra i dispositivi collegati.

# 2 - Tipi di sistemi operativi

I principali tipi di sistemi operativi sono:
- **Sistemi operativi desktop**: sono progettati per essere utilizzati su computer desktop e laptop. Esempi: Windows, macOS, Linux.
- **Sistemi operativi per dispositivi mobili**: sono progettati per essere utilizzati su smartphone e tablet. Esempi: Android, iOS.
- **Sistemi operativi per server**: sono ottimizzati per la gestione di reti, servizi web e database. Esempi: Linux, Windows Server.
- **Sistemi operativi embedded**: sono progettati per dispositivi specifici come router, elettrodomestici e dispositivi IoT (_**I**nternet **o**f **T**hings_)%%link%%, con funzionalità limitate e adattate all'hardware specifico.

# 3 - Struttura di un sistema operativo

Un sistema operativo è generalmente organizzato in livelli o moduli, ciascuno con funzioni specifiche, che lavorano insieme per gestire l'hardware e fornire servizi agli utenti e alle applicazioni. Generalmente, le componenti di un sistema operativo sono le seguenti:
- **Kernel**%%link%%: è il cuore del sistema operativo, gestisce le risorse hardware e fornisce un'interfaccia tra l'hardware e gli altri livelli del sistema.
- **Shell**%%link%%: è la componente del sistema operativo visibile all'utente, quella con cui si possono impartire comandi e richiedere l'avvio di altri programmi.
- **File system**%%link%%: si occupa di organizzare i dati sui dispositivi di archiviazione e fornisce una struttura per la gestione dei file e delle directory. Gestisce anche i permessi per la sicurezza e la condivisione dei dati.
- **Gestore dei processi**%%link%%: si occupa della [creazione](Processi.md#5%20-%20Creazione%20di%20un%20processo), gestione (monitora gli stati) e [terminazione](Processi.md#6%20-%20Terminazione%20di%20un%20processo) dei processi. È responsabile del [multitasking]( Processi.md#8%20-%20Multitasking), ovvero della possibilità di eseguire più [processi](Processi.md) o [thread](Thread.md) contemporaneamente, e dell'allocazione dei tempi di CPU ai processi.
- **Gestore della memoria**%%link%%: oltre alla gestione della memoria%%link%% a livello del kernel%%link%%, il sistema operativo può implementare funzioni aggiuntive per ottimizzare l'uso della RAM e gestire la memoria virtuale%%link%% (spazio su disco che funge da memoria aggiuntiva). Le strategie includono la segmentazione%%link%% e la paginazione%%link%%.
- **Gestore dei dispositivi I/O**%%link%%: si occupa di controllare, monitorare e coordinare tutte le comunicazioni tra il sistema e le periferiche di input e output, come tastiere, mouse, stampanti, dischi rigidi, monitor, schede di rete, ecc.
- **Gestore della rete**%%link%%: gestisce le connessioni di rete, permettendo al computer di connettersi a reti locali o a Internet. Comprende protocolli di rete, sicurezza, e gestione degli indirizzi IP%%link%%.
- **Gestore della sicurezza**%%link%%: il sistema operativo fornisce meccanismi di sicurezza per proteggere i dati e le risorse da accessi non autorizzati, tramite un meccanismo di controllo e di autenticazione.

In molti sistemi operativi, questi moduli sono organizzati in una **struttura a livelli**, dal kernel (livello più basso) all'interfaccia utente (livello più alto), semplificando la gestione del sistema operativo e aumentando la sicurezza e l'affidabilità.

%%
• Utilities are the applications that enable you to work on the system (not to be confused with the shell).
- These utilities include the Web browser for navigating the Internet, word processing utilities, e-mail programs, and other commands that will be discussed throughout this course
%%

## 3.1 - Kernel

Il **kernel** è il nucleo fondamentale di un sistema operativo ed è il software che funge da intermediario tra l'hardware del computer (come CPU, memoria, dispositivi di I/O) e le applicazioni. Il kernel gestisce le risorse del sistema e ne controlla l'accesso, garantendo che i [processi](Processi.md) possano operare in modo sicuro ed efficiente.

Il kernel è progettato per funzionare con uno specifico tipo di hardware. Ciò significa che, per esempio, un kernel creato per un processore Sun SPARC non funzionerà su una macchina con un processore Intel senza essere adattato o modificato. Questo accade perché ogni tipo di hardware ha specifiche caratteristiche e istruzioni che il kernel deve conoscere per gestirlo correttamente. Le architetture di processori diverse hanno insiemi di istruzioni unici, e il kernel deve essere "costruito" in modo specifico per quell'architettura affinché possa comunicare efficacemente con l’hardware.

Inoltre, il kernel si occupa di operazioni molto tecniche e a basso livello, come l’accesso diretto ai componenti hardware (ad esempio, l’hard disk, la memoria e i processori) e, di conseguenza, non è un componente “user-friendly” del sistema operativo: generalmente l'utente non interagisce mai direttamente con esso. Anziché interagire con il kernel, gli utenti utilizzano il sistema operativo e le applicazioni, che a loro volta comunicano con il kernel per svolgere le operazioni richieste.

%%
Un kernel non è strettamente necessario per far funzionare un computer. I [programmi](https://it.wikipedia.org/wiki/Programma_(informatica) "Programma (informatica)") possono essere infatti direttamente caricati ed eseguiti sulla macchina, a patto che i loro [sviluppatori](https://it.wikipedia.org/wiki/Programmatore "Programmatore") ritengano necessario fare a meno del supporto del sistema operativo.

Questa era la modalità di funzionamento tipica dei primi computer, che venivano resettati prima di eseguire un nuovo programma. In un secondo tempo, alcuni programmi accessori come i program loader e i [debugger](https://it.wikipedia.org/wiki/Debugger "Debugger") venivano lanciati da una [memoria a sola lettura](https://it.wikipedia.org/wiki/Read_Only_Memory "Read Only Memory"), o fatti risiedere in [memoria](https://it.wikipedia.org/wiki/Memoria_(informatica) "Memoria (informatica)") durante le transizioni del computer da un'[applicazione](https://it.wikipedia.org/wiki/Applicazione_(informatica) "Applicazione (informatica)") all'altra: essi formarono la base di fatto per la creazione dei primi sistemi operativi.

Un'altra situazione in cui l'assenza di sistema operativo è auspicabile è l'esempio dei [microcontrollori](https://it.wikipedia.org/wiki/Microcontrollore "Microcontrollore") monolitici.

L'accesso diretto al kernel da parte di un utente/[amministratore](https://it.wikipedia.org/wiki/Sistemista "Sistemista") può avvenire in modalità [user mode](https://it.wikipedia.org/wiki/User_mode "User mode") o [kernel mode](https://it.wikipedia.org/wiki/Kernel_mode "Kernel mode").
%%

### Classificazione dei kernel

L'accesso diretto all'hardware può essere anche molto complesso, quindi i kernel usualmente implementano uno o più tipi di astrazione dall'hardware detti _livelli di astrazione dell'hardware_ (HAL, Hardware Abstraction Layer). Queste astrazioni servono a "nascondere" la complessità e a fornire un'interfaccia pulita e uniforme all'hardware sottostante, in modo da semplificare il lavoro degli sviluppatori.

I kernel si possono classificare in quattro categorie, in base al grado di astrazione dell'hardware:
- **Kernel monolitici**: implementano direttamente una completa astrazione dell'hardware sottostante. È più veloce ma più complesso da gestire e ne è un esempio Linux%%link%%.
- **Microkernel**: forniscono un insieme ristretto e semplice di astrazione dell'hardware e usano software "esterni" al kernel per fornire maggiori funzionalità. Ne sono un esempio MINIX e HURD.
- **Kernel ibridi** (o **microkernel modificati**): si differenziano dai microkernel puri per l'implementazione di alcune funzioni aggiuntive al fine di incrementare le prestazioni. È utilizzato in sistemi come Windows e macOS.
- **Esokernel**: rimuovono tutte le limitazioni legate all'astrazione dell'hardware e permettono ai programmi di comunicare quasi direttamente con le risorse fisiche, come la CPU, la memoria e i dispositivi di I/O. Lasciano la maggior parte della gestione del sistema a delle librerie di livello superiore (dette _libOS_), cioè collezioni di codice che forniscono alle applicazioni le funzioni di base tipiche di un sistema operativo, ma senza essere integrate direttamente nel kernel.

%%
![](Pasted%20image%2020241110153307.png)
Aggiungere nella foto l'esokernel e spiegare cosa c'è nella foto
%%

In base al tipo, quindi, altri componenti del sistema operativo come il gestore dei processi%%link%%, il gestore dei dispositivi%%link%% o il file system%%link%% possono o meno fare parte del kernel.

## 3.2 - Shell

%%
The shell is a command line interpreter that enables
the user to interact with the operating system.
• A shell provides the next layer of functionality for the
system; it is what you use directly to administer and
run the system.
- The shell is used almost exclusively via the command line,
a text-based mechanism by which the user interacts with
the system.
- There are three major shells available on most systems:
the Bourne shell (also called sh), the C shell (csh), and the
Korn shell (ksh)
%%

%%
Può essere una GUI, cioè un'interfaccia grafica che offre finestre, icone, pulsanti, e altri elementi visivi, o una CLI, cioè un'interfaccia a riga di comando che consente l'interazione attraverso comandi testuali, o una TUI.
%%

## 3.3 - File system

%%
The file system enables the user to view, organize, secure, and interact with, in a consistent manner,
files and directories located on storage devices.
%%

%%
\### File system in UNIX

Files have names: file extension does not imply anything about the content, it is just part of the name
• In most file systems, files are arranged in a tree structure
• Directories are special files which may contain other files
• The root of the tree is “/”
• The full pathname of a file is the list of all directories from the root
• “/” until the directory of the file
• “.” is the current directory
• “..” is the parent directory
• “~” is the home directory of the user
• Files may be links to other files: command ln to create links

Files are an abstraction of anything that can be viewed as a sequence of
bytes: the disk is a (special) file
• More in general, there are 7 types of files:
	- (marked by “-” in ls -l) regular file: contains data, are on disk
	- (marked by “d” in ls -l) directories: contains names of other files
	- (marked by “c” in ls -l) character special file: used to read/write devices byte by byte (stat
	/dev/urandom)
	- (marked by “b” in ls -l) block special file: used to read/write to devices in block (disks). Try stat
	/dev/sda1
	- (marked by “p” in ls -l) FIFO: a special file used for interprocess communication (IPC)
	- (marked by “s” in ls -l) socket: used for network communication
	- (marked by “l” in ls -l) symbolic link: it just points to another file
• try `stat <some-file>`, stat /dev/sda1 to view status and type of any file
• the disk is a file: cat /dev/sda1 to show its content

![](Pasted%20image%2020241110160903.png)
%%

## 3.4 - Gestore dei processi

%%
Una parte specifica del gestore dei processi è lo scheduler
- **Scheduler**: è il componente fondamentale dei sistemi operativi [multitasking]( Processi.md#8%20-%20Multitasking), cioè quelli in grado di eseguire più [processi](Processi.md) contemporaneamente, e si occupa di fare avanzare un processo interrompendone temporaneamente un altro, realizzando così un [cambio di contesto](Processi.md#3.4%20-%20Il%20cambio%20di%20contesto) (context switch).
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

%%
Sometimes a process requires more memory than is available (too many other processes running, for example).
This is where virtual memory comes in.
- When there isn’t enough physical memory, the system tries to accommodate the process by moving portions of it to the hard disk.
- When the portion of the process that was moved to hard disk is needed again, it is returned to physical memory. This procedure, called paging, allows the system to provide multitasking capabilities, even with limited physical memory.

- Another aspect of virtual memory is called swap, whereby the kernel identifies the least-busy process or a process that does not require immediate execution
- The kernel then moves the entire process out of RAM to the hard drive until it is needed again, at which point it can be run from the hard drive or from physical RAM.
- The difference between the two is that paging moves only part of the process to the hard drive, while swapping moves the entire process to hard drive space. The segment of the hard drive used for virtual memory is called the swap space in Unix.
%%

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

# Fonti

- Abraham Silberschatz, Peter Baer Galvin, Greg Gagne - [Sistemi Operativi (10ᵃ Edizione)](https://he.pearson.it/catalogo/1099) - Pearson, 2019 - ISBN: `9788891904560`.
- Slide del Prof. Aldinucci Marco del corso di Sistemi Operativi (canale B), Corso di Laurea in Informatica presso l'Università di Torino, A.A. 2024-25:
	- [Cap_03](https://informatica.i-learn.unito.it/mod/resource/view.php?id=253884)
- Slide del Prof. Schifanella Claudio del corso di Laboratorio di Sistemi Operativi (canale B, turno T4), Corso di Laurea in Informatica presso l'Università di Torino, A.A. 2024-25:
	- [Slide: introduzione al corso e introduzione a UNIX](https://informatica.i-learn.unito.it/pluginfile.php/422768/mod_resource/content/2/01_introduzione_UNIX.pdf)