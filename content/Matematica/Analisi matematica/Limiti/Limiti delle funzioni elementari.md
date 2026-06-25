
> [!premessa]+ Premessa
> 
> Ciao! Se è la prima volta che capiti su questo sito, ti consiglio di consultare la [pagina principale](index.md) di questo cosiddetto _Giardino Digitale_ per scoprire meglio cos'è e come navigarlo.
> 
> Lo stato di questa nota è al momento: 🔴 <font color="#FF7F7F">_Bozza_</font>.

---

# 1 - Limiti delle funzioni costanti

$$
f(x) = c \in \mathbb{R}
$$

Si ha che

$$
\forall x_0 \in \mathbb{R}. \big( \lim_{x \to x_0} f(x) = \lim_{x \to \pm \infty} f(x) = c \big) 
$$

# 2 - Limiti delle funzioni potenza

## 2.1 - $f(x) = x^n$

con $n \in \mathbb{N}^{\ge 1}$

Si ha che

$$
\forall x_0 \in \mathbb{R} . \big( \lim_{x \to x_0} x^n = x_0^n \big) 
$$

$$
\lim_{x \to + \infty} x^n = + \infty
$$

$$
\lim_{x \to - \infty} x^n = \begin{cases}
+ \infty & \text{se } n \text{ è pari} \\
- \infty & \text{se } n \text{ è dispari} \\
\end{cases}
$$

## 2.2 - $f(x) = \dfrac{1}{x^n}$

%% che è uguale a $x^n$ con $n < 0$? %%

con $n \in \mathbb{N}^{> 0}$

Si ha che

$$
\forall x_0 \ne 0 . \big( \lim_{x \to x_0} \dfrac{1}{x^n} = \dfrac{1}{x^n_0} \big) 
$$

$$
\lim_{x \to \pm \infty} \dfrac{1}{x^n} = 0
$$

Se $n$ è pari, allora $\lim_{x \to 0} \dfrac{1}{x^n} = + \infty$
Se $n$ è dispari, allora $\lim_{x \to 0^\pm} \dfrac{1}{x^n} = \pm \infty$ ma non esiste $\lim_{x \to 0} \dfrac{1}{x^n}$

La retta $x = 0$ è un asintoto verticale, la retta $y = 0$ è un asintoto orizzontale.

## 2.3 - $f(x) = \dfrac{1}{(x-a)^n}$

con $a \in \mathbb{R} \setminus \{ 0 \} \land n \in \mathbb{N}^{> 0}$

abbiamo che

$$
\text{dom}(f) = (-\infty, a) \cup (a, + \infty)
$$

%% 
continuare pagg. 152-155 Lancelotti
%%

---

> [!fonti]+ Fonti
> 
> - 📚 Sergio Lancelotti, _Lezioni di Analisi Matematica I_, Celid, 2020 (ISBN: `978-8867891979`):
> 	- Capitolo 3 - _Limiti e continuità_:
> 		- 2 - _Limiti di funzioni_:
> 			- 2.5 - _Limiti delle funzioni elementari_.
