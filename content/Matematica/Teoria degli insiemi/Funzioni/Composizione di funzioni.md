
> [!premessa]+ Premessa
> 
> Ciao! Se è la prima volta che capiti su questo sito, ti consiglio di consultare la [pagina principale](index.md) di questo cosiddetto _Giardino Digitale_ per scoprire meglio cos'è e come navigarlo.
> 
> Lo stato di questa nota è al momento: 🟡 <font color="#FFFF7F">_Incompleta_</font>.

---

> [!definizione]+ Definizione: composizione di due funzioni
> Date due [funzioni](Matematica/Teoria%20degli%20insiemi/Funzioni/Funzioni.md#^definizione-funzione) $f\colon A\to B$ e $g\colon B \to C$ (dove $\text{cod}(f) = \text{dom}(g) = B$), la **composizione** di $f$ e $g$, denotata con "$g \circ f$", è la funzione:
> $$
> \begin{align*}
> g \circ f \colon A & \to C \\
> a & \mapsto g(f(a))
> \end{align*}
> $$
^definizione-composizione-di-due-funzioni

> [!osservazione]+ Osservazione: composizione rappresentata con le frecce
> La notazione "a frecce" delle [funzioni](Matematica/Teoria%20degli%20insiemi/Funzioni/Funzioni.md#^definizione-funzione) permette di rappresentare semplicemente la composizione $g \circ f$ come:
> 
> $$
> A \xrightarrow{f} B \xrightarrow{g} C,\quad A \xrightarrow{g\circ f} C
> $$
> 
> dove entrambi i percorsi che può seguire un elemento $a \in A$ per arrivare in $C$ danno lo stesso risultato.

> [!esempio]- Esempio: composizione di $\color{#7F7FFF} f(x)=x^2$ con $\color{#7F7FFF} g(x)=4x+1$
> Date due [funzioni](Matematica/Teoria%20degli%20insiemi/Funzioni/Funzioni.md#^definizione-funzione) $f\colon \mathbb{R}\to \mathbb{R},f(x)=x^2$ e $g\colon \mathbb{R}\to \mathbb{R},g(x)=4x+1$, allora la [funzione composta](Composizione%20di%20funzioni.md#^definizione-composizione-di-due-funzioni) $g\circ f$ è definita da
> $$
> (g\circ f)(x)=g(f(x))=4f(x)+1=4x^2+1
> $$
> Invertendo i ruoli di $f$ e $g$, è possibile definire anche la funzione composta $f\circ g$ definita da
> $$
> (f\circ g)(x)=f(g(x))=(g(x))^2=(4x+1)^2
> $$
^esempio-composizione-di-funzioni

> [!attenzione]+ Attenzione: composizione non è commutativa!
> 
> L'[esempio precedente](Composizione%20di%20funzioni.md#^esempio-composizione-di-funzioni) mostra che in generale le [funzioni composte](Composizione%20di%20funzioni.md#^definizione-composizione-di-due-funzioni) $g \circ f$ e $f \circ g$ non coincidono: l'operazione di composizione tra funzioni **non è commutativa**.

> [!osservazione]+ Osservazione: composizione di una funzione costante con altre funzioni
> Data una [funzione costante](Matematica/Teoria%20degli%20insiemi/Funzioni/Funzioni.md#^definizione-funzione-costante)
> $$
> \begin{align*}
> f_\beta\colon A & \to B \\
> a & \mapsto \beta
> \end{align*}
> $$
> allora per ogni funzione $g\colon B\to C$ e per ogni funzione $h\colon D\to A$ si ha:
> 
> - $\forall a \in A \big( (g\circ f_\beta)(a)=g(\beta) \big)$.
> - $\forall d \in D \big( (f_\beta\circ h)(d)=f_\beta(h(d))=\beta \big)$.
> 
> Quindi $g \circ f_\beta\colon A\to C$ è la funzione costante $f_\beta({g(\beta)})$ e $f_\beta\circ h\colon D \to B$ è la funzione costante $f_\beta$ con dominio $D$. Dal punto di vista grafico:
> $$ D \xrightarrow{h} A \xrightarrow{f_\beta} B \xrightarrow{g} C, \quad D \xrightarrow{f_\beta} B, \quad A \xrightarrow{f(g(\beta))} C $$
> %%da confermare che sia corretto%%

%% 
Osservazione 1.1.12 di pagina 14 di Dambrosio, mettere il grafico a centro pagina
%%

> [!esempio]- Esempio: composizione di funzioni di tempo
> 
> In un moto rettilineo, dato il tempo $t$ misurato in secondi e la posizione $y$ al tempo $t$ misurata in metri, supponiamo che $t$ e $y$ siano legate dalla relazione $y = g(t)$ con $g(t) = t^2 + t$ per ogni $t \ge 0$.
> 
> Supponiamo ora che il tempo sia riscalato in minuti, denotato stavolta con $x$, per cui vale quindi la relazione $t = f(x)$ con $f(x) = 60x$.
> 
> Ci chiediamo quale sia la relazione che intercorre tra la posizione $y$ e il tempo $x$ misurato in minuti: per rispondere a questa domanda è sufficiente sostituire l'espressione di $t$ in funzione di $x$ nella relazione $y = g(t)$; si ha quindi
> 
> $$
> \forall x \ge 0 \left(
> \begin{align*}
> y &= t^2 + t \\
> &= (60x)^2 + (60x) \\
> &= 3600x^2 + 60x
> \end{align*}
> \right) 
> $$
> 
> Abbiamo così introdotto una [funzione composta](Composizione%20di%20funzioni.md#^definizione-composizione-di-due-funzioni) di $g$ ed $f$:
> 
> $$
> g(f(x)) = g \circ f
> $$

> [!attenzione]+ Attenzione: necessità di far coincidere dominio e codominio nella composizione
> 
> Consideriamo le [funzioni](Matematica/Teoria%20degli%20insiemi/Funzioni/Funzioni.md#^definizione-funzione) $f$ e $g$ definite da
> 
> $$
> f(x) = x - 4
> $$
> 
> e
> 
> $$
> g(x) = \sqrt x
> $$
> 
> Osserviamo che la funzione $f$ è definita per ogni $x \in \mathbb{R}$, mentre la funzione $g$ è definita per ogni $x \ge 0$%% perché non è definita una funzione nelle radici %%.
> 
> Un semplice calcolo mostra che
> 
> $$
> \begin{align*}
> (g \circ f)(13) &= g(f(13)) \\
> &= \sqrt{f(13)} \\
> &= \sqrt{13-4} \\
> &= \sqrt 9 \\
> &= 3
> \end{align*}
> $$
> 
> Se però volessimo calcolare $(g \circ f)(1)$ incontreremmo un problema: infatti $f(1)=-3$ e dunque $g(f(1))$ non esiste perché $\sqrt{-3}$ non è definito in $\mathbb{R}$.
> 
> Osserviamo quindi il motivo per cui, nella [definizione di _funzione composta_](Composizione%20di%20funzioni.md#^definizione-composizione-di-due-funzioni), viene richiesto che il [codominio](Matematica/Teoria%20degli%20insiemi/Funzioni/Funzioni.md#^definizione-funzione) di $f$ debba coincidere con il dominio di $g$.

# 1 - Monotonia e composizione di funzioni

Ora vediamo una proposizione%% link %% che lega la [monotonia](Proprietà%20delle%20funzioni.md#^definizione-funzione-strettamente-decrescente-o-monotona-su-un-intervallo) alla [composizione di funzioni](Composizione%20di%20funzioni.md#^definizione-composizione-di-due-funzioni).

> [!proposizione]+ Regola dei segni per la monotonia della funzione composta
> 
> Date due [funzioni](Matematica/Teoria%20degli%20insiemi/Funzioni/Funzioni.md#^definizione-funzione) $f \colon \text{dom}(f) \to \mathbb{R}$ e $g \colon \text{dom}(g) \to \mathbb{R}$ (con $\text{rng}(f) \subseteq \text{dom}(g)$) e due intervalli%% Link %% $I \subseteq \text{dom}(f)$ e $g \subseteq \text{dom}(g)$:
> - Se $f$ è [(strettamente) crescente](Proprietà%20delle%20funzioni.md#^definizione-funzione-strettamente-decrescente-o-monotona-su-un-intervallo) su $I$ e $g$ è [(strettamente) crescente](Proprietà%20delle%20funzioni.md#^definizione-funzione-strettamente-decrescente-o-monotona-su-un-intervallo) su $J$, allora la loro [composizione](Composizione%20di%20funzioni.md#^definizione-composizione-di-due-funzioni) $g \circ f$ è [(strettamente) crescente](Proprietà%20delle%20funzioni.md#^definizione-funzione-strettamente-decrescente-o-monotona-su-un-intervallo) su $I$.
> - Se $f$ è [(strettamente) decrescente](Proprietà%20delle%20funzioni.md#^definizione-funzione-strettamente-decrescente-o-monotona-su-un-intervallo) su $I$ e $g$ è [(strettamente) crescente](Proprietà%20delle%20funzioni.md#^definizione-funzione-strettamente-decrescente-o-monotona-su-un-intervallo) su $J$, allora la loro [composizione](Composizione%20di%20funzioni.md#^definizione-composizione-di-due-funzioni) $g \circ f$ è [(strettamente) decrescente](Proprietà%20delle%20funzioni.md#^definizione-funzione-strettamente-decrescente-o-monotona-su-un-intervallo) su $I$.
> - Se $f$ è [(strettamente) crescente](Proprietà%20delle%20funzioni.md#^definizione-funzione-strettamente-decrescente-o-monotona-su-un-intervallo) su $I$ e $g$ è [(strettamente) decrescente](Proprietà%20delle%20funzioni.md#^definizione-funzione-strettamente-decrescente-o-monotona-su-un-intervallo) su $J$, allora la loro [composizione](Composizione%20di%20funzioni.md#^definizione-composizione-di-due-funzioni) $g \circ f$ è [(strettamente) decrescente](Proprietà%20delle%20funzioni.md#^definizione-funzione-strettamente-decrescente-o-monotona-su-un-intervallo) su $I$.
> - Se $f$ è [(strettamente) decrescente](Proprietà%20delle%20funzioni.md#^definizione-funzione-strettamente-decrescente-o-monotona-su-un-intervallo) su $I$ e $g$ è [(strettamente) decrescente](Proprietà%20delle%20funzioni.md#^definizione-funzione-strettamente-decrescente-o-monotona-su-un-intervallo) su $J$, allora la loro [composizione](Composizione%20di%20funzioni.md#^definizione-composizione-di-due-funzioni) $g \circ f$ è [(strettamente) decrescente](Proprietà%20delle%20funzioni.md#^definizione-funzione-strettamente-decrescente-o-monotona-su-un-intervallo) su $I$.
> 
> |                                                                                                             | **$f$ è [(strettamente) crescente](Proprietà%20delle%20funzioni.md#^definizione-funzione-strettamente-decrescente-o-monotona-su-un-intervallo) su $I$**       | **$f$ è [(strettamente) decrescente](Proprietà%20delle%20funzioni.md#^definizione-funzione-strettamente-decrescente-o-monotona-su-un-intervallo) su $I$**     |
> | ----------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------- |
> | **$g$ è [(strettamente) crescente](Proprietà%20delle%20funzioni.md#^definizione-funzione-strettamente-decrescente-o-monotona-su-un-intervallo) su $J$** | $g \circ f$ è [(strettamente) crescente](Proprietà%20delle%20funzioni.md#^definizione-funzione-strettamente-decrescente-o-monotona-su-un-intervallo) su $I$   | $g \circ f$ è [(strettamente) decrescente](Proprietà%20delle%20funzioni.md#^definizione-funzione-strettamente-decrescente-o-monotona-su-un-intervallo) su $I$ |
> | **$g$ è [(strettamente) decrescente](Proprietà%20delle%20funzioni.md#^definizione-funzione-strettamente-decrescente-o-monotona-su-un-intervallo) su $J$ | $g \circ f$ è [(strettamente) decrescente](Proprietà%20delle%20funzioni.md#^definizione-funzione-strettamente-decrescente-o-monotona-su-un-intervallo) su $I$ | $g \circ f$ è [(strettamente) crescente](Proprietà%20delle%20funzioni.md#^definizione-funzione-strettamente-decrescente-o-monotona-su-un-intervallo) su $I$   |
^regola-dei-segni-per-la-monotonia-della-funzione-composta

> [!trucco]+ Trucco per ricordare la regola dei segni per la monotonia della funzione composta
> 
> La [regola dei segni per la monotonia della funzione composta](Composizione%20di%20funzioni.md#^regola-dei-segni-per-la-monotonia-della-funzione-composta) si chiama così proprio perché ricorda la regola dei segni per il prodotto di due numeri reali%% link %%:
> - Se le due [funzioni](Matematica/Teoria%20degli%20insiemi/Funzioni/Funzioni.md#^definizione-funzione) sono "concordi", cioè entrambe o [(strettamente) crescenti](Proprietà%20delle%20funzioni.md#^definizione-funzione-strettamente-decrescente-o-monotona-su-un-intervallo) o [(strettamente) decrescenti](Proprietà%20delle%20funzioni.md#^definizione-funzione-strettamente-decrescente-o-monotona-su-un-intervallo), allora la loro [composizione](Composizione%20di%20funzioni.md#^definizione-composizione-di-due-funzioni) è [(strettamente) crescente](Proprietà%20delle%20funzioni.md#^definizione-funzione-strettamente-decrescente-o-monotona-su-un-intervallo).
> - Se le due [funzioni](Matematica/Teoria%20degli%20insiemi/Funzioni/Funzioni.md#^definizione-funzione) sono "discordi", cioè una è [(strettamente) crescente](Proprietà%20delle%20funzioni.md#^definizione-funzione-strettamente-decrescente-o-monotona-su-un-intervallo) e l'altra è [(strettamente) decrescente](Proprietà%20delle%20funzioni.md#^definizione-funzione-strettamente-decrescente-o-monotona-su-un-intervallo), allora la loro [composizione](Composizione%20di%20funzioni.md#^definizione-composizione-di-due-funzioni) è [(strettamente) decrescente](Proprietà%20delle%20funzioni.md#^definizione-funzione-strettamente-decrescente-o-monotona-su-un-intervallo).

%% 
figure 1.24 e 1.25 pag. 23 Dambrosio
%%

%% 
Dimostrazione pag. 23 Dambrosio
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
