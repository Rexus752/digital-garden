---
title: Proprietà locali delle funzioni continue
---

> [!premessa]+ Premessa
> 
> Ciao! Se è la prima volta che capiti su questo sito, ti consiglio di consultare la [pagina principale](index.md) di questo cosiddetto _Giardino Digitale_ per scoprire meglio cos'è e come navigarlo.
> 
> Lo stato di questa nota è al momento: 🔴 <font color="#FF7F7F">_Bozza_</font>.

---

%% 
vedere se questa pagina si può ficcare in [Asintoti verticali e orizzontali](Asintoti%20verticali%20e%20orizzontali.md) o [Limiti](Matematica/Analisi%20matematica/Limiti/_index.md)
%%

> [!teorema]+ Teorema di limitatezza locale
> 
> Data una [funzione](Matematica/Teoria%20degli%20insiemi/Funzioni/_index.md#^definizione-funzione) $f \colon \text{dom}(f) \to \mathbb{R}$ e un [punto di accumulazione](Topologia%20dei%20reali.md#^definizione-punto-di-accumulazione) $x_0 \in \mathbb{R} \cup \{ \pm \infty \}$ per $\text{dom}(f)$, se esiste un [limite](Matematica/Analisi%20matematica/Limiti/_index.md#^definizione-limite)
> 
> $$
> \lim_{x \to x_0} f(x) = l \in \mathbb{R}
> $$
> 
> allora esiste un [intorno](Topologia%20dei%20reali.md#^definizione-intorno-di-un-punto) $I(x_0)$ di $x_0$ tale che $f$ è limitata%% link %% su $(\text{dom}(f) \cap I(x_0)) \setminus \{ x_0 \}$.
^teorema-di-limitatezza-locale

%% 
dimostrazione pag. 156 lancelotti
%%

%% 
osservazioni 3.2 pag. 156 lancelotti
%%

> [!teorema]+ Teorema della permanenza del segno
> 
> Data una [funzione](Matematica/Teoria%20degli%20insiemi/Funzioni/_index.md#^definizione-funzione) $f \colon \text{dom}(f) \to \mathbb{R}$ e un [punto di accumulazione](Topologia%20dei%20reali.md#^definizione-punto-di-accumulazione) $x_0 \in \mathbb{R} \cup \{ \pm \infty \}$ per $\text{dom}(f)$, se esiste un [limite](Matematica/Analisi%20matematica/Limiti/_index.md#^definizione-limite)
> 
> $$
> \lim_{x \to x_0} f(x) = l \in \mathbb{R} \cup \{ \pm \infty \}
> $$
> 
> allora:
> - Se $l > 0$ oppure $l = +\infty$ allora esiste un [intorno](Topologia%20dei%20reali.md#^definizione-intorno-di-un-punto) $I(x_0)$ di $x_0$ tale che $f(x) > 0$ per ogni $x \in (\text{dom}(f) \cap I(x_0)) \setminus \{ x_0 \}$.
> - Se $l < 0$ oppure $l = -\infty$ allora esiste un [intorno](Topologia%20dei%20reali.md#^definizione-intorno-di-un-punto) $I(x_0)$ di $x_0$ tale che $f(x) < 0$ per ogni $x \in (\text{dom}(f) \cap I(x_0)) \setminus \{ x_0 \}$.
^teorema-della-permanenza-del-segno

%% 
dimostrazione pag. 157 lancelotti
%%

%% 
osservazioni 3.4 pag. 157 lancelotti
%%

> [!corollario]+ Corollario del teorema della permanenza del segno
> 
> Data una [funzione](Matematica/Teoria%20degli%20insiemi/Funzioni/_index.md#^definizione-funzione) $f \colon \text{dom}(f) \to \mathbb{R}$ e un [punto di accumulazione](Topologia%20dei%20reali.md#^definizione-punto-di-accumulazione) $x_0 \in \mathbb{R} \cup \{ \pm \infty \}$ per $\text{dom}(f)$, se esiste un [limite](Matematica/Analisi%20matematica/Limiti/_index.md#^definizione-limite)
> 
>  $$
> \lim_{x \to x_0} f(x) = l \in \mathbb{R}
> $$
> 
> e un [intorno](Topologia%20dei%20reali.md#^definizione-intorno-di-un-punto) $I(x_0)$ di $x_0$ tale che $f(x) \ge 0$ (alternativamente $f(x) \le 0$) per ogni $x \in (\text{dom}(f) \cap I(x_0)) \setminus \{ x_0 \}$, allora $l \ge 0$ (alternativamente $l \le 0$).
^corollario-del-teorema-della-permanenza-del-segno

%% 
dimostrazione pag. 157 lancelotti
%%

%% 
osservazione 3.6 pag. 158 lancelotti
%%

---

> [!fonti]+ Fonti
> 
> - 📚 _Lezioni di Analisi Matematica I_ di Sergio Lancelotti, Celid, 2020 (ISBN: `978-8867891979`):
> 	- Capitolo 3 - _Limiti e continuità_:
> 		- 3 - _Teoremi su limiti e continuità_:
> 			- 3.1 - _Proprietà locali_.
