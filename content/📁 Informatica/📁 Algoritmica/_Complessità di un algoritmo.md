---
draft: true
---
L'analisi della **complessità di un algoritmo** è uno degli aspetti chiave nello studio degli [algoritmi](Algoritmica.md), poiché consente di valutare le prestazioni e l'efficienza di un algoritmo rispetto al tempo di esecuzione (complessità temporale%%link%%) e allo spazio di memoria utilizzato (complessità spaziale%%link%%). L'obiettivo è capire come queste risorse variano in base alla dimensione dell'input (generalmente indicata con $n$).

%%
Se i computer fossero infinitamente veloci e la memoria dei computer fosse gra-
tuita, avremmo ancora qualche motivo per studiare gli algoritmi? La risposta `e
s`ı, se non altro perch´e vorremmo ugualmente dimostrare che il nostro metodo di
risoluzione termina e fornisce la soluzione esatta.
Se i computer fossero infinitamente veloci, qualsiasi metodo corretto per risol-
vere un problema andrebbe bene. Probabilmente, vorremmo che la nostra imple-
mentazione rispettasse le buone norme dell’ingegneria del software (ovvero fosse
ben progettata e documentata), ma il pi`u delle volte adotteremmo il metodo pi`u
semplice da implementare. Ovviamente, i computer possono essere veloci, ma
non infinitamente veloci. La memoria pu`o costare poco, ma non pu`o essere gra-
tuita. Il tempo di elaborazione e lo spazio nella memoria sono risorse limitate, che
devono essere saggiamente utilizzate; gli algoritmi che sono efficienti in termini
di tempo o spazio ci aiuteranno a farlo.
%%

# Notazione asintotica

## Notazione $\Theta$

Per una data funzione $g(n)$, indichiamo con $\Theta(g(n))$ l’insieme delle funzioni
$$
\Theta(g(n)) = \{
f(n)
\mid
\text{esistono delle costanti positive $c_1$, $c_2$ e $n_0$ tali che }
0 \le c_1g(n) \le f(n) \le c_2g(n) \text{ per ogni } n \ge n_0
\}
$$
Una funzione $f(n)$ appartiene all’insieme $\Theta(g(n))$ se esistono delle costanti positive $c_1$ e $c_2$ tali che essa possa essere compresa fra $c_1g(n)$ e $c_2g(n)$, per un valore sufficientemente grande di $n$.

![](Notazione%20Theta.png)

La figura presenta un quadro intuitivo delle funzioni $f(n)$ e $g(n)$, dove $f(n) = \Theta(g(n))$. Per tutti i valori di $n$ a destra di $n_0$, il valore di $f(n)$ coincide o sta sopra $c_1g(n)$ e coincide o sta sotto $c_2g(n)$. In altre parole, per ogni $n \ge n_0$, la funzione $f(n)$ è uguale a $g(n)$ a meno di un fattore costante. Si dice che $g(n)$ è un _limite asintoticamente stretto_ per $f(n)$.

