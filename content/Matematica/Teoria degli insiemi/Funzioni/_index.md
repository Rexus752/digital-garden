---
title: Funzioni
---

> [!premessa]+ Premessa
> 
> Ciao! Se è la prima volta che capiti su questo sito, ti consiglio di consultare la [pagina principale](index.md) di questo cosiddetto _Giardino Digitale_ per scoprire meglio cos'è e come navigarlo.
> 
> Lo stato di questa nota è al momento: 🟡 <font color="#FFFF7F">_Incompleta_</font>.

---

%% 
Vedere meglio pagine 64-68 di LAncelotti
%%

# 1 - Introduzione alle funzioni

> [!definizione]+ Definizione: funzione
> 
> Una [relazione binaria](Relazioni%20tra%20insiemi.md#^definizione-relazione-n-aria) $f$ tra due [insiemi](Matematica/Teoria%20degli%20insiemi/_index.md#^osservazione-insiemi-come-elementi-di-altri-insiemi) $A$ e $B$ si dice **_funzione (o applicazione o trasformazione) da $A$ in $B$_** se:
> 1. Per ogni $a \in A$ c'è un $b \in B$ tale che $(a,b) \in f$.
> 2. Se $(a,b_1) \in f$ e $(a,b_2) \in f$, allora $b_1 = b_2$.
> 
> In questo caso scriveremo:
> 
> $$
> \begin{align*}
> f \colon A & \to B \\
> a & \mapsto b
> \end{align*}
> $$
> 
> oppure:
> 
> $$
> A \overset{f}\to B
> $$
> 
> Inoltre:
> - L'unico $b \in B$ tale che $(a,b) \in f$ si indica con "$f(a)$":
> 	$$
> 	\exists!\ b \in B\ \big( (a,b) \in f \land f(a) = b \big)
> 	$$
> - L'insieme $A$ è detto **_dominio_** della funzione e si indica con "$\text{dom}(f)$":
> 	$$
> 	\text{dom}(f) = A
> 	$$
> - L'insieme $B$ è detto **_codominio_** della funzione e si indica con "$\text{cod}(f)$":
> 	$$
> 	\text{cod}(f) = B
> 	$$
^definizione-funzione

%% 
separare definizioni di dominio e codominio
%%

> [!esempio]- Esempio: $\color{#7F7FFF} f \colon \mathbb{R} \to \mathbb{R}, x \mapsto x^2$
> 
> La [funzione](Matematica/Teoria%20degli%20insiemi/Funzioni/_index.md#^definizione-funzione) $f \colon \mathbb{R} \to \mathbb{R}, x \mapsto x^2$ o $f(x) = x^2$ è una funzione che associa a ogni numero reale $x$ il suo quadrato $y=x^2$. Essa è una funzione perché per ogni numero il suo quadrato è unico e non può averne altri.

> [!esempio]- Esempio: $\color{#7F7FFF} R=\{(1,2),(1,3),(2,4)\}$ non è una funzione
> Data una [relazione binaria](Relazioni%20tra%20insiemi.md#^definizione-relazione-n-aria) $R=\{(1,2),(1,3),(2,4)\}$, essa non è una [funzione](Matematica/Teoria%20degli%20insiemi/Funzioni/_index.md#^definizione-funzione) in quanto c'è un elemento del [dominio](Matematica/Teoria%20degli%20insiemi/Funzioni/_index.md#^definizione-funzione) (l'elemento $1$) che è associato a più elementi del [codominio](Matematica/Teoria%20degli%20insiemi/Funzioni/_index.md#^definizione-funzione) (gli elementi $2$ e $3$).

> [!osservazione]+ Osservazione: funzione come dipendenza tra due grandezze
> 
> Il concetto di [funzione](Matematica/Teoria%20degli%20insiemi/Funzioni/_index.md#^definizione-funzione) è il modello matematico che esprime la *dipendenza* tra due grandezze. Se una certa grandezza $Y$ dipende da un'altra grandezza $X$ e se a ogni valore di $X$ è associato un unico valore di $Y$, allora $Y$ è una funzione di $X$: in questo caso si dice che $X$ è la grandezza _indipendente_ e che $Y$ è la grandezza _dipendente_.
> 
> Un esempio molto semplice è dato dalle grandezze $X$ e $Y$ definite rispettivamente come "lunghezza del lato di un quadrato" e "area del quadrato": l'insieme dei possibili valori assunti da $X$, cioè il dominio, è $\{ x \in \mathbb{R} \mid x > 0\}$ e a ogni $x$ si associa l'area corrispondente $y=x^2$ (in opportune unità di misura), che è l'unico valore dell'area del quadrato di lato avente lunghezza $x$.
> Possiamo quindi affermare che l'area del quadrato è _funzione_ della lunghezza del suo lato, secondo la relazione:
> $$
> \forall x > 0\ \big(f(x)=x^{2}\big) 
> $$

> [!osservazione]+ Osservazione: funzione come concetto non strettamente algebrico
> 
> La nozione di "funzione" è molto generale e non si limita a considerare solo quelle funzioni che si possono scrivere esplicitamente usando le quattro operazioni aritmetiche ed altre funzioni note, come quelle trigonometriche.
> Per esempio, si può scegliere di definire una funzione del tipo:
> 
> $$
> \begin{align*}
> f \colon \mathbb{N} & \to \mathbb{N} \\
> n & \mapsto \text{l'$n$-esimo numero primo}
> \end{align*}
> $$
> 
> oppure una funzione del tipo:
> 
> $$
> \begin{align*}
> f \colon \mathbb{R} & \to \mathbb{N} \\
> x & \mapsto \text{la $127$-esima cifra di $x$ nel suo sviluppo decimale}
> \end{align*}
> $$

> [!osservazione]+ Osservazione: funzione come processo con input e output
> 
> Il concetto di funzione può essere facilmente inteso in termini di processo che, dato un certo input, fornisce un determinato output.
> 
> Una funzione $f$ è assimilabile a una macchina che prende in ingresso un valore $x$ e restituisce in uscita un unico valore corrispondente $f(x)$:
> 
> $$
> x \to f(x)
> $$
> 
> Il valore in uscita si ottiene spesso mediante una procedura che specifica le operazioni da effettuare sul valore in ingresso: per esempio, per la funzione $f \colon \mathbb{R} \to \mathbb{R}$ definita come $f(x)=2x+1$, la procedura può essere descritta dalle operazioni "moltiplica per 2" e "aggiungi 1":
> 
> $$
> x \xrightarrow{\text{moltiplica per }2} 2x \xrightarrow{\text{aggiungi }1} 2x+1
> $$
> 
> %% sottolineare importanza dell'ordine: prima moltiplicazione per 2, poi aggiungere 1 %%
^osservazione-funzione-come-processo-con-input-e-output

## 1.1 - Grafico di una funzione

> [!definizione]+ Definizione: grafico di una funzione
> 
> Data una [funzione](Matematica/Teoria%20degli%20insiemi/Funzioni/_index.md#^definizione-funzione) $f \colon A \to B, x \mapsto f(x)$, si definisce ***grafico*** di $f$ il [sottoinsieme](Matematica/Teoria%20degli%20insiemi/_index.md#^definizione-sottoinsieme) $\Gamma_{f} \subseteq \mathbb{R}^{2}$ definito da:
> 
> $$
> \begin{align*}
> \Gamma_{f} & = \{(x,y)\in \mathbb{R}^{2}\mid x\in A, y=f(x)\} \\
> & = \{(x,f(x))\mid x\in A\}
> \end{align*}
> $$
> 
> cioè l'insieme delle coppie di elementi in $\mathbb{R}^{2}$ legate tra di loro dalla funzione $f$.
^definizione-grafico-di-una-funzione

%% 
Poiché il valore dell'ordinata di un punto (x, y) del grafico dipende da
quello dell'ascissa dalla relazione y = f (x), si dice che "y è funzione di x"; x è detta variabile
indipendente, y è detta variabile dipendente. Con questa scelta si ha che il dominio A \subseteq
R è rappresentato come un sottoinsieme dell'asse delle ascisse, mentre il codominio B \subseteq R `e
rappresentato come un sottoinsieme dell'asse delle ordinate.
%%

%%
Osservazione: parola "grafico"

Significa sia il sottoinsieme $\Gamma_{f} \subseteq \mathbb{R}^{2}$ delle coppie di elementi in $\mathbb{R}^{2}$ legate tra di loro dalla funzione $f$, sia la rappresentazione grafica di $f$.
%%

%% 
Rappresentazione grafica del grafico
%%

%% 
Esempi:
- 1.1.4 e 1.1.5 del libro di Analisi
%%

## 1.2 - Immagine e controimmagine

> [!definizione]+ Definizione: immagine
> 
> Data una [funzione](Matematica/Teoria%20degli%20insiemi/Funzioni/_index.md#^definizione-funzione) $f \colon A \to B, x \mapsto f(x)$:
> - L'elemento $f(x)$ è detto **_immagine di $a$ mediante $f$_** (oppure _valore di $f$ su $a$_).
> - Dato un [sottoinsieme](Matematica/Teoria%20degli%20insiemi/_index.md#^definizione-sottoinsieme) $C \subseteq A$, l'insieme degli $f(x) \in B$ associati a ogni $x \in C$, denotato con "$f(C)$", è detto **_immagine di $C$ mediante $f$_**:
> $$
> \begin{align*}
> f(C) & = \{ f(x) \in B \mid x \in C \} \\
>  & = \{ y \in B \mid \exists x \in C (f(x) = y) \}
> \end{align*}
> $$
> - Se $C=A$, l'insieme degli $f(x) \in B$ associati a ogni $x \in A$, denotato con "$\text{rng}(f)$", è detto **_immagine della funzione $f$_** (o _range di $f$_):
> $$
> \begin{align*}
> \text{rng}(f) & = \{ f(x) \in B \mid x \in A \} \\
>  & = \{ y \in B \mid \exists x \in A (f(x) = y) \}
> \end{align*}
> $$
^definizione-immagine

%% 
Slide 7-9 di Viale
%%

> [!definizione]+ Definizione: controimmagine
> 
> Data una [funzione](Matematica/Teoria%20degli%20insiemi/Funzioni/_index.md#^definizione-funzione) $f \colon A \to B, x \mapsto f(x)$:
> - L'insieme degli $x \in A$ associati a un elemento $y \in B$, denotato con $f^{-1}(y)$, è detto **_controimmagine di $y$_**:
> $$
> f^{-1}(y) = \{ x \in A \mid f(x) = y \}
> $$
> - Dato un [sottoinsieme](Matematica/Teoria%20degli%20insiemi/_index.md#^definizione-sottoinsieme) $D \subseteq B$, l'unione di tutte le controimmagini degli $x \in A$ associati a ogni $f(x) \in D$, denotato con "$f^{-1}(D)$", è detto **_controimmagine di $D$_**:
> $$
> f^{-1}(D) = \bigcup_{y \in D} f^{-1}(y)
> $$
^definizione-controimmagine

%% 
Slide 11-12 di Viale
%%

%% 
Osservazione:

Se $D=B$, l'insieme degli $x \in A$ associati a ogni $y \in B$ corrisponde al [dominio](Matematica/Teoria%20degli%20insiemi/Funzioni/_index.md#^definizione-funzione) di $f$.
%%

%% 
fare tabella riassuntiva per spiegare meglio differenza tra immagine/controimmagine dei singoli elementi/degli interi insiemi 
%%

> [!esempio]- Esempio: controimmagine di una funzione costante
> 
> Data una [funzione costante](Matematica/Teoria%20degli%20insiemi/Funzioni/_index.md#^definizione-funzione-costante) $f_\beta \colon A \to B, a \mapsto \beta$, se $T \subsetneq B$ è un sottoinsieme del codominio $B$ si ha che:
> - Se $\beta \in T$, allora $f^{-1}(T) = A$.
> - Se $\beta \notin T$, allora $f^{-1}(T) = \emptyset$.

> [!esempio]- Esempio: controimmagine di una funzione proiezione
> 
> Data una [funzione proiezione](Matematica/Teoria%20degli%20insiemi/Funzioni/_index.md#^definizione-funzione-proiezione) $p_2 \colon A \times B \to B, (a,b) \mapsto b$, allora $\forall b \in B(f^{-1}(b) = A\times\{b\})$.

> [!esempio]- Esempio: controimmagine della funzione $\color{#7F7FFF} f \colon [-1,1] \to \mathbb{R}, x \mapsto \sin(x)$
> 
> Data una funzione $f \colon [-1,1] \to \mathbb{R}, x \mapsto \sin(x)$, la controimmagine dell'insieme $\mathbb{N} \subsetneq \mathbb{R}$ dei numeri naturali è l'insieme:
> $$
> f^{-1}(\mathbb{N}) = \left\{ \ldots, -\dfrac{3\pi}{2}, -\pi, -\dfrac{\pi}{2}, 0, \dfrac{\pi}{2}, \pi, \dfrac{3\pi}{2}, \ldots \right\} = \left\{ \dfrac{n\pi}{2} \middle| n \in \mathbb{Z} \right\}
> $$

## 1.3 - Definizioni e rappresentazioni di una funzione

Ci sono diversi modi per poter definire la struttura di una [funzione](Matematica/Teoria%20degli%20insiemi/Funzioni/_index.md#^definizione-funzione), alcuni dei quali molto simili a quanto avviene per gli [insiemi](Matematica/Teoria%20degli%20insiemi/_index.md#^definizione-insieme).

### 1.3.1 - Definizione per elencazione di una funzione

> [!notazione]+ Definizione per elencazione di una funzione
> 
> Una [funzione](Matematica/Teoria%20degli%20insiemi/Funzioni/_index.md#^definizione-funzione) $f \colon A \to B$ può essere definita **per elencazione** fornendo un elenco di tutte le coppie $(a,b) \in A \times B$ tali che $(a,b) \in f$, ovvero tali che $b = f(a)$.
^definizione-per-elencazione-di-una-funzione

> [!esempio]- Esempio di definizione per elencazione di una funzione
> 
> Dati due [insiemi](Matematica/Teoria%20degli%20insiemi/_index.md#^definizione-insieme) $A = \{ a,b,c \}$ e $B = \{ 0,1 \}$, allora la lista:
> $$
> \begin{align*}
> f(a) = 0 \\
> f(b) = 1 \\
> f(c) = 0
> \end{align*}
> $$
> descrive in maniera univoca una [funzione](Matematica/Teoria%20degli%20insiemi/Funzioni/_index.md#^definizione-funzione) $f \colon A \to B$.

### 1.3.2 - Definizione per caratteristica di una funzione

> [!notazione]+ Definizione per caratteristica di una funzione
> 
> Una [funzione](Matematica/Teoria%20degli%20insiemi/Funzioni/_index.md#^definizione-funzione) $f \colon A \to B$ può essere definita **per caratteristica** fornendo una "regola" che permette di determinare i valori di $f$ su ciascun $x \in A$, ma ciò presuppone che il dominio e il codominio della funzione siano stati specificati precedentemente o facilmente intuibili dal contesto.
^definizione-per-caratteristica-di-una-funzione

> [!esempio]- Esempio di definizione per caratteristica di una funzione
> 
> Facendo finta di star lavorando esclusivamente su numeri reali, la scrittura:
> $$
> f(x) = x^2 + 3
> $$
> descrive in maniera univoca una funzione $f \colon \mathbb{R} \to \mathbb{R}$ che manda ogni $x \in \mathbb{R}$ in un $y \in \mathbb{R}$ tale che $y = f(x)$ sia uguale a $x^2 + 3$.

### 1.3.3 - Rappresentazione col piano cartesiano

%% 
spostare il piano cartesiano nelle relazioni (perché può essere generico a qualsiasi relazione) e qua citarlo solo
%%

> [!notazione]+ Rappresentazione di una funzione col piano cartesiano
> 
> Per rappresentare una [funzione](Matematica/Teoria%20degli%20insiemi/Funzioni/_index.md#^definizione-funzione) "visivamente" si usa il **piano cartesiano**, cioè un piano composto da due rette perpendicolari tra loro, dette **_assi cartesiani_**, che hanno alcune caratteristiche particolari:
> - Sono disegnate in modo che una di esse sia orizzontale e l'altra verticale.
> - Ognuna di loro rappresenta una grandezza: generalmente la retta orizzontale, detta **_asse delle ascisse_**, rappresenta i valori che può assumere la $x$, mentre la retta verticale, detta **_asse delle ordinate_**, rappresenta i valori che può assumere la $y$.
> - Sono orientate, cioè a una delle due estremità presentano una freccia che indica il verso in cui le grandezze aumentano di valore (generalmente verso destra per l'asse delle ascisse e verso l'alto per l'asse delle ordinate).
> - Il loro punto di incontro viene detto **_origine degli assi_** e viene indicato con $O$.
> - Le quattro parti in cui viene diviso il piano dagli assi prendono il nome di **_quadranti_** e, partendo da quello in alto a destra e procedendo in senso antiorario, vengono numerati da $1$ a $4$.

%%
come si disegna la funzione sul piano cartesiano?
%%

> [!esempio]- Esempio: piano cartesiano di ${\color{#7F7FFF} f(x)=3x-1 }$
> 
> Il [grafico](Matematica/Teoria%20degli%20insiemi/Funzioni/_index.md#^definizione-grafico-di-una-funzione) della [funzione](Matematica/Teoria%20degli%20insiemi/Funzioni/_index.md#^definizione-funzione) $f \colon \mathbb{R} \to \mathbb{R}, x \mapsto 3x-1$ è l'insieme $\Gamma_{f} = \{ (x,y) \in \mathbb{R}^{2} \mid y=3x-1 \}$ ed è rappresentato dalla seguente retta nel piano cartesiano:
> ![350](Pasted%20image%2020240220105837.png)

%% sostituire grafici con Geogebra %%

> [!esempio]- Esempio: ricavare le informazioni dal grafico di una funzione
> 
> Si consideri la funzione $f$ che presenta il seguente grafico:
> 
> ![350](Pasted%20image%2020240220110213.png)
> 
> Il dominio $D$ di $f$, ossia l'insieme di tutti i valori $x$ per cui esiste $f(x)$, è dato da $D = [-2;1] \cup (2;5]$.
> Si presti attenzione al fatto che $x=2$ non appartiene al dominio di $f$, infatti il pallino vuoto in corrispondenza del punto $(2,-3)$ significa che tale punto non appartiene al grafico di $f$; di conseguenza, non esistono punti sul grafico di $f$ aventi ascissa $x=2$ e, dunque, $2 \notin D$.
> 
> %%mettere il piano cartesiano dopo la definizione di immagine e mettere il link alla parola "immagine" seguente%%
> 
> Per determinare l'immagine $f(D)$ di $f$ si devono trovare tutti i possibili valori $f(x)$ al variare di $x\in D$; essi si leggono sull'asse delle ordinate e sono tutte le quote $y$ alle quali esiste un punto sul grafico di $f$. Si ha quindi $f(D) = (-3;0] \cup [2;5]$.
> 
> ![350](Pasted%20image%2020240220110901.png)

%%

### 1.3.4 - Rappresentazione grafica di funzioni con diagrammi di Venn

Slide 3-5 di Viale

o di Eulero-Venn? 

scrivere introduzione

Rappresentazione grafica di una funzione come insieme di frecce tra
diagrammi di Venn.

![](Pasted%20image%2020250111194239.png)

Rappresentazione grafica come insieme di frecce tra diagrammi di Venn di
una relazione che non è una funzione (perché non è definita su tutto A).

![](Pasted%20image%2020250111194301.png)

Rappresentazione grafica come insieme di frecce tra diagrammi di Venn di
una relazione che non è una funzione (perché c'è almeno un punto di A da
cui parte più di una freccia).

![](Pasted%20image%2020250111194319.png)

%%

# 2 - Uguaglianza di due funzioni

> [!definizione]+ Definizione: uguaglianza di due funzioni
> 
> Date due [funzioni](Matematica/Teoria%20degli%20insiemi/Funzioni/_index.md#^definizione-funzione) $f$ e $g$, sono definite **uguali** se hanno lo stesso dominio e lo stesso codominio e se $f(x) = g(x)$ per ogni elemento $x$ del dominio.
^definizione-uguaglianza-di-due-funzioni

%% 
Osservazione:
quindi il loro grafico deve coincidere
%%

> [!esempio]- Esempio: uguaglianza di due funzioni apparentemente diverse
> Date due funzioni $f(x)=3x^2-1$ e $g(x)=x^3+2x-1$ definite in $\mathbb{R}$ e con dominio $\{0,1,2\}$, ossia $f,g \colon \{0,1,2\} \to \mathbb{R}$, allora $f=g$ perché:
> - $f(0)=g(0)=-1$;
> - $f(1)=g(1)=2$;
> - $f(2)=g(2)=11$.

# 3 - Funzioni particolari

Ci sono alcune [funzioni](Matematica/Teoria%20degli%20insiemi/Funzioni/_index.md#^definizione-funzione) che hanno un comportamento particolare.

%% 
Funzione segno:
ia sgn : R \to R la funzione definita da
sgn(x) =
- -1 se x < 0
- 0 se x = 0
- 1 se x > 0.
Questa funzione è detta funzione segno e trasforma i numeri negativi in -1, 0 in se stesso
e i numeri positivi in 1.
%%

%% 
Le funzioni di questo tipo sono dette definite a tratti. Un'altra funzione definita a tratti è ϕ(x) = |x|.
%%

## 3.1 - Funzione identità

> [!definizione]+ Definizione: funzione identità
> 
> Dato un [insieme](Matematica/Teoria%20degli%20insiemi/_index.md#^definizione-insieme) $X$, la **funzione identità** $\text{id}_X$ su $X$ è la [funzione](Matematica/Teoria%20degli%20insiemi/Funzioni/_index.md#^definizione-funzione) che associa a ogni elemento di $X$ se stesso:
> 
> $$
> \begin{align*}
> \text{id}_X \colon X & \to X \\
> x & \mapsto x
> \end{align*}
> $$
^definizione-funzione-identita

%% 
fare esempio
%%

## 3.2 - Funzione costante

> [!definizione]+ Definizione: funzione costante
> 
> Dati due [insiemi](Matematica/Teoria%20degli%20insiemi/_index.md#^definizione-insieme) $A$ e $B$ non necessariamente distinti e un elemento fissato $\beta \in B$, la **funzione costante** $f_\beta$ con valore $\beta$ è la [funzione](Matematica/Teoria%20degli%20insiemi/Funzioni/_index.md#^definizione-funzione) che associa a ogni elemento di $A$ sempre lo stesso elemento $\beta$ di $B$:
> 
> $$
> \begin{align*}
> f_\beta \colon A & \to B \\
> a & \mapsto \beta
> \end{align*}
> $$
^definizione-funzione-costante

%% 
fare esempio
%%

## 3.3 - Funzione proiezione

> [!definizione]+ Definizione: funzione proiezione
> 
> Dati due [insiemi](Matematica/Teoria%20degli%20insiemi/_index.md#^definizione-insieme) $A$ e $B$, le **funzioni proiezioni** $p_1$ e $p_2$ sui singoli fattori sono le funzioni che associano a ogni coppia di valori $(a,b) \in A \times B$ uno solo dei due valori:
> 
> $$
> \begin{align*}
> p_1 \colon A & \to B \\
> (a,b) & \mapsto a
> \end{align*}
> $$
> 
> $$
> \begin{align*}
> p_2 \colon A & \to B \\
> (a,b) & \mapsto b
> \end{align*}
> $$
^definizione-funzione-proiezione

%% 
fare esempio
%%

## 3.4 - Funzione restrizione

> [!definizione]+ Definizione: funzione restrizione
> 
> Data una [funzione](Matematica/Teoria%20degli%20insiemi/Funzioni/_index.md#^definizione-funzione) $f \colon A\to B$ e un [sottoinsieme](Matematica/Teoria%20degli%20insiemi/_index.md#^definizione-sottoinsieme) $C \subseteq A$, si dice _**restrizione**_ di $f$ a $C$ la funzione $f_{\vert C}$ che restringe il dominio di $f$ a $C$:
> 
> $$
> \begin{align*}
> f_{\vert C} \colon C & \to B \\
> x & \mapsto f_{\vert C}(x)
> \end{align*}
> $$
> 
> Essa è cioè una funzione che in $C$ si comporta esattamente come la funzione originaria si comporta in $A$, ma che si "dimentica" dei punti al di fuori di quel sottoinsieme.
^definizione-funzione-restrizione

%% 
Definizione 1.3 di Lancellotti
%%

> [!esempio]- Esempio: ${\color{#7F7FFF} f|_\mathbb{N} \colon \mathbb{N} \to \mathbb{R} }$ restrizione di ${\color{#7F7FFF} f \colon \mathbb{R} \to \mathbb{R} }$
> 
> Data una funzione $f \colon \mathbb{R} \to \mathbb{R}, x \mapsto x^2$, essa si può restringere al sottoinsieme $\mathbb{N} \subsetneq \mathbb{R}$ e diventa la funzione $f|_\mathbb{N} \colon \mathbb{R} \to \mathbb{R} x \mapsto x^2$.

%% 
Esempio:
Siano f : R \to R la funzione f(x) = x2 e g : [0, +∞) \to R la funzione g(x) = x2.
Poiché dom (f )  = dom (g), allora f  = g. Inoltre, essendo dom (g) = [0, +∞) \subseteq R = dom (f ), allora
g è la restrizione di f a [0, +∞) e possiamo scrivere g = f|[0,+∞).
%%

%% 
Osservazione:
Siano A, A, A, B quattro insiemi non vuoti con A \subseteq A \subseteq A e f : A \to B.
È chiaro che esiste un'unica restrizione di f ad A, mentre in generale se A  = A esistono pi`u
estensioni, anche infinite, di f ad A.
%%

%% 
Si osservi che
dom(f|C) = C
rng(f|C) = f [C].
%%

%% 
![](Pasted%20image%2020250112010435.png)
%%

## 3.5 - Funzioni limitate

> [!definizione]+ Definizione: funzioni limitate
> 
> Data una [funzione](Matematica/Teoria%20degli%20insiemi/Funzioni/_index.md#^definizione-funzione) $f \colon D \to \mathbb{R}$ con il [dominio](Matematica/Teoria%20degli%20insiemi/Funzioni/_index.md#^definizione-funzione) $D \subseteq \mathbb{R}$, allora:
> - $f$ si dice **superiormente limitata su $D$** se esiste un valore $M \in \mathbb{R}$ tale che:
> 	$$
> 	\exists M \in \mathbb{R}, \forall x \in D \big( f(x) \le M \big)
> 	$$
> - $f$ si dice **inferiormente limitata** su $D$ se esiste un valore $m \in \mathbb{R}$ tale che:
> 	$$
> 	\exists m \in \mathbb{R}, \forall x \in D \big( f(x) \ge m \big)
> 	$$
> - $f$ si dice **limitata** su $D$ se è sia superiormente sia inferiormente limitata su $D$, ossia se esistono due valori $m,M \in \mathbb{R}$ tali che:
> 	$$
> 	\exists m, M \in \mathbb{R}, \forall x \in D \big( m \le f(x) \le M \big)
> 	$$
^definizione-funzioni-limitate

%% 
Esempio di funzioni limitate dal punto di vista grafico (definizione 1.1.3 a pagina 8 del libro di Analisi)
%%

## 3.6 - Funzioni pari e dispari

> [!definizione]+ Definizione: funzioni pari e dispari
> 
> Data una [funzione](Matematica/Teoria%20degli%20insiemi/Funzioni/_index.md#^definizione-funzione) $f \colon D \to \mathbb{R}$ con il [dominio](Matematica/Teoria%20degli%20insiemi/Funzioni/_index.md#^definizione-funzione) $D \subseteq \mathbb{R}$, allora:
> - $f$ si dice **pari** se:
> 	$$
> 	\forall x \in D \big( f(-x) = f(x) \big) 
> 	$$
> - $f$ si dice **dispari** se:
> 	$$
> 	\forall x \in D \big( f(-x) = -f(x) \big) 
> 	$$
^definizione-funzioni-pari-e-dispari

> [!osservazione]+ Osservazione: simmetria dei grafici di funzioni pari e dispari
> 
> In termini di [grafico](Matematica/Teoria%20degli%20insiemi/Funzioni/_index.md#^definizione-grafico-di-una-funzione) $\Gamma_f$ di $f$ è semplice osservare che, per una [funzione pari](Matematica/Teoria%20degli%20insiemi/Funzioni/_index.md#^definizione-funzioni-pari-e-dispari), vale
> 
> $$
> (x,y) \in \Gamma_f \iff (-x,y) \in \Gamma_f
> $$
> 
> mentre, per una [funzione dispari](Matematica/Teoria%20degli%20insiemi/Funzioni/_index.md#^definizione-funzioni-pari-e-dispari), vale
> 
> $$
> (x,y) \in \Gamma_f \iff (-x,-y) \in \Gamma_f
> $$
> 
> Questo significa che il grafico%% link grafico grafico %% di una [funzione pari](Matematica/Teoria%20degli%20insiemi/Funzioni/_index.md#^definizione-funzioni-pari-e-dispari) è simmetrico rispetto all'asse delle ordinate%% link %%, mentre il grafico%% link grafico grafico %% di una [funzione dispari](Matematica/Teoria%20degli%20insiemi/Funzioni/_index.md#^definizione-funzioni-pari-e-dispari) è simmetrico rispetto all'origine.

%% esempio definizione 1.1.5 pagina 11 del libro di Analisi %%

## 3.7 - Funzioni periodiche

> [!definizione]+ Definizione: funzione periodica
> 
> Data una [funzione](Matematica/Teoria%20degli%20insiemi/Funzioni/_index.md#^definizione-funzione) $f \colon D \to \mathbb{R}$ con il [dominio](Matematica/Teoria%20degli%20insiemi/Funzioni/_index.md#^definizione-funzione) $D \subseteq \mathbb{R}$, $f$ si dice **periodica** se esiste un $T > 0$, detto **periodo di $f$**, tale che:
> 1. l'insieme $D$ soddisfa la proprietà
> 	$$
> 	x \in D \iff x + T \in D
> 	$$
> 	e
> 2. vale la relazione
> 	$$
> 	\forall x \in D \big( f(x+T) = f(x) \big) 
> 	$$
^definizione-funzione-periodica

> [!osservazione]+ Osservazione: grafico di una funzione periodica
> 
> È semplice osservare che il grafico%% link grafico grafico %% di una [funzione periodica](Matematica/Teoria%20degli%20insiemi/Funzioni/_index.md#^definizione-funzione-periodica) $f$ di periodo $T$ è invariante per traslazioni orizzontali di ampiezza $T$: questo significa che è sufficiente tracciare il grafico di $f$ su un intervallo di lunghezza $T$ e ripeterlo infinite volte a destra e a sinistra dell'intervallo considerato.

# 4 - Iniettività, suriettività e biettività

## 4.1 - Iniettività

> [!definizione]+ Definizione: iniettività
> 
> Una [funzione](Matematica/Teoria%20degli%20insiemi/Funzioni/_index.md#^definizione-funzione) $f \colon A \to B$ si dice che è _**iniettiva**_ o che è una _**iniezione**_ se, per ogni scelta di due numeri $a_1, a_2 \in A$ con $a_1 \ne a_2$, si ha $f(a_1) \ne f(a_2)$:
> $$
> \forall a_1, a_2 \in A (a_1 \ne a_2 \implies f(a_1) \ne f(a_2))
> $$
^definizione-iniettivita

> [!esempio]- Esempio: esempio grafico dell'iniettività
> 
> Un esempio grafico dell'iniettività è il seguente, in cui ogni elemento dell'insieme $A=\{2,4,6\}$ è associato a un solo elemento dell'insieme $B=\{9,7,5,3\}$:
> ![[Iniettività.png]]

%%
La rappresentazione mediante diagrammi di Venn di una funzione iniettiva
f : A \to B è tale che ogni punto di B è raggiunto al più da una freccia.
%%

> [!esempio]- Esempio: iniettività della funzione $\color{#7F7FFF} f\colon \mathbb{Z}\to\mathbb{Z},n\mapsto2n+1$
> 
> Data una funzione $f\colon \mathbb{Z}\to\mathbb{Z},n\mapsto2n+1$, essa è iniettiva. Infatti, dati due interi $m\ne n$ si ha certamente $f(m)=2m+1\ne f(n)=2n+1$.

> [!esempio]- Esempio: non-iniettività della funzione $\color{#7F7FFF} f\colon\mathbb{R}\to\mathbb{R},x\mapsto x^2$
> Data una funzione $f\colon\mathbb{R}\to\mathbb{R},x\mapsto x^2$, essa non è iniettiva. Infatti, si ha $f(1)=f(-1)=1$ e, più in generale, $\forall x \in \mathbb{R}(f(x)=f(-x))$.

> [!esempio]- Esempio: iniettività della funzione proiezione $\color{#7F7FFF} p_1\colon A\times B\to A,(a,b)\mapsto a$
> Data una funzione proiezione $p_1\colon A\times B\to A,(a,b)\mapsto a$, siccome si ha $p_1((a,b))=a$ per ogni $(a,b)\in A\times B$ la funzione è iniettiva solo se $B$ consiste di un unico elemento: se $B$ contiene due elementi distinti $b_1$ e $b_2$ allora $p_1((a,b_1))=p_1((a,b_2))$.

> [!osservazione]+ Osservazione: rendere una funzione iniettiva restringendo il dominio
> Una funzione $f\colon A\to B$ non iniettiva può diventare iniettiva [restringendo](Matematica/Teoria%20degli%20insiemi/Funzioni/_index.md#^definizione-funzione-restrizione) opportunamente il dominio. Per esempio, la funzione $f(x)=x^2$ che non è iniettiva sul dominio $\mathbb{R}$, può diventarlo se viene ristretto il dominio ai numeri reali non-negativi. Infatti, per ogni coppia di due numeri reali non-negativi distinti $x_1$ e $x_2$, si avrà sicuramente $x_1^2 \ne x_2^2$.

## 4.2 - Suriettività

> [!definizione]+ Definizione: suriettività
> Una [funzione](Matematica/Teoria%20degli%20insiemi/Funzioni/_index.md#^definizione-funzione) $f\colon A\to B$ si dice che è _**suriettiva**_ o che è una _**suriezione**_ se ogni elemento del codominio è immagine di almeno un elemento del dominio:
> $$
> \forall y \in B, \exists x \in A (f(x) = y)
> $$
^definizione-suriettivita

> [!esempio]- Esempio: esempio grafico della suriettività
> Un esempio grafico della suriettività è il seguente, in cui ogni elemento dell'insieme $B=\{9,7,5\}$ è associato ad almeno un elemento della funzione $A=\{2,4,6,8\}$:
> ![[Suriettività.png]]

%%
La rappresentazione mediante diagrammi di Venn di una funzione suriettiva
f : A \to B è tale che ogni punto di B è raggiunto almeno da una freccia.
%%

> [!esempio]- Esempio: non-suriettività della funzione $\color{#7F7FFF} f\colon\mathbb{Z}\to\mathbb{Z},x\mapsto 2x+1$
> Data una funzione $f\colon\mathbb{Z}\to\mathbb{Z},x\mapsto 2x+1$, le immagini dei singoli elementi sono sempre numeri dispari e ogni numeri intero dispari $m$ può essere scritto nella forma $\forall k \in \mathbb{Z} (m = 2k+1)$. Dunque $m=f(k)$ e si può concludere che l'immagine di $f$ è costituita dagli interi dispari ovvero $\text{rng}(f)=2\mathbb{Z}+1$. Poiché $2\mathbb{Z}+1\ne\mathbb{Z}$, la funzione $f$ non è suriettiva.

> [!esempio]- Esempio: non-suriettività della funzione $\color{#7F7FFF} f\colon\mathbb{R}\to\mathbb{R},x\mapsto x^2$
> Data una funzione $f\colon\mathbb{R}\to\mathbb{R},x\mapsto x^2$, le immagini dei singoli elementi sono sempre numeri reali non negativo e ogni reale non negativo $y$ può essere scritto nella forma $\forall x \in \mathbb{R} (y=x^2)$. Dunque $y=f(x)$ e si può concludere che l'immagine di $f$ è costituita dai numeri reali positivi, ovvero $\text{rng}(f) = \{ x \in \mathbb{R} \mid x \ge 0 \}$. Poiché $\{ x \in \mathbb{R} \mid x \ge 0 \} \ne \mathbb{R}$, la funzione $f$ non è suriettiva.

> [!esempio]- Esempio: suriettività della funzione $\color{#7F7FFF} f\colon[0,+\infty]\to\mathbb{R},x\mapsto\log(x)$
> Data una funzione $f\colon[0,+\infty]\to\mathbb{R},x\mapsto\log(x)$, ogni numero reale $r$ è il logaritmo di un altro qualsiasi numero reale $x$ (basti prendere $x=e^r$). Dunque, dato che $\text{rng}(f)=\mathbb{R}$, la funzione è suriettiva.

> [!esempio]- Esempio: suriettività della funzione proiezione $\color{#7F7FFF} p_1\colon A\times B\to A,(a,b)\mapsto a$
> Data una funzione proiezione $p_1:A\times B \to A$, poiché $B\ne\emptyset$ (se $B$ fosse vuoto allora $A\times B =A\times\emptyset=\emptyset$ e non si potrebbe parlare di funzione) e dato un $a\in A$ si può sempre scrivere $\forall b \in B(a=p_1((a,b)))$. Pertanto, ogni $a \in A$ è anche in $\text{rng}(p_1)$, quindi $A=\text{rng}(p_1)$ e $p_1$ è suriettiva.

> [!osservazione]+ Osservazione: suriettività intesa come $\color{7F7F7F} \text{rng}(f)=B$
> Un'altra definizione della suriettività è quella secondo cui la funzione $f$, per essere suriettiva, deve avere l'immagine corrispondente al codominio:
> $$
> \text{rng}(f)=B
> $$
> In questo caso, infatti, si ha che non ci sono elementi del codominio senza una controimmagine in $A$.

## 4.3 - Biettività

> [!definizione]+ Definizione: biettività
> 
> Una [funzione](Matematica/Teoria%20degli%20insiemi/Funzioni/_index.md#^definizione-funzione) $f \colon A\to B$ si dice che è _**biettiva**_ o che è una _**biezione**_ se è contemporaneamente sia [iniettiva](Matematica/Teoria%20degli%20insiemi/Funzioni/_index.md#^definizione-iniettivita) che [suriettiva](Matematica/Teoria%20degli%20insiemi/Funzioni/_index.md#^definizione-suriettivita), ovvero se per ogni elemento del codominio $y\in B$ esiste ed è unico un elemento del dominio $x \in A$ tale che $f(x)=y$:
> $$
> \forall y \in B, \exists! \, x \in A (f(x) = y)
> $$
^definizione-biettivita

> [!esempio]- Esempio: esempio grafico della biettività
> Un esempio grafico della biettività è il seguente, in cui ogni elemento dell'insieme $B=\{9,7,5,3\}$ è associato a uno e un solo elemento della funzione $A=\{2,4,6,8\}$:
> ![[Biettività.png]]

%%
La rappresentazione mediante diagrammi di Venn di una funzione biettiva
f : A \to B è tale che ogni punto di B è raggiunto esattamente da una
freccia.
%%

> [!esempio]- Esempio: biettività della funzione identità
> Per ogni insieme $A$, la [funzione identità](Matematica/Teoria%20degli%20insiemi/Funzioni/_index.md#^definizione-funzione-identita) $\text{id}_A:A\to A$ è biettiva, in quanto a ogni elemento del codominio è associato un solo elemento del dominio (ossia se stesso).

> [!esempio]- Esempio: biettività della funzione $\color{#7F7FFF} f\colon\mathbb{R} \to \mathbb{R},x\mapsto x^2$ con restringimento di dominio
> Data una funzione $f\colon\mathbb{R}\to\mathbb{R},x\mapsto x^2$, essa non è né iniettiva, né suriettiva, ma può diventare biettiva [restringendo](Matematica/Teoria%20degli%20insiemi/Funzioni/_index.md#^definizione-funzione-restrizione) il suo dominio ai numeri non-negativi $\{ x \in \mathbb{R} \mid x \ge 0 \}$ e pensandola con codominio $\{ x \in \mathbb{R} \mid x \ge 0 \}$ (se il codominio fosse $\mathbb{R}$, allora non potrebbe essere suriettiva, in quanto non ci sono numeri che, elevati alla seconda, danno numeri negativi). In questo modo, per ogni numero reale $x> 0$ esiste un solo $y> 0$ tale che $y=x^2$.

> [!esempio]- Esempio: biettività della funzione $\color{#7F7FFF} f\colon A\times B\to B\times A,(a,b)\mapsto(b,a)$
> La funzione $f\colon A\times B\to B\times A,(a,b)\mapsto(b,a)$ è una biezione. Infatti, ogni coppia $(b,a)\in B\times A$ è immagine solo di una coppia $(a,b)\in A \times B$.

%%
Osservazioni:
1 Se f : A \to A con A finito si ha che f è una biezione se e solo se f `e
una iniezione se e solo se f è una suriezione. Lo stesso vale per le
funzioni f : A \to B in cui A e B sono insiemi finiti con lo stesso
numero di elementi.
2 Se f : A \to B è iniettiva allora f : A \to rng(f ) (ovvero la stessa f ,
ma vista come funzione da A nella sua immagine) è una biezione.
3 Date f : A \to B e g : B \to C, si ha che se sia f che g sono iniettive
anche g ◦ f lo `e, e se f e g sono entrambe suriezioni anche g ◦ f lo `e.
In particolare, la composizione di due biezioni è una biezione.
4 Sia f : A \to B una funzione. Allora f è un'iniezione se e solo se
f -1(b) contiene al più un elemento per ogni b \in B, ed è una
suriezione se e solo se f -1(b) \ne \emptyset per ogni b \in B
%%

## 4.4 - Relazioni con la cardinalità

> [!proposizione]+ Proposizione: iniettività, suriettività e biettività dipendono dalla cardinalità
> Data una funzione $f\colon A\to B$, la sua iniettività, suriettività o biettività dipendono dalla sua cardinalità:
> 1. $f$ è suriettiva se e soltanto se $|f^{-1}(b)|\ge1$ per ogni $b\in B$.
> 2. $f$ è iniettiva se e soltanto se $|f^{-1}(b)|\le1$ per ogni $b\in B$.
> 3. $f$ è biettiva se e soltanto se è sia suriettiva che iniettiva, cioè se $|f^{-1}(b)| = 1$ per ogni $b \in B$.
> 
> > [!dimostrazione]- Dimostrazione
> > 
> > 1. La condizione che esista un elemento $a\in f^{-1}(b)$ (cioè che $|f^{-1}(b)|\ge1$) è equivalente, per la definizione di [controimmagine](Matematica/Teoria%20degli%20insiemi/Funzioni/_index.md#^definizione-controimmagine), alla condizione che esista un $a \in A$ tale che $f(a)=b$.
> > 
> > 2. Si può dimostrare analogamente che $f$ non è iniettiva se e soltanto se esiste un $b\in B$ tale che $|f^{-1}(b)|\ge2$, in quanto in questo caso esistono due elementi distinti $a_1\ne a_2$ nel dominio tali che $f(a_1)=f(a_2)=b$.
> > 
> > 3. Una funzione per essere biettiva deve essere sia iniettiva che suriettiva, quindi dovendo essere $|f^{-1}(b)|$ sia $\ge1$ che $\le 1$, l'unico caso che soddisfa entrambe le condizioni è $|f^{-1}(b)\vDash1$.
> >    
> > $\blacksquare$
^proposizione-iniettivita-suriettivita-e-biettivita-dipendono-dalla-cardinalita

# 5 - Composizione di funzioni

> [!definizione]+ Definizione: composizione di due funzioni
> Date due [funzioni](Matematica/Teoria%20degli%20insiemi/Funzioni/_index.md#^definizione-funzione) $f\colon A\to B$ e $g\colon B \to C$, la **composizione** di $f$ e $g$, denotata con "$g \circ f$", è la funzione:
> $$
> \begin{align*}
> g \circ f \colon A & \to C \\
> a & \mapsto g(f(a))
> \end{align*}
> $$
> È importante osservare che la composizione $g \circ f$ è definita solo se il codominio di $f$ coincide col dominio di $g$.
^definizione-composizione-di-due-funzioni

> [!osservazione]+ Osservazione: composizione rappresentata con le frecce
> La notazione "a frecce" delle funzioni permette di rappresentare semplicemente la composizione $g \circ f$ come:
> $$ A \xrightarrow{f} B \xrightarrow{g} C,\quad A \xrightarrow{g\circ f} C $$
> dove entrambi i percorsi che può seguire un elemento $a \in A$ per arrivare in $C$ danno lo stesso risultato.

> [!esempio]- Esempio: composizione di $\color{#7F7FFF} f(x)=x^2$ con $\color{#7F7FFF} g(x)=4x+1$
> Date due [funzioni](Matematica/Teoria%20degli%20insiemi/Funzioni/_index.md#^definizione-funzione) $f\colon \mathbb{R}\to \mathbb{R},f(x)=x^2$ e $g\colon \mathbb{R}\to \mathbb{R},g(x)=4x+1$, allora la [funzione composta](Matematica/Teoria%20degli%20insiemi/Funzioni/_index.md#^definizione-composizione-di-due-funzioni) $g\circ f$ è definita da
> $$
> (g\circ f)(x)=g(f(x))=4f(x)+1=4x^2+1
> $$
> Invertendo i ruoli di $f$ e $g$, è possibile definire anche la funzione composta $f\circ g$ definita da
> $$
> (f\circ g)(x)=f(g(x))=(g(x))^2=(4x+1)^2
> $$
^esempio-composizione-di-funzioni

> [!attenzione]+ Attenzione: composizione non è commutativa!
> 
> L'[esempio precedente](Matematica/Teoria%20degli%20insiemi/Funzioni/_index.md#^esempio-composizione-di-funzioni) mostra che in generale le [funzioni composte](Matematica/Teoria%20degli%20insiemi/Funzioni/_index.md#^definizione-composizione-di-due-funzioni) $g \circ f$ e $f \circ g$ non coincidono: l'operazione di composizione tra funzioni **non è commutativa**.

> [!osservazione]+ Osservazione: composizione di una funzione costante con altre funzioni
> Data una [funzione costante](Matematica/Teoria%20degli%20insiemi/Funzioni/_index.md#^definizione-funzione-costante)
> $$
> \begin{align*}
> f_\beta\colon A & \to B \\
> a & \mapsto \beta
> \end{align*}
> $$
> allora per ogni funzione $g\colon B\to C$ e per ogni funzione $h\colon D\to A$ si ha:
> 
> - $\forall a \in A \big( (g\circ f_\beta)(a)=g(\beta) \big)$.
> - $\forall d \in D \big( (f_\beta\circ h)(d)=f_\beta(h(d))=\beta \big)$.
> 
> Quindi $g \circ f_\beta\colon A\to C$ è la funzione costante $f_\beta({g(\beta)})$ e $f_\beta\circ h\colon D \to B$ è la funzione costante $f_\beta$ con dominio $D$. Dal punto di vista grafico:
> $$ D \xrightarrow{h} A \xrightarrow{f_\beta} B \xrightarrow{g} C, \quad D \xrightarrow{f_\beta} B, \quad A \xrightarrow{f(g(\beta))} C $$
> %%da confermare che sia corretto%%

%% 
Osservazione 1.1.12 di pagina 14 del libro di Analisi, mettere il grafico a centro pagina
%%

> [!esempio]- Esempio: composizione di funzioni di tempo
> 
> In un moto rettilineo, dato il tempo $t$ misurato in secondi e la posizione $y$ al tempo $t$ misurata in metri, supponiamo che $t$ e $y$ siano legate dalla relazione $y = g(t)$ con $g(t) = t^2 + t$ per ogni $t \ge 0$.
> 
> Supponiamo ora che il tempo sia riscalato in minuti, denotato stavolta con $x$, per cui vale quindi la relazione $t = f(x)$ con $f(x) = 60x$.
> 
> Ci chiediamo quale sia la relazione che intercorre tra la posizione $y$ e il tempo $x$ misurato in minuti: per rispondere a questa domanda è sufficiente sostituire l'espressione di $t$ in funzione di $x$ nella relazione $y = g(t)$; si ha quindi
> 
> $$
> \forall x \ge 0 \left(
> \begin{align*}
> y &= t^2 + t \\
> &= (60x)^2 + (60x) \\
> &= 3600x^2 + 60x
> \end{align*}
> \right) 
> $$
> 
> Abbiamo così introdotto una [funzione composta](Matematica/Teoria%20degli%20insiemi/Funzioni/_index.md#^definizione-composizione-di-due-funzioni) di $g$ ed $f$:
> 
> $$
> g(f(x)) = g \circ f
> $$

> [!attenzione]+ Attenzione: necessità di far coincidere dominio e codominio nella composizione
> 
> Consideriamo le [funzioni](Matematica/Teoria%20degli%20insiemi/Funzioni/_index.md#^definizione-funzione) $f$ e $g$ definite da
> 
> $$
> f(x) = x - 4
> $$
> 
> e
> 
> $$
> g(x) = \sqrt x
> $$
> 
> Osserviamo che la funzione $f$ è definita per ogni $x \in \mathbb{R}$, mentre la funzione $g$ è definita per ogni $x \ge 0$%% perché non è definita una funzione nelle radici %%.
> 
> Un semplice calcolo mostra che
> 
> $$
> \begin{align*}
> (g \circ f)(13) &= g(f(13)) \\
> &= \sqrt{f(13)} \\
> &= \sqrt{13-4} \\
> &= \sqrt 9 \\
> &= 3
> \end{align*}
> $$
> 
> Se però volessimo calcolare $(g \circ f)(1)$ incontreremmo un problema: infatti $f(1)=-3$ e dunque $g(f(1))$ non esiste perché $\sqrt{-3}$ non è definito in $\mathbb{R}$.
> 
> Osserviamo quindi il motivo per cui, nella [definizione di _funzione composta_](Matematica/Teoria%20degli%20insiemi/Funzioni/_index.md#^definizione-composizione-di-due-funzioni), viene richiesto che il [codominio](Matematica/Teoria%20degli%20insiemi/Funzioni/_index.md#^definizione-funzione) di $f$ debba coincidere con il dominio di $g$.

# 6 - Funzioni inverse

I valori della temperatura in gradi Celsius ($C$) e in Kelvin ($K$) sono legati dalla relazione

$$
C = K - 273.15
$$

Questa formula esprime $C$ in funzione di $K$: supponiamo ora di voler determinare $K$ in funzione di $C$, cioè ricavare il valore di $K$ a partire da un dato valore di $C$. Si tratta quindi di determinare una formula del tipo $K = g(C)$: per far questo è sufficiente ricavare $K$ dalla relazione $C = K - 273.15$. Si ottiene quindi:

$$
K = C + 273.15
$$

Abbiamo cioè ricavato la _funzione inversa_%% link %% di $f$: a partire dalla [funzione](Matematica/Teoria%20degli%20insiemi/Funzioni/_index.md#^definizione-funzione) $f$ che esprimeva la dipendenza di $C$ da $K$, data da

$$
f(K) = K - 273.15
$$

abbiamo ricavato una nuova funzione che esprime $K$ in funzione di $C$; essa si chiama _funzione inversa_%% link %% di $f$ e si denota con $f^{-1}$. Con riferimento alla funzione precedente, abbiamo dunque

$$
f^{-1}(C) = C + 273.15
$$

Osserviamo che il procedimento effettuato corrisponde alla risposta al seguente quesito: a partire da una relazione $C = f(K)$ è possibile ricavare _in modo unico_ $K$ quando è nota $C$? Si presti attenzione all'**unicità** del risultato: in questo caso $K$ è individuata in modo unico da $C$.

Alla luce di quest'ultima osservazione, è facile rendersi conto che la funzione inversa di $f$ non sempre esiste: per esempio se due variabili $x$ e $y$ sono legate dalla relazione $y = f(x)$ con $f(x) = x^2$ per ogni $x \in \mathbb{R}$, allora data una certa $y$ non è possibile risalire _in modo unico_ a $x$ tale che $x^2 = y$. Infatti, se per esempio $y = 9$, esistono due valori di $x$ tali che $x^2 = 9$, ossia $+3$ e $-3$.

L'esempio precedente pone quindi il problema di capire quando sia definita la funzione inversa; una semplice riflessione suggerisce che, affinché la funzione inversa sia definita, non devono esistere due valori diversi di $x$ aventi la stessa [immagine](Matematica/Teoria%20degli%20insiemi/Funzioni/_index.md#^definizione-immagine) $f(x)$, ossia $f$ deve essere [iniettiva](Matematica/Teoria%20degli%20insiemi/Funzioni/_index.md#^definizione-iniettivita).

> [!definizione]+ Definizione: funzione inversa
> 
> Data una [funzione iniettiva](Matematica/Teoria%20degli%20insiemi/Funzioni/_index.md#^definizione-iniettivita) $f \colon A \to B$, si chiama **funzione inversa di $f$** la [funzione](Matematica/Teoria%20degli%20insiemi/Funzioni/_index.md#^definizione-funzione)
> 
> $$
> f^{-1} \colon \ \text{rng}(f) \to A
> $$
> 
> definita dalla relazione
> 
> $$
> \forall x \in A, \forall y \in \text{rng}(f) \big( x = f^{-1}(y) \iff y = f(x) \big)
> $$
> 
> La funzione $f$ è detta **invertibile su $A$**.
^definizione-funzione-inversa

%% 
esempi:
- 1.1.16 pagina 17 libro di Analisi
- 1.1.17 pagina 18 libro di Analisi
%%

# 7 - Altre caratteristiche sulle funzioni

## 7.1 - Funzione identicamente nulla

> [!definizione]+ Definizione: funzione identicamente nulla
> 
> Una [funzione](Matematica/Teoria%20degli%20insiemi/Funzioni/_index.md#^definizione-funzione) $f \colon A \to \mathbb{R}$ si dice **identicamente nulla** su un [insieme](Matematica/Teoria%20degli%20insiemi/_index.md#^definizione-insieme) $B \subseteq A$ se $f(x) = 0$ per ogni $x \in B$:
> 
> $$
> \begin{array}{}
> f \colon A \to \mathbb{R} \text{ è identicamente nulla su } B \subseteq A \\
> \Updownarrow \\
> \forall x \in B . \big( f(x) = 0 \big) 
> \end{array}
> $$
^definizione-funzione-identicamente-nulla

---

> [!fonti]+ Fonti
> 
> - 🏫 Corso di Laurea in Informatica (`L-31 R`) presso l'Università di Torino:
> 	- Corso di _Matematica Discreta, Algebra e Geometria - parte di Matematica Discreta & Algebra (parte 1) - canale C_, A.A. 2023-24 ([pagina Moodle](https://informatica.i-learn.unito.it/course/view.php?id=2750)):
> 		- Proff. Chen Yu e Terracini Lea, lezioni in aula.
> 	- Corso di _Matematica Discreta, Algebra e Geometria - parte di Algebra Lineare & Geometria (parte 2) - canale C_, A.A. 2023-24 ([pagina Moodle](https://informatica.i-learn.unito.it/course/view.php?id=2750)):
> 		- Prof. Radeschi Marco, lezioni in aula.
> 	- Corso di _Logica Matematica_, A.A. 2022-23 ([pagina Moodle](https://informatica.i-learn.unito.it/course/view.php?id=2480)):
> 		- Proff. Andretta Alessandro, Motto Ros Luca e Viale Matteo, slide:
> 			- [_2.3 - Funzioni_](https://informatica.i-learn.unito.it/pluginfile.php/336712/mod_folder/content/0/Capitolo%202%20-%20Elementi%20di%20teoria%20degli%20insiemi/2.3%20-%20Funzioni_moodle.pdf).
> - 📚 _Analisi matematica - Fare e comprendere_ di Walter Dambrosio, Zanichelli, 2018 (ISBN: `9788808220745`):
> 	- Parte I - _I concetti dell'analisi matematica_:
> 		- 1 - _Funzioni e modelli_:
> 			- 1 - _Funzioni e grafici_:
> 				- 1.1 - _Funzioni e loro rappresentazioni_.
> 				- 1.2 - _Funzione composta e funzione inversa_.
> - 📚 Sergio Lancelotti, _Lezioni di Analisi Matematica I_, Celid, 2020 (ISBN: `978-8867891979`):
> 	- Capitolo 2 - _Funzioni_:
> 		- 1 - _Nozioni preliminari_.
