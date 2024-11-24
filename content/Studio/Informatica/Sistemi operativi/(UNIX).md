---
draft: false
---
UNIX%% ([pronuncia]: `/ˈjuːnɪks/`)%% è un [sistema operativo](Sistemi%20operativi.md) sviluppato originariamente nei laboratori Bell di AT&T, una delle più grandi aziende di telecomunicazioni al mondo, tra gli anni '60 e '70. UNIX ha influenzato profondamente lo sviluppo di molti altri sistemi operativi, come Linux%%link%%, BSD%%link%% e macOS%%link%%. Le sue caratteristiche principali includono un design modulare, in cui ogni programma esegue una funzione specifica e può essere combinato con altri programmi tramite la riga di comando.

Oggi, molto più spesso, con il termine "UNIX" si fa riferimento non più al sistema operativo UNIX sviluppato da AT&T, ma a una famiglia di sistemi operativi certificati per essere conformi agli standard ufficiali POSIX (Portable Operating System Interface), stabiliti per mantenere una certa compatibilità con l'originale UNIX. Alcuni esempi di questi sistemi sono macOS%%link%% e AIX (di IBM).

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

# Principi di UNIX

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

# Standard POSIX

**POSIX** (**P**ortable **O**perating **S**ystem **I**nterface for UNI**X**) è una famiglia di standard definiti dall'IEEE (denominati formalmente _IEEE 1003_) per definire alcuni concetti base che vanno seguiti durante la realizzazione del sistema operativo e per mantenere la compatibilità tra di essi.

# Account

- A user account provides you with access to the Unix system, whether by a shell, an ftp account, or other means.
- To use the resources that the Unix system provides, you need a valid user account and resource permissions.
- There are three primary types of accounts on a Unix system:
	- the root user (or superuser) account,
	- system accounts, and
	- user accounts.
- Almost all accounts fall into one of those categories.

## Root

- The root account’s user has complete control of the system, to the point that he can run commands to completely destroy the system.
- The root user (also called root) can do absolutely anything on the system, with no restrictions on files that can be accessed, removed, and modified.
```
We trust you have received the usual lecture from the local System Administrator. It usually boils down to these three things:
#1) Respect the privacy of others.
#2) Think before you type.
#3) With great power comes great responsibility.
```
- The Unix methodology assumes that root users know what they want to do, so if they issue a command that will completely destroy the system, Unix allows it.
- This basic tenet is why people generally use root for only the most important tasks, and then use it only for the time required — and very cautiously.

## System accounts

- System accounts are those needed for the operation of system-specific components. They include, for example, the mail account (for electronic mail functions) and the sshd account (for ssh functionality).
	- They generally assist in the running of services or programs that the users require.
- some of them may not exist on your Unix system. These accounts are usually needed for some specific function on your system, and any modifications to them could adversely affect the system.
	- some of the system account names you may find in your /etc/passwd file are adm, alias, apache, backup, bin, bind, daemon, ftp, guest, gdm, gopher, mail, mysql, etc.

## User accounts

- User accounts provide interactive access to the system for users and groups of users.
- General users are typically assigned to these accounts and usually have limited access to critical system files and directories.
	- Generally you want to use eight characters or fewer in an account name, but this is no longer a requirement for all Unix systems.
	- For interoperability with other Unix systems and services, however, you will most likely want to restrict your account names to eight characters or fewer.

## Group accounts

- Group accounts add the capability to assemble other accounts into logical arrangements for simplification of privilege (permission) management
- Unix permissions are placed on files and directories and are granted in three subsets:
	- the owner of the file, also known as the user;
	- the group assigned to the file, also known simply as group; and
	- anyone who has a valid login to the system but does not fall into either the owner or group subsets, also known as others.
- The existence of a group enables a resource or file owner to grant access to files to a class of people.
- One of the strengths of groups is that an account can belong to many groups, based on access requirements.
	- For instance, the two members of the internal audit team may need to access everyone’s data, but their directory, called Audit, needs to be protected from everyone else’s account.
	- To do this, they can belong to all groups and still have a special audit group in which they are the only members.
### Example

- For example, say that a company with about 100 employees uses a central Unix server.
- Three of the employees compose the company’s human resources (HR) staff; they often deal with sensitive information, including salaries, pay raises, and disciplinary actions. The HR staff has to store its information on the server everyone else uses, but its directory, Human_Resources, needs to be protected so that others cannot view the contents.
- To enable HR to set specific permissions on its files that allow access only to HR staff, the three staff members are put into a group called hr. The permissions on the Human_Resources directory can then be set to allow those members to view and modify files, while excluding all who fall into the other group (everyone else).

## File Ownership and Permissions

### A multiuser system

