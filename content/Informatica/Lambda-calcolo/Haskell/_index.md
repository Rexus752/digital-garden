---
title: Haskell
---

> [!premessa]+ Premessa
> 
> Ciao! Se è la prima volta che capiti su questo sito, ti consiglio di consultare la [pagina principale](index.md) di questo cosiddetto _Giardino Digitale_ per scoprire meglio cos'è e come navigarlo.
> 
> Lo stato di questa nota è al momento: 🔴 <font color="#FF7F7F">_Bozza_</font>.

%%
prerequisiti:
- conoscenza minima di linguaggi di programmazione imperativi (es. C)
- linguaggi funzionali
%%

---

> [!definizione]+ Definizione: Haskell
> 
> **Haskell** è un linguaggio di programmazione%% link %% puramente funzionale%% link %% [lazy](Informatica/Lambda-calcolo/_index.md#^definizione-ordine-normale), general-purpose%% link %% e fortemente tipizzato%% link %%, creato%% da un apposito comitato alla fine degli anni ottanta%% principalmente per analizzare le caratteristiche dei linguaggi%% link %%. È stato chiamato così in onore del matematico e logico statunitense Haskell Curry%% link %%.
^definizione-haskell

%% 
In imperative languages you get things done by giving the computer a sequence of tasks and then it executes them. While executing them, it can change state. For instance, you set variable `a` to 5 and then do some stuff and then set it to something else. You have control flow structures for doing some action several times. In purely functional programming you don't tell the computer what to do as such but rather you tell it what stuff _is_. The factorial of a number is the product of all the numbers from 1 to that number, the sum of a list of numbers is the first number plus the sum of all the other numbers, and so on. You express that in the form of functions. You also can't set a variable to something and then set it to something else later. If you say that `a` is 5, you can't say it's something else later because you just said it was 5. What are you, some kind of liar? So in purely functional languages, a function has no side effects. The only thing a function can do is calculate something and return it as a result. At first, this seems kind of limiting but it actually has some very nice consequences: if a function is called twice with the same parameters, it's guaranteed to return the same result. That's called referential transparency and not only does it allow the compiler to reason about the program's behavior, but it also allows you to easily deduce (and even prove) that a function is correct and then build more complex functions by gluing simple functions together.

Haskell is **lazy**. That means that unless specifically told otherwise, Haskell won't execute functions and calculate things until it's really forced to show you a result. That goes well with referential transparency and it allows you to think of programs as a series of **transformations on data**. It also allows cool things such as infinite data structures. Say you have an immutable list of numbers `xs = [1,2,3,4,5,6,7,8]` and a function `doubleMe` which multiplies every element by 2 and then returns a new list. If we wanted to multiply our list by 8 in an imperative language and did `doubleMe(doubleMe(doubleMe(xs)))`, it would probably pass through the list once and make a copy and then return it. Then it would pass through the list another two times and return the result. In a lazy language, calling `doubleMe` on a list without forcing it to show you the result ends up in the program sort of telling you "Yeah yeah, I'll do it later!". But once you want to see the result, the first `doubleMe` tells the second one it wants the result, now! The second one says that to the third one and the third one reluctantly gives back a doubled 1, which is a 2. The second one receives that and gives back 4 to the first one. The first one sees that and tells you the first element is 8. So it only does one pass through the list and only when you really need it. That way when you want something from a lazy language you can just take some initial data and efficiently transform and mend it so it resembles what you want at the end.
%%

%% 
Haskell is **statically typed**. When you compile your program, the compiler knows which piece of code is a number, which is a string and so on. That means that a lot of possible errors are caught at compile time. If you try to add together a number and a string, the compiler will whine at you. Haskell uses a very good type system that has **type inference**. That means that you don't have to explicitly label every piece of code with a type because the type system can intelligently figure out a lot about it. If you say à = 5 + 4`, you don't have to tell Haskell that `a` is a number, it can figure that out by itself. Type inference also allows your code to be more general. If a function you make takes two parameters and adds them together and you don't explicitly state their type, the function will work on any two parameters that act like numbers.
%%

%% 
generalizzarlo ai linguaggi funzionali (come [!osservazione]):
Haskell is **elegant and concise**. Because it uses a lot of high level concepts, Haskell programs are usually shorter than their imperative equivalents. And shorter programs are easier to maintain than longer ones and have fewer bugs.
%% 

%%
Haskell was made by some **really smart folk** (with PhDs). Work on Haskell began in 1987 when a committee of researchers got together to design a kick-ass language. In 2003 the Haskell Report was published, which defines a stable version of the language.
%%

%% 
(inglese)  

«We wanted a language that could be used, among other purposes, for research into language features;»

(italiano)  
«Noi volevamo un linguaggio che potesse essere usato, oltre agli altri scopi, per studiare le caratteristiche del linguaggio;»

(A History of Haskell: Being Lazy With Class, Simon Peyton Jones, Paul Hudak, John Hughes, Philip Wadler)
%%

# 1 - Introduzione ad Haskell

## 1.1 - Installazione e compilatori

Per usare [Haskell](Informatica/Lambda-calcolo/Haskell/_index.md#^definizione-haskell), come ogni altro linguaggio di programmazione%% Link %%, c'è bisogno di un IDE%% link %% e di un compilatore%% Link %%. Uno dei compilatori%% link %% più diffusi per [Haskell](Informatica/Lambda-calcolo/Haskell/_index.md#^definizione-haskell) è il [_Glasgow Haskell Compiler (GHC)_](Informatica/Lambda-calcolo/Haskell/_index.md#^definizione-glasgow-haskell-compiler-ghc).

> [!definizione]+ Definizione: Glasgow Haskell Compiler (GHC)
> 
> Il **Glasgow Haskell Compiler (GHC)** è un compilatore%% link %% per il linguaggio di programmazione%% link %% [Haskell](Informatica/Lambda-calcolo/Haskell/_index.md#^definizione-haskell), chiamato così perché inizialmente sviluppato presso l'Università di Glasgow in Scozia.
> 
> Permette di compilare%% link %% file%% link %% di codice%% Link %% [Haskell](Informatica/Lambda-calcolo/Haskell/_index.md#^definizione-haskell) (solitamente con estensione%% link %% `.hs`), ma supporta anche una modalità interattiva%% link %% da terminale%% link %% tramite il [GHCi](Informatica/Lambda-calcolo/Haskell/_index.md#^definizione-ghci).
^definizione-glasgow-haskell-compiler-ghc

Puoi trovare [qui](https://downloads.haskell.org/ghc/latest/docs/users_guide/index.html) la documentazione%% link %% completa sul [GHC](Informatica/Lambda-calcolo/Haskell/_index.md#^definizione-glasgow-haskell-compiler-ghc).

> [!definizione]+ Definizione: GHCi
> 
> **GHCi** è l'interfaccia interattiva (REPL)%% link %% del [GHC](Informatica/Lambda-calcolo/Haskell/_index.md#^definizione-glasgow-haskell-compiler-ghc) che permette di eseguire espressioni%% Link %% [Haskell](Informatica/Lambda-calcolo/Haskell/_index.md#^definizione-haskell) direttamente da riga di comando%% Link %% senza dover compilare%% link %% un file sorgente%% link %%.
^definizione-ghci

Per imparare a usare [Haskell](Informatica/Lambda-calcolo/Haskell/_index.md#^definizione-haskell) è molto più facile e veloce usare il [GHCi](Informatica/Lambda-calcolo/Haskell/_index.md#^definizione-ghci) anziché compilare%% Link %% ed eseguire%% Link %% nuovamente il programma%% Link %% per ogni modifica che si fa. Il [GHCi](Informatica/Lambda-calcolo/Haskell/_index.md#^definizione-ghci) è accessibile da terminale%% link %% tramite il comando%% Link %% `ghci`.

> [!sintassi]+ Sintassi: uso del GHCi
> 
> All'interno del [GHCi](Informatica/Lambda-calcolo/Haskell/_index.md#^definizione-ghci) si possono chiamare%% link %% funzioni%% Link %% da file%% link %% [Haskell](Informatica/Lambda-calcolo/Haskell/_index.md#^definizione-haskell) che vengono _caricati_. Per _caricare_ un file%% link %% nel [GHCi](Informatica/Lambda-calcolo/Haskell/_index.md#^definizione-ghci), si usa il comando
> 
> ```haskell
> :l <file_name.hs>
> ```
> 
> Per esempio, per caricare un file%% link %% [Haskell](Informatica/Lambda-calcolo/Haskell/_index.md#^definizione-haskell) con nome `myfunctions.hs`, bisogna scrivere nel [GHCi](Informatica/Lambda-calcolo/Haskell/_index.md#^definizione-ghci) `:l myfunctions.hs`.
> 
> Se il file%% Link %% `myfunctions.hs` viene modificato, per aggiornare le modifiche anche nel [GHCi](Informatica/Lambda-calcolo/Haskell/_index.md#^definizione-ghci) basta nuovamente scrivere `:l myfunctions.hs`, oppure equivalentemente `:r` che ricarica tutti i file già caricati.
> 
> Per uscire dal [GHCi](Informatica/Lambda-calcolo/Haskell/_index.md#^definizione-ghci) e tornare al terminale%% link %% basta premere `Ctrl+D`.

---

%% 
https://downloads.haskell.org/ghc/latest/docs/users_guide/ghci.html
%%

> [!fonti]+ Fonti
> 
> - 🏫 Corso di Laurea in Informatica (`L-31 R`) presso l'Università di Torino:
>     - Corso di _Linguaggi e Paradigmi di Programmazione_, A.A. 2020-21 ([pagina Moodle](https://informatica.i-learn.unito.it/enrol/index.php?id=1987)):
> 		- Prof. Luca Padovani, [sezione del suo sito personale su Linguaggi e Paradigmi di Programmazione](https://boystrange.github.io/LPP/):
> 			- Introduzione:
> 				- [_Installazione_](https://boystrange.github.io/LPP/Installazione).
> - 📚 Miran Lipovača, _Learn You a Haskell for Great Good!_:
> 	- [1 - _Introduction_](https://learnyouahaskell.github.io/introduction.html).
