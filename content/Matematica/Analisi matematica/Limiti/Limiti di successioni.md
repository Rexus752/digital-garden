
> [!premessa]+ Premessa
> 
> Ciao! Se è la prima volta che capiti su questo sito, ti consiglio di consultare la [pagina principale](index.md) di questo cosiddetto _Giardino Digitale_ per scoprire meglio cos'è e come navigarlo.
> 
> Lo stato di questa nota è al momento: 🔴 <font color="#FF7F7F">_Bozza_</font>.

%% 
scegliere se adottare come notazione $(a_n)$ o $\{ a_n \}$ 
%%

---

> [!definizione]+ Definizione: successione
> 
> Una **successione** è una [funzione](Funzioni.md#^definizione-funzione) $a \colon \mathbb{N} \to \mathbb{R}$, denotata con "$(a_n)_{n \in \mathbb{N}}$" o "$\{ a_n \}_{n \in \mathbb{N}}$" (o, quando non c'è ambiguità di notazione, anche $(a_n)$ o $\{ a_n \}$), che associa a ogni numero naturale%% link %% $n \in \mathbb{N}$, detto **indice della successione**, un valore $a(n) \in \mathbb{R}$ denotato con "$a_n$" e detto **termine della successione**.
^definizione-successione

%%
specificare che la usccessione è in $A \subseteq \mathbb{N} \to \mathbb{R}$ (in particolare $a \colon \{ n \in \mathbb{N} \mid n \ge n_0 \}$ dato un certo $n_0 \in \mathbb{N}$)

se $A = \mathbb{N}$ allora è illimitata
%%

%% 
esempio 5.2 pag. 215 lancelotti
%%

%% 
Esempio di grafico della successione
%%

> [!osservazione]+ Osservazioni: successioni sono funzioni continue
> 
> Poiché una [successione](Limiti%20di%20successioni.md#^definizione-successione) è una [funzione](Funzioni.md#^definizione-funzione) definita su $\mathbb{N}$ o su un suo [sottoinsieme](Teoria%20degli%20insiemi.md#^definizione-sottoinsieme) illimitato superiormente%% Link %%, il dominio%% Link %% della [successione](Limiti%20di%20successioni.md#^definizione-successione) è un [insieme](Teoria%20degli%20insiemi.md#^definizione-insieme) discreto%% link %%, cioè costituito solo da [punti isolati](Topologia%20dei%20reali.md#^definizione-punto-isolato)%% perché? %%, pertanto la [successione](Limiti%20di%20successioni.md#^definizione-successione) è una [funzione continua](Funzioni%20continue.md#^definizione-funzione-continua)%% perché? %%.

> [!osservazione]+ Osservazione: possibili applicazioni delle successioni
> 
> A cosa ci può servire quindi studiare queste [successioni](Limiti%20di%20successioni.md#^definizione-successione)?
> 
> Una possibile applicazione del concetto di [_successione_](Limiti%20di%20successioni.md#^definizione-successione) si può trovare in biologia per quanto riguarda la riproduzione cellulare: si può per esempio studiare una [successione](Limiti%20di%20successioni.md#^definizione-successione) $\{ a_n \}$ dove l'$n$-esimo [termine](Limiti%20di%20successioni.md#^definizione-successione) indica il numero di cellule che costituiscono l'organismo all'$n$-esima generazione, similmente all'applicazione del concetto di _derivata_ allo studio demografico di una popolazione%% link a quell'osservazione %%.
> 
> Un'altra possibile applicazione è nello studio della complessità degli algoritmi%% link %% in cui si può studiare una [successione](Limiti%20di%20successioni.md#^definizione-successione) $\{ o_n \}$ dove l'$n$-esimo [termine](Limiti%20di%20successioni.md#^definizione-successione) indica il numero di operazioni%% link %% per eseguire l'algoritmo%% link %% su un array%% link %% di dimensione%% link %% $n$.

> [!notazione]+ Notazione: successione definita con una formula esplicita
> 
> Una [successione](Limiti%20di%20successioni.md#^definizione-successione) si può definire attraverso una **formula esplicita**, cioè esattamente come facciamo con le funzioni definite con una formula esplicita%% link %%, definendo qual è la trasformazione che viene applicata all'$n$-esimo [termine](Limiti%20di%20successioni.md#^definizione-successione): per esempio, possiamo definire una [successione](Limiti%20di%20successioni.md#^definizione-successione) come
> 
> $$
> \{ a_n \} = n!
> $$
> 
> dove al [termine](Limiti%20di%20successioni.md#^definizione-successione) $n$-esimo viene assegnato il valore del suo fattoriale%% link %% (es. $a_5 = 5! = 120$), oppure la [successione](Limiti%20di%20successioni.md#^definizione-successione)
> 
> $$
> \{ b_n \} = n^2 + 1
> $$
> 
> dove al [termine](Limiti%20di%20successioni.md#^definizione-successione) $n$-esimo viene assegnato il valore di $n^2 + 1$ (es. $b_3 = 3^2 + 1 = 10$).
^notazione-successione-definita-con-una-formula-esplicita

%% 
Posso definire una [successione](Limiti%20di%20successioni.md#^definizione-successione)

$$
\{ c_n \} = \dfrac{1}{n - 2}
$$

anche se il termine $c_2$ non esiste e quindi il suo dominio non è più $\mathbb{N}$ ma $\mathbb{N} \setminus \{ 2 \}$?
%%

> [!notazione]+ Notazione: successione definita con una relazione ricorsiva
> 
> Una [successione](Limiti%20di%20successioni.md#^definizione-successione) si può definire attraverso una **relazione ricorsiva** in cui si esprime ricorsivamente%% link %%%% quando aggiungerò la ricorsione sul Giardino, mettere riferimento alla pagina Facebook dei fan delle strutture ricorsive %% il valore del [termine](Limiti%20di%20successioni.md#^definizione-successione) $n$-esimo, in particolare:
> - si esprime il valore del [termine](Limiti%20di%20successioni.md#^definizione-successione) $n$-esimo rispetto a $k \ge 1$ [termini](Limiti%20di%20successioni.md#^definizione-successione) che lo precedono, i quali sono parametri di una [funzione](Funzioni.md#^definizione-funzione) $g(x_{n-1}, x_{n-2}, \ldots, x_{n-k})$ detta **relazione ricorsiva** e
> - si esprime il valore iniziale dei primi $k$ [termini](Limiti%20di%20successioni.md#^definizione-successione) della [successione](Limiti%20di%20successioni.md#^definizione-successione) $a_0, \ldots, a_{k-1}$:
> 
> $$
> \{ x_n \} = \begin{cases}
> x_0 = v_0 \\
> x_1 = v_1 \\
> \ldots \\
> x_{k-1} = v_{k-1} \\
> x_n = g(x_{n-1}, x_{n-2}, \ldots, x_{n-k})
> \end{cases}
> $$
> 
> Per esempio, nella [successione](Limiti%20di%20successioni.md#^definizione-successione)
> 
> $$
> \{ r_n \} = \begin{cases}
> r_0 = 3 \\
> r_{n} = r_{n-1}^2 - r_{n-1}
> \end{cases}
> $$
> 
> abbiamo che:
> - $r_1 = r_0^2 - r_0 = 3^2 - 3 = 6$,
> - $r_2 = r_1^2 - r_1 = 6^2 - 6 = 30$,
> - $r_3 = r_2^2 - r_2 = 30^2 - 30 = 870$
> - e così via.
^notazione-successione-definita-con-una-relazione-ricorsiva

%% 
trasformare in definizione

Definizione: successione ricorsiva e relazione ricorsiva
%%

Un esempio invece di una [successione definita con una relazione ricorsiva](Limiti%20di%20successioni.md#^notazione-successione-definita-con-una-relazione-ricorsiva) con $k = 2$ è la _successione di Fibonacci_.

> [!definizione]+ Definizione: successione di Fibonacci
> 
> La **successione (o sequenza) di Fibonacci** è una [successione](Limiti%20di%20successioni.md#^definizione-successione) definita come
> 
> $$
> \{ F_n \} = \begin{cases}
> F_0 = 0 \\
> F_1 = 1 \\
> F_{n} = F_{n-1} + F_{n-2}
> \end{cases}
> $$
^definizione-successione-di-fibonacci

%% 
chi è Fibonacci?
%%

> [!osservazione]+ Osservazione: differenza nelle due notazioni
> 
> La principale differenza tra la [notazione con la formula esplicita](Limiti%20di%20successioni.md#^notazione-successione-definita-con-una-formula-esplicita) e [quella con la relazione ricorsiva](Limiti%20di%20successioni.md#^notazione-successione-definita-con-una-relazione-ricorsiva) è che la prima ci permette di calcolare direttamente l'$n$-esimo [termine](Limiti%20di%20successioni.md#^definizione-successione), mentre con la seconda siamo costretti a calcolare anche tutti gli altri [termini](Limiti%20di%20successioni.md#^definizione-successione) precedenti.
> 
> Possiamo quindi fare un parallelismo con i tipi di accesso alla memoria%% link ai tipi di accesso alla memoria %% in informatica%% link, oppure mettere qualcosa di più specifico di "informatica" %%, in cui la [notazione con la formula esplicita](Limiti%20di%20successioni.md#^notazione-successione-definita-con-una-formula-esplicita) ci permette di fare un _accesso casuale_%% link (oppure _accesso diretto_?) %% all'$n$-esimo [termine](Limiti%20di%20successioni.md#^definizione-successione), mentre la [notazione con la relazione ricorsiva](Limiti%20di%20successioni.md#^notazione-successione-definita-con-una-relazione-ricorsiva) ci permette di fare un _accesso sequenziale_.

Dal momento che le [successioni](Limiti%20di%20successioni.md#^definizione-successione) sono in realtà [funzioni](Funzioni.md#^definizione-funzione), anche a loro si applicano concetti come quello di [monotonia](Proprietà%20delle%20funzioni.md#^definizione-funzione-strettamente-decrescente-o-monotona-su-un-intervallo) e [limitatezza](Proprietà%20delle%20funzioni.md#^definizione-funzioni-limitate).

> [!definizione]+ Definizione: successione monotona
> 
> Una [successione](Limiti%20di%20successioni.md#^definizione-successione) $\{ a_n \}$ si dice
> - **monotona crescente** se
> 	$$
> 	\forall n \in \mathbb{N} . (a_{n + 1} \ge a_n)
> 	$$
> - **monotona strettamente crescente** se
> 	$$
> 	\forall n \in \mathbb{N} . (a_{n + 1} > a_n)
> 	$$
> - **monotona decrescente** se
> 	$$
> 	\forall n \in \mathbb{N} . (a_{n + 1} \le a_n)
> 	$$
> - **monotona strettamente decrescente** se
> 	$$
> 	\forall n \in \mathbb{N} . (a_{n + 1} < a_n)
> 	$$
> - **monotona** se è monotona crescente o monotona decrescente e
> - **strettamente monotona** se è strettamente monotona crescente o strettamente monotona decrescente.
^definizione-successione-monotona

> [!definizione]+ Definizione: successione limitata
> 
> Una [successione](Limiti%20di%20successioni.md#^definizione-successione) $\{ a_n \}$ si dice
> - **superiormente limitata** se
> 	$$
> 	\exists m \in \mathbb{R}, \forall n \in \mathbb{N} . (m \le a_n)
> 	$$
> - **inferiormente limitata** se
> 	$$
> 	\exists m \in \mathbb{R}, \forall n \in \mathbb{N} . (a_n \le M)
> 	$$
> - **limitata** se
> 	$$
> 	\exists m, M \in \mathbb{R}, \forall n \in \mathbb{N} . (m \le a_n \le M)
> 	$$
^definizione-successione-limitata

# 1 - Limiti di successioni

Una [successione](Limiti%20di%20successioni.md#^definizione-successione), essendo illimitata superiormente%% link %%, si ha che $+\infty$ è un [punto di accumulazione](Topologia%20dei%20reali.md#^definizione-punto-di-accumulazione) per il suo [dominio](Funzioni.md#^definizione-dominio-e-codominio-della-funzione)%% perché? %%. È quindi l'unico [punto di accumulazione](Topologia%20dei%20reali.md#^definizione-punto-di-accumulazione)%% perché? %%. Ne segue che per le [successioni](Limiti%20di%20successioni.md#^definizione-successione) l'unico [limite](Limiti.md#^definizione-limite) che ha senso calcolare è quello per la variabile $n$ che tende a $+ \infty$.

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

%%
$$
\forall \varepsilon > 0, \exists N_\varepsilon > 0 . \big( n > N_\varepsilon \implies |a_n - l| < \varepsilon \big) 
$$

- $N_\varepsilon$ sarebbe $\delta$? (nel caso sostituirlo con $\delta$)
- $\varepsilon, N_\varepsilon$ sono in $\mathbb{N}$ o in $\mathbb{R}$? Nel caso sarebbe sbagliato considerarli in $\mathbb{R}$?

stessa definizione del limite infinito all'infinito (per questo si usa $N_\varepsilon$)
%%

In base al valore%% link %% che può assumere il [limite](Limiti%20di%20successioni.md#^definizione-limite-di-successione), la [successione](Limiti%20di%20successioni.md#^definizione-successione) può essere [_convergente_](Limiti%20di%20successioni.md#^definizione-convergenza-e-divergenza-di-successioni), [_divergente (positivamente o negativamente)_](Limiti%20di%20successioni.md#^definizione-convergenza-e-divergenza-di-successioni) o [_indeterminata_](Limiti%20di%20successioni.md#^definizione-convergenza-e-divergenza-di-successioni).

> [!definizione]+ Definizione: convergenza e divergenza di successioni
> 
> Una [successione](Limiti%20di%20successioni.md#^definizione-successione) $(a_n)$ si dice che:
> - **converge a $l$** (oppure **$a_n$ è una [successione](Limiti%20di%20successioni.md#^definizione-successione) convergente**) se $\displaystyle\lim_{n} a_n = l \in \mathbb{R}$.
> - **diverge positivamente** (oppure **$a_n$ è una [successione](Limiti%20di%20successioni.md#^definizione-successione) divergente positivamente**) se $\displaystyle\lim_{n} a_n = + \infty$.
> - **diverge negativamente** (oppure **$a_n$ è una [successione](Limiti%20di%20successioni.md#^definizione-successione) divergente negativamente**) se $\displaystyle\lim_{n} a_n = - \infty$.
> - **è indeterminata** se non esiste il [limite](Limiti%20di%20successioni.md#^definizione-limite-di-successione) $\displaystyle\lim_{n} a_n$.
^definizione-convergenza-e-divergenza-di-successioni

> [!teorema]+ Teorema del legame tra la convergenza e la limitatezza di una successione
> 
> Se una [successione](Limiti%20di%20successioni.md#^definizione-successione) $\{ a_n \}$ è [convergente](Limiti%20di%20successioni.md#^definizione-convergenza-e-divergenza-di-successioni) allora è anche [limitata](Limiti%20di%20successioni.md#^definizione-successione-limitata).
^teorema-del-legame-tra-la-convergenza-e-la-limitatezza-di-una-successione

%% 
Spiegazione: se è convergente allora il limite è $l \in \mathbb{R}$ e basterà trovare un qualsiasi $\varepsilon$ per cui $\underbrace{l - \varepsilon}_{=m} \le a_n \le \underbrace{l + \varepsilon}_{=M}$
%%

%% 
Osservazione: non vale il viceversa, cioè limitatezza =/=> convergenza perché per esempio

$$
\{ a_n \} = (-1)^n
$$

è limitata $-1 \le a_n \le 1$ per ogni $n \in \mathbb{N}$, ma il limite $\lim_n a_n$ non esiste (cioè è indeterminata)
%%

> [!teorema]+ Teorema del legame tra la monotonia e il limite di una successione
> 
> Se una [successione](Limiti%20di%20successioni.md#^definizione-successione) $\{ a_n \}$ è [monotona](Limiti%20di%20successioni.md#^definizione-successione-monotona) allora il [limite](Limiti%20di%20successioni.md#^definizione-limite-di-successione) $\displaystyle\lim_n a_n$ esiste e, in particolare,
> - se $\{ a_n \}$ è [crescente](Limiti%20di%20successioni.md#^definizione-successione-monotona) e [superiormente limitata](Limiti%20di%20successioni.md#^definizione-successione-limitata) allora $\{ a_n \}$ è [convergente](Limiti%20di%20successioni.md#^definizione-convergenza-e-divergenza-di-successioni),
> - se $\{ a_n \}$ è [decrescente](Limiti%20di%20successioni.md#^definizione-successione-monotona) e [inferiormente limitata](Limiti%20di%20successioni.md#^definizione-successione-limitata) allora $\{ a_n \}$ è [convergente](Limiti%20di%20successioni.md#^definizione-convergenza-e-divergenza-di-successioni),
> - se $\{ a_n \}$ è [crescente](Limiti%20di%20successioni.md#^definizione-successione-monotona) e [superiormente illimitata](Limiti%20di%20successioni.md#^definizione-successione-limitata) allora $\{ a_n \}$ è [divergente](Limiti%20di%20successioni.md#^definizione-convergenza-e-divergenza-di-successioni) a $+ \infty$,
> - se $\{ a_n \}$ è [decrescente](Limiti%20di%20successioni.md#^definizione-successione-monotona) e [inferiormente illimitata](Limiti%20di%20successioni.md#^definizione-successione-limitata) allora $\{ a_n \}$ è [divergente](Limiti%20di%20successioni.md#^definizione-convergenza-e-divergenza-di-successioni) a $- \infty$. 
^teorema-del-legame-tra-la-monotonia-e-il-limite-di-una-successione

%% 
attenzione: $l$ non deve essere necessariamente uguale ai massimi e minimi della limitatezza
%%

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

%% 
modificare anche qua le definizioni formali nel caso
%%

## 1.1 - Legame tra limiti di funzioni e limiti di successioni

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

## 1.2 - Teorema di caratterizzazione del limite

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

# 3 - Successioni geometriche

%% 
da spostare nella pagina delle successioni e basta senza limite
%%

> [!definizione]+ Definizione: successione geometrica
> 
> Una [successione](Limiti%20di%20successioni.md#^definizione-successione) $\{ a_n \}$ si dice **geometrica** se
> 
> $$
> \exists q \in \mathbb{R}, \forall n \in \mathbb{N} . \left( a_{n + 1} = q \cdot a_n \right) 
> $$
> 
> In particolare, $q$ si dice **ragione della successione**.
^definizione-successione-geometrica

> [!osservazione]+ Osservazioni: successioni geometriche definite solo con relazione ricorsiva
> 
> Data la loro natura in cui ogni [termine](Limiti%20di%20successioni.md#^definizione-successione) è legato al precedente, le [successioni geometriche](Limiti%20di%20successioni.md#^definizione-successione-geometrica) si possono definire solo tramite la [notazione con la relazione ricorsiva](Limiti%20di%20successioni.md#^notazione-successione-definita-con-una-relazione-ricorsiva).
> 
> Per esempio, possiamo definire la [successione geometrica](Limiti%20di%20successioni.md#^definizione-successione-geometrica)
> 
> $$
> \{ a_n \} = \begin{cases}
> a_0 = 1 \\
> a_{n + 1} = 3 \cdot a_n
> \end{cases}
> $$
> 
> in cui abbiamo che la sua [ragione](Limiti%20di%20successioni.md#^definizione-successione-geometrica) è $3$ e i primi $4$ [termini](Limiti%20di%20successioni.md#^definizione-successione) sono:
> - $a_0 = 1$,
> - $a_1 = 3 \cdot a_0 = 3 \cdot 1 = 3$,
> - $a_2 = 3 \cdot a_1 = 3 \cdot 3 = 9$,
> - $a_3 = 3 \cdot a_2 = 3 \cdot 9 = 27$,
> - e così via.

> [!osservazione]+ Osservazione: formula esplicita di una successione geometrica
> 
> Data una [successione geometrica](Limiti%20di%20successioni.md#^definizione-successione-geometrica) $\{ a_n \}$, se $a_0 = 0$, allora $a_n = 0$ per ogni $n \ge 0$.
> 
> Se invece $a_0 \ne 0$, allora avremo che:
> - $a_1 = q \cdot a_0$,
> - $a_2 = q \cdot a_1 = q \cdot q \cdot a_0 = q^2 \cdot a_0$,
> - $a_3 = q \cdot a_2 = q \cdot q^2 \cdot a_0 = q^3 \cdot a_0$,
> - e così via.
> 
> Possiamo generalizzare ciò come
> 
> $$
> a_n = q^n \cdot a_0
> $$
> 
> e questa formula viene detta **formula esplicita** della [successione geometrica](Limiti%20di%20successioni.md#^definizione-successione-geometrica) perché è un modo alternativo di definirla.
^osservazione-formula-esplicita-di-una-successione-geometrica

%%
| $q$          | **Limitatezza** | **Monotonia** | **Limite**    |
| ------------ | --------------- | ------------- | ------------- |
| $q > 1$      | no              | crescente     | $+ \infty$    |
| $q = 1$      | sì              | costante      | $1$           |
| $0 < q < 1$  | sì              | decrescente   | $0$           |
| $q = 0$      | sì              | costante      | $0$           |
| $-1 < q < 0$ | sì              | non monotona  | $0$           |
| $q = -1$     | sì              | non monotona  | $\not\exists$ |
| $q < -1$     | no              | non monotona  | $\not\exists$ |
%%

# 4 - Successioni definite con relazione ricorsiva

## 4.1 - Punti fissi

Approfondiamo le [successioni definite con una relazione ricorsiva](Limiti%20di%20successioni.md#^notazione-successione-definita-con-una-relazione-ricorsiva).

%% 
Osservazione: grafico a ragnatela delle successioni definite con una relazione ricorsiva
%%

> [!definizione]+ Definizione: punto fisso o punto di equilibrio di una relazione ricorsiva
> 
> In una [successione](Limiti%20di%20successioni.md#^definizione-successione) $\{ x_n \}$ [definita con una relazione ricorsiva](Limiti%20di%20successioni.md#^notazione-successione-definita-con-una-relazione-ricorsiva), un valore $x^\star \in \text{dom}(g)$ viene detto **punto fisso (o punto di equilibrio) di $g$** se
> 
> $$
> g(x^\star) = x^\star
> $$
^definizione-punto-fisso-o-punto-di-equilibrio-di-una-relazione-ricorsiva

%% 
Osservazione: perché viene detto punto fisso o punto di equilibrio
%%

> [!proposizione]+ Proposizione: legame tra la convergenza di una successione e il punto fisso
> 
> Data una [funzione](Funzioni.md#^definizione-funzione) $g \colon \mathbb{R} \to \mathbb{R}$ [continua](Funzioni%20continue.md#^definizione-funzione-continua) e una [successione](Limiti%20di%20successioni.md#^definizione-successione) $\{ x_n \}$ [definita con la relazione ricorsiva](Limiti%20di%20successioni.md#^notazione-successione-definita-con-una-relazione-ricorsiva) $g$, se esiste il [limite](Limiti%20di%20successioni.md#^definizione-limite-di-successione)
> 
> $$
> \lim_n x_n = x^\star \in \mathbb{R}
> $$
> 
> (cioè $\{ x_n \}$ [converge](Limiti%20di%20successioni.md#^definizione-convergenza-e-divergenza-di-successioni)), allora $x^\star$ è un [punto fisso](Limiti%20di%20successioni.md#^definizione-punto-fisso-o-punto-di-equilibrio-di-una-relazione-ricorsiva) di $g$ (cioè $g(x^\star) = x^\star$). 
^proposizione-legame-tra-la-convergenza-di-una-successione-e-il-punto-fisso

> [!dimostrazione]- Dimostrazione del legame tra convergenza di una successione e punto fisso
> 
> Dimostriamo il [legame tra la convergenza di una successione e il punto fisso](Limiti%20di%20successioni.md#^proposizione-legame-tra-convergenza-di-una-successione-e-punto-fisso).
> 
> Poiché la [successione](Limiti%20di%20successioni.md#^definizione-successione) $\{ x_n \}$ [converge](Limiti%20di%20successioni.md#^definizione-convergenza-e-divergenza-di-successioni), cioè
> 
> $$
> \lim_{n} x_n = x^\star
> $$
> 
> allora abbiamo anche che
> 
> $$
> \lim_n x_{n+1} = x^\star
> $$
> 
> e cioè, [per definizione di _relazione ricorsiva_](Limiti%20di%20successioni.md#^notazione-successione-definita-con-una-relazione-ricorsiva),
> 
> $$
> \lim_n g(x_n) = x^\star
> $$
> 
> D'altra parte, poiché $g$ è [continua](Funzioni%20continue.md#^definizione-funzione-continua) in $x^\star$, per il teorema del limite della funzione composta%% link %% (o, equivalentemente, per la caratterizzazione della continuità per successioni%% link %%) possiamo portare il [limite](Limiti%20di%20successioni.md#^definizione-limite-di-successione) "dentro" $g$:
> 
> $$
> \lim_n g(x_n) = g\left( \lim_n x_n \right) = g(x^\star)
> $$
> 
> Confrontando le due espressioni ottenute per $\displaystyle\lim_n g(x_n)$, cioè
> 
> $$
> \lim_n g(x_n) = x^\star \quad \land \quad \lim_n g(x_n) = g(x^\star)
> $$
> 
> per il [teorema di unicità del limite](Limiti.md#^teorema-di-unicita-del-limite), otteniamo
> 
> $$
> g(x^\star) = x^\star
> $$
> 
> che è proprio la definizione di [punto fisso](Limiti%20di%20successioni.md#^definizione-punto-fisso-o-punto-di-equilibrio-di-una-relazione-ricorsiva) di $g$.
> 
> $\blacksquare$

## 4.2 - Successioni ricorsive lineari

Consideriamo ora un caso specifico delle successioni ricorsive%% link %%, ossia quelle _lineari_.

> [!definizione]+ Definizione: successione ricorsiva lineare
> 
> Una successione ricorsiva%% link %% $\{ x_n \}$ si dice **lineare** quando la sua formula ricorsiva%% link %% è della forma $g(x) = ax+b$ con $a,b \in \mathbb{R}$, ossia
> 
> $$
> \begin{cases}
> x_0 = v_0 \\
> x_n = ax_{n-1} + b
> \end{cases}
> $$
^definizione-successione-ricorsiva-lineare

> [!osservazione]+ Osservazione: casi specifici di successioni ricorsive lineari
> 
> - Se $b = 0$, allora si trova che $x_n = ax_{n-1}$, ovvero la successione geometrica $x_n = a^n x_0$, quindi
> 	- Se $x_0 = 0$, allora $x_n = 0$ per ogni $n \in \mathbb{N}$
> 	- Se $x_0 \ne 0$, allora
> 		$$
> 		\lim_n x_n = \begin{cases}
> 		+ \infty & \text{se } a>1 \land x_0 > 0 \\
> 		- \infty & \text{se } a>1 \land x_0 < 0 \\
> 		0 & \text{se } -1 < a < 1 \\
> 		\not\exists & \text{se } a < -1
> 		\end{cases}
> 		$$
> 		%%
> 		Fare il grafico a ragnatela dei vari casi
> 		%%
> - Se $b \ne 0$ allora
> 	- $a = 1$, allora $g(x) = x + b$ non ha punti fissi e la progressione è aritmetica:
> 		$$
> 		x_n = x_{n-1} + b
> 		$$
> 		e quindi
> 		$$
> 		\lim_n x_n = \begin{cases}
> 		+ \infty & \text{se } b > 0 \\
> 		- \infty & \text{se } b < 0
> 		\end{cases}
> 		$$
> 		(ovviamente se $b = 0$ diventa un punto fisso)
> 	- $a \ne 1$, allora $g(x) = ax+b$ e ha come unico punto fisso
> 		$$
> 		x^\star = ax^\star + b
> 		$$
> 		cioè
> 		$$
> 		x^\star = \dfrac{b}{1 - a}
> 		$$
> 		Definiamo ora
> 		$$
> 		y_n = x_n - x^\star
> 		$$
> 		e si ha che
> 		$$
> 		\begin{align*}
> 		y_n &= x_n - x^\star \\
> 		&= g(x_{n-1}) - x^\star \\
> 		&= ax_n + b - x^\star \\
> 		&= ay_n + ax^\star + b - x^\star \\
> 		&= ay_n
> 		\end{align*}
> 		$$
> 		da cui $y_n = a^ny_0$ è una successione geometrica con $y_0 = x_0 - x^\star$ e quindi
> 		$$
> 		x_n = a^n(x_0 - x^\star) + x^\star
> 		$$
> 		In particolare:
> 		- se $x_0 = x^\star$ allora $x_n = x^\star$ per ogni $n \in \mathbb{N}$
> 		- se $x_0 \ne x^\star$ allora
> 			$$
> 			\lim_n x_n = \begin{cases}
> 			+ \infty & \text{se } a > 1 \\
> 			x^\star & \text{se } -1 < a < 1 \\
> 			\not\exists & \text{se } a \le -1
> 			\end{cases}
> 			$$
> 			Il caso $a = 1$ l'abbiamo già visto prima
> 		Anche in questi casi si può visualizzare con il grafico a ragnatela.

## 4.3 - Successioni ricorsive non lineari

Ora vediamo il caso generale, ossia le successioni ricorsive%% link %% non [lineari](Limiti%20di%20successioni.md#^definizione-successione-ricorsiva-lineare).

In generale, non è possibile stabilire qual è il comportamento di una arbitraria [successione](Limiti%20di%20successioni.md#^definizione-successione) $\{ x_n \}$, ma in molti casi è possibile farlo se $x_0 \simeq x^\star$, cioè se prendiamo $x_0$ abbastanza vicino a $x^\star$, facendo così uno studio locale.

> [!definizione]+ Definizione: punto di equilibrio stabile
> 
> Data una successione ricorsiva%% link %% $\{ x_n \}$ con formula ricorsiva%% link %% $g$ e un [punto fisso](Limiti%20di%20successioni.md#^definizione-punto-fisso-o-punto-di-equilibrio-di-una-relazione-ricorsiva) $x^\star \in \mathbb{R}$ di $g$, diciamo che **$x^\star$ è un punto di equilibrio stabile** se
> 
> $$
> \forall \varepsilon > 0, \exists \delta > 0, \forall n \in \mathbb{N} . \big( |x_0 - x^\star| < \delta \implies |x_n - x^\star| < \varepsilon \big)
> $$
> 
> Altrimenti, si dice che **$x^\star$ è un punto di equilibrio instabile**.
^definizione-punto-di-equilibrio-stabile

%%
[!osservazione]+ Osservazione: significato di _punto di equilibrio stabile_
%%

> [!definizione]+ Definizione: punto di equilibrio asintoticamente stabile
> 
> Data una successione ricorsiva%% link %% $\{ x_n \}$ con formula ricorsiva%% link %% $g$ e un [punto fisso](Limiti%20di%20successioni.md#^definizione-punto-fisso-o-punto-di-equilibrio-di-una-relazione-ricorsiva) $x^\star \in \mathbb{R}$ di $g$, diciamo che **$x^\star$ è un punto di equilibrio asintoticamente stabile** se è [stabile](Limiti%20di%20successioni.md#^definizione-punto-di-equilibrio-stabile) e se
> 
> $$
> \exists \hat \delta > 0 . \left( |x_0 - x^\star| < \hat \delta \implies \lim_n x_n = x^\star \right)
> $$
^definizione-punto-di-equilibrio-asintoticamente-stabile

%% 
cioè se la condizione iniziale $x_0$ è sufficientemente vicina a $x^\star$ tale che $\{ x_n \}$ converge a $x^\star$
%%

%% 
Parallelismo tra stabiltà e pallina:
- una pallina su una collina è instabile perché basta un minimo tocco per farla scivolare giù dalla collina
- una pallina su un piano è stabile perché può muoversi e troverà un altro equilibrio
- una pallina in una conca è asintoticamente stabile perché comunque venga mossa tornerà sempre nel punto stabile
%%

%% 
[!osservazione]+ Osservazione

Nel caso delle [successioni ricorsive lineari](Limiti%20di%20successioni.md#^definizione-successione-ricorsiva-lineare) $g(x) = ax + b$ con $a \ne 1$ il [punto fisso](Limiti%20di%20successioni.md#^definizione-punto-fisso-o-punto-di-equilibrio-di-una-relazione-ricorsiva) $x^\star = \dfrac{b}{1-a}$ è
- [asintoticamente stabile](Limiti%20di%20successioni.md#^definizione-punto-di-equilibrio-asintoticamente-stabile) se $|a| < 1$ e in questo caso tutti gli $x_n$ convergono a $x^\star$
- [instabile](Limiti%20di%20successioni.md#^definizione-punto-di-equilibrio-stabile) se $|a| > 1$ e nessuna soluzione $x_n$ diversa da $x^\star$ rimane vicina a $x^\star$
 
 Il caso $g(x) = x$ (con $a = 1, b = 0$) dà invece luogo ad equilibri stabili ma non asintoticamente stabili
 %%

> [!teorema]+ Teorema di stabilità per linearizzazione
> 
> Data una successione ricorsiva%% link %% $\{ x_n \}$ con formula ricorsiva%% link %% $g$ e un [punto fisso](Limiti%20di%20successioni.md#^definizione-punto-fisso-o-punto-di-equilibrio-di-una-relazione-ricorsiva) $x^\star \in \mathbb{R}$ di $g$, allora:
> - Se $|g'(x^\star)| < 1$, allora $x^\star$ è [asintoticamente stabile](Limiti%20di%20successioni.md#^definizione-punto-di-equilibrio-asintoticamente-stabile).
> - Se $|g'(x^\star)| > 1$, allora $x^\star$ è [instabile](Limiti%20di%20successioni.md#^definizione-punto-di-equilibrio-stabile).
^teorema-di-stabilita-per-linearizzazione

%% 
Significato: nei casi non lineari, per vedere il loro comportamento si linearizza
%%

%%
[!osservazione]+ Osservazione

Il risultato è coerente con il caso lineare, infatti se $g(x) = ax + b$ allora $g'(x) = a$.
%%

> [!esempio]- Esempio del teorema di stabilità per linearizzazione
> 
> Dato un $g(x) = rx(1 - x)$ con $r > 0$. Per ragioni applicative ci limitiamo al caso $x \ge 0$.
> 
> Cerchiamo i punti fissi: $x^\star = rx^\star (1 - x^\star)$ e quindi $x^\star(1 - r + rx^\star) = 0$ e quindi
> - $x^\star_1 = 0$
> - $x^\star_2 = \dfrac{r-1}{r} = 1 - \dfrac{1}{r}$ (notare che $x^\star_2 \ge 0 \iff r \ge 1$)
> 
> Quindi se $0 < r < 1$ abbiamo che $x^\star_1 = 0$ è l'unico punto fisso.
> 
> Si ha $g'(x) = -2rx + r$ e quindi $g'(0) = r < 1$ dunque $x^\star_1$ è asintoticamente stabile. 
> 
> Notiamo che $\forall x_0 \in [0,1]$ abbiamo che $\lim_n x_n = x^\star_1 = 0$ e l'intervallo $[0,1]$ viene detto _bacino di attrazione_.
> 
> Vediamo invece che succede se $r = 2$: ora $g'(0) = 2 = r > 1$, quindi $x^\star_1 = 0$ è instabile. Anche partendo con $x_0$ vicino a $x^\star_1$, la successione si allontana e sembra convergere a $x^\star_2$. In effetti, se $1 < r < 3$, allora $g'(x^\star_2) = g'\left( 1 - \dfrac{1}{r} \right) = -2r\left( 1 - \dfrac{1}{r} \right) + r = -r + 2 \in (-1,1)$ quindi essendo $|g'(x^\star_2)| < 1$ abbiamo che $x^\star_2$ è asintoticamente stabile.
> 
> Per $r \ge 3$ si può invece verificare che sia $x^\star_1$ che $x^\star_2$ sono instabili: al crescere del parametro $r$, la dinamica diventa sempre più complicata (teoria del caos deterministico).

[!osservazione]+ Osservazione: applicazione delle successioni ricorsive nel merge sort

Vediamo ora un'applicazione delle successioni ricorsive%% link %% nel merge sort.

Determiniamo la complessità $T(n)$ del merge sort su un array di $n$ elementi, supponendo per semplicità

$$
n = 2^m
$$

così posso continuare a dividere l'array in due metà della stessa lunghezza.

Il merge sort ha costo $c \cdot n$ (con $c$ costante), dunque

$$
T(n) = 2T\left( \dfrac{n}{2} \right) + c \cdot n
$$

Quindi

$$
\begin{align*}
T(n) &= 2\left( 2T\left( \dfrac{n}{4} \right) + c \cdot \dfrac{n}{2} \right) + c \cdot n \\
&= 4 T \left( \dfrac{n}{4} \right) + 2 cn \\
&= 8T\left( \dfrac{n}{8} \right) + 3cn \\
&= 16T\left( \dfrac{n}{16} \right) + 4cn \\
&= \ldots \\
&= 2^m T\left( \dfrac{n}{2^m} \right) + mcn
\end{align*}
$$

Dato che nell'ipotesi iniziale $n = 2^m$, abbiamo che

$$
\begin{align*}
T(n) &= 2^m T(1) + mcn \\
&= T(1) n + c \log_2n \cdot n \\
&= O(n \log_2 n)
\end{align*}
$$

Quindi il merge sort ha complessità $O(n \log n)$ nel caso peggiore.

---

> [!fonti]+ Fonti
> 
> - 🏫 Corso di Laurea in Informatica (`L-31 R`) presso l'Università di Torino:
> 	- Corso di _Analisi Matematica - canale C_, A.A. 2020-21 ([pagina Moodle](https://informatica.i-learn.unito.it/course/view.php?id=2075)):
> 		- Prof. Boscaggin Alberto, videolezioni:
> 			- [_L13a_](https://informatica.i-learn.unito.it/local/streamingfilemanager/file.php/informatica.i-learn.unito.it/2075/L13a.mp4), [_L13b_](https://informatica.i-learn.unito.it/local/streamingfilemanager/file.php/informatica.i-learn.unito.it/2075/L13b.mp4).
> 			- [_L15a_](https://informatica.i-learn.unito.it/local/streamingfilemanager/file.php/informatica.i-learn.unito.it/2075/L15a.mp4), [_L15b_](https://informatica.i-learn.unito.it/local/streamingfilemanager/file.php/informatica.i-learn.unito.it/2075/L15b.mp4)%% relazioni per ricorrenza %%.
> 			- [_L16a_](https://informatica.i-learn.unito.it/local/streamingfilemanager/file.php/informatica.i-learn.unito.it/2075/L16a.mp4), [_L16b_](https://informatica.i-learn.unito.it/local/streamingfilemanager/file.php/informatica.i-learn.unito.it/2075/L16b.mp4)%% relazioni per ricorrenza %%.
> - 📚 Sergio Lancelotti, _Lezioni di Analisi Matematica I_, Celid, 2020 (ISBN: `978-8867891979`):
> 	- Capitolo 3 - _Limiti e continuità_:
> 		- 5 - _Limiti di successioni_.
