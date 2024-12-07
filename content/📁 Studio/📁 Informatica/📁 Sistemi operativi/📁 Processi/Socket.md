I **socket** sono un meccanismo di [comunicazione tra processi](Processi.md#7%20-%20Comunicazione%20tra%20processi%20(IPC)) che consentono a due o più processi di comunicare tra loro sia all'interno dello stesso sistema sia su sistemi diversi tramite rete. Nella comunicazione tra processi, i socket più utilizzati sono quelli di [dominio UNIX](Socket.md#1.2%20-%20Famiglie%20di%20socket) %%cambiare link poi quando farò sezione specifica per dominio UNIX%%e quelli di [dominio Internet (IPv4 o IPv6)](Socket.md#3%20-%20Internet%20socket), e l'uso varia a seconda del tipo di applicazione e delle esigenze di comunicazione.

# 1 - Caratteristiche principali

- [**Half-duplex e full-duplex**](Socket.md#1.1%20-%20Half-duplex%20e%20full-duplex): i socket possono supportare la comunicazione bidirezionale alternata ([half-duplex](Socket.md#1.1.1%20-%20Half-duplex)) o bidirezionale simultanea ([full-duplex](Socket.md#1.1.2%20-%20Full-duplex)), in cui i dati possono essere inviati e ricevuti rispettivamente solo in una direzione alla volta oppure in entrambe contemporaneamente.
- [**Famiglia di socket**](Socket.md#1.2%20-%20Famiglie%20di%20socket): è un raggruppamento di socket che utilizzano gli stessi protocolli sottostanti, supporta un sottoinsieme di stili di comunicazione e possiede un proprio formato di indirizzamento.
- [**Tipo di socket**](Socket.md#1.3%20-%20Tipo%20di%20socket): definisce come i dati vengono trasmessi attraverso il socket e determina le modalità di comunicazione tra i dispositivi.
- [**Orientamento alla connessione**](Socket.md#1.4%20-%20Orientamento%20alla%20connessione): il tipo di collegamento stabilito tra due dispositivi che comunicano in rete che si distingue tra [connection-oriented](Socket.md#1.4.1%20-%20Connection-oriented%20(orientato%20alla%20connessione)) (in cui prima di iniziare la trasmissione dei dati, viene stabilita una connessione stabile e affidabile tra i dispositivi) e [connectionless](Socket.md#1.4.2%20-%20Connectionless%20(senza%20connessione)) (in cui non è necessario stabilire una connessione continua prima di inviare i dati).
- **Bloccanti e non-bloccanti**: possono essere configurati per operare in modalità bloccante (attesa di una risposta prima di procedere) o non-bloccante (eseguono altre operazioni in attesa della risposta).%%sistemare questo punto%%

## 1.1 - Half-duplex e full-duplex

I dati nei socket possono essere trasferiti in due modalità:
- [**Half-duplex**](Socket.md#1.1.1%20-%20Half-duplex): i dati possono essere trasmessi in entrambe le direzioni tra due dispositivi, ma non contemporaneamente.
- [**Full-duplex**](Socket.md#1.1.2%20-%20Full-duplex): i dati possono essere trasmessi simultaneamente in entrambe le direzioni tra due dispositivi.

### 1.1.1 - Half-duplex

Nella comunicazione **half-duplex**, i dati possono essere trasmessi in entrambe le direzioni tra due dispositivi, ma non contemporaneamente. Ciò significa che, in un dato momento, solo un dispositivo può inviare i dati mentre l'altro riceve.

Le principali caratteristiche delle comunicazioni half-duplex sono:
- **Comunicazione alternata**: se un dispositivo sta inviando, l'altro deve attendere prima di poter trasmettere.
- **Ritardo**: a causa della trasmissione alternata, possono verificarsi ritardi quando il controllo passa da un dispositivo all'altro.

Esempi di utilizzo delle comunicazioni half-duplex sono:
- **Walkie-talkie**: in un walkie-talkie, solo una persona alla volta può parlare mentre l'altra ascolta.
- **Reti wireless**: alcune reti Wi-Fi possono utilizzare modalità half-duplex per gestire il traffico.

### 1.1.2 - Full-duplex

Nella comunicazione full-duplex, i dati possono essere trasmessi simultaneamente in entrambe le direzioni tra due dispositivi, permettendo così una comunicazione bidirezionale continua.

Le principali caratteristiche delle comunicazioni full-duplex sono:
- **Trasmissione simultanea**: entrambi i dispositivi possono inviare e ricevere dati contemporaneamente.
- **Maggiore efficienza**: riduce il ritardo poiché non è necessario alternare tra invio e ricezione.

Esempi di utilizzo delle comunicazioni full-duplex sono:
- **Telefonia**: durante una chiamata telefonica, entrambi gli interlocutori possono parlare e ascoltare simultaneamente.
- **Ethernet**: molti cavi Ethernet supportano la comunicazione full-duplex, migliorando la velocità di trasferimento dei dati.

### 1.1.3 - Tabella riassuntiva delle differenze

Ecco una tabella riassuntiva che confronta la modalità [half-duplex](Socket.md#1.1.1%20-%20Half-duplex) e la modalità [full-duplex](Socket.md#1.1.2%20-%20Full-duplex):

| Caratteristica         | [Half-duplex](Socket.md#1.1.1%20-%20Half-duplex) | [Full-duplex](Socket.md#1.1.2%20-%20Full-duplex)   |
| ---------------------- | ---------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------ |
| **Direzione dei dati** | Bidirezionale, ma non simultanea (un solo dispositivo trasmette alla volta)              | Bidirezionale e simultanea (entrambi i dispositivi possono trasmettere contemporaneamente) |
| **Efficienza**         | Minore, per via dell'alternanza                                                          | Maggiore, grazie alla trasmissione simultanea                                              |
| **Ritardo**            | Potenziale ritardo dovuto all'attesa                                                     | Ridotto, poiché non c'è attesa                                                             |
| **Esempi**             | Walkie-talkie, alcune reti Wi-Fi                                                         | Telefonia, Ethernet                                                                        |

## 1.2 - Famiglie di socket

Le **famiglie di socket** sono i raggruppamenti in cui vengono divisi i vari tipi di socket in base al tipo di protocollo di rete e il metodo di indirizzamento utilizzato per la comunicazione. Le principali famiglie di socket sono:
- **UNIX domain socket (`AF_UNIX` o `AF_LOCAL`)**: permette la comunicazione tra processi sullo stesso sistema operativo e utilizza file di sistema come punto di connessione, infatti il nome del socket è identificato dal percorso del file%%link%% (`/<path>/<filename>`).
- **[Internet socket](Socket.md#3%20-%20Internet%20socket) (`AF_INET` e `AF_INET6`)**: permette la comunicazione su reti IP%%link%%, sia locale che su Internet e usa indirizzi IP%%link%% (IPv4 e IPv6 rispettivamente per `AF_INET` e `AF_INET6`) e numeri di porta%%link%% per identificare i dispositivi, infatti il nome del socket è identificato dalla coppia indirizzo-porta (`<indirizzo IP>:<porta>`).
- **Bluetooth socket (`AF_BLUETOOTH`)**: viene utilizzato per la comunicazione su reti Bluetooth%%link%% e supporta connessioni wireless a corto raggio, ad esempio tra dispositivi mobili e periferiche. Per identificare i dispositivi, usa indirizzi MAC Bluetooth%%link%%, che sono identificatori unici per dispositivi Bluetooth (simili agli indirizzi MAC Ethernet%%link%%).
- **Packet socket (`AF_PACKET`)**: disponibile solo su Linux, permette l'accesso diretto ai pacchetti a livello di rete, senza passare per un protocollo specifico (come l'IP%%link%%). Usato per operazioni a basso livello come sniffing di rete e diagnostica.

## 1.3 - Tipo di socket

Il **tipo di socket** definisce come i dati vengono trasmessi attraverso il socket e determina le modalità di comunicazione tra i dispositivi. I principali tipi di socket sono:
- **`SOCK_STREAM`**: utilizza il TCP (Transmission Control Protocol)%%link%% e fornisce una connessione affidabile ([connection-oriented](Socket.md#1.4.1%20-%20Connection-oriented%20(orientato%20alla%20connessione))), cioè i dati vengono trasmessi in modo sequenziale e senza errori, garantendo che arrivino nell'ordine giusto.
- **`SOCK_DGRAM`**: utilizza l'UDP (User Datagram Protocol)%%link%% e non richiede una connessione ([connectionless](Socket.md#1.4.2%20-%20Connectionless%20(senza%20connessione))), cioè i pacchetti possono essere persi o arrivare in ordine diverso, poiché non ci sono garanzie di consegna.
- **`SOCK_RAW`**: permette l'accesso diretto ai pacchetti a livello di rete, senza passare per un protocollo specifico (come TCP%%link%% o UDP%%link%%). Viene utilizzato per operazioni a basso livello, come il monitoraggio del traffico di rete e l'analisi dei pacchetti.
- **`SOCK_SEQPACKET`**: fornisce una connessione orientata ai pacchetti, simile a `SOCK_STREAM` ma con messaggi di lunghezza fissa. Garantisce la consegna dei pacchetti e mantiene l'ordine.

## 1.4 - Orientamento alla connessione

L'**orientamento alla connessione** si riferisce al modo in cui le applicazioni comunicano tra loro attraverso una rete, specificando se una connessione deve essere stabilita e mantenuta prima del trasferimento dei dati. Questa modalità è particolarmente importante nel contesto dei socket e dei protocolli di comunicazione. Esistono due modalità di orientamento alla connessione: [connection-oriented](Socket.md#1.4.1%20-%20Connection-oriented%20(orientato%20alla%20connessione)) e [connectionless](Socket.md#1.4.2%20-%20Connectionless%20(senza%20connessione)).

### 1.4.1 - Connection-oriented (orientato alla connessione)

In un sistema **connection-oriented (orientato alla connessione)**, è necessario stabilire una connessione affidabile tra due dispositivi (come client e server) prima che avvenga qualsiasi scambio di dati. Questo processo assicura che i dati vengano trasmessi in modo ordinato e senza perdite. Il protocollo più comune associato a questa modalità è il TCP (Transmission Control Protocol)%%link%% che garantisce che i pacchetti di dati arrivino nella sequenza corretta e senza errori.

Le principali caratteristiche dei sistemi connection-oriented sono:
- **Handshake iniziale**: prima di iniziare a inviare dati, il TCP%%link%% esegue un processo di handshake a tre vie per stabilire la connessione. Durante questo processo, il client e il server scambiano messaggi per confermare che sono pronti a comunicare.
- **Affidabilità**: il TCP%%link%% include meccanismi per garantire la consegna dei pacchetti, il controllo degli errori e la correzione degli errori. Se un pacchetto viene perso, il TCP si assicura che venga ritrasmesso.
- **Flusso di dati**: garantisce che i dati vengano inviati e ricevuti in un ordine preciso. Questa caratteristica è fondamentale per applicazioni come il trasferimento di file o le comunicazioni web, in cui la trasmissione dei dati in ordine casuale potrebbe creare problemi.

Esempi di utilizzo dei sistemi connection-oriented sono:
- **Web Browsing**: quando un browser si connette a un server web, stabilisce una connessione TCP%%link%% per garantire che tutte le informazioni vengano ricevute correttamente e nell'ordine giusto.
- **Email**: i protocolli come SMTP%%link%% (per inviare email) e POP3/IMAP%%link%% (per ricevere email) utilizzano connessioni TCP%%link%%.

### 1.4.2 - Connectionless (senza connessione)

In un sistema **connectionless (senza connessione)**, i dati possono essere inviati senza stabilire una connessione permanente. Non è necessario alcun processo di handshake iniziale e i pacchetti possono viaggiare indipendentemente. Il protocollo più comune associato a questa modalità è l'UDP (User Datagram Protocol)%%link%% che non garantisce che i pacchetti vengano consegnati o che arrivino nell'ordine corretto.

Le principali caratteristiche dei sistemi connectionless sono:
- **Nessun handshake**: l'UDP%%link%% non richiede un processo di stabilimento della connessione, il che rende il trasferimento di dati più veloce.
- **Meno overhead**: non ci sono controlli di errore e riconoscimenti, il che riduce l'overhead e aumenta la velocità di trasmissione.
- **Inaffidabilità**: non c'è garanzia che i dati arrivino o che vengano ricevuti nell'ordine corretto. Questo può essere accettabile per alcune applicazioni, come streaming audio o video, dove la velocità è più importante della completezza.

Esempi di utilizzo dei sistemi connectionless sono:
- **Streaming**: i servizi di streaming video e audio utilizzano l'UDP%%link%% per trasmettere dati in tempo reale, dove è più importante ricevere i dati rapidamente piuttosto che garantirne l'integrità%%esempio dirette quando mancano qualche pixel o frame%%.
- **Giochi online**: molti giochi online usano l'UDP%%link%% per inviare rapidamente aggiornamenti di stato ai giocatori senza l'onere di garantire l'affidabilità.

### 1.4.3 - Tabella riassuntiva delle differenze

Ecco una tabella riassuntiva che confronta la modalità [connection-oriented](Socket.md#1.4.1%20-%20Connection-oriented%20(orientato%20alla%20connessione)) e la modalità [connectionless](Socket.md#1.4.2%20-%20Connectionless%20(senza%20connessione)):

| Caratteristica                     | [Connection-oriented (orientato alla connessione)](Socket.md#1.4.1%20-%20Connection-oriented%20(orientato%20alla%20connessione)) | [Connectionless (senza connessione)](Socket.md#1.4.2%20-%20Connectionless%20(senza%20connessione)) |
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

# 2 - Vantaggi e svantaggi dei socket

I principali vantaggi dei socket sono:
- **Flessibilità**: permettono una varietà di protocolli di trasporto%%link%% (TCP%%link%%/UDP%%link%%) e [orientamento alla connessione](Socket.md#1.4%20-%20Orientamento%20alla%20connessione) ([connection-oriented](Socket.md#1.4.1%20-%20Connection-oriented%20(orientato%20alla%20connessione))/[connectionless](Socket.md#1.4.2%20-%20Connectionless%20(senza%20connessione))), adattandosi a diverse esigenze di comunicazione.
- **Efficienza nella comunicazione**: offrono un metodo standard per lo scambio di dati tra dispositivi, consentendo connessioni rapide tra applicazioni su macchine differenti.
- **Compatibilità cross-platform**: le API dei socket sono disponibili e relativamente simili su molti sistemi operativi, facilitando lo sviluppo di applicazioni distribuite.
- **Affidabilità con il TCP**: con il TCP%%link%%, i socket garantiscono che i dati arrivino in modo sicuro, ordinato e senza perdite. È quindi ideale per applicazioni critiche come web server, trasferimento di file e posta elettronica.
- **Supporto alla comunicazione in tempo reale con l'UDP**: con l'UDP%%link%%, i socket permettono una comunicazione veloce, poiché non hanno overhead di connessione, rendendoli ideali per streaming, giochi online, e applicazioni dove la velocità è più importante della precisione.
- **Multithreading e scalabilità**: i socket possono essere gestiti in modo asincrono o su più [thread](Thread.md), permettendo a un singolo server di gestire più connessioni contemporaneamente, aumentando così la scalabilità dell'applicazione.

I principali svantaggi dei socket sono:
- **Complessità di gestione**: richiedono una gestione accurata dei processi di connessione e chiusura, con il rischio di problemi come il blocco dei socket, connessioni non terminate correttamente, o errori di timeout.
- **Overhead con il TCP**: le connessioni che usano il TCP%%link%% implicano un certo overhead per il controllo di errori e la garanzia di consegna, aumentando la latenza. Non è ideale per applicazioni che richiedono un trasferimento estremamente rapido di piccoli pacchetti di dati.
- **Limitata sicurezza intrinseca**: di per sé, i socket non offrono cifratura o autenticazione dei dati. Per garantire sicurezza, è necessario implementare soluzioni aggiuntive come TLS/SSL%%link%%.
- **Vulnerabilità a attacchi**: i socket sono esposti ad attacchi come DDoS (Distributed Denial of Service) e hijacking, in cui malintenzionati possono sfruttare le connessioni aperte.
- **Supporto limitato per la trasmissione multicast**: sebbene l'UDP%%link%% supporti il multicast, cioè l'invio di dati a più destinatari, i socket TCP%%link%% non lo fanno nativamente, limitando la comunicazione a un solo client per connessione.
- **Problemi di firewall e NAT**: i firewall e i router NAT possono bloccare o ostacolare la connessione dei socket, causando problemi di accesso e richiedendo configurazioni aggiuntive.

# 3 - Internet socket

Gli **Internet socket** sono una [famiglia di socket](Socket.md#1.2%20-%20Famiglie%20di%20socket) utilizzati per la comunicazione su reti basate su IP, come Internet. Questi socket possono essere utilizzati per stabilire connessioni tra dispositivi che si trovano anche in posizioni geografiche diverse.

Gli internet socket hanno le seguenti principali caratteristiche:
- **Indirizzamento**: ogni socket è identificato univocamente da un indirizzo IP%%link%% e da una porta%%link%%, che consentono ai dispositivi di indirizzare correttamente i dati.
- **Protocollo**: i socket utilizzano protocolli di trasporto che determinano come vengono trasferiti i dati. I due protocolli più usati sono il TCP (Transmission Control Protocol)%%link%%, che crea una connessione stabile e affidabile e garantisce la consegna dei dati in modo ordinato e senza perdite, e l'UDP (User Datagram Protocol)%%link%%, che crea una connessione più leggera e veloce, ma non garantisce affidabilità, sequenzialità o controllo della perdita di pacchetti.

## 3.1 - Funzionamento degli internet socket

Il funzionamento base di un socket è il seguente:
1. **Creazione di un socket**: un'applicazione crea un socket, specificando il tipo di protocollo%%link%% (come TCP%%link%% o UDP%%link%%) e altre opzioni (ad esempio, indirizzo IP%%link%% e porta%%link%%). Nei sistemi basati su UNIX, questo avviene tipicamente con la funzione `socket()`, che restituisce un identificatore%%ID?%% del socket.
2. **Associazione (binding)**: nel caso di un server, il socket viene "associato" a un indirizzo IP%%link%% e una porta%%link%% con l'operazione di binding. Questo assicura che il socket ascolti su uno specifico indirizzo e sia accessibile per le connessioni in entrata. Ad esempio, in un server web, il socket è spesso associato alla porta 80 (HTTP%%link%%) o 443 (HTTPS%%link%%). %%Perché proprio questi due numeri specifici di porta?%%
3. **Modalità d'ascolto e connessione**: server e client svolgono funzioni diverse.
	- **Server**: il socket entra in modalità d'ascolto con la funzione `listen()`, in attesa di connessioni in entrata. Quando un client tenta di connettersi, il server accetta la connessione con la funzione `accept()`, che restituisce un nuovo socket per gestire la comunicazione con il client.
	- **Client**: il client richiede una connessione con il server attraverso il socket e la funzione `connect()`, specificando l'indirizzo IP%%link%% e la porta%%link%% del server.
4. **Trasferimento dei dati**: una volta stabilita la connessione, il client e il server possono scambiarsi dati. I dati sono inviati e ricevuti (in pacchetti) tramite funzioni di lettura e scrittura, come `send()` e `recv()` in TCP%%link%%, che garantiscono la consegna, oppure `sendto()` e `recvfrom()` in UDP%%link%%, dove non è garantita.
5. **Chiusura della connessione**: al termine della comunicazione, il socket viene chiuso. Nel TCP%%link%%, entrambe le parti devono chiudere il socket per terminare la connessione (half-close), garantendo che non ci siano dati persi. Nell'UDP%%link%%, che è senza connessione, la chiusura non ha bisogno di un processo specifico.

# Fonti

- Abraham Silberschatz, Peter Baer Galvin, Greg Gagne - [Sistemi Operativi (10ᵃ Edizione)](https://he.pearson.it/catalogo/1099) - Pearson, 2019 - ISBN: `9788891904560`.
- Slide del Prof. Aldinucci Marco del corso di Sistemi Operativi (canale B), Corso di Laurea in Informatica presso l'Università di Torino, A.A. 2024-25:
	- [Cap_03](https://informatica.i-learn.unito.it/mod/resource/view.php?id=253884)
