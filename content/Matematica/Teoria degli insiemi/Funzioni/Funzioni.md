
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
> Una [relazione binaria](Relazioni%20tra%20insiemi.md#^definizione-relazione-n-aria) $f$ tra due [insiemi](Teoria%20degli%20insiemi.md#^osservazione-insiemi-come-elementi-di-altri-insiemi) $A$ e $B$ si dice **_funzione_ (o _applicazione_ o _trasformazione_) _da $A$ in $B$_** se:
> 1. per ogni $a \in A$ c'è un $b \in B$ tale che $(a,b) \in f$ e
> 2. se $(a,b_1) \in f$ e $(a,b_2) \in f$, allora $b_1 = b_2$.
> 
> Si indica con "$f \colon A \to B$" o, più precisamente,
> 
> $$
> \begin{align*}
> f \colon A & \to B \\
> a & \mapsto b
> \end{align*}
> $$
> 
> dove:
> - $a$ indica la **variabile%% link %% indipendente** e
> - $b$ indica la **variabile%% link %% dipendente** o la trasformazione che subisce la $a$.
> 
> Inoltre, l'unico $b \in B$ tale che $(a,b) \in f$ si indica con "$f(a)$":
> $$
> \exists!\ b \in B\ \big( (a,b) \in f \land f(a) = b \big)
> $$
^definizione-funzione

> [!definizione]+ Definizione: dominio e codominio della funzione
> 
> In una [funzione](Funzioni.md#^definizione-funzione) $f \colon A \to B$, l'[insieme](Teoria%20degli%20insiemi.md#^definizione-insieme) $A$ è detto **dominio della funzione** (o, più semplicemente, **dominio**) e viene indicato con "$\text{dom}(f)$":
> 
> $$
> \text{dom}(f) = A
> $$
> 
> L'[insieme](Teoria%20degli%20insiemi.md#^definizione-insieme) $B$, invece, è detto **codominio della funzione** (o, più semplicemente, **codominio**) e viene indicato con "$\text{cod}(f)$":
> 
> $$
> \text{cod}(f) = B
> $$
^definizione-dominio-e-codominio-della-funzione

> [!esempio]- Esempio di funzione
> 
> Un esempio di [funzione](Funzioni.md#^definizione-funzione) è $f \colon \mathbb{R} \to \mathbb{R}$ che associa a ogni numero reale%% link %% $x \in \mathbb{R}$ il suo quadrato $x^2 \in \mathbb{R}$. Essa è una funzione perché per ogni numero il suo quadrato è unico e non può averne altri.
^esempio-di-funzione

> [!esempio]- Esempio: $\color{#7F7FFF} R=\{(1,2),(1,3),(2,4)\}$ non è una funzione
> 
> Data una [relazione binaria](Relazioni%20tra%20insiemi.md#^definizione-relazione-n-aria) $R=\{(1,2),(1,3),(2,4)\}$, essa non è una [funzione](Funzioni.md#^definizione-funzione) perché c'è un elemento del [dominio](Funzioni.md#^definizione-dominio-e-codominio-della-funzione) che è associato a più elementi del [codominio](Funzioni.md#^definizione-dominio-e-codominio-della-funzione).

> [!osservazione]+ Osservazione: funzione come dipendenza tra due grandezze
> 
> Il concetto di [funzione](Funzioni.md#^definizione-funzione) è un modello matematico usato per esprimere la *dipendenza* tra due grandezze. Se una certa grandezza $Y$ dipende da un'altra grandezza $X$ e se a ogni valore di $X$ è associato un unico valore di $Y$, allora $Y$ è una funzione di $X$: in questo caso si dice che $X$ è la grandezza _indipendente_ e che $Y$ è la grandezza _dipendente_.
> 
> Un esempio molto semplice è dato dalle grandezze $X$ e $Y$ definite rispettivamente come "lunghezza del lato di un quadrato" e "area del quadrato": l'insieme dei possibili valori assunti da $X$, cioè il dominio, è $\{ x \in \mathbb{R} \mid x > 0\}$ e a ogni $x$ si associa l'area corrispondente $y=x^2$ (in opportune unità di misura), che è l'unico valore dell'area del quadrato di lato avente lunghezza $x$.
> Possiamo quindi affermare che l'area del quadrato è _funzione_ della lunghezza del suo lato, secondo la relazione:
> $$
> \forall x > 0\ \big(f(x)=x^{2}\big) 
> $$

> [!notazione]+ Notazioni alternative per una funzione
> 
> Una [funzione](Funzioni.md#^definizione-funzione) $f \colon A \to B$ si può anche indicare in altri modi:
> - Possiamo usare la notazione "completa"
> 	
> 	$$
> 	\begin{align*}
> 	f \colon A & \to B \\
> 	a & \mapsto b
> 	\end{align*}
> 	$$
> 	
> 	ma in riga (in inglese _inline_), cioè
> 	
> 	$$
> 	f \colon A \to B, a \mapsto b
> 	$$
> 
> - Possiamo usare quest'altra notazione che sottolinea il fatto che una [funzione](Funzioni.md#^definizione-funzione) è una _trasformazione_ di un oggetto $a \in A$ in un altro oggetto $b \in B$:
> 
> 	$$
> 	A \overset{f}\to B
> 	$$
> 
> - Possiamo indicare direttamente la trasformazione che applichiamo sull'oggetto (come già scritto nella [definizione di _funzione_](Funzioni.md#^definizione-funzione)). Per esempio, nell'[esempio di prima](Funzioni.md#^esempio-di-funzione), la [funzione](Funzioni.md#^definizione-funzione) $f \colon \mathbb{R} \to \mathbb{R}$ che prende un $x \in \mathbb{R}$ e ne restituisce il suo quadrato $x^2 \in \mathbb{R}$ si può indicare come
> 
> 	$$
> 	\begin{align*}
> 	f \colon \mathbb{R} & \to \mathbb{R} \\
> 	x & \mapsto x^2
> 	\end{align*}
> 	$$
> 	
> 	oppure come
> 	
> 	$$
> 	f(x) = x^2
> 	$$

> [!notazione]+ Notazione: dominio e codominio sottintesi
> 
> Quando una [funzione](Funzioni.md#^definizione-funzione) è indicata solo attraverso la sua "trasformazione" (per esempio $f(x) = x^2$), si dà per scontato che la [funzione](Funzioni.md#^definizione-funzione) abbia come [codominio](Funzioni.md#^definizione-dominio-e-codominio-della-funzione) l'insieme dei numeri reali%% link %% $\mathbb{R}$, mentre come [dominio](Funzioni.md#^definizione-dominio-e-codominio-della-funzione) non $\mathbb{R}$ ma un [sottoinsieme](Teoria%20degli%20insiemi.md#^definizione-insieme) di $\mathbb{R}$ che corrisponde a tutti e soli i punti%% link %% su cui la [funzione](Funzioni.md#^definizione-funzione) è definita che viene solitamente indicato direttamente con "$\text{dom}(f)$"):
> 
> $$
> f \colon \text{dom}(f) \to \mathbb{R}
> $$
> 
> Il [dominio](Funzioni.md#^definizione-dominio-e-codominio-della-funzione) non può essere "generalizzato" ponendolo uguale a $\mathbb{R}$ perché ciò significherebbe che la [funzione](Funzioni.md#^definizione-funzione) è definita su tutto $\mathbb{R}$, ma ciò non è sempre vero: molte funzioni, per esempio $f(x) = \dfrac{1}{x}$ o $f(x) = \sqrt x$ sono definite solo su alcuni punti%% Link %% di $\mathbb{R}$ (es. $f(x) = \dfrac{1}{x}$ è definita su $\mathbb{R} \setminus \{ 0 \}$, mentre $f(x) = \sqrt x$ è definita solo sui reali positivi%% link %% $\mathbb{R}^{\ge0}$).
> 
> Ecco perché userò spesso la notazione "$f \colon \text{dom}(f) \to \mathbb{R}$" per indicare una [funzione](Funzioni.md#^definizione-funzione) generica.

> [!osservazione]+ Osservazione: funzione come concetto non strettamente algebrico
> 
> La nozione di [_funzione_](Funzioni.md#^definizione-funzione) è molto generale e non si limita a considerare solo quelle funzioni che si possono scrivere esplicitamente in modi strettamente "matematici". Per esempio, si può scegliere di definire una [funzione](Funzioni.md#^definizione-funzione) del tipo:
> 
> $$
> \begin{align*}
> f \colon \mathbb{N} & \to \mathbb{N} \\
> n & \mapsto \text{l'$n$-esimo numero primo}
> \end{align*}
> $$
> 
> oppure una [funzione](Funzioni.md#^definizione-funzione) del tipo:
> 
> $$
> \begin{align*}
> f \colon \mathbb{R} & \to \mathbb{N} \\
> x & \mapsto \text{la $127$-esima cifra di $x$ nel suo sviluppo decimale}
> \end{align*}
> $$

> [!osservazione]+ Osservazione: funzione come processo con input e output
> 
> Il concetto di [_funzione_](Funzioni.md#^definizione-funzione) può essere facilmente inteso in termini di processo che, dato un certo input, fornisce un determinato output.
> 
> Una [funzione](Funzioni.md#^definizione-funzione) $f$ è assimilabile a una macchina che prende in ingresso un valore $x$ e restituisce in uscita un unico valore corrispondente $f(x)$:
> 
> $$
> \boxed x \to \boxed{f(x)}
> $$
> 
> Il valore in uscita si ottiene spesso mediante una procedura che specifica le operazioni da effettuare sul valore in ingresso: per esempio, per la funzione $f \colon \mathbb{R} \to \mathbb{R}$ definita come $f(x)=2x+1$, la procedura può essere descritta dalle operazioni "moltiplica per 2" e "aggiungi 1":
> 
> $$
> \boxed x \xrightarrow{\text{moltiplica per }2} \boxed{2x} \xrightarrow{\text{aggiungi }1} \boxed{2x+1}
> $$
> 
> %% sottolineare importanza dell'ordine: prima moltiplicazione per 2, poi aggiungere 1 %%
^osservazione-funzione-come-processo-con-input-e-output

## 1.1 - Grafico di una funzione

> [!definizione]+ Definizione: grafico di una funzione
> 
> Data una [funzione](Funzioni.md#^definizione-funzione) $f \colon A \to B$, si definisce ***grafico*** di $f$ il [sottoinsieme](Teoria%20degli%20insiemi.md#^definizione-sottoinsieme) $\Gamma_{f} \subseteq \mathbb{R}^{2}$ definito da:
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
- 1.1.4 e 1.1.5 pag. 6-7 Dambrosio
%%

## 1.2 - Immagine e controimmagine

> [!definizione]+ Definizione: immagine
> 
> Data una [funzione](Funzioni.md#^definizione-funzione) $f \colon A \to B, x \mapsto f(x)$:
> - L'elemento $f(x)$ è detto **_immagine di $a$ mediante $f$_** (oppure **_valore di $f$ su $a$_**).
> - Dato un [sottoinsieme](Teoria%20degli%20insiemi.md#^definizione-sottoinsieme) $C \subseteq A$, l'insieme degli $f(x) \in B$ associati a ogni $x \in C$, denotato con "$f(C)$", è detto **_immagine di $C$ mediante $f$_**:
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
> Data una [funzione](Funzioni.md#^definizione-funzione) $f \colon A \to B, x \mapsto f(x)$:
> - L'insieme degli $x \in A$ associati a un elemento $y \in B$, denotato con $f^{-1}(y)$, è detto **_controimmagine di $y$_**:
> $$
> f^{-1}(y) = \{ x \in A \mid f(x) = y \}
> $$
> - Dato un [sottoinsieme](Teoria%20degli%20insiemi.md#^definizione-sottoinsieme) $D \subseteq B$, l'unione di tutte le controimmagini degli $x \in A$ associati a ogni $f(x) \in D$, denotato con "$f^{-1}(D)$", è detto **_controimmagine di $D$_**:
> $$
> f^{-1}(D) = \bigcup_{y \in D} f^{-1}(y)
> $$
^definizione-controimmagine

%% 
Slide 11-12 di Viale
%%

%% 
Osservazione:

Se $D=B$, l'insieme degli $x \in A$ associati a ogni $y \in B$ corrisponde al [dominio](Matem[dominio](Funzioni.md#^definizione-funzione) 
fare tabella riassuntiva per spiegare meglio differenza tra immagine/controimmagine dei singoli elementi/degli interi insiemi 
%%

> [!esempio]- Esempio: controimmagine di una funzione costante
> 
> Data una [funzione costante](Funzioni.md#^definizione-funzione-costante) $f \colon A \to B, a \mapsto \beta$, se $T \subsetneq B$ è un sottoinsieme del codominio $B$ si ha che:
> - Se $\beta \in T$, allora $f^{-1}(T) = A$.
> - Se $\beta \notin T$, allora $f^{-1}(T) = \emptyset$.

> [!esempio]- Esempio: controimmagine di una funzione proiezione
> 
> Data una [funzione proiezione](Funzioni.md#^definizione-funzione-proiezione) $f \colon A \times B \to B, (a,b) \mapsto b$, allora $\forall b \in B(f^{-1}(b) = A\times\{b\})$.

> [!esempio]- Esempio: controimmagine della funzione $\color{#7F7FFF} f \colon [-1,1] \to \mathbb{R}, x \mapsto \sin(x)$
> 
> Data una [funzione](Funzioni.md#^definizione-funzione) $f \colon [-1,1] \to \mathbb{R}, x \mapsto \sin(x)$, la controimmagine dell'insieme $\mathbb{N} \subsetneq \mathbb{R}$ dei numeri naturali è l'insieme:
> $$
> f^{-1}(\mathbb{N}) = \left\{ \ldots, -\dfrac{3\pi}{2}, -\pi, -\dfrac{\pi}{2}, 0, \dfrac{\pi}{2}, \pi, \dfrac{3\pi}{2}, \ldots \right\} = \left\{ \dfrac{n\pi}{2} \middle| n \in \mathbb{Z} \right\}
> $$

## 1.3 - Definizioni e rappresentazioni di una funzione

Ci sono diversi modi per poter definire la struttura di una [funzione](Funzioni.md#^definizione-funzione), alcuni dei quali molto simili a quanto avviene per gli [insiemi](Teoria%20degli%20insiemi.md#^definizione-insieme).

### 1.3.1 - Definizione per elencazione di una funzione

> [!notazione]+ Definizione per elencazione di una funzione
> 
> Una [funzione](Funzioni.md#^definizione-funzione) $f \colon A \to B$ può essere definita **per elencazione** fornendo un elenco di tutte le coppie $(a,b) \in A \times B$ tali che $(a,b) \in f$, ovvero tali che $b = f(a)$.
^definizione-per-elencazione-di-una-funzione

> [!esempio]- Esempio di definizione per elencazione di una funzione
> 
> Dati due [insiemi](Teoria%20degli%20insiemi.md#^definizione-insieme) $A = \{ a,b,c \}$ e $B = \{ 0,1 \}$, allora la lista:
> $$
> \begin{align*}
> f(a) = 0 \\
> f(b) = 1 \\
> f(c) = 0
> \end{align*}
> $$
> descrive in maniera univoca una [funzione](Funzioni.md#^definizione-funzione) $f \colon A \to B$.

### 1.3.2 - Definizione per caratteristica di una funzione

> [!notazione]+ Definizione per caratteristica di una funzione
> 
> Una [funzione](Funzioni.md#^definizione-funzione) $f \colon A \to B$ può essere definita **per caratteristica** fornendo una "regola" che permette di determinare i valori di $f$ su ciascun $x \in A$, ma ciò presuppone che il dominio e il codominio della funzione siano stati specificati precedentemente o facilmente intuibili dal contesto.
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
> Per rappresentare una [funzione](Funzioni.md#^definizione-funzione) "visivamente" si usa il **piano cartesiano**, cioè un piano composto da due rette perpendicolari tra loro, dette **_assi cartesiani_**, che hanno alcune caratteristiche particolari:
> - Sono disegnate in modo che una di esse sia orizzontale e l'altra verticale.
> - Ognuna di loro rappresenta una grandezza: generalmente la retta orizzontale, detta **_asse delle ascisse_**, rappresenta i valori che può assumere la $x$, mentre la retta verticale, detta **_asse delle ordinate_**, rappresenta i valori che può assumere la $y$.
> - Sono orientate, cioè a una delle due estremità presentano una freccia che indica il verso in cui le grandezze aumentano di valore (generalmente verso destra per l'asse delle ascisse e verso l'alto per l'asse delle ordinate).
> - Il loro punto di incontro viene detto **_origine degli assi_** e viene indicato con $O$.
> - Le quattro parti in cui viene diviso il piano dagli assi prendono il nome di **_quadranti_** e, partendo da quello in alto a destra e procedendo in senso antiorario, vengono numerati da $1$ a $4$.

%%
come si disegna la funzione sul piano cartesiano?
%%

<!--

> [!esempio]- Esempio: piano cartesiano di ${\color{#7F7FFF} f(x)=3x-1 }$
> 
> Il [grafico](Funzioni.md#^definizione-grafico-di-una-funzione) della [funzione](Funzioni.md#^definizione-funzione) $f(x)=3x-1$ è l'insieme $\Gamma_{f} = \{ (x,y) \in \mathbb{R}^{2} \mid y=3x-1 \}$ ed è rappresentato dalla seguente retta nel piano cartesiano:
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

-->

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
> Date due [funzioni](Funzioni.md#^definizione-funzione) $f$ e $g$, esse sono definite **uguali** se hanno lo stesso dominio e lo stesso codominio e se $f(x) = g(x)$ per ogni elemento $x$ del dominio.
^definizione-uguaglianza-di-due-funzioni

%% 
Osservazione:
quindi il loro grafico deve coincidere
%%

> [!esempio]- Esempio: uguaglianza di due funzioni apparentemente diverse
> 
> Date due [funzioni](Funzioni.md#^definizione-funzione) $f(x)=3x^2-1$ e $g(x)=x^3+2x-1$ definite in $\mathbb{R}$ e con [dominio](Funzioni.md#^definizione-dominio-e-codominio-della-funzione) $\{0,1,2\}$, ossia $f,g \colon \{0,1,2\} \to \mathbb{R}$, allora $f=g$ perché:
> - $f(0)=g(0)=-1$;
> - $f(1)=g(1)=2$;
> - $f(2)=g(2)=11$.

%% 
Attenzione:

$$
\dfrac{x^2-1}{x-1} \ne x+1
$$

perché la prima non è definita per $x = 1$
%%

# 3 - Funzioni particolari

Ci sono alcune [funzioni](Funzioni.md#^definizione-funzione) che hanno un comportamento particolare.

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
> Dato un [insieme](Teoria%20degli%20insiemi.md#^definizione-insieme) $X$, la **funzione identità** $\text{id}_X$ su $X$ è la [funzione](Funzioni.md#^definizione-funzione) che associa a ogni elemento di $X$ se stesso:
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
> Dati due [insiemi](Teoria%20degli%20insiemi.md#^definizione-insieme) $A$ e $B$ non necessariamente distinti e un elemento fissato $\beta \in B$, la **funzione costante** $f_\beta$ con valore $\beta$ è la [funzione](Funzioni.md#^definizione-funzione) che associa a ogni elemento di $A$ sempre lo stesso elemento $\beta$ di $B$:
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
> Dati due [insiemi](Teoria%20degli%20insiemi.md#^definizione-insieme) $A$ e $B$, le **funzioni proiezioni** $p_1$ e $p_2$ sui singoli fattori sono le [funzioni](Funzioni.md#^definizione-funzione) che associano a ogni coppia di valori $(a,b) \in A \times B$ uno solo dei due valori:
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
> Data una [funzione](Funzioni.md#^definizione-funzione) $f \colon A \to B$ e un [sottoinsieme](Teoria%20degli%20insiemi.md#^definizione-sottoinsieme) $C \subseteq A$, si dice _**restrizione**_ di $f$ a $C$ la funzione $f_{\vert C}$ che restringe il dominio di $f$ a $C$:
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
> Data una [funzione](Funzioni.md#^definizione-funzione) $f \colon \mathbb{R} \to \mathbb{R}, x \mapsto x^2$, essa si può [restringere](Funzioni.md#^definizione-funzione-restrizione) al [sottoinsieme](Teoria%20degli%20insiemi.md#^definizione-insieme) $\mathbb{N} \subsetneq \mathbb{R}$ e diventa la [funzione](Funzioni.md#^definizione-funzione) $f|_\mathbb{N} \colon \mathbb{R} \to \mathbb{R} x \mapsto x^2$.

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

# 4 - Operazioni tra funzioni

## 4.1 - Somma di funzioni

> [!definizione]+ Definizione: somma di funzioni
> 
> Date due [funzioni](Funzioni.md#^definizione-funzione) $f \colon \text{dom}(f) \to \mathbb{R}$ e $g \colon \text{dom}(g) \to \mathbb{R}$, si definisce la **somma** $f + g$ come la [funzione](Funzioni.md#^definizione-funzione):
> 
> $$
> (f + g) \colon \text{dom}(f) \cap \text{dom}(g) \to \mathbb{R}
> $$
> 
> tale che per ogni $x \in \text{dom}(f) \cap \text{dom}(g)$:
> 
> $$
> (f+g)(x) = f(x) + g(x)
> $$
^definizione-somma-di-funzioni

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
> - 📚 Walter Dambrosio, _Analisi matematica - Fare e comprendere_, Zanichelli, 2018 (ISBN: `9788808220745`):
> 	- Parte I - _I concetti dell'analisi matematica_:
> 		- Capitolo 1 - _Funzioni e modelli_:
> 			- 1 - _Funzioni e grafici_:
> 				- 1.1 - _Funzioni e loro rappresentazioni_.
> - 📚 Sergio Lancelotti, _Lezioni di Analisi Matematica I_, Celid, 2020 (ISBN: `978-8867891979`):
> 	- Capitolo 2 - _Funzioni_:
> 		- 1 - _Nozioni preliminari_.
