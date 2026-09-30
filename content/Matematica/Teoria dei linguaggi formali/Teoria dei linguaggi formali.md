---
aliases:
  - Teoria dei linguaggi formali
---

> [!premessa]+ Premessa
> 
> Ciao! Se è la prima volta che capiti su questo sito, ti consiglio di consultare la [pagina principale](index.md) di questo cosiddetto _Giardino Digitale_ per scoprire meglio cos'è e come navigarlo.
> 
> Lo stato di questa nota è al momento: 🔴 <font color="#FF7F7F">_Bozza_</font>.

%% 
https://it.wikipedia.org/wiki/Teoria_dei_linguaggi_formali
%%

---

%% 
Introduzione: spiegare come esistono linguaggi "artificiali" (?) contrapposti a quelli naturali, tra questi ci sono i linguaggi formali
%%

Quando pensiamo alla parola _linguaggio_, pensiamo normalmente a qualcosa che serve agli esseri umani per comunicare: l'italiano, l'inglese o la lingua dei segni%% link %%. Un _linguaggio_ è quindi un sistema che ci permette di costruire espressioni e di attribuire loro un significato.

Ma cosa succede se vogliamo studiare il concetto di _linguaggio_ in modo completamente "astratto" e "[matematico](Matematica.md#^definizione-matematica)", senza preoccuparci del significato delle sue espressioni? È proprio da questa domanda che nasce la [_teoria dei linguaggi formali_](Teoria%20dei%20linguaggi%20formali.md#^definizione-teoria-dei-linguaggi-formali).

Una _lingua naturale_, ossia una di quelle usate nella vita di tutti i giorni (come l'italiano), è estremamente complessa: non comprende soltanto un insieme di parole, ma anche regole grammaticali, eccezioni, ambiguità, contesto, significati impliciti e moltissimi altri fenomeni.

Per esempio, una persona capisce immediatamente che

> Il gatto mangia il topo.

è una frase grammaticalmente ben formata, mentre

> Gatto il topo mangia il.

non lo è. Possiamo quindi chiederci: è possibile descrivere un linguaggio attraverso un insieme preciso di regole, in modo che sia possibile stabilire _meccanicamente_ quali espressioni sono ammesse e quali no?

Un essere umano può leggere una frase e utilizzare la propria conoscenza linguistica per stabilire se abbia senso. Un computer, invece, non possiede intuitivamente il concetto di "frase corretta". Se vogliamo che possa elaborare un linguaggio, dobbiamo fornirgli una descrizione precisa e non ambigua delle sue regole.

%% 
CONTINUARE
%%

> [!definizione] Definizione: teoria dei linguaggi formali
> 
> La **teoria dei linguaggi formali** è un ramo della matematica applicata%% link a "matematica applicata" %% che studia i linguaggi formali%% link %% e le loro proprietà%% link %%, utili in logica%% link %%, [informatica](Informatica.md#^definizione-informatica) e linguistica%% link %%.
^definizione-teoria-dei-linguaggi-formali

[!definizione] Definizione: simbolo

Un **simbolo** (o **carattere**) è un oggetto matematico%% link a "oggetti matematici" %% considerato come un'unità indivisibile.

> [!definizione] Definizione: alfabeto e simboli
> 
> Un **alfabeto**, denotato solitamente con $\Sigma$, è un [insieme](Teoria%20degli%20insiemi.md#^definizione-insieme) finito%% link %% e non [vuoto](Teoria%20degli%20insiemi.md#^definizione-insieme-vuoto) di elementi chiamati **simboli** o **caratteri**.
^definizione-alfabeto

> [!esempio] Esempi di alfabeti
> 
> Ecco un po' di esempi di [alfabeti](Teoria%20dei%20linguaggi%20formali.md#^definizione-alfabeto):
> - $\Sigma_1 = \{ 0,1 \}$ è l'[alfabeto](Teoria%20dei%20linguaggi%20formali.md#^definizione-alfabeto) delle cifre binarie, i cui unici [simboli](Teoria%20dei%20linguaggi%20formali.md#^definizione-alfabeto) sono $0$ e $1$.
> - $\Sigma_2 = \{ 0,1,\ldots,9 \}$ è l'[alfabeto](Teoria%20dei%20linguaggi%20formali.md#^definizione-alfabeto) delle cifre decimali.
> - $\Sigma_3 = \{ \text{a}, \text{b}, \ldots, \text{z}, \text{A}, \text{B}, \ldots, \text{Z} \}$ è l'[alfabeto](Teoria%20dei%20linguaggi%20formali.md#^definizione-alfabeto) latino.
> 
> Ricordiamo che gli [alfabeti](Teoria%20dei%20linguaggi%20formali.md#^definizione-alfabeto) sono a tutti gli effetti degli [insiemi](Teoria%20degli%20insiemi.md#^definizione-insieme), quindi possiamo farci delle operazioni%% link %%, come per esempio l'[unione](Teoria%20degli%20insiemi.md#^definizione-unione-di-due-insiemi). Abbiamo quindi che
> 
> $$
> \begin{align*}
> \Sigma_4 &= \Sigma_2 \cup \{ \text{\ ,\ } \} \\
> &= \{ 0,1,\ldots, 9 \} \cup \{ \text{\ ,\ } \}
> \end{align*}
> $$
> 
> è l'[alfabeto](Teoria%20dei%20linguaggi%20formali.md#^definizione-alfabeto) che possiamo usare per rappresentare i numeri con la virgola, oppure
> 
> $$
> \begin{align*}
> \Sigma_5 &= \Sigma_2 \cup \Sigma_3 \cup \{ \_ \}
> \end{align*}
> $$
> 
> è l'[alfabeto](Teoria%20dei%20linguaggi%20formali.md#^definizione-alfabeto) che possiamo usare per gli identificatori%% link %% in C%% link %%.

Gli [alfabeti](Teoria%20dei%20linguaggi%20formali.md#^definizione-alfabeto) possono essere usati per creare _stringhe_%% link %%.

> [!definizione] Definizione: stringa
> 
> Una **stringa** (o **parola** o **frase**) su un [alfabeto](Teoria%20dei%20linguaggi%20formali.md#^definizione-alfabeto) $\Sigma$ è una sequenza%% link %% finita%% link %% di [simboli](Teoria%20dei%20linguaggi%20formali.md#^definizione-alfabeto) in $\Sigma$.
^definizione-stringa

---

> [!fonti]+ Fonti
> 
> - 🏫 Corso di Laurea in Informatica (`L-31 R`) presso l'Università di Torino:
>     - Corso di _Linguaggi Formali e Traduttori_, A.A. 2026-27 ([pagina Moodle](https://informatica.i-learn.unito.it/course/view.php?id=3735)):
> 		- Prof. Jeremy James Sproston, slide del corso:
> 			- [1.3 - _Linguaggi_](https://informatica.i-learn.unito.it/pluginfile.php/510313/mod_folder/content/0/1-3_linguaggi.pdf).
