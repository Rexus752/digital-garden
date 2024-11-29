---
draft: false
---
Nei sistemi [UNIX](UNIX.md), un **account** (in italiano _conto_) rappresenta un'entità (che sia un utente o un servizio) che può accedere al sistema operativo e utilizzarne le sue risorse a seconda dei permessi che gli vengono riservati.

# Caratteristiche degli account in UNIX

Ogni account in UNIX è identificato da:
- **Username**: il nome con cui l'account viene identificato in modo univoco e con il quale è possibile accedere al sistema.
- **Password**: una stringa segreta utilizzata per autenticare un utente al momento del login o per accedere a risorse protette.
- **User ID** (abbreviato in _UID_): un identificatore numerico univoco che rappresenta l'utente all'interno del sistema.
- **Group ID** (abbreviato in _GID_): uno o più identificatori numerici che identificano i gruppi a cui l'utente appartiene, cioè un insieme di permessi che condividono gli utenti al quale appartengono%%scrivere meglio%%.
	%%
	uno o più numeri ([GID](https://it.wikipedia.org/wiki/Group_identifier "Group identifier")) che identificano i gruppi di cui essa fa parte, di cui uno è detto _gruppo principale_ e gli altri sono detti _gruppi supplementari_.
	%%

%%
Solo gli account utente hanno:
- **Home directory**: una directory (cartella) del file system personale per l'utente che contiene i file personali e le configurazioni specifiche, situata di solito in `/home/<username>`. 
- **Shell**: il programma che interpreta i comandi dopo aver effettuato l'accesso.
- una data di scadenza (facoltativa) della password;
- una breve descrizione testuale (facoltativa) dell'utente;
- una quantità massima di spazio occupato nel [file system](https://it.wikipedia.org/wiki/File_system "File system") dai file dell'utente, detta _[quota](https://it.wikipedia.org/w/index.php?title=Quota_(informatica)&action=edit&redlink=1 "Quota (informatica) (la pagina non esiste)")_ (facoltativa).

L'assegnamento di tali informazioni deve essere effettuata dall'amministratore di sistema prima del primo utilizzo effettivo da parte dell'utenza. L'assegnamento di home directory e shell comporta anche la creazione automatica, nell'area dell'utente, di [file di preferenze](https://it.wikipedia.org/w/index.php?title=File_di_preferenze&action=edit&redlink=1 "File di preferenze (la pagina non esiste)") di default che l'utente può poi personalizzare.

A loro volta, ciascuna risorsa presente nei [file system](https://it.wikipedia.org/wiki/File_system "File system") ([file](https://it.wikipedia.org/wiki/File "File") semplici, [directory](https://it.wikipedia.org/wiki/Directory "Directory"), [dispositivi a blocchi](https://it.wikipedia.org/wiki/Dispositivo_a_blocchi "Dispositivo a blocchi"), [dispositivi a caratteri](https://it.wikipedia.org/wiki/Dispositivo_a_caratteri "Dispositivo a caratteri"), etc.) è associata ad uno _UID_ (che ne identifica il proprietario) e ad un _GID_ (che ne identifica il gruppo di appartenenza).

Ciascun [processo](https://it.wikipedia.org/wiki/Processo_(informatica) "Processo (informatica)") è associato:

- ad uno _UID_ principale, detto _real UID_, che ne identifica il proprietario e che inizialmente è quello associato all'utente che ha avviato il processo;
- ad uno _UID_ usato ai fini dei permessi, detto _effective UID_, che solitamente coincide col precedente, ma che può essere diverso in caso di programmi che usano il permesso [setuid](https://it.wikipedia.org/wiki/Setuid "Setuid");
- ad uno _UID_ detto _saved effective UID_, che è inizializzato con il valore dello _effective UID_ ma che in seguito può variare in caso di programmi che usano il permesso [setuid](https://it.wikipedia.org/wiki/Setuid "Setuid");
- ad una serie di _GID_, di cui uno è detto _principale_ e gli altri _supplementari_, che sono quelli associati all'utente che ha avviato il processo;
- ad un _GID_ detto _effective GID_, che solitamente coincide con il _GID_ principale associato al processo, ma che può essere diverso in caso di programmi che usano il permesso [setgid](https://it.wikipedia.org/wiki/Setgid "Setgid");
- ad un _GID_ detto _saved effective GID_, che inizialmente coincide con lo _effective GID_, ma che in seguito può cambiare in caso di programmi che usano il permesso [setgid](https://it.wikipedia.org/wiki/Setgid "Setgid");

Gli _UID_ ed i _GID_ assegnati agli utenti sono usati per inizializzare i vari _UID_ e _GID_ dei processi che essi avviano. Questi ultimi sono di volta in volta confrontati dal sistema con gli _UID_ e _GID_ assegnati ai file, unitamente ai loro [permessi](https://it.wikipedia.org/wiki/Permessi_(Unix) "Permessi (Unix)"), per implementare una stretta attività di controllo sui contenuti e operazioni. Questo insieme di informazioni costituisce il [profilo di sicurezza](https://it.wikipedia.org/wiki/Profilo_utente "Profilo utente") dell'utente.

Un utente molto particolare è quello associato allo _UID_ **0**, normalmente denominato con lo _username_ _`[root](https://it.wikipedia.org/wiki/Root_(utente) "Root (utente)")`_. L'utente root è l'amministratore del sistema e possiede un controllo pressoché totale di esso. Al contrario gli altri utenti possiedono funzionalità limitate secondo modalità e criteri complessi. Esistono infatti, utenti di sistema, associati generalmente a singole funzionalità di controllo della macchina ed utenti semplici, associati a vere e proprie account.

Nel maggior numero di sistemi Unix, le informazioni su nome utente, nome gruppo, password, etc., sono mantenuti nei file `/etc/[passwd](https://it.wikipedia.org/wiki/Passwd "Passwd")`, `/etc/[group](https://it.wikipedia.org/wiki/Group_(Unix) "Group (Unix)")` ed `/etc/[shadow](https://it.wikipedia.org/wiki/Shadow_(Unix) "Shadow (Unix)")`, ma possono anche essere mantenuti in un [server](https://it.wikipedia.org/wiki/Server "Server") [NIS+](https://it.wikipedia.org/wiki/Nisplus "Nisplus"), o in un [servizio di directory](https://it.wikipedia.org/wiki/Servizio_di_directory "Servizio di directory") accessibile via [LDAP](https://it.wikipedia.org/wiki/Lightweight_Directory_Access_Protocol "Lightweight Directory Access Protocol").
%%

I diversi username eventualmente attribuiti allo stesso UID sono considerati del tutto equivalenti dal sistema (costituiscono dei cosiddetti _alias_).

# Categorie degli account

Ogni account nei sistemi [UNIX](UNIX.md) rientra sempre in una delle seguenti tre categorie:
- **Account utente**: account creati per utenti che accedono al sistema per scopi generici, come lavorare su file personali, eseguire programmi o accedere a servizi.
- **Account root**: account con privilegi illimitati su tutto il sistema, con la possibilità di accedere, modificare e cancellare qualsiasi file e configurazione, oltre ad installare o rimuovere software. Ha solitamente UID `0`.
- **Account di sistema**: account speciali utilizzati dai servizi e dai processi del sistema operativo per svolgere compiti specifici, come eseguire applicazioni, demoni o servizi di rete. Non è destinato all'uso diretto da parte degli utenti umani.

| Tipo di Account    | Destinazione d'uso            | Privilegi                  | Interazione diretta?     |
| ------------------ | ----------------------------- | -------------------------- | ------------------------ |
| Account utente     | Attività quotidiane           | Limitati                   | Sì                       |
| Account root       | Amministrazione di sistema    | Illimitati                 | Sì, ma usato con cautela |
| Account di sistema | Servizi e processi di sistema | Limitati a scopo specifico | No                       |

## Account utente

Gli **account utente** sono account creati per utenti che accedono al sistema per scopi generici, come lavorare su file personali, eseguire programmi o accedere a servizi. Sono generalmente il tipo di account utilizzato da un utente generico di un sistema UNIX.

### Caratteristiche principali degli account utente

- **Privilegi limitati**: gli account utente hanno permessi ristretti, che impediscono loro di modificare file di sistema, installare software o gestire altri utenti. Possono accedere e modificare solo i file di cui sono proprietari, solitamente situati nella loro home directory.
- **Home directory personale**: una directory dedicata che funge da spazio privato per i suoi file e impostazioni personali. Il percorso tipico di una home directory: `/home/<username>` (per esempio, un utente chiamato `alice` avrà la sua home directory in `/home/alice`).
- **Shell interattiva**%%link%%: shell assegnata che consente di interagire con il sistema attraverso comandi. Shell comuni sono: `/bin/bash`, `/bin/zsh`, `/bin/sh`. La shell predefinita è definita al momento della creazione dell'account.%%sistemare questo%%
- **File di configurazione personalizzati**: ogni account utente può avere configurazioni personalizzate, salvate in file nascosti detti _dotfile_ (perché il loro nome comincia con un `.`) nella sua home directory. Esempi di dotfile sono i file `.bashrc` o `.zshrc` per configurare la shell, `.ssh/` per chiavi SSH personali o `.profile` per impostazioni di ambiente.

### Scelta dello username

Una buona norma è scegliere uno username per l'account utente con massimo otto caratteri.

Nonostante non sia più obbligatorio nei sistemi UNIX, è comunque consigliato rispettare questa convenzione per assicurare l'interoperabilità con altri sistemi e servizi UNIX.

## Account root

L'**account root** (noto anche come _**superutente**_, in inglese **_superuser_**) è l'account amministrativo del sistema, dotato di privilegi illimitati su tutto il sistema che gli forniscono l'accesso completo e il controllo su tutte le risorse e operazioni del sistema.

Avendo il controllo completo sul sistema, è in grado di eseguire comandi che possano anche distruggere il sistema stesso, senza alcun tipo di restrizioni. La filosofia di UNIX%%link%% presume che gli utenti che utilizzino gli account root sanno ciò che fanno, quindi se eseguono un comando che possa rendere il sistema inutilizzabile, UNIX glielo permette. Proprio per questo principio, generalmente si usa l'account root unicamente per i compiti più importanti e solamente per il tempo necessario.

### Caratteristiche principali dell'account root

- **Privilegi completi**: l'account root può accedere, modificare e eliminare qualsiasi file, incluse le risorse di sistema protette, bypassando tutte le restrizioni di sicurezza imposte agli account normali.
- **Identificazione univoca e fissa**: l'account root ha come username predefinito `root` e ha sempre l'UID `0` che lo identifica a livello di sistema.
- **Shell interattiva**%%link%%: come l'account utente, anche l'account root ha una shell assegnata che consente di interagire con il sistema attraverso comandi che, però, non saranno limitati da eventuali permessi negati.
- **Accesso indiretto tramite `sudo`**: per motivi di sicurezza, l'uso diretto dell'account root è scoraggiato e gli utenti autorizzati possono temporaneamente eseguire comandi con privilegi root utilizzando `sudo` (_**s**uper**u**ser **do**_), senza accedere direttamente all'account.

## Account di sistema

Gli **account di sistema** sono account speciali utilizzati dai servizi e dai processi del sistema operativo per svolgere compiti specifici, come eseguire applicazioni, demoni o servizi di rete. Non è destinato all'uso diretto da parte degli utenti umani.

%%
Alcuni dei nomi di account di sistema che si possono trovare nel file `/etc/passwd` sono `adm`, `alias`, `apache`, `backup`, `bin`, `bind`, `daemon`, `ftp`, `guest`, `gdm`, `gopher`, `mail`, `mysql`, ecc.

cambiare questa lista di account di sistema in una lista di account di sistema "comuni" con relativa descrizione. es:
Account di sistema comuni sono i seguenti:
- **`adm`**: bau bau miao miao
- **`alias`**: pipopopi
%%

### Caratteristiche principali degli account di sistema

- **Privilegi limitati al contesto**: ogni account di sistema ha permessi specifici per evitare che un servizio interferisca con un altro o con il sistema stesso.
- **UID riservato**: hanno UID compresi in un intervallo riservato, solitamente inferiore a 1000 (o 500 in alcuni sistemi più vecchi). In particolare, gli account di sistema con UID compreso tra 1 e 99 riguardano servizi critici, mentre quelli compresi tra 100 e 999 riguardano altri servizi.
- **Limitazioni di accesso**: spesso non hanno una shell%%link%% interattiva, per impedire l'accesso diretto (es. `/bin/false` o `/sbin/nologin` come shell predefinita), e non hanno una home directory%%link%% utilizzabile (o, se esiste, è limitata).

# Gruppi di account

I **gruppi di account** in [UNIX](UNIX.md) sono un meccanismo per gestire e organizzare gli account utenti, assegnando permessi e privilegi condivisi a un insieme di utenti. Ogni gruppo rappresenta una collezione logica di utenti e può essere utilizzato per semplificare la gestione delle autorizzazioni per file, directory o risorse del sistema.

Ogni gruppo è identificato da un nome descrittivo (es. `users`, `developers`, `www-data`) un Group ID (abbreviato in _GID_), cioè un numero univoco che identifica il gruppo a livello di sistema.

Ogni utente è associato automaticamente a un gruppo al momento della creazione, detto _gruppo primario_. In seguito, oltre a quello primario, si può aggiungere l'utente a uno o più _gruppi secondari_, per condividere permessi con altri gruppi.

> [!esempio] Esempio
> 
> Supponiamo che un'azienda con circa 100 dipendenti utilizzi un server centrale UNIX.
> 
> Tre di questi dipendenti fanno parte dello staff delle risorse umane (HR) dell'azienda: si occupano spesso di informazioni sensibili, come stipendi, aumenti di salario e provvedimenti disciplinari. Lo staff HR deve memorizzare le proprie informazioni sullo stesso server utilizzato da tutti, ma la loro directory, `human_resources`, deve essere protetta in modo che gli altri non possano visualizzarne il contenuto.
> 
> Per consentire al personale HR di impostare permessi specifici sui propri file, in modo che solo loro possano accedervi, i tre membri dello staff vengono inseriti in un gruppo chiamato `hr`. I permessi sulla directory `human_resources` possono quindi essere configurati per consentire solamente a quei membri di visualizzare e modificare i file, escludendo tutti gli altri dipendenti dell'azienda.

# Fonti

- Slide del Prof. Schifanella Claudio del corso di Laboratorio di Sistemi Operativi (canale B, turno T4), Corso di Laurea in Informatica presso l'Università di Torino, A.A. 2024-25:
	- [Slide: introduzione al corso e introduzione a UNIX](https://informatica.i-learn.unito.it/pluginfile.php/422768/mod_resource/content/2/01_introduzione_UNIX.pdf)
%%
Da vedere:
- https://en.wikipedia.org/wiki/Group_identifier
%%
