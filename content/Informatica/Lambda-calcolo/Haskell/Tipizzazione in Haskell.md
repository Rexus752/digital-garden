
> [!premessa]+ Premessa
> 
> Ciao! Se è la prima volta che capiti su questo sito, ti consiglio di consultare la [pagina principale](index.md) di questo cosiddetto _Giardino Digitale_ per scoprire meglio cos'è e come navigarlo.
> 
> Lo stato di questa nota è al momento: 🔴 <font color="#FF7F7F">_Bozza_</font>.

---

%% 
**Asse 1 — quando avviene il controllo: statica vs dinamica**

- **Statica**: i tipi vengono controllati a _compile time_. Se sbagli tipo, il programma non compila nemmeno. (Haskell, Rust, Java)
- **Dinamica**: i tipi vengono controllati a _runtime_, mentre il programma gira. L'errore arriva solo quando quella riga viene eseguita. (Python, JavaScript)

**Asse 2 — quanto è rigido il controllo: forte vs debole**

- **Forte**: il linguaggio rifiuta (o lancia un errore) se provi a mescolare tipi incompatibili. `"3" + 5` \to errore.
- **Debole**: il linguaggio converte silenziosamente i tipi per far tornare i conti. `"3" + 5` \to `"35"` o `8` a seconda dei casi. Questo si chiama _coercizione implicita_.

**Attenzione**: "forte/debole" non è una proprietà binaria netta — è più uno spettro. C è statico ma abbastanza debole (casting libero dei puntatori); Python è dinamico ma forte (nessuna coercizione silenziosa tra tipi incompatibili).

Haskell si trova nell'angolo più estremo del quadrante _statico + forte_: il type system è così rigoroso che se il programma compila, una larga classe di bug è già esclusa per costruzione.

- statica + forte: Haskell, Rust, Java, Scala, OCaml, TypeScript, Kotlin, Swift
- statica + debole: C, C++
- dinamica + forte: Python, Ruby, Clojure
- dinamica + debole: JavaScript, PHP, Perl
%%

