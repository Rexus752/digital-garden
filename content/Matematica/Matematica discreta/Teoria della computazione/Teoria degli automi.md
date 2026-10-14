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

> [!definizione]+ Definizione: automa a stati finiti deterministico (DFA)
> 
> Un **automa a stati finiti deterministico** (**DFA**, dall'inglese _**D**eterministic **F**inite-state **A**utomaton_) è una [quintupla](Teoria%20degli%20insiemi.md#^definizione-tupla) $\mathcal{A} = \langle \Sigma, S, \delta, s_0, F \rangle$ dove:
> - $\Sigma = \{ a_0, a_1, \ldots, a_n \}$ è un [alfabeto](Teoria%20dei%20linguaggi%20formali.md#^definizione-alfabeto),
> - $S = \{ s_0, s_1, \ldots, s_m \}$ è un insieme finito%% link %% di stati,
> - $\delta \colon \Sigma \times S \to S$ è una [funzione](Funzioni.md#^definizione-funzione) detta **funzione di transizione fra stati**,
> - $s_0 \in S$ è uno stato%% link %% detto **stato iniziale** e
> - $F \subseteq S$ è un [insieme](Teoria%20degli%20insiemi.md#^definizione-insieme) degli stati finali%% link %%.
> 
> ![definizione-dfa](definizione-dfa.svg)
^definizione-automa-a-stati-finiti-deterministico-dfa

> [!esempio]- Esempio: numero dispari di $\color{#7F7FFF} \text{a}$
> 
> Proviamo a definire un [DFA](Teoria%20degli%20automi.md#^definizione-automa-a-stati-finiti-deterministico-dfa) che riconosce solo le [stringhe](Teoria%20dei%20linguaggi%20formali.md#^definizione-stringa) di $\text{a}$ di [lunghezza](Teoria%20dei%20linguaggi%20formali.md#^definizione-lunghezza-di-una-stringa) dispari.
> 
> Questo [automa](Teoria%20degli%20automi.md#^definizione-automa-a-stati-finiti-deterministico-dfa) $\mathcal{A} = \langle \Sigma, S, \delta, s_0, F \rangle$ sarà così definito:
> - $\Sigma = \{ \text{a} \}$ perché ci servono solo [stringhe](Teoria%20dei%20linguaggi%20formali.md#^definizione-stringa) contenenti il [simbolo](Teoria%20dei%20linguaggi%20formali.md#^definizione-simbolo) $\text{a}$;
> - $S = \{ s_0, s_1 \}$ perché servono solo due stati, uno per quando la [stringa](Teoria%20dei%20linguaggi%20formali.md#^definizione-stringa) sarà di [lunghezza](Teoria%20dei%20linguaggi%20formali.md#^definizione-lunghezza-di-una-stringa) pari e uno per quando sarà di [lunghezza](Teoria%20dei%20linguaggi%20formali.md#^definizione-lunghezza-di-una-stringa) dispari;
> - $\delta \colon \Sigma \times S \to S$ così definita:
> 	- $\delta(\text{a}, s_0) = s_1$ perché quando la [stringa](Teoria%20dei%20linguaggi%20formali.md#^definizione-stringa) sarà di [lunghezza](Teoria%20dei%20linguaggi%20formali.md#^definizione-lunghezza-di-una-stringa) pari ($s_0$) e riceve un $\text{a}$ in input diventa dispari ($s_1$) e, viceversa,
> 	- $\delta(\text{a}, s_1) = s_0$ perché quando la [stringa](Teoria%20dei%20linguaggi%20formali.md#^definizione-stringa) sarà di [lunghezza](Teoria%20dei%20linguaggi%20formali.md#^definizione-lunghezza-di-una-stringa) dispari ($s_1$) e riceve un $\text{a}$ in input diventa pari ($s_0$);
> - $s_0 \in S$ come stato finale%% link %% e
> - $F = \{ s_1 \}$ perché la [stringa](Teoria%20dei%20linguaggi%20formali.md#^definizione-stringa) sarà accettabile solo quando avrà [lunghezza](Teoria%20dei%20linguaggi%20formali.md#^definizione-lunghezza-di-una-stringa) dispari.
> 
> ![esempio-numero-dispari-di-a](esempio-numero-dispari-di-a.svg)

---

> [!fonti]+ Fonti
> 
> - 🏫 Corso di Laurea in Informatica (`L-31 R`) presso l'Università di Torino:
>     - Corso di _Linguaggi Formali e Traduttori_ (`INF0344`), A.A. 2026-27 ([pagina Moodle](https://informatica.i-learn.unito.it/course/view.php?id=3735)):
> 		- Prof. Jeremy James Sproston, slide del corso:
> 			- [2.1 - _DFA_](https://informatica.i-learn.unito.it/pluginfile.php/514089/mod_folder/content/0/2-1_dfa.pdf).
