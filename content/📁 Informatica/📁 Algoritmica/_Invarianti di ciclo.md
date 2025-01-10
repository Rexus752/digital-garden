---
draft: true
---

# Correttezza di programmi contenenti un ciclo e invarianti di ciclo

Consideriamo il problema di calcolare il quoziente $q$ ed il resto $r$ della divisione tra due numeri interi $X \ge 0$ e $D > 0$.

Per definizione di quoziente e resto, si ha $X = q · D + r$ con $r < D$, da cui $X − q · D = r$. Quindi per determinare $q$ e $d$ bisogna calcolare quante volte si pu`o sottrarre $D$ da $X$ (questo ci d`a $q$), e ci`o che rimane dopo l’ultima sottrazione `e il resto $r < D$.
Questa osservazione ci fornisce un algoritmo per il calcolo della divisione implementabile su un computer: tale algoritmo consiste nel sottrarre ripetutamente $D$ a $X$, aumentando ogni volta di $1$ il valore di $q$ che inizialmente ha valore $0$. Schematicamente, l’algoritmo `e il seguente:
> [!algoritmo] Algoritmo della divisione per sottrazioni successive
> 1. Inizializza le variabili ausiliarie $r$ e $q$ ponendo $r = X$ e $q = 0$.
> 2. Fino a quando $r ≥ D$ esegui le seguenti azioni:
> 	1. Sottrai $D$ a $r$.
> 	2. Aumenta $q$ di $1$.
> 3. Quando $r < D$, dai come output i valori correnti di $q$ (quoziente) e $r$ (resto).

Un programma Java che realizza questo algoritmo `e il seguente:
```
class divisione {
	public static void main (String[] args) {
		int X, D, q, r;
		X = ? ; // inizializzazione
		D = ? ; // inizializzazione
		q = 0;
		r = X;
		while (r >= D) {
			r = r - D;
			q = q + 1;
		}
		System.out.println ("Il quoziente `e: " + q);
		System.out.println ("Il resto `e: " + r);
	}
}
```

Come si pu`o dimostrare che il programma precedente `e corretto?

Prima di tutto:
La condizione di ingresso del programma, cio`e la propriet`a che i dati in
ingresso X e D devono soddisfare, `e che:

> X ≥ 0 e D > 0

