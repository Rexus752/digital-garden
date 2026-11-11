---
aliases:
  - Espressioni regolari
---

> [!premessa]+ Premessa
> 
> Ciao! Se è la prima volta che capiti su questo sito, ti consiglio di consultare la [pagina principale](index.md) di questo _Giardino Digitale_ per scoprire meglio cos'è e come navigarlo.
> 
> Lo stato di questa nota è al momento: 🟡 <font color="#FFFF7F">_Incompleta_</font>.

---

Abbiamo visto come sia possibile descrivere un [linguaggio regolare](Teoria%20degli%20automi.md#^definizione-linguaggio-regolare) attraverso un automa%% link %% ([DFA](Teoria%20degli%20automi.md#^definizione-automa-a-stati-finiti-deterministico-dfa), [NFA](Teoria%20degli%20automi.md#^definizione-automa-a-stati-finiti-non-deterministico-nfa) o [$\varepsilon$-NFA](Teoria%20degli%20automi.md#^definizione-automa-a-stati-finiti-deterministico-dfa)), basandoci sul [riconoscimento](Teoria%20degli%20automi.md#^definizione-linguaggio-riconosciuto-da-un-dfa) delle [stringhe](Teoria%20dei%20linguaggi%20formali.md#^definizione-stringa) fornite in ingresso all'automa%% link %%. Infatti, per [definizione di _linguaggio regolare_](Teoria%20degli%20automi.md#^definizione-linguaggio-regolare), un [linguaggio formale](Teoria%20dei%20linguaggi%20formali.md#^definizione-linguaggio-formale) $L$ è regolare se e solo se esiste un automa finito%% link %% che riconosce esattamente tutte e sole le [stringhe](Teoria%20dei%20linguaggi%20formali.md#^definizione-stringa) appartenenti a $L$. Questo approccio prende il nome di **approccio riconoscitivo**.

Esiste tuttavia un secondo modo per descrivere un [linguaggio regolare](Teoria%20degli%20automi.md#^definizione-linguaggio-regolare): l'**approccio descrittivo** (o **generativo**). Anziché verificare se una [stringa](Teoria%20dei%20linguaggi%20formali.md#^definizione-stringa) appartiene a un [linguaggio](Teoria%20dei%20linguaggi%20formali.md#^definizione-linguaggio-formale), possiamo infatti descrivere direttamente l'[insieme](Teoria%20degli%20insiemi.md#^definizione-insieme) delle [stringhe](Teoria%20dei%20linguaggi%20formali.md#^definizione-stringa) che lo compongono, attraverso uno strumento chiamato [_espressione regolare_](Espressioni%20regolari.md#^definizione-espressione-regolare-regex).

> [!definizione]+ Definizione: espressione regolare
> 
> Dato un [alfabeto](Teoria%20dei%20linguaggi%20formali.md#^definizione-alfabeto) $\Sigma$, un'**espressione regolare su $\Sigma$** (anche detta **regex**, dall'inglese _**reg**ular **ex**pression_) è una notazione formale che permette di descrivere un [linguaggio regolare](Teoria%20degli%20automi.md#^definizione-linguaggio-regolare), definita induttivamente come segue:
> 1. $\emptyset$ è l'espressione regolare che descrive il [linguaggio vuoto](Teoria%20dei%20linguaggi%20formali.md#^definizione-linguaggio-vuoto) $\emptyset$.
> 2. $\varepsilon$ è l'espressione regolare che descrive il [linguaggio](Teoria%20dei%20linguaggi%20formali.md#^definizione-linguaggio-formale) $\{ \varepsilon \}$ contenente solo la [stringa vuota](Teoria%20dei%20linguaggi%20formali.md#^definizione-stringa-vuota) $\varepsilon$.
> 3. Per ogni [simbolo](Teoria%20dei%20linguaggi%20formali.md#^definizione-simbolo) $a \in \Sigma$, $a$ è un'espressione regolare che descrive il [linguaggio](Teoria%20dei%20linguaggi%20formali.md#^definizione-linguaggio-formale) $\{ a \}$ contenente solo il [simbolo](Teoria%20dei%20linguaggi%20formali.md#^definizione-simbolo) $a$.
> 4. Date due espressioni regolari $\mathcal{R}$ ed $\mathcal{S}$, anche $\mathcal{R}+\mathcal{S}$ è un'espressione regolare che descrive il [linguaggio](Teoria%20dei%20linguaggi%20formali.md#^definizione-linguaggio-formale) dato dall'[unione](Teoria%20degli%20insiemi.md#^definizione-unione-di-due-insiemi) dei [linguaggi](Teoria%20dei%20linguaggi%20formali.md#^definizione-linguaggio-formale) descritti da $\mathcal{R}$ ed $\mathcal{S}$.
> 5. Date due espressioni regolari $\mathcal{R}$ ed $\mathcal{S}$, anche $\mathcal{RS}$ è un'espressione regolare che descrive il [linguaggio](Teoria%20dei%20linguaggi%20formali.md#^definizione-linguaggio-formale) dato dalla [concatenazione](Teoria%20dei%20linguaggi%20formali.md#^definizione-concatenazione-di-due-linguaggi) dei [linguaggi](Teoria%20dei%20linguaggi%20formali.md#^definizione-linguaggio-formale) descritti da $\mathcal{R}$ ed $\mathcal{S}$.
> 6. Data un'espressione regolare $\mathcal{R}$, anche $\mathcal{R}^*$ è un'espressione regolare che descrive il [linguaggio](Teoria%20dei%20linguaggi%20formali.md#^definizione-linguaggio-formale) dato dalla [chiusura di Kleene](Teoria%20dei%20linguaggi%20formali.md#^definizione-chiusura-di-kleene-su-un-linguaggio) del [linguaggio](Teoria%20dei%20linguaggi%20formali.md#^definizione-linguaggio-formale) descritto da $\mathcal{R}$.
> 
> Inoltre, per convenzione, gli operatori hanno il seguente ordine di precedenza, dal più basso al più alto:
> 1. [unione](Teoria%20degli%20insiemi.md#^definizione-unione-di-due-insiemi) $+$,
> 2. [concatenazione](Teoria%20dei%20linguaggi%20formali.md#^definizione-concatenazione-di-due-linguaggi) e
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
> | ${\color{#FF7F7F} \mathcal{R}+\mathcal{S} }$         | $L({\color{#FF7F7F} \mathcal{R}+\mathcal{S} }) = {\color{#7F7FFF} L(\mathcal{R}) \cup L(\mathcal{S}) }$            |
> | ${\color{#FF7F7F} \mathcal{RS} }$          | $L({\color{#FF7F7F} \mathcal{RS} }) = {\color{#7F7FFF} L(\mathcal{R})L(\mathcal{S}) }$                   |
> | ${\color{#FF7F7F} \mathcal{R}^* }$         | $L({\color{#FF7F7F} \mathcal{R}^* }) = {\color{#7F7FFF} L(\mathcal{R})^* }$                    |
> 
> Per esempio, quando scriviamo che $\emptyset$ è un'[espressione regolare](Espressioni%20regolari.md#^definizione-espressione-regolare-regex), non stiamo affermando che sia il [linguaggio vuoto](Teoria%20dei%20linguaggi%20formali.md#^definizione-linguaggio-vuoto): stiamo utilizzando il simbolo $\emptyset$ come etichetta che denota proprio quel [linguaggio](Teoria%20dei%20linguaggi%20formali.md#^definizione-linguaggio-formale).

> [!esempio]- Esempi di espressioni regolari
> 
> Sono [espressioni regolari](Espressioni%20regolari.md#^definizione-espressione-regolare-regex) le seguenti:
> - $\text{ab}+\text{c}$, che seguendo le [regole di precedenza](Espressioni%20regolari.md#^definizione-espressione-regolare-regex) va interpretato come $(\text{ab})+\text{c}$, rappresenta il [linguaggio](Teoria%20dei%20linguaggi%20formali.md#^definizione-teoria-dei-linguaggi-formali)
> 	$$
> 	\begin{align*}
> 	L(\text{ab}+\text{c}) &= L(\text{ab}) \cup L(\text{c}) \\
> 	&= L(\text{a})L(\text{b}) \cup L(\text{c}) \\
> 	&= \{ \text{a} \}\{ \text{b} \} \cup \{ \text{c} \} \\
> 	&= \{ \text{ab} \} \cup \{ \text{c} \} \\
> 	&= \{ \text{ab}, \text{c} \}
> 	\end{align*}
> 	$$
> - $01^*$, che seguendo le [regole di precedenza](Espressioni%20regolari.md#^definizione-espressione-regolare-regex) va interpretato come $0(1^*)$, rappresenta il [linguaggio](Teoria%20dei%20linguaggi%20formali.md#^definizione-linguaggio-formale)
> 	$$
> 	\begin{align*}
> 	L(01^*) &= L(0)L(1^*) \\
> 	&= L(0)\big( L(1)^* \big) \\
> 	&= \{ 0 \}\{ \varepsilon, 1, 11, 111, \ldots \} \\
> 	&= \{ 0, 01, 011, 0111, \ldots \}
> 	\end{align*}
> 	$$
> - $0 + 11^*$, che seguendo le [regole di precedenza](Espressioni%20regolari.md#^definizione-espressione-regolare-regex) va interpretato come $0 + (1(1)^*)$, rappresenta il [linguaggio](Teoria%20dei%20linguaggi%20formali.md#^definizione-linguaggio-formale)
> 	$$
> 	\begin{align*}
> 	L(0 + 11^*) &= L(0) \cup L(11^*) \\
> 	&= L(0) \cup L(1)L(1^*) \\
> 	&= L(0) \cup L(1)\big( L(1)^* \big) \\
> 	&= \{ 0 \} \cup \{ 1 \}\{ \varepsilon, 1, 11, 111, \ldots \} \\
> 	&= \{ 0 \} \cup \{ 1, 11, 111, 1111, \ldots \} \\
> 	&= \{ 0, 1, 11, 111, 1111, \ldots \}
> 	\end{align*}
> 	$$

> [!definizione]+ Definizione: espressioni regolari equivalenti
> 
> Due [espressioni regolari](Espressioni%20regolari.md#^definizione-espressione-regolare-regex) $\mathcal{R}$ ed $\mathcal{S}$ si dicono **equivalenti** e si denotano come $\mathcal{R} = \mathcal{S}$ se descrivono lo stesso [linguaggio](Teoria%20dei%20linguaggi%20formali.md#^definizione-linguaggio-formale):
> 
> $$
> \mathcal{R} = \mathcal{S} \iff L(\mathcal{R}) = L(\mathcal{S})
> $$
^definizione-espressioni-regolari-equivalenti

> [!esercizio]+ Esercizio: linguaggio generato da espressioni regolari
> 
> Calcolare il [linguaggio](Teoria%20dei%20linguaggi%20formali.md#^definizione-linguaggio-formale) generato dalle seguenti [espressioni regolari](Espressioni%20regolari.md#^definizione-espressione-regolare-regex):
> 1. $(\text{a} + \text{b})^*$
> 2. $(\text{ab})^*$
> 3. $\text{a}^*\text{b}^*$
> 4. $0 + 11^*$
> 5. $(\text{abb}+\text{b})^*$
> 6. $(\text{a} + \text{b})^*\text{abb}(\text{a} + \text{b})^*$
> 
> > [!soluzione]- Soluzione 1: $(\text{a} + \text{b})^*$
> > 
> > L'[espressione regolare](Espressioni%20regolari.md#^definizione-espressione-regolare-regex) $(\text{a} + \text{b})^*$ genera il [linguaggio](Teoria%20dei%20linguaggi%20formali.md#^definizione-linguaggio-formale)
> > 
> > $$
> > \begin{align*}
> > L\big( (\text{a} + \text{b})^* \big) &= L(\text{a} + \text{b})^* \\
> > &= \big( L(\text{a}) \cup L(\text{b}) \big)^* \\
> > &= \big( \{ \text{a} \} \cup \{ \text{b} \} \big)^* \\
> > &= \{ \text{a}, \text{b} \}^* \\
> > &= \{ \varepsilon, \text{a}, \text{b}, \text{aa}, \text{ab}, \text{ba}, \text{bb}, \text{aaa}, \text{aab}, \ldots \}
> > \end{align*}
> > $$
> 
> > [!soluzione]- Soluzione 2: $(\text{ab})^*$
> > 
> > L'[espressione regolare](Espressioni%20regolari.md#^definizione-espressione-regolare-regex) $(\text{ab})^*$ genera il [linguaggio](Teoria%20dei%20linguaggi%20formali.md#^definizione-linguaggio-formale)
> > 
> > $$
> > \begin{align*}
> > L\big( (\text{ab})^* \big) &= L(\text{ab})^* \\
> > &= \big( L(\text{a})L(\text{b}) \big)^* \\
> > &= \big( \{ \text{a} \}\{ \text{b} \} \big)^* \\
> > &= \{ \text{ab} \}^* \\
> > &= \{ \varepsilon, \text{ab}, \text{abab}, \text{ababab}, \ldots \}
> > \end{align*}
> > $$
> 
> > [!soluzione]- Soluzione 3: $\text{a}^*\text{b}^*$
> > 
> > L'[espressione regolare](Espressioni%20regolari.md#^definizione-espressione-regolare-regex) $\text{a}^*\text{b}^*$ genera il [linguaggio](Teoria%20dei%20linguaggi%20formali.md#^definizione-linguaggio-formale)
> > 
> > $$
> > \begin{align*}
> > L(\text{a}^*\text{b}^*) &= L(\text{a}^*)L(\text{b}^*) \\
> > &= L(\text{a})^*L(\text{b})^* \\
> > &= \{ \text{a} \}^* \{ \text{b} \}^* \\
> > &= \{ \varepsilon, \text{a}, \text{aa}, \text{aaa}, \ldots \}\{ \varepsilon, \text{b}, \text{bb}, \text{bbb}, \ldots \} \\
> > &= \{ \varepsilon, \text{a}, \text{b}, \text{aa}, \text{ab}, \text{bb}, \text{aaa}, \text{aab}, \text{abb}, \text{bbb}, \ldots \}
> > \end{align*}
> > $$
> 
> > [!soluzione]- Soluzione 4: $0 + 11^*$
> > 
> > L'[espressione regolare](Espressioni%20regolari.md#^definizione-espressione-regolare-regex) $0 + 11^*$ genera il [linguaggio](Teoria%20dei%20linguaggi%20formali.md#^definizione-linguaggio-formale)
> > 
> > $$
> > \begin{align*}
> > L(0 + 11^*) &= L(0) \cup L(11^*) \\
> > &= L(0) \cup L(1)L(1^*) \\
> > &= \{ 0 \} \cup \{ 1 \}\{ \varepsilon, 1, 11, 111, \ldots \} \\
> > &= \{ 0 \} \cup \{ 1, 11, 111, 1111, \ldots \} \\
> > &= \{ 0, 1, 11, 111, 1111, \ldots \}
> > \end{align*}
> > $$
> 
> > [!soluzione]- Soluzione 5: $(\text{abb}+\text{b})^*$
> > 
> > L'[espressione regolare](Espressioni%20regolari.md#^definizione-espressione-regolare-regex) $(\text{abb}+\text{b})^*$ genera il [linguaggio](Teoria%20dei%20linguaggi%20formali.md#^definizione-linguaggio-formale)
> > 
> > $$
> > \begin{align*}
> > L\big( (\text{abb}+\text{b})^* \big) &= L(\text{abb}+\text{b})^* \\
> > &= \big( L(\text{abb}) \cup L(\text{b}) \big)^* \\
> > &= \big( L(\text{a})L(\text{b})L(\text{b}) \cup L(\text{b}) \big)^* \\
> > &= \big( \{ \text{a} \}\{ \text{b} \}\{ \text{b} \} \cup \{ \text{b} \} \big)^* \\
> > &= \big( \{ \text{abb} \} \cup \{ \text{b} \} \big)^* \\
> > &= \{ \text{abb}, \text{b} \}^* \\
> > &= \{ \varepsilon, \text{abb}, \text{b}, \text{abbabb}, \text{abbb}, \text{babb}, \text{bb}, \ldots \}
> > \end{align*}
> > $$
> 
> > [!soluzione]- Soluzione 6: $(\text{a} + \text{b})^*\text{abb}(\text{a} + \text{b})^*$
> > 
> > L'[espressione regolare](Espressioni%20regolari.md#^definizione-espressione-regolare-regex) $(\text{a} + \text{b})^*\text{abb}(\text{a} + \text{b})^*$ genera il [linguaggio](Teoria%20dei%20linguaggi%20formali.md#^definizione-linguaggio-formale)
> > 
> > $$
> > \begin{align*}
> > L\big( (\text{a} + \text{b})^*\text{abb}(\text{a} + \text{b})^* \big) &= L\big( (\text{a} + \text{b})^*\big)L(\text{abb})L\big( (\text{a} + \text{b})^*\big) \\
> > &= L(\text{a} + \text{b})^*L(\text{a})L(\text{b})L(\text{b}) L(\text{a} + \text{b})^* \\
> > &= \big( L(\text{a}) \cup L(\text{b}) \big)^* L(\text{a})L(\text{b})L(\text{b}) \big( L(\text{a}) \cup L(\text{b}) \big)^* \\
> > &= \big( \{ \text{a} \} \cup \{ \text{b} \} \big)^* \{ \text{a} \}\{ \text{b} \}\{ \text{b} \} \big( \{ \text{a} \} \cup \{ \text{b} \} \big)^* \\
> > &= \{ \text{a}, \text{b} \}^* \{ \text{abb} \} \{ \text{a}, \text{b} \}^* \\
> > &= {\color{#FF7F7F} \{ \varepsilon, \text{a}, \text{b}, \text{aa}, \text{ab}, \text{ba}, \text{bb}, \ldots \} }{\color{#7FFF7F} \{ \text{abb} \} } {\color{#7F7FFF} \{ \varepsilon, \text{a}, \text{b}, \text{aa}, \text{ab}, \text{ba}, \text{bb}, \ldots \} } \\
> > &= \{ {\color{#7FFF7F} \text{abb} }, {\color{#FF7F7F} \text{a} }{\color{#7FFF7F} \text{abb} }, {\color{#7FFF7F} \text{abb} }{\color{#7F7FFF} \text{a} }, {\color{#FF7F7F} \text{a} }{\color{#7FFF7F} \text{abb} }{\color{#7F7FFF} \text{a} }, \ldots,{\color{#FF7F7F} \text{b} }{\color{#7FFF7F} \text{abb} }{\color{#7F7FFF} \text{abb} },\ldots \}
> > \end{align*}
> > $$

%% 

\# Proprietà delle espressioni regolari

Unione
- commutatività: R + S = S + R
- associatività: R + (S + T) = (R + S) + T
- idempotenza: R + R = R
- identità: R + \emptyset = \emptyset + R = R

Concatenazione
- associatività: R(ST) = (RS)T
- identità: R ε = ε R = R
- assorbimento: R \emptyset = \emptyset R = \emptyset
- distributività sinistra sull’unione: R (S + T ) = RS + RT
- distributività destra sull’unione: (R + S )T = RT + ST

Chiusura di Kleene
- idempotenza: (R ∗)∗ = R ∗
- casi banali: ε∗ = \emptyset∗ = ε
%%

%% 
Definire espressioni regolari che generino i seguenti linguaggi:
1. stringhe di a, b e c che iniziano con due a e finiscono con due b
2. stringhe di 0 e 1 la cui lunghezza è un multiplo di 3
3. stringhe di 0 e 1 con un numero pari di 0
4. stringhe di a, b e c che non contengono la sottostringa ab
5. costanti numeriche binarie pari senza 0 inutili a sinistra (es. 0, 10, ma non 010 o 11)
6. costanti numeriche decimali con virgola facoltativa (es. 42, .5, 12.3, 12. ma non .)
%%

# 1 - Espressioni e linguaggi regolari

Abbiamo introdotto le [espressioni regolari](Espressioni%20regolari.md#^definizione-espressione-regolare-regex) come un modo alternativo agli automi%% link %% per poter definire un [linguaggio regolare](Teoria%20degli%20automi.md#^definizione-linguaggio-regolare).

> [!definizione]+ Definizione: linguaggio generato da un'espressione regolare
>
> Data un'[espressione regolare](Espressioni%20regolari.md#^definizione-espressione-regolare-regex) $\mathcal{R}$ su un [alfabeto](Teoria%20dei%20linguaggi%20formali.md#^definizione-alfabeto) $\Sigma$, il **linguaggio generato** (o **descritto** o **rappresentato**) da $\mathcal{R}$ è il [linguaggio formale](Teoria%20dei%20linguaggi%20formali.md#^definizione-linguaggio-formale) $L(\mathcal{R}) \subseteq \Sigma^*$ costituito da tutte e sole le [stringhe](Teoria%20dei%20linguaggi%20formali.md#^definizione-stringa) generate da $\mathcal{R}$:
>
> $$ 
> L(\mathcal{R}) = \{w \in \Sigma^* \mid w \text{ è generata da } \mathcal{R}\}
> $$
^definizione-linguaggio-generato-da-un-espressione-regolare

> [!definizione]+ Definizione: linguaggio regolare
> 
> Un [linguaggio](Teoria%20dei%20linguaggi%20formali.md#^definizione-linguaggio-formale) $L$ si dice **regolare** se esiste un'[espressione regolare](Espressioni%20regolari.md#^definizione-espressione-regolare-regex) $\mathcal{R}$ per cui è il suo [linguaggio generato](Espressioni%20regolari.md#^definizione-linguaggio-generato-da-un-espressione-regolare):
> 
> $$
> L = L(\mathcal R)
> $$
^definizione-linguaggio-regolare

> [!teorema]+ Teorema: da DFA a regex
> 
> Dato un [DFA](Teoria%20degli%20automi.md#^definizione-automa-a-stati-finiti-deterministico-dfa) $\cal D$, esiste una [regex](Espressioni%20regolari.md#^definizione-espressione-regolare-regex) $\mathcal{R}$ tale che il [linguaggio](Teoria%20dei%20linguaggi%20formali.md#^definizione-linguaggio-formale) $L(\mathcal{D})$ [riconosciuto](Teoria%20degli%20automi.md#^definizione-linguaggio-riconosciuto-da-un-dfa) da $\mathcal{D}$ è uguale al [linguaggio](Teoria%20dei%20linguaggi%20formali.md#^definizione-linguaggio-formale) $L(\mathcal{R})$ [generato](Espressioni%20regolari.md#^definizione-linguaggio-generato-da-un-espressione-regolare) da $\mathcal{R}$:
> 
> $$
> \forall \mathcal{D}, \exists \mathcal{R} . \big( 
> L(\mathcal{D}) = L(\mathcal{R}) \big) 
> $$
^teorema-da-dfa-a-regex

%% 
Dimostrazione
Si veda la Sez. 3.2.1 del libro (lettura facoltativa)
%%

> [!teorema]+ Teorema: da regex a $\color{#FF3F3F} \varepsilon$-NFA
> 
> Dato una [regex](Espressioni%20regolari.md#^definizione-espressione-regolare-regex) $\mathcal{R}$, esiste un [$\varepsilon$-NFA](Teoria%20degli%20automi.md#^definizione-automa-a-stati-finiti-non-deterministico-con-e-transizioni-enfa) $\mathcal{E}$ tale che il [linguaggio](Teoria%20dei%20linguaggi%20formali.md#^definizione-linguaggio-formale) $L(\mathcal{R})$ [generato](Espressioni%20regolari.md#^definizione-linguaggio-generato-da-un-espressione-regolare) da $\mathcal{R}$ è uguale al [linguaggio](Teoria%20dei%20linguaggi%20formali.md#^definizione-linguaggio-formale) $L(\mathcal{E})$ [riconosciuto](Teoria%20degli%20automi.md#^definizione-linguaggio-riconosciuto-da-un-enfa) da $\mathcal{E}$:
> 
> $$
> \forall \mathcal{R}, \exists \mathcal{E} . \big( L(\mathcal{R}) = L(\mathcal{E}) \big) 
> $$
> 
> > [!dimostrazione]- Dimostrazione
> > 
> > Costruiamo l'[$\varepsilon$-NFA](Teoria%20degli%20automi.md#^definizione-automa-a-stati-finiti-non-deterministico-con-e-transizioni-enfa) $\mathcal{E}$ per induzione%% Link %% sulla struttura di $\mathcal{R}$ distinguendo i diversi casi in base alla forma che può assumere, come specificato nella [sua definizione](Espressioni%20regolari.md#^definizione-espressione-regolare-regex). Imporremo che ogni [$\varepsilon$-NFA](Teoria%20degli%20automi.md#^definizione-automa-a-stati-finiti-non-deterministico-con-e-transizioni-enfa) costruito abbia esattamente uno [stato iniziale](Teoria%20degli%20automi.md#^definizione-automa-a-stati-finiti-non-deterministico-con-e-transizioni-enfa) e uno [stato finale](Teoria%20degli%20automi.md#^definizione-automa-a-stati-finiti-non-deterministico-con-e-transizioni-enfa), in modo da semplificare la costruzione dei casi induttivi: potremo infatti combinare gli [$\varepsilon$-NFA](Teoria%20degli%20automi.md#^definizione-automa-a-stati-finiti-non-deterministico-con-e-transizioni-enfa) delle "[sottoespressioni regolari](Espressioni%20regolari.md#^definizione-espressione-regolare-regex)" mediante [$\varepsilon$-transizioni](Teoria%20degli%20automi.md#^definizione-automa-a-stati-finiti-non-deterministico-con-e-transizioni-enfa) che collegano direttamente i rispettivi stati iniziali e finali, senza dover gestire innumerevoli stati iniziali o finali.
> > 
> > Analizziamo quindi i [6 casi delle espressioni regolari](Espressioni%20regolari.md#^definizione-espressione-regolare-regex), verificando che ciascuna delle costruzioni soddisfi la proprietà richiesta, ovvero che il [linguaggio riconosciuto](Teoria%20degli%20automi.md#^definizione-linguaggio-riconosciuto-da-un-enfa) dall'[$\varepsilon$-NFA](Teoria%20degli%20automi.md#^definizione-automa-a-stati-finiti-non-deterministico-con-e-transizioni-enfa) $\mathcal{E}$ sia uguale al [linguaggio generato](Espressioni%20regolari.md#^definizione-linguaggio-generato-da-un-espressione-regolare) di $\mathcal{R}$:
> > 1. Caso $\emptyset$ (che descrive il [linguaggio vuoto](Teoria%20dei%20linguaggi%20formali.md#^definizione-linguaggio-vuoto) $\emptyset$):
> >    ![teorema-da-regex-a-enfa-linguaggio-vuoto](teorema-da-regex-a-enfa-linguaggio-vuoto.svg)
> >    L'[$\varepsilon$-NFA](Teoria%20degli%20automi.md#^definizione-automa-a-stati-finiti-non-deterministico-con-e-transizioni-enfa) non possiede alcuna [transizione](Teoria%20degli%20automi.md#^definizione-automa-a-stati-finiti-non-deterministico-con-e-transizioni-enfa) tra lo [stato iniziale](Teoria%20degli%20automi.md#^definizione-automa-a-stati-finiti-non-deterministico-con-e-transizioni-enfa) e quello [finale](Teoria%20degli%20automi.md#^definizione-automa-a-stati-finiti-non-deterministico-con-e-transizioni-enfa), perciò non esiste alcun percorso che permetta di raggiungere uno stato finale partendo da quello iniziale. Di conseguenza, non [riconosce](Teoria%20degli%20automi.md#^definizione-linguaggio-riconosciuto-da-un-enfa) alcuna [stringa](Teoria%20dei%20linguaggi%20formali.md#^definizione-stringa):
> > 	$$
> > 	L(\mathcal{E}) = \emptyset = L(\emptyset)
> > 	$$
> > 2. Caso $\varepsilon$ (che descrive il [linguaggio](Teoria%20dei%20linguaggi%20formali.md#^definizione-linguaggio-formale) $\{ \varepsilon \}$ contenente solo la [stringa vuota](Teoria%20dei%20linguaggi%20formali.md#^definizione-stringa-vuota) $\varepsilon$):
> >    ![teorema-da-regex-a-enfa-stringa-vuota](teorema-da-regex-a-enfa-stringa-vuota.svg)
> >    L'[$\varepsilon$-NFA](Teoria%20degli%20automi.md#^definizione-automa-a-stati-finiti-non-deterministico-con-e-transizioni-enfa) presenta un'[$\varepsilon$-transizione](Teoria%20degli%20automi.md#^definizione-automa-a-stati-finiti-non-deterministico-con-e-transizioni-enfa) dallo stato iniziale a quello finale, pertanto [riconosce](Teoria%20degli%20automi.md#^definizione-linguaggio-riconosciuto-da-un-enfa) esclusivamente la [stringa vuota](Teoria%20dei%20linguaggi%20formali.md#^definizione-stringa-vuota):
> > 	$$
> > 	L(\mathcal{E}) = \{\varepsilon\} = L(\varepsilon)
> > 	$$
> > 3. Caso $a$ (che descrive il [linguaggio](Teoria%20dei%20linguaggi%20formali.md#^definizione-linguaggio-formale) $\{ a \}$ contenente solo il [simbolo](Teoria%20dei%20linguaggi%20formali.md#^definizione-simbolo) $a \in \Sigma$):
> >    ![teorema-da-regex-a-enfa-simbolo-a](teorema-da-regex-a-enfa-simbolo-a.svg)
> > 	L'[$\varepsilon$-NFA](Teoria%20degli%20automi.md#^definizione-automa-a-stati-finiti-non-deterministico-con-e-transizioni-enfa) presenta una [transizione](Teoria%20degli%20automi.md#^definizione-automa-a-stati-finiti-non-deterministico-con-e-transizioni-enfa) etichettata con il [simbolo](Teoria%20dei%20linguaggi%20formali.md#^definizione-simbolo) $a$ dallo stato iniziale a quello finale. Pertanto, riconosce esclusivamente la [stringa](Teoria%20dei%20linguaggi%20formali.md#^definizione-stringa) costituita dal [simbolo](Teoria%20dei%20linguaggi%20formali.md#^definizione-simbolo) $a$:
> > 	$$
> > 	L(\mathcal{E}) = \{a\} = L(a)
> > 	$$
> > 4. Caso $\mathcal{R}_1+\mathcal{R}_2$ (che descrive il [linguaggio](Teoria%20dei%20linguaggi%20formali.md#^definizione-linguaggio-formale) dato dall'[unione](Teoria%20degli%20insiemi.md#^definizione-unione-di-due-insiemi) dei [linguaggi](Teoria%20dei%20linguaggi%20formali.md#^definizione-linguaggio-formale) descritti dalle [espressioni regolari](Espressioni%20regolari.md#^definizione-espressione-regolare-regex) $\mathcal{R}_1$ ed $\mathcal{R}_2$):
> >    ![teorema-da-regex-a-enfa-unione](teorema-da-regex-a-enfa-unione.svg)
> > 	Per ipotesi induttiva, esistono due [$\varepsilon$-NFA](Teoria%20degli%20automi.md#^definizione-automa-a-stati-finiti-non-deterministico-con-e-transizioni-enfa) $\mathcal{E}_1$ e $\mathcal{E}_2$ tali che:
> > 	
> > 	$$
> > 	\begin{aligned}
> > 	L(\mathcal{E}_1) &= L(\mathcal{R}_1) \\
> > 	L(\mathcal{E}_2) &= L(\mathcal{R}_2)
> > 	\end{aligned}
> > 	$$
> > 	
> > 	La costruzione introduce un nuovo stato iniziale e un nuovo stato finale, collegandoli rispettivamente agli stati iniziali e finali dei due [$\varepsilon$-NFA](Teoria%20degli%20automi.md#^definizione-automa-a-stati-finiti-non-deterministico-con-e-transizioni-enfa) mediante [$\varepsilon$-transizioni](Teoria%20degli%20automi.md#^definizione-automa-a-stati-finiti-non-deterministico-con-e-transizioni-enfa).
> > 	
> > 	Di conseguenza, una [stringa](Teoria%20dei%20linguaggi%20formali.md#^definizione-stringa) viene [riconosciuta](Teoria%20degli%20automi.md#^definizione-linguaggio-riconosciuto-da-un-enfa) se e solo se viene [riconosciuta](Teoria%20degli%20automi.md#^definizione-linguaggio-riconosciuto-da-un-enfa) da almeno uno dei due [$\varepsilon$-NFA](Teoria%20degli%20automi.md#^definizione-automa-a-stati-finiti-non-deterministico-con-e-transizioni-enfa) di partenza ($\mathcal{E}_1$ o $\mathcal{E}_2$). Pertanto:
> > 	
> > 	$$
> > 	\begin{aligned}
> > 	L(\mathcal{E})
> > 	&= L(\mathcal{E}_1) \cup L(\mathcal{E}_2) \\
> > 	&= L(\mathcal{R}_1) \cup L(\mathcal{R}_2) \\
> > 	&= L(\mathcal{R}_1+\mathcal{R}_2)
> > 	\end{aligned}
> > 	$$
> > 5. Caso $\mathcal{R}_1\mathcal{R}_2$ (che descrive il [linguaggio](Teoria%20dei%20linguaggi%20formali.md#^definizione-linguaggio-formale) dato dalla [concatenazione](Teoria%20dei%20linguaggi%20formali.md#^definizione-concatenazione-di-due-linguaggi) dei [linguaggi](Teoria%20dei%20linguaggi%20formali.md#^definizione-linguaggio-formale) descritti dalle [espressioni regolari](Espressioni%20regolari.md#^definizione-espressione-regolare-regex) $\mathcal{R}_1$ ed $\mathcal{R}_2$):
> >    ![teorema-da-regex-a-enfa-concatenazione](teorema-da-regex-a-enfa-concatenazione.svg)
> > 
> > 	Per ipotesi induttiva, esistono due [$\varepsilon$-NFA](Teoria%20degli%20automi.md#^definizione-automa-a-stati-finiti-non-deterministico-con-e-transizioni-enfa) $\mathcal{E}_1$ e $\mathcal{E}_2$ tali che:
> > 	
> > 	$$
> > 	\begin{aligned}
> > 	L(\mathcal{E}_1) &= L(\mathcal{R}_1) \\
> > 	L(\mathcal{E}_2) &= L(\mathcal{R}_2)
> > 	\end{aligned}
> > 	$$
> > 	
> > 	La costruzione collega lo stato finale di $\mathcal{E}_1$ allo stato iniziale di $\mathcal{E}_2$ mediante un'[$\varepsilon$-transizione](Teoria%20degli%20automi.md#^definizione-automa-a-stati-finiti-non-deterministico-con-e-transizioni-enfa).
> > 	
> > 	Di conseguenza, una [stringa](Teoria%20dei%20linguaggi%20formali.md#^definizione-stringa) viene [riconosciuta](Teoria%20degli%20automi.md#^definizione-linguaggio-riconosciuto-da-un-enfa) se e solo se può essere scomposta in due [sottostringhe](Teoria%20dei%20linguaggi%20formali.md#^definizione-sottostringa-di-una-stringa), la prima riconosciuta da $\mathcal{E}_1$ e la seconda riconosciuta da $\mathcal{E}_2$. Pertanto:
> > 	
> > 	$$
> > 	\begin{aligned}
> > 	L(\mathcal{E})
> > 	&= L(\mathcal{E}_1)L(\mathcal{E}_2) \\
> > 	&= L(\mathcal{R}_1)L(\mathcal{R}_2) \\
> > 	&= L(\mathcal{R}_1\mathcal{R}_2)
> > 	\end{aligned}
> > 	$$
> > 6. Caso $\mathcal{R}_1^*$ (che descrive il [linguaggio](Teoria%20dei%20linguaggi%20formali.md#^definizione-linguaggio-formale) dato dalla [chiusura di Kleene](Teoria%20dei%20linguaggi%20formali.md#^definizione-chiusura-di-kleene-su-un-linguaggio) del [linguaggio](Teoria%20dei%20linguaggi%20formali.md#^definizione-linguaggio-formale) descritto dall'[espressione regolare](Espressioni%20regolari.md#^definizione-espressione-regolare-regex) $\mathcal{R}_1$):
> >    ![teorema-da-regex-a-enfa-chiusura-di-kleene](teorema-da-regex-a-enfa-chiusura-di-kleene.svg)
> > 	Per ipotesi induttiva, esiste un [$\varepsilon$-NFA](Teoria%20degli%20automi.md#^definizione-automa-a-stati-finiti-non-deterministico-con-e-transizioni-enfa) $\mathcal{E}_1$ tale che:
> > 	
> > 	$$
> > 	L(\mathcal{E}_1) = L(\mathcal{R}_1)
> > 	$$
> > 	
> > 	La costruzione introduce un nuovo stato iniziale e un nuovo stato finale, collegandoli mediante [$\varepsilon$-transizioni](Teoria%20degli%20automi.md#^definizione-automa-a-stati-finiti-non-deterministico-con-e-transizioni-enfa) agli stati iniziale e finale di $\mathcal{E}_1$. Inoltre, introduce un'[$\varepsilon$-transizione](Teoria%20degli%20automi.md#^definizione-automa-a-stati-finiti-non-deterministico-con-e-transizioni-enfa) dallo stato finale di $\mathcal{E}_1$ al suo stato iniziale, consentendo di ripetere arbitrariamente il percorso dell'[$\varepsilon$-NFA](Teoria%20degli%20automi.md#^definizione-automa-a-stati-finiti-non-deterministico-con-e-transizioni-enfa).
> > 	
> > 	In questo modo, il nuovo automa riconosce:
> > 	- la [stringa vuota](Teoria%20dei%20linguaggi%20formali.md#^definizione-stringa-vuota) $\varepsilon$, grazie all'[$\varepsilon$-transizione](Teoria%20degli%20automi.md#^definizione-automa-a-stati-finiti-non-deterministico-con-e-transizioni-enfa) diretta dallo stato iniziale a quello finale e
> > 	- qualsiasi [concatenazione](Teoria%20dei%20linguaggi%20formali.md#^definizione-concatenazione-di-due-stringhe) finita di [stringhe](Teoria%20dei%20linguaggi%20formali.md#^definizione-stringa) [riconosciute](Teoria%20degli%20automi.md#^definizione-linguaggio-riconosciuto-da-un-enfa) da $\mathcal{E}_1$, grazie alla possibilità di ripetere il percorso un numero arbitrario di volte.
> > 	
> > 	Pertanto:
> > 	
> > 	$$
> > 	\begin{aligned}
> > 	L(\mathcal{E})
> > 	&= L(\mathcal{E}_1)^* \\
> > 	&= L(\mathcal{R}_1)^* \\
> > 	&= L(\mathcal{R}_1^*)
> > 	\end{aligned}
> > 	$$
> > 
> > Abbiamo dimostrato che, in tutti e sei i casi previsti dalla [definizione di _espressione regolare_](Espressioni%20regolari.md#^definizione-espressione-regolare-regex), è possibile costruire un [$\varepsilon$-NFA](Teoria%20degli%20automi.md#^definizione-automa-a-stati-finiti-non-deterministico-con-e-transizioni-enfa) $\mathcal{E}$ tale che:
> > 
> > $$
> > L(\mathcal{E}) = L(\mathcal{R})
> > $$
> > 
> > Per induzione strutturale la proprietà vale quindi per qualsiasi [espressione regolare](Espressioni%20regolari.md#^definizione-espressione-regolare-regex) $\mathcal{R}$.
> > 
> > $\blacksquare$
^teorema-da-regex-a-enfa

> [!algoritmo]+ Algoritmo di conversione di una regex in un $\color{#FF3F3F} \varepsilon$-NFA tramite costruzione induttiva
> 
> Data un'[espressione regolare](Espressioni%20regolari.md#^definizione-espressione-regolare-regex) $\mathcal{R}$, costruiamo un [$\varepsilon$-NFA](Teoria%20degli%20automi.md#^definizione-automa-a-stati-finiti-non-deterministico-con-e-transizioni-enfa) $\mathcal{E} = \langle \Sigma, Q_{\mathcal E}, \delta_{\mathcal E}, q_0, F_{\mathcal E} \rangle$ equivalente, tale che abbia esattamente uno [stato iniziale](Teoria%20degli%20automi.md#^definizione-automa-a-stati-finiti-non-deterministico-con-e-transizioni-enfa) e uno [stato finale](Teoria%20degli%20automi.md#^definizione-automa-a-stati-finiti-non-deterministico-con-e-transizioni-enfa), attraverso i seguenti passaggi:
> 1. **Casi base**: se $\mathcal{R}$ assume una delle forme base previste dalla [definizione di _espressione regolare_](Espressioni%20regolari.md#^definizione-espressione-regolare-regex), costruiamo il corrispondente [$\varepsilon$-NFA](Teoria%20degli%20automi.md#^definizione-automa-a-stati-finiti-non-deterministico-con-e-transizioni-enfa):
> 	- **Caso $\emptyset$**: creiamo due stati, uno iniziale e uno finale, senza alcuna transizione tra di essi:
> 		![teorema-da-regex-a-enfa-linguaggio-vuoto](teorema-da-regex-a-enfa-linguaggio-vuoto.svg)
> 	- **Caso $\varepsilon$**: creiamo due stati, uno iniziale e uno finale, collegati da un'[$\varepsilon$-transizione](Teoria%20degli%20automi.md#^definizione-automa-a-stati-finiti-non-deterministico-con-e-transizioni-enfa):
> 		![teorema-da-regex-a-enfa-stringa-vuota](teorema-da-regex-a-enfa-stringa-vuota.svg)
> 	- **Caso $a \in \Sigma$**: creiamo due stati, uno iniziale e uno finale, collegati da una [transizione](Teoria%20degli%20automi.md#^definizione-automa-a-stati-finiti-non-deterministico-con-e-transizioni-enfa) etichettata con $a$:
> 		![teorema-da-regex-a-enfa-simbolo-a](teorema-da-regex-a-enfa-simbolo-a.svg)
> 2. **Casi induttivi**: se $\mathcal{R}$ è costruita a partire da una o più [sottoespressioni regolari](Espressioni%20regolari.md#^definizione-espressione-regolare-regex), costruiamo innanzitutto i rispettivi [$\varepsilon$-NFA](Teoria%20degli%20automi.md#^definizione-automa-a-stati-finiti-non-deterministico-con-e-transizioni-enfa) per ipotesi induttiva, quindi li combiniamo secondo l'operazione applicata:
> 	- **Caso $\mathcal{R}_1+\mathcal{R}_2$ (unione)**: costruiamo gli [$\varepsilon$-NFA](Teoria%20degli%20automi.md#^definizione-automa-a-stati-finiti-non-deterministico-con-e-transizioni-enfa) $\mathcal{E}_1$ ed $\mathcal{E}_2$ per $\mathcal{R}_1$ e $\mathcal{R}_2$. Introduciamo un nuovo stato iniziale e un nuovo stato finale, collegando:
> 	     - il nuovo stato iniziale agli stati iniziali di $\mathcal{E}_1$ ed $\mathcal{E}_2$ mediante [$\varepsilon$-transizioni](Teoria%20degli%20automi.md#^definizione-automa-a-stati-finiti-non-deterministico-con-e-transizioni-enfa);
> 	     - gli stati finali di $\mathcal{E}_1$ ed $\mathcal{E}_2$ al nuovo stato finale mediante [$\varepsilon$-transizioni](Teoria%20degli%20automi.md#^definizione-automa-a-stati-finiti-non-deterministico-con-e-transizioni-enfa).
> 		![teorema-da-regex-a-enfa-unione](teorema-da-regex-a-enfa-unione.svg)
> 	- **Caso $\mathcal{R}_1\mathcal{R}_2$ (concatenazione)**: costruiamo gli [$\varepsilon$-NFA](Teoria%20degli%20automi.md#^definizione-automa-a-stati-finiti-non-deterministico-con-e-transizioni-enfa) $\mathcal{E}_1$ ed $\mathcal{E}_2$ per $\mathcal{R}_1$ e $\mathcal{R}_2$. Colleghiamo lo stato finale di $\mathcal{E}_1$ allo stato iniziale di $\mathcal{E}_2$ mediante un'[$\varepsilon$-transizione](Teoria%20degli%20automi.md#^definizione-automa-a-stati-finiti-non-deterministico-con-e-transizioni-enfa). Lo stato iniziale del nuovo automa coincide con quello di $\mathcal{E}_1$, mentre lo stato finale coincide con quello di $\mathcal{E}_2$.
> 		![teorema-da-regex-a-enfa-concatenazione](teorema-da-regex-a-enfa-concatenazione.svg)
> 	- **Caso $\mathcal{R}_1^\*$ (chiusura di Kleene)**: costruiamo l'$\varepsilon$-NFA $\mathcal{E}_1$ per $\mathcal{R}_1$. Introduciamo un nuovo stato iniziale e un nuovo stato finale, collegando:
> 		 - il nuovo stato iniziale allo stato iniziale di $\mathcal{E}_1$ mediante un'[$\varepsilon$-transizione](Teoria%20degli%20automi.md#^definizione-automa-a-stati-finiti-non-deterministico-con-e-transizioni-enfa);
> 		 - il nuovo stato iniziale al nuovo stato finale mediante un'[$\varepsilon$-transizione](Teoria%20degli%20automi.md#^definizione-automa-a-stati-finiti-non-deterministico-con-e-transizioni-enfa);
> 		 - lo stato finale di $\mathcal{E}_1$ al suo stato iniziale mediante un'[$\varepsilon$-transizione](Teoria%20degli%20automi.md#^definizione-automa-a-stati-finiti-non-deterministico-con-e-transizioni-enfa);
> 		 - lo stato finale di $\mathcal{E}_1$ al nuovo stato finale mediante un'[$\varepsilon$-transizione](Teoria%20degli%20automi.md#^definizione-automa-a-stati-finiti-non-deterministico-con-e-transizioni-enfa).
> 		![teorema-da-regex-a-enfa-chiusura-di-kleene](teorema-da-regex-a-enfa-chiusura-di-kleene.svg)
> 3. **Individuazione degli stati iniziali e finali**: in ogni costruzione, garantiamo che il nuovo [$\varepsilon$-NFA](Teoria%20degli%20automi.md#^definizione-automa-a-stati-finiti-non-deterministico-con-e-transizioni-enfa) abbia esattamente uno stato iniziale e uno stato finale. Gli stati iniziali e finali dei sottoautomi vengono mantenuti come stati intermedi, mentre quelli introdotti o selezionati dalla costruzione diventano rispettivamente lo stato iniziale e lo stato finale del nuovo automa.
> 4. **Composizione dell'automa**: ripetiamo ricorsivamente i passaggi precedenti per tutte le [sottoespressioni](Espressioni%20regolari.md#^definizione-espressione-regolare-regex) di $\mathcal{R}$, fino a ottenere un unico [$\varepsilon$-NFA](Teoria%20degli%20automi.md#^definizione-automa-a-stati-finiti-non-deterministico-con-e-transizioni-enfa) $\mathcal{E}$ che [riconosce](Teoria%20degli%20automi.md#^definizione-linguaggio-riconosciuto-da-un-enfa) lo stesso [linguaggio](Teoria%20dei%20linguaggi%20formali.md#^definizione-linguaggio-formale) [generato](Espressioni%20regolari.md#^definizione-linguaggio-generato-da-un-espressione-regolare) da $\mathcal{R}$:
> 	$$ 
> 	L(\mathcal{E}) = L(\mathcal{R})
> 	$$
^algoritmo-di-conversione-di-una-regex-in-un-enfa-tramite-costruzione-induttiva

%% 
fare esempio dell'algoritmo
%%

%% 
fare corollario di equivalenza tra regex ed e-nfa
%%

%% 
Convertire le seguenti espressioni regolari in ε-NFA e gli automi ottenuti in DFA:
1. (a + b)*
2. (ab)*
3. a\*b\*
4. a\* + b\*
%%

# 2 - Proprietà di chiusura dei linguaggi regolari

%% 
Vediamo alternativamente come si può dimostrare la chiusura rispetto all'unione
%%

> [!proprieta]+ Proprietà di chiusura dei linguaggi regolari rispetto all'unione
> 
> I [linguaggi regolari](Espressioni%20regolari.md#^definizione-linguaggio-regolare) sono chiusi%% link %% rispetto all'[unione](Teoria%20degli%20insiemi.md#^definizione-unione-di-due-insiemi), ossia dati due [linguaggi regolari](Espressioni%20regolari.md#^definizione-linguaggio-regolare) $L_1$ ed $L_2$ la loro [unione](Teoria%20degli%20insiemi.md#^definizione-unione-di-due-insiemi) $L_1 \cup L_2$ è anch'essa [regolare](Espressioni%20regolari.md#^definizione-linguaggio-regolare).
> 
> > [!dimostrazione]- Dimostrazione
> > 
> > Se $L_1$ ed $L_2$ sono due [linguaggi regolari](Espressioni%20regolari.md#^definizione-linguaggio-regolare), allora per [definizione di _linguaggi regolari_](Espressioni%20regolari.md#^definizione-linguaggio-regolare) esistono due [espressioni regolari](Espressioni%20regolari.md#^definizione-espressione-regolare-regex) $\mathcal{R}_1$ ed $\mathcal{R}_2$ tali che $L_1 = L(\mathcal{R}_1)$ e $L_2 = L(\mathcal{R}_2)$.
> > 
> > Consideriamo ora l'[espressione regolare](Espressioni%20regolari.md#^definizione-espressione-regolare-regex) $\mathcal{R} = \mathcal{R}_1 + \mathcal{R}_2$. Per [definizione di _espressione regolare_](Espressioni%20regolari.md#^definizione-espressione-regolare-regex), il [linguaggio](Teoria%20dei%20linguaggi%20formali.md#^definizione-linguaggio-formale) da essa [generato](Espressioni%20regolari.md#^definizione-linguaggio-generato-da-un-espressione-regolare) è
> > 
> > $$
> > \begin{align*}
> > L(\mathcal{R}) &= L(\mathcal{R}_1 + \mathcal{R}_2) \\
> > &= L(\mathcal{R}_1) \cup L(\mathcal{R}_2) \\
> > &= L_1 \cup L_2
> > \end{align*}
> > $$
> > 
> > Poiché $\mathcal{R}$ è un'[espressione regolare](Espressioni%20regolari.md#^definizione-espressione-regolare-regex) che [genera](Espressioni%20regolari.md#^definizione-linguaggio-generato-da-un-espressione-regolare) $L_1 \cup L_2$, per [definizione di _linguaggio regolare_](Espressioni%20regolari.md#^definizione-linguaggio-regolare) anche $L_1 \cup L_2$ è [regolare](Espressioni%20regolari.md#^definizione-linguaggio-regolare).
> > 
> > $\blacksquare$
^proprieta-di-chiusura-dei-linguaggi-regolari-rispetto-all-unione

> [!proprieta]+ Proprietà di chiusura dei linguaggi regolari rispetto alla concatenazione
> 
> I [linguaggi regolari](Espressioni%20regolari.md#^definizione-linguaggio-regolare) sono chiusi%% link %% rispetto alla [concatenazione](Teoria%20dei%20linguaggi%20formali.md#^definizione-concatenazione-di-linguaggi), ossia dati due [linguaggi regolari](Espressioni%20regolari.md#^definizione-linguaggio-regolare) $L_1$ ed $L_2$ la loro [concatenazione](Teoria%20dei%20linguaggi%20formali.md#^definizione-concatenazione-di-linguaggi) $L_1 L_2$ è anch'essa [regolare](Espressioni%20regolari.md#^definizione-linguaggio-regolare).
> 
> > [!dimostrazione]- Dimostrazione
> > 
> > Se $L_1$ ed $L_2$ sono due [linguaggi regolari](Espressioni%20regolari.md#^definizione-linguaggio-regolare), allora per [definizione di _linguaggi regolari_](Espressioni%20regolari.md#^definizione-linguaggio-regolare) esistono due [espressioni regolari](Espressioni%20regolari.md#^definizione-espressione-regolare-regex) $\mathcal{R}_1$ ed $\mathcal{R}_2$ tali che $L_1 = L(\mathcal{R}_1)$ e $L_2 = L(\mathcal{R}_2)$.
> > 
> > Consideriamo ora l'[espressione regolare](Espressioni%20regolari.md#^definizione-espressione-regolare-regex) $\mathcal{R} = \mathcal{R}_1\mathcal{R}_2$. Per [definizione di _espressione regolare_](Espressioni%20regolari.md#^definizione-espressione-regolare-regex), il [linguaggio](Teoria%20dei%20linguaggi%20formali.md#^definizione-linguaggio-formale) da essa [generato](Espressioni%20regolari.md#^definizione-linguaggio-generato-da-un-espressione-regolare) è
> > 
> > $$
> > \begin{align*}
> > L(\mathcal{R}) &= L(\mathcal{R}_1\mathcal{R}_2) \\
> > &= L(\mathcal{R}_1)L(\mathcal{R}_2) \\
> > &= L_1 L_2
> > \end{align*}
> > $$
> > 
> > Poiché $\mathcal{R}$ è un'[espressione regolare](Espressioni%20regolari.md#^definizione-espressione-regolare-regex) che [genera](Espressioni%20regolari.md#^definizione-linguaggio-generato-da-un-espressione-regolare) $L_1 L_2$, per [definizione di _linguaggio regolare_](Espressioni%20regolari.md#^definizione-linguaggio-regolare) anche $L_1 L_2$ è [regolare](Espressioni%20regolari.md#^definizione-linguaggio-regolare).
> > 
> > $\blacksquare$
^proprieta-di-chiusura-dei-linguaggi-regolari-rispetto-alla-concatenazione

> [!proprieta]+ Proprietà di chiusura dei linguaggi regolari rispetto all'inversione
> 
> I [linguaggi regolari](Espressioni%20regolari.md#^definizione-linguaggio-regolare) sono chiusi%% link %% rispetto all'[inversione](Teoria%20dei%20linguaggi%20formali.md#^definizione-linguaggio-inverso), ossia dato un [linguaggio regolare](Espressioni%20regolari.md#^definizione-linguaggio-regolare) $L$ il suo [inverso](Teoria%20dei%20linguaggi%20formali.md#^definizione-linguaggio-inverso) $L^R$ è anch'esso [regolare](Espressioni%20regolari.md#^definizione-linguaggio-regolare).
> 
> > [!dimostrazione]- Dimostrazione
> > 
> > Se $L$ è un [linguaggio regolare](Espressioni%20regolari.md#^definizione-linguaggio-regolare), allora per [definizione di _linguaggio regolare_](Espressioni%20regolari.md#^definizione-linguaggio-regolare) esiste una [regex](Espressioni%20regolari.md#^definizione-espressione-regolare-regex) $\mathcal{R}$ tale che $L = L(\mathcal{R})$.
> > 
> > Definiamo la [regex](Espressioni%20regolari.md#^definizione-espressione-regolare-regex) $\mathcal{R}^R$ per induzione%% Link %% sulla struttura di $\mathcal{R}$ distinguendo i diversi casi in base alla forma che può assumere, come specificato nella [sua definizione](Espressioni%20regolari.md#^definizione-espressione-regolare-regex):
> > 1. Caso $\emptyset$ (che descrive il [linguaggio vuoto](Teoria%20dei%20linguaggi%20formali.md#^definizione-linguaggio-vuoto) $\emptyset$): poniamo
> >    $$
> >    \emptyset^R = \emptyset
> >    $$
> > 2. Caso $\varepsilon$ (che descrive il [linguaggio](Teoria%20dei%20linguaggi%20formali.md#^definizione-linguaggio-formale) $\{ \varepsilon \}$ contenente solo la [stringa vuota](Teoria%20dei%20linguaggi%20formali.md#^definizione-stringa-vuota) $\varepsilon$): poniamo
> > 	$$
> > 	\varepsilon^R = \varepsilon
> > 	$$
> > 3. Caso $a$ (che descrive il [linguaggio](Teoria%20dei%20linguaggi%20formali.md#^definizione-linguaggio-formale) $\{ a \}$ contenente solo il [simbolo](Teoria%20dei%20linguaggi%20formali.md#^definizione-simbolo) $a \in \Sigma$): poniamo
> > 	$$
> > 	a^R = a
> > 	$$
> > 4. Caso $\mathcal{R}_1+\mathcal{R}_2$ (che descrive il [linguaggio](Teoria%20dei%20linguaggi%20formali.md#^definizione-linguaggio-formale) dato dall'[unione](Teoria%20degli%20insiemi.md#^definizione-unione-di-due-insiemi) dei [linguaggi](Teoria%20dei%20linguaggi%20formali.md#^definizione-linguaggio-formale) descritti dalle [espressioni regolari](Espressioni%20regolari.md#^definizione-espressione-regolare-regex) $\mathcal{R}_1$ ed $\mathcal{R}_2$): poniamo
> >    $$
> > 	(\mathcal{R}_1 + \mathcal{R}_2)^R = \mathcal{R}_1^R + \mathcal{R}_2^R
> > 	$$
> > 5. Caso $\mathcal{R}_1\mathcal{R}_2$ (che descrive il [linguaggio](Teoria%20dei%20linguaggi%20formali.md#^definizione-linguaggio-formale) dato dalla [concatenazione](Teoria%20dei%20linguaggi%20formali.md#^definizione-concatenazione-di-due-linguaggi) dei [linguaggi](Teoria%20dei%20linguaggi%20formali.md#^definizione-linguaggio-formale) descritti dalle [espressioni regolari](Espressioni%20regolari.md#^definizione-espressione-regolare-regex) $\mathcal{R}_1$ ed $\mathcal{R}_2$): poniamo
> >    $$
> > 	(\mathcal{R}_1\mathcal{R}_2)^R = \mathcal{R}_2^R\mathcal{R}_1^R
> > 	$$
> > 	(**fai attenzione a invertire $\boldsymbol{\mathcal{R}_1}$ ed $\boldsymbol{\mathcal{R}_2}$!**)
> > 6. Caso $\mathcal{R}_1^*$ (che descrive il [linguaggio](Teoria%20dei%20linguaggi%20formali.md#^definizione-linguaggio-formale) dato dalla [chiusura di Kleene](Teoria%20dei%20linguaggi%20formali.md#^definizione-chiusura-di-kleene-su-un-linguaggio) del [linguaggio](Teoria%20dei%20linguaggi%20formali.md#^definizione-linguaggio-formale) descritto dall'[espressione regolare](Espressioni%20regolari.md#^definizione-espressione-regolare-regex) $\mathcal{R}_1$): poniamo
> > 	$$
> > 	(\mathcal{R}_1^*)^R = (\mathcal{R}_1^R)^*
> > 	$$
> > 
> > Abbiamo dimostrato che, in ciascuno dei sei casi previsti dalla [definizione di _espressione regolare_](Espressioni%20regolari.md#^definizione-espressione-regolare-regex), è possibile costruire una nuova [regex](Espressioni%20regolari.md#^definizione-espressione-regolare-regex) $\mathcal{R}^R$ a partire da $\mathcal{R}$, in modo tale che il [linguaggio](Teoria%20dei%20linguaggi%20formali.md#^definizione-linguaggio-formale) $L(\mathcal{R}^R)$ da essa [generato](Espressioni%20regolari.md#^definizione-linguaggio-generato-da-un-espressione-regolare) coincida con l'[inverso](Teoria%20dei%20linguaggi%20formali.md#^definizione-linguaggio-inverso) $L(\mathcal{R})^R$ del [linguaggio](Teoria%20dei%20linguaggi%20formali.md#^definizione-linguaggio-formale) $L(\mathcal{R})$ [generato](Espressioni%20regolari.md#^definizione-linguaggio-generato-da-un-espressione-regolare) da $\mathcal{R}$, ossia:
> > 
> > $$
> > L(\mathcal{R}^R) = L(\mathcal{R})^R = L^R
> > $$
> > 
> > Poiché $\mathcal{R}^R$ è a sua volta una [regex](Espressioni%20regolari.md#^definizione-espressione-regolare-regex), allora anche $L^R$ è un [linguaggio regolare](Espressioni%20regolari.md#^definizione-linguaggio-regolare) per [definizione di _linguaggio regolare_](Espressioni%20regolari.md#^definizione-linguaggio-regolare).
> > 
> > $\blacksquare$
^proprieta-di-chiusura-dei-linguaggi-regolari-rispetto-all-inversione

%% 
esercizio

Se L è un linguaggio regolare, cosa si può dire di L* e di L+? Sono regolari?
%%

%% 
esercizio
Definire un DFA che riconosca il linguaggio delle stringhe sull’alfabeto {0, 1} in cui non c’è uno 0 seguito da due 1
%%

%% 
esercizio
Definire un DFA che riconosca il linguaggio delle stringhe sull’alfabeto {0, 1} di lunghezza pari e che contengono almeno un 1.
%%

%% 
esercizio
Definire un’espressione regolare per il linguaggio $L(\mathcal{R})^R$ dove $\mathcal{R} = (\text{ab})^*(\text{b}+\text{a}^*)^*$
%%

---

> [!fonti]+ Fonti
> 
> - 🏫 Corso di Laurea in Informatica (`L-31 R`) presso l'Università di Torino:
>     - Corso di _Linguaggi Formali e Traduttori_ (`INF0344`), A.A. 2026-27 ([pagina Moodle](https://informatica.i-learn.unito.it/course/view.php?id=3735)):
> 		- Prof. Jeremy James Sproston, slide del corso:
> 			- [2.4 - _RE_](https://informatica.i-learn.unito.it/pluginfile.php/514089/mod_folder/content/0/2-4_re.pdf).
> 			- [2.5 - _Proprietà di chiusura dei linguaggi regolari_](https://informatica.i-learn.unito.it/pluginfile.php/514089/mod_folder/content/0/2-5_prop_lr.pdf).
