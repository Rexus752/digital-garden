---
icon: FasQuestion
iconColor: "#FF8888"
---
# 1 - Esperimenti e dimostrazioni

Nella maggior parte delle discipline scientifiche (ad esempio fisica, chimica, biologia...) per stabilire la verità di un'affermazione si ricorre a misurazioni, esperimenti o simulazioni: se gli esperimenti, magari fatti più volte e da più persone, confermano l'affermazione, allora questa viene accettata (almeno temporaneamente), altrimenti viene rifiutata.

> [!esempio] Esempio: il principio di Archimede
> 
> Ogni corpo immerso parzialmente o completamente in un fluido riceve una spinta verticale dal basso verso l'alto, uguale per intensità al peso del volume del fluido spostato.
> 
> ![Principio di Archimede](Principio%20di%20Archimede.png)

In logica, il metodo scientifico NON funziona: infatti, controllare solo alcuni casi specifici può essere utile per avere indizi sulla verità o meno di un'affermazione, ma a volte non possono confermarla nella sua interezza. Ad esempio, nessun esperimento potrà mai stabilire se $\sqrt 2$ sia un numero razionale (ovvero se $\sqrt 2 = \frac{m}{n}$ con $m,n \in \mathbb{Z}$).

> [!esempio] Esempio
> 
> > [!proposizione] Congettura
> > 
> > Dato un intero $n$, il risultato di $991 \cdot n^2 + 1$ non è mai un quadrato perfetto (ovvero la sua radice quadrata non è un numero intero).
> 
> Si è dimostrato che tale congettura è falsa, anzi ci sono infiniti numeri del tipo $991 \cdot n^2 + 1$ che sono quadrati perfetti. Tuttavia, il più piccolo di tali numeri è
> $$
> n = 12055735790331359447442538767 \approx 1,2 \cdot 10^{28}
> $$
> 
> Quanto è grande questo numero? Confrontatelo con il numero di stelle nell'universo osservabile, ovvero: $\approx 3 \cdot 10^{23}$. Il nostro numero è enorme!
> Quindi controllare a mano la congettura con degli esempi (anche moltissimi!) ci avrebbe erroneamente indotti a crederla vera.

# 2 - Cos'è un teorema

In matematica, per stabilire la verità di un'affermazione (detta _teorema_) si deve ricorrere a una _dimostrazione_.

> [!definizione] Definizione: teorema
> 
> Un **teorema** è un'affermazione (riguardante numeri, funzioni, enti geometrici, o altri oggetti matematici) che si vuole dimostrare, solitamente enunciato nella forma _"se valgono $P_1, P_2, \ldots, P_n$, allora vale anche $Q$"_ (dove le affermazioni $P_1, P_2, \ldots, P_n$ sono dette _ipotesi del teorema_, mentre $Q$ è detta _tesi del teorema_).

> [!esempio] Esempio
> 
> Se $n$ è un numero naturale dispari ed $m$ è un numero naturale pari, allora il risultato di $n + m$ è un numero dispari.
> 
> $$
> \text{Se }
> \underbrace{\text{$n$ è un numero naturale dispari}}_{P_1}
> \text{ ed }
> \underbrace{\text{$m$ è un numero naturale pari}}_{P_2}
> \text{, allora }
> \underbrace{\text{$n+m$ è dispari}}_{Q}
> \text{.}
> $$

> [!osservazione] Osservazione: differenza tra _teorema_, _proposizione_ e _lemma_
> 
> In matematica sono di uso comune anche altri sinonimi di _"teorema"_, ad esempio _"proposizione"_, _"lemma"_ e così via. Dal punto di vista tecnico, tutti questi termini vogliono dire esattamente la stessa cosa, ovvero che quel che si sta affermando è un teorema.
> 
> La differenza tra le varie espressioni è l'importanza (del tutto soggettiva) che chi scrive o parla vuole attribuire all'affermazione che si sta dimostrando: solitamente si impiegano nel seguente modo:
> - Il termine _"teorema"_ per riferirsi a tutte quelle affermazioni che si ritengono veramente importanti e significative.
> - Il termine _"proposizione"_ per quelle che sono un po' meno importanti ma pur sempre abbastanza significative.
> - Il termine _"lemma"_ per quelle affermazioni che di per se non sarebbero molto significative, ma che servono poi per dimostrare altri fatti più importanti.