(La seconda propriet`a serve ad evitare casi di divisione per 0.)

La condizione di uscita del programma, cio`e la propriet`a che i dati in uscita q
ed r devono soddisfare, `e che

> X = q ∗ D + r, con r < D.

Questa propriet`a dice proprio che q ed r sono, rispettivamente, il
quoziente ed il resto della divisione intera di X per D.
La correttezza del programma (qualche volta si parla di questa condizione
come di correttezza parziale) asserisce che:

> Per ogni dato in ingresso che soddisfa la condizione di ingresso, se il programma termina, allora i dati in uscita soddisfano la condizione di uscita.

Una condizione pi`u esigente di correttezza `e quella che si chiama correttezza totale:
> Per ogni dato in ingresso che soddisfa la condizione di ingresso, certamente il programma termina e i dati in uscita soddisfano la condizione di uscita.

Per stabilire che un programma soddisfa la specifica vi sono vari modi, ma la tecnica pi`u conveniente consiste nel trovare quello che si chiama un invariante (di ciclo):

Un invariante (di un ciclo) `e una propriet`a che lega (tutte o alcune del)le
variabili coinvolte nel ciclo, e che `e vera dopo un numero arbitrario di
iterazioni del ciclo. In particolare, `e vera anche all’ingresso nel ciclo (cio`e
dopo 0 iterazioni).

Ci sono molte propriet`a invarianti del ciclo
```c
while (r >= D) {
	r -= D;
	q++;
}
```
per esempio la propriet`a q ≥ 0. Tuttavia tra tutte le possibili propriet`a ce
ne sono alcune che sono pi`u interessanti di altre, nel nostro caso:
$X = q \cdot D + r$.
In effetti, se il ciclo termina abbiamo che r < D (condizione di uscita del ciclo): quindi se $X = q \cdot D + r$ `e effettivamente un invariante, avremo che tale condizione vale anche all’uscita del ciclo (indipendentemente dal numero di cicli eseguiti), e quindi le condizioni di uscita saranno soddisfatte. Avremmo cos`ı dimostrato la correttezza parziale del programma che stiamo analizzando.

L’uso di un opportuno invariante di ciclo ci permette quindi di dimostrare che il programma `e parzialmente corretto: bisogna per`o ancora dimostrare che la propriet`a $X = q \cdot D + r$ `e proprio invariante di ciclo! Questo si pu`o fare per induzione sul numero $n$ di iterazioni del ciclo. Verificheremo quindi il caso base, cioè con $n = 0$ iterazioni, e il passo induttivo, cioè che se la propriet`a vale dopo $n$ iterazioni, allora continua a valere anche dopo $n + 1$ iterazioni (ovvero dopo che il ciclo `e stato nuovamente eseguito)

Caso base: 0 iterazioni
Se il ciclo non `e ancora eseguito si ha che q = 0 (perch´e q non viene
incrementato) e r = X. Allora X = q ∗ D + r perch´e questo si riduce a
dire che X = 0 ∗ D + X, che `e ovviamente vero.

Supponiamo che valga

> Ipotesi induttiva
> La propriet`a X = q ∗ D + r `e vera dopo che il ciclo `e stato eseguito n volte.

Vogliamo dimostrare che la propriet`a resta vera anche dopo la (n + 1)-esima iterazione (ovvero dopo una nuova esecuzione del ciclo). Durante questa nuova iterazione vengono modificati i valori di q e di r, ottenendo valori
q′ = q + 1
r′ = r − D
dove q′ ed r′ sono i valori delle variabili q ed r dopo l’esecuzione delle
istruzioni
`r -= D;`
`q++;`

Vogliamo dimostrare che X = q′ ∗ D + r′ (che `e la nostra tesi induttiva).
Eseguendo i calcoli si ottiene
q′ ∗ D + r′ = (q + 1) ∗ D + (r − D)
= q ∗ D + D + r − D
= q ∗ D + r
= X
dove l’ultimo passaggio sfrutta l’ipotesi induttiva.
Per il principio di induzione, si conclude allora che la propriet`a
X = q ∗ D + r
e vera per qualsiasi numero di iterazioni del ciclo, quindi `e veramente un
invariante di ciclo.

Se vogliamo dimostrare la correttezza totale del programma precedente,
dobbiamo ora mostrare che se le condizioni di ingresso X ≥ 0 e D > 0
sono soddisfatte, allora il programma termina certamente. Questo vuol dire
che il programma non va in loop: il ciclo non viene eseguito all’infinito, ma
dopo un numero finito di iterazioni la condizione di uscita dal ciclo r < D
viene soddisfatta e il programma termina eseguendo l’ultima istruzione.

Per dimostrare ci`o, basta osservare che ad ogni iterazione a r viene
sottratto il valore D che, per la condizione di ingresso, `e un numero > 0:
quindi prima o poi deve accadere che r < D, che `e proprio la condizione di
uscita dal ciclo.

Osservazione
Il fatto che sottraendo a r una quantit`a non nulla D si debba prima o poi
avere r < D segue dal fatto che non ci sono successioni discendenti
infinite di numeri naturali, ovvero successioni infinite della forma
n0 > n1 > n2 > n3 > . . .. Vedremo tra poco che questo fatto `e
equivalente al cosiddetto principio del minimo, che a sua volta `e
equivalente al principio di induzione stesso.

# Il principio del minimo

C’`e un altro principio fondamentale per ragionare sui numeri naturali:

Principio del minimo:
> [!definizione] Definizione: principio del minimo
> 
> Se una propriet`a%% link %% $P$ `e vera per qualche numero naturale, allora c’`e un minimo numero naturale $n$ per il quale vale $P$.

Dire che n `e il minimo per il quale la propriet`a P vuole dire che P (n) ma per ogni k < n si ha ¬P (k). Il principio del minimo si pu`o riformulare equivalentemente come

> Ogni insieme A ⊆ N non vuoto ha un elemento minimo rispetto a ≤.

Importante! Si dimostra che il principio di induzione e il principio del minimo sono
equivalenti: da ciascuno dei due principi si pu`o derivare l’altro, quindi in
un certo senso sono due formulazioni diverse dello stesso principio.

Vediamo ora un’esempio di applicazione del principio del minimo.

> [!proposizione] Proposizione
> 
> Ogni numero naturale maggiore o uguale a $2$ ha una scomposizione in fattori primi.

> [!dimostrazione] Dimostrazione
> 
> Per assurdo, sia n ≥ 2 tale da non avere una scomposizione in fattori primi. Per il principio del minimo, possiamo supporre che n sia il minimo
> numero con questa propriet`a. Ci sono due casi:
> 1. n `e primo: allora n ha una scomposizione in fattori primi, assurdo.
> 2. n `e composto: sia n = m · l, dove 2 ≤ m, l < n. I numeri m e l devono avere una scomposizione in fattori primi, perch´e n `e il minimo che non ce l’ha: quindi anche n ha una scomposizione, che si ottiene componendo in modo opportuno le scomposizioni di m e l, assurdo.
> 
> In entrambi i casi abbiamo contraddetto l’ipotesi che ci sia un numero naturale che non ha scomposizione in fattori primi, quindi abbiamo dimostrato la proposizione.
> 
> $\blacksquare$

Una conseguenza fondamentale del principio del minimo `e la seguente.
La relazione < su N `e ben fondata, ovvero in N non esiste alcuna
successione discendente infinita della forma
n0 > n1 > n2 > . . .
La ben fondatezza di < `e in realt`a equivalente al principio del minimo.

Infatti, se esistesse una successione discendente n0 > n1 > n2 > . . . l’insieme
A = {n0, n1, n2, . . .} non avrebbe un minimo elemento, contraddicendo il
principio del minimo.
Viceversa, supponiamo che < sia ben fondata ma che per assurdo fallisca il
principio del minimo, ovvero che esista A ⊆ \N non vuoto e senza un elemento
minimo rispetto a ≤. Definiamo per ricorsione la successione n0, n1, n2, . . . di
elementi di A come segue. Sia n0 un qualunque elemento di A (c’`e almeno una
scelta per n0 perch´e A̸ = ∅). Definiamo nk+1 come il pi`u grande elemento
nell’insieme {n ∈ A | n < nk} (tale insieme `e non vuoto perch´e altrimenti nk
sarebbe il minimo di A). Per costruzione si ha che n0 > n1 > n2 > . . .,
contraddicendo il fatto che < sia ben fondata.