La definizione di Θ(g(n)) richiede che ogni membro di f (n) ∈ Θ(g(n)) sia asintoticamente non negativo, ovvero che f (n) sia non negativa quando n `e sufficientemente grande (una funzione asintoticamente positiva `e positiva per qualsiasi valore sufficientemente grande di n). Di conseguenza, la funzione g(n) stessa deve essere asintoticamente non negativa, altrimenti l’insieme Θ(g(n)) `e vuoto.

Pertanto, supporremo che ogni funzione utilizzata nella notazione Θ sia asintoticamente non negativa. Questa ipotesi vale anche per le altre notazioni asintotiche definite in questo capitolo.

### Notazione: uguaglianza anziché appartenenza

Poiché $\Theta(g(n))$ è un insieme, potremmo scrivere "$f(n) \in \Theta(g(n))$" per indicare che $f(n)$ è un membro di $\Theta(g(n))$. Invece, di solito, scriveremo “$f(n) = \Theta(g(n))$” per esprimere lo stesso concetto. Questo abuso del simbolo di uguaglianza per denotare l’appartenenza a un insieme, inizialmente, potrebbe sembrare poco chiaro, ma vedremo più avanti che ha i suoi vantaggi.

### Ignorare le costanti e i gradi inferiori%%scrivere meglio qua%%

Nel Capitolo 2 abbiamo introdotto un concetto informale della notazione $\Theta$ che equivaleva a escludere i termini di ordine inferiore e a ignorare il coefficiente del termine di ordine più elevato. Giustifichiamo brevemente questa intuizione utilizzando la definizione formale per dimostrare che $\frac{1}{2} n^2 - 3n = \Theta(n^2)$.

Per farlo, dobbiamo determinare le costanti positive $c_1$, $c_2$ e $n_0$ in modo che
$$
c_1 n^2 \le \frac{1}{2} n^2 - 3n \le c_2 n^2
$$
per qualsiasi $n \ge n_0$. Dividendo tutto per $n^2$, si ha
$$
c_1 \le \frac{1}{2} - \frac{3}{n} \le c_2
$$
La disuguaglianza destra $c_2 \ge \frac{1}{2} - \frac{3}{n}$ può essere resa valida per qualsiasi valore di $n \ge 1$ scegliendo $c_2 \ge \frac{1}{2}$. Analogamente, la disuguaglianza sinistra $c_1 \le \frac{1}{2} - \frac{3}{n}$ può essere resa valida per qualsiasi valore di $n \ge 7$ scegliendo $c_1 \le \frac{1}{14}$.

Quindi, scegliendo $c_1 = \frac{1}{14}$, $c_2 = \frac{1}{2}$ e $n_0 = 7$, otteniamo $\frac{1}{14} \le \frac{1}{2} - \frac{3}{7}  = \frac{1}{14} \le \frac{1}{2}$ e possiamo verificare che $\frac{1}{2} n^2 - 3n = \Theta(n^2)$.

%%sistemare da qua in poi%%

Certamente `e possibile scegliere altri valori delle costanti, ma la cosa importante
`e che esiste qualche scelta. Notate che queste costanti dipendono dalla funzione
1
2 n2 − 3n; un’altra funzione che appartiene a Θ(n2), di solito, richiede costan-
ti differenti. Possiamo applicare anche la definizione formale per verificare che
6n3 = Θ(n2). Supponiamo per assurdo che esistano le costanti c2 e n0 tali che
6n3 ≤ c2n2 per ogni n ≥ n0; ma allora n ≤ c2/6 e questo non pu`o essere
assolutamente vero per n arbitrariamente grande, in quanto c2 `e costante.
Intuitivamente, i termini di ordine inferiore di una funzione asintoticamente
positiva possono essere ignorati nel determinare i limiti asintoticamente stretti,
perch´e sono insignificanti per grandi valori di n. Una piccola frazione del termine
di ordine pi`u elevato `e sufficiente a dominare i termini di ordine inferiore. Quin-
di, assegnando a c1 un valore che `e leggermente pi`u piccolo del coefficiente del
termine di ordine pi`u elevato e a c2 un valore che `e leggermente pi`u grande, `e pos-
sibile soddisfare le disuguaglianze nella definizione della notazione Θ. In modo
analogo, pu`o essere ignorato il coefficiente del termine di ordine pi`u elevato, in
quanto esso cambia soltanto c1 e c2 di un fattore costante pari al coefficiente.
Come esempio consideriamo una funzione quadratica f (n) = an2 +bn+c, do-
ve a, b e c sono costanti e a > 0. Escludendo i termini di ordine inferiore e ignoran-
do la costante, si ha f (n) = Θ(n2). Formalmente, per dimostrare la stessa cosa,
prendiamo le costanti c1 = a/4, c2 = 7a/4 e n0 = 2 · max((|b| /a), √(|c| /a)).
Il lettore pu`o verificare che 0 ≤ c1n2 ≤ an2 + bn + c ≤ c2n2 per ogni n ≥ n0. In
generale, per qualsiasi polinomio p(n) = ∑d
i=0 aini, dove i coefficienti ai sono
costanti e ad > 0, si ha p(n) = Θ(nd) (vedere Problema 3-1).
Poich´e qualsiasi costante `e un polinomio di grado 0, possiamo esprimere qual-
siasi funzione costante come Θ(n0) o Θ(1). Quest’ultima notazione, tuttavia, `e n abuso di second’ordine, perch´e non `e chiaro quale variabile tende all’infinito. 2 %%qua vedere nota 2 a pag. 36 del PDF%%
Adotteremo spesso la notazione Θ(1) per indicare una costante o una funzione
costante rispetto a qualche variabile.

## Notazione $O$

La notazione Θ limita asintoticamente una funzione da sopra e da sotto. Quando abbiamo soltanto un limite asintotico superiore, utilizziamo la notazione O. Per una data funzione g(n), denotiamo con O(g(n)) (si legge “O grande di g di n” o semplicemente “O di g di n”) l’insieme delle funzioni

O(g(n)) = {f (n) : esistono delle costanti positive c e n0 tali che 0 ≤ f (n) ≤ cg(n) per ogni n ≥ n0}

La notazione O si usa per assegnare un limite superiore a una funzione, a meno
di un fattore costante.

![](Notazione%20O.png)

La figura illustra il concetto intuitivo che sta dietro questa notazione. Per qualsiasi valore n a destra di n0, il valore della funzione f (n) coincide o sta sotto cg(n). Si scrive f (n) = O(g(n)) per indicare che una funzione f (n) `e un membro dell’insieme O(g(n)).

