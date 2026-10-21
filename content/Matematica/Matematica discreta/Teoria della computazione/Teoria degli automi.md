---
aliases:
  - Teoria degli automi
---

> [!premessa]+ Premessa
> 
> Ciao! Se è la prima volta che capiti su questo sito, ti consiglio di consultare la [pagina principale](index.md) di questo _Giardino Digitale_ per scoprire meglio cos'è e come navigarlo.
> 
> Lo stato di questa nota è al momento: 🔴 <font color="#FF7F7F">_Bozza_</font>.

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

> [!esempio]- Esempio di NFA
> 
> 
> Definiamo un [DFA](Teoria%20degli%20automi.md#^definizione-automa-a-stati-finiti-deterministico-dfa) che riconosce le [stringhe](Teoria%20dei%20linguaggi%20formali.md#^definizione-stringa) su $\Sigma = \{ \text{a},\text{b} \}$ che terminano in $\text{abb}$:
> 
> ![esempio-di-nfa-1](esempio-di-nfa-1.svg)
> 
> Definiamo ora un [NFA](Teoria%20degli%20automi.md#^definizione-automa-a-stati-finiti-non-deterministico-nfa) con lo stesso comportamento:
> 
> ![esempio-di-nfa-2](esempio-di-nfa-2.svg)
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
> Dato un [NFA](Teoria%20degli%20automi.md#^definizione-automa-a-stati-finiti-non-deterministico-nfa) $\mathcal{A} = \langle \Sigma, Q, \delta, q_0, F \rangle$, il **linguaggio riconosciuto** (o **accettato**) $L(A)$ da $\cal A$ è il [linguaggio formale](Teoria%20dei%20linguaggi%20formali.md#^definizione-linguaggio-formale) dato dalla [chiusura di Kleene](Teoria%20dei%20linguaggi%20formali.md#^definizione-chiusura-di-kleene-su-un-alfabeto) $\Sigma^*$ in cui, per ogni [stringa](Teoria%20dei%20linguaggi%20formali.md#^definizione-stringa) $w \in \Sigma^*$, la [funzione di transizione estesa](Teoria%20degli%20automi.md#^definizione-funzione-di-transizione-estesa-di-un-nfa) restituisce almeno uno [stato finale](Teoria%20degli%20automi.md#^definizione-automa-a-stati-finiti-deterministico-dfa):
> 
> $$
> L(\mathcal{A}) = \{ w \in \Sigma^* \mid \hat\delta(q_0, w) \cap F \ne \emptyset \}
> $$
^definizione-linguaggio-riconosciuto-da-un-nfa

## 2.1 - Equivalenza tra DFA e NFA

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

> [!teorema]+ Teorema: da NFA a DFA
> 
> Dato un [NFA](Teoria%20degli%20automi.md#^definizione-automa-a-stati-finiti-non-deterministico-nfa) $\cal N$, esiste un [DFA](Teoria%20degli%20automi.md#^definizione-automa-a-stati-finiti-deterministico-dfa) $\cal D$ tale che il [linguaggio riconosciuto](Teoria%20degli%20automi.md#^definizione-linguaggio-riconosciuto-da-un-dfa) $L(\mathcal{N})$ da $\mathcal{N}$ è uguale al [linguaggio riconosciuto](Teoria%20degli%20automi.md#^definizione-linguaggio-riconosciuto-da-un-nfa) $L(\mathcal{D})$ da $\cal D$:
> 
> $$
> \forall \mathcal{N}, \exists \mathcal{D} . \big( 
> L(\mathcal{N}) = L(\mathcal{D}) \big) 
> $$
^teorema-da-nfa-a-dfa

[!dimostrazione]- Dimostrazione: da NFA a DFA

La differenza fondamentale tra [NFA](Teoria%20degli%20automi.md#^definizione-automa-a-stati-finiti-non-deterministico-nfa) e [DFA](Teoria%20degli%20automi.md#^definizione-automa-a-stati-finiti-deterministico-dfa) è che il primo può trovarsi in più [stati](Teoria%20degli%20automi.md#^definizione-automa-a-stati-finiti-non-deterministico-nfa) contemporaneamente, mentre quest'ultimo in un solo [stato](Teoria%20degli%20automi.md#^definizione-automa-a-stati-finiti-deterministico-dfa) alla volta. Per ottenere una corrispondenza tra i due, costruiamo il [DFA](Teoria%20degli%20automi.md#^definizione-automa-a-stati-finiti-deterministico-dfa) facendo corrispondere a ogni suo stato un [insieme](Teoria%20degli%20insiemi.md#^definizione-insieme) di [stati](Teoria%20degli%20automi.md#^definizione-automa-a-stati-finiti-non-deterministico-nfa) dell'[NFA](Teoria%20degli%20automi.md#^definizione-automa-a-stati-finiti-non-deterministico-nfa).

Per esempio, se dopo aver letto una certa parola l'[NFA](Teoria%20degli%20automi.md#^definizione-automa-a-stati-finiti-non-deterministico-nfa) potrebbe trovarsi negli [stati](Teoria%20degli%20automi.md#^definizione-automa-a-stati-finiti-non-deterministico-nfa) $q_1$​, $q_2$​ e $q_3$​, il [DFA](Teoria%20degli%20automi.md#^definizione-automa-a-stati-finiti-deterministico-dfa) si troverà nello [stato](Teoria%20degli%20automi.md#^definizione-automa-a-stati-finiti-deterministico-dfa) che rappresenta l'[insieme](Teoria%20degli%20insiemi.md#^definizione-insieme):

$$
\{ q_1,q_2,q_3 \}
$$

La [funzione di transizione del DFA](Teoria%20degli%20automi.md#^definizione-automa-a-stati-finiti-deterministico-dfa) seguirà quindi una regola molto semplice: prendi tutti gli [stati](Teoria%20degli%20automi.md#^definizione-automa-a-stati-finiti-non-deterministico-nfa) che l'[NFA](Teoria%20degli%20automi.md#^definizione-automa-a-stati-finiti-non-deterministico-nfa) potrebbe assumere, verifica per ciascuno dove si può andare leggendo il [simbolo](Teoria%20dei%20linguaggi%20formali.md#^definizione-simbolo) successivo e raggruppali in un unico [insieme](Teoria%20degli%20insiemi.md#^definizione-insieme).

Ora esprimiamo questi concetti formalmente.

Dato un [DFA](Teoria%20degli%20automi.md#^definizione-automa-a-stati-finiti-deterministico-dfa) $\mathcal{D} = \langle \Sigma, Q_\mathcal{D}, \delta_\mathcal{D}, q_0, F \rangle$ definiamo un [NFA](Teoria%20degli%20automi.md#^definizione-automa-a-stati-finiti-non-deterministico-nfa) $\mathcal{N} = \langle \Sigma, Q_\mathcal{N}, \delta_\mathcal{N}, q_0, F \rangle$ (notare la differenza tra il $Q_\mathcal{D}$ e $\delta_\mathcal{D}$ di $\mathcal{D}$ e il $Q_\mathcal{N}$ e $\delta_\mathcal{N}$ di $\mathcal{N}$) in cui:
- $Q_\mathcal{D}$ è l'[insieme delle parti](Teoria%20degli%20insiemi.md#^definizione-insieme-delle-parti) di $Q_\mathcal{N}$:
	$$
	Q_\mathcal{D} = \mathcal{P}(Q_\mathcal{N})
	$$
- Per ogni [stato](Teoria%20degli%20automi.md#^definizione-automa-a-stati-finiti-deterministico-dfa) $q \in Q_\mathcal{D}$ (ossia ogni possibile [sottoinsieme](Teoria%20degli%20insiemi.md#^definizione-sottoinsieme) di $Q_\mathcal{N}$) e ogni [simbolo](Teoria%20dei%20linguaggi%20formali.md#^definizione-simbolo) $a \in \Sigma$ la [funzione di transizione](Teoria%20degli%20automi.md#^definizione-automa-a-stati-finiti-deterministico-dfa) $\delta_\mathcal{D}(q, a)$ darà tutti gli 

---

> [!fonti]+ Fonti
> 
> - 🏫 Corso di Laurea in Informatica (`L-31 R`) presso l'Università di Torino:
>     - Corso di _Linguaggi Formali e Traduttori_ (`INF0344`), A.A. 2026-27 ([pagina Moodle](https://informatica.i-learn.unito.it/course/view.php?id=3735)):
> 		- Prof. Jeremy James Sproston, slide del corso:
> 			- [2.1 - _DFA_](https://informatica.i-learn.unito.it/pluginfile.php/514089/mod_folder/content/0/2-1_dfa.pdf).
> 			- [2.2 - _NFA_](https://informatica.i-learn.unito.it/pluginfile.php/514089/mod_folder/content/0/2-2_nfa.pdf).
