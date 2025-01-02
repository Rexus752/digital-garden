---
draft: true
---
# 4 - Operazioni sugli insiemi

## 4.1 - Definizione: intersezione di due insiemi

Dati due insiemi $A$ e $B$, si dice _**intersezione**_ di $A$ e $B$ e si denota $A\cap B$ l'insieme che comprende gli elementi che appartengono contemporaneamente sia ad $A$ che a $B$:
$$ A \cap B = \{x \mid x \in A \land x \in B\} $$
Due insiemi $A$ e $B$ si dicono _disgiunti_ se non hanno elementi in comune:
$$ A \cap B = \emptyset $$
%% rappresentazione con Eulero-Venn %%

### 4.1.1 - Esempio: intersezione di due insiemi

Dati due insiemi $A=\{n \in \mathbb{N} \mid n \text{ è pari}\}$ e $B=\{n\in\mathbb{N}\mid10\le n^2 \le200\}$, allora si ha che $A \cap B = \{4,6,8,10,12,14\}$.​

### 4.1.2 - Esempio: intersezione di tre insiemi

Dati tre insiemi $A=\{a,b,c,d,e\}$, $B=\{d,e,f,g\}$ e $C=\{g,h,i\}$, allora si ha che: $A\cap B = \{d,e\}$, $B\cap C = \{g\}$, $A \cap C = \emptyset$ e $A\cap B\cap C=\emptyset$.

### 4.1.3 - Esempio: intersezione di insiemi delle parti

Dato un insieme $X=\{a,b,c,d\}$ e dati due insiemi
$$
A = \{S \in \mathcal{P}(X) \mid |S| = 2\} = \{\{a,b\}, \{a,c\}, \{a,d\}, \{b,c\}, \{b,d\}, \{c,d\}\}, \\
B = \{S \in \mathcal{P}(X) \mid c \in S\} = \{\{c\}, \{a,c\}, \{b,c\}, \{c,d\}, \{a,b,c\}, \{b,c,d\}, \{a,c,d\}, \{a,b,c,d\}\}
$$
allora
$$
A \cap B = \{\{a,c\},\{b,c\},\{c,d\}\}
$$

## 4.2 - Definizione: unione di due insiemi

