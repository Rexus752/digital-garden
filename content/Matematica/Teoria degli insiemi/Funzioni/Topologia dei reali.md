---
title: Topologia dei reali
---

> [!premessa]+ Premessa
> 
> Ciao! Se è la prima volta che capiti su questo sito, ti consiglio di consultare la [pagina principale](index.md) di questo cosiddetto _Giardino Digitale_ per scoprire meglio cos'è e come navigarlo.
> 
> Lo stato di questa nota è al momento: 🔴 <font color="#FF7F7F">_Bozza_</font>.

---

# 1 - Intorni

> [!definizione]+ Definizione: intorno di un punto
> 
> Dato un punto%% link %% $x_0 \in \mathbb{R}$ e un $r > 0$, si chiama **intorno di centro $x_0$ e raggio $r$** e si indica con "$I(x_0)$" l'intervallo aperto%% link %%
> 
> $$
> \begin{align*}
> (x_0 - r, x_0 + r) &= \{ x \in \mathbb{R} \mid x_0 - r < x < x_0 + r \} \\
> &= \{ x \in \mathbb{R} \mid -r < x - x_0 < r \} \\
> &= \{ x \in \mathbb{R} \mid |x - x_0| < r \}
> \end{align*}
> $$
> 
> ossia l'insieme di tutti e soli i punti%% link %% di $\mathbb{R}$ aventi distanza da $x_0$ minore di $r$.
> 
> Si chiama **intorno destro di $x_0$ di raggio $r$** l'intervallo aperto%% link %% $(x_0, x_0 + r)$.
> 
> Si chiama **intorno sinistro di $x_0$ di raggio $r$** l'intervallo aperto%% link %% $(x_0 - r, x_0)$.
^definizione-intorno-di-un-punto

%% 
mettere rappresentazione grafica a pagina 115 di Lancelotti
%%

%% esempio %%

