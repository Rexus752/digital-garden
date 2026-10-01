---
aliases:
  - Teoria dei linguaggi formali
---

> [!premessa]+ Premessa
> 
> Ciao! Se è la prima volta che capiti su questo sito, ti consiglio di consultare la [pagina principale](index.md) di questo cosiddetto _Giardino Digitale_ per scoprire meglio cos'è e come navigarlo.
> 
> Lo stato di questa nota è al momento: 🟡 <font color="#FFFF7F">_Incompleta_</font>.

%% 
https://it.wikipedia.org/wiki/Teoria_dei_linguaggi_formali
%%

---

%% 
Introduzione: spiegare come esistono linguaggi "artificiali" (?) contrapposti a quelli naturali, tra questi ci sono i linguaggi formali
%%

Quando pensiamo alla parola _linguaggio_, pensiamo normalmente a qualcosa che serve agli esseri umani per comunicare: l'italiano, l'inglese o la lingua dei segni%% link %%. Un _linguaggio_ è quindi un sistema che ci permette di costruire espressioni e di attribuire loro un significato.

Una _lingua naturale_, ossia una di quelle usate nella vita di tutti i giorni (come l'italiano), è estremamente complessa: non comprende soltanto un insieme di parole, ma anche regole grammaticali, eccezioni, ambiguità, contesto, significati impliciti e moltissimi altri fenomeni.

Per esempio, una persona capisce immediatamente che

> Il gatto mangia il topo.

è una frase grammaticalmente ben formata, mentre

> Gatto il topo mangia il.

non lo è.

Un essere umano può leggere una frase e utilizzare la propria conoscenza linguistica per stabilire se abbia senso. Un [computer](Informatica.md#^definizione-computer), invece, non possiede intuitivamente il concetto di "frase corretta". Se vogliamo che possa elaborare un linguaggio, dobbiamo fornirgli una descrizione precisa e non ambigua delle sue regole, in modo che sia possibile stabilire _meccanicamente_ quali espressioni sono ammesse e quali no.

È proprio da questa idea che nasce la [_teoria dei linguaggi formali_](Matematica/Teoria%20dei%20linguaggi%20formali/Teoria%20dehi%20linguaggi%20formali.md#^definizione-teoria-dei-linguaggi-formali), in cui il termine _formale_ indica qualcosa che è stabilito da regole oggettive e ben chiare, non soggette a possibili interpretazioni come nel caso dei _linguaggi naturali_.

> [!definizione]+ Definizione: teoria dei linguaggi formali
> 
> La **teoria dei linguaggi formali** è un ramo della matematica applicata%% link a "matematica applicata" %% che studia i [linguaggi formali](Matematica/Teoria%20dei%20linguaggi%20formali/Teoria%20dehi%20linguaggi%20formali.md#^definizione-linguaggio-formale) e le loro proprietà%% link %%, utili in logica%% link %%, [informatica](Informatica.md#^definizione-informatica) e linguistica%% link %%.
^definizione-teoria-dei-linguaggi-formali

# 1 - Introduzione ai linguaggi formali

Così come per i linguaggi naturali alla base di tutto ci sono le lettere dell'alfabeto con cui costruiamo le parole, anche i linguaggi formali hanno alla propria base i [_simboli_](Matematica/Teoria%20dei%20linguaggi%20formali/Teoria%20dehi%20linguaggi%20formali.md#^definizione-simbolo) di un [_alfabeto_](Matematica/Teoria%20dei%20linguaggi%20formali/Teoria%20dehi%20linguaggi%20formali.md#^definizione-alfabeto) con cui possiamo costruire [stringhe](Matematica/Teoria%20dei%20linguaggi%20formali/Teoria%20dehi%20linguaggi%20formali.md#^definizione-stringa).

Partiamo quindi da questi concetti fondamentali per arrivare pian piano alla definizione di [_linguaggio formale_](Matematica/Teoria%20dei%20linguaggi%20formali/Teoria%20dehi%20linguaggi%20formali.md#^definizione-linguaggio-formale).

## 1.1 - Simboli e alfabeti

> [!definizione]+ Definizione: simbolo
> 
> Un **simbolo** (o **carattere**) è un oggetto matematico%% link a "oggetti matematici" %% considerato come un'unità indivisibile all'interno di un [linguaggio formale](Matematica/Teoria%20dei%20linguaggi%20formali/Teoria%20dehi%20linguaggi%20formali.md#^definizione-linguaggio-formale).
^definizione-simbolo

> [!esempio]- Esempi di simboli
> 
> Un [simbolo](Matematica/Teoria%20dei%20linguaggi%20formali/Teoria%20dehi%20linguaggi%20formali.md#^definizione-simbolo) può essere qualsiasi cosa vogliamo: i [simboli](Matematica/Teoria%20dei%20linguaggi%20formali/Teoria%20dehi%20linguaggi%20formali.md#^definizione-simbolo) più intuibili sono per esempio le lettere minuscole e maiuscole dell'alfabeto latino $\text{a}, \text{b}, \ldots, \text{z}, \text{A}, \text{B}, \ldots, \text{Z}$ o le cifre decimali $0,1,\ldots,9$.
> 
> I [simboli](Matematica/Teoria%20dei%20linguaggi%20formali/Teoria%20dehi%20linguaggi%20formali.md#^definizione-simbolo) però possono essere anche altri tipi di caratteri, come il trattino basso $\text{\_}$ o anche figure geometriche come $\triangle$ e $\square$ e, perché no, anche intere parole stesse possono essere considerate come [simboli](Matematica/Teoria%20dei%20linguaggi%20formali/Teoria%20dehi%20linguaggi%20formali.md#^definizione-simbolo), per esempio le parole chiave%% link %% $\texttt{if}$ e $\tt while$.

> [!definizione]+ Definizione: alfabeto
> 
> Un **alfabeto**, denotato solitamente con $\Sigma$, è un [insieme](Teoria%20degli%20insiemi.md#^definizione-insieme) finito%% link %% e non [vuoto](Teoria%20degli%20insiemi.md#^definizione-insieme-vuoto) di [simboli](Matematica/Teoria%20dei%20linguaggi%20formali/Teoria%20dehi%20linguaggi%20formali.md#^definizione-simbolo).
^definizione-alfabeto

> [!esempio]- Esempi di alfabeti
> 
> Ecco un po' di esempi di [alfabeti](Matematica/Teoria%20dei%20linguaggi%20formali/Teoria%20dehi%20linguaggi%20formali.md#^definizione-alfabeto):
> - $\Sigma_1 = \{ 0,1 \}$ è l'[alfabeto](Matematica/Teoria%20dei%20linguaggi%20formali/Teoria%20dehi%20linguaggi%20formali.md#^definizione-alfabeto) delle cifre binarie, i cui unici [simboli](Matematica/Teoria%20dei%20linguaggi%20formali/Teoria%20dehi%20linguaggi%20formali.md#^definizione-simbolo) sono $0$ e $1$.
> - $\Sigma_2 = \{ 0,1,\ldots,9 \}$ è l'[alfabeto](Matematica/Teoria%20dei%20linguaggi%20formali/Teoria%20dehi%20linguaggi%20formali.md#^definizione-alfabeto) delle cifre decimali.
> - $\Sigma_3 = \{ \text{a}, \text{b}, \ldots, \text{z}, \text{A}, \text{B}, \ldots, \text{Z} \}$ è l'[alfabeto](Matematica/Teoria%20dei%20linguaggi%20formali/Teoria%20dehi%20linguaggi%20formali.md#^definizione-alfabeto) latino.
> 
> Ricordiamo che gli [alfabeti](Matematica/Teoria%20dei%20linguaggi%20formali/Teoria%20dehi%20linguaggi%20formali.md#^definizione-alfabeto) sono a tutti gli effetti degli [insiemi](Teoria%20degli%20insiemi.md#^definizione-insieme), quindi possiamo farci delle operazioni%% link %%, come per esempio l'[unione](Teoria%20degli%20insiemi.md#^definizione-unione-di-due-insiemi). Abbiamo quindi che
> 
> $$
> \begin{align*}
> \Sigma_4 &= \Sigma_2 \cup \{ \text{\ ,\ } \} \\
> &= \{ 0,1,\ldots, 9 \} \cup \{ \text{\ ,\ } \}
> \end{align*}
> $$
> 
> è l'[alfabeto](Matematica/Teoria%20dei%20linguaggi%20formali/Teoria%20dehi%20linguaggi%20formali.md#^definizione-alfabeto) che possiamo usare per rappresentare i numeri con la virgola, oppure
> 
> $$
> \begin{align*}
> \Sigma_5 &= \Sigma_2 \cup \Sigma_3 \cup \{ \_ \}
> \end{align*}
> $$
> 
> è l'[alfabeto](Matematica/Teoria%20dei%20linguaggi%20formali/Teoria%20dehi%20linguaggi%20formali.md#^definizione-alfabeto) che possiamo usare per gli identificatori%% link %% in C%% link %%.

## 1.2 - Stringhe

Gli [alfabeti](Matematica/Teoria%20dei%20linguaggi%20formali/Teoria%20dehi%20linguaggi%20formali.md#^definizione-alfabeto) possono essere usati per creare [_stringhe_](Matematica/Teoria%20dei%20linguaggi%20formali/Teoria%20dehi%20linguaggi%20formali.md#^definizione-stringa).

> [!definizione]+ Definizione: stringa
> 
> Una **stringa** (o **parola** o **frase**) su un [alfabeto](Matematica/Teoria%20dei%20linguaggi%20formali/Teoria%20dehi%20linguaggi%20formali.md#^definizione-alfabeto) $\Sigma$ è una sequenza%% link %% finita%% link %% di [simboli](Matematica/Teoria%20dei%20linguaggi%20formali/Teoria%20dehi%20linguaggi%20formali.md#^definizione-simbolo) in $\Sigma$.
^definizione-stringa

Una [stringa](Matematica/Teoria%20dei%20linguaggi%20formali/Teoria%20dehi%20linguaggi%20formali.md#^definizione-stringa) particolare è quella [_vuota_](Matematica/Teoria%20dei%20linguaggi%20formali/Teoria%20dehi%20linguaggi%20formali.md#^definizione-stringa-vuota).

> [!definizione]+ Definizione: stringa vuota
> 
> La **stringa vuota**, solitamente denotata con $\varepsilon$, è la [stringa](Matematica/Teoria%20dei%20linguaggi%20formali/Teoria%20dehi%20linguaggi%20formali.md#^definizione-stringa) composta da zero [simboli](Matematica/Teoria%20dei%20linguaggi%20formali/Teoria%20dehi%20linguaggi%20formali.md#^definizione-simbolo).
^definizione-stringa-vuota

### 1.2.1 - Operazioni e nozioni sulle stringhe

> [!definizione]+ Definizione: stringhe uguali
> 
> Due [stringhe](Matematica/Teoria%20dei%20linguaggi%20formali/Teoria%20dehi%20linguaggi%20formali.md#^definizione-stringa) si dicono **uguali** se e solo se sono composte dagli stessi [simboli](Matematica/Teoria%20dei%20linguaggi%20formali/Teoria%20dehi%20linguaggi%20formali.md#^definizione-simbolo) nello stesso ordine.
^definizione-stringhe-uguali

> [!esempio]- Esempio di stringhe non uguali
> 
> Per esempio, le [stringhe](Matematica/Teoria%20dei%20linguaggi%20formali/Teoria%20dehi%20linguaggi%20formali.md#^definizione-stringa) $\text{caos}$ e $\text{caso}$ **non** sono [uguali](Matematica/Teoria%20dei%20linguaggi%20formali/Teoria%20dehi%20linguaggi%20formali.md#^definizione-stringhe-uguali) perché, anche se composte dagli stessi [simboli](Matematica/Teoria%20dei%20linguaggi%20formali/Teoria%20dehi%20linguaggi%20formali.md#^definizione-simbolo), essi non compaiono nello stesso ordine.

> [!definizione]+ Definizione: lunghezza di una stringa
> 
> Data una [stringa](Matematica/Teoria%20dei%20linguaggi%20formali/Teoria%20dehi%20linguaggi%20formali.md#^definizione-stringa) $u$, la sua **lunghezza** $|u|$ è il numero di [simboli](Matematica/Teoria%20dei%20linguaggi%20formali/Teoria%20dehi%20linguaggi%20formali.md#^definizione-simbolo) di cui è costituita.
^definizione-lunghezza-di-una-stringa

> [!esempio]- Esempi di lunghezze di stringhe
> 
> Abbiamo per esempio che la [stringa](Matematica/Teoria%20dei%20linguaggi%20formali/Teoria%20dehi%20linguaggi%20formali.md#^definizione-stringa) $\text{aab}$ ha [lunghezza](Matematica/Teoria%20dei%20linguaggi%20formali/Teoria%20dehi%20linguaggi%20formali.md#^definizione-lunghezza-di-una-stringa) $|\text{aab}| = 3$, mentre la [stringa vuota](Matematica/Teoria%20dei%20linguaggi%20formali/Teoria%20dehi%20linguaggi%20formali.md#^definizione-stringa) $\varepsilon$ ha [lunghezza](Matematica/Teoria%20dei%20linguaggi%20formali/Teoria%20dehi%20linguaggi%20formali.md#^definizione-lunghezza-di-una-stringa) $|\varepsilon| = 0$.

> [!definizione]+ Definizione: concatenazione di stringhe
> 
> Date due [stringhe](Matematica/Teoria%20dei%20linguaggi%20formali/Teoria%20dehi%20linguaggi%20formali.md#^definizione-stringa) $u$ e $v$, la loro **concatenazione** $uv$ è la [stringa](Matematica/Teoria%20dei%20linguaggi%20formali/Teoria%20dehi%20linguaggi%20formali.md#^definizione-stringa) ottenuta giustapponendo i [simboli](Matematica/Teoria%20dei%20linguaggi%20formali/Teoria%20dehi%20linguaggi%20formali.md#^definizione-simbolo) di $u$ seguiti dai [simboli](Matematica/Teoria%20dei%20linguaggi%20formali/Teoria%20dehi%20linguaggi%20formali.md#^definizione-simbolo) di $v$.
^definizione-concatenazione-di-stringhe

> [!esempio]- Esempio di concatenazione di stringhe
> 
> Date le [stringhe](Matematica/Teoria%20dei%20linguaggi%20formali/Teoria%20dehi%20linguaggi%20formali.md#^definizione-stringa) $u=\text{po}$ e $v=\text{sta}$, la loro [concatenazione](Matematica/Teoria%20dei%20linguaggi%20formali/Teoria%20dehi%20linguaggi%20formali.md#^definizione-concatenazione-di-stringhe) $uv$ è $\text{posta}$.

> [!proprieta]+ Proprietà: neutralità della concatenazione rispetto alla stringa vuota
> 
> La [stringa vuota](Matematica/Teoria%20dei%20linguaggi%20formali/Teoria%20dehi%20linguaggi%20formali.md#^definizione-stringa-vuota) $\varepsilon$ è l'elemento neutro%% link %% della [concatenazione](Matematica/Teoria%20dei%20linguaggi%20formali/Teoria%20dehi%20linguaggi%20formali.md#^definizione-concatenazione-di-stringhe): infatti, presa una qualsiasi [stringa](Matematica/Teoria%20dei%20linguaggi%20formali/Teoria%20dehi%20linguaggi%20formali.md#^definizione-stringa) $u$, la loro [concatenazione](Matematica/Teoria%20dei%20linguaggi%20formali/Teoria%20dehi%20linguaggi%20formali.md#^definizione-concatenazione-di-stringhe) $u\varepsilon$ o $\varepsilon u$ produce sempre $u$.
^proprieta-neutralita-della-concatenazione-rispetto-alla-stringa-vuota

> [!proprieta]+ Proprietà: associatività della concatenazione
> 
> La [concatenazione](Matematica/Teoria%20dei%20linguaggi%20formali/Teoria%20dehi%20linguaggi%20formali.md#^definizione-concatenazione-di-stringhe) è associativa%% link %%, cioè date tre [stringhe](Matematica/Teoria%20dei%20linguaggi%20formali/Teoria%20dehi%20linguaggi%20formali.md#^definizione-stringa) $u$, $v$ e $w$ vale
> 
> $$
> u(vw) = (uv)w
> $$

> [!osservazione]+ Osservazione: non commutatività della concatenazione
> 
> La [concatenazione](Matematica/Teoria%20dei%20linguaggi%20formali/Teoria%20dehi%20linguaggi%20formali.md#^definizione-concatenazione-di-stringhe) **non** è commutativa%% link %%, infatti date due [stringhe](Matematica/Teoria%20dei%20linguaggi%20formali/Teoria%20dehi%20linguaggi%20formali.md#^definizione-stringa) $u$ e $v$ abbiamo che genericamente
> 
> $$
> uv \ne vu
> $$
> 
> eccetto nel caso in cui almeno una delle due è la [stringa vuota](Matematica/Teoria%20dei%20linguaggi%20formali/Teoria%20dehi%20linguaggi%20formali.md#^definizione-stringa-vuota) $\varepsilon$ (perché [è l'elemento neutro della concatenazione](Matematica/Teoria%20dei%20linguaggi%20formali/Teoria%20dehi%20linguaggi%20formali.md#^proprieta-neutralita-della-concatenazione-rispetto-alla-stringa-vuota)) o in cui le due [stringhe](Matematica/Teoria%20dei%20linguaggi%20formali/Teoria%20dehi%20linguaggi%20formali.md#^definizione-stringa) sono [uguali](Matematica/Teoria%20dei%20linguaggi%20formali/Teoria%20dehi%20linguaggi%20formali.md#^definizione-stringhe-uguali).

> [!definizione]+ Definizione: prefisso di una stringa
> 
> Date due [stringhe](Matematica/Teoria%20dei%20linguaggi%20formali/Teoria%20dehi%20linguaggi%20formali.md#^definizione-stringa) $u$ e $w$, diciamo che $u$ è un **prefisso** di $w$ se esiste una terza [stringa](Matematica/Teoria%20dei%20linguaggi%20formali/Teoria%20dehi%20linguaggi%20formali.md#^definizione-stringa) $v$ tale che $w = uv$.
^definizione-prefisso-di-una-stringa

> [!definizione]+ Definizione: suffisso di una stringa
> 
> Date due [stringhe](Matematica/Teoria%20dei%20linguaggi%20formali/Teoria%20dehi%20linguaggi%20formali.md#^definizione-stringa) $u$ e $w$, diciamo che $u$ è un **suffisso** di $w$ se esiste una terza [stringa](Matematica/Teoria%20dei%20linguaggi%20formali/Teoria%20dehi%20linguaggi%20formali.md#^definizione-stringa) $v$ tale che $w = vu$.
^definizione-suffisso-di-una-stringa

> [!esempio]- Esempio di prefisso e suffisso di una stringa
> 
> Date le [stringhe](Matematica/Teoria%20dei%20linguaggi%20formali/Teoria%20dehi%20linguaggi%20formali.md#^definizione-stringa) $u = \text{posta}$ e $w =\text{postazione}$, abbiamo che $u$ è un [prefisso](Matematica/Teoria%20dei%20linguaggi%20formali/Teoria%20dehi%20linguaggi%20formali.md#^definizione-prefisso-di-una-stringa) di $w$ perché esiste la [stringa](Matematica/Teoria%20dei%20linguaggi%20formali/Teoria%20dehi%20linguaggi%20formali.md#^definizione-stringa) $v =\text{zione}$ tale che $uv = w = \text{postazione}$.
> 
> Allo stesso modo, date le [stringhe](Matematica/Teoria%20dei%20linguaggi%20formali/Teoria%20dehi%20linguaggi%20formali.md#^definizione-stringa) $u=\text{vero}$ e $w=\text{papavero}$, abbiamo che $u$ è un [suffisso](Matematica/Teoria%20dei%20linguaggi%20formali/Teoria%20dehi%20linguaggi%20formali.md#^definizione-suffisso-di-una-stringa) di $w$ perché esiste la [stringa](Matematica/Teoria%20dei%20linguaggi%20formali/Teoria%20dehi%20linguaggi%20formali.md#^definizione-stringa) $v =\text{vero}$ tale che $vu = w = \text{papavero}$.

> [!osservazione]+ Osservazione: una stringa è prefisso e suffisso di se stessa
> 
> Data una [stringa](Matematica/Teoria%20dei%20linguaggi%20formali/Teoria%20dehi%20linguaggi%20formali.md#^definizione-stringa) $u$, essa è contemporaneamente sia [prefisso](Matematica/Teoria%20dei%20linguaggi%20formali/Teoria%20dehi%20linguaggi%20formali.md#^definizione-prefisso-di-una-stringa) che [suffisso](Matematica/Teoria%20dei%20linguaggi%20formali/Teoria%20dehi%20linguaggi%20formali.md#^definizione-suffisso-di-una-stringa) di se stessa perché esiste la [stringa vuota](Matematica/Teoria%20dei%20linguaggi%20formali/Teoria%20dehi%20linguaggi%20formali.md#^definizione-stringa-vuota) $\varepsilon$ per cui $u\varepsilon =u$ (nel caso del [prefisso](Matematica/Teoria%20dei%20linguaggi%20formali/Teoria%20dehi%20linguaggi%20formali.md#^definizione-prefisso-di-una-stringa)) e $\varepsilon u = u$ (nel caso del [suffisso](Matematica/Teoria%20dei%20linguaggi%20formali/Teoria%20dehi%20linguaggi%20formali.md#^definizione-suffisso-di-una-stringa)).

> [!definizione]+ Definizione: inversa di una stringa
> 
> Data una [stringa](Matematica/Teoria%20dei%20linguaggi%20formali/Teoria%20dehi%20linguaggi%20formali.md#^definizione-stringa) $u = a_1a_2\ldots a_n$, la sua **inversa** $u^R$ è la [stringa](Matematica/Teoria%20dei%20linguaggi%20formali/Teoria%20dehi%20linguaggi%20formali.md#^definizione-stringa) ottenuta invertendo l'ordine dei [simboli](Matematica/Teoria%20dei%20linguaggi%20formali/Teoria%20dehi%20linguaggi%20formali.md#^definizione-simbolo) $a_1,a_2,\ldots,a_n$ di $u$:
> 
> $$
> u^R = a_n\ldots a_2a_1
> $$
^definizione-inversa-di-una-stringa

> [!esempio]- Esempio di inversa di una stringa
> 
> Data la [stringa](Matematica/Teoria%20dei%20linguaggi%20formali/Teoria%20dehi%20linguaggi%20formali.md#^definizione-stringa) $a = \text{casa}$, la sua [inversa](Matematica/Teoria%20dei%20linguaggi%20formali/Teoria%20dehi%20linguaggi%20formali.md#^definizione-inversa-di-una-stringa) è $a^R=\text{asac}$.

> [!definizione]+ Definizione: stringa palindroma
> 
> Una [stringa](Matematica/Teoria%20dei%20linguaggi%20formali/Teoria%20dehi%20linguaggi%20formali.md#^definizione-stringa) $u$ è **palindroma** se è [uguale](Matematica/Teoria%20dei%20linguaggi%20formali/Teoria%20dehi%20linguaggi%20formali.md#^definizione-stringhe-uguali) alla sua [inversa](Matematica/Teoria%20dei%20linguaggi%20formali/Teoria%20dehi%20linguaggi%20formali.md#^definizione-inversa-di-una-stringa) $u^R$.
^definizione-stringa-palindroma

> [!esempio]- Esempi di stringhe palindrome
> 
> Un esempio di [stringa palindroma](Matematica/Teoria%20dei%20linguaggi%20formali/Teoria%20dehi%20linguaggi%20formali.md#^definizione-stringa-palindroma) è $u=\text{radar}$, la cui [inversa](Matematica/Teoria%20dei%20linguaggi%20formali/Teoria%20dehi%20linguaggi%20formali.md#^definizione-inversa-di-una-stringa) $u^R$ è sempre $\text{radar}$. Anche la [stringa vuota](Matematica/Teoria%20dei%20linguaggi%20formali/Teoria%20dehi%20linguaggi%20formali.md#^definizione-stringa-vuota) $\varepsilon$ è considerata [palindroma](Matematica/Teoria%20dei%20linguaggi%20formali/Teoria%20dehi%20linguaggi%20formali.md#^definizione-stringa-palindroma).

> [!definizione]+ Definizione: potenza $\color{#FF7FFF} n$-esima di una stringa
> 
> Data una [stringa](Matematica/Teoria%20dei%20linguaggi%20formali/Teoria%20dehi%20linguaggi%20formali.md#^definizione-stringa) $u$, la sua **potenza $n$-esima** $u^n$ è la [stringa](Matematica/Teoria%20dei%20linguaggi%20formali/Teoria%20dehi%20linguaggi%20formali.md#^definizione-stringa) ottenuta [concatenando](Matematica/Teoria%20dei%20linguaggi%20formali/Teoria%20dehi%20linguaggi%20formali.md#^definizione-concatenazione-di-stringhe) $u$ per $n$ volte, ossia
> 
> $$
> u^n = \underbrace{uu\ldots u}_{n \text{ volte}}
> $$
> 
> In particolare, $u^0 = \varepsilon$ e $u^1 = u$.
^definzione-potenza-n-esima-di-una-stringa

## 1.3 - Linguaggi formali

Ora possiamo finalmente definire cos'è un [_linguaggio formale_](Matematica/Teoria%20dei%20linguaggi%20formali/Teoria%20dehi%20linguaggi%20formali.md#^definizione-linguaggio-formale).

> [!definizione]+ Definizione: linguaggio formale
> 
> Un **linguaggio formale** (o più semplicemente **linguaggio**) $L$ su un [alfabeto](Matematica/Teoria%20dei%20linguaggi%20formali/Teoria%20dehi%20linguaggi%20formali.md#^definizione-alfabeto) $\Sigma$ è un qualunque [insieme](Teoria%20degli%20insiemi.md#^definizione-insieme) di [stringhe](Matematica/Teoria%20dei%20linguaggi%20formali/Teoria%20dehi%20linguaggi%20formali.md#^definizione-stringa) su $\Sigma$.
^definizione-linguaggio-formale

> [!esempio]- Esempi di linguaggi formali
> 
> Dato l'[alfabeto](Matematica/Teoria%20dei%20linguaggi%20formali/Teoria%20dehi%20linguaggi%20formali.md#^definizione-alfabeto) $\Sigma = \{ 0,1 \}$ delle cifre binarie, un possibile [linguaggio formale](Matematica/Teoria%20dei%20linguaggi%20formali/Teoria%20dehi%20linguaggi%20formali.md#^definizione-linguaggio-formale) $L$ su $\Sigma$ è
> 
> $$
> \{ \varepsilon, 1, 01, 100, 1010111, \ldots \}
> $$

---

> [!fonti]+ Fonti
> 
> - 🏫 Corso di Laurea in Informatica (`L-31 R`) presso l'Università di Torino:
>     - Corso di _Linguaggi Formali e Traduttori_, A.A. 2026-27 ([pagina Moodle](https://informatica.i-learn.unito.it/course/view.php?id=3735)):
> 		- Prof. Jeremy James Sproston, slide del corso:
> 			- [1.3 - _Linguaggi_](https://informatica.i-learn.unito.it/pluginfile.php/510313/mod_folder/content/0/1-3_linguaggi.pdf).
