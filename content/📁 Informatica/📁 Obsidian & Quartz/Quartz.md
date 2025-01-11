---
icon: SiObsidian
iconColor: "#888888"
---
[Quartz](https://quartz.jzhao.xyz/) è un tool che genera siti completi a partire da note scritte in Markdown. Per scrivere queste note in Markdown, uso [Obsidian](https://obsidian.md/).

# 1 - Installazione e troubleshooting

Seguire la guida per l'installazione indicata sul [sito di Quartz](https://quartz.jzhao.xyz/#-get-started).

Se durante l'installazione, dopo aver eseguito il comando `npm i`, esce un errore del genere:

```
added 526 packages, and audited 528 packages in 9s

173 packages are looking for funding
  run npm fund for details

3 vulnerabilities (2 moderate, 1 high)

To address all issues, run:
  npm audit fix

Run npm audit for details.
```

Allora eseguire il comando `npm audit fix` per risolvere.

Se durante il clone vi esce il seguente messaggio:

```
error: RPC failed; curl 92 HTTP/2 stream 5 was not closed cleanly: CANCEL (err 8)
error: 40 bytes of body are still expected
fetch-pack: unexpected disconnect while reading sideband packet
fatal: early EOF
fatal: fetch-pack: invalid index-pack output
```

Allora significa che c'è stato un problema di connessione, quindi rieseguire il clone.

# 2 - Configurazione

Ecco quello che ho modificato nei file di Quartz per ottenere la configurazione che adotta per generare questo sito.

## 2.1 - `quartz.config.ts`

- **`pageTitle: "🪴 Giardino Digitale di Rexus752"`**: titolo che esce all'inizio di ogni pagina.
- **`locale: "it-IT"`**: per impostare la lingua in italiano.
- **`baseUrl: "rexus752.pages.dev"`**: URL del sito.

## 2.2 - `quartz.layout.ts`

Questo è il layout che uso nel mio sito.

```typescript
import { PageLayout, SharedLayout } from "./quartz/cfg"
import * as Component from "./quartz/componentypescript"

// componentypescript shared across all pages
export const sharedPageComponentypescript: SharedLayout = {
	head: Component.Head(),
	header: [],
	afterBody: [
		Component.Commentypescript({
			provider: 'giscus',
			options: {
				// from data-repo
				repo: 'Rexus752/digital-garden',
				// from data-repo-id
				repoId: '<repoId>',
				// from data-category
				category: 'Announcementypescript',
				// from data-category-id
				categoryId: '<categoryId>',
			}
		}),
	],
	footer: Component.Footer({
		links: {
			"GitHub Repository": "https://github.com/Rexus752/digital-garden",
		},
	}),
}

// componentypescript for pages that display a single page (e.g. a single note)
export const defaultContentPageLayout: PageLayout = {
	beforeBody: [
		Component.Breadcrumbs(),
		Component.MobileOnly(Component.TableOfContentypescript()),
		Component.ArticleTitle(),
		Component.ContentMeta(),
		Component.TagList(),
	],
	left: [
		Component.PageTitle(),
		Component.Search(),
		// Component.Darkmode(),
		Component.DesktopOnly(Component.TableOfContentypescript()),
		
	],
	right: [
		Component.DesktopOnly(Component.Explorer()),
		Component.Graph(),
	],
}

// componentypescript for pages that display listypescript of pages	(e.g. tags or folders)
export const defaultListPageLayout: PageLayout = {
	beforeBody: [
		Component.Breadcrumbs(),
		Component.ArticleTitle(),
		Component.ContentMeta()
	],
	left: [
		Component.PageTitle(),
		Component.MobileOnly(Component.Spacer()),
		Component.Search(),
		// Component.Darkmode(),
	],
	right: [
		Component.DesktopOnly(Component.Explorer()),
		Component.Graph(),
	],
}

```

## 2.3 - `quartz/static`

Nella cartella ho messo la mia `icon.png` per dare l'icona al sito. L'icona l'ho creata attraverso questo [generatore sul sito ufficiale di Obsidian](https://obsidian.md/blog/new-obsidian-icon/) che ti permette di personalizzare la nuova icona di Obsidian adottata nel 2023 con i propri colori (e io ho usato l'azzurro e il rosa perché ricordano la mia classica propic che uso ovunque). 

