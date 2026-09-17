
> [!premessa]+ Premessa
> 
> Ciao! Se è la prima volta che capiti su questo sito, ti consiglio di consultare la [pagina principale](index.md) di questo cosiddetto _Giardino Digitale_ per scoprire meglio cos'è e come navigarlo.
> 
> Lo stato di questa nota è al momento: 🔴 <font color="#FF7F7F">_Bozza_</font>.

---

%% 
introdurre meglio l'unità immaginaria
%%

I [_numeri complessi_](Matematica/Algebra/Numeri%20complessi.md#^definizione-numero-complesso) sono un ampliamento dell'insieme dei numeri reali $\mathbb{R}$%% Link %% a cui aggiungiamo l'[_unità immaginaria_](Matematica/Algebra/Numeri%20complessi.md#^definizione-unita-immaginaria).

> [!definizione]+ Definizione: unità immaginaria
> 
> L'**unità immaginaria** $i$ è un valore definito come
> 
> $$
> i^2 = -1
> $$
^definizione-unita-immaginaria

> [!definizione]+ Definizione: numero complesso
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

> [!esempio]- Esempi di numeri complessi
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

> [!definizione]+ Definizione: insieme dei numeri complessi $\color{#FF7FFF} \mathbb{C}$
> 
> L'**insieme dei numeri complessi $\mathbb{C}$** è l'[insieme](Matematica/Teoria%20degli%20insiemi/Teoria%20degli%20insiemi.md#^definizione-insieme) di tutti [numeri complessi](Matematica/Algebra/Numeri%20complessi.md#^definizione-numero-complesso).
^definizione-insieme-dei-numeri-complessi

%% 
definire meglio l'insieme dei numeri complessi ed esplicitare quale tipo di struttura algebrica è
%%

> [!osservazione]+ Osservazione: collegamento tra numeri reali e numeri complessi
> 
> Possiamo notare come ogni numero reale%% link %% in realtà non è altro che un [numero complesso](Matematica/Algebra/Numeri%20complessi.md#^definizione-numero-complesso) $a + bi$ in cui la [parte immaginaria](Matematica/Algebra/Numeri%20complessi.md#^definizione-numero-complesso) $b$ vale $0$: per esempio, $\sqrt 7$ è un [numero complesso](Matematica/Algebra/Numeri%20complessi.md#^definizione-numero-complesso) in cui $a = \sqrt 7$ e $b = 0$.
> 
> Per questo l'insieme dei numeri reali $\mathbb{R}$%% link %% viene considerato un  [sottoinsieme](Matematica/Teoria%20degli%20insiemi/Teoria%20degli%20insiemi.md#^definizione-sottoinsieme) dell'insieme dei numeri complessi $\mathbb{C}$%% link %%.

Ogni [numero complesso](Matematica/Algebra/Numeri%20complessi.md#^definizione-numero-complesso) ha un suo "fratello", detto [_coniugato_](Matematica/Algebra/Numeri%20complessi.md#^definizione-coniugato-di-un-numero-complesso).

> [!definizione]+ Definizione: coniugato di un numero complesso
> 
> Dato un [numero complesso](Matematica/Algebra/Numeri%20complessi.md#^definizione-numero-complesso) $z = a + bi$, il suo **coniugato** (o **coniugio**) $\overline z$ è il [numero complesso](Matematica/Algebra/Numeri%20complessi.md#^definizione-numero-complesso)
> 
> $$
> \overline z = a - bi
> $$
> 
> ottenuto da $z$ cambiando il segno%% link %% della sua [parte immaginaria](Matematica/Algebra/Numeri%20complessi.md#^definizione-numero-complesso).
^definizione-coniugato-di-un-numero-complesso

> [!osservazione]+ Osservazione: numero complesso uguale al suo coniugato
> 
> Notiamo come un [numero complesso](Matematica/Algebra/Numeri%20complessi.md#^definizione-numero-complesso) $z = a + bi$ è uguale al suo [coniugato](Matematica/Algebra/Numeri%20complessi.md#^definizione-coniugato-di-un-numero-complesso) $\overline z = a - bi$ solo quando la [parte immaginaria](Matematica/Algebra/Numeri%20complessi.md#^definizione-numero-complesso) $b$ è nulla, ossia quando $z$ è in realtà un numero reale%% Link %%, quindi:
> 
> $$
> z \in \mathbb{R} \iff z = \overline z
> $$

> [!definizione]+ Definizione: modulo di un numero complesso
> 
> Dato un [numero complesso](Matematica/Algebra/Numeri%20complessi.md#^definizione-numero-complesso) $z = a + bi$, il suo **modulo** $\vert z \vert$ è il numero reale%% link %%
> 
> $$
> \vert z \vert = \sqrt{a^2 + b^2}
> $$
^definizione-modulo-di-un-numero-complesso

> [!osservazione]+ Osservazione: prodotto di un numero complesso col suo coniugato
> 
> Il prodotto%% link %% tra un [numero complesso](Matematica/Algebra/Numeri%20complessi.md#^definizione-numero-complesso) $z = a + bi$ e il suo [coniugato](Matematica/Algebra/Numeri%20complessi.md#^definizione-coniugato-di-un-numero-complesso) $\overline z = a - bi$ è uguale al quadrato del [modulo](Matematica/Algebra/Numeri%20complessi.md#^definizione-modulo-di-un-numero-complesso) $\vert z \vert = \sqrt{a^2 + b^2}$, infatti
> 
> $$
> z \cdot \overline z = (a+bi) \cdot (a-bi) = a^2 + b^2 = \vert z \vert ^2
> $$
^osservazione-prodotto-di-un-numero-complesso-col-suo-coniugato

> [!definizione]+ Definizione: inverso di un numero complesso
> 
> Dato un [numero complesso](Matematica/Algebra/Numeri%20complessi.md#^definizione-numero-complesso) $z = a + bi$, il suo **inverso** $z^{-1}$ è il [numero complesso](Matematica/Algebra/Numeri%20complessi.md#^definizione-numero-complesso)
> 
> $$
> z^{-1} = \dfrac{\overline z}{\vert z \vert^2}
> $$
^definizione-inverso-di-un-numero-complesso

Possiamo provare l'[inverso di un numero complesso](Matematica/Algebra/Numeri%20complessi.md#^definizione-inverso-di-un-numero-complesso) è effettivamente il suo _inverso_%% link %% per come lo intendiamo dal punto di vista della teoria dei gruppi%% link %%, infatti moltiplicando un [numero complesso](Matematica/Algebra/Numeri%20complessi.md#^definizione-numero-complesso) per il suo [inverso](Matematica/Algebra/Numeri%20complessi.md#^definizione-inverso-di-un-numero-complesso) otteniamo $1$.

> [!proposizione]+ Proposizione: inverso di un numero complesso
> 
> Dato un [numero complesso](Matematica/Algebra/Numeri%20complessi.md#^definizione-numero-complesso) $z = a + bi$, il suo [inverso](Matematica/Algebra/Numeri%20complessi.md#^definizione-inverso-di-un-numero-complesso) $\displaystyle z^{-1} = \dfrac{\overline z}{|z|^2}$ rispetta la definizione di _inverso_%% link %%, ossia:
> 
> $$
> z \cdot z^{-1} = 1
> $$
^proposizione-inverso-di-un-numero-complesso

> [!dimostrazione]- Dimostrazione: inverso di un numero complesso
> 
> Dimostriamo che $z \cdot z^{-1} = 1$:
> 
> $$
> z \cdot z^{-1} = z \cdot \dfrac{\overline z}{|z|^2} = \dfrac{z \cdot \overline z}{|z|^2} \ {\color{#FF7F7F} = } \ \dfrac{|z|^2}{|z|^2} = 1
> $$
> 
> Sottolineiamo che l'uguaglianza segnalata in rosso, ossia $z \cdot \overline z = |z|^2$, è già stata verificata in una [osservazione precedente](Matematica/Algebra/Numeri%20complessi.md#^osservazione-prodotto-di-un-numero-complesso-col-suo-coniugato).
> 
> $\blacksquare$

> [!esempio]- Esempi di inversi di numeri complessi
> 
> Ecco alcuni esempi di [inversi di numeri complessi](Matematica/Algebra/Numeri%20complessi.md#^definizione-inverso-di-un-numero-complesso):
> 
> | **Numero complesso** | **Suo inverso**             |
> | -------------------- | --------------------------- |
> | $z_1 = 2 + i$        | $z_1^{-1} = \dfrac{2-i}{5}$ |
> | $z_2 = -3i$          | $z_2^{-1} = \dfrac{i}{3}$   |
> | $z_3 = i$            | $z_3^{-1} = -i$             |

# 1 - Piano complesso

Mentre l'insieme dei numeri reali $\mathbb{R}$%% link %% viene generalmente rappresentato con una retta%% link %%, detta appunto _retta reale_%% Link %%, i [numeri complessi](Matematica/Algebra/Numeri%20complessi.md#^definizione-numero-complesso) vengono rappresentati su un piano cartesiano%% Link %% detto [_piano complesso_](Matematica/Algebra/Numeri%20complessi.md#^definizione-piano-complesso).

> [!definizione]+ Definizione: piano complesso
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

## 1.1 - Coordinate polari

Come sappiamo già%% link %%, ogni punto%% Link %% sul piano cartesiano%% link %% può essere rappresentato anche come un vettore%% link %%. Questo vettore, nel caso del [piano complesso](Matematica/Algebra/Numeri%20complessi.md#^definizione-piano-complesso), può essere identificato usando le [_coordinate polari_](Matematica/Algebra/Numeri%20complessi.md#^definizione-coordinate-polari).

> [!definizione]+ Definizione: coordinate polari
> 
> In un [piano complesso](Matematica/Algebra/Numeri%20complessi.md#^definizione-piano-complesso), le **coordinate polari** di un [numero complesso](Matematica/Algebra/Numeri%20complessi.md#^definizione-numero-complesso) $z = a + bi$ sono una coppia di valori $(r, \theta)$ in cui, dato un vettore%% link %% che parte dall'origine del piano%% link %% e arriva al punto%% link %% $(a,b)$ corrispondente al [numero complesso](Matematica/Algebra/Numeri%20complessi.md#^definizione-numero-complesso) $z = a + bi$,
> - $r$, detto **raggio**, corrisponde alla lunghezza del vettore
> - $\theta$, detto **argomento** o **fase**, corrisponde all'angolo formato dal vettore con l'[asse reale](Matematica/Algebra/Numeri%20complessi.md#^definizione-numero-complesso).
^definizione-coordinate-polari

%% inserire figura di esempio nella definizione %%

%% 
esempi di coordinate polari
%%

> [!osservazione]+ Osservazione: corrispondenza tra coordinate cartesiane e coordinate polari
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
^corrispondenza-tra-coordinate-cartesiane-e-coordinate-polari

> [!osservazione]+ Osservazione: corrispondenza tra modulo e raggio delle coordinate polari
> 
> Dato un [numero complesso](Matematica/Algebra/Numeri%20complessi.md#^definizione-numero-complesso) $z = a + bi$, il suo raggio $r$ delle [coordinate polari](Matematica/Algebra/Numeri%20complessi.md#^definizione-coordinate-polari) si calcola come
> 
> $$
> r = \sqrt{a^2 + b^2}
> $$
> 
> ma ciò non è altro che la formula del [modulo di un numero complesso](Matematica/Algebra/Numeri%20complessi.md#^definizione-modulo-di-un-numero-complesso) $|z|$, che quindi corrisponde proprio alla lunghezza del vettore che descrive $z$. 
> 
> Per questo motivo il [raggio](Numeri%20complessi.md#^definizione-coordinate-polari) $r$ viene anche chiamato spesso _modulo_.
^osservazione-corrispondenza-tra-modulo-e-raggio-delle-coordinate-polari

> [!osservazione]+ Osservazione: piano complesso e coniugato
> 
> Dato un [numero complesso](Matematica/Algebra/Numeri%20complessi.md#^definizione-numero-complesso) $z = a + bi$, il suo [coniugato](Matematica/Algebra/Numeri%20complessi.md#^definizione-coniugato-di-un-numero-complesso) $\overline z = a - bi$ è il punto%% link %% ottenuto cambiando il segno della [parte immaginaria](Matematica/Algebra/Numeri%20complessi.md#^definizione-numero-complesso): geometricamente questo corrisponde a riflettere%% link %% il punto rispetto all'[asse reale](Matematica/Algebra/Numeri%20complessi.md#^definizione-piano-complesso).
> 
> In [coordinate polari](Matematica/Algebra/Numeri%20complessi.md#^definizione-coordinate-polari), questo corrisponde a cambiare l'argomento $\theta$ in $-\theta$ ma lasciando fisso il raggio $r$.

%% mettere figura che faccia vedere z e il suo coniugato sul piano complesso %%

## 1.2 - Notazione esponenziale

> [!notazione]+ Notazione esponenziale delle coordinate polari
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

> [!proposizione]+ Proposizione: proprietà degli esponenti nella notazione esponenziale
> 
> Nella [notazione esponenziale](Matematica/Algebra/Numeri%20complessi.md#^notazione-esponenziale-delle-coordinate-polari), vale la relazione
> 
> $$
> e^{i(\theta + \varphi)} = e^{i\theta} \cdot e^{i\varphi}
> $$
^proposizione-proprieta-degli-esponenti-nella-notazione-esponenziale

> [!dimostrazione]- Dimostrazione: proprietà degli esponenti nella notazione esponenziale
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

> [!osservazione]+ Osservazione: utilità della notazione esponenziale
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

> [!osservazione]+ Osservazione: numeri complessi con modulo unitario
> 
> I [numeri complessi](Matematica/Algebra/Numeri%20complessi.md#^definizione-numero-complesso) $e^{i\theta}$ in cui $r = 1$, ossia avente [modulo](Matematica/Algebra/Numeri%20complessi.md#^definizione-modulo-di-un-numero-complesso) unitario (ricordiamo la [corrispondenza tra modulo e raggio](Matematica/Algebra/Numeri%20complessi.md#^osservazione-corrispondenza-tra-modulo-e-raggio-delle-coordinate-polari)), sono precisamente i punti%% link %% che compongono la circonferenza unitaria%% link a definizione di "circonferenza unitaria" in "piano cartesiano" = circonferenza con raggio 1 e centro nell'origine %%.

%% 
identità di eulero

nel caso in cui $\theta = \pi$, allora
$$
e^{i\pi} = -1
$$
%%

> [!osservazione]+ Osservazione: uguaglianza di numeri complessi
> 
> Notiamo che due [numeri complessi](Matematica/Algebra/Numeri%20complessi.md#^definizione-numero-complesso) $z_1 = r_1e^{i\theta_1}$ e $z_2 = r_2e^{i\theta_2}$ non nulli%% link %% sono in realtà lo stesso numero complesso se e solo se valgono entrambi questi fatti:
> 1. $r_1 = r_2$ e
> 2. $\theta_1 = \theta_2 + 2k\pi$ per qualche $k \in \mathbb{Z}$, perché essendo $\theta_1$ e $\theta_2$ angoli%% Link %% vale la periodicità degli angoli%% link %%.

# 2 - Proprietà dei numeri complessi

I [numeri complessi](Matematica/Algebra/Numeri%20complessi.md#^definizione-numero-complesso) hanno numerose proprietà: nel caso di un prodotto%% link %%, si dimostrano facilmente attraverso la [notazione esponenziale](Numeri%20complessi.md#^notazione-esponenziale-delle-coordinate-polari). Prova a svolgere le dimostrazioni come esercizio prima di leggerle.

> [!proprieta]+ Proprietà: disuguaglianza triangolare dei moduli
> 
> Dati due [numeri complessi](Numeri%20complessi.md#^definizione-numero-complesso) $z,w \in \mathbb{C}$, vale la disuguaglianza triangolare%% Link %% per i loro [moduli](Numeri%20complessi.md#^definizione-modulo-di-un-numero-complesso), ossia
> 
> $$
> |z + w| \le |z| + |w|
> $$

%%
[!dimostrazione]- Dimostrazione: disuguaglianza triangolare dei moduli
%%

> [!proprieta]+ Proprietà: distributività del modulo rispetto al prodotto
> 
> Dati due [numeri complessi](Numeri%20complessi.md#^definizione-numero-complesso) $z,w \in \mathbb{C}$, vale la distributività%% link %% per i loro [moduli](Numeri%20complessi.md#^definizione-modulo-di-un-numero-complesso) rispetto al prodotto%% Link %%, ossia
> 
> $$
> |z \cdot w| = |z| \cdot |w|
> $$

%% 
Dimostrazione
%%

> [!proprieta]+ Proprietà del modulo dell'inverso
> 
> Dato un [numero complesso](Numeri%20complessi.md#^definizione-numero-complesso) $z \in \mathbb{C} \setminus \{ 0 \}$, il [modulo](Numeri%20complessi.md#^definizione-modulo-di-un-numero-complesso) del suo [inverso](Numeri%20complessi.md#^definizione-inverso-di-un-numero-complesso) $|z^{-1}|$ è pari all'inverso%% link %% del suo [modulo](Numeri%20complessi.md#^definizione-modulo-di-un-numero-complesso) $|z|$:
> 
> $$
> |z^{-1}| = \dfrac{1}{|z|}
> $$

%% 
Dimostrazione
%%

> [!proprieta]+ Proprietà: uguaglianza dei moduli di un complesso e il suo coniugato
> 
> Dato un [numero complesso](Numeri%20complessi.md#^definizione-numero-complesso) $z \in \mathbb{C}$, il suo [modulo](Numeri%20complessi.md#^definizione-modulo-di-un-numero-complesso) $|z|$ è uguale al [modulo](Numeri%20complessi.md#^definizione-modulo-di-un-numero-complesso) del suo [coniugato](Numeri%20complessi.md#^definizione-coniugato-di-un-numero-complesso) $|\overline z|$:
> 
> $$
> |z| = |\overline z|
> $$

%% 
Dimostrazione
%%

> [!proprieta]+ Proprietà: distributività del coniugato rispetto alla somma
> 
> Dati due [numeri complessi](Numeri%20complessi.md#^definizione-numero-complesso) $z,w \in \mathbb{C}$, vale la distributività%% link %% per i loro [coniugati](Numeri%20complessi.md#^definizione-coniugato-di-un-numero-complesso) rispetto alla somma%% Link %%, ossia
> 
> $$
> \overline{z + w} = \overline z + \overline w
> $$

%% 
Dimostrazione
%%

> [!proprieta]+ Proprietà: distributività del coniugato rispetto al prodotto
> 
> Dati due [numeri complessi](Numeri%20complessi.md#^definizione-numero-complesso) $z,w \in \mathbb{C}$, vale la distributività%% link %% per i loro [coniugati](Numeri%20complessi.md#^definizione-coniugato-di-un-numero-complesso) rispetto al prodotto%% Link %%, ossia
> 
> $$
> \overline{z \cdot w} = \overline z \cdot \overline w
> $$

%% 
Dimostrazione
%%

# 3 - Radici $n$-esime di un numero complesso

Dato un [numero complesso](Numeri%20complessi.md#^definizione-numero-complesso) $z_0 \in \mathbb{C} \setminus { 0 }$, vediamo come trovare tutti i [numeri complessi](Numeri%20complessi.md#^definizione-numero-complesso) $z$ che, elevati alla potenza $n$, danno come risultato $z_0$, ossia come determinare le radici $n$-esime%% link %% di $z_0$ (con $n \in \mathbb{N}$):

$$
z^n = z_0
$$

Riscrivendo $z$ e $z_0$ in [notazione esponenziale](Numeri%20complessi.md#^notazione-esponenziale-delle-coordinate-polari), l'equazione diventa

$$
r^ne^{in\theta} = r_0e^{i\theta_0}
$$

Perché questa uguaglianza sia vera, devono essere uguali sia i [moduli](Numeri%20complessi.md#^osservazione-corrispondenza-tra-modulo-e-raggio-delle-coordinate-polari) sia gli [argomenti](Numeri%20complessi.md#^definizione-coordinate-polari):

1. Per i [moduli](Numeri%20complessi.md#^osservazione-corrispondenza-tra-modulo-e-raggio-delle-coordinate-polari), abbiamo che

   $$
   r^n = r_0 \implies r = \sqrt[n]{r_0}
   $$

   ma, [poiché il raggio $r_0$ è il modulo di $z_0$](Numeri%20complessi.md#^osservazione-corrispondenza-tra-modulo-e-raggio-delle-coordinate-polari), riscriviamo la formula come
   
   $$
   r = \sqrt[n]{|z_0|}
   $$
   
   per evitare che malauguratamente ci venga in mente di calcolare la radice $n$-esima di un numero negativo, come nel caso di $z_0=-1$. Infatti, il modulo di $z_0$ è sempre non negativo, e quindi anche il raggio $r$ delle radici è sempre non negativo.

2. Per gli [argomenti](Numeri%20complessi.md#^definizione-coordinate-polari), abbiamo che

   $$
   e^{in\theta} = e^{i\theta_0} \implies n\theta = \theta_0 + 2k\pi
   $$

   dove $k \in \mathbb{Z}$. Ricordiamoci della necessità di aggiungere $2k\pi$ perché aggiungere un multiplo intero di $2\pi$ a un angolo non cambia la direzione rappresentata da quell'angolo%% link %%.

In particolare, dividendo entrambi i membri per $n$, la seconda condizione può essere riscritta come

$$
\theta = \dfrac{\theta_0}{n} + \dfrac{2k\pi}{n}
$$

per qualche $k \in \mathbb{Z}$. Questa formula ci dice che, per ogni $k \in \mathbb{Z}$, otteniamo un possibile [argomento](Numeri%20complessi.md#^definizione-coordinate-polari) $\theta$ di una radice%% link %% dell'equazione iniziale $z^n = z_0$.

A prima vista, poiché $k$ può essere qualsiasi numero intero, sembrerebbe che esistano infinite radici%% link %%. In realtà, i valori di $k$ producono esattamente $n$ [numeri complessi](Numeri%20complessi.md#^definizione-numero-complesso) distinti: dopo $n$ valori consecutivi di $k$, le radici si ripetono, proprio perché aggiungere un multiplo intero di $2\pi$ a un angolo non cambia la direzione rappresentata da quell'angolo%% link %%.

Possiamo verificare questa cosa prendendo per esempio $k = n + 1$:

$$
\begin{align*}
\frac{2(n + 1)\pi}{n} &= \dfrac{2n\pi + 2\pi}{n} \\
&= \dfrac{2n\pi}{n} + \dfrac{2\pi}{n} \\
&= 2\pi + \dfrac{2\pi}{n}
\end{align*}
$$

E infatti, a causa della periodicità di $2\pi$%% link alla periodicità di $2\pi$ %%, il valore di questo [argomento](Numeri%20complessi.md#^definizione-coordinate-polari) $2\pi + \dfrac{2\pi}{n}$ è equivalente a $\dfrac{2\pi}{n}$, che corrisponde anche all'[argomento](Numeri%20complessi.md#^definizione-coordinate-polari) del caso $k=1$. Quindi i casi $k=n+1$ e $k=1$ rappresentano in realtà lo stesso [numero complesso](Numeri%20complessi.md#^definizione-numero-complesso).

Possiamo evincere quindi che per ogni $k \in \mathbb{Z}$ gli [argomenti](Numeri%20complessi.md#^definizione-coordinate-polari) saranno equivalenti a quelli ottenuti scegliendo un valore di $k$ compreso tra $0$ e $n-1$, sottraendo o aggiungendo opportuni multipli di $n$.

Per esempio, $k=n$ produrrà lo stesso [numero complesso](Numeri%20complessi.md#^definizione-numero-complesso) di $k=0$, $k=n+1$ lo stesso di $k=1$, e così via. Analogamente, $k=-n-2$ produrrà lo stesso numero complesso di $k=n-2$.

Di conseguenza, possiamo limitarci a considerare i valori di $k$ da $0$ a $n-1$, ottenendo così precisamente $n$ soluzioni distinte:

$$
\theta = \underbrace{\dfrac{\theta_0}{n}}_{k = 0}, \underbrace{\dfrac{\theta_0}{n} + \dfrac{2\pi}{n}}_{k = 1}, \underbrace{\dfrac{\theta_0}{n} + \dfrac{4\pi}{n}}_{k = 2}, \ldots, \underbrace{\dfrac{\theta_0}{n} + \dfrac{2(n-1)\pi}{n}}_{k = n-1}
$$

Le $n$ soluzioni%% Link %% dell'equazione $z^n = z_0$, riprendendo le due condizioni di prima, hanno tutte lo stesso [modulo](Numeri%20complessi.md#^osservazione-corrispondenza-tra-modulo-e-raggio-delle-coordinate-polari) e quindi lo stesso raggio:

$$
r = \sqrt[n]{|z_0|}
$$

I loro [argomenti](Numeri%20complessi.md#^definizione-coordinate-polari), invece, variano in una sequenza di angoli separati da un passo%% link a "passo" = valore fisso tra intervalli (?) %% costante%% link %% pari a

$$
\dfrac{2\pi}{n}
$$

Geometricamente, questo significa che le soluzioni formano i vertici%% Link %% di un poligono regolare%% Link %% centrato nell'origine, con $n$ lati%% Link %% e raggio%% link %% $\sqrt[n]{r_0}$.

Per esempio, le radici $n$-esime%% link %% di $1$, ossia le soluzioni%% link %% dell'equazione%% link %%

$$
z^n = 1
$$

sono

$$
z = e^{i \frac{2k\pi}{n}}
$$

dove $k = 0, 1, \ldots, n-1$. Queste $n$ soluzioni sono i vertici di un poligono regolare%% Link %% di raggio%% Link %% $1$ con $n$ lati%% Link %%.

Ora, per esempio, vediamo le radici terze di $-8$, cioè le soluzioni di $z^3 = -8$. Tutte le radici%% link %% avranno [raggio](Numeri%20complessi.md#^definizione-coordinate-polari)

$$
r = \sqrt[3]{|-8|} = \sqrt[3]{8} = 2
$$

Possiamo poi determinare i loro [argomenti](Numeri%20complessi.md#^definizione-coordinate-polari) e [passare dalle coordinate polari a quelle cartesiane](Numeri%20complessi.md#^corrispondenza-tra-coordinate-cartesiane-e-coordinate-polari):

| $\boldsymbol k$ | **[Notazione esponenziale $\boldsymbol{re^{i\theta}}$](Numeri%20complessi.md#^notazione-esponenziale-delle-coordinate-polari)** | **[Parte reale $\boldsymbol a$](Numeri%20complessi.md#^definizione-numero-complesso)** | **[Parte immaginaria $\boldsymbol b$](Numeri%20complessi.md#^definizione-numero-complesso)** |
| --------------- | ------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- |
| $0$             | $2e^{i\frac{\pi}{3}}$                                                                                                           | $2\cos \dfrac{\pi}{3}=1$                                                               | $2\sin \dfrac{\pi}{3}=\sqrt{3}$                                                              |
| $1$             | $2e^{i\pi}$                                                                                                                     | $2\cos \pi=-2$                                                                         | $2\sin \pi=0$                                                                                |
| $2$             | $2e^{i\frac{5\pi}{3}}$                                                                                                          | $2\cos \dfrac{5\pi}{3}=1$                                                              | $2\sin \dfrac{5\pi}{3}=-\sqrt{3}$                                                            |

Le tre radici sono quindi

$$
\begin{align*}
z_1&=1+i\sqrt{3} \\
z_2&=-2 \\
z_3&=1-i\sqrt{3}
\end{align*}
$$

%% 
scrivere algoritmo per calcolare le soluzioni
%%

%% 
esercizio: usa l'algoritmo per calcolare $z^4 = i$
%%

# 4 - Teorema fondamentale dell'algebra

Vediamo ora il risultato più importante in cui si possono applicare i [numeri complessi](Numeri%20complessi.md#^definizione-numero-complesso): il _teorema fondamentale dell'algebra_.

> [!teorema]+ Teorema fondamentale dell'algebra
> 
> Ogni polinomio%% link %% a coefficienti [complessi](Numeri%20complessi.md#^definizione-numero-complesso) ha almeno una radice%% link %% [complessa](Numeri%20complessi.md#^definizione-numero-complesso).
^teorema-fondamentale-dell-algebra

Esistono innumerevoli dimostrazioni di questo [teorema](Numeri%20complessi.md#^teorema-fondamentale-dell-algebra), ma nel libro di Martelli da cui ho studiato algebra lineare%% Link %% (lo trovi tra le fonti in fondo alla pagina) non sono riportate quindi per il momento non le affronterò qua, magari un giorno lo farò :)

<!--

[!esempio]- Esempio: soluzioni di $z^2 + 1$

Vediamo ora come si può applicare il [teorema fondamentale dell'algebra](Numeri%20complessi.md#^teorema-fondamentale-dell-algebra).

Consideriamo il polinomio%% link %%

$$
p(z) = z^2 + 1
$$

Il [teorema fondamentale dell'algebra](Numeri%20complessi.md#^teorema-fondamentale-dell-algebra) ci garantisce che questo polinomio ha almeno una radice%% link %% [complessa](Numeri%20complessi.md#^definizione-numero-complesso). Proviamo allora a risolverlo, trasformandolo in

$$
z^2 + 1 = 0 \implies z^2 = -1
$$

in modo da poter usare l'algoritmo di risoluzione delle radici $n$-esime%% link %%.

-->

> [!corollario]+ Corollario 1 del teorema fondamentale dell'algebra
> 
> Un polinomio%% link %% $p(x)$ a coefficienti [complessi](Numeri%20complessi.md#^definizione-numero-complesso) di grado%% link %% $n$ ha esattamente $n$ radici%% link %% [complesse](Numeri%20complessi.md#^definizione-numero-complesso), contate con molteplicità (ossia una radice%% link %% che si ripete più volte deve essere contata più volte).
^corollario-1-del-teorema-fondamentale-dell-algebra

%% 
dimostrazione pagg. 31-32 martelli
%%

> [!esempio]- Esempio: applicazione del corollario 1 del teorema fondamentale dell'algebra
> 
> Possiamo notare la veridicità del [corollario 1 del teorema fondamentale dell'algebra](Numeri%20complessi.md#^corollario-1-del-teorema-fondamentale-dell-algebra) già nell'esempio svolto prima%% Link %% in cui abbiamo visto che il polinomio%% link %% $p(z) = z^2 + 1$, di grado%% link %% $2$, ha esattamente $2$ radici%% link %% [complesse](Numeri%20complessi.md#^definizione-numero-complesso), ossia $+i$ e $-i$.
> 
> Prendiamo invece il polinomio%% Link %% $p(z) = (z - 2)^3$ di grado%% link %% $3$: possiamo riscriverlo come
> 
> $$
> \begin{align*}
> p(z) &= (z-1)^2(z-3) \\
> &= (z-1)(z-1)(z-3)
> \end{align*}
> $$
> 
> e notiamo che le sue radici sono $1$, $1$ e $3$: se contate in modo distinto sono due (cioè solo $1$ e $3$), ma se le contiamo con molteplicità sono tre come il grado%% link %% del polinomio%% link %%, confermando così quanto dice il [corollario](Numeri%20complessi.md#^corollario-1-del-teorema-fondamentale-dell-algebra).

C'è un motivo se il [corollario 1](Numeri%20complessi.md#^corollario-1-del-teorema-fondamentale-dell-algebra) si chiama così e non solo "corollario" e basta: ovviamente perché esiste anche una sua _remastered edition_, il [_corollario 2_](Numeri%20complessi.md#^corollario-2-del-teorema-fondamentale-dell-algebra), che esprime lo stesso concetto ma in maniera diversa.

> [!corollario]+ Corollario 2 del teorema fondamentale dell'algebra
> 
> Ogni polinomio%% link %% $p(x)$ a coefficienti%% link %% [complessi](Numeri%20complessi.md#^definizione-numero-complesso) si può riscrivere come prodotto%% link %% di polinomi%% link %% di primo grado%% link %%:
> 
> $$
> p(x) = a_n(x - z_1)(x - z_2) \ldots (x - z_n)
> $$
> 
> dove $a_n$ è il coefficiente più grande di $p(x)$ e $z_1, \ldots, z_n$ sono le radici%% link %% [complesse](Numeri%20complessi.md#^definizione-numero-complesso) di $p(x)$ contate con molteplicità (ossia una radice%% link %% che si ripete più volte deve essere contata più volte).
^corollario-2-del-teorema-fondamentale-dell-algebra

> [!esempio]- Esempio: applicazione del corollario 2 del teorema fondamentale dell'algebra
> 
> Consideriamo il polinomio%% link %%
> 
> $$
> p(x) = 2x^3 - 6x^2 + 8x - 4
> $$
> 
> Un uccellino ci ha detto che le sue radici%% link %% sono
> 
> $$
> \begin{align*}
> z_1 &= 1 \\
> z_2 &= 1 + i \\
> z_3 &= 1 - i
> \end{align*}
> $$
> 
> Per il [corollario 2](Numeri%20complessi.md#^corollario-2-del-teorema-fondamentale-dell-algebra), possiamo riscrivere il polinomio%% link %% come:
> 
> $$
> p(x) = 2(x - 1)(x - (1 + i))(x - (1 - i))
> $$
> 
> E infatti, sviluppandolo, otteniamo
> 
> $$
> \begin{align*}
> p(x) &= 2(x - 1)(x - (1 + i))(x - (1 - i)) \\
> &= 2(x-1)(x-1-i)(x-1+i) \\
> &= 2(x-1)((x-1)^2+1) \\
> &= 2(x-1)(x^2 - 2x + 2) \\
> &= 2(x^3 - 2x^2 + 2x - x^2 + 2x - 2) \\
> &= 2(x^3 - 3x^2 + 4x - 2) \\
> &= 2x^3 + 6x^2 + 8x - 4
> \end{align*}
> $$
> 
> che è proprio il polinomio%% link %% iniziale. Abbiamo così verificato che il polinomio è stato riscritto come prodotto di tre polinomi di primo grado%% Link %%, uno per ciascuna radice%% link %% [complessa](Numeri%20complessi.md#^definizione-numero-complesso).

## 4.1 - Polinomi a coefficienti reali

Sappiamo ora grazie al [teorema fondamentale dell'algebra](Numeri%20complessi.md#^teorema-fondamentale-dell-algebra) e al suo [corollario 1](Numeri%20complessi.md#^corollario-1-del-teorema-fondamentale-dell-algebra) che un polinomio%% link %% $p(x)$ di grado%% link %% $n$ ha esattamente $n$ radici%% link %% [complesse](Numeri%20complessi.md#^definizione-numero-complesso) contate con molteplicità.

Se $p(x)$ ha coefficienti%% link %% reali%% link %% (ossia in realtà [complessi](Numeri%20complessi.md#^definizione-numero-complesso) ma aventi [parte immaginaria](Numeri%20complessi.md#^definizione-numero-complesso) nulla%% link %%), possiamo dire qualcosa in più sulle sue radici%% link %% [complesse](Numeri%20complessi.md#^definizione-numero-complesso).

> [!proposizione]+ Proposizione: radice complessa e suo coniugato
> 
> Dato un polinomio%% Link %% $p(x)$ a coefficienti%% link %% reali%% link %%, se un [numero complesso](Numeri%20complessi.md#^definizione-numero-complesso) $z \in \mathbb{Z}$ è una sua radice%% link %%, allora lo è anche il suo [coniugato](Numeri%20complessi.md#^definizione-coniugato-di-un-numero-complesso) $\overline z \in \mathbb{Z}$.
^proposizione-radice-complessa-e-suo-coniugato

> [!esempio]- Esempio: radice complessa e il suo coniugato
> 
> Consideriamo il polinomio%% link %% a coefficienti%% link %% reali%% link %%:
> 
> $$
> p(x) = x^2 - 2x + 2
> $$
> 
> Un uccellino ci ha suggerito che $z = 1+i$ è una sua radice%% link %% di $p(x)$, quindi verifichiamo che anche il suo [coniugato](Numeri%20complessi.md#^definizione-coniugato-di-un-numero-complesso) $\overline z = 1-i$ sia una radice%% link %%. Sostituendo otteniamo:
> 
> $$
> \begin{align*}
> p(1-i) &= (1-i)^2 - 2(1-i) + 2 \\
> &= 1 - 2i + i^2 - 2 + 2i + 2 \\
> &= 1 - 2i - 1 - 2 + 2i + 2 \\
> &= 0.
> \end{align*}
> $$
> 
> Anche $\overline z=1-i$ è quindi una radice%% link %% di $p(x)$, verificando così la [proposizione](Numeri%20complessi.md#^proposizione-radice-complessa-e-suo-coniugato).

%% 
Dimostrazione pagg. 32-33 martelli
%%

Possiamo dedurre una fattorizzazione%% Link %% per i polinomi%% link %% a coefficienti%% link %% reali%% link %% (come abbiamo fatto per quelli a coefficienti%% link %% [complessi](Numeri%20complessi.md#^definizione-numero-complesso) nel [corollario 2](Numeri%20complessi.md#^corollario-2-del-teorema-fondamentale-dell-algebra)) in fattori%% link %% di grado%% link %% $1$ e $2$: i fattori di grado $2$ hanno radici%% link %% [complesse](Numeri%20complessi.md#^definizione-numero-complesso) $z$, mentre quelli di grado $1$ hanno radici%% link %% reali%% link %%.

> [!proposizione]+ Proposizione: fattorizzazione di un polinomio a coefficienti reali
> 
> Un polinomio%% link %% a coefficienti%% link %% reali%% link %% si può riscrivere come
> 
> $$
> p(x) = q_1(x) q_2(x) \ldots q_m(x) \cdot (x-x_1)(x-x_2) \ldots (x-x_n)
> $$
> 
> dove i $q_1(x),q_2(x),\ldots,q_m(x)$ sono polinomi%% link %% a coefficienti%% link %% reali%% link %% di grado%% link %% $2$ con discriminante%% link %% negativo ($\Delta < 0$) e gli $x_1,x_2,\ldots,x_n$ sono radici%% link %% reali%% link %% di $p(x)$ contate con molteplicità.
^proposizione-fattorizzazione-di-un-polinomio-a-coefficienti-reali

> [!esempio]- Esempio: fattorizzazione di un polinomio a coefficienti reali
> 
> Consideriamo il polinomio%% link %% a coefficienti%% link %% reali%% link %%:
> 
> $$
> p(x) = x^4 - 3x^3 + 3x^2 -3x + 2
> $$
> 
> Vogliamo riscriverlo come prodotto%% link %% di polinomi%% link %% di grado%% link %% $2$ con discriminante%% link %% negativo e di polinomi di primo grado associati alle radici%% link %% reali%% link %%.
> 
> Sappiamo grazie a un uccellino che le radici reali sono $x_1 = 1$ e $x_2 = 2$ e, dividendo $p(x)$ per $(x-1)(x-2)$, otteniamo $(x^2+1)$ che sarà proprio il polinomio di grado $2$ con discriminante%% link %% negativo che stavamo cercando.
> 
> Possiamo quindi riscrivere $p(x)$ come
> 
> $$
> p(x)=(x^2+1) \cdot (x-1)(x-2)
> $$
> 
> e verificare che ciò corrisponde al polinomio di partenza:
> 
> $$
> \begin{align*}
> p(x) &= (x^2+1) \cdot (x-1)(x-2) \\
> &= (x^2 + 1) \cdot (x^2 - 2x - x + 2) \\
> &= (x^2 + 1) \cdot (x^2 - 3x + 2) \\
> &= x^4 - 3x^3 + 2x^2 + x^2 - 3x + 2 \\
> &= x^4 - 3x^3 + 3x^2 - 3x + 2
> \end{align*}
> $$
> 
> Abbiamo così verificato la [proposizione](Numeri%20complessi.md#^proposizione-fattorizzazione-di-un-polinomio-a-coefficienti-reali).

%% 
Dimostrazione pag. 33 martelli
%%

Grazie alla [proposizione di prima](Numeri%20complessi.md#^proposizione-radice-complessa-e-suo-coniugato), abbiamo capito che in ogni polinomio%% link %% $p(x)$ a coefficienti%% Link %% reali%% link %% le radici%% link %% [complesse](Numeri%20complessi.md#^definizione-numero-complesso) non reali%% link %% sono accoppiate, nel senso che per ogni radice $z \in \mathbb{C} \setminus \mathbb{R}$ esisterà un'altra radice $\overline z \in \mathbb{C} \setminus \mathbb{R}$ che corrisponde al suo [coniugato](Numeri%20complessi.md#^definizione-coniugato-di-un-numero-complesso). Possiamo dedurre quindi il fatto seguente.

> [!proposizione]+ Proposizione: polinomio di grado dispari ha almeno una radice reale
> 
> Un polinomio%% link %% $p(x)$ a coefficienti%% Link %% reali%% link %% di grado%% link %% dispari ha sempre almeno una radice%% link %% reale%% link %%.

> [!dimostrazione]- Dimostrazione: polinomio di grado dispari ha almeno una radice reale
> 
> Se il polinomio%% link %% $p(x)$ ha grado%% link %% $n$ dispari, per il [corollario 1 del teorema fondamentale dell'algebra](Numeri%20complessi.md#^corollario-1-del-teorema-fondamentale-dell-algebra) ha esattamente $n$ radici%% link %% [complesse](Numeri%20complessi.md#^definizione-numero-complesso) contate con molteplicità.
> 
> Di queste, un numero pari non sono reali%% link %% perché per ogni radice $z \in \mathbb{C} \setminus \mathbb{R}$ esisterà un'altra radice $\overline z \in \mathbb{C} \setminus \mathbb{R}$ che corrisponde al suo [coniugato](Numeri%20complessi.md#^definizione-coniugato-di-un-numero-complesso).
> 
> Di conseguenza, rimuovendo dalle $n$ radici dispari queste coppie di radici, ne rimarrà almeno una reale%% link %%.
> 
> $\blacksquare$

%% 
Osservazione 1.4.14 pag. 33 Martelli
%%

---

> [!fonti]+ Fonti
> 
> - 📚 Bruno Martelli, _Geometria e algebra lineare_, autopubblicato, 2025:
> 	- Capitolo 1 - _Nozioni preliminari_:
> 		- 1.4 - _Numeri complessi_.