Notate che f (n) = Θ(g(n)) implica f (n) = O(g(n)), in quanto la notazione Θ `e una nozione pi`u forte della notazione O. Secondo la notazione della teoria degli insiemi possiamo scrivere Θ(g(n)) ⊆ O(g(n)).

Quindi, la nostra dimostrazione che qualsiasi funzione quadratica an2 + bn + c,
con a > 0, `e in Θ(n2) implica anche che tali funzioni quadratiche sono in O(n2).
Ci`o che pu`o sembrare pi`u sorprendente `e che qualsiasi funzione lineare an + b `e
in O(n2); questo `e facilmente verificabile ponendo c = a + |b| e n0 = 1.

### Diversa notazione di $O$

I lettori che hanno gi`a visto la notazione O potrebbero trovare strano che noi
scriviamo, per esempio, n = O(n2). Nella letteratura, la notazione O viene a vol-
te utilizzata informalmente per descrivere i limiti asintoticamente stretti, ovvero
ci`o che noi abbiamo definito con la notazione Θ. In questo libro, tuttavia, quando
scriviamo f (n) = O(g(n)), stiamo semplicemente affermando che qualche co-
stante multipla di g(n) `e un limite asintotico superiore di f (n), senza specificare
quanto sia stretto il limite superiore. La distinzione fra limiti superiori asintotici e
limiti asintoticamente stretti `e diventata standard nella letteratura degli algoritmi.

### Complessità degli algoritmi

Utilizzando la notazione O, spesso, `e possibile descrivere il tempo di esecuzio-
ne di un algoritmo, esaminando semplicemente la struttura complessiva dell’al-
goritmo. Per esempio, la struttura con i cicli doppiamente annidati dell’algoritmo
insertion sort del Capitolo 2 genera immediatamente un limite superiore O(n2)
sul tempo di esecuzione nel caso peggiore: il costo di ogni iterazione del ciclo in-
terno `e limitato superiormente da O(1) (costante), gli indici i e j sono entrambi al
massimo n; il ciclo interno viene eseguito al massimo una volta per ognuna delle
n2 coppie di valori i e j.

Poich´e la notazione O descrive un limite superiore, quando la utilizziamo per
limitare il tempo di esecuzione nel caso peggiore di un algoritmo, abbiamo un
limite sul tempo di esecuzione dell’algoritmo per ogni input. Quindi, il limite O(n2) sul tempo di esecuzione nel caso peggiore di insertion sort si applica anche
al suo tempo di esecuzione per qualsiasi input. Il limite Θ(n2) sul tempo di ese-
cuzione nel caso peggiore di insertion sort, tuttavia, non implica un limite Θ(n2)
sul tempo di esecuzione di insertion sort per qualsiasi input. Per esempio, abbia-
mo visto nel Capitolo 2 che, quando l’input `e gi`a ordinato, insertion sort viene
eseguito nel tempo Θ(n).
Tecnicamente, `e un abuso dire che il tempo di esecuzione di insertion sort `e
O(n2), in quanto, per un dato n, il tempo effettivo di esecuzione varia a seconda
del particolare input di dimensione n. Quando scriviamo “il tempo di esecuzione
`e O(n2)”, intendiamo dire che c’`e una funzione f (n) che `e O(n2) tale che, per
qualsiasi valore di n, indipendentemente da quale input di dimensione n venga
scelto, il tempo di esecuzione con quell’input `e limitato superiormente dal valo-
re f (n). In modo equivalente, intendiamo che il tempo di esecuzione nel caso
peggiore `e O(n2).

