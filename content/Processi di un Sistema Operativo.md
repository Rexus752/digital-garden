%% Prova
Controllare nei codici di esempio che sia scritto tutto in italiano, verbi all'imperativo ecc.

---

\# Storia

I primi sistemi elaborativi consentivano l'esecuzione di un solo programma alla volta, che aveva il completo controllo del sistema e accesso a tutte le sue risorse. Gli attuali sistemi elaborativi consentono, invece, che più programmi siano caricati in memoria ed eseguiti in modo concorrente. Tale evoluzione richiede un più severo controllo e una maggiore compartimentazione dei vari programmi. Da tali necessità deriva la nozione di processo d'elaborazione – o, più brevemente, processo – che in prima istanza si può definire come un programma in esecuzione, e costituisce l'unità di lavoro dei moderni sistemi time-sharing.

---

Differenza tra multitasking e multiprogrammazione

La **differenza tra multitasking e multiprogrammazione** riguarda il modo in cui i sistemi operativi gestiscono l'esecuzione dei processi, ed entrambi i concetti si riferiscono a tecniche per massimizzare l'utilizzo delle risorse della CPU e migliorare l'efficienza. Tuttavia, ci sono distinzioni importanti tra i due termini:

\### Multiprogrammazione
- **Definizione**: La **multiprogrammazione** è una tecnica in cui più programmi (o processi) sono caricati in memoria principale (RAM) **simultaneamente**, permettendo alla CPU di passare da un processo all'altro quando un processo è bloccato (ad esempio, in attesa di un'operazione di input/output). L'obiettivo principale è **massimizzare l'uso della CPU** e ridurre i tempi di inattività.
  
