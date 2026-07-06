
> [!premessa]+ Premessa
> 
> Ciao! Se è la prima volta che capiti su questo sito, ti consiglio di consultare la [pagina principale](index.md) di questo cosiddetto _Giardino Digitale_ per scoprire meglio cos'è e come navigarlo.
> 
> Lo stato di questa nota è al momento: 🟢 <font color="#7FFF7F">_Completa_</font>.

---

> [!definizione]+ Definizione: variazione di $\color{#FF7FFF} x$ nel passaggio da $\color{#FF7FFF} x_1$ a $\color{#FF7FFF} x_2$
> 
> Data una [funzione](Funzioni.md#^definizione-funzione) $f \colon \text{dom}(f) \to \mathbb{R}$ e due punti%% Link %% $x_1, x_2 \in \text{dom}(f)$, chiamiamo **variazione (o incremento) di $x$ nel passaggio da $x_1$ a $x_2$** la loro differenza%% link %%, denotata con $\Delta x$:
> 
> $$
> \Delta x \overset{\text{def}}{=} x_2 - x_1
> $$
^definizione-variazione-di-x-nel-passaggio-da-x1-a-x2

> [!definizione]+ Definizione: variazione di $\color{#FF7FFF} f$ nel passaggio da $\color{#FF7FFF} x_1$ a $\color{#FF7FFF} x_2$
> 
> Data una [funzione](Funzioni.md#^definizione-funzione) $f \colon \text{dom}(f) \to \mathbb{R}$ e due punti%% Link %% $x_1, x_2 \in \text{dom}(f)$, chiamiamo **variazione (o incremento) di $f$ nel passaggio da $x_1$ a $x_2$** la differenza%% link %% delle loro immagini%% link %% $f(x_2)$ e $f(x_1)$, denotata con $\Delta f$:
> 
> $$
> \Delta f \overset{\text{def}}{=} f(x_2) - f(x_1)
> $$
^definizione-variazione-di-f-nel-passaggio-da-x1-a-x2

> [!definizione]+ Definizione: quoziente di Newton
> 
> Data una [funzione](Funzioni.md#^definizione-funzione) $f \colon \text{dom}(f) \to \mathbb{R}$ e due punti distinti%% Link %% $x_1, x_2 \in \text{dom}(f)$, diciamo che il **quoziente di Newton di $f$ tra $x_1$ e $x_2$** (o **tasso medio di variazione di $f$ nel passaggio da $x_1$ a $x_2$**) è il quoziente%% link %% tra la [variazione di $x$](Variazioni%20e%20quoziente%20di%20Newton.md#^definizione-variazione-di-x-nel-passaggio-da-x1-a-x2) e la [variazione di $f$](Variazioni%20e%20quoziente%20di%20Newton.md#^definizione-variazione-di-f-nel-passaggio-da-x1-a-x2):
> 
> $$
> \dfrac{\Delta f}{\Delta x} = \dfrac{f(x_2) - f(x_1)}{x_2 - x_1}
> $$
^definizione-quoziente-di-newton

%% 
spiegare nella definizione perché si chiama Quoziente di Newton
%%

> [!esempio]- Esempio: variazioni e quoziente di Newton
>
> Consideriamo la [funzione](Funzioni.md#^definizione-funzione) $f(x) = x^2$ e i punti%% Link %% $x_1 = 2$ e $x_2 = 5$.
> 
> La [variazione di $x$ nel passaggio da $x_1$ a $x_2$](Variazioni%20e%20quoziente%20di%20Newton.md#^definizione-variazione-di-x-nel-passaggio-da-x1-a-x2) è:
> 
> $$
> \begin{align*}
> \Delta x &= x_2 - x_1 \\
> &= 5 - 2 \\
> &= 3
> \end{align*}
> $$
>
> La [variazione di $f$ nel passaggio da $x_1$ a $x_2$](Variazioni%20e%20quoziente%20di%20Newton.md#^definizione-variazione-di-f-nel-passaggio-da-x1-a-x2) è:
>
> $$
> \begin{align*}
> \Delta f &= f(x_2) - f(x_1) \\
> &= f(5) - f(2) \\
> &= 25 - 4 \\
> &= 21
> \end{align*}
> $$
> 
> Il [quoziente di Newton](Variazioni%20e%20quoziente%20di%20Newton.md#^definizione-quoziente-di-newton) è:
> 
> $$
> \begin{align*}
> \frac{\Delta f}{\Delta x} &= \frac{f(5) - f(2)}{5 - 2} \\
> &= \frac{25 - 4}{3} \\
> &= \frac{21}{3} \\
> &= 7
> \end{align*}
> $$

---

> [!fonti]+ Fonti
> 
> - 📚 Walter Dambrosio, _Analisi matematica - Fare e comprendere_, Zanichelli, 2018 (ISBN: `9788808220745`):
> 	- Parte I - _I concetti dell'analisi matematica_:
> 		- Capitolo 1 - _Funzioni e modelli_:
> 			- 1 - _Funzioni e grafici_:
> 				- 1.1 - _Funzioni e loro rappresentazioni_.
> - 📚 Sergio Lancelotti, _Lezioni di Analisi Matematica I_, Celid, 2020 (ISBN: `978-8867891979`):
> 	- Capitolo 2 - _Funzioni_:
> 		- 1 - _Nozioni preliminari_.