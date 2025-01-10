---
draft: false
---
%%
In matematica (ed in informatica) `e spesso necessario dimostrare che una certa propriet`a `e vera per tutti i numeri naturali. Vediamo alcuni esempi.
1. $\forall n \in \mathbb{N} \left( \displaystyle\sum_{i=0}^n i = \frac{n(n+1)}{2} \right)$.
2. Per ogni $n \in \mathbb{N}$, $n^3-n$ è divisibile per $3$.
3. Per ogni $n \in \mathbb{N}$, il numero $16^{n+1}$ scritto in notazione decimale termina con la cifra $6$.

In ciascun caso si tratta di verificare che una certa proprietà $P(n)$ vale per tutti gli $n ∈ \mathbb{N}$.
L’esempio 1 fa parte di una tipologia più vasta di problemi.

Se una funzione $f: \mathbb{N} \to \mathbb{N}$ è definita ricorsivamente (es. $f(n+1) = \displaystyle\sum_{i=0}^{n+1} i = (\displaystyle\sum_{i=0}^n i) + (n+1) = f(n) + (n+1)$) ed $E(n)$ è una qualunque espressione aritmetica che contiene la variabile $n$ (es. $E(n) = \frac{n(n+1)}{2}$), verificare che $f(n) = E(n)$ per ogni $n$.

%%

# Principio di induzione semplice

> [!definizione]+ Definizione: principio di induzione semplice
> 
> Data una proprietà $P$%%link%% dei numeri naturali%% link %%, il **principio di induzione semplice** stabilisce che, se vengono rispettate le seguenti condizioni:
> 1. <font color="#FF8888">**Caso base**</font>: $P(0)$ è vera;
> 2. <font color="#8888FF">**Passo induttivo**</font>: assunta per vera $P(k)$ per un generico $k \in \mathbb{N}$ (_ipotesi induttiva_), risulta che $P(k+1)$ è vera (_tesi induttiva_);
> 
> allora la proprietà $P$%%link%% è vera per ogni $n \in \mathbb{N}$. In simboli:
> $$
> {\color{#FF8888} P(0) } \land {\color{#8888FF} \forall k \in \mathbb{N} (P(k) \implies P(k+1)) } \implies \forall n \in \mathbb{N} (P(n))
> $$

> [!osservazione]+ Osservazione: funzionamento del principio di induzione
> 
> Intuitivamente, il principio di induzione semplice si può giustificare come segue. Supponiamo che valgano ${\color{#FF8888} P(0) }$ e ${\color{#8888FF} \forall k \in \mathbb{N} (P(k) \implies P(k+1)) }$, allora:
> - ${\color{#FF8888} P(0) }$ vale perché è la prima ipotesi.
> - Poiché valgono ${\color{#FF8888} P(0) }$ per la prima ipotesi e ${\color{#8888FF} \forall k \in \mathbb{N} (P(k) \implies P(k+1)) }$ per la seconda ipotesi (applicata a $n = 0$), si ha per modus ponens%% link %% che vale ${\color{#88FF88} P(0+1) = P(1) }$.
> - Poiché valgono ${\color{#88FF88} P(1) }$ per il punto precedente e ${\color{#8888FF} \forall k \in \mathbb{N} (P(k) \implies P(k+1)) }$ per la seconda ipotesi (applicata a $n = 1$), si ha per modus ponens%% link %% che vale ${\color{#FFFF88} P(1+1) = P(2) }$.
> - Poiché valgono ${\color{#FFFF88} P(2) }$ per il punto precedente e ${\color{#8888FF} \forall k \in \mathbb{N} (P(k) \implies P(k+1)) }$ per la seconda ipotesi (applicata a $n = 2$), si ha per modus ponens%% link %% che vale ${\color{#FF88FF} P(2+1) = P(3) }$.
> 
> Proseguendo in questo modo, qualunque sia $k > 0$, arriveremo a dimostrare che deve valere $P(k)$ (poiché valeva $P(k-1)$, che a sua volta seguiva da $P(k-2)$, che a sua volta seguiva da $P(k-3)$ e così via, fino a $P(0)$). Dunque si ha che $P(k)$ vale per ogni $k \in \mathbb{N}$ come desiderato.

> [!esempio]+ Esempio
> 
> > [!proposizione] Proposizione
> > 
> > $$
> > \forall n \in \mathbb{N} \left( \sum_{i=0}^n i = \frac{n(n+1)}{2} \right) 
> > $$
> 
> > [!dimostrazione] Dimostrazione
> > 
> > Dimostriamo per induzione che $\forall n \in \mathbb{N} (P(n))$, dove $P(n)$ è l'uguaglianza $\displaystyle\sum_{i=0}^n i = \frac{n(n+1)}{2}$.
> > 1. Caso base: dobbiamo verificare $P(0)$, ovvero che $\displaystyle\sum_{i=0}^0 i = \frac{0(0+1)}{2}$:
> > $$
> > \left( \sum_{i=0}^0 i = 0 \right) \land \left( \frac{0(0+1)}{2} = 0 \right) \implies \sum_{i=0}^0 i = \frac{0(0+1)}{2}
> > $$
> > 2. Passo induttivo: dobbiamo dimostrare che $\forall n \in \mathbb{N} (P(n) \implies P(n+1) )$. Consideriamo un generico $n \in \mathbb{N}$ e assumiamo che valga $P(n)$ (cioè $\displaystyle\sum_{i=0}^n i = \frac{n(n+1)}{2}$) al fine di dimostrare $P(n+1)$ (cioè $\displaystyle\sum_{i=0}^{n+1} i = \frac{(n+1)(n+2)}{2}$):
> > $$
> > \begin{align*}
> > \sum_{i=0}^{n+1} i & = \sum_{i=0}^n i + (n+1) \\
> >  & = \frac{n(n+1)}{2} + (n+1) \\
> >  & = \frac{n(n+1) + 2(n+1)}{2} \\
> >  & = \frac{(n+1)(n+2)}{2}
> > \end{align*}
> > $$
> > %% per il raccoglimento %%
> > 
> > Avendo dimostrato sia il caso base $P(0)$ che il passo induttivo $\forall n \in \mathbb{N} (P(n) \implies P(n+1) )$, possiamo concludere che la proposizione è verificata.
> > 
> > $\blacksquare$

> [!esempio]+ Esempio
> 
> > [!proposizione] Proposizione
> > 
> > $$
> > \forall n \in \mathbb{N} \left( \sum_{i=0}^n 2i+1 = (n+1)^2 \right) 
> > $$
> 
> > [!dimostrazione] Dimostrazione
> > 
> > Dimostriamo per induzione che $\forall n \in \mathbb{N} (P(n))$, dove $P(n)$ è l'uguaglianza $\displaystyle\sum_{i=0}^n 2i+1 = (n+1)^2$.
> > 1. Caso base: dobbiamo verificare $P(0)$, ovvero che $\displaystyle\sum_{i=0}^0 2i+1 = (0+1)^2$:
> > $$
> > \left( \sum_{i=0}^0 2i+1 = 1 \right) \land \left( (0+1)^2 = 1 \right) \implies \sum_{i=0}^0 2i+1 = (0+1)^2
> > $$
> > 2. Passo induttivo: dobbiamo dimostrare che $\forall n \in \mathbb{N} (P(n) \implies P(n+1) )$. Consideriamo un generico $n \in \mathbb{N}$ e assumiamo che valga $P(n)$ (cioè $\displaystyle\sum_{i=0}^n 2i+1 = (n+1)^2$) al fine di dimostrare $P(n+1)$ (cioè $\displaystyle\sum_{i=0}^{n+1} 2i+1 = (n+2)^2$):
> > $$
> > \begin{align*}
> > \sum_{i=0}^{n+1} 2i+1 & = \left( \sum_{i=0}^{n} 2i+1 \right) + 2(n+1) + 1 \\
> >  & = (n+1)^2 + 2(n+1) + 1 \\
> >  & = (n+2)^2
> > \end{align*}
> > $$
> > %% per la formula del binomio %%
> > 
> > Avendo dimostrato sia il caso base $P(0)$ che il passo induttivo $\forall n \in \mathbb{N} (P(n) \implies P(n+1) )$, possiamo concludere che la proposizione è verificata.
> > 
> > $\blacksquare$

> [!osservazione] Osservazione: dimostrazione per induzione da $n > 0$
> 
> A volte si deve dimostrare che una proprietà $P(n)$ vale non per tutti i numeri naturali, ma solo da un certo $k$ in poi, cioè si deve dimostrare che $P(n)$ vale per ogni $n \ge k > 0$.
> 
> Dal punto di vista teorico, non è necessario introdurre un nuovo principio di induzione, dato che $\forall n \ge k ((P(n))$ è equivalente a $\forall m (Q(m))$, dove $Q(m)$ è $P(m+k)$. Dimostrare per induzione $\forall m (Q(m))$ equivale a:
> 1. Verificare il caso base $Q(0)$, cioè $P(k)$;
> 2. Dimostrare il passo induttivo: fissato un $m$ arbitrario, verificare che $Q(m) \implies Q(m+1)$, cioè $P(m+k) \implies P(m+k+1)$; in altre parole, fissato un $m \ge k$ arbitrario, dobbiamo verificare che $P(m) \implies P(m+1)$.

%%
$$
∀n ≥ 3 (2n + 1 < 2^n)
$$

Dimostrazione.
Base: $2 · 3 + 1 = 7 < 2^3$.
Passo induttivo. Supponiamo che $n ≥ 3$ e che $2n + 1 < 2^n$. Allora
$$
2(n + 1) + 1 = 2n + 1 + 2 < 2^n + 2 < 2^n + 2^n = 2^{n+1}
$$
%%

%% 
∀n ≥ 4 (2^n < n!).
Dimostrazione.
Base: 2^4 = 16 < 24 = 4! Passo induttivo: assumiamo 2^n < n!
2^{n+1} = 2^n · 2
< n! · 2 per ipotesi induttiva
< n! · (n + 1) perch´e n ≥ 4 e n! ≥ 1
= (n + 1)!
%%

%% 
∀n ≥ 1 (16^n termina con la cifra 6).
Dimostrazione.
Un numero naturale termina con la cifra k ∈ {0, 1, . . . , 9} se e solo `e della
forma i · 10 + k per qualche $i ∈ \mathbb{N}$.
Caso base: 16^1 = 16 termina con la cifra 6.
Passo induttivo. Supponiamo 16^n = i · 10 + 6. Allora
$$
16^{n+1} = (i · 10 + 6) · 16 = (i · 16) · 10 + 96 = (i · 16 + 9) · 10 + 6
$$
termina con la cifra 6.
%%

