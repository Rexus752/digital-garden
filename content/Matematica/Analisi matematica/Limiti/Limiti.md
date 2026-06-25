
> [!premessa]+ Premessa
> 
> Ciao! Se è la prima volta che capiti su questo sito, ti consiglio di consultare la [pagina principale](index.md) di questo cosiddetto _Giardino Digitale_ per scoprire meglio cos'è e come navigarlo.
> 
> Lo stato di questa nota è al momento: 🔴 <font color="#FF7F7F">_Bozza_</font>.

%% 
in realtà è **Calcolo infinitesimale**
%%

---

%%
Parlando di pendenza di f nel punto c, abbiamo

$$
\lim_{\Delta x \to 0} \dfrac{f(c + \Delta x) - f(c)}{\Delta x}
$$

e se questo oggetto esiste finito allora è $f'(c)$.

Per esempio, $f(x) = 4x^2$ con $c = 1$, abbiamo che
$$
f'(1) = \lim_{\Delta x \to 0} (8 + 4\Delta x) = 0
$$

Con questa scrittura vogliamo indicare che i valori di $8 + 4\Delta x$ si avvicinano a $8$ quando quello di $\Delta x$ si avvicina a $0$.

Però ora ci chiediamo: quanto piccolo deve essere $\Delta x$ affinché $8 + 4\Delta x$ si trovi a una distanza da $8$ inferiore (per esempio) a $10^{-2}$ (cioè al massimo $8 \pm 0.01$)?

Calcoliamo:

$$
d(8 + 4\Delta x, 8) < 10^{-2} \iff |4\Delta x| < 10^{-2} \iff |\Delta x| < 0.04
$$

Quindi

$$
\Delta x \in I_{0.04}(0) \implies 8+4\Delta x \in I_{0.01}(8)
$$

Invece di fissare $10^{-2}$ come soglia, potevamo prendere un qualsiasi numero $\varepsilon > 0$ piccolo a piacere e chiedere: quanto vicino a $0$ devo prendere $\Delta x$ affinché $8 + 4\Delta x$ sia a una distanza da $8$ inferiore a $\varepsilon$?

$$
d(8 + 4\Delta x, 8) < \varepsilon \iff |4\Delta x| < \varepsilon \iff |\Delta x| < \dfrac{\varepsilon}{4}
$$

Conclusione:

$$
\forall \epsilon > 0 . \left( \Delta x \in I_{\dfrac{\varepsilon}{4}}(0) \implies 8 + 4\Delta x \in I_{\varepsilon}(8) \right)
$$

Attenzione: l'ampiezza dell'intorno in cui devo prendere $\Delta x$ dipende da "quanto vicino a $8$" voglio avere $8 + 4 \Delta x$.

Formalizzando, abbiamo che $\lim_{\Delta x \to 0} (8 + 4 \Delta x) = 8$ significa che, per ogni $\varepsilon > 0$ esiste un $\delta$ (in questo caso uguale a $\dfrac{\varepsilon}{4}$) tale che se $\Delta x \in I_\delta(0)$ allora $8 + 4\Delta x \in I_\varepsilon(8)$.

Questa è la definizione di limite finito al finito.

[!definizione] Definizione: limite finito al finito

