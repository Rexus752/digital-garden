
> [!premessa]+ Premessa
> 
> Ciao! Se è la prima volta che capiti su questo sito, ti consiglio di consultare la [pagina principale](index.md) di questo cosiddetto _Giardino Digitale_ per scoprire meglio cos'è e come navigarlo.
> 
> Lo stato di questa nota è al momento: 🔴 <font color="#FF7F7F">_Bozza_</font>.

---

> [!definizione]+ Definizione: distribuzione del software
> 
> La **distribuzione del [software](Informatica.md#^definizione-software)** è il processo in cui si distribuisce un [software](Informatica.md#^definizione-software) dal [computer](Informatica.md#^definizione-computer) su cui è stato creato, ossia quello dello sviluppatore%% link %%, a quelli degli utenti finali%% link %%.
^definizione-distribuzione-del-software

> [!definizione]+ Definizione: distribuzione corretta
> 
> La **[distribuzione di un software](Distribuzione%20del%20software.md#^definizione-distribuzione-del-software)** si dice **_corretta_** quando, a parità di input%% link %%, il [software](Informatica.md#^definizione-software) si comporta allo stesso modo su ogni [computer](Informatica.md#^definizione-computer) su cui è stato distribuito.
^definizione-distribuzione-corretta

Molto semplicemente, se creo un [software](Informatica.md#^definizione-software) su un mio [computer](Informatica.md#^definizione-computer), durante la fase di [distribuzione](Distribuzione%20del%20software.md#^definizione-distribuzione-del-software) devo assicurarmi che, una volta che lo trasferisco su un altro [computer](Informatica.md#^definizione-computer), si comporti allo stesso modo.

> [!esempio]- Esempio di distribuzione corretta
> 
> Io creo un programma%% link %% che somma due numeri: lo eseguo sul mio [computer](Informatica.md#^definizione-computer) e, dandogli in input $7$ e $5$, mi restituisce $12$.
> 
> Allo stesso modo, se la [distribuzione](Distribuzione%20del%20software.md#^definizione-distribuzione-del-software) è stata [corretta](Distribuzione%20del%20software.md#^definizione-distribuzione-corretta), se questo stesso programma%% link %% lo trasferisco sul tuo [computer](Informatica.md#^definizione-computer), dandogli in input $7$ e $5$ dovrà sempre restituire $12$.

La [distribuzione corretta](Distribuzione%20del%20software.md#^definizione-distribuzione-corretta) dovrebbe essere una cosa molto semplice: per esempio, se ho un [software](Informatica.md#^definizione-software) composto da un insieme di file%% link %%, allora la [distribuzione](Distribuzione%20del%20software.md#^definizione-distribuzione-del-software) consiste semplicemente nel copiare%% Link %% quei file%% link %% nei [computer](Informatica.md#^definizione-computer) degli utenti finali%% link %%. In pratica, questo processo è molto più complicato di così, infatti possono sorgere diversi problemi.

Uno di questi può essere la [_mancanza di dipendenze_](Distribuzione%20del%20software.md#^problema-della-mancanza-di-dipendenze).

%% [!problema] Problema della mancanza di dipendenze %%

> [!osservazione]+ Osservazione: problema della mancanza di dipendenze
> 
> Facciamo finta che uno sviluppatore%% link %% abbia scritto un [software](Informatica.md#^definizione-software) e l'abbia testato su diversi casi d'uso per assicurarsi che il [software](Informatica.md#^definizione-software) funzioni correttamente: può capitare che il [sistema operativo](Sistemi%20operativi.md#^definizione-sistema-operativo) del [computer](Informatica.md#^definizione-computer) dell'utente finale%% link %% non sia esattamente uguale a quello dello sviluppatore%% link %%. Spesso i [software](Informatica.md#^definizione-software) hanno delle [dipendenze](Informatica.md#^definizione-dipendenza) su cui si appoggiano e se queste [dipendenze](Informatica.md#^definizione-dipendenza) non sono presenti nel [computer](Informatica.md#^definizione-computer) dell'utente finale%% link %%, allora il [software](Informatica.md#^definizione-software) non funzionerà correttamente.
> 
> In altre parole: avere lo stesso [software](Informatica.md#^definizione-software) con gli stessi dati%% link %% in input%% link %% non assicura che il risultato sia lo stesso su ogni [computer](Informatica.md#^definizione-computer).
^problema-della-mancanza-di-dipendenze

Un altro problema possibile è l'[_interferenza tra dipendenze_](Distribuzione%20del%20software.md#^problema-dell-interferenza-tra-dipendenze).

%% [!problema] Problema dell'interferenza tra dipendenze %%

> [!osservazione]+ Osservazione: problema dell'interferenza tra dipendenze
> 
> L'aggiornamento%% link %% di un [software](Informatica.md#^definizione-software) $X$ può necessitare anche dell'aggiornamento delle [dipendenze](Informatica.md#^definizione-dipendenza) $Y$ su cui poggia: tuttavia, ci può essere un terzo [software](Informatica.md#^definizione-software) $Z$ che [dipende](Informatica.md#^definizione-dipendenza) da $Y$ e che potrebbe risultare incompatibile dall'aggiornamento%% link %% di quest'ultimo.
> 
> ```mermaid
> graph TD
> 	X ---> Y
> 	Z ---> Y
> ```
^problema-dell-interferenza-tra-dipendenze

%% Per approfondire i problemi ambientali, vedere tesi di Eelco Dolstra:

In pratica, questo processo è molto più complicato di così per diversi motivi, ascrivibili in due categorie: i _problemi ambientali_ e i _problemi di gestione_.

Problemi ambientali:

[!osservazione]+ Osservazione: problemi ambientali della distribuzione del software

I problemi ambientali della [distribuzione del software](Distribuzione%20del%20software.md#^definizione-distribuzione-del-software) riguardano essenzialmente la sua [correttezza](Distribuzione%20del%20software.md#^definizione-distribuzione-corretta). Il [software](Informatica.md#^definizione-software) può richiedere alcuni requisiti riguardo l'ambiente in cui viene eseguito, come la presenza di altri [software](Informatica.md#^definizione-software) da cui [dipende](Informatica.md#^definizione-dipendenza), l'esistenza di determinati fileLINK di configurazione e così via. Se una qualsiasi di queste caratteristiche dell’ambiente non è soddisfatta, esiste la possibilità che il [software](Informatica.md#^definizione-software) **non funzioni allo stesso modo** rispetto alla macchina dello sviluppatoreLINK, non assicurando così la [correttezza della distribuzione](Distribuzione%20del%20software.md#^definizione-distribuzione-corretta).

In sostanza, anche avendo lo stesso programmaLINK con lo stesso inputLINK, potrebbe non comportarsi allo stesso modo su ogni computerLINK.

Per esempio:
- Per una [distribuzione corretta](Distribuzione%20del%20software.md#^definizione-distribuzione-corretta) è necessario che lo sviluppatoreLINK identifichi tutte le [dipendenze](Informatica.md#^definizione-dipendenza) su cui regge il proprio softwareLINK. Facciamo finta che nel mio softwareLINK $X$ io abbia usato le [dipendenze](Informatica.md#^definizione-dipendenza) $a$, $b$ e $c$: nella specifica delle [dipendenze](Informatica.md#^definizione-dipendenza) potrei aver dimenticato di identificare $c$ (pensiamo a un softwareLINK con centinaia di dipendenze), ma non ho modo di verificarlo facilmente perché potrei non accorgermene se $c$ è già presente sul mio computerLINK.
- Le [dipendenze](Informatica.md#^definizione-dipendenza) devono inoltre essere compatibili con ciò che il [software](Informatica.md#^definizione-software) che le utilizza si aspetta. In generale, non tutte le versioniLINK di un [software](Informatica.md#^definizione-software) funzionano. Questo vale anche in presenza di interfacce con controllo dei tipi, perché le interfacce non forniscono mai una specifica completa del comportamento osservabile di un componente. Inoltre, i componenti spesso presentano **variabilità in fase di build**, cioè possono essere compilati con o senza certe funzionalità opzionali, o con parametri diversi scelti al momento della compilazione. Peggio ancora, un componente può dipendere da uno specifico compilatore o da particolari opzioni di compilazione usate per le sue dipendenze (ad esempio per la compatibilità dell’**ABI – Application Binary Interface**).
 %%

%% 
Hashing per verificare il corretto download (per esempio delle ISO)
%%

---

%% 
Fonti:
- Eelco Dastra
- https://www.youtube.com/watch?v=nLwbNhSxLd4
%%

> [!fonti]+ Fonti
> 
> 
