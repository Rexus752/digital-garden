
> [!premessa]+ Premessa
> 
> Ciao! Se è la prima volta che capiti su questo sito, ti consiglio di consultare la [pagina principale](index.md) di questo cosiddetto _Giardino Digitale_ per scoprire meglio cos'è e come navigarlo.
> 
> Lo stato di questa nota è al momento: 🔴 <font color="#FF7F7F">_Bozza_</font>.

%% 
capire se integrare questa nota in [Derivate](Derivate.md)
%%

---

Esempio: $f(x) = x^2$ => $f'(x) = 2x$

Data la funzione $f'(x) = 2x$ so che una possibile $f$ è $x^2$, però mi accorgo che tutte le parabole $x^2 + c$ (con $c \in \mathbb{R}$) hanno come derivata la funzione $2x$.

> [!definizione]+ Definizione: primitiva di una derivata
> 
> Data una [funzione](Funzioni.md#^definizione-funzione) $f' \colon \text{dom}(f') \to \mathbb{R}$, diciamo che un'altra [funzione](Funzioni.md#^definizione-funzione) $f \colon \text{dom}(f) \to \mathbb{R}$ è la **primitiva di $f'$** se la [derivata](Derivate.md#^definizione-derivabilita-e-derivata-prima-di-una-funzione) di $f$ è $f'$.
^definizione-primitiva-di-una-derivata

%% 
mettere grafico
f -- primitiva di --> f'
f <- derivata di -- f'
%%

Quindi ogni $x^2 + c$ (per ogni $c \in \mathbb{R}$) è primitiva di $2x$.

> [!teorema]+ Teorema
> 
> Dato un intervallo%% link %% $I \subseteq \mathbb{R}$, se $f$ è una primitiva di $f'$ su $I$, allora $f+c$ è ancora una primitiva di $f$, per ogni $c \in \mathbb{R}$.

> [!teorema]+ Teorema
> 
> Dato un intervallo%% link %% $I \subseteq \mathbb{R}$, se $f_0$ ed $f_1$ sono primitive di $f$ su $I$, allora $f_0 - f_1$ è una costante.

%% 
esercizio: tracciare grafico della primitiva dalla derivata
%%

---

> [!fonti]+ Fonti
> 
> - 🏫 Corso di Laurea in Informatica (`L-31 R`) presso l'Università di Torino:
> 	- Corso di _Analisi Matematica - canale C_, A.A. 2020-21 ([pagina Moodle](https://informatica.i-learn.unito.it/course/view.php?id=2075)):
> 		- Prof. Barutello Vivina Laura, videolezioni:
> 			- [_L3b_](https://informatica.i-learn.unito.it/local/streamingfilemanager/file.php/informatica.i-learn.unito.it/2075/L3b.mp4).