Dati due insiemi $A$ e $B$, si dice _**unione**_ di $A$ e $B$ e si denota $A\cup B$ l'insieme contenente tutti gli elementi di entrambi gli insiemi:
$$ A \cup B = \{x \mid x \in A \lor x \in B\} $$
Gli elementi che si trovano sia in $A$ che in $B$ vengono presi in considerazione una volta sola perché, []((Insiemistica).md#1.1.4%20-%20<span%20style="color%20888888;%20background%2000000000">Osservazione%20unicità%20degli%20elementi), non ci possono essere elementi ripetuti in un insieme.
%% rappresentazione con Eulero-Venn %%

### 4.2.1 - Esempio: unione di due insiemi

Dati due insiemi $A=\{0,1\}$ e $B=\{2,3,4\}$, si ha che $A\cup B=\{0,1,2,3,4\}$.

### 4.2.2 - Esempio: unione di tre insiemi

Dati tre insiemi
$$
A=\{a,b,c,d,e\} \\
B=\{d,e,f,g\} \\
C=\{g,h,i\}
$$
allora si ha che $A \cup B = \{a,b,c,d,e,f,g\}$, $B\cup C = \{d,e,f,g,h,i\}$, $A \cup C = \{a,b,c,d,e,g,h,i\}$ e $A\cup B \cup C = \{a,b,c,d,e,f,g,h,i\}$.

### 4.2.3 - Esempio: unione degli insiemi dei numeri pari e dispari

Dati due insiemi $A = \{n \in \mathbb{N} \mid n \bmod 2 = 0\}$ e $B = \{n \in \mathbb{N} \mid n \bmod 2 = 1\}$, ossia rispettivamente gli insiemi dei numeri naturali pari e dispari, allora $A \cup B = \mathbb{N}$.

## 4.3 - Definizione: differenza tra due insiemi

Dati due insiemi $A$ e $B$, si dice _**differenza**_ tra $A$ e $B$ e si denota $A \setminus B$ l'insieme degli elementi presenti in $A$ ma non in $B$:
$$
A \setminus B = \{x \mid x \in A \land x \notin B\}
$$
%% rappresentazione con Eulero-Venn %%

### 4.3.1 - Esempio: differenza tra due insiemi

Dati due insiemi $A=\{0,1,2\}$ e $B=\{2\}$, si ha che $A\setminus B=\{0,1\}$.

%%
\### Definizione: differenza simmetrica tra due insiemi

Dati due insiemi $A$ e $B$, si dice _**differenza simmetrica**_ tra $A$ e $B$ e si denota $A \Delta B$ l'insieme degli elementi presenti solamente in uno dei due insiemi:
$$
A \Delta B = \{ x \mid \forall x ((x \in A \land x \notin B) \lor (x \in B \land x \notin A)) \}
$$
Alternativamente, si può indicare la differenza simmetrica tra $A$ e $B$ come l'unione delle differenze tra i due insiemi:
$$
A \Delta B = (A \setminus B) \cup (B \setminus A)
$$
Oppure, come la differenza tra la loro unione e la loro intersezione:
$$
A \Delta B = (A \cup B) \setminus (A \cap B)
$$

\#### Esempio

Dati due insiemi $A = \{1, 4, 6, 23, 57\}$ e $B = \{2, 4, 6, 8, 10\}$, allora:
$$
A \Delta B = \{1, 2, 8, 10, 23, 57\}
$$
%%

## 4.4 - Definizione: complementare di un insieme

%%
Differenza tra complementare assoluto e complementare relativo:
https://en.wikipedia.org/wiki/Complement_(set_theory)

Cambiare notazione per il complementare in $A^\complement$
%%

Dati due insiemi $A$ e $B$ con $A\subseteq B$, si dice _**complementare**_ di $A$ in $B$ e si denota $\complement_B(A)$ il sottoinsieme degli elementi di $B$ non in $A$:
$$
\complement_B(A) = \{ x \mid x \in B \land x \notin A \}
$$

### 4.4.1 - Osservazione: $\color{#888888}\complement_B(A)=B\backslash A$

Dati due insiemi $A$ e $B$ con $A\subseteq B$, il complementare $\complement_B(A)$ di $A$ in $B$ si può esprimere anche come la []((Insiemistica).md#4.3%20-%20<span%20style="color%20FF88FF;%20background%2000000000">Definizione%20differenza%20tra%20due%20insiemi) $B\backslash A$ tra $B$ e $A$: $\complement_B(A)=B\backslash A$.

### 4.4.2 - Osservazione: $\color{#888888}\Bbb{I}=\complement_\Bbb{R}(\Bbb{Q})$

L'insieme dei numeri irrazionali $\Bbb{I}$ si può esprimere come complementare di $\Bbb{Q}$ in $\Bbb{R}$: $\Bbb{I}=\complement_\Bbb{R}(\Bbb{Q})$.

%%
Proposizione: $\color{#FF8888}\complement_B(\complement_B(A)) = A$
Dati due insiemi $A$ e $B$ con $A\subseteq B$, il doppio complementare $\complement_B(\complement_B(A))$ di $A$ in $B$ è sempre uguale ad $A$: $\complement_B(\complement_B(A)) = A$.

Dimostrazione:
Dobbiamo verificare che, qualunque sia A, valga la formula
∀x (x \in \complement\complementA \leftrightarrow x \in A).

Fissiamo quindi un generico x. Sfruttando la corrispondenza tra operazioni insiemistiche e connettivi logici visti in precedenza, la formula
x \in \complement\complementA \leftrightarrow x \in A
diventa
\lnot(\lnot(x \in A)) \leftrightarrow x \in A.

Se ora nella formula
\lnot(\lnot(x \in A)) \leftrightarrow x \in A
sostituiamo l'affermazione "x \in A" con una corrispondente lettera
proposizionale P otteniamo la formula proposizionale
\lnot(\lnotP) \leftrightarrow P.

In generale, il fatto che P sia vera o meno dipenderà naturalmente dalla scelta di A e x: ma noi vogliamo proprio dimostrare che l'equivalenza è vera in ogni caso (cioè comunque vengano presi A e x), ovvero che la proposizione precedente è una tautologia. Utilizzando le tavole di verità si verifica facilmente che questo è vero (legge della doppia negazione), quindi comunque siano presi A e x avremo che
x \in \complement\complementA \leftrightarrow x \in A,
da cui \complement\complementA = A, come desiderato.
$\blacksquare$
%%

%%
Proposizione:
\complement(A \cup B) = \complementA \cap \complementB

Dimostrazione:
Dobbiamo dimostrare che per ogni x
x \in \complement(A \cup B) \leftrightarrow x \in \complementA \cap \complementB.

Utilizzando la corrispondenza tra operazioni insiemistiche e connettivi che abbiamo visto, la formula precedente diventa
\lnot(x \in A \lor x \in B) \leftrightarrow \lnot(x \in A) \land \lnot(x \in B).

Questa è una proposizione della forma
\lnot(P \lor Q) \leftrightarrow \lnotP \land \lnotQ
dove P e Q sono, rispettivamente, "x \in A" e "x \in B". Poiché tale proposizione è una tautologia (leggi di De Morgan), l'identità insiemistica è dimostrata
$\blacksquare$
%%

%%
Proposizione:
\complement(A \cap B) = \complementA \cup \complementB

Dimostrazione:
Dobbiamo dimostrare che per ogni x
x \in \complement(A \cap B) \leftrightarrow x \in \complementA \cup \complementB,
ovvero che
\lnot(x \in A \land x \in B) \leftrightarrow \lnot(x \in A) \lor \lnot(x \in B).

Questa è una proposizione della forma
\lnot(P \land Q) \leftrightarrow \lnotP \lor \lnotQ,
dove P e Q sono, rispettivamente, "x \in A" e "x \in B". Poiché tale proposizione è una tautologia (leggi di De Morgan), l'identità insiemistica iniziale è dimostrata.
$\blacksquare$

Altra dimostrazione:

La stessa identità può anche essere dimostrata utilizzando ciò che abbiamo già dimostrato, ovvero che per tutti gli insiemi X e Y valgono \complement\complementX = X e \complement(X \cup Y ) = \complementX \cap \complementY .
Dimostrazione.
\complement(A \cap B) = \complement(\complement\complementA \cap \complement\complementB)
= \complement (\complement (\complementA \cup \complementB))
= \complement\complement (\complementA \cup \complementB)
= \complementA \cup \complementB
$\blacksquare$
%%

%%
\##Liste ordinate

aggiungere la definizione di liste ordinate o tuple o n-uple
La coppia ordinata $(x, y)$ denota una lista ordinata di due elementi il cui primo elemento è $x$ e il cui secondo elemento è $y$.
Attenzione! A differenza degli insiemi, nelle coppie ordinate l'ordine è fondamentale, cioè $\color{#FF8800}(x, y)$ è un oggetto diverso da $\color{#FF8800}(y, x)$, a meno che $\color{#FF8800}x$ non sia $\color{#FF8800}y$.
Ad esempio, $(0, 1) \ne (1, 0)$ dato che, ad esempio, il primo elemento di $(0, 1)$ è diverso dal primo elemento di $(1, 0)$. Invece abbiamo visto che $\{0, 1\} = \{1, 0\}$ perché in un insieme l'ordine e le ripetizioni non contano.

Più in generale, se n \ge 1
(x_1 x_2, . . . , x_n)
indica la n-upla (ossia una sequenza ordinata con n elementi) costituita dagli elementi x1, x2, . . . , xn.
Attenzione!
A differenza di quel che accade per gli insiemi, nelle n-uple ordinate contano sia l'ordine che eventuali ripetizioni.

Le n-uple vengono anche dette sequenze (di lunghezza n). Come notazione, spesso si scrive
$$
\langle x_1, x_2, \ldots, x_n \rangle
$$
al posto di (x1, . . . , xn), specialmente quando si considerano triple, quadruple e, più in generale, n-uple di lunghezza \ge 3.
%%

## 4.5 - Definizione: prodotto cartesiano di due insiemi

Dati due insiemi $A$ e $B$, si definisce ***prodotto cartesiano*** di $A$ e $B$ e si denota $A \times B$ l'insieme i cui elementi sono coppie di elementi con il primo elemento in $A$ e il secondo in $B$:
$$
A \times B = \{ (x, y) \mid x \in A \land y \in B \}
$$

### 4.5.1 - Esempio: prodotto cartesiano tra due insiemi

Dati due insiemi $A=\{1,2\}$ e $B=\{3,4,5\}$, si ha che il loro prodotto cartesiano è:
$$
A\times B=\{(1,3),(1,4),(1,5),(2,3),(2,4),(2,5)\}
$$

%%
\### Esempio: prodotto cartesiano tra due intervalli e relativa rappresentazione grafica

Dati due insiemi $A=\{x\mid 0\le x\le1\}$ e $B=\{x\mid -1\le x\le0\}$, %\%collegare a rappresentazione intervalli%\% rappresentabili anche con gli intervalli chiusi $A=[0,1]$ e $B=[-1,0]$, il loro prodotto cartesiano $A\times B$ è rappresentabile su un piano cartesiano come l'insieme di tutti i punti compresi tra il punto $\color{Red}A(0,1)$ e il punto $\color{Green}B(-1,0)$:

![[Prodotto cartesiano tra due intervalli e relativa rappresentazione grafica.png]]
Embeddare Geogebra o [Manim](https://www.manim.community/)
%%

### 4.5.2 - Osservazione: $\color{#888888}A \times \emptyset = \emptyset$

Il prodotto cartesiano tra un insieme $A$ e l'insieme vuoto $\emptyset$ è sempre pari all'insieme vuoto $\emptyset$:
$$
A \times \emptyset = \emptyset
$$

### 4.5.3 - Osservazione: $\color{#888888}A \ne \emptyset \land B \ne \emptyset \implies A \times B \ne \emptyset$

Il prodotto cartesiano tra due insiemi A e B non vuoti è sempre pari a un insieme non vuoto:
$$
A \ne \emptyset \land B \ne \emptyset \implies A \times B \ne \emptyset
$$
%%è corretta la scrittura logica?%%

### 4.5.4 - Osservazione: valenza geometrica del prodotto cartesiano

Se si interpreta l'insieme $\mathbb{R}$ dei numeri reali come una retta, allora il prodotto cartesiano $\mathbb{R}^2=\mathbb{R}\times\mathbb{R}$ è l'insieme formato da tutte le coppie $(x, y)$ di numeri reali:
$$
\mathbb{R}^2 = \{(x, y)\mid x \in \mathbb{R}\land y \in \mathbb{R}\}
$$
In altre parole, $\mathbb{R}^2$ non è nient'altro che il piano cartesiano, in cui un elemento di $\mathbb{R}^2$ è un punto identificato dalla coppia $(x, y)$; stesso discorso si può fare per l'insieme $\mathbb{R}^3$, ossia l'insieme che rappresenta lo spazio cartesiano in cui i punti sono identificati dalle tre coordinate $(x,y,z)$.

%%Esempio: rappresentazione grafica del prodotto cartesiano
![](Pasted%20image%2020240928175730.png)

Poiché i prodotti cartesiani sono costituiti da coppie ordinate, bisogna prestare attenzione al fatto che $A \times B$ è in genere distinto da $B \times A$ se $A \ne B$.
Ad esempio, se A = {0, 1, 2, 3} e B = {a, b, c}, allora la coppia (0, a) appartiene ad A \times B ma non a B \times A.
Se invece A = B, allora A \times B = B \times A: in questo caso, tale prodotto cartesiano viene indicato con $A^2$.%%

## 4.6 - Proposizione: cardinalità del prodotto cartesiano

Dati due insiemi finiti $A$ e $B$, con $|A| = m$ e $|B| = n$, allora la cardinalità del loro prodotto cartesiano $|A\times B|$ è uguale al prodotto delle loro cardinalità $m\cdot n$; se, invece, almeno uno tra $A$ e $B$ è infinito, allora anche $|A \times B|$ è infinito:
$$
|A| = m, |B| = n
\implies
|A \times B| = \begin{cases}
m \cdot n & \text{se } m, n \ne \infty \\
\infty & \text{se } m, n = \infty
\end{cases}
$$

### 4.6.1 - Dimostrazione

Se $A$ e $B$ sono finiti con $|A| = m$ e $|B| = n$, si possono numerare ed elencare i loro elementi come $A=\{a_1,a_2,...,a_m\}$ e $B=\{b_1,b_2,...,b_n\}$ e si possono organizzare gli elementi di $A \times B$ in una tabella:
$$
\begin{matrix}
(a_1, b_1) & (a_1, b_2) & \dots & (a_1, b_n) \\
(a_2, b_1) & (a_2, b_2) & \dots & (a_2, b_n) \\
\vdots & \vdots & \ddots & \vdots \\
(a_m, b_1) & (a_m, b_2) & \dots & (a_m, b_n)
\end{matrix}
$$
La tabella include chiaramente tutti gli elementi di $A \times B$ una volta sola e, quindi, devono essere $m \cdot n$ in totale, essendo $m$ in verticale ed $n$ in orizzontale. Il caso in cui uno degli insieme è infinito è chiaro, in quanto la tabella risulterà avere righe o colonne infinite.

$\blacksquare$

%%
vedere in che posto ficcare sta roba

Proposizione:
(A \cup B) \ (A \cap B) = (A \ B) \cup (B \ A)

Dimostrazione:
Poiché X \ Y = X \cap \complementY , l'identità pu`o essere riscritta come
(A \cup B) \cap \complement(A \cap B) = (A \cap \complementB) \cup (B \cap \complementA).
Quindi dobbiamo dimostrare che per ogni x
x \in (A \cup B) \cap \complement(A \cap B) \leftrightarrow x \in (A \cap \complementB) \cup (B \cap \complementA),
ovvero
(x \in A \lor x \in B) \land \lnot(x \in A \land x \in B) \leftrightarrow
(x \in A \land \lnot(x \in B)) \lor (x \in B \land \lnot(x \in A)).
Questa è una proposizione del tipo
(P \lor Q) \land \lnot(P \land Q) \leftrightarrow (P \land \lnotQ) \lor (Q \land \lnotP).
Usando le tavole di verità si verifica che tale proposizione è una tautologia,
quindi l'identità insiemistica proposta è corretta.

Lo stesso metodo può essere utilizzato anche per trovare controesempi quando una certa identità booleana non è valida.

Dimostrare (trovando un controesempio) che non vale l'identità
A \cap (B \cup C) = A \cup (B \cap C)
Dato un generico x, dobbiamo verificare che non è vero in generale che
x \in A \cap (B \cup C) \leftrightarrow x \in A \cup (B \cap C),
ovvero
x \in A \land (x \in B \lor x \in C) \leftrightarrow x \in A \lor (x \in B \land x \in C).
Questa è una proposizione del tipo
P \land (Q \lor R) \leftrightarrow P \lor (Q \land R),
dove P, Q e R sono, rispettivamente, "x \in A", "x \in B" e "x \in C".
![](Pasted%20image%2020240928182940.png)
%%


