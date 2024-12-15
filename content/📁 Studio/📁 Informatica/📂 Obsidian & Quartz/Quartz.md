---
icon:
---
[Quartz](https://quartz.jzhao.xyz/) è un tool che genera siti completi a partire da note scritte in Markdown. Per scrivere queste note in Markdown, uso [Obsidian](https://obsidian.md/).

# Installazione

Seguire la guida per l'installazione indicata sul [sito di Quartz](https://quartz.jzhao.xyz/#-get-started). Se durante l'installazione, dopo aver eseguito il comando `npm i`, esce un errore del genere:

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

# Configurazione

Ecco quello che ho modificato nei file di Quartz per ottenere la configurazione che adotta per generare questo sito.

## `quartz.config.ts`

- **`pageTitle: "🪴 Giardino Digitale di Rexus752"`**: titolo che esce all'inizio di ogni pagina.
- **`locale: "it-IT"`**: per impostare la lingua in italiano.
- **`baseUrl: "rexus752.pages.dev"`**: URL del sito.

## `quartz.layout.ts`

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
				repoId: 'R_kgDONHp66Q',
				// from data-category
				category: 'Announcementypescript',
				// from data-category-id
				categoryId: 'DIC_kwDONHp66c4Cjzbq',
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

## `quartz/static`

Nella cartella ho messo la mia `icon.png` per dare l'icona al sito. L'icona l'ho creata attraverso questo [generatore sul sito ufficiale di Obsidian](https://obsidian.md/blog/new-obsidian-icon/) che ti permette di personalizzare la nuova icona di Obsidian adottata nel 2023 con i propri colori (e io ho usato l'azzurro e il rosa perché ricordano la mia classica propic che uso ovunque). 

## Modalità scura di default

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

## `quartz/styles/customs.scss`

In questo file ci vanno le configurazioni personalizzate per lo stile.

### Tabelle

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
	background-color: #222224;
}
```

## `quartz/styles/variables.scss`

In questo file, ho modificato le seguenti righe per evitare di avere spazio inutilmente occupato all'inizio della pagina e ai lati.

```scss
$sidePanelWidth: 300px; // Initial value: 380px
$topSpacing: 2rem; // Initial value: 6rem
```

## `quartz/i18n/locales/it-IT.ts`

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