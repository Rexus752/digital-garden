---
icon: RiFlowChart
iconColor: "#88FF88"
---
%%
introduzione sull'algoritmica
%%

> [!definizione] Definizione: _algoritmo_
> 
> Un **algoritmo** è la specificazione di una sequenza finita di operazioni (dette anche _istruzioni_) che consente di risolvere tutti i quesiti di una stessa classe, ognuno dei quali viene detto _istanza del problema_, o di calcolare il risultato di un'espressione matematica.
> 
> Un algoritmo, per essere considerato tale, deve essere:
> - **Finito**: costituito da un numero finito di istruzioni e deve sempre terminare;
> - **Deterministico**: partendo dagli stessi dati in ingresso, si devono ottenere i medesimi risultati;
> - **Non ambiguo**: le operazioni non devono poter essere interpretate in modi differenti;
> - **Generale**: applicabile a tutte le istanze del problema computazionale%%link%% che si intende risolva.

%%
Procedura: algoritmo che non necessariamente termina.
%%

# 1 - Esempio: algoritmo dell'addizione in colonna

Quella dell'addizione in colonna è una sequenza finita di istruzioni che tutti conoscono e che, in realtà, è un vero e proprio algoritmo, usato per la somma di due numeri o più numeri. Ecco una possibile descrizione dell'algoritmo, usando come esempio la somma $712 + 2609 + 431$:
1. Scrivere i numeri da sommare uno sotto l'altro, separando le singole cifre e allineando le cifre per colonna (unità sotto unità, decine sotto decine, centinaia sotto centinaia, ecc.);
$$
\begin{array}{}
& \color{Green}7 & \color{Red}1 & \color{Blue}2 & + \\
\color{Orange}2 & \color{Green}6 & \color{Red}0 & \color{Blue}9 & + \\
& \color{Green}4 & \color{Red}3 & \color{Blue}1 & = \\
\hline
\end{array}
$$
2. Sommare le cifre nella colonna delle <font color="Blue">unità</font>:
   - Se la somma è inferiore a $10$, scrivere il risultato sotto la colonna;
   - Se la somma è $10$ o maggiore, scrivere sotto la colonna delle unità la cifra delle unità della somma e "riportare" la decina in cima alla colonna delle decine;
$$
\begin{array}{}
& & \color{Red}_1 \\
& \color{Green}7 & \color{Red}1 & \color{Blue}2 & + \\
\color{Orange}2 & \color{Green}6 & \color{Red}0 & \color{Blue}9 & + \\
& \color{Green}4 & \color{Red}3 & \color{Blue}1 & = \\
\hline
& & & \color{Blue}2
\end{array}
$$

4. Sommare le cifre nella colonna delle <font color="Red">decine</font>, inclusa quella dell'eventuale riporto presente in cima alla colonna ed effettuare nuovamente il riporto se il risultato dovesse essere maggiore o uguale a $10$;
$$
\begin{array}{}
& & \color{Red}_1 \\
& \color{Green}7 & \color{Red}1 & \color{Blue}2 & + \\
\color{Orange}2 & \color{Green}6 & \color{Red}0 & \color{Blue}9 & + \\
& \color{Green}4 & \color{Red}3 & \color{Blue}1 & = \\
\hline
& & \color{Red}5 & \color{Blue}2
\end{array}
$$
5. Ripetere lo stesso procedimento anche per le colonne delle <font color="Green">centinaia</font> e delle <font color="Orange">migliaia</font>;
$$
\begin{array}{}
\color{Orange}_1 & & \color{Red}_1 \\
& \color{Green}7 & \color{Red}1 & \color{Blue}2 & + \\
\color{Orange}2 & \color{Green}6 & \color{Red}0 & \color{Blue}9 & + \\
& \color{Green}4 & \color{Red}3 & \color{Blue}1 & = \\
\hline
\color{Orange}3 & \color{Green}7 & \color{Red}5 & \color{Blue}2
\end{array}
$$
6. Il risultato finale dell'addizione è quello riportato nella riga in basso.

# 2 - Un algoritmo non è necessariamente matematico

Dal momento che l'algoritmo è semplicemente una sequenza di istruzioni da seguire per raggiungere un obiettivo, esso non deve necessariamente rappresentare una situazione matematica fatta di numeri e calcoli. Per esempio, si può descrivere un algoritmo per preparare una tazza di tè:
1. Raccogliere gli ingredienti e gli strumenti:
	- Tazza;
	- Bustina di tè;
	- Acqua;
	- Zucchero (facoltativo);
	- Limone (facoltativo);
	- Bollitore o pentola per riscaldare l'acqua;
