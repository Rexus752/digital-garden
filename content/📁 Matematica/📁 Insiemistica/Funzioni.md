---
icon: BoBxArrowFromLeft
iconColor: "#8888FF"
---
# Introduzione alle funzioni

> [!definizione] Definizione: funzione
> 
> Una **funzione**, denotata con le lettere latine minuscole (solitamente "$f$", oppure anche "$g$" e "$h$" quando sono presenti più funzioni), è una [relazione binaria](Relazioni%20tra%20insiemi.md#^Definizione-relazione-n-aria) tra due [insiemi](Insiemistica.md#^Osservazione-insiemi-come-elementi-di-altri-insiemi) $A$ e $B$, chiamati rispettivamente **_dominio_** e **_codominio_** della funzione, che associa a ogni elemento $x \in A$ del dominio uno e un solo elemento $y \in B$ del codominio:
> 
> $$
> \begin{align*}
> f \colon A & \to B \\
> x & \mapsto y
> \end{align*}
> $$
^Definizione-funzione

> [!esempio] Esempio: $f \colon \mathbb{R} \to \mathbb{R}, x \mapsto x^2$
> 
> La funzione $f \colon \mathbb{R} \to \mathbb{R}, x \mapsto x^2$ è una funzione che associa a ogni numero reale $x$ il suo quadrato $y=x^2$. Essa è una funzione perché per ogni numero il suo quadrato è unico e non può averne altri.

> [!esempio] Esempio: $R=\{(1,2),(1,3),(2,4)\}$ non è una funzione
> Data una [relazione binaria](Relazioni%20tra%20insiemi.md#^Definizione-relazione-n-aria) $R=\{(1,2),(1,3),(2,4)\}$, essa non è una funzione in quanto c’è un elemento del dominio (l’elemento $1$) che è associato a più elementi del codominio (gli elementi $2$ e $3$).

Quando si vuole omettere il codominio della funzione (perché facilmente intuibili dal contesto), si può anche usare la dicitura "$\forall x \in A (f(x) = y)$" dove, al posto della $y$, c'è direttamente la trasformazione operata su $x$ (es. la funzione $f \colon \mathbb{R} \to \mathbb{R}, x \mapsto x^2$ si può anche scrivere come $\forall x \in \mathbb{R} (f(x) = x^2)$).

Quando si vuole omettere anche il dominio della funzione (sempre perché facilmente intuibile dal contesto), specificando però una proprietà $P(x)$ che devono rispettare gli elementi del dominio, si può usare la dicitura "$P(x)(f(x) = y)$" dove, al posto della $y$, c'è sempre la trasformazione operata su $x$ (es. la funzione $f \colon \{ x \in \mathbb{R} \mid x > 0 \} \to \mathbb{R}, x \mapsto x^2$ si può scrivere come $\forall x > 0 (f(x) = x^2)$).

> [!osservazione] Osservazione: funzione come dipendenza tra due grandezze
> 
> Il concetto di funzione è il modello matematico che esprime la *dipendenza* tra due grandezze. Se una certa grandezza $Y$ dipende da un'altra grandezza $X$ e se a ogni valore di $X$ è associato un unico valore di $Y$, allora $Y$ è una funzione di $X$: in questo caso si dice che $X$ è la grandezza _indipendente_ e che $Y$ è la grandezza _dipendente_.
> 
> Un esempio molto semplice è dato dalle grandezze $X$ e $Y$ definite rispettivamente come "lunghezza del lato di un quadrato" e "area del quadrato": l'insieme dei possibili valori assunti da $X$, cioè il dominio, è $\{ x \in \mathbb{R} \mid x > 0\}$ e a ogni $x$ si associa l'area corrispondente $y=x^2$ (in opportune unità di misura), che è l'unico valore dell'area del quadrato di lato avente lunghezza $x$.
> Possiamo quindi affermare che l'area del quadrato è _funzione_ della lunghezza del suo lato, secondo la relazione:
> $$
> \forall x > 0 (f(x)=x^{2}) 
> $$

> [!osservazione] Osservazione: funzione come concetto non strettamente algebrico
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

> [!osservazione] Osservazione: funzione come processo con input e output
> 
> Il concetto di funzione può essere facilmente inteso in termini di processo che, dato un certo input, fornisce un determinato output.
> 
> Una funzione $f$ è assimilabile a una macchina che prende in ingresso un valore $x$ e restituisce in uscita un unico valore corrispondente $f(x)$:
> 
> $$
> \boxed{x} \to \boxed{f(x)}
> $$
> 
> Il valore in uscita si ottiene spesso mediante una procedura che specifica le operazioni da effettuare sul valore in ingresso: per esempio, per la funzione $f \colon \mathbb{R} \to \mathbb{R}$ definita da $f(x)=2x+1$, la procedura può essere descritta dalle operazioni "moltiplica per 2" e "aggiungi 1":
> 
> $$
> \boxed{x} \xrightarrow{\text{moltiplica per }2} \boxed{2x} \xrightarrow{\text{aggiungi }1} \boxed{2x+1}
> $$
> 
> Il modo più semplice per rappresentare il meccanismo input-output che soggiace al concetto di funzione è un diagramma a frecce come il seguente, che rappresenta una generica funzione $f \colon X \to Y, x \mapsto f(x)$:
> ![asd](Pasted%20image%2020240220102800.png)

> [!definizione] Definizione: grafico di una funzione
> 
> Data una [funzione](Funzioni.md#^Definizione-funzione) $f \colon A \to B, x \mapsto f(x)$, si definisce ***grafico*** di $f$ il [sottoinsieme](Insiemistica.md#^Definizione-sottoinsieme) $\Gamma_{f} \subseteq \mathbb{R}^{2}$ definito da:
> 
> $$
> \Gamma_{f} = \{(x,y)\in \mathbb{R}^{2}\mid x\in A, y=f(x)\} = \{(x,f(x))\mid x\in A\}
> $$
> 
> cioè l'insieme delle coppie di elementi in $\mathbb{R}^{2}$ legate tra di loro dalla funzione $f$.
^Definizione-grafico-di-una-funzione

%%
Osservazione: parola "grafico"

Significa sia il sottoinsieme $\Gamma_{f} \subseteq \mathbb{R}^{2}$ delle coppie di elementi in $\mathbb{R}^{2}$ legate tra di loro dalla funzione $f$, sia la rappresentazione grafica di $f$.
%%

# Piano cartesiano

Per rappresentare un grafico "visivamente" si usa il **piano cartesiano**, cioè un piano composto da due rette perpendicolari tra loro, dette **_assi cartesiani_**, che hanno alcune caratteristiche particolari:
- Sono disegnate in modo che una di esse sia orizzontale e l'altra verticale.
- Ognuna di loro rappresenta una grandezza: generalmente la retta orizzontale, detta **_asse delle ascisse_**, rappresenta i valori che può assumere la $x$, mentre la retta verticale, detta **_asse delle ordinate_**, rappresenta i valori che può assumere la $y$.
- Sono orientate, cioè a una delle due estremità presentano una freccia che indica il verso in cui le grandezze aumentano di valore (generalmente verso destra per l'asse delle ascisse e verso l'alto per l'asse delle ordinate).
- Il loro punto di incontro viene detto **_origine degli assi_** e viene indicato con $O$.

%%
come si disegna la funzione sul piano cartesiano?
%%

Inoltre, le quattro parti in cui viene diviso il piano dagli assi prendono il nome di **_quadranti_** e, partendo da quello in alto a destra e procedendo in senso antiorario, vengono numerati da $1$ a $4$.

> [!esempio] Esempio: piano cartesiano di $f(x)=3x-1$
> 
> Il [grafico](Funzioni.md#^Definizione-grafico-di-una-funzione) della [funzione](Funzioni.md#^Definizione-funzione) $f \colon \mathbb{R} \to \mathbb{R}, x \mapsto 3x-1$ è l'insieme $\Gamma_{f} = \{ (x,y) \in \mathbb{R}^{2} \mid y=3x-1 \}$ ed è rappresentato dalla seguente retta nel piano cartesiano:
> ![350](Pasted%20image%2020240220105837.png)

%% sostituire grafici con Geogebra %%

> [!esempio] Esempio: ricavare le informazioni dal grafico di una funzione
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

# Uguaglianza di due funzioni

> [!definizione] Definizione: uguaglianza di due funzioni
> 
> Date due [funzioni](Funzioni.md#^Definizione-funzione) $f$ e $g$, sono definite **uguali** se hanno lo stesso dominio e lo stesso codominio e se $f(x) = g(x)$ per ogni elemento $x$ del dominio.
^Definizione-uguaglianza-di-due-funzioni

%% 
Osservazione:
quindi il loro grafico deve coincidere
%%

> [!esempio] Esempio: uguaglianza di due funzioni apparentemente diverse
> Date due funzioni $f(x)=3x^2-1$ e $g(x)=x^3+2x-1$ definite in $\mathbb{R}$ e con dominio $\{0,1,2\}$, ossia $f,g \colon \{0,1,2\} \to \mathbb{R}$, allora $f=g$ perché:
> - $f(0)=g(0)=-1$;
> - $f(1)=g(1)=2$;
> - $f(2)=g(2)=11$.

# Funzioni particolari

> [!definizione] Definizione: funzione identità
> 
> Dato un [insieme](Insiemistica.md#^Definizione-insieme) $X$, la **funzione identità** su $X$ è la [funzione](Funzioni.md#^Definizione-funzione) che associa a ogni elemento di $X$ se stesso:
> 
> $$
> \begin{align*}
> \text{id}_X \colon X & \to X \\
> x & \mapsto x
> \end{align*}
> $$
^Definizione-funzione-identita

> [!definizione] Definizione: funzione costante
> 
> Dati due [insiemi](Insiemistica.md#^Definizione-insieme) $A$ e $B$ non necessariamente distinti e un elemento fissato $\beta \in B$, la **funzione costante** con valore $\beta$ è la [funzione](Funzioni.md#^Definizione-funzione) che associa a ogni elemento di $A$ sempre lo stesso elemento $\beta$ di $B$:
> 
> $$
> \begin{align*}
> f_\beta \colon A & \to B \\
> a & \mapsto \beta
> \end{align*}
> $$
^Definizione-funzione-costante

> [!definizione] Definizione: funzione proiezione
> 
> Dati due [insiemi](Insiemistica.md#^Definizione-insieme) $A$ e $B$, le **funzioni proiezioni** sui singoli fattori sono le funzioni che associano a ogni coppia di valori $(a,b) \in A \times B$ uno solo dei due valori:
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
^Definizione-funzione-proiezione

> [!definizione] Definizione: funzione restrizione
> 
> Data una [funzione](Funzioni.md#^Definizione-funzione) $f \colon A\to B$ e un [sottoinsieme](Insiemistica.md#^Definizione-sottoinsieme) $S \subseteq A$, si dice _**restrizione**_ di $f$ a $S$ la funzione che restringe il dominio di $f$ a $S$:
> 
> $$
> \begin{align*}
> f_{\vert S} \colon S & \to B \\
> x & \mapsto f_{\vert S}(x)
> \end{align*}
> $$
> 
> Essa è cioè una funzione che in $S$ si comporta esattamente come la funzione originaria si comporta in $A$, ma che si "dimentica" dei punti al di fuori di quel sottoinsieme.
^Definizione-funzione-restrizione

> [!esempio] Esempio: $f|_\mathbb{N} \colon \mathbb{N} \to \mathbb{R}$
> 
> Data una funzione $f \colon \mathbb{R} \to \mathbb{R}, x \mapsto x^2$, essa si può restringere al sottoinsieme $\mathbb{N} \subsetneq \mathbb{R}$ e diventa la funzione $f|_\mathbb{N} \colon \mathbb{R} \to \mathbb{R} x \mapsto x^2$.


# Fonti

- Lezioni dei Prof. Chen Yu e Terracini Lea del corso di Matematica Discreta (canale C), Corso di Laurea in Informatica presso l'Università di Torino, A.A. 2023-24.
- Lezioni del Prof. Radeschi Marco del corso di Algebra Lineare (canale C), Corso di Laurea in Informatica presso l'Università di Torino, A.A. 2023-24.

%%
- libro di bruno martelli
- libro di mdag
- lezioni seiler
- libro di analisi
%%