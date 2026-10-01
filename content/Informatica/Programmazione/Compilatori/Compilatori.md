---
aliases:
  - Compilatori
---

> [!premessa]+ Premessa
> 
> Ciao! Se è la prima volta che capiti su questo sito, ti consiglio di consultare la [pagina principale](index.md) di questo cosiddetto _Giardino Digitale_ per scoprire meglio cos'è e come navigarlo.
> 
> Lo stato di questa nota è al momento: 🔴 <font color="#FF7F7F">_Bozza_</font>.

---

All'alba dei tempi della [programmazione](Programmazione.md#^definizione-programmazione) (ossia intorno agli anni '40/'50), i [programmi](Informatica.md#^definizione-programma) venivano scritti direttamente in linguaggio macchina%% Link %% poiché non esistevano ancora i [linguaggi di programmazione](Programmazione.md#^definizione-linguaggio-di-programmazione): la [programmazione](Programmazione.md#^definizione-programmazione) era ovviamente molto difficile perché per noi umani non è semplice dover tradurre le [istruzioni](Informatica.md#^definizione-istruzione) che vogliamo far eseguire a un [computer](Informatica.md#^definizione-computer) in una sequenza di zeri e uno, tenendo anche conto del fatto che ogni [computer](Informatica.md#^definizione-computer) ha una propria architettura%% Link %% e, di conseguenza, un programma scritto per una determinata architettura non funzionerà su ogni computer.

Per questo motivo sono stati inventati i [_linguaggi di programmazione_](Programmazione.md#^definizione-linguaggio-di-programmazione), ossia linguaggi che ci permettono di scrivere [programmi](Informatica.md#^definizione-programma) in un formato più _leggibile_ a noi umani (usando parole inglesi al posto di `0` e `1`).

Tuttavia c'è un problema: un [computer](Informatica.md#^definizione-computer) è in grado di comprendere solo il proprio linguaggio macchina%% Link %% e non capisce i [linguaggi di programmazione](Programmazione.md#^definizione-linguaggio-di-programmazione). Ecco che allora serve un "traduttore" che prenda i [programmi](Informatica.md#^definizione-programma) scritti in un determinato [linguaggio di programmazione](Programmazione.md#^definizione-linguaggio-di-programmazione) e li trasformi in linguaggio macchina%% Link %%: questi "traduttori" sono detti _compilatori_.

%% 
Introdurre in questa definizione "codice sorgente" e "codice macchina"
%%

> [!definizione]+ Definizione: compilatore
> 
> Un **compilatore** è un [programma](Informatica.md#^definizione-programma) che traduce una sequenza di [istruzioni](Informatica.md#^definizione-istruzione) scritte in un [linguaggio di programmazione](Programmazione.md#^definizione-linguaggio-di-programmazione) in linguaggio macchina%% Link %%.
^definizione-compilatore

> [!osservazione]+ Osservazione: a cosa serve studiare i compilatori?
> 
> Al giorno d'oggi (quasi) nessuno realizza più [compilatori](Compilatori.md#^definizione-compilatore) (eccetto se si sta inventando un nuovo [linguaggio di programmazione](Programmazione.md#^definizione-linguaggio-di-programmazione)), ma allora a cosa serve studiarli?
> 
> Innanzitutto, come per qualsiasi altra cosa nel mondo dell'[informatica](Informatica.md#^definizione-informatica) (e non solo), concetti e metodi studiati qua possono essere applicati anche in altri ambiti, come la lettura e l'analisi di [dati](Informatica.md#^definizione-dato) organizzati in strutture dati%% link %%, lo studio di linguaggi formali%% link %%, ecc.

%% 
fare callout per questa roba sotto
%%

Un [compilatore](Compilatori.md#^definizione-compilatore) è diviso in più fasi:
1. Parte dal codice sorgente
2. Fa l'analisi lessicale, generando i token
3. Fa l'analisi sintattica, generando AST
4. Fa l'analisi semantica, generando AST
5. Genera il codice intermedio
6. Ottimizza il codice intermedio
7. Genera il codice oggetto

---

> [!fonti]+ Fonti
> 
> - 🏫 Corso di Laurea in Informatica (`L-31 R`) presso l'Università di Torino:
>     - Corso di _Linguaggi Formali e Traduttori_, A.A. 2026-27 ([pagina Moodle](https://informatica.i-learn.unito.it/course/view.php?id=3735)):
> 		- Prof. Jeremy James Sproston, slide del corso:
> 			- [1.1 - _Motivazione_](https://informatica.i-learn.unito.it/pluginfile.php/510313/mod_folder/content/0/1-1_motivazione.pdf).
> 			- [1.2 - _Organizzazione_](https://informatica.i-learn.unito.it/pluginfile.php/510313/mod_folder/content/0/1-2_organizzazione.pdf).
