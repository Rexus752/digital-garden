---
title: Limiti notevoli
---

> [!premessa] Premessa
> 
> Ciao! Se è la prima volta che capiti su questo sito, ti consiglio di consultare la [pagina principale](index.md) di questo cosiddetto _Giardino Digitale_ per scoprire meglio cos'è e come navigarlo.
> 
> Lo stato di questa nota è al momento: 🔴 <font color="#FF7F7F">_Bozza_</font>.

---

Ci sono alcuni [limiti](content/Matematica/Analisi%20matematica/Limiti/_index.md#^definizione-limite) particolari di cui è sempre noto il loro valore, detti [_limiti notevoli_](Limiti%20notevoli.md#^definizione-limite-notevole).

> [!definizione] Definizione: limite notevole
> 
> Un **limite notevole** è un [limite](content/Matematica/Analisi%20matematica/Limiti/_index.md#^definizione-limite) di una [forma indeterminata](content/Matematica/Analisi%20matematica/Limiti/_index.md#^definizione-forma-indeterminata), il cui valore è noto e dimostrato, usato come formula pronta per calcolare limiti più complessi senza dover ricorrere ogni volta alla dimostrazione%% link %%.
^definizione-limite-notevole

# Limiti notevoli delle funzioni trigometriche

## Seno

### Tendente a $0$

> [!proposizione] Proposizione: limite notevole del seno tendente a $0$
> 
> Vale il seguente [limite notevole](content/Matematica/Analisi%20matematica/Limiti/_index.md#^definizione-limite-notevole):
> 
> $$
> \lim_{x \to 0} \dfrac{\sin x}{x} = 1
> $$
^proposizione-limite-notevole-del-seno-tendente-a-0

%%
[!dimostrazione] Dimostrazione del limite notevole del seno tendente a $0$

Questo [limite](content/Matematica/Analisi%20matematica/Limiti/_index.md#^definizione-limite) è una [forma indeterminata](content/Matematica/Analisi%20matematica/Limiti/_index.md#^definizione-forma-indeterminata) del tipo $\dfrac{0}{0}$.

Osserviamo che la [funzione](content/Matematica/Teoria%20degli%20insiemi/Funzioni/_index.md#^definizione-funzione) $f(x) = \dfrac{\sin x}{x}$ è [pari](content/Matematica/Teoria%20degli%20insiemi/Funzioni/_index.md#^definizione-funzioni-pari-e-dispari), infatti il dominio(Link) $\text{dom}(f) = (-\infty, 0) \cup (0, +\infty)$ è simmetrico rispetto a $0$ e

$$
\forall x \ne 0 . \left( f(-x) = \dfrac{\sin(-x)}{-x} = \dfrac{-\sin x}{-x} = \dfrac{\sin x}{x} = f(x) \right) 
$$

Per questo motivo(perché? dov'è scritto questo?), è sufficiente calcolare $\displaystyle\lim_{x \to 0^+} \dfrac{\sin x}{x}$.

pag. 172-173 lancelotti
%%

### Tendente all'infinito

> [!proposizione] Proposizione: limite notevole del seno tendente all'infinito
> 
> Vale il seguente [limite notevole](content/Matematica/Analisi%20matematica/Limiti/_index.md#^definizione-limite-notevole):
> 
> $$
> \lim_{x \to \pm \infty} \dfrac{\sin x}{x} = 0
> $$
^proposizione-limite-notevole-del-seno-tendente-all-infinito

%% dimostrazione pag. 174 lancelotti %%

## Coseno

### Tendente a $0$

> [!proposizione] Proposizione: Tendente a $0$
> 
> Vale il seguente [limite notevole](content/Matematica/Analisi%20matematica/Limiti/_index.md#^definizione-limite-notevole):
> 
> $$
> \lim_{x \to 0} \dfrac{1 - \cos x}{x^2} = \dfrac{1}{2}
> $$
^proposizione-limite-notevole-del-coseno-tendente-a-0

%% dimostrazione pag. 173 lancelotti %%

### Tendente all'infinito

> [!proposizione] Proposizione: Tendente all'infinito
> 
> Vale il seguente [limite notevole](content/Matematica/Analisi%20matematica/Limiti/_index.md#^definizione-limite-notevole):
> 
> $$
> \lim_{x \to \pm \infty} \dfrac{\cos x}{x} = 0
> $$
^proposizione-limite-notevole-del-coseno-tendente-all-infinito

%% dimostrazione pag. 174 lancelotti %%

## Tangente

> [!proposizione] Proposizione: limite notevole della tangente
> 
> Vale il seguente [limite notevole](content/Matematica/Analisi%20matematica/Limiti/_index.md#^definizione-limite-notevole):
> 
> $$
> \lim_{x \to 0} \dfrac{\tan x}{x} = 1
> $$
^proposizione-limite-notevole-della-tangente

%% 
dimostrazione pag. 173 lancelotti
%%

%% 
e il limite notevole della tangente all'infinito?
%%

%% 
Esercizio 3.33 pag. 174
%%

# Lemma del modulo

%% 
va qui questo lemma?
e a che serve?
%%

> [!lemma] Lemma del modulo
> 
> Data una [funzione](Matematica/Teoria%20degli%20insiemi/Funzioni/_index.md#^definizione-funzione) $f \colon \text{dom}(f) \to \mathbb{R}$, un [punto di accumulazione](Topologia%20dei%20reali.md#^definizione-punto-di-accumulazione) $x_0 \in \mathbb{R} \cup \{ \pm \infty \}$ per $\text{dom}(f)$, abbiamo che
> 
> $$
> \lim_{x \to x_0} f(x) = 0 \iff \lim_{x \to x_0} |f(x)| = 0
> $$
^lemma-del-modulo

%% 
Dimostrazione: è un'immediata conseguenza della definizione di limite (per esercizio)
%%

%% 
Osservazioni 3.38 pagg. 174-175
con relative dimostrazioni
%%

> [!corollario] Corollario del lemma del modulo
> 
> Date due [funzioni](content/Matematica/Teoria%20degli%20insiemi/Funzioni/_index.md#^definizione-funzione) $f,g \colon A \subseteq \mathbb{R} \to \mathbb{R}$ (con $A \ne \emptyset$) e un [punto di accumulazione](Topologia%20dei%20reali.md#^definizione-punto-di-accumulazione) $x_0 \in \mathbb{R} \cup \{ \pm \infty \}$ per $A$, se esiste un [intorno](Topologia%20dei%20reali.md#^definizione-intorno-di-un-punto) $I(x_0)$ di $x_0$ tale che $f$ sia limitata%% link %% su $(A \cap I(x_0)) \setminus \{ x_0 \}$ e vale il [limite](content/Matematica/Analisi%20matematica/Limiti/_index.md#^definizione-limite) $\displaystyle\lim_{x \to x_0} g(x) = 0$, allora
> 
> $$
> \lim_{x \to x_0} \big( f(x) \circ g(x) \big)  = 0
> $$
^corollario-del-lemma-del-modulo

%% dimostrazione pag. 175 lancelotti %%

%% osservazioni 3.40 pag. 175 lancelotti %%

%% esempi pagg. 176-177 lancelotti %%

# Limiti notevoli di forme indeterminate

## Esponenziali

### Risoluzione delle esponenziali

> [!osservazione] Osservazione: forma alternativa delle forme indeterminate esponenziali
> 
> I teoremi elementari%% cosa si intende per "elementari"? %% sui limiti, come l'algebra dei limiti%% sostituire "algebra dei limiti" con teoremi dell'algebra dei limiti e linkare %%, regola di De L'Hôpital%% link %% e infinitesimi equivalenti%% link %% si applicano a [forme indeterminate algebriche](Forme%20indeterminate.md#^definizione-forma-indeterminata-algebrica).
> 
> Le [forme indeterminate esponenziali](Forme%20indeterminate.md#^definizione-forma-indeterminata-esponenziale) del tipo [$1^\infty$](Forme%20indeterminate.md#^definizione-forma-indeterminata-espnenziale-del-tipo-1-all-infinito), [$\infty^0$](Forme%20indeterminate.md#^definizione-forma-indeterminata-esponenziale-del-tipo-infinito-allo-zero) e [$0^0$](Forme%20indeterminate.md#^definizione-forma-indeterminata-esponenziale-del-tipo-0-alla-0) coinvolgono un [limite](content/Matematica/Analisi%20matematica/Limiti/_index.md#^definizione-limite) della forma
> 
> $$
> \lim_{x \to x_0} [f(x)]^{g(x)}
> $$
> 
> che non è direttamente riconducibile a nessuna [forma indeterminata algebrica](Forme%20indeterminate.md#^definizione-forma-indeterminata-algebrica). Tuttavia, sfruttando il fatto che la funzione esponenziale%% link %% e il logaritmo naturale%% link %% sono una l'inversa%% link %% dell'altra%% link a una proposizione in cui dimostro il legame tra queste due funzioni %%, si può scrivere
> 
> $$
> [f(x)]^{g(x)} = e^{\ln [f(x)]^{g(x)}} = e^{g(x) \ln f(x)}
> $$
> 
> e, poiché $e$ è [continua](Funzioni%20continue.md#^definizione-funzione-continua)%% dimostrare che $e$ è continua %%, il [limite](content/Matematica/Analisi%20matematica/Limiti/_index.md#^definizione-limite) si riconduce a
> 
> $$
> \lim_{x \to x_0} [f(x)]^{g(x)} = e^{\displaystyle\lim_{x \to x_0} \big( g(x) \ln f(x) \big)}
> $$
> 
> %% perché si ha questa trasformazione? %%
> 
> Il problema si riduce quindi allo studio del [limite](content/Matematica/Analisi%20matematica/Limiti/_index.md#^definizione-limite) dell'esponente%% link %% $g(x) \ln f(x)$, che è un prodotto e ricade nella [forma indeterminata algebrica del tipo $0 \cdot \infty$](Forme%20indeterminate.md#^definizione-forma-indeterminata-algebrica-del-tipo-0-per-infinito). Questa identità%% link %% costituisce il metodo standard per ricondurre qualsiasi [forma indeterminata esponenziale](Forme%20indeterminate.md#^definizione-forma-indeterminata-esponenziale) a una [algebrica](Forme%20indeterminate.md#^definizione-forma-indeterminata-algebrica).
^osservazione-forma-alternativa-delle-forme-indeterminate-esponenziali

> [!proposizione] Proposizione: risoluzione delle forme indeterminate esponenziali
> 
> Date due [funzioni](content/Matematica/Teoria%20degli%20insiemi/Funzioni/_index.md#^definizione-funzione) $f, g \colon A \subseteq \mathbb{R} \to \mathbb{R}$ (con $A \ne \emptyset$) e un [punto di accumulazione](Topologia%20dei%20reali.md#^definizione-punto-di-accumulazione) $x_0 \in \mathbb{R} \cup \{\pm\infty\}$ per $A$, supposto che esista il [limite](content/Matematica/Analisi%20matematica/Limiti/_index.md#^definizione-limite) $\displaystyle\lim_{x \to x_0} \big( g(x) \ln f(x) \big)$, per il [teorema del limite della funzione composta](Limiti%20delle%20funzioni%20composte.md#^teorema-del-limite-della-funzione-composta) e il [teorema del limite della funzione composta continua](Limiti%20delle%20funzioni%20composte.md#^teorema-del-limite-della-funzione-composta-continua) e per la continuità di $e$%% link alla continuità di $e$ %%, si ha che:
> 
> $$
> \lim_{x \to x_0} [f(x)]^{g(x)} = \displaystyle\lim_{x \to x_0}e^{ g(x) \ln f(x)} = \begin{cases}
> e^l & \text{se } \displaystyle\lim_{x \to x_0} \big( g(x) \ln f(x) \big) = l \in \mathbb{R} \\
> + \infty & \text{se } \displaystyle\lim_{x \to x_0} \big( g(x) \ln f(x) \big) = + \infty \\
> 0 & \text{se } \displaystyle\lim_{x \to x_0} \big( g(x) \ln f(x) \big) = - \infty
> \end{cases}
> $$
^proposizione-risoluzione-delle-forme-indeterminate-esponenziali

> [!dimostrazione] Dimostrazione della risoluzione delle forme indeterminate esponenziali
> 
> Poniamo $\varphi(x) = g(x) \ln f(x)$ e $h(t) = e^t$, cosicché 
> 
> $$
> [f(x)]^{g(x)} = e^{ g(x) \ln f(x)} = h(\varphi(x))
> $$
> 
> Per ipotesi esiste il [limite](content/Matematica/Analisi%20matematica/Limiti/_index.md#^definizione-limite) $\displaystyle\lim_{x \to x_0} \big( g(x) \ln f(x) \big) = \displaystyle\lim_{x \to x_0} \varphi(x) = l$, con $l \in\mathbb{R} \cup \{ \pm \infty \}$. Analizziamo ogni possibile caso in cui può ricadere $l$:
> - $l \in \mathbb{R}$: poiché $h(t) = e^t$ è continua su $\mathbb{R}$%% link alla continuità di $e$ %%, per il [teorema del limite della funzione composta continua](Limiti%20delle%20funzioni%20composte.md#^teorema-del-limite-della-funzione-composta-continua) abbiamo che
> 	$$
> 	\lim_{x \to x_0} h(\varphi(x)) = h \left( \lim_{x \to x_0} \varphi(x) \right) = h(l) = e^l
> 	$$
> - $l = +\infty$: per definizione di limite infinito%% link %%, per ogni $M > 0$ esiste un [intorno](Topologia%20dei%20reali.md#^definizione-intorno-di-un-punto) $I(x_0)$ tale che $\varphi(x) > M$ per ogni $x \in (A \cap I(x_0)) \setminus {x_0}$. Poiché $h(t) = e^t$ è strettamente crescente e $\displaystyle\lim_{t \to +\infty} e^t = +\infty$, si ha $e^{\varphi(x)} > e^M$ per ogni tale $x$, e poiché $e^M \to +\infty$ al crescere di $M$, si conclude
> 	$$
> 	\lim_{x \to x_0} e^{\varphi(x)} = +\infty
> 	$$
> - $l = -\infty$: analogamente, per ogni $\varepsilon > 0$ esiste un [intorno](Topologia%20dei%20reali.md#^definizione-intorno-di-un-punto) $I(x_0)$ tale che $\varphi(x) < -M$ per ogni $x \in (A \cap I(x_0)) \setminus {x_0}$, con $M > 0$ arbitrariamente grande. Poiché $\displaystyle\lim_{t \to -\infty} e^t = 0^+$, si ha $0 < e^{\varphi(x)} < e^{-M}$ per ogni tale $x$, e poiché $e^{-M} \to 0$ al crescere di $M$, si conclude
> 	$$
> 	\lim_{x \to x_0} e^{\varphi(x)} = 0
> 	$$
> 
> $\blacksquare$
^dimostrazione-della-risoluzione-delle-forme-indeterminate-esponenziali

> [!osservazione] Osservazione: base costantemente uguale a $1$ in un intorno di $x_0$
> 
> Se durante la [risoluzione delle forme indeterminate esponenziali](Limiti%20notevoli.md#^proposizione-risoluzione-delle-forme-indeterminate-esponenziali) abbiamo che la base%% link %% $f(x)$ è uguale a $1$ in tutto un [intorno](Topologia%20dei%20reali.md#^definizione-intorno-di-un-punto) di $x_0$, escluso $x_0$, allora il [limite](content/Matematica/Analisi%20matematica/Limiti/_index.md#^definizione-limite)
> 
> $$
> \lim_{x \to x_0} [f(x)]^{g(x)}
> $$
> 
> **non** è una [forma indeterminata esponenziale del tipo $1^\infty$](Forme%20indeterminate.md#^definizione-forma-indeterminata-espnenziale-del-tipo-1-all-infinito). Infatti, in tal caso,
> 
> $$
> \lim_{x \to x_0} [f(x)]^{g(x)} = \lim_{x\to x_0} \underbrace{1^{g(x)}}_{=1} = \lim_{x \to x_0} 1 = 1
> $$

%% 
osservazione c pagina 185
%%

### Tipo $1^\infty$

#### Limite notevole di Eulero

> [!teorema] Teorema: limite notevole di Eulero
> 
> Vale il seguente [limite notevole](content/Matematica/Analisi%20matematica/Limiti/_index.md#^definizione-limite-notevole):
> 
> $$
> \lim_{x \to \pm \infty} \left( 1 + \dfrac{1}{x} \right)^x = e
> $$
^teorema-limite-notevole-di-eulero

%% 
Il secondo è il nome più diffuso, poiché questo limite è storicamente attribuito a Eulero ed è precisamente la definizione originaria del numero e — tanto che in molti testi il numero di Eulero viene *definito* proprio come il valore di questo limite, e le proprietà di ee e vengono poi dedotte da esso.
%%

Tralasciamo la dimostrazione%% link %% di [questo teorema](Limiti%20notevoli.md#^teorema-limite-notevole-di-eulero) che non è per nulla banale. Tuttavia, possiamo facilmente intuire che questo [limite](content/Matematica/Analisi%20matematica/Limiti/_index.md#^definizione-limite) è una [forma indeterminata esponenziale del tipo $1^\infty$](Forme%20indeterminate.md#^definizione-forma-indeterminata-espnenziale-del-tipo-1-all-infinito).

#### Generalizzazione del limite notevole di Eulero

> [!proposizione] Proposizione: generalizzazione del limite notevole di Eulero
> 
> Vale il seguente [limite notevole](content/Matematica/Analisi%20matematica/Limiti/_index.md#^definizione-limite-notevole):
> 
> $$
> \forall a \in \mathbb{R} . \left( \lim_{x \to \pm \infty} \left( 1 + \dfrac{a}{x} \right) ^x = e^a \right) 
> $$
^proposizione-generalizzazione-del-limite-notevole-di-eulero

%% 
È il nome più appropriato perché questa proposizione è esattamente la versione parametrica del limite di Eulero: sostituendo $a = 1$ si recupera il caso fondamentale $\displaystyle\lim_{x \to \pm\infty} \left(1 + \frac{1}{x}\right)^x = e$. Il parametro $a \in \mathbb{R}$ generalizza il risultato a qualsiasi potenza di $e$, rendendo il limite uno strumento molto più flessibile per il calcolo delle forme indeterminate del tipo $1^\infty$.
%%

%% dimostrazione pag. 185 lancelotti %%

#### Limite notevole di Eulero in forma locale

> [!proposizione] Proposizione: limite notevole di Eulero in forma locale
> 
> Vale il seguente [limite notevole](content/Matematica/Analisi%20matematica/Limiti/_index.md#^definizione-limite-notevole):
> 
> $$
> \lim_{x \to 0} (1 + x)^{\frac{1}{x}} = e
> $$
^proposizione-limite-notevole-di-eulero-in-forma-locale

%% 
Il nome è giustificato dalla sostituzione $x \mapsto \frac{1}{x}$, che trasforma il limite notevole di Eulero $\displaystyle\lim_{x \to \pm\infty}\left(1+\frac{1}{x}\right)^x = e$ nel limite per $x \to 0$ — i due sono quindi la stessa proposizione espressa in due "scale" diverse: una all'infinito, l'altra in un intorno dell'origine. Il termine **locale** riflette proprio il fatto che $x \to 0$ descrive il comportamento della funzione in un intorno del punto $0$, anziché all'infinito.
%%

%% 
dimostrazione pag. 186 lanceltti
%%

#### Generalizzazione del limite notevole di Eulero in forma locale

> [!proposizione] Proposizione: generalizzazione del limite notevole di Eulero in forma locale
> 
> Vale il seguente [limite notevole](content/Matematica/Analisi%20matematica/Limiti/_index.md#^definizione-limite-notevole):
> 
> $$
> \forall a \in \mathbb{R} . \left( \lim_{x \to 0} (1 + ax)^{\frac{1}{x}} = e^a \right) 
> $$
^proposizione-generalizzazione-del-limite-notevole-di-eulero-in-forma-locale

%% dimostrazione pagina 186 lancelotti %%

## Forme indeterminate algebriche

### Tipo $\dfrac{0}{0}$

#### Limite notevole del logaritmo

> [!proposizione] Proposizione: limite notevole del logaritmo
> 
> Vale il seguente [limite notevole](content/Matematica/Analisi%20matematica/Limiti/_index.md#^definizione-limite-notevole):
> 
> $$
> \forall a > 0, a \ne 1 . \left( \lim_{x \to 0} \dfrac{\log_a (1+x)}{x} = \dfrac{1}{\ln a} \right) 
> $$
^proposizione-limite-notevole-del-logaritmo

%% 
dimostrazione pag. 186 lancelotti
%%

#### Limite notevole dell'esponenziale

> [!proposizione] Proposizione: limite notevole dell'esponenziale
> 
> Vale il seguente [limite notevole](content/Matematica/Analisi%20matematica/Limiti/_index.md#^definizione-limite-notevole):
> 
> $$
> \forall a > 0 . \left( \lim_{x \to 0} \dfrac{a^x - 1}{x} = \ln a \right) 
> $$
^proposizione-limite-notevole-dell-esponenziale

%% 
dimostrazione pag. 186 lancelotti
%%

#### Limite notevole della potenza

> [!proposizione] Proposizione: limite notevole della potenza
> 
> Vale il seguente [limite notevole](content/Matematica/Analisi%20matematica/Limiti/_index.md#^definizione-limite-notevole):
> 
> $$
> \forall a \in \mathbb{R} . \left( \lim_{x \to 0} \dfrac{(1+x)^a - 1}{x} = a \right) 
> $$
^proposizione-limite-notevole-della-potenza

%% dimostrazione pag. 187 lancelotti %%

### Tipo $\dfrac{\infty}{\infty}$

#### Limite notevole dell'esponenziale

%% 
anche quelli del tipo $\dfrac{0}{0}$ si chiamano esponenziale e logaritmo, cambiare nome (es. esponenziale parametrico?)
%%

> [!proposizione] Proposizione: limite notevole dell'esponenziale a base maggiore di $1$
> 
> Vale il seguente [limite notevole](content/Matematica/Analisi%20matematica/Limiti/_index.md#^definizione-limite-notevole):
> 
> $$
> \forall a > 1, \forall k > 0 . \left( \lim_{x \to + \infty} \dfrac{x^k}{a^x} = 0 \right)
> $$
^proposizione-limite-notevole-dell-esponenziale-a-base-maggiore-di-1

%%
Da questo [limite notevole](content/Matematica/Analisi%20matematica/Limiti/_index.md#^definizione-limite-notevole) ne derivano altri: FARE LISTA
%%

> [!corollario] Corollario: limite notevole dell'esponenziale a base minore di $1$
> 
> Vale il seguente [limite notevole](content/Matematica/Analisi%20matematica/Limiti/_index.md#^definizione-limite-notevole):
> 
> $$
> \forall 0 < a < 1, \forall k > 0 . \left( \lim_{x \to - \infty} \dfrac{|x|^k}{a^x} = 0 \right) 
> $$
^corollario-limite-notevole-dell-esponenziale-a-base-minore-di-1

%% 
dimostrazione pag. 188 lancelotti
%%

> [!corollario] Corollario: limite notevole del reciproco dell'esponenziale a base minore di $1$
> 
> Vale il seguente [limite notevole](content/Matematica/Analisi%20matematica/Limiti/_index.md#^definizione-limite-notevole):
> 
> $$
> \forall 0 < a < 1, \forall k > 0 . \left( \lim_{x \to -\infty} \dfrac{a^x}{|x|^k} = + \infty \right) 
> $$

#### Limite notevole del logaritmo

> [!proposizione] Proposizione: limite notevole del logaritmo a base maggiore di $1$
> 
> Vale il seguente [limite notevole](content/Matematica/Analisi%20matematica/Limiti/_index.md#^definizione-limite-notevole):
> 
> $$
> \forall a > 1, \forall k > 0 . \left( \lim_{x \to + \infty} \dfrac{\log_a x}{x^k} = 0 \right)
> $$
^proposizione-limite-notevole-del-logaritmo-a-base-maggiore-di-1

%% 
dimostrazione pag. 187 lancelotti
%%

> [!corollario] Corollario: limite notevole del logaritmo a base minore di $1$
> 
> Vale il seguente [limite notevole](content/Matematica/Analisi%20matematica/Limiti/_index.md#^definizione-limite-notevole):
> 
> $$
> \forall 0 < a < 1, \forall k > 0 . \left( \lim_{x \to + \infty} \dfrac{\log_a x}{x^k} = 0 \right) 
> $$
^corollario-limite-notevole-del-logaritmo-a-base-minore-di-1

%% 
dimostrazione pag. 188 lancelotti
%%

> [!corollario] Corollario: limite notevole del reciproco del logaritmo a base minore di $1$
> 
> Vale il seguente [limite notevole](content/Matematica/Analisi%20matematica/Limiti/_index.md#^definizione-limite-notevole):
> 
> $$
> \forall 0 < a < 1, \forall k > 0 . \left( \lim_{x \to + \infty} \dfrac{x^k}{\log_a x} = - \infty \right) 
> $$

### Tipo $0 \cdot \infty$

%% 
Questi limiti notevoli sono tutti riconducibili a forme ind. esp. del tipo 0 .* infty
%%

#### Limite notevole dell'esponenziale decrescente

> [!proposizione] Proposizione: limite notevole dell'esponenziale decrescente
> 
> Vale il seguente [limite notevole](content/Matematica/Analisi%20matematica/Limiti/_index.md#^definizione-limite-notevole):
> 
> $$
> \forall a > 1, \forall k > 0 . \left( \lim_{x \to - \infty} (|x|^k a^x) = 0 \right) 
> $$
^proposizione-limite-notevole-dell-esponenziale-decrescente

%% 
È il corrispettivo per x→−∞x \to -\infty x→−∞ della prevalenza dell'esponenziale sulla potenza: quando x→−∞x \to -\infty x→−∞, l'esponenziale axa^x ax tende a 00 0 così rapidamente da annullare qualsiasi potenza ∣x∣k|x|^k ∣x∣k, per grande che sia kk k.
%%

%%
dimostrazione pag. 188 lancelotti
%%

> [!corollario] Corollario: limite notevole dell'esponenziale decrescente a base minore di uno
> 
> Vale il seguente [limite notevole](content/Matematica/Analisi%20matematica/Limiti/_index.md#^definizione-limite-notevole):
> 
> $$
> \forall 0 < a < 1, \forall k > 0 . \left( \lim_{x \to + \infty} x^ka^x = 0 \right) 
> $$
^proposizione-limite-notevole-dell-esponenziale-decrescente-a-base-minore-di-uno

%% 
dimostrazione pag. 188 lancelotti
%%

#### Limite notevole del logaritmo in zero

> [!proposizione] Proposizione: limite notevole del logaritmo in zero
> 
> Vale il seguente [limite notevole](content/Matematica/Analisi%20matematica/Limiti/_index.md#^definizione-limite-notevole):
> 
> $$
> \forall a > 1, \forall k > 0 . \left( \lim_{x \to 0^+} (x^k \log_a x) = 0 \right) 
> $$
^proposizione-limite-notevole-del-logaritmo-in-zero

%% 
È il corrispettivo per x→0+x \to 0^+ x→0+ della prevalenza della potenza sul logaritmo: quando x→0+x \to 0^+ x→0+, la potenza xkx^k xk tende a 00 0 così rapidamente da annullare la divergenza di log⁡ax→−∞\log_a x \to -\infty loga​x→−∞, per piccolo che sia k>0k > 0 k>0.
%%

%%
dimostrazione pag. 188 lancelotti
%%

> [!corollario] Corollario: limite notevole del logaritmo in zero a base minore di $1$
> 
> Vale il seguente [limite notevole](content/Matematica/Analisi%20matematica/Limiti/_index.md#^definizione-limite-notevole):
> 
> $$
> \forall 0 < a < 1, \forall k > 0 . \left( \lim_{x \to 0^+} (x^k \log_a x) = 0 \right) 
> $$

%% 
dimostrazione pag. 188 lancelotti
%%

%% 
Esercizio 3.54 pagina 188 lancelotti
%%

---

> [!fonti]+ Fonti
> 
> - 📚 _Lezioni di Analisi Matematica I_ di Sergio Lancelotti, Celid, 2020 (ISBN: `978-8867891979`):
> 	- Capitolo 3 - _Limiti e continuità_:
> 		- 3 - _Teoremi su limiti e continuità_:
> 			- 3.5 - _Teoremi del confronto_.
> 			- 3.8 - _Limiti notevoli_.
