
> [!premessa]+ Premessa
> 
> Ciao! Se è la prima volta che capiti su questo sito, ti consiglio di consultare la [pagina principale](index.md) di questo cosiddetto _Giardino Digitale_ per scoprire meglio cos'è e come navigarlo.
> 
> Lo stato di questa nota è al momento: 🟡 <font color="#FFFF7F">_Incompleta_</font>

---

%% 
Linkare tutte le "funzioni" citate in tutto il lambda-calcolo alle "funzioni come astrazioni"
%%

Negli anni Venti e Trenta del Novecento, logici e matematici come Hilbert, Gödel, Church e Turing cercavano un modello rigoroso di **"procedura effettiva"** (ossia di algoritmo) per affrontare il cosiddetto **Entscheidungsproblem** (problema della decisione): esiste un metodo meccanico per decidere la verità o falsità di qualunque enunciato matematico?%% spiegare meglio questa roba %%

Per rispondere, occorreva chiarire cosa significhi **calcolare in modo puramente meccanico**: come descrivere formalmente una sequenza di operazioni che, dato un valore iniziale, produca un risultato.

Il matematico statunitense Alonzo Church sviluppò allora un formalismo minimale che prendeva come unica base il concetto di [funzione matematica](Matematica/Teoria%20degli%20insiemi/Funzioni/Funzioni.md#^definizione-funzione), in quanto una [funzione](Matematica/Teoria%20degli%20insiemi/Funzioni/Funzioni.md#^definizione-funzione) può essere rappresentata come un [processo che, dato un certo input, restituisce un certo output](Matematica/Teoria%20degli%20insiemi/Funzioni/Funzioni.md#^osservazione-funzione-come-processo-con-input-e-output). La sua intuizione fu di considerare le [funzioni](Matematica/Teoria%20degli%20insiemi/Funzioni/Funzioni.md#^definizione-funzione) non più soltanto come [relazioni](Matematica/Teoria%20degli%20insiemi/Relazioni%20tra%20insiemi.md#^definizione-relazione-n-aria) immutabili tra [insiemi](Matematica/Teoria%20degli%20insiemi/Teoria%20degli%20insiemi.md#^definizione-teoria-degli-insiemi), ma come oggetti matematici manipolabili, su cui fondare una nuova branca della matematica: ecco quindi la nascita del [$\lambda$-calcolo](Informatica/Lambda-calcolo/Lambda-calcolo.md#^definizione-lambda-calcolo).

> [!definizione]+ Definizione: $\color{#FF7FFF} \lambda$-calcolo
> 
> Il **$\lambda$-calcolo** è un sistema formale formulato a partire dagli anni Trenta dal matematico americano Alonzo Church, sviluppato per esprimere formalmente il procedimento di computazione di una [funzione matematica](Matematica/Teoria%20degli%20insiemi/Funzioni/Funzioni.md#^definizione-funzione) espressa per mezzo di un linguaggio formale i cui [termini](Informatica/Lambda-calcolo/Lambda-calcolo.md#^definizione-termine) possono essere usati per rappresentare calcoli in modo astratto.
^definizione-lambda-calcolo

Il [$\lambda$-calcolo](Informatica/Lambda-calcolo/Lambda-calcolo.md#^definizione-lambda-calcolo) essenzialmente permette di "calcolare" con le [funzioni matematiche](Matematica/Teoria%20degli%20insiemi/Funzioni/Funzioni.md#^definizione-funzione) così come è possibile calcolare normalmente con i numeri: avendo anticipato così il concetto di _linguaggio di programmazione_%% link %% prima dell'avvento stesso dei computer (che arriveranno solo negli anni Quaranta), il [$\lambda$-calcolo](Informatica/Lambda-calcolo/Lambda-calcolo.md#^definizione-lambda-calcolo) viene considerato uno dei primi linguaggi di programmazione%% link %% della storia ma utilizzabile solo "sulla carta" (perché, appunto, non esistevano ancora i computer lol).

Dal [$\lambda$-calcolo](Informatica/Lambda-calcolo/Lambda-calcolo.md#^definizione-lambda-calcolo), inoltre, nasce uno dei primi paradigmi di programmazione%% link %% della storia: quello _funzionale_%% link %%, che prende il nome proprio dal concetto delle [funzioni matematiche](Matematica/Teoria%20degli%20insiemi/Funzioni/Funzioni.md#^definizione-funzione) su cui è costruito.

Per intenderci, guarda questa espressione apparentemente senza senso:

$$
\begin{array}{}
\lambda n.n\ (\lambda f.\lambda a.\lambda x.f\ ((\lambda x.\lambda y.\lambda z.x\ (y\ z))\ a\ x) \\
((\lambda n.\lambda f.\lambda x.f\ (n\ f\ x))\ x))\ (\lambda x.\lambda y.x) \\
(\lambda f.\lambda x.f\ x)\ (\lambda f.\lambda x.f\ x)
\end{array}
$$

Sentiti liber* di crederci o no, ma questa espressione, che chiameremo [_termine_](Informatica/Lambda-calcolo/Lambda-calcolo.md#^definizione-termine), rappresenta il "codice" in [$\lambda$-calcolo](Informatica/Lambda-calcolo/Lambda-calcolo.md#^definizione-lambda-calcolo) per calcolare il fattoriale%% link %% di un numero naturale%% link %% $n$ qualsiasi.

Ma come fa a essere questo ammasso di lettere casuali un codice? Se sei curios* di saperlo, benvenut* nel magico mondo del [$\lambda$-calcolo](Informatica/Lambda-calcolo/Lambda-calcolo.md#^definizione-lambda-calcolo).

(_Attent*! Stai per finire in un rabbit-hole da cui potresti non uscirne più. Io ti ho avvertit*..._)

# 1 - Termini del $\lambda$-calcolo

Prima di arrivare a capire cosa sono gli oggetti principali con cui opera il [$\lambda$-calcolo](Informatica/Lambda-calcolo/Lambda-calcolo.md#^definizione-lambda-calcolo), cioè i [termini](Informatica/Lambda-calcolo/Lambda-calcolo.md#^definizione-termine), vediamo come sono nati.

## 1.1 - Astrazioni

Durante il processo di definizione del [$\lambda$-calcolo](Informatica/Lambda-calcolo/Lambda-calcolo.md#^definizione-lambda-calcolo), Alonzo Church decise in primis di modificare la notazione classica della definizione di una [funzione](Matematica/Teoria%20degli%20insiemi/Funzioni/Funzioni.md#^definizione-funzione):

$$
\begin{align*}
f \colon & A \to B \\
& a \mapsto b
\end{align*}
$$

Il signor Church, per rendere la notazione più scorrevole e, soprattutto, il più astratta possibile (in modo da poterci fare operazioni più comodamente), scelse di evitare di indicare per ogni [funzione](Matematica/Teoria%20degli%20insiemi/Funzioni/Funzioni.md#^definizione-funzione) il suo nome (in questo caso $f$) e gli [insiemi](Matematica/Teoria%20degli%20insiemi/Teoria%20degli%20insiemi.md#^definizione-insieme) posti in [relazione](Matematica/Teoria%20degli%20insiemi/Relazioni%20tra%20insiemi.md#^definizione-relazione-n-aria) ($A$ e $B$), valorizzando in particolare proprio la trasformazione che avviene grazie alla [funzione](Matematica/Teoria%20degli%20insiemi/Funzioni/Funzioni.md#^definizione-funzione) ($a \mapsto b$).

La nuova notazione di Church rappresenta le [funzioni](Matematica/Teoria%20degli%20insiemi/Funzioni/Funzioni.md#^definizione-funzione) introducendole con un $\lambda$ (da qui il nome del [$\lambda$-calcolo](Informatica/Lambda-calcolo/Lambda-calcolo.md#^definizione-lambda-calcolo)) per indicare l'inizio della definizione di una [funzione](Matematica/Teoria%20degli%20insiemi/Funzioni/Funzioni.md#^definizione-funzione), seguito dalle due variabili separate da un punto:

$$
\lambda a.b
$$

Questo modo di definire "astrattamente" una [funzione](Matematica/Teoria%20degli%20insiemi/Funzioni/Funzioni.md#^definizione-funzione) viene detto [_astrazione_](Informatica/Lambda-calcolo/Lambda-calcolo.md#^definizione-astrazione).

> [!definizione]+ Definizione: astrazione
> 
> Nel [$\lambda$-calcolo](Informatica/Lambda-calcolo/Lambda-calcolo.md#^definizione-lambda-calcolo), un'**astrazione** (anche detta **$\lambda$-astrazione** o, nell'ambito del [$\lambda$-calcolo](Informatica/Lambda-calcolo/Lambda-calcolo.md#^definizione-lambda-calcolo), chiamata anche semplicemente **funzione**) è una definizione di una [funzione](Matematica/Teoria%20degli%20insiemi/Funzioni/Funzioni.md#^definizione-funzione) anonima, cioè una funzione che non ha un nome ma è identificata direttamente dalla sua regola di trasformazione.
> 
> Un'**astrazione** ha la forma:
> 
> $$
> \lambda x.M
> $$
> 
> dove:
> 
> - $x$ è una variabile%% link %% che rappresenta l'argomento%% link %% della [funzione](Matematica/Teoria%20degli%20insiemi/Funzioni/Funzioni.md#^definizione-funzione) e
> - $M$ è un [termine](Informatica/Lambda-calcolo/Lambda-calcolo.md#^definizione-termine) del [$\lambda$-calcolo](Informatica/Lambda-calcolo/Lambda-calcolo.md#^definizione-lambda-calcolo) che rappresenta il corpo%% link %% della [funzione](Matematica/Teoria%20degli%20insiemi/Funzioni/Funzioni.md#^definizione-funzione).
^definizione-astrazione

> [!osservazione]+ Osservazione: $\color{#7F7F7F} \lambda x.M \equiv M(x)$
> 
> La notazione
> 
> $$
> \lambda x.M
> $$
> 
> di un'[astrazione](Informatica/Lambda-calcolo/Lambda-calcolo.md#^definizione-astrazione) equivale alla notazione classica di una [funzione](Matematica/Teoria%20degli%20insiemi/Funzioni/Funzioni.md) qualsiasi con argomento%% link %% $x$ e corpo%% link %% $M$:
> 
> $$
> M(x)
> $$
> 
> Cioè:
> 
> $$
> \lambda x.M \equiv M(x)
> $$

## 1.2 - Applicazioni

Con l'[astrazione](Informatica/Lambda-calcolo/Lambda-calcolo.md#^definizione-astrazione) abbiamo capito come possiamo definire una [funzione](Matematica/Teoria%20degli%20insiemi/Funzioni/Funzioni.md#^definizione-funzione) e il suo comportamento, ma concretamente come facciamo a "utilizzarla" dandole in input un certo numero?

Il mitico Alonzo%% link %% decise di adottare quindi la seguente notazione: presa un'[astrazione](Informatica/Lambda-calcolo/Lambda-calcolo.md#^definizione-astrazione) $\lambda x.M$, questa viene posta tra parentesi tonde e viene seguita dal numero $n$ che vogliamo sostituire all'argomento dell'[astrazione](Informatica/Lambda-calcolo/Lambda-calcolo.md#^definizione-astrazione):

$$
(\lambda x.M)\ n
$$

Per esempio, data un'[astrazione](Informatica/Lambda-calcolo/Lambda-calcolo.md#^definizione-astrazione) $\lambda x.M$ dove $M$ indica la somma di $1$ a $x$ (quindi $x+1$) e $n$ è uguale a $3$, potremmo scrivere (seppur effettuando in questo caso un abuso di notazione, perché nel [$\lambda$-calcolo](Informatica/Lambda-calcolo/Lambda-calcolo.md#^definizione-lambda-calcolo) non è possibile usare direttamente i numeri in questo modo):

$$
(\lambda x.x+1)\ 3
$$

Ciò ci indica che, alla variabile di input $x$ che rappresenta l'argomento dell'[astrazione](Informatica/Lambda-calcolo/Lambda-calcolo.md#^definizione-astrazione), noi dobbiamo sostituire il numero $3$, in modo da ottenere come risultato $4$: a questa notazione Church diede il nome di [_applicazione_](Informatica/Lambda-calcolo/Lambda-calcolo.md#^definizione-applicazione).

> [!definizione]+ Definizione: applicazione
> 
> Nel [$\lambda$-calcolo](Informatica/Lambda-calcolo/Lambda-calcolo.md#^definizione-lambda-calcolo), un'**applicazione** (anche detta **$\lambda$-applicazione**) è l'operazione che consiste nell'utilizzare una [funzione](Informatica/Lambda-calcolo/Lambda-calcolo.md#^definizione-astrazione) su un argomento.
> 
> Un'**applicazione** ha la forma:
> 
> $$
> (M\ N)
> $$
> 
> dove:
> 
> - $M$ è un'espressione del [$\lambda$-calcolo](Informatica/Lambda-calcolo/Lambda-calcolo.md#^definizione-lambda-calcolo) che rappresenta una [funzione](Informatica/Lambda-calcolo/Lambda-calcolo.md#^definizione-astrazione) e
> - $N$ è un'espressione del [$\lambda$-calcolo](Informatica/Lambda-calcolo/Lambda-calcolo.md#^definizione-lambda-calcolo) che rappresenta l'argomento su cui la [funzione](Informatica/Lambda-calcolo/Lambda-calcolo.md#^definizione-astrazione) viene applicata.
^definizione-applicazione

## 1.3 - Termini

Ora che abbiamo definito cosa sono un'[astrazione](Informatica/Lambda-calcolo/Lambda-calcolo.md#^definizione-astrazione) e un'[applicazione](Informatica/Lambda-calcolo/Lambda-calcolo.md#^definizione-applicazione), potremmo dire che questi due sono gli oggetti fondamentali con cui andremo a operare nel [$\lambda$-calcolo](Informatica/Lambda-calcolo/Lambda-calcolo.md#^definizione-lambda-calcolo): i nostri [_termini_](Informatica/Lambda-calcolo/Lambda-calcolo.md#^definizione-termine), quindi, possono assumere una di queste _forme sintattiche_ possibili tra un'[astrazione](Informatica/Lambda-calcolo/Lambda-calcolo.md#^definizione-astrazione), un'[applicazione](Informatica/Lambda-calcolo/Lambda-calcolo.md#^definizione-applicazione) e una semplice variabile.

> [!definizione]+ Definizione: termine nel $\color{#FF7FFF} \lambda$-calcolo
> 
> Nel [$\lambda$-calcolo](Informatica/Lambda-calcolo/Lambda-calcolo.md#^definizione-lambda-calcolo), un **termine** $T$ (anche detto **$\lambda$-termine** o **$\lambda$-espressione**) è una stringa ben formata a partire dalla seguente grammatica espressa in BNF%% link %%:
> 
> $$
> T ::= x \mid (\lambda x.{\color{#7FFF7F} T }) \mid ({\color{#FF7F7F} T }\ {\color{#7F7FFF} T })
> $$
> 
> dove:
> 
> 1. $x$ è una variabile%%link%%,
> 2. $(\lambda x.{\color{#7FFF7F} T })$ è un'[astrazione](Informatica/Lambda-calcolo/Lambda-calcolo.md#^definizione-astrazione) con argomento $x$ e corpo $\color{#7FFF7F} T$ e
> 3. $({\color{#FF7F7F} T }\ {\color{#7F7FFF} T })$ è un'[applicazione](Informatica/Lambda-calcolo/Lambda-calcolo.md#^definizione-applicazione) in cui la [funzione](Informatica/Lambda-calcolo/Lambda-calcolo.md#^definizione-astrazione) $\color{#FF7F7F} T$ viene applicata all'argomento $\color{#7F7FFF} T$.
> 
> Ognuna di queste 3 forme che può assumere un **termine** è detta **forma sintattica**.
^definizione-termine

> [!esempio]- Esempi di termini
> 
> Ecco qualche esempio di [termini](Informatica/Lambda-calcolo/Lambda-calcolo.md#^definizione-termine) del [$\lambda$-calcolo](Informatica/Lambda-calcolo/Lambda-calcolo.md#^definizione-lambda-calcolo) correttamente espressi:
> 
> - $x$ è un [termine](Informatica/Lambda-calcolo/Lambda-calcolo.md#^definizione-termine) che rappresenta una semplice variabile $x$.
> - $(\lambda x.x)$ è un [termine](Informatica/Lambda-calcolo/Lambda-calcolo.md#^definizione-termine) che rappresenta un'[astrazione](Informatica/Lambda-calcolo/Lambda-calcolo.md#^definizione-astrazione) con argomento $x$ e corpo $x$.
> - ${\color{#FF7F7F} ( } {\color{#7FFF7F} ( } \lambda x.{\color{#7F7FFF} ( } x\ x {\color{#7F7FFF} ) } {\color{#7FFF7F} ) }\ {\color{#FFFF7F} ( }\lambda y.{\color{#7FFFFF} ( }y\ y{\color{#7FFFFF} ) }{\color{#FFFF7F} ) }{\color{#FF7F7F} ) }$ è un [termine](Informatica/Lambda-calcolo/Lambda-calcolo.md#^definizione-termine) che rappresenta un'[applicazione](Informatica/Lambda-calcolo/Lambda-calcolo.md#^definizione-applicazione) della [funzione](Informatica/Lambda-calcolo/Lambda-calcolo.md#^definizione-astrazione) ${\color{#7FFF7F} ( } \lambda x.{\color{#7F7FFF} ( } x\ x {\color{#7F7FFF} ) } {\color{#7FFF7F} ) }$ all'argomento ${\color{#FFFF7F} ( }\lambda y.{\color{#7FFFFF} ( }y\ y{\color{#7FFFFF} ) }{\color{#FFFF7F} ) }$. A loro volta, possiamo analizzare questi "sotto-[termini](Informatica/Lambda-calcolo/Lambda-calcolo.md#^definizione-termine)":
> 	- ${\color{#7FFF7F} ( } \lambda x.{\color{#7F7FFF} ( } x\ x {\color{#7F7FFF} ) } {\color{#7FFF7F} ) }$ è un [termine](Informatica/Lambda-calcolo/Lambda-calcolo.md#^definizione-termine) che rappresenta un'[astrazione](Informatica/Lambda-calcolo/Lambda-calcolo.md#^definizione-astrazione) con argomento $x$ e corpo ${\color{#7F7FFF} ( } x\ x {\color{#7F7FFF} ) }$. A sua volta:
> 		- ${\color{#7F7FFF} ( } x\ x {\color{#7F7FFF} ) }$ è un [termine](Informatica/Lambda-calcolo/Lambda-calcolo.md#^definizione-termine) che rappresenta un'[applicazione](Informatica/Lambda-calcolo/Lambda-calcolo.md#^definizione-applicazione) della [funzione](Informatica/Lambda-calcolo/Lambda-calcolo.md#^definizione-astrazione) $x$ all'argomento $x$.
> 	- ${\color{#FFFF7F} ( }\lambda y.{\color{#7FFFFF} ( }y\ y{\color{#7FFFFF} ) }{\color{#FFFF7F} ) }$ è un [termine](Informatica/Lambda-calcolo/Lambda-calcolo.md#^definizione-termine) che rappresenta un'[astrazione](Informatica/Lambda-calcolo/Lambda-calcolo.md#^definizione-astrazione) con argomento $y$ e corpo ${\color{#7FFFFF} ( }y\ y{\color{#7FFFFF} ) }$. A sua volta:
> 		- ${\color{#7FFFFF} ( }y\ y{\color{#7FFFFF} ) }$ è un [termine](Informatica/Lambda-calcolo/Lambda-calcolo.md#^definizione-termine) che rappresenta un'[applicazione](Informatica/Lambda-calcolo/Lambda-calcolo.md#^definizione-applicazione) della [funzione](Informatica/Lambda-calcolo/Lambda-calcolo.md#^definizione-astrazione) $y$ all'argomento $y$.
> - ${\color{#FFFF7F} ( }\lambda f.{\color{#7F7FFF} ( }\lambda x.{\color{#7FFF7F} ( }f\ {\color{#FF7F7F} ( }f\ x{\color{#FF7F7F} ) }{\color{#7FFF7F} ) }{\color{#7F7FFF} ){\color{#FFFF7F} ) } }$ è un [termine](Informatica/Lambda-calcolo/Lambda-calcolo.md#^definizione-termine) che rappresenta un'[astrazione](Informatica/Lambda-calcolo/Lambda-calcolo.md#^definizione-astrazione) con argomento $f$ e corpo ${\color{#7F7FFF} ( }\lambda x.{\color{#7FFF7F} ( }f\ {\color{#FF7F7F} ( }f\ x{\color{#FF7F7F} ) }{\color{#7FFF7F} ) }{\color{#7F7FFF} ) }$. A sua volta:
>     - ${\color{#7F7FFF} ( }\lambda x.{\color{#7FFF7F} ( }f\ {\color{#FF7F7F} ( }f\ x{\color{#FF7F7F} ) }{\color{#7FFF7F} ) }{\color{#7F7FFF} )}$ è un [termine](Informatica/Lambda-calcolo/Lambda-calcolo.md#^definizione-termine) che rappresenta un'[astrazione](Informatica/Lambda-calcolo/Lambda-calcolo.md#^definizione-astrazione) con argomento $x$ e corpo ${\color{#7FFF7F} ( }f\ {\color{#FF7F7F} ( }f\ x{\color{#FF7F7F} ) }{\color{#7FFF7F} ) }$. A sua volta:
>         - ${\color{#7FFF7F} ( }f\ {\color{#FF7F7F} ( }f\ x{\color{#FF7F7F} ) }{\color{#7FFF7F} ) }$ è un [termine](Informatica/Lambda-calcolo/Lambda-calcolo.md#^definizione-termine) che rappresenta un'[astrazione](Informatica/Lambda-calcolo/Lambda-calcolo.md#^definizione-astrazione) con argomento $f$ e corpo ${\color{#FF7F7F} ( }f\ x{\color{#FF7F7F} ) }$. A sua volta:
>             - ${\color{#FF7F7F} ( }f\ x{\color{#FF7F7F} ) }$ è un [termine](Informatica/Lambda-calcolo/Lambda-calcolo.md#^definizione-termine) che rappresenta un'[applicazione](Informatica/Lambda-calcolo/Lambda-calcolo.md#^definizione-applicazione) della [funzione](Informatica/Lambda-calcolo/Lambda-calcolo.md#^definizione-astrazione) $f$ all'argomento $x$.

## 1.4 - Riscrittura dei termini

È possibile riscrivere i [termini](Informatica/Lambda-calcolo/Lambda-calcolo.md#^definizione-termine) eliminando alcune parentesi per migliorare la leggibilità.

> [!notazione]+ Notazione: omissione delle parentesi più esterne di un termine
> 
> In un [termine](Informatica/Lambda-calcolo/Lambda-calcolo.md#^definizione-termine) è possibile omettere le parentesi più esterne.
> 
> Per esempio, un [termine](Informatica/Lambda-calcolo/Lambda-calcolo.md#^definizione-termine) $T=(\lambda V.T)$ che rappresenta un'[astrazione](Informatica/Lambda-calcolo/Lambda-calcolo.md#^definizione-astrazione) con argomento%% Link %% $V$ e corpo%% link %% $T$ si può riscrivere come $T=\lambda V.T$:
> 
> $$
> \begin{align*}
> T &= {\color{#FF7F7F} ( }\lambda V.T{\color{#FF7F7F} ) } \\
> &= \lambda V.T
> \end{align*}
> $$
> 
> Allo stesso modo, un [termine](Informatica/Lambda-calcolo/Lambda-calcolo.md#^definizione-termine) $T' = (U\ V)$ che rappresenta un'[applicazione](Informatica/Lambda-calcolo/Lambda-calcolo.md#^definizione-applicazione) della [funzione](Informatica/Lambda-calcolo/Lambda-calcolo.md#^definizione-astrazione) $U$ all'argomento%% link %% $V$ si può riscrivere come $T'=U\ V$:
> 
> $$
> \begin{align*}
> T' &= {\color{#FF7F7F} ( }U\ V{\color{#FF7F7F} ) } \\
> &= U\ V
> \end{align*}
> $$
^notazione-omissione-delle-parentesi-piu-esterne-di-un-termine

> [!notazione]+ Notazione: omissione delle parentesi in un'astrazione
> 
> In un [termine](Informatica/Lambda-calcolo/Lambda-calcolo.md#^definizione-termine) $T=\lambda V.T'$ che rappresenta un'[astrazione](Informatica/Lambda-calcolo/Lambda-calcolo.md#^definizione-astrazione) con argomento $V$ e corpo $T$ si possono eliminare le parentesi più esterne del sotto-[termine](Informatica/Lambda-calcolo/Lambda-calcolo.md#^definizione-termine) $T'$.
> 
> Per esempio, un [termine](Informatica/Lambda-calcolo/Lambda-calcolo.md#^definizione-termine) $T=\lambda V.(X\ (\lambda y.Z))$ si può riscrivere come $T=\lambda V.X\ (\lambda y.Z)$:
> 
> $$
> \begin{align*}
> T &= \lambda V.{\color{#FF7F7F} ( }X\ (\lambda y.Z){\color{#FF7F7F} ) } \\
> &= \lambda V.X\ (\lambda y.Z)
> \end{align*}
> $$
> 
> Semplicemente, se non sono presenti delle parentesi, tutto quello a destra del punto viene considerato come il corpo dell'[astrazione](Informatica/Lambda-calcolo/Lambda-calcolo.md#^definizione-astrazione) (che in questo caso corrisponderebbe a $X\ (\lambda y.Z)$).
^notazione-omissione-delle-parentesi-in-un-astrazione

> [!notazione]+ Notazione: omissione delle parentesi in un'applicazione
> 
> In un [termine](Informatica/Lambda-calcolo/Lambda-calcolo.md#^definizione-termine) $T=U\ V$ che rappresenta un'[applicazione](Informatica/Lambda-calcolo/Lambda-calcolo.md#^definizione-applicazione) della [funzione](Informatica/Lambda-calcolo/Lambda-calcolo.md#^definizione-astrazione) $U$ all'argomento $V$ si possono eliminare le parentesi più esterne della [funzione](Informatica/Lambda-calcolo/Lambda-calcolo.md#^definizione-astrazione) $U$.
> 
> Per esempio, un [termine](Informatica/Lambda-calcolo/Lambda-calcolo.md#^definizione-termine) $T = (M_1\ M_2)\ (M_3\ M_4)$ si può riscrivere come $T = M_1\ M_2\ (M_3\ M_4)$:
> 
> $$
> \begin{align*}
> T &= {\color{#FF7F7F} ( }M_1\ M_2{\color{#FF7F7F} ) }\ (M_3\ M_4) \\
> &= M_1\ M_2\ (M_3\ M_4)
> \end{align*}
> $$
> 
> **NON** si può riscrivere come $T = M_1\ M_2\ M_3\ M_4$ perché $(M_3\ M_4)$ è l'argomento dell'[applicazione](Informatica/Lambda-calcolo/Lambda-calcolo.md#^definizione-applicazione).
^notazione-omissione-delle-parentesi-in-un-applicazione

> [!trucco]+ Trucco: astrazione associativa a destra, applicazione associativa a sinistra
> 
> Per ricordare più facilmente come funziona l'[omissione delle parentesi in un'astrazione](Informatica/Lambda-calcolo/Lambda-calcolo.md#^notazione-omissione-delle-parentesi-in-un-astrazione) e [in un'applicazione](Informatica/Lambda-calcolo/Lambda-calcolo.md#^notazione-omissione-delle-parentesi-in-un-applicazione), ti basta ricordare che:
> - L'[astrazione](Informatica/Lambda-calcolo/Lambda-calcolo.md#^definizione-astrazione) è associativa a destra, cioè tutto quello che c'è a destra del punto è parte del corpo%% link %% dell'[astrazione](Informatica/Lambda-calcolo/Lambda-calcolo.md#^definizione-astrazione):
> 	$$
> 	\lambda x.{\color{#7FFF7F} \underbrace{T_1\ T_2 (T_3\ T_4)}_{\text{a destra del punto}} }
> 	\equiv
> 	\lambda x.\big( {\color{#7FFF7F} T_1\ T_2 (T_3\ T_4) } \big) 
> 	$$
> - L'[applicazione](Informatica/Lambda-calcolo/Lambda-calcolo.md#^definizione-applicazione) è associativa a sinistra, cioè tutto quello che c'è a sinistra dell'ultimo [termine](Informatica/Lambda-calcolo/Lambda-calcolo.md#^definizione-termine) (cioè l'argomento%% Link %%) è la [funzione](Matematica/Teoria%20degli%20insiemi/Funzioni/Funzioni.md#^definizione-funzione) su cui viene applicato l'argomento%% Link %%:
> 	$$
> 	{\color{#FF7F7F}
> 	\underbrace{T_1\ T_2\ T_3}_{
> 	\begin{array}{}
> 	\text{a sinistra} \\
> 	\text{dell'ultimo} \\
> 	\text{termine}
> 	\end{array}
> 	}
> 	} \ T_4
> 	\equiv
> 	({\color{#FF7F7F} T_1\ T_2\ T_3 })\ T_4
> 	$$

> [!esercizio]+ Esercizio 1 sulla rimozione delle parentesi
> 
> Rimuovere il più possibile le parentesi, senza cambiare il significato, del seguente [termine](Informatica/Lambda-calcolo/Lambda-calcolo.md#^definizione-termine):
> 
> $$
> (\lambda x.((x\ x)\ x))
> $$
> 
> > [!soluzione]- Soluzione
> > 
> > È possibile innanzitutto [rimuovere le parentesi più esterne](Informatica/Lambda-calcolo/Lambda-calcolo.md#^notazione-omissione-delle-parentesi-piu-esterne-di-un-termine) del [termine](Informatica/Lambda-calcolo/Lambda-calcolo.md#^definizione-termine):
> > 
> > $$
> > {\color{#FF7F7F} ( }\lambda x.((x\ x)\ x){\color{#FF7F7F} ) }
> > =
> > \lambda x.((x\ x)\ x)
> > $$
> > 
> > Avendo un'[astrazione](Informatica/Lambda-calcolo/Lambda-calcolo.md#^definizione-astrazione) con argomento $x$ e corpo $((x\ x)\ x)$, è possibile [rimuovere le parentesi nel corpo](Informatica/Lambda-calcolo/Lambda-calcolo.md#^notazione-omissione-delle-parentesi-in-un-astrazione):
> > 
> > $$
> > \lambda x.{\color{#FF7F7F} ( }(x\ x)\ x{\color{#FF7F7F} ) }
> > =
> > \lambda x.(x\ x)\ x
> > $$
> > 
> > Il corpo $(x\ x)$ x è un'[applicazione](Informatica/Lambda-calcolo/Lambda-calcolo.md#^definizione-applicazione) della [funzione](Informatica/Lambda-calcolo/Lambda-calcolo.md#^definizione-astrazione) $(x\ x)$ all'argomento $x$, quindi possiamo [rimuovere le parentesi della funzione](Informatica/Lambda-calcolo/Lambda-calcolo.md#^notazione-omissione-delle-parentesi-in-un-applicazione):
> > 
> > $$
> > \lambda x.{\color{#FF7F7F} ( }x\ x{\color{#FF7F7F} ) }\ x
> > =
> > \lambda x.x\ x\ x
> > $$

> [!esercizio]+ Esercizio 2 sulla rimozione delle parentesi
> 
> Rimuovere il più possibile le parentesi, senza cambiare il significato, del seguente [termine](Informatica/Lambda-calcolo/Lambda-calcolo.md#^definizione-termine):
> 
> $$
> (\lambda x.(\lambda y.(\lambda y.((x\ z)\ (y\ z)))))
> $$
> 
> > [!soluzione]- Soluzione
> > 
> > È possibile [rimuovere le parentesi più esterne del termine](Informatica/Lambda-calcolo/Lambda-calcolo.md#^notazione-omissione-delle-parentesi-piu-esterne-di-un-termine):
> > 
> > $$
> > {\color{#FF7F7F} ( }\lambda x.(\lambda y.(\lambda y.((x\ z)\ (y\ z)))){\color{#FF7F7F} ) }
> > =
> > \lambda x.(\lambda y.(\lambda y.((x\ z)\ (y\ z))))
> > $$
> > 
> > Avendo un'[astrazione](Informatica/Lambda-calcolo/Lambda-calcolo.md#^definizione-astrazione) con argomento%% link %% $x$ e corpo%% link %% $(\lambda y.(\lambda y.((x\ z)\ (y\ z))))$, è possibile [rimuovere le parentesi più esterne del corpo](Informatica/Lambda-calcolo/Lambda-calcolo.md#^notazione-omissione-delle-parentesi-in-un-astrazione):
> > 
> > $$
> > \lambda x.{\color{#FF7F7F} ( }\lambda y.(\lambda y.((x\ z)\ (y\ z))){\color{#FF7F7F} ) }
> > =
> > \lambda x.\lambda y.(\lambda y.((x\ z)\ (y\ z)))
> > $$
> > 
> > Avendo un'[astrazione](Informatica/Lambda-calcolo/Lambda-calcolo.md#^definizione-astrazione) con argomento%% link %% $y$ e corpo%% link %% $(\lambda y.((x\ z)\ (y\ z)))$, è possibile [rimuovere le parentesi più esterne del corpo](Informatica/Lambda-calcolo/Lambda-calcolo.md#^notazione-omissione-delle-parentesi-in-un-astrazione):
> > 
> > $$
> > \lambda x.\lambda y.{\color{#FF7F7F} ( }\lambda y.((x\ z)\ (y\ z)){\color{#FF7F7F} ) }
> > =
> > \lambda x.\lambda y.\lambda y.((x\ z)\ (y\ z))
> > $$
> > 
> > Avendo un'[astrazione](Informatica/Lambda-calcolo/Lambda-calcolo.md#^definizione-astrazione) con argomento%% link %% $y$ e corpo%% link %% $((x\ z)\ (y\ z))$, è possibile [rimuovere le parentesi più esterne del corpo](Informatica/Lambda-calcolo/Lambda-calcolo.md#^notazione-omissione-delle-parentesi-in-un-astrazione):
> > 
> > $$
> > \lambda x.\lambda y.\lambda y.{\color{#FF7F7F} ( }(x\ z)\ (y\ z){\color{#FF7F7F} ) }
> > =
> > \lambda x.\lambda y.\lambda y.(x\ z)\ (y\ z)
> > $$
> > 
> > Avendo un'[applicazione](Informatica/Lambda-calcolo/Lambda-calcolo.md#^definizione-applicazione) con funzione%% link %% $(x\ z)$ e argomento $(y\ z)$, è possibile [rimuovere le parentesi più esterne della funzione](Informatica/Lambda-calcolo/Lambda-calcolo.md#^notazione-omissione-delle-parentesi-in-un-applicazione):
> > 
> > $$
> > \lambda x.\lambda y.\lambda y.{\color{#FF7F7F} ( }x\ z{\color{#FF7F7F} ) }\ (y\ z)
> > =
> > \lambda x.\lambda y.\lambda y.x\ z\ (y\ z)
> > $$

%% 
Rimuovere parentesi:
$$
(((a\ b)\ (c\ d))\ ((e\ f)\ (g\ h)))
$$

Ripristinare tutte le parentesi omesse:
$$
x\ x\ x\ x
$$

Ripristinare:
$$
\lambda x.x\ \lambda y.y
$$

Ripristinare:
$$
\lambda x.(x\ \lambda y.y\ x\ x)\ x
$$
%%

## 1.5 - Variabili libere e legate in un termine

Prima di cominciare a effettuare operazioni con i [termini](Informatica/Lambda-calcolo/Lambda-calcolo.md#^definizione-termine), ci serve definire un ultimo concetto che ci permette di capire quale valore hanno le variabili%% link %% all'interno dei [termini](Informatica/Lambda-calcolo/Lambda-calcolo.md#^definizione-termine) stessi: per esempio, nell'[astrazione](Informatica/Lambda-calcolo/Lambda-calcolo.md#^definizione-astrazione) $\lambda x.M$ e nell'[applicazione](Informatica/Lambda-calcolo/Lambda-calcolo.md#^definizione-applicazione) $x\ M$ la variabile%% link %% $x$ non ha lo stesso "peso", perché nel primo caso è "legata" al [termine](Informatica/Lambda-calcolo/Lambda-calcolo.md#^definizione-termine) $M$ (essendo un argomento di quella funzione), mentre nel secondo caso è "libera" e non ha alcun particolare legame con $M$.

Fare questa distinzione è importante perché, svolgendo operazioni sui [termini](Informatica/Lambda-calcolo/Lambda-calcolo.md#^definizione-termine), dobbiamo assicurarci che il loro significato non venga modificato andando a toccare quelle variabili "legate".

Definiamo formalmente quindi questa differenza.

> [!definizione]+ Definizione: variabili libere e legate
> 
> L'**insieme delle variabili libere** di un [termine](Informatica/Lambda-calcolo/Lambda-calcolo.md#^definizione-termine) $T$, denotate con $\text{fv}(T)$ (dall'inglese _free variables_), è definito induttivamente sulla struttura di $T$ come segue:
> 
> - Quando il [termine](Informatica/Lambda-calcolo/Lambda-calcolo.md#^definizione-termine) $T$ è una variabile%% link %% $x$:
> 
> 	$$
> 	\text{fv}(T) = \text{fv}(x) \overset{\text{def}}{=} \{ x \}
> 	$$
> 
> - Quando il [termine](Informatica/Lambda-calcolo/Lambda-calcolo.md#^definizione-termine) $T$ è un'[astrazione](Informatica/Lambda-calcolo/Lambda-calcolo.md#^definizione-astrazione) $\lambda x.M$:
> 
> 	$$
> 	\text{fv}(T) = \text{fv}(\lambda x.M) \overset{\text{def}}{=} \text{fv}(M) \setminus \{ x \}
> 	$$
> 
> - Quando il [termine](Informatica/Lambda-calcolo/Lambda-calcolo.md#^definizione-termine) $T$ è un'[applicazione](Informatica/Lambda-calcolo/Lambda-calcolo.md#^definizione-applicazione) $M\ N$:
> 
> 	$$
> 	\text{fv}(T) = \text{fv}(M\ N) \overset{\text{def}}{=} \text{fv}(M) \cup \text{fv}(N)
> 	$$
> 
> Una variabile contenuta in $T$ si dice **_libera_** se è presente in $\text{fv}(T)$, **_legata_** altrimenti.
^definizione-variabili-libere-e-legate

> [!esempio]- Esempi di variabili libere e legate
> 
> Ecco qualche esempio di [variabili libere e legate](Informatica/Lambda-calcolo/Lambda-calcolo.md#^definizione-variabili-libere-e-legate) in diversi [termini](Informatica/Lambda-calcolo/Lambda-calcolo.md#^definizione-termine):
> 
> - $x$: la variabile%% link %% $x$ è [libera](Informatica/Lambda-calcolo/Lambda-calcolo.md#^definizione-variabili-libere-e-legate) perché non è vincolata da alcuna [astrazione](Informatica/Lambda-calcolo/Lambda-calcolo.md#^definizione-astrazione):
> 
> 	$$
> 	\text{fv}(x) = \{ x \}
> 	$$
> 
> - $\lambda x.x$: la variabile%% link %% $x$ è [legata](Informatica/Lambda-calcolo/Lambda-calcolo.md#^definizione-variabili-libere-e-legate) perché è vincolata dall'[astrazione](Informatica/Lambda-calcolo/Lambda-calcolo.md#^definizione-astrazione) (essendo un suo argomento):
> 
> 	$$
> 	\begin{align*}
> 	\text{fv}(\lambda x.y) & = \text{fv}(x) \setminus \{ x \} \\
> 	& = \{ x \} \setminus \{ x \} \\
> 	& = \emptyset
> 	\end{align*}
> 	$$
> 
> - $\lambda x.y$: la variabile%% link %% $x$ è [legata](Informatica/Lambda-calcolo/Lambda-calcolo.md#^definizione-variabili-libere-e-legate) perché è vincolata dall'[astrazione](Informatica/Lambda-calcolo/Lambda-calcolo.md#^definizione-astrazione) (essendo un suo argomento), ma la variabile%% link %% $y$ no:
> 
> 	$$
> 	\begin{align*}
> 	\text{fv}(\lambda x.y) & = \text{fv}(y) \setminus \{ x \} \\
> 	& = \{ y \} \setminus \{ x \} \\
> 	& = \{ y \}
> 	\end{align*}
> 	$$
> 
> - $\lambda x.\lambda y.y\ z\ x$: le variabili%% link %% $x$ e $y$ sono [legate](Informatica/Lambda-calcolo/Lambda-calcolo.md#^definizione-variabili-libere-e-legate) perché vincolate dalle rispettive [astrazioni](Informatica/Lambda-calcolo/Lambda-calcolo.md#^definizione-astrazione) (essendo loro argomenti%% link %%), ma la variabile%% link %% $z$ no:
> 
> $$
> \begin{align*}
> \text{fv}(\lambda x.\lambda y.y\ z\ x) & = \text{fv}(\lambda y.y\ z\ x) \setminus \{ x \} \\
> & = {\color{#FF7F7F} ( } \text{fv}(y\ z\ x) \setminus \{ y \} {\color{#FF7F7F} ) } \setminus \{ x \} \\
> & = {\color{#FF7F7F} ( } {\color{#7FFF7F} ( } \text{fv}(y) \cup \text{fv}(z) \cup \text{fv}(x) {\color{#7FFF7F} ) } \setminus \{ y \} {\color{#FF7F7F} ) } \setminus \{ x \} \\
> & = {\color{#FF7F7F} ( } {\color{#7FFF7F} ( } \{ y \} \cup \{ z \} \cup \{ x \} {\color{#7FFF7F} ) } \setminus \{ y \} {\color{#FF7F7F} ) } \setminus \{ x \} \\
> & = {\color{#FF7F7F} ( } \{ y, z, x \} \setminus \{ y \} {\color{#FF7F7F} ) } \setminus \{ x \} \\
> & = \{ z,x \} \setminus \{ x \} \\
> & = \{ z \}
> \end{align*}
> $$

> [!osservazione]+ Osservazione: una variabile che compare sia libera che legata
> 
> Consideriamo il [termine](Informatica/Lambda-calcolo/Lambda-calcolo.md#^definizione-termine)
> 
> $$
> (\lambda x.x\ y)\ x
> $$
> 
> Dato che $x$ compare sia come argomento%% link %% dell'[astrazione](Informatica/Lambda-calcolo/Lambda-calcolo.md#^definizione-astrazione) (e quindi [legata](Informatica/Lambda-calcolo/Lambda-calcolo.md#^definizione-variabili-libere-e-legate)), sia come argomento%% link %% dell'[applicazione](Informatica/Lambda-calcolo/Lambda-calcolo.md#^definizione-applicazione) esterna (e quindi [libera](Informatica/Lambda-calcolo/Lambda-calcolo.md#^definizione-variabili-libere-e-legate)), deve essere considerata libera o legata?
> 
> La risposta è che in realtà queste due $x$ non vanno considerate come la stessa $x$ ma separatamente, proprio perché vengono usate per due scopi diversi: per evitare confusioni quindi sarebbe opportuno _rinominare_ una delle due $x$ (per esempio in $z$) ed effettuando quindi un'operazione che prende il nome di [$\alpha$-conversione](Informatica/Lambda-calcolo/Lambda-calcolo.md#^definizione-alfa-conversione) (che vedremo più tardi).

%% 
trucco per ricordarsi come trovare le variabili libere: togliere tutte le variabili legate da un'astrazione
%%

> [!osservazione]+ Osservazione: variabili libere e legate come visibilità nei linguaggi di programmazione
> 
> La distinzione tra [variabili libere e legate](Informatica/Lambda-calcolo/Lambda-calcolo.md#^definizione-variabili-libere-e-legate) è utile a farci capire, trasportando questo concetto sui linguaggi di programmazione%% link %%, a capire qual è la visibilità%% link %% delle variabili%% link %% che usiamo:
> 
> - Le [variabili legate](Informatica/Lambda-calcolo/Lambda-calcolo.md#^definizione-variabili-libere-e-legate) possono essere pensate come variabili "locali"%% link %% della funzione%% link %%, utilizzabili unicamente all'interno di quella funzione e senza bisogno di altre informazioni dall'esterno per capire a cosa servono.
> - Le [variabili libere](Informatica/Lambda-calcolo/Lambda-calcolo.md#^definizione-variabili-libere-e-legate) possono essere pensate come variabili "globali"%% link %% della funzione%% link %%, usate al suo interno ma in realtà dichiarate all'esterno della funzione e, quindi, il loro valore dipende dal contesto in cui si trova la funzione%% link %%.

### 1.5.1 - Combinatori

Un concetto strettamente collegato a quello di [variabili libere](Informatica/Lambda-calcolo/Lambda-calcolo.md#^definizione-variabili-libere-e-legate) e che ci tornerà utile più tardi è quello dei [_combinatori_](Informatica/Lambda-calcolo/Lambda-calcolo.md#^definizione-combinatore).

> [!definizione]+ Definizione: combinatore
> 
> Un **combinatore** (o **termine chiuso**) è un [termine](Informatica/Lambda-calcolo/Lambda-calcolo.md#^definizione-termine) $T$ senza [variabili libere](Informatica/Lambda-calcolo/Lambda-calcolo.md#^definizione-variabili-libere-e-legate):
> 
> $$
> \text{fv}(T) = \emptyset
> $$
^definizione-combinatore

%% 
esempi di combinatori
%%

# 2 - Operazioni su termini

## 2.1 - Sostituzione

Come abbiamo visto, un'[applicazione](Informatica/Lambda-calcolo/Lambda-calcolo.md#^definizione-applicazione) $M\ N$ rappresenta essenzialmente la sostituzione delle variabili contenute in $M$ con i valori di $N$. Ma ciò non è un'operazione banale: le uniche variabili sostituibili sono quelle [libere](Informatica/Lambda-calcolo/Lambda-calcolo.md#^definizione-variabili-libere-e-legate) e questa è una cosa di cui bisogna tener conto per evitare che diventino [legate](Informatica/Lambda-calcolo/Lambda-calcolo.md#^definizione-variabili-libere-e-legate). Definiamo quindi correttamente come deve funzionare una [_sostituzione_](Informatica/Lambda-calcolo/Lambda-calcolo.md#^definizione-sostituzione) in un [termine](Informatica/Lambda-calcolo/Lambda-calcolo.md#^definizione-termine).

> [!definizione]+ Definizione: sostituzione
> 
> Nel [$\lambda$-calcolo](Informatica/Lambda-calcolo/Lambda-calcolo.md#^definizione-lambda-calcolo), una **sostituzione** è un'operazione binaria tra due [termini](Informatica/Lambda-calcolo/Lambda-calcolo.md#^definizione-termine) $T$ ed $N$ in cui una [variabile libera](Informatica/Lambda-calcolo/Lambda-calcolo.md#^definizione-variabili-libere-e-legate) $y$ di $T$ viene sostituita con $N$. Viene denotata come $T[N/y]$ ed è definita induttivamente sulla struttura di $T$ come segue:
> 
> - Quando il [termine](Informatica/Lambda-calcolo/Lambda-calcolo.md#^definizione-termine) $T$ è una variabile $x$:
> 
> 	$$
> 	T[N / y] = x [N / y] \overset{\text{def}}{=} \begin{cases}
> 	N & x = y \\
> 	x & x \ne y
> 	\end{cases}
> 	$$
> 
> - Quando il [termine](Informatica/Lambda-calcolo/Lambda-calcolo.md#^definizione-termine) $T$ è un'[astrazione](Informatica/Lambda-calcolo/Lambda-calcolo.md#^definizione-astrazione) $\lambda x.M$:
> 
> 	$$
> 	T[N / y] = (\lambda x.M)[N / y] \overset{\text{def}}{=} \begin{cases}
> 	\lambda x.M & x = y \\
> 	\lambda x.M[N / y] & x \ne y \land x \notin \text{fv}(N) \\
> 	\lambda z.M[z / x][N / y] & x \ne y \land x \in \text{fv}(N) \\
> 	\end{cases}
> 	$$
> 
> 	con $z \in \text{Var} \setminus (\text{fv}(M) \cup \text{fv}(N))$
> 
> - Quando il [termine](Informatica/Lambda-calcolo/Lambda-calcolo.md#^definizione-termine) $T$ è un'[applicazione](Informatica/Lambda-calcolo/Lambda-calcolo.md#^definizione-applicazione) $M_1\ M_2$:
> 	$$
> 	T[N / y] = (M_1\ M_2)[N / y] \overset{\text{def}}{=} M_1[N / y]\ M_2[N / y]
> 	$$
^definizione-sostituzione

%% 
esempio per ogni caso

$$
\begin{array}{}
(\lambda x.x)[y / x] \\
((\lambda x.x)\ x) [y / x] \\
(\lambda z.x) [y / x] \\
(\lambda y.x\ y)[y / x] \\
(\lambda x.y)[\lambda x.x / y] \\
(\lambda x.y)[\lambda z.x / y]
\end{array}
$$
%%

%% 
trucco per ricordarsi come fare la sostituzione
%%

## 2.2 - $\alpha$-conversione

Abbiamo detto che le [funzioni matematiche](Matematica/Teoria%20degli%20insiemi/Funzioni/Funzioni.md#^definizione-funzione) sono quindi un modo per rappresentare in maniera generica una [relazione](Matematica/Teoria%20degli%20insiemi/Relazioni%20tra%20insiemi.md#^definizione-relazione-n-aria) tra due [insiemi](Matematica/Teoria%20degli%20insiemi/Teoria%20degli%20insiemi.md#^definizione-insieme).

Per esempio, la [relazione](Matematica/Teoria%20degli%20insiemi/Relazioni%20tra%20insiemi.md#^definizione-relazione-n-aria) che associa a ogni numero naturale $x$ il suo quadrato $x^2$ (anch'esso nell'insieme dei numeri naturali $\mathbb{N}$) possiamo rappresentarla con la [funzione](Matematica/Teoria%20degli%20insiemi/Funzioni/Funzioni.md#^definizione-funzione)

$$
\begin{align*}
f \colon & \mathbb{N} \to \mathbb{N} \\
& x \mapsto x^2
\end{align*}
$$

Ma al posto di $x$ potremmo usare un'altra variabile per descrivere la [funzione](Matematica/Teoria%20degli%20insiemi/Funzioni/Funzioni.md#^definizione-funzione) mantenendo invariato il suo significato, per esempio $y$:

$$
\begin{align*}
f \colon & \mathbb{N} \to \mathbb{N} \\
& y \mapsto y^2
\end{align*}
$$

Oppure anche un simbolo che non è una lettera, come il simbolo $\star$ (si legge _star_, ossia _stella_):

$$
\begin{align*}
f \colon & \mathbb{N} \to \mathbb{N} \\
& \star \mapsto \star^2
\end{align*}
$$

Queste tre rappresentazioni sono perfettamente equivalenti e, nell'ambito del [$\lambda$-calcolo](Informatica/Lambda-calcolo/Lambda-calcolo.md#^definizione-lambda-calcolo), Alonzo Church decise di chiamare il processo di rinominare le variabili di una [funzione](Matematica/Teoria%20degli%20insiemi/Funzioni/Funzioni.md#^definizione-funzione) con il nome di [_$\alpha$-conversione_](Informatica/Lambda-calcolo/Lambda-calcolo.md#^definizione-alfa-conversione).

> [!definizione]+ Definizione: $\alpha$-conversione
> 
> L'**$\alpha$-conversione**, denotata con $\equiv_\alpha$, è una [relazione binaria](Matematica/Teoria%20degli%20insiemi/Relazioni%20tra%20insiemi.md#^definizione-relazione-n-aria) tra due [astrazioni](Informatica/Lambda-calcolo/Lambda-calcolo.md#^definizione-astrazione) $\lambda x.M$ e $\lambda y.M$ che permette di rinominare la [variabile legata](Informatica/Lambda-calcolo/Lambda-calcolo.md#^definizione-variabili-libere-e-legate) $x$ in un'altra [variabile legata](Informatica/Lambda-calcolo/Lambda-calcolo.md#^definizione-variabili-libere-e-legate) $y$ senza alterare il significato del [termine](Informatica/Lambda-calcolo/Lambda-calcolo.md#^definizione-termine):
> 
> $$
> y \notin \text{fv(M)} \iff \lambda x.M \equiv_\alpha \lambda y.M [y / x]
> $$
> 
> Le due [astrazioni](Informatica/Lambda-calcolo/Lambda-calcolo.md#^definizione-astrazione) $\lambda x.M$ e $\lambda y.M$ si dicono **_$\alpha$-equivalenti_**.
^definizione-alfa-conversione

%% 
esempi
$$
\begin{array}{}
\lambda x.x \equiv_\alpha \lambda y.y \\
\lambda x.y \equiv_\alpha \lambda z.y \\
\lambda x.y \not\equiv_\alpha \lambda y.y \\
\lambda x.\lambda y.x \equiv_\alpha \lambda z.\lambda y.z \\
\lambda x.\lambda y.x \equiv_\alpha \lambda x.\lambda z.x \\
\lambda x.\lambda y.x \not\equiv_\alpha \lambda y.\lambda y.y \\
\end{array} 
$$
%%

## 2.3 - $\beta$-riduzione

In matematica abbiamo che, data per esempio una [funzione](Matematica/Teoria%20degli%20insiemi/Funzioni/Funzioni.md#^definizione-funzione) $f(x) = x^2 + 2x + 1$, allora $f(5) = 5^2 + 2 \cdot 5 + 1 = 36$.

Nell'ambito del [$\lambda$-calcolo](Informatica/Lambda-calcolo/Lambda-calcolo.md#^definizione-lambda-calcolo), [applicare](Informatica/Lambda-calcolo/Lambda-calcolo.md#^definizione-applicazione) un'[astrazione](Informatica/Lambda-calcolo/Lambda-calcolo.md#^definizione-astrazione) $\lambda x.M$ a un argomento $N$ significa valutare il corpo della [funzione](Informatica/Lambda-calcolo/Lambda-calcolo.md#^definizione-astrazione) $M$ in cui ogni occorrenza della [variabile libera](Informatica/Lambda-calcolo/Lambda-calcolo.md#^definizione-variabili-libere-e-legate) $x$ è stata [sostituita](Informatica/Lambda-calcolo/Lambda-calcolo.md#^definizione-sostituzione) da $N$. Per intenderci, nell'esempio di prima abbiamo valutato $f(x)$ [applicandola](Informatica/Lambda-calcolo/Lambda-calcolo.md#^definizione-applicazione) all'argomento%% link %% $5$.

Questa idea è alla base della [_$\beta$-riduzione_](Informatica/Lambda-calcolo/Lambda-calcolo.md#^definizione-beta-riduzione).

> [!definizione]+ Definizione: $\beta$-riduzione
> 
> La **$\beta$-riduzione**, denotata con $\to_\beta$, è l'operazione che permette di [sostituire](Informatica/Lambda-calcolo/Lambda-calcolo.md#^definizione-sostituzione) in un'[applicazione](Informatica/Lambda-calcolo/Lambda-calcolo.md#^definizione-applicazione) $(\lambda x.M)\ N$ l'argomento $x$ dell'[astrazione](Informatica/Lambda-calcolo/Lambda-calcolo.md#^definizione-astrazione) con l'argomento $N$:
> 
> $$
> (\lambda x.M)\ N \to_\beta M[N / x]
> $$
> 
> In particolare, diciamo che:
> 
> - $(\lambda x.M)\ N$ è un **$\beta$-redex** (da _**red**ucible **ex**pression_, in italiano _espressione riducibile_) o, in alcuni casi, ricalcato in italiano come **redesso** e
> - $M[N/x]$ è il suo **ridotto**.
> 
> L'operazione inversa, cioè quella che dal **ridotto** ci fa risalire al **redesso**, viene detta **$\beta$-espansione** e viene denotata con $\leftarrow_\beta$:
> 
> $$
> M[N / x] \leftarrow_\beta (\lambda x.M)\ N
> $$
^definizione-beta-riduzione

> [!esempio]- Esempi di $\beta$-riduzione
> 
> Ecco qualche esempio di [$\beta$-riduzione](Informatica/Lambda-calcolo/Lambda-calcolo.md#^definizione-beta-riduzione) correttamente svolta:
> 
> $$
> \begin{align*}
> (\lambda x.x) M & \to_\beta x
> \end{align*}
> $$
> 
> $$
> \begin{align*}
> (\lambda x.x\ x)\ (\lambda y.y) & \to_\beta (\lambda y.y)\ (\lambda y.y)
> \\ & \to_\beta \lambda y.y \end{align*}
> $$
> 
> $$
> \begin{align*} (\lambda f.\lambda x.f\ (f\ x))\ M & \to_\beta \lambda x.M\ (M\ x)
> \end{align*}
> $$
> 
> $$
> \begin{align*}
> (\lambda f.\lambda g.\lambda x.f\ (g\ x))\ M\ N & \to_\beta (\lambda g.\lambda x.M\ (g\ x))\ N \\
> & \to_\beta \lambda x.M\ (N\ x)
> \end{align*}
> $$
> 
> $$
> \begin{align*}
> (\lambda x.\lambda y.x)\ M\ N & \to_\beta (\lambda y.M)\ N \\
> & \to_\beta M
> \end{align*}
> $$

%% 
Esercizio: applica la $\beta$-riduzione

$$
(\lambda x.y)\ ((\lambda z.(z\ z))\ (\lambda w.w))
$$
%%

## 2.4 - $\eta$-riduzione

Prendiamo un esempio di [$\beta$-riduzione](Informatica/Lambda-calcolo/Lambda-calcolo.md#^definizione-beta-riduzione):

$$
\begin{align*}
(\lambda x.M\ x)\ N & \to_\beta M\ N
\end{align*}
$$

Dal momento che l'[applicazione](Informatica/Lambda-calcolo/Lambda-calcolo.md#^definizione-applicazione) della [funzione](Informatica/Lambda-calcolo/Lambda-calcolo.md#^definizione-astrazione) $(\lambda x.M\ x)$ all'argomento $N$ e l'[applicazione](Informatica/Lambda-calcolo/Lambda-calcolo.md#^definizione-applicazione) della [funzione](Informatica/Lambda-calcolo/Lambda-calcolo.md#^definizione-astrazione) $M$ all'argomento $N$ generano in entrambi i casi $M\ N$, per il principio di estensionalità delle funzioni%% link %% potremmo dire che $(\lambda x.M\ x)$ e $M$ sono due [funzioni](Matematica/Teoria%20degli%20insiemi/Funzioni/Funzioni.md#^definizione-funzione) equivalenti, quindi l'una deve essere trasformabile nell'altra attraverso una [$\beta$-riduzione](Informatica/Lambda-calcolo/Lambda-calcolo.md#^definizione-beta-riduzione).

Tuttavia, però, non in tutti i casi può valere la [$\beta$-riduzione](Informatica/Lambda-calcolo/Lambda-calcolo.md#^definizione-beta-riduzione) che da $(\lambda x.M\ x)$ ci porta a $M$ o viceversa (attenzione: per poter applicare la [$\beta$-riduzione](Informatica/Lambda-calcolo/Lambda-calcolo.md#^definizione-beta-riduzione) e ottenere $M$ ci serve avere $(\lambda x.M)\ x$ che non è equivalente a $(\lambda x.M\ x)$!):

$$
\begin{align*}
(\lambda x.M\ x) \not\to_\beta M \\
M \not\to_\beta (\lambda x.M\ x)
\end{align*}
$$

Ciò ci fa pensare che, per continuare a far valere correttamente il principio di estensionalità delle funzioni%% link %%, la [$\beta$-riduzione](Informatica/Lambda-calcolo/Lambda-calcolo.md#^definizione-beta-riduzione) da sola non ci basta (come, per esempio, in questi casi appena visti): abbiamo bisogno di introdurre quindi una nuova operazione, la [_$\eta$-riduzione_](Informatica/Lambda-calcolo/Lambda-calcolo.md#^definizione-eta-riduzione).

> [!definizione]+ Definizione: $\eta$-riduzione
> 
> L'**$\eta$-riduzione**, denotata con $\to_\eta$, è l'operazione che permette di ridurre un'[astrazione](Informatica/Lambda-calcolo/Lambda-calcolo.md#^definizione-astrazione) $\lambda x.M\ x$ nel [termine](Informatica/Lambda-calcolo/Lambda-calcolo.md#^definizione-termine) $M$:
> 
> $$
> \lambda x.M\ x \to_\eta M
> $$
> 
> In particolare, diciamo che:
> 
> - $\lambda x.M\ x$ è un **$\eta$-redex** (da _**red**ucible **ex**pression_, in italiano _espressione riducibile_) o, in alcuni casi, ricalcato in italiano come **redesso** e
> - $M$ è il suo **ridotto**.
> 
> L'operazione inversa, cioè quella che dal **ridotto** ci fa risalire al **redesso**, viene detta **$\eta$-espansione** e viene denotata con $\leftarrow_\eta$:
> 
> $$
> M \leftarrow_\eta \lambda x.M\ x
> $$
^definizione-eta-riduzione

## 2.5 - Riduzione singola e multipla

Durante lo svolgimento di [$\beta$-riduzioni](Informatica/Lambda-calcolo/Lambda-calcolo.md#^definizione-beta-riduzione) ed [$\eta$-riduzioni](Informatica/Lambda-calcolo/Lambda-calcolo.md#^definizione-eta-riduzione) è comodo alcune volte "generalizzare" il concetto di _riduzione_ senza specificare quale delle due si sta applicando: per questo motivo, chiamiamo _[riduzione singola](Informatica/Lambda-calcolo/Lambda-calcolo.md#^definizione-riduzione-singola)_, denotata con $\to$, l'uso generale di una delle due riduzioni tra la [$\beta$-riduzione](Informatica/Lambda-calcolo/Lambda-calcolo.md#^definizione-beta-riduzione) e l'[$\eta$-riduzione](Informatica/Lambda-calcolo/Lambda-calcolo.md#^definizione-eta-riduzione).

> [!definizione]+ Definizione: riduzione singola
> 
> Una **riduzione singola** (o, più semplicemente, **riduzione**), denotata con $\to$, è un singolo passo di [$\beta$-riduzione](Informatica/Lambda-calcolo/Lambda-calcolo.md#^definizione-beta-riduzione) o di [$\eta$-riduzione](Informatica/Lambda-calcolo/Lambda-calcolo.md#^definizione-eta-riduzione).
> 
> $M$ si dice **riducibile** in $N$.
^definizione-riduzione-singola

Avendo definito formalmente la [riduzione singola](Informatica/Lambda-calcolo/Lambda-calcolo.md#^definizione-riduzione-singola), possiamo ora generalizzare ulteriormente più passi di riduzione in una sola operazione, senza avere la necessità di esplicitarli tutti: definiamo quindi la [_riduzione multipla_](Informatica/Lambda-calcolo/Lambda-calcolo.md#^definizione-riduzione-multipla).

> [!definizione]+ Definizione: riduzione multipla
> 
> Una **riduzione multipla**, denotata con $\Rightarrow$ (o, in alcuni casi, con $\to^\star$), è una chiusura riflessiva e transitiva della relazione di [riduzione singola](Informatica/Lambda-calcolo/Lambda-calcolo.md#^definizione-riduzione-singola), ossia la più piccola relazione tale che:
> 
> - Riflessività (zero passi sono ammessi): $M \implies M$.
> - Un passo è ammesso: $(M \to N) \implies (M \Rightarrow N)$.
> - Transitività (più passi sono ammessi): $(M \Rightarrow N \land N \Rightarrow O) \implies (M \Rightarrow O)$.
> 
> $M$ si dice **riducibile in zero o più passi** in $N$.
^definizione-riduzione-multipla

## 2.6 - Conversione

La [riduzione multipla](Informatica/Lambda-calcolo/Lambda-calcolo.md#^definizione-riduzione-multipla) è una [relazione](Matematica/Teoria%20degli%20insiemi/Relazioni%20tra%20insiemi.md#^definizione-relazione-n-aria) tra due [termini](Informatica/Lambda-calcolo/Lambda-calcolo.md#^definizione-termine) che può essere interpretata come una sorta di "equivalenza" tra di essi: se abbiamo che $M \Rightarrow N$, allora possiamo dedurre che in qualche modo dal [termine](Informatica/Lambda-calcolo/Lambda-calcolo.md#^definizione-termine) $M$ si può arrivare al [termine](Informatica/Lambda-calcolo/Lambda-calcolo.md#^definizione-termine) $N$, seppur con più di qualche passaggio di [riduzione singola](Informatica/Lambda-calcolo/Lambda-calcolo.md#^definizione-riduzione-singola). Viceversa, facendo lo stesso discorso per le _espansioni_, cioè [$\beta$-espansione](Informatica/Lambda-calcolo/Lambda-calcolo.md#^definizione-beta-riduzione) ed [$\eta$-espansione](Informatica/Lambda-calcolo/Lambda-calcolo.md#^definizione-eta-riduzione), si potrebbe dire che da $N$ possiamo risalire a $M$. Insomma, si potrebbe dire che $M$ ed $N$ sono uguali _semanticamente_, cioè rappresentano la stessa [funzione](Informatica/Lambda-calcolo/Lambda-calcolo.md#^definizione-astrazione).

A questa intercambiabilità tra [termini](Informatica/Lambda-calcolo/Lambda-calcolo.md#^definizione-termine) collegati da una [riduzione multipla](Informatica/Lambda-calcolo/Lambda-calcolo.md#^definizione-riduzione-multipla) diamo il nome di [_conversione_](Informatica/Lambda-calcolo/Lambda-calcolo.md#^definizione-conversione).

> [!definizione]+ Definizione: conversione
> 
> Sia $\Lambda$ l'[insieme](Matematica/Teoria%20degli%20insiemi/Teoria%20degli%20insiemi.md#^definizione-insieme) di [termini](Informatica/Lambda-calcolo/Lambda-calcolo.md#^definizione-termine) del [$\lambda$-calcolo](Informatica/Lambda-calcolo/Lambda-calcolo.md#^definizione-lambda-calcolo). La [relazione binaria](Matematica/Teoria%20degli%20insiemi/Relazioni%20tra%20insiemi.md#^definizione-relazione-n-aria) $\Leftrightarrow\, \subseteq \Lambda \times \Lambda$ è detta **conversione** ed è definita come segue:
> 
> $$
> \forall M,N \in \Lambda (M \Leftrightarrow N \iff (M \Rightarrow N \lor N \Rightarrow M))
> $$
> 
> In questo caso, $M$ si dice **convertibile** in $N$ e viceversa.
^definizione-conversione

%% 
esempi:

$$
% Lambda Calculus environment 
(\lambda x.\lambda y.x)\ M\ N \Leftrightarrow \lambda z.M\ z
$$
perché
$$
\begin{align*}
(\lambda x.\lambda y.x)\ M\ N & \to_\beta (\lambda y.M)\ N \\
& \to_\beta M \\
& \leftarrow_\eta \lambda z.M\ z
\end{align*}
$$

altro esempio:
$$
% Lambda Calculus environment 
(\lambda x.x\ x)\ (\lambda y.y) \Leftrightarrow \lambda u.u
$$
%%

# 3 - Forma normale e strategie di riduzione

> [!osservazione]+ Osservazione: $\beta$-riduzioni che non terminano
> 
> Consideriamo il seguente esempio di [$\beta$-riduzione](Informatica/Lambda-calcolo/Lambda-calcolo.md#^definizione-beta-riduzione):
> 
> $$
> \begin{align*}
> (\lambda x.x\ x)\ (\lambda y.y\ y) & \to_\beta (\lambda y.y\ y)\ (\lambda y.y\ y) \\
> & \to_\beta (\lambda y.y\ y)\ (\lambda y.y\ y) \\
> & \ldots
> \end{align*}
> $$
> 
> Come possiamo notare, ogni passo di [$\beta$-riduzione](Informatica/Lambda-calcolo/Lambda-calcolo.md#^definizione-beta-riduzione) non ci permette di ridurre ulteriormente il [termine](Informatica/Lambda-calcolo/Lambda-calcolo.md#^definizione-termine) ma ci fa ritornare puntualmente allo stato in cui è nella forma $(\lambda x.x\ x)\ (\lambda y.y\ y)$: da ciò possiamo evincere che la [$\beta$-riduzione](Informatica/Lambda-calcolo/Lambda-calcolo.md#^definizione-beta-riduzione) in alcuni casi può anche non terminare mai.

Questo particolare [termine](Informatica/Lambda-calcolo/Lambda-calcolo.md#^definizione-termine) $(\lambda x.x\ x)\ (\lambda y.y\ y)$ è un [combinatore](Informatica/Lambda-calcolo/Lambda-calcolo.md#^definizione-combinatore) (perché ha solo [variabili legate](Informatica/Lambda-calcolo/Lambda-calcolo.md#^definizione-variabili-libere-e-legate)) e scopriremo più tardi che è un [combinatore](Informatica/Lambda-calcolo/Lambda-calcolo.md#^definizione-combinatore) molto famoso, ossia il _combinatore di punto fisso $Y$_%% link %%.

%% 
Non tutti i lambda termini hanno forma normale e la beta riduzione non ha sempre lunghezza finita. Questo fenomeno rappresenta il fatto che il calcolo di un programma può procedere indefinitamente e divergere e permette di rappresentare [funzioni parziali](https://it.wikipedia.org/w/index.php?title=Funzioni_parziali&action=edit&redlink=1 "Funzioni parziali (la pagina non esiste)").

L'esempio classico di divergenza è costruibile a partire dal termine duplicatore 𝛿=𝑑𝑒𝑓𝜆𝑥.(𝑥𝑥)![{\displaystyle \delta ={def}\lambda x.(xx)}](https://wikimedia.org/api/rest_v1/media/math/render/svg/32e1236a84fb9c153eca9a24765dcb39e87194d1), che non fa altro che prendere un termine e restituirne due copie, l'una applicata all'altra. È possibile dunque definire il termine 𝜔=𝑑𝑒𝑓(𝛿𝛿)![{\displaystyle \omega ={def}(\delta \delta )}](https://wikimedia.org/api/rest_v1/media/math/render/svg/958a21ed50b20879ee4a91f4937eb78f3c2a5bbb), e notare che esso riduce a se stesso 𝜔\to𝛽𝜔\to𝛽...![{\displaystyle \omega \rightarrow {\beta }\omega \rightarrow {\beta }\dots }](https://wikimedia.org/api/rest_v1/media/math/render/svg/7475423b76bf608c15fcf4842ab84cba1c6a13e0).

%%

Intanto, ai [termini](Informatica/Lambda-calcolo/Lambda-calcolo.md#^definizione-termine) che prima o poi arrivano a un certo punto in cui non possono essere più [ridotti](Informatica/Lambda-calcolo/Lambda-calcolo.md#^definizione-beta-riduzione) diciamo che sono in [_forma normale_](Informatica/Lambda-calcolo/Lambda-calcolo.md#^definizione-forma-normale).

> [!definizione]+ Definizione: forma normale
> 
> Nel [$\lambda$-calcolo](Informatica/Lambda-calcolo/Lambda-calcolo.md#^definizione-lambda-calcolo), un [termine](Informatica/Lambda-calcolo/Lambda-calcolo.md#^definizione-termine) $M$ si dice che è in **forma normale** e si denota con $M \not\to$ se non può più essere [ridotto](Informatica/Lambda-calcolo/Lambda-calcolo.md#^definizione-riduzione-singola), ovvero se **non** esiste un altro [termine](Informatica/Lambda-calcolo/Lambda-calcolo.md#^definizione-termine) $N$ tale che $M \to N$:
> 
> $$
> \forall M \in \Lambda \big( (M \not\to) \iff \not\exists N \in \Lambda (M \to N) \big)
> $$
> 
> dove $\Lambda$ è l'[insieme](Matematica/Teoria%20degli%20insiemi/Teoria%20degli%20insiemi.md#^definizione-insieme) di [termini](Informatica/Lambda-calcolo/Lambda-calcolo.md#^definizione-termine) del [$\lambda$-calcolo](Informatica/Lambda-calcolo/Lambda-calcolo.md#^definizione-lambda-calcolo).
^definizione-forma-normale

## 3.1 - Confluenza

%% 
spiegazione idea teorema della confluenza:
ordine in cui si fanno le operazioni è importante.
Per esempio in aritmetica:
$$
(1 + 2) \cdot (3 + 4) = \{ 3 \cdot (3 + 4), (1+2) \cdot 7 \} = 3 \cdot 7  =21
$$
in aritmetica entrambe le espressioni confluiscono nello stesso risultato.

In Java no:
esempio (consideriamo `{java}int a = 1;`):
$$
(a = 2) * (a + 1) = 2 * (a + 1) = 2 * 3 = 6
$$
oppure
$$
(a = 2) * (a + 1) = (a = 2) * 2 = 2 * 2 = 4
$$
in base a quale delle due operazioni Java valuta prima, il risultato cambia: la confluenza non funziona

Quindi la confluenza vale finché non ci sono di mezzo modifiche della memoria (come in Java): ciò significa che vale anche nel $\lambda$-calcolo
%%

> [!teorema]+ Teorema della confluenza
> 
> Sia $\Lambda$ l'[insieme](Matematica/Teoria%20degli%20insiemi/Teoria%20degli%20insiemi.md#^definizione-insieme) di [termini](Informatica/Lambda-calcolo/Lambda-calcolo.md#^definizione-termine) del [$\lambda$-calcolo](Informatica/Lambda-calcolo/Lambda-calcolo.md#^definizione-lambda-calcolo).
> Dati tre [termini](Informatica/Lambda-calcolo/Lambda-calcolo.md#^definizione-termine) $M, N_1, N_2 \in \Lambda$, con $M \Rightarrow N_1$ e $M \Rightarrow N_2$, allora esiste un [termine](Informatica/Lambda-calcolo/Lambda-calcolo.md#^definizione-termine) $N \in \Lambda$ tale che $N_1 \Rightarrow N$ e $N_2 \Rightarrow N$.
> 
> $$
> \forall M,N_1,N_2 \in \Lambda \big((M \Rightarrow N_1 \land M \Rightarrow N_2) \implies \exists N \in \Lambda (N_1 \Rightarrow N \land N_2 \Rightarrow N)\big)
> $$
^teorema-della-confluenza

%% 
Grazie alla forma normale, possiamo aggiungere un importante corollario al teorema della confluenza, specificando che grazie alla confluenza otteniamo UN'UNICA forma normale di un termine (quando esiste)
%%

> [!corollario]+ Corollario del teorema della confluenza
> 
> La [forma normale](Informatica/Lambda-calcolo/Lambda-calcolo.md#^definizione-forma-normale) di un [termine](Informatica/Lambda-calcolo/Lambda-calcolo.md#^definizione-termine) $M$, se esiste, è **unica** (a meno di [$\alpha$-conversioni](Informatica/Lambda-calcolo/Lambda-calcolo.md#^definizione-alfa-conversione)).
> 
> In termini matematici, per ogni [termine](Informatica/Lambda-calcolo/Lambda-calcolo.md#^definizione-termine) $M$, se esistono due [termini](Informatica/Lambda-calcolo/Lambda-calcolo.md#^definizione-termine) $N_1$ ed $N_2$ in [forma normale](Informatica/Lambda-calcolo/Lambda-calcolo.md#^definizione-forma-normale) ($N_1\not\to$ e $N_2\not\to$) nei quali $M$ può essere [ridotto](Informatica/Lambda-calcolo/Lambda-calcolo.md#^definizione-riduzione-singola) ($M \Rightarrow N_1$ e $M \Rightarrow N_2$), allora $N_1$ ed $N_2$ sono [$\alpha$-equivalenti](Informatica/Lambda-calcolo/Lambda-calcolo.md#^definizione-alfa-conversione) ($N_1 \equiv_\alpha N_2$):
> 
> $$
> \forall M \in  \Lambda , \exists N_1,N_2 \in  \Lambda \Big(\big((M \Rightarrow N_1\not\to)\land(M \Rightarrow N_2\not\to)\big) \implies (N_1 \equiv_\alpha N_2)\Big)
> $$
> 
> dove $\Lambda$ è l'[insieme](Matematica/Teoria%20degli%20insiemi/Teoria%20degli%20insiemi.md#^definizione-insieme) di [termini](Informatica/Lambda-calcolo/Lambda-calcolo.md#^definizione-termine) del [$\lambda$-calcolo](Informatica/Lambda-calcolo/Lambda-calcolo.md#^definizione-lambda-calcolo).

%% questo corollario è importantissimo: ci assicura che i nostri programmi in lambda-calcolo si comportano in maniera deterministica %%

%% 
Dimostrazione per assurdo
![dimostrazione per assurdo](Pasted%20image%2020251128201000.png)
%%

## 3.2 - Strategie di riduzione

%% 
introduzione alle strategie di riduzione
%%

>[!definizione]+ Definizione: ordine applicativo
> 
> L'**ordine applicativo** è una strategia di [riduzione](Informatica/Lambda-calcolo/Lambda-calcolo.md#^definizione-riduzione-singola) in cui [applicare](Informatica/Lambda-calcolo/Lambda-calcolo.md#^definizione-applicazione) una [funzione](Informatica/Lambda-calcolo/Lambda-calcolo.md#^definizione-astrazione) a un argomento significa prima valutare l'argomento e poi sostituire il valore ottenuto nel corpo della [funzione](Informatica/Lambda-calcolo/Lambda-calcolo.md#^definizione-astrazione). In altre parole, in un [termine](Informatica/Lambda-calcolo/Lambda-calcolo.md#^definizione-termine) del tipo
> 
> $$
> ( \lambda x.x)\ (( \lambda y.y)\ z)
> $$
> 
> viene scelto il [$\beta$-redex](Informatica/Lambda-calcolo/Lambda-calcolo.md#^definizione-beta-riduzione) più a sinistra e più interno, ossia in questo caso $(\lambda y.y)\ z$:
> 
> $$
> ( \lambda x.x)\ (( \lambda y.y)\ z) \to_\beta ( \lambda x.x)\ z
> $$
> 
> I linguaggi funzionali che utilizzano l'ordine applicativo sono detti **linguaggi zelanti** (in inglese **eager languages**).
^definizione-ordine-applicativo

> [!definizione]+ Definizione: ordine normale
> 
> L'**ordine normale** è una strategia di [riduzione](Informatica/Lambda-calcolo/Lambda-calcolo.md#^definizione-riduzione-singola) in cui [applicare](Informatica/Lambda-calcolo/Lambda-calcolo.md#^definizione-applicazione) una [funzione](Informatica/Lambda-calcolo/Lambda-calcolo.md#^definizione-astrazione) a un argomento significa sostituire l'argomento nel corpo della [funzione](Informatica/Lambda-calcolo/Lambda-calcolo.md#^definizione-astrazione). In altre parole, in un [termine](Informatica/Lambda-calcolo/Lambda-calcolo.md#^definizione-termine) del tipo
> 
> $$
> ( \lambda x.x)\ (( \lambda y.y)\ z)
> $$
> 
> viene scelto il [$\beta$-redex](Informatica/Lambda-calcolo/Lambda-calcolo.md#^definizione-beta-riduzione) più a sinistra e più esterno, ossia in questo caso l'intero [termine](Informatica/Lambda-calcolo/Lambda-calcolo.md#^definizione-termine):
> 
> $$
> ( \lambda x.x)\ (( \lambda y.y)\ z) \to_\beta ( \lambda y.y)\ z
> $$
> 
> I linguaggi funzionali che utilizzano l'ordine applicativo sono detti **linguaggi pigri** (in inglese **lazy languages**).
^definizione-ordine-normale

> [!osservazione]+ Osservazione: cosa scegliere tra ordine applicativo e ordine applicativo
> 
> Le due strategie di riduzione viste, ossia l'[ordine applicativo](Informatica/Lambda-calcolo/Lambda-calcolo.md#^definizione-ordine-applicativo) e l'[ordine normale](Informatica/Lambda-calcolo/Lambda-calcolo.md#^definizione-ordine-normale), **non** sono equivalenti, e spesso conviene usare una al posto dell'altra.
> 
> Prendiamo come esempio il seguente [termine](Informatica/Lambda-calcolo/Lambda-calcolo.md#^definizione-termine):
> 
> $$
> ( \lambda x.y)\ (( \lambda z.z)\ ( \lambda z.z))
> $$
> 
> Se eseguito con l'[ordine applicativo](Informatica/Lambda-calcolo/Lambda-calcolo.md#^definizione-ordine-applicativo), otteniamo le seguenti [$\beta$-riduzioni](Informatica/Lambda-calcolo/Lambda-calcolo.md#^definizione-beta-riduzione):
> 
> $$
> \begin{align*}
> ( \lambda x.y)\ (( \lambda z.z)\ ( \lambda z.z)) &\to_\beta ( \lambda x.y)\ ( \lambda z.z) \\
> &\to_\beta y
> \end{align*}
> $$
> 
> Se invece viene eseguito con l'[ordine normale](Informatica/Lambda-calcolo/Lambda-calcolo.md#^definizione-ordine-normale), otteniamo la seguente [$\beta$-riduzione](Informatica/Lambda-calcolo/Lambda-calcolo.md#^definizione-beta-riduzione):
> 
> $$
> \begin{align*}
> ( \lambda x.y)\ (( \lambda z.z)\ ( \lambda z.z)) &\to_\beta y
> \end{align*}
> $$
> 
> Notiamo quindi che in questo caso l'[ordine normale](Informatica/Lambda-calcolo/Lambda-calcolo.md#^definizione-ordine-normale) conviene, perché in questo modo l'argomento $x$ non viene proprio valutato.
> 
> Al contrario, consideriamo il seguente [termine](Informatica/Lambda-calcolo/Lambda-calcolo.md#^definizione-termine):
> 
> $$
> ( \lambda x.x\ x)\ (( \lambda y.y)\ ( \lambda z.z))
> $$
> 
> Se eseguito con l'[ordine applicativo](Informatica/Lambda-calcolo/Lambda-calcolo.md#^definizione-ordine-applicativo), otteniamo le seguenti [$\beta$-riduzioni](Informatica/Lambda-calcolo/Lambda-calcolo.md#^definizione-beta-riduzione):
> 
> $$
> \begin{align*}
> ( \lambda x.x\ x)\ (( \lambda y.y)\ ( \lambda z.z)) &\to_\beta ( \lambda x.x\ x)\ ( \lambda z.z) \\
> &\to_\beta ( \lambda z.z)\ ( \lambda z.z) \\
> &\to_\beta \lambda z.z
> \end{align*}
> $$
> 
> Se invece viene eseguito con l'[ordine normale](Informatica/Lambda-calcolo/Lambda-calcolo.md#^definizione-ordine-normale), otteniamo le seguenti [$\beta$-riduzioni](Informatica/Lambda-calcolo/Lambda-calcolo.md#^definizione-beta-riduzione):
> 
> $$
> \begin{align*}
> ( \lambda x.x\ x)\ (( \lambda y.y)\ ( \lambda z.z)) &\to_\beta (( \lambda y.y)\ ( \lambda z.z))\ (( \lambda y.y)\ ( \lambda z.z)) \\
> &\to_\beta ( \lambda z.z)(( \lambda y.y)\ ( \lambda z.z)) \\
> &\to_\beta ( \lambda y.y)\ ( \lambda z.z) \\
> &\to_\beta \lambda z.z
> \end{align*}
> $$
> 
> Possiamo notare come invece, in questo caso, convenga usare l'[ordine applicativo](Informatica/Lambda-calcolo/Lambda-calcolo.md#^definizione-ordine-applicativo) perché l'argomento $x$ viene usato due volte e in quest'ultimo caso viene valutato entrambe le volte in due step diversi.

%% 
osservazione:
per ottimizzare l'ordine normale nei casi in cui viene valutata più volte la stessa [$\lambda$-espressione](Informatica/Lambda-calcolo/Lambda-calcolo.md#^definizione-termine), si può costruire un meccanismo di caching: il risultato della valutazione di ogni [$\lambda$-espressione](Informatica/Lambda-calcolo/Lambda-calcolo.md#^definizione-termine) viene memorizzato, così che nel caso in cui si dovesse ripresentare in futuro, si sa già direttamente qual è il risultato
%%

## 3.3 - Normalizzazione

> [!teorema]+ Teorema della normalizzazione
> 
> Dati due [termini](Informatica/Lambda-calcolo/Lambda-calcolo.md#^definizione-termine) $M,N$, se $M$ è [convertibile](Informatica/Lambda-calcolo/Lambda-calcolo.md#^definizione-conversione) in $N$ (cioè $M \Leftrightarrow N$) ed $N$ è in [forma normale](Informatica/Lambda-calcolo/Lambda-calcolo.md#^definizione-forma-normale) ($N\not\to$), allora esiste una [riduzione multipla](Informatica/Lambda-calcolo/Lambda-calcolo.md#^definizione-riduzione-multipla) composta da [$\beta$-riduzioni](Informatica/Lambda-calcolo/Lambda-calcolo.md#^definizione-beta-riduzione) in [ordine normale](Informatica/Lambda-calcolo/Lambda-calcolo.md#^definizione-ordine-normale) (che indichiamo con $\Rightarrow_{\text{no}}$) che porta da $M$ a $N$:
> 
> $$
> (M \Leftrightarrow N \land N\not\to) \implies (M \Rightarrow_{\text{no}} N)
> $$
^teorema-della-normalizzazione

> [!osservazione]+ Osservazione: teorema della normalizzazione non vale per l'ordine applicativo
> 
> Il [teorema della normalizzazione](Informatica/Lambda-calcolo/Lambda-calcolo.md#^teorema-della-normalizzazione) vale solo se le [$\beta$-riduzioni](Informatica/Lambda-calcolo/Lambda-calcolo.md#^definizione-beta-riduzione) vengono eseguite secondo l'[ordine normale](Informatica/Lambda-calcolo/Lambda-calcolo.md#^definizione-ordine-normale), mentre non vale se si usa l'[ordine applicativo](Informatica/Lambda-calcolo/Lambda-calcolo.md#^definizione-ordine-applicativo). Un esempio di ciò è dato dal seguente [termine](Informatica/Lambda-calcolo/Lambda-calcolo.md#^definizione-termine):
> 
> $$
> ( \lambda x.y)\ (( \lambda x.x\ x)\ ( \lambda x.x\ x))
> $$
> 
> Se eseguito con l'[ordine applicativo](Informatica/Lambda-calcolo/Lambda-calcolo.md#^definizione-ordine-applicativo), abbiamo:
> 
> $$
> \begin{align*}
> ( \lambda x.y)\ (( \lambda x.x\ x)\ ( \lambda x.x\ x)) &\to_\beta ( \lambda x.y)\ (x\ x)[( \lambda x.x\ x)/x]\\
> &=( \lambda x.y)\ (( \lambda x.x\ x)\ ( \lambda x.x\ x)) \\
> & \ldots
> \end{align*}
> $$
> 
> Possiamo notare che il [termine](Informatica/Lambda-calcolo/Lambda-calcolo.md#^definizione-termine), con questa strategia di riduzione, non raggiunge mai la sua [forma normale](Informatica/Lambda-calcolo/Lambda-calcolo.md#^definizione-forma-normale). Al contrario, con l'[ordine normale](Informatica/Lambda-calcolo/Lambda-calcolo.md#^definizione-ordine-normale) abbiamo:
> 
> $$
> \begin{align*}
> ( \lambda x.y)\ (( \lambda x.x\ x)\ ( \lambda x.x\ x)) &\to_\beta y[(( \lambda x.x\ x)\ ( \lambda x.x\ x))/x] \\
> &=y
> \end{align*}
> $$
> 
> Con l'[ordine normale](Informatica/Lambda-calcolo/Lambda-calcolo.md#^definizione-ordine-normale) raggiungiamo subito la [forma normale](Informatica/Lambda-calcolo/Lambda-calcolo.md#^definizione-forma-normale).

# 4 - Currying

Abbiamo notato che nelle [astrazioni](Informatica/Lambda-calcolo/Lambda-calcolo.md#^definizione-astrazione) possiamo passare come parametri una singola variabile, il che sembra abbastanza limitante se abbiamo bisogno di usare funzioni che necessitano più parametri.

Possiamo tuttavia usare un piccolo trucchetto sfruttando le funzioni di ordine superiore. Prendendo per esempio due variabili $x$ e $y$ che devono essere passate come parametri alla stessa funzione $x+y$, possiamo creare un'[astrazione](Informatica/Lambda-calcolo/Lambda-calcolo.md#^definizione-astrazione) che ha come parametro $x$ e nel suo corpo prende un'altra [astrazione](Informatica/Lambda-calcolo/Lambda-calcolo.md#^definizione-astrazione) che ha come parametro $y$ e come corpo $x+y$:

$$
 \lambda x. \lambda y.x+y
$$

In questo modo, [applicando](Informatica/Lambda-calcolo/Lambda-calcolo.md#^definizione-applicazione) a quest'[astrazione](Informatica/Lambda-calcolo/Lambda-calcolo.md#^definizione-astrazione) i due valori per i parametri $x$ e $y$ (per esempio, passiamo rispettivamente i valori $2$ e $3$), tramite la [$\beta$-riduzione](Informatica/Lambda-calcolo/Lambda-calcolo.md#^definizione-beta-riduzione) possiamo verificare che otterremo proprio quel che vogliamo:

$$
\begin{align*}
( \lambda x. \lambda y.x+y)\ 2\ 3 &\to_\beta ( \lambda y.x+y)[2/x]\ 3 \\
&=( \lambda y.2+y)\ 3 \\
&\to_\beta (2+y)[3/y] \\
&=2+3 \\
&=5
\end{align*}
$$

Questo metodo di passare molteplici parametri alla stessa [astrazione](Informatica/Lambda-calcolo/Lambda-calcolo.md#^definizione-astrazione) venne chiamato [_currying_](Informatica/Lambda-calcolo/Lambda-calcolo.md#^definizione-currying), in onore del matematico Haskell Curry per il suo apporto al [$\lambda$-calcolo](Informatica/Lambda-calcolo/Lambda-calcolo.md#^definizione-lambda-calcolo).

> [!definizione]+ Definizione: currying
> 
> Il **currying** è una tecnica che permette di [applicare](Informatica/Lambda-calcolo/Lambda-calcolo.md#^definizione-applicazione) a un'[astrazione](Informatica/Lambda-calcolo/Lambda-calcolo.md#^definizione-astrazione) con corpo ${\color{#FF7FFF} L }$ più valori ${\color{#FF7F7F} M },{\color{#7FFF7F} N },\ldots,{\color{#7F7FFF} O }$ per ognuno dei suoi argomenti ${\color{#FF7F7F} x },{\color{#7FFF7F} y },\ldots,{\color{#7F7FFF} z }$:
> 
> $$
> (\lambda {\color{#FF7F7F} x }.\lambda {\color{#7FFF7F} y }. \ldots .\lambda {\color{#7F7FFF} o }.{\color{#FF7FFF} L })\ {\color{#FF7F7F} M }\ {\color{#7FFF7F} N }\ \ldots\ {\color{#7F7FFF} O } \Leftrightarrow {\color{#FF7FFF} L } [{\color{#FF7F7F} M } / {\color{#FF7F7F} x }][{\color{#7FFF7F} N } / {\color{#7FFF7F} y }]\ldots[{\color{#7F7FFF} O } / {\color{#7F7FFF} z }]
> $$
^definizione-currying

---

%% 
https://twiki.di.uniroma1.it/pub/TPFI/MaterialiDidattici/02-lambda.pdf

- Il seguente articolo, scritto in modo molto chiaro e accessibile, fornisce dettagli sulla storia e l'evoluzione dei linguaggi funzionali e illustra le caratteristiche essenziali di questi linguaggi. L'introduzione al **λ-calcolo** iniziata questa settimana è basata su questo articolo. Il contenuto delle sezioni 3.2-3.4 è **obsoleto**, ma comunque interessante da leggere in prospettiva storica.  
    [Paul Hudak, "Conception, Evolution, and Application of Functional Programming Languages", 1989.File](https://informatica.i-learn.unito.it/mod/resource/view.php?id=271977)
- ---
- Il seguente articolo (lettura consigliata) descrive la storia e l'evoluzione di Haskell, fornendo dettagli tecnici e aneddoti sulla genesi di alcune caratteristiche del linguaggio.
    [Paul Hudak, John Hughes, Simon Peyton Jones, Philip Wadler, "A History of Haskell: Being Lazy with Class", 2007.File](https://informatica.i-learn.unito.it/mod/resource/view.php?id=271983)

- Prof. Viviana Bono, [_Note della lezione del 29 settembre_](https://informatica.i-learn.unito.it/mod/resource/view.php?id=279712)
%%

> [!fonti]+ Fonti
> 
> - 🏫 Corso di Laurea in Informatica (`L-31 R`) presso l'Università di Torino:
>     - Corso di _Linguaggi e Paradigmi di Programmazione_, A.A. 2020-21 ([pagina Moodle](https://informatica.i-learn.unito.it/enrol/index.php?id=1987)):
> 		- Prof. Luca Padovani, slide del corso:
> 			- [_Introduzione ai paradigmi di programmazione e breve storia dei linguaggi funzionali_](https://informatica.i-learn.unito.it/pluginfile.php/466243/mod_resource/content/0/storia.pdf).
> 			- [_Sintassi del $\lambda$-calcolo_](https://informatica.i-learn.unito.it/pluginfile.php/466247/mod_resource/content/0/lc_sintassi.pdf).
> 			- [_Semantica operazionale del $\lambda$-calcolo_](https://informatica.i-learn.unito.it/pluginfile.php/466251/mod_resource/content/0/lc_semantica.pdf).
> 			- [_Confluenza e strategie di riduzione_](https://informatica.i-learn.unito.it/pluginfile.php/466419/mod_resource/content/0/lc_strategie.pdf).
> 		- Prof. Luca Padovani, videoregistrazioni del corso:
> 			- [_Introduzione ai paradigmi di programmazione e breve storia dei linguaggi funzionali_](https://informatica.i-learn.unito.it/mod/url/view.php?id=271963).
> 			- [_Sintassi del $\lambda$-calcolo_](https://informatica.i-learn.unito.it/mod/url/view.php?id=271967).
> 			- [_Semantica operazionale del $\lambda$-calcolo_](https://informatica.i-learn.unito.it/mod/url/view.php?id=271971).
> 			- [_Confluenza e strategie di riduzione_](https://informatica.i-learn.unito.it/mod/url/view.php?id=272139).
>     - Corso di _Linguaggi e Paradigmi di Programmazione_, A.A. 2025-26 ([pagina Moodle](https://informatica.i-learn.unito.it/course/view.php?id=3475)):
> 		- Prof. Viviana Bono, lezioni del corso.
> - 📹 Eyesomorphic, [_Programming with Math | The Lambda Calculus_](https://www.youtube.com/watch?v=ViPNHMSUcog) su YouTube.
> - 🌐 [_Lambda-calcolo_](https://it.wikipedia.org/wiki/Lambda_calcolo) su Wikipedia in lingua italiana, [archiviato sulla Wayback Machine](https://web.archive.org/web/20251125013725/https://it.wikipedia.org/wiki/Lambda_calcolo) in data 25 novembre 2025.
> - 🌐 [_Simply typed lambda calculus_](https://en.wikipedia.org/wiki/Simply_typed_lambda_calculus) su Wikipedia in lingua inglese, [archiviato sulla Wayback Machine](https://web.archive.org/web/20251125013806/https://en.wikipedia.org/wiki/Simply_typed_lambda_calculus) in data 25 novembre 2025.
