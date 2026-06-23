---
title: Integrali
---

> [!premessa] Premessa
> 
> Ciao! Se è la prima volta che capiti su questo sito, ti consiglio di consultare la [pagina principale](index.md) di questo cosiddetto _Giardino Digitale_ per scoprire meglio cos'è e come navigarlo.
> 
> Lo stato di questa nota è al momento: 🔴 <font color="#FF7F7F">_Bozza_</font>.

---

Un oggetto si muove su una retta sotto l'azine di una forza $F$ che dipende solo dalla posizione in cui si trova:
- $x$: posizione dell'oggetto
- $F(x)$: forza nel punto $x$

Vogliamo arrivare a definire il LAVORO compiuto da $F$ per spostare l'oggetto dal punto $a$ al punto $b$.

1° passo: $F$ costante
Definizione del lavoro: se $F \colon [a,b] \to \mathbb{R}$ è costante, allora
$$
L_{F} = F \cdot (b - a)
$$
Se $F > 0$, allora $L_F$ è l'area

2° passo: $F$ costante a tratti, ovvero $F$ assume al più un numero finito di valori su $[a,b]$ su un numero finito $N > 1$ di suoi sottointervalli $x_1 < x_2 < \ldots < x_{n-1}$ (con $a = x_0$ e $b = x_n$). Si ha cioè che $F$ è costante nel singolo intervallo, ma non in generale.
Definizione del lavoro: se $F \colon [a,b] \to \mathbb{R}$ è costante a tratti, allora
$$
L_F = \sum_{i = 1}^N F_i(x_i - x_{i-1})
$$
Se $F_i > 0$ per ogni $i$, allora $L_F$ è la somma delle aree dei rettangolini.

3° passo: $F$ qualsiasi, neanche costante a tratti. Proviamo a fare così:
1. Prendiamo $N \in \mathbb{N}^{> 1}$ e suddividiamo $[a,b]$ in $N$ sottointervalli della stessa lunghezza (per semplicità scegliamo la stessa lunghezza):
	$$
	\dfrac{b-a}{N}
	$$
	Gli intervalli saranno:
	$$
	[x_0,\underbrace{x_1}_{=a}], [x_1, x_2], \ldots, [x_{n-2}, x_{n-1}], [x_{n-1}, \underbrace{x_{n}}_{=b}]
	$$
2. Su ognuno di questi intervalli approssimiamo $F$ con un valore costante. Per farlo scegliamo un punto $z_i \in [x_{i-1}, x_i)$ nell'intervallo e definiamo una funzione $G(x)$ che vale il valore della forza $F$ nel punto $z_i$.
3. Ora questa funzioen $G$ è costante a tratti, quindi potremmo provare ad applicare la definzione di prima del lavoro di una funzione $F$ costante a tratti per il lavoro di $G$ che effettivamente è costante a tratti:
	$$
	\begin{align*}
	L_F &\approx L_G \\
	& = \sum_{i = 1}^N F(z_i) \underbrace{(x_i - x_{i - 1})}_{\dfrac{b-a}{N}} \\
	& = \dfrac{b-a}{N} \sum_{i = 1}^N F(z_i)
	\end{align*}
	$$
	nota: $(x_i - x_{i - 1})$, per qualsiasi $i$, è sempre uguale a $\dfrac{b-a}{N}$ perché le lunghezze sono uguali.
4. Per rendere questa approssimazione sempre più accurata, dobbiamo ridurre sempre di più la lunghezza degli intervalli. Per farlo, usiamo il limite

Definizione: se $\displaystyle\lim_{\dfrac{b-a}{N} \to 0} \left( \dfrac{b-a}{N} \sum_{i=1}^N F(z_i) \right)$ esiste ed è finito e non dipende da come sono stati scelti i punti $z_i$, allora questo valore è $L_F$.

Problema: come scegliamo i punti $z_i$ in cui valutare $F$?
1. Prendo gli $z_i$ dopo aver fatto delle valutazioni sulla $F$, ad esempio scegliendo il punto in cui $F$ è massima o minima nell'intervallo $[x_{i-1}, x_i)$
2. Prendo gli $z_i$ secondo un criterio indipendente da $F$, per esempio il punto medio.

Arriviamo quindi ad un'approssimazione di $L_F$ attraverso la seguente espressione:

$$
L_F \approx \dfrac{b-a}{N} \sum_{i = 1}^N F\left( \dfrac{x_{i-1}+x_i}{2} \right)
$$

