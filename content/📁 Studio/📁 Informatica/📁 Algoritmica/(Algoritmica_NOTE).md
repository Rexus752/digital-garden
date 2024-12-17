---
draft: true
---
# I fantastici 9

libro divulgativo uscito qualche anno fa sugli algoritmi: alla base delle applicazioni comuni che utilizziamo tutti i giorni ci sono algoritmi .
1. Indicizzazione: insieme di tecniche per riconoscere contenuto di una pagina web senza doverlo archiviare tutto
2. Page rank: più noti algoritmi di raccomandazione, usati per piattaforme che distribuiscono contenuti
3. Crittografia a chiave pubblica: es. RSA, sono protocolli =/= algoritmi, ma i protocolli utilizzano algoritmi
4. Codici a correzione d'errore: algoritmi che servono per assicurare che la trasmissione dei dati sia senza errore.
5. ecc.
9. Verificatore di programmi: algoritmo fantasma, teorema: tutti i problemi di decisione che riguardino semantica dei programmi sono indecidibili (eccetto quelli triviali). Non esiste un verificatore, ma esistono sistemi che servono per verificarli.

# Problemi computazionali

Un problema computazionale è una relazione ingresso-uscita, dove l'ingresso e l'uscita sono discreti, finiti ecc., con relazione definibile in modo finito.

es. MCD:
Ingressi: coppie di interi a,b non entrambi nulli
Uscite: un intero c tale che:
- c divide sia a che b
- se d divide a e b, allora d divide c

Non prendiamo in ingresso 0,0 perché 0 è multiplo di qualsiasi altro numero, infatti $0 = x \cdot 0$ per qualsiasi $x$, quindi non ha un massimo.

## Esempi

Funzioni aritmetiche sono problemi computazionali perché sono relazioni ingresso-uscita:
- Moltiplicazione
- Fattorizzazione
- Ordinamento (sorting)
- Ordinamento topologico (topological sorting)
- Percorso ottimo (shortest path)

## Definizione

Un problema è una relazione (binaria) del tipo
R = {(istanza, risposta) | istanza, risposta soddisfano ...}
le cui istanze sono in
dom(R) = {i | exists r t.c. (i,r) in R}

istanze = casi particolari
risposta = non è necessario che sia univoca

## Univocità

