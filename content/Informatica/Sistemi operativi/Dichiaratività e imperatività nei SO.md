
> [!premessa]+ Premessa
> 
> Ciao! Se è la prima volta che capiti su questo sito, ti consiglio di consultare la [pagina principale](index.md) di questo cosiddetto _Giardino Digitale_ per scoprire meglio cos'è e come navigarlo.
> 
> Lo stato di questa nota è al momento: 🔴 <font color="#FF7F7F">_Bozza_</font>.

---

Tradizionalmente, i [sistemi operativi](Sistemi%20operativi.md#^definizione-sistema-operativo) sono basati su un approccio di tipo [_imperativo_](Dichiaratività%20e%20imperatività%20nei%20SO.md#^definizione-sistema-operativo-imperativo): per apportare modifiche alla propria [configurazione](Sistemi%20operativi.md#^definizione-configurazione-di-un-sistema-operativo) (che comprende le impostazioni di base del [sistema operativo](Sistemi%20operativi.md#^definizione-sistema-operativo) stesso, le applicazioni installate o i pacchetti nel caso delle distribuzioni Linux%% link %%, le impostazioni delle applicazioni, ecc.), si eseguono istruzioni o si effettuano operazioni "manuali" che, una dopo l'altra, ne alterano lo stato.

> [!definizione]+ Definizione: sistema operativo imperativo
> 
> Un [sistema operativo](Sistemi%20operativi.md#^definizione-sistema-operativo) si dice **_imperativo_** quando la sua [configurazione](Sistemi%20operativi.md#^definizione-configurazione-di-un-sistema-operativo) viene determinata da una sequenza di azioni che l'utente%% link %% effettua sul [sistema operativo](Sistemi%20operativi.md#^definizione-sistema-operativo) stesso, come l'installazione di applicazioni%% link %% o la modifica di file%% link %%.
^definizione-sistema-operativo-imperativo

Esistono, però, [sistemi operativi](Sistemi%20operativi.md#^definizione-sistema-operativo) usa un approccio di tipo [_dichiarativo_](Dichiaratività%20e%20imperatività%20nei%20SO.md#^definizione-sistema-operativo-dichiarativo): la [configurazione del sistema operativo](Sistemi%20operativi.md#^definizione-configurazione-di-un-sistema-operativo) è tutta contenuta (_dichiarata_) in uno o più file di codice%% Link %% e, a ogni avvio, il [sistema](Sistemi%20operativi.md#^definizione-sistema-operativo) viene letteralmente _costruito_ esattamente come dichiarato nei file. Ciò permette di tenere traccia facilmente di tutto ciò che contribuisce alla configurazione del sistema, proprio perché è tutto scritto in dei semplici file testuali.

> [!definizione]+ Definizione: sistema operativo dichiarativo
> 
> Un **[sistema operativo](Sistemi%20operativi.md#^definizione-sistema-operativo)** si dice **_dichiarativo_** quando la sua configurazione e il suo comportamento vengono descritti, sotto forma di codice%% link %%, dichiarando lo stato desiderato, invece di specificare passo per passo come ottenerlo.
> 
> I **[sistemi operativi](Sistemi%20operativi.md#^definizione-sistema-operativo) dichiarativi** godono della proprietà di essere [riproducibili](Dichiaratività%20e%20imperatività%20nei%20SO.md#^proprieta-di-riproducibilita-dei-sistemi-operativi-dichiarativi) e [indistruttibili](Dichiaratività%20e%20imperatività%20nei%20SO.md#^proprieta-di-indistruttibilita-dei-sistemi-operativi-dichiarativi).
^definizione-sistema-operativo-dichiarativo

> [!esempio]- Esempi di sistemi operativi dichiarativi
> 
> L'esempio più noto di [sistema operativo dichiarativo](Dichiaratività%20e%20imperatività%20nei%20SO.md#^definizione-sistema-operativo-dichiarativo) è [NixOS](NixOS.md#^definizione-nixos), una distribuzione Linux%% link %% basata sul package manager Nix%% link %%, nonché il [sistema operativo](Sistemi%20operativi.md#^definizione-sistema-operativo) che attualmente uso (ti consiglio di dargli un'occhiata!).
> 
> Un altro importante esempio è Guix System%% Link %%, basato su GNU Guix%% link %%.

%% mettere nell'esempio uno screenshot del codice della mia configurazione di NixOS %%

> [!proprieta]+ Proprietà di _riproducibilità_ dei sistemi operativi dichiarativi
> 
> I [sistemi operativi dichiarativi](Dichiaratività%20e%20imperatività%20nei%20SO.md#^definizione-sistema-operativo-dichiarativo) godono della caratteristica di essere **_riproducibili_**, ossia ogni [configurazione](Sistemi%20operativi.md#^definizione-configurazione-di-un-sistema-operativo) di questi [sistemi](Sistemi%20operativi.md#^definizione-sistema-operativo) si può facilmente riprodurre su altri computer%% link %% senza doverla replicare "a mano" (per esempio non c'è bisogno di installare manualmente le applicazioni%% link %%), semplicemente clonando i file%% link %% contenenti la dichiarazione della [configurazione](Sistemi%20operativi.md#^definizione-configurazione-di-un-sistema-operativo) desiderata.
^proprieta-di-riproducibilita-dei-sistemi-operativi-dichiarativi

> [!proprieta]+ Proprietà di _indistruttibilità_ dei sistemi operativi dichiarativi
> 
> I [sistemi operativi dichiarativi](Dichiaratività%20e%20imperatività%20nei%20SO.md#^definizione-sistema-operativo-dichiarativo) godono della caratteristica di essere **_indistruttibili_**, ossia è praticamente impossibile ritrovarsi nella condizione di avere un [sistema operativo](Sistemi%20operativi.md#^definizione-sistema-operativo) non funzionante perché ogni [configurazione](Sistemi%20operativi.md#^definizione-configurazione-di-un-sistema-operativo) è determinata da una descrizione dello stato del [sistema](Sistemi%20operativi.md#^definizione-sistema-operativo) sotto forma di file di codice%% link %%, quindi basterebbe recuperare file di codice%% link %% precedenti che generano una [configurazione](Sistemi%20operativi.md#^definizione-configurazione-di-un-sistema-operativo) funzionante per risolvere il problema (questo processo può essere facilitato dall'uso del controllo di versione%% Link %% per tenere traccia dell'evoluzione della [configurazione](Sistemi%20operativi.md#^definizione-configurazione-di-un-sistema-operativo)).
^proprieta-di-indistruttibilita-dei-sistemi-operativi-dichiarativi

> [!vantaggi]+ Vantaggi dei sistemi operativi dichiarativi
> 
> Nei [sistemi operativi dichiarativi](Dichiaratività%20e%20imperatività%20nei%20SO.md#^definizione-sistema-operativo-dichiarativo), oltre al vantaggio di essere [indistruttibili](Dichiaratività%20e%20imperatività%20nei%20SO.md#^proprieta-di-indistruttibilita-dei-sistemi-operativi-dichiarativi) e [riproducibili](Dichiaratività%20e%20imperatività%20nei%20SO.md#^proprieta-di-riproducibilita-dei-sistemi-operativi-dichiarativi), quest'ultima proprietà offre ulteriori vantaggi:
> - Proprio perché tutta la [configurazione del sistema](Sistemi%20operativi.md#^definizione-configurazione-di-un-sistema-operativo) è salvata in file%% link %%, basta semplicemente copiare questi file su altri computer%% link %% su cui è installato lo stesso [sistema operativo](Sistemi%20operativi.md#^definizione-sistema-operativo) per riprodurre perfettamente la stessa identica [configurazione](Sistemi%20operativi.md#^definizione-configurazione-di-un-sistema-operativo); ovviamente, [tutto ciò che non è parte della configurazione del sistema](Sistemi%20operativi.md#^osservazione-cosa-fa-parte-della-configurazione-di-un-so-e-cosa-no), quindi tutti quei dati come documenti, salvataggi di giochi, ecc., non saranno automaticamente trasferiti e, per farlo, bisogna usare altri metodi.
> - Nel caso in cui ci sia bisogno di configurare multipli computer%% link %% nello stesso modo, per esempio in un ufficio o in un laboratorio universitario in cui tutti i computer devono essere configurati allo stesso modo con gli stessi programmi installati, grazie ai [sistemi operativi dichiarativi](Dichiaratività%20e%20imperatività%20nei%20SO.md#^definizione-sistema-operativo-dichiarativo) basta lavorare su un solo computer%% link %% per effettuare delle nuove modifiche al sistema (come l'installazione di un nuovo programma) e, in automatico, propagarle a tutte le altre macchine, senza dover mettere mani su ognuna di esse.
> - Ogni utente%% link %% può facilmente condividere la propria [configurazione](Sistemi%20operativi.md#^definizione-configurazione-di-un-sistema-operativo) a chiunque possa essere interessato ad avercela: per esempio io uso [NixOS](NixOS.md#^definizione-nixos) e puoi trovare la mia [configurazione](Sistemi%20operativi.md#^definizione-configurazione-di-un-sistema-operativo) sul [rispettivo repository](https://forgejo.it/Rexus752/my-nixos-config) sul mio account Forgejo.it%% link %%. 

%% vantaggi e svantaggi di dichiaratività e imperatività %%

---

%% fonti: ChatGPT
%%

> [!fonti]+ Fonti
> 
> - 📹 Vimjoyer, [_NixOS beginner guide_](https://www.youtube.com/watch?v=bjTxiFLSNFA), YouTube.
