---
icon: IbPhoneCallTransfer
iconColor: "#88FF88"
---
Le **chiamate di procedure remote** (in inglese _**RPC**_, _**R**emote **P**rocedure **C**alls_) sono un meccanismo di [comunicazione tra processi](Processi.md#7%20-%20Comunicazione%20tra%20processi%20(IPC)) che consentono a un programma di eseguire una procedura (funzione o subroutine) in un altro indirizzo di rete, come se fosse una funzione locale. Questo tipo di comunicazione è usato frequentemente in sistemi distribuiti per facilitare l'interazione tra componenti che risiedono su macchine diverse.

# 1 - Caratteristiche principali

- **Trasparenza della rete**: le RPC nascondono i dettagli di rete, permettendo agli sviluppatori di chiamare funzioni remote come funzioni locali, semplificando il codice e la logica applicativa. La comunicazione tra client e server avviene senza che il chiamante debba preoccuparsi di dettagli come indirizzi IP%%link%%, porte%%link%% o protocolli%%link%%.
- **Indipendenza dalla piattaforma e dal linguaggio**: molti sistemi di RPC sono progettati per essere indipendenti dal linguaggio di programmazione e dalla piattaforma, consentendo la comunicazione tra componenti eterogenei (ad esempio, un'app Java su Linux può chiamare una procedura C# su Windows).
- **Modello client-server**: le RPC si basano su un'architettura client-server, in cui il client richiede l'esecuzione della procedura e il server la esegue e restituisce il risultato.
- **Gestione degli errori e delle condizioni di guasto**: in un ambiente di rete, possono verificarsi guasti come timeout, interruzioni di connessione o server non raggiungibili, quindi le RPC devono implementare meccanismi per gestire questi errori, come ritentativi automatici, gestione delle eccezioni e timeout configurabili.
- **Sicurezza**: le RPC spesso includono meccanismi di autenticazione, autorizzazione e crittografia per proteggere la comunicazione tra client e server e garantire che solo gli utenti autorizzati possano accedere ai servizi.
- **Efficienza**: le RPC devono essere efficienti e leggere per poter supportare una vasta gamma di applicazioni distribuite.
- **Asincronia e synchronous calls**: sebbene le RPC tradizionali siano sincrone (il client attende la risposta dal server), alcune implementazioni supportano anche chiamate asincrone per evitare il blocco del client. Le chiamate asincrone sono particolarmente utili in applicazioni ad alte prestazioni e in ambienti distribuiti complessi.

# 2 - Funzionamento delle RPC

Il **funzionamento delle RPC** si basa su un meccanismo che permette a un programma di richiedere l'esecuzione di una funzione su un sistema remoto, come se fosse una normale chiamata a una funzione locale.

I principali passaggi e i componenti chiave di questo processo sono:
1. **Chiamata del client**: con un programma client che desidera utilizzare una funzione specifica disponibile su un server remoto, il client non deve preoccuparsi di come inviare la richiesta al server; al contrario, invoca semplicemente la funzione come se fosse una funzione locale.
2. **Stub del client**: quando il client invoca la funzione, questa chiamata non parte direttamente verso il server. Invece, viene intercettata da un componente chiamato _stub del client_: esso agisce come un "proxy" per la funzione remota, preparandosi a inviare la richiesta al server.
3. **Marshalling dello stub**: per inviare la richiesta al server, lo stub raccoglie i dati necessari (i parametri della funzione) e li serializza in un formato standard compatibile con la trasmissione su rete: questo processo è chiamato _marshalling_ e assicura che i dati possano essere compresi dall'altro lato della comunicazione, indipendentemente dal sistema operativo o dal linguaggio di programmazione.
4. **Invio della richiesta alla rete**: dopo aver effettuato il marshalling, lo stub del client invia i dati attraverso la rete verso il server. In questa fase, il sistema di comunicazione di rete (tipicamente utilizzando il protocollo TCP/IP%%link%%) si occupa di consegnare i dati al server remoto.
5. **Skeleton del server**: sul lato del server, un componente chiamato _skeleton_ riceve la richiesta. Questo skeleton è, in un certo senso, il "gemello" dello stub, e ha il compito di agire come rappresentante della funzione remota. Una volta ricevuta la richiesta, lo skeleton esegue il processo inverso al marshalling, chiamato _demarshalling_, col quale i dati vengono deserializzati e convertiti in un formato che può essere interpretato e utilizzato dal server.
6. **Esecuzione della funzione remota**: una volta completato il demarshalling, lo skeleton chiama la funzione effettiva sul server (la stessa invocata dal client) e passa i parametri originali. La funzione viene quindi eseguita localmente sul server e produce un risultato.
7. **Restituzione del risultato**: il risultato ottenuto dall'esecuzione della funzione viene quindi restituito dallo skeleton, che si occupa di trasformarlo di nuovo in un formato standard, facendo il marshalling del risultato per prepararlo alla trasmissione. I dati vengono inviati indietro attraverso la rete, tornando verso lo stub del client.
8. **Riconversione e risultato finale**: quando i dati tornano al client, lo stub del client esegue di nuovo il demarshalling per trasformare i dati ricevuti in un formato comprensibile dall'applicazione client. Infine, lo stub restituisce il risultato al client, che lo riceve come se fosse stato prodotto da una funzione locale.

# 3 - Vantaggi e svantaggi delle RPC

I principali vantaggi delle RPC sono:
- **Trasparenza della rete**: le RPC nascondono i dettagli di rete, permettendo agli sviluppatori di invocare funzioni remote con una sintassi simile a quella locale. Questo riduce la complessità e facilita lo sviluppo di applicazioni distribuite.
- **Astrazione della comunicazione**: il client non deve preoccuparsi di gestire le connessioni di rete, il formato dei dati o i protocolli di comunicazione. Lo stub e lo skeleton si occupano di tutti i dettagli tecnici, semplificando il codice applicativo.
- **Riusabilità e modularità**: con le RPC, le funzioni server possono essere utilizzate da diverse applicazioni e client. Questo migliora la modularità, rendendo i componenti del sistema più riutilizzabili e facilitando lo sviluppo di architetture distribuite.
- **Indipendenza dalla piattaforma e dal linguaggio**: alcune implementazioni RPC, come gRPC%%link%%, permettono di creare servizi compatibili tra diversi linguaggi di programmazione e sistemi operativi, rendendo le RPC adatte a progetti complessi ed eterogenei.
- **Supporto per sistemi distribuiti**: le RPC sono progettate per sistemi distribuiti e favoriscono una struttura client-server, spesso essenziale per applicazioni come microservizi, in cui diversi componenti comunicano tra loro in rete.

I principali svantaggi delle RPC sono:
- **Dipendenza dalla rete**: la performance delle RPC dipende fortemente dalla rete, in quanto eventuali problemi di connessione, come latenza o instabilità, possono rallentare le chiamate o provocare errori, riducendo l'affidabilità del sistema.
- **Gestione complessa degli errori**: gestire errori di rete, timeout, o guasti dei server può essere difficile. Le RPC devono implementare meccanismi di gestione dei guasti, ma questi aggiungono complessità al sistema e richiedono un'accurata gestione degli errori.
- **Overhead di marshalling e demarshalling**: il processo di serializzazione e deserializzazione dei dati per adattarli al formato di rete introduce un overhead. In scenari ad alte prestazioni, questo può essere un collo di bottiglia.
- **Limiti sui tipi di dati complessi**: il marshalling di dati complessi (come oggetti, strutture nidificate o referenze) può essere difficile e non sempre supportato, a meno di utilizzare strumenti avanzati di serializzazione, che però aumentano la complessità.
- **Sicurezza e autenticazione**: poiché i dati viaggiano sulla rete, le RPC devono spesso implementare meccanismi di autenticazione, autorizzazione e crittografia, aggiungendo ulteriore complessità e possibili punti deboli alla sicurezza.
- **Costi di manutenzione e debug**: diagnosticare e risolvere i problemi in un sistema distribuito è più difficile rispetto a un'applicazione locale. Tracciamento e monitoraggio diventano essenziali, ma introducono un ulteriore livello di complessità e richiedono strumenti dedicati.

# Fonti

- Abraham Silberschatz, Peter Baer Galvin, Greg Gagne - [Sistemi Operativi (10ᵃ Edizione)](https://he.pearson.it/catalogo/1099) - Pearson, 2019 - ISBN: `9788891904560`.
- Slide del Prof. Aldinucci Marco del corso di Sistemi Operativi (canale B), Corso di Laurea in Informatica presso l'Università di Torino, A.A. 2024-25:
	- [Cap_03](https://informatica.i-learn.unito.it/mod/resource/view.php?id=253884)