- **Funzionamento**:
  - La CPU esegue un processo finché questo non è bloccato (per esempio, attende che un'operazione di I/O sia completata).
  - Quando un processo è bloccato, la CPU passa ad un altro processo che è pronto per essere eseguito.
  - Non esiste un'idea di "condivisione di tempo" precisa come nel multitasking; la CPU viene assegnata ai processi a seconda della disponibilità.

- **Caratteristiche**:
  - **Esecuzione non interattiva**: La multiprogrammazione è più orientata verso sistemi **batch**, in cui i processi non richiedono interazione immediata da parte degli utenti. Un esempio comune sono i sistemi batch utilizzati per l'elaborazione di grandi quantità di dati.
  - **Esecuzione sequenziale dei processi**: La CPU esegue un processo fino a quando questo non si blocca, e solo allora passa al successivo.
  - **Non c'è time-sharing**: Il tempo non è suddiviso in intervalli regolari, e un processo può monopolizzare la CPU finché non richiede operazioni di I/O.

- **Obiettivo**: Minimizzare i tempi morti della CPU e migliorare l'efficienza complessiva.

\### Multitasking
- **Definizione**: Il **multitasking** è una tecnica in cui **più processi** vengono eseguiti **quasi contemporaneamente**, suddividendo il tempo della CPU in piccoli intervalli (detti **time-slice** o **quantum**) tra i vari processi. L'obiettivo del multitasking è **fornire l'illusione di esecuzione parallela** dei processi e migliorare l'interattività del sistema.
  
- **Funzionamento**:
  - La CPU passa velocemente da un processo all'altro, in modo che ciascun processo venga eseguito per un breve periodo di tempo (quantum).
  - Anche se un processo non è bloccato, viene sospeso temporaneamente dopo che il suo quantum di tempo è scaduto, permettendo ad altri processi di essere eseguiti.
  - Questo dà l'**illusione di esecuzione simultanea** per più processi, poiché il passaggio tra processi avviene molto rapidamente.

- **Caratteristiche**:
  - **Esecuzione interattiva**: Il multitasking è essenziale per i sistemi **interattivi**, come i computer desktop o i server, dove gli utenti eseguono molteplici programmi contemporaneamente (ad esempio, un browser web, un editor di testi e un lettore musicale).
  - **Time-sharing**: Il sistema operativo assegna la CPU ai processi per brevi intervalli di tempo, garantendo che tutti i processi attivi ricevano una porzione di tempo CPU.
  - **Cambio di contesto frequente**: Il multitasking richiede frequenti cambi di contesto, poiché la CPU passa regolarmente da un processo all'altro.

- **Obiettivo**: Migliorare l'**interattività** del sistema e dare agli utenti l'impressione che più attività vengano eseguite contemporaneamente.

\### Differenze principali:

| Caratteristica              | **Multiprogrammazione**                                     | **Multitasking**                                            |
|-----------------------------|-------------------------------------------------------------|-------------------------------------------------------------|
| **Focus principale**         | Massimizzare l'uso della CPU minimizzando i tempi di inattività. | Fornire esecuzione simultanea apparente e interattività.    |
| **Tipo di esecuzione**       | Non interattiva, orientata ai sistemi batch.                | Interattiva, orientata agli utenti e sistemi interattivi.    |
| **Time-sharing**             | Non c'è divisione precisa del tempo CPU.                    | La CPU è condivisa tra i processi in piccoli intervalli (quantum). |
| **Cambio di contesto**       | Avviene quando un processo è bloccato (ad esempio, attesa di I/O). | Avviene regolarmente, anche se i processi non sono bloccati. |
| **Obiettivo**                | Migliorare l'efficienza della CPU.                          | Migliorare l'interattività per l'utente.                     |
| **Esempi di utilizzo**       | Sistemi batch, mainframe.                                  | Sistemi operativi moderni (Windows, Linux, macOS).           |

\### Esempio pratico:</span>
- **Multiprogrammazione**: In un sistema batch, un processo che elabora un grande file di dati potrebbe essere sospeso quando inizia un'operazione di lettura da disco, e durante questo tempo, un altro processo può usare la CPU per elaborare i suoi dati. Quando l'operazione di I/O è completata, il primo processo riprende l'esecuzione.
  
- **Multitasking**: In un sistema operativo come Windows o Linux, un utente può ascoltare musica, navigare sul web e scrivere in un editor di testo contemporaneamente. Il sistema operativo assegna piccoli intervalli di tempo a ciascuno di questi processi, creando l'illusione che vengano eseguiti simultaneamente.

In sintesi, la **multiprogrammazione** si concentra sull'efficienza della CPU, mentre il **multitasking** si concentra sull'interattività e sulla gestione di più attività per l'utente.

---

Multitasking nei sistemi per dispositivi mobili:
A causa dei vincoli imposti sui dispositivi mobili, le prime versioni di ios non fornivano il multitasking per le
applicazioni utente; una sola applicazione veniva eseguita in foreground, mentre tutte le altre erano sospese. I processi
del sistema operativo erano invece gestiti in multitasking, perché essendo scritti da Apple si comportavano in maniera
corretta. A partire da ios 4 Apple offre una forma limitata di multitasking per le applicazioni utente, consentendo così
all'applicazione in foreground di funzionare contemporaneamente a più applicazioni in background. Su un dispositivo
mobile, l'applicazione in foregroud è l'applicazione aperta al momento e che appare sul display. L'applicazione in
background rimane in memoria, ma non occupa lo schermo del display. L'api ios 4 fornisce il supporto per il
multitasking, permettendo così a un processo di rimanere in esecuzione in background senza essere sospeso. Tuttavia,
questa possibilità è limitata e disponibile soltanto per un numero ridotto di tipologie di applicazioni. Quando l'hardware
dei dispositivi mobili ha iniziato a offrire memorie più grandi, diversi core di elaborazione e una maggiore durata della
batteria, le versioni di iOS hanno iniziato a supportare funzionalità più complete e meno restrittive per il multitasking.
Per esempio, lo schermo più grande sui tablet iPad consentiva di eseguire due app in primo piano contemporaneamente, una tecnica nota come split-screen.
Fin dalle sue origini, Android ha supportato il multitasking e non ha posto vincoli sulle tipologie di applicazioni che
possono essere eseguite in background. Un'applicazione che voglia richiedere l'elaborazione mentre è in background
deve utilizzare un servizio, un componente applicativo separato che viene eseguito per conto del processo in background.
Si consideri un'applicazione di streaming audio: se l'applicazione si sposta in background, il servizio continua a inviare
i file audio al driver di periferica audio per suo conto. Il servizio continuerà a funzionare anche se l'applicazione in
background viene sospesa. I servizi non hanno un'interfaccia utente e hanno un ingombro di memoria modesto,
fornendo così una tecnica efficace per il multitasking in un ambiente mobile.

• Some mobile systems (e.g., early version of iOS) allow only one process to run, others suspended
• Due to screen real estate, user interface limits iOS provides for a
	• Single foreground process- controlled via user interface
	• Multiple background processes– in memory, running, but not on the display, and with limits
	• Limits include single, short task, receiving notification of events, specific long-running tasks like audio playback
• Android runs foreground and background, with fewer limits
	• Background process uses a service to perform tasks
	• Service can keep running even if background process is suspended
	• Service has no user interface, small memory use

---

3.3.2.1 Gerarchia dei processi Android
A causa dei vincoli imposti dalle risorse, come la memoria limitata, i sistemi operativi mobili possono aver bisogno di terminare
processi esistenti per recuperare risorse di sistema. Anziché terminare un processo arbitrario, Android ha definito una gerarchia di
importanza dei processi. Quando il sistema deve terminare un processo per rendere disponibili le risorse per un processo nuovo o più
importante, esso effettua la scelta di quale processo terminare in base all'ordine crescente di importanza. Dal più al meno importante,
la classificazione gerarchica dei processi è la seguente.
Processo in primo piano: il processo visibile sullo schermo, che rappresenta l'applicazione con cui l'utente sta attualmente
interagendo.
Processo visibile: un processo che non è direttamente visibile in primo piano, ma che sta eseguendo un'attività a cui il processo
in primo piano fa riferimento (vale a dire, un processo che esegue un'attività il cui stato è visualizzato dal processo in primo
piano).
Processo di servizio: un processo simile a un processo in background, ma che sta eseguendo un'attività evidente all'utente
(come lo streaming di musica).
Processo in background: un processo che può svolgere un'attività non evidente all'utente.
Processo vuoto: un processo che non contiene componenti attive associate a un'applicazione.
Se occorre recuperare risorse di sistema, Android interrompe prima i processi vuoti, poi i processi in background, e così via. Ai
processi viene assegnata una valutazione di importanza e Android assegna a un processo la posizione più alta possibile. Per esempio,
se un processo fornisce un servizio ed è anche visibile, gli verrà assegnata la classificazione di processo visibile più importante.
Inoltre, le prassi di sviluppo Android suggeriscono di seguire le linee guida del ciclo di vita dei processi, che prevedono che lo stato di
un processo sia salvato prima della sua terminazione e ripristinato quando l'utente ritorna all'applicazione.

---

Link a UNIX & Linux
Controllare che UNIX sia scritto tutto in maiuscolo

---

https://stackoverflow.com/questions/5815675/what-is-sock-dgram-and-sock-stream/60425748#60425748

%%

# Indice

- **1 - Cos'è un processo**
	- **1.1 - Differenza tra processo e programma**
		- **1.1.1 - Multipli processi, stesso programma**
- **2 - Il PCB e le informazioni sul processo**
	- **2.1 - Informazioni contenute in un PCB**
	- **2.2 - Funzione del PCB**
	- **2.3 - Stato di un processo**
		- **2.3.1 - Cambiamenti di stato di un processo**
		- **2.3.2 - Utilità degli stati**
	- **2.4 - Spazio di memoria**
		- **2.4.1 - Variazione della grandezza dei segmenti di memoria**
- **3 - Schedulazione dei processi**
	- **3.1 - Obiettivi della schedulazione dei processi**
	- **3.2 - Code di schedulazione**
		- **3.2.1 - Principali code di schedulazione**
		- **3.2.2 - Rappresentazione in memoria delle code di schedulazione**
	- **3.3 - Tipi di schedulazione**
	- **3.4 - Il cambio di contesto**
		- **3.4.1 - Utilità e vantaggi del cambio di contesto**
		- **3.4.2 - Come funziona il cambio di contesto**
		- **3.4.3 - Costi del cambio di contesto**
	- **3.5 - Parametri di performance della schedulazione**
- **4 - Processi I/O-bound e CPU-bound**
	- **4.1 - Processo I/O-bound**
		- **4.1.1 - Caratteristiche principali dei processi I/O-bound**
	- **4.2 - Processo CPU-bound**
		- **4.2.1 - Caratteristiche principali dei processi CPU-bound**
	- **4.3 - Differenze principali tra i due tipi**
	- **4.4 - Importanza per la schedulazione**
- **5 - Operazioni sui processi**
	- **5.1 - Creazione di un processo**
		- **5.1.1 - Fasi principali della creazione di un processo**
		- **5.1.2 - `fork()` in Unix/Linux**
		- **5.1.3 - `CreateProcess()` in Windows**
	- **5.2 - Terminazione di un processo**
		- **5.2.1 - Fasi principali della terminazione di un processo**
		- **5.2.2 - Codice di uscita**
		- **5.2.3 - Terminazione a cascata**
			- **5.2.3.1 - Funzionamento della terminazione a cascata**
			- **5.2.3.2 - Esempio di terminazione a cascata in linguaggio C**
	- **5.3 - Comunicazione tra processi**
		- **5.3.1 - Pipe**
			- **5.3.1.1 - Caratteristiche principali delle pipe**
			- **5.3.1.2 - Funzionamento di base delle pipe**
				- **5.3.1.2.1 - Esempio di codice in linguaggio C**
			- **5.3.1.3 - Vantaggi e svantaggi delle pipe**
			- **5.3.1.4 - Named pipe**
		- **5.3.2 - Code di messaggi**
			- **5.3.2.1 - Caratteristiche principali delle code di messaggi**
			- **5.3.2.2 - Funzionamento delle code di messaggi**
				- **5.3.2.2.1 - Esempio di codice in linguaggio C**
			- **5.3.2.3 - Vantaggi e svantaggi delle code di messaggi**
		- **5.3.3 - Memoria condivisa**
			- **5.3.3.1 - Caratteristiche principali della memoria condivisa**
			- **5.3.3.2 - Funzionamento della memoria condivisa**
				- **5.3.3.2.1 - Esempio di codice in linguaggio C**
			- **5.3.3.3 - Vantaggi e svantaggi della memoria condivisa**
		- **5.3.4 - Socket**
			- **5.3.4.1 - Caratteristiche principali dei socket%% SISTEMARE %%**
				- **5.3.4.1.1 - Half-duplex e full-duplex**
					- **5.3.4.1.1.1 - Half-duplex**
					- **5.3.4.1.1.2 - Full-duplex**
					- **5.3.4.1.1.3 - Tabella riassuntiva delle differenze**
				- **5.3.4.1.2 - Famiglie di socket**
				- **5.3.4.1.3 - Tipo di socket**
				- **5.3.4.1.4 - Orientamento alla connessione**
					- **5.3.4.1.4.1 - Connection-oriented (orientato alla connessione)**
					- **5.3.4.1.4.2 - Connectionless (senza connessione)**
					- **5.3.4.1.4.3 - Tabella riassuntiva delle differenze**
			- **5.3.4.2 - Vantaggi e svantaggi dei socket**
			- **5.3.4.3 - Internet socket**
				- **5.3.4.3.1 - Funzionamento degli internet socket**
- **6 - Thread**
	- **6.1 - Differenza tra processo e thread**
	- **6.2 - Utilità dei thread**

# 1 - Cos'è un processo

Il processo è un'istanza di un programma in esecuzione su un computer e rappresenta una delle unità fondamentali di gestione delle risorse da parte di un sistema operativo. Quando un programma viene eseguito, il sistema operativo crea un processo per esso, fornendogli le risorse necessarie, come CPU, memoria, accesso ai file e altri dispositivi. Ogni processo è identificato da un codice univoco chiamato _PID_ (_Process ID_).

Può essere visibile all'utente, come nel caso di un'applicazione durante la sua esecuzione, oppure può essere eseguito in background; per visualizzare la lista completa dei processi eseguiti su un computer e le relative risorse impiegate è possibile utilizzare un software comunemente chiamato _task manager_, mentre la gestione dei processi da parte del sistema operativo è affidata a un particolare programma, detto _process scheduler_, attraverso opportuni algoritmi di schedulazione%%link%%.

## 1.1 - Differenza tra processo e programma

La differenza  tra il concetto di "processo" e quello di "programma" è fondamentale in informatica, poiché indicano concetti distinti legati all'esecuzione di un'applicazione:
- Un **programma** è un insieme di istruzioni scritte in un linguaggio di programmazione, che descrive quali operazioni un computer deve eseguire. È un'entità **passiva** e rappresenta il codice sorgente o il codice binario di un'applicazione, che viene memorizzato in un file su disco (es. un file eseguibile `.exe` su Windows, oppure un documento contenente codice sorgente scritto in un linguaggio di programmazione come Python o C). Un programma non fa nulla da solo finché non viene avviato.
- Un **processo** è un'istanza di un programma in esecuzione sulla memoria centrale (RAM). È un'entità **attiva** che include il codice del programma, lo stato della CPU (come il contatore del programma e i registri), lo spazio di memoria (segmento di testo e dei dati, stack e heap) e le risorse utilizzate dal programma. Quando un programma viene eseguito, il sistema operativo crea un processo per gestirne l'esecuzione.

Ecco una tabella riassuntiva:

| Caratteristica  | **Programma**                                      | **Processo**                                                  |
| --------------- | -------------------------------------------------- | ------------------------------------------------------------- |
| **Definizione** | Un insieme di istruzioni memorizzate su disco      | Un'istanza di un programma in esecuzione                      |
| **Stato**       | Entità passiva                                     | Entità attiva                                                 |
| **Memoria**     | Non usa memoria attiva                             | Utilizza memoria (segmento di testo e dei dati, stack e heap) |
| **Esecuzione**  | Non è in esecuzione                                | In esecuzione                                                 |
| **Durata**      | Permanente fino a quando è cancellato o modificato | Temporanea, esiste solo durante l'esecuzione                  |
| **Gestione**    | Non richiede gestione attiva                       | Gestito dal sistema operativo (CPU, memoria, I/O)             |
| **Relazione**   | Un programma può generare più processi             | Ogni processo è basato su un programma                        |

### 1.1.1 - Multipli processi, stesso programma

Sebbene due processi siano associabili allo stesso programma, sono tuttavia da considerare due sequenze d'esecuzione distinte: alcuni utenti possono, per esempio, far eseguire diverse istanze dello stesso programma di posta elettronica, così come un utente può invocare più istanze dello stesso browser. Ciascuna di queste è un diverso processo e, benché le sezioni di memoria contenenti il codice siano equivalenti, in realtà quelle dei dati, dell'heap e dello stack sono diverse. È inoltre usuale che durante la propria esecuzione un processo generi altri processi.

# 2 - Il PCB e le informazioni sul processo

Il **blocco di controllo del processo** (in inglese _PCB_, _Process Control Block_) è una struttura dati fondamentale utilizzata dal sistema operativo per memorizzare tutte le informazioni relative a un processo in esecuzione. Il PCB contiene informazioni cruciali per la gestione del processo, come il suo [stato](Processi%20di%20un%20Sistema%20Operativo.md#2.3%20-%20Stato%20di%20un%20processo), l'allocazione delle risorse, la sua posizione nella memoria e molto altro. Ogni processo attivo nel sistema ha un PCB associato, che viene creato al momento della sua inizializzazione, memorizzato nella RAM e aggiornato durante l'intero ciclo di vita del processo.

## 2.1 - Informazioni contenute in un PCB

Le informazioni contenute in un PCB variano a seconda delle implementazioni nei vari sistemi operativi, ma in generale sono presenti:
1. [**Stato del processo**](Processi%20di%20un%20Sistema%20Operativo.md#2.3%20-%20Stato%20di%20un%20processo): la condizione in cui si trova un processo in un dato momento durante la sua esecuzione nel sistema operativo (`new`, `ready`, `running`, `waiting` o `terminated`).
2. **Identificatore del processo (PID, Process ID)**: un numero univoco assegnato al processo dal sistema operativo. Questo identificatore viene utilizzato per distinguere il processo dagli altri processi attivi.
3. **Program Counter (PC)**: il PCB salva il valore contenuto nel Program Counter%%link%%, il registro nella CPU che rappresenta l'indirizzo dell'istruzione successiva che il processo deve eseguire. Se il processo viene interrotto, il Program Counter consente di riprendere l'esecuzione dal punto in cui è stata interrotta, perché appunto conterrà il valore dell'indirizzo di memoria in cui è presente l'istruzione del processo da cui ripartire.
4. **Contenuto dei registri della CPU**: il PCB salva il contenuto dei registri della CPU (es. accumulatori, puntatori allo stack, registri di uso generale) nel momento in cui il processo è stato interrotto. Questo è essenziale per riprendere correttamente l'esecuzione del processo in un successivo [cambio di contesto](Processi%20di%20un%20Sistema%20Operativo.md#3.4%20-%20Il%20cambio%20di%20contesto).
5. **Informazioni sulla gestione della memoria**: include dati su come la memoria è allocata al processo, come indirizzi di base e limiti di memoria del processo, oppure tabelle di paginazione o segmentazione, nel caso il sistema operativo utilizzi tecniche di gestione della memoria virtuale.
6. **Informazioni di I/O**: un elenco dei dispositivi di input/output utilizzati dal processo (es. file aperti, dispositivi hardware come stampanti, reti) e file descriptor che fanno riferimento ai file aperti dal processo.
7. **Informazioni di schedulazione**: un elenco delle informazioni utili alla schedulazione della CPU, come:
	- **Priorità del processo**: indica l'importanza relativa del processo rispetto agli altri.
	- **Tempo di esecuzione accumulato**: il tempo che il processo ha trascorso in esecuzione.
	- **Algoritmo di schedulazione utilizzato**: se il sistema operativo utilizza diverse politiche di schedulazione, nel PCB viene specificata quale viene usata.
8. **Informazioni di accounting**: dati utilizzati per tenere traccia del tempo CPU consumato dal processo, della quantità di risorse utilizzate e di eventuali statistiche di utilizzo, utili per la fatturazione o il monitoraggio delle prestazioni.
9. **Informazioni sui segnali**: elenco dei segnali che il processo può ricevere e le relative azioni da eseguire al ricevimento di un segnale (ad esempio, terminare il processo o ignorare il segnale).

## 2.2 - Funzione del PCB

Il PCB svolge un ruolo cruciale nel gestire i processi nel sistema operativo. Le sue principali funzioni includono:
- **Salvataggio del contesto del processo**: quando un processo viene sospeso (ad esempio, per un [cambio di contesto](Processi%20di%20un%20Sistema%20Operativo.md#3.4%20-%20Il%20cambio%20di%20contesto)), il suo stato (registri CPU, Program Counter, ecc.) viene memorizzato nel PCB. Quando il processo viene ripreso, il contesto viene ripristinato.  
- **Gestione della memoria**: il PCB tiene traccia delle risorse di memoria utilizzate dal processo, assicurando che il processo non acceda a zone di memoria riservate ad altri processi o al sistema operativo.
- **Identificazione del processo**: grazie al PID e alle altre informazioni contenute nel PCB, il sistema operativo può gestire un numero elevato di processi contemporaneamente, distinguendo un processo dall'altro.
- **Schedulazione e gestione della priorità**: le informazioni di priorità e di tempo di esecuzione accumulate nel PCB consentono al sistema operativo di decidere quale processo eseguire in un dato momento, ottimizzando l'uso della CPU.

## 2.3 - Stato di un processo

Lo **stato di un processo** rappresenta la condizione in cui si trova un processo in un dato momento durante la sua esecuzione nel sistema operativo. Il sistema operativo utilizza questi stati per gestire i processi in modo efficiente, garantendo che la CPU venga utilizzata in modo ottimale.

Gli stati principali di un processo sono:
- **`new` (nuovo)**: il processo è appena stato creato, ma non è ancora pronto per essere eseguito. Si trova in fase di inizializzazione, durante la quale vengono assegnate risorse come memoria e ID del processo.
- **`ready` (pronto)**: il processo è pronto per essere eseguito ma sta aspettando che la CPU diventi disponibile. In questo stato, il processo ha tutto ciò di cui ha bisogno per essere eseguito (memoria, dati, risorse), ma la CPU è attualmente occupata con un altro processo.
- **`running` (in esecuzione)**: il processo sta attualmente utilizzando la CPU e le sue istruzioni vengono eseguite. Il sistema operativo ha assegnato il controllo della CPU al processo, che sta attivamente svolgendo il suo lavoro.
- **`waiting` o `blocked` (in attesa o bloccato)**: il processo è in attesa di un evento esterno per continuare l'esecuzione. Questo evento può essere, ad esempio, il completamento di un'operazione di input/output (I/O), la ricezione di dati o un messaggio. In questo stato, il processo non può proseguire fino a che l'evento atteso non si verifica.
- **`terminated` (terminato)**: il processo ha completato la sua esecuzione o è stato interrotto in modo anomalo (per esempio, a causa di un errore). In questo stato, tutte le risorse del processo vengono rilasciate e il processo non esiste più nel sistema.

Questi termini sono piuttosto arbitrari e potrebbero variare a seconda del sistema operativo. Gli stati che rappresentano sono in ogni modo presenti in tutti i sistemi, anche se alcuni sistemi operativi introducono ulteriori distinzioni tra di essi. È importante capire che in ciascuna unità d'elaborazione può essere in esecuzione solo un processo per volta, sebbene molti processi possano essere pronti o nello stato di attesa.

### 2.3.1 - Cambiamenti di stato di un processo

In un sistema operativo, un processo può attraversare diversi **cambiamenti di stato** a seconda delle sue interazioni con le risorse del sistema e con altri processi. Questi cambiamenti di stato riflettono come il sistema operativo gestisce l'allocazione della CPU e l'attesa di eventi esterni, come l'input/output (I/O). Il seguente diagramma rappresenta la transizione tra i vari stati di un processo:

```mermaid
stateDiagram-v2
	direction LR
    New --> Ready: 1
    Ready --> Running: 2
    Ready --> Terminated: 3
    Running --> Ready: 4
    Running --> Waiting: 5
    Running --> Terminated: 6
    Waiting --> Running: 7
    Waiting --> Terminated: 8
```

%%
Nel rendering sul sito, centrare il diagramma di Mermaid
%%

In particolare:
1. **`new` → `ready`**: dopo che il sistema operativo ha completato l'inizializzazione del processo e assegnato le risorse necessarie (come la memoria), il processo entra nello stato `ready`, in attesa di essere schedulato per l'esecuzione.
2. **`ready` → `running`**: il sistema operativo seleziona il processo dalla coda dei processi pronti e lo assegna alla CPU. A questo punto, il processo inizia a essere eseguito.
3. **`ready` → `terminated`**: anche se raro, un processo potrebbe essere terminato mentre è in stato `ready`, magari a causa di un'azione manuale dell'utente o per altre ragioni di sistema.
4. **`running` → `ready`**: il sistema operativo può interrompere il processo (ad esempio, a causa di un'interruzione del timer%%, come accade con l'algoritmo di schedulazione round-robin (aggiungere link)%%). In questo caso, il processo viene sospeso e rimesso nella coda dei processi pronti%%ready queue%%, aspettando di ottenere nuovamente la CPU.
5. **`running` → `waiting`**: se il processo richiede un'operazione di I/O o deve attendere che un evento specifico accada (ad esempio, il completamento di una lettura da disco), viene sospeso ed entra nello stato `waiting` fino a quando l'evento non si verifica.
6. **`running` → `terminated`**: quando il processo completa la sua esecuzione (o si verifica un errore fatale), entra nello stato `terminated`, liberando tutte le risorse allocate.
7. **`waiting` → `ready`**: una volta che l'evento atteso si verifica (ad esempio, un'operazione I/O termina), il processo torna nello stato `ready`, poiché ha tutto ciò di cui ha bisogno per continuare l'esecuzione e aspetta solo che la CPU diventi disponibile.
8. **`waiting` → `terminated`**: se il processo viene terminato durante l'attesa di un evento (ad esempio, un errore grave o una terminazione forzata dall'utente), il processo passa direttamente allo stato `terminated`.

Ecco una tabella riassuntiva delle transizioni di stato:

| Stato di partenza | Stato di arrivo | Descrizione della transizione                                  |
| ----------------- | --------------- | -------------------------------------------------------------- |
| `new`             | `ready`         | Il processo viene creato e preparato per l'esecuzione.         |
| `ready`           | `running`       | Il processo ottiene la CPU e inizia a essere eseguito.         |
| `ready`           | `terminated`    | Il processo viene terminato prima di essere eseguito.          |
| `running`         | `ready`         | Il processo viene sospeso (ad esempio, per multitasking).      |
| `running`         | `waiting`       | Il processo attende un'operazione I/O o un evento esterno.     |
| `running`         | `terminated`    | Il processo completa l'esecuzione o termina per errore.        |
| `waiting`         | `ready`         | L'evento atteso si verifica e il processo è pronto a eseguire. |
| `waiting`         | `terminated`    | Il processo viene terminato mentre attende un evento.          |

### 2.3.2 - Utilità degli stati

La gestione degli stati permette al sistema operativo di organizzare l'esecuzione dei processi in modo efficiente: ad esempio, quando un processo è in attesa (`waiting`), il sistema operativo può assegnare la CPU a un altro processo nello stato `ready`, garantendo che la CPU non rimanga inattiva.

## 2.4 - Spazio di memoria

Lo **spazio di memoria di un processo** rappresenta l'insieme di tutte le aree di memoria allocate per un processo dal sistema operativo. Questo spazio contiene il codice eseguibile, i dati e le strutture necessarie per far funzionare il programma. Ogni processo ha il proprio spazio di memoria isolato, separato da quello degli altri processi, garantendo che un processo non possa accedere o modificare direttamente la memoria di un altro processo: questa separazione migliora la sicurezza e la stabilità del sistema.

Lo spazio di memoria di un processo è solitamente diviso in:
1. **Segmento di codice (o segmento testo)**: contiene il codice eseguibile del programma, cioè le istruzioni che la CPU eseguirà. Il segmento di codice è generalmente di sola lettura, per evitare che il codice del programma venga accidentalmente modificato.
2. **Segmento dati**: contiene le variabili globali e statiche del programma, divise in:
	- **Dati inizializzati**: l'insieme delle variabili globali e statiche a cui è stato assegnato un valore al momento della dichiarazione.
	- **Dati non inizializzati (BSS, Block Started by Symbol)**: l'insieme delle variabili globali e statiche che sono dichiarate ma non esplicitamente inizializzate, quindi non hanno un valore inizialmente definito; in alcuni sistemi operativi vengono inizializzate a zero.%%approfondire cos'è il BSS%%
3. **Heap**: è l'area della memoria dinamica utilizzata per l'allocazione di memoria a runtime. Quando un programma richiede memoria dinamica (ad esempio tramite funzioni come `malloc()` in C o `new` in C++/Java), questa viene allocata nello heap, il quale viene gestito unicamente dal programmatore stesso (cioè il programmatore è l'unico responsabile della gestione e del rilascio della memoria).
4. **Stack**: area di memoria che viene utilizzata per memorizzare variabili locali, parametri di funzione e indirizzi di ritorno da funzioni. Ogni volta che viene chiamata una funzione, un nuovo "frame" viene aggiunto allo stack, che contiene le informazioni relative a quella particolare chiamata. Quando la funzione termina, lo stack viene "srotolato" e il frame della funzione viene rimosso. Lo stack si espande e si contrae automaticamente durante l'esecuzione del programma, e la sua gestione è di solito curata dal compilatore e dal sistema operativo.
%%approfondire heap e stack in una pagina a parte sulla https://it.wikipedia.org/wiki/Gestione_della_memoria %%

Ecco una rappresentazione grafica dello spazio di memoria di un processo:

![](Spazio%20di%20memoria%20di%20un%20processo.png)
%%rimuovere questa foto e mettere uno schema fatto da me%%

### 2.4.1 - Variazione della grandezza dei segmenti di memoria

Si può notare che le dimensioni dei segmenti di codice e di dati sono fisse, ovvero non cambiano durante l'esecuzione del programma, mentre le dimensioni di stack e heap possono ridursi e crescere dinamicamente durante l'esecuzione:
- Ogni volta che si chiama una funzione, viene inserito nello stack una struttura dati detta _record di attivazione_ (_activation record_) contenente i suoi parametri, le variabili locali e l'indirizzo di ritorno; quando la funzione restituisce il controllo al chiamante, il record di attivazione viene rimosso dallo stack.
- Allo stesso modo, l'heap crescerà quando viene allocata memoria dinamicamente e si ridurrà quando la memoria viene restituita al sistema.

Visto che le sezioni dello stack e dell'heap crescono l'una verso l'altra, tocca al sistema operativo garantire che non si sovrappongano.

# 3 - Schedulazione dei processi

La **schedulazione dei processi** è il meccanismo attraverso il quale il sistema operativo decide quale processo deve essere eseguito dalla CPU in un dato momento. In un sistema multitasking%%link%%, più processi competono per l'utilizzo della CPU ed esiste un programma specifico detto _process scheduler_ il cui ruolo è quello di assegnare la CPU a questi processi in modo efficiente, garantendo che il sistema risponda correttamente alle richieste degli utenti e ottimizzi le prestazioni.

## 3.1 - Obiettivi della schedulazione dei processi

Gli **obiettivi della schedulazione dei processi** sono:
1. **Massimizzare l'utilizzo della CPU**: ridurre i tempi morti della CPU, assicurando che sia sempre in uso.
2. **Condivisione equa**: assicurare che tutti i processi abbiano la possibilità di essere eseguiti, evitando che alcuni processi monopolizzino le risorse.
3. **Ridurre i tempi di risposta**: ridurre il tempo che intercorre tra la richiesta di esecuzione di un processo e l'inizio della sua esecuzione.
4. **Massimizzare la produttività**: aumentare il numero di processi completati in un intervallo di tempo.
5. **Ridurre il tempo di attesa**: minimizzare il tempo che un processo trascorre in attesa di essere eseguito.
6. **Garantire scadenze**: nei sistemi in tempo reale, garantire che i processi rispettino le loro scadenze temporali.

## 3.2 - Code di schedulazione

Le **code di schedulazione** (scheduling queues) sono strutture di dati utilizzate dal sistema operativo per gestire i processi in diverse fasi del loro ciclo di vita. Queste code aiutano il sistema operativo a organizzare e determinare quale processo deve essere eseguito, aspettare o bloccarsi, basandosi su determinati algoritmi di schedulazione%%link%%.

### 3.2.1 - Principali code di schedulazione

Le **principali code di schedulazione** sono:
1. **Job queue**: contiene tutti i processi nel sistema, indipendentemente dallo stato in cui si trovano. Non appena un processo viene creato, viene aggiunto a questa coda.
2. **Ready queue**: contiene tutti i processi che sono pronti per l'esecuzione (cioè nello stato `ready`) e in attesa che la CPU sia disponibile. Lo [schedulatore a breve termine](Processi%20di%20un%20Sistema%20Operativo.md#3.3%20-%20Tipi%20di%20schedulazione) sceglie i processi da questa coda per essere eseguiti. Questa coda è una delle più attive e importanti, poiché determina quali processi avranno accesso alla CPU.
3. **Device queue**: ogni dispositivo di I/O nel sistema ha una propria coda. Quando un processo richiede un'operazione di I/O, entra nella coda del dispositivo corrispondente e rimane bloccato finché l'operazione non viene completata. Dopo che l'I/O è completato, il processo può ritornare nella coda dei processi pronti. Per esempio, se un processo sta aspettando che venga completata la lettura da disco, sarà nella coda del disco fino al termine dell'operazione.
4. **Waiting queue**: contiene processi che sono bloccati in attesa di un evento (cioè nello stato `waiting`), come l'input da un dispositivo o il completamento di una richiesta di I/O. Quando l'evento atteso si verifica, il processo ritorna nella ready queue. È simile alla device queue, ma può anche includere processi in attesa di altri tipi di eventi non legati ai dispositivi di I/O.

### 3.2.2 - Rappresentazione in memoria delle code di schedulazione

Ogni coda generalmente viene memorizzata come una lista concatenata%%link%%, con un'intestazione della coda contenente i puntatori al primo [PCB](Processi%20di%20un%20Sistema%20Operativo.md#2%20-%20Il%20PCB%20e%20le%20informazioni%20sul%20processo) della lista che a sua volta comprende un campo puntatore che indica il successivo processo contenuto nella coda e così via:

![](Pasted%20image%2020241019202031.png)
%%eliminare questo schema e farne uno mio%%

## 3.3 - Tipi di schedulazione

Esistono diversi **tipi di schedulazione**, che variano in base a quando e come viene assegnata la CPU ai processi:
1. **Schedulazione a lungo termine (job scheduler)**: decide quali processi devono essere caricati in memoria principale (RAM) dalla [job queue](Processi%20di%20un%20Sistema%20Operativo.md#3.2.1%20-%20Principali%20code%20di%20schedulazione). Il suo scopo è quello di controllare il grado di multiprogrammazione%%link%%, cioè il numero di processi che possono essere mantenuti in memoria e pronti per essere eseguiti contemporaneamente.
3. **Schedulazione a medio termine (swapper scheduler)**: è responsabile del cosiddetto _swapping dei processi_, cioè dello spostamento temporaneo di processi in stato `waiting` dalla RAM a una memoria secondaria (per esempio su disco) per liberare memoria e fare spazio ad altri processi.
4. **Schedulazione a breve termine (CPU scheduler)**: è l'unica schedulazione realmente necessaria in un sistema operativo, poiché decide quale processo tra quelli nello stato `ready` dovrà essere eseguito dalla CPU attraverso l'uso di diversi algoritmi di schedulazione%%link%%. Questo processo avviene molto frequentemente (nell'ordine dei millisecondi).

%%
\## Algoritmi di schedulazione

Esistono vari **algoritmi di schedulazione** utilizzati per determinare quale processo deve essere eseguito dalla CPU in un dato momento. I vari algoritmi di schedulazione hanno caratteristiche diverse che li rendono più adatti a determinati scenari (interattivi, in tempo reale, ecc.), e la scelta dell'algoritmo giusto dipende dai requisiti specifici del sistema.

\### 1. **First-Come, First-Served (FCFS)**

- **Descrizione**: I processi vengono eseguiti nell'ordine in cui arrivano. Il primo processo che arriva è il primo a essere eseguito.
- **Vantaggi**: Semplice da implementare.
- **Svantaggi**: Può causare il problema della **convoy effect**, dove i processi più lunghi bloccano l'esecuzione di quelli più brevi, aumentando i tempi di attesa.

\#### 2. **Shortest Job Next (SJN) o Shortest Job First (SJF)**:
- **Descrizione**: Il processo con il tempo di esecuzione più breve viene eseguito per primo.
- **Vantaggi**: Minimizza il tempo di attesa medio.
- **Svantaggi**: Difficile da implementare, poiché è necessario conoscere in anticipo la durata di ogni processo. Può causare **starvation** (processi lunghi potrebbero non essere mai eseguiti).

\#### 3. **Round Robin (RR)**:
- **Descrizione**: Ogni processo viene eseguito per un intervallo di tempo fisso (detto **quantum**), dopodiché la CPU passa al processo successivo in coda. Se un processo non termina nel suo quantum, viene reinserito in coda per essere eseguito più tardi.
- **Vantaggi**: Fornisce equità, poiché ogni processo ha un'opportunità di essere eseguito in modo ciclico.
- **Svantaggi**: Se il quantum è troppo lungo, il comportamento diventa simile a FCFS. Se è troppo breve, si ha un overhead elevato per i frequenti cambi di contesto.

\#### 4. **Priority Scheduling**:
- **Descrizione**: Ad ogni processo viene assegnata una priorità, e la CPU viene assegnata al processo con la priorità più alta. In caso di parità di priorità, si può usare un altro criterio, come l'FCFS.
- **Vantaggi**: Può essere utilizzato per dare la precedenza a processi importanti.
- **Svantaggi**: Può causare **starvation** per i processi con priorità bassa, che potrebbero attendere a lungo prima di essere eseguiti. Il problema può essere risolto con tecniche di **aging**, che aumentano la priorità di un processo man mano che rimane in attesa.

\#### 5. **Multilevel Queue Scheduling**:
- **Descrizione**: I processi vengono suddivisi in più code, ciascuna con una diversa priorità (ad esempio, processi interattivi in una coda e processi batch in un'altra). Ogni coda può avere il proprio algoritmo di schedulazione.
- **Vantaggi**: Permette di gestire diversi tipi di processi in modo efficace.
- **Svantaggi**: La separazione rigida tra code può causare squilibri nel carico della CPU.

\#### 6. **Multilevel Feedback Queue Scheduling**:
- **Descrizione**: Simile al multilevel queue, ma i processi possono "scendere" o "salire" da una coda all'altra in base al loro comportamento (es. se un processo usa troppo la CPU, può essere spostato in una coda a priorità inferiore).
- **Vantaggi**: Più flessibile rispetto al multilevel queue, permette di adattare la schedulazione alle caratteristiche di esecuzione dei processi.
- **Svantaggi**: Può essere complesso da implementare e configurare correttamente.
%%

## 3.4 - Il cambio di contesto

Il **cambio di contesto** (context switch) è l'operazione che il sistema operativo esegue per sospendere l'esecuzione di un processo attualmente in corso e passare l'esecuzione ad un altro processo. Questa operazione è essenziale per implementare il multitasking%%link%%, ovvero la capacità di un sistema di eseguire più processi quasi simultaneamente, facendo in modo che ciascun processo ottenga la CPU a turno.

### 3.4.1 - Utilità e vantaggi del cambio di contesto

Il cambio di contesto serve principalmente per:
1. **Multitasking**: dovendo gestire più processi quasi simultaneamente, la CPU esegue ogni processo per un breve intervallo di tempo e poi passa a un altro processo, servendosi proprio del cambio di contesto e garantendo che ogni processo ottenga una porzione del tempo della CPU utile alla sua esecuzione.
2. **Prevenzione del monopolio della CPU**: in un sistema operativo multitasking, il cambio di contesto permette di sospendere temporaneamente un processo e riprendere l'esecuzione di un altro, assicurando che nessun processo monopolizzi la CPU. Questo permette a più programmi di essere eseguiti nello stesso momento senza che uno blocchi l'altro.
3. **Gestione dei processi bloccati**: quando un processo è bloccato (cioè nello stato `waiting`, per esempio in attesa di un'operazione di I/O), il cambio di contesto consente alla CPU di passare immediatamente a un altro processo pronto per essere eseguito, ottimizzando l'utilizzo delle risorse.
4. **Risposta a eventi esterni**: il cambio di contesto può essere innescato da un interrupt%%link%% (ad esempio, l'arrivo di un input da tastiera o il completamento di un'operazione di I/O) che richiede l'attenzione del sistema operativo. Quando si verifica un evento esterno, la CPU può eseguire il cambio di contesto per gestire l'evento e successivamente tornare al processo precedente.
5. **Supporto alla concorrenza**: nei sistemi multiprocessore%%link%% o multithread%%link%%, il cambio di contesto consente a diversi [thread](#6%20-%20Thread) o processi di essere eseguiti contemporaneamente o in sequenza sulla stessa CPU, migliorando la concorrenza tra le operazioni.
6. **Ottimizzazione del sistema**: permette di bilanciare [processi I/O-bound](Processi%20di%20un%20Sistema%20Operativo.md#4.1%20-%20Processo%20I/O-bound) (che richiedono più operazioni di I/O) e [processi CPU-bound](Processi%20di%20un%20Sistema%20Operativo.md#4.2%20-%20Processo%20CPU-bound) (che utilizzano intensivamente la CPU), migliorando le prestazioni complessive del sistema.

### 3.4.2 - Come funziona il cambio di contesto

Le fasi principali di un cambio di contesto sono:
1. **Salvataggio dello stato del processo corrente**: il sistema operativo salva lo stato corrente del processo (o thread) in esecuzione, inclusi i valori dei registri della CPU, il valore del Program Counter (PC) che tiene traccia dell'istruzione successiva da eseguire, lo [stato di un processo](Processi%20di%20un%20Sistema%20Operativo.md#2.3%20-%20Stato%20di%20un%20processo) e le altre informazioni necessarie per riprendere l'esecuzione in futuro. Queste informazioni sono memorizzate nel [PCB](Processi%20di%20un%20Sistema%20Operativo.md#2%20-%20Il%20PCB%20e%20le%20informazioni%20sul%20processo) del processo.
2. **Caricamento del nuovo contesto**: il sistema operativo carica il contesto del prossimo processo da eseguire dal suo corrispettivo [PCB](Processi%20di%20un%20Sistema%20Operativo.md#2%20-%20Il%20PCB%20e%20le%20informazioni%20sul%20processo), ripristinando i suoi valori dei registri della CPU e del Program Counter, quindi la CPU riprende l'esecuzione del nuovo processo da dove era stato interrotto l'ultima volta.
3. **Ripresa dell'esecuzione**: la CPU riprende l'esecuzione del nuovo processo dal punto in cui era stato sospeso.

Ecco un diagramma che illustra il cambio di contesto tra due processi $P_0$ e $P_1$:

![](Cambio%20di%20contesto.png)

### 3.4.3 - Costi del cambio di contesto

Il cambio di contesto è un'operazione che ha un costo in termini di tempo e risorse. Durante il tempo necessario per il cambio di contesto, nessun processo utente viene effettivamente eseguito: il cambio di contesto è puro overhead, perché il sistema esegue solo operazioni volte alla gestione dei processi e non alla computazione.

Il tempo necessario varia da sistema a sistema, dipendendo dalla velocità della memoria, dal numero di registri da copiare e dall'esistenza di istruzioni macchina appropriate (per esempio, una singola istruzione per caricare o trasferire in memoria tutti i registri). In genere si tratta di qualche millisecondo di computazione, ma la frequenza del cambio di contesto deve essere ottimizzata per evitare che un eccessivo numero di cambi riduca l'efficienza del sistema.

## 3.5 - Parametri di performance della schedulazione

Alcuni criteri utilizzati per valutare le prestazioni di un algoritmo di schedulazione includono:
- **Tempo di attesa**: il tempo che un processo trascorre nella coda dei processi pronti prima di essere eseguito.
- **Tempo di turnaround**: il tempo totale che un processo impiega dal momento in cui viene creato fino a quando termina (inclusi i tempi di attesa e di esecuzione).
- **Tempo di risposta**: il tempo che intercorre tra la creazione di un processo e il primo istante in cui il processo inizia a essere eseguito.
- **Throughput**: il numero di processi completati in un dato intervallo di tempo.

# 4 - Processi I/O-bound e CPU-bound

I concetti di **processi I/O-bound e CPU-bound** si riferiscono al tipo di risorse su cui un processo è più dipendente durante la sua esecuzione. La distinzione tra questi due tipi di processi è fondamentale per l'ottimizzazione delle prestazioni dei sistemi operativi e per la [schedulazione dei processi](Processi%20di%20un%20Sistema%20Operativo.md#3%20-%20Schedulazione%20dei%20processi).

## 4.1 - Processo I/O-bound

Un **processo I/O-bound** è un processo che passa la maggior parte del suo tempo in attesa di operazioni di I/O, come la lettura da o la scrittura su un disco, l'attesa di dati dalla rete, o l'interazione con dispositivi come tastiere e stampanti. Il tempo di esecuzione sulla CPU è relativamente breve rispetto al tempo trascorso in attesa di I/O.

### 4.1.1 - Caratteristiche principali dei processi I/O-bound

Le **caratteristiche principali dei processi I/O-bound** sono:
- **Uso intenso di I/O**: questi processi effettuano molte operazioni di input e output e, quindi, tendono a essere spesso bloccati (quindi nello stato `waiting`) fino a quando le operazioni di I/O non sono completate.
- **Breve tempo di utilizzo della CPU**: quando il processo ottiene il controllo della CPU, tende a eseguire solo un piccolo numero di calcoli prima di essere nuovamente bloccato per attendere l'I/O (ad esempio, un programma che attende frequenti input da parte dell'utente, come un editor di testo o un'applicazione interattiva, oppure un processo che trasferisce grandi quantità di dati da o verso un disco rigido).
- **Obiettivo della schedulazione**: i processi I/O-bound beneficiano di una schedulazione che li rimuova rapidamente dallo stato di attesa (quando l'I/O è completato) e gli assegni prontamente la CPU, per minimizzare i tempi di attesa e garantire che le operazioni di I/O siano gestite efficientemente.

## 4.2 - Processo CPU-bound

Un **processo CPU-bound** è un processo che trascorre la maggior parte del suo tempo effettuando calcoli sulla CPU e richiede relativamente poche operazioni di I/O. Il tempo speso in attesa di operazioni di I/O è trascurabile rispetto al tempo di utilizzo della CPU.

### 4.2.1 - Caratteristiche principali dei processi CPU-bound

Le **caratteristiche principali dei processi CPU-bound** sono:
- **Uso intenso della CPU**: Questi processi richiedono molto tempo di CPU per eseguire i loro calcoli e rimangono in esecuzione per lunghi periodi senza essere bloccati per operazioni di I/O.
- **Basso utilizzo di I/O**: I processi CPU-bound raramente richiedono accesso a dispositivi di input e output, quindi tendono a non essere frequentemente bloccati (es. un programma di elaborazione scientifica o di simulazione che esegue complessi calcoli matematici, oppure un software che genera immagini grafiche complesse o esegue algoritmi di compressione dati).
- **Obiettivo della schedulazione**: i processi CPU-bound possono richiedere quanti di tempo più lunghi, poiché tendono a utilizzare la CPU per periodi prolungati prima di completare il loro lavoro o di cedere la CPU.

## 4.3 - Differenze principali tra i due tipi

Ecco una tabella riassuntiva delle differenze principali tra i due tipi di processi:

| Caratteristica      | **I/O-bound**                                           | **CPU-bound**                                                   |
| ------------------- | ------------------------------------------------------- | --------------------------------------------------------------- |
| **Uso principale**  | Predomina l'attesa per operazioni di I/O.               | Predomina l'uso intensivo della CPU per calcoli.                |
| **Tempo in attesa** | Passa molto tempo in attesa di I/O (stato `waiting`).   | Passa la maggior parte del tempo eseguendo calcoli.             |
| **Tempo sulla CPU** | Utilizza la CPU solo per brevi periodi.                 | Utilizza la CPU per lunghi periodi senza interruzioni.          |
| **Esempi**          | Editor di testo, programmi di rete, trasferimenti dati. | Elaborazione scientifica, rendering grafico, compressione dati. |
| **Schedulazione**   | Richiede una gestione rapida dell'I/O.                  | Richiede tempi più lunghi di utilizzo della CPU.                |

## 4.4 - Importanza per la schedulazione

Il sistema operativo deve tenere conto del tipo di processo (I/O-bound o CPU-bound) durante la schedulazione per ottimizzare le prestazioni del sistema:
- **Processi I/O-bound**: vengono solitamente eseguiti con maggiore priorità o con quanti di tempo più brevi per evitare che rimangano inutilmente in attesa di operazioni I/O completate.
- **Processi CPU-bound**: possono essere eseguiti con quanti di tempo più lunghi per evitare frequenti [cambi di contesto](Processi%20di%20un%20Sistema%20Operativo.md#3.4%20-%20Il%20cambio%20di%20contesto) e overhead associati, poiché tendono a utilizzare la CPU per periodi più estesi.

# 5 - Operazioni sui processi

Le **operazioni sui processi** rappresentano le azioni che un sistema operativo può eseguire per gestire e controllare i processi in esecuzione. Queste operazioni includono la [creazione di un processo](Processi%20di%20un%20Sistema%20Operativo.md#5.1%20-%20Creazione%20di%20un%20processo), la [terminazione di un processo](Processi%20di%20un%20Sistema%20Operativo.md#5.2%20-%20Terminazione%20di%20un%20processo), la [comunicazione tra processi](Processi%20di%20un%20Sistema%20Operativo.md#5.3%20-%20Comunicazione%20tra%20processi) e il coordinamento%%link%% dei processi.

## 5.1 - Creazione di un processo

Ogni nuovo processo viene creato a partire da un processo già esistente: il processo creante viene detto _processo padre_ (_parent process_), mentre il nuovo processo è chiamato _processo figlio_ (_child process_). Il sistema operativo assegna al processo appena creato risorse (come spazio di memoria e tempo CPU) e lo aggiunge alla [job queue](Processi%20di%20un%20Sistema%20Operativo.md#3.2.1%20-%20Principali%20code%20di%20schedulazione).

### 5.1.1 - Fasi principali della creazione di un processo

Le fasi principali della creazione di un processo sono:
1. **Assegnazione di un PID**: ogni processo ha un identificatore univoco (solitamente rappresentato in memoria come un numero intero), noto come _Process ID_ (_PID_). Il PID fornisce un valore univoco per ogni processo del sistema e può essere usato come indice per accedere a vari attributi di un processo all'interno del kernel%%link%%.
2. **Allocazione delle risorse**: vengono allocate le risorse necessarie per il nuovo processo, come lo [spazio di memoria](Processi%20di%20un%20Sistema%20Operativo.md#2.4%20-%20Spazio%20di%20memoria), i descrittori dei file aperti dal processo padre che possono essere ereditati o copiati da lui, il tempo di CPU e così via.
3. **Inizializzazione del contesto**: il sistema operativo crea un [PCB](Processi%20di%20un%20Sistema%20Operativo.md#2%20-%20Il%20PCB%20e%20le%20informazioni%20sul%20processo) per il processo figlio contenente tutte le informazioni di controllo necessarie, come lo stato del processo, i registri, i puntatori alla memoria, i file aperti e altro.
4. **Inserimento nelle code di schedulazione**: il processo viene aggiunto alla [job queue](Processi%20di%20un%20Sistema%20Operativo.md#3.2.1%20-%20Principali%20code%20di%20schedulazione), cioè alla coda di schedulazione contenente tutti i processi nel sistema.

%%https://it.wikipedia.org/wiki/Init
fare una sottosezione%%

### 5.1.2 - `fork()` in Unix/Linux

Nei sistemi Unix/Linux, la creazione di un nuovo processo avviene tramite la chiamata di sistema `fork()`. Questa chiamata crea una copia esatta del processo padre, ma con un nuovo PID. Il valore restituito dalla chiamata `fork()` è diverso per il padre e per il figlio: mentre il processo padre riceve il PID del processo figlio, il processo figlio riceve un valore pari a `0`, indicando che è il processo appena creato.

Un esempio di codice in linguaggio C che utilizza `fork()`:

```c
#include <stdio.h>
#include <unistd.h>

int main() {

	// Creazione di un nuovo processo figlio
    pid_t pid = fork();

    if (pid == 0) {
        // Codice eseguito dal processo figlio
        printf("Sono il processo figlio. PID: %d\n", getpid());
        
        // Array di argomenti per exec()
        char *args[] = { "ls", "-l", NULL };

        // Esecuzione di exec() utilizzando il percorso assoluto
        if (exec("/bin/ls", args) == -1) {
            // Se exec restituisce, c'è stato un errore
            perror("exec failed");
            exit(EXIT_FAILURE);
        }
    } else if (pid > 0) {
        // Codice eseguito dal processo padre
        printf("Sono il processo padre. PID del figlio: %d\n", pid);
        wait(NULL);
        printf("Processo figlio completato.\n");
    } else {
        // Errore durante la creazione del processo
        printf("Errore nella creazione del processo\n");
        exit(EXIT_FAILURE);
    }
    return 0;
}

```

Il processo figlio può poi sovrascrivere il suo spazio di memoria e l'eseguibile, entrambi ereditati dal padre, con una nuova immagine di processo tramite una chiamata come `exec()`, che permette di eseguire un programma differente all'interno del processo figlio.

### 5.1.3 - `CreateProcess()` in Windows

Nei sistemi operativi Windows, un nuovo processo viene creato tramite l'API%%link%% `CreateProcess()`. Questa funzione crea un nuovo processo e contemporaneamente un [thread](Processi%20di%20un%20Sistema%20Operativo.md#6%20-%20Thread) principale all'interno del processo.

A differenza di [`fork()`](Processi%20di%20un%20Sistema%20Operativo.md#5.1.2%20-%20`fork()`%20in%20Unix/Linux) che duplica il processo corrente, `CreateProcess()` consente di specificare il nome dell'eseguibile che il processo figlio deve eseguire. Questo significa che, in Windows, il processo figlio inizia immediatamente con l'esecuzione di un programma distinto.

Un esempio di codice in linguaggio C che utilizza `CreateProcess()`:

```c
#include <windows.h>
#include <stdio.h>

int main() {
   STARTUPINFO si;
   PROCESS_INFORMATION pi;

   // Zero-fill the structures
   ZeroMemory(&si, sizeof(si));
   si.cb = sizeof(si);
   ZeroMemory(&pi, sizeof(pi));

   // Create a new process
   if (CreateProcess(NULL,           // No module name (use command line)
					 "C:\\Program.exe", // Command line
					 NULL,           // Process handle not inheritable
					 NULL,           // Thread handle not inheritable
					 FALSE,          // Set handle inheritance to FALSE
					 0,              // No creation flags
					 NULL,           // Use parent's environment block
					 NULL,           // Use parent's starting directory
					 &si,            // Pointer to STARTUPINFO structure
					 &pi)            // Pointer to PROCESS_INFORMATION structure
   ) {
	   printf("Processo creato con successo!\n");
	   printf("PID del processo figlio: %d\n", pi.dwProcessId);

	   // Wait until child process exits
	   WaitForSingleObject(pi.hProcess, INFINITE);

	   // Close process and thread handles
	   CloseHandle(pi.hProcess);
	   CloseHandle(pi.hThread);
   } else {
	   printf("Errore nella creazione del processo.\n");
   }
   return 0;
}
```

## 5.2 - Terminazione di un processo

Un processo può terminare per vari motivi. Quando termina, le risorse assegnate al processo (come la memoria, i file aperti e il tempo CPU) vengono liberate dal sistema operativo. La terminazione di un processo può essere volontaria o forzata:
- **Terminazione volontaria**: il processo completa l'esecuzione del suo codice (ad esempio, l'utente chiude un programma). Ogni processo può chiamare esplicitamente la funzione di terminazione, usando come `exit()` in Unix/Linux o `ExitProcess()` in Windows.
- **Terminazione forzata**: un errore o un'eccezione non gestita (come una divisione per zero o un accesso in memoria non valido) può causare la terminazione forzata del processo. Il sistema operativo o un altro processo può terminare forzatamente un processo tramite chiamate di sistema (ad esempio, tramite `kill()` in UNIX o `TerminateProcess()` in Windows). Generalmente solo il processo padre del processo che si vuole terminare può invocare una chiamata di sistema di questo tipo, altrimenti gli utenti potrebbero causare arbitrariamente la terminazione forzata di processi di chiunque.

### 5.2.1 - Fasi principali della terminazione di un processo

Le fasi principali della terminazione di un processo sono:
1. **Richiesta di terminazione**: il processo chiama una funzione di uscita o riceve un segnale di terminazione. Questo avvia il processo di chiusura.
2. **Chiusura e liberazione delle risorse**: il sistema operativo chiude automaticamente tutti i file aperti dal processo. Anche altri tipi di risorse come [socket](Processi%20di%20un%20Sistema%20Operativo.md#5.3.4%20-%20Socket), canali di comunicazione%%link%%, semafori%%link%% o altre strutture di dati vengono rilasciate, così come lo [spazio di memoria](Processi%20di%20un%20Sistema%20Operativo.md#2.4%20-%20Spazio%20di%20memoria) assegnato al processo (sia quella per il codice che per i dati) viene liberato, in modo che possa essere utilizzato da altri processi.
3. **Aggiornamento dello stato del processo**: lo [stato del processo](Processi%20di%20un%20Sistema%20Operativo.md#2.3%20-%20Stato%20di%20un%20processo) nel [PCB](Processi%20di%20un%20Sistema%20Operativo.md#2%20-%20Il%20PCB%20e%20le%20informazioni%20sul%20processo) viene aggiornato in `terminated`. Finché il processo padre non recupera lo stato del processo figlio, si dice che quest'ultimo diventa un _processo zombie_ (in quanto il padre non sa che il processo figlio è morto).
4. **Liberazione del PCB dalle code di schedulazione**: il processo viene rimosso dalla coda dei processi pronti (la [ready queue](Processi%20di%20un%20Sistema%20Operativo.md#3.2.1%20-%20Principali%20code%20di%20schedulazione)) o da altre [code di schedulazione](Processi%20di%20un%20Sistema%20Operativo.md#3.2%20-%20Code%20di%20schedulazione). Il [PCB](Processi%20di%20un%20Sistema%20Operativo.md#2%20-%20Il%20PCB%20e%20le%20informazioni%20sul%20processo) del processo viene marcato per la rimozione o, nel caso di un processo zombie, viene mantenuto in memoria fino a che il processo padre recupera il suo stato.
5. **Notifica del processo padre**: se il processo è stato generato da un processo padre, quest'ultimo viene notificato della terminazione del figlio. Nei sistemi Unix/Linux, il padre può chiamare la funzione `wait()` per raccogliere il codice di uscita del figlio e permettere la completa rimozione del [PCB](Processi%20di%20un%20Sistema%20Operativo.md#2%20-%20Il%20PCB%20e%20le%20informazioni%20sul%20processo) del figlio dalla memoria.
6. **Rimozione del processo dal sistema operativo**: una volta che tutte le risorse sono state rilasciate e, se necessario, il processo padre ha recuperato il codice di uscita del figlio, il sistema operativo rimuove il [PCB](Processi%20di%20un%20Sistema%20Operativo.md#2%20-%20Il%20PCB%20e%20le%20informazioni%20sul%20processo) e altre strutture associate al processo dalla memoria. A questo punto, il processo è completamente terminato.

### 5.2.2 - Codice di uscita

Quando un processo termina, spesso restituisce un **codice di uscita** al sistema operativo o al processo padre. Questo codice è un valore numerico che indica se il processo è terminato correttamente o se si è verificato un errore. I valori solitamente usati sono:
- `0`: indica che il processo è terminato con successo.
- **Un numero diverso dallo `0`**: indica un errore o una condizione specifica che ha causato la terminazione del processo.

### 5.2.3 - Terminazione a cascata

La **terminazione a cascata** è un meccanismo che si verifica in un sistema operativo quando un processo termina e i suoi processi figli vengono automaticamente terminati insieme ad esso. Questo comportamento è spesso associato ai processi di tipo _daemon_%%link%% o ai servizi che, quando vengono interrotti, devono anche interrompere i processi che hanno creato.

#### 5.2.3.1 - Funzionamento della terminazione a cascata

Quando un processo padre termina, i processi figli possono essere influenzati in diversi modi a seconda della loro relazione con il processo padre e della gestione dei segnali. Alcuni punti chiave della terminazione a cascata sono:
- **Segnale di terminazione**: quando un processo padre termina, può inviare segnali ai suoi processi figli. Se i processi figli non sono in grado di gestire il segnale di terminazione (come `SIGTERM` o `SIGKILL`), verranno terminati dal sistema operativo.
- **Processi orfani**: se un processo padre termina, i suoi processi figli diventano _orfani_. In UNIX e Linux, i processi orfani vengono adottati dal processo `init` (che ha [PID](Processi%20di%20un%20Sistema%20Operativo.md#2.1%20-%20Informazioni%20contenute%20in%20un%20PCB) con valore `1`), che si occupa di gestire la loro terminazione. I processi orfani non vengono necessariamente terminati a meno che non vengano esplicitamente chiesti di farlo.
- **Comportamento di `wait()`**: quando un processo padre utilizza la funzione `wait()`, attende la terminazione di uno dei suoi processi figli. Se il padre termina prima dei figli, il sistema operativo può terminare i figli se la relazione di dipendenza è tale che non ha senso che continuino a vivere.

#### 5.2.3.2 - Esempio di terminazione a cascata in linguaggio C

Ecco un esempio in linguaggio C%%link%%, in cui un processo padre crea un processo figlio e poi termina. Se il processo padre termina, il comportamento dei processi figli può essere osservato.

```c
#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <sys/wait.h>

int main() {
    pid_t pid = fork();

    if (pid < 0) {
        perror("fork failed");
        exit(EXIT_FAILURE);
    } else if (pid == 0) {
        // Questo è il processo figlio
        while (1) {
            printf("Processo figlio in esecuzione (PID: %d).\n", getpid());
            sleep(1);
        }
    } else {
        // Questo è il processo padre
        printf("Processo padre (PID: %d) in attesa di 5 secondi prima di terminare.\n", getpid());
        sleep(5);
        printf("Processo padre sta per terminare.\n");
        exit(0); // Termina il processo padre
    }

    return 0;
}
```

Durante l'esecuzione di questo programma, si può notare che il processo figlio continua a stampare i messaggi anche dopo la terminazione del processo padre, poiché diventa un processo orfano e viene adottato da `init`. Se invece il processo padre inviasse un segnale di terminazione, come `SIGKILL` o `SIGTERM`, anche il processo figlio verrebbe terminato, mostrando un comportamento di terminazione a cascata.

## 5.3 - Comunicazione tra processi

Spesso, i processi hanno bisogno di comunicare e collaborare tra di loro scambiandosi dati. La **comunicazione tra processi** (Inter-Process Communication, IPC) riguarda le tecniche e i meccanismi attraverso cui i processi di un sistema operativo, che possono essere eseguiti in parallelo o separatamente, scambiano informazioni tra loro. Ogni metodo di comunicazione tra processi ha vantaggi e svantaggi, ed è scelto in base alle esigenze specifiche di sincronizzazione, latenza, throughput e complessità dell'applicazione.

Le principali tecniche di comunicazione tra processi sono:%% SISTEMARE LISTA CON TUTTE LE TECNICHE %%
- **Pipe**: è un canale di comunicazione unidirezionale tra due processi. Un processo scrive dati in un'estremità della pipe, mentre l'altro processo legge dall'altra estremità.
- **Code di messaggi**: I processi inviano e ricevono messaggi tra di loro tramite **code di messaggi** (message queues).
- **Memoria condivisa**: Due o più processi possono condividere una porzione di memoria, il che permette lo scambio rapido di informazioni.
- **Socket**: Permettono la comunicazione tra processi su macchine diverse tramite protocolli di rete.
- Chiamate di procedura remota (RPC)

### 5.3.1 - Pipe

Le **pipe** %%([pronuncia]: `/paɪp/`)%%sono un meccanismo di comunicazione tra processi che permette a uno o più processi di condividere dati tramite un canale unidirezionale. In sostanza, una pipe crea un collegamento tra due processi: uno scrive dati nella pipe e l'altro legge quei dati.

#### 5.3.1.1 - Caratteristiche principali delle pipe

Le caratteristiche principali delle pipe sono:
- **Unidirezionali**: i dati fluiscono in una sola direzione (dal processo scrivente a quello leggente).
- **Anonime**: sono tipicamente usate tra processi che hanno una relazione gerarchica (padre-figlio). In genere, il processo padre crea una pipe e poi genera il processo figlio che la usa.
- **Comunicazione in memoria**: la pipe si comporta come un buffer circolare tra i due processi, memorizzando temporaneamente i dati fino a quando non vengono letti.

#### 5.3.1.2 - Funzionamento di base delle pipe

Una pipe in UNIX o Linux può essere creata con la chiamata di sistema%%link%% `pipe()`. Questa funzione genera due file descriptor:
- Il file descriptor per la lettura (`fd[0]`);
- Il file descriptor per la scrittura (`fd[1]`).

Un processo può scrivere dati nel file descriptor `fd[1]` e un altro processo può leggerli dal file descriptor `fd[0]`.

%%mettere link ai file descriptor%%

##### 5.3.1.2.1 - Esempio di codice in linguaggio C

Ecco un esempio di uso delle pipe in linguaggio C%%link%%, in cui un processo padre invia un messaggio al processo figlio usando una pipe.

```c
#include <stdio.h>
#include <unistd.h>
#include <string.h>

int main() {
    int fd[2]; // fd[0] per lettura, fd[1] per scrittura
    pid_t pid;
    char buffer[100];
    
    // Creazione della pipe
    if (pipe(fd) == -1) {
        perror("pipe");
        return 1;
    }

    // Creazione del processo figlio
    pid = fork();

    if (pid < 0) {
        perror("fork");
        return 1;
    }

    if (pid > 0) {
        // Processo padre
        close(fd[0]); // Chiudiamo l'estremità di lettura nel padre

        // Scriviamo un messaggio nella pipe
        char msg[] = "Ciao dal processo padre!";
        write(fd[1], msg, strlen(msg) + 1);

        close(fd[1]); // Chiudiamo l'estremità di scrittura dopo aver scritto
    } else {
        // Processo figlio
        close(fd[1]); // Chiudiamo l'estremità di scrittura nel figlio

        // Leggiamo il messaggio dalla pipe
        read(fd[0], buffer, sizeof(buffer));
        printf("Messaggio ricevuto dal figlio: %s\n", buffer);

        close(fd[0]); // Chiudiamo l'estremità di lettura dopo aver letto
    }

    return 0;
}
```

Spiegazione del codice:
- `pipe(fd)` crea una pipe. `fd[0]` è usato per la lettura e `fd[1]` per la scrittura.
- `fork()` crea un nuovo processo figlio.
	- Nel processo padre, chiudiamo l'estremità di lettura (`fd[0]`) e scriviamo il messaggio nella pipe tramite `write()`.
	- Nel processo figlio, chiudiamo l'estremità di scrittura (`fd[1]`) e leggiamo il messaggio tramite `read()`.
- Dopo la comunicazione, ogni processo chiude l'estremità della pipe che non è più necessaria.
%%nel codice e nella sua spiegazione scrivere tutto in modo impersonale, non in prima persona plurale%%

#### 5.3.1.3 - Vantaggi e svantaggi delle pipe

I principali vantaggi delle pipe sono:
- **Semplicità**: le pipe sono facili da usare e implementare, soprattutto per la comunicazione tra processi con una relazione gerarchica (ad esempio, un processo padre e un processo figlio). Sono supportate direttamente a livello del sistema operativo, con chiamate di sistema semplici come `pipe()` per creare una pipe e `read()`/`write()` per leggere e scrivere dati.
- **Comunicazione unidirezionale**: le pipe forniscono un canale di comunicazione unidirezionale, utile in situazioni in cui i dati devono fluire solo in una direzione (da un processo produttore a un processo consumatore).
- **Buffering automatico**: le pipe utilizzano un buffer interno gestito dal sistema operativo, che rende la gestione dei dati tra i processi più semplice, senza necessità di gestire manualmente il buffering dei dati.
- **Sincronizzazione implicita**: le pipe assicurano una forma di sincronizzazione implicita, in quanto se un processo tenta di leggere da una pipe vuota, verrà bloccato fino a quando non ci saranno dati disponibili. Allo stesso modo, se la pipe è piena, il processo che scrive attenderà fino a quando c'è spazio libero.
- **Indipendenza dalla rete**: le pipe funzionano a livello locale tra processi sullo stesso sistema, senza necessità di connessioni di rete, il che le rende efficienti in termini di prestazioni per la comunicazione tra processi locali.

I principali svantaggi delle pipe sono:
- **Unidirezionalità**: i dati nelle pipe possono fluire in una sola direzione. Se è necessaria la comunicazione bidirezionale (andata e ritorno), bisogna creare due pipe, aumentando la complessità della gestione dei dati.
- **Uso limitato tra processi correlati**: le pipe, dette anche _pipe anonime_ o _pipe convenzionali_, funzionano solo tra processi che hanno una relazione gerarchica (ad esempio, un processo padre che comunica con il figlio). Per comunicare tra processi non correlati, è necessario usare le [named pipe](Processi%20di%20un%20Sistema%20Operativo.md#5.3.1.4%20-%20Named%20pipe), che sono più complesse da gestire rispetto alle pipe anonime.
- **Capacità limitata**: le pipe hanno una capacità limitata (tipicamente qualche kilobyte%%link%%). Se il buffer si riempie, il processo scrivente viene bloccato finché il buffer non viene svuotato. Allo stesso modo, se non ci sono dati, il processo leggente viene bloccato.
- **Accesso sequenziale**: le pipe operano in modo sequenziale secondo la politica FIFO (First In, First Out). Questo è ideale per flussi semplici di dati, ma in scenari complessi, in cui è richiesta una gestione avanzata dei messaggi, le pipe possono risultare limitate.
- **No persistenza dei dati**: i dati nelle pipe sono transienti, cioè una volta che i dati vengono letti, vengono rimossi dalla pipe. Se un processo legge i dati ma non li elabora correttamente, non è possibile rileggere il messaggio. Inoltre, se un processo termina senza leggere i dati, questi vengono persi.
- **Sincronizzazione manuale nei processi complessi**: sebbene ci sia sincronizzazione implicita, in scenari complessi potrebbe essere necessario gestire manualmente la sincronizzazione tra processi per evitare race condition%%link%% o blocchi inutili.
- **Non adatte per grandi quantità di dati**: le pipe sono ideali per il passaggio di piccoli blocchi di dati. Quando è necessario trasferire grandi quantità di dati o file complessi, l'uso delle pipe diventa inefficiente rispetto ad altri metodi di comunicazione tra processi come la [memoria condivisa](Processi%20di%20un%20Sistema%20Operativo.md#5.3.3%20-%20Memoria%20condivisa).

#### 5.3.1.4 - Named pipe

Le **named pipe** (anche chiamate _FIFO_ per il loro comportamento) sono una versione più avanzata delle pipe anonime o pipe convenzionali, cioè le comuni pipe: a differenza di quest'ultime, infatti, le named pipe possono essere utilizzate anche tra processi non legati da una relazione padre-figlio e sono bidirezionali. Vengono create con il comando `mkfifo` o la chiamata di sistema `mkfifo()`.

Ecco un esempio in bash di named pipe:

```bash
mkfifo mypipe
```

Dopo aver creato una named pipe, due processi distinti possono usarla per scambiarsi dati:
- Un processo può scrivere nella pipe con `echo "Hello" > mypipe`;
- Un altro processo può leggere da essa con `cat < mypipe`.

%% approfondire le named pipe (magari con un esempio fatto meglio) %%

%%
\#### Pipe nella shell

Esempi: `pipe()` in UNIX/Linux, pipe nei comandi shell (`|`).
%%

### 5.3.2 - Code di messaggi

Le **code di messaggi** (message queues) sono un meccanismo di comunicazione tra processi che permette a più processi di inviare e ricevere messaggi in maniera asincrona: un processo può inserire un messaggio in una coda, e un altro processo (o più processi) può leggerlo in un momento successivo, senza che i processi debbano sincronizzarsi perfettamente.

#### 5.3.2.1 - Caratteristiche principali delle code di messaggi

Le caratteristiche principali delle code di messaggi sono:
- **Asincronia**: un processo può inviare un messaggio senza aspettare che l'altro processo lo legga immediatamente.
- **Ordinamento**: i messaggi sono normalmente gestiti secondo la politica FIFO (First In, First Out), cioè il primo messaggio inserito è il primo a essere letto.
- **Identificatori**: i messaggi possono avere identificatori o tipi per permettere ai processi di filtrare quelli di interesse.
- **Persistenza temporanea**: i messaggi rimangono nella coda fino a quando non vengono letti o cancellati.

#### 5.3.2.2 - Funzionamento delle code di messaggi

In un sistema operativo come UNIX o Linux, le code di messaggi sono implementate usando una serie di chiamate di sistema%%link%%:
- `msgget()`: crea o accede a una coda di messaggi esistente.
- `msgsnd()`: invia un messaggio a una coda.
- `msgrcv()`: riceve un messaggio da una coda.
- `msgctl()`: esegue operazioni di controllo sulla coda, come eliminarla.

##### 5.3.2.2.1 - Esempio di codice in linguaggio C

Ecco un esempio di uso delle code di messaggi in linguaggio C%%link%%, in cui un processo invia un messaggio a una coda e un altro lo legge.

Ecco il codice per scrivere in una coda:

```c
#include <stdio.h>
#include <sys/ipc.h>
#include <sys/msg.h>
#include <string.h>

// Definizione della struttura del messaggio
struct msg_buffer {
    long msg_type;
    char msg_text[100];
} message;

int main() {

    // Generazione di una chiave univoca
    key_t key = ftok("progfile", 65);

    // Creazione di una coda di messaggi e ottenimento del suo ID
    int msgid = msgget(key, 0666 | IPC_CREAT);

    message.msg_type = 1;

    printf("Inserisci un messaggio: ");
    fgets(message.msg_text, sizeof(message.msg_text), stdin);

    // Invio del messaggio nella coda
    msgsnd(msgid, &message, sizeof(message), 0);

    printf("Messaggio inviato: %s\n", message.msg_text);

    return 0;
}
```

Ecco il codice per leggere dalla coda:

```c
#include <stdio.h>
#include <sys/ipc.h>
#include <sys/msg.h>

// Definizione della struttura del messaggio
struct msg_buffer {
    long msg_type;
    char msg_text[100];
} message;

int main() {

    // Generazione di una chiave univoca
    key_t key = ftok("progfile", 65);

    // Accesso alla coda di messaggi esistente
    int msgid = msgget(key, 0666 | IPC_CREAT);

    // Ricezione del messaggio dalla coda
    msgrcv(msgid, &message, sizeof(message), 1, 0);

    // Stampa del messaggio ricevuto
    printf("Messaggio ricevuto: %s\n", message.msg_text);

    // Rimozione della coda di messaggi
    msgctl(msgid, IPC_RMID, NULL);

    return 0;
}
```

Spiegazione del codice:
- `key_t key = ftok("progfile", 65);`: genera una chiave univoca, utilizzata per identificare la coda di messaggi.
- `msgget()`: crea (o accede, se esiste già) a una coda di messaggi associata a quella chiave.
- `msgsnd()`: invia un messaggio a quella coda. Il messaggio è contenuto nella struttura `msg_buffer`, dove `msg_type` indica il tipo di messaggio e `msg_text` contiene il testo.
- `msgrcv()`: riceve un messaggio dalla coda. È possibile specificare un tipo di messaggio (`msg_type`) per filtrare i messaggi da leggere.
- `msgctl()`: rimuove la coda di messaggi quando non è più necessaria.

#### 5.3.2.3 - Vantaggi e svantaggi delle code di messaggi

I principali vantaggi delle code di messaggi sono:
- **Comunicazione asincrona**: i processi non devono essere eseguiti contemporaneamente per scambiarsi dati. Un processo può inviare un messaggio e terminare, mentre il destinatario può ricevere il messaggio in un secondo momento.
- **Decoupling tra processi**: i processi non devono essere direttamente collegati o conoscere l'identità l'uno dell'altro. Questo rende i sistemi più flessibili e modulari, poiché è possibile aggiungere o rimuovere processi senza influenzare gli altri.
- **Ordine dei messaggi**: i messaggi vengono normalmente gestiti secondo la politica FIFO (First In, First Out). Questo garantisce che i messaggi vengano elaborati nell'ordine in cui sono stati inviati, il che è utile per mantenere la coerenza temporale.
- **Supporto per messaggi di diversi tipi e filtri**: è possibile associare a ciascun messaggio un "tipo" o identificatore. Questo permette ai processi di filtrare e leggere solo i messaggi di un certo tipo, migliorando la flessibilità nella gestione di diverse categorie di messaggi.
- **Persistenza temporanea dei messaggi**: i messaggi rimangono nella coda fino a quando non vengono letti, rendendo possibile la comunicazione anche se i processi sono avviati o terminano in momenti diversi.
- **Semplicità di implementazione**: le code di messaggi offrono un'interfaccia relativamente semplice per inviare e ricevere dati rispetto ad altre tecniche di comunicazione tra processi più complesse come [socket](Processi%20di%20un%20Sistema%20Operativo.md#5.3.4%20-%20Socket) o [memoria condivisa](Processi%20di%20un%20Sistema%20Operativo.md#5.3.3%20-%20Memoria%20condivisa).

I principali svantaggi delle code di messaggi sono:
- **Dimensione limitata della coda**: le code di messaggi hanno una dimensione massima limitata. Se la coda si riempie e non viene letta in tempo, i nuovi messaggi non possono essere inviati, causando un blocco o un ritardo nei processi di invio.
- **Performance**: le operazioni sulle code di messaggi possono introdurre overhead, poiché ogni operazione di invio e ricezione richiede il passaggio attraverso il kernel del sistema operativo. Questo rende le code di messaggi meno efficienti rispetto a metodi come la [memoria condivisa](Processi%20di%20un%20Sistema%20Operativo.md#5.3.3%20-%20Memoria%20condivisa), che permette accesso diretto ai dati.
- **Possibile perdita di messaggi**: se la coda viene eliminata o se un processo termina bruscamente senza leggere i messaggi, questi possono essere persi, a meno che non venga implementato un meccanismo di persistenza.
- **Sincronizzazione non garantita**: anche se la comunicazione è asincrona, i processi che devono essere strettamente sincronizzati richiederanno meccanismi aggiuntivi (es. semafori%%link%%) per evitare condizioni di gara (race conditions%%link%%) o accessi concorrenti ai messaggi.
- **Meno adatte per grandi quantità di dati**: le code di messaggi sono più adatte per scambiare piccoli messaggi, piuttosto che grandi blocchi di dati. Per grandi quantità di dati, la [memoria condivisa](Processi%20di%20un%20Sistema%20Operativo.md#5.3.3%20-%20Memoria%20condivisa) è più efficiente.
- **Gestione complessa di timeout**: la gestione dei timeout (attesa di un messaggio per un certo tempo prima di rinunciare) può richiedere logica aggiuntiva, rendendo la programmazione più complessa in scenari che necessitano di risposte rapide o certe.

### 5.3.3 - Memoria condivisa

La **memoria condivisa** (shared memory) è un meccanismo di comunicazione tra processi che consente a più processi di accedere alla stessa area di memoria. Questo metodo è molto veloce poiché non richiede copie di dati tra processi, ma i processi devono coordinarsi per evitare conflitti di accesso.

#### 5.3.3.1 - Caratteristiche principali della memoria condivisa

Le caratteristiche principali della memoria condivisa sono:
- **Accesso diretto ai dati**: la memoria condivisa consente a più processi di accedere allo stesso segmento di memoria fisica senza necessità di trasferire dati tra processi. Questo avviene mappando lo stesso spazio di memoria nello spazio di indirizzi virtuale di ciascun processo.
- **Elevata velocità di comunicazione**: poiché i dati non devono essere copiati o trasferiti, l'accesso alla memoria condivisa è estremamente rapido rispetto ad altri metodi di comunicazione tra processi, come le [code di messaggi](Processi%20di%20un%20Sistema%20Operativo.md#5.3.2%20-%20Code%20di%20messaggi) o i [socket](Processi%20di%20un%20Sistema%20Operativo.md#5.3.4%20-%20Socket).
- **Dipendenza dalla sincronizzazione**: la memoria condivisa non fornisce un meccanismo di sincronizzazione integrato. I processi devono gestire autonomamente l'accesso alla memoria per evitare condizioni di gara%%link%% e inconsistenze. Si utilizzano spesso semafori%%link%% o mutex%%link%% per garantire l'accesso ordinato.
- **Persistenza temporanea dei dati**: il segmento di memoria condivisa esiste fino a quando almeno un processo è collegato ad esso. Una volta che tutti i processi si scollegano, la memoria può essere rilasciata dal sistema operativo, oppure può essere rimossa esplicitamente con una chiamata di sistema%%link per "chiamata di sistema"%% come `shmctl()`.
- **Efficienza per grandi volumi di dati**: è particolarmente vantaggiosa per gestire dati di grandi dimensioni, poiché non richiede la duplicazione dei dati in ciascun processo che deve accedervi. Tutti i processi accedono alla stessa copia dei dati, riducendo l'uso di memoria e migliorando l'efficienza.
- **Accesso locale**: la memoria condivisa funziona meglio per la comunicazione tra processi sullo stesso sistema. Per la comunicazione tra processi su sistemi diversi, occorre usare un altro meccanismo come i socket%%link%%.
- **Utilizzo di chiavi IPC**: nei sistemi UNIX/Linux%%link%%, ogni segmento di memoria condivisa è identificato da una chiave (usata con `shmget()`), permettendo ai processi di connettersi alla stessa area. Questo ID deve essere noto ai processi per poter accedere alla memoria. %%rendere più chiaro questo punto%%

La memoria condivisa funziona consentendo a più processi di accedere alla stessa area di memoria fisica. Di seguito sono illustrati i principali passaggi e concetti necessari per il funzionamento di una memoria condivisa in un sistema operativo come UNIX/Linux.

#### 5.3.3.2 - Funzionamento della memoria condivisa

In un sistema operativo come UNIX o Linux, la memoria condivisa viene implementata usando una serie di chiamate di sistema%%link%%:
1. **Creazione dell'area di memoria**: un processo crea un'area di memoria condivisa con una chiamata di sistema%%link%% come `shmget()`. Questa funzione assegna un segmento di memoria e restituisce un ID per accedere alla memoria.
2. **Mappatura nello spazio di indirizzi**: una volta creata, l'area di memoria deve essere _mappata_, cioè collegata, allo spazio di indirizzi virtuale del processo, utilizzando `shmat()`. Questo permette al processo di accedere alla memoria come se fosse una variabile o un array ordinario.
3. **Accesso alla memoria**: dopo la mappatura, il processo può leggere e scrivere nella memoria condivisa. I dati scritti sono immediatamente visibili agli altri processi che accedono alla stessa area, a condizione che anch'essi abbiano mappato il segmento con `shmat()`.
4. **Sincronizzazione**: poiché più processi possono accedere contemporaneamente alla memoria, è necessario usare semafori%%link%%, mutex%%link%% o altri meccanismi di sincronizzazione. Questi impediscono che i processi modifichino la stessa area di memoria nello stesso momento, evitando condizioni di stallo o errori di dati incoerenti.
5. **Scollegamento dalla memoria**: quando un processo ha terminato l'uso della memoria condivisa, la "scollega" usando `shmdt()`. Tuttavia, la memoria non viene liberata fino a quando tutti i processi che vi sono connessi non si sono scollegati.
6. **Rimozione dell'area di memoria**: dopo lo scollegamento, il segmento di memoria condivisa può essere rimosso definitivamente con `shmctl()`, che libera la memoria.

##### 5.3.3.2.1 - Esempio di codice in linguaggio C

Ecco un esempio di uso della memoria condivisa in linguaggio C%%link%% che illustra come due processi possano utilizzare la memoria condivisa per scambiarsi informazioni.

```c
#include <stdio.h>
#include <stdlib.h>
#include <sys/ipc.h>
#include <sys/shm.h>
#include <sys/types.h>

int main() {
    // Chiave IPC e dimensione della memoria
    key_t key = ftok("shmfile", 65); // Genera una chiave unica
    int shmid = shmget(key, 1024, 0666|IPC_CREAT); // Crea memoria condivisa

    // Mappa la memoria nello spazio di indirizzi
    char *data = (char*) shmat(shmid, (void*)0, 0);

    // Scrive nella memoria condivisa
    printf("Scrivo 'Hello World' nella memoria condivisa\n");
    sprintf(data, "Hello World");

    // Stacca la memoria
    shmdt(data);

    return 0;
}
```

Un secondo programma potrebbe collegarsi alla stessa area di memoria con lo stesso `key_t` e leggere il messaggio.

#### 5.3.3.3 - Vantaggi e svantaggi della memoria condivisa

I principali vantaggi della memoria condivisa sono:
- **Elevata velocità di comunicazione**: l'accesso diretto alla stessa area di memoria elimina la necessità di copiare dati tra processi, garantendo una comunicazione molto rapida. Questo è particolarmente utile in applicazioni ad alte prestazioni, come la grafica, il calcolo scientifico, o i sistemi di trading.
- **Efficienza per grandi quantità di dati**: la memoria condivisa è ideale per scambiare grandi volumi di dati tra processi, poiché riduce il consumo di memoria rispetto alla duplicazione dei dati. Tutti i processi accedono allo stesso blocco di dati, quindi è molto efficiente in termini di utilizzo della memoria.
- **Flessibilità nel formato dei dati**: a differenza di altri metodi di comunicazione tra processi (come le [code di messaggi](Processi%20di%20un%20Sistema%20Operativo.md#5.3.2%20-%20Code%20di%20messaggi)), la memoria condivisa non impone un formato specifico dei dati, permettendo una grande flessibilità nella struttura dei dati da condividere.
- **Accesso simultaneo ai dati**: più processi possono accedere ai dati contemporaneamente, cosa che può ridurre il tempo di latenza in applicazioni real-time. Ciò è utile per operazioni di lettura parallela di dati comuni o aggiornamenti a bassa frequenza.

I principali svantaggi della memoria condivisa sono:
- **Necessità di sincronizzazione esplicita**: la memoria condivisa non include un meccanismo di sincronizzazione integrato. I processi devono coordinarsi manualmente per evitare condizioni di gara%%link%% o accessi incoerenti. Questo può complicare lo sviluppo e richiede l'uso di semafori%%link%% o mutex%%link%% per coordinare gli accessi.
- **Problemi di sicurezza e isolamento**: dal momento che la memoria condivisa è accessibile a più processi, un errore in uno di essi può influire su tutti gli altri. Il controllo degli accessi deve essere gestito correttamente per prevenire modifiche accidentali o non autorizzate, specialmente nei sistemi multiutente.
- **Debug complesso**: il debug della memoria condivisa è più complicato rispetto ad altri metodi di comunicazione tra processi, poiché le condizioni di gara%%link%% e i problemi di sincronizzazione possono essere difficili da rilevare. Gli errori di accesso concorrente possono portare a comportamenti non deterministici difficili da riprodurre.
- **Dipendenza dal sistema operativo**: l'implementazione della memoria condivisa varia tra sistemi operativi, quindi il codice potrebbe non essere portabile. Nei sistemi UNIX-like%%link%%, l'API POSIX%%link%% standardizza alcune chiamate di memoria condivisa, ma Windows%%link%% utilizza un set di API diverso (ad esempio `CreateFileMapping` e `MapViewOfFile`), creando complicazioni di portabilità.
- **Rimozione manuale della memoria**: la memoria condivisa non viene automaticamente rimossa se un processo termina senza scollegarla correttamente. Questo può portare a perdite di memoria (memory leak) nel sistema, rendendo necessaria la rimozione esplicita della memoria condivisa quando non è più utilizzata.

### 5.3.4 - Socket

I **socket** sono un meccanismo di comunicazione tra processi che consentono a due o più processi di comunicare tra loro sia all'interno dello stesso sistema sia su sistemi diversi tramite rete. Nella comunicazione tra processi, i socket più utilizzati sono quelli di [dominio UNIX](Processi%20di%20un%20Sistema%20Operativo.md#5.3.4.1.2%20-%20Famiglie%20di%20socket) e quelli di [dominio Internet (IPv4 o IPv6)](Processi%20di%20un%20Sistema%20Operativo.md#5.3.4.3%20-%20Internet%20socket), e l'uso varia a seconda del tipo di applicazione e delle esigenze di comunicazione.

#### 5.3.4.1 - Caratteristiche principali dei socket%% SISTEMARE %%

Le caratteristiche principali dei socket sono:
- [**Half-duplex e full-duplex**](Processi%20di%20un%20Sistema%20Operativo.md#5.3.4.1.1%20-%20Half-duplex%20e%20full-duplex): i socket possono supportare la comunicazione o monodirezionale ([half-duplex](Processi%20di%20un%20Sistema%20Operativo.md#5.3.4.1.1.1%20-%20Half-duplex)) o bidirezionale ([full-duplex](Processi%20di%20un%20Sistema%20Operativo.md#5.3.4.1.1.2%20-%20Full-duplex)), in cui i dati possono essere inviati e ricevuti simultaneamente o solo in una direzione alla volta.
- [**Famiglia di socket**](Processi%20di%20un%20Sistema%20Operativo.md#5.3.4.1.2%20-%20Famiglie%20di%20socket): è un raggruppamento di socket che utilizzano gli stessi protocolli sottostanti, supporta un sottoinsieme di stili di comunicazione e possiede un proprio formato di indirizzamento.
- [**Tipo di socket**](Processi%20di%20un%20Sistema%20Operativo.md#5.3.4.1.3%20-%20Tipo%20di%20socket): definisce come i dati vengono trasmessi attraverso il socket e determina le modalità di comunicazione tra i dispositivi.
- [**Orientamento alla connessione**](Processi%20di%20un%20Sistema%20Operativo.md#5.3.4.1.4%20-%20Orientamento%20alla%20connessione): il tipo di collegamento stabilito tra due dispositivi che comunicano in rete che si distingue tra [connection-oriented](Processi%20di%20un%20Sistema%20Operativo.md#5.3.4.1.4.1%20-%20Connection-oriented%20(orientato%20alla%20connessione)) (in cui prima di iniziare la trasmissione dei dati, viene stabilita una connessione stabile e affidabile tra i dispositivi) e [connectionless](Processi%20di%20un%20Sistema%20Operativo.md#5.3.4.1.4.2%20-%20Connectionless%20(senza%20connessione)) (in cui non è necessario stabilire una connessione continua prima di inviare i dati).
- **Bloccanti e non-bloccanti**: possono essere configurati per operare in modalità bloccante (attesa di una risposta prima di procedere) o non-bloccante (eseguono altre operazioni in attesa della risposta).%%sistemare questo punto%%

##### 5.3.4.1.1 - Half-duplex e full-duplex

I dati nei socket possono essere trasferiti in due modalità:
- [**Half-duplex**](Processi%20di%20un%20Sistema%20Operativo.md#5.3.4.1.1.1%20-%20Half-duplex): i dati possono essere trasmessi in entrambe le direzioni tra due dispositivi, ma non contemporaneamente.
- [**Full-duplex**](Processi%20di%20un%20Sistema%20Operativo.md#5.3.4.1.1.2%20-%20Full-duplex): i dati possono essere trasmessi simultaneamente in entrambe le direzioni tra due dispositivi.

###### 5.3.4.1.1.1 - Half-duplex

Nella comunicazione **half-duplex**, i dati possono essere trasmessi in entrambe le direzioni tra due dispositivi, ma non contemporaneamente. Ciò significa che, in un dato momento, solo un dispositivo può inviare i dati mentre l'altro riceve.

Le principali caratteristiche delle comunicazioni half-duplex sono:
- **Comunicazione alternata**: se un dispositivo sta inviando, l'altro deve attendere prima di poter trasmettere.
- **Ritardo**: a causa della trasmissione alternata, possono verificarsi ritardi quando il controllo passa da un dispositivo all'altro.

Esempi di utilizzo delle comunicazioni half-duplex sono:
- **Walkie-talkie**: in un walkie-talkie, solo una persona alla volta può parlare mentre l'altra ascolta.
- **Reti wireless**: alcune reti Wi-Fi possono utilizzare modalità half-duplex per gestire il traffico.

###### 5.3.4.1.1.2 - Full-duplex

Nella comunicazione full-duplex, i dati possono essere trasmessi simultaneamente in entrambe le direzioni tra due dispositivi, permettendo così una comunicazione bidirezionale continua.

Le principali caratteristiche delle comunicazioni full-duplex sono:
- **Trasmissione simultanea**: entrambi i dispositivi possono inviare e ricevere dati contemporaneamente.
- **Maggiore efficienza**: riduce il ritardo poiché non è necessario alternare tra invio e ricezione.

Esempi di utilizzo delle comunicazioni full-duplex sono:
- **Telefonia**: durante una chiamata telefonica, entrambi gli interlocutori possono parlare e ascoltare simultaneamente.
- **Ethernet**: molti cavi Ethernet supportano la comunicazione full-duplex, migliorando la velocità di trasferimento dei dati.

###### 5.3.4.1.1.3 - Tabella riassuntiva delle differenze

Ecco una tabella riassuntiva che confronta la modalità [half-duplex](Processi%20di%20un%20Sistema%20Operativo.md#5.3.4.1.1.1%20-%20Half-duplex) e la modalità [full-duplex](Processi%20di%20un%20Sistema%20Operativo.md#5.3.4.1.1.2%20-%20Full-duplex):
%% controllare se la tabella nel rendering su Quartz ha i link in grassetto%%

| Caratteristica         | [Half-duplex](Processi%20di%20un%20Sistema%20Operativo.md#5.3.4.1.1.1%20-%20Half-duplex) | [Full-duplex](Processi%20di%20un%20Sistema%20Operativo.md#5.3.4.1.1.2%20-%20Full-duplex) |
| ---------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- |
| **Direzione dei dati** | Alternata (unidirezionale per volta)                                                     | Bidirezionale simu                                                                       |
| **Efficienza**         | Minore, per via dell'alternanza                                                          | Maggiore, grazie alla trasmissione s                                                     |
| **Ritardo**            | Potenziale ritardo dovuto all'attesa                                                     | Ridotto, poiché non c'                                                                   |
| **Esempi**             | Walkie-talkie, alcune reti Wi-Fi                                                         | Telefonia, Ethernet,                                                                     |

##### 5.3.4.1.2 - Famiglie di socket

Le **famiglie di socket** sono i raggruppamenti in cui vengono divisi i vari tipi di socket in base al tipo di protocollo di rete e il metodo di indirizzamento utilizzato per la comunicazione. Le principali famiglie di socket sono:
- **UNIX domain socket (`AF_UNIX` o `AF_LOCAL`)**: permette la comunicazione tra processi sullo stesso sistema operativo e utilizza file di sistema come punto di connessione, infatti il nome del socket è identificato dal percorso del file%%link%% (`/<path>/<filename>`).
- **[Internet socket](Processi%20di%20un%20Sistema%20Operativo.md#5.3.4.3%20-%20Internet%20socket) (`AF_INET` e `AF_INET6`)**: permette la comunicazione su reti IP%%link%%, sia locale che su Internet e usa indirizzi IP%%link%% (IPv4 e IPv6 rispettivamente per `AF_INET` e `AF_INET6`) e numeri di porta%%link%% per identificare i dispositivi, infatti il nome del socket è identificato dalla coppia indirizzo-porta (`<indirizzo IP>:<porta>`).
- **Bluetooth socket (`AF_BLUETOOTH`)**: viene utilizzato per la comunicazione su reti Bluetooth%%link%% e supporta connessioni wireless a corto raggio, ad esempio tra dispositivi mobili e periferiche. Per identificare i dispositivi, usa indirizzi MAC Bluetooth%%link%%, che sono identificatori unici per dispositivi Bluetooth (simili agli indirizzi MAC Ethernet%%link%%).
- **Packet socket (`AF_PACKET`)**: disponibile solo su Linux, permette l'accesso diretto ai pacchetti a livello di rete, senza passare per un protocollo specifico (come IP%%link%%). Usato per operazioni a basso livello come sniffing di rete e diagnostica.

##### 5.3.4.1.3 - Tipo di socket

Il **tipo di socket** definisce come i dati vengono trasmessi attraverso il socket e determina le modalità di comunicazione tra i dispositivi. I principali tipi di socket sono:
- **`SOCK_STREAM`**: utilizza il TCP (Transmission Control Protocol)%%link%% e fornisce una connessione affidabile ([connection-oriented](Processi%20di%20un%20Sistema%20Operativo.md#5.3.4.1.4.1%20-%20Connection-oriented%20(orientato%20alla%20connessione))), cioè i dati vengono trasmessi in modo sequenziale e senza errori, garantendo che arrivino nell'ordine giusto.
- **`SOCK_DGRAM`**: utilizza l'UDP (User Datagram Protocol)%%link%% e non richiede una connessione ([connectionless](Processi%20di%20un%20Sistema%20Operativo.md#5.3.4.1.4.2%20-%20Connectionless%20(senza%20connessione))), cioè i pacchetti possono essere persi o arrivare in ordine diverso, poiché non ci sono garanzie di consegna.
- **`SOCK_RAW`**: permette l'accesso diretto ai pacchetti a livello di rete, senza passare per un protocollo specifico (come TCP%%link%% o UDP%%link%%). Viene utilizzato per operazioni a basso livello, come il monitoraggio del traffico di rete e l'analisi dei pacchetti.
- **`SOCK_SEQPACKET`**: fornisce una connessione orientata ai pacchetti, simile a `SOCK_STREAM` ma con messaggi di lunghezza fissa. Garantisce la consegna dei pacchetti e mantiene l'ordine.

##### 5.3.4.1.4 - Orientamento alla connessione

L'**orientamento alla connessione** si riferisce al modo in cui le applicazioni comunicano tra loro attraverso una rete, specificando se una connessione deve essere stabilita e mantenuta prima del trasferimento dei dati. Questa modalità è particolarmente importante nel contesto dei socket e dei protocolli di comunicazione. Esistono due modalità di orientamento alla connessione: [connection-oriented](Processi%20di%20un%20Sistema%20Operativo.md#5.3.4.1.4.1%20-%20Connection-oriented%20(orientato%20alla%20connessione)) e [connectionless](Processi%20di%20un%20Sistema%20Operativo.md#5.3.4.1.4.2%20-%20Connectionless%20(senza%20connessione)).

###### 5.3.4.1.4.1 - Connection-oriented (orientato alla connessione)

In un sistema **connection-oriented (orientato alla connessione)**, è necessario stabilire una connessione affidabile tra due dispositivi (come client e server) prima che avvenga qualsiasi scambio di dati. Questo processo assicura che i dati vengano trasmessi in modo ordinato e senza perdite. Il protocollo più comune associato a questa modalità è il TCP (Transmission Control Protocol)%%link%% che garantisce che i pacchetti di dati arrivino nella sequenza corretta e senza errori.

Le principali caratteristiche dei sistemi connection-oriented sono:
- **Handshake iniziale**: prima di iniziare a inviare dati, il TCP%%link%% esegue un processo di handshake a tre vie per stabilire la connessione. Durante questo processo, il client e il server scambiano messaggi per confermare che sono pronti a comunicare.
- **Affidabilità**: il TCP%%link%% include meccanismi per garantire la consegna dei pacchetti, il controllo degli errori e la correzione degli errori. Se un pacchetto viene perso, il TCP si assicura che venga ritrasmesso.
- **Flusso di dati**: garantisce che i dati vengano inviati e ricevuti in un ordine preciso. Questa caratteristica è fondamentale per applicazioni come il trasferimento di file o le comunicazioni web, in cui la trasmissione dei dati in ordine casuale potrebbe creare problemi.

Esempi di utilizzo dei sistemi connection-oriented sono:
- **Web Browsing**: quando un browser si connette a un server web, stabilisce una connessione TCP%%link%% per garantire che tutte le informazioni vengano ricevute correttamente e nell'ordine giusto.
- **Email**: i protocolli come SMTP%%link%% (per inviare email) e POP3/IMAP%%link%% (per ricevere email) utilizzano connessioni TCP%%link%%.

###### 5.3.4.1.4.2 - Connectionless (senza connessione)

In un sistema **connectionless (senza connessione)**, i dati possono essere inviati senza stabilire una connessione permanente. Non è necessario alcun processo di handshake iniziale e i pacchetti possono viaggiare indipendentemente. Il protocollo più comune associato a questa modalità è l'UDP (User Datagram Protocol)%%link%% che non garantisce che i pacchetti vengano consegnati o che arrivino nell'ordine corretto.

Le principali caratteristiche dei sistemi connectionless sono:
- **Nessun handshake**: l'UDP%%link%% non richiede un processo di stabilimento della connessione, il che rende il trasferimento di dati più veloce.
- **Meno overhead**: non ci sono controlli di errore e riconoscimenti, il che riduce l'overhead e aumenta la velocità di trasmissione.
- **Inaffidabilità**: non c'è garanzia che i dati arrivino o che vengano ricevuti nell'ordine corretto. Questo può essere accettabile per alcune applicazioni, come streaming audio o video, dove la velocità è più importante della completezza.

Esempi di utilizzo dei sistemi connectionless sono:
- **Streaming**: i servizi di streaming video e audio utilizzano l'UDP%%link%% per trasmettere dati in tempo reale, dove è più importante ricevere i dati rapidamente piuttosto che garantirne l'integrità%%esempio dirette quando mancano qualche pixel o frame%%.
- **Giochi online**: molti giochi online usano l'UDP%%link%% per inviare rapidamente aggiornamenti di stato ai giocatori senza l'onere di garantire l'affidabilità.

###### 5.3.4.1.4.3 - Tabella riassuntiva delle differenze

Ecco una tabella riassuntiva che confronta la modalità [connection-oriented](Processi%20di%20un%20Sistema%20Operativo.md#5.3.4.1.4.1%20-%20Connection-oriented%20(orientato%20alla%20connessione)) e la modalità [connectionless](Processi%20di%20un%20Sistema%20Operativo.md#5.3.4.1.4.2%20-%20Connectionless%20(senza%20connessione)):

| Caratteristica                     | [Connection-oriented (orientato alla connessione)](Processi%20di%20un%20Sistema%20Operativo.md#5.3.4.1.4.1%20-%20Connection-oriented%20(orientato%20alla%20connessione)) | [Connectionless (senza connessione)](Processi%20di%20un%20Sistema%20Operativo.md#5.3.4.1.4.2%20-%20Connectionless%20(senza%20connessione)) |
| ---------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------ |
| **Protocollo comune**              | TCP (Transmission Control Protocol)%%link%%                                                                                                                              | UDP (User Datagram Protocol)%%link%%                                                                                                       |
| **Stabilimento della connessione** | Richiede un handshake iniziale a 3 vie                                                                                                                                   | Nessun handshake necessario                                                                                                                |
| **Affidabilità**                   | Garantita (controlla la consegna e l'ordine dei dati)                                                                                                                    | Non garantita (i dati possono andare persi o arrivare fuori ordine)                                                                        |
| **Overhead**                       | Maggiore (a causa di controlli di errore e ritrasmissione)                                                                                                               | Minore (poiché non ci sono controlli di errore)                                                                                            |
| **Velocità**                       | Più lenta (a causa dell'overhead e della gestione della connessione)                                                                                                     | Più veloce (grazie all'assenza di overhead)                                                                                                |
| **Esempi di utilizzo**             | Browsing web, email, trasferimento di file                                                                                                                               | Streaming video/audio, giochi online                                                                                                       |
| **Flusso di dati**                 | Ordinato (i dati vengono ricevuti nell'ordine corretto)                                                                                                                  | Non ordinato (i dati possono arrivare in ordine casuale)                                                                                   |
| **Gestione degli errori**          | Inclusa (ritrasmissione automatica in caso di errore)                                                                                                                    | Assente (l'applicazione deve gestire eventuali errori)                                                                                     |
| **Uso di risorse**                 | Maggiore uso di risorse di rete e CPU                                                                                                                                    | Minore uso di risorse, poiché non ci sono controlli                                                                                        |

#### 5.3.4.2 - Vantaggi e svantaggi dei socket

I principali vantaggi dei socket sono:
- **Flessibilità**: permettono una varietà di protocolli di trasporto%%link%% (TCP%%link%%/UDP%%link%%) e [orientamento alla connessione](Processi%20di%20un%20Sistema%20Operativo.md#5.3.4.1.4%20-%20Orientamento%20alla%20connessione) ([connection-oriented](Processi%20di%20un%20Sistema%20Operativo.md#5.3.4.1.4.1%20-%20Connection-oriented%20(orientato%20alla%20connessione))/[connectionless](Processi%20di%20un%20Sistema%20Operativo.md#5.3.4.1.4.2%20-%20Connectionless%20(senza%20connessione))), adattandosi a diverse esigenze di comunicazione.
- **Efficienza nella comunicazione**: offrono un metodo standard per lo scambio di dati tra dispositivi, consentendo connessioni rapide tra applicazioni su macchine differenti.
- **Compatibilità cross-platform**: le API dei socket sono disponibili e relativamente simili su molti sistemi operativi, facilitando lo sviluppo di applicazioni distribuite.
- **Affidabilità con il TCP**: con il TCP%%link%%, i socket garantiscono che i dati arrivino in modo sicuro, ordinato e senza perdite. È quindi ideale per applicazioni critiche come web server, trasferimento di file e posta elettronica.
- **Supporto alla comunicazione in tempo reale con l'UDP**: con l'UDP%%link%%, i socket permettono una comunicazione veloce, poiché non hanno overhead di connessione, rendendoli ideali per streaming, giochi online, e applicazioni dove la velocità è più importante della precisione.
- **Multithreading e scalabilità**: i socket possono essere gestiti in modo asincrono o su più [thread](Processi%20di%20un%20Sistema%20Operativo.md#6%20-%20Thread), permettendo a un singolo server di gestire più connessioni contemporaneamente, aumentando così la scalabilità dell'applicazione.

I principali svantaggi dei socket sono:
- **Complessità di gestione**: richiedono una gestione accurata dei processi di connessione e chiusura, con il rischio di problemi come il blocco dei socket, connessioni non terminate correttamente, o errori di timeout.
- **Overhead con il TCP**: le connessioni che usano il TCP%%link%% implicano un certo overhead per il controllo di errori e la garanzia di consegna, aumentando la latenza. Non è ideale per applicazioni che richiedono un trasferimento estremamente rapido di piccoli pacchetti di dati.
- **Limitata sicurezza intrinseca**: di per sé, i socket non offrono cifratura o autenticazione dei dati. Per garantire sicurezza, è necessario implementare soluzioni aggiuntive come TLS/SSL%%link%%.
- **Vulnerabilità a attacchi**: i socket sono esposti ad attacchi come DDoS (Distributed Denial of Service) e hijacking, in cui malintenzionati possono sfruttare le connessioni aperte.
- **Supporto limitato per la trasmissione multicast**: sebbene l'UDP%%link%% supporti il multicast, cioè l'invio di dati a più destinatari, i socket TCP%%link%% non lo fanno nativamente, limitando la comunicazione a un solo client per connessione.
- **Problemi di firewall e NAT**: i firewall e i router NAT possono bloccare o ostacolare la connessione dei socket, causando problemi di accesso e richiedendo configurazioni aggiuntive.

#### 5.3.4.3 - Internet socket

Gli **Internet socket** sono una [famiglia di socket](Processi%20di%20un%20Sistema%20Operativo.md#5.3.4.1.2%20-%20Famiglie%20di%20socket) utilizzati per la comunicazione su reti basate su IP, come Internet. Questi socket possono essere utilizzati per stabilire connessioni tra dispositivi che si trovano anche in posizioni geografiche diverse.

Gli internet socket hanno le seguenti caratteristiche principali:
- **Indirizzamento**: ogni socket è identificato univocamente da un indirizzo IP%%link%% e da una porta%%link%%, che consentono ai dispositivi di indirizzare correttamente i dati.
- **Protocollo**: i socket utilizzano protocolli di trasporto che determinano come vengono trasferiti i dati. I due protocolli più usati sono il TCP (Transmission Control Protocol)%%link%%, che crea una connessione stabile e affidabile e garantisce la consegna dei dati in modo ordinato e senza perdite, e l'UDP (User Datagram Protocol)%%link%%, che crea una connessione più leggera e veloce, ma non garantisce affidabilità, sequenzialità o controllo della perdita di pacchetti.

##### 5.3.4.3.1 - Funzionamento degli internet socket

Il funzionamento base di un socket è il seguente:
1. **Creazione di un socket**: un'applicazione crea un socket, specificando il tipo di protocollo%%link%% (come TCP%%link%% o UDP%%link%%) e altre opzioni (ad esempio, indirizzo IP%%link%% e porta%%link%%). Nei sistemi basati su UNIX, questo avviene tipicamente con la funzione `socket()`, che restituisce un identificatore%%ID?%% del socket.
2. **Associazione (binding)**: nel caso di un server, il socket viene "associato" a un indirizzo IP%%link%% e una porta%%link%% con l'operazione di binding. Questo assicura che il socket ascolti su uno specifico indirizzo e sia accessibile per le connessioni in entrata. Ad esempio, in un server web, il socket è spesso associato alla porta 80 (HTTP%%link%%) o 443 (HTTPS%%link%%). %%Perché proprio questi due numeri specifici di porta?%%
3. **Modalità d'ascolto e connessione**: server e client svolgono funzioni diverse.
	- **Server**: il socket entra in modalità d'ascolto con la funzione `listen()`, in attesa di connessioni in entrata. Quando un client tenta di connettersi, il server accetta la connessione con la funzione `accept()`, che restituisce un nuovo socket per gestire la comunicazione con il client.
	- **Client**: il client richiede una connessione con il server attraverso il socket e la funzione `connect()`, specificando l'indirizzo IP%%link%% e la porta%%link%% del server.
4. **Trasferimento dei dati**: una volta stabilita la connessione, il client e il server possono scambiarsi dati. I dati sono inviati e ricevuti (in pacchetti) tramite funzioni di lettura e scrittura, come `send()` e `recv()` in TCP%%link%%, che garantiscono la consegna, oppure `sendto()` e `recvfrom()` in UDP%%link%%, dove non è garantita.
5. **Chiusura della connessione**: al termine della comunicazione, il socket viene chiuso. Nel TCP%%link%%, entrambe le parti devono chiudere il socket per terminare la connessione (half-close), garantendo che non ci siano dati persi. Nell'UDP%%link%%, che è senza connessione, la chiusura non ha bisogno di un processo specifico.

%%

\### 5. **Segnali (Signals)**
   - I **segnali** sono un metodo per inviare notifiche asincrone a un processo. Un processo può ricevere segnali che indicano la necessità di eseguire qualche azione (es. terminazione, interruzione).
   - Esempi: `kill()`, `signal()`.

\### 6. **Semafori (Semaphores)**
   - I **semafori** sono variabili che vengono utilizzate per gestire l'accesso concorrente alle risorse condivise, come la memoria condivisa. Aiutano a evitare situazioni come il **race condition**.
   - Esempi: `semget()`, `semop()`.

\### 7. **File temporanei**
   - I **file temporanei** possono essere usati per lo scambio di dati tra processi. I dati vengono scritti su file e letti da altri processi.

\### 8. **RPC (Remote Procedure Call)**
   - Un **RPC** permette a un processo di chiamare una funzione eseguita su un altro processo (anche su un'altra macchina). Maschera la complessità della comunicazione, rendendola simile a una chiamata di funzione locale.
   - Esempi: gRPC, XML-RPC.

\### 9. **Database e Sistemi di File**
   - Un processo può scrivere dati in un database o file, e un altro processo può leggerli. Questo metodo è meno efficiente rispetto ad altri, ma può essere utile per la persistenza e condivisione di grandi quantità di dati.
%%

%%
\### 6. **Coordinamento e sincronizzazione tra processi**
   Nei sistemi con **processi concorrenti**, è necessario coordinare l'esecuzione di più processi per evitare problemi come **race conditions** (condizioni di corsa) o **deadlock** (stallo). Le operazioni per la sincronizzazione includono:

   - **Mutua esclusione**: Garantisce che un solo processo possa accedere a una risorsa condivisa alla volta (utilizzando semafori o mutex).
   - **Semafori**: I **semafori** sono variabili utilizzate per controllare l'accesso a risorse condivise, permettendo ai processi di attendere in modo sicuro l'accesso a una risorsa.
   - **Monitor**: I **monitor** sono costrutti di alto livello per gestire la mutua esclusione e la sincronizzazione dei processi.

\### 7. **Forking e clonazione di processi**
   Alcuni sistemi operativi (come Unix/Linux) permettono a un processo di creare una **copia di se stesso** tramite l'operazione di **fork**. Il processo figlio risultante è una replica del processo padre, con la stessa memoria, ma con un diverso **PID**.

\### 8. **Gestione dei segnali (Signals)**
   I processi possono inviare e ricevere **segnali**, che sono notifiche asincrone inviate dal sistema operativo o da altri processi per segnalare eventi come errori, richieste di terminazione o altri eventi specifici. Ad esempio, in Unix/Linux, il comando **kill** invia segnali a un processo (ad esempio, **SIGTERM** per richiedere la terminazione del processo).

\### 9. **Esecuzione di processi in foreground e background**
   Nei sistemi multiutente, è possibile eseguire un processo in **foreground** (in primo piano) o in **background** (sullo sfondo). Un processo in background può continuare a essere eseguito mentre l'utente esegue altre attività.

\### In sintesi:
Le operazioni sui processi sono fondamentali per gestire l'esecuzione dei programmi in un sistema operativo. Esse includono la **creazione**, la **terminazione**, la **comunicazione**, la **sincronizzazione**, e la **schedulazione** dei processi, tutte attività necessarie per garantire l'efficienza e la stabilità del sistema.
%%

# 6 - Thread

Un _thread_ (abbreviazione di _thread of execution_, _filo dell'esecuzione_) è l'unità granulare in cui un processo può essere suddiviso e che può essere eseguito a divisione di tempo (cioè assegnando a ognuno una determinata porzione di tempo in cui poter essere eseguito) o in parallelo ad altri thread da parte del processore. In altre parole, un thread è una parte del processo che viene eseguita, in maniera concorrente ed indipendente, internamente allo stato generale del processo stesso.

## 6.1 - Differenza tra processo e thread

I termini _processo_ e _thread_, nonostante a volte vengano usati in maniera interscambiabile, in realtà indicano due cose distinte:
- Un processo è un'istanza indipendente del programma, con il proprio spazio di memoria.
- Un thread è un'unità di esecuzione all'interno di un processo. Più thread possono condividere lo stesso spazio di memoria del processo.

Il termine inglese rende bene l'idea, in quanto si rifà visivamente al concetto di fune composta da vari fili attorcigliati: se la fune è il processo in esecuzione, allora i singoli fili che la compongono sono i thread.

%%
La differenza tra **processo** e **thread** è fondamentale nella gestione dell'esecuzione delle applicazioni in un sistema operativo. Sebbene siano concetti correlati, rappresentano unità diverse di esecuzione, con caratteristiche e scopi distinti.

\### 1. Processo:
Un **processo** è un'istanza di un programma in esecuzione. È l'unità di esecuzione principale del sistema operativo, con risorse e uno spazio di memoria proprio. Ogni processo è indipendente dagli altri e dispone di un proprio spazio di indirizzamento nella memoria, il che significa che i dati di un processo non sono condivisibili direttamente con quelli di un altro processo (salvo meccanismi appositi, come la memoria condivisa o la comunicazione inter-processo).

\#### Caratteristiche del processo
- **Spazio di memoria separato**: Ogni processo ha il proprio spazio di memoria (stack, heap, segmenti dati, codice).
- **Isolamento**: I processi sono isolati l'uno dall'altro, il che significa che un processo non può accedere direttamente alla memoria o alle risorse di un altro processo.
- **Interazione complessa**: La comunicazione tra processi (IPC - Inter-Process Communication) è relativamente complessa, richiedendo meccanismi come pipe, socket, o file condivisi.
- **Overhead elevato**: Creare e gestire processi ha un overhead elevato, poiché il sistema operativo deve allocare risorse separate per ogni processo.

\### 2. Thread:
Un **thread** (o thread di esecuzione) è l'unità di esecuzione più piccola che può essere schedulata dal sistema operativo. Un **thread** è parte di un processo e tutti i thread di un processo condividono lo stesso spazio di memoria e le stesse risorse del processo che li contiene. Un singolo processo può avere uno o più thread (questo è il concetto di **multithreading**).

\#### Caratteristiche del thread
- **Spazio di memoria condiviso**: I thread di un processo condividono lo stesso spazio di memoria e le risorse (stack, heap, dati, ecc.).
- **Interazione semplice**: I thread all'interno di uno stesso processo possono facilmente condividere dati tra loro, poiché accedono allo stesso spazio di memoria.
- **Overhead ridotto**: Creare e gestire thread è più efficiente rispetto ai processi, poiché i thread condividono le risorse del processo padre e non richiedono la creazione di uno spazio di memoria separato.
- **Esecuzione concorrente**: I thread possono essere eseguiti in modo concorrente o parallelo su sistemi multi-core, consentendo una migliore performance per attività che possono essere suddivise in compiti più piccoli.

\### Differenze principali tra processo e thread:

| Caratteristica         | **Processo**                               | **Thread**                                  |
|------------------------|--------------------------------------------|---------------------------------------------|
| **Spazio di memoria**   | Ha uno spazio di memoria separato          | Condivide lo spazio di memoria con altri thread del processo |
| **Isolamento**          | Isolato da altri processi                  | Condivide le risorse con altri thread nel processo |
| **Comunicazione**       | Comunicazione inter-processo (IPC) complessa | Comunicazione interna semplice (tramite memoria condivisa) |
| **Creazione**           | Maggiore overhead nella creazione e gestione | Più leggero e rapido da creare e gestire    |
| **Esecuzione**          | Un processo può avere uno o più thread, eseguiti separatamente | Ogni thread è un'unità di esecuzione all'interno di un processo |
| **Crashing**            | Se un processo va in crash, non influenza altri processi | Se un thread va in crash, può compromettere l'intero processo |
| **Cambio di contesto**  | Richiede un cambio di contesto completo (salvataggio di registri, memoria, ecc.) | Il cambio di contesto tra thread è più rapido poiché condividono memoria e risorse |

\### Esempio pratico:</span>
- **Processo**: Immagina di avviare un'applicazione come un editor di testo. Quando l'applicazione viene avviata, il sistema operativo crea un processo con il suo spazio di memoria. Se apri una seconda istanza dell'editor, viene creato un nuovo processo.
- **Thread**: All'interno dell'editor di testo, ci possono essere più thread: uno che gestisce la visualizzazione del testo, un altro che gestisce il salvataggio automatico, e un altro che risponde ai comandi dell'utente. Tutti questi thread lavorano contemporaneamente e condividono lo stesso spazio di memoria, consentendo un'esecuzione fluida e parallela delle operazioni.

\### Riassunto:
- Un **processo** è un'istanza di un programma in esecuzione, con uno spazio di memoria indipendente e isolato.
- Un **thread** è un'unità di esecuzione all'interno di un processo, con un overhead minore e uno spazio di memoria condiviso con altri thread dello stesso processo.
- I processi sono utili per l'esecuzione di programmi separati e indipendenti, mentre i thread sono utilizzati per suddividere le attività all'interno di uno stesso programma, migliorando la performance e la reattività grazie alla concorrenza o parallelismo.

In sintesi: **ogni processo può contenere più thread**, ma i **thread** appartengono sempre a un **processo**.
%%

## 6.2 - Utilità dei thread

I thread servono appositamente per rendere concorrente l'esecuzione di più operazioni all'interno di uno stesso processo: se un processo sta, per esempio, eseguendo un browser, l'esecuzione avviene seguendo una singola sequenza di istruzioni; quindi il processo può svolgere un solo compito alla volta. Tramite lo stesso processo, per esempio, un utente non può contemporaneamente inserire caratteri e verificare la correttezza ortografica di quel che sta scrivendo.

Questa funzione è particolarmente utile sui sistemi multicore, in cui più thread possono essere eseguiti in parallelo. In un sistema che supporta i thread, il [PCB](Processi%20di%20un%20Sistema%20Operativo.md#2%20-%20Il%20PCB%20e%20le%20informazioni%20sul%20processo) viene esteso per includere informazioni su ogni thread.

%%
\# Fonti
- Slide del Prof. Aldinucci
	- 
- Libro di SO
	- 

Prendere info da:
- Libro di SO
	- Capitoli 3.7.2 e 3.7.3 (IPC su Mach e Windows)
- https://it.wikipedia.org/wiki/Processo_(informatica)
- https://it.wikipedia.org/wiki/Thread_(informatica)
- https://it.wikipedia.org/wiki/Pipe_(informatica)
- https://en.wikipedia.org/wiki/Pipeline_(Unix)
- https://en.wikipedia.org/wiki/Anonymous_pipe
- https://en.wikipedia.org/wiki/Named_pipe
%%


