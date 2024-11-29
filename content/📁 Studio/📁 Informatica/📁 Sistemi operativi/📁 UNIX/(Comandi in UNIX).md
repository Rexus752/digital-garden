---
draft: true
---
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
