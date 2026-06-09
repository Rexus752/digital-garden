---
title: Forme indeterminate
---

> [!premessa] Premessa
> 
> Ciao! Se è la prima volta che capiti su questo sito, ti consiglio di consultare la [pagina principale](index.md) di questo cosiddetto _Giardino Digitale_ per scoprire meglio cos'è e come navigarlo.
> 
> Lo stato di questa nota è al momento: 🔴 <font color="#FF7F7F">_Bozza_</font>.

---

> [!definizione] Definizione: forma indeterminata
> 
> Una **forma indeterminata** è un'espressione in cui i valori dei [limiti](content/Matematica/Analisi%20matematica/Limiti/_index.md#^definizione-limite) dipendono dalle [funzioni](content/Matematica/Teoria%20degli%20insiemi/Funzioni/_index.md) di cui è composta. Essa possono essere [_algebriche_](Forme%20indeterminate.md#^definizione-forma-indeterminata-algebrica) o [_esponenziali_](Forme%20indeterminate.md#^definizione-forma-indeterminata-esponenziale).
^definizione-forma-indeterminata

# Forme indeterminate algebriche

> [!definizione] Definizione: forma indeterminata algebrica
> 
> Una [forma indeterminata](Forme%20indeterminate.md#^definizione-forma-indeterminata) si dice **algebrica** se è data dal _contrasto_ tra infiniti%% link %% o infinitesimi%% link %% legati da un'operazione algebrica.
> 
> Le **forme indeterminate algebrica** sono del tipo [$\dfrac{0}{0}$](Forme%20indeterminate.md#^forma-indeterminata-algebrica-del-tipo-0-su-0), [$\dfrac{\infty}{\infty}$](Forme%20indeterminate.md#^definizione-forma-indeterminata-algebrica-del-tipo-infinito-su-infinito), [$\infty - \infty$](Forme%20indeterminate.md#^forma-indeterminata-algebrica-del-tipo-infinito-meno-infinito) e [$0 \cdot \infty$](Forme%20indeterminate.md#^definizione-forma-indeterminata-algebrica-del-tipo-0-per-infinito).
^definizione-forma-indeterminata-algebrica

## Tipo $\dfrac{0}{0}$

%% 
è richiesto che $f$ e $g$ abbiano lo stesso dominio $A$ o possono avere domini generici $\text{dom}(f)$ e $\text{dom}(g)$?
%%

> [!definizione] Definizione: forma indeterminata algebrica del tipo $\dfrac{0}{0}$
> 
> Date due [funzioni](content/Matematica/Teoria%20degli%20insiemi/Funzioni/_index.md#^definizione-funzione) $f, g \colon A \subseteq \mathbb{R} \to \mathbb{R}$ (con $A \ne \emptyset$) e un [punto di accumulazione](Topologia%20dei%20reali.md#^definizione-punto-di-accumulazione) $x_0 \in \mathbb{R} \cup \{\pm\infty\}$ per $A$, se esiste un [intorno](Topologia%20dei%20reali.md#^definizione-intorno-di-un-punto) $I(x_0)$ di $x_0$ tale che $g(x) \ne 0$ su $(A \cap I(x_0)) \setminus \{x_0\}$, si dice che il [limite](content/Matematica/Analisi%20matematica/Limiti/_index.md#^definizione-limite)
> 
> $$\lim_{x \to x_0} \frac{f(x)}{g(x)}$$
> 
> presenta una **[forma indeterminata algebrica](Forme%20indeterminate.md#^definizione-forma-indeterminata-algebrica) del tipo $\dfrac{0}{0}$** se
> 
> $$\lim_{x \to x_0} f(x) = 0 \quad \land \quad \lim_{x \to x_0} g(x) = 0$$
> 
> Il [limite](content/Matematica/Analisi%20matematica/Limiti/_index.md#^definizione-limite) non ha un valore%% link %% $l \in \mathbb{R} \cup \{\pm\infty\}$ determinabile dalla sola conoscenza dei [limiti](content/Matematica/Analisi%20matematica/Limiti/_index.md#^definizione-limite) di $f$ e $g$, poiché il risultato dipende dal comportamento specifico delle due [funzioni](content/Matematica/Teoria%20degli%20insiemi/Funzioni/_index.md#^definizione-funzione) su $(A \cap I(x_0)) \setminus \{x_0\}$.
^forma-indeterminata-algebrica-del-tipo-0-su-0

%% osservazione: perché è una forma indeterminata? %%

%% 
Sostituire

$\mathbb{R} \cup \{ \pm \infty \}$

con

$\overline{\mathbb{R}}$ (R esteso)
%%

## Tipo $\dfrac{\infty}{\infty}$

> [!definizione] Definizione: forma indeterminata algebrica del tipo $\dfrac{\infty}{\infty}$
> 
> Date due [funzioni](content/Matematica/Teoria%20degli%20insiemi/Funzioni/_index.md#^definizione-funzione) $f, g \colon A \subseteq \mathbb{R} \to \mathbb{R}$ (con $A \ne \emptyset$) e un [punto di accumulazione](Topologia%20dei%20reali.md#^definizione-punto-di-accumulazione) $x_0 \in \mathbb{R} \cup \{\pm\infty\}$ per $A$, se esiste un [intorno](Topologia%20dei%20reali.md#^definizione-intorno-di-un-punto) $I(x_0)$ di $x_0$ tale che $g(x) \ne 0$ su $(A \cap I(x_0)) \setminus \{x_0\}$, si dice che il [limite](content/Matematica/Analisi%20matematica/Limiti/_index.md#^definizione-limite)
> 
> $$\lim_{x \to x_0} \frac{f(x)}{g(x)}$$
> 
> presenta una **[forma indeterminata algebrica](Forme%20indeterminate.md#^definizione-forma-indeterminata-algebrica) del tipo $\dfrac{\infty}{\infty}$** se
> 
> $$\lim_{x \to x_0} f(x) = \pm\infty \quad \land \quad \lim_{x \to x_0} g(x) = \pm\infty$$
> 
> Il [limite](content/Matematica/Analisi%20matematica/Limiti/_index.md#^definizione-limite) non ha un valore%% link %% $l \in \mathbb{R} \cup \{\pm\infty\}$ determinabile dalla sola conoscenza dei [limiti](content/Matematica/Analisi%20matematica/Limiti/_index.md#^definizione-limite) di $f$ e $g$, poiché il risultato dipende dal comportamento specifico delle due [funzioni](content/Matematica/Teoria%20degli%20insiemi/Funzioni/_index.md#^definizione-funzione) su $(A \cap I(x_0)) \setminus \{x_0\}$.
^definizione-forma-indeterminata-algebrica-del-tipo-infinito-su-infinito

%% osservazione: perché è una forma indeterminata? %%

%% 
Una sola osservazione: la condizione $g(x) \ne 0$ su $(A \cap I(x_0)) \setminus {x_0}$ è in questo caso meno restrittiva da richiedere esplicitamente, poiché se $\lim_{x \to x_0} g(x) = \pm\infty$ allora $g(x) \ne 0$ in un intorno forato di $x_0$ è automaticamente garantito per la permanenza del segno. Puoi scegliere se mantenerla per uniformità con la definizione di $\dfrac{0}{0}$, oppure ometterla citando quel teorema.
%%

## Tipo $\infty - \infty$

> [!definizione] Definizione: forma indeterminata algebrica del tipo $\infty-\infty$
> 
> Date due [funzioni](content/Matematica/Teoria%20degli%20insiemi/Funzioni/_index.md#^definizione-funzione) $f, g \colon A \subseteq \mathbb{R} \to \mathbb{R}$ (con $A \ne \emptyset$) e un [punto di accumulazione](Topologia%20dei%20reali.md#^definizione-punto-di-accumulazione) $x_0 \in \mathbb{R} \cup \{\pm\infty\}$ per $A$, si dice che il [limite](content/Matematica/Analisi%20matematica/Limiti/_index.md#^definizione-limite)
> 
> $$\lim_{x \to x_0} \big( f(x)-g(x) \big) $$
> 
> presenta una **[forma indeterminata algebrica](Forme%20indeterminate.md#^definizione-forma-indeterminata-algebrica) del tipo $\infty - \infty$** se
> 
> $$\lim_{x \to x_0} f(x) = \pm\infty \quad \land \quad \lim_{x \to x_0} g(x) = \pm\infty$$
> 
> Il [limite](content/Matematica/Analisi%20matematica/Limiti/_index.md#^definizione-limite) non ha un valore%% link %% $l \in \mathbb{R} \cup \{\pm\infty\}$ determinabile dalla sola conoscenza dei [limiti](content/Matematica/Analisi%20matematica/Limiti/_index.md#^definizione-limite) di $f$ e $g$, poiché il risultato dipende dal comportamento specifico delle due [funzioni](content/Matematica/Teoria%20degli%20insiemi/Funzioni/_index.md#^definizione-funzione) su $(A \cap I(x_0)) \setminus \{x_0\}$.
^forma-indeterminata-algebrica-del-tipo-infinito-meno-infinito

%% osservazione: perché è una forma indeterminata? %%

%%
Un'osservazione: rispetto alle forme frazionarie, qui non compare alcuna condizione aggiuntiva di buona definizione (come $g(x) \ne 0$), poiché la differenza $f(x) - g(x)$ è definita su tutto $A$ senza restrizioni. La definizione è quindi leggermente più semplice nella sua ipotesi.
%%

## Tipo $0 \cdot \infty$

> [!definizione] Definizione: forma indeterminata algebrica del tipo $0 \cdot \infty$
> 
> Date due [funzioni](content/Matematica/Teoria%20degli%20insiemi/Funzioni/_index.md#^definizione-funzione) $f, g \colon A \subseteq \mathbb{R} \to \mathbb{R}$ (con $A \ne \emptyset$) e un [punto di accumulazione](Topologia%20dei%20reali.md#^definizione-punto-di-accumulazione) $x_0 \in \mathbb{R} \cup \{\pm\infty\}$ per $A$, si dice che il [limite](content/Matematica/Analisi%20matematica/Limiti/_index.md#^definizione-limite)
> 
> $$\lim_{x \to x_0} \big( f(x) \cdot g(x) \big)$$
> 
> presenta una **[forma indeterminata algebrica](Forme%20indeterminate.md#^definizione-forma-indeterminata-algebrica) del tipo $0 \cdot \infty$** se
> 
> $$\lim_{x \to x_0} f(x) = 0 \quad \land \quad \lim_{x \to x_0} g(x) = \pm\infty$$
> 
> Il [limite](content/Matematica/Analisi%20matematica/Limiti/_index.md#^definizione-limite) non ha un valore%% link %% $l \in \mathbb{R} \cup \{\pm\infty\}$ determinabile dalla sola conoscenza dei [limiti](content/Matematica/Analisi%20matematica/Limiti/_index.md#^definizione-limite) di $f$ e $g$, poiché il risultato dipende dal comportamento specifico delle due [funzioni](content/Matematica/Teoria%20degli%20insiemi/Funzioni/_index.md#^definizione-funzione) su $(A \cap I(x_0)) \setminus \{x_0\}$.
^definizione-forma-indeterminata-algebrica-del-tipo-0-per-infinito

%% osservazione: perché è una forma indeterminata? %%

%%
Un'osservazione: come per $\infty - \infty$, il prodotto $f(x) \cdot g(x)$ è definito su tutto $A$ senza restrizioni aggiuntive, quindi non occorre alcuna ipotesi di buona definizione. La forma è simmetrica — si potrebbe equivalentemente scrivere $\lim f = \pm\infty$ e $\lim g = 0$, ma per convenzione si indica sempre prima il fattore infinitesimo.
%%

# Forme indeterminate esponenziali

> [!definizione] Definizione: forma indeterminata esponenziale
> 
> Una [forma indeterminata](Forme%20indeterminate.md#^definizione-forma-indeterminata) si dice **esponenziale** se è data dal _contrasto_ tra basi ed esponenti i cui [limiti](content/Matematica/Analisi%20matematica/Limiti/_index.md#^definizione-limite) tendono a valori critici che generano un conflitto di tendenze.
> 
> Le **forme indeterminate esponenziali** sono del tipo [$1^\infty$](Forme%20indeterminate.md#^definizione-forma-indeterminata-espnenziale-del-tipo-1-all-infinito), [$\infty^0$](Forme%20indeterminate.md#^definizione-forma-indeterminata-esponenziale-del-tipo-infinito-allo-zero) e [$0^0$](Forme%20indeterminate.md#^definizione-forma-indeterminata-esponenziale-del-tipo-0-alla-0).
^definizione-forma-indeterminata-esponenziale

## Tipo $1^\infty$

> [!definizione] Definizione: forma indeterminata esponenziale del tipo $1^\infty$
> 
> Date due [funzioni](content/Matematica/Teoria%20degli%20insiemi/Funzioni/_index.md#^definizione-funzione) $f, g \colon A \subseteq \mathbb{R} \to \mathbb{R}$ (con $A \ne \emptyset$) e un [punto di accumulazione](Topologia%20dei%20reali.md#^definizione-punto-di-accumulazione) $x_0 \in \mathbb{R} \cup \{\pm\infty\}$ per $A$, si dice che il [limite](content/Matematica/Analisi%20matematica/Limiti/_index.md#^definizione-limite)
> 
> $$\lim_{x \to x_0} \big( f(x)^{g(x)} \big)$$
> 
> presenta una **[forma indeterminata esponenziale](Forme%20indeterminate.md#^definizione-forma-indeterminata-esponenziale) del tipo $1^\infty$** se
> 
> $$\lim_{x \to x_0} f(x) = 1 \quad \land \quad \lim_{x \to x_0} g(x) = \pm\infty$$
> 
> Il [limite](content/Matematica/Analisi%20matematica/Limiti/_index.md#^definizione-limite) non ha un valore%% link %% $l \in \mathbb{R} \cup \{\pm\infty\}$ determinabile dalla sola conoscenza dei [limiti](content/Matematica/Analisi%20matematica/Limiti/_index.md#^definizione-limite) di $f$ e $g$, poiché il risultato dipende dal comportamento specifico delle due [funzioni](content/Matematica/Teoria%20degli%20insiemi/Funzioni/_index.md#^definizione-funzione) su $(A \cap I(x_0)) \setminus \{x_0\}$.
^definizione-forma-indeterminata-espnenziale-del-tipo-1-all-infinito

%% osservazione: perché è una forma indeterminata? %%

> [!osservazione] Osservazione: condizioni di esistenza della base di $1^\infty$ e di $\infty^0$
> 
> Di solito, per l'esistenza stessa della funzione potenza%% link %% $f(x)^{g(x)}$ nel campo reale%% link %%, si richiede implicitamente che $f(x) > 0$ in un [intorno](Topologia%20dei%20reali.md#^definizione-intorno-di-un-punto) di $x_0$.
> 
> Nel caso delle [forme indeterminate esponenziali](Forme%20indeterminate.md#^definizione-forma-indeterminata-esponenziale) del tipo [$1^\infty$](Forme%20indeterminate.md#^definizione-forma-indeterminata-espnenziale-del-tipo-1-all-infinito) e [$\infty^0$](Forme%20indeterminate.md#^definizione-forma-indeterminata-esponenziale-del-tipo-infinito-allo-zero), poiché il [limite](content/Matematica/Analisi%20matematica/Limiti/_index.md#^definizione-limite) di $f(x)$ è rispettivamente $1$ e $+\infty$, il [teorema della permanenza del segno](Proprietà%20locali%20delle%20funzioni%20continue.md#^teorema-della-permanenza-del-segno) e il suo [corollario](Proprietà%20locali%20delle%20funzioni%20continue.md#^corollario-del-teorema-della-permanenza-del-segno) ci garantiscono matematicamente che $f(x) > 0$ per tutte le $x$ abbastanza vicine a $x_0$. In questi casi, quindi, non c'è bisogno di specificare questa condizione nelle ipotesi iniziali.
^osservazione-condizioni-di-esistenza-della-base-di-1-all-infinito-e-infinito-allo-zero

## Tipo $\infty^0$

> [!definizione] Definizione: forma indeterminata esponenziale del tipo $\infty^0$
> 
> Date due [funzioni](content/Matematica/Teoria%20degli%20insiemi/Funzioni/_index.md#^definizione-funzione) $f, g \colon A \subseteq \mathbb{R} \to \mathbb{R}$ (con $A \ne \emptyset$) e un [punto di accumulazione](Topologia%20dei%20reali.md#^definizione-punto-di-accumulazione) $x_0 \in \mathbb{R} \cup \{\pm\infty\}$ per $A$, si dice che il [limite](content/Matematica/Analisi%20matematica/Limiti/_index.md#^definizione-limite)
> 
> $$\lim_{x \to x_0} \big( f(x) \big)^{g(x)}$$
> 
> presenta una **[forma indeterminata esponenziale](Forme%20indeterminate.md#^definizione-forma-indeterminata-esponenziale) del tipo $\infty^0$** se
> 
> $$\lim_{x \to x_0} f(x) = +\infty \quad \land \quad \lim_{x \to x_0} g(x) = 0$$
> 
> Il [limite](content/Matematica/Analisi%20matematica/Limiti/_index.md#^definizione-limite) non ha un valore%% link %% $l \in \mathbb{R} \cup \{\pm\infty\}$ determinabile dalla sola conoscenza dei [limiti](content/Matematica/Analisi%20matematica/Limiti/_index.md#^definizione-limite) di $f$ e $g$, poiché il risultato dipende dal comportamento specifico delle due [funzioni](content/Matematica/Teoria%20degli%20insiemi/Funzioni/_index.md#^definizione-funzione) su $(A \cap I(x_0)) \setminus \{x_0\}$.
^definizione-forma-indeterminata-esponenziale-del-tipo-infinito-allo-zero

%% osservazione: perché è una forma indeterminata? %%

## Tipo $0^0$

> [!definizione] Definizione: forma indeterminata esponenziale del tipo $0^0$
> 
> Date due [funzioni](content/Matematica/Teoria%20degli%20insiemi/Funzioni/_index.md#^definizione-funzione) $f, g \colon A \subseteq \mathbb{R} \to \mathbb{R}$ (con $A \ne \emptyset$) e un [punto di accumulazione](Topologia%20dei%20reali.md#^definizione-punto-di-accumulazione) $x_0 \in \mathbb{R} \cup \{\pm\infty\}$ per $A$, si dice che il [limite](content/Matematica/Analisi%20matematica/Limiti/_index.md#^definizione-limite)
> 
> $$\lim_{x \to x_0} \big( f(x) \big)^{g(x)}$$
> 
> presenta una **[forma indeterminata esponenziale](Forme%20indeterminate.md#^definizione-forma-indeterminata-esponenziale) del tipo $0^0$** se
> 
> $$\lim_{x \to x_0} f(x) = 0^+ \quad \land \quad \lim_{x \to x_0} g(x) = 0$$
> 
> Il [limite](content/Matematica/Analisi%20matematica/Limiti/_index.md#^definizione-limite) non ha un valore%% Link %% $l \in \mathbb{R} \cup \{\pm\infty\}$ determinabile dalla sola conoscenza dei [limiti](content/Matematica/Analisi%20matematica/Limiti/_index.md#^definizione-limite) di $f$ e $g$, poiché il risultato dipende dal comportamento specifico delle due [funzioni](content/Matematica/Teoria%20degli%20insiemi/Funzioni/_index.md#^definizione-funzione) su $(A \cap I(x_0)) \setminus \{x_0\}$.
^definizione-forma-indeterminata-esponenziale-del-tipo-0-alla-0

%% osservazione: perché è una forma indeterminata? %%

> [!osservazione] Osservazione: condizioni di esistenza della base di $0^0$
> 
> A differenza di [quanto avviene per le forme indeterminate esponenziali del tipo $1^\infty$ e $\infty^0$](Forme%20indeterminate.md#^osservazione-condizioni-di-esistenza-della-base-di-1-all-infinito-e-infinito-allo-zero), nel caso della [forma indeterminata esponenziale del tipo $0^0$](Forme%20indeterminate.md#^definizione-forma-indeterminata-esponenziale-del-tipo-0-alla-0), poiché il [limite](content/Matematica/Analisi%20matematica/Limiti/_index.md#^definizione-limite) della base%% link %% è $0$, il [teorema della permanenza del segno](Proprietà%20locali%20delle%20funzioni%20continue.md#^teorema-della-permanenza-del-segno) non è applicabile e non assicura che $f(x)$ sia positiva%% link %%. Pertanto, per questa specifica forma, è strettamente necessario imporre per ipotesi che $f(x) > 0$ in un [intorno](Topologia%20dei%20reali.md#^definizione-intorno-di-un-punto) di $x_0$, oppure scrivere esplicitamente che $\displaystyle\lim_{x \to x_0} f(x) = 0^+$ (cioè come abbiamo fatto noi nella definizione).

# Limiti con forme indeterminate

## Limiti all'infinito di un polinomio

> [!teorema] Teorema dei limiti all'infinito di un polinomio
> 
> Dato un polinomio%% link %% $P(x) = a_nx^n + a_{n-1}x^{n-1} + \ldots + a_1x + a_0$ di grado $n \in \mathbb{N}^{\ge 1}$, allora
> 
> $$
> \begin{array}{}
> \displaystyle\lim_{x\to + \infty} P(x) = \begin{cases}
> + \infty & \text{se } a_n > 0 \\
> - \infty & \text{se } a_n < 0
> \end{cases} \\
> \displaystyle\lim_{x \to - \infty} P(x) = \begin{cases}
> + \infty & \text{se } a_n>0 \land n \text{ è pari} \\
> - \infty & \text{se } a_n>0 \land n \text{ è dispari} \\
> - \infty & \text{se } a_n<0 \land n \text{ è pari} \\
> + \infty & \text{se } a_n<0 \land n \text{ è dispari} \\
> \end{cases}
> \end{array}
> $$
> 
> Questi [limiti](content/Matematica/Analisi%20matematica/Limiti/_index.md#^definizione-limite) presentano [forme indeterminate algebriche del tipo $\infty - \infty$](Forme%20indeterminate.md#^forma-indeterminata-algebrica-del-tipo-infinito-meno-infinito).
^teorema-dei-limiti-all-infinito-di-un-polinomio

%% 
dimostrazione pagg. 164-165
%%

> [!trucco] Trucco: è sufficiente osservare il termine di grado massimo
> 
> Osservando il [teorema](content/Matematica/Analisi%20matematica/Limiti/_index.md#^teorema-dei-limiti-all-infinito-di-un-polinomio) si può evincere che i [limiti](content/Matematica/Analisi%20matematica/Limiti/_index.md#^definizione-limite) all'infinito di un polinomio dipendono esclusivamente dal termine di grado massimo e sono $+ \infty$ o $- \infty$, quindi è sufficiente solo determinare a cosa tende il termine di grado massimo.

%% 
esempi pag. 165 lancelotti
%%

## Limiti all'infinito di una funzione razionale fratta

> [!teorema] Teorema dei limiti all'infinito di una funzione razionale fratta
> 
> Dati due polinomi%% link %% $P(x) = a_nx^n + a_{n-1}x^{n-1} + \ldots + a_1x + a_0$ e $Q(x) = b_mx^m + b_{m-1}x^{m-1} + \ldots + b_1x + b_0$ di grado rispettivamente $n \in \mathbb{N}$ e $m \in \mathbb{N}^{\ge 1}$, allora
> 
> $$
> \begin{array}{}
> \displaystyle\lim_{x \to + \infty} \dfrac{P(x)}{Q(x)} = \begin{cases}
> +\infty & \text{se } n > m \land \dfrac{a_n}{b_m} > 0 \\
> -\infty & \text{se } n > m \land \dfrac{a_n}{b_m} < 0 \\
> \dfrac{a_n}{b_m} & \text{se } n = m \\
> 0 & \text{se } n < m
> \end{cases} \\
> \displaystyle\lim_{x \to - \infty} \dfrac{P(x)}{Q(x)} = \begin{cases}
> +\infty & \text{se } n > m \land n - m \text{ è pari } \land \dfrac{a_n}{b_m} > 0 \\
> -\infty & \text{se } n > m \land n - m \text{ è dispari } \land \dfrac{a_n}{b_m} > 0 \\
> -\infty & \text{se } n > m \land n - m \text{ è pari } \land \dfrac{a_n}{b_m} < 0 \\
> +\infty & \text{se } n > m \land n - m \text{ è dispari } \land \dfrac{a_n}{b_m} < 0 \\
> \dfrac{a_n}{b_m} & \text{se } n = m \\
> 0 & \text{se } n < m
> \end{cases}
> \end{array}
> $$
> 
> Questi [limiti](content/Matematica/Analisi%20matematica/Limiti/_index.md#^definizione-limite) presentano [forme indeterminate algebriche del tipo $\dfrac{\infty}{\infty}$](Forme%20indeterminate.md#^definizione-forma-indeterminata-algebrica-del-tipo-infinito-su-infinito).
^teorema-dei-limiti-all-infinito-di-una-funzione-razionale-fratta

%% 
Dimostrazione pag. 166 lancelotti
%%

> [!trucco] Trucco per i limiti all'infinito di una funzione razionale fratta
> 
> Osservando il [teorema](content/Matematica/Analisi%20matematica/Limiti/_index.md#^teorema-dei-limiti-all-infinito-di-una-funzione-razionale-fratta) si può evincere che i [limiti](content/Matematica/Analisi%20matematica/Limiti/_index.md#^definizione-limite) all'infinito di una funzione razionale fratta%% link %% dipendono esclusivamente dal termine di grado massimo di numeratore e denominatore. In particolare:
> - $\text{grado num.} > \text{grado den.} \implies \text{limite} = \pm \infty$,
> - $\text{grado num.} < \text{grado den.} \implies \text{limite} = 0$ e
> - $\text{grado num.} = \text{grado den.} \implies \text{limite = quoziente termini di grado massimo}$.

%% 
esempi pag. 167
%%

## Limiti in un punto finito di una funzione razionale fratta

> [!teorema] Teorema dei limiti in un punto finito di una funzione razionale fratta
> 
> Dati un punto%% Link %% $x_0 \in \mathbb{R}$ e due polinomi%% Link %% $P(x) = (x - x_0)^n R(x)$ e $Q(x)=(x-x_0)^m S(x)$ con $n,m \in \mathbb{N}^{\ge 1}$ e $R(x),S(x)$ due polinomi%% link %% tali che $R(x_0), S(x_0) \ne 0$, allora
> 
> $$
> \lim_{x \to x_0} \dfrac{P(x)}{Q(x)} = \lim_{x \to x_0} \dfrac{(x-x_0)^n R(x)}{(x-x_0)^m S(x)} = \begin{cases}
> 0 & \text{se } n > m \\
> \dfrac{R(x_0)}{S(x_0)} & \text{se } n = m \\
> +\infty & \text{se } n < m \land m - n \text{ è pari } \land \dfrac{R(x_0)}{S(x_0)} > 0 \\
> -\infty & \text{se } n < m \land m - n \text{ è pari } \land \dfrac{R(x_0)}{S(x_0)} < 0 \\
> \not\exists & \text{se } n < m \land m-n \text{ è dispari} 
> \end{cases}
> $$
> 
> Questo [limite](content/Matematica/Analisi%20matematica/Limiti/_index.md#^definizione-limite) presenta una [forma indeterminata algebrica del tipo $\dfrac{0}{0}$](Forme%20indeterminate.md#^forma-indeterminata-algebrica-del-tipo-0-su-0).

%% 
dimostrazione pagg. 167-168 lancelotti
%%

%% 
esempio pag. 169 lancelotti
%%

---

> [!fonti]+ Fonti
> 
> - 📚 _Lezioni di Analisi Matematica I_ di Sergio Lancelotti, Celid, 2020 (ISBN: `978-8867891979`):
> 	- Capitolo 3 - _Limiti e continuità_:
> 		- 3 - _Teoremi su limiti e continuità_:
> 			- 3.4 - _Forme indeterminate di tipo algebrico_.
> 			- 3.8 - _Limiti notevoli_.
