In UNIX, i **permessi** definiscono chi può leggere, scrivere o eseguire un file o una directory. Una delle caratteristiche distintive di UNIX, infatti, è che è stato progettato sin dai suoi primi giorni per essere un sistema multiutente, quindi deve utilizzare meccanismi che permettano agli utenti di gestire i propri file senza avere accesso ai file di altri utenti.

I permessi di un file o di una directory si possono configurare su tre distinte categorie di utenti:
- **Proprietario** (in inglese **_owner_**): l'utente che possiede il file.
- **Gruppo** (in inglese **_group_**): gli utenti appartenenti allo stesso gruppo a cui appartiene il file.
- **Altri** (in inglese **_others_**): tutti gli altri utenti che non rientrano nelle due categorie precedenti.

# Tipi di permessi

I tre tipi di permessi che si possono assegnare a un file o una directory sono:
- **Lettura**: permette di leggere il contenuto del file o, per una directory, di elencarne i contenuti.
- **Scrittura**: consente di modificare il file o, per una directory, aggiungere/eliminare file.
- **Esecuzione**: permette di eseguire un file o accedere a una directory.

## Rappresentazione dei permessi

All'interno di UNIX, ognuno dei tre tipi di permessi è rappresentato da una singola lettera dell'alfabeto:
- **Lettura**: rappresentato con la `r` (da _**r**ead_);
- **Scrittura**: rappresentato con la `w` (da _**w**rite_);
- **Esecuzione**: rappresentato con la `x` (da _e**x**ecute_).

Questi caratteri sono usati per rappresentare l'insieme dei permessi di un file o di una directory attraverso un'unica stringa di 10 caratteri, suddivisa nei seguenti 4 blocchi:
$$
\color{Red}{X}\color{Orange}{XXX}\color{Green}{XXX}\color{Blue}{XXX}
$$
- $\color{Red}{X}$: indica il tipo di file:
	- **`-`**: file normale.
    - **`d`**: directory.
    - **`l`**: link simbolico.
- $\color{Orange}{XXX}$: permessi per il proprietario (_owner_);
- $\color{Green}{XXX}$: permessi per il gruppo (_group_);
- $\color{Blue}{XXX}$: permessi per gli altri (_others_).

In particolare, nelle triple di caratteri $XXX$ che identificano i permessi di _owner_, _group_ e _others_:
- Il primo carattere rappresenta il permesso di **lettura** (`r` se il permesso è abilitato, `-` altrimenti);
- Il secondo carattere rappresenta il permesso di **scrittura** (`w` se il permesso è abilitato, `-` altrimenti);
- Il terzo carattere rappresenta il permesso di **esecuzione** (`x` se il permesso è abilitato, `-` altrimenti).

> [!esempio] Esempio
> 
> Si consideri la seguente stringa.
>
> ```
> drwxr-xr--
> ```
> 
> Si può dedurre che:
> - Si tratta di una cartella, in quanto il primo carattere è una `d`;
> - I permessi del proprietario sono `rwx`, quindi il proprietario ha permesso di lettura, scrittura ed esecuzione;
> - I permessi del gruppo sono `r-x`, quindi i componenti del gruppo possono leggere e aprire la cartella;
> - I permessi degli altri sono `r--`, quindi hanno solo il permesso di lettura.

%%
### Modifica dei permessi:

1. **Comando `chmod`**:
    
    - Modalità simbolica:
        
        ```bash
        chmod u+rwx,g+rx,o+r file.txt
        ```
        
        (aggiunge permessi al proprietario, gruppo e altri).
    - Modalità numerica (ottale):
        
        ```bash
        chmod 755 file.txt
        ```
        
        Dove:
        - `7` = lettura (4) + scrittura (2) + esecuzione (1).
        - `5` = lettura (4) + esecuzione (1).
2. **Modifica della proprietà**:
    
    - Proprietario: `chown utente file.txt`
    - Gruppo: `chgrp gruppo file.txt`

Conoscere e gestire i permessi è cruciale per la sicurezza e l'organizzazione dei file in un sistema Unix.

- Generally, the files that the user owns are ones that he created, or which were created as a result of some action on his part.
	- The exception to this, of course, is the superuser, also known as root.
	- The superuser can change the ownership of any file, whether he created it or not, with the chown command. For example, if the superuser gives the command
		```
		chown jane /home/bill/billsfile
		```
- la proprietà del file `/home/bill/billsfile` viene trasferita all'utente `jane`.
%%

%%
# Proprietà dei file

