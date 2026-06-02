---
title: Teoria degli insiemi
---

> [!premessa]+ Premessa
> 
> Ciao! Se è la prima volta che capiti su questo sito, ti consiglio di consultare la [pagina principale](index.md) di questo cosiddetto _Giardino Digitale_ per scoprire meglio cos'è e come navigarlo.
> 
> Lo stato di questa nota è al momento: 🟡 <font color="#FFFF7F">_Incompleta_</font>.

%% 
prerequisito: Logica Matematica per teoremi e dimostrazioni
%%

---

%% mettere link a tutti i termini %%

> [!definizione]+ Definizione: teoria degli insiemi
> 
> La **teoria degli insiemi** è una branca della [matematica](content/Matematica/_index.md#^definizione-matematica) che si occupa dello studio degli [insiemi](Matematica/Teoria%20degli%20insiemi/_index.md#^definizione-insieme), cioè collezioni di oggetti distinti che possono essere definiti e manipolati secondo determinate regole.
^definizione-teoria-degli-insiemi

%% 
- in 1.1 - Insiemi e loro proprietà di Lezioni di Analisi I di Lancelotti c'è roba di Logica
- fare capitolo 2 sugli insiemi numerici
%%

# 1 - Introduzione agli insiemi

Gli **insiemi** sono l'oggetto matematico su cui si fonda la **teoria degli insiemi** e vengono utilizzati per descrivere e analizzare gruppi di oggetti, numeri o concetti.

> [!definizione]+ Definizione: insieme
> 
> Un **insieme**, denotato con le lettere latine maiuscole (es. $A$, $B$, $C$, ecc.), è una collezione ben definita di oggetti distinti, detti **_elementi dell'insieme_**, generalmente denotati con le lettere latine minuscole (es. $a$, $b$, $c$, ecc.).
> 
> Per affermare l'appartenenza di un dato elemento a un insieme si usa il simbolo "$\in$" (si legge come _"appartiene a"_, per esempio "$a \in A$" denota che l'elemento $a$ appartiene all'insieme $A$), mentre per negarla si usa il simbolo "$\notin$" (si legge come _"non appartiene a"_, per esempio "$b \notin B$" denota che l'elemento $b$ non appartiene all'insieme $B$).
^definizione-insieme

%% 
Questa affermazione non è la definizione di insieme. Infatti, per dire cosa è un insieme abbiamo utilizzato il termine collezione che non abbiamo precedentemente definito. Avremmo potuto usare il termine famiglia in luogo di collezione. In ogni caso anche questo termine non lo abbiamo precedentemente definito. Inoltre, anche il termine oggetto non è stato precedentemente definito.
Quindi per dire cosa è un insieme abbiamo utilizzato termini che non abbiamo precedentemente
definito ma di cui è noto il significato. Ne segue che il concetto di insieme, come quello di elemento,
è da considerarsi un concetto primitivo, ossia una nozione sul cui significato siamo tutti concordi e
che per essere spiegata necessita esclusivamente di sinonimi.
%%

> [!osservazione]+ Osservazione: restrizioni sulla natura degli elementi di un insieme
> 
> Non c'è alcuna restrizione su quale sia la natura degli oggetti che possono appartenere a un [insieme](Matematica/Teoria%20degli%20insiemi/_index.md#^definizione-insieme): essi possono essere sia oggetti "matematici" (come i numeri), ma non solo (es. l'insieme delle capitali dei Paesi nel mondo). Non è neanche detto che gli oggetti dell'[insieme](Matematica/Teoria%20degli%20insiemi/_index.md#^definizione-insieme) debbano avere una natura "omogenea" (es. può esistere un insieme che ha come elementi il numero 4, il nome del Rettore dell'Università di Torino e la Mole Antonelliana).
^osservazione-restrizioni-sulla-natura-degli-elementi-di-un-insieme

