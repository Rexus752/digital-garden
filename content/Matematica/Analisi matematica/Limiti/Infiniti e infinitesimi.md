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
> Data una [funzione](Matematica/Teoria%20degli%20insiemi/Funzioni/_index.md#^definizione-funzione) $f \colon \text{dom}(f) \to \mathbb{R}$ e un [punto di accumulazione](Topologia%20dei%20reali.md#^definizione-punto-di-accumulazione) $x_0 \in \mathbb{R} \cup \{ \pm \infty \}$ per $\text{dom}(f)$, se in ogni [intorno](Topologia%20dei%20reali.md#^definizione-intorno-di-un-punto) $I(x_0)$ di $x_0$ esiste un $x \in \text{dom}(f) \setminus \{ x_0 \}$ tale che $f(x) \ne 0$, allora $f$ è un [infinitesimo](Infiniti%20e%20infinitesimi.md#^definizione-infinito-e-infinitesimo) in $x_0$ se e solo se $\dfrac{1}{f}$ è un [infinito](Infiniti%20e%20infinitesimi.md#^definizione-infinito-e-infinitesimo) in $x_0$.
^proposizione-rapporto-tra-infiniti-e-infinitesimi

%%
[!dimostrazione] Dimostrazione

Per esercizio
%%

# Simboli di Landau

Introduciamo ora delle nozioni che ci permettono di confrontare localmente%% link %% le [funzioni](content/Matematica/Teoria%20degli%20insiemi/Funzioni/_index.md#^definizione-funzione), cioè in un [intorno](Topologia%20dei%20reali.md#^definizione-intorno-di-un-punto) di un punto%% Link %%. Poiché la nozione locale più generale che conosciamo è quella del [_limite_](content/Matematica/Analisi%20matematica/Limiti/_index.md#^definizione-limite), tutte queste nozioni che introdurremo si baseranno su di essa, anzi non saranno altro che un modo diverso di scrivere l'operazione%% link %% di [limite](content/Matematica/Analisi%20matematica/Limiti/_index.md#^definizione-limite).

> [!definizione] Definizione: $o$-piccolo
> 
> Date due [funzioni](content/Matematica/Teoria%20degli%20insiemi/Funzioni/_index.md#^definizione-funzione) $f,g \colon A \subseteq \mathbb{R} \to \mathbb{R}$ (con $A \ne \emptyset$) e un [punto di accumulazione](Topologia%20dei%20reali.md#^definizione-punto-di-accumulazione) $x_0 \in \mathbb{R} \cup \{ \pm \infty \}$ per $A$, diciamo che **$f$ è $o$-piccolo di $g$ per $x$ che tende a $x_0$** se
> 
> $$
> \lim_{x \to x_0} \dfrac{f(x)}{g(x)} = 0
> $$
> 
> e in tal caso scriviamo $f = o(g)$ per $x \to x_0$ (oppure $f(x) = o(g(x))$ per $x \to x_0$).
^definizione-o-piccolo

%% 
Evidentemente la [funzione](content/Matematica/Teoria%20degli%20insiemi/Funzioni/_index.md#^definizione-funzione) $g$ non è identicamente nulla in ogni [intorno](Topologia%20dei%20reali.md#^definizione-intorno-di-un-punto) di $x_0$ intersecato con $A$ escluso $x_0$.
%%

> [!esempio] Esempio di $o$-piccolo con $x$ e $x^2$
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

> [!esempio] Esempio di $o$-piccolo con $\sin x$ e $\sqrt x$
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

> [!esempio] Esempio di $o$-piccolo con $x^p$ e $x^q$ con $0 < p < q$
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
^proposizione-o-piccolo-di-se-stesso


---

> [!fonti]+ Fonti
> 
> - 📚 _Lezioni di Analisi Matematica I_ di Sergio Lancelotti, Celid, 2020 (ISBN: `978-8867891979`):
> 	- Capitolo 3 - _Limiti e continuità_:
> 		- 4 - _Confronto locale fra funzioni_:
> 			- 4.1 - _Infiniti e infinitesimi_.
> 			- 4.2 - _Simboli di Landau_.
