
> [!premessa] Premessa
> 
> Ciao! Se è la prima volta che capiti su questo sito, ti consiglio di consultare la [pagina principale](index.md) di questo cosiddetto _Giardino Digitale_ per scoprire meglio cos'è e come navigarlo.
> 
> Lo stato di questa nota è al momento: 🔴 <font color="#FF7F7F">_Bozza_</font>.

---

Paradigma dichiarativo si concentra su _quel_ che si vuole ottenere, non sul _come_ ottenerlo (a differenza del paradigma imperativo).

Se vogliamo fare un'analogia con i linguaggi naturali, il paradigma imperativo è associabile al modo imperativo dei verbi (es. "mangia la mela!"), mentre quello dichiarativo al modo indicativo dei verbi (es. "una mela è mangiata").

Allo stesso modo, i linguaggi dichiarativi non specificano le istruzioni da eseguire per ottenere un determinato risultato, ma specificano esattamente il risultato che si vuole ottenere: per esempio, con i package manager imperativi come apt%% link %%, dovremmo fare qualcosa del tipo:

```shell
sudo apt-get install neofetch
sudo apt-get install vim
sudo apt-get install htop
```

Con i package manager dichiarativi come Nix%% link %%, invece, abbiamo:

```nix
environment.systemPackages = with pkgs; [
  neofetch
  vim
  htop
];
```

> [!definizione] Definizione: paradigma dichiarativo
> 
^definizione-paradigma-dichiarativo

---

%% 
Fonti:
- https://www.youtube.com/watch?v=nLwbNhSxLd4
%%

> [!fonti] Fonti
> 
> 
