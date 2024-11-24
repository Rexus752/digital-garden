---
draft: true
---
Una **struttura dati** è un'entità usata per organizzare un insieme di dati all'interno della memoria del computer. Ogni tipo di struttura dati è progettato per ottimizzare l'accesso e la manipolazione dei dati in contesti specifici e la scelta delle strutture dati da utilizzare è strettamente legata a quella degli algoritmi; per questo, spesso essi vengono considerati insieme. Infatti, la scelta della struttura dati influisce inevitabilmente sull'efficienza computazionale degli algoritmi che la manipolano.

# Strutture dinamiche

## Insiemi dinamici

Sono collezioni di elementi. Caratteristiche:
- Numero finito di elementi
- Elementi modificabili (ecco perché è una struttura dinamica)
- Numero di elementi variabile durante l'esecuzione (ecco perché è una struttura dinamica)
- Ogni elemento ha una chiave che lo identifica
- Le chiavi sono univoche (non esistono duplicati di chiavi)

Operazioni di due tipi:
- Interrogazioni (query)
	- Ricerca
- Modifiche
	- Inserimento
	- Cancellazione

Operazioni tipiche in caso di chiavi estratte da insiemi totalmente ordinati:
- Ricerca del massimo
- Ricerca del minimo
- Ricerca del prossimo elemento più grande (successor)
- Ricerca del prossimo elemento più piccolo (predecessor)

# Complessità delle operazioni

La complessità è misurata in funzione della dimensione dell'insieme e dipende da che tipo di struttura dati si utilizza per rappresentare l'insieme dinamico.

Un’operazione molto costosa con una certa struttura dati può costare poco con un’altra.

Quali operazioni sono necessarie dipende dall’applicazione.

# Array

Un array è una sequenza di caselle:
• ogni casella può contenere un elemento dell’insieme
• le caselle hanno ognuna la stessa dimensione e sono allocate in memoria consecutivamente

Definizioni:
- Base: indirizzo in memoria del primo elemento
- A[i] = valore dell'indirizzo base + i * sizeof(valore)

Con l'accesso diretto il tempo di lettura e scrittura in una cella è O(1)

## Array statico

Un array statico è un array in cui il numero massimo di elementi è prefissato:
• $M$ denota il numero massimo di elementi (dimensione fisica)
• $N$ denota il numero attuale di elementi (dimensione logica)
• gli $N$ elementi occupano sempre le prime $N$ celle del array
Ci interessa studiare
• quanto costano le varie operazioni
• quando conviene utilizzare questo tipo di array

Una delle opzioni per rappresentare le collezioni (insiemi dinamici)

![](Pasted%20image%2020241104181657.png)

- A[i] è l'elemento alla posizione i
- Il primo elemento è $A[0]$
- $A.M$ è la dimensione fisica dell'array
	- Lo spazio fisico dell'array va da $A[0]$ a $A[M-1]$
- $A.N$ è la dimensione logica dell'array (cioè è la cardinalità della collezione)
	- Lo spazio logico dell'array va da $A[0]$ a $A[N-1]$
	- $A[N]$ è il primo elemento che non fa parte dell'array
- Invariante: $0 \le N \le M$

### Inserimento

```
Array-Insert(A, key)
if A.N < A.M then
	A.N <- A.N + 1
	A[N] <- key
	return A.N
else
	return nil
end if
```

L'inserimento ha costo $O(1)$.

