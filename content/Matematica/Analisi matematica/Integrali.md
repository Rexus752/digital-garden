
> [!premessa]+ Premessa
> 
> Ciao! Se è la prima volta che capiti su questo sito, ti consiglio di consultare la [pagina principale](index.md) di questo cosiddetto _Giardino Digitale_ per scoprire meglio cos'è e come navigarlo.
> 
> Lo stato di questa nota è al momento: 🔴 <font color="#FF7F7F">_Bozza_</font>.

%% 
in realtà è **Calcolo integrale**
%%

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

Dati una [funzione](Funzioni.md#^definizione-funzione) $f \colon [a,b] \to \mathbb{R}$, un valore $N \in \mathbb{N}^{\ge 1}$ intero e $x_0 = a$, $x_N = b$ e $x_1, \ldots, x_{n-1}$ i punti di $(a,b)$ che suddividono $[a,b]$ in $N$ intervalli di ampiezza $\dfrac{b-a}{N}$ e un punto medio $z_i \in [x_{i-1}, x_i)$ per ogni intervallo se il [limite](Limiti.md#^definizione-limite) $\displaystyle\lim_{N \to + \infty} \dfrac{b-a}{N} \sum_{i=1}^N F(z_i)$ esiste finito e non dipende dalla scelta degli $z_i$ allora il valore che si ottiene è detto **integrale definito di $F$ su $[a,b]$** e si indica con

$$
\int_a^b f(x)dx
$$

(dove la $\int$ rappresenta una S di "sommatoria" allungata).

---

Un'osservazione: la somma $\displaystyle\dfrac{b-a}{N} \sum_{i=1}^N f(z_i)$ viene detta **somma di Riemann** e si indica con $S_N(f; z_1, \ldots, z_N)$.

In realtà la somma di Riemann è una successione:

$$
a_n = S_N(f; z_1, \ldots, z_N)
$$

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

Qual è il significato dell'integrale della velocità?

Riprendiamo l'oggetto che si muove su una retta:
- $s(t)$: posizione dell'oggetto al tempo $t$
- $v(t)$: velocità istantena dell'oggetto al tempo $t$

Che cosa rappresenta $\int_a^b v(t)dt$?

In termini di unità di misura, se $f$ è $[Y]$ e $x$ è $[X]$, allora $\int_a^b f(x)dx$ è $[Y \cdot X]$

Allo stesso modo, $\int_a^b v(t)dt$ è $\left[ \dfrac{m}{s} \cdot s \right] = [m]$, cioè l'integrale definito della velocità è dimensionalmente uno spostamento

Ma di quale spostamento si tratta?

$$
\int_a^b v(t)dt = \lim_{N \to \infty} \sum_{i = 1}^N v(z_i) \dfrac{b-a}{N}
$$
dove:
- $z_i$ è il punto medio in $[t_{i-1},t_i)$
- $a = t_0 < t_1 < \ldots < t_{n-1} < t_n = b$
- $v(z_i)$ è la velocità istantanea in $z_i$

$v(z_i)$ è la pendenza della retta tangente al grafico di $s$ nel punto $(z_i, s(z_i))$ e possiamo approssimarla alla pendenza della retta secante che passa per i punti $(t_{i-1}, s(t_{i-1}))$ e $(t_i, s(t_i))$, ovvero si può approssimare col rapporto di Newton:

$$
\begin{align*}
v(z_i) &\approx \dfrac{s(t_i) - s(t_{i-1})}{t_i - t_{i-1}} \\
&= \dfrac{s(t_i) - s(t_{i-1})}{\dfrac{b-a}{N}} \implies v(z_i) \cdot \dfrac{b-a}{N} \approx s(t_i) - s(t_{i-1})
\end{align*}
$$

Con la costruzione che abbiamo fatto, $t_i - t_{i-1}$ è uguale a $\dfrac{b-a}{N}$, quindi moltiplichiamo entrambe le quantità per $\dfrac{b-a}{N}$ e otteniamo dopo il $\implies$ che $v(z_i) \cdot \dfrac{b-a}{N}$ è il termine delle somme di Riemann, quindi

$$
\begin{align*}
\int_a^b v(t)dt &= \lim_{N \to \infty} \sum_{i = 1}^N v(z_i) \dfrac{b-a}{N} \\
&\approx \sum_{i=1}^N v(z_i) \dfrac{b-a}{N} \\
&= \sum_{i=1}^N s(t_i) - s(t_{i-1}) \\
&= \cancel{s(t_1)} - s(t_0) \cancel{+ s(t_2)} \cancel{- s(t_1)} \cancel{+ s(t_3)} \cancel{- s(t_2)} + \ldots + s(t_n) \cancel{- s(t_{n-1})} \\
&= s(t_N) - s(t_0) \\
&= s(b) - s(a)
\end{align*}
$$

Conclusione:

$$
\int_a^b v(t)dt = s(b) - s(a)
$$

e non dipende da $N$! È quindi lo spostamento netto tra il tempo $a$ e il tempo $b$.

Con questo quindi possiamo passare dal grafico della velocità a quello dello spostamento.

---

Dal momento che $v$ è la derivata di $s$, abbiamo che

$$
\int_a^b s'(t)dt = s(b) - s(a)
$$

e, semplicemente cambiando nome agli oggetti, potevamo dedurre

$$
\int_a^b f'(t)dt = f(b) - f(a)
$$

oppure

$$
\int_a^b f(t)dt = F(b) - F(a)
$$

con $F'(t) = f(t)$ (cioè $F$ è la primitiva di $f$)

cioè il Teorema di Torricelli-Barrow o Teorema di valutazione

---

Se $f \ge 0$ su $[a,b]$, allora $\int_a^b f(t)dt = F(b) - F(a)$ rappresenta l'area.

---

Possiamo ora sostituire $b$ con qualsiasi $x \in [a,b]$ e considerare solo una porzione di quest'area:

$$
\int_a^x f(t)dt = F(x) - F(a)
$$

definiamo questo integrale come $G(x)$ e notiamo che:
- $G(a) = 0$
- $G$ è una primitiva di $f$, infatti $G'(x) = (F(x) - F(a))' = (F(x))' - (F(a))' = F'(x) + 0$ (perché $F(a)$ è una costante)

$G(x)$ è una funzione integrale.

Arriviamo quindi al seguente risultato:

Teorema fondamentale del calcolo integrale:
Data una [funzione](Funzioni.md#^definizione-funzione) $f \colon [a,b] \to \mathbb{R}$ tale che $G(x) = \int_a^b f(t)dt$, allora $G$ è derivabile e $G'(x)=f(x)$ per ogni $x \in [a,b]$.

---

Esempio: grafico rappresenta la velocità di un oggetto che si muove su una retta. Stimare la posizione dell'oggetto quando $t=2$ sapendo che $s(0)=2$.

Ora sappiamo che $\int_0^2 v(t)dt = s(2)-s(0)$ quindi $s(2) = s(0) + \int_0^2 v(t)dt$ e possiamo stimare $\int_0^2 v(t)dt$ con una somma del tipo $\sum_{i=1}^n v(z_i)\dfrac{(b-a)}{N}$

Scegliamo $N = 4$ così ogni intervallo è $0.5$ e determiniamo i vari punti $x_i$, $z_i$ e $v(z_i)$.

Facciamo quindi i calcoli:

$$
s(2) \approx s(0) + \sum_{i=1}^4 v(z_i)\dfrac{(2-0)}{4} = 2 + 0.66 = 2.66
$$

Se avessimo usato $N=3$ avremmo ottenuto $s(1.5) \approx 2.95$

---

Data una [funzione](Funzioni.md#^definizione-funzione) $f \colon [a,b] \to \mathbb{R}$, cos'è la sua media?
Sappiamo cos'è la media aritmetica, quindi se prendiamo $N$ valori assunti dalla $f$ su $[a,b]$ e facciamo la media di questi valori, otteniamo

$$
\dfrac{f(z_i) + \ldots + f(z_n)}{n}
$$

ma
1. quanto grande prendiamo $n$?
2. quali $z_i$ prendiamo?

Risposte:
1. più grande è $n$, più è precisa l'approssimazione!
2. come nella costruzione dell'integrale, prendiamo i putni medi
$$
\lim_{n \to + \infty} \dfrac{1}{n} \sum_{i=1}^n f(z_i) = \lim_{n \to + \infty} \dfrac{1}{b-a} \sum_{i=1}^n f(z_i) \dfrac{b-a}{n} = \dfrac{1}{b-a} \int_a^b f(t)dt
$$

che è il teorema della media integrale.

---

Interpretazione geometrica del teorema della media integrale:

se $f \ge 0$ allora la media di $f$ su $[a,b]$ è il numero che moltiplicato per la lunghezza di $[a,b]$ ci fornisce l'area $\int_a^b f$, cioè è l'altezza dell'area $\int_a^b f$.

---

> [!fonti]+ Fonti
> 
> - 🏫 Corso di Laurea in Informatica (`L-31 R`) presso l'Università di Torino:
> 	- Corso di _Analisi Matematica - canale C_, A.A. 2020-21 ([pagina Moodle](https://informatica.i-learn.unito.it/course/view.php?id=2075)):
> 		- Prof. Barutello Vivina Laura, videolezioni:
> 			- [_L4a_](https://informatica.i-learn.unito.it/local/streamingfilemanager/file.php/informatica.i-learn.unito.it/2075/L4a.mp4), [_L4b_](https://informatica.i-learn.unito.it/local/streamingfilemanager/file.php/informatica.i-learn.unito.it/2075/L4b.mp4).
> 			- [_L5a_](https://informatica.i-learn.unito.it/local/streamingfilemanager/file.php/informatica.i-learn.unito.it/2075/L5a.mp4), [_L5b_](https://informatica.i-learn.unito.it/local/streamingfilemanager/file.php/informatica.i-learn.unito.it/2075/L5b.mp4).
