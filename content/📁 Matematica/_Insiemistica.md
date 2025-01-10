---
draft: true
---
# Descrizione informale dei principali insiemi numerici

## N

L’insieme dei numeri naturali `e
N = {0, 1, 2, . . .}

N `e incluso propriamente nell’insieme dei numeri interi
Z = {. . . , −2, −1, 0, 1, 2, . . .}

Osservazione:
Qui sopra stiamo estendendo la notazione che abbiamo introdotto per
insiemi finiti {x0, x1, . . . , xn} ad insiemi infiniti. I puntini indicano che
l’elenco degli elementi prosegue indefinitamente in maniera “naturale”. Ad
esempio, possiamo indicare l’insieme dei numeri naturali pari con
{0, 2, 4, 6, . . .} 

## Q

L’insieme Q dei numeri razionali `e l’insieme di tutti i numeri della forma
$$
\frac{n}{m}
$$
con n, m ∈ Z e m̸ = 0. Ogni k ∈ Z pu`o essere scritto come $k/1$ quindi
Z ⊆ Q e poich´e ci sono razionali che non sono interi (ad esempio 1/2 ),
l’inclusione `e propria, cio`e Z ⊊ Q.

## R

Un razionale ha un’espansione decimale finita (per esempio 1/2 = 0,5) oppure un’espansione periodica (per esempio 1/3 = 0,33333 . . .). I numeri la cui espansione decimale `e arbitraria (cio`e finita, periodica o aperiodica) si dicono numeri reali e l’insieme dei numeri reali si denota con R.
Chiaramente Q ⊆ R e l’inclusione `e stretta (ovvero Q ⊊ R) poich´e, ad
esempio, √2 ∈ R \ Q.

Attenzione!
Alcuni numeri ammettono due espansioni decimali diverse: ad esempio 0,99999 . . . e 1 indicano lo stesso numero reale.

# Vedere in che posto ficcare sta roba

Proposizione:
(A \cup B) \ (A \cap B) = (A \ B) \cup (B \ A)

Dimostrazione:
Poiché X \ Y = X \cap \complementY , l'identità pu`o essere riscritta come
(A \cup B) \cap \complement(A \cap B) = (A \cap \complementB) \cup (B \cap \complementA).
Quindi dobbiamo dimostrare che per ogni x
x \in (A \cup B) \cap \complement(A \cap B) \leftrightarrow x \in (A \cap \complementB) \cup (B \cap \complementA),
ovvero
(x \in A \lor x \in B) \land \lnot(x \in A \land x \in B) \leftrightarrow
(x \in A \land \lnot(x \in B)) \lor (x \in B \land \lnot(x \in A)).
Questa è una proposizione del tipo
(P \lor Q) \land \lnot(P \land Q) \leftrightarrow (P \land \lnotQ) \lor (Q \land \lnotP).
Usando le tavole di verità si verifica che tale proposizione è una tautologia,
quindi l'identità insiemistica proposta è corretta.

Lo stesso metodo può essere utilizzato anche per trovare controesempi quando una certa identità booleana non è valida.

Dimostrare (trovando un controesempio) che non vale l'identità
A \cap (B \cup C) = A \cup (B \cap C)
Dato un generico x, dobbiamo verificare che non è vero in generale che
x \in A \cap (B \cup C) \leftrightarrow x \in A \cup (B \cap C),
ovvero
x \in A \land (x \in B \lor x \in C) \leftrightarrow x \in A \lor (x \in B \land x \in C).
Questa è una proposizione del tipo
P \land (Q \lor R) \leftrightarrow P \lor (Q \land R),
dove P, Q e R sono, rispettivamente, "x \in A", "x \in B" e "x \in C".
![](Pasted%20image%2020240928182940.png)



# Proprietà delle operazioni sugli insiemi

## _Proprietà:_ associatività

Dati tre insiemi $A,B,C$, per la proprietà **associativa** degli insiemi valgono le seguenti identità:
- $(A\cap B)\cap C=A\cap (B\cap C)$;
- $(A\cup B)\cup C=A\cup(B\cup C)$.

