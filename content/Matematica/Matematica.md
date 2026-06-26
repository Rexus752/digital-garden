
> [!premessa]+ Premessa
> 
> Ciao! Se è la prima volta che capiti su questo sito, ti consiglio di consultare la [pagina principale](index.md) di questo cosiddetto _Giardino Digitale_ per scoprire meglio cos'è e come navigarlo.
> 
> Lo stato di questa nota è al momento: 🔴 <font color="#FF7F7F">_Bozza_</font>.

---

%% 
dimostrazioni sempre come callout a parte perché se no i riferimenti non funzionano
%%

La [**matematica**](Matematica.md#^definizione-matematica) è una delle mie discipline preferite in assoluto. Mi ha sempre affascinato fin da quando ero piccolo, motivo per cui molto probabilmente ho fin da subito sviluppato una _forma mentis_ molto più tecnica che artistica/umanistica.

Dico spesso che, in un'altra vita, se non avessi sviluppato la passione per l'informatica%% Link %%, quasi certamente sarei finito per studiare matematica. Non che il percorso che ho scelto mi dispiaccia, anzi, l'approccio che ho avuto nei confronti dell'informatica%% Link %% a livello didattico (universitario) è stato particolarmente orientato alla [matematica](Matematica.md#^definizione-matematica), cosa che mi ha portato ad apprezzarla ulteriormente.

> [!definizione]+ Definizione: matematica
> 
> La **matematica** è la disciplina che studia le quantità, i numeri, lo spazio, le strutture, i calcoli e, in generale, gli oggetti astratti rigorosamente definiti, la loro stessa definizione e le relazioni tra essi.
^definizione-matematica

In questa pagina potresti trovare roba sparsa di [matematica](Matematica.md#^definizione-matematica) che non ho ancora asistemato in altre pagine.

# 1 - Distanza tra due punti sulla retta reale

La distanza di un punto $x$ dall'origine $0$ è la lunghezza ($\ge 0$) di questo segmento:

$$
d(x,0) = \begin{cases}
x & \text{se } x \ge 0 \\
-x & \text{se } x < 0
\end{cases}
$$

quindi $d(x,0) = |x|$.

La funzione $|x|$ è una funzione che coincide con la bisettrice del primo quadrante e del secondo quadrante.

La distanza invece tra due punti $x$ e $y$ è la lunghezza di questo segmento:

$$
d(x,y) = \begin{cases}
y-x &\text{se } y \ge x \\
x-y &\text{se } y<x
\end{cases} = |y-x|
$$

Fissato $y$, la distanza di $x$ da $y$ la possiamo rappresentare come la "traslazione" di $|x|$.

[!esempio]- Esempio

Quali sono i punti dela retta che distano al più (al massimo) 2 dall'origine?

$$
\{ x \in \mathbb{R} \mid d(x,0) \le 2 \} = \{ x \in \mathbb{R} \mid |x| \le 2 \} = \{ x \in \mathbb{R} \mid -2 \le x \le 2 \} = [-2,2]
$$

Se invece cerchiamo i punti con distanza strettamente minore di $2$ troviamo

$$
\{ x \in \mathbb{R} \mid d(x,0) < 2 \} = \{ x \in \mathbb{R} \mid |x| < 2 \} = \{ x \in \mathbb{R} \mid -2 < x < 2 \} = (-2,2)
$$

 I punti della retta che distano al più 3 dal punto di ascissa 1:
 
$$
\{ x \in \mathbb{R} \mid d(x,1) < 3 \} = \{ x \in \mathbb{R} \mid |x - 1| < 3 \} = \{ x \in \mathbb{R} \mid -3 < x - 1 < 3 \} = (-2,4)
$$

---

> [!fonti]+ Fonti
> 
> - 🌐 [_Matematica_](https://it.wikipedia.org/wiki/Matematica) su Wikipedia in lingua italiana, [archiviato sulla Wayback Machine](https://web.archive.org/web/20260408183630/https://it.wikipedia.org/wiki/Matematica) in data 8 aprile 2026.
> - 🏫 Corso di Laurea in Informatica (`L-31 R`) presso l'Università di Torino%% per la roba sulla distanza tra due punti %%:
> 	- Corso di _Analisi Matematica - canale C_, A.A. 2020-21 ([pagina Moodle](https://informatica.i-learn.unito.it/course/view.php?id=2075)):
> 		- Prof. Barutello Vivina Laura, videolezioni:
> 			- [_L6a_](https://informatica.i-learn.unito.it/local/streamingfilemanager/file.php/informatica.i-learn.unito.it/2075/L6a.mp4).