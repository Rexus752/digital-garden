---
aliases:
  - Automi a pila
---

> [!premessa]+ Premessa
> 
> Ciao! Se è la prima volta che capiti su questo sito, ti consiglio di consultare la [pagina principale](index.md) di questo _Giardino Digitale_ per scoprire meglio cos'è e come navigarlo.
> 
> Lo stato di questa nota è al momento: 🔴 <font color="#FF7F7F">_Bozza_</font>.

---

Facciamo un riassunto di quel che abbiamo visto finora:
- Per i [linguaggi regolari](Espressioni%20regolari.md#^definizione-linguaggio-regolare), abbiamo visto che gli automi%% Link %% ([DFA](Teoria%20degli%20automi.md#^definizione-automa-a-stati-finiti-deterministico-dfa), [NFA](Teoria%20degli%20automi.md#^definizione-automa-a-stati-finiti-non-deterministico-nfa) ed [$\varepsilon$-NFA](Teoria%20degli%20automi.md#^definizione-automa-a-stati-finiti-non-deterministico-con-e-transizioni-enfa)) forniscono un _approccio riconoscitivo_%% link %% per la loro descrizione, mentre le [espressioni regolari](Espressioni%20regolari.md#^definizione-espressione-regolare-regex) forniscono un _approccio generativo_%% Link %%.
- Per i [linguaggi liberi](Grammatiche%20libere%20dal%20contesto.md#^definizione-linguaggio-libero), abbiamo visto che le [grammatiche libere](Grammatiche%20libere%20dal%20contesto.md#^definizione-grammatica-libera-dal-contesto) forniscono un _approccio generativo_%% link %% per la loro descrizione.

|                                       | **[Linguaggi regolari](Espressioni%20regolari.md#^definizione-linguaggio-regolare)**                                                                                                                                                                                                                                                    | **[Linguaggi liberi](Grammatiche%20libere%20dal%20contesto.md#^definizione-linguaggio-libero)**            |
| ------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- |
| **Approccio riconoscitivo%% Link %%** | Automi%% Link %% ([DFA](Teoria%20degli%20automi.md#^definizione-automa-a-stati-finiti-deterministico-dfa), [NFA](Teoria%20degli%20automi.md#^definizione-automa-a-stati-finiti-non-deterministico-nfa) ed [$\varepsilon$-NFA](Teoria%20degli%20automi.md#^definizione-automa-a-stati-finiti-non-deterministico-con-e-transizioni-enfa)) | ???                                                                                                        |
| **Approccio generativo%% link %%**    | [Espressioni regolari](Espressioni%20regolari.md#^definizione-espressione-regolare-regex)                                                                                                                                                                                                                                               | [Grammatiche libere](Grammatiche%20libere%20dal%20contesto.md#^definizione-grammatica-libera-dal-contesto) |

Ebbene, quel che ci manca ora è trovare un approccio riconoscitivo%% Link %% per i [linguaggi liberi](Grammatiche%20libere%20dal%20contesto.md#^definizione-linguaggio-libero): ecco che qui entrano in gioco gli _automi a pila_.

L'idea di base è, essenzialmente, creare una pila LIFO%% link %% di [simboli](Teoria%20dei%20linguaggi%20formali.md#^definizione-simbolo) che si possono aggiungere con un _push_%% link %% e levare con un _pop_%% link %% e verificare se la pila%% Link %% è completamente vuota alla fine della lettura della [stringa](Teoria%20dei%20linguaggi%20formali.md#^definizione-stringa).

[!definizione]+ Definizione: automa a pila (PDA)

Un **automa a pila** (**PDA**, dall'inglese _**P**ush **D**own **A**utomaton_) è una [settupla](Teoria%20degli%20insiemi.md#^definizione-tupla)

$$
\mathcal{P} = \langle Q, \Sigma, \delta, q_0, F \rangle
$$

dove:
- $Q = \{ q_0, q_1, \ldots, q_m \}$ è un insieme finito%% link %% di **stati**,
- $\delta \colon Q \times \Sigma \to Q$ è una [funzione](Funzioni.md#^definizione-funzione) detta **funzione di transizione fra stati**,
- $\Sigma = \{ a_0, a_1, \ldots, a_n \}$ è un [alfabeto](Teoria%20dei%20linguaggi%20formali.md#^definizione-alfabeto),
- $q_0 \in Q$ è uno stato detto **stato iniziale** e
- $F \subseteq Q$ è un [insieme](Teoria%20degli%20insiemi.md#^definizione-insieme) di stati detti **stati finali**.
^definizione-automa-a-stati-finiti-deterministico-dfa


---

> [!fonti]+ Fonti
> 
> - 🏫 Corso di Laurea in Informatica (`L-31 R`) presso l'Università di Torino:
>     - Corso di _Linguaggi Formali e Traduttori_ (`INF0344`), A.A. 2026-27 ([pagina Moodle](https://informatica.i-learn.unito.it/course/view.php?id=3735)):
> 		- Prof. Jeremy James Sproston, slide del corso:
> 			- [3.4 - _Automi a pila_](https://informatica.i-learn.unito.it/pluginfile.php/518900/mod_folder/content/0/3-4_pda.pdf).