## _Proprietà:_ idempotenza

Dato un insieme $A$, per la proprietà di **idempotenza** degli insiemi valgono le seguenti identità:
- $A\cap A=A$;
- $A\cap\emptyset=\emptyset$;
- $A\cup A=A$;
- $A\cup\emptyset=A$.

## _Proprietà:_ distributività

Dati tre insiemi $A$, $B$ e $C$, per la proprietà **distributiva** degli insiemi valgono le seguenti identità:
- $(A\cup B)\cap C = (A\cap C) \cup (B \cap C)$;
- $(A\cap B)\cup C = (A\cup C) \cap (B \cup C)$.

### _Dimostrazione:_ $(A\cup B)\cap C = (A\cap C) \cup (B \cap C)$

La prima identità $(A\cup B)\cap C = (A\cap C) \cup (B \cap C)$ si dimostra usando la tecnica della doppia inclusione usata anche per dimostrare l'[uguaglianza di due insiemi](#^Uguaglianza-di-due-insiemi).
Quindi, si deve dimostrare che $(A\cup B)\cap C\subseteq (A\cap C) \cup (B \cap C)$ e $(A\cap C) \cup (B \cap C) \subseteq (A\cup B)\cap C$.

#### Dimostrazione: di $(A\cup B)\cap C\subseteq (A\cap C) \cup (B \cap C)$

- Sia $x \in (A \cup B) \cap C$;
- Sviluppando le definizioni, si trova che $x\in (A \cup B) \land x \in C$, quindi $(x\in A \lor x \in B) \land x \in C$;
- Si può ipotizzare che $x$ si trovi:
	- In $A$, quindi si ha che $x \in A \cap C$;
	- In $B$, quindi si ha che $x \in B \cap C$;
	- Sia in $A$ che in $B$, quindi si ha che $x \in (A \cap C) \cup (B \cap C)$, che può valere anche per i due casi precedenti;
- Si dimostra quindi così che $(A\cup B)\cap C\subseteq (A\cap C) \cup (B \cap C)$.

#### Dimostrazione di $(A\cap C) \cup (B \cap C) \subseteq (A\cup B)\cap C​$

- Sia $x\in(A\cap C) \cup (B \cap C)$;
- Sviluppando le definizioni, si trova che $x\in A \cap C$ oppure $x \in B \cap C$;
- Prendendo il caso di $x\in A\cap C$ (ma vale ugualmente anche per $x \in B \cap C$), si ha che $x$ si deve trovare necessariamente in $A$, quindi $x\in (A\cup B)\cap C$ (perché non importa se $x$ si trova in $A$ e $B$);
- Si dimostra quindi così che $(A\cap C) \cup (B \cap C) \subseteq (A\cup B)\cap C$.

#### Conclusione dimostrazione

Avendo dimostrato quindi entrambe le inclusioni, per la tecnica della doppia inclusione si può affermare che $(A\cup B)\cap C = (A\cap C) \cup (B \cap C)$.
$\blacksquare$

### _Dimostrazione:_ $(A\cap B)\cup C = (A\cup C) \cap (B \cup C)$ 

%%finire di scrivere%%

%%
Dimostrare che A ∩ (B ∪ C) = (A ∩ B) ∪ (A ∩ C)
Dobbiamo dimostrare che per ogni x
x ∈ A ∩ (B ∪ C) ↔ x ∈ (A ∩ B) ∪ (A ∩ C),
ovvero
x ∈ A ∧ (x ∈ B ∨ x ∈ C) ↔ (x ∈ A ∧ x ∈ B) ∨ (x ∈ A ∧ x ∈ C).
Questa è una proposizione della forma
P ∧ (Q ∨ R) ↔ (P ∧ Q) ∨ (P ∧ R),
dove P, Q e R sono, rispettivamente, “x ∈ A”, “x ∈ B” e “x ∈ C”.
Poiché la proposizione precedente è una tautologia (come si può verificare facilmente con le tavole di verità), l’equivalenza è dimostrata.
$\blacksquare$
%%

# Ricoprimento e partizione

