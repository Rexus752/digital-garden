---
icon: TiCirclesRelation
iconColor: "#FF88FF"
---
# 1 - Introduzione agli insiemi

# 1.1 - Insiemi

> [!definizione] Definizione: insieme
> 
> Un **insieme**, denotato con le lettere latine maiuscole (es. $A$, $B$, $C$, ecc.), è una collezione ben definita di oggetti distinti, detti _elementi dell'insieme_, generalmente denotati con le lettere latine minuscole (es. $a$, $b$, $c$, ecc.).
> 
> Per affermare l'appartenenza di un dato elemento a un insieme si usa il simbolo $\in$ e si legge come _"appartiene a"_ (es. $a \in A$ denota che l'elemento $a$ appartiene all'insieme $A$), mentre per negarla si usa il simbolo $\notin$ e si legge come _"non appartiene a"_ (es. $b \notin B$ denota che l'elemento $b$ non appartiene all'insieme $B$).

> [!osservazione] Osservazione: restrizioni sulla natura degli elementi di un insieme
> 
> Non c'è alcuna restrizione su quale sia la natura degli oggetti che possono appartenere a un insieme: essi possono essere sia oggetti "matematici" (come i numeri), ma non solo (es. l'insieme delle capitali dei Paesi nel mondo). Non è neanche detto che gli oggetti dell'insieme debbano avere una natura "omogenea" (es. può esistere un insieme che ha come elementi il numero 4, il nome del Rettore dell'Università di Torino e la Mole Antonelliana).

> [!osservazione] Osservazione: significato di _"ben definita"_
> 
> La richiesta che la collezione sia ben definita significa che non deve esserci alcuna ambiguità circa il fatto che un oggetto sia o meno un elemento di un dato insieme (es. l'insieme dei professori bravi dell'Università di Torino non può essere un insieme perché non è possibile definire in modo oggettivo quali professori ne facciano parte e quali no).

> [!osservazione] Osservazione: insiemi come elementi di altri insiemi
> 
> Una volta definito correttamente un certo insieme, esso è certamente un oggetto e come tale può essere esso stesso elemento di un altro insieme: gli elementi di un insieme possono essere a loro volta insiemi (es. l'insieme $B$ può essere inteso come un elemento dell'insieme $A$).
> 
> Inoltre, dati un insieme $A$ e un suo elemento l'insieme $B\in A$, gli elementi di $B$ non sono elementi di $A$ (es. se abbiamo $B=\{3,4\}$ e $A=\{0,1,2,\{3,4\}\}$, con $B \in A$ sono 4, in quanto gli elementi $\{3,4\}$ di $B$ sono contati come un unico elemento in $A$).
^Osservazione-insiemi-come-elementi-di-altri-insiemi

> [!osservazione] Osservazione: unicità degli elementi
> 
> Per definizione, essendo un insieme una collezione di oggetti distinti, esso non può avere elementi ripetuti (es. gli insiemi $A=\{0,0,1,2,3\}$ e $B=\{0,1,2,3\}$ sono lo stesso insieme).

> [!osservazione] Osservazione: irrilevanza dell'ordine degli elementi
> 
> In un insieme non conta l'ordine degli elementi (es. gli insiemi $A=\{0,1\}$ e $B=\{1,0\}$ sono lo stesso insieme).

## 1.2 - Insieme vuoto

> [!definizione] Definizione: insieme vuoto
> 
> L'**insieme vuoto**, denotato col simbolo $\emptyset$, è l'insieme privo di elementi.

