---
title: Sintassi di base di Haskell
---

> [!premessa]+ Premessa
> 
> Ciao! Se è la prima volta che capiti su questo sito, ti consiglio di consultare la [pagina principale](index.md) di questo cosiddetto _Giardino Digitale_ per scoprire meglio cos'è e come navigarlo.
> 
> Lo stato di questa nota è al momento: 🔴 <font color="#FF7F7F">_Bozza_</font>.

%% 
trasformare [!sintassi]+ in [!definizione]+ e [!osservazione]
%%

---

Ora proviamo a esplorare un po' la sintassi di base di [Haskell](Informatica/Lambda-calcolo/Haskell/_index.md#^definizione-haskell).

> [!sintassi]+ Sintassi: aritmetica di base in Haskell
> 
> In [Haskell](Informatica/Lambda-calcolo/Haskell/_index.md#^definizione-haskell), è valido usare i soliti operatori aritmetici%% Link %% `+`, `-`, `*`, `/` e parentesi per dare precedenze alle operazioni:
> 
> ```haskell
> ghci> 2 + 15
> 17
> ghci> 49 * 100
> 4900
> ghci> 1892 - 1472
> 420
> ghci> 5 / 2
> 2.5
> ghci> (50 * 100) - 4999
> 1
> ghci> 50 * 100 - 4999
> 1
> ghci> 50 * (100 - 4999)
> -244950
> ```
> 
> Se come secondo operando%% link %% c'è un numero negativo, bisogna racchiuderlo tra parentesi, altrimenti [GHC](Informatica/Lambda-calcolo/Haskell/_index.md#^definizione-glasgow-haskell-compiler-ghc) non capisce cosa vogliamo fare. Per esempio, la moltiplicazione%% Link %% tra `5` e `-3` si scrive `5 * (-3)` e non `5 * -3` perché in questo caso [GHC](Informatica/Lambda-calcolo/Haskell/_index.md#^definizione-glasgow-haskell-compiler-ghc) interpreta quel `-` non come segno negativo del `3` ma come una sottrazione%% link %%.
> 
> Anche l'algebra booleana%% link %% è, come al solito, utilizzabile tramite i valori di verità%% Link %% `True` e `False`, manipolabili attraverso le operazioni `&&`, `||` e `not`:
> 
> ```haskell
> ghci> True && False
> False
> ghci> True && True
> True
> ghci> False || True
> True
> ghci> not False
> True
> ghci> not (True && True)
> False
> ```
> 
> Il test per l'uguaglianza tra due oggetti è fatto per mezzo degli operatori `==` e `/=`. Valgono anche gli operatori di confronto `<`, `<=`, `>` e `>=`:
> 
> ```haskell
> ghci> 5 == 5
> True
> ghci> 1 == 0
> False
> ghci> 5 /= 5
> False
> ghci> 5 /= 4
> True
> ghci> "hello" == "hello"
> True
> ```

> [!attenzione]+ Attenzione: errori in Haskell
> 
> Se proviamo a eseguire del codice%% link %% [Haskell](Informatica/Lambda-calcolo/Haskell/_index.md#^definizione-haskell) non corretto dal punto di vista sintattico, [GHC](Informatica/Lambda-calcolo/Haskell/_index.md#^definizione-glasgow-haskell-compiler-ghc) terminerà il programma%% link %% con un errore. Per esempio, provando a sommare il numero `5` e la stringa%% link %% `"llama"`, otteniamo:
> 
> ```haskell
> ghci> 5 + "llama"
> <interactive>:4:1: error: [GHC-39999]
> • No instance for ‘Num String' arising from the literal ‘5'
> • In the first argument of ‘(+)', namely ‘5'
> In the expression: 5 + "llama"
> In an equation for ‘it': it = 5 + "llama"
> ```
> 
> Ciò accade perché la stringa%% link %% `"llama"` non è un numero e [GHC](Informatica/Lambda-calcolo/Haskell/_index.md#^definizione-glasgow-haskell-compiler-ghc) non sa come sommargli `5`. La stessa cosa accadrebbe anche se al posto di `"llama"` mettessimo `"four"` o `"4"` perché anche queste sono stringhe e non numeri (fai caso alle virgolette `"` attorno al numero!).
^attenzione-errori-in-haskell

> [!consiglio]+ Consiglio: codici identificativi degli errori in Haskell
> 
> Ogni errore in [Haskell](Informatica/Lambda-calcolo/Haskell/_index.md#^definizione-haskell) ha un _codice identificativo_ della forma `X-Y`, dove `X` è il programma in cui è avvenuto l'errore (es. [`GHC`](Informatica/Lambda-calcolo/Haskell/_index.md#^definizione-glasgow-haskell-compiler-ghc)) e `Y` indica il numero dell'errore.
> 
> Per esempio, l'[errore di prima](Informatica/Lambda-calcolo/Haskell/_index.md#^attenzione-errori-in-haskell) è rappresentato dal codice `GHC-39999`. Puoi approfondire il significato di ogni codice nell'[Haskell Error Index](https://errors.haskell.org/).

> [!sintassi]+ Sintassi: chiamata di funzioni in Haskell e notazioni
> 
> In [Haskell](Informatica/Lambda-calcolo/Haskell/_index.md#^definizione-haskell), ogni cosa è una funzione%% link %%. Per esempio, l'operatore%% link %% `*` è una funzione%% Link %% che prende due numeri e li moltiplica. Questo operatore usa la notazione infissa%% link %%, in cui l'operatore è posto in mezzo tra i due parametri%% link %% (es. per fare la moltiplicazione%% link %% tra `5` e `7` scriviamo `5 * 7` con il `*` nel mezzo).
> 
> La maggior parte delle funzioni%% link %%, però, usa la notazione prefissa%% link %%, cioè quella in cui l'operatore è posto _prima_ dei parametri che richiede. Per esempio, se vogliamo usare la funzione%% link %% `succ` che restituisce il successore%% link %% di un numero intero%% link %% per trovare il successore di `6`, dobbiamo scrivere `succ 6`:
> 
> ```haskell
> ghci> succ 6
> 7
> ```
> 
> Per le funzioni%% link %% con più parametri, come la funzione%% link %% `min` che prende due parametri%% link %% e restituisce quello minore, agiamo allo stesso modo: per calcolare per esempio il minimo%% Link %% tra `2` e `3` scriviamo `min 2 3`:
> 
> ```haskell
> ghci> min 2 3 
> 2
> ghci> max 100 101  
> 101  
> ```
> 
> In [Haskell](Informatica/Lambda-calcolo/Haskell/_index.md#^definizione-haskell) si usa la notazione prefissa%% link %% per rendere la notazione il più simile possibile a quanto avviene nel [$\lambda$-calcolo](Informatica/Lambda-calcolo/_index.md#^definizione-lambda-calcolo), nelle cui [applicazioni](Informatica/Lambda-calcolo/_index.md#^definizione-applicazione) viene posta prima la funzione%% Link %% e poi gli argomenti da applicare a quella funzione%% Link %%.
> 
> L'[applicazione](Informatica/Lambda-calcolo/_index.md#^definizione-applicazione) di funzioni%% link %% ha la più alta precedenza tra tutti gli operatori. Per esempio, non c'è differenza tra lo scrivere
> 
> ```haskell
> ghci> succ 9 + max 5 4 + 1  
> 16 
> ```
> 
> e
> 
> ```haskell
> ghci> (succ 9) + (max 5 4) + 1  
> 16  
> ```
> 
> È possibile usare le funzioni prefisse%% link %% con la notazione infissa%% link %% se le circondiamo con dei backtick%% link %% (`Shift+'` per scriverlo). Per esempio, `min 1 3` può essere scritto anche come
> 
> ```haskell
> ghci> 1 `min` 3
> 1
> ```

%% 
magari quest'ultima osservazione sulle notazioni prefisse si può spostare nel lambda-calcolo
%%

%% 
assegnare valori a variabili e richiamare variabili solo scrivendo il loro nome
%%

# 1 - Prima funzione in Haskell

In the previous section we got a basic feel for calling functions. Now let's try making our own! Open up your favorite text editor and punch in this function that takes a number and multiplies it by two.

doubleMe x = x + x

Functions are defined in a similar way that they are called. The function name is followed by parameters separated by spaces. But when defining functions, there's a = and after that we define what the function does. Save this as baby.hs or something. Now navigate to where it's saved and run ghci from there. Once inside GHCi, do :l baby. Now that our script is loaded, we can play with the function that we defined.

ghci> :l baby
[1 of 1] Compiling Main ( baby.hs, interpreted )
Ok, one module loaded.
ghci> doubleMe 9
18
ghci> doubleMe 8.3
16.6

Because + works on integers as well as on floating-point numbers (anything that can be considered a number, really), our function also works on any number. Let's make a function that takes two numbers and multiplies each by two and then adds them together.

doubleUs x y = x*2 + y*2

Simple. We could have also defined it as doubleUs x y = x + x + y + y. Testing it out produces pretty predictable results (remember to append this function to the baby.hs file, save it and then do :l baby inside GHCi).

ghci> doubleUs 4 9
26
ghci> doubleUs 2.3 34.2
73.0
ghci> doubleUs 28 88 + doubleMe 123
478

As expected, you can call your own functions from other functions that you made. With that in mind, we could redefine doubleUs like this:

doubleUs x y = doubleMe x + doubleMe y

This is a very simple example of a common pattern you will see throughout Haskell. Making basic functions that are obviously correct and then combining them into more complex functions. This way you also avoid repetition. What if some mathematicians figured out that 2 is actually 3 and you had to change your program? You could just redefine doubleMe to be x + x + x and since doubleUs calls doubleMe, it would automatically work in this strange new world where 2 is 3.

Functions in Haskell don't have to be in any particular order, so it doesn't matter if you define doubleMe first and then doubleUs or if you do it the other way around.

Now we're going to make a function that multiplies a number by 2 but only if that number is smaller than or equal to 100 because numbers bigger than 100 are big enough as it is!

doubleSmallNumber x = if x <= 100
then x*2
else x

this is you

Right here we introduced Haskell's if statement. You're probably familiar with if statements from other languages. The difference between Haskell's if statement and if statements in imperative languages is that the else part is mandatory in Haskell. In imperative languages you can just skip a couple of steps if the condition isn't satisfied but in Haskell every expression and function must return something. We could have also written that if statement in one line but I find this way more readable. Another thing about the if statement in Haskell is that it is an expression. An expression is basically a piece of code that returns a value. 5 is an expression because it returns 5, 4 + 8 is an expression, x + y is an expression because it returns the sum of x and y. Because the else is mandatory, an if statement will always return something and that's why it's an expression. If we wanted to add one to every number that's produced in our previous function, we could have written its body like this.

doubleSmallNumber' x = (if x > 100 then x else x*2) + 1

Had we omitted the parentheses, it would have added one only if x wasn't greater than 100. Note the ' at the end of the function name. That apostrophe doesn't have any special meaning in Haskell's syntax. It's a valid character to use in a function name. We usually use ' to either denote a strict version of a function (one that isn't lazy) or a slightly modified version of a function or a variable. Because ' is a valid character in functions, we can make a function like this.

conanO'Brien = "It's a-me, Conan O'Brien!"

There are two noteworthy things here. The first is that in the function name we didn't capitalize Conan's name. That's because functions can't begin with uppercase letters. We'll see why a bit later. The second thing is that this function doesn't take any parameters. When a function doesn't take any parameters, we usually say it's a definition (or a name). Because we can't change what names (and functions) mean once we've defined them, conanO'Brien and the string "It's a-me, Conan O'Brien!" can be used interchangeably.

# 2 - Liste in Haskell

Una delle strutture dati%% link %% più usate sono le liste%% link %% e in [Haskell](Informatica/Lambda-calcolo/Haskell/_index.md#^definizione-haskell) si possono implementare in diversi modi.

> [!sintassi]+ Sintassi: lista in Haskell
> 
> In [Haskell](Informatica/Lambda-calcolo/Haskell/_index.md#^definizione-haskell), una **lista** è una struttura dati%% link %% omogenea%% link %% (cioè formata dallo stesso tipo di dati%% link %%). Una lista è rappresentata da due parentesi quadre `[]` che racchiudono gli elementi della lista separati da virgole, per esempio:
> 
> ```haskell
> ghci> lostNumbers = [4,8,15,16,23,42]  
> ghci> lostNumbers  
> [4,8,15,16,23,42]  
> ```
> 
> Le **liste vuote** sono rappresentate da parentesi quadre `[]` vuote.
^sintassi-lista-in-haskell

> [!sintassi]+ Sintassi: lista annidata in Haskell
> 
> In [Haskell](Informatica/Lambda-calcolo/Haskell/_index.md#^definizione-haskell) è possibile creare anche una **lista annidata**, cioè una [lista](Sintassi%20di%20base%20di%20Haskell.md#^sintassi-lista-in-haskell) che contiene altre liste:
> 
> ```haskell
> ghci> b = [[1,2,3,4],[5,3,3,3],[1,2,2,3,4],[1,2,3]]  
> ghci> b  
> [[1,2,3,4],[5,3,3,3],[1,2,2,3,4],[1,2,3]]  
> ghci> b ++ [[1,1,1,1]]  
> [[1,2,3,4],[5,3,3,3],[1,2,2,3,4],[1,2,3],[1,1,1,1]]  
> ghci> [6,6,6]:b  
> [[6,6,6],[1,2,3,4],[5,3,3,3],[1,2,2,3,4],[1,2,3]]  
> ghci> b !! 2  
> [1,2,2,3,4]  
> ```
^sintassi-lista-annidata-in-haskell

> [!osservazione]+ Osservazione: vincoli di tipo nelle liste annidate
>
> Le [liste](Sintassi%20di%20base%20di%20Haskell.md#^sintassi-lista-in-haskell) all'interno di una [lista annidata](Sintassi%20di%20base%20di%20Haskell.md#^sintassi-lista-annidata-in-haskell) possono avere lunghezze diverse, ma non possono essere di tipi diversi: così come non puoi avere una lista che contiene sia caratteri che numeri, non puoi avere una lista che contiene sia liste di caratteri che liste di numeri.

%% 
Attenzione

**Note:** `[]`, `[[]]` and`[[],[],[]]` are all different things. The first one is an empty list, the second one is a list that contains one empty list, the third one is a list that contains three empty lists.
%%

Esattamente come per il C%% link %%, anche [Haskell](Informatica/Lambda-calcolo/Haskell/_index.md#^definizione-haskell) considera le stringhe%% link %% come [liste](Sintassi%20di%20base%20di%20Haskell.md#^definizione-lista-in-haskell) di caratteri%% link %%.

> [!sintassi]+ Sintassi: stringa in Haskell
> 
> In [Haskell](Informatica/Lambda-calcolo/Haskell/_index.md#^definizione-haskell) una **stringa** è una [lista](Sintassi%20di%20base%20di%20Haskell.md#^definizione-lista-in-haskell) di caratteri%% link %%. Ogni stringa può essere rappresentata con la solita notazione con le parentesi quadre `[]` che racchiudono i caratteri della stringa separati da virgole, oppure circondando la stringa con delle virgolette `""`:
> 
> ```haskell
> "hello" equivale a ["h", "e", "l", "l", "o"]
> ```
^sintassi-stringa-in-haskell

## 2.1 - Operazioni con liste

> [!sintassi]+ Sintassi: concatenazione di liste
> 
> In [Haskell](Informatica/Lambda-calcolo/Haskell/_index.md#^definizione-haskell) è possibile concatenare due [liste](Sintassi%20di%20base%20di%20Haskell.md#^sintassi-lista-in-haskell) (cioè unire le due liste giustapponendo agli elementi della prima quella della seconda) attraverso l'operatore `++`, detto **operatore di concatenazione** o, in inglese, **_concat operator_**:
> 
> ```haskell
> ghci> [1,2,3,4] ++ [5,6,7] == [1,2,3,4,5,6,7]
> True
> ```
> 
> Ciò vale anche per le [stringhe](Sintassi%20di%20base%20di%20Haskell.md#^sintassi-stringa-in-haskell) dato che anch'esse sono considerate [liste](Sintassi%20di%20base%20di%20Haskell.md#^sintassi-lista-in-haskell):
> 
> ```haskell
> ghci> "Hello" ++ " " ++ "world!" == "Hello world!"
> True
> ```
^sintassi-concatenazione-di-liste

> [!attenzione]+ Attenzione: concatenazione di liste troppo grandi
> 
> Quando [concateniamo](Sintassi%20di%20base%20di%20Haskell.md#^sintassi-concatenazione-di-liste) due [liste](Sintassi%20di%20base%20di%20Haskell.md#^sintassi-lista-in-haskell), anche se si concatena una [lista](Sintassi%20di%20base%20di%20Haskell.md#^sintassi-lista-in-haskell) _singoletto_%% link %% (cioè con un singolo elemento) a una lista, per esempio `[1,2,3] ++ [4]`, internamente [Haskell](Informatica/Lambda-calcolo/Haskell/_index.md#^definizione-haskell) deve attraversare l'intera [lista](Sintassi%20di%20base%20di%20Haskell.md#^sintassi-lista-in-haskell) a sinistra del `++` per trovarne l'ultimo elemento e concatenarle la seconda lista.
> 
> Ciò non è un problema con [liste](Sintassi%20di%20base%20di%20Haskell.md#^sintassi-lista-in-haskell) anche con qualche centinaio di elementi, però se si usa l'[operatore di concatenazione `++`](Sintassi%20di%20base%20di%20Haskell.md#^sintassi-concatenazione-di-liste) su [liste](Sintassi%20di%20base%20di%20Haskell.md#^sintassi-lista-in-haskell) troppo grandi (es. da centinaia di milioni di elementi) [Haskell](Informatica/Lambda-calcolo/Haskell/_index.md#^definizione-haskell) ci metterà un pochino a scorrerla tutta.

> [!sintassi]+ Sintassi: anteposizione di un elemento a una lista
> 
> In [Haskell](Informatica/Lambda-calcolo/Haskell/_index.md#^definizione-haskell) è possibile anteporre un elemento a una [lista](Sintassi%20di%20base%20di%20Haskell.md#^sintassi-lista-in-haskell) (cioè metterlo all'inizio della lista) attraverso l'operatore `:`, detto **operatore di anteposizione** o, in inglese, **_cons operator_**:
> 
> ```haskell
> ghci> 1 : [2, 3, 4] == [1, 2, 3, 4]
> True
> ```
> 
> Ovviamente anche questo operatore vale anche per le [stringhe](Sintassi%20di%20base%20di%20Haskell.md#^sintassi-stringa-in-haskell), essendo anch'esse [liste](Sintassi%20di%20base%20di%20Haskell.md#^sintassi-lista-in-haskell):
> 
> ```haskell
> ghci> "A" : " small cat" == "A small cat"
> True
> ```
^sintassi-anteposizione-di-un-elemento-a-una-lista

%% 
Osservazione: differenza tra concatenazione e anteposizione

Una prende due liste, l'altro un elemento e una lsita

Però equivalenti:

```haskell
ghci> [1] ++ [2, 3, 4] == 1 : [2, 3, 4]
True
```
%%

%% 
Osservazione:

```
ghci> [1, 2, 3] == 1:2:3:[]
True
```

perché If we prepend `3` to it, it becomes `[3]`. If we prepend `2` to that, it becomes `[2,3]`, and so on.
%%

> [!sintassi]+ Sintassi: accesso agli elementi di una lista con `!!`
> 
> In [Haskell](Informatica/Lambda-calcolo/Haskell/_index.md#^definizione-haskell) è possibile accedere a un elemento di una [lista](Sintassi%20di%20base%20di%20Haskell.md#^sintassi-lista-in-haskell) in base alla sua posizione (indice) attraverso l'operatore `!!`. Gli indici iniziano da `0`:
> 
> ```haskell
> ghci> "Steve Buscemi" !! 6  
> 'B'  
> ghci> [9.4,33.2,96.2,11.2,23.25] !! 1  
> 33.2  
> ```
> 
> Questo operatore funziona anche con le [stringhe](Sintassi%20di%20base%20di%20Haskell.md#^sintassi-stringa-in-haskell), essendo anch'esse [liste](Sintassi%20di%20base%20di%20Haskell.md#^sintassi-lista-in-haskell) di caratteri. Se si tenta di accedere a un indice fuori dai limiti della lista, Haskell genererà un errore.

> [!sintassi]+ Sintassi: confronto di liste
> 
In [Haskell](Informatica/Lambda-calcolo/Haskell/_index.md#^definizione-haskell) è possibile confrontare [](Sintassi%20di%20base%20di%20Haskell.md#^sintassi-lista-in-haskell) usando gli operatori `<`, `<=`, `>` e `>=`, a condizione che gli elementi contenuti siano confrontabili. Le liste vengono confrontate in **ordine lessicografico**: prima si confrontano gli elementi in testa (il primo elemento), se sono uguali si confrontano i secondi elementi, e così via:
> 
> ```haskell
> ghci> [3,2,1] > [2,1,0]
> True
> ghci> [3,2,1] > [2,10,100]
> True
> ghci> [3,4,2] > [3,4]
> True
> ghci> [3,4,2] > [2,4]
> True
> ghci> [3,4,2] == [3,4,2]
> True
> ```

> [!sintassi]+ Sintassi: funzione%% link %% `head`
> 
> La **funzione%% link %% `head`** prende una [lista](Sintassi%20di%20base%20di%20Haskell.md#^sintassi-lista-in-haskell) e restituisce il suo primo elemento:
> 
> ```haskell
> ghci> head [5,4,3,2,1]
> 5
> ```
^sintassi-funzione-head

> [!sintassi]+ Sintassi: funzione%% link %% `tail`
> 
> La **funzione%% link %% `tail`** prende una [lista](Sintassi%20di%20base%20di%20Haskell.md#^sintassi-lista-in-haskell) e restituisce la sua coda, cioè tutto ciò che rimane dopo aver rimosso il primo elemento:
> 
> ```haskell
> ghci> tail [5,4,3,2,1]
> [4,3,2,1]
> ```
^sintassi-funzione-tail

> [!sintassi]+ Sintassi: funzione%% link %% `last`
> 
> La **funzione%% link %% `last`** prende una [lista](Sintassi%20di%20base%20di%20Haskell.md#^sintassi-lista-in-haskell) e restituisce il suo ultimo elemento:
> 
> ```haskell
> ghci> last [5,4,3,2,1]
> 1
> ```
^sintassi-funzione-last

> [!sintassi]+ Sintassi: funzione%% link %% `init`
> 
> La **funzione%% link %% `init`** prende una [lista](Sintassi%20di%20base%20di%20Haskell.md#^sintassi-lista-in-haskell) e restituisce tutto ciò che rimane dopo aver rimosso l'ultimo elemento:
> 
> ```haskell
> ghci> init [5,4,3,2,1]
> [5,4,3,2]
> ```
^sintassi-funzione-init

> [!attenzione]+ Attenzione: funzioni su liste vuote
> 
> Le funzioni%% link %% [`head`](Sintassi%20di%20base%20di%20Haskell.md#^sintassi-funzione-head), [`tail`](Sintassi%20di%20base%20di%20Haskell.md#^sintassi-funzione-tail), [`last`](Sintassi%20di%20base%20di%20Haskell.md#^sintassi-funzione-last) e [`init`](Sintassi%20di%20base%20di%20Haskell.md#^sintassi-funzione-init) generano un errore se applicate a [liste vuote](Sintassi%20di%20base%20di%20Haskell.md#^sintassi-lista-in-haskell). Se tenti di ottenere l'elemento in testa di una lista vuota, Haskell genererà un'eccezione%% link %%:
> 
> ```haskell
> ghci> head []
> *** Exception: Prelude.head: empty list
> ```

%% 
Questo errore **non può essere catturato in fase di compilazione**, quindi è sempre buona pratica prendere precauzioni per evitare di applicare accidentalmente queste funzioni a liste vuote.
%%

> [!sintassi]+ Sintassi: funzione%% link %% `length`
> 
> La **funzione%% link %% `length`** prende una [lista](Sintassi%20di%20base%20di%20Haskell.md#^sintassi-lista-in-haskell) e restituisce la sua lunghezza:
> 
> ```haskell
> ghci> length [5,4,3,2,1]
> 5
> ```
^sintassi-funzione-length

> [!sintassi]+ Sintassi: funzione%% link %% `null`
> 
> La **funzione%% link %% `null`** verifica se una [lista](Sintassi%20di%20base%20di%20Haskell.md#^sintassi-lista-in-haskell) è vuota, restituendo `True` se la lista è vuota o `False` altrimenti:
> 
> ```haskell
> ghci> null [1,2,3]
> False
> ghci> null []
> True
> ```
^sintassi-funzione-null

> [!sintassi]+ Sintassi: funzione%% link %% `reverse`
> 
> La **funzione%% link %% `reverse`** inverte l'ordine degli elementi di una [lista](Sintassi%20di%20base%20di%20Haskell.md#^sintassi-lista-in-haskell):
> 
> ```haskell
> ghci> reverse [5,4,3,2,1]
> [1,2,3,4,5]
> ```
^sintassi-funzione-reverse

> [!sintassi]+ Sintassi: funzione%% link %% `take`
> 
> La **funzione%% link %% `take`** prende un numero e una [lista](Sintassi%20di%20base%20di%20Haskell.md#^sintassi-lista-in-haskell) ed estrae quel numero di elementi partendo dall'inizio della lista:
> 
> ```haskell
> ghci> take 3 [5,4,3,2,1]
> [5,4,3]
> ghci> take 1 [3,9,3]
> [3]
> ghci> take 5 [1,2]
> [1,2]
> ghci> take 0 [6,6,6]
> []
> ```
> 
> Se si tenta di estrarre più elementi di quanti ne contiene la lista, viene restituita l'intera lista. Se si estraggono 0 elementi, si ottiene una lista vuota.
^sintassi-funzione-take

> [!sintassi]+ Sintassi: funzione%% link %% `drop`
> 
> La **funzione%% link %% `drop`** prende un numero e una [lista](Sintassi%20di%20base%20di%20Haskell.md#^sintassi-lista-in-haskell) e scarta il numero di elementi specificato dall'inizio della [lista](Sintassi%20di%20base%20di%20Haskell.md#^sintassi-lista-in-haskell):
> 
> ```haskell
> ghci> drop 3 [8,4,2,1,5,6]
> [1,5,6]
> ghci> drop 0 [1,2,3,4]
> [1,2,3,4]
> ghci> drop 100 [1,2,3,4]
> []
> ```
^sintassi-funzione-drop

> [!sintassi]+ Sintassi: funzioni `maximum` e `minimum`
> 
> La **funzione%% link %% `maximum`** prende una [lista](Sintassi%20di%20base%20di%20Haskell.md#^sintassi-lista-in-haskell) di elementi ordinabili e restituisce l'elemento più grande, mentre la **funzione%% link %% `minimum`** restituisce l'elemento più piccolo:
> 
> ```haskell
> ghci> minimum [8,4,2,1,5,6]
> 1
> ghci> maximum [1,9,2,3,4]
> 9
> ```
^sintassi-funzioni-maximum-minimum

> [!sintassi]+ Sintassi: funzioni `sum` e `product`
> 
> La **funzione%% link %% `sum`** prende una [lista](Sintassi%20di%20base%20di%20Haskell.md#^sintassi-lista-in-haskell) di numeri e restituisce la loro somma%% link %%, mentre la **funzione%% link %% `product`** prende una lista di numeri e restituisce il loro prodotto%% link %%:
> 
> ```haskell
> ghci> sum [5,2,1,6,3,2,5,7]
> 31
> ghci> product [6,2,1,2]
> 24
> ghci> product [1,2,5,6,7,9,2,0]
> 0
> ```
^sintassi-funzioni-sum-product

> [!sintassi]+ Sintassi: funzione%% link %% `elem`
> 
> La **funzione%% link %% `elem`** prende un elemento e una [lista](Sintassi%20di%20base%20di%20Haskell.md#^sintassi-lista-in-haskell) e ci dice se quell'elemento è presente nella lista:
> 
> ```haskell
> ghci> elem 4 [3,4,5,6]
> True
> ```
> 
>  Solitamente viene usata come funzione infissa%% link %% perché è più leggibile:
> 
> ```haskell
> ghci> 10 `elem` [3,4,5,6]
> False
> ```
^sintassi-funzione-elem

## 2.2 - Range list

In [Haskell](Informatica/Lambda-calcolo/Haskell/_index.md#^definizione-haskell), quando vogliamo creare una [lista](Sintassi%20di%20base%20di%20Haskell.md#^sintassi-lista-in-haskell) di numeri che seguono una sequenza aritmetica%% link %%, non è necessario scrivere manualmente ogni elemento. Le [range list](Sintassi%20di%20base%20di%20Haskell.md#^sintassi-range-list) sono una sintassi conveniente per generare [liste](Sintassi%20di%20base%20di%20Haskell.md#^sintassi-lista-in-haskell) di elementi enumerabili, come numeri e caratteri. Un elemento è enumerabile%% link %% se fa parte di una sequenza ordinata (i numeri naturali, le lettere dell'alfabeto, ecc.), mentre nomi arbitrari non lo sono.

> [!sintassi]+ Sintassi: range list
> 
> In [Haskell](Informatica/Lambda-calcolo/Haskell/_index.md#^definizione-haskell) una **range list** è una [lista](Sintassi%20di%20base%20di%20Haskell.md#^sintassi-lista-in-haskell) definita attraverso un intervallo, cioè usando la sintassi `[inizio..fine]` per creare una lista di elementi contenente tutti i valori compresi tra il valore `inizio` e il valore `fine`, compresi questi ultimi:
> 
> ```haskell
> ghci> [1..20]
> [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
> ghci> ['a'..'z']
> "abcdefghijklmnopqrstuvwxyz"
> ghci> ['K'..'Z']
> "KLMNOPQRSTUVWXYZ"
> ```
> 
> Per specificare un passo (incremento) diverso da 1, scrivi i primi due elementi separati da virgola, seguito da `..` e dal limite superiore: `[primo,secondo..fine]`:
> 
> ```haskell
> ghci> [2,4..20]
> [2,4,6,8,10,12,14,16,18,20]
> ghci> [3,6..20]
> [3,6,9,12,15,18]
> ```
> 
> Per creare [liste](Sintassi%20di%20base%20di%20Haskell.md#^sintassi-lista-in-haskell) decrescenti, specifica esplicitamente il passo negativo:
> 
> ```haskell
> ghci> [20,19..1]
> [20,19,18,17,16,15,14,13,12,11,10,9,8,7,6,5,4,3,2,1]
> ```
> 
> Omettendo il limite superiore, puoi creare [liste](Sintassi%20di%20base%20di%20Haskell.md#^sintassi-lista-in-haskell) infinite. [Haskell](Informatica/Lambda-calcolo/Haskell/_index.md#^definizione-haskell) le valuta in modo [lazy](Informatica/Lambda-calcolo/_index.md#^definizione-ordine-normale), quindi calcola solo gli elementi di cui hai bisogno:
> 
> ```haskell
> ghci> take 24 [13,26..]
> [13,26,39,52,65,78,91,104,117,130,143,156,169,182,195,208,221,234,247,260,273,286]
> ```
^sintassi-range-list

> [!attenzione]+ Attenzione: limitazioni delle range list
> 
> [Definendo una range list](Sintassi%20di%20base%20di%20Haskell.md#^sintassi-range-list) è possibile solo specificare un incremento costante (cioè ottenere sequenze aritmetiche%% link %%), non progressioni più complesse come potenze.
> 
> È consigliato inoltre evitare intervalli con numeri in virgola mobile%% link %%, poiché la loro imprecisione può produrre risultati inaspettati:
> 
> ```haskell
> ghci> [0.1, 0.3 .. 1]
> [0.1,0.3,0.5,0.7,0.8999999999999999,1.0999999999999999]
> ```

## 2.3 - Liste infinite

> [!sintassi]+ Sintassi: funzione `cycle`
> 
> La **funzione%% link %% `cycle`** prende una [lista](Sintassi%20di%20base%20di%20Haskell.md#^sintassi-lista-in-haskell) e la ripete infinitamente. Poiché il risultato è una lista infinita, bisogna sempre troncarla usando funzioni%% link %% come [`take`](Sintassi%20di%20base%20di%20Haskell.md#^sintassi-funzione-take) per ottenere un numero finito di elementi:
> 
> ```haskell
> ghci> take 10 (cycle [1,2,3])
> [1,2,3,1,2,3,1,2,3,1]
> ghci> take 12 (cycle "LOL ")
> "LOL LOL LOL "
> ```
^sintassi-funzione-cycle

> [!sintassi]+ Sintassi: funzione `repeat`
> 
> La **funzione%% link %% `repeat`** prende un elemento e produce una [lista](Sintassi%20di%20base%20di%20Haskell.md#^sintassi-lista-in-haskell) infinita contenente solo quel elemento. È equivalente a ciclare una lista con un solo elemento:
> 
> ```haskell
> ghci> take 10 (repeat 5)
> [5,5,5,5,5,5,5,5,5,5]
> ```
^sintassi-funzione-repeat

> [!sintassi]+ Sintassi: funzione `replicate`
> 
> La **funzione%% link %% `replicate`** prende un numero e un elemento, e restituisce una [lista](Sintassi%20di%20base%20di%20Haskell.md#^sintassi-lista-in-haskell) finita contenente quel numero di copie dell'elemento. È conveniente usarla al posto di [`repeat`](Sintassi%20di%20base%20di%20Haskell.md#^sintassi-funzione-repeat) quando si sa esattamente quanti elementi servono:
> 
> ```haskell
> ghci> replicate 3 10
> [10,10,10]
> ```
^sintassi-funzione-replicate

## 2.4 - List comprehension

Un modo molto più comodo per definire una [lista](Sintassi%20di%20base%20di%20Haskell.md#^sintassi-lista-in-haskell) contenente solo elementi che rispettano un certo criterio è la [list comprehension](Sintassi%20di%20base%20di%20Haskell.md#^sintassi-list-comprehension).

> [!sintassi]+ Sintassi: list comprehension
> 
> In [Haskell](Informatica/Lambda-calcolo/Haskell/_index.md#^definizione-haskell) una **list comprehension** è una [lista](Sintassi%20di%20base%20di%20Haskell.md#^sintassi-lista-in-haskell) definita attraverso una funzione%% link %% [applicata](Informatica/Lambda-calcolo/_index.md#^definizione-applicazione) a ogni elemento di un'altra [lista](Sintassi%20di%20base%20di%20Haskell.md#^sintassi-lista-in-haskell) passata in input. Ha la forma: `[funzione_output | variabile <- lista_input]`
> 
> ```haskell
> ghci> [x*2 | x <- [1..10]]
> [2,4,6,8,10,12,14,16,18,20]
> ```
> 
> In questo esempio, `x*2` è la funzione di output, `x <- [1..10]` estrae ogni elemento dalla lista `[1..10]`.
^sintassi-list-comprehension

%% 
È l'equivalente informatico delle comprensioni di insiemi usate in matematica.
%%

> [!sintassi]+ Sintassi: list comprehension con predicati
> 
> Una [list comprehension](Sintassi%20di%20base%20di%20Haskell.md#^sintassi-list-comprehension) può contenere **predicati** che filtrano gli elementi usando una o più condizioni, separate da virgole:
> 
> ```haskell
> ghci> [x*2 | x <- [1..10], x*2 >= 12]
> [12,14,16,18,20]
> ghci> [x | x <- [50..100], x `mod` 7 == 3]
> [52,59,66,73,80,87,94]
> ```
> 
> Nel primo esempio, vengono raddoppiati solo gli elementi il cui doppio è maggiore o uguale a 12. Nel secondo, vengono selezionati solo i numeri tra 50 e 100 il cui resto della divisione per 7 è 3.
> 
> Possono anche esserci **più predicati** separati da virgole. Un elemento viene incluso solo se soddisfa **tutti** i predicati:
> 
> ```haskell
> ghci> [ x | x <- [10..20], x /= 13, x /= 15, x /= 19]
> [10,11,12,14,16,17,18,20]
> ```
> 
> In questo esempio, vengono selezionati solo i numeri tra 10 e 20 che non sono 13, 15 o 19.
^sintassi-list-comprehension-con-predicati

> [!sintassi]+ Sintassi: list comprehension con condizionali
> 
> Una [list comprehension](Sintassi%20di%20base%20di%20Haskell.md#^sintassi-list-comprehension) può contenere **espressioni condizionali** (`if-then-else`) nella funzione di output per trasformare gli elementi in base a condizioni:
> 
> ```haskell
> boomBangs xs = [ if x < 10 then "BOOM!" else "BANG!" | x <- xs, odd x]
> ghci> boomBangs [7..13]
> ["BOOM!","BOOM!","BANG!","BANG!"]
> ```
> 
> In questo esempio, la funzione `odd` verifica se un numero è dispari. L'elemento viene incluso nella lista solo se il predicato `odd x` è `True`.
^sintassi-list-comprehension-con-condizionali

> [!sintassi]+ Sintassi: list comprehension con più liste
> 
> Una [list comprehension](Sintassi%20di%20base%20di%20Haskell.md#^sintassi-list-comprehension) può ottenere dati da **più liste**. Produce tutte le combinazioni possibili degli elementi delle liste, applicate alla funzione%% link %% di output:
> 
> ```haskell
> ghci> [ x*y | x <- [2,5,10], y <- [8,10,11]]
> [16,20,22,40,50,55,80,100,110]
> ghci> [ x*y | x <- [2,5,10], y <- [8,10,11], x*y > 50]
> [55,80,100,110]
> ```
> 
> Si possono anche combinare [stringhe](Sintassi%20di%20base%20di%20Haskell.md#^sintassi-stringa-in-haskell) (ossia [liste](Sintassi%20di%20base%20di%20Haskell.md#^sintassi-lista-in-haskell) di caratteri):
> 
> ```haskell
> ghci> nouns = ["hobo","frog","pope"]
> ghci> adjectives = ["lazy","grouchy","scheming"]
> ghci> [adjective ++ " " ++ noun | adjective <- adjectives, noun <- nouns]
> ["lazy hobo","lazy frog","lazy pope","grouchy hobo","grouchy frog","grouchy pope","scheming hobo","scheming frog","scheming pope"]
> ```
^sintassi-list-comprehension-piu-liste

%%

[!sintassi]+ Sintassi: list comprehension con segnaposto

Una [list comprehension](Sintassi%20di%20base%20di%20Haskell.md#^sintassi-list-comprehension-con-condizionali) può usare un **segnaposto**, identificato dal `_`, quando non si è interessati al valore estratto dalla [lista](Sintassi%20di%20base%20di%20Haskell.md#^sintassi-lista-in-haskell), senza nominare una variabileLINK inutilizzata:

```haskell
length' xs = sum [1 | _ <- xs]
ghci> length' [1,2,3,4,5]
5
```

In questo esempio, `_` rappresenta ogni elemento della lista, che viene sostituito con 1 e poi sommato per ottenere la lunghezza della lista.
^sintassi-list-comprehension-con-segnaposto

%%

> [!esempio]- Esempio: list comprehension su stringhe
> 
> Poiché le [stringhe](Sintassi%20di%20base%20di%20Haskell.md#^sintassi-stringa-in-haskell) sono [liste](Sintassi%20di%20base%20di%20Haskell.md#^sintassi-lista-in-haskell) di caratteri in [Haskell](Informatica/Lambda-calcolo/Haskell/_index.md#^definizione-haskell), si può usare una [list comprehension](Sintassi%20di%20base%20di%20Haskell.md#^sintassi-list-comprehension) per filtrare e processare stringhe:
> 
> ```haskell
> removeNonUppercase st = [ c | c <- st, c `elem` ['A'..'Z']]
> ghci> removeNonUppercase "Hahaha! Ahahaha!"
> "HA"
> ghci> removeNonUppercase "IdontLIKEFROGS"
> "ILIKEFROGS"
> ```
> 
> In questo esempio, il predicato filtra solo i caratteri maiuscoli dalla stringa.
^sintassi-list-comprehension-stringhe

> [!sintassi]+ Sintassi: list comprehension annidate
> 
> Una **list comprehension annidata** è una [list comprehension](Sintassi%20di%20base%20di%20Haskell.md#^sintassi-list-comprehension) che contiene altre [list comprehension](Sintassi%20di%20base%20di%20Haskell.md#^sintassi-list-comprehension) al suo interno. Questo permette di operare su [liste annidate](Sintassi%20di%20base%20di%20Haskell.md#^sintassi-lista-annidata-in-haskell) e filtrarne gli elementi senza appiattire la struttura:
> 
> ```haskell
> ghci> let xxs = [[1,3,5,2,3,1,2,4,5],[1,2,3,4,5,6,7,8,9],[1,2,4,2,1,6,3,1,3,2,3,6]]
> ghci> [ [ x | x <- xs, even x ] | xs <- xxs]
> [[2,2,4],[2,4,6,8],[2,4,2,6,2,6]]
> ```
> 
> In questo esempio, la [list comprehension](Sintassi%20di%20base%20di%20Haskell.md#^sintassi-list-comprehension) esterna itera su ogni lista in `xxs` (estraendo ogni sottolista `xs`), mentre quella interna filtra i numeri pari da ogni lista `xs`, mantenendo la struttura annidata. Il risultato è una lista di liste contenente solo i numeri pari da ogni sottolista.
^sintassi-list-comprehension-annidate

# 3 - Tuple

Le [tupla](Sintassi%20di%20base%20di%20Haskell.md#^definizione-tupla-in-haskell) sono un modo per memorizzare più valori in un'unica struttura, simile alle [liste](Sintassi%20di%20base%20di%20Haskell.md#^sintassi-lista-in-haskell), ma la loro dimensione e i tipi dei loro componenti sono fissi e definiti al momento della creazione.

> [!definizione]+ Definizione: tupla in Haskell
> 
> In [Haskell](Informatica/Lambda-calcolo/Haskell/_index.md#^definizione-haskell), una **tupla** è una struttura dati%% link %% eterogenea%% link %% che combina un numero fisso e noto di valori, chiamati **componenti**. È denotata con parentesi tonde `()` contenente i suoi componenti separati da virgole:
> 
> ```haskell
> ghci> (1, 2)
> (1,2)
> ghci> ("David", "Lynch", 55)
> ("David","Lynch",55)
> ghci> (1, "hello", True)
> (1,"hello",True)
> ```
> 
> Una **tupla** di due elementi si chiama **coppia** (in inglese **_pair_**), una di tre elementi si chiama **tripla** (in inglese **_triple_**) e così via.
^sintassi-tupla-in-haskell

> [!osservazione]+ Osservazione: il tipo delle tuple dipende da numero e tipi dei componenti
> 
> Il tipo%% link %% di una [tupla](Sintassi%20di%20base%20di%20Haskell.md#^sintassi-tupla-in-haskell) è determinato da due fattori: il numero di [componenti](Sintassi%20di%20base%20di%20Haskell.md#^sintassi-tupla-in-haskell) e i tipi di ciascun [componente](Sintassi%20di%20base%20di%20Haskell.md#^sintassi-tupla-in-haskell). Questo significa che ogni tupla di diversa dimensione o con diversi tipi è considerata un tipo completamente diverso. Per esempio:
> - `(1, 2)` è di tipo `(Integer, Integer)`,
> - `(1, 2, 3)` è di tipo `(Integer, Integer, Integer)`,
> - `(1, "hello")` è di tipo `(Integer, String)` e
> - `("David", "Lynch", 55)` è di tipo `(String, String, Integer)`.
^osservazione-il-tipo-delle-tuple-dipende-da-numero-e-tipi-dei-componenti

> [!osservazione]+ Osservazione: tuple e liste
> 
> A differenza delle [liste](Sintassi%20di%20base%20di%20Haskell.md#^sintassi-lista-in-haskell), le [tuple](Sintassi%20di%20base%20di%20Haskell.md#^sintassi-tupla-in-haskell):
> - Hanno una dimensione fissa, nota al momento della creazione.
> - Possono contenere elementi di tipi diversi (sono cioè strutture dati%% link %% eterogenee%% link %%).
> - Il loro tipo dipende dal numero di componenti e dai loro tipi, come già [osservato](Sintassi%20di%20base%20di%20Haskell.md#^osservazione-il-tipo-delle-tuple-dipende-da-numero-e-tipi-dei-componenti) poco fa.
> 
> Proprio per quest'ultimo punto, se una [lista](Sintassi%20di%20base%20di%20Haskell.md#^sintassi-lista-in-haskell) ha come elementi delle [tuple](Sintassi%20di%20base%20di%20Haskell.md#^sintassi-tupla-in-haskell), esse devono avere [componenti](Sintassi%20di%20base%20di%20Haskell.md#^sintassi-tupla-in-haskell) dello stesso tipo e dello stesso numero. Non possiamo avere una [lista](Sintassi%20di%20base%20di%20Haskell.md#^sintassi-lista-in-haskell) mista di [coppie](Sintassi%20di%20base%20di%20Haskell.md#^sintassi-tupla-in-haskell) e [triple](Sintassi%20di%20base%20di%20Haskell.md#^sintassi-tupla-in-haskell), né puoi possiamo una [lista](Sintassi%20di%20base%20di%20Haskell.md#^sintassi-lista-in-haskell) che contenga sia `(1,2)` che `(1,"hello")` perché il primo elemento sarebbe una coppia di numeri e il secondo sarebbe una coppia di numero e stringa:
> 
> ```haskell
> ghci> [(1,2), (8,11,5), (4,5)]
> <interactive>:5:9: error: [GHC-83865]
>     • Couldn't match expected type: (a, b)
>                   with actual type: (a0, b0, c0)
>     • In the expression: (8, 11, 5)
>       In the expression: [(1, 2), (8, 11, 5), (4, 5)]
>       In an equation for ‘it': it = [(1, 2), (8, 11, 5), (4, 5)]
>     • Relevant bindings include
>         it :: [(a, b)] (bound at <interactive>:5:1)
> ```

> [!attenzione]+ Attenzione: non esiste la tupla _singoletto_
> 
> In [Haskell](Informatica/Lambda-calcolo/Haskell/_index.md#^definizione-haskell) non esiste il concetto di [tupla](Sintassi%20di%20base%20di%20Haskell.md#^sintassi-tupla-in-haskell) _singoletto_, cioè con un solo elemento: una [tupla](Sintassi%20di%20base%20di%20Haskell.md#^sintassi-tupla-in-haskell) di un elemento sarebbe semplicemente il valore stesso, quindi non avrebbe utilità pratica.

## 3.1 - Funzioni su tuple

Ora vediamo un po' di funzioni%% link %% che agiscono sulle [tuple](Sintassi%20di%20base%20di%20Haskell.md#^sintassi-tupla-in-haskell).

> [!definizione]+ Definizione: funzione `fst`
> 
> **`fst`** è una funzione%% link %% di [Haskell](Informatica/Lambda-calcolo/Haskell/_index.md#^definizione-haskell) che prende una [coppia](Sintassi%20di%20base%20di%20Haskell.md#^sintassi-tupla-in-haskell) e restituisce il suo primo [componente](Sintassi%20di%20base%20di%20Haskell.md#^sintassi-tupla-in-haskell):
> 
> ```haskell
> ghci> fst (9,11)
> 8
> ghci> fst ("Wow", False)
> "Wow"
> ```
> 
> Questa funzione%% link %% opera solo su [coppie](Sintassi%20di%20base%20di%20Haskell.md#^sintassi-tupla-in-haskell), cioè [tuple](Sintassi%20di%20base%20di%20Haskell.md#^sintassi-tupla-in-haskell) di 2 [componenti](Sintassi%20di%20base%20di%20Haskell.md#^sintassi-tupla-in-haskell), non su [triple](Sintassi%20di%20base%20di%20Haskell.md#^sintassi-tupla-in-haskell) o tuple più grandi.
^sintassi-funzione-fst

> [!definizione]+ Definizione: funzione `snd`
> 
> **`snd`** è una funzione%% link %% di [Haskell](Informatica/Lambda-calcolo/Haskell/_index.md#^definizione-haskell) che prende una [coppia](Sintassi%20di%20base%20di%20Haskell.md#^sintassi-tupla-in-haskell) e restituisce il suo secondo [componente](Sintassi%20di%20base%20di%20Haskell.md#^sintassi-tupla-in-haskell):
> 
> ```haskell
> ghci> snd (8,11)
> 11
> ghci> snd ("Wow", False)
> False
> ```
> 
> Questa funzione%% link %% opera solo su [coppie](Sintassi%20di%20base%20di%20Haskell.md#^sintassi-tupla-in-haskell), cioè [tuple](Sintassi%20di%20base%20di%20Haskell.md#^sintassi-tupla-in-haskell) di 2 [componenti](Sintassi%20di%20base%20di%20Haskell.md#^sintassi-tupla-in-haskell), non su [triple](Sintassi%20di%20base%20di%20Haskell.md#^sintassi-tupla-in-haskell) o tuple più grandi.
^sintassi-funzione-snd

> [!definizione]+ Definizione: funzione `zip`
> 
> **`zip`** è una funzione%% link %% di [Haskell](Informatica/Lambda-calcolo/Haskell/_index.md#^definizione-haskell) che prende due [liste](Sintassi%20di%20base%20di%20Haskell.md#^sintassi-lista-in-haskell) e le "cuce" insieme (come una cerniera lampo, cioè in inglese _zip_), creando una [lista](Sintassi%20di%20base%20di%20Haskell.md#^sintassi-lista-in-haskell) di [coppie](Sintassi%20di%20base%20di%20Haskell.md#^sintassi-tupla-in-haskell) con gli elementi corrispondenti abbinati a due a due:
> 
> ```haskell
> ghci> zip [1,2,3,4,5] [5,5,5,5,5]
> [(1,5),(2,5),(3,5),(4,5),(5,5)]
> ghci> zip [1 .. 5] ["one", "two", "three", "four", "five"]
> [(1,"one"),(2,"two"),(3,"three"),(4,"four"),(5,"five")]
> ```
> 
> Se le [liste](Sintassi%20di%20base%20di%20Haskell.md#^sintassi-lista-in-haskell) hanno lunghezze diverse, la lista più lunga viene troncata per corrispondere alla lunghezza di quella più corta:
> 
> ```haskell
> ghci> zip [5,3,2,6,2,7,2,5,4,6,6] ["im","a","turtle"]
> [(5,"im"),(3,"a"),(2,"turtle")]
> ```
^sintassi-funzione-zip

> [!osservazione]+ Osservazione: zip tra una lista finita e una infinita
> 
> Poiché [Haskell](Informatica/Lambda-calcolo/Haskell/_index.md#^definizione-haskell) è [lazy](Informatica/Lambda-calcolo/_index.md#^definizione-ordine-normale), è possibile fare una [`zip`](Sintassi%20di%20base%20di%20Haskell.md#^sintassi-funzione-zip) tra una [lista](Sintassi%20di%20base%20di%20Haskell.md#^sintassi-lista-in-haskell) finita%% link %% e una infinita%% link %%, perché quest'ultima verrà valutata solo finché serve (cioè per un numero di [componenti](Sintassi%20di%20base%20di%20Haskell.md#^sintassi-tupla-in-haskell) pari a quello della lista finita):
> 
> ```haskell
> ghci> zip [1..] ["apple", "orange", "cherry", "mango"]
> [(1,"apple"),(2,"orange"),(3,"cherry"),(4,"mango")]
> ```

%%

> [!esempio]- Esempio: tuple con list comprehension - triangoli rettangoli
> 
> Le tuple e le list comprehension possono essere combinate per risolvere problemi complessi. Per esempio, per trovare tutti i triangoli rettangoli con lati interi minori o uguali a 10:
> 
> ```haskell
> ghci> triangles = [ (a,b,c) | c <- [1..10], a <- [1..10], b <- [1..10] ]
> ```
> 
> Aggiungendo il vincolo che siano triangoli rettangoli (teorema di Pitagora):
> 
> ```haskell
> ghci> rightTriangles = [ (a,b,c) | c <- [1..10], a <- [1..c], b <- [1..a], a^2 + b^2 == c^2]
> ```
> 
> Infine, aggiungendo il vincolo che il perimetro sia 24:
> 
> ```haskell
> ghci> rightTriangles' = [ (a,b,c) | c <- [1..10], a <- [1..c], b <- [1..a], a^2 + b^2 == c^2, a+b+c == 24]
> ghci> rightTriangles'
> [(8,6,10)]
> ```
> 
> Questo è un esempio comune di pattern di programmazione funzionale: partire da un insieme di soluzioni possibili e applicare trasformazioni e filtri fino ad ottenere le soluzioni desiderate.

%%

---

> [!fonti]+ Fonti
> 
> - 📚 Miran Lipovača, _Learn You a Haskell for Great Good!_:
> 	- 2 - [_Starting out_](https://learnyouahaskell.github.io/starting-out.html).
