Le **relazioni tra insiemi** descrivono i legami che possono esistere tra due o più [insiemi](Insiemistica.md#^Definizione-insieme). Queste relazioni sono fondamentali in [insiemistica](Insiemistica.md) e matematica in generale.

# 1 - Introduzione alle relazioni

> [!definizione]+ Definizione: relazione $\color{#FF88FF}n$-aria
> 
> Dati $n \ge 1$ insiemi non vuoti $A_0, A_1, \ldots, A_{n-1}$, si definisce _**relazione $n$-aria**_ e si denota "$\mathcal{R}$" un [sottoinsieme](Insiemistica.md#^Definizione-sottoinsieme) del [prodotto cartesiano](Insiemistica.md#^Definizione-prodotto-cartesiano-di-due-insiemi) tra tutti gli insiemi:
> 
> $$
> \mathcal{R} \subseteq A_0 \times A_1 \times \ldots \times A_{n-1}
> $$
> 
> Se gli insiemi $A_0, A_1, \ldots, A_{n-1}$ coincidono tutti con uno stesso insieme $A$, si parla di _**relazione $n$-aria su $A$**_.
> 
> Inoltre, quando $n = 1$, oltre a "_relazione unaria_" si parla anche di _**predicato**_, mentre quando $n=2$, oltre a _"relazione binaria"_, si parla anche semplicemente di _"relazione"_ e, dati due elementi $a \in A_0$ e $b \in A_1$, si scrive:
> $$
> a \mathcal{R} b
> $$
> invece di $(a,b) \in \mathcal{R}$.
^Definizione-relazione-n-aria

> [!esempio]+ Esempio: relazione binaria tra due insiemi
> 
> Dati due insiemi:
> $$
> \begin{align*}
>  & A = \{1,2,3\} \\
>  & B = \{3,4,5\}
> \end{align*}
> $$
> Una loro possibile relazione è:
> $$
> \mathcal{R} = \{(1,3), (3,3), (2,4)\} \subseteq A \times B
> $$

> [!esempio]+ Esempio: gli ordinamenti sono relazioni binarie
> 
> Le usuali operazioni di ordine sui numeri naturali $\mathbb{N}$%% link %% sono relazioni binarie su $\mathbb{N}$ (es. l'ordine non-decrescente $\le$%% link %% è una relazione binaria e la coppia $(2, 7)$ è un elemento di tale relazione perché $2 \le 7$, mentre la coppia $(5, 1)$ non lo è).
> 
> Inoltre, essendo una relazione binaria, si può notare come solitamente si scriva $2 \le 7$ anziché $(2,7) \in \le$.

> [!osservazione]+ Osservazione: database relazionali come relazioni $\color{#888888}n$-arie
>
> I database relazionali%% link %% sono esempi di relazioni $n$-arie dove:
> - $n$ è il numero di colonne.
> - Ogni colonna rappresenta l'[insieme](Insiemistica.md#^Definizione-insieme) degli oggetti che compaiono (o possono comparire) in tale colonna.
> - Il database visto come relazione è un sottoinsieme del [prodotto cartesiano](Insiemistica.md#^Definizione-prodotto-cartesiano-di-due-insiemi) dei suddetti insiemi.
> - Ogni riga costituisce una [$n$-upla](Insiemistica.md#^Definizione-tupla) di tale [prodotto cartesiano](Insiemistica.md#^Definizione-prodotto-cartesiano-di-due-insiemi) che dichiariamo appartenere alla relazione.
>
> In altre parole: la tabella di un database è una rappresentazione grafica di una relazione $n$-aria in cui vengono esplicitamente elencati gli elementi (ovvero le $n$-uple) di tale relazione.

> [!esempio]+ Esempio: database relazionale come relazione $n$-aria
> 
> Consideriamo il seguente (ipotetico) database dell'anagrafe:
> 
> | Cognome | Nome  | Data di nascita | Luogo di nascita |
> | ------- | ----- | --------------- | ---------------- |
> | Rossi   | Mario | 05/10/1976      | Firenze          |
> | Verdi   | Luigi | 25/01/2001      | Torino           |
> | Bianchi | Carla | 22/06/1983      | Napoli           |
> | Neri    | Marco | 19/03/1969      | Milano           |
> 
> In termini di relazioni, questo database si può considerare come una relazione quaternaria (cioè con $n = 4$):
> $$
> \mathcal{R} \subseteq A \times B \times C \times D
> $$
> dove:
> - $A$: è l'insieme di tutti i cognomi.
> - $B$: è l'insieme di tutti i nomi.
> - $C$: è l'insieme di tutte le date di nascita.
> - $D$: è l'insieme di tutti i luoghi di nascita.
> 
> Le righe forniscono l'elenco completo delle $4$-uple che sono elementi di $\mathcal{R}$, ad esempio:
> $$
> \langle \text{Neri, Marco, 19/03/1969, Milano} \rangle \in \mathcal{R}
> $$

## 1.1 - Rappresentazioni grafiche delle relazioni con i diagrammi di Eulero-Venn

%% collegamento ocn diagrammi di eulero-venn %%

Le relazioni $n$-arie si possono rappresentare graficamente tramite i diagrammi di Eulero-Venn%% link %%.

%% 
> [!esempio]+ Esempio: rappresentazione di $\color{#8888FF}\mathcal{R} \subseteq A \times B$ con i diagrammi
> 

dati due insiemi bla bla bla, si rappresentano ecc. ecc.:
![](Pasted%20image%2020240928185550.png)
%%

Una relazione $n$-aria su uno stesso insieme $A$ si può rappresentare o come una generica relazione $n$-aria su $n$ "copie" dell'insieme $A$, oppure come insieme di frecce tra i punti della stessa copia di $A$.

%% 
Esempio:

![](Pasted%20image%2020240928185557.png)

![](Pasted%20image%2020240928185603.png)

%%

## 1.2 - Rappresentazioni grafiche delle relazioni con il piano cartesiano

Esattamente come il prodotto cartesiano si può rappresentare sul piano cartesiano, anche le relazioni $n$-arie si possono rappresentare su quest'ultimo essendo sottoinsiemi del prodotto.%% aggiungere tutti i link %%

%% 
Esempio:

![](Pasted%20image%2020240928185611.png)

%%

%% 

Esempio su R:

![](Pasted%20image%2020240928185650.png)
%%

## 1.3 - Dominio e immagine di una relazione

%% 
Sia R \subseteq A \times B una relazione binaria.
Il sottoinsieme di A definito da
dom(R) = {a \in A | (a, b) \in R per qualche b \in B}
è detto dominio della relazione R.
Il sottoinsieme di B definito da
rng(R) = {b \in B | (a, b) \in R per qualche a \in A}
è detto range o immagine della relazione R.
%%

### 1.3.1 - Rappresentazioni grafiche di dominio e immagine tramite diagrammi di Eulero-Venn

%%

![](Pasted%20image%2020240928185951.png)
![](Pasted%20image%2020240928190001.png)
%%

## 1.4 - Relazione inversa

> [!definizione]+ Definizione: relazione inversa
> 
> Dati due [insiemi](Insiemistica.md#^Definizione-insieme) $A$ e $B$ e una loro [relazione binaria](Relazioni%20tra%20insiemi.md#^Definizione-relazione-n-aria) $\mathcal{R} \subseteq A \times B$, si definisce _**relazione inversa**_ di $\mathcal{R}$ e si indica con $\mathcal{R}^{-1}$ un [sottoinsieme](Insiemistica.md#^Definizione-sottoinsieme) del [prodotto cartesiano](Insiemistica.md#^Definizione-prodotto-cartesiano-di-due-insiemi) $B \times A$:
> 
> $$
> \mathcal{R}^{-1} = \{ (b,a) \in B \times A \mid (a,b) \in \mathcal{R} \} \subseteq B \times A
> $$
> 
> In altre parole, per ogni $b \in B$ e per ogni $a \in A$ si ha:
> $$
> b \mathcal{R}^{-1} a \iff a \mathcal{R} b
> $$

%% 
Esempio
Se R è la relazione \le di minore o uguale su N, allora R^{-1} è la relazione \ge di maggiore o uguale su N.
%%

%% 
2 Osservazioni:
1. Chiaramente per ogni relazione binaria R: (R^{-1})^{-1} = R,
2. rng(R^{-1}) = dom(R), dom(R^{-1}) = rng(R).
%%

### 1.4.1 - Rappresentazione grafica di una relazione inversa tramite diagrammi di Eulero-Venn

%%
![](Pasted%20image%2020240928190126.png)
%%

## 1.5 - Proprietà delle relazioni binarie

> [!definizione]+ Definizione: proprietà delle relazioni binarie
> 
> Dati un [insieme](Insiemistica.md#^Definizione-insieme) $A$ e una [relazione binaria](Relazioni%20tra%20insiemi.md#^Definizione-relazione-n-aria) $\mathcal{R}$ su $A$ (cioè $\mathcal{R} \subseteq A^2$), si definiscono le seguenti _**proprietà**_ su quest'ultima:
> - **Riflessività**: $\forall a \in A (a \mathcal{R} a)$.
> - **Irriflessività**: $\forall a \in A (\lnot(a \mathcal{R} a ))$.
> - **Simmetria**: $\forall a,b \in A (a \mathcal{R} b \implies b \mathcal{R} a)$.
> - **Antisimmetria**: $\forall a,b \in A (a \mathcal{R} b \land b \mathcal{R} a \implies a = b)$.
> - **Transitività**: $\forall a,b,c \in A (a \mathcal{R} b \land b \mathcal{R} c \implies a \mathcal{R} c)$.
^Definizione-proprieta-delle-relazioni-binarie

> [!osservazione]+ Osservazione: relazione simmetrica solo se $\mathcal{R} = \mathcal{R}^{-1}$
> 
> Dati un [insieme](Insiemistica.md#^Definizione-insieme) $A$ e una [relazione binaria](Relazioni%20tra%20insiemi.md#^Definizione-relazione-n-aria) $\mathcal{R}$ su $A$ (cioè $\mathcal{R} \subseteq A^2$), $\mathcal{R}$ è simmetrica se e solo se $\mathcal{R} = \mathcal{R}^{-1}$, ovvero se:
> $$
> \forall (a,b) \in A^2 (a \mathcal{R} b \iff a \mathcal{R}^{-1}b)
> $$

%% 
Inoltre, R è riflessiva/simmetrica/antisimmetrica/transitiva se e solo se R-1 lo `e.
%%

%% 
Esempi
Sia A l'insieme delle rette del piano e sia R una relazione su A.
- Se a R b significa che a e b sono rette parallele (eventualmente coincidenti), allora R è riflessiva, simmetrica e transitiva.
- Se a R b significa che le rette a e b hanno intersezione non vuota, allora R è riflessiva e simmetrica, ma non transitiva.
- Se a R b significa che le rette a e b sono ortogonali, allora R è simmetrica, ma non è né riflessiva, né transitiva.
%%

%% 
fare poi tabella con checklist delle proprietà che ogni relazione vuole siano rispettate e quali no
%%

### 1.5.1 - Rappresentazioni grafiche delle proprietà delle relazioni

%% 

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

# 2 - Relazioni di equivalenza

> [!definizione]+ Definizione: relazione di equivalenza
> 
> Dato un [insieme](Insiemistica.md#^Definizione-insieme) $A$, si definisce _**relazione di equivalenza**_ su $A$ e si denota con "$\sim$" una [relazione binaria](Relazioni%20tra%20insiemi.md#^Definizione-relazione-n-aria) che rispetta le seguenti [proprietà](Relazioni%20tra%20insiemi.md#^Definizione-proprieta-delle-relazioni-binarie):
> - **Riflessività**: $\forall a \in A (a \mathcal{R} a)$.
> - **Simmetria**: $\forall a,b \in A (a \mathcal{R} b \implies b \mathcal{R} a)$.
> - **Transitività**: $\forall a,b,c \in A (a \mathcal{R} b \land b \mathcal{R} c \implies a \mathcal{R} c)$.
^Definizione-relazione-di-equivalenza

> [!esempio]+ Esempio: relazione di divisibilità per $\color{#8888FF}n$ tra due interi
> 
> Dato un numero naturale $n \in \mathbb{N}$, un numero intero $x \in \mathbb{Z}$ si dice _divisibile_ per $n$ e si denota con "$n|x$" se esiste un $k \in \mathbb{Z}$ tale che $k \cdot n = x$. Si può definire una relazione di equivalenza sull'insieme dei numeri interi $\mathbb{Z}$%% link %% affermando che, dati due elementi $x, y \in \mathbb{Z}$, $x$ è in relazione a $y$ se la loro differenza è divisibile per $n$:
> $$
> x \sim y \iff n|(x-y)
> $$
> Si può dimostrare che questa è una relazione di equivalenza verificando le tre [proprietà](Relazioni%20tra%20insiemi.md#^Definizione-proprieta-delle-relazioni-binarie):
> 1. **Riflessività**: $n|(x-x)\implies n|0$ vale, perché $0$ è divisibile per qualsiasi numero naturale $n$.
> 2. **Simmetria**: $n|(x-y)\implies n|(y-x)$ vale, perché se $x-y$ è divisibile per $n$, allora è divisibile anche il suo opposto $y-x$ (es. $2|(12-6)\implies 2|(6-12)$, con $n=2,x=12,y=6$).
> 3. **Transitività**: $n|(x-y),n|(y-z)\implies n|(x-z)$ vale, perché se $x-y$ e $y-z$ sono divisibili per $n$, lo è anche $x-z$ (es. $2|(12-6),2|(6-4)\implies 2|(12-4)$, con $n=2,x=12,y=6,z=4$).

Oltre al simbolo "$\sim$", spesso per denotare la relazione di equivalenza si usano le lettere $\mathcal{E}$, $\mathcal{F}$, ecc., oppure simboli che, in qualche misura, richiamano la relazione d'uguaglianza%% link %%, quali ad esempio "$\equiv$", "$\simeq$", "$\cong$", "$\approx$", ecc.

> [!definizione]+ Definizione: classe di equivalenza
> 
> Dati un [insieme](Insiemistica.md#^Definizione-insieme) $A$ e una [relazione di equivalenza](Relazioni%20tra%20insiemi.md#^Definizione-relazione-di-equivalenza) $\sim$ su $A$, la **classe di equivalenza** di un elemento $a \in A$ rispetto alla relazione di equivalenza $\sim$, indicata con "$[a]_\sim$", è l'insieme degli elementi di $A$ che hanno una [relazione di equivalenza](Relazioni%20tra%20insiemi.md#^Definizione-relazione-di-equivalenza) con $a$:
> $$
> [a]_\sim = \{x \in A \mid x \sim a\}
> $$
> Quando la relazione $\sim$ è chiara dal contesto, si può scrivere anche solo $[a]$ al posto di $[a]_\sim$.
^Definizione-classe-di-equivalenza

> [!definizione]+ Definizione: insieme quoziente
>
> Dati un [insieme](Insiemistica.md#^Definizione-insieme) $A$ e una [relazione di equivalenza](Relazioni%20tra%20insiemi.md#^Definizione-relazione-di-equivalenza) $\sim$ su $A$, l'insieme delle [classi di equivalenza](Relazioni%20tra%20insiemi.md#^Definizione-classe-di-equivalenza) $[a]_\sim$ si dice _**insieme quoziente**_ di $X$ per la relazione $\sim$ e si indica con "$A/\sim$":
> $$
> A/\sim = \{[a]_\sim \mid a \in A\}
> $$
^Definizione-insieme-quoziente

> [!esempio]+ Esempio: relazione di equivalenza su automobili con stesso colore
> 
> Dati un [insieme](Insiemistica.md#^Definizione-insieme) $A$ e una [relazione di equivalenza](Relazioni%20tra%20insiemi.md#^Definizione-relazione-di-equivalenza) $\sim$ su $A$ letta come _"ha lo stesso colore di"_, allora una [classe di equivalenza](Relazioni%20tra%20insiemi.md#^Definizione-classe-di-equivalenza) $[a]_\sim$ può essere quella che comprende tutte le automobili verdi, mentre l'[insieme quoziente](Relazioni%20tra%20insiemi.md#^Definizione-insieme-quoziente) $A/\sim$ è l'insieme dei colori delle automobili.

> [!esempio]+ Esempio: insieme $\mathbb{Q}$ dei numeri razionali come insieme quoziente
> 
> L'insieme $\mathbb{Q}$ dei numeri razionali%% link %% può essere espresso come un [insieme quoziente](Relazioni%20tra%20insiemi.md#^Definizione-insieme-quoziente). Data una coppia $(p,q)$ ottenuta dal [prodotto cartesiano](Insiemistica.md#^Definizione-prodotto-cartesiano-di-due-insiemi) $\mathbb{Z}\times (\mathbb{Z}\setminus\{0\})$ (quindi $p$ può essere qualsiasi numero intero, mentre $q$ qualsiasi numero intero eccetto lo $0$), si può definire una relazione di equivalenza come:
> $$
> (p, q) \sim (p', q') \iff pq' = p'q
> $$
> Ciò è verificabile se si interpreta la coppia $(p,q)$ come una frazione $\frac{p}{q}$, quindi questa [relazione di equivalenza](Relazioni%20tra%20insiemi.md#^Definizione-relazione-di-equivalenza) indica che due frazioni sono in relazione tra loro se sono uguali il prodotto tra il numeratore di uno e il denominatore dell'altro: $\frac{p}{q} = \frac{p'}{q'} \iff pq' = p'q$ (es. prendendo le frazioni $\frac{2}{3}$ e $\frac{4}{6}$, si può constatare che $2 \cdot 6 = 3 \cdot 4$).
> Se si prende l'insieme quoziente di questa relazione, ossia $[\mathbb{Z} \times (\mathbb{Z} \setminus \{0\})] / \sim$, si può notare come esso corrisponda proprio all'insieme $\mathbb{Q}$ dei numeri razionali perché comprende tutte le combinazioni possibili di numeri presenti in $\mathbb{Q}$.

%% 
Osservazione:
L'insieme quoziente è una famiglia di sottoinsiemi di A, cioè A/E \subseteq P(A).
%%

%% 
Esempio: campionato di serie A
Sia X l'insieme di tutti i giocatori di squadre di serie A.
Definiamo ora una relazione binaria E sull'insieme X stabilendo che a E b
se e solo se a e b giocano nella stessa squadra.
La relazione E è chiaramente riflessiva, simmetrica e transitiva, quindi `e
una relazione di equivalenza su X.
Le classi di equivalenza sono le squadre del campionato di serie A.
Il quoziente X/E consiste nel campionato di serie A, ossia è l'insieme
delle squadre che giocano in quel campionato.
%%

%% 
Esempio: le regioni
Sia X l'insieme di tutti i comuni italiani.
Definiamo ora una relazione binaria E sull'insieme X stabilendo che a E b
se e solo se a e b si trovano nella stessa regione.
La relazione E è chiaramente riflessiva, simmetrica e transitiva, quindi `e
una relazione di equivalenza su X.
Le classi di equivalenza sono le regioni italiane.
Il quoziente X/E consiste nell'insieme di tutte le regioni italiane.
%%

%% 
Esempio: congruenza modulo 2
Dati due interi a, b \in Z, a è congruente a b modulo 2 se a - b è pari
(ovvero se a - b = 2 · k per qualche k \in Z). In questo caso scriviamo
a \equiv b mod 2
La relazione di congruenza modulo 2 è una relazione di equivalenza:
Riflessivit`a: a - a = 0 è pari, quindi a \equiv a mod 2.
Simmetria: b - a = -(a - b), quindi a - b è pari se e solo se b - a lo `e.
Transitivit`a: a - c = (a - b) + (b - c), per cui se a - b e b - c sono pari,
allora anche a - c lo `e.
Ci sono due classi di equivalenza per questa relazione:
i numeri pari, ossia [0] = {n | n - 0 = n è pari},
i numeri dispari, ossia [1] = {n | n - 1 è pari},
e l'insieme quoziente {[0], [1]} ha esattamente 2 elementi e lo si indica con
Z_2 ovvero Z/2Z
%%

%% 
Esempio: congruenza modulo n
Più in generale, dato 0̸ = n \in N e a, b \in Z, a è congruente a b modulo
n se a - b è un multiplo di n (ovvero se a - b = n · k per qualche k \in Z).
In questo caso scriviamo
a \equiv b mod n

Esercizio (perché Viale ha scritto che questo è un esercizio?)
La relazione di congruenza modulo n è una relazione di equivalenza e
ciascuna classe di equivalenza è della forma
[k] = {a \in Z | la divisione intera di a per n ha resto k}
per qualche k \in {0, . . . , n - 1}

Dunque l'insieme quoziente risultante
Z_n = Z/nZ := {[k] | 0 \le k \le n - 1}
ha esattamente n elementi.
%%

%% 
Proposizione
Sia E una relazione d'equivalenza su A e consideriamo a, b \in A. Se a E b
allora $[a]_E = [b]_E$, mentre se a NOT-E b (cioè \lnot(a E b)), allora [a]_E \cap [b]_E = \emptyset.
In particolare, due classi di equivalenza sono disgiunte o coincidono.
 
Dimostrazione.
Supponiamo a E b. Sia c \in [a]E : allora c E a e per la proprietà transitiva
c E b, quindi c \in [b]E . Essendo c arbitrario, abbiamo dimostrato che
[a]E \subseteq [b]E . Sia ora c \in [b]E : allora c E b. Per la proprietà simmetrica
b E a, da cui c E a per la proprietà transitiva: quindi c \in [a]E . Segue che
[b]E \subseteq [a]E . Per il principio della doppia inclusione abbiamo quindi
[a]E = [b]E .

Supponiamo ora a NOT-E b. Verifichiamo che in questo caso [a]E \cap [b]E = \emptyset.
Supponiamo, per assurdo, che ci sia un c \in [a]E \cap [b]E . Allora c E b, da
cui b E c per simmetria. Inoltre c E a, quindi b E a per transitivit`a, e
a E b per simmetria. Ma questo contraddice la nostra assunzione che
a̸ E b.

$\blacksquare$
%%

## 2.1 - Relazioni di equivalenza e partizioni

%% 
Se E è una relazione di equivalenza su A, allora il quoziente A/E è una
partizione di A: ogni [a]E \subseteq A è non vuota, due classi di equivalenza
distinte sono disgiunte (Proposizione precedente) e per ogni a \in A si ha
a \in [a]E \in A/E.
Viceversa, data una partizione C di A, la relazione E su A definita da:

> a E b se e solo se a e b appartengono allo stesso X \in C

e una relazione di equivalenza su A, ovvero è riflessiva, simmetrica e
transitiva (se a, b \in X \in C e b, c \in Y \in C, allora X = Y poiché b \in X \cap Y
e C è una partizione: perciò a, c \in X \in C), e A/E = C. Quindi partizioni su A e insiemi quozienti di A sono la stessa cosa.
%%

%% 
Esempio
Sia C = {P, D} la partizione di Z in numeri pari e dispari. Consideriamo la
relazione di congruenza modulo 2 su Z, e sia Z2 lo spazio quoziente.
Allora C = Z2. Infatti Z2 = {[0], [1]} e [0] = P e [1] = D.
%%

%% 
Esercizio su relazioni di equivalenza 1:
Consideriamo la relazione E su R definita da
x E y se e solo se |x| = |y|.
Dimostrare che E è una relazione d'equivalenza.

Soluzione:
Siano x, y, z elementi arbitrari di R.
Riflessività Ovvio, x E x perché |x| = |x|.
Simmetria Anche questo è facile: se x E y allora |x| = |y|, quindi anche
y E x perché |y| = |x|.
Transitività Supponiamo che x E y e y E z: vogliamo dimostrare che
x E z. Dalla prima condizione otteniamo |x| = |y|, mentre
dalla seconda |y| = |z|: quindi |x| = |y| = |z|, ovvero x E z.

Esercizio:
Consideriamo la relazione di equivalenza E su R definita da
x E y se e solo se |x| = |y|.

Come sono fatte le classi di equivalenza di E?
Risposta: Sono del tipo [r]E = {r, -r} per r \in R.
Quanti elementi ha ciascuna di tali classi?
Risposta: Due elementi distinti se r̸ = 0, uno solo se r = 0.
Quante classi di equivalenza distinte otteniamo?
Risposta: Infinite, una per ogni r \ge 0.
Com'è fatto l'insieme quoziente R/E?
Risposta: R/E = {{r, -r} | r \in R}.
%%

%% 
Esercizi su relazioni d'equivalenza (2)
Consideriamo la relazione E su N definita da

> n E m se e solo se n ed m hanno lo stesso numero di cifre (in notazione decimale).

Dimostrare che E è una relazione d'equivalenza.

Soluzione:
Siano n, m, l elementi arbitrari di N.
Riflessività Ovvio, n E n poiché ciascun numero si scrive con lo stesso
numero di cifre di sé stesso.
Simmetria Ovvio, se n E m vuol dire che n ha lo stesso numero di cifre
di m: quindi anche m E n, ovvero m ha lo stesso numero di
cifre di n.
Transitività Se n E m e, in particolare, n e m hanno entrambi k cifre, e
inoltre m E l, ovvero m e l hanno hanno lo stesso numero di
cifre, allora anche l ha k cifre, per cui n E l.

Esercizio:
Consideriamo la relazione di equivalenza E su N definita da
n E m se e solo se n ed m hanno lo stesso numero di cifre
(in notazione decimale).

Domande e risposte:
```latex
\begin{itemize}
    \item Come sono fatte le classi di equivalenza di \(E\)?\\
    Sono del tipo \(C_k = \{n \in \mathbb{N} \mid n \text{ ha esattamente } k \text{ cifre}\}\) per \(k \in \mathbb{N} \setminus \{0\}\). Più precisamente, \(C_1 = \{0, 1, 2, 3, 4, 5, 6, 7, 8, 9\}\) e \(C_k = \{n \in \mathbb{N} \mid 10^{k-1} \leq n < 10^k\}\) se \(k \geq 2\).
    
    \item Quanti elementi ha ciascuna di tali classi?\\
    \(C_k\) ha \(10\) elementi se \(k = 1\), e ne ha \(9 \cdot 10^{k-1}\) se \(k > 1\).
    
    \item Quante classi di equivalenza distinte otteniamo?\\
    Infinite, una per ogni \(k \in \mathbb{N} \setminus \{0\}\).
    
    \item Com'è fatto l'insieme quoziente \(\mathbb{N} / E\)?\\
    \(\mathbb{N} / E = \{C_k \mid k \in \mathbb{N} \setminus \{0\}\}\).
\end{itemize}
```
%%

%% 
Esercizi su relazioni d'equivalenza (3)
Sia
Fin = {X \subseteq N | X è finito}.
Consideriamo la relazione ≈ su Fin definita da
X ≈ Y se e solo se X e Y hanno lo stesso numero di elementi.
Dimostrare che ≈ è una relazione d'equivalenza.

Soluzione:
Siano X, Y, Z arbitrari elementi di Fin.
Riflessività Ovvio, ogni X ha lo stesso numero di elementi di se stesso.
Simmetria Ovvio, se X ≈ Y allora X e Y hanno lo stesso numero di
elementi, quindi anche Y ≈ X.
Transitività Se X e Y hanno entrambi k elementi, e inoltre Y e Z hanno
lo stesso numero di elementi, allora anche Z ha k elementi,
da cui X ≈ Z.

Domande e risposte:
```latex
\begin{itemize}
    \item Come sono fatte le classi di equivalenza di \(\approx\)?\\
    Sono del tipo \(I_k = \{X \in \mathrm{Fin} \mid X \text{ ha } k \text{ elementi}\}\) per \(k \in \mathbb{N}\). In particolare, \(I_0 = \{\emptyset\}\), \(I_1 = \{\{n\} \mid n \in \mathbb{N}\}\), \(I_2 = \{\{n, m\} \mid n, m \in \mathbb{N}, n \neq m\}\) e così via.
    
    \item Quanti elementi ha ciascuna di tali classi?\\
    \(I_0\) ha un solo elemento, mentre tutte le altre classi \(I_k\) con \(k \geq 1\) ne hanno infiniti.
    
    \item Quante classi di equivalenza distinte otteniamo?\\
    Infinite, una per ogni \(k \in \mathbb{N}\).
    
    \item Com'è fatto l'insieme quoziente \(\mathrm{Fin} / \approx\)?\\
    \(\mathrm{Fin} / \approx = \{I_k \mid k \in \mathbb{N}\}\).
\end{itemize}

```
%%

# 3 - Relazioni di ordine

> [!definizione]+ Definizione: relazione di ordine
> 
> Dato un [insieme](Insiemistica.md#^Definizione-insieme) $A$, una **relazione di ordine** su $A$ (o, più semplicemente, un **ordine** o un **ordinamento** su $A$) è una [relazione](Relazioni%20tra%20insiemi.md#^Definizione-relazione-n-aria) che rispetta le seguenti [proprietà](Relazioni%20tra%20insiemi.md#^Definizione-proprieta-delle-relazioni-binarie):
> - **Riflessività**: $\forall a \in A (a \mathcal{R} a)$.
> - **Antisimmetria**: $\forall a,b \in A (a \mathcal{R} b \land b \mathcal{R} a \implies a = b)$.
> - **Transitività**: $\forall a,b,c \in A (a \mathcal{R} b \land b \mathcal{R} c \implies a \mathcal{R} c)$.
^Definizione-relazione-di-ordine

> [!esempio]+ Esempio: ordine non-decrescente $\le$ è una relazione di ordine
> 
> Un esempio canonico per la relazione di ordine è l'ordine non-decrescente $\le$ su $\mathbb{N}$, cioè l'insieme:
> $$
> \{ (n,m) \in \mathbb{N}^2 \mid n \le m \}
> $$
> 
> %% dimostrare perché è una relazione di ordine %%
> Analogamente, $\le$ è un ordine anche sugli insiemi $\mathbb{Z}$, $\mathbb{Q}$ ed $\mathbb{R}$%% link a tutti %%.

%% 
chiarire perché "ordine non-decrescente" anziché "ordine crescente"
%%

Per indicare relazioni di ordine spesso si usano, oltre a "$\le$", altri simboli che in qualche misura gli somigliano, come "$\preceq$", "$\trianglelefteq$", "$\lesssim$", "$\sqsubseteq$", ecc.

Quando vorremo esplicitare l'insieme $A$ su cui è definito l'ordine $\le$, scriveremo $\langle A, \le \rangle$. Questa notazione è utile per distinguere, ad esempio, l'ordine sui numeri naturali%% link %% $\langle \mathbb{N}, \le \rangle$ dall'ordine sui numeri interi%% link %% $\langle \mathbb{Z}, \le \rangle$.

%% 
Esempio
Sia A un insieme qualunque. La relazione di inclusione \subseteq è un ordine
sull'insieme P(A) = {B | B \subseteq A}. Infatti
Riflessività Segue dal fatto che B \subseteq B per ogni insieme B.
Antisimmetria Segue dal principio di doppia inclusione:
se B \subseteq C e C \subseteq B allora B = C.
Transitività Supponiamo che B \subseteq C \subseteq D. Allora dato un qualunque
x \in B si deve avere anche x \in C poiché B \subseteq C, quindi
anche x \in D poiché C \subseteq D. Dunque ogni elemento di B `e
anche un elemento di D, ovvero B \subseteq D.
%%

## 3.1 - Relazione di ordine totale

> [!definizione]+ Definizione: relazione di ordine totale
> 
> Dato un [insieme](Insiemistica.md#^Definizione-insieme) $A$, una [relazione di ordine](Relazioni%20tra%20insiemi.md#^Definizione-relazione-di-ordine) $\mathcal{R}$ su $A$ si dice **totale** (o **lineare**) se:
> $$
> \forall a,b \in A(a \mathcal{R} b \lor b \mathcal{R} a)
> $$

%% 
Esempio:
L'ordine \le su N, Z, Q o R è un ordine lineare
%%

Come già visto%% link %%, per qualunque insieme $A$ l'inclusione $\subseteq$ è un ordine su $\mathcal{P}(A) = \{B \mid B \subseteq A\}$. Tuttavia, se ad esempio $A = \{ a,b \}$, quest'ordine non è totale, poiché $\{ a \} \nsubseteq \{ b \}$ e $\{ b \} \nsubseteq \{ a \}$.

%% 
Esercizio 1
Disegnare il diagramma di Hasse degli ordini $\langle\mathcal{P}(\{0\}), \subseteq\rangle$, $\langle\mathcal{P}(\{0, 1\}), \subseteq\rangle$ e $\langle\mathcal{P}(\{0, 1, 2\}), \subseteq\rangle$. In quali casi si ha un ordine lineare?
%%

## 3.2 - Relazione di successione immediata e diagrammi di Hasse

> [!definizione]+ Definizione: relazione di successione immediata
> 
> Dati un [insieme](Insiemistica.md#^Definizione-insieme) $A$ e una [relazione di ordine](Relazioni%20tra%20insiemi.md#^Definizione-relazione-di-ordine) $\le$ $A$, un elemento $y \in A$ è un **successore immediato** di $x \in A$ (e $x$ è un **predecessore immediato** di $y$), in simboli $x \lhd y$, se:
> $$
> x \le y \land x \ne y \land \forall z \in A (x \le z \land z \le y \implies z = x \lor z = y)
> $$
> %% cioè, se nell'ordine non ci sono elementi in mezzo ai due %%
> %% anche come b<a e ∄c(b<c<a) %%

%% 
![](Pasted%20image%2020250106193233.png)

![](Pasted%20image%2020250106193243.png)

ATTENZIONE: il diagramma di Hasse in un ordine NON è unico!

![](Pasted%20image%2020250106193308.png)

%%

## 3.3 - Massimi e minimi di un ordine

> [!definizione]+ Definizione: massimo e minimo di un ordine
> 
> Dati un [insieme](Insiemistica.md#^Definizione-insieme) $A$ e una [relazione di ordine](Relazioni%20tra%20insiemi.md#^Definizione-relazione-di-ordine) $\le$ $A$, un elemento $a \in A$ si dice:
> - **Massimo** (rispetto a $\le$) se $\forall b \in A (b \le a)$.
> - **Minimo** (rispetto a $\le$) se $\forall b \in A (a \le b)$.

%% 
L'ordine \le su N ha minimo (il numero 0), ma non ha massimo.
L'ordine \le su Z non ha né minimo, né massimo.
L'ordine \le sull'intervallo (0; 1] := {x \in R | 0 < x \le 1} ha massimo (il numero 1) ma non ha minimo.
L'ordine \subseteq su P(A) ha minimo (l'insieme \emptyset) e massimo (l'insieme A), poiché \emptyset \subseteq B \subseteq A per ogni B \subseteq A.
%%

%%
Esempio: la relazione di divisibilità fra numeri naturali
Definiamo ⪯ su N come

> n ⪯ m se e solo se m = n · k per qualche k \in N.

Dimostrare che ⪯ è un ordine non totale su N che ha minimo e massimo.

Siano n, m, l \in N arbitrari.

Riflessività n ⪯ n poiché n = n · 1.

Antisimmetria Supponiamo che n ⪯ m e m ⪯ n. Allora esiste i \in N tale che
m = n · i ed esiste j \in N tale che n = m · j. Se m = 0 allora
n = 0 · j = 0, quindi m = n. Altrimenti per sostituzione si ha
m = m · j · i, da cui, dividendo per m, si ottiene j · i = 1. Perci`o
j = i = 1, da cui m = n · 1 = n.

Transitività Supponiamo che n ⪯ m e m ⪯ l. Siano i, j \in N tali che l = m · i
e m = n · j. Allora l = n · j · i, ovvero n ⪯ l.

Non totale Ad esempio, 2̸ ⪯ 3 e 3̸ ⪯ 2.

Minimo `E il numero 1: si ha sempre 1 ⪯ n poiché n = 1 · n.
Massimo `E il numero 0: si ha sempre n ⪯ 0 perché 0 = n · 0.
%%

%% 
La relazione di divisibilità spesso si denota con il simbolo |:

> n | m se e solo se n divide m,

ovvero m = n · k per qualche k \in N.
Dato m \in N, l'insieme dei divisori di m `e
Div(m) = {n \in N | n divide m} .
Si osservi che Div(m)̸ = \emptyset poich´e, ad esempio, 1 ed m vi appartengono.
Se m̸ = 0 l'insieme Div(m) è un insieme finito e contiene solo numeri
compresi tra 1 ed m. Invece Div(0) = N.
%%

%% 
Esercizio 2
Calcolare il diagramma di Hasse dei seguenti ordini: \langleDiv(6), |\rangle,
\langleDiv(8), |\rangle, \langleDiv(9), |\rangle, \langleDiv(12), |\rangle e \langleDiv(30), |\rangle. Quali di questi sono
ordini lineari?
%%

%% 
Esercizio su ordini
Definiamo ⊴ su N \ {0} ponendo
n ⊴ m se e solo se m = nk per qualche k \in N.
Dimostrare che ⊴ è un ordine non lineare che ha massimo ma non ha
minimo.

Soluzione:
Siano n, m, l \in N \ {0} arbitrari.
Riflessività n ⊴ n poiché n = n1.
Antisimmetria Supponiamo che n ⊴ m e m ⊴ n. Allora esistono i, j \in N tali che
m = ni e n = mj . Quindi m = (mj )i = mj·i, da cui o m = 1
oppure j · i = 1. Nel primo caso, n = mj = 1j = 1, da cui m = n.
Nel secondo caso j = i = 1, da cui m = n1 = n.
Transitività Supponiamo che n ⊴ m e m ⊴ l. Siano i, j \in N tali che l = mi e
m = nj . Allora l = (nj )i = nj·i, ovvero n ⊴ l.
Non lineare Ad esempio, \lnot(2 ⊴ 3) e \lnot(3 ⊴ 2).
Minimo Non esiste, perché non esiste alcun n tale che n ⊴ 2 e n ⊴ 3.
Massimo `E il numero 1: si ha sempre n0 = 1, perciò n ⊴ 1.
%%

## 3.4 - Relazione di ordine stretto

> [!definizione]+ Definizione: relazione di ordine stretto
> 
> Dato un [insieme](Insiemistica.md#^Definizione-insieme) $A$, una [relazione di ordine](Relazioni%20tra%20insiemi.md#^Definizione-relazione-di-ordine) $\mathcal{R}$ su $A$ si dice **stretta** se rispetta le seguenti [proprietà](Relazioni%20tra%20insiemi.md#^Definizione-proprieta-delle-relazioni-binarie):
> - **Irriflessività**: $\forall a \in A (\lnot(a \mathcal{R} a ))$.
> - **Transitività**: $\forall a,b,c \in A (a \mathcal{R} b \land b \mathcal{R} c \implies a \mathcal{R} c)$.

%% 
Esempi:
- La relazione < su N o su R
- L'inclusione stretta $\subsetneq$ su $\mathcal{P}(A)$
%%

%% 
Per indicare gli ordini stretti spesso si usano i simboli per gli ordini senza la
parte che richiama l'uguaglianza, ad esempio
< ≺ ◁ ⊏ . . .

Scriveremo ad esempio \langleA, ≺\rangle per indicare che ≺ è definito su A.
Vedremo a breve che un ordine stretto è esattamente la parte stretta di un ordine (che minghie significa?).
%%

%%
Esempio: discendenti e antenati
Sia A l'insieme di tutti gli esseri umani. Definiamo la relazione ◁ su A ponendo
a ◁ b se e solo se a è un/una discendente di b.
(Equivalentemente, a ◁ b se e solo se b è un/una antenato/a di a.)
La relazione ◁ è chiaramente irriflessiva, perché nessuno è discendente di se stesso.
Inoltre, se a è un discendente di b e b è un discendente di c, allora anche a è un discendente di c: quindi ◁ è transitiva.
Questo mostra che ◁ è un ordine stretto.
%%

%% 
Proposizione: relazione tra ordini stretti e ordini
Dato un qualunque ordine ⪯ su un insieme A, possiamo considerare la sua parte stretta ≺ definita da
a ≺ b se e solo se a ⪯ b \land a̸ = b.
Si verifica facilmente che ≺ è ancora una relazione transitiva.

Dimostrazione:
(Supponiamo a ≺ b ≺ c. Allora a ⪯ c per la transitività di ⪯. Se per assurdo a = c, allora si avrebbe a ⪯ b e b ⪯ c = a, quindi a = b per l'antisimmetria di ⪯, assurdo. Segue che a̸ = c, e quindi a ≺ c.)
Inoltre ≺ è irriflessiva: per definizione non c'è nessun elemento a \in A per cui valga a ≺ a.
Questo mostra che, in accordo con la terminologia usata, la parte stretta di un ordine è sempre un ordine stretto.

Viceversa, dato un ordine stretto ≺ su A possiamo canonicamente costruire la relazione binaria ⪯ su A definita da
a ⪯ b se e solo se (a ≺ b \lor a = b).
Si verifica facilmente che ⪯ è un ordine:
Riflessività Immediato dalla definizione: a ⪯ a poiché ovviamente a = a.
Antisimmetria Supponiamo per assurdo che ci siano a̸ = b tali che a ⪯ b e b ⪯ a. Allora per definizione di ⪯ si deve avere a ≺ b e b ≺ a (poiché abbiamo assunto a̸ = b). Usando la transitività di ≺ concludiamo che a ≺ a, in contraddizione con l'irriflessività di ≺.
Transitività Supponiamo che a ⪯ b e b ⪯ c. Se a = b oppure b = c allora banalmente a ⪯ c. Possiamo quindi assumere che a, b e c siano distinti. Per definizione di ⪯ si ha allora a ≺ b e b ≺ c, da cui a ≺ c per transitività di ≺. Segue che a ⪯ c.

Dunque ogni ordine stretto è necessariamente la parte stretta di un ordine.
%%

## 3.5 - Relazione di pre-ordine

> [!definizione]+ Definizione: relazione di pre-ordine
> 
> Dato un [insieme](Insiemistica.md#^Definizione-insieme) $A$, una [relazione binaria](Relazioni%20tra%20insiemi.md#^Definizione-relazione-n-aria) $\precsim$ su $A$ si dice _**di pre-ordine**_ (o _**di quasi-ordine**_) se rispetta le seguenti [proprietà](Relazioni%20tra%20insiemi.md#^Definizione-proprieta-delle-relazioni-binarie):
> - **Riflessività**: $\forall a \in A (a \mathcal{R} a )$.
> - **Transitività**: $\forall a,b,c \in A (a \mathcal{R} b \land b \mathcal{R} c \implies a \mathcal{R} c)$.

%% 
Esempio
La classifica del campionato di serie A è un pre-ordine \precsim (lineare)
sull'insieme delle squadre X: se la squadra S ha n punti e la squadra T ha
m punti, diciamo che S \precsim T ("S precede T nella classifica") se e solo se
n \ge m. Si verifica allora che la relazione \precsim `e:
riflessiva: S \precsim S per ogni S \in X;
transitiva: per ogni S, T, U \in X, se S \precsim T e T \precsim U allora S \precsim U ;
ma non è antisimmetrica: può accadere che S \precsim T e T \precsim S per due squadre distinte S, T \in X (S e T sono a pari merito).
Dunque si tratta di un pre-ordine e non di un ordine.
%%

%% 
Proposizione
Se \precsim è un pre-ordine su A, allora
a \sim b \iff a \precsim b \land b \precsim a
è una relazione di equivalenza su A (detta relazione di equivalenza
indotta da \precsim) e la relazione su A/\sim
[a]\sim \le [b]\sim \iff a \precsim b
è ben definita ed è un ordine (detto ordine indotto da \precsim).

Ad esempio, nella classifica del campionato di serie A (vista come
pre-ordine \precsim), le classi di equivalenza rispetto alla relazione \sim indotta da
\precsim sono gli insiemi di squadre a parimerito (cioè con lo stesso numero di
punti). L'ordine \le indotto su tali classi di equivalenza è quella che ordina
questi gruppi di squadre in base al punteggio ottenuto: l'insieme delle
squadre che hanno 20 punti formano una classe di equivalenza che precede
la classe di equivalenza delle squadre che hanno 19 punti, e così via.

Dimostrazione di "La relazione \sim definita da a \sim b \iff a \precsim b \land b \precsim a è una relazione d'equivalenza":
Dimostrazione.
`E evidentemente riflessiva, dato che lo è \precsim.
Se a \sim b allora a \precsim b \land b \precsim a e quindi b \precsim a \land a \precsim b, cioè b \sim a; quindi \sim
è simmetrica.
Se a \sim b e b \sim c, allora a \precsim b \land b \precsim a e b \precsim c \land c \precsim b, da cui per
transitività di \precsim si ha a \precsim c \land c \precsim a, cioè a \sim c
$\blacksquare$

Dimostrazione di "La relazione su A/\sim
[a]\sim \le [b]\sim ⇐⇒ a \precsim b
è ben definita ed è un ordine.":
Dimostrazione.
Supponiamo che a \precsim b e a′ \sim a e b′ \sim b: allora a′ \precsim a e b \precsim b′ quindi
a′ \precsim b′ per la transitività di \precsim. Ne segue che la definizione di \le su A/\sim `e
ben posta, dato che non dipende dal rappresentante.
`E immediato verificare che \le è riflessiva e transitiva, quindi è sufficiente
verificare che è antisimmetrica. Se [a]\sim \le [b]\sim e [b]\sim \le [a]\sim, allora
a \precsim b \land b \precsim a, da cui a \sim b per definizione, e quindi [a]\sim = [b]\sim.
%%

# Fonti

- Lezioni dei Prof. Chen Yu e Terracini Lea del corso di Matematica Discreta (canale C), Corso di Laurea in Informatica presso l'Università di Torino, A.A. 2023-24.
- Lezioni del Prof. Radeschi Marco del corso di Algebra Lineare (canale C), Corso di Laurea in Informatica presso l'Università di Torino, A.A. 2023-24.
- Slide del Prof. Viale Matteo del corso di Logica Matematica (canale B), Corso di Laurea in Informatica presso l'Università di Torino, A.A. 2024-25:
	- [2.2 - Relazioni_moodle.pdf](https://informatica.i-learn.unito.it/pluginfile.php/417200/mod_folder/content/0/2.2%20-%20Relazioni_moodle.pdf)

