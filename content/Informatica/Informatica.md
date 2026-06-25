
> [!premessa]+ Premessa
> 
> Ciao! Se è la prima volta che capiti su questo sito, ti consiglio di consultare la [pagina principale](index.md) di questo cosiddetto _Giardino Digitale_ per scoprire meglio cos'è e come navigarlo.
> 
> Lo stato di questa nota è al momento: 🔴 <font color="#FF7F7F">_Bozza_</font>.

---

> [!definizione]+ Definizione: informatica
> 
> L'**informatica** (termine che deriva dal francese _informatique_, ottenuto dalla contrazione _informazione automatica_) è la [scienza](Scienza.md#^definizione-scienza) che studia l'[informazione](Informatica.md#^definizione-informazione) e come trattarla in modo automatico, cioè tramite [computer](Informatica.md#^definizione-computer).
^definizione-informatica

%% 
\### Due anime complementari

\#### Informatica teorica

Si occupa dei fondamenti matematici e logici:

- **Teoria della computabilità** — cosa può essere calcolato in linea di principio
- **Teoria della complessità** — quante risorse (tempo, memoria) richiede un calcolo
- **Teoria degli algoritmi** — progettazione e analisi di procedure risolutive
- **Teoria dei linguaggi formali** — grammatiche, automi, compilatori
- **Logica e semantica** — fondamenti dei linguaggi di programmazione

\#### Informatica applicata

Si occupa della realizzazione concreta di sistemi:

- Programmazione e ingegneria del software
- Basi di dati
- Reti e sistemi distribuiti
- Intelligenza artificiale
- Sistemi operativi
- Sicurezza informatica
%%

Ma cos'è esattamente un'[_informazione_](Informatica.md#^definizione-informazione)? E cosa rappresenta invece il termine [_dato_](Informatica.md#^definizione-dato)? Sebbene vengano usati spesso in maniera intercambiabile, i termini [_dato_](Informatica.md#^definizione-dato) e [_informazione_](Informatica.md#^definizione-informazione) hanno significati ben distinti.

> [!definizione]+ Definizione: dato
> 
> Un **dato** è una rappresentazione elementare (numerica, testuale, visiva, ecc.) di un fenomeno della realtà che si vuole rappresentare. È grezzo e privo di significato di per sé e senza un contesto o un'interpretazione non ha valore informativo e non ci dice nulla.
^definizione-dato

I [dati](Basi%20di%20dati.md#^definizione-dato), però, se aggregati, possono rappresentare un'[_informazione_](Informatica.md#^definizione-informazione).

> [!definizione]+ Definizione: informazione
> 
> Un'**informazione** è il risultato dell'interpretazione e della correlazione di uno o più [dati](Basi%20di%20dati.md#^definizione-dato) inquadrati in un determinato contesto.
^definizione-informazione

> [!esempio]- Esempio di differenza tra dato e informazione
> 
> Immaginiamo di avere come [dati](Basi%20di%20dati.md#^definizione-dato) la scritta `Mario Rossi` e il numero `741` scritti su un foglio di carta. Da soli, questi elementi non hanno un significato chiaro; tuttavia, se sappiamo che il foglio risponde alla domanda _"chi è il responsabile del Dipartimento di Informatica e qual è la sua matricola?"_, allora possiamo interpretare i [dati](Basi%20di%20dati.md#^definizione-dato) e ottenere l'[informazione](Basi%20di%20dati.md#^definizione-informazione) che Mario Rossi è il responsabile del Dipartimento di Informatica e il suo numero di telefono è 741.

In sintesi, i [dati](Basi%20di%20dati.md#^definizione-dato) diventano [informazioni](Basi%20di%20dati.md#^definizione-informazione) quando vengono elaborati, contestualizzati e resi comprensibili per un determinato scopo.

> [!definizione]+ Definizione: computer
> 
> Un **computer** (o, in italiano, **calcolatore** o **elaboratore**) è una macchina elettronica capace di ricevere dati in ingresso, elaborarli seguendo una serie di istruzioni e restituire un risultato in uscita.
^definizione-computer

Un [computer](Informatica.md#^definizione-computer) spesso fa parte di un [sistema informatico](Informatica.md#^definizione-sistema-informatico).

> [!definizione]+ Definizione: sistema informatico
> 
> Un **sistema informatico** è un insieme organizzato di componenti che lavorano insieme per raccogliere, elaborare, conservare e trasmettere [informazioni](Informatica.md#^definizione-informazione).
> 
> Le due componenti fondamentali di ogni **sistema informatico**, inseparabili e complementari, sono l'[hardware](Informatica.md#^definizione-hardware) e il [software](Informatica.md#^definizione-software).
^definizione-sistema-informatico

# 1 - Hardware

> [!definizione]+ Definizione: hardware
> 
> L'**hardware** è l'insieme dei componenti fisici e tangibili di un [sistema informatico](Informatica.md#^definizione-sistema-informatico), cioè comprende tutto ciò che si può vedere e toccare: il processore, la memoria, lo schermo, la tastiera, i cavi%% link a tutto %%. È la parte "materiale" di un [computer](Informatica.md#^definizione-computer), quella che esegue concretamente le operazioni.
^definizione-hardware

# 2 - Software

> [!definizione]+ Definizione: software
> 
> Il **software** è la parte immateriale di un [sistema informatico](Informatica.md#^definizione-sistema-informatico), cioè comprende tutto ciò che non si può vedere o toccare ed è la parte che comprende i programmi%% link %% e le istruzioni%% link %% che comandano l'[hardware](Informatica.md#^definizione-hardware).
^definizione-software

> [!definizione]+ Definizione: istruzione
> 
> Un'**istruzione** è il comando elementare che un [computer](Informatica.md#^definizione-computer) è in grado di eseguire.
^definizione-istruzione

%% 
Esempi concreti
In linguaggio umano, un'istruzione assomiglia a:

"Somma questi due numeri"
"Confronta A con B"
"Scrivi questo testo sullo schermo"
"Vai alla riga 10"
"Leggi il valore inserito dall'utente"
%%

%% 
\### Caratteristiche di un'istruzione

- È **elementare** — non si scompone in operazioni più semplici
- È **precisa** — non ammette ambiguità
- È **eseguibile** — la macchina sa esattamente come svolgerla
%%

Le [istruzioni](Informatica.md#^definizione-istruzione) compongono i [_programmi_](Informatica.md#^definizione-programma).

> [!definizione]+ Definizione: programma
> 
> Un **programma** è una sequenza di [istruzioni](Informatica.md#^definizione-istruzione) scritte in un linguaggio comprensibile al [computer](Informatica.md#^definizione-computer) che descrive come eseguire un compito specifico, prendendo [dati](Informatica.md#^definizione-dato) in ingresso (detti [input](Informatica.md#^definizione-input)) e restituendo altri [dati](Informatica.md#^definizione-dato) in uscita (detti [output](Informatica.md#^definizione-output)).
^definizione-programma

%% 
**Esempi:**

- Un programma che calcola la media di una serie di numeri
- Un programma che apre un file e ne mostra il contenuto
- Un programma che gestisce il login di un utente
%%

%% 
\### Differenza tra programma e software

Sono termini spesso usati come sinonimi, ma c'è una sfumatura importante:

||Programma|Software|
|---|---|---|
|**Cosa è**|Una singola sequenza di istruzioni|Un insieme più ampio|
|**Ampiezza**|Specifico, limitato a un compito|Può includere più programmi|
|**Contiene**|Istruzioni|Programmi + dati + configurazioni + documentazione|

---

\### In parole semplici

> Un **programma** è come un singolo capitolo. Il **software** è l'intero libro.

Microsoft Word, per esempio, è un software — ma al suo interno contiene decine di programmi distinti: uno gestisce la tastiera, uno salva i file, uno corregge l'ortografia, e così via.
%%

> [!definizione]+ Definizione: input
> 
> L'**input** (in italiano _mettere dentro_) è qualsiasi [dato](Informatica.md#^definizione-dato) fornito dall'esterno a un [computer](Informatica.md#^definizione-computer) affinché lo elabori attraverso un [programma](Informatica.md#^definizione-programma).
^definizione-input

%% 
**Esempi:**
- Premere un tasto sulla tastiera
- Cliccare con il mouse
- Parlare in un microfono
- Caricare un file
- Toccare lo schermo di uno smartphone
%%

> [!definizione]+ Definizione: output
> 
> L'**output** (in italiano _mettere fuori_) è qualsiasi [dato](Informatica.md#^definizione-dato) che il [computer](Informatica.md#^definizione-computer) fornisce in uscita dopo aver elaborato un [input](Informatica.md#^definizione-input) attraverso un [programma](Informatica.md#^definizione-programma).
^definizione-output

%% 
**Esempi:**
- Il testo che appare sullo schermo
- Un documento stampato
- Un suono emesso dagli altoparlanti
- Un file salvato
- Una risposta di un'intelligenza artificiale
%%

Un [software](Informatica.md#^definizione-software) non è quasi mai autosufficiente: piuttosto, dipende da altri [software](Informatica.md#^definizione-software) per svolgere parte del lavoro. Queste sono le sue [_dipendenze_](Informatica.md#^definizione-dipendenza).

> [!definizione]+ Definizione: dipendenza
> 
> Una **dipendenza** è un [programma](Informatica.md#^definizione-programma) di cui un [software](Informatica.md#^definizione-software) ha bisogno per funzionare, ma che non contiene al proprio interno.
^definizione-dipendenza

%% 
\### Analogia

Pensa a una ricetta:

- La ricetta è il tuo **programma**
- Gli ingredienti (farina, uova, latte...) sono le **dipendenze** — non li produci tu, li prendi già pronti dal supermercato

Se manca un ingrediente, la ricetta non funziona. Stesso discorso per il software.

---

\### Esempio concreto

Un'app che mostra le previsioni meteo potrebbe dipendere da:

- Una **libreria** per connettersi a internet
- Un **servizio esterno** che fornisce i dati meteorologici
- Un **componente grafico** per disegnare i grafici

Lo sviluppatore non ha scritto tutto questo da zero — lo ha "preso" da altri e lo usa nel suo programma.

---

\### Perché esistono

Perché non ha senso **reinventare la ruota** ogni volta. Se qualcuno ha già scritto un componente che funziona bene, conviene usarlo invece di riscriverlo.
%%

---

%% 
Fonti:
- Tesi di Eelco Dastra
%%

> [!fonti]+ Fonti
> 
> 
