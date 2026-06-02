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

# Limiti notevoli del seno

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

> [!proposizione] Proposizione: limite notevole del seno tendente all'infinito
> 
> Vale il seguente [limite notevole](content/Matematica/Analisi%20matematica/Limiti/_index.md#^definizione-limite-notevole):
> 
> $$
> \lim_{x \to \pm \infty} \dfrac{\sin x}{x} = 0
> $$
^proposizione-limite-notevole-del-seno-tendente-all-infinito

%% dimostrazione pag. 174 lancelotti %%

# Limiti notevoli del coseno

> [!proposizione] Proposizione: limite notevole del coseno tendente a $0$
> 
> Vale il seguente [limite notevole](content/Matematica/Analisi%20matematica/Limiti/_index.md#^definizione-limite-notevole):
> 
> $$
> \lim_{x \to 0} \dfrac{1 - \cos x}{x^2} = \dfrac{1}{2}
> $$
^proposizione-limite-notevole-del-coseno-tendente-a-0

%% dimostrazione pag. 173 lancelotti %%

> [!proposizione] Proposizione: limite notevole del coseno tendente all'infinito
> 
> Vale il seguente [limite notevole](content/Matematica/Analisi%20matematica/Limiti/_index.md#^definizione-limite-notevole):
> 
> $$
> \lim_{x \to \pm \infty} \dfrac{\cos x}{x} = 0
> $$
^proposizione-limite-notevole-del-coseno-tendente-all-infinito

%% dimostrazione pag. 174 lancelotti %%

# Limiti notevoli della tangente

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

# Forme indeterminate esponenziali

[!osservazione] Osservazione: forma alternativa delle forme indeterminate esponenziali

Per le [forme indeterminate esponenziali](Forme%20indeterminate.md#^definizione-forma-indeterminata-esponenziale) abbiamo che

---

> [!fonti]+ Fonti
> 
> - 📚 _Lezioni di Analisi Matematica I_ di Sergio Lancelotti, Celid, 2020 (ISBN: `978-8867891979`):
> 	- Capitolo 3 - _Limiti e continuità_:
> 		- 3 - _Teoremi su limiti e continuità_:
> 			- 3.5 - _Teoremi del confronto_.
> 			- 3.8 - _Limiti notevoli_.