2. Riempire il bollitore con acqua;
3. Accendere il bollitore e portare l'acqua a ebollizione;
4. Mentre l'acqua si riscalda, posizionare la bustina di tè nella tazza;
5. Quando l'acqua è bollente, versarla nella tazza sopra la bustina di tè;
6. Lasciare in infusione la bustina di tè per 3-5 minuti, a seconda dell'intensità desiderata;
7. Rimuovere la bustina di tè dalla tazza e scartarla;
8. Aggiungere zucchero o limone a piacere e mescolare bene;
9. Lasciare raffreddare un po' e poi gustare il tè.

Si può notare come anche questa sequenza di istruzioni rispetti le condizioni per essere considerata un _algoritmo_: è una sequenza **finita** di passi (l'algoritmo termina dopo 9 passi), **deterministica** (usando sempre gli stessi ingredienti e lo stesso procedimento, al termine dell'algoritmo si otterrà lo stesso tipo di tè), **non ambigua** (le istruzioni descrivono precisamente i passi da compiere) e **generale** (con queste istruzioni si può preparare qualsiasi tazza di tè).

# 3 - Etimologia ed origine

Il termine deriva dalla trascrizione latina del nome del matematico persiano Muḥammad ibn Mūsā al-Khwārizmī, vissuto nel IX secolo d.C., che è considerato uno dei primi autori ad aver fatto riferimento a questo concetto scrivendo il libro _"Regole di ripristino e riduzione"_.

Le prime nozioni di algoritmo si trovano in documenti risalenti al XVII secolo a.C., conosciuti come _papiri di Ahmes_ e noti anche come _papiri di Rhind_, che contengono una collezione di problemi con relativa soluzione comprendendo un problema di moltiplicazione che lo scrittore dichiara di aver copiato da altri papiri anteriori di due secoli.

# 4 - L'algoritmo in informatica

L'algoritmo è un concetto fondamentale dell'informatica, anzitutto perché è alla base della nozione teorica di calcolabilità: un problema è calcolabile quando è risolvibile mediante un algoritmo. Inoltre, l'algoritmo è un concetto cardine anche nella fase di programmazione dello sviluppo di un software: preso un problema da automatizzare, la programmazione costituisce essenzialmente la traduzione o codifica di un algoritmo per tale problema in programma, scritto in un certo linguaggio, che può essere quindi effettivamente eseguito da un calcolatore rappresentandone la logica di elaborazione.

