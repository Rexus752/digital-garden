
> [!premessa]+ Premessa
> 
> Ciao! Se è la prima volta che capiti su questo sito, ti consiglio di consultare la [pagina principale](index.md) di questo cosiddetto _Giardino Digitale_ per scoprire meglio cos'è e come navigarlo.
> 
> Lo stato di questa nota è al momento: 🔴 <font color="#FF7F7F">_Bozza_</font>.

---

Osserviamo alcune proprietà che potrebbero rispettare le [funzioni](Funzioni.md#^definizione-funzione).

# 1 - Funzioni limitate

> [!definizione]+ Definizione: funzioni limitate
> 
> Data una [funzione](Funzioni.md#^definizione-funzione) $f \colon D \to \mathbb{R}$ con il [dominio](Funzioni.md#^definizione-funzione) $D \subseteq \mathbb{R}$, allora:
> - $f$ si dice **superiormente limitata su $D$** se esiste un valore $M \in \mathbb{R}$ tale che:
> 	$$
> 	\exists M \in \mathbb{R}, \forall x \in D \big( f(x) \le M \big)
> 	$$
> - $f$ si dice **inferiormente limitata** su $D$ se esiste un valore $m \in \mathbb{R}$ tale che:
> 	$$
> 	\exists m \in \mathbb{R}, \forall x \in D \big( f(x) \ge m \big)
> 	$$
> - $f$ si dice **limitata** su $D$ se è sia superiormente sia inferiormente limitata su $D$, ossia se esistono due valori $m,M \in \mathbb{R}$ tali che:
> 	$$
> 	\exists m, M \in \mathbb{R}, \forall x \in D \big( m \le f(x) \le M \big)
> 	$$
^definizione-funzioni-limitate

%% 
Esempio di funzioni limitate dal punto di vista grafico (definizione 1.1.3 a pagina 8 del libro di Dambrosio)
%%

# 2 - Punti di massimo e minimo

> [!definizione]+ Definizione: punto di massimo relativo e assoluto
> 
> Data una [funzione](Funzioni.md#^definizione-funzione) $f \colon \text{dom}(f) \to \mathbb{R}$, un punto%% link %% $x_0 \in \text{dom}(f)$ si dice **punto di massimo relativo (o locale) di $f$ su $\text{dom}(f)$** se esiste un valore%% link %% $r > 0$ tale che
> 
> $$
> \forall x \in D \cap (x_0 - r, x_0 + r) . \big( f(x) \le f(x_0) \big) 
> $$
> 
> e in questo caso il valore%% Link %% $f(x_0)$ si dice **massimo relativo (o locale) di $f$**.
> 
> Se $f(x) \le f(x_0)$ per ogni $x \in D$, allora $x_0$ si dice **punto di massimo assoluto (o globale) di $f$ su $\text{dom}(f)$** e il valore%% link %% $f(x_0)$ si dice **massimo assoluto (o globale) di $f$ su $\text{dom}(f)$**.
^definizione-punto-di-massimo-relativo-e-assoluto

> [!definizione]+ Definizione: punto di minimo relativo e assoluto
> 
> Data una [funzione](Funzioni.md#^definizione-funzione) $f \colon \text{dom}(f) \to \mathbb{R}$, un punto%% link %% $x_0 \in \text{dom}(f)$ si dice **punto di minimo relativo (o locale) di $f$ su $\text{dom}(f)$** se esiste un valore%% link %% $r > 0$ tale che
> 
> $$
> \forall x \in D \cap (x_0 - r, x_0 + r) . \big( f(x) \ge f(x_0) \big) 
> $$
> 
> e in questo caso il valore%% Link %% $f(x_0)$ si dice **minimo relativo (o locale) di $f$**.
> 
> Se $f(x) \ge f(x_0)$ per ogni $x \in D$, allora $x_0$ si dice **punto di minimo assoluto (o globale) di $f$ su $\text{dom}(f)$** e il valore%% link %% $f(x_0)$ si dice **minimo assoluto (o globale) di $f$ su $\text{dom}(f)$**.
^definizione-punto-di-minimo-relativo-e-assoluto

%% 
esempio figura 1.11 pag. 10 dambrosio
%%

# 3 - Parità e disparità

> [!definizione]+ Definizione: funzioni pari e dispari
> 
> Data una [funzione](Funzioni.md#^definizione-funzione) $f \colon D \to \mathbb{R}$ con il [dominio](Funzioni.md#^definizione-funzione) $D \subseteq \mathbb{R}$, allora:
> - $f$ si dice **pari** se:
> 	$$
> 	\forall x \in D \big( f(-x) = f(x) \big) 
> 	$$
> - $f$ si dice **dispari** se:
> 	$$
> 	\forall x \in D \big( f(-x) = -f(x) \big) 
> 	$$
^definizione-funzioni-pari-e-dispari

> [!osservazione]+ Osservazione: simmetria dei grafici di funzioni pari e dispari
> 
> In termini di [grafico](Funzioni.md#^definizione-grafico-di-una-funzione) $\Gamma_f$ di $f$ è semplice osservare che, per una [funzione pari](Proprietà%20delle%20funzioni.md#^definizione-funzioni-pari-e-dispari), vale
> 
> $$
> (x,y) \in \Gamma_f \iff (-x,y) \in \Gamma_f
> $$
> 
> mentre, per una [funzione dispari](Proprietà%20delle%20funzioni.md#^definizione-funzioni-pari-e-dispari), vale
> 
> $$
> (x,y) \in \Gamma_f \iff (-x,-y) \in \Gamma_f
> $$
> 
> Questo significa che il grafico%% link grafico grafico %% di una [funzione pari](Proprietà%20delle%20funzioni.md#^definizione-funzioni-pari-e-dispari) è simmetrico rispetto all'asse delle ordinate%% link %%, mentre il grafico%% link grafico grafico %% di una [funzione dispari](Proprietà%20delle%20funzioni.md#^definizione-funzioni-pari-e-dispari) è simmetrico rispetto all'origine.

%% esempio definizione 1.1.5 pagina 11 Dambrosio %%

# 4 - Periodicità

> [!definizione]+ Definizione: funzione periodica
> 
> Data una [funzione](Funzioni.md#^definizione-funzione) $f \colon D \to \mathbb{R}$ con il [dominio](Funzioni.md#^definizione-funzione) $D \subseteq \mathbb{R}$, $f$ si dice **periodica** se esiste un $T > 0$, detto **periodo di $f$**, tale che:
> 1. l'insieme $D$ soddisfa la proprietà
> 	$$
> 	x \in D \iff x + T \in D
> 	$$
> 	e
> 2. vale la relazione
> 	$$
> 	\forall x \in D \big( f(x+T) = f(x) \big) 
> 	$$
^definizione-funzione-periodica

> [!osservazione]+ Osservazione: grafico di una funzione periodica
> 
> È semplice osservare che il grafico%% link grafico grafico %% di una [funzione periodica](Proprietà%20delle%20funzioni.md#^definizione-funzione-periodica) $f$ di periodo $T$ è invariante per traslazioni orizzontali di ampiezza $T$: questo significa che è sufficiente tracciare il grafico di $f$ su un intervallo di lunghezza $T$ e ripeterlo infinite volte a destra e a sinistra dell'intervallo considerato.

%% 
esempio figura 1.14 pag. 12 dambrosio
%%

# 5 - Iniettività, suriettività e biettività

## 5.1 - Iniettività

> [!definizione]+ Definizione: iniettività
> 
> Una [funzione](Funzioni.md#^definizione-funzione) $f \colon A \to B$ si dice che è _**iniettiva**_ o che è una _**iniezione**_ se, per ogni scelta di due numeri $a_1, a_2 \in A$ con $a_1 \ne a_2$, si ha $f(a_1) \ne f(a_2)$:
> $$
> \forall a_1, a_2 \in A (a_1 \ne a_2 \implies f(a_1) \ne f(a_2))
> $$
^definizione-iniettivita

> [!esempio]- Esempio: esempio grafico dell'iniettività
> 
> Un esempio grafico dell'iniettività è il seguente, in cui ogni elemento dell'insieme $A=\{2,4,6\}$ è associato a un solo elemento dell'insieme $B=\{9,7,5,3\}$:
> ![[Iniettività.png]]

%%
La rappresentazione mediante diagrammi di Venn di una funzione iniettiva
f : A \to B è tale che ogni punto di B è raggiunto al più da una freccia.
%%

> [!esempio]- Esempio: iniettività della funzione $\color{#7F7FFF} f\colon \mathbb{Z}\to\mathbb{Z},n\mapsto2n+1$
> 
> Data una funzione $f\colon \mathbb{Z}\to\mathbb{Z},n\mapsto2n+1$, essa è iniettiva. Infatti, dati due interi $m\ne n$ si ha certamente $f(m)=2m+1\ne f(n)=2n+1$.

> [!esempio]- Esempio: non-iniettività della funzione $\color{#7F7FFF} f\colon\mathbb{R}\to\mathbb{R},x\mapsto x^2$
> Data una funzione $f\colon\mathbb{R}\to\mathbb{R},x\mapsto x^2$, essa non è iniettiva. Infatti, si ha $f(1)=f(-1)=1$ e, più in generale, $\forall x \in \mathbb{R}(f(x)=f(-x))$.

> [!esempio]- Esempio: iniettività della funzione proiezione $\color{#7F7FFF} p_1\colon A\times B\to A,(a,b)\mapsto a$
> Data una funzione proiezione $p_1\colon A\times B\to A,(a,b)\mapsto a$, siccome si ha $p_1((a,b))=a$ per ogni $(a,b)\in A\times B$ la funzione è iniettiva solo se $B$ consiste di un unico elemento: se $B$ contiene due elementi distinti $b_1$ e $b_2$ allora $p_1((a,b_1))=p_1((a,b_2))$.

> [!osservazione]+ Osservazione: rendere una funzione iniettiva restringendo il dominio
> Una funzione $f\colon A\to B$ non iniettiva può diventare iniettiva [restringendo](Funzioni.md#^definizione-funzione-restrizione) opportunamente il dominio. Per esempio, la funzione $f(x)=x^2$ che non è iniettiva sul dominio $\mathbb{R}$, può diventarlo se viene ristretto il dominio ai numeri reali non-negativi. Infatti, per ogni coppia di due numeri reali non-negativi distinti $x_1$ e $x_2$, si avrà sicuramente $x_1^2 \ne x_2^2$.

## 5.2 - Suriettività

> [!definizione]+ Definizione: suriettività
> Una [funzione](Funzioni.md#^definizione-funzione) $f\colon A\to B$ si dice che è _**suriettiva**_ o che è una _**suriezione**_ se ogni elemento del codominio è immagine di almeno un elemento del dominio:
> $$
> \forall y \in B, \exists x \in A (f(x) = y)
> $$
^definizione-suriettivita

> [!esempio]- Esempio: esempio grafico della suriettività
> Un esempio grafico della suriettività è il seguente, in cui ogni elemento dell'insieme $B=\{9,7,5\}$ è associato ad almeno un elemento della funzione $A=\{2,4,6,8\}$:
> ![[Suriettività.png]]

%%
La rappresentazione mediante diagrammi di Venn di una funzione suriettiva
f : A \to B è tale che ogni punto di B è raggiunto almeno da una freccia.
%%

> [!esempio]- Esempio: non-suriettività della funzione $\color{#7F7FFF} f\colon\mathbb{Z}\to\mathbb{Z},x\mapsto 2x+1$
> Data una funzione $f\colon\mathbb{Z}\to\mathbb{Z},x\mapsto 2x+1$, le immagini dei singoli elementi sono sempre numeri dispari e ogni numeri intero dispari $m$ può essere scritto nella forma $\forall k \in \mathbb{Z} (m = 2k+1)$. Dunque $m=f(k)$ e si può concludere che l'immagine di $f$ è costituita dagli interi dispari ovvero $\text{rng}(f)=2\mathbb{Z}+1$. Poiché $2\mathbb{Z}+1\ne\mathbb{Z}$, la funzione $f$ non è suriettiva.

> [!esempio]- Esempio: non-suriettività della funzione $\color{#7F7FFF} f\colon\mathbb{R}\to\mathbb{R},x\mapsto x^2$
> Data una funzione $f\colon\mathbb{R}\to\mathbb{R},x\mapsto x^2$, le immagini dei singoli elementi sono sempre numeri reali non negativo e ogni reale non negativo $y$ può essere scritto nella forma $\forall x \in \mathbb{R} (y=x^2)$. Dunque $y=f(x)$ e si può concludere che l'immagine di $f$ è costituita dai numeri reali positivi, ovvero $\text{rng}(f) = \{ x \in \mathbb{R} \mid x \ge 0 \}$. Poiché $\{ x \in \mathbb{R} \mid x \ge 0 \} \ne \mathbb{R}$, la funzione $f$ non è suriettiva.

> [!esempio]- Esempio: suriettività della funzione $\color{#7F7FFF} f\colon[0,+\infty]\to\mathbb{R},x\mapsto\log(x)$
> Data una funzione $f\colon[0,+\infty]\to\mathbb{R},x\mapsto\log(x)$, ogni numero reale $r$ è il logaritmo di un altro qualsiasi numero reale $x$ (basti prendere $x=e^r$). Dunque, dato che $\text{rng}(f)=\mathbb{R}$, la funzione è suriettiva.

> [!esempio]- Esempio: suriettività della funzione proiezione $\color{#7F7FFF} p_1\colon A\times B\to A,(a,b)\mapsto a$
> Data una funzione proiezione $p_1:A\times B \to A$, poiché $B\ne\emptyset$ (se $B$ fosse vuoto allora $A\times B =A\times\emptyset=\emptyset$ e non si potrebbe parlare di funzione) e dato un $a\in A$ si può sempre scrivere $\forall b \in B(a=p_1((a,b)))$. Pertanto, ogni $a \in A$ è anche in $\text{rng}(p_1)$, quindi $A=\text{rng}(p_1)$ e $p_1$ è suriettiva.

> [!osservazione]+ Osservazione: suriettività intesa come $\color{7F7F7F} \text{rng}(f)=B$
> Un'altra definizione della suriettività è quella secondo cui la funzione $f$, per essere suriettiva, deve avere l'immagine corrispondente al codominio:
> $$
> \text{rng}(f)=B
> $$
> In questo caso, infatti, si ha che non ci sono elementi del codominio senza una controimmagine in $A$.

## 5.3 - Biettività

> [!definizione]+ Definizione: biettività
> 
> Una [funzione](Funzioni.md#^definizione-funzione) $f \colon A\to B$ si dice che è _**biettiva**_ o che è una _**biezione**_ se è contemporaneamente sia [iniettiva](Proprietà%20delle%20funzioni.md#^definizione-iniettivita) che [suriettiva](Proprietà%20delle%20funzioni.md#^definizione-suriettivita), ovvero se per ogni elemento del codominio $y\in B$ esiste ed è unico un elemento del dominio $x \in A$ tale che $f(x)=y$:
> $$
> \forall y \in B, \exists! \, x \in A (f(x) = y)
> $$
^definizione-biettivita

> [!esempio]- Esempio: esempio grafico della biettività
> Un esempio grafico della biettività è il seguente, in cui ogni elemento dell'insieme $B=\{9,7,5,3\}$ è associato a uno e un solo elemento della funzione $A=\{2,4,6,8\}$:
> ![[Biettività.png]]

%%
La rappresentazione mediante diagrammi di Venn di una funzione biettiva
f : A \to B è tale che ogni punto di B è raggiunto esattamente da una
freccia.
%%

> [!esempio]- Esempio: biettività della funzione identità
> Per ogni insieme $A$, la [funzione identità](Funzioni.md#^definizione-funzione-identita) $\text{id}_A:A\to A$ è biettiva, in quanto a ogni elemento del codominio è associato un solo elemento del dominio (ossia se stesso).

> [!esempio]- Esempio: biettività della funzione $\color{#7F7FFF} f\colon\mathbb{R} \to \mathbb{R},x\mapsto x^2$ con restringimento di dominio
> Data una funzione $f\colon\mathbb{R}\to\mathbb{R},x\mapsto x^2$, essa non è né iniettiva, né suriettiva, ma può diventare biettiva [restringendo](Funzioni.md#^definizione-funzione-restrizione) il suo dominio ai numeri non-negativi $\{ x \in \mathbb{R} \mid x \ge 0 \}$ e pensandola con codominio $\{ x \in \mathbb{R} \mid x \ge 0 \}$ (se il codominio fosse $\mathbb{R}$, allora non potrebbe essere suriettiva, in quanto non ci sono numeri che, elevati alla seconda, danno numeri negativi). In questo modo, per ogni numero reale $x> 0$ esiste un solo $y> 0$ tale che $y=x^2$.

> [!esempio]- Esempio: biettività della funzione $\color{#7F7FFF} f\colon A\times B\to B\times A,(a,b)\mapsto(b,a)$
> La funzione $f\colon A\times B\to B\times A,(a,b)\mapsto(b,a)$ è una biezione. Infatti, ogni coppia $(b,a)\in B\times A$ è immagine solo di una coppia $(a,b)\in A \times B$.

%%
Osservazioni:
1 Se f : A \to A con A finito si ha che f è una biezione se e solo se f `e
una iniezione se e solo se f è una suriezione. Lo stesso vale per le
funzioni f : A \to B in cui A e B sono insiemi finiti con lo stesso
numero di elementi.
2 Se f : A \to B è iniettiva allora f : A \to rng(f ) (ovvero la stessa f ,
ma vista come funzione da A nella sua immagine) è una biezione.
3 Date f : A \to B e g : B \to C, si ha che se sia f che g sono iniettive
anche g ◦ f lo `e, e se f e g sono entrambe suriezioni anche g ◦ f lo `e.
In particolare, la composizione di due biezioni è una biezione.
4 Sia f : A \to B una funzione. Allora f è un'iniezione se e solo se
f -1(b) contiene al più un elemento per ogni b \in B, ed è una
suriezione se e solo se f -1(b) \ne \emptyset per ogni b \in B
%%

## 5.4 - Relazioni con la cardinalità

> [!proposizione]+ Proposizione: iniettività, suriettività e biettività dipendono dalla cardinalità
> Data una funzione $f\colon A\to B$, la sua iniettività, suriettività o biettività dipendono dalla sua cardinalità:
> 1. $f$ è suriettiva se e soltanto se $|f^{-1}(b)|\ge1$ per ogni $b\in B$.
> 2. $f$ è iniettiva se e soltanto se $|f^{-1}(b)|\le1$ per ogni $b\in B$.
> 3. $f$ è biettiva se e soltanto se è sia suriettiva che iniettiva, cioè se $|f^{-1}(b)| = 1$ per ogni $b \in B$.
> 
> > [!dimostrazione]- Dimostrazione
> > 
> > 1. La condizione che esista un elemento $a\in f^{-1}(b)$ (cioè che $|f^{-1}(b)|\ge1$) è equivalente, per la definizione di [controimmagine](Funzioni.md#^definizione-controimmagine), alla condizione che esista un $a \in A$ tale che $f(a)=b$.
> > 
> > 2. Si può dimostrare analogamente che $f$ non è iniettiva se e soltanto se esiste un $b\in B$ tale che $|f^{-1}(b)|\ge2$, in quanto in questo caso esistono due elementi distinti $a_1\ne a_2$ nel dominio tali che $f(a_1)=f(a_2)=b$.
> > 
> > 3. Una funzione per essere biettiva deve essere sia iniettiva che suriettiva, quindi dovendo essere $|f^{-1}(b)|$ sia $\ge1$ che $\le 1$, l'unico caso che soddisfa entrambe le condizioni è $|f^{-1}(b)\vDash1$.
> >    
> > $\blacksquare$
^proposizione-iniettivita-suriettivita-e-biettivita-dipendono-dalla-cardinalita

# 6 - Funzioni identicamente nulle

> [!definizione]+ Definizione: funzione identicamente nulla
> 
> Una [funzione](Funzioni.md#^definizione-funzione) $f \colon \text{dom}(f) \to \mathbb{R}$ si dice **identicamente nulla** su un [insieme](Teoria%20degli%20insiemi.md#^definizione-insieme) $A \subseteq \text{dom}(f)$ se $f(x) = 0$ per ogni $x \in A$:
> 
> $$
> \begin{array}{}
> f \colon \text{dom}(f) \to \mathbb{R} \text{ è identicamente nulla su } A \subseteq \text{dom}(f) \\
> \Updownarrow \\
> \forall x \in A . \big( f(x) = 0 \big) 
> \end{array}
> $$
^definizione-funzione-identicamente-nulla

# 7 - Monotonia

> [!definizione]+ Definizione: funzione (strettamente) (de)crescente o monotona su un intervallo
> 
> Data una [funzione](Funzioni.md#^definizione-funzione) $f \colon \text{dom}(f) \to \mathbb{R}$ e un intervallo%% link %% $I \subseteq \text{dom}(f)$:
> - si dice **crescente su $I$** se
> 	$$
> 	\forall x_1, x_2 \in I . \left( x_1 < x_2 \implies f(x_1) \le f(x_2) \right) 
> 	$$
> 	o, equivalentemente,
> 	$$
> 	\forall x_1, x_2 \in I . \left( \Delta x > 0 \implies \Delta f \ge 0 \right) 
> 	$$
> - si dice **strettamente crescente su $I$** se
> 	$$
> 	\forall x_1, x_2 \in I . \left( x_1 < x_2 \implies f(x_1) < f(x_2) \right) 
> 	$$
> 	o, equivalentemente,
> 	$$
> 	\forall x_1, x_2 \in I . \left( \Delta x > 0 \implies \Delta f > 0 \right) 
> 	$$
> - si dice **decrescente su $I$** se
> 	$$
> 	\forall x_1, x_2 \in I . \left( x_1 < x_2 \implies f(x_1) \ge f(x_2) \right) 
> 	$$
> 	o, equivalentemente,
> 	$$
> 	\forall x_1, x_2 \in I . \left( \Delta x > 0 \implies \Delta f \le 0 \right) 
> 	$$
> - si dice **strettamente decrescente su $I$** se
> 	$$
> 	\forall x_1, x_2 \in I . \left( x_1 < x_2 \implies f(x_1) > f(x_2) \right) 
> 	$$
> 	o, equivalentemente,
> 	$$
> 	\forall x_1, x_2 \in I . \left( \Delta x > 0 \implies \Delta f < 0 \right) 
> 	$$
> - si dice **monotona su $I$** se è crescente su $I$ o decrescente su $I$ e
> - si dice **strettamente monotona su $I$** se è strettamente crescente su $I$ oppure strettamente decrescente su $I$.
^definizione-funzione-strettamente-decrescente-o-monotona-su-un-intervallo

%% 
fare esempi grafici su ogni caso
%%

%% 
Osservazione

Il concetto di [monotonia](Proprietà%20delle%20funzioni.md#^definizione-funzione-strettamente-decrescente-o-monotona-su-un-intervallo) è legato a quello dell'ordinamento sulla retta reale: le funzioni crescenti mantengono l'ordinamento nel passaggio da $x$ a $f(x)$, mentre le funzioni decrescenti lo invertono:

figure 1.19, 1.20 pag. 20 Dmbrosio
%%

%% 
Osservazione: monotonia dal punto di vista grafico
pag. 21 Dambrosio
%%

%% 
Osservazione 1.1.18 pag. 21 Dambrosio
%%

> [!proposizione]+ Proposizione sulla somma di funzioni monotone
> 
> Date due [funzioni](Funzioni.md#^definizione-funzione) $f \colon \text{dom}(f) \to \mathbb{R}$ e $g \colon \text{dom}(g) \to \mathbb{R}$ e un intervallo%% link %% $I \subseteq \text{dom}(f) \cap \text{dom}(g)$:
> - Se $f_1$ ed $f_2$ sono [(strettamente) crescenti](Proprietà%20delle%20funzioni.md#^definizione-funzione-strettamente-decrescente-o-monotona-su-un-intervallo) su $I$ allora la loro [somma](Funzioni.md#^definizione-somma-di-funzioni) $f_1 + f_2$ è [(strettamente) crescente](Proprietà%20delle%20funzioni.md#^definizione-funzione-strettamente-decrescente-o-monotona-su-un-intervallo) su $I$.
> - Se $f_1$ ed $f_2$ sono [(strettamente) decrescenti](Proprietà%20delle%20funzioni.md#^definizione-funzione-strettamente-decrescente-o-monotona-su-un-intervallo) su $I$ allora la loro [somma](Funzioni.md#^definizione-somma-di-funzioni) $f_1 + f_2$ è [(strettamente) decrescente](Proprietà%20delle%20funzioni.md#^definizione-funzione-strettamente-decrescente-o-monotona-su-un-intervallo) su $I$.

%% 
dimostrazione per esercizio
%%

# 8 - Concavità e convessità di funzioni

Il concetto di _convessità e concavità_ di una [funzione](Funzioni.md#^definizione-funzione) è legato a quello dell'andamento del suo grafico%% Link %%: in modo simile a quanto avviene per gli angoli%% link alla concavità/covnessità di angoli %%, possiamo definire una [funzione](Funzioni.md#^definizione-funzione) come _concava_ quando il suo grafico%% Link %% ha la "pancia" verso l'alto (cioè graficamente si può rappresentare come "$\frown$"), mentre è _convessa_ quando il suo grafico%% link %% ha la "pancia" verso il basso (cioè "$\smile$").

Purtroppo però ci tocca definire questo concetto in termini rigorosamente matematici.

Data una [funzione](Funzioni.md#^definizione-funzione) $f \colon \text{dom}(f) \to \mathbb{R}$ e un intervallo%% link %% $I \subseteq \text{dom}(f)$, per ogni coppia di punti%% link %% $x_1, x_2 \in I$ con $x_1 < x_2$ indichiamo con $r_{1,2}$ la retta passante%% link %% per i punti%% link %% $(x_1, f(x_1))$ ed $(x_2, f(x_2))$: sappiamo%% link %% che essa ha equazione

$$
\begin{align*}
y &= f(x_1) + \dfrac{f(x_2) - f(x_1)}{x_2 - x_1} (x - x_1) \\
&= f(x_1) + \dfrac{\Delta f}{\Delta x}(x - x_1)
\end{align*}
$$

(dove $\dfrac{\Delta f}{\Delta x}$ è ovviamente il [quoziente di Newton](Variazioni%20e%20quoziente%20di%20Newton.md#^definizione-quoziente-di-newton)).

Ebbene, possiamo dire ora che la [funzione](Funzioni.md#^definizione-funzione) $f$ è _concava_ su $I$ se per ogni ogni coppia di punti%% link %% $x_1, x_2 \in I$ con $x_1 < x_2$ il grafico%% link %% di $f$ è "sopra" quello della retta%% link %% $r_{1,2}$ su tutto l'intervallo%% link %% $[x_1, x_2]$; analogamente, è _convessa_ su $I$ se per ogni ogni coppia di punti%% link %% $x_1, x_2 \in I$ con $x_1 < x_2$ il grafico%% link %% di $f$ è "sotto" quello della retta%% link %% $r_{1,2}$ su tutto l'intervallo%% link %% $[x_1, x_2]$.

%% 
Mettere figure 1.26, 1.27 pag. 24 Dambrosio
%%

La prossima definizione esprime matematicamente quanto abbiamo appena detto.

> [!definizione]+ Definizione: funzione concava o convessa su un intervallo
> 
> Data una [funzione](Funzioni.md#^definizione-funzione) $f \colon \text{dom}(f) \to \mathbb{R}$ e un intervallo%% link %% $I \subseteq \text{dom}(f)$:
> - $f$ si dice **concava su $I$** se
> 	$$
> 	\forall x_1, x_2 \in I, \forall x \in [x_1, x_2] . \left( x_1 < x_2 \implies f(x_1) \ge f(x_2) + \dfrac{\Delta f}{\Delta x}(x - x_1) \right) 
> 	$$
> - $f$ si dice **convessa su $I$** se
> 	$$
> 	\forall x_1, x_2 \in I, \forall x \in [x_1, x_2] . \left( x_1 < x_2 \implies f(x_1) \le f(x_2) + \dfrac{\Delta f}{\Delta x}(x - x_1) \right) 
> 	$$
^definizione-funzione-concava-o-convessa-su-un-intervallo

> [!osservazione]+ Osservazione: funzione né concava né convessa
> 
> Una [funzione](Funzioni.md#^definizione-funzione) potrebbe non essere né [concava](Proprietà%20delle%20funzioni.md#^definizione-funzione-concava-o-convessa-su-un-intervallo) né [convessa](Proprietà%20delle%20funzioni.md#^definizione-funzione-concava-o-convessa-su-un-intervallo) su un intervallo%% link %%: per esempio, la [funzione](Funzioni.md#^definizione-funzione) $f(x) = \sin x$ non è né [concava](Proprietà%20delle%20funzioni.md#^definizione-funzione-concava-o-convessa-su-un-intervallo) né [convessa](Proprietà%20delle%20funzioni.md#^definizione-funzione-concava-o-convessa-su-un-intervallo) sull'intervallo%% link %% $[-3,3]$, però è [concava](Proprietà%20delle%20funzioni.md#^definizione-funzione-concava-o-convessa-su-un-intervallo) in $[0, \pi]$ e [convessa](Proprietà%20delle%20funzioni.md#^definizione-funzione-concava-o-convessa-su-un-intervallo) in $[-\pi, 0]$.

%% 
grafico della funzione nell'osservazione
%%

---

> [!fonti]+ Fonti
> 
> - 🏫 Corso di Laurea in Informatica (`L-31 R`) presso l'Università di Torino:
> 	- Corso di _Matematica Discreta, Algebra e Geometria - parte di Matematica Discreta & Algebra (parte 1) - canale C_, A.A. 2023-24 ([pagina Moodle](https://informatica.i-learn.unito.it/course/view.php?id=2750)):
> 		- Proff. Chen Yu e Terracini Lea, lezioni in aula.
> 	- Corso di _Matematica Discreta, Algebra e Geometria - parte di Algebra Lineare & Geometria (parte 2) - canale C_, A.A. 2023-24 ([pagina Moodle](https://informatica.i-learn.unito.it/course/view.php?id=2750)):
> 		- Prof. Radeschi Marco, lezioni in aula.
> 	- Corso di _Logica Matematica_, A.A. 2022-23 ([pagina Moodle](https://informatica.i-learn.unito.it/course/view.php?id=2480)):
> 		- Proff. Andretta Alessandro, Motto Ros Luca e Viale Matteo, slide:
> 			- [_2.3 - Funzioni_](https://informatica.i-learn.unito.it/pluginfile.php/336712/mod_folder/content/0/Capitolo%202%20-%20Elementi%20di%20teoria%20degli%20insiemi/2.3%20-%20Funzioni_moodle.pdf).
> 	- Corso di _Analisi Matematica - canale C_, A.A. 2020-21 ([pagina Moodle](https://informatica.i-learn.unito.it/course/view.php?id=2075)):
> 		- Prof. Barutello Vivina Laura, videolezioni:
> 			- [_L8b_](https://informatica.i-learn.unito.it/local/streamingfilemanager/file.php/informatica.i-learn.unito.it/2075/L8b.mp4).%% per quanto riguarda la monotonia e le funzioni limitate %%
> - 📚 Walter Dambrosio, _Analisi matematica - Fare e comprendere_, Zanichelli, 2018 (ISBN: `9788808220745`):
> 	- Parte I - _I concetti dell'analisi matematica_:
> 		- Capitolo 1 - _Funzioni e modelli_:
> 			- 1 - _Funzioni e grafici_:
> 				- 1.1 - _Funzioni e loro rappresentazioni_.
> 				- 1.2 - _Funzione composta e funzione inversa_.
> 				- 1.3 - _Proprietà globali di una funzione su un intervallo_.
