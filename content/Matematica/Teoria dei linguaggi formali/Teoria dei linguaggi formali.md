---
aliases:
  - Teoria dei linguaggi formali
---

> [!premessa]+ Premessa
> 
> Ciao! Se è la prima volta che capiti su questo sito, ti consiglio di consultare la [pagina principale](index.md) di questo _Giardino Digitale_ per scoprire meglio cos'è e come navigarlo.
> 
> Lo stato di questa nota è al momento: 🟡 <font color="#FFFF7F">_Incompleta_</font>.

%% 
https://it.wikipedia.org/wiki/Teoria_dei_linguaggi_formali
%%

---

Quando pensiamo alla parola _linguaggio_, pensiamo normalmente a qualcosa che serve agli esseri umani per comunicare: l'italiano, l'inglese o la lingua dei segni%% link %%. Un _linguaggio_ è quindi un sistema che ci permette di costruire espressioni e di attribuire loro un significato.

Una _lingua naturale_, ossia una di quelle usate nella vita di tutti i giorni (come l'italiano), è estremamente complessa: non comprende soltanto un insieme di parole, ma anche regole grammaticali, eccezioni, ambiguità, contesto, significati impliciti e moltissimi altri fenomeni.

Per esempio, una persona capisce immediatamente che

> Il gatto mangia il topo.

è una frase grammaticalmente ben formata, mentre

> Gatto il topo mangia il.

non lo è.

Un essere umano può leggere una frase e utilizzare la propria conoscenza linguistica per stabilire se abbia senso. Un [computer](Informatica.md#^definizione-computer), invece, non possiede intuitivamente il concetto di "frase corretta". Se vogliamo che possa elaborare un linguaggio, dobbiamo fornirgli una descrizione precisa e non ambigua delle sue regole, in modo che sia possibile stabilire _meccanicamente_ quali espressioni sono ammesse e quali no.

È proprio da questa idea che nasce la [_teoria dei linguaggi formali_](Teoria%20dei%20linguaggi%20formali.md#^definizione-teoria-dei-linguaggi-formali), in cui il termine _formale_ indica qualcosa che è stabilito da regole oggettive e ben chiare, non soggette a possibili interpretazioni come nel caso dei _linguaggi naturali_.

> [!definizione]+ Definizione: teoria dei linguaggi formali
> 
> La **teoria dei linguaggi formali** è un ramo della matematica applicata%% link a "matematica applicata" %% che studia i [linguaggi formali](Teoria%20dei%20linguaggi%20formali.md#^definizione-linguaggio-formale) e le loro proprietà%% link %%, utili in logica%% link %%, [informatica](Informatica.md#^definizione-informatica) e linguistica%% link %%.
^definizione-teoria-dei-linguaggi-formali

# 1 - Introduzione ai linguaggi formali

Così come per i linguaggi naturali alla base di tutto ci sono le lettere dell'alfabeto con cui costruiamo le parole, anche i linguaggi formali hanno alla propria base i [_simboli_](Teoria%20dei%20linguaggi%20formali.md#^definizione-simbolo) di un [_alfabeto_](Teoria%20dei%20linguaggi%20formali.md#^definizione-alfabeto) con cui possiamo costruire [stringhe](Teoria%20dei%20linguaggi%20formali.md#^definizione-stringa).

Partiamo quindi da questi concetti fondamentali per arrivare pian piano alla definizione di [_linguaggio formale_](Teoria%20dei%20linguaggi%20formali.md#^definizione-linguaggio-formale).

## 1.1 - Simboli e alfabeti

> [!definizione]+ Definizione: simbolo
> 
> Un **simbolo** (o **carattere**) è un oggetto matematico%% link a "oggetti matematici" %% considerato come un'unità indivisibile all'interno di un [linguaggio formale](Teoria%20dei%20linguaggi%20formali.md#^definizione-linguaggio-formale).
^definizione-simbolo

> [!esempio]- Esempi di simboli
> 
> Un [simbolo](Teoria%20dei%20linguaggi%20formali.md#^definizione-simbolo) può essere qualsiasi cosa vogliamo: i [simboli](Teoria%20dei%20linguaggi%20formali.md#^definizione-simbolo) più intuibili sono per esempio le lettere minuscole e maiuscole dell'alfabeto latino $\text{a}, \text{b}, \ldots, \text{z}, \text{A}, \text{B}, \ldots, \text{Z}$ o le cifre decimali $0,1,\ldots,9$.
> 
> I [simboli](Teoria%20dei%20linguaggi%20formali.md#^definizione-simbolo) però possono essere anche altri tipi di caratteri, come il trattino basso $\text{\_}$ o anche figure geometriche come $\triangle$ e $\square$ e, perché no, anche intere parole stesse possono essere considerate come [simboli](Teoria%20dei%20linguaggi%20formali.md#^definizione-simbolo), per esempio le parole chiave%% link %% $\texttt{if}$ e $\tt while$.

> [!definizione]+ Definizione: alfabeto
> 
> Un **alfabeto**, denotato solitamente con $\Sigma$, è un [insieme](Teoria%20degli%20insiemi.md#^definizione-insieme) finito%% link %% e non [vuoto](Teoria%20degli%20insiemi.md#^definizione-insieme-vuoto) di [simboli](Teoria%20dei%20linguaggi%20formali.md#^definizione-simbolo).
^definizione-alfabeto

> [!esempio]- Esempi di alfabeti
> 
> Ecco un po' di esempi di [alfabeti](Teoria%20dei%20linguaggi%20formali.md#^definizione-alfabeto):
> - $\Sigma_1 = \{ 0,1 \}$ è l'[alfabeto](Teoria%20dei%20linguaggi%20formali.md#^definizione-alfabeto) delle cifre binarie, i cui unici [simboli](Teoria%20dei%20linguaggi%20formali.md#^definizione-simbolo) sono $0$ e $1$.
> - $\Sigma_2 = \{ 0,1,\ldots,9 \}$ è l'[alfabeto](Teoria%20dei%20linguaggi%20formali.md#^definizione-alfabeto) delle cifre decimali.
> - $\Sigma_3 = \{ \text{a}, \text{b}, \ldots, \text{z}, \text{A}, \text{B}, \ldots, \text{Z} \}$ è l'[alfabeto](Teoria%20dei%20linguaggi%20formali.md#^definizione-alfabeto) latino.
> 
> Ricordiamo che gli [alfabeti](Teoria%20dei%20linguaggi%20formali.md#^definizione-alfabeto) sono a tutti gli effetti degli [insiemi](Teoria%20degli%20insiemi.md#^definizione-insieme), quindi possiamo farci delle operazioni%% link %%, come per esempio l'[unione](Teoria%20degli%20insiemi.md#^definizione-unione-di-due-insiemi). Abbiamo quindi che
> 
> $$
> \begin{align*}
> \Sigma_4 &= \Sigma_2 \cup \{ \text{\ ,\ } \} \\
> &= \{ 0,1,\ldots, 9 \} \cup \{ \text{\ ,\ } \}
> \end{align*}
> $$
> 
> è l'[alfabeto](Teoria%20dei%20linguaggi%20formali.md#^definizione-alfabeto) che possiamo usare per rappresentare i numeri con la virgola, oppure
> 
> $$
> \begin{align*}
> \Sigma_5 &= \Sigma_2 \cup \Sigma_3 \cup \{ \_ \}
> \end{align*}
> $$
> 
> è l'[alfabeto](Teoria%20dei%20linguaggi%20formali.md#^definizione-alfabeto) che possiamo usare per gli identificatori%% link %% in C%% link %%.

## 1.2 - Stringhe

Gli [alfabeti](Teoria%20dei%20linguaggi%20formali.md#^definizione-alfabeto) possono essere usati per creare [_stringhe_](Teoria%20dei%20linguaggi%20formali.md#^definizione-stringa).

> [!definizione]+ Definizione: stringa
> 
> Una **stringa** (o **parola** o **frase**) su un [alfabeto](Teoria%20dei%20linguaggi%20formali.md#^definizione-alfabeto) $\Sigma$ è una sequenza%% link %% finita%% link %% di [simboli](Teoria%20dei%20linguaggi%20formali.md#^definizione-simbolo) in $\Sigma$.
^definizione-stringa

Una [stringa](Teoria%20dei%20linguaggi%20formali.md#^definizione-stringa) particolare è quella [_vuota_](Teoria%20dei%20linguaggi%20formali.md#^definizione-stringa-vuota).

> [!definizione]+ Definizione: stringa vuota
> 
> La **stringa vuota**, solitamente denotata con $\varepsilon$, è la [stringa](Teoria%20dei%20linguaggi%20formali.md#^definizione-stringa) composta da zero [simboli](Teoria%20dei%20linguaggi%20formali.md#^definizione-simbolo).
^definizione-stringa-vuota

### 1.2.1 - Operazioni e nozioni sulle stringhe

> [!definizione]+ Definizione: stringhe uguali
> 
> Due [stringhe](Teoria%20dei%20linguaggi%20formali.md#^definizione-stringa) si dicono **uguali** se e solo se sono composte dagli stessi [simboli](Teoria%20dei%20linguaggi%20formali.md#^definizione-simbolo) nello stesso ordine.
^definizione-stringhe-uguali

> [!esempio]- Esempio di stringhe non uguali
> 
> Per esempio, le [stringhe](Teoria%20dei%20linguaggi%20formali.md#^definizione-stringa) $\text{caos}$ e $\text{caso}$ **non** sono [uguali](Teoria%20dei%20linguaggi%20formali.md#^definizione-stringhe-uguali) perché, anche se composte dagli stessi [simboli](Teoria%20dei%20linguaggi%20formali.md#^definizione-simbolo), essi non compaiono nello stesso ordine.

> [!definizione]+ Definizione: lunghezza di una stringa
> 
> Data una [stringa](Teoria%20dei%20linguaggi%20formali.md#^definizione-stringa) $u$, la sua **lunghezza** $|u|$ è il numero di [simboli](Teoria%20dei%20linguaggi%20formali.md#^definizione-simbolo) di cui è costituita.
^definizione-lunghezza-di-una-stringa

> [!esempio]- Esempi di lunghezze di stringhe
> 
> Abbiamo per esempio che la [stringa](Teoria%20dei%20linguaggi%20formali.md#^definizione-stringa) $\text{aab}$ ha [lunghezza](Teoria%20dei%20linguaggi%20formali.md#^definizione-lunghezza-di-una-stringa) $|\text{aab}| = 3$, mentre la [stringa vuota](Teoria%20dei%20linguaggi%20formali.md#^definizione-stringa) $\varepsilon$ ha [lunghezza](Teoria%20dei%20linguaggi%20formali.md#^definizione-lunghezza-di-una-stringa) $|\varepsilon| = 0$.

> [!definizione]+ Definizione: concatenazione di due stringhe
> 
> Date due [stringhe](Teoria%20dei%20linguaggi%20formali.md#^definizione-stringa) $u$ e $v$, la loro **concatenazione** $uv$ è la [stringa](Teoria%20dei%20linguaggi%20formali.md#^definizione-stringa) ottenuta giustapponendo i [simboli](Teoria%20dei%20linguaggi%20formali.md#^definizione-simbolo) di $u$ seguiti dai [simboli](Teoria%20dei%20linguaggi%20formali.md#^definizione-simbolo) di $v$.
^definizione-concatenazione-di-due-stringhe

> [!esempio]- Esempio di concatenazione di stringhe
> 
> Date le [stringhe](Teoria%20dei%20linguaggi%20formali.md#^definizione-stringa) $u=\text{po}$ e $v=\text{sta}$, la loro [concatenazione](Teoria%20dei%20linguaggi%20formali.md#^definizione-concatenazione-di-due-stringhe) $uv$ è $\text{posta}$.

> [!proprieta]+ Proprietà: neutralità della concatenazione rispetto alla stringa vuota
> 
> La [stringa vuota](Teoria%20dei%20linguaggi%20formali.md#^definizione-stringa-vuota) $\varepsilon$ è l'elemento neutro%% link %% della [concatenazione](Teoria%20dei%20linguaggi%20formali.md#^definizione-concatenazione-di-due-stringhe): infatti, presa una qualsiasi [stringa](Teoria%20dei%20linguaggi%20formali.md#^definizione-stringa) $u$, la loro [concatenazione](Teoria%20dei%20linguaggi%20formali.md#^definizione-concatenazione-di-due-stringhe) $u\varepsilon$ o $\varepsilon u$ produce sempre $u$.
^proprieta-neutralita-della-concatenazione-rispetto-alla-stringa-vuota

> [!proprieta]+ Proprietà: associatività della concatenazione
> 
> La [concatenazione](Teoria%20dei%20linguaggi%20formali.md#^definizione-concatenazione-di-due-stringhe) è associativa%% link %%, cioè date tre [stringhe](Teoria%20dei%20linguaggi%20formali.md#^definizione-stringa) $u$, $v$ e $w$ vale
> 
> $$
> u(vw) = (uv)w
> $$

> [!osservazione]+ Osservazione: non commutatività della concatenazione
> 
> La [concatenazione](Teoria%20dei%20linguaggi%20formali.md#^definizione-concatenazione-di-due-stringhe) **non** è commutativa%% link %%, infatti date due [stringhe](Teoria%20dei%20linguaggi%20formali.md#^definizione-stringa) $u$ e $v$ abbiamo che genericamente
> 
> $$
> uv \ne vu
> $$
> 
> eccetto nel caso in cui almeno una delle due è la [stringa vuota](Teoria%20dei%20linguaggi%20formali.md#^definizione-stringa-vuota) $\varepsilon$ (perché [è l'elemento neutro della concatenazione](Teoria%20dei%20linguaggi%20formali.md#^proprieta-neutralita-della-concatenazione-rispetto-alla-stringa-vuota)) o in cui le due [stringhe](Teoria%20dei%20linguaggi%20formali.md#^definizione-stringa) sono [uguali](Teoria%20dei%20linguaggi%20formali.md#^definizione-stringhe-uguali).

> [!definizione]+ Definizione: prefisso di una stringa
> 
> Date due [stringhe](Teoria%20dei%20linguaggi%20formali.md#^definizione-stringa) $u$ e $w$, diciamo che $u$ è un **prefisso** di $w$ se esiste una terza [stringa](Teoria%20dei%20linguaggi%20formali.md#^definizione-stringa) $v$ tale che $w = uv$.
^definizione-prefisso-di-una-stringa

> [!definizione]+ Definizione: suffisso di una stringa
> 
> Date due [stringhe](Teoria%20dei%20linguaggi%20formali.md#^definizione-stringa) $u$ e $w$, diciamo che $u$ è un **suffisso** di $w$ se esiste una terza [stringa](Teoria%20dei%20linguaggi%20formali.md#^definizione-stringa) $v$ tale che $w = vu$.
^definizione-suffisso-di-una-stringa

> [!esempio]- Esempio di prefisso e suffisso di una stringa
> 
> Date le [stringhe](Teoria%20dei%20linguaggi%20formali.md#^definizione-stringa) $u = \text{posta}$ e $w =\text{postazione}$, abbiamo che $u$ è un [prefisso](Teoria%20dei%20linguaggi%20formali.md#^definizione-prefisso-di-una-stringa) di $w$ perché esiste la [stringa](Teoria%20dei%20linguaggi%20formali.md#^definizione-stringa) $v =\text{zione}$ tale che $uv = w = \text{postazione}$.
> 
> Allo stesso modo, date le [stringhe](Teoria%20dei%20linguaggi%20formali.md#^definizione-stringa) $u=\text{vero}$ e $w=\text{papavero}$, abbiamo che $u$ è un [suffisso](Teoria%20dei%20linguaggi%20formali.md#^definizione-suffisso-di-una-stringa) di $w$ perché esiste la [stringa](Teoria%20dei%20linguaggi%20formali.md#^definizione-stringa) $v =\text{vero}$ tale che $vu = w = \text{papavero}$.

> [!osservazione]+ Osservazione: una stringa è prefisso e suffisso di se stessa
> 
> Data una [stringa](Teoria%20dei%20linguaggi%20formali.md#^definizione-stringa) $u$, essa è contemporaneamente sia [prefisso](Teoria%20dei%20linguaggi%20formali.md#^definizione-prefisso-di-una-stringa) che [suffisso](Teoria%20dei%20linguaggi%20formali.md#^definizione-suffisso-di-una-stringa) di se stessa perché esiste la [stringa vuota](Teoria%20dei%20linguaggi%20formali.md#^definizione-stringa-vuota) $\varepsilon$ per cui $u\varepsilon =u$ (nel caso del [prefisso](Teoria%20dei%20linguaggi%20formali.md#^definizione-prefisso-di-una-stringa)) e $\varepsilon u = u$ (nel caso del [suffisso](Teoria%20dei%20linguaggi%20formali.md#^definizione-suffisso-di-una-stringa)).

> [!definizione]+ Definizione: inversa di una stringa
> 
> Data una [stringa](Teoria%20dei%20linguaggi%20formali.md#^definizione-stringa) $u = a_1a_2\ldots a_n$, la sua **inversa** $u^R$ è la [stringa](Teoria%20dei%20linguaggi%20formali.md#^definizione-stringa) ottenuta invertendo l'ordine dei [simboli](Teoria%20dei%20linguaggi%20formali.md#^definizione-simbolo) $a_1,a_2,\ldots,a_n$ di $u$:
> 
> $$
> u^R = a_n\ldots a_2a_1
> $$
^definizione-inversa-di-una-stringa

> [!esempio]- Esempio di inversa di una stringa
> 
> Data la [stringa](Teoria%20dei%20linguaggi%20formali.md#^definizione-stringa) $a = \text{casa}$, la sua [inversa](Teoria%20dei%20linguaggi%20formali.md#^definizione-inversa-di-una-stringa) è $a^R=\text{asac}$.

> [!definizione]+ Definizione: stringa palindroma
> 
> Una [stringa](Teoria%20dei%20linguaggi%20formali.md#^definizione-stringa) $u$ è **palindroma** se è [uguale](Teoria%20dei%20linguaggi%20formali.md#^definizione-stringhe-uguali) alla sua [inversa](Teoria%20dei%20linguaggi%20formali.md#^definizione-inversa-di-una-stringa) $u^R$.
^definizione-stringa-palindroma

> [!esempio]- Esempi di stringhe palindrome
> 
> Un esempio di [stringa palindroma](Teoria%20dei%20linguaggi%20formali.md#^definizione-stringa-palindroma) è $u=\text{radar}$, la cui [inversa](Teoria%20dei%20linguaggi%20formali.md#^definizione-inversa-di-una-stringa) $u^R$ è sempre $\text{radar}$. Anche la [stringa vuota](Teoria%20dei%20linguaggi%20formali.md#^definizione-stringa-vuota) $\varepsilon$ è considerata [palindroma](Teoria%20dei%20linguaggi%20formali.md#^definizione-stringa-palindroma).

> [!definizione]+ Definizione: potenza $\color{#FF7FFF} n$-esima di una stringa
>
> Data una [stringa](Teoria%20dei%20linguaggi%20formali.md#^definizione-stringa) $u$, la sua **potenza $n$-esima** $u^n$ (con $n \in \mathbb{N}$) è la [stringa](Teoria%20dei%20linguaggi%20formali.md#^definizione-stringa) ottenuta [concatenando](Teoria%20dei%20linguaggi%20formali.md#^definizione-concatenazione-di-due-stringhe) $u$ per $n$ volte:
>
> $$
> u^n = \underbrace{uu\ldots u}_{n \text{ volte}} =
> \begin{cases}
> \varepsilon & \text{se } n = 0 \\
> u^{n-1}u & \text{se } n > 0
> \end{cases}
> $$
> ^definizione-potenza-n-esima-di-una-stringa
^definizione-potenza-n-esima-di-una-stringa

## 1.3 - Linguaggi formali

Ora possiamo finalmente definire cos'è un [_linguaggio formale_](Teoria%20dei%20linguaggi%20formali.md#^definizione-linguaggio-formale).

> [!definizione]+ Definizione: linguaggio formale
> 
> Un **linguaggio formale** (o più semplicemente **linguaggio**) $L$ su un [alfabeto](Teoria%20dei%20linguaggi%20formali.md#^definizione-alfabeto) $\Sigma$ è un qualunque [insieme](Teoria%20degli%20insiemi.md#^definizione-insieme) di [stringhe](Teoria%20dei%20linguaggi%20formali.md#^definizione-stringa) su $\Sigma$.
^definizione-linguaggio-formale

> [!esempio]- Esempi di linguaggi formali
> 
> Dato l'[alfabeto](Teoria%20dei%20linguaggi%20formali.md#^definizione-alfabeto) $\Sigma = \{ 0,1 \}$ delle cifre binarie, un possibile [linguaggio formale](Teoria%20dei%20linguaggi%20formali.md#^definizione-linguaggio-formale) $L$ su $\Sigma$ è
> 
> $$
> \{ \varepsilon, 1, 01, 100, 1010111, \ldots \}
> $$
> 
> Un altro possibile [linguaggio](Teoria%20dei%20linguaggi%20formali.md#^definizione-linguaggio-formale) è $L = \Sigma$, formato unicamente dai [simboli](Teoria%20dei%20linguaggi%20formali.md#^definizione-simbolo) dell'[alfabeto](Teoria%20dei%20linguaggi%20formali.md#^definizione-alfabeto).

> [!notazione]+ Notazione: rappresentazione per caratteristica di un linguaggio
> 
> [Esattamente come avviene per gli insiemi](Teoria%20degli%20insiemi.md#^rappresentazione-per-caratteristica-di-un-insieme), anche i [linguaggi](Teoria%20dei%20linguaggi%20formali.md#^definizione-linguaggio-formale) possono essere rappresentati _per caratteristica_: per esempio,
> 
> $$
> \{ \text{a}^{2n+1} \mid n \in \mathbb{N} \}
> $$
> 
> indica il [linguaggio](Teoria%20dei%20linguaggi%20formali.md#^definizione-linguaggio-formale) composto dalle [stringhe](Teoria%20dei%20linguaggi%20formali.md#^definizione-stringa) di $\text{a}$ di [lunghezza](Teoria%20dei%20linguaggi%20formali.md#^definizione-lunghezza-di-una-stringa) dispari, oppure
> 
> $$
> \{ \text{a}^m\text{b}^n  \mid m,n \in \mathbb{N} \}
> $$
> 
> indica il [linguaggio](Teoria%20dei%20linguaggi%20formali.md#^definizione-linguaggio-formale) delle [stringhe](Teoria%20dei%20linguaggi%20formali.md#^definizione-stringa) composte da un numero arbitrario di $\text{a}$ seguite da un numero arbitrario di $\text{b}$.

> [!definizione]+ Definizione: linguaggio vuoto
> 
> Il **linguaggio vuoto** $\emptyset$ è un [linguaggio](Teoria%20dei%20linguaggi%20formali.md#^definizione-linguaggio-formale) contenente zero [stringhe](Teoria%20dei%20linguaggi%20formali.md#^definizione-stringa) ed è quindi un [insieme vuoto](Teoria%20degli%20insiemi.md#^definizione-insieme-vuoto).
^definizione-linguaggio-vuoto

> [!attenzione]+ Attenzione: linguaggio vuoto diverso da linguaggio con stringa vuota
> 
> Il [linguaggio vuoto](Teoria%20dei%20linguaggi%20formali.md#^definizione-linguaggio-vuoto), corrispondente a un [insieme vuoto](Teoria%20degli%20insiemi.md#^definizione-insieme-vuoto) $\emptyset$, e un [linguaggio](Teoria%20dei%20linguaggi%20formali.md#^definizione-linguaggio-formale) $L$ composto dalla sola [stringa vuota](Teoria%20dei%20linguaggi%20formali.md#^definizione-stringa-vuota) **non** sono la stessa cosa, perché mentre il primo non ha elementi%% link %%, il secondo ha un solo elemento%% link %% che è $\varepsilon$:
> 
> $$
> \emptyset \ne \{ \varepsilon \}
> $$

### 1.3.1 - Operazioni su linguaggi

> [!osservazione]+ Osservazione: operazioni insiemistiche sui linguaggi
> 
> Dal momento che i [linguaggi](Teoria%20dei%20linguaggi%20formali.md#^definizione-linguaggio-formale) sono [insiemi](Teoria%20degli%20insiemi.md#^definizione-insieme), anche su di essi possono essere applicate le operazioni%% link %% insiemistiche dell'[unione $\cup$](Teoria%20degli%20insiemi.md#^definizione-unione-di-due-insiemi), [intersezione $\cap$](Teoria%20degli%20insiemi.md#^definizione-intersezione-di-due-insiemi) e [differenza $\setminus$](Teoria%20degli%20insiemi.md#^definizione-differenza-tra-due-insiemi).

> [!definizione]+ Definizione: linguaggio inverso
> 
> Dato un [linguaggio](Teoria%20dei%20linguaggi%20formali.md#^definizione-linguaggio-formale) $L$ su un [alfabeto](Teoria%20dei%20linguaggi%20formali.md#^definizione-alfabeto) $\Sigma$, il suo **inverso** $L^R$ è il [linguaggio](Teoria%20dei%20linguaggi%20formali.md#^definizione-linguaggio-formale) ottenuto [invertendo](Teoria%20dei%20linguaggi%20formali.md#^definizione-inversa-di-una-stringa) ogni [stringa](Teoria%20dei%20linguaggi%20formali.md#^definizione-stringa) $w \in L$:
> 
> $$
> L^R = \{ w^R \mid w \in L \}
> $$
^definizione-linguaggio-inverso

> [!definizione]+ Definizione: potenza $\color{#FF7FFF} n$-esima di un alfabeto
> 
> Dato un [alfabeto](Teoria%20dei%20linguaggi%20formali.md#^definizione-alfabeto) $\Sigma$, la sua **potenza $n$-esima** $\Sigma^n$ (con $n\in\mathbb{N}$) è il [linguaggio](Teoria%20dei%20linguaggi%20formali.md#^definizione-linguaggio-formale) costituito da tutte le [stringhe](Teoria%20dei%20linguaggi%20formali.md#^definizione-stringa) su $\Sigma$ di [lunghezza](Teoria%20dei%20linguaggi%20formali.md#^definizione-lunghezza-di-una-stringa) $n$:
> 
> $$
> \Sigma^n = \{a_1a_2\cdots a_n \mid \forall i\in\{1,\ldots,n\}.(a_i\in\Sigma)\}
> $$
> 
> In particolare, $\Sigma^0={\varepsilon}$.
^definizione-potenza-n-esima-di-un-alfabeto

> [!esempio]- Esempio di potenza $\color{#7F7FFF} n$-esima di un alfabeto
> 
> Dato l'[alfabeto](Teoria%20dei%20linguaggi%20formali.md#^definizione-alfabeto) $\Sigma = \{ \text{a}, \text{b} \}$, la sua [potenza](Teoria%20dei%20linguaggi%20formali.md#^definizione-potenza-n-esima-di-un-alfabeto) seconda $\Sigma^2$ è il [linguaggio](Teoria%20dei%20linguaggi%20formali.md#^definizione-linguaggio-formale)
> 
> $$
> \Sigma^2 = \{ \text{aa}, \text{ab}, \text{ba}, \text{bb} \}
> $$

> [!proposizione]+ Proposizione: cardinalità della potenza $\color{#FF7F7F} n$-esima di un alfabeto
>
> Dato un [alfabeto](Teoria%20dei%20linguaggi%20formali.md#^definizione-alfabeto) finito $\Sigma$, con $|\Sigma| = m$, e dato un $n\in\mathbb{N}$, la cardinalità della sua [potenza $n$-esima](Teoria%20dei%20linguaggi%20formali.md#^definizione-potenza-n-esima-di-un-alfabeto) $\Sigma^n$ è:
>
> $$
> |\Sigma^n| = |\Sigma|^n=m^n
> $$

> [!dimostrazione]- Dimostrazione: cardinalità della potenza $\color{#7FFF7F} n$-esima di un alfabeto
> 
> Per [definizione](Teoria%20dei%20linguaggi%20formali.md#^definizione-potenza-n-esima-di-un-alfabeto), $\Sigma^n$ è l'[insieme](Teoria%20degli%20insiemi.md#^definizione-insieme) di tutte le [stringhe](Teoria%20dei%20linguaggi%20formali.md#^definizione-stringa) su $\Sigma$ di [lunghezza](Teoria%20dei%20linguaggi%20formali.md#^definizione-lunghezza-di-una-stringa) $n$ formate da [simboli](Teoria%20dei%20linguaggi%20formali.md#^definizione-simbolo) appartenenti a $\Sigma$ e, quindi, per costruire una [stringa](Teoria%20dei%20linguaggi%20formali.md#^definizione-stringa) di [lunghezza](Teoria%20dei%20linguaggi%20formali.md#^definizione-lunghezza-di-una-stringa) $n$ è necessario scegliere un [simbolo](Teoria%20dei%20linguaggi%20formali.md#^definizione-simbolo) di $\Sigma$ per ciascuna delle $n$ posizioni della [stringa](Teoria%20dei%20linguaggi%20formali.md#^definizione-stringa).
> 
> Poiché $|\Sigma| = m$ per ipotesi, per la prima posizione possiamo scegliere tra $m$ [simboli](Teoria%20dei%20linguaggi%20formali.md#^definizione-simbolo) dell'[alfabeto](Teoria%20dei%20linguaggi%20formali.md#^definizione-alfabeto), per la seconda posizione stessa cosa, e così via fino alla $n$-esima posizione. Per il principio fondamentale del conteggio%% link %%, il numero totale di [stringhe](Teoria%20dei%20linguaggi%20formali.md#^definizione-stringa) ottenibili è quindi:
> 
> $$
> \underbrace{m\cdot m\cdot\ldots\cdot m}_{n\text{ volte}}=m^n
> $$
> 
> Pertanto:
> 
> $$
> |\Sigma^n| = m^n = |\Sigma|^n
> $$
> 
> Per $n=0$, si ha $\Sigma^0={\varepsilon}$ e quindi:
> 
> $$
> |\Sigma^0| = 1 = |\Sigma|^0
> $$
> 
> $\blacksquare$

> [!definizione]+ Definizione: chiusura di Kleene su un alfabeto
> 
> Dato un [alfabeto](Teoria%20dei%20linguaggi%20formali.md#^definizione-alfabeto) $\Sigma$, la sua **chiusura di Kleene** $\Sigma^*$ è il [linguaggio](Teoria%20dei%20linguaggi%20formali.md#^definizione-linguaggio-formale) formato da tutte le [stringhe](Teoria%20dei%20linguaggi%20formali.md#^definizione-stringa) su $\Sigma$, inclusa quella [vuota](Teoria%20dei%20linguaggi%20formali.md#^definizione-stringa-vuota) $\varepsilon$. Formalmente, è l'unione%% link a unione di n insiemi %% di tutte le [potenze $n$-esime](Teoria%20dei%20linguaggi%20formali.md#^definizione-potenza-n-esima-di-un-alfabeto) di $\Sigma$:
> 
> $$
> \Sigma^* = \bigcup_{i \in \mathbb{N}} \Sigma^i
> $$
^definizione-chiusura-di-kleene-su-un-alfabeto

> [!esempio]- Esempio di chiusura di Kleene su un alfabeto
> 
> Dato l'[alfabeto](Teoria%20dei%20linguaggi%20formali.md#^definizione-alfabeto) $\Sigma = \{ \text{a}, \text{b} \}$, la sua [chiusura di Kleene](Teoria%20dei%20linguaggi%20formali.md#^definizione-chiusura-di-kleene-su-un-alfabeto) $\Sigma^*$ è
> 
> $$
> \begin{align*}
> \Sigma^* &= \bigcup_{i \in \mathbb{N}} \Sigma^i \\
> &= \Sigma^0 \cup \Sigma^1 \cup \Sigma^2 \cup \Sigma^3 \cup \ldots \\
> &= \{ \underbrace{\varepsilon}_{\Sigma^0}, \underbrace{\text{a}, \text{b}}_{\Sigma^1}, \underbrace{\text{aa}, \text{ab}, \text{ba}, \text{bb}}_{\Sigma^2}, \underbrace{\text{aaa}, \text{aab}, \text{aba}, \text{abb}, \text{baa}}_{\text{parte di }\Sigma^3}, \ldots \}
> \end{align*}
> $$

> [!definizione]+ Definizione: chiusura transitiva su un alfabeto
> 
> Dato un [alfabeto](Teoria%20dei%20linguaggi%20formali.md#^definizione-alfabeto) $\Sigma$. la sua **chiusura transitiva** $\Sigma^+$ è il [linguaggio](Teoria%20dei%20linguaggi%20formali.md#^definizione-linguaggio-formale) formato da tutte le [stringhe](Teoria%20dei%20linguaggi%20formali.md#^definizione-stringa) su $\Sigma$, eccetto quella [vuota](Teoria%20dei%20linguaggi%20formali.md#^definizione-stringa-vuota) $\varepsilon$. Formalmente, è l'unione%% link a unione di n insiemi %% di tutte le [potenze $n$-esime](Teoria%20dei%20linguaggi%20formali.md#^definizione-potenza-n-esima-di-un-alfabeto) di $\Sigma$ eccetto $\Sigma^0$:
> 
> $$
> \Sigma^+ = \bigcup_{i \in \mathbb{N} \setminus \{0\}} \Sigma^i
> $$
> 
> o, in alternativa,
> 
> $$
> \Sigma^+ = \Sigma^* \setminus \{ \varepsilon \}
> $$
^definizione-chiusura-transitiva-su-un-alfabeto

> [!esercizio]+ Esercizio sulle chiusure sugli alfabeti
> 
> Dato l'[alfabeto](Teoria%20dei%20linguaggi%20formali.md#^definizione-alfabeto) $\Sigma = \{ \text{a},\text{b},\text{c} \}$, elenca dieci [stringhe](Teoria%20dei%20linguaggi%20formali.md#^definizione-stringa) del [linguaggio](Teoria%20dei%20linguaggi%20formali.md#^definizione-linguaggio-formale)
> 
> $$
> L = \Sigma^+ \setminus \{ \text{b},\text{c} \}^*
> $$

> [!soluzione]- Soluzione dell'esercizio sulle chiusure sugli alfabeti
> 
> Il [linguaggio](Teoria%20dei%20linguaggi%20formali.md#^definizione-linguaggio-formale) $L = \Sigma^+ \setminus \{ \text{b},\text{c} \}^*$ è formato dalla [differenza](Teoria%20degli%20insiemi.md#^definizione-differenza-tra-due-insiemi) tra la [chiusura transitiva](Teoria%20dei%20linguaggi%20formali.md#^definizione-chiusura-transitiva-su-un-alfabeto) $L_1 = \Sigma^+$ e la [chiusura di Kleene](Teoria%20dei%20linguaggi%20formali.md#^definizione-chiusura-di-kleene-su-un-alfabeto) $L_2 = \{ \text{b},\text{c} \}$.
> 
> In particolare, la [chiusura transitiva](Teoria%20dei%20linguaggi%20formali.md#^definizione-chiusura-transitiva-su-un-alfabeto) $L_1 = \Sigma^+$ indica l'[insieme](Teoria%20degli%20insiemi.md#^definizione-insieme) di tutte le [stringhe](Teoria%20dei%20linguaggi%20formali.md#^definizione-stringa) su $\Sigma$, eccetto quella [vuota](Teoria%20dei%20linguaggi%20formali.md#^definizione-stringa-vuota) $\varepsilon$, mentre la [chiusura di Kleene](Teoria%20dei%20linguaggi%20formali.md#^definizione-chiusura-di-kleene-su-un-alfabeto) $L_2 = \{ \text{b},\text{c} \}$ indica l'[insieme](Teoria%20degli%20insiemi.md#^definizione-insieme) di tutte le [stringhe](Teoria%20dei%20linguaggi%20formali.md#^definizione-stringa) su $\{ \text{b},\text{c} \}$ compresa quella [vuota](Teoria%20dei%20linguaggi%20formali.md#^definizione-stringa-vuota) $\varepsilon$.
> 
> Quindi, facendo la [differenza](Teoria%20degli%20insiemi.md#^definizione-differenza-tra-due-insiemi) tra $L_1 = \Sigma^+$ (cioè tutte le [stringhe](Teoria%20dei%20linguaggi%20formali.md#^definizione-stringa) formate dai [simboli](Teoria%20dei%20linguaggi%20formali.md#^definizione-simbolo) $\text{a}$, $\text{b}$ o $\text{c}$) e $L_2 = \{ \text{b},\text{c} \}$ (cioè tutte le [stringhe](Teoria%20dei%20linguaggi%20formali.md#^definizione-stringa) formate dai [simboli](Teoria%20dei%20linguaggi%20formali.md#^definizione-simbolo) $\text{b}$ o $\text{c}$), otteniamo le [stringhe](Teoria%20dei%20linguaggi%20formali.md#^definizione-stringa) che contengono il [simbolo](Teoria%20dei%20linguaggi%20formali.md#^definizione-simbolo) $\text{a}$ almeno una volta:
> 
> $$
> \begin{align*}
> L &= L_1 \setminus L_2 \\
> &= \Sigma^+ \setminus \{ \text{b},\text{c} \}^* \\
> &= \{ \text{a}, \text{ba}, \text{ac}, \text{ccac}, \text{bba}, \text{aab}, \text{aca}, \text{baa}, \text{bac}, \text{cacca}, \ldots \}
> \end{align*}
> $$

Sia la [chiusura di Kleene](Teoria%20dei%20linguaggi%20formali.md#^definizione-chiusura-di-kleene-su-un-alfabeto) che quella [transitiva](Teoria%20dei%20linguaggi%20formali.md#^definizione-chiusura-transitiva-su-un-alfabeto) possono anche essere applicate su un [linguaggio](Teoria%20dei%20linguaggi%20formali.md#^definizione-linguaggio-formale) oltre che su un [alfabeto](Teoria%20dei%20linguaggi%20formali.md#^definizione-alfabeto).

> [!definizione]+ Definizione: chiusura di Kleene su un linguaggio
> 
> Dato un [linguaggio](Teoria%20dei%20linguaggi%20formali.md#^definizione-linguaggio-formale) $L$, la sua **chiusura di Kleene** $L^*$ è il [linguaggio](Teoria%20dei%20linguaggi%20formali.md#^definizione-linguaggio-formale) formato da tutte le [stringhe](Teoria%20dei%20linguaggi%20formali.md#^definizione-stringa) ottenibili [concatenando](Teoria%20dei%20linguaggi%20formali.md#^definizione-concatenazione-di-due-stringhe) un numero finito (anche nullo) di [stringhe](Teoria%20dei%20linguaggi%20formali.md#^definizione-stringa) appartenenti a $L$, inclusa quindi la [stringa vuota](Teoria%20dei%20linguaggi%20formali.md#^definizione-stringa-vuota) $\varepsilon$.
> 
> Formalmente, è l'unione di tutte le [potenze $n$-esime](Teoria%20dei%20linguaggi%20formali.md#^definizione-potenza-n-esima-di-un-linguaggio) di $L$:
> 
> $$
> L^* = \bigcup_{i \in \mathbb{N}} L^i
> $$
^definizione-chiusura-di-kleene-su-un-linguaggio

> [!esempio]- Esempio di chiusura di Kleene su un linguaggio
> 
> Dato il [linguaggio](Teoria%20dei%20linguaggi%20formali.md#^definizione-linguaggio-formale) $L = \{ \text{ab}, \text{ba} \}$, la sua [chiusura di Kleene](Teoria%20dei%20linguaggi%20formali.md#^definizione-chiusura-di-kleene-su-un-linguaggio) $L^*$ è:
> 
> $$
> \begin{align*}
> L^* &= \bigcup_{i \in \mathbb{N}} L^i \\
> &= L^0 \cup L^1 \cup L^2 \cup L^3 \cup \ldots \\
> &= \{ \underbrace{\varepsilon}_{L^0}, \underbrace{\text{ab}, \text{ba}}_{L^1}, \underbrace{\text{abab}, \text{abba}, \text{baab}, \text{baba}}_{L^2}, \underbrace{\text{ababab}, \text{ababba}, \text{abbaab}}_{\text{parte di }L^3}, \ldots \}
> \end{align*}
> $$
^esempio-di-chiusura-di-kleene-su-un-linguaggio

> [!definizione]+ Definizione: chiusura transitiva su un linguaggio
> 
> Dato un [linguaggio](Teoria%20dei%20linguaggi%20formali.md#^definizione-linguaggio-formale) $L$, la sua **chiusura transitiva** $L^+$ è il [linguaggio](Teoria%20dei%20linguaggi%20formali.md#^definizione-linguaggio-formale) formato da tutte le [stringhe](Teoria%20dei%20linguaggi%20formali.md#^definizione-stringa) ottenibili [concatenando](Teoria%20dei%20linguaggi%20formali.md#^definizione-concatenazione-di-due-stringhe) una o più [stringhe](Teoria%20dei%20linguaggi%20formali.md#^definizione-stringa) appartenenti a $L$, escludendo quindi la [stringa vuota](Teoria%20dei%20linguaggi%20formali.md#^definizione-stringa-vuota) $\varepsilon$ quando non è ottenibile tramite [concatenazione](Teoria%20dei%20linguaggi%20formali.md#^definizione-concatenazione-di-due-stringhe) di [stringhe](Teoria%20dei%20linguaggi%20formali.md#^definizione-stringa) appartenenti a $L$.
> 
> Formalmente, è l'unione di tutte le [potenze $n$-esime](Teoria%20dei%20linguaggi%20formali.md#^definizione-potenza-n-esima-di-un-linguaggio) di $L$, escludendo $L^0$:
> 
> $$
> L^+ = \bigcup_{i \in \mathbb{N}\setminus\{0\}} L^i
> $$
^definizione-chiusura-transitiva-su-un-linguaggio

> [!attenzione]+ Attenzione: una chiusura transitiva su un linguaggio può contenere la stringa vuota
> 
> A differenza della [chiusura transitiva su un alfabeto](Teoria%20dei%20linguaggi%20formali.md#^definizione-chiusura-transitiva-su-un-alfabeto), la [chiusura transitiva di un linguaggio](Teoria%20dei%20linguaggi%20formali.md#^definizione-chiusura-transitiva-su-un-linguaggio) $L$ non esclude necessariamente la [stringa vuota](Teoria%20dei%20linguaggi%20formali.md#^definizione-stringa-vuota) $\varepsilon$.
> 
> Infatti, se $\varepsilon \in L$, allora $\varepsilon \in L^+$, poiché la [chiusura transitiva](Teoria%20dei%20linguaggi%20formali.md#^definizione-chiusura-transitiva-su-un-linguaggio) comprende anche le [stringhe](Teoria%20dei%20linguaggi%20formali.md#^definizione-stringa) ottenute [concatenando](Teoria%20dei%20linguaggi%20formali.md#^definizione-concatenazione-di-due-stringhe) una sola [stringa](Teoria%20dei%20linguaggi%20formali.md#^definizione-stringa) appartenente a $L$.
> 
> Ad esempio, se $L=\{\varepsilon, \text{a}\}$, allora la [chiusura di Kleene](Teoria%20dei%20linguaggi%20formali.md#^definizione-chiusura-di-kleene-su-un-linguaggio) e quella [transitiva](Teoria%20dei%20linguaggi%20formali.md#^definizione-chiusura-transitiva-su-un-linguaggio) coincidono, perché $\varepsilon$ viene inclusa anche nella [transitiva](Teoria%20dei%20linguaggi%20formali.md#^definizione-chiusura-transitiva-su-un-alfabeto):
> 
> $$
> L^+=L^*=\{\varepsilon,\text{a},\text{aa},\text{aaa},\ldots\}
> $$
> 
> Se invece $L = \{ \text{a} \}$, allora
> 
> $$
> \begin{array}{}
> L^*=\{\varepsilon,\text{a},\text{aa},\text{aaa},\ldots\} \\
> L^+=\{\text{a},\text{aa},\text{aaa},\ldots\}
> \end{array}
> $$
> 
> Si può riassumere questo comportamento generalmente come:
> 
> $$
> L^+ = L^* \setminus \{\varepsilon\} \iff \varepsilon \not\in L
> $$

Ora possiamo "ri-definire" l'operazione%% link %% [insiemistica](Teoria%20degli%20insiemi.md#^definizione-insieme) del [complemento](Teoria%20degli%20insiemi.md#^definizione-complemento-di-un-insieme), applicando questo concetto ai [linguaggi formali](Teoria%20dei%20linguaggi%20formali.md#^definizione-linguaggio-formale).

> [!definizione]+ Definizione: complemento di un linguaggio
> 
> Dato un [linguaggio](Teoria%20dei%20linguaggi%20formali.md#^definizione-linguaggio-formale) $L$ su un [alfabeto](Teoria%20dei%20linguaggi%20formali.md#^definizione-alfabeto) $\Sigma$, il suo **complemento** $\overline L$ è il [linguaggio](Teoria%20dei%20linguaggi%20formali.md#^definizione-linguaggio-formale) ottenuto dalla [differenza](Teoria%20degli%20insiemi.md#^definizione-differenza-tra-due-insiemi) tra la [chiusura di Kleene](Teoria%20dei%20linguaggi%20formali.md#^definizione-chiusura-di-kleene-su-un-alfabeto) $\Sigma^*$ e $L$ stesso:
> 
> $$
> \overline L = \Sigma^* \setminus L
> $$
^definizione-complemento-di-un-linguaggio

> [!definizione]+ Definizione: concatenazione di due linguaggi
> 
> Dati due [linguaggi](Teoria%20dei%20linguaggi%20formali.md#^definizione-linguaggio-formale) $L_1$ e $L_2$, la loro **concatenazione** $L_1L_2$ è il [linguaggio](Teoria%20dei%20linguaggi%20formali.md#^definizione-linguaggio-formale) ottenuto [concatenando](Teoria%20dei%20linguaggi%20formali.md#^definizione-concatenazione-di-due-stringhe) ogni [stringa](Teoria%20dei%20linguaggi%20formali.md#^definizione-stringa) $u \in L_1$ con ogni [stringa](Teoria%20dei%20linguaggi%20formali.md#^definizione-stringa) $v \in L_2$:
> 
> $$
> L_1L_2 = \{ uv \mid u \in L_1 \land v \in L_2 \}
> $$
^definizione-concatenazione-di-due-linguaggi

> [!esempio]- Esempio di concatenazione di due linguaggi
> 
> Dati i [linguaggi](Teoria%20dei%20linguaggi%20formali.md#^definizione-linguaggio-formale) $L_1 = \{ \text{ca}, \text{pa} \}$ e $L_2 = \{ \text{sta}, \text{ne} \}$, la loro [concatenazione](Teoria%20dei%20linguaggi%20formali.md#^definizione-concatenazione-di-due-linguaggi) $L_1L_2$ è
> 
> $$
> L_1L_2 = \{ \text{casta}, \text{pasta}, \text{cane}, \text{pane} \}
> $$

> [!proprieta]+ Proprietà: associatività della concatenazione di linguaggi
>
> La [concatenazione](Teoria%20dei%20linguaggi%20formali.md#^definizione-concatenazione-di-due-linguaggi) è associativa%% link %%, cioè dati tre [linguaggi](Teoria%20dei%20linguaggi%20formali.md#^definizione-linguaggio-formale) $L_1$, $L_2$ e $L_3$ vale
>
> $$
> L_1(L_2L_3) = (L_1L_2)L_3
> $$

> [!osservazione]+ Osservazione: non commutatività della concatenazione di linguaggi
>
> La [concatenazione](Teoria%20dei%20linguaggi%20formali.md#^definizione-concatenazione-di-due-linguaggi) **non** è commutativa%% link %%, infatti dati due [linguaggi](Teoria%20dei%20linguaggi%20formali.md#^definizione-linguaggio-formale) $L_1$ e $L_2$ abbiamo che genericamente
>
> $$
> L_1L_2 \ne L_2L_1
> $$
>
> eccetto in particolari casi, ad esempio quando almeno uno dei due è il [linguaggio vuoto](Teoria%20dei%20linguaggi%20formali.md#^definizione-linguaggio-vuoto), oppure quando i due [linguaggi](Teoria%20dei%20linguaggi%20formali.md#^definizione-linguaggio-formale) coincidono.

> [!proprieta]+ Proprietà: assorbimento della concatenazione rispetto al linguaggio vuoto
> 
> Il [linguaggio vuoto](Teoria%20dei%20linguaggi%20formali.md#^definizione-linguaggio-vuoto) $\emptyset$ è un elemento assorbente%% link %% della [concatenazione](Teoria%20dei%20linguaggi%20formali.md#^definizione-concatenazione-di-due-linguaggi): infatti, preso un qualsiasi [linguaggio](Teoria%20dei%20linguaggi%20formali.md#^definizione-linguaggio-formale) $L$, la loro [concatenazione](Teoria%20dei%20linguaggi%20formali.md#^definizione-concatenazione-di-due-stringhe) $L\emptyset$ o $\emptyset L$ produce sempre il [linguaggio vuoto](Teoria%20dei%20linguaggi%20formali.md#^definizione-linguaggio-vuoto) $\emptyset$.
> 
> Infatti, per la [definizione di _concatenazione_](Teoria%20dei%20linguaggi%20formali.md#^definizione-concatenazione-di-due-linguaggi), abbiamo che
> 
> $$
> L\emptyset=\{uv\mid u\in L \land v\in\emptyset\}
> $$
> 
> ma, poiché il [linguaggio vuoto](Teoria%20dei%20linguaggi%20formali.md#^definizione-linguaggio-vuoto) non contiene alcuna [stringa](Teoria%20dei%20linguaggi%20formali.md#^definizione-stringa), non esiste nessuna stringa $v$ tale che $v \in \emptyset$. Di conseguenza, non esistono stringhe concatenabili e l'insieme risultante non contiene alcun elemento: da qui l'[insieme vuoto](Teoria%20degli%20insiemi.md#^definizione-insieme-vuoto). Stesso discorso per $\emptyset L$.

> [!proprieta]+ Proprietà: neutralità della concatenazione rispetto al linguaggio contenente la stringa vuota
>
> Il [linguaggio](Teoria%20dei%20linguaggi%20formali.md#^definizione-linguaggio-formale) $\{\varepsilon\}$, costituito dalla sola [stringa vuota](Teoria%20dei%20linguaggi%20formali.md#^definizione-stringa-vuota), è l'elemento neutro%% link %% della [concatenazione dei linguaggi](Teoria%20dei%20linguaggi%20formali.md#^definizione-concatenazione-di-due-linguaggi): infatti, preso un qualsiasi [linguaggio](Teoria%20dei%20linguaggi%20formali.md#^definizione-linguaggio-formale) $L$, la sua [concatenazione](Teoria%20dei%20linguaggi%20formali.md#^definizione-concatenazione-di-due-linguaggi) con $\{\varepsilon\}$, sia $L\{\varepsilon\}$ sia $\{\varepsilon\}L$, produce sempre $L$.

> [!esercizio]+ Esercizio 1 sulla concatenazione di linguaggi
> 
> Dato l'[alfabeto](Teoria%20dei%20linguaggi%20formali.md#^definizione-alfabeto) $\Sigma = \{ \text{a},\text{b},\text{c} \}$, elenca dieci [stringhe](Teoria%20dei%20linguaggi%20formali.md#^definizione-stringa) del [linguaggio](Teoria%20dei%20linguaggi%20formali.md#^definizione-linguaggio-formale)
> 
> $$
> L = (\Sigma^2 \cup \Sigma^3)\{ \text{a},\text{b} \}
> $$

> [!soluzione]- Soluzione dell'esercizio 1 sulla concatenazione di linguaggi
> 
> Il [linguaggio](Teoria%20dei%20linguaggi%20formali.md#^definizione-linguaggio-formale) $L = (\Sigma^2 \cup \Sigma^3)\{ \text{a},\text{b} \}$ è formato dalla [concatenazione](Teoria%20dei%20linguaggi%20formali.md#^definizione-concatenazione-di-due-linguaggi) di $L_1 = \Sigma^2 \cup \Sigma^3$ e $L_2 = \{ \text{a},\text{b} \}$.
> 
> Il [linguaggio](Teoria%20dei%20linguaggi%20formali.md#^definizione-linguaggio-formale) $L_1 = \Sigma^2 \cup \Sigma^3$ indica l'[unione](Teoria%20degli%20insiemi.md#^definizione-unione-di-due-insiemi) delle [potenze](Teoria%20dei%20linguaggi%20formali.md#^definizione-potenza-n-esima-di-un-alfabeto) seconde e terze di $\Sigma$, ossia tutte le [stringhe](Teoria%20dei%20linguaggi%20formali.md#^definizione-stringa) di [lunghezza](Teoria%20dei%20linguaggi%20formali.md#^definizione-lunghezza-di-una-stringa) $2$ o $3$ su $\Sigma$, quindi
> 
> $$
> L_1 = \{ \text{ab},\text{bcc},\text{cb},\text{aaa}, \text{ac}\ldots \}
> $$
> 
> [Concatenando](Teoria%20dei%20linguaggi%20formali.md#^definizione-concatenazione-di-due-linguaggi) queste cinque [stringhe](Teoria%20dei%20linguaggi%20formali.md#^definizione-stringa) di $L_1$ con $L_2 = \{ \text{a},\text{b} \}$, otteniamo
> 
> $$
> \begin{align*}
> L &= L_1L_2 \\
> &= \{ \text{ab},\text{bcc},\text{cb},\text{aaa}, \text{ac}\ldots \}\{ \text{a},\text{b} \} \\
> &= \{ \text{aba}, \text{bcca}, \text{cba}, \text{aaaa}, \text{aca}, \text{abb}, \text{bccb}, \text{cbb}, \text{aaab}, \text{acb}, \ldots \}
> \end{align*}
> $$
> 
> ed ecco dieci possibili [stringhe](Teoria%20dei%20linguaggi%20formali.md#^definizione-stringa) di $L$.

> [!definizione]+ Definizione: potenza $\color{#FF7FFF} n$-esima di un linguaggio
>
> Dato un [linguaggio](Teoria%20dei%20linguaggi%20formali.md#^definizione-linguaggio-formale) $L$, la sua **potenza $n$-esima** $L^n$ (con $n \in \mathbb{N}$) è il [linguaggio](Teoria%20dei%20linguaggi%20formali.md#^definizione-linguaggio-formale) ottenuto [concatenando](Teoria%20dei%20linguaggi%20formali.md#^definizione-concatenazione-di-due-linguaggi) $L$ per $n$ volte:
>
> $$
> L^n = \underbrace{LL\ldots L}_{n \text{ volte}} =
> \begin{cases}
> \{\varepsilon\} & \text{se } n = 0 \\
> L^{n-1}L & \text{se } n > 0
> \end{cases}
> $$
^definizione-potenza-n-esima-di-un-linguaggio

> [!esempio]- Esempio di potenza $\color{#7F7FFF} n$-esima di un linguaggio
> 
> Dato il [linguaggio](Teoria%20dei%20linguaggi%20formali.md#^definizione-linguaggio-formale) $L = \{ \text{sì}, \text{no} \}$, la sua [potenza](Teoria%20dei%20linguaggi%20formali.md#^definizione-potenza-n-esima-di-un-linguaggio) seconda $L^2$ è il [linguaggio](Teoria%20dei%20linguaggi%20formali.md#^definizione-linguaggio-formale)
> 
> $$
> \begin{align*}
> L^2 &= LL^1 \\
> &= LLL^0 \\
> &= \{ \text{sì}, \text{no} \} \{ \text{sì}, \text{no} \} \{ \varepsilon \} \\
> &= \{ \text{sìsì}, \text{sìno}, \text{nosì}, \text{nono} \}
> \end{align*}
> $$

# 2 - Approcci per la descrizione di linguaggi

Come abbiamo visto, possiamo descrivere un [linguaggio formale](Teoria%20dei%20linguaggi%20formali.md#^definizione-linguaggio-formale) attraverso le [stringhe](Teoria%20dei%20linguaggi%20formali.md#^definizione-stringa) che lo compongono. Solitamente, ai fini dello studio, i [linguaggi](Teoria%20dei%20linguaggi%20formali.md#^definizione-linguaggio-formale) davvero interessanti sono quelli contenenti un numero _infinito_%% link %% di [stringhe](Teoria%20dei%20linguaggi%20formali.md#^definizione-stringa), ma non è possibile descriverli semplicemente elencandole tutte (come per esempio fanno i vocabolari che elencano tutte le parole di una lingua).

Occorre quindi un approccio _finito_%% link %% per descrivere un [linguaggio](Teoria%20dei%20linguaggi%20formali.md#^definizione-linguaggio-formale) _infinito_: potremmo per esempio trovare un modo _meccanico_ per dire se una [stringa](Teoria%20dei%20linguaggi%20formali.md#^definizione-stringa) è "accettabile" all'interno di un [linguaggio](Teoria%20dei%20linguaggi%20formali.md#^definizione-linguaggio-formale) o meno.

%% collegarsi da qui ai DFA %%

---

> [!fonti]+ Fonti
> 
> - 🏫 Corso di Laurea in Informatica (`L-31 R`) presso l'Università di Torino:
>     - Corso di _Linguaggi Formali e Traduttori_ (`INF0344`), A.A. 2026-27 ([pagina Moodle](https://informatica.i-learn.unito.it/course/view.php?id=3735)):
> 		- Prof. Jeremy James Sproston, slide del corso:
> 			- [1.3 - _Linguaggi_](https://informatica.i-learn.unito.it/pluginfile.php/510313/mod_folder/content/0/1-3_linguaggi.pdf).