Quando si analizza il ragionamento matematico, come faremo noi in questo corso, non si tiene conto di queste distinzioni e si parla sempre di teorema.

%% Se il risultato dipende direttamente da un altro teorema, è un corollario.
Se è un passaggio necessario per un teorema più grande, è un lemma.
In alcuni casi, una stessa implicazione potrebbe essere chiamata corollario in un libro e proprietà in un altro, a seconda dell'enfasi o del pubblico. %%
# 3 - La conseguenza logica

%%
https://en.wikipedia.org/wiki/Logical_consequence
%%

> [!definizione] Definizione: conseguenza logica
> 
> Utilizzeremo la scrittura
> $$
> P_1, P_2, \ldots, P_n \vDash Q
> $$
> (che si legge _"Q è conseguenza logica di $P_1, P_2, \ldots, P_n$"_) per tradurre in un linguaggio simbolico il teorema con ipotesi $P_1, P_2, \ldots, P_n$ e tesi $Q$.

## 3.1 - Proprietà della conseguenza logica

%%separare le proprietà%%

Date tre affermazioni $P$, $Q$ ed $R$ qualsiasi, si ha che:
- Riflessività: $P \vDash P$;
- Transitività: se $P \vDash Q$ e $Q \vDash R$, allora $P \vDash R$

La prima proprietà è del tutto ovvia. La seconda segue dal fatto che $P \vDash R$ può essere dimostrato componendo le dimostrazioni di $P \vDash Q$ e $Q \vDash R$ (dimostrazione per composizione o interpolazione).

# 4 - Dimostrare un teorema

> [!definizione] Definizione: dimostrazione di un teorema
> 
> Una **dimostrazione di un teorema** è una catena di ragionamenti che ci permette di concludere che la tesi del teorema $Q$ deve essere vera partendo dall'assunzione che le ipotesi del teorema $P_1, P_2, \ldots, P_n$ siano vere.

> [!esempio]
> 
> Supponiamo di aver scritto il programma che controlla la ventilazione di una sonda spaziale. Verificare con un certo numero (anche elevatissimo!) di esperimenti o simulazioni che il programma non va in crash ed esegue correttamente tutte le operazioni che deve svolgere non è sufficiente... 
> 
> Come si può garantire che una volta in funzione sulla sonda spaziale non si verifichi proprio una situazione, mai incontrata nelle simulazioni, che porti al blocco del sistema (per la gioia degli astronauti presenti a bordo, che morirebbero soffocati)? L'unico modo è fornire una dimostrazione del fatto che il programma funziona, ovvero della sua correttezza. Pur parlando di programmi e non di numeri, il concetto di dimostrazione è esattamente lo stesso usato in matematica quando si parla di teoremi.

> [!definizione] Definizione: contesto di un'affermazione
> 
> Il **contesto di un'affermazione** è il dominio %%(?)%%in cui ci si chiede se può essere vera o meno.

Stabilire che cosa sia un contesto/situazione in cui sia possibile valutare se una data affermazione $P$ sia vera o falsa è molto delicato. Negli esempi seguenti tutti le affermazioni $P$ che considereremo parleranno di numeri $n, m, x$: i "contesti" possibili saranno allora tutti i possibili valori che questi numeri possono assumere.

> [!esempio]
> 
> L'affermazione _"$n$ è un numero naturale dispari"_ è vera nella situazione in cui $n$ vale $3$, ma falsa quando $n$ vale $4$.

> [!definizione] Definizione: tautologia
> 
> Una **tautologia** è un'affermazione sempre vera in qualunque contesto, ossia un enunciato per il quale
> $$
> \vDash Q
> $$
> è un teorema che non ha bisogno di ipotesi.
> 
> $Q$ solitamente è della forma
> $$
> P \lor \lnot P
> $$
> (si legge _"$P$ oppure non-$P$"_) dove $P$ è una qualche affermazione e $\lnot P$ la sua negazione. Indipendentemente da che cosa asserisce $P$ e dal contesto in cui ci poniamo, dobbiamo concludere che $Q$ è valido.

> [!esempio]
> 
> L'affermazione _"un numero intero è pari, oppure non lo è"_ è una tautologia.

## 4.1 - Tautologie e contraddizioni