## Definizione: ricoprimento

Dati un insieme $X$ e una famiglia di sottoinsiemi $\mathcal A$ di $X$, allora la famiglia $\mathcal A$ si definisce un _**ricoprimento**_ di $X$ se l'unione di tutti gli $n$ insiemi $A_i$ della famiglia dà come risultato $X$:
$$
\bigcup_{i = 1}^n A_i = X
$$

### Esempio: ricoprimento di $\mathbb{R}$ con 3 sottoinsiemi

Dati un insieme $X = \mathbb{R}$ e una famiglia $\mathcal A=\{A_1,A_2,A_3\}$ con $A_1=\{x\in\mathbb{R} : x<0\}$, $A_2=\{x\in\mathbb{R} : x>0\}$ e $A_3=\{x\in\mathbb{R} : -1<x<1\}$, allora la famiglia $\mathcal A$ è un ricoprimento di $X$ perché comprende qualsiasi numero reale $x$ in $\mathbb{R}$:
- Se $x$ è negativo, allora è compreso in $A_1=\{x\in\mathbb{R} : x<0\}$;
- Se $x$ è positivo, allora è compreso in $A_2=\{x\in\mathbb{R} : x>0\}$;
- Se $x=0$, allora è compreso in $A_3=\{x\in\mathbb{R} : -1<x<1\}$.

### Esempio: ricoprimento di $\mathbb{R}$ con infiniti sottoinsiemi

Dati un insieme $X=\mathbb{R}$ e una famiglia di insiemi $\mathcal A$ con $A_n=[n,n+1]$, allora la famiglia $\mathcal A$ è un ricoprimento di $X$ perché, per un qualsiasi indice $n\in\mathbb{Z}$, esisterà un insieme $A_n$ i cui elementi saranno tutti quei numeri reali compresi nell'intervallo $[n,n+1]$ con gli estremi inclusi. In questo modo, si riesce a ricoprire l'intero insieme $X$ (e quindi $\mathbb{R}$).

### Esempio: ricoprimento di $\mathbb{R}$ con infiniti sottoinsiemi

Dati un insieme $X=\mathbb{R}$ e una famiglia di insiemi $\mathcal A$ con $A_n=[n,n+1]$, allora la famiglia $\mathcal A$ è un ricoprimento di $X$ perché, per un qualsiasi indice $n\in\mathbb{Z}$, esisterà un insieme $A_n$ i cui elementi saranno tutti quei numeri reali compresi nell'intervallo $[n,n+1]$ con gli estremi inclusi. In questo modo, si riesce a ricoprire l'intero insieme $X$ (e quindi $\mathbb{R}$).

## Definizione: partizione

