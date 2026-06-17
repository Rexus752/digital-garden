---
title: Derivate
---

> [!premessa]+ Premessa
> 
> Ciao! Se è la prima volta che capiti su questo sito, ti consiglio di consultare la [pagina principale](index.md) di questo cosiddetto _Giardino Digitale_ per scoprire meglio cos'è e come navigarlo.
> 
> Lo stato di questa nota è al momento: 🔴 <font color="#FF7F7F">_Bozza_</font>.

---

> [!definizione] Definizione: derivabilità e derivata (prima) di una funzione in un punto
> 
> Data una [funzione](content/Matematica/Teoria%20degli%20insiemi/Funzioni/_index.md#^definizione-funzione) $f \colon \text{dom}(f) \to \mathbb{R}$ e un [punto interno](Topologia%20dei%20reali.md#^definizione-punto-interno) $x_0 \in \text{dom}(f)$ a $\text{dom}(f)$, diciamo che **$f$ è derivabile in $x_0$** se esiste finito%% link %% il [limite](content/Matematica/Analisi%20matematica/Limiti/_index.md#^definizione-limite)
> 
> $$
> \lim_{x \to x_0} \dfrac{f(x) - f(x_0)}{x - x_0}
> $$
> 
> e in tal caso denotiamo questo [limite](content/Matematica/Analisi%20matematica/Limiti/_index.md#^definizione-limite) con uno dei seguenti simboli:
> 
> $$
> f'(x_0), \quad Df(x_0), \quad \dfrac{df}{dx}(x_0), \quad \dot f(x_0)
> $$
> 
> e lo chiamiamo **derivata (prima) di $f$ in $x_0$**.
^definizione-derivabilita-e-derivata-prima-di-una-funzione-in-un-punto

> [!definizione] Definizione: derivabilità di una funzione in un sottoinsieme del dominio
> 
> Data una [funzione](content/Matematica/Teoria%20degli%20insiemi/Funzioni/_index.md#^definizione-funzione) $f \colon \text{dom}(f) \to \mathbb{R}$ e un [sottoinsieme](content/Matematica/Teoria%20degli%20insiemi/_index.md#^definizione-insieme) $A \subseteq \text{dom}(f)$ (con $A \ne \emptyset$), diciamo che **$f$ è derivabile in $A$** se è [derivabile](content/Matematica/Analisi%20matematica/Derivate/_index.md#^definizione-derivabilita-e-derivata-prima-di-una-funzione-in-un-punto) in ogni punto%% link %% di $A$.
^definizione-derivabilita-di-una-funzione-in-un-sottoinsieme-del-dominio

%% 
Il quoeiente è detto rapporto incrementale di f in x0 e rappresenta la variazione relativa di f rispetto a quella della variabile indipendente x nel passare da x0 a x. Il limite di questo rapporto incrememntale, se esiste in R, è la derivata di f in x0. Quindi rappresenta la variazione relativa di f rispetto a quella dela variabile indipendente x nel passare da x0 a x, quando x tende a x0.
%%

Se il [limite](content/Matematica/Analisi%20matematica/Limiti/_index.md#^definizione-limite) è $\pm \infty$ o non esiste, allora $f$ non è derivabile in $x_0$. %% integrare nella definizione %%

Talvolta il limite del rapporto incrementale è scritto nel seguente modo:

$$
\lim_{x \to x_0} \dfrac{f(x)-f(x_0)}{x - x_0} = \lim_{h \to 0} \dfrac{f(x_0 + h) - f(x_0)}{h}
$$

con $h = x - x_0$.

%% 
osservazione 1.2 pag. 238-239 lancelotti
%%

%% 
osservazione 1.4 ed esempio 1.5 pagg. 239-241
%%

> [!teorema] Teorema del legame fra la continuità e la derivabilità
> 
> Data una [funzione](content/Matematica/Teoria%20degli%20insiemi/Funzioni/_index.md#^definizione-funzione) $f \colon \text{dom}(f) \to \mathbb{R}$ e un [punto interno](Topologia%20dei%20reali.md#^definizione-punto-interno) $x_0 \in \text{dom}(f)$ a $\text{dom}(f)$, se $f$ è [derivabile](content/Matematica/Analisi%20matematica/Derivate/_index.md#^definizione-derivabilita-e-derivata-prima-di-una-funzione-in-un-punto) in $x_0$ allora $f$ è [continua](Funzioni%20continue.md#^definizione-funzione-continua) in $x_0$.
^teorema-del-legame-fra-la-continuita-e-la-derivabilita

%% 
dimostrazione pag. 242 lancelotti
%%

> [!osservazione] Osservazione: derivabilità implica continuità ma non il contrario
> 
> Per il [teorema del legame fra la continuità e la derivabilità](content/Matematica/Analisi%20matematica/Derivate/_index.md#^teorema-del-legame-fra-la-continuita-e-la-derivabilita), la [derivabilità](content/Matematica/Analisi%20matematica/Derivate/_index.md#^definizione-derivabilita-e-derivata-prima-di-una-funzione-in-un-punto) implica automaticamente la [continuità](Funzioni%20continue.md#^definizione-funzione-continua), ma non è vero il contrario: per esempio, la [funzione](content/Matematica/Teoria%20degli%20insiemi/Funzioni/_index.md#^definizione-funzione) $f(x) = |x|$ è [continua](Funzioni%20continue.md#^definizione-funzione-continua) ma non [derivabile](content/Matematica/Analisi%20matematica/Derivate/_index.md#^definizione-derivabilita-e-derivata-prima-di-una-funzione-in-un-punto) in $0$.
> 
> In particolare, abbiamo che per contrapposizione%% link %% se una [funzione](content/Matematica/Teoria%20degli%20insiemi/Funzioni/_index.md#^definizione-funzione) non è [continua](Funzioni%20continue.md#^definizione-funzione-continua) allora non è neanche [derivabile](content/Matematica/Analisi%20matematica/Derivate/_index.md#^definizione-derivabilita-e-derivata-prima-di-una-funzione-in-un-punto): riprendendo l'esempio precedente della funzione $f(x) = \text{sgn}(x)$%% link %%, poiché $f$ non è [continua](Funzioni%20continue.md#^definizione-funzione-continua) in $0$, allora possiamo immediatamente concludere che $f$ non è [derivabile](content/Matematica/Analisi%20matematica/Derivate/_index.md#^definizione-derivabilita-e-derivata-prima-di-una-funzione-in-un-punto) in $0$.

> [!proposizione] Proposizione: in una derivata la variazione è un infinitesimo
> 
> Se una [funzione](content/Matematica/Teoria%20degli%20insiemi/Funzioni/_index.md#^definizione-funzione) $f$ è [derivabile](content/Matematica/Analisi%20matematica/Derivate/_index.md#^definizione-derivabilita-e-derivata-prima-di-una-funzione-in-un-punto) in $x_0$, ossia
> 
> $$
> \lim_{x \to x_0} \dfrac{f(x) - f(x_0)}{x - x_0} = f'(x_0) \in \mathbb{R}
> $$
> 
> allora la variazione%% link %% di $f$ nel passaggio da $x_0$ a $x$
> - è un [infinitesimo del primo ordine](Infiniti%20e%20infinitesimi.md#^definizione-infinitesimo-di-ordine-alfa-rispetto-all-infinitesimo-campione-u) se $f'(x_0) \ne 0$ o
> - è un [infinitesimo di ordine superiore al primo](Infiniti%20e%20infinitesimi.md#^definizione-infinitesimo-di-ordine-superiore-o-inferiore-all-ordine-alpha-rispetto-all-infinitesimo-campione-u) se $f'(x_0) = 0$
> rispetto all'[infinitesimo campione](Infiniti%20e%20infinitesimi.md#^definizione-infiniti-e-infinitesimi-campione) $u(x) = |x - x_0|$ per $x \to x_0$ con [parte principale](Infiniti%20e%20infinitesimi.md#^definizione-infinitesimo-di-ordine-alfa-rispetto-all-infinitesimo-campione-u) $f'(x_0)(x - x_0)$:
> 
> $$
> f(x) - f(x_0) = f'(x_0)(x - x_0) + o(|x - x_0|) \text{ per } x \to x_0
> $$
^proposizione-in-una-derivata-la-variazione-e-un-infinitesimo

> [!dimostrazione] Dimostrazione: in una derivata la variazione è un infinitesimo
> 
> Dimostriamo che [in una funzione derivabile la variazione di $f$ nel passaggio da $x_0$ a $x$ è un infinitesimo](content/Matematica/Analisi%20matematica/Derivate/_index.md#^proposizione-in-una-derivata-la-variazione-e-un-infinitesimo).
> 
> Analizziamo prima il caso in cui $f'(x_0) \ne 0$: se osserviamo la [definizione di _infinitesimo di ordine $\alpha$ rispetto all'infinitesimo campione $u(x)$_](Infiniti%20e%20infinitesimi.md#^definizione-infinitesimo-di-ordine-alfa-rispetto-all-infinitesimo-campione-u), abbiamo che
> 
> $$
> \displaystyle\lim_{x \to x_0} \dfrac{f(x)}{[u(x)]^\alpha} = l \in \mathbb{R} \setminus \{ 0 \}
> $$
> 
> Nel nostro caso:
> - $f(x)$ corrisponde a $f(x) - f(x_0)$,
> - $[u(x)]^\alpha$ è l'[infinitesimo campione](Infiniti%20e%20infinitesimi.md#^definizione-infiniti-e-infinitesimi-campione) $|x - x_0|$ con ordine $\alpha = 1$ e
> - $l$ è $f'(x_0)$ che, in questo caso, è diverso da $0$, quindi rispettiamo la condizione $l \in \mathbb{R} \setminus \{ 0 \}$.
> 
> Sostituendo quindi i termini della [definizione](Infiniti%20e%20infinitesimi.md#^definizione-infinitesimo-di-ordine-alfa-rispetto-all-infinitesimo-campione-u) (e, in particolare, utilizzando la terza formula, quella con l'[$o$-piccolo](Infiniti%20e%20infinitesimi.md#^definizione-o-piccolo)), otteniamo
> 
> $$
> f(x) - f(x_0) =f'(x_0)(|x - x_0|)^1 + o((|x - x_0|)^1) \text{ per } x \to x_0
> $$
> 
> Possiamo quindi concludere che in questo caso la variazione%% link %% di $f$ nel passaggio da $x_0$ a $x$ è un [infinitesimo del primo ordine](Infiniti%20e%20infinitesimi.md#^definizione-infinitesimo-di-ordine-alfa-rispetto-all-infinitesimo-campione-u) se $f'(x_0) \ne 0$.
> 
> Nel caso in cui $f'(x_0) = 0$, abbiamo che
> 
> $$
> \lim_{x \to x_0} \frac{f(x) - f(x_0)}{x - x_0} = 0
> $$
> 
> Cioè $f(x) - f(x_0)$ è [$o$-piccolo](Infiniti%20e%20infinitesimi.md#^definizione-o-piccolo) di $x - x_0$:
> 
> $$
> f(x) - f(x_0) = o(x - x_0)
> $$
> 
> Ciò implica che [$f(x) - f(x_0)$ è un infinitesimo di ordine superiore al primo rispetto all'infinitesimo campione $u(x) = |x - x_0|$ per $x -> x_0$](Infiniti%20e%20infinitesimi.md#^definizione-infinitesimo-di-ordine-superiore-o-inferiore-all-ordine-alpha-rispetto-all-infinitesimo-campione-u).
> 
> In entrambi i casi, è corretto riassumere il tutto nella formula
> 
> $$
> f(x) - f(x_0) = f'(x_0)(x - x_0) + o(|x - x_0|) \text{ per } x \to x_0
> $$
> 
> perché:
> - Se $f'(x_0) \ne 0$, questa formula è letteralmente la [terza formula della definizione di _infinitesimo di ordine $\alpha$ rispetto all'infinitesimo campione $u(x)$_](Infiniti%20e%20infinitesimi.md#^definizione-infinitesimo-di-ordine-alfa-rispetto-all-infinitesimo-campione-u) che abbiamo scritto poco fa.
> - Se $f'(x_0) = 0$, otteniamo la [terza formula della definizione di _infinitesimo di ordine superiore al primo rispetto all'infinitesimo campione $u(x)$_](Infiniti%20e%20infinitesimi.md#^definizione-infinitesimo-di-ordine-superiore-o-inferiore-all-ordine-alpha-rispetto-all-infinitesimo-campione-u).
> 
> $\blacksquare$

%% 
scrivere meglio queste definizioni per far capire le formule
%%

%% 
Capire come integrare i valori assoluti in $x - x_0$ per rispecchiare la formula dell'infinitesimo campione
%%

%% 
Osservazione: il termine $f(x) = f(x_0) + f'(x_0)(x - x_0)$ è il second membro dell'equazione della retta tangente al grafico di $f$ in $(x_0, f(x_0))$ (vedi interpretazione geometrica di prima)- Questa uguaglianza ci dice che per $x \to x_0$ la funzione $f$ è approssimabile con il polinomio di primo grado $f(x_0) + f'(x_0)(x - x_0)$, ovvero ce il grafico di $f$ è approssimabile con la retta tangente al grafico di $f$ in $(x_0, f(x_0))$, a meno di termini che sono infinitesimi di ordine superiore al primo.
%%

%% 
\# Derivate delle funzioni elementari

trasformare tutte in proposizioni da dimostrare, pagg. 243-245:


- $\forall x \in \mathbb{R}.(f(x) = c \in \mathbb{R} \implies f'(x) = 0)$
- $\forall x,n \in \mathbb{R}.(f(x) = x^n \implies f'(x) = nx^{n-1})$

ecc.
%%

# Differenziale

> [!definizione] Definizione: differenziale di una funzione
> 
> Data una [funzione](content/Matematica/Teoria%20degli%20insiemi/Funzioni/_index.md#^definizione-funzione) $f \colon \text{dom}(f) \to \mathbb{R}$ e un [punto interno](Topologia%20dei%20reali.md#^definizione-punto-interno) $x_0 \in \text{dom}(f)$ a $\text{dom}(f)$, diciamo che **$f$ è differenziabile in $x_0$** se $f$ è [derivabile](content/Matematica/Analisi%20matematica/Derivate/_index.md#^definizione-derivabilita-e-derivata-prima-di-una-funzione-in-un-punto) in $x_0$ e in tal caso chiamiamo **differenziale di $f$ in $x_0$** la funzione lineare%% link %% $df(x_0) \colon \mathbb{R} \to \mathbb{R}$ definita da
> 
> $$
> df(x_0)(x) = f'(x_0)x
> $$
^definizione-differenziale-di-una-funzione

Quindi il [differenziale](content/Matematica/Analisi%20matematica/Derivate/_index.md#^definizione-differenziale-di-una-funzione) di $f$ in $x_0$ è una [funzione](content/Matematica/Teoria%20degli%20insiemi/Funzioni/_index.md#^definizione-funzione) il cui grafico%% link %% è una retta%% link %% passante per l'origine $O(0;0)$%% ink %% con coefficiente angolare%% Link %% $f'(x_0)$.

Posto $dx \colon \mathbb{R} \to \mathbb{R}$ la funzione lineare identica%% link %%, cioè la funzione tale che $dx(x) = x$ per ogni $x \in \mathbb{R}$, allora il [differenziale](content/Matematica/Analisi%20matematica/Derivate/_index.md#^definizione-differenziale-di-una-funzione) di $f$ in $x_0$ diventa

$$
df(x_0) = f'(x_0)dx
$$

Infatti

$$
\forall x \in \mathbb{R}. \left( df(x_0)(x) = f'(x_0) \cdot \underbrace{dx(x)}_{=x} = f'(x_0)x \right) 
$$

> [!esempio] Esempi di differenziali
> 
> - $f(x) = x^2 \implies df(x) = f'(x)dx = 2xdx$
> - $f(x) = \sin x \implies df(x) = f'(x)dx = \cos x\ dx$
> - $f(x) = e^x \implies df(x) = f'(x)dx = e^xdx$
> - $f(x) = \log x \implies df(x) = f'(x)dx = \dfrac{1}{x}dx$

# Derivate laterali

> [!definizione] Definizione: derivate laterali di una funzione
> 
> Data una [funzione](content/Matematica/Teoria%20degli%20insiemi/Funzioni/_index.md#^definizione-funzione) $f \colon \text{dom}(f) \to \mathbb{R}$, un [punto interno](Topologia%20dei%20reali.md#^definizione-punto-interno) $x_0 \in \text{dom}(f)$ a $\text{dom}(f)$ e un $\delta > 0$ tale che $[x_0;x_0 + \delta) \subseteq \text{dom}(f)$, diciamo che **$f$ è derivabile da destra in $x_0$** se esiste il [limite](content/Matematica/Analisi%20matematica/Limiti/_index.md#^definizione-limite)
> 
> $$
> \lim_{x \to x_0^+} \dfrac{f(x) - f(x_0)}{x - x_0} = l \in \mathbb{R}
> $$
> 
> e in tal caso denotiamo questo [limite](content/Matematica/Analisi%20matematica/Limiti/_index.md#^definizione-limite) con $D^+f(x_0)$ e lo chiamiamo **derivata destra di $f$ in $x_0$**.
> 
> Se esiste un $\delta > 0$ tale che $(x_0 - \delta, x_0] \subseteq \text{dom}(f)$, diciamo che **$f$ è derivabile da sinistra in $x_0$** se esiste il [limite](content/Matematica/Analisi%20matematica/Limiti/_index.md#^definizione-limite)
> 
> $$
> \lim_{x \to x_0^-} \dfrac{f(x) - f(x_0)}{x - x_0} = l \in \mathbb{R}
> $$
> 
> e in tal caso denotiamo questo [limite](content/Matematica/Analisi%20matematica/Limiti/_index.md#^definizione-limite) con $D^-f(x_0)$ e lo chiamiamo **derivata sinistra di $f$ in $x_0$**.
> 
> Le derivate destra e sinistra sono anche dette **derivate laterali**.
^definizione-derivate-laterali-di-una-funzione

> [!esempio] Esempio di derivate laterali di una funzione
> 
> Consideriamo la [funzione](content/Matematica/Teoria%20degli%20insiemi/Funzioni/_index.md#^definizione-funzione) $f(x) = |x|$, abbiamo visto%% Link %% che è [derivabile](content/Matematica/Analisi%20matematica/Derivate/_index.md#^definizione-derivabilita-e-derivata-prima-di-una-funzione-in-un-punto) in ogni $x \ne 0$ e che non è [derivabile](content/Matematica/Analisi%20matematica/Derivate/_index.md#^definizione-derivabilita-e-derivata-prima-di-una-funzione-in-un-punto) in $0$. Inoltre si ha che
> 
> $$
> \begin{array}{}
> \displaystyle\lim_{x \to 0^+} \dfrac{f(x) - f(0)}{x - 0} = \lim_{x \to 0^+} \dfrac{|x|}{x} = \lim_{x \to 0^+} \dfrac{x}{x} = 1 \implies D^+f(0)=1 \\
> \displaystyle\lim_{x \to 0^-} \dfrac{f(x) - f(0)}{x - 0} = \lim_{x \to 0^-} \dfrac{|x|}{x} = \lim_{x \to 0^-} \dfrac{-x}{x} = -1 \implies D^-f(0)=-1 \\
> \end{array}
> $$

%% 
Osservazione 1.14 pag. 247 Lancelotti
%%

> [!teorema] Teorema del legame fra la derivata e le derivate laterali
> 
> Data una [funzione](content/Matematica/Teoria%20degli%20insiemi/Funzioni/_index.md#^definizione-funzione) $f \colon \text{dom}(f) \to \mathbb{R}$ e un [punto interno](Topologia%20dei%20reali.md#^definizione-punto-interno) $x_0 \in \text{dom}(f)$ a $\text{dom}(f)$. Se esistono le [derivate laterali](content/Matematica/Analisi%20matematica/Derivate/_index.md#^definizione-derivate-laterali-di-una-funzione) $D^+f(x_0)$ e $D^-f(x_0)$, allora $f$ è [continua](Funzioni%20continue.md#^definizione-funzione-continua) in $x_0$ e inoltre $f$ è [derivabile](content/Matematica/Analisi%20matematica/Derivate/_index.md#^definizione-derivabilita-e-derivata-prima-di-una-funzione-in-un-punto) in $x_0$ se e solo se $D^+f(x_0) = D^-f(x_0)$ e, in tal caso,
> 
> $$
> f'(x_0) = D^+f(x_0) = D^-f(x_0)
> $$

%% 
dimostrazione pag. 247 lancelotti
%%

> [!definizione] Definizione: derivabilità e derivata (prima) di una funzione
> 
> Data una [funzione](content/Matematica/Teoria%20degli%20insiemi/Funzioni/_index.md#^definizione-funzione) $f \colon \text{dom}(f) \to \mathbb{R}$, diciamo che **$f$ è derivabile** se è [derivabile](content/Matematica/Analisi%20matematica/Derivate/_index.md#^definizione-derivabilita-e-derivata-prima-di-una-funzione-in-un-punto) in ogni punto%% link %% del dominio%% link %% $\text{dom}(f)$ e, nei [punti di frontiera](Topologia%20dei%20reali.md#^definizione-punto-di-frontiera) appartenenti al dominio%% link %%, se sono [derivabili lateralmente](content/Matematica/Analisi%20matematica/Derivate/_index.md#^definizione-derivate-laterali-di-una-funzione).
> 
> In tal caso è definita una [funzione](content/Matematica/Teoria%20degli%20insiemi/Funzioni/_index.md#^definizione-funzione), detta **derivata (prima) di $f$**, denotata con $f'$ (oppure $Df$, $\dfrac{df}{dx}$ p $\dot f$) e definita come
> 
> $$
> \begin{align*}
> f' \colon \text{dom}(f) & \to \mathbb{R} \\
> x & \mapsto f'(x)
> \end{align*}
> $$
^definizione-derivabilita-e-derivata-prima-di-una-funzione

> [!esempio] Esempio di derivabiità di una funzione
> 
> Consideriamo la [funzione](content/Matematica/Teoria%20degli%20insiemi/Funzioni/_index.md#^definizione-funzione) $f(x) = x^q$ con $q \in \mathbb{Q}^{> 0} \setminus \mathbb{N}$. Abbiamo che $\text{dom}(f) = [0, + \infty)$ e, per ogni $x > 0$, si ha che $f$ è [derivabile](content/Matematica/Analisi%20matematica/Derivate/_index.md#^definizione-derivabilita-e-derivata-prima-di-una-funzione-in-un-punto) in $x$ con $f'(x) = qx^{q-1}$. In $x=0$ si ha che
> 
> $$
> \lim_{x \to 0^+} \dfrac{f(x) - f(0)}{x} = \lim_{x \to 0^+} \dfrac{x^q}{x} = \lim_{x \to 0^+} x^{q-1} = \begin{cases}
> + \infty & \text{se } q < 1 \\
> 0 & \text{se } q > 1
> \end{cases}
> $$
> 
> Quindi $f$ è [derivabile da destra](content/Matematica/Analisi%20matematica/Derivate/_index.md#^definizione-derivate-laterali-di-una-funzione) in $0$ solo se $q > 1$ e in tal caso $D^+f(0) = 0$.

# Punti di non derivabilità

Introduciamo una classificazione per i punti di non derivabilità%% link %% di una [funzione](content/Matematica/Teoria%20degli%20insiemi/Funzioni/_index.md#^definizione-funzione), ossia per i punti%% link %% in cui $f$ è [continua](Funzioni%20continue.md#^definizione-funzione-continua) ma non [derivabile](content/Matematica/Analisi%20matematica/Derivate/_index.md#^definizione-derivabilita-e-derivata-prima-di-una-funzione).

> [!definizione] Definizione: punto angoloso
> 
> Data una [funzione](content/Matematica/Teoria%20degli%20insiemi/Funzioni/_index.md#^definizione-funzione) $f \colon \text{dom}(f) \to \mathbb{R}$ e un [punto interno](Topologia%20dei%20reali.md#^definizione-punto-interno) $x_0 \in \text{dom}(f)$ a $\text{dom}(f)$, diciamo che **$x_0$ è un punto angoloso per $f$** se esistono le [derivate laterali](content/Matematica/Analisi%20matematica/Derivate/_index.md#^definizione-derivate-laterali-di-una-funzione) $D^+f(x_0)$ e $D^-f(x_0)$ ma sono diverse.
^definizione-punto-angoloso

%% 
Osserviamo che per il teorema del legame fra la derivata e le derivate laterali $f$ è continua in $x_0$
%%

> [!esempio] Esempio di punto angoloso per $f(x) =|x|$
> 
> Consideriamo la [funzione](content/Matematica/Teoria%20degli%20insiemi/Funzioni/_index.md#^definizione-funzione) $f(x) = |x|$: il punto%% link %% $x_0 = 0$ è [angoloso](content/Matematica/Analisi%20matematica/Derivate/_index.md#^definizione-punto-angoloso) per $f$, infatti le [derivate laterali](content/Matematica/Analisi%20matematica/Derivate/_index.md#^definizione-derivate-laterali-di-una-funzione) non coincidono:
> 
> $$
> D^+f(0) = 1 \ne -1 = D^-f(0)
> $$
^esempio-di-punto-angoloso-per-valore-assoluto-di-x

> [!osservazione] Osservazione: perché _punto angoloso_?
> 
> Osservando l'[esempio del punto angoloso per $f(x) = |x|$](content/Matematica/Analisi%20matematica/Derivate/_index.md#^esempio-di-punto-angoloso-per-valore-assoluto-di-x), possiamo notare che le semirette%% link %% tangenti%% link %% al grafico%% link %% nell'origine%% link %% $O(0,0)$ sono rispettivamente $y=-x$ e $y=x$ e formano tra loro un angolo retto%% link %%: risulta quindi giustificata la denominazione [_punto angoloso_](content/Matematica/Analisi%20matematica/Derivate/_index.md#^definizione-punto-angoloso).

%% 
esempio 1.20 di punto angoloso per funzione a tratti pagg. 248-249 lancelotti
%%

> [!definizione] Definizione: cuspide
> 
> Data una [funzione](content/Matematica/Teoria%20degli%20insiemi/Funzioni/_index.md#^definizione-funzione) $f \colon \text{dom}(f) \to \mathbb{R}$ e un [punto interno](Topologia%20dei%20reali.md#^definizione-punto-interno) $x_0 \in \text{dom}(f)$ a $\text{dom}(f)$, diciamo che **$x_0$ è una cuspide per $f$** se $f$ è [continua](Funzioni%20continue.md#^definizione-funzione-continua) in $x_0$ e
> 
> $$
> \lim_{x \to x_0^+} \dfrac{f(x) - f(x_0)}{x - x_0} = \pm \infty \ne \mp \infty = \lim_{x \to x_0^-} \dfrac{f(x) - f(x_0)}{x - x_0}
> $$
> 
> cioè i [limiti laterali](content/Matematica/Analisi%20matematica/Limiti/_index.md#^definizione-limiti-laterali) sono entrambi uguali a $\infty$ ma di segno opposto: se uno vale $+ \infty$, l'altro deve valere $- \infty$.
^definizione-cuspide

%% 
In questo caso è necessaria l'ipotesi di continuità di $f$ in $x_0$
CHE SIGNIFICA?
%%

%% 
esempio 1.21 pag. 249
%%

> [!definizione] Definizione: punto di flesso a tangente verticale
> 
> Data una [funzione](content/Matematica/Teoria%20degli%20insiemi/Funzioni/_index.md#^definizione-funzione) $f \colon \text{dom}(f) \to \mathbb{R}$ e un [punto interno](Topologia%20dei%20reali.md#^definizione-punto-interno) $x_0 \in \text{dom}(f)$ a $\text{dom}(f)$, diciamo che **$x_0$ è un punto di flesso a tangente verticale per $f$** se $f$ è [continua](Funzioni%20continue.md#^definizione-funzione-continua) in $x_0$ e
> 
> $$
> \lim_{x \to x_0^+} \dfrac{f(x) - f(x_0)}{x - x_0} = \lim_{x \to x_0^-} \dfrac{f(x) - f(x_0)}{x - x_0} = \pm \infty
> $$
> 
> cioè i [limiti laterali](content/Matematica/Analisi%20matematica/Limiti/_index.md#^definizione-limiti-laterali) sono entrambi uguali o a $+ \infty$ o a $- \infty$.
^definizione-punto-di-flesso-a-tangente-verticale

%% 
esempio 1.22 pag. 250 lancelotti
%%

%% 
osservazione 1.23 pag. 250-251 lancelotti
%%

# Algebra delle derivate

> [!teorema] Teorema della derivata della somma
> 
> Date due [funzioni](content/Matematica/Teoria%20degli%20insiemi/Funzioni/_index.md#^definizione-funzione) $f \colon \text{dom}(f) \to \mathbb{R}$ e $g \colon \text{dom}(g) \to \mathbb{R}$ [derivabili](content/Matematica/Analisi%20matematica/Derivate/_index.md#^definizione-derivabilita-e-derivata-prima-di-una-funzione-in-un-punto) in un punto%% link %% $x_0$ [interno](Topologia%20dei%20reali.md#^definizione-punto-interno) a $\text{dom}(f) \cap \text{dom}(g)$, allora la loro somma%% link %% $f+g$ è [derivabile](content/Matematica/Analisi%20matematica/Derivate/_index.md#^definizione-derivabilita-e-derivata-prima-di-una-funzione-in-un-punto) in $x_0$ e
> 
> $$
> (f+g)'(x_0) = f'(x_0) + g'(x_0)
> $$
^teorema-della-derivata-della-somma

%% 
Dimostrazione: è un'immediata conseguenza della definizione di derivatat e viene lasciata per esercizio
%%

> [!teorema] Teorema della derivata del prodotto
> 
> Date due [funzioni](content/Matematica/Teoria%20degli%20insiemi/Funzioni/_index.md#^definizione-funzione) $f \colon \text{dom}(f) \to \mathbb{R}$ e $g \colon \text{dom}(g) \to \mathbb{R}$ [derivabili](content/Matematica/Analisi%20matematica/Derivate/_index.md#^definizione-derivabilita-e-derivata-prima-di-una-funzione-in-un-punto) in un punto%% link %% $x_0$ [interno](Topologia%20dei%20reali.md#^definizione-punto-interno) a $\text{dom}(f) \cap \text{dom}(g)$, allora il loro prodotto%% link %% $f \cdot g$ è [derivabile](content/Matematica/Analisi%20matematica/Derivate/_index.md#^definizione-derivabilita-e-derivata-prima-di-una-funzione-in-un-punto) in $x_0$ e
> 
> $$
> (f \cdot g)'(x_0) = f'(x_0) \cdot g(x_0) + f(x_0) \cdot g'(x_0)
> $$
^teorema-della-derivata-del-prodotto

%% 
dimostrazione pag. 252 lancelotti
%%

> [!teorema] Teorema della derivata del reciproco
> 
> Data una [funzione](content/Matematica/Teoria%20degli%20insiemi/Funzioni/_index.md#^definizione-funzione) $f \colon \text{dom}(f) \to \mathbb{R}$ [derivabile](content/Matematica/Analisi%20matematica/Derivate/_index.md#^definizione-derivabilita-e-derivata-prima-di-una-funzione-in-un-punto) in un punto%% link %% $x_0$ [interno](Topologia%20dei%20reali.md#^definizione-punto-interno) a $\text{dom}(f)$, se $f(x_0) \ne 0$ allora il reciproco%% link %% $\dfrac{1}{f}$ è [derivabile](content/Matematica/Analisi%20matematica/Derivate/_index.md#^definizione-derivabilita-e-derivata-prima-di-una-funzione-in-un-punto) in $x_0$ e
> 
> $$
> \left( \dfrac{1}{f} \right)'(x_0) = - \dfrac{f'(x_0)}{[f(x_0)]^2}
> $$
^teorema-della-derivata-del-reciproco

%% 
dimostrazione pag. 253 lancelotti
%%

> [!teorema] Teorema della derivata del quoziente
> 
> Date due [funzioni](content/Matematica/Teoria%20degli%20insiemi/Funzioni/_index.md#^definizione-funzione) $f \colon \text{dom}(f) \to \mathbb{R}$ e $g \colon \text{dom}(g) \to \mathbb{R}$ [derivabili](content/Matematica/Analisi%20matematica/Derivate/_index.md#^definizione-derivabilita-e-derivata-prima-di-una-funzione-in-un-punto) in un punto%% link %% $x_0$ [interno](Topologia%20dei%20reali.md#^definizione-punto-interno) a $\text{dom}(f) \cap \text{dom}(g)$, se $g(x_0) \ne 0$ allora il loro quoziente%% Link %% $\dfrac{f}{g}$ è [derivabile](content/Matematica/Analisi%20matematica/Derivate/_index.md#^definizione-derivabilita-e-derivata-prima-di-una-funzione-in-un-punto) in $x_0$ e
> 
> $$
> \left( \dfrac{f}{g} \right)'(x_0) = \dfrac{f'(x_0)g(x_0) - f(x_0)g'(x_0)}{[g(x_0)]^2}
> $$
^teorema-della-derivata-del-quoziente

%% 
dimostrazione pag. 253 lancelotti
%%

%% 
osservazione 1.25 pag. 253 lancelotti
%%

%% 
esempio 1.26 pagg. 253-254 lancelotti
%%

%% 
esercizio 1.27 pag. 254 lancelotti
%%

> [!teorema] Teorema della derivata della funzione composta
> 
> Date due [funzioni](content/Matematica/Teoria%20degli%20insiemi/Funzioni/_index.md#^definizione-funzione) $f \colon \text{dom}(f) \to \mathbb{R}$ e $g \colon \text{dom}(g) \to \mathbb{R}$ con immagine%% link %% di $f$ nel dominio%% Link %% di $g$ (cioè $\text{im}(f) \subseteq \text{dom}(f)$) e un punto%% link %% $x_0$ [interno](Topologia%20dei%20reali.md#^definizione-punto-interno) a $\text{dom}(f)$ tale che $f(x_0)$ è [interno](Topologia%20dei%20reali.md#^definizione-punto-interno) a $\text{dom}(g)$, se $f$ è [derivabile](content/Matematica/Analisi%20matematica/Derivate/_index.md#^definizione-derivabilita-e-derivata-prima-di-una-funzione-in-un-punto) in $x_0$ e $g$ è [derivabile](content/Matematica/Analisi%20matematica/Derivate/_index.md#^definizione-derivabilita-e-derivata-prima-di-una-funzione-in-un-punto) in $f(x_0)$, allora la loro composizione%% link %% $g \circ f$ è [derivabile](content/Matematica/Analisi%20matematica/Derivate/_index.md#^definizione-derivabilita-e-derivata-prima-di-una-funzione-in-un-punto) in $x_0$ e
> 
> $$
> (g \circ f)'(x_0) = g'(f(x_0)) \cdot f'(x_0)
> $$
^teorema-della-derivata-della-funzione-composta

%% 
dimostrazione pagg. 254-255 lancelotti
%%

%% 
esempio 1.29 pagg. 255-256 lancelotti
%%

%% 
osservazioni 1.30, 1.31 pag. 256 + dimostrazione 1.32 ed esempio 1.33 pagg. 256-257 lancelotti
%%

> [!teorema] Teorema della derivata della funzione inversa
> 
> Dato un intervallo%% link %% $I \subseteq \mathbb{R}$ e una [funzione continua](Funzioni%20continue.md#^definizione-funzione-continua) e invertibile%% link %% $f \colon I \to \mathbb{R}$ e un [punto interno](Topologia%20dei%20reali.md#^definizione-punto-interno) $x_0$ a $I$, se $f$ è [derivabile](content/Matematica/Analisi%20matematica/Derivate/_index.md#^definizione-derivabilita-e-derivata-prima-di-una-funzione-in-un-punto) in $x_0$ con $f'(x_0) \ne 0$, allora la sua inversa%% link %% $f^{-1}$ è [derivabile](content/Matematica/Analisi%20matematica/Derivate/_index.md#^definizione-derivabilita-e-derivata-prima-di-una-funzione-in-un-punto) in $x_0$ in $y_0 = f(x_0)$ e
> 
> $$
> \left( f^{-1} \right)'(y_0) = \dfrac{1}{f'(f^{-1}(y_0))}
> $$
^teorema-della-derivata-della-funzione-inversa

%% 
dimostrazione pag. 257 lancelotti
%%

%% 
osservazione 1.35 pagg. 257-258 lancelotti
%%

%% 
esempi 1.36 pagg. 258-259 lancelotti
%%

%% 
proposizione 1.37 pag. 259 lancelotti
%%

%% 
I teoremi 1.24, 1.28 e 1.34 valgono anche per le derivate laterali
%%

# Teoremi fondamentali del calcolo differenziale

%% 
definizione di "calcolo differenziale"
%%

## Teorema di Fermat

> [!osservazione] Osservazione: comportamento di $f$ nei punti di estremo locale
> 
> Riprendiamo la definizione di punti minimi/massimi relativi%% link %%.
> 
> Nelle applicazioni%% di cosa? %% succede spesso che:
> - i punti di massimo%% Link %% sono punti%% link %% in cui $f$ è crescente%% link %% in un [intorno sinistro](Topologia%20dei%20reali.md#^definizione-intorno-di-un-punto) di tali punti%% link %% e decrescente%% link %% in un [intorno destro](Topologia%20dei%20reali.md#^definizione-intorno-di-un-punto),
> - mentre i punti di minimo%% link %% sono punti%% link %% in cui $f$ è decrescente%% link %% in un [intorno sinistro](Topologia%20dei%20reali.md#^definizione-intorno-di-un-punto) di tali punti%% link %% e crescente%% link %% in un [intorno destro](Topologia%20dei%20reali.md#^definizione-intorno-di-un-punto):
> 
> |                  | Punti di massimo  | Punti di minimo   |
> | ---------------- | ----------------- | ----------------- |
> | Intorno sinistro | $f$ è crescente   | $f$ è decrescente |
> | Intorno destro   | $f$ è decrescente | $f$ è crescente   |
> 
> %% mettere link nella tabella %%
> 
> Inoltre, se $f$ è [derivabile](content/Matematica/Analisi%20matematica/Derivate/_index.md#^definizione-derivabilita-e-derivata-prima-di-una-funzione-in-un-punto) in tali punti%% link %%, allora la [derivata](content/Matematica/Analisi%20matematica/Derivate/_index.md#^definizione-derivabilita-e-derivata-prima-di-una-funzione-in-un-punto) in quei punti%% Link %% è nulla%% link %%, cioè la retta tangente%% Link %% al grafico%% link %% nei punti%% link %% corrispondenti ai punti di massimo%% link %% e di minimo%% link %% è orizzontale%% link %%.
> 
> %% 
> mettere foto grafico pag. 260 però disegnando le rette tangenti orizzontali con resto della spiegazione
> %%
> 
> Oppure $f$ potrebbe non essere [continua](Funzioni%20continue.md#^definizione-funzione-continua) in tali punti%% link %%, come nel caso della [funzione](content/Matematica/Teoria%20degli%20insiemi/Funzioni/_index.md#^definizione-funzione) $f(x) = |\text{sgn}(x)|$ che ha un punto di minimo%% Link %% in $x=0$ ma non è [continua](Funzioni%20continue.md#^definizione-funzione-continua) in tale punto%% link %%.
> 
> %% 
> mettere foto grafico funzione modulo segno
> %%
> 
> Oppure $f$ potrebbe non essere [derivabile](content/Matematica/Analisi%20matematica/Derivate/_index.md#^definizione-derivabilita-e-derivata-prima-di-una-funzione-in-un-punto) in tali punti%% link %%, come nel caso della [funzione](content/Matematica/Teoria%20degli%20insiemi/Funzioni/_index.md#^definizione-funzione) $f(x) = |x|$ che ha un punto di minimo%% link %% in $x = 0$ ma non è [derivabile](content/Matematica/Analisi%20matematica/Derivate/_index.md#^definizione-derivabilita-e-derivata-prima-di-una-funzione-in-un-punto) in tale punto%% link %%.
> 
> %% 
> mettere foto grafico funzione f(x)=|x|
> %%
> 
> Oppure tali punti%% link %% potrebbero anche essere [isolati](Topologia%20dei%20reali.md#^definizione-punto-isolato).
> 
> Poiché la casistica è piuttosto vasta, vogliamo poter stabilire delle condizioni necessarie e/o sufficienti affinché un punto%% link %% sia di estremo locale%% Link %% per una [funzione](content/Matematica/Teoria%20degli%20insiemi/Funzioni/_index.md#^definizione-funzione).

> [!definizione] Definizione: punto stazionario
> 
> Data una [funzione](content/Matematica/Teoria%20degli%20insiemi/Funzioni/_index.md#^definizione-funzione) $f \colon \text{dom}(f) \to \mathbb{R}$ e un [punto interno](Topologia%20dei%20reali.md#^definizione-punto-interno) $x_0 \in \text{dom}(f)$ a $\text{dom}(f)$, se $f$ è [derivabile](content/Matematica/Analisi%20matematica/Derivate/_index.md#^definizione-derivabilita-e-derivata-prima-di-una-funzione-in-un-punto) in $x_0$ allora diciamo che **$x_0$ è un punto stazionario (o critico) per $f$** se $f'(x_0) = 0$.
^definizione-punto-stazionario

%% 
esempi di punti stazionari
%%

> [!teorema] Teorema di Fermat
> 
> Data una [funzione](content/Matematica/Teoria%20degli%20insiemi/Funzioni/_index.md#^definizione-funzione) $f \colon \text{dom}(f) \to \mathbb{R}$ e un [punto interno](Topologia%20dei%20reali.md#^definizione-punto-interno) $x_0 \in \text{dom}(f)$ a $\text{dom}(f)$, se $f$ è [derivabile](content/Matematica/Analisi%20matematica/Derivate/_index.md#^definizione-derivabilita-e-derivata-prima-di-una-funzione-in-un-punto) in $x_0$ e $x_0$ è un punto di massimo%% Link %% o di minimo locale%% link %% per $f$, allora $x_0$ è un [punto stazionario](content/Matematica/Analisi%20matematica/Derivate/_index.md#^definizione-punto-stazionario) per $f$.
^teorema-di-fermat

%% 
Questo teorema prende il nome da Pierre de Fermat: https://it.wikipedia.org/wiki/Teorema_di_Fermat_sui_punti_stazionari
%%

%% 
dimostrazione pag. 262 lancelotti
%%

%% 
osservazione 2.5 pagg. 262-263 lancelotti
%%

%% 
osservazione 2.6 pag. 263 lancelotti
%%

## Teorema di Lagrange e sue conseguenze

> [!teorema] Teorema di Rolle
> 
> Data una [funzione](content/Matematica/Teoria%20degli%20insiemi/Funzioni/_index.md#^definizione-funzione) $f \colon [a,b] \to \mathbb{R}$, se $f$ è [continua](Funzioni%20continue.md#^definizione-funzione-continua) in $[a,b]$, [derivabile](content/Matematica/Analisi%20matematica/Derivate/_index.md#^definizione-derivabilita-di-una-funzione-in-un-sottoinsieme-del-dominio) in $(a,b)$ e $f(a) = f(b)$, allora esiste almeno un punto%% link %% $x_0 \in (a,b)$ tale che $f'(x_0) = 0$.
^teorema-di-rolle

%% chi è Rolle? %%

%% 
dimostrazione pagg. 263-264 lancelotti
%%

%% esempio del teorema di Rolle %%

%% osservazione 2.8 pagg. 264-265 lancelotti %%

> [!teorema] Teorema di Lagrange (o del valore medio)
> 
> Data una [funzione](content/Matematica/Teoria%20degli%20insiemi/Funzioni/_index.md#^definizione-funzione) $f \colon [a,b] \to \mathbb{R}$, se $f$ è [continua](Funzioni%20continue.md#^definizione-funzione-continua) in $[a,b]$ e [derivabile](content/Matematica/Analisi%20matematica/Derivate/_index.md#^definizione-derivabilita-di-una-funzione-in-un-sottoinsieme-del-dominio) in $(a,b)$, allora esiste almeno un punto%% link %% $x_0 \in (a,b)$ tale che $f'(x_0) = \dfrac{f(b) - f(a)}{b - a}$.
^teorema-di-lagrange-o-del-valore-medio

%% chi è Lagrange? %%

%% 
dimostrazione pag. 265 lancelotti
%%

%% 
osservazione 2.11 pag. 266 lncelotti
%%

> [!corollario] Corollario del teorema di Lagrange
> 
> Dato un intervallo%% Link %% $I \subseteq \mathbb{R}$ e una [funzione](content/Matematica/Teoria%20degli%20insiemi/Funzioni/_index.md#^definizione-funzione) $f \colon I \to \mathbb{R}$ [derivabile](content/Matematica/Analisi%20matematica/Derivate/_index.md#^definizione-derivabilita-e-derivata-prima-di-una-funzione) e due punti%% Link %% $x_0, x \in I$, esiste un punto%% link %% $t$ compreso tra $x_0$ e $x$ (non necessariamente in questo ordine) tale che
> 
> $$
> f(x) - f(x_0) = f'(t)(x - x_0)
> $$
^corollario-del-teorema-di-lagrange

%% 
la formula $f(x) - f(x_0) = f'(t)(x - x_0)$ è detta **seconda formula dell'incremento finito** (fare definizione per questa e anche per la prima formula dell'incremento finito)
%%

%% 
Dimostrazione: si applica il Teorema di Lagrange alla funzioen $f$ ristretta all'intervallo di estremi $x_0$ e $x$.
%%

%% 
Osservazione 2.13 pag. 266 lancelotti
%%

> [!teorema] Teorema del legame fra la monotonia e il segno della derivata
> 
> Dato un intervallo%% Link %% $I \subseteq \mathbb{R}$ e una [funzione](content/Matematica/Teoria%20degli%20insiemi/Funzioni/_index.md#^definizione-funzione) $f \colon I \to \mathbb{R}$ [derivabile](content/Matematica/Analisi%20matematica/Derivate/_index.md#^definizione-derivabilita-e-derivata-prima-di-una-funzione), allora:
> - $f$ è crescente%% link %% (o decrescente%% link %%) su $I$ se e solo se $f'(x) \ge 0$ (o $f'(x) \le 0$) per ogni $x \in I$:
> 	$$
> 	\forall x \in I . \left( \begin{array}{}
> 	f \text{ crescente su } I \iff f'(x) \ge 0 \\
> 	f \text{ decrescente su } I \iff f'(x) \le 0 \\
> 	\end{array} \right) 
> 	$$
> - Se $f'(x) > 0$ (o $f'(x) < 0$) per ogni $x \in I$, allora $f$ è strettamente crescente%% link %% (o strettamente decrescente%% link %%) su $I$:
> 	$$
> 	\forall x \in I . \left( \begin{array}{}
> 	f'(x) > 0 \implies f \text{ strettamente crescente su } I \\
> 	f'(x) < 0 \implies f \text{ strettamente decrescente su } I \\
> 	\end{array} \right) 
> 	$$
> 
> Se $I$ contiene uno o entrambi i suoi estremi%% link %%, la [derivabilità](content/Matematica/Analisi%20matematica/Derivate/_index.md#^definizione-derivabilita-e-derivata-prima-di-una-funzione-in-un-punto) di $f$ in quei punti%% Link %% va intesa come la [derivabilità laterale](content/Matematica/Analisi%20matematica/Derivate/_index.md#^definizione-derivate-laterali-di-una-funzione).
^teorema-del-legame-fra-la-monotonia-e-il-segno-della-derivata

%% 
dimostrazione pagg. 267-268 lancelotti
%%

%% 
Osservazioni pagg. 268 lancelotti
%%

> [!corollario] Corollario del teorema del legame fra la monotonia e il segno della derivata
> 
> Data una [funzione](content/Matematica/Teoria%20degli%20insiemi/Funzioni/_index.md#^definizione-funzione) $f \colon [a,b] \to \mathbb{R}$, se $f$ è [continua](Funzioni%20continue.md#^definizione-funzione-continua) in $[a,b]$ e [derivabile](content/Matematica/Analisi%20matematica/Derivate/_index.md#^definizione-derivabilita-di-una-funzione-in-un-sottoinsieme-del-dominio) in $(a,b)$, allora:
> - Se $f'(x) \ge 0$ (o $f'(x) \le 0$) per ogni $x \in (a,b)$, allora $f$ è crescente%% link %% (o decrescente%% link %%) su $[a,b]$.
> - Se $f'(x) > 0$ (o $f'(x) < 0$) per ogni $x \in (a,b)$, allora $f$ è strettamente crescente%% link %% (o strettamente decrescente%% link %%) su $[a,b]$.
> 
> $$
> \forall x \in (a,b) . \left( \begin{array}{}
> f'(x) \ge 0 \implies f \text{ crescente su } [a,b] \\
> f'(x) \le 0 \implies f \text{ decrescente su } [a,b] \\
> f'(x) > 0 \implies f \text{ strettamente crescente su } [a,b] \\
> f'(x) < 0 \implies f \text{ strettamente decrescente su } [a,b] \\
> \end{array} \right) 
> $$

%% 
dimostrazione pag. 269
%%

%% 
osservazione 2.17 pag. 269-270 lancelotti
%%

> [!teorema] Teorema del test per la ricerca dei punti di massimo e minimo
> 
> Data una [funzione](content/Matematica/Teoria%20degli%20insiemi/Funzioni/_index.md#^definizione-funzione) $f \colon \text{dom}(f) \to \mathbb{R}$, un intervallo%% link %% $I \subseteq \text{dom}(f)$ e un [punto interno](Topologia%20dei%20reali.md#^definizione-punto-interno) $x_0$ a $I$, se $f$ è [continua](Funzioni%20continue.md#^definizione-funzione-continua) in $I$ e [derivabile](content/Matematica/Analisi%20matematica/Derivate/_index.md#^definizione-derivabilita-di-una-funzione-in-un-sottoinsieme-del-dominio) in $I \setminus \{ x_0 \}$, allora:
> - Se $f'(x) > 0$ per ogni $x \in I$ con $x < x_0$ e $f'(x) < 0$ per ogni $x \in I$ con $x > x_0$, allora $x_0$ è un punto di massimo locale%% link %% per $f$:
> 	
> 	|                  | $x < x_0$       | $x > x_0$         |
> 	| ---------------- | --------------- | ----------------- |
> 	| Valore di $f'$   | $f'(x) > 0$     | $f'(x) < 0$       |
> 	| Monotonia di $f$ | $f$ è crescente | $f$ è decrescente |
> 
> - Se $f'(x) < 0$ per ogni $x \in I$ con $x < x_0$ e $f'(x) > 0$ per ogni $x \in I$ con $x > x_0$, allora $x_0$ è un punto di minimo locale%% link %% per $f$:
> 	 
> 	|                  | $x < x_0$         | $x > x_0$       |
> 	| ---------------- | ----------------- | --------------- |
> 	| Valore di $f'$   | $f'(x) < 0$       | $f'(x) > 0$     |
> 	| Monotonia di $f$ | $f$ è decrescente | $f$ è crescente |
> 
> - Se $f'(x) > 0$ per ogni $x \in I$ con $x \ne x_0$, allora $x_0$ non è né un punto di massimo%% link %% né un punto di minimo%% link %% per $f$:
> 	
> 	|                  | $x < x_0$       | $x > x_0$       |
> 	| ---------------- | --------------- | --------------- |
> 	| Valore di $f'$   | $f'(x) > 0$     | $f'(x) > 0$     |
> 	| Monotonia di $f$ | $f$ è crescente | $f$ è crescente |
> 
> - Se $f'(x) < 0$ per ogni $x \in I$ con $x \ne x_0$, allora $x_0$ non è né un punto di massimo%% link %% né un punto di minimo%% link %% per $f$:
> 	
> 	|                  | $x < x_0$         | $x > x_0$         |
> 	| ---------------- | ----------------- | ----------------- |
> 	| Valore di $f'$   | $f'(x) < 0$       | $f'(x) < 0$       |
> 	| Monotonia di $f$ | $f$ è decrescente | $f$ è decrescente |
^teorema-del-test-per-la-ricerca-dei-punti-di-massimo-e-minimo

%% 
mettere colori e link a queste tabelle
%%

%% dimostrazione pag. 271 lancelotti %%

%% osservazione 2.19 pagg. 271-272 lancelotti %%

%% osservazione 2.20 pag. 272 lancelotti %%

Abbiamo visto che se $f$ è una funzione costante%% link %% ed è [derivabile](content/Matematica/Analisi%20matematica/Derivate/_index.md#^definizione-derivabilita-e-derivata-prima-di-una-funzione), allora $f'(x) = 0$ per ogni $x \in \text{dom}(f)$%% , come asserito nel teorema ??? %%. Il viceversa è vero, sotto opportune ipotesi, come afferma il prossimo risultato.

> [!teorema] Teorema di caratterizzazione delle funzioni costanti
> 
> Dato un intervallo%% link %% $I \subseteq \mathbb{R}$ e una [funzione](content/Matematica/Teoria%20degli%20insiemi/Funzioni/_index.md#^definizione-funzione) $f \colon I \to \mathbb{R}$ [derivabile](content/Matematica/Analisi%20matematica/Derivate/_index.md#^definizione-derivabilita-e-derivata-prima-di-una-funzione) tale che $f'(x) = 0$ per ogni $x \in I$, allora $f$ è costante%% link %% su $I$.
^teorema-di-caratterizzazione-delle-funzioni-costanti

%% dimostrazione pag. 273 lancelotti %%

%% osservazione 2.22 pag. 273 lancelotti %%

%% esempio 2.23 pag. 273 lancelotti %%

%% esercizio 2.24 pag. 273 lancelotti %%

## Teoremi di De l'Hôpital

Questi teoremi%% link %% sono uno strumento molto potente per calcolare alcuni [limiti](content/Matematica/Analisi%20matematica/Limiti/_index.md#^definizione-limite) che sono [forme indeterminate del tipo $\dfrac{0}{0}$](Forme%20indeterminate.md#^forma-indeterminata-algebrica-del-tipo-0-su-0) o [$\dfrac{\infty}{\infty}$](Forme%20indeterminate.md#^definizione-forma-indeterminata-algebrica-del-tipo-infinito-su-infinito).

> [!teorema] Teorema di De l'Hôpital della forma indeterminata del tipo $\dfrac{0}{0}$
> 
> Dato un intervallo%% link %% $A \subseteq \mathbb{R}$, due [funzioni](content/Matematica/Teoria%20degli%20insiemi/Funzioni/_index.md#^definizione-funzione) $f,g \colon A \to \mathbb{R}$, e un [punto di accumulazione](Topologia%20dei%20reali.md#^definizione-punto-di-accumulazione) $x_0 \in \mathbb{R} \cup \{ \pm \infty \}$ per $A$, se:
> 1. i [limiti](content/Matematica/Analisi%20matematica/Limiti/_index.md#^definizione-limite) di $f$ e $g$ per $x \to x_0$ sono nulli%% link %% (cioè $\displaystyle\lim_{x \to x_0} f(x) = \lim_{x \to x_0} g(x) = 0$),
> 2. esiste un [intorno](Topologia%20dei%20reali.md#^definizione-intorno-di-un-punto) $I(x_0)$ di $x_0$ tale che $f$ e $g$ siano [derivabili](content/Matematica/Analisi%20matematica/Derivate/_index.md#^definizione-derivabilita-di-una-funzione-in-un-sottoinsieme-del-dominio) in ogni $x \in A \cap I(x_0)$ (con $x \ne x_0$) e che per tali $x$ si ha $g'(x) \ne 0$ e
> 3. esiste il [limite](content/Matematica/Analisi%20matematica/Limiti/_index.md#^definizione-limite) $\displaystyle\lim_{x \to x_0} \dfrac{f'(x)}{g'(x)} = l \in \mathbb{R} \cup \{ \pm \infty \}$,
> 
> allora
> 
> $$
> \lim_{x \to x_0} \dfrac{f(x)}{g(x)} = l
> $$
^teorema-di-de-l-hopital-della-forma-indeterminata-del-tipo-0-su-0

> [!teorema] Teorema di De l'Hôpital della forma indeterminata del tipo $\dfrac{\infty}{\infty}$
> 
> Dato un intervallo%% link %% $A \subseteq \mathbb{R}$, due [funzioni](content/Matematica/Teoria%20degli%20insiemi/Funzioni/_index.md#^definizione-funzione) $f,g \colon A \to \mathbb{R}$, e un [punto di accumulazione](Topologia%20dei%20reali.md#^definizione-punto-di-accumulazione) $x_0 \in \mathbb{R} \cup \{ \pm \infty \}$ per $A$, se:
> 1. i [limiti](content/Matematica/Analisi%20matematica/Limiti/_index.md#^definizione-limite) di $f$ e $g$ per $x \to x_0$ sono infiniti%% link %% (cioè $\displaystyle\lim_{x \to x_0} f(x) = \pm \infty$ e $\displaystyle\lim_{x \to x_0} g(x) = \pm \infty$),
> 2. esiste un [intorno](Topologia%20dei%20reali.md#^definizione-intorno-di-un-punto) $I(x_0)$ di $x_0$ tale che $f$ e $g$ siano [derivabili](content/Matematica/Analisi%20matematica/Derivate/_index.md#^definizione-derivabilita-di-una-funzione-in-un-sottoinsieme-del-dominio) in ogni $x \in A \cap I(x_0)$ (con $x \ne x_0$) e che per tali $x$ si ha $g'(x) \ne 0$ e
> 3. esiste il [limite](content/Matematica/Analisi%20matematica/Limiti/_index.md#^definizione-limite) $\displaystyle\lim_{x \to x_0} \dfrac{f'(x)}{g'(x)} = l \in \mathbb{R} \cup \{ \pm \infty \}$,
> 
> allora
> 
> $$
> \lim_{x \to x_0} \dfrac{f(x)}{g(x)} = l
> $$
^teorema-di-de-l-hopital-della-forma-indeterminata-del-tipo-infinito-su-infinito

%% 
osservazioni pag. 275 lancelotti
%%

---

> [!fonti]+ Fonti
> 
> - 📚 Sergio Lancelotti, _Lezioni di Analisi Matematica I_, Celid, 2020 (ISBN: `978-8867891979`):
> 	- Capitolo 4 - _Calcolo differenziale per funzioni di una variabile_:
> 		- 1 - _Derivata di una funzione_:
> 			- 1.1 - _Punti di non derivabilità_.
> 			- 1.2 - _Algebra delle derivate_.
> 		- 2 - _Teoremi fondamentali del calcolo differenziale_:
> 			- 2.1 - _Teorema di Fermat_.
> 			- 2.2 - _Teorema di Lagrange e sue conseguenze_.
> 			- 2.3 - _I teoremi di De l'Hôpital_.
> - 📚 Walter Dambrosio, _Analisi matematica - Fare e comprendere_, Zanichelli, 2018 (ISBN: `9788808220745`):
> 	- Parte I - _I concetti dell'analisi matematica_:
> 		- Capitolo 2 - _Introduzione al calcolo differenziale_:
> 			- 1 - _Derivata di una funzione in un punto_:
> 				- 1.1 - _Pendenza di una funzione in un punto: il concetto di "localmente dritto"_.