Data una [funzione](Funzioni.md#^definizione-funzione) $f \colon I_r(c) \setminus \{ c \} \to \mathbb{R}$ per qualche $r > 0$, si dice che $f$ ammette limite finito $l$ per $x$ che tende a $c$ e si scrive

$$
\lim_{x \to c} f(x) = l
$$

se

$$
\forall \varepsilon > 0, \exists \delta > 0 . \left( x \in I_\delta(c) \setminus \{ c \} \implies f(x) \in I_\varepsilon(l) \right) 
$$

Osservazioni:
1. Gli intorni possono essere sostituiti dalla distanza:
	$$
	\forall \varepsilon > 0, \exists \delta > 0 . \left( 0 < |x - c| < \delta \implies |f(x) - l| < \varepsilon  \right) 
	$$
2. Il valore di $\delta$ dipende da $\varepsilon$, motivo per cui alcuni usano la notazione $\delta(\varepsilon)$ per indicare che $\delta$ è in funzione di $\varepsilon$
3. Il limite per $x \to c$ non prescrive il comportamento della funzione in $x = c$, cioè non è necessario che la funzione sia definita anche in $c$.
	Esempio:
	- Una funzione non definita in $c$
	- Una funzione per cui $f(x) = l$
	- Una funzione per cui $f(x) \ne l$
	hanno tutte limite uguale a $l$!
%%

Introduciamo quindi una delle nozioni più importanti dell'analisi matematica, ossia quella di [_limite_](Limiti.md#^definizione-limite). È alla base di altre nozioni fondamentali, quali ad esempio quella di _derivata_%% link %% e di _integrale_%% link %%. Prima di vedere la definizione, introduciamo questo concetto attraverso alcuni esempi che ci permettono di capire il suo significato.

Immaginiamo di avere una [funzione](Funzioni.md#^definizione-funzione)
$$
\begin{align*}
f \colon \mathbb{R} & \to \mathbb{R} \\
x & \mapsto 2x^2 - x
\end{align*}
$$

Quando la variabile indipendente%% Link %% $x$ diventa _arbitrariamente grande_, ossia quando assume valori via via sempre maggiori, si dice che $x$ _tende all'infinito_ o, più precisamente, $x$ _tende a più infinito_ e si indica con

$$
x \to + \infty
$$

Analizziamo il comportamento di $f$ quando $x \to + \infty$:

| $x$    | $f(x) = 2x^2 - x$    |
| ------ | -------------------- |
| $10^1$ | $1.9 \cdot 10^2$     |
| $10^2$ | $1.99 \cdot 10^4$    |
| $10^3$ | $1.99 \cdot 10^6$    |
| $10^4$ | $1.99 \cdot 10^8$    |
| $10^5$ | $1.99 \cdot 10^{10}$ |

Da questa tabella si intuisce che al tendere di $x$ all'infinito i valori di $f(x)$ diventano sempre più grandi. Con il linguaggio introdotto in precedenza possiamo affermare che anche $f(x)$ tende a più infinito: esprimiamo questo fatto con la scrittura

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

> [!definizione]+ Definizione: limite
> 
> Data una [funzione](Funzioni.md#^definizione-funzione) $f \colon \text{dom}(f) \to \mathbb{R}$, un [punto di accumulazione](Topologia%20dei%20reali.md#^definizione-punto-di-accumulazione) $x_0 \in \mathbb{R} \cup \{ \pm \infty \}$ per $\text{dom}(f)$ e un valore%% link %% $l \in \mathbb{R} \cup \{ \pm \infty \}$, diciamo che **$f$ ha limite $l$ per $x$ che tende a $x_0$** se, per ogni [intorno](Topologia%20dei%20reali.md#^definizione-intorno-di-un-punto) $I(l)$ di $l$, esiste un [intorno](Topologia%20dei%20reali.md#^definizione-intorno-di-un-punto) $I(x_0)$ di $x_0$ tale che, per ogni $x \in \text{dom}(f)$ con $x \in I(x_0)$ e $x \ne x_0$, si ha che $f(x) \in I(l)$:
> 
> $$
> \forall I(l), \exists I(x_0) . \big( x \in \text{dom}(f) \cap I(x_0) \land x = x_0 \implies f(x) \in I(l) \big) 
> $$
> 
> In tal caso, scriviamo
> 
> $$
> \lim_{x \to x_0} f(x) = l
> $$
> 
> che si legge "_limite per $x$ che tende a $x_0$ di $f(x)$ uguale a $l$_" o "_$f(x)$ tende a $l$ per $x$ che tende a $x_0$_".
^definizione-limite

> [!osservazione]+ Osservazione: non è necessario che $\color{#7F7F7F} x_0 \in \text{dom}(f)$
> 
> Nella [definizione di _limite_](Limiti.md#^definizione-limite), il punto%% link %% $x_0$ è un [punto di accumulazione](Topologia%20dei%20reali.md#^definizione-punto-di-accumulazione) per $\text{dom}(f)$, quindi può anche **non** appartenere al dominio%% link %%: ecco perché si richiede che $x \ne x_0$. Un altro motivo per cui ciò accade è che, anche se $x_0 \in \text{dom}(f)$, il [limite](Limiti.md#^definizione-limite), sia che esista sia che non esista, non dipende dal valore%% link %% di $f$ in $x_0$, ma solo dai valori di $f$ nei punti%% link %% in un [intorno](Topologia%20dei%20reali.md#^definizione-intorno-di-un-punto) di $x_0$.

# 1 - I casi specifici dei limiti

La [definizione di _limite_](Limiti.md#^definizione-limite) che abbiamo introdotto contempla tutti i casi possibili, in cui $x$ può essere reale (cioè $x \in \mathbb{R}$) o infinito%% Link %% (cioè $x = \pm \infty$) ed $l$ può anch'esso essere reale (cioè $l \in \mathbb{R}$) o infinito%% link %% (cioè $l = \pm \infty$). Analizziamo quindi tutte le possibili combinazioni.

%% fare tabella con tutte le combinazioni possibili con link a tutte le osservazioni %%

## 1.1 - $x_0 \in \mathbb{R} \land l \in \mathbb{R}$

> [!osservazione]+ Osservazione: limite con $\color{#7F7F7F} x_0 \in \mathbb{R} \land l \in \mathbb{R}$
> 
> Nel caso in cui $x_0 \in \mathbb{R} \land l \in \mathbb{R}$, gli [intorni](Topologia%20dei%20reali.md#^definizione-intorno-di-un-punto) di $x_0$ e di $l$ sono
> 
> $$
> \begin{array}{}
> I(x_0) = I_\delta(x_0) = (x_0 - \delta, x_0 + \delta) \\
> I(l) = I_\varepsilon(l) = (l - \varepsilon, l + \varepsilon)
> \end{array}
> $$
> 
> La definizione diventa quindi:
> 
> $$
> \begin{array}{}
> \displaystyle
> \lim_{x \to x_0} f(x) = l \\
> \Updownarrow \\
> \forall \varepsilon > 0, \exists \delta > 0, \forall x \in \text{dom}(f) . \big( 0 < |x - x_0| < \delta \implies |f(x) - l| < \varepsilon \big)
> \end{array}
> $$
> 
> Questa definizione ci dice che, più $x$ è vicino a $x_0$, più $f(x)$ è vicino a $l$. Infatti, per quanto ci si voglia avvicinare a $l$ (ossia per quanto sia piccolo il valore della distanza $\varepsilon$ tra $f(x)$ ed $l$), si trova che per tutti i punti%% link %% $x$ in $\text{dom}(f)$ (escluso $x_0$) abbastanza vicini a $x_0$ (ossia contenuti nella distanza $\delta$ tra $x$ ed $x_0$) il corrispondente valore $f(x)$ è nella distanza $\varepsilon$ prestabilita da $l$.
^osservazione-limite-con-x0-finito-l-finito

> [!esempio]- Esempio di un limite con $\color{#7F7FFF} x_0 \in \mathbb{R} \land l \in \mathbb{R}$
> 
> Per esempio, per la [funzione](Funzioni.md#^definizione-funzione)
> 
> $$
> f(x) = \dfrac{x^2 - 1}{x - 1}
> $$
> 
> diamo per scontato di sapere che vale il [limite](Limiti.md#^definizione-limite)
> 
> $$
> \lim_{x \to 1} f(x) = 2
> $$
> 
> Prendendo un certo punto%% link %% $x'$ "lontano" da $x_0$, dobbiamo dimostrare che la sua immagine%% link %% $f(x')$ sia più distante da $l$ di quanto lo saranno le immagini%% link %% di altri punti%% link %% $x_1, x_2, \ldots$ più vicini a $x_0$.
> 
> Per esempio, prendiamo il punto%% link %% $x' = 1.4$ distante da $x_0$ per $\delta' = |x' - x_0| = 0.4$ la cui immagine%% Link %% $f(x') = f(1.4) = 2.4$ è distante da $l=2$ per un valore $\varepsilon' = f(x') - l = 0.4$.
> 
> Prendiamo tutti i punti $x_1 = 1.05, x_2 = 1.1, \ldots$ più vicini a $x_0$ di quanto non lo sia $x'$, ossia con distanze
> 
> $$
> \begin{array}{}
> \delta_1 = |x_1 - x_0| = 0.05 \\
> \delta_2 = |x_2 - x_0| = 0.01 \\
> \ldots
> \end{array}
> $$
> 
> Questi punti avranno la propria immagine $f(x_1) = 2.05, f(x_2) =2.1, \ldots$ molto più vicina a $l$ di quanto non lo sia quella di $f(x)$, cioè $\varepsilon' = 0.4$:
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
> | Valori di $x$ | $\delta = \|x - x_0\|$     | $f(x)$          | $\varepsilon = \|f(x) - l\|$    |
> | ------------- | ----------------- | --------------- | ----------------- |
> | $x' = 1.4$    | $\delta' = 0.4$   | $f(x') = 2.4$   | $\varepsilon' = 0.4$ |
> | $x_2 = 1.1$   | $\delta_2 = 0.1$  | $f(x_2) = 2.1$  | $\varepsilon' = 0.1$ |
> | $x_1 = 1.05$  | $\delta_1 = 0.05$ | $f(x_1) = 2.05$ | $\varepsilon' = 0.5$ |
> 
> Abbiamo cioè dimostrato che, per un $\varepsilon$ qualsiasi (in questo caso $e' = 0.4$), esiste un $\delta$ (in questo caso $\delta' = 0.4$) tale che, per ogni $x \in \text{dom}(f)$ (come, per esempio, $x_1$ e $x_2$), se la distanza tra questi e $x_0$ è minore di $\delta$ allora la distanza tra $f(x)$ ed $l$ è minore di $\varepsilon$.

%% rappresentare graficamente %%

> [!osservazione]+ Osservazione: basta un $\color{#7F7F7F} \delta$ qualsiasi nei limiti con $\color{#7F7F7F} x_0 \in \mathbb{R} \land l \in \mathbb{R}$
> 
> In un [limite con $x_0 \in \mathbb{R} \land l \in \mathbb{R}$](Limiti.md#^osservazione-limite-con-x0-finito-l-finito) non è importante trovare il miglior $\delta$, cioè la distanza minore possibile tra $f(x)$ ed $l$, ma ne basta uno qualunque che funzioni.
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
> Vogliamo dimostrare che vale il [limite](Limiti.md#^definizione-limite)
> 
> $$
> \lim_{x \to 1} f(x) = 5
> $$
> 
> Secondo la [definizione del caso $x_0 \in \mathbb{R} \land l \in \mathbb{R}$](Limiti.md#^osservazione-limite-con-x0-finito-l-finito), abbiamo che
> 
> $$
> \forall \varepsilon > 0, \exists \delta > 0, \forall x \in \mathbb{R} . \big( 0 < |x - 1| < \delta \implies |f(x) - 5| < \varepsilon \big)
> $$
> 
> Consideriamo un $\varepsilon > 0$ qualunque: esiste un $\delta$ che rispetta questa definizione?
> 
> Partiamo dall'obiettivo che vogliamo dimostrare, cioè che $|f(x) - 5| < \varepsilon$. Si ha che, se $x \ne x_0 = 1$, allora
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
> Dato che, per definizione, abbiamo anche $|x-1| < \delta$, prendiamo arbitrariamente $\displaystyle\delta = \dfrac{\varepsilon}{3}$, che non è necessariamente il $\delta$ più piccolo che possiamo prendere in questo [limite](Limiti.md#^definizione-limite).
> 
> Ciò ci porta al fatto che, per ogni $x$ tale che $0 < |x-1| < \delta$, soddisfiamo automaticamente l'obiettivo $|f(x) - 5| < \varepsilon$, verificando così il [limite](Limiti.md#^definizione-limite). 
> 
> Perché $\displaystyle\delta = \dfrac{\varepsilon}{3}$ è "arbitrario"? Perché avremmo potuto prendere $\displaystyle\delta = \dfrac{\varepsilon}{4}$ o $\displaystyle\delta = \dfrac{\varepsilon}{10}$ o qualunque altro valore più piccolo di $\dfrac{\varepsilon}{3}$, ma tanto funzionerebbero tutti: $\dfrac{\varepsilon}{3}$ è semplicemente il più comodo che emerge dal calcolo.
> 
> Notiamo anche il fatto che $f(1) = 4 \ne 5$, ma è irrilevante: la condizione $0 < |x - 1|$ esclude esattamente $x = 1$, quindi il valore in quel punto%% link %% non conta.

%% continua dall'ultima frase a pagina 128 a pagina 129 di Lancelotti %%

## 1.2 - $x_0 \in \mathbb{R} \land l = + \infty$

> [!osservazione]+ Osservazione: limite con $\color{#7F7F7F} x_0 \in \mathbb{R} \land l = + \infty$
> 
> Nel caso in cui $x_0 \in \mathbb{R} \land l = + \infty$, gli [intorni](Topologia%20dei%20reali.md#^definizione-intorno-di-un-punto) di $x_0$ e di $l$ sono
> 
> $$
> \begin{array}{}
> I(x_0) = I_\delta(x_0) = (x_0 - \delta, x_0 + \delta) \\
> I(l) = (a, + \infty)
> \end{array}
> $$
> 
> La definizione diventa quindi:
> 
> $$
> \begin{array}{}
> \displaystyle
> \lim_{x \to x_0} f(x) = + \infty \\
> \Updownarrow \\
> \forall a \in \mathbb{R}, \exists \delta > 0, \forall x \in \text{dom}(f) . \big( 0 < |x - x_0| < \delta \implies f(x) > a\big)
> \end{array}
> $$
> 
> Questa definizione ci dice che, più $x$ è vicino a $x_0$, più $f(x)$ diventa positivo. Infatti, per quanto si voglia spingere $f(x)$ verso $+ \infty$ (ossia per quanto $f(x)$ sia strettamente maggiore di $a$ con $a$ sufficientemente grande), si trova che per tutti i punti%% link %% $x$ in $\text{dom}(f)$ (escluso $x_0$) abbastanza vicini a $x_0$ (ossia contenuti nella distanza $\delta$ tra $x$ ed $x_0$) il corrispondente valore $f(x)$ sarà più grande di $a$ come prestabilito.
^osservazione-limite-con-x0-finito-l-piu-infinito

> [!esempio]- Esempio di un limite con $\color{#7F7FFF} x_0 \in \mathbb{R} \land l = +\infty$
> 
> Per esempio, per la [funzione](Funzioni.md#^definizione-funzione)
> 
> $$
> f(x) = \dfrac{1}{(x-1)^2}
> $$
> 
> diamo per scontato di sapere che vale il [limite](Limiti.md#^definizione-limite)
> 
> $$
> \lim_{x \to 1} f(x) = + \infty
> $$
> 
> Prendendo un certo punto%% link %% $x'$ "lontano" da $x_0$, dobbiamo dimostrare che la sua immagine%% link %% $f(x')$ sia minore di una certa soglia reale $a$, mentre le immagini%% link %% di altri punti%% link %% $x_1, x_2, \ldots$ più vicini a $x_0$ diventano molto più grandi di tale soglia.
> 
> Per esempio, scegliamo come soglia $a = 25$ e prendiamo il punto%% link %% $x' = 1.4$ distante da $x_0$ per $\delta' = |x' - x_0| = 0.4$ la cui immagine%% Link %% $f(x') = f(1.4) = 6.25$ è ancora minore della soglia $a = 25$.
> 
> Prendiamo tutti i punti $x_1 = 1.05, x_2 = 1.1, \ldots$ più vicini a $x_0$ di quanto non lo sia $x'$, ossia con distanze
> 
> $$
> \begin{array}{}
> \delta_1 = |x_1 - x_0| = 0.05 \\
> \delta_2 = |x_2 - x_0| = 0.01 \\
> \ldots
> \end{array}
> $$
> 
> Questi punti avranno la propria immagine $f(x_1) = 400, f(x_2) =10000, \ldots$ molto più grande della soglia $a = 25$.
> 
> | Valori di $x$ | $\delta = \|x - x_0\|$ | $f(x)$         | Confronto con $a = 25$ |
> | ------------- | ---------------------- | -------------- | ---------------------- |
> | $x' = 1.4$    | $\delta' = 0.4$        | $f(x') = 6.25$ | $f(x') < a$            |
> | $x_2 = 1.1$   | $\delta_2 = 0.1$       | $f(x_2) = 100$ | $f(x_2) > a$           |
> | $x_1 = 1.05$  | $\delta_1 = 0.05$      | $f(x_1) = 400$ | $f(x_1) > a$           |
> 
> Abbiamo cioè dimostrato che, per una soglia reale qualsiasi $a$ (in questo caso $a = 25$), esiste un $\delta$ (in questo caso $\delta' = 0.4$) tale che, per ogni $x \in \text{dom}(f)$ (come, per esempio, $x_1$ e $x_2$), se la distanza tra questi e $x_0$ è minore di $\delta$, allora il valore di $f(x)$ è maggiore di $a$.

> [!osservazione]+ Osservazione: basta un $\color{#7F7F7F} \delta$ qualsiasi nei limiti con $\color{#7F7F7F} x_0 \in \mathbb{R} \land l = + \infty$
> 
> In un [limite con $x_0 \in \mathbb{R} \land l = + \infty$](Limiti.md#^osservazione-limite-con-x0-finito-l-piu-infinito) non è importante trovare il miglior $\delta$, cioè la distanza minore possibile tra $f(x)$ ed $l$, ma ne basta uno qualunque che funzioni.
> 
> Per esempio, consideriamo la [funzione](Funzioni.md#^definizione-funzione) $f \colon \mathbb{R} \to \mathbb{R}$ definita da
> 
> $$
> f(x) = \dfrac{1}{x^2}
> $$
> 
> Vogliamo dimostrare che vale il [limite](Limiti.md#^definizione-limite)
> 
> $$
> \lim_{x \to 0} f(x) = + \infty
> $$
> 
> Secondo la [definizione del caso $x_0 \in \mathbb{R} \land l = +\infty$](Limiti.md#^osservazione-limite-con-x0-finito-l-piu-infinito), abbiamo che
> 
> $$
> \forall a \in \mathbb{R}, \exists \delta > 0, \forall x \in \mathbb{R} . \left(  0 < |x| < \delta \implies \dfrac{1}{x^2} > a \right)
> $$
> 
> Consideriamo un $a \in \mathbb{R}$ qualunque: esiste un $\delta$ che rispetta questa definizione?
> 
> Partiamo dall'obiettivo che vogliamo dimostrare, cioè che $\dfrac{1}{x^2} > a$. Si ha che, se $x \ne x_0 = 0$, allora
> 
> $$
> \begin{array}{}
> \dfrac{1}{x^2} > a \\
> \Updownarrow \\
> x^2 < \dfrac{1}{a} \\
> \Updownarrow \\
> - \dfrac{1}{\sqrt a} < x < \dfrac{1}{\sqrt a}
> \end{array}
> $$
> 
> Dato che, per definizione, abbiamo anche $|x| < \delta$, prendiamo arbitrariamente $\displaystyle\delta = \dfrac{1}{\sqrt a}$, che non è necessariamente il $\delta$ più piccolo che possiamo prendere in questo [limite](Limiti.md#^definizione-limite).
> 
> Ciò ci porta al fatto che, per ogni $x$ tale che $0 < |x| < \delta$, soddisfiamo automaticamente l'obiettivo $\dfrac{1}{x^2} > a$, verificando così il [limite](Limiti.md#^definizione-limite). 

%%
Osservazione:
non c'è bisogno di scrivere come condizioni di esistenza
$$
\forall x \in \mathbb{R} \setminus \{ 0 \}
$$
perché nelle parentesi tonde viene già richiesto che $x \ne 0$
%%

## 1.3 - $x_0 \in \mathbb{R} \land l = - \infty$

> [!osservazione]+ Osservazione: limite con $\color{#7F7F7F} x_0 \in \mathbb{R} \land l = - \infty$
> 
> Nel caso in cui $x_0 \in \mathbb{R} \land l = - \infty$, gli [intorni](Topologia%20dei%20reali.md#^definizione-intorno-di-un-punto) di $x_0$ e di $l$ sono
> 
> $$
> \begin{array}{}
> I(x_0) = I_\delta(x_0) = (x_0 - \delta, x_0 + \delta) \\
> I(l) = (-\infty, a)
> \end{array}
> $$
> 
> La definizione diventa quindi:
> 
> $$
> \begin{array}{}
> \displaystyle
> \lim_{x \to x_0} f(x) = - \infty \\
> \Updownarrow \\
> \forall a \in \mathbb{R}, \exists \delta > 0, \forall x \in \text{dom}(f) . \big( 0 < |x - x_0| < \delta \implies f(x) < a \big)
> \end{array}
> $$
> 
> Questa definizione ci dice che, più $x$ è vicino a $x_0$, più $f(x)$ diventa negativo. Infatti, per quanto si voglia spingere $f(x)$ verso $- \infty$ (ossia per quanto $f(x)$ sia strettamente minore di $a$ con $a$ sufficientemente piccolo), si trova che per tutti i punti%% link %% $x$ in $\text{dom}(f)$ (escluso $x_0$) abbastanza vicini a $x_0$ (ossia contenuti nella distanza $\delta$ tra $x$ ed $x_0$) il corrispondente valore $f(x)$ sarà più piccolo di $a$ come prestabilito.
^osservazione-limite-con-x0-finito-l-meno-infinito

## 1.4 - $x_0 = + \infty \land l \in \mathbb{R}$

> [!osservazione]+ Osservazione: limite con $\color{#7F7F7F} x_0 = + \infty \land l \in \mathbb{R}$
> 
> Nel caso in cui $x_0 = + \infty \land l \in \mathbb{R}$, gli [intorni](Topologia%20dei%20reali.md#^definizione-intorno-di-un-punto) di $x_0$ e di $l$ sono
> 
> $$
> \begin{array}{}
> I(x_0) = (a, + \infty)\\
> I(l) = I_\varepsilon(l) = (l - \varepsilon, l + \varepsilon)
> \end{array}
> $$
> 
> La definizione diventa quindi:
> 
> $$
> \begin{array}{}
> \displaystyle
> \lim_{x \to + \infty} f(x) = l \\
> \Updownarrow \\
> \forall \varepsilon > 0, \exists a \in \mathbb{R}, \forall x \in \text{dom}(f) . \big( x > a \implies |f(x) - l| < \varepsilon \big)
> \end{array}
> $$
> 
> Questa definizione ci dice che, più $x$ è positivo, più $f(x)$ è vicino a $l$. Infatti, per quanto ci si voglia avvicinare a $l$ (ossia per quanto sia piccolo il valore della distanza $\varepsilon$ tra $f(x)$ ed $l$), si trova che per tutti i punti%% link %% $x$ in $\text{dom}(f)$ (escluso $x_0$) maggiori di un certo punto $a$ il corrispondente valore $f(x)$ è nella distanza $\varepsilon$ prestabilita da $l$.
^osservazione-limite-con-x0-piu-infinito-l-finito

> [!osservazione]+ Osservazione: basta un $\color{#7F7F7F} a$ qualsiasi nei limiti con $\color{#7F7F7F} x_0 = + \infty \land l \in \mathbb{R}$
> 
> In un [limite con $x_0 = + \infty \land l \in \mathbb{R}$](Limiti.md#^osservazione-limite-con-x0-piu-infinito-l-finito) non è importante trovare il miglior $a$, cioè la soglia migliore per cui $x$ deve essere maggiore, ma ne basta uno qualunque che funzioni.
> 
> Per esempio, consideriamo la [funzione](Funzioni.md#^definizione-funzione) $f \colon \mathbb{R} \to \mathbb{R}$ definita da
> 
> $$
> f(x) = \dfrac{1}{x}
> $$
> 
> Vogliamo dimostrare che vale il [limite](Limiti.md#^definizione-limite)
> 
> $$
> \lim_{x \to +\infty} f(x) = 0
> $$
> 
> Secondo la [definizione del caso $x_0 = + \infty \land l \in \mathbb{R}$](Limiti.md#^osservazione-limite-con-x0-piu-infinito-l-finito), abbiamo che
> 
> $$
> \forall \varepsilon > 0, \exists a \in \mathbb{R}, \forall x \in \mathbb{R} \setminus \{ 0 \} . \left( x > a \implies \left| \dfrac{1}{x} \right| < \varepsilon \right)
> $$
> 
> Consideriamo un $\varepsilon > 0$ qualunque: esiste un $a$ che rispetta questa definizione?
> 
> Partiamo dall'obiettivo che vogliamo dimostrare, cioè che $\displaystyle\left| \dfrac{1}{x} \right| < \varepsilon$. Si ha che, se $x \ne 0$, allora
> 
> $$
> \begin{array}{}
> \displaystyle \left| \dfrac{1}{x} \right| < \varepsilon \\
> \Updownarrow \\
> |x| > \dfrac{1}{\varepsilon} \\
> \Updownarrow \\
> x < - \dfrac{1}{\varepsilon} \land x > \dfrac{1}{\varepsilon}
> \end{array}
> $$
> 
> Dato che, per definizione, abbiamo anche $x > a$, prendiamo arbitrariamente $a = \dfrac{1}{\varepsilon}$, che non è necessariamente l'$a$ più piccolo che possiamo prendere in questo [limite](Limiti.md#^definizione-limite).
> 
> Ciò ci porta al fatto che, per ogni $x\in \mathbb{R} \setminus \{ 0 \}$ tale che $x > a$, soddisfiamo automaticamente l'obiettivo $\displaystyle\left| \dfrac{1}{x} \right| < \varepsilon$, verificando così il [limite](Limiti.md#^definizione-limite).

## 1.5 - $x_0 = - \infty \land l \in \mathbb{R}$

> [!osservazione]+ Osservazione: limite con $\color{#7F7F7F} x_0 = - \infty \land l \in \mathbb{R}$
> 
> Nel caso in cui $x_0 = -\infty \land l \in \mathbb{R}$, gli [intorni](Topologia%20dei%20reali.md#^definizione-intorno-di-un-punto) di $x_0$ e di $l$ sono
> 
> $$
> \begin{array}
> I(x_0) = (- \infty, a) \\
> I(l) = I_\varepsilon(l) = (l - \varepsilon, l + \varepsilon)
> \end{array}
> $$
> 
> La definizione diventa quindi:
> 
> $$
> \begin{array}{}
> \displaystyle
> \lim_{x \to - \infty} f(x) = l \\
> \Updownarrow \\
> \forall \varepsilon > 0, \exists a \in \mathbb{R}, \forall x \in \text{dom}(f) . \big( x < a \implies |f(x) - l| < \varepsilon \big)
> \end{array}
> $$
> 
> Questa definizione ci dice che, più $x$ è negativo, più $f(x)$ è vicino a $l$. Infatti, per quanto ci si voglia avvicinare a $l$ (ossia per quanto sia piccolo il valore della distanza $\varepsilon$ tra $f(x)$ ed $l$), si trova che per tutti i punti%% link %% $x$ in $\text{dom}(f)$ (escluso $x_0$) minori di un certo punto $a$ il corrispondente valore $f(x)$ è nella distanza $\varepsilon$ prestabilita da $l$.
^osservazione-limite-con-x0-meno-infinito-l-finito

## 1.6 - $x_0 = + \infty \land l = + \infty$

> [!osservazione]+ Osservazione: limite con $\color{#7F7F7F} x_0 = + \infty \land l = + \infty$
> 
> Nel caso in cui $x_0 = + \infty \land l = + \infty$, gli [intorni](Topologia%20dei%20reali.md#^definizione-intorno-di-un-punto) di $x_0$ e di $l$ sono
> 
> $$
> I(x_0) = (a, + \infty)
> $$
> 
> e
> 
> $$
> I(l) = (b, + \infty)
> $$
> 
> La definizione diventa quindi:
> 
> $$
> \begin{array}{}
> \displaystyle
> \lim_{x \to + \infty} f(x) = + \infty \\
> \Updownarrow \\
> \forall a \in \mathbb{R}, \exists b \in \mathbb{R}, \forall x \in \text{dom}(f) . \big( x > b \implies f(x) > a \big)
> \end{array}
> $$
> 
> Questa definizione ci dice che, più $x$ è positivo, più $f(x)$ diventa positivo. Infatti, comunque si scelga un valore $a \in \mathbb{R}$, si trova che per tutti i punti%% link %% $x \in \text{dom}(f)$ maggiori di un certo punto%% link %% $b$ la loro rispettiva immagine%% link %% $f(x)$ è maggiore di $a$.
^osservazione-limite-con-x0-piu-infinito-l-piu-infinito

%% grafico %%

> [!osservazione]+ Osservazione: basta un $\color{#7F7F7F} b$ qualsiasi nei limiti con $\color{#7F7F7F} x_0 = + \infty \land l = + \infty$
> 
> In un [limite con $x_0 = + \infty \land l = + \infty$](Limiti.md#^osservazione-limite-con-x0-piu-infinito-l-piu-infinito) non è importante trovare il miglior $b$, cioè la soglia migliore per cui $x$ deve essere maggiore, ma ne basta uno qualunque che funzioni.
> 
> Per esempio, consideriamo la [funzione](Funzioni.md#^definizione-funzione) $f \colon \mathbb{R} \to \mathbb{R}$ definita da
> 
> $$
> f(x) = e^x
> $$
> 
> Vogliamo dimostrare che vale il [limite](Limiti.md#^definizione-limite)
> 
> $$
> \lim_{x \to +\infty} e^x = + \infty
> $$
> 
> Secondo la [definizione del caso $x_0 = + \infty \land l = + \infty$](Limiti.md#^osservazione-limite-con-x0-piu-infinito-l-piu-infinito), abbiamo che
> 
> $$
> \forall a \in \mathbb{R}, \exists b \in \mathbb{R}, \forall x \in \mathbb{R} . \left( x > b \implies e^x > a \right)
> $$
> 
> Consideriamo un $a \in \mathbb{R}$ qualunque: esiste un $b$ che rispetta questa definizione?
> 
> Partiamo dall'obiettivo che vogliamo dimostrare, cioè che $e^x > a$. Si ha che, se $x \ne 0$, allora
> 
> $$
> \begin{array}{}
> e^x > a \\
> \Updownarrow \\
> x > \ln a
> \end{array}
> $$
> 
> Dato che, per definizione, abbiamo anche $x > b$, prendiamo arbitrariamente $b = \ln a$, che non è necessariamente il $b$ più grande che possiamo prendere in questo [limite](Limiti.md#^definizione-limite).
> 
> Ciò ci porta al fatto che, per ogni $x\in \mathbb{R}$ tale che $x > b$, soddisfiamo automaticamente l'obiettivo $e^x > a$, verificando così il [limite](Limiti.md#^definizione-limite).

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
> 
> > [!dimostrazione]- Dimostrazione
> > 
> > Infatti, per assurdo supponiamo che questo limite esista e sia
> > 
> > $$
> > \lim_{x \to 0} \text{sgn}(x) = l
> > $$
> > 
> > Poiché $|\text{sgn}(x)| \le l$, possiamo supporre che $l \in \mathbb{R}$, cioè $l \ne \pm \infty$.
> > 
> > Per la [definizione di limite con $x_0 \in \mathbb{R} \land l \in \mathbb{R}$](Limiti.md#^osservazione-limite-con-x0-finito-l-finito), abbiamo che
> > 
> > $$
> > \forall \varepsilon > 0, \exists \delta > 0, \forall x \in \mathbb{R} . \big( 0 < |x| < \delta \implies |\text{sgn}(x) - l| < \varepsilon \big)
> > $$
> > 
> > Abbiamo allora tre casi possibili:
> > - Se $l>0$, allora preso un $\displaystyle\varepsilon = \dfrac{l}{2}$ esiste un $\delta > 0$ tale che, per ogni $x \in \mathbb{R}$ con $0 < |x| < \delta$, si ha che
> > 	$$
> > 	\begin{array}{}
> > 	|\text{sgn}(x)-l| < \dfrac{l}{2} \\
> > 	\Updownarrow \\
> > 	-\dfrac{l}{2} < \text{sgn}(x) - l < \dfrac{l}{2} \\
> > 	\Updownarrow \\
> > 	\dfrac{l}{2} < \text{sgn}(x) < \dfrac{3}{2}l\\
> > 	\end{array}
> > 	$$
> > 	e in particolare, per ogni $x \in \mathbb{R}$ tale che $0 < |x| < \delta$, si ha che $\text{sgn}(x) > \dfrac{l}{2} > 0$: otteniamo però un assurdo perché, se $x < 0$, allora $\text{sgn}(x)= -1 < 0$.
> > - Se $l < 0$, allora preso un $\displaystyle\varepsilon = - \dfrac{l}{2}$ esiste un $\delta > 0$ tale che, per ogni $x \in \mathbb{R}$ con $0 < |x| < \delta$, si ha che
> > 	$$
> > 	\begin{array}{}
> > 	|\text{sgn}(x)-l| < -\dfrac{l}{2} \\
> > 	\Updownarrow \\
> > 	\dfrac{l}{2} < \text{sgn}(x) - l < -\dfrac{l}{2} \\
> > 	\Updownarrow \\
> > 	\dfrac{3}{2}l < \text{sgn}(x) < \dfrac{l}{2} \\
> > 	\end{array}
> > 	$$
> > 	e in particolare, per ogni $x \in \mathbb{R}$ tale che $0 < |x| < \delta$, si ha che $\text{sgn}(x) < \dfrac{l}{2} < 0$: otteniamo però un assurdo perché, se $x > 0$, allora $\text{sgn}(x)= 1 > 0$.
> > - Se $l = 0$, allora preso un $\displaystyle\varepsilon = \dfrac{l}{2}$ esiste un $\delta > 0$ tale che, per ogni $x \in \mathbb{R}$ con $0 < |x| < \delta$, si ha che $|\text{sgn}(x)| < \dfrac{l}{2}$: otteniamo però un assurdo perché, se $x > 0$, allora $|\text{sgn}(x)| =1 >\dfrac{l}{2}$.
> > 
> > $\blacksquare$

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

> [!definizione] Definizione: limiti laterali
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

%% spiegare perché vale questa osservazione %%

# 5 - Algebra dei limiti

%% 
pagg. 161-164 lancelotti
%%

# 6 - Teoremi del confronto

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

%% dimostrazione pag. 169 %%

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

> [!teorema]+ Secondo teorema del confronto (o teorema dei due carabinieri)
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
^secondo-teorema-del-confronto-o-teorema-dei-due-carabinieri

%% 
dimostrazione pag. 171 lancelotti
%%

%% 
Perché si chiama "teorema dei due carabinieri"
%%

%% 
Osservazioni 3.28 e 3.29 pag. 172 lancelotti
%%

# 7 - Limiti delle funzioni monotone

> [!teorema]+ Teorema dei limiti laterali delle funzioni monotone
> 
> Data una funzione monotona%% link %% $f \colon \text{dom}(f) \to \mathbb{R}$ e un [punto di accumulazione](Topologia%20dei%20reali.md#^definizione-punto-di-accumulazione) $x_0 \in \mathbb{R}$ per $\text{dom}(f) \cap (x_0, + \infty)$, allora si ha che
> 
> $$
> \lim_{x \to x_0^+} f(x) = \begin{cases}
> \inf\{ f(x) \mid x \in \text{dom}(f) \land x > x_0 \} & \text{se } f \text{ è crescente} \\
> \sup\{ f(x) \mid x \in \text{dom}(f) \land x > x_0 \} & \text{se } f \text{ è decrescente}
> \end{cases}
> $$
> 
> Se $x_0$ è un [punto di accumulazione](Topologia%20dei%20reali.md#^definizione-punto-di-accumulazione) per $\text{dom}(f) \cap (-\infty, x_0)$, allora si ha che
> 
> $$
> \lim_{x \to x_0^-} f(x) = \begin{cases}
> \sup\{ f(x) \mid x \in \text{dom}(f) \land x < x_0 \} & \text{se } f \text{ è crescente} \\
> \inf\{ f(x) \mid x \in \text{dom}(f) \land x < x_0 \} & \text{se } f \text{ è decrescente}
> \end{cases}
> $$
^teorema-dei-limiti-laterali-delle-funzioni-monotone

%% grafico pag. 177-178 lancelotti %%

%% osservazione 3.43 lancelotti %%

---

> [!fonti]+ Fonti
> 
> - 🏫 Corso di Laurea in Informatica (`L-31 R`) presso l'Università di Torino:
> 	- Corso di _Analisi Matematica - canale C_, A.A. 2020-21 ([pagina Moodle](https://informatica.i-learn.unito.it/course/view.php?id=2075)):
> 		- Prof. Barutello Vivina Laura, videolezioni:
> 			- [_L6b_](https://informatica.i-learn.unito.it/local/streamingfilemanager/file.php/informatica.i-learn.unito.it/2075/L6b.mp4).
> - 📚 Sergio Lancelotti, _Lezioni di Analisi Matematica I_, Celid, 2020 (ISBN: `978-8867891979`):
> 	- Capitolo 3 - _Limiti e continuità_:
> 		- 2 - _Limiti di funzioni_:
> 			- 2.2 - _Limiti laterali_.
> 		- 3 - _Teoremi su limiti e continuità_:
> 			- 3.3 - _Algebra dei limiti_.
> 			- 3.5 - _Teoremi del confronto_.
> 			- 3.6 - _Limiti delle funzioni monotone_.
