
> [!premessa]+ Premessa
> 
> Ciao! Se è la prima volta che capiti su questo sito, ti consiglio di consultare la [pagina principale](index.md) di questo cosiddetto _Giardino Digitale_ per scoprire meglio cos'è e come navigarlo.
> 
> Lo stato di questa nota è al momento: 🔴 <font color="#FF7F7F">_Bozza_</font>.

---

Dal momento che il [$\lambda$-calcolo](Lambda-calcolo.md#^definizione-lambda-calcolo) è computazionalmente completo, abbiamo visto come è possibile con esso creare con esso dei veri e propri programmi, semplicemente codificando in [termini](Lambda-calcolo.md#^definizione-termine) determinati costrutti della programmazione%% link %% classica (come abbiamo fatto, per esempio, con la [codifica di Church](Codifica%20di%20Church.md#^definizione-codifica-di-church)).

Tuttavia, possiamo subito notare un problemino non trascurabile: nella [codifica di Church](Codifica%20di%20Church.md#^definizione-codifica-di-church), possiamo tranquillamente scrivere [$\lambda$-espressioni](Lambda-calcolo.md#^definizione-lambda-calcolo) che da un punto di vista puramente sintattico hanno senso, ma semanticamente no.

Per esempio, possiamo fare un'[addizione](Codifica%20di%20Church.md#^definizione-addizione-nella-codifica-di-church) tra due [valori booleani](Codifica%20di%20Church.md#^definizione-valori-booleani-nella-codifica-di-church):

$$
\text{ADD}\ \text{TRUE}\ \text{FALSE}
$$

Però questa [$\lambda$-espressione](Lambda-calcolo.md#^definizione-termine), da un punto di vista semantico, non ha senso: cosa dovrebbe significarci la somma di due valori booleani?

Allo stesso modo, possiamo provare a fare una [disgiunzione logica](Codifica%20di%20Church.md#^definizione-disgiunzione-logica-nella-codifica-di-church) tra due [numerali di Church](Codifica%20di%20Church.md#^definizione-numerale-di-church):

$$
\text{OR}\ \underline{3}\ \underline{2}
$$

Ma cosa vuole dire questa [$\lambda$-espressione](Lambda-calcolo.md#^definizione-termine)?

Proprio per questo motivo, ci serve in qualche modo _discriminare_ sulla forma che vogliamo che abbiano i nostri [termini](Lambda-calcolo.md#^definizione-termine) quando andiamo a usarli: ecco che quindi importiamo direttamente dal mondo della programmazione%% link %% la classica nozione di _tipo_%% link %% per espandere il [$\lambda$-calcolo](Lambda-calcolo.md#^definizione-lambda-calcolo) e crearne sue versioni "tipizzate", come il [$\lambda$-calcolo semplicemente tipizzato](Lambda-calcolo%20semplicemente%20tipizzato%20(STLC).md#^definizione-lambda-calcolo-semplicemente-tipizzato).

> [!definizione]+ Definizione: $\color{#FF7FFF} \lambda$-calcolo semplicemente tipizzato
> 
> Il **$\lambda$-calcolo semplicemente tipizzato** (spesso indicato anche come **$\lambda^\to$-calcolo** o con l'acronimo **STLC**, dall'inglese _**S**imply **T**yped **L**ambda **C**alculus_), è un'espansione del [$\lambda$-calcolo](Lambda-calcolo.md#^definizione-lambda-calcolo) che include i [tipi](Lambda-calcolo%20semplicemente%20tipizzato%20(STLC).md#^definizione-tipo-nel-STLC).
^definizione-lambda-calcolo-semplicemente-tipizzato

Questi [_tipi_](Lambda-calcolo%20semplicemente%20tipizzato%20(STLC).md#^definizione-tipo-nel-STLC) non sono altro che semplici "etichette" che decidiamo noi di assegnare ai [termini](Lambda-calcolo.md#^definizione-termine) per distinguere l'uso che dobbiamo farne di loro nelle nostre [$\lambda$-espressioni](Lambda-calcolo.md#^definizione-termine).

Nel [$\lambda^\to$-calcolo](Lambda-calcolo%20semplicemente%20tipizzato%20(STLC).md#^definizione-lambda-calcolo-semplicemente-tipizzato) vogliamo distinguere i [termini](Lambda-calcolo.md#^definizione-termine) solo in due categorie: quelli che rappresentano dati atomici%% link %% (come numeri, valori booleani, stringhe, ecc.) e quelli che rappresentano [funzioni](Funzioni.md#^definizione-funzione) che, dato un [termine](Lambda-calcolo.md#^definizione-termine) di un certo [tipo](Lambda-calcolo%20semplicemente%20tipizzato%20(STLC).md#^definizione-tipo-nel-STLC), restituiscono un altro [termine](Lambda-calcolo.md#^definizione-termine) di un altro [tipo](Lambda-calcolo%20semplicemente%20tipizzato%20(STLC).md#^definizione-tipo-nel-STLC).

> [!definizione]+ Definizione: tipo nel $\color{#FF7FFF} \lambda^\to$-calcolo
> 
> Nel [$\lambda^\to$-calcolo](Lambda-calcolo%20semplicemente%20tipizzato%20(STLC).md#^definizione-lambda-calcolo-semplicemente-tipizzato), un **tipo** $\tau$ è un'etichetta assegnata a un [termine](Lambda-calcolo%20semplicemente%20tipizzato%20(STLC).md#^definizione-termine-nel-stlc) che corrisponde a una stringa ben formata a partire dalla seguente grammatica espressa in BNF:
> 
> $$
> \tau ::= \alpha \mid {\color{#FF7F7F} \tau } \to {\color{#7F7FFF} \tau }
> $$
> 
> dove:
> - $\alpha$ è il **tipo atomico**, ossia un **tipo** non ulteriormente riducibile.
> - ${\color{#FF7F7F} \tau } \to {\color{#7F7FFF} \tau }$ è il **tipo funzione**, ossia un **tipo** che indica che un'[astrazione](Lambda-calcolo.md#^definizione-astrazione) prende come argomento%% link %% un [termine](Lambda-calcolo%20semplicemente%20tipizzato%20(STLC).md#^definizione-termine-nel-stlc) di tipo ${\color{#FF7F7F} \tau }$ e restituisce un [termine](Lambda-calcolo%20semplicemente%20tipizzato%20(STLC).md#^definizione-termine-nel-stlc) di tipo ${\color{#7F7FFF} \tau }$.
^definizione-tipo-nel-stlc

> [!esempio]- Esempi di tipi
> 
> Esempi di [tipo atomico](Lambda-calcolo%20semplicemente%20tipizzato%20(STLC).md#^definizione-tipo-nel-STLC) sono $\text{Bool}$ e $\text{Nat}$, da assegnare a [termini](Lambda-calcolo%20semplicemente%20tipizzato%20(STLC).md#^definizione-termine-nel-stlc) che rappresentano rispettivamente valori booleani%% link %% e numeri naturali%% link %%.
> 
> Un esempio invece di [tipo funzione](Lambda-calcolo%20semplicemente%20tipizzato%20(STLC).md#^definizione-tipo-nel-STLC) è $\text{Nat} \to \text{Bool}$, da assegnare a un'[astrazione](Lambda-calcolo.md#^definizione-astrazione) che prende come argomento un [termine](Lambda-calcolo%20semplicemente%20tipizzato%20(STLC).md#^definizione-termine-nel-stlc) di [tipo atomico](Lambda-calcolo%20semplicemente%20tipizzato%20(STLC).md#^definizione-tipo-nel-STLC) $\text{Nat}$ e restituisce un [termine](Lambda-calcolo%20semplicemente%20tipizzato%20(STLC).md#^definizione-termine-nel-stlc) di [tipo atomico](Lambda-calcolo%20semplicemente%20tipizzato%20(STLC).md#^definizione-tipo-nel-STLC) $\text{Bool}$. Per esempio, nella [codifica di Church](Codifica%20di%20Church.md#^definizione-codifica-di-church) c'è il [test per zero](Codifica%20di%20Church.md#^definizione-test-per-zero-nella-codifica-di-church) che prende come argomento un [numerale di Church](Codifica%20di%20Church.md#^definizione-numerale-di-church) (che rappresenta un numero naturale%% link %%) e restituisce un [valore booleano](Codifica%20di%20Church.md#^definizione-valori-booleani-nella-codifica-di-church).

Ecco che quindi possiamo ridefinire il [termine](Lambda-calcolo%20semplicemente%20tipizzato%20(STLC).md#^definizione-termine-nel-stlc) per includere al suo interno le costanti%% link %%, che ci aiuteranno a rappresentare i [tipi atomici](Lambda-calcolo%20semplicemente%20tipizzato%20(STLC).md#^definizione-tipo-nel-STLC).

> [!definizione]+ Definizione: termine nel $\color{#FF7FFF} \lambda^\to$-calcolo
> 
> Nel [$\lambda^\to$-calcolo](Lambda-calcolo%20semplicemente%20tipizzato%20(STLC).md#^definizione-lambda-calcolo-semplicemente-tipizzato), un **termine** $T$ (anche detto **$\lambda^\to$-termine** o **$\lambda^\to$-espressione**) è una stringa ben formata a partire dalla seguente grammatica espressa in BNF%% link %%:
> 
> $$
> T ::= x \mid c \mid (\lambda x .{\color{#7FFF7F} T }) \mid ({\color{#FF7F7F} T }\ {\color{#7F7FFF} T })
> $$
> 
> dove:
> 
> 1. $x$ è una variabile%%link%%,
> 2. $c$ è una costante%% link %%,
> 3. $(\lambda x.{\color{#7FFF7F} T })$ è un'[astrazione](Lambda-calcolo.md#^definizione-astrazione) con argomento $x$ e corpo $\color{#7FFF7F} T$ e
> 4. $({\color{#FF7F7F} T }\ {\color{#7F7FFF} T })$ è un'[applicazione](Lambda-calcolo.md#^definizione-applicazione) in cui la [funzione](Lambda-calcolo.md#^definizione-astrazione) $\color{#FF7F7F} T$ viene applicata all'argomento $\color{#7F7FFF} T$.
> 
> Ognuna di queste 4 forme che può assumere un **termine** è detta **forma sintattica**.
^definizione-termine-nel-stlc

Nel [$\lambda$-calcolo semplicemente tipizzato](Lambda-calcolo%20semplicemente%20tipizzato%20(STLC).md#^definizione-lambda-calcolo-semplicemente-tipizzato), l'avverbio _semplicemente_ indica che, a differenza di altri varianti tipizzate del [$\lambda$-calcolo](Lambda-calcolo.md#^definizione-lambda-calcolo), in questa decidiamo di adottare solamente il [tipo atomico](Lambda-calcolo%20semplicemente%20tipizzato%20(STLC).md#^definizione-tipo-nel-STLC) e il [tipo funzione](Lambda-calcolo%20semplicemente%20tipizzato%20(STLC).md#^definizione-tipo-nel-STLC) e nient'altro.

# 1 - Giudizi sui tipi

Il motivo per cui abbiamo introdotto questa nozione di [_tipi_](Lambda-calcolo%20semplicemente%20tipizzato%20(STLC).md#^definizione-tipo-nel-STLC) è per determinare se un [termine](Lambda-calcolo%20semplicemente%20tipizzato%20(STLC).md#^definizione-termine-nel-stlc), oltre a essere sintatticamente corretto, lo è anche dal punto di vista semantico.

Questo lo controlleremo attraverso dei [_giudizi_](Lambda-calcolo%20semplicemente%20tipizzato%20(STLC).md#^definizione-giudizio), ossia proposizioni logiche in cui affermiamo che un [termine](Lambda-calcolo%20semplicemente%20tipizzato%20(STLC).md#^definizione-termine-nel-stlc) $M$ ha [tipo](Lambda-calcolo%20semplicemente%20tipizzato%20(STLC).md#^definizione-tipo-nel-STLC) $t$ e le esprimeremo nella seguente notazione:

$$
\vdash M \colon t
$$

C'è solo un problemino: questo [termine](Lambda-calcolo%20semplicemente%20tipizzato%20(STLC).md#^definizione-termine-nel-stlc) $M$ potrebbe contenere al proprio interno delle [variabili libere](Lambda-calcolo.md#^definizione-variabili-libere-e-legate) e, di conseguenza, per capire qual è il tipo da assegnare a queste variabili non ci basta più il solo [termine](Lambda-calcolo%20semplicemente%20tipizzato%20(STLC).md#^definizione-termine-nel-stlc) $M$ ma ci serve un [_contesto_](Lambda-calcolo%20semplicemente%20tipizzato%20(STLC).md#^definizione-contesto) che ci aiuti a capirlo, sotto forma di una funzione parziale che associa a ogni variabile che usiamo nel [termine](Lambda-calcolo%20semplicemente%20tipizzato%20(STLC).md#^definizione-termine-nel-stlc) un [tipo](Lambda-calcolo%20semplicemente%20tipizzato%20(STLC).md#^definizione-tipo-nel-STLC).

> [!definizione]+ Definizione: contesto
> 
> Nel [$\lambda^\to$-calcolo](Lambda-calcolo%20semplicemente%20tipizzato%20(STLC).md#^definizione-lambda-calcolo-semplicemente-tipizzato), un **contesto** $\Gamma$ è una funzione parziale da variabili a [tipi](Lambda-calcolo%20semplicemente%20tipizzato%20(STLC).md#^definizione-tipo-nel-STLC):
> 
> $$
> \Gamma \colon \{ x,y,z,\ldots \} \rightharpoonup \{ \alpha, \tau \to \sigma \}
> $$
^definizione-contesto

%% esempio %%

Ora abbiamo tutti gli strumenti per definire formalmente un [_giudizio_](Lambda-calcolo%20semplicemente%20tipizzato%20(STLC).md#^definizione-giudizio).

> [!definizione]+ Definizione: giudizio
> 
> Nel [$\lambda^\to$-calcolo](Lambda-calcolo%20semplicemente%20tipizzato%20(STLC).md#^definizione-lambda-calcolo-semplicemente-tipizzato), un **giudizio** è una proposizione logica che asserisce che, dati dei [contesti](Lambda-calcolo%20semplicemente%20tipizzato%20(STLC).md#^definizione-contesto) $\Gamma_1, \Gamma_2, \ldots, \Gamma_n$, un [termine](Lambda-calcolo%20semplicemente%20tipizzato%20(STLC).md#^definizione-termine-nel-stlc) $M$ ha [tipo](Lambda-calcolo%20semplicemente%20tipizzato%20(STLC).md#^definizione-tipo-nel-STLC) $t$:
> 
> $$
> \Gamma_1, \Gamma_2, \ldots, \Gamma_n \vdash M \colon t
> $$
> 
> dove $\Gamma_1, \Gamma_2, \ldots, \Gamma_n$ indica l'unione%% link a UNIONE DI FUNZIONI %% dei [contesti](Lambda-calcolo%20semplicemente%20tipizzato%20(STLC).md#^definizione-contesto) $\Gamma_1, \Gamma_2, \ldots, \Gamma_n$:
> 
> $$
> \bigcup_{i=1}^n \Gamma_i
> $$
> 
> Il **giudizio** può anche non avere [contesti](Lambda-calcolo%20semplicemente%20tipizzato%20(STLC).md#^definizione-contesto) se $M$ è un [combinatore](Lambda-calcolo.md#^definizione-combinatore):
> 
> $$
> \vdash M \colon \tau
> $$
^definizione-giudizio

> [!esempio]- Esempio di giudizio
> 
> Il [giudizio](Lambda-calcolo%20semplicemente%20tipizzato%20(STLC).md#^definizione-giudizio)
> 
> $$
> \Gamma \vdash x \colon \text{Bool}
> $$
> 
> indica che la variabile $x$, nel [contesto](Lambda-calcolo%20semplicemente%20tipizzato%20(STLC).md#^definizione-contesto) $\Gamma$, ha [tipo atomico](Lambda-calcolo%20semplicemente%20tipizzato%20(STLC).md#^definizione-tipo-nel-STLC) $\text{Bool}$:
> 
> $$
> \Gamma(x) = \text{Bool}
> $$

Grazie ai [giudizi](Lambda-calcolo%20semplicemente%20tipizzato%20(STLC).md#^definizione-giudizio) possiamo determinare se un [termine](Lambda-calcolo%20semplicemente%20tipizzato%20(STLC).md#^definizione-termine-nel-stlc) è [_ben tipato_](Lambda-calcolo%20semplicemente%20tipizzato%20(STLC).md#^definizione-termine-ben-tipato) o meno, ossia se le sue componenti rispettano i loro [tipi](Lambda-calcolo%20semplicemente%20tipizzato%20(STLC).md#^definizione-tipo-nel-STLC).

> [!definizione]+ Definizione: termine ben tipato
> 
> Un [termine](Lambda-calcolo%20semplicemente%20tipizzato%20(STLC).md#^definizione-termine-nel-stlc) $T$ si dice **ben tipato** se e solo se esiste un [contesto](Lambda-calcolo%20semplicemente%20tipizzato%20(STLC).md#^definizione-contesto) $\Gamma$ e un [tipo](Lambda-calcolo%20semplicemente%20tipizzato%20(STLC).md#^definizione-tipo-nel-STLC) $\tau$ tali che:
> 
> $$
> \Gamma \vdash T \colon \tau
> $$
^definizione-termine-ben-tipato

## 1.1 - Regole di tipo

Avendo definito questi [giudizi](Lambda-calcolo%20semplicemente%20tipizzato%20(STLC).md#^definizione-giudizio) come proposizioni logiche, possiamo usare le regole di inferenza per dedurre nuovi [giudizi](Lambda-calcolo%20semplicemente%20tipizzato%20(STLC).md#^definizione-giudizio) a partire da quelli che sappiamo già per certo, in modo da poter stabilire se un [termine](Lambda-calcolo%20semplicemente%20tipizzato%20(STLC).md#^definizione-termine-nel-stlc) è [ben tipato](Lambda-calcolo%20semplicemente%20tipizzato%20(STLC).md#^definizione-termine-ben-tipato) o meno. Queste regole di inferenza le chiameremo [_regole di tipo_](Lambda-calcolo%20semplicemente%20tipizzato%20(STLC).md#^definizione-regola-di-tipo).

> [!definizione]+ Definizione: regola di tipo
> 
> Una **regola di tipo** è una regola di inferenza%% link %% che stabilisce, in base alla forma sintattica%% link %% di un [termine](Lambda-calcolo%20semplicemente%20tipizzato%20(STLC).md#^definizione-termine-nel-stlc) $T$ e al [tipo](Lambda-calcolo%20semplicemente%20tipizzato%20(STLC).md#^definizione-tipo-nel-STLC) dei suoi costituenti, quale [tipo](Lambda-calcolo%20semplicemente%20tipizzato%20(STLC).md#^definizione-tipo-nel-STLC) può essere assegnato all'intero [termine](Lambda-calcolo%20semplicemente%20tipizzato%20(STLC).md#^definizione-termine-nel-stlc) $T$.
> 
> Una **regola di tipo** è generalmente espressa come:
> 
> $$
> \dfrac{P_1 \quad P_2 \quad \ldots \quad P_n}{C}
> $$
> 
> dove:
> - $P_1,P_2,\ldots,P_n$ sono le **premesse**, espresse sotto forma di [giudizi](Lambda-calcolo%20semplicemente%20tipizzato%20(STLC).md#^definizione-giudizio), che indicano i [tipi](Lambda-calcolo%20semplicemente%20tipizzato%20(STLC).md#^definizione-tipo-nel-STLC) dei costituenti del [termine](Lambda-calcolo%20semplicemente%20tipizzato%20(STLC).md#^definizione-termine-nel-stlc) $T$ e
> - $C$ è la **conclusione**, espressa anch'essa sotto forma di [giudizio](Lambda-calcolo%20semplicemente%20tipizzato%20(STLC).md#^definizione-giudizio), che stabilisce il [tipo](Lambda-calcolo%20semplicemente%20tipizzato%20(STLC).md#^definizione-tipo-nel-STLC) del [termine](Lambda-calcolo%20semplicemente%20tipizzato%20(STLC).md#^definizione-termine-nel-stlc) $T$.
^definizione-regola-di-tipo

> [!definizione]+ Definizione: regola di tipo assiomatica
> 
> Una [regola di tipo](Lambda-calcolo%20semplicemente%20tipizzato%20(STLC).md#^definizione-regola-di-tipo) si dice **assiomatica** se non ha premesse ma solo la conclusione:
> 
> $$
> \dfrac{}{C}
> $$
^definizione-regola-di-tipo-assiomatica

Ogni [regola di tipo](Lambda-calcolo%20semplicemente%20tipizzato%20(STLC).md#^definizione-regola-di-tipo), a partire da un gruppo di [giudizi](Lambda-calcolo%20semplicemente%20tipizzato%20(STLC).md#^definizione-giudizio) (ossia le [premesse](Lambda-calcolo%20semplicemente%20tipizzato%20(STLC).md#^definizione-regola-di-tipo)) è in grado di generare un nuovo [giudizio](Lambda-calcolo%20semplicemente%20tipizzato%20(STLC).md#^definizione-giudizio) (la [conclusione](Lambda-calcolo%20semplicemente%20tipizzato%20(STLC).md#^definizione-regola-di-tipo)). Tuttavia, a loro volta le [premesse](Lambda-calcolo%20semplicemente%20tipizzato%20(STLC).md#^definizione-regola-di-tipo) possono essere [conclusioni](Lambda-calcolo%20semplicemente%20tipizzato%20(STLC).md#^definizione-regola-di-tipo) di altre [regole di tipo](Lambda-calcolo%20semplicemente%20tipizzato%20(STLC).md#^definizione-regola-di-tipo) precedenti, come nel caso

$$
\dfrac{
	\dfrac{
		A_1 \quad A_2
	}{
		P_1
	}
	\quad
	\dfrac{}{P_2}
	\quad
	\ldots
	\quad
	\dfrac{
		B_1 \quad B_2 \quad \ldots \quad  B_n
	}{
		P_n
	}
}{C}
$$

dove le [premesse](Lambda-calcolo%20semplicemente%20tipizzato%20(STLC).md#^definizione-regola-di-tipo) $P_1$ e $P_n$ sono a loro volta [conclusioni](Lambda-calcolo%20semplicemente%20tipizzato%20(STLC).md#^definizione-regola-di-tipo) di [regole di tipo](Lambda-calcolo%20semplicemente%20tipizzato%20(STLC).md#^definizione-regola-di-tipo) che hanno come [premesse](Lambda-calcolo%20semplicemente%20tipizzato%20(STLC).md#^definizione-regola-di-tipo), rispettivamente, i [giudizi](Lambda-calcolo%20semplicemente%20tipizzato%20(STLC).md#^definizione-giudizio) $A_1,A_2$ e $B_1,B_2,\ldots,B_n$, mentre la [premessa](Lambda-calcolo%20semplicemente%20tipizzato%20(STLC).md#^definizione-regola-di-tipo) $P_2$ è [conclusione](Lambda-calcolo%20semplicemente%20tipizzato%20(STLC).md#^definizione-regola-di-tipo) di una [regola di tipo assiomatica](Lambda-calcolo%20semplicemente%20tipizzato%20(STLC).md#^definizione-regola-di-tipo-assiomatica), non avendo [premesse](Lambda-calcolo%20semplicemente%20tipizzato%20(STLC).md#^definizione-regola-di-tipo).

Possiamo quindi costruire dei grafici a forma di _albero_%% link alla struttura dati "albero" %% che ci permettono di risalire da un determinato [giudizio](Lambda-calcolo%20semplicemente%20tipizzato%20(STLC).md#^definizione-giudizio) alle [regole di tipo assiomatiche](Lambda-calcolo%20semplicemente%20tipizzato%20(STLC).md#^definizione-regola-di-tipo-assiomatica) che ci permettono di dedurlo%% link %%: l'_albero di derivazione_.

> [!definizione]+ Definizione: albero di derivazione
> 
> Nel [$\lambda^\to$-calcolo](Lambda-calcolo%20semplicemente%20tipizzato%20(STLC).md#^definizione-lambda-calcolo-semplicemente-tipizzato), un **albero di derivazione** è una struttura ad albero%% link %% che mostra passo per passo come un certo [giudizio](Lambda-calcolo%20semplicemente%20tipizzato%20(STLC).md#^definizione-giudizio) $G$ è ottenuto applicando le [regole di tipo](Lambda-calcolo%20semplicemente%20tipizzato%20(STLC).md#^definizione-regola-di-tipo) a partire da quelle [assiomatiche](Lambda-calcolo%20semplicemente%20tipizzato%20(STLC).md#^definizione-regola-di-tipo-assiomatica). In particolare:
> - la radice%% link %% dell'albero è rappresentata dal [giudizio](Lambda-calcolo%20semplicemente%20tipizzato%20(STLC).md#^definizione-giudizio) $G$,
> - ogni nodo interno%% link %% è rappresentato da un [giudizio](Lambda-calcolo%20semplicemente%20tipizzato%20(STLC).md#^definizione-giudizio) ottenuto applicando una specifica [regola di tipo](Lambda-calcolo%20semplicemente%20tipizzato%20(STLC).md#^definizione-regola-di-tipo), in modo che i figli%% link %% del nodo siano esattamente i [giudizi](Lambda-calcolo%20semplicemente%20tipizzato%20(STLC).md#^definizione-giudizio) presenti nelle [premesse](Lambda-calcolo%20semplicemente%20tipizzato%20(STLC).md#^definizione-regola-di-tipo) della [regola di tipo](Lambda-calcolo%20semplicemente%20tipizzato%20(STLC).md#^definizione-regola-di-tipo) applicata e
> - le foglie%% link %% sono rappresentate da [regole di tipo assiomatiche](Lambda-calcolo%20semplicemente%20tipizzato%20(STLC).md#^definizione-regola-di-tipo-assiomatica).
^definizione-albero-di-derivazione

# 2 - STLC con booleani (STLCB)

Ora , seguendo quanto ho studiato nel corso di _Linguaggi e Paradigmi di Programmazione_%% link %% che ho seguito all'Università, proviamo a espandere ulteriormente il [$\lambda^\to$-calcolo](Lambda-calcolo%20semplicemente%20tipizzato%20(STLC).md#^definizione-lambda-calcolo-semplicemente-tipizzato) accettando come unico [tipo atomico](Lambda-calcolo%20semplicemente%20tipizzato%20(STLC).md#^definizione-tipo-nel-STLC) quello _booleano_.

> [!definizione]+ Definizione: $\color{#FF7FFF} \lambda^\to$-calcolo con booleani
> 
> Il **$\lambda^\to$-calcolo con booleani** (spesso indicato anche come **$\lambda^\to_\text{Bool}$-calcolo** o con l'acronimo **STLCB**, dall'inglese _**S**imply **T**yped **L**ambda **C**alculus with **B**ooleans_), è un'espansione del [$\lambda^\to$-calcolo](Lambda-calcolo%20semplicemente%20tipizzato%20(STLC).md#^definizione-lambda-calcolo-semplicemente-tipizzato) che ammette tra i [tipi atomici](Lambda-calcolo%20semplicemente%20tipizzato%20(STLC).md#^definizione-tipo-nel-STLC) unicamente il [tipo booleano](Lambda-calcolo%20semplicemente%20tipizzato%20(STLC).md#^definizione-tipo-nel-STLCB).
^definizione-lambda-calcolo-semplicemente-tipizzato-con-booleani

Ridefiniamo quindi il concetto di _tipo_.

> [!definizione]+ Definizione: tipo nel $\color{#FF7FFF} \lambda^\to_\text{Bool}$-calcolo
> 
> Nel [$\lambda^\to_\text{Bool}$-calcolo](Lambda-calcolo%20semplicemente%20tipizzato%20(STLC).md#^definizione-lambda-calcolo-semplicemente-tipizzato-con-booleani), un **tipo** $\tau$ è un'etichetta assegnata a un [termine](Lambda-calcolo%20semplicemente%20tipizzato%20(STLC).md#^definizione-termine-nel-stlcb) che corrisponde a una stringa ben formata a partire dalla seguente grammatica espressa in BNF:
> 
> $$
> \tau ::= \text{Bool} \mid {\color{#FF7F7F} \tau } \to {\color{#7F7FFF} \tau }
> $$
> 
> dove:
> - $\text{Bool}$ è il **tipo booleano**, ossia il **tipo** che possono assumere le costanti%% link %% booleane%% link %%.
> - ${\color{#FF7F7F} \tau } \to {\color{#7F7FFF} \tau }$ è il **tipo funzione**, ossia un **tipo** che indica che un'[astrazione](Lambda-calcolo.md#^definizione-astrazione) prende come argomento%% link %% un [termine](Lambda-calcolo%20semplicemente%20tipizzato%20(STLC).md#^definizione-termine-nel-stlcb) di tipo ${\color{#FF7F7F} \tau }$ e restituisce un [termine](Lambda-calcolo%20semplicemente%20tipizzato%20(STLC).md#^definizione-termine-nel-stlcb) di tipo ${\color{#7F7FFF} \tau }$.
^definizione-tipo-nel-stlcb

Nel [$\lambda^\to_\text{Bool}$-calcolo](Lambda-calcolo%20semplicemente%20tipizzato%20(STLC).md#^definizione-lambda-calcolo-semplicemente-tipizzato-con-booleani), avendo sovrascritto la [definizione di _tipo_](Lambda-calcolo%20semplicemente%20tipizzato%20(STLC).md#^definizione-tipo-nel-STLCB), dobbiamo ridefinire anche il [termine](Lambda-calcolo%20semplicemente%20tipizzato%20(STLC).md#^definizione-termine-nel-stlc), in cui però specifichiamo che gli unici valori che possono assumere le costanti%% Link %% sono solo quelli booleani%% Link %% ($\text{True}$ e $\text{False}$) e aggiungiamo una nuova [forma sintattica](Lambda-calcolo%20semplicemente%20tipizzato%20(STLC).md#^definizione-termine-nel-stlcb): quella della struttura di controllo%% link %%.

> [!definizione]+ Definizione: termine nel $\color{#FF7FFF} \lambda^\to_\text{Bool}$-calcolo
> 
> Nel [$\lambda^\to_\text{Bool}$-calcolo](Lambda-calcolo%20semplicemente%20tipizzato%20(STLC).md#^definizione-lambda-calcolo-semplicemente-tipizzato-con-booleani), un **termine** $T$ (anche detto **$\lambda^\to_\text{Bool}$-termine** o **$\lambda^\to_\text{Bool}$-espressione**) è una stringa ben formata a partire dalla seguente grammatica espressa in BNF%% link %%:
> 
> $$
> T ::=
> x
> \mid c
> \mid (\lambda x.{\color{#7FFF7F} T })
> \mid ({\color{#FF7F7F} T }\ {\color{#7F7FFF} T })
> \mid (\text{if}\ c\ {\color{#FFFF7F} T }\ {\color{#7FFFFF} T })
> $$
> 
> dove:
> 
> 1. $x$ è una variabile%%link%%,
> 2. $c$ è una costante%% link %% che può assumere come valori soltanto $\text{True}$ e $\text{False}$ ($c \in \{\text{True},\text{False}\}$),
> 3. $(\lambda x.{\color{#7FFF7F} T })$ è un'[astrazione](Lambda-calcolo.md#^definizione-astrazione) con argomento $x$ e corpo ${\color{#7FFF7F} T }$,
> 4. $({\color{#FF7F7F} T }\ {\color{#7F7FFF} T })$ è un'[applicazione](Lambda-calcolo.md#^definizione-applicazione) in cui la [funzione](Lambda-calcolo.md#^definizione-astrazione) ${\color{#FF7F7F} T }$ viene applicata all'argomento ${\color{#7F7FFF} T }$,
> 5. $(\text{if}\ c\ {\color{#FFFF7F} T }\ {\color{#7FFFFF} T })$ è una struttura di controllo in cui, se la condizione $c$ risulta vera ($c=\text{True}$), allora è uguale a ${\color{#FFFF7F} T }$, altrimenti è uguale a ${\color{#7FFFFF} T }$:
> 	$$
> 	\begin{align*}
> 	\text{if}\ \text{True}\ {\color{#FFFF7F} T }\ {\color{#7FFFFF} T } = {\color{#FFFF7F} T } \\
> 	\text{if}\ \text{False}\ {\color{#FFFF7F} T }\ {\color{#7FFFFF} T } = {\color{#7FFFFF} T }
> 	\end{align*}
> 	$$
> 
> Ognuna di queste 5 forme che può assumere un **termine** è detta **forma sintattica**.
^definizione-termine-nel-stlcb

## 2.1 - Regole di tipo nell'STLCB

Prima di tutto, dichiariamo 5 [regole di tipo](Lambda-calcolo%20semplicemente%20tipizzato%20(STLC).md#^definizione-regola-di-tipo) per le 5 [forme sintattiche](Lambda-calcolo%20semplicemente%20tipizzato%20(STLC).md#^definizione-termine-nel-stlcb) che può assumere un [termine](Lambda-calcolo%20semplicemente%20tipizzato%20(STLC).md#^definizione-termine-nel-stlcb) nel [$\lambda^\to_\text{Bool}$-calcolo](Lambda-calcolo%20semplicemente%20tipizzato%20(STLC).md#^definizione-lambda-calcolo-semplicemente-tipizzato-con-booleani).

> [!definizione]+ Definizione: regola di tipo $\color{#FF7FFF} \text{(var)}$
> 
> Sia $\Lambda^\to_\text{Bool}$ l'[insieme](Teoria%20degli%20insiemi.md#^definizione-insieme) di [termini](Lambda-calcolo%20semplicemente%20tipizzato%20(STLC).md#^definizione-termine-nel-stlcb) del [$\lambda^\to_\text{Bool}$-calcolo](Lambda-calcolo%20semplicemente%20tipizzato%20(STLC).md#^definizione-lambda-calcolo-semplicemente-tipizzato-con-booleani).
> 
> La [regola di tipo](Lambda-calcolo%20semplicemente%20tipizzato%20(STLC).md#^definizione-regola-di-tipo) $\text{(var)}$ dice che, se in un [contesto](Lambda-calcolo%20semplicemente%20tipizzato%20(STLC).md#^definizione-contesto) un [termine della forma di una variabile](Lambda-calcolo%20semplicemente%20tipizzato%20(STLC).md#^definizione-termine-nel-stlcb) $x \in \Lambda^\to$ ha [tipo](Lambda-calcolo%20semplicemente%20tipizzato%20(STLC).md#^definizione-tipo-nel-STLC) $\tau$, allora $x$ ha [tipo](Lambda-calcolo%20semplicemente%20tipizzato%20(STLC).md#^definizione-tipo-nel-STLC) $\tau$:
> 
> $$
> \dfrac{}{\Gamma, x \colon \tau \vdash x \colon \tau}
> $$
^definizione-regola-di-tipo-var

> [!definizione]+ Definizione: regola di tipo $\color{#FF7FFF} \text{(bool)}$
> 
> Sia $\Lambda^\to_\text{Bool}$ l'[insieme](Teoria%20degli%20insiemi.md#^definizione-insieme) di [termini](Lambda-calcolo%20semplicemente%20tipizzato%20(STLC).md#^definizione-termine-nel-stlcb) del [$\lambda^\to_\text{Bool}$-calcolo](Lambda-calcolo%20semplicemente%20tipizzato%20(STLC).md#^definizione-lambda-calcolo-semplicemente-tipizzato-con-booleani).
> 
> La [regola di tipo](Lambda-calcolo%20semplicemente%20tipizzato%20(STLC).md#^definizione-regola-di-tipo) $\text{(bool)}$ dice che, se in un [contesto](Lambda-calcolo%20semplicemente%20tipizzato%20(STLC).md#^definizione-contesto) un [termine della forma di una costante](Lambda-calcolo%20semplicemente%20tipizzato%20(STLC).md#^definizione-termine-nel-stlcb) $c$ è di [tipo booleano](Lambda-calcolo%20semplicemente%20tipizzato%20(STLC).md#^definizione-tipo-nel-STLCB) $\text{Bool}$, allora ha [tipo booleano](Lambda-calcolo%20semplicemente%20tipizzato%20(STLC).md#^definizione-tipo-nel-STLCB) $\text{Bool}$:
> 
> $$
> \dfrac{}{\Gamma \vdash c \colon \text{Bool}}
> $$
^definizione-regola-di-tipo-bool

> [!definizione]+ Definizione: regola di tipo $\color{#FF7FFF} \text{(astr)}$
> 
> Sia $\Lambda^\to_\text{Bool}$ l'[insieme](Teoria%20degli%20insiemi.md#^definizione-insieme) di [termini](Lambda-calcolo%20semplicemente%20tipizzato%20(STLC).md#^definizione-termine-nel-stlcb) del [$\lambda^\to_\text{Bool}$-calcolo](Lambda-calcolo%20semplicemente%20tipizzato%20(STLC).md#^definizione-lambda-calcolo-semplicemente-tipizzato-con-booleani).
> 
> La [regola di tipo](Lambda-calcolo%20semplicemente%20tipizzato%20(STLC).md#^definizione-regola-di-tipo) $\text{(astr)}$ dice che, se in un [contesto](Lambda-calcolo%20semplicemente%20tipizzato%20(STLC).md#^definizione-contesto) un [termine della forma di un'astrazione](Lambda-calcolo%20semplicemente%20tipizzato%20(STLC).md#^definizione-termine-nel-stlcb) $\lambda x.M$ avente l'argomento%% link %% $x$ con [tipo](Lambda-calcolo%20semplicemente%20tipizzato%20(STLC).md#^definizione-tipo-nel-STLC) $\sigma$ abbiamo $M$ con [tipo](Lambda-calcolo%20semplicemente%20tipizzato%20(STLC).md#^definizione-tipo-nel-STLC) $\tau$, allora l'intera [astrazione](Lambda-calcolo.md#^definizione-astrazione) $\lambda x.M$ ha [tipo funzione](Lambda-calcolo%20semplicemente%20tipizzato%20(STLC).md#^definizione-tipo-nel-STLC) $\sigma \to \tau$:
> 
> $$
> \dfrac{\Gamma, x \colon \sigma \vdash M \colon \tau}{\Gamma \vdash \lambda x.M \colon \sigma \to \tau}
> $$
^definizione-regola-di-tipo-astr

> [!definizione]+ Definizione: regola di tipo $\color{#FF7FFF} \text{(app)}$
> 
> Sia $\Lambda^\to_\text{Bool}$ l'[insieme](Teoria%20degli%20insiemi.md#^definizione-insieme) di [termini](Lambda-calcolo%20semplicemente%20tipizzato%20(STLC).md#^definizione-termine-nel-stlcb) del [$\lambda^\to_\text{Bool}$-calcolo](Lambda-calcolo%20semplicemente%20tipizzato%20(STLC).md#^definizione-lambda-calcolo-semplicemente-tipizzato-con-booleani).
> 
> La [regola di tipo](Lambda-calcolo%20semplicemente%20tipizzato%20(STLC).md#^definizione-regola-di-tipo) $\text{(app)}$ dice che, se in un [contesto](Lambda-calcolo%20semplicemente%20tipizzato%20(STLC).md#^definizione-contesto) un [termine della forma di un'applicazione](Lambda-calcolo%20semplicemente%20tipizzato%20(STLC).md#^definizione-termine-nel-stlcb) $M\ N$ abbiamo la funzione%% link %% $M$ con [tipo funzione](Lambda-calcolo%20semplicemente%20tipizzato%20(STLC).md#^definizione-tipo-nel-STLC) $\sigma \to \tau$ e l'argomento%% link %% $N$ con [tipo](Lambda-calcolo%20semplicemente%20tipizzato%20(STLC).md#^definizione-tipo-nel-STLC) $\sigma$ , allora l'intera [applicazione](Lambda-calcolo.md#^definizione-applicazione) $M\ N$ ha [tipo](Lambda-calcolo%20semplicemente%20tipizzato%20(STLC).md#^definizione-tipo-nel-STLC) $\tau$:
> 
> $$
> \dfrac{\Gamma \vdash M \colon \sigma \to \tau \quad \Gamma \vdash N \colon \sigma}{\Gamma \vdash M\ N \colon \tau}
> $$
^definizione-regola-di-tipo-app

> [!definizione]+ Definizione: regola di tipo $\color{#FF7FFF} \text{(if)}$
> 
> Sia $\Lambda^\to_\text{Bool}$ l'[insieme](Teoria%20degli%20insiemi.md#^definizione-insieme) di [termini](Lambda-calcolo%20semplicemente%20tipizzato%20(STLC).md#^definizione-termine-nel-stlcb) del [$\lambda^\to_\text{Bool}$-calcolo](Lambda-calcolo%20semplicemente%20tipizzato%20(STLC).md#^definizione-lambda-calcolo-semplicemente-tipizzato-con-booleani).
> 
> La [regola di tipo](Lambda-calcolo%20semplicemente%20tipizzato%20(STLC).md#^definizione-regola-di-tipo) $\text{(if)}$ dice che, se in un [contesto](Lambda-calcolo%20semplicemente%20tipizzato%20(STLC).md#^definizione-contesto) un [termine della forma di una struttura di controllo](Lambda-calcolo%20semplicemente%20tipizzato%20(STLC).md#^definizione-termine-nel-stlcb) $\text{if}\ c\ M\ N$ ha $c$ di [tipo booleano](Lambda-calcolo%20semplicemente%20tipizzato%20(STLC).md#^definizione-tipo-nel-STLCB) $\text{Bool}$ ed $M$ ed $N$ entrambi di [tipo](Lambda-calcolo%20semplicemente%20tipizzato%20(STLC).md#^definizione-tipo-nel-STLCB) $\tau$, allora l'intera struttura di controllo $\text{if}\ c\ M\ N$ ha [tipo](Lambda-calcolo%20semplicemente%20tipizzato%20(STLC).md#^definizione-tipo-nel-STLCB) $\tau$:
> 
> $$
> \dfrac{\Gamma \vdash c \colon \text{Bool} \quad \Gamma \vdash M \colon \tau \quad \Gamma \vdash N \colon \tau}{\Gamma \vdash \text{if}\ c\ M\ N \colon \tau}
> $$
^definizione-regola-di-tipo-if

Nonostante non abbiamo ancora tutti gli strumenti corretti per farlo, proviamo a vedere come andrebbero usate queste [regole di tipo](Lambda-calcolo%20semplicemente%20tipizzato%20(STLC).md#^definizione-regola-di-tipo) per verificare se un [termine](Lambda-calcolo%20semplicemente%20tipizzato%20(STLC).md#^definizione-termine-nel-stlcb) è [ben tipato](Lambda-calcolo%20semplicemente%20tipizzato%20(STLC).md#^definizione-termine-ben-tipato) provando a costruire un [albero di derivazione](Lambda-calcolo%20semplicemente%20tipizzato%20(STLC).md#^definizione-albero-di-derivazione) (spoiler: più avanti introdurremo un algoritmo%% link %% per farlo correttamente, l'[_algoritmo di inferenza_](Algoritmo%20di%20inferenza.md#^algoritmo-di-inferenza)).

> [!esempio]- Esempio di uso delle regole di tipo in un albero di derivazione
> 
> Prendiamo come esempio il seguente [termine](Lambda-calcolo%20semplicemente%20tipizzato%20(STLC).md#^definizione-termine-nel-stlcb):
> 
> $$
> (\lambda x.x)\ \text{True}
> $$
> 
> Assumiamo che sia [ben tipato](Lambda-calcolo%20semplicemente%20tipizzato%20(STLC).md#^definizione-termine-ben-tipato): che [tipo](Lambda-calcolo%20semplicemente%20tipizzato%20(STLC).md#^definizione-tipo-nel-STLC) avrà?
> 
> Possiamo barare un po' e notare che è un'[applicazione](Lambda-calcolo.md#^definizione-applicazione) del combinatore identità%% link %% alla costante booleana%% link %% $\text{True}$, quindi il risultato sarà proprio la costante booleana%% link %% $\text{True}$ e avrà lo stesso [tipo](Lambda-calcolo%20semplicemente%20tipizzato%20(STLC).md#^definizione-tipo-nel-STLC) di $\text{True}$, ossia il [tipo booleano](Lambda-calcolo%20semplicemente%20tipizzato%20(STLC).md#^definizione-tipo-nel-STLCB) $\text{Bool}$.
> 
> Avremo quindi il seguente [giudizio](Lambda-calcolo%20semplicemente%20tipizzato%20(STLC).md#^definizione-giudizio):
> 
> $$
> \vdash (\lambda x.x)\ \text{True} \colon \text{Bool}
> $$
> 
> Per procedere da questo [giudizio](Lambda-calcolo%20semplicemente%20tipizzato%20(STLC).md#^definizione-giudizio), basta guardare la [forma sintattica del termine](Lambda-calcolo%20semplicemente%20tipizzato%20(STLC).md#^definizione-termine-nel-stlcb): essendo un'[applicazione](Lambda-calcolo.md#^definizione-applicazione), useremo la [regola di tipo $\text{(app)}$](Lambda-calcolo%20semplicemente%20tipizzato%20(STLC).md#^definizione-regola-di-tipo-app) che dice che, affinché l'[applicazione](Lambda-calcolo.md#^definizione-applicazione) $(\lambda x.x)\ \text{True}$ sia [ben tipata](Lambda-calcolo%20semplicemente%20tipizzato%20(STLC).md#^definizione-termine-ben-tipato), la funzione%% link %% $(\lambda x.x)$ deve essere di un [tipo funzione](Lambda-calcolo%20semplicemente%20tipizzato%20(STLC).md#^definizione-tipo-nel-STLC) $\alpha \to\ ?$ dove $\alpha$ deve coincidere con il [tipo](Lambda-calcolo%20semplicemente%20tipizzato%20(STLC).md#^definizione-tipo-nel-STLC) dell'argomento%% link %% $\text{True}$ (che ha [tipo booleano](Lambda-calcolo%20semplicemente%20tipizzato%20(STLC).md#^definizione-tipo-nel-STLC) $\text{Bool}$), mentre usiamo momentaneamente $?$ come segnaposto per decidere più tardi cosa metterci lì. Avremo quindi:
> 
> $$
> \dfrac{
> 	\vdash \lambda x.x \colon \text{Bool} \to\ ?
> 	\quad 
> 	\vdash \text{True} \colon \text{Bool}
> }{
> 	\vdash (\lambda x.x)\ \text{True} \colon \text{Bool}
> }
> \text{(app)}
> $$
> 
> Il ramo della costante%% link %% $c$ possiamo subito chiuderlo usando la [regola di tipo $\text{(bool)}$](Lambda-calcolo%20semplicemente%20tipizzato%20(STLC).md#^definizione-regola-di-tipo-bool) che è [assiomatica](Lambda-calcolo%20semplicemente%20tipizzato%20(STLC).md#^definizione-regola-di-tipo-assiomatica), quindi siamo arrivati al capolinea da questo lato:
> 
> $$
> \dfrac{
> 	\vdash \lambda x.x \colon \text{Bool} \to\ ?
> 	\quad
> 	\dfrac{
> 	}{
> 		\vdash \text{True} \colon \text{Bool}
> 	}
> 	\text{(bool)}
> }{
> 	\vdash (\lambda x.x)\ \text{True} \colon \text{Bool}
> }
> \text{(app)}
> $$
> 
> Dall'altro lato, quel $?$ come segnaposto possiamo sostituirlo barando un altro po' e vedendo che, dato che l'[astrazione](Lambda-calcolo.md#^definizione-astrazione) $\lambda x.x$ è il combinatore identità%% link %%, se gli passiamo un argomento%% link %% di [tipo booleano](Lambda-calcolo%20semplicemente%20tipizzato%20(STLC).md#^definizione-tipo-nel-STLC) $\text{Bool}$ ci restituirà un risultato sempre di [tipo booleano](Lambda-calcolo%20semplicemente%20tipizzato%20(STLC).md#^definizione-tipo-nel-STLC) $\text{Bool}$:
> 
> $$
> \dfrac{
> 	\vdash \lambda x.x \colon \text{Bool} \to \text{Bool}
> 	\quad
> 	\dfrac{
> 	}{
> 		\vdash \text{True} \colon \text{Bool}
> 	}
> 	\text{(bool)}
> }{
> 	\vdash (\lambda x.x)\ \text{True} \colon \text{Bool}
> }
> \text{(app)}
> $$
> 
> Per la [regola di tipo $\text{(astr)}$], il corpo%% link %% $x$ è [ben tipato](Lambda-calcolo%20semplicemente%20tipizzato%20(STLC).md#^definizione-termine-ben-tipato) in un [contesto](Lambda-calcolo%20semplicemente%20tipizzato%20(STLC).md#^definizione-contesto) in cui l'argomento%% link %% $x$ ha [tipo](Lambda-calcolo%20semplicemente%20tipizzato%20(STLC).md#^definizione-tipo-nel-STLC) $\text{Bool}$ e ottiene [tipo](Lambda-calcolo%20semplicemente%20tipizzato%20(STLC).md#^definizione-tipo-nel-STLC) $\text{Bool}$:
> 
> $$
> \dfrac{
> 	\dfrac{
> 		x \colon \text{Bool} \vdash x \colon \text{Bool}
> 	}{
> 		\vdash \lambda x.x \colon \text{Bool} \to \text{Bool}
> 	}
> 	\text{(astr)}
> 	\quad
> 	\dfrac{
> 	}{
> 		\vdash \text{True} \colon \text{Bool}
> 	}
> 	\text{(bool)}
> }{
> 	\vdash (\lambda x.x)\ \text{True} \colon \text{Bool}
> }
> \text{(app)}
> $$
> 
> Infine, il [giudizio](Lambda-calcolo%20semplicemente%20tipizzato%20(STLC).md#^definizione-giudizio) $x \colon \text{Bool} \vdash x \colon \text{Bool}$ è frutto dell'uso della [regola di tipo $\text{(var)}$](Lambda-calcolo%20semplicemente%20tipizzato%20(STLC).md#^definizione-regola-di-tipo-var):
> 
> $$
> \dfrac{
> 	\dfrac{
> 		\dfrac{
> 		}{
> 			x \colon \text{Bool} \vdash x \colon \text{Bool}
> 		}
> 		\text{(var)}
> 	}{
> 		\vdash \lambda x.x \colon \text{Bool} \to \text{Bool}
> 	}
> 	\text{(astr)}
> 	\quad
> 	\dfrac{
> 	}{
> 		\vdash \text{True} \colon \text{Bool}
> 	}
> 	\text{(bool)}
> }{
> 	\vdash (\lambda x.x)\ \text{True} \colon \text{Bool}
> }
> \text{(app)}
> $$
> 
> Dato che anche qui siamo arrivati a usare una [regola di tipo assiomatica](Lambda-calcolo%20semplicemente%20tipizzato%20(STLC).md#^definizione-regola-di-tipo-assiomatica), abbiamo concluso qua e abbiamo dimostrato che il [termine](Lambda-calcolo%20semplicemente%20tipizzato%20(STLC).md#^definizione-termine-nel-stlcb) $(\lambda x.x)\ c$ è [ben tipato](Lambda-calcolo%20semplicemente%20tipizzato%20(STLC).md#^definizione-termine-ben-tipato) e ha [tipo booleano](Lambda-calcolo%20semplicemente%20tipizzato%20(STLC).md#^definizione-tipo-nel-STLC) $\text{Bool}$, costruendo così correttamente un [albero di derivazione](Lambda-calcolo%20semplicemente%20tipizzato%20(STLC).md#^definizione-albero-di-derivazione).
^esempio-di-uso-delle-regole-di-tipo-in-un-albero-di-derivazione

%% 
Determinare quali delle seguenti espressioni sono ben tipate, cercando di costruire per ciascuna un albero di prova:

$$
% Lambda Calculus environment 
\begin{array}{}
\lambda f.\lambda x.f\ (f\ x) \\
\lambda x.x\ x \\
\text{if}\ \text{True}\ (\lambda x.\lambda y.x)\ (\lambda x.\lambda y.y) \\
\text{if}\ \text{True}\ (\lambda x.x)\ (\lambda x.\lambda y.y) \\
((\lambda x.x)\ \text{True})\ \text{False} \\
(\lambda x.\lambda y.\lambda z.z\ x\ y)\ (\lambda x.x)\ \text{True}
\end{array}
$$

Nota: è possibile verificare le risposte chiedendo a GHCi il tipo di queste espressioni

- [Lambda calcolo con tipi semplici (soluzione degli esercizi)File](https://informatica.i-learn.unito.it/mod/resource/view.php?id=272201)
%%

## 2.2 - Proprietà dei termini ben tipati

%% 
Lemma di sostituzione e dimostrazione
![](Pasted%20image%2020251117013553.png)
%%

Se un [termine](Lambda-calcolo%20semplicemente%20tipizzato%20(STLC).md#^definizione-termine-nel-stlcb) $M$ è [ben tipato](Lambda-calcolo%20semplicemente%20tipizzato%20(STLC).md#^definizione-termine-ben-tipato) e si [riduce](Lambda-calcolo.md#^definizione-riduzione-singola) a un altro [termine](Lambda-calcolo%20semplicemente%20tipizzato%20(STLC).md#^definizione-termine-nel-stlcb) $N$, allora $M$ ed $N$ avranno lo stesso [tipo](Lambda-calcolo%20semplicemente%20tipizzato%20(STLC).md#^definizione-tipo-nel-STLC). Ciò significa quindi che la [riduzione singola](Lambda-calcolo.md#^definizione-riduzione-singola) _preserva_ il [tipo](Lambda-calcolo%20semplicemente%20tipizzato%20(STLC).md#^definizione-tipo-nel-STLC).

> [!lemma]+ Lemma di _subject reduction_
> 
> Sia $\Lambda^\to_\text{Bool}$ l'[insieme](Teoria%20degli%20insiemi.md#^definizione-insieme) di [termini](Lambda-calcolo%20semplicemente%20tipizzato%20(STLC).md#^definizione-termine-nel-stlcb) del [$\lambda^\to_\text{Bool}$-calcolo](Lambda-calcolo%20semplicemente%20tipizzato%20(STLC).md#^definizione-lambda-calcolo-semplicemente-tipizzato-con-booleani).
> Dati due [termini](Lambda-calcolo%20semplicemente%20tipizzato%20(STLC).md#^definizione-termine-nel-stlcb) $M,N \in \Lambda^\to_\text{Bool}$, se in un [contesto](Lambda-calcolo%20semplicemente%20tipizzato%20(STLC).md#^definizione-contesto) $\Gamma$ $M$ ha [tipo](Lambda-calcolo%20semplicemente%20tipizzato%20(STLC).md#^definizione-tipo-nel-STLC) $\tau$ e si [riduce](Lambda-calcolo.md#^definizione-riduzione-singola) a $N$, allora anche $N$ avrà [tipo](Lambda-calcolo%20semplicemente%20tipizzato%20(STLC).md#^definizione-tipo-nel-STLC) $\tau$ nel [contesto](Lambda-calcolo%20semplicemente%20tipizzato%20(STLC).md#^definizione-contesto) $\Gamma$:
> 
> $$
> \forall M,N \in \Lambda^\to_\text{Bool} \big( (\Gamma \vdash M \colon \tau \land M \to N) \implies (\Gamma \vdash N \colon \tau) \big)
> $$
^lemma-di-subject-reduction

%% 
Dimostrazione
![](Pasted%20image%20202511170135531.png)
%%

> [!definizione]+ Definizione: valore
> 
> Nel [$\lambda^\to_\text{Bool}$-calcolo](Lambda-calcolo%20semplicemente%20tipizzato%20(STLC).md#^definizione-lambda-calcolo-semplicemente-tipizzato-con-booleani), un **valore** è un [termine](Lambda-calcolo%20semplicemente%20tipizzato%20(STLC).md#^definizione-termine-nel-stlcb) $T$ che è della [forma semantica](Lambda-calcolo%20semplicemente%20tipizzato%20(STLC).md#^definizione-termine-nel-stlcb) di una costante booleana%% link %% o di un'[astrazione](Lambda-calcolo.md#^definizione-astrazione).
^definizione-valore

> [!esempio]- Esempi di valori
> 
> Ecco una lista di [termini](Lambda-calcolo%20semplicemente%20tipizzato%20(STLC).md#^definizione-termine-nel-stlcb) e per ognuno dei quali vediamo se sono [valori](Lambda-calcolo%20semplicemente%20tipizzato%20(STLC).md#^definizione-valore) o meno:
> - $(\lambda x.x)\ \text{True}$: **non** è un [valore](Lambda-calcolo%20semplicemente%20tipizzato%20(STLC).md#^definizione-valore) perché è un'[applicazione](Lambda-calcolo.md#^definizione-applicazione) con funzione%% link %% $\lambda x.x$ e argomento%% link %% $\text{True}$. Tuttavia, con un passaggio di [$\beta$-riduzione](Lambda-calcolo.md#^definizione-beta-riduzione), otteniamo $\text{True}$ che è una costante booleana%% link %% e diventa un [valore](Lambda-calcolo%20semplicemente%20tipizzato%20(STLC).md#^definizione-valore).
> - $\text{True}\ (\lambda x.x)$: **non** è un [valore](Lambda-calcolo%20semplicemente%20tipizzato%20(STLC).md#^definizione-valore) perché è un'[applicazione](Lambda-calcolo.md#^definizione-applicazione) con funzione%% link %% $\text{True}$ e argomento%% link %% $\lambda x.x$. È in [forma normale](Lambda-calcolo.md#^definizione-forma-normale), quindi non è [riducibile](Lambda-calcolo.md#^definizione-riduzione-singola) e non potrà mai diventare un [valore](Lambda-calcolo%20semplicemente%20tipizzato%20(STLC).md#^definizione-valore).
> - $\lambda x.x\ (\lambda y.y)$: è un [valore](Lambda-calcolo%20semplicemente%20tipizzato%20(STLC).md#^definizione-valore) perché è un'[astrazione](Lambda-calcolo.md#^definizione-astrazione) con argomento%% link %% $x$ e corpo $x\ (\lambda y.y)$.

Possiamo dimostrare che, per ogni [termine](Lambda-calcolo%20semplicemente%20tipizzato%20(STLC).md#^definizione-termine-nel-stlcb) $M$ [riducibile in zero o più passi](Lambda-calcolo.md#^definizione-riduzione-multipla) in un altro [termine](Lambda-calcolo%20semplicemente%20tipizzato%20(STLC).md#^definizione-termine-nel-stlcb) $N$ in [forma normale](Lambda-calcolo.md#^definizione-forma-normale), quest'ultimo è un [valore](Lambda-calcolo%20semplicemente%20tipizzato%20(STLC).md#^definizione-valore).

> [!teorema]+ Teorema del progresso
> 
> Sia $\Lambda^\to_\text{Bool}$ l'[insieme](Teoria%20degli%20insiemi.md#^definizione-insieme) di [termini](Lambda-calcolo%20semplicemente%20tipizzato%20(STLC).md#^definizione-termine-nel-stlcb) del [$\lambda^\to_\text{Bool}$-calcolo](Lambda-calcolo%20semplicemente%20tipizzato%20(STLC).md#^definizione-lambda-calcolo-semplicemente-tipizzato-con-booleani).
> Dati due [termini](Lambda-calcolo%20semplicemente%20tipizzato%20(STLC).md#^definizione-termine-nel-stlcb) $M,N \in \Lambda^\to_\text{Bool}$ con $M$ [combinatore](Lambda-calcolo.md#^definizione-combinatore) e $N$ in [forma normale](Lambda-calcolo.md#^definizione-forma-normale), se $M$ ha [tipo](Lambda-calcolo%20semplicemente%20tipizzato%20(STLC).md#^definizione-tipo-nel-STLC) $\tau$ ed è [riducibile in zero o più passi](Lambda-calcolo.md#^definizione-riduzione-multipla) in $N$, allora $N$ è un [valore](Lambda-calcolo%20semplicemente%20tipizzato%20(STLC).md#^definizione-valore):
> 
> $$
> \forall M,N \in \Lambda^\to_\text{Bool} \Big( \big( (\vdash M \colon \tau) \land (M \Rightarrow N \not\to) \big) \implies (N \text{ è un valore}) \Big)
> $$
^teorema-del-progresso

%% 
Dimostrazione:
![](Pasted%20image%20202511170135533.png)
%%

---

> [!fonti]+ Fonti
> 
> - 🏫 Corso di Laurea in Informatica (`L-31 R`) presso l'Università di Torino:
>     - Corso di _Linguaggi e Paradigmi di Programmazione_, A.A. 2020-21 ([pagina Moodle](https://informatica.i-learn.unito.it/enrol/index.php?id=1987)):
> 		- Prof. Luca Padovani, slide del corso:
> 			- [_Lambda calcolo con tipi_](https://informatica.i-learn.unito.it/pluginfile.php/466479/mod_resource/content/0/lc_tipi.pdf).
> 		- Prof. Luca Padovani, videoregistrazioni del corso:
> 			- [_Lambda calcolo con tipi_](https://informatica.i-learn.unito.it/mod/url/view.php?id=272199).
>     - Corso di _Linguaggi e Paradigmi di Programmazione_, A.A. 2025-26 ([pagina Moodle](https://informatica.i-learn.unito.it/course/view.php?id=3475)):
> 		- Prof. Viviana Bono, lezioni del corso.
> - 📹 Eyesomorphic, [_Programming with Math | The Lambda Calculus_](https://www.youtube.com/watch?v=ViPNHMSUcog) su YouTube.
> - 🌐 [_Lambda-calcolo_](https://it.wikipedia.org/wiki/Lambda_calcolo) su Wikipedia in lingua italiana, [archiviato sulla Wayback Machine](https://web.archive.org/web/20251125013725/https://it.wikipedia.org/wiki/Lambda_calcolo) in data 25 novembre 2025.
> - 🌐 [_Simply typed lambda calculus_](https://en.wikipedia.org/wiki/Simply_typed_lambda_calculus) su Wikipedia in lingua inglese, [archiviato sulla Wayback Machine](https://web.archive.org/web/20251125013806/https://en.wikipedia.org/wiki/Simply_typed_lambda_calculus) in data 25 novembre 2025.

%% 
https://www.math.unipd.it/~silvio/Corsi/Dispense/LambdaCalcolo.pdf
%%