Come già detto, [Haskell](Haskell.md#^definizione-haskell) ha un sistema di tipi statico%% link %%. Ciò significa che il [tipo](Tipizzazione%20in%20Haskell.md#^definizione-tipo-in-haskell) di ogni espressione è noto a tempo di compilazione%% link %%, il che ci porta ad avere un codice%% Link %% più sicuro. Se scrivi un programma in cui provi a dividere un booleano%% link %% con qualche numero, non ti permette neanche di compilare. Ciò ci va più che bene perché è meglio catturare questo tipo di errori a tempo di compilazione%% link %% anziché far crashare il progrmma. Ogni cosa in [Haskell](Haskell.md#^definizione-haskell) ha un tipo%% so the compiler can reason quite a lot about your program before compiling it. %%.

> [!definizione]+ Definizione: tipo in Haskell
> 
> In [Haskell](Haskell.md#^definizione-haskell), un **tipo** è un'etichetta che descrive quali valori può assumere un'espressione%% link %%. [Haskell](Haskell.md#^definizione-haskell) ha una tipizzazione statica%% Link %%, cioè il **tipo** dell'espressione viene determinato a tempo di compilazione%% link %%, ed è fortemente tipizzato%% link %%, cioè non permette a una espressione di cambiare **tipo** durante l'esecuzione%% o valutazione? %% del programma.
> 
> [Haskell](Haskell.md#^definizione-haskell) gode inoltre dell'inferenza di tipo%% link %%.
^definizione-tipo-in-haskell

%%
L'**inferenza di tipo** è la capacità del compilatore di dedurre automaticamente il tipo di un'espressione senza che il programmatore lo scriva esplicitamente.

Quasi tutti i linguaggi moderni con tipizzazione statica hanno una qualche forma di inferenza di tipo. La differenza è quanto è *potente* e *pervasiva*.

---

**Inferenza alla Hindley-Milner** — completa, deduce tutto

Sono i linguaggi dove l'inferenza è totale: raramente serve scrivere un tipo, e il compilatore deduce anche i vincoli di classe / i polimorfismi.

- Haskell
- OCaml
- F#
- Elm
- Idris
- Agda

---

**Inferenza parziale** — deduce il tipo locale, ma serve aiuto in certi punti

Linguaggi dove l'inferenza c'è ma ha limiti — spesso richiede firme esplicite sui metodi pubblici, nei generici complessi, o ai confini tra moduli.

- Rust — inferenza forte dentro le funzioni, firme obbligatorie nelle dichiarazioni
- Swift — simile a Rust
- Kotlin — inferisce le variabili locali, spesso vuole il tipo nei parametri
- Scala — inferenza potente ma non completa come HM
- C++ — `auto` e `decltype` dal 2011, ma limitati

---

**Inferenza minimale** — solo le variabili locali

- TypeScript — inferisce il tipo di una variabile dal valore assegnato, ma non fa polimorfismo parametrico vero
- C# — `var` deduce il tipo locale, niente di più

---

**La differenza pratica con Haskell**

Haskell (e OCaml, Elm...) usano HM in forma pura: l'inferenza è *decidibile* e *completa* — il compilatore trova sempre il tipo più generale possibile senza aiuto. Rust e Scala fanno scelte che rendono l'inferenza più potente in alcuni casi ma non più garantita — ci sono situazioni dove il compilatore si arrende e chiede una firma esplicita.

Unlike Java or Pascal, Haskell has type inference. If we write a number, we don’t have to tell Haskell it’s a number. It can _infer_ that on its own, so we don’t have to explicitly write out the types of our functions and expressions to get things done. We covered some of the basics of Haskell with only a very superficial glance at types. However, understanding the type system is a very important part of learning Haskell.

attenzione: inferenza =/= debolmente tipizzato: Haskell inferisce il tipo di un'espressione ma non permette di modificarlo (perché è **fortemente** tipizzato).
%%

> [!definizione]+ Definizione: comando `:t` nel GHCi
> 
> **`:t`** (abbreviazione di **`:type`**) è un comando di [GHCi](Haskell.md#^definizione-ghci) che mostra la firma di tipo di un'espressione senza valutarla.
^definizione-comando-t-nel-ghci

Now we’ll use GHCi to examine the types of some expressions. We’ll do that by using the :t command which, followed by any valid expression, tells us its type. Let’s give it a whirl.

```haskell
ghci> :t 'a'  
'a' :: Char  
ghci> :t True  
True :: Bool  
ghci> :t "HELLO!"  
"HELLO!" :: [Char]  
ghci> :t (True, 'a')  
(True, 'a') :: (Bool, Char)  
ghci> :t 4 == 5  
4 == 5 :: Bool  
```

Here we see that doing `:t` on an expression prints out the expression followed by `::` and its type. `::` is read as "has type of". Explicit types are always denoted with the first letter in capital case. `'a'`, as it would seem, has a type of `Char`. It’s not hard to conclude that it stands for _character_. `True` is of a `Bool` type. That makes sense. But what’s this? Examining the type of `"HELLO!"` yields a `[Char]`. The square brackets denote a list. So we read that as it being _a list of characters_. Unlike lists, each tuple length has its own type. So the expression of `(True, 'a')` has a type of `(Bool, Char)`, whereas an expression such as `('a','b','c')` would have the type of `(Char, Char, Char)`. `4 == 5` will always return `False`, so its type is `Bool`.

Functions also have types. When writing our own functions, we can choose to give them an explicit type declaration. This is generally considered to be good practice except when writing very short functions. From here on, we’ll give all the functions that we make type declarations. Remember the list comprehension we made previously that filters a string so that only caps remain? Here’s how it looks like with a type declaration.

```haskell
removeNonUppercase :: [Char] -> [Char]  
removeNonUppercase st = [c | c <- st, c `elem` ['A'..'Z']]  
```

`removeNonUppercase` has a type of `[Char] -> [Char]`, meaning that it maps from a string to a string. That’s because it takes one string as a parameter and returns another as a result. The `[Char]` type is synonymous with `String` so it’s clearer if we write `removeNonUppercase :: String -> String`. We didn’t have to give this function a type declaration because the compiler can infer by itself that it’s a function from a string to a string but we did anyway. But how do we write out the type of a function that takes several parameters? Here’s a simple function that takes three integers and adds them together:

```haskell
addThree :: Int -> Int -> Int -> Int  
addThree x y z = x + y + z  
```

The parameters are separated with `->` and there’s no special distinction between the parameters and the return type. The return type is the last item in the declaration and the parameters are the first three. Later on we’ll see why they’re all just separated with `->` instead of having some more explicit distinction between the return types and the parameters like `Int, Int, Int -> Int` or something.

If you want to give your function a type declaration but are unsure as to what it should be, you can always just write the function without it and then check it with `:t`. Functions are expressions too, so `:t` works on them without a problem.

Here’s an overview of some common types.

> [!definizione]+ Definizione: tipo `Int`
> 
> **`Int`** è un [tipo](Tipizzazione%20in%20Haskell.md#^definizione-tipo-in-haskell) in [Haskell](Haskell.md#^definizione-haskell) usato per rappresentare i numeri interi%% link %% (in inglese _integer numbers_). È un tipo _bounded_%% link %% e sulle macchine a 32 bit%% link %% l'intervallo di valori corrisponde a $[-2147483648,2147483647]$.
^definizione-tipo-int

> [!definizione]+ Definizione: tipo `Integer`
> 
> **`Integer`** è un [tipo](Tipizzazione%20in%20Haskell.md#^definizione-tipo-in-haskell) in [Haskell](Haskell.md#^definizione-haskell) usato per rappresentare i numeri interi%% link %% (in inglese _integer numbers_) ma, a differenza del [tipo `Int`](Tipizzazione%20in%20Haskell.md#^definizione-tipo-int), non è _bounded_%% link %% e, quindi, può essere usato per rappresentare numeri molto più grandi o più piccoli.
^definizione-tipo-integer

%% 
Quindi perché non usiamo sempre `Integer` al posto di `Int`? qual è il vantaggio di `Int`?
%%

%%
```haskell
factorial :: Integer -> Integer  
factorial n = product [1..n]  

ghci> factorial 50  
30414093201713378043612608166064768844377641568960512000000000000 
```
%%

> [!definizione]+ Definizione: tipo `Float`
> 
> **`Float`** è un [tipo](Tipizzazione%20in%20Haskell.md#^definizione-tipo-in-haskell) in [Haskell](Haskell.md#^definizione-haskell) usato per rappresentare i numeri reali a virgola mobile%% Link %% (in inglese _real floating point_) con precisione singola%% link %%.
^definizione-tipo-float

%% 
```haskell
circumference :: Float -> Float  
circumference r = 2 * pi * r  

ghci> circumference 4.0  
25.132742  
```
%%

> [!definizione]+ Definizione: tipo `Double`
> 
> **`Double`** è un [tipo](Tipizzazione%20in%20Haskell.md#^definizione-tipo-in-haskell) in [Haskell](Haskell.md#^definizione-haskell) usato per rappresentare i numeri reali a virgola mobile%% Link %% (in inglese _real floating point_) con precisione doppia%% link %% (da qui il nome del tipo).
^definizione-tipo-double

%% 
```haskell
circumference' :: Double -> Double  
circumference' r = 2 * pi * r  

ghci> circumference' 4.0  
25.132741228718345  
```
%%

> [!definizione]+ Definizione: tipo `Bool`
> 
> **`Bool`** è un [tipo](Tipizzazione%20in%20Haskell.md#^definizione-tipo-in-haskell) in [Haskell](Haskell.md#^definizione-haskell) usato per rappresentare i valori booleani di verità%% link %%. Può assumere solo i valori%% link %% `True` e `False`.
^definizione-tipo-bool

> [!definizione]+ Definizione: tipo `Char`
> 
> **`Char`** è un [tipo](Tipizzazione%20in%20Haskell.md#^definizione-tipo-in-haskell) in [Haskell](Haskell.md#^definizione-haskell) usato per rappresentare i caratteri, delimitati da singole virgolette `''`.
^definizione-tipo-char

%% 
Tuples are types but they are dependent on their length as well as the types of their components, so there is theoretically an infinite number of tuple types, which is too many to cover in this tutorial. Note that the empty tuple () is also a type which can only have a single value: ()
 %%

# 1 - Variabili di tipi

Secondo te qual è il [tipo](Tipizzazione%20in%20Haskell.md#^definizione-tipo-in-haskell) della [funzione `head`](Sintassi%20di%20base%20di%20Haskell.md#^definizione-funzione-head)? Non è una domanda banale, perché [`head`](Sintassi%20di%20base%20di%20Haskell.md#^definizione-funzione-head) prende una [lista](Sintassi%20di%20base%20di%20Haskell.md#^definizione-lista-in-haskell) di un [tipo](Tipizzazione%20in%20Haskell.md#^definizione-tipo-in-haskell) qualsiasi ne restituisce il primo elemento, quindi quale [tipo](Tipizzazione%20in%20Haskell.md#^definizione-tipo-in-haskell) assume? Controlliamo su [GHCi](Haskell.md#^definizione-ghci):

```haskell
ghci> :t head  
head :: [a] -> a  
```

Hmmm! What is this `a`? Is it a type? Remember that we previously stated that types are written in capital case, so it can’t exactly be a type. Because it’s not in capital case it’s actually a **type variable**. That means that `a` can be of any type. This is much like generics in other languages, only in Haskell it’s much more powerful because it allows us to easily write very general functions if they don’t use any specific behavior of the types in them. Functions that have type variables are called **polymorphic functions**. The type declaration of `head` states that it takes a list of any type and returns one element of that type.

> [!definizione]+ Definizione: variabile di tipo
> 
> In [Haskell](Haskell.md#^definizione-haskell) una **variabile di tipo** è un segnaposto generico nel [tipo](Tipizzazione%20in%20Haskell.md#^definizione-tipo-in-haskell) di una [funzione](Sintassi%20di%20base%20di%20Haskell.md#^definizione-funzione-in-haskell) o struttura dati%% link %%e generalmente si indica con una singola lettera minuscola (`a`, `b`, `c`, ...).
^definizione-variabile-di-tipo

> [!definizione]+ Definizione: funzione polimorfica
> 
> In [Haskell](Haskell.md#^definizione-haskell) una **funzione polimorfica** è una [funzione](Sintassi%20di%20base%20di%20Haskell.md#^definizione-funzione-in-haskell) che nel suo [tipo](Tipizzazione%20in%20Haskell.md#^definizione-tipo-in-haskell) contiene [variabili di tipo](Tipizzazione%20in%20Haskell.md#^definizione-variabile-di-tipo).
^definizione-funzione-polimorfica

Remember fst? It returns the first component of a pair. Let’s examine its type.

```haskell
ghci> :t fst  
fst :: (a, b) -> a  
```

We see that fst takes a tuple which contains two types and returns an element which is of the same type as the pair’s first component. That’s why we can use fst on a pair that contains any two types. Note that just because a and b are different type variables, they don’t have to be different types. It just states that the first component’s type and the return value’s type are the same.

# 2 - Classi di tipi

> [!definizione]+ Definizione: classe di tipo
> 
> In [Haskell](Haskell.md#^definizione-haskell) una **classe di tipo** è un insieme di [tipi](Tipizzazione%20in%20Haskell.md#^definizione-tipo-in-haskell) che condividono un insieme di operazioni.
^definizione-classe-di-tipo

%% 
A lot of people coming from OOP get confused by typeclasses because they think they are like classes in object-oriented languages. Well, they’re not. You can think of them kind of as Java interfaces, only better.
%%

Qual è il [tipo](Tipizzazione%20in%20Haskell.md#^definizione-tipo-in-haskell) della funzione `==`%% link %%? Controlliamo su [GHCi](Haskell.md#^definizione-ghci):

```haskell
ghci> :t (==)  
(==) :: (Eq a) => a -> a -> Bool  
```

%% 
**Note**: the equality operator, `==` is a function. So are `+`, `*`, `-`, `/` and pretty much all operators. If a function name is comprised only of special characters, it’s considered an infix function by default. If we want to examine its type, pass it to another function or call it as a prefix function, we have to surround it in parentheses.
%%

Interesting. We see a new thing here, the `=>` symbol. Everything before the `=>` symbol is called a **class constraint**. We can read the previous type declaration like this: the equality function takes any two values that are of the same type and returns a `Bool`. The type of those two values must be a member of the `Eq` class (this was the class constraint).

> [!definizione]+ Definizione: vincolo di classe
> 
> In [Haskell](Haskell.md#^definizione-haskell) un **vincolo di classe** è un'affermazione che precede il [tipo](Tipizzazione%20in%20Haskell.md#^definizione-tipo-in-haskell) di una [funzione](Sintassi%20di%20base%20di%20Haskell.md#^definizione-funzione-in-haskell) e dichiara quali [classi di tipo](Tipizzazione%20in%20Haskell.md#^definizione-classe-di-tipo) una [variabile di tipo](Tipizzazione%20in%20Haskell.md#^definizione-variabile-di-tipo) deve soddisfare perché la [funzione](Sintassi%20di%20base%20di%20Haskell.md#^definizione-funzione-in-haskell) possa essere usata.
> 
> Nella firma di tipo%% link %% è inserito tra l'operatore `::`%% link %% e il [tipo](Tipizzazione%20in%20Haskell.md#^definizione-tipo-in-haskell) (da cui è separato dall'operatore `=>`):
> 
> ```haskell
> (==) :: (Eq a) => a -> a -> Bool
> ```
> 
> In questo caso indica che la funzione `==`%% link %% contiene nel suo [tipo](Tipizzazione%20in%20Haskell.md#^definizione-tipo-in-haskell) una [variabile di tipo](Tipizzazione%20in%20Haskell.md#^definizione-variabile-di-tipo) `a` che però deve appartenere alla [classe di tipo](Tipizzazione%20in%20Haskell.md#^definizione-classe-di-tipo) `Eq`.
^definizione-vincolo-di-classe

%%
Nel caso di più **vincoli di classe**, si elencano tra parentesi separati da virgole.
%%

Vediamo alcune [classi di tipo](Tipizzazione%20in%20Haskell.md#^definizione-classe-di-tipo).

> [!definizione]+ Definizione: classe di tipo `Eq`
> 
> **`Eq`** è una [classe di tipo](Tipizzazione%20in%20Haskell.md#^definizione-classe-di-tipo) su cui è definita l'uguaglianza strutturale%% link %% e appartiene a essa qualsiasi [tipo](Tipizzazione%20in%20Haskell.md#^definizione-tipo-in-haskell) i cui valori%% link %% possono essere confrontati tra loro con le funzioni `==`%% link %% e `/=`%% link %%.
^definizione-classe-di-tipo-eq

> [!definizione]+ Definizione: classe di tipo `Ord`
> 
> **`Ord`** è una [classe di tipo](Tipizzazione%20in%20Haskell.md#^definizione-classe-di-tipo) a cui appartiene qualsiasi [tipo](Tipizzazione%20in%20Haskell.md#^definizione-tipo-in-haskell) i cui valori possono essere ordinati%% link %% tra loro, per esempio usando gli operatori%% Link %% `>`, `<`, `>=` e `<=`%% link a tutti %%.
^definizione-classe-di-tipo-ord

> [!definizione]+ Definizione: tipo `Ordering`
> 
> **`Ordering`** è un [tipo](Tipizzazione%20in%20Haskell.md#^definizione-tipo-in-haskell) in [Haskell](Haskell.md#^definizione-haskell) usato per rappresentare il confronto tra due valori. Può assumere solo i seguenti tre valori:
> - `LT`: sta per _less than_ (in italiano _minore di_) e indica che il primo valore è minore del secondo.
> - `EQ`: sta per _equal to_ (in italiano _uguale a_) e indica che i due valori sono uguali.
> - `GT`: sta per _greater than_ (in italiano _maggiore di_) e indica che il primo valore è maggiore del secondo.
> 
> Viene usato principalmente nella [funzione `compare`](Tipizzazione%20in%20Haskell.md#^definizione-funzione-compare).
^definizione-tipo-ordering

> [!definizione]+ Definizione: funzione `compare`
>
> La **funzione%% link %% `compare`** prende due valori dello stesso [tipo](Tipizzazione%20in%20Haskell.md#^definizione-tipo-in-haskell) appartenente alla [classe di tipo `Ord`](Tipizzazione%20in%20Haskell.md#^definizione-classe-di-tipo-ord) e restituisce un [`Ordering`](Tipizzazione%20in%20Haskell.md#^definizione-tipo-ordering) che descrive la relazione d'ordine tra i due:
>
> ```haskell
> ghci> compare 3 5
> LT
> ghci> compare 5 5
> EQ
> ghci> compare 7 5
> GT
> ```
^definizione-funzione-compare

%%
**Definizione nella libreria standard:**

```haskell
class Eq a where
  (==) :: a -> a -> Bool
  (/=) :: a -> a -> Bool
  x /= y = not (x == y)   -- implementazione di default
```

`(/=)` ha già un'implementazione di default in termini di `(==)`, quindi per creare un'istanza basta definire solo `(==)`.

---

**Esempio di istanza:**

```haskell
data Stagione = Primavera | Estate | Autunno | Inverno

instance Eq Stagione where
  Primavera == Primavera = True
  Estate    == Estate    = True
  Autunno   == Autunno   = True
  Inverno   == Inverno   = True
  _         == _         = False
```

---

**`deriving`**

Per tipi semplici Haskell può generare l'istanza automaticamente:

```haskell
data Stagione = Primavera | Estate | Autunno | Inverno
  deriving Eq
```

Il compilatore confronta i costruttori uno a uno — due valori sono uguali se e solo se sono costruiti con lo stesso costruttore e tutti i loro campi sono uguali.

---

**Cosa *non* è `Eq`**

Non tutti i tipi possono avere un'istanza di `Eq`. Le funzioni, per esempio, non ce l'hanno — non esiste un modo generale per stabilire se due funzioni sono uguali (è un problema indecidibile). Quindi `Int -> Int` non appartiene a `Eq`, e scrivere `f == g` per due funzioni è un errore di compilazione.
%%

%% 
L'**uguaglianza strutturale** confronta due valori guardando *come sono costruiti* — pezzo per pezzo, ricorsivamente — piuttosto che confrontare, ad esempio, un indirizzo in memoria.

Due valori sono strutturalmente uguali se:
- hanno lo stesso **costruttore**
- e tutti i loro **campi** sono ricorsivamente uguali

---

**Esempio:**

```haskell
data Albero = Foglia | Nodo Albero Int Albero

t1 = Nodo (Nodo Foglia 3 Foglia) 5 Foglia
t2 = Nodo (Nodo Foglia 3 Foglia) 5 Foglia
t3 = Nodo Foglia 5 Foglia
```

`t1 == t2` \to `True` — stessa struttura, stessi valori  
`t1 == t3` \to `False` — il sottoalbero sinistro è diverso

Non importa se `t1` e `t2` sono due oggetti distinti in memoria — ciò che conta è la forma.

---

**Contrasto con altri tipi di uguaglianza**

| tipo di uguaglianza | confronta | esempio |
|---|---|---|
| strutturale | la forma e i valori | Haskell `(==)`, Python `==` |
| referenziale | l'indirizzo in memoria | Java `==` su oggetti, Python `is` |
| semantica | il significato astratto | due `Set` con gli stessi elementi ma struttura interna diversa |

In Haskell l'uguaglianza referenziale non è esposta al programmatore per design — i valori sono immutabili e l'identità in memoria è irrilevante. `Eq` implementa sempre uguaglianza strutturale (o al più semantica, come nel caso di `Set`).

The `Eq` typeclass provides an interface for testing for equality. Any type where it makes sense to test for equality between two values of that type should be a member of the `Eq` class. All standard Haskell types except for IO (the type for dealing with input and output) and functions are a part of the `Eq` typeclass.
%%

> [!definizione]+ Definizione: classe di tipo `Show`
>
> **`Show`** è una [classe di tipo](Tipizzazione%20in%20Haskell.md#^definizione-classe-di-tipo) a cui appartiene qualsiasi [tipo](Tipizzazione%20in%20Haskell.md#^definizione-tipo-in-haskell) i cui valori possono essere convertiti in una [stringa](Sintassi%20di%20base%20di%20Haskell.md#^definizione-stringa-in-haskell), per esempio tramite la funzione%% link %% `show`.
^definizione-classe-di-tipo-show

> [!definizione]+ Definizione: classe di tipo `Read`
>
> **`Read`** è una [classe di tipo](Tipizzazione%20in%20Haskell.md#^definizione-classe-di-tipo) a cui appartiene qualsiasi [tipo](Tipizzazione%20in%20Haskell.md#^definizione-tipo-in-haskell) i cui valori possono essere ottenuti dal parsing%% link %% di una [stringa](Sintassi%20di%20base%20di%20Haskell.md#^definizione-stringa-in-haskell), per esempio tramite la funzione%% link %% `read`. È in un certo senso l'inverso di `Show`.
^definizione-classe-di-tipo-read

> [!definizione]+ Definizione: funzione `show`
>
> La **funzione `show`** prende un valore di qualsiasi tipo appartenente alla [classe di tipo `Show`](Tipizzazione%20in%20Haskell.md#^definizione-classe-di-tipo-show) e restituisce la sua rappresentazione come [stringa](Sintassi%20di%20base%20di%20Haskell.md#^definizione-stringa-in-haskell):
>
> ```haskell
> ghci> show 42
> "42"
> ghci> show 3.14
> "3.14"
> ghci> show True
> "True"
> ```

> [!definizione]+ Definizione: funzione `read`
>
> La **funzione `read`** prende una [stringa](Sintassi%20di%20base%20di%20Haskell.md#^definizione-stringa-in-haskell) e la converte in un valore di qualsiasi tipo appartenente alla [classe di tipo `Read`](Tipizzazione%20in%20Haskell.md#^definizione-classe-di-tipo-read). È l'inverso di `show` e richiede spesso un'annotazione di tipo%% link %% esplicita per disambiguare il tipo restituito:
>
> ```haskell
> ghci> read "42" :: Int
> 42
> ghci> read "3.14" :: Double
> 3.14
> ghci> read "True" :: Bool
> True
> ```

%% 
Read is sort of the opposite typeclass of Show. The read function takes a string and returns a type which is a member of Read.

```haskell
ghci> read "True" || False  
True  
ghci> read "8.2" + 3.8  
12.0  
ghci> read "5" - 2  
3  
ghci> read "[1,2,3,4]" ++ [3]  
[1,2,3,4,3]  
```

So far so good. Again, all types covered so far are in this typeclass. But what happens if we try to do just read "4"?

```haskell
ghci> read "4"  
<interactive>:1:0:  
	Ambiguous type variable `a' in the constraint:  
	  `Read a' arising from a use of `read' at <interactive>:1:0-7  
	Probable fix: add a type signature that fixes these type variable(s)  
```

What GHCi is telling us here is that it doesn’t know what we want in return. Notice that in the previous uses of read we did something with the result afterwards. That way, GHCi could infer what kind of result we wanted out of our read. If we used it as a boolean, it knew it had to return a Bool. But now, it knows we want some type that is part of the Read class, it just doesn’t know which one. Let’s take a look at the type signature of read.

```haskell
ghci> :t read  
read :: (Read a) => String -> a  
```

See? It returns a type that’s part of Read but if we don’t try to use it in some way later, it has no way of knowing which type. That’s why we can use explicit type annotations. Type annotations are a way of explicitly saying what the type of an expression should be. We do that by adding :: at the end of the expression and then specifying a type. Observe:

```haskell
ghci> read "5" :: Int  
5  
ghci> read "5" :: Float  
5.0  
ghci> (read "5" :: Float) * 4  
20.0  
ghci> read "[1,2,3,4]" :: [Int]  
[1,2,3,4]  
ghci> read "(3, 'a')" :: (Int, Char)  
(3, 'a')  
```

Most expressions are such that the compiler can infer what their type is by itself. But sometimes, the compiler doesn’t know whether to return a value of type Int or Float for an expression like read "5". To see what the type is, Haskell would have to actually evaluate read "5". But since Haskell is a statically typed language, it has to know all the types before the code is compiled (or in the case of GHCi, evaluated). So we have to tell Haskell: "Hey, this expression should have this type, in case you don’t know!".
%%

> [!definizione]+ Definizione: classe di tipo `Enum`
>
> **`Enum`** è una [classe di tipo](Tipizzazione%20in%20Haskell.md#^definizione-classe-di-tipo) a cui appartiene qualsiasi [tipo](Tipizzazione%20in%20Haskell.md#^definizione-tipo-in-haskell) i cui valori sono enumerabili%% link %%, ovvero hanno un predecessore e un successore ben definiti. Questo permette di usarli nelle range notation%% link %% delle liste, come `[LT .. GT]` o `['a' .. 'z']`.

%% 
They also have defined successors and predecessors, which you can get with the `succ` and `pred` functions. Types in this class: `()`, `Bool`, `Char`, `Ordering`, `Int`, `Integer`, `Float` and `Double`.

```haskell
ghci> ['a'..'e']  
"abcde"  
ghci> [LT .. GT]  
[LT,EQ,GT]  
ghci> [3 .. 5]  
[3,4,5]  
ghci> succ 'B'  
'C'  
```
%%

> [!definizione]+ Definizione: classe di tipo `Bounded`
>
> **`Bounded`** è una [classe di tipo](Tipizzazione%20in%20Haskell.md#^definizione-classe-di-tipo) a cui appartiene qualsiasi [tipo](Tipizzazione%20in%20Haskell.md#^definizione-tipo-in-haskell) che ha un valore minimo e un valore massimo%% link %%, accessibili tramite le funzioni%% link %% `minBound` e `maxBound`.

%% 
```haskell
ghci> minBound :: Int  
-2147483648  
ghci> maxBound :: Char  
'\1114111'  
ghci> maxBound :: Bool  
True  
ghci> minBound :: Bool  
False  
```

`minBound` and `maxBound` are interesting because they have a type of `(Bounded a) => a`. In a sense they are polymorphic constants.

All tuples are also part of `Bounded` if the components are also in it.

```haskell
ghci> maxBound :: (Bool, Int, Char)  
(True,2147483647,'\1114111')  
```
%%

> [!definizione]+ Definizione: classe di tipo `Num`
>
> **`Num`** è una [classe di tipo](Tipizzazione%20in%20Haskell.md#^definizione-classe-di-tipo) a cui appartiene qualsiasi [tipo](Tipizzazione%20in%20Haskell.md#^definizione-tipo-in-haskell) numerico%% link %% i cui valori supportano le operazioni aritmetiche%% link %% di base, come `+`, `-` e `*`%% link a tutti %%.

%% 
```haskell
ghci> :t 20  
20 :: (Num t) => t  
```

It appears that whole numbers are also polymorphic constants. They can act like any type that’s a member of the Num typeclass.

    ghci> 20 :: Int  
    20  
    ghci> 20 :: Integer  
    20  
    ghci> 20 :: Float  
    20.0  
    ghci> 20 :: Double  
    20.0  

Those are types that are in the Num typeclass. If we examine the type of *, we’ll see that it accepts all numbers.

    ghci> :t (*)  
    (*) :: (Num a) => a -> a -> a  

It takes two numbers of the same type and returns a number of that type. That’s why (5 :: Int) * (6 :: Integer) will result in a type error whereas 5 * (6 :: Integer) will work just fine and produce an Integer because 5 can act like an Integer or an Int.

To join Num, a type must already be friends with Show and Eq.
%%

> [!definizione]+ Definizione: classe di tipo `Integral`
>
> **`Integral`** è una [classe di tipo](Tipizzazione%20in%20Haskell.md#^definizione-classe-di-tipo) a cui appartiene qualsiasi [tipo](Tipizzazione%20in%20Haskell.md#^definizione-tipo-in-haskell) numerico intero%% link %%, come `Int` e `Integer`. Estende `Num`%% link %% e aggiunge la divisione intera%% link %% e il modulo%% link %% tramite le funzioni%% link %% `div` e `mod`.

> [!definizione]+ Definizione: classe di tipo `Floating`
>
> **`Floating`** è una [classe di tipo](Tipizzazione%20in%20Haskell.md#^definizione-classe-di-tipo) a cui appartiene qualsiasi [tipo](Tipizzazione%20in%20Haskell.md#^definizione-tipo-in-haskell) numerico in virgola mobile%% link %%, come `Float` e `Double`. Estende `Num`%% link %% e aggiunge operazioni matematiche avanzate%% link %% come `sqrt`, `sin`, `cos` e `**`%% link a tutti %%.

%% 
A very useful function for dealing with numbers is `fromIntegral`. It has a type declaration of `fromIntegral :: (Num b, Integral a) => a -> b`. From its type signature we see that it takes an integral number and turns it into a more general number. That’s useful when you want integral and floating point types to work together nicely. For instance, the `length` function has a type declaration of `length :: [a] -> Int` instead of having a more general type of `(Num b) => length :: [a] -> b`. If we try to get a length of a list and then add it to `3.2`, we’ll get an error because we tried to add together an `Int` and a floating point number. So to get around this, we do `fromIntegral (length [1,2,3,4]) + 3.2` and it all works out.

Notice that `fromIntegral` has several class constraints in its type signature. That’s completely valid and as you can see, the class constraints are separated by commas inside the parentheses.
%%

%%
**Sintassi:**

```haskell
class Eq a where
  (==) :: a -> a -> Bool
  (/=) :: a -> a -> Bool
```

Questo dice: "un tipo `a` appartiene alla classe `Eq` se fornisce un'implementazione di `==` e `/=`."

---

**Istanza — dichiarare che un tipo appartiene a una classe:**

```haskell
data Colore = Rosso | Verde | Blu

instance Eq Colore where
  Rosso == Rosso = True
  Verde == Verde = True
  Blu   == Blu   = True
  _     == _     = False
```

---

**Vincoli sulle variabili di tipo**

Le classi di tipo si combinano con le variabili di tipo per esprimere vincoli:

```haskell
elem :: Eq a => a -> [a] -> Bool
```

`Eq a =>` è un **vincolo**: "`a` può essere qualsiasi tipo, *purché* appartenga a `Eq`." Senza quel vincolo il compilatore non saprebbe come confrontare gli elementi.

---

**Classi predefinite fondamentali:**

| classe | operazioni | esempio di istanze |
|---|---|---|
| `Eq` | `==`, `/=` | `Int`, `Bool`, `String` |
| `Ord` | `<`, `>`, `compare` | `Int`, `Char` |
| `Show` | `show` (\to stringa) | quasi tutto |
| `Read` | `read` (← stringa) | quasi tutto |
| `Num` | `+`, `*`, `negate` | `Int`, `Double` |
| `Functor` | `fmap` | `[]`, `Maybe`, `IO` |

---

**Classe di tipo vs interfaccia OOP**

Sembrano simili ma ci sono differenze importanti:

- In OOP l'interfaccia è dichiarata *insieme* alla classe. In Haskell puoi aggiungere un'istanza a un tipo *esistente*, anche di una libreria esterna.
- In Haskell non c'è ereditarietà di dati — solo di comportamento (tramite **superclassi**: `Ord` richiede `Eq`).
- Le istanze vengono risolte staticamente a compile time, non dinamicamente a runtime.
%%

%% 
The `elem` function has a type of `(Eq a) => a -> [a] -> Bool` because it uses `==` over a list to check whether some value we’re looking for is in it.
%%

---

> [!fonti]+ Fonti
> 
> - 📚 Miran Lipovača, _Learn You a Haskell for Great Good!_:
> 	- [3 - _Types and Typeclasses_](https://learnyouahaskell.github.io/types-and-typeclasses.html).
