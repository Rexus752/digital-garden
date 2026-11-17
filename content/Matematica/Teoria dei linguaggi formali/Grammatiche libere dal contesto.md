---
aliases:
  - Grammatiche libere dal contesto
---

> [!premessa]+ Premessa
> 
> Ciao! Se è la prima volta che capiti su questo sito, ti consiglio di consultare la [pagina principale](index.md) di questo _Giardino Digitale_ per scoprire meglio cos'è e come navigarlo.
> 
> Lo stato di questa nota è al momento: 🔴 <font color="#FF7F7F">_Bozza_</font>.

---

> [!definizione]+ Definizione: grammatica libera dal contesto
> 
> Una **grammatica libera dal contesto** (o semplicemente **grammatica libera**) è una [quadrupla](Teoria%20degli%20insiemi.md#^definizione-tupla)
> 
> $$
> \mathcal{G} = \langle V,T,P,V_0 \rangle
> $$
> 
> dove:
> - $V$ è un [insieme](Teoria%20degli%20insiemi.md#^definizione-insieme) finito%% Link %% di variabili (o simboli non terminali o categorie sintattiche),
> - $T$ è un [alfabeto](Teoria%20dei%20linguaggi%20formali.md#^definizione-alfabeto) di [simboli](Teoria%20dei%20linguaggi%20formali.md#^definizione-simbolo) terminali,
> - $P$ è un [insieme](Teoria%20degli%20insiemi.md#^definizione-insieme) finito%% Link %% di produzioni%% link %% della forma $A \to \alpha$ in cui
> 	- $A \in V$ è detta **testa della produzione** e
> 	- $\alpha \in (V \cup T)^*$ è detta **corpo della produzione**,
> - $V_0 \in V$ è il [simbolo](Teoria%20dei%20linguaggi%20formali.md#^definizione-simbolo) iniziale della grammatica.
^definizione-grammatica-libera-dal-contesto

> [!notazione]+ Notazioni delle grammatiche libere dal contesto
> 
> Le [grammatiche libere dal contesto](Grammatiche%20libere%20dal%20contesto.md#^definizione-grammatica-libera-dal-contesto) adottano le seguenti notazioni convenzionali:
> - Gli [elementi](Teoria%20degli%20insiemi.md#^definizione-insieme) dell'[insieme](Teoria%20degli%20insiemi.md#^definizione-insieme) delle [variabili](Grammatiche%20libere%20dal%20contesto.md#^definizione-grammatica-libera-dal-contesto) $V$ si indicano con le lettere maiuscole dell'alfabeto latino:
> 	$$
> 	V = \{ A,B,C,\ldots \}
> 	$$
> - Gli [elementi](Teoria%20degli%20insiemi.md#^definizione-insieme) dell'[insieme](Teoria%20degli%20insiemi.md#^definizione-insieme) dei [simboli terminali](Grammatiche%20libere%20dal%20contesto.md#^definizione-grammatica-libera-dal-contesto) $T$ si indicano con le lettere minuscole dell'alfabeto latino:
> 	$$
> 	T = \{ a,b,c,\ldots \}
> 	$$
> - Gli [elementi](Teoria%20degli%20insiemi.md#^definizione-insieme) dell'[insieme](Teoria%20degli%20insiemi.md#^definizione-insieme) dei [simboli](Teoria%20dei%20linguaggi%20formali.md#^definizione-simbolo) $V \cup T$ si indicano con le ultime lettere maiuscole dell'alfabeto latino:
> 	$$
> 	V \cup T = \{ X,Y,Z, \ldots \}
> 	$$
> 
> - Gli [elementi](Teoria%20degli%20insiemi.md#^definizione-insieme) dell'[insieme](Teoria%20degli%20insiemi.md#^definizione-insieme) delle [stringhe](Teoria%20dei%20linguaggi%20formali.md#^definizione-stringa) di [simboli terminali](Grammatiche%20libere%20dal%20contesto.md#^definizione-grammatica-libera-dal-contesto) $T^*$ si indicano con le ultime lettere minuscole dell'alfabeto latino:
> 	$$
> 	T^* = \{ u,v,w,\ldots \}
> 	$$
> - Gli [elementi](Teoria%20degli%20insiemi.md#^definizione-insieme) dell'[insieme](Teoria%20degli%20insiemi.md#^definizione-insieme) delle [stringhe](Teoria%20dei%20linguaggi%20formali.md#^definizione-stringa) di [simboli](Teoria%20dei%20linguaggi%20formali.md#^definizione-simbolo) $(V \cup T)^*$ si indicano cone le lettere dell'alfabeto greco:
> 	$$
> 	(V \cup T)^* = \{ \alpha, \beta, \gamma, \ldots \}
> 	$$
> - Abbreviamo multiple [produzioni](Grammatiche%20libere%20dal%20contesto.md#^definizione-grammatica-libera-dal-contesto) da una [variabile](Grammatiche%20libere%20dal%20contesto.md#^definizione-grammatica-libera-dal-contesto) $A$ a più [stringhe](Teoria%20dei%20linguaggi%20formali.md#^definizione-stringa) $\alpha_1, \alpha_2, \ldots, \alpha_n$, cioè
> 	$$
> 	A \to \alpha_1, A \to \alpha_2, \ldots, A \to \alpha_n
> 	$$
> 	come
> 	$$
> 	A \to \alpha_1 \mid \alpha_2 \mid \ldots \mid \alpha_n
> 	$$

> [!definizione]+ Definizione: derivazione in un passo
> 
> Data una [grammatica libera](Grammatiche%20libere%20dal%20contesto.md#^definizione-grammatica-libera-dal-contesto) $\mathcal{G} = \langle V,T,P,V_0 \rangle$ e date due [stringhe](Teoria%20dei%20linguaggi%20formali.md#^definizione-stringa) di [simboli](Teoria%20dei%20linguaggi%20formali.md#^definizione-simbolo) $\alpha,\beta \in (V \cup T)^*$ e una [variabile](Grammatiche%20libere%20dal%20contesto.md#^definizione-grammatica-libera-dal-contesto) $A \in V$, definiamo una **derivazione in un passo** come la [relazione](Relazioni%20tra%20insiemi.md#^definizione-relazione-n-aria) $\Rightarrow_{\mathcal{G}}$ tale che
> 
> $$
> \alpha A \beta \Rightarrow_{\mathcal{G}} \alpha \gamma \beta
> $$
> 
> se e solo se $A \to \gamma \in P$.
> 
> In tal caso diciamo che $\alpha\gamma\beta$ **deriva in un passo** da $\alpha A\beta$ in $\mathcal{G}$.
> 
> Possiamo omettere $\mathcal{G}$ da $\Rightarrow_\mathcal{G}$ e scrivere solo $\Rightarrow$ quando si può intuire dal contesto che ci stiamo riferendo alla [grammatica](Grammatiche%20libere%20dal%20contesto.md#^definizione-grammatica-libera-dal-contesto) $\mathcal{G}$.
^definizione-derivazione-in-un-passo

%% dove $\alpha A \beta$ è la concatenazione di $\alpha$, $A$ e $\beta$ %%

> [!definizione]+ Definizione: derivazione in zero o più passi
>
> Data una [grammatica libera](Grammatiche%20libere%20dal%20contesto.md#^definizione-grammatica-libera-dal-contesto) $\mathcal{G} = \langle V,T,P,V_0 \rangle$, definiamo una **derivazione in zero o più passi** come la [relazione](Relazioni%20tra%20insiemi.md#^definizione-relazione-n-aria) $\Rightarrow_{\mathcal{G}}^*$, definita come la chiusura riflessiva e transitiva%% Link %% della [relazione di derivazione in un passo](#^definizione-derivazione-in-un-passo) $\Rightarrow_\mathcal{G}$, tale che:
>
> 1. Per ogni [stringa](Teoria%20dei%20linguaggi%20formali.md#^definizione-stringa) $\alpha \in (V \cup T)^*$:
>
>    $$
>    \alpha \Rightarrow_{\mathcal{G}}^* \alpha
>    $$
>
> 2. Se $\alpha \Rightarrow_{\mathcal{G}} \beta$ e $\beta \Rightarrow_{\mathcal{G}}^* \gamma$, allora:
>
>    $$
>    \alpha \Rightarrow_{\mathcal{G}}^* \gamma
>    $$
>
> In tal caso diciamo che $\gamma$ **deriva in zero o più passi** da $\alpha$ in $\mathcal{G}$.
>
> Possiamo omettere $\mathcal{G}$ da $\Rightarrow_{\mathcal{G}}^*$ e scrivere solo $\Rightarrow^*$ quando si può intuire dal contesto che ci stiamo riferendo alla [grammatica](Grammatiche%20libere%20dal%20contesto.md#^definizione-grammatica-libera-dal-contesto) $\mathcal{G}$.
^definizione-derivazione-in-zero-o-piu-passi

> [!esempio]- Esempio: grammatica libera delle stringhe palindrome
> 
> Definiamo la [grammatica libera](Grammatiche%20libere%20dal%20contesto.md#^definizione-grammatica-libera-dal-contesto)
> 
> $$
> \mathcal{G} = \langle \{ A \}, \{ 0,1 \}, \{ A \to \varepsilon \mid 0 \mid 1 \mid 0A0 \mid 1A1 \}, A \rangle 
> $$
> 
> da cui otteniamo per esempio le seguenti [derivazioni](Grammatiche%20libere%20dal%20contesto.md#^definizione-grammatica-libera-dal-contesto):
> - $A \Rightarrow \varepsilon$
> - $A \Rightarrow 0$
> - $A \Rightarrow 1$
> - $A \Rightarrow 0A0 \Rightarrow 0\varepsilon0 = 00$
> - $A \Rightarrow 1A1 \Rightarrow 1\varepsilon1 = 11$
> - $A \Rightarrow 0A0 \Rightarrow 01A10 \Rightarrow 011A110 \Rightarrow 0110110$
> 
> che rappresentano tutte [stringhe palindrome](Teoria%20dei%20linguaggi%20formali.md#^definizione-stringa-palindroma).
^esempio-grammatica-libera-dalle-stringhe-palindrome

> [!definizione]+ Definizione: linguaggio generato da una grammatica libera
> 
> Data una [grammatica libera](Grammatiche%20libere%20dal%20contesto.md#^definizione-grammatica-libera-dal-contesto) $\mathcal{G} = \langle V,T,P,V_0 \rangle$, il **linguaggio generato da $\mathcal{G}$**, denotato come $L(\mathcal{G})$, è il [linguaggio formale](Teoria%20dei%20linguaggi%20formali.md#^definizione-linguaggio-formale) definito come
> 
> $$
> L(\mathcal{G}) \overset{\text{def}}{=} \{ w \in T^* \mid V_0 \Rightarrow^*_\mathcal{G} w \}
> $$
^definizione-linguaggio-generato-da-una-grammatica-libera

> [!esempio]- Esempio di linguaggio generato da una grammatica libera
> 
> Riprendendo l'[esempio della grammatica libera delle stringhe palindrome](Grammatiche%20libere%20dal%20contesto.md#^esempio-grammatica-libera-dalle-stringhe-palindrome)
> 
> $$
> \mathcal{G} = \langle \{ A \}, \{ 0,1 \}, \{ A \to \varepsilon \mid 0 \mid 1 \mid 0A0 \mid 1A1 \}, A \rangle 
> $$
> 
> il suo [linguaggio generato](Grammatiche%20libere%20dal%20contesto.md#^definizione-linguaggio-generato-da-una-grammatica-libera) è
> 
> $$
> L(\mathcal{G}) = \{ w \in \{ 0,1 \}^* \mid w = w^R \}
> $$
> 
> ossia il [linguaggio](Teoria%20dei%20linguaggi%20formali.md#^definizione-linguaggio-formale) formato dalle [stringhe](Teoria%20dei%20linguaggi%20formali.md#^definizione-stringa) di $0$ e $1$ [palindrome](Teoria%20dei%20linguaggi%20formali.md#^definizione-stringa-palindroma).

> [!definizione]+ Definizione: linguaggio libero
> 
> Un [linguaggio](Teoria%20dei%20linguaggi%20formali.md#^definizione-linguaggio-formale) $L$ si dice **linguaggio libero** se esiste una [grammatica libera](Grammatiche%20libere%20dal%20contesto.md#^definizione-grammatica-libera-dal-contesto) $\mathcal{G} = \langle V,T,P,V_0 \rangle$ che lo [genera](Grammatiche%20libere%20dal%20contesto.md#^definizione-linguaggio-generato-da-una-grammatica-libera):
> 
> $$
> L = L(\mathcal{G})
> $$
^definizione-linguaggio-libero

> [!esempio]- Esempio: stringhe della forma $\color{#7F7FFF} \text{a}^n\text{b}^n$
> 
> Definiamo la [grammatica libera](Grammatiche%20libere%20dal%20contesto.md#^definizione-grammatica-libera-dal-contesto)
> 
> $$
> \mathcal{G} = \langle \{ V_0 \}, \{ \text{a},\text{b} \}, \{ V_0 \to \varepsilon \mid \text{a}V_0\text{b} \}, S \rangle 
> $$
> 
> da cui otteniamo per esempio le seguenti [derivazioni](Grammatiche%20libere%20dal%20contesto.md#^definizione-grammatica-libera-dal-contesto):
> - $V_0 \Rightarrow \varepsilon$
> - $V_0 \Rightarrow \text{a}V_0\text{b} \Rightarrow\text{a}\varepsilon\text{b} = \text{ab}$
> - $V_0 \Rightarrow \text{a}V_0\text{b} \Rightarrow \text{aa}V_0\text{bb} \Rightarrow \text{aa}\varepsilon\text{bb} = \text{aabb}$
> - $V_0 \Rightarrow \text{a}V_0\text{b} \Rightarrow \text{aa}V_0\text{bb} \Rightarrow \text{aaa}V_0\text{bbb} \Rightarrow \text{aaa}\varepsilon\text{bbb} = \text{aaabbb}$
> 
> e, più in generale, $V_0 \Rightarrow^* \text{a}^n\text{b}^n$ per ogni $n \in \mathbb{N}$.
^esempio-stringhe-della-forma-anbn

> [!esempio]- Esempio: stringhe della forma $\color{#7F7FFF} \text{a}^m\text{b}^n$
> 
> Definiamo la [grammatica libera](Grammatiche%20libere%20dal%20contesto.md#^definizione-grammatica-libera-dal-contesto)
> 
> $$
> \mathcal{G} = \langle \{ V_0,A,B \}, \{ \text{a},\text{b} \}, \{ V_0 \to AB, A \to \varepsilon \mid \text{a}A, B \to \varepsilon \text{b}B \}, V_0 \rangle 
> $$
> 
> da cui otteniamo per esempio le seguenti [derivazioni](Grammatiche%20libere%20dal%20contesto.md#^definizione-grammatica-libera-dal-contesto):
> - $V_0 \Rightarrow AB \Rightarrow A\varepsilon = A \Rightarrow \varepsilon$
> - $V_0 \Rightarrow AB \Rightarrow \text{a}AB \Rightarrow \text{a}A\text{b}B \Rightarrow \text{a}\varepsilon\text{b}B = \text{ab}B \Rightarrow \text{ab}\varepsilon = \text{ab}$
> - $V_0 \Rightarrow AB \Rightarrow \text{a}AB \Rightarrow \text{aa}AB \Rightarrow \text{aaa}AB \Rightarrow \text{aaa}\varepsilon B = \text{aaa}B \Rightarrow \text{aaab}B \Rightarrow \text{aaab}\varepsilon = \text{aaab}$
> 
> e, più in generale, $V_0 \Rightarrow^* \text{a}^m\text{b}^n$ per ogni $m,n \in \mathbb{N}$.

> [!esempio]- Esempio: espressioni aritmetiche
> 
> Definiamo la [grammatica libera](Grammatiche%20libere%20dal%20contesto.md#^definizione-grammatica-libera-dal-contesto)
> 
> $$
> \mathcal{G} = \langle \{ E \}, \{ \text{x},\text{y}, +, *, (, ) \}, P, E \rangle 
> $$
> 
> in cui $P$ è l'[insieme](Teoria%20degli%20insiemi.md#^definizione-insieme) delle [produzioni](Grammatiche%20libere%20dal%20contesto.md#^definizione-grammatica-libera-dal-contesto)
> 
> $$
> E \to \text{x} \mid \text{y} \mid E+E \mid E*E \mid (E)
> $$
> 
> e da cui otteniamo per esempio le seguenti [derivazioni](Grammatiche%20libere%20dal%20contesto.md#^definizione-grammatica-libera-dal-contesto):
> - $E \Rightarrow E+E \Rightarrow \text{x} + E \Rightarrow \text{x} + \text{y}$
> - $E \Rightarrow E+E \Rightarrow \text{x}+E \Rightarrow \text{x}+E*E \Rightarrow \text{x} + \text{y} * E \Rightarrow \text{x} + \text{y} * \text{y}$
> - $E \Rightarrow E*E \Rightarrow (E)*E \Rightarrow (E+E)*E \Rightarrow (\text{x}+E)*E \Rightarrow (\text{x}+\text{y})*E \Rightarrow (\text{x}+\text{y})*\text{y}$

> [!esempio]- Esempio: assegnamento in Java
> 
> Definiamo la [grammatica libera](Grammatiche%20libere%20dal%20contesto.md#^definizione-grammatica-libera-dal-contesto)
> 
> $$
> \mathcal{G} = \langle \{ V_0,R,E \}, \{ =,[,],\text{c},\text{x} \}, P, V_0 \rangle 
> $$
> 
> in cui $P$ è l'[insieme](Teoria%20degli%20insiemi.md#^definizione-insieme) delle [produzioni](Grammatiche%20libere%20dal%20contesto.md#^definizione-grammatica-libera-dal-contesto)
> 
> $$
> \begin{align*}
> V_0 &\to R = E \\
> R &\to \text{x} \mid R[E] \\
> E &\to \text{c} \mid R
> \end{align*}
> $$
> 
> e da cui otteniamo per esempio le seguenti [derivazioni](Grammatiche%20libere%20dal%20contesto.md#^definizione-grammatica-libera-dal-contesto):
> - $V_0 \Rightarrow R=E \Rightarrow \text{x}=E \Rightarrow \text{x = c}$
> - $V_0 \Rightarrow R = E \Rightarrow R = R \Rightarrow \text{x}=R \Rightarrow \text{x = x}$
> - $V_0 \Rightarrow R=E \Rightarrow R[E]=E \Rightarrow \text{x}[E]=E \Rightarrow \text{x[c]}=E \Rightarrow \text{x[c] = c}$
> 
> Non sono però [derivabili](Grammatiche%20libere%20dal%20contesto.md#^definizione-derivazione-in-zero-o-piu-passi) le seguenti [stringhe](Teoria%20dei%20linguaggi%20formali.md#^definizione-stringa):
> - $V_0 \not\Rightarrow^* \text{x}$
> - $V_0 \not\Rightarrow^* \text{c = x}$

%% 
Esercizio: definire grammatiche per generare i seguenti linguaggi:
1. Linguaggio generato dalla regex $(\text{ab})^*$
2. Stringhe di parentesi quadre bilanciate (es. $\text{[ [ ] [ [ ] ] ]}$)
3. Stringhe di $0$ e $1$ della forma $ww^R$
4. Stringhe di $0$ e $1$ in cui c'è lo stesso numero di $0$ e $1$ (es. $00100111$)
5. Espressioni booleane composte dalle costanti $\text{T}$ (true), $\text{F}$ (false) e i connettivi $\land$ (congiunzione), $\land$ (disgiunzione) e $\lnot$ (negazione). Ammettere la possibilità di usare parentesi (es. $\text{T} \land (\text{F} \lor \lnot\text{T})$ e $\lnot(\text{T} \lor \text{F})$).
%%

%%
Esercizio: descrivere il linguaggio generato dalle seguenti grammatiche:
1. $\langle \{ V_0 \}, \{ \text{a}, \text{b} \}, \{ V_0 \to \varepsilon \mid \text{aa}V_0\text{b} \}, V_0 \rangle$
2. $\langle \{ V_0,A \}, \{ \text{a}, \text{b} \}, \{ V_0 \to \varepsilon \mid AV_0\text{b}, A \to \varepsilon \mid \text{a} \}, V_0 \rangle$
3. $\langle \{ V_0,X,C \}, \{ \text{a}, \text{b}, \text{c} \}, \{ V_0 \to XC, X \to \varepsilon \mid \text{a}X\text{b}, C \to \varepsilon \mid \text{c}C \}, V_0 \rangle$
4. $\langle \{ V_0 \}, \{ \text{a}, \text{b} \}, \{ V_0 \to \varepsilon \mid \text{a}V_0\text{b} \mid \text{b}V_0\text{a} \}, V_0 \rangle$
%%

%% 
cambiare nome al teorema (?)
%%

> [!teorema]+ Teorema di esistenza delle grammatiche libere
> 
> Dato un [linguaggio regolare](Espressioni%20regolari.md#^definizione-linguaggio-regolare) $L$, esiste una [grammatica libera](Grammatiche%20libere%20dal%20contesto.md#^definizione-grammatica-libera-dal-contesto) $\mathcal{G}$ che [genera](Grammatiche%20libere%20dal%20contesto.md#^definizione-linguaggio-generato-da-una-grammatica-libera) $L$:
> 
> $$
> L(\mathcal{G}) = L
> $$
> 
> > [!dimostrazione]- Dimostrazione
> > 
> > Supponiamo che esista un [DFA](Teoria%20degli%20automi.md#^definizione-automa-a-stati-finiti-deterministico-dfa) $\mathcal{D} = \langle \Sigma, Q, \delta, q_0, F \rangle$ che [riconosce](Teoria%20degli%20automi.md#^definizione-linguaggio-riconosciuto-da-un-dfa) $L$:
> > 
> > $$
> > L(\mathcal{D}) = L
> > $$
> > 
> > Definiamo una [grammatica libera](Grammatiche%20libere%20dal%20contesto.md#^definizione-grammatica-libera-dal-contesto) $\mathcal{G} = \langle Q, \Sigma, P, q_0 \rangle$ in cui riutilizziamo direttamente gli elementi del [DFA](Teoria%20degli%20automi.md#^definizione-automa-a-stati-finiti-deterministico-dfa):
> > 
> > | **Elemento** | **[DFA](Teoria%20degli%20automi.md#^definizione-automa-a-stati-finiti-deterministico-dfa)** | **[Grammatica libera](Grammatiche%20libere%20dal%20contesto.md#^definizione-grammatica-libera-dal-contesto)** |
> > | ------------ | ------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------- |
> > | $Q$          | Insieme degli stati                                                                         | Insieme dei simboli non terminali                                                                             |
> > | $\Sigma$     | Alfabeto                                                                                    | Insieme dei simboli terminali                                                                                 |
> > | $q_0$        | Stato iniziale                                                                              | Simbolo iniziale                                                                                              |
> > 
> > In particolare, notiamo come ogni [stato del DFA](Teoria%20degli%20automi.md#^definizione-automa-a-stati-finiti-deterministico-dfa) diventa un [simbolo non terminale della grammatica](Grammatiche%20libere%20dal%20contesto.md#^definizione-grammatica-libera-dal-contesto), in modo che durante ogni [derivazione](Grammatiche%20libere%20dal%20contesto.md#^definizione-derivazione-in-zero-o-piu-passi) il [simbolo non terminale](Grammatiche%20libere%20dal%20contesto.md#^definizione-grammatica-libera-dal-contesto) rappresenti lo [stato](Teoria%20degli%20automi.md#^definizione-automa-a-stati-finiti-deterministico-dfa) in cui si troverebbe il [DFA](Teoria%20degli%20automi.md#^definizione-automa-a-stati-finiti-deterministico-dfa).
> > 
> > L'[insieme delle produzioni](Grammatiche%20libere%20dal%20contesto.md#^definizione-grammatica-libera-dal-contesto) $P$ viene definito attraverso due regole:
> > 1. Simulando le [transizioni del DFA](Teoria%20degli%20automi.md#^definizione-automa-a-stati-finiti-deterministico-dfa): quando il DFA si trova nello stato $q \in Q$ e legge il simbolo $a \in \Sigma$ raggiunge lo stato $q' = \delta(q,a)$. La [grammatica libera](Grammatiche%20libere%20dal%20contesto.md#^definizione-grammatica-libera-dal-contesto) $\mathcal{G}$ introduce quindi la [produzione](Grammatiche%20libere%20dal%20contesto.md#^definizione-grammatica-libera-dal-contesto) $q \to aq'$ con la seguente regola:
> > 	$$
> > 	q \in Q \land a \in \Sigma \implies q \to a\delta(q,a) \in P
> > 	$$
> > 2. Permettendo di terminare una [derivazione](Grammatiche%20libere%20dal%20contesto.md#^definizione-derivazione-in-zero-o-piu-passi) in uno stato finale: quando il [simbolo non terminale](Grammatiche%20libere%20dal%20contesto.md#^definizione-grammatica-libera-dal-contesto) $q$ rappresenta uno [stato finale](Teoria%20degli%20automi.md#^definizione-automa-a-stati-finiti-deterministico-dfa) (cioè $q \in F$), possiamo eliminarlo sostituendolo con la [stringa vuota](Teoria%20dei%20linguaggi%20formali.md#^definizione-stringa-vuota):
> > 	$$
> > 	q \in F \implies q \to \varepsilon
> > 	$$
> > 
> > Ciò implica che una [derivazione](Grammatiche%20libere%20dal%20contesto.md#^definizione-derivazione-in-zero-o-piu-passi) deve avere necessariamente questa struttura:
> > 
> > $$
> > q_0 \Rightarrow a_1q_1 \Rightarrow a_1a_2q_2 \Rightarrow^* a_1a_2\ldots a_nq_n \Rightarrow a_1a_2\ldots a_n
> > $$
> > 
> > dove:
> > - $a_1, a_2, \ldots, a_n \in \Sigma$ sono i [simboli terminali](Grammatiche%20libere%20dal%20contesto.md#^definizione-grammatica-libera-dal-contesto),
> > - $q_1,q_2,\ldots,q_n \in Q$ sono i [simboli non terminali](Grammatiche%20libere%20dal%20contesto.md#^definizione-grammatica-libera-dal-contesto), ossia gli [stati](Teoria%20degli%20automi.md#^definizione-automa-a-stati-finiti-deterministico-dfa) che il [DFA](Teoria%20degli%20automi.md#^definizione-automa-a-stati-finiti-deterministico-dfa) attraversa,
> > - $a_1a_2\ldots a_n = w$ è la [stringa](Teoria%20dei%20linguaggi%20formali.md#^definizione-stringa) [generata](Grammatiche%20libere%20dal%20contesto.md#^definizione-linguaggio-generato-da-una-grammatica-libera)/[riconosciuta](Teoria%20degli%20automi.md#^definizione-linguaggio-riconosciuto-da-un-dfa) e
> > - l'ultimo passaggio $q_n \to \varepsilon$ è possibile solo perché $q_n \in F$ (cioè $q_n$ è uno stato finale).
> > 
> > Per dimostrare che questa [grammatica](Grammatiche%20libere%20dal%20contesto.md#^definizione-grammatica-libera-dal-contesto) $\mathcal{G}$ [genera](Grammatiche%20libere%20dal%20contesto.md#^definizione-linguaggio-generato-da-una-grammatica-libera) esattamente il [linguaggio](Teoria%20dei%20linguaggi%20formali.md#^definizione-linguaggio-formale) $L$, dobbiamo dimostrare che una [stringa](Teoria%20dei%20linguaggi%20formali.md#^definizione-stringa) $w$ è generata dalla grammatica se e solo se viene riconosciuta dal [DFA](Teoria%20degli%20automi.md#^definizione-automa-a-stati-finiti-deterministico-dfa), ovvero:
> > 
> > $$
> > q_0 \Rightarrow^* w \iff \hat{\delta}(q_0,w)\in F
> > $$
> > 
> > Dimostriamo nella direzione dell'implicazione ($\implies$): supponiamo che la [grammatica](Grammatiche%20libere%20dal%20contesto.md#^definizione-grammatica-libera-dal-contesto) $\mathcal{G}$ [generi](Grammatiche%20libere%20dal%20contesto.md#^definizione-linguaggio-generato-da-una-grammatica-libera) $w$, ovvero valga:
> > 
> > $$
> > q_0 \Rightarrow^* w
> > $$
> > 
> > Per la struttura delle [produzioni](Grammatiche%20libere%20dal%20contesto.md#^definizione-grammatica-libera-dal-contesto) che abbiamo appena visto, la [derivazione](Grammatiche%20libere%20dal%20contesto.md#^definizione-derivazione-in-zero-o-piu-passi) deve necessariamente terminare attraverso una produzione del tipo:
> > 
> > $$
> > q_n \to \varepsilon
> > $$
> > 
> > Poiché questa produzione è stata definita soltanto per gli [stati finali](Teoria%20degli%20automi.md#^definizione-automa-a-stati-finiti-deterministico-dfa), sappiamo che:
> > 
> > $$
> > q_n \in F
> > $$
> > 
> > Inoltre, per come abbiamo definito le [produzioni](Grammatiche%20libere%20dal%20contesto.md#^definizione-grammatica-libera-dal-contesto), ogni passaggio della [derivazione](Grammatiche%20libere%20dal%20contesto.md#^definizione-derivazione-in-zero-o-piu-passi) del tipo $q_{i-1}\to a_iq_i$ corrisponde a una [transizione del DFA](Teoria%20degli%20automi.md#^definizione-automa-a-stati-finiti-deterministico-dfa), ovvero:
> > 
> > $$
> > q_i = \delta(q_{i-1},a_i)
> > $$
> > 
> > Pertanto, per [definizione della _funzione di transizione estesa di un DFA_](Teoria%20degli%20automi.md#^definizione-funzione-di-transizione-estesa-di-un-dfa), dopo aver letto l'intera [stringa](Teoria%20dei%20linguaggi%20formali.md#^definizione-stringa) $w=a_1a_2\ldots a_n$  il [DFA](Teoria%20degli%20automi.md#^definizione-automa-a-stati-finiti-deterministico-dfa) si trova nello stato $q_n$, ovvero:
> > 
> > $$
> > q_n = \hat{\delta}(q_0,w)
> > $$
> > 
> > Poiché sappiamo che $q_n\in F$, sostituendo otteniamo:
> > 
> > $$
> > \hat{\delta}(q_0,w)\in F
> > $$
> > 
> > Abbiamo quindi dimostrato questa direzione della bi-implicazione%% link %%.
> > 
> > Dimostriamo nella direzione opposta dell'implicazione ($\impliedby$): supponiamo che il [DFA](Teoria%20degli%20automi.md#^definizione-automa-a-stati-finiti-deterministico-dfa) [riconosca](Teoria%20degli%20automi.md#^definizione-linguaggio-riconosciuto-da-un-dfa) $w$, ovvero valga:
> > 
> > $$
> > \hat{\delta}(q_0,w)\in F
> > $$
> > 
> > Sia $w=a_1a_2\ldots a_n$ la [stringa](Teoria%20dei%20linguaggi%20formali.md#^definizione-stringa) da riconoscere e siano $q_0,q_1,\ldots,q_n$ gli [stati](Teoria%20degli%20automi.md#^definizione-automa-a-stati-finiti-deterministico-dfa) attraversati dal [DFA](Teoria%20degli%20automi.md#^definizione-automa-a-stati-finiti-deterministico-dfa) durante la sua lettura. Per [definizione della _funzione di transizione estesa di un DFA_](Teoria%20degli%20automi.md#^definizione-funzione-di-transizione-estesa-di-un-dfa) vale che:
> > 
> > $$
> > q_i = \delta(q_{i-1},a_i)
> > $$
> > 
> > con $1\leq i\leq n$.
> > 
> > Poiché abbiamo definito una [produzione](Grammatiche%20libere%20dal%20contesto.md#^definizione-grammatica-libera-dal-contesto) per ogni [transizione del DFA](Teoria%20degli%20automi.md#^definizione-automa-a-stati-finiti-deterministico-dfa), possiamo applicare consecutivamente le produzioni corrispondenti a tali transizioni, ottenendo:
> > 
> > $$
> > \begin{aligned}
> > q_0
> > &\Rightarrow a_1q_1\\
> > &\Rightarrow a_1a_2q_2\\
> > &\Rightarrow \cdots\\
> > &\Rightarrow a_1a_2\ldots a_nq_n
> > \end{aligned}
> > $$
> > 
> > Ma, per ipotesi, il [DFA](Teoria%20degli%20automi.md#^definizione-automa-a-stati-finiti-deterministico-dfa) [riconosce](Teoria%20degli%20automi.md#^definizione-linguaggio-riconosciuto-da-un-dfa) $w$, quindi lo stato raggiunto dopo aver letto l'intera [stringa](Teoria%20dei%20linguaggi%20formali.md#^definizione-stringa) appartiene all'[insieme degli stati finali](Teoria%20degli%20automi.md#^definizione-automa-a-stati-finiti-deterministico-dfa) $F$:
> > 
> > $$
> > q_n = \hat{\delta}(q_0,w)\in F
> > $$
> > 
> > Di conseguenza, possiamo applicare anche la produzione $q_n\to\varepsilon$, che abbiamo definito per tutti gli stati finali, ottenendo:
> > 
> > $$
> > \begin{aligned}
> > q_0
> > &\Rightarrow a_1q_1\\
> > &\Rightarrow a_1a_2q_2\\
> > &\Rightarrow \cdots\\
> > &\Rightarrow a_1a_2\ldots a_nq_n\\
> > &\Rightarrow a_1a_2\ldots a_n\\
> > &=w
> > \end{aligned}
> > $$
> > 
> > Abbiamo quindi dimostrato anche quest'altra direzione della bi-implicazione%% Link %%.
> > 
> > Avendo dimostrato entrambe le direzioni, possiamo concludere che:
> > 
> > $$
> > q_0 \Rightarrow^* w \iff \hat{\delta}(q_0,w)\in F
> > $$
> > 
> > Ricordando che, per [definizione di _linguaggio generato da una grammatica libera_](Grammatiche%20libere%20dal%20contesto.md#^definizione-linguaggio-generato-da-una-grammatica-libera),
> > 
> > $$
> > L(\mathcal{G}) = \{ w \in \Sigma^* \mid q_0 \Rightarrow^* w \}
> > $$
> > 
> > e che, per [definizione di _linguaggio riconosciuto da un DFA_](Teoria%20degli%20automi.md#^definizione-linguaggio-riconosciuto-da-un-dfa),
> > 
> > $$
> > L(\mathcal{D}) = \{ w \in \Sigma^* \mid \hat\delta(q_0,w) \in F \}
> > $$
> > 
> > e avendo
> > 
> > $$
> > q_0 \Rightarrow^* w \iff \hat{\delta}(q_0,w)\in F
> > $$
> > 
> > possiamo concludere che
> > 
> > $$
> > L(\mathcal G) = L(\mathcal D)
> > $$
> > 
> > e, avendo $L(\mathcal{D}) = L$ per ipotesi, concludiamo che
> > 
> > $$
> > L(\mathcal G) = L
> > $$
> > 
> > $\blacksquare$

> [!osservazione]+ Osservazione: linguaggi regolari $\color{#7F7F7F} \subsetneq$ linguaggi liberi
> 
> Questo teorema%% link %% mostra che le [grammatiche libere](Grammatiche%20libere%20dal%20contesto.md#^definizione-grammatica-libera-dal-contesto) possono [generare](Grammatiche%20libere%20dal%20contesto.md#^definizione-linguaggio-generato-da-una-grammatica-libera) **tutti** i [linguaggi regolari](Espressioni%20regolari.md#^definizione-linguaggio-regolare) ma, sapendo anche che le [grammatiche](Grammatiche%20libere%20dal%20contesto.md#^definizione-grammatica-libera-dal-contesto) possono [generare](Grammatiche%20libere%20dal%20contesto.md#^definizione-linguaggio-generato-da-una-grammatica-libera) anche [linguaggi](Teoria%20dei%20linguaggi%20formali.md#^definizione-teoria-dei-linguaggi-formali) **non** [regolari](Espressioni%20regolari.md#^definizione-linguaggio-regolare) (come il [linguaggio $\{ \text{a}^n\text{b}^n  \mid n \in \mathbb{N} \}$ che abbiamo dimostrato essere **non** regolare](Pumping%20lemma.md#^esempio-akbk-non-e-regolare) ma comunque [generabile da una grammatica libera](Grammatiche%20libere%20dal%20contesto.md#^esempio-stringhe-della-forma-anbn)), allora possiamo dedurre che i [linguaggi regolari](Espressioni%20regolari.md#^definizione-linguaggio-regolare) sono un [sottoinsieme proprio](Teoria%20degli%20insiemi.md#^definizione-sottoinsieme-proprio) dei [linguaggi liberi](Grammatiche%20libere%20dal%20contesto.md#^definizione-linguaggio-libero):
> 
> $$
> \text{linguaggi regolari} \subsetneq \text{linguaggi liberi}
> $$

# 1 - Alberi sintattici

> [!definizione]+ Definizione: albero sintattico
> 
> Data una [grammatica libera](Grammatiche%20libere%20dal%20contesto.md#^definizione-grammatica-libera-dal-contesto) $\mathcal{G} = \langle V,T,P,V_0 \rangle$, un **albero sintattico $\boldsymbol{\mathcal{A}}$ di $\boldsymbol{\mathcal{G}}$** è un albero%% Link %% con le seguenti caratteristiche:
> 1. Ogni nodo interno%% link %% non foglia%% link %% è etichettato con una [variabile](Grammatiche%20libere%20dal%20contesto.md#^definizione-grammatica-libera-dal-contesto) in $V$.
> 2. Ogni foglia%% link %% è etichettata con una [variabile](Grammatiche%20libere%20dal%20contesto.md#^definizione-grammatica-libera-dal-contesto) in $V$ o con un [simbolo terminale](Grammatiche%20libere%20dal%20contesto.md#^definizione-grammatica-libera-dal-contesto) in $T$ o con la [stringa vuota](Teoria%20dei%20linguaggi%20formali.md#^definizione-stringa-vuota) $\varepsilon$.
> 3. Se una foglia%% link %% è etichettata con la [stringa vuota](Teoria%20dei%20linguaggi%20formali.md#^definizione-stringa-vuota) $\varepsilon$, è anche l'unico figlio%% link %% del suo genitore%% link %%.
> 4. Se un nodo interno%% link %% è etichettato con $A$ e i suoi figli sono etichettati (da sinistra a destra) con $X_1,X_2,\ldots,X_n$, allora $A \to X_1X_2\ldots X_n$ è una [produzione](Grammatiche%20libere%20dal%20contesto.md#^definizione-grammatica-libera-dal-contesto) in $P$.
^definizione-albero-sintattico

> [!esempio]- Esempio: albero sintattico delle espressioni aritmetiche
> 
> Data la [grammatica libera](Grammatiche%20libere%20dal%20contesto.md#^definizione-grammatica-libera-dal-contesto)
> 
> $$
> \mathcal{G} = \langle \{ E \}, \{ 0,1,\ldots,9,+,*,(,) \},P, E \rangle 
> $$
> 
> in cui $P$ è l'[insieme](Teoria%20degli%20insiemi.md#^definizione-insieme) delle [produzioni](Grammatiche%20libere%20dal%20contesto.md#^definizione-grammatica-libera-dal-contesto)
> 
> $$
> E \to 0 \mid 1 \mid \ldots \mid 9 \mid E+E \mid E*E \mid (E)
> $$
> 
> un suo possibile [albero sintattico](Grammatiche%20libere%20dal%20contesto.md#^definizione-albero-sintattico) $\mathcal{A}$ è
> 
> ![esempio-albero-sintattico-delle-espressioni-aritmetiche.drawio](esempio-albero-sintattico-delle-espressioni-aritmetiche.drawio.svg)
> 
> che corrisponde alla [produzione](Grammatiche%20libere%20dal%20contesto.md#^definizione-grammatica-libera-dal-contesto)
> 
> $$
> \begin{align*}
> E &\Rightarrow E+E \\
> &\Rightarrow 1+E \\
> &\Rightarrow 1+E*E \\
> &\Rightarrow 1+2*E \\
> &\Rightarrow 1+2*3
> \end{align*}
> $$
^esempio-albero-sintattico-delle-espressioni-aritmetiche

> [!definizione]+ Definizione: prodotto di un albero sintattico
> 
> Il **prodotto $\boldsymbol{\alpha}$** di un [albero sintattico](Grammatiche%20libere%20dal%20contesto.md#^definizione-albero-sintattico) $\mathcal{A}$ è la [stringa](Teoria%20dei%20linguaggi%20formali.md#^definizione-stringa) ottenuta [concatenando](Teoria%20dei%20linguaggi%20formali.md#^definizione-concatenazione-di-due-stringhe), da sinistra verso destra, le etichette di tutte le foglie%% link %% dell'[albero](Grammatiche%20libere%20dal%20contesto.md#^definizione-albero-sintattico).
^definizione-prodotto-di-un-albero-sintattico

> [!esempio]- Esempio di prodotto
> 
> Riprendendo l'[esempio dell'albero sintattico delle espressioni aritmetiche](Grammatiche%20libere%20dal%20contesto.md#^esempio-albero-sintattico-delle-espressioni-aritmetiche), il suo [prodotto](Grammatiche%20libere%20dal%20contesto.md#^definizione-prodotto-di-un-albero-sintattico) è la [stringa](Teoria%20dei%20linguaggi%20formali.md#^definizione-stringa)
> 
> $$
> \alpha = 1 + 2 * 3
> $$

> [!teorema]+ Teorema di corrispondenza tra derivazioni e alberi sintattici
> 
> Dato un [albero sintattico](Grammatiche%20libere%20dal%20contesto.md#^definizione-albero-sintattico) $\mathcal{A}$ di una [grammatica libera](Grammatiche%20libere%20dal%20contesto.md#^definizione-grammatica-libera-dal-contesto) $\mathcal{G}$ con radice%% link %% $R$ e [prodotto](Grammatiche%20libere%20dal%20contesto.md#^definizione-prodotto-di-un-albero-sintattico) $\alpha$, $R$ è [derivabile](Grammatiche%20libere%20dal%20contesto.md#^definizione-derivazione-in-zero-o-piu-passi) in $\alpha$ se e solo se esiste $\mathcal{A}$:
> 
> $$
> R \Rightarrow_{\mathcal{G}}^* \alpha \iff
> \exists\mathcal{A}\text{ albero sintattico di }\mathcal{G}
> . (R \text{ radice di } \mathcal{A} \land \alpha \text{ prodotto di } \mathcal{A})
> $$
^teorema-di-corrispondenza-tra-derivazioni-e-alberi-sintattici

## 1.1 - Grammatiche ambigue

> [!definizione]+ Definizione: grammatica ambigua
> 
> Una [grammatica libera](Grammatiche%20libere%20dal%20contesto.md#^definizione-grammatica-libera-dal-contesto) $\mathcal{G}$ si dice **ambigua** se ammette più [alberi sintattici](Grammatiche%20libere%20dal%20contesto.md#^definizione-albero-sintattico) distinti con lo stesso [prodotto](Grammatiche%20libere%20dal%20contesto.md#^definizione-prodotto-di-un-albero-sintattico).
^definizione-grammatica-ambigua

> [!esempio]- Esempio di grammatica ambigua
> 
> Riprendendo l'[esempio dell'albero sintattico delle espressioni aritmetiche](Grammatiche%20libere%20dal%20contesto.md#^esempio-albero-sintattico-delle-espressioni-aritmetiche), abbiamo che il [prodotto](Grammatiche%20libere%20dal%20contesto.md#^definizione-prodotto-di-un-albero-sintattico) $\alpha = 1 + 2*3$ può essere generato da entrambi questi [alberi sintattici](Grammatiche%20libere%20dal%20contesto.md#^definizione-albero-sintattico), rendendo questa [grammatica ambigua](Grammatiche%20libere%20dal%20contesto.md#^definizione-grammatica-ambigua):
> 
> ![esempio-albero-sintattico-delle-espressioni-aritmetiche.drawio](esempio-albero-sintattico-delle-espressioni-aritmetiche.drawio.svg)
> 
> e
> 
> ![esempio-di-grammatica-ambigua.drawio](esempio-di-grammatica-ambigua.drawio.svg)
> 
> Questi due [alberi](Grammatiche%20libere%20dal%20contesto.md#^definizione-albero-sintattico) sottintendono due significati molto diversi per l'espressione $1+2*3$ che certamente vorremmo tradurre in modi diversi: per esempio, si potrebbero introdurre le parentesi per distingue tra $1 + (2*3)$ nel primo caso e $(1+2)*3$ nel secondo caso.
^esempio-di-grammatica-ambigua

> [!attenzione]+ Attenzione: grammatiche ambigue hanno alberi sintattici distinti, non derivazioni distinte
> 
> Per avere una [grammatica ambigua](Grammatiche%20libere%20dal%20contesto.md#^definizione-grammatica-ambigua) basta trovare due [alberi sintattici](Grammatiche%20libere%20dal%20contesto.md#^definizione-albero-sintattico) distinti con lo stesso [prodotto](Grammatiche%20libere%20dal%20contesto.md#^definizione-prodotto-di-un-albero-sintattico), ma non basta trovare due [derivazioni](Grammatiche%20libere%20dal%20contesto.md#^definizione-derivazione-in-zero-o-piu-passi) distinte che [generano](Grammatiche%20libere%20dal%20contesto.md#^definizione-linguaggio-generato-da-una-grammatica-libera) la stessa [stringa](Teoria%20dei%20linguaggi%20formali.md#^definizione-stringa): per esempio, le [derivazioni](Grammatiche%20libere%20dal%20contesto.md#^definizione-derivazione-in-un-passo)
> 
> $$
> E \Rightarrow E+E \Rightarrow \underline{1+E} \Rightarrow 1+2
> $$
> 
> e
> 
> $$
> E \Rightarrow E+E \Rightarrow \underline{E+2} \Rightarrow 1+2
> $$
> 
> Queste due [derivazioni](Grammatiche%20libere%20dal%20contesto.md#^definizione-derivazione-in-un-passo) sono evidentemente distinte (notiamo la parte sottolineata) nonostante [generino](Grammatiche%20libere%20dal%20contesto.md#^definizione-linguaggio-generato-da-una-grammatica-libera) la stessa [stringa](Teoria%20dei%20linguaggi%20formali.md#^definizione-stringa) $1+2$, ma corrispondono allo stesso [albero sintattico](Grammatiche%20libere%20dal%20contesto.md#^definizione-albero-sintattico):
> 
> ![attenzione-grammatiche-ambigue-hanno-alberi-sintattici-distinti.drawio](attenzione-grammatiche-ambigue-hanno-alberi-sintattici-distinti.drawio.svg)
> 
> L'ordine in cui vengono riscritte [variabili](Grammatiche%20libere%20dal%20contesto.md#^definizione-grammatica-libera-dal-contesto) **diverse** è irrilevante, ciò che conta è se la **stessa** [variabile](Grammatiche%20libere%20dal%20contesto.md#^definizione-grammatica-libera-dal-contesto) viene riscritta in modi **diversi** come [abbiamo visto prima](Grammatiche%20libere%20dal%20contesto.md#^esempio-di-grammatica-ambigua).
^attenzione-grammatiche-ambigue-hanno-alberi-sintattici-distinti

Imponendo quindi un particolare ordine di riscrittura delle variabili possiamo individuale l'[ambiguità](Grammatiche%20libere%20dal%20contesto.md#^definizione-grammatica-ambigua) guardando le [derivazioni](Grammatiche%20libere%20dal%20contesto.md#^definizione-derivazione-in-zero-o-piu-passi).

> [!definizione]+ Definizione: derivazione canonica a sinistra e a destra
> 
> Data una [grammatica libera](Grammatiche%20libere%20dal%20contesto.md#^definizione-grammatica-libera-dal-contesto) $\mathcal{G} = \langle V,T,P,V_0 \rangle$ e un suo [albero sintattico](Grammatiche%20libere%20dal%20contesto.md#^definizione-albero-sintattico) con [prodotto](Grammatiche%20libere%20dal%20contesto.md#^definizione-prodotto-di-un-albero-sintattico) $\alpha$, la [derivazione](Grammatiche%20libere%20dal%20contesto.md#^definizione-derivazione-in-zero-o-piu-passi) $V_0 \Rightarrow^* \alpha$ si dice:
> - **Derivazione canonica a sinistra** e si indica con $\Rightarrow^*_{\text{lm}}$ (dove $\text{lm}$ sta per _**l**eft **m**ost_, ossia "più a sinistra" in inglese) se in ogni [passo](Grammatiche%20libere%20dal%20contesto.md#^definizione-derivazione-in-un-passo) viene riscritta la [variabile](Grammatiche%20libere%20dal%20contesto.md#^definizione-grammatica-libera-dal-contesto) che si trova più a sinistra nell'[albero sintattico](Grammatiche%20libere%20dal%20contesto.md#^definizione-albero-sintattico) o, equivalentemente, nel suo [prodotto](Grammatiche%20libere%20dal%20contesto.md#^definizione-prodotto-di-un-albero-sintattico) $\alpha$.
> - **Derivazione canonica a destra** e si indica con $\Rightarrow^*_{\text{rm}}$ (dove $\text{rm}$ sta per _**r**ight **m**ost_, ossia "più a destra" in inglese) se in ogni [passo](Grammatiche%20libere%20dal%20contesto.md#^definizione-derivazione-in-un-passo) viene riscritta la [variabile](Grammatiche%20libere%20dal%20contesto.md#^definizione-grammatica-libera-dal-contesto) che si trova più a destra nell'[albero sintattico](Grammatiche%20libere%20dal%20contesto.md#^definizione-albero-sintattico) o, equivalentemente, nel suo [prodotto](Grammatiche%20libere%20dal%20contesto.md#^definizione-prodotto-di-un-albero-sintattico) $\alpha$.
> 
> La stessa definizione si applica anche per la [relazione di _derivazione in un passo_](Grammatiche%20libere%20dal%20contesto.md#^definizione-derivazione-in-un-passo) $\Rightarrow$ in cui si può specificare $\Rightarrow_\text{lm}$ o $\Rightarrow_\text{rm}$.
^definizione-derivazione-canonica-a-sinistra-e-a-destra

> [!proposizione]+ Proposizione: ambiguità con due derivazioni canoniche distinte
> 
> Data una [grammatica libera](Grammatiche%20libere%20dal%20contesto.md#^definizione-grammatica-libera-dal-contesto) $\mathcal{G} = \langle V,T,P,V_0 \rangle$, se esistono due [derivazioni canoniche](Grammatiche%20libere%20dal%20contesto.md#^definizione-derivazione-canonica-a-sinistra-e-a-destra) distinte di $\mathcal{G}$ (entrambe [a sinistra](Grammatiche%20libere%20dal%20contesto.md#^definizione-derivazione-canonica-a-sinistra-e-a-destra) o [a destra](Grammatiche%20libere%20dal%20contesto.md#^definizione-derivazione-canonica-a-sinistra-e-a-destra)) che portano alla stessa [stringa](Teoria%20dei%20linguaggi%20formali.md#^definizione-stringa) allora $\mathcal{G}$ è [ambigua](Grammatiche%20libere%20dal%20contesto.md#^definizione-grammatica-ambigua).
^proposizione-ambiguita-con-due-derivazioni-canoniche-distinte

> [!esempio]- Esempio di ambiguità con due derivazioni canoniche distinte
> 
> Riprendiamo l'[esempio di grammatica ambigua](Grammatiche%20libere%20dal%20contesto.md#^esempio-di-grammatica-ambigua): possiamo verificare l'[ambiguità della grammatica](Grammatiche%20libere%20dal%20contesto.md#^definizione-grammatica-ambigua) trovando due [derivazioni canoniche a sinistra](Grammatiche%20libere%20dal%20contesto.md#^definizione-derivazione-canonica-a-sinistra-e-a-destra) che ottengono lo stesso [prodotto](Grammatiche%20libere%20dal%20contesto.md#^definizione-prodotto-di-un-albero-sintattico) $\alpha = 1+2*3$ nonostante gli [alberi sintattici](Grammatiche%20libere%20dal%20contesto.md#^definizione-albero-sintattico) siano distinti.
> 
> In particolare, per l'[albero sintattico](Grammatiche%20libere%20dal%20contesto.md#^definizione-albero-sintattico)
> 
> ![esempio-albero-sintattico-delle-espressioni-aritmetiche.drawio](esempio-albero-sintattico-delle-espressioni-aritmetiche.drawio.svg)
> 
> abbiamo la seguente [derivazione canonica a sinistra](Grammatiche%20libere%20dal%20contesto.md#^definizione-derivazione-canonica-a-sinistra-e-a-destra):
> 
> $$
> \begin{align*}
> E &\Rightarrow_\text{lm} E+E \\
> &\Rightarrow_\text{lm} 1+E \\
> &\Rightarrow_\text{lm} 1+E*E \\
> &\Rightarrow_\text{lm} 1+2*E \\
> &\Rightarrow_\text{lm} 1+2*3
> \end{align*}
> $$
> 
> Invece, per l'altro [albero sintattico](Grammatiche%20libere%20dal%20contesto.md#^definizione-albero-sintattico)
> 
> ![esempio-di-grammatica-ambigua.drawio](esempio-di-grammatica-ambigua.drawio.svg)
> 
> abbiamo la seguente [derivazione canonica a sinistra](Grammatiche%20libere%20dal%20contesto.md#^definizione-derivazione-canonica-a-sinistra-e-a-destra):
> 
> $$
> \begin{align*}
> E &\Rightarrow_\text{lm} E*E \\
> &\Rightarrow_\text{lm} E+E*E \\
> &\Rightarrow_\text{lm} 1+E*E \\
> &\Rightarrow_\text{lm} 1+2*E \\
> &\Rightarrow_\text{lm} 1+2*3
> \end{align*}
> $$
> 
> Per la [proposizione sull'ambiguità](Grammatiche%20libere%20dal%20contesto.md#^proposizione-ambiguita-con-due-derivazioni-canoniche-distinte), avendo trovato due [derivazioni canoniche a sinistra](Grammatiche%20libere%20dal%20contesto.md#^definizione-derivazione-canonica-a-sinistra-e-a-destra) distinte, possiamo confermare che si tratta di una [grammatica ambigua](Grammatiche%20libere%20dal%20contesto.md#^definizione-grammatica-ambigua).

 %%
Esercizio: mostrare che le seguenti grammatiche sono ambigue:
1. $S \to \text{a}S \mid \text{a}S\text{b}S \mid \varepsilon$
2. $B \to \text{T} \mid \text{F}\mid B \land B \mid B \lor B \mid \lnot B \mid (B)$
trovando per ciascuna:
- Due alberi sintattici distinti con lo stesso prodotto
- Due derivazioni canoniche a sinistra distinte per la stessa stringa
- Due derivazioni canoniche a destra distinte per la stessa stringa
%%

### 1.1.1 - Eliminazione delle ambiguità

Vediamo come è possibile, in alcuni casi, eliminare l'[ambiguità](Grammatiche%20libere%20dal%20contesto.md#^definizione-grammatica-ambigua) da una [grammatica](Grammatiche%20libere%20dal%20contesto.md#^definizione-grammatica-libera-dal-contesto) ottenendone una equivalente (e cioè che [genera](Grammatiche%20libere%20dal%20contesto.md#^definizione-linguaggio-generato-da-una-grammatica-libera) lo stesso [linguaggio](Teoria%20dei%20linguaggi%20formali.md#^definizione-linguaggio-formale)) che non sia [ambigua](Grammatiche%20libere%20dal%20contesto.md#^definizione-grammatica-ambigua).

Per eliminare l'[ambiguità](Grammatiche%20libere%20dal%20contesto.md#^definizione-grammatica-ambigua), dobbiamo darci delle regole in base alle quali decidere come standardizzare l'interpretazione di un [albero sintattico](Grammatiche%20libere%20dal%20contesto.md#^definizione-albero-sintattico) a partire dal suo [prodotto](Grammatiche%20libere%20dal%20contesto.md#^definizione-prodotto-di-un-albero-sintattico), creando così una [biettività](Proprietà%20delle%20funzioni.md#^definizione-biettivita) tra ogni [albero](Grammatiche%20libere%20dal%20contesto.md#^definizione-albero-sintattico) e il suo [prodotto](Grammatiche%20libere%20dal%20contesto.md#^definizione-prodotto-di-un-albero-sintattico) (e cioè creando una corrispondenza uno a uno).

> [!esempio]- Esempio di eliminazione delle ambiguità
> 
> Riprendiamo l'[esempio di grammatica ambigua](Grammatiche%20libere%20dal%20contesto.md#^esempio-di-grammatica-ambigua): lì abbiamo un [prodotto](Grammatiche%20libere%20dal%20contesto.md#^definizione-prodotto-di-un-albero-sintattico), che è
> 
> $$
> 1 + 2 * 3
> $$
> 
> a cui però corrispondono due [alberi sintattici](Grammatiche%20libere%20dal%20contesto.md#^definizione-albero-sintattico) diversi:
> 
> ![esempio-albero-sintattico-delle-espressioni-aritmetiche.drawio](esempio-albero-sintattico-delle-espressioni-aritmetiche.drawio.svg)
> 
> in cui il [prodotto](Grammatiche%20libere%20dal%20contesto.md#^definizione-prodotto-di-un-albero-sintattico) verrebbe interpretato come $1+(2*3)$ e
> 
> ![esempio-di-grammatica-ambigua.drawio](esempio-di-grammatica-ambigua.drawio.svg)
> 
> in cui il [prodotto](Grammatiche%20libere%20dal%20contesto.md#^definizione-prodotto-di-un-albero-sintattico) verrebbe interpretato come $(1+2)*3$.
> 
> In questo caso, trattandosi di due operatori diversi ($+$ e $*$), possiamo sfruttare le convenzioni dell'aritmetica e stabilire che ha precedenza l'operatore $*$, stabilendo così che l'unico [albero sintattico](Grammatiche%20libere%20dal%20contesto.md#^definizione-albero-sintattico) che si può associare correttamente al [prodotto](Grammatiche%20libere%20dal%20contesto.md#^definizione-prodotto-di-un-albero-sintattico) $1+2*3$ è il primo, quello in cui viene interpretato come $1+(2*3)$.
> 
> Ma cosa succede nel caso in cui usiamo gli stessi operatori? Per esempio, nel caso del [prodotto](Grammatiche%20libere%20dal%20contesto.md#^definizione-prodotto-di-un-albero-sintattico) $1+2+3$ possiamo risalire a due [alberi sintattici](Grammatiche%20libere%20dal%20contesto.md#^definizione-albero-sintattico) diversi:
> 
> ![eliminazione-delle-ambiguita-1.drawio](eliminazione-delle-ambiguita-1.drawio.svg)
> 
> in cui il [prodotto](Grammatiche%20libere%20dal%20contesto.md#^definizione-prodotto-di-un-albero-sintattico) verrebbe interpretato come $(1+2)+3$ e
> 
> ![eliminazione-delle-ambiguita-2.drawio](eliminazione-delle-ambiguita-2.drawio.svg)
> 
> in cui il [prodotto](Grammatiche%20libere%20dal%20contesto.md#^definizione-prodotto-di-un-albero-sintattico) verrebbe interpretato come $1+(2+3)$.
> 
> A questo punto, in casi come questi in cui abbiamo lo stesso operatore e non possiamo sfruttare le regole di precedenza, potremmo stabilire che ad avere la priorità potrebbe essere per esempio sempre l'operatore a sinistra, stabilendo così che l'unico [albero sintattico](Grammatiche%20libere%20dal%20contesto.md#^definizione-albero-sintattico) che si può associare correttamente al [prodotto](Grammatiche%20libere%20dal%20contesto.md#^definizione-prodotto-di-un-albero-sintattico) $1+2+3$ è il primo, quello in cui viene interpretato come $(1+2)+3$.
> 
> Possiamo quindi provare a eliminare questa [ambiguità](Grammatiche%20libere%20dal%20contesto.md#^definizione-grammatica-ambigua) introducendo una nuova regola, in base alla quale andremo a creare una nuova [grammatica](Grammatiche%20libere%20dal%20contesto.md#^definizione-grammatica-libera-dal-contesto) **non** [ambigua](Grammatiche%20libere%20dal%20contesto.md#^definizione-grammatica-ambigua): per generare una addizione all'interno di una moltiplicazione, vanno necessariamente usate le parentesi $()$.
> 
> Definiamo quindi la nuova [grammatica](Grammatiche%20libere%20dal%20contesto.md#^definizione-grammatica-libera-dal-contesto)
> 
> $$
> \mathcal{G}' = \langle \{ A,M,O \}, \{ 0,1,\ldots,9,+,*,(,) \}, P, A \rangle 
> $$
> 
> in cui $P$ è l'[insieme](Teoria%20degli%20insiemi.md#^definizione-insieme) delle [produzioni](Grammatiche%20libere%20dal%20contesto.md#^definizione-grammatica-libera-dal-contesto)
> 
> $$
> \begin{align*}
> A &\to M \mid A + M \\
> M &\to O \mid M * O \\
> O &\to 0 \mid 1 \mid \ldots \mid 9 \mid (A)
> \end{align*}
> $$
> 
> e le [variabili](Grammatiche%20libere%20dal%20contesto.md#^definizione-grammatica-libera-dal-contesto) corrispondono a:
> - $A$: espressioni additive,
> - $M$: espressioni moltiplicative e
> - $O$: espressioni atomiche (in cui compaiono solo le costanti numeriche o vengono aggiunte le parentesi $()$).
> 
> %% 
> colorare frecce $\Rightarrow$ e frecce dell'albero sintattico corrispondenti (color coding)
> %%
> 
> Abbiamo quindi che questa nuova [grammatica](Grammatiche%20libere%20dal%20contesto.md#^definizione-grammatica-libera-dal-contesto) $\mathcal{G}'$ potrebbe produrre per esempio le seguenti [derivazioni](Grammatiche%20libere%20dal%20contesto.md#^definizione-derivazione-in-un-passo):
> 
> $$
> \begin{align*}
> A &\Rightarrow M \\
> &\Rightarrow M * O \\
> &\Rightarrow O * O \\
> &\Rightarrow (A) * O \\
> &\Rightarrow (A + M) * O \\
> &\Rightarrow (M + M) * O \\
> &\Rightarrow (O + M) * O \\
> &\Rightarrow (1 + M) * O \\
> &\Rightarrow (1 + O) * O \\
> &\Rightarrow (1 + 2) * O \\
> &\Rightarrow (1 + 2) * 3 \\
> \end{align*}
> $$
> 
> il cui [albero sintattico](Grammatiche%20libere%20dal%20contesto.md#^definizione-albero-sintattico) è
> 
> ![eliminazione-delle-ambiguita-3.drawio](eliminazione-delle-ambiguita-3.drawio.svg)
> 
> Possiamo osservare come, in questa [grammatica](Grammatiche%20libere%20dal%20contesto.md#^definizione-grammatica-libera-dal-contesto) $\mathcal{G}'$, l'espressione la cui struttura comporta il calcolo della somma prima della moltiplicazione è generabile solo con parentesi.

Esistono però [linguaggi](Teoria%20dei%20linguaggi%20formali.md#^definizione-linguaggio-formale) che possono essere [generati](Grammatiche%20libere%20dal%20contesto.md#^definizione-linguaggio-generato-da-una-grammatica-libera) unicamente da [grammatiche ambigue](Grammatiche%20libere%20dal%20contesto.md#^definizione-grammatica-ambigua), i cosiddetti [_linguaggi inerentemente ambigui_](Grammatiche%20libere%20dal%20contesto.md#^definizione-linguaggio-inerentemente-ambiguo).

> [!definizione]+ Definizione: linguaggio inerentemente ambiguo
> 
> Un [linguaggio](Teoria%20dei%20linguaggi%20formali.md#^definizione-linguaggio-formale) $L$ si dice **inerentemente ambiguo** se può essere [generato](Grammatiche%20libere%20dal%20contesto.md#^definizione-linguaggio-generato-da-una-grammatica-libera) unicamente da [grammatiche ambigue](Grammatiche%20libere%20dal%20contesto.md#^definizione-grammatica-ambigua).
^definizione-linguaggio-inerentemente-ambiguo

> [!esempio]- Esempio di linguaggio inerentemente ambiguo
> 
> Un esempio di [linguaggio inerentemente ambiguo](Grammatiche%20libere%20dal%20contesto.md#^definizione-linguaggio-inerentemente-ambiguo) è il [linguaggio](Teoria%20dei%20linguaggi%20formali.md#^definizione-linguaggio-formale)
> 
> $$
> L = \{ \text{a}^n\text{b}^n\text{c}^m\text{d}^m \mid n \ge 1 \land m \ge 1 \} \cup \{ \text{a}^n\text{b}^m\text{c}^m\text{d}^n \mid n \ge 1 \land m \ge 1 \}
> $$
> 
> perché, a prescindere dal tipo di [grammatica](Grammatiche%20libere%20dal%20contesto.md#^definizione-grammatica-libera-dal-contesto) che [genera](Grammatiche%20libere%20dal%20contesto.md#^definizione-linguaggio-generato-da-una-grammatica-libera) $L$, ci saranno sempre almeno due [derivazioni canoniche](Grammatiche%20libere%20dal%20contesto.md#^definizione-derivazione-canonica-a-sinistra-e-a-destra) distinte che [genereranno](Grammatiche%20libere%20dal%20contesto.md#^definizione-linguaggio-generato-da-una-grammatica-libera) una [stringa](Teoria%20dei%20linguaggi%20formali.md#^definizione-stringa) della forma $\text{a}^n\text{b}^n\text{c}^n\text{d}^n$.
> 
> Per esempio, la [grammatica](Grammatiche%20libere%20dal%20contesto.md#^definizione-grammatica-libera-dal-contesto)
> 
> $$
> \mathcal{G} = \langle \{ S,A,B,C,D \}, \{ \text{a},\text{b},\text{c},\text{d} \}, P, S \rangle 
> $$
> 
> in cui $P$ è l'[insieme](Teoria%20degli%20insiemi.md#^definizione-insieme) delle [produzioni](Grammatiche%20libere%20dal%20contesto.md#^definizione-grammatica-libera-dal-contesto)
> 
> $$
> \begin{align*}
> S &\to AB \mid C \\
> A &\to \text{a}A\text{b} \mid \text{ab} \\
> B &\to \text{c}B\text{d} \mid \text{cd} \\
> C &\to \text{a}C\text{d} \mid \text{a}D\text{d} \\
> D &\to \text{b}D\text{c} \mid \text{bc}
> \end{align*}
> $$
> 
> e da cui possiamo ottenere il [prodotto](Grammatiche%20libere%20dal%20contesto.md#^definizione-prodotto-di-un-albero-sintattico) $\text{aabbccdd}$ sia dalla [derivazione canonica](Grammatiche%20libere%20dal%20contesto.md#^definizione-derivazione-canonica-a-sinistra-e-a-destra)
> 
> $$
> \begin{align*}
> S &\Rightarrow_\text{lm} AB \\
> &\Rightarrow_\text{lm} \text{a}A\text{b}B \\
> &\Rightarrow_\text{lm} \text{aabb}B \\
> &\Rightarrow_\text{lm} \text{aabbc}B\text{d} \\
> &\Rightarrow_\text{lm} \text{aabbccdd}
> \end{align*}
> $$
> 
> sia dalla [derivazione canonica](Grammatiche%20libere%20dal%20contesto.md#^definizione-derivazione-canonica-a-sinistra-e-a-destra)
> 
> $$
> \begin{align*}
> S &\Rightarrow_\text{lm} C \\
> &\Rightarrow_\text{lm} \text{a}C\text{d} \\
> &\Rightarrow_\text{lm} \text{aa}D\text{dd} \\
> &\Rightarrow_\text{lm} \text{aab}D\text{cdd} \\
> &\Rightarrow_\text{lm} \text{aabbccdd}
> \end{align*}
> $$

%%
Esercizio:
data la grammatica

$$
B \to \text{T} \mid \text{F} \mid B \land B \mid B \lor B \mid \lnot B \mid (B) 
$$

delle espressioni booleane, risolvere i seguenti esercizi:
1. Modificare la grammatica per eliminare l'ambiguità, dando ai connettivi la precedenza $\lor < \land < \lnot$ e l'associatività a destra per $\lor$ e $\land$
2.  Usando la grammatica non ambigua ottenuta, mostrare le derivazioni a sinistra, a destra e gli alberi sintattici relativi alle espressioni $\text{T} \land \text{F} \lor \text{T}$ e $\lnot\text{T} \land \text{F}$
%%

---

> [!fonti]+ Fonti
> 
> - 🏫 Corso di Laurea in Informatica (`L-31 R`) presso l'Università di Torino:
>     - Corso di _Linguaggi Formali e Traduttori_ (`INF0344`), A.A. 2026-27 ([pagina Moodle](https://informatica.i-learn.unito.it/course/view.php?id=3735)):
> 		- Prof. Jeremy James Sproston, slide del corso:
> 			- [3.1 - _Grammatiche libere dal contesto_](https://informatica.i-learn.unito.it/pluginfile.php/518900/mod_folder/content/0/3-1_cfg.pdf).
> 			- [3.2 - _Alberi sintattici, derivazioni canoniche e ambiguità_](https://informatica.i-learn.unito.it/pluginfile.php/518900/mod_folder/content/0/3-2_alberi.pdf).
> 			- [3.3 - _Eliminazione dell'ambiguità_](https://informatica.i-learn.unito.it/pluginfile.php/518900/mod_folder/content/0/3-3_elim_amb.pdf).
