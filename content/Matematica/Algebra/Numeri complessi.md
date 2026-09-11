
> [!premessa] Premessa
> 
> Ciao! Se è la prima volta che capiti su questo sito, ti consiglio di consultare la [pagina principale](index.md) di questo cosiddetto _Giardino Digitale_ per scoprire meglio cos'è e come navigarlo.
> 
> Lo stato di questa nota è al momento: 🔴 <font color="#FF7F7F">_Bozza_</font>.

---

%% 
introdurre meglio l'unità immaginaria
%%

I [_numeri complessi_](Matematica/Algebra/Numeri%20complessi.md#^definizione-numero-complesso) sono un ampliamento dell'insieme dei numeri reali $\mathbb{R}$%% Link %% a cui aggiungiamo l'[_unità immaginaria_](Matematica/Algebra/Numeri%20complessi.md#^definizione-unita-immaginaria).

> [!definizione] Definizione: unità immaginaria
> 
> L'**unità immaginaria** $i$ è un valore definito come
> 
> $$
> i^2 = -1
> $$
^definizione-unita-immaginaria

> [!definizione] Definizione: numero complesso
> 
> Un **numero complesso** $z$ è un oggetto algebrico che si scrive come
> 
> $$
> z = a + bi
> $$
> 
> dove:
> - $a$ è un numero reale%% Link %% arbitrario ed è detto **parte reale**,
> - $b$ è un numero reale%% link %% arbitrario ed è detto **parte immaginaria** e
> - $i$ è l'[unità immaginaria](Matematica/Algebra/Numeri%20complessi.md#^definizione-unita-immaginaria).
^definizione-numero-complesso

> [!esempio] Esempi di numeri complessi
> 
> Sono esempi di [numeri complessi](Matematica/Algebra/Numeri%20complessi.md#^definizione-numero-complesso) i numeri nella seguente tabella, in cui viene specificato il valore dei coefficienti%% Link %% $a$ e $b$:
> 
> | **Numero complesso** | $\boldsymbol a$       | $\boldsymbol b$   |
> | ---------------- | --------- | ----- |
> | $2 + i$          | $2$       | $1$   |
> | $\sqrt 7$        | $\sqrt 7$ | $0$   |
> | $23i$            | $0$       | $23$  |
> | $-1 + \pi i$     | $-1$      | $\pi$ 
^esempi-di-numeri-complessi

I [numeri complessi](Matematica/Algebra/Numeri%20complessi.md#^definizione-numero-complesso) costituiscono l'[_insieme dei numeri complessi $\mathbb{C}$_](Matematica/Algebra/Numeri%20complessi.md#^definizione-insieme-dei-numeri-complessi).

> [!definizione] Definizione: insieme dei numeri complessi $\mathbb{C}$
> 
> L'**insieme dei numeri complessi $\mathbb{C}$** è l'[insieme](Matematica/Teoria%20degli%20insiemi/Teoria%20degli%20insiemi.md#^definizione-insieme) di tutti [numeri complessi](Matematica/Algebra/Numeri%20complessi.md#^definizione-numero-complesso).
^definizione-insieme-dei-numeri-complessi

%% 
definire meglio l'insieme dei numeri complessi
%%

> [!osservazione] Osservazione: collegamento tra numeri reali e numeri complessi
> 
> Possiamo notare come ogni numero reale%% link %% in realtà non è altro che un [numero complesso](Matematica/Algebra/Numeri%20complessi.md#^definizione-numero-complesso) $a + bi$ in cui la [parte immaginaria](Matematica/Algebra/Numeri%20complessi.md#^definizione-numero-complesso) $b$ vale $0$: per esempio, $\sqrt 7$ è un [numero complesso](Matematica/Algebra/Numeri%20complessi.md#^definizione-numero-complesso) in cui $a = \sqrt 7$ e $b = 0$.
> 
> Per questo l'insieme dei numeri reali $\mathbb{R}$%% link %% viene considerato un  [sottoinsieme](Matematica/Teoria%20degli%20insiemi/Teoria%20degli%20insiemi.md#^definizione-sottoinsieme) dell'insieme dei numeri complessi $\mathbb{C}$%% link %%.

Ogni [numero complesso](Matematica/Algebra/Numeri%20complessi.md#^definizione-numero-complesso) ha un suo "fratello", detto [_coniugato_](Matematica/Algebra/Numeri%20complessi.md#^definizione-coniugato-di-un-numero-complesso).

> [!definizione] Definizione: coniugato di un numero complesso
> 
> Dato un [numero complesso](Matematica/Algebra/Numeri%20complessi.md#^definizione-numero-complesso) $z = a + bi$, il suo **coniugato** (o **coniugio**) $\bar z$ è il [numero complesso](Matematica/Algebra/Numeri%20complessi.md#^definizione-numero-complesso)
> 
> $$
> \bar z = a - bi
> $$
> 
> ottenuto da $z$ cambiando il segno%% link %% della sua [parte immaginaria](Matematica/Algebra/Numeri%20complessi.md#^definizione-numero-complesso).
^definizione-coniugato-di-un-numero-complesso

> [!osservazione] Osservazione: numero complesso uguale al suo coniugato
> 
> Notiamo come un [numero complesso](Matematica/Algebra/Numeri%20complessi.md#^definizione-numero-complesso) $z = a + bi$ è uguale al suo [coniugato](Matematica/Algebra/Numeri%20complessi.md#^definizione-coniugato-di-un-numero-complesso) $\bar z = a - bi$ solo quando la [parte immaginaria](Matematica/Algebra/Numeri%20complessi.md#^definizione-numero-complesso) $b$ è nulla, ossia quando $z$ è in realtà un numero reale%% Link %%, quindi:
> 
> $$
> z \in \mathbb{R} \iff z = \bar z
> $$

> [!definizione] Definizione: modulo di un numero complesso
> 
> Dato un [numero complesso](Matematica/Algebra/Numeri%20complessi.md#^definizione-numero-complesso) $z = a + bi$, il suo **modulo** $\vert z \vert$ è il numero reale%% link %%
> 
> $$
> \vert z \vert = \sqrt{a^2 + b^2}
> $$
^definizione-modulo-di-un-numero-complesso

> [!osservazione] Osservazione: prodotto di un numero complesso col suo coniugato
> 
> Il prodotto%% link %% tra un [numero complesso](Matematica/Algebra/Numeri%20complessi.md#^definizione-numero-complesso) $z = a + bi$ e il suo [coniugato](Matematica/Algebra/Numeri%20complessi.md#^definizione-coniugato-di-un-numero-complesso) $\bar z = a - bi$ è uguale al quadrato del [modulo](Matematica/Algebra/Numeri%20complessi.md#^definizione-modulo-di-un-numero-complesso) $\vert z \vert = \sqrt{a^2 + b^2}$, infatti
> 
> $$
> z \cdot \bar z = (a+bi) \cdot (a-bi) = a^2 + b^2 = \vert z \vert ^2
> $$
^osservazione-prodotto-di-un-numero-complesso-col-suo-coniugato

> [!definizione] Definizione: inverso di un numero complesso
> 
> Dato un [numero complesso](Matematica/Algebra/Numeri%20complessi.md#^definizione-numero-complesso) $z = a + bi$, il suo **inverso** $z^{-1}$ è il [numero complesso](Matematica/Algebra/Numeri%20complessi.md#^definizione-numero-complesso)
> 
> $$
> z^{-1} = \dfrac{\bar z}{\vert z \vert^2}
> $$
^definizione-inverso-di-un-numero-complesso

Possiamo provare l'[inverso di un numero complesso](Matematica/Algebra/Numeri%20complessi.md#^definizione-inverso-di-un-numero-complesso) è effettivamente il suo _inverso_%% link %% per come lo intendiamo dal punto di vista della teoria dei gruppi%% link %%, infatti moltiplicando un [numero complesso](Matematica/Algebra/Numeri%20complessi.md#^definizione-numero-complesso) per il suo [inverso](Matematica/Algebra/Numeri%20complessi.md#^definizione-inverso-di-un-numero-complesso) otteniamo $1$.

> [!proposizione] Proposizione: inverso di un numero complesso
> 
> Dato un [numero complesso](Matematica/Algebra/Numeri%20complessi.md#^definizione-numero-complesso) $z = a + bi$, il suo [inverso](Matematica/Algebra/Numeri%20complessi.md#^definizione-inverso-di-un-numero-complesso) $\displaystyle z^{-1} = \dfrac{\bar z}{|z|^2}$ rispetta la definizione di _inverso_%% link %%, ossia:
> 
> $$
> z \cdot z^{-1} = 1
> $$
^proposizione-inverso-di-un-numero-complesso

> [!dimostrazione] Dimostrazione: inverso di un numero complesso
> 
> Dimostriamo che $z \cdot z^{-1} = 1$:
> 
> $$
> z \cdot z^{-1} = z \cdot \dfrac{\bar z}{|z|^2} = \dfrac{z \cdot \bar z}{|z|^2} \ {\color{#FF7F7F} = } \ \dfrac{|z|^2}{|z|^2} = 1
> $$
> 
> Sottolineiamo che l'uguaglianza segnalata in rosso, ossia $z \cdot \bar z = |z|^2$, è già stata verificata in una [osservazione precedente](Matematica/Algebra/Numeri%20complessi.md#^osservazione-prodotto-di-un-numero-complesso-col-suo-coniugato).
> 
> $\blacksquare$

> [!esempio] Esempi di inversi di numeri complessi
> 
> Ecco alcuni esempi di [inversi di numeri complessi](Matematica/Algebra/Numeri%20complessi.md#^definizione-inverso-di-un-numero-complesso):
> 
> | **Numero complesso** | **Suo inverso**             |
> | -------------------- | --------------------------- |
> | $z_1 = 2 + i$        | $z_1^{-1} = \dfrac{2-i}{5}$ |
> | $z_2 = -3i$          | $z_2^{-1} = \dfrac{i}{3}$   |
> | $z_3 = i$            | $z_3^{-1} = -i$             |

# Piano complesso

Mentre l'insieme dei numeri reali $\mathbb{R}$%% link %% viene generalmente rappresentato con una retta%% link %%, detta appunto _retta reale_%% Link %%, i [numeri complessi](Matematica/Algebra/Numeri%20complessi.md#^definizione-numero-complesso) vengono rappresentati su un piano cartesiano%% Link %% detto [_piano complesso_](Matematica/Algebra/Numeri%20complessi.md#^definizione-piano-complesso).

> [!definizione] Definizione: piano complesso
> 
> Il **piano complesso** è un piano cartesiano%% link %% su cui viene rappresentato ogni [numero complesso](Matematica/Algebra/Numeri%20complessi.md#^definizione-numero-complesso) $z = a + bi$ come un punto%% link %% di coordinate%% link a "coordinate cartesiane" %% $(a,b)$:
> - sull'asse delle ascisse%% Link %%, detto **asse reale**, viene indicata la [parte reale](Matematica/Algebra/Numeri%20complessi.md#^definizione-numero-complesso) e
> - sull'asse delle ordinate%% link %%, detto **asse immaginario**, viene indicata la [parte immaginaria](Matematica/Algebra/Numeri%20complessi.md#^definizione-numero-complesso).
^definizione-piano-complesso

%% inserire figura nella definizione con alcuni esempi di numeri complessi %%

%% 
osservazione: asse reale non è altro che la retta reale
%%

%% 
osservazione: somma di due numeri complessi come vettori sul piano complesso fatta con regola del parallelogramma
%%

## Coordinate polari

Come sappiamo già%% link %%, ogni punto%% Link %% sul piano cartesiano%% link %% può essere rappresentato anche come un vettore%% link %%. Questo vettore, nel caso del [piano complesso](Matematica/Algebra/Numeri%20complessi.md#^definizione-piano-complesso), può essere identificato usando le [_coordinate polari_](Matematica/Algebra/Numeri%20complessi.md#^definizione-coordinate-polari).

> [!definizione] Definizione: coordinate polari
> 
> In un [piano complesso](Matematica/Algebra/Numeri%20complessi.md#^definizione-piano-complesso), le **coordinate polari** di un [numero complesso](Matematica/Algebra/Numeri%20complessi.md#^definizione-numero-complesso) $z = a + bi$ sono una coppia di valori $(r, \theta)$ in cui, dato un vettore%% link %% che parte dall'origine del piano%% link %% e arriva al punto%% link %% $(a,b)$ corrispondente al [numero complesso](Matematica/Algebra/Numeri%20complessi.md#^definizione-numero-complesso) $z = a + bi$,
> - $r$, detto **raggio**, corrisponde alla lunghezza del vettore
> - $\theta$, detto **argomento** o **fase**, corrisponde all'angolo formato dal vettore con l'[asse reale](Matematica/Algebra/Numeri%20complessi.md#^definizione-numero-complesso).
^definizione-coordinate-polari

%% inserire figura di esempio nella definizione %%

%% 
esempi di coordinate polari
%%

> [!osservazione] Osservazione: corrispondenza tra coordinate cartesiane e coordinate polari
> 
> Dato un [numero complesso](Matematica/Algebra/Numeri%20complessi.md#^definizione-numero-complesso) $z = a + bi$ rappresentato su un [piano complesso](Matematica/Algebra/Numeri%20complessi.md#^definizione-piano-complesso), per passare dalle sue [coordinate polari](Matematica/Algebra/Numeri%20complessi.md#^definizione-coordinate-polari) $(r, \theta)$ a quelle cartesiane%% link a "coordinate cartesiane" %% $(a,b)$ basta usare le formule
> 
> $$
> a = r \cos \theta \qquad b = r \sin \theta
> $$
> 
> e, viceversa,
> 
> $$
> r = \sqrt{a^2 + b^2} \qquad \theta = \arccos \dfrac{x}{\sqrt{a^2 + b^2}}
> $$
> 
> Di conseguenza, un [numero complesso](Matematica/Algebra/Numeri%20complessi.md#^definizione-numero-complesso) $z = a + bi$ può essere scritto direttamente in [coordinate polari](Matematica/Algebra/Numeri%20complessi.md#^definizione-coordinate-polari) come
> 
> $$
> \begin{align*}
> z &= a + bi \\
> &= r \cos \theta + (r \sin \theta)i \\
> &= r(\cos \theta + i\sin \theta)
> \end{align*}
> $$

> [!osservazione] Osservazione: corrispondenza tra modulo e raggio delle coordinate polari
> 
> Dato un [numero complesso](Matematica/Algebra/Numeri%20complessi.md#^definizione-numero-complesso) $z = a + bi$, il suo raggio $r$ delle [coordinate polari](Matematica/Algebra/Numeri%20complessi.md#^definizione-coordinate-polari) si calcola come
> 
> $$
> r = \sqrt{a^2 + b^2}
> $$
> 
> ma ciò non è altro che la formula del [modulo di un numero complesso](Matematica/Algebra/Numeri%20complessi.md#^definizione-modulo-di-un-numero-complesso) $|z|$, che quindi corrisponde proprio alla lunghezza del vettore che descrive $z$. 
^osservazione-corrispondenza-tra-modulo-e-raggio-delle-coordinate-polari

> [!osservazione] Osservazione: piano complesso e coniugato
> 
> Dato un [numero complesso](Matematica/Algebra/Numeri%20complessi.md#^definizione-numero-complesso) $z = a + bi$, il suo [coniugato](Matematica/Algebra/Numeri%20complessi.md#^definizione-coniugato-di-un-numero-complesso) $\bar z = a - bi$ è il punto%% link %% ottenuto cambiando il segno della [parte immaginaria](Matematica/Algebra/Numeri%20complessi.md#^definizione-numero-complesso): geometricamente questo corrisponde a riflettere%% link %% il punto rispetto all'[asse reale](Matematica/Algebra/Numeri%20complessi.md#^definizione-piano-complesso).
> 
> In [coordinate polari](Matematica/Algebra/Numeri%20complessi.md#^definizione-coordinate-polari), questo corrisponde a cambiare l'argomento $\theta$ in $-\theta$ ma lasciando fisso il raggio $r$.

%% mettere figura che faccia vedere z e il suo coniugato sul piano complesso %%

## Notazione esponenziale

> [!notazione] Notazione esponenziale delle coordinate polari
> 
> Un [numero complesso](Matematica/Algebra/Numeri%20complessi.md#^definizione-numero-complesso) può essere espresso in [coordinate polari](Matematica/Algebra/Numeri%20complessi.md#^definizione-coordinate-polari) attraverso la sua **notazione esponenziale**
> 
> $$
> z = re^{i\theta}
> $$
> 
> dove
> 
> $$
> e^{i\theta} = \cos \theta + i \sin \theta
> $$
^notazione-esponenziale-delle-coordinate-polari

Questa $e$ nella [notazione esponenziale](Matematica/Algebra/Numeri%20complessi.md#^notazione-esponenziale-delle-coordinate-polari) va intesa proprio come costante di Nepero%% link %%, ma il motivo per cui è stata adottata in questa notazione è dovuto alle rappresentazioni delle funzioni esponenziali%% link %% e trigonometriche%% link %% come serie di potenze%% link %%: giustificare questa scelta ci porterebbe troppo lontano, per noi è sufficiente considerare questa misteriosa notazione $e^{i\theta}$ come un simbolo che vuol dire semplicemente $\cos \theta + i \sin \theta$.

%% 
spiegare poi perché si usa $e$ qui, magari più in avanti nel percorso di Algebra
%%

Possiamo però notare come $e^{i\theta}$ si comporti esattamente come una potenza%% link a "potenza" $ %%, motivo per cui viene considerata lecita questa notazione.

> [!proposizione] Proposizione: proprietà degli esponenti nella notazione esponenziale
> 
> Nella [notazione esponenziale](Matematica/Algebra/Numeri%20complessi.md#^notazione-esponenziale-delle-coordinate-polari), vale la relazione
> 
> $$
> e^{i(\theta + \varphi)} = e^{i\theta} \cdot e^{i\varphi}
> $$
^proposizione-proprieta-degli-esponenti-nella-notazione-esponenziale

> [!dimostrazione] Dimostrazione: proprietà degli esponenti nella notazione esponenziale
> 
> Dimostriamo che vale la [proprietà degli esponenti nella notazione esponenziale](Matematica/Algebra/Numeri%20complessi.md#^proposizione-proprieta-degli-esponenti-nella-notazione-esponenziale):
> 
> $$
> \begin{align*}
> e^{i(\theta + \varphi)} &= {\color{#FF7F7F} \cos (\theta + \varphi) } + i \ {\color{#7F7FFF} \sin (\theta + \varphi) } \\
> &= {\color{#FF7F7F} \cos \theta \cos \varphi - \sin \theta \sin \varphi } + i \ {\color{#7F7FFF} (\sin \theta \cos \varphi + \cos \theta \sin \varphi ) } \\
> &= (\cos \theta + i \sin \theta) \cdot (\cos \varphi + i \sin \varphi) \\
> &= e^{i\theta} \cdot e^{i \varphi}
> \end{align*}
> $$
> 
> $\blacksquare$

> [!osservazione] Osservazione: utilità della notazione esponenziale
> 
> Grazie a questa [proprietà degli esponenti](Matematica/Algebra/Numeri%20complessi.md#^proposizione-proprieta-degli-esponenti-nella-notazione-esponenziale), ora possiamo comprendere perché è così utile la [notazione esponenziale](Matematica/Algebra/Numeri%20complessi.md#^notazione-esponenziale-delle-coordinate-polari): dati due [numeri complessi](Matematica/Algebra/Numeri%20complessi.md#^definizione-numero-complesso) $z_1 = r_1e^{i\theta_1}$ e $z_2 = r_2e^{i\theta_2}$, il loro prodotto%% Link %% è semplicemente
> 
> $$
> z_1 \cdot z_2 = r_1e^{i\theta_1} \cdot r_2e^{i\theta_2} = r_1r_2e^{i(\theta_1 + \theta_2)}
> $$
> 
> In altre parole, quando si fa il prodotto%% Link %% di due [numeri complessi](Matematica/Algebra/Numeri%20complessi.md#^definizione-numero-complesso), i loro raggi si moltiplicano e gli argomenti si sommano.
> 
> Con la [notazione esponenziale](Matematica/Algebra/Numeri%20complessi.md#^notazione-esponenziale-delle-coordinate-polari), per ogni [numero complesso](Matematica/Algebra/Numeri%20complessi.md#^definizione-numero-complesso) $z = re^{i\theta} \ne 0$ possiamo facilmente calcolare anche il suo [inverso](Matematica/Algebra/Numeri%20complessi.md#^definizione-inverso-di-un-numero-complesso) come
> 
> $$
> z^{-1} = r^{-1}e^{-i\theta}
> $$
> 
> Ossia, per ottenere l'[inverso di un numero complesso](Matematica/Algebra/Numeri%20complessi.md#^definizione-inverso-di-un-numero-complesso), si fa l'inverso%% link %% del raggio e l'opposto%% link %% dell'argomento.

> [!osservazione] Osservazione: numeri complessi con modulo unitario
> 
> I [numeri complessi](Matematica/Algebra/Numeri%20complessi.md#^definizione-numero-complesso) $e^{i\theta}$ in cui $r = 1$, ossia avente [modulo](Matematica/Algebra/Numeri%20complessi.md#^definizione-modulo-di-un-numero-complesso) unitario (ricordiamo la [corrispondenza tra modulo e raggio](Matematica/Algebra/Numeri%20complessi.md#^osservazione-corrispondenza-tra-modulo-e-raggio-delle-coordinate-polari)), sono precisamente i punti%% link %% che compongono la circonferenza unitaria%% link a definizione di "circonferenza unitaria" in "piano cartesiano" = circonferenza con raggio 1 e centro nell'origine %%.

%% 
identità di eulero

nel caso in cui $\theta = \pi$, allora
$$
e^{i\pi} = -1
$$
%%

> [!osservazione] Osservazione: uguaglianza di numeri complessi
> 
> Notiamo che due [numeri complessi](Matematica/Algebra/Numeri%20complessi.md#^definizione-numero-complesso) $z_1 = r_1e^{i\theta_1}$ e $z_2 = r_2e^{i\theta_2}$ non nulli%% link %% sono in realtà lo stesso numero complesso se e solo se valgono entrambi questi fatti:
> 1. $r_1 = r_2$ e
> 2. $\theta_1 = \theta_2 + 2k\pi$ per qualche $k \in \mathbb{Z}$, perché essendo $\theta_1$ e $\theta_2$ angoli%% Link %% vale la periodicità degli angoli%% link %%.

---

> [!fonti] Fonti
> 
> - 📚 Bruno Martelli, _Geometria e algebra lineare_, autopubblicato, 2025:
> 	- Capitolo 1 - _Nozioni preliminari_:
> 		- 1.4 - _Numeri complessi_.
