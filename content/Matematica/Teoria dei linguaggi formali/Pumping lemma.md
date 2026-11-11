---
aliases:
  - Pumping lemma
---

> [!premessa]+ Premessa
> 
> Ciao! Se è la prima volta che capiti su questo sito, ti consiglio di consultare la [pagina principale](index.md) di questo _Giardino Digitale_ per scoprire meglio cos'è e come navigarlo.
> 
> Lo stato di questa nota è al momento: 🔴 <font color="#FF7F7F">_Bozza_</font>.

---

Per dimostrare che un [linguaggio formale](Teoria%20dei%20linguaggi%20formali.md#^definizione-linguaggio-formale) è [regolare](Espressioni%20regolari.md#^definizione-linguaggio-regolare), basta trovare un automa a stati finiti%% Link %% ([DFA](Teoria%20degli%20automi.md#^definizione-automa-a-stati-finiti-deterministico-dfa), [NFA](Teoria%20degli%20automi.md#^definizione-automa-a-stati-finiti-non-deterministico-nfa) o [$\varepsilon$-NFA](Teoria%20degli%20automi.md#^definizione-automa-a-stati-finiti-non-deterministico-con-e-transizioni-enfa)) che lo [riconosce](Teoria%20degli%20automi.md#^definizione-linguaggio-riconosciuto-da-un-enfa), oppure un'[espressione regolare](Espressioni%20regolari.md#^definizione-espressione-regolare-regex) che lo [genera](Espressioni%20regolari.md#^definizione-linguaggio-generato-da-un-espressione-regolare).

Tuttavia, l'incapacità di trovare tale automa%% link %% o [espressione](Espressioni%20regolari.md#^definizione-espressione-regolare-regex) non è una dimostrazione diretta del fatto che il [linguaggio](Teoria%20dei%20linguaggi%20formali.md#^definizione-linguaggio-formale) non sia [regolare](Espressioni%20regolari.md#^definizione-linguaggio-regolare) (?).

Per dimostrare la [regolarità di un linguaggio](Espressioni%20regolari.md#^definizione-linguaggio-regolare), introduciamo una proprietà%% link %% $P$ che tutti i [linguaggi regolari](Espressioni%20regolari.md#^definizione-linguaggio-regolare) devono necessariamente soddisfare:

$$
L \text{ è regolare} \implies L \text{ soddisfa } P
$$

Per contrapposizione%% Link %%, quindi, abbiamo che se $L$ **non** soddisfa questa proprietà%% Link %% $P$, allora $L$ **non** è [regolare](Espressioni%20regolari.md#^definizione-linguaggio-regolare):

$$
L\ \mathbf{non} \text{ soddisfa } P \implies L \ \mathbf{non} \text{ è regolare}
$$

Questa proprietà%% link %% $P$ è rappresentata dal [_pumping lemma_](Pumping%20lemma.md#^teorema-pumping-lemma-linguaggi-regolari), che fornisce una condizione _necessaria_ ma non _sufficiente_ per la [regolarità](Espressioni%20regolari.md#^definizione-linguaggio-regolare):

$$
\{ \text{Linguaggi regolari} \}\ \subsetneq \left\{ \begin{array}{}
\text{Linguaggi che soddisfano} \\
\text{il pumping lemma}
\end{array} \right\} 
$$

> [!teorema]+ Teorema: pumping lemma per i linguaggi regolari
> 
> Per ogni [linguaggio regolare](Espressioni%20regolari.md#^definizione-linguaggio-regolare) $L$ esiste una costante $n \in \mathbb{N}$ tale che ogni [stringa](Teoria%20dei%20linguaggi%20formali.md#^definizione-stringa) $w \in L$ con [lunghezza](Teoria%20dei%20linguaggi%20formali.md#^definizione-lunghezza-di-una-stringa) $|w| \geq n$ può essere suddivisa in tre [sottostringhe](Teoria%20dei%20linguaggi%20formali.md#^definizione-stringa) $x$, $y$ e $z$ tali che $w = xyz$, in modo che:
> 1. La [sottostringa](Teoria%20dei%20linguaggi%20formali.md#^definizione-sottostringa-di-una-stringa) $y$ non è [vuota](Teoria%20dei%20linguaggi%20formali.md#^definizione-stringa-vuota):
> 	$$
> 	y \neq \varepsilon
> 	$$
> 2. La [sottostringa](Teoria%20dei%20linguaggi%20formali.md#^definizione-sottostringa-di-una-stringa) $y$ si trova interamente all'interno dei primi $n$ [simboli](Teoria%20dei%20linguaggi%20formali.md#^definizione-simbolo) della [stringa](Teoria%20dei%20linguaggi%20formali.md#^definizione-stringa), ossia la [lunghezza](Teoria%20dei%20linguaggi%20formali.md#^definizione-lunghezza-di-una-stringa) di $x$ e $y$ [concatenati](Teoria%20dei%20linguaggi%20formali.md#^definizione-concatenazione-di-due-stringhe) non supera $n$:
> 	$$
> 	|xy| \leq n
> 	$$
> 3. La [sottostringa](Teoria%20dei%20linguaggi%20formali.md#^definizione-sottostringa-di-una-stringa) $y$ può essere ripetuta un numero arbitrario di volte oppure eliminata del tutto ottenendo sempre una [stringa](Teoria%20dei%20linguaggi%20formali.md#^definizione-stringa) appartenente a $L$:
> 	$$
> 	\forall k \ge 0 . (xy^kz \in L)
> 	$$
> 
> > [!dimostrazione]- Dimostrazione
> > 
> > Se $L$ è un [linguaggio regolare](Teoria%20degli%20automi.md#^definizione-linguaggio-regolare-riconosciuto-da-un-dfa) allora esiste un [DFA](Teoria%20degli%20automi.md#^definizione-automa-a-stati-finiti-deterministico-dfa) $\mathcal{D} = \langle \Sigma, Q, \delta, q_0, F \rangle$ che lo [riconosce](Teoria%20degli%20automi.md#^definizione-linguaggio-riconosciuto-da-un-dfa):
> > 
> > $$
> > L = L(\mathcal{D})
> > $$
> > 
> > Poniamo $n = |Q| = |\{ q_0, q_1, \ldots, q_{n-1} \}|$, ovvero $n$ è il numero di [stati](Teoria%20degli%20automi.md#^definizione-automa-a-stati-finiti-deterministico-dfa) del [DFA](Teoria%20degli%20automi.md#^definizione-automa-a-stati-finiti-deterministico-dfa) $\mathcal{D}$. Prendiamo una [stringa](Teoria%20dei%20linguaggi%20formali.md#^definizione-stringa) $w \in L$ tale che la sua [lunghezza](Teoria%20dei%20linguaggi%20formali.md#^definizione-lunghezza-di-una-stringa) $|w| = m \ge n$: deve essere
> > 
> > $$
> > w = a_1a_2\ldots a_m
> > $$
> > 
> > Rappresentiamo il cammino fatto dal [DFA](Teoria%20degli%20automi.md#^definizione-automa-a-stati-finiti-deterministico-dfa) $\mathcal{D}$ per [riconoscere](Teoria%20degli%20automi.md#^definizione-linguaggio-riconosciuto-da-un-dfa) la [stringa](Teoria%20dei%20linguaggi%20formali.md#^definizione-stringa) $w$ come segue, indicando con $q_i$ lo [stato](Teoria%20degli%20automi.md#^definizione-automa-a-stati-finiti-deterministico-dfa) raggiunto dopo aver letto i primi $i$ [simboli](Teoria%20dei%20linguaggi%20formali.md#^definizione-simbolo) di $w$ (con $q_0$ corrispondente allo [stato iniziale](Teoria%20degli%20automi.md#^definizione-automa-a-stati-finiti-deterministico-dfa)):
> > 
> > ![dimostrazione-pumping-lemma](dimostrazione-pumping-lemma.svg)
> > 
> > Notiamo che questo cammino passa attraverso $m+1$ [stati](Teoria%20degli%20automi.md#^definizione-automa-a-stati-finiti-deterministico-dfa) (non necessariamente distinti perché, essendo un [DFA](Teoria%20degli%20automi.md#^definizione-automa-a-stati-finiti-deterministico-dfa) qualsiasi, non possiamo escludere che uno stato possa essere visitato più di una volta).
> > 
> > Dal momento che $m \geq n$, per le proprietà delle disuguaglianze%% link %% abbiamo anche che
> > 
> > $$
> > m \geq n \implies m+1 \ge n+1
> > $$
> > 
> > quindi se il cammino attraversa esattamente $m+1$ stati allora ne attraverserà almeno $n+1$.
> > 
> > Se il [DFA](Teoria%20degli%20automi.md#^definizione-automa-a-stati-finiti-deterministico-dfa) attraversa almeno $n+1$ stati ma ne possiede soltanto $n$ distinti, allora per il principio dei cassetti%% link %% almeno uno stato deve essere visitato più di una volta. Indichiamo con $q_i$ e $q_j$ due visite allo stesso stato, in cui la prima visita è $q_i$ e, dopo $j-i$ simboli, viene visitato una seconda volta, indicando questa seconda visita con $q_j$:
> > 
> > $$
> > q_i = q_j
> > $$
> > 
> > con $0 \leq i < j \leq n$.
> > 
> > Il cammino fatto dal [DFA](Teoria%20degli%20automi.md#^definizione-automa-a-stati-finiti-deterministico-dfa) $\mathcal{D}$ si può rappresentare così:
> > 
> > ![dimostrazione-pumping-lemma-2](dimostrazione-pumping-lemma-2.svg)
> > 
> > Presupponendo che $q_i = q_j$ sia il **primo** [stato](Teoria%20degli%20automi.md#^definizione-automa-a-stati-finiti-deterministico-dfa) che si ripete in questo cammino (ma ce ne possono essere anche altri tra $q_i=q_j$ e $q_m$), possiamo rappresentare il cammino fatto dal [DFA](Teoria%20degli%20automi.md#^definizione-automa-a-stati-finiti-deterministico-dfa) $\mathcal{D}$ anche così:
> > 
> > ![dimostrazione-pumping-lemma-3](dimostrazione-pumping-lemma-3.svg)
> > 
> > Possiamo quindi suddividere $w$ in tre [sottostringhe](Teoria%20dei%20linguaggi%20formali.md#^definizione-sottostringa-di-una-stringa) $x$, $y$ e $z$ tali che $w = xyz$, dove $x$ contiene i primi $i$ simboli, $y$ contiene i successivi $j-i$ simboli e $z$ contiene i rimanenti $m-j$ simboli:
> > 
> > $$
> > \begin{aligned}
> > x &= a_1a_2\ldots a_i\\
> > y &= a_{i+1}a_{i+2}\ldots a_j\\
> > z &= a_{j+1}a_{j+2}\ldots a_m
> > \end{aligned}
> > $$
> > 
> > In questo modo, il nostro [DFA](Teoria%20degli%20automi.md#^definizione-automa-a-stati-finiti-deterministico-dfa) $\mathcal{D}$ diventa
> > 
> > ![dimostrazione-pumping-lemma-4](dimostrazione-pumping-lemma-4.svg)
> > 
> > e notiamo che:
> > 1. La [condizione 1 del pumping lemma](Pumping%20lemma.md#^teorema-pumping-lemma-linguaggi-regolari) ($y \ne \varepsilon$) è rispettata, in quanto avendo che $i < j$ sappiamo che in $y$ c'è almeno un [simbolo](Teoria%20dei%20linguaggi%20formali.md#^definizione-simbolo).
> > 2. La [condizione 2 del pumping lemma](Pumping%20lemma.md#^teorema-pumping-lemma-linguaggi-regolari) ($|xy| \le n$) è rispettata in quanto, per costruzione, la [sottostringa](Teoria%20dei%20linguaggi%20formali.md#^definizione-sottostringa-di-una-stringa) $xy$ contiene i primi $j$ [simboli](Teoria%20dei%20linguaggi%20formali.md#^definizione-simbolo) di $w$, dove $j$ è l'indice della seconda visita che facciamo allo stato $q_i=q_j$. Poiché, come avevamo già dedotto prima, questa seconda visita avviene entro le prime $n+1$ visite agli stati, sappiamo che sicuramente $j \le n$ e, di conseguenza, $|xy| = j \le n$.
> > 3. La [condizione 3 del pumping lemma](Pumping%20lemma.md#^teorema-pumping-lemma-linguaggi-regolari) ($\forall k \ge 0 . (xy^kz \in L)$) è rispettata, in quanto leggendo la [stringa](Teoria%20dei%20linguaggi%20formali.md#^definizione-stringa) $xy^kz$ il [DFA](Teoria%20degli%20automi.md#^definizione-automa-a-stati-finiti-deterministico-dfa) compie il seguente percorso:
> > 	* Leggendo $x$, il [DFA](Teoria%20degli%20automi.md#^definizione-automa-a-stati-finiti-deterministico-dfa) parte dallo stato iniziale $q_0$ e arriva allo stato $q_i$.
> > 	* Leggendo $y$, il [DFA](Teoria%20degli%20automi.md#^definizione-automa-a-stati-finiti-deterministico-dfa) compie un ciclo che parte dallo stato $q_i$ e ritorna allo stato $q_i$ stesso (poiché $q_i = q_j$). Ripetendo $y$ per $k$ volte ($y^k$), l'automa percorre questo ciclo $k$ volte, rimanendo sempre nello stato $q_i$.
> > 	* Leggendo $z$, il [DFA](Teoria%20degli%20automi.md#^definizione-automa-a-stati-finiti-deterministico-dfa) parte dallo stato $q_i$ e raggiunge uno stato di accettazione (in quanto la [stringa](Teoria%20dei%20linguaggi%20formali.md#^definizione-stringa) originaria $w = xyz$ apparteneva a $L$ e veniva quindi riconosciuta).  
> > 	
> > 	Poiché l'automa termina la lettura di $xy^kz$ sempre nello [stato finale](Teoria%20degli%20automi.md#^definizione-automa-a-stati-finiti-deterministico-dfa) $q_m$ a prescindere dal valore di $k$, la stringa $xy^kz$ viene [riconosciuta](Teoria%20degli%20automi.md#^definizione-linguaggio-riconosciuto-da-un-dfa) dal [DFA](Teoria%20degli%20automi.md#^definizione-automa-a-stati-finiti-deterministico-dfa) $\mathcal{D}$ e appartiene pertanto a $L$ per ogni $k \ge 0$.
> > 
> > Avendo dimostrato tutte e tre le [condizioni del pumping lemma](Pumping%20lemma.md#^teorema-pumping-lemma-linguaggi-regolari), abbiamo dimostrato il [pumping lemma](Pumping%20lemma.md#^teorema-pumping-lemma-linguaggi-regolari) stesso.
> > 
> > $\blacksquare$
^teorema-pumping-lemma-linguaggi-regolari

Capire nei dettagli la dimostrazione di questo teorema ha portato via 3 ore del mio tempo.

> [!esempio]- Esempio: $\color{#7F7FFF} \text{a}^k\text{b}^k$ non è regolare
> 
> Dimostriamo che il [linguaggio formale](Teoria%20dei%20linguaggi%20formali.md#^definizione-linguaggio-formale) $L = \{ \text{a}^k\text{b}^k \mid k \ge 0 \}$ **non** è [regolare](Espressioni%20regolari.md#^definizione-linguaggio-generato-da-un-espressione-regolare) facendo vedere che per $L$ il [pumping lemma](Pumping%20lemma.md#^teorema-pumping-lemma-linguaggi-regolari) **non** vale.
> 
> Supponiamo, per assurdo, che esista una costante $n \in \mathbb{N}$ con le proprietà enunciate nel [pumping lemma](Pumping%20lemma.md#^teorema-pumping-lemma-linguaggi-regolari): prendiamo quindi per esempio la [stringa](Teoria%20dei%20linguaggi%20formali.md#^definizione-stringa) $w = \text{a}^n\text{b}^n \in L$ e che ha [lunghezza](Teoria%20dei%20linguaggi%20formali.md#^definizione-lunghezza-di-una-stringa) $|w| = 2n \ge n$.
> 
> Devono esistere allora tre [sottostringhe](Teoria%20dei%20linguaggi%20formali.md#^definizione-sottostringa-di-una-stringa) ${\color{#FF7F7F} x }$, ${\color{#7FFF7F} y }$ e ${\color{#7F7FFF} z }$ tali che $w = {\color{#FF7F7F} x }{\color{#7FFF7F} y }{\color{#7F7FFF} z }$ e che soddisfano le [tre condizioni del pumping lemma](Pumping%20lemma.md#^teorema-pumping-lemma-linguaggi-regolari): in particolare:
> - Dalla [condizione 2](Pumping%20lemma.md#^teorema-pumping-lemma-linguaggi-regolari) ($|xy| \leq n$) sappiamo che ${\color{#FF7F7F} x }$ e ${\color{#7FFF7F} y }$ sono composte di sole $\text{a}$ perché i primi $n$ [simboli](Teoria%20dei%20linguaggi%20formali.md#^definizione-simbolo) di $w = \text{a}^n\text{b}^n$ sono $\text{a}$:
> 	$$
> 	w = \underbrace{{\color{#FF7F7F} \text{aa} \ldots \text{a} }{\color{#7FFF7F} \text{aa} \ldots \text{a} }}_{\text{al max }n\text{ volte}} {\color{#7F7FFF} z }
> 	$$
> - Dalla [condizione 1](Pumping%20lemma.md#^teorema-pumping-lemma-linguaggi-regolari) (${\color{#7FFF7F} y } \ne \varepsilon$) sappiamo che ${\color{#7FFF7F} y }$ contiene almeno una $\text{a}$:
> 	$$
> 	{\color{#7FFF7F} y = \text{a}^m }
> 	$$
> 	(con $m \ge 1$).
> - Dalla [condizione 3](Pumping%20lemma.md#^teorema-pumping-lemma-linguaggi-regolari) ($\forall k \ge 0 . ({\color{#FF7F7F} x }{\color{#7FFF7F} y^k }{\color{#7F7FFF} z } \in L)$) sappiamo che ${\color{#FF7F7F} x }{\color{#7F7FFF} z } \in L$ (con ${\color{#7FFF7F} y^k }$ avente $k = 0$).
> 
> Abbiamo quindi che
> 
> $$
> w = \underbrace{
> {\color{#FF7F7F} \underbrace{\text{aa}\ldots\text{a}}_{n-m \text{ volte}} }
> {\color{#7FFF7F} \underbrace{\text{aa}\ldots\text{a}}_{m \text{ volte}} }
> }_{n \text{ volte}}
> {\color{#7F7FFF} \underbrace{\text{bb}\ldots\text{b}}_{n \text{ volte}} }
> $$
> 
> Poiché ${\color{#7FFF7F} y = \text{a}^m }$ con $m \geq 1$, eliminando $y$ otteniamo una [stringa](Teoria%20dei%20linguaggi%20formali.md#^definizione-stringa)
> 
> $$
> w = 
> {\color{#FF7F7F} \underbrace{\text{aa}\ldots\text{a}}_{n-m \text{ volte}} }
> {\color{#7F7FFF} \underbrace{\text{bb}\ldots\text{b}}_{n \text{ volte}} }
> $$
> 
> che contiene ${\color{#FF7F7F} n-m }$ volte $\text{a}$ e ${\color{#7F7FFF} n }$ volte $\text{b}$. Pertanto, il numero di [simboli](Teoria%20dei%20linguaggi%20formali.md#^definizione-simbolo) $\text{a}$ e $\text{b}$ non è uguale, contraddicendo la definizione del [linguaggio](Teoria%20dei%20linguaggi%20formali.md#^definizione-linguaggio-formale) $L$.

---

> [!fonti]+ Fonti
> 
> - 🏫 Corso di Laurea in Informatica (`L-31 R`) presso l'Università di Torino:
>     - Corso di _Linguaggi Formali e Traduttori_ (`INF0344`), A.A. 2026-27 ([pagina Moodle](https://informatica.i-learn.unito.it/course/view.php?id=3735)):
> 		- Prof. Jeremy James Sproston, slide del corso:
> 			- [2.6 - _Pumping lemma per i linguaggi regolari_](https://informatica.i-learn.unito.it/pluginfile.php/514089/mod_folder/content/0/2-6_pumping_lr.pdf).