> [!osservazione] Osservazione: l'insieme $\color{#888888}A=\{\emptyset\}$ non è vuoto
> 
> L'insieme $A = \{\emptyset\}$ non è un insieme vuoto: l'insieme vuoto è privo di elementi, mentre l'insieme $\color{#888888}A$ ha un elemento, ossia l'elemento-insieme vuoto $\emptyset \in A$ ([come già osservato](Insiemistica.md#^Osservazione-insiemi-come-elementi-di-altri-insiemi), un insieme può avere come suoi elementi altri insiemi).

%%
\### Osservazione: unicità dell'insieme vuoto

L'insieme vuoto è unico, ovvero: se $A$ e $B$ sono due insiemi che non contengono nessun elemento, allora, per il principio di estensionalità(LINK), si ha che:
$$
A = B
$$
Infatti, $A$ e $B$ hanno gli stessi elementi (cioè nessuno), ovvero $A$ e $B$ verificano la formula
$$
\forall x (x \in A \leftrightarrow x \in B)
$$
SISTEMARE FORMULA LOGICA
%%

## 1.3 - Singoletti

> [!definizione] Definizione: singoletto
> 
> Un **singoletto** o **insieme unitario** è un insieme formato da un solo elemento.

> [!esempio] Esempio: $\color{#8888FF}\{0\}$ e $\color{#8888FF}\{\{1,2,3\}\}$ sono singoletti
> 
> Gli insiemi $\{0\}$ e $\{\{1,2,3\}\}$ sono singoletti: in particolare, il primo è formato unicamente dall'elemento $0$, mentre il secondo è formato dall'unico elemento $\{1,2,3\}$ che a sua volta è un insieme (non unitario).

## 1.4 - Cardinalità di un insieme

> [!definizione] Definizione: cardinalità di un insieme
> 
> La **cardinalità** di un insieme $A$, denotata $|A|$ oppure $\#A$, è il numero degli elementi di $A$.
> 
> Se $A$ contiene un numero finito $n$ di elementi si denota $|A| = n$ (es. $|\{0,1\}| = 2$), mentre se $A$ contiene infiniti elementi si denota $|A| = \infty$.

> [!esempio] Esempio: $\color{#8888FF}|\{\{0,1\}, 0, 1\}| = 3$
> 
> Dato un insieme $A=\{0,1\}$ e un insieme $B$ che ha come elementi l'insieme $A$ e i numeri $0$ e $1$, quindi $B=\{\{0,1\},0,1\}$, la sua cardinalità $|B| = |\{\{0,1\},0,1\}|$ è pari a $3$, in quanto l'insieme $A$ viene considerato come un unico elemento in $B$, mentre gli altri due numeri $0$ e $1$ vengono considerati ognuno come un elemento a sé stante.
> %%mettere colori%%

> [!esempio] Esempio: $\color{#8888FF}|\{\{0,1\}, 0, 1\}| = 3$
> 
> Dato un insieme $A=\{0,1\}$ e un insieme $B$ che ha come elementi l'insieme $A$ e i numeri $0$ e $1$, quindi $B=\{\{0,1\},0,1\}$, la sua cardinalità $|B| = |\{\{0,1\},0,1\}|$ è pari a $3$, in quanto l'insieme $A$ viene considerato come un unico elemento in $B$, mentre gli altri due numeri $0$ e $1$ vengono considerati ognuno come un elemento a sé stante.
> %%mettere colori%%

> [!esempio] Esempio: $\color{#8888FF}|\mathbb{N}| = \infty$
> 
> La cardinalità dell'insieme dei numeri naturali $\mathbb{N}$%% link %%, quindi $|\mathbb{N}|$, è uguale a $\infty$, in quanto l'insieme $\mathbb{N}$ contiene infiniti elementi che vanno da $0$ a $+\infty$.

## 1.5 - Rappresentazioni di un insieme

### 1.5.1 - Rappresentazione per elencazione di un insieme

La **rappresentazione per elencazione** di un insieme prevede di indicare tutti gli elementi che appartengono ad un insieme semplicemente elencandoli uno ad uno, all'interno di parentesi graffe. Quando si rappresenta un insieme per elencazione, non ha mai importanza l'ordine con cui si scrivono gli elementi e, inoltre, tale metodo è pratico solo quando l'insieme in questione contiene pochi elementi.

Nel caso in cui ci siano invece più elementi che si vogliono omettere nella notazione (come anche nel caso di insiemi infiniti, in cui si vogliono esplicitare soltanto alcuni determinati elementi dell'insieme), si possono usare i puntini di sospensione $\ldots$ all'interno delle graffe.

> [!esempio] Esempio: $\color{#8888FF}A=\{1,2,3,4,5,6,7,8,9\}$ e $\color{#8888FF}B=\{\text{Francia}, \space\text{Germania}, \space\text{Svizzera}\}$
> 
> La notazione $A=\{1,2,3,4,5,6,7,8,9\}$ definisce correttamente l'insieme $A$ come l'insieme dei numerali naturali compresi tra 1 e 9, mentre $B=\{\text{Francia}, \space\text{Germania}, \space\text{Svizzera}\}$ definisce correttamente l'insieme $B$ come un insieme contenente alcune nazioni europee.
> 
> Per l'insieme $A$, si può anche utilizzare per esempio la notazione $A = \{1, 2, \ldots, 9\}$ se si vuole sottintendere che tra gli elementi $2$ e $9$ ci sono gli altri numeri interi non menzionati.

> [!esempio] Esempio: $\color{#8888FF}\mathbb{N} = \{0, 1, 2, 3, \ldots\}, \mathbb{Z} = \{\ldots, -2, -1, 0, 1, 2, \ldots\}, \mathbb{R} = \{\ldots, 3, \ldots, 4, \ldots \}$
> 
> Ognuno dei seguenti insiemi numerici usa i puntini di sospensione in modo diverso:
> - L'insieme dei numeri naturali $\mathbb{N}$ può essere rappresentato con la notazione $\mathbb{N} = \{0, 1, 2, 3, \ldots\}$, in cui i puntini che seguono il $3$ indicano che ci sono infiniti numeri naturali dopo di esso.
> - Allo stesso modo, per l'insieme dei numeri interi $\mathbb{Z}$, nella notazione $\mathbb{Z} = \{\ldots, -2, -1, 0, 1, 2, \ldots\}$ i primi puntini indicano che prima del $-2$ ci sono infiniti numeri interi.
> - Anche per l'insieme dei numeri reali $\mathbb{R}$, nella notazione $\mathbb{R} = \{\ldots, 3, \ldots, 4, \ldots \}$ i puntini tra il $3$ e il $4$ indicano che ci sono infiniti numeri reali tra i due. 

### 1.5.2 - Rappresentazione per caratteristica di un insieme

La **rappresentazione per caratteristica** di un insieme consiste nel dare una proprietà che risulti verificata da tutti gli elementi dell'insieme e solo da essi. Dunque, la forma generale della definizione di un insieme $X$ con questo metodo è del tipo
$$
X=\{x\in U\mid P(x)\}
$$
oppure del tipo
$$
X = \{x \mid x \in U, P(x)\}
$$
(da leggersi _"$X$ è l'insieme degli elementi $x$ in $U$ tali che $x$ soddisfa la proprietà $P$"_) dove l'insieme $U$, detto _insieme universale_, che può essere implicito o esplicito, è definito precedentemente e funziona da ambito del discorso.

> [!esempio] Esempio: $\color{#8888FF}C=\{\text{cittadini italiani}\}$ e $\color{#8888FF}D=\{x\in\mathbb{R}\mid x^2>1\}$
> 
> Le notazioni $C=\{\text{cittadini italiani}\}$ e $D=\{x\in\mathbb{R}\mid x^2>1\}$ definiscono correttamente due insiemi nonostante non siano elencati esplicitamente tutti i loro elementi, specialmente nel caso dell'insieme $D$ che sarebbe matematicamente impossibile, essendo questo insieme infinito.
> In particolare, gli oggetti a cui applicare i due criteri sono presi a priori da un certo insieme di riferimento, esplicito nel caso di $D$ (l'insieme $\mathbb{R}$ dei numeri reali) ed implicito nel caso di $C$ (avrebbe senso applicare il criterio su un insieme di esseri umani).

### 1.5.3 - Rappresentazione grafica di un insieme

La **rappresentazione grafica di un insieme** consiste nel rappresentarlo con una regione di piano limitata da una curva chiusa: gli elementi dell'insieme sono scritti all'interno della linea chiusa, mentre gli elementi che non appartengono all'insieme stanno all'esterno. Il nome dell'insieme, invece, viene posto all'esterno della linea chiusa vicino a essa. Forme grafiche di questo tipo sono generalmente denominate _diagrammi di Eulero-Venn_ ed offrono un supporto intuitivo notevole nel rappresentare gli insiemi.
%% fare esempio %%

### 1.5.4 - Rappresentazione per intervalli di un insieme

La **rappresentazione per intervalli di un insieme** si può usare nel caso in cui l'insieme contiene tutti i numeri (generalmente in $\mathbb{R}$) compresi tra due valori detti _estremi dell'intervallo_, che possono essere compresi o meno nell'intervallo stesso. Per indicare l'intervallo, quindi, si racchiudono i due valori, separati da una virgola, in due parentesi che sono quadre se i valori sono compresi nell'intervallo o, altrimenti, tonde.

%%fare un esempio con solo estremi esclusi e uno con solo estremi inclusi%%

> [!osservazione] Osservazione: intervalli con un solo estremo incluso
> 
> Gli intervalli non devono necessariamente avere entrambi gli intervalli inclusi o esclusi: possono averne anche uno solo incluso e l'altro escluso.

> [!esempio] Esempio: $\color{#8888FF}A=\{x\in\mathbb{R}\mid x >-1 \land x \le 4\} = (-1,4]$
> 
> Dato un insieme $A=\{x\in\mathbb{R}\mid x >-1 \land x \le 4\}$, esso si può anche rappresentare come l'intervallo $(-1,4]$ dal momento che esso racchiude tutti i numeri $x\in\mathbb{R}$ compresi tra $-1$ escluso e $4$ incluso.

# 2 - Sottoinsiemi

> [!definizione] Definizione: sottoinsieme
> 
> Dati due insiemi $A$ e $B$, $B$ si dice _**sottoinsieme**_ di $A$ e si denota con $B \subseteq A$ (_"$B$ è incluso in $A$"_) se ogni elemento di $B$ è anche un elemento di $A$:
> $$
> B \subseteq A = \{b \in B \mid b \in A\}
> $$
> Alternativamente, si può dire che $B$ è incluso in $A$ se ogni elemento di $B$ è anche elemento di $A$:
> $$
> B \subseteq A \leftrightarrow \forall x(x \in B \to x \in A)
> $$
> %% aggiustare formula logica %%
> $A$ viene chiamato _soprainsieme_ di $B$.
> 
> Per indicare che $B$ non è un sottoinsieme di $A$ (e cioè che esiste almeno un elemento in $B$ che non è in $A$) si usa la notazione:
> $$
> B \nsubseteq A \leftrightarrow \exists x(x \in B \to x \notin A)
> $$
> %% aggiustare formula logica %%

> [!esempio] Esempio: sottoinsiemi di $\color{#8888FF}A=\{0,1,2,3,4\}$
> 
> Dato un insieme $A=\{0,1,2,3,4\}$, possibili sottoinsiemi di $A$ sono gli insiemi $B=\{0,1,2\}$ e $C=\{4\}$, in quanto gli elementi che contengono appartengono anche ad $A$:
> $$
> B, C \subseteq A
> $$
> 
> Non è invece sottoinsieme di $A$ l'insieme $D = \{1, 4, 5\}$, perché l'elemento $5$ non è contenuto anche in $A$:
> $$
> D \nsubseteq A
> $$

> [!osservazione] Osservazione: confusione sul termine _"contenere"_
> 
> In italiano, il termine _"contenere"_ è ambiguo perché si utilizza:
> - Sia nel senso di appartenenza (es. _"$\mathbb{N}$ contiene $1$"_, inteso come _"$1$ è un elemento di $\mathbb{N}$"_ che si traduce in termini matematici con "$1 \in \mathbb{N}$").
> - Sia nel senso di inclusione (es. _"$\mathbb{N}$ contiene i numeri pari"_, inteso come _"l'insieme dei numeri pari è incluso in $\mathbb{N}$"_ che si traduce in termini matematici con "$\{ x \in \mathbb{Z} \mid x = 2k, \; k \in \mathbb{Z} \} \in \mathbb{N}$"%% corretta questa definizione dell'insieme dei pari? %%).

%%
\### Attenzione: differenza tra appartenenza ($\color{#FF8800}\color{#FF8800}\color{#FF8800}\in$) e inclusione ($\color{#FF8800}\color{#FF8800}\color{#FF8800}\subseteq$)

\emptyset . . . \subseteq N 
{5} . . . \subseteq N 
5 . . . \in N
{5} . . . \in P(N)
N . . . \subseteq $\mathbb{Z}$
N . . . \in P(Z)
P(N) . . . \subseteq P(Z)
{n \in N | n = 4k per qualche k} . . . \subseteq {n \in N | n = 2k per qualche k}
%%

%%
smistare nelle altre sezioni:

Quale delle seguenti affermazioni sono corrette?
1 \emptyset \in A per ogni insieme A FALSO
2 \emptyset \in P(A) per ogni insieme A VERO
3 a \in {{a}} FALSO
4 {a} \subseteq {{a}} FALSO
5 {a} \in {{a}} VERO
6 {a} \in {a, {a}} VERO
7 {a} \subseteq {a, {a}} VERO
8 {0, 1, 2} \subseteq P(N) FALSO
%%

## 2.1 - Sottoinsiemi banali

> [!definizione] Definizione: sottoinsiemi banali
> 
> Per ogni insieme $X$ si ha sempre che $\emptyset \subseteq X$ e $X \subseteq X$: questi sono detti ***sottoinsiemi banali*** di $X$.
^Definizione-sottoinsiemi-banali

> [!esempio] Esempio: sottoinsiemi banali di $\color{#8888FF}A=\{0,1,2,3,4\}$
> 
> Dato un insieme $A=\{0,1,2,3,4\}$, i suoi sottoinsiemi banali sono l'insieme vuoto $\emptyset$ e l'insieme $B = \{0,1,2,3,4\}$.


## 2.2 - Sottoinsiemi propri

> [!definizione] Definizione: sottoinsieme proprio
> 
> Dati un insieme $A$ e un suo sottoinsieme $B$ con $B \ne A$, $B$ è detto **_sottoinsieme proprio_** di $A$ e, per evidenziarne la disuguaglianza, si può indicare anche nel seguente modo:
> $$
> B\subsetneq A
> $$

%%
Osservazione: significa che esiste almeno un elemento di B non in A
%%

> [!esempio] Esempio: sottoinsiemi propri di $\color{#8888FF}A=\{0,1,2,3,4\}$
> 
> Dato un insieme $A=\{0,1,2,3,4\}$, dei suoi possibili sottoinsiemi propri sono gli insiemi $E=\{1,3,4\}$ ed $F=\{0,1,2,3\}$.

%%
\### Attenzione

Non confondere $\subsetneq$ con $\nsubseteq$: dati due insiemi $A$ e $B$, se $B \subsetneq A$ (cioè $B$ è un sottoinsieme proprio di $A$), allora in particolare $A$ è un sottoinsieme di $B$ (cioè $B \subseteq A$) e quindi non potrà essere vero che $A \nsubseteq B$.

Ad esempio, $\{1, 2\} \subsetneq \{1, 2, 3\}$ ma non è vero che $\{1, 2\} \nsubseteq \{1, 2, 3\}$.
%%

## 2.4 - Insieme delle parti

> [!definizione] Definizione: insieme delle parti
> 
> Dato un insieme $A$, si definisce **_insieme delle parti_** o _insieme potenza_ di $A$ e si denota $\mathcal{P}(A)$ l'insieme i cui elementi sono tutti i possibili sottoinsiemi di $A$:
> $$\mathcal{P}(A)=\{B\mid B \subseteq A\}$$

> [!esempio] Esempio: insieme delle parti di $\color{#8888FF}A=\{a,b,c\}$
> 
> Dato un insieme $A=\{a,b,c\}$, si ha $\mathcal{P}(A)=\{\emptyset, \{a\}, \{b\}, \{c\}, \{a,b\}, \{b,c\}, \{a,c\},A\}$.

> [!osservazione] Osservazione: $\color{#888888}\mathcal{P}(\emptyset)=\{\emptyset\}$
> 
> L'unico sottoinsieme di $\emptyset$ è $\{\emptyset\}$. Pertanto, $\mathcal{P}(\emptyset)=\{\emptyset\}$ e, dunque, $\mathcal{P}(\emptyset)\ne\emptyset$.

> [!osservazione] Osservazione: $\color{#888888}\mathcal{P}(\{a\})=\{\emptyset,\{a\}\}$
> 
> Dato un insieme $A$ con un solo elemento $a \in A$, gli unici sottoinsiemi sono quelli [banali](Insiemistica.md#^Definizione-sottoinsiemi-banali), quindi $\mathcal{P}(A) = \mathcal{P}(\{a\}) = \{\emptyset, \{a\}\}$.

> [!osservazione] Osservazione: $\color{#888888}\mathcal{P}(A)$ è sempre non vuoto
> 
> Per qualsiasi insieme $A$, vuoto o non vuoto, il suo insieme delle parti $\mathcal{P}(A)$ contiene sempre l'insieme vuoto $\emptyset$ e $A$ stesso come elementi, quindi è sempre non vuoto.

> [!osservazione] Osservazione: $\color{#888888}|\mathcal{P}(A)| = 2^{|A|}$
> 
> Dato un insieme finito $A$ con $n$ elementi (quindi $|A| = n$), allora il suo insieme delle parti $\mathcal{P}(A)$ ha esattamente $2^n$ elementi, cioè $|\mathcal{P}(A)| = 2^{|A|}$. Per esempio, dato un insieme $A$ con $3$ elementi, il suo insieme delle parti $\mathcal{P}(A)$ avrà $2^3 = 8$ elementi.

# 3 - Uguaglianza di due insiemi

%%
\## Principio di estensionalità

Due insiemi coincidono se e solo se hanno gli stessi elementi, ovvero:
$$
A = B \leftrightarrow \forall x (x \in A \leftrightarrow x \in B)
$$

\### Osservazione: unicità e irrilevanza dell'ordine degli elementi

Dato un insieme $\{-1, 2, 3\}$, per il principio di estensionalità, si ha che:
$$
\{−1, 2, 3\} = \{2, −1, 3\} = \{-1, 2, 3, 3\}
$$
In altre parole: l'ordine in cui vengono elencati gli elementi di un insieme è irrilevante e le eventuali ripetizioni non contano, proprio perché per tutti e tre insiemi vale il principio di estensionalità:
$$
\{-1, 2, 3\} = \{2, -1, 3\} = \{-1, 2, 3, 3\} \leftrightarrow \forall x (x \in \{-1, 2, 3\} \leftrightarrow x \in \{2, -1, 3\} \leftrightarrow x \in \{-1, 2, 3, 3\})
$$
Al contrario, $\{3, −1, 2\} \ne \{2, −1, 2\}$ poiché $3$ appartiene al primo insieme ma non al secondo.
%%

> [!proposizione] Proposizione: uguaglianza di due insiemi
> 
> Dati due insiemi $A$ e $B$, essi sono uguali solo se $A\subseteq B$ e $B\subseteq A$ contemporaneamente.
> 
> > [!dimostrazione] Dimostrazione
> > 
> > Se $A=B$, allora $A$ e $B$ hanno esattamente gli stessi elementi, cioè ogni elemento di $A$ è anche un elemento di $B$ (e quindi $A \subseteq B$) e ogni elemento di $B$ è anche un elemento di $A$ (e quindi $B \subseteq A$).
> > Viceversa, se $A \subseteq B$ e $B \subseteq A$, allora $A$ e $B$ devono contenere esattamente gli stessi elementi, perché l'esistenza di un $x \in A \mid x \notin B$ contraddice l'ipotesi $A \subseteq B$ e l'esistenza di un $y \in B \mid y \notin A$ contraddice l'ipotesi $B \subseteq A$.
> > 
> > $\blacksquare$