%%
L'ordinamento non è affatto l'unico problema computazionale per cui sono sta-
ti sviluppati gli algoritmi (molti lo avranno intuito osservando la mole di que-
sto libro). Le applicazioni pratiche degli algoritmi sono innumerevoli; ne citiamo
alcune:
• Il Progetto Genoma Umano ha l'obiettivo di identificare tutti i 100.000 geni
del DNA umano, determinando le sequenze di 3 miliardi di paia di basi chimi-
che che formano il DNA umano, registrando queste informazioni nei database
e sviluppando gli strumenti per analizzare i dati. Ciascuno di questi passaggi
richiede sofisticati algoritmi. Sebbene le soluzioni di questi problemi esulino
dagli obiettivi di questo libro, i concetti esposti in molti capitoli vengono uti-
lizzati per risolvere tali problemi biologici, consentendo così agli scienziati
di svolgere i loro compiti utilizzando in modo efficiente le risorse. Si rispar-
mia tempo (di persone e macchine) e denaro, in quanto è possibile estrarre più
informazioni dalle tecniche di laboratorio.
• Internet consente agli utenti di tutto il mondo di accedere rapidamente a grandi
quantità di informazioni. Per fare ciò vengono impiegati algoritmi intelligenti
che gestiscono e manipolano enormi volumi di dati. Fra gli esempi di proble-
mi che devono essere risolti citiamo la ricerca dei percorsi ottimali che i dati
devono seguire (le tecniche per risolvere questi problemi sono descritte nel
Capitolo 24) e l'uso di un motore di ricerca per trovare velocemente le pagine
che contengono una particolare informazione (le relative tecniche sono trattate
nei Capitoli 11 e 32).
• Il commercio elettronico consente di negoziare e scambiare elettronicamente
beni e servizi. La capacità di mantenere riservate informazioni quali i codici
delle carte di credito, le password e gli estratti conto è essenziale alla diffusione
su vasta scala del commercio elettronico. La crittografia a chiave pubblica e le
firme digitali (descritte nel Capitolo 31) sono le principali tecnologie utilizzate
e si basano su algoritmi numerici e sulla teoria dei numeri.
• Nelle attività industriali e commerciali spesso è importante allocare poche ri-
sorse nel modo più vantaggioso. Una compagnia petrolifera potrebbe essere
interessata a sapere dove disporre i propri pozzi per massimizzare i profitti.
Un candidato alla presidenza degli Stati Uniti d'America potrebbe essere in-
teressato a determinare in quale campagna pubblicitaria investire i suoi soldi
per massimizzare le probabilità di vincere le elezioni. Una compagnia aerea
potrebbe essere interessata ad assegnare il personale ai voli nel modo più eco-
nomico possibile, verificando che ogni volo sia coperto e che siano soddisfatte
le disposizioni governative sulla programmazione del personale di volo. Un provider di servizi Internet potrebbe essere interessato a determinare dove al-
locare delle risorse addizionali per servire i suoi clienti in modo più efficiente.
Tutti questi sono esempi di problemi che possono essere risolti utilizzando la
programmazione lineare, che sarà trattata nel Capitolo 29.
Sebbene alcuni dettagli di questi esempi esulino dagli scopi di questo libro,
tuttavia è opportuno descrivere le tecniche di base che si applicano a questi tipi
di problemi. Spiegheremo inoltre come risolvere molti problemi concreti, inclusi
i seguenti:
• Supponiamo di avere una carta stradale dove sono segnate le distanze fra ogni
coppia di incroci adiacenti; il nostro obiettivo è determinare il percorso più
breve da un incrocio all'altro. Il numero di percorsi possibili può essere enor-
me, anche se escludiamo i percorsi che passano su sé stessi. Come scegliere
il più breve di tutti i percorsi? In questo caso, creiamo un modello della carta
stradale (che a sua volta è un modello delle strade reali) come un grafo (che
descriveremo nel Capitolo 10 e nell'Appendice B) e cerchiamo di determina-
re il cammino più breve da un vertice all'altro del grafo. Spiegheremo come
risolvere efficientemente questo problema nel Capitolo 24.
• Data una sequenza 〈A1, A2, . . . , An〉 di n matrici, vogliamo determinare il
loro prodotto A1A2 · · · An. Poiché la moltiplicazione di matrici è associativa,
ci sono vari modi di moltiplicare. Per esempio, se n = 4, potremmo ese-
guire il prodotto delle matrici in uno dei seguenti modi: (A1(A2(A3A4))),
(A1((A2A3)A4)), ((A1A2)(A3A4)), ((A1(A2A3))A4) o (((A1A2)A3)A4).
Se le matrici sono tutte quadrate (e quindi della stessa dimensione), il modo
di moltiplicare le matrici non avrà effetto sul tempo richiesto per eseguire il
prodotto. Se, invece, queste matrici hanno dimensioni differenti (ma compa-
tibili con la moltiplicazione delle matrici), allora il modo di moltiplicare può
determinare una differenza significativa. Il numero dei possibili modi di mol-
tiplicare le matrici è esponenziale in n, pertanto provare tutti i possibili modi
potrebbe richiedere un tempo molto lungo. Vedremo nel Capitolo 15 come uti-
lizzare una tecnica generale, la programmazione dinamica, per risolvere questo
problema in una maniera molto più efficiente.
• Data l'equazione ax \equiv b (mod n), dove a, b e n sono interi, vogliamo de-
terminare tutti gli interi x, modulo n, che soddisfano l'equazione. Ci posso-
no essere zero, una o più soluzioni. Potremmo semplicemente provare x =
0, 1, . . . , n-1 nell'ordine, ma il Capitolo 31 descrive un metodo più efficiente.
• Dati n punti nel piano, vogliamo determinare il guscio convesso di questi pun-
ti. Il guscio convesso è il più piccolo poligono convesso che contiene i punti.
Intuitivamente, possiamo immaginare ogni punto come se fosse rappresentato
da un chiodo che fuoriesce da una tavola. Il guscio convesso potrebbe essere
rappresentato da un elastico teso che circonda tutti i chiodi. Ogni chiodo attor-
no al quale l'elastico fa un giro è un vertice del guscio convesso (un esempio
è illustrato nella Figura 33.6 a pagina 805). Uno dei 2n sottoinsiemi dei punti
potrebbe essere formato dai vertici del guscio convesso. Conoscere i punti che
formano i vertici del guscio convesso non è sufficiente, in quanto occorre sa-
pere anche l'ordine in cui essi si presentano. Ci sono dunque molte possibilità
di scelta per i vertici del guscio convesso. Il Capitolo 33 descrive due buoni
metodi per trovare il guscio convesso.
Questo elenco non è affatto esaustivo (come probabilmente avrete immaginato
dalle dimensioni di questo libro), ma presenta due caratteristiche che sono comuni
a molti algoritmi.
1. Esistono numerose soluzioni possibili, molte delle quali non sono ciò che
vogliamo. Trovare quella desiderata può essere un'impresa ardua.
2. Esistono varie applicazioni pratiche. Fra i problemi precedentemente elencati,
determinare il percorso più breve rappresenta l'esempio più semplice. Un'a-
zienda di trasporti su strada o rotaie è interessata a trovare i percorsi minimi
nelle reti stradali o ferroviarie, perché tali percorsi consentono di risparmiare
costi di manodopera e carburante. Come altro esempio, potrebbe essere neces-
sario un nodo di routing su Internet per trovare il percorso più breve nella rete
che permette di instradare rapidamente un messaggio.
%%