> [!definizione]+ Definizione: intorno bucato di un punto
> 
> Un **intorno bucato** di un punto%% link %% $x_0$ è un [intorno](Topologia%20dei%20reali.md#^definizione-intorno-di-un-punto) $I(x_0)$ di $x_0$ da cui si esclude $x_0$ stesso.
^definizione-intorno-bucato-di-un-punto

> [!osservazione]+ Osservazione: utilità dell'intorno bucato
> 
> L'[_intorno bucato_](Topologia%20dei%20reali.md#^definizione-intorno-bucato) ci tornerà utile più in là quando studieremo i [_limiti_](Matematica/Analisi%20matematica/Limiti/_index.md#^definizione-limite) perché ci interesserà analizzare l'[intorno](Topologia%20dei%20reali.md#^definizione-intorno-di-un-punto) di un punto%% link %% $x_0$ escluso $x_0$ stesso, cioè proprio l'[intorno bucato](Topologia%20dei%20reali.md#^definizione-intorno-bucato) di $x_0$.

> [!definizione]+ Definizione: intorno di un infinito
> 
> Dato un $a \in \mathbb{R}$:
> - L'**intorno di $+ \infty$** è l'intervallo aperto%% link %% $(a, + \infty)$.
> - L'**intorno di $- \infty$** è l'intervallo aperto%% link %% $(-\infty, a)$.
^definizione-intorno-di-un-infinito

%% 
mettere rappresentazione grafica a pagina 116 di Lancelotti
%%

%% 
(1.5) Osservazione Sia x0 \in R \cup {±∞}.
Allora l'intersezione di un numero finito di intorni di x0 è un intorno di x0.
%%

> [!definizione]+ Definizione: punto interno
> 
> Dato un [insieme](Matematica/Teoria%20degli%20insiemi/_index.md#^definizione-insieme) $A \subseteq \mathbb{R}$ e un punto $x_0 \in A$, quest'ultimo è un **punto interno ad $A$** se esite un [intorno](Topologia%20dei%20reali.md#^definizione-intorno-di-un-punto) $I$ di $x_0$ tale che $I \subseteq A$.
^definizione-punto-interno

%% esempio di punto interno %%

> [!definizione]+ Definizione: parte interna di un insieme
> 
> Dato un [insieme](Matematica/Teoria%20degli%20insiemi/_index.md#^definizione-insieme) $A \subseteq \mathbb{R}$, l'insieme dei suoi [punti interni](Topologia%20dei%20reali.md#^definizione-punto-interno-e-parte-interna) viene detto **parte interna di $A$** e si indica con "$\text{int}(A)$".
^definizione-parte-interna-di-un-insieme

> [!proposizione]+ Proposizione: punti interni di $\color{#FF7F7F} [a,b]$ sono $\color{#FF7F7F} (a,b)$
> 
> Dato un intervallo chiuso%% link %% $A = [a,b]$, i [punti interni](Topologia%20dei%20reali.md#^definizione-punto-interno-e-parte-interna) di $A$ sono tutti e soli i punti dell'intervallo aperto%% Link %% $(a,b)$.
> 
> > [!dimostrazione]- Dimostrazione
> > 
> > Dato un $x_0 \in (a,b)$, cioè $a < x_0 < b$, consideriamo $0 < r < \min\{ x_0 - a, b - x_0 \}$ e l'[intorno](Topologia%20dei%20reali.md#^definizione-intorno-di-un-punto) $I_r = (x_0 - r, x_0 + r)$. Dobbiamo dimostrare che $I_r \subseteq A$.
> > 
> > Essendo $r < \min\{ x_0 - a, b - x_0 \}$ si ha che
> > 
> > $$
> > r < x_0 - a \quad \land \quad r < b - x_0
> > $$
> > 
> > Quindi se $x \in I_r$, cioè $x_0 - r < x < x_0 + r$, si ha che:
> > 
> > $$
> > \begin{cases}
> > x > x_0 - r > x_0 - x_0 + a = a \\
> > x < x_0 + r < x_0 + b - x_0 = b
> > \end{cases}
> > \implies
> > a < x < b
> > \implies
> > x \in A
> > $$
> > 
> > %% 
> > mettere grafico di pagina 117
> > %%
> > 
> > Evidentemente né $a$ né $b$ sono [punti interni](Topologia%20dei%20reali.md#^definizione-punto-interno-e-parte-interna) ad $A$. Infatti, ogni [intorno](Topologia%20dei%20reali.md#^definizione-intorno-di-un-punto) $I_\delta = (a - \delta, a + \delta)$ di $a$, con $\delta > 0$, contiene punti di $\mathbb{R}$ non appartenenti ad $A$ (ossia i punti $a - \delta < x < a$). Analogamente, ogni intorno $I_\varepsilon = (b - \varepsilon, b + \varepsilon)$ di $b$, con $\varepsilon > 0$, contiene punti di $\mathbb{R}$ non appartenenti ad $A$ (ossia i punti $b < x < b + \varepsilon$).
> > 
> > %% 
> > mettere grafico di pagina 117
> > Graficamente per $a$ 
> > %%

%% 
Proposizioni:
- Se A = (a, b), allora tutti punti di A sono interni ad A, cioè A = int(A).
- e A = [a, +∞), oppure A = (-∞, a], allora int(A) è rispettivamente (a, +∞) e (-∞, a).
- Se A = (a, +∞), oppure A = (-∞, a), allora tutti punti di A sono interni ad A, cioè A = int(A).

In tutte e 3 queste proposizioni si procede come nella proposiizone precedente).
%%

> [!definizione]+ Definizione: insieme aperto o chiuso di $\color{#FF7FFF} \mathbb{R}$
> 
> Dato un [insieme](Matematica/Teoria%20degli%20insiemi/_index.md#^definizione-insieme) $A \subseteq \mathbb{R}$ abbiamo che:
> - $A$ si dice **aperto** se ogni punto di $A$ è [interno](Topologia%20dei%20reali.md#^definizione-punto-interno-e-parte-interna) ad $A$, cioè se $\text{int}(A) = A$.
> - $A$ si dice **chiuso** se il [complementare](Matematica/Teoria%20degli%20insiemi/_index.md#^definizione-complemento-di-un-insieme) $\complement_\mathbb{R}(A)$ di $A$ è aperto.
> 
> Per convenzione, l'[insieme vuoto](Matematica/Teoria%20degli%20insiemi/_index.md#^definizione-insieme-vuoto) $\emptyset$ e l'insieme dei numeri reali%% link %% $\mathbb{R}$ sono contemporaneamente sia aperti che chiusi.
^definizione-insieme-aperto-o-chiuso-di-r

%% 
Attenzione: aperto e chiuso non sono due concetti mutualmente esclusivi, un insieme può essere sia aperto che chiuso (esattamente come lo sono per definizione l'insieme vuoto e l'insieme dei numeri reali) e, allo stesso tempo, un insieme non deve essere necessariamente o aperto o chiuso: per esempio, l'intervallo $[a,b)$ non è né aperto né chiuso.

Infatti, non è aperto perché $a \in [a,b)$ ma non è interno e non è chiuso perché il suo complementare è $(-\infty, a) \cup [b, + \infty)$ che non è aperto perché contiene $b$ che però non è interno.
%%

%% 
[!proposizione]+ Proposizione

Gli intervalli aperti sono aperti, gli intervalli chiusi sono chiusi

Fare dimostrazione
%%

# 2 - Punti isolati

> [!definizione]+ Definizione: punto isolato
> 
> Dato un [insieme](Matematica/Teoria%20degli%20insiemi/_index.md#^definizione-insieme) $A \subseteq \mathbb{R}$ e un punto%% link %% $x_0 \in A$, diciamo che $x_0$ è un **punto isolato** di $A$ se esiste un [intorno](Topologia%20dei%20reali.md#^definizione-intorno-di-un-punto) $I$ di $x_0$ tale che $A \cap I = \{ x_0 \}$.
> 
> In altri termini, $x_0$ è isolato in $A$ se l'unico punto di $A$ contenuto in un suo opportuno intorno è $x_0$ stesso.
^definizione-punto-isolato

> [!definizione]+ Definizione: insieme discreto
> 
> Un [insieme](Matematica/Teoria%20degli%20insiemi/_index.md#^definizione-insieme) $A \subseteq \mathbb{R}$ si dice **discreto** se è costituito solo da [punti isolati](Topologia%20dei%20reali.md#^definizione-punto-isolato).
^definizione-insieme-discreto

> [!esempio]- Esempio di punto isolato
> 
> Consideriamo l'[insieme](Matematica/Teoria%20degli%20insiemi/_index.md#^definizione-insieme)
> 
> $$
> A = \{ x \in \mathbb{R} \mid x^4 - x^2 \ge 0 \}
> $$
> 
> Il punto%% Link %% $x_0 = 0$ è un [punto isolato](Topologia%20dei%20reali.md#^definizione-punto-isolato) in $A$ perché
> 
> $$
> \begin{align*}
> A &= \{ x \in \mathbb{R} \mid x^4 - x^2 \ge 0 \} \\
> &= (-\infty, -1] \cup \{ 0 \} \cup [1, + \infty)
> \end{align*}
> $$
> 
> e se consideriamo l'[intorno](Topologia%20dei%20reali.md#^definizione-intorno-di-un-punto) $I = (-1, 1)$ di $x_0 = 0$ abbiamo che $A \cap I = \{ 0 \}$.

%% esempio di insieme discreto %%

%%
[!proposizione]+ $\mathbb{N}$ e $\mathbb{Z}$ sono insiemi discreti

Sono insiemi discreti gli insiemi $\mathbb{N}$ e $\mathbb{Z}$ in ogni loro sottinsieme.

da dimostrare
%%

# 3 - Punti di accumulazione

> [!definizione]+ Definizione: punto di accumulazione
> 
> Dato un [insieme](Matematica/Teoria%20degli%20insiemi/_index.md#^definizione-insieme) $A \subseteq \mathbb{R}$ e un punto%% link %% $x_0 \in \mathbb{R} \cup \{ \pm \infty \}$, abbiamo che $x_0$ è un **punto di accumulazione per $A$** se ogni [intorno](Topologia%20dei%20reali.md#^definizione-intorno-di-un-punto) di $x_0$ contiene punti%% link %% di $A$ diversi da $x_0$.
^definizione-punto-di-accumulazione

%% 
La denominazione "punto di accumulazione" indica che comunque ci si ponga vicini a questo
punto (in un intorno), si trovano punti dell'insieme diversi dal punto stesso (che potrebbe anche
non appartenere all'insieme), quindi vicino a questo punto si accumulano punti dell'insieme.
%%

> [!esempio]- Esempio di punto di accumulazione
> 
> Dato un intervallo%% link %% $A = [a,b)$, i [punti di accumulazione](Topologia%20dei%20reali.md#^definizione-punto-di-accumulazione) di $A$ sono tutti e soli i punti%% link %% di $[a,b]$. Infatti, consideriamo inizialmente i [punti interni](Topologia%20dei%20reali.md#^definizione-punto-interno-e-parte-interna) ad $A$, cioè i punti%% Link %% $x_0 \in (a,b)$. Poiché $x_0$ è [interno](Topologia%20dei%20reali.md#^definizione-punto-interno) ad $A$, allora esiste un [intorno](Topologia%20dei%20reali.md#^definizione-intorno-di-un-punto) $I_r = (x_0 - r, x_0 + r)$ tale che $I_r \subseteq A$.
> 
> Consideriamo quindi un qualunque intorno $I_\delta = (x_0 - \delta, x_0 + \delta)$ i $x_0$:
> - Se $\delta \le r$, allora $I_\delta \subseteq I_r \subseteq A$. Poiché $I_\delta$ contiene punti%% link %% diversi da $x_0$, allora è verificato che contiene punti di $A$ diversi da $x_0$.
> - Se $\delta > r$, allora $I_r \subseteq I_\delta$ ed essendo $I_r \subseteq A$ si ha che $I_r \subseteq A \cap I_\delta$. Poiché $I_r$ contiene punti diversi da $x_0$, allora è verificato che $I_\delta$ contiene punti di $A$ diversi da $x_0$.
> 
> Pertanto, $x_0$ è un [punto di accumulazione](Topologia%20dei%20reali.md#^definizione-punto-di-accumulazione) per $A$.
> 
> Inoltre, anche $a$ e $b$ sono [punti di accumulazione](Topologia%20dei%20reali.md#^definizione-punto-di-accumulazione) per $A$: consideriamo $a$ e sia $I_r = (a-r,a+r)$ un qualunque [intorno](Topologia%20dei%20reali.md#^definizione-intorno-di-un-punto) di $a$. Si ha che:
> - Se $r \le b - a$, allora $A \cap I_r = [a, a + r)$.
> - Se $r > b - a$, allora $A \cap I_r = [a,b)$.
> 
> In ogni caso, $I_r$ contiene punti%% Link %% di $A$ diversi da $a$, pertanto $a$ è un [punto di accumulazione](Topologia%20dei%20reali.md#^definizione-punto-di-accumulazione) per $A$. Analogamente per $b$.
> 
> Infine dimostriamo che i punti%% link %% $x_0 \in \mathbb{R} \cup \{ \pm \infty \}$ non appartenenti ad $[a,b]$ non sono di accumulazione per $A$: consideriamo inizialmente $x_0 \in \mathbb{R}$ con $x_0 < a$ (analogamente se $x_0 > b$).
> 
> Consideriamo $r = a - x_0$ e l'[intorno](Topologia%20dei%20reali.md#^definizione-intorno-di-un-punto)
> 
> $$
> \begin{align*}
> I_r &= (x_0 - r, x_0 + r) \\
> &= (2x_0 - a,a)
> \end{align*}
> $$
> 
> di $x_0$. Allora $A \cap I_r = \emptyset$, quindi $x_0$ non è un [punto di accumulazione](Topologia%20dei%20reali.md#^definizione-punto-di-accumulazione) per $A$.
> 
> Se $x_0 = -\infty$ (analogamente se $x_0 = +\infty$) e consideriamo l'[intorno](Topologia%20dei%20reali.md#^definizione-intorno-di-un-punto) $I = (-\infty, a - 1)$ di $-\infty$, allora $A \cap I = \emptyset$ e quindi $x_0 = -\infty$ non è un [punto di accumulazione](Topologia%20dei%20reali.md#^definizione-punto-di-accumulazione) per $A$.
> 
> Analoghe conclusioni se $A$ contiene l'altro estremo oppure non ne contiene alcuno.

%% 
esempio:

Sia A = [a, +∞). I punti di accumulazione di A sono tutti e soli i punti di [a, +∞) \cup {+∞}.
Infatti, per i punti interni ad A e per a si procede come nell'esempio precedente. Mostriamo
che +∞ è di accumulazione per A.
Consideriamo l'intorno I = (b, +∞) di +∞. Allora si ha che
b \le a =⇒ A \cap I = [a, +∞),
b > a =⇒ A \cap I = [b, +∞).
In ogni caso I contiene punti di A, ovviamente diversi da +∞. Pertanto +∞ è di accumula-
zione per A.
Analoga conclusione se A non contiene a.
%%

%% 
esempi:
3) Sia A = (-∞, b] oppure A = (-∞, b). I punti di accumulazione di A sono tutti e soli i punti
di (-∞, b] \cup {-∞}. Si procede come nel caso precedente.
4) Se A \subseteq R è illimitato superiormente, allora +∞ è di accumulazione per A.
Infatti, se A è illimitato superiormente, allora per ogni m \in R esiste a \in A tale che a > m, cio`e
a \in (m, +∞). Poiché gli intorni di +∞ sono tutti della forma (m, +∞), abbiamo dimostrato
che ogni intorno di +∞ contiene punti di A, ovviamente diversi da +∞. Quindi +∞ è di
accumulazione per A.
5) Se A \subseteq R è illimitato inferiormente, allora -∞ è di accumulazione per A. Si procede come
nel caso precedente.
In particolare +∞ è di accumulazione per N, ±∞ sono di accumulazione per Z, Q e R.
6) Se A \subseteq R è limitato superiormente, allora +∞ non è di accumulazione per A. Infatti, se A `e
limitato superiormente, allora esiste m \in R tale che per ogni a \in A si ha che a \le m, cioè a \in
(-∞, m]. Quindi se consideriamo l'intorno I = (m, +∞) di +∞, si ha che A \cap (m, +∞) = \emptyset.
Ne segue che +∞ non è di accumulazione per A.
7) Se A \subseteq R è limitato inferiormente, allora -∞ non è di accumulazione per A. Si procede
come nel caso precedente.
8) Se A \subseteq R è limitato, allora ±∞ non sono di accumulazione per A.
%%

> [!esempio]- Esempio
> 
> Consideriamo l'[insieme](Matematica/Teoria%20degli%20insiemi/_index.md#^definizione-insieme)
> 
> $$
> A = \left\{
> \begin{array}{c|c}
> \displaystyle
> \dfrac{1}{n} & n \in \mathbb{N}, n \ge 1
> \end{array}
> \right\}
> $$
> 
> Determiniamo i [punti di accumulazione](Topologia%20dei%20reali.md#^definizione-punto-di-accumulazione) di $A$: osserviamo che i punti%% link %% di $A$ sono tutti [isolati](Topologia%20dei%20reali.md#^definizione-punto-isolato), cioè che $A$ è [discreto](Topologia%20dei%20reali.md#^definizione-insieme-discreto). Infatti, se consideriamo $\dfrac{1}{n} \in A$, abbiamo che
> 
> $$
> r = \dfrac{1}{n} - \dfrac{1}{n+1}
> $$
> 
> e
> 
> $$
> I_r = \left( \dfrac{1}{n} - r, \dfrac{1}{n} + r \right) \subseteq \left( \dfrac{1}{n+1}. \dfrac{1}{n-1} \right) 
> $$
> 
> L'[insieme](Matematica/Teoria%20degli%20insiemi/_index.md#^definizione-insieme) $I_r$ è un [intorno](Topologia%20dei%20reali.md#^definizione-intorno-di-un-punto) di $\dfrac{1}{n}$ e si ha che $A \cap I_r = \left\{  \dfrac{1}{n}  \right\}$. Quindi $\dfrac{1}{n}$ è un [punto isolato](Topologia%20dei%20reali.md#^definizione-punto-isolato) in $A$.
> 
> Evidentemente i punti isolati non sono di accumulazione.%% quindi un punto isolato non può essere di accumulazione e viceversa? da trasformare in proposizione? %%
> 
> Osserviamo che i punti%% link %% $\dfrac{1}{n} \in A$ sono tali che
> 
> $$
> 0 < \dfrac{1}{n} \le 1
> $$
> 
> e, man mano che $n$ aumenta, questi punti sono sempre più prossimi a $0$, dato che il quoziente fra $1$ ed $n$ diventa sempre più vicino allo zero. Anche graficamente, fin dove è possibile fare il disegno, si vede che i punti $\dfrac{1}{n} \in A$ all'aumentare di $n$ sono sempre più vicini a $0$ e, anzi, si accumulano in un [intorno destro](Topologia%20dei%20reali.md#^definizione-intorno-di-un-punto) di $0$.
> 
> da finire
> 
> %% 
> finire da pagina 120 a pagina 122 di Lancellotti
> %%

> [!proposizione]+ Proposizione
> 
> Dato un [insieme](Matematica/Teoria%20degli%20insiemi/_index.md#^definizione-insieme) $A \subseteq \mathbb{R}$ e un punto%% link %% $x_0 \in A$, allora abbiamo che se $x_0$ è un [punto interno](Topologia%20dei%20reali.md#^definizione-punto-interno) ad $A$, allora $x_0$ è un [punto di accumulazione](Topologia%20dei%20reali.md#^definizione-punto-di-accumulazione) di $A$ ma non viceversa:
> 
> $$
> x_0 \text{ punto interno ad } A \implies x_0 \text{ punto di accumulazione di } A
> $$

%% dimostrazione per esercizio %%

> [!proposizione]+ Proposizione
> 
> Dato un [insieme](Matematica/Teoria%20degli%20insiemi/_index.md#^definizione-insieme) $A \subseteq \mathbb{R}$ e un punto%% link %% $x_0 \in A$, allora abbiamo che $x_0$ è un [punto isolato](Topologia%20dei%20reali.md#^definizione-punto-isolato) di $A$ se e solo se non è un [punto di accumulazione](Topologia%20dei%20reali.md#^definizione-punto-di-accumulazione) di $A$:
> 
> $$
> x_0 \text{ punto isolato di } A \iff x_0 \text{ non punto di accumulazione di } A
> $$

%% dimostrazione per esercizio %%

> [!proposizione]+ Proposizione
> 
> Dato un [insieme](Matematica/Teoria%20degli%20insiemi/_index.md#^definizione-insieme) $A \subseteq \mathbb{R}$ e un punto%% link %% $x_0 \in A$, se $x_0$ è un [punto isolato](Topologia%20dei%20reali.md#^definizione-punto-isolato) di $A$ allora non è un [punto interno](Topologia%20dei%20reali.md#^definizione-punto-interno) ad $A$:
> 
> $$
> x_0 \text{ punto isolato di } A \implies x_0 \text{ non punto interno ad } A
> $$

%% dimostrazione per esercizio %%

# 4 - Frontiere

> [!definizione]+ Definizione: punto di frontiera
> 
> Dato un [insieme](Matematica/Teoria%20degli%20insiemi/_index.md#^definizione-insieme) $A \subseteq \mathbb{R}$ e un punto%% link %% $x_0 \in \mathbb{R}$, diciamo che $x_0$ è un **punto di frontiera per $A$** se per ogni [intorno](Topologia%20dei%20reali.md#^definizione-intorno-di-un-punto) $I$ di $x_0$ si ha che $A \cap I \ne \emptyset$ e $\complement_\mathbb{R}(A) \cap I \ne \emptyset$.
^definizione-punto-di-frontiera

> [!definizione]+ Definizione: frontiera di un insieme
> 
> Dato un [insieme](Matematica/Teoria%20degli%20insiemi/_index.md#^definizione-insieme) $A \subseteq \mathbb{R}$, la **frontiera (o bordo) di $A$** è l'[insieme](Matematica/Teoria%20degli%20insiemi/_index.md#^definizione-insieme) dei [punti di frontiera](Topologia%20dei%20reali.md#^definizione-punto-di-frontiera) di $A$ e si denota con "$\text{Fr}(A)$" o "$\partial A$".
^definizione-frontiera-di-un-insieme

I punti di frontiera sono quei punti che "separano" l'insieme dal suo complementare. Eviden-
temente la frontiera di A coincide con quella del suo complementare.

%% 
[!esempio]- Esempio
a) Sia A = [a, b]. I punti di frontiera di A sono a e b.
Infatti, ogni intorno I = (a - r, a + r) di a interseca sia A che CA. Analogamente per b.
Invece i punti x0  = a, b non sono di frontiera. Infatti, se a < x0 < b, allora x0 è interno ad A
e quindi esiste un intorno I di x0 tale che I \subseteq A. Quindi C A \cap I = \emptyset. Ne segue che x0 non `e
di frontiera per A.
Se x0 < a (analogamente se x0 > b) allora preso r = a - x0, l'intorno Ir = (x0 - r, x0 + r) =
(2x0 - a, a) di x0 è tale che Ir \subseteq CA. Quindi A \cap Ir = \emptyset. Ne segue che x0 non è di frontiera
per A.
Analoghe conclusioni valgono se A contiene uno solo o nessuno dei suoi estremi.
b) Sia A = [a, +∞), oppure A = (-∞, a]. L'unico punto di frontiera di A è a. Si procede come
nel caso precedente. Analoga conclusione se a  \in A.
%%

> [!proposizione]+ Proposizione
> 
> Dato un [insieme](Matematica/Teoria%20degli%20insiemi/_index.md#^definizione-insieme) $A \subseteq \mathbb{R}$ e un punto%% link %% $x_0 \in \mathbb{R}$, allora si ha che se $x_0$ è anche in $A$ ed è un [punto isolato](Topologia%20dei%20reali.md#^definizione-punto-isolato) di $A$, allora è anche un [punto di frontiera](Topologia%20dei%20reali.md#^definizione-punto-di-frontiera) di $A$:
> 
> $$
> x_0 \in A \land x_0 \text{ punto isolato di } A \implies x_0 \text{ punto di frontiera di } A
> $$

%% dimostrazione %%

> [!proposizione]+ Proposizione
> 
> Dato un [insieme](Matematica/Teoria%20degli%20insiemi/_index.md#^definizione-insieme) $A \subseteq \mathbb{R}$ e un punto%% link %% $x_0 \in \mathbb{R}$, allora si ha che se $x_0$ **non** è in $A$ ed è un [punto di frontiera](Topologia%20dei%20reali.md#^definizione-punto-di-frontiera) di $A$, allora è un [punto di accumulazione](Topologia%20dei%20reali.md#^definizione-punto-di-accumulazione) di $A$:
> 
> $$
> x_0 \not\in A \land x_0 \text{ punto di frontiera di } A \implies x_0 \text{ punto di accumulazione di } A
> $$

%% dimostrazione %%

> [!proposizione]+ Proposizione
> 
> Dato un [insieme](Matematica/Teoria%20degli%20insiemi/_index.md#^definizione-insieme) $A \subseteq \mathbb{R}$, $A$ è un [sottoinsieme](Matematica/Teoria%20degli%20insiemi/_index.md#^definizione-sottoinsieme) dell'unione%% Link %% tra la [parte interna](Topologia%20dei%20reali.md#^definizione-parte-interna-di-un-insieme) e la [frontiera](Topologia%20dei%20reali.md#^definizione-frontiera-di-un-insieme) di $A$:
> 
> $$
> A \subseteq \text{int}(A) \cup \partial A
> $$
> 
> Ossia, ogni punto%% Link %% $x_0 \in A$ è o un [punto interno](Topologia%20dei%20reali.md#^definizione-punto-interno) o un [punto di frontiera](Topologia%20dei%20reali.md#^definizione-punto-di-frontiera) di $A$:
> 
> $$
> \forall x_0 \in A (x_0 \in \text{int}(A) \lor x_0 \in \partial A)
> $$

%% dimostrazione a pagina 123 %%

> [!proposizione]+ Proposizione
> 
> Dato un [insieme](Matematica/Teoria%20degli%20insiemi/_index.md#^definizione-insieme) $A \subseteq \mathbb{R}$, $A$ è [chiuso](Topologia%20dei%20reali.md#^definizione-insieme-aperto-o-chiuso-di-r) se e solo se $\partial A \subseteq A$:
> 
> $$
> A \text{ chiuso} \iff \partial A \subseteq A
> $$
> 
> In tal caso, si ha che $A$ è dato dall'unione%% link %% tra la [parte interna](Topologia%20dei%20reali.md#^definizione-parte-interna-di-un-insieme) e la [frontiera](Topologia%20dei%20reali.md#^definizione-frontiera-di-un-insieme) di $A$:
> 
> $$
> A = \text{int}(A) \cup \partial A
> $$

%% dimostrazione a pagina 123 %%

---

> [!fonti]+ Fonti
> 
> - 📚 Sergio Lancelotti, _Lezioni di Analisi Matematica I_, Celid, 2020 (ISBN: `978-8867891979`):
> 	- Capitolo 3 - _Limiti e continuità_:
> 		- 1 - _Topologia di $\mathbb{R}$_.