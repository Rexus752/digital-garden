
> [!premessa]+ Premessa
> 
> Ciao! Se è la prima volta che capiti su questo sito, ti consiglio di consultare la [pagina principale](index.md) di questo cosiddetto _Giardino Digitale_ per scoprire meglio cos'è e come navigarlo.
> 
> Lo stato di questa nota è al momento: 🔴 <font color="#FF7F7F">_Bozza_</font>.

---

%%
System calls: sono delle API che consentono l'accesso ai servizi dell'ISO. Ogni SO ha un tipo di API diversa:
- Windows: win32
- Linux/macOS: POSIX
- JVM: Java API

Le **API (Application Programming Interfaces)** offrono agli sviluppatori un insieme di comandi e funzioni per interagire con il sistema operativo senza accedere direttamente al kernel. Ad esempio, un'applicazione può usare le API per aprire file, eseguire operazioni di rete, o interagire con la memoria.

Attività del sistema operativo: all'avvio del computer, viene avviato il bootstrap program dal firmware. Esso deve individuare e avviare il kernel e subito dopo i processi di sistema (o deamon).
%%

%% 
https://www.geeksforgeeks.org/computer-organization-architecture/difference-between-uniform-memory-access-uma-and-non-uniform-memory-access-numa/
Multiprocessori di due tipi:
- UMA (Uniform Memory Access): processori equidistanti dalla memoria = stessa latenza per tutti i processori
	- Vantaggi
		- Facile da implementare
		- Bassa latenza
		- Basso costo
	- Svantaggi:
		- Scalabilità limitata: dopo un certo punto, aggiungere più processori o core al sistema può causare contesa per il bus della memoria
		- Larghezza di banda limitata: tutti i processori/core condividono un unico memory bus
		- Capacità di memoria limitata
- NUMA (Non-Uniform Memory Access): processori non equidistanti dalla memoria = latenza dipende da quale zona di memoria si vuole accedere, ogni processore ha una porzione della memoria vicino a se
	- Vantaggi
		- Performance migliori: ogni professore ha la propria memoria locale quindi tempi di accesso alla memoria ridotti
		- Scalabilità: sistemi NUMA altamente scalabili
		- Contesa della memoria ridotta: ogni processore ha la propria memoria, è meno frequente che due processori chiedano accesso alla stessa porzione di memoria
	- Svantaggi
		- Complessità
		- Costo alto
		- Variabilità della performance: in alcuni casi meglio UMA, specie se serve accesso frequente a memoria condivisa
%%