- One of the distinguishing features of Unix is that it was designed from its earliest days to be a multiuser system.
- Because of its multiple-user design, Unix must use mechanisms that enable users to manage their own files without having access to the files of other users.
	- These mechanisms are called file ownership and file permissions.

### File ownership

- Generally, the files that the user owns are ones that he created, or which were created as a result of some action on his part.
	- The exception to this, of course, is the superuser, also known as root.
	- The superuser can change the ownership of any file, whether he created it or not, with the chown command. For example, if the superuser gives the command
		```
		chown jane /home/bill/billsfile
		```
	- the ownership of the file /home/bill/billsfile is transferred to the user jane.

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

# Commands

- Since its earliest days, Unix has primarily used a command-line interface: a simple prompt, followed by a cursor, using only text.
- In this kind of environment, there is only one mode of interacting with the machine, and that’s via commands.
- Commands are executable programs.
	- Sometimes they are stand-alone programs, and
	- sometimes they are functions that are built into the shell. In either case, a command enables the user to request some sort of behavior from the machine.

## Anatomy of a command

- A Unix command can be broken down into two parts: the command itself and the arguments appended to it.
	- For example, the `ls` command is used to list the contents of a directory. If you type ls at the command prompt, the contents of the working directory (that is, the directory in which you are currently located) is printed to the screen
- With the use of arguments, you can influence the behavior or output of the command.
	- An argument adds additional information that changes the way in which the command executes.
	- Arguments can influence the form of a command’s output as well as its operation.
		- the ls command would show the directory listing for /etc in long format, which provides additional information about the files being listed.
- Flags are usually —but not always— preceded by a dash, or hyphen.
	- The tar command, for example, takes its flags without a prepended dash.
- In addition to accepting multiple arguments at one time, some commands require multiple targets (e.g. cp).

## Man pages

- Unix manual pages (or man pages) are the best way to learn about any given command. Find a particular manual page with the command man command.

| Section | Description                                                      |
| ------- | ---------------------------------------------------------------- |
| 1       | General commands                                                 |
| 2       | System calls                                                     |
| 3       | Library functions, covering in particular the C standard library |

## Command Modification

- Unix commands are not limited to the functions performed when the command name is typed at the prompt.
- You can use a number of different tools to enhance or alter the function of a command, or to manage the command’s output.

## Metacharacters

- One of the more interesting aspects of using a command-line interface is the capability to use special characters called metacharacters to alter a command’s behavior.
- wildcards are special characters that can be used to match multiple files at the same time
	- `?` matches any one character in a filename.
	- `*` matches any character or characters in a filename.
	- `[ ]` matches one of the characters included inside the `[ ]` symbols.

### Metacharacters and ls command

• suppose that the working directory contains the files:
```
date help1 help2 help3 myprog.f myprog.o
```
• You can add wildcards to the target argument of the ls command to find any or all of these files in a single search.

| Argument + Wildcard | Files Matched                            |
| ------------------- | ---------------------------------------- |
| `help?`             | help1 help2 help3                        |
| `myprog.[fo]`       | myprog.f myprog.o                        |
| `*`                 | date help1 help2 help3 myprog.f myprog.o |
| `*.f`               | myprog.f                                 |
| `help*`             | help1 help2 help3                        |

# Input and Output Redirection

- To function, every command needs a source of input and a destination for output.
	- In the vast majority of cases, the standard input is the keyboard, and the standard output is the screen — specifically, the Terminal window, if you’re using a graphical interface.
- Redirection allows to force a particular command to take input from a source other than the keyboard, or to put the output somewhere besides the monitor.
	- For example, you might want to set up a program to run without having to be at the keys to invoke it, and then to dump its output into a text file
- Input and output redirection uses the < and > characters to define the temporary input and output sources.
	- Suppose that you want to use ls to find the contents of a directory, but you want the output captured in a text file rather than printing to the screen. To do so, create a file named ls_output and then issue the command:
	```
	$ ls > ls_output
	```
	- The > character takes the output of ls, which would normally go to the screen, and writes it to the ls_output file.
- If the specified file does not already exist, the > operator will create it.
- If the preceding command were executed twice, the second command would overwrite the contents of the ls_output file and destroy the previous data.
	- If you want to preserve existing data, use the >> operator, which appends the new data to the end of the file. If the specified file doesn’t exist, or is empty, >> acts just like >.
- In the same way that > redirects the output of a command, < can be used to change the input.
	- For example, assume that you want to alphabetize a list of terms contained in a file called terms. You can use the sort command in combination with the input redirection operator <, as in:
	```
	sort < terms
	```