Mediante le tavole di verità è immediato osservare che
$$
P \lor \lnot P
$$
è sempre vera, qualunque sia $P$.
Proposizioni di questo tipo, ovvero affermazioni la cui tavola di verità assume sempre il valore $V$ si dicono _tautologie_. In simboli, scriviamo $\vDash Q$ per dire che $Q$ è una tautologia.
Viceversa, il valore di verità di
$$
P \land \lnot P
$$
è sempre falso, qualunque sia $P$.
Proposizioni di questo tipo, ovvero affermazioni la cui tavola di verità assume sempre il valore F si dicono _contraddizioni_.

Osserviamo che
$$
Q \vDash P \lor \lnot P
$$
qualunque siano $P$ e $Q$. Infatti presa una qualsiasi riga della tavola di verità di $P$ e $Q$ in cui $Q$ assume il valore VERO, allora in quella riga anche $P \lor \lnot P$ ha valore VERO. Infatti in ogni riga $P \lor \lnot P$ ha valore VERO.
Viceversa,
$$
P \land \lnot P \vDash Q
$$
indipendentemente da $P$ e $Q$. Infatti, poiché $P \land \lnot P$ è sempre falsa, quindi non c'è nessuna riga della tavola di verità di $P$ e $Q$ in cui $P \land \lnot P$ assuma il valore VERO ma $Q$ ha valore FALSO.
Ovviamente $P \land \lnot P$ potrebbe essere sostituita da qualunque contraddizione.
Questo è il cosiddetto principio dell'_ex falso quodlibet_.

# 5 - Tipi di dimostrazioni

Ci sono diverse strategie dimostrative variamente utilizzate (spesso in combinazione tra loro). Nel seguito presenteremo le più comuni ossia:
- La dimostrazione diretta;
- La dimostrazione per assurdo;
- La dimostrazione per contrapposizione;
- La dimostrazione per composizione (o interpolazione);
- La dimostrazione per casi.

La correttezza di tutte queste strategie dimostrative può essere verificata in maniera rigorosa utilizzando la logica proposizionale.

## 5.1 - Dimostrazione diretta

> [!definizione] Definizione: dimostrazione diretta
> 
> Una **dimostrazione diretta** di un teorema della forma $P_1, P_2, \ldots, P_n \vDash Q$ è una dimostrazione in cui, sulla base di semplici e rigorosi ragionamenti, a partire dalle ipotesi $P_1, P_2, \ldots, P_n$ si stabilisce che in tale contesto anche la tesi $Q$ è verificata.

> [!esempio] Esempio
> 
> > [!proposizione] Teorema
> > 
> > Se $n$ è un numero intero dispari e $m$ è un numero intero pari, allora il risultato di $n + m$ è un numero intero dispari.
> 
> > [!dimostrazione] Dimostrazione
> > 
> > Siano $n$ ed $m$ interi qualsiasi e assumiamo che $n$ sia dispari ed $m$ pari, ovvero che $n = 2l + 1$ per qualche intero $l$, mentre $m = 2k$ per qualche intero $k$. Bisogna dimostrare che $n + m$ è dispari. Effettuando i calcoli si ha:
> > $$
> > \begin{align*}
> > n + m
> > & = (2l + 1) + 2k \\
> > & = (2l + 2k) + 1 \\
> > & = 2(l + k) + 1 \\
> > & = 2j + 1 \quad \text{con $j = l + k$}
> > \end{align*}
> > $$
> > 
> > Questo dimostra che $n + m$ è dispari perché ha la forma $2j + 1$.
> > 
> > $\blacksquare$

## 5.2 - Dimostrazione per assurdo

> [!definizione] Definizione: dimostrazione per assurdo
> 
> Una **dimostrazione per assurdo** (o **_dimostrazione indiretta_**) di un teorema della forma $P_1, P_2, \ldots, P_n \vDash Q$ è una dimostrazione in cui si assume che la tesi $Q$ sia falsa e da questa assunzione si deriva (utilizzando anche le ipotesi $P_1, P_2, \ldots, P_n$) una contraddizione, ovvero una proposizione della forma
> $$
> R \land \lnot R
> $$
> che asserisce che una qualche affermazione $R$ è al contempo sia vera che falsa. Poiché una contraddizione è necessariamente falsa (una proposizione in un dato contesto può essere vera o falsa, ma non entrambe contemporaneamente!), questo prova che assumere che $Q$ sia falsa porta a conclusioni assurde, e quindi $Q$ non può che essere vera. 

In altre parole: si dimostra che se le premesse $P_1, P_2, \ldots, P_n$ sono vere non è possibile che $Q$ sia falsa.

