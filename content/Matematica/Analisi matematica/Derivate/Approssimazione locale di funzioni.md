
> [!premessa]+ Premessa
> 
> Ciao! Se è la prima volta che capiti su questo sito, ti consiglio di consultare la [pagina principale](index.md) di questo cosiddetto _Giardino Digitale_ per scoprire meglio cos'è e come navigarlo.
> 
> Lo stato di questa nota è al momento: 🔴 <font color="#FF7F7F">_Bozza_</font>.

---

Dato un [intorno](Matematica/Teoria%20degli%20insiemi/Funzioni/Topologia%20dei%20reali.md#^definizione-intorno-di-un-punto) $I_r(c) \subseteq \mathbb{R}$ di centro $c \in \mathbb{R}$ e raggio $r \in \mathbb{R}$ e una [funzione](Matematica/Teoria%20degli%20insiemi/Funzioni/Funzioni.md#^definizione-funzione) $f \colon I_r(c) \to \mathbb{R}$ [derivabile](Matematica/Analisi%20matematica/Derivate/Derivate.md#^definizione-derivata-prima-di-una-funzione-in-un-punto) in $c$ e [continua](Matematica/Analisi%20matematica/Limiti/Funzioni%20continue.md#^definizione-funzione-continua-in-un-punto) su $I_r(c)$, allora abbiamo visto%% link %% che se $f'(c) \ne 0$ si ha che

$$
\lim_{x \to c} \dfrac{f(x) - f(c)}{(x-c) \cdot f'(c)} = 1
$$

ovvero che $f(x)$ è [equivalente](Matematica/Analisi%20matematica/Limiti/Infiniti%20e%20infinitesimi.md#^definizione-equivalenza-asintotica) a $f(c) + f'(c) \cdot (x-c)$ per $x \to c$:

$$
f(x) \sim f(c) + f'(c) \cdot (x-c) \text{ per } x \to c
$$

Quindi $f(x)$ è approssimabile alla retta tangente%% Link %% quando $x \to c$.

> [!definizione]+ Definizione: polinomio di Taylor di ordine $\color{#FF7FFF} 1$ di $\color{#FF7FFF} f$ centrato in $\color{#FF7FFF} c$
> 
> Dato un [intorno](Matematica/Teoria%20degli%20insiemi/Funzioni/Topologia%20dei%20reali.md#^definizione-intorno-di-un-punto) $I_r(c) \subseteq \mathbb{R}$ di centro $c \in \mathbb{R}$ e raggio $r \in \mathbb{R}$ e una [funzione](Matematica/Teoria%20degli%20insiemi/Funzioni/Funzioni.md#^definizione-funzione) $f \colon I_r(c) \to \mathbb{R}$ [derivabile](Matematica/Analisi%20matematica/Derivate/Derivate.md#^definizione-derivata-prima-di-una-funzione-in-un-punto) in $c$ e [continua](Matematica/Analisi%20matematica/Limiti/Funzioni%20continue.md#^definizione-funzione-continua-in-un-punto) su $I_r(c)$, definiamo il **polinomio di Taylor di ordine $1$ di $f$ centrato in $c$** e denotiamo con $T_{1,c}(x)$ il seguente polinomio%% Link %%:
> 
> $$
> T_{1,c}(x) \overset{\text{def}}{=} f(c) + f'(c) \cdot (x-c)
> $$
^definizione-polinomio-di-taylor-di-ordine-1-di-f-centrato-in-c

%% 
chi è Taylor?
%%

> [!esempio]- Esempio di polinomio di Taylor per $\color{#7F7FFF} f(x) = e^x$
> 
> Calcoliamo il [polinomio di Taylor di ordine 1](Matematica/Analisi%20matematica/Derivate/Approssimazione%20locale%20di%20funzioni.md#^definizione-polinomio-di-taylor-di-ordine-1-di-f-centrato-in-c) della [funzione](Matematica/Teoria%20degli%20insiemi/Funzioni/Funzioni.md#^definizione-funzione) $f(x) = e^x$ centrato in $c = 0$:
> 
> $$
> \begin{align*}
> T_{1,0}(x) &= f(0) + f'(0) \cdot (x - 0) \\
> &= 1 + 1 \cdot x \\
> &= 1 + x
> \end{align*}
> $$
> 
> cioè
> 
> $$
> e^x \sim \underbrace{1 + x}_{T_{1,0}} \text{ per } x \to 0
> $$

> [!osservazione]+ Osservazione: quantificare l'errore del polinomio di Taylor
> 
> Che errore commetto prendendo il valore di $T_{1,c}(x)$ al posto di $f(x)$?
> 
> Distinguiamo in due casi:
> - In $x = c$, abbiamo che $T_{1,c}(c) = f(c)$, quindi non commetto alcun errore.
> - Quando $x \ne c$, calcolo l'errore facendo la differenza tra i due:
> 	$$
> 	E_1(x) = |f(x) - T_{1,c}(x)|
> 	$$
> 	Dato che $f$ e $T_{1,c}$ sono [continue](Matematica/Analisi%20matematica/Limiti/Funzioni%20continue.md#^definizione-funzione-continua) e anche la funzione valore assoluto%% link %% è [continua](Matematica/Analisi%20matematica/Limiti/Funzioni%20continue.md#^definizione-funzione-continua), allora anche $E_1(x)$ è [continua](Matematica/Analisi%20matematica/Limiti/Funzioni%20continue.md#^definizione-funzione-continua).
> 	Sfruttando la [definizione di _funzione continua_](Matematica/Analisi%20matematica/Limiti/Funzioni%20continue.md#^definizione-funzione-continua), abbiamo che il [limite](Matematica/Analisi%20matematica/Limiti/Limiti.md#^definizione-limite) di $E_1(c)$ per $x \to c$ ha lo stesso valore di $E_1(c)$, cioè $0$:
> 	$$
> 	\lim_{x \to c} E_1(x) = E_1(x) = 0
> 	$$
> 	Quindi, per [definizione di _limite_](Matematica/Analisi%20matematica/Limiti/Limiti.md#^definizione-limite),
> 	$$
> 	\forall \varepsilon \in \mathbb{R}, \exists \delta \in \mathbb{R}, \forall x \in \mathbb{R} . \left( 0 < |x - c| < \delta \implies E_1(x) < \varepsilon \right) 
> 	$$
> 	Quindi posso fare un errore piccolo a piacere, pur di prendere $x$ sufficientemente vicino a $c$.

%% 
questa osservazione l'avevamo già vista
%%

[!osservazione]+ Osservazione: migliorare l'approssimazione del polinomio di Taylor

%% 
Ora sappiamo che l'approssimazione possiamo "sceglierla" noi, ma
%%

Riusciamo a migliorare l'approssimazione del valore di $f(x)$ in prossimità di $x = c$ prendendo, invece di una retta, un polinomio di ordine $2$, o magari di ordine $n$?

Per capire come fare, notiamo che $T_{1,c}(x)$ ha queste caratteristiche:

$$
T_{1,c} (c) = f(c) \iff T_{1,c}'(c) = f'(c)
$$

Pare quindi naturale cercare $T_{2,c}(x)$ tale che

$$
T_{1,c}''(c) = f''(c)
$$

Ma siamo sicuri che esista un polinomio di ordine $2$ che soddisfi questa condizione? E se esiste, è unico?

Il polinomio di Taylor di $\text{II°}$ ordine che in $x = c$ vale $f(c)$ è

$$
T_{2,c}(x) = a(x-c)^2 + b(x-c) + d
$$

e possiamo notare che è simile alla forma di un polinomio di $\text{II°}$ ordine generico che è $ax^2 + bx + c$ (o, in questo caso, $ax^2 + bx + d$ per evitare la confusione col punto $c$).

In particolare:
- $T_{2,c}(c) = d$
- $T_{2,c}'(x) = 2a(x-c) + b$
- $T'_{2,c}(c) = b$ ma, dato che ci eravamo prefissati di volere $T_{1,c}'(c) = f'(c)$, allora $f'(c) = b$.
- $T''_{2,c}(x) = 2a$ ma, dato che ci eravamo prefissati di volere $T_{1,c}''(c) = f''(c)$, allora $f''(c) = 2a$

In particolare, possiamo notare che
- $d = f(c)$
- $b = f'(c)$
- $a = \dfrac{f''(c)}{2}$

e sono determinati tutti in modo univoco.

L'unico polinomio di $\text{II°}$ ordine che soddisfa le condizioni iniziali è quindi quello della prossima definizione.

> [!definizione]+ Definizione: polinomio di Taylor di $\color{#FF7FFF} \text{II°}$ ordine di una funzione in un punto
> 
> $$
> T_{2,c}(x) \overset{\text{def}}{=} f(c) + f'(c) \cdot (x-c) + \dfrac{1}{2} f''(c) \cdot (x-c)^2
> $$
^definizione-polinomio-di-taylor-di-ii-ordine-di-una-funzione-in-un-punto

Ora reiteriamo questo ragionamento per i prossimi ordini.

> [!teorema]+ Teorema del polinomio di Taylor di ordine $\color{#FF3F3F} n$ per $\color{#FF3F3F} f$ centrato in $\color{#FF3F3F} x = c$
> 
> Dato un [intorno](Matematica/Teoria%20degli%20insiemi/Funzioni/Topologia%20dei%20reali.md#^definizione-intorno-di-un-punto) $I_r(c) \subseteq \mathbb{R}$ di centro $c \in \mathbb{R}$ e raggio $r \in \mathbb{R}$ e una [funzione](Matematica/Teoria%20degli%20insiemi/Funzioni/Funzioni.md#^definizione-funzione) $f \colon I_r(c) \to \mathbb{R}$ [derivabile $n$ volte](Matematica/Analisi%20matematica/Derivate/Derivate.md#^definizione-derivata-n-esima-di-una-funzione) in $x = c$, esiste un unico polinomio di ordine $n$%% link %%, denotato con $T_{n,c}(x)$, tale che
> 
> $$
> \forall k \in \{ 0, \ldots, n \} . \left( T^{(k)}_{n,c}(c) = f^{(k)}(c) \right) 
> $$
> 
> Tale polinomio si chiama polinomio di Taylor di ordine $n$ per $f$ centrato in $x = c$ ed è
> 
> $$
> \begin{align*}
> T_{n,c}(x) &\overset{\text{def}}{=} \sum_{k = 0}^n \dfrac{f^{(k)}(c)}{k!} (x - c)^k \\
> &\overset{\text{def}}{=} f(c) + f'(c) \cdot (x - c) + \ldots + \dfrac{f^{(n)}(c)}{n!} (x - c)^n
> \end{align*}
> $$

> [!definizione]+ Definizione: polinomio di McLaurin di ordine $\color{#FF7FFF} n$
> 
> Quando $c = 0$, il polinomio di Taylor viene chiamato **polinomio di McLaurin**.

> [!esempio]- Esempi di polinomi di Taylor di $\color{#7F7FFF} f(x) = e^x$
> 
> - $f(x) = e^x$
> - $f^{(k)}(x) = e^x$ per ogni $k \ge 0$
> - $f^{(k)}(0) = 1$ per ogni $k \ge 0$
> 
> quindi
> 
> $$
> T_{n,0}(x) = \sum_{k = 0}^n \dfrac{1}{k!} x^k
> $$

> [!osservazione]+ Osservazione: quantificare l'errore del polinomio di Taylor di ordine $\color{#7F7F7F} n$
> 
> Cosa possiamo dire dell'errore commesso prendendo $T_{n,c}(x)$ al posto di $f(x)$?
> 
> Mi aspetto che $E_n(x) \le E_{n-1}(x)$ per ogni $n \ge 1$, dove
> 
> $$
> E_k(x) = |f(x) - T_{k,c}(x)|
> $$
> 
> Possiamo anche scrivere come $f(x)$ da approssimare = $T_{n,c}(x)$ + RESTO (dove $E_n(x) = |RESTO|$)
> 
> quale comportamento mi aspetto dal RESTO?
> - $\lim_{x \to c}$ RESTO = 0
> - fissato $x$, RESTO decresce al crescere di $n$
> 
> Rileggiamo quindi il teorema di Lagrange in questi termini:
> sotto opportune ipotesi su $f \colon [a,b] \to \mathbb{R}$ si ha che
> 
> $$
> \exists c \in (a,b) . \left( f'(c) = \dfrac{f(b) - f(a)}{b - a} \right) 
> $$
> 
> ovvero che
> 
> $$
> \exists c \in (a,b) . \big( f(b) = f(a) + f'(c) \cdot (b - a) \big) 
> $$
> 
> Cambiamo nome ai punti: $b$ -> $x$, $a$ -> $c$, $c$ -> $\xi$
> e leggiamo il Teorema di Lagrange:
> 
> $$
> \exists \xi \in [c,x] . \big( f(x) = f(c) + f'(\xi) \cdot (x - c) \big) 
> $$
> 
> Ma dato che $f(c) = T_{0,c}(x)$, allora RESTO = $f'(\xi) \cdot (x-c)$ è il resto di ordine 0

> [!definizione]+ Definizione: formula di Taylor con il resto di Lagrange
> 
> Data una [funzione](Matematica/Teoria%20degli%20insiemi/Funzioni/Funzioni.md#^definizione-funzione) $f \colon [a,b] \to \mathbb{R}$ [derivabile $(n+1)$ volte](Matematica/Analisi%20matematica/Derivate/Derivate.md#^definizione-derivata-n-esima-di-una-funzione), allora
> 
> $$
> \forall c,x \in (a,b), \exists \xi \in (c,x) . \left( f(x) = T_{n,c}(x) + \dfrac{f^{(n+1)}(\xi)}{(n+1)!} (x-c)^{n+1} \right) 
> $$

> [!osservazione]+ Osservazione: calcolo dell'errore commesso
> 
> Con questa scrittura esplicita del RESTO possiamo calcolare l'errore commesso, infatti
> 
> $$
> \begin{align*}
> E_n(x) &= | f(x) - T_{n,c}(x) | \\
> &= \left| \dfrac{f^{(n+1)}(\xi)}{(n+1)!} (x-c)^{n+1} \right| \\
> &= \dfrac{|f^{(n+1)}(\xi)|}{(n+1)!} |x-c|^{n+1}
> \end{align*}
> $$
> 
> Inoltre
> 
> $$
> E_n(x) \le \dfrac{M}{(n+1)!} |x-c|^{n+1}
> $$
> 
> dove
> 
> $$
> M = \max_{\xi \in [c,x]} |f^{(n+1)}(\xi)|
> $$
> 
> ammesso che $f^{(n+1)}$ sia continua (si usa il Teorema di Weierstrass).

> [!esempio]- Esempio: calcolo dell'errore dell'approssimazione di $\color{#7F7FFF} e^x$
> 
> Che errore commetto approssimando $\sqrt e$ con il polinomio di McLaurin di $e^x$ di ordine $3$? E con quello di ordine $5$? E di ordine $n$?
> 
> - Il polinomio di McLaurin è Taylor con $c = 0$
> - $\sqrt e$ si riscrive come $e^\frac{1}{2}$, quindi ci interessa il punto $x = \dfrac{1}{2}$
> - Calcoliamo con quello di ordine 3 => $n = 3$
> 
> quindi usiamo la formula dell'osservazione 
> 
> $$
> e^\frac{1}{2} - T_{3,0}\left( \dfrac{1}{2} \right) = \dfrac{f^{(4)}(\xi)}{4!} \left( \dfrac{1}{2} - 0 \right)^4
> $$
> per qualche $\xi \in \left(0, \dfrac{1}{2}\right)$.
> 
> Abbiamo che $f^{(4)}(\xi) = e^\xi$ (perché $f^{(n)}(x) = (e^x)^{(n)} = e^x$)
> 
> Dato che $e^\xi$ è continua, possiamo fare una stima dell'errore:
> 
> $$
> M = \max_{\xi \in \left[ 0, \dfrac{1}{2} \right]} e^\xi = e^\frac{1}{2}
> $$
> 
> (scegliamo $\xi = \dfrac{1}{2}$ perché $e^x$ è crescente e il valore massimo nell'intervallo $\left[ 0, \dfrac{1}{2} \right]$ sarà $f\left( \dfrac{1}{2} \right)$)
> 
> Ora vogliamo provare a stimare più o meno il valore di $e^\frac{1}{2}$ e per farlo sappiamo che $2 < e < 3$, quindi $e^\frac{1}{2} < 3^\frac{1}{2}$, quindi
> 
> $$
> \left| \sqrt e - T_{3,0}\left( \dfrac{1}{2} \right) \right| = \dfrac{f^{(4)}(\xi)}{4!} \left( \dfrac{1}{2} - 0 \right)^4 \le \dfrac{\sqrt 3}{4!} \cdot \dfrac{1}{2^4}
> $$
> 
> Se io prendo quindi $T_{3,0}\left( x \right) = 1 + x + \dfrac{1}{2}x^2 + \dfrac{1}{6}x^3$ con $x = \dfrac{1}{2}$ commetterò un errore minore di $\dfrac{\sqrt 3}{4!} \cdot \dfrac{1}{2^4}$.
> 
> Approssimiamo con $T_{5,0}\left( \dfrac{1}{2} \right)$:
> 
> $$
> e^\frac{1}{2} - T_{5,0}\left( \dfrac{1}{2} \right) = \dfrac{f^{(6)}(\xi)}{6!} \left( \dfrac{1}{2} - 0 \right)^6
> $$
> per qualche $\xi \in \left(0, \dfrac{1}{2}\right)$, ergo
>  
> $$
> E_5\left( \dfrac{1}{2} \right) \le \dfrac{{\sqrt 3}}{6! \cdot 2^6}
> $$
> 
> Approssimazione con $T_{n,0}\left( \dfrac{1}{2} \right)$:
> 
> $$
> E_n\left( \dfrac{1}{2} \right) \le \dfrac{{\sqrt 3}}{n! \cdot 2^n}
> $$
> 
> e notiamo che al crescere di $n$ il valore con cui si stima

---

> [!fonti]+ Fonti
> 
> - 🏫 Corso di Laurea in Informatica (`L-31 R`) presso l'Università di Torino:
> 	- Corso di _Analisi Matematica - canale C_, A.A. 2020-21 ([pagina Moodle](https://informatica.i-learn.unito.it/course/view.php?id=2075)):
> 		- Prof. Barutello Vivina Laura, videolezioni:
> 			- [_L12a_](https://informatica.i-learn.unito.it/local/streamingfilemanager/file.php/informatica.i-learn.unito.it/2075/L12a.mp4), [_L12b_](https://informatica.i-learn.unito.it/local/streamingfilemanager/file.php/informatica.i-learn.unito.it/2075/L12b.mp4).
