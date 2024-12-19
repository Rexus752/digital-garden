---
draft: true
---
%%
Fonti già viste:
- Lezioni di
- Del capitolo 1:
	- Capitolo 1.1 - Insiemi

Fonti da vedere:
- Del capitolo 1:
	- Capitolo 1 (prima del 1.1)
	- Capitolo 1.2 - Modelli probabilistici
	- Del capitolo 1.2, vedere:
		- Choosing an Appropriate Sample Space
		- Sequential Models
%%

Probabilità = scienza che studia esperimenti che hanno un esito "non facilmente prevedibile", detti _esperimenti probabilistici_.

Per esempio, il lancio di un dado a 6 facce è un esperimento di cui non si può facilmente prevedere il risultato, proprio perché può uscire una qualsiasi tra le 6 facce disponibili. In realtà, se si fosse in grado di conoscere tutte le quantità fisiche in gioco in un lancio (es. velocità di lancio del dado, inclinazione del lancio, posizione della mano, materiali del dado e della superficie su cui atterra il dado, peso del dado, ecc.) si potrebbe effettivamente prevedere il movimento esatto del dado e, quindi, sapere quale sarà la faccia che uscirà. %% [Persi Diaconis ce l'ha fatta](https://www.stat.berkeley.edu/~aldous/157/Papers/diaconis_coinbias.pdf) %%

Metodologia probabilistica: usa la teoria degli insiemi

# Strumenti della probabilità

> [!definizione] Definizione: esperimento probabilistico
> Un **esperimento probabilistico** è un processo in cui si produce un esito %%completare%%

> [!osservazione] Osservazione: restrizioni sulla definizione di "esperimento probabilistico"
> Non ci sono restrizioni su cosa può essere un esperimento probabilistico.
> Per esempio, potrebbe essere un singolo lancio di una moneta, tre lanci, o una sequenza infinita di lanci.

> [!definizione] Definizione: spazio campionario
> Uno **spazio campionario** è l'insieme di tutti i possibili esiti di un esperimento probabilistico e si indica solitamente con $\Omega$. 

> [!esempio] Esempio: lancio di un dado a sei facce
> Lo spazio campionario di un lancio di un dado a sei facce viene indicato come
> $$
> \Omega = \{1,2,3,4,5,6\}
> $$

> [!osservazione] Osservazione: descrizione di esiti probabilistici non numerici
> Dal momento che non tutti gli esperimenti probabilistici sono esperimenti di tipo numerico (es. il lancio di una moneta, che ha come possibili esiti le due facce _"testa"_ o _"croce"_), si può associare arbitrariamente a ogni esito un'etichetta che lo identifichi.

> [!esempio] Esempio: lancio di una moneta
> $$
> \Omega = \{T, C\}
> $$
> dove $T$ sta per _"testa"_ e $C$ sta per _"croce"_.

> [!osservazione] Osservazione: finitezza e infinità%%o infinitezza?%% degli eventi di uno spazio campionario
> Lo spazio campionario di un esperimento probabilistico può avere un numero finito o infinito di possibili esiti. Gli spazi campionari composti da un numero finito di esiti sono concettualmente e matematicamente più semplici, ma allo stesso tempo spazi campionari composti da un numero infinito di esiti sono abbastanza comuni. Per esempio, si consideri il tiro di un dardo su un %%bersaglio bianco e rosso%% e guardare il punto di impatto del dardo come un esito (ci sono infiniti punti sulla superficie).

> [!definizione] Definizione: legge di probabilità
> Una legge di probabilità è una funzione che associa a ogni possibile sottoinsieme $A$ (detto _evento_) di uno spazio campionario $\Omega$ un valore reale compreso tra $0$ e $1$ che ne esprime la _probabilità_. %%è compreso tra 0 e 1?%%
> $$
> \begin{align*}
> \mathbb{P} \colon A \in \mathcal{P}(\Omega) & \to [0, 1] \\
> x & \mapsto y
> \end{align*} 
> $$

> [!esempio] Esempio: legge di probabilità del lancio di un dado
> Spazio campionario: $\Omega = \{1,2,3,4,5,6\}$
> %%Lista possibili sottoinsiemi di $\Omega$%%
> Possibile sottoinsieme di $\Omega$: $\mathcal{P}(\Omega) \ni A = \{2, 4, 6\} = \{2\} \cup \{4\} \cup \{6\} = \{x \mid x \text{ è una faccia con un numero pari}\}$
> Legge di probabilità:
> $$
> \mathbb{P}(A) = \mathbb{P}(\{2, 4, 6\})
> $$

### Assiomi%%o proprietà?%% di $\mathbb{P}$

1. Non-negatività: $\forall A \in \mathcal{P}(\Omega), \mathbb{P}(A) \ge 0$
2. Finitezza (%%normalization in inglese%%): $\mathbb{P}(\Omega) = 1$
3. Additività: If A and B are two disjoint events, then the probability of their union is the same as the somma delle singole probabilità
$$\forall A, B \in \mathcal{P}(\Omega),\ A \cap B = \emptyset \implies \mathbb{P}(A \cup B) = \mathbb{P}(A) + \mathbb{P}(B)$$

### Probabilità dell'insieme vuoto

There are many natural properties of a probability law which have not been included in the above axioms for the simple reason that they can be derived from them. For example, note that the normalization and additivity axioms imply that
$$1 = \mathbb{P}(\Omega) = \mathbb{P}(\Omega \cup \emptyset) = \mathbb{P}(\Omega) + \mathbb{P}(\emptyset) = 1 + \mathbb{P}(\emptyset)$$
and this shows that the probability of the empty event is $0$:
$$
\mathbb{P}(\emptyset) = 0
$$

### Additività numerabile

> [!teorema] Teorema:
> Additività numerabile o $\sigma$-additività: se $(A_i)_{i = 1}^{+\infty}$ è una collezione di sottoinsiemi di $\Omega$, disgiunti a due a due (cioè $\forall i \ne j, A_i \cap A_j = \emptyset$), allora
> $$
> \mathbb{P}\left(\bigcup_{i = 1}^\infty A_i\right) = \sum_{i=1}^{+\infty} \mathbb{P}(A_i)
> $$

> [!dimostrazione] Dimostrazione:
> As another example, consider three disjoint events AI, A 2 , and A3. We can use the additivity axiom for two disjoint events repeatedly, to obtain
> $$
> \begin{align}
> \mathbb{P}(A_1 \cup A_2 \cup A_3) &= \mathbb{P}(A_1 \cup (A_2 \cup A_3)) \\
> &= \mathbb{P}(A_1) + \mathbb{P}(A_2 \cup A_3) \\
> &= \mathbb{P}(A_1) + \mathbb{P}(A_2) + \mathbb{P}(A_3)
> \end{align}
> $$
> Proceeding similarly, we obtain that the probability of the union of finitely many disjoint events is always equal to the sum of the probabilities of these events.
> More such properties will be considered shortly.

### Legge di probabilità dei singoletti

$$
\begin{align*}
1 &= \mathbb{P}(\Omega) \\ 
&= \mathbb{P}(\{1\}) + \mathbb{P}(\{2\}) + \ldots + \mathbb{P}(\{n\}) \\
&= n \cdot \mathbb{P}(\{1\}) \\
\implies
\mathbb{P}(\{1\}) = \frac{1}{n}
\end{align*}
$$

> [!definizione] Definizione: modello probabilistico
> Un modello probabilistico è una descrizione matematica di una situazione incerta. Esso è composto da due elementi:
> 1. Uno [spazio campionario](#Definizione%20spazio%20campionario), cioè un insieme di tutti i possibili esiti di un esperimento probabilistico e si indica solitamente con $\Omega$;
> 2. Una legge di probabilità%%link%% che determina le probabilità degli eventi dello spazio campionario.

> [!attenzione] Attenzione: spazio campionario di un singolo esperimento
> Lo spazio campionario oggetto del modello probabilistico deve rappresentare un singolo esperimento: per esempio, nel caso di un lancio di una moneta per tre volte, viene considerato un unico esperimento in cui ogni esito è la tripla dei possibili esiti di ogni singolo lancio, anziché considerarlo come tre esperimenti separati.

> [!definizione] Definizione: probabilità uniforme discreta
> Dato un sottoinsieme $A \subseteq \Omega$ (quindi $A \in \mathcal{P}(\Omega)$), la probabilità di quell'insieme $A$ è uguale a:
> $$
> \mathbb{P}(A) = \frac{|A|}{|\Omega|}
> $$

> [!esempio] Esempio:
> Lancio tre volte una moneta equa.
> $$
> \begin{align*}
> \Omega
> &= \{(\omega_1, \omega_2, \omega_3) \mid \forall i \in I, \omega_i \in \{T,C\}\} \\
> &= \{(T,T,T), (T,T,C), (T,C,T), (T,C,C), (C,T,T), (C,T,C), (C,C,T), (C,C,C)\}
> \end{align*}
> $$

> [!esempio] Esempio: lanciamo un dado EQUO ad $n$ facce
> $$
> \Omega = \{1, 2, 3, \ldots, n\}
> $$
> Oltre allo spazio campionario, ci serve:
> $$
> \begin{align}
> \mathcal{P}(\Omega) = \{ & \\
> & \emptyset, \Omega, \\
> & \{1\}, \{2\}, \{3\}, \ldots, \{n\}, \\
> & \{1, 2\}, \{2, 3\}, \{1, 3\}, \ldots, \\
> & \{1, 2, 3\}, \{1, 2, 4\}, \ldots, \\
> & \vdots \\
> & \{1, 2, \ldots, n-1 \}, \{1, 2, \ldots, n-2, n\} \\
> \}
> \end{align}
> $$
> Calcolare la numerosità di ogni riga (es. quante coppie o quante terne?): "quanti sono i sottoinsiemi di cardinalità $k$ estratti da un insieme di cardinalità $n$?"
> Formula:
> $$
> \binom{n}{k} = \frac{n!}{k!(n-k)!}
> $$
> dove $n!$ è i modi in cui posso permutare gli elementi di $n$. Nelle permutazioni l'ordine conta: le permutazioni non indicano "una ciotola" in cui ci sono le palline, ma l'ordine in cui le palline vengono estratte.
> $k$ si può riempire da $n$ a $n - k + 1$:
> $$
> n \cdot (n-1) \cdot (n-2) \cdot \ldots \cdot (n-k+1) \cdot \frac{(n-k)!}{(n-k)!} =
> \frac{n!}{(n-k)!}
> $$
> Denominatore = numero di ordinamenti di palline non estratte
> Non è finita qua: non voglio che gli insiemi estratti siano ordinati, ma vogliamo che siano come un sacchetto: per eliminare l'ordinamento delle k palline estratte, dividerò per il numero di ordinamenti delle k palline estratte, cioè k!
> Se mi interessa ordinamento, non serve 1/k!

Esempio:
$$
\binom{6}{2} = \frac{6!}{2!(6-2)!} = \frac{6!}{2! \cdot 4!} = \frac{6 \cdot 5 \cdot \cancel{4!}}{2! \cdot \cancel{4!}} = \frac{30}{2} = 15
$$
$$
\binom{6}{3} = \frac{6!}{3!(6-3)!} = \frac{6!}{3! \cdot 3!} = \frac{6 \cdot 5 \cdot 4 \cdot \cancel{3!}}{\cancel{3!} \cdot 3!} = \frac{120}{6} = 20
$$

Probabilità dei singoletti:
Dato che il dado è equo, ogni faccia ha la stessa probabilità di uscire. Equità implica che:
$$
\mathbb{P}(\{1\}) = \mathbb{P}(\{2\}) = \ldots = \mathbb{P}(\{n\})
$$
Quindi
$$
1 = \mathbb{P}(\Omega) = \mathbb{P}(\{1\} \cup \{2\} \cup \ldots \cup \{n\}) = (additività) = \mathbb{P}(\{1\}) + \mathbb{P}(\{2\}) + \ldots + \mathbb{P}(\{n\}) = n \cdot \mathbb{P}(\{1\})
$$
cioè
$$
\mathbb{P}(\{1\}) = \frac{1}{n}
$$

Probabilità delle coppie:
$$
\{i,j\} per i,j=1, \ldots, n \text{ con } i \ne j
$$
Quindi
$$
\mathbb{P}(\{i,j\}) = \mathbb{P}(\{i\} \cup \{j\}) = (additività) = \mathbb{P}(\{i\}) + \mathbb{P}(\{j\}) = \frac{1}{n} + \frac{1}{n} = \frac{2}{n}
$$
Esempio (con $n = 6$):
$$
\mathbb{P}(\{1,6\}) = \frac{2}{6} = \frac{1}{3}
$$

E così via con le terne ecc.

Possiamo notare che le cardinalità degli insiemi che si stanno considerando è il numeratore di $\frac{*}{n}$:
$$
Dato A \subseteq \Omega (\in \mathcal{P}(\Omega)), \mathbb{P}(A) = \frac{|A|}{|\Omega|}
$$

es. A = "esce un numero pari" = {2, 4, 6} con n = 6.
$$
|A| = 3
$$
quindi
$$
\mathbb{P}(A) = \frac{3}{6} = \frac{1}{2}
$$

Possiamo anche fare $\Omega = \{P, D\}$.

Quando per ogni $A \subseteq \Omega, \mathbb{P}(A) = \frac{|A|}{|\Omega|}$, allora $\mathbb{P}$ si chiama "probabilità uniforme discreta" (uniforme = tutti i singoletti hanno la stessa probabilità, discreta = spazio campionario è discreto, non continuo, oppure cardinalità numerabile, infatti al denominatore mi serve che la cardinalità di $\Omega$ sia finita, altrimenti le probabilità sarebbero $0$).

1:02:00

# Fonti

- Videolezioni del Prof. Polito Federico del corso di Elementi di Probabilità e Statistica (canale B), Corso di Laurea in Informatica presso l'Università di Torino, A.A. 2024-25:
	- [Lez 1 canale B](https://informatica.i-learn.unito.it/mod/url/view.php?id=251450)
	- [Lez 2 canale B](https://informatica.i-learn.unito.it/mod/url/view.php?id=251506)
