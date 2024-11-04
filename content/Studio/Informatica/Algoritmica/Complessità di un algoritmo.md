---
draft: false
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