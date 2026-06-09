---
title: Funzioni elementari
---

> [!premessa]+ Premessa
> 
> Ciao! Se è la prima volta che capiti su questo sito, ti consiglio di consultare la [pagina principale](index.md) di questo cosiddetto _Giardino Digitale_ per scoprire meglio cos'è e come navigarlo.
> 
> Lo stato di questa nota è al momento: 🔴 <font color="#FF7F7F">_Bozza_</font>.

---

# 1 - Funzioni lineari

> [!definizione]+ Definizione: funzione lineare
> 
> Una **funzione lineare** è una [funzione](Matematica/Teoria%20degli%20insiemi/Funzioni/_index.md#^definizione-funzione) del tipo
> 
> $$
> f(x) = mx + q
> $$
> 
> con $m, q \in \mathbb{R}$.
^definizione-funzione-lineare

Il grafico di una [funzione lineare](Funzioni%20elementari.md#^definizione-funzione-lineare) è la retta di equazione

$$
y = mx + q
$$

Analizziamo il comportamento di $f$ al variare di $m$:

|           | Dominio      | Immagine     | Monotonia                       | Comportamento asintotico al'infinito                      |
| --------- | ------------ | ------------ | ------------------------------- | --------------------------------------------------------- |
| $m > 0$   | $\mathbb{R}$ | $\mathbb{R}$ | $f$ crescente su $\mathbb{R}$   | $\displaystyle \lim_{x \to \pm \infty} f(x) = \pm \infty$ |
| $m < 0$   | $\mathbb{R}$ | $\mathbb{R}$ | $f$ decrescente su $\mathbb{R}$ | $\displaystyle \lim_{x \to \pm \infty} f(x) = \mp \infty$ |
| $m =<= 0$ | $\mathbb{R}$ | $\{ q \}$    | $f$ costante su $\mathbb{R}$    | $\displaystyle \lim_{x \to \pm \infty} f(x) = q$          |

%% inserire grafici per mostrarlo %%

Si può quindi evincere che il coefficiente $m$ assume due significati fondamentali:
- È la pendenza della retta $y = mx + q$: per ogni coppia di punti $x_1 \ne x_2$ abbiamo:
	$$
	\dfrac{\Delta f}{\Delta x} = \dfrac{f(x_2) - f(x_1)}{x_2 - x_1} = m
	$$
- È il tasso medio di variazione di $f$ in ogni intervallo.

> [!esempio]- Esempio: funzione lineare passante per un punto assegnato e con pendenza assegnata
> 
> Determiniamo l'unica funzione lineare $f$ di pendenza $m_0 \in \mathbb{R}$ assegnata e il cui grafico passa per un punto $(x_0, y_0)$ assegnato.
> 
> Dato un generico punto $(x, f(x))$ sulla retta grafico di $f$, in accordo con la relazione della pendenza della retta abbiamo
> 
> $$
> \dfrac{\Delta f}{\Delta x} = \dfrac{f(x) - f(x_0)}{x - x_0} = m_0
> $$
> 
> Da cui si ricava la relazione
> 
> $$
> f(x) - y_0 = m_0 (x - x_0)
> $$
> 
> e quindi
> 
> $$
> f(x) = m_0(x - x_0) + y_0
> $$
> 
> Per esempio, la funzione lineare avente pendenza $m_0 = -2$ e il cui grafico passa per $(1,4)$ è:
> 
> $$
> f(x) = -2(x - 1) + 4 = -2x + 6
> $$

[!esempio]- Esempio: funzione lineare passante per due punti assegnati

Determiniamo l'unica funzione lineare $f$ il cui grafico passa per due punti $(x_1, y_1)$ e $(x_2, y_2)$ assegnati (con $x_1 \ne x_2$). Osserviamo che la pendenza di $f$, in accordo con la relazione della pendenza della retta, abbiamo

$$
\dfrac{\Delta f}{\Delta x} = \dfrac{f(x_2) - f(x_1)}{x_2 - x_1} = \dfrac{y_2 - y_1}{x_2 - x_1} = m
$$

Applicando la formula di prima della retta passante per un dato punto ($f(x) = m_0(x - x_0) + y_0$), abbiamo

$$
\begin{align*}
f(x) &= m (x - x_1) + y_1 \\
&= \dfrac{y_2 - y_1}{x_2 - x_1} (x - x_1) + y_1
\end{align*}
$$

Per esempio, la funzione lineare il cui grafico passa per $(1,4)$ e per $(3, -2)$ è

$$
\begin{align*}
f(x) &= \dfrac{-2 - 4}{3 - 1}(x - 1) + 4 \\
&= -3(x - 1) + 4 \\
&= -3x + 3 + 4 \\
&= -3x + 7
\end{align*}
$$

# 2 - Funzioni potenza

> [!definizione]+ Definizione: funzione potenza
> 
> Una **funzione potenza** è una [funzione](Matematica/Teoria%20degli%20insiemi/Funzioni/_index.md#^definizione-funzione) del tipo
> 
> $$
> f(x) = x^n
> $$
> 
> con $n \in \mathbb{R}$.
^definizione-funzione-potenza

Il comportamento delle funzioni potenza dipende dall'esponente $n$:

|                   | $f(x) = x^n$ con $n > 0$ pari                                    | $f(x) = x^n$ con $n > 0$ dispari                         |
| :---------------: | ---------------------------------------------------------------- | -------------------------------------------------------- |
|    **Dominio**    | $\mathbb{R}$                                                     | $\mathbb{R}$                                             |
|   **Immagine**    | $[0; + \infty)$                                                  | $\mathbb{R}$                                             |
|   **Simmetrie**   | $f$ è pari                                                       | $f$ è dispari                                            |
|   **Monotonia**   | $f$ decrescente su $(-\infty; 0]$ e crescente su $[0; + \infty)$ | $f$ crescente su $\mathbb{R}$                            |
| **Comportamento** | $\displaystyle \lim_{x \to \pm \infty} f(x) = +\infty$           | $\displaystyle \lim_{x \to \pm \infty} f(x) = \pm\infty$ |

|                   | $f(x) = x^n$ con $n < 0$ pari                                    | $f(x) = x^n$ con $n < 0$ dispari                                   |
| :---------------: | ---------------------------------------------------------------- | ------------------------------------------------------------------ |
|    **Dominio**    | $\mathbb{R} \setminus \{ 0 \}$                                   | $\mathbb{R} \setminus \{ 0 \}$                                     |
|   **Immagine**    | $(0; + \infty)$                                                  | $\mathbb{R} \setminus \{ 0 \}$                                     |
|   **Simmetrie**   | $f$ è pari                                                       | $f$ è dispari                                                      |
|   **Monotonia**   | $f$ decrescente su $(-\infty; 0)$ e crescente su $(0; + \infty)$ | $f$ decrescente su $(-\infty; 0)$ e decrescente su $(0; + \infty)$ |
| **Comportamento** | $\displaystyle \lim_{x \to \pm \infty} f(x) = 0$                 | $\displaystyle \lim_{x \to \pm \infty} f(x) = 0$                   |

|                   | $f(x) = \sqrt[n]{x} = x^{\dfrac 1 n}$ con $n > 0$ pari        | $f(x) = \sqrt[n]{x} = x^{\dfrac 1 n}$ con $n > 0$ dispari  |
| :---------------: | ------------------------------------------------------------ | --------------------------------------------------------- |
|    **Dominio**    | $[0; + \infty)$                                              | $\mathbb{R}$                                              |
|   **Immagine**    | $[0; + \infty)$                                              | $\mathbb{R}$                                              |
|   **Monotonia**   | $f$ crescente su $[0; + \infty)$                             | $f$ crescente su $\mathbb{R}$                             |
| **Comportamento** | $\displaystyle \lim_{x \to + \infty} f(x) = + \infty$        | $\displaystyle \lim_{x \to \pm \infty} f(x) = \pm \infty$ |
|    **Inversa**    | $f$ è l'inversa della restrizione di $x^n$ su $[0; +\infty)$ | $f$ è l'inversa di $x^n$                                  |

# 3 - Funzioni esponenziali

> [!definizione]+ Definizione: funzione esponenziale
> 
> Una **funzione esponenziale** è una [funzione](Matematica/Teoria%20degli%20insiemi/Funzioni/_index.md#^definizione-funzione) del tipo
> 
> $$
> f(x) = a^x
> $$
> 
> con $a > 0 \land a \ne 1$.
^definizione-funzione-esponenziale

Il comportamento delle funzioni potenza dipende dalla base $a$:

|                   | $f(x) = a^x$ con $a > 1$                                                                               | $f(x) = a^x$ con $0 < a < 1$                                                                           |
| :---------------: | ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ |
|    **Dominio**    | $\mathbb{R}$                                                                                           | $\mathbb{R}$                                                                                           |
|   **Immagine**    | $(0; + \infty)$                                                                                        | $(0; + \infty)$                                                                                        |
|   **Monotonia**   | $f$ crescente su $\mathbb{R}$                                                                          | $f$ decrescente su $\mathbb{R}$                                                                        |
| **Comportamento** | $\displaystyle \lim_{x \to - \infty} f(x) = 0$ e $\displaystyle \lim_{x \to + \infty} f(x) = + \infty$ | $\displaystyle \lim_{x \to - \infty} f(x) = + \infty$ e $\displaystyle \lim_{x \to + \infty} f(x) = 0$ |

# 4 - Funzioni logaritmiche

> [!definizione]+ Definizione: funzione logaritmica
> 
> Una **funzione logaritmica** è una [funzione](Matematica/Teoria%20degli%20insiemi/Funzioni/_index.md#^definizione-funzione) del tipo
> 
> $$
> f(x) = \log_a x
> $$
> 
> con $a > 0 \land a \ne 1$.
^definizione-funzione-logaritmica

Il comportamento delle funzioni potenza dipende dalla base del logaritmo $a$:

|                   | $f(x) = \log_a x$ con $a > 1$                                                                           | $f(x) = \log_a x$ con $0 < a < 1$                                                                       |
| :---------------: | ------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------- |
|    **Dominio**    | $(0; + \infty)$                                                                                         | $(0; + \infty)$                                                                                         |
|   **Immagine**    | $\mathbb{R}$                                                                                            | $\mathbb{R}$                                                                                            |
|   **Monotonia**   | $f$ crescente su $(0; + \infty)$                                                                        | $f$ decrescente su $(0; + \infty)$                                                                      |
| **Comportamento** | $\displaystyle \lim_{x \to 0^+} f(x) = -\infty$ e $\displaystyle \lim_{x \to + \infty} f(x) = + \infty$ | $\displaystyle \lim_{x \to 0^+} f(x) = +\infty$ e $\displaystyle \lim_{x \to + \infty} f(x) = - \infty$ |
|    **Inversa**    | $f$ è l'inversa di $a^x$                                                                                | $f$ è l'inversa di $a^x$                                                                                |

# 5 - Funzioni goniometriche

> [!definizione]+ Definizione: funzione goniometrica
> 
> Una **funzione goniometrica** è una [funzione](Matematica/Teoria%20degli%20insiemi/Funzioni/_index.md#^definizione-funzione) del tipo
> 
> $$
> f(x) = \sin x
> $$
> 
> o
> 
> $$
> f(x) = \cos x
> $$
> 
> o
> 
> $$
> f(x) = \tan x
> $$
^definizione-funzione-goniometrica

|                 | $f(x) = \sin x$                 | $f(x) = \cos x$                 | $f(x) = \tan x$                                                                                             |
| :-------------: | ------------------------------- | ------------------------------- | ----------------------------------------------------------------------------------------------------------- |
|   **Dominio**   | $\mathbb{R}$                    | $\mathbb{R}$                    | $\left\{ x \in \mathbb{R} \mid \forall k \in \mathbb{Z} \left( x \ne \dfrac{\pi}{2} + k\pi \right) \right\}$ |
|  **Immagine**   | $[-1; +1]$                      | $[-1; +1]$                      | $\mathbb{R}$                                                                                                |
| **Periodicità** | $f$ periodica di periodo $2\pi$ | $f$ periodica di periodo $2\pi$ | $f$ periodica di periodo $\pi$                                                                              |
|  **Simmetrie**  | $f$ dispari                     | $f$ pari                        | $f$ dispari                                                                                                 |
|  **Monotonia**  |                                 |                                 | $f$ crescente su $\left( - \dfrac{\pi}{2} + k \pi; + \dfrac{\pi}{2} + k \pi \right)$                          |

## 5.1 - Funzioni goniometriche inverse

|               | $f(x) = \arcsin x$                                                                                | $f(x) = \arctan x$                                                                                |
| ------------- | ------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------- |
| **Dominio**   | $[-1; +1]$                                                                                        | $\mathbb{R}$                                                                                      |
| **Immagine**  | $\left[ - \dfrac{\pi}{2}; + \dfrac{\pi}{2} \right]$                                                 | $\left( - \dfrac{\pi}{2}; + \dfrac{\pi}{2} \right)$                                                 |
| **Simmetrie** | $f$ dispari                                                                                       | $f$ dispari                                                                                       |
| **Monotonia** | $f$ crescente su $[-1; +1]$                                                                       | $f$ crescente su $\mathbb{R}$                                                                     |
| **Inversa**   | $f$ è l'inversa della restrizione di $\sin x$ a $\left[ - \dfrac{\pi}{2}; + \dfrac{\pi}{2} \right]$ | $f$ è l'inversa della restrizione di $\tan x$ a $\left( - \dfrac{\pi}{2}; + \dfrac{\pi}{2} \right)$ |

%% 
Fare da 2.4 in poi del libro di Analisi 
%%

---

> [!fonti]+ Fonti
> 
> - 📚 _Analisi matematica - Fare e comprendere_ di Walter Dambrosio, Zanichelli, 2018 (ISBN: `9788808220745`):
> 	- 1 - _Funzioni e modelli_:
> 		- 2 - _Grafici delle funzioni elementari_:
> 			- 2.1 - _Funzioni lineari e funzioni potenza_.
> 			- 2.2 - _Funzioni esponenziali e logaritmiche_.