%% 
∀n ∈ N (n^3 − n `e divisibile per 3).
Dimostrazione.
Dimostriamo per induzione che ∀n ∈ N P (n) dove P (n) `e
∃k (n^3 − n = 3k).
Caso base: 0^3 − 0 = 0 = 3 · 0.
Passo induttivo: assumiamo P (n), cio`e n^3 − n = 3i per qualche i e
dimostriamo P (n + 1) cio`e (n + 1)^3 − (n + 1) = 3j per qualche j.
(n + 1)^3 − (n + 1) = n^3 + 3n^2 + 2n
= (n^3 − n) + 3n^2 + 3n
= 3i + 3(n^2 + n) per ip. ind.
= 3(i + n^2 + n)

quindi P(n + 1).
%%

%% 

![](Pasted%20image%2020250107174136.png)

![](Pasted%20image%2020250107174146.png)

%%

%%
# Un uso fallace dell’induzione

Consideriamo l’affermazione (falsa!)

> se n ≥ 2 e $l_1, l_2, . . ., l_n$ sono rette distinte del piano, a due a due non parallele, allora sono tutte incidenti in uno stesso punto.

Proviamo a “dimostrarla” per induzione.
Caso base
Se n = 2 abbiamo due rette non parallele del piano $l_1, l_2$ che sono
chiaramente incidenti.

Passo induttivo
Fissiamo $l_1, l_2, \ldots, l_n, l_{n+1}$ rette nel piano a due a due non parallele. Per ipotesi induttiva, $l_1, l_2, . . ., l_n$ sono incidenti in un punto $p$ e ℓ2, . . . , ℓn+1
sono incidenti in q. Allora ℓ2 e ℓn sono incidenti in p, e sono incidenti in q
e quindi p = q. Quindi ℓ1, . . . , ℓn, ℓn+1 passano per uno stesso punto.

Dov’`e il problema?

Il caso base è corretto, il passo induttivo NO!

Allora ℓ2 e ℓn sono incidenti in p e sono incidenti in q ✗ (funziona solo se
n > 2)

Il passo induttivo sarebbe corretto se assumessimo $n ≥ 3$, quindi se la propriet`a valesse per $n = 3$ allora  varrebbe per tutti gli $n ∈ \mathbb{N}$. Ma per $n = 3$ ci sono ovvi controesempi:
![](Pasted%20image%2020250107174605.png)
%%

# Principio di induzione forte

> [!definizione]+ Definizione: principio di induzione forte
> 
> Data una proprietà $P$%%link%% dei numeri naturali%% link %%, il **principio di induzione forte** stabilisce che, se vengono rispettate le seguenti condizioni:
> 1. <font color="#FF8888">**Caso base**</font>: $P(0)$ è vera;
> 2. <font color="#8888FF">**Passo induttivo**</font>: assunti per veri tutti i $P(0), P(1), \ldots, P(k)$ per un generico $k \in \mathbb{N}$ (_ipotesi induttiva_), risulta che $P(k+1)$ è vera (_tesi induttiva_);
> 
> allora la proprietà $P$%%link%% è vera per ogni $n \in \mathbb{N}$. In simboli:
> 
> $$
> {\color{#FF8888} P(0) } \land {\color{#8888FF} \forall k \in \mathbb{N} (P(0) \land P(1) \land \ldots \land P(k) \implies P(k+1)) } \implies \forall n \in \mathbb{N} (P(n))
> $$

%%
Osservazione: si dimostra che anche il principio di induzione forte è equivalente al principio di induzione semplice (e quindi anche al principio del minimo).
%%

%%
Esempio: Utilizziamo il principio di induzione forte per dare una nuova dimostrazione della seguente

Proposizione
Ogni numero naturale ≥ 2 ha una scomposizione in fattori primi.

Dimostrazione.
`E sufficiente dimostrare che, dato un generico n, se la propriet`a P (m) data da

> se m ≥ 2 allora m ha una scomposizione in fattori primi

vale per ogni m < n, allora vale anche P(n). Se n `e un numero primo non c’`e nulla da dimostrare, la sua scomposizione in fattori primi `e n stesso. Se invece n `e composto, allora n = m · l con 2 ≤ m, l < n. Poich´e m, l < n, sia m che l sono scomponibili in fattori primi, quindi anche n lo `e (la sua scomposizione `e il prodotto delle scomposizioni di m ed l).

$\blacksquare$
%%

# Principio di induzione strutturale semplice

Il principio di induzione può talvolta essere utilizzato per dimostrare proprietà universali per insiemi ([non necessariamente numerici](Insiemistica.md#^Osservazione-restrizioni-sulla-natura-degli-elementi-di-un-insieme)) “stratificati” in maniera opportuna. Il **principio di induzione strutturale semplice** è una tecnica utilizzata per dimostrare proprietà su oggetti definiti in modo ricorsivo o induttivo, come stringhe, alberi, o termini di linguaggi formali.

> [!definizione]+ Definizione: principio di induzione strutturale semplice
> 
> Data una proprietà $P$%%link%% su un [insieme](Insiemistica.md#^Definizione-insieme) della forma $A = \displaystyle\bigcup_{n ∈ \mathbb{N}} A_n$%% è un ricoprimento? %%, il **principio di induzione strutturale semplice** stabilisce che, se vengono rispettate le seguenti condizioni:
> 1. <font color="#FF8888">**Caso base**</font>: $P(a)$ è vera per ogni $a \in A_0$;
> 2. <font color="#8888FF">**Passo induttivo**</font>: per ogni $n \in \mathbb{N}$, assunta per vera $P(a)$ per un generico $a \in A_n$ (_ipotesi induttiva_), risulta che $P(a)$ vale per un generico $a \in A_{n+1}$ (_tesi induttiva_);
> 
> allora la proprietà $P$%%link%% è vera per ogni $a \in A$. In simboli:
> 
> $$
> {\color{#FF8888} \forall a \in A_0 (P(a)) } \land {\color{#8888FF} \forall n \in \mathbb{N} (\forall a \in A_n (P(a)) \implies \forall a \in A_{n+1} (P(a))) } \implies \forall a \in A (P(a))
> $$

%% 
Osservazione: Si dimostra che il principio di induzione strutturale semplice `e equivalente al principio di induzione.
%%

%% 
Esempio:
Vediamo un’applicazione del principio di induzione semplice.
Lemma
Per ogni sequenza di numeri naturali s = ⟨s1, . . . , sn⟩ di lunghezza n ≥ 2, se si < n − 1 per ogni 1 ≤ i ≤ n allora esistono $i \ne j$ tali che $s_i = s_j$.

Applichiamo il principio induzione strutturale semplice con
- $A$ l’insieme delle sequenze s = ⟨s1, . . . , sn⟩ di lunghezza n ≥ 2 tali che $s_i < n − 1$ per ogni 1 ≤ i ≤ n.
- $P$ è la proprietàLINK
> $P(s)$ se e solo se $s_i = s_j$ per qualche 1 ≤ i < j ≤ lh(s). (che cazzo è lh(s)?)

Vogliamo dimostrare che la propriet`a P vale per ogni s ∈ A. Sia
$A_n = \{s ∈ A \mid lh(s) = n + 2\}$, cosicch´e $A = \displaystyle\bigcup_{n ∈ \mathbb{N}} A_n$. Per il principio di
induzione strutturale semplice, `e sufficiente dimostrare che valgono le
condizioni 1 e  2.

![](Pasted%20image%2020250107191309.png)
%%

%% 

## Il principio dei cassetti

Abbiamo dimostrato che per ogni sequenza di numeri naturali
s = ⟨s1, . . . , sn⟩ di lunghezza n ≥ 2, se si < n − 1 per ogni 1 ≤ i ≤ n
allora esistono i̸ = j tali che si = sj . Da questo segue immediatamente il
%%

%%
Principio dei cassetti:
Se disponiamo n oggetti in k cassetti e 1 ≤ k < n, allora ci saranno
almeno due oggetti che finiranno nello stesso cassetto.
%%

%%
Dimostrazione:
Numeriamo i cassetti con i numeri da 0 a k − 1, e consideriamo la
sequenza ⟨s1, . . . , sn⟩ di lunghezza n, dove per ogni 1 ≤ i ≤ n definiamo

> s_i = il numero del cassetto in cui viene posto l’i-esimo oggetto.

Poich´e 1 ≤ k < n si ha n ≥ 2. Inoltre, si < k ≤ n − 1. Quindi esistono $i \ne j$ tali che si = sj , ovvero l’i-esimo oggetto e il j-esimo oggetto vengono riposti nello stesso cassetto.
$\blacksquare$
 %%

# Principio di induzione strutturale forte

Similmente, anche il principio di induzione forte può essere generalizzato.

> [!definizione]+ Definizione: principio di induzione strutturale forte
> 
> Data una proprietà $P$%%link%% su un [insieme](Insiemistica.md#^Definizione-insieme) della forma $A = \displaystyle\bigcup_{n ∈ \mathbb{N}} A_n$%% è un ricoprimento? %%, il **principio di induzione strutturale semplice** stabilisce che, se vengono rispettate le seguenti condizioni:
> 1. <font color="#FF8888">**Caso base**</font>: $P(a)$ è vera per ogni $a \in A_0$;
> 2. <font color="#8888FF">**Passo induttivo**</font>: per ogni $n \in \mathbb{N}$, assunta per vera $P(a)$ per ogni $a \in \displaystyle\bigcup_{k=0}^{n} A_k$ (_ipotesi induttiva_), risulta che $P(a)$ vale per ogni $a \in A_{n+1}$​ (_tesi induttiva_);
> 
> allora la proprietà $P$%%link%% è vera per ogni $a \in A$. In simboli:
> 
> $$
> {\color{#FF8888} \forall a \in A_0 (P(a)) } \land {\color{#8888FF} \forall n \in \mathbb{N} \left( \forall a \in \bigcup_{k=0}^{n} A_k (P(a)) \implies \forall a \in A_{n+1} (P(a)) \right) } \implies \forall a \in A (P(a))
> $$

%% 
Nel **principio di induzione strutturale forte**, l'ipotesi induttiva non si limita a considerare un singolo elemento $a \in A_n$, ma coinvolge **tutti gli elementi precedenti** appartenenti a $\bigcup_{k=0}^{n} A_k$​. Questo è utile quando la dimostrazione per $P(a)$ in $A_{n+1}$ richiede informazioni su più di un livello precedente della struttura.
%%

%% 
Osservazione: Si dimostra che il principio di induzione strutturale forte `e equivalente al principio di induzione forte (e quindi anche al principio di induzione).
%%

%% 
Vedremo un esempio di applicazione del principio di induzione strutturale forte quando studieremo la sintassi della logica proposizionale.
Per ora ci basta osservare che in generale questo principio (come anche la sua versione semplice) si pu`o utilizzare ogni volta che si costruisca un insieme A definendo per ricorsione:
- un insieme A0 di oggetti “di base”,
- una regola che dica come costruire gli oggetti in An+1 a partire dagli oggetti in An o nei livelli precedenti,
e si ponga infine $A = \displaystyle\bigcup_{n \in \mathbb{N}} A_n$.
%%

%% 
Quindi questi cinque principi sono tra loro equivalenti:
Principio di induzione (semplice) 
Principio del minimo 
Principio di induzione forte
Principio di induzione strutturale semplice 
Principio di induzione strutturale 
%%

%% 
# Alice, Bob e la tavoletta di cioccolato

![](Pasted%20image%2020250110002448.png)

Alice e Bob a turno staccano a turno pezzi di cioccolata con la seguente regola: quando si sceglie un quadretto, bisogna prendere anche tutti quelli a destra e sopra di esso. Chi prende l’ultimo quadretto in basso a sinistra perde.

Una strategia vincente per Alice `e un programma che dice come fare la prima mossa e poi dice come rispondere alle mosse di Bob e tale che alla fine della partita Alice vince:

> ∃ mossa di Alice ∀ mossa di Bob ∃ mossa di Alice ∀ mossa di Bob . . . Alice vince.

Una strategia vincente per Bob `e un programma che dice come rispondere alle mosse di Bob e tale che alla fine della partita Bob vince.

> ∀ mossa di Alice ∃ mossa di Bob ∀ mossa di Alice ∃ mossa di Bob . . . Bob vince.

Visto che il gioco termina in un numero finito (≤ nm) di mosse, uno e uno solo tra Alice e Bob ha una strategia vincente.
Chi dei due ha una strategia vincente?

Se n ≥ 2, Alice ha una strategia vincente per n × 1 .
Consideriamo una tavoletta della forma n × 1:
![](Pasted%20image%2020250110002624.png)
Alice prende tutti i quadretti, lasciando l’ultimo a Bob.

Se n ≥ 2, Alice ha una strategia vincente per n × 2.
Infatti dimostreremo per induzione su n ≥ 1 che
data una tavoletta della forma n × 2

CONTINUARE FINO ALLA FINE DELLE SLIDE

%%

