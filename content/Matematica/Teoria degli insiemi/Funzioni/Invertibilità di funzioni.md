
> [!premessa]+ Premessa
> 
> Ciao! Se è la prima volta che capiti su questo sito, ti consiglio di consultare la [pagina principale](index.md) di questo cosiddetto _Giardino Digitale_ per scoprire meglio cos'è e come navigarlo.
> 
> Lo stato di questa nota è al momento: 🔴 <font color="#FF7F7F">_Bozza_</font>.

---

I valori della temperatura in gradi Celsius ($C$) e in Kelvin ($K$) sono legati dalla relazione

$$
C = K - 273.15
$$

Questa formula esprime $C$ in funzione di $K$: supponiamo ora di voler determinare $K$ in funzione di $C$, cioè ricavare il valore di $K$ a partire da un dato valore di $C$. Si tratta quindi di determinare una formula del tipo $K = g(C)$: per far questo è sufficiente ricavare $K$ dalla relazione $C = K - 273.15$. Si ottiene quindi:

$$
K = C + 273.15
$$

Abbiamo cioè ricavato la _funzione inversa_ di $f$: a partire dalla [funzione](Matematica/Teoria%20degli%20insiemi/Funzioni/Funzioni.md#^definizione-funzione) $f$ che esprimeva la dipendenza di $C$ da $K$, data da

$$
f(K) = K - 273.15
$$

abbiamo ricavato una nuova funzione che esprime $K$ in funzione di $C$; essa si chiama _funzione inversa_ di $f$ e si denota con $f^{-1}$. Con riferimento alla funzione precedente, abbiamo dunque

$$
f^{-1}(C) = C + 273.15
$$

Osserviamo che il procedimento effettuato corrisponde alla risposta al seguente quesito: a partire da una relazione $C = f(K)$ è possibile ricavare _in modo unico_ $K$ quando è nota $C$? Si presti attenzione all'**unicità** del risultato: in questo caso $K$ è individuata in modo unico da $C$.

Alla luce di quest'ultima osservazione, è facile rendersi conto che la funzione inversa di $f$ non sempre esiste: per esempio se due variabili $x$ e $y$ sono legate dalla relazione $y = f(x)$ con $f(x) = x^2$ per ogni $x \in \mathbb{R}$, allora data una certa $y$ non è possibile risalire _in modo unico_ a $x$ tale che $x^2 = y$. Infatti, se per esempio $y = 9$, esistono due valori di $x$ tali che $x^2 = 9$, ossia $+3$ e $-3$.

L'esempio precedente pone quindi il problema di capire quando sia definita la funzione inversa; una semplice riflessione suggerisce che, affinché la funzione inversa sia definita, non devono esistere due valori diversi di $x$ aventi la stessa [immagine](Matematica/Teoria%20degli%20insiemi/Funzioni/Funzioni.md#^definizione-immagine) $f(x)$, ossia $f$ deve essere [iniettiva](Matematica/Teoria%20degli%20insiemi/Funzioni/Proprietà%20delle%20funzioni.md#^definizione-iniettivita).

> [!definizione]+ Definizione: funzione inversa
> 
> Data una [funzione iniettiva](Matematica/Teoria%20degli%20insiemi/Funzioni/Proprietà%20delle%20funzioni.md#^definizione-iniettivita) $f \colon A \to B$, si chiama **funzione inversa di $f$** la [funzione](Matematica/Teoria%20degli%20insiemi/Funzioni/Funzioni.md#^definizione-funzione)
> 
> $$
> f^{-1} \colon \ \text{rng}(f) \to A
> $$
> 
> definita dalla relazione
> 
> $$
> \forall x \in A, \forall y \in \text{rng}(f) \big( x = f^{-1}(y) \iff y = f(x) \big)
> $$
> 
> La funzione $f$ è detta **invertibile su $A$**.
^definizione-funzione-inversa

%% 
esempi:
- 1.1.16 pagina 17 Dambrosio
- 1.1.17 pagina 18 Dambrosio
%%

# 1 - Monotonia e invertibilità di funzioni

> [!proposizione]+ Proposizione sulla monotonia e invertibilità di funzioni
> 
> Data una [funzione](Matematica/Teoria%20degli%20insiemi/Funzioni/Funzioni.md#^definizione-funzione) $f \colon \text{dom}(f) \to \mathbb{R}$ e un intervallo%% link %% $I \subseteq \text{dom}(f)$:
> - Se $f$ è [strettamente crescente](Matematica/Teoria%20degli%20insiemi/Funzioni/Proprietà%20delle%20funzioni.md#^definizione-funzione-strettamente-decrescente-o-monotona-su-un-intervallo) su $I$, allora $f$ è [invertibile](Invertibilità%20di%20funzioni.md#^definizione-funzione-inversa) su $I$ e la sua [inversa](Invertibilità%20di%20funzioni.md#^definizione-funzione-inversa) $f^{-1}$ è [strettamente crescente](Matematica/Teoria%20degli%20insiemi/Funzioni/Proprietà%20delle%20funzioni.md#^definizione-funzione-strettamente-decrescente-o-monotona-su-un-intervallo) su $f(I)$.
> - Se $f$ è [strettamente decrescente](Matematica/Teoria%20degli%20insiemi/Funzioni/Proprietà%20delle%20funzioni.md#^definizione-funzione-strettamente-decrescente-o-monotona-su-un-intervallo) su $I$, allora $f$ è [invertibile](Invertibilità%20di%20funzioni.md#^definizione-funzione-inversa) su $I$ e la sua [inversa](Invertibilità%20di%20funzioni.md#^definizione-funzione-inversa) $f^{-1}$ è [strettamente decrescente](Matematica/Teoria%20degli%20insiemi/Funzioni/Proprietà%20delle%20funzioni.md#^definizione-funzione-strettamente-decrescente-o-monotona-su-un-intervallo) su $f(I)$.

%% 
dimostrazione (non presente nel libro)
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
> - 📚 Walter Dambrosio, _Analisi matematica - Fare e comprendere_, Zanichelli, 2018 (ISBN: `9788808220745`):
> 	- Parte I - _I concetti dell'analisi matematica_:
> 		- Capitolo 1 - _Funzioni e modelli_:
> 			- 1 - _Funzioni e grafici_:
> 				- 1.2 - _Funzione composta e funzione inversa_.
> 				- 1.3 - _Proprietà globali di una funzione su un intervallo_.
> - 📚 Sergio Lancelotti, _Lezioni di Analisi Matematica I_, Celid, 2020 (ISBN: `978-8867891979`):
> 	- Capitolo 2 - _Funzioni_:
> 		- 1 - _Nozioni preliminari_.
