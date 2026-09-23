---
aliases:
  - Strutture algebriche
---

> [!premessa]+ Premessa
> 
> Ciao! Se è la prima volta che capiti su questo sito, ti consiglio di consultare la [pagina principale](index.md) di questo cosiddetto _Giardino Digitale_ per scoprire meglio cos'è e come navigarlo.
> 
> Lo stato di questa nota è al momento: 🔴 <font color="#FF7F7F">_Bozza_</font>.

---

I vari insiemi numerici%% Link %% sono accomunati da diverse proprietà algebriche che li caratterizzano. Proviamo quindi a esplicitare quali sono queste proprietà e diamo un nome agli [insiemi](Teoria%20degli%20insiemi.md#^definizione-insieme) dotati di operazioni che le soddisfano.

> [!definizione]+ Definizione: struttura algebrica
> 
> Una **struttura algebrica** è un [insieme](Teoria%20degli%20insiemi.md#^definizione-insieme) non [vuoto](Teoria%20degli%20insiemi.md#^definizione-insieme-vuoto) $S$, detto **insieme sostegno** della struttura, dotato di una o più operazioni $\star,{\color{#7F7FFF} \otimes },\ldots$ che rispettano determinate proprietà e viene indicato come
> $$
> (S, \star,{\color{#7F7FFF} \otimes },\ldots)
> $$
^definizione-struttura-algebrica

# 1 - Gruppi

> [!definizione]+ Definizione: gruppo
> 
> Un **gruppo** è una [struttura algebrica](Strutture%20algebriche.md#^definizione-struttura-algebrica) $(G, \star)$ in cui l'[insieme sostegno](Strutture%20algebriche.md#^definizione-struttura-algebrica) $G$ è dotato di un'operazione binaria%% Link %% $\star$ che soddisfa i seguenti assiomi:
> 1. Esistenza dell'elemento neutro $e \in G$%% link %%:
> 	$$
> 	\exists e \in G, \forall a \in G .(e \star a = a \star e = a)
> 	$$
> 2. Proprietà associativa%% Link %%:
> 	$$
> 	\forall a,b,c \in G . \big(a \star (b \star c) = (a \star b) \star c \big)
> 	$$
> 3. Esistenza dell'inverso%% link %% $a' \in G$:
> 	$$
> 	\forall a \in G, \exists a' \in G . (a \star a' = a' \star a = e)
> 	$$
^definizione-gruppo

> [!esempio]- Esempio: gruppi con l'insieme dei numeri interi $\color{#7F7FFF} \mathbb{Z}$
> 
> La [struttura algebrica](Strutture%20algebriche.md#^definizione-struttura-algebrica) $(\mathbb{Z}, +)$ formata dall'insieme dei numeri interi $\mathbb{Z}$%% link %% e l'operazione%% link %% di addizione%% link %% $+$ è un [gruppo](Strutture%20algebriche.md#^definizione-gruppo), infatti:
> 1. Esiste l'elemento neutro%% link %% $0 \in \mathbb{Z}$:
> 	$$
> 	\forall a \in \mathbb{Z} . (0 + a = a + 0 = a)
> 	$$
> 2. Vale la proprietà associativa%% link %%:
> 	$$
> 	\forall a,b,c \in \mathbb{Z} . \big( a + (b+c) = (a+b)+c \big) 
> 	$$
> 3. Ogni numero intero $a \in \mathbb{Z}$ ha un suo inverso $a' = -a \in \mathbb{Z}$:
> 	$$
> 	\forall a \in \mathbb{Z}, \exists - a \in \mathbb{Z} . \big(a + (-a) = (-a) + a = e = 0\big)
> 	$$
> 
> Notiamo che invece non è un [gruppo](Strutture%20algebriche.md#^definizione-gruppo) la [struttura algebrica](Strutture%20algebriche.md#^definizione-struttura-algebrica) $(\mathbb{Z}, \cdot)$ perché non è soddisfatta la proprietà 3, ossia per ogni $a \in \mathbb{Z}$ non esiste un inverso%% Link %% $a' \in \mathbb{Z}$ tale che $a \cdot a' = e$ (elemento neutro $e$ il numero $1 \in \mathbb{Z}$) perché, per esempio, l'inverso di $2$ è $\dfrac{1}{2}$ che non fa parte di $\mathbb{Z}$ ma dell'insieme dei numeri razionali $\mathbb{Q}$%% link %%.
^esempio-gruppi-con-l-insieme-dei-numeri-interi-z

%%
Esempio: $(S_n, \circ)$ è un gruppo, dove $S_n$ è l'insieme formato da tutte le $n!$ permutazioni dell'insieme $X = \{ 1, 2, \ldots, n \}$:
1. $e = \text{id} \in S_n$
2. $\forall \rho, \sigma, \tau \in S_n. \big( \rho \circ (\sigma \circ \tau) = (\rho \circ \sigma) \circ \tau \big)$
3. ogni permutaizone $\sigma$ ha un'inversa $\sigma^{-1}$ tale che $\sigma \circ \sigma^{-1} = e = \text{id}$

Il gruppo $S_n$ è detto **gruppo simmetrico** (gruppo formato dall'insieme delle permutazioni dei suoi elementi, cioè dall'insieme delle funzioni biiettive di tale insieme in se stesso, munito dell'operazione binaria di composizione di funzioni)

A differenza degli altri insiemi numerici, $S_n$ contiene un numero finito di elementi e non è commutativo se $n \ge 3$: per esempio le trasposizioni $(1\ 2)$ e $(2\ 3)$ non commutano:

$$
(2\ 3\ 1) = (1\ 2) \circ (2\ 3) \ne (2\ 3) \circ (1\ 2) = (1\ 3\ 2)
$$
%%

## 1.1 - Gruppi abeliani

> [!definizione]+ Definizione: gruppo abeliano
> 
> Un **gruppo abeliano** (o **gruppo commutativo**) è un [gruppo](Strutture%20algebriche.md#^definizione-gruppo) $(G, \star)$ in cui vale anche la proprietà commutativa%% link %% per l'operazione%% link %% $\star$, ossia una [struttura algebrica](Strutture%20algebriche.md#^definizione-struttura-algebrica) in cui valgono i seguenti assiomi:
> 1. Esistenza dell'elemento neutro $e \in G$%% link %%:
> 	$$
> 	\exists e \in G, \forall a \in G .(e \star a = a \star e = a)
> 	$$
> 2. Proprietà associativa%% Link %%:
> 	$$
> 	\forall a,b,c \in G . \big(a \star (b \star c) = (a \star b) \star c \big)
> 	$$
> 3. Esistenza dell'inverso%% link %% $a' \in G$:
> 	$$
> 	\forall a \in G, \exists a' \in G . (a \star a' = a' \star a = e)
> 	$$
> 4. Proprietà commutativa%% link %%:
> 	$$
> 	\forall a,b \in G . (a \star b = b \star a)
> 	$$
^definizione-gruppo-abeliano

> [!esempio]- Esempio: $\color{#7F7FFF} (\mathbb{Z}, +)$ è un gruppo abeliano
> 
> La [struttura algebrica](Strutture%20algebriche.md#^definizione-struttura-algebrica) $(\mathbb{Z}, +)$ è un [gruppo](Strutture%20algebriche.md#^definizione-gruppo) (come [abbiamo già visto](Strutture%20algebriche.md#^esempio-gruppi-con-l-insieme-dei-numeri-interi-z)), ma anche un [gruppo abeliano](Strutture%20algebriche.md#^definizione-gruppo-abeliano) perché vale la proprietà commutativa%% link %%, infatti
> 
> $$
> \forall a,b \in \mathbb{Z} . (a + b = b + a)
> $$

## 1.2 - Teoremi sui gruppi

> [!proposizione]+ Proposizione: unicità dell'elemento neutro nei gruppi
> 
> In un [gruppo](Strutture%20algebriche.md#^definizione-gruppo) $(G, \star)$ l'elemento inverso%% link %% $a' \in G$ è unico, ossia
> 
> $$
> \forall a, a', a'' \in G . \left(
> \begin{array}{}
> a \star a' = a' \star a = e \\
> \land
> \\
> a \star a'' = a'' \star a = e \\
> \end{array}
> \implies
> a' = a''
> \right)
> $$
^proposizione-unicita-dell-elemento-neutro-nei-gruppi

> [!dimostrazione]- Dimostrazione: unicità dell'elemento neutro nei gruppi
> 
> La dimostrazione dell'[unicità dell'elemento neutro nei gruppi](Strutture%20algebriche.md#^proposizione-unicita-dell-elemento-neutro-nei-gruppi) è frutto di una sequenza di uguaglianze:
> 
> $$
> \begin{align*}
> a' &= a' \star e \\
> &= a' \star (a \star a'') \\
> &= (a' \star a) \star a'' \\
> &= e \star a'' \\
> &= a''
> \end{align*}
> $$
> 
> Otteniamo infine che $a' = a''$.
> 
> $\blacksquare$

Nei [gruppi](Strutture%20algebriche.md#^definizione-gruppo) è anche facile dimostrare che è possibile _cancellare_ degli elementi dalle uguaglianze.

> [!proposizione]+ Proposizione: leggi di cancellazione nei gruppi
> 
> In un [gruppo](Strutture%20algebriche.md#^definizione-gruppo) $(G, \star)$, un elemento $a \in G$ può essere cancellato da entrambi i membri%% link %% di un'uguaglianza%% link %% purché si trovi dalla stessa parte, ossia vale
> 
> $$
> \forall a,b,c \in G .
> \left(
> \begin{array}{}
> a \star b = a \star c \implies b = c
> \\
> \land
> \\
> b \star a = c \star a \implies b = c
> \end{array}
> \right)
> $$
^proposizione-leggi-di-cancellazione-nei-gruppi

> [!dimostrazione]- Dimostrazione: leggi di cancellazione nei gruppi
> 
> Dimostriamo le [leggi di cancellazione nei gruppi](Strutture%20algebriche.md#^proposizione-leggi-di-cancellazione-nei-gruppi) usando l'elemento neutro%% link %% $e$.
> 
> Nelle biimplicazioni%% link %% di colore rosso $\color{#FF7F7F} \Updownarrow$ notiamo che abbiamo sfruttato la proprietà associativa%% Link %% dei [gruppi](Strutture%20algebriche.md#^definizione-gruppo).
> 
> Per la cancellazione a sinistra, moltiplichiamo entrambi i membri per $a^{-1}$ a sinistra:
> 
> $$
> \begin{align*}
> a \star b &= a \star c \\
> &\Updownarrow \\
> a^{-1} \star (a \star b) &= a^{-1} \star (a \star c) \\
> &\color{#FF7F7F} \Updownarrow \\
> (a^{-1} \star a) \star b &= (a^{-1} \star a) \star c \\
> &\Updownarrow \\
> e \star b &= e \star c \\
> &\Updownarrow \\
> b &= c
> \end{align*}
> $$
> 
> Per la cancellazione a destra, moltiplichiamo invece entrambi i membri per $a^{-1}$ a destra:
> 
> $$
> \begin{align*}
> b \star a &= c \star a \\
> &\Updownarrow \\
> (b \star a) \star a^{-1} &= (c \star a) \star a^{-1} \\
> &\color{#FF7F7F} \Updownarrow \\
> b \star (a \star a^{-1}) &= c \star (a \star a^{-1}) \\
> &\Updownarrow \\
> b \star e &= c \star e \\
> &\Updownarrow \\
> b &= c
> \end{align*}
> $$
> 
> Otteniamo quindi in entrambi i casi che $b=c$.
> 
> $\blacksquare$

In un [gruppo](Strutture%20algebriche.md#^definizione-gruppo) $(G, \star)$ generalmente non vale

$$
\forall a,b,c \in G (a \star b = c \star a \implies b = c)
$$

perché il termine $a$ non compare sempre allo stesso lato dell'operazione $\star$. 

Per esempio, prendendo il [gruppo](Strutture%20algebriche.md#^definizione-gruppo) $(S_n, \circ)$, non vale

$$
(1\ 2)\circ(2\ 3) = (1\ 3) \circ (1\ 2) \not\implies (2\ 3) = (1\ 3)
$$

Possiamo però evidenziare come questa regola valga solo per i [gruppi abeliani](Strutture%20algebriche.md#^definizione-gruppo-abeliano).

> [!proposizione]+ Proposizione: legge di cancellazione incrociata nei gruppi abeliani
> 
> In un [gruppo abeliano](Strutture%20algebriche.md#^definizione-gruppo-abeliano) $(G, \star)$, un elemento $a \in G$ può essere cancellato da entrambi i membri%% link %% di un'uguaglianza%% link %% anche se si trova non dallo stesso alto dell'uguaglianza, ossia vale
> 
> $$
> \forall a,b,c\in G. (a\star b=c\star a\implies b=c)
> $$
> ^proposizione-legge-di-cancellazione-incrociata-nei-gruppi-abeliani

> [!dimostrazione]- Dimostrazione: legge di cancellazione incrociata nei gruppi abeliani
> 
> Dimostriamo la [legge di cancellazione incrociata nei gruppi abeliani](Strutture%20algebriche.md#^proposizione-legge-di-cancellazione-incrociata-nei-gruppi-abeliani).
> 
> Nelle biimplicazioni%% link %% di colore rosso $\color{#FF7F7F} \Updownarrow$ notiamo che abbiamo sfruttato la proprietà commutativa%% Link %% dei [gruppi abeliani](Strutture%20algebriche.md#^definizione-gruppo-abeliano).
> 
> Dato un [gruppo abeliano](Strutture%20algebriche.md#^definizione-gruppo-abeliano) $(G, \star)$ e tre elementi $a,b,c \in G$, otteniamo che
> 
> $$
> \begin{array}{}
> a \star b = c \star a \\
> {\color{#FF7F7F} \Updownarrow } \\
> a \star b = a \star c \\
> \Updownarrow \\
> b=c
> \end{array}
> $$
> 
> e, viceversa,
> 
> $$
> \begin{array}{}
> b \star a = a \star c \\
> {\color{#FF7F7F} \Updownarrow } \\
> b \star a = c \star a \\
> \Updownarrow \\
> b=c
> \end{array}
> $$
> 
> per le [leggi di cancellazione nei gruppi](Strutture%20algebriche.md#^proposizione-leggi-di-cancellazione-nei-gruppi).
> 
> $\blacksquare$

# 2 - Anelli

> [!definizione]+ Definizione: anello
> 
> Un **anello** è una [struttura algebrica](Strutture%20algebriche.md#^definizione-struttura-algebrica) $(A, {\color{#FF7F7F} \oplus }, {\color{#7F7FFF} \otimes })$ in cui l'[insieme sostegno](Strutture%20algebriche.md#^definizione-struttura-algebrica) $A$ è dotato di due operazioni binarie%% Link %% ${\color{#FF7F7F} \oplus }$ e ${\color{#7F7FFF} \otimes }$ che soddisfano i seguenti assiomi:
> 1. Esistenza dell'elemento neutro $e_{\color{#FF7F7F} \oplus } \in A$%% link %% per l'operazione ${\color{#FF7F7F} \oplus }$:
> 	$$
> 	\exists e_{\color{#FF7F7F} \oplus } \in A, \forall a \in A .(e_{\color{#FF7F7F} \oplus }\ {\color{#FF7F7F} \oplus }\ a = a\ {\color{#FF7F7F} \oplus }\ e_{\color{#FF7F7F} \oplus } = a)
> 	$$
> 2. Esistenza dell'elemento neutro $e_{\color{#7F7FFF} \otimes } \in A$%% link %% per l'operazione ${\color{#7F7FFF} \otimes }$:
> 	$$
> 	\exists e_{\color{#7F7FFF} \otimes } \in A, \forall a \in A .(e_{\color{#7F7FFF} \otimes }\ {\color{#7F7FFF} \otimes }\ a = a\ {\color{#7F7FFF} \otimes }\ e_{\color{#7F7FFF} \otimes } = a)
> 	$$
> 3. Proprietà associativa%% Link %% per l'operazione ${\color{#FF7F7F} \oplus }$:
> 	$$
> 	\forall a,b,c \in A . \big(a\ {\color{#FF7F7F} \oplus }\ (b\ {\color{#FF7F7F} \oplus }\ c) = (a\ {\color{#FF7F7F} \oplus }\ b)\ {\color{#FF7F7F} \oplus }\ c \big)
> 	$$
> 4. Proprietà associativa%% link %% per l'operazione ${\color{#7F7FFF} \otimes }$:
> 	$$
> 	\forall a,b,c \in A . \big(a\ {\color{#7F7FFF} \otimes }\ (b\ {\color{#7F7FFF} \otimes }\ c) = (a\ {\color{#7F7FFF} \otimes }\ b)\ {\color{#7F7FFF} \otimes }\ c \big)
> 	$$
> 5. Esistenza dell'inverso%% link %% $a' \in A$ per l'operazione ${\color{#FF7F7F} \oplus }$:
> 	$$
> 	\forall a \in A, \exists a' \in A . (a\ {\color{#FF7F7F} \oplus }\ a' = a'\ {\color{#FF7F7F} \oplus }\ a = e_{\color{#FF7F7F} \oplus })
> 	$$
> 6. Proprietà commutativa%% link %% per l'operazione ${\color{#FF7F7F} \oplus }$:
> 	$$
> 	\forall a,b \in A . (a\ {\color{#FF7F7F} \oplus }\ b = b\ {\color{#FF7F7F} \oplus }\ a)
> 	$$
> 7. Proprietà distributiva%% link %%:
> 	$$
> 	\forall a,b,c \in A. \left( \begin{array}{}
> 	a\ {\color{#7F7FFF} \otimes }\ (b\ {\color{#FF7F7F} \oplus }\ c) = (a\ {\color{#7F7FFF} \otimes }\ b)\ {\color{#FF7F7F} \oplus }\ (a\ {\color{#7F7FFF} \otimes }\ c) \\
> 	\land \\
> 	(b\ {\color{#FF7F7F} \oplus }\ c)\ {\color{#7F7FFF} \otimes }\ a = (b\ {\color{#7F7FFF} \otimes }\ a)\ {\color{#FF7F7F} \oplus }\ (c\ {\color{#7F7FFF} \otimes }\ a)
> 	\end{array} \right) 
> 	$$
^definizione-anello

%% 
esempi: $(\mathbb{Z}, +, \cdot)$ sono anello,
%%

%% 
anello commutativo se vale la proprietà commutativa anche per ${\color{#7F7FFF} \otimes }$
%%

Gli [anelli](Strutture%20algebriche.md#^definizione-anello) possiedono proprietà interessanti per quanto riguarda i due elementi neutri%% link %% $e_{\color{#FF7F7F} \oplus }$ e $e_{\color{#7F7FFF} \otimes }$ rispettivamente per le operazioni%% link %% ${\color{#FF7F7F} \oplus }$ e ${\color{#7F7FFF} \otimes }$: in particolare, possiamo verificare che l'elemento neutro%% link %% $e_{\color{#FF7F7F} \oplus }$ di ${\color{#FF7F7F} \oplus }$ è anche l'elemento assorbente%% Link %% di ${\color{#7F7FFF} \otimes }$.

Per esempio, per l'[anello](Strutture%20algebriche.md#^definizione-anello) $(\mathbb{Z}, +, \cdot)$ l'elemento neutro $0$ di $+$ è l'elemento assorbente%% Link %% di $\cdot$.

> [!proposizione] Proposizione: elemento neutro e assorbente
> 
> Dato un [anello](Strutture%20algebriche.md#^definizione-anello) $(A, {\color{#FF7F7F} \oplus }, {\color{#7F7FFF} \otimes })$ con $e_{\color{#FF7F7F} \oplus }$ elemento neutro%% link %% di ${\color{#FF7F7F} \oplus }$, abbiamo che $e_{{\color{#FF7F7F} \oplus }}$ è anche l'elemento assorbente%% Link %% di ${\color{#7F7FFF} \otimes }$:
> 
> $$
> \forall a \in A .(e_{\color{#FF7F7F} \oplus }\ {\color{#7F7FFF} \otimes }\ a = a\ {\color{#7F7FFF} \otimes }\ e_{\color{#FF7F7F} \oplus } = e_{\color{#FF7F7F} \oplus }) 
> $$
^proposizione-elemento-neutro-e-assorbente

> [!dimostrazione] Dimostrazione: elemento neutro e assorbente
> 
> Dimostriamo che in un [anello](Strutture%20algebriche.md#^definizione-anello) $(A, {\color{#FF7F7F} \oplus }, {\color{#7F7FFF} \otimes })$ [l'elemento neutro $e_{\color{#FF7F7F} \oplus }$ di ${\color{#FF7F7F} \oplus }$ è anche l'elemento assorbente di ${\color{#7F7FFF} \otimes }$](Strutture%20algebriche.md#^proposizione-elemento-neutro-e-assorbente) attraverso una serie di uguaglianze:
> 
> $$
> \begin{align*}
> e_{\color{#FF7F7F} \oplus }\ {\color{#7F7FFF} \otimes }\ a &= (e_{\color{#FF7F7F} \oplus }\ {\color{#FF7F7F} \oplus }\ e_{\color{#FF7F7F} \oplus })\ {\color{#7F7FFF} \otimes }\ a \\
> &= (e_{\color{#FF7F7F} \oplus }\ {\color{#7F7FFF} \otimes }\ a)\ {\color{#FF7F7F} \oplus }\ (e_{\color{#FF7F7F} \oplus }\ {\color{#7F7FFF} \otimes }\ a) \\
> &= e_{\color{#FF7F7F} \oplus }\ {\color{#FF7F7F} \oplus }\ e_{\color{#FF7F7F} \oplus } \\
> &= e_{\color{#FF7F7F} \oplus }
> \end{align*}
> $$
> 
> E analogamente si può dimostrare che vale anche $a\ {\color{#7F7FFF} \otimes }\ e_{\color{#FF7F7F} \oplus } = e_{\color{#FF7F7F} \oplus }$.
> 
> $\blacksquare$

%% 
unicità dell'elemento neutro e_\times
%%

# Campi

> [!definizione]+ Definizione: campo
> 
> Un **campo** è una [struttura algebrica](Strutture%20algebriche.md#^definizione-struttura-algebrica) $(C, {\color{#FF7F7F} \oplus }, {\color{#7F7FFF} \otimes })$ in cui l'[insieme sostegno](Strutture%20algebriche.md#^definizione-struttura-algebrica) $C$ è dotato di due operazioni binarie%% Link %% ${\color{#FF7F7F} \oplus }$ e ${\color{#7F7FFF} \otimes }$ che soddisfano i seguenti assiomi:
> 1. Esistenza dell'elemento neutro $e_{\color{#FF7F7F} \oplus } \in C$%% link %% per l'operazione ${\color{#FF7F7F} \oplus }$:
> 	$$
> 	\exists e_{\color{#FF7F7F} \oplus } \in C, \forall a \in C .(e_{\color{#FF7F7F} \oplus }\ {\color{#FF7F7F} \oplus }\ a = a\ {\color{#FF7F7F} \oplus }\ e_{\color{#FF7F7F} \oplus } = a)
> 	$$
> 2. Esistenza dell'elemento neutro $e_{\color{#7F7FFF} \otimes } \in C$%% link %% per l'operazione ${\color{#7F7FFF} \otimes }$:
> 	$$
> 	\exists e_{\color{#7F7FFF} \otimes } \in C, \forall a \in C .(e_{\color{#7F7FFF} \otimes }\ {\color{#7F7FFF} \otimes }\ a = a\ {\color{#7F7FFF} \otimes }\ e_{\color{#7F7FFF} \otimes } = a)
> 	$$
> 3. Proprietà associativa%% Link %% per l'operazione ${\color{#FF7F7F} \oplus }$:
> 	$$
> 	\forall a,b,c \in C . \big(a\ {\color{#FF7F7F} \oplus }\ (b\ {\color{#FF7F7F} \oplus }\ c) = (a\ {\color{#FF7F7F} \oplus }\ b)\ {\color{#FF7F7F} \oplus }\ c \big)
> 	$$
> 4. Proprietà associativa%% link %% per l'operazione ${\color{#7F7FFF} \otimes }$:
> 	$$
> 	\forall a,b,c \in C . \big(a\ {\color{#7F7FFF} \otimes }\ (b\ {\color{#7F7FFF} \otimes }\ c) = (a\ {\color{#7F7FFF} \otimes }\ b)\ {\color{#7F7FFF} \otimes }\ c \big)
> 	$$
> 5. Esistenza dell'inverso%% link %% $a' \in C$ per l'operazione ${\color{#FF7F7F} \oplus }$:
> 	$$
> 	\forall a \in C, \exists a' \in C . (a\ {\color{#FF7F7F} \oplus }\ a' = a'\ {\color{#FF7F7F} \oplus }\ a = e_{\color{#FF7F7F} \oplus })
> 	$$
> 6. Esistenza dell'inverso%% link %% $a'' \in C$ per l'operazione ${\color{#7F7FFF} \otimes }$:
> 	$$
> 	\forall a \in C, \exists a'' \in C . (a\ {\color{#7F7FFF} \otimes }\ a'' = a''\ {\color{#7F7FFF} \otimes }\ a = e_{\color{#7F7FFF} \otimes })
> 	$$
> 7. Proprietà commutativa%% link %% per l'operazione ${\color{#FF7F7F} \oplus }$:
> 	$$
> 	\forall a,b \in C . (a\ {\color{#FF7F7F} \oplus }\ b = b\ {\color{#FF7F7F} \oplus }\ a)
> 	$$
> 8. Proprietà commutativa%% link %% per l'operazione ${\color{#7F7FFF} \otimes }$:
> 	$$
> 	\forall a,b \in C . (a\ {\color{#7F7FFF} \otimes }\ b = b\ {\color{#7F7FFF} \otimes }\ a)
> 	$$
> 9. Proprietà distributiva%% link %%:
> 	$$
> 	\forall a,b,c \in C. \left( \begin{array}{}
> 	a\ {\color{#7F7FFF} \otimes }\ (b\ {\color{#FF7F7F} \oplus }\ c) = (a\ {\color{#7F7FFF} \otimes }\ b)\ {\color{#FF7F7F} \oplus }\ (a\ {\color{#7F7FFF} \otimes }\ c) \\
> 	\land \\
> 	(b\ {\color{#FF7F7F} \oplus }\ c)\ {\color{#7F7FFF} \otimes }\ a = (b\ {\color{#7F7FFF} \otimes }\ a)\ {\color{#FF7F7F} \oplus }\ (c\ {\color{#7F7FFF} \otimes }\ a)
> 	\end{array} \right) 
> 	$$
^definizione-campo

%% 
esercizi pagg. 36-38
%%

---

> [!fonti]+ Fonti
> 
> - 📚 Bruno Martelli, _Geometria e algebra lineare_, autopubblicato, 2025:
> 	- Capitolo 1 - _Nozioni preliminari_:
> 		- 1.5 - _Strutture algebriche_.
