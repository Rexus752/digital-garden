---
draft: true
---
%%
tabella connettivi:
- nome
- simbolo
- tabella di verità
- trascrizione a parole

Altro materiale da vedere:
- https://it.wikipedia.org/wiki/Logica_intensionale
%%



# Operatori logici

Ci sono alcune espressioni che ricorrono in ogni testo matematico:
- le particelle “non”, “e”, “o”
- “se ... allora ...”
- “... se e solo se ...”
- “c’è almeno un $x$ tale che ...”
- “per ogni $x$ ...”

Per scrivere in modo non ambiguo i ragionamenti e le dimostrazioni introduciamo dei simboli che rappresentano questi costrutti linguistici, ovvero i connettivi $\lnot, \lor, \land, \to, \leftrightarrow$ ed i simboli di quantificatore $\exists, \forall$.  

I connettivi e i quantificatori si dicono costanti logiche.
Cominciamo con i connettivi, richiamando il loro significato e alcune delle loro proprietà di base.

Ogni connettivo è completamente descritto dalla sua tavola di verità. A partire da affermazioni di base $A, B, C, \ldots$ dette _lettere proposizionali_, mediante i connettivi è possibile costruire affermazioni più complesse $P, Q, R, \ldots$ dette _proposizioni_. Ad ogni proposizione $P$ possiamo associare una tavola di verità; se $P$ è costruita a partire da $k$ lettere proposizionali, allora la tavola di verità avrà $2^k$ righe.
La nozione di conseguenza logica $P_1, P_2, \ldots, P_n \vDash Q$ è stata introdotta informalmente come: _ogni qual volta $P_1, P_2, \ldots, P_n$ sono vere, allora anche $Q$ è vera_.

## Conseguenza logica $\vDash$

%%unire alla roba precedente%%

La definizione rigorosa della relazione $\vDash$ è:
Supponiamo $P_1, P_2, \ldots, P_n, Q$ sono proposizioni costruite mediante connettivi a partire dalle lettere $A_1, \ldots, A_k$:
$$
P_1, P_2, \ldots, P_n \vDash Q
$$
se, considerata la tavola di verità di $2^k$ righe contenente le $A_1, \ldots, A_k$ e le affermazioni $P_1, P_2, \ldots, P_n, Q$, per ogni riga per cui il valore di verità di $P_1, P_2, \ldots, P_n$ è VERO, allora anche il valore di verità di $Q$ è VERO.

## <span style="color:#FF88FF; background:#00000000">Definizione: equivalenza logica</span>

Date due proposizioni $P$ e $Q$, se $P \vDash Q$ e $Q \vDash P$, allora $P$ e $Q$ si dicono _logicamente equivalenti_ e si denota $P \equiv Q$.

Se questo accade, vuol dire che in ogni contesto in cui vale $P$ deve valere anche $Q$ e, viceversa, in ogni contesto in cui vale $Q$ deve valere anche $P$; quindi $P$ è vera se e solo se $Q$ è vera.
In altre parole: in ogni possibile contesto, o $P$ e $Q$ sono entrambe vere, oppure sono entrambe false e sono pertanto "indistinguibili" per quel che riguarda l’essere vere o meno.

### <span style="color:#8888FF; background:#00000000">Esempio</span>

Consideriamo le seguenti affermazioni riguardanti un numero reale $x$:
- $P$: $x \ge 0$;
- $Q$: $x = y^2$ per qualche numero reale $y$.

Dato un qualunque numero reale $x$, se $x \ge 0$ allora basta porre $y = \sqrt x$ per avere $x = y^2$, quindi $P \vDash Q$.
D’altra parte, se $x = y^22$ per qualche numero reale $y$ allora $x \ge 0$ perché il quadrato di un numero reale è sempre un numero non negativo, quindi $Q \vDash P$.

Abbiamo perciò verificato che per ogni possibile valore di $x$, la proprietà $P$ è vera se e solo se $Q$ è vera. Questo vuole dire che $P$ e $Q$ sono affermazioni equivalenti, ovvero $P \equiv Q$.

### Proprietà dell'equivalenza logica

%% separare le varie proprietà %%
Date tre affermazioni $P$, $Q$ ed $R$ qualsiasi, si ha che:
- Riflessività: $P \equiv P$;
- Simmetria: se $P \equiv Q$, allora anche $Q \equiv P$;
- Transitività: se $P \equiv Q$ e $Q \equiv R$, allora $P \equiv R$.

