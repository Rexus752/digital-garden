---
icon: RiProhibited2Line
iconColor: "#FF8888"
---
Nei sistemi [UNIX](UNIX.md), i **permessi** sono un meccanismo che permettono di definire chi può leggere, scrivere o eseguire un file o una directory. Una delle caratteristiche distintive di UNIX, infatti, è che è stato progettato sin dai suoi primi giorni per essere un sistema multiutente, quindi deve utilizzare meccanismi che permettano agli utenti di gestire i propri file senza avere accesso ai file di altri utenti.

I permessi di un file o di una directory si possono configurare su tre distinte categorie di utenti:
- **Proprietario** (in inglese **_owner_**): l'utente che possiede il file.
- **Gruppo** (in inglese **_group_**): gli utenti appartenenti allo stesso gruppo a cui appartiene il file.
- **Altri** (in inglese **_others_**): tutti gli altri utenti che non rientrano nelle due categorie precedenti.

# 1 - Tipi di permessi

I tre tipi di permessi che si possono assegnare a un file o una directory sono:
- **Lettura**: permette di leggere il contenuto del file o, per una directory, di elencarne i contenuti.
- **Scrittura**: consente di modificare il file o, per una directory, aggiungere/eliminare file.
- **Esecuzione**: permette di eseguire un file o accedere a una directory.

# 2 - Rappresentazione dei permessi

All'interno di UNIX, ognuno dei tre tipi di permessi è rappresentato da una singola lettera dell'alfabeto:
- **Lettura**: rappresentato con la `r` (da _**r**ead_).
- **Scrittura**: rappresentato con la `w` (da _**w**rite_).
- **Esecuzione**: rappresentato con la `x` (da _e**x**ecute_).

Questi caratteri sono usati per rappresentare l'insieme dei permessi di un file o di una directory attraverso un'unica stringa di 10 caratteri, suddivisa nei seguenti 4 blocchi:
$$
\color{Red}{X}\color{Orange}{XXX}\color{Green}{XXX}\color{Blue}{XXX}
$$
dove:
- $\color{Red}{X}$: indica il tipo di file:
	- **`-`**: file normale.
    - **`d`**: directory.
    - **`l`**: link simbolico.
- $\color{Orange}{XXX}$: permessi per il proprietario (detto _owner_).
- $\color{Green}{XXX}$: permessi per il gruppo (detto _group_).
- $\color{Blue}{XXX}$: permessi per gli altri (detti _others_).

In particolare, nelle triple di caratteri $XXX$ che identificano i permessi di _owner_, _group_ e _others_:
- Il primo carattere rappresenta il permesso di **lettura** (`r` se il permesso è abilitato, `-` altrimenti).
- Il secondo carattere rappresenta il permesso di **scrittura** (`w` se il permesso è abilitato, `-` altrimenti).
- Il terzo carattere rappresenta il permesso di **esecuzione** (`x` se il permesso è abilitato, `-` altrimenti).

> [!esempio] Esempio
> Un esempio di rappresentazione dei permessi di una directory è il seguente:
> ```
> drwxr-xr--
> ```
> dove:
> - **`d`**: indica che si tratta di una directory.
> - **`rwx`**: indica i permessi del proprietario, quindi il proprietario ha permesso di lettura, scrittura ed esecuzione.
> - **`r-x`**: indica i permessi del gruppo, quindi i componenti del gruppo possono leggere e aprire la cartella, ma non modificarla, perché il permesso di scrittura è disabilitato con il `-`.
> - **`r--`**: indica i permessi degli altri, quindi gli altri hanno solamente il permesso di lettura.

# 3 - Modifica dei permessi

