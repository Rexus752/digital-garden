---
draft: true
---

# Definizioni ricorsive di funzioni

> [!definizione] Definizione: funzione definita ricorsivamente
> 
> Una funzione $f \colon \mathbb{N} \to \mathbb{N}$ è **definita ricorsivamente** se il suo valore per un dato argomento viene determinato sulla base di uno o più valori precedenti della funzione stessa:
> $$
> f(n) = \begin{cases}
> a & n = k \\
> E(n, f(n-1)) & n > k
> \end{cases}
> $$
> dove:
> - $k \in \mathbb{N}$: è il punto di partenza, noto anche come _**caso base**_, per la definizione della funzione.
> - $a \in \mathbb{N}$: è il valore assegnato a $f(k)$, specificato esplicitamente.
> - $E(n, f(n-1))$: è un'espressione che calcola $f(n)$ utilizzando il valore precedente della funzione, $f(n-1)$, ed eventualmente il valore di $n$ stesso.
^Definizione-funzione-ricorsiva

%% 
https://it.wikipedia.org/wiki/Definizione_ricorsiva
https://it.wikipedia.org/wiki/Funzione_ricorsiva
%%

> [!esempio] Esempio: funzione ricorsiva per il calcolo del quadrato
> 
> Si può definire ricorsivamente una funzione $q(n)$ per calcolare il quadrato di un numero naturale $n \in \mathbb{N}$ nel seguente modo:
> $$
> q(n) = \begin{cases}
> 0 & n = 0 \\
> q(n-1) + 2 \cdot n + 1 & n > 0
> \end{cases}
> $$
> 
> Le clausole della definizione ricorsiva della funzione $q(n)$ consentono di calcolare il valore di questa funzione per un valore arbitrario dell'argomento, ad esempio:
> 
> $$
> \begin{align*}
> {\color{#FF8888} q(0) } &  = {\color{#FF8888} 0 } \\
> {\color{#88FF88} q(1) } & = {\color{#FF8888} q(0) } + 2 \cdot 0 + 1 = {\color{#FF8888} 0 } + 1 = {\color{#88FF88} 1 } \\
> {\color{#8888FF} q(2) } & = {\color{#88FF88} q(1) } + 2 \cdot 1 + 1 = {\color{#88FF88} 1 } + 3 = {\color{#8888FF} 4 } \\
> {\color{#FFFF88} q(3) } & = {\color{#8888FF} q(2) } + 2 \cdot 2 + 1 = {\color{#8888FF} 4 } + 5 = {\color{#FFFF88} 9 } \\
> {\color{#FF88FF} q(4) } & = {\color{#FFFF88} q(3) } + 2 \cdot 3 + 1 = {\color{#FFFF88} 9 } + 7 = {\color{#FF88FF} 16 }
> \end{align*}
> $$
> 
> e così via.
^Esempio-funzione-ricorsiva-per-il-calcolo-del-quadrato

%%
Vediamo ora che le clausole precedenti definiscono effettivamente la funzione desiderata, dimostrando per induzione che la proprietà $q(n) = n^2$ è vera per ogni valore di $n$.

Caso base (n = 0)
= 0^2

Ipotesi induttiva: $q(n) = n^2$. Tesi induttiva: $q(n + 1) = (n + 1)^2$.

Passo induttivo (n → n + 1)
q(n + 1) = q(n) + 2 · n + 1 (per definizione)
= n^2 + 2 · n + 1 (per ipotesi induttiva)
= (n + 1)^2 (per propriet`a algebriche)
%%

# Fonti

- Slide del Prof. Viale Matteo del corso di Logica Matematica (canale B), Corso di Laurea in Informatica presso l'Università di Torino, A.A. 2024-25:
	- [3.1 - Le Diverse Forme del Principio di Induzione_moodle.pdf](https://informatica.i-learn.unito.it/pluginfile.php/417200/mod_folder/content/0/3.1%20-%20Le%20Diverse%20Forme%20del%20Principio%20di%20Induzione_moodle.pdf)
