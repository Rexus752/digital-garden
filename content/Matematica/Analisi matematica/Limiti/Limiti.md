
> [!premessa]+ Premessa
> 
> Ciao! Se è la prima volta che capiti su questo sito, ti consiglio di consultare la [pagina principale](index.md) di questo cosiddetto _Giardino Digitale_ per scoprire meglio cos'è e come navigarlo.
> 
> Lo stato di questa nota è al momento: 🔴 <font color="#FF7F7F">_Bozza_</font>.

%% 
in realtà è **Calcolo infinitesimale**
%%

---

Introduciamo una delle nozioni più importanti dell'analisi matematica%% link %%, ossia quella di [_limite_](Limiti.md#^definizione-limite). È alla base di altre nozioni fondamentali, quali ad esempio quella di _derivata_%% link %% e di _integrale_%% link %%. Prima di vedere la definizione, introduciamo questo concetto attraverso alcuni esempi che ci permettono di capire il suo significato.

# 1 - Introduzione ai limiti

## 1.1 - Limite finito al finito

Immaginiamo di avere una [funzione](Funzioni.md#^definizione-funzione)

$$
\begin{align*}
f \colon \mathbb{R} \setminus \{ 1 \} & \to \mathbb{R} \\
x & \mapsto \dfrac{x^2-1}{x-1}
\end{align*}
$$

Ovviamente sappiamo che questa [funzione](Funzioni.md#^definizione-funzione) non è definita per $x = 1$. Tuttavia, quando $x$ si avvicina al punto%% link %% $1$, la [funzione](Funzioni.md#^definizione-funzione) come si comporta? Cosa fa? Questa funzione è fisicamente una funzione?

Diciamo quindi che vogliamo scoprire cosa succede quando $x$ _tende_ a $1$, cioè quando si avvicina ai punti%% link %% intorno all'$1$ ma non assume il valore%% Link %% $1$. Indichiamo questa cosa con

$$
x \to 1
$$

Proviamo ad analizzare il comportamento di $f$ quando $x \to 1$, sia avvicinandoci a $1$ da "sinistra" (cioè partendo da valori minori di $1$), sia da "destra" (cioè partendo da valori maggiori di $1$):

| $x$    | $f(x)$ |
| ------ | ------ |
| $0$    | $1$    |
| $0.5$  | $1.5$  |
| $0.9$  | $1.9$  |
| $0.95$ | $1.95$ |
| $0.99$ | $1.99$ |
| $1.01$ | $2.01$ |
| $1.05$ | $2.05$ |
| $1.1$  | $2.1$  |
| $1.5$  | $2.5$  |

Possiamo ipotizzare che, per $x \to 1$, $f$ tenda a $2$. Però ora ci chiediamo: quanto vicino a $1$ deve stare la $x$ affinché $f(x)$ si trovi a una distanza%% link %% da $2$ inferiore (per esempio) a $0.01$ (cioè al massimo $2 \pm 0.01$)? Per definizione di _distanza_%% link %%, abbiamo che

$$
\begin{align*}
d(f(x), 2) < 0.01 &\iff |f(x) - 2| < 0.01
\end{align*}
$$

Quindi, per [definizione di _intorno_](Topologia%20dei%20reali.md#^definizione-intorno-di-un-punto), possiamo riscrivere che se $x$ si trova in un [intorno](Topologia%20dei%20reali.md#^definizione-intorno-di-un-punto) di $1$ di raggio $0.01$ (cioè $x \in (0.99, 1.01)$), allora $f(x)$ si troverà in un [intorno](Topologia%20dei%20reali.md#^definizione-intorno-di-un-punto) di $2$ di raggio $0.01$ (cioè $f(x) \in (1.99, 2.01)$):

$$
x \in I_{0.01}(1) \implies f(x) \in I_{0.01}(2)
$$

Ma invece di fissare come soglia $0.01$, possiamo prendere un qualsiasi numero $\varepsilon > 0$ piccolo a piacere e chiederci: quanto vicino a $1$ devo prendere $x$ affinché $x+1$ sia a una distanza da $2$ inferiore a $\varepsilon$?

$$
\forall \varepsilon > 0 . \left( x \in I_{\varepsilon}(1) \implies f(x) \in I_{\varepsilon}(2) \right)
$$

Riassumiamo tutta questa pappardella nella notazione del _limite_, scrivendo così:

$$
\lim_{x \to 1} f(x) = 2
$$

Questa notazione significa che, per ogni distanza $\varepsilon > 0$ di $x$ da $1$, esiste un valore $\delta$ (in questo caso uguale a $\varepsilon$) che indica la distanza di $f(x)$ da $2$, tale che se $x \in I_\delta(1)$ (cioè se $x$ ha una distanza da $1$ minore di $\delta$) allora $f(x) \in I_\varepsilon(2)$ (cioè $f(x)$ avrà una distanza da $2$ sicuramente minore di $\varepsilon$).

Non è un concetto semplice da capire, ma proseguendo più in là ci verrà naturale capire cosa stiamo provando a dire qui.

Esistono vari "tipi" di _limite_ e questo è detto _limite finito al finito_ perché se $x$ tende a un valore finito%% link %% $c \in \mathbb{R}$ allora la $f(x)$ tenderà a un valore finito%% link %% $l \in \mathbb{R}$.

> [!definizione]+ Definizione: limite finito al finito
> 
> Data una [funzione](Funzioni.md#^definizione-funzione) $f \colon I_r(c) \setminus \{ c \} \to \mathbb{R}$ per qualche $r > 0$ e $c \in \mathbb{R}$, si dice che **$f$ ammette limite finito $l$ per $x$ che tende a $c$** e si scrive
> 
> $$
> \lim_{x \to c} f(x) = l
> $$
> 
> se
> 
> $$
> \forall \varepsilon > 0, \exists \delta > 0, \forall x \in \mathbb{R} . \left( x \in I_\delta(c) \setminus \{ c \} \implies f(x) \in I_\varepsilon(l) \right) 
> $$
^definizione-limite-finito-al-finito

%% 
fare interpretazione grafica di questo caso specifico del limite
%%

%% 
siamo sicuri che $\forall x \in \mathbb{R}$ e non $\forall x \in \mathbb{R} \cup \{ \pm \infty \}$?
nel caso andrebbe modificato anche negli altri 3 casi e nella definizione generale
%%

> [!osservazione]+ Osservazione: definizione alternativa di _limite finito al finito_
> 
> Nella [definizione di _limite finito al finito_](Limiti.md#^definizione-limite-finito-al-finito) gli [intorni](Topologia%20dei%20reali.md#^definizione-intorno-di-un-punto) possono essere sostituiti dalla distanza%% link %% sfruttando la [definizione stessa di _intorno_](Topologia%20dei%20reali.md#^definizione-intorno-di-un-punto):
> 
> $$
> \begin{array}{}
> \displaystyle\lim_{x \to c} f(x) = l \\
> \Updownarrow \\
> \forall \varepsilon > 0, \exists \delta > 0, \forall x \in \mathbb{R} . \left( 0 < |x - c| < \delta \implies |f(x) - l| < \varepsilon  \right) 
> \end{array}
> $$
^osservazione-definizione-alternativa-di-limite-finito-al-finito

> [!osservazione]+ Osservazione: dipendenza di $\color{#7F7F7F} \delta$ da $\color{#7F7F7F} \varepsilon$
> 
> Il valore di $\delta$ dipende da $\varepsilon$ perché, a seconda di quanto piccolo scegliamo $\varepsilon$, il $\delta$ sarà sufficientemente piccolo da rispettare la [definizione di _limite finito al finito_](Limiti.md#^definizione-limite-finito-al-finito).
> 
> Per questo motivo, alcuni usano la notazione $\delta(\varepsilon)$ per indicare che $\delta$ è in funzione di $\varepsilon$.

%%
1. Il limite per $x \to c$ non prescrive il comportamento della funzione in $x = c$, cioè non è necessario che la funzione sia definita anche in $c$.
	Esempio:
	- Una funzione non definita in $c$
	- Una funzione per cui $f(x) = l$
	- Una funzione per cui $f(x) \ne l$
	hanno tutte limite uguale a $l$!

Questa osservazione varrà anche per gli altri tipi di limite, ossia il limite infinito all'infinito, finito all'infinito e infinito al finito.
%%

> [!esempio]- Esempio di limite finito al finito
> 
> Riprendendo la [funzione](Funzioni.md#^definizione-funzione) di prima
> 
> $$
> f(x) = \dfrac{x^2 - 1}{x - 1}
> $$
> 
> vogliamo dimostrare che vale il [limite finito al finito](Limiti.md#^definizione-limite-finito-al-finito)
> 
> $$
> \lim_{x \to 1} f(x) = 2
> $$
> 
> proprio sfruttando questa definizione, che ci dice che, per un $\varepsilon$ qualsiasi, esiste un $\delta$ tale che, per ogni $x \in \text{dom}(f)$, se la distanza%% link %% tra questi e $x_0$ è minore di $\delta$ allora la distanza%% Link %% tra le loro immagini%% Link %% ed $l$ è minore di $\varepsilon$.
> 
> Per esempio, prendiamo il punto%% link %% $x' = 1.4$ distante da $x_0$ per $\delta' = |x' - x_0| = 0.4$ la cui immagine%% Link %% $f(x') = f(1.4) = 2.4$ è distante da $l=2$ per un valore $\varepsilon' = f(x') - l = 0.4$.
> 
> Prendiamo tutti i punti%% link %% $x_1 = 1.05, x_2 = 1.1, \ldots$ più vicini a $x_0$ di quanto non lo sia $x'$, ossia con distanze%% Link %%
> 
> $$
> \begin{array}{}
> \delta_1 = |x_1 - x_0| = 0.05 \\
> \delta_2 = |x_2 - x_0| = 0.01 \\
> \ldots
> \end{array}
> $$
> 
> Questi punti avranno la propria immagine%% Link %% $f(x_1) = 2.05, f(x_2) =2.1, \ldots$ molto più vicina a $l$ di quanto non lo sia quella di $f(x)$, cioè $\varepsilon' = 0.4$:
> 
> $$
> \begin{array}{}
> \varepsilon_1 = |f(x_1) - l| = 0.05 \\
> \varepsilon_2 = |f(x_2) - l| = 0.01 \\
> \ldots
> \end{array}
> $$
> 
> Riassumendo, abbiamo:
> 
> | Valori di $x$ | $\delta = \vert x - x_0 \vert$ | $f(x)$          | $\varepsilon = \vert f(x) - l \vert$ |
> | ------------- | ------------------------------ | --------------- | ------------------------------------ |
> | $x' = 1.4$    | $\delta' = 0.4$                | $f(x') = 2.4$   | $\varepsilon' = 0.4$                 |
> | $x_2 = 1.1$   | $\delta_2 = 0.1$               | $f(x_2) = 2.1$  | $\varepsilon_2 = 0.1$                |
> | $x_1 = 1.05$  | $\delta_1 = 0.05$              | $f(x_1) = 2.05$ | $\varepsilon_1 = 0.5$                |
> 
> Abbiamo cioè dimostrato che, per un $\varepsilon$ qualsiasi (in questo caso $\varepsilon' = 0.4$), esiste un $\delta$ (in questo caso $\delta' = 0.4$) tale che, per ogni $x \in \text{dom}(f)$ (come, per esempio, $x_1$ e $x_2$), se la distanza tra questi ($x_1$ e $x_2$) e $x_0$ è minore di $\delta$ allora la distanza tra le loro immagini%% Link %% ($f(x_1)$ ed $f(x_2)$) ed $l$ è minore di $\varepsilon$.

%% rappresentare graficamente %%

> [!osservazione]+ Osservazione: basta un $\color{#7F7F7F} \delta$ qualsiasi nel limite finito al finito
> 
> In un [limite finito al finito](Limiti.md#^definizione-limite-finito-al-finito) non è importante trovare il miglior $\delta$, cioè la distanza minore possibile tra $f(x)$ ed $l$, ma ne basta uno qualunque che funzioni.
> 
> Per esempio, consideriamo la [funzione](Funzioni.md#^definizione-funzione) $f \colon \mathbb{R} \to \mathbb{R}$ definita da
> 
> $$
> f(x) = \begin{cases}
> 3x + 2 & \text{se } x \ne 1 \\
> 4 & \text{se } x = 1
> \end{cases}
> $$
> 
> Vogliamo dimostrare che vale il [limite](Limiti.md#^definizione-limite-finito-al-finito)
> 
> $$
> \lim_{x \to 1} f(x) = 5
> $$
> 
> Secondo la [definizione alternativa del _limite finito al finito_](Limiti.md#^osservazione-definizione-alternativa-di-limite-finito-al-finito), abbiamo che
> 
> $$
> \forall \varepsilon > 0, \exists \delta > 0, \forall x \in \mathbb{R} . \big( 0 < |x - 1| < \delta \implies |f(x) - 5| < \varepsilon \big)
> $$
> 
> Consideriamo un $\varepsilon > 0$ qualunque: esiste un $\delta$ che rispetta questa [definizione](Limiti.md#^definizione-limite-finito-al-finito)?
> 
> Partiamo dall'obiettivo che vogliamo dimostrare, cioè che $|f(x) - 5| < \varepsilon$. Si ha che, se $x \ne x_0 = 1$ allora, per la definizione di questa [funzione](Funzioni.md#^definizione-funzione), abbiamo che
> 
> $$
> \begin{array}{}
> |f(x) - 5| < \varepsilon \\
> \Updownarrow \\
> |(3x+2) - 5| < \varepsilon \\
> \Updownarrow \\
> |3x - 3| < \varepsilon \\
> \Updownarrow \\
> |x - 1| < \dfrac{\varepsilon}{3}
> \end{array}
> $$
> 
> Dato che abbiamo anche che $|x-1| < \delta$, poniamo arbitrariamente $\displaystyle\delta = \dfrac{\varepsilon}{3}$, che non è necessariamente il $\delta$ più piccolo che possiamo prendere in questo [limite](Limiti.md#^definizione-limite-finito-al-finito).
> 
> Ciò ci porta al fatto che, per ogni $x$ tale che $0 < |x-1| < \delta$, soddisfiamo automaticamente l'obiettivo $|f(x) - 5| < \varepsilon$, verificando così il [limite](Limiti.md#^definizione-limite-finito-al-finito).
>  
> Perché $\displaystyle\delta = \dfrac{\varepsilon}{3}$ è "arbitrario"? Perché avremmo potuto prendere $\displaystyle\delta = \dfrac{\varepsilon}{4}$ o $\displaystyle\delta = \dfrac{\varepsilon}{10}$ o qualunque altro valore più piccolo di $\dfrac{\varepsilon}{3}$, ma tanto funzionerebbero tutti: $\dfrac{\varepsilon}{3}$ è semplicemente il più comodo che emerge dal calcolo.
> 
> Notiamo anche il fatto che $f(1) = 4 \ne 5$, ma è irrilevante: la condizione $0 < |x - 1|$ esclude esattamente $x = 1$, quindi il valore in quel punto%% link %% non conta.

%% continua dall'ultima frase a pagina 128 a pagina 129 di Lancelotti %%

%% 
Questa osservazione vale anche per gli altri tipi di limite, ossia il limite infinito all'infinito, finito all'infinito e infinito al finito, anche se la rivedremo ogni volta adattandola al caso specifico
%%

## 1.2 - Limite infinito all'infinito

Immaginiamo di avere una [funzione](Funzioni.md#^definizione-funzione)

$$
\begin{align*}
f \colon \mathbb{R} & \to \mathbb{R} \\
x & \mapsto x^2
\end{align*}
$$

Questa [funzione](Funzioni.md#^definizione-funzione) è definita ovunque, quindi non c'è nessun punto "proibito". Tuttavia, ci chiediamo una cosa diversa: cosa succede ai valori di $f(x)$ quando $x$ diventa arbitrariamente grande? Esiste un valore verso cui $f$ tende?

Diciamo quindi che vogliamo scoprire cosa succede quando $x$ _tende_ a $+\infty$, cioè quando cresce senza mai fermarsi. Indichiamo questa cosa con

$$
x \to +\infty
$$

Proviamo ad analizzare il comportamento di $f$ quando $x \to +\infty$, osservando cosa succede ai valori di $f(x)$ man mano che $x$ cresce:

| $x$     | $f(x)$        |
| ------- | ------------- |
| $1$     | $1$           |
| $10$    | $100$         |
| $100$   | $10'000$      |
| $1000$  | $1'000'000$   |
| $10000$ | $100'000'000$ |

Possiamo ipotizzare che, per $x \to +\infty$, anche $f(x)$ tenda a $+\infty$. Però ora ci chiediamo: quanto grande deve essere $x$ affinché $f(x)$ superi (per esempio) la soglia $10^4$?

$$
\begin{align*}
f(x) > 10^4 &\iff x^2 > 10^4 \\
&\iff x > 10^2 \\
&\iff x > 100
\end{align*}
$$

Quindi, se $x$ si trova oltre la soglia $100$, allora $f(x)$ si troverà sicuramente oltre la soglia $10^4$:

$$
x > 100 \implies f(x) > 10^4
$$

Ma invece di fissare come soglia $10^4$, possiamo prendere un qualsiasi valore%% link %% $M > 0$ grande a piacere e chiederci: quanto grande deve essere $x$ affinché $f(x)$ superi $M$?

$$
f(x) > M \iff x^2 > M \iff x > \sqrt{M}
$$

Otteniamo quindi che:

$$
\forall M > 0 .\ \left( x > \sqrt{M} \implies f(x) > M \right)
$$

Possiamo riassumere tutto ciò nella seguente notazione:

$$
\lim_{x \to +\infty} f(x) = +\infty
$$

Questa notazione significa che, per ogni soglia $M > 0$ grande quanto vogliamo, esiste un valore $K$ (in questo caso uguale a $\sqrt{M}$) tale che se $x > K$ allora $f(x) > M$.

Questo tipo di limite è detto _limite infinito all'infinito_ perché se $x$ tende a un valore infinito%% link %% (cioè $x \to +\infty$) allora anche $f(x)$ tenderà a un valore infinito%% link %% (cioè $f(x) \to +\infty$).

> [!definizione]+ Definizione: limite infinito all'infinito
> 
> Data una [funzione](Funzioni.md#^definizione-funzione) $f \colon (a, +\infty) \to \mathbb{R}$ per qualche $a \in \mathbb{R}$, si dice che:
> - **$f$ ammette limite $+\infty$ per $x$ che tende a $+\infty$** se:
> 	$$
> 	\begin{array}{}
> 	\displaystyle\lim_{x \to +\infty} f(x) = +\infty \\
> 	\Updownarrow \\
> 	\forall M > 0, \exists K > 0, \forall x \in \mathbb{R} .\ \left( x > K \implies f(x) > M \right)
> 	\end{array}
> 	$$
> - **$f$ ammette limite $-\infty$ per $x$ che tende a $+\infty$** se:
> 	$$
> 	\begin{array}{}
> 	\displaystyle\lim_{x \to +\infty} f(x) = -\infty \\
> 	\Updownarrow \\
> 	\forall M > 0, \exists K > 0, \forall x \in \mathbb{R} .\ \left( x > K \implies f(x) < -M \right)
> 	\end{array}
> 	$$
> - **$f$ ammette limite $+\infty$ per $x$ che tende a $-\infty$** se:
> 	$$
> 	\begin{array}{}
> 	\displaystyle\lim_{x \to -\infty} f(x) = +\infty \\
> 	\Updownarrow \\
> 	\forall M > 0, \exists K > 0, \forall x \in \mathbb{R} .\ \left( x < - K \implies f(x) > M \right)
> 	\end{array}
> 	$$
> - **$f$ ammette limite $-\infty$ per $x$ che tende a $-\infty$** se:
> 	$$
> 	\begin{array}{}
> 	\displaystyle\lim_{x \to -\infty} f(x) = -\infty \\
> 	\Updownarrow \\
> 	\forall M > 0, \exists K > 0, \forall x \in \mathbb{R} .\ \left( x < -K \implies f(x) < -M \right)
> 	\end{array}
> 	$$
^definizione-limite-infinito-all-infinito

%% 
siamo sicuri che $f \colon (a, + \infty) \to \mathbb{R}$ vada bene anche per $x \to - \infty$?
%%

%% 
fare interpretazione grafica di questo caso specifico del limite
%%

> [!esempio]- Esempio di limite infinito all'infinito
> 
> Prendendo la [funzione](Funzioni.md#^definizione-funzione)
> 
> $$
> f(x) = x^2
> $$
> 
> vogliamo dimostrare che vale il [limite infinito all'infinito](Limiti.md#^definizione-limite-infinito-all-infinito)
> 
> $$
> \lim_{x \to +\infty} f(x) = +\infty
> $$
> 
> proprio sfruttando la [definizione del _limite infinito all'infinito_](Limiti.md#^definizione-limite-infinito-all-infinito), che ci dice che, per una soglia $M$ qualsiasi, esiste un $K$ tale che, per ogni $x \in \text{dom}(f)$, se $x > K$ allora $f(x) > M$.
> 
> Per esempio, prendiamo la soglia $M' = 100$: vogliamo trovare un $K'$ tale che, per ogni $x > K'$, si abbia $f(x) > M' = 100$. Notiamo che ci basta prendere $K' = \sqrt{100} = 10$: infatti, per $x = 11$ si ha $f(11) = 121 > M' = 100$.
> 
> Prendiamo ora soglie $M_1 = 10'000, M_2 = 1'000'000, \ldots$ sempre più grandi di $M'$: per ciascuna basterà prendere $K_1 = \sqrt{10'000} = 100$, $K_2 = \sqrt{1'000'000} = 1000$, $\ldots$ e tutti i punti $x > K_i$ avranno immagine oltre la soglia corrispondente:
> 
> | **Soglia $M$** | $K = \sqrt{M}$ | **Esempio di $x > K$** | $f(x) = x^2$ |
> | --- | --- | --- | --- |
> | $M' = 100$ | $K' = 10$ | $x = 11$ | $f(11) = 121$ |
> | $M_1 = 10'000$ | $K_1 = 100$ | $x = 101$ | $f(101) = 10'201$ |
> | $M_2 = 1'000'000$ | $K_2 = 1000$ | $x = 1001$ | $f(1001) = 1'002'001$ |
> 
> Abbiamo cioè dimostrato che, per una soglia $M$ qualsiasi (per esempio $M' = 100$), esiste un $K$ (in questo caso $K' = 10$) tale che, per ogni $x > K$ (come $x = 11, 12, \ldots$), si ha $f(x) > M$.

> [!osservazione]+ Osservazione: basta un $\color{#7F7F7F} K$ qualsiasi nel limite infinito all'infinito
> 
> In un [limite infinito all'infinito](Limiti.md#^definizione-limite-infinito-all-infinito) non è importante trovare il miglior $K$, cioè la soglia più piccola possibile oltre la quale $f(x) > M$, ma ne basta uno qualunque che funzioni.
> 
> Per esempio, consideriamo la [funzione](Funzioni.md#^definizione-funzione) $f \colon \mathbb{R} \to \mathbb{R}$ definita da
> 
> $$
> f(x) = 2x^2 + 1
> $$
> 
> Vogliamo dimostrare che vale il [limite](Limiti.md#^definizione-limite-infinito-all-infinito)
> 
> $$
> \lim_{x \to +\infty} f(x) = +\infty
> $$
> 
> Secondo la [definizione del _limite infinito all'infinito_](Limiti.md#^definizione-limite-infinito-all-infinito), abbiamo che
> 
> $$
> \forall M > 0, \exists K > 0, \forall x \in \mathbb{R} . \big( x > K \implies 2x^2 + 1 > M \big)
> $$
> 
> Consideriamo un $M > 0$ qualunque: esiste un $K$ che rispetta questa definizione?
> 
> Partiamo dall'obiettivo che vogliamo dimostrare, cioè che $2x^2 + 1 > M$. Si ha che
> 
> $$
> \begin{array}{}
> 2x^2 + 1 > M \\
> \Updownarrow \\
> x^2 > \dfrac{M-1}{2} \\
> \Updownarrow \\
> x > \sqrt{\dfrac{M-1}{2}}
> \end{array}
> $$
> 
> Dato che, per definizione, abbiamo anche $x > K$, poniamo arbitrariamente $\displaystyle K = \sqrt{\dfrac{M-1}{2}}$, che non è necessariamente il $K$ più piccolo che possiamo prendere in questo [limite](Limiti.md#^definizione-limite-infinito-all-infinito).
> 
> Ciò ci porta al fatto che, per ogni $x$ tale che $x > K$, soddisfiamo automaticamente l'obiettivo $2x^2 + 1 > M$, verificando così il [limite](Limiti.md#^definizione-limite-infinito-all-infinito).
> 
> Perché $\displaystyle K = \sqrt{\dfrac{M-1}{2}}$ è "arbitrario"? Perché avremmo potuto prendere $K = \sqrt{\dfrac{M}{2}}$ o $K = \sqrt{M}$ o qualunque altro valore più grande di $\sqrt{\dfrac{M-1}{2}}$, ma tanto funzionerebbero tutti: $\sqrt{\dfrac{M-1}{2}}$ è semplicemente il più preciso che emerge dal calcolo.

---

Immaginiamo di avere una [funzione](Funzioni.md#^definizione-funzione)
$$
\begin{align*}
f \colon \mathbb{R} & \to \mathbb{R} \\
x & \mapsto 2x^2 - x
\end{align*}
$$

Quando la [variabile indipendente](Funzioni.md#^definizione-funzione) $x$ diventa _arbitrariamente grande_,, si dice che $x$ _tende all'infinito_ o, più precisamente, $x$ _tende a più infinito_ e si indica con

$$
x \to + \infty
$$

Analizziamo il comportamento di $f$ quando $x \to + \infty$ (usando la notazione scientifica%% link %%):

| $x$    | $f(x) = 2x^2 - x$    |
| ------ | -------------------- |
| $10^1$ | $1.9 \cdot 10^2$     |
| $10^2$ | $1.99 \cdot 10^4$    |
| $10^3$ | $1.99 \cdot 10^6$    |
| $10^4$ | $1.99 \cdot 10^8$    |
| $10^5$ | $1.99 \cdot 10^{10}$ |

Da questa tabella si intuisce che al tendere di $x$ all'infinito i valori%% link %% di $f(x)$ diventano sempre più grandi. Con il linguaggio introdotto in precedenza possiamo affermare che anche $f(x)$ tende a più infinito: esprimiamo questo fatto con la scrittura

$$
\lim_{x \to + \infty} f(x) = + \infty
$$

che si legge _limite per $x$ che tende a più infinito di $f(x)$ uguale a più infinito_.

Consideriamo ora la [funzione](Funzioni.md#^definizione-funzione)

$$
\begin{align*}
g \colon (-\infty, 0) \cup (0, +\infty) & \to \mathbb{R} \\
x & \mapsto \dfrac{1}{x}
\end{align*}
$$

%% mettere grafico %%

Siamo interessati a conoscere qual è il comportamento di $g$ quando la variabile%% link %% $x$ si avvicina sempre di più al punto%% link %% $x_0 = 0$. Osserviamo che, per $x \to 0$ con $x>0$, il valore di $g(x) = \dfrac{1}{x}$ diventa sempre più positivo, mentre per $x \to 0$ con $x < 0$ il valore di $g(x) = \dfrac{1}{x}$ diventa sempre più negativo.

Se, tuttavia, $x$ si avvicina a $x_0 = 0$ in modo casuale, cambiando anche segno, e "saltando" da un lato all'altro rispetto allo $0$, non possiamo dire con certezza se sta diventando sempre più positivo o sempre più negativo, quindi potremmo concludere che per $x \to 0$ si ha che $g(x)$ non ha un comportamento ben determinato e il _limite_ di $g(x)$ per $x \to 0$ non esiste. Ecco che quindi, in questo caso, dobbiamo necessariamente specificare da quale lato vogliamo avvicinarci allo $0$, se da destra o da sinistra.

Da questi esempi si capisce che la nozione di [_limite_](Limiti.md#^definizione-limite) ci dice qual è il _comportamento_ (o _andamento_) di una [funzione](Funzioni.md#^definizione-funzione) e dei valori che essa può assumere a seconda di come la sua variabile indipendente%% link %% _tende_ a un determinato "punto"%% link %% (e qui la parola _punto_ viene messa tra virgolette perché la variabile%% link %% può anche tendere verso $+\infty$ o $-\infty$ che **non** sono punti%% link %% di $\mathbb{R}$).

## 1.3 - Limite finito all'infinito

Immaginiamo ora di avere una [funzione](Funzioni.md#^definizione-funzione)

$$
\begin{align*}
f \colon \mathbb{R} \setminus \{0\} & \to \mathbb{R} \\
x & \mapsto \dfrac{1}{x}
\end{align*}
$$

Questa [funzione](Funzioni.md#^definizione-funzione) è definita ovunque tranne che in $x = 0$. Ci chiediamo: cosa succede ai valori di $f(x)$ quando $x$ diventa arbitrariamente grande? Esiste un valore finito verso cui $f$ tende?

Diciamo quindi che vogliamo scoprire cosa succede quando $x$ _tende_ a $+\infty$. Proviamo ad analizzare il comportamento di $f$ quando $x \to +\infty$:

| $x$      | $f(x)$       |
| -------- | ------------ |
| $1$      | $1$          |
| $10$     | $0.1$        |
| $100$    | $0.01$       |
| $1000$   | $0.001$      |
| $10000$  | $0.0001$     |

Possiamo ipotizzare che, per $x$ che tende a $+ \infty$, $f(x)$ tenda a $0$. Però ora ci chiediamo: quanto grande deve essere $x$ affinché $f(x)$ si trovi a una distanza da $0$ inferiore (per esempio) a $10^{-2}$?

$$
\begin{align*}
|f(x) - 0| < 10^{-2} &\iff \left|\dfrac{1}{x}\right| < 10^{-2} \\
&\iff \dfrac{1}{x} < 10^{-2} \\
&\iff x > 10^{2} = 100
\end{align*}
$$

Quindi, se $x > 100$, allora $f(x)$ si troverà sicuramente entro una distanza $10^{-2}$ da $0$:

$$
x > 100 \implies |f(x) - 0| < 10^{-2}
$$

Ma invece di fissare come soglia $10^{-2}$, possiamo prendere un qualsiasi valore $\varepsilon > 0$ piccolo a piacere e chiederci: quanto grande deve essere $x$ affinché $|f(x) - 0| < \varepsilon$?

$$
|f(x) - 0| < \varepsilon \iff \dfrac{1}{x} < \varepsilon \iff x > \dfrac{1}{\varepsilon}
$$

Otteniamo quindi che:

$$
\forall \varepsilon > 0 .\ \left( x > \dfrac{1}{\varepsilon} \implies |f(x) - 0| < \varepsilon \right)
$$

Possiamo riassumere tutto ciò nella seguente notazione:

$$
\lim_{x \to +\infty} f(x) = 0
$$

Questa notazione significa che, per ogni soglia $\varepsilon > 0$ piccola quanto vogliamo, esiste un valore $K$ (in questo caso uguale a $\dfrac{1}{\varepsilon}$) tale che se $x > K$ allora $|f(x) - 0| < \varepsilon$.

Questo tipo di limite è detto _limite finito all'infinito_ perché se $x$ tende a un valore infinito (cioè $x \to +\infty$) allora $f(x)$ tende a un valore finito (cioè $f(x) \to 0$).

> [!definizione]+ Definizione: limite finito all'infinito
> 
> Data una [funzione](Funzioni.md#^definizione-funzione) $f \colon (a, +\infty) \to \mathbb{R}$ per qualche $a \in \mathbb{R}$ e $l \in \mathbb{R}$, si dice che:
> - **$f$ ammette limite $l$ per $x$ che tende a $+\infty$** se:
> 	$$
> 	\begin{array}{}
> 	\displaystyle\lim_{x \to +\infty} f(x) = l \\
> 	\Updownarrow \\
> 	\forall \varepsilon > 0, \exists K > 0, \forall x \in \mathbb{R} .\ \left( x > K \implies |f(x) - l| < \varepsilon \right)
> 	\end{array}
> 	$$
> - **$f$ ammette limite $l$ per $x$ che tende a $-\infty$** se:
> 	$$
> 	\begin{array}{}
> 	\displaystyle\lim_{x \to -\infty} f(x) = l \\
> 	\Updownarrow \\
> 	\forall \varepsilon > 0, \exists K > 0, \forall x \in \mathbb{R} .\ \left( x < -K \implies |f(x) - l| < \varepsilon \right)
> 	\end{array}
> 	$$
> ^definizione-limite-finito-all-infinito

%% 
fare interpretazione grafica di questo caso specifico del limite
%%

> [!esempio]- Esempio di limite finito all'infinito
> 
> Prendendo la [funzione](Funzioni.md#^definizione-funzione)
> 
> $$
> f(x) = \dfrac{1}{x}
> $$
> 
> vogliamo dimostrare che vale il [limite finito all'infinito](Limiti.md#^definizione-limite-finito-all-infinito)
> 
> $$
> \lim_{x \to +\infty} f(x) = 0
> $$
> 
> proprio sfruttando la [definizione del _limite finito all'infinito_](Limiti.md#^definizione-limite-finito-all-infinito), che ci dice che, per una tolleranza $\varepsilon$ qualsiasi, esiste un $K$ tale che, per ogni $x > K$, si ha $|f(x) - 0| < \varepsilon$.
> 
> Per esempio, prendiamo $\varepsilon' = 0.01$: vogliamo trovare un $K'$ tale che, per ogni $x > K'$, si abbia $|f(x)| < 0.01$. Ci basta prendere $K' = \dfrac{1}{0.01} = 100$: infatti, per $x = 200$ si ha $f(200) = 0.005 < 0.01$.
> 
> Prendiamo ora tolleranze $\varepsilon_1 = 0.001, \varepsilon_2 = 0.0001, \ldots$ sempre più piccole: per ciascuna basterà prendere $K_1 = 1000$, $K_2 = 10'000$, $\ldots$:
> 
> | **Tolleranza $\varepsilon$** | $K = \frac{1}{\varepsilon}$ | **Esempio di $x > K$** | $f(x) = \frac{1}{x}$ |
> | --- | --- | --- | --- |
> | $\varepsilon' = 0.01$ | $K' = 100$ | $x = 200$ | $f(200) = 0.005$ |
> | $\varepsilon_1 = 0.001$ | $K_1 = 1000$ | $x = 2000$ | $f(2000) = 0.0005$ |
> | $\varepsilon_2 = 0.0001$ | $K_2 = 10'000$ | $x = 20'000$ | $f(20'000) = 0.00005$ |
> 
> Abbiamo cioè dimostrato che, per una tolleranza $\varepsilon$ qualsiasi, esiste un $K$ tale che, per ogni $x > K$, si ha $|f(x) - 0| < \varepsilon$.

> [!osservazione]+ Osservazione: basta un $\color{#7F7F7F} K$ qualsiasi nel limite finito all'infinito
> 
> In un [limite finito all'infinito](Limiti.md#^definizione-limite-finito-all-infinito) non è importante trovare il miglior $K$, cioè la soglia più piccola possibile oltre la quale $|f(x) - l| < \varepsilon$, ma ne basta uno qualunque che funzioni.
> 
> Per esempio, consideriamo la [funzione](Funzioni.md#^definizione-funzione) $f \colon \mathbb{R} \setminus \{0\} \to \mathbb{R}$ definita da
> 
> $$
> f(x) = \dfrac{1}{x^2} + 3
> $$
> 
> Vogliamo dimostrare che vale il [limite](Limiti.md#^definizione-limite-finito-all-infinito)
> 
> $$
> \lim_{x \to +\infty} f(x) = 3
> $$
> 
> Secondo la [definizione del _limite finito all'infinito_](Limiti.md#^definizione-limite-finito-all-infinito), abbiamo che
> 
> $$
> \forall \varepsilon > 0, \exists K > 0, \forall x \in \mathbb{R} .\ \big( x > K \implies |f(x) - 3| < \varepsilon \big)
> $$
> 
> Consideriamo un $\varepsilon > 0$ qualunque: esiste un $K$ che rispetta questa definizione?
> 
> Partiamo dall'obiettivo che vogliamo dimostrare, cioè che $|f(x) - 3| < \varepsilon$. Si ha che
> 
> $$
> \begin{array}{}
> |f(x) - 3| < \varepsilon \\
> \Updownarrow \\
> \left|\dfrac{1}{x^2}\right| < \varepsilon \\
> \Updownarrow \\
> \dfrac{1}{x^2} < \varepsilon \\
> \Updownarrow \\
> x > \dfrac{1}{\sqrt{\varepsilon}}
> \end{array}
> $$
> 
> Dato che, per definizione, abbiamo anche $x > K$, poniamo arbitrariamente $K = \dfrac{1}{\sqrt{\varepsilon}}$, che non è necessariamente il $K$ più piccolo che possiamo prendere in questo [limite](Limiti.md#^definizione-limite-finito-all-infinito).
> 
> Ciò ci porta al fatto che, per ogni $x > K$, soddisfiamo automaticamente l'obiettivo $|f(x) - 3| < \varepsilon$, verificando così il [limite](Limiti.md#^definizione-limite-finito-all-infinito).
> 
> Perché $K = \dfrac{1}{\sqrt{\varepsilon}}$ è "arbitrario"? Perché avremmo potuto prendere $K = \dfrac{2}{\sqrt{\varepsilon}}$ o $K = \dfrac{1}{\sqrt{\varepsilon}} + 1$ o qualunque altro valore più grande, ma tanto funzionerebbero tutti.

## 1.4 - Limite infinito al finito

Ora analizziamo l'ultimo "tipo" di limite. Immaginiamo di avere una [funzione](Funzioni.md#^definizione-funzione)

$$
\begin{align*}
f \colon \mathbb{R} \setminus \{0\} & \to \mathbb{R} \\
x & \mapsto \dfrac{1}{x^2}
\end{align*}
$$

Questa [funzione](Funzioni.md#^definizione-funzione) non è definita in $x = 0$. Ci chiediamo: cosa succede ai valori di $f(x)$ quando $x$ si avvicina a $0$? Tende a un valore finito, oppure succede qualcos'altro?

Diciamo quindi che vogliamo scoprire cosa succede quando $x$ _tende_ a $0$. Proviamo ad analizzare il comportamento di $f$ quando $x \to 0$, avvicinandoci sia da sinistra che da destra:

| $x$      | $f(x)$         |
| -------- | -------------- |
| $\pm 1$     | $1$            |
| $\pm 0.1$   | $100$          |
| $\pm 0.01$  | $10'000$       |
| $\pm 0.001$ | $1'000'000$    |

Possiamo ipotizzare che, per $x \to 0$, $f(x)$ tenda a $+\infty$. Però ora ci chiediamo: quanto vicino a $0$ deve stare $x$ affinché $f(x)$ superi (per esempio) la soglia $10^4$?

$$
\begin{align*}
f(x) > 10^4 &\iff \dfrac{1}{x^2} > 10^4 \\
&\iff x^2 < 10^{-4} \\
&\iff |x| < 10^{-2} = 0.01
\end{align*}
$$

Quindi, se $x \in I_{0.01}(0)$ (cioè se $x \in (-0.01, 0.01)$), allora $f(x)$ si troverà sicuramente oltre la soglia $10^4$:

$$
x \in I_{0.01}(0) \implies f(x) > 10^4
$$

Ma invece di fissare come soglia $10^4$, possiamo prendere un qualsiasi valore $M > 0$ grande a piacere e chiederci: quanto vicino a $0$ deve stare $x$ affinché $f(x) > M$?

$$
f(x) > M \iff \dfrac{1}{x^2} > M \iff |x| < \dfrac{1}{\sqrt{M}}
$$

Otteniamo quindi che:

$$
\forall M > 0 .\ \left( x \in I_{\cfrac{1}{\sqrt{M}}}(0) \implies f(x) > M \right)
$$

Possiamo riassumere tutto ciò nella seguente notazione:

$$
\lim_{x \to 0} f(x) = +\infty
$$

Questa notazione significa che, per ogni soglia $M > 0$ grande quanto vogliamo, esiste un $\delta$ (in questo caso uguale a $\dfrac{1}{\sqrt{M}}$) tale che se $x \in I_\delta(0) \setminus \{0\}$ allora $f(x) > M$.

Questo tipo di limite è detto _limite infinito al finito_ perché se $x$ tende a un valore finito (cioè $x \to 0$) allora $f(x)$ diverge a $+\infty$. 

> [!definizione]+ Definizione: limite infinito al finito
> 
> Data una [funzione](Funzioni.md#^definizione-funzione) $f \colon I_r(c) \setminus \{c\} \to \mathbb{R}$ per qualche $r > 0$ e $c \in \mathbb{R}$, si dice che:
> - **$f$ ammette limite $+\infty$ per $x$ che tende a $c$** se:
> 	$$
> 	\begin{array}{}
> 	\displaystyle\lim_{x \to c} f(x) = +\infty \\
> 	\Updownarrow \\
> 	\forall M > 0, \exists \delta > 0, \forall x \in \mathbb{R} .\ \left( x \in I_\delta(c) \setminus \{c\} \implies f(x) > M \right)
> 	\end{array}
> 	$$
> - **$f$ ammette limite $-\infty$ per $x$ che tende a $c$** se:
> 	$$
> 	\begin{array}{}
> 	\displaystyle\lim_{x \to c} f(x) = -\infty \\
> 	\Updownarrow \\
> 	\forall M > 0, \exists \delta > 0, \forall x \in \mathbb{R} .\ \left( x \in I_\delta(c) \setminus \{c\} \implies f(x) < -M \right)
> 	\end{array}
> 	$$
> ^definizione-limite-infinito-al-finito

%% 
fare interpretazione grafica di questo caso specifico del limite
%%

> [!esempio]- Esempio di limite infinito al finito
> 
> Prendendo la [funzione](Funzioni.md#^definizione-funzione)
> 
> $$
> f(x) = \dfrac{1}{x^2}
> $$
> 
> vogliamo dimostrare che vale il [limite infinito al finito](Limiti.md#^definizione-limite-infinito-al-finito)
> 
> $$
> \lim_{x \to 0} f(x) = +\infty
> $$
> 
> proprio sfruttando la [definizione del _limite infinito al finito_](Limiti.md#^definizione-limite-infinito-al-finito), che ci dice che, per una soglia $M$ qualsiasi, esiste un $\delta$ tale che, per ogni $x \in I_\delta(0) \setminus \{0\}$, si ha $f(x) > M$.
> 
> Per esempio, prendiamo la soglia $M' = 100$: vogliamo trovare un $\delta'$ tale che, per ogni $x \in I_{\delta'}(0) \setminus \{0\}$, si abbia $f(x) > 100$. Ci basta prendere $\delta' = \dfrac{1}{\sqrt{100}} = 0.1$: infatti, per $x = 0.05$ si ha $f(0.05) = 400 > 100$.
> 
> Prendiamo ora soglie $M_1 = 10'000, M_2 = 1'000'000, \ldots$ sempre più grandi: per ciascuna basterà prendere $\delta$ sempre più piccolo:
> 
> | **Soglia $M$** | $\delta = \frac{1}{\sqrt{M}}$ | **Esempio di $x \in I_\delta(0)$** | $f(x) = \frac{1}{x^2}$ |
> | --- | --- | --- | --- |
> | $M' = 100$ | $\delta' = 0.1$ | $x = 0.05$ | $f(0.05) = 400$ |
> | $M_1 = 10'000$ | $\delta_1 = 0.01$ | $x = 0.005$ | $f(0.005) = 40'000$ |
> | $M_2 = 1'000'000$ | $\delta_2 = 0.001$ | $x = 0.0005$ | $f(0.0005) = 4'000'000$ |
> 
> Abbiamo cioè dimostrato che, per una soglia $M$ qualsiasi, esiste un $\delta$ tale che, per ogni $x \in I_\delta(0) \setminus \{0\}$, si ha $f(x) > M$.

> [!osservazione]+ Osservazione: basta un $\color{#7F7F7F} \delta$ qualsiasi nel limite infinito al finito
> 
> In un [limite infinito al finito](Limiti.md#^definizione-limite-infinito-al-finito) non è importante trovare il miglior $\delta$, cioè il più grande possibile tale che $f(x) > M$ per ogni $x \in I_\delta(c) \setminus \{c\}$, ma ne basta uno qualunque che funzioni.
> 
> Per esempio, consideriamo la [funzione](Funzioni.md#^definizione-funzione) $f \colon \mathbb{R} \setminus \{0\} \to \mathbb{R}$ definita da
> 
> $$
> f(x) = \dfrac{1}{x^2} + x^2
> $$
> 
> Vogliamo dimostrare che vale il [limite](Limiti.md#^definizione-limite-infinito-al-finito)
> 
> $$
> \lim_{x \to 0} f(x) = +\infty
> $$
> 
> Secondo la [definizione del _limite infinito al finito_](Limiti.md#^definizione-limite-infinito-al-finito), abbiamo che
> 
> $$
> \forall M > 0, \exists \delta > 0, \forall x \in \mathbb{R} .\ \big( x \in I_\delta(0) \setminus \{0\} \implies f(x) > M \big)
> $$
> 
> Consideriamo un $M > 0$ qualunque: esiste un $\delta$ che rispetta questa definizione?
> 
> Notiamo che, poiché $x^2 \geq 0$, abbiamo che
> 
> $$
> f(x) = \dfrac{1}{x^2} + x^2 \geq \dfrac{1}{x^2}
> $$
> 
> Quindi ci basta trovare un $\delta$ tale che $\dfrac{1}{x^2} > M$, che è più semplice:
> 
> $$
> \begin{array}{}
> \dfrac{1}{x^2} > M \\
> \Updownarrow \\
> x^2 < \dfrac{1}{M} \\
> \Updownarrow \\
> |x| < \dfrac{1}{\sqrt{M}}
> \end{array}
> $$
> 
> Poniamo quindi arbitrariamente $\delta = \dfrac{1}{\sqrt{M}}$, che non è necessariamente il $\delta$ più grande che possiamo prendere in questo [limite](Limiti.md#^definizione-limite-infinito-al-finito).
> 
> Ciò ci porta al fatto che, per ogni $x \in I_\delta(0) \setminus \{0\}$, si ha $\dfrac{1}{x^2} > M$ e quindi $f(x) \geq \dfrac{1}{x^2} > M$, verificando così il [limite](Limiti.md#^definizione-limite-infinito-al-finito).
> 
> Perché $\delta = \dfrac{1}{\sqrt{M}}$ è "arbitrario"? Perché avremmo potuto prendere qualunque $\delta$ più piccolo, come $\delta = \dfrac{1}{2\sqrt{M}}$ o $\delta = \dfrac{1}{\sqrt{M}+1}$, e funzionerebbero tutti ugualmente.

## 1.5 - Definizione generale di limite

Ora proviamo a riunire questi quattro casi "specifici" in una definizione più generale di _limite_.

> [!definizione]+ Definizione: limite
> 
> Data una [funzione](Funzioni.md#^definizione-funzione) $f \colon \text{dom}(f) \to \mathbb{R}$, un [punto di accumulazione](Topologia%20dei%20reali.md#^definizione-punto-di-accumulazione) $c \in \mathbb{R} \cup \{ \pm \infty \}$ per $\text{dom}(f)$ e un valore%% link %% $l \in \mathbb{R} \cup \{ \pm \infty \}$, diciamo che **$f$ ha limite $l$ per $x$ che tende a $c$** e si scrive
> 
> $$
> \lim_{x \to c} f(x) = l
> $$
> 
> se
> 
> $$
> \forall I_\varepsilon(l), \exists I_\delta(c), \forall x \in \mathbb{R} . \big( x \in I_\delta(c) \cap \text{dom}(f) \setminus \{ c \} \implies f(x) \in I_\varepsilon(l) \big) 
> $$
^definizione-limite

%% 
è necessario che $x \in \text{dom}(f)$ e non solo nell'intorno al più senza $c$ stesso?
%%

%%
I casi specifici si ottengono come istanze particolari:

| $c$ | $l$ | intorno di $c$ | intorno di $l$ |
|---|---|---|---|
| $c \in \mathbb{R}$ | $l \in \mathbb{R}$ | $I_\delta(c)$ | $I_\varepsilon(l)$ |
| $c \in \mathbb{R}$ | $+\infty$ | $I_\delta(c)$ | $(M, +\infty)$ |
| $+\infty$ | $l \in \mathbb{R}$ | $(K, +\infty)$ | $I_\varepsilon(l)$ |
| $+\infty$ | $+\infty$ | $(K, +\infty)$ | $(M, +\infty)$ |

e così via per $-\infty$, i limiti per eccesso/difetto, e i limiti da sinistra/destra.
%%

%% 
mettere vari tipi di limite nella definizione di limite
%%

> [!osservazione]+ Osservazione: non è necessario che $\color{#7F7F7F} c \in \text{dom}(f)$
> 
> Nella [definizione di _limite_](Limiti.md#^definizione-limite), il punto%% link %% $c$ è un [punto di accumulazione](Topologia%20dei%20reali.md#^definizione-punto-di-accumulazione) per $\text{dom}(f)$, quindi può anche **non** appartenere al dominio%% link %%: ecco perché si richiede che $x \ne c$. Un altro motivo per cui ciò accade è che, anche se $c \in \text{dom}(f)$, il [limite](Limiti.md#^definizione-limite), sia che esista sia che non esista, non dipende dal valore%% link %% di $f$ in $c$, ma solo dai valori di $f$ nei punti%% link %% in un [intorno](Topologia%20dei%20reali.md#^definizione-intorno-di-un-punto) di $c$.

%% 
questa osservazione riprende quanto detto prima sul comportamento della funzione nel punto specifico
%%

# 2 - Funzioni senza limite

> [!proposizione]+ Proposizione: la funzione segno $\color{#FF7F7F} \text{sgn}(x)$ non ha limite
> 
> Data la funzione segno%% link %% $\text{sgn} \colon \mathbb{R} \to \mathbb{R}$ definita da
> 
> $$
> \text{sgn}(x) = \begin{cases}
> -1 & \text{se } x < 0 \\
> 0 & \text{se } x = 0 \\
> 1 & \text{se } x > 0
> \end{cases}
> $$
> 
> %% grafico della funzione %%
> 
> il suo [limite](Limiti.md#^definizione-limite)
> 
> $$
> \lim_{x \to 0} \text{sgn}(x)
> $$
> 
> non esiste.

> [!dimostrazione]- Dimostrazione
> 
> Infatti, per assurdo supponiamo che questo limite esista e sia
> 
> $$
> \lim_{x \to 0} \text{sgn}(x) = l
> $$
> 
> Poiché $|\text{sgn}(x)| \le l$, possiamo supporre che $l \in \mathbb{R}$, cioè $l \ne \pm \infty$.
> 
> Per la [definizione di _limite finito al finito_](Limiti.md#^definizione-limite-finito-al-finito), abbiamo che
> 
> $$
> \forall \varepsilon > 0, \exists \delta > 0, \forall x \in \mathbb{R} . \big( 0 < |x| < \delta \implies |\text{sgn}(x) - l| < \varepsilon \big)
> $$
> 
> Abbiamo allora tre casi possibili:
> - Se $l>0$, allora preso un $\displaystyle\varepsilon = \dfrac{l}{2}$ esiste un $\delta > 0$ tale che, per ogni $x \in \mathbb{R}$ con $0 < |x| < \delta$, si ha che
> 	$$
> 	\begin{array}{}
> 	|\text{sgn}(x)-l| < \dfrac{l}{2} \\
> 	\Updownarrow \\
> 	-\dfrac{l}{2} < \text{sgn}(x) - l < \dfrac{l}{2} \\
> 	\Updownarrow \\
> 	\dfrac{l}{2} < \text{sgn}(x) < \dfrac{3}{2}l\\
> 	\end{array}
> 	$$
> 	e in particolare, per ogni $x \in \mathbb{R}$ tale che $0 < |x| < \delta$, si ha che $\text{sgn}(x) > \dfrac{l}{2} > 0$: otteniamo però un assurdo perché, se $x < 0$, allora $\text{sgn}(x)= -1 < 0$.
> - Se $l < 0$, allora preso un $\displaystyle\varepsilon = - \dfrac{l}{2}$ esiste un $\delta > 0$ tale che, per ogni $x \in \mathbb{R}$ con $0 < |x| < \delta$, si ha che
> 	$$
> 	\begin{array}{}
> 	|\text{sgn}(x)-l| < -\dfrac{l}{2} \\
> 	\Updownarrow \\
> 	\dfrac{l}{2} < \text{sgn}(x) - l < -\dfrac{l}{2} \\
> 	\Updownarrow \\
> 	\dfrac{3}{2}l < \text{sgn}(x) < \dfrac{l}{2} \\
> 	\end{array}
> 	$$
> 	e in particolare, per ogni $x \in \mathbb{R}$ tale che $0 < |x| < \delta$, si ha che $\text{sgn}(x) < \dfrac{l}{2} < 0$: otteniamo però un assurdo perché, se $x > 0$, allora $\text{sgn}(x)= 1 > 0$.
> - Se $l = 0$, allora preso un $\displaystyle\varepsilon = \dfrac{l}{2}$ esiste un $\delta > 0$ tale che, per ogni $x \in \mathbb{R}$ con $0 < |x| < \delta$, si ha che $|\text{sgn}(x)| < \dfrac{l}{2}$: otteniamo però un assurdo perché, se $x > 0$, allora $|\text{sgn}(x)| =1 >\dfrac{l}{2}$.
> 
> $\blacksquare$

> [!osservazione]+ Osservazione: utilità della definizione del limite
> 
> La [definizione di _limite_](Limiti.md#^definizione-limite) non è utile ai fini del calcolo del limite, ma solo per verificare il valore del limite o per confutarne l'esistenza. 

> [!esercizio]+ Esercizio
> 
> Provare che non esiste il [limite](Limiti.md#^definizione-limite)
> 
> $$
> \lim_{x \to 0} \dfrac{1}{x}
> $$

%% 
mettere soluzione
%%

# 3 - Unicità del limite

> [!teorema]+ Teorema di unicità del limite
> 
> Data una [funzione](Funzioni.md#^definizione-funzione) $f \colon \text{dom}(f) \to \mathbb{R}$, un [punto di accumulazione](Topologia%20dei%20reali.md#^definizione-punto-di-accumulazione) $x_0 \in \mathbb{R} \cup \{ \pm \infty \}$ per $\text{dom}(f)$ e due valori%% link %% $l_1,l_2 \in \mathbb{R} \cup \{ \pm\infty \}$ per i quali esiste il [limite](Limiti.md#^definizione-limite) $\displaystyle\lim_{x \to x_0}f(x)$, allora
> 
> $$
> l_1 = l_2
> $$
^teorema-di-unicita-del-limite

%%
[!dimostrazione]- Dimostrazione

Per assurdo supponiamo che esistano due valori distintiLINK $l_1 \ne l_2$.

Pagina 135 e 136del Lancelotti
%%

# 4 - Limiti laterali

%% 
Ora definiamo due particolari [limiti](Limiti.md#^definizione-limite), detti _limiti laterali_ perché ???, in particolare limite destro e limite sinistro.
%%

%%
Modificare le definizioni di limite destro e sinistro

limite destro:
$$
\forall \varepsilon > 0, \exists \delta > 0, \forall x \in \mathbb{R} . \big( x \in I_\delta^+(c) \setminus \{ c \} \implies f(x) \in I_\varepsilon^+(l) \big) 
$$
o definizione alternativa:
$$
\forall \varepsilon > 0, \exists \delta > 0, \forall x \in \mathbb{R} . \big( 0 < x - c < \delta \implies |f(x) - l| < \varepsilon \big)
$$

limite sinistro:
$$
\forall \varepsilon > 0, \exists \delta > 0, \forall x \in \mathbb{R} . \big( x \in I_\delta^-(c) \setminus \{ c \} \implies f(x) \in I_\varepsilon^-(l) \big) 
$$
o definizione alternativa:
$$
\forall \varepsilon > 0, \exists \delta > 0, \forall x \in \mathbb{R} . \big( - \delta < x - c < 0 \implies |f(x) - l| < \varepsilon \big)
$$
%%

> [!definizione]+ Definizione: limite destro
> 
> Data una [funzione](Funzioni.md#^definizione-funzione) $f \colon \text{dom}(f) \to \mathbb{R}$ e un [punto di accumulazione](Topologia%20dei%20reali.md#^definizione-punto-di-accumulazione) $x_0 \in \mathbb{R}$ per $\text{dom}(f) \cap (x_0, + \infty)$ e un valore%% link %% $l \in \mathbb{R} \cup \{ \pm \infty \}$, diciamo che **$f$ ha limite destro $l$ per $x$ che tende a $x_0$** (o che **$f$ tende a $l$ per $x$ che tende a $x_0$ da destra**) se, per ogni [intorno](Topologia%20dei%20reali.md#^definizione-intorno-di-un-punto) $I(l)$ di $l$, esiste un [intorno destro](Topologia%20dei%20reali.md#^definizione-intorno-di-un-punto) $I^+(x_0)$ di $x_0$ tale che, per ogni $x \in \text{dom}(f)$ con $x \in I^+(x_0)$, si ha che $f(x) \in I(l)$:
> 
> $$
> \forall I(l) \text{ intorno di } l, \exists I^+(x_0) \text{ intorno destro di } x_0 .\big( x \in \text{dom}(f) \cap I^+(x_0) \implies f(x) \in I(l) \big) 
> $$
> 
> In tal caso scriviamo
> 
> $$
> \lim_{x \to x^+_0} f(x) = l
> $$
> 
> che si legge "_limite per $x$ che tende a $x_0^+$ di $f(x)$ uguale $l$_" o "_$f(x)$ tende a $l$ per $x$ che tende a $x_0$ da destra_".
^definizione-limite-destro

> [!definizione]+ Definizione: limite sinistro
> 
> Data una [funzione](Funzioni.md#^definizione-funzione) $f \colon \text{dom}(f) \to \mathbb{R}$ e un [punto di accumulazione](Topologia%20dei%20reali.md#^definizione-punto-di-accumulazione) $x_0 \in \mathbb{R}$ per $\text{dom}(f) \cap (- \infty, x_0)$ e un valore%% link %% $l \in \mathbb{R} \cup \{ \pm \infty \}$, diciamo che **$f$ ha limite sinistro $l$ per $x$ che tende a $x_0$** (o che **$f$ tende a $l$ per $x$ che tende a $x_0$ da sinistra**) se, per ogni [intorno](Topologia%20dei%20reali.md#^definizione-intorno-di-un-punto) $I(l)$ di $l$, esiste un [intorno sinistro](Topologia%20dei%20reali.md#^definizione-intorno-di-un-punto) $I^-(x_0)$ di $x_0$ tale che, per ogni $x \in \text{dom}(f)$ con $x \in I^-(x_0)$, si ha che $f(x) \in I(l)$:
> 
> $$
> \forall I(l) \text{ intorno di } l, \exists I^-(x_0) \text{ intorno sinistro di } x_0 .\big( x \in \text{dom}(f) \cap I^-(x_0) \implies f(x) \in I(l) \big) 
> $$
> 
> In tal caso scriviamo
> 
> $$
> \lim_{x \to x^-_0} f(x) = l
> $$
> 
> che si legge "_limite per $x$ che tende a $x_0^-$ di $f(x)$ uguale $l$_" o "_$f(x)$ tende a $l$ per $x$ che tende a $x_0$ da sinistra_".
^definizione-limite-sinistro

> [!definizione]+ Definizione: limiti laterali
> 
> Il [limite destro](Limiti.md#^definizione-limite-destro) e [limite sinistro](Limiti.md#^definizione-limite-sinistro) sono detti **limiti laterali**.
^definizione-limiti-laterali

%% 
I limiti laterali non si definiscono per $+\infty$ e $- \infty$.
%%

> [!osservazione]+ Osservazione: casi specifici dei limiti laterali
> 
> Queste definizioni, esattamente per come avviene per i [limiti](Limiti.md#^definizione-limite), possono essere scritte in modo più specifico a seconda che $l \in \mathbb{R}$ o $l = \pm \infty$.
> 
> Per esempio, con un [limite destro](Limiti.md#^definizione-limite) di $f(x)$ con $l \in \mathbb{R}$, si ha che
> 
> $$
> \begin{array}{}
> \displaystyle\lim_{x \to x_0^+} f(x) = l \\
> \Updownarrow \\
> \forall \varepsilon > 0, \exists \delta > 0, \forall x \in \text{dom}(f) . \big( x_0 < x < x_0 + \delta \implies |f(x) - l| < \varepsilon \big) 
> \end{array}
> $$
> 
> Invece, con un [limite sinistro](Limiti.md#^definizione-limite-sinistro) di $f(x)$ con $l = - \infty$, si ha che
> 
> $$
> \begin{array}{}
> \displaystyle\lim_{x \to x_0^-} f(x) = -\infty \\
> \Updownarrow \\
> \forall a \in \mathbb{R}, \exists \delta > 0, \forall x \in \text{dom}(f) . \big( x_0 - \delta < x < x_0 \implies f(x) < a \big) 
> \end{array}
> $$

%% 
esercizio: scrivere definizioni degli altri casi
%%

> [!proposizione]+ Proposizione: limiti laterali coincidenti
> 
> Data una [funzione](Funzioni.md#^definizione-funzione) $f \colon \text{dom}(f) \to \mathbb{R}$ e un [punto di accumulazione](Topologia%20dei%20reali.md#^definizione-punto-di-accumulazione) $x_0 \in \mathbb{R}$ sia per $\text{dom}(f) \cap (x_0, + \infty)$ che per $\text{dom}(f) \cap (- \infty, x_0)$ e un valore%% link %% $l \in \mathbb{R} \cup \{ \pm \infty \}$, allora
> 
> $$
> \lim_{x \to x_0} f(x) = l \iff \lim_{x \to x_0^+} f(x) = \lim_{x \to x_0^-} f(x) = l
> $$
^propoisizione-limiti-laterali-coincidenti

%% 
Dimostrazione: segue immediatamente dalle definizioni (per esercizio)
%%

%% 
Corollario:
il limite non esiste se il limite destro =/= limite sinistro o se almeno uno dei due non esiste.
%%

> [!corollario]+ Corollario del teorema di unicità del limite per i limiti laterali
> 
> Il [teorema di unicità del limite](Limiti.md#^teorema-di-unicita-del-limite) vale anche per il [limite destro](Limiti.md#^definizione-limite-destro) e il [limite sinistro](Limiti.md#^definizione-limite-sinistro).

%% 
esempio 2.28 pagg. 146-147 Lancelotti
%%

> [!osservazione]+ Osservazione: equivalenza tra limiti e limiti laterali
> 
> Se una [funzione](Funzioni.md#^definizione-funzione) $f$ è definita solo per $x > x_0$, allora
> 
> $$
> \lim_{x \to x_0^+} f(x) = \lim_{x \to x_0} f(x)
> $$
> 
> Analogamente, se una [funzione](Funzioni.md#^definizione-funzione) $f$ è definita solo per $x < x_0$, allora
> 
> $$
> \lim_{x \to x_0^-} f(x) = \lim_{x \to x_0} f(x)
> $$

%% spiegare perché vale questa osservazione (ed eventualmente trasformarla in proposizione) %%

# 5 - Limiti per eccesso e per difetto

> [!definizione]+ Definizione: limite per eccesso
>
> Data una [funzione](Funzioni.md#^definizione-funzione) $f \colon I_r(c) \setminus \{ c \} \to \mathbb{R}$ per qualche $r > 0$ e $c \in \mathbb{R}$, si dice che **$f$ ammette limite finito $l$ per eccesso per $x$ che tende a $c$** e si scrive
>
> $$
> \lim_{x \to c} f(x) = l^+
> $$
>
> se
>
> $$
> \forall \varepsilon > 0, \exists \delta > 0, \forall x \in \mathbb{R} . \left( x \in I_\delta(c) \setminus \{ c \} \implies f(x) \in I_\varepsilon^+(l) \right)
> $$
^definizione-limite-per-eccesso

> [!definizione]+ Definizione: limite per difetto
>
> Data una [funzione](Funzioni.md#^definizione-funzione) $f \colon I_r(c) \setminus \{ c \} \to \mathbb{R}$ per qualche $r > 0$ e $c \in \mathbb{R}$, si dice che **$f$ ammette limite finito $l$ per difetto per $x$ che tende a $c$** e si scrive
>
> $$
> \lim_{x \to c} f(x) = l^-
> $$
>
> se
>
> $$
> \forall \varepsilon > 0, \exists \delta > 0, \forall x \in \mathbb{R} . \left( x \in I_\delta(c) \setminus \{ c \} \implies f(x) \in I_\varepsilon^-(l) \right)
> $$
^definizione-limite-per-difetto

%%
Interpretazione del limite per eccesso e per difetto

In altre parole, il limite per eccesso richiede che $f(x)$ si avvicini a $l$ **restando sempre strettamente maggiore** di $l$, mentre il limite per difetto richiede che $f(x)$ si avvicini a $l$ **restando sempre strettamente minore** di $l$.
%%

%% 
osservazione: limite per eccesso e per difetto sono casi specifici dei limiti laterali (?)
%%

> [!esempio]- Esempio di limite per eccesso
> 
> Un esempio di [limite per eccesso](Limiti.md#^definizione-limite-per-eccesso) è il [limite](Limiti.md#^definizione-limite)
> 
> $$
> \lim_{x \to + \infty} \dfrac{1}{x^2} = 0^+
> $$
> 
> perché, $x^2 > 0$ per ogni $x \ne 0$, si ha sempre $f(x) = \dfrac{1}{x^2} > 0$, dunque $f(x)$ si avvicina a $0$ restando sempre al di sopra di $0$.

> [!esempio]- Esempio di limite per difetto
> 
> Un esempio di [limite per difetto](Limiti.md#^definizione-limite-per-difetto) è il [limite](Limiti.md#^definizione-limite)
> 
> $$
> \lim_{x \to 0} (1 - x^2) = 1^-
> $$
> 
> perché, essendo $x^2 > 0$ per ogni $x \ne 0$, si ha sempre $f(x) = 1 - x^2 < 1$, dunque $f(x)$ si avvicina a $1$ restando sempre al di sotto di $1$.

%% 
Esempio:

$$
\lim_{x \to + \infty} (\sin x)
$$
a cosa corrisponde?

Sappiamo che il $\sin x$ oscilla sempre tra $-1$ e $1$, quindi non ha segno costante quando $x \to + \infty$.

Ma il suo limite a cosa equivale? Non equivale sicuramente a $0$ perché anche all'infinito continua a oscillare sempre tra $-1$ e $1$, quindi non tende mai a un valore specifico come lo $0$.

Possiamo però provare a "smorzare" le oscillazioni man mano che la funzione tende a $+ \infty$, per esempio dividendo $\sin x$ per $x$. Avendo $x$ valori sempre maggiori man mano che tende verso $+ \infty$, "smorzerà" sempre di più le oscillazioni fino ad annullarle: ecco perché $\lim_{x \to 0} \dfrac{\sin x}{x} = 0$.

Verifichiamo usando la definizione di limite:

$$
\forall \varepsilon > 0, \exists M > 0, \forall x \in \mathbb{R} . \left( x > 0 \implies \left| \dfrac{\sin x}{x} \right| < \varepsilon \right)
$$

ma

$$
\left| \dfrac{\sin x}{x} \right| \underbrace{=}_{\text{perché } x>0} \dfrac{|\sin x|}{x} \le \dfrac{1}{x} < \varepsilon \iff x > \dfrac{1}{\varepsilon}
$$

Conclusione:

$$
\forall \varepsilon > 0 . \left( x > \underbrace{\dfrac{1}{\varepsilon}}_{=M} \implies \left| \dfrac{\sin x}{x} \right| < \varepsilon \right) 
$$
%%

# 6 - Algebra dei limiti

> [!teorema]+ Teorema della somma di limiti finiti
> 
> Dato un [sottoinsieme](Teoria%20degli%20insiemi.md#^definizione-insieme) $A \subseteq \mathbb{R}$ non [vuoto](Teoria%20degli%20insiemi.md#^definizione-insieme-vuoto), due [funzioni](Funzioni.md#^definizione-funzione) $f \colon A \to \mathbb{R}$ e $g \colon A \to \mathbb{R}$ e un [punto di accumulazione](Topologia%20dei%20reali.md#^definizione-punto-di-accumulazione) $x_0 \in \mathbb{R} \cup \{ \pm \infty \}$ per $A$, se esistono i [limiti](Limiti.md#^definizione-limite) $\displaystyle\lim_{x \to x_0} f(x) = l \in \mathbb{R}$ e $\displaystyle\lim_{x \to x_0} g(x) = m \in \mathbb{R}$, allora il [limite](Limiti.md#^definizione-limite) della loro [somma](Funzioni.md#^definizione-somma-di-funzioni) $f + g$ è uguale alla somma%% Link %% dei loro [limiti](Limiti.md#^definizione-limite):
> 
> $$
> \lim_{x \to x_0} \big( f(x) + g(x) \big) = \lim_{x \to x_0} f(x) + \lim_{x \to x_0} g(x) = l + m
> $$
^teorema-della-somma-di-limiti-finiti

<!--

[!dimostrazione]- Dimostrazione del teorema della somma di limiti finiti

Dimostriamo che vale il [teorema della somma di limiti finiti](Limiti.md#^teorema-della-somma-di-limiti-finiti). Consideriamo per il momento il caso in cui $x_0 \in \mathbb{R}$ e, usando la [definizione alternativa di _limite finito al finito_](Limiti.md#^osservazione-definizione-alternativa-di-limite-finito-al-finito), abbiamo che la tesi si può riscrivere in questa forma:

$$
\begin{array}{}
\forall \varepsilon > 0, \exists \delta > 0, \forall x \in \mathbb{R} . \left( 0 < |x - c| < \delta \implies |\big( f(x) + g(x) \big)  - (l + m)| < \varepsilon \right) \\
\Updownarrow \\
\forall \varepsilon > 0, \exists \delta > 0, \forall x \in \mathbb{R} . \left( 0 < |x - c| < \delta \implies | f(x) + g(x) - l - m| < \varepsilon \right) \\
\end{array}
$$

Per la disuguaglianza triangolare%% link %%, abbiamo in particolare che

$$
|f(x) + g(x) - l - m| \le |f(x) - l| + |g(x) - m|
$$

Per ipotesi, i due [limiti](Limiti.md#^definizione-limite) di $f(x)$ e $g(x)$ esistono rispettivamente un $\delta_f > 0$ e un $\delta_g > 0$ tali che

$$
\begin{array}{}
x \in (I_{\delta_f}(x_0) \cap I_{\delta_g} (x_0)) \setminus \{ x_0 \} \\
\Downarrow \\
|f(x) - l| < \dfrac{\varepsilon}{2} \quad \land \quad |g(x) - m| < \dfrac{\varepsilon}{2}
\end{array}
$$

%% perché $\dfrac{\varepsilon}{2}$? %%

Quindi, per dimostrare il [limite](Limiti.md#^definizione-limite) iniziale, scegliamo come $\delta$ quello minore tra $\delta_f$ e $\delta_g$.

%% fare anche caso del limite finito all'infinito %%

-->

%% 
dimostrazioni analoghe a quelle dell'algebra delle funzioni continue
%%

> [!teorema]+ Teorema del prodotto di limiti finiti
> 
> Dato un [sottoinsieme](Teoria%20degli%20insiemi.md#^definizione-insieme) $A \subseteq \mathbb{R}$ non [vuoto](Teoria%20degli%20insiemi.md#^definizione-insieme-vuoto), due [funzioni](Funzioni.md#^definizione-funzione) $f \colon A \to \mathbb{R}$ e $g \colon A \to \mathbb{R}$ e un [punto di accumulazione](Topologia%20dei%20reali.md#^definizione-punto-di-accumulazione) $x_0 \in \mathbb{R} \cup \{ \pm \infty \}$ per $A$, se esistono i [limiti](Limiti.md#^definizione-limite) $\displaystyle\lim_{x \to x_0} f(x) = l \in \mathbb{R}$ e $\displaystyle\lim_{x \to x_0} g(x) = m \in \mathbb{R}$, allora il [limite](Limiti.md#^definizione-limite) del loro [prodotto](Funzioni.md#^definizione-prodotto-di-funzioni) è uguale al prodotto%% Link %% dei loro [limiti](Limiti.md#^definizione-limite):
> 
> $$
> \lim_{x \to x_0} \big( f(x) \cdot g(x) \big) = \lim_{x \to x_0} f(x) \cdot \lim_{x \to x_0} g(x) = l \cdot m
> $$

%% 
dimostrazioni analoghe a quelle dell'algebra delle funzioni continue
%%

> [!teorema]+ Teorema del quoziente di limiti finiti
> 
> Dato un [sottoinsieme](Teoria%20degli%20insiemi.md#^definizione-insieme) $A \subseteq \mathbb{R}$ non [vuoto](Teoria%20degli%20insiemi.md#^definizione-insieme-vuoto), due [funzioni](Funzioni.md#^definizione-funzione) $f \colon A \to \mathbb{R}$ e $g \colon A \to \mathbb{R}$ e un [punto di accumulazione](Topologia%20dei%20reali.md#^definizione-punto-di-accumulazione) $x_0 \in \mathbb{R} \cup \{ \pm \infty \}$ per $A$, se esistono i [limiti](Limiti.md#^definizione-limite) $\displaystyle\lim_{x \to x_0} f(x) = l \in \mathbb{R}$ e $\displaystyle\lim_{x \to x_0} g(x) = m \in \mathbb{R}$ con $m \ne 0$, allora il [limite](Limiti.md#^definizione-limite) del loro quoziente%% link al quoziente di funzioni %% è uguale al quoziente%% Link %% dei loro [limiti](Limiti.md#^definizione-limite):
> 
> $$
> \lim_{x \to x_0} \dfrac{f(x)}{g(x)} = \dfrac{\displaystyle\lim_{x \to x_0} f(x)}{\displaystyle\lim_{x \to x_0} g(x)} = \dfrac{l}{m}
> $$

%% 
dimostrazioni analoghe a quelle dell'algebra delle funzioni continue
%%

> [!teorema]+ Teorema del reciproco di un limite
> 
> Data una [funzione](Funzioni.md#^definizione-funzione) $f \colon \text{dom}(f) \to \mathbb{R}$ e un [punto di accumulazione](Topologia%20dei%20reali.md#^definizione-punto-di-accumulazione) $x_0 \in \mathbb{R} \cup \{ \pm \infty \}$, se esiste il [limite](Limiti.md#^definizione-limite) $\displaystyle\lim_{x \to x_0} f(x) = l \in \mathbb{R} \cup \{ \pm \infty \}$ ed è diverso da $0$, allora il [limite](Limiti.md#^definizione-limite) del suo reciproco%% link %% $\dfrac{1}{f(x)}$ è uguale al reciproco%% link %% del [limite](Limiti.md#^definizione-limite):
> 
> $$
> \lim_{x \to x_0} \dfrac{1}{f(x)} = \dfrac{1}{\displaystyle\lim_{x \to x_0} f(x)} = \dfrac{1}{l}
> $$

%% 
dimostrazione: caso specifico del teorema del limite del quoziente con f(x)=1 e g(x)=f(x)
%%

%% 
pagg. 161-164 lancelotti
%%

## 6.1 - Algebra dei limiti infiniti

Ora vediamo alcune operazioni in cui almeno uno dei due [limiti](Limiti.md#^definizione-limite) è infinito (cioè è o un [limite infinito all'infinito](Limiti.md#^definizione-limite-infinito-all-infinito) o un [limite infinito al finito](Limiti.md#^definizione-limite-infinito-al-finito)).

> [!teorema]+ Teorema della somma di limite finito con limite infinito
>
> Dato un [sottoinsieme](Teoria%20degli%20insiemi.md#^definizione-insieme) $A \subseteq \mathbb{R}$ non [vuoto](Teoria%20degli%20insiemi.md#^definizione-insieme-vuoto), due [funzioni](Funzioni.md#^definizione-funzione) $f, g \colon A \to \mathbb{R}$ e un [punto di accumulazione](Topologia%20dei%20reali.md#^definizione-punto-di-accumulazione) $x_0 \in \mathbb{R} \cup \{ \pm\infty \}$ per $A$, se
>
> $$
> \lim_{x \to x_0} f(x) = l \in \mathbb{R} \quad \land \quad \lim_{x \to x_0} g(x) = \pm\infty
> $$
>
> allora
>
> $$
> \lim_{x \to x_0} \big( f(x) + g(x) \big) = \pm\infty
> $$

> [!teorema]+ Teorema della somma di limiti infiniti concordi
>
> Dato un [sottoinsieme](Teoria%20degli%20insiemi.md#^definizione-insieme) $A \subseteq \mathbb{R}$ non [vuoto](Teoria%20degli%20insiemi.md#^definizione-insieme-vuoto), due [funzioni](Funzioni.md#^definizione-funzione) $f, g \colon A \to \mathbb{R}$ e un [punto di accumulazione](Topologia%20dei%20reali.md#^definizione-punto-di-accumulazione) $x_0 \in \mathbb{R} \cup \{ \pm\infty \}$ per $A$, se
>
> $$
> \lim_{x \to x_0} f(x) = \lim_{x \to x_0} g(x) = \pm\infty
> $$
>
> allora
>
> $$
> \lim_{x \to x_0} \big( f(x) + g(x) \big) = \pm\infty
> $$

> [!teorema]+ Teorema del prodotto di limiti infiniti concordi
>
> Dato un [sottoinsieme](Teoria%20degli%20insiemi.md#^definizione-insieme) $A \subseteq \mathbb{R}$ non [vuoto](Teoria%20degli%20insiemi.md#^definizione-insieme-vuoto), due [funzioni](Funzioni.md#^definizione-funzione) $f, g \colon A \to \mathbb{R}$ e un [punto di accumulazione](Topologia%20dei%20reali.md#^definizione-punto-di-accumulazione) $x_0 \in \mathbb{R} \cup \{ \pm\infty \}$ per $A$, se
>
> $$
> \lim_{x \to x_0} f(x) = \lim_{x \to x_0} g(x) = \pm\infty
> $$
>
> allora
>
> $$
> \lim_{x \to x_0} \big( f(x) \cdot g(x) \big) = +\infty
> $$

%% 
Attenzione: $(- \infty) \cdot (- \infty) = + \infty$
%%

> [!teorema]+ Teorema del quoziente di limite finito con limite infinito
>
> Dato un [sottoinsieme](Teoria%20degli%20insiemi.md#^definizione-insieme) $A \subseteq \mathbb{R}$ non [vuoto](Teoria%20degli%20insiemi.md#^definizione-insieme-vuoto), due [funzioni](Funzioni.md#^definizione-funzione) $f, g \colon A \to \mathbb{R}$ e un [punto di accumulazione](Topologia%20dei%20reali.md#^definizione-punto-di-accumulazione) $x_0 \in \mathbb{R} \cup \{ \pm\infty \}$ per $A$, se
>
> $$
> \lim_{x \to x_0} f(x) = l \in \mathbb{R} \setminus \{ 0 \} \quad \land \quad \lim_{x \to x_0} g(x) = \pm\infty
> $$
>
> allora
>
> $$
> \lim_{x \to x_0} \dfrac{f(x)}{g(x)} = 0
> $$

%% 
Corollario:
- $0^+$ quando limite di $g(x) = + \infty$
- $0^-$ quando limite di $g(x) = - \infty$
%%

> [!teorema]+ Teorema del quoziente di limite finito con limite nullo
>
> Dato un [sottoinsieme](Teoria%20degli%20insiemi.md#^definizione-insieme) $A \subseteq \mathbb{R}$ non [vuoto](Teoria%20degli%20insiemi.md#^definizione-insieme-vuoto), due [funzioni](Funzioni.md#^definizione-funzione) $f, g \colon A \to \mathbb{R}$ e un [punto di accumulazione](Topologia%20dei%20reali.md#^definizione-punto-di-accumulazione) $x_0 \in \mathbb{R} \cup \{ \pm\infty \}$ per $A$, se
>
> $$
> \lim_{x \to x_0} f(x) = l \in \mathbb{R} \setminus \{ 0 \} \quad \land \quad \lim_{x \to x_0} g(x) = 0^+
> $$
>
> allora
>
> $$
> \lim_{x \to x_0} \dfrac{f(x)}{g(x)} = +\infty
> $$

%% 
e se lim g(x) = 0^- allora limite del quoziente è $- \infty$?
%%

%% 
Gli altri casi di operazioni tra limiti infiniti non li vediamo perché, come osserveremo più avanti, sono forme indeterminate.
%%

# 7 - Teoremi del confronto

%% 
spiegare cosa sono i teoremi del confronto
%%

> [!teorema]+ Teorema dei due carabinieri
> 
> Date tre [funzioni](Funzioni.md#^definizione-funzione) $f,g,h \colon A \subseteq \mathbb{R} \to \mathbb{R}$ (con $A \ne \emptyset$) e un [punto di accumulazione](Topologia%20dei%20reali.md#^definizione-punto-di-accumulazione) $x_0 \in \mathbb{R} \cup \{ \pm \infty \}$ per $A$, se esistono i [limiti](Limiti.md#^definizione-limite)
> 
> $$
> \lim_{x \to x_0} f(x) = \lim_{x \to x_0} h(x) = l \in \mathbb{R}
> $$
> 
> ed esiste un [intorno](Topologia%20dei%20reali.md#^definizione-intorno-di-un-punto) $I(x_0)$ di $x_0$ tale che
> 
> $$
> \forall x \in (A \cap I(x_0)) \setminus \{ x_0 \} . \big (f(x) \le g(x) \le h(x))
> $$
> 
> allora
> 
> $$
> \lim_{x \to x_0} g(x) = l
> $$
^teorema-dei-due-carabinieri

%% 
spiegazione (con grafico) del teorema dei due carabinieri
e spiegare perché si chiama "teorema dei due carabinieri"
%%

> [!dimostrazione]- Dimostrazione del teorema dei due carabinieri
> 
> Dimostriamo il [teorema dei due carabinieri](Limiti.md#^teorema-dei-due-carabinieri). Vogliamo dimostrare che
> 
> $$
> \lim_{x \to x_0} g(x) = l
> $$
> 
> ossia che, per [definizione di _limite_](Limiti.md#^definizione-limite),
> 
> $$
> \forall I_\varepsilon(l), \exists I_\delta(x_0), \forall x \in \mathbb{R} . \big( x \in I_\delta(x_0) \setminus \{ x_0 \} \implies g(x) \in I_\varepsilon(l) \big) 
> $$
> 
> Per ipotesi sappiamo che
> 
> $$
> \lim_{x \to x_0} f(x) = \lim_{x \to x_0} h(x) = l \in \mathbb{R}
> $$
> 
> ossia che, per [definizione di _limite_](Limiti.md#^definizione-limite),
> 
> $$
> \forall I_\varepsilon(l), \begin{cases}
> \exists \hat I_{\hat\delta}(x_0), \forall x \in \mathbb{R} . (x \in \hat I_{\hat\delta}(x_0) \implies f(x) \in I_\varepsilon(l)) \\
> \exists \dot I_{\dot\delta}(x_0), \forall x \in \mathbb{R} . (x \in \dot I_{\dot\delta}(x_0) \implies h(x) \in I_\varepsilon(l)) \\
> \end{cases}
> $$
> 
> Scegliamo come [intorno](Topologia%20dei%20reali.md#^definizione-intorno-di-un-punto) $I_\delta(x_0)$ proprio l'[intersezione](Teoria%20degli%20insiemi.md#^definizione-intersezione-di-due-insiemi) tra $\hat I_{\hat\delta}(x_0)$ e $\dot I_{\dot\delta}(x_0)$:
> 
> $$
> I_\delta(x_0) = \hat I_{\hat\delta}(x_0) \cap \dot I_{\dot\delta}(x_0)
> $$
> 
> e osserviamo che, dato che ogni $x \in I_\delta(x_0)$ sarà automaticamente contenuta sia in $\hat I_{\hat\delta}(x_0)$ che in $\dot I_{\dot\delta}(x_0)$,
> 
> $$
> \forall I_\varepsilon(l), \exists I_\delta(x_0), \forall x \in \mathbb{R} . \left( x \in I_\delta(x_0) \setminus \{ x_0 \} \implies \begin{array}{}
> f(x) \in I_\varepsilon(l) \\
> \land \\
> h(x) \in I_\varepsilon(l)
> \end{array} \right)
> $$
> 
> che, per [definizione di _intorno_](Topologia%20dei%20reali.md#^definizione-intorno-di-un-punto), diventa
> 
> $$
> \forall I_\varepsilon(l), \exists I_\delta(x_0), \forall x \in \mathbb{R} . \left( x \in I_\delta(x_0) \setminus \{ x_0 \} \implies \begin{array}{}
> | f(x) - l | < \varepsilon \\
> \land \\
> | h(x) - l | < \varepsilon
> \end{array} \right) 
> $$
> 
> Sviluppiamo le disuguaglianze%% link %% con i valori assoluti%% link %%:
> 
> $$
> \forall I_\varepsilon(l), \exists I_\delta(x_0), \forall x \in \mathbb{R} . \left( x \in I_\delta(x_0) \setminus \{ x_0 \} \implies \begin{array}{}
> l - \varepsilon\ {\color{#FF7F7F} < }\ f(x) < l + \varepsilon \\
> \land \\
> l - \varepsilon < h(x)\ {\color{#7FFF7F} < }\ l + \varepsilon
> \end{array} \right) 
> $$
> 
> Dato che, per ipotesi, abbiamo che $f(x) \le g(x) \le h(x)$, allora
> 
> $$
> \forall I_\varepsilon(l), \exists I_\delta(x_0), \forall x \in \mathbb{R} . \left( x \in I_\delta(x_0) \setminus \{ x_0 \} \implies
> l - \varepsilon\ {\color{#FF7F7F} < }\ f(x) \le g(x) \le h(x)\ {\color{#7FFF7F} < }\ l + \varepsilon
> \right) 
> $$
> 
> Per cui possiamo concludere che
> 
> $$
> \forall I_\varepsilon(l), \exists I_\delta(x_0), \forall x \in \mathbb{R} . \left( x \in I_\delta(x_0) \setminus \{ x_0 \} \implies
> l - \varepsilon\ {\color{#FF7F7F} < }\ g(x) \ {\color{#7FFF7F} < }\ l + \varepsilon
> \right) 
> $$
> 
> E da qui risalire alla [definizione di _limite_](Limiti.md#^definizione-limite):
> 
> 
> $$
> \begin{array}{}
> \forall I_\varepsilon(l), \exists I_\delta(x_0), \forall x \in \mathbb{R} . \left( x \in I_\delta(x_0) \setminus \{ x_0 \} \implies
> | g(x) - l | < \varepsilon
> \right) \\
> \Updownarrow \\
> \forall I_\varepsilon(l), \exists I_\delta(x_0), \forall x \in \mathbb{R} . \left( x \in I_\delta(x_0) \setminus \{ x_0 \} \implies
> g(x) \in I_\varepsilon(l)
> \right) \\
> \Updownarrow \\
> \displaystyle\lim_{x \to x_0} g(x) = l
> \end{array}
> $$
> 
> $\blacksquare$

%% 
dimostrazione pag. 171 lancelotti
%%

%% 
Osservazioni 3.28 e 3.29 pag. 172 lancelotti
%%

> [!teorema]+ Teorema del confronto per limiti infiniti
> 
> Date due [funzioni](Funzioni.md#^definizione-funzione) $f,g \colon A \subseteq \mathbb{R} \to \mathbb{R}$ (con $A \ne \emptyset$) e un [punto di accumulazione](Topologia%20dei%20reali.md#^definizione-punto-di-accumulazione) $x_0 \in \mathbb{R} \cup \{ \pm \infty \}$ per $A$, se esiste un [intorno](Topologia%20dei%20reali.md#^definizione-intorno-di-un-punto) $I(x_0)$ di $x_0$ tale che, per ogni $x \in (A \cap I(x_0)) \setminus \{ x_0 \}$, si abbia $f(x) \le g(x)$, allora
> 
> $$
> \begin{array}{}
> \displaystyle\lim_{x \to x_0} f(x) = + \infty \implies \lim_{x \to x_0} g(x) = + \infty \\
> \displaystyle\lim_{x \to x_0} g(x) = - \infty \implies \lim_{x \to x_0} f(x) = - \infty
> \end{array}
> $$
^teorema-del-confronto-per-limiti-infiniti

%% 
spiegazione (con grafico) del teorema del confronto per limiti infiniti
%%

> [!dimostrazione]- Dimostrazione del teorema del confronto per limiti infiniti
> 
> Dimostriamo il [teorema del confronto per limiti infiniti](Limiti.md#^teorema-del-confronto-per-limiti-infiniti).
> 
> Dimostriamo prima il primo caso:
> 
> $$
> \displaystyle\lim_{x \to x_0} f(x) = + \infty \implies \lim_{x \to x_0} g(x) = + \infty
> $$
> 
> Per [definizione di _limite infinito al finito_](Limiti.md#^definizione-limite-infinito-al-finito),
> 
> $$
> \begin{array}{}
> \displaystyle\lim_{x \to x_0} f(x) = + \infty \\
> \Updownarrow \\
> \forall M > 0, \exists \delta > 0, \forall x \in \mathbb{R} .\ \left( x \in I_\delta(x_0) \setminus \{x_0\} \implies f(x) > M \right)
> \end{array}
> $$
> 
> Dato che per ipotesi abbiamo $f(x) \le g(x)$, allora anche $g(x)$ sarà sicuramente più grande di $M$:
> 
> $$
> \begin{cases}
> f(x) > M \\
> f(x) \le g(x)
> \end{cases}
> \implies
> \begin{cases}
> f(x) > M \\
> g(x) > f(x)
> \end{cases}
> \implies
> g(x) > f(x) > M
> \implies
> g(x) > M
> $$
> 
> Ciò quindi conferma che il [limite](Limiti.md#^definizione-limite) $\displaystyle\lim_{x \to x_0} g(x) = + \infty$ vale:
> 
> $$
> \begin{array}{}
> \forall M > 0, \exists \delta > 0, \forall x \in \mathbb{R} .\ \left( x \in I_\delta(x_0) \setminus \{x_0\} \implies g(x) > M \right) \\
> \Updownarrow \\
> \displaystyle\lim_{x \to x_0} g(x) = + \infty
> \end{array}
> $$
> 
> dimostrando così la tesi.
> 
> Stesso discorso per il secondo caso.
> 
> $\blacksquare$
^dimostrazione-del-teorema-del-confronto-per-limiti-infiniti

> [!esercizio]+ Esercizio ($\blacklozenge \lozenge \lozenge$): completa la dimostrazione
> 
> Completa la [dimostrazione del teorema del confronto per limiti infiniti](Limiti.md#^dimostrazione-del-teorema-del-confronto-per-limiti-infiniti) dimostrando il secondo caso:
> 
> $$
> \displaystyle\lim_{x \to x_0} g(x) = - \infty \implies \lim_{x \to x_0} f(x) = - \infty
> $$

%% 
mettere soluzione dell'esercizio
%%

%% dimostrazione pag. 169 Lancelotti %%

%% 
Osservazioni 3.24 pag. 170 Lancelotti
%%

> [!teorema]+ Primo teorema del confronto
> 
> Date due [funzioni](Funzioni.md#^definizione-funzione) $f,g \colon A \subseteq \mathbb{R} \to \mathbb{R}$ (con $A \ne \emptyset$) e un [punto di accumulazione](Topologia%20dei%20reali.md#^definizione-punto-di-accumulazione) $x_0 \in \mathbb{R} \cup \{ \pm \infty \}$ per $A$, se esistono i [limiti](Limiti.md#^definizione-limite)
> 
> $$
> \begin{array}{}
> \displaystyle\lim_{x \to x_0} f(x) = l \in \mathbb{R} \cup \{ \pm \infty \} \\
> \displaystyle\lim_{x \to x_0} g(x) = m \in \mathbb{R} \cup \{ \pm \infty \}
> \end{array}
> $$
> 
> ed esiste un [intorno](Topologia%20dei%20reali.md#^definizione-intorno-di-un-punto) $I(x_0)$ di $x_0$ tale che
> 
> $$
> \forall x \in (A \cap I(x_0)) \setminus \{ x_0 \} . \big (f(x) \le g(x))
> $$
> 
> allora
> 
> $$
> l \le m
> $$
^primo-teorema-del-confronto

%% 
dimostrazione pag. 170 lancelotti
%%

%% 
osservazioni pag. 170-171 lancelotti
%%

# 8 - Limiti di funzioni monotone

> [!teorema]+ Teorema dei limiti laterali di funzioni monotone
> 
> Data una [funzione](Funzioni.md#^definizione-funzione) $f \colon \text{dom}(f) \to \mathbb{R}$ [monotona](Proprietà%20delle%20funzioni.md#^definizione-funzione-strettamente-decrescente-o-monotona-su-un-intervallo) su $\text{dom}(f)$ e un [punto di accumulazione](Topologia%20dei%20reali.md#^definizione-punto-di-accumulazione) $x_0 \in \mathbb{R}$ per $\text{dom}(f) \cap (x_0, + \infty)$, allora si ha che:
> - Se $f$ è [(strettamente) crescente](Proprietà%20delle%20funzioni.md#^definizione-funzione-strettamente-decrescente-o-monotona-su-un-intervallo), allora:
> 	$$
> 	\lim_{x \to x_0^+} f(x) = \inf\{ f(x) \mid x \in \text{dom}(f) \land x > x_0 \}
> 	$$
> - Se $f$ è [(strettamente) decrescente](Proprietà%20delle%20funzioni.md#^definizione-funzione-strettamente-decrescente-o-monotona-su-un-intervallo), allora:
> 	$$
> 	\lim_{x \to x_0^+} f(x) = \sup\{ f(x) \mid x \in \text{dom}(f) \land x > x_0 \}
> 	$$
> 
> Se $x_0$ è un [punto di accumulazione](Topologia%20dei%20reali.md#^definizione-punto-di-accumulazione) per $\text{dom}(f) \cap (-\infty, x_0)$, allora si ha che:
> - Se $f$ è [(strettamente) crescente](Proprietà%20delle%20funzioni.md#^definizione-funzione-strettamente-decrescente-o-monotona-su-un-intervallo), allora:
> 	$$
> 	\lim_{x \to x_0^+} f(x) = \sup\{ f(x) \mid x \in \text{dom}(f) \land x < x_0 \}
> 	$$
> - Se $f$ è [(strettamente) decrescente](Proprietà%20delle%20funzioni.md#^definizione-funzione-strettamente-decrescente-o-monotona-su-un-intervallo), allora:
> 	$$
> 	\lim_{x \to x_0^+} f(x) = \inf\{ f(x) \mid x \in \text{dom}(f) \land x < x_0 \}
> 	$$
^teorema-dei-limiti-laterali-di-funzioni-monotone

%% grafico pag. 177-178 lancelotti %%

%% osservazione 3.43 lancelotti %%

---

> [!fonti]+ Fonti
> 
> - 🏫 Corso di Laurea in Informatica (`L-31 R`) presso l'Università di Torino:
> 	- Corso di _Analisi Matematica - canale C_, A.A. 2020-21 ([pagina Moodle](https://informatica.i-learn.unito.it/course/view.php?id=2075)):
> 		- Prof. Barutello Vivina Laura, videolezioni:
> 			- [_L6b_](https://informatica.i-learn.unito.it/local/streamingfilemanager/file.php/informatica.i-learn.unito.it/2075/L6b.mp4).
> 			- [_L7a_](https://informatica.i-learn.unito.it/local/streamingfilemanager/file.php/informatica.i-learn.unito.it/2075/L7a.mp4), [_L7b_](https://informatica.i-learn.unito.it/local/streamingfilemanager/file.php/informatica.i-learn.unito.it/2075/L7b.mp4).
> 			- [_L8a_](https://informatica.i-learn.unito.it/local/streamingfilemanager/file.php/informatica.i-learn.unito.it/2075/L8a.mp4), [_L8b_](https://informatica.i-learn.unito.it/local/streamingfilemanager/file.php/informatica.i-learn.unito.it/2075/L8b.mp4).
> - 📚 Sergio Lancelotti, _Lezioni di Analisi Matematica I_, Celid, 2020 (ISBN: `978-8867891979`):
> 	- Parte I - _I concetti dell'analisi matematica_:
> 		- Capitolo 1 - _Funzioni e modelli_:
> 			- 1 - _Funzioni e grafici_:
> 				- 1.4 - _Comportamento asintotico all'infinito_.
> 		- Capitolo 3 - _Limiti e continuità_:
> 			- 2 - _Limiti di funzioni_:
> 				- 2.2 - _Limiti laterali_.
> 			- 3 - _Teoremi su limiti e continuità_:
> 				- 3.3 - _Algebra dei limiti_.
> 				- 3.5 - _Teoremi del confronto_.
> 				- 3.6 - _Limiti delle funzioni monotone_.
