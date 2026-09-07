
> [!premessa]+ Premessa
> 
> Ciao! Se è la prima volta che capiti su questo sito, ti consiglio di consultare la [pagina principale](index.md) di questo cosiddetto _Giardino Digitale_ per scoprire meglio cos'è e come navigarlo.
> 
> Lo stato di questa nota è al momento: 🔴 <font color="#FF7F7F">_Bozza_</font>.

---

Per determinare se un [termine](Informatica/Lambda-calcolo/Lambda-calcolo%20semplicemente%20tipizzato%20(STLC)/Lambda-calcolo%20semplicemente%20tipizzato%20(STLC).md#^definizione-termine-nel-stlcb) è [ben tipato](Informatica/Lambda-calcolo/Lambda-calcolo%20semplicemente%20tipizzato%20(STLC)/Lambda-calcolo%20semplicemente%20tipizzato%20(STLC).md#^definizione-termine-ben-tipato) o meno si procede cercando di costruire un [albero di derivazione](Informatica/Lambda-calcolo/Lambda-calcolo%20semplicemente%20tipizzato%20(STLC)/Lambda-calcolo%20semplicemente%20tipizzato%20(STLC).md#^definizione-albero-di-derivazione) ma, nel farlo, non ci è sempre chiaro come procedere in maniera sistematica, come abbiamo visto nell'[esempio di prima](Informatica/Lambda-calcolo/Lambda-calcolo%20semplicemente%20tipizzato%20(STLC)/Lambda-calcolo%20semplicemente%20tipizzato%20(STLC).md#^esempio-di-uso-delle-regole-di-tipo-in-un-albero-di-derivazione). Ecco che quindi vogliamo costruire un algoritmo%% link %% che ci permetta di farlo sistematicamente: l'[algoritmo di inferenza](Informatica/Lambda-calcolo/Lambda-calcolo%20semplicemente%20tipizzato%20(STLC)/Algoritmo%20di%20inferenza.md#^algoritmo-di-inferenza).

L'idea generale dell'[algoritmo di inferenza](Informatica/Lambda-calcolo/Lambda-calcolo%20semplicemente%20tipizzato%20(STLC)/Algoritmo%20di%20inferenza.md#^algoritmo-di-inferenza) è la seguente: innanzitutto ci dotiamo di un sistema grafico che ci permetta di operare facilmente sulle [$\lambda^\to_\text{Bool}$-espressioni](Informatica/Lambda-calcolo/Lambda-calcolo%20semplicemente%20tipizzato%20(STLC)/Lambda-calcolo%20semplicemente%20tipizzato%20(STLC).md#^definizione-termine-nel-stlcb) (fase 1 dell'algoritmo), quindi proviamo a "intuire" quali [tipi](Informatica/Lambda-calcolo/Lambda-calcolo%20semplicemente%20tipizzato%20(STLC)/Lambda-calcolo%20semplicemente%20tipizzato%20(STLC).md#^definizione-tipo-nel-stlcb) potremmo assegnare ai sotto-[termini](Informatica/Lambda-calcolo/Lambda-calcolo%20semplicemente%20tipizzato%20(STLC)/Lambda-calcolo%20semplicemente%20tipizzato%20(STLC).md#^definizione-termine-nel-stlcb) della [$\lambda^\to_\text{Bool}$-espressione](Informatica/Lambda-calcolo/Lambda-calcolo%20semplicemente%20tipizzato%20(STLC)/Lambda-calcolo%20semplicemente%20tipizzato%20(STLC).md#^definizione-termine-nel-stlcb), creando dei collegamenti che ci permettano di porli in relazione tra di loro (fase 2 dell'algoritmo), e infine proviamo a trovare una soluzione (fase 3 dell'algoritmo).

# 1 - Fase 1 dell'algoritmo

Come già detto, per il primo passo di questo [algoritmo di inferenza](Informatica/Lambda-calcolo/Lambda-calcolo%20semplicemente%20tipizzato%20(STLC)/Algoritmo%20di%20inferenza.md#^algoritmo-di-inferenza) ci serve un modo "visivamente comodo" per rappresentare le [$\lambda^\to$-espressioni](Informatica/Lambda-calcolo/Lambda-calcolo%20semplicemente%20tipizzato%20(STLC)/Lambda-calcolo%20semplicemente%20tipizzato%20(STLC).md#^definizione-termine-nel-stlcb). Per farlo, scegliamo una struttura ad albero%% link %% esattamente come abbiamo fatto per l'[albero di derivazione](Informatica/Lambda-calcolo/Lambda-calcolo%20semplicemente%20tipizzato%20(STLC)/Lambda-calcolo%20semplicemente%20tipizzato%20(STLC).md#^definizione-albero-di-derivazione), infatti questa nuova struttura sarà facilmente "traducibile" poi in un [albero di derivazione](Informatica/Lambda-calcolo/Lambda-calcolo%20semplicemente%20tipizzato%20(STLC)/Lambda-calcolo%20semplicemente%20tipizzato%20(STLC).md#^definizione-albero-di-derivazione) proprio perché sono entrambi della forma ad albero%% link %%.

Questa struttura verrà chiamata [albero sintattico](Informatica/Lambda-calcolo/Lambda-calcolo%20semplicemente%20tipizzato%20(STLC)/Algoritmo%20di%20inferenza.md#^definizione-albero-sintattico).

%% 
- prendere codice SVG da play.d2lang.com
- andare su https://www.svgviewer.dev/
- cliccare su "Optimize" in alto
- cancellare il tag `<rect ... />` nelle prime righe

- Con D2 da CLI si può impostare il padding a 0
- Togliere il tag `<rect ... />` nelle prime righe così da togliere lo sfondo e il gioco è fatto
%%


> [!definizione]+ Definizione: albero sintattico
> 
> Data una [$\lambda^\to_\text{Bool}$-espressione](Informatica/Lambda-calcolo/Lambda-calcolo%20semplicemente%20tipizzato%20(STLC)/Lambda-calcolo%20semplicemente%20tipizzato%20(STLC).md#^definizione-termine-nel-stlcb) $T$, l'**albero sintattico** $\text{Tree}[T]$:
> 
> 1. Se $T$ è un [termine della forma di una variabile](Informatica/Lambda-calcolo/Lambda-calcolo%20semplicemente%20tipizzato%20(STLC)/Lambda-calcolo%20semplicemente%20tipizzato%20(STLC).md#^definizione-termine-nel-stlcb) $x$, allora $\text{Tree}[T] = \text{Tree}[x]$ sarà:
> ![500](Informatica/Lambda-calcolo/Lambda-calcolo%20semplicemente%20tipizzato%20(STLC)/_attachments/definizione-albero-sintattico-variabile.svg)
> 2. Se $T$ è un [termine della forma di una costante](Informatica/Lambda-calcolo/Lambda-calcolo%20semplicemente%20tipizzato%20(STLC)/Lambda-calcolo%20semplicemente%20tipizzato%20(STLC).md#^definizione-termine-nel-stlcb) $c$, allora $\text{Tree}[T] = \text{Tree}[c]$ sarà:
> ![500](Informatica/Lambda-calcolo/Lambda-calcolo%20semplicemente%20tipizzato%20(STLC)/_attachments/definizione-albero-sintattico-costante-booleana.svg)
> 3. Se $T$ è un [termine della forma di un'astrazione](Informatica/Lambda-calcolo/Lambda-calcolo%20semplicemente%20tipizzato%20(STLC)/Lambda-calcolo%20semplicemente%20tipizzato%20(STLC).md#^definizione-termine-nel-stlcb) $\lambda x.M$, allora $\text{Tree}[T] = \text{Tree}[\lambda x.M]$ sarà:
> ![500](Informatica/Lambda-calcolo/Lambda-calcolo%20semplicemente%20tipizzato%20(STLC)/_attachments/definizione-albero-sintattico-astrazione.svg)
> 4.  Se $T$ è un [termine della forma di un'applicazione](Informatica/Lambda-calcolo/Lambda-calcolo%20semplicemente%20tipizzato%20(STLC)/Lambda-calcolo%20semplicemente%20tipizzato%20(STLC).md#^definizione-termine-nel-stlcb) $M\ N$, allora $\text{Tree}[T] = \text{Tree}[M\ N]$ sarà:
> ![500](Informatica/Lambda-calcolo/Lambda-calcolo%20semplicemente%20tipizzato%20(STLC)/_attachments/definizione-albero-sintattico-applicazione.svg)
> 5.  Se $T$ è un [termine della forma di una struttura di controllo](Informatica/Lambda-calcolo/Lambda-calcolo%20semplicemente%20tipizzato%20(STLC)/Lambda-calcolo%20semplicemente%20tipizzato%20(STLC).md#^definizione-termine-nel-stlcb) $\text{if}\ c\ M\ N$, allora $\text{Tree}[T] = \text{Tree}[\text{if}\ c\ M\ N]$ sarà:
> ![500](Informatica/Lambda-calcolo/Lambda-calcolo%20semplicemente%20tipizzato%20(STLC)/_attachments/definizione-albero-sintattico-struttura-di-controllo.svg)
^definizione-albero-sintattico

> [!esempio]- Esempio di albero sintattico
> 
> Ecco un esempio di [albero sintattico](Informatica/Lambda-calcolo/Lambda-calcolo%20semplicemente%20tipizzato%20(STLC)/Algoritmo%20di%20inferenza.md#^definizione-albero-sintattico) della [$\lambda^\to_\text{Bool}$-espressione](Informatica/Lambda-calcolo/Lambda-calcolo%20semplicemente%20tipizzato%20(STLC)/Lambda-calcolo%20semplicemente%20tipizzato%20(STLC).md#^definizione-termine-nel-stlcb) $(\lambda x.x)\ \text{True}$:
> 
> ![500](Informatica/Lambda-calcolo/Lambda-calcolo%20semplicemente%20tipizzato%20(STLC)/_attachments/esempio-di-albero-sintattico.svg)

> [!esercizio]+ Esercizio 1 di costruzione di un albero sintattico
> 
> Costruisci l'[albero sintattico](Informatica/Lambda-calcolo/Lambda-calcolo%20semplicemente%20tipizzato%20(STLC)/Algoritmo%20di%20inferenza.md#^definizione-albero-sintattico) della [$\lambda^\to_\text{Bool}$-espressione](Informatica/Lambda-calcolo/Lambda-calcolo%20semplicemente%20tipizzato%20(STLC)/Lambda-calcolo%20semplicemente%20tipizzato%20(STLC).md#^definizione-termine-nel-stlcb) $\lambda x.\lambda y.\lambda z.\text{False}\ z\ (x\ y)$.

%% 
mettere soluzione
%%

> [!esercizio]+ Esercizio 2 di costruzione di un albero sintattico
> 
> Costruisci l'[albero sintattico](Informatica/Lambda-calcolo/Lambda-calcolo%20semplicemente%20tipizzato%20(STLC)/Algoritmo%20di%20inferenza.md#^definizione-albero-sintattico) della [$\lambda^\to_\text{Bool}$-espressione](Informatica/Lambda-calcolo/Lambda-calcolo%20semplicemente%20tipizzato%20(STLC)/Lambda-calcolo%20semplicemente%20tipizzato%20(STLC).md#^definizione-termine-nel-stlcb) $\text{if}\ \text{True}\ (\lambda x.x)\ (\lambda x.\lambda y.y)$.

%% 
mettere soluzione
%%

%% 
esercizi:
$$
% Lambda Calculus environment 
\begin{array}{}
\lambda f.\lambda x.f\ (f\ x) \\
\lambda x.x\ x \\
\text{if}\ \text{True}\ (\lambda x.\lambda y.x)\ (\lambda x.\lambda y.y) \\
\text{if}\ \text{True}\ (\lambda x.x)\ (\lambda x.\lambda y.y) \\
((\lambda x.x)\ \text{True})\ \text{False} \\
(\lambda x.\lambda y.\lambda z.z\ x\ y)\ (\lambda x.x)\ \text{True}
\end{array}
$$
%%

# 2 - Fase 2 dell'algoritmo

Dopo aver costruito l'[albero sintattico](Informatica/Lambda-calcolo/Lambda-calcolo%20semplicemente%20tipizzato%20(STLC)/Algoritmo%20di%20inferenza.md#^definizione-albero-sintattico), si fa una visita dell'albero usando la strategia _bottom-up_ (quindi partendo dalle foglie%% link %% e arrivando alla radice%% link %%): ogni nodo%% link %% viene "annotato" con un'[espressione di tipo](Informatica/Lambda-calcolo/Lambda-calcolo%20semplicemente%20tipizzato%20(STLC)/Algoritmo%20di%20inferenza.md#^definizione-espressione-di-tipo), ossia delle "etichette" che ci aiutano a intuire quale [tipo](Informatica/Lambda-calcolo/Lambda-calcolo%20semplicemente%20tipizzato%20(STLC)/Lambda-calcolo%20semplicemente%20tipizzato%20(STLC).md#^definizione-tipo-nel-stlcb) potrebbe assumere quel nodo%% link %%.

> [!definizione]+ Definizione: espressione di tipo
> 
> Sia $\text{TVar} = \{ \alpha, \beta, \gamma, \ldots \}$ l'[insieme](Matematica/Teoria%20degli%20insiemi/Teoria%20degli%20insiemi.md#^definizione-insieme) infinito%% link %% di variabili%% link %% di [tipo](Informatica/Lambda-calcolo/Lambda-calcolo%20semplicemente%20tipizzato%20(STLC)/Lambda-calcolo%20semplicemente%20tipizzato%20(STLC).md#^definizione-tipo-nel-stlcb).
> 
> Un'**espressione di tipo** $\tau$ è un'etichetta assegnata a un nodo%% link %% dell'[albero sintattico](Informatica/Lambda-calcolo/Lambda-calcolo%20semplicemente%20tipizzato%20(STLC)/Algoritmo%20di%20inferenza.md#^definizione-albero-sintattico) che corrisponde a una stringa ben formata a partire dalla seguente grammatica espressa in BNF:
> 
> $$
> \tau ::= \alpha \mid \text{Bool} \mid {\color{#FF7F7F} \tau } \to {\color{#7F7FFF} \tau }
> $$
> 
> dove:
> - $\alpha$ è una **variabile di tipo** per un [tipo](Informatica/Lambda-calcolo/Lambda-calcolo%20semplicemente%20tipizzato%20(STLC)/Lambda-calcolo%20semplicemente%20tipizzato%20(STLC).md#^definizione-tipo-nel-stlcb) ancora sconosciuto.
> - $\text{Bool}$ è il **[tipo booleano](Informatica/Lambda-calcolo/Lambda-calcolo%20semplicemente%20tipizzato%20(STLC)/Lambda-calcolo%20semplicemente%20tipizzato%20(STLC).md#^definizione-tipo-nel-stlcb)**.
> - ${\color{#FF7F7F} \tau } \to {\color{#7F7FFF} \tau }$ è il [**tipo funzione**](Informatica/Lambda-calcolo/Lambda-calcolo%20semplicemente%20tipizzato%20(STLC)/Lambda-calcolo%20semplicemente%20tipizzato%20(STLC).md#^definizione-tipo-nel-stlcb).
^definizione-espressione-di-tipo

%% 
La variabile di tipo può essere intesa come una sorta di "segnaposto" temporaneo da usare finché non si sa con certezza quale tipo assumerà quel nodo.
%%

Per determinare delle "relazioni" tra le varie [espressione di tipo](Informatica/Lambda-calcolo/Lambda-calcolo%20semplicemente%20tipizzato%20(STLC)/Algoritmo%20di%20inferenza.md#^definizione-espressione-di-tipo) usiamo dei [vincoli](Informatica/Lambda-calcolo/Lambda-calcolo%20semplicemente%20tipizzato%20(STLC)/Algoritmo%20di%20inferenza.md#^definizione-vincolo) che devono essere rispettati affinché la [$\lambda^\to_\text{Bool}$-espressione](Informatica/Lambda-calcolo/Lambda-calcolo%20semplicemente%20tipizzato%20(STLC)/Lambda-calcolo%20semplicemente%20tipizzato%20(STLC).md#^definizione-termine-nel-stlcb) sia [ben tipata](Informatica/Lambda-calcolo/Lambda-calcolo%20semplicemente%20tipizzato%20(STLC)/Lambda-calcolo%20semplicemente%20tipizzato%20(STLC).md#^definizione-termine-ben-tipato).

> [!definizione]+ Definizione: vincolo
> 
> Un **vincolo** è una relazione di uguaglianza%% link %% tra due [espressione di tipo](Informatica/Lambda-calcolo/Lambda-calcolo%20semplicemente%20tipizzato%20(STLC)/Algoritmo%20di%20inferenza.md#^definizione-espressione-di-tipo) $\tau$ e $\sigma$:
> 
> $$
> \tau = \sigma
> $$
^definizione-vincolo

Proviamo quindi a capire come annotare le [espressione di tipo](Informatica/Lambda-calcolo/Lambda-calcolo%20semplicemente%20tipizzato%20(STLC)/Algoritmo%20di%20inferenza.md#^definizione-espressione-di-tipo) sull'[albero sintattico](Informatica/Lambda-calcolo/Lambda-calcolo%20semplicemente%20tipizzato%20(STLC)/Algoritmo%20di%20inferenza.md#^definizione-albero-sintattico) distinguendo tra i vari casi.

Nel caso di un [termine della forma di una variabile](Informatica/Lambda-calcolo/Lambda-calcolo%20semplicemente%20tipizzato%20(STLC)/Lambda-calcolo%20semplicemente%20tipizzato%20(STLC).md#^definizione-termine-nel-stlcb) $x$, nel nodo%% link %% $x$ ci annotiamo un [espressione di tipo](Informatica/Lambda-calcolo/Lambda-calcolo%20semplicemente%20tipizzato%20(STLC)/Algoritmo%20di%20inferenza.md#^definizione-espressione-di-tipo) $\alpha$, avendo cura di usare lo stesso segnaposto $\alpha$ per tutte le occorrenze di $x$ e **solo** per quelle:

![500](Informatica/Lambda-calcolo/Lambda-calcolo%20semplicemente%20tipizzato%20(STLC)/_attachments/espressione-di-tipo-variabile.svg)

Nel caso di un [termine della forma di una costante](Informatica/Lambda-calcolo/Lambda-calcolo%20semplicemente%20tipizzato%20(STLC)/Lambda-calcolo%20semplicemente%20tipizzato%20(STLC).md#^definizione-termine-nel-stlcb) $c$, nel nodo%% link %% $c$ ci annotiamo il [espressione di tipo](Informatica/Lambda-calcolo/Lambda-calcolo%20semplicemente%20tipizzato%20(STLC)/Algoritmo%20di%20inferenza.md#^definizione-espressione-di-tipo) $\text{Bool}$:

![500](Informatica/Lambda-calcolo/Lambda-calcolo%20semplicemente%20tipizzato%20(STLC)/_attachments/espressione-di-tipo-costante-booleana.svg)

Nel caso di un [termine della forma di un'astrazione](Informatica/Lambda-calcolo/Lambda-calcolo%20semplicemente%20tipizzato%20(STLC)/Lambda-calcolo%20semplicemente%20tipizzato%20(STLC).md#^definizione-termine-nel-stlcb) $\lambda x.M$, partendo dal basso (perché stiamo usando la strategia _bottom-up_):
- Dal sotto-albero%% link %% $\text{Tree}[M]$ avremo ottenuto un'[espressione di tipo](Informatica/Lambda-calcolo/Lambda-calcolo%20semplicemente%20tipizzato%20(STLC)/Algoritmo%20di%20inferenza.md#^definizione-espressione-di-tipo) $\tau$.
- Nel nodo%% link %% $\lambda x$ ci annotiamo un [espressione di tipo](Informatica/Lambda-calcolo/Lambda-calcolo%20semplicemente%20tipizzato%20(STLC)/Algoritmo%20di%20inferenza.md#^definizione-espressione-di-tipo) $\alpha \to \tau$, dove $\alpha$ è un [espressione di tipo](Informatica/Lambda-calcolo/Lambda-calcolo%20semplicemente%20tipizzato%20(STLC)/Algoritmo%20di%20inferenza.md#^definizione-espressione-di-tipo) (e, per ogni occorrenza di $x$ in $M$, dovremo usare sempre lo stesso [espressione di tipo](Informatica/Lambda-calcolo/Lambda-calcolo%20semplicemente%20tipizzato%20(STLC)/Algoritmo%20di%20inferenza.md#^definizione-espressione-di-tipo) $\alpha$) e $\tau$ è l'[espressione di tipo](Informatica/Lambda-calcolo/Lambda-calcolo%20semplicemente%20tipizzato%20(STLC)/Algoritmo%20di%20inferenza.md#^definizione-espressione-di-tipo) del sotto-albero%% link %% $\text{Tree}[M]$.

Il risultato è il seguente:

![500](Informatica/Lambda-calcolo/Lambda-calcolo%20semplicemente%20tipizzato%20(STLC)/_attachments/espressione-di-tipo-astrazione.svg)

Nel caso di un [termine della forma di un'applicazione](Informatica/Lambda-calcolo/Lambda-calcolo%20semplicemente%20tipizzato%20(STLC)/Lambda-calcolo%20semplicemente%20tipizzato%20(STLC).md#^definizione-termine-nel-stlcb) $M\ N$, partendo sempre dal basso (perché stiamo usando la strategia _bottom-up_):
- Dal sotto-albero%% link %% $\text{Tree}[M]$ avremo ottenuto un'[espressione di tipo](Informatica/Lambda-calcolo/Lambda-calcolo%20semplicemente%20tipizzato%20(STLC)/Algoritmo%20di%20inferenza.md#^definizione-espressione-di-tipo) $\tau$ (dove $\tau$ è diverso dal $\tau$ usato nell'[astrazione](Informatica/Lambda-calcolo/Lambda-calcolo.md#^definizione-astrazione) $\lambda x.M$, perché questi due sotto-[termini](Informatica/Lambda-calcolo/Lambda-calcolo%20semplicemente%20tipizzato%20(STLC)/Lambda-calcolo%20semplicemente%20tipizzato%20(STLC).md#^definizione-termine-nel-stlcb) $M$ non sono la stessa cosa).
- Dal sotto-albero%% link %% $\text{Tree}[N]$ avremo ottenuto un'[espressione di tipo](Informatica/Lambda-calcolo/Lambda-calcolo%20semplicemente%20tipizzato%20(STLC)/Algoritmo%20di%20inferenza.md#^definizione-espressione-di-tipo) $\sigma$.
- Nel nodo%% link %% $@$ ci annotiamo un nuovo [espressione di tipo](Informatica/Lambda-calcolo/Lambda-calcolo%20semplicemente%20tipizzato%20(STLC)/Algoritmo%20di%20inferenza.md#^definizione-espressione-di-tipo) $\alpha$.
- Generiamo un nuovo [vincolo](Informatica/Lambda-calcolo/Lambda-calcolo%20semplicemente%20tipizzato%20(STLC)/Algoritmo%20di%20inferenza.md#^definizione-vincolo) $\tau = \sigma \to \alpha$.

Il risultato è il seguente:

![espressione-di-tipo-applicazione](Informatica/Lambda-calcolo/Lambda-calcolo%20semplicemente%20tipizzato%20(STLC)/_attachments/espressione-di-tipo-applicazione.svg)

In particolare, se $\text{Tree}[M]$ è di un certo [tipo funzione](Informatica/Lambda-calcolo/Lambda-calcolo%20semplicemente%20tipizzato%20(STLC)/Algoritmo%20di%20inferenza.md#^definizione-espressione-di-tipo) $\tau_1 \to \tau_2$, allora il nodo%% link %% $@$ ha [tipo](Informatica/Lambda-calcolo/Lambda-calcolo%20semplicemente%20tipizzato%20(STLC)/Algoritmo%20di%20inferenza.md#^definizione-espressione-di-tipo) $\tau_2$ e il [vincolo](Informatica/Lambda-calcolo/Lambda-calcolo%20semplicemente%20tipizzato%20(STLC)/Algoritmo%20di%20inferenza.md#^definizione-vincolo) generato è $\tau_1 = \sigma$:

![espressione-di-tipo-applicazione2](Informatica/Lambda-calcolo/Lambda-calcolo%20semplicemente%20tipizzato%20(STLC)/_attachments/espressione-di-tipo-applicazione2.svg)

Nel caso di un [termine della forma di una struttura di controllo](Informatica/Lambda-calcolo/Lambda-calcolo%20semplicemente%20tipizzato%20(STLC)/Lambda-calcolo%20semplicemente%20tipizzato%20(STLC).md#^definizione-termine-nel-stlcb) $\text{if}\ c\ M\ N$:
- Dal sotto-albero%% link %% $\text{Tree}[c]$ avremo ottenuto un'[espressione di tipo](Informatica/Lambda-calcolo/Lambda-calcolo%20semplicemente%20tipizzato%20(STLC)/Algoritmo%20di%20inferenza.md#^definizione-espressione-di-tipo) $\tau_1$.
- Dal sotto-albero%% link %% $\text{Tree}[M]$ avremo ottenuto un'[espressione di tipo](Informatica/Lambda-calcolo/Lambda-calcolo%20semplicemente%20tipizzato%20(STLC)/Algoritmo%20di%20inferenza.md#^definizione-espressione-di-tipo) $\tau_2$.
- Dal sotto-albero%% link %% $\text{Tree}[N]$ avremo ottenuto un'[espressione di tipo](Informatica/Lambda-calcolo/Lambda-calcolo%20semplicemente%20tipizzato%20(STLC)/Algoritmo%20di%20inferenza.md#^definizione-espressione-di-tipo) $\tau_3$.
- Generiamo il [vincolo](Informatica/Lambda-calcolo/Lambda-calcolo%20semplicemente%20tipizzato%20(STLC)/Algoritmo%20di%20inferenza.md#^definizione-vincolo) che richiede che il [tipo](Informatica/Lambda-calcolo/Lambda-calcolo%20semplicemente%20tipizzato%20(STLC)/Algoritmo%20di%20inferenza.md#^definizione-espressione-di-tipo) di $c$ sia [booleano](Informatica/Lambda-calcolo/Lambda-calcolo%20semplicemente%20tipizzato%20(STLC)/Lambda-calcolo%20semplicemente%20tipizzato%20(STLC).md#^definizione-tipo-nel-stlcb): $\tau_1 = \text{Bool}$.
- Generiamo il [vincolo](Informatica/Lambda-calcolo/Lambda-calcolo%20semplicemente%20tipizzato%20(STLC)/Algoritmo%20di%20inferenza.md#^definizione-vincolo) che richiede che il [tipo](Informatica/Lambda-calcolo/Lambda-calcolo%20semplicemente%20tipizzato%20(STLC)/Algoritmo%20di%20inferenza.md#^definizione-espressione-di-tipo) di $\tau_2$ e di $\tau_3$ coincida: $\tau_2 = \tau_3$.
- Nel nodo%% link %% $\text{if}$ ci annotiamo il [tipo](Informatica/Lambda-calcolo/Lambda-calcolo%20semplicemente%20tipizzato%20(STLC)/Algoritmo%20di%20inferenza.md#^definizione-espressione-di-tipo) $\tau_2$ ($= \tau_3$), che sarà proprio il [tipo](Informatica/Lambda-calcolo/Lambda-calcolo%20semplicemente%20tipizzato%20(STLC)/Lambda-calcolo%20semplicemente%20tipizzato%20(STLC).md#^definizione-tipo-nel-stlcb) che restituisce la struttura di controllo%% link %%.

Il risultato è il seguente:

![espressione-di-tipo-struttura-di-controllo](Informatica/Lambda-calcolo/Lambda-calcolo%20semplicemente%20tipizzato%20(STLC)/_attachments/espressione-di-tipo-struttura-di-controllo.svg)

%% 

basandoti sugli alberi sintattici costruiti in precedenza, fai questi esercizi

> [!esercizio]+ Esercizio 1 di costruzione di un albero sintattico
> 
> Costruisci l'[albero sintattico](Informatica/Lambda-calcolo/Lambda-calcolo%20semplicemente%20tipizzato%20(STLC)/Algoritmo%20di%20inferenza.md#^definizione-albero-sintattico) della [$\lambda^\to_\text{Bool}$-espressione](Informatica/Lambda-calcolo/Lambda-calcolo%20semplicemente%20tipizzato%20(STLC)/Lambda-calcolo%20semplicemente%20tipizzato%20(STLC).md#^definizione-termine-nel-stlcb) $\lambda x.\lambda y.\lambda z.\text{False}\ z\ (x\ y)$.

mettere soluzione

> [!esercizio]+ Esercizio 2 di costruzione di un albero sintattico
> 
> Costruisci l'[albero sintattico](Informatica/Lambda-calcolo/Lambda-calcolo%20semplicemente%20tipizzato%20(STLC)/Algoritmo%20di%20inferenza.md#^definizione-albero-sintattico) della [$\lambda^\to_\text{Bool}$-espressione](Informatica/Lambda-calcolo/Lambda-calcolo%20semplicemente%20tipizzato%20(STLC)/Lambda-calcolo%20semplicemente%20tipizzato%20(STLC).md#^definizione-termine-nel-stlcb) $\text{if}\ \text{True}\ (\lambda x.x)\ (\lambda x.\lambda y.y)$.

mettere soluzione

esercizi:
$$
% Lambda Calculus environment 
\begin{array}{}
\lambda f.\lambda x.f\ (f\ x) \\
\lambda x.x\ x \\
\text{if}\ \text{True}\ (\lambda x.\lambda y.x)\ (\lambda x.\lambda y.y) \\
\text{if}\ \text{True}\ (\lambda x.x)\ (\lambda x.\lambda y.y) \\
((\lambda x.x)\ \text{True})\ \text{False} \\
(\lambda x.\lambda y.\lambda z.z\ x\ y)\ (\lambda x.x)\ \text{True}
\end{array}
$$
%%

# 3 - Fase 3 dell'algoritmo

Nella terza fase dell'[algoritmo di inferenza](Informatica/Lambda-calcolo/Lambda-calcolo%20semplicemente%20tipizzato%20(STLC)/Algoritmo%20di%20inferenza.md#^algoritmo-di-inferenza), una volta che l'[albero sintattico](Informatica/Lambda-calcolo/Lambda-calcolo%20semplicemente%20tipizzato%20(STLC)/Algoritmo%20di%20inferenza.md#^definizione-albero-sintattico) è stato annotato, si cerca di capire se questo insieme di [vincoli](Informatica/Lambda-calcolo/Lambda-calcolo%20semplicemente%20tipizzato%20(STLC)/Algoritmo%20di%20inferenza.md#^definizione-vincolo) ammette una soluzione e si cerca di trovare quella generale da cui derivare tutte le altre.

All'inizio della terza fase ci ritroviamo con un sistema di $n$ [vincoli](Informatica/Lambda-calcolo/Lambda-calcolo%20semplicemente%20tipizzato%20(STLC)/Algoritmo%20di%20inferenza.md#^definizione-vincolo):

$$
\text{Sys} = \{ \tau_i = \sigma_i \}_{1 \le i \le n}
$$

Per risolvere questo sistema%% link %% usiamo un [_algoritmo di risoluzione_](Informatica/Lambda-calcolo/Lambda-calcolo%20semplicemente%20tipizzato%20(STLC)/Algoritmo%20di%20inferenza.md#^algoritmo-di-risoluzione).

> [!algoritmo]+ Algoritmo di risoluzione
> 
> Dato un sistema di $n$ [vincoli](Informatica/Lambda-calcolo/Lambda-calcolo%20semplicemente%20tipizzato%20(STLC)/Algoritmo%20di%20inferenza.md#^definizione-vincolo) $\text{Sys} = \{ \tau_i = \sigma_i \}_{1 \le i \le n}$, l'**algoritmo di risoluzione** permette di risolvere $\text{Sys}$, ottenendo un successo o un fallimento.
> 
> I passi da seguire sono i seguenti:
> 
> 1. Per ogni [vincolo](Informatica/Lambda-calcolo/Lambda-calcolo%20semplicemente%20tipizzato%20(STLC)/Algoritmo%20di%20inferenza.md#^definizione-vincolo) $\tau_i = \sigma_i \in \text{Sys}$, verificare se nella seguente tabella il [vincolo](Informatica/Lambda-calcolo/Lambda-calcolo%20semplicemente%20tipizzato%20(STLC)/Algoritmo%20di%20inferenza.md#^definizione-vincolo) rispetta una delle seguenti forme e condizioni e, eventualmente, eseguire la trasformazione indicata:
> 
> | **Forma del [vincolo](Informatica/Lambda-calcolo/Lambda-calcolo%20semplicemente%20tipizzato%20(STLC)/Algoritmo%20di%20inferenza.md#^definizione-vincolo)** | **Condizione**                                                                                                                                                                                                                                         | **Cosa fare**                                                                                                                                                       |
> | -------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
> | $\tau = \tau$                                                                    | $\tau$ è un'[espressione di tipo](Informatica/Lambda-calcolo/Lambda-calcolo%20semplicemente%20tipizzato%20(STLC)/Algoritmo%20di%20inferenza.md#^definizione-espressione-di-tipo) qualsiasi                                                                                                                                       | Eliminare il [vincolo](Informatica/Lambda-calcolo/Lambda-calcolo%20semplicemente%20tipizzato%20(STLC)/Algoritmo%20di%20inferenza.md#^definizione-vincolo)                                                                                     |
> | $\tau = \alpha$                                                                  | $\tau$ è un'[espressione di tipo](Informatica/Lambda-calcolo/Lambda-calcolo%20semplicemente%20tipizzato%20(STLC)/Algoritmo%20di%20inferenza.md#^definizione-espressione-di-tipo) qualsiasi e $\alpha$ è un [segnaposto](Informatica/Lambda-calcolo/Lambda-calcolo%20semplicemente%20tipizzato%20(STLC)/Algoritmo%20di%20inferenza.md#^definizione-espressione-di-tipo)                                     | Rimpiazzare il [vincolo](Informatica/Lambda-calcolo/Lambda-calcolo%20semplicemente%20tipizzato%20(STLC)/Algoritmo%20di%20inferenza.md#^definizione-vincolo) con $\alpha = \tau$                                                               |
> | $\tau \to \tau' = \sigma \to \sigma'$                                            | $\tau$ e $\sigma$ sono due [espressione di tipo](Informatica/Lambda-calcolo/Lambda-calcolo%20semplicemente%20tipizzato%20(STLC)/Algoritmo%20di%20inferenza.md#^definizione-espressione-di-tipo) qualsiasi                                                                                                                        | Rimpiazzare il [vincolo](Informatica/Lambda-calcolo/Lambda-calcolo%20semplicemente%20tipizzato%20(STLC)/Algoritmo%20di%20inferenza.md#^definizione-vincolo) con $\tau = \sigma$ e $\tau' = \sigma'$                                           |
> | $\tau \to \sigma = \text{Bool}$                                                  | $\tau$ e $\sigma$ sono due [espressioni di tipo](Informatica/Lambda-calcolo/Lambda-calcolo%20semplicemente%20tipizzato%20(STLC)/Algoritmo%20di%20inferenza.md#^definizione-espressione-di-tipo) qualsiasi, $\text{Bool}$ è il [tipo booleano](Informatica/Lambda-calcolo/Lambda-calcolo%20semplicemente%20tipizzato%20(STLC)/Algoritmo%20di%20inferenza.md#^definizione-espressione-di-tipo)               | **L'algoritmo fallisce per _errore di tipo_**                                                                                                                       |
> | $\text{Bool} = \tau \to \sigma$                                                  | $\tau$ e $\sigma$ sono due [espressione di tipo](Informatica/Lambda-calcolo/Lambda-calcolo%20semplicemente%20tipizzato%20(STLC)/Algoritmo%20di%20inferenza.md#^definizione-espressione-di-tipo) qualsiasi, $\text{Bool}$ è il [tipo booleano](Informatica/Lambda-calcolo/Lambda-calcolo%20semplicemente%20tipizzato%20(STLC)/Algoritmo%20di%20inferenza.md#^definizione-espressione-di-tipo)               | **L'algoritmo fallisce per _errore di tipo_**                                                                                                                       |
> | $\alpha = \tau$                                                                  | $\tau$ è un'[espressione di tipo](Informatica/Lambda-calcolo/Lambda-calcolo%20semplicemente%20tipizzato%20(STLC)/Algoritmo%20di%20inferenza.md#^definizione-espressione-di-tipo) qualsiasi, $\alpha$ è un [segnaposto](Informatica/Lambda-calcolo/Lambda-calcolo%20semplicemente%20tipizzato%20(STLC)/Algoritmo%20di%20inferenza.md#^definizione-espressione-di-tipo) e $\alpha$ compare in $\tau$         | **L'algoritmo fallisce per _errore di occorrenza_**                                                                                                                 |
> | $\alpha = \tau$                                                                  | $\tau$ è un'[espressione di tipo](Informatica/Lambda-calcolo/Lambda-calcolo%20semplicemente%20tipizzato%20(STLC)/Algoritmo%20di%20inferenza.md#^definizione-espressione-di-tipo) qualsiasi, $\alpha$ è un [segnaposto](Informatica/Lambda-calcolo/Lambda-calcolo%20semplicemente%20tipizzato%20(STLC)/Algoritmo%20di%20inferenza.md#^definizione-espressione-di-tipo) e $\alpha$ **non** compare in $\tau$ | Rimpiazzare le occorrenze di $\alpha$ con $\tau$ in tutti gli altri [vincoli](Informatica/Lambda-calcolo/Lambda-calcolo%20semplicemente%20tipizzato%20(STLC)/Algoritmo%20di%20inferenza.md#^definizione-vincolo) e lasciando questo invariato |
> 
> 2. Ripetere il _passo 1_ finché non si ottiene un fallimento dell'algoritmo o finché non è più possibile applicare le trasformazioni indicate.
> 3. Se non è avvenuto un fallimento dell'algoritmo, allora ha avuto successo e si è risolto il sistema%% link %% $\text{Sys}$.
^algoritmo-di-risoluzione

> [!osservazione]+ Osservazione: invarianza dell'ordine delle trasformazioni
> 
> L'ordine in cui si applicano le trasformazioni del [passo 1 dell'algoritmo di risoluzione](Informatica/Lambda-calcolo/Lambda-calcolo%20semplicemente%20tipizzato%20(STLC)/Algoritmo%20di%20inferenza.md#^algoritmo-di-risoluzione) non influisce sul risultato.

Con il successo dell'[algoritmo di risoluzione](Informatica/Lambda-calcolo/Lambda-calcolo%20semplicemente%20tipizzato%20(STLC)/Algoritmo%20di%20inferenza.md#^algoritmo-di-risoluzione), avremo ottenuto un nuovo sistema%% link %% di $n'$ [vincoli](Informatica/Lambda-calcolo/Lambda-calcolo%20semplicemente%20tipizzato%20(STLC)/Algoritmo%20di%20inferenza.md#^definizione-vincolo)

$$
\text{Sys}' = \{ \alpha_i = \rho_i \}_{1 \le i \le n'}
$$

dove ogni $\alpha_i$ è un [segnaposto](Informatica/Lambda-calcolo/Lambda-calcolo%20semplicemente%20tipizzato%20(STLC)/Algoritmo%20di%20inferenza.md#^definizione-espressione-di-tipo) (che compare una sola volta nel sistema%% link %%) corrispondente esattamente a un [tipo](Informatica/Lambda-calcolo/Lambda-calcolo%20semplicemente%20tipizzato%20(STLC)/Lambda-calcolo%20semplicemente%20tipizzato%20(STLC).md#^definizione-tipo-nel-stlcb) che sarà uguale a un'[espressione di tipo](Informatica/Lambda-calcolo/Lambda-calcolo%20semplicemente%20tipizzato%20(STLC)/Algoritmo%20di%20inferenza.md#^definizione-espressione-di-tipo) $\rho_i$.

A questo punto non ci rimane altro che fare una [_sostituzione_](Informatica/Lambda-calcolo/Lambda-calcolo%20semplicemente%20tipizzato%20(STLC)/Algoritmo%20di%20inferenza.md#^definizione-sostituzione) di ogni $\alpha_i$ con il rispettivo $\rho_i$.

> [!definizione]+ Definizione: sostituzione
> 
> Nell'[algoritmo di inferenza](Informatica/Lambda-calcolo/Lambda-calcolo%20semplicemente%20tipizzato%20(STLC)/Algoritmo%20di%20inferenza.md#^algoritmo-di-inferenza), una **sostituzione** $\theta$ è una [funzione](Matematica/Teoria%20degli%20insiemi/Funzioni/Funzioni.md#^definizione-funzione) da variabili di [tipo](Informatica/Lambda-calcolo/Lambda-calcolo%20semplicemente%20tipizzato%20(STLC)/Lambda-calcolo%20semplicemente%20tipizzato%20(STLC).md#^definizione-tipo-nel-stlcb) a [espressioni di tipo](Informatica/Lambda-calcolo/Lambda-calcolo%20semplicemente%20tipizzato%20(STLC)/Algoritmo%20di%20inferenza.md#^definizione-espressione-di-tipo) in cui, dato un [tipo](Informatica/Lambda-calcolo/Lambda-calcolo%20semplicemente%20tipizzato%20(STLC)/Lambda-calcolo%20semplicemente%20tipizzato%20(STLC).md#^definizione-tipo-nel-stlcb) $\tau$, sostituiamo in $\tau$ ogni occorrenza di ogni sotto-[tipo](Informatica/Lambda-calcolo/Lambda-calcolo%20semplicemente%20tipizzato%20(STLC)/Lambda-calcolo%20semplicemente%20tipizzato%20(STLC).md#^definizione-tipo-nel-stlcb) $\alpha$ con la **sostituzione** $\theta(\alpha)$:
> 
> $$
> \begin{align*}{}
> \theta \colon \tau & \to \tau \\
> \alpha & \mapsto \theta(\alpha)
> \end{align*}
> $$
^definizione-sostituzione

Da questa [sostituzione](Informatica/Lambda-calcolo/Lambda-calcolo%20semplicemente%20tipizzato%20(STLC)/Algoritmo%20di%20inferenza.md#^definizione-sostituzione) otteniamo una possibile [_soluzione_](Informatica/Lambda-calcolo/Lambda-calcolo%20semplicemente%20tipizzato%20(STLC)/Algoritmo%20di%20inferenza.md#^definizione-soluzione) dell'[algoritmo di inferenza](Informatica/Lambda-calcolo/Lambda-calcolo%20semplicemente%20tipizzato%20(STLC)/Algoritmo%20di%20inferenza.md#^algoritmo-di-inferenza).

> [!definizione]+ Definizione: soluzione
> 
> Nell'[algoritmo di inferenza](Informatica/Lambda-calcolo/Lambda-calcolo%20semplicemente%20tipizzato%20(STLC)/Algoritmo%20di%20inferenza.md#^algoritmo-di-inferenza), dato un sistema%% link %% di $n$ [vincoli](Informatica/Lambda-calcolo/Lambda-calcolo%20semplicemente%20tipizzato%20(STLC)/Algoritmo%20di%20inferenza.md#^definizione-vincolo) $\{ \tau_i = \sigma_i \}_{1 \le i \le n}$ e una [sostituzione](Informatica/Lambda-calcolo/Lambda-calcolo%20semplicemente%20tipizzato%20(STLC)/Algoritmo%20di%20inferenza.md#^definizione-sostituzione) $\theta$, diciamo che $\theta$ è una **soluzione** (o **unificatore**) del sistema%% link %% se, per ogni $1 \le i \le n$:
> 
> $$
> \theta(\tau_i) = \theta(\sigma_i)
> $$
^definizione-soluzione

> [!attenzione]+ Attenzione: differenza tra gli $\color{#FFBF7F} =$ nella definizione di _soluzione_
> 
> Nella [definizione di _soluzione_](Informatica/Lambda-calcolo/Lambda-calcolo%20semplicemente%20tipizzato%20(STLC)/Algoritmo%20di%20inferenza.md#^definizione-soluzione), i due $=$ che compaiono rispettivamente nel sistema%% link %% di $n$ [vincoli](Informatica/Lambda-calcolo/Lambda-calcolo%20semplicemente%20tipizzato%20(STLC)/Algoritmo%20di%20inferenza.md#^definizione-vincolo) $\{ \tau_i = \sigma_i \}_{1 \le i \le n}$ e nella relazione di uguaglianza%% link %% $\theta(\tau_i) = \theta(\sigma_i)$ non significano la stessa cosa: mentre nel primo caso serve solo come "promemoria" per ricordarsi di come sono "collegate" tra di loro le [espressione di tipo](Informatica/Lambda-calcolo/Lambda-calcolo%20semplicemente%20tipizzato%20(STLC)/Algoritmo%20di%20inferenza.md#^definizione-espressione-di-tipo), nel secondo indica una vera e propria uguaglianza%% link %% tra i risultati delle [sostituzioni](Informatica/Lambda-calcolo/Lambda-calcolo%20semplicemente%20tipizzato%20(STLC)/Algoritmo%20di%20inferenza.md#^definizione-sostituzione).

In particolare, usando l'[algoritmo di risoluzione](Informatica/Lambda-calcolo/Lambda-calcolo%20semplicemente%20tipizzato%20(STLC)/Algoritmo%20di%20inferenza.md#^algoritmo-di-risoluzione) per "ridurre al minimo" il sistema%% link %% di [vincoli](Informatica/Lambda-calcolo/Lambda-calcolo%20semplicemente%20tipizzato%20(STLC)/Algoritmo%20di%20inferenza.md#^definizione-vincolo), otterremo non una [soluzione](Informatica/Lambda-calcolo/Lambda-calcolo%20semplicemente%20tipizzato%20(STLC)/Algoritmo%20di%20inferenza.md#^definizione-soluzione) qualsiasi ma la [_soluzione più generale_](Informatica/Lambda-calcolo/Lambda-calcolo%20semplicemente%20tipizzato%20(STLC)/Algoritmo%20di%20inferenza.md#^definizione-soluzione-piu-generale), che ci permette di ricavare a partire da essa tutte le altre possibili [soluzioni](Informatica/Lambda-calcolo/Lambda-calcolo%20semplicemente%20tipizzato%20(STLC)/Algoritmo%20di%20inferenza.md#^definizione-soluzione).

> [!definizione]+ Definizione: soluzione più generale
> 
> Nell'[algoritmo di inferenza](Informatica/Lambda-calcolo/Lambda-calcolo%20semplicemente%20tipizzato%20(STLC)/Algoritmo%20di%20inferenza.md#^algoritmo-di-inferenza), dato un sistema%% link %% di $n$ [vincoli](Informatica/Lambda-calcolo/Lambda-calcolo%20semplicemente%20tipizzato%20(STLC)/Algoritmo%20di%20inferenza.md#^definizione-vincolo) $\{ \tau_i = \sigma_i \}_{1 \le i \le n}$ e una [soluzione](Informatica/Lambda-calcolo/Lambda-calcolo%20semplicemente%20tipizzato%20(STLC)/Algoritmo%20di%20inferenza.md#^definizione-soluzione) $\theta$, diciamo che $\theta$ è la **soluzione più generale** (o **unificatore più generale**) del sistema%% link %% se ogni [soluzione](Informatica/Lambda-calcolo/Lambda-calcolo%20semplicemente%20tipizzato%20(STLC)/Algoritmo%20di%20inferenza.md#^definizione-soluzione) del sistema%% link %% è ottenibile componendo%% link a composizione di funzioni %% $\theta$ con un'altra [sostituzione](Informatica/Lambda-calcolo/Lambda-calcolo%20semplicemente%20tipizzato%20(STLC)/Algoritmo%20di%20inferenza.md#^definizione-sostituzione).
^definizione-soluzione-piu-generale

# 4 - Definizione dell'algoritmo

Dopo aver esplicitato il funzionamento dell'[algoritmo di inferenza](Informatica/Lambda-calcolo/Lambda-calcolo%20semplicemente%20tipizzato%20(STLC)/Algoritmo%20di%20inferenza.md#^algoritmo-di-inferenza) attraverso le 3 fasi di cui si compone, possiamo finalmente dichiararlo formalmente.

> [!algoritmo]+ Algoritmo di inferenza
> 
> Data una [$\lambda^\to_\text{Bool}$-espressione](Informatica/Lambda-calcolo/Lambda-calcolo%20semplicemente%20tipizzato%20(STLC)/Lambda-calcolo%20semplicemente%20tipizzato%20(STLC).md#^definizione-termine-nel-stlcb) $T$, l'**algoritmo di inferenza** permette di inferire%% link %% il [tipo](Informatica/Lambda-calcolo/Lambda-calcolo%20semplicemente%20tipizzato%20(STLC)/Lambda-calcolo%20semplicemente%20tipizzato%20(STLC).md#^definizione-tipo-nel-stlcb) di $T$.
> 
> I passi da seguire sono i seguenti:
> 
> 1. Costruire l'[albero sintattico](Informatica/Lambda-calcolo/Lambda-calcolo%20semplicemente%20tipizzato%20(STLC)/Algoritmo%20di%20inferenza.md#^definizione-albero-sintattico) $\text{Tree}[T]$.
> 2. Su ogni nodo%% link %% dell'[albero sintattico](Informatica/Lambda-calcolo/Lambda-calcolo%20semplicemente%20tipizzato%20(STLC)/Algoritmo%20di%20inferenza.md#^definizione-albero-sintattico) $\text{Tree}[T]$ annotare delle [espressioni di tipo](Informatica/Lambda-calcolo/Lambda-calcolo%20semplicemente%20tipizzato%20(STLC)/Algoritmo%20di%20inferenza.md#^definizione-espressione-di-tipo) e generare i rispettivi [vincoli](Informatica/Lambda-calcolo/Lambda-calcolo%20semplicemente%20tipizzato%20(STLC)/Algoritmo%20di%20inferenza.md#^definizione-vincolo) seguendo questa tabella:
> 
> | **Contenuto del nodo%% link %%**                                                                                                                                                                                                                                                                                                                                                                                                        | **Cosa annotare**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             | **[Vincoli](Informatica/Lambda-calcolo/Lambda-calcolo%20semplicemente%20tipizzato%20(STLC)/Algoritmo%20di%20inferenza.md#^definizione-vincolo) da generare**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             | **Risultato sull'[albero sintattico](Informatica/Lambda-calcolo/Lambda-calcolo%20semplicemente%20tipizzato%20(STLC)/Algoritmo%20di%20inferenza.md#^definizione-albero-sintattico)**       |
> | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
> | [Termine della forma di una variabile](Informatica/Lambda-calcolo/Lambda-calcolo%20semplicemente%20tipizzato%20(STLC)/Lambda-calcolo%20semplicemente%20tipizzato%20(STLC).md#^definizione-termine-nel-stlcb) $x$                                                                                                                                                                                                                        | Nel nodo%% link %% $x$: un [segnaposto](Informatica/Lambda-calcolo/Lambda-calcolo%20semplicemente%20tipizzato%20(STLC)/Algoritmo%20di%20inferenza.md#^definizione-espressione-di-tipo) $\alpha$, avendo cura di usare lo stesso segnaposto $\alpha$ per tutte le occorrenze di $x$ e **solo** per quelle                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          | ![espressione-di-tipo-variabile](Informatica/Lambda-calcolo/Lambda-calcolo%20semplicemente%20tipizzato%20(STLC)/_attachments/espressione-di-tipo-variabile.svg)                           |
> | [Termine della forma di una costante](Informatica/Lambda-calcolo/Lambda-calcolo%20semplicemente%20tipizzato%20(STLC)/Lambda-calcolo%20semplicemente%20tipizzato%20(STLC).md#^definizione-termine-nel-stlcb) $c$                                                                                                                                                                                                                         | Nel nodo%% link %% $c$: il [tipo booleano](Informatica/Lambda-calcolo/Lambda-calcolo%20semplicemente%20tipizzato%20(STLC)/Algoritmo%20di%20inferenza.md#^definizione-espressione-di-tipo) $\text{Bool}$                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          | ![espressione-di-tipo-costante-booleana](Informatica/Lambda-calcolo/Lambda-calcolo%20semplicemente%20tipizzato%20(STLC)/_attachments/espressione-di-tipo-costante-booleana.svg)<br>       |
> | [Termine della forma di un'astrazione](Informatica/Lambda-calcolo/Lambda-calcolo%20semplicemente%20tipizzato%20(STLC)/Lambda-calcolo%20semplicemente%20tipizzato%20(STLC).md#^definizione-termine-nel-stlcb) $\lambda x.M$                                                                                                                                                                                                              | Nel nodo%% link %% $\lambda x$: un [tipo funzione](Informatica/Lambda-calcolo/Lambda-calcolo%20semplicemente%20tipizzato%20(STLC)/Algoritmo%20di%20inferenza.md#^definizione-espressione-di-tipo) $\alpha \to \tau$, dove $\alpha$ è un [segnaposto](Informatica/Lambda-calcolo/Lambda-calcolo%20semplicemente%20tipizzato%20(STLC)/Algoritmo%20di%20inferenza.md#^definizione-espressione-di-tipo) (e, per ogni occorrenza di $x$ in $M$, dovremo usare sempre lo stesso [segnaposto](Informatica/Lambda-calcolo/Lambda-calcolo%20semplicemente%20tipizzato%20(STLC)/Algoritmo%20di%20inferenza.md#^definizione-espressione-di-tipo) $\alpha$) e $\tau$ è l'[espressione di tipo](Informatica/Lambda-calcolo/Lambda-calcolo%20semplicemente%20tipizzato%20(STLC)/Algoritmo%20di%20inferenza.md#^definizione-espressione-di-tipo) del sotto-albero%% link %% $\text{Tree}[M]$ |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          | ![espressione-di-tipo-astrazione](Informatica/Lambda-calcolo/Lambda-calcolo%20semplicemente%20tipizzato%20(STLC)/_attachments/espressione-di-tipo-astrazione.svg)                         |
> | [Termine della forma di un'applicazione](Informatica/Lambda-calcolo/Lambda-calcolo%20semplicemente%20tipizzato%20(STLC)/Lambda-calcolo%20semplicemente%20tipizzato%20(STLC).md#^definizione-termine-nel-stlcb) $M\ N$ con $\text{Tree}[M]$ con [espressione di tipo](Informatica/Lambda-calcolo/Lambda-calcolo%20semplicemente%20tipizzato%20(STLC)/Algoritmo%20di%20inferenza.md#^definizione-espressione-di-tipo) $\tau$ qualsiasi    | Nel nodo%% link %% $@$: un [segnaposto](Informatica/Lambda-calcolo/Lambda-calcolo%20semplicemente%20tipizzato%20(STLC)/Algoritmo%20di%20inferenza.md#^definizione-espressione-di-tipo) $\alpha$                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               | $\tau = \sigma \to \alpha$, dove $\tau$ è l'[espressione di tipo](Informatica/Lambda-calcolo/Lambda-calcolo%20semplicemente%20tipizzato%20(STLC)/Algoritmo%20di%20inferenza.md#^definizione-espressione-di-tipo) del sotto-albero%% Link %% $\text{Tree}[M]$ e $\sigma$ è l'[espressione di tipo](Informatica/Lambda-calcolo/Lambda-calcolo%20semplicemente%20tipizzato%20(STLC)/Algoritmo%20di%20inferenza.md#^definizione-espressione-di-tipo) del sotto-albero%% Link %% $\text{Tree}[N]$                                                                                                                                                                                                                             | ![espressione-di-tipo-applicazione](Informatica/Lambda-calcolo/Lambda-calcolo%20semplicemente%20tipizzato%20(STLC)/_attachments/espressione-di-tipo-applicazione.svg)                     |
> | [Termine della forma di un'applicazione](Informatica/Lambda-calcolo/Lambda-calcolo%20semplicemente%20tipizzato%20(STLC)/Lambda-calcolo%20semplicemente%20tipizzato%20(STLC).md#^definizione-termine-nel-stlcb) $M\ N$ con $\text{Tree}[M]$ con [espressione di tipo](Informatica/Lambda-calcolo/Lambda-calcolo%20semplicemente%20tipizzato%20(STLC)/Algoritmo%20di%20inferenza.md#^definizione-espressione-di-tipo) $\tau_1 \to \tau_2$ | Nel nodo%% link %% $@$: il [tipo](Informatica/Lambda-calcolo/Lambda-calcolo%20semplicemente%20tipizzato%20(STLC)/Algoritmo%20di%20inferenza.md#^definizione-espressione-di-tipo) $\tau_2$                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     | $\tau_1 = \sigma$, dove $\sigma$ è l'[espressione di tipo](Informatica/Lambda-calcolo/Lambda-calcolo%20semplicemente%20tipizzato%20(STLC)/Algoritmo%20di%20inferenza.md#^definizione-espressione-di-tipo) del sotto-albero%% Link %% $\text{Tree}[N]$                                                                                                                                                                                                                                                                                                                                                                                                                                                                    | ![espressione-di-tipo-applicazione2](Informatica/Lambda-calcolo/Lambda-calcolo%20semplicemente%20tipizzato%20(STLC)/_attachments/espressione-di-tipo-applicazione2.svg)                   |
> | [Termine della forma di una struttura di controllo](Informatica/Lambda-calcolo/Lambda-calcolo%20semplicemente%20tipizzato%20(STLC)/Lambda-calcolo%20semplicemente%20tipizzato%20(STLC).md#^definizione-termine-nel-stlcb) $\text{if}\ c\ M\ N$                                                                                                                                                                                          | Nel nodo%% link %% $\text{if}$: il [tipo](Informatica/Lambda-calcolo/Lambda-calcolo%20semplicemente%20tipizzato%20(STLC)/Algoritmo%20di%20inferenza.md#^definizione-espressione-di-tipo) $\tau_2$, dove $\tau_2$ è l'[espressione di tipo](Informatica/Lambda-calcolo/Lambda-calcolo%20semplicemente%20tipizzato%20(STLC)/Algoritmo%20di%20inferenza.md#^definizione-espressione-di-tipo) del sotto-albero%% link %% $\text{Tree}[M]$                                                                                                                                                                                                                                                                                                                                                                                                                                         | $\tau_1 = \text{Bool}$ dove $\tau_1$ è l'[espressione di tipo](Informatica/Lambda-calcolo/Lambda-calcolo%20semplicemente%20tipizzato%20(STLC)/Algoritmo%20di%20inferenza.md#^definizione-espressione-di-tipo) del sotto-albero $\text{Tree}[c]$<br><br>$\tau_2 = \tau_3$, dove $\tau_2$ è l'[espressione di tipo](Informatica/Lambda-calcolo/Lambda-calcolo%20semplicemente%20tipizzato%20(STLC)/Algoritmo%20di%20inferenza.md#^definizione-espressione-di-tipo) del sotto-albero $\text{Tree}[M]$ e $\tau_3$ è l'[espressione di tipo](Informatica/Lambda-calcolo/Lambda-calcolo%20semplicemente%20tipizzato%20(STLC)/Algoritmo%20di%20inferenza.md#^definizione-espressione-di-tipo) del sotto-albero $\text{Tree}[N]$ | ![espressione-di-tipo-struttura-di-controllo](Informatica/Lambda-calcolo/Lambda-calcolo%20semplicemente%20tipizzato%20(STLC)/_attachments/espressione-di-tipo-struttura-di-controllo.svg) |
>  
> 3. Sul sistema di $n$ [vincoli](Informatica/Lambda-calcolo/Lambda-calcolo%20semplicemente%20tipizzato%20(STLC)/Algoritmo%20di%20inferenza.md#^definizione-vincolo) $\text{Sys} = \{ \tau_i = \sigma_i \}_{1 \le i \le n}$ usare l'[algoritmo di risoluzione](Informatica/Lambda-calcolo/Lambda-calcolo%20semplicemente%20tipizzato%20(STLC)/Algoritmo%20di%20inferenza.md#^algoritmo-di-risoluzione).
> 4. Se l'[algoritmo di risoluzione](Informatica/Lambda-calcolo/Lambda-calcolo%20semplicemente%20tipizzato%20(STLC)/Algoritmo%20di%20inferenza.md#^algoritmo-di-risoluzione) ha fallito, allora la [$\lambda^\to_\text{Bool}$-espressione](Informatica/Lambda-calcolo/Lambda-calcolo%20semplicemente%20tipizzato%20(STLC)/Lambda-calcolo%20semplicemente%20tipizzato%20(STLC).md#^definizione-lambda-calcolo-semplicemente-tipizzato-con-booleani) **non** è [ben tipata](Informatica/Lambda-calcolo/Lambda-calcolo%20semplicemente%20tipizzato%20(STLC)/Lambda-calcolo%20semplicemente%20tipizzato%20(STLC).md#^definizione-termine-ben-tipato).
> 5. Se l'[algoritmo di risoluzione](Informatica/Lambda-calcolo/Lambda-calcolo%20semplicemente%20tipizzato%20(STLC)/Algoritmo%20di%20inferenza.md#^algoritmo-di-risoluzione) ha avuto successo, effettuare su ogni [vincolo](Informatica/Lambda-calcolo/Lambda-calcolo%20semplicemente%20tipizzato%20(STLC)/Algoritmo%20di%20inferenza.md#^definizione-vincolo) del nuovo sistema%% link %% $\text{Sys}' = \{ \alpha_i = \rho_i \}_{1 \le i \le n'}$ la [sostituzione](Informatica/Lambda-calcolo/Lambda-calcolo%20semplicemente%20tipizzato%20(STLC)/Algoritmo%20di%20inferenza.md#^definizione-sostituzione).
> 6. Il risultato del _passo 5_ è la [soluzione più generale](Informatica/Lambda-calcolo/Lambda-calcolo%20semplicemente%20tipizzato%20(STLC)/Algoritmo%20di%20inferenza.md#^definizione-soluzione-piu-generale) del sistema%% link %%.
^algoritmo-di-inferenza

# 5 - Estensioni dell'algoritmo

L'[algoritmo di inferenza](Informatica/Lambda-calcolo/Lambda-calcolo%20semplicemente%20tipizzato%20(STLC)/Algoritmo%20di%20inferenza.md#^algoritmo-di-inferenza) può essere esteso a versioni del [$\lambda^\to_\text{Bool}$-calcolo](Informatica/Lambda-calcolo/Lambda-calcolo%20semplicemente%20tipizzato%20(STLC)/Lambda-calcolo%20semplicemente%20tipizzato%20(STLC).md#^definizione-lambda-calcolo-semplicemente-tipizzato-con-booleani) con ulteriori [tipi](Informatica/Lambda-calcolo/Lambda-calcolo%20semplicemente%20tipizzato%20(STLC)/Lambda-calcolo%20semplicemente%20tipizzato%20(STLC).md#^definizione-tipo-nel-STLCB).

## 5.1 - Estensione con i numeri interi

Possiamo, per esempio, aggiungere tra i [tipi](Informatica/Lambda-calcolo/Lambda-calcolo%20semplicemente%20tipizzato%20(STLC)/Lambda-calcolo%20semplicemente%20tipizzato%20(STLC).md#^definizione-tipo-nel-STLCB) anche i numeri interi $\mathbb{Z}$%% link %%, sotto forma del [tipo](Informatica/Lambda-calcolo/Lambda-calcolo%20semplicemente%20tipizzato%20(STLC)/Lambda-calcolo%20semplicemente%20tipizzato%20(STLC).md#^definizione-tipo-nel-STLCB) $\text{Int}$:

$$
\tau ::= \text{Bool} \mid \text{Int} \mid {\color{#FF7F7F} \tau } \to {\color{#7F7FFF} \tau }
$$

Di conseguenza, nella definizione del [termine](Informatica/Lambda-calcolo/Lambda-calcolo%20semplicemente%20tipizzato%20(STLC)/Lambda-calcolo%20semplicemente%20tipizzato%20(STLC).md#^definizione-termine-nel-stlcb) basterà specificare che le costanti%% link %% $c$ potranno assumere come valori%% Link %% anche i numeri interi $\mathbb{Z}$%% link %%:

$$
c \in \{ \text{True}, \text{False}, 0, 1, -1, 2, -2, \ldots \}
$$

e, nella [forma sintattica della struttura di controllo](Informatica/Lambda-calcolo/Lambda-calcolo%20semplicemente%20tipizzato%20(STLC)/Lambda-calcolo%20semplicemente%20tipizzato%20(STLC).md#^definizione-termine-nel-stlcb) $\text{if}\ c\ M\ N$, $c$ potrà assumere solo i valori $\text{True}$ e $\text{False}$.

Nell'[algoritmo di inferenza](Informatica/Lambda-calcolo/Lambda-calcolo%20semplicemente%20tipizzato%20(STLC)/Algoritmo%20di%20inferenza.md#^algoritmo-di-inferenza) non si notano particolari differenze, ma:
- Tra le [espressione di tipo](Informatica/Lambda-calcolo/Lambda-calcolo%20semplicemente%20tipizzato%20(STLC)/Algoritmo%20di%20inferenza.md#^definizione-espressione-di-tipo), annoverare tra le possibili forme anche $\text{Int}$.
- Nella tabella di generazione dei [vincoli](Informatica/Lambda-calcolo/Lambda-calcolo%20semplicemente%20tipizzato%20(STLC)/Algoritmo%20di%20inferenza.md#^definizione-vincolo), specificare che ai [termine della forma di una costante](Informatica/Lambda-calcolo/Lambda-calcolo%20semplicemente%20tipizzato%20(STLC)/Lambda-calcolo%20semplicemente%20tipizzato%20(STLC).md#^definizione-termine-nel-stlcb) $c$ va assegnato il [tipo](Informatica/Lambda-calcolo/Lambda-calcolo%20semplicemente%20tipizzato%20(STLC)/Lambda-calcolo%20semplicemente%20tipizzato%20(STLC).md#^definizione-tipo-nel-STLCB) giusto a seconda del valore che assume, quindi:
	$$
	c \colon \begin{cases}
	\text{Bool} & \text{se } c \in \{ \text{True}, \text{False} \} \\
	\text{Int} & \text{se } c \in \{ 0, 1, -1, 2, -2, \ldots \}
	\end{cases}
	$$
- Nell'[algoritmo di risoluzione](Informatica/Lambda-calcolo/Lambda-calcolo%20semplicemente%20tipizzato%20(STLC)/Algoritmo%20di%20inferenza.md#^algoritmo-di-risoluzione), aggiungere che, se c'è un [vincolo](Informatica/Lambda-calcolo/Lambda-calcolo%20semplicemente%20tipizzato%20(STLC)/Algoritmo%20di%20inferenza.md#^definizione-vincolo) della forma
	$$
	\tau \to \sigma = \text{Int}
	$$
	oppure
	$$
	\text{Int} = \tau \to \sigma
	$$
	oppure
	$$
	\text{Int} = \text{Bool}
	$$
	oppure
	$$
	\text{Bool} = \text{Int}
	$$
	allora l'**algoritmo fallisce per _errore di tipo_**.

## 5.2 - Estensione con le liste

Questa volta, tra i [tipi](Informatica/Lambda-calcolo/Lambda-calcolo%20semplicemente%20tipizzato%20(STLC)/Lambda-calcolo%20semplicemente%20tipizzato%20(STLC).md#^definizione-tipo-nel-STLCB) annoveriamo anche le liste, costituite da elementi%% link %% di [tipo](Informatica/Lambda-calcolo/Lambda-calcolo%20semplicemente%20tipizzato%20(STLC)/Lambda-calcolo%20semplicemente%20tipizzato%20(STLC).md#^definizione-tipo-nel-STLCB) $\tau$:

$$
\tau ::= \text{Bool} \mid \text{Int} \mid {\color{#FF7F7F} \tau } \to {\color{#7F7FFF} \tau } \mid [\tau]
$$

Ovviamente, ciò implica che anche tra le [espressione di tipo](Informatica/Lambda-calcolo/Lambda-calcolo%20semplicemente%20tipizzato%20(STLC)/Algoritmo%20di%20inferenza.md#^definizione-espressione-di-tipo) dobbiamo annoverare tra le possibili forme anche $[\tau]$.

Nei valori possibili che può assumere un [termine-costante](Informatica/Lambda-calcolo/Lambda-calcolo%20semplicemente%20tipizzato%20(STLC)/Lambda-calcolo%20semplicemente%20tipizzato%20(STLC).md#^definizione-termine-nel-stlcb), ci includiamo i due costruttori canonici delle liste%% link %%, la lista vuota $[\ ]$%% link %% e il cons $(:)$%% link %%:

$$
c \in \{ \text{True}, \text{False}, 0, 1, -1, 2, -2, \ldots, [\ ], (:) \}
$$

In particolare, in Haskell il costruttore lista vuota $[\ ]$%% link %% ha tipo $[\alpha]$ e il costruttore cons $(:)$%% link %% ha tipo $\alpha \to [\alpha] \to [\alpha]$:

$$
\begin{array}{}
[\ ] :: [\alpha] \\
(:) :: \alpha \to [\alpha] \to [\alpha]
\end{array}
$$

Tenendo conto che nella stessa [$\lambda^\to_\text{Bool}$-espressione](Informatica/Lambda-calcolo/Lambda-calcolo%20semplicemente%20tipizzato%20(STLC)/Lambda-calcolo%20semplicemente%20tipizzato%20(STLC).md#^definizione-termine-nel-stlcb) possiamo costruire liste%% link %% di elementi di tipo diverso (per esempio, possono coesistere in una [$\lambda^\to_\text{Bool}$-espressione](Informatica/Lambda-calcolo/Lambda-calcolo%20semplicemente%20tipizzato%20(STLC)/Lambda-calcolo%20semplicemente%20tipizzato%20(STLC).md#^definizione-termine-nel-stlcb) una lista di tipo $[\text{Int}]$ e una lista di tipo $[\text{Bool}]$), abbiamo che le costanti dei costruttori canonici delle liste (cioè $[\ ]$ e $(:)$) devono essere interpretate come costanti polimorfe, cioè in ogni loro occorrenza possono assumere tipo diverso.

Per questo motivo, nella fase di generazione dei [vincolo](Informatica/Lambda-calcolo/Lambda-calcolo%20semplicemente%20tipizzato%20(STLC)/Algoritmo%20di%20inferenza.md#^definizione-vincolo) dell'[algoritmo di inferenza](Informatica/Lambda-calcolo/Lambda-calcolo%20semplicemente%20tipizzato%20(STLC)/Algoritmo%20di%20inferenza.md#^algoritmo-di-inferenza), per ogni occorrenza di uno di questi due costruttori dobbiamo stare attenti ad annotare nel nodo tipi che usano segnaposti%% link %% freschi: se, per esempio, in un nodo trovo $[\ ]$, lo annoto come una lista di elementi che hanno come tipo un segnaposto%% link %% $\alpha$; se lo troverò una seconda volta, lo annoterò come una lista di elementi che hanno come tipo un segnaposto%% Link %% $\beta$ e così via:
$$
\begin{array}{}
[\ ] \colon [\alpha] \\
\lambda x \colon \tau \to \sigma \\
\ldots \\
[\ ] \colon [\beta] \\
\end{array}
$$

Per quanto riguarda la fase di risoluzione dei vincoli, se abbiamo vincoli che impongono l'uguaglianza di tipi che hanno forme palesemente diverse (per esempio $[\tau] = \text{Bool}$, $\text{Bool} = [\tau]$ o $[\tau] = \sigma_1 \to \sigma_2$) allora l'algoritmo fallisce per errore di tipo.

Abbiamo anche un caso analogo a quello dei tipi funzioni in cui possiamo semplificare l'uguaglianza di due funzioni ($\tau \to \tau' = \sigma \to \sigma'$) imponendo l'uguaglianza dei domini e dei codomini ($\tau = \sigma$ e $\tau' = \sigma'$): se c'è un vincolo $[\tau] = [\sigma]$ allora possiamo rimpiazzarlo con $\tau = \sigma$.

## 5.3 - Estensione con funzioni di libreria

In generale, possiamo estendere l'algoritmo di inferenza assumendo che nelle espressioni da tipare compaiano le funzioni della libreria standard di Haskell (es. id, head, tail, ...), che potranno essere funzioni polimorfe (ossia il loro tipo non è un tipo specifico ma è una variabile di tipo) e per trattarle in questo modo va fatto come abbiamo appena fatto per le liste: ogni occorrenza deve usare nuove variabili di tipo (segnaposti) per ogni occorrenza.

## 5.4 - Estensione con definizioni ricorsive

Potremmo volere stabilire il tipo di una definizione ricorsiva della forma

$$
f = M
$$

dove $f$ può comparire in $M$.

Quel che dobbiamo fare è aggiungere il vincolo $\alpha = \tau$ dove $\alpha$ è la variabile di tipo associata a $f$ e $\tau$ è l'annotazione di $M$.

%% 
Perché abbiamo le definizioni ricorsive se abbiamo i combinatori di punti fissi?
Risposta: punti fissi non sono ben tipati se proviamo a eseguire l'algoritmo di inferenza, ciò avviene perché il sistema di tipi descritto finora garantisce che le espressioni siano fortemente normalizzanti, cioè non è possibile scrivere espressioni la cui valutazione va avanti all'infinito.
 %%

---

%% 
L'algoritmo di risoluzione dei vincoli (fase 3 dell'algoritmo di inferenza dei tipi) è ispirato direttamente a quello presentato nel seguente articolo. Alberto Martelli è professore emerito del dipartimento di informatica.
- [Alberto Martelli e Ugo Montanari, "An Efficient Unification Algorithm", 1982 File](https://informatica.i-learn.unito.it/mod/resource/view.php?id=272229)
    
- [John Hughes, "Why Functional Programming Matters", 1999 File](https://informatica.i-learn.unito.it/mod/resource/view.php?id=272249)
    Questo articolo illustra altre applicazioni della laziness.
    
- [Simon Peyton-Jones, "The implementation of functional programming languages", 1987 File](https://informatica.i-learn.unito.it/mod/resource/view.php?id=272251)
    Questo testo presenta i principi dell'implementazione dei linguaggi funzionali (ovvero, i principi che stanno alla base dell'implementazione del compilatore di Haskell).
%%

> [!fonti]+ Fonti
> 
> - 🏫 Corso di Laurea in Informatica (`L-31 R`) presso l'Università di Torino:
>     - Corso di _Linguaggi e Paradigmi di Programmazione_, A.A. 2020-21 ([pagina Moodle](https://informatica.i-learn.unito.it/enrol/index.php?id=1987)):
> 		- Prof. Luca Padovani, slide del corso:
> 			- [_Algoritmo di inferenza (fase 1)_](https://informatica.i-learn.unito.it/pluginfile.php/466485/mod_resource/content/0/lc_inferenza_1.pdf).
> 			- [_Algoritmo di inferenza (fase 2)_](https://informatica.i-learn.unito.it/pluginfile.php/466489/mod_resource/content/0/lc_inferenza_2.pdf).
> 			- [_Algoritmo di inferenza (fase 3)_](https://informatica.i-learn.unito.it/pluginfile.php/466493/mod_resource/content/0/lc_inferenza_3.pdf).
> 			- [_Algoritmo di inferenza (estensioni)_](https://informatica.i-learn.unito.it/pluginfile.php/466519/mod_resource/content/0/lc_inferenza_4.pdf).
> 		- Prof. Luca Padovani, videoregistrazioni del corso:
> 			- [_Algoritmo di inferenza (fase 1)_](https://informatica.i-learn.unito.it/mod/url/view.php?id=272205).
> 			- [_Algoritmo di inferenza (fase 2)_](https://informatica.i-learn.unito.it/mod/url/view.php?id=272209).
> 			- [_Algoritmo di inferenza (fase 3)_](https://informatica.i-learn.unito.it/mod/url/view.php?id=272213).
> 			- [_Algoritmo di inferenza (estensioni)_](https://informatica.i-learn.unito.it/mod/url/view.php?id=272239).
>     - Corso di _Linguaggi e Paradigmi di Programmazione_, A.A. 2025-26 ([pagina Moodle](https://informatica.i-learn.unito.it/course/view.php?id=3475)):
> 		- Prof. Viviana Bono, lezioni del corso.
> - 🌐 [_Lambda-calcolo_](https://it.wikipedia.org/wiki/Lambda_calcolo) su Wikipedia in lingua italiana, [archiviato sulla Wayback Machine](https://web.archive.org/web/20251125013725/https://it.wikipedia.org/wiki/Lambda_calcolo) in data 25 novembre 2025.
> - 🌐 [_Simply typed lambda calculus_](https://en.wikipedia.org/wiki/Simply_typed_lambda_calculus) su Wikipedia in lingua inglese, [archiviato sulla Wayback Machine](https://web.archive.org/web/20251125013806/https://en.wikipedia.org/wiki/Simply_typed_lambda_calculus) in data 25 novembre 2025.