La prima e la seconda proprietà sono del tutto ovvie. La terza segue dalla transitività di $\vDash$. Infatti, se $P \equiv Q$ e $Q \equiv R$, allora in particolare $P \vDash Q$ e $Q \vDash R$, da cui $P \vDash R$ per la transitività di $\vDash$. Viceversa, da $P \equiv Q$ e $Q \equiv R$ segue anche che $Q \vDash P$ e $R \vDash Q$, da cui $R \vDash P$ sempre per transitività di $\vDash$. Quindi $P \equiv R$.

## Equivalenza logica $\equiv$

%%unire alla roba precedente%%

L’equivalenza logica
$$
P \equiv Q
$$
è definita come $P \vDash Q$ e $Q \vDash P$. In altre parole:
Se $P$ e $Q$ sono proposizioni costruite a partire dalle lettere $A_1, \ldots, A_k$, allora $P \equiv Q$ se e solo se $P$ e $Q$ hanno la medesima tavola di verità.

## Definizione: negazione

Il simbolo $\lnot$ denota la negazione e serve per affermare l’opposto di quanto asserisce l’affermazione a cui si applica.

Per esempio $\lnot(x < y)$ significa che $x$ non è minore di $y$, ovvero che $x \ge y$. Il significato di $\lnot$ è completamente descritto dalla sua tavola di verità:

| $P$ | $\lnot P$ |
| --- | --------- |
| V   | F         |
| F   | V         |
dove V e F denotano, rispettivamente, il vero e il falso.

Data una proposizione $P$, si ha sempre che $P$ è vera se e solo se $\lnot P$ è falsa, e questo accade se e solo $\lnot\lnot P$ è vera. Questo mostra che $P$ e $\lnot \lnot P$ sono equivalenti, ovvero che vale la medesima tavola di verità.

Legge della doppia negazione: $P \equiv \lnot \lnot P$ e, inoltre, $P \equiv Q \leftrightarrow \lnot P \equiv \lnot Q$.

## Definizione: congiunzione

Il simbolo $\land$ è la congiunzione e serve per asserire che due fatti valgono contemporaneamente.
Per esempio
$$
\text{($x$ è pari) $\land$ ($x$ è un quadrato perfetto)}
$$
significa che il numero $x$ è sia pari che un quadrato perfetto (ovvero è il quadrato di qualche numero): poiché abbiamo dimostrato che se $k^2$ è pari allora anche $k$ lo è, questo vuol dire che $x = (2n)^2 = 4n^2$ per qualche $n \in \mathbb{N}$ . La tavola di verità di $\land$ è:

| $P$ | $Q$ | $P \land Q$ |
| --- | --- | ----------- |
| V   | V   | V           |
| V   | F   | F           |
| F   | V   | F           |
| F   | F   | F           |

Anche le particelle “ma” e “però” sono delle congiunzioni, a cui noi attribuiamo una connotazione avversativa. Tuttavia, in matematica il significato di “$P$ ma $Q$” o di “$P$ però $Q$” è lo stesso di “$P$ e $Q$” e quindi si scrivono comunque come “$P \land Q$”.

### Proprietà

