
> [!premessa]+ Premessa
> 
> Ciao! Se è la prima volta che capiti su questo sito, ti consiglio di consultare la [pagina principale](index.md) di questo cosiddetto _Giardino Digitale_ per scoprire meglio cos'è e come navigarlo.
> 
> Lo stato di questa nota è al momento: 🔴 <font color="#FF7F7F">_Bozza_</font>.

---

Dopo aver definito gli [asintoti verticali](Asintoti%20verticali%20e%20orizzontali.md#^definizione-asintoto-verticale) e quelli [orizzontali](Asintoti%20verticali%20e%20orizzontali.md#^definizione-asintoto-orizzontale), ora vediamo quelli [_obliqui_](Asintoti%20obliqui.md#^definizione-asintoto-obliquo).

> [!definizione]+ Definizione: asintoto obliquo
> 
> Data una [funzione](Funzioni.md#^definizione-funzione) $f \colon \text{dom}(f) \to \mathbb{R}$ con $\text{dom}(f)$ illimitato superiormente%% Link %% (o inferiormente%% link %%) e dati $m,q \in \mathbb{R}$ con $m \ne 0$, diciamo che la retta%% link %% $y = mx + q$ è un **asintoto obliquo destro per $x \to + \infty$ (o sinistro per $x \to - \infty$) per $f$** se
> 
> $$
> f(x) = mx + q + o(1)
> $$
> 
> Se la retta%% link %% $y = mx + q$ è contemporaneamente sia un asintoto obliquo destro, sia un asintoto obliquo sinistro, diciamo che più semplicemente la retta%% link %% $y = mx + q$ è un **asintoto obliquo per $f$**.
^definizione-asintoto-obliquo

%% 
esempi 4.35 pagg. 209-210 lancelotti
%%

%% 
Osservazioni 4.36 pagg. 210-211
%%

> [!teorema]+ Teorema di caratterizzazione degli asintoti obliqui
> 
> Data una [funzione](Funzioni.md#^definizione-funzione) $f \colon \text{dom}(f) \to \mathbb{R}$ con $\text{dom}(f)$ illimitato superiormente%% Link %% (o inferiormente%% link %%) e dati $m,q \in \mathbb{R}$ con $m \ne 0$, la retta%% link %% $y = mx + q$ è un [asintoto obliquo destro](Asintoti%20obliqui.md#^definizione-asintoto-obliquo) (o [sinistro](Asintoti%20obliqui.md#^definizione-asintoto-obliquo)) se e solo se
> 1. $f$ è un [infinito](Infiniti%20e%20infinitesimi.md#^definizione-infinito-e-infinitesimo) per $x \to + \infty$ (o per $x \to - \infty$):
> 	$$
> 	\lim_{x \to \pm \infty} f(x) = \pm \infty
> 	$$
> 2. $f$ è un [infinito di ordine $1$ rispetto all'infinito campione $u(x) = |x|$](Infiniti%20e%20infinitesimi.md#^definizione-infinitesimo-di-ordine-alfa-rispetto-all-infinitesimo-campione-u) per $x \to + \infty$ (o per $x \to - \infty$):
> 	$$
> 	\lim_{x \to \pm \infty} \dfrac{f(x)}{|x|} = m
> 	$$
> 3. Vale il seguente [limite](Limiti.md#^definizione-limite):
> 	$$
> 	\lim_{x \to \pm \infty} \left( f(x) - mx \right) = q
> 	$$
^teorema-di-caratterizzazione-degli-asintoti-obliqui

%% 
Dimostrazione per esercizio
%%

%% 
Osservazione 4.38 pag. 211 Lancelotti
%%

%% 
Esercizio 4.39 pag. 211 Lancelotti
%%

%% 
Osservazione 4.40 pagg. 210-211 Lancelotti
%%

%% 
Esempi pagg. 212-214 Lancelotti
%%

---

> [!fonti]+ Fonti
> 
> - 📚 Sergio Lancelotti, _Lezioni di Analisi Matematica I_, Celid, 2020 (ISBN: `978-8867891979`):
> 	- Capitolo 3 - _Limiti e continuità_:
> 		- 4 - _Confronto locale fra funzioni_:
> 			- 4.4 - _Asintoti obliqui_.