L’uso del principio del minimo in matematica `e frequente. Ad esempio,
viene implicitamente utilizzato ogni volta che in qualche dimostrazione si
usano espressioni del tipo

> Sia n ∈ N il minimo tale che. . .

Un esempio di ci`o `e la dimostrazione vista in precedenza del fatto che ogni
numero naturale maggiore o uguale a 2 ammette una scomposizione in
fattori primi.

In informatica, l’importanza del principio del minimo risiede nel fatto che
la ben fondatezza della relazione < sui numeri naturali pu`o essere
utilizzata per dimostrare la terminazione di programmi. Implicitamente
questa propriet`a era gi`a stata utilizzata, per esempio, nella dimostrazione
della correttezza totale del programma per la divisione intera.

Per dimostrare che un programma contenente un ciclo termina (ovvero che
dopo un certo numero di iterazioni del ciclo, che dipender`a dall’input
iniziale, si esce dal ciclo) si pu`o procedere come segue:

> Si assegna ad ogni configurazione di valori c assunti dalle corrispondenti
> variabili del programma un numero naturale T (c). Tale scelta va fatta in
> modo che se eseguendo le istruzioni del ciclo il programma passa da una
> configurazione c ad una configurazione c′, allora T (c) > T (c′). In altre
> parole, deve accadere che il numero T (c) diminuisca ogni volta che viene
> eseguita una nuova iterazione del ciclo.
> Fatto questo, si pu`o immediatamente concludere che il ciclo deve
> terminare: se cos`ı non fosse, si otterrebbe una successione discendente
> infinita
> T (c) > T (c′) > T (c′′) > T (c′′′) > . . .
> contraddicendo la ben fondatezza di < su N (ovvero il principio del
> minimo).

Consideriamo nuovamente il ciclo
```c
while (r >= D) {
	r -= D;
	q ++;
}
```

Una configurazione $c$ `e la sequenza dei valori assunti dalle variabili del
programma in un dato istante, ovvero $c = ⟨X, D, q, r⟩$ (si ricordi che,
anche se non compare esplicitamente nel ciclo, nel programma c’era anche
la variabile $X$). Durante una iterazione del ciclo, si passa da una
configurazione c = ⟨X, D, q, r⟩ ad una configurazione c′ = ⟨X′, D′, q′, r′⟩
dove X′ = X, D′ = D, q′ = q + 1 e r′ = r − D. Poniamo allora T (c) = r:
in questo modo, nel passare da c a c′ si ha
T (c) = r > r′ = T (c′)
poich´e D > 0 (condizione di ingresso del programma). Per il principio del
minimo, il fatto che T (c) decresca ad ogni iterazione del ciclo garantisce
che per qualunque input iniziale che soddisfi le condizioni di ingresso del
programma si esca dal ciclo dopo un numero finito di iterazioni.

# Provare un invariante

![](Pasted%20image%2020250109164945.png)

Invariante: $x \le z \land y = x^2$

1. Dimostrare che è verificato prima di entrare nel ciclo (es. "prima di entrare nel ciclo $x = 0, y = 0$ e $z \ge 0$ dalla precondizione, da cui otteniamo $x = 0 \le 0 = z$ e $0 = 0^2$".
2. Dimostrare che è verificato in una esecuzione generica del ciclo. Es. "Assumiamo che $x < z$ e che appena entrati nel ciclo abbiamo $y = x^2$. Denotiamo con $x'$ e $y'$ i nuovi valori di $x$ e $y$ a fine ciclo. Abbiamo $x < z \implies x'= x + 1 < z'$ e $y = x^2 \implies y' = y + 2x + 1 =$ (sostituendo $y$ con $x^2$) $x^2 + 2x + 1 = (x + 1)^2$ da cui, per la proposizione precedente, $x'^2$.
3. Dimostrare che all'uscita del ciclo è verificato $\lnot(x < z)$, quindi significa che $x = z$. Insieme all'invariante $y = x^2$, abbiamo $y = x^2 = z^2$.

# Invariante nella ricorsione

Si chiama "ipotesi induttiva" e va fatta sul valore di ritorno (es. sulla riga del "return") e deve valere quando il valore viene restituito.

%% 

## Invariante di ciclo in Logica

Consideriamo un frammento di codice della forma:
```
while (b)
	S;
```

Se $P$ `e una proposizione che esprime una relazione tra i valori delle variabili che compaiono nell’istruzione $S$, allora si pu`o definire un’altra propriet`a dei numeri naturali $Q$ ponendo:

> $Q(n) ↔ P$ `e vera dopo n iterazioni del ciclo while.

e si pu`o poi cercare di dimostrare che $Q(n)$ `e vera per ogni $n ∈ \mathbb{N}$.

Propriet`a di questo tipo sono utilizzate per stabilire che $P$ `e una propriet`a invariante del ciclo in questione, ovvero un invariante di ciclo.

%%

# Fonti

- Slide del Prof. Viale Matteo del corso di Logica Matematica (canale B), Corso di Laurea in Informatica presso l'Università di Torino, A.A. 2024-25:
	- [3.1 - Le Diverse Forme del Principio di Induzione_moodle.pdf](https://informatica.i-learn.unito.it/pluginfile.php/417200/mod_folder/content/0/3.1%20-%20Le%20Diverse%20Forme%20del%20Principio%20di%20Induzione_moodle.pdf)