Concretamente, in una dimostrazione per assurdo di un teorema del tipo
$$
P_1, P_2, \ldots, P_n \vDash Q
$$
si assume che le ipotesi $P_1, P_2, \ldots, P_n$ siano vere ma che, per assurdo, la tesi $Q$ sia falsa, e da questa assunzione si deriva una contraddizione.
Quando invece il teorema è del tipo
$$
\vDash Q
$$
ovvero quando si deve dimostrare $Q$ senza partire da alcuna ipotesi (cioè quando bisogna mostrare che $Q$ è una tautologia), allora una dimostrazione
per assurdo consiste semplicemente nell'assumere per assurdo che $Q$ sia falsa, e poi dimostrare che da quest'assunzione deriva una contraddizione.

> [!esempio] Esempio
> 
> > [!proposizione] Teorema
> > 
> > Per ogni coppia di numeri reali $x$ e $y$, se $\underbrace{x + y \ge 2}_{P}$ allora $\underbrace{x \ge 1 \text{ oppure } y \ge 1}_{Q}$.
> 
> > [!dimostrazione] Dimostrazione
> > 
> > Siano $x$ e $y$ due numeri reali qualsiasi e supponiamo per assurdo che $P$ sia vera ma $Q$ sia falsa, ovvero che valgano $x + y \ge 2$ e $x, y < 1$  (si osservi che assumere che _"$x \ge 1$ oppure $y \ge 1$"_ sia falsa è equivalente ad assumere che _"$x < 1$ e $y < 1$"_ sia vera).
> > 
> > Dalla negazione di $Q$ segue che $x + y < 1 + 1$, ovvero $x + y < 2$. Ma questo contraddice l'assunzione $P$, quella per cui $x + y \ge 2$.
> > 
> > Questo dimostra (per assurdo) che se vale $P$ allora $Q$ non può essere falsa. In altre parole, è vero che se vale $P$ allora deve valere anche $Q$, quindi il teorema è dimostrato.
> > 
> > $\blacksquare$

> [!esempio] Esempio
> 
> > [!proposizione] Teorema
> > 
> > Per ogni numero intero $n$, se $\underbrace{n^2 \text{ è pari}}_{P}$, allora $\underbrace{n \text{ è pari}}_{Q}$.
> 
> > [!dimostrazione] Dimostrazione
> > 
> > Supponiamo per assurdo che $P$ sia vera ma $Q$ sia falsa (ovvero che $n$ sia dispari) e facciamo vedere che queste assunzioni portano ad una contraddizione. Sia $n$ dispari, ovvero $n = 2m + 1$ per qualche intero $m$.
> > 
> > Allora possiamo calcolare:
> > $$
> > \begin{align*}
> > n^2 &= (2m + 1)^2 \\
> > &= 4m^2 + 4m + 1 \\
> > &= 2(2m^2 + 2m) + 1
> > \end{align*}
> > $$
> > per cui $n^2$ è dispari (essendo della forma $2j+1$ con $j = 2m^2 + 2m$), ma ciò contraddice l'ipotesi iniziale $P$ per la quale $n^2$ è pari.
> > 
> > Abbiamo una contraddizione, quindi se vale $P$ deve necessariamente valere anche $Q$.
> > 
> > $\blacksquare$

## 5.3 - Dimostrazione per contrapposizione

> [!definizione] Definizione: dimostrazione per contrapposizione
> 
> Una **dimostrazione per contrapposizione** di un teorema della forma $P_1, P_2, \ldots, P_n \vDash Q$ è una dimostrazione in cui la tesi $Q$ viene negata e, a partire da questa, si deve dimostrare che anche le ipotesi $P_1, P_2, \ldots, P_n$ vengono negate:
> $$
> \lnot Q \vDash \lnot(P_1, P_2, \ldots, P_n)
> $$
> Infatti, supponiamo di aver stabilito la correttezza del teorema $\lnot Q \vDash \lnot(P_1, P_2, \ldots, P_n)$ e di essere in un contesto in cui valgono le ipotesi $P_1, P_2, \ldots, P_n$. Allora in tale contesto anche la tesi $Q$ deve essere vera, perché se fosse falsa (ovvero se valesse $\lnot Q$) allora si avrebbe che sia $P_1, P_2, \ldots, P_n$ (per ipotesi) che $\lnot(P_1, P_2, \ldots, P_n)$ (per il teorema $\lnot Q \vDash \lnot(P_1, P_2, \ldots, P_n)$) sarebbero vere, contraddizione!
> Posto di sapere che $\lnot Q \vDash \lnot(P_1, P_2, \ldots, P_n)$, questo argomento mostra che in ogni contesto in cui valgano le ipotesi $P_1, P_2, \ldots, P_n$ deve valere anche la tesi $Q$, ossia che $P_1, P_2, \ldots, P_n \vDash Q$.

