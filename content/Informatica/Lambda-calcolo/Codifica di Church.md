---
title: Codifica di Church
---

> [!premessa]+ Premessa
> 
> Ciao! Se è la prima volta che capiti su questo sito, ti consiglio di consultare la [pagina principale](index.md) di questo cosiddetto _Giardino Digitale_ per scoprire meglio cos'è e come navigarlo.
> 
> Lo stato di questa nota è al momento: 🟡 <font color="#FFFF7F">_Incompleta_</font>.

---

%% linkare tutto %%

Con l'introduzione a variabili, [astrazioni](Informatica/Lambda-calcolo/_index.md#^definizione-astrazione), [applicazioni](Informatica/Lambda-calcolo/_index.md#^definizione-applicazione), operazioni come la [$\beta$-riduzione](Informatica/Lambda-calcolo/_index.md#^definizione-beta-riduzione) e metodi come il [currying](Informatica/Lambda-calcolo/_index.md#^definizione-currying), abbiamo tutto quel che ci serve per trasformare il [$\lambda$-calcolo](Informatica/Lambda-calcolo/_index.md#^definizione-lambda-calcolo) in un linguaggio di programmazione Turing-completo (tramite l'implementazione di strumenti fondamentali nella programmazione come cicli, tipi di dati basilari e strutture dati più complicate), esattamente come dimostrato nella tesi di Church-Turing.

