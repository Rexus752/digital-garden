---
title: Infiniti e infinitesimi
---

> [!premessa]+ Premessa
> 
> Ciao! Se è la prima volta che capiti su questo sito, ti consiglio di consultare la [pagina principale](index.md) di questo cosiddetto _Giardino Digitale_ per scoprire meglio cos'è e come navigarlo.
> 
> Lo stato di questa nota è al momento: 🔴 <font color="#FF7F7F">_Bozza_</font>.

---

> [!definizione]+ Definizione: infinito e infinitesimo
> 
> Data una [funzione](Matematica/Teoria%20degli%20insiemi/Funzioni/_index.md#^definizione-funzione) $f \colon \text{dom}(f) \to \mathbb{R}$ e un [punto di accumulazione](Topologia%20dei%20reali.md#^definizione-punto-di-accumulazione) $x_0 \in \mathbb{R} \cup \{ \pm \infty \}$ per $\text{dom}(f)$, diciamo che:
> - **$f$ è un infinitesimo in $x_0$** (o **per $x$ che tende a $x_0$**) se
> 	$$
> 	\lim_{x \to x_0} f(x) = 0
> 	$$
> - **$f$ è un infinito in $x_0$** (o **per $x$ che tende a $x_0$**) se
> 	$$
> 	\lim_{x \to x_0} |f(x)| = + \infty
> 	$$
^definizione-infinito-e-infinitesimo

> [!esempio]- Esempi di infiniti e infinitesimi
> 
> Ecco alcuni esempi di [infiniti](Infiniti%20e%20infinitesimi.md#^definizione-infinito-e-infinitesimo) e [infinitesimi](Infiniti%20e%20infinitesimi.md#^definizione-infinito-e-infinitesimo):
> - La [funzione](Matematica/Teoria%20degli%20insiemi/Funzioni/_index.md#^definizione-funzione) $f(x) = x^n$ con $n \in \mathbb{N}^{ \ge 1}$ è un [infinitesimo](Infiniti%20e%20infinitesimi.md#^definizione-infinito-e-infinitesimo) per $x \to 0$ e un [infinitesimo](Infiniti%20e%20infinitesimi.md#^definizione-infinito-e-infinitesimo) per $x \to \pm \infty$.
> - La [funzione](Matematica/Teoria%20degli%20insiemi/Funzioni/_index.md#^definizione-funzione) $f(x) = \dfrac{1}{x^n}$ con $n \in \mathbb{N}^{\ge 1}$ è un [infinito](Infiniti%20e%20infinitesimi.md#^definizione-infinito-e-infinitesimo) per $x \to 0$ e un [infinitesimo](Infiniti%20e%20infinitesimi.md#^definizione-infinito-e-infinitesimo) per $x \to \pm \infty$.
> - La [funzione](Matematica/Teoria%20degli%20insiemi/Funzioni/_index.md#^definizione-funzione) $f(x) = e^x$ è un [infinitesimo](Infiniti%20e%20infinitesimi.md#^definizione-infinito-e-infinitesimo) per $x \to - \infty$ e un [infinito](Infiniti%20e%20infinitesimi.md#^definizione-infinito-e-infinitesimo) per $x \to + \infty$.
> - La [funzione](Matematica/Teoria%20degli%20insiemi/Funzioni/_index.md#^definizione-funzione) $f(x) = \ln x$ è un [infinito](Infiniti%20e%20infinitesimi.md#^definizione-infinito-e-infinitesimo) per $x \to 0^+$ e per $x \to + \infty$ e un [infinitesimo](Infiniti%20e%20infinitesimi.md#^definizione-infinito-e-infinitesimo) per $x \to 1$.

> [!proposizione]+ Proposizione: rapporto tra infiniti e infinitesimi
> 
> Data una [funzione](Matematica/Teoria%20degli%20insiemi/Funzioni/_index.md#^definizione-funzione) $f \colon \text{dom}(f) \to \mathbb{R}$ e un [punto di accumulazione](Topologia%20dei%20reali.md#^definizione-punto-di-accumulazione) $x_0 \in \mathbb{R} \cup \{ \pm \infty \}$ per $\text{dom}(f)$, se in ogni [intorno](Topologia%20dei%20reali.md#^definizione-intorno-di-un-punto) $I(x_0)$ di $x_0$ esiste un $x \in \text{dom}(f) \setminus \{ x_0 \}$ tale che $f(x) \ne 0$, allora $f$ è un [infinitesimo](Infiniti%20e%20infinitesimi.md#^definizione-infinito-e-infinitesimo) in $x_0$ se e solo se $\dfrac{1}{f}$ è un [infinito](Infiniti%20e%20infinitesimi.md#^definizione-infinito-e-infinitesimo) in $x_0$:
> 
> $$
> f \text{ infinitesimo in } x_0 \iff \dfrac{1}{f} \text{ infinito in } x_0
> $$
^proposizione-rapporto-tra-infiniti-e-infinitesimi

%%
[!dimostrazione]- Dimostrazione

Per esercizio
%%

# 1 - Simboli di Landau

Introduciamo ora delle nozioni che ci permettono di confrontare localmente%% link %% le [funzioni](Matematica/Teoria%20degli%20insiemi/Funzioni/_index.md#^definizione-funzione), cioè in un [intorno](Topologia%20dei%20reali.md#^definizione-intorno-di-un-punto) di un punto%% Link %%. Poiché la nozione locale più generale che conosciamo è quella del [_limite_](Matematica/Analisi%20matematica/Limiti/_index.md#^definizione-limite), tutte queste nozioni che introdurremo si baseranno su di essa, anzi non saranno altro che un modo diverso di scrivere l'operazione%% link %% di [limite](Matematica/Analisi%20matematica/Limiti/_index.md#^definizione-limite). Faremo ciò attraverso quelli che vengono chiamati [_simboli di Landau_](Infiniti%20e%20infinitesimi.md#^definizione-simboli-di-landau).

> [!definizione]+ Definizione: simboli di Landau
> 
> I **simboli di Landau** (o **notazione asintotica**) sono un linguaggio formale%% link %% per confrontare il comportamento di due [funzioni](Matematica/Teoria%20degli%20insiemi/Funzioni/_index.md#^definizione-funzione) in prossimità di un punto%% Link %% (finito%% Link %% o infinito%% Link %%). Non descrivono il valore%% Link %% di una [funzione](Matematica/Teoria%20degli%20insiemi/Funzioni/_index.md#^definizione-funzione), ma la sua velocità di crescita relativa rispetto a un'altra.
> 
> I **simboli di Landau** sono l'[$o$-piccolo](Infiniti%20e%20infinitesimi.md#^definizione-o-piccolo), l'[equivalenza asintotica $\sim$](Infiniti%20e%20infinitesimi.md#^definizione-equivalenza-asintotica), ... e prendono il nome dal matematico tedesco Edmund Landau che li ha ideati e formalizzati.
^definizione-simboli-di-landau

## 1.1 - $o$-piccolo

> [!definizione]+ Definizione: $\color{#FF7FFF} o$-piccolo
> 
> Date due [funzioni](Matematica/Teoria%20degli%20insiemi/Funzioni/_index.md#^definizione-funzione) $f,g \colon A \subseteq \mathbb{R} \to \mathbb{R}$ (con $A \ne \emptyset$) e un [punto di accumulazione](Topologia%20dei%20reali.md#^definizione-punto-di-accumulazione) $x_0 \in \mathbb{R} \cup \{ \pm \infty \}$ per $A$, diciamo che **$f$ è $o$-piccolo di $g$ per $x$ che tende a $x_0$** se
> 
> $$
> \lim_{x \to x_0} \dfrac{f(x)}{g(x)} = 0
> $$
> 
> e in tal caso scriviamo "$f = o(g)$ per $x \to x_0$" (oppure "$f(x) = o(g(x))$ per $x \to x_0$").
> 
> L'**$o$-piccolo** è uno dei [simboli di Landau](Infiniti%20e%20infinitesimi.md#^definizione-simboli-di-landau).
^definizione-o-piccolo

> [!osservazione]+ Osservazione: nell'$o$-piccolo $\color{#7F7F7F} g$ non identicamente nulla
> 
> Affinché l'[$o$-piccolo](Infiniti%20e%20infinitesimi.md#^definizione-o-piccolo) sia ben definito (e cioè, affinché possa esistere il [limite](Matematica/Analisi%20matematica/Limiti/_index.md#^definizione-limite)), è necessario che la [funzione](Matematica/Teoria%20degli%20insiemi/Funzioni/_index.md#^definizione-funzione) $g$ non sia [identicamente nulla](Matematica/Teoria%20degli%20insiemi/Funzioni/_index.md#^definizione-funzione-identicamente-nulla) in alcun [intorno bucato](Topologia%20dei%20reali.md#^definizione-intorno-bucato-di-un-punto) $I(x_0)$ di $x_0$ [intersecato](Matematica/Teoria%20degli%20insiemi/_index.md#^definizione-intersezione-di-due-insiemi) con $A$:
> 
> $$
> \begin{array}{}
> f = o(g) \text{ per } x \to x_0 \\
> \Downarrow \\
> g \text{ non identicamente nulla per ogni } (I(x_0) \cap A) \setminus \{ x_0 \}
> \end{array}
> $$
> 
> Ciò garantisce che il rapporto%% link %% $\dfrac{f}{g}$ sia definito in un [insieme](Matematica/Teoria%20degli%20insiemi/_index.md#^definizione-insieme) di punti%% link %% che si [accumula](Topologia%20dei%20reali.md#^definizione-punto-di-accumulazione) su $x_0$, permettendoci così di fare affermazioni sensate sul suo comportamento asintotico.
^osservazione-nell-o-piccolo-g-non-identicamente-nulla

> [!esempio]- Esempio: $\color{#7F7FFF} x^2 = o(x)$ per $\color{#7F7FFF} x \to 0$ e $\color{#7F7FFF} x = o(x^2)$ per $\color{#7F7FFF} x \to \pm \infty$
> 
> Si ha che $x^2$ è [$o$-piccolo](Infiniti%20e%20infinitesimi.md#^definizione-o-piccolo) di $x$ per $x \to 0$, infatti
> 
> $$
> \begin{array}{}
> x^2 = o(x) \text{ per } x \to 0 \\
> \Updownarrow \\
> \displaystyle\lim_{x \to 0} \dfrac{x^2}{x} = \lim_{x \to 0} x = 0
> \end{array}
> $$
> 
> E si ha anche che $x$ è [$o$-piccolo](Infiniti%20e%20infinitesimi.md#^definizione-o-piccolo) di $x^2$ per $x \to \pm \infty$, infatti
> 
> $$
> \begin{array}{}
> x = o(x^2) \text{ per } x \to \pm \infty \\
> \Updownarrow \\
> \displaystyle\lim_{x \to \pm \infty} \dfrac{x}{x^2} = \lim_{x \to \pm \infty} \dfrac{1}{x} = 0
> \end{array}
> $$

> [!esempio]- Esempio: $\color{#7F7FFF} \sin x = o(\sqrt x)$ per $\color{#7F7FFF} x \to 0^+$
> 
> Si ha che $\sin x$ è [$o$-piccolo](Infiniti%20e%20infinitesimi.md#^definizione-o-piccolo) di $\sqrt x$ per $x \to 0^+$, infatti
> 
> $$
> \begin{array}{}
> \sin x = o(\sqrt x) \text{ per } x \to 0^+ \\
> \Updownarrow \\
> \begin{align*}
> \lim_{x \to 0^+} \dfrac{\sin x}{\sqrt x} &= \lim_{x \to 0^+} \left( \dfrac{\sin x}{\sqrt x} \cdot \dfrac{x}{x} \right) \\
> &= \lim_{x \to 0^+} \left( \underbrace{\dfrac{\sin x}{x}}_{=1} \cdot \underbrace{\sqrt x}_{=0} \right) \\
> &= 0
> \end{align*}
> \end{array}
> $$
> 
> Quel $\underbrace{\dfrac{\sin x}{x}}_{=1}$ è dovuto al [limite notevole del seno tendente a $0$](Limiti%20notevoli.md#^proposizione-limite-notevole-del-seno-tendente-a-0).
> 
> Si ha anche che $\sin x$ è [$o$-piccolo](Infiniti%20e%20infinitesimi.md#^definizione-o-piccolo) di $\sqrt x$ per $x \to + \infty$ perché
> 
> $$
> \begin{array}{}
> \sin x = o(\sqrt x) \text{ per } x \to + \infty \\
> \Updownarrow \\
> \displaystyle\lim_{x \to + \infty} \dfrac{\sin x}{\sqrt x} = \lim_{x \to + \infty} \left( \underbrace{\sin x}_{\text{è limitata}} \cdot \underbrace{\dfrac{1}{\sqrt x}}_{= 0} \right) = 0
> \end{array}
> $$

%% spiegare meglio perché sin x è limitata e perché 1/\sqrt x è 0 %%

> [!esempio]- Esempio: $\color{#7F7FFF} o$-piccolo tra $\color{#7F7FFF} x^p$ e $\color{#7F7FFF} x^q$
> 
> Si ha che $x^p$ è [$o$-piccolo](Infiniti%20e%20infinitesimi.md#^definizione-o-piccolo) di $x^q$ per $x \to + \infty$ se $0 < p < q$:
> 
> $$
> \forall 0 < p < q . (x^p = o(x^q)\text{ per } x \to + \infty)
> $$
> 
> %% perché $x^q$ cresce più velocemente, giusto? %%
> 
> Si ha anche che $x^p$ è [$o$-piccolo](Infiniti%20e%20infinitesimi.md#^definizione-o-piccolo) di $x^q$ per $x \to 0^+$ se $0 < q < p$
> 
> $$
> \forall 0 < q < p . (x^p = o(x^q)\text{ per } x \to 0^+)
> $$
> 
> %% perché $x^p$ cresce più velocemente, giusto? %%

%% esempio 4 di o-piccolo a pagina 190 lancelotti %%

### 1.1.1 - Proprietà dell'$o$-piccolo

> [!proprieta]+ Proprietà: transitività di $\color{#FFFF7F} o$-piccolo
> 
> Vale la proprietà transitiva%% Link %% per [$o$-piccolo](Infiniti%20e%20infinitesimi.md#^definizione-o-piccolo): se $f = o(g)$ e $g = o(h)$ per un certo $x \to x_0$, allora vale anche $f = o(h)$ per $x \to x_0$, infatti
> 
> $$
> \lim_{x \to x_0} \dfrac{f(x)}{h(x)} = \lim_{x \to x_0} \left( \dfrac{f(x)}{h(x)} \cdot \dfrac{g(x)}{g(x)} \right) = \lim_{x \to x_0} \left( \underbrace{\dfrac{f(x)}{g(x)}}_{=0} \cdot \underbrace{\dfrac{g(x)}{h(x)}}_{=0} \right) = 0
> $$
^proprieta-transitivita-di-o-piccolo

> [!attenzione]+ Attenzione: abuso di notazione nei simboli di Landau
> 
> Nella notazione di [$o$-piccolo](Infiniti%20e%20infinitesimi.md#^definizione-o-piccolo) $f = o(g)$, il simbolo $=$ **NON** è un'uguaglianza%% link %% di fatto tra [funzioni](Matematica/Teoria%20degli%20insiemi/Funzioni/_index.md#^definizione-funzione), ma sta solo ad indicare una proprietà qualitativa di $f$ rispetto a $g$.
> 
> Non è quindi applicabile la proprietà transitiva dell'uguaglianza%% link %%, cioè
> 
> $$
> f = o(g) \land h = o(g) \not \implies f = h
> $$
> 
> Infatti, $x^2 = o(x)$ e $x^3 = o(x)$ ma $x^2 \ne x^3$.
^attenzione-abuso-di-notazione-nei-simboli-di-landau

> [!proposizione]+ Proposizione: $\color{#FF7F7F} o$-piccolo di se stesso
> 
> Data una [funzione](Matematica/Teoria%20degli%20insiemi/Funzioni/_index.md#^definizione-funzione) $f$, l'[$o$-piccolo](Infiniti%20e%20infinitesimi.md#^definizione-o-piccolo) di $f$ è [$o$-piccolo](Infiniti%20e%20infinitesimi.md#^definizione-o-piccolo) di $f$ per $x \to x_0$ (che può sembrare uno scioglilingua, ma non lo è), cioè vale
> 
> $$
> \lim_{x \to x_0} \dfrac{o(f(x))}{f(x)} = 0
> $$
> 
> > [!dimostrazione]- Dimostrazione
> > 
> > Per [definizione di _$o$-piccolo_](Infiniti%20e%20infinitesimi.md#^definizione-o-piccolo), abbiamo che
> > 
> > $$
> > \begin{array}{}
> > f = o(g) \text{ per } x \to x_0 \\
> > \Updownarrow \\
> > \displaystyle\lim_{x \to x_0} \dfrac{f(x)}{g(x)} = 0
> > \end{array}
> > $$
> > 
> > Quindi si ha che
> > 
> > $$
> > \lim_{x \to x_0} \dfrac{\overbrace{f(x)}^{= o(g(x))}}{g(x)} = \lim_{x \to x_0} \dfrac{o(g(x))}{g(x)} = 0
> > $$
> > 
> > (Nella [proposizione](Infiniti%20e%20infinitesimi.md#^proposizione-o-piccolo-di-se-stesso) viene usato $f$ al posto di $g$, ma è la stessa cosa.)
> > 
> > Notiamo che l'uguaglianza $f(x) = o(g(x))$ è da intendersi come un semplice collegamento "qualitativo" tra $f$ e $g$, cioè indica che $f$ è una qualsiasi [funzione](Matematica/Teoria%20degli%20insiemi/Funzioni/_index.md#^definizione-funzione) che è [$o$-piccolo](Infiniti%20e%20infinitesimi.md#^definizione-o-piccolo) di $g$ per $x \to x_0$, quindi perfettamente in accordo con [quanto detto prima sull'abuso di notazione](Infiniti%20e%20infinitesimi.md#^attenzione-abuso-di-notazione-nei-simboli-di-landau).
> > 
> > $\blacksquare$
^proposizione-o-piccolo-di-se-stesso

> [!proposizione]+ Proposizione: $\color{#FF7F7F} o$-piccolo, infiniti e infinitesimi
> 
> Data una [funzione](Matematica/Teoria%20degli%20insiemi/Funzioni/_index.md#^definizione-funzione) $f$ che è [$o$-piccolo](Infiniti%20e%20infinitesimi.md#^definizione-o-piccolo) di $1$ per $x \to x_0$, si ha che $f$ è un [infinitesimo](Infiniti%20e%20infinitesimi.md#^definizione-infinito-e-infinitesimo) in $x_0$ e, al contrario, se $1$ è [$o$-piccolo](Infiniti%20e%20infinitesimi.md#^definizione-o-piccolo) di $f$ per $x \to x_0$, allora $f$ è un [infinito](Infiniti%20e%20infinitesimi.md#^definizione-infinito-e-infinitesimo) in $x_0$:
> 
> $$
> \begin{align*}
> f = o(1) \text{ per } x \to x_0 \iff & f \text{ è un infinitesimo in } x_0 \\
> 1 = o(f) \text{ per } x \to x_0 \iff & f \text{ è un infinito in } x_0
> \end{align*}
> $$
> 
> > [!dimostrazione]- Dimostrazione
> > 
> > Dimostriamo prima che se $f$ è [$o$-piccolo](Infiniti%20e%20infinitesimi.md#^definizione-o-piccolo) di $1$ per $x \to x_0$ si ha che $f$ è un [infinitesimo](Infiniti%20e%20infinitesimi.md#^definizione-infinito-e-infinitesimo) in $x_0$. Per [definizione di _$o$-piccolo_](Infiniti%20e%20infinitesimi.md#^definizione-o-piccolo), abbiamo che
> > 
> > $$
> > \begin{array}{}
> > f = o(1) \text{ per } x \to x_0 \\
> > \Updownarrow \\
> > \displaystyle\lim_{x \to x_0} \dfrac{f(x)}{1} = 0 \\
> > \Updownarrow \\
> > \displaystyle\lim_{x \to x_0} f(x) = 0
> > \end{array}
> > $$
> > 
> > che corrisponde proprio alla [definizione di _infinitesimo_](Infiniti%20e%20infinitesimi.md#^definizione-infinito-e-infinitesimo).
> > 
> > Ora dimostriamo che se $1$ è [$o$-piccolo](Infiniti%20e%20infinitesimi.md#^definizione-o-piccolo) di $f$ per $x \to x_0$ si ha che $f$ è un [infinito](Infiniti%20e%20infinitesimi.md#^definizione-infinito-e-infinitesimo) in $x_0$. Per [definizione di _$o$-piccolo_](Infiniti%20e%20infinitesimi.md#^definizione-o-piccolo), abbiamo che
> > 
> > $$
> > \begin{array}{}
> > 1 = o(f) \text{ per } x \to x_0 \\
> > \Updownarrow \\
> > \displaystyle\lim_{x \to x_0} \dfrac{1}{f(x)} = 0
> > \end{array}
> > $$
> > 
> > cioè $\dfrac{1}{f(x)}$ è un [infinitesimo](Infiniti%20e%20infinitesimi.md#^definizione-infinito-e-infinitesimo) in $x_0$, ma dal [rapporto tra infiniti e infinitesimi](Infiniti%20e%20infinitesimi.md#^proposizione-rapporto-tra-infiniti-e-infinitesimi) abbiamo che se $\dfrac{1}{f(x)}$ è un [infinitesimo](Infiniti%20e%20infinitesimi.md#^definizione-infinito-e-infinitesimo) in $x_0$, allora $\dfrac{1}{\frac{1}{f(x)}} = f(x)$ è un [infinito](Infiniti%20e%20infinitesimi.md#^definizione-infinito-e-infinitesimo) in $x_0$.
> > 
> > $\blacksquare$
^proposizione-o-piccolo-infiniti-e-infinitesimi

%% 
Osservazione "e", "f" di pagina 191 lancelotti
%%

### 1.1.2 - Trascurabilità di una funzione

> [!definizione]+ Definizione: trascurabilità di una funzione
> 
> Date due [funzioni](Matematica/Teoria%20degli%20insiemi/Funzioni/_index.md#^definizione-funzione) $f,g \colon A \subseteq \mathbb{R} \to \mathbb{R}$ (con $A \ne \emptyset$) e un [punto di accumulazione](Topologia%20dei%20reali.md#^definizione-punto-di-accumulazione) $x_0 \in \mathbb{R} \cup \{ \pm \infty \}$ per $A$, se $f$ è [$o$-piccolo](Infiniti%20e%20infinitesimi.md#^definizione-o-piccolo) di $g$ per $x \to x_0$, allora diciamo che **$f$ è trascurabile rispetto a $g$ per $x \to x_0$**.
^definizione-trascurabilita-di-una-funzione

> [!osservazione]+ Osservazione: significato di _trascurabilità_
> 
> Cerchiamo di comprendere meglio il significato di questa denominazione, anche al fine di evitare equivoci.
> 
> La dicitura "$f$ è [trascurabile](Infiniti%20e%20infinitesimi.md#^definizione-trascurabilita-di-una-funzione) rispetto a $g$ per $x \to x_0$" indica che il [limite](Matematica/Analisi%20matematica/Limiti/_index.md#^definizione-limite)
> 
> $$
> \lim_{x \to x_0} \big( f(x) + g(x) \big) 
> $$
> 
> dipende solo da $g$ e non da $f$, cioè nel calcolare questo [limite](Matematica/Analisi%20matematica/Limiti/_index.md#^definizione-limite) l'addendo $f(x)$ può essere trascurato rispetto a $g(x)$. Quindi si ha che
> 
> $$
> \lim_{x \to x_0} \big( f(x) + g(x) \big) = \lim_{x \to x_0} g(x)
> $$
> 
> Infatti, raccogliendo $g(x)$, si ha che
> 
> $$
> \lim_{x \to x_0} \big( f(x) + g(x) \big) = \lim_{x \to x_0} \left( g(x) \left( \dfrac{f(x)}{g(x)} + 1 \right)  \right) 
> $$
> 
> Essendo $f$ [$o$-piccolo](Infiniti%20e%20infinitesimi.md#^definizione-o-piccolo) di $g(x)$ per $x \to x_0$, si ha che $\displaystyle\lim_{x \to x_0} \dfrac{f(x)}{g(x)} = 0$. Se esiste il [limite](Matematica/Analisi%20matematica/Limiti/_index.md#^definizione-limite) $\displaystyle\lim_{x \to x_0} g(x) = l \in \mathbb{R} \cup \{ \pm \infty \}$, allora per l'algebra dei limiti%% link %% si ha che
> 
> $$
> \lim_{x \to x_0} \big( f(x) + g(x) \big) = \lim_{x \to x_0} \left( \underbrace{g(x)}_{= l} \left( \underbrace{\dfrac{f(x)}{g(x)}}_{= 0} + 1 \right)  \right) = l = \lim_{x \to x_0} g(x)
> $$
> 
> Se invece non esiste il [limite](Matematica/Analisi%20matematica/Limiti/_index.md#^definizione-limite) $\displaystyle\lim_{x \to x_0} g(x)$, allora anche il [limite](Matematica/Analisi%20matematica/Limiti/_index.md#^definizione-limite) $\displaystyle\lim_{x \to x_0} \big( f(x) + g(x) \big)$ non esiste. Infatti, se per assurdo esistesse questo [limite](Matematica/Analisi%20matematica/Limiti/_index.md#^definizione-limite) e fosse $\displaystyle\lim_{x \to x_0} \big( f(x) + g(x) \big) = l' \in \mathbb{R} \cup \{ \pm \infty \}$, poiché
> 
> $$
> \begin{align*}
> g(x) &= g(x) \dfrac{f(x) + g(x)}{f(x) + g(x)} \\
> &= \dfrac{f(x) + g(x)}{\dfrac{f(x) + g(x)}{g(x)}} \\
> &= \dfrac{f(x) + g(x)}{\dfrac{f(x)}{g(x)} + 1}
> \end{align*}
> $$
> 
> e, sempre per l'algebra dei limiti%% link %%, avremmo che
> 
> $$
> \lim_{x\to x_0} g(x) = \lim_{x \to x_0} \dfrac{\overbrace{f(x) + g(x)}^{=l'}}{\underbrace{\dfrac{f(x)}{g(x)} + 1}_{=1}} = l'
> $$
> 
> e otterremmo l'assurda affermazione che $\displaystyle\lim_{x\to x_0} g(x) = l'$ che va in contrasto con l'ipotesi iniziale per cui il [limite](Matematica/Analisi%20matematica/Limiti/_index.md#^definizione-limite) $\displaystyle\lim_{x \to x_0} g(x)$ non esiste.

### 1.1.3 - Principio di eliminazione dei termini trascurabili (PETT)

> [!teorema]+ Principio di eliminazione dei termini trascurabili (PETT)
> 
> Date quattro [funzioni](Matematica/Teoria%20degli%20insiemi/Funzioni/_index.md#^definizione-funzione) $f,g,f',g' \colon A \subseteq \mathbb{R} \to \mathbb{R}$ (con $A \ne \emptyset$) e un [punto di accumulazione](Topologia%20dei%20reali.md#^definizione-punto-di-accumulazione) $x_0 \in \mathbb{R} \cup \{ \pm \infty \}$ per $A$, abbiamo che se $f'$ è [$o$-piccolo](Infiniti%20e%20infinitesimi.md#^definizione-o-piccolo) di $f$ per $x \to x_0$ e $g'$ è [$o$-piccolo](Infiniti%20e%20infinitesimi.md#^definizione-o-piccolo) di $g$ per $x \to x_0$, allora $f'$ e $g'$ sono [trascurabili](Infiniti%20e%20infinitesimi.md#^definizione-trascurabilita-di-una-funzione) nella rispettiva somma con $f$ e $g$:
> 
> $$
> \begin{array}{}
> f' = o(f) \text{ per } x \to x_0 \land g' = o(f) \text{ per } x \to x_0 \\
> \Downarrow \\
> \displaystyle\lim_{x \to x_0} \dfrac{f(x) + f'(x)}{g(x) + g'(x)} = \lim_{x \to x_0} \dfrac{f(x)}{g(x)}
> \end{array}
> $$
^principio-di-eliminazione-dei-termini-trascurabili

%% 
dimostrazione pagg. 193-194 lancelotti
%%

> [!osservazione]+ Osservazione: riformulazione del PETT
> 
> Il [principio di eliminazione dei termini trascurabili (PETT)](Infiniti%20e%20infinitesimi.md#^principio-di-eliminazione-dei-termini-trascurabili) può essere riformulato anche come
> 
> $$
> \lim_{x \to x_0} \dfrac{f(x) + o(f(x))}{g(x) + o(g(x))} = \lim_{x \to x_0} \dfrac{f(x)}{g(x)}
> $$

> [!osservazione]+ Osservazione: PETT per solo numeratore o denominatore
> 
> Il [principio di eliminazione dei termini trascurabili (PETT)](Infiniti%20e%20infinitesimi.md#^principio-di-eliminazione-dei-termini-trascurabili) può essere utilizzato anche se la [funzione trascurabile](Infiniti%20e%20infinitesimi.md#^definizione-trascurabilita-di-una-funzione) è presente solo al numeratore%% Link %% o al denominatore%% link %%. Più precisamente,
> 
> $$
> \lim_{x \to x_0} \dfrac{f(x) + o(f(x))}{g(x)} = \lim_{x \to x_0} \dfrac{f(x)}{g(x) + o(g(x))} = \lim_{x \to x_0} \dfrac{f(x)}{g(x)}
> $$

%% 
osservazioni c, d pagina 194 lancelotti
%%

> [!esempio]- Esempio di uso del PETT
> 
> Calcoliamo il [limite](Matematica/Analisi%20matematica/Limiti/_index.md#^definizione-limite)
> 
> $$
> \lim_{x \to 0} \dfrac{x^2 + \sin x}{x^2 - \sin x} 
> $$
> 
> Possiamo osservare che $x^2$ è [$o$-piccolo](Infiniti%20e%20infinitesimi.md#^definizione-o-piccolo) di $\sin x$ per $x \to 0$, infatti
> 
> $$
> \lim_{x \to 0} \dfrac{x^2}{\sin x} = \lim_{x \to 0} \left( \underbrace{x}_{=0} \cdot \dfrac{x}{\underbrace{\sin x}_{=1}} \right) = 0
> $$
> 
> Allora, per il [PETT](Infiniti%20e%20infinitesimi.md#^principio-di-eliminazione-dei-termini-trascurabili), possiamo dire che
> 
> $$
> \lim_{x \to 0} \dfrac{x^2 + \sin x}{x^2 - \sin x} = \lim_{x \to 0} \dfrac{o(\sin x) + \sin x}{o(\sin x) - \sin x} \overset{\text{PETT}}{=} \lim_{x \to 0} \dfrac{\overbrace{\sin x}^{=1}}{\underbrace{- \sin x}_{=-1}} = -1
> $$

## 1.2 - Equivalenza asintotica

> [!definizione]+ Definizione: equivalenza asintotica
> 
> Date due [funzioni](Matematica/Teoria%20degli%20insiemi/Funzioni/_index.md#^definizione-funzione) $f,g \colon A \subseteq \mathbb{R} \to \mathbb{R}$ (con $A \ne \emptyset$) e un [punto di accumulazione](Topologia%20dei%20reali.md#^definizione-punto-di-accumulazione) $x_0 \in \mathbb{R} \cup \{ \pm \infty \}$ per $A$, diciamo che **$f$ è equivalente a $g$ per $x$ che tende a $x_0$ se**
> 
> $$
> \lim_{x \to x_0} \dfrac{f(x)}{g(x)} = 1
> $$
> 
> e in tal caso scriviamo "$f \sim g$ per $x \to x_0$" (oppure "$f(x) \sim g(x)$ per $x \to x_0$").
^definizione-equivalenza-asintotica

> [!osservazione]+ Osservazione: nell'equivalenza asintotica $\color{#7F7F7F} g$ non identicamente nulla
> 
> Esattamente [come avviene per l'$o$-piccolo](Infiniti%20e%20infinitesimi.md#^osservazione-nell-o-piccolo-g-non-identicamente-nulla), anche per l'[equivalenza asintotica](Infiniti%20e%20infinitesimi.md#^definizione-equivalenza-asintotica) serve che la [funzione](Matematica/Teoria%20degli%20insiemi/Funzioni/_index.md#^definizione-funzione) $g$ non sia [identicamente nulla](Matematica/Teoria%20degli%20insiemi/Funzioni/_index.md#^definizione-funzione-identicamente-nulla) in ogni [intorno bucato](Topologia%20dei%20reali.md#^definizione-intorno-bucato-di-un-punto) $I(x_0)$ di $x_0$ [intersecato](Matematica/Teoria%20degli%20insiemi/_index.md#^definizione-intersezione-di-due-insiemi) con $A$ affinché il [limite](Matematica/Analisi%20matematica/Limiti/_index.md#^definizione-limite) dell'[equivalenza asintotica](Infiniti%20e%20infinitesimi.md#^definizione-equivalenza-asintotica) sia ben definito:
> 
> $$
> \begin{array}{}
> f \sim g \text{ per } x \to x_0 \\
> \Downarrow \\
> g \text{ non identicamente nulla per ogni } (I(x_0) \cap A) \setminus \{ x_0 \}
> \end{array}
> $$
^osservazione-nell-equivalenza-asintotica-g-non-identicamente-nulla

> [!proposizione]+ Proposizione: nell'equivalenza asintotica $\color{#FF7F7F} f$ non identicamente nulla
> 
> Se una [funzione](Matematica/Teoria%20degli%20insiemi/Funzioni/_index.md#^definizione-funzione) $f$ è [equivalente](Infiniti%20e%20infinitesimi.md#^definizione-equivalenza-asintotica) a un'altra [funzione](Matematica/Teoria%20degli%20insiemi/Funzioni/_index.md#^definizione-funzione) $g$ per $x \to x_0$, allora anche $f$ non è [identicamente nulla](Matematica/Teoria%20degli%20insiemi/Funzioni/_index.md#^definizione-funzione-identicamente-nulla) in ogni [intorno bucato](Topologia%20dei%20reali.md#^definizione-intorno-bucato-di-un-punto) $I(x_0)$ di $x_0$ [intersecato](Matematica/Teoria%20degli%20insiemi/_index.md#^definizione-intersezione-di-due-insiemi) con $A$:
> 
> $$
> \begin{array}{}
> f \sim g \text{ per } x \to x_0 \\
> \Downarrow \\
> f \text{ non identicamente nulla per ogni } (I(x_0) \cap A) \setminus \{ x_0 \}
> \end{array}
> $$
> 
> > [!dimostrazione]- Dimostrazione
> > 
> > Per il [teorema della permanenza del segno](Proprietà%20locali%20delle%20funzioni%20continue.md#^teorema-della-permanenza-del-segno) esiste un [intorno](Topologia%20dei%20reali.md#^definizione-intorno-di-un-punto) $I(x_0)$ di $x_0$ tale che
> > 
> > $$
> > \forall x \in \big( I(x_0) \cap A \big)  \setminus \{ x_0 \} . \left( \dfrac{f(x)}{g(x)} > 0 \right) 
> > $$
> > 
> > [Poiché $g$ non è identicamente nulla nell'intorno bucato $I(x_0)$ intersecato con $A$](Infiniti%20e%20infinitesimi.md#^osservazione-nell-equivalenza-asintotica-g-non-identicamente-nulla), allora in ogni [intorno](Topologia%20dei%20reali.md#^definizione-intorno-di-un-punto) di $x_0$ contenuto in $I(x_0)$ esiste un $x \in A \setminus \{ x_0 \}$ tale che
> > 
> > $$
> > \begin{array}{}
> > \dfrac{f(x)}{g(x)} > 0 \land g(x) \ne 0 \\
> > \Downarrow \\
> > f(x) = \underbrace{\dfrac{f(x)}{g(x)}}_{> 0} \cdot \underbrace{g(x)}_{\ne 0} \ne 0
> > \end{array}
> > $$
> > 
> > Avendo $f(x) \ne 0$, possiamo assumere che ovunque $g$ non è [identicamente nulla](Matematica/Teoria%20degli%20insiemi/Funzioni/_index.md#^definizione-funzione-identicamente-nulla), non lo sarà neanche $f$.
> > 
> > $\blacksquare$
^proposizione-nell-equivalenza-asintotica-f-non-identicamente-nulla

> [!esempio]- Esempio: $\color{#7F7FFF} \sin x \sim x$ per $\color{#7F7FFF} x \to 0$
> 
> Si ha che $\sin x$ è [equivalente](Infiniti%20e%20infinitesimi.md#^definizione-equivalenza-asintotica) a $x$ per $x \to 0$, infatti
> 
> $$
> \begin{array}{}
> \sin x \sim x \text{ per } x \to 0 \\
> \Updownarrow \\
> \displaystyle\lim_{x \to 0} \dfrac{\sin x}{x} = 1
> \end{array}
> $$
> 
> per il [limite notevole del seno tendente a $0$](Limiti%20notevoli.md#^proposizione-limite-notevole-del-seno-tendente-a-0).

> [!esempio]- Esempio: $\color{#7F7FFF} 1 - \cos x \sim \dfrac{1}{2} x^2$ per $\color{#7F7FFF} x \to 0$
> 
> Si ha che $1 - \cos x$ è [equivalente](Infiniti%20e%20infinitesimi.md#^definizione-equivalenza-asintotica) a $\dfrac{1}{2} x^2$ per $x \to 0$, infatti
> 
> $$
> \begin{array}{}
> 1 - \cos x \sim \dfrac{1}{2} x^2 \text{ per } x \to 0 \\
> \Updownarrow \\
> \displaystyle\lim_{x \to 0} \dfrac{1 - \cos x}{\dfrac{1}{2} x^2} = \displaystyle\lim_{x \to 0} \left( 2 \cdot \underbrace{\dfrac{1 - \cos x}{x^2}}_{= \frac{1}{2}} \right) = 1
> \end{array}
> $$
> 
> Ricordo che $\dfrac{1 - \cos x}{x^2}$ è uguale a $\dfrac{1}{2}$ per il [limite notevole del coseno tendente a $0$](Limiti%20notevoli.md#^proposizione-limite-notevole-del-coseno-tendente-a-0).

%%
[!esempio]- Esempio: $\tan x \sim x$ per $x \to 0$

[!esempio]- Esempio: $\arctan \sim x$ per $x \to 0$
%%

> [!esempio]- Esempio: $\color{#7F7FFF} P(x) \sim a_nx^n$ per $\color{#7F7FFF} x \to \pm \infty$
> 
> Dato un polinomio%% link %% non nullo%% link %% $P(x) = a_nx^n + a_{n-1}x^{n-1} + \ldots + a_1x + a_0$ di grado%% link %% $n \in \mathbb{N}$, allora si ha che $P(x)$ è [equivalente](Infiniti%20e%20infinitesimi.md#^definizione-equivalenza-asintotica) a $a_nx^n$ per $x \to \pm \infty$, infatti
> 
> $$
> \begin{array}{}
> P(x) \sim a_nx^n \text{ per } x \to \pm \infty \\
> \Updownarrow \\
> \displaystyle\lim_{x \to \pm \infty} \dfrac{P(x)}{a_nx^n} = \lim_{x \to \pm \infty} \dfrac{a_nx^n + a_{n-1}x^{n-1} + \ldots + a_1x + a_0}{a_nx^n} = 1
> \end{array}
> $$
> 
> %% per la dominanza del termine di grado massimo (fare proposizione in cui dimostro questa cosa) %%

%%
[!esempio]- Esempio: $x^2 - 3x + 2 \sim x^2 + 12x - 7$ per $x \to \pm \infty$
%%

%% 
per questi ultimi due esempi possiamo dire che il PETT si può applicare sui polinomi
%%

### 1.2.1 - Proprietà dell'equivalenza asintotica

> [!proprieta]+ Proprietà: riflessività dell'equivalenza asintotica
> 
> Una [funzione](Matematica/Teoria%20degli%20insiemi/Funzioni/_index.md#^definizione-funzione) $f$ è sempre [equivalente](Infiniti%20e%20infinitesimi.md#^definizione-equivalenza-asintotica) a se stessa per $x \to x_0$, cioè l'[equivalenza asintotica](Infiniti%20e%20infinitesimi.md#^definizione-equivalenza-asintotica) gode della proprietà riflessiva%% link %%:
> 
> $$
> f \sim f \text{ per } x \to x_0
> $$
> 
> > [!dimostrazione]- Dimostrazione
> > 
> > Per [definizione di _equivalenza asintotica_](Infiniti%20e%20infinitesimi.md#^definizione-equivalenza-asintotica), dobbiamo dimostrare che
> > 
> > $$
> > \begin{array}{}
> > f \sim f \text{ per } x \to x_0 \\
> > \Updownarrow \\
> > \displaystyle\lim_{x \to x_0} \dfrac{f(x)}{f(x)} = 1
> > \end{array}
> > $$
> > 
> > Il rapporto%% link %% $\dfrac{f(x)}{f(x)} = 1$ è costantemente uguale a $1$ per ogni $x$ in cui $f(x) \neq 0$. Pertanto:
> > 
> > $$\lim_{x \to x_0} \frac{f(x)}{f(x)} = \lim_{x \to x_0} 1 = 1$$
> > 
> > Dunque $f \sim f$ per $x \to x_0$.
> > 
> > $\blacksquare$
^proprieta-riflessivita-dell-equivalenza-asintotica

> [!proprieta]+ Proprietà: simmetria dell'equivalenza asintotica
> 
> Date due [funzioni](Matematica/Teoria%20degli%20insiemi/Funzioni/_index.md#^definizione-funzione) $f$ e $g$, si ha che se $f$ è [equivalente](Infiniti%20e%20infinitesimi.md#^definizione-equivalenza-asintotica) a $g$ per $x \to x_0$, allora anche $g$ è [equivalente](Infiniti%20e%20infinitesimi.md#^definizione-equivalenza-asintotica) a $f$ per $x \to x_0$, cioè l'[equivalenza asintotica](Infiniti%20e%20infinitesimi.md#^definizione-equivalenza-asintotica) gode della proprietà simmetrica%% link %%:
> 
> $$
> \begin{array}{}
> f \sim g \text{ per } x \to x_0 \\
> \Updownarrow \\
> g \sim f \text{ per } x \to x_0
> \end{array}
> $$
> 
> > [!dimostrazione]- Dimostrazione
> > 
> > Per [definizione di _equivalenza asintotica_](Infiniti%20e%20infinitesimi.md#^definizione-equivalenza-asintotica), dobbiamo dimostrare che
> > 
> > $$
> > \begin{array}{}
> > \displaystyle\lim_{x \to x_0} \dfrac{f(x)}{g(x)} = 1 \\
> > \Updownarrow \\
> > \displaystyle\lim_{x \to x_0} \dfrac{g(x)}{f(x)} = 1
> > \end{array}
> > $$
> > 
> > Possiamo facilmente notare che
> > 
> > $$
> > \displaystyle\lim_{x \to x_0} \dfrac{g(x)}{f(x)} = \lim_{x \to x_0} \dfrac{1}{\underbrace{\dfrac{f(x)}{g(x)}}_{= 1}} = 1
> > $$
^proprieta-simmetria-dell-equivalenza-asintotica

%% 
Proprietà transitiva dell'equivalenza asintotica pag. 196 lancelotti
%%

> [!proposizione]+ Proposizione: limiti di due funzioni equivalenti
> 
> Se una [funzione](Matematica/Teoria%20degli%20insiemi/Funzioni/_index.md#^definizione-funzione) $f$ è [equivalente](Infiniti%20e%20infinitesimi.md#^definizione-equivalenza-asintotica) a un'altra [funzione](Matematica/Teoria%20degli%20insiemi/Funzioni/_index.md#^definizione-funzione) $g$ per $x \to x_0$ e se esiste il [limite](Matematica/Analisi%20matematica/Limiti/_index.md#^definizione-limite) di $f(x)$ per $x \to x_0$, allora esiste il [limite](Matematica/Analisi%20matematica/Limiti/_index.md#^definizione-limite) di $g(x)$ per $x \to x_0$ ed è uguale a $l$:
> 
> $$
> \begin{array}{}
> f \sim g \text{ per } x \to x_0 \\
> \land \\
> \displaystyle\lim_{x \to x_0} f(x) = l \in \mathbb{R} \cup \{ \pm \infty \}
> \end{array}
> \implies
> \displaystyle\lim_{x \to x_0} g(x) = l
> $$

%% 
dimostrazione pag. 197 lancelotti
%%

> [!proposizione]+ Proposizione: relazione tra l'equivalenza asintotica e l'$o$-piccolo
> 
> Si ha che una [funzione](Matematica/Teoria%20degli%20insiemi/Funzioni/_index.md#^definizione-funzione) $f$ è [equivalente](Infiniti%20e%20infinitesimi.md#^definizione-equivalenza-asintotica) a un'altra [funzione](Matematica/Teoria%20degli%20insiemi/Funzioni/_index.md#^definizione-funzione) $g$ per $x \to x_0$ se e solo se $f$ è [$o$-piccolo](Infiniti%20e%20infinitesimi.md#^definizione-o-piccolo) di $g + o(g)$ per $x \to x_0$:
> 
> $$
> \begin{array}{}
> f \sim g \text{ per } x \to x_0 \\
> \Updownarrow \\
> f = g + o(g) \text{ per } x \to x_0
> \end{array}
> $$
^proposizione-relazione-tra-l-equivalenza-asintotica-e-l-o-piccolo

%% 
dimostrazione pag. 197 lancelotti
%%

> [!osservazione]+ Osservazione: come interpretare $\color{#7F7F7F} f = g + o(g)$
> 
> La notazione $f = g + o(g)$ non è da intendersi come un'uguaglianza%% link %% ma, [esattamente come già detto prima](Infiniti%20e%20infinitesimi.md#^attenzione-abuso-di-notazione-nei-simboli-di-landau), è un abuso di notazione che ci permette di indicare una proprietà qualitativa di $f$ rispetto a $g$: questa notazione indica che $f$ differisce da $g$ solo per un termine [trascurabile](Infiniti%20e%20infinitesimi.md#^definizione-trascurabilita-di-una-funzione) rispetto a $g$ stesso.
> 
> In altre parole, per $x \to x_0$, possiamo approssimare $f$ con $g$ e l'errore che commettiamo (cioè $f - g$) è uguale a $o(g)$, cioè $o(g)$ va intesa come una quantità minuscola.

%% 
esempi 4.14 pagina 197 lancelotti
%%

%% 
esempio ultima parte di pagina 198 in cui parla della pericolosità di $\sim$, compresa tutta pag. 199 lancelotti
%%

%% 
limiti notevoli con gli o-piccolo pagina 200 lancelotti

(nel caso spostare tutto in una pagina a parte)
%%

%% 
algebra degli o-piccolo pagg. 200-201 lancelotti
%%

%% 
osservazione 4.18 ed esempio 4.19 pagg. 201-202
%%

# 2 - Confronto fra infiniti e infinitesimi

Introduciamo una terminologia per confrontare fra loro gli [infiniti](Infiniti%20e%20infinitesimi.md#^definizione-infinito-e-infinitesimo) e fra loro gli [infinitesimi](Infiniti%20e%20infinitesimi.md#^definizione-infinito-e-infinitesimo), utilizzando le nozioni di [_$o$-piccolo_](Infiniti%20e%20infinitesimi.md#^definizione-o-piccolo) e di [_equivalenza asintotica_](Infiniti%20e%20infinitesimi.md#^definizione-equivalenza-asintotica).

> [!definizione]+ Definizione: ordine di infinito
> 
> Date due [funzioni](Matematica/Teoria%20degli%20insiemi/Funzioni/_index.md#^definizione-funzione) $f,g \colon A \subseteq \mathbb{R} \to \mathbb{R}$ (con $A \ne \emptyset$) e un [punto di accumulazione](Topologia%20dei%20reali.md#^definizione-punto-di-accumulazione) $x_0 \in \mathbb{R} \cup \{ \pm \infty \}$ per $A$, con $f$ e $g$ [infiniti](Infiniti%20e%20infinitesimi.md#^definizione-infinito-e-infinitesimo) in $x_0$, se $f$ è [$o$-piccolo](Infiniti%20e%20infinitesimi.md#^definizione-o-piccolo) di $g$ per $x \to x_0$, allora diciamo che
> - **$f$ ha un ordine di infinito inferiore a $g$ per $x \to x_0$** (o che **$f$ è un infinito di ordine inferiore a $g$ per $x \to x_0$**)  e
> - **$g$ ha un ordine di infinito superiore a $f$ per $x \to x_0$** (o che **$g$ è un infinito di ordine superiore a $f$ per $x \to x_0$**):
> 
> $$
> \begin{array}{}
> f = o(g) \text{ per } x \to x_0 \\
> \Updownarrow \\
> f \text{ ha un ordine di infinito inferiore a } g \text{ per } x \to x_0 \\
> \land\ g \text{ ha un ordine di infinito superiore a } f \text{ per } x \to x_0 \\
> \end{array}
> $$
> 
> Se invece $f$ è [equivalente](Infiniti%20e%20infinitesimi.md#^definizione-equivalenza-asintotica) a $l \cdot g$ per $x \to x_0$ (con $l \in \mathbb{R} \setminus \{ 0 \}$), allora diciamo che **$f$ e $g$ hanno lo stesso ordine di infinito per $x \to x_0$**:
> 
> $$
> \forall l \in \mathbb{R} \setminus \{ 0 \} . \left( 
> \begin{array}{}
> f \sim l \cdot g \text{ per } x \to x_0 \\
> \Updownarrow \\
> f \text{ e } g \text{ hanno lo stesso ordine di infinito per } x \to x_0
> \end{array}
> \right) 
> $$
^definizione-ordine-di-infinito

%% 
Analoghe definizioni si introducono per $x \to x_0^\pm$ se $x_0 \in \mathbb{R}$
%%

%% 
esempi 4.21 pagg. 202-203 lancelotti
%%

> [!definizione]+ Definizione: ordine di infinitesimo
> 
> Date due [funzioni](Matematica/Teoria%20degli%20insiemi/Funzioni/_index.md#^definizione-funzione) $f,g \colon A \subseteq \mathbb{R} \to \mathbb{R}$ (con $A \ne \emptyset$) e un [punto di accumulazione](Topologia%20dei%20reali.md#^definizione-punto-di-accumulazione) $x_0 \in \mathbb{R} \cup \{ \pm \infty \}$ per $A$, con $f$ e $g$ [infinitesimi](Infiniti%20e%20infinitesimi.md#^definizione-infinito-e-infinitesimo) in $x_0$, se $f$ è [$o$-piccolo](Infiniti%20e%20infinitesimi.md#^definizione-o-piccolo) di $g$ per $x \to x_0$, allora diciamo che
> - **$f$ ha un ordine di infinitesimo superiore a $g$ per $x \to x_0$** (o che **$f$ è un infinitesimo di ordine superiore a $g$ per $x \to x_0$**)  e
> - **$g$ ha un ordine di infinitesimo inferiore a $f$ per $x \to x_0$** (o che **$g$ è un infinitesimo di ordine inferiore a $f$ per $x \to x_0$**):
> 
> $$
> \begin{array}{}
> f = o(g) \text{ per } x \to x_0 \\
> \Updownarrow \\
> f \text{ ha un ordine di infinitesimo superiore a } g \text{ per } x \to x_0 \\
> \land\ g \text{ ha un ordine di infinitesimo inferiore a } f \text{ per } x \to x_0 \\
> \end{array}
> $$
> 
> Se invece $f$ è [equivalente](Infiniti%20e%20infinitesimi.md#^definizione-equivalenza-asintotica) a $l \cdot g$ per $x \to x_0$ (con $l \in \mathbb{R} \setminus \{ 0 \}$), allora diciamo che **$f$ e $g$ hanno lo stesso ordine di infinitesimo per $x \to x_0$**:
> 
> $$
> \forall l \in \mathbb{R} \setminus \{ 0 \} . \left( 
> \begin{array}{}
> f \sim l \cdot g \text{ per } x \to x_0 \\
> \Updownarrow \\
> f \text{ e } g \text{ hanno lo stesso ordine di infinitesimoo per } x \to x_0
> \end{array}
> \right) 
> $$
^definizione-ordine-di-infinitesimo

%% 
Analoghe definizioni si introducono per $x \to x_0^\pm$ se $x_0 \in \mathbb{R}$
%%

%% 
esempi 4.23 pagg. 203-204 lancelotti
%%

> [!osservazione]+ Osservazione: differenza di significato di $\color{#7F7F7F} f = o(g)$ tra infiniti e infinitesimi
> 
> Dalle definizioni sull'[_ordine di infinito_](Infiniti%20e%20infinitesimi.md#^definizione-ordine-di-infinito) e l'[_ordine di infinitesimo_](Infiniti%20e%20infinitesimi.md#^definizione-ordine-di-infinitesimo) possiamo evincere che la scrittura $f = o(g)$ ha un significato diverso a seconda che $f$ e $g$ siano entrambi [infiniti](Infiniti%20e%20infinitesimi.md#^definizione-infinito-e-infinitesimo) o [infinitesimi](Infiniti%20e%20infinitesimi.md#^definizione-infinito-e-infinitesimo). In particolare:
> 
> |                            | **$f$ e $g$ [infiniti](Infiniti%20e%20infinitesimi.md#^definizione-infinito-e-infinitesimo)**                  | **$f$ e $g$ [infinitesimi](Infiniti%20e%20infinitesimi.md#^definizione-infinito-e-infinitesimo)**                      |
> | -------------------------- | -------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------- |
> | $f = o(g)$ per $x \to x_0$ | $f$ ha un [ordine di infinito](Infiniti%20e%20infinitesimi.md#^definizione-ordine-di-infinito) inferiore a $g$ | $f$ ha un [ordine di infinitesimo](Infiniti%20e%20infinitesimi.md#^definizione-ordine-di-infinitesimo) superiore a $g$ |

%% 
esercizi 4.25 pag. 204 lancelotti
%%

## 2.1 - Infiniti e infinitesimi campione

Sin qui abbiamo introdotto una terminologia per confrontare fra loro gli [infiniti](Infiniti%20e%20infinitesimi.md#^definizione-infinito-e-infinitesimo) e gli [infinitesimi](Infiniti%20e%20infinitesimi.md#^definizione-infinito-e-infinitesimo). Poiché la casistica è vasta, per poterli confrontare in modo rapido è necessario avere a disposizione delle [funzioni](Matematica/Teoria%20degli%20insiemi/Funzioni/_index.md#^definizione-funzione) che svolgano il ruolo di "sistemi di riferimento" con cui confrontarli. Queste [funzioni](Matematica/Teoria%20degli%20insiemi/Funzioni/_index.md#^definizione-funzione) sono gli [_infiniti e gli infinitesimi campione_](Infiniti%20e%20infinitesimi.md#^definizione-infiniti-e-infinitesimi-campione).

Poiché le [funzioni](Matematica/Teoria%20degli%20insiemi/Funzioni/_index.md#^definizione-funzione) più "semplici" sono quelle razionali%% link %%, questi [_infiniti e gli infinitesimi campione_](Infiniti%20e%20infinitesimi.md#^definizione-infiniti-e-infinitesimi-campione) sono proprio funzioni razionali%% link %%.

> [!definizione]+ Definizione: infiniti e infinitesimi campione
> 
> Dato un punto%% link %% $x_0$:
> - Se $x_0 \in \mathbb{R}$, allora l'**infinito campione** è la [funzione](Matematica/Teoria%20degli%20insiemi/Funzioni/_index.md#^definizione-funzione) $u(x) = \dfrac{1}{|x -x _0|}$.
> - Se $x_0 = \pm \infty$, allora l'**infinito campione** è la [funzione](Matematica/Teoria%20degli%20insiemi/Funzioni/_index.md#^definizione-funzione) $u(x) = \vert x \vert$.
> - Se $x_0 \in \mathbb{R}$, allora l'**infinitesimo campione** è la [funzione](Matematica/Teoria%20degli%20insiemi/Funzioni/_index.md#^definizione-funzione) $u(x) = |x - x_0|$.
> - Se $x_0 = \pm \infty$, allora l'**infinitesimo campione** è la [funzione](Matematica/Teoria%20degli%20insiemi/Funzioni/_index.md#^definizione-funzione) $u(x) = \dfrac{1}{\vert x \vert}$.
> 
> |                      | **Infinito campione**           | **Infinitesimo campione** |
> | -------------------- | ------------------------------- | ------------------------- |
> | $x_0 \in \mathbb{R}$ | $u(x) = \dfrac{1}{\vert x - x_0 \vert}$ | $u(x) = \vert x - x_0 \vert$      |
> | $x_0 = \pm \infty$   | $u(x) = \vert x \vert$                  | $u(x) = \dfrac{1}{\vert x \vert}$ |
^definizione-infiniti-e-infinitesimi-campione

%% 
Sì, **in questa definizione il valore assoluto è opportuno**, perché rende la nozione indipendente dal lato da cui ci si avvicina a (x_0) e garantisce che le funzioni campione siano sempre positive.

Per esempio, se (x_0 \in \mathbb{R}):

[  
u(x)=\frac1{|x-x_0|}  
]

ha la proprietà che

[  
\lim_{x\to x_0} u(x)=+\infty,  
]

sia da destra sia da sinistra.

Se invece scrivessi

[  
u(x)=\frac1{x-x_0},  
]

allora:

[  
\lim_{x\to x_0^+}\frac1{x-x_0}=+\infty,  
\qquad  
\lim_{x\to x_0^-}\frac1{x-x_0}=-\infty,  
]

quindi non avresti un "infinito campione" che tende semplicemente a (+\infty), ma una funzione che cambia segno.

Lo stesso vale per l'infinitesimo campione:

[  
u(x)=|x-x_0|  
]

soddisfa

[  
\lim_{x\to x_0}u(x)=0^+.  
]

Senza valore assoluto,

[  
u(x)=x-x_0,  
]

tende comunque a (0), quindi come infinitesimo potrebbe ancora funzionare, ma assumerebbe valori positivi e negativi.

In molti testi si usa il valore assoluto perché gli **infiniti e infinitesimi campione** servono come modelli di riferimento e si preferisce che siano sempre positivi. Se invece stai studiando limiti unilaterali, puoi tranquillamente usare

[  
\frac1{x-x_0}  
\quad\text{oppure}\quad  
x-x_0,  
]

specificando il verso di avvicinamento.

Quindi:
- per un **infinito campione bilaterale**: il valore assoluto è sostanzialmente necessario;
- per un **infinitesimo campione**: non è strettamente necessario per avere limite (0), ma è comodo e coerente con la convenzione di considerare infinitesimi positivi.
%%

La presenza del valore assoluto%% link %% negli [infiniti e infinitesimi campione](Infiniti%20e%20infinitesimi.md#^definizione-infiniti-e-infinitesimi-campione) è giustificata dalla seguente definizione.

> [!definizione]+ Definizione: infinit(esim)o di ordine $\color{#FF7FFF} \alpha$ rispetto all'infinit(esim)o campione $\color{#FF7FFF} u$
> 
> Date due [funzioni](Matematica/Teoria%20degli%20insiemi/Funzioni/_index.md#^definizione-funzione) $f,g \colon A \subseteq \mathbb{R} \to \mathbb{R}$ (con $A \ne \emptyset$) e un [punto di accumulazione](Topologia%20dei%20reali.md#^definizione-punto-di-accumulazione) $x_0 \in \mathbb{R} \cup \{ \pm \infty \}$ per $A$ con $f$ [infinito](Infiniti%20e%20infinitesimi.md#^definizione-infinito-e-infinitesimo) (o [infinitesimo](Infiniti%20e%20infinitesimi.md#^definizione-infinito-e-infinitesimo)) in $x_0$, diciamo che **$f$ è un [infinito (o infinitesimo)](Infiniti%20e%20infinitesimi.md#^definizione-infinito-e-infinitesimo) di ordine $\alpha > 0$ rispetto all'[infinito (o infinitesimo) campione](Infiniti%20e%20infinitesimi.md#^definizione-infiniti-e-infinitesimi-campione) $u$ per $x \to x_0$** se
> 
> $$
> \begin{array}{}
> \displaystyle\lim_{x \to x_0} \dfrac{f(x)}{[u(x)]^\alpha} = l \in \mathbb{R} \setminus \{ 0 \} \\
> \Updownarrow \\
> f(x) \sim l[u(x)]^\alpha \text{ per } x \to x_0 \text{ con } l \in \mathbb{R} \setminus \{ 0 \} \\
> \Updownarrow \\
> f(x) = l[u(x)]^\alpha + o([u(x)]^\alpha) \text{ per } x \to x_0 \text{ con } l \in \mathbb{R} \setminus \{ 0 \}
> \end{array}
> $$
> 
> In tal caso diciamo che $l[u(x)]^\alpha$ è la **parte principale dell'[infinito (o infinitesimo)](Infiniti%20e%20infinitesimi.md#^definizione-infinito-e-infinitesimo) $f$ rispetto all'[infinito (o infinitesimo) campione](Infiniti%20e%20infinitesimi.md#^definizione-infiniti-e-infinitesimi-campione) $u$ per $x \to x_0$**.
^definizione-infinitesimo-di-ordine-alfa-rispetto-all-infinitesimo-campione-u

%% 
Analoghe definizioni si introducono per $x \to x_0^\pm$ se $x_0 \in \mathbb{R}$
%%

> [!osservazione]+ Osservazione: come va inteso un infinit(esim)o di ordine $\color{#7F7F7F} \alpha$ rispetto all'infinit(esim)o campione $\color{#7F7F7F} u$
> 
> Quando diciamo che $f$ è un [infinito (o infinitesimo) di ordine $\alpha$ rispetto all'infinito (o infinitesimo) campione $u(x)$](Infiniti%20e%20infinitesimi.md#^definizione-infinitesimo-di-ordine-alfa-rispetto-all-infinitesimo-campione-u) per $x \to x_0$, stiamo dicendo che $f$ si comporta come $u^\alpha$, a meno di una costante.
> 
> In pratica, l'ordine $\alpha$ misura la velocità di avvicinamento a $0$ (o di fuga verso $\pm \infty$) usando l'[infinito (o infinitesimo) campione](Infiniti%20e%20infinitesimi.md#^definizione-infiniti-e-infinitesimi-campione) $u$ come "righello": più è alto l'ordine, più rapidamente la funzione va verso $0$ o verso $\pm \infty$.
> 
> Per esempio, prendendo per $x \to 0$ l'[infinitesimo campione](Infiniti%20e%20infinitesimi.md#^definizione-infiniti-e-infinitesimi-campione) $u(x) = |x - x_0| = \vert x \vert$, si ha una gerarchia naturale:
> 
> | Ordine $\alpha$         | **[Infinitesimi](Infiniti%20e%20infinitesimi.md#^definizione-infinito-e-infinitesimo) di esempio** | **Comportamento**                        |
> | ----------------------- | -------------------------------------------------------------------------------------------------- | ---------------------------------------- |
> | $\alpha = \dfrac{1}{2}$ | $\sqrt x$                                                                                          | Tendono a $0$ più lentamente di $\vert x \vert$  |
> | $\alpha = 1$            | $\sin x$, $\tan x$, $3x$                                                                           | Tendono a $0$ come $\vert x \vert$               |
> | $\alpha = 2$            | $x^2 - x^4$, $1 - \cos x$                                                                          | Tendono a $0$ più velocemente di $\vert x \vert$ |
> | $\alpha = 3$            | $x - \sin x$, $x^3$                                                                                | Tendono a $0$ ancora più velocemente     |

> [!osservazione]+ Osservazione: perché serve che $\color{#7F7F7F} l \in \mathbb{R} \setminus \{ 0 \}$?
> 
> Il [limite](Matematica/Analisi%20matematica/Limiti/_index.md#^definizione-limite) di $\dfrac{f(x)}{[u(x)]^\alpha}$ deve essere finito%% link %% e non nullo%% link %% perché:
> - Se fosse $0$, significherebbe che $[u(x)]^\alpha$ cresce (o decresce) molto più velocemente di $f$, quindi l'ordine $\alpha$ va abbassato. 
> - Se fosse $\pm \infty$, significherebbe che $[u(x)]^\alpha$ cresce (o decresce) molto più lentamente di $f$, quindi l'ordine $\alpha$ va alzato. 
> 
> L'ordine $\alpha$ è dunque il valore "giusto" che risponde alla domanda: "alzando $u$ alla potenza $\alpha$, riesco a tenere il passo con $f$?". Quando il [limite](Matematica/Analisi%20matematica/Limiti/_index.md#^definizione-limite) dà un $l \in \mathbb{R} \setminus \{0\}$, la risposta è sì: $\alpha$ è quello corretto, e $l[u(x)]^\alpha$ è la [parte principale](Infiniti%20e%20infinitesimi.md#^definizione-infinitesimo-di-ordine-alfa-rispetto-all-infinitesimo-campione-u), cioè l'approssimazione più semplice di $f$ vicino a $x_0$.

> [!esempio]- Esempio: $\color{#7F7FFF} \sin x$ infinitesimo di ordine $\color{#7F7FFF} 1$ rispetto all'infinitesimo campione $\color{#7F7FFF} u(x) = \vert x \vert$
> 
> Supponiamo che valga il [limite](Matematica/Analisi%20matematica/Limiti/_index.md#^definizione-limite)
> 
> $$
> \lim_{x \to 0} \sin x = 0
> $$
> 
> Ciò significa che $\sin x$ è un [infinitesimo](Infiniti%20e%20infinitesimi.md#^definizione-infinito-e-infinitesimo) in $0$. Essendo un [infinitesimo](Infiniti%20e%20infinitesimi.md#^definizione-infinito-e-infinitesimo) con $l = 0 \in \mathbb{R}$, il suo [infinitesimo campione](Infiniti%20e%20infinitesimi.md#^definizione-infiniti-e-infinitesimi-campione) è
> 
> $$
> u(x) = |x - x_0| = |x - 0| = \vert x \vert
> $$
> 
> Dal momento che vale il [limite](Matematica/Analisi%20matematica/Limiti/_index.md#^definizione-limite) (con $\alpha = 1$)
> 
> $$
> \lim_{x \to 0} \dfrac{\sin x}{\vert x \vert^1} = 1
> $$
> 
> possiamo concludere che $\sin x$ è un [infinitesimo di ordine $1$ rispetto all'infinitesimo campione $u(x) = \vert x \vert$](Infiniti%20e%20infinitesimi.md#^definizione-infinitesimo-di-ordine-alfa-rispetto-all-infinitesimo-campione-u) per $x \to 0$, con [parte principale](Infiniti%20e%20infinitesimi.md#^definizione-infinitesimo-di-ordine-alfa-rispetto-all-infinitesimo-campione-u) $1 \cdot \vert x \vert^1 = x$.

%% 
osservazioni c,d,e, pagg. 206-207
%%

%% 
esempi pagg. 207-208
%%

> [!definizione]+ Definizione: infinit(esim)o di ordine superiore o inferiore a qualsiasi potenza di $\color{#FF7FFF} u(x)$
> 
> Data una [funzione](Matematica/Teoria%20degli%20insiemi/Funzioni/_index.md#^definizione-funzione) $f \colon A \subseteq \mathbb{R} \to \mathbb{R}$ (con $A \ne \emptyset$) e un [punto di accumulazione](Topologia%20dei%20reali.md#^definizione-punto-di-accumulazione) $x_0 \in \mathbb{R} \cup \{ \pm \infty \}$ per $A$ con $f$ [infinito](Infiniti%20e%20infinitesimi.md#^definizione-infinito-e-infinitesimo) (o [infinitesimo](Infiniti%20e%20infinitesimi.md#^definizione-infinito-e-infinitesimo)) in $x_0$, diciamo che $f(x)$ è un **[infinito](Infiniti%20e%20infinitesimi.md#^definizione-infinito-e-infinitesimo) di ordine superiore o [infinitesimo](Infiniti%20e%20infinitesimi.md#^definizione-infinito-e-infinitesimo) di ordine inferiore a qualsiasi potenza di un [infinito o infinitesimo campione](Infiniti%20e%20infinitesimi.md#^definizione-infiniti-e-infinitesimi-campione) $u(x)$** per $x \to x_0$ se:
> 
> $$
> \forall k \in \mathbb{R}^{> 0} . \big( [u(x)]^k = o(f(x)) \big)
> $$
> 
> cioè se $f(x)$ è un [infinito](Infiniti%20e%20infinitesimi.md#^definizione-infinito-e-infinitesimo) tende a $\pm\infty$ più velocemente di $|u(x)|^k$ per ogni $k$, mentre se è un [infinitesimo](Infiniti%20e%20infinitesimi.md#^definizione-infinito-e-infinitesimo) tende a $0$ più lentamente di $|u(x)|^k$ per ogni $k$.
> 
> Al contrario, $f(x)$ è un **[infinito](Infiniti%20e%20infinitesimi.md#^definizione-infinito-e-infinitesimo) di ordine inferiore o [infinitesimo](Infiniti%20e%20infinitesimi.md#^definizione-infinito-e-infinitesimo) di ordine superiore a qualsiasi potenza di un [infinito o infinitesimo campione](Infiniti%20e%20infinitesimi.md#^definizione-infiniti-e-infinitesimi-campione) $u(x)$** per $x \to x_0$ se:
> 
> $$
> \forall k \in \mathbb{R}^{> 0} . \big( f(x) = o([u(x)]^k) \big)
> $$
> 
> cioè se $f(x)$ è un [infinito](Infiniti%20e%20infinitesimi.md#^definizione-infinito-e-infinitesimo) tende a $\pm\infty$ più lentamente di $|u(x)|^k$ per ogni $k$, mentre se è un [infinitesimo](Infiniti%20e%20infinitesimi.md#^definizione-infinito-e-infinitesimo) tende a $0$ più velocemente di $|u(x)|^k$ per ogni $k$.
> 
> |                                                                   | **$f(x)$ è un [infinito](Infiniti%20e%20infinitesimi.md#^definizione-infinito-e-infinitesimo)**                                                                              | **$f(x)$ è un [infinitesimo](Infiniti%20e%20infinitesimi.md#^definizione-infinito-e-infinitesimo)**                                                                     |
> | ----------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
> | $\forall k \in \mathbb{R}^{> 0} . \big( [u(x)]^k = o(f(x)) \big)$ | $f(x)$ è un [infinito](Infiniti%20e%20infinitesimi.md#^definizione-infinito-e-infinitesimo) di ordine _superiore_,<br>tende a $\pm \infty$ più _velocemente_ di $\vert u(x)\vert^k$ | $f(x)$ è un [infinitesimo](Infiniti%20e%20infinitesimi.md#^definizione-infinito-e-infinitesimo) di ordine _inferiore_,<br>tende a $0$ più _lentamente_ di $\vert u(x)\vert^k$  |
> | $\forall k \in \mathbb{R}^{> 0} . \big( f(x) = o([u(x)]^k) \big)$ | $f(x)$ è un [infinito](Infiniti%20e%20infinitesimi.md#^definizione-infinito-e-infinitesimo) di ordine _inferiore_,<br>tende a $\pm \infty$ più _lentamente_ di $\vert u(x)\vert^k$  | $f(x)$ è un [infinitesimo](Infiniti%20e%20infinitesimi.md#^definizione-infinito-e-infinitesimo) di ordine _superiore_,<br>tende a $0$ più _velocemente_ di $\vert u(x)\vert^k$ |
^definizione-infinitesimo-di-ordine-superiore-o-inferiore-a-qualsiasi-potenza-di-u-x

%% 
Fare le tre formule equivalenti come nella [definizione dell'ordine $\alpha$](Infiniti%20e%20infinitesimi.md#^definizione-infinitesimo-di-ordine-alfa-rispetto-all-infinitesimo-campione-u)
%%

> [!esempio]- Esempio: $\color{#7F7FFF} f(x) = a^x$ con $\color{#7F7FFF} a > 1$
> 
> La [funzione](Matematica/Teoria%20degli%20insiemi/Funzioni/_index.md#^definizione-funzione) $f(x) = a^x$ (con $a > 1$) è un [infinito](Infiniti%20e%20infinitesimi.md#^definizione-infinito-e-infinitesimo) per $x \to + \infty$ e il suo [infinito campione](Infiniti%20e%20infinitesimi.md#^definizione-infiniti-e-infinitesimi-campione) è $u(x) = \vert x \vert$. Poiché si ha che
> 
> $$
> \forall k \in \mathbb{R}^{> 0} . \big( \vert x \vert^k = o(a^x) \big)
> $$
> 
> allora $a^x$ è un [infinito di ordine superiore a qualsiasi potenza di $\vert x \vert$](Infiniti%20e%20infinitesimi.md#^definizione-infinitesimo-di-ordine-superiore-o-inferiore-a-qualsiasi-potenza-di-u-x) per $x \to + \infty$, cioè $a^x$ tende a $x \to + \infty$ più velocemente di $\vert x \vert^k$, qualsiasi sia la potenza%% link %% $k$.
> 
> Inoltre, è un [infinitesimo](Infiniti%20e%20infinitesimi.md#^definizione-infinito-e-infinitesimo) per $x \to - \infty$ e il suo [infinito campione](Infiniti%20e%20infinitesimi.md#^definizione-infiniti-e-infinitesimi-campione) è $u(x) = \dfrac{1}{\vert x \vert}$. Poiché si ha che
> 
> $$
> \forall k \in \mathbb{R}^{> 0} . \left( a^x = o\left(\left( \dfrac{1}{\vert x \vert} \right) ^k\right) \right)
> $$
> 
> allora $a^x$ è un [infinitesimo di ordine superiore a qualsiasi potenza di $\dfrac{1}{\vert x \vert}$](Infiniti%20e%20infinitesimi.md#^definizione-infinitesimo-di-ordine-superiore-o-inferiore-a-qualsiasi-potenza-di-u-x) per $x \to - \infty$, cioè $a^x$ tende a $x \to - \infty$ più velocemente di $\left( \dfrac{1}{\vert x \vert} \right)^k$, qualsiasi sia la potenza%% link %% $k$.

%% 
Esercizio: cosa avviene con $f(x) = a^x$ con $0 < a < 1$?
Soluzione: i ruoli si invertono
%%

> [!esempio]- Esempio: $\color{#7F7FFF} f(x) = \log_a x$ con $\color{#7F7FFF} a \in \mathbb{R}^{> 0} \setminus \{ 1 \}$
> 
> La [funzione](Matematica/Teoria%20degli%20insiemi/Funzioni/_index.md#^definizione-funzione) $f(x) = \log_a x$ (con $a \in \mathbb{R}^{> 0} \setminus \{ 1 \}$) è un [infinito](Infiniti%20e%20infinitesimi.md#^definizione-infinito-e-infinitesimo) per $x \to + \infty$ e il suo [infinito campione](Infiniti%20e%20infinitesimi.md#^definizione-infiniti-e-infinitesimi-campione) è $u(x) = \vert x \vert$. Poiché si ha che
> 
> $$
> \forall k \in \mathbb{R}^{> 0} . \left( \log_a x = o\left(|x|^k\right) \right) 
> $$
> 
> allora $\log_a x$ è un [infinito di ordine inferiore a qualsiasi potenza di $|x|$](Infiniti%20e%20infinitesimi.md#^definizione-infinitesimo-di-ordine-superiore-o-inferiore-a-qualsiasi-potenza-di-u-x) per $x \to + \infty$, cioè $\log_a x$ tende a $x \to + \infty$ più velocemente di $\vert x \vert^k$, qualsiasi sia la potenza%% link %% $k$.
> 
> Inoltre, è un [infinito](Infiniti%20e%20infinitesimi.md#^definizione-infinito-e-infinitesimo) anche per $x \to 0^+$ e il suo [infinito campione](Infiniti%20e%20infinitesimi.md#^definizione-infiniti-e-infinitesimi-campione) è $u(x) = \dfrac{1}{\vert x - x_0 \vert} = \dfrac{1}{\vert x - 0 \vert} = \dfrac{1}{\vert x \vert}$. Poiché si ha che
> 
> $$
> \forall k \in \mathbb{R}^{> 0} . \left( \log_a x = o\left( \left( \dfrac{1}{\vert x \vert} \right)^k \right) \right) 
> $$
> 
> allora $\log_a x$ è un [infinito di ordine inferiore a qualsiasi potenza di $\dfrac{1}{\vert x \vert}$](Infiniti%20e%20infinitesimi.md#^definizione-infinitesimo-di-ordine-superiore-o-inferiore-a-qualsiasi-potenza-di-u-x) per $x \to 0^+$, cioè $\log_a x$ tende a $x \to 0^+$ più velocemente di $\left( \dfrac{1}{\vert x \vert} \right)^k$, qualsiasi sia la potenza%% link %% $k$.

%% 
esempi 4.33 pagg. 208-209
%%

Ci sono casi però in cui un [infinito](Infiniti%20e%20infinitesimi.md#^definizione-infinito-e-infinitesimo) o un [infinitesimo](Infiniti%20e%20infinitesimi.md#^definizione-infinito-e-infinitesimo) non sono di un [ordine $\alpha$](Infiniti%20e%20infinitesimi.md#^definizione-infinitesimo-di-ordine-alfa-rispetto-all-infinitesimo-campione-u) preciso, ma non sono neanche [superiori o inferiori a qualsiasi potenza](Infiniti%20e%20infinitesimi.md#^definizione-infinitesimo-di-ordine-superiore-o-inferiore-a-qualsiasi-potenza-di-u-x) rispetto all'[infinito o infinitesimo campione](Infiniti%20e%20infinitesimi.md#^definizione-infiniti-e-infinitesimi-campione) $u(x)$, bensì il loro ordine $\alpha$ si trova in un intervallo.

%% 
![[Ordini alfa.png]]

Sistemare questa foto mettendo anche sulla prima retta le varie potenze di u
%%

> [!definizione]+ Definizione: infinit(esim)o di ordine superiore o inferiore all'ordine $\color{#FF7FFF}\alpha$ rispetto all'infinit(esim)o campione $\color{#FF7FFF}u$
>
> Data una [funzione](Matematica/Teoria%20degli%20insiemi/Funzioni/_index.md#^definizione-funzione) $f \colon A \subseteq \mathbb{R} \to \mathbb{R}$ (con $A \ne \emptyset$) e un [punto di accumulazione](Topologia%20dei%20reali.md#^definizione-punto-di-accumulazione) $x_0 \in \mathbb{R} \cup \{ \pm \infty \}$ per $A$ con $f$ [infinito](Infiniti%20e%20infinitesimi.md#^definizione-infinito-e-infinitesimo) (o [infinitesimo](Infiniti%20e%20infinitesimi.md#^definizione-infinito-e-infinitesimo)) in $x_0$, diciamo che **$f(x)$ è un [infinito](Infiniti%20e%20infinitesimi.md#^definizione-infinito-e-infinitesimo) di ordine superiore o [infinitesimo](Infiniti%20e%20infinitesimi.md#^definizione-infinito-e-infinitesimo) di ordine inferiore all'ordine $\alpha$ rispetto all'[infinito o infinitesimo campione](Infiniti%20e%20infinitesimi.md#^definizione-infiniti-e-infinitesimi-campione) $u(x)$ per $x \to x_0$** se
>
> $$
> \lim_{x \to x_0} \frac{f(x)}{[u(x)]^\alpha} = \pm\infty
> $$
> 
> %%cioè se $f(x)$ è O-grande??? di $[u(x)]^\alpha$ (nel caso metterlo come biimplicazione qua%%
> 
> Al contrario, **$f(x)$ è un [infinito](Infiniti%20e%20infinitesimi.md#^definizione-infinito-e-infinitesimo) di ordine inferiore o [infinitesimo](Infiniti%20e%20infinitesimi.md#^definizione-infinito-e-infinitesimo) di ordine superiore all'ordine $\alpha$ rispetto all'[infinito o infinitesimo campione](Infiniti%20e%20infinitesimi.md#^definizione-infiniti-e-infinitesimi-campione) $u(x)$ per $x \to x_0$** se
>
> $$
> \begin{array}{}
> f(x) = o([u(x)]^\alpha) \\
> \Updownarrow \\
> \displaystyle\lim_{x \to x_0} \frac{f(x)}{[u(x)]^\alpha} = 0
> \end{array}
> $$
^definizione-infinitesimo-di-ordine-superiore-o-inferiore-all-ordine-alpha-rispetto-all-infinitesimo-campione-u

%% 
Fare le tre formule equivalenti come nella [definizione dell'ordine $\alpha$](Infiniti%20e%20infinitesimi.md#^definizione-infinitesimo-di-ordine-alfa-rispetto-all-infinitesimo-campione-u)
%%

---

> [!fonti]+ Fonti
> 
> - 📚 Sergio Lancelotti, _Lezioni di Analisi Matematica I_, Celid, 2020 (ISBN: `978-8867891979`):
> 	- Capitolo 3 - _Limiti e continuità_:
> 		- 4 - _Confronto locale fra funzioni_:
> 			- 4.1 - _Infiniti e infinitesimi_.
> 			- 4.2 - _Simboli di Landau_.
> 			- 4.3 - _Confronto fra infiniti e infinitesimi_.
