---
title: NixOS
---

> [!premessa] Premessa
> 
> Ciao! Se è la prima volta che capiti su questo sito, ti consiglio di consultare la [pagina principale](index.md) di questo cosiddetto _Giardino Digitale_ per scoprire meglio cos'è e come navigarlo.
> 
> Lo stato di questa nota è al momento: 🔴 <font color="#FF7F7F">_Bozza_</font>.

---

%% 
https://nixos.org/guides/nix-pills/00-preface.html
%%

[NixOS](NixOS.md#^definizione-nixos) è il mio [sistema operativo](Sistemi%20operativi.md#^definizione-sistema-operativo) principale dal 2024 e ho deciso di scrivere questa nota sul mio Giardino Digitale per divulgare tutto ciò che ho imparato nel corso di questi anni sul ✨magico mondo✨ di [NixOS](NixOS.md#^definizione-nixos) e permettere a chiunque ne possa essere interessato di superare facilmente tutti gli ostacoli che ho dovuto affrontare anche io nell'usarlo.

Senza girarci troppo intorno, diciamoci le cose così come stanno. Si sa che ogni utente di Linux%% link %% cerca di vendere la propria distribuzione Linux in uso come se fosse la panacea per tutti i mali di questo mondo, cercando di convincere chiunque lo ascolti di avere il cazzo più marmoreo fra tutti perché la propria distribuzione Linux è quella perfetta.

Proprio per queste ragioni, con questa nota non voglio assolutamente insinuare che [NixOS](NixOS.md#^definizione-nixos) sia la distribuzione perfetta, ma semplicemente offrire il mio punto di vista da utente di [NixOS](NixOS.md#^definizione-nixos) sulle sue peculiarità e i motivi che mi hanno spinto a sceglierla e che tutt'ora mi fanno desistere dal passare stabilmente ad altre distribuzioni.

# Introduzione a NixOS

Ma quindi, cos'è [NixOS](NixOS.md#^definizione-nixos) e perché dovrei usarlo?

Innanzitutto, partiamo col dire che [NixOS](NixOS.md#^definizione-nixos) è una distribuzione Linux%% link %% basata sul [package manager Nix](Nix.md#^definizione-package-manager-nix). Inizialmente [Nix](Nix.md#^definizione-nix-store) era disponibile per sistemi UNIX-like%% Link %%, ma c'erano molti dubbi sul fatto che si potesse creare a tutti gli effetti un [sistema operativo](Sistemi%20operativi.md#^definizione-sistema-operativo) basato su di esso.

Tuttavia, Eelco Dolstra%% link %% (il creatore di [Nix](Nix.md#^definizione-package-manager-nix)) precisò già a suo tempo%% nella sua tesi di dottorato in cui introduceva Nix %% che i moderni metodi di gestione delle [configurazioni dei sistemi operativi](Sistemi%20operativi.md#^definizione-configurazione-di-un-sistema-operativo), esattamente come per la [distribuzione del software](Distribuzione%20del%20software.md#^definizione-distribuzione-del-software), erano parecchio caotici: i file di configurazione%% link %%, così come i pacchetti%% link %%, erano sparsi per tutto il file system

> [!definizione] Definizione: NixOS
> 
> **NixOS** è una distribuzione Linux%% link %% basata sul [package manager Nix](Nix.md#^definizione-package-manager-nix). È un [sistema operativo dichiarativo](Dichiaratività%20e%20imperatività%20nei%20SO.md#^definizione-sistema-operativo-dichiarativo), ossia la [configurazione](Sistemi%20operativi.md#^definizione-configurazione-di-un-sistema-operativo) del [sistema](Sistemi%20operativi.md#^definizione-sistema-operativo) è dichiarata in file%% link %% scritti in linguaggio Nix%% link %% e gode delle proprietà di [riproducibilità](Dichiaratività%20e%20imperatività%20nei%20SO.md#^proprieta-di-riproducibilita-dei-sistemi-operativi-dichiarativi) e di [indistruttibilità](Dichiaratività%20e%20imperatività%20nei%20SO.md#^proprieta-di-indistruttibilita-dei-sistemi-operativi-dichiarativi).
^definizione-nixos

%% mettere logo di NixOS nella definizione %%

%% 
![150](Dichiaratività.svg) ![120](Riproducibilità.svg) ![120](Indistruttibilità.svg)
%%

> [!attenzione]+ Attenzione: usa NixOS se hai familiarità con Linux
> 
> Essendo [NixOS](NixOS.md#^definizione-nixos) una distribuzione Linux%% link %% (anche abbastanza peculiare, data la sua caratteristica di essere [dichiarativa](Dichiaratività%20e%20imperatività%20nei%20SO.md#^definizione-sistema-operativo-dichiarativo)), questa nota è rivolta a chi ha già un minimo di esperienza con altre distribuzioni%% link %% più "popolari", come Ubuntu%% link %% o Debian%% link %%. Nel caso tu fossi completamente novizio nel mondo di Linux%% link %%, ti consiglio di prendere un po' di dimestichezza con altre distribuzioni prima di tentare di usarlo, in modo da poter padroneggiare più facilmente i concetti espressi in questa nota.

# Concetti chiave di NixOS

Ogni volta che in [NixOS](NixOS.md#^definizione-nixos) vogliamo apportare una modifica alla [configurazione del sistema operativo](Sistemi%20operativi.md#^definizione-configurazione-di-un-sistema-operativo), come l'installazione%% link %% di un nuovo pacchetto%% link %%, non si interviene direttamente sul [sistema](Sistemi%20operativi.md#^definizione-sistema-operativo) in esecuzione, ma si aggiorna la [configurazione](Sistemi%20operativi.md#^definizione-configurazione-di-un-sistema-operativo) dichiarativa e si avvia un [_rebuild_](NixOS.md#^definizione-rebuild) del [sistema](Sistemi%20operativi.md#^definizione-sistema-operativo).

> [!definizione] Definizione: rebuild
> 
> In [NixOS](NixOS.md#^definizione-nixos), il **rebuild** è il processo con cui il [sistema operativo](Sistemi%20operativi.md#^definizione-sistema-operativo) viene ricostruito a partire dalla [configurazione](Sistemi%20operativi.md#^definizione-configurazione-di-un-sistema-operativo) dichiarata, lasciando inalterate le versioni precedenti.
^definizione-rebuild

Ogni [rebuild](NixOS.md#^definizione-rebuild) produce una nuova [_generazione_](NixOS.md#^definizione-generazione).

> [!definizione] Definizione: generazione
> 
> In [NixOS](NixOS.md#^definizione-nixos), una **generazione** è una versione del [sistema operativo](Sistemi%20operativi.md#^definizione-sistema-operativo) risultante da una sua specifica [configurazione](Sistemi%20operativi.md#^definizione-configurazione-di-un-sistema-operativo), ottenuta da un [rebuild](NixOS.md#^definizione-rebuild).
> 
> Ogni **generazione** viene salvata in memoria e ciò permette all'utente%% link %%, durante la fase di avvio del sistema, di accedere a qualsiasi [configurazione](Sistemi%20operativi.md#^definizione-configurazione-di-un-sistema-operativo) salvata precedentemente
^definizione-generazione

Potremmo dire che, con un [rebuild](NixOS.md#^definizione-rebuild), possiamo ottenere un'istantanea (la [generazione](NixOS.md#^definizione-generazione)) della nostra [configurazione](Sistemi%20operativi.md#^definizione-configurazione-di-un-sistema-operativo).

> [!osservazione] Osservazione: il salvataggio delle varie generazioni assicura l'indistruttibilità
> 
> Se si effettua un [rebuild](NixOS.md#^definizione-rebuild) che in qualche modo "rompe" il [sistema operativo](Sistemi%20operativi.md#^definizione-sistema-operativo) e ne impedisce perfino l'avvio, basta tornare all'ultima [generazione](NixOS.md#^definizione-generazione) ancora funzionante salvata in memoria e ripartire da lì risolvendo gli errori, assicurando così l'_indistruttibilità_ del [sistema](Sistemi%20operativi.md#^definizione-sistema-operativo).
> 
> Diversamente, con altri [sistemi operativi](Sistemi%20operativi.md#^definizione-sistema-operativo), se ne viene compromesso perfino l'avvio%% link %% bisogna necessariamente trovare l'origine del problema e provare a ripararlo, altrimenti l'alternativa è reinstallare il [sistema operativo](Sistemi%20operativi.md#^definizione-sistema-operativo) da zero e ripartire da capo con la sua [configurazione](Sistemi%20operativi.md#^definizione-configurazione-di-un-sistema-operativo).

> [!consiglio] Consiglio: usa un controllo di versione con NixOS
> 
> Dato che ogni [generazione](NixOS.md#^definizione-generazione) salva con sé anche i file che l'hanno generata, ti consiglio di impostare appena possibile (preferibilmente subito dopo l'installazione di [NixOS](NixOS.md#^definizione-nixos)) un controllo di versione%% Link %% sui file%% Link %% di [configurazione](Sistemi%20operativi.md#^definizione-configurazione-di-un-sistema-operativo), in modo da poter sempre facilmente recuperare le [generazioni](NixOS.md#^definizione-generazione) precedenti.
^consiglio-usa-un-controllo-di-versione-con-nixos


---

> [!fonti] Fonti
> 
> - 🌐 Drake Rossman, [_How to dualboot Windows and NixOS_](https://drakerossman.com/blog/how-to-dualboot-windows-and-nixos), Drake Rossman's Blog.
> - 📹 Vimjoyer, [_NixOS beginner guide_](https://www.youtube.com/watch?v=bjTxiFLSNFA), YouTube.
> - 📹 Ampersand, [_Full NixOS Guide: Everything You Need to Know in One Place!_](https://www.youtube.com/watch?v=nLwbNhSxLd4), YouTube.

%%
https://nixos.org/manual/nixos/stable/#sec-installation-manual
https://nixos.wiki/wiki/NixOS_Installation_Guide/multibootusb
%%