> [!esempio] Esempio
> 
> > [!proposizione] Teorema
> > 
> > Se $\underbrace{n^2 \text{ è un numero intero pari}}_{P}$, allora $\underbrace{n \text{ è un numero intero pari}}_{Q}$.
> 
> > [!dimostrazione] Dimostrazione
> > 
> > Usando la dimostrazione per contrapposizione, l'enunciato diventa "se $\underbrace{n \text{ è un numero intero dispari}}_{\lnot Q}$, allora $\underbrace{n^2 \text{ è un numero intero dispari}}_{\lnot P}$".
> > 
> > Si può procedere adesso anche col metodo diretto: assumiamo che $n$ sia dispari, ovvero che $n = 2k + 1$ per qualche intero $k$: bisogna dimostrare allora che anche $n^2$ è dispari. Svolgendo i calcoli si ha che:
> > $$
> > \begin{align*}
> > n^2 &= (2k + 1)^2 \\
> > &= (4k^2 + 4k + 1) \\
> > &= 2(2k^2 + 2k) + 1
> > \end{align*}
> > $$
> > quindi $n^2$ è dispari (poiché è della forma $2j + 1$ con $j = 2k^2 + 2k$).
> > 
> > $\blacksquare$

%%mettere in corsivo l'enunciato, sia qua che in tutti gli altri esempi%%

## 5.4 - Dimostrazione per composizione

> [!definizione] Definizione: dimostrazione per composizione
> 
> Una **dimostrazione per composizione** (o **_dimostrazione per interpolazione_**) di un teorema della forma $P_1, P_2, \ldots, P_n \vDash Q$ è una dimostrazione effettuata unendo le dimostrazioni di due sotto-teoremi $P_1, P_2, \ldots, P_n \vDash R$ e $R \vDash Q$.

Spiegazione:
In ogni contesto in cui valgano le ipotesi $P_1, P_2, \ldots, P_n$ deve valere anche $R$, dato che $P_1, P_2, \ldots, P_n \vDash R$. Ma allora in tale contesto deve valere anche $Q$ poiché $R \vDash Q$. Quindi abbiamo stabilito che in ogni contesto in cui valgano $P_1, P_2, \ldots, P_n$ anche $Q$ deve valere, ossia che $P_1, P_2, \ldots, P_n \vDash Q$.

> [!esempio] Esempio
> 
> > [!proposizione] Teorema
> > 
> > Se $\underbrace{n \text{ è un numero intero pari}}_{P_1}$ ed $\underbrace{m \text{ è un numero intero pari}}_{P_2}$, allora $\underbrace{(n+m)^2 \text{ è un numero intero pari}}_{Q}$.
> 
> > [!dimostrazione] Dimostrazione
> > 
> > Abbiamo visto in precedenza che considerando $\underbrace{(n+m) \text{ è un numero intero pari}}_{R}$ si ha che $P_1, P_2 \vDash R$ e $R \vDash Q$. Componendo le dimostrazioni dei due teoremi otteniamo quindi una dimostrazione di $P_1, P_2 \vDash Q$.
> > 
> > $\blacksquare$

## 5.5 - Dimostrazione per casi

> [!definizione] Definizione: dimostrazione per casi
> 
> Una **dimostrazione per casi** di un teorema della forma $P \vDash Q$, dove $P$ è una serie di disgiunzione di enunciati della forma $P_1 \lor P_2 \lor \ldots \lor P_n$, è una dimostrazione in cui ogni enunciato viene dimostrato separatamente dagli altri.

Spiegazione:
Supponiamo di aver dimostrato ciascuno dei teoremi sopra elencati. Se in un contesto vale $P$, in questo contesto almeno un $P_i$ tra i $P_1, P_2, \ldots, P_n$ che sarà vero, per cui avendo dimostrato che $P_i \vDash Q$ possiamo concludere che in tale contesto anche Q è vero.