Questa è la formula del punto medio con $N$ suddivisioni

---

Esempio di applicazione:

$$
F(x) = \dfrac{1}{x^2}
$$

(cioè la forza repulsiva).

Calcoliamo il lavoro su 5 suddivisioni, con $a = 1$ e $b = 5$. Ampiezza dell'intervallo: $\dfrac{b-a}{5} = 0.8$.

%% 
tabella con $i$, $x_{i-1}$, $x_i$, $z_i$ e $F(z_i)$
%%

Calcoliamo il lavoro:

$$
L_F \approx \dfrac{b-a}{N} \sum_{i=1}^5 F(z_i) = 0.8 \sum_{i=1}^5 F(z_i) \approx 0.76
$$

---

Ora possiamo parlare di _integrale definito di una funzione su un intervallo_:

Dati una [funzione](content/Matematica/Teoria%20degli%20insiemi/Funzioni/_index.md#^definizione-funzione) $f \colon [a,b] \to \mathbb{R}$, un valore $N \in \mathbb{N}^{\ge 1}$ intero e $x_0 = a$, $x_N = b$ e $x_1, \ldots, x_{n-1}$ i punti di $(a,b)$ che suddividono $[a,b]$ in $N$ intervalli di ampiezza $\dfrac{b-a}{N}$ e un punto medio $z_i \in [x_{i-1}, x_i)$ per ogni intervallo se il [limite](content/Matematica/Analisi%20matematica/Limiti/_index.md#^definizione-limite) $\displaystyle\lim_{N \to + \infty} \dfrac{b-a}{N} \sum_{i=1}^N F(z_i)$ esiste finito e non dipende dalla scelta degli $z_i$ allora il valore che si ottiene è detto **integrale definito di $F$ su $[a,b]$** e si indica con

$$
\int_a^b f(x)dx
$$

(dove la $\int$ rappresenta una S di "sommatoria" allungata).

---

Un'osservazione: la somma $\displaystyle\dfrac{b-a}{N} \sum_{i=1}^N f(z_i)$ viene detta **somma di Riemann** e si indica con $S_N(f; z_1, \ldots, z_N)$.

Se $f \ge 0$, allora la $S_N$ è la somma delle aree dei rettangoli di base $\dfrac{b-a}{N}$ e altezza $F(z_i)$.

---

Osservazione: quando $\dfrac{b-a}{N} \to 0$ (cioè $N \to +\infty$) la somma di Riemann tende all'integrale, dove:
- $f(x)$ sono i singoli $f(z_i)$ perché, dato che col limite abbiamo infiniti intervalli, riusciamo a "coprire" ogni $x$ con un $z_i$ del rispettivo intervallo.
- $dx$ corrisponde a $\dfrac{b-a}{N}$ che è la lunghezza infinitesima (cioè che tende a 0) del singolo intervallo.

---

L'integrale è quindi un numero e, se $F \ge 0$, è il valore dell'area compresa tra il grafico di $F$ e l'asse delle ascisse.

Se $F$ è negativa o se assume valori negativi sull'intervallo $[a,b]$ allora l'inegrale non rappresenta un'area (non esistono aree negative!).

Però c'è comunque una relazione tra $\int_a^b f(x)dx$ e l'area tra il grafico di $f$ e l'asse $x$:
- Se $f \le 0$ su $[a,b]$ allora l'area è $- \int_a^b f(x)dx$ (cioè l'integrale ma invertito di segno per renderlo positivo)
- Se $f$ cambia segno, invertiamo di segno solo le parti negative e sommiamole a quelle positive.

In generale:

$$
\text{Area} = \int_a^n |f(x)|dx
$$

---

> [!fonti]+ Fonti
> 
> - 🏫 Corso di Laurea in Informatica (`L-31 R`) presso l'Università di Torino:
> 	- Corso di _Analisi Matematica - canale C_, A.A. 2020-21 ([pagina Moodle](https://informatica.i-learn.unito.it/course/view.php?id=2075)):
> 		- Prof. Barutello Vivina Laura, videolezioni:
> 			- [_L4a_](https://informatica.i-learn.unito.it/local/streamingfilemanager/file.php/informatica.i-learn.unito.it/2075/L4a.mp4), [_L4b_](https://informatica.i-learn.unito.it/local/streamingfilemanager/file.php/informatica.i-learn.unito.it/2075/L4b.mp4).