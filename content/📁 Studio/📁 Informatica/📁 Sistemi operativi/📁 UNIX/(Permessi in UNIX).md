---
draft: true
---
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

# Fonti

- Slide del Prof. Schifanella Claudio del corso di Laboratorio di Sistemi Operativi (canale B, turno T4), Corso di Laurea in Informatica presso l'Università di Torino, A.A. 2024-25:
	- [Slide: introduzione al corso e introduzione a UNIX](https://informatica.i-learn.unito.it/pluginfile.php/422768/mod_resource/content/2/01_introduzione_UNIX.pdf)