A volte i "casi" $P_1, P_2, \ldots, P_n$ non sono esplicitamente dati dall'enunciato, ma possiamo comunque distinguere diversi casi nella dimostrazione (quando questo è utile).
Ad esempio, per dimostrare un teorema $\vDash Q$ senza nessuna ipotesi (quindi quando è una tautologia), possiamo sfruttare il fatto che l'asserzione $P \lor \lnot P$ è necessariamente vera in qualunque contesto (e indipendentemente da chi sia $P$: in ciascun contesto, o $P$ è vera oppure è falsa). Quindi per dimostrare $\vDash Q$ ci basta considerare i due casi ($P$ vera, oppure $P$ falsa) e dimostrare che valgono sia $P \vDash Q$ che $\lnot P \vDash Q$.

> [!esempio] Esempio
> 
> Se vogliamo dimostrare che una certa proprietà vale per tutti i numeri reali, possiamo considerare separatamente diversi casi (purché ogni reale sia compreso in almeno uno di essi): ad esempio possiamo trattare separatamente il caso dei reali $< 0$ e quello dei reali $\ge 0$.

> [!esempio] Esempio
> 
> > [!proposizione] Teorema
> > 
> > Per ogni numero reale $x$ si ha che $x \le |x|$.
> 
> Il teorema è della forma $\vDash Q$ con $\underbrace{x \le |x|}_{Q}$ e vogliamo mostrare che $Q$ è vera in tutti i contesti possibili, ovvero per qualunque valore di $x$. Siccome nella definizione di valore assoluto
> $$
> |x| =
> \begin{cases}
> x & \text{se } x \ge 0 \\
> -x & \text{se } x < 0
> \end{cases}
> $$
> si considerano i due casi $\underbrace{x < 0}_{P}$ e $\underbrace{x \ge 0}_{\lnot P}$, è naturale distinguere tra tali casi anche nella dimostrazione.
> (Si osservi che $P \lor \lnot P$, ovvero l'affermazione $x < 0 \lor x \ge 0$ , è vera per ogni numero reale $x$, ovvero in ogni contesto che dobbiamo considerare.)
> 
> > [!dimostrazione] Dimostrazione
> > 
> > Distinguiamo due casi:
> > - $x < 0$: in questo caso $|x| = -x$, quindi $|x| > 0 > x$, da cui $x \le |x|$.
> > - $x \ge 0$: in questo caso $|x| = x$, per cui vale $x \le |x|$.
> > 
> > Poiché ogni reale $x$ è o $x < 0$ oppure $x \ge 0$, si può allora concludere che $x \le |x|$ vale per ogni reale $x$.
> > 
> > $\blacksquare$

## 5.6 - Combinazione delle dimostrazioni

Le varie tecniche di dimostrazione viste possono poi essere combinate tra loro in vario modo all'interno di una stessa dimostrazione, dando luogo ad argomenti via via più complessi ma sempre logicamente corretti.

> [!esempio] Esempio
> 
> > [!proposizione] Teorema
> > 
> > $\sqrt 2 \not \in \mathbb{Q}$
> 
> Notiamo che posto $\underbrace{\sqrt 2 \not \in \mathbb{Q}}_{Q}$, questo è un teorema della forma $\vDash Q$.
> 
> > [!dimostrazione] Dimostrazione
> > 
> > Supponiamo per assurdo che $\underbrace{\exists m,n \in \mathbb{N} \setminus \{0\} : (\frac{m}{n})^2 = 2}_{\lnot Q}$ e cerchiamo di ottenere una contraddizione. Se $m$ ed $n$ hanno $d$ come massimo comun divisore, cioè $m = m_1 \cdot d$ e $n = n_1 \cdot d$, allora
> > $$
> > \frac{m}{n} = \frac{m_1 \cdot d}{n_1 \cdot d} = \frac{m_1}{n_1}
> > $$
> > quindi si ha che $(\frac{m_1}{n_1})^2 = 2$ e che $m_1$ ed $n_1$ sono coprimi (ovvero il loro massimo comun divisore è $1$).
> > 
> > Da $\underbrace{\exists m,n \in \mathbb{N} \setminus \{0\} : (\frac{m}{n})^2 = 2}_{\lnot Q}$ abbiamo quindi dedotto (in maniera diretta) l'esistenza di numeri interi $m_1$, $n_1$ tali che $\underbrace{m_1 \text{ e } n_1 \text{ sono coprimi}}_{P}$ e $\underbrace{(\frac{m_1}{n_1})^2 = 2}_{R}$.
> > Vogliamo ora ottenere una contraddizione. Per fare questo da $R$ dedurremo $\lnot P$, cosicché alla fine si avrà che da $\lnot Q$ segue $P \land \lnot P$.
> > 
> > Siccome $\underbrace{(\frac{m_1}{n_1})^2 = 2}_{R}$, si ha che $\frac{m_1^2}{n_1^2} = 2$, da cui $m_1^2 = 2n_1^2$. Questo mostra che $m_1^2$ è pari, quindi, per quanto dimostrato nelle slides precedenti, $m_1$ è pari, cioè è della forma $m_1 = 2k$ per qualche intero $k$. Quindi $m_1^2 = 4k^2$ e, sostituendo questo valore nell'equazione $m_1^2 = 2n_1^2$, si ottiene $4k^2 = 2n_1^2$, da cui $n_1^2= 2k^2$ . Quindi anche $n_1^2$ è pari, e per quanto visto in precedenza questo implica che $n_1$ sia pari. Ma poiché sono entrambi pari, questo vuol dire che $\underbrace{m_1 \text{ e } n_1 \text{ NON sono coprimi}}_{\lnot P}$, contraddizione!
> > 
> > $\blacksquare$
> 
> La struttura della dimostrazione precedente è quindi:
> 1. Si assume (per assurdo) che la tesi del teorema $Q$ sia falsa, ovvero si assume $\lnot Q$.
> 2. Si dimostra in maniera diretta che $\lnot Q \vDash P$.
> 3. Si dimostra in maniera diretta che $\lnot Q \vDash R$ e $R \vDash \lnot P$, da cui per composizione $\lnot Q \vDash \lnot P$ (si noti però che durante questa dimostrazione diretta abbiamo usato due volte il fatto che "se un numero $j^2$ è pari allora $j$ è anch'esso pari", che era stato dimostrato per contrapposizione: quindi in realtà si tratta della composizione di alcune dimostrazioni dirette, come ad esempio quella di $\lnot Q \vDash (m_2 \text { è pari})$, oppure quella di $(m \text{ è pari}) \vDash (n^2 \text{ è pari})$ , con la dimostrazione per contrapposizione del risultato menzionato).
> 4. Si conclude quindi che $\lnot Q \vDash P \land \lnot P$, cosicché si è dimostrato che dall'ipotesi (assurda) $\lnot Q$ seguirebbe una contraddizione.
> 5. Utilizzando il metodo della dimostrazione per assurdo, si conclude allora che $Q$ deve essere vera.
> 
> > [!dimostrazione] Dimostrazione alternativa di $\sqrt 2 \not \in Q$
> > 
> > Come prima, ragioniamo per assurdo. Supponiamo che esistano $m, n \in \mathbb{N} \setminus \{0\}$ tali che $(\frac{m}{n})^2 = 2$ (ovvero tali che $m^2 = 2n^2$; in particolare $\frac{m}{2} < n < m$) e supponiamo che $m$ sia il più piccolo numero siffatto.
> > 
> > ![](Pasted%20image%2020240925114331.png)
> > 
> > Allora $m^2 = n^2 + n^2 + 2(m-n)^2 + k^2$, da cui (tenendo conto che $m^2 = 2n^2$) si ha $0 = 2(m-n)^2 - k^2$, cioè $k^2 = 2(m-n)^2$, ovvero $(\frac{k}{m-n})^2 = 2$.
> > 
> > Ma $k = m - 2(m-n) < m$, contraddizione!
> > 
> > $\blacksquare$

# Fonti

- Slide del Prof. Viale Matteo del corso di Logica Matematica (canale B), Corso di Laurea in Informatica presso l'Università di Torino, A.A. 2024-25:
	- [1.1 - Teoremi e dimostrazioni_moodle.pdf](https://informatica.i-learn.unito.it/pluginfile.php/417200/mod_folder/content/0/1.1%20-%20Teoremi%20e%20dimostrazioni_moodle.pdf?forcedownload=1)
	- [1.2 - Simboli logici_moodle.pdf](https://informatica.i-learn.unito.it/pluginfile.php/417200/mod_folder/content/0/1.2%20-%20Simboli%20logici_moodle.pdf?forcedownload=1)
