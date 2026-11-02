---
aliases:
  - Teoria degli automi
---

> [!premessa]+ Premessa
> 
> Ciao! Se è la prima volta che capiti su questo sito, ti consiglio di consultare la [pagina principale](index.md) di questo _Giardino Digitale_ per scoprire meglio cos'è e come navigarlo.
> 
> Lo stato di questa nota è al momento: 🔴 <font color="#FF7F7F">_Bozza_</font>.

^2a02ff

%% 
https://en.wikipedia.org/wiki/Finite-state_machine
%%

---

%% 
Fare introduzione agli automi

automa = macchina che riconosce stringhe

- l’automa legge la stringa un simbolo alla volta, da sinistra verso destra ⇒ l’automa ha una visione locale e limitata
- ogni simbolo letto altera lo stato dell’automa ⇒ l’automa "ricorda" le caratteristiche della stringa letta usando lo stato
- quando la stringa è stata letta interamente, l’automa risponde "s`ı" se si trova in un cosiddetto stato finale e "no" altrimenti
%%

# 1 - DFA

> [!definizione]+ Definizione: automa a stati finiti deterministico (DFA)
> 
> Un **automa a stati finiti deterministico** (**DFA**, dall'inglese _**D**eterministic **F**inite-state **A**utomaton_) è una [quintupla](Teoria%20degli%20insiemi.md#^definizione-tupla)
> 
> $$
> \mathcal{A} = \langle \Sigma, Q, \delta, q_0, F \rangle
> $$
> 
> dove:
> - $\Sigma = \{ a_0, a_1, \ldots, a_n \}$ è un [alfabeto](Teoria%20dei%20linguaggi%20formali.md#^definizione-alfabeto),
> - $Q = \{ q_0, q_1, \ldots, q_m \}$ è un insieme finito%% link %% di **stati**,
> - $\delta \colon Q \times \Sigma \to Q$ è una [funzione](Funzioni.md#^definizione-funzione) detta **funzione di transizione fra stati**,
> - $q_0 \in Q$ è uno stato detto **stato iniziale** e
> - $F \subseteq Q$ è un [insieme](Teoria%20degli%20insiemi.md#^definizione-insieme) di stati detti **stati finali**.
^definizione-automa-a-stati-finiti-deterministico-dfa

> [!notazione]+ Notazione: rappresentazione grafica di un DFA
> 
> Un [DFA](Teoria%20degli%20automi.md#^definizione-automa-a-stati-finiti-deterministico-dfa) si può rappresentare graficamente in questo modo:
> - ogni [stato](Teoria%20degli%20automi.md#^definizione-automa-a-stati-finiti-deterministico-dfa) $q_0, q_1, \ldots, q_m \in Q$ è un pallino contenente il nome dello stato,
> - ogni transizione è rappresentata da una freccia, etichettata con il [simbolo](Teoria%20dei%20linguaggi%20formali.md#^definizione-simbolo) $a_0, a_1, \ldots, a_n \in \Sigma$, che collega i due stati legati dalla [funzione di transizione fra stati](Teoria%20degli%20automi.md#^definizione-automa-a-stati-finiti-deterministico-dfa),
> - lo [stato iniziale](Teoria%20degli%20automi.md#^definizione-automa-a-stati-finiti-deterministico-dfa) $q_0 \in Q$ è rappresentato da una freccia entrante e
> - gli [stati finali](Teoria%20degli%20automi.md#^definizione-automa-a-stati-finiti-deterministico-dfa) $F \subseteq Q$ hanno un doppio contorno.
> 
> Per esempio, un [DFA](Teoria%20degli%20automi.md#^definizione-automa-a-stati-finiti-deterministico-dfa) $\mathcal{A} = \langle \Sigma, Q, \delta, q_0, F \rangle$ definito come:
> - $\Sigma = \{ \text{a}, \text{b} \}$,
> - $Q = \{ q_0, q_1, q_2 \}$,
> - $\delta(q_0, \text{a}) = q_1,\ \delta(q_0, \text{b}) = q_2,\ \delta(q_2, \text{a}) = q_2,\ \ldots$
> - $F = \{ q_1 \}$
> 
> sarà rappresentato così:
> 
> ![notazione-rappresentazione-di-un-dfa](notazione-rappresentazione-di-un-dfa.svg)
^rappresentazione-grafica-di-un-automa

> [!esempio]- Esempio: numero dispari di $\color{#7F7FFF} \text{a}$
> 
> Proviamo a definire un [DFA](Teoria%20degli%20automi.md#^definizione-automa-a-stati-finiti-deterministico-dfa) che riconosce solo le [stringhe](Teoria%20dei%20linguaggi%20formali.md#^definizione-stringa) di $\text{a}$ di [lunghezza](Teoria%20dei%20linguaggi%20formali.md#^definizione-lunghezza-di-una-stringa) dispari.
> 
> Questo [automa](Teoria%20degli%20automi.md#^definizione-automa-a-stati-finiti-deterministico-dfa) $\mathcal{A} = \langle \Sigma, Q, \delta, q_0, F \rangle$ sarà così definito:
> - $\Sigma = \{ \text{a} \}$ perché ci servono solo [stringhe](Teoria%20dei%20linguaggi%20formali.md#^definizione-stringa) contenenti il [simbolo](Teoria%20dei%20linguaggi%20formali.md#^definizione-simbolo) $\text{a}$;
> - $Q = \{ q_0, q_1 \}$ perché servono solo due stati, uno per quando la [stringa](Teoria%20dei%20linguaggi%20formali.md#^definizione-stringa) sarà di [lunghezza](Teoria%20dei%20linguaggi%20formali.md#^definizione-lunghezza-di-una-stringa) pari e uno per quando sarà di [lunghezza](Teoria%20dei%20linguaggi%20formali.md#^definizione-lunghezza-di-una-stringa) dispari;
> - $\delta \colon Q \times \Sigma \to Q$ così definita:
> 	- $\delta(q_0, \text{a}) = q_1$ perché quando la [stringa](Teoria%20dei%20linguaggi%20formali.md#^definizione-stringa) sarà di [lunghezza](Teoria%20dei%20linguaggi%20formali.md#^definizione-lunghezza-di-una-stringa) pari ($q_0$) e riceve un $\text{a}$ in input diventa dispari ($q_1$) e, viceversa,
> 	- $\delta(q_1, \text{a}) = q_0$ perché quando la [stringa](Teoria%20dei%20linguaggi%20formali.md#^definizione-stringa) sarà di [lunghezza](Teoria%20dei%20linguaggi%20formali.md#^definizione-lunghezza-di-una-stringa) dispari ($q_1$) e riceve un $\text{a}$ in input diventa pari ($q_0$);
> - $q_0 \in Q$ come [stato iniziale](Teoria%20degli%20automi.md#^definizione-automa-a-stati-finiti-deterministico-dfa) e
> - $F = \{ q_1 \} \subseteq Q$ perché la [stringa](Teoria%20dei%20linguaggi%20formali.md#^definizione-stringa) sarà accettabile solo quando avrà [lunghezza](Teoria%20dei%20linguaggi%20formali.md#^definizione-lunghezza-di-una-stringa) dispari.
> 
> ![esempio-numero-dispari-di-a](esempio-numero-dispari-di-a.svg)

> [!esempio]- Esempio: numeri binari pari
> 
> Proviamo a definire un [DFA](Teoria%20degli%20automi.md#^definizione-automa-a-stati-finiti-deterministico-dfa) che riconosce solo le [stringhe](Teoria%20dei%20linguaggi%20formali.md#^definizione-stringa) di numeri binari%% Link %% pari%% link %%, ossia [stringhe](Teoria%20dei%20linguaggi%20formali.md#^definizione-stringa) non [vuote](Teoria%20dei%20linguaggi%20formali.md#^definizione-stringa-vuota) e che terminano con $0$.
> 
> Questo [automa](Teoria%20degli%20automi.md#^definizione-automa-a-stati-finiti-deterministico-dfa) $\mathcal{A} = \langle \Sigma, Q, \delta, q_0, F \rangle$ sarà così definito:
> - $\Sigma = \{ 0,1 \}$ perché le [stringhe](Teoria%20dei%20linguaggi%20formali.md#^definizione-stringa) sono numeri binari%% Link %%;
> - $Q = \{ q_x, q_0, q_1 \}$ perché serve uno [stato](Teoria%20degli%20automi.md#^definizione-automa-a-stati-finiti-deterministico-dfa) $q_x$ in cui non è ancora stato riconosciuto alcun bit e due [stati](Teoria%20degli%20automi.md#^definizione-automa-a-stati-finiti-deterministico-dfa) $q_0$ e $q_1$ in cui almeno un bit è stato riconosciuto e l'ultimo è stato rispettivamente $0$ e $1$;
> - $\delta \colon Q \times \Sigma \to Q$ così definita:
> 	- in qualsiasi caso in cui viene riconosciuto un bit $0$ lo [stato](Teoria%20degli%20automi.md#^definizione-automa-a-stati-finiti-deterministico-dfa) transiziona a $q_0$, ossia
> 		$$
> 		\begin{array}{}
> 		\delta(q_n, 0) = q_0 \\ \delta(q_0, 0) = q_0 \\ \delta(q_1, 0) = q_0
> 		\end{array}
> 		$$
> 	- in qualsiasi caso in cui viene riconosciuto un bit $1$ lo [stato](Teoria%20degli%20automi.md#^definizione-automa-a-stati-finiti-deterministico-dfa) transiziona a $q_1$, ossia
> 		$$
> 		\begin{array}{}
> 		\delta(q_n, 1) = q_1 \\ \delta(q_0, 1) = q_1 \\ \delta(q_1, 1) = q_1
> 		\end{array}
> 		$$
> - $q_x \in Q$ come [stato iniziale](Teoria%20degli%20automi.md#^definizione-automa-a-stati-finiti-deterministico-dfa) e
> - $F = \{ q_0 \}\subseteq Q$ perché la [stringa](Teoria%20dei%20linguaggi%20formali.md#^definizione-stringa) sarà accettabile solo quando il suo ultimo bit riconosciuto sarà stato $0$.
> 
> ![esempio-numeri-binari-pari](esempio-numeri-binari-pari.svg)
^esempio-numeri-binari-pari

Ora definiamo matematicamente cosa significa "accettare" una [stringa](Teoria%20dei%20linguaggi%20formali.md#^definizione-stringa) per un [DFA](Teoria%20degli%20automi.md#^definizione-automa-a-stati-finiti-deterministico-dfa).

Innanzitutto definiamo un'estensione della [funzione di transizione](Teoria%20degli%20automi.md#^definizione-automa-a-stati-finiti-deterministico-dfa) che ci permetta di fare la transizione non su un singolo [simbolo](Teoria%20dei%20linguaggi%20formali.md#^definizione-simbolo) ma su un'intera [stringa](Teoria%20dei%20linguaggi%20formali.md#^definizione-stringa) in maniera ricorsiva, utilizzando la [funzione di transizione](Teoria%20degli%20automi.md#^definizione-automa-a-stati-finiti-deterministico-dfa) che già conosciamo per saltare da un simbolo all'altro della stringa.

> [!definizione]+ Definizione: funzione di transizione estesa di un DFA
> 
> In un [DFA](Teoria%20degli%20automi.md#^definizione-automa-a-stati-finiti-deterministico-dfa) $\mathcal{A} = \langle \Sigma, Q, \delta, q_0, F \rangle$, la **funzione di transizione estesa** $\hat\delta \colon Q \times \Sigma^* \to Q$ è una [funzione](Funzioni.md#^definizione-funzione) definita induttivamente%% link %% sul suo secondo argomento così come segue:
> 
> $$
> \begin{align*}
> \hat\delta(q, \varepsilon) &= q \\
> \hat\delta(q, wa) &= \delta(\hat\delta(q,w),a)
> \end{align*}
> $$
^definizione-funzione-di-transizione-estesa-di-un-dfa

> [!esempio]- Esempio di funzione di transizione estesa
> 
> Riprendiamo l'[esempio dei numeri binari pari](Teoria%20degli%20automi.md#^esempio-numeri-binari-pari) per illustrare come opera la [funzione di transizione estesa](Teoria%20degli%20automi.md#^definizione-funzione-di-transizione-estesa-di-un-dfa).
> 
> Data la [stringa](Teoria%20dei%20linguaggi%20formali.md#^definizione-stringa) $1011$ e lo [stato iniziale](Teoria%20degli%20automi.md#^definizione-automa-a-stati-finiti-deterministico-dfa) $q_x$, la [funzione di transizione estesa](Teoria%20degli%20automi.md#^definizione-funzione-di-transizione-estesa-di-un-dfa) si sviluppa in questo modo:
> 
> $$
> \begin{align*}
> \hat\delta(q_x, 1011) &= \delta(\hat\delta(q_x, 101), 1) \\
> &= \delta(\delta(\hat\delta(q_x,10),1),1) \\
> &= \delta(\delta(\delta(\hat\delta(q_x, 1),0),1),1) \\
> &= \delta(\delta(\delta(\delta(\hat\delta(q_x, \varepsilon), 1),0),1),1) \\
> &= \delta(\delta(\delta(\delta(q_x, 1),0),1),1) \\
> &= \delta(\delta(\delta(q_1,0),1),1) \\
> &= \delta(\delta(q_0,1),1) \\
> &= \delta(q_1,1) \\
> &= q_1 \\
> \end{align*}
> $$
> 
> Possiamo infatti notare che, essendo $1011$ dispari, dopo l'ultimo bit ci ritroveremo nello [stato](Teoria%20degli%20automi.md#^definizione-automa-a-stati-finiti-deterministico-dfa) $q_1$. Ciò che fa la [funzione di transizione estesa](Teoria%20degli%20automi.md#^definizione-funzione-di-transizione-estesa-di-un-dfa) non è altro che applicare la [funzione di transizione](Teoria%20degli%20automi.md#^definizione-automa-a-stati-finiti-deterministico-dfa) nel passaggio da ogni [simbolo](Teoria%20dei%20linguaggi%20formali.md#^definizione-simbolo) a quello successivo della [stringa](Teoria%20dei%20linguaggi%20formali.md#^definizione-stringa):
> 
> $$
> q_x \overset{\displaystyle 1}\to q_1 \overset{\displaystyle 0}\to q_0 \overset{\displaystyle 1}\to q_1 \overset{\displaystyle 1}\to q_1
> $$

> [!definizione]+ Definizione: linguaggio riconosciuto da un DFA
> 
> Dato un [DFA](Teoria%20degli%20automi.md#^definizione-automa-a-stati-finiti-deterministico-dfa) $\mathcal{A} = \langle \Sigma, Q, \delta, q_0, F \rangle$, il **linguaggio riconosciuto** (o **accettato**) $L(A)$ da $\cal A$ è il [linguaggio formale](Teoria%20dei%20linguaggi%20formali.md#^definizione-linguaggio-formale) dato dalla [chiusura di Kleene](Teoria%20dei%20linguaggi%20formali.md#^definizione-chiusura-di-kleene-su-un-alfabeto) $\Sigma^*$ in cui, per ogni [stringa](Teoria%20dei%20linguaggi%20formali.md#^definizione-stringa) $w \in \Sigma^*$, la [funzione di transizione estesa](Teoria%20degli%20automi.md#^definizione-funzione-di-transizione-estesa-di-un-dfa) restituisce uno [stato finale](Teoria%20degli%20automi.md#^definizione-automa-a-stati-finiti-deterministico-dfa):
> 
> $$
> L(\mathcal{A}) = \{ w \in \Sigma^* \mid \hat\delta(q_0, w) \in F \}
> $$
^definizione-linguaggio-riconosciuto-da-un-dfa

Banalmente, un [linguaggio riconosciuto](Teoria%20degli%20automi.md#^definizione-linguaggio-riconosciuto-da-un-dfa) è un [linguaggio](Teoria%20dei%20linguaggi%20formali.md#^definizione-linguaggio-formale) in cui, presa una [stringa](Teoria%20dei%20linguaggi%20formali.md#^definizione-stringa) qualsiasi, sappiamo che terminerà su uno [stato finale](Teoria%20degli%20automi.md#^definizione-automa-a-stati-finiti-deterministico-dfa).

> [!esempio]- Esempio di linguaggio riconosciuto
> 
> Riprendendo sempre l'[esempio dei numeri binari pari](Teoria%20degli%20automi.md#^esempio-numeri-binari-pari), il [linguaggio riconosciuto](Teoria%20degli%20automi.md#^definizione-linguaggio-riconosciuto-da-un-dfa) di questo [DFA](Teoria%20degli%20automi.md#^definizione-automa-a-stati-finiti-deterministico-dfa) sarà dato da tutte le [stringhe](Teoria%20dei%20linguaggi%20formali.md#^definizione-stringa) terminanti per $0$:
> 
> $$
> L(\mathcal{A}) = \{ w \in \Sigma^* \mid w = w'0 \}
> $$
> 
> (dove $w'$ è un [prefisso](Teoria%20dei%20linguaggi%20formali.md#^definizione-prefisso-di-una-stringa) di $w$).

> [!definizione]+ Definizione: linguaggio regolare
> 
> Un [linguaggio](Teoria%20dei%20linguaggi%20formali.md#^definizione-linguaggio-formale) $L$ si dice **regolare** se esiste un [DFA](Teoria%20degli%20automi.md#^definizione-automa-a-stati-finiti-deterministico-dfa) $\cal A$ per cui è il suo [linguaggio riconosciuto](Teoria%20degli%20automi.md#^definizione-linguaggio-riconosciuto-da-un-dfa):
> 
> $$
> L = L(\mathcal A)
> $$
^definizione-linguaggio-regolare

> [!notazione]+ Notazione: tabella di transizione
> 
> Un [DFA](Teoria%20degli%20automi.md#^definizione-automa-a-stati-finiti-deterministico-dfa) $\mathcal{A} = \langle \Sigma, Q, \delta, q_0, F \rangle$ si può rappresentare in forma tabellare attraverso la sua **tabella di transizione**, in cui:
> - ogni riga corrisponde a uno [stato](Teoria%20degli%20automi.md#^definizione-automa-a-stati-finiti-deterministico-dfa) del [DFA](Teoria%20degli%20automi.md#^definizione-automa-a-stati-finiti-deterministico-dfa),
> - ogni riga corrisponde a un [simbolo](Teoria%20dei%20linguaggi%20formali.md#^definizione-simbolo) dell'[alfabeto](Teoria%20dei%20linguaggi%20formali.md#^definizione-alfabeto) $\Sigma$ del [DFA](Teoria%20degli%20automi.md#^definizione-automa-a-stati-finiti-deterministico-dfa),
> - lo [stato iniziale](Teoria%20degli%20automi.md#^definizione-automa-a-stati-finiti-deterministico-dfa) $q_0 \in Q$ è marcato con una freccia $\to$,
> - ogni [stato finale](Teoria%20degli%20automi.md#^definizione-automa-a-stati-finiti-deterministico-dfa) è marcato con un asterisco $*$ e
> - la cella corrispondente alla riga $q_i$ e alla colonna $a_j$ contiene il valore di $\delta(q_i, a_j)$.
> 
> Per esempio, un [DFA](Teoria%20degli%20automi.md#^definizione-automa-a-stati-finiti-deterministico-dfa) $\mathcal{A} = \langle \Sigma, Q, \delta, q_0, F \rangle$ definito come:
> - $\Sigma = \{ \text{a}, \text{b} \}$,
> - $Q = \{ q_0, q_1, q_2 \}$,
> - $\delta(q_0, \text{a}) = q_1,\ \delta(q_0, \text{b}) = q_2,\ \delta(q_2, \text{a}) = q_2,\ \ldots$
> - $F = \{ q_1 \}$
> 
> e la sua [rappresentazione grafica](Teoria%20degli%20automi.md#^rappresentazione-grafica-di-un-automa) è
> 
> ![notazione-rappresentazione-di-un-dfa](notazione-rappresentazione-di-un-dfa.svg)
> 
> sarà rappresentato così:
> 
> | **Stato** | $\mathbf{a}$ | $\mathbf{b}$ |
> | --------- | ------------ | ------------ |
> | $\to q_0$ | $q_1$        | $q_2$        |
> | $q_1$     | $q_0$        | $q_1$        |
> | $*q_2$    | $q_2$        | $q_0$        |
^notazione-tabella-di-transizione

> [!esempio]- Esempio: stringhe contenenti almeno un $\color{#7F7FFF} \text{abb}$
> 
> Definiamo ora un [DFA](Teoria%20degli%20automi.md#^definizione-automa-a-stati-finiti-deterministico-dfa) che [riconosce](Teoria%20degli%20automi.md#^definizione-linguaggio-riconosciuto-da-un-dfa) le [stringhe](Teoria%20dei%20linguaggi%20formali.md#^definizione-stringa) su $\Sigma = \{ \text{a}, \text{b} \}$ in cui esiste almeno un $\text{abb}$ (es. $\text{b}{\color{#7FFF7F} \text{abb} }\text{a}$ viene riconosciuta).
> 
> Avremo bisogno di quattro [stati](Teoria%20degli%20automi.md#^definizione-automa-a-stati-finiti-deterministico-dfa):
> - $q_0$: non sono stati riconosciuti [simboli](Teoria%20dei%20linguaggi%20formali.md#^definizione-simbolo) o gli unici finora sono stati $\text{b}$,
> - $q_1$: l'ultimo [simbolo](Teoria%20dei%20linguaggi%20formali.md#^definizione-simbolo) riconosciuto era una $\text{a}$,
> - $q_2$: gli ultimi due [simboli](Teoria%20dei%20linguaggi%20formali.md#^definizione-simbolo) riconosciuti erano $\text{ab}$,
> - $q_3$: è stato riconosciuto almeno un $\text{abb}$.
> 
> In particolare, una volta raggiunto lo stato $q_3$ il [DFA](Teoria%20degli%20automi.md#^definizione-automa-a-stati-finiti-deterministico-dfa) ha riconosciuto almeno un $\text{abb}$ e, a prescindere dai prossimi [simboli](Teoria%20dei%20linguaggi%20formali.md#^definizione-simbolo) che riconoscerà, la [stringa](Teoria%20dei%20linguaggi%20formali.md#^definizione-stringa) sarà sempre accettata. Questo [stato](Teoria%20degli%20automi.md#^definizione-automa-a-stati-finiti-deterministico-dfa) lo chiameremo [_stato pozzo_](Teoria%20degli%20automi.md#^definizione-stato-pozzo).
> 
> La sua [rappresentazione grafica](Teoria%20degli%20automi.md#^rappresentazione-grafica-di-un-automa) sarà la seguente:
> 
> ![esempio-stringhe-contenenti-almeno-un-abb](esempio-stringhe-contenenti-almeno-un-abb.svg)

> [!definizione]+ Definizione: stato pozzo
> 
> Dato un [DFA](Teoria%20degli%20automi.md#^definizione-automa-a-stati-finiti-deterministico-dfa) $\mathcal{A} = \langle \Sigma, Q, \delta, q_0, F \rangle$, uno [stato](Teoria%20degli%20automi.md#^definizione-automa-a-stati-finiti-deterministico-dfa) $q_p \in Q$ viene detto **stato pozzo** (o **stato trappola**, in inglese **sink state** o **trap state**) se una volta entrati è impossibile uscirne, ossia se per ogni [simbolo](Teoria%20dei%20linguaggi%20formali.md#^definizione-simbolo) $a \in \Sigma$ la [funzione di transizione](Teoria%20degli%20automi.md#^definizione-automa-a-stati-finiti-deterministico-dfa) darà sempre $q_p$ stesso:
> 
> $$
> \forall a \in \Sigma . \big( \delta(q_p, a) = q_p \big) 
> $$
^definizione-stato-pozzo

> [!esempio]- Esempio: stringhe in cui ogni $\color{#7F7FFF} \text{a}$ è seguita da $\color{#7F7FFF} \text{bb}$
> 
> Definiamo ora un [DFA](Teoria%20degli%20automi.md#^definizione-automa-a-stati-finiti-deterministico-dfa) che [riconosce](Teoria%20degli%20automi.md#^definizione-linguaggio-riconosciuto-da-un-dfa) le [stringhe](Teoria%20dei%20linguaggi%20formali.md#^definizione-stringa) su $\Sigma = \{ \text{a}, \text{b} \}$ in cui ogni $\text{a}$ è seguita immediatamente da $\text{bb}$ (es. $\text{b}{\color{#7FFF7F} \text{abb} }$ viene riconosciuta, ma ${\color{#7FFF7F} \text{abb} }{\color{#FF7F7F} \text{a} }$ no perché l'ultima ${\color{#FF7F7F} \text{a} }$ non è seguita da un $\text{bb}$).
> 
> Avremo bisogno di quattro [stati](Teoria%20degli%20automi.md#^definizione-automa-a-stati-finiti-deterministico-dfa):
> - $q_0$: ogni $\text{a}$ riconosciuta era seguita da $\text{bb}$,
> - $q_1$: l'ultimo [simbolo](Teoria%20dei%20linguaggi%20formali.md#^definizione-simbolo) riconosciuto era una $\text{a}$,
> - $q_2$: gli ultimi due [simboli](Teoria%20dei%20linguaggi%20formali.md#^definizione-simbolo) riconosciuti erano $\text{ab}$,
> - $q_3$: è stata riconosciuta una $\text{a}$ seguita da una sequenza diversa da $\text{bb}$.
> 
> In particolare, una volta raggiunto lo stato $q_3$ il [DFA](Teoria%20degli%20automi.md#^definizione-automa-a-stati-finiti-deterministico-dfa) non ha più speranze di riconoscere la [stringa](Teoria%20dei%20linguaggi%20formali.md#^definizione-stringa) perché ha trovato almeno una $\text{a}$ **non** seguita da $\text{bb}$. Anche questo [stato](Teoria%20degli%20automi.md#^definizione-automa-a-stati-finiti-deterministico-dfa) è uno [_stato pozzo_](Teoria%20degli%20automi.md#^definizione-stato-pozzo).
> 
> La sua [rappresentazione grafica](Teoria%20degli%20automi.md#^rappresentazione-grafica-di-un-automa) sarà la seguente:
> 
> ![esempio-stringhe-in-cui-ogni-a-e-seguita-da-bb](esempio-stringhe-in-cui-ogni-a-e-seguita-da-bb.svg)
^esempio-stringhe-in-cui-ogni-a-e-seguita-da-bb

%% 
Slide 13 di 2.1 - DFA

[!esempio]- Esempio: numeri binari multipli di $5$

Definiamo ora un [DFA](Teoria%20degli%20automi.md#^definizione-automa-a-stati-finiti-deterministico-dfa) che [riconosce](Teoria%20degli%20automi.md#^definizione-linguaggio-riconosciuto-da-un-dfa) le [stringhe](Teoria%20dei%20linguaggi%20formali.md#^definizione-stringa) su $\Sigma = \{ 0,1 \}$ in cui i numeri binari rappresentano multipli di $5$.
%%

%% 
Esercizi slide 14 e 15 e 16 di 2.1 - DFA
%%

# 2 - NFA

Finora abbiamo visto i [DFA](Teoria%20degli%20automi.md#^definizione-automa-a-stati-finiti-deterministico-dfa), ossia [automi a stati finiti _deterministici_](Teoria%20degli%20automi.md#^definizione-automa-a-stati-finiti-deterministico-dfa): se questi vengono definiti _deterministici_, vuol dire che esisteranno anche automi a stati finiti _non deterministici_, ossia automi in cui, dato uno [stato](Teoria%20degli%20automi.md#^definizione-automa-a-stati-finiti-deterministico-dfa) e un [simbolo](Teoria%20dei%20linguaggi%20formali.md#^definizione-simbolo) in ingresso, non è necessariamente individuato un **unico** [stato](Teoria%20degli%20automi.md#^definizione-automa-a-stati-finiti-deterministico-dfa) successivo, ma può prevedere più transizioni in [stati](Teoria%20degli%20automi.md#^definizione-automa-a-stati-finiti-deterministico-dfa) diversi etichettate con il medesimo simbolo, oppure nessuna transizione per un determinato [simbolo](Teoria%20dei%20linguaggi%20formali.md#^definizione-simbolo).

Ciò significa che una [stringa](Teoria%20dei%20linguaggi%20formali.md#^definizione-stringa) in questo tipo di automi detti [_NFA_](Teoria%20degli%20automi.md#^definizione-automa-a-stati-finiti-non-deterministico-nfa)%% Link %% può intraprendere più "percorsi" e viene [riconosciuta](Teoria%20degli%20automi.md#^definizione-linguaggio-riconosciuto-da-un-dfa) se se esiste almeno un percorso di transizioni che, consumando interamente la [stringa](Teoria%20dei%20linguaggi%20formali.md#^definizione-stringa) (cioè scandendo tutti i suoi [simboli](Teoria%20dei%20linguaggi%20formali.md#^definizione-simbolo)), conduce a uno [stato finale](Teoria%20degli%20automi.md#^definizione-automa-a-stati-finiti-deterministico-dfa).

Nonostante questa differenza, [DFA](Teoria%20degli%20automi.md#^definizione-automa-a-stati-finiti-deterministico-dfa) e [NFA](Teoria%20degli%20automi.md#^definizione-automa-a-stati-finiti-non-deterministico-nfa) sono equivalenti dal punto di vista della potenza espressiva, in quanto con entrambi possiamo definire gli stessi [linguaggi regolari](Teoria%20degli%20automi.md#^definizione-linguaggio-regolare). Pertanto, ogni [NFA](Teoria%20degli%20automi.md#^definizione-automa-a-stati-finiti-non-deterministico-nfa) può essere trasformato in un [DFA](Teoria%20degli%20automi.md#^definizione-automa-a-stati-finiti-deterministico-dfa) equivalente, sebbene quest'ultimo possa richiedere un numero maggiore di [stati](Teoria%20degli%20automi.md#^definizione-automa-a-stati-finiti-deterministico-dfa).

> [!definizione]+ Definizione: automa a stati finiti non deterministico (NFA)
> 
> Un **automa a stati finiti non deterministico** (**NFA**, dall'inglese _**N**on-deterministic **F**inite-state **A**utomaton_) è una [quintupla](Teoria%20degli%20insiemi.md#^definizione-tupla)
> 
> $$
> \mathcal{A} = \langle \Sigma, Q, \delta, q_0, F \rangle
> $$
> 
> dove:
> - $\Sigma = \{ a_0, a_1, \ldots, a_n \}$ è un [alfabeto](Teoria%20dei%20linguaggi%20formali.md#^definizione-alfabeto),
> - $Q = \{ q_0, q_1, \ldots, q_m \}$ è un insieme finito%% link %% di **stati**,
> - $\delta \colon S \times \Sigma \to \mathcal{P}(Q)$ è una [funzione](Funzioni.md#^definizione-funzione) detta **funzione di transizione fra stati** (in cui $\mathcal{P}(Q)$ è l'[insieme delle parti](Teoria%20degli%20insiemi.md#^definizione-insieme-delle-parti) di $Q$),
> - $q_0 \in Q$ è uno stato detto **stato iniziale** e
> - $F \subseteq Q$ è un [insieme](Teoria%20degli%20insiemi.md#^definizione-insieme) di stati detti **stati finali**.
^definizione-automa-a-stati-finiti-non-deterministico-nfa

In particolare, se $\delta(q,a)$ è un [singoletto](Teoria%20degli%20insiemi.md#^definizione-singoletto), allora abbiamo solo una scelta possibile per la transizione (che è esattamente come si comporta il [DFA](Teoria%20degli%20automi.md#^definizione-automa-a-stati-finiti-deterministico-dfa)), mentre se è un [insieme vuoto](Teoria%20degli%20insiemi.md#^definizione-insieme-vuoto) allora l'[NFA](Teoria%20degli%20automi.md#^definizione-automa-a-stati-finiti-non-deterministico-nfa) rifiuta automaticamente la [stringa](Teoria%20dei%20linguaggi%20formali.md#^definizione-stringa).

> [!esempio]- Esempio: stringhe che terminano con $\color{#7F7FFF} \text{abb}$ con un NFA
> 
> Definiamo un [DFA](Teoria%20degli%20automi.md#^definizione-automa-a-stati-finiti-deterministico-dfa) che riconosce le [stringhe](Teoria%20dei%20linguaggi%20formali.md#^definizione-stringa) su $\Sigma = \{ \text{a},\text{b} \}$ che terminano in $\text{abb}$:
> 
> ![esempio-stringhe-che-terminano-con-abb-con-un-nfa-1](esempio-stringhe-che-terminano-con-abb-con-un-nfa-1.svg)
> 
> Definiamo ora un [NFA](Teoria%20degli%20automi.md#^definizione-automa-a-stati-finiti-non-deterministico-nfa) con lo stesso comportamento:
> 
> ![esempio-stringhe-che-terminano-con-abb-con-un-nfa-2](esempio-stringhe-che-terminano-con-abb-con-un-nfa-2.svg)
> 
> Possiamo notare come l'[NFA](Teoria%20degli%20automi.md#^definizione-automa-a-stati-finiti-non-deterministico-nfa) sia più semplice rispetto al [DFA](Teoria%20degli%20automi.md#^definizione-automa-a-stati-finiti-deterministico-dfa), avendo meno transizioni. Quando l'[NFA](Teoria%20degli%20automi.md#^definizione-automa-a-stati-finiti-non-deterministico-nfa) è in $q_0$ e legge una $\text{a}$ può scegliere se rimanere in $q_0$ o transire in $q_1$: per ogni [stringa](Teoria%20dei%20linguaggi%20formali.md#^definizione-stringa) letta ci sono quindi diversi percorsi alternativi che possiamo percorrere in un [NFA](Teoria%20degli%20automi.md#^definizione-automa-a-stati-finiti-non-deterministico-nfa), ma ci basta che ne esista almeno uno che ci permette di [riconoscere](Teoria%20degli%20automi.md#^definizione-linguaggio-riconosciuto-da-un-dfa) le [stringhe](Teoria%20dei%20linguaggi%20formali.md#^definizione-stringa) volute. In questo caso esiste un percorso che ci permette di [riconoscere](Teoria%20degli%20automi.md#^definizione-linguaggio-riconosciuto-da-un-dfa) le [stringhe](Teoria%20dei%20linguaggi%20formali.md#^definizione-stringa) $w \in \{ \text{a},\text{b} \}^*$ che terminano in $\text{abb}$, ovvero $w = v\text{abb}$ con $v$ [prefisso](Teoria%20dei%20linguaggi%20formali.md#^definizione-prefisso-di-una-stringa) di $w$: questo percorso è dato dalla permanenza nello [stato](Teoria%20degli%20automi.md#^definizione-automa-a-stati-finiti-non-deterministico-nfa) $q_0$ durante la lettura del [prefisso](Teoria%20dei%20linguaggi%20formali.md#^definizione-prefisso-di-una-stringa) $v$, poi si passa a $q_1$ leggendo $\text{a}$, poi a $q_2$ leggendo $\text{b}$ e si arriva allo [stato finale](Teoria%20degli%20automi.md#^definizione-automa-a-stati-finiti-non-deterministico-nfa) $q_3$ leggendo l'ultima $\text{b}$.
> 
> La [tabella di transizione](Teoria%20degli%20automi.md#^notazione-tabella-di-transizione) di questo [NFA](Teoria%20degli%20automi.md#^definizione-automa-a-stati-finiti-non-deterministico-nfa) è data da
> 
> | **Stato** | $\mathbf{a}$     | $\mathbf{b}$ |
> | --------- | ---------------- | ------------ |
> | $\to q_0$ | $\{ q_0, q_1 \}$ | $\{ q_0 \}$  |
> | $q_1$     | $\emptyset$      | $\{ q_2 \}$  |
> | $q_2$     | $\emptyset$      | $\{ q_3 \}$  |
> | $*q_3$    | $\emptyset$      | $\emptyset$  |
^esempio-stringhe-che-terminano-con-abb-con-un-nfa

> [!esempio]- Esempio: stringhe in cui ogni $\color{#7F7FFF} \text{a}$ è seguita da $\color{#7F7FFF} \text{bb}$ con un NFA
> 
> Riprendiamo l'[esempio del DFA che riconosce le stringhe in cui ogni $\text{a}$ è seguita da $\text{bb}$](Teoria%20degli%20automi.md#^esempio-stringhe-in-cui-ogni-a-e-seguita-da-bb), la cui [rappresentazione grafica](Teoria%20degli%20automi.md#^rappresentazione-grafica-di-un-automa) è la seguente:
> 
> ![esempio-stringhe-in-cui-ogni-a-e-seguita-da-bb](esempio-stringhe-in-cui-ogni-a-e-seguita-da-bb.svg)
> 
> Anche qui possiamo creare un [NFA](Teoria%20degli%20automi.md#^definizione-automa-a-stati-finiti-non-deterministico-nfa) che ha lo stesso comportamento:
> 
> ![esempio-stringhe-in-cui-ogni-a-e-seguita-da-bb-con-un-nfa](esempio-stringhe-in-cui-ogni-a-e-seguita-da-bb-con-un-nfa.svg)
> 
> Possiamo notare come l'[NFA](Teoria%20degli%20automi.md#^definizione-automa-a-stati-finiti-non-deterministico-nfa) ha uno [stato](Teoria%20degli%20automi.md#^definizione-automa-a-stati-finiti-non-deterministico-nfa) in meno rispetto al [DFA](Teoria%20degli%20automi.md#^definizione-automa-a-stati-finiti-deterministico-dfa) e anche meno [transizioni](Teoria%20degli%20automi.md#^definizione-automa-a-stati-finiti-non-deterministico-nfa), risultando anche in questo caso più semplice.
> 
> La sua [tabella di transizione](Teoria%20degli%20automi.md#^notazione-tabella-di-transizione) è la seguente:
> 
> | **Stato** | $\mathbf{a}$ | $\mathbf{b}$ |
> | --------- | ------------ | ------------ |
> | $\to*q_0$ | $\{ q_1 \}$  | $\{ q_0 \}$  |
> | $q_1$     | $\emptyset$  | $\{ q_2 \}$  |
> | $q_2$     | $\emptyset$  | $\{ q_0 \}$  |
^esempio-stringhe-in-cui-ogni-a-e-seguita-da-bb-con-un-nfa

Adattiamo le definizioni di [_funzione di transizione estesa_](Teoria%20degli%20automi.md#^definizione-funzione-di-transizione-estesa-di-un-dfa) e di [_linguaggio riconosciuto_](Teoria%20degli%20automi.md#^definizione-linguaggio-riconosciuto-da-un-dfa) agli [NFA](Teoria%20degli%20automi.md#^definizione-automa-a-stati-finiti-non-deterministico-nfa).

> [!definizione]+ Definizione: funzione di transizione estesa di un NFA
> 
> In un [NFA](Teoria%20degli%20automi.md#^definizione-automa-a-stati-finiti-non-deterministico-nfa) $\mathcal{A} = \langle \Sigma, Q, \delta, q_0, F \rangle$, la **funzione di transizione estesa** $\hat\delta \colon Q \times \Sigma^* \to \mathcal{P}(Q)$ è una [funzione](Funzioni.md#^definizione-funzione) definita induttivamente%% link %% sul suo secondo argomento così come segue:
> 
> $$
> \begin{align*}
> \hat\delta(q, \varepsilon) &= \{ q \} \\
> \hat\delta(q, wa) &= \{ r \in \delta(p,a) \mid p \in \hat\delta(q,w) \}
> \end{align*}
> $$
^definizione-funzione-di-transizione-estesa-di-un-nfa

> [!definizione]+ Definizione: linguaggio riconosciuto da un NFA
> 
> Dato un [NFA](Teoria%20degli%20automi.md#^definizione-automa-a-stati-finiti-non-deterministico-nfa) $\mathcal{A} = \langle \Sigma, Q, \delta, q_0, F \rangle$, il **linguaggio riconosciuto** (o **accettato**) $L(A)$ da $\cal A$ è il [linguaggio formale](Teoria%20dei%20linguaggi%20formali.md#^definizione-linguaggio-formale) dato dalla [chiusura di Kleene](Teoria%20dei%20linguaggi%20formali.md#^definizione-chiusura-di-kleene-su-un-alfabeto) $\Sigma^*$ in cui, per ogni [stringa](Teoria%20dei%20linguaggi%20formali.md#^definizione-stringa) $w \in \Sigma^*$, la [funzione di transizione estesa](Teoria%20degli%20automi.md#^definizione-funzione-di-transizione-estesa-di-un-nfa) restituisce almeno uno [stato finale](Teoria%20degli%20automi.md#^definizione-automa-a-stati-finiti-non-deterministico-nfa):
> 
> $$
> L(\mathcal{A}) = \{ w \in \Sigma^* \mid \hat\delta(q_0, w) \cap F \ne \emptyset \}
> $$
^definizione-linguaggio-riconosciuto-da-un-nfa

## 2.1 - Equivalenza tra DFA e NFA

> [!teorema]+ Teorema: da NFA a DFA
> 
> Dato un [NFA](Teoria%20degli%20automi.md#^definizione-automa-a-stati-finiti-non-deterministico-nfa) $\cal N$, esiste un [DFA](Teoria%20degli%20automi.md#^definizione-automa-a-stati-finiti-deterministico-dfa) $\cal D$ tale che il [linguaggio riconosciuto](Teoria%20degli%20automi.md#^definizione-linguaggio-riconosciuto-da-un-dfa) $L(\mathcal{N})$ da $\mathcal{N}$ è uguale al [linguaggio riconosciuto](Teoria%20degli%20automi.md#^definizione-linguaggio-riconosciuto-da-un-nfa) $L(\mathcal{D})$ da $\cal D$:
> 
> $$
> \forall \mathcal{N}, \exists \mathcal{D} . \big( 
> L(\mathcal{N}) = L(\mathcal{D}) \big) 
> $$
^teorema-da-nfa-a-dfa

> [!dimostrazione]- Dimostrazione (parziale): da NFA a DFA
> 
> La differenza fondamentale tra [NFA](Teoria%20degli%20automi.md#^definizione-automa-a-stati-finiti-non-deterministico-nfa) e [DFA](Teoria%20degli%20automi.md#^definizione-automa-a-stati-finiti-deterministico-dfa) è che il primo può trovarsi in più [stati](Teoria%20degli%20automi.md#^definizione-automa-a-stati-finiti-non-deterministico-nfa) contemporaneamente, mentre quest'ultimo in un solo [stato](Teoria%20degli%20automi.md#^definizione-automa-a-stati-finiti-deterministico-dfa) alla volta. Per ottenere una corrispondenza tra i due, costruiamo il [DFA](Teoria%20degli%20automi.md#^definizione-automa-a-stati-finiti-deterministico-dfa) facendo corrispondere a ogni suo stato un [insieme](Teoria%20degli%20insiemi.md#^definizione-insieme) di [stati](Teoria%20degli%20automi.md#^definizione-automa-a-stati-finiti-non-deterministico-nfa) dell'[NFA](Teoria%20degli%20automi.md#^definizione-automa-a-stati-finiti-non-deterministico-nfa).
> 
> Per esempio, se dopo aver letto una certa parola l'[NFA](Teoria%20degli%20automi.md#^definizione-automa-a-stati-finiti-non-deterministico-nfa) potrebbe trovarsi negli [stati](Teoria%20degli%20automi.md#^definizione-automa-a-stati-finiti-non-deterministico-nfa) $q_1$​, $q_2$​ e $q_3$​, il [DFA](Teoria%20degli%20automi.md#^definizione-automa-a-stati-finiti-deterministico-dfa) si troverà nello [stato](Teoria%20degli%20automi.md#^definizione-automa-a-stati-finiti-deterministico-dfa) che rappresenta l'[insieme](Teoria%20degli%20insiemi.md#^definizione-insieme)
> 
> $$
> \{ q_1,q_2,q_3 \}
> $$
> 
> La [funzione di transizione del DFA](Teoria%20degli%20automi.md#^definizione-automa-a-stati-finiti-deterministico-dfa) seguirà quindi una regola molto semplice: prendi tutti gli [stati](Teoria%20degli%20automi.md#^definizione-automa-a-stati-finiti-non-deterministico-nfa) che l'[NFA](Teoria%20degli%20automi.md#^definizione-automa-a-stati-finiti-non-deterministico-nfa) potrebbe assumere, verifica per ciascuno dove si può andare leggendo il [simbolo](Teoria%20dei%20linguaggi%20formali.md#^definizione-simbolo) successivo e raggruppali in un unico [insieme](Teoria%20degli%20insiemi.md#^definizione-insieme).
> 
> Ora esprimiamo questi concetti formalmente.
> 
> Dato un [DFA](Teoria%20degli%20automi.md#^definizione-automa-a-stati-finiti-deterministico-dfa) $\mathcal{D} = \langle \Sigma, Q_\mathcal{D}, \delta_\mathcal{D}, q_0, F_\mathcal{D} \rangle$ definiamo un [NFA](Teoria%20degli%20automi.md#^definizione-automa-a-stati-finiti-non-deterministico-nfa) $\mathcal{N} = \langle \Sigma, Q_\mathcal{N}, \delta_\mathcal{N}, q_0, F_\mathcal{N} \rangle$ in cui:
> - $Q_\mathcal{D}$ è l'[insieme delle parti](Teoria%20degli%20insiemi.md#^definizione-insieme-delle-parti) di $Q_\mathcal{N}$:
> 	$$
> 	Q_\mathcal{D} = \mathcal{P}(Q_\mathcal{N})
> 	$$
> - Per ogni [stato](Teoria%20degli%20automi.md#^definizione-automa-a-stati-finiti-deterministico-dfa) $Q \in Q_\mathcal{D}$ (ossia ogni possibile [sottoinsieme](Teoria%20degli%20insiemi.md#^definizione-sottoinsieme) di $Q_\mathcal{N}$) e ogni [simbolo](Teoria%20dei%20linguaggi%20formali.md#^definizione-simbolo) $a \in \Sigma$ la [funzione di transizione](Teoria%20degli%20automi.md#^definizione-automa-a-stati-finiti-deterministico-dfa) $\delta_\mathcal{D}(Q, a)$ darà l'unione%% link a ^definizione-unione-di-n-insiemi %% di tutte le [transizioni](Teoria%20degli%20automi.md#^definizione-automa-a-stati-finiti-non-deterministico-nfa) $\delta_\mathcal{N}(q,a)$ possibili per ogni "sotto-stato" $q \in Q$:
> 	$$
> 	\forall Q \in Q_\mathcal{D}, \forall a \in \Sigma . \left( \delta_\mathcal{D}(Q,a) = \bigcup_{q \in Q} \delta_\mathcal{N}(q,a) \right)
> 	$$
> - Gli [stati finali del DFA](Teoria%20degli%20automi.md#^definizione-automa-a-stati-finiti-deterministico-dfa) $F_\mathcal{D}$ sono tali se contengono almeno uno degli [stati finali dell'NFA](Teoria%20degli%20automi.md#^definizione-automa-a-stati-finiti-non-deterministico-nfa) $F_\mathcal{N}$:
> 	$$
> 	F_\mathcal{D} = \{ q_F \in Q_\mathcal{D} \mid q_F \cap F_\mathcal{N} \ne \emptyset \}
> 	$$
> 
> A questo punto, per dimostrare che $L(\mathcal{N}) = L(\mathcal{D})$, ci basta dimostrare che, presa una qualsiasi [stringa](Teoria%20dei%20linguaggi%20formali.md#^definizione-stringa) $w \in \Sigma^*$, valga
> 
> $$
> w \in L(\mathcal{N}) \iff w \in L(\mathcal{D})
> $$
> 
> Partendo da $w \in L(\mathcal{N})$, abbiamo che, per [definizione di _linguaggio riconosciuto da un NFA_](Teoria%20degli%20automi.md#^definizione-linguaggio-riconosciuto-da-un-nfa),
> 
> $$
> w \in L(\mathcal{N}) \iff \hat\delta_{\mathcal{N}}(q_0, w) \cap F_\mathcal{N} \ne \emptyset
> $$
> 
> Si può dimostrare induttivamente%% Link %% sulla [lunghezza](Teoria%20dei%20linguaggi%20formali.md#^definizione-lunghezza-di-una-stringa) $|w|$ di $w$ (approfondire dal libro di testo [_Compilers - Principles, Techniques, and Tools_](https://openlibrary.org/books/OL59750369M/Compilers) citato nelle fonti in fondo a questa pagina) che vale
> 
> $$
> \hat\delta_\mathcal{N}(q_0,w) = \hat\delta_\mathcal{D}(\{ q_0 \},w)
> $$
> 
> e, quindi,
> 
> $$
> \hat\delta_{\mathcal{N}}(q_0, w) \cap F_\mathcal{N} \ne \emptyset \iff \hat\delta_\mathcal{D}(\{ q_0 \},w) \cap F_\mathcal{N} \ne \emptyset
> $$
> 
> ma, per la definizione di $F_\mathcal{D}$ che ci siamo dati prima, ossia $F_\mathcal{D} = \{ Q \in Q_\mathcal{D} \mid Q \cap F_\mathcal{N} \ne \emptyset \}$, allora
> 
> $$
> \hat\delta_\mathcal{D}(\{ q_0 \},w) \cap F_\mathcal{N} \ne \emptyset \iff \hat\delta_\mathcal{D}(\{ q_0 \},w) \in F_\mathcal{D}
> $$
> 
> e, finalmente,
> 
> $$
> \hat\delta_\mathcal{D}(\{ q_0 \},w) \in F_\mathcal{D} \iff w \in L(\mathcal{D})
> $$
> 
> per [definizione di _linguaggio riconosciuto da un DFA_](Teoria%20degli%20automi.md#^definizione-linguaggio-riconosciuto-da-un-dfa).
> 
> Con una serie di bi-implicazioni%% link %% abbiamo dimostrato che
> 
> $$
> w \in L(\mathcal{N}) \iff w \in L(\mathcal{D})
> $$
> 
> $\blacksquare$
^dimostrazione-parziale-da-nfa-a-dfa

> [!algoritmo]+ Algoritmo di conversione di un NFA in un DFA tramite costruzione per sottoinsiemi
> 
> Dato un [NFA](Teoria%20degli%20automi.md#^definizione-automa-a-stati-finiti-non-deterministico-nfa) $\mathcal N = \langle \Sigma, Q_{\mathcal N}, \delta_{\mathcal N}, q_0, F_{\mathcal N} \rangle$, costruiamo un [DFA](Teoria%20degli%20automi.md#^definizione-automa-a-stati-finiti-deterministico-dfa) $\mathcal D = \langle \Sigma, Q_{\mathcal D}, \delta_{\mathcal D}, \{q_0\}, F_{\mathcal D} \rangle$ equivalente attraverso i seguenti passaggi:
> 1. **Stato iniziale**: inizializziamo $Q_{\mathcal D}$ con il solo [stato](Teoria%20degli%20automi.md#^definizione-automa-a-stati-finiti-deterministico-dfa) $\{q_0\}$, che rappresenta lo [stato iniziale](Teoria%20degli%20automi.md#^definizione-automa-a-stati-finiti-non-deterministico-nfa) dell'[NFA](Teoria%20degli%20automi.md#^definizione-automa-a-stati-finiti-non-deterministico-nfa).
> 2. **Calcolo delle transizioni**: per ogni [stato](Teoria%20degli%20automi.md#^definizione-automa-a-stati-finiti-deterministico-dfa) $Q \in Q_{\mathcal D}$ e ogni [simbolo](Teoria%20dei%20linguaggi%20formali.md#^definizione-simbolo) $a \in \Sigma$, calcoliamo l'[insieme](Teoria%20degli%20insiemi.md#^definizione-insieme) degli [stati](Teoria%20degli%20automi.md#^definizione-automa-a-stati-finiti-non-deterministico-nfa) raggiungibili:
> 	$$
> 	\forall Q \in Q_\mathcal{D}, \forall a \in \Sigma . \left( \delta_\mathcal{D}(Q,a) = \bigcup_{q \in Q} \delta_\mathcal{N}(q,a) \right)
> 	$$
>    Se l'[insieme](Teoria%20degli%20insiemi.md#^definizione-insieme) ottenuto non è ancora presente in $Q_{\mathcal D}$, lo aggiungiamo agli [stati](Teoria%20degli%20automi.md#^definizione-automa-a-stati-finiti-deterministico-dfa) del [DFA](Teoria%20degli%20automi.md#^definizione-automa-a-stati-finiti-deterministico-dfa) $Q_\mathcal{D}$. In particolare, se l'[insieme](Teoria%20degli%20insiemi.md#^definizione-insieme) ottenuto è l'[insieme vuoto](Teoria%20degli%20insiemi.md#^definizione-insieme-vuoto) $\emptyset$, lo aggiungiamo come [stato pozzo](Teoria%20degli%20automi.md#^definizione-stato-pozzo), dal quale tutte le [transizioni](Teoria%20degli%20automi.md#^definizione-automa-a-stati-finiti-deterministico-dfa) riportano a sé stesso:
> 	$$
> 	\forall a \in \Sigma.\big( \delta_{\mathcal D}(\emptyset,a)=\emptyset \big) 
> 	$$
>    Ripetiamo questo passaggio per tutti i nuovi [stati](Teoria%20degli%20automi.md#^definizione-automa-a-stati-finiti-deterministico-dfa) individuati, finché non rimangono stati da esaminare.
> 3. **Individuazione degli stati finali**: consideriamo [finali](Teoria%20degli%20automi.md#^definizione-automa-a-stati-finiti-deterministico-dfa) tutti gli [stati](Teoria%20degli%20automi.md#^definizione-automa-a-stati-finiti-deterministico-dfa) $q_F \in Q_{\mathcal D}$ che contengono almeno uno [stato finale](Teoria%20degli%20automi.md#^definizione-automa-a-stati-finiti-non-deterministico-nfa) dell'[NFA](Teoria%20degli%20automi.md#^definizione-automa-a-stati-finiti-non-deterministico-nfa):
> 	$$
> 	F_\mathcal{D} = \{ q_F \in Q_\mathcal{D} \mid q_F \cap F_\mathcal{N} \ne \emptyset \}
> 	$$
^algoritmo-di-conversione-di-un-nfa-in-un-dfa-tramite-costruzione-per-sottoinsiemi

> [!esempio]- Esempio dell'algoritmo di conversione di un NFA in un DFA tramite costruzione per sottoinsiemi
> 
> Riprendiamo l'[esempio dell'NFA che riconosce le stringhe che terminano con $\text{abb}$](Teoria%20degli%20automi.md#^esempio-stringhe-che-terminano-con-abb-con-un-nfa):
> 
> ![esempio-stringhe-che-terminano-con-abb-con-un-nfa-2](esempio-stringhe-che-terminano-con-abb-con-un-nfa-2.svg)
> 
> Questo [NFA](Teoria%20degli%20automi.md#^definizione-automa-a-stati-finiti-non-deterministico-nfa) $\mathcal N = \langle \Sigma, Q_{\mathcal N}, \delta_{\mathcal N}, q_0, F_{\mathcal N} \rangle$ ha [alfabeto](Teoria%20dei%20linguaggi%20formali.md#^definizione-alfabeto) $\Sigma = \{a,b\}$, [stati](Teoria%20degli%20automi.md#^definizione-automa-a-stati-finiti-non-deterministico-nfa) $Q_{\mathcal N} = \{q_0,q_1,q_2,q_3\}$, [stato iniziale](Teoria%20degli%20automi.md#^definizione-automa-a-stati-finiti-non-deterministico-nfa) $q_0$ e [stati finali](Teoria%20degli%20automi.md#^definizione-automa-a-stati-finiti-non-deterministico-nfa) $F_{\mathcal N} = \{q_3\}$. Applichiamo l'[algoritmo di conversione di un NFA in un DFA tramite costruzione per sottoinsiemi](Teoria%20degli%20automi.md#^algoritmo-di-conversione-di-un-nfa-in-un-dfa-tramite-costruzione-per-sottoinsiemi) per ottenere il [DFA](Teoria%20degli%20automi.md#^definizione-automa-a-stati-finiti-deterministico-dfa) $\mathcal D = \langle \Sigma, Q_{\mathcal D}, \delta_{\mathcal D}, \{q_0\}, F_{\mathcal D} \rangle$ equivalente.
> 
> **Passo 1**: calcoliamo lo [stato iniziale del DFA](Teoria%20degli%20automi.md#^definizione-automa-a-stati-finiti-deterministico-dfa) che è $\{q_0\}$, che rappresenta l'unica posizione in cui l'[NFA](Teoria%20degli%20automi.md#^definizione-automa-a-stati-finiti-non-deterministico-nfa) può trovarsi prima di leggere qualsiasi [simbolo](Teoria%20dei%20linguaggi%20formali.md#^definizione-simbolo).
> 
> **Passo 2**: calcoliamo le [transizioni](Teoria%20degli%20automi.md#^definizione-automa-a-stati-finiti-deterministico-dfa). Abbiamo
> 
> $$
> Q_\mathcal{D} = \{ \{ q_0 \} \}
> $$
> 
> con $\{ q_0 \}$ da esplorare, quindi vediamo quali [stati](Teoria%20degli%20automi.md#^definizione-automa-a-stati-finiti-deterministico-dfa) otteniamo per ogni $Q \in Q_\mathcal{D} = \{ \{ q_0 \} \}$ e per ogni $a \in \Sigma = \{ \text{a},\text{b} \}$:
> 
> |                            | $\mathbf{a}$  | $\mathbf{b}$ |
> | -------------------------- | ------------- | ------------ |
> | $\boldsymbol{\to \{q_0\}}$ | $\{q_0,q_1\}$ | $\{q_0\}$    |
> 
> dove, per esempio, scelti $Q = \{ q_0 \}$ e $a = \text{a}$:
> 
> $$
> \begin{align*}
> \delta_{\mathcal D}(\{q_0\},\text{a})
> &= \bigcup_{q \in \{q_0\}} \delta_{\mathcal N}(q,\text{a}) \\
> &= \delta_{\mathcal N}(q_0,\text{a}) \\
> &= \{q_0,q_1\}
> \end{align*}
> $$
> 
> Ora abbiamo
> 
> $$
> Q_\mathcal{D} = \{ \{ q_0 \}, \{ q_0,q_1 \} \}
> $$
> 
> con $\{ q_0,q_1 \}$ da esplorare, quindi vediamo quali [stati](Teoria%20degli%20automi.md#^definizione-automa-a-stati-finiti-deterministico-dfa) otteniamo per ogni $Q \in Q_\mathcal{D} = \{ \{ q_0 \}, \{ q_0, q_1 \} \}$ e per ogni $a \in \Sigma = \{ \text{a},\text{b} \}$:
> 
> |                            | $\mathbf{a}$  | $\mathbf{b}$  |
> | -------------------------- | ------------- | ------------- |
> | $\boldsymbol{\to \{q_0\}}$ | $\{q_0,q_1\}$ | $\{q_0\}$     |
> | $\boldsymbol{\{q_0,q_1\}}$ | $\{q_0,q_1\}$ | $\{q_0,q_2\}$ |
> 
> Ora abbiamo
> 
> $$
> Q_\mathcal{D} = \{ \{ q_0 \}, \{ q_0,q_1 \},\{ q_0,q_2 \} \}
> $$
> 
> con $\{ q_0,q_2 \}$ da esplorare, quindi vediamo quali [stati](Teoria%20degli%20automi.md#^definizione-automa-a-stati-finiti-deterministico-dfa) otteniamo per ogni $Q \in Q_\mathcal{D} = \{ \{ q_0 \}, \{ q_0,q_1 \},\{ q_0,q_2 \} \}$ e per ogni $a \in \Sigma = \{ \text{a},\text{b} \}$:
> 
> |                            | $\mathbf{a}$  | $\mathbf{b}$  |
> | -------------------------- | ------------- | ------------- |
> | $\boldsymbol{\to \{q_0\}}$ | $\{q_0,q_1\}$ | $\{q_0\}$     |
> | $\boldsymbol{\{q_0,q_1\}}$ | $\{q_0,q_1\}$ | $\{q_0,q_2\}$ |
> | $\boldsymbol{\{q_0,q_2\}}$ | $\{q_0,q_1\}$ | $\{q_0,q_3\}$ |
> 
> Ora abbiamo
> 
> $$
> Q_\mathcal{D} = \{ \{ q_0 \}, \{ q_0,q_1 \},\{ q_0,q_2 \} \}
> $$
> 
> con $\{ q_0,q_2 \}$ da esplorare, quindi vediamo quali [stati](Teoria%20degli%20automi.md#^definizione-automa-a-stati-finiti-deterministico-dfa) otteniamo per ogni $Q \in Q_\mathcal{D} = \{ \{ q_0 \}, \{ q_0,q_1 \},\{ q_0,q_2 \} \}$ e per ogni $a \in \Sigma = \{ \text{a},\text{b} \}$:
> 
> |                            | $\mathbf{a}$  | $\mathbf{b}$  |
> | -------------------------- | ------------- | ------------- |
> | $\boldsymbol{\to \{q_0\}}$ | $\{q_0,q_1\}$ | $\{q_0\}$     |
> | $\boldsymbol{\{q_0,q_1\}}$ | $\{q_0,q_1\}$ | $\{q_0,q_2\}$ |
> | $\boldsymbol{\{q_0,q_2\}}$ | $\{q_0,q_1\}$ | $\{q_0,q_3\}$ |
> | $\boldsymbol{\{q_0,q_3\}}$ | $\{q_0,q_1\}$ | $\{q_0\}$     |
> 
> Questa è la [tabella di transizione](Teoria%20degli%20automi.md#^notazione-tabella-di-transizione) del nostro nuovo [DFA](Teoria%20degli%20automi.md#^definizione-automa-a-stati-finiti-deterministico-dfa).
> 
> **Passo 3**: individuazione degli [stati finali](Teoria%20degli%20automi.md#^definizione-automa-a-stati-finiti-deterministico-dfa). Uno [stato](Teoria%20degli%20automi.md#^definizione-automa-a-stati-finiti-deterministico-dfa) del [DFA](Teoria%20degli%20automi.md#^definizione-automa-a-stati-finiti-deterministico-dfa) è [finale](Teoria%20degli%20automi.md#^definizione-automa-a-stati-finiti-deterministico-dfa) se contiene almeno uno [stato finale](Teoria%20degli%20automi.md#^definizione-automa-a-stati-finiti-non-deterministico-nfa) dell'[NFA](Teoria%20degli%20automi.md#^definizione-automa-a-stati-finiti-non-deterministico-nfa). Poiché $F_{\mathcal N}=\{q_3\}$, l'unico insieme raggiungibile che contiene $q_3$ è $\{q_0,q_3\}$. Pertanto:
> 
> $$
> F_{\mathcal D} = \{\{q_0,q_3\}\}
> $$
> 
> Questa è la [tabella di transizione](Teoria%20degli%20automi.md#^notazione-tabella-di-transizione) finale del nostro nuovo [DFA](Teoria%20degli%20automi.md#^definizione-automa-a-stati-finiti-deterministico-dfa) $\mathcal D = \langle \Sigma,Q_{\mathcal D},\delta_{\mathcal D},\{q_0\},F_{\mathcal D} \rangle$ è la seguente:
> 
> |                             | $\mathbf{a}$  | $\mathbf{b}$  |
> | --------------------------- | ------------- | ------------- |
> | $\boldsymbol{\to \{q_0\}}$  | $\{q_0,q_1\}$ | $\{q_0\}$     |
> | $\boldsymbol{\{q_0,q_1\}}$  | $\{q_0,q_1\}$ | $\{q_0,q_2\}$ |
> | $\boldsymbol{\{q_0,q_2\}}$  | $\{q_0,q_1\}$ | $\{q_0,q_3\}$ |
> | $\boldsymbol{*\{q_0,q_3\}}$ | $\{q_0,q_1\}$ | $\{q_0\}$     |
> 
> La sua [rappresentazione grafica](Teoria%20degli%20automi.md#^rappresentazione-grafica-di-un-automa) è la seguente:
> 
> ![esempio-dell-algoritmo-di-conversione-di-un-nfa-in-un-dfa](esempio-dell-algoritmo-di-conversione-di-un-nfa-in-un-dfa.svg)
> 
> Possiamo notare che il [DFA](Teoria%20degli%20automi.md#^definizione-automa-a-stati-finiti-deterministico-dfa) appena costruito coincide sostanzialmente con il [DFA dell'esempio da cui eravamo partiti per generare un NFA equivalente](Teoria%20degli%20automi.md#^esempio-stringhe-che-terminano-con-abb-con-un-nfa):
>  ![esempio-stringhe-che-terminano-con-abb-con-un-nfa-1](esempio-stringhe-che-terminano-con-abb-con-un-nfa-1.svg)
> 
> L'unica differenza riguarda i nomi degli [stati](Teoria%20degli%20automi.md#^definizione-automa-a-stati-finiti-deterministico-dfa): mentre nel [DFA](Teoria%20degli%20automi.md#^definizione-automa-a-stati-finiti-deterministico-dfa) ottenuto tramite la [conversione da NFA](Teoria%20degli%20automi.md#^algoritmo-di-conversione-di-un-nfa-in-un-dfa-tramite-costruzione-per-sottoinsiemi) questi siano rappresentati come "insiemi" di stati, vanno comunque intesi come semplici etichette, prive di un significato intrinseco. Per esempio, lo stato $\{q_0,q_1\}$, che nel DFA originale corrisponde allo stato $q_1$, avrebbe potuto essere chiamato arbitrariamente anche _Pippo_, senza modificare il funzionamento dell'automa, perché ciò che importa davvero sono le [transizioni tra stati](Teoria%20degli%20automi.md#^definizione-automa-a-stati-finiti-deterministico-dfa).

> [!esercizio]+ Esercizio 1 sull'algoritmo di conversione
> 
> Prendi l'[NFA che riconosce le stringhe in cui ogni $\text{a}$ è seguita da $\text{bb}$](Teoria%20degli%20automi.md#^esempio-stringhe-in-cui-ogni-a-e-seguita-da-bb-con-un-nfa) la cui [rappresentazione grafica](Teoria%20degli%20automi.md#^rappresentazione-grafica-di-un-automa) è
> 
> ![esempio-stringhe-in-cui-ogni-a-e-seguita-da-bb-con-un-nfa](esempio-stringhe-in-cui-ogni-a-e-seguita-da-bb-con-un-nfa.svg)
> 
> e, tramite l'[algoritmo di conversione tramite costruzione per sottoinsiemi](Teoria%20degli%20automi.md#^algoritmo-di-conversione-di-un-nfa-in-un-dfa-tramite-costruzione-per-sottoinsiemi), trasformalo in un [DFA](Teoria%20degli%20automi.md#^definizione-automa-a-stati-finiti-deterministico-dfa).

%% 
fare soluzione
%%

> [!teorema]+ Teorema: da DFA a NFA
> 
> Dato un [DFA](Teoria%20degli%20automi.md#^definizione-automa-a-stati-finiti-deterministico-dfa) $\cal D$, esiste un [NFA](Teoria%20degli%20automi.md#^definizione-automa-a-stati-finiti-non-deterministico-nfa) $\cal N$ tale che il [linguaggio riconosciuto](Teoria%20degli%20automi.md#^definizione-linguaggio-riconosciuto-da-un-dfa) $L(\mathcal{D})$ da $\mathcal{D}$ è uguale al [linguaggio riconosciuto](Teoria%20degli%20automi.md#^definizione-linguaggio-riconosciuto-da-un-nfa) $L(\mathcal{N})$ da $\cal N$:
> 
> $$
> \forall \mathcal{D}, \exists \mathcal{N} . \big( 
> L(\mathcal{D}) = L(\mathcal{N}) \big) 
> $$
^teorema-da-dfa-a-nfa

> [!dimostrazione]- Dimostrazione: da DFA a NFA
> 
> Dato un [DFA](Teoria%20degli%20automi.md#^definizione-automa-a-stati-finiti-deterministico-dfa) $\mathcal{D} = \langle \Sigma, Q, \delta_\mathcal{D}, q_0, F \rangle$ definiamo un [NFA](Teoria%20degli%20automi.md#^definizione-automa-a-stati-finiti-non-deterministico-nfa) $\mathcal{N} = \langle \Sigma, Q, \delta_\mathcal{N}, q_0, F \rangle$ (notare la differenza tra il $\delta_\mathcal{D}$ di $\mathcal{D}$ e il $\delta_\mathcal{N}$ di $\mathcal{N}$) in cui
> 
> $$
> \delta_\mathcal{N}(q,a) = \{ \delta_\mathcal{D}(q,a) \}
> $$
> 
> Si può dimostrare per induzione%% link %% sulla [lunghezza](Teoria%20dei%20linguaggi%20formali.md#^definizione-lunghezza-di-una-stringa) $|w|$ di una qualsiasi [stringa](Teoria%20dei%20linguaggi%20formali.md#^definizione-stringa) $w \in \Sigma^*$ che
> 
> $$
> \hat\delta_\mathcal{D}(q_0, w) = q_f \iff \hat\delta_\mathcal{N}(q_0, w) = \{ q_f \}
> $$
> 
> (ossia sia la [funzione di transizione estesa di un DFA](Teoria%20degli%20automi.md#^definizione-funzione-di-transizione-estesa-di-un-dfa) $\hat\delta_\mathcal{D}$ che [quella di un NFA](Teoria%20degli%20automi.md#^definizione-funzione-di-transizione-estesa-di-un-nfa) $\hat\delta_\mathcal{N}$ producono entrambi lo stesso [stato finale](Teoria%20degli%20automi.md#^definizione-automa-a-stati-finiti-non-deterministico-nfa) $q_f \in Q$), da cui si conclude che
> 
> $$
> \hat\delta_\mathcal{D}(q_0, w) \in F \iff \hat\delta_\mathcal{N}(q_0, w) \cap F \ne \emptyset
> $$
> 
> Poiché quindi entrambi gli automi raggiungono lo stesso stato finale per le stesse parole, abbiamo dimostrato che
> 
> $$
> L(\mathcal{D}) = L(\mathcal{N})
> $$
> 
> $\blacksquare$

Tecnicamente, un [DFA](Teoria%20degli%20automi.md#^definizione-automa-a-stati-finiti-deterministico-dfa) è già di per sè un [NFA](Teoria%20degli%20automi.md#^definizione-automa-a-stati-finiti-non-deterministico-nfa), motivo per cui non c'è bisogno di usare un particolare algoritmo per fare la conversione.

%% 
Algoritmo per ridurre gli stati inutili di un NFA
%%

> [!corollario]+ Corollario: equivalenza tra DFA e NFA
>
> I [DFA](Teoria%20degli%20automi.md#^definizione-automa-a-stati-finiti-deterministico-dfa) e gli [NFA](Teoria%20degli%20automi.md#^definizione-automa-a-stati-finiti-non-deterministico-nfa) hanno la stessa potenza espressiva, ossia riconoscono esattamente gli stessi [linguaggi formali](Teoria%20dei%20linguaggi%20formali.md#^definizione-linguaggio-formale) e sono quindi equivalenti da questo punto di vista:
>
> $$
> \begin{array}{}
> \forall \mathcal{D}, \exists \mathcal{N} . \big( L(\mathcal{D}) = L(\mathcal{N}) \big) \\
> \land \\
> \forall \mathcal{N}, \exists \mathcal{D} . \big( L(\mathcal{N}) = L(\mathcal{D}) \big) 
> \end{array}
> $$
^corollario-equivalenza-tra-dfa-e-nfa

> [!dimostrazione]- Dimostrazione: equivalenza tra DFA e NFA
>
> Per il [primo teorema](Teoria%20degli%20automi.md#^teorema-da-dfa-a-nfa), per ogni [DFA](Teoria%20degli%20automi.md#^definizione-automa-a-stati-finiti-deterministico-dfa) esiste un [NFA](Teoria%20degli%20automi.md#^definizione-automa-a-stati-finiti-non-deterministico-nfa) che [riconosce](Teoria%20degli%20automi.md#^definizione-linguaggio-riconosciuto-da-un-nfa) lo stesso [linguaggio](Teoria%20dei%20linguaggi%20formali.md#^definizione-linguaggio-formale); viceversa, per il [secondo teorema](Teoria%20degli%20automi.md#^teorema-da-nfa-a-dfa) è vero il contrario: abbiamo quindi che le due tipologie di automi riconoscono gli stessi [linguaggi formali](Teoria%20dei%20linguaggi%20formali.md#^definizione-linguaggio-formale).
> 
> $\blacksquare$

> [!osservazione]+ Osservazione: linguaggi regolari riconosciuti da un NFA
> 
> Dal momento che [DFA ed NFA sono equivalenti](Teoria%20degli%20automi.md#^corollario-equivalenza-tra-dfa-e-nfa), possiamo caratterizzare un [linguaggio regolare](Teoria%20degli%20automi.md#^definizione-linguaggio-regolare) $L$ anche attraverso un [NFA](Teoria%20degli%20automi.md#^definizione-automa-a-stati-finiti-non-deterministico-nfa) $\mathcal{N}$ che lo [riconosce](Teoria%20degli%20automi.md#^definizione-linguaggio-riconosciuto-da-un-nfa).
^osservazione-linguaggi-regolari-riconosciuti-da-un-nfa

%% 
Esercizio: definire un NFA che riconosce le stringhe di 0 e 1 in cui il terzultimo simbolo è un 1

Esercizio: Convertire in DFA l’NFA dell’esercizio precedente

Esercizio: disegnare i diagrammi di transizione dei seguenti NFA e convertirli in DFA

|                      | $\boldsymbol{0}$ | $\boldsymbol{1}$ |
| -------------------- | ---------------- | ---------------- |
| $\boldsymbol{\to p}$ | $\{ p,q \}$      | $\{ p \}$        |
| $\boldsymbol{q}$     | $\{ r \}$        | $\{ r \}$        |
| $\boldsymbol{r}$     | $\{ s \}$        | $\emptyset$      |
| $\boldsymbol{*s}$    | $\{ s \}$        | $\{ s \}$        |

|                      | $\boldsymbol{0}$ | $\boldsymbol{1}$ |
| -------------------- | ---------------- | ---------------- |
| $\boldsymbol{\to p}$ | $\{ q,s \}$      | $\{ q \}$        |
| $\boldsymbol{*q}$    | $\{ r \}$        | $\{ q,r \}$      |
| $\boldsymbol{r}$     | $\{ s \}$        | $\{ p \}$        |
| $\boldsymbol{*s}$    | $\emptyset$      | $\{ p \}$        |

Esercizio: Definire un NFA sull’alfabeto {a, c, e, n, s} che riconosca le parole cane, casa e cena, poi convertirlo in DFA
%%

# 3 - $\varepsilon$-NFA

Abbiamo visto la classe dei [DFA](Teoria%20degli%20automi.md#^definizione-automa-a-stati-finiti-deterministico-dfa) $\mathcal{A} = \langle \Sigma, Q, \delta, q_0, F \rangle$ in cui a ogni [simbolo](Teoria%20dei%20linguaggi%20formali.md#^definizione-simbolo) $a \in \Sigma$ corrisponde una [transizione](Teoria%20degli%20automi.md#^definizione-automa-a-stati-finiti-deterministico-dfa) a uno [stato](Teoria%20degli%20automi.md#^definizione-automa-a-stati-finiti-deterministico-dfa) $q \in Q$ e la classe degli [NFA](Teoria%20degli%20automi.md#^definizione-automa-a-stati-finiti-non-deterministico-nfa) in cui a ogni [simbolo](Teoria%20dei%20linguaggi%20formali.md#^definizione-simbolo) $a \in \Sigma$ corrisponde una [transizione](Teoria%20degli%20automi.md#^definizione-automa-a-stati-finiti-deterministico-dfa) a uno o più [stati](Teoria%20degli%20automi.md#^definizione-automa-a-stati-finiti-non-deterministico-nfa) $Q' \subseteq Q$.

Ma cosa succederebbe se fosse possibile effettuare una [transizione](Teoria%20degli%20automi.md#^definizione-automa-a-stati-finiti-deterministico-dfa) verso uno [stato](Teoria%20degli%20automi.md#^definizione-automa-a-stati-finiti-deterministico-dfa) successivo **spontaneamente**, senza dover leggere alcun [simbolo](Teoria%20dei%20linguaggi%20formali.md#^definizione-simbolo) $a \in \Sigma$? In altre parole, sarebbe possibile passare da uno [stato](Teoria%20degli%20automi.md#^definizione-automa-a-stati-finiti-deterministico-dfa) a un altro senza consumare alcun simbolo dell'input, come se l'automa potesse spostarsi da uno stato all'altro usando la [stringa vuota](Teoria%20dei%20linguaggi%20formali.md#^definizione-stringa-vuota) $\varepsilon$?

Ecco che quindi introduciamo gli [_$\varepsilon$-NFA_](Teoria%20degli%20automi.md#^definizione-automa-a-stati-finiti-non-deterministico-con-e-transizioni-enfa).

> [!definizione]+ Definizione: automa a stati finiti non deterministico con $\color{#FF7FFF} \boldsymbol{\varepsilon}$-transizioni ($\boldsymbol{\varepsilon}$-NFA)
> 
> Un **automa a stati finiti non deterministico con $\boldsymbol{\varepsilon}$-transizioni** (**$\boldsymbol{\varepsilon}$-NFA**, dall'inglese _**$\boldsymbol{\varepsilon}$**-transitions **N**on-deterministic **F**inite-state **A**utomaton_) è una [quintupla](Teoria%20degli%20insiemi.md#^definizione-tupla)
> 
> $$
> \mathcal{A} = \langle \Sigma, Q, \delta, q_0, F \rangle
> $$
> 
> dove:
> - $\Sigma = \{ a_0, a_1, \ldots, a_n \}$ è un [alfabeto](Teoria%20dei%20linguaggi%20formali.md#^definizione-alfabeto),
> - $Q = \{ q_0, q_1, \ldots, q_m \}$ è un insieme finito%% link %% di **stati**,
> - $\delta \colon S \times (\Sigma \cup \{ \varepsilon \}) \to \mathcal{P}(Q)$ è una [funzione](Funzioni.md#^definizione-funzione) detta **funzione di transizione fra stati** (in cui $\mathcal{P}(Q)$ è l'[insieme delle parti](Teoria%20degli%20insiemi.md#^definizione-insieme-delle-parti) di $Q$),
> - $q_0 \in Q$ è uno stato detto **stato iniziale** e
> - $F \subseteq Q$ è un [insieme](Teoria%20degli%20insiemi.md#^definizione-insieme) di stati detti **stati finali**.
^definizione-automa-a-stati-finiti-non-deterministico-con-e-transizioni-enfa

Ma a cosa potrebbero servirci queste [$\varepsilon$-transizioni](Teoria%20degli%20automi.md#^definizione-automa-a-stati-finiti-non-deterministico-con-e-transizioni-enfa)? Banalmente, potrebbero servirci per rappresentare delle _parti facoltative_ di una [stringa](Teoria%20dei%20linguaggi%20formali.md#^definizione-stringa) da riconoscere, oppure per costruire agevolmente automi complessi in maniera modulare.

> [!esempio]- Esempio: $\color{#7F7FFF} \varepsilon$-NFA che riconosce numeri interi
> 
> Vediamo un caso in cui potrebbe tornarci utile un [$\varepsilon$-NFA](Teoria%20degli%20automi.md#^rappresentazione-grafica-di-un-automa): i numeri interi $\mathbb{Z}$%% link %%, in cui ogni numero%% link %% ha un segno davanti ($+$ o $-$) e, per comodità, facciamo queste due semplificazioni:
> 1. Anche se dal punto di vista matematico stiamo commettendo un'eresia%% link all'unicità dello $0$ %%, facciamo finta che anche lo $0$ possa avere segno, ergo accetteremo sia $+0$ che $-0$.
> 2. Accetteremo anche numeri che avranno lo $0$ come prima cifra (es. $-042$ sarà accettato).
> 
> Creiamo un [NFA](Teoria%20degli%20automi.md#^definizione-automa-a-stati-finiti-non-deterministico-nfa) che riconosce questi numeri%% Link %%:
> 
> ![esempio-enfa-che-riconosce-numeri-interi-nfa](esempio-enfa-che-riconosce-numeri-interi-nfa.svg)
> 
> Tuttavia, noi sappiamo che per scrivere i numeri interi $\mathbb{Z}$%% link %% non è necessario mettere il segno davanti al numero, per esempio se scriviamo $304$ sappiamo che in realtà intendiamo $+304$. Ecco che qui può tornarci utile l'[$\varepsilon$-NFA](Teoria%20degli%20automi.md#^definizione-automa-a-stati-finiti-non-deterministico-con-e-transizioni-enfa): tra i [simboli](Teoria%20dei%20linguaggi%20formali.md#^definizione-simbolo) accettabili nella [transizione](Teoria%20degli%20automi.md#^definizione-automa-a-stati-finiti-non-deterministico-con-e-transizioni-enfa) dallo [stato](Teoria%20degli%20automi.md#^definizione-automa-a-stati-finiti-non-deterministico-con-e-transizioni-enfa) $q_0$ e $q_1$, oltre al $+$ e al $-$, accettiamo anche la [stringa vuota](Teoria%20dei%20linguaggi%20formali.md#^definizione-stringa-vuota) $\varepsilon$, per indicare che possiamo anche omettere il segno davanti al numero:
> 
> ![esempio-enfa-che-riconosce-numeri-interi-enfa-1](esempio-enfa-che-riconosce-numeri-interi-enfa-1.svg)
> 
> In realtà possiamo ancora espandere questo [$\varepsilon$-NFA](Teoria%20degli%20automi.md#^definizione-automa-a-stati-finiti-non-deterministico-con-e-transizioni-enfa) eliminando le due semplificazioni che avevamo stabilito prima, ossia facendo sì che lo $0$ non abbia segno (aggiungendo uno [stato finale](Teoria%20degli%20automi.md#^definizione-automa-a-stati-finiti-non-deterministico-con-e-transizioni-enfa) $q_3$) e che un numero non possa avere degli $0$ davanti togliendo il [simbolo](Teoria%20dei%20linguaggi%20formali.md#^definizione-simbolo) $0$ nella transizione dallo [stato](Teoria%20degli%20automi.md#^definizione-automa-a-stati-finiti-non-deterministico-con-e-transizioni-enfa) $q_1$ al $q_2$:
> 
> ![esempio-enfa-che-riconosce-numeri-interi-enfa-2](esempio-enfa-che-riconosce-numeri-interi-enfa-2.svg)
^esempio-enfa-che-riconosce-numeri-interi

Introduciamo ora la [_$\varepsilon$-chiusura_](Teoria%20degli%20automi.md#^definizione-e-chiusura-di-uno-stato) che ci serve per tenere comodamente traccia di tutte le [$\varepsilon$-transizioni](Teoria%20degli%20automi.md#^definizione-automa-a-stati-finiti-non-deterministico-con-e-transizioni-enfa) che possiamo effettuare a partire da un certo [stato](Teoria%20degli%20automi.md#^definizione-automa-a-stati-finiti-non-deterministico-con-e-transizioni-enfa) $q$, ossia fin dove possiamo spingerci partendo da $q$ senza consumare alcun [simbolo](Teoria%20dei%20linguaggi%20formali.md#^definizione-simbolo) in ingresso.

> [!definizione]+ Definizione: $\color{#FF7FFF} \varepsilon$-chiusura di uno stato
> 
> Dato un [$\varepsilon$-NFA](Teoria%20degli%20automi.md#^definizione-automa-a-stati-finiti-non-deterministico-con-e-transizioni-enfa) $\mathcal{A} = \langle \Sigma, Q, \delta, q_0, F \rangle$ e uno [stato](Teoria%20degli%20automi.md#^definizione-automa-a-stati-finiti-non-deterministico-con-e-transizioni-enfa) $q \in Q$, la sua **$\varepsilon$-chiusura** $\text{ECLOSE}(q)$ è il più piccolo [insieme](Teoria%20degli%20insiemi.md#^definizione-insieme) di [stati](Teoria%20degli%20automi.md#^definizione-automa-a-stati-finiti-non-deterministico-con-e-transizioni-enfa) tale che:
> 1. $q$ fa parte della sua chiusura $\text{ECLOSE}(q)$:
> 	$$
> 	q \in \text{ECLOSE}(q)
> 	$$
> 2. Se un certo [stato](Teoria%20degli%20automi.md#^definizione-automa-a-stati-finiti-non-deterministico-con-e-transizioni-enfa) $p \in Q$ fa parte della chiusura $\text{ECLOSE}(q)$, allora anche tutti gli [stati](Teoria%20degli%20automi.md#^definizione-automa-a-stati-finiti-non-deterministico-con-e-transizioni-enfa) raggiungibili da $p$ tramite [$\varepsilon$-transizioni](Teoria%20degli%20automi.md#^definizione-automa-a-stati-finiti-non-deterministico-con-e-transizioni-enfa) fanno parte di $\text{ECLOSE}(q)$:
> 	$$
> 	p \in \text{ECLOSE}(q) \implies \delta(p,\varepsilon) \subseteq \text{ECLOSE}(q)
> 	$$
^definizione-e-chiusura-di-uno-stato

Facciamo subito un esempio per capire come si costruisce una [$\varepsilon$-chiusura](Teoria%20degli%20automi.md#^definizione-e-chiusura-di-uno-stato).

> [!esempio]- Esempio: $\color{#7F7FFF} \varepsilon$-chiusura di uno stato
> 
> Prendiamo questo [$\varepsilon$-NFA](Teoria%20degli%20automi.md#^definizione-automa-a-stati-finiti-non-deterministico-con-e-transizioni-enfa):
> 
> ![esempio-e-chiusura-di-uno-stato](esempio-e-chiusura-di-uno-stato.svg)
> 
> Partendo dallo [stato](Teoria%20degli%20automi.md#^definizione-automa-a-stati-finiti-non-deterministico-con-e-transizioni-enfa) $q_1$, possiamo calcolare la sua [$\varepsilon$-chiusura](Teoria%20degli%20automi.md#^definizione-e-chiusura-di-uno-stato) $\text{ECLOSE}(q_1)$ ricorsivamente:
> - Per la [regola 1 delle $\varepsilon$-chiusure](Teoria%20degli%20automi.md#^definizione-e-chiusura-di-uno-stato), $q_1$ fa automaticamente parte di $\text{ECLOSE}(q_1)$:
> 	$$
> 	\text{ECLOSE}(q_1) = \{ q_1 \}
> 	$$
> - Per la [regola 2 delle $\varepsilon$-chiusure](Teoria%20degli%20automi.md#^definizione-e-chiusura-di-uno-stato), dato che $q_1 \in \text{ECLOSE}(q_1)$, allora anche tutti gli [stati](Teoria%20degli%20automi.md#^definizione-automa-a-stati-finiti-non-deterministico-con-e-transizioni-enfa) raggiungibili da $q_1$ tramite [$\varepsilon$-transizioni](Teoria%20degli%20automi.md#^definizione-automa-a-stati-finiti-non-deterministico-con-e-transizioni-enfa) fanno parte della [$\varepsilon$-chiusura](Teoria%20degli%20automi.md#^definizione-e-chiusura-di-uno-stato) $\text{ECLOSE}(q_1)$:
> 	$$
> 	\text{ECLOSE}(q_1) = \{ q_1, q_2, q_4 \}
> 	$$
> - Per la [regola 2 delle $\varepsilon$-chiusure](Teoria%20degli%20automi.md#^definizione-e-chiusura-di-uno-stato), dato che $q_2 \in \text{ECLOSE}(q_1)$, allora anche tutti gli [stati](Teoria%20degli%20automi.md#^definizione-automa-a-stati-finiti-non-deterministico-con-e-transizioni-enfa) raggiungibili da $q_2$ tramite [$\varepsilon$-transizioni](Teoria%20degli%20automi.md#^definizione-automa-a-stati-finiti-non-deterministico-con-e-transizioni-enfa) fanno parte della [$\varepsilon$-chiusura](Teoria%20degli%20automi.md#^definizione-e-chiusura-di-uno-stato) $\text{ECLOSE}(q_1)$:
> 	$$
> 	\text{ECLOSE}(q_1) = \{ q_1, q_2, q_3, q_4 \}
> 	$$
> - Per la [regola 2 delle $\varepsilon$-chiusure](Teoria%20degli%20automi.md#^definizione-e-chiusura-di-uno-stato), dato che $q_3 \in \text{ECLOSE}(q_1)$, allora anche tutti gli [stati](Teoria%20degli%20automi.md#^definizione-automa-a-stati-finiti-non-deterministico-con-e-transizioni-enfa) raggiungibili da $q_3$ tramite [$\varepsilon$-transizioni](Teoria%20degli%20automi.md#^definizione-automa-a-stati-finiti-non-deterministico-con-e-transizioni-enfa) fanno parte della [$\varepsilon$-chiusura](Teoria%20degli%20automi.md#^definizione-e-chiusura-di-uno-stato) $\text{ECLOSE}(q_1)$:
> 	$$
> 	\text{ECLOSE}(q_1) = \{ q_1, q_2, q_3, q_4, q_6 \}
> 	$$
> 
> Da $q_4$ e $q_6$ non partono [$\varepsilon$-transizioni](Teoria%20degli%20automi.md#^definizione-automa-a-stati-finiti-non-deterministico-con-e-transizioni-enfa) ad altri [stati](Teoria%20degli%20automi.md#^definizione-automa-a-stati-finiti-non-deterministico-con-e-transizioni-enfa), di conseguenza la costruzione di $\text{ECLOSE}(q_1)$ è terminata. Da notare che $q_7 \not \in \text{ECLOSE}(q_1)$ perché, anche se ci si può arrivare tramite una [$\varepsilon$-transizione](Teoria%20degli%20automi.md#^definizione-automa-a-stati-finiti-non-deterministico-con-e-transizioni-enfa) da $q_5$, per arrivare a $q_5$ dobbiamo necessariamente consumare il [simbolo](Teoria%20dei%20linguaggi%20formali.md#^definizione-simbolo) $\text{a}$.
> 
> Invece, se consideriamo la [$\varepsilon$-chiusura](Teoria%20degli%20automi.md#^definizione-e-chiusura-di-uno-stato) $\text{ECLOSE}(q_5)$ di $q_5$, abbiamo che
> 
> $$
> \text{ECLOSE}(q_5) = \{ q_5,q_7 \}
> $$
> 
> perché possiamo raggiungere $q_7$ da $q_5$ tramite una [$\varepsilon$-transizione](Teoria%20degli%20automi.md#^definizione-automa-a-stati-finiti-non-deterministico-con-e-transizioni-enfa): non importa che $q_7$ sia raggiungibile anche tramite il [simbolo](Teoria%20dei%20linguaggi%20formali.md#^definizione-simbolo) $\text{c}$, ci basta che accetti almeno la [stringa vuota](Teoria%20dei%20linguaggi%20formali.md#^definizione-stringa-vuota) $\varepsilon$.

Possiamo anche generalizzare questa definizione di [$\varepsilon$-chiusura](Teoria%20degli%20automi.md#^definizione-e-chiusura-di-uno-stato) a un [insieme](Teoria%20degli%20insiemi.md#^definizione-insieme) di [stati](Teoria%20degli%20automi.md#^definizione-automa-a-stati-finiti-non-deterministico-con-e-transizioni-enfa).

> [!definizione]+ Definizione: $\color{#FF7FFF} \varepsilon$-chiusura di un insieme di stati
> 
> Dato un [$\varepsilon$-NFA](Teoria%20degli%20automi.md#^definizione-automa-a-stati-finiti-non-deterministico-con-e-transizioni-enfa) $\mathcal{A} = \langle \Sigma, Q, \delta, q_0, F \rangle$ e un [insieme](Teoria%20degli%20insiemi.md#^definizione-insieme) di [stati](Teoria%20degli%20automi.md#^definizione-automa-a-stati-finiti-non-deterministico-con-e-transizioni-enfa) $S \subseteq Q$, la loro **$\varepsilon$-chiusura** $\text{ECLOSE}(S)$ è definita come l'unione%% link %% delle [$\varepsilon$-chiusure](Teoria%20degli%20automi.md#^definizione-e-chiusura-di-uno-stato) di ogni [stato](Teoria%20degli%20automi.md#^definizione-automa-a-stati-finiti-non-deterministico-con-e-transizioni-enfa) $q \in S$:
> 
> $$
> \text{ECLOSE}(S) = \bigcup_{q \in S} \text{ECLOSE}(q)
> $$
^definizione-e-chiusura-di-un-insieme-di-stati

Usiamo il concetto di [$\varepsilon$-chiusura](Teoria%20degli%20automi.md#^definizione-e-chiusura-di-uno-stato) per adattare le definizioni di [_funzione di transizione estesa_](Teoria%20degli%20automi.md#^definizione-funzione-di-transizione-estesa-di-un-nfa) e di [_linguaggio riconosciuto_](Teoria%20degli%20automi.md#^definizione-linguaggio-riconosciuto-da-un-nfa) agli [$\varepsilon$-NFA](Teoria%20degli%20automi.md#^definizione-automa-a-stati-finiti-non-deterministico-con-e-transizioni-enfa).

> [!definizione]+ Definizione: funzione di transizione estesa di un $\color{#FF7FFF} \varepsilon$-NFA
> 
> In un [$\varepsilon$-NFA](Teoria%20degli%20automi.md#^definizione-automa-a-stati-finiti-non-deterministico-con-e-transizioni-enfa) $\mathcal{A} = \langle \Sigma, Q, \delta, q_0, F \rangle$, la **funzione di transizione estesa** $\hat\delta \colon Q \times \Sigma^* \to \mathcal{P}(Q)$ è una [funzione](Funzioni.md#^definizione-funzione) definita induttivamente%% link %% sul suo secondo argomento così come segue:
> 
> $$
> \begin{align*}
> \hat\delta(q, \varepsilon) &= \text{ECLOSE}(q) \\
> \hat\delta(q, wa) &= \bigcup_{p \in \hat\delta(q,w)} \text{ECLOSE}\big( \delta(p,a) \big) 
> \end{align*}
> $$
^definizione-funzione-di-transizione-estesa-di-un-enfa

> [!definizione]+ Definizione: linguaggio riconosciuto da un $\color{#FF7FFF} \varepsilon$-NFA
> 
> Dato un [$\varepsilon$-NFA](Teoria%20degli%20automi.md#^definizione-automa-a-stati-finiti-non-deterministico-con-e-transizioni-enfa) $\mathcal{A} = \langle \Sigma, Q, \delta, q_0, F \rangle$, il **linguaggio riconosciuto** (o **accettato**) $L(A)$ da $\cal A$ è il [linguaggio formale](Teoria%20dei%20linguaggi%20formali.md#^definizione-linguaggio-formale) dato dalla [chiusura di Kleene](Teoria%20dei%20linguaggi%20formali.md#^definizione-chiusura-di-kleene-su-un-alfabeto) $\Sigma^*$ in cui, per ogni [stringa](Teoria%20dei%20linguaggi%20formali.md#^definizione-stringa) $w \in \Sigma^*$, la [funzione di transizione estesa](Teoria%20degli%20automi.md#^definizione-funzione-di-transizione-estesa-di-un-enfa) restituisce almeno uno [stato finale](Teoria%20degli%20automi.md#^definizione-automa-a-stati-finiti-non-deterministico-con-e-transizioni-enfa):
> 
> $$
> L(\mathcal{A}) = \{ w \in \Sigma^* \mid \hat\delta(q_0, w) \cap F \ne \emptyset \}
> $$
^definizione-linguaggio-riconosciuto-da-un-enfa

## 3.1 - Equivalenza tra DFA e $\varepsilon$-NFA

[Esattamente come già abbiamo fatto tra DFA e NFA](Teoria%20degli%20automi.md#^corollario-equivalenza-tra-dfa-e-nfa), possiamo dimostrare che anche [NFA](Teoria%20degli%20automi.md#^definizione-automa-a-stati-finiti-non-deterministico-nfa) e [$\varepsilon$-NFA](Teoria%20degli%20automi.md#^definizione-automa-a-stati-finiti-non-deterministico-con-e-transizioni-enfa) sono equivalenti dal punto di vista espressivo, cioè riconoscono esattamente gli stessi [linguaggi formali](Teoria%20dei%20linguaggi%20formali.md#^definizione-linguaggio-formale).

In particolare, nella conversione da [DFA](Teoria%20degli%20automi.md#^definizione-automa-a-stati-finiti-deterministico-dfa) a [$\varepsilon$-NFA](Teoria%20degli%20automi.md#^definizione-automa-a-stati-finiti-non-deterministico-con-e-transizioni-enfa), [sappiamo già che si può passare dai DFA agli NFA](Teoria%20degli%20automi.md#^teorema-da-dfa-a-nfa), quindi ora ci basta vedere come passare dagli [NFA](Teoria%20degli%20automi.md#^definizione-automa-a-stati-finiti-non-deterministico-nfa) agli [$\varepsilon$-NFA](Teoria%20degli%20automi.md#^definizione-automa-a-stati-finiti-non-deterministico-con-e-transizioni-enfa).

> [!teorema]+ Teorema: da NFA a $\color{#FF3F3F} \varepsilon$-NFA
> 
> Dato un [NFA](Teoria%20degli%20automi.md#^definizione-automa-a-stati-finiti-non-deterministico-nfa) $\cal N$, esiste un [$\varepsilon$-NFA](Teoria%20degli%20automi.md#^definizione-automa-a-stati-finiti-non-deterministico-con-e-transizioni-enfa) $\cal E$ tale che il [linguaggio riconosciuto](Teoria%20degli%20automi.md#^definizione-linguaggio-riconosciuto-da-un-dfa) $L(\mathcal{N})$ da $\mathcal{N}$ è uguale al [linguaggio riconosciuto](Teoria%20degli%20automi.md#^definizione-linguaggio-riconosciuto-da-un-nfa) $L(\mathcal{E})$ da $\cal E$:
> 
> $$
> \forall \mathcal{N}, \exists \mathcal{E} . \big( 
> L(\mathcal{N}) = L(\mathcal{E}) \big) 
> $$
^teorema-da-nfa-a-enfa

> [!dimostrazione]- Dimostrazione: da NFA a $\color{#7FFF7F} \varepsilon$-NFA
> 
> Per dimostrare che [per ogni NFA si trova un $\varepsilon$-NFA](Teoria%20degli%20automi.md#^teorema-da-nfa-a-enfa) equivalente, basta osservare che un [NFA](Teoria%20degli%20automi.md#^definizione-automa-a-stati-finiti-non-deterministico-nfa) è un caso particolare di [$\varepsilon$-NFA](Teoria%20degli%20automi.md#^definizione-automa-a-stati-finiti-non-deterministico-con-e-transizioni-enfa) in cui non ci sono [$\varepsilon$-transizioni](Teoria%20degli%20automi.md#^definizione-automa-a-stati-finiti-non-deterministico-con-e-transizioni-enfa).
> 
> $\blacksquare$

Ora invece vediamo come da un [$\varepsilon$-NFA](Teoria%20degli%20automi.md#^definizione-automa-a-stati-finiti-non-deterministico-con-e-transizioni-enfa) possiamo ottenere un [DFA](Teoria%20degli%20automi.md#^definizione-automa-a-stati-finiti-deterministico-dfa) equivalente.

> [!teorema]+ Teorema: da $\color{#FF3F3F} \varepsilon$-NFA a DFA
> 
> Dato un [$\varepsilon$-NFA](Teoria%20degli%20automi.md#^definizione-automa-a-stati-finiti-non-deterministico-con-e-transizioni-enfa) $\cal E$, esiste un [DFA](Teoria%20degli%20automi.md#^definizione-automa-a-stati-finiti-deterministico-dfa) $\cal D$ tale che il [linguaggio riconosciuto](Teoria%20degli%20automi.md#^definizione-linguaggio-riconosciuto-da-un-dfa) $L(\mathcal{E})$ da $\mathcal{E}$ è uguale al [linguaggio riconosciuto](Teoria%20degli%20automi.md#^definizione-linguaggio-riconosciuto-da-un-nfa) $L(\mathcal{D})$ da $\cal D$:
> 
> $$
> \forall \mathcal{E}, \exists \mathcal{D} . \big( 
> L(\mathcal{E}) = L(\mathcal{D}) \big) 
> $$
^teorema-da-enfa-a-dfa

> [!dimostrazione]- Dimostrazione (parziale): da $\color{#7FFF7F} \varepsilon$-NFA a DFA
> 
> Questa dimostrazione segue la stessa logica della [dimostrazione parziale del caso da NFA a DFA](Teoria%20degli%20automi.md#^dimostrazione-parziale-da-nfa-a-dfa).
> 
> La differenza fondamentale tra [$\varepsilon$-NFA](Teoria%20degli%20automi.md#^definizione-automa-a-stati-finiti-non-deterministico-con-e-transizioni-enfa) e [DFA](Teoria%20degli%20automi.md#^definizione-automa-a-stati-finiti-deterministico-dfa) è che il primo può trovarsi in più [stati](Teoria%20degli%20automi.md#^definizione-automa-a-stati-finiti-non-deterministico-nfa) contemporaneamente, mentre quest'ultimo in un solo [stato](Teoria%20degli%20automi.md#^definizione-automa-a-stati-finiti-deterministico-dfa) alla volta. Per ottenere una corrispondenza tra i due, costruiamo il [DFA](Teoria%20degli%20automi.md#^definizione-automa-a-stati-finiti-deterministico-dfa) facendo corrispondere a ogni suo stato un [insieme](Teoria%20degli%20insiemi.md#^definizione-insieme) di [stati](Teoria%20degli%20automi.md#^definizione-automa-a-stati-finiti-non-deterministico-nfa) dell'[$\varepsilon$-NFA](Teoria%20degli%20automi.md#^definizione-automa-a-stati-finiti-non-deterministico-con-e-transizioni-enfa).
> 
> Per esempio, se dopo aver letto una certa parola l'[$\varepsilon$-NFA](Teoria%20degli%20automi.md#^definizione-automa-a-stati-finiti-non-deterministico-con-e-transizioni-enfa). potrebbe trovarsi negli [stati](Teoria%20degli%20automi.md#^definizione-automa-a-stati-finiti-non-deterministico-nfa) $q_1$​, $q_2$​ e $q_3$​, il [DFA](Teoria%20degli%20automi.md#^definizione-automa-a-stati-finiti-deterministico-dfa) si troverà nello [stato](Teoria%20degli%20automi.md#^definizione-automa-a-stati-finiti-deterministico-dfa) che rappresenta l'[insieme](Teoria%20degli%20insiemi.md#^definizione-insieme)
> 
> $$
> \{ q_1,q_2,q_3 \}
> $$
> 
> La [funzione di transizione del DFA](Teoria%20degli%20automi.md#^definizione-automa-a-stati-finiti-deterministico-dfa) seguirà quindi una regola molto semplice: prendi tutti gli [stati](Teoria%20degli%20automi.md#^definizione-automa-a-stati-finiti-non-deterministico-nfa) che l'[$\varepsilon$-NFA](Teoria%20degli%20automi.md#^definizione-automa-a-stati-finiti-non-deterministico-con-e-transizioni-enfa) potrebbe assumere (**considerando anche quelli raggiungibili tramite [$\boldsymbol{\varepsilon}$-transizioni](Teoria%20degli%20automi.md#^definizione-automa-a-stati-finiti-non-deterministico-con-e-transizioni-enfa)**), verifica per ciascuno dove si può andare leggendo il [simbolo](Teoria%20dei%20linguaggi%20formali.md#^definizione-simbolo) successivo e raggruppali in un unico [insieme](Teoria%20degli%20insiemi.md#^definizione-insieme).
> 
> Ora esprimiamo questi concetti formalmente.
> 
> Dato un [DFA](Teoria%20degli%20automi.md#^definizione-automa-a-stati-finiti-deterministico-dfa) $\mathcal{D} = \langle \Sigma, Q_\mathcal{D}, \delta_\mathcal{D}, q_0, F_\mathcal{D} \rangle$ definiamo un [$\varepsilon$-NFA](Teoria%20degli%20automi.md#^definizione-automa-a-stati-finiti-non-deterministico-con-e-transizioni-enfa) $\mathcal{E} = \langle \Sigma, Q_\mathcal{E}, \delta_\mathcal{E}, q_0, F_\mathcal{E} \rangle$ in cui:
> - $Q_\mathcal{D}$ è l'[insieme delle parti](Teoria%20degli%20insiemi.md#^definizione-insieme-delle-parti) di $Q_\mathcal{E}$:
> 	$$
> 	Q_\mathcal{D} = \mathcal{P}(Q_\mathcal{E})
> 	$$
> - Per ogni [stato](Teoria%20degli%20automi.md#^definizione-automa-a-stati-finiti-deterministico-dfa) $Q \in Q_\mathcal{D}$ (ossia ogni possibile [sottoinsieme](Teoria%20degli%20insiemi.md#^definizione-sottoinsieme) di $Q_\mathcal{E}$) e ogni [simbolo](Teoria%20dei%20linguaggi%20formali.md#^definizione-simbolo) $a \in \Sigma$ la [funzione di transizione](Teoria%20degli%20automi.md#^definizione-automa-a-stati-finiti-deterministico-dfa) $\delta_\mathcal{D}(Q, a)$ darà l'unione%% link a ^definizione-unione-di-n-insiemi %% di tutte le [chiusure](Teoria%20degli%20automi.md#^definizione-e-chiusura-di-un-insieme-di-stati) su ogni $\delta_\mathcal{E}(q,a)$:
> 	$$
> 	\forall Q \in Q_\mathcal{D}, \forall a \in \Sigma . \left( \delta_\mathcal{D}(Q,a) = \bigcup_{q \in Q} \text{ECLOSE}\big( \delta_\mathcal{E}(q,a) \big)  \right)
> 	$$
> - Gli [stati finali del DFA](Teoria%20degli%20automi.md#^definizione-automa-a-stati-finiti-deterministico-dfa) $F_\mathcal{D}$ sono tali se contengono almeno uno degli [stati finali dell'$\varepsilon$-NFA](Teoria%20degli%20automi.md#^definizione-automa-a-stati-finiti-non-deterministico-con-e-transizioni-enfa) $F_\mathcal{E}$:
> 	$$
> 	F_\mathcal{D} = \{ q_F \in Q_\mathcal{D} \mid q_F \cap F_\mathcal{E} \ne \emptyset \}
> 	$$
> 
> A questo punto, per dimostrare che $L(\mathcal{E}) = L(\mathcal{D})$, ci basta dimostrare che, presa una qualsiasi [stringa](Teoria%20dei%20linguaggi%20formali.md#^definizione-stringa) $w \in \Sigma^*$, valga
> 
> $$
> w \in L(\mathcal{E}) \iff w \in L(\mathcal{D})
> $$
> 
> Partendo da $w \in L(\mathcal{E})$, abbiamo che, per [definizione di _linguaggio riconosciuto da un $\varepsilon$-NFA_](Teoria%20degli%20automi.md#^definizione-linguaggio-riconosciuto-da-un-enfa),
> 
> $$
> w \in L(\mathcal{E}) \iff \hat\delta_{\mathcal{E}}(q_0, w) \cap F_\mathcal{E} \ne \emptyset
> $$
> 
> Si può dimostrare induttivamente%% Link %% sulla [lunghezza](Teoria%20dei%20linguaggi%20formali.md#^definizione-lunghezza-di-una-stringa) $|w|$ di $w$ (approfondire dal libro di testo [_Compilers - Principles, Techniques, and Tools_](https://openlibrary.org/books/OL59750369M/Compilers) citato nelle fonti in fondo a questa pagina) che vale
> 
> $$
> \hat\delta_\mathcal{E}(q_0,w) = \hat\delta_\mathcal{D}(\text{ECLOSE}(q_0),w)
> $$
> 
> e, quindi,
> 
> $$
> \hat\delta_{\mathcal{E}}(q_0, w) \cap F_\mathcal{E} \ne \emptyset \iff \hat\delta_\mathcal{D}(\text{ECLOSE}(q_0),w) \cap F_\mathcal{E} \ne \emptyset
> $$
> 
> ma, per la definizione di $F_\mathcal{D}$ che ci siamo dati prima, ossia $F_\mathcal{D} = \{ Q \in Q_\mathcal{D} \mid Q \cap F_\mathcal{E} \ne \emptyset \}$, allora
> 
> $$
> \hat\delta_\mathcal{D}(\{ q_0 \},w) \cap F_\mathcal{D} \ne \emptyset \iff \hat\delta_\mathcal{D}(\text{ECLOSE}(q_0),w) \in F_\mathcal{D}
> $$
> 
> e, finalmente,
> 
> $$
> \hat\delta_\mathcal{D}(\text{ECLOSE}(q_0),w) \in F_\mathcal{D} \iff w \in L(\mathcal{D})
> $$
> 
> per [definizione di _linguaggio riconosciuto da un DFA_](Teoria%20degli%20automi.md#^definizione-linguaggio-riconosciuto-da-un-dfa).
> 
> Con una serie di bi-implicazioni%% link %% abbiamo dimostrato che
> 
> $$
> w \in L(\mathcal{E}) \iff w \in L(\mathcal{D})
> $$
> 
> $\blacksquare$

> [!algoritmo]+ Algoritmo di conversione di un $\color{#FF3F3F} \varepsilon$-NFA in un DFA tramite costruzione per sottoinsiemi
> 
> Dato un [$\varepsilon$-NFA](Teoria%20degli%20automi.md#^2a02ff) $\mathcal E = \langle \Sigma, Q_{\mathcal E}, \delta_{\mathcal E}, q_0, F_{\mathcal E} \rangle$, costruiamo un [DFA](Teoria%20degli%20automi.md#^definizione-automa-a-stati-finiti-deterministico-dfa) $\mathcal D = \langle \Sigma, Q_{\mathcal D}, \delta_{\mathcal D}, \text{ECLOSE}(q_0), F_{\mathcal D} \rangle$ equivalente attraverso i seguenti passaggi:
> 1. **Stato iniziale**: inizializziamo $Q_{\mathcal D}$ con la [chiusura](Teoria%20degli%20automi.md#^definizione-e-chiusura-di-uno-stato) $\text{ECLOSE}(q_0)$ dello [stato iniziale](Teoria%20degli%20automi.md#^definizione-automa-a-stati-finiti-non-deterministico-con-e-transizioni-enfa) $q_0$ dell'[$\varepsilon$-NFA](Teoria%20degli%20automi.md#^definizione-automa-a-stati-finiti-non-deterministico-con-e-transizioni-enfa).
> 2. **Calcolo delle transizioni**: per ogni [stato](Teoria%20degli%20automi.md#^definizione-automa-a-stati-finiti-deterministico-dfa) $Q \in Q_{\mathcal D}$ e ogni [simbolo](Teoria%20dei%20linguaggi%20formali.md#^definizione-simbolo) $a \in \Sigma$, calcoliamo l'[insieme](Teoria%20degli%20insiemi.md#^definizione-insieme) degli [stati](Teoria%20degli%20automi.md#^definizione-automa-a-stati-finiti-non-deterministico-con-e-transizioni-enfa) raggiungibili:
> 	$$
> 	\forall Q \in Q_\mathcal{D}, \forall a \in \Sigma . \left( \delta_\mathcal{D}(Q,a) = \bigcup_{q \in Q} \text{ECLOSE}\big( \delta_\mathcal{E}(q,a) \big)  \right)
> 	$$
>    Se l'[insieme](Teoria%20degli%20insiemi.md#^definizione-insieme) ottenuto non è ancora presente in $Q_{\mathcal D}$, lo aggiungiamo agli [stati](Teoria%20degli%20automi.md#^definizione-automa-a-stati-finiti-deterministico-dfa) del [DFA](Teoria%20degli%20automi.md#^definizione-automa-a-stati-finiti-deterministico-dfa) $Q_\mathcal{D}$. In particolare, se l'[insieme](Teoria%20degli%20insiemi.md#^definizione-insieme) ottenuto è l'[insieme vuoto](Teoria%20degli%20insiemi.md#^definizione-insieme-vuoto) $\emptyset$, lo aggiungiamo come [stato pozzo](Teoria%20degli%20automi.md#^definizione-stato-pozzo), dal quale tutte le [transizioni](Teoria%20degli%20automi.md#^definizione-automa-a-stati-finiti-deterministico-dfa) riportano a sé stesso:
> 	$$
> 	\forall a \in \Sigma.\big( \delta_{\mathcal D}(\emptyset,a)=\emptyset \big) 
> 	$$
>    Ripetiamo questo passaggio per tutti i nuovi [stati](Teoria%20degli%20automi.md#^definizione-automa-a-stati-finiti-deterministico-dfa) individuati, finché non rimangono stati da esaminare.
> 3. **Individuazione degli stati finali**: consideriamo [finali](Teoria%20degli%20automi.md#^definizione-automa-a-stati-finiti-deterministico-dfa) tutti gli [stati](Teoria%20degli%20automi.md#^definizione-automa-a-stati-finiti-deterministico-dfa) $q_F \in Q_{\mathcal D}$ che contengono almeno uno [stato finale](Teoria%20degli%20automi.md#^definizione-automa-a-stati-finiti-non-deterministico-con-e-transizioni-enfa) dell'[$\varepsilon$-NFA](Teoria%20degli%20automi.md#^definizione-automa-a-stati-finiti-non-deterministico-con-e-transizioni-enfa):
> 	$$
> 	F_\mathcal{D} = \{ q_F \in Q_\mathcal{D} \mid q_F \cap F_\mathcal{E} \ne \emptyset \}
> 	$$
^algoritmo-di-conversione-di-un-enfa-in-un-dfa-tramite-costruzione-per-sottoinsiemi

> [!esempio]- Esempio dell'algoritmo di conversione di un $\color{#7F7FFF} \varepsilon$-NFA in un DFA tramite costruzione per sottoinsiemi
> 
> Riprendiamo l'[esempio dell'$\varepsilon$-NFA che riconosce numeri interi](Teoria%20degli%20automi.md#^esempio-enfa-che-riconosce-numeri-interi):
> 
> ![esempio-enfa-che-riconosce-numeri-interi-enfa-2](esempio-enfa-che-riconosce-numeri-interi-enfa-2.svg)
> 
> Questo [$\varepsilon$-NFA](Teoria%20degli%20automi.md#^2a02ff) $\mathcal E = \langle \Sigma, Q_{\mathcal E}, \delta_{\mathcal E}, q_0, F_{\mathcal E} \rangle$ ha [alfabeto](Teoria%20dei%20linguaggi%20formali.md#^definizione-alfabeto) $\Sigma = \{ +,-,0,1,2,\ldots,9 \}$, [stati](Teoria%20degli%20automi.md#^definizione-automa-a-stati-finiti-non-deterministico-nfa) $Q_{\mathcal E} = \{q_0,q_1,q_2,q_3\}$, [stato iniziale](Teoria%20degli%20automi.md#^definizione-automa-a-stati-finiti-non-deterministico-nfa) $q_0$ e [stati finali](Teoria%20degli%20automi.md#^definizione-automa-a-stati-finiti-non-deterministico-nfa) $F_{\mathcal E} = \{q_2,q_3\}$. Applichiamo l'[algoritmo di conversione di un $\varepsilon$-NFA in un DFA tramite costruzione per sottoinsiemi](Teoria%20degli%20automi.md#^algoritmo-di-conversione-di-un-enfa-in-un-dfa-tramite-costruzione-per-sottoinsiemi) per ottenere il [DFA](Teoria%20degli%20automi.md#^definizione-automa-a-stati-finiti-deterministico-dfa) $\mathcal D = \langle \Sigma, Q_{\mathcal D}, \delta_{\mathcal D}, \text{ECLOSE}(q_0), F_{\mathcal D} \rangle$ equivalente.
> 
> **Passo 1**: calcoliamo lo [stato iniziale del DFA](Teoria%20degli%20automi.md#^definizione-automa-a-stati-finiti-deterministico-dfa) che è dato dalla [chiusura](Teoria%20degli%20automi.md#^definizione-e-chiusura-di-uno-stato) $\text{ECLOSE}(q_0)$ sullo [stato iniziale](Teoria%20degli%20automi.md#^definizione-automa-a-stati-finiti-non-deterministico-con-e-transizioni-enfa) $q_0$ dell'[$\varepsilon$-NFA](Teoria%20degli%20automi.md#^definizione-automa-a-stati-finiti-non-deterministico-con-e-transizioni-enfa):
> 
> $$
> \text{ECLOSE}(q_0) = \{ q_0, q_1 \}
> $$
> 
> **Passo 2**: calcoliamo le [transizioni](Teoria%20degli%20automi.md#^definizione-automa-a-stati-finiti-deterministico-dfa). Abbiamo
> 
> $$
> Q_\mathcal{D} = \{ \{ q_0, q_1 \} \}
> $$
> 
> con $\{ q_0, q_1 \}$ da esplorare, quindi vediamo quali [stati](Teoria%20degli%20automi.md#^definizione-automa-a-stati-finiti-deterministico-dfa) otteniamo per ogni $Q \in Q_\mathcal{D} = \{ \{ q_0, q_1 \} \}$ e per ogni $a \in \Sigma = \{ +,-,0,1,2,\ldots,9 \}$:
> 
> |                                   | $\boldsymbol{+,-}$ | $\boldsymbol{0}$ | $\boldsymbol{1,2,\ldots,9}$ |
> | --------------------------------- | ------------------ | ---------------- | --------------------------- |
> | $\boldsymbol{\to \{ q_0, q_1 \}}$ | $\{q_1\}$          | $\{q_3\}$        | $\{q_2\}$                   |
> 
> dove, per esempio, scelti $Q = \{ q_0 \}$ e $a = 0$:
> 
> $$
> \begin{align*}
> \delta_\mathcal{D}(\{ q_0, q_1 \},0) &= \bigcup_{q \in \{ q_0, q_1 \}} \text{ECLOSE}\big( \delta_\mathcal{E}(q,0) \big) \\
> &= \text{ECLOSE}\big( \delta_\mathcal{E}(q_0,0) \big) \cup \text{ECLOSE}\big( \delta_\mathcal{E}(q_1,0) \big) \\
> &= \text{ECLOSE}(q_3) \cup \text{ECLOSE}(\emptyset) \\
> &= \{ q_3 \} \cup \emptyset \\
> &= \{ q_3 \}
> \end{align*}
> $$
> 
> Ora abbiamo
> 
> $$
> Q_\mathcal{D} = \{ \{ q_0,q_1 \}, \{ q_1 \}, \{ q_2 \}, \{ q_3 \} \}
> $$
> 
> con $\{ q_1 \}$, $\{ q_2 \}$ e $\{ q_3 \}$ da esplorare, quindi vediamo quali [stati](Teoria%20degli%20automi.md#^definizione-automa-a-stati-finiti-deterministico-dfa) otteniamo per ogni $Q \in Q_\mathcal{D} = \{ \{ q_0,q_1 \}, \{ q_1 \}, \{ q_2 \}, \{ q_3 \} \}$ e per ogni $a \in \Sigma = \{ +,-,0,1,2,\ldots,9 \}$:
> 
> |                                   | $\boldsymbol{+,-}$ | $\boldsymbol{0}$ | $\boldsymbol{1,2,\ldots,9}$ |
> | --------------------------------- | ------------------ | ---------------- | --------------------------- |
> | $\boldsymbol{\to \{ q_0, q_1 \}}$ | $\{q_1\}$          | $\{q_3\}$        | $\{ q_2 \}$                 |
> | $\boldsymbol{\{ q_1 \}}$          | $\emptyset$        | $\emptyset$      | $\{ q_2 \}$                 |
> | $\boldsymbol{\{ q_2 \}}$          | $\emptyset$        | $\{ q_2 \}$      | $\{ q_2 \}$                 |
> | $\boldsymbol{\{ q_3 \}}$          | $\emptyset$        | $\emptyset$      | $\emptyset$                 |
> 
> Ora abbiamo
> 
> $$
> Q_\mathcal{D} = \{ \{ q_0,q_1 \}, \{ q_1 \}, \{ q_2 \}, \{ q_3 \}, \emptyset \}
> $$
> 
> con $\emptyset$ ancora da esplorare, ma questo secondo l'[algoritmo](Teoria%20degli%20automi.md#^algoritmo-di-conversione-di-un-enfa-in-un-dfa-tramite-costruzione-per-sottoinsiemi) è uno [stato pozzo](Teoria%20degli%20automi.md#^definizione-stato-pozzo) e quindi ogni [transizione](Teoria%20degli%20automi.md#^definizione-automa-a-stati-finiti-deterministico-dfa) porta sempre a $\emptyset$:
> 
> |                                   | $\boldsymbol{+,-}$ | $\boldsymbol{0}$ | $\boldsymbol{1,2,\ldots,9}$ |
> | --------------------------------- | ------------------ | ---------------- | --------------------------- |
> | $\boldsymbol{\to \{ q_0, q_1 \}}$ | $\{q_1\}$          | $\{q_3\}$        | $\{ q_2 \}$                 |
> | $\boldsymbol{\{ q_1 \}}$          | $\emptyset$        | $\emptyset$      | $\{ q_2 \}$                 |
> | $\boldsymbol{\{ q_2 \}}$          | $\emptyset$        | $\{ q_2 \}$      | $\{ q_2 \}$                 |
> | $\boldsymbol{\{ q_3 \}}$          | $\emptyset$        | $\emptyset$      | $\emptyset$                 |
> | $\boldsymbol{\emptyset}$          | $\emptyset$        | $\emptyset$      | $\emptyset$                 |
> 
> Questa è la [tabella di transizione](Teoria%20degli%20automi.md#^notazione-tabella-di-transizione) del nostro nuovo [DFA](Teoria%20degli%20automi.md#^definizione-automa-a-stati-finiti-deterministico-dfa).
> 
> **Passo 3**: individuazione degli [stati finali](Teoria%20degli%20automi.md#^definizione-automa-a-stati-finiti-deterministico-dfa). Uno [stato](Teoria%20degli%20automi.md#^definizione-automa-a-stati-finiti-deterministico-dfa) del [DFA](Teoria%20degli%20automi.md#^definizione-automa-a-stati-finiti-deterministico-dfa) è [finale](Teoria%20degli%20automi.md#^definizione-automa-a-stati-finiti-deterministico-dfa) se contiene almeno uno [stato finale](Teoria%20degli%20automi.md#^definizione-automa-a-stati-finiti-non-deterministico-con-e-transizioni-enfa) dell'[$\varepsilon$-NFA](Teoria%20degli%20automi.md#^definizione-automa-a-stati-finiti-non-deterministico-con-e-transizioni-enfa). Poiché $F_{\mathcal E}=\{q_2,q_3\}$, abbiamo che
> 
> $$
> F_{\mathcal D} = \{\{q_2\},\{ q_3 \}\}
> $$
> 
> Questa è la [tabella di transizione](Teoria%20degli%20automi.md#^notazione-tabella-di-transizione) finale del nostro nuovo [DFA](Teoria%20degli%20automi.md#^definizione-automa-a-stati-finiti-deterministico-dfa) $\mathcal D = \langle \Sigma,Q_{\mathcal D},\delta_{\mathcal D},\{q_0,q_1\},F_{\mathcal D} \rangle$ è la seguente:
> 
> |                                   | $\boldsymbol{+,-}$ | $\boldsymbol{0}$ | $\boldsymbol{1,2,\ldots,9}$ |
> | --------------------------------- | ------------------ | ---------------- | --------------------------- |
> | $\boldsymbol{\to \{ q_0, q_1 \}}$ | $\{q_1\}$          | $\{q_3\}$        | $\{ q_2 \}$                 |
> | $\boldsymbol{\{ q_1 \}}$          | $\emptyset$        | $\emptyset$      | $\{ q_2 \}$                 |
> | $*\boldsymbol{\{ q_2 \}}$         | $\emptyset$        | $\{ q_2 \}$      | $\{ q_2 \}$                 |
> | $*\boldsymbol{\{ q_3 \}}$         | $\emptyset$        | $\emptyset$      | $\emptyset$                 |
> | $\boldsymbol{\emptyset}$          | $\emptyset$        | $\emptyset$      | $\emptyset$                 |
> 
> La sua [rappresentazione grafica](Teoria%20degli%20automi.md#^rappresentazione-grafica-di-un-automa) è la seguente:
> 
> ![esempio-dell-algoritmo-di-conversione-di-un-enfa-in-un-dfa](esempio-dell-algoritmo-di-conversione-di-un-enfa-in-un-dfa.svg)

> [!corollario]+ Corollario: equivalenza tra DFA ed $\color{#FFCF7F} \varepsilon$-NFA
>
> I [DFA](Teoria%20degli%20automi.md#^definizione-automa-a-stati-finiti-deterministico-dfa) e gli [$\varepsilon$-NFA](Teoria%20degli%20automi.md#^definizione-automa-a-stati-finiti-non-deterministico-con-e-transizioni-enfa) hanno la stessa potenza espressiva, ossia riconoscono esattamente gli stessi [linguaggi formali](Teoria%20dei%20linguaggi%20formali.md#^definizione-linguaggio-formale) e sono quindi equivalenti da questo punto di vista:
>
> $$
> \begin{array}{}
> \forall \mathcal{D}, \exists \mathcal{E} . \big( L(\mathcal{D}) = L(\mathcal{E}) \big) \\
> \land \\
> \forall \mathcal{E}, \exists \mathcal{D} . \big( L(\mathcal{E}) = L(\mathcal{D}) \big) 
> \end{array}
> $$
^corollario-equivalenza-tra-dfa-ed-enfa

> [!dimostrazione]- Dimostrazione: equivalenza tra DFA ed $\color{#7FFF7F} \varepsilon$-NFA
>
> Per il [primo teorema](Teoria%20degli%20automi.md#^teorema-da-nfa-a-enfa), per ogni [NFA](Teoria%20degli%20automi.md#^definizione-automa-a-stati-finiti-non-deterministico-nfa) esiste un [$\varepsilon$-NFA](Teoria%20degli%20automi.md#^definizione-automa-a-stati-finiti-non-deterministico-con-e-transizioni-enfa) che [riconosce](Teoria%20degli%20automi.md#^definizione-linguaggio-riconosciuto-da-un-enfa) lo stesso [linguaggio](Teoria%20dei%20linguaggi%20formali.md#^definizione-linguaggio-formale) e, dato che [DFA ed NFA sono equivalenti](Teoria%20degli%20automi.md#^corollario-equivalenza-tra-dfa-ed-enfa), allora anche per ogni [DFA](Teoria%20degli%20automi.md#^definizione-automa-a-stati-finiti-deterministico-dfa) esiste un [$\varepsilon$-NFA](Teoria%20degli%20automi.md#^definizione-automa-a-stati-finiti-non-deterministico-con-e-transizioni-enfa) che [riconosce](Teoria%20degli%20automi.md#^definizione-linguaggio-riconosciuto-da-un-enfa) lo stesso [linguaggio](Teoria%20dei%20linguaggi%20formali.md#^definizione-linguaggio-formale).
> 
> Viceversa, per il [secondo teorema](Teoria%20degli%20automi.md#^teorema-da-enfa-a-dfa) è vero il contrario: abbiamo quindi che le due tipologie di automi riconoscono gli stessi [linguaggi formali](Teoria%20dei%20linguaggi%20formali.md#^definizione-linguaggio-formale).
> 
> $\blacksquare$

> [!osservazione]+ Osservazione: linguaggi regolari riconosciuti da un $\color{#7F7F7F} \varepsilon$-NFA
> 
> Dal momento che [DFA ed $\varepsilon$-NFA sono equivalenti](Teoria%20degli%20automi.md#^corollario-equivalenza-tra-dfa-ed-enfa), possiamo caratterizzare un [linguaggio regolare](Teoria%20degli%20automi.md#^definizione-linguaggio-regolare) $L$ anche attraverso un [$\varepsilon$-NFA](Teoria%20degli%20automi.md#^definizione-automa-a-stati-finiti-non-deterministico-con-e-transizioni-enfa) $\mathcal{E}$ che lo [riconosce](Teoria%20degli%20automi.md#^definizione-linguaggio-riconosciuto-da-un-enfa).
^osservazione-linguaggi-regolari-riconosciuti-da-un-enfa

# 4 - Teoremi e proprietà sugli automi

Specifichiamo che tutti i teoremi%% Link %% presentati da qui in avanti riguarderanno i [DFA](Teoria%20degli%20automi.md#^definizione-automa-a-stati-finiti-deterministico-dfa) ma, a meno che non sia esplicitamente scritto, grazie all'[equivalenza tra DFA ed NFA](Teoria%20degli%20automi.md#^corollario-equivalenza-tra-dfa-ed-nfa) e all'[equivalenza tra DFA ed $\varepsilon$-NFA](Teoria%20degli%20automi.md#^corollario-equivalenza-tra-dfa-ed-enfa) potranno rispettivamente essere applicati anche agli [NFA](Teoria%20degli%20automi.md#^definizione-automa-a-stati-finiti-non-deterministico-nfa) e [$\varepsilon$-NFA](Teoria%20degli%20automi.md#^definizione-automa-a-stati-finiti-non-deterministico-con-e-transizioni-enfa).

> [!proprieta]+ Proprietà: chiusura dei linguaggi regolari rispetto all'unione
> 
> I [linguaggi regolari](Teoria%20degli%20automi.md#^definizione-linguaggio-regolare) sono chiusi%% link %% rispetto all'operazione%% link %% di [unione](Teoria%20degli%20insiemi.md#^definizione-unione-di-due-insiemi), ovvero se due [linguaggi formali](Teoria%20dei%20linguaggi%20formali.md#^definizione-linguaggio-formale) $L_1$ ed $L_2$ sono [regolari](Teoria%20degli%20automi.md#^definizione-linguaggio-regolare), allora anche la loro [unione](Teoria%20degli%20insiemi.md#^definizione-unione-di-due-insiemi) $L_1 \cup L_2$ è [regolare](Teoria%20degli%20automi.md#^definizione-linguaggio-regolare).
^proprieta-chiusura-dei-linguaggi-regolari-rispetto-all-unione

[!dimostrazione]- Dimostrazione: chiusura dei linguaggi regolari rispetto all'unione

Se due [linguaggi formali](Teoria%20dei%20linguaggi%20formali.md#^definizione-linguaggio-formale) $L_1$ ed $L_2$ sono [regolari](Teoria%20degli%20automi.md#^definizione-linguaggio-regolare), allora per [definizione di _linguaggio regolare_](Teoria%20degli%20automi.md#^definizione-linguaggio-regolare) esistono due [DFA](Teoria%20degli%20automi.md#^definizione-automa-a-stati-finiti-deterministico-dfa) $\mathcal{D}_1 = \langle \Sigma, Q_1, \delta_1, q_1, F_1 \rangle$ e $\mathcal{D}_2 = \langle \Sigma, Q_2, \delta_2, q_2, F_2 \rangle$ tali che $L_1 = L(\mathcal{D}_1)$ e $L_2 = L(\mathcal{D}_2)$.

Proviamo a costruire il [DFA](Teoria%20degli%20automi.md#^definizione-automa-a-stati-finiti-deterministico-dfa) $\mathcal D$ come

$$
\mathcal D = \langle \Sigma, Q_1 \cup Q_2 \cup \{ q_0 \}, \delta, q_0, F_1 \cup F_2 \rangle 
$$

e, dati uno [stato](Teoria%20degli%20automi.md#^definizione-automa-a-stati-finiti-deterministico-dfa) $q \in Q$ e un [simbolo](Teoria%20dei%20linguaggi%20formali.md#^definizione-simbolo) $a \in \Sigma$, la [funzione di transizione](Teoria%20degli%20automi.md#^definizione-automa-a-stati-finiti-deterministico-dfa) $\delta$ è definita come

$$
\delta(q, a) = \begin{cases}
\{ q_1,q_2 \} & \text{se } q = q_0 \land a = \varepsilon \\
\delta_1(q,a) & \text{se } q \in Q_1 \\
\delta_2(q,a) & \text{se } q \in Q_2 \\
\emptyset & \text{altrimenti}
\end{cases}
$$

Ecco come si potrebbe [rappresentare graficamente](Teoria%20degli%20automi.md#^rappresentazione-grafica-di-un-automa) $\mathcal D$:

![dimostrazione-proprieta-chiusura-dei-linguaggi-regolari-rispetto-all-unione](dimostrazione-proprieta-chiusura-dei-linguaggi-regolari-rispetto-all-unione.svg)

---

> [!fonti]+ Fonti
> 
> - 🏫 Corso di Laurea in Informatica (`L-31 R`) presso l'Università di Torino:
>     - Corso di _Linguaggi Formali e Traduttori_ (`INF0344`), A.A. 2026-27 ([pagina Moodle](https://informatica.i-learn.unito.it/course/view.php?id=3735)):
> 		- Prof. Jeremy James Sproston, slide del corso:
> 			- [2.1 - _DFA_](https://informatica.i-learn.unito.it/pluginfile.php/514089/mod_folder/content/0/2-1_dfa.pdf).
> 			- [2.2 - _NFA_](https://informatica.i-learn.unito.it/pluginfile.php/514089/mod_folder/content/0/2-2_nfa.pdf).
> 			- [2.3 - $\varepsilon$-NFA](https://informatica.i-learn.unito.it/pluginfile.php/514089/mod_folder/content/0/2-3_enfa.pdf).
> - 📚 Alfred V. Aho, Monica S. Lam, Ravi Sethi, Jeffrey D. Ullman, [_Compilers - Principles, Techniques, and Tools_](https://openlibrary.org/books/OL59750369M/Compilers), Pearson India, 2023 (ISBN: `9789357054119`):