In UNIX, la **modifica dei permessi** dei file e delle directory può essere effettuata utilizzando i seguenti comandi:
- [**`chmod`**](Permessi%20in%20UNIX.md#3.1%20-%20Comando%20`chmod`): consente di modificare i permessi del file o della directory.
- [**`chown`**](Permessi%20in%20UNIX.md#3.2%20-%20Comando%20`chown`): consente di modificare il proprietario del file o della directory.
- [**`chgrp`**](Permessi%20in%20UNIX.md#3.3%20-%20Comando%20`chgrp`): consente di modificare il gruppo di appartenenza del file o della directory.

L'uso di questi comandi è riservato solamente:
- All'**account root**%%link%%, che può modificare i permessi, il proprietario e il gruppo di qualsiasi file o directory senza restrizioni (o, allo stesso modo, un utente con privilegi speciali%%link%%).
- Al **proprietario** del file o della directory, che può solamente utilizzare il comando `chmod`.
Quindi, un utente comune non può modificare i permessi, ma solamente utilizzare i file o le directory secondo quelli già stabiliti.

## 3.1 - Comando `chmod`

Il **comando `chmod`** (dall'inglese _**ch**ange **mod**e_) modifica i permessi di lettura, scrittura ed esecuzione di _owner_, _group_ e _others_. La sintassi del comando è la seguente:
```shell
chmod <modalità> <file/directory>
```
dove:
- **`<modalità>`**: rappresentazione dei nuovi permessi da applicare al file o alla directory attraverso la [modalità simbolica](Permessi%20in%20UNIX.md#3.1.1%20-%20Modalità%20simbolica) o la [modalità numerica](Permessi%20in%20UNIX.md#3.1.2%20-%20Modalità%20numerica).
- **`<file/directory>`**: il percorso al file o alla directory a cui applicare i nuovi permessi.

### 3.1.1 - Modalità simbolica

Nella **modalità simbolica**, per rappresentare i permessi si usano lettere e simboli:
- **`u`**: per indicare il proprietario del file o della directory (da _**u**ser_).
- **`g`**: per indicare il gruppo a cui appartiene il file o la directory (da _**g**roup_).
- **`o`**: per indicare gli altri (da _**o**thers_).
- **`a`**: per indicare i permessi di tutte e tre le categorie contemporaneamente (da _**a**ll_).
- **`+`**: per aggiungere nuovi permessi oltre a quelli già esistenti.
- **`-`**: per rimuovere dei permessi già esistenti.
- **`=`**: per reimpostare nuovi permessi (sovrascrivendo quelli precedenti).

> [!esempio] Esempio
> 
> Si consideri il seguente comando.
>
> ```shell
> chmod u+w, g=rx, o-r file.txt
> ```
> 
> Si può dedurre che:
> - **`u+w`**: viene aggiunto (`+`) il permesso di scrittura (`w`) all'utente proprietario del file (`u`);
> - **`g=rx`**: vengono reimpostati (`=`) solamente i permessi di lettura (`r`) e di esecuzione (`x`) del file per il gruppo (`g`);
> - **`o-r`**: viene rimosso (`-`) il permesso di lettura (`r`) al file per gli altri (`o`). 

### 3.1.2 - Modalità numerica

Nella **modalità numerica**, per rappresentare i permessi si usano triple di cifre ottali (quindi da `0` a `7`) per rappresentare rispettivamente i permessi di _owner_, _group_ e _others_. Le cifre ottali vengono rappresentate in binario ognuna da tre bit:
$$
\color{Red}{X}\color{Green}{X}\color{Blue}{X}
$$
dove:
- $\color{Red}{X}$: permesso di lettura (`1` se abilitato, `0` altrimenti).
- $\color{Green}{X}$: permesso di scrittura (`1` se abilitato, `0` altrimenti).
- $\color{Blue}{X}$: permesso di esecuzione (`1` se abilitato, `0` altrimenti).
Questa combinazione di tre bit viene convertita in decimale (ecco perché può assumere valori da $0_{10}=000_{2}$ a $7_{10}=111_{2}$) e rappresenta i permessi della singola categoria di ogni gruppo

> [!esempio] Esempio
> 
> Si consideri il seguente comando.
>
> ```shell
> chmod 752 file.txt
> ```
> 
> Si può dedurre che:
> - **`7`** (in binario ${\color{Red}1}{\color{Green}1}{\color{Blue}1}_2$): per il proprietario saranno abilitati i permessi di scrittura ($\color{Red}1$), i permessi di lettura ($\color{Green}1$) e i permessi di esecuzione del file ($\color{Blue}1$).
> - **`5`** (in binario ${\color{Red}1}{\color{Green}0}{\color{Blue}1}_2$): per il gruppo saranno abilitati i permessi di scrittura ($\color{Red}1$) e i permessi di esecuzione del file ($\color{Blue}1$), ma non i permessi di lettura ($\color{Green}0$).
> - **`2`** (in binario ${\color{Red}0}{\color{Green}1}{\color{Blue}0}_2$): per gli altri saranno abilitati solamente i permessi di lettura ($\color{Green}1$).

## 3.2 - Comando `chown`

Il **comando `chown`** (dall'inglese _**ch**ange **own**er_) modifica l'utente proprietario di un file o di una directory. La sintassi del comando è la seguente:

```bash
chown <utente> <file/directory>
```

dove:
- **`<utente>`**: è il nome dell'utente che si vuole impostare come nuovo proprietario del file o della directory.
- **`<file/directory>`**: il percorso al file o alla directory a cui si vuole cambiare il proprietario.

Opzionalmente, si può anche cambiare contemporaneamente sia l'utente proprietario che il gruppo di appartenenza del file o della directory:
```shell
chown <utente>:<gruppo> <file/directory>
```

## 3.3 - Comando `chgrp`

Il **comando `chgrp`** (dall'inglese _**ch**ange **gr**ou**p**_) modifica il gruppo di appartenenza di un file o di una directory. La sintassi del comando è la seguente:

```shell
chgrp <gruppo> <file/directory>
```

dove:
- **`<gruppo>`**: è il nome del gruppo che si vuole impostare come nuovo gruppo di appartenenza del file o della directory.
- **`<file/directory>`**: il percorso al file o alla directory a cui si vuole cambiare il gruppo.

%%
### 5. **Permessi speciali**

- **Setuid (`s`):** Esegui il file come proprietario.
- **Setgid (`s`):** File eseguito con il gruppo proprietario o directory con ereditarietà dei permessi.
- **Sticky bit (`t`):** Solo il proprietario può eliminare file in una directory.

Esempio per sticky bit:

```bash
chmod +t /cartella
```
%%

# Fonti

- Slide del Prof. Schifanella Claudio del corso di Laboratorio di Sistemi Operativi (canale B, turno T4), Corso di Laurea in Informatica presso l'Università di Torino, A.A. 2024-25:
	- [Slide: introduzione al corso e introduzione a UNIX](https://informatica.i-learn.unito.it/pluginfile.php/422768/mod_resource/content/2/01_introduzione_UNIX.pdf)
%%
Da vedere:
- https://1stoldsite.to.infn.it/groups/group4/mirror/linux/AppuntiLinux/AL-4.13.53.html
%%
