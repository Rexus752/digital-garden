---
aliases:
  - Espressioni regolari
---

> [!premessa]+ Premessa
> 
> Ciao! Se è la prima volta che capiti su questo sito, ti consiglio di consultare la [pagina principale](index.md) di questo _Giardino Digitale_ per scoprire meglio cos'è e come navigarlo.
> 
> Lo stato di questa nota è al momento: 🔴 <font color="#FF7F7F">_Bozza_</font>.

---

Abbiamo visto come sia possibile descrivere un [linguaggio regolare](Teoria%20degli%20automi.md#^definizione-linguaggio-regolare) attraverso un automa%% link %% ([DFA](Teoria%20degli%20automi.md#^definizione-automa-a-stati-finiti-deterministico-dfa), [NFA](Teoria%20degli%20automi.md#^definizione-automa-a-stati-finiti-non-deterministico-nfa) o [$\varepsilon$-NFA](Teoria%20degli%20automi.md#^definizione-automa-a-stati-finiti-deterministico-dfa)), basandoci sul [riconoscimento](Teoria%20degli%20automi.md#^definizione-linguaggio-riconosciuto-da-un-dfa) delle [stringhe](Teoria%20dei%20linguaggi%20formali.md#^definizione-stringa) fornite in ingresso all'automa%% link %%. Infatti, per [definizione di _linguaggio regolare_](Teoria%20degli%20automi.md#^definizione-linguaggio-regolare), un [linguaggio formale](Teoria%20dei%20linguaggi%20formali.md#^definizione-linguaggio-formale) $L$ è regolare se e solo se esiste un automa finito%% link %% che riconosce esattamente tutte e sole le [stringhe](Teoria%20dei%20linguaggi%20formali.md#^definizione-stringa) appartenenti a $L$. Questo approccio prende il nome di **approccio riconoscitivo**.

Esiste tuttavia un secondo modo per descrivere un [linguaggio regolare](Teoria%20degli%20automi.md#^definizione-linguaggio-regolare): l'**approccio generativo**. Anziché verificare se una [stringa](Teoria%20dei%20linguaggi%20formali.md#^definizione-stringa) appartiene a un [linguaggio](Teoria%20dei%20linguaggi%20formali.md#^definizione-linguaggio-formale), possiamo infatti descrivere direttamente l'[insieme](Teoria%20degli%20insiemi.md#^definizione-insieme) delle [stringhe](Teoria%20dei%20linguaggi%20formali.md#^definizione-stringa) che lo compongono, attraverso uno strumento chiamato [_espressione regolare_](Espressioni%20regolari.md#^definizione-espressione-regolare-regex).

> [!definizione]+ Definizione: espressione regolare
> 
> Dato un [alfabeto](Teoria%20dei%20linguaggi%20formali.md#^definizione-alfabeto) $\Sigma$, un'**espressione regolare su $\Sigma$** (anche detta **regex**, dall'inglese _**reg**ular **ex**pression_) è una notazione formale che permette di descrivere un [linguaggio regolare](Teoria%20degli%20automi.md#^definizione-linguaggio-regolare), definita induttivamente come segue:
> 1. $\emptyset$ è l'espressione regolare che descrive il [linguaggio vuoto](Teoria%20dei%20linguaggi%20formali.md#^definizione-linguaggio-vuoto) $\emptyset$.
> 2. $\varepsilon$ è l'espressione regolare che descrive il [linguaggio](Teoria%20dei%20linguaggi%20formali.md#^definizione-linguaggio-formale) $\{ \varepsilon \}$ contenente solo la [stringa vuota](Teoria%20dei%20linguaggi%20formali.md#^definizione-stringa-vuota) $\varepsilon$.
> 3. Per ogni [simbolo](Teoria%20dei%20linguaggi%20formali.md#^definizione-simbolo) $a \in \Sigma$, $a$ è un'espressione regolare che descrive il [linguaggio](Teoria%20dei%20linguaggi%20formali.md#^definizione-linguaggio-formale) $\{ a \}$ contenente solo il [simbolo](Teoria%20dei%20linguaggi%20formali.md#^definizione-simbolo) $a$.
> 4. Date due espressioni regolari $E$ ed $F$, anche $E+F$ è un'espressione regolare che descrive il [linguaggio](Teoria%20dei%20linguaggi%20formali.md#^definizione-linguaggio-formale) dato dall'[unione](Teoria%20degli%20insiemi.md#^definizione-unione-di-due-insiemi) dei [linguaggi](Teoria%20dei%20linguaggi%20formali.md#^definizione-linguaggio-formale) descritti da $E$ ed $F$.
> 5. Date due espressioni regolari $E$ ed $F$, anche $EF$ è un'espressione regolare che descrive il [linguaggio](Teoria%20dei%20linguaggi%20formali.md#^definizione-linguaggio-formale) dato dalla [concatenazione](Teoria%20dei%20linguaggi%20formali.md#^definizione-concatenazione-di-due-stringhe) dei [linguaggi](Teoria%20dei%20linguaggi%20formali.md#^definizione-linguaggio-formale) descritti da $E$ ed $F$.
> 6. Data un'espressione regolare $E$, anche $E^*$ è un'espressione regolare che descrive il [linguaggio](Teoria%20dei%20linguaggi%20formali.md#^definizione-linguaggio-formale) dato dalla [chiusura di Kleene](Teoria%20dei%20linguaggi%20formali.md#^definizione-chiusura-di-kleene-su-un-linguaggio) del [linguaggio](Teoria%20dei%20linguaggi%20formali.md#^definizione-linguaggio-formale) descritto da $E$.
> 
> Inoltre, per convenzione, gli operatori hanno il seguente ordine di precedenza, dal più basso al più alto:
> 1. [unione](Teoria%20degli%20insiemi.md#^definizione-unione-di-due-insiemi) $+$,
> 2. [concatenazione](Teoria%20dei%20linguaggi%20formali.md#^definizione-concatenazione-di-due-stringhe) e
> 3. [chiusura di Kleene](Teoria%20dei%20linguaggi%20formali.md#^definizione-chiusura-di-kleene-su-un-linguaggio) $^*$.
> 
> Le parentesi tonde $()$ possono essere utilizzate per specificare esplicitamente l'ordine delle operazioni e disambiguare la struttura di un'espressione regolare.
^definizione-espressione-regolare-regex

> [!osservazione]+ Osservazione: le espressioni regolari non sono linguaggi formali
> 
> Le [espressioni regolari](Espressioni%20regolari.md#^definizione-espressione-regolare-regex) non vanno confuse con i [linguaggi formali](Teoria%20dei%20linguaggi%20formali.md#^definizione-linguaggio-formale) che descrivono: sono **notazioni sintattiche**, ovvero "etichette" a cui associamo un determinato [linguaggio](Teoria%20dei%20linguaggi%20formali.md#^definizione-linguaggio-formale). Va quindi fatta una distinzione tra la _sintassi_%% link %% delle [espressioni regolari](Espressioni%20regolari.md#^definizione-espressione-regolare-regex), ossia il modo in cui vengono rappresentate come "etichette", e la loro _semantica_%% link %%, ossia il significato che queste etichette rappresentano, cioè i [linguaggi](Teoria%20dei%20linguaggi%20formali.md#^definizione-linguaggio-formale) che esse descrivono. Possiamo riassumere questa distinzione nella seguente tabella, dove in <font color="#FF7F7F">rosso</font> sono indicate le [espressioni regolari](Espressioni%20regolari.md#^definizione-espressione-regolare-regex) (cioè la loro sintassi%% Link %%) e in <font color="#7F7FFF">blu</font> i rispettivi [linguaggi](Teoria%20dei%20linguaggi%20formali.md#^definizione-linguaggio-formale) che descrivono (cioè la loro semantica%% Link %%):
> 
> | **Espressione regolare**         | **Linguaggio che descrive**                                                |
> | -------------------------------- | -------------------------------------------------------------------------- |
> | ${\color{#FF7F7F} \emptyset }$   | $L({\color{#FF7F7F} \emptyset }) = {\color{#7F7FFF} \emptyset }$           |
> | ${\color{#FF7F7F} \varepsilon }$ | $L({\color{#FF7F7F} \varepsilon }) = {\color{#7F7FFF} \{ \varepsilon \} }$ |
> | ${\color{#FF7F7F} a }$           | $L({\color{#FF7F7F} a }) = {\color{#7F7FFF} \{ a \} }$                     |
> | ${\color{#FF7F7F} E+F }$         | $L({\color{#FF7F7F} E+F }) = {\color{#7F7FFF} L(E) \cup L(F) }$            |
> | ${\color{#FF7F7F} EF }$          | $L({\color{#FF7F7F} EF }) = {\color{#7F7FFF} L(E)L(F) }$                   |
> | ${\color{#FF7F7F} E^* }$         | $L({\color{#FF7F7F} E^* }) = {\color{#7F7FFF} L(E)^* }$                    |
> 
> Per esempio, quando scriviamo che $\emptyset$ è un'[espressione regolare](Espressioni%20regolari.md#^definizione-espressione-regolare-regex), non stiamo affermando che sia il [linguaggio vuoto](Teoria%20dei%20linguaggi%20formali.md#^definizione-linguaggio-vuoto): stiamo utilizzando il simbolo $\emptyset$ come etichetta che denota proprio quel [linguaggio](Teoria%20dei%20linguaggi%20formali.md#^definizione-linguaggio-formale).

> [!esempio]- Esempi di espressioni regolari
> 
> Sono [espressioni regolari](Espressioni%20regolari.md#^definizione-espressione-regolare-regex) le seguenti:
> - $\text{ab+c}$, che seguendo le [regole di precedenza](Espressioni%20regolari.md#^definizione-espressione-regolare-regex) va interpretato come $(\text{ab})+\text{c}$, rappresenta il [linguaggio](Teoria%20dei%20linguaggi%20formali.md#^definizione-teoria-dei-linguaggi-formali)
> 	$$
> 	\begin{align*}
> 	L(\text{ab+c}) &= L(\text{ab}) \cup L(\text{c}) \\
> 	&= L(\text{a})L(\text{b}) \cup L(\text{c})
> 	\end{align*}
> 	$$
> - $01^*$, che seguendo le [regole di precedenza](Espressioni%20regolari.md#^definizione-espressione-regolare-regex) va interpretato come $0(1^*)$, rappresenta il [linguaggio](Teoria%20dei%20linguaggi%20formali.md#^definizione-linguaggio-formale)
> 	$$
> 	\begin{align*}
> 	L(01^*) &= L(0)L(1^*) \\
> 	&= L(0)\big( L(1)^* \big) 
> 	\end{align*}
> 	$$
> - $0 + 11^*$, che seguendo le [regole di precedenza](Espressioni%20regolari.md#^definizione-espressione-regolare-regex) va interpretato come $0 + (1(1)^*)$, rappresenta il [linguaggio](Teoria%20dei%20linguaggi%20formali.md#^definizione-linguaggio-formale)
> 	$$
> 	\begin{align*}
> 	L(0 + 11^*) &= L(0) \cup L(11^*) \\
> 	&= L(0) \cup L(1)L(1^*) \\
> 	&= L(0) \cup L(1)\big( L(1)^* \big)  \\
> 	\end{align*}
> 	$$

---

> [!fonti]+ Fonti
> 
> - 🏫 Corso di Laurea in Informatica (`L-31 R`) presso l'Università di Torino:
>     - Corso di _Linguaggi Formali e Traduttori_ (`INF0344`), A.A. 2026-27 ([pagina Moodle](https://informatica.i-learn.unito.it/course/view.php?id=3735)):
> 		- Prof. Jeremy James Sproston, slide del corso:
> 			- [2.4 - RE](https://informatica.i-learn.unito.it/pluginfile.php/514089/mod_folder/content/0/2-4_re.pdf).