- Input and output redirection can also be combined.
	- For example, the following command will sort the items in the terms file and then send the output of the sort into a new file called terms-alpha.
	```
	sort < terms > terms-alpha
	```

# Pipe

- A pipe is an operator that combines input and output redirection so that the output of one command is immediately used as the input for another. The pipe is represented by the vertical line character (|)
	- Suppose you want to list the contents of a long directory. A pipe gives you a simple way to display the output one page at a time, with the following command:
	```
	$ ls -l /etc | more
	```

# Navigating the File System

| Command | Description                                                          |
| ------- | -------------------------------------------------------------------- |
| `cat`   | Concatenate: displays a file.                                        |
| `cd`    | Change directory: moves you to the directory identified.             |
| `cp`    | Copy: copies one file/directory to specified location.               |
| `file`  | Identifies the file type (binary, text, etc).                        |
| `find`  | Finds a file/directory.                                              |
| `head`  | Shows the beginning of a file.                                       |
| `less`  | Browses through a file from end or beginning.                        |
| `ls`    | List: shows the contents of the directory specified.                 |
| `mkdir` | Make directory: creates the specified directory.                     |
| `more`  | Browses through a file from beginning to end.                        |
| `mv`    | Move: moves the location of or renames a file/directory.             |
| `pwd`   | Print working directory: shows the current directory the user is in. |
| `rm`    | Remove: removes a file.                                              |
| `tail`  | Shows the end of a file.                                             |
| `touch` | Creates a blank file or modifies an existing file’s attributes.      |
| `which` | Shows the location of a file if it is in your PATH.                  |

# ls

ls
• The most common Unix commands are those used to manage files and directories. The ls command takes the syntax:
```
ls [options] [directory]
```

| Argument | Function                                                                                                |
| -------- | ------------------------------------------------------------------------------------------------------- |
| `-l`     | Lists directory contents in long format, which shows individual file size, permissions, and other data. |
| `-t`     | Lists directory contents sorted by the timestamp (time of the last modification).                       |
| `-a`     | Lists all directory contents, including hidden files whose name begins with the `.` character.          |
| `-i`     | Lists directory contents including inode or disk index number.                                          |
| `-R`     | Lists directory contents including all subdirectories and their contents.                               |

# cd

The cd command is something that you will use frequently. It’s the command used to move through the
file system. It takes the syntax:
```
cd directory
cd .. // to move one level up on the hierarchy
cd // to move to the /home dir
```

# cat

- If you want to see the contents of a given file, there’s no easier way than the cat command, which prints the contents of a specified file to the standard output, usually the monitor. It takes the following syntax:
```
cat [options] file(s)
```
• -n Numbers the output’s lines;
• -v Shows all nonprinting characters
• to concatenate multiple files into one larger new file, cat file1 file2 file3 >> newfile

# more/less

- Virtually identical commands, used to break up command output or file contents into single-screen chunks so that you can read the contents more easily. Both more and less can move forward through a file, although only less can be used to move backward.
```
more filename
less filename
```
- Press the spacebar to advance to the next screen. If you are using less to view the output or file, you can use the B key to move back one screen. To return to the command prompt press Q in either more or less.

# mv

- The mv command is used to move a file from one location to another. It takes the syntax:
```
mv old new
```
- where old is the current name of the file to be moved to the location defined as new.
	- If the value of new is simply a new filename, the file is renamed and remains in the current directory.
	- If the value of new is a new directory location, the file is moved to the new location with the existing filename.
	- If the value of old is a directory, the entire directory and its contents will be moved to the location specified as new.

# cp

- Like the mv command, cp is used to create new files or move the content of files to another location. Unlike mv, however, cp leaves the original file intact at its original location. cp uses the syntax
```
cp file1 file2
```
- where file1 is the original file and file2 is the destination file.
- If you use the name of an existing file as the destination value, cp overwrites that file’s contents with the contents of file1.

# rm

• The rm command is used to delete a file. It uses the syntax:
```
rm [options] filename
```
• This command can be quite destructive unless you are careful when you issue it, especially if you use wildcards.
• For example, the command rm conf* deletes all files beginning with the characters conf, whether you wanted to delete those files or not.

-i Forces interactive mode, prompting you to confirm each deletion
-r Forces recursive mode, deleting all subdirectories and the files they contain
-f Forces force mode, ignoring all warnings (very dangerous)

# Fonti

- Slide del Prof. Schifanella Claudio del corso di Laboratorio di Sistemi Operativi (canale B, turno T4), Corso di Laurea in Informatica presso l'Università di Torino, A.A. 2024-25:
	- [Slide: introduzione al corso e introduzione a UNIX](https://informatica.i-learn.unito.it/pluginfile.php/422768/mod_resource/content/2/01_introduzione_UNIX.pdf)