## Notazione $\Omega$

Cos`ı come la notazione O fornisce un limite asintotico superiore a una funzione,
la notazione Ω fornisce un **limite asintotico inferiore**. Per una data funzione g(n),
denotiamo con Ω(g(n)) (si legge “Omega grande di g di n” o semplicemente
“Omega di g di n”) l’insieme delle funzioni

Ω(g(n)) = {f (n) : esistono delle costanti positive c e n0 tali che 0 ≤ cg(n) ≤ f (n) per ogni n ≥ n0}

![](Notazione%20Omega.png)

Il concetto intuitivo che sta dietro la notazione Ω `e illustrato nella figura.
Per tutti i valori di n a destra di n0, il valore di f (n) coincide o sta sopra cg(n).
Dalle definizioni delle notazioni asintotiche che abbiamo visto finora, `e facile
dimostrare il seguente importante teorema (vedere Esercizio 3.1-5).

## Teorema

Per ogni coppia di funzioni f (n) e g(n), si ha f (n) = Θ(g(n)), se e soltanto se
f (n) = O(g(n)) e f (n) = Ω(g(n)).

Come esempio applicativo di questo teorema, la nostra dimostrazione che an2+
bn + c = Θ(n2) per qualsiasi costante a, b e c, con a > 0, implica immediata-
mente che an2 + bn + c = Ω(n2) e an2 + bn + c = O(n2). In pratica, anzich´e
usare il Teorema 3.1 per ottenere i limiti asintotici superiore e inferiore dai limiti
asintoticamente stretti, come abbiamo fatto per questo esempio, di solito lo usia-
mo per dimostrare i limiti asintoticamente stretti dai limiti asintotici superiore e
inferiore.

Poich´e la notazione Ω descrive un limite inferiore, quando la usiamo per li-
mitare il tempo di esecuzione nel caso migliore di un algoritmo, implicitamen-
te limitiamo anche il tempo di esecuzione dell’algoritmo con input arbitrari. Per
esempio, il tempo di esecuzione nel caso migliore di insertion sort `e Ω(n), che
implica che il tempo di esecuzione di insertion sort `e Ω(n).
Il tempo di esecuzione di insertion sort quindi `e compreso fra Ω(n) e O(n2), in
quanto si trova in una zona compresa tra una funzione lineare di n e una funzione
quadratica di n. Inoltre, questi limiti sono asintoticamente i pi`u stretti possibili:
per esempio, il tempo di esecuzione di insertion sort non `e Ω(n2), in quanto esiste
un input per il quale insertion sort viene eseguito nel tempo Θ(n) (per esempio,
quando l’input `e gi`a ordinato). Tuttavia, non `e contraddittorio affermare che il
tempo di esecuzione nel caso peggiore di insertion sort `e Ω(n2), in quanto esiste
un input con il quale l’algoritmo impiega un tempo Ω(n2). Quando diciamo che il
tempo di esecuzione di un algoritmo `e Ω(g(n)), intendiamo che indipendentemen-
te da quale particolare input di dimensione n sia scelto per qualsiasi valore di n,
il tempo di esecuzione con quell’input `e pari ad almeno una costante moltiplicata
per g(n), con n sufficientemente grande.

## Notazione asintotica nelle equazioni e nelle disuguaglianze