Problema: in questo modo ci possono essere ripetizioni, non controlla se la chiave (cioè l'elemento da inserire) è univoca.

Se si implementa con la chiave univoca, diventa O(n)

### Cancellazione

#### Fase 1

```
Array-Delete(A, key)
for i <- 1 to A.N do
	if A[i] = key then
		A.N <- A.N - 1
		for j <- i to A.N do
			A[j] <- A[j + 1]
		end for
	end if
end for
```

Questo algoritmo ha tempo O(N^2), non va bene
%%Assume che le chiavi non sono univoche (?)%%

#### Fase 2

```
Array-Delete(A, key)
deleted <- 0
for i <- 1 to A.N do
	if A[i] = key then
		deleted <- deleted + 1
	else
		A[i - deleted] <- A[i]
	end if
	end for
A.N <- A.N - deleted
```

Questa versione ha tempo O(N) 

### Ricerca

```
Array-Search(A, key)
for i <- 1 to A.N do
	if A[i] = key then
		return i
	end if
end for
return nil
```

Array-Search è O(N) ed è ottimo perché la ricerca in un array non ordinato è Ω(n)

### Riassunto

Riassumendo:
• Inserimento in tempo O(1) (con ridondanza)
• Cancellazione in tempo O(N)
• Ricerca in tempo O(N)

### Array statico ordinato

E se l'array fosse ordinato?

Possiamo avere:
• Ricerca in tempo O(log N) (usando Binary-Search)
• Cancellazione con duplicati in tempo O(N) perché non posso fare di meglio (ho bisogno di scansionare tutti gli elementi dell'array per vedere se non ci sono più elementi da cancellare)
• L’inserimento ?

```
Array-InsertOrd(A, key)
if A.N < A.M then
	A.N <- A.N + 1
	A[N] <- key
	i <- N
	while i > 1 \land A[i - 1] > A[i] do
		# Qual è l'invariante?
		scambia A[i - 1] e A[i]
	end while
	return i
else
	return nil
end if
```

Questo inserimento ha tempo O(n)

Domande:
- come si fa e quanto costa cercare il minimo e il massimo in un array ordinato?
- come si fa e quanto costa cercare il minimo e il massimo in un array non ordinato?
- come si realizzano e che complessità hanno le operazioni successor e predecessor in array ordinati e non ordinati?

Mantenendo l’array ordinato ci si guadagna in tutti i casi salvo in quello dell’inserimento

## Array ridimensionabile

Cosa si può fare se non si conosce a priori il numero massimo di elementi (oppure se non si vuole sprecare spazio allocando molta più memoria del necessario)?
Risposta: si può “espandere” l’array quando risulti troppo piccolo …

Ma come si “espande” un array?
Risposta: Non si ridimensiona per davvero, ma ogni volta che si cambia la dimensione, si copia il contenuto del vecchio array in un array + grande

```
Array-Extend(A, n)
B <- un array dimensione A.M + n
B.M <- A.M + n
B.N <- A.N
for i <- 1 to A.N do
	B[i] <- A[i]
end for
return B
```

il tempo dell'operazione di estensione è O(N)

## Prima idea

1. allochiamo inizialmente spazio per 𝑀 elementi (array di lunghezza 𝑀)
2. quando viene aggiunto un elemento, se l’array è pieno, espandiamo l’array di una cella
3. espandere costa tempo perché richiede di allocare memoria e copiare gli elementi dell’array

```
Pre-cond: A.N <= A.M

Dyn-Array-Insert-1(A, key)
if A.N = A.M then
	A <- Array-Extend(A, 1)
end if
return Array-Insert(A, key)
```

Ciò significa che, arrivati al limite dell'array dopo la prima allocazione, per ogni nuovo inserimento verrà usata la funzione array-extend (che ha costo O(N)).
Si può notare che non conviene espandere l'array di 1 per ogni singolo inserimento: abbiamo bisogno di un concetto nuovo di costo, che dipenda dalla “storia” degli inserimenti

## Seconda idea

- problema della prima idea: se N = M allora successivi inserimenti richiedono altrettante allocazioni
- quando occorre, allocare più spazio di quanto strettamente necessario, in previsione di ulteriori inserimenti

quindi ecco cosa fare:
- inizialmente allochiamo un array di M elementi
- quando l’array è pieno ne allochiamo uno nuovo di 2M elementi
- quando il numero di elementi si riduce ad ¼ della dimensione, riallochiamo un array di dimensione ½ M

```
Pre-cond: A.N <= A.M
Dyn-Array-Insert-2(A, key)
if A.N = A.M then
	A <- Array-Extend(A, A.M)
end if
return Array-Insert(A, key)
```

e

```
Dyn-Array-Delete(A, key)
if A.N <= 1/4 * A.M then
	B <- un array dimensione A.M/2
	B.M <- A.M/2
	B.N <- A.N
	for i <- 1 to A.N do
		B[i] <- A[i]
	end for
	A <- B
end if
```

Tempo ammortizzato:
Per confrontare diverse soluzioni nella realizzazione di ADT si valutano i tempi di una sequenza di operazioni, che determinano ciascuna la dimensione dell’ingresso della successiva
$$
T_{amm}(m) = \frac{1}{m} \sum_{i=1}^m T_i(n_i) = \frac{T_1(n_1) + \ldots + T_m(n_m)}{m}
$$
dove:
- $m$: numero di operazioni nella sequenza
- $n_i$: dimensione dei dati in ingresso dell'$i$-esima operazione
- $T_i(n_i)$: tempo dell'$i$-esima operazione

Idea: attribuiamo a ciascuna operazione la media del costo totale: _metodo dell’aggregazione_

E così, per Dyn-Array-Insert-1 otteniamo:
$$
\begin{align}
T_{amm}(m) &= \frac{1}{m} \sum_{i=1}^m T_{D-Ins}(i) \\
&= \frac{1}{m} \sum_{i=1}^m O(i) \\
&= \frac{O(m^2)}{m} \\
&= O(m)
\end{align}
$$
%%non dovrebbe essere $T_{D-Ins}(n_i)$?%%
Cioè, con Dyn-Array-Insert-1 il tempo ammortizzato di ogni inserimento è lineare
$$
T_{D-Ins}(i) = \begin{cases}
i & \text{se $i-1=2^k$ per qualche $k$} \\
1 & \text{altrimenti}
\end{cases}
$$
![](Dyn-Array-Insert-1.png)

![](Dyn-Array-Insert-1%20Formula.png)

Mentre, per Dyn-Array-Insert-2 otteniamo:
$$
T_{amm}(m) = \frac{1}{m} \sum_{i=1}^m T_{D-Ins}(i) < \frac{3m}{m} = 3
$$
Con Dyn-Array-Insert-2 il tempo ammortizzato di ogni inserimento è costante!

# Liste

Una lista è una sequenza finita di valori:
$$
L = [a_1, a_2, \ldots, a_k]
$$
dove $a_1, a_2, \ldots, a_k \in A$, per qualche insieme $A$.
Se $k = 0$, allora $L = []$, o anche $L = null$, è la lista vuota.

Sia $k \ne 0$:
$$
L = [a_1, a_2, \ldots, a_k]
$$
- $head(L) = a_1$
- $tail(L) = [a_2, \ldots, a_k]$
- $cons(a, [a_1, a_2, \ldots, a_k]) = [a, a_1, a_2, \ldots, a_k]$
- $cons(head(L), tail(L)) = L, \forall L \ne null$

## Definizione induttiva

Fissato un insieme di elementi $A$, l’insieme delle liste su $A$, detta $List(A)$ o semplicemente $List$, è il più piccolo tale che:
- $[]$ (ovvero $null$) $\in List$
- se $a \in A$ e $L \in List$, allora $cons(a, L) \in List$
Confrontiamo questa definizione con quella dei numeri naturali $\mathbb{N}$, che è il più piccolo insieme tale che:
- $0 \in \mathbb{N}$
- se $n \in \mathbb{N}$ allora $succ(n) \in \mathbb{N}$ (dove $succ(n) = n + 1$)

## Liste concatenate

Come struttura dati una lista è una sequenza di record, ciascuno dei quali contiene un campo che punta al successivo.

Funzioni:

```
Cons(x, L)
N.head <- x
N.next <- L
return N
```

```
Head(L)
return L.head
```

```
Tail(L)
return L.next
```

Al fondo di ogni lista c’è la lista vuota, ossia un puntatore a $null$

Lunghezza di una lista ricorsiva:
```
Length-Rec(L)
if IsEmpty(L) then
	return 0
else
	return 1 + Length-Rec(Tail(L))
end if
```

Lunghezza iterativa:
```
Length-Iter(L)
n <- 0
while not IsEmpty(L) do
	L <- Tail(L)
	n <- n + 1
end while
return n
```

Le versioni ricorsiva di coda ed iterativa sono equivalenti in tempo

Ricerca:
```
Search(x, L)
if IsEmpty(L) then
	return false
else
	return Head(L) = x or Search(x, Tail(L))
end if
```
Cioè: se $L ≠ ∅$ allora $x \in L$ solo se $x = Head(L)$ oppure $x \in Tail(L)$

Concatenazione di liste:
```
Append(L, M )
if L = nil then
	return M
else
	L.next <- Append(Tail(L), M )
	return L
end if
```
Append(L, M) ha tempo O(|L|)

Inserimento ricorsivo:
```
Insert(x, i, L)
Post-cond: x inserito davanti all’el. di posto i in L
if i = 1 then
	return Cons(x, L)
else
	L.next <- Insert(x, i - 1, Tail(L))
	return L
end if
```

Cancellazione:
```
DeleteAll(x, L)
Post-cond: ogni occ. di x è rimossa da L
if IsEmpty(L) then
	return nil
else
	if x = Head(L) then
		return DeleteAll(x, Tail(L))
	else
		L.next <- DeleteAll(x, Tail(L))
		return L
	end if
end if
```

Altri algoritmi sulle liste:
Per apprendere come manipolare (ricorsivamente) le liste consideriamo:
• Copia di una lista
• Inversione dell’ordine degli elementi in una lista
• Ricerca, inserimento e cancellazione in una lista ordinata
• Ordinamento di una lista per fusione (Merge-Sort), dopo averla divisa in due metà (circa)

Copia di una lista:
- Una lista è una struttura dati persistente, che può subire modifiche durante l’esecuzione di una procedura
- È allora utile poter duplicare una lista quando si vuole che l’effetto delle modifiche sia solo temporaneo

```
Clone-Iter(L)
R <- Cons(-, nil)
C <- R
while L =/= nil do
	C.next <- Cons(Head(L), nil)
	C <- Tail(C)
	L <- Tail(L)
end while
return Tail(R)
```

```
Clone-Rec(L)
if IsEmpty(L) then
	return nil
else
	return Cons(Head(L), Clone-Rec(Tail(L)))
end if
```

---

Inversione di una lista:
L’inversa della lista: `[1, 2, 3, 4, 5]`
è la lista: `[5, 4, 3, 2, 1]`

Problema: una lista semplice ha un verso solo (quindi l’algoritmo di inversione per un vettore non lo posso adattare)
Idea: Posso “girare” i puntatori mentre scandisco la lista con due puntatori

```
Reverse-Iter(L)
M <- nil
while not IsEmpty(L) do
	T <- Tail(L)
	L.next <- M
	M <- L
	L <- T
end while
return M
```

Come posso definire l’inversa induttivamente?
Idee:
• L’inversa della lista vuota o con un solo elemento è la lista stessa
• L’inversa di una lista [a|L] con almeno due elementi, è l’inversa di L con a aggiunto in fondo

```
Slow-Reverse(L)
if IsEmpty(L) or IsEmpty(Tail(L)) then
	return L
else
	R <- Slow-Reverse(Tail(L))
	return Append(R, Cons(Head(L), nil))
end if
```

Però ha complessità O(n^2)

```
Reverse-Tail-Rec(L, M )
if IsEmpty(L) then
	return M
else
	R <- L
	L <- Tail(L)
	R.next <- M
	return Reverse-Tail-Rec(L, R)
end if
```

Quest'ultimo algoritmo ritorna l’inversa di L davanti ad M
Ha complessità O(n)

```
Reverse-Rec(L)
if IsEmpty(L) or IsEmpty(Tail(L)) then
	return L
else
	R <- Reverse-Rec(Tail(L))
	L.next.next <- L
	L.next <- nil
	return R
end if
```

# Liste ordinate

Possiamo rappresentare insiemi con liste ordinate

Ricerca ordinata:
```
InOrd(x, L)
Pre-cond: L ordinata
Post-cond: ritorna true se x 2 L
if isEmpty(L) or x < Head(L) then
	return false
else
	if x = Head(L) then
		return true
	else
		return InOrd(x, Tail(L))
	end if
end if
```

`if isEmpty(L) or x < Head(L) then`: Se x < Head(L) allora x \notin L

`return InOrd(x, Tail(L))`: allora x > Head(L) quindi x \notin L sse x in Tail(L)

---

Inserimento ordinato:
```
Insert(x, L)
Pre-cond: L ordinata
Post-con: L ordinata e x \in L
if isEmpty(L) or x < Head(L) then
	return Cons(x, L)
else
	if x = Head(L) then
		return L
	else
		L.next <- Insert(x, Tail(L))
		return L
	end if
end if
```

`L.next <- Insert(x, Tail(L))`: Inserimento distruttivo nella coda

---

Cancellazione ordinata:

```
Delete(x, L)
. Pre: L ordinata
. Post: L ordinata e x 6 2 L
if isEmpty(L) or x < Head(L) then
	return L
else
	if x = Head(L) then
		return Tail(L)
	else
		L.next <- Delete(x, Tail(L))
		return L
	end if
end if
```

`return Tail(L)`: Questo valore serve per “ricucire” la lista

`L.next <- Delete(x, Tail(L))`: In questo punto la lista viene ricucita

---

Unione:

```
Union(L, M )
. Pre: L, M ordinate
. Post: ritorna la nuova lista L [ M
if isEmpty(L) then
	return Clone(M)
else
	if isEmpty(M) then
		return Clone(L)
	else
		if Head(L) = Head(M) then
			return Cons(Head(L), Union(Tail(L), Tail(M)))
		else
			if Head(L) < Head(M) then
				return Cons(Head(L), Union(Tail(L), M))
			else # Head(L) > Head(M)
				return Cons(Head(M), Union(L, Tail(M)))
			end if
		end if
	end if
end if
```

Questo algoritmo è O(n)

---

Ordinamento per fusione

Come per i vettori; la fusione è più semplice, un po’ più complicata la divisione:
```
Mergesort(L):
dividi L in due parti uguali, L ed M
L = Mergesort(L)
M = Mergesort(M)
ritorna la fusione ordinata di L ed M
```

```
MergeSort(L)
. Post: L ordinata
if isEmpty(L) or isEmpty(Tail(L)) then
	return L
else
	M <- Split(L) # L ed M sono le due met`a di L
	L <- MergeSort(L)
	M <- MergeSort(M )
	return Merge(L, M )
end if
```

Fondi (Merge)
```
Merge(L, M )
. Pre: L, M ordinate
. Post: ritorna una lista N ordinata modificando i puntatori in L ed M tale che Len(N ) = Len(L) + Len(M )
```

Molto simile a Union: dove sono le differenze?

---

Dividi (Split): prima versione

```
SplitAfter(L, n)  
. Pre: 0 <= n <= Len(L)  
. Post: divide distruttivamente L dopo n elementi ritornandone la seconda parte 
```

```
Split1(L)
n <- Length(L)
return SplitAfter(L, n/2)
```

Questo algoritmo scandisce una volta e mezzo la lista

---

Dividi: seconda versione

Idea: percorriamo la lista con due puntatori, uno dei quali si muova a velocità doppia dell’altro.

---

Dividi: terza versione

Idea: dividiamo la lista unendo gli elementi di posto pari in una nuova lista, e lasciando quelli di posto dispari.

---

Confronto con l’alg. sugli array

Merge Sort su array:
T (n) = 2T (n/2) + n -> T (n) = 2^kT (n/2^k) + kn

Merge Sort su liste
T (n) = 2T (n/2) + 2n -> T (n) = 2^kT (n/2^k) + 2^k n

sostituendo k con log_2 n si ottiene in ambo i casi T(n) \in O(n log n)