Per fare ciò, Church ha ideato una sua codifica, la [_codifica di Church_](Codifica%20di%20Church.md#^definizione-codifica-di-church), che permette di esprimere coerentemente (dal punto di vista semantico) tutti i costrutti fondamentali della computazione esclusivamente mediante il [$\lambda$-calcolo](Informatica/Lambda-calcolo/_index.md#^definizione-lambda-calcolo).

> [!definizione]+ Definizione: codifica di Church
> 
> La **codifica di Church** è una rappresentazione formale dei dati e degli operatori all'interno del [$\lambda$-calcolo](Informatica/Lambda-calcolo/_index.md#^definizione-lambda-calcolo), in cui ogni valore e ogni operazione vengono espressi unicamente attraverso [termini](Informatica/Lambda-calcolo/_index.md#^definizione-termine).
^definizione-codifica-di-church

# 1 - Logica booleana e strutture di controllo

Partendo dai classici valori booleani $\text{TRUE}$ e $\text{FALSE}$%% link %%, Church nella sua [codifica](Codifica%20di%20Church.md#^definizione-codifica-di-church) decise di definirli seguendo una semplice regola: presi due valori in input $x$ e $y$ (tramite [currying](Informatica/Lambda-calcolo/_index.md#^definizione-currying)), TRUE restituirà il primo valore ($x$) e FALSE il secondo ($y$):

$$
\begin{array}{}
\text{TRUE} \overset{\text{def}}{=} \lambda x.\lambda y.x \\
\text{FALSE} \overset{\text{def}}{=} \lambda x.\lambda y.y
\end{array}
$$

> [!definizione]+ Definizione: valori booleani nella codifica di Church
> 
> Nella [codifica di Church](Codifica%20di%20Church.md#^definizione-codifica-di-church), i valori booleani _vero_ e _falso_ sono rispettivamente codificati nei [termini](Informatica/Lambda-calcolo/_index.md#^definizione-termine) $\text{TRUE}$ e $\text{FALSE}$ definiti come segue:
> 
> $$
> \begin{array}{}
> \text{TRUE} \overset{\text{def}}{=} \lambda x.\lambda y.x \\
> \text{FALSE} \overset{\text{def}}{=} \lambda x.\lambda y.y
> \end{array}
> $$
^definizione-valori-booleani-nella-codifica-di-church

Questa [definizione di $\text{TRUE}$ e $\text{FALSE}$](Codifica%20di%20Church.md#^definizione-valori-booleani-nella-codifica-di-church) può sembrare completamente arbitraria e senza senso così da sola, ma se codifichiamo un [termine](Informatica/Lambda-calcolo/_index.md#^definizione-termine) $\text{IF}$ (che rappresenta una struttura di controllo%% link %%) come

$$
\text{IF} \overset{\text{def}}{=} \lambda z.z
$$

e [applichiamo](Informatica/Lambda-calcolo/_index.md#^definizione-applicazione) questo [termine](Informatica/Lambda-calcolo/_index.md#^definizione-termine) $\text{IF}$ nel seguente modo:

$$
\text{IF}\ \text{TRUE}\ M\ N
$$

allora possiamo dimostrare che verrà correttamente restituito il [termine](Informatica/Lambda-calcolo/_index.md#^definizione-termine) $M$ e, se calcoliamo invece il risultato di

$$
\text{IF}\ \text{FALSE}\ M\ N
$$

otterremo il [termine](Informatica/Lambda-calcolo/_index.md#^definizione-termine) $N$, esattamente come vorremmo che si comportasse una struttura di controllo.

> [!definizione]+ Definizione: struttura di controllo nella codifica di Church
> 
> Nella [codifica di Church](Codifica%20di%20Church.md#^definizione-codifica-di-church), la struttura di controllo è codificata nel [termine](Informatica/Lambda-calcolo/_index.md#^definizione-termine) $\text{IF}$ definito come segue:
> 
> $$
> \text{IF} \overset{\text{def}}{=} \lambda z.z
> $$
^definizione-struttura-di-controllo-nella-codifica-di-church

Ora verifichiamo formalmente che l'[$\text{IF}$](Codifica%20di%20Church.md#^definizione-struttura-di-controllo-nella-codifica-di-church) si comporta come vorremmo.

> [!proposizione]+ Verifica della correttezza semantica dell'$\text{IF}$
> 
> Sia $\Lambda$ l'[insieme](Matematica/Teoria%20degli%20insiemi/_index.md#^definizione-insieme) di [termini](Informatica/Lambda-calcolo/_index.md#^definizione-termine) del [$\lambda$-calcolo](Informatica/Lambda-calcolo/_index.md#^definizione-lambda-calcolo).
> 
> Dati due [termini](Informatica/Lambda-calcolo/_index.md#^definizione-termine) $M,N \in\Lambda$:
> 
> 1. La [$\lambda$-espressione](Informatica/Lambda-calcolo/_index.md#^definizione-termine) $\text{IF}\ \text{TRUE}\ M\ N$ è [convertibile](Informatica/Lambda-calcolo/_index.md#^definizione-conversione) in $M$:
> 
> 	$$
> 	\text{IF}\ \text{TRUE}\ M\ N \Leftrightarrow M
> 	$$
> 
> 2. La [$\lambda$-espressione](Informatica/Lambda-calcolo/_index.md#^definizione-termine) $\text{IF}\ \text{FALSE}\ M\ N$ è [convertibile](Informatica/Lambda-calcolo/_index.md#^definizione-conversione) in $N$:
> 
> 	$$
> 	\text{IF}\ \text{FALSE}\ M\ N \Leftrightarrow N
> 	$$

%%
[!dimostrazione]- Dimostrazione della correttezza semantica dell'$\text{IF}$

1. Verifichiamo $\text{IF}\ \text{TRUE}\ M\ N \Leftrightarrow M$:

$$
\begin{align*}
\text{IF}\ \text{TRUE}\ M\ N & = (\lambda z.z)\ (\lambda x.\lambda y.x)\ M\ N & \text{definizione di IF e TRUE} \\
& \to_\beta z[(\lambda x.\lambda y.x) / z]\ M\ N & \text{$\beta$-riduzione} \\
& = (\lambda x.\lambda y.x)\ M\ N & \text{sostituzione} \\
& \to_\beta (\lambda y.x)[M / x]\ N & \text{$\beta$-riduzione} \\
& = (\lambda y.M)\ N & \text{sostituzione} \\
& \to_\beta M[N / y] & \text{$\beta$-riduzione} \\
& = M & \text{sostituzione}
\end{align*}
$$

2. Verifichiamo $\text{IF}\ \text{FALSE}\ M\ N \Leftrightarrow N$:
%%

Ovviamente, quando andremo a "programmare" realmente tramite il [$\lambda$-calcolo](Informatica/Lambda-calcolo/_index.md#^definizione-lambda-calcolo), al posto di [$\text{TRUE}$ e $\text{FALSE}$](Codifica%20di%20Church.md#^definizione-valori-booleani-nella-codifica-di-church) ci saranno delle espressioni booleane%% link %% codificate in [$\lambda$-calcolo](Informatica/Lambda-calcolo/_index.md#^definizione-lambda-calcolo) che, appunto, si ridurranno nei valori [$\text{TRUE}$ e $\text{FALSE}$](Codifica%20di%20Church.md#^definizione-valori-booleani-nella-codifica-di-church).

> [!osservazione]+ Osservazione: usare l'$\text{IF}$ in un linguaggio zelante
> 
> Osserviamo cosa succede se proviamo a usare l'[$\text{IF}$](Codifica%20di%20Church.md#^definizione-struttura-di-controllo-nella-codifica-di-church) in un [linguaggio zelante](Informatica/Lambda-calcolo/_index.md#^definizione-ordine-applicativo), ossia usando l'[ordine applicativo](Informatica/Lambda-calcolo/_index.md#^definizione-ordine-applicativo).
> 
> Proviamo per esempio a ridurre la [$\lambda$-espressione](Informatica/Lambda-calcolo/_index.md#^definizione-lambda-calcolo) $\text{IF}\ \text{TRUE}\ M\ N$ usando l'[ordine applicativo](Informatica/Lambda-calcolo/_index.md#^definizione-ordine-applicativo):
> 
> $$
> \begin{align*}
> \text{IF}\ \text{TRUE}\ M\ N & = (\lambda z.z)\ (\lambda x.\lambda y.x)\ M\ N & \text{definizione di IF e TRUE} \\
> & \to_\beta z [(\lambda x.\lambda y.x)\ M\ N / z] & \text{$\beta$-riduzione} \\
> & = (\lambda x.\lambda y.x)\ M\ N & \text{sostituzione} \\
> & \to_\beta (\lambda y.x)[M\ N / x] & \text{$\beta$-riduzione} \\
> & = \lambda y.M\ N & \text{sostituzione}
> \end{align*}
> $$
> 
> Arrivati a questo punto, non possiamo [ridurre](Informatica/Lambda-calcolo/_index.md#^definizione-beta-riduzione) ulteriormente $\lambda y.M\ N$, ottenendo così un [termine](Informatica/Lambda-calcolo/_index.md#^definizione-termine) che, nel concreto, ci serve poco o niente. Ecco perché si preferisce sempre usare l'[ordine normale](Informatica/Lambda-calcolo/_index.md#^definizione-ordine-normale) nell'ambito della [codifica di Church](Codifica%20di%20Church.md#^definizione-codifica-di-church).

## 1.1 - Negazione logica

Avendo codificato i [valori booleani $\text{TRUE}$ e $\text{FALSE}$](Codifica%20di%20Church.md#^definizione-valori-booleani-nella-codifica-di-church) e un [$\text{IF}$](Codifica%20di%20Church.md#^definizione-struttura-di-controllo-nella-codifica-di-church) che si comporta come ci aspetteremmo, ora possiamo creare condizioni booleane più elaborate provando a codificare anche gli operatori booleani.

Per esempio, una semplice negazione logica $\text{NOT}$ potrebbe funzionare così: preso in input un argomento $x$, se ([$\text{IF}$](Codifica%20di%20Church.md#^definizione-struttura-di-controllo-nella-codifica-di-church)) $x$ è vero allora restituisce falso ([FALSE](Codifica%20di%20Church.md#^definizione-valori-booleani-nella-codifica-di-church)), altrimenti restituisce vero ([TRUE](Codifica%20di%20Church.md#^definizione-valori-booleani-nella-codifica-di-church)):

$$
\text{NOT} \overset{\text{def}}{=} \lambda x.\text{IF}\ x\ \text{FALSE}\ \text{TRUE}
$$

> [!definizione]+ Definizione: negazione logica nella codifica di Church
> 
> Nella [codifica di Church](Codifica%20di%20Church.md#^definizione-codifica-di-church), la negazione logica è codificata nel [termine](Informatica/Lambda-calcolo/_index.md#^definizione-termine) $\text{NOT}$ definito come segue:
> 
> $$
> \text{NOT} \overset{\text{def}}{=} \lambda x.\text{IF}\ x\ \text{FALSE}\ \text{TRUE}
> $$
^definizione-negazione-logica-nella-codifica-di-church

Verifichiamo che semanticamente il [$\text{NOT}$](Codifica%20di%20Church.md#^definizione-negazione-logica-nella-codifica-di-church) si comporti come ci aspettiamo.

> [!proposizione]+ Verifica della correttezza semantica del $\color{#FF7F7F} \text{NOT}$
> 
> 1. La [$\lambda$-espressione](Informatica/Lambda-calcolo/_index.md#^definizione-termine) $\text{NOT}\ \text{TRUE}$ è [convertibile](Informatica/Lambda-calcolo/_index.md#^definizione-conversione) in $\text{FALSE}$:
> 
> $$
> % Lambda Calculus environment 
> \text{NOT}\ \text{TRUE} \Leftrightarrow \text{FALSE}
> $$
> 
> 2. La [$\lambda$-espressione](Informatica/Lambda-calcolo/_index.md#^definizione-termine) $\text{NOT}\ \text{FALSE}$ è [convertibile](Informatica/Lambda-calcolo/_index.md#^definizione-conversione) in $\text{TRUE}$:
> 
> $$
> % Lambda Calculus environment 
> \text{NOT}\ \text{FALSE} \Leftrightarrow \text{TRUE}
> $$

## 1.2 - Congiunzione logica

Per la congiunzione logica $\text{AND}$, presi in input due argomenti $x$ e $y$, se ([$\text{IF}$](Codifica%20di%20Church.md#^definizione-struttura-di-controllo-nella-codifica-di-church)) $x$ è vero allora restituisce il valore di $y$ (perché da $y$ dipenderà se l'$\text{AND}$ è vero o falso), altrimenti (essendo già $x$ falso) restituisce il valore falso ([$\text{FALSE}$](Codifica%20di%20Church.md#^definizione-valori-booleani-nella-codifica-di-church)):

$$
\text{AND} \overset{\text{def}}{=} \lambda x.\lambda y.\text{IF}\ x\ y\ \text{FALSE}
$$

> [!definizione]+ Definizione: congiunzione logica nella codifica di Church
> 
> Nella [codifica di Church](Codifica%20di%20Church.md#^definizione-codifica-di-church), la congiunzione logica è codificata nel [termine](Informatica/Lambda-calcolo/_index.md#^definizione-termine) $\text{AND}$ definito come segue:
> 
> $$
> \text{AND} \overset{\text{def}}{=} \lambda x.\lambda y.\text{IF}\ x\ y\ \text{FALSE}
> $$
^definizione-congiunzione-logica-nella-codifica-di-church

> [!proposizione]+ Verifica della correttezza semantica dell'$\text{AND}$
> 
> 1. La [$\lambda$-espressione](Informatica/Lambda-calcolo/_index.md#^definizione-termine) $\text{AND} \ \text{TRUE}\ \text{TRUE}$ è [convertibile](Informatica/Lambda-calcolo/_index.md#^definizione-conversione) in $\text{TRUE}$:
> 
> 	$$
> 	\text{AND}\ \text{TRUE}\ \text{TRUE} \Leftrightarrow \text{TRUE}
> 	$$
> 
> 2. La [$\lambda$-espressione](Informatica/Lambda-calcolo/_index.md#^definizione-termine) $\text{AND} \ \text{TRUE}\ \text{FALSE}$ è [convertibile](Informatica/Lambda-calcolo/_index.md#^definizione-conversione) in $\text{FALSE}$:
> 
> 	$$
> 	\text{AND}\ \text{TRUE}\ \text{FALSE} \Leftrightarrow \text{FALSE}
> 	$$
> 
> 3. La [$\lambda$-espressione](Informatica/Lambda-calcolo/_index.md#^definizione-termine) $\text{AND} \ \text{FALSE}\ \text{TRUE}$ è [convertibile](Informatica/Lambda-calcolo/_index.md#^definizione-conversione) in $\text{FALSE}$:
> 
> 	$$
> 	\text{AND}\ \text{FALSE}\ \text{TRUE} \Leftrightarrow \text{FALSE}
> 	$$
> 
> 4. La [$\lambda$-espressione](Informatica/Lambda-calcolo/_index.md#^definizione-termine) $\text{AND} \ \text{FALSE}\ \text{FALSE}$ è [convertibile](Informatica/Lambda-calcolo/_index.md#^definizione-conversione) in $\text{FALSE}$:
> 
> 	$$
> 	\text{AND}\ \text{FALSE}\ \text{FALSE} \Leftrightarrow \text{FALSE}
> 	$$

%% dimostrazione %%

## 1.3 - Disgiunzione logica

Per la disgiunzione logica $\text{OR}$, presi in input due argomenti $x$ e $y$, se ([$\text{IF}$](Codifica%20di%20Church.md#^definizione-struttura-di-controllo-nella-codifica-di-church)) $x$ è vero allora restituisce vero ($\text{TRUE}$), altrimenti restituisce il valore di $y$ (perché da $y$ dipenderà se l'$\text{OR}$ è vero o falso):

$$
\text{OR} \overset{\text{def}}{=} \lambda x.\lambda y.\text{IF}\ x\ \text{TRUE}\ y
$$

> [!definizione]+ Definizione: disgiunzione logica nella codifica di Church
> 
> Nella [codifica di Church](Codifica%20di%20Church.md#^definizione-codifica-di-church), la disgiunzione logica è codificata nel [termine](Informatica/Lambda-calcolo/_index.md#^definizione-termine) $\text{OR}$ definito come segue:
> 
> $$
> \text{OR} \overset{\text{def}}{=} \lambda x.\lambda y.\text{IF}\ x\ \text{TRUE}\ y
> $$
^definizione-disgiunzione-logica-nella-codifica-di-church

> [!proposizione]+ Verifica della correttezza semantica dell'$\text{OR}$
> 
> 1. La [$\lambda$-espressione](Informatica/Lambda-calcolo/_index.md#^definizione-termine) $\text{OR}\ \text{TRUE}\ \text{TRUE}$ è [convertibile](Informatica/Lambda-calcolo/_index.md#^definizione-conversione) in $\text{TRUE}$:
> 
> 	$$
> 	\text{OR}\ \text{TRUE}\ \text{TRUE} \Leftrightarrow \text{TRUE}
> 	$$
> 
> 2. La [$\lambda$-espressione](Informatica/Lambda-calcolo/_index.md#^definizione-termine) $\text{OR} \ \text{TRUE}\ \text{FALSE}$ è [convertibile](Informatica/Lambda-calcolo/_index.md#^definizione-conversione) in $\text{TRUE}$:
> 
> 	$$
> 	\text{OR}\ \text{TRUE}\ \text{FALSE} \Leftrightarrow \text{TRUE}
> 	$$
> 
> 3. La [$\lambda$-espressione](Informatica/Lambda-calcolo/_index.md#^definizione-termine) $\text{OR} \ \text{FALSE}\ \text{TRUE}$ è [convertibile](Informatica/Lambda-calcolo/_index.md#^definizione-conversione) in $\text{TRUE}$:
> 
> 	$$
> 	\text{OR}\ \text{FALSE}\ \text{TRUE} \Leftrightarrow \text{TRUE}
> 	$$
> 
> 4. La [$\lambda$-espressione](Informatica/Lambda-calcolo/_index.md#^definizione-termine) $\text{OR} \ \text{FALSE}\ \text{FALSE}$ è [convertibile](Informatica/Lambda-calcolo/_index.md#^definizione-conversione) in $\text{FALSE}$:
> 
> 	$$
> 	\text{OR}\ \text{FALSE}\ \text{FALSE} \Leftrightarrow \text{FALSE}
> 	$$

%% 
dimostrazione
%%

# 2 - Coppie di termini

> [!definizione]+ Definizione: coppie nella codifica di Church
> 
> Nella [codifica di Church](Codifica%20di%20Church.md#^definizione-codifica-di-church), le coppie sono codificate nel [termine](Informatica/Lambda-calcolo/_index.md#^definizione-termine) $\text{PAIR}$ definito come segue:
> 
> $$
> \text{PAIR} \overset{\text{def}}{=} \lambda x.\lambda y.\lambda z.z\ x\ y
> $$
> 
> Il primo elemento della coppia è codificato nel [termine](Informatica/Lambda-calcolo/_index.md#^definizione-termine) $\text{FIRST}$ definito come segue:
> 
> $$
> \text{FIRST} \overset{\text{def}}{=} \lambda p.p\ \text{TRUE}
> $$
> 
> Il secondo elemento della coppia è codificato nel [termine](Informatica/Lambda-calcolo/_index.md#^definizione-termine) $\text{SECOND}$ definito come segue:
> 
> $$
> \text{SECOND} \overset{\text{def}}{=} \lambda p.p\ \text{FALSE}
> $$
^definizione-coppie-nella-codifica-di-church

> [!proposizione]+ Verifica della correttezza semantica di PAIR, FIRST e SECOND
> 
> Sia $\Lambda$ l'[insieme](Matematica/Teoria%20degli%20insiemi/_index.md#^definizione-insieme) di [termini](Informatica/Lambda-calcolo/_index.md#^definizione-termine) del [$\lambda$-calcolo](Informatica/Lambda-calcolo/_index.md#^definizione-lambda-calcolo).
> 
> Dati due [termini](Informatica/Lambda-calcolo/_index.md#^definizione-termine) $M, N \in \Lambda$:
> 
> 1. La [$\lambda$-espressione](Informatica/Lambda-calcolo/_index.md#^definizione-termine) $\text{FIRST (PAIR}\ M\ N)$ è [convertibile](Informatica/Lambda-calcolo/_index.md#^definizione-conversione) in $\text{M}$:
> 
> 	$$
> 	\text{FIRST (PAIR}\ M\ N) \Leftrightarrow M
> 	$$
> 
> 2. La [$\lambda$-espressione](Informatica/Lambda-calcolo/_index.md#^definizione-termine) $\text{SECOND (PAIR}\ M\ N)$ è [convertibile](Informatica/Lambda-calcolo/_index.md#^definizione-conversione) in $N$:
> 
> 	$$
> 	\text{SECOND (PAIR}\ M\ N) \Leftrightarrow N
> 	$$

%% 
dimostrazione
%%

# 3 - Numerali di Church

Può sembrare scontato, ma uno strumento importante in ogni linguaggio di programmazione sono i numeri, uno dei tipi di dato più utili in un linguaggio.

Nella sua [codifica](Codifica%20di%20Church.md#^definizione-codifica-di-church),  Alonzo Church ha deciso di rappresentare ogni numero naturale $n$, detto [_numerale di Church_](Codifica%20di%20Church.md#^definizione-numerale-di-church) e rappresentato come $\underline n$, come una funzione che mappa una qualsiasi funzione $f$ alla sua composizione per $n$ volte:

$$
\underline n \colon f \mapsto f^n
$$

Prima di andare avanti, definiamo un attimo più formalmente questa notazione "esponenziale" dell'[applicazione](Informatica/Lambda-calcolo/_index.md#^definizione-applicazione).

> [!definizione]+ Definizione: applicazione esponenziale
> 
> Sia $\Lambda$ l'[insieme](Matematica/Teoria%20degli%20insiemi/_index.md#^definizione-insieme) di [termini](Informatica/Lambda-calcolo/_index.md#^definizione-termine) del [$\lambda$-calcolo](Informatica/Lambda-calcolo/_index.md#^definizione-lambda-calcolo). Dati due [termini](Informatica/Lambda-calcolo/_index.md#^definizione-termine) $M,N \in \Lambda$ e un $k \in \mathbb{N}$, l'**applicazione esponenziale** di $M$ per $k$ volte a $N$, denotata con $M^k\ N$, è definita nel seguente modo:
> 
> $$
> M^k\ N \overset{\text{def}}{=} \underbrace{M\ (M\ (\ldots\ (M\ N)))}_{k\text{ volte}}
> $$
> In particolare:
> 
> $$
> M^0\ N \overset{\text{def}}{=} N
> $$
^definizione-applicazione-esponenziale

Ritornando ai numerali, per un numero naturale%% link %% $n$ qualsiasi, data una funzione $f$ e un parametro $x$, verrà restituito il parametro $x$ su cui viene [applicata](Informatica/Lambda-calcolo/_index.md#^definizione-applicazione) la funzione $f$ per $n$ volte:

$$
f^n\ x = \underbrace{f\ (f\ (\ldots\ (f\ x)))}_{n\text{ volte}}
$$

Possiamo quindi formalmente definire i [numerali di Church](Codifica%20di%20Church.md#^definizione-numerale-di-church).

> [!definizione]+ Definizione: numerale di Church
> 
> Nella [codifica di Church](Codifica%20di%20Church.md#^definizione-codifica-di-church), un **numerale di Church** $\underline n$ è un [termine](Informatica/Lambda-calcolo/_index.md#^definizione-termine) che codifica un numero naturale%% link %% $n$ ed è definito come segue:
> 
> $$
> \underline n \overset{\text{def}}{=} \lambda f.\lambda x.f^n\ x
> $$
^definizione-numerale-di-church

Ecco una breve tabella che riassume il comportamento dei [numerali di Church](Codifica%20di%20Church.md#^definizione-numerale-di-church):

| **Numerale di Church** | Definizione del numerale                                                                                                                   | Utilizzo del numerale                                                                                                                                                        |
| ---------------------- | ------------------------------------------------------------------------------------------------------------------------------------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| $\underline 0$         | $\underline 0 \overset{\text{def}}{=} \lambda f.\lambda x.f^0\ x = \lambda f.\lambda x.x$                                                  | $\underline 0\ f\ x = (\lambda f.\lambda x.x)\ f\ x = x$                                                                                                                     |
| $\underline 1$         | $\underline 1\overset{\text{def}}{=}\lambda f.\lambda x.f^1\ x=\lambda f.\lambda x.f x$                                                    | $\underline 1\ f\ x=(\lambda f.\lambda x.f\ x) f\ x=f\ x$                                                                                                                    |
| $\underline 2$         | $\underline 2\overset{\text{def}}{=}\lambda f.\lambda x.f^2\ x=\lambda f.\lambda x.f\ (f\ x)$                                              | $\underline 2\ f\ x=(\lambda f.\lambda x.f\ (f\ x))\ f\ x=f\ (f\ x)$                                                                                                         |
| $\underline 3$         | $\underline 3\overset{\text{def}}{=}\lambda f.\lambda x.f^3\ x=\lambda f.\lambda x.f\ (f\ (f\ x))$                                         | $\underline 3\ f\ x=\lambda f.\lambda x.f\ (f\ (f\ x))\ f\ x=f\ (f\ (f\ x)$                                                                                                  |
| $\ldots$               | $\ldots$                                                                                                                                   | $\ldots$                                                                                                                                                                     |
| $\underline n$         | $\underline n\overset{\text{def}}{=}\lambda f.\lambda x.f^n\ x=\lambda f.\lambda x.\underbrace{f\ (f\ (\ldots (f\ }_{n \text{ volte}}x)))$ | $\underline n\ f\ x=\lambda f.\lambda x.\lambda f.\lambda x.\underbrace{f\ (f\ (\ldots (f\ }_{n \text{ volte}}x)))\ =\underbrace{f\ (f\ (\ldots (f\ }_{n \text{ volte}}x)))$ |

> [!osservazione]+ Osservazione: numerali di Church come codifica unaria dei numeri naturali
> 
> I [numerali di Church](Codifica%20di%20Church.md#^definizione-numerale-di-church) costituiscono una codifica unaria dei numeri naturali, ossia rappresentano un numero n come n [applicazioni](Informatica/Lambda-calcolo/_index.md#^definizione-applicazione) di una funzione.
> 
> La codifica unaria ha il vantaggio della semplicità concettuale e della chiarezza semantica, ma non è efficiente nei casi pratici per numeri grandi, proprio perché ogni numero è "codificato" con un numero di [applicazioni](Informatica/Lambda-calcolo/_index.md#^definizione-applicazione) proporzionale al valore numerico.

## 3.1 - Successore naturale

Nell'ambito dei [numerali di Church](Codifica%20di%20Church.md#^definizione-numerale-di-church), introduciamo un operatore, $\text{SUCC}$, che ci permette di ottenere il successore di un certo [numerale](Codifica%20di%20Church.md#^definizione-numerale-di-church) $\underline n$ (es. $\text{SUCC}\ \underline 3 = \underline 4$).

Per far ciò, partiamo dalla [definizione del numerale di Church](Codifica%20di%20Church.md#^definizione-numerale-di-church) ($\underline n \overset{\text{def}}{=} \lambda f.\lambda x.f^n\ x$): prendendo in input un [numerale](Codifica%20di%20Church.md#^definizione-numerale-di-church) $a$ ($\lambda a$), gli [applichiamo](Informatica/Lambda-calcolo/_index.md#^definizione-applicazione) un'altra volta ancora $f$:

$$
\lambda a.\lambda f.\lambda x.a\ f\ (f\ x)
$$

> [!definizione]+ Definizione: successore naturale nella codifica di Church
> 
> Nella [codifica di Church](Codifica%20di%20Church.md#^definizione-codifica-di-church), il successore naturale%% link %% è codificato nel [termine](Informatica/Lambda-calcolo/_index.md#^definizione-termine) $\text{SUCC}$ definito come segue:
> 
> $$
> \text{SUCC} \overset{\text{def}}{=} \lambda a.\lambda f.\lambda x.a\ f\ (f\ x)
> $$
^definizione-successore-naturale-nella-codifica-di-church

Ora verifichiamo che [$\text{SUCC}$](Codifica%20di%20Church.md#^definizione-successore-naturale-nella-codifica-di-church), per come l'abbiamo definito, si comporti come vorremmo.

> [!proposizione]+ Verifica della correttezza semantica di $\color{#FF7F7F} \text{SUCC}$
> 
> Dato un [numerale di Church](Codifica%20di%20Church.md#^definizione-numerale-di-church) $\underline n$, vale:
> 
> $$
> \text{SUCC}\ \underline n \Leftrightarrow \underline{n + 1}
> $$

> [!dimostrazione]- Dimostrazione della correttezza semantica di $\color{#7FFF7F} \text{SUCC}$
> 
> SUCC n=($\Lambda$a.$\Lambda$f.$\Lambda$x.a f (f x)) ($\Lambda$f.$\Lambda$x.fn x)\toβ($\Lambda$f.$\Lambda$x.a f (f x))[($\Lambda$f.$\Lambda$x.fn x)/a]=$\Lambda$f.$\Lambda$x.$\Lambda$f.$\Lambda$x.fn x) f (f x)\toβ$\Lambda$f.$\Lambda$x.($\Lambda$x.fn x)[f/f] (f x)=$\Lambda$f.$\Lambda$x.($\Lambda$x.fn x) (f x)\toβ$\Lambda$f.$\Lambda$x.(fn x)[(f x)/x]=$\Lambda$f.$\Lambda$x.fn (f x)=$\Lambda$f.$\Lambda$x.fn+1 x=SUCC n+1definizione di SUCC e del numerale di Church n$\beta$-riduzionesostituzione$\beta$-riduzionesostituzione$\beta$-riduzionesostituzionedefinizione dell'applicazione esponenzialedefinizione del numerale di Church

## 3.2 - Predecessore naturale

Vogliamo ottenere una funzione PRED tale che:

PRED n=n-1

con PRED 0=0.

Prendendo ispirazione da [SUCC](Codifica%20di%20Church.md#^definizione-successore-naturale-nella-codifica-di-church), definito come

SUCC\overset{\text{def}}{=}$\Lambda$a.$\Lambda$f.$\Lambda$x.a f (f x)

possiamo notare che, per calcolare il successoreLINK di un numero naturale, basta aggiungergli un'[applicazione](Informatica/Lambda-calcolo/_index.md#^definizione-applicazione). Viceversa, per calcolare il suo predecessoreLINK, dovremo **togliere** un'[applicazione](Informatica/Lambda-calcolo/_index.md#^definizione-applicazione).

Tuttavia, nel [$\lambda$-calcolo](Informatica/Lambda-calcolo/_index.md#^definizione-lambda-calcolo), non è possibile togliere [applicazioni](Informatica/Lambda-calcolo/_index.md#^definizione-applicazione) a una funzione di Church. Occorre quindi un espediente funzionale.

L'idea di Church è questa: quando [applichiamo](Informatica/Lambda-calcolo/_index.md#^definizione-applicazione) una funzione f per n volte, vogliamo tener traccia non solo dell'ultimo risultato, ma anche del penultimo. Se riuscissimo a costruire una sequenza di coppie

(0,0),(0,1),(1,2),(2,3),...,(n-2,n-1),(n-1,n)

alla fine potremmo restituire il primo elemento della coppia finale per ottenere n-1.

Perciò, costruiamo una funzione "iteratrice" next(x) che parte da x=(0,0) e ad ogni passo aggiorna la coppia in questo modo:

next(x)=(x1second(x),x2succ(second(x)))

Così facendo, la funzione next(x) funzionerà nel seguente modo:

|x|x1=second(x)|x2=succ(second(x))|next(x)=(x1,x2)|
|---|---|---|---|
|(0,0)|second((0,0))=0|succ(second((0,0)))=succ(0)=1|next((0,0))=(0,1)|
|(0,1)|second((0,1))=1|succ(second((0,1)))=succ(1)=2|next((0,1))=(1,2)|
|(1,2)|second((1,2))=2|succ(second((1,2)))=succ(2)=3|next((1,2))=(2,3)|
|(2,3)|second((2,3))=3|succ(second((2,3)))=succ(3)=4|next((2,3))=(3,4)|
|...|...|...|...|
|(n-2,n-1)|second((n-2,n-1))=n-1|succ(second((n-2,n-1)))=succ(n-1)=n|next((n-2,n-1))=(n-1,n)|
|(n-1,n)|second((n-1,n))=n|succ(second((n-1,n)))=succ(n)=n+1|next((n-1,n))=(n,n+1)|

Osserviamo che dopo n passi di next(x), la prima componente (x1) è esattamente n-1 (per n>0).

Nel [$\lambda$-calcolo](Informatica/Lambda-calcolo/_index.md#^definizione-lambda-calcolo) traduciamo questa funzione next(x) come:

NEXT\overset{\text{def}}{=}$\Lambda$p.PAIR (SECOND p) (SUCC (SECOND p))

La nostra [$\lambda$-espressione](Informatica/Lambda-calcolo/_index.md#^definizione-termine) PRED dovrà quindi prendere la prima componente (FIRST) della coppia generata all'n-esima iterazione di NEXT:

PRED\overset{\text{def}}{=}$\Lambda$n.FIRST (n NEXT (PAIR 0 0))

> [!definizione]+ Definizione: predecessore naturale nella codifica di Church
> 
> Nella [codifica di Church](Codifica%20di%20Church.md#^definizione-codifica-di-church), il predecessore naturale è codificato nel [termine](Informatica/Lambda-calcolo/_index.md#^definizione-termine) PRED definito come segue:
> 
> PRED\overset{\text{def}}{=}$\Lambda$n.FIRST (n NEXT (PAIR 0 0))
> 
> dove
> 
> NEXT\overset{\text{def}}{=}$\Lambda$p.PAIR (SECOND p) (SUCC (SECOND p))
^definizione-predecessore-naturale-nella-codifica-di-church

> [!proposizione]+ Verifica della correttezza semantica di PRED
> 
> Dato un [numerale di Church](Codifica%20di%20Church.md#^definizione-numerale-di-church) n:
> 
> 1. Il successore della coppia (n-1,n) è (n,n+1):
> 
> NEXT (PAIR n-1 n)⇔PAIR n n+1
> 
> 1. Il [predecessore](Codifica%20di%20Church.md#^definizione-predecessore-naturale-nella-codifica-di-church) di 0 è 0 e il predecessore di n è n-1:
> 
> PRED n⇔{0n-1n=0n>0

## 3.3 - Addizione

> [!definizione]+ Definizione: addizione nella codifica di Church
> 
> Nella [codifica di Church](Codifica%20di%20Church.md#^definizione-codifica-di-church), l'addizione è codificata nel [termine](Informatica/Lambda-calcolo/_index.md#^definizione-termine) ADD definito come segue:
> 
> ADD\overset{\text{def}}{=}$\Lambda$a.$\Lambda$b.b SUCC a
^definizione-addizione-nella-codifica-di-church

> [!proposizione]+ Verifica della correttezza semantica di ADD
> 
> Dati due [numerali di Church](Codifica%20di%20Church.md#^definizione-numerale-di-church) m e n, vale:
> 
> ADD m n⇔m+n

> [!dimostrazione]- Dimostrazione della correttezza semantica di ADD
> 
> ADD m n=($\Lambda$a.$\Lambda$b.b SUCC a) m n\toβ($\Lambda$b.b SUCC a)[m/a] n=($\Lambda$b.b SUCC m) n\toβ(b SUCC m)[n/b]=n SUCC m=($\Lambda$f.$\Lambda$x.fn x) SUCC m\toβ($\Lambda$x.fn x)[SUCC/f] m=($\Lambda$x.SUCCn x) m\toβ(SUCCn x)[m/x]=SUCCn m=n volteSUCC (SUCC (... (SUCC m)))⇔n volte(((m+1)+1)...)+1=m+ndefinizione di ADD$\beta$-riduzionesostituzione$\beta$-riduzionesosituzionedefinizione dei numerali di Church$\beta$-riduzionesostituzione$\beta$-riduzionesostituzioneapplicazione esponenzialesemantica di SUCCaddizione

## 3.4 - Moltiplicazione

> [!definizione]+ Definizione: moltiplicazione nella codifica di Church
> 
> Nella [codifica di Church](Codifica%20di%20Church.md#^definizione-codifica-di-church), la moltiplicazione è codificata nel [termine](Informatica/Lambda-calcolo/_index.md#^definizione-termine) MUL definito come segue:
> 
> MUL\overset{\text{def}}{=}$\Lambda$a.$\Lambda$b.b (ADD a) 0

## 3.5 - Esponenziazione

> [!definizione]+ Definizione: esponenziazione nella codifica di Church
> 
> Nella [codifica di Church](Codifica%20di%20Church.md#^definizione-codifica-di-church), l'esponenziazione è codificata nel [termine](Informatica/Lambda-calcolo/_index.md#^definizione-termine) EXP definito come segue:
> 
> EXP\overset{\text{def}}{=}$\Lambda$a.$\Lambda$b.b (MUL a) 1

## 3.6 - Test per zero

> [!definizione]+ Definizione: test per zero nella codifica di Church
> 
> Nella [codifica di Church](Codifica%20di%20Church.md#^definizione-codifica-di-church), il test per zero è codificato nel [termine](Informatica/Lambda-calcolo/_index.md#^definizione-termine) ISZERO definito come segue:
> 
> ISZERO\overset{\text{def}}{=}$\Lambda$a.a ($\Lambda$x.FALSE) TRUE
^definizione-test-per-zero-nella-codifica-di-church

> [!proposizione]+ Verifica della correttezza semantica di ISZERO
> 
> Dato un [numerale di Church](Codifica%20di%20Church.md#^definizione-numerale-di-church) n, se n=0 allora ISZERO n restituisce TRUE, altrimenti FALSE:
> 
> ISZERO n⇔{TRUEFALSEn=0n=0

# 4 - Punti fissi e funzioni ricorsive

Ora che abbiamo le operazioni aritmetiche per calcolare con i [numerali di Church](Codifica%20di%20Church.md#^definizione-numerale-di-church), possiamo cimentarci nella codifica di una prima funzione ricorsiva nel [$\lambda$-calcolo](Informatica/Lambda-calcolo/_index.md#^definizione-lambda-calcolo): il fattoriale.

Il fattoriale di un numero naturale n, tradizionalmente, nella sua definizione ricorsiva si esprime come il n moltiplicato per il fattoriale del suo predecessore n-1 (con il fattoriale di 0 uguale a 1):

n!={1n∗(n-1)!n=0n>0

Come primo tentativo, potremmo tradurre questa definizione ricorsiva del fattoriale nella [codifica di Church](Codifica%20di%20Church.md#^definizione-codifica-di-church) così:

FACT\overset{\text{def}}{=}$\Lambda$a.IF (ISZERO a) 1 (MUL a (FACT (PRED a)))

Tuttavia, ciò non ci soddisfa perché il [termine](Informatica/Lambda-calcolo/_index.md#^definizione-termine) FACT compare pure a destra. Proviamo però ad [astrarre](Informatica/Lambda-calcolo/_index.md#^definizione-astrazione) ulteriormente questo [termine](Informatica/Lambda-calcolo/_index.md#^definizione-termine) passandogli il FACT nella sua definizione come argomento:

FACT\overset{\text{def}}{=}($\Lambda$f.$\Lambda$a.IF (ISZERO a) 1 (MUL a (f (PRED a)))) FACT

(Ovviamente possiamo notare che, tramite un semplice passaggio di [$\beta$-riduzione](Informatica/Lambda-calcolo/_index.md#^definizione-beta-riduzione), [sostituiamo](Informatica/Lambda-calcolo/_index.md#^definizione-sostituzione) f con FACT e torniamo alla situazione iniziale.)

Assegniamo momentaneamente al [termine](Informatica/Lambda-calcolo/_index.md#^definizione-termine) "ausiliare" AUX tutto quell'ambaradan a cui va poi [applicato](Informatica/Lambda-calcolo/_index.md#^definizione-applicazione) ricorsivamente FACT:

AUX\overset{\text{def}}{=}$\Lambda$f.$\Lambda$a.IF (ISZERO a) 1 (MUL a (f (PRED a)))

In qualche modo, una definizione "accettabile" del fattoriale che vogliamo ottenere avrà una forma del tipo:

FACT\overset{\text{def}}{=}AUX AUX AUX ...

Ma a noi serve avere una definizione **finita** per poter operare con questo [termine](Informatica/Lambda-calcolo/_index.md#^definizione-termine) e ottenere il risultato che vogliamo. È per questo che ci torna utile il concetto di punto fisso di una funzione che ci permetterà di definirla in maniera finita.

Non preoccuparti, a breve sarà tutto più chiaro, ma intanto beccati questa definizione di un punto fisso nel [$\lambda$-calcolo](Informatica/Lambda-calcolo/_index.md#^definizione-lambda-calcolo) espresso mediante questo particolare [combinatore](Informatica/Lambda-calcolo/_index.md#^definizione-combinatore) scoperto da Haskell Curry: il _combinatore di punto fisso_%% link %%.

> [!definizione]+ Definizione: combinatore di punto fisso $\text Y$
> 
> Il **combinatore di punto fisso** (anche detto **combinatore di Curry** perché scoperto da Haskell Curry) Y è un [combinatore](Informatica/Lambda-calcolo/_index.md#^definizione-combinatore) definito nel seguente modo:
> 
> Y\overset{\text{def}}{=}$\Lambda$f.($\Lambda$x.f(x x)) ($\Lambda$x.f(x x))
^definizione-combinatore-di-punto-fisso-y

Possiamo dimostrare che questo [combinatore di punto fisso $\text Y$](Codifica%20di%20Church.md#^definizione-combinatore-di-punto-fisso-y) si comporta semanticamente proprio come un punto fisso.

> [!proposizione]+ Verifica della correttezza semantica del combinatore di punto fisso $\text Y$
> 
> Sia $\Lambda$ l'[insieme](Matematica/Teoria%20degli%20insiemi/_index.md#^definizione-insieme) di [termini](Informatica/Lambda-calcolo/_index.md#^definizione-termine) del [$\lambda$-calcolo](Informatica/Lambda-calcolo/_index.md#^definizione-lambda-calcolo).
> 
> Dato un [termine](Informatica/Lambda-calcolo/_index.md#^definizione-termine) M\in$\Lambda$, vale:
> 
> Y M=M (Y M)

## 4.1 - Fattoriale

Il [combinatore di punto fisso Y](Codifica%20di%20Church.md#^definizione-combinatore-di-punto-fisso-y) è uno strumento molto potente: ci permette, infatti, di implementare il concetto di _ricorsione_ in un linguaggio, quello del [$\lambda$-calcolo](Informatica/Lambda-calcolo/_index.md#^definizione-lambda-calcolo), che formalmente non ce l'ha.

Ciò infatti è possibile perché, ogni [termine](Informatica/Lambda-calcolo/_index.md#^definizione-termine) M a cui viene [applicato](Informatica/Lambda-calcolo/_index.md#^definizione-applicazione) il [combinatore di punto fisso Y](Codifica%20di%20Church.md#^definizione-combinatore-di-punto-fisso-y), diventa a sua volta l'argomento della [$\lambda$-espressione](Informatica/Lambda-calcolo/_index.md#^definizione-lambda-calcolo) di partenza:

Y M=M (Y M)=M (M (Y M))=M (M (M (Y M)))=...

Riprendendo quel [termine](Informatica/Lambda-calcolo/_index.md#^definizione-termine) "ausiliare" di prima, che abbiamo espresso come

AUX\overset{\text{def}}{=}$\Lambda$f.$\Lambda$a.IF (ISZERO a) 1 (MUL a (f (PRED a)))

possiamo renderci ora conto che, passandogli come argomento al posto della f il [combinatore di punto fisso Y](Codifica%20di%20Church.md#^definizione-combinatore-di-punto-fisso-y), ci aiuta a definire in maniera finita la funzione fattoriale nel [$\lambda$-calcolo](Informatica/Lambda-calcolo/_index.md#^definizione-lambda-calcolo).

> [!definizione]+ Definizione: fattoriale nella codifica di Church
> 
> Nella [codifica di Church](Codifica%20di%20Church.md#^definizione-codifica-di-church), il fattoriale è codificato nel [termine](Informatica/Lambda-calcolo/_index.md#^definizione-termine) FACT definito come segue:
> 
> FACT\overset{\text{def}}{=}($\Lambda$f.$\Lambda$a.IF (ISZERO a) 1 (MUL a (f (PRED a)))) Y
^definizione-fattoriale-nella-codifica-di-church

Sì, ma siamo sicuri che quella che abbiamo appena scritto non sia una cazzata colossale e che effettivamente la ricorsione funzioni? Verifichiamolo.

> [!proposizione]+ Verifica della ricorsione nel fattoriale nella codifica di Church
> 
> Il [termine FACT](Codifica%20di%20Church.md#^definizione-fattoriale-nella-codifica-di-church) è [convertibile](Informatica/Lambda-calcolo/_index.md#^definizione-conversione) nel seguente modo:
> 
> FACT⇔$\Lambda$a.IF (ISZERO a) 1 (MUL a (FACT (PRED a)))

---

> [!fonti]+ Fonti
> 
> - 🏫 Corso di Laurea in Informatica (`L-31 R`) presso l'Università di Torino:
>     - Corso di _Linguaggi e Paradigmi di Programmazione_, A.A. 2020-21 ([pagina Moodle](https://informatica.i-learn.unito.it/enrol/index.php?id=1987)):
> 		- Prof. Luca Padovani, slide del corso:
> 	        - [_Programmare nel $\lambda$-calcolo_](https://informatica.i-learn.unito.it/pluginfile.php/466461/mod_resource/content/0/lc_codifiche.pdf).
>     - Corso di _Linguaggi e Paradigmi di Programmazione_, A.A. 2025-26 ([pagina Moodle](https://informatica.i-learn.unito.it/course/view.php?id=3475)):
> 		- Prof. Viviana Bono, lezioni del corso.
> - 📹 Eyesomorphic, [_Programming with Math | The Lambda Calculus_](https://www.youtube.com/watch?v=ViPNHMSUcog) su YouTube.
> - 🌐 [_Lambda-calcolo_](https://it.wikipedia.org/wiki/Lambda_calcolo) su Wikipedia in lingua italiana, [archiviato sulla Wayback Machine](https://web.archive.org/web/20251125013725/https://it.wikipedia.org/wiki/Lambda_calcolo) in data 25 novembre 2025.
> - 🌐 [_Simply typed lambda calculus_](https://en.wikipedia.org/wiki/Simply_typed_lambda_calculus) su Wikipedia in lingua inglese, [archiviato sulla Wayback Machine](https://web.archive.org/web/20251125013806/https://en.wikipedia.org/wiki/Simply_typed_lambda_calculus) in data 25 novembre 2025.
