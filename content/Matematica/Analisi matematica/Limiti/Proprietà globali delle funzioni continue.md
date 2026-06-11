---
title: Proprietà globali delle funzioni continue
---

> [!premessa]+ Premessa
> 
> Ciao! Se è la prima volta che capiti su questo sito, ti consiglio di consultare la [pagina principale](index.md) di questo cosiddetto _Giardino Digitale_ per scoprire meglio cos'è e come navigarlo.
> 
> Lo stato di questa nota è al momento: 🔴 <font color="#FF7F7F">_Bozza_</font>.

---

Dopo aver studiato le proprietà locali delle [funzioni continue](Funzioni%20continue.md#^definizione-funzione-continua)%% come il teorema ... %%, ora ci occupiamo delle proprietà globali, cioè di quelle proprietà che coinvolgono tutto il dominio%% link %% e non solo l'[intorno](Topologia%20dei%20reali.md#^definizione-intorno-di-un-punto) di un punto%% link %%.

> [!teorema]+ Teorema degli zeri
> 
> Data una [funzione continua](Funzioni%20continue.md#^definizione-funzione-continua) $f \colon [a,b] \to \mathbb{R}$ tale che $f(a) \cdot f(b) < 0$ (cioè $f(a)$ e $f(b)$ sono discordi), allora esiste un punto%% link %% $x_0 \in (a,b)$ tale che $f(x_0) = 0$.
> 
> Inoltre, se $f$ è strettamente monotona%% Link %%, allora questo punto%% link %% $x_0$ è unico.
^teorema-degli-zeri

%% 
dimostrazione pag. 226-227 lancelotti
%%

> [!osservazione]+ Osservazione: significato del teorema degli zeri
> 
> Il [teorema degli zeri](Proprietà%20globali%20delle%20funzioni%20continue.md#^teorema-degli-zeri) asserisce che se $f$ è [continua](Funzioni%20continue.md#^definizione-funzione-continua) sull'intervallo chiuso%% link %% e limitato%% link %% $[a,b]$ e negli estremi%% link %% assume valori discordi%% link %% allora ammette almeno uno _zero_, cioè un punto%% Link %% in cui si annulla (ossia in cui $f(x)$ vale $0$). Il [teorema](Proprietà%20globali%20delle%20funzioni%20continue.md#^teorema-degli-zeri) non dice quanti ce ne sono (a meno che $f$ non sia strettamente monotona%% Link %%, in quel caso sicuramente ce n'è uno e uno solo) enon ci dice chi sono.

%% 
esempio 6.3 pag. 227-228 lancelotti
%%

> [!corollario]+ Corollario del teorema degli zeri
> 
> Dato un intervallo%% link %% $I \subseteq \mathbb{R}$ e una [funzione continua](Funzioni%20continue.md#^definizione-funzione-continua) $f \colon I \to \mathbb{R}$, se $f$ ammette [limiti](Matematica/Analisi%20matematica/Limiti/_index.md#^definizione-limite) per $x$ che tende agli estremi dell'intervallo%% link %% $I$ e questi [limiti](Matematica/Analisi%20matematica/Limiti/_index.md#^definizione-limite) hanno segni opposti, allora esiste un punto%% link %% $x_0 \in I$ tale che $f(x_0) = 0$.
> 
> Inoltre, se $f$ è strettamente monotona%% Link %%, allora questo punto%% link %% $x_0$ è unico.
^corollario-del-teorema-degli-zeri

%% 
dimostrazione pag. 228 lancelotti
%%

> [!teorema]+ Teorema dei valori intermedi
> 
> Una [funzione continua](Funzioni%20continue.md#^definizione-funzione-continua) $f \colon [a,b] \to \mathbb{R}$ assume tutti i valori%% link %% compresi tra $f(a)$ e $f(b)$, non necessariamente in questo ordine.
> 
> In altri termini, l'intervallo chiuso%% Link %% avente per estremi%% link %% $f(a)$ e $f(b)$ è contenuto in $\text{rng}(f)$.
^teorema-dei-valori-intermedi

%% 
dimostrazione pag. 228-229 lancelotti
%%

%% 
Osservazione 6.6 pag. 229 lancelotti
%%

> [!corollario]+ Corollario 1 del teorema dei valori intermedi
> 
> Dato un intervallo%% Link %% $I \subseteq \mathbb{R}$ e una [funzione continua](Funzioni%20continue.md#^definizione-funzione-continua) $f \colon I \to \mathbb{R}$, allora $f(I) = \text{rng}(f)$ è un intervallo%% link %%.
^corollario-1-del-teorema-dei-valori-intermedi

%% 
dimostrazione pag. 229
%%

%% 
Questa proprietà è molto utile per determinare l'immagine di una funzione continau quando è definita su un intervallo, oppure ristretta ad un intervallo contenuto nel suo dominio. In particolare, se $f$ è monotona, allora possiamo già dire chi è l'immagine, come mostrano i seguenti risultati.
%%

> [!corollario]+ Corollario 2 del teorema dei valori intermedi
> 
> Data una [funzione continua](Matematica/Teoria%20degli%20insiemi/Funzioni/_index.md#^definizione-funzione) e monotona%% link %% $f \colon [a,b] \to \mathbb{R}$, si ha che:
> - se $f$ è crescente%% link %%, allora $\text{rng}(f) = [f(a), f(b)]$ e
> - se $f$ è decrescente%% link %%, allora $\text{rng}(f) = [f(b),f(a)]$.
^corollario-2-del-teorema-dei-valori-intermedi

%% 
Dimostrazione
Segue immediatamente dal corollario 1 e dalla monotonia di $f$
%%

> [!corollario]+ Corollario 3 del teorema dei valori intermedi
> 
> Data una [funzione continua](Funzioni%20continue.md#^definizione-funzione-continua) e monotona%% Link %% $f \colon [a,b) \to \mathbb{R}$, si ha che:
> - se $f$ è crescente%% link %%, allora $\text{rng}(f) = \left[ f(a), \displaystyle\lim_{x \to b^-} f(x) \right)$ e
> - se $f$ è decrescente%% link %%, allora $\text{rng}(f) = \left( \displaystyle\lim_{x \to b^-} f(x), f(a) \right]$.
^corollario-3-del-teorema-dei-valori-intermedi

%% 
Dimostrazione
Segue immediatamente dal corollario 1 e dalla monotonia di $f$
%%

%% 
Osservazione 6.10 pag. 230 lancelotti
%%

%% 
Esempio 6.11 pag. 230 Lancelotti
%%

> [!lemma]+ Lemma delle successioni minimizzanti e massimizzanti
> 
> Dato un [sottoinsieme](Matematica/Teoria%20degli%20insiemi/_index.md#^definizione-sottoinsieme) non [vuoto](Matematica/Teoria%20degli%20insiemi/_index.md#^definizione-insieme-vuoto) $A \subseteq \mathbb{R}$, esistono due [successioni](Limiti%20di%20successioni.md#^definizione-successione) $(x_n)$ e $(y_n)$ in $A$ tali che
> 
> $$
> \lim_n x_n = \inf A \land \lim_n y_n = \sup A
> $$
> 
> La [successione](Limiti%20di%20successioni.md#^definizione-successione) $(x_n)$ è detta **successione minimizzante** e la [successione](Limiti%20di%20successioni.md#^definizione-successione) $(y_n)$ è detta **successione massimizzante**.
^lemma-delle-successioni-minimizzanti-e-massimizzanti

%% 
dimostrazione pagg. 230-231 lancelotti
%%

> [!teorema]+ Teorema di Weierstrass
> 
> Una [funzione continua](Funzioni%20continue.md#^definizione-funzione-continua) $f \colon [a,b] \to \mathbb{R}$ assume minimo%% link %% e massimo%% link %%, cioè esistono due valori%% link %%
> 
> $$
> m = \min_{[a,b]} f \land M = \max_{[a,b]} f
> $$
> 
> In particolare, esistono due punti%% Link %% $x_m, x_M \in [a,b]$ tali che
> 
> $$
> \begin{array}{}
> \displaystyle f(x_m) = m = \min_{[a,b]} f \\
> \displaystyle f(x_M) = M = \max_{[a,b]} f
> \end{array}
> $$
> 
> Inoltre, chiaramente, $\text{rng}(f) = [m,M]$.
^teorema-di-weierstrass

%% 
dimostrazione pag. 231-232 lancelotti
%%

> [!teorema]+ Teorema di monotonia per funzioni continue iniettive
> 
> Dato un intervallo%% link %% $I \subseteq R$ e una [funzione continua](Funzioni%20continue.md#^definizione-funzione-continua) $f \colon I \to \mathbb{R}$, quest'ultima è [iniettiva](Matematica/Teoria%20degli%20insiemi/Funzioni/_index.md#^definizione-iniettivita) se e solo se è strettamente monotona%% Link %%.

%% 
dimostrazione pag. 232 lancelotti
%%

%% 
Questo risultato è fondamentale ogniqualvolta vogliamo invertire una funzione su un intervallo: se la funzione è continua e strettamente monotona, allora per i corollari del teorema dei valori intermedi sappiamo chi è la sua immagine. Inoltre, in base al teorema di monotonia per funzioni continue iniettive, è iniettiva, e quindi restringendo il codominio all'immagine è anche invertibile su questo intervallo
%%

%% 
Osservazione 6.15 pag. 232 lancelotti
%%

> [!teorema]+ Teorema sulla continuità della funzione inversa
> 
> Dati due intervalli%% link %% $I, J \subseteq \mathbb{R}$ e una [funzione continua](Funzioni%20continue.md#^definizione-funzione-continua) e invertibile%% link %% $f \colon I \to J$, la sua inversa%% link %% $f^{-1} \colon J \to I$ è anch'essa [continua](Funzioni%20continue.md#^definizione-funzione-continua).

%% 
dimsotrazione pag. 233 lancelotti
%%

# 1 - Funzioni uniformemente continue

> [!definizione]+ Definizione: funzione uniformemente continua
> 
> Data una [funzione](Matematica/Teoria%20degli%20insiemi/Funzioni/_index.md#^definizione-funzione) $f \colon A \subseteq \mathbb{R} \to \mathbb{R}$ (con $A \ne \emptyset$), diciamo che **$f$ è uniformemente continua in $A$** se, per ogni $\varepsilon > 0$, esiste un $\delta > 0$ tale che, per ogni $x,x_0 \in A$ con $|x - x_0| < \delta$, si ha che $|f(x) - f(x_0)| < \varepsilon$:
> 
> $$
> \begin{array}{}
> \text{$f$ è uniformemente continua in $A$} \\
> \Updownarrow \\
> \forall \varepsilon > 0, \exists \delta > 0, \forall x,x_0 \in A \big( |x - x_0| < \delta \implies |f(x) - f(x_0)| < \varepsilon \big) 
> \end{array}
> $$
^definizione-funzione-uniformemente-continua

> [!osservazione]+ Osservazione: affinità e divergenze tra continuità uniforme e continuità
> 
> La nozione di [_funzione uniformemente continua_](Proprietà%20globali%20delle%20funzioni%20continue.md#^definizione-funzione-uniformemente-continua) è simile a quella di [_funzione continua_](Funzioni%20continue.md#^definizione-funzione-continua), ma si differenziano per i seguenti motivi:
> - La [continuità uniforme](Proprietà%20globali%20delle%20funzioni%20continue.md#^definizione-funzione-uniformemente-continua) è una proprietà globale%% Link %%, mentre la [continuità](Funzioni%20continue.md#^definizione-funzione-continua) è una proprietà locale%% Link %%.
> - Nella [continuità uniforme](Proprietà%20globali%20delle%20funzioni%20continue.md#^definizione-funzione-uniformemente-continua) $\delta$ dipende solo da $\varepsilon$%%, mentre nella [continuità](Funzioni%20continue.md#^definizione-funzione-continua) dipende da ???%%.

%% 
esempio 6.18 paagg. 233-234
%%

> [!teorema]+ Teorema di regolarità della continuità uniforme 
> 
> Se una [funzione](Matematica/Teoria%20degli%20insiemi/Funzioni/_index.md#^definizione-funzione) $f \colon \text{dom}(f) \to \mathbb{R}$ è [uniformemente continua](Proprietà%20globali%20delle%20funzioni%20continue.md#^definizione-funzione-uniformemente-continua), allora è anche [continua](Funzioni%20continue.md#^definizione-funzione-continua).

%% 
Osservazione: il viceversa non è vero, coem mostra la funzione $f(x) = x^2$. Lo è se per esempio $f$ è definita su un intervallo chiuso e limitato, come evidenzia il prossimo risultato.
%%

> [!teorema]+ Teorema di Heine-Cantor
> 
> Se una [funzione](Matematica/Teoria%20degli%20insiemi/Funzioni/_index.md#^definizione-funzione) $f \colon [a,b] \to \mathbb{R}$ è [continua](Funzioni%20continue.md#^definizione-funzione-continua), allora è anche [uniformemente continua](Proprietà%20globali%20delle%20funzioni%20continue.md#^definizione-funzione-uniformemente-continua) in $[a,b]$.

%% 
dimostrazione pagg. 234-235 lancelotti
%%

---

> [!fonti]+ Fonti
> 
> - 📚 Sergio Lancelotti, _Lezioni di Analisi Matematica I_, Celid, 2020 (ISBN: `978-8867891979`):
> 	- Capitolo 3 - _Limiti e continuità_:
> 		- 6 - _Proprietà globali delle funzioni continue_:
> 			- 6.1 - _Funzioni uniformemente continue_.
