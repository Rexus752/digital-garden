---
title: Funzioni continue
---

> [!premessa]+ Premessa
> 
> Ciao! Se è la prima volta che capiti su questo sito, ti consiglio di consultare la [pagina principale](index.md) di questo cosiddetto _Giardino Digitale_ per scoprire meglio cos'è e come navigarlo.
> 
> Lo stato di questa nota è al momento: 🔴 <font color="#FF7F7F">_Bozza_</font>.

---

> [!definizione]+ Definizione: funzione continua
> 
> Data una [funzione](Matematica/Teoria%20degli%20insiemi/Funzioni/_index.md#^definizione-funzione) $f \colon \text{dom}(f) \to \mathbb{R}$ e un punto%% link %% $x_0 \in \text{dom}(f)$, diciamo che $f$ è **continua in $x_0$** se, per ogni [intorno](Topologia%20dei%20reali.md#^definizione-intorno-di-un-punto) $I(f(x_0))$ di $f(x_0)$ esiste un [intorno](Topologia%20dei%20reali.md#^definizione-intorno-di-un-punto) $I(x_0)$ di $x_0$ tale che, per ogni punto%% link %% $x \in \text{dom}(f)$ con $x \in I(x_0)$, si ha che $f(x) \in I(f(x_0))$.
> 
> Poiché gli [intorni](Topologia%20dei%20reali.md#^definizione-intorno-di-un-punto) di $f(x_0)$ e di $x_0$ sono rispettivamente della forma
> 
> $$
> I(f(x_0)) = I_\varepsilon(f(x_0)) = (f(x_0) - \varepsilon, f(x_0) + \varepsilon)
> $$
> 
> e
> 
> $$
> I(x_0) = I_\delta(x_0) = (x_0 - \delta, x_0 + \delta)
> $$
> 
> la definizione può essere così riformulata:
> 
> $$
> \begin{array}{}
> f \text{ è continua in } x_0 \\
> \Updownarrow \\
> \forall \varepsilon > 0, \exists \delta < 0, \forall x \in \text{dom}(f) . \big( | x - x_0| < \delta \implies |f(x) - f(x_0)| < \varepsilon \big) 
> \end{array}
> $$
> 
> Inoltre:
> - $f$ è **discontinua in $x_0$** se $f$ non è continua in $x_0$.
> - $f$ è **continua** se $f$ è continua in ogni punto%% link %% del dominio%% link %% $\text{dom}(f)$.
> - $f$ è **discontinua** se $f$ è discontinua in almeno un punto%% link %% del dominio%% link %% $\text{dom}(f)$.
> - Dato un [sottoinsieme](Matematica/Teoria%20degli%20insiemi/_index.md#^definizione-sottoinsieme) $A \subseteq \text{dom}(f)$ non [vuoto](Matematica/Teoria%20degli%20insiemi/_index.md#^definizione-insieme-vuoto), $f$ è **continua in $A$** se $f$ è continua in ogni punto%% Link %% di $A$.
^definizione-funzione-continua

%% CHE SIGNIFICA?
L'interpretazione è simile a quella del $\displaystyle\lim_{x \to x_0} f(x) = l$ nel caso in cui $x_0,l \in \mathbb{R}$. Si osserva che $\delta$ può dipendere oltre che da $\varepsilon$ anche da $x_0$.
%%

> [!osservazione]+ Osservazione: interpretazione informale di _funzione continua_
> 
> In termini poco rigorosi, possiamo dire che una [funzione](Matematica/Teoria%20degli%20insiemi/Funzioni/_index.md#^definizione-funzione) è [continua](Funzioni%20continue.md#^definizione-funzione-continua) in un punto%% link %% $x_0$ del suo dominio%% link %% se a "piccole" variazioni di $x$ nelle vicinanze di $x_0$ corrispondono "piccole" variazioni di $f(x)$ nelle vicinanze di $f(x_0)$. Questa interpretazione tuttavia non è per nulla rigorosa, in quanto il concetto di "piccolo" non è ben definito. È meglio dire che $f$ è [continua](Funzioni%20continue.md#^definizione-funzione-continua) in $x_0$ se è sempre possibile avere un "controllo" delle variazioni di $f$ dal valore $f(x_0)$ al valore $f(x)$ in tutti i punti%% link %% di $x$ sufficientemente vicini a $x_0$.

> [!osservazione]+ Osservazione: funzione continua in tutti e soli i punti del suo dominio
> 
> Osserviamo che la [definizione di _continuità_](Funzioni%20continue.md#^definizione-funzione-continua) di $f$ in $x_0$ si applica in tutti e soli i punti del suo dominio%% link %%: rispetto alla [definizione di _limite_ con $x_0 \in \mathbb{R} \land l \in \mathbb{R}$](Matematica/Analisi%20matematica/Limiti/_index.md#^osservazione-limite-con-x0-finito-l-finito), infatti, in questa **non** si impone che $x \ne x_0$. Infatti, per $x = x_0$, è automaticamente verificato che
> 
> $$
> |f(x) - f(x_0)| < \varepsilon
> $$

Inoltre, dal confronto fra queste due nozioni, seguono le seguenti proposizioni.

> [!proposizione]+ Proposizione: continuità e punti di accumulazione
> 
> Data una [funzione](Matematica/Teoria%20degli%20insiemi/Funzioni/_index.md#^definizione-funzione) $f \colon \text{dom}(f) \to \mathbb{R}$ e un punto%% link %% $x_0 \in \text{dom}(f)$, si ha che, se $x_0$ è un [punto di accumulazione](Topologia%20dei%20reali.md#^definizione-punto-di-accumulazione) per $\text{dom}(f)$, allora
> 
> $$
> f \text{ è continua in } x_0 \iff \lim_{x \to x_0} f(x) = f(x_0)
> $$
^proposizione-continuita-e-punti-di-accumulazione

%% 
Dimostrazione pag. 137 Lancelotti
%%

> [!proposizione]+ Proposizione: continuità e punti isolati
> 
> Data una [funzione](Matematica/Teoria%20degli%20insiemi/Funzioni/_index.md#^definizione-funzione) $f \colon \text{dom}(f) \to \mathbb{R}$ e un punto%% link %% $x_0 \in \text{dom}(f)$, si ha che, se $x_0$ è un [punto isolato](Topologia%20dei%20reali.md#^definizione-punto-isolato) per $\text{dom}(f)$, allora $f$ è [continua](Funzioni%20continue.md#^definizione-funzione-continua) in $x_0$.
^proposiizone-continuita-e-punti-isolati

%% 
Dimostrazione pag. 137 Lancelotti
%%

> [!osservazione]+ Osservazione: importanza della proposizione su continuità e punti di accumulazione
> 
> La [proposizione su continuità e punti di accumulazione](Funzioni%20continue.md#^proposizione-continuita-e-punti-di-accumulazione) è molto importante e la useremo spesso, in quanto la bi-implicazione%% link %% ci dà due importanti affermazioni:
> 1. Seguendo la direzione dell'implicazione ($\implies$), abbiamo che
> 	$$
> 	f \text{ è continua in } x_0 \implies \lim_{x \to x_0} f(x) = f(x_0)
> 	$$
> 	cioè, se $f$ è [continua](Funzioni%20continue.md#^definizione-funzione-continua) in un punto%% link %% $x_0$ del suo dominio%% link %% in cui ha senso calcolare il [limite](Matematica/Analisi%20matematica/Limiti/_index.md#^definizione-limite) di $f(x)$ per $x \to x_0$, allora sappiamo già quanto vale questo limite, ossia vale $f(x_0)$.
> 2. Seguendo la direzione della conseguenza ($\impliedby$), abbiamo che
> 	$$
> 	\lim_{x \to x_0} f(x) = f(x_0) \implies f \text{ è continua in } x_0
> 	$$
> 	cioè, per sapere se una [funzione](Matematica/Teoria%20degli%20insiemi/Funzioni/_index.md#^definizione-funzione) $f$ è [continua](Funzioni%20continue.md#^definizione-funzione-continua) in un punto%% link %% $x_0$ del suo dominio%% link %% in cui ha senso calcolare il [limite](Matematica/Analisi%20matematica/Limiti/_index.md#^definizione-limite) di $f(x)$ per $x \to x_0$, allora è sufficiente calcolare questo limite e controllare che coincida con $f(x_0)$. In particolare, abbiamo che
> 	$$
> 	\lim_{x \to x_0} f(x) \ne f(x_0) \implies f \text{ non è continua in } x_0
> 	$$

%% 
esempio pagg. 138-141 Lancelotti
%%

%% 
[!esercizio]+ Esercizio

Determinare una [funzione](Matematica/Teoria%20degli%20insiemi/Funzioni/_index.md#^definizione-funzione) definita su tutto $\mathbb{R}$ e [continua](Funzioni%20continue.md#^definizione-funzione-continua) solo in $0$ e $1$.
%%

> [!attenzione]+ Attenzione: si può parlare di (dis)continuità solo dove $\color{#FFBF7F} f$ è definita
> 
> Non ha senso parlare di [dis(continuità)](Funzioni%20continue.md#^definizione-funzione-continua) di una [funzione](Matematica/Teoria%20degli%20insiemi/Funzioni/_index.md#^definizione-funzione) nei punti%% link %% in cui non è definita%% link %%. Per esempio,
> 
> $$
> f(x) = \dfrac{1}{x}
> $$
> 
> non è definita in $0$, pertanto non ha senso parlare di [dis(continuità)](Funzioni%20continue.md#^definizione-funzione-continua) di $f$ in $0$.

> [!proposizione]+ Proposizione
> 
> Data una [funzione](Matematica/Teoria%20degli%20insiemi/Funzioni/_index.md#^definizione-funzione) $f \colon \text{dom}(f) \to \mathbb{R}$ e un [punto di accumulazione](Topologia%20dei%20reali.md#^definizione-punto-di-accumulazione) $x_0$ per $\text{dom}(f)$, abbiamo che
> 
> $$
> \begin{array}{}
> \lim_{x \to x_0} f(x) = l \in \mathbb{R} \\
> \Updownarrow \\
> \tilde f \text{ è continua in } x_0
> \end{array}
> $$
> 
> Dove la [funzione](Matematica/Teoria%20degli%20insiemi/Funzioni/_index.md#^definizione-funzione) $\tilde f \colon \text{dom}(f) \cup \{ x_0 \} \to \mathbb{R}$ è definita da
> 
> $$
> \tilde f(x) = \begin{cases}
> f(x) & \text{se } x \ne x_0 \\
> l & \text{se } x = x_0
> \end{cases}
> $$

%% 
La chiamerei:

**"Caratterizzazione del limite tramite prolungamento continuo"**

oppure, più brevemente, **"Criterio del prolungamento per continuità"**.

L'idea è proprio quella: il limite esiste (ed è finito) se e solo se si riesce a *prolungare* (o *estendere*) ff f in x0x_0 x0​ ottenendo una funzione continua f~\tilde{f} f~​. Il nome cattura entrambe le direzioni del doppio implicazione.
%%

%% 
dimostrazione pag. 142 Lancelotti
%%

> [!lemma]+ Lemma%% della proposizione X %%
> 
> Per ogni punto%% link %% $x \in \mathbb{R}$, si ha che
> 
> $$
> |\sin x| \le |x|
> $$
> 
> e, inoltre,
> 
> $$
> |\sin x| = |x| \iff x = 0
> $$

%% 
dimostrazione pag. 143 lancelotti
%%

%% 
Osservazione: sono funzioni continui sui lroo domini le funioni elementari

pagg. 143-144 lancelotti
%%

> [!osservazione]+ Osservazione: località e globalità delle nozioni dell'analisi matematica
> 
> Le nozioni e le proprietà che si studiano in analisi matematica%% link %% si possono distinguere in due classi: **locali** e **globali**.
> 
> Sono _locali_ quelle che si realizzano nelle "vicinanze" di un punto%% Link %% di una [funzione](Matematica/Teoria%20degli%20insiemi/Funzioni/_index.md#^definizione-funzione), ossia coinvolgono (riguardano) solo certi punti%% link %%, mentre sono _globali_ quelle che coinvolgono tutti i punti%% Link %% di quella [funzione](Matematica/Teoria%20degli%20insiemi/Funzioni/_index.md#^definizione-funzione).
> 
> Per esempio, riferite alle nozioni sin qui introdotte sulle [funzioni](Matematica/Teoria%20degli%20insiemi/Funzioni/_index.md#^definizione-funzione), sono nozioni locali quella di [limite](Matematica/Analisi%20matematica/Limiti/_index.md#^definizione-limite) e quella di [funzione continua](Funzioni%20continue.md#^definizione-funzione-continua); infatti, sono definite coinvolgendo solo i punti%% Link %% in un [intorno](Topologia%20dei%20reali.md#^definizione-intorno-di-un-punto) del punto%% Link %% a cui tende la variabile indipendente%% link %%.
> 
> Sono invece globali l'[iniettività](Matematica/Teoria%20degli%20insiemi/Funzioni/_index.md#^definizione-iniettivita), la [suriettività](Matematica/Teoria%20degli%20insiemi/Funzioni/_index.md#^definizione-suriettivita), la [biettività](Matematica/Teoria%20degli%20insiemi/Funzioni/_index.md#^definizione-biettivita), la monotonia%% Link %%, la simmetria%% link %%, la periodicità%% Link %%; infatti, sono definite coinvolgendo ogni punto%% link %% del dominio%% link %%.
> 
> Altre nozioni locali sono, per esempio, quelle di massimo%% link %% e di minimo locale%% link %%, mentre sono globali quelle di massimo%% Link %% e di minimo assoluto%% Link %%.
^osservazione-localita-e-globalita-delle-nozioni-dell-analisi-matematica

%% non so se è giusto metterla qui questa osservazione o se metterla in [Analisi matematica](Matematica/Analisi%20matematica/_index.md) %%

# 1 - Funzioni continue dai lati

> [!definizione]+ Definizione: funzione continua da destra
> 
> Data una [funzione](Matematica/Teoria%20degli%20insiemi/Funzioni/_index.md#^definizione-funzione) $f \colon \text{dom}(f) \to \mathbb{R}$ e un [punto di accumulazione](Topologia%20dei%20reali.md#^definizione-punto-di-accumulazione) $x_0 \in \mathbb{R}$ per $\text{dom}(f)$, diciamo che **$f$ è continua da destra in $x_0$** se $f$ [ristretta](Matematica/Teoria%20degli%20insiemi/Funzioni/_index.md#^definizione-funzione-restrizione) a $\text{dom}(f) \cap [x_0, + \infty)$ è [continua](Funzioni%20continue.md#^definizione-funzione-continua) in $x_0$:
> 
> $$
> \begin{array}{}
> f \text{ continua da destra in } x_0 \\
> \Updownarrow \\
> f_{|\text{dom}(f) \cap [x_0, + \infty)} \text{ continua in } x_0
> \end{array}
> $$
^definizione-funzione-continua-da-destra

> [!definizione]+ Definizione: funzione continua da sinistra
> 
> Data una [funzione](Matematica/Teoria%20degli%20insiemi/Funzioni/_index.md#^definizione-funzione) $f \colon \text{dom}(f) \to \mathbb{R}$ e un [punto di accumulazione](Topologia%20dei%20reali.md#^definizione-punto-di-accumulazione) $x_0 \in \mathbb{R}$ per $\text{dom}(f)$, diciamo che **$f$ è continua da sinistra in $x_0$** se $f$ [ristretta](Matematica/Teoria%20degli%20insiemi/Funzioni/_index.md#^definizione-funzione-restrizione) a $\text{dom}(f) \cap (-\infty, x_0]$ è [continua](Funzioni%20continue.md#^definizione-funzione-continua) in $x_0$:
> 
> $$
> \begin{array}{}
> f \text{ continua da sinistra in } x_0 \\
> \Updownarrow \\
> f_{|\text{dom}(f) \cap (-\infty, x_0]} \text{ continua in } x_0
> \end{array}
> $$
^definizione-funzione-continua-da-sinistra

> [!proposizione]+ Proposizione: $\color{#FF7F7F} f$ continua solo se continua dai lati
> 
> Data una [funzione](Matematica/Teoria%20degli%20insiemi/Funzioni/_index.md#^definizione-funzione) $f \colon \text{dom}(f) \to \mathbb{R}$ e un [punto di accumulazione](Topologia%20dei%20reali.md#^definizione-punto-di-accumulazione) $x_0 \in \mathbb{R}$ per $\text{dom}(f)$, abbiamo che $f$ è [continua](Funzioni%20continue.md#^definizione-funzione-continua) in $x_0$ se e solo se $f$ è [continua da destra](Funzioni%20continue.md#^definizione-funzione-continua-da-destra) e [da sinistra](Funzioni%20continue.md#^definizione-funzione-continua-da-sinistra) in $x_0$:
> 
> $$
> \begin{array}{}
> f \text{ continua in } x_0 \\
> \Updownarrow \\
> f \text{ continua da destra e da sinistra in } x_0
> \end{array}
> $$

> [!proposizione]+ Proposizione: $\color{#FF7F7F} f$ continua dai lati solo se limite uguale a $\color{#FF7F7F} f(x_0)$
> 
> Data una [funzione](Matematica/Teoria%20degli%20insiemi/Funzioni/_index.md#^definizione-funzione) $f \colon \text{dom}(f) \to \mathbb{R}$ e un [punto di accumulazione](Topologia%20dei%20reali.md#^definizione-punto-di-accumulazione) $x_0 \in \mathbb{R}$ per $\text{dom}(f) \cap [x_0, + \infty)$, abbiamo che
> 
> $$
> \begin{array}{}
> f \text{ continua da destra in } x_0 \\
> \Updownarrow \\
> \displaystyle\lim_{x \to x_0^+} f(x) = f(x_0)
> \end{array}
> $$
> 
> Dato invece un [punto di accumulazione](Topologia%20dei%20reali.md#^definizione-punto-di-accumulazione) $x_0 \in \mathbb{R}$ per $\text{dom}(f) \cap (-\infty, x_0]$, abbiamo che
> 
> $$
> \begin{array}{}
> f \text{ continua da sinistra in } x_0 \\
> \Updownarrow \\
> \displaystyle\lim_{x \to x_0^-} f(x) = f(x_0)
> \end{array}
> $$

> [!proposizione]+ Proposizione: $\color{#FF7F7F} f$ definita per $\color{#FF7F7F} x \lesseqgtr x_0$ continua anche dai lati
> 
> Se una [funzione](Matematica/Teoria%20degli%20insiemi/Funzioni/_index.md#^definizione-funzione) è definita solo per $x \ge x_0$, allora è la stessa cosa dire che $f$ è [continua](Funzioni%20continue.md#^definizione-funzione-continua) in $x_0$ e dire che $f$ è [continua da destra](Funzioni%20continue.md#^definizione-funzione-continua-da-destra) in $x_0$:
> 
> $$
> \begin{array}{}
> f \text{ continua in } x_0 \\
> \Updownarrow \\
> f \text{ continua da destra in } x_0
> \end{array}
> $$
> 
> Analogicamente, se una [funzione](Matematica/Teoria%20degli%20insiemi/Funzioni/_index.md#^definizione-funzione) è definita solo per $x \le x_0$, allora è la stessa cosa dire che $f$ è [continua](Funzioni%20continue.md#^definizione-funzione-continua) in $x_0$ e dire che $f$ è [continua da sinistra](Funzioni%20continue.md#^definizione-funzione-continua-da-sinistra) in $x_0$:
> 
> $$
> \begin{array}{}
> f \text{ continua in } x_0 \\
> \Updownarrow \\
> f \text{ continua da sinistra in } x_0
> \end{array}
> $$

# 2 - Punti di discontinuità

> [!definizione]+ Definizione: discontinuità eliminabile
> 
> Data una [funzione](Matematica/Teoria%20degli%20insiemi/Funzioni/_index.md#^definizione-funzione) $f \colon \text{dom}(f) \to \mathbb{R}$ e un [punto di accumulazione](Topologia%20dei%20reali.md#^definizione-punto-di-accumulazione) $x_0 \in \mathbb{R}$ per $\text{dom}(f)$, diciamo che $f$ ha una **discontinuità eliminabile in $x_0$** (oppure che $x_0$ è un **punto di discontinuità eliminabile per $f$**) se esiste il [limite](Matematica/Analisi%20matematica/Limiti/_index.md#^definizione-limite)
> 
> $$
> \lim_{x \to x_0} f(x) = l \in \mathbb{R}
> $$
> 
> con $l \ne f(x_0)$.
^definizione-discontinuita-eliminabile

> [!osservazione]+ Osservazione: perché si chiama "discontinuità eliminabile"
> 
> La denominazione "discontinuità eliminabile" sta ad indicare che, a patto di modificare la [funzione](Matematica/Teoria%20degli%20insiemi/Funzioni/_index.md#^definizione-funzione) $f$ in modo opportuno nel punto%% link %% $x_0$, questa discontinuità si può eliminare, semplicemente ponendo il valore di $f(x_0)$ uguale a $l$. Infatti, la [funzione](Matematica/Teoria%20degli%20insiemi/Funzioni/_index.md#^definizione-funzione) $\hat f \colon \text{dom}(f) \to \mathbb{R}$ definita da
> 
> $$
> \hat f(x) = \begin{cases}
> f(x) & \text{se } x \ne x_0 \\
> l & \text{se } x = x_0
> \end{cases}
> $$
> 
> coincide con $f$ dappertutto tranne che in $x_0$ ed è [continua](Funzioni%20continue.md#^definizione-funzione-continua) in $x_0$ (mentre $f$ non lo è).

> [!definizione]+ Definizione: discontinuità di prima specie (o salto)
> 
> Data una [funzione](Matematica/Teoria%20degli%20insiemi/Funzioni/_index.md#^definizione-funzione) $f \colon \text{dom}(f) \to \mathbb{R}$ e un [punto di accumulazione](Topologia%20dei%20reali.md#^definizione-punto-di-accumulazione) $x_0 \in \mathbb{R}$ per $\text{dom}(f)$, diciamo che $f$ ha una **discontinuità di prima specie (o salto) in $x_0$** (oppure che $x_0$ è un **punto di discontinuità di prima specie (o salto) per $f$**) se esistono finiti e diversi fra loro i [limiti](Matematica/Analisi%20matematica/Limiti/_index.md#^definizione-limite) $\displaystyle\lim_{x \to x_0^{\pm}} f(x)$:
> 
> $$
> \lim_{x \to x_0^+} f(x) = l \ne l' = \lim_{x \to x_0^-} f(x)
> $$
^definizione-discontinuita-di-prima-specie-o-salto

> [!definizione]+ Definizione: discontinuità di seconda specie
> 
> Data una [funzione](Matematica/Teoria%20degli%20insiemi/Funzioni/_index.md#^definizione-funzione) $f \colon \text{dom}(f) \to \mathbb{R}$ e un [punto di accumulazione](Topologia%20dei%20reali.md#^definizione-punto-di-accumulazione) $x_0 \in \mathbb{R}$ per $\text{dom}(f)$, diciamo che $f$ ha una **discontinuità di seconda specie in $x_0$** (oppure che $x_0$ è un **punto di discontinuità di seconda specie per $f$**) se almeno uno tra il [limite destro](Matematica/Analisi%20matematica/Limiti/_index.md#^definizione-limite-destro) $\displaystyle\lim_{x \to x_0^-} f(x)$ o il [limite sinistro](Matematica/Analisi%20matematica/Limiti/_index.md#^definizione-limite-sinistro) $\displaystyle\lim_{x \to x_0^+} f(x)$ è uguale a $\pm \infty$ o non esiste.
^definizione-discontinuita-di-seconda-specie

%% 
esempio pagg. 150-151 lancelotti
%%

# 3 - Algebra delle funzioni continue

%% 
pagg. 158-160
%%

---

> [!fonti]+ Fonti
> 
> - 📚 _Lezioni di Analisi Matematica I_ di Sergio Lancelotti, Celid, 2020 (ISBN: `978-8867891979`):
> 	- Capitolo 3 - _Limiti e continuità_:
> 		- 2 - _Limiti di funzioni_:
> 			- 2.1 - _Funzioni continue_.
> 			- 2.2 - _Limiti laterali_.
> 			- 2.4 - _Punti di discontinuità_.
> 	- Capitolo 3 - _Limiti e continuità_:
> 		- 3 - _Teoremi su limiti e continuità_:
> 			- 3.2 - _Algebra delle funzioni continue_.
