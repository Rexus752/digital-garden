---
title: Asintoti verticali e orizzontali
---

> [!premessa]+ Premessa
> 
> Ciao! Se è la prima volta che capiti su questo sito, ti consiglio di consultare la [pagina principale](index.md) di questo cosiddetto _Giardino Digitale_ per scoprire meglio cos'è e come navigarlo.
> 
> Lo stato di questa nota è al momento: 🔴 <font color="#FF7F7F">_Bozza_</font>.

---

# 1 - Asintoti verticali

> [!definizione]+ Definizione: asintoto verticale
> 
> Data una [funzione](Matematica/Teoria%20degli%20insiemi/Funzioni/_index.md#^definizione-funzione) $f \colon \text{dom}(f) \to \mathbb{R}$ e un [punto di accumulazione](Topologia%20dei%20reali.md#^definizione-punto-di-accumulazione) $x_0 \in \mathbb{R}$ per $\text{dom}(f) \cap (x_0, + \infty)$, se
> 
> $$
> \lim_{x \to x_0^+} f(x) = \pm \infty
> $$
> 
> allora la retta%% link %% $x = x_0$ è un **asintoto verticale destro per $f$**.
> 
> Data una [funzione](Matematica/Teoria%20degli%20insiemi/Funzioni/_index.md#^definizione-funzione) $f \colon \text{dom}(f) \to \mathbb{R}$ e un [punto di accumulazione](Topologia%20dei%20reali.md#^definizione-punto-di-accumulazione) $x_0 \in \mathbb{R}$ per $\text{dom}(f) \cap (-\infty, x_0)$, se
> 
> $$
> \lim_{x \to x_0^-} f(x) = \pm \infty
> $$
> 
> allora la retta%% link %% $x = x_0$ è un **asintoto verticale sinistro per $f$**.
> 
> Se la retta%% link %% $x = x_0$ è contemporaneamente un asintoto verticale destro e sinistro per $f$, allora è un **asintoto verticale per $f$**.
^definizione-asintoto-verticale

%% 
esempio pag. 148 lancelotti
%%

> [!osservazione]+ Osservazione: asintoti verticali dal punto di vista grafico
> 
> Graficamente, se la retta%% link %% $x = x_0$ è un [asintoto verticale destro/sinistro](Asintoti%20verticali%20e%20orizzontali.md#^definizione-asintoto-verticale) per $f$, allora il grafico%% link %% di $f$ si avvicina sempre più a questa retta per $x$ che tende a $x_0$ da destra/sinistra, senza però mai attraversarlo (cioè senza poter andare "dall'altro lato" rispetto a $x = x_0$).
> 
> Nonostante ciò, il grafico%% link %% di $f$ e l'[asintoto](Asintoti%20verticali%20e%20orizzontali.md#^definizione-asintoto-verticale) possono avere uno e un solo punto%% link %% in comune, ossia $x_0$.

> [!osservazione]+ Osservazione: multipli asintoti verticali per una stessa funzione
> 
> Una stessa [funzione](Matematica/Teoria%20degli%20insiemi/Funzioni/_index.md#^definizione-funzione) $f$ può avere anche più di un [asintoto verticale](Asintoti%20verticali%20e%20orizzontali.md#^definizione-asintoto-verticale): per esempio, la [funzione](Matematica/Teoria%20degli%20insiemi/Funzioni/_index.md#^definizione-funzione) $f(x) = \tan x$ ammette infiniti [asintoti verticali](Asintoti%20verticali%20e%20orizzontali.md#^definizione-asintoto-verticale) di equazione
> 
> $$
> \forall k \in \mathbb{Z} \left( x = \dfrac{\pi}{2} + k\pi \right) 
> $$

> [!attenzione]+ Attenzione: si può parlare di asintoti verticali solo con valori reali
> 
> Data una [funzione](Matematica/Teoria%20degli%20insiemi/Funzioni/_index.md#^definizione-funzione) $f$, se
> 
> $$
> \lim_{x \to \pm \infty} f(x) = \pm \infty
> $$
> 
> allora **non** si può parlare di [asintoti verticali](Asintoti%20verticali%20e%20orizzontali.md#^definizione-asintoto-verticale) perché, per definizione, un asintoto verticale si presenta al tendersi di $x$ verso un determinato punto%% link %% $x_0 \in \mathbb{R}$, mentre $\pm \infty \not\in \mathbb{R}$.

# 2 - Asintoti orizzontali

> [!definizione]+ Definizione: asintoto orizzontale
> 
> Data una [funzione](Matematica/Teoria%20degli%20insiemi/Funzioni/_index.md#^definizione-funzione) $f \colon \text{dom}(f) \to \mathbb{R}$ con $\text{dom}(f)$ illimitato superiormente%% link %%, se
> 
> $$
> \lim_{x \to + \infty} f(x) = l \in \mathbb{R}
> $$
> 
> allora la retta%% link %% $y = l$ è un **asintoto orizzontale destro per $f$**.
> 
> Data una [funzione](Matematica/Teoria%20degli%20insiemi/Funzioni/_index.md#^definizione-funzione) $f \colon \text{dom}(f) \to \mathbb{R}$ con $\text{dom}(f)$ illimitato superiormente%% link %%, se
> 
> $$
> \lim_{x \to - \infty} f(x) = l \in \mathbb{R}
> $$
> 
> allora la retta%% link %% $y = l$ è un **asintoto orizzontale sinistro per $f$**.
> 
> Se la retta%% link %% $y = l$ è contemporaneamente un asintoto orizzontale destro e sinistro per $f$, allora è un **asintoto orizzontale per $f$**.
^definizione-asintoto-orizzontale

%% 
esempi pag. 149 lancelotti
%%

> [!osservazione]+ Osservazione: asintoti orizzontali dal punto di vista grafico
> 
> Graficamente, se la retta%% link %% $y = l$ è un [asintoto orizzontale destro/sinistro](Asintoti%20verticali%20e%20orizzontali.md#^definizione-asintoto-orizzontale) per $f$, allora il grafico%% link %% di $f$ si avvicina sempre più a questa retta per $x$ che tende a $\pm \infty$ e può anche attraversarlo (cioè può andare "dall'altro lato" rispetto a $y = l$, l'importante è che, per $x \to \pm \infty$, si abbia che $f(x) \to l$).

%% 
**Esempio:** $f(x) = \dfrac{\sin x}{x}$​ ha asintoto orizzontale y=0y = 0 y=0, ma attraversa l'asse xx x infinite volte.
%%

> [!osservazione]+ Osservazione: un asintoto orizzontale destro/sinistro per funzione
> 
> Una [funzione](Matematica/Teoria%20degli%20insiemi/Funzioni/_index.md#^definizione-funzione) $f$ può avere al massimo un [asintoto orizzontale destro](Asintoti%20verticali%20e%20orizzontali.md#^definizione-asintoto-orizzontale) e al massimo un [asintoto orizzontale sinistro](Asintoti%20verticali%20e%20orizzontali.md#^definizione-asintoto-orizzontale).

---

> [!fonti]+ Fonti
> 
> - 📚 Sergio Lancelotti, _Lezioni di Analisi Matematica I_, Celid, 2020 (ISBN: `978-8867891979`):
> 	- Capitolo 3 - _Limiti e continuità_:
> 		- 2 - _Limiti di funzioni_:
> 			- 2.3 - _Asintoti verticali e orizzontali_.