Il connettivo $\land$ è commutativo, poiché asserire $P \land Q$ è come asserire $Q \land P$:
$$
P \land Q \equiv Q \land P
$$
ed è associativo, poiché asserire $P \land (Q \land R)$ è la stessa cosa di asserire $(P \land Q) \land R$ (ovvero: $P$, $Q$ ed $R$ sono tutt'e tre vere):
$$
P \land (Q \land R) \equiv (P \land Q) \land R
$$
Infine:
Se $P \equiv R$ e $Q \equiv S$, allora $P \land Q \equiv R \land S$.

## Definizione: disgiunzione

$\lor$ è la disgiunzione (inclusiva) e corrisponde al _vel_ latino o all'inglese _or_: questo o quello o eventualmente entrambi.
Affermare $P \lor Q$ non vuol dire che soltanto una tra $P$ e $Q$ è vera. Dire
$$
\text{($x$ è pari) $\lor$ ($x$ è un quadrato perfetto)}
$$
significa che x può essere pari (cioè della forma $2n$, per esempio $6$), o un quadrato perfetto (cioè della forma $n^2$, per esempio $9$), o magari un numero che è un quadrato perfetto pari (cioè della forma $4n^2$, per esempio $4$). La tavola di verità di $\lor$ è:

| $P$ | $Q$ | $P \lor Q$ |
| --- | --- | ---------- |
| V   | V   | V          |
| V   | F   | V          |
| F   | V   | V          |
| F   | F   | F          |

### Proprietà

Anche il connettivo $\lor$ è commutativo:
$$
P \lor Q ≡ Q \lor P
$$
e associativo:
$$
P \lor (Q \lor R) ≡ (P \lor Q) \lor R
$$
Se sappiamo che $P$ è vera, allora possiamo anche asserire che $P \lor Q$ è vera, qualsiasi sia $Q$.
Analogamente, se $Q$ è vera allora anche $P \lor Q$ lo è, qualunque sia $P$, quindi:
$$
P \vDash P \lor Q e Q \vDash P \lor Q
$$

Invece a partire da $P ∨ Q$ non possiamo né concludere $P$ né concludere $Q$.
Infatti, se $P ∨ Q$ è vera sappiamo solo che almeno una tra $P$ e $Q$ è vera, ma non possiamo sapere quale (in genere dipenderà dal contesto).
Invece, se sappiamo che $P ∨ Q$ è vera ma che $P$ è falsa, allora l’unica possibilità è che $Q$ sia vera.
Similmente, se $P ∨ Q$ è vera ma $Q$ è falsa, allora possiamo concludere che $P$ deve essere vera.

Legge della disgiunzione:
$$
P ∨ Q, ¬P |= Q e P ∨ Q, ¬Q |= P
$$
Infine
$$
Se P ≡ R e Q ≡ S, allora P ∨ Q ≡ R ∨ S
$$

## Leggi di De Morgan

$$
¬(P ∧ Q) ≡ ¬P ∨ ¬Q
$$
e
$$
¬(P ∨ Q) ≡ ¬P ∧ ¬Q
$$

Possiamo argomentare la validità di queste leggi anche senza le tavole di verità. Se sappiamo che $P ∧ Q$ è falsa, allora almeno una tra $P$ e $Q$ deve essere falsa: questo mostra che $¬(P ∧ Q) |= ¬P ∨ ¬Q$. Viceversa, se sappiamo che almeno una tra $P$ e $Q$ è certamente falsa, allora $P ∧ Q$ è anch'essa falsa: questo dimostra che $¬P ∨ ¬Q |= ¬(P ∧ Q)$, da cui $¬(P ∧ Q) ≡ ¬P ∨ ¬Q$.
Lasciamo al lettore il verificare con ragionamenti analoghi che $¬(P ∨ Q) ≡ ¬P ∧ ¬Q$.

Negando entrambi i termini dell’equivalenza $¬(P ∧ Q) ≡ ¬P ∨ ¬Q$ si ottiene, sfruttando quanto visto per la $¬$, che $¬¬(P ∧ Q) ≡ ¬(¬P ∨ ¬Q)$, da cui per la legge della doppia negazione $P ∧ Q ≡ ¬(¬P ∨ ¬Q)$. Questo vuol dire che la congiunzione $∧$ può essere “definita” a partire da negazione $¬$ e disgiunzione $∨$: ogni affermazione che contenga una congiunzione potrebbe essere riscritta in maniera equivalente utilizzando al suo posto negazioni e disgiunzioni in modo opportuno.

Similmente, partendo da $¬(P ∨ Q) ≡ ¬P ∧ ¬Q$ e ragionando come prima, si verifica che $P ∨ Q ≡ ¬(¬P ∧ ¬Q)$, ovvero che la disgiunzione $∨$ può essere “definita” a partire da negazione $¬$ e congiunzione $∧$.

## Distributività di congiunzione e disgiunzione

Mediante le tavole di verità è facile verificare le seguenti proprietà.

Proprietà distributiva di $∨$ su $∧$
$$
P ∨ (Q ∧ R) ≡ (P ∨ Q) ∧ (P ∨ R)
$$
Proprietà distributiva di $∧$ su $∨$
$$
P ∧ (Q ∨ R) ≡ (P ∧ Q) ∨ (P ∧ R)
$$
Analogamente
$$
(P ∧ Q) ∨ R ≡ (P ∨ R) ∧ (Q ∨ R)
$$
e
$$
(P ∨ Q) ∧ R ≡ (P ∧ R) ∨ (Q ∧ R)
$$

## Definizione: disgiunzione esclusiva

La disgiunzione esclusiva $⊕$ corrisponde al latino aut: _“o questo o quello, ma non entrambi”_. In informatica è nota come _xor_ dall’inglese _“exclusive or”_. La sua tavola di verità è:

| $P$ | $Q$ | $P \oplus Q$ |
| --- | --- | ------------ |
| V   | V   | F            |
| V   | F   | V            |
| F   | V   | V            |
| F   | F   | F            |

E immediato verificare che
$$
P ⊕ Q ≡ ¬(P ↔ Q)
$$
e che
$$
(P ≡ R \land Q ≡ S) \to (P ⊕ Q ≡ R ⊕ S)
$$

### Proprietà: commutatività della disgiunzione esclusiva

Inoltre il connettivo ⊕ è commutativo
$$
P ⊕ Q ≡ Q ⊕ P
$$

### Proprietà: associatività della disgiunzione esclusiva

$$
P ⊕ (Q ⊕ R) ≡ (P ⊕ Q) ⊕ R
$$

## Nor

Il connettivo nor $\overline{\lor}$ corrisponde alla locuzione _“né questo né quello”_.
Quindi asserire $P ¯∨ Q$ è come dire $¬P ∧ ¬Q$, che è equivalente a $¬(P ∨ Q)$.
La sua tavola di verità è

| $P$ | $Q$ | $P \overline{\lor} Q$ |
| --- | --- | --------------------- |
| V   | V   | F                     |
| V   | F   | F                     |
| F   | V   | F                     |
| F   | F   | V                     |

### Commutatività

$$
P ¯∨ Q ≡ Q ¯∨ P
$$
 
### Associatività

$$
P ¯∨ (Q ¯∨ R) ≡ (P ¯∨ Q) ¯∨ R
$$

## Nand

Il connettivo nand $\overline{\land}$ serve per asserire che due affermazioni non valgono simultaneamente. Quindi asserire $P ¯∧ Q$ è come dire $¬(P ∧ Q)$, che è equivalente a $¬P ∨ ¬Q$.
La sua tavola di verità è:

| $P$ | $Q$ | $P \overline{\land} Q$ |
| --- | --- | ---------------------- |
| V   | V   | F                      |
| V   | F   | V                      |
| F   | V   | V                      |
| F   | F   | V                      |

### Commutatività

$$
P ¯∧ Q ≡ Q ¯∧ P
$$
 
### Associatività

$$
P ¯∧ (Q ¯∧ R) ≡ (P ¯∧ Q) ¯∧ R
$$

## Definizione: implicazione

%%
differenza tra implicazione logica materiale $\to$ e implicazione logica semantica $\implies$
https://it.wikipedia.org/wiki/Implicazione_logica#Descrizione
%%

$\to$ è l’implicazione e corrisponde all’espressione “se . . . allora . . . ”.
La sua tavola di verità è

| $P$ | $Q$ | $P \to Q$ |
| --- | --- | -------------- |
| V   | V   | V              |
| V   | F   | F              |
| F   | V   | V              |
| F   | F   | V              |

### Esempio

Precisare il significato dell’implicazione è piuttosto delicato ed è il primo scoglio in cui ci si imbatte quando si formalizza il ragionamento matematico.
Per chiarire la situazione, cominciamo con un esempio. Consideriamo la seguente affermazione riguardante un generico numero reale $x$: _se $\underbrace{x > 0}_{P}$ allora $\underbrace{x = y^2 \text{ per qualche } y \ge 0}_{Q}$_.
Tale frase è chiaramente vera in ogni contesto in cui abbia senso valutarla: infatti, per ogni numero reale $x$ se vale $P$, ovvero $x > 0$, allora basta porre $y = \sqrt x$ per avere che anche $Q$ vale. Notiamo che anche nei contesti in cui $x \ge 0$, ovvero quando $P$ è falsa, non possiamo ritenere l’affermazione precedente errata: semplicemente diremmo che in quel caso non c’è nulla da verificare perché l’affermazione impone vincoli solo per gli $x > 0$ (in
particolare, è ininfluente se $Q$ sia vera o meno in tale contesto).
In altre parole:
L’affermazione _“se $P$ allora $Q$”_ precedente risulterebbe falsa in un dato contesto, ovvero per un dato valore di $x$, solo se si verificasse che $x > 0$ (quindi $P$ è vera) ma $x$ non fosse il quadrato di un numero positivo (quindi $Q$ è falsa).

### Esempio

Proviamo ora a considerare quest’altra affermazione riguardante un generico numero reale $x$.
Se $\underbrace{x > 0}_{P}$, allora $\underbrace{x^2 > 1}_{Q}$.
Anche questa frase è della forma “se $P$ allora $Q$”, ma questa volta non saremo disposti a ritenerla vera in generale: più precisamente, noteremo che ci sono alcuni contesti in cui essa vale (ad esempio quando $x > 1$) e contesti in cui essa non vale. Questi ultimi sono esattamente quelli dati dai valori di $x$ per cui accade che $x > 0$ ($P$ vera) ma $x^2 \le 1$ ($Q$ falsa), ovvero i contesti in cui $0 < x \le 1$.

### Definizione di implicazione da negazione e congiunzione o negazione e disgiunzione

Riassumendo quanto discusso finora, abbiamo quindi che:
- L’affermazione $P \to Q$ è falsa in un dato contesto se e solo se in tale contesto accade che $P$ è vera ma $Q$ è falsa, ovvero se in esso vale $P ∧ ¬Q$;
- Di conseguenza, $P \to Q$ è vera in un dato contesto se e solo se in tale contesto non vale $P ∧ ¬Q$; equivalentemente, se in esso vale $¬P ∨ Q$.

Infatti i nostri ragionamenti (e le tavole di verità) evidenziano che
$$
¬(P → Q) ≡ P ∧ ¬Q e P → Q ≡ ¬(P ∧ ¬Q)
$$
Dalla seconda equivalenza, per le leggi di De Morgan e della doppia negazione
$$
P → Q ≡ ¬P ∨ Q
$$
In particolare, questo vuol dire che l’implicazione può essere “definita” a partire da negazione e congiunzione, oppure a partire da negazione e disgiunzione.

In accordo con la nostra intuizione, il significato dato all’implicazione cattura quello di conseguenza logica: $P |= Q$ se e solo se $|= P → Q$.
Infatti, supponiamo che $P |= Q$. Allora in ogni contesto in cui vale $P$ deve valere anche $Q$: in particolare, in nessun contesto può valere $P ∧ ¬Q$, per cui $|= ¬(P ∧ ¬Q)$. Poiché $¬(P ∧ ¬Q) ≡ P → Q$, abbiamo $|= P → Q$.
Viceversa, supponiamo che $|= P → Q$, ovvero che l’implicazione $P → Q$ sia vera in qualunque contesto. Supponiamo di trovarci in un contesto in cui vale $P$, cosicché vale anche $¬¬P$ per la legge della doppia negazione. Siccome $P → Q ≡ ¬P ∨ Q$, in tale contesto deve valere anche $¬P ∨ Q$. Per la legge della disgiunzione applicata a $¬P ∨ Q$ e $¬¬P$, si ha allora che $Q$ vale in tale contesto. Quindi abbiamo verificato che $P |= Q$.

Più in generale, ricordiamo che $P_1, P_2, \ldots, P_n |= Q$ se in ogni contesto in cui tutte le $P_1, P_2, \ldots, P_n$ sono vere si ha che anche $Q$ è vera. Poiché in ogni contesto si ha che $P_1, P_2, \ldots, P_n$ sono tutte vere se e solo se è vera $P_1 ∧ P_2 \land \ldots ∧ P_n$, allora
$$
P_1, P_2, \ldots, P_n |= Q
$$
se e solo se
$$
P_1 ∧ P_2 \land \ldots ∧ P_n |= Q
$$
se e solo se
$$
|= (P_1 ∧ P_2 \land \ldots∧ P_n) → Q
$$

### Altre espressioni equivalenti all'implicazione

In matematica, si usano anche altre espressioni che sono equivalenti all’implicazione.
Le espressioni _“affinché valga $P$ deve valere $Q$”_ oppure _“affinché valga $P$ è necessario che valga $Q$”_ significano che non può accadere che $P$ valga ma $Q$ no. Il loro significato è quindi equivalente a quello di _“se $P$ allora $Q$”_ e perciò si scrivono, in simboli, $P → Q$.
L’espressione _“affinché valga $P$ è sufficiente che valga $Q$”_ significa che, non appena si sa che $Q$ vale, allora anche $P$ deve valere. Il suo significato è quindi equivalente a quello di _“se $Q$ allora $P$”_ e perciò si scrive, in simboli, $Q → P$.

### Osservazione

L’implicazione cattura il concetto intuitivo di conseguenza. Diciamo che $Q$ è una conseguenza di $P$ se ogni volta che si verifica $P$ allora anche $Q$ si deve verificare, ovvero $P → Q$.
L’implicazione non ha invece nulla a che fare con il concetto di causalità. Infatti, si ritiene usualmente che $P$ sia una causa di $Q$ se è una _condicio sine qua non_, ovvero se non può accadere $Q$ senza che si verifichi $P$.
Questo vuol dire che se c’è un nesso di causalità tra $P$ e $Q$, allora l’unica cosa che possiamo affermare è che $Q → P$; non possiamo invece affermare che $P → Q$, perché non possiamo asserire con certezza che $P$ sia sufficiente, da sola, a causare $Q$ (potrebbero essere necessarie altre concause affinché si verifichi veramente $Q$).

### Osservazione: rapporto logico di causa-conseguenza non necessario

C’è poi un’ultimo aspetto di cui tener conto. A differenza di quanto accade per i concetti intuitivi di "conseguenza” e “causa”, è possibile valutare se è vero che $P → Q$ anche quando $P$ e $Q$ sono affermazioni che non hanno nulla a che fare una con l’altra.
Ad esempio se $P$ è l’affermazione _"il ghiaccio ha una temperatura di 100 gradi centigradi"_ e $Q$ è l’affermazione _"l’Empoli vincerà il campionato di calcio nel 2028"_, allora si può comunque ritenere l’implicazione $P → Q$ vera (poiché non può certamente verificarsi che $P$ valga ma $Q$ no, essendo che $P$ è sempre falsa), anche se evidentemente non c’è nessuna relazione di “conseguenza” o “causalità” tra $P$ e $Q$ nel senso intuitivo di tali termini.

### Non-commutatività dell'implicazione

Il connettivo → non è affatto commutativo: $P → Q$ e $Q → P$ hanno significati completamente diversi!
Infatti, se ad esempio $Q$ è vera e $P$ è falsa, allora l’implicazione $P → Q$ risulterà vera, mentre l’implicazione $Q → P$ risulterà falsa. Dunque queste due implicazioni non sono equivalenti.

### Non-associatività dell'implicazione

Si verifica anche che $→$ non è associativo, ovvero che $P → (Q → R)$ e $(P → Q) → R$ non sono espressioni equivalenti.
Infatti, se ad esempio sia $P$ che $R$ sono false, allora è facile verificare che $P → (Q → R)$ è vera, mentre $(P → Q) → R$ è falsa (indipendentemente dal fatto che $Q$ sia vera o meno).
L’implicazione $P → Q$ è invece equivalente al suo contrappositivo $¬Q → ¬P$, in simboli
$$
P → Q ≡ ¬Q → ¬P
$$
Infine, se $P ≡ R$ e $Q ≡ S$, allora $P → Q ≡ R → S$.

## Definizione: bi-implicazione

↔ è la bi-implicazione e corrisponde all’espressione “. . . se e solo se . . . ”.
La sua tavola di verità è

| $P$ | $Q$ | $P \leftrightarrow Q$ |
| --- | --- | ---------- |
| V   | V   | V          |
| V   | F   | F          |
| F   | V   | F          |
| F   | F   | V          |

Quando asseriamo che _“$P$ se e solo se $Q$”_ intendiamo dire che _“se $P$ allora $Q$, e se $Q$ allora $P$”_. In altre parole,
$$
P ↔ Q ≡ (P → Q) ∧ (Q → P)
$$
In particolare, $P ↔ Q$ è vera se e solo se in ogni contesto si verifica che o $P$ e $Q$ sono entrambe vere, oppure sono entrambe false.

Spesso in matematica _“P se e solo se Q”_ lo si scrive come: _“la condizione necessaria e sufficiente affinché valga $P$ è che valga $Q$”_.

### Proprietà: commutatività della bi-implicazione

Utilizzando le tavole di verità si verifica che la bi-implicazione è commutativa:
$$
P ↔ Q ≡ Q ↔ P
$$

%% infatti
(tabella)
%%

### Proprietà: associatività della bi-implicazione

$$
P ↔ (Q ↔ R) ≡ (P ↔ Q) ↔ R
$$

### Altra proprietà %%chiedere a ChatGPT come si chiama%%

Se $P ≡ R$ e $Q ≡ S$, allora $P ↔ Q ≡ R ↔ S$.

Utilizzando l’equivalenza $P ↔ Q ≡ (P → Q) ∧ (Q → P)$ e le leggi viste per la congiunzione si ha che 
$$
P ↔ Q |= P → Q e P ↔ Q |= Q → P
$$
e
$$
P → Q, Q → P |= P ↔ Q
$$

Osserviamo infine che il bi-condizionale cattura il concetto di equivalenza logica, ovvero che
$$
P ≡ Q \leftrightarrow |= P ↔ Q
$$

## Connettivi logici fondamentali nand e nor

Abbiamo visto che:
- La disgiunzione esclusiva ⊕ e la bi-implicazione ↔ sono definibili l’una a partire dall’altra mediante la negazione ¬;
- Il connettivo ¯∧ è definibile dalla congiunzione ∧ e ¬;
- Il connettivo ¯∨ è definibile dalla disgiunzione ∨ e ¬;
- ↔ è definibile da → e ∧;
- → e ∨ sono definibili l’una a partire dall’altra mediante la negazione ¬;
- ∧ e ∨ sono definibili l’una a partire dall’altra mediante ¬ (leggi di De Morgan).

Quindi ciascuna delle seguenti coppie di connettivi è sufficiente per definire tutti gli altri
$$
\{¬, ∨\}, \{¬, ∧\}, \{¬, →\}
$$
Viceversa le coppie $\{¬, ↔\}$ e $\{¬, ⊕\}$ non sono in grado di definire nessuno tra $→$, $∧$, $∨$.

Osserviamo che
$¬P ≡ P ¯∨ P$ e $¬P ≡ P ∧ P$
Dato che $P ∨ Q ≡ ¬(P ¯∨ Q)$ e $P ∧ Q ≡ ¬(P ¯∧ Q)$, si ha
$P ∨ Q ≡ (P ¯∨ Q) ¯∨ (P ¯∨ Q)$ e $P ∧ Q ≡ (P ¯∧ Q) ¯∧ (P ¯∧ Q)$.
Quindi a partire da uno dei due connettivi $¯∧$ o $¯∨$ si possono definire tutti gli altri connettivi.

# Quantificatori

## Definizione: quantificatore esistenziale

∃ è il quantificatore esistenziale.
L’espressione $\exists x (P(x))$ si legge: _“c’è un $x$ tale che $P$”_, ovvero _“l’affermazione $P$ vale per qualche $x$”_. Essa asserisce che c’è almeno un elemento (non necessariamente unico!) $x$ che gode della proprietà descritta da $P$.

## Definizione: quantificatore universale

∀ è il quantificatore universale.
L’espressione $\forall x (P(x))$ si legge: _“per ogni $x$ tale che $P$”_, ovvero _“l’affermazione $P$ vale per tutti gli $x$”_. Essa asserisce che ogni ente gode della proprietà descritta da $P$.

## Differenza tra $\exists$ e $\forall$

Quando scriviamo un’affermazione del tipo $\exists x (P(x))$ o $\forall x (P(x))$ spesso siamo in una situazione in cui $P$ afferma qualche proprietà che l’elemento $x$ può avere o meno.
Esempio:
Se $P$ è l’equazione $x^2 + x = 0$, l’espressione $\exists x (P(x))$ dice che l’equazione data ammette una soluzione. Invece $\forall x (P(x))$ dice che ogni numero è soluzione di $P$.

Se invece $P$ non dice nulla della variabile $x$, il significato di $\exists x (P(x))$ e di $\forall x (P(x))$ coincide con quello di $P$.
Esempio:
Le espressioni $\exists x \exists y (y^2 + y = 0)$ e $\forall x \exists y (y^2 + y = 0)$ sono entrambe equivalenti a $\exists y (y^2 + y = 0)$: tutte e tre asseriscono che l’equazione $y^2 + y = 0$ ammette una soluzione.

La negazione di espressioni che iniziano con un quantificatore è un altro dei punti che può trarre in inganno se non si presta abbastanza attenzione al significato di ciò che si sta dicendo.
La frase _"non tutti i politici sono onesti"_ (ovvero $\lnot \forall x (P(x))$, dove $P(x)$ significa _“$x$ è onesto”_), non vuol dire che _"tutti i politici sono disonesti"_ (ovvero $\forall x (\lnot P(x))$), bensì è equivalente a _"esiste (almeno) un politico disonesto"_ (ovvero all'espressione $\exists x (\lnot P(x))$).
Similmente, l’affermazione _"non esiste un vaccino pericoloso"_ (che è della forma $\lnot \exists x (P(x))$, dove $P(x)$ sta per _“$x$ è pericoloso”_), non vuole dire che _"qualche vaccino è sicuro"_ (ovvero $\exists x (\lnot P(x))$), bensì è equivalente a _"tutti i vaccini sono sicuri"_ (ovvero all'espressione $\forall x (\lnot P(x))$).

Più in generale, negare $\forall x (P(x))$ significa dire che non tutti gli $x$ godono della proprietà descritta da $P$, cioè c'è almeno un $x$ per cui si può asserire $\lnot P$, quindi:
$$
\lnot \forall x (P(x)) \equiv \exists x (\lnot P(x))
$$
Viceversa, se neghiamo $\exists x (P(x))$ allora vuol dire che non si dà il caso che ci sia un $x$ per cui vale $P$, cioè che per ogni $x$ deve valere $\lnot P$, quindi:
$$
\lnot \exists x (P(x)) \equiv \forall x (\lnot P(x))
$$
Negando entrambi i termini di ciascuna delle equivalenze precedenti e applicando la legge della doppia negazione si ottiene
$$
\forall x (P(x)) \equiv \lnot\exists x (\lnot P(x))
$$
e
$$
\exists x (P(x)) \equiv \lnot \forall x (\lnot P(x))
$$
Questo vuol dire che ciascuno dei due quantificatori $\forall$ e $\exists$ può essere “definito” a partire dall’altro quantificatore e dalla negazione.

## Proprietà commutativa

Quando scriviamo $\forall x \forall y (P(x,y))$ intendiamo dire che in qualsiasi modo si scelgano gli elementi $x$ e $y$ vale la proprietà $P$, e questo è la stessa cosa che dire $\forall y \forall x (P(x,y))$. Analogamente, $\exists x \exists y (P(x,y))$ ha lo stesso significato di $\exists y \exists x (P(x,y))$. Quindi $∃x∃yP ≡ ∃y∃xP$ e $∀x∀yP ≡ ∀y∀xP$.
Bisogna invece stare molto attenti quando si vuole scambiare due quantificatori di diverso tipo...

Supponiamo che valga $\exists x \exists y (P(x,y))$: questo vuol dire che c’è un $x$ tale che per ogni $y$ vale $P$. Quindi è vero che dato un $y$ arbitrario possiamo sempre trovare un $x$ tale che $P$: basta prendere l’elemento $x$ di prima. In altre
parole
$$
\exists x \forall y (P(x,y)) \vDash \forall y \exists x (P(x,y))
$$
Questa regola non può però essere invertita! Da $\forall y \exists x (P(x,y))$ non possiamo affatto concludere $\exists x \forall y (P(x,y))$: si considerino ad esempio le affermazioni $\forall y \exists x (y < x)$ e $\exists x \forall y (y < x)$: nei numeri naturali, la prima è vera ma la seconda è falsa).
Questo vuol dire, in particolare, che le espressioni $\exists x \forall y (P(x,y))$ e $\forall y \exists x (P(x,y))$ non sono equivalenti: dalla prima segue la seconda, ma non viceversa.

Il quantificatore esistenziale si può distribuire e raccogliere rispetto alla disgiunzione nel seguente senso: dire che _“c’è un $x$ per cui $P$ oppure c’è un $x$ per cui $Q$”_ è equivalente a dire _“c’è un $x$ per cui $P$ o $Q$”_, in simboli:
$$
∃x(P(x)) ∨ ∃x(Q(x)) \equiv ∃x (P(x) ∨ Q(x))
$$
Rispetto alla congiunzione, invece, solo una delle due possibili regole è valida: il quantificatore si può distribuire ma non raccogliere. Infatti, se _“c’è un $x$ tale che $P$ e $Q$”_ allora _“c’è un $x$ tale che $P$ e c’è un $x$ tale che $Q$”_, in simboli
$$
∃x(P(x) ∧ Q(x)) \vDash (∃x(P(x))) ∧ (∃x(Q(x)))
$$
Il viceversa però non vale: ad esempio, dal fatto che ci sia un numero naturale pari e ci sia un numero naturale dispari non possiamo concludere che esista un numero naturale che è sia pari che dispari.

Specularmente, il quantificatore universale si distribuisce e raccoglie rispetto alla congiunzione
$$
(∀xP) ∧ (∀xQ) ≡ ∀x (P ∧ Q)
$$
ma rispetto alla disgiunzione si può raccogliere
$$
(∀xP) ∨ (∀xQ) |= ∀x (P ∨ Q)
$$
ma non distribuire. Ad esempio, è vero che ogni numero naturale è o pari o dispari, ma da questo non si può concludere che tutti i numeri naturali sono pari o tutti i numeri naturali sono dispari.
Questo parallelismo tra il quantificatore esistenziale e la disgiunzione, da un lato, e il quantificatore universale e la congiunzione, dall’altro, non è così sorprendente, visto che i quantificatori possono essere visti come disgiunzioni e congiunzioni generalizzate: infatti, dire che vale $∃x(P(x))$ in $N$ equivale ad asserire $P(0) ∨ P(1) ∨ P(2) ∨ \ldots$, mentre dire che vale $∀x(P(x))$ in $N$ equivale ad asserire $P(0) ∧ P(1) ∧ P(2) ∧ \ldots$.

# Leggi logiche

## Modus ponens

Dall’equivalenza $P → Q ≡ ¬P ∨ Q$, %%definizione dell'implicazione come disgiunzione e negazione%%si può anche ricavare una delle più famose tra le leggi logiche, ovvero il modus ponens:
$$
P → Q, P |= Q
$$
Infatti, se siamo in un contesto in cui vale $P → Q$, allora vale anche $¬P ∨ Q$. Se inoltre vale anche $P$, per la legge della doppia negazione vale anche $¬¬P$. Applicando la legge della disgiunzione, concludiamo che deve valere $Q$.
