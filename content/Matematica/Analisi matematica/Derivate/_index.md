---
title: Derivate
---

> [!premessa]+ Premessa
> 
> Ciao! Se è la prima volta che capiti su questo sito, ti consiglio di consultare la [pagina principale](index.md) di questo cosiddetto _Giardino Digitale_ per scoprire meglio cos'è e come navigarlo.
> 
> Lo stato di questa nota è al momento: 🔴 <font color="#FF7F7F">_Bozza_</font>.

%% 
in realtà è **Calcolo differenziale**
%%

---

Proviamo a introdurre il concetto di _derivata_%% link %%, uno dei concetti fondamentali dell'analisi matematica%% link %%, partendo da un concetto molto semplice: la _pendenza_ di un grafico%% link %%.

# 1 - Pendenza di un grafico e introduzione alle derivate

<!--
Prendendo una [funzione](Matematica/Teoria%20degli%20insiemi/Funzioni/_index.md#^definizione-funzione) $f$ qualsiasi, possiamo definire intuitivamente la _pendenza_ come l'inclinazione del grafico della funzione: per esempio. nel caso delle [funzioni lineari](Funzioni%20elementari.md#^definizione-funzione-lineare), il cui grafico%% link %% è una retta%% link %%, [la pendenza è costante e uguale al coefficiente $m$](Funzioni%20elementari.md#^teorema-della-pendenza-costante-della-funzione-lineare).

Diversa è però la situazione per le [funzioni](Matematica/Teoria%20degli%20insiemi/Funzioni/_index.md#^definizione-funzione) non [lineari](Funzioni%20elementari.md#^definizione-funzione-lineare): per esempio, nel caso della [funzione](Matematica/Teoria%20degli%20insiemi/Funzioni/_index.md#^definizione-funzione) ${\color{#FF7F7F} f(x) = \log_2 x - 1 }$, la _pendenza_ varia in base al punto in cui la misuriamo: la pendenza della tangente%% link %% ${\color{#7FFF7F} t_1 }$ al punto%% link %% ${\color{#7FFF7F} P_1(-1,1) }$ sarà sicuramente maggiore della pendenza della tangente%% link %% ${\color{#7F7FFF} t_2 }$ al punto%% link %% ${\color{#7F7FFF} P_2(4,1) }$.

%% 
fare grafico
%%

Possiamo quindi notare come il concetto di _pendenza_ è legato al singolo punto%% link %% del grafico%% link %%: a seconda del punto%% link %% cambia la pendenza, quindi parleremo di _pendenza in un punto_.

Prendiamo ora la [funzione](Matematica/Teoria%20degli%20insiemi/Funzioni/_index.md#^definizione-funzione) ${\color{#7FFFFF} f(x) = \ln(1 + 2x) }$ e supponiamo di voler determinare la pendenza di ${\color{#7FFFFF} f(x) }$ nel punto%% Link %% ${\color{#FFFF7F} P(0,0) }$.

%% mettere grafico %%

Ora ingrandiamo il grafico facendo uno zoom attorno al punto ${\color{#FFFF7F} P(0,0) }$ in cui vogliamo determinare la pendenza: se ci restringiamo alla finestra $[-0.10;0.13] \times [-0.2;0.2]$ otteniamo questo grafico:

%% 
mettere grafico
%%

Possiamo notare una cosa molto interessante: se ingrandiamo abbastanza troviamo che il grafico è praticamente rettilineo: si ha quindi che, ingrandendo il grafico di ${\color{#7FFFFF} f(x) }$
-->

Se prendiamo il [quoziente di Newton](Matematica/Teoria%20degli%20insiemi/Funzioni/_index.md#^definizione-quoziente-di-newton) e sfruttiamo la nozione di [limite](Matematica/Analisi%20matematica/Limiti/_index.md#^definizione-limite) per far tendere un punto%% link %% verso l'altro, in modo da diminuire quanto più possibile la distanza tra i due fino a farli combaciare in un unico punto%% link %%, la retta secante i due punti diventerà tangente a quell'unico punto e diventerà proprio il valore della pendenza in quel punto.

> [!definizione]+ Definizione: pendenza di una funzione in un punto
> 
> Data una [funzione](Matematica/Teoria%20degli%20insiemi/Funzioni/_index.md#^definizione-funzione) $f \colon \text{dom}(f) \to \mathbb{R}$ e un punto%% link %% $x_0 \in \text{dom}(f)$, la **pendenza di $f$ in $x_0$**, indicata con $p_f(x_0)$, è il [limite](Matematica/Analisi%20matematica/Limiti/_index.md#^definizione-limite) per $x \to x_0$ del [quoziente di Newton](Matematica/Teoria%20degli%20insiemi/Funzioni/_index.md#^definizione-quoziente-di-newton):
> 
> $$
> p_f(x_0) \overset{\text{def}}{=} \lim_{x \to x_0} \dfrac{\Delta f}{\Delta x} = \lim_{x \to x_0} \dfrac{f(x) - f(x_0)}{x - x_0}
> $$
^definizione-pendenza-di-una-funzione-in-un-punto

%%
Esempio: $f(x)=\ln(1+2x)$

Abbiamo che:
- $f$ è definita se e solo se $1 + 2x > 0$ quindi $x > - \dfrac{1}{2}$
- $f(0) = \ln 1 = 0$

proviamo a calcolare la pendenza in $0$ (ammesso che esista!)

$$
p_f(0) = \lim_{x_2 \to 0} \dfrac{\Delta f}{\Delta x} = \lim_{x_2 \to 0} \dfrac{f(x_2) - f(0)}{x_2 - 0} = \lim_{x_2 \to 0} \dfrac{\ln(1 + 2x_2)}{x_2}
$$

Provando a calcolare i valori vicini a $x_2 = 0$ possiamo notare come $p_f(0)$ tenda a 2. Ma è effettivamente uguale a 2? 

Provando a ingrandire il grafico, possiamo notare come vicino a $O(0,0)$ il grafico di $f$ "diventa" il grafico di $y=2x$, quindi effettivamente $p_f(0)=2$. 

In questo caso ingrandendo il grafico di $f$ vicino a $P(x_0, f(x_0))$ vediamo un grafico sempre più simile a una retta., per questo possiamo dire che è localmente dritta
%%

> [!esempio]- Esempio di pendenza non definita
> 
> Prendiamo la [funzione](Matematica/Teoria%20degli%20insiemi/Funzioni/_index.md#^definizione-funzione) del valore assoluto%% link %% di $x$, definità così:
> 
> $$
> f(x) = |x| = \begin{cases}
> x & \text{se } x \ge 0 \\
> -x & \text{se } x < 0
> \end{cases}
> $$
> 
> Proviamo a calcolare la [pendenza](Matematica/Analisi%20matematica/Derivate/_index.md#^definizione-pendenza-di-una-funzione-in-un-punto) $p_f(0)$:
> - Se proviamo a prendere il [limite destro](Matematica/Analisi%20matematica/Limiti/_index.md#^definizione-limite-destro) (cioè $x > 0$):
> 	$$
> 	\lim_{x \to x_0^+} \dfrac{\Delta f}{\Delta x} = 1
> 	$$
> - Se proviamo a prendere il [limite sinistro](Matematica/Analisi%20matematica/Limiti/_index.md#^definizione-limite-sinistro) (cioè $x < 0$):
> 	$$
> 	\lim_{x \to x_0^-} \dfrac{\Delta f}{\Delta x} = -1
> 	$$
> 
> Dal momento che i due limiti laterali%% link %% differiscono e non sapremmo quale dei due scegliere, possiamo concludere che la [pendenza](Matematica/Analisi%20matematica/Derivate/_index.md#^definizione-pendenza-di-una-funzione-in-un-punto) in questo punto non è definita.
^esempio-di-pendenza-non-definita

> [!definizione]+ Definizione: funzione localmente dritta in un punto
> 
> Data una [funzione](Matematica/Teoria%20degli%20insiemi/Funzioni/_index.md#^definizione-funzione) $f \colon \text{dom}(f) \to \mathbb{R}$ e un punto%% link %% $x_0 \in \text{dom}(f)$, diciamo che **$f$ è localmente dritta in $x_0$** se è possibile definire la [pendenza](Matematica/Analisi%20matematica/Derivate/_index.md#^definizione-pendenza-di-una-funzione-in-un-punto) in $x_0$ (cioè $p_f(x_0)$).
^definizione-funzione-localmente-dritta-in-un-punto

> [!esempio]- Esempio di funzione non localmente dritta in un punto
> 
> [Riprendendo l'esempio della funzione $f(x) = |x|$](Matematica/Analisi%20matematica/Derivate/_index.md#^esempio-di-pendenza-non-definita), dato che la [pendenza](Matematica/Analisi%20matematica/Derivate/_index.md#^definizione-pendenza-di-una-funzione-in-un-punto) in $x_0$ non è definita, possiamo dire che $f$ **non** è [localmente dritta](Matematica/Analisi%20matematica/Derivate/_index.md#^definizione-funzione-localmente-dritta-in-un-punto) in $0$.

> [!definizione]+ Definizione: retta tangente a una funzione in un punto
> 
> Data una [funzione](Matematica/Teoria%20degli%20insiemi/Funzioni/_index.md#^definizione-funzione) $f \colon \text{dom}(f) \to \mathbb{R}$ e un punto%% link %% $x_0 \in \text{dom}(f)$, diciamo che la **retta tangente a $f$ in $x_0$** è la retta passante%% link %% per il punto%% link %% $P(x_0, f(x_0))$ e con [pendenza](Matematica/Analisi%20matematica/Derivate/_index.md#^definizione-pendenza-di-una-funzione-in-un-punto) $p_f(x_0)$.
^definizione-retta-tangente-a-una-funzione-in-un-punto

## Derivabilità di una funzione in un punto

> [!definizione]+ Definizione: derivabilità e derivata (prima) di una funzione in un punto
> 
> Data una [funzione](Matematica/Teoria%20degli%20insiemi/Funzioni/_index.md#^definizione-funzione) $f \colon \text{dom}(f) \to \mathbb{R}$ e un [punto interno](Topologia%20dei%20reali.md#^definizione-punto-interno) $x_0 \in \text{dom}(f)$ a $\text{dom}(f)$, diciamo che **$f$ è derivabile in $x_0$** se esiste finito%% link %% il [limite](Matematica/Analisi%20matematica/Limiti/_index.md#^definizione-limite)
> 
> $$
> \lim_{x \to x_0} \dfrac{f(x) - f(x_0)}{x - x_0}
> $$
> 
> e in tal caso denotiamo questo [limite](Matematica/Analisi%20matematica/Limiti/_index.md#^definizione-limite) con uno dei seguenti simboli:
> 
> $$
> f'(x_0), \quad Df(x_0), \quad \dfrac{df}{dx}(x_0), \quad \dot f(x_0)
> $$
> 
> e lo chiamiamo **derivata (prima) di $f$ in $x_0$**.
^definizione-derivabilita-e-derivata-prima-di-una-funzione-in-un-punto

> [!definizione]+ Definizione: derivabilità di una funzione in un sottoinsieme del dominio
> 
> Data una [funzione](Matematica/Teoria%20degli%20insiemi/Funzioni/_index.md#^definizione-funzione) $f \colon \text{dom}(f) \to \mathbb{R}$ e un [sottoinsieme](Matematica/Teoria%20degli%20insiemi/_index.md#^definizione-insieme) $A \subseteq \text{dom}(f)$ (con $A \ne \emptyset$), diciamo che **$f$ è derivabile in $A$** se è [derivabile](Matematica/Analisi%20matematica/Derivate/_index.md#^definizione-derivabilita-e-derivata-prima-di-una-funzione-in-un-punto) in ogni punto%% link %% di $A$.
^definizione-derivabilita-di-una-funzione-in-un-sottoinsieme-del-dominio

%% 
Il quoeiente è detto rapporto incrementale di f in x0 e rappresenta la variazione relativa di f rispetto a quella della variabile indipendente x nel passare da x0 a x. Il limite di questo rapporto incrememntale, se esiste in R, è la derivata di f in x0. Quindi rappresenta la variazione relativa di f rispetto a quella dela variabile indipendente x nel passare da x0 a x, quando x tende a x0.
%%

Se il [limite](Matematica/Analisi%20matematica/Limiti/_index.md#^definizione-limite) è $\pm \infty$ o non esiste, allora $f$ non è derivabile in $x_0$. %% integrare nella definizione %%

Talvolta il limite del rapporto incrementale è scritto nel seguente modo:

$$
\lim_{x \to x_0} \dfrac{f(x)-f(x_0)}{x - x_0} = \lim_{h \to 0} \dfrac{f(x_0 + h) - f(x_0)}{h}
$$

con $h = x - x_0$.

%% 
osservazione 1.2 pag. 238-239 lancelotti
%%

%% 
osservazione 1.4 ed esempio 1.5 pagg. 239-241
%%

> [!teorema]+ Teorema del legame fra la continuità e la derivabilità
> 
> Data una [funzione](Matematica/Teoria%20degli%20insiemi/Funzioni/_index.md#^definizione-funzione) $f \colon \text{dom}(f) \to \mathbb{R}$ e un [punto interno](Topologia%20dei%20reali.md#^definizione-punto-interno) $x_0 \in \text{dom}(f)$ a $\text{dom}(f)$, se $f$ è [derivabile](Matematica/Analisi%20matematica/Derivate/_index.md#^definizione-derivabilita-e-derivata-prima-di-una-funzione-in-un-punto) in $x_0$ allora $f$ è [continua](Funzioni%20continue.md#^definizione-funzione-continua) in $x_0$.
^teorema-del-legame-fra-la-continuita-e-la-derivabilita

%% 
dimostrazione pag. 242 lancelotti
%%

> [!osservazione]+ Osservazione: derivabilità implica continuità ma non il contrario
> 
> Per il [teorema del legame fra la continuità e la derivabilità](Matematica/Analisi%20matematica/Derivate/_index.md#^teorema-del-legame-fra-la-continuita-e-la-derivabilita), la [derivabilità](Matematica/Analisi%20matematica/Derivate/_index.md#^definizione-derivabilita-e-derivata-prima-di-una-funzione-in-un-punto) implica automaticamente la [continuità](Funzioni%20continue.md#^definizione-funzione-continua), ma non è vero il contrario: per esempio, la [funzione](Matematica/Teoria%20degli%20insiemi/Funzioni/_index.md#^definizione-funzione) $f(x) = |x|$ è [continua](Funzioni%20continue.md#^definizione-funzione-continua) ma non [derivabile](Matematica/Analisi%20matematica/Derivate/_index.md#^definizione-derivabilita-e-derivata-prima-di-una-funzione-in-un-punto) in $0$.
> 
> In particolare, abbiamo che per contrapposizione%% link %% se una [funzione](Matematica/Teoria%20degli%20insiemi/Funzioni/_index.md#^definizione-funzione) non è [continua](Funzioni%20continue.md#^definizione-funzione-continua) allora non è neanche [derivabile](Matematica/Analisi%20matematica/Derivate/_index.md#^definizione-derivabilita-e-derivata-prima-di-una-funzione-in-un-punto): riprendendo l'esempio precedente della funzione $f(x) = \text{sgn}(x)$%% link %%, poiché $f$ non è [continua](Funzioni%20continue.md#^definizione-funzione-continua) in $0$, allora possiamo immediatamente concludere che $f$ non è [derivabile](Matematica/Analisi%20matematica/Derivate/_index.md#^definizione-derivabilita-e-derivata-prima-di-una-funzione-in-un-punto) in $0$.

> [!proposizione]+ Proposizione: in una derivata la variazione è un infinitesimo
> 
> Se una [funzione](Matematica/Teoria%20degli%20insiemi/Funzioni/_index.md#^definizione-funzione) $f$ è [derivabile](Matematica/Analisi%20matematica/Derivate/_index.md#^definizione-derivabilita-e-derivata-prima-di-una-funzione-in-un-punto) in $x_0$, ossia
> 
> $$
> \lim_{x \to x_0} \dfrac{f(x) - f(x_0)}{x - x_0} = f'(x_0) \in \mathbb{R}
> $$
> 
> allora la variazione%% link %% di $f$ nel passaggio da $x_0$ a $x$
> - è un [infinitesimo del primo ordine](Infiniti%20e%20infinitesimi.md#^definizione-infinitesimo-di-ordine-alfa-rispetto-all-infinitesimo-campione-u) se $f'(x_0) \ne 0$ o
> - è un [infinitesimo di ordine superiore al primo](Infiniti%20e%20infinitesimi.md#^definizione-infinitesimo-di-ordine-superiore-o-inferiore-all-ordine-alpha-rispetto-all-infinitesimo-campione-u) se $f'(x_0) = 0$
> rispetto all'[infinitesimo campione](Infiniti%20e%20infinitesimi.md#^definizione-infiniti-e-infinitesimi-campione) $u(x) = |x - x_0|$ per $x \to x_0$ con [parte principale](Infiniti%20e%20infinitesimi.md#^definizione-infinitesimo-di-ordine-alfa-rispetto-all-infinitesimo-campione-u) $f'(x_0)(x - x_0)$:
> 
> $$
> f(x) - f(x_0) = f'(x_0)(x - x_0) + o(|x - x_0|) \text{ per } x \to x_0
> $$
^proposizione-in-una-derivata-la-variazione-e-un-infinitesimo

> [!dimostrazione]- Dimostrazione: in una derivata la variazione è un infinitesimo
> 
> Dimostriamo che [in una funzione derivabile la variazione di $f$ nel passaggio da $x_0$ a $x$ è un infinitesimo](Matematica/Analisi%20matematica/Derivate/_index.md#^proposizione-in-una-derivata-la-variazione-e-un-infinitesimo).
> 
> Analizziamo prima il caso in cui $f'(x_0) \ne 0$: se osserviamo la [definizione di _infinitesimo di ordine $\alpha$ rispetto all'infinitesimo campione $u(x)$_](Infiniti%20e%20infinitesimi.md#^definizione-infinitesimo-di-ordine-alfa-rispetto-all-infinitesimo-campione-u), abbiamo che
> 
> $$
> \displaystyle\lim_{x \to x_0} \dfrac{f(x)}{[u(x)]^\alpha} = l \in \mathbb{R} \setminus \{ 0 \}
> $$
> 
> Nel nostro caso:
> - $f(x)$ corrisponde a $f(x) - f(x_0)$,
> - $[u(x)]^\alpha$ è l'[infinitesimo campione](Infiniti%20e%20infinitesimi.md#^definizione-infiniti-e-infinitesimi-campione) $|x - x_0|$ con ordine $\alpha = 1$ e
> - $l$ è $f'(x_0)$ che, in questo caso, è diverso da $0$, quindi rispettiamo la condizione $l \in \mathbb{R} \setminus \{ 0 \}$.
> 
> Sostituendo quindi i termini della [definizione](Infiniti%20e%20infinitesimi.md#^definizione-infinitesimo-di-ordine-alfa-rispetto-all-infinitesimo-campione-u) (e, in particolare, utilizzando la terza formula, quella con l'[$o$-piccolo](Infiniti%20e%20infinitesimi.md#^definizione-o-piccolo)), otteniamo
> 
> $$
> f(x) - f(x_0) =f'(x_0)(|x - x_0|)^1 + o((|x - x_0|)^1) \text{ per } x \to x_0
> $$
> 
> Possiamo quindi concludere che in questo caso la variazione%% link %% di $f$ nel passaggio da $x_0$ a $x$ è un [infinitesimo del primo ordine](Infiniti%20e%20infinitesimi.md#^definizione-infinitesimo-di-ordine-alfa-rispetto-all-infinitesimo-campione-u) se $f'(x_0) \ne 0$.
> 
> Nel caso in cui $f'(x_0) = 0$, abbiamo che
> 
> $$
> \lim_{x \to x_0} \frac{f(x) - f(x_0)}{x - x_0} = 0
> $$
> 
> Cioè $f(x) - f(x_0)$ è [$o$-piccolo](Infiniti%20e%20infinitesimi.md#^definizione-o-piccolo) di $x - x_0$:
> 
> $$
> f(x) - f(x_0) = o(x - x_0)
> $$
> 
> Ciò implica che [$f(x) - f(x_0)$ è un infinitesimo di ordine superiore al primo rispetto all'infinitesimo campione $u(x) = |x - x_0|$ per $x -> x_0$](Infiniti%20e%20infinitesimi.md#^definizione-infinitesimo-di-ordine-superiore-o-inferiore-all-ordine-alpha-rispetto-all-infinitesimo-campione-u).
> 
> In entrambi i casi, è corretto riassumere il tutto nella formula
> 
> $$
> f(x) - f(x_0) = f'(x_0)(x - x_0) + o(|x - x_0|) \text{ per } x \to x_0
> $$
> 
> perché:
> - Se $f'(x_0) \ne 0$, questa formula è letteralmente la [terza formula della definizione di _infinitesimo di ordine $\alpha$ rispetto all'infinitesimo campione $u(x)$_](Infiniti%20e%20infinitesimi.md#^definizione-infinitesimo-di-ordine-alfa-rispetto-all-infinitesimo-campione-u) che abbiamo scritto poco fa.
> - Se $f'(x_0) = 0$, otteniamo la [terza formula della definizione di _infinitesimo di ordine superiore al primo rispetto all'infinitesimo campione $u(x)$_](Infiniti%20e%20infinitesimi.md#^definizione-infinitesimo-di-ordine-superiore-o-inferiore-all-ordine-alpha-rispetto-all-infinitesimo-campione-u).
> 
> $\blacksquare$

%% 
scrivere meglio queste definizioni per far capire le formule
%%

%% 
Capire come integrare i valori assoluti in $x - x_0$ per rispecchiare la formula dell'infinitesimo campione
%%

%% 
Osservazione: il termine $f(x) = f(x_0) + f'(x_0)(x - x_0)$ è il second membro dell'equazione della retta tangente al grafico di $f$ in $(x_0, f(x_0))$ (vedi interpretazione geometrica di prima)- Questa uguaglianza ci dice che per $x \to x_0$ la funzione $f$ è approssimabile con il polinomio di primo grado $f(x_0) + f'(x_0)(x - x_0)$, ovvero ce il grafico di $f$ è approssimabile con la retta tangente al grafico di $f$ in $(x_0, f(x_0))$, a meno di termini che sono infinitesimi di ordine superiore al primo.
%%

%% 
\# Derivate delle funzioni elementari

trasformare tutte in proposizioni da dimostrare, pagg. 243-245:

- $\forall x \in \mathbb{R}.(f(x) = c \in \mathbb{R} \implies f'(x) = 0)$
- $\forall x,n \in \mathbb{R}.(f(x) = x^n \implies f'(x) = nx^{n-1})$

ecc.
%%

<!--

## Interpretazione cinematica della derivata

Proviamo ora a dare un'interpretazione cinematica della [derivata di una funzione in un punto](content/Matematica/Analisi%20matematica/Derivate/_index.md#^definizione-derivabilita-e-derivata-prima-di-una-funzione-in-un-punto)%% spiegare cos'è la cinematica %%.

Consideriamo un oggetto puntiforme che si muove di moto rettilineo. La sua posizione sulla retta del moto è misurata rispetto a un punto fissato, detto _origine_. A destra dell'origine la posizione sarà positiva, a sinistra negativa.

La posizione del punto viene misurata a istanti diversi attraverso la funzione $s(t)$ che determina la posizione del punto al tempo $t$.

Abbiamo il grafico dell'oggetto così:
- $s(0)=1$
- $s(3)=3$
- $s(6) = -3$

Quoziente di Newton = velocità media

Derivata in un punto = velocità istantanea

-->

<!--

## Interpretazione demografica della derivata

Ora intrepretiamo la derivata dal punto di vista demografico come tasso di crescita di una popolazione.

Funzione $N(t)$ è il numero di individui al tempo $t$ (con $N(t) \ge 0$ perché non può essere negativa una popolazione)

Quoziente di Newton = tasso medio di crescita della popolazione
Derivata in un punto = tasso istantaneo di crescita della popolazione in un punto

- $N(0) = 1$
- $N(10) = 2$
- $N(20) = 1$
- poi continua a diminuire fino a estinguersi

stimare tasso di crescita in (20,1) = -1/6 milioni all'ano

tabella riassuntiva delle varie interpretazioni con quoziente di Newton e derivata
-->


# 2 - Differenziale

> [!definizione]+ Definizione: differenziale di una funzione
> 
> Data una [funzione](Matematica/Teoria%20degli%20insiemi/Funzioni/_index.md#^definizione-funzione) $f \colon \text{dom}(f) \to \mathbb{R}$ e un [punto interno](Topologia%20dei%20reali.md#^definizione-punto-interno) $x_0 \in \text{dom}(f)$ a $\text{dom}(f)$, diciamo che **$f$ è differenziabile in $x_0$** se $f$ è [derivabile](Matematica/Analisi%20matematica/Derivate/_index.md#^definizione-derivabilita-e-derivata-prima-di-una-funzione-in-un-punto) in $x_0$ e in tal caso chiamiamo **differenziale di $f$ in $x_0$** la funzione lineare%% link %% $df(x_0) \colon \mathbb{R} \to \mathbb{R}$ definita da
> 
> $$
> df(x_0)(x) = f'(x_0)x
> $$
^definizione-differenziale-di-una-funzione

Quindi il [differenziale](Matematica/Analisi%20matematica/Derivate/_index.md#^definizione-differenziale-di-una-funzione) di $f$ in $x_0$ è una [funzione](Matematica/Teoria%20degli%20insiemi/Funzioni/_index.md#^definizione-funzione) il cui grafico%% link %% è una retta%% link %% passante per l'origine $O(0;0)$%% ink %% con coefficiente angolare%% Link %% $f'(x_0)$.

Posto $dx \colon \mathbb{R} \to \mathbb{R}$ la funzione lineare identica%% link %%, cioè la funzione tale che $dx(x) = x$ per ogni $x \in \mathbb{R}$, allora il [differenziale](Matematica/Analisi%20matematica/Derivate/_index.md#^definizione-differenziale-di-una-funzione) di $f$ in $x_0$ diventa

$$
df(x_0) = f'(x_0)dx
$$

Infatti

$$
\forall x \in \mathbb{R}. \left( df(x_0)(x) = f'(x_0) \cdot \underbrace{dx(x)}_{=x} = f'(x_0)x \right) 
$$

> [!esempio]- Esempi di differenziali
> 
> - $f(x) = x^2 \implies df(x) = f'(x)dx = 2xdx$
> - $f(x) = \sin x \implies df(x) = f'(x)dx = \cos x\ dx$
> - $f(x) = e^x \implies df(x) = f'(x)dx = e^xdx$
> - $f(x) = \log x \implies df(x) = f'(x)dx = \dfrac{1}{x}dx$

# 3 - Derivate laterali

> [!definizione]+ Definizione: derivate laterali di una funzione
> 
> Data una [funzione](Matematica/Teoria%20degli%20insiemi/Funzioni/_index.md#^definizione-funzione) $f \colon \text{dom}(f) \to \mathbb{R}$, un [punto interno](Topologia%20dei%20reali.md#^definizione-punto-interno) $x_0 \in \text{dom}(f)$ a $\text{dom}(f)$ e un $\delta > 0$ tale che $[x_0;x_0 + \delta) \subseteq \text{dom}(f)$, diciamo che **$f$ è derivabile da destra in $x_0$** se esiste il [limite](Matematica/Analisi%20matematica/Limiti/_index.md#^definizione-limite)
> 
> $$
> \lim_{x \to x_0^+} \dfrac{f(x) - f(x_0)}{x - x_0} = l \in \mathbb{R}
> $$
> 
> e in tal caso denotiamo questo [limite](Matematica/Analisi%20matematica/Limiti/_index.md#^definizione-limite) con $D^+f(x_0)$ e lo chiamiamo **derivata destra di $f$ in $x_0$**.
> 
> Se esiste un $\delta > 0$ tale che $(x_0 - \delta, x_0] \subseteq \text{dom}(f)$, diciamo che **$f$ è derivabile da sinistra in $x_0$** se esiste il [limite](Matematica/Analisi%20matematica/Limiti/_index.md#^definizione-limite)
> 
> $$
> \lim_{x \to x_0^-} \dfrac{f(x) - f(x_0)}{x - x_0} = l \in \mathbb{R}
> $$
> 
> e in tal caso denotiamo questo [limite](Matematica/Analisi%20matematica/Limiti/_index.md#^definizione-limite) con $D^-f(x_0)$ e lo chiamiamo **derivata sinistra di $f$ in $x_0$**.
> 
> Le derivate destra e sinistra sono anche dette **derivate laterali**.
^definizione-derivate-laterali-di-una-funzione

> [!esempio]- Esempio di derivate laterali di una funzione
> 
> Consideriamo la [funzione](Matematica/Teoria%20degli%20insiemi/Funzioni/_index.md#^definizione-funzione) $f(x) = |x|$, abbiamo visto%% Link %% che è [derivabile](Matematica/Analisi%20matematica/Derivate/_index.md#^definizione-derivabilita-e-derivata-prima-di-una-funzione-in-un-punto) in ogni $x \ne 0$ e che non è [derivabile](Matematica/Analisi%20matematica/Derivate/_index.md#^definizione-derivabilita-e-derivata-prima-di-una-funzione-in-un-punto) in $0$. Inoltre si ha che
> 
> $$
> \begin{array}{}
> \displaystyle\lim_{x \to 0^+} \dfrac{f(x) - f(0)}{x - 0} = \lim_{x \to 0^+} \dfrac{|x|}{x} = \lim_{x \to 0^+} \dfrac{x}{x} = 1 \implies D^+f(0)=1 \\
> \displaystyle\lim_{x \to 0^-} \dfrac{f(x) - f(0)}{x - 0} = \lim_{x \to 0^-} \dfrac{|x|}{x} = \lim_{x \to 0^-} \dfrac{-x}{x} = -1 \implies D^-f(0)=-1 \\
> \end{array}
> $$

%% 
Osservazione 1.14 pag. 247 Lancelotti
%%

> [!teorema]+ Teorema del legame fra la derivata e le derivate laterali
> 
> Data una [funzione](Matematica/Teoria%20degli%20insiemi/Funzioni/_index.md#^definizione-funzione) $f \colon \text{dom}(f) \to \mathbb{R}$ e un [punto interno](Topologia%20dei%20reali.md#^definizione-punto-interno) $x_0 \in \text{dom}(f)$ a $\text{dom}(f)$. Se esistono le [derivate laterali](Matematica/Analisi%20matematica/Derivate/_index.md#^definizione-derivate-laterali-di-una-funzione) $D^+f(x_0)$ e $D^-f(x_0)$, allora $f$ è [continua](Funzioni%20continue.md#^definizione-funzione-continua) in $x_0$ e inoltre $f$ è [derivabile](Matematica/Analisi%20matematica/Derivate/_index.md#^definizione-derivabilita-e-derivata-prima-di-una-funzione-in-un-punto) in $x_0$ se e solo se $D^+f(x_0) = D^-f(x_0)$ e, in tal caso,
> 
> $$
> f'(x_0) = D^+f(x_0) = D^-f(x_0)
> $$

%% 
dimostrazione pag. 247 lancelotti
%%

> [!definizione]+ Definizione: derivabilità e derivata (prima) di una funzione
> 
> Data una [funzione](Matematica/Teoria%20degli%20insiemi/Funzioni/_index.md#^definizione-funzione) $f \colon \text{dom}(f) \to \mathbb{R}$, diciamo che **$f$ è derivabile** se è [derivabile](Matematica/Analisi%20matematica/Derivate/_index.md#^definizione-derivabilita-e-derivata-prima-di-una-funzione-in-un-punto) in ogni punto%% link %% del dominio%% link %% $\text{dom}(f)$ e, nei [punti di frontiera](Topologia%20dei%20reali.md#^definizione-punto-di-frontiera) appartenenti al dominio%% link %%, se sono [derivabili lateralmente](Matematica/Analisi%20matematica/Derivate/_index.md#^definizione-derivate-laterali-di-una-funzione).
> 
> In tal caso è definita una [funzione](Matematica/Teoria%20degli%20insiemi/Funzioni/_index.md#^definizione-funzione), detta **derivata (prima) di $f$**, denotata con $f'$ (oppure $Df$, $\dfrac{df}{dx}$ p $\dot f$) e definita come
> 
> $$
> \begin{align*}
> f' \colon \text{dom}(f) & \to \mathbb{R} \\
> x & \mapsto f'(x)
> \end{align*}
> $$
^definizione-derivabilita-e-derivata-prima-di-una-funzione

> [!esempio]- Esempio di derivabiità di una funzione
> 
> Consideriamo la [funzione](Matematica/Teoria%20degli%20insiemi/Funzioni/_index.md#^definizione-funzione) $f(x) = x^q$ con $q \in \mathbb{Q}^{> 0} \setminus \mathbb{N}$. Abbiamo che $\text{dom}(f) = [0, + \infty)$ e, per ogni $x > 0$, si ha che $f$ è [derivabile](Matematica/Analisi%20matematica/Derivate/_index.md#^definizione-derivabilita-e-derivata-prima-di-una-funzione-in-un-punto) in $x$ con $f'(x) = qx^{q-1}$. In $x=0$ si ha che
> 
> $$
> \lim_{x \to 0^+} \dfrac{f(x) - f(0)}{x} = \lim_{x \to 0^+} \dfrac{x^q}{x} = \lim_{x \to 0^+} x^{q-1} = \begin{cases}
> + \infty & \text{se } q < 1 \\
> 0 & \text{se } q > 1
> \end{cases}
> $$
> 
> Quindi $f$ è [derivabile da destra](Matematica/Analisi%20matematica/Derivate/_index.md#^definizione-derivate-laterali-di-una-funzione) in $0$ solo se $q > 1$ e in tal caso $D^+f(0) = 0$.

# 4 - Punti di non derivabilità

Introduciamo una classificazione per i punti di non derivabilità%% link %% di una [funzione](Matematica/Teoria%20degli%20insiemi/Funzioni/_index.md#^definizione-funzione), ossia per i punti%% link %% in cui $f$ è [continua](Funzioni%20continue.md#^definizione-funzione-continua) ma non [derivabile](Matematica/Analisi%20matematica/Derivate/_index.md#^definizione-derivabilita-e-derivata-prima-di-una-funzione).

> [!definizione]+ Definizione: punto angoloso
> 
> Data una [funzione](Matematica/Teoria%20degli%20insiemi/Funzioni/_index.md#^definizione-funzione) $f \colon \text{dom}(f) \to \mathbb{R}$ e un [punto interno](Topologia%20dei%20reali.md#^definizione-punto-interno) $x_0 \in \text{dom}(f)$ a $\text{dom}(f)$, diciamo che **$x_0$ è un punto angoloso per $f$** se esistono le [derivate laterali](Matematica/Analisi%20matematica/Derivate/_index.md#^definizione-derivate-laterali-di-una-funzione) $D^+f(x_0)$ e $D^-f(x_0)$ ma sono diverse.
^definizione-punto-angoloso

%% 
Osserviamo che per il teorema del legame fra la derivata e le derivate laterali $f$ è continua in $x_0$
%%

%% 
riprendere l'esempio della pendenza di $f(x) = |x|$
%%

> [!esempio]- Esempio di punto angoloso per $\color{#7F7FFF} f(x) =|x|$
> 
> Consideriamo la [funzione](Matematica/Teoria%20degli%20insiemi/Funzioni/_index.md#^definizione-funzione) $f(x) = |x|$: il punto%% link %% $x_0 = 0$ è [angoloso](Matematica/Analisi%20matematica/Derivate/_index.md#^definizione-punto-angoloso) per $f$, infatti le [derivate laterali](Matematica/Analisi%20matematica/Derivate/_index.md#^definizione-derivate-laterali-di-una-funzione) non coincidono:
> 
> $$
> D^+f(0) = 1 \ne -1 = D^-f(0)
> $$
^esempio-di-punto-angoloso-per-valore-assoluto-di-x

> [!osservazione]+ Osservazione: perché _punto angoloso_?
> 
> Osservando l'[esempio del punto angoloso per $f(x) = |x|$](Matematica/Analisi%20matematica/Derivate/_index.md#^esempio-di-punto-angoloso-per-valore-assoluto-di-x), possiamo notare che le semirette%% link %% tangenti%% link %% al grafico%% link %% nell'origine%% link %% $O(0,0)$ sono rispettivamente $y=-x$ e $y=x$ e formano tra loro un angolo retto%% link %%: risulta quindi giustificata la denominazione [_punto angoloso_](Matematica/Analisi%20matematica/Derivate/_index.md#^definizione-punto-angoloso).

%% 
esempio 1.20 di punto angoloso per funzione a tratti pagg. 248-249 lancelotti
%%

> [!definizione]+ Definizione: cuspide
> 
> Data una [funzione](Matematica/Teoria%20degli%20insiemi/Funzioni/_index.md#^definizione-funzione) $f \colon \text{dom}(f) \to \mathbb{R}$ e un [punto interno](Topologia%20dei%20reali.md#^definizione-punto-interno) $x_0 \in \text{dom}(f)$ a $\text{dom}(f)$, diciamo che **$x_0$ è una cuspide per $f$** se $f$ è [continua](Funzioni%20continue.md#^definizione-funzione-continua) in $x_0$ e
> 
> $$
> \lim_{x \to x_0^+} \dfrac{f(x) - f(x_0)}{x - x_0} = \pm \infty \ne \mp \infty = \lim_{x \to x_0^-} \dfrac{f(x) - f(x_0)}{x - x_0}
> $$
> 
> cioè i [limiti laterali](Matematica/Analisi%20matematica/Limiti/_index.md#^definizione-limiti-laterali) sono entrambi uguali a $\infty$ ma di segno opposto: se uno vale $+ \infty$, l'altro deve valere $- \infty$.
^definizione-cuspide

%% 
In questo caso è necessaria l'ipotesi di continuità di $f$ in $x_0$
CHE SIGNIFICA?
%%

%% 
esempio 1.21 pag. 249
%%

> [!definizione]+ Definizione: punto di flesso a tangente verticale
> 
> Data una [funzione](Matematica/Teoria%20degli%20insiemi/Funzioni/_index.md#^definizione-funzione) $f \colon \text{dom}(f) \to \mathbb{R}$ e un [punto interno](Topologia%20dei%20reali.md#^definizione-punto-interno) $x_0 \in \text{dom}(f)$ a $\text{dom}(f)$, diciamo che **$x_0$ è un punto di flesso a tangente verticale per $f$** se $f$ è [continua](Funzioni%20continue.md#^definizione-funzione-continua) in $x_0$ e
> 
> $$
> \lim_{x \to x_0^+} \dfrac{f(x) - f(x_0)}{x - x_0} = \lim_{x \to x_0^-} \dfrac{f(x) - f(x_0)}{x - x_0} = \pm \infty
> $$
> 
> cioè i [limiti laterali](Matematica/Analisi%20matematica/Limiti/_index.md#^definizione-limiti-laterali) sono entrambi uguali o a $+ \infty$ o a $- \infty$.
^definizione-punto-di-flesso-a-tangente-verticale

%% 
esempio 1.22 pag. 250 lancelotti
%%

%% 
osservazione 1.23 pag. 250-251 lancelotti
%%

# 5 - Algebra delle derivate

> [!teorema]+ Teorema della derivata della somma
> 
> Date due [funzioni](Matematica/Teoria%20degli%20insiemi/Funzioni/_index.md#^definizione-funzione) $f \colon \text{dom}(f) \to \mathbb{R}$ e $g \colon \text{dom}(g) \to \mathbb{R}$ [derivabili](Matematica/Analisi%20matematica/Derivate/_index.md#^definizione-derivabilita-e-derivata-prima-di-una-funzione-in-un-punto) in un punto%% link %% $x_0$ [interno](Topologia%20dei%20reali.md#^definizione-punto-interno) a $\text{dom}(f) \cap \text{dom}(g)$, allora la loro somma%% link %% $f+g$ è [derivabile](Matematica/Analisi%20matematica/Derivate/_index.md#^definizione-derivabilita-e-derivata-prima-di-una-funzione-in-un-punto) in $x_0$ e
> 
> $$
> (f+g)'(x_0) = f'(x_0) + g'(x_0)
> $$
^teorema-della-derivata-della-somma

%% 
Dimostrazione: è un'immediata conseguenza della definizione di derivatat e viene lasciata per esercizio
%%

> [!teorema]+ Teorema della derivata del prodotto
> 
> Date due [funzioni](Matematica/Teoria%20degli%20insiemi/Funzioni/_index.md#^definizione-funzione) $f \colon \text{dom}(f) \to \mathbb{R}$ e $g \colon \text{dom}(g) \to \mathbb{R}$ [derivabili](Matematica/Analisi%20matematica/Derivate/_index.md#^definizione-derivabilita-e-derivata-prima-di-una-funzione-in-un-punto) in un punto%% link %% $x_0$ [interno](Topologia%20dei%20reali.md#^definizione-punto-interno) a $\text{dom}(f) \cap \text{dom}(g)$, allora il loro prodotto%% link %% $f \cdot g$ è [derivabile](Matematica/Analisi%20matematica/Derivate/_index.md#^definizione-derivabilita-e-derivata-prima-di-una-funzione-in-un-punto) in $x_0$ e
> 
> $$
> (f \cdot g)'(x_0) = f'(x_0) \cdot g(x_0) + f(x_0) \cdot g'(x_0)
> $$
^teorema-della-derivata-del-prodotto

%% 
dimostrazione pag. 252 lancelotti
%%

> [!teorema]+ Teorema della derivata del reciproco
> 
> Data una [funzione](Matematica/Teoria%20degli%20insiemi/Funzioni/_index.md#^definizione-funzione) $f \colon \text{dom}(f) \to \mathbb{R}$ [derivabile](Matematica/Analisi%20matematica/Derivate/_index.md#^definizione-derivabilita-e-derivata-prima-di-una-funzione-in-un-punto) in un punto%% link %% $x_0$ [interno](Topologia%20dei%20reali.md#^definizione-punto-interno) a $\text{dom}(f)$, se $f(x_0) \ne 0$ allora il reciproco%% link %% $\dfrac{1}{f}$ è [derivabile](Matematica/Analisi%20matematica/Derivate/_index.md#^definizione-derivabilita-e-derivata-prima-di-una-funzione-in-un-punto) in $x_0$ e
> 
> $$
> \left( \dfrac{1}{f} \right)'(x_0) = - \dfrac{f'(x_0)}{[f(x_0)]^2}
> $$
^teorema-della-derivata-del-reciproco

%% 
dimostrazione pag. 253 lancelotti
%%

> [!teorema]+ Teorema della derivata del quoziente
> 
> Date due [funzioni](Matematica/Teoria%20degli%20insiemi/Funzioni/_index.md#^definizione-funzione) $f \colon \text{dom}(f) \to \mathbb{R}$ e $g \colon \text{dom}(g) \to \mathbb{R}$ [derivabili](Matematica/Analisi%20matematica/Derivate/_index.md#^definizione-derivabilita-e-derivata-prima-di-una-funzione-in-un-punto) in un punto%% link %% $x_0$ [interno](Topologia%20dei%20reali.md#^definizione-punto-interno) a $\text{dom}(f) \cap \text{dom}(g)$, se $g(x_0) \ne 0$ allora il loro quoziente%% Link %% $\dfrac{f}{g}$ è [derivabile](Matematica/Analisi%20matematica/Derivate/_index.md#^definizione-derivabilita-e-derivata-prima-di-una-funzione-in-un-punto) in $x_0$ e
> 
> $$
> \left( \dfrac{f}{g} \right)'(x_0) = \dfrac{f'(x_0)g(x_0) - f(x_0)g'(x_0)}{[g(x_0)]^2}
> $$
^teorema-della-derivata-del-quoziente

%% 
dimostrazione pag. 253 lancelotti
%%

%% 
osservazione 1.25 pag. 253 lancelotti
%%

%% 
esempio 1.26 pagg. 253-254 lancelotti
%%

%% 
esercizio 1.27 pag. 254 lancelotti
%%

> [!teorema]+ Teorema della derivata della funzione composta
> 
> Date due [funzioni](Matematica/Teoria%20degli%20insiemi/Funzioni/_index.md#^definizione-funzione) $f \colon \text{dom}(f) \to \mathbb{R}$ e $g \colon \text{dom}(g) \to \mathbb{R}$ con immagine%% link %% di $f$ nel dominio%% Link %% di $g$ (cioè $\text{im}(f) \subseteq \text{dom}(f)$) e un punto%% link %% $x_0$ [interno](Topologia%20dei%20reali.md#^definizione-punto-interno) a $\text{dom}(f)$ tale che $f(x_0)$ è [interno](Topologia%20dei%20reali.md#^definizione-punto-interno) a $\text{dom}(g)$, se $f$ è [derivabile](Matematica/Analisi%20matematica/Derivate/_index.md#^definizione-derivabilita-e-derivata-prima-di-una-funzione-in-un-punto) in $x_0$ e $g$ è [derivabile](Matematica/Analisi%20matematica/Derivate/_index.md#^definizione-derivabilita-e-derivata-prima-di-una-funzione-in-un-punto) in $f(x_0)$, allora la loro composizione%% link %% $g \circ f$ è [derivabile](Matematica/Analisi%20matematica/Derivate/_index.md#^definizione-derivabilita-e-derivata-prima-di-una-funzione-in-un-punto) in $x_0$ e
> 
> $$
> (g \circ f)'(x_0) = g'(f(x_0)) \cdot f'(x_0)
> $$
^teorema-della-derivata-della-funzione-composta

%% 
dimostrazione pagg. 254-255 lancelotti
%%

%% 
esempio 1.29 pagg. 255-256 lancelotti
%%

%% 
osservazioni 1.30, 1.31 pag. 256 + dimostrazione 1.32 ed esempio 1.33 pagg. 256-257 lancelotti
%%

> [!teorema]+ Teorema della derivata della funzione inversa
> 
> Dato un intervallo%% link %% $I \subseteq \mathbb{R}$ e una [funzione continua](Funzioni%20continue.md#^definizione-funzione-continua) e invertibile%% link %% $f \colon I \to \mathbb{R}$ e un [punto interno](Topologia%20dei%20reali.md#^definizione-punto-interno) $x_0$ a $I$, se $f$ è [derivabile](Matematica/Analisi%20matematica/Derivate/_index.md#^definizione-derivabilita-e-derivata-prima-di-una-funzione-in-un-punto) in $x_0$ con $f'(x_0) \ne 0$, allora la sua inversa%% link %% $f^{-1}$ è [derivabile](Matematica/Analisi%20matematica/Derivate/_index.md#^definizione-derivabilita-e-derivata-prima-di-una-funzione-in-un-punto) in $x_0$ in $y_0 = f(x_0)$ e
> 
> $$
> \left( f^{-1} \right)'(y_0) = \dfrac{1}{f'(f^{-1}(y_0))}
> $$
^teorema-della-derivata-della-funzione-inversa

%% 
dimostrazione pag. 257 lancelotti
%%

%% 
osservazione 1.35 pagg. 257-258 lancelotti
%%

%% 
esempi 1.36 pagg. 258-259 lancelotti
%%

%% 
proposizione 1.37 pag. 259 lancelotti
%%

%% 
I teoremi 1.24, 1.28 e 1.34 valgono anche per le derivate laterali
%%

# 6 - Teoremi fondamentali del calcolo differenziale

%% 
definizione di "calcolo differenziale"
%%

## 6.1 - Teorema di Fermat

> [!osservazione]+ Osservazione: comportamento di $\color{#7F7F7F} f$ nei punti di estremo locale
> 
> Riprendiamo la definizione di punti minimi/massimi relativi%% link %%.
> 
> Nelle applicazioni%% di cosa? %% succede spesso che:
> - i punti di massimo%% Link %% sono punti%% link %% in cui $f$ è crescente%% link %% in un [intorno sinistro](Topologia%20dei%20reali.md#^definizione-intorno-di-un-punto) di tali punti%% link %% e decrescente%% link %% in un [intorno destro](Topologia%20dei%20reali.md#^definizione-intorno-di-un-punto),
> - mentre i punti di minimo%% link %% sono punti%% link %% in cui $f$ è decrescente%% link %% in un [intorno sinistro](Topologia%20dei%20reali.md#^definizione-intorno-di-un-punto) di tali punti%% link %% e crescente%% link %% in un [intorno destro](Topologia%20dei%20reali.md#^definizione-intorno-di-un-punto):
> 
> |                  | Punti di massimo  | Punti di minimo   |
> | ---------------- | ----------------- | ----------------- |
> | Intorno sinistro | $f$ è crescente   | $f$ è decrescente |
> | Intorno destro   | $f$ è decrescente | $f$ è crescente   |
> 
> %% mettere link nella tabella %%
> 
> Inoltre, se $f$ è [derivabile](Matematica/Analisi%20matematica/Derivate/_index.md#^definizione-derivabilita-e-derivata-prima-di-una-funzione-in-un-punto) in tali punti%% link %%, allora la [derivata](Matematica/Analisi%20matematica/Derivate/_index.md#^definizione-derivabilita-e-derivata-prima-di-una-funzione-in-un-punto) in quei punti%% Link %% è nulla%% link %%, cioè la retta tangente%% Link %% al grafico%% link %% nei punti%% link %% corrispondenti ai punti di massimo%% link %% e di minimo%% link %% è orizzontale%% link %%.
> 
> %% 
> mettere foto grafico pag. 260 però disegnando le rette tangenti orizzontali con resto della spiegazione
> %%
> 
> Oppure $f$ potrebbe non essere [continua](Funzioni%20continue.md#^definizione-funzione-continua) in tali punti%% link %%, come nel caso della [funzione](Matematica/Teoria%20degli%20insiemi/Funzioni/_index.md#^definizione-funzione) $f(x) = |\text{sgn}(x)|$ che ha un punto di minimo%% Link %% in $x=0$ ma non è [continua](Funzioni%20continue.md#^definizione-funzione-continua) in tale punto%% link %%.
> 
> %% 
> mettere foto grafico funzione modulo segno
> %%
> 
> Oppure $f$ potrebbe non essere [derivabile](Matematica/Analisi%20matematica/Derivate/_index.md#^definizione-derivabilita-e-derivata-prima-di-una-funzione-in-un-punto) in tali punti%% link %%, come nel caso della [funzione](Matematica/Teoria%20degli%20insiemi/Funzioni/_index.md#^definizione-funzione) $f(x) = |x|$ che ha un punto di minimo%% link %% in $x = 0$ ma non è [derivabile](Matematica/Analisi%20matematica/Derivate/_index.md#^definizione-derivabilita-e-derivata-prima-di-una-funzione-in-un-punto) in tale punto%% link %%.
> 
> %% 
> mettere foto grafico funzione f(x)=|x|
> %%
> 
> Oppure tali punti%% link %% potrebbero anche essere [isolati](Topologia%20dei%20reali.md#^definizione-punto-isolato).
> 
> Poiché la casistica è piuttosto vasta, vogliamo poter stabilire delle condizioni necessarie e/o sufficienti affinché un punto%% link %% sia di estremo locale%% Link %% per una [funzione](Matematica/Teoria%20degli%20insiemi/Funzioni/_index.md#^definizione-funzione).

> [!definizione]+ Definizione: punto stazionario
> 
> Data una [funzione](Matematica/Teoria%20degli%20insiemi/Funzioni/_index.md#^definizione-funzione) $f \colon \text{dom}(f) \to \mathbb{R}$ e un [punto interno](Topologia%20dei%20reali.md#^definizione-punto-interno) $x_0 \in \text{dom}(f)$ a $\text{dom}(f)$, se $f$ è [derivabile](Matematica/Analisi%20matematica/Derivate/_index.md#^definizione-derivabilita-e-derivata-prima-di-una-funzione-in-un-punto) in $x_0$ allora diciamo che **$x_0$ è un punto stazionario (o critico) per $f$** se $f'(x_0) = 0$.
^definizione-punto-stazionario

%% 
esempi di punti stazionari
%%

> [!teorema]+ Teorema di Fermat
> 
> Data una [funzione](Matematica/Teoria%20degli%20insiemi/Funzioni/_index.md#^definizione-funzione) $f \colon \text{dom}(f) \to \mathbb{R}$ e un [punto interno](Topologia%20dei%20reali.md#^definizione-punto-interno) $x_0 \in \text{dom}(f)$ a $\text{dom}(f)$, se $f$ è [derivabile](Matematica/Analisi%20matematica/Derivate/_index.md#^definizione-derivabilita-e-derivata-prima-di-una-funzione-in-un-punto) in $x_0$ e $x_0$ è un punto di massimo%% Link %% o di minimo locale%% link %% per $f$, allora $x_0$ è un [punto stazionario](Matematica/Analisi%20matematica/Derivate/_index.md#^definizione-punto-stazionario) per $f$.
^teorema-di-fermat

%% 
Questo teorema prende il nome da Pierre de Fermat: https://it.wikipedia.org/wiki/Teorema_di_Fermat_sui_punti_stazionari
%%

%% 
dimostrazione pag. 262 lancelotti
%%

%% 
osservazione 2.5 pagg. 262-263 lancelotti
%%

%% 
osservazione 2.6 pag. 263 lancelotti
%%

## 6.2 - Teorema di Lagrange e sue conseguenze

> [!teorema]+ Teorema di Rolle
> 
> Data una [funzione](Matematica/Teoria%20degli%20insiemi/Funzioni/_index.md#^definizione-funzione) $f \colon [a,b] \to \mathbb{R}$, se $f$ è [continua](Funzioni%20continue.md#^definizione-funzione-continua) in $[a,b]$, [derivabile](Matematica/Analisi%20matematica/Derivate/_index.md#^definizione-derivabilita-di-una-funzione-in-un-sottoinsieme-del-dominio) in $(a,b)$ e $f(a) = f(b)$, allora esiste almeno un punto%% link %% $x_0 \in (a,b)$ tale che $f'(x_0) = 0$.
^teorema-di-rolle

%% chi è Rolle? %%

%% 
dimostrazione pagg. 263-264 lancelotti
%%

%% esempio del teorema di Rolle %%

%% osservazione 2.8 pagg. 264-265 lancelotti %%

> [!teorema]+ Teorema di Lagrange (o del valore medio)
> 
> Data una [funzione](Matematica/Teoria%20degli%20insiemi/Funzioni/_index.md#^definizione-funzione) $f \colon [a,b] \to \mathbb{R}$, se $f$ è [continua](Funzioni%20continue.md#^definizione-funzione-continua) in $[a,b]$ e [derivabile](Matematica/Analisi%20matematica/Derivate/_index.md#^definizione-derivabilita-di-una-funzione-in-un-sottoinsieme-del-dominio) in $(a,b)$, allora esiste almeno un punto%% link %% $x_0 \in (a,b)$ tale che $f'(x_0) = \dfrac{f(b) - f(a)}{b - a}$.
^teorema-di-lagrange-o-del-valore-medio

%% chi è Lagrange? %%

%% 
dimostrazione pag. 265 lancelotti
%%

%% 
osservazione 2.11 pag. 266 lncelotti
%%

> [!corollario]+ Corollario del teorema di Lagrange
> 
> Dato un intervallo%% Link %% $I \subseteq \mathbb{R}$ e una [funzione](Matematica/Teoria%20degli%20insiemi/Funzioni/_index.md#^definizione-funzione) $f \colon I \to \mathbb{R}$ [derivabile](Matematica/Analisi%20matematica/Derivate/_index.md#^definizione-derivabilita-e-derivata-prima-di-una-funzione) e due punti%% Link %% $x_0, x \in I$, esiste un punto%% link %% $t$ compreso tra $x_0$ e $x$ (non necessariamente in questo ordine) tale che
> 
> $$
> f(x) - f(x_0) = f'(t)(x - x_0)
> $$
^corollario-del-teorema-di-lagrange

%% 
la formula $f(x) - f(x_0) = f'(t)(x - x_0)$ è detta **seconda formula dell'incremento finito** (fare definizione per questa e anche per la prima formula dell'incremento finito)
%%

%% 
Dimostrazione: si applica il Teorema di Lagrange alla funzioen $f$ ristretta all'intervallo di estremi $x_0$ e $x$.
%%

%% 
Osservazione 2.13 pag. 266 lancelotti
%%

> [!teorema]+ Teorema del legame fra la monotonia e il segno della derivata
> 
> Dato un intervallo%% Link %% $I \subseteq \mathbb{R}$ e una [funzione](Matematica/Teoria%20degli%20insiemi/Funzioni/_index.md#^definizione-funzione) $f \colon I \to \mathbb{R}$ [derivabile](Matematica/Analisi%20matematica/Derivate/_index.md#^definizione-derivabilita-e-derivata-prima-di-una-funzione), allora:
> - $f$ è crescente%% link %% (o decrescente%% link %%) su $I$ se e solo se $f'(x) \ge 0$ (o $f'(x) \le 0$) per ogni $x \in I$:
> 	$$
> 	\forall x \in I . \left( \begin{array}{}
> 	f \text{ crescente su } I \iff f'(x) \ge 0 \\
> 	f \text{ decrescente su } I \iff f'(x) \le 0 \\
> 	\end{array} \right) 
> 	$$
> - Se $f'(x) > 0$ (o $f'(x) < 0$) per ogni $x \in I$, allora $f$ è strettamente crescente%% link %% (o strettamente decrescente%% link %%) su $I$:
> 	$$
> 	\forall x \in I . \left( \begin{array}{}
> 	f'(x) > 0 \implies f \text{ strettamente crescente su } I \\
> 	f'(x) < 0 \implies f \text{ strettamente decrescente su } I \\
> 	\end{array} \right) 
> 	$$
> 
> Se $I$ contiene uno o entrambi i suoi estremi%% link %%, la [derivabilità](Matematica/Analisi%20matematica/Derivate/_index.md#^definizione-derivabilita-e-derivata-prima-di-una-funzione-in-un-punto) di $f$ in quei punti%% Link %% va intesa come la [derivabilità laterale](Matematica/Analisi%20matematica/Derivate/_index.md#^definizione-derivate-laterali-di-una-funzione).
^teorema-del-legame-fra-la-monotonia-e-il-segno-della-derivata

%% 
dimostrazione pagg. 267-268 lancelotti
%%

%% 
Osservazioni pagg. 268 lancelotti
%%

> [!corollario]+ Corollario del teorema del legame fra la monotonia e il segno della derivata
> 
> Data una [funzione](Matematica/Teoria%20degli%20insiemi/Funzioni/_index.md#^definizione-funzione) $f \colon [a,b] \to \mathbb{R}$, se $f$ è [continua](Funzioni%20continue.md#^definizione-funzione-continua) in $[a,b]$ e [derivabile](Matematica/Analisi%20matematica/Derivate/_index.md#^definizione-derivabilita-di-una-funzione-in-un-sottoinsieme-del-dominio) in $(a,b)$, allora:
> - Se $f'(x) \ge 0$ (o $f'(x) \le 0$) per ogni $x \in (a,b)$, allora $f$ è crescente%% link %% (o decrescente%% link %%) su $[a,b]$.
> - Se $f'(x) > 0$ (o $f'(x) < 0$) per ogni $x \in (a,b)$, allora $f$ è strettamente crescente%% link %% (o strettamente decrescente%% link %%) su $[a,b]$.
> 
> $$
> \forall x \in (a,b) . \left( \begin{array}{}
> f'(x) \ge 0 \implies f \text{ crescente su } [a,b] \\
> f'(x) \le 0 \implies f \text{ decrescente su } [a,b] \\
> f'(x) > 0 \implies f \text{ strettamente crescente su } [a,b] \\
> f'(x) < 0 \implies f \text{ strettamente decrescente su } [a,b] \\
> \end{array} \right) 
> $$

%% 
dimostrazione pag. 269
%%

%% 
osservazione 2.17 pag. 269-270 lancelotti
%%

> [!teorema]+ Teorema del test per la ricerca dei punti di massimo e minimo
> 
> Data una [funzione](Matematica/Teoria%20degli%20insiemi/Funzioni/_index.md#^definizione-funzione) $f \colon \text{dom}(f) \to \mathbb{R}$, un intervallo%% link %% $I \subseteq \text{dom}(f)$ e un [punto interno](Topologia%20dei%20reali.md#^definizione-punto-interno) $x_0$ a $I$, se $f$ è [continua](Funzioni%20continue.md#^definizione-funzione-continua) in $I$ e [derivabile](Matematica/Analisi%20matematica/Derivate/_index.md#^definizione-derivabilita-di-una-funzione-in-un-sottoinsieme-del-dominio) in $I \setminus \{ x_0 \}$, allora:
> - Se $f'(x) > 0$ per ogni $x \in I$ con $x < x_0$ e $f'(x) < 0$ per ogni $x \in I$ con $x > x_0$, allora $x_0$ è un punto di massimo locale%% link %% per $f$:
> 	
> 	|                  | $x < x_0$       | $x > x_0$         |
> 	| ---------------- | --------------- | ----------------- |
> 	| Valore di $f'$   | $f'(x) > 0$     | $f'(x) < 0$       |
> 	| Monotonia di $f$ | $f$ è crescente | $f$ è decrescente |
> 
> - Se $f'(x) < 0$ per ogni $x \in I$ con $x < x_0$ e $f'(x) > 0$ per ogni $x \in I$ con $x > x_0$, allora $x_0$ è un punto di minimo locale%% link %% per $f$:
> 	 
> 	|                  | $x < x_0$         | $x > x_0$       |
> 	| ---------------- | ----------------- | --------------- |
> 	| Valore di $f'$   | $f'(x) < 0$       | $f'(x) > 0$     |
> 	| Monotonia di $f$ | $f$ è decrescente | $f$ è crescente |
> 
> - Se $f'(x) > 0$ per ogni $x \in I$ con $x \ne x_0$, allora $x_0$ non è né un punto di massimo%% link %% né un punto di minimo%% link %% per $f$:
> 	
> 	|                  | $x < x_0$       | $x > x_0$       |
> 	| ---------------- | --------------- | --------------- |
> 	| Valore di $f'$   | $f'(x) > 0$     | $f'(x) > 0$     |
> 	| Monotonia di $f$ | $f$ è crescente | $f$ è crescente |
> 
> - Se $f'(x) < 0$ per ogni $x \in I$ con $x \ne x_0$, allora $x_0$ non è né un punto di massimo%% link %% né un punto di minimo%% link %% per $f$:
> 	
> 	|                  | $x < x_0$         | $x > x_0$         |
> 	| ---------------- | ----------------- | ----------------- |
> 	| Valore di $f'$   | $f'(x) < 0$       | $f'(x) < 0$       |
> 	| Monotonia di $f$ | $f$ è decrescente | $f$ è decrescente |
^teorema-del-test-per-la-ricerca-dei-punti-di-massimo-e-minimo

%% 
mettere colori e link a queste tabelle
%%

%% dimostrazione pag. 271 lancelotti %%

%% osservazione 2.19 pagg. 271-272 lancelotti %%

%% osservazione 2.20 pag. 272 lancelotti %%

Abbiamo visto che se $f$ è una funzione costante%% link %% ed è [derivabile](Matematica/Analisi%20matematica/Derivate/_index.md#^definizione-derivabilita-e-derivata-prima-di-una-funzione), allora $f'(x) = 0$ per ogni $x \in \text{dom}(f)$%% , come asserito nel teorema ??? %%. Il viceversa è vero, sotto opportune ipotesi, come afferma il prossimo risultato.

> [!teorema]+ Teorema di caratterizzazione delle funzioni costanti
> 
> Dato un intervallo%% link %% $I \subseteq \mathbb{R}$ e una [funzione](Matematica/Teoria%20degli%20insiemi/Funzioni/_index.md#^definizione-funzione) $f \colon I \to \mathbb{R}$ [derivabile](Matematica/Analisi%20matematica/Derivate/_index.md#^definizione-derivabilita-e-derivata-prima-di-una-funzione) tale che $f'(x) = 0$ per ogni $x \in I$, allora $f$ è costante%% link %% su $I$.
^teorema-di-caratterizzazione-delle-funzioni-costanti

%% dimostrazione pag. 273 lancelotti %%

%% osservazione 2.22 pag. 273 lancelotti %%

%% esempio 2.23 pag. 273 lancelotti %%

%% esercizio 2.24 pag. 273 lancelotti %%

%% 
Teorema del legame tra la convessità e la monotonia della derivata, L2a
%%

## 6.3 - Teoremi di De l'Hôpital

Questi teoremi%% link %% sono uno strumento molto potente per calcolare alcuni [limiti](Matematica/Analisi%20matematica/Limiti/_index.md#^definizione-limite) che sono [forme indeterminate algebriche del tipo $\dfrac{0}{0}$](Forme%20indeterminate.md#^forma-indeterminata-algebrica-del-tipo-0-su-0) o [$\dfrac{\infty}{\infty}$](Forme%20indeterminate.md#^definizione-forma-indeterminata-algebrica-del-tipo-infinito-su-infinito).

> [!teorema]+ Teorema di De l'Hôpital della forma indeterminata algebrica del tipo $\color{#FF3F3F} \dfrac{0}{0}$
> 
> Dato un intervallo%% link %% $A \subseteq \mathbb{R}$, due [funzioni](Matematica/Teoria%20degli%20insiemi/Funzioni/_index.md#^definizione-funzione) $f,g \colon A \to \mathbb{R}$, e un [punto di accumulazione](Topologia%20dei%20reali.md#^definizione-punto-di-accumulazione) $x_0 \in \mathbb{R} \cup \{ \pm \infty \}$ per $A$, se:
> 1. i [limiti](Matematica/Analisi%20matematica/Limiti/_index.md#^definizione-limite) di $f$ e $g$ per $x \to x_0$ sono nulli%% link %% (cioè $\displaystyle\lim_{x \to x_0} f(x) = \lim_{x \to x_0} g(x) = 0$),
> 2. esiste un [intorno](Topologia%20dei%20reali.md#^definizione-intorno-di-un-punto) $I(x_0)$ di $x_0$ tale che $f$ e $g$ siano [derivabili](Matematica/Analisi%20matematica/Derivate/_index.md#^definizione-derivabilita-di-una-funzione-in-un-sottoinsieme-del-dominio) in ogni $x \in A \cap I(x_0)$ (con $x \ne x_0$) e che per tali $x$ si ha $g'(x) \ne 0$ e
> 3. esiste il [limite](Matematica/Analisi%20matematica/Limiti/_index.md#^definizione-limite) $\displaystyle\lim_{x \to x_0} \dfrac{f'(x)}{g'(x)} = l \in \mathbb{R} \cup \{ \pm \infty \}$,
> 
> allora
> 
> $$
> \lim_{x \to x_0} \dfrac{f(x)}{g(x)} = l
> $$
^teorema-di-de-l-hopital-della-forma-indeterminata-algebrica-del-tipo-0-su-0

> [!teorema]+ Teorema di De l'Hôpital della forma indeterminata algebrica del tipo $\color{#FF3F3F} \dfrac{\infty}{\infty}$
> 
> Dato un intervallo%% link %% $A \subseteq \mathbb{R}$, due [funzioni](Matematica/Teoria%20degli%20insiemi/Funzioni/_index.md#^definizione-funzione) $f,g \colon A \to \mathbb{R}$, e un [punto di accumulazione](Topologia%20dei%20reali.md#^definizione-punto-di-accumulazione) $x_0 \in \mathbb{R} \cup \{ \pm \infty \}$ per $A$, se:
> 1. i [limiti](Matematica/Analisi%20matematica/Limiti/_index.md#^definizione-limite) di $f$ e $g$ per $x \to x_0$ sono infiniti%% link %% (cioè $\displaystyle\lim_{x \to x_0} f(x) = \pm \infty$ e $\displaystyle\lim_{x \to x_0} g(x) = \pm \infty$),
> 2. esiste un [intorno](Topologia%20dei%20reali.md#^definizione-intorno-di-un-punto) $I(x_0)$ di $x_0$ tale che $f$ e $g$ siano [derivabili](Matematica/Analisi%20matematica/Derivate/_index.md#^definizione-derivabilita-di-una-funzione-in-un-sottoinsieme-del-dominio) in ogni $x \in A \cap I(x_0)$ (con $x \ne x_0$) e che per tali $x$ si ha $g'(x) \ne 0$ e
> 3. esiste il [limite](Matematica/Analisi%20matematica/Limiti/_index.md#^definizione-limite) $\displaystyle\lim_{x \to x_0} \dfrac{f'(x)}{g'(x)} = l \in \mathbb{R} \cup \{ \pm \infty \}$,
> 
> allora
> 
> $$
> \lim_{x \to x_0} \dfrac{f(x)}{g(x)} = l
> $$
^teorema-di-de-l-hopital-della-forma-indeterminata-algebrica-del-tipo-infinito-su-infinito

%% 
osservazioni pag. 275 lancelotti
%%

> [!esempio]- Esempio: $\color{#7F7FFF} \displaystyle\lim_{x\to0} \dfrac{\sin x - x}{x^3}$ col teorema di De l'Hôpital
> 
> Prendiamo il [limite](Matematica/Analisi%20matematica/Limiti/_index.md#^definizione-limite) $\displaystyle\lim_{x\to0} \dfrac{\sin x - x}{x^3}$.
> 
> Questo [limite](Matematica/Analisi%20matematica/Limiti/_index.md#^definizione-limite) è una [forma indeterminata algebrica del tipo $\dfrac{0}{0}$](Forme%20indeterminate.md#^forma-indeterminata-algebrica-del-tipo-0-su-0) perché
> 
> $$
> \lim_{x \to 0} (\sin x - x) = 0 \quad  \land \quad \lim_{x \to 0} x^3 = 0
> $$
> 
> Inoltre, abbiamo che sia il numeratore%% link %% $\sin x - x$ che il denominatore%% Link %% $x^3$ sono [funzioni derivabili](Matematica/Analisi%20matematica/Derivate/_index.md#^definizione-derivabilita-e-derivata-prima-di-una-funzione).
> 
> Non possiamo sapere a priori se riusciamo a usare il [teorema di De l'Hôpital della forma indeterminata algebrica del tipo $\dfrac{0}{0}$](Matematica/Analisi%20matematica/Derivate/_index.md#^teorema-di-de-l-hopital-della-forma-indeterminata-algebrica-del-tipo-0-su-0) perché non sappiamo se viene rispettata la terza condizione, cioè non sappiamo se esiste il [limite](Matematica/Analisi%20matematica/Limiti/_index.md#^definizione-limite) del rapporto%% link al quoziente tra funzioni %% delle [derivate](Matematica/Analisi%20matematica/Derivate/_index.md#^definizione-derivabilita-e-derivata-prima-di-una-funzione) $(\sin x - x)'$ e $(x^3)'$. Nel caso tentar non nuoce, quindi proviamo a calcolarlo e vediamo se esiste:
> 
> $$
> \lim_{x \to 0} \dfrac{(\sin x - x)'}{(x^3)'} = \lim_{x \to 0} \dfrac{\cos x - 1}{3x^2} = \lim_{x \to 0} \left( -\dfrac{1}{3} \cdot \dfrac{1 - \cos x}{x^2} \right) = -\dfrac{1}{3} \cdot \dfrac{1}{2} = - \dfrac{1}{6}  
> $$
> 
> (Ricordiamo che $\displaystyle\lim_{x \to 0} \dfrac{1 - \cos x}{x^2} = \dfrac{1}{2}$ per il [limite notevole del coseno tendente a $0$](Limiti%20notevoli.md#^proposizione-limite-notevole-del-coseno-tendente-a-0)).
> 
> Poiché il [limite](Matematica/Analisi%20matematica/Limiti/_index.md#^definizione-limite) del rapporto%% link al quoziente tra funzioni %% delle [derivate](Matematica/Analisi%20matematica/Derivate/_index.md#^definizione-derivabilita-e-derivata-prima-di-una-funzione) $(\sin x - x)'$ e $(x^3)'$ esiste ed è pari a $- \dfrac{1}{6} \in \mathbb{R} \cup \{ \pm \infty \}$, possiamo concludere che siamo dei ludopatici davvero in gamba dato che abbiamo vinto la scommessa iniziale. Possiamo quindi usare il [teorema di De l'Hôpital della forma indeterminata algebrica del tipo $\dfrac{0}{0}$](Matematica/Analisi%20matematica/Derivate/_index.md#^teorema-di-de-l-hopital-della-forma-indeterminata-algebrica-del-tipo-0-su-0), il quale ci dice che il [limite](Matematica/Analisi%20matematica/Limiti/_index.md#^definizione-limite) $\displaystyle\lim_{x\to0} \dfrac{\sin x - x}{x^3}$ ha lo stesso valore del [limite](Matematica/Analisi%20matematica/Limiti/_index.md#^definizione-limite) $\displaystyle\lim_{x \to 0} \dfrac{(\sin x - x)'}{(x^3)'}$, ossia $-\dfrac{1}{6}$:
> 
> $$
> \displaystyle\lim_{x\to0} \dfrac{\sin x - x}{x^3} = - \dfrac{1}{6}
> $$

%%
In particolare, possiamo anche aggiungere che

$$
\sin x = x - \dfrac{1}{6} x^3 + o(x^3) \text{ per } x \to 0
$$

(da dove se ne sono usciti con questa cosa?)
%%

%% 
esempio 2-30 pagg- 275-276 lancelotti
%%

> [!attenzione]+ Attenzione: cosa fare se non esiste il limite delle derivate
> 
> Se una delle ipotesi del [teorema di De l'Hôpital della forma indeterminata algebrica del tipo $\dfrac{0}{0}$](Matematica/Analisi%20matematica/Derivate/_index.md#^teorema-di-de-l-hopital-della-forma-indeterminata-algebrica-del-tipo-0-su-0) non è verificata, allora non possiamo usarlo e dobbiamo trovare un altro modo per calcolare quel [limite](Matematica/Analisi%20matematica/Limiti/_index.md#^definizione-limite). Il caso più comune è quello in cui non viene soddisfatta la terza ipotesi, cioè non esiste il [limite](Matematica/Analisi%20matematica/Limiti/_index.md#^definizione-limite) del rapporto%% link al quoziente tra funzioni %% delle [derivate](Matematica/Analisi%20matematica/Derivate/_index.md#^definizione-derivabilita-e-derivata-prima-di-una-funzione) del numeratore%% link %% e del denominatore%% link %%. In questo caso, **è errato dire che se n0n esiste il [limite](Matematica/Analisi%20matematica/Limiti/_index.md#^definizione-limite) delle [derivate](Matematica/Analisi%20matematica/Derivate/_index.md#^definizione-derivabilita-e-derivata-prima-di-una-funzione) allora non esiste neanche il [limite](Matematica/Analisi%20matematica/Limiti/_index.md#^definizione-limite) "normale"**:
> 
> $$
> \not\exists \lim_{x \to x_0} \dfrac{f'(x)}{g'(x)} \not\implies \not\exists \lim_{x \to x_0} \dfrac{f(x)}{g(x)}
> $$

> [!esempio]- Esempio di limite delle derivate che non esiste
> 
> Prendiamo il [limite](Matematica/Analisi%20matematica/Limiti/_index.md#^definizione-limite) $\displaystyle\lim_{x\to+\infty} \dfrac{x + \sin x}{x+3}$.
> 
> Questo [limite](Matematica/Analisi%20matematica/Limiti/_index.md#^definizione-limite) è una [forma indeterminata algebrica del tipo $\dfrac{\infty}{\infty}$](Forme%20indeterminate.md#^forma-indeterminata-algebrica-del-tipo-infinito-su-infinito) perché
> 
> $$
> \lim_{x \to +\infty} (x + \sin x) = +\infty \quad  \land \quad \lim_{x \to +\infty} (x+3) = +\infty
> $$
> 
> Inoltre, abbiamo che sia il numeratore%% link %% $x + \sin x$ che il denominatore%% Link %% $x+3$ sono [funzioni derivabili](Matematica/Analisi%20matematica/Derivate/_index.md#^definizione-derivabilita-e-derivata-prima-di-una-funzione).
> 
> Non possiamo sapere a priori se riusciamo a usare il [teorema di De l'Hôpital della forma indeterminata algebrica del tipo $\dfrac{\infty}{\infty}$](Matematica/Analisi%20matematica/Derivate/_index.md#^teorema-di-de-l-hopital-della-forma-indeterminata-algebrica-del-tipo-infinito-su-infinito) perché non sappiamo se viene rispettata la terza condizione, cioè non sappiamo se esiste il [limite](Matematica/Analisi%20matematica/Limiti/_index.md#^definizione-limite) del rapporto%% link al quoziente tra funzioni %% delle [derivate](Matematica/Analisi%20matematica/Derivate/_index.md#^definizione-derivabilita-e-derivata-prima-di-una-funzione) $(x + \sin x)'$ e $(x+3)'$. Anche in questo caso facciamo un po' di gioco d'azzardo e tentiamo la giocata provando a calcolarlo:
> 
> $$
> \lim_{x \to + \infty} \dfrac{(x+\sin x)'}{(x+3)'} = \lim_{x \to + \infty} \dfrac{1 + \cos x}{1} = \lim_{x \to + \infty} (1 + \cos x)
> $$
> 
> Poiché quest'ultmo [limite](Matematica/Analisi%20matematica/Limiti/_index.md#^definizione-limite) non esiste%% perché? %%, allora abbiamo perso la scommessa e non possiamo applicare il [teorema di De l'Hôpital della forma indeterminata algebrica del tipo $\dfrac{\infty}{\infty}$](Matematica/Analisi%20matematica/Derivate/_index.md#^teorema-di-de-l-hopital-della-forma-indeterminata-algebrica-del-tipo-infinito-su-infinito). Per calcolare il [limite](Matematica/Analisi%20matematica/Limiti/_index.md#^definizione-limite) di partenza, quindi, dobbiamo cambiare metodo: per esempio, essendo $\sin x$ [$o$-piccolo](Infiniti%20e%20infinitesimi.md#^definizione-o-piccolo) di $x$ per $x \to + \infty$ e $3$ è [$o$-piccolo](Infiniti%20e%20infinitesimi.md#^definizione-o-piccolo) di $x$ per $x \to + \infty$, possiamo usare il [PETT](Infiniti%20e%20infinitesimi.md#^principio-di-eliminazione-dei-termini-trascurabili) per eliminare proprio questi termini:
> 
> $$
> \lim_{x \to + \infty} \dfrac{x + \sin x}{x + 3} = \lim_{x \to + \infty} \dfrac{x + o(x)}{x + o(x)} \overset{\text{PETT}}{=} = \lim_{x \to + \infty} \dfrac{x}{x} = 1
> $$
> 
> Abbiamo capito quindi che non ci conviene fare sempre ricorso ai teoremi di De l'Hôpital per risolvere le [forme indeterminate](Forme%20indeterminate.md#^definizione-forma-indeterminata).

> [!esempio]- Esempio di limite delle derivate ricorsive
> 
> Ora prendiamo il [limite](Matematica/Analisi%20matematica/Limiti/_index.md#^definizione-limite) $\displaystyle\lim_{x\to+\infty} \dfrac{\sqrt{x^2 + 1}}{x}$.
> 
> Questo [limite](Matematica/Analisi%20matematica/Limiti/_index.md#^definizione-limite) è una [forma indeterminata algebrica del tipo $\dfrac{\infty}{\infty}$](Forme%20indeterminate.md#^forma-indeterminata-algebrica-del-tipo-infinito-su-infinito) perché
> 
> $$
> \lim_{x \to +\infty} \sqrt{x^2 + 1} = +\infty \quad  \land \quad \lim_{x \to +\infty} (x) = +\infty
> $$
> 
> Inoltre, abbiamo che sia il numeratore%% link %% $x + \sin x$ che il denominatore%% Link %% $x+3$ sono [funzioni derivabili](Matematica/Analisi%20matematica/Derivate/_index.md#^definizione-derivabilita-e-derivata-prima-di-una-funzione).
> 
> Non possiamo sapere a priori se riusciamo a usare il [teorema di De l'Hôpital della forma indeterminata algebrica del tipo $\dfrac{\infty}{\infty}$](Matematica/Analisi%20matematica/Derivate/_index.md#^teorema-di-de-l-hopital-della-forma-indeterminata-algebrica-del-tipo-infinito-su-infinito) perché non sappiamo se viene rispettata la terza condizione, cioè non sappiamo se esiste il [limite](Matematica/Analisi%20matematica/Limiti/_index.md#^definizione-limite) del rapporto%% link al quoziente tra funzioni %% delle [derivate](Matematica/Analisi%20matematica/Derivate/_index.md#^definizione-derivabilita-e-derivata-prima-di-una-funzione) $(\sqrt{x^2+1})'$ e $x'$. Proviamo a calcolarlo:
> 
> $$
> \lim_{x \to + \infty} \dfrac{(\sqrt{x^2+1})'}{x'} = \lim_{x \to + \infty} \dfrac{\dfrac{x}{\sqrt{x^2+1}}}{1} = \lim_{x \to + \infty} \dfrac{x}{\sqrt{x^2+1}}
> $$
> 
> Dato che non sappiamo come procedere, proviamo nuovamente ad applicare il [teorema di De l'Hôpital della forma indeterminata algebrica del tipo $\dfrac{\infty}{\infty}$](Matematica/Analisi%20matematica/Derivate/_index.md#^teorema-di-de-l-hopital-della-forma-indeterminata-algebrica-del-tipo-infinito-su-infinito), calcolando di nuovo il [limite](Matematica/Analisi%20matematica/Limiti/_index.md#^definizione-limite) del rapporto%% link al quoziente tra funzioni %% delle [derivate](Matematica/Analisi%20matematica/Derivate/_index.md#^definizione-derivabilita-e-derivata-prima-di-una-funzione) $x'$ e $(\sqrt{x^2+1})'$:
> 
> $$
> \lim_{x \to + \infty} \dfrac{x'}{(\sqrt{x^2+1})'} = \lim_{x \to + \infty} \dfrac{1}{\dfrac{x}{\sqrt{x^2+1}}} = \displaystyle\lim_{x\to+\infty} \dfrac{\sqrt{x^2 + 1}}{x}
> $$
> 
> Boh a quanto pare siamo stati trollati: siamo tornati esattamente al [limite](Matematica/Analisi%20matematica/Limiti/_index.md#^definizione-limite) di partenza. Abbiamo quindi capito che ci sono alcuni [limiti](Matematica/Analisi%20matematica/Limiti/_index.md#^definizione-limite) che portano a [derivate](Matematica/Analisi%20matematica/Derivate/_index.md#^definizione-derivabilita-e-derivata-prima-di-una-funzione) "ricorsive", cioè che prima o poi tornano su se stesse.
> 
> Non possiamo quindi applicare il [teorema di De l'Hôpital della forma indeterminata algebrica del tipo $\dfrac{\infty}{\infty}$](Matematica/Analisi%20matematica/Derivate/_index.md#^teorema-di-de-l-hopital-della-forma-indeterminata-algebrica-del-tipo-infinito-su-infinito) perché non arriveremo mai a risolvere il [limite](Matematica/Analisi%20matematica/Limiti/_index.md#^definizione-limite), quindi meglio se tentiamo un altro metodo.

### 6.3.1 - Conseguenze dei teoremi di De l'Hôpital

> [!teorema]+ Teorema di derivabilità in un punto mediante il limite della derivata
> 
> Dato un intervallo%% link %% $I \subseteq \mathbb{R}$, una [funzione](Matematica/Teoria%20degli%20insiemi/Funzioni/_index.md#^definizione-funzione) $f \colon I \to \mathbb{R}$ e un [punto interno](Topologia%20dei%20reali.md#^definizione-punto-interno) $x_0$ a $I$ e supponiamo che:
> 1. $f$ sia [continua](Funzioni%20continue.md#^definizione-funzione-continua) in $I$,
> 2. $f$ sia [derivabile](Matematica/Analisi%20matematica/Derivate/_index.md#^definizione-derivabilita-e-derivata-prima-di-una-funzione) in $I \setminus \{ x_0 \}$ (cioè non sappiamo se è [derivabile](Matematica/Analisi%20matematica/Derivate/_index.md#^definizione-derivabilita-e-derivata-prima-di-una-funzione-in-un-punto) anche in $x_0$) e
> 3. esista il [limite](Matematica/Analisi%20matematica/Limiti/_index.md#^definizione-limite) $\displaystyle\lim_{x \to x_0} f'(x) = l \in \mathbb{R}$,
> 
> allora $f$ è [derivabile](Matematica/Analisi%20matematica/Derivate/_index.md#^definizione-derivabilita-e-derivata-prima-di-una-funzione-in-un-punto) in $x_0$ con $f'(x_0) = l$ e la [derivata](Matematica/Analisi%20matematica/Derivate/_index.md#^definizione-derivabilita-e-derivata-prima-di-una-funzione) $f'$ è [continua](Funzioni%20continue.md#^definizione-funzione-continua) in $x_0$.
^teorema-di-derivabilita-in-un-punto-mediante-il-limite-della-derivata

%% 
dimostrazione pag. 277 lancelotti
%%

> [!osservazione]+ Osservazione: significato del teorema di derivabilità in un punto mediante il limite della derivata
> 
> Il [teorema di derivabilità in un punto mediante il limite della derivata](Matematica/Analisi%20matematica/Derivate/_index.md#^teorema-di-derivabilita-in-un-punto-mediante-il-limite-della-derivata) ci dice che se una [funzione](Matematica/Teoria%20degli%20insiemi/Funzioni/_index.md#^definizione-funzione) $f$ è [continua](Funzioni%20continue.md#^definizione-funzione-continua) in un punto%% link %% $x_0$ ed è [derivabile](Matematica/Analisi%20matematica/Derivate/_index.md#^definizione-derivabilita-di-una-funzione-in-un-sottoinsieme-del-dominio) in tutto un [intorno](Topologia%20dei%20reali.md#^definizione-intorno-di-un-punto) di $x_0$ ma non sappiamo se è [derivabile](Matematica/Analisi%20matematica/Derivate/_index.md#^definizione-derivabilita-e-derivata-prima-di-una-funzione-in-un-punto) in $x_0$ stesso, se il [limite](Matematica/Analisi%20matematica/Limiti/_index.md#^definizione-limite) della [derivata](Matematica/Analisi%20matematica/Derivate/_index.md#^definizione-derivabilita-e-derivata-prima-di-una-funzione) per $x \to x_0$ è un numero reale%% link %% allora possiamo confermare che $f$ è [derivabile](Matematica/Analisi%20matematica/Derivate/_index.md#^definizione-derivabilita-e-derivata-prima-di-una-funzione-in-un-punto) in $x_0$ e questa [derivata](Matematica/Analisi%20matematica/Derivate/_index.md#^definizione-derivabilita-e-derivata-prima-di-una-funzione) $f'$ nel punto%% link %% $x_0$ ha proprio lo stesso valore%% Link %% $l$ del [limite](Matematica/Analisi%20matematica/Limiti/_index.md#^definizione-limite) per $x \to x_0$.
> 
> Se invece non esiste il [limite](Matematica/Analisi%20matematica/Limiti/_index.md#^definizione-limite) della [derivata](Matematica/Analisi%20matematica/Derivate/_index.md#^definizione-derivabilita-e-derivata-prima-di-una-funzione) per $x \to x_0$, allora non possiamo concludere nulla sulla [derivabilità](Matematica/Analisi%20matematica/Derivate/_index.md#^definizione-derivabilita-e-derivata-prima-di-una-funzione-in-un-punto) di $f$ in $x_0$ e dobbiamo ricorrere al calcolo del [limite](Matematica/Analisi%20matematica/Limiti/_index.md#^definizione-limite) del rapporto incrementale%% link %% senza poter ricorrere ai teoremi di De l'Hôpital.

> [!proposizione]+ Proposizione: non-derivabilità se il limite della derivata è infinito
> 
> Data una [funzione](Matematica/Teoria%20degli%20insiemi/Funzioni/_index.md#^definizione-funzione) $f \colon \text{dom}(f) \to \mathbb{R}$ e un [punto interno](Topologia%20dei%20reali.md#^definizione-punto-interno) $x_0$ a $\text{dom}(f)$, se il [limite](Matematica/Analisi%20matematica/Limiti/_index.md#^definizione-limite) della sua [derivata](Matematica/Analisi%20matematica/Derivate/_index.md#^definizione-derivabilita-e-derivata-prima-di-una-funzione) $f'$ per $x \to x_0$ è infinito, allora $f$ non è sicuramente [derivabile](Matematica/Analisi%20matematica/Derivate/_index.md#^definizione-derivabilita-e-derivata-prima-di-una-funzione-in-un-punto) in $x_0$:
> 
> $$
> \lim_{x \to x_0} f'(x) = \pm \infty \implies f \text{ non è derivabile in } x_0
> $$
^proposizione-non-derivabilita-se-il-limite-della-derivata-e-infinito

%%

[!dimostrazione]- Dimostrazione: non-derivabilità se il limite della derivata è infinito

Dimostriamo che [se il limite di $f'$ per $x->x_0$ è infinito allora $f$ non è derivabile in $x_0$](Matematica/Analisi%20matematica/Derivate/_index.md#^proposizione-non-derivabilita-se-il-limite-della-derivata-e-infinito).

pag. 278 lancelotti
%%

%% 
esempio 2.37 pag. 278 lancelotti
%%

%% 
osservazioen 2.38 pag. 278 lancelotti
%%

%% 
esempio 2.39 pag. 278-279 lancelotti
%%

%% 
esercizio 2.40 pag. 279 lancelotti
%%

> [!teorema]+ Teorema di discontinuità della derivata
> 
> Dato un intervallo aperto%% link %% $I \subseteq \mathbb{R}$ e una [funzione derivabile](Matematica/Analisi%20matematica/Derivate/_index.md#^definizione-derivabilita-e-derivata-prima-di-una-funzione) $f \colon I \to \mathbb{R}$, la sua [derivata](Matematica/Analisi%20matematica/Derivate/_index.md#^definizione-derivabilita-e-derivata-prima-di-una-funzione) $f'$ non può presentare [punti di discontinuità eliminabile](Funzioni%20continue.md#^definizione-discontinuita-eliminabile) o [di prima specie](Funzioni%20continue.md#^definizione-discontinuita-di-prima-specie-o-salto), cioè se $f'$ è [discontinua](Funzioni%20continue.md#^definizione-funzione-continua) allora presenta solo [punti di discontinuità di seconda specie](Funzioni%20continue.md#^definizione-discontinuita-di-seconda-specie).
> 
> In particolare, se un punto%% link %% $x_0 \in I$ è [di discontinuità](Funzioni%20continue.md#^definizione-funzione-continua) di $f'$, allora non esistono i limiti laterali%% link %% $\displaystyle\lim_{x \to x_0^\pm} f'(x)$.

%% dimostrazione pag. 279 lancelotti %%

%% 
La funzione $f$ dell'esempio 2.39 pag. 278.279 lancelotti è derivabile su R e 0 è un punto di discontinuità di seconda specie per $f'$
%%

> [!osservazione]+ Osservazione: riformulazione dei punti di non derivabilità con De l'Hôpital
> 
> Grazie al [teorema di De l'Hôpital della forma indeterminata algebrica del tipo $\dfrac{0}{0}$](Matematica/Analisi%20matematica/Derivate/_index.md#^teorema-di-de-l-hopital-della-forma-indeterminata-algebrica-del-tipo-0-su-0) abbiamo un modo più semplice per classificare i punti di non derivabilità%% link %%.
> 
> Infatti, data una [funzione](Matematica/Teoria%20degli%20insiemi/Funzioni/_index.md#^definizione-funzione) $f \colon \text{dom}(f) \to \mathbb{R}$ e un punto%% link %% $x_0$ [interno](Topologia%20dei%20reali.md#^definizione-punto-interno) a $\text{dom}(f)$, se $f$ è [continua](Funzioni%20continue.md#^definizione-funzione-continua) in $x_0$ e [derivabile](Matematica/Analisi%20matematica/Derivate/_index.md#^definizione-derivabilita-di-una-funzione-in-un-sottoinsieme-del-dominio) in tutto un [intorno](Topologia%20dei%20reali.md#^definizione-intorno-di-un-punto) $I \subseteq \text{dom}(f)$ escluso $x_0$ stesso in cui non sappiamo se $f$ è [derivabile](Matematica/Analisi%20matematica/Derivate/_index.md#^definizione-derivabilita-e-derivata-prima-di-una-funzione-in-un-punto), allora:
> - Se i limiti laterali%% link %% della [derivata](Matematica/Analisi%20matematica/Derivate/_index.md#^definizione-derivabilita-e-derivata-prima-di-una-funzione) $\displaystyle\lim_{x \to x_0^\pm} f'(x)$ esistono finiti%% link %% e diversi fra loro, oppure se uno è finito%% link %% e l'altro è infinito%% link %%, allora $x_0$ è un [punto angoloso](Matematica/Analisi%20matematica/Derivate/_index.md#^definizione-punto-angoloso) per $f$.
> - Se i limiti laterali%% link %% della [derivata](Matematica/Analisi%20matematica/Derivate/_index.md#^definizione-derivabilita-e-derivata-prima-di-una-funzione) $\displaystyle\lim_{x \to x_0^\pm} f'(x)$ esistono infiniti%% link %% e diversi fra loro, allora $x_0$ è una [cuspide](Matematica/Analisi%20matematica/Derivate/_index.md#^definizione-cuspide) per $f$.
> - Se i limiti laterali%% link %% della [derivata](Matematica/Analisi%20matematica/Derivate/_index.md#^definizione-derivabilita-e-derivata-prima-di-una-funzione) $\displaystyle\lim_{x \to x_0^\pm} f'(x)$ esistono infiniti%% link %% e uguali, allora $x_0$ è un [punto di flesso a tangente verticale](Matematica/Analisi%20matematica/Derivate/_index.md#^definizione-punto-di-flesso-a-tangente-verticale) per $f$.
> 
> |                                                                                  | $\displaystyle\lim_{x \to x_0^+} f'(x) = \underbrace{l}_{\ne l'} \in \mathbb{R}$                                            | $\displaystyle\lim_{x \to x_0^+} f'(x) = - \infty$                                                                                                                      | $\displaystyle\lim_{x \to x_0^+} f'(x) = + \infty$                                                                                                                      |
> | -------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
> | $\displaystyle\lim_{x \to x_0^-} f'(x) = \underbrace{l'}_{\ne l} \in \mathbb{R}$ | $x_0$ è un [punto angoloso](Matematica/Analisi%20matematica/Derivate/_index.md#^definizione-punto-angoloso) per $f$ | $x_0$ è un [punto angoloso](Matematica/Analisi%20matematica/Derivate/_index.md#^definizione-punto-angoloso) per $f$                                             | $x_0$ è un [punto angoloso](Matematica/Analisi%20matematica/Derivate/_index.md#^definizione-punto-angoloso) per $f$                                             |
> | $\displaystyle\lim_{x \to x_0^-} f'(x) = - \infty$                               | $x_0$ è un [punto angoloso](Matematica/Analisi%20matematica/Derivate/_index.md#^definizione-punto-angoloso) per $f$ | $x_0$ è un [punto di flesso a tangente verticale](Matematica/Analisi%20matematica/Derivate/_index.md#^definizione-punto-di-flesso-a-tangente-verticale) per $f$ | $x_0$ è una [cuspide](Matematica/Analisi%20matematica/Derivate/_index.md#^definizione-cuspide) per $f$                                                          |
> | $\displaystyle\lim_{x \to x_0^-} f'(x) = + \infty$                               | $x_0$ è un [punto angoloso](Matematica/Analisi%20matematica/Derivate/_index.md#^definizione-punto-angoloso) per $f$ | $x_0$ è una [cuspide](Matematica/Analisi%20matematica/Derivate/_index.md#^definizione-cuspide) per $f$                                                          | $x_0$ è un [punto di flesso a tangente verticale](Matematica/Analisi%20matematica/Derivate/_index.md#^definizione-punto-di-flesso-a-tangente-verticale) per $f$ |

%% 
Dimostrazione lasciata per esercizio
%%

---

> [!fonti]+ Fonti
> 
> - 🏫 Corso di Laurea in Informatica (`L-31 R`) presso l'Università di Torino:
> 	- Corso di _Analisi Matematica - canale C_, A.A. 2020-21 ([pagina Moodle](https://informatica.i-learn.unito.it/course/view.php?id=2075)):
> 		- Prof. Barutello Vivina Laura, videolezioni:
> 			- [_L1a_](https://informatica.i-learn.unito.it/local/streamingfilemanager/file.php/informatica.i-learn.unito.it/2075/L1a.mp4), [_L1b_](https://informatica.i-learn.unito.it/local/streamingfilemanager/file.php/informatica.i-learn.unito.it/2075/L1b.mp4).
> 			- [_L2a_](https://informatica.i-learn.unito.it/local/streamingfilemanager/file.php/informatica.i-learn.unito.it/2075/L2a.mp4), [_L2b_](https://informatica.i-learn.unito.it/local/streamingfilemanager/file.php/informatica.i-learn.unito.it/2075/L2b.mp4).
> 			- [_L3a_](https://informatica.i-learn.unito.it/local/streamingfilemanager/file.php/informatica.i-learn.unito.it/2075/L3a.mp4).
> - 📚 Sergio Lancelotti, _Lezioni di Analisi Matematica I_, Celid, 2020 (ISBN: `978-8867891979`):
> 	- Capitolo 4 - _Calcolo differenziale per funzioni di una variabile_:
> 		- 1 - _Derivata di una funzione_:
> 			- 1.1 - _Punti di non derivabilità_.
> 			- 1.2 - _Algebra delle derivate_.
> 		- 2 - _Teoremi fondamentali del calcolo differenziale_:
> 			- 2.1 - _Teorema di Fermat_.
> 			- 2.2 - _Teorema di Lagrange e sue conseguenze_.
> 			- 2.3 - _I teoremi di De l'Hôpital_.
> - 📚 Walter Dambrosio, _Analisi matematica - Fare e comprendere_, Zanichelli, 2018 (ISBN: `9788808220745`):
> 	- Parte I - _I concetti dell'analisi matematica_:
> 		- Capitolo 2 - _Introduzione al calcolo differenziale_:
> 			- 1 - _Derivata di una funzione in un punto_:
> 				- 1.1 - _Pendenza di una funzione in un punto: il concetto di "localmente dritto"_.
