Un **thread** (abbreviazione di _**thread of execution**_, in italiano _filo dell'esecuzione_) è l'unità granulare in cui un processo può essere suddiviso e che può essere eseguito a divisione di tempo (cioè assegnando a ognuno una determinata porzione di tempo in cui poter essere eseguito) o in parallelo ad altri thread da parte del processore. In altre parole, un thread è una parte del processo che viene eseguita, in maniera concorrente ed indipendente, internamente allo stato generale del processo stesso.

# 1 - Differenza tra "processo" e "thread"

I termini "processo" e "thread", nonostante a volte vengano usati in maniera interscambiabile, in realtà indicano due cose distinte:
- Un processo è un'istanza di un programma in esecuzione, con risorse e uno spazio di memoria proprio. Ogni processo è indipendente dagli altri e dispone di un proprio spazio di indirizzamento nella memoria, il che significa che i dati di un processo non sono condivisibili direttamente con quelli di un altro processo (salvo meccanismi appositi, come la memoria condivisa o la comunicazione inter-processo).
- Un thread è un'unità di esecuzione all'interno di un processo. Tutti i thread di un processo condividono lo stesso spazio di memoria e le stesse risorse del processo che li contiene. Un singolo processo può avere uno o più thread (concetto di multithreading%%link%%).

Il termine inglese "thread" rende bene l'idea, in quanto si rifà visivamente al concetto di fune metallica composta da vari fili attorcigliati: se la fune è il processo in esecuzione, allora i singoli fili che la compongono sono i thread.
%% mettere l'immagine al lato%%

![150](Thread%20-%20Fune.png)

## 1.1 - Esempio pratico

Ecco un esempio pratico della differenza tra "processo" e "thread".

Immagina di avviare un'applicazione come, per esempio, un editor di testo. Quando l'applicazione viene avviata, il sistema operativo crea un **processo** con il suo spazio di memoria. Se apri una seconda istanza dell'editor, viene creato un nuovo processo.

All'interno dell'editor di testo, ci possono essere più **thread**: uno che gestisce la visualizzazione del testo, un altro che gestisce il salvataggio automatico, e un altro che risponde ai comandi dell'utente. Tutti questi thread lavorano contemporaneamente e condividono lo stesso spazio di memoria, consentendo un'esecuzione fluida e parallela delle operazioni.

## 1.2 - Tabella riassuntiva delle differenze

Ecco una tabella riassuntiva delle differenze tra "processo" e "thread":

| Caratteristica                                                             | **Processo**                                                                     | **Thread**                                                                           |
| -------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------ |
| **Spazio di memoria**                                                      | Ha uno spazio di memoria separato                                                | Condivide lo spazio di memoria con altri thread del processo                         |
| **Isolamento**                                                             | Isolato da altri processi                                                        | Condivide le risorse con altri thread nel processo                                   |
| **Comunicazione**                                                          | Comunicazione tra processi complessa                                             | Comunicazione interna semplice (tramite [memoria condivisa](Memoria%20condivisa.md)) |
| **Esecuzione**                                                             | Un processo può avere uno o più thread, eseguiti separatamente                   | Ogni thread è un'unità di esecuzione all'interno di un processo                      |
| **Crashing**                                                               | Se un processo va in crash, non influenza altri processi                         | Se un thread va in crash, può compromettere l'intero processo                        |
| [**Cambi di contesto**](Processi.md#3.4%20-%20Il%20cambio%20di%20contesto) | Richiede un cambio di contesto completo (salvataggio di registri, memoria, ecc.) | Il cambio di contesto tra thread è più rapido poiché condividono memoria e risorse   |

# 2 - Vantaggi e svantaggi dei thread

I principali vantaggi dei thread sono:
- **Parallelismo**: i thread permettono di eseguire compiti contemporaneamente, sfruttando al meglio i processori multicore%%link%%, il che riduce i tempi di elaborazione per compiti intensivi.
- **Reattività**: nei programmi con interfaccia utente, i thread aiutano a mantenere il programma reattivo, separando i compiti di elaborazione in background dalle operazioni principali (come la gestione dell'interfaccia grafica).
- **Efficienza nella gestione della memoria**: i thread condividono la memoria e le risorse del processo principale, il che riduce la duplicazione e l'uso della memoria rispetto ai processi separati.
- **Minore overhead**: i thread richiedono meno risorse per essere creati rispetto ai processi, poiché condividono risorse e spazio di indirizzamento del processo che li ha generati.
- **Comunicazione più semplice**: condividendo la memoria, i thread possono comunicare tra loro più facilmente, evitando le complessità dei canali di comunicazione tra processi separati.

I principali svantaggi dei thread sono:
- **Complessità nella programmazione**: la programmazione multithreading può essere complessa, specialmente per la gestione della sincronizzazione tra thread, aumentando il rischio di errori come race conditions%%link%% e deadlock%%link%%.
- **Sincronizzazione dei dati**: poiché i thread condividono la memoria, devono sincronizzare l'accesso ai dati condivisi per evitare conflitti e incoerenze, il che può risultare difficile da gestire.
- **Debug difficile**: identificare e risolvere i problemi nei programmi multithreading può essere complesso, soprattutto quando si tratta di bug non deterministici che si verificano solo in determinate condizioni.
- **Scalabilità limitata**: anche se i thread migliorano le prestazioni su CPU multicore, non tutti i problemi possono essere parallelizzati, e oltre un certo limite i benefici si riducono.
- **Rischio di deadlock e starvation**: se i thread non sono ben gestiti, possono bloccarsi in uno stato di attesa reciproca (_deadlock_) o essere "affamati" di risorse, restando bloccati e incapaci di completare il loro compito (_starvation_).

# Fonti

- Abraham Silberschatz, Peter Baer Galvin, Greg Gagne - [Sistemi Operativi (10ᵃ Edizione)](https://he.pearson.it/catalogo/1099) - Pearson, 2019 - ISBN: `9788891904560`.
- Slide del Prof. Aldinucci Marco del corso di Sistemi Operativi (canale B), Corso di Laurea in Informatica presso l'Università di Torino, A.A. 2024-25:
	- [Cap_03](https://informatica.i-learn.unito.it/mod/resource/view.php?id=253884)