- Moltiplicazione: sì
- Fattorizzazione: sì (ma a meno dell'ordine)
- Ordinamento (sorting): sì (ma no se permutazione)
- Ordinamento topologico: NO
- Percorso ottimo: NO

# Algoritmo

Algoritmo = soluzione meccanica di un problema computazionale

Procedura = guida finita composta da operazioni elementari eseguibili da un automa finito e concatenate in un determinato flusso. Deve essere determinatistica.

L'algoritmo è una procedura che termina per ogni ingresso ammissibile.

Un algoritmo è corretto rispetto ad un problema computazionale se associa ad ogni istanza del problema un'uscita che ne soddisfi il criterio di correttezza.

## Primo algoritmo: calcolo del MCD

Settimo libro degli Elementi di Euclide, è una presentazione assiomatica della geometria, non dell'aritmetica. E allora se MCD è aritmetico, perché nella geometria? Perché MCD è rapporto tra segmenti/aree, si può rappresentare geometricamente.

Algoritmo classico:
- Scomposizione in fattori primi
- Scelta dei fattori primi comuni con il minimo esponente
- Moltiplicazione
- Ottenuto MCD

Algoritmo diverso da quello di Euclide, ma notevolmente più inefficiente, perché comprende il passo della fattorizzazione in primi che è un problema risolvibile ma poco efficiente, infatti è talmente inefficiente che proprio la fattorizzazione viene sfruttata in crittografia.

Algoritmo di Euclide: problema di tassellamento, cioè dato un pavimento, trovare una dimensione di mattonelle quadrate che copra tutta l'area senza tagliarle ma con il minor numero possibile. Come si fa:
- Prendere il lato minore e usare mattonelle con dimensione questo lato. Avanzerà spazio, procedere allo stesso modo dell'originale.
- Questa è un metodo ricorsivo, cioè riduce il problema a uno omogeneo (cioè della stessa specie) ma di taglia minore.
- Continua finché non trova una mattonella che non lascia il resto. L'ultima mattonella inserita è la dimensione del tassellamento.
- Si può fare anche con mattonelle più piccole (anche da 1), ma si cerca quella migliore possibile, cioè con minor numero di mattonelle da piazzare.

Scritto in termini matematici:
- $MCD(a,0) = a$
- $MCD(a,b) = MCD(b, a \bmod b)$ se $b > 0$.
Applicando più volte la seconda equazione, arrivo alla prima.

$$
\displaylines{
\begin{align*}
 & \textbf{Euclid}(a, b) \quad \rhd a > 0 \lor b > 0 \\
 & \textrm{if } b = 0 \textrm{ then} \\
 & \quad \textrm{return } a \\
 & \textrm{else} \\
 & \quad r \gets a \bmod 5 \\
 & \quad \textrm{while } r \ne 0 \textrm{ do} \\
 & \quad\quad a \gets b \\
 & \quad\quad b \gets r \\
 & \quad\quad r \gets a \bmod b \\
 & \quad \textrm{end while} \\
 & \quad \textrm{return } b \\
 & \textrm{end if}
\end{align*}
}
$$

Il calcolo di MCD(a,b) con Euclide richiede tempo O(log a) (supponendo a>b), mentre la fattorizzazione di a richiede tempo $O(\sqrt a)$.

# Differenza programma-algoritmo

- Un programma può essere composto da diversi algoritmi
- Un programma è scritto in uno specifico linguaggio di programmazione, un algoritmo è una descrizione generica del procedimento (spesso in pseudocodice)
- In un programma occorre specificare ed implementare opportune strutture dati
- Programma può anche non terminare mai
- Programma concreto, algoritmo astratto

Niklaus Emil Wirth: "Algorithms + Data Structures = Programs"

# Solubilità dei problemi

Problemi solubili hanno infiniti algoritmi per risolverli, ma solo alcuni sono quelli più efficienti.

## Esempio: peak finding

Picchi = punti in cui i punti a destra o sinistra non sono più in alto.

Input: un vettore $A[0, \ldots, n-1]$ di interi positivi
Output: un intero $0 \le p < n$ tale che $A[p-1] \le A[p] \ge A[p+1]$ dove $A[-1] = A[n] = -\infty$.

Per far sì che funzioni anche agli estremi (quindi a $A[0]$ e $A[n-1]$, poniamo $A[-1] = A[n] = -\infty$ (andava bene anche $=-1$ dato che sono interi positivi)).

### Picco massimo

$$
\displaylines{
\begin{align*}
 & \textbf{Peak-Find-Max}(A, n) \quad \rhd n \ge 1 \\
 & p \gets 0 \\
 & \textrm{for } k \gets 1 \textrm{ to } n-1 \textrm{ do} \\
 & \quad \textrm{if } A[p] < A[k] \textrm{ then} \\
 & \quad\quad p \gets k \\
 & \quad \textrm{end if} \\
 & \textrm{end for} \\
 & \textrm{return } p
\end{align*}
}
$$

Se $A[p]$ è il massimo in $A[0,\ldots,n-1]$, allora $p$ è il picco più alto
In tutti i casi si effettuano $n-1$ confronti.

### Picco qualunque

È possibile trovare un picco qualunque in minor tempo?

Soluzione del programmatore furbo:
$$
\displaylines {
\begin{align*}
 & \textbf{Peak-Find-Left}(A,n) \quad \rhd n \ge 1 \\
 & p \gets 0 \\
 & k \gets 1 \\
 & \textrm{while } k < n \land A[p] < A[k] \textrm{ do} \\
 & \quad p \gets k \\
 & \quad k \gets k + 1 \\
 & \textrm{end while} \\
 & \textrm{return } p
\end{align*}
}
$$

Idea: Peak-left trova il picco più a sinistra in $A[0,\ldots,n-1]$.
Nel caso migliore, $p = 0$ è un picco.
Nel caso peggiore, il picco più a sinistra è $p = n-1$ (il vettore $A[0,\ldots,n-1]$ è una "salita").

Questo è un algoritmo di forza bruta.

## aaa

Che cosa assicura che, dato comunque $A$, un picco esista?

> [!proposizione] Teorema
> 
> Siano $i \le j$.
> 
> Se $A[i-1] < A[i]$ e $A[j] > A[j+1]$, allora esiste $i \le p \le j$ tale che $A[p-1] \le A[p] \ge A[p+1]$, ossia $p$ è un picco in $A[i,\ldots,j]$

> [!dimostrazione] Dimostrazione
> 
> Induzione su $n = j - 1 + 1$.
> 
> - $n=1$: si ha che $i=j$ e $A[i-1] < A[i] > A[i+1]$, quindi il picco $p$ è $p=i$.
> - $n>1$: sia $q \in [i,j]$ un punto qualsiasi; se $q$ è un picco ok, altrimenti:
> 	- $A[q-1] > A[q]$: allora $[i,q-1]$ è un intervallo più piccolo di $[i,j]$ e soddisfa le ipotesi del teorema, dunque vale l'ipotesi induttiva.
> 	- $A[q] < A[q+1]$: anche qui $[q+1,j]$ è più piccolo di $[i,j]$ e soddisfa le ipotesi del teorema, dunque vale l'ipotesi induttiva.
> 
> $\blacksquare$

Quindi, nel caso di $A[0,\ldots,n-1]$ di interi positivi e $A[-1] = A[n] = -\infty$ dal teorema, segue che in $A[0,\ldots,n-1]$ esiste un picco.

Osservazione: la scelta di $q$ è arbitraria, quindi possiamo scegliere il punto medio. Posso sfruttare il metodo divide et impera:
$$
\begin{align*}
 & \textbf{Peak-Find-DI}(A,n) \quad \rhd n \ge 1 \\
 & \textrm{return } \textbf{Peak-DI}(A,0,n-1)
\end{align*}
$$
e
$$
\begin{align*}
 & \textbf{Peak-DI}(A,i,j) \quad \rhd i \le j \\
 & p \gets \frac{i+1}{2} \\
 & \textrm{if } A[p-1] \le A[p] \ge A[p+1] \textrm{ then} \\
 & \quad \textrm{return } p \\
 & \textrm{else} \quad \rhd A[p-1] > A[p] \lor A[p] < A[p+1] \\
 & \quad \textrm{if } A[p-1] > A[p] \textrm{ then} \\
 & \quad\quad \textrm{return } \textbf{Peak-DI}(A,i,p-1) \\
 & \quad \textrm{else} \\
 & \quad\quad \textrm{return } \textbf{Peak-DI}(A,p+1, j) \\
 & \quad \textrm{end if} \\
 & \textrm{end if}
\end{align*}
$$

Calcolo del punto medio.
Sono stato fortunato? Ho trovato il picco? apposto
Altrimenti, tramite leggi di Morgan, dalla negazione di quell'if si ottiene l'invariante dell'else, da cui possiamo evincere che è stato riscontrato almeno uno dei due casi: o $A[p-1] > A[p]$, oppure l'altro.
Se il primo caso, allora il picco si trova nella parte a sinistra di p, nell'intervallo$[i,p-1]$, altrimenti a destra.
Non è un caso che la chiamata ricorsiva corrisponda all'ipotesi induttiva.