La **proprietà dei file** è un meccanismo che definisce chi controlla un file o una directory, in modo da gestirne i permessi e, conseguentemente, chi può interagirci o meno. Ogni file ha tre livelli di proprietà:

```shell
chown jane /home/bill/billsfile  
```

L'account root%\%link%\% può cambiare la proprietà di qualsiasi file con il comando `chown`, indipendentemente da chi sia il proprietario originale.

Generalmente, i file che un utente possiede sono quelli che ha creato o che sono stati creati a seguito di un'azione da parte sua.
- L'eccezione a questa regola è il superutente, noto anche come root.
- Il superutente può modificare la proprietà di qualsiasi file, indipendentemente dal fatto che l'abbia creato o meno, utilizzando il comando `chown`. Ad esempio, se il superutente esegue il comando:
%%

%%
### File Permissions

- As the owner of a file, a user has a right to decide who can access a file, and what kind of access others can have.
- There are three kinds of file permission:
	- Read (file can be viewed)
	- Write (file can be edited)
	- Execute (file can be run as a program)
- there are three categories of users to whom these permissions can be applied:
	- User (owner of that particular file)
	- Group (group to which the file is assigned)
	- All (all users and groups)
- When you define permissions for a given file, you must assign a type of permission to each category (u,g,o) of users.
	- If you are writing a program, you probably want to give yourself read, write, and execute permission.
	- If you are working with a team, you might want to have your system administrator create a group for the team.
		- You can then give the team read and execute permissions so they can test your program and make suggestions but not be able to edit the file.

How to Read a Permissions List
- use the `ls -l` command, and the permission information is printed as part of a directory listing.
- from left to right, the columns show file permissions, UID, username, group name, file size, timestamp, and filename
- The string of characters on the left displays all the permission information for each file.
- The permission information consists of nine characters, beginning with the second character from the left.
- The first three characters represent the permission for the user, the second three for the group, and the final set of three represents permission for all.

| Permission      | Applied to a Directory                                                         | Applied to Any Other Type of File                                                                                                        |
| --------------- | ------------------------------------------------------------------------------ | ---------------------------------------------------------------------------------------------------------------------------------------- |
| **read (r)**    | Grants the capability to read the contents of the directory or subdirectories. | Grants the capability to view the file.                                                                                                  |
| **write (w)**   | Grants the capability to create, modify, or remove files or subdirectories.    | Grants write permissions, allowing an authorized entity to modify the file, such as by adding text to a text file, or deleting the file. |
| **execute (x)** | Grants the capability to enter the directory.                                  | Allows the user to "run" the program.                                                                                                    |
| **-**           | No permission.                                                                 | No permission.                                                                                                                           |

Esempio: `-rwxr-xr--`

| Characters                | Apply to                                      | Definition                                                                                                                                                                                                                                     |
| ------------------------- | --------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **rwx** (characters 2–4)  | The owner (known as user in Unix) of the file | The **owner** of the file has read (or view), write, and execute permission to the file.                                                                                                                                                       |
| **r-x** (characters 5–7)  | The group to which the file belongs           | The users in the **owning group** (users) can read the file and execute the file if it has executable components (commands, and so forth). The group does not have write permission: the "-" character fills the space of a denied permission. |
| **r--** (characters 8–10) | Everyone else (others)                        | **Anyone else** with a valid login to the system can only read the file: write and execute permissions are denied (--).                                                                                                                        |
%%

%%
### Changing permissions

- To change file or directory permissions, you use the chmod (change mode) command. There are two ways to use chmod: symbolic mode and absolute mode.
- In symbolic mode, + (or -) adds (pr removes) the designated permission(s) to a file or directory. es:
	```
	chmod o+wx myfile
	```
	Adds write and execute permissions for others
- In Absolute mode
	```
	chmod 754 myfile
	```
viene convertito in
```
111 101 100
rwx rwx rwx
 7   5   4
```
%%

# Fonti

- Slide del Prof. Schifanella Claudio del corso di Laboratorio di Sistemi Operativi (canale B, turno T4), Corso di Laurea in Informatica presso l'Università di Torino, A.A. 2024-25:
	- [Slide: introduzione al corso e introduzione a UNIX](https://informatica.i-learn.unito.it/pluginfile.php/422768/mod_resource/content/2/01_introduzione_UNIX.pdf)
%%
Da vedere:
- https://1stoldsite.to.infn.it/groups/group4/mirror/linux/AppuntiLinux/AL-4.13.53.html
%%