## 2.4 - Modalità scura di default

Impostare la modalità scura di default sul sito è un bel casino, ci ho messo un bel po' per capire come diamine farlo, ma alla fine ho scelto l'opzione più stupida e più diretta per realizzarlo: nel file `quartz.config.ts` ho scambiato di posto le parole `lightMode` e `darkMode`.

```typescript
colors: {
	darkMode: {
		light: "#faf8f8",
		lightgray: "#e5e5e5",
		gray: "#b8b8b8",
		darkgray: "#4e4e4e",
		dark: "#2b2b2b",
		secondary: "#284b63",
		tertiary: "#84a59d",
		highlight: "rgba(143, 159, 169, 0.15)",
		textHighlight: "#fff23688",
	},
	lightMode: {
		light: "#161618",
		lightgray: "#393639",
		gray: "#646464",
		darkgray: "#d4d4d4",
		dark: "#ebebec",
		secondary: "#7b97aa",
		tertiary: "#84a59d",
		highlight: "rgba(143, 159, 169, 0.15)",
		textHighlight: "#b3aa0288",
	},
},
```

Stessa cosa ho fatto per quanto riguarda il [syntax highlighting](https://quartz.jzhao.xyz/features/syntax-highlighting) (sempre in `quartz.config.ts`), al quale ho applicato i colori scuri semplicemente scambiando i valori `github-light` e `github-dark`.

```typescript
Plugin.SyntaxHighlighting({
	theme: {
		light: "github-dark",
		dark: "github-light",
	},
	keepBackground: false,
}),
```

## 2.5 - `quartz/styles/customs.scss`

In questo file ci vanno le configurazioni personalizzate per lo stile.

### 2.5.1 - Tabelle

Il padding delle tabelle l'ho modificato in modo da renderle un po' più "compatte" senza lasciar passare l'intera Autostrada del Sole tra il contenuto della cella e il bordo.

```scss
.table-container {
	& > table {
		margin: 0rem;
		padding: 0rem;
		& > * {
			line-height: 1.2rem;
		}
	}
}

th {
	text-align: center;
	border: 1px solid var(--gray);
	background-color: var(--lightgray);
}

td {
	border: 1px solid var(--lightgray);
}
```

Inoltre, per alternare i colori delle righe (in modo da distinguerle più facilmente), ho aggiunto questo:

```scss
tbody tr:nth-child(2n) {
	background-color: #22222488;
}
```

Nota: quell'`88` finale alla fine del codice del colore serve per rendere trasparente la riga della tabella, in modo che nei callout colorati faccia trasparire il colore dello sfondo.

## 2.6 - `quartz/styles/variables.scss`

In questo file, ho modificato le seguenti righe per evitare di avere spazio inutilmente occupato all'inizio della pagina e ai lati.

```scss
$sidePanelWidth: 300px; // Initial value: 380px
$topSpacing: 2rem; // Initial value: 6rem
```

## 2.7 - `quartz/i18n/locales/it-IT.ts`

Nel file delle traduzioni in italiano, ho modificato le seguenti traduzioni.

```typescript
graph: {
  title: "Vista grafo",
},
```

```typescript
tableOfContentypescript: {
  title: "Indice",
},
```

```typescript
contentMeta: {
  readingTime: ({ minutes }) => `${minutes} minuti di lettura`,
},
```

## 2.8 - Callout personalizzati

All'interno del mio Giardino Digitale, uso i seguenti callout personalizzati, dichiarati nel file `quartz/styles/custom.scss`. Sul [sito di Quartz](https://quartz.jzhao.xyz/features/callouts) viene spiegato come aggiungerne di nuovi.

Io, per aggiungere nuovi callout, uso questo metodo:
- Cerco una possibile icona su [FontAwesome](https://fontawesome.com/v6/search).
- Copio il codice SVG.
- Lo converto in URL tramite questo [tool](https://yoksel.github.io/url-encoder/).
- Lo aggiungo nel file `custom.scss` con il seguente formato:
	```scss
	.callout {
		&[data-callout="<name>"] {
			--color: #<color>;
		    --border: #<border color>;
			--bg: #<bg color>;
			--callout-icon: url("data:image/svg+xml; utf8, <custom formatted SVG icon code>");
		}
	}
	```

### 2.8.1 - Lista dei callout che uso

#### 2.8.1.1 - Generici

> [!esempio] Esempio
> 
> Per gli esempi.

> [!trucco] Trucco
> Per i trucchetti mnemonici.

%%
da aggiungere:
- [!consiglio]
- [!attenzione]
%%

#### 2.8.1.2 - Matematici

> [!definizione]
> 
> Per le definizioni matematiche.

> [!osservazione] Osservazione
>
> Per le osservazioni matematiche.

> [!proposizione] Proposizione
> Per i teoremi, proposizioni, lemmi, corollari e proprietà matematiche o, in genere, tutto ciò che va dimostrato.

> [!dimostrazione] Dimostrazione
> Per le dimostrazioni matematiche.

> [!principio] Principio
> Per i principi matematici.

# 3 - Problemi di Quartz

Ecco una lista di problemi che ho trovato usando Quartz e come li ho risolti. Per molti di questi problemi non ho ancora trovato una soluzione e, non avendo idea di come risolverli, credo che semplicemente aspetterò che il creatore di Quartz (Jacky Zhao) lo faccia.
%% collegare ogni problema a una issue sul repo di GitHub aperta da me o da qualcun altro %%
%% da aggiungere: parseBlockReferences non funziona %%

## 3.1 - `/` nei displayed name dei link

### 3.1.1 - Problema

Se ho un link del tipo

```
[processi I/O-bound](Processi.md#4.1%20-%20Processo%20I/O-bound)
```

Quel `/` nel displayed name del link crede sia tipo un path quindi compare solo come link [O-bound](Processi.md#4.1%20-%20Processo%20I/O-bound).

### 3.1.2 - Soluzione

Non l'ho ancora risolto (lol), infatti nella pagina [Processi](Processi.md) si trovano dei link [O-bound](Processi.md#4.1%20-%20Processo%20I/O-bound).

## 3.2 - Table Of Contents non renderizza correttamente

### 3.2.1 - Problema

Il Table Of Contents (l'indice al lato) renderizza i pezzetti di codice inline come testo normale. Fin qui non ci sarebbe nessun problema, se non fosse che non renderizza neanche il LaTeX inline.

Anche i tag HTML che usavo per cambiare colore al font (es. `<span style="color:#FF88FF; background:#00000000">Definizione: insieme</span>`) non me li renderizzava ma me li prendeva come testo normale.

### 3.2.2 - Soluzione

Non ho ancora risolto, però ho intenzione di provare a integrare una sorta di "renderer" in Quartz (però c'è da studiarsi come funziona il parsing dei dati per creare il Table Of Contents e se è effettivamente fattibile o meno).

## 3.3 - Table Of Contents mezza colonna

### 3.3.1 - Problema

Se `Component.TableOfContents()` viene specificato come `DesktopOnly` (quindi con `Component.DesktopOnly(Component.TableOfContents())`), occupa solo mezza colonna anziché l'intero resto della colonna laterale in cui viene inserito.

### 3.3.2 - Soluzione

Non l'ho risolto, infatti occupa ancora solo mezza colonna laterale.

## 3.4 - Table Of Contents fisso se non `DesktopOnly`

### 3.4.1 - Problema

Se `Component.TableOfContents()` non viene specificato come `DesktopOnly` (quindi con `Component.DesktopOnly(Component.TableOfContents())`), non si può scorrere.

### 3.4.2 - Soluzione

Devo ancora trovare un modo per risolverlo.

## 3.5 - Click sul link all'heading non porta all'heading

### 3.5.1 - Problema

Se in una pagina clicco su un link che mi porta a un heading nella stessa pagina, a volte non succede nulla oppure porta a un altro heading.

### 3.5.2 - Soluzione

Cliccare sui link aprendoli in un'altra tab (col `Middle Click`) anziché nella stessa tab (col `Left Click`). È un workaround non ottimale, ma non ho idea di come si possa sistemare.

## 3.6 - File e cartelle con stesso nome nella stessa cartella

### 3.6.1 - Problema

Quartz si rincoglionisce quando ci sono file e cartelle con lo stesso nome nella stessa cartella, in particolare:
- Nell'explorer compare solo la pagina, ma non la cartella.
- Sminchia completamente gli hyperlink nell'headcrumb.

### 3.6.2 - Soluzione

È un workaround, ma almeno funziona: mettere `📁` all'inizio del nome della cartella, così Quartz riesce a distinguerli.

## 3.7 - Titoli dei callout non colorano il LaTeX

### 3.7.1 - Problema

Se ho un callout di questo tipo:

> [!esempio] Esempio: $\{0\}$ e $\{\{1,2,3\}\}$ sono singoletti
> 
> Gli insiemi $\{0\}$ e $\{\{1,2,3\}\}$ sono singoletti: in particolare, il primo è formato unicamente dall'elemento $0$, mentre il secondo è formato dall'unico elemento $\{1,2,3\}$ che a sua volta è un insieme (non unitario).

I blocchi di LaTeX inline nel titolo del callout non vengono colorati ma rimangono bianchi.

### 3.7.2 - Soluzione

È un workaround, ma almeno funziona: mettere `\color{<codice colore>}` nel blocco inline di LaTeX.

> [!esempio] Esempio: $\color{#8888FF}\{0\}$ e $\color{#8888FF}\{\{1,2,3\}\}$ sono singoletti
> 
> Gli insiemi $\{0\}$ e $\{\{1,2,3\}\}$ sono singoletti: in particolare, il primo è formato unicamente dall'elemento $0$, mentre il secondo è formato dall'unico elemento $\{1,2,3\}$ che a sua volta è un insieme (non unitario).

# 4 - TODO

Lista delle cose che devo fare per migliorare questo Giardino Digitale:
- Cambiare il font monospaziato usato per il codice (quando è inline è inguardabile per me).
- Diminuire la grandezza del font del LaTeX (quello inline è più grande del testo normale).
- Per la visualizzazione da mobile: aggiungere un pulsante fluttuante per vedere il Table Of Contents.
- Per la visualizzazione da desktop: aggiungere un Table Of Contents fluttuante sul lato (stile Notion).
- Risolvere problema dei [`/` nei displayed name dei link](Quartz.md#3.1%20-%20`/`%20nei%20displayed%20name%20dei%20link).
- Risolvere il problema del [Table Of Contents che non renderizza correttamente](Quartz.md#3.2%20-%20Table%20Of%20Contents%20non%20renderizza%20correttamente).
- Risolvere il problema del [Table Of Contents mezza colonna](Quartz.md#3.3%20-%20Table%20Of%20Contents%20mezza%20colonna).
- Risolvere il problema del [Table Of Contents fisso se non `DesktopOnly`](Quartz.md#3.4%20-%20Table%20Of%20Contents%20fisso%20se%20non%20`DesktopOnly`).
- Risolvere il problema del [click sul link all'heading non porta all'heading](Quartz.md#3.5%20-%20Click%20sul%20link%20all'heading%20non%20porta%20all'heading).
- Aggiungere una funzionalità per aprire una nota casuale nel Giardino Digitale.
- Cercare di integrare il plugin Iconize aggiungendo le icone alle pagine e le icone inline.
- Le tabelle non devono essere scrollabili in larghezza, ma devono essere fixed con larghezza pari alla larghezza del body.