> [!osservazione]+ Osservazione: significato di _"ben definita"_
> 
> La richiesta che la collezione sia ben definita significa che non deve esserci alcuna ambiguità circa il fatto che un oggetto sia o meno un elemento di un dato [insieme](Matematica/Teoria%20degli%20insiemi/_index.md#^definizione-insieme) (es. l'insieme dei professori più bravi dell'Università di Torino non può essere un insieme perché non è possibile definire in modo oggettivo quali professori ne facciano parte e quali no).
^osservazione-significato-di-ben-definita

> [!osservazione]+ Osservazione: insiemi come elementi di altri insiemi
> 
> Una volta definito correttamente un certo [insieme](Matematica/Teoria%20degli%20insiemi/_index.md#^definizione-insieme), esso è certamente un oggetto matematico e, in quanto tale, può essere esso stesso elemento di un altro insieme: gli elementi di un insieme possono essere a loro volta insiemi (es. l'insieme $B$ può essere inteso come un elemento dell'insieme $A$).
> 
> Inoltre, dati un insieme $A$ e un suo elemento l'insieme $B\in A$, gli elementi di $B$ **NON** sono elementi di $A$ (es. se abbiamo $B=\{3,4\}$ e $A=\{0,1,2,\{3,4\}\}$, con $B \in A$ , gli elementi di $A$ sono 4, in quanto gli elementi $\{3,4\}$ di $B$ sono contati come un unico elemento in $A$).
^osservazione-insiemi-come-elementi-di-altri-insiemi

> [!definizione]+ Definizione: insieme universo
> 
> Un **insieme universo** (o **universo di riferimento**), solitamente denotato con "$\mathcal{U}$", è un [insieme](Matematica/Teoria%20degli%20insiemi/_index.md#^definizione-insieme) che comprende tutti gli insiemi/oggetti/enti pertinenti a un certo contesto o problema.
^definizione-insieme-universo

> [!esempio]- Esempio
> 
> Se si sta lavorando con un mazzo di carte da gioco francesi standard, che contiene 52 carte divise in 4 semi, l'insieme universo $\mathcal{U}$ è l'insieme di tutte e 52 le carte del mazzo.

## 1.1 - Insieme vuoto

> [!definizione]+ Definizione: insieme vuoto
> 
> L'**insieme vuoto**, denotato col simbolo "$\emptyset$", è l'insieme privo di elementi.
^definizione-insieme-vuoto

> [!osservazione]+ Osservazione: l'insieme $\color{#7F7F7F}A=\{\emptyset\}$ non è vuoto
> 
> L'insieme $A = \{\emptyset\}$ non è un insieme vuoto: l'insieme vuoto è privo di elementi, mentre l'insieme $A$ ha un elemento, ossia l'elemento-insieme vuoto $\emptyset \in A$ ([come già osservato](Matematica/Teoria%20degli%20insiemi/_index.md#^osservazione-insiemi-come-elementi-di-altri-insiemi), un insieme può avere come suoi elementi altri insiemi).
^osservazione-l-insieme-A-non-e-vuoto

> [!osservazione]+ Osservazione: unicità dell'insieme vuoto
> 
> L'insieme vuoto è unico, ovvero: se $A$ e $B$ sono due insiemi che non contengono nessun elemento, allora, per il [principio di estensionalità](Matematica/Teoria%20degli%20insiemi/_index.md#^principio-di-estensionalita), si ha che:
> $$
> A = B
> $$
> Infatti $A$ e $B$, avendo gli stessi elementi (cioè nessuno), verificano la formula:
> $$
> \forall x (x \in A \iff x \in B)
> $$
^osservazione-unicita-dell-insieme-vuoto

## 1.2 - Singoletti

> [!definizione]+ Definizione: singoletto
> 
> Un **singoletto** o **insieme unitario** è un insieme formato da un solo elemento.
^definizione-singoletto

> [!esempio]- Esempio: $\color{#7F7FFF}\{0\}$ e $\color{#7F7FFF}\{\{1,2,3\}\}$ sono singoletti
> 
> Gli insiemi $\{0\}$ e $\{\{1,2,3\}\}$ sono [singoletti](Matematica/Teoria%20degli%20insiemi/_index.md#^definizione-singoletto): in particolare, il primo è formato unicamente dall'elemento $0$, mentre il secondo è formato dall'unico elemento $\{1,2,3\}$ che a sua volta è un [insieme](Matematica/Teoria%20degli%20insiemi/_index.md#^definizione-insieme) (quest'ultimo però non [unitario](Matematica/Teoria%20degli%20insiemi/_index.md#^definizione-singoletto)).

## 1.3 - Cardinalità di un insieme

> [!definizione]+ Definizione: cardinalità di un insieme
> 
> La **cardinalità** di un [insieme](Matematica/Teoria%20degli%20insiemi/_index.md#^definizione-insieme) $A$, denotata "$|A|$" oppure "$\#A$", è il numero degli elementi di $A$.
> 
> Se $A$ contiene un numero finito $n$ di elementi si denota "$|A| = n$" (es. $|\{0,1\}| = 2$), mentre se $A$ contiene infiniti elementi (e cioè è un insieme infinito%% link %%) si denota "$|A| = \infty$".
^definizione-cardinalita-di-un-insieme

> [!esempio]- Esempio: $\color{#7F7FFF}|\{\{0,1\}, 0, 1\}| = 3$
> 
> Dato un insieme $A=\{0,1\}$ e un insieme $B$ che ha come elementi l'insieme $A$ e i numeri $0$ e $1$, quindi $B=\{\{0,1\},0,1\}$, la sua cardinalità $|B| = |\{\{0,1\},0,1\}|$ è pari a $3$, in quanto l'insieme $A$ viene considerato come un unico elemento in $B$, mentre gli altri due numeri $0$ e $1$ vengono considerati ognuno come un elemento a sé stante.
> %%mettere colori%%

> [!esempio]- Esempio: $\color{#7F7FFF}|\mathbb{N}| = \infty$
> 
> La cardinalità dell'insieme dei numeri naturali $\mathbb{N}$%% link %%, quindi $|\mathbb{N}|$, è uguale a $\infty$, in quanto l'insieme $\mathbb{N}$ contiene infiniti elementi che vanno da $0$ a $+\infty$.

## 1.4 - Rappresentazioni di un insieme

I modi per rappresentare un [insieme](Matematica/Teoria%20degli%20insiemi/_index.md#^definizione-insieme) sono molteplici e ognuno di essi è più adatto in determinati casi piuttosto che in altri.

### 1.4.1 - Rappresentazione per elencazione di un insieme

> [!notazione]+ Rappresentazione per elencazione di un insieme
> 
> La **rappresentazione per elencazione (o estensiva)** di un [insieme](Matematica/Teoria%20degli%20insiemi/_index.md#^definizione-insieme) prevede di indicare tutti gli elementi che appartengono ad un insieme semplicemente elencandoli uno ad uno, all'interno di parentesi graffe. Quando si rappresenta un insieme per elencazione, non ha mai importanza l'ordine con cui si scrivono gli elementi e, inoltre, tale metodo è pratico solo quando l'insieme in questione contiene pochi elementi.
> 
> Nel caso in cui ci siano invece più elementi che si vogliono omettere nella notazione (come anche nel caso di insiemi infiniti%% link %%, in cui si vogliono esplicitare soltanto alcuni determinati elementi dell'insieme), si possono usare i puntini di sospensione "$\ldots$" all'interno delle graffe.
^rappresentazione-per-elencazione-di-un-insieme

> [!esempio]- Esempio: $\color{#7F7FFF}A=\{1,2,3,4,5,6,7,8,9\}$ e $\color{#7F7FFF}B=\{\text{Francia}, \space\text{Germania}, \space\text{Svizzera}\}$
> 
> La notazione $A=\{1,2,3,4,5,6,7,8,9\}$ definisce correttamente l'[insieme](Matematica/Teoria%20degli%20insiemi/_index.md#^definizione-insieme) $A$ come l'insieme dei numerali naturali compresi tra 1 e 9, mentre $B=\{\text{Francia}, \space\text{Germania}, \space\text{Svizzera}\}$ definisce correttamente l'insieme $B$ come un insieme contenente alcune nazioni europee.

> [!esempio]- Esempio: $\color{#7F7FFF}\mathbb{N} = \{0, 1, 2, 3, \ldots\}, \mathbb{Z} = \{\ldots, -2, -1, 0, 1, 2, \ldots\}, \mathbb{R} = \{\ldots, 3, \ldots, 4, \ldots \}$
> 
> Ognuno dei seguenti [insiemi](Matematica/Teoria%20degli%20insiemi/_index.md#^definizione-insieme) numerici usa i puntini di sospensione in modo diverso:
> - L'insieme dei numeri naturali $\mathbb{N}$ può essere rappresentato con la notazione $\mathbb{N} = \{0, 1, 2, 3, \ldots\}$, in cui i puntini che seguono il $3$ indicano che ci sono infiniti numeri naturali dopo di esso.
> - Allo stesso modo, per l'insieme dei numeri interi $\mathbb{Z}$, nella notazione $\mathbb{Z} = \{\ldots, -2, -1, 0, 1, 2, \ldots\}$ i primi puntini indicano che prima del $-2$ ci sono infiniti numeri interi.
> - Anche per l'insieme dei numeri reali $\mathbb{R}$, nella notazione $\mathbb{R} = \{\ldots, 3, \ldots, 4, \ldots \}$ i puntini tra il $3$ e il $4$ indicano che ci sono infiniti numeri reali tra i due. 

### 1.4.2 - Rappresentazione per caratteristica di un insieme

> [!notazione]+ Rappresentazione per caratteristica di un insieme
> 
> La **rappresentazione per caratteristica (o intensiva)** di un [insieme](Matematica/Teoria%20degli%20insiemi/_index.md#^definizione-insieme) consiste nel dare una proprietà che risulti verificata da tutti gli elementi dell'insieme e solo da essi. Dunque, la forma generale della definizione di un insieme $X$ con questo metodo è del tipo
> $$
> X = \{ x \in \mathcal{U} \mid P(x) \}
> $$
> oppure del tipo
> $$
> X = \{x \mid x \in \mathcal{U}, P(x)\}
> $$
> (da leggersi _"$X$ è l'insieme degli elementi $x$ in $\mathcal{U}$ tali che $x$ soddisfa la proprietà $P$"_) dove l'[insieme universo](Matematica/Teoria%20degli%20insiemi/_index.md#^definizione-insieme-universo) $\mathcal{U}$, che può essere implicito o esplicito, è stato già definito precedentemente e funziona da ambito del discorso.
^rappresentazione-per-caratteristica-di-un-insieme

> [!esempio]- Esempio: $\color{#7F7FFF}C=\{\text{cittadini italiani}\}$ e $\color{#7F7FFF}D=\{x\in\mathbb{R}\mid x^2>1\}$
> 
> Le notazioni $C=\{\text{cittadini italiani}\}$ e $D=\{x\in\mathbb{R}\mid x^2>1\}$ definiscono correttamente due [insiemi](Matematica/Teoria%20degli%20insiemi/_index.md#^definizione-insieme) nonostante non siano elencati esplicitamente tutti i loro elementi, specialmente nel caso dell'insieme $D$ che sarebbe matematicamente impossibile, essendo questo insieme infinito%% link %%.
> 
> In particolare, gli oggetti a cui applicare i due criteri sono presi a priori da un certo insieme di riferimento, esplicito nel caso di $D$ (l'insieme dei numeri reali $\mathbb{R}$%% link %%) ed implicito nel caso di $C$ (avrebbe senso applicare il criterio su un insieme di esseri umani).

### 1.4.3 - Rappresentazione grafica di un insieme

> [!notazione]+ Rappresentazione grafica di un insieme
> 
> La **rappresentazione grafica di un insieme** consiste nel rappresentare un [insieme](Matematica/Teoria%20degli%20insiemi/_index.md#^definizione-insieme) con una regione di piano limitata da una curva chiusa: gli elementi dell'insieme sono scritti all'interno della linea chiusa, mentre gli elementi che non appartengono all'insieme stanno all'esterno. Il nome dell'insieme, invece, viene posto all'esterno della linea chiusa vicino a essa. Forme grafiche di questo tipo sono generalmente denominate **_diagrammi di Eulero-Venn_** ed offrono un supporto intuitivo notevole nel rappresentare gli insiemi.
%% fare esempio %%
^rappresentazione-grafica-di-un-insieme

%% 
Esempio con un diagramma di Eulero-Venn
%%

### 1.4.4 - Rappresentazione per intervalli di un insieme

> [!notazione]+ Rappresentazione per intervalli di un insieme
> 
> La **rappresentazione per intervalli di un insieme** si può usare nel caso in cui l'[insieme](Matematica/Teoria%20degli%20insiemi/_index.md#^definizione-insieme) contiene tutti i numeri (generalmente in $\mathbb{R}$) compresi tra due valori detti **_estremi dell'intervallo_**, che possono essere compresi o meno nell'intervallo stesso. Per indicare l'intervallo, quindi, si racchiudono i due valori, separati da una virgola, in due parentesi che sono quadre se i valori sono compresi nell'intervallo o, altrimenti, tonde.
^rappresentazione-per-intervalli-di-un-insieme

%%fare un esempio con solo estremi esclusi e uno con solo estremi inclusi%%

> [!osservazione]+ Osservazione: intervalli con un solo estremo incluso
> 
> Gli intervalli non devono necessariamente avere entrambi gli intervalli inclusi o esclusi: possono averne anche uno solo incluso e l'altro escluso.

> [!esempio]- Esempio: $\color{#7F7FFF}A=\{x\in\mathbb{R}\mid x >-1 \land x \le 4\} = (-1,4]$
> 
> Dato un insieme $A=\{x\in\mathbb{R}\mid x >-1 \land x \le 4\}$, esso si può anche rappresentare come l'intervallo $(-1,4]$ dal momento che esso racchiude tutti i numeri $x\in\mathbb{R}$ compresi tra $-1$ escluso e $4$ incluso.

%% 
1.8) Osservazione Consideriamo l'insieme A = {1, 3, 4, 27}.
Le seguenti scritture hanno senso e sono corrette, nel senso di VERE:
1 \in A, {1, 3} \subseteq A, 4 not\in {1, 3}, {1, 4} \subseteq {1, 4, 27}, 2 not\in A.
Le seguenti scritture hanno senso e sono errate, nel senso di FALSE:
1 not\in A, {1, 3} not\subseteq A, 4 \in {1, 3}, {1, 4} not\subseteq {1, 4, 27}, 2 \in A.
Le seguenti scritture non hanno senso e ovviamente sono errate. In tal caso però non ha
senso dire se sono VERE o FALSE.
1 \subseteq A, {1, 3} \in A, 4 \subseteq {1, 3}, {1, 4} not\in {1, 4, 27}, 2 not\subseteq A.
Infatti, non ha senso dire che 1 è un sottoinsieme di A, essendo 1 un elemento di A e non un insieme.
Così come non ha senso dire che l'insieme {1, 3} appartiene ad A, essendo un suo sottoinsieme e
non un elemento. Analoghe motivazioni negli altri casi.
Se per esempio si vuol indicare che l'insieme contenente 1 è un sottoinsieme di A, si deve
scrivere
{1} \subseteq A.
%%
## 1.5 - Tuple

> [!definizione]+ Definizione: tupla
> 
> Una **tupla** (o **lista ordinata**) è una collezione di oggetti disposti in un ordine specifico. [A differenza di un insieme](Matematica/Teoria%20degli%20insiemi/_index.md#^osservazione-irrilevanza-dell-ordine-e-unicita-degli-elementi), l'ordine degli elementi in una tupla è significativo, e gli stessi elementi possono comparire più volte.
> 
> Una **$n$-upla** è una tupla di esattamente $n$ elementi, dove $n$ è un numero intero non-negativo e si denota similmente alla [rappresentazione per elencazione di un insieme](Matematica/Teoria%20degli%20insiemi/_index.md#^rappresentazione-per-elencazione-di-un-insieme) nei seguenti modi:
> $$
> (a_1, a_2, \ldots, a_n)
> $$
> oppure:
> $$
> \langle a_1, a_2, \ldots, a_n \rangle
> $$
> 
> Se la tupla è composta da solamente $2$ elementi $a$ e $b$, si parla di _**coppia ordinata**_ e solitamente si denota solo con le parentesi tonde:
> $$
> (a, b)
> $$
^definizione-tupla

# 2 - Sottoinsiemi

> [!definizione]+ Definizione: sottoinsieme
> 
> Dati due [insiemi](Matematica/Teoria%20degli%20insiemi/_index.md#^definizione-insieme) $A$ e $B$, $B$ si dice _**sottoinsieme**_ di $A$ e si denota con "$B \subseteq A$" (_"$B$ è incluso in $A$"_) se ogni elemento di $B$ è anche un elemento di $A$:
> $$
> B \subseteq A = \{b \in B \mid b \in A\}
> $$
> Alternativamente, usando i connettivi logici%% link %%, la definizione di sottoinsieme si può esprimere nel seguente modo:
> $$
> B \subseteq A \iff \forall x(x \in B \implies x \in A)
> $$
> 
> Per indicare che $B$ non è un sottoinsieme di $A$ (e cioè che esiste almeno un elemento in $B$ che non è in $A$) si usa la notazione "$B \nsubseteq A$":
> $$
> B \nsubseteq A \iff \exists x(x \in B \implies x \notin A)
> $$
^definizione-sottoinsieme

> [!esempio]- Esempio: sottoinsiemi di $\color{#7F7FFF}A=\{0,1,2,3,4\}$
> 
> Dato un insieme $A=\{0,1,2,3,4\}$, possibili sottoinsiemi di $A$ sono gli [insiemi](Matematica/Teoria%20degli%20insiemi/_index.md#^definizione-insieme) $B=\{0,1,2\}$ e $C=\{4\}$, in quanto gli elementi che contengono appartengono anche ad $A$:
> $$
> B, C \subseteq A
> $$
> 
> Non è invece sottoinsieme di $A$ l'insieme $D = \{1, 4, 5\}$, perché l'elemento $5$ non è contenuto anche in $A$:
> $$
> D \nsubseteq A
> $$

> [!osservazione]+ Osservazione: confusione sul termine _"contenere"_
> 
> In italiano, il termine _"contenere"_ è ambiguo perché si utilizza:
> - Sia nel senso di appartenenza (es. _"$\mathbb{N}$ contiene $1$"_, inteso come _"$1$ è un elemento di $\mathbb{N}$"_ che si traduce in termini matematici con "$1 \in \mathbb{N}$").
> - Sia nel senso di inclusione (es. _"$\mathbb{N}$ contiene i numeri pari"_, inteso come _"l'insieme dei numeri pari è incluso in $\mathbb{N}$"_ che si traduce in termini matematici con "$\{ x \in \mathbb{Z} \mid x = 2k, \; k \in \mathbb{Z} \} \in \mathbb{N}$"%% corretta questa definizione dell'insieme dei pari? %%).
> 
> Per questo motivo, l'uso del termine _"contenere"_ è sconsigliato in ambito insiemistico.

%%
Esercizio: differenza tra appartenenza ($\in$) e inclusione ($\subseteq$)

\emptyset \ldots \subseteq N 
{5} \ldots \subseteq N 
5 \ldots \in N
{5} \ldots \in P(N)
N \ldots \subseteq $\mathbb{Z}$
N \ldots \in P(Z)
P(N) \ldots \subseteq P(Z)
{n \in N | n = 4k per qualche k} \ldots \subseteq {n \in N | n = 2k per qualche k}
%%

%%
esercizi da separare e smistare ognuno nelle altre sezioni:

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

## 2.1 - Sottoinsiemi propri

> [!definizione]+ Definizione: sottoinsieme proprio
> 
> Dati un insieme $A$ e un suo sottoinsieme $B$ con $B \ne A$ (cioè che almeno un elemento in $A$ non appartiene a $B$), $B$ è detto **_sottoinsieme proprio_** di $A$ e, per evidenziarne la disuguaglianza, si può indicare nel seguente modo:
> $$
> B\subsetneq A
> $$
^definizione-sottoinsieme-proprio

> [!esempio]- Esempio: sottoinsiemi propri di $\color{#7F7FFF}A=\{0,1,2,3,4\}$
> 
> Dato un insieme $A=\{0,1,2,3,4\}$, dei suoi possibili sottoinsiemi propri sono gli [insiemi](Matematica/Teoria%20degli%20insiemi/_index.md#^definizione-insieme) $B=\{1,3,4\} \subsetneq A$ e $C=\{0,1,2,3\} \subsetneq A$.

> [!notazione]+ Notazione: evitare il simbolo "$\subset$"
> 
> Personalmente, un consiglio che mi sento di dare è quello di evitare **sempre** l'uso del simbolo "$\subset$", in quanto viene spesso usato intercambiabilmente in letteratura sia per evidenziare il [sottoinsieme proprio](Matematica/Teoria%20degli%20insiemi/_index.md#^definizione-sottoinsieme-proprio) che per indicare la relazione "generale" di [sottoinsieme](Matematica/Teoria%20degli%20insiemi/_index.md#^definizione-sottoinsieme).
> 
> Nel dubbio, per evitare qualsiasi confusione, va evitato e, al suo posto, vanno usati rispettivamente "$\subsetneq$" nel caso di un [sottoinsieme proprio](Matematica/Teoria%20degli%20insiemi/_index.md#^definizione-sottoinsieme-proprio) e "$\subseteq$" nel caso di un [sottoinsieme](Matematica/Teoria%20degli%20insiemi/_index.md#^definizione-sottoinsieme) qualsiasi.

> [!attenzione]+ Attenzione: non confondere "$\subsetneq$" con "$\not\subseteq$"
> 
> Fai molta attenzione a non confondere "$\subsetneq$" con "$\nsubseteq$": dati due [insiemi](Matematica/Teoria%20degli%20insiemi/_index.md#^definizione-insieme) $A$ e $B$, se $B \subsetneq A$ (cioè $B$ è un [sottoinsieme proprio](Matematica/Teoria%20degli%20insiemi/_index.md#^definizione-sottoinsieme-proprio) di $A$), allora in particolare $A$ è un [sottoinsieme](Matematica/Teoria%20degli%20insiemi/_index.md#^definizione-sottoinsieme) di $B$ (cioè $B \subseteq A$) e quindi non potrà essere vero che $A \nsubseteq B$ perché, quest'ultima relazione, indica che $A$ **non** è sottoinsieme di $B$.
> 
> Ad esempio, vale la relazione $\{1, 2\} \subsetneq \{1, 2, 3\}$, ma non è vero che $\{1, 2\} \nsubseteq \{1, 2, 3\}$.

## 2.2 - Sottoinsiemi banali

> [!definizione]+ Definizione: sottoinsiemi banali
> 
> Per ogni insieme $X$ si ha sempre che $\emptyset \subseteq X$ e $X \subseteq X$: questi sono detti ***sottoinsiemi banali*** di $X$.
^definizione-sottoinsiemi-banali

> [!esempio]- Esempio: sottoinsiemi banali di $\color{#7F7FFF}A=\{0,1,2,3,4\}$
> 
> Dato un insieme $A=\{0,1,2,3,4\}$, i suoi sottoinsiemi banali sono l'insieme vuoto $\emptyset$ e l'insieme $B = \{0,1,2,3,4\}$.

## 2.3 - Insieme delle parti

> [!definizione]+ Definizione: insieme delle parti
> 
> Dato un insieme $A$, si definisce **_insieme delle parti_** o **_insieme potenza_** di $A$ e si denota "$\mathcal{P}(A)$" l'insieme i cui elementi sono tutti i possibili sottoinsiemi di $A$:
> $$\mathcal{P}(A)=\{B\mid B \subseteq A\}$$
^definizione-insieme-delle-parti

> [!esempio]- Esempio di insieme delle parti
> 
> Dato un [insieme](Matematica/Teoria%20degli%20insiemi/_index.md#^definizione-insieme) $A=\{a,b,c\}$, si ha $\mathcal{P}(A)=\{\emptyset, \{a\}, \{b\}, \{c\}, \{a,b\}, \{b,c\}, \{a,c\},A\}$.

> [!osservazione]+ Osservazione: insieme delle parti di un insieme vuoto
> 
> L'unico [sottoinsieme](Matematica/Teoria%20degli%20insiemi/_index.md#^definizione-sottoinsieme) di un [insieme vuoto](Matematica/Teoria%20degli%20insiemi/_index.md#^definizione-insieme-vuoto) $\emptyset$ è $\{\emptyset\}$. Pertanto, il suo [insieme delle parti](Matematica/Teoria%20degli%20insiemi/_index.md#^definizione-insieme-delle-parti) è $\mathcal{P}(\emptyset)=\{\emptyset\}$ e, dunque, $\mathcal{P}(\emptyset)\ne\emptyset$.
^osservazione-insieme-delle-parti-di-un-insieme-vuoto

> [!osservazione]+ Osservazione: insieme delle parti di un singoletto
> 
> Dato un [singoletto](Matematica/Teoria%20degli%20insiemi/_index.md#^definizione-singoletto) $A = \{ a \}$, gli suoi [sottoinsiemi](Matematica/Teoria%20degli%20insiemi/_index.md#^definizione-sottoinsieme) sono quelli [banali](Matematica/Teoria%20degli%20insiemi/_index.md#^definizione-sottoinsiemi-banali), quindi il suo [insieme delle parti](Matematica/Teoria%20degli%20insiemi/_index.md#^definizione-insieme-delle-parti) è $\mathcal{P}(A) = \mathcal{P}(\{a\}) = \{\emptyset, \{a\}\}$.
^osservazione-insieme-delle-parti-di-un-singoletto

> [!osservazione]+ Osservazione: insieme delle parti è sempre non vuoto
> 
> Per qualsiasi [insieme](Matematica/Teoria%20degli%20insiemi/_index.md#^definizione-insieme) $A$, vuoto o non vuoto, il suo [insieme delle parti](Matematica/Teoria%20degli%20insiemi/_index.md#^definizione-insieme-delle-parti) $\mathcal{P}(A)$ contiene sempre l'[insieme vuoto](Matematica/Teoria%20degli%20insiemi/_index.md#^definizione-insieme-vuoto) $\emptyset$ e $A$ stesso come elementi (cioè i suoi [sottoinsiemi banali](Matematica/Teoria%20degli%20insiemi/_index.md#^definizione-sottoinsiemi-banali)), quindi è sempre non vuoto.
^osservazione-insieme-delle-parti-e-sempre-non-vuoto

> [!osservazione]+ Osservazione: cardinalità di un insieme delle parti
> 
> Dato un [insieme](Matematica/Teoria%20degli%20insiemi/_index.md#^definizione-insieme) [finito](Matematica/Teoria%20degli%20insiemi/_index.md#^definizione-cardinalita-di-un-insieme) $A$ con $n$ elementi (quindi $|A| = n$), allora il suo [insieme delle parti ](Matematica/Teoria%20degli%20insiemi/_index.md#^definizione-insieme-delle-parti) $\mathcal{P}(A)$ ha esattamente $2^n$ elementi, cioè $|\mathcal{P}(A)| = 2^{|A|}$. Per esempio, dato un insieme $A$ con $3$ elementi, il suo insieme delle parti $\mathcal{P}(A)$ avrà $2^3 = 8$ elementi.
^osservazione-cardinalita-di-un-insieme-delle-parti

%% 
Esercizio:

Descrivere P(A) dove A = {0, 1, 2}
P(A) = {\emptyset, {0} , {1} , {2} , {0, 1} , {0, 2} , {1, 2} , {0, 1, 2} }
%%

%% 
Esercizio:
Descrivere P(P(A)) con A = {1}
Si ha P(A) = {\emptyset, A}, e quindi P(P(A)) = {\emptyset, {\emptyset} , {A} , {\emptyset, A}}.
%%

%% 
(1.17) Osservazione Sia A not= \emptyset. Allora valgono i seguenti fatti:
a) A \in P(A);
b) {A} \subseteq P(A);
c) A not\subseteq P(A);
a) \emptyset \in P(\emptyset);
b) {\emptyset} \subseteq P(\emptyset);
c) \emptyset \subseteq P(\emptyset)

Le proprietà c) e c) non sono in contraddizione con quanto affermato nell'Osservazione (1.8). Infatti,
pur essendo A un elemento dell'insieme P(A), è pure lui un insieme e quindi ha senso dire se `e
contenuto o meno in P(A). Analogamente per \emptyset. Inoltre, in quest'ultimo caso la proprietà c)
risulta vera, essendo \emptyset sottoinsieme di ogni insieme. Si osservi infine che {A} not= A, A \in {A} e se
A not= \emptyset, allora A not\subseteq {A}, mentre \emptyset \subseteq {\emptyset}.
%%

# 3 - Uguaglianza di due insiemi

L'uguaglianza di due [insiemi](Matematica/Teoria%20degli%20insiemi/_index.md#^definizione-insieme) viene verificata solo se viene rispettato il _principio di estensionalità_.

> [!principio]+ Principio di estensionalità
> 
> Due [insiemi](Matematica/Teoria%20degli%20insiemi/_index.md#^definizione-insieme) sono **uguali** se e solo se hanno gli stessi elementi, ovvero:
> $$
> A = B \iff \forall x (x \in A \iff x \in B)
> $$
^principio-di-estensionalita

> [!osservazione]+ Osservazione: irrilevanza dell'ordine e unicità degli elementi
> 
> Dato un insieme $\{-1, 2, 3\}$, per il [principio di estensionalità](Matematica/Teoria%20degli%20insiemi/_index.md#^principio-di-estensionalita), si ha che:
> 
> $$
> \{-1, 2, 3\} = \{2, -1, 3\} = \{-1, 2, 3, 3\}
> $$
> 
> In altre parole: l'ordine in cui vengono elencati gli elementi di un insieme è irrilevante e le eventuali ripetizioni non contano, proprio perché per tutti e tre [insiemi](Matematica/Teoria%20degli%20insiemi/_index.md#^definizione-insieme) vale il principio di estensionalità e, quindi, sono in realtà tutti lo stesso insieme:
> 
> $$
> \begin{array}{}
> \{-1, 2, 3\} = \{2, -1, 3\} = \{-1, 2, 3, 3\} \\
> \iff \\
> \forall x (x \in \{-1, 2, 3\} \iff x \in \{2, -1, 3\} \iff x \in \{-1, 2, 3, 3\})
> \end{array}
> $$
> 
> Al contrario, $\{3, -1, 2\} \ne \{2, -1, 2\}$ poiché $3$ appartiene al primo insieme ma non al secondo.
^osservazione-irrilevanza-dell-ordine-e-unicita-degli-elementi

Dal [principio di estensionalità](Matematica/Teoria%20degli%20insiemi/_index.md#^principio-di-estensionalita) si ottiene il [teorema della doppia inclusione](Matematica/Teoria%20degli%20insiemi/_index.md#^teorema-della-doppia-inclusione), usato spesso (in maniera implicita) per dimostrare%% link %% l'uguaglianza di due insiemi.

> [!teorema]+ Teorema della doppia inclusione
> 
> Dati due [insiemi](Matematica/Teoria%20degli%20insiemi/_index.md#^definizione-insieme) $A$ e $B$, essi sono uguali se e solo se ciascuno è un sottoinsieme dell'altro contemporaneamente:
> $$
> A = B \iff A \subseteq B \land B \subseteq A
> $$
> 
> > [!dimostrazione]- Dimostrazione
> > 
> > Avendo una bi-implicazione%% link %%, si devono dimostrare entrambe le direzioni:
> > - Direzione dell'implicazione ($\implies$): se $A=B$, allora $A$ e $B$ hanno esattamente gli stessi elementi, cioè ogni elemento di $A$ è anche un elemento di $B$ (e quindi $A \subseteq B$) e ogni elemento di $B$ è anche un elemento di $A$ (e quindi $B \subseteq A$).
> > - Direzione della conseguenza ($\impliedby$): se $A \subseteq B$ e $B \subseteq A$, allora $A$ e $B$ devono contenere esattamente gli stessi elementi, perché l'esistenza di un $x \in A \mid x \notin B$ contraddice l'ipotesi $A \subseteq B$ e l'esistenza di un $y \in B \mid y \notin A$ contraddice l'ipotesi $B \subseteq A$.
> > 
> > $\blacksquare$
^teorema-della-doppia-inclusione

# 4 - Operazioni sugli insiemi

%% 
1.12) Proposizione Siano A, B, C sottoinsiemi di un insieme X . Allora valgono i seguenti
fatti:
a) A \cap B \subseteq A, A \cap B \subseteq B;
b) A \cap B = B \cap A;
c) (A \cap B) \cap C = A \cap (B \cap C);
d) (A \cap B) \cup C = (A \cup C) \cap (B \cup C);
a') A \subseteq A \cup B, B \subseteq A \cup B ;
b') A \cup B = B \cup A;
c') (A \cup B ) \cup C = A \cup (B \cup C);
d') (A \cup B ) \cap C = (A \cap C) \cup (B \cap C).
Inoltre si ha che
A \cup B = \emptyset ⇐⇒ A = B = \emptyset
%%

## 4.1 - Intersezione di insiemi

> [!definizione]+ Definizione: intersezione di due insiemi
> 
> Dati due [insiemi](Matematica/Teoria%20degli%20insiemi/_index.md#^definizione-insieme) $A$ e $B$, si dice _**intersezione**_ di $A$ e $B$ e si denota "$A\cap B$" l'insieme che comprende gli elementi che appartengono contemporaneamente sia ad $A$ che a $B$:
> $$
> A \cap B = \{ x \mid x \in A \land x \in B \}
> $$
> Due [insiemi](Matematica/Teoria%20degli%20insiemi/_index.md#^definizione-insieme) $A$ e $B$ si dicono **_disgiunti_** se non hanno elementi in comune:
> $$
> A \cap B = \emptyset
> $$
^definizione-intersezione-di-due-insiemi

%% 
mettere a parte la definizione di disgiunzione:
(1.13) Definizione Siano A e B due sottoinsiemi di un insieme X. Diciamo che A e B
sono disgiunti se A \cap B = \emptyset.
(1.14) Definizione Consideriamo n sottoinsiemi A1, \ldots , An di un insieme X , con n intero
maggiore di uno. Diciamo che A1, \ldots , An sono a due a due disgiunti se per ogni i, j =
1, \ldots , n con i not= j si ha che Ai \cap Aj = \emptyset.
%%

%% rappresentazione con Eulero-Venn %%

> [!esempio]- Esempio: intersezione di due insiemi
> 
> Dati due insiemi:
> $$
> \begin{align*}
>  & A = \{ n \in \mathbb{N} \mid n \text{ è pari} \} = \{ 0, 2, 4, 6, \ldots \} \\
>  & B = \{ n \in \mathbb{N} \mid 10 \le n^2 \le 200 \} = \{ 4,6,8,10,12,14 \}
> \end{align*}
> $$
> la loro intersezione è:
> $$ A \cap B = \{ 4,6,8,10,12,14 \} $$

> [!esempio]- Esempio: intersezione di tre insiemi
> 
> Dati tre insiemi:
> $$
> \begin{align*}
>  & A = \{ a,b,c,d,e \} \\
>  & B = \{ d,e,f,g \} \\
>  & C = \{ g,h,i \}
> \end{align*}
> $$
> le combinazioni delle loro intersezioni sono:
> $$
> \begin{align*}
> A \cap B & = \{d,e\} \\
> B \cap C & = \{g\} \\
> A \cap C & = \emptyset \\
> A \cap B \cap C & = \emptyset
> \end{align*}
> $$

> [!esempio]- Esempio: intersezione di insiemi delle parti
> 
> Dato un insieme $X=\{a,b,c,d\}$ e dati due insiemi
> $$
> \begin{align*}
>  & A = \{S \in \mathcal{P}(X) \mid |S| = 2\} = \{\{a,b\}, \{a,c\}, \{a,d\}, \{b,c\}, \{b,d\}, \{c,d\}\} \\
>  & B = \{S \in \mathcal{P}(X) \mid c \in S\} = \{\{c\}, \{a,c\}, \{b,c\}, \{c,d\}, \{a,b,c\}, \{b,c,d\}, \{a,c,d\}, \{a,b,c,d\}\}
> \end{align*}
> $$
> allora
> $$
> A \cap B = \{\{a,c\},\{b,c\},\{c,d\}\}
> $$

## 4.2 - Unione di insiemi

> [!definizione]+ Definizione: unione di due insiemi
> 
> Dati due [insiemi](Matematica/Teoria%20degli%20insiemi/_index.md#^definizione-insieme) $A$ e $B$, si dice _**unione**_ di $A$ e $B$ e si denota "$A\cup B$" l'insieme contenente tutti gli elementi di entrambi gli insiemi:
> $$
> A \cup B = \{x \mid x \in A \lor x \in B\}
> $$
> Gli elementi che si trovano sia in $A$ che in $B$ vengono presi in considerazione una volta sola perché, per l'unicità degli elementi%% link %%, non ci possono essere elementi ripetuti in un insieme.
^definizione-unione-di-due-insiemi

%% rappresentazione con Eulero-Venn %%

> [!esempio]- Esempio: unione di due insiemi
> 
> Dati due insiemi:
> 
> $$
> \begin{align*}
>  & A = \{ 0,1 \} \\
>  & B = \{ 2, 3, 4 \}
> \end{align*}
> $$
> la loro unione è
> $$
> A \cup B = \{0,1,2,3,4\}
> $$

> [!esempio]- Esempio: unione di tre insiemi
> 
> Dati tre insiemi:
> $$
> \begin{align*}
>  & A = \{ a,b,c,d,e \} \\
>  & B = \{ d,e,f,g \} \\
>  & C = \{ g,h,i \}
> \end{align*}
> $$
> le combinazioni delle loro unioni sono:
> $$
> \begin{align*}
> A \cup B & = \{ a,b,c,d,e,f,g \} \\
> B \cup C & = \{ d,e,f,g,h,i \} \\
> A \cup C & = \{ a,b,c,d,e,g,h,i \} \\
> A \cup B \cup C & = \{ a,b,c,d,e,f,g,h,i \}
> \end{align*}
> $$

> [!esempio]- Esempio: unione degli insiemi dei numeri pari e dispari
> 
> Dati due insiemi:
> $$
> \begin{align*}
>  & A = \{n \in \mathbb{N} \mid n \bmod 2 = 0\} \\
>  & B = \{n \in \mathbb{N} \mid n \bmod 2 = 1\}
> \end{align*}
> $$
> ossia rispettivamente gli [insiemi](Matematica/Teoria%20degli%20insiemi/_index.md#^definizione-insieme) dei numeri naturali pari e dispari, allora lo loro unione è l'insieme dei numeri naturali $\mathbb{N}$%% link %%:
> $$
> A \cup B = \mathbb{N}
> $$

## 4.3 - Differenza di insiemi

> [!definizione]+ Definizione: differenza tra due insiemi
> 
> Dati due [insiemi](Matematica/Teoria%20degli%20insiemi/_index.md#^definizione-insieme) $A$ e $B$, si dice _**differenza**_ tra $A$ e $B$ e si denota "$A \setminus B$" l'insieme degli elementi presenti in $A$ ma non in $B$:
> $$
> A \setminus B = \{x \mid x \in A \land x \notin B\}
> $$
^definizione-differenza-tra-due-insiemi

%% rappresentazione con Eulero-Venn %%

> [!esempio]- Esempio: differenza tra due insiemi
> Dati due insiemi:
> 
> $$
> \begin{align*}
>  & A = \{ 0,1,2 \} \\
>  & B = \{ 2 \}
> \end{align*}
> $$
> la loro differenza è:
> $$
> A \setminus B = \{ 0,1 \}
> $$

## 4.4 - Differenza simmetrica di insiemi

> [!definizione]+ Definizione: differenza simmetrica tra due insiemi
> 
> Dati due [insiemi](Matematica/Teoria%20degli%20insiemi/_index.md#^definizione-insieme) $A$ e $B$, si dice _**differenza simmetrica**_ tra $A$ e $B$ e si denota "$A \Delta B$" l'insieme degli elementi presenti solamente in uno dei due insiemi:
> $$
> A \Delta B = \{ x \mid \forall x ((x \in A \land x \notin B) \lor (x \in B \land x \notin A)) \}
> $$
^definizione-differenza-simmetrica-tra-due-insiemi

> [!esempio]- Esempio: differenza simmetrica di due insiemi
> 
> Dati due insiemi:
> $$
> \begin{align*}
> A = \{ 1,4,6,23,57 \} \\
> B = \{ 2,4,6,8,10 \}
> \end{align*}
> $$
> la loro differenza simmetrica è:
> $$
> A \Delta B = \{1, 2, 8, 10, 23, 57\}
> $$

%% 
Alternativamente, si può indicare la differenza simmetrica tra $A$ e $B$ come l'unione delle differenze tra i due insiemi:
$$
A \Delta B = (A \setminus B) \cup (B \setminus A)
$$
Oppure, come la differenza tra la loro unione e la loro intersezione:
$$
A \Delta B = (A \cup B) \setminus (A \cap B)
$$

PRENDERE COME ESEMPIO:

> [!osservazione]+ Osservazione: $\color{#7F7F7F}\complement_B(A)=B\backslash A$
> 
> Dati due [insiemi](Matematica/Teoria%20degli%20insiemi/_index.md#^definizione-insieme) $A$ e $B$ con $A\subseteq B$, il complemento $\complement_B(A)$ di $A$ in $B$ si può esprimere anche come la [differenza](Matematica/Teoria%20degli%20insiemi/_index.md#^definizione-differenza-tra-due-insiemi) $B\backslash A$ tra $B$ e $A$:
> $$
> \complement_B(A)=B\backslash A
> $$

%%

%% 
(1.20) Proposizione Siano A e B due insiemi. Allora valgono i seguenti fatti:
a) A \ B = A \ (A \cap B);
b) AB = (A \cup B) \ (A \cap B);
c) AB = B A.
%%

## 4.5 - Complemento di un insieme

%% 
Usare come notazione $\complement_\mathcal{U}(A)$ perché è più completa
%%

> [!definizione]+ Definizione: complemento di un insieme
> 
> Dati un [insieme universo](Matematica/Teoria%20degli%20insiemi/_index.md#^definizione-insieme-universo) $\mathcal{U}$ e un insieme $A \subseteq \mathcal{U}$, si dice _**complemento**_ di $A$ e si denota "$A^\complement$" (ma anche "$A'$", "$\overline{A}$", "$\complement_\mathcal{U}(A)$" e "$\complement(A)$") la [differenza](Matematica/Teoria%20degli%20insiemi/_index.md#^definizione-differenza-tra-due-insiemi) $\mathcal{U} \setminus A$, cioè il [sottoinsieme](Matematica/Teoria%20degli%20insiemi/_index.md#^definizione-sottoinsieme) degli elementi di $\mathcal{U}$ non in $A$:
> $$
> A^\complement = \mathcal{U} \setminus A = \{ x \mid x \in \mathcal{U} \land x \notin A \}
> $$
^definizione-complemento-di-un-insieme

> [!osservazione]+ Osservazione: $\color{#7F7F7F}\mathbb{I} = \mathbb{Q}^\complement$ con $\color{#7F7F7F}\mathcal{U} = \mathbb{R}$
> 
> L'insieme dei numeri irrazionali $\mathbb{I}$%% link %% si può esprimere come complemento di $\mathbb{Q}$ se si considera come [insieme universo](Matematica/Teoria%20degli%20insiemi/_index.md#^definizione-insieme-universo) $\mathbb{R}$:
> $$
> \mathbb{I} = \mathbb{Q}^\complement \text{ con } \mathcal{U} = \mathbb{R}
> $$

> [!proprieta]+ Proprietà del doppio complemento: $\color{#FFFF7F}(A^\complement)^\complement = A$
> Dati un [insieme universo](Matematica/Teoria%20degli%20insiemi/_index.md#^definizione-insieme-universo) $\mathcal{U}$ e un insieme $A \subseteq \mathcal{U}$, il doppio complemento $(A^\complement)^\complement$ di $A$ in $\mathcal{U}$ è sempre uguale ad $A$:
> $$
> (A^\complement)^\complement = A
> $$
> 
> > [!dimostrazione]- Dimostrazione
> > 
> > Dobbiamo verificare che, qualunque sia $A$, valga la formula:
> > $$
> > \forall x (x \in (A^\complement)^\complement) \iff x \in A)
> > $$
> > Fissiamo quindi un generico $x$. Sfruttando la corrispondenza tra operazioni insiemistiche e connettivi logici visti in precedenza, la formula:
> > $$
> > x \in (A^\complement)^\complement \iff x \in A
> > $$
> > diventa:
> > $$
> > \lnot(\lnot(x \in A)) \iff x \in A
> > $$
> > 
> > Se ora nella formula sostituiamo l'affermazione "$x \in A$" con una corrispondente lettera proposizionale $P$ otteniamo la formula proposizionale:
> > $$
> > \lnot(\lnot P) \iff P
> > $$
> > 
> > In generale, il fatto che $P$ sia vera o meno dipenderà naturalmente dalla scelta di $A$ e $x$: ma noi vogliamo proprio dimostrare che l'equivalenza è vera in ogni caso (cioè comunque vengano presi $A$ e $x$), ovvero che la proposizione precedente è una tautologia%% link %%.
> > 
> > Utilizzando le tavole di verità%% link, quindi far vedere la tavola di verità %% si verifica facilmente che questo è vero (legge della doppia negazione%% link %%), quindi comunque siano presi $A$ e $x$ avremo che:
> > $$
> > x \in (A^\complement)^\complement \iff x \in A
> > $$
> > da cui $(A^\complement)^\complement = A$, come volevasi dimostrare.
> > 
> > $\blacksquare$
^Doppio-complemento

### 4.5.1 - Leggi di De Morgan

Le **leggi di De Morgan** (o **teoremi di De Morgan**) sono due regole fondamentali usate sia in **teoria degli insiemi** che in logica proposizionale%% link %%. Esse descrivono come negare combinazioni di proposizioni logiche o insiemi, permettendo di trasformare espressioni complesse in forme equivalenti.

In particolare, in teoria degli insiemi, le leggi di De Morgan descrivono la relazione tra [intersezione](Matematica/Teoria%20degli%20insiemi/_index.md#^definizione-intersezione-di-due-insiemi), [unione](Matematica/Teoria%20degli%20insiemi/_index.md#^definizione-unione-di-due-insiemi) e [complemento](Matematica/Teoria%20degli%20insiemi/_index.md#^definizione-complemento-di-un-insieme) di due [insiemi](Matematica/Teoria%20degli%20insiemi/_index.md#^definizione-insieme) e si esprimono nei seguenti due teoremi.

> [!proposizione]+ Prima legge di De Morgan: $\color{#FF7F7F}(A \cup B)^\complement = A^\complement \cap B^\complement$
> 
> Il complemento dell'insieme $A \cup B$, cioè l'insieme di tutti gli elementi che non appartengono né ad $A$ né a $B$, è uguale all'intersezione dei complementi di $A$ e $B$, ovvero l'insieme di tutti gli elementi che non appartengono a $A$ e, contemporaneamente, non appartengono a $B$:
> $$
> (A \cup B)^\complement = A^\complement \cap B^\complement
> $$ 
> 
> > [!dimostrazione]- Dimostrazione
> > 
> > Dobbiamo dimostrare che, per ogni $x$, vale la formula:
> > $$
> > x \in (A \cup B)^\complement \iff x \in (A^\complement \cap B^\complement)
> > $$
> > 
> > Utilizzando la corrispondenza tra operazioni insiemistiche e connettivi%% link %%, la formula precedente diventa:
> > $$
> > \lnot(x \in A \lor x \in B) \iff \lnot(x \in A) \land \lnot(x \in B)
> > $$
> > 
> > Questa è una proposizione della forma:
> > $$
> > \lnot(P \lor Q) \iff \lnot P \land \lnot Q
> > $$
> > dove $P$ e $Q$ sono, rispettivamente, "$x \in A$" e "$x \in B$".
> > 
> > Poiché tale proposizione è una tautologia%% link %%, l'identità insiemistica è dimostrata.
> > 
> > $\blacksquare$
^Prima-legge-di-De-Morgan

> [!proposizione]+ Seconda legge di De Morgan: $\color{#FF7F7F}(A \cap B)^\complement = A^\complement \cup B^\complement$
> 
> Il complemento dell'insieme $A \cap B$, cioè l'insieme di tutti gli elementi che appartengono contemporaneamente sia ad $A$ che a $B$, è uguale all'unione dei complementi di $A$ e $B$, ovvero l'insieme di tutti gli elementi che non appartengono ad $A$ oppure che non appartengono a $B$:
> $$
> (A \cap B)^\complement = A^\complement \cup B^\complement
> $$ 
> 
> > [!dimostrazione]- Dimostrazione
> > 
> > Dobbiamo dimostrare che, per ogni $x$, vale la formula:
> > $$
> > x \in (A \cap B)^\complement \iff x \in (A^\complement \cup B^\complement)
> > $$
> > 
> > Utilizzando la corrispondenza tra operazioni insiemistiche e connettivi%% link %%, la formula precedente diventa:
> > $$
> > \lnot(x \in A \land x \in B) \iff \lnot(x \in A) \lor \lnot(x \in B)
> > $$
> > 
> > Questa è una proposizione della forma:
> > $$
> > \lnot(P \land Q) \iff \lnot P \lor \lnot Q
> > $$
> > dove $P$ e $Q$ sono, rispettivamente, "$x \in A$" e "$x \in B$".
> > 
> > Poiché tale proposizione è una tautologia%% link %%, l'identità insiemistica è dimostrata.
> > 
> > $\blacksquare$
> 
> > [!dimostrazione]- Dimostrazione alternativa
> > 
> > La stessa identità può anche essere dimostrata utilizzando ciò che abbiamo già dimostrato, ovvero che per tutti gli [insiemi](Matematica/Teoria%20degli%20insiemi/_index.md#^definizione-insieme) $X$ e $Y$ valgono $(X^\complement)^\complement = X$ per la [proprietà del doppio complemento](Matematica/Teoria%20degli%20insiemi/_index.md#^Doppio-complemento) e $(X \cup Y)^\complement = X^\complement \cap Y^\complement$ per la [prima legge di De Morgan](Matematica/Teoria%20degli%20insiemi/_index.md#^Prima-legge-di-De-Morgan).
> > 
> > %% colorare le trasformazioni %%
> > Partendo da $(A \cap B)^\complement$, per la proprietà del doppio complemento abbiamo che:
> > $$
> > (A \cap B)^\complement = (A^\complement)^\complement \cap (B^\complement)^\complement)^\complement
> > $$
> > Per la prima legge di De Morgan, possiamo passare dall'intersezione all'unione:
> > $$
> > ((A^\complement)^\complement \cap (B^\complement)^\complement)^\complement = ((A^\complement \cup B^\complement)^\complement)^\complement
> > $$
> > Avendo dei doppi complementi, possiamo rimuoverli:
> > $$
> > ((A^\complement \cup B^\complement)^\complement)^\complement = A^\complement \cup B^\complement
> > $$
> > Si ottiene così la formula desiderata.
> > 
> > $\blacksquare$

%% 
Slide di Viale dalla 38 alla 42: varie dimostrazioni
%%

## 4.6 - Prodotto cartesiano di insiemi

> [!definizione]+ Definizione: prodotto cartesiano di due insiemi
> 
> Dati due [insiemi](Matematica/Teoria%20degli%20insiemi/_index.md#^definizione-insieme) $A$ e $B$, si definisce ***prodotto cartesiano*** di $A$ e $B$ e si denota "$A \times B$" l'insieme i cui elementi sono [coppie ordinate](Matematica/Teoria%20degli%20insiemi/_index.md#^definizione-tupla) di elementi con il primo elemento in $A$ e il secondo in $B$:
> $$
> A \times B = \{ (x, y) \mid x \in A \land y \in B \}
> $$
^definizione-prodotto-cartesiano-di-due-insiemi

> [!esempio]- Esempio: prodotto cartesiano di due insiemi
> 
> Dati due insiemi:
> 
> $$
> \begin{align*}
>  & A = \{ 1,2 \} \\
>  & B = \{ 3,4,5 \}
> \end{align*}
> $$
> il loro prodotto cartesiano è
> $$
> A \times B = \{(1,3),(1,4),(1,5),(2,3),(2,4),(2,5)\}
> $$

%%
Esempio: prodotto cartesiano tra due intervalli e relativa rappresentazione grafica

Dati due [insiemi](Matematica/Teoria%20degli%20insiemi/_index.md#^definizione-insieme) $A=\{x\mid 0\le x\le1\}$ e $B=\{x\mid -1\le x\le0\}$, %\%collegare a rappresentazione intervalli%\% rappresentabili anche con gli intervalli chiusi $A=[0,1]$ e $B=[-1,0]$, il loro prodotto cartesiano $A\times B$ è rappresentabile su un piano cartesiano come l'insieme di tutti i punti compresi tra il punto $\color{Red}A(0,1)$ e il punto $\color{Green}B(-1,0)$:

![Prodotto cartesiano tra due intervalli e relativa rappresentazione grafica.png]]
Embeddare Geogebra o [Manim](https://www.manim.community/)
%%

> [!osservazione]+ Osservazione: $\color{#7F7F7F}A \times \emptyset = \emptyset$
> 
> Il prodotto cartesiano tra un insieme $A$ e l'insieme vuoto $\emptyset$ è sempre pari all'insieme vuoto $\emptyset$:
> $$
> A \times \emptyset = \emptyset
> $$

> [!osservazione]+ Osservazione: $\color{#7F7F7F}A \ne \emptyset \land B \ne \emptyset \implies A \times B \ne \emptyset$
> 
> Il [prodotto cartesiano tra due insiemi](Matematica/Teoria%20degli%20insiemi/_index.md#^definizione-prodotto-cartesiano-di-due-insiemi) $A$ e $B$ non [vuoti](Matematica/Teoria%20degli%20insiemi/_index.md#^definizione-insieme-vuoto) è sempre pari a un insieme non vuoto:
> $$
> A \ne \emptyset \land B \ne \emptyset \implies A \times B \ne \emptyset
> $$

%%Esempio: rappresentazione grafica del prodotto cartesiano
Vedere slide 28 delle slide di Viale
%% 

%%
Osservazione:
Poiché i prodotti cartesiani sono costituiti da coppie ordinate, bisogna prestare attenzione al fatto che $A \times B$ è in genere distinto da $B \times A$ se $A \ne B$.
Ad esempio, se A = {0, 1, 2, 3} e B = {a, b, c}, allora la coppia (0, a) appartiene ad A \times B ma non a B \times A.
%%

> [!proposizione]+ Proposizione: cardinalità del prodotto cartesiano
> 
> Dati due insiemi finiti%% link %% $A$ e $B$, con $|A| = m$ e $|B| = n$, allora la cardinalità del loro prodotto cartesiano $|A\times B|$ è uguale al prodotto delle loro cardinalità $m\cdot n$; se, invece, almeno uno tra $A$ e $B$ è infinito, allora anche $|A \times B|$ è infinito:
> $$
> |A| = m, |B| = n
> \implies
> |A \times B| = \begin{cases}
> m \cdot n & m, n \ne \infty \\
> \infty & m, n = \infty
> \end{cases}
> $$
> 
> > [!dimostrazione]- Dimostrazione
> > 
> > Se $A$ e $B$ sono finiti con $|A| = m$ e $|B| = n$, si possono numerare ed elencare i loro elementi come $A=\{a_1,a_2,...,a_m\}$ e $B=\{b_1,b_2,...,b_n\}$ e si possono organizzare gli elementi di $A \times B$ in una tabella:
> > $$
> > \begin{matrix}
> > (a_1, b_1) & (a_1, b_2) & \dots & (a_1, b_n) \\
> > (a_2, b_1) & (a_2, b_2) & \dots & (a_2, b_n) \\
> > \vdots & \vdots & \ddots & \vdots \\
> > (a_m, b_1) & (a_m, b_2) & \dots & (a_m, b_n)
> > \end{matrix}
> > $$
> > La tabella include chiaramente tutti gli elementi di $A \times B$ una volta sola e, quindi, devono essere $m \cdot n$ in totale, essendo $m$ in verticale ed $n$ in orizzontale. Il caso in cui uno degli insieme è infinito è chiaro, in quanto la tabella risulterà avere righe o colonne infinite.
> > 
> > $\blacksquare$

### 4.6.1 - Potenza ennesima di un insieme

> [!definizione]+ Definizione: potenza $\color{#FF7FFF} n$-sima di un insieme
> 
> Il [prodotto cartesiano](Matematica/Teoria%20degli%20insiemi/_index.md#^definizione-prodotto-cartesiano-di-due-insiemi) $\underbrace{A \times A \times \ldots \times A}_{n \text{volte}}$ di $n$ copie di un [insieme](Matematica/Teoria%20degli%20insiemi/_index.md#^definizione-insieme) $A$ viene detto **potenza $n$-esima di $A$** e si denota come "$A^n$":
> 
> $$
> A^n = \underbrace{A \times A \times \ldots \times A}_{n \text{volte}} = \{ \langle x_0, x_1, \ldots, x_{n-1} \rangle \mid \forall i \in I (x_i \in A) \}
> $$
> 
> Per convenzione, inoltre, si pone anche $A^0 = \{\emptyset\}$.
^definizione-potenza-ennesima-di-un-insieme

> [!osservazione]+ Osservazione: valenza geometrica del prodotto cartesiano
> 
> Se si interpreta l'insieme $\mathbb{R}$ dei numeri reali%% link %% come una retta, allora il prodotto cartesiano $\mathbb{R}^2=\mathbb{R}\times\mathbb{R}$ è l'insieme formato da tutte le [coppie ordinate](Matematica/Teoria%20degli%20insiemi/_index.md#^definizione-tupla) $(x, y)$ di numeri reali:
> $$
> \mathbb{R}^2 = \{(x, y)\mid x \in \mathbb{R}\land y \in \mathbb{R}\}
> $$
> In altre parole, $\mathbb{R}^2$ non è nient'altro che il piano cartesiano, in cui un elemento di $\mathbb{R}^2$ è un punto identificato dalla coppia $(x, y)$; stesso discorso si può fare per l'insieme $\mathbb{R}^3$, ossia l'insieme che rappresenta lo spazio cartesiano in cui i punti sono identificati dalle tre coordinate $(x,y,z)$.

# 5 - Famiglia di insiemi

> [!definizione]+ Definizione: famiglia di insiemi
> 
> Un [insieme](Matematica/Teoria%20degli%20insiemi/_index.md#^definizione-insieme) è detto **_famiglia di insiemi_** se ognuno degli elementi è a sua volta un insieme e viene denotata come:
> $$
> \{ A_i \}_{i \in I}
> $$
> dove l'insieme $I$ è chiamato _**insieme degli indici**_ e ciascun $i \in I$ identifica univocamente un insieme $A_i$ della famiglia.
^definizione-famiglia-di-insiemi

## 5.1 - Operazioni su famiglie di insiemi

> [!definizione]+ Definizione: intersezione di una famiglia di insiemi
> 
> Data una [famiglia di insiemi](Matematica/Teoria%20degli%20insiemi/_index.md#^definizione-famiglia-di-insiemi) $\{ A_i \}_{i \in I}$, l'[intersezione](Matematica/Teoria%20degli%20insiemi/_index.md#^definizione-intersezione-di-due-insiemi) degli $A_i$ è l'insieme degli elementi che appartengono a ogni $A_i$:
> $$
> \bigcap_{i = 1}^n A_i = \{x \mid \forall i \in I (x \in A_i)\}
> $$

> [!definizione]+ Definizione: unione di una famiglia di insiemi
> 
> Data una [famiglia di insiemi](Matematica/Teoria%20degli%20insiemi/_index.md#^definizione-famiglia-di-insiemi) $\{ A_i \}_{i \in I}$, l'[unione](Matematica/Teoria%20degli%20insiemi/_index.md#^definizione-unione-di-due-insiemi) degli $A_i$ è l'insieme degli elementi che appartengono ad almeno un $A_i$:
> $$
> \bigcup_{i = 1}^n A_i = \{x \mid \exists i \in I (x \in A_i)\}
> $$

%%
Esempio: slide 16 e 17 di Viale
%%

%% 
Esempio:
Data una famiglia di insiemi $\mathcal A$ formata dagli $n$-esimi insiemi $A_n\in\mathcal A$ con $n \in \mathbb{N}\setminus\{0\}$ in cui ogni $A_n$ è definito come l'[intervallo aperto] che va da $-\dfrac{1}{n}$ a $\dfrac{1}{n}$, quindi $A_n=(-\dfrac{1}{n},\dfrac{1}{n})$. Si ha quindi che $\displaystyle\bigcap_{n=0}^{+\infty}A_n=\{0\}$ perché $0 \in A_n$ per ogni $n \in \mathbb{N}\setminus\{0\}$.
%%

> [!definizione]+ Definizione: prodotto cartesiano di una famiglia di insiemi
> 
> Data una [famiglia di insiemi](Matematica/Teoria%20degli%20insiemi/_index.md#^definizione-famiglia-di-insiemi) $\{ A_i \}_{i \in I}$, il [prodotto cartesiano](Matematica/Teoria%20degli%20insiemi/_index.md#^definizione-prodotto-cartesiano-di-due-insiemi) degli $A_i$ è l'insieme delle [$n$-uple](Matematica/Teoria%20degli%20insiemi/_index.md#^definizione-tupla) $(x_1, x_2, \ldots, x_n)$ con $x_i\in A_i$:
> 
> $$
> \prod_{i = 1}^n A_i = \{(x_1, x_2, \ldots, x_n) \mid \forall i\in I(x_i \in A_i)\}
> $$

---

> [!fonti]+ Fonti
> 
> - 🏫 Corso di Laurea in Informatica (`L-31 R`) presso l'Università di Torino:
>     - Corso di _Matematica Discreta, Algebra e Geometria - parte di Matematica Discreta & Algebra (parte 1) - canale C_, A.A. 2023-24 ([pagina Moodle](https://informatica.i-learn.unito.it/course/view.php?id=2750)):
> 		- Lezioni in aula dei Proff. Chen Yu e Terracini Lea.
>     - Corso di _Matematica Discreta, Algebra e Geometria - parte di Algebra Lineare & Geometria (parte 2) - canale C_, A.A. 2023-24 ([pagina Moodle](https://informatica.i-learn.unito.it/course/view.php?id=2750)):
> 		- Lezioni in aula del Prof. Radeschi Marco.
>     - Corso di _Logica Matematica_, A.A. 2022-23 ([pagina Moodle](https://informatica.i-learn.unito.it/course/view.php?id=2480)):
> 		- Slide dei Proff. Andretta Alessandro, Motto Ros Luca e Viale Matteo:
> 			- [_2.1 - Insiemi_](https://informatica.i-learn.unito.it/pluginfile.php/336712/mod_folder/content/0/Capitolo%202%20-%20Elementi%20di%20teoria%20degli%20insiemi/2.1%20-%20Insiemi_moodle.pdf).
> - 📚 _Lezioni di Analisi Matematica I_ di Sergio Lancelotti, Celid, 2020 (ISBN: `978-8867891979`):
> 	- Capitolo 1 - _Nozioni preliminari_:
> 		- 1 - _Richiami di teoria degli insiemi_:
> 			- 1.1 - _Insiemi e loro proprietà_.
> 			- 1.2 - _Rappresentazione di un insieme_.
> 			- 1.3 - _Operazioni insiemistiche_.
