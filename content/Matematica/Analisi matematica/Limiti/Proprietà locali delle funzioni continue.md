
> [!premessa]+ Premessa
> 
> Ciao! Se è la prima volta che capiti su questo sito, ti consiglio di consultare la [pagina principale](index.md) di questo cosiddetto _Giardino Digitale_ per scoprire meglio cos'è e come navigarlo.
> 
> Lo stato di questa nota è al momento: 🔴 <font color="#FF7F7F">_Bozza_</font>.

---

> [!teorema]+ Teorema di limitatezza locale
> 
> Data una [funzione](Matematica/Teoria%20degli%20insiemi/Funzioni/Funzioni.md#^definizione-funzione) $f \colon \text{dom}(f) \to \mathbb{R}$ e un [punto di accumulazione](Matematica/Teoria%20degli%20insiemi/Funzioni/Topologia%20dei%20reali.md#^definizione-punto-di-accumulazione) $x_0 \in \mathbb{R} \cup \{ \pm \infty \}$ per $\text{dom}(f)$, se esiste un [limite](Matematica/Analisi%20matematica/Limiti/Limiti.md#^definizione-limite)
> 
> $$
> \lim_{x \to x_0} f(x) = l \in \mathbb{R}
> $$
> 
> allora esiste un [intorno](Matematica/Teoria%20degli%20insiemi/Funzioni/Topologia%20dei%20reali.md#^definizione-intorno-di-un-punto) $I(x_0)$ di $x_0$ tale che $f$ è limitata%% link %% su $(\text{dom}(f) \cap I(x_0)) \setminus \{ x_0 \}$.
^teorema-di-limitatezza-locale

%% 
dimostrazione pag. 156 lancelotti
%%

%% 
osservazioni 3.2 pag. 156 lancelotti
%%

> [!teorema]+ Teorema della permanenza del segno
> 
> Data una [funzione](Matematica/Teoria%20degli%20insiemi/Funzioni/Funzioni.md#^definizione-funzione) $f \colon \text{dom}(f) \to \mathbb{R}$ e un [punto di accumulazione](Matematica/Teoria%20degli%20insiemi/Funzioni/Topologia%20dei%20reali.md#^definizione-punto-di-accumulazione) $x_0 \in \mathbb{R} \cup \{ \pm \infty \}$ per $\text{dom}(f)$, se esiste un [limite](Matematica/Analisi%20matematica/Limiti/Limiti.md#^definizione-limite)
> 
> $$
> \lim_{x \to x_0} f(x) = l \in \mathbb{R} \cup \{ \pm \infty \}
> $$
> 
> allora:
> - Se $l > 0$ oppure $l = +\infty$ allora $f(x) > 0$ [vale definitivamente](Matematica/Teoria%20degli%20insiemi/Funzioni/Topologia%20dei%20reali.md#^definizione-proprieta-vera-definitivamente-per-x-che-tende-a-c) per $x \to x_0$.
> - Se $l < 0$ oppure $l = -\infty$ allora $f(x) < 0$ [vale definitivamente](Matematica/Teoria%20degli%20insiemi/Funzioni/Topologia%20dei%20reali.md#^definizione-proprieta-vera-definitivamente-per-x-che-tende-a-c) per $x \to x_0$.
^teorema-della-permanenza-del-segno

> [!osservazione]+ Osservazione: significato del teorema della permanenza del segno
> 
> Il [teorema della permanenza del segno](Matematica/Analisi%20matematica/Limiti/Proprietà%20locali%20delle%20funzioni%20continue.md#^teorema-della-permanenza-del-segno) ci dice che, dato un certo [limite](Matematica/Analisi%20matematica/Limiti/Limiti.md#^definizione-limite) con valore%% link %%, se $l$ è positivo%% link %% allora ci sarà sicuramente un qualche [intorno](Matematica/Teoria%20degli%20insiemi/Funzioni/Topologia%20dei%20reali.md#^definizione-intorno-di-un-punto) per cui $f(x)$ assume valori strettamente positivi%% link %%, mentre se $l$ è negativo%% link %% allora ci sarà sicuramente un qualche [intorno](Matematica/Teoria%20degli%20insiemi/Funzioni/Topologia%20dei%20reali.md#^definizione-intorno-di-un-punto) per cui $f(x)$ assume valori strettamente negativi%% link %%.
> 
> Per esempio, il [limite](Matematica/Analisi%20matematica/Limiti/Limiti.md#^definizione-limite)
> 
> $$
> \lim_{x \to 0} (x + 3)
> $$
> 
> vale $3$ che è positivo%% link %%. Ciò significa che, nelle vicinanze di $x = 0$, per esempio nell'[intorno](Matematica/Teoria%20degli%20insiemi/Funzioni/Topologia%20dei%20reali.md#^definizione-intorno-di-un-punto) $(-1,1)$, avremo che $f(x)$ assumerà valori strettamente positivi%% link %%: ciò è vero perché nell'[intorno](Matematica/Teoria%20degli%20insiemi/Funzioni/Topologia%20dei%20reali.md#^definizione-intorno-di-un-punto) $(-1,1)$ il valore di $f(x)$ varierà tra $(-1 + 3, 1 + 3) = (2, 4)$, ossia assumerà sempre valori strettamente positivi%% link %%.
> 
> Però attenzione: non è detto che la [funzione](Matematica/Teoria%20degli%20insiemi/Funzioni/Funzioni.md#^definizione-funzione) sia positiva%% link %% ovunque, magari per $x$ molto lontano da $x_0$ cambia segno (es. nell'[intorno](Matematica/Teoria%20degli%20insiemi/Funzioni/Topologia%20dei%20reali.md#^definizione-intorno-di-un-punto) $(-5,5)$ quando $x = -4$ avremo che $f(x) = -1$), cioè il [teorema](Matematica/Analisi%20matematica/Limiti/Proprietà%20locali%20delle%20funzioni%20continue.md#^teorema-della-permanenza-del-segno) garantisce il segno%% link %% solo vicino al punto%% Link %% $x_0$.

%% 
dimostrazione pag. 157 lancelotti
%%

> [!dimostrazione]- Dimostrazione del teorema della permanenza del segno
> 
> Dimostriamo il [teorema della permanenza del segno](Matematica/Analisi%20matematica/Limiti/Proprietà%20locali%20delle%20funzioni%20continue.md#^teorema-della-permanenza-del-segno).
> 
> Prendiamo il caso in cui $l > 0$: per ipotesi abbiamo che
> 
> $$
> \lim_{x \to x_0} f(x) = l
> $$
> 
> ossia, sfruttando la [definizione alternativa di limite finito al finito](Matematica/Analisi%20matematica/Limiti/Limiti.md#^osservazione-definizione-alternativa-di-limite-finito-al-finito),
> 
> $$
> \forall \varepsilon > 0, \exists \delta > 0, \forall x \in \mathbb{R} . \big( 0 < |x - x_0| < \delta \implies |f(x) - l| < \varepsilon \big) 
> $$
> 
> Dato che $l > 0$, possiamo porre $\varepsilon = \dfrac{l}{2}$. Possiamo quindi riscrivere la formula di sopra come
> 
> $$
> \begin{array}{}
> \forall \varepsilon > 0, \exists \delta > 0, \forall x \in \mathbb{R} . \left( 0 < |x - x_0| < \delta \implies {\color{#FF7F7F} |f(x) - l| < \dfrac{l}{2} } \right) \\
> \Updownarrow \\
> \forall \varepsilon > 0, \exists \delta > 0, \forall x \in \mathbb{R} . \left( 0 < |x - x_0| < \delta \implies {\color{#FF7F7F} - \dfrac{l}{2} < f(x) - l < \dfrac{l}{2} } \right) \\
> \Updownarrow \\
> \forall \varepsilon > 0, \exists \delta > 0, \forall x \in \mathbb{R} . \left( 0 < |x - x_0| < \delta \implies {\color{#FF7F7F} \dfrac{l}{2} < f(x) < \dfrac{3}{2}l } \right)
> \end{array}
> $$
> 
> Possiamo notare che $f(x)$ allora assumerà sempre valori strettamente positivi%% link %% (perché è compresa tra $\dfrac{l}{2}$ e $\dfrac{3}{2}l$ con $l > 0$), quindi ciò sarò [vero definitivamente](Matematica/Teoria%20degli%20insiemi/Funzioni/Topologia%20dei%20reali.md#^definizione-proprieta-vera-definitivamente-per-x-che-tende-a-c) per $x \to x_0$.

%% finire la dimostrazione %%

%% 
osservazioni 3.4 pag. 157 lancelotti
%%

> [!corollario]+ Corollario del teorema della permanenza del segno
> 
> Data una [funzione](Matematica/Teoria%20degli%20insiemi/Funzioni/Funzioni.md#^definizione-funzione) $f \colon \text{dom}(f) \to \mathbb{R}$ e un [punto di accumulazione](Matematica/Teoria%20degli%20insiemi/Funzioni/Topologia%20dei%20reali.md#^definizione-punto-di-accumulazione) $x_0 \in \mathbb{R} \cup \{ \pm \infty \}$ per $\text{dom}(f)$, se esiste un [limite](Matematica/Analisi%20matematica/Limiti/Limiti.md#^definizione-limite)
> 
>  $$
> \lim_{x \to x_0} f(x) = l \in \mathbb{R}
> $$
> 
> allora:
> - Se $f(x) \ge 0$ allora $l \ge 0$ [vale definitivamente](Matematica/Teoria%20degli%20insiemi/Funzioni/Topologia%20dei%20reali.md#^definizione-proprieta-vera-definitivamente-per-x-che-tende-a-c) per $x \to x_0$.
> - Se $f(x) \le 0$ allora $l \le 0$ [vale definitivamente](Matematica/Teoria%20degli%20insiemi/Funzioni/Topologia%20dei%20reali.md#^definizione-proprieta-vera-definitivamente-per-x-che-tende-a-c) per $x \to x_0$.
^corollario-del-teorema-della-permanenza-del-segno

> [!osservazione]+ Osservazione: significato del corollario del teorema della permanenza del segno
> 
> Questo [corollario](Matematica/Analisi%20matematica/Limiti/Proprietà%20locali%20delle%20funzioni%20continue.md#^corollario-del-teorema-della-permanenza-del-segno) è in un certo senso il "contrario" del [teorema della permanenza del segno](Matematica/Analisi%20matematica/Limiti/Proprietà%20locali%20delle%20funzioni%20continue.md#^teorema-della-permanenza-del-segno), perché qua anziché partire dal segno del [limite](Matematica/Analisi%20matematica/Limiti/Limiti.md#^definizione-limite) $l$ per dedurre il segno della [funzione](Matematica/Teoria%20degli%20insiemi/Funzioni/Funzioni.md#^definizione-funzione) $f(x)$ facciamo il contrario.
> 
> In parole povere, se una [funzione](Matematica/Teoria%20degli%20insiemi/Funzioni/Funzioni.md#^definizione-funzione) è sempre (almeno nei dintorni di $x_0$) positiva%% link %%, allora anche il [limite](Matematica/Analisi%20matematica/Limiti/Limiti.md#^definizione-limite) sarà positivo%% link %%. Viceversa, se una [funzione](Matematica/Teoria%20degli%20insiemi/Funzioni/Funzioni.md#^definizione-funzione) è sempre (almeno nei dintorni di $x_0$) negativa%% link %%, allora anche il [limite](Matematica/Analisi%20matematica/Limiti/Limiti.md#^definizione-limite) sarà negativo%% link %%.
> 
> Per esempio, il [limite](Matematica/Analisi%20matematica/Limiti/Limiti.md#^definizione-limite)
> 
> $$
> \lim_{x \to 0} (x + 5)
> $$
> 
> vale $5$ che è positivo%% link %%. Ciò significa che, nelle vicinanze di $x = 0$, per esempio nell'[intorno](Matematica/Teoria%20degli%20insiemi/Funzioni/Topologia%20dei%20reali.md#^definizione-intorno-di-un-punto) $(-1,1)$, dato che $f(x)$ assume sempre valori positivi%% link %% (perché oscilla tra $4$ e $6$), allora anche il [limite](Matematica/Analisi%20matematica/Limiti/Limiti.md#^definizione-limite) sarà positivo%% Link %% (e infatti vale $5$ che è positivo%% link %%).
> 
> Anche qui non è detto che il [limite](Matematica/Analisi%20matematica/Limiti/Limiti.md#^definizione-limite) sia positivo%% link %% ovunque, magari per $x$ molto lontano da $x_0$ cambia segno (es. nell'[intorno](Matematica/Teoria%20degli%20insiemi/Funzioni/Topologia%20dei%20reali.md#^definizione-intorno-di-un-punto) $(-15,15)$ quando $x = -10$ avremo che $f(x) = -5$, quindi osservando solo questo [intorno](Matematica/Teoria%20degli%20insiemi/Funzioni/Topologia%20dei%20reali.md#^definizione-intorno-di-un-punto) e non altri più "piccoli" non possiamo dedurre con certezza che segno avrà il [limite](Matematica/Analisi%20matematica/Limiti/Limiti.md#^definizione-limite)), cioè il [corollario](Matematica/Analisi%20matematica/Limiti/Proprietà%20locali%20delle%20funzioni%20continue.md#^corollario-del-teorema-della-permanenza-del-segno) garantisce il segno%% link %% solo vicino al punto%% Link %% $x_0$.

> [!osservazione]+ Osservazione: funzione strettamente positiva o negativa
> 
> Se modificassimo l'enunciato del [corollario del teorema della permanenza del segno](Matematica/Analisi%20matematica/Limiti/Proprietà%20locali%20delle%20funzioni%20continue.md#^corollario-del-teorema-della-permanenza-del-segno) ipotizzando che $f(x)$ sia strettamente positiva%% link %% o strettamente negativa%% link %%, allora la tesi rimarrebbe comunque che il [limite](Matematica/Analisi%20matematica/Limiti/Limiti.md#^definizione-limite) è positivo%% link %% o negativo%% link %%:
> 
> $$
> \begin{array}{}
> f(x) > 0 \implies l \ge 0 \text{ vero definitivamente per } x \to x_0 \\
> f(x) < 0 \implies l \le 0 \text{ vero definitivamente per } x \to x_0
> \end{array}
> $$
> 
> Per esempio, il [limite](Matematica/Analisi%20matematica/Limiti/Limiti.md#^definizione-limite)
> 
> $$
> \lim_{x \to 0} x^2
> $$
> 
> vale $0$ anche se $f(x)$ assumerà sempre e solo valori strettamente positivi%% link %% e mai $0$ (eccetto per $x = 0$ stesso).

> [!dimostrazione]- Dimostrazione del corollario del teorema della permanenza del segno
> 
> Dimostriamo il [corollario del teorema della permanenza del segno](Matematica/Analisi%20matematica/Limiti/Proprietà%20locali%20delle%20funzioni%20continue.md#^corollario-del-teorema-della-permanenza-del-segno).
> 
> Prendiamo il caso in cui $f(x) \ge 0$: dobbiamo dimostrare che $l \ge 0$ [vale definitivamente](Matematica/Teoria%20degli%20insiemi/Funzioni/Topologia%20dei%20reali.md#^definizione-proprieta-vera-definitivamente-per-x-che-tende-a-c) per $x \to x_0$:
> 
> $$
> f(x) \ge 0 \implies l \ge 0
> $$
> 
> Per contrapposizione%% link %%, possiamo riscrivere questa proposizione logica come
> 
> $$
> l < 0 \implies f(x) < 0
> $$
> 
> Per il [teorema della permanenza del segno](Matematica/Analisi%20matematica/Limiti/Proprietà%20locali%20delle%20funzioni%20continue.md#^teorema-della-permanenza-del-segno) abbiamo che vale questa implicazione%% link %%.
> 
> Stesso discorso per il caso $f(x) \le 0$: dobbiamo dimostrare che $l \le 0$ [vale definitivamente](Matematica/Teoria%20degli%20insiemi/Funzioni/Topologia%20dei%20reali.md#^definizione-proprieta-vera-definitivamente-per-x-che-tende-a-c) per $x \to x_0$:
> 
> $$
> f(x) \le 0 \implies l \le 0
> $$
> 
> Per contrapposizione%% link %%, possiamo riscrivere questa proposizione logica come
> 
> $$
> l > 0 \implies f(x) > 0
> $$
> 
> e anche questo vale per il [teorema della permanenza del segno](Matematica/Analisi%20matematica/Limiti/Proprietà%20locali%20delle%20funzioni%20continue.md#^teorema-della-permanenza-del-segno).
> 
> $\blacksquare$

%% 
dimostrazione pag. 157 lancelotti
%%

%% 
osservazione 3.6 pag. 158 lancelotti
%%

---

> [!fonti]+ Fonti
> 
> - 🏫 Corso di Laurea in Informatica (`L-31 R`) presso l'Università di Torino:
> 	- Corso di _Analisi Matematica - canale C_, A.A. 2020-21 ([pagina Moodle](https://informatica.i-learn.unito.it/course/view.php?id=2075)):
> 		- Prof. Barutello Vivina Laura, videolezioni:
> 			- [_L8a_](https://informatica.i-learn.unito.it/local/streamingfilemanager/file.php/informatica.i-learn.unito.it/2075/L8a.mp4).
> - 📚 Sergio Lancelotti, _Lezioni di Analisi Matematica I_, Celid, 2020 (ISBN: `978-8867891979`):
> 	- Capitolo 3 - _Limiti e continuità_:
> 		- 3 - _Teoremi su limiti e continuità_:
> 			- 3.1 - _Proprietà locali_.
