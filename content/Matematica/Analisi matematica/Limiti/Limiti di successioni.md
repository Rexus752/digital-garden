
> [!premessa]+ Premessa
> 
> Ciao! Se è la prima volta che capiti su questo sito, ti consiglio di consultare la [pagina principale](index.md) di questo cosiddetto _Giardino Digitale_ per scoprire meglio cos'è e come navigarlo.
> 
> Lo stato di questa nota è al momento: 🔴 <font color="#FF7F7F">_Bozza_</font>.

---

> [!definizione]+ Definizione: successione
> 
> Una **successione** è una [funzione](Funzioni.md#^definizione-funzione) $a \colon \mathbb{N} \to \mathbb{R}$, denotata con "$(a_n)_{n \in \mathbb{N}}$" o "$\{ a_n \}_{n \in \mathbb{N}}$" (o, quando non c'è ambiguità di notazione, anche $(a_n)$ o $\{ a_n \}$), che associa a ogni numero naturale%% link %% $n \in \mathbb{N}$, detto **indice della successione**, un valore $a(n) \in \mathbb{R}$ denotato con "$a_n$" e detto **termine della successione**.
^definizione-successione

%% specificare che la usccessione è in $A \to \mathbb{R}$ e se $A = \mathbb{N}$ allora è illimitata %%

%% 
esempio 5.2 pag. 215 lancelotti
%%

Poiché una [successione](Limiti%20di%20successioni.md#^definizione-successione) è una [funzione](Funzioni.md#^definizione-funzione) definita su $\mathbb{N}$ o su un suo [sottoinsieme](Teoria%20degli%20insiemi.md#^definizione-sottoinsieme) illimitato superiormente%% Link %%, il dominio%% Link %% della [successione](Limiti%20di%20successioni.md#^definizione-successione) è un [insieme](Teoria%20degli%20insiemi.md#^definizione-insieme) discreto%% link %%, cioè costituito solo da [punti isolati](Topologia%20dei%20reali.md#^definizione-punto-isolato)%% perché? %%, pertanto la [successione](Limiti%20di%20successioni.md#^definizione-successione) è una [funzione continua](Funzioni%20continue.md#^definizione-funzione-continua)%% perché? %%.

Inoltre, essendo illimitato superiormente%% link %%, si ha che $+\infty$ è un [punto di accumulazione](Topologia%20dei%20reali.md#^definizione-punto-di-accumulazione) per il dominio%% link %% della [successione](Limiti%20di%20successioni.md#^definizione-successione)%% perché? %%. È quindi l'unico [punto di accumulazione](Topologia%20dei%20reali.md#^definizione-punto-di-accumulazione)%% perché? %%. Ne segue che per le [successioni](Limiti%20di%20successioni.md#^definizione-successione) l'unico [limite](Limiti.md#^definizione-limite) che ha senso calcolare è quello per la variabile $n$ che tende a $+ \infty$.

Richiamiamo la [definizione di _limite_](Limiti.md#^definizione-limite), adattandola alle [successioni](Limiti%20di%20successioni.md#^definizione-successione), per $n \to + \infty$.

> [!definizione]+ Definizione: limite di successione
> 
> Data una [successione](Limiti%20di%20successioni.md#^definizione-successione) $(a_n)$ e un valore%% link %% $l \in \mathbb{R} \cup \{ \pm \infty \}$, diciamo che **$(a_n)$ ha [limite](Limiti.md#^definizione-limite) $l$ per $n$ che tende a $+ \infty$** se, per ogni [intorno](Topologia%20dei%20reali.md#^definizione-intorno-di-un-punto) $I(l)$ di $l$, esiste un $n_0 \in \mathbb{N}$ tale che per ogni $n \ge n_0$ si ha che $a_n \in I(l)$. In tal caso scriviamo
> 
> $$
> \lim_{n \to + \infty} a_n = l
> $$
> 
> o, più semplicemente,
> 
> $$
> \lim_{n} a_n = l
> $$
> 
> Cioè
> 
> $$
> \begin{array}{}
> \displaystyle\lim_{n} a_n = l \\
> \Updownarrow \\
> \forall I(l), \exists n_0 \in \mathbb{N}, \forall n \in \mathbb{N}. \big( n \ge n_0 \implies a_n \in I(l) \big)  
> \end{array}
> $$
^definizione-limite-di-successione

In base al valore%% link %% che può assumere il [limite](Limiti%20di%20successioni.md#^definizione-limite-di-successione), la [successione](Limiti%20di%20successioni.md#^definizione-successione) può essere [_convergente_](Limiti%20di%20successioni.md#^definizione-convergenza-e-divergenza-di-successioni), [_divergente (positivamente o negativamente)_](Limiti%20di%20successioni.md#^definizione-convergenza-e-divergenza-di-successioni) o [_indeterminata_](Limiti%20di%20successioni.md#^definizione-convergenza-e-divergenza-di-successioni).

> [!definizione]+ Definizione: convergenza e divergenza di successioni
> 
> Una [successione](Limiti%20di%20successioni.md#^definizione-successione) $(a_n)$:
> - **converge a $l$** (oppure **$a_n$ è una [successione](Limiti%20di%20successioni.md#^definizione-successione) convergente**) se $\displaystyle\lim_{n} a_n = l \in \mathbb{R}$.
> - **diverge positivamente** (oppure **$a_n$ è una [successione](Limiti%20di%20successioni.md#^definizione-successione) divergente positivamente**) se $\displaystyle\lim_{n} a_n = + \infty$.
> - **diverge negativamente** (oppure **$a_n$ è una [successione](Limiti%20di%20successioni.md#^definizione-successione) divergente negativamente**) se $\displaystyle\lim_{n} a_n = - \infty$.
> - **è indeterminata** se non esiste il [limite](Limiti%20di%20successioni.md#^definizione-limite-di-successione) $\displaystyle\lim_{n} a_n$.
^definizione-convergenza-e-divergenza-di-successioni

> [!osservazione]+ Osservazione: casi specifici del limite di successioni
> 
> Se una [successione](Limiti%20di%20successioni.md#^definizione-successione) ha [limite](Limiti%20di%20successioni.md#^definizione-limite-di-successione) $l \in \mathbb{R}$ (cioè è una [successione convergente](Limiti%20di%20successioni.md#^definizione-convergenza-e-divergenza-di-successioni)), si ha che
> 
> $$
> \begin{array}{}
> \displaystyle\lim_n a_n = l \in \mathbb{R} \\
> \Updownarrow \\
> \forall \varepsilon > 0, \exists n_0 \in \mathbb{N}, \forall n \in \mathbb{N} . \big( n \ge n_0 \implies \vert a_n - l \vert < \varepsilon \big) 
> \end{array}
> $$
> 
> Invece, se ha [limite](Limiti%20di%20successioni.md#^definizione-limite-di-successione) $l = \pm \infty$ (cioè è una [successione divergente positivamente o negativamente](Limiti%20di%20successioni.md#^definizione-convergenza-e-divergenza-di-successioni)), si ha che
> 
> $$
> \begin{array}{}
> \displaystyle\lim_n a_n = + \infty \\
> \Updownarrow \\
> \forall b \in \mathbb{R}, \exists n_0 \in \mathbb{N}, \forall n \in \mathbb{N} . \big( n \ge n_0 \implies a_n > b \big) \\
> \\
> \displaystyle\lim_n a_n = - \infty \\
> \Updownarrow \\
> \forall b \in \mathbb{R}, \exists n_0 \in \mathbb{N}, \forall n \in \mathbb{N} . \big( n \ge n_0 \implies a_n < b \big) 
> \end{array}
> $$

# 1 - Limiti di funzioni e limiti di successioni

> [!osservazione]+ Osservazione: validità dei teoremi dei limiti nei limiti di successioni
> 
> Poiché i [limiti di successioni](Limiti%20di%20successioni.md#^definizione-limite-di-successione) non sono altro che [limiti](Limiti.md#^definizione-limite) di [funzioni](Funzioni.md#^definizione-funzione) per $n \to + \infty$, per essi valgono tutti i teoremi%% link %% e le considerazioni fatte per questi ultimi, in particolare:
> - il [teorema di unicità del limite](Limiti.md#^teorema-di-unicita-del-limite),
> - il [teorema di limitatezza locale](Proprietà%20locali%20delle%20funzioni%20continue.md#^teorema-di-limitatezza-locale),
> - il [teorema della permanenza del segno](Proprietà%20locali%20delle%20funzioni%20continue.md#^teorema-della-permanenza-del-segno) e le sue conseguenze,
> - l'algebra dei limiti (somma, prodotto, quoziente e composizione)%% link %%,
> - i teoremi del confronto%% link %% e le loro conseguenze,
> - il teorema sui limiti delle successioni monotone%% link %%.
> 
> Inoltre, anche per i [limiti di successioni](Limiti%20di%20successioni.md#^definizione-limite-di-successione) si introducono le stesse [forme indeterminate](Forme%20indeterminate.md#^definizione-forma-indeterminata) e si hanno i seguenti [limiti notevoli](Limiti%20notevoli.md#^definizione-limite-notevole):
> - $\displaystyle\lim_n \left(1 + \dfrac{1}{n}\right)^n = e$,
> - $\forall k \in \mathbb{R}^{> 0}, \forall a \in \mathbb{R}^{>1} . \left( \displaystyle\lim_n \dfrac{n^k}{a_n} = 0 \right)$,
> - $\forall k \in \mathbb{R}^{> 0}, \forall a \in \mathbb{R}^{>0} \setminus \{ 1 \} . \left( \displaystyle\lim_n \dfrac{\log_a n}{n^k} = 0 \right)$,
> - $\forall k \in \mathbb{R}^{> 0}, \forall a \in (0,1) . \left( \displaystyle\lim_n n^ka^n = 0 \right)$.
> 
> Inoltre, anche ai [limiti di successioni](Limiti%20di%20successioni.md#^definizione-limite-di-successione) si associano le nozioni di [infinito](Infiniti%20e%20infinitesimi.md#^definizione-infinito-e-infinitesimo), [infinitesimo](Infiniti%20e%20infinitesimi.md#^definizione-infinito-e-infinitesimo), [$o$-piccolo](Infiniti%20e%20infinitesimi.md#^definizione-o-piccolo), [equivalenza asintotica](Infiniti%20e%20infinitesimi.md#^definizione-equivalenza-asintotica), [ordini di infinito](Infiniti%20e%20infinitesimi.md#^definizione-ordine-di-infinito) e [di infinitesimo](Infiniti%20e%20infinitesimi.md#^definizione-ordine-di-infinitesimo), [infiniti e infinitesimi campione](Infiniti%20e%20infinitesimi.md#^definizione-infiniti-e-infinitesimi-campione) e [parte principale](Infiniti%20e%20infinitesimi.md#^definizione-infinitesimo-di-ordine-alfa-rispetto-all-infinitesimo-campione-u).

%% 
forse mettere a parte i limtii notevoli e dimostrarli uno a uno
%%

%% 
esempio 5.6 pag. 217 lancelotti
%%

## 1.1 - Teorema di caratterizzazione del limite

Il prossimo teorema%% link %% lega tra loro le nozioni di [limite di funzione](Limiti.md#^definizione-limite) e di [limite di successione](Limiti%20di%20successioni.md#^definizione-limite-di-successione).

> [!teorema]+ Teorema di caratterizzazione del limite
> 
> Data una [funzione](Funzioni.md#^definizione-funzione) $f \colon A \subseteq \mathbb{R} \to \mathbb{R}$ (con $A \ne \emptyset$), un [punto di accumulazione](Topologia%20dei%20reali.md#^definizione-punto-di-accumulazione) $x_0 \in \mathbb{R} \cup \{ \pm \infty \}$ per $A$ e un valore%% link %% $l \in \mathbb{R} \cup \{ \pm \infty \}$, allora $\displaystyle\lim_{x \to x_0} f(x) = l$ se e solo se, per ogni [successione](Limiti%20di%20successioni.md#^definizione-successione) $(x_n)$ in $A \setminus \{ x_0 \}$ che tende a $x_0$ si ha che $\displaystyle\lim_n f(x_n) = l$:
> 
> $$
> \begin{array}{}
> \displaystyle\lim_{x \to x_0} f(x) = l \\
> \Updownarrow \\
> \forall (x_n) \subseteq A \setminus \{x_0\}. \big( x_n \to x_0 \implies \displaystyle\lim_n f(x_n) = l \big)
> \end{array}
> $$
^teorema-di-caratterizzazione-del-limite

%% 
che significa "ogni successione **in** A"?
%%

%% 
dimostrazione pag. 217 lancelotti
%%

%%
È utile in due direzioni opposte:

- **$\Rightarrow$** — per *calcolare* limiti di successioni riconducendoli a limiti di funzioni (spesso più facili da trattare).
- **$\Leftarrow$** — per *dimostrare che un limite non esiste*, trovando due successioni $x_n, y_n \to x_0$ tali che $f(x_n)$ e $f(y_n)$ tendono a valori diversi.
%%

%% 
Osservazioni 5.8 ed esempi 5.9, 5.10 pagg. 218-219 lancelotti
%%

%% 
Esercizio 2.11 pag. 219 lancelotti
%%

# 2 - Sottosuccessioni

Se da una [successione](Limiti%20di%20successioni.md#^definizione-successione) selezioniamo solo alcuni [termini](Limiti%20di%20successioni.md#^definizione-successione) stiamo creando una [_sottosuccessione_](Limiti%20di%20successioni.md#^definizione-sottosuccessione).

> [!definizione]+ Definizione: sottosuccessione
> 
> Date due [successioni](Limiti%20di%20successioni.md#^definizione-successione) $(a_n)$ e $(b_n)$, diciamo che **$(b_n)$ è una sottosuccessione (o successione estratta) di $(a_n)$** se $b_n = a_{\varphi(n)}$, dove $\varphi \colon \mathbb{N} \to \mathbb{N}$ è una [successione](Limiti%20di%20successioni.md#^definizione-successione) strettamente crescente%% link %%.
> 
> $(b_n)$ si può anche denotare come "$(a_{n_k})$".
^definizione-sottosuccessione

> [!esempio]- Esempio di sottosuccessione
> 
> Consideriamo una [successione](Limiti%20di%20successioni.md#^definizione-successione) qualsiasi $(a_n)$ e consideriamo una [sottosuccessione](Limiti%20di%20successioni.md#^definizione-sottosuccessione) $(b_n)$ definita da $b_n = a_{\varphi(n)}$, dove $\varphi \colon \mathbb{N} \to \mathbb{N}$ è una [successione](Limiti%20di%20successioni.md#^definizione-successione) strettamente crescente%% link %%. Supponiamo che
> 
> $$
> \begin{array}{}
> \varphi(0) = 2, \\
> \varphi(1) = 4, \\
> \varphi(2) = 5, \\
> \varphi(3) = 13, \\
> \ldots
> \end{array}
> $$
> 
> Seguendo la regola $b_n = a_{\varphi(n)}$, abbiamo che
> 
> $$
> \begin{array}{}
> \varphi(0) = 2 \implies b_0 = a_{\varphi(0)} = a_2, \\
> \varphi(1) = 4 \implies b_1 = a_{\varphi(1)} = a_4, \\
> \varphi(2) = 5 \implies b_2 = a_{\varphi(2)} = a_5, \\
> \varphi(3) = 13 \implies b_3 = a_{\varphi(3)} = a_{13}, \\
> \ldots
> \end{array}
> $$
> 
> Cioè, quello che stiamo facendo è selezionare tramite la [funzione](Funzioni.md#^definizione-funzione) $\varphi$ gli indici dei [termini](Limiti%20di%20successioni.md#^definizione-successione) di $(a_n)$ che vogliamo associare a $(b_n)$.
> 
> Una [sottosuccessione](Limiti%20di%20successioni.md#^definizione-sottosuccessione) di una [successione](Limiti%20di%20successioni.md#^definizione-successione) è quindi una [successione](Limiti%20di%20successioni.md#^definizione-successione) i cui [termini](Limiti%20di%20successioni.md#^definizione-successione) sono selezionati tra quelli della [successione](Limiti%20di%20successioni.md#^definizione-successione) di partenza, in modo che se un [elemento](Teoria%20degli%20insiemi.md#^definizione-insieme) è selezionato (per esempio $a_2$), allora i successivi sono selezionati tra quelli che hanno un indice maggiore di quest'ultimo (cioè $a_4$, $a_5$, $a_{13}$, ecc.).

%% 
esempio 5.13 pag. 220 lancelotti
%%

> [!teorema]+ Teorema di permanenza del limite per sottosuccessioni
> 
> Data una [successione](Limiti%20di%20successioni.md#^definizione-successione) $(a_n)$, se ha [limite](Limiti%20di%20successioni.md#^definizione-limite-di-successione) uguale a $l \in \mathbb{R} \cup \{ \pm \infty \}$, allora per ogni [sottosuccessione](Limiti%20di%20successioni.md#^definizione-sottosuccessione) $(a_{n_k})$ di $(a_n)$ si ha che $\displaystyle\lim_k a_{n_k} = l$:
> 
> $$
> \forall (a_n), \forall (a_{n_k}) \text{ sottosuccessione di } (a_n) . \left( \lim_n a_n = l \in \mathbb{R} \cup \{ \pm \infty \} \implies \lim_k a_{n_k} = l \right) 
> $$

> [!teorema]+ Teorema di Bolzano-Weierstrass
> 
> Una [successione](Limiti%20di%20successioni.md#^definizione-successione) $(a_n)$ limitata%% link %% ammette almeno una [sottosuccessione](Limiti%20di%20successioni.md#^definizione-sottosuccessione) [convergente](Limiti%20di%20successioni.md#^definizione-convergenza-e-divergenza-di-successioni).
^teorema-di-bolzano-weierstrass

> [!teorema]+ Criterio del rapporto per le successioni
> 
> Data una [successione](Limiti%20di%20successioni.md#^definizione-successione) $(a_n)$ a [termini](Limiti%20di%20successioni.md#^definizione-successione) positivi%% link %%, se esiste il [limite](Limiti%20di%20successioni.md#^definizione-limite-di-successione) $\displaystyle\lim_n \dfrac{a_{n+1}}{a_n} = l \in [0, + \infty) \cup \{ + \infty \}$, allora:
> - Se $l < 1$, allora $\displaystyle\lim_n a_n = 0$.
> - Se $l > 1$, allora $\displaystyle\lim_n a_n = +\infty$.
^criterio-del-rapporto-per-le-successioni

%% 
dimostrazione pagg. 220-221 lancelotti
%%

> [!osservazione]+ Osservazione: $\color{#7F7F7F} l=1$ nel criterio del rapporto per le successioni
> 
> Nel [criterio del rapporto per le successioni](Limiti%20di%20successioni.md#^criterio-del-rapporto-per-le-successioni) non viene considerato il caso $l=1$ perché, in questo caso, non si può concludere nulla ed è necessario ricorrere a un altro metodo per calcolare il [limite](Limiti%20di%20successioni.md#^definizione-limite-di-successione) $\displaystyle\lim_n a_n$.

%% 
Esempi 5.18, 5-19 pag. 221-222 lancelotti
%%

> [!teorema]+ Criterio della radice per le successioni
> 
> Data una [successione](Limiti%20di%20successioni.md#^definizione-successione) $(a_n)$ a [termini](Limiti%20di%20successioni.md#^definizione-successione) positivi%% link %%, se esiste il [limite](Limiti%20di%20successioni.md#^definizione-limite-di-successione) $\displaystyle\lim_n \sqrt[n]{a_n} = l \in [0, + \infty) \cup \{ + \infty \}$, allora:
> - Se $l < 1$, allora $\displaystyle\lim_n a_n = 0$.
> - Se $l > 1$, allora $\displaystyle\lim_n a_n = +\infty$.
^criterio-della-radice-per-le-successioni

%% 
dimostrazione pag. 223 lancelotti
%%

> [!osservazione]+ Osservazione: $\color{#7F7F7F} l=1$ nel criterio della radice per le successioni
> 
> Anche nel [criterio della radice per le successioni](Limiti%20di%20successioni.md#^criterio-della-radice-per-le-successioni) non viene considerato il caso $l=1$ perché, sempre per lo stesso motivo, in questo caso non si può concludere nulla ed è necessario ricorrere a un altro metodo per calcolare il [limite](Limiti%20di%20successioni.md#^definizione-limite-di-successione) $\displaystyle\lim_n a_n$.

> [!teorema]+ Teorema della generalità del criterio della radice
> 
> Data una [successione](Limiti%20di%20successioni.md#^definizione-successione) $(a_n)$ a [termini](Limiti%20di%20successioni.md#^definizione-successione) positivi%% link %%, se esiste il [limite](Limiti%20di%20successioni.md#^definizione-limite-di-successione) $\displaystyle\lim_n \dfrac{a_{n+1}}{a_n} = l \in [0, + \infty) \cup \{ + \infty \}$, allora $\displaystyle\lim_n \sqrt[n]{a_n} = l$.

%% 
dimostrazione pag. 223-224 lancelotti
%%

%% 
osservazione 5. 24 pagg. 224-225 lancelotti
%%

%% 
esempi 5.25, 5.26 pagg. 225 lancelotti
%%

---

> [!fonti]+ Fonti
> 
> - 📚 Sergio Lancelotti, _Lezioni di Analisi Matematica I_, Celid, 2020 (ISBN: `978-8867891979`):
> 	- Capitolo 3 - _Limiti e continuità_:
> 		- 5 - _Limiti di successioni_.
