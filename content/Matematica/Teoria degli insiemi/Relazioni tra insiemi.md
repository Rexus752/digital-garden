
> [!premessa]+ Premessa
> 
> Ciao! Se è la prima volta che capiti su questo sito, ti consiglio di consultare la [pagina principale](index.md) di questo cosiddetto _Giardino Digitale_ per scoprire meglio cos'è e come navigarlo.
> 
> Lo stato di questa nota è al momento: 🔴 <font color="#FF7F7F">_Bozza_</font>.

---

Le **relazioni tra insiemi** descrivono i legami che possono esistere tra due o più [insiemi](Teoria%20degli%20insiemi.md#^definizione-insieme). Queste relazioni sono fondamentali in [teoria degli insiemi](Teoria%20degli%20insiemi.md#^definizione-teoria-degli-insiemi).

# 1 - Introduzione alle relazioni

> [!definizione]+ Definizione: relazione $\color{#FF7FFF}n$-aria
> 
> Dati $n \ge 1$ [insiemi](Teoria%20degli%20insiemi.md#^definizione-insieme) non [vuoti](Teoria%20degli%20insiemi.md#^definizione-insieme-vuoto) $A_0, A_1, \ldots, A_{n-1}$, si definisce _**relazione $n$-aria**_ o _**relazione di grado $n$**_ e si denota "$\mathcal{R}$" un [sottoinsieme](Teoria%20degli%20insiemi.md#^definizione-sottoinsieme) del [prodotto cartesiano](Teoria%20degli%20insiemi.md#^definizione-prodotto-cartesiano-di-due-insiemi) tra tutti gli insiemi:
> 
> $$
> \mathcal{R} \subseteq A_0 \times A_1 \times \ldots \times A_{n-1}
> $$
> 
> Nel caso di una relazione sottoinsieme di una [potenza $n$-sima](Teoria%20degli%20insiemi.md#^definizione-potenza-ennesima-di-un-insieme) $A^n$, si parla di _**relazione $n$-aria su $A$**_:
> 
> $$
> R \subseteq A^n = \underbrace{A \times A \times \ldots \times A}_{n \text{volte}} 
> $$
> 
> Inoltre, quando $n = 1$, oltre a "_relazione unaria_" si parla anche di _**predicato**_, mentre quando $n=2$, oltre a _"relazione binaria"_, si parla anche semplicemente di _"relazione"_ e, dati due elementi $a \in A_0$ e $b \in A_1$, si scrive:
> $$
> a \mathcal{R} b
> $$
> invece di $(a,b) \in \mathcal{R}$.
^definizione-relazione-n-aria

> [!esempio]- Esempio: relazione binaria tra due insiemi
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

%% 
Osservazione: in aRb, al posto della R ci può anche andare un simbolo
%%

> [!esempio]- Esempio: gli ordinamenti sono relazioni binarie
> 
> Le usuali operazioni di ordine sui numeri naturali $\mathbb{N}$%% link %% sono relazioni binarie su $\mathbb{N}$ (es. l'ordine non-decrescente $\le$%% link %% è una relazione binaria e la coppia $(2, 7)$ è un elemento di tale relazione perché $2 \le 7$, mentre la coppia $(5, 1)$ non lo è).
> 
> Inoltre, essendo una relazione binaria, si può notare come solitamente si scriva $2 \le 7$ anziché $(2,7) \in \le$.

## 1.1 - Rappresentazioni grafiche delle relazioni con i diagrammi di Eulero-Venn

%% collegamento ocn diagrammi di eulero-venn %%

Le relazioni $n$-arie si possono rappresentare graficamente tramite i diagrammi di Eulero-Venn%% link %%.

%%
Slide 10-11 di Viale
%%

Una relazione $n$-aria su uno stesso insieme $A$ si può rappresentare o come una generica relazione $n$-aria su $n$ "copie" dell'insieme $A$, oppure come insieme di frecce tra i punti della stessa copia di $A$.

%%
Slide 12 di Viale
%%

## 1.2 - Rappresentazioni grafiche delle relazioni con il piano cartesiano

Esattamente come il prodotto cartesiano si può rappresentare sul piano cartesiano, anche le relazioni $n$-arie si possono rappresentare su quest'ultimo essendo sottoinsiemi del prodotto.%% aggiungere tutti i link %%

%% 
Slide 13-14 di Viale
%%

## 1.3 - Relazione inversa

> [!definizione]+ Definizione: relazione inversa
> 
> Dati due [insiemi](Teoria%20degli%20insiemi.md#^definizione-insieme) $A$ e $B$ e una loro [relazione binaria](Relazioni%20tra%20insiemi.md#^definizione-relazione-n-aria) $\mathcal{R} \subseteq A \times B$, si definisce _**relazione inversa**_ di $\mathcal{R}$ e si indica con "$\mathcal{R}^{-1}$" un [sottoinsieme](Teoria%20degli%20insiemi.md#^definizione-sottoinsieme) del [prodotto cartesiano](Teoria%20degli%20insiemi.md#^definizione-prodotto-cartesiano-di-due-insiemi) $B \times A$:
> 
> $$
> \mathcal{R}^{-1} = \{ (b,a) \in B \times A \mid (a,b) \in \mathcal{R} \} \subseteq B \times A
> $$
> 
> In altre parole, per ogni $b \in B$ e per ogni $a \in A$ si ha:
> $$
> b \mathcal{R}^{-1} a \iff a \mathcal{R} b
> $$

> [!esempio]
> 
> Se $\mathcal{R}$ è la relazione $\le$ di minore o uguale su $\mathbb{N}$, allora $\mathcal{R}^{-1}$ sarà la relazione $\ge$ di maggiore o uguale su $\mathbb{N}$ perché:
> $$
> a \le b \iff b \ge a
> $$

%%

> [!esempio]- Esempio
> 
> Se R è la relazione \le di minore o uguale su N, allora R^{-1} è la relazione \ge di maggiore o uguale su N.

> [!osservazione]+ 2 osservazioni
> 
> 1. Chiaramente per ogni relazione binaria R: (R^{-1})^{-1} = R,
> 2. rng(R^{-1}) = dom(R), dom(R^{-1}) = rng(R).

%%

### 1.3.1 - Rappresentazione grafica di una relazione inversa tramite diagrammi di Eulero-Venn

%%
Slide 19 di Viale
%%

## 1.4 - Proprietà delle relazioni binarie

> [!definizione]+ Definizione: proprietà delle relazioni binarie
> 
> Dati un [insieme](Teoria%20degli%20insiemi.md#^definizione-insieme) $A$ e una [relazione binaria](Relazioni%20tra%20insiemi.md#^definizione-relazione-n-aria) $\mathcal{R}$ su $A$ (cioè $\mathcal{R} \subseteq A^2$), essa può avere le seguenti _**proprietà**_:
> - **Riflessività**: $\forall a \in A (a \mathcal{R} a)$.
> - **Irriflessività**: $\forall a \in A (\lnot(a \mathcal{R} a ))$.
> - **Simmetria**: $\forall a,b \in A (a \mathcal{R} b \implies b \mathcal{R} a)$.
> - **Antisimmetria**: $\forall a,b \in A (a \mathcal{R} b \land b \mathcal{R} a \implies a = b)$.
> - **Transitività**: $\forall a,b,c \in A (a \mathcal{R} b \land b \mathcal{R} c \implies a \mathcal{R} c)$.
> - **Totalità**: $\forall a,b \in A (a \mathcal{R} b \lor b \mathcal{R} a)$.
^definizione-proprieta-delle-relazioni-binarie

> [!osservazione]+ Osservazione: relazione simmetrica solo se $\color{#7F7F7F} \mathcal{R} = \mathcal{R}^{-1}$
> 
> Dati un [insieme](Teoria%20degli%20insiemi.md#^definizione-insieme) $A$ e una [relazione binaria](Relazioni%20tra%20insiemi.md#^definizione-relazione-n-aria) $\mathcal{R}$ su $A$ (cioè $\mathcal{R} \subseteq A^2$), $\mathcal{R}$ è simmetrica se e solo se $\mathcal{R} = \mathcal{R}^{-1}$, ovvero se:
> $$
> \forall (a,b) \in A^2 (a \mathcal{R} b \iff a \mathcal{R}^{-1}b)
> $$

%%

> [!osservazione]+ Osservazione
> 
> Inoltre, R è riflessiva/simmetrica/antisimmetrica/transitiva se e solo se R-1 lo `e.

> [!esempio]- Esempio
> 
> Sia A l'insieme delle rette del piano e sia R una relazione su A.
> - Se a R b significa che a e b sono rette parallele (eventualmente coincidenti), allora R è riflessiva, simmetrica e transitiva.
> - Se a R b significa che le rette a e b hanno intersezione non vuota, allora R è riflessiva e simmetrica, ma non transitiva.
> - Se a R b significa che le rette a e b sono ortogonali, allora R è simmetrica, ma non è né riflessiva, né transitiva.

%%

| Relazione                                                                                                          | Riflessività<br> | Simmetria | Transitività | Totalità |
| ------------------------------------------------------------------------------------------------------------------ | ---------------- | --------- | ------------ | -------- |
| [Relazione di equivalenza](Relazioni%20tra%20insiemi.md#^definizione-relazione-di-equivalenza)                     | ✅                | ✅         | ✅            | ➖        |
| [Relazione di ordine](Relazioni%20tra%20insiemi.md#^definizione-relazione-di-ordine)                               | ✅                | ❌         | ✅            | ➖        |
| [Relazione di ordine totale](Relazioni%20tra%20insiemi.md#^definizione-relazione-di-ordine-totale)                 | ✅                | ❌         | ✅            | ✅        |
| [Relazione di successione immediata](Relazioni%20tra%20insiemi.md#^definizione-relazione-di-successione-immediata) | ✅                | ❌         | ✅            | ➖        |
| [Relazione di ordine stretto](Relazioni%20tra%20insiemi.md#^definizione-relazione-di-ordine-stretto)               | ❌                | ➖         | ✅            | ➖        |
| [Relazione di pre-ordine](Relazioni%20tra%20insiemi.md#^definizione-relazione-di-pre-ordine)                       | ✅                | ➖         | ✅            | ➖        |

### 1.4.1 - Rappresentazioni grafiche delle proprietà delle relazioni

%% 

> [!esempio]- Esempio
> 
> ![](Pasted%20image%2020240928190234.png)
> 
> ![](Pasted%20image%2020240928190241.png)
> 
> ![](Pasted%20image%2020240928190257.png)
> 
> ![](Pasted%20image%2020240928190306.png)
> 
> ![](Pasted%20image%2020240928190336.png)
> 
> ![](Pasted%20image%2020240928190355.png)
> 
> ![](Pasted%20image%2020240928190406.png)
> 
> ![](Pasted%20image%2020240928190414.png)
> 
> ![](Pasted%20image%2020240928190424.png)
> 
> ![](Pasted%20image%2020240928190432.png)
> 
> ![](Pasted%20image%2020240928190441.png)
> 
> ![](Pasted%20image%2020240928190450.png)

%%

# 2 - Relazioni di equivalenza

> [!definizione]+ Definizione: relazione di equivalenza
> 
> Dato un [insieme](Teoria%20degli%20insiemi.md#^definizione-insieme) $A$, si definisce _**relazione di equivalenza**_ su $A$ e si denota con "$\sim$" una [relazione binaria](Relazioni%20tra%20insiemi.md#^definizione-relazione-n-aria) che rispetta le seguenti [proprietà](Relazioni%20tra%20insiemi.md#^definizione-proprieta-delle-relazioni-binarie):
> - **Riflessività**: $\forall a \in A (a \mathcal{R} a)$.
> - **Simmetria**: $\forall a,b \in A (a \mathcal{R} b \implies b \mathcal{R} a)$.
> - **Transitività**: $\forall a,b,c \in A (a \mathcal{R} b \land b \mathcal{R} c \implies a \mathcal{R} c)$.
^definizione-relazione-di-equivalenza

> [!esempio]- Esempio: relazione di divisibilità per $\color{#7F7FFF}n$ tra due interi
> 
> Dato un numero naturale $n \in \mathbb{N}$, un numero intero $x \in \mathbb{Z}$ si dice _divisibile_ per $n$ e si denota con "$n|x$" se esiste un $k \in \mathbb{Z}$ tale che $k \cdot n = x$. Si può definire una relazione di equivalenza sull'insieme dei numeri interi $\mathbb{Z}$%% link %% affermando che, dati due elementi $x, y \in \mathbb{Z}$, $x$ è in relazione a $y$ se la loro differenza è divisibile per $n$:
> $$
> x \sim y \iff n|(x-y)
> $$
> Si può dimostrare che questa è una relazione di equivalenza verificando le tre [proprietà](Relazioni%20tra%20insiemi.md#^definizione-proprieta-delle-relazioni-binarie):
> 1. **Riflessività**: $n|(x-x)\implies n|0$ vale, perché $0$ è divisibile per qualsiasi numero naturale $n$.
> 2. **Simmetria**: $n|(x-y)\implies n|(y-x)$ vale, perché se $x-y$ è divisibile per $n$, allora è divisibile anche il suo opposto $y-x$ (es. $2|(12-6)\implies 2|(6-12)$, con $n=2,x=12,y=6$).
> 3. **Transitività**: $n|(x-y),n|(y-z)\implies n|(x-z)$ vale, perché se $x-y$ e $y-z$ sono divisibili per $n$, lo è anche $x-z$ (es. $2|(12-6),2|(6-4)\implies 2|(12-4)$, con $n=2,x=12,y=6,z=4$).

> [!notazione]+ Notazioni alternative per le relazioni di equivalenza
> 
> Oltre al simbolo "$\sim$", spesso per denotare le [relazioni di equivalenza](Relazioni%20tra%20insiemi.md#^definizione-relazione-di-equivalenza) si usano le lettere $\mathcal{E}$, $\mathcal{F}$, ecc., oppure simboli che, in qualche misura, richiamano la relazione d'uguaglianza%% link %%, quali ad esempio "$\equiv$", "$\simeq$", "$\cong$", "$\approx$", ecc.

> [!definizione]+ Definizione: classe di equivalenza
> 
> Dati un [insieme](Teoria%20degli%20insiemi.md#^definizione-insieme) $A$ e una [relazione di equivalenza](Relazioni%20tra%20insiemi.md#^definizione-relazione-di-equivalenza) $\sim$ su $A$, la **classe di equivalenza** di un elemento $a \in A$ rispetto alla relazione di equivalenza $\sim$, indicata con "$[a]_\sim$", è l'insieme degli elementi di $A$ che hanno la [relazione di equivalenza](Relazioni%20tra%20insiemi.md#^definizione-relazione-di-equivalenza) $\sim$ con $a$:
> $$
> [a]_\sim = \{x \in A \mid x \sim a\}
> $$
> Quando la relazione $\sim$ è chiara dal contesto, si può scrivere anche solo $[a]$ al posto di $[a]_\sim$.
^definizione-classe-di-equivalenza

> [!definizione]+ Definizione: insieme quoziente
>
> Dati un [insieme](Teoria%20degli%20insiemi.md#^definizione-insieme) $A$ e una [relazione di equivalenza](Relazioni%20tra%20insiemi.md#^definizione-relazione-di-equivalenza) $\sim$ su $A$, l'insieme delle [classi di equivalenza](Relazioni%20tra%20insiemi.md#^definizione-classe-di-equivalenza) $[a]_\sim$ si dice _**insieme quoziente**_ di $X$ per la relazione $\sim$ e si indica con "$A/\sim$":
> $$
> A/\sim = \{[a]_\sim \mid a \in A\}
> $$
^definizione-insieme-quoziente

> [!esempio]- Esempio: relazione di equivalenza su automobili con stesso colore
> 
> Dati un [insieme](Teoria%20degli%20insiemi.md#^definizione-insieme) $A$ e una [relazione di equivalenza](Relazioni%20tra%20insiemi.md#^definizione-relazione-di-equivalenza) $\sim$ su $A$ letta come _"ha lo stesso colore di"_, allora una [classe di equivalenza](Relazioni%20tra%20insiemi.md#^definizione-classe-di-equivalenza) $[a]_\sim$ può essere quella che comprende tutte le automobili verdi, mentre l'[insieme quoziente](Relazioni%20tra%20insiemi.md#^definizione-insieme-quoziente) $A/\sim$ è l'insieme dei colori delle automobili.

> [!esempio]- Esempio: insieme $\color{#7F7FFF} \mathbb{Q}$ dei numeri razionali come insieme quoziente
> 
> L'insieme $\mathbb{Q}$ dei numeri razionali%% link %% può essere espresso come un [insieme quoziente](Relazioni%20tra%20insiemi.md#^definizione-insieme-quoziente). Data una coppia $(p,q)$ ottenuta dal [prodotto cartesiano](Teoria%20degli%20insiemi.md#^definizione-prodotto-cartesiano-di-due-insiemi) $\mathbb{Z}\times (\mathbb{Z}\setminus\{0\})$ (quindi $p$ può essere qualsiasi numero intero, mentre $q$ qualsiasi numero intero eccetto lo $0$), si può definire una relazione di equivalenza come:
> $$
> (p, q) \sim (p', q') \iff pq' = p'q
> $$
> Ciò è verificabile se si interpreta la coppia $(p,q)$ come una frazione $\dfrac{p}{q}$, quindi questa [relazione di equivalenza](Relazioni%20tra%20insiemi.md#^definizione-relazione-di-equivalenza) indica che due frazioni sono in relazione tra loro se sono uguali il prodotto tra il numeratore di uno e il denominatore dell'altro: $\dfrac{p}{q} = \dfrac{p'}{q'} \iff pq' = p'q$ (es. prendendo le frazioni $\dfrac{2}{3}$ e $\dfrac{4}{6}$, si può constatare che $2 \cdot 6 = 3 \cdot 4$).
> Se si prende l'insieme quoziente di questa relazione, ossia $[\mathbb{Z} \times (\mathbb{Z} \setminus \{0\})] / \sim$, si può notare come esso corrisponda proprio all'insieme $\mathbb{Q}$ dei numeri razionali perché comprende tutte le combinazioni possibili di numeri presenti in $\mathbb{Q}$.

> [!osservazione]+ Osservazione: $\color{#7F7F7F} (A/\sim) \subseteq \mathcal{P}(A)$
> 
> Dati un [insieme](Teoria%20degli%20insiemi.md#^definizione-insieme) $A$ e una [relazione di equivalenza](Relazioni%20tra%20insiemi.md#^definizione-relazione-di-equivalenza) $\sim$ su $A$, l'[insieme quoziente](Relazioni%20tra%20insiemi.md#^definizione-insieme-quoziente) $A/\sim$ è una [famiglia](Teoria%20degli%20insiemi.md#^definizione-famiglia-di-insiemi) di sottoinsiemi di $A$, cioè è un sottoinsieme dell'[insieme delle parti](Teoria%20degli%20insiemi.md#^definizione-insieme-delle-parti) di $A$:
> $$
> (A/\sim) \subseteq \mathcal{P}(A) 
> $$
> 
> Per costruzione, infatti, ogni elemento di $A / \sim$ è una classe di equivalenza $[a]_\sim$, e ogni classe di equivalenza è un sottoinsieme di $A$. Quindi:
> $$
> \forall a \in A ([a]_\sim \subseteq A) 
> $$
> Poiché $A / \sim$ è formato unicamente dalle classi di equivalenza, ogni elemento di $A / \sim$ è un sottoinsieme di $A$.
> 
> L'insieme delle parti $\mathcal{P}(A)$ è definito come l'insieme di tutti i sottoinsiemi di $A$ e, dal momento che ogni classe di equivalenza è un sottoinsieme di $A$, si ha che $A / \sim \subseteq \mathcal{P}(A)$.

> [!esempio]- Esempio: campionato di serie A come insieme quoziente
> 
> Dato un [insieme](Teoria%20degli%20insiemi.md#^definizione-insieme) $X$ di tutti i giocatori di squadre di serie A e una [relazione binaria](Relazioni%20tra%20insiemi.md#^definizione-relazione-n-aria) $\mathcal{R}$ su $X$ stabilendo che due giocatori $a,b \in X$ sono in relazione ($a \mathcal{R} b$) se e solo se $a$ e $b$ giocano nella stessa squadra.
> 
> La relazione $\mathcal{R}$ è chiaramente riflessiva, simmetrica e transitiva, quindi è una [relazione di equivalenza](Relazioni%20tra%20insiemi.md#^definizione-relazione-di-equivalenza) su $X$.%% far vedere come sono rispettate queste proprietà %%
> Le [classi di equivalenza](Relazioni%20tra%20insiemi.md#^definizione-classe-di-equivalenza) sono le squadre del campionato di serie A, mentre il [quoziente](Relazioni%20tra%20insiemi.md#^definizione-insieme-quoziente) $X / \mathcal{R}$ consiste nel campionato di serie A, ossia è l'insieme delle squadre che giocano in quel campionato.

> [!esempio]- Esempio: regioni italiane come insieme quoziente
> 
> Dato un [insieme](Teoria%20degli%20insiemi.md#^definizione-insieme) $X$ di tutti i comuni italiani e una [relazione binaria](Relazioni%20tra%20insiemi.md#^definizione-relazione-n-aria) $\mathcal{R}$ su $X$ stabilendo che due comuni $a,b \in X$ sono in relazione ($a \mathcal{R} b$) se e solo se $a$ e $b$ si trovano nella stessa regione.
> 
> La relazione $\mathcal{R}$ è chiaramente riflessiva, simmetrica e transitiva, quindi è una [relazione di equivalenza](Relazioni%20tra%20insiemi.md#^definizione-relazione-di-equivalenza) su $X$.%% far vedere come sono rispettate queste proprietà %%
> Le [classi di equivalenza](Relazioni%20tra%20insiemi.md#^definizione-classe-di-equivalenza) sono le regioni italiane, mentre il [quoziente](Relazioni%20tra%20insiemi.md#^definizione-insieme-quoziente) $X / \mathcal{R}$ consiste nell'insieme di tutte le regioni italiane.

%%

> [!esempio]- Esempio: congruenza modulo $\color{#7F7FFF} 2$
> 
> Dati due interi $a, b \in \mathbb{Z}$, $a$ è congruente a $b \bmod 2$ se $a - b$ è pari (ovvero se $a - b = 2 \cdot k$ per qualche $k \in \mathbb{Z}$). In questo caso scriviamo
> $$
> a \equiv b \bmod 2
> $$
> La relazione di congruenza modulo $2$ è una relazione di equivalenza:
> - Riflessività: $a - a = 0$ è pari, quindi $a \equiv a \bmod 2$.
> - Simmetria: $b - a = -(a - b)$, quindi $a - b$ è pari se e solo se $b - a$ lo è.
> - Transitività: $a - c = (a - b) + (b - c)$, per cui se $a - b$ e $b - c$ sono pari, allora anche $a - c$ lo è.
> 
> Ci sono due classi di equivalenza per questa relazione:
> - I numeri pari, ossia $[0] = \{n \mid n-0 \bmod 2 = 0\}$.
> - I numeri dispari, ossia $[1] = \{n \mid n - 1 \bmod 2 = 0\}$.
> 
> L'insieme quoziente $\{[0], [1]\}$ ha esattamente $2$ elementi e lo si indica con "$\mathbb{Z}_2$" ovvero $\dfrac{\mathbb{Z}}{2\mathbb{Z}}$.

> [!esempio]- Esempio: congruenza modulo $\color{#7F7FFF} n$
> 
> Esempio: congruenza modulo n
> Più in generale, dato 0̸ = n \in N e a, b \in Z, a è congruente a b modulo
> n se a - b è un multiplo di n (ovvero se a - b = n \cdot k per qualche k \in Z).
> In questo caso scriviamo
> a \equiv b mod n
> 
> Esercizio (perché Viale ha scritto che questo è un esercizio?)
> La relazione di congruenza modulo n è una relazione di equivalenza e
> ciascuna classe di equivalenza è della forma
> [k] = {a \in Z | la divisione intera di a per n ha resto k}
> per qualche k \in {0, \ldots , n - 1}
> 
> Dunque l'insieme quoziente risultante
> Z_n = Z/nZ := {[k] | 0 \le k \le n - 1}
> ha esattamente n elementi.

%%

> [!proposizione]+ Proposizione: due classi di equivalenza o sono disgiunte o coincidono
> 
> Data una [relazione di equivalenza](Relazioni%20tra%20insiemi.md#^definizione-relazione-di-equivalenza) $\sim$ su un [insieme](Teoria%20degli%20insiemi.md#^definizione-insieme) $A$ e due elementi $a,b \in A$, se $a \sim b$, allora $[a]_\sim = [b]_\sim$:
> $$
> a \sim b \implies [a]_\sim = [b]_\sim
> $$
> Inoltre, se $a \not\sim b$, cioè se $\lnot(a \sim b)$, allora $[a]_\sim \cap [b]_\sim = \emptyset$:
> $$
> a \not\sim b \implies [a]_\sim \cap [b]_\sim = \emptyset
> $$
> 
> In particolare, due classi di equivalenza o sono disgiunte o coincidono.
^proposizione-due-classi-di-equivalenza-o-sono-disgiunte-o-coincidono

%%

> [!dimostrazione]- Dimostrazione
> 
> Supponiamo a E b. Sia c \in [a]E : allora c E a e per la proprietà transitiva
> c E b, quindi c \in [b]E . Essendo c arbitrario, abbiamo dimostrato che
> [a]E \subseteq [b]E . Sia ora c \in [b]E : allora c E b. Per la proprietà simmetrica
> b E a, da cui c E a per la proprietà transitiva: quindi c \in [a]E . Segue che
> [b]E \subseteq [a]E . Per il principio della doppia inclusione abbiamo quindi
> [a]E = [b]E .
> 
> Supponiamo ora a NOT-E b. Verifichiamo che in questo caso [a]E \cap [b]E = \emptyset.
> Supponiamo, per assurdo, che ci sia un c \in [a]E \cap [b]E . Allora c E b, da
> cui b E c per simmetria. Inoltre c E a, quindi b E a per transitivit`a, e
> a E b per simmetria. Ma questo contraddice la nostra assunzione che
> a̸ E b.
> 
> $\blacksquare$

%%

> [!esempio]- Esempio: relazione di congruenza modulo $\color{#7F7FFF} 3$
> 
> Consideriamo l'[insieme](Teoria%20degli%20insiemi.md#^definizione-insieme) $A = \{0, 1, 2, 3, 4, 5\}$ e la [relazione di equivalenza](Relazioni%20tra%20insiemi.md#^definizione-relazione-di-equivalenza) $\sim$ definita dalla congruenza modulo $3$%% link %%:
> $$
> a \sim b \iff a \equiv b (\text{mod} \ 3)
> $$
> Questo significa che due numeri sono equivalenti se hanno lo stesso resto quando divisi per $3$.
> 
> Le [classi di equivalenza](Relazioni%20tra%20insiemi.md#^definizione-classe-di-equivalenza), in base alla relazione $\sim$, sono i gruppi di numeri che danno lo stesso resto modulo $3$. Ecco le classi di equivalenza possibili:
> - $[0]_\sim = \{0, 3\}$ perché $0 \equiv 3 \ (\text{mod} \ 3)$.
> - $[1]_\sim = \{1, 4\}$ perché $1 \equiv 4 \ (\text{mod} \ 3)$.
> - $[2]_\sim = \{2, 5\}$ perché $2 \equiv 5 \ (\text{mod} \ 3)$.
> 
> Verifichiamo la proposizione quindi in entrambi i casi:
> - Se $a \sim b$, allora le classi di equivalenza $[a]_\sim$ e $[b]_\sim$ devono essere uguali. Ad esempio:
> 	- Se $a = 0$ e $b = 3$, allora $0 \sim 3$, quindi $[0]_\sim = [3]_\sim = \{0, 3\}$.
> 	- Se $a = 1$ e $b = 4$, allora $1 \sim 4$, quindi $[1]_\sim = [4]_\sim = \{1, 4\}$.
> 	
> 	In entrambi i casi, le classi di equivalenza coincidono.
> - Se $a \not\sim b$, allora le classi di equivalenza $[a]_\sim$ e $[b]_\sim$ sono disgiunte, cioè non hanno elementi in comune. Ad esempio, se $a=0$ e $b=1$, allora $0 \not\sim 1$, quindi $[0]_\sim = \{ 0,3 \}$ e $[1]_\sim = \{ 1,4 \}$ e possiamo vedere che $[0]_\sim \cap [1]_\sim = \emptyset$
> 	In questo caso, le classi di equivalenza sono disgiunte.

## 2.1 - Relazioni di equivalenza e partizioni

> [!osservazione]+ Osservazione: insieme quoziente $\color{#7F7F7F} A/\sim$ partizione di $\color{#7F7F7F} A$
> 
> Data una [relazione di equivalenza](Relazioni%20tra%20insiemi.md#^definizione-relazione-di-equivalenza) $\sim$ su un [insieme](Teoria%20degli%20insiemi.md#^definizione-insieme) $A$, l'[insieme quoziente](Relazioni%20tra%20insiemi.md#^definizione-insieme-quoziente) $A/\sim$ è una partizione%% link %% di $A$, infatti:
> - Ogni $[a]_\sim \subseteq A$ è non vuota.
> - Due classi di equivalenza distinte sono disgiunte (per la [proposizione](Relazioni%20tra%20insiemi.md#^proposizione-due-classi-di-equivalenza-o-sono-disgiunte-o-coincidono) precedente).
> - Per ogni $a \in A$, si ha $a \in [a]_\sim \in A/\sim$.
> 
> Viceversa, data una partizione $\mathcal{C}$ di A, la relazione $\sim$ su $A$ definita da:
> $$
> a \sim b \iff a,b \ \text{appartengono allo stesso} \ X \in \mathcal{C}
> $$
> è una [relazione di equivalenza](Relazioni%20tra%20insiemi.md#^definizione-relazione-di-equivalenza) su $A$, ovvero è riflessiva, simmetrica e
> transitiva%% DIMOSTRARE OGNI PROPRIETÀ ESPLICITAMENTE %% (se $a, b \in X \in \mathcal{C}$ e $b, c \in Y \in \mathcal{C}$, allora $X = Y$ poiché $b \in X \cap Y$ e $\mathcal{C}$ è una partizione: perciò $a, c \in X \in C$), e $A/\sim = \mathcal{C}$.
> 
> Quindi, in sostanza, si può concludere che partizioni%% Link %% su $A$ e [insiemi quozienti](Relazioni%20tra%20insiemi.md#^definizione-insieme-quoziente) di $A$ sono la stessa cosa.

%%
Su questa osservazione:
- Associare ogni punto alle relative regole della definizione di partizione
- Trasformare in proposizione

> [!esempio]- Esempio
> 
> Sia C = {P, D} la partizione di Z in numeri pari e dispari. Consideriamo la relazione di congruenza modulo 2 su Z, e sia Z2 lo spazio quoziente.
> Allora C = Z2. Infatti Z2 = {[0], [1]} e [0] = P e [1] = D.

> [!esercizio]+ Esercizio su relazioni di equivalenza 1
> 
> Consideriamo la relazione $\mathcal{R}$ sull'insieme dei numeri realiLINK $\mathbb{R}$ definita da:
> $$
> x \mathcal{R} y \iff |x| = |y|
> $$
> Dimostrare che $\mathcal{R}$ è una relazione d'equivalenza.
> 
> > [!soluzione]- Soluzione
> > 
> > Siano x, y, z elementi arbitrari di R.
> > Riflessività Ovvio, x E x perché |x| = |x|.
> > Simmetria Anche questo è facile: se x E y allora |x| = |y|, quindi anche
> > y E x perché |y| = |x|.
> > Transitività Supponiamo che x E y e y E z: vogliamo dimostrare che
> > x E z. Dalla prima condizione otteniamo |x| = |y|, mentre
> > dalla seconda |y| = |z|: quindi |x| = |y| = |z|, ovvero x E z.

> [!esercizio]+ Esercizio
> 
> Consideriamo la relazione di equivalenza E su R definita da
> x E y se e solo se |x| = |y|.
> Come sono fatte le classi di equivalenza di E?
> 
> > [!soluzione]- Soluzione
> > 
> > Sono del tipo [r]E = {r, -r} per r \in R.
> > Quanti elementi ha ciascuna di tali classi?
> > Risposta: Due elementi distinti se r̸ = 0, uno solo se r = 0.
> > Quante classi di equivalenza distinte otteniamo?
> > Risposta: Infinite, una per ogni r \ge 0.
> > Com'è fatto l'insieme quoziente R/E?
> > Risposta: R/E = {{r, -r} | r \in R}.

> [!esercizio]+ Esercizi su relazioni d'equivalenza (2)
> 
> Consideriamo la relazione E su N definita da
> 
> > n E m se e solo se n ed m hanno lo stesso numero di cifre (in notazione decimale).
> 
> Dimostrare che E è una relazione d'equivalenza.
> 
> > [!soluzione]- Soluzione
> > 
> > Siano n, m, l elementi arbitrari di N.
> > Riflessività Ovvio, n E n poiché ciascun numero si scrive con lo stesso
> > numero di cifre di sé stesso.
> > Simmetria Ovvio, se n E m vuol dire che n ha lo stesso numero di cifre
> > di m: quindi anche m E n, ovvero m ha lo stesso numero di
> > cifre di n.
> > Transitività Se n E m e, in particolare, n e m hanno entrambi k cifre, e
> > inoltre m E l, ovvero m e l hanno hanno lo stesso numero di
> > cifre, allora anche l ha k cifre, per cui n E l.

> [!esercizio]+ Esercizio
> 
> Consideriamo la relazione di equivalenza E su N definita da
> n E m se e solo se n ed m hanno lo stesso numero di cifre
> (in notazione decimale).

> [!esercizio]+ Domande e risposte:
> 
> ```latex
> \begin{itemize}
>     \item Come sono fatte le classi di equivalenza di \(E\)?\\
>     Sono del tipo \(C_k = \{n \in \mathbb{N} \mid n \text{ ha esattamente } k \text{ cifre}\}\) per \(k \in \mathbb{N} \setminus \{0\}\). Più precisamente, \(C_1 = \{0, 1, 2, 3, 4, 5, 6, 7, 8, 9\}\) e \(C_k = \{n \in \mathbb{N} \mid 10^{k-1} \leq n < 10^k\}\) se \(k \geq 2\).
>     
>     \item Quanti elementi ha ciascuna di tali classi?\\
>     \(C_k\) ha \(10\) elementi se \(k = 1\), e ne ha \(9 \cdot 10^{k-1}\) se \(k > 1\).
>     
>     \item Quante classi di equivalenza distinte otteniamo?\\
>     Infinite, una per ogni \(k \in \mathbb{N} \setminus \{0\}\).
>     
>     \item Com'è fatto l'insieme quoziente \(\mathbb{N} / E\)?\\
>     \(\mathbb{N} / E = \{C_k \mid k \in \mathbb{N} \setminus \{0\}\}\).
> \end{itemize}
> ```

> [!esercizio]+ Esercizi su relazioni d'equivalenza (3)
> 
> Sia
> Fin = {X \subseteq N | X è finito}.
> Consideriamo la relazione \approx su Fin definita da
> X \approx Y se e solo se X e Y hanno lo stesso numero di elementi.
> Dimostrare che \approx è una relazione d'equivalenza.
> 
> > [!soluzione]- Soluzione
> > 
> > Siano X, Y, Z arbitrari elementi di Fin.
> > Riflessività Ovvio, ogni X ha lo stesso numero di elementi di se stesso.
> > Simmetria Ovvio, se X \approx Y allora X e Y hanno lo stesso numero di
> > elementi, quindi anche Y \approx X.
> > Transitività Se X e Y hanno entrambi k elementi, e inoltre Y e Z hanno
> > lo stesso numero di elementi, allora anche Z ha k elementi,
> > da cui X \approx Z.

> [!esercizio]+ Domande e risposte:
> 
> ```latex
> \begin{itemize}
>     \item Come sono fatte le classi di equivalenza di \(\approx\)?\\
>     Sono del tipo \(I_k = \{X \in \mathrm{Fin} \mid X \text{ ha } k \text{ elementi}\}\) per \(k \in \mathbb{N}\). In particolare, \(I_0 = \{\emptyset\}\), \(I_1 = \{\{n\} \mid n \in \mathbb{N}\}\), \(I_2 = \{\{n, m\} \mid n, m \in \mathbb{N}, n \neq m\}\) e così via.
>     
>     \item Quanti elementi ha ciascuna di tali classi?\\
>     \(I_0\) ha un solo elemento, mentre tutte le altre classi \(I_k\) con \(k \geq 1\) ne hanno infiniti.
>     
>     \item Quante classi di equivalenza distinte otteniamo?\\
>     Infinite, una per ogni \(k \in \mathbb{N}\).
>     
>     \item Com'è fatto l'insieme quoziente \(\mathrm{Fin} / \approx\)?\\
>     \(\mathrm{Fin} / \approx = \{I_k \mid k \in \mathbb{N}\}\).
> \end{itemize}
> 
> ```

%%

# 3 - Relazioni di ordine

> [!definizione]+ Definizione: relazione di ordine
> 
> Dato un [insieme](Teoria%20degli%20insiemi.md#^definizione-insieme) $A$, una **relazione di ordine** $\le$ su $A$ (o, più semplicemente, un **ordine** o un **ordinamento** su $A$) è una [relazione](Relazioni%20tra%20insiemi.md#^definizione-relazione-n-aria) che rispetta le seguenti [proprietà](Relazioni%20tra%20insiemi.md#^definizione-proprieta-delle-relazioni-binarie):
> - **Riflessività**: $\forall a \in A (a \le a)$.
> - **Antisimmetria**: $\forall a,b \in A (a \le b \land b \le a \implies a = b)$.
> - **Transitività**: $\forall a,b,c \in A (a \le b \land b \le c \implies a \le c)$.
> 
> L'insieme $A$ è detto **_ordinato_** e, per esplicitarne la relazione di ordine $\le$ che insiste su di esso, si può scrivere come:
> $$
> (A, \le) 
> $$
^definizione-relazione-di-ordine

> [!esempio]- Esempio: ordine non-decrescente $\color{#7F7FFF} \le$ è una relazione di ordine
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

> [!notazione]+ Notazioni alternative per le relazioni di ordine
> 
> Oltre al simbolo "$\le$", spesso per denotare le [relazioni di ordine](Relazioni%20tra%20insiemi.md#^definizione-relazione-di-ordine) si usano altri simboli che in qualche misura gli somigliano, come "$\preceq$", "$\trianglelefteq$", "$\lesssim$", "$\sqsubseteq$", ecc.

%% 

> [!esempio]- Esempio
> 
> Sia A un insieme qualunque. La relazione di inclusione \subseteq è un ordine
> sull'insieme P(A) = {B | B \subseteq A}. Infatti
> Riflessività Segue dal fatto che B \subseteq B per ogni insieme B.
> Antisimmetria Segue dal principio di doppia inclusione:
> se B \subseteq C e C \subseteq B allora B = C.
> Transitività Supponiamo che B \subseteq C \subseteq D. Allora dato un qualunque
> x \in B si deve avere anche x \in C poiché B \subseteq C, quindi
> anche x \in D poiché C \subseteq D. Dunque ogni elemento di B `e
> anche un elemento di D, ovvero B \subseteq D.

%%

## 3.1 - Relazione di ordine totale

> [!definizione]+ Definizione: relazione di ordine totale
> 
> Dato un [insieme](Teoria%20degli%20insiemi.md#^definizione-insieme) $A$, una [relazione di ordine](Relazioni%20tra%20insiemi.md#^definizione-relazione-di-ordine) $\le$ su $A$ si dice **totale** (o **lineare**) se:
> $$
> \forall a,b \in A(a \le b \lor b \le a)
> $$
^definizione-relazione-di-ordine-totale

%% cioè se rispetta la proprietà di totalità %%

%%

> [!esempio]- Esempio
> 
> L'ordine $\le$ su $\mathbb{N}$, $\mathbb{Z}$, $\mathbb{Q}$ o $\mathbb{R}$ è un ordine lineare.

Come già vistoLINK, per qualunque insieme $A$ l'inclusione $\subseteq$ è un ordine su $\mathcal{P}(A) = \{B \mid B \subseteq A\}$. Tuttavia, se ad esempio $A = \{ a,b \}$, quest'ordine non è totale, poiché $\{ a \} \nsubseteq \{ b \}$ e $\{ b \} \nsubseteq \{ a \}$. (cioè se l'insieme ha solo due elementi?)

> [!esercizio]+ Esercizio
> 
> Disegnare il diagramma di Hasse degli ordini $\langle\mathcal{P}(\{0\}), \subseteq\rangle$, $\langle\mathcal{P}(\{0, 1\}), \subseteq\rangle$ e $\langle\mathcal{P}(\{0, 1, 2\}), \subseteq\rangle$. In quali casi si ha un ordine lineare?

%%

## 3.2 - Relazione di successione immediata e diagrammi di Hasse

> [!definizione]+ Definizione: relazione di successione immediata
> 
> Dato un [insieme ordinato](Relazioni%20tra%20insiemi.md#^definizione-relazione-di-ordine) $(A, \le)$, un elemento $y \in A$ è un **successore immediato** di $x \in A$ (e $x$ è un **predecessore immediato** di $y$), in simboli $x \lhd y$, se:
> $$
> x \le y \land x \ne y \land \forall z \in A (x \le z \land z \le y \implies z = x \lor z = y)
> $$
> %% cioè, se nell'ordine non ci sono elementi in mezzo ai due %%
> %% anche come b<a e ∄c(b<c<a) %%
^definizione-relazione-di-successione-immediata

%%

> [!notazione]+ Notazione: diagramma di Hasse
> 
> 
> ![](Pasted%20image%2020250106193233.png)
> 
> ![](Pasted%20image%2020250106193243.png)

le linee rosse sono per far vedere $c \preceq g$ e $b \preceq e$.

> [!osservazione]+ Osservazione: il diagramma di Hasse in un ordine NON è unico!
> 
> ![](Pasted%20image%2020250106193308.png)

> [!esempio]- Esempio
> 
> ![](Pasted%20image%2020250203163701.png)
> cioè ogni elemento è divisibile per gli elementi che gli stanno "sotto".

%%

%% 

> [!osservazione]+ Perché si usano i diagrammi di Hasse (AGGIUNGERE LA PAGINA WIKIPEDIA DEI DIAGRAMMI DI HASSE COME FONTE)
> 
> Se si prova a creare una rappresentazione visuale di un insieme parzialmente ordinato (_S_, \le) si può procedere in vari modi. Si potrebbe cominciare creando un [grafo](https://it.wikipedia.org/wiki/Grafo "Grafo") dove ogni nodo del grafo è un elemento in _S_ e ogni arco (_u_, _v_) nel grafo rappresenta la relazione _u_ \le _v_.
> 
> Procedendo in questo modo quando si prova a disegnare il grafo si noterà che la rappresentazione risultante è molto "affollata", in effetti questa rappresentazione si porta dietro molte ridondanze. Si richiamano le proprietà di un ordinamento parziale:
> 
> - _a_ \le _a_ (riflessività)
> - se _a_ \le _b_ e _b_ \le _c_ allora _a_ \le _c_ (transitività)
> - se _a_ \le _b_ e _b_ \le _a_ allora _a_ = _b_ (antisimmetricità)
> 
> Nel grafo originale si ha una quantità di archi - cicli su ogni nodo del grafo - nella forma (_u_, _u_) poiché la proprietà riflessiva significa che _u_ \le _u_. Questo è vero per ogni elemento in _S_ altrimenti non sarebbe un ordinamento parziale.
> 
> Si può provare a creare il grafo come sopra ma eliminando i cicli dell'insieme parzialmente ordinato ({1,2,3,4}, \le) dove un [partizione](https://it.wikipedia.org/wiki/Partizione_\(teoria_degli_insiemi\) "Partizione (teoria degli insiemi)") più piccola è minore di una partizione più grande. Si otterrà quindi il seguente grafo:

%%

## 3.3 - Massimi e minimi di un ordine

> [!definizione]+ Definizione: massimo e minimo di un ordine
> 
> Dato un [insieme ordinato](Relazioni%20tra%20insiemi.md#^definizione-relazione-di-ordine) $(A, \le)$, un elemento $a \in A$ si dice:
> - **Massimo** (rispetto a $\le$) se $\forall b \in A (b \le a)$.
> - **Minimo** (rispetto a $\le$) se $\forall b \in A (a \le b)$.
^definizione-massimo-e-minimo-di-un-ordine

> [!esempio]- Esempi
> 
> L'ordine $\le$ su $\mathbb{N}$ ha minimo (il numero $0$), ma non ha massimo.
> L'ordine $\le$ su $\mathbb{Z}$ non ha né minimo, né massimo.
> L'ordine $\le$ sull'intervallo $(0; 1] := \{x \in R \mid 0 < x \le 1\}$ ha massimo (il numero $1$) ma non ha minimo.
> L'ordine $\subseteq$ su $\mathcal{P}(A)$ ha minimo (l'insieme $\emptyset$) e massimo (l'insieme $A$), poiché $\emptyset \subseteq B \subseteq A$ per ogni $B \subseteq A$.

%%

> [!esempio]- Esempio: la relazione di divisibilità fra numeri naturali
> 
> Definiamo una [relazione binaria](Relazioni%20tra%20insiemi.md#^definizione-relazione-n-aria) "$|$" su $\mathbb{N}$ come:
> $$
> n|m \iff \exists k \in \mathbb{N}(m = n \cdot k)
> $$
> Dimostrare che $|$ è un ordine non totale su $\mathbb{N}$ che ha minimo e massimo.
> 
> Dimostrazione:
> Siano n, m, l \in N arbitrari.
> 
> Riflessività n ⪯ n poiché n = n \cdot 1.
> 
> Antisimmetria Supponiamo che n ⪯ m e m ⪯ n. Allora esiste i \in N tale che
> m = n \cdot i ed esiste j \in N tale che n = m \cdot j. Se m = 0 allora
> n = 0 \cdot j = 0, quindi m = n. Altrimenti per sostituzione si ha
> m = m \cdot j \cdot i, da cui, dividendo per m, si ottiene j \cdot i = 1. Perci`o
> j = i = 1, da cui m = n \cdot 1 = n.
> 
> Transitività Supponiamo che n ⪯ m e m ⪯ l. Siano i, j \in N tali che l = m \cdot i
> e m = n \cdot j. Allora l = n \cdot j \cdot i, ovvero n ⪯ l.
> 
> Non totale Ad esempio, 2̸ ⪯ 3 e 3̸ ⪯ 2.
> 
> Minimo È il numero 1: si ha sempre 1 ⪯ n poiché n = 1 \cdot n.
> Massimo È il numero 0: si ha sempre n ⪯ 0 perché 0 = n \cdot 0.
> 
> La relazione di divisibilità spesso si denota con il simbolo $|$:
> $$
> n | m \iff n \bmod m = 0
> $$
> 
> ovvero $m = n \cdot k$ per qualche $k \in \mathbb{N}$.
> Dato $m \in \mathbb{N}$, l'insieme dei divisori di $m$ è:
> $$
> Div(m) = \{n \in \mathbb{N} \mid n|m \}
> $$
> Si osservi che, per ogni $m \in \mathbb{N}$, $Div(m) \ne \emptyset$ poiché, ad esempio, $1$ ed $m$ vi appartengono.
> Se $m \ne 0$, l'insieme $Div(m)$ è un insieme finito e contiene solo numeri compresi tra $1$ ed $m$. Invece $Div(0) = \mathbb{N}$.
 
> [!esercizio]+ Esercizio 2
> 
> Calcolare il diagramma di Hasse dei seguenti ordini: $\langle Div(6), |\rangle$, $\langle Div(8), |\rangle$, $\langle Div(9), |\rangle$, $\langle Div(12), |\rangle$ e $\langle Div(30), |\rangle$. Quali di questi sono ordini lineari?

> [!esercizio]+ Esercizio su ordini
> 
> Definiamo $\trianglelefteq$ su $\mathbb{N} \setminus \{ 0 \}$ ponendo:
> $$
> n \trianglelefteq m \iff \exists k \in \mathbb{N}(m = n \cdot k)
> $$
> Dimostrare che $\trianglelefteq$ è un ordine non lineare che ha massimo ma non ha minimo.
> 
> > [!soluzione]- Soluzione
> > 
> > Siano $n, m, l \in \mathbb{N} \setminus \{ 0 \}$ arbitrari.
> > Sono rispettate le proprietà:
> > - Riflessività: $n \trianglelefteq n$ poiché $n = n \cdot 1$
> > - Antisimmetria: supponiamo che $n \trianglelefteq m$ e $m \trianglelefteq n$. Allora esistono $i, j \in \mathbb{N}$ tali che $m = n \cdot i$ e $n = m \cdot j$. Quindi $m = (m \cdot j )i = m \cdot j \cdot i$, da cui o $m = 1$ oppure $j \cdot i = 1$. Nel primo caso, $n = m \cdot j = 1 \cdot j = 1$, da cui $m = n$. Nel secondo caso $j = i = 1$, da cui $m = n \cdot i = n \cdot 1 = n$.
> > - Transitività: supponiamo che $n \trianglelefteq m$ e $m \trianglelefteq l$. Siano i, j \in N tali che l = mi e
> > m = nj . Allora l = (nj )i = nj\cdoti, ovvero n ⊴ l.
> > Non lineare Ad esempio, \lnot(2 ⊴ 3) e \lnot(3 ⊴ 2).
> > Minimo Non esiste, perché non esiste alcun n tale che n ⊴ 2 e n ⊴ 3.
> > Massimo È il numero 1: si ha sempre n0 = 1, perciò n ⊴ 1.

%%

## 3.4 - Relazione di ordine stretto

> [!definizione]+ Definizione: relazione di ordine stretto
> 
> Dato un [insieme](Teoria%20degli%20insiemi.md#^definizione-insieme) $A$, una [relazione binaria](Relazioni%20tra%20insiemi.md#^definizione-relazione-n-aria) $<$ su $A$ si dice **stretta** se rispetta le seguenti [proprietà](Relazioni%20tra%20insiemi.md#^definizione-proprieta-delle-relazioni-binarie):
> - **Irriflessività**: $\forall a \in A (\lnot(a < a ))$.
> - **Transitività**: $\forall a,b,c \in A (a < b \land b < c \implies a < c)$.
^definizione-relazione-di-ordine-stretto

%%

> [!esempio]- Esempio
> 
> - La relazione < su N o su R
> - L'inclusione stretta $\subsetneq$ su $\mathcal{P}(A)$

> [!notazione]+ Notazione
>  
> Per indicare gli ordini stretti spesso si usano i simboli per gli ordini senza la
> parte che richiama l'uguaglianza, ad esempio
> < ≺ ◁ ⊏ \ldots
> 
> Scriveremo ad esempio \langleA, ≺\rangle per indicare che ≺ è definito su A.

Vedremo a breve che un ordine stretto è esattamente la parte stretta di un ordine (che minghie significa?).

> [!esempio]- Esempio: discendenti e antenati
> 
> Sia A l'insieme di tutti gli esseri umani. Definiamo la relazione ◁ su A ponendo
> a ◁ b se e solo se a è un/una discendente di b.
> (Equivalentemente, a ◁ b se e solo se b è un/una antenato/a di a.)
> La relazione ◁ è chiaramente irriflessiva, perché nessuno è discendente di se stesso.
> Inoltre, se a è un discendente di b e b è un discendente di c, allora anche a è un discendente di c: quindi ◁ è transitiva.
> Questo mostra che ◁ è un ordine stretto.

> [!proposizione]+ Proposizione: relazione tra ordini stretti e ordini
> 
> Dato un qualunque ordine ⪯ su un insieme A, possiamo considerare la sua parte stretta ≺ definita da
> a ≺ b se e solo se a ⪯ b \land a̸ = b.
> Si verifica facilmente che ≺ è ancora una relazione transitiva.
> 
> > [!dimostrazione]- Dimostrazione
> > 
> > (Supponiamo a ≺ b ≺ c. Allora a ⪯ c per la transitività di ⪯. Se per assurdo a = c, allora si avrebbe a ⪯ b e b ⪯ c = a, quindi a = b per l'antisimmetria di ⪯, assurdo. Segue che a̸ = c, e quindi a ≺ c.)
> > Inoltre ≺ è irriflessiva: per definizione non c'è nessun elemento a \in A per cui valga a ≺ a.
> > Questo mostra che, in accordo con la terminologia usata, la parte stretta di un ordine è sempre un ordine stretto.
> > 
> > Viceversa, dato un ordine stretto ≺ su A possiamo canonicamente costruire la relazione binaria ⪯ su A definita da
> > a ⪯ b se e solo se (a ≺ b \lor a = b).
> > Si verifica facilmente che ⪯ è un ordine:
> > Riflessività Immediato dalla definizione: a ⪯ a poiché ovviamente a = a.
> > Antisimmetria Supponiamo per assurdo che ci siano a̸ = b tali che a ⪯ b e b ⪯ a. Allora per definizione di ⪯ si deve avere a ≺ b e b ≺ a (poiché abbiamo assunto a̸ = b). Usando la transitività di ≺ concludiamo che a ≺ a, in contraddizione con l'irriflessività di ≺.
> > Transitività Supponiamo che a ⪯ b e b ⪯ c. Se a = b oppure b = c allora banalmente a ⪯ c. Possiamo quindi assumere che a, b e c siano distinti. Per definizione di ⪯ si ha allora a ≺ b e b ≺ c, da cui a ≺ c per transitività di ≺. Segue che a ⪯ c.
> > 
> > Dunque ogni ordine stretto è necessariamente la parte stretta di un ordine.

%%

## 3.5 - Relazione di pre-ordine

> [!definizione]+ Definizione: relazione di pre-ordine
> 
> Dato un [insieme](Teoria%20degli%20insiemi.md#^definizione-insieme) $A$, una **relazione di pre-ordine** $\precsim$ su $A$ (o **relazione di quasi-ordine**) è una [relazione](Relazioni%20tra%20insiemi.md#^definizione-relazione-n-aria) che rispetta le seguenti [proprietà](Relazioni%20tra%20insiemi.md#^definizione-proprieta-delle-relazioni-binarie):
> - **Riflessività**: $\forall a \in A (a \precsim a)$.
> - **Transitività**: $\forall a,b,c \in A (a \precsim b \land b \precsim c \implies a \precsim c)$.
> 
> L'insieme $A$ è detto **_parzialmente ordinato_** e, per esplicitarne la relazione di ordine $\precsim$ che insiste su di esso, si può scrivere come:
> $$
> (A, \precsim) 
> $$
^definizione-relazione-di-pre-ordine

%% 

> [!esempio]- Esempio: la classifica del campionato di serie A è un pre-ordine \precsim (lineare)
> 
> la classifica del campionato di serie A è un pre-ordine \precsim (lineare) sull'insieme delle squadre X: se la squadra S ha n punti e la squadra T ha
> m punti, diciamo che S \precsim T ("S precede T nella classifica") se e solo se
> n \ge m. Si verifica allora che la relazione \precsim `e:
> riflessiva: S \precsim S per ogni S \in X;
> transitiva: per ogni S, T, U \in X, se S \precsim T e T \precsim U allora S \precsim U ;
> ma non è antisimmetrica: può accadere che S \precsim T e T \precsim S per due squadre distinte S, T \in X (S e T sono a pari merito).
> Dunque si tratta di un pre-ordine e non di un ordine.

> [!proposizione]+ Proposizione
> 
> Se \precsim è un pre-ordine su A, allora
> a \sim b \iff a \precsim b \land b \precsim a
> è una relazione di equivalenza su A (detta relazione di equivalenza
> indotta da \precsim) e la relazione su A/\sim
> [a]\sim \le [b]\sim \iff a \precsim b
> è ben definita ed è un ordine (detto ordine indotto da \precsim).
> 
> > [!esempio]- Esempio
> > 
> > Ad esempio, nella classifica del campionato di serie A (vista come
> > pre-ordine \precsim), le classi di equivalenza rispetto alla relazione \sim indotta da
> > \precsim sono gli insiemi di squadre a parimerito (cioè con lo stesso numero di
> > punti). L'ordine \le indotto su tali classi di equivalenza è quella che ordina
> > questi gruppi di squadre in base al punteggio ottenuto: l'insieme delle
> > squadre che hanno 20 punti formano una classe di equivalenza che precede
> > la classe di equivalenza delle squadre che hanno 19 punti, e così via.
> 
> > [!dimostrazione]- Dimostrazione
> > 
> > Dimostrazione di "La relazione \sim definita da $a \sim b \iff a \precsim b \land b \precsim a$ è una relazione d'equivalenza":
> > Dimostrazione.
> > È evidentemente riflessiva, dato che lo è \precsim.
> > Se a \sim b allora a \precsim b \land b \precsim a e quindi b \precsim a \land a \precsim b, cioè b \sim a; quindi \sim
> > è simmetrica.
> > Se a \sim b e b \sim c, allora a \precsim b \land b \precsim a e b \precsim c \land c \precsim b, da cui per
> > transitività di \precsim si ha a \precsim c \land c \precsim a, cioè a \sim c
> > $\blacksquare$
> 
> > [!dimostrazione]- Dimostrazione di "La relazione su $A/\sim$ data da $[a]_\sim \le [b]_\sim \iff a \precsim b$ è ben definita ed è un ordine.":
> > Dimostrazione.
> > Supponiamo che a \precsim b e a' \sim a e b' \sim b: allora a' \precsim a e b \precsim b' quindi
> > a' \precsim b' per la transitività di \precsim. Ne segue che la definizione di \le su A/\sim `e
> > ben posta, dato che non dipende dal rappresentante.
> > È immediato verificare che \le è riflessiva e transitiva, quindi è sufficiente
> > verificare che è antisimmetrica. Se [a]\sim \le [b]\sim e [b]\sim \le [a]\sim, allora
> > a \precsim b \land b \precsim a, da cui a \sim b per definizione, e quindi [a]\sim = [b]\sim.

> [!esempio]- Esempio di pre-ordine: conseguenza logica
> 
> La relazione di conseguenza logica \vDash sull'insieme di tutte le proposizioni è un pre-ordine (ma non un ordine).
> Riflessivit`a: Chiaramente P \vDash P per ogni proposizione P, quindi \vDash `e
> riflessiva.
> Transivit`a: Assumiamo che P \vDash Q e Q \vDash R e dimostriamo che P \vDash R.
> Costruiamo la tavola di verità di P, Q, R su tutte le variabili proposizionali
> che compaiono in P o in Q o in R. Si ha che in ogni riga in cui P è vera
> anche Q risulta vera (poiché P \vDash Q), e che in ogni riga in cui Q è vera
> anche R risulta vera (poiché Q \vDash R). Quindi in ogni riga in cui P è vera
> risulterà vera anche R, cioè P \vDash R.
> Tuttavia, la relazione \vDash non è un ordine. Infatti, A \to B \vDash \lnotA \lor B e
> \lnotA \lor B \vDash A \to B ma le due proposizioni sono distinte: quindi \vDash non `e
> antisimmetrica. Le relazione d'equivalenza associata a \vDash è proprio la
> relazione di equivalenza logica \equiv

> [!esempio]- Esempio di pre-ordine che non è un ordine
> 
> Consideriamo la relazione ⪯ su N definita da
> n ⪯ m se e solo se m ha un numero di cifre maggiore o uguale
> a quelle di n (in notazione decimale).
> Allora ⪯ è una relazione riflessiva e transitiva, ma non è antisimmetrica
> poich´e, ad esempio, 10 ⪯ 25 e 25 ⪯ 10 (ma 10̸ = 25). Quindi ⪯ è un
> esempio di un pre-ordine che non è un ordine.
> La relazione di equivalenza associata a ⪯ è la relazione E ("avere lo stesso
> numero di cifre") della slide 48 . L'ordine indotto sul quoziente N/E rispetto
> a tale relazione d'equivalenza è un ordine lineare: Ck precede Ck' in tale
> ordine se e solo se k \le k', dove le Ck sono le classi di equivalenza rispetto
> ad E definite nella slide 49 .

> [!esempio]- Esempio di pre-ordine (3)
> 
> Consideriamo la relazione \precsim su Fin = {X \subseteq N | X è finito} definita da
> X \precsim Y se e solo se il numero di elementi di X è minore o uguale
> al numero di elementi di Y .
> La relazione \precsim è chiaramente riflessiva e transitiva, ma non `e
> antisimmetrica poich´e, ad esempio, {1, 2} \precsim {5, 14} e {5, 14} \precsim {1, 2},
> ma chiaramente {1, 2}̸ = {5, 14}. Quindi \precsim è un altro esempio di un
> pre-ordine che non è un ordine.
> La relazione di equivalenza associata a \precsim è la relazione \approx ("avere lo stesso
> numero di elementi") della slide 50 . Anche in questo caso, l'ordine indotto
> sul quoziente Fin/\approx rispetto a tale relazione d'equivalenza è un ordine
> lineare: Ik precede Ik' in tale ordine se e solo se k \le k', dove le Ik sono le
> classi di equivalenza rispetto a \approx definite nella slide 51 .

> [!esempio]- Esempio di pre-ordine (4)
> 
> Sia \subseteq∗ la relazione su P(N) definita per ogni A, B \subseteq N da
> A \subseteq∗ B se e solo se A \ B è finito.
> In altre parole, A \subseteq∗ B se e solo se ogni n \in A appartiene anche a B
> tranne che per un numero finito di tali n.
> Dimostrare che \subseteq∗ è un pre-ordine su P(N).
> Riflessivit`a: A \subseteq∗ A poiché A \ A = \emptyset è finito.
> Transitivit`a: Siano A \subseteq∗ B \subseteq∗ C. Si ha
> A \ C \subseteq (A \ B) \cup (B \ C).
> Infatti, sia n \in A \ C, ovvero n \in A ma n /\in C. Distinguiamo due casi. Se
> n /\in B, allora n \in A \ B e quindi n \in (A \ B) \cup (B \ C). Se invece n \in B,
> allora n \in B \ C e quindi nuovamente n \in (A \ B) \cup (B \ C). Poich´e
> A \ B e B \ C sono finiti, anche A \ C lo `e, ovvero A \subseteq∗ C.
> Per definizione, la relazione di equivalenza =∗ indotta da \subseteq∗ è data da
> A =∗ B se e solo se A \subseteq∗ B e B \subseteq∗ A.
> È facile vedere che A =∗ B se e solo se A △ B è finito e che ogni classe di
> equivalenza rispetto alla relazione =∗ è infinita.
> Poiché A △ B := (A \ B) \cup (B \ A), si ha che A △ B è finito se e solo se
> entrambi gli insiemi A \ B e B \ A sono finiti, ovvero se e solo se A \subseteq∗ B
> e B \subseteq∗ A.
> Sia A \subseteq N. Se A è finito, allora per ogni insieme finito B \subseteq N si ha che
> A △ B è finito poiché A △ B \subseteq A \cup B, per cui A =∗ B. Poiché la
> collezione dei sottoinsiemi di N finiti contiene infiniti elementi (ad esempio,
> contiene tutti gli {n} per n \in N), si ha che [A]=∗ è infinita. Se invece
> A = {a0, a1, a2, \ldots} è infinito, allora posto An = A \ {an} per ogni n \in N
> si ha che gli An sono a due a due distinti e tali che An =∗ A (infatti
> A △ An = {an}). Quindi anche in questo caso [A]=∗ è infinita.

> [!esercizio]+ Esercizio
> 
> Siano R e S relazioni su un insieme A, che ha almeno 3 elementi. Stabilire se ciascuna delle seguenti affermazioni è vera o è falsa:
> 1.  Se R e S sono simmetriche, allora R \cap S è simmetrica.
> VERO:
> $$
> (x, y) \in R \cap S \to (x, y) \in R \land (x, y) \in S \to (y, x) \in R \land (y, x) \in S \to (y, x) \in R \cap S
> $$
> 2. Se R e S sono simmetriche, allora R \cup S è simmetrica.
> VERO
> $$
> (x, y) \in R \cup S \to (x, y) \in R \lor (x, y) \in S \to (y, x) \in R \lor (y, x) \in S \to (y, x) \in R \cup S
> $$
> 3. Se R e S sono transitive, allora R \cap S è transitiva.
> VERO:
> $$
> (x, y), (y, z) \in R \cap S \to (x, y), (y, z) \in R \land (x, y), (y, z) \in S \to (x, z) \in R \land (x, z) \in S \to (x, z) \in R \cap S
> $$
> 4.  Se R e S sono transitive, allora R \cup S è transitiva.
> FALSO:
> Posto A = {1, 2, 3}, le relazioni R = {(1, 2)} e S = {(2, 3)} sono
> transitive, (1, 2), (2, 3) \in R \cup S ma (1, 3) /\in R \cup S
> 5. Se R è antisimmetrica e S arbitraria, allora R \cap S è antisimmetrica.
> VERO:
> Supponiamo (x, y), (y, x) \in R \cap S, allora (x, y), (y, x) \in R e quindi x = y.
> 6. Se R e S sono antisimmetriche, allora R \cup S è antisimmetrica.
> FALSO;
> Posto A = {1, 2, 3}, le relazioni R = {(1, 2)} e S = {(2, 1)} sono
> antisimmetriche, (1, 2), (2, 1) \in R \cup S ma 1̸ = 2.

%%

### 3.5.1 - Maggioranti e minoranti in una relazione di pre-ordine

> [!definizione]+ Definizione: maggiorante, minorante, estremo superiore ed estremo inferiore
> 
> Dato un [insieme parzialmente ordinato](Relazioni%20tra%20insiemi.md#^definizione-relazione-di-pre-ordine) $(A, \precsim)$ e un sottoinsieme $X \subseteq A$:
> - Un **maggiorante** di $X$ è un elemento $a \in A$ tale che $\forall x \in X (x \precsim a)$.
> - Un **minorante** di $X$ è un elemento $a \in A$ tale che $\forall x \in X (a \precsim x)$.
> - Un **estremo superiore** di $X$, denotato con "$\sup X$", è un elemento $a \in A$ che è maggiorante di $X$ e tale che, per ogni $b \in A$, se $b$ è un maggiorante di $X$, allora $a \precsim b$.
> - Un **estremo inferiore** di $X$, denotato con "$\inf X$", è un elemento $a \in A$ che è minorante di $X$ e tale che, per ogni $b \in A$, se $b$ è un minorante di $X$, allora $b \precsim a$.
^definizione-maggiorante-minorante-estremo-superiore-ed-estremo-inferiore

%% 

> [!osservazione]+ Osservazione
> 
> Non è detto che un insieme X abbia un estremo superiore o inferiore,
> anche se X è finito.
 
> [!proposizione]+ Proposizione: unicità dell'estremo superiore e inferiore
> 
> Sia (A, \precsim) un insieme parzialmente ordinato e sia X \subseteq A.
> L'estremo superiore di X, se esiste, è unico.
> L'estremo inferiore di X, se esiste, è unico.
> 
> > [!dimostrazione]- Dimostrazione
> > 
> > Se a1, a2 sono due estremi superiori di X, allora a1 \precsim a2 e a2 \precsim a1, quindi
> > il risultato segue dalla proprietà antisimmetrica.
> > Il caso dell'estremo inferiore è simile.

%%

### 3.5.2 - Massimi e minimi di un pre-ordine

> [!definizione]+ Definizione: massimo e minimo di un pre-ordine
> 
> Dato un [insieme parzialmente ordinato](Relazioni%20tra%20insiemi.md#^definizione-relazione-di-pre-ordine) $(A, \precsim)$, un elemento $a \in A$ si dice:
> - **Massimo** (rispetto a $\precsim$) se $\forall b \in A (b \precsim a)$.
> - **Minimo** (rispetto a $\precsim$) se $\forall b \in A (a \precsim b)$.
^definizione-massimo-e-minimo-di-un-pre-ordine

%%

> [!osservazione]+ Unicità di massimo e minimo di un pre-ordine
> 
> Come nel caso dell'estremo superiore/inferiore, il massimo ed il minimo, se
> esistono, sono unici e li si indicano con max X e min X.
> (stessa cosa anche per massimi e minimi di un ordine)

> [!osservazione]+ Quindi
> 
> sup X = min{y \in A | \forall x \in X (x \le y)} è il minimo dei maggioranti di X.
> inf X = max{y \in A | \forall x \in X (y \le x)} è il massimo dei minoranti di X.
> Se max X esiste, allora coincide con sup X.
> Se sup X esiste ed appartiene ad X, allora sup(X) = max(X).
> Se min X esiste, allora coincide con inf X.
> Se inf X esiste ed appartiene ad X, allora inf(X) = min(X).

> [!esempio]- Esempio
> 
> Se X = {a}, allora sup X = inf X = max X = min X = a.

> [!esempio]- Esempio
> 
> ![](Pasted%20image%2020250110104126.png)
> 
> Se X = {a, b} allora sup X non esiste, inf X = c e min X non esiste.

> [!esercizio]+ Esercizio
> 
> Per ciascun ordine parziale stabilire se esiste il massimo e il minimo. Per
> ogni sottoinsieme non vuoto X, di ciascuno di essi stabilire se esistono
> sup X e inf X.
> ![](Pasted%20image%2020250110104154.png)

%%

# 4 - Reticoli

> [!definizione]+ Definizione: reticolo
> 
> Un **reticolo** è un [insieme parzialmente ordinato](Relazioni%20tra%20insiemi.md#^definizione-relazione-di-pre-ordine) non vuoto $(R, \precsim)$ in cui, per ogni coppia di elementi $x,y \in R$, esistono un [estremo superiore](Relazioni%20tra%20insiemi.md#^definizione-maggiorante-minorante-estremo-superiore-ed-estremo-inferiore) $\sup \{ x,y \}$ e un [estremo inferiore](Relazioni%20tra%20insiemi.md#^definizione-maggiorante-minorante-estremo-superiore-ed-estremo-inferiore) $\inf \{ x,y \}$.
^definizione-reticolo

%%

> [!osservazione]+ Osservazione
> 
> Quindi (R, \le) è un reticolo se per ogni x, y \in R esistono due elementi \sup \{ x,y \} e \inf \{ x,y \} tali che
> - $x \precsim \sup \{ x,y \}$ e $y \precsim \sup \{ x,y \}$
> - $\inf \{ x,y \} \precsim x$ e $\inf \{ x,y \} \precsim y$,
> - $\forall z \in L (x \precsim z \land y \precsim z \to \sup \{ x,y \} \precsim z)$,
> - $\forall z \in L (z \precsim x \land z \precsim y \to z \precsim \inf \{ x,y \})$.

> [!esempio]- Esempi
> 
> - Ogni ordine lineare è un reticolo: x \lor y = max{x, y} e x \land y = min{x, y}.
> - (P(A), \subseteq) è un reticolo: X \land Y = X \cap Y e X \lor Y = X \cup Y .
> - Sia \mathcal{F} = {f | f : \mathbb{N} \to \mathbb{N}} e poniamo f \precsim g se e solo se \foralln \in N (f (n) \le g(n)).
> È facile verificare che (F, ⪯) è un ordine parziale.
> In effetti è un reticolo: f \land g, f \lor g : N \to N sono definite da
> (f \land g)(n) = min{f (n), g(n)} e (f \lor g)(n) = max{f (n), g(n)}.
> - Sia | la relazione di divisibilit`a. (N, |) è un reticolo: n \lor m è il minimo
> comune multiplo e n \land m è il massimo comun divisore.
> - Sia \mathcal{I} := {X \subseteq N | X è infinito}. L'insieme ordinato (I, \subseteq) non è un
> reticolo.
> Infatti {2n | n \in N}, {2n + 1 | n \in N} \in I e tuttavia non esiste
> nessun insieme infinito X che sia contenuto nei pari e nei dispari.

sostituire $\precsim$ con $\lesssim$ per il pre-ordine?

> [!esercizio]+ Esercizio
> 
> Quali dei seguenti ordini sono reticoli?
> 
> ![](Pasted%20image%2020250110105307.png)

> [!proposizione]+ Proposizione
> 
> In un reticolo (R, \le) valgono le seguenti proprietà, per ogni x, y, z:
> 1. $\sup \{ x, y \} = \sup \{ y,x \}$ e $\inf \{ x, y \} = \inf \{ y,x \}$ (commutativa)
> 2. $\sup \{ x, \sup \{ y,z \} \} = \sup \{ \sup \{ x, y \}, z \}$ e $\inf \{ x, \inf \{ y,z \} \} = \inf \{ \inf \{ x, y \}, z \}$ (associativa)
> 3. $\sup \{ x, \inf \{ x,y \} \} = x$ e $\inf \{ x, \sup \{ x,y \} \} = x$.
> 
> > [!dimostrazione]- Dimostrazione
> > 
> > 1 è ovvia.
> > 2 $\sup \{ x, \sup \{ y,z \} \}$ è $\precsim$ di $x$ e di $\sup \{ y,z \}$, che a sua volta è $\precsim$ di $y$ e di $z$, quindi $\sup \{ x, \sup \{ y,z \} \} \precsim x, y, z$. Quindi $\sup \{ x, \sup \{ y,z \} \}$ è $\precsim$ di $\sup \{ x, y \}$ e di $z$, e quindi $\sup \{ x, \sup \{ y,z \} \} = \sup \{ \sup \{ x, y \}, z \}$.
> > Analogamente $\inf \{ x, \inf \{ y,z \} \} = \inf \{ \inf \{ x, y \}, z \}$. L'associatività di $\inf$ è simile ed è lasciata per esercizio.
> > 3 $x$ è $\precsim$ di $x$ e di $\inf \{ x,y \}$ quindi $x \precsim \sup \{ x, \inf \{ x,y \} \}$. Viceversa $\sup \{ x, \inf \{ x,y \} \} \precsim x$.
> > La dimostrazione di $\inf \{ x, \sup \{ x,y \} \} = x$ è simile.

%%

## 4.1 - Algebra reticolare

> [!definizione]+ Definizione: algebra reticolare
> 
> Un'**algebra reticolare** è un [insieme](Teoria%20degli%20insiemi.md#^definizione-insieme) $R$ dotato di due operazioni binarie%% link %% $\lor$ e $\land$ per cui valgano le seguenti proprietà:
> - $\forall x, y (x \land y = y \land x)$ e $\forall x, y (x \lor y = y \lor x)$.
> - $\forall x, y, z (x \land (y \land z) = (x \land y) \land z)$ e $\forall x, y, z (x \lor (y \lor z) = (x \lor y) \lor z)$.
> - $\forall x, y((x \lor y) \land y = y)$ e $\forall x, y((x \land y) \lor y = y)$%%(leggi di assorbimento)%%.
^definizione-algebra-reticolare

%%

> [!osservazione]+ Ogni reticolo definisce un'algebra reticolare
> 
> Per quanto visto, ogni reticolo (R, \le) definisce un'algebra reticolare (R, \lor, \land).

> [!proposizione]+ Proposizione: proprietà dell'algebra reticolare
> 
> Sia (R, \lor, \land) un'algebra reticolare. Allora valgono le seguenti proprietà:
> 1. $\forall x(x = x \lor x)$ e $\forall x(x = x \land x)$ (legge di idempotenza),
> 2. $\forall x, y (x \lor y = y \iff x \land y = x)$.
> 
> > [!dimostrazione]- Dimostrazione
> > 
> > 1. Posto x = y nella legge di assorbimento, x = (x \lor x) \land x; per commutatività $x = x \land (x \lor x)$.
> > Quindi $x \lor x = x \lor (x \land (x \lor x)) = (x \land (x \lor x)) \lor x = ((x \lor x) \land x) \lor x$, per commutatività. Sostituendo $x \lor x$ e $x$ al posto di $x$ e $y$ nella legge di assorbimento, $((x \lor x) \land x) \lor x = x$. Quindi $x \lor x = x$.
> > Analogamente $x \land x = x \land (x \lor (x \land x)) = x$.
> > 2. Se $x \lor y = y$ allora $x = (x \lor y) \land x = x \land y$ per assorbimento e commutatività.
> > Se $x \land y = x$ allora $x \lor y = (x \land y) \lor y = y$ per assorbimento e commutatività.

> [!proposizione]+ Proposizione: algebra reticolare -> relazione binaria
> 
> Data un'algebra reticolare (R, \lor, \land) , definiamo la relazione binaria \le su
> R come
> a \le b \iff a \lor b = b \iff a \land b = a.
> Allora (L, \le) è un reticolo e sup {x, y} = x \lor y e inf {x, y} = x \land y.
> 
> > [!dimostrazione]- Dimostrazione
> > 
> > Per idempotenza x \le x. Supponiamo che x \le y e y \le x, cioè x \land y = x e
> > y \lor x = x: allora x = x \land y = (y \lor x) \land y = y per assorbimento. Infine
> > supponiamo x \le y e y \le z, cioè x = x \land y e y = y \land z: allora
> > x \land z = (x \land y) \land z = x \land (y \land z) = x \land y = x.
> > Ne segue che (R, \le) è un insieme parzialmente ordinato.
> > Per assorbimento e commutatività (x \land y) \lor x = x e (x \land y) \lor y = y, cio`e
> > x \land y \le x, y. Se z \le x, y, cioè z \land x = z e z \land y = z, allora
> > z \land (x \land y) = (z \land x) \land y = z \land y = z, cioè z \le x \land y.
> > Quindi inf {x, y} = x \land y. Analogamente x \lor y = sup {x, y}.

> [!notazione]+ Notazione: algebra reticolare e reticolo stessa cosa
> 
> Siano
> $$
> \mathcal{Ret} = \{ (R, \le) \mid (R, \le) \text{ è un reticolo} \}
> $$
> la [famiglia](Teoria%20degli%20insiemi.md#^definizione-famiglia-di-insiemi) di tutti i [reticoli](Relazioni%20tra%20insiemi.md#^definizione-reticolo) e
> $$
> \mathcal{AlgRet} = \{ (R, \land, \lor) \mid (R, \land, \lor) \text{ è un'algebra reticolare} \}
> $$
> la [famiglia](Teoria%20degli%20insiemi.md#^definizione-famiglia-di-insiemi) di tutte le [algebre reticolari](Relazioni%20tra%20insiemi.md#^definizione-algebra-reticolare).
> 
> Abbiamo dimostrato che le trasformazioni
> Ret \to AlgRet (R, \le) 7 \to (R, \land, \lor)
> AlgRet \to Ret (R, \land, \lor) 7 \to (R, \le)
> sono l'una l'inversa dell'altra, quindi non distingueremo più tra la nozione
> d'ordine (reticolo) e quella algebrica (algebra reticolare) e parleremo
> semplicemente di reticoli.

%%

# 5 - Grafi

> [!definizione]+ Definizione: grafo
> 
> Un **grafo** è una [coppia ordinata](Teoria%20degli%20insiemi.md#^definizione-tupla) $(V,E)$ dove:
> - $V$: è un [insieme](Teoria%20degli%20insiemi.md#^definizione-insieme) non vuoto i cui elementi sono detti **_vertici_**.
> - $E$: è una [relazione binaria](Relazioni%20tra%20insiemi.md#^definizione-relazione-n-aria) su $V$ che è simmetrica e irriflessiva%% link %%, cioè $\forall v \in V (\lnot (v E v))$.
> 
> Se due vertici $v,w \in V$ soddisfano la relazione binaria $v E w$, essi si dicono **_adiacenti_**.
^definizione-grafo

%%

> [!notazione]+ Notazione: disegnare un grafo
> 
> E possibile rappresentare un grafo (V, E) disegnando i vertici di V sul piano e unendo due
> vertici con una linea se e solo se sono in relazione E. Per esempio se V = {a, b, c, d, e} ed
> E = {(a, c), (c, a), (a, d), (d, a), (a, e), (e, a), (c, d), (d, c)}, allora:
> ![](Pasted%20image%2020250111175512.png)

> [!osservazione]+ Osservazione: $\color{#7F7F7F} E$ come famiglia di sottoinsiemi di $\color{#7F7F7F} V$
> 
> Se in un grafo due vertici distinti $v, w \in V$ sono adiacenti, cioè $v E w$, allora anche $w E w$. Per questo motivo un grafo può essere visto come un [insieme](Teoria%20degli%20insiemi.md#^definizione-insieme) $V$ di vertici ed una [famiglia](Teoria%20degli%20insiemi.md#^definizione-famiglia-di-insiemi) $E$ di [sottoinsiemi](Teoria%20degli%20insiemi.md#^definizione-sottoinsieme) di $V$ di [cardinalità](Teoria%20degli%20insiemi.md#^definizione-cardinalita-di-un-insieme) $2$, cioè gli elementi di $E$ sono insiemi della forma $\{v, w\}$ con $v, w \in V$ e $v \ne w$; gli elementi di $E$ si dicono _spigoli_.

> [!definizione]+ Definizione: spigolo
> 
> gli elementi di E si dicono spigoli.
^definizione-spigolo

> [!esempio]- Esempi: spigoli
> 
> Nell'esempio qui sopra E = {{a, c}, {a, d}, {a, e}, {c, d}}.

> [!definizione]+ Definizione: grafo completo
> 
> Ogni vertice è adiacente a ogni altro vertice.
^definizione-grafo-completo

> [!esempio]- Esempio di grafo completo
> 
> ![](Pasted%20image%2020250111175857.png)
> Questo è un grafo completo, cioè ogni vertice `e
> adiacente ad ogni altro vertice: E = {{a, b}, {a, c},
> {a, d}, {a, e}, {b, c}, {b, d}, {b, e}, {c, d}, {c, e}, {d, e}}.

> [!definizione]+ Definizione: vertici indipendenti e grafo indipendente
> 
> Un insieme $U$ formato da vertici indipendenti è detto indipendente
> Un grafo $V$ formato da vertici indipendenti è detto grafo indipendente.

> [!osservazione]+ Osservazione: grafo indipendente => $\color{#7F7F7F} E = \emptyset$

> [!esempio]- Esempio: vertici indipendenti
> 
> ![](Pasted%20image%2020250111175943.png)
> In questo grafo, l'insieme U = {b, c} è indipendente, cioè nessun vertice di U è adiacente ad qualche altro.

> [!esempio]- Esempio: grafo indipendente
> 
> ![](Pasted%20image%2020250111180121.png)
> In questo grafo V è indipendente, cioè nessun vertice
> è adiacente a qualche altro vertice: E = \emptyset.

> [!definizione]+ Definizione: grafo bipartito

> [!esempio]- Esempio: grafo bipartito
> 
> ![](Pasted%20image%2020250111180148.png)
> Questo è un grafo bipartito, cioè l'insieme dei ver-
> tici V può essere ripartito in due insiemi disgiunti
> U = {a, b, c} e W = {d, e} tali che sia U che W
> sono indipendenti.

> [!osservazione]+ Non-unicità dei disegni di un grafo
> 
> Attenzione!:
> Il modo di disegnare un grafo non è unico! Per esempio
> ![](Pasted%20image%2020250111180303.png)
> denotano il medesimo grafo completo con 5 vertici.

(al massimo fare simulazione con Manim che fa vedere la trasformazione di un grafo nell'altro)
%%

---

> [!fonti]+ Fonti
> 
> - 🏫 Corso di Laurea in Informatica (`L-31 R`) presso l'Università di Torino:
>     - Corso di _Matematica Discreta, Algebra e Geometria - parte di Matematica Discreta & Algebra (parte 1) - canale C_, A.A. 2023-24 ([pagina Moodle](https://informatica.i-learn.unito.it/course/view.php?id=2750)):
> 		- Proff. Chen Yu e Terracini Lea, lezioni in aula.
>     - Corso di _Matematica Discreta, Algebra e Geometria - parte di Algebra Lineare & Geometria (parte 2) - canale C_, A.A. 2023-24 ([pagina Moodle](https://informatica.i-learn.unito.it/course/view.php?id=2750)):
> 		- Prof. Radeschi Marco, lezioni in aula.
>     - Corso di _Logica Matematica_, A.A. 2022-23 ([pagina Moodle](https://informatica.i-learn.unito.it/course/view.php?id=2480)):
> 		- Proff. Andretta Alessandro, Motto Ros Luca e Viale Matteo, slide:
> 			- [_2.2 - Relazioni_](https://informatica.i-learn.unito.it/pluginfile.php/336712/mod_folder/content/0/Capitolo%202%20-%20Elementi%20di%20teoria%20degli%20insiemi/2.2%20-%20Relazioni_moodle.pdf).
