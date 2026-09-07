
> [!premessa]+ Premessa
> 
> Ciao! Se è la prima volta che capiti su questo sito, ti consiglio di consultare la [pagina principale](index.md) di questo cosiddetto _Giardino Digitale_ per scoprire meglio cos'è e come navigarlo.
> 
> Lo stato di questa nota è al momento: 🔴 <font color="#FF7F7F">_Bozza_</font>.

---

[Nix](Informatica/Nix/Nix.md#^definizione-package-manager-nix) è il punto d'ingresso a un _rabbit hole_ in cui sono cascato ormai anni fa e da cui non ne sono più uscito, complice anche il fatto che da [Nix](Informatica/Nix/Nix.md#^definizione-package-manager-nix) deriva il [sistema operativo _NixOS_](Informatica/Sistemi%20operativi/NixOS/NixOS.md#^definizione-nixos) che è tutt'ora il [sistema operativo](Informatica/Sistemi%20operativi/Sistemi%20operativi.md#^definizione-sistema-operativo) che principalmente uso.

Un buon punto di partenza per capire cos'è esattamente [Nix](Informatica/Nix/Nix.md#^definizione-package-manager-nix) e come funziona tutto il suo ecosistema sono le [_Nix Pills_](https://nixos.org/guides/nix-pills/), una serie di tutorial pensati per spiegare [Nix](Informatica/Nix/Nix.md#^definizione-package-manager-nix) in modo progressivo. Molti dei contenuti delle note riguardanti [Nix](Informatica/Nix/Nix.md#^definizione-package-manager-nix) nel mio Giardino Digitale sono presi dalle [_Nix Pills_](https://nixos.org/guides/nix-pills/).

Non spiegherò qui nei dettagli come installare [Nix](Informatica/Nix/Nix.md#^definizione-package-manager-nix) (per quello c'è la [documentazione ufficiale](https://nix.dev/install-nix#install-nix)), ma piuttosto preferisco spiegarti cos'è e perché dovresti usarlo.

# 1 - Introduzione a Nix

Ok, [Nix](Informatica/Nix/Nix.md#^definizione-package-manager-nix) è un package manager%% link %%, ma cos'ha di speciale? Perché dovrei usarlo? Te lo spiego subito.

## 1.1 - Pacchetti come _derivazioni_

%% 
nel mondo dei sistemi UNIX-likeLINK, la maggior parte (se non tutti) i package managerLINK più diffusi (es. dpkgLINK, rpmLINK, ecc.) modificano lo stato globale del [sistema operativo](Informatica/Sistemi%20operativi/Sistemi%20operativi.md#^definizione-sistema-operativo). Se un packageLINK `foo-1.0` installa un programmaLINK nella cartellaLINK `/usr/bin/foo`, non puoi installare anche `foo-1.1`, a meno di cambiare i percorsi di installazione o il nome del binarioLINK. Ma cambiare i nomi dei binari significa rompere i programmi che li usano.

Esistono alcuni tentativi di mitigare questo problema. DebianLINK, per esempio, lo risolve parzialmente con il sistema delle alternativesLINK.

Quindi, anche se in teoria con alcuni sistemi attuali è possibile installare più versioni dello stesso pacchettoLINK, in pratica è un dito in culo. Ancora peggio, immagina di voler utilizzare due versioni diverse di un desktop environmentLINK come GNOMELINK.

Certo, al giorno d'oggi esistono soluzioni come i containerLINK o strumenti come `virtualenv`LINK, ma a quel punto riuscire a far comunicare tra di loro le due parti diventa un'impresa titanica.
%%

Nel 2003, uno sviluppatore nederlandese di nome Eelco Dolstra%% link %% progetta un nuovo package manager%% link %% come progetto di ricerca presso l'Università di Utrecht, nei Paesi Bassi. Qui nasce l'idea di [Nix](Informatica/Nix/Nix.md#^definizione-package-manager-nix) che qualche anno dopo verrà approfondita nella sua tesi di dottorato del 2006, dal titolo _The Purely Functional Software Deployment Model_ (disponibile [qui](https://edolstra.github.io/pubs/phd-thesis.pdf)), in cui Dolstra%% link %% descrive un approccio che punta a risolvere i problemi degli approcci tradizionali alla [distribuzione di software](Informatica/Distribuzione%20del%20software.md#^definizione-distribuzione-del-software), come la [mancanza di dipendenze](Informatica/Distribuzione%20del%20software.md#^problema-della-mancanza-di-dipendenze) o l'[interferenza tra dipendenze](Informatica/Distribuzione%20del%20software.md#^problema-dell-interferenza-tra-dipendenze).

Per farlo, Dolstra%% link %% utilizza un semplice ma geniale trucco: ogni pacchetto%% link %% viene isolato in una cartella%% link %% a se stante e, anziché conservare il pacchetto%% link %% vero e proprio, il [sistema operativo](Informatica/Sistemi%20operativi/Sistemi%20operativi.md#^definizione-sistema-operativo) si salva una sua "descrizione", detta [_derivazione_](Informatica/Nix/Nix.md#^definizione-derivazione), che specifica come costruire il pacchetto%% link %%, incluse le sue [dipendenze](Informatica.md#^definizione-dipendenza).

Le [derivazioni](Informatica/Nix/Nix.md#^definizione-derivazione) sono espresse (o meglio, _dichiarate_) sotto forma di funzioni%% link %% che prendono in input le [dipendenze](Informatica.md#^definizione-dipendenza) del pacchetto%% link %% in questione e il cui risultato è l'installazione%% link %% del pacchetto%% link %% nel [sistema operativo](Informatica/Sistemi%20operativi/Sistemi%20operativi.md#^definizione-sistema-operativo).

Questo metodo sfrutta i vantaggi sia del [paradigma dichiarativo](Paradigma%20dichiarativo.md#^definizione-paradigma-dichiarativo) che di quello [funzionale](Paradigma%20funzionale.md#^definizione-paradigma-funzionale). I pacchetti%% link %% sono rappresentati sotto forma di funzioni%% link %% e una delle proprietà del [paradigma funzionale](Paradigma%20funzionale.md#^definizione-paradigma-funzionale) è proprio il determinismo%% link %%, per cui una funzione%% link %%, dati determinati argomenti%% link %% in input%% link %%, produce sempre gli stessi risultati%% link %%.%% Vantaggi del paradigma dichiarativo? %%

Ecco perché [Nix](Informatica/Nix/Nix.md#^definizione-package-manager-nix) è una delle scelte migliori nell'ambito della [distribuzione del software](Informatica/Distribuzione%20del%20software.md#^definizione-distribuzione-del-software).

> [!definizione]+ Definizione: derivazione
> 
> In [Nix](Informatica/Nix/Nix.md#^definizione-package-manager-nix), una **derivazione** è una descrizione dichiarativa%% link %% della build di un pacchetto%% link %%, espressa sotto forma di una funzione%% link %% che prende come input%% link %% le [dipendenze](Informatica.md#^definizione-dipendenza) del pacchetto%% link %% e il cui risultato è l'installazione%% link %% del pacchetto%% link %% nel [sistema operativo](Informatica/Sistemi%20operativi/Sistemi%20operativi.md#^definizione-sistema-operativo).
> 
> Una **derivazione** è racchiusa in una cartella il cui nome è del formato
> 
> ```
> hash-nome
> ```
> 
> dove:
> - **`hash`** è una stringa che identifica univocamente la [derivazione](Informatica/Nix/Nix.md#^definizione-derivazione) e
> - **`nome`** è il nome della [derivazione](Informatica/Nix/Nix.md#^definizione-derivazione).
^definizione-derivazione

%% 
dove l’hash identifica in modo univoco la derivazione (non è del tutto vero, è un po’ più complesso),
%%

Ciò significa che [Nix](Informatica/Nix/Nix.md#^definizione-package-manager-nix) non lavora direttamente sui pacchetti%% link %%, ma su come ottenere quei pacchetti%% link %% dal loro codice sorgente%% link %%.

> [!attenzione]+ Attenzione: _derivazione_ e _pacchetto_ come sinonimi
> 
> Pur non essendo esattamente la stessa cosa, in queste note potrei usare per comodità i termini [_derivazione_](Informatica/Nix/Nix.md#^definizione-derivazione) e _pacchetto_%% link %% come sinonimi.

%% 
Fai attenzione poi alla caratteristica delle [derivazioni](Informatica/Nix/Nix.md#^definizione-derivazione) di essere _immutabili_: più tardi la analizzeremo meglio.
 %%
 
%% 
### 1.1.1 - Proprietà delle derivazioni

- isolamento: ogni derivazione è isolata dall'altra
	- vantaggi: posso avere diverse versioni dello stesso pacchetto, risolvendo il problema dell'interferenza
	- L'isolamento permette anche di avere più versioni dello stesso pacchetto, che normalmente sarebbe difficile da ottenere con i package manager tradizionali. Ciò risolve il [problema dell'interferenza tra dipendenze](Informatica/Distribuzione%20del%20software.md#^problema-dell-interferenza-tra-dipendenze), perché [Nix](Informatica/Nix/Nix.md#^definizione-package-manager-nix) ci permette di avere due versioni separate delle stesse [dipendenze](Informatica.md#^definizione-dipendenza) per i diversi [software](Informatica.md#^definizione-software) che le richiedono.
- immutabilità: una derivazione è immutabile
	- vantaggi: quando si aggiorna un pacchetto, la nuova versione non sostituisce la precedente ma entrambe coesistono all'interno del sistema operativo.
- atomicità: durante l'aggiornamento dei pacchetti con i tradizionali package manager, c'è una finestra di tempo (seppur breve) in cui una parte del sistema è stata aggiornata e un'altra no. Se l'aggiornamento viene interrotto in questo esatto momento, il sistema potrebbe rompersi. Con Nix, dato che i vecchi pacchetti rimangono all'interno del sistema operativo, il sistema non rimane mai in uno stato inconsistente in cui rischia di rompersi. Il sistema o si è aggiornato o non si è aggiornato, non ci sono vie di mezzo. 
- univocità
- determinismo: con gli stessi software e dati in input, otterremo lo stesso risultato, a prescindere dalla situazione del resto del sistema operativo. Ciò è possibile grazie all'isolamento dei pacchetti. Se un software funziona su un computer, funzionerà su ogni altro computer. Al contrario, se non funziona su un computer, non funzionerà nemmeno sugli altri.
%%

## 1.2 - Il Nix store

Le [derivazioni](Informatica/Nix/Nix.md#^definizione-derivazione) sono raccolte nel [_Nix store_](Informatica/Nix/Nix.md#^definizione-nix-store) (dove il termine _store_ va inteso non come _negozio_, ma come _deposito_).

> [!definizione]+ Definizione: Nix store
> 
> Il **Nix store** è una cartella del [sistema operativo](Informatica/Sistemi%20operativi/Sistemi%20operativi.md#^definizione-sistema-operativo) (solitamente `/nix/store`) in cui [Nix](Informatica/Nix/Nix.md#^definizione-package-manager-nix) memorizza tutte le [derivazioni](Informatica/Nix/Nix.md#^definizione-derivazione) al suo interno.
^definizione-nix-store

> [!esempio]- Esempio di derivazione nel Nix store
> 
> Prendiamo come esempio una [derivazione](Informatica/Nix/Nix.md#^definizione-derivazione) di bash%% link %% contenuta nel [Nix store](Informatica/Nix/Nix.md#^definizione-nix-store):
> 
> ```
> /nix/store/s4zia7hhqkin1di0f187b79sa2srhv6k-bash-4.2-p45/
> ```
> 
> All'interno di questa cartella potremo trovare il binario%% link %% di bash%% link %%, ossia il `/bin/bash` che conosciamo tutti, al percorso%% link %%
> 
> ```
> /nix/store/s4zia7hhqkin1di0f187b79sa2srhv6k-bash-4.2-p45/bin/bash
> ```
> 
> Ogni volta che vorremo usare il programma%% link %% bash%% link %%, dovremo far riferimento a questo binario%% link %% presente nel [Nix store](Informatica/Nix/Nix.md#^definizione-nix-store).

Ovviamente, per rendere questi programmi comodi da usare%% link %%, [Nix](Informatica/Nix/Nix.md#^definizione-package-manager-nix) si occupa di far comparire i binari%% link %% nel tuo `PATH`%% link %% nel modo appropriato.

Ciò evita anche il problema di avere pacchetti%% link %% sparsi per tutto il file system%% link %%: se stiamo cercando un pacchetto%% link %% (o meglio, in questo caso una [derivazione](Informatica/Nix/Nix.md#^definizione-derivazione), sappiamo che la troveremo sicuramente nel [Nix store](Informatica/Nix/Nix.md#^definizione-nix-store)).

In sostanza, quello che abbiamo è un archivio (il [Nix store](Informatica/Nix/Nix.md#^definizione-nix-store)) di tutti i pacchetti (sotto forma di [derivazioni](Informatica/Nix/Nix.md#^definizione-derivazione)), a volte anche con versioni multiple ma distinte (grazie all'univocità%% link %% della [derivazione](Informatica/Nix/Nix.md#^definizione-derivazione)).

> [!osservazione]+ Osservazione: comportamento di Nix con le dipendenze
> 
> Come si comporta [Nix](Informatica/Nix/Nix.md#^definizione-package-manager-nix) per le [dipendenze](Informatica.md#^definizione-dipendenza)? [Nix](Informatica/Nix/Nix.md#^definizione-package-manager-nix) si assicura di collegare a ogni [derivazione](Informatica/Nix/Nix.md#^definizione-derivazione) le proprie [dipendenze](Informatica.md#^definizione-dipendenza), a loro volta gestite tramite altre [derivazioni](Informatica/Nix/Nix.md#^definizione-derivazione).
> 
> Mi spiego meglio: facciamo finta che io stia usando bash%% link %% con la versione 5.2.26 che ha come dipendenza glibc%% link %% versione 2.42. Grazie all'indipendenza tra le [derivazioni](Informatica/Nix/Nix.md#^definizione-derivazione), posso decidere di usare nello stesso [sistema operativo](Informatica/Sistemi%20operativi/Sistemi%20operativi.md#^definizione-sistema-operativo) anche bash%% link %% 5.2.27 che ha come dipendenza glibc%% link %% versione 2.43. Allo stesso modo, potrei usare contemporaneamente un modulo%% link %% di Python 2.7%% link %% compilato con gcc 4.6%% link %% e lo stesso modulo%% link %% ma scritto in Python 3%% link %% compilato con gcc 4.8%% link %%.
> 
> In altre parole, [Nix](Informatica/Nix/Nix.md#^definizione-package-manager-nix) offre solo [dipendenze](Informatica.md#^definizione-dipendenza) "dirette" da una [derivazione](Informatica/Nix/Nix.md#^definizione-derivazione) a un'altra [derivazione](Informatica/Nix/Nix.md#^definizione-derivazione).

Insomma, [Nix](Informatica/Nix/Nix.md#^definizione-package-manager-nix) ti permette di usare pacchetti%% link %% e [configurazioni](Informatica/Sistemi%20operativi/Sistemi%20operativi.md#^definizione-configurazione-di-un-sistema-operativo) in modo isolato, riproducibile e senza conflitti e gestendo più versioni dello stesso [software](Informatica.md#^definizione-software) contemporaneamente. Rappresenta un _deus ex machina_ per chi ha sempre voluto un [sistema](Informatica/Sistemi%20operativi/Sistemi%20operativi.md#^definizione-sistema-operativo) in cui la gestione di pacchetti%% link %% e delle loro [dipendenze](Informatica.md#^definizione-dipendenza) non sono un incubo.

> [!definizione]+ Definizione: package manager Nix
> 
> **Nix** è un package manager%% link %% per sistemi UNIX-like%% link %%, ideato dallo sviluppatore nederlandese Eelco Dolstra%% link %%, in cui ogni pacchetto%% link %% è rappresentato da una [derivazione](Informatica/Nix/Nix.md#^definizione-derivazione) che determina come costruirlo%% link %% e il cui risultato viene memorizzato nel [Nix store](Informatica/Nix/Nix.md#^definizione-nix-store) che garantisce isolamento, immutabilità e univocità delle [derivazioni](Informatica/Nix/Nix.md#^definizione-derivazione) stesse.
^definizione-package-manager-nix

> [!osservazione]+ Osservazione: parallelismo tra i package manager e i linguaggi di programmazione
> 
> [Nix](Informatica/Nix/Nix.md#^definizione-package-manager-nix) sta ai pacchetti%% link %% come linguaggi a basso livello%% link %% come il C%% link %% stanno alla memoria%% link %%:
> - come "contenitore", al posto della RAM%% link %%, abbiamo lo spazio sul disco%% link %%;
> - come oggetti su cui operare, anziché variabili%% link %%, abbiamo le [derivazioni](Informatica/Nix/Nix.md#^definizione-derivazione);
> - per accedere a questi oggetti, anziché indirizzi%% link %%, abbiamo i percorsi%% link %% delle [derivazioni](Informatica/Nix/Nix.md#^definizione-derivazione);
> - per riferirsi a questi oggetti, anziché usare i puntatori%% link %%, accediamo alle [derivazioni](Informatica/Nix/Nix.md#^definizione-derivazione) tramite i loro percorsi%% link %% e, al posto dei dangling pointer%% link %%, abbiamo percorsi%% link %% che fanno riferimenti a [derivazioni](Informatica/Nix/Nix.md#^definizione-derivazione) inesistenti;
> - per manipolare questi riferimenti, anziché l'aritmetica dei puntatori%% link %%, abbiamo le operazioni su stringhe che rappresentano i percorsi%% link %% delle [derivazioni](Informatica/Nix/Nix.md#^definizione-derivazione);
> - come struttura dati per gestire il tutto, anziché avere un directory tree%% link %%, abbiamo un dependency tree%% link %%;
> - e così via.
> 
> Allo stesso modo, linguaggi che non hanno una gestione strutturata dei puntatori%% link %%, come Assembly, è comparabile ai package manager%% link %% tradizionali in cui i file dei pacchetti%% link %% sono disorganizzati e sparsi per tutto il file system%% link %%.

## 1.3 - Il Nixpkgs

La lista dei pacchetti%% link %% che [Nix](Informatica/Nix/Nix.md#^definizione-package-manager-nix) ha a disposizione è contenuta nel [_Nixpkgs_](Informatica/Nix/Nix.md#^definizione-nixpkgs).

> [!definizione]+ Definizione: Nixpkgs
> 
> Il **Nixpkgs** (pronuncia: _Nix packages_%% pronuncia IPA %%) è la collezione di pacchetti%% link %% disponibili per il package manager [Nix](Informatica/Nix/Nix.md#^definizione-package-manager-nix).
> 
> Su GitHub%% link %% si può trovare il repository%% link %% completo, disponibile [qui](https://github.com/NixOS/nixpkgs).
^definizione-nixpkgs

%% nella definizione mettere "repository di pacchetti" anziché collezione (e definire cos'è un repository di pacchetti) %%

[Nixpkgs](Informatica/Nix/Nix.md#^definizione-nixpkgs), al momento in cui sto scrivendo questa nota (gennaio 2026), è il repository%% link %% di pacchetti%% link %% più grande al momento, con oltre 120.000 pacchetti%% link %% disponibili.%% AGGIUNGERE FONTE %%

I pacchetti%% link %% all'interno del [Nixpkgs](Informatica/Nix/Nix.md#^definizione-nixpkgs) sono divisi in [_canali_](Informatica/Nix/Nix.md#^definizione-canale).

> [!definizione]+ Definizione: canale
> 
> In [Nix](Informatica/Nix/Nix.md#^definizione-package-manager-nix), un **canale** è una collezione di determinate versioni%% link %% dei pacchetti%% link %% disponibili nel [Nixpkgs](Informatica/Nix/Nix.md#^definizione-nixpkgs).
^definizione-canale

%% [!problema] Problema dell'incompatibilità tra canali %%

> [!osservazione]+ Osservazione: incompatibilità tra canali
> 
> I [canali](Informatica/Nix/Nix.md#^definizione-canale) possono generare alcuni problemi: [computer](Informatica.md#^definizione-computer) diversi potrebbero usare [canali](Informatica/Nix/Nix.md#^definizione-canale) diversi (oppure stessi [canali](Informatica/Nix/Nix.md#^definizione-canale)) e, di conseguenza, non avere a disposizione le stesse versioni%% Link %% degli stessi pacchetti%% link %%.
> 
> Questo problema viene risolto attraverso i _flake_%% link %%.

%% 
Lo script contenuto nella [derivazione](Informatica/Nix/Nix.md#^definizione-derivazione) per costruire un pacchetto è chiamato solitamente `default.nix` e rappresenta una funzioneLINK che prende le [dipendenze](Informatica.md#^definizione-dipendenza) come argomentoLINK e installa un [software](Informatica.md#^definizione-software) come specificato.

Questo script viene poi costruito come derivazione nel Nix store, come un codice sorgente che viene prima trasformato in bytecode e poi compilato nel codice macchina.

mettere foto della sequenza da espressioni Nix a derivaizoni

Durante la traduzione dell'espressione in derivazione, viene creato un hash dal contenuto del file derivato e viene messo come valore del campo `output`.

Prima viene fatto un hash sul file usando lo SHA-256, creando così un hash lungo 256 bit che viene convertito in 52 caratteri:

$$
\frac{256}{\log_2(32)} \approx 52
$$

(perché $\log_2(32)$? forse perché 32 sono i bit dell'architettura)

Dal momento che questi caratteri sono troppi per alcuni file system, Nix tronca l'hash risultante a 160 bit, risultando in una lunghezza di 32 caratteri:

$$
\frac{160}{\log_2(32)} = 32
$$
%%

%% 

# 2 - La Trinità di Nix

Nix, come Dio per la religione cristiana, è un'entità _una e trina_: è un package manager, è un linguaggio ed è un sistema operativo

Nix è come un JSON file con qualche aggiunta, come le funzioni
%%

%% 
Fonti:
- ChatGPT
%%

---

%% 
https://nix-community.github.io/awesome-nix/
https://www.youtube.com/watch?v=5D3nUU1OVx8
https://www.youtube.com/watch?v=S3VBi6kHw5c
https://nixos-and-flakes.thiscute.world/
%%

> [!fonti]+ Fonti
> 
> - 📹 Vimjoyer, [_NixOS beginner guide_](https://www.youtube.com/watch?v=bjTxiFLSNFA), YouTube.
> - 📹 Ampersand, [_Full NixOS Guide: Everything You Need to Know in One Place!_](https://www.youtube.com/watch?v=nLwbNhSxLd4), YouTube.
> - 🌐 Luca "Lethalman" Bruno, [_Nix Pills_](https://nixos.org/guides/nix-pills/00-preface.html), [nixos.org](https://nixos.org/):
> 	- [_1 - Why You Should Give it a Try_](https://nixos.org/guides/nix-pills/01-why-you-should-give-it-a-try.html#why-you-should-give-it-a-try)
