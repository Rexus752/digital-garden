---
title: Infiniti e infinitesimi
---

> [!premessa] Premessa
> 
> Ciao! Se è la prima volta che capiti su questo sito, ti consiglio di consultare la [pagina principale](index.md) di questo cosiddetto _Giardino Digitale_ per scoprire meglio cos'è e come navigarlo.
> 
> Lo stato di questa nota è al momento: 🔴 <font color="#FF7F7F">_Bozza_</font>.

---

> [!definizione] Definizione: infinito e infinitesimo
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

> [!esempio] Esempi di infiniti e infinitesimi
> 
> Ecco alcuni esempi di [infiniti](Infiniti%20e%20infinitesimi.md#^definizione-infinito-e-infinitesimo) e [infinitesimi](Infiniti%20e%20infinitesimi.md#^definizione-infinito-e-infinitesimo):
> - La [funzione](content/Matematica/Teoria%20degli%20insiemi/Funzioni/_index.md#^definizione-funzione) $f(x) = x^n$ con $n \in \mathbb{N}^{ \ge 1}$ è un [infinitesimo](Infiniti%20e%20infinitesimi.md#^definizione-infinito-e-infinitesimo) per $x \to 0$ e un [infinitesimo](Infiniti%20e%20infinitesimi.md#^definizione-infinito-e-infinitesimo) per $x \to \pm \infty$.
> - La [funzione](content/Matematica/Teoria%20degli%20insiemi/Funzioni/_index.md#^definizione-funzione) $f(x) = \dfrac{1}{x^n}$ con $n \in \mathbb{N}^{\ge 1}$ è un [infinito](Infiniti%20e%20infinitesimi.md#^definizione-infinito-e-infinitesimo) per $x \to 0$ e un [infinitesimo](Infiniti%20e%20infinitesimi.md#^definizione-infinito-e-infinitesimo) per $x \to \pm \infty$.
> - La [funzione](content/Matematica/Teoria%20degli%20insiemi/Funzioni/_index.md#^definizione-funzione) $f(x) = e^x$ è un [infinitesimo](Infiniti%20e%20infinitesimi.md#^definizione-infinito-e-infinitesimo) per $x \to - \infty$ e un [infinito](Infiniti%20e%20infinitesimi.md#^definizione-infinito-e-infinitesimo) per $x \to + \infty$.
> - La [funzione](content/Matematica/Teoria%20degli%20insiemi/Funzioni/_index.md#^definizione-funzione) $f(x) = \ln x$ è un [infinito](Infiniti%20e%20infinitesimi.md#^definizione-infinito-e-infinitesimo) per $x \to 0^+$ e per $x \to + \infty$ e un [infinitesimo](Infiniti%20e%20infinitesimi.md#^definizione-infinito-e-infinitesimo) per $x \to 1$.

> [!proposizione] Proposizione: rapporto tra infiniti e infinitesimi
> 
> Data una [funzione](Matematica/Teoria%20degli%20insiemi/Funzioni/_index.md#^definizione-funzione) $f \colon \text{dom}(f) \to \mathbb{R}$ e un [punto di accumulazione](Topologia%20dei%20reali.md#^definizione-punto-di-accumulazione) $x_0 \in \mathbb{R} \cup \{ \pm \infty \}$ per $\text{dom}(f)$, se in ogni [intorno](Topologia%20dei%20reali.md#^definizione-intorno-di-un-punto) $I(x_0)$ di $x_0$ esiste un $x \in \text{dom}(f) \setminus \{ x_0 \}$ tale che $f(x) \ne 0$, allora $f$ è un [infinitesimo](Infiniti%20e%20infinitesimi.md#^definizione-infinito-e-infinitesimo) in $x_0$ se e solo se $\dfrac{1}{f}$ è un [infinito](Infiniti%20e%20infinitesimi.md#^definizione-infinito-e-infinitesimo) in $x_0$:
> 
> $$
> f \text{ infinitesimo in } x_0 \iff \dfrac{1}{f} \text{ infinito in } x_0
> $$
^proposizione-rapporto-tra-infiniti-e-infinitesimi

%%
[!dimostrazione] Dimostrazione

Per esercizio
%%

# Simboli di Landau

Introduciamo ora delle nozioni che ci permettono di confrontare localmente%% link %% le [funzioni](content/Matematica/Teoria%20degli%20insiemi/Funzioni/_index.md#^definizione-funzione), cioè in un [intorno](Topologia%20dei%20reali.md#^definizione-intorno-di-un-punto) di un punto%% Link %%. Poiché la nozione locale più generale che conosciamo è quella del [_limite_](content/Matematica/Analisi%20matematica/Limiti/_index.md#^definizione-limite), tutte queste nozioni che introdurremo si baseranno su di essa, anzi non saranno altro che un modo diverso di scrivere l'operazione%% link %% di [limite](content/Matematica/Analisi%20matematica/Limiti/_index.md#^definizione-limite). Faremo ciò attraverso quelli che vengono chiamati [_simboli di Landau_](Infiniti%20e%20infinitesimi.md#^definizione-simboli-di-landau).

> [!definizione] Definizione: simboli di Landau
> 
> I **simboli di Landau** (o **notazione asintotica**) sono un linguaggio formale%% link %% per confrontare il comportamento di due [funzioni](content/Matematica/Teoria%20degli%20insiemi/Funzioni/_index.md#^definizione-funzione) in prossimità di un punto%% Link %% (finito%% Link %% o infinito%% Link %%). Non descrivono il valore%% Link %% di una [funzione](content/Matematica/Teoria%20degli%20insiemi/Funzioni/_index.md#^definizione-funzione), ma la sua velocità di crescita relativa rispetto a un'altra.
> 
> I **simboli di Landau** sono l'[$o$-piccolo](Infiniti%20e%20infinitesimi.md#^definizione-o-piccolo), l'[equivalenza asintotica $\sim$](Infiniti%20e%20infinitesimi.md#^definizione-equivalenza-asintotica), ... e prendono il nome dal matematico tedesco Edmund Landau che li ha ideati e formalizzati.
^definizione-simboli-di-landau

## $o$-piccolo

> [!definizione] Definizione: $o$-piccolo
> 
> Date due [funzioni](content/Matematica/Teoria%20degli%20insiemi/Funzioni/_index.md#^definizione-funzione) $f,g \colon A \subseteq \mathbb{R} \to \mathbb{R}$ (con $A \ne \emptyset$) e un [punto di accumulazione](Topologia%20dei%20reali.md#^definizione-punto-di-accumulazione) $x_0 \in \mathbb{R} \cup \{ \pm \infty \}$ per $A$, diciamo che **$f$ è $o$-piccolo di $g$ per $x$ che tende a $x_0$** se
> 
> $$
> \lim_{x \to x_0} \dfrac{f(x)}{g(x)} = 0
> $$
> 
> e in tal caso scriviamo "$f = o(g)$ per $x \to x_0$" (oppure "$f(x) = o(g(x))$ per $x \to x_0$").
> 
> L'**$o$-piccolo** è uno dei [simboli di Landau](Infiniti%20e%20infinitesimi.md#^definizione-simboli-di-landau).
^definizione-o-piccolo

> [!osservazione] Osservazione: nell'$o$-piccolo $g$ non identicamente nulla
> 
> Affinché l'[$o$-piccolo](Infiniti%20e%20infinitesimi.md#^definizione-o-piccolo) sia ben definito (e cioè, affinché possa esistere il [limite](content/Matematica/Analisi%20matematica/Limiti/_index.md#^definizione-limite)), è necessario che la [funzione](content/Matematica/Teoria%20degli%20insiemi/Funzioni/_index.md#^definizione-funzione) $g$ non sia [identicamente nulla](content/Matematica/Teoria%20degli%20insiemi/Funzioni/_index.md#^definizione-funzione-identicamente-nulla) in alcun [intorno bucato](Topologia%20dei%20reali.md#^definizione-intorno-bucato-di-un-punto) $I(x_0)$ di $x_0$ [intersecato](content/Matematica/Teoria%20degli%20insiemi/_index.md#^definizione-intersezione-di-due-insiemi) con $A$:
> 
> $$
> \begin{array}{}
> f o(g) \text{ per } x \to x_0 \\
> \Downarrow \\
> g \text{ non identicamente nulla per ogni } (I(x_0) \cap A) \setminus \{ x_0 \}
> \end{array}
> $$
> 
> Ciò garantisce che il rapporto%% link %% $\dfrac{f}{g}$ sia definito in un [insieme](content/Matematica/Teoria%20degli%20insiemi/_index.md#^definizione-insieme) di punti%% link %% che si [accumula](Topologia%20dei%20reali.md#^definizione-punto-di-accumulazione) su $x_0$, permettendoci così di fare affermazioni sensate sul suo comportamento asintotico.
^osservazione-nell-o-piccolo-g-non-identicamente-nulla

> [!esempio] Esempio: $x^2 = o(x)$ per $x \to 0$ e $x = o(x^2)$ per $x \to \pm \infty$
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

> [!esempio] Esempio: $\sin x = o(\sqrt x)$ per $x \to 0^+$
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

> [!esempio] Esempio: $o$-piccolo tra $x^p$ e $x^q$
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

### Proprietà dell'$o$-piccolo

> [!proprieta] Proprietà: transitività di $o$-piccolo
> 
> Vale la proprietà transitiva%% Link %% per [$o$-piccolo](Infiniti%20e%20infinitesimi.md#^definizione-o-piccolo): se $f = o(g)$ e $g = o(h)$ per un certo $x \to x_0$, allora vale anche $f = o(h)$ per $x \to x_0$, infatti
> 
> $$
> \lim_{x \to x_0} \dfrac{f(x)}{h(x)} = \lim_{x \to x_0} \left( \dfrac{f(x)}{h(x)} \cdot \dfrac{g(x)}{g(x)} \right) = \lim_{x \to x_0} \left( \underbrace{\dfrac{f(x)}{g(x)}}_{=0} \cdot \underbrace{\dfrac{g(x)}{h(x)}}_{=0} \right) = 0
> $$
^proprieta-transitivita-di-o-piccolo

> [!attenzione] Attenzione: abuso di notazione nei simboli di Landau
> 
> Nella notazione di [$o$-piccolo](Infiniti%20e%20infinitesimi.md#^definizione-o-piccolo) $f = o(g)$, il simbolo $=$ **NON** è un'uguaglianza%% link %% di fatto tra [funzioni](content/Matematica/Teoria%20degli%20insiemi/Funzioni/_index.md#^definizione-funzione), ma sta solo ad indicare una proprietà qualitativa di $f$ rispetto a $g$.
> 
> Non è quindi applicabile la proprietà transitiva dell'uguaglianza%% link %%, cioè
> 
> $$
> f = o(g) \land h = o(g) \not \implies f = h
> $$
> 
> Infatti, $x^2 = o(x)$ e $x^3 = o(x)$ ma $x^2 \ne x^3$.
^attenzione-abuso-di-notazione-nei-simboli-di-landau

> [!proposizione] Proposizione: $o$-piccolo di se stesso
> 
> Data una [funzione](content/Matematica/Teoria%20degli%20insiemi/Funzioni/_index.md#^definizione-funzione) $f$, l'[$o$-piccolo](Infiniti%20e%20infinitesimi.md#^definizione-o-piccolo) di $f$ è [$o$-piccolo](Infiniti%20e%20infinitesimi.md#^definizione-o-piccolo) di $f$ per $x \to x_0$ (che può sembrare uno scioglilingua, ma non lo è), cioè vale
> 
> $$
> \lim_{x \to x_0} \dfrac{o(f(x))}{f(x)} = 0
> $$
> 
> > [!dimostrazione] Dimostrazione
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
> > Notiamo che l'uguaglianza $f(x) = o(g(x))$ è da intendersi come un semplice collegamento "qualitativo" tra $f$ e $g$, cioè indica che $f$ è una qualsiasi [funzione](content/Matematica/Teoria%20degli%20insiemi/Funzioni/_index.md#^definizione-funzione) che è [$o$-piccolo](Infiniti%20e%20infinitesimi.md#^definizione-o-piccolo) di $g$ per $x \to x_0$, quindi perfettamente in accordo con [quanto detto prima sull'abuso di notazione](Infiniti%20e%20infinitesimi.md#^attenzione-abuso-di-notazione-nei-simboli-di-landau).
> > 
> > $\blacksquare$
^proposizione-o-piccolo-di-se-stesso

> [!proposizione] Proposizione: $o$-piccolo, infiniti e infinitesimi
> 
> Data una [funzione](content/Matematica/Teoria%20degli%20insiemi/Funzioni/_index.md#^definizione-funzione) $f$ che è [$o$-piccolo](Infiniti%20e%20infinitesimi.md#^definizione-o-piccolo) di $1$ per $x \to x_0$, si ha che $f$ è un [infinitesimo](Infiniti%20e%20infinitesimi.md#^definizione-infinito-e-infinitesimo) in $x_0$ e, al contrario, se $1$ è [$o$-piccolo](Infiniti%20e%20infinitesimi.md#^definizione-o-piccolo) di $f$ per $x \to x_0$, allora $f$ è un [infinito](Infiniti%20e%20infinitesimi.md#^definizione-infinito-e-infinitesimo) in $x_0$:
> 
> $$
> \begin{align*}
> f = o(1) \text{ per } x \to x_0 \iff & f \text{ è un infinitesimo in } x_0 \\
> 1 = o(f) \text{ per } x \to x_0 \iff & f \text{ è un infinito in } x_0
> \end{align*}
> $$
> 
> > [!dimostrazione] Dimostrazione
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

### Trascurabilità di una funzione

> [!definizione] Definizione: trascurabilità di una funzione
> 
> Date due [funzioni](content/Matematica/Teoria%20degli%20insiemi/Funzioni/_index.md#^definizione-funzione) $f,g \colon A \subseteq \mathbb{R} \to \mathbb{R}$ (con $A \ne \emptyset$) e un [punto di accumulazione](Topologia%20dei%20reali.md#^definizione-punto-di-accumulazione) $x_0 \in \mathbb{R} \cup \{ \pm \infty \}$ per $A$, se $f$ è [$o$-piccolo](Infiniti%20e%20infinitesimi.md#^definizione-o-piccolo) di $g$ per $x \to x_0$, allora diciamo che **$f$ è trascurabile rispetto a $g$ per $x \to x_0$**.
^definizione-trascurabilita-di-una-funzione

> [!osservazione] Osservazione: significato di _trascurabilità_
> 
> Cerchiamo di comprendere meglio il significato di questa denominazione, anche al fine di evitare equivoci.
> 
> La dicitura "$f$ è [trascurabile](Infiniti%20e%20infinitesimi.md#^definizione-trascurabilita-di-una-funzione) rispetto a $g$ per $x \to x_0$" indica che il [limite](content/Matematica/Analisi%20matematica/Limiti/_index.md#^definizione-limite)
> 
> $$
> \lim_{x \to x_0} \big( f(x) + g(x) \big) 
> $$
> 
> dipende solo da $g$ e non da $f$, cioè nel calcolare questo [limite](content/Matematica/Analisi%20matematica/Limiti/_index.md#^definizione-limite) l'addendo $f(x)$ può essere trascurato rispetto a $g(x)$. Quindi si ha che
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
> Essendo $f$ [$o$-piccolo](Infiniti%20e%20infinitesimi.md#^definizione-o-piccolo) di $g(x)$ per $x \to x_0$, si ha che $\displaystyle\lim_{x \to x_0} \dfrac{f(x)}{g(x)} = 0$. Se esiste il [limite](content/Matematica/Analisi%20matematica/Limiti/_index.md#^definizione-limite) $\displaystyle\lim_{x \to x_0} g(x) = l \in \mathbb{R} \cup \{ \pm \infty \}$, allora per l'algebra dei limiti%% link %% si ha che
> 
> $$
> \lim_{x \to x_0} \big( f(x) + g(x) \big) = \lim_{x \to x_0} \left( \underbrace{g(x)}_{= l} \left( \underbrace{\dfrac{f(x)}{g(x)}}_{= 0} + 1 \right)  \right) = l = \lim_{x \to x_0} g(x)
> $$
> 
> Se invece non esiste il [limite](content/Matematica/Analisi%20matematica/Limiti/_index.md#^definizione-limite) $\displaystyle\lim_{x \to x_0} g(x)$, allora anche il [limite](content/Matematica/Analisi%20matematica/Limiti/_index.md#^definizione-limite) $\displaystyle\lim_{x \to x_0} \big( f(x) + g(x) \big)$ non esiste. Infatti, se per assurdo esistesse questo [limite](content/Matematica/Analisi%20matematica/Limiti/_index.md#^definizione-limite) e fosse $\displaystyle\lim_{x \to x_0} \big( f(x) + g(x) \big) = l' \in \mathbb{R} \cup \{ \pm \infty \}$, poiché
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
> e otterremmo l'assurda affermazione che $\displaystyle\lim_{x\to x_0} g(x) = l'$ che va in contrasto con l'ipotesi iniziale per cui il [limite](content/Matematica/Analisi%20matematica/Limiti/_index.md#^definizione-limite) $\displaystyle\lim_{x \to x_0} g(x)$ non esiste.

### Principio di eliminazione dei termini trascurabili (PETT)

> [!teorema] Principio di eliminazione dei termini trascurabili (PETT)
> 
> Date quattro [funzioni](content/Matematica/Teoria%20degli%20insiemi/Funzioni/_index.md#^definizione-funzione) $f,g,f',g' \colon A \subseteq \mathbb{R} \to \mathbb{R}$ (con $A \ne \emptyset$) e un [punto di accumulazione](Topologia%20dei%20reali.md#^definizione-punto-di-accumulazione) $x_0 \in \mathbb{R} \cup \{ \pm \infty \}$ per $A$, abbiamo che se $f'$ è [$o$-piccolo](Infiniti%20e%20infinitesimi.md#^definizione-o-piccolo) di $f$ per $x \to x_0$ e $g'$ è [$o$-piccolo](Infiniti%20e%20infinitesimi.md#^definizione-o-piccolo) di $g$ per $x \to x_0$, allora $f'$ e $g'$ sono [trascurabili](Infiniti%20e%20infinitesimi.md#^definizione-trascurabilita-di-una-funzione) nella rispettiva somma con $f$ e $g$:
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

> [!osservazione] Osservazione: riformulazione del PETT
> 
> Il [principio di eliminazione dei termini trascurabili (PETT)](Infiniti%20e%20infinitesimi.md#^principio-di-eliminazione-dei-termini-trascurabili) può essere riformulato anche come
> 
> $$
> \lim_{x \to x_0} \dfrac{f(x) + o(f(x))}{g(x) + o(g(x))} = \lim_{x \to x_0} \dfrac{f(x)}{g(x)}
> $$

> [!osservazione] Osservazione: PETT per solo numeratore o denominatore
> 
> Il [principio di eliminazione dei termini trascurabili (PETT)](Infiniti%20e%20infinitesimi.md#^principio-di-eliminazione-dei-termini-trascurabili) può essere utilizzato anche se la [funzione trascurabile](Infiniti%20e%20infinitesimi.md#^definizione-trascurabilita-di-una-funzione) è presente solo al numeratore%% Link %% o al denominatore%% link %%. Più precisamente,
> 
> $$
> \lim_{x \to x_0} \dfrac{f(x) + o(f(x))}{g(x)} = \lim_{x \to x_0} \dfrac{f(x)}{g(x) + o(g(x))} = \lim_{x \to x_0} \dfrac{f(x)}{g(x)}
> $$

%% 
osservazioni c, d pagina 194 lancelotti
%%

> [!esempio] Esempio di uso del PETT
> 
> Calcoliamo il [limite](content/Matematica/Analisi%20matematica/Limiti/_index.md#^definizione-limite)
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

## Equivalenza asintotica

> [!definizione] Definizione: equivalenza asintotica
> 
> Date due [funzioni](content/Matematica/Teoria%20degli%20insiemi/Funzioni/_index.md#^definizione-funzione) $f,g \colon A \subseteq \mathbb{R} \to \mathbb{R}$ (con $A \ne \emptyset$) e un [punto di accumulazione](Topologia%20dei%20reali.md#^definizione-punto-di-accumulazione) $x_0 \in \mathbb{R} \cup \{ \pm \infty \}$ per $A$, diciamo che **$f$ è equivalente a $g$ per $x$ che tende a $x_0$ se**
> 
> $$
> \lim_{x \to x_0} \dfrac{f(x)}{g(x)} = 1
> $$
> 
> e in tal caso scriviamo "$f \sim g$ per $x \to x_0$" (oppure "$f(x) \sim g(x)$ per $x \to x_0$").
^definizione-equivalenza-asintotica

> [!osservazione] Osservazione: nell'equivalenza asintotica $g$ non identicamente nulla
> 
> Esattamente [come avviene per l'$o$-piccolo](Infiniti%20e%20infinitesimi.md#^osservazione-nell-o-piccolo-g-non-identicamente-nulla), anche per l'[equivalenza asintotica](Infiniti%20e%20infinitesimi.md#^definizione-equivalenza-asintotica) serve che la [funzione](content/Matematica/Teoria%20degli%20insiemi/Funzioni/_index.md#^definizione-funzione) $g$ non sia [identicamente nulla](content/Matematica/Teoria%20degli%20insiemi/Funzioni/_index.md#^definizione-funzione-identicamente-nulla) in ogni [intorno bucato](Topologia%20dei%20reali.md#^definizione-intorno-bucato-di-un-punto) $I(x_0)$ di $x_0$ [intersecato](content/Matematica/Teoria%20degli%20insiemi/_index.md#^definizione-intersezione-di-due-insiemi) con $A$ affinché il [limite](content/Matematica/Analisi%20matematica/Limiti/_index.md#^definizione-limite) dell'[equivalenza asintotica](Infiniti%20e%20infinitesimi.md#^definizione-equivalenza-asintotica) sia ben definito:
> 
> $$
> \begin{array}{}
> f \sim g \text{ per } x \to x_0 \\
> \Downarrow \\
> g \text{ non identicamente nulla per ogni } (I(x_0) \cap A) \setminus \{ x_0 \}
> \end{array}
> $$
^osservazione-nell-equivalenza-asintotica-g-non-identicamente-nulla

> [!proposizione] Proposizione: nell'equivalenza asintotica $f$ non identicamente nulla
> 
> Se una [funzione](content/Matematica/Teoria%20degli%20insiemi/Funzioni/_index.md#^definizione-funzione) $f$ è [equivalente](Infiniti%20e%20infinitesimi.md#^definizione-equivalenza-asintotica) a un'altra [funzione](content/Matematica/Teoria%20degli%20insiemi/Funzioni/_index.md#^definizione-funzione) $g$ per $x \to x_0$, allora anche $f$ non è [identicamente nulla](content/Matematica/Teoria%20degli%20insiemi/Funzioni/_index.md#^definizione-funzione-identicamente-nulla) in ogni [intorno bucato](Topologia%20dei%20reali.md#^definizione-intorno-bucato-di-un-punto) $I(x_0)$ di $x_0$ [intersecato](content/Matematica/Teoria%20degli%20insiemi/_index.md#^definizione-intersezione-di-due-insiemi) con $A$:
> 
> $$
> \begin{array}{}
> f \sim g \text{ per } x \to x_0 \\
> \Downarrow \\
> f \text{ non identicamente nulla per ogni } (I(x_0) \cap A) \setminus \{ x_0 \}
> \end{array}
> $$
> 
> > [!dimostrazione] Dimostrazione
> > 
> > Per il [teorema della permanenza del segno](Proprietà%20locali%20dei%20limiti.md#^teorema-della-permanenza-del-segno) esiste un [intorno](Topologia%20dei%20reali.md#^definizione-intorno-di-un-punto) $I(x_0)$ di $x_0$ tale che
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
> > Avendo $f(x) \ne 0$, possiamo assumere che ovunque $g$ non è [identicamente nulla](content/Matematica/Teoria%20degli%20insiemi/Funzioni/_index.md#^definizione-funzione-identicamente-nulla), non lo sarà neanche $f$.
> > 
> > $\blacksquare$
^proposizione-nell-equivalenza-asintotica-f-non-identicamente-nulla

> [!esempio] Esempio: $\sin x \sim x$ per $x \to 0$
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

> [!esempio] Esempio: $1 - \cos x \sim \dfrac{1}{2} x^2$ per $x \to 0$
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
[!esempio] Esempio: $\tan x \sim x$ per $x \to 0$

[!esempio] Esempio: $\arctan \sim x$ per $x \to 0$
%%

> [!esempio] Esempio: $P(x) \sim a_nx^n$ per $x \to \pm \infty$
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
[!esempio] Esempio: $x^2 - 3x + 2 \sim x^2 + 12x - 7$ per $x \to \pm \infty$
%%

%% 
per questi ultimi due esempi possiamo dire che il PETT si può applicare sui polinomi
%%

### Proprietà dell'equivalenza asintotica

> [!proprieta] Proprietà: riflessività dell'equivalenza asintotica
> 
> Una [funzione](content/Matematica/Teoria%20degli%20insiemi/Funzioni/_index.md#^definizione-funzione) $f$ è sempre [equivalente](Infiniti%20e%20infinitesimi.md#^definizione-equivalenza-asintotica) a se stessa per $x \to x_0$, cioè l'[equivalenza asintotica](Infiniti%20e%20infinitesimi.md#^definizione-equivalenza-asintotica) gode della proprietà riflessiva%% link %%:
> 
> $$
> f \sim f \text{ per } x \to x_0
> $$
> 
> > [!dimostrazione] Dimostrazione
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

> [!proprieta] Proprietà: simmetria dell'equivalenza asintotica
> 
> Date due [funzioni](content/Matematica/Teoria%20degli%20insiemi/Funzioni/_index.md#^definizione-funzione) $f$ e $g$, si ha che se $f$ è [equivalente](Infiniti%20e%20infinitesimi.md#^definizione-equivalenza-asintotica) a $g$ per $x \to x_0$, allora anche $g$ è [equivalente](Infiniti%20e%20infinitesimi.md#^definizione-equivalenza-asintotica) a $f$ per $x \to x_0$, cioè l'[equivalenza asintotica](Infiniti%20e%20infinitesimi.md#^definizione-equivalenza-asintotica) gode della proprietà simmetrica%% link %%:
> 
> $$
> \forall f, g . \left( 
> \begin{array}{}
> f \sim g \text{ per } x \to x_0 \\
> \Updownarrow \\
> g \sim f \text{ per } x \to x_0
> \end{array}
> \right)  
> $$
> 
> > [!dimostrazione] Dimostrazione
> > 
> > Per [definizione di _equivalenza asintotica_](Infiniti%20e%20infinitesimi.md#^definizione-equivalenza-asintotica), dobbiamo dimostrare che
> > 
> > $$
> > \forall f, g . \left( 
> > \begin{array}{}
> > \displaystyle\lim_{x \to x_0} \dfrac{f(x)}{g(x)} = 1 \\
> > \Updownarrow \\
> > \displaystyle\lim_{x \to x_0} \dfrac{g(x)}{f(x)} = 1
> > \end{array}
> > \right)
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

> [!proposizione] Proposizione: limiti di due funzioni equivalenti
> 
> Se una [funzione](content/Matematica/Teoria%20degli%20insiemi/Funzioni/_index.md#^definizione-funzione) $f$ è [equivalente](Infiniti%20e%20infinitesimi.md#^definizione-equivalenza-asintotica) a un'altra [funzione](content/Matematica/Teoria%20degli%20insiemi/Funzioni/_index.md#^definizione-funzione) $g$ per $x \to x_0$ e se esiste il [limite](content/Matematica/Analisi%20matematica/Limiti/_index.md#^definizione-limite) di $f(x)$ per $x \to x_0$, allora esiste il [limite](content/Matematica/Analisi%20matematica/Limiti/_index.md#^definizione-limite) di $g(x)$ per $x \to x_0$ ed è uguale a $l$:
> 
> $$
> \forall f, g . \left( 
> \begin{array}{}
> f \sim g \text{ per } x \to x_0 \\
> \land \\
> \displaystyle\lim_{x \to x_0} f(x) = l \in \mathbb{R} \cup \{ \pm \infty \}
> \end{array}
> \implies
> \displaystyle\lim_{x \to x_0} g(x) = l
> \right) 
> $$

%% 
dimostrazione pag. 197 lancelotti
%%

> [!proposizione] Proposizione: relazione tra l'equivalenza asintotica e l'$o$-piccolo
> 
> Si ha che una [funzione](content/Matematica/Teoria%20degli%20insiemi/Funzioni/_index.md#^definizione-funzione) $f$ è [equivalente](Infiniti%20e%20infinitesimi.md#^definizione-equivalenza-asintotica) a un'altra [funzione](content/Matematica/Teoria%20degli%20insiemi/Funzioni/_index.md#^definizione-funzione) $g$ per $x \to x_0$ se e solo se $f$ è [$o$-piccolo](Infiniti%20e%20infinitesimi.md#^definizione-o-piccolo) di $g + o(g)$ per $x \to x_0$:
> 
> $$
> \forall f,g . \left( 
> \begin{array}{}
> f \sim g \text{ per } x \to x_0 \\
> \Updownarrow \\
> f = g + o(g) \text{ per } x \to x_0
> \end{array}
> \right)
> $$
^proposizione-relazione-tra-l-equivalenza-asintotica-e-l-o-piccolo

%% 
dimostrazione
%%

---

> [!fonti]+ Fonti
> 
> - 📚 _Lezioni di Analisi Matematica I_ di Sergio Lancelotti, Celid, 2020 (ISBN: `978-8867891979`):
> 	- Capitolo 3 - _Limiti e continuità_:
> 		- 4 - _Confronto locale fra funzioni_:
> 			- 4.1 - _Infiniti e infinitesimi_.
> 			- 4.2 - _Simboli di Landau_.
