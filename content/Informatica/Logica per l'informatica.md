
> [!premessa]+ Premessa
> 
> Ciao! Se è la prima volta che capiti su questo sito, ti consiglio di consultare la [pagina principale](index.md) di questo cosiddetto _Giardino Digitale_ per scoprire meglio cos'è e come navigarlo.
> 
> Lo stato di questa nota è al momento: 🔴 <font color="#FF7F7F">_Bozza_</font>.

---

Logica PER l'informatica: perché PER?

Focus: sintassi e semantica (interpretazione semantica della sintassi)
Fare differenza tra matematici "puri" e "sporchi"

# 1 - Strumenti

Rocq = proof assistant (prima si chiamava Coq, cambiato nome per un motivo)
- funzionale
- si cerca dimostrazioni da formule

Z3 = SMT-solver = dimostra teoremi
- si dimostra che formule sono soddisfacibili

# 2 - Esempio

Abbiamo due affermazioni:
1. "Se $x$ è un numero primo maggiore di $2$, allora $x$ è dispari" che si rappresenta in simboli come:
$$
\text{prime}(x) \land x > 2 \implies \text{odd}(x)
$$
2. "Non esiste un caso in cui $x$ non è un numero primo maggiore di $2$":

$$
\overline{\overline{\text{prime}(x) \land x > 2}}
$$

Domanda: è vero che $x$ non è dispari? In simboli:
$$
\overline{\text{odd}(x)}
$$

Come facciamo a rispondere a questa domanda?

Procedimento:
1. Astraiamo dal significato vero e proprio delle proposizioni
2. Concentriamoci sulla struttura logica delle proposizioni:
	1. Introduciamo variabili proposizionali:
$$
\begin{array}{}
A := \text{prime}(x) \land x > 2 \\
B := \text{odd}(x)
\end{array}
$$
	2. Riformuliamo il problema: "Possono le tre proposizioni logiche $A \implies B$, $\overline{\overline A}$ e $\overline B$ reggere?"
		Cioè:
		$$
		A \implies B \land \overline{\overline A} \land \overline B \overset{?}{=} TRUE
		$$

## 2.1 - Soluzione model-teorica/combinatoria

Esaminiamo tutte le possibili combinazioni:

[Tabella]

Non c'è un valore di verità che soddisfa tutte le formule proposizionali in una sola volta, quindi:
- il problema non ha un modello
- il problema è insoddisfacibile

## 2.2 - Soluzione deduttiva/proof-theoretic

$$
\dfrac{
	\quad 
	\overline B
}{

}
$$

Questa derivazione ha:
- Delle assunzioni di partenza:
- Delle regole:
- Una conclusione: falso

Quindi \notB non può essere compatibile con \not\notA e $A \implies B$.

# 3 - Esempio 2

---

> [!fonti]+ Fonti
> 
> - 🏫 Corso di Laurea in Informatica (`L-31 R`) presso l'Università di Torino:
>     - Corso di _Logica per l'Informatica_, A.A. 2025-26 ([pagina Moodle](https://informatica.i-learn.unito.it/course/view.php?id=3477)):
> 		- Prof. Roversi Luca, slide del corso:
> 			- [_Organizzazione_](https://drive.google.com/file/d/1NB1splxyYTw1GnMoiHo942Svh7FN_doG/view)
> 			- [_Preludio_](https://drive.google.com/file/d/1az-Yi3Ab2Yz0rZ73Y61nM_0MsA2M4xSB/view)
> 		- Prof. Roversi Luca, videoregistrazioni del corso:
> 			- [_Organizzazione_](https://unito.webex.com/recordingservice/sites/unito/recording/fffcc1f681f149809e0c48ee29be0e9b/playback)
> 			- [_Preludio 1_](https://unito.webex.com/webappng/sites/unito/recording/3feaf6f9387e483696f09caa72ed4436/playback)
> 			- [_Preludio 2_](https://unito.webex.com/webappng/sites/unito/recording/a16673f51b294b348c593a17b9fed751/playback)
> 			- [_Preludio 3_](https://unito.webex.com/webappng/sites/unito/recording/259fa0424c5745899c677febee0f3fd3/playback)
