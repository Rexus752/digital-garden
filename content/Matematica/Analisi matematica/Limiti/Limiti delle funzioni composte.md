
> [!premessa]+ Premessa
> 
> Ciao! Se è la prima volta che capiti su questo sito, ti consiglio di consultare la [pagina principale](index.md) di questo cosiddetto _Giardino Digitale_ per scoprire meglio cos'è e come navigarlo.
> 
> Lo stato di questa nota è al momento: 🔴 <font color="#FF7F7F">_Bozza_</font>.

---

%% 
Nei paragrafi precedenti abbiamo studiato l'algebra delle funzioni continue e quella dei limiti. Per questi ultimi ci siamo occupati della somma, del prodotto e del quoziente. Resta da analizzare cosa succede nel caso dell composizione. Come vedremo, la situazione è meno ovvia del previsto, a differenz di quello che succede nella composizione di funzioni continue.

resto dell'introduzione a pag. 178-179
%%

> [!teorema]+ Teorema del limite della funzione composta
> 
> Date due [funzioni](Matematica/Teoria%20degli%20insiemi/Funzioni/Funzioni.md#^definizione-funzione) $f \colon \text{dom}(f) \to \mathbb{R}$ e $g \colon \text{dom}(g) \to \mathbb{R}$ con $\text{rng}(f) \subseteq \text{dom}(g)$ e un [punto di accumulazione](Topologia%20dei%20reali.md#^definizione-punto-di-accumulazione) $x_0 \in \mathbb{R} \cup \{ \pm \infty \}$ per $\text{dom}(f)$:
> 1. se esiste il [limite](Limiti.md#^definizione-limite) $\displaystyle\lim_{x \to x_0} f(x) = y_0 \in \mathbb{R} \cup \{ \pm \infty \}$ e $y_0$ è un [punto di accumulazione](Topologia%20dei%20reali.md#^definizione-punto-di-accumulazione) per $\text{dom}(g)$,
> 2. se $y_0 \in \mathbb{R}$, supponiamo che $y_0 \in \text{dom}(g)$ e che $g$ sia [continua](Funzioni%20continue.md#^definizione-funzione-continua) in $y_0$ con $g(y_0) = l \in \mathbb{R}$ e
> 3. se $y_0 = \pm \infty$, supponiamo che esista il [limite](Limiti.md#^definizione-limite) $\displaystyle\lim_{y \to y_0} g(y) = l \in \mathbb{R} \cup \{ \pm \infty \}$,
> 
> allora
> 
> $$
> \lim_{x \to x_0} (g \circ f)(x) = l
> $$
^teorema-del-limite-della-funzione-composta

%% 
dimostrazione pag. 179 lancelotti
%%

%% 
esempi pagg. 180-181 lancelotti
%%

> [!teorema]+ Teorema del limite della funzione composta continua
> 
> Date due [funzioni](Matematica/Teoria%20degli%20insiemi/Funzioni/Funzioni.md#^definizione-funzione)
> 
> $$
> \begin{array}{}
> f \colon \text{dom}(f) \to \mathbb{R} \\
> g \colon \text{dom}(g) \to \mathbb{R}
> \end{array}
> $$
> 
> con $\text{rng}(f) \subseteq \text{dom}(g)$ e un [punto di accumulazione](Topologia%20dei%20reali.md#^definizione-punto-di-accumulazione) $x_0 \in \mathbb{R} \cup \{ \pm \infty \}$ per $\text{dom}(f)$:
> 1. se esiste il [limite](Limiti.md#^definizione-limite) $\displaystyle\lim_{x \to x_0} f(x) = y_0 \in \mathbb{R} \cup \{ \pm \infty \}$ e $y_0$ è un [punto di accumulazione](Topologia%20dei%20reali.md#^definizione-punto-di-accumulazione) per $\text{dom}(g)$,
> 2. se esiste il [limite](Limiti.md#^definizione-limite) $\displaystyle\lim_{x \to x_0} g(y) = l \in \mathbb{R} \cup \{ \pm \infty \}$ e
> 3. se esiste un [intorno](Topologia%20dei%20reali.md#^definizione-intorno-di-un-punto) $I(x_0)$ di $x_0$ tale che $f(x) \ne y_0$ per ogni $x \in (\text{dom}(f) \cap I(x_0)= \setminus \{ x_0 \}$,
> 
> allora
> 
> $$
> \lim_{x \to x_0} (g \circ f)(x) = l
> $$
^teorema-del-limite-della-funzione-composta-continua

%% va bene chiamarlo così questo teorema per distinguerlo dall'altro? %%

%% dimostrazioen pag. 181 lancelotti %%

%% osservazioni pag. 181-182 lancelotti %%

%% esempi pagg. 182-183 lancelotti %%

> [!proposizione]+ Proposizione: limiti di funzioni pari o dispari
> 
> Data una [funzione pari (o dispari)](Matematica/Teoria%20degli%20insiemi/Funzioni/Proprietà%20delle%20funzioni.md#^definizione-funzioni-pari-e-dispari) $f \colon \text{dom}(f) \to \mathbb{R}$ e un [punto di accumulazione](Topologia%20dei%20reali.md#^definizione-punto-di-accumulazione) $x_0 \in \mathbb{R} \cup \{ \pm \infty \}$ per $\text{dom}(f)$, allora si ha che
> 
> $$
> \begin{array}{}
> \displaystyle f \text{ pari} \implies \lim_{x \to -x_0} f(x) = \lim_{x \to x_0} f(x) \\
> \displaystyle f \text{ dispari} \implies \lim_{x \to -x_0} f(x) = - \lim_{x \to x_0} f(x)
> \end{array}
> $$
^proposizione-limiti-di-funzioni-pari-o-dispari

%% questa proposizione va qui? %%

%% dimostrazione pag. 183 lancelotti %%

> [!proposizione]+ Proposizione: continuità della funzione composta
> 
>  Date due [funzioni](Matematica/Teoria%20degli%20insiemi/Funzioni/Funzioni.md#^definizione-funzione) $f \colon \text{dom}(f) \to \mathbb{R}$ e $g \colon \text{dom}(g) \to \mathbb{R}$ con $\text{rng}(f) \subseteq \text{dom}(g)$ e un [punto di accumulazione](Topologia%20dei%20reali.md#^definizione-punto-di-accumulazione) $x_0 \in \mathbb{R} \cup \{ \pm \infty \}$ per $\text{dom}(f)$, se $f$ è [continua](Funzioni%20continue.md#^definizione-funzione-continua-in-un-punto) in $x_0$ e $g$ è [continua](Funzioni%20continue.md#^definizione-funzione-continua-in-un-punto) in $f(x_0)$, allora la loro [composizione](Composizione%20di%20funzioni.md#^definizione-composizione-di-due-funzioni) $f \circ g$ è anch'essa [continua](Funzioni%20continue.md#^definizione-funzione-continua-in-un-punto) in $x_0$.
^proposizione-continuita-della-funzione-composta

%% 
ed è continua nell'intervallo dato dall'intersezione degli intervalli di continuità delle due funzioni
%%

> [!esempio]- Esempio di continuità della funzione composta
> 
> - $\sin x^2 = \sin x \circ x^2$ è continua su $\mathbb{R}$ perché sia $\sin x$ che $x^2$ sono continue in $\mathbb{R}$
> - $\sqrt{\cos x} = \sqrt x \circ \cos x$ è continua su $\displaystyle\bigcup_{k \in \mathbb{N}} \left[ - \dfrac{\pi}{2} + 2k\pi, \dfrac{\pi}{2} + 2k\pi \right]$ perché $\sqrt x$ è continua su $[0, + \infty)$ e $\cos x$ su $\displaystyle\bigcup_{k \in \mathbb{N}} \left[ - \dfrac{\pi}{2} + 2k\pi, \dfrac{\pi}{2} + 2k\pi \right]$:
> 	- $[0, + \infty) \cap \mathbb{R} = [0, + \infty)$
> - $\sin(e^{x^2} + \sqrt{\cos x})$:
> 	- $\sqrt{\cos x}$ è continua su $\displaystyle\bigcup_{k \in \mathbb{N}} \left[ - \dfrac{\pi}{2} + 2k\pi, \dfrac{\pi}{2} + 2k\pi \right]$
> 	- $e^{x^2}$ è continua su $\mathbb{R}$
> 	- $\sin x$ è continua su $\mathbb{R}$
> 	- la funzione è continua su $\displaystyle\bigcup_{k \in \mathbb{N}} \left[ - \dfrac{\pi}{2} + 2k\pi, \dfrac{\pi}{2} + 2k\pi \right]$

---

> [!fonti]+ Fonti
> 
> - 🏫 Corso di Laurea in Informatica (`L-31 R`) presso l'Università di Torino:
> 	- Corso di _Analisi Matematica - canale C_, A.A. 2020-21 ([pagina Moodle](https://informatica.i-learn.unito.it/course/view.php?id=2075)):
> 		- Prof. Barutello Vivina Laura, videolezioni:
> 			- [_L9a_](https://informatica.i-learn.unito.it/local/streamingfilemanager/file.php/informatica.i-learn.unito.it/2075/L9a.mp4).
> - 📚 Sergio Lancelotti, _Lezioni di Analisi Matematica I_, Celid, 2020 (ISBN: `978-8867891979`):
> 	- Capitolo 3 - _Limiti e continuità_:
> 		- 2 - _Limiti di funzioni_:
> 			- 2.2 - _Limiti laterali_.
> 	- Capitolo 3 - _Limiti e continuità_:
> 		- 3 - _Teoremi su limiti e continuità_:
> 			- 3.7 - _Limiti delle funzioni composte_.