Dati un insieme $X$ e una famiglia di insiemi $\mathcal A$ una famiglia di $n$ sottoinsiemi di $X$, allora la famiglia $\mathcal A$ è una **partizione** di $X$ se e solo se sono soddisfatte le seguenti condizioni:
1. È un [ricoprimento](#^Ricoprimento) di $X$;
2. Non ci sono sottoinsiemi vuoti, ossia $\forall i \in I(A_i \ne \emptyset)$;
3. Non ci sono due diversi sottoinsiemi con elementi in comune, ossia $\forall i,j \in I (i \ne j \land A_i \cap A_j = \emptyset)$.

### Esempio: partizione di $\mathbb{Z}$ tra numeri pari e dispari

Dati un insieme $X = \mathbb{Z}$ e una famiglia $\mathcal A=\{A_1,A_2\}$ con $A_1=\{x : 2x \in X\}$ e $A_2=\{x : 2x+1 \in X\}$, allora la famiglia $\mathcal A$ è una partizione di $X$ perché è un ricoprimento (condizione 1 della definizione), non contiene elementi vuoti (condizione 2) e $A_1 \cap A_2=\emptyset$ perché non esistono numeri sia pari che dispari (condizione 3).

### Esempio: partizione tra un insieme e il suo complementare

Dato un sottoinsieme [[#^5cc3b3|non banale]]+ $A$ di un insieme $X$ (quindi $A \ne X$), allora $\{A,\complement_X(A)\}$ è una partizione di $X$ perché, per definizione, $A\cap \complement_X(A)=\emptyset$.

### Esempio: partizione di $\Bbb{Q}$ come famiglia di insiemi di frazioni

Data una famiglia $\mathcal P$ di sottoinsiemi di $\Bbb{Q}$ con $P_n=\{q=\frac{a}{n}\in\Bbb{Q} : a \in \mathbb{Z} \land \frac{a}{n}\text{ è ridotta ai minimi termini}\}$, allora $\mathcal P$ è una partizione di $\Bbb{Q}$ perché la scrittura di un numero razionale come frazione ridotta ai minimi termini con denominatore positivo è unica (quindi $P_m \cap P_n=\emptyset,\quad \forall m,n\in\mathbb{N}:m\ne n$). Inoltre, si può notare che $P_1=\mathbb{Z}$.

%%
Osservazione: nelle partizioni ci possono essere infiniti insiemi vuoti
%%

# Relazioni tra insiemi

## Definizione: relazione tra due insiemi

Dati due insiemi $A$ e $B$ non vuoti, si definisce _**relazione**_ tra $A$ e $B$ e si denota $A\mathcal{R}B$ un sottoinsieme del [[#^f8c559|prodotto cartesiano]] tra $A$ e $B$:

$$
A \mathcal{R} B = \{(a,b) \mid (a,b) \in A \times B\}
$$

%%
Definizione:
Sia n ≥ 1. Una relazione n-aria è un sottoinsieme di un prodotto
cartesiano della forma A0 × · · · × An−1.
Se gli insiemi A0, . . . , An−1 sono tutti lo stesso insieme A, parleremo di
relazione n-aria su A.
Se n = 1 parleremo di relazione unaria o predicato, se n = 2 parleremo
di relazione binaria, se n = 3 parleremo di relazione ternaria, ecc. . .
Sia R ⊆ A0 × · · · × An−1 una relazione n-aria. Diciamo che gli elementi
a0, . . . , an−1 sono in relazione R se ⟨a0, . . . , an−1⟩ ∈ R.
%%

%%
Osservazione: database come relazioni n-arie
I database (relazionali) sono esempi di relazioni n-arie dove:
- n `e il numero di colonne;
- ogni colonna rappresenta un insieme, ovvero l’insieme degli oggetti che compaiono (o possono comparire) in tale colonna;
- il database, visto come relazione, è un sottoinsieme del prodotto cartesiano degli insiemi di cui al punto precedente;
- ogni riga costituisce una n-upla di tale prodotto cartesiano che dichiariamo appartenere alla relazione.

In altre parole:
La tabella di un database è una rappresentazione grafica di una relazione n-aria in cui vengono esplicitamente elencati gli elementi (ovvero le n-uple) di tale relazione.

Esempio:
![](Pasted%20image%2020240928185338.png)

Esempio:
![](Pasted%20image%2020240928185358.png)
![](Pasted%20image%2020240928185407.png)
![](Pasted%20image%2020240928185421.png)
%%

%%
Relazione binaria
Una relazione binaria è un sotto insieme di un prodotto cartesiano della forma A × B; se A = B, parliamo di relazione binaria su A.

Esempio:
L’usuale ordinamento ≤ sui numeri naturali è una relazione binaria su N. La coppia (2, 7) è un elemento di tale relazione, mentre la coppia (5, 1) non lo è.

Spesso le relazioni binarie si dicono semplicemente relazioni e si scrive $a R b$ invece di (a, b) ∈ R. Ad esempio, di solito scriviamo 2 ≤ 3 invece di (2, 3) ∈ ≤.

![](Pasted%20image%2020240928185550.png)
![](Pasted%20image%2020240928185557.png)
![](Pasted%20image%2020240928185603.png)
![](Pasted%20image%2020240928185611.png)
![](Pasted%20image%2020240928185650.png)
%%

### Esempio: relazione tra due insiemi

Dati due insiemi $A=\{1,2,3\}$ e $B=\{3,4,5\}$, una loro possibile relazione è $A\mathcal{R}B=\{(1,3), (3,3), (2,4)\}$.

### Osservazione: relazioni tra più insiemi o tra una famiglia di insiemi

Una relazione si può stabilire anche tra un numero $n$ di insiemi $S_1,S_2,\ldots,S_n$ ed è un sottoinsieme del loro prodotto cartesiano $S_1\times S_2\times\ldots\times S_n$.

In egual modo, una relazione su una [[#^a73b10|famiglia di insiemi]] $\mathcal S$ è un sottoinsieme del loro prodotto cartesiano $\displaystyle\prod_{i=1}^nS_i$.

## Definizione: relazione di equivalenza

Dato un insieme $X$, si definisce _**relazione di equivalenza**_ su $X$ e si denota con il simbolo $\sim$ una [[#^2f81d7|relazione]]+ che occorre fra alcune coppie di elementi di $X$ e che soddisfa le seguenti proprietà:
1. _Riflessività_: $x\sim x,\quad \forall x \in X$;
2. _Simmetria_: $x\sim y\implies y\sim x,\quad \forall x,y\in X$;
3. _Transitività_: $x\sim y,y\sim z\implies x\sim z,\quad \forall x,y,z\in X$.

### Esempio: relazione di divisibilità tra due interi

Dato un numero naturale $n\in \mathbb{N}$, un numero intero $x\in\mathbb{Z}$ si dice _**divisibile**_ per $n$ e si denota con $n|x$ se esiste un $k\in \mathbb{Z}$ tale che $kn=x$. Si può definire una relazione di equivalenza sull'insieme $\mathbb{Z}$ degli interi affermando che, dati due elementi $x,y\in\mathbb{Z}$, $x$ è in relazione a $y$ se la loro differenza è divisibile per $n$:
$$
x \sim y \iff n|(x-y)
$$
Si può dimostrare che questa è una relazione di equivalenza verificando le tre proprietà:
1. _Riflessività_: $n|(x-x)\implies n|0$ vale, perché $0$ è divisibile per qualsiasi numero naturale $n$;
2. _Simmetria_: $n|(x-y)\implies n|(y-x)$ vale, perché se $x-y$ è divisibile per $n$, allora è divisibile anche il suo opposto $y-x$; per esempio, $2|(12-6)\implies 2|(6-12),\quad n=2,x=12,y=6$.
3. _Transitività_: $n|(x-y),n|(y-z)\implies n|(x-z)$ vale, perché se $x-y$ e $y-z$ sono divisibili per $n$, lo è anche $x-z$; per esempio, $2|(12-6),2|(6-4)\implies 2|(12-4),\quad n=2,x=12,y=6,z=4$.

## Definizione: classe di equivalenza e insieme quoziente

Dato un insieme $A$ e un insieme $X$, si dice _**classe di equivalenza**_ di $a$ rispetto alla relazione di equivalenza $\sim$ e si indica con $[a]_\sim$ l'insieme degli elementi di $X$ che hanno una relazione di equivalenza con $a$:
$$
[a]_\sim = \{x \in X \mid x \sim a\}
$$
L'insieme delle classi di equivalenza $[a]_\sim$ si dice _**insieme quoziente**_ di $X$ per la relazione $\sim$ e si indica con $X/\sim$:
$$
X/\sim = \{[a]_\sim \mid a \in X\}
$$

### Esempio: relazione di equivalenza su automobili con stesso colore

Dato un insieme $X$ di tutte le automobili e una sua relazione di equivalenza $\sim$ letta come _"ha lo stesso colore di"_, allora una classe di equivalenza può essere quella che comprende tutte le automobili verdi, mentre l'insieme quoziente $X/\sim$ è l'insieme dei colori delle automobili.

### Esempio: insieme $\Bbb Q$ dei numeri razionali come insieme quoziente

L'insieme $\Bbb Q$ dei numeri razionali può essere espresso come un insieme quoziente. Data una coppia $(p,q)$ ottenuta dal prodotto cartesiano $\mathbb{Z}\times (\mathbb{Z}\setminus\{0\})$ (quindi $p$ può essere qualsiasi numero intero, mentre $q$ qualsiasi numero intero eccetto lo $0$), si può definire una relazione di equivalenza come:
$$
(p, q) \sim (p', q') \iff pq' = p'q
$$
Ciò è verificabile se si interpreta la coppia $(p,q)$ come una frazione $\frac{p}{q}$, quindi questa relazione di equivalenza indica che due frazioni sono in relazione tra loro se sono uguali il prodotto tra il numeratore di uno e il denominatore dell'altro: $\frac{p}{q}=\frac{p'}{q'}\iff pq'=p'q$ (es. prendendo le frazioni $2\over 3$ e $4\over 6$, si può constatare che $2\cdot6=3\cdot4$).
Se si prende l'insieme quoziente di questa relazione, ossia $[\mathbb{Z}\times (\mathbb{Z}\setminus \{0\})]/\sim$, si può notare come esso corrisponda proprio all'insieme $\Bbb Q$ dei numeri razionali perché comprende tutte le combinazioni possibili di numeri presenti in $\Bbb Q$.

%%
Sia R ⊆ A × B una relazione binaria.
Il sottoinsieme di A definito da
dom(R) = {a ∈ A | (a, b) ∈ R per qualche b ∈ B}
è detto dominio della relazione R.
Il sottoinsieme di B definito da
rng(R) = {b ∈ B | (a, b) ∈ R per qualche a ∈ A}
è detto range o immagine della relazione R.

![](Pasted%20image%2020240928185951.png)
![](Pasted%20image%2020240928190001.png)
%%

%%
Relazione inversa
Se R ⊆ A × B `e una relazione (binaria), allora la relazione inversa di R, che indichiamo con R−1 e che `e ancora una relazione binaria, `e il sottoinsieme di B × A definito da
R^{−1} = {(b, a) ∈ B × A | (a, b) ∈ R}.
In altre parole, per ogni b ∈ B e a ∈ A si ha
b R^{−1} a se e solo se a R b.
Chiaramente per ogni relazione binaria R
(R^{−1})^{-1} = R,
rng(R^{−1}) = dom(R),
dom(R^{−1}) = rng(R).

Esempio
Se R `e la relazione ≤ di minore o uguale su N, allora R^{−1} `e la relazione ≥ di maggiore o uguale su N.

![](Pasted%20image%2020240928190126.png)

Definizione
Diremo che una relazione (binaria) R su un insieme A `e
- riflessiva se a R a per ogni a ∈ A;
- simmetrica se da a R b segue che b R a;
- antisimmetrica se da a R b e b R a segue che a = b;
- transitiva se da a R b e b R c segue che a R c.

Osservazione: Una relazione R su un insieme A `e simmetrica se e solo se R = R^{−1}, ovvero se per ogni (a, b) ∈ A^2
a R b se e solo se a R^{−1} b.
Inoltre, R `e riflessiva/simmetrica/antisimmetrica/transitiva se e solo se R^{−1} lo `e.
![](Pasted%20image%2020240928190234.png)
![](Pasted%20image%2020240928190241.png)
![](Pasted%20image%2020240928190257.png)
![](Pasted%20image%2020240928190306.png)
![](Pasted%20image%2020240928190336.png)
![](Pasted%20image%2020240928190355.png)
![](Pasted%20image%2020240928190406.png)
![](Pasted%20image%2020240928190414.png)
![](Pasted%20image%2020240928190424.png)
![](Pasted%20image%2020240928190432.png)
![](Pasted%20image%2020240928190441.png)
![](Pasted%20image%2020240928190450.png)
%%



Insiemi numerabili = posso contare gli elementi dell'insieme, cioè posso associare in modo biunivoco ogni elemento dell'insieme ai numeri naturali. %%e in relazione alla cardinalità come funziona?%%
$\mathbb{R}$ è un insieme NON numerabile, mentre $\mathbb{N}$ sì (la sua cardinalità è $\infty$)
%% Osservazione: $\mathbb{N}$ include lo $0$ o no? %%