> [!definizione]+ Definizione: sistema operativo
> 
> Il **sistema operativo** (abbreviato in **_SO_**, in inglese **_OS_**, _**O**perating **S**ystem_) è il software di base che gestisce le risorse hardware (in particolare la memoria primaria e secondaria, le periferiche, e la stessa CPU) e software di un computer, permettendo e facilitando l'interazione tra l'utente e la macchina.
> 
> Un generico sistema operativo moderno si compone di alcune parti standard, più o meno ben definite: [kernel](Informatica/Sistemi%20operativi/Sistemi%20operativi.md#^definizione-kernel), 
> 
> In base al tipo di computer per cui viene progettato, i sistemi operativi si dividono in desktop%% link %%, per dispositivi mobili%% link %%, per server %% link %% ed embedded%% link %%.
^definizione-sistema-operativo

%% link a tutte le parole nella definizione e nell'osservazione qua sotto %%

> [!osservazione]+ Osservazione: cosa fa parte di un sistema operativo e cosa no?
> 
> Non esiste una definizione universalmente accettata di che cosa faccia parte o meno di un [sistema operativo](Informatica/Sistemi%20operativi/Sistemi%20operativi.md#^definizione-sistema-operativo): il confine tra il SO e le altre componenti software non è sempre ben definibile.
> 
> Per esempio, l'interfaccia grafica (cioè quella parte del [sistema operativo](Informatica/Sistemi%20operativi/Sistemi%20operativi.md#^definizione-sistema-operativo) che gestisce la grafica che ci viene mostrata) non ne fa sempre parte: nel passaggio da MS-DOS%% link %% a Windows%% link %%, l'interfaccia grafica si è integrata nel SO, ma inizialmente non ne faceva parte, così come in [UNIX]() i comandi a disposizione dell'utente non sono parte del SO, come pure le varie interfacce grafiche a disposizione.
> 
> Il problema di definire esattamente quali siano i componenti di un sistema operativo sembra avere poca importanza, ma da un punto di vista commerciale/economico può avere una rilevanza fondamentale: basti pensare, per esempio, a un cliente che ha bisogno di acquistare la licenza di un sistema operativo completo, ma che poi scopre non essere fornito dell'interfaccia grafica (essenziale per coloro che non hanno molta domestichezza con l'informatica).

Ogni [sistema operativo](Informatica/Sistemi%20operativi/Sistemi%20operativi.md#^definizione-sistema-operativo), in un dato momento del suo utilizzo, ha una determinata [_configurazione_](Informatica/Sistemi%20operativi/Sistemi%20operativi.md#^definizione-configurazione-di-un-sistema-operativo).

> [!definizione]+ Definizione: configurazione di un sistema operativo
> 
> La **configurazione di un [sistema operativo](Informatica/Sistemi%20operativi/Sistemi%20operativi.md#^definizione-sistema-operativo)** è l'insieme delle impostazioni, regole e componenti software che determinano come il [sistema operativo](Informatica/Sistemi%20operativi/Sistemi%20operativi.md#^definizione-sistema-operativo) è organizzato, quali funzioni svolge e in che modo le svolge.
^definizione-configurazione-di-un-sistema-operativo

> [!osservazione]+ Osservazione: cosa fa parte della configurazione di un SO e cosa no?
> 
> All'interno della definizione di [_configurazione di un sistema operativo_](Informatica/Sistemi%20operativi/Sistemi%20operativi.md#^definizione-configurazione-di-un-sistema-operativo) solitamente si include unicamente ciò che, indica _come_ il [sistema operativo](Informatica/Sistemi%20operativi/Sistemi%20operativi.md#^definizione-sistema-operativo) si deve comportare: per esempio, le impostazioni di sistema, i driver%% link %% installati, i servizi%% link %% attivi, le politiche di sicurezza%% link %%, la configurazione della rete%% link %% e la gestione degli utenti%% link %% e dei permessi%% link %%.
> 
> I dati%% link %% dell'utente%% link %% (come documenti%% link %%, salvataggi di giochi, foto, ecc.) non fanno parte della [configurazione del sistema operativo](Informatica/Sistemi%20operativi/Sistemi%20operativi.md#^definizione-configurazione-di-un-sistema-operativo), anche se possono dipendere da essa.
^osservazione-cosa-fa-parte-della-configurazione-di-un-so-e-cosa-no

%%
\# 1 - Funzioni principali di un sistema operativo

Le funzioni principali di un sistema operativo sono:
- **Gestione della CPU e del multitasking**: assegna la CPU ai vari [processi]() in esecuzione, permettendo il [multitasking](), cioè l'esecuzione (apparentemente) simultanea di più attività, e garantendo che ogni processo abbia il giusto tempo di elaborazione.
- **Gestione della memoria**: tiene traccia dell'uso della memoria principale (RAM) e assegna spazio ai vari processi, ottimizzando l'uso delle risorse e prevenendo conflitti di accesso alla memoria.
- **Gestione delle risorse hardware**: controlla e coordina l'uso delle risorse hardware, come dischi, stampanti e schede di rete, assicurando che i vari programmi possano accedere alle risorse necessarie senza interferenze.
- **Gestione dei file**: fornisce un sistema di gestione dei file che organizza i dati su supporti di memoria (dischi rigidi, SSD) e facilita operazioni come creare, leggere, scrivere, e cancellare file e directory.
- **Interfaccia utente**: può offrire un'interfaccia grafica (_**GUI**_, _**G**raphical **U**ser **I**nterface_) o a riga di comando (_**CLI**_, _**C**ommand **L**ine **I**nterface_), che consente agli utenti di interagire facilmente con il sistema.
- **Gestione della sicurezza e dei permessi**: protegge i dati e le risorse del sistema tramite meccanismi di sicurezza, come autorizzazioni e autenticazione, e limita l'accesso ai file e alle risorse sensibili.
- **Gestione della rete**: permette la comunicazione tra computer attraverso reti, gestendo protocolli di rete e assicurando la condivisione delle risorse tra i dispositivi collegati.
%%

# 1 - Struttura di un sistema operativo

%% 
Sono di diversi tipi:
- Struttura monolitica: tutti i servizi sono nel kernel, che viene organizzato in un singolo file con un unico spazio di indirizzamento. Vantaggi: veloce per latenze ridotte. Svantaggi: difficile da implementare ed estendere. Possono essere:
	- Tightly coupled: le modifiche a un componente avranno impatto anche su altri componenti
	- Loosely coupled: le modifiche avranno un impatto **solo** su quel componente
- A strati: si definiscono i layer da 0 (kernel) a $n$ (GUI). Ogni strato chiama metodi degli strati precedenti. Vantaggi: facile progettaziobe. Svantaggi: lentezza.
- Micro-kernel: il kernel si occupa solo di poche attività mentre i servizi sono programmi applicativi fuori dal kernel. In particolare, si occupa di comunicazione tra processi, gestione della memroia, scheduling CPU. Vantaggi: facile progettazione ed estensione coi moduli caricati dinamicamente. Svantaggi: può avere latenza nella IPC.
- A moduli: il SO imposta le funzionalità principali del kernel, mentre le altre funzionalità sono caricate in maniera dinamica.

I SO possono avere 2 tipologie diverse di esecuzione dei programmi:
- Batch system: i programmi vengono eseguiti in maniera sequenziale senza interruzioni
- Time-shared system: i programmi vengono eseguiti in multitasking. Ogni task è formato da:
	- Text section: codice
	- Registri e Program Counter
	- Stack: dati e strutture staitche
	- Data section: SOLO per le variabili globali
	- Heap: dati e strutture dinamiche
%%

Un sistema operativo è generalmente organizzato in livelli o moduli, ciascuno con funzioni specifiche, che lavorano insieme per gestire l'hardware e fornire servizi agli utenti e alle applicazioni. Generalmente, le componenti di un sistema operativo sono le seguenti:
- **Kernel**%%link%%: è il cuore del sistema operativo, gestisce le risorse hardware e fornisce un'interfaccia tra l'hardware e gli altri livelli del sistema.
- **Shell**%%link%%: è la componente del sistema operativo visibile all'utente, quella con cui si possono impartire comandi e richiedere l'avvio di altri programmi.
- **File system**%%link%%: si occupa di organizzare i dati sui dispositivi di archiviazione e fornisce una struttura per la gestione dei file e delle directory. Gestisce anche i permessi per la sicurezza e la condivisione dei dati.
- **Gestore dei processi**%%link%%: si occupa della [creazione](), gestione (monitora gli stati) e [terminazione]() dei processi. È responsabile del [multitasking](), ovvero della possibilità di eseguire più [processi]() o [thread]() contemporaneamente, e dell'allocazione dei tempi di CPU ai processi.
- **Gestore della memoria**%%link%%: oltre alla gestione della memoria%%link%% a livello del kernel%%link%%, il sistema operativo può implementare funzioni aggiuntive per ottimizzare l'uso della RAM e gestire la memoria virtuale%%link%% (spazio su disco che funge da memoria aggiuntiva). Le strategie includono la segmentazione%%link%% e la paginazione%%link%%.
- **Gestore dei dispositivi I/O**%%link%%: si occupa di controllare, monitorare e coordinare tutte le comunicazioni tra il sistema e le periferiche di input e output, come tastiere, mouse, stampanti, dischi rigidi, monitor, schede di rete, ecc.
- **Gestore della rete**%%link%%: gestisce le connessioni di rete, permettendo al computer di connettersi a reti locali o a Internet. Comprende protocolli di rete, sicurezza, e gestione degli indirizzi IP%%link%%.
- **Gestore della sicurezza**%%link%%: il sistema operativo fornisce meccanismi di sicurezza per proteggere i dati e le risorse da accessi non autorizzati, tramite un meccanismo di controllo e di autenticazione.

In molti sistemi operativi, questi moduli sono organizzati in una **struttura a livelli**, dal kernel (livello più basso) all'interfaccia utente (livello più alto), semplificando la gestione del sistema operativo e aumentando la sicurezza e l'affidabilità.

%% 
Altre componenti del sistema operativo:
- Programmi di sistema: sono programmi associati al Sistema Operativo ma che non è detto che facciano parte del kernel (es. browser, blocco note, esplora risorse ecc.)
- Middleware (generalmente per mobile): software aggiuntivo a supporto di sviluppatori
%%

%%
• Utilities are the applications that enable you to work on the system (not to be confused with the shell).
- These utilities include the Web browser for navigating the Internet, word processing utilities, e-mail programs, and other commands that will be discussed throughout this course
%%

## 1.1 - Kernel

> [!definizione]+ Definizione: kernel
> 
> Il **kernel** è il nucleo fondamentale di un [sistema operativo](Informatica/Sistemi%20operativi/Sistemi%20operativi.md#^definizione-sistema-operativo) ed è il software che funge da intermediario tra l'hardware del computer (come CPU%% link %%, memoria%% link %%, dispositivi di I/O%% link %%) e tutte le altre applicazioni. Il kernel gestisce le risorse del sistema e ne controlla l'accesso, garantendo che i [processi]() possano operare in modo sicuro ed efficiente.
^definizione-kernel

> [!osservazione]+ Osservazione: kernel apposito per ogni sistema operativo
> 
> Il [kernel](Informatica/Sistemi%20operativi/Sistemi%20operativi.md#^definizione-kernel) è progettato per funzionare con uno specifico tipo di hardware. Ciò significa che, per esempio, un kernel creato per un processore Sun SPARC non funzionerà su una macchina con un processore Intel senza essere adattato o modificato. Questo accade perché ogni tipo di hardware ha specifiche caratteristiche e istruzioni che il kernel deve conoscere per gestirlo correttamente. Le architetture di processori diverse hanno insiemi di istruzioni unici, e il kernel deve essere "costruito" in modo specifico per quell'architettura affinché possa comunicare efficacemente con l'hardware.

%%
Un kernel non è strettamente necessario per far funzionare un computer. I [programmi](https://it.wikipedia.org/wiki/Programma_(informatica) "Programma (informatica)") possono essere infatti direttamente caricati ed eseguiti sulla macchina, a patto che i loro [sviluppatori](https://it.wikipedia.org/wiki/Programmatore "Programmatore") ritengano necessario fare a meno del supporto del sistema operativo.

Questa era la modalità di funzionamento tipica dei primi computer, che venivano resettati prima di eseguire un nuovo programma. In un secondo tempo, alcuni programmi accessori come i program loader e i [debugger](https://it.wikipedia.org/wiki/Debugger "Debugger") venivano lanciati da una [memoria a sola lettura](https://it.wikipedia.org/wiki/Read_Only_Memory "Read Only Memory"), o fatti risiedere in [memoria](https://it.wikipedia.org/wiki/Memoria_(informatica) "Memoria (informatica)") durante le transizioni del computer da un'[applicazione](https://it.wikipedia.org/wiki/Applicazione_(informatica) "Applicazione (informatica)") all'altra: essi formarono la base di fatto per la creazione dei primi sistemi operativi.

Un'altra situazione in cui l'assenza di sistema operativo è auspicabile è l'esempio dei [microcontrollori](https://it.wikipedia.org/wiki/Microcontrollore "Microcontrollore") monolitici.

L'accesso diretto al kernel da parte di un utente/[amministratore](https://it.wikipedia.org/wiki/Sistemista "Sistemista") può avvenire in modalità [user mode](https://it.wikipedia.org/wiki/User_mode "User mode") o [kernel mode](https://it.wikipedia.org/wiki/Kernel_mode "Kernel mode").
%%

### 1.1.1 - Classificazione dei kernel

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

## 1.2 - Shell

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

## 1.3 - File system

%%
The file system enables the user to view, organize, secure, and interact with, in a consistent manner,
files and directories located on storage devices.
%%

%%
\### File system in UNIX

Files have names: file extension does not imply anything about the content, it is just part of the name
• In most file systems, files are arranged in a tree structure
• Directories are special files which may contain other files
• The root of the tree is "/"
• The full pathname of a file is the list of all directories from the root
• "/" until the directory of the file
• "." is the current directory
• ".." is the parent directory
• "~" is the home directory of the user
• Files may be links to other files: command ln to create links

Files are an abstraction of anything that can be viewed as a sequence of
bytes: the disk is a (special) file
• More in general, there are 7 types of files:
	- (marked by "-" in ls -l) regular file: contains data, are on disk
	- (marked by "d" in ls -l) directories: contains names of other files
	- (marked by "c" in ls -l) character special file: used to read/write devices byte by byte (stat
	/dev/urandom)
	- (marked by "b" in ls -l) block special file: used to read/write to devices in block (disks). Try stat
	/dev/sda1
	- (marked by "p" in ls -l) FIFO: a special file used for interprocess communication (IPC)
	- (marked by "s" in ls -l) socket: used for network communication
	- (marked by "l" in ls -l) symbolic link: it just points to another file
• try `stat <some-file>`, stat /dev/sda1 to view status and type of any file
• the disk is a file: cat /dev/sda1 to show its content

![](Pasted%20image%2020241110160903.png)
%%

## 1.4 - Gestore dei processi

%%
Una parte specifica del gestore dei processi è lo scheduler
- **Scheduler**: è il componente fondamentale dei sistemi operativi [multitasking](), cioè quelli in grado di eseguire più [processi]() contemporaneamente, e si occupa di fare avanzare un processo interrompendone temporaneamente un altro, realizzando così un [cambio di contesto]() (context switch).
%%

### 1.4.1 - Scheduler

%%
No, il **gestore dei processi** e lo **scheduler** non sono la stessa cosa, anche se lavorano a stretto contatto nella gestione dei processi in un sistema operativo.

### 1.4.2 - Differenza tra Gestore dei Processi e Scheduler

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

## 1.5 - Gestore della memoria

%%
Sometimes a process requires more memory than is available (too many other processes running, for example).
This is where virtual memory comes in.
- When there isn't enough physical memory, the system tries to accommodate the process by moving portions of it to the hard disk.
- When the portion of the process that was moved to hard disk is needed again, it is returned to physical memory. This procedure, called paging, allows the system to provide multitasking capabilities, even with limited physical memory.

- Another aspect of virtual memory is called swap, whereby the kernel identifies the least-busy process or a process that does not require immediate execution
- The kernel then moves the entire process out of RAM to the hard drive until it is needed again, at which point it can be run from the hard drive or from physical RAM.
- The difference between the two is that paging moves only part of the process to the hard drive, while swapping moves the entire process to hard drive space. The segment of the hard drive used for virtual memory is called the swap space in Unix.
%%

## 1.6 - Gestore dei dispositivi I/O

%%
Il modulo di **gestione dei dispositivi I/O** e i **driver** di periferica consentono al sistema operativo di comunicare con hardware specifico (come stampanti, schede di rete, e dischi). I driver traducono i comandi generali del sistema operativo in istruzioni specifiche per i dispositivi.
%%

%% 
Ogni dispositivo I/O è composto da un device controller che contiene un buffer per la memoria e dei registri che si contendono l'uso della memoria con la CPU. Il sistema operativo dispone di un driver per ogni device controller che consente di astrarre la logica della loro gestione.
%%

%% 
Il kernel comunica con gli applicativi tramite:
- Interrupt: eventi asincroni dai dispositivi.
- Exceptions: eventi sincroni da istruzioni.

In particolare, per gli interrupt, la CPU dispone di un pin chiamato INT che viene controllato dopo l'esecuzione di ogni istruzione e che, se viene attivato:
1. Viene letto il valore dell'interrupt
2. Viene salvato lo stato del Program Counter e dei registri in appositi registri dedicati
3. Usa il valore come indice nel vettore delle interruzioni per cercare la corrispondenzna
4. Esegue le istruzioni trovate nel vettore, sovrascrivendo il PC
5. Ripristina lo stato precedente all'interrupt ed esegue l'istruzione di ritorno dall'interrupt

Interrupt chaining:
in alcuni casi sono presenti troppi gestori e, per farli entrare nel vettore delle interruzioni, si fa puntare una collezione di gestori che verranno invocati uno dopo l'altro fin quando non si trova quello giusto (stile liste di trabocco)

Interrupt in sistemi multi-core: vengono assegnati a 1 CPU tramite le logiche degli interrupt controller

Masking e priorità: le CPU hanno un sistema di priorità e due linee di interrupt:
1. Maskable: può essere disattivato dalla CPU
2. Non maskable: non può essere disattivato

Gli I/O comunicano tramite:
- Interrupt: per piccole quantitò di dati
- DMA: il device controller sposta blocchi di dati direttamente nella memoria. La CPU prenderà in carico ogni blocco con un interrupt invece di ogni byte, evitando sovraccarichi (overhead)
- MMIO: memoria virtuale per trasferire da CPU a I/O

Le architetture attualmente possono essere:
- Sistemi a memoria condivisa (multicore o multiprocessore)
	- Ad accesso uniforme a memoria (UMA o SMP, Symmetric MultiProcessing, ogni processore può fare tutto): , sistemi in cui ci sono più processori o cores ma che hanno memoria primaria condivisa (insieme eventualmente a cache)
	- Ad accesso non uniforme (NUMA): ogni CPU o gruppo di CPU ha una memoria locale collegata con un mini bus. Perde efficienza nel caso di operazioni cross nella memoria. L'SO gestisce memroia e processi ma può venire modificato dal programmatore
- Sistemi a memoria **non** condivisa (multicomputer): condividono memoria di massa e sono collegati con LAN. Ogni nodo della rete ha un SO.
- Sistemi con acceleratori hardware (GPU, manycore) con memoria sia condivisa che non
%%

## 1.7 - Gestore della rete

%%
Gestisce la connessione e comunicazione tra computer, implementando protocolli di rete come TCP/IP. Supporta le operazioni di rete come la trasmissione di dati e l'accesso a risorse remote, fondamentale per internet e le reti locali.
%%

## 1.8 - Gestore della sicurezza

# 2 - Tipi di sistemi operativi

I principali tipi di sistemi operativi sono:
- **Sistemi operativi desktop**: sono progettati per essere utilizzati su computer desktop e laptop. Esempi: Windows, macOS, Linux.
- **Sistemi operativi per dispositivi mobili**: sono progettati per essere utilizzati su smartphone e tablet. Esempi: Android, iOS.
- **Sistemi operativi per server**: sono ottimizzati per la gestione di reti, servizi web e database. Esempi: Linux, Windows Server.
- **Sistemi operativi embedded**: sono progettati per dispositivi specifici come router, elettrodomestici e dispositivi IoT (acronimo di _**I**nternet **o**f **T**hings_)%%link%%, con funzionalità limitate e adattate all'hardware specifico.

# 3 - Servizi del sistema operativo

L'SO mette a disposizione:
- User interface: di tipo CLI (shell) o GUI
- Program execution: gestisce le risorse per l'esecuzione dei programmi
- I/O operations: gestisce gli I/O richiesti dall'utente/processo
- Gestione della memoria e file system
- Comunicazione con altri sistemi
- Ricevimento degli errori: sia nel software che nella gestione dell'hardware
- Allocazione delle risorse: per gestire più programmi
- Accounting: monitoraggio delle risorse e degli usi degli utenti
- Protection & security

I servizi sono divisi in:
- Funzioni utili all'utente: process execution, comunicazione, file system, I/O, error handling, GUI
- Funzioni di efficientamento dell'SO: Resource allocation, Accounting, Protection & security.

# 4 - Progettazione di un sistema operativo

L'SO si progetta seguendo obiettivi generici dell'utente e del sistema.

Separation of concerns: nella progettazione bisogna separare policy (che cosa fa) dal mechanism (come lo fa) per garantire maggiore flessibilità all'SO.

# 5 - Installazione e avvio di un sistema operativo

%% 
https://it.wikipedia.org/wiki/Sistema_operativo#Installazione_e_avvio

https://it.wikipedia.org/wiki/Live_USB

Tipicamente il [sistema operativo](Informatica/Sistemi%20operativi/Sistemi%20operativi.md#^definizione-sistema-operativo), una volta installato sulla macchina, risiede nell'hard disk pronto ad essere caricato nella RAM durante la fase di avvio della macchina.

È possibile installare più [sistemi operativi](Informatica/Sistemi%20operativi/Sistemi%20operativi.md#^definizione-sistema-operativo) sulla stessa macchina in modalità dual boot, selezionando poi il sistema desiderato nella fase di avvio del PC attraverso il boot manager. Tutto ciò è possibile solo in virtù dell'operazione di partizionamento della memoria secondaria (hard disk) in più settori logici indipendenti dove ciascuno può ospitare un diverso sistema.

All'accensione del computer il BIOS, dopo la fase di POST, esegue nella cosiddetta fase di boot, attraverso il boot loader, il caricamento del kernel del sistema operativo dall'hard disk alla RAM, come qualunque programma, pronto ad essere eseguito dal processore, rendendo la macchina pronta all'uso da parte dell'utente. Nel caso di sistemi operativi ad interazione con l'utente questa fase, dopo il login iniziale da parte dell'utente stesso, tipicamente comporta anche il caricamento di tutte le impostazioni di configurazione (settings) e profilo utente inizializzando così lo spazio utente.
%%

%% 

## 5.1 - Installazione

Ecco i tool che puoi usare:
- Ventoy (MS, Linux)
- Rufus (MS, Linux con Wine)
- `dd` (Linux)
- WoeUSB su Linux per installare Windows
- USBImager su Linux per installare Windows ma mi dava problemi perché il boot manager non vedeva la chiavetta

### 5.1.1 - Ventoy

Carino, ma ho avuto problemi quando ho provato a fare il dual boot Windows-NixOS perché NixOS con Ventoy non sa dove andare a pescare l'ISO da montare e contemporaneamente mantiene tutti i dispositivi come _busy_ senza la possibilità di sbloccarli

### 5.1.2 - Rufus

### 5.1.3 - `dd`

```
sudo dd if="~/Downloads/nixos-graphical-25.11.8107.1073dad219cb-x86_64-linux.iso" of="/dev/sdb" status="progress" conv="fsync" bs=4M
```
### 5.1.4 - WoeUSB

```
sudo woeusb --device ~/Downloads/Win10_22H2_EnglishInternational_x64v1.iso /dev/sdb
```

%%

%% 
https://itsfoss.com/live-usb-with-dd-command/

❗ L’ISO di Windows non è un’immagine ibrida avviabile tramite dd

Le ISO ufficiali Windows 10/11 non sono ibridate per il direct-write, a differenza di Linux.
Microsoft richiede sempre:

Media Creation Tool
oppure

Rufus
oppure

Ventoy (con plugin Windows)
oppure

WoeUSB (Linux)

%%

%% 
## 5.2 - Linux’s ISOHybrids vs. Windows ISOs

The differences between Linux and Windows installation ISO images and the concept of an "isohybrid" image are essential to understand, especially if you’re working with bootable USB drives.

### 5.2.1 - Linux ISO Images

Many Linux distributions use ISO images that are "isohybrid." It’s a type of ISO file that combines features of a traditional [ISO 9660 CD-ROM](https://en.wikipedia.org/wiki/ISO_9660) and a hard disk image.

Unlike traditional ISO images, such as Windows ones, **an isohybrid image contains special code in its boot sector** that allows it to be bootable when written directly to a USB flash drive and bootable when written to a CD or DVD.

As a result, they are generally more flexible regarding the methods used for creating bootable USB drives. Here’s why tools like `dd` can directly write these ISO images to USB drives, and the drives will boot correctly.

### 5.2.2 - Windows ISO Images

Windows installation ISOs are typically not isohybrid. They are designed with the assumption that they will be burned to a DVD. As such, simply writing these ISOs directly to a USB drive using a method like `dd` will not make them bootable.

Why? Because the bootloader setup in Windows ISOs is different from most Linux distributions. This requires a specific process to create a bootable USB that involves extracting the contents of the ISO and then correctly setting up the bootloader on the USB drive.

Fortunately, Linux offers excellent tools that are ideally suited for this job. We highly recommend WoeUSB, which we will use in the following example to create a Windows bootable USB from an ISO file.
%%

---

> [!fonti]+ Fonti
> 
> - 🏫 Corso di Laurea in Informatica (`L-31 R`) presso l'Università di Torino:
>     - Corso di _Sistemi Operativi - canale B_, A.A. 2024-25 ([pagina Moodle](https://informatica.i-learn.unito.it/course/view.php?id=2956)):
> 		- Prof. Aldinucci Marco, lezioni in aula e slide:
> 			- [_Capitolo 3_](https://informatica.i-learn.unito.it/mod/resource/view.php?id=253884).
> 	- Corso di _Laboratorio di Sistemi Operativi - canale B, turno T4_, A.A. 2024-25 ([pagina Moodle](https://informatica.i-learn.unito.it/course/view.php?id=3038)):
> 		- Prof. Schifanella Claudio, lezioni in aula e slide:
> 			- [_Introduzione al corso e introduzione a UNIX_](https://informatica.i-learn.unito.it/pluginfile.php/422768/mod_resource/content/2/01_introduzione_UNIX.pdf).
> - 📚 Abraham Silberschatz, Peter Baer Galvin, Greg Gagne, [_Sistemi Operativi (10ᵃ Edizione)_](https://he.pearson.it/catalogo/1099), Pearson, 2019 (ISBN: `9788891904560`).

%% 
quali capitoli del libro di sistemi operativi?
%%

%%
- 🏫 Appunti di Carlos Palomino del corso di Sistemi Operativi, Corso di Laurea in Informatica presso l'Università di Torino, A.A. 2024-25 (caricati sul repository GitHub del Team Studentesco Informatica):
	- [[SO] - L01-L02 2024.09.28.pdf](https://github.com/tsi-unito/guida_degli_studenti_di/blob/master/Materie/SO/appunti/2024_2025_B/teoria/%5BSO%5D%20-%20L01-L02%202024.09.28.pdf "[SO] - L01-L02 2024.09.28.pdf")
	- [[SO] - L03 2024.09.28.pdf](https://github.com/tsi-unito/guida_degli_studenti_di/blob/master/Materie/SO/appunti/2024_2025_B/teoria/%5BSO%5D%20-%20L03%202024.09.28.pdf "[SO] - L03 2024.09.28.pdf")
	- [[SO] - L04 2024.09.28.pdf](https://github.com/tsi-unito/guida_degli_studenti_di/blob/master/Materie/SO/appunti/2024_2025_B/teoria/%5BSO%5D%20-%20L04%202024.09.28.pdf "[SO] - L04 2024.09.28.pdf")
%%