Abbiamo gi`a visto come la notazione asintotica possa essere utilizzata all’interno
di formule matematiche. Per esempio, presentando la notazione O, abbiamo scrit-
to “n = O(n2)”. Avremmo potuto scrivere anche 2n2 + 3n + 1 = 2n2 + Θ(n).
Come vanno interpretate queste formule?
Quando la notazione asintotica sta da sola sul lato destro di un’equazione (o
disuguaglianza), come in n = O(n2), abbiamo gi`a definito il segno uguale per
indicare l’appartenenza all’insieme: n ∈ O(n2). In generale, per`o, quando la no-
tazione asintotica appare in una formula, va interpretata come se indicasse qualche
funzione anonima, di cui non `e importante fare il nome. Per esempio, la formula
2n2 + 3n + 1 = 2n2 + Θ(n) significa che 2n2 + 3n + 1 = 2n2 + f (n), dove
f (n) `e qualche funzione dell’insieme Θ(n). In questo caso, f (n) = 3n + 1, che
appartiene effettivamente a Θ(n).
Utilizzando la notazione asintotica in questo modo, `e possibile eliminare detta-
gli superflui e poco chiari da un’equazione. Per esempio, nel Capitolo 2 abbiamo
espresso il tempo di esecuzione nel caso peggiore di merge sort come la ricorrenza
T (n) = 2T (n/2) + Θ(n)
Se siamo interessati soltanto al comportamento asintotico di T (n), non `e impor-
tante specificare con esattezza tutti i termini di ordine inferiore; `e sottointeso che
essi siano tutti inclusi nella funzione anonima indicata dal termine Θ(n).
Il numero di funzioni anonime in un’espressione `e sottointeso che sia uguale al
numero di volte che appare la notazione asintotica; per esempio, nell’espressione
$$
\sum_{i=1}^n = O(i)
$$
c’`e una sola funzione anonima (una funzione di i). Questa espressione non `e quin-
di la stessa cosa di O(1) + O(2) + · · · + O(n) che, in effetti, non ha una chiara
interpretazione.

In alcuni casi, la notazione asintotica si trova sul lato sinistro di un’equazione,
come in 2n^2 + Θ(n) = Θ(n^2)

Per interpretare simili equazioni, applichiamo la seguente regola: Indipendente-
mente dal modo in cui vengano scelte le funzioni anonime a sinistra del segno
uguale, c’`e un modo di scegliere le funzioni anonime a destra del segno uguale
per rendere valida l’equazione. Quindi, il significato del nostro esempio `e che per
qualsiasi funzione f (n) ∈ Θ(n), c’`e qualche funzione g(n) ∈ Θ(n2) tale che
2n2 + f (n) = g(n) per ogni n. In altre parole, il lato destro di un’equazione for-
nisce un livello di dettaglio pi`u grossolano del lato sinistro.

Simili relazioni potrebbero essere concatenate in questo modo
2n2 + 3n + 1 = 2n2 + Θ(n)
			= Θ(n2)

Applicando la precedente regola, possiamo interpretare separatamente le singole
equazioni. La prima equazione indica che esiste qualche funzione f (n) ∈ Θ(n)
tale che 2n2 + 3n + 1 = 2n2 + f (n) per ogni n. La seconda equazione indica che
per qualsiasi funzione g(n) ∈ Θ(n) (come la funzione f (n) appena citata), c’`e
qualche funzione h(n) ∈ Θ(n2) tale che 2n2 + g(n) = h(n) per ogni n. Notate
che questa interpretazione implica che 2n2 + 3n + 1 = Θ(n2), che `e quanto
intuitivamente indicano le equazioni concatenate.

%%
## Complessità temporale

La **complessità temporale** misura il tempo necessario per l'esecuzione di un algoritmo in relazione alla dimensione dell'input. Solitamente, si esprime in termini di notazione asintotica, ovvero:

- **O(n)** (Notazione Big-O): Esprime un limite superiore alla crescita del tempo di esecuzione nel caso peggiore. La complessità O(f(n)) indica che, per un input di dimensione $n$, il tempo di esecuzione è al più proporzionale a f(n) per $n$ grande.
  
  Esempi comuni:
  - **O(1)**: Tempo costante, indipendente dalla dimensione dell'input.
  - **O(n)**: Tempo lineare, cresce proporzionalmente alla dimensione dell'input.
  - **O(n^2)**: Tempo quadratico, tipico degli algoritmi di tipo brute-force che eseguono due cicli annidati.

- **Ω(n)** (Notazione Omega): Indica il limite inferiore della complessità temporale. Ovvero, l'algoritmo impiega almeno \( f(n) \) tempo in media o nel caso migliore.

- **Θ(n)** (Theta): Se un algoritmo ha sia complessità O(f(n)) che Ω(f(n)), allora si dice che ha complessità Θ(f(n)), indicando che la sua complessità è esattamente f(n).

#### Tipi di complessità temporale:
1. **Caso peggiore (Worst Case)**: Descrive il tempo massimo che un algoritmo potrebbe richiedere per un input di dimensione $n$. È la più comunemente utilizzata.
2. **Caso medio (Average Case)**: Calcola il tempo medio che l'algoritmo impiega per un input casuale di dimensione $n$.
3. **Caso migliore (Best Case)**: Rappresenta il tempo minimo che l'algoritmo potrebbe impiegare, solitamente poco rilevante, ma importante in alcuni casi (ad es. se l'input è già ordinato).

### 2. **Complessità Spaziale**
La **complessità spaziale** misura la quantità di memoria aggiuntiva richiesta dall'algoritmo rispetto alla dimensione dell'input. Come per la complessità temporale, anche la complessità spaziale può essere espressa tramite la notazione asintotica (Big-O, Ω, Θ).

Tipi di complessità spaziale:
- **Spazio fisso**: Quando la quantità di memoria utilizzata dall'algoritmo è indipendente dalla dimensione dell'input, ad esempio O(1).
- **Spazio variabile**: Se la memoria cresce con l'aumentare della dimensione dell'input, ad esempio O(n), l'algoritmo utilizza una quantità di memoria proporzionale all'input.

### 3. **Analisi Asintotica**
L'**analisi asintotica** studia il comportamento di un algoritmo per valori grandi dell'input, ignorando le costanti moltiplicative e i termini non dominanti. I tipi di notazione asintotica principali sono:

- **Big-O**: Stima il caso peggiore, dando un limite superiore.
- **Omega (Ω)**: Stima il caso migliore, fornendo un limite inferiore.
- **Theta (Θ)**: Quando un algoritmo ha sia limite superiore che inferiore definiti da f(n), si usa la notazione Θ.

### 4. **Esempio di Algoritmi e Complessità**
- **Ricerca lineare**: La complessità è O(n), poiché l'algoritmo deve scorrere tutti gli elementi di un array per trovare un elemento.
- **Ricerca binaria**: La complessità è O(log n), poiché riduce a metà l'input a ogni iterazione.
- **Ordinamento a bolle (Bubble Sort)**: La complessità è O(n^2), perché richiede l'ordinamento comparando ogni coppia di elementi.
- **Merge Sort**: Ha una complessità O(n log n), che è più efficiente rispetto ai metodi quadratici.

### 5. **Strategie di Analisi**
Alcune tecniche di analisi includono:
- **Somme aritmetiche e geometriche**: Utili per esprimere il costo di cicli nidificati.
- **Ricorrenze**: Spesso si utilizzano nelle analisi di algoritmi ricorsivi. Le ricorrenze descrivono la complessità di un problema dividendolo in sottoproblemi più piccoli, come nel caso del Merge Sort.
  
### 6. **Ottimizzazione dell'Algoritmo**
Lo scopo dell'analisi della complessità è spesso quello di ottimizzare l'algoritmo:
- **Ridurre la complessità temporale**: Cercare algoritmi con minore dipendenza dalla dimensione dell'input.
- **Bilanciare tempo e spazio**: Esistono algoritmi che migliorano il tempo di esecuzione a scapito dell'utilizzo di più memoria, e viceversa.

### Conclusione
L'analisi della complessità di un algoritmo è essenziale per scegliere o progettare soluzioni efficienti. L'uso della notazione asintotica consente di confrontare facilmente gli algoritmi e prevedere il loro comportamento su grandi input, fornendo una guida pratica nella scelta dell'algoritmo migliore per un problema specifico.
%%