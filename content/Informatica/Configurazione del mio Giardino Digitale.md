---
title: Configurazione del mio Giardino Digitale
---

> [!premessa]+ Premessa
> 
> Ciao! Se è la prima volta che capiti su questo sito, ti consiglio di consultare la [pagina principale](index.md) di questo cosiddetto _Giardino Digitale_ per scoprire meglio cos'è e come navigarlo.
> 
> Lo stato di questa nota è al momento: 🟢 <font color="#7FFF7F">_Completa_</font>.

Stai creando un tuo Giardino Digitale in cui vuoi inserire una funzionalità presente nel mio? Sei nel posto giusto!

Man mano che modifico le impostazioni di questo Giardino Digitale discostandomi dal template di default, segno qua tutto ciò che faccio, anche con l'obiettivo di facilitare il lavoro al me del futuro nel caso in cui ci sia bisogno di ricreare da zero il repository.

Nel caso in cui non ti fosse chiaro quello che spiego qua in questa nota, puoi direttamente consultare il codice sorgente del sito andando sul [repository](https://forgejo.it/Rexus752/digital-garden).

# 1 - Punto di partenza

Come punto di partenza c'è, ovviamente, la creazione del giardino digitale a partire dal template di default che Quartz offre. La versione di Quartz che sto usando al momento in cui sto scrivendo questa nota è la `5.0.0`. Eventualmente, nel futuro, aggiornerò Quartz a versioni successive e, se si dovesse rompere qualcosa, specificherò qua come sistemarlo.

Le istruzioni su come costruire e impostare inizialmente un giardino digitale si trovano nella [home page di Quartz](https://quartz.jzhao.xyz/#-get-started).

Qua sotto riporto un paio di problemini che ho riscontrato durante l'installazione di Quartz:

> [!attenzione]+ Attenzione: errore nel cloning del repository
> 
> Se durante il cloning del repository (cioè dopo aver eseguito il comando `git clone https://github.com/jackyzha0/quartz.git`) esce il seguente messaggio
> 
> ```shell
> error: RPC failed; curl 92 HTTP/2 stream 5 was not closed cleanly: CANCEL (err 8)
> error: 40 bytes of body are still expected
> fetch-pack: unexpected disconnect while reading sideband packet
> fatal: early EOF
> fatal: fetch-pack: invalid index-pack output
> ```
> 
> basta rieseguire di nuovo questo comando, perché significa che c'è stato un errore di connessione durante l'operazione.

> [!attenzione]+ Attenzione: errore nell'esecuzione di `npm i`
> 
> Se durante l'installazione di Quartz, dopo aver eseguito il comando `npm i`, esce un errore del tipo
> 
> ```shell
> added 526 packages, and audited 528 packages in 9s
> 
> 173 packages are looking for funding
>   run npm fund for details
> 
> 3 vulnerabilities (2 moderate, 1 high)
> 
> To address all issues, run:
>   npm audit fix
> 
> Run npm audit for details.
> ```
> 
> allora eseguire il comando `npm audit fix` per risolvere.

# 2 - Configurazione

Ecco quindi tutte le modifiche che ho applicato al sito per personalizzarlo.

## 2.1 - Configurazione generale

Nel file `quartz.config.yaml` ho configurato queste impostazioni generali:
- `pageTitle: 🪴 Giardino Digitale di Rexus752`: titolo del Giardino Digitale che compare sulla sinistra di ogni nota.
- `locale: it-IT`: per impostare la lingua in italiano.
- `baseUrl: rexus752.dev`: URL del sito (anche se in realtà nella mia configurazione non serve a qualcosa in particolare).

La prima parte del file `quartz.config.yaml` risulta così:

```yaml title="quartz.config.yaml" {3, 9, 10}
# yaml-language-server: $schema=./quartz/plugins/quartz-plugins.schema.json
configuration:
  pageTitle: 🪴 Giardino Digitale di Rexus752
  pageTitleSuffix: ""
  enableSPA: true
  enablePopovers: true
  analytics:
    provider: plausible
  locale: it-IT
  baseUrl: rexus752.dev
  ignorePatterns:
    - private
    - templates
    - .obsidian
```

## 2.2 - Tema

Ho disabilitato il plugin dei temi perché mi creava problemi nella personalizzazione dell'interfaccia sovrascrivendo le modifiche che provavo ad apportare (e anche perché il tema `default` che mi sceglie lui fa cacare al cazzo rispetto a quello originale di Quartz che stai vedendo ora):

```yaml title="quartz.config.yaml" showLineNumbers{259}
#  - source:
#      name: quartz-themes
#      repo: github:saberzero1/quartz-themes
#      subdir: plugin
#    enabled: true
#    options:
#      theme: default
```

## 2.2 - Font

In questo sito:
- Per i _body_ (cioè il testo normale come questo che stai leggendo) uso il typeface Inter%% link %%, ossia lo stesso che GNOME%% link %% usa di default a partire dalla versione 47 e che io reputo uno dei migliori sulla piazza al momento (è anche completamente gratuito!).
- Per il codice, uso il typeface Fira Code%% link %%, studiato appositamente per creare _legature_, cioè unioni tra due o più glifi (simboli, lettere, ecc.). Per esempio, se scrivo due volte di fila `=`, Fira Code mi mostra un unico segno: `==`.

Per usare questi font, ho modificato il file `quartz.config.yaml` in questo modo:

```yaml title="quartz.config.yaml" showLineNumbers{15} {6, 7}
  theme:
    fontOrigin: googleFonts
    cdnCaching: true
    typography:
      header: Schibsted Grotesk
      body: Inter
      code: Fira Code
```

## 2.3 - File system

Il mio Giardino Digitale contiene note divise per cartelle a seconda dell'argomento di cui trattano. Ogni cartella ha una nota associata e le relative sotto-cartelle e sotto-note comprese in quell'argomento.

Per esempio, la cartella `Matematica` contiene la nota `Matematica.md` che fa da introduzione a quell'argomento e le sue sotto-cartelle come `Teoria degli insiemi` che a sua volta avrà la sua nota principale:

```
📂 Matematica/
├── 🗒 Matematica.md
├── 🗒 Analisi.md
└── 📂 Teoria degli insiemi/
    └── 🗒 Teoria degli insiemi.md
```

Problemino: Quartz%% link %% genera delle pagine web non solo per le note, ma anche per le cartelle stesse (nella pagina della cartella ti inserisce i link alle note contenute nella cartella). Ciò significa che, per esempio, la nota `Matematica.md` è disponibile al percorso `./Matematica/Matematica.md`, perché al percorso `./Matematica` apre la pagina della cartella Matematica%% link %%.

Per ovviare a questo problema, Quartz offre già a priori una soluzione: nella cartella desiderata, si può rinominare la sua "nota associata" in `_index.md` o `index.md` in modo da sostituirla alla nota della cartella. Il titolo della nota lo prende dalla proprietà `title` inserita nel frontmatter della nota.

> [!attenzione]+ Attenzione: `_index.md` o `index.md`?
> 
> Riguardo quest'ultima cosa, sono stato costretto a scegliere `_index.md` come nome di default per le note associate alle cartelle, perché `index.md` l'ho riservato alla nota della homepage del sito (cioè `content/index.md`). Ho dovuto fare così perché, in questo modo, nelle premesse delle note posso mettere un link che reindirizza semplicemente all'unica nota che in tutto il vault di Obsidian ha come nome `index.md`, ossia proprio `content/index.md`. Se anche questa nota avesse come nome `_index.md`, Obsidian "forza" a inserire come percorso nell'hyperlink il percorso `content/_index.md`, generando il problema per cui, sul sito, questo hyperlink rimanda alla nota `https://rexus752.github.io/digital-garden/content/_index.md` che non esiste.

Quindi, nella cartella `Matematica`, la nota `Matematica.md` diventa `_index.md` e, quando nell'Esplora sul lato della pagina cliccherò su `Matematica`, non mi porterà alla pagina della cartella, ma a quella della nota `Matematica.md`.

Il risultato è il seguente:

```
📂 Matematica/
├── 🗒 _index.md
├── 🗒 Analisi.md
└── 📂 Teoria degli insiemi/
    └── 🗒 _index.md
```

Per evitare che comunque le pagine associate delle cartelle mostrino sotto il contenuto della nota associata anche il contenuto della cartella, ho dovuto modificare il codice SCSS del sito perché non capivo come modificarlo dalle impostazioni del plugin, dato che le opzioni che il [plugin `FolderPage`](https://quartz.jzhao.xyz/plugins/folderpage) mette a disposizione non mi permette di disabilitarlo in toto e, se provo ad eliminarlo direttamente dal `quartz.config.yaml`, mi disabilita proprio l'intera pagina.

Per modificare il codice SCSS, Quartz%% link %% mette a disposizione il file `custom.scss` nella cartella `quartz/styles` per scriverci le proprie modifiche. In nome del sacro principio della _modularità del codice_%% link %%, ho inserito questa modifica in un file `disable-folder-page.scss` in una sotto-cartella `custom` della cartella `quartz/styles` che, appunto, conterrà tutte le varie modifiche da applicare all'SCSS del sito.

Quindi, nel file `disable-folder-page.scss` in `quartz/styles/custom` ci ho scritto questo:

```scss title="quartz/styles/custom/disable-folder-page.scss"
.page-listing {
  display: none;
}
```

E, per dire a Quartz di leggere questo file, nel file `custom.scss` nella cartella `quartz/styles` ci ho scritto ciò:

```scss title="quartz/styles/custom.scss" {3}
@use "./base.scss";

@use "./custom/disable-folder-page.scss";
```

## 2.4 - Layout delle note

Nel file `quartz.config.yaml` ho modificato il layout delle note, cioè la struttura della nota. Ecco ciò che ho fatto:
- Nei link nel footer ci ho messo il link al repository e al mio Linktree%% link %%:
	```yaml title="quartz.config.yaml" showLineNumbers{222} {5, 6}
  - source: github:quartz-community/footer
    enabled: true
    options:
      links:
        Repository: https://forgejo.it/Rexus752/digital-garden.git
        Il mio Linktree: https://linktr.ee/rexus752
	```
- Per fare in modo che anche nelle _folder page_ (cioè nelle pagine-cartelle come [Matematica](content/Matematica/_index.md)) escano tutti i componenti come l'indice, ho modificato le impostazioni del `layout` che si possono trovare in fondo al `quartz.config.yaml`:
	```yaml title="quartz.config.yaml" showLineNumbers{273} {13}
	layout:
	  groups:
	    toolbar:
	      priority: 35
	      direction: row
	      gap: 0.5rem
	  byPageType:
	    "404":
	      positions:
	        beforeBody: []
	        left: []
	        right: []
	    content: {}
	    folder: {}
	    tag:
	      exclude:
	        - reader-mode
	      positions:
	        right: []
	    canvas: {}
	    bases: {}
	```
- Nel layout delle pagine ho rimosso i _backlinks_, cambiando in `false` il valore di `enabled` tra le opzioni del [plugin `Backlinks`](https://quartz.jzhao.xyz/plugins/backlinks) in `quartz-config.yaml`:
	```yaml title="quartz.config.yaml" showLineNumbers{171} {2}
	  - source: github:quartz-community/backlinks
	    enabled: false
	    layout:
	      position: right
	      priority: 50
	```

- Nel layout delle pagine ho anche rimosso anche i _graph view_, che per quanto possano essere carini sono comunque inutili:
```yaml title="quartz.config.yaml" showLineNumbers{158} {2}
  - source: github:quartz-community/graph
    enabled: false
    layout:
      position: right
      priority: 10
```

## 2.5 - Icona personalizzata

Nella cartella `quartz/static` ho sostituito il file `icon.png` con una mia icona personalizzata, che è appunto l'icona di questo Giardino Digitale:

![Icona Giardino Digitale](Icona%20Giardino%20Digitale.png)

Questa l'ho creata attraverso il [generatore sul sito ufficiale di Obsidian](https://obsidian.md/blog/new-obsidian-icon/) che ti permette di personalizzare la nuova icona di Obsidian adottata nel 2023 con i tuoi colori. Io ho usato gli stessi colori della mia classica immagine di profilo che uso ovunque, ossia quella di Patrick con il cervello esploso:

![Immagine di profilo](Immagine%20di%20profilo.png)

Ne ho approfittato anche per sostituire con questa icona il file `og-image.png`, sempre nella cartella `quartz/static`, che è la foto che compare nelle preview del Giardino Digitale quando si inserisce il link in un messaggio:

![Preview link Giardino Digitale|400](Preview%20link%20Giardino%20Digitale.png)

Facendo ciò ho anche disabilitato il [plugin Custom OG Images](https://quartz.jzhao.xyz/plugins/CustomOgImages) nel file `quartz.config.yaml`, che è il plugin che si occupa di generare delle preview uniche per ogni nota del sito (e che, in realtà, rallenta anche il tempo di _build_ del sito):

```yaml title="quartz.config.yaml" showLineNumbers{142} {2}
  - source: github:quartz-community/og-image
    enabled: false
```

# DA QUI IN POI STO FINENDO DI AGGIORNARLO ALLA VERSIONE 5 DI QUARTZ

## 2.6 - Modalità scura di default

Nel mio Giardino Digitale, per questione di comodità, ho scelto di inserire la modalità scura di default e tolto la possibilità di passare alla modalità chiara. Ciò l'ho fatto perché io in primis, quando scrivo le mie note su Obsidian, uso la modalità scura, e di conseguenza anche tutti i contenuti che ho inserito nelle note come le foto o gli schemi sono adattati a questo tema. Mantenere la possibilità di passare alla modalità chiara significherebbe dover  creare un sistema per cui anche queste foto debbano adattarsi alla modalità chiara, cosa che non ho assolutamente intenzione di fare lol.

Impostare la modalità scura di default sul sito è un bel casino, ci ho messo un bel po' per capire come straminghie farlo, ma alla fine ho scelto l'opzione più stupida e più diretta per realizzarlo: nel file `quartz.config.ts` ho scambiato di posto le parole `lightMode` e `darkMode`:

```typescript title="quartz.config.ts" {2,13}
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

Per applicare la modalità scura fissa anche nel syntax highlighting%% link %% (cioè il colore nel codice) ho modificato le impostazioni del relativo plugin%% link %% che si possono trovare in `quartz.config.ts`, semplicemente scambiando i valori `github-light` e `github-dark`:

```typescript title="quartz.config.ts" {3,4}
Plugin.SyntaxHighlighting({
    theme: {
        light: "github-dark",
        dark: "github-light",
    },
}),
```

Per quanto riguarda invece i diagrammi Mermaid%% link %%, questi sono inclusi in tutto ciò che riguarda la [compatibilità di Quartz con Obsidian](https://quartz.jzhao.xyz/features/Obsidian-compatibility) e, di conseguenza, sono gestiti dal plugin [ObsidianFlavoredMarkdown](https://quartz.jzhao.xyz/plugins/ObsidianFlavoredMarkdown).

Per invertire i colori anche nei diagrammi, non so come si possa fare ora nelle ultime versioni di Quartz (e per questo proverò ad astenermi dall'usare i diagrammi Mermaid nel sito, altrimenti sembrano uno schifo i diagrammi in modalità chiara con il resto del sito in modalità scura). Se può essere utile saperlo per trovare magari una soluzione, posso dirti che nella versione 4.4 di Quartz, nel file `quartz/plugins/transformers/ofm.ts`, approssimativamente alla riga 695, bisognava scambiare i valori `'dark'` e `'default'`:

```typescript title="quartz/plugins/transformers/ofm.ts" {11}
script: `
let mermaidImport = undefined
document.addEventListener('nav', async () => {
if (document.querySelector("code.mermaid")) {
  mermaidImport |\vDash await import('https://cdnjs.cloudflare.com/ajax/libs/mermaid/10.7.0/mermaid.esm.min.mjs')
  const mermaid = mermaidImport.default
  const darkMode = document.documentElement.getAttribute('saved-theme') === 'dark'
  mermaid.initialize({
    startOnLoad: false,
    securityLevel: 'loose',
    theme: darkMode ? 'default' : 'dark'
  })

  await mermaid.run({
    querySelector: '.mermaid'
  })
}
});
`,
```

Infine, ho rimosso il pulsante per passare dalla modalità chiara a quella scura e viceversa in `quartz.layout.ts`, sia in `defaultContentPageLayout` che in `defaultListPageLayout`:

```typescript title="quartz.layout.ts" {14, 36}
export const defaultContentPageLayout: PageLayout = {
  beforeBody: [
    // ...
  ],
  left: [
    Component.PageTitle(),
    Component.MobileOnly(Component.Spacer()),
    Component.Flex({
      components: [
        {
          Component: Component.Search(),
          grow: true,
        },
        // { Component: Component.Darkmode() },
        { Component: Component.ReaderMode() },
      ],
    }),
    Component.Explorer(),
  ],
  right: [
    // ...
  ],
}

export const defaultListPageLayout: PageLayout = {
  beforeBody: [Component.Breadcrumbs(), Component.ArticleTitle(), Component.ContentMeta()],
  left: [
    Component.PageTitle(),
    Component.MobileOnly(Component.Spacer()),
    Component.Flex({
      components: [
        {
          Component: Component.Search(),
          grow: true,
        },
        // { Component: Component.Darkmode() },
      ],
    }),
    Component.Explorer(),
  ],
  right: [
    // ...
  ],
}
```

## 2.7 - Foto centrate

Esattamente come avrai potuto notare con quelle che ho inserito qua sopra, le foto vengono automaticamente centrate nel mezzo della pagina.

Ciò si può fare modificando il codice SCSS del sito, infatti Quartz%% link %% mette a disposizione il file `custom.scss` nella cartella `quartz/styles` per scriverci le proprie modifiche.

In nome del sacro principio della _modularità del codice_%% link %%, ho inserito questa modifica in un file `centered-photos.scss` in una sotto-cartella `custom` della cartella `quartz/styles` che, appunto, conterrà tutte le varie modifiche da applicare all'SCSS del sito.

Quindi, nel file `centered-photos.scss` in `quartz/styles/custom` ci ho scritto questo:

```scss title="quartz/styles/custom/centered-photos.scss"
img {
  display: block;
  margin: auto;
}
```

E, per dire a Quartz di leggere questo file, nel file `custom.scss` nella cartella `quartz/styles` ci ho scritto ciò:

```scss title="quartz/styles/custom.scss" {3}
@use "./base.scss";

@use "./custom/centered-photos.scss";
```

## 2.8 - Callout personalizzati

All'interno del mio Giardino Digitale, uso diversi callout%% link %% personalizzati, descritti attraverso codice SCSS. Tutti i callout che ho aggiunto sono inseriti nel file `callouts.scss` nella cartella `quartz/styles/custom` col seguente formato:

```scss title="quartz/styles/custom/callouts.scss"
.callout {
  &[data-callout="<name>"] {
    --color: #<color>;
    --border: #<border color>;
    --bg: #<background color>;
    --callout-icon: url("data:image/svg+xml; utf8, <URL-encoded SVG>");
  }

  &[data-callout="<name>"] {
    --color: #<color>;
    --border: #<border color>;
    --bg: #<background color>;
    --callout-icon: url("data:image/svg+xml; utf8, <URL-encoded SVG>");
  }
}
```

Ovviamente, il file `quartz/styles/custom.scss` dovrà importare `callouts.scss`:

```scss title="quartz/styles/custom.scss" {4}
@use "./base.scss";

@use "./custom/centered-photos.scss";
@use "./custom/callouts.scss";
```

Sul [sito di Quartz](https://quartz.jzhao.xyz/features/callouts) viene spiegato come aggiungerne di nuovi. Io, per aggiungere nuovi callout, uso questo metodo:
- Cerco una possibile icona su [FontAwesome](https://fontawesome.com/).
- Copio il codice SVG.
- Lo converto in URL tramite questo [URL-encoder per SVG](https://yoksel.github.io/url-encoder/).
- Lo aggiungo nel file `callouts.scss` sostituendo la stringa `<URL-encoded SVG>{:typescript}` con quella appena copiata.

Qua sotto ho inserito una lista dei callout che uso, ognuno dei quali ha al proprio interno il codice SCSS per impostarlo (clicca sulla freccetta affianco al titolo del callout per espanderlo).

### 2.8.1 - Generici

> [!premessa]+ Premessa
> 
> ```scss
> &[data-callout="premessa"] {
>   --color: #FFFFFF;
>   --border: #FFFFFF3F;
>   --bg: #FFFFFF1F;
>   --callout-icon: url("data:image/svg+xml; utf8, %3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 512 512'%3E%3C!--!Font Awesome Free 6.7.2 by @fontawesome - https://fontawesome.com License - https://fontawesome.com/license/free Copyright 2025 Fonticons, Inc.--%3E%3Cpath d='M256 512A256 256 0 1 0 256 0a256 256 0 1 0 0 512zM216 336l24 0 0-64-24 0c-13.3 0-24-10.7-24-24s10.7-24 24-24l48 0c13.3 0 24 10.7 24 24l0 88 8 0c13.3 0 24 10.7 24 24s-10.7 24-24 24l-80 0c-13.3 0-24-10.7-24-24s10.7-24 24-24zm40-208a32 32 0 1 1 0 64 32 32 0 1 1 0-64z'/%3E%3C/svg%3E");
> }
> ```

> [!fonti]+ Fonti
> 
> ```scss
> &[data-callout="fonti"] {
>   --color: #FFFFFF;
>   --border: #FFFFFF3F;
>   --bg: #FFFFFF1F;
>   --callout-icon: url("data:image/svg+xml; utf8, %3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 512 512'%3E%3C!--!Font Awesome Free 6.7.2 by @fontawesome - https://fontawesome.com License - https://fontawesome.com/license/free Copyright 2025 Fonticons, Inc.--%3E%3Cpath d='M256 512A256 256 0 1 0 256 0a256 256 0 1 0 0 512zM216 336l24 0 0-64-24 0c-13.3 0-24-10.7-24-24s10.7-24 24-24l48 0c13.3 0 24 10.7 24 24l0 88 8 0c13.3 0 24 10.7 24 24s-10.7 24-24 24l-80 0c-13.3 0-24-10.7-24-24s10.7-24 24-24zm40-208a32 32 0 1 1 0 64 32 32 0 1 1 0-64z'/%3E%3C/svg%3E");
> }
> ```

> [!esempio]- Esempio
> 
> ```scss
> &[data-callout="esempio"] {
>   --color: #7F7FFF;
>   --border: #7F7FFF3F;
>   --bg: #7F7FFF1F;
>   --callout-icon: url("data:image/svg+xml; utf8, %3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 512 512'%3E%3C!--!Font Awesome Free 6.7.1 by @fontawesome - https://fontawesome.com License - https://fontawesome.com/license/free Copyright 2024 Fonticons, Inc.--%3E%3Cpath d='M410.3 231l11.3-11.3-33.9-33.9-62.1-62.1L291.7 89.8l-11.3 11.3-22.6 22.6L58.6 322.9c-10.4 10.4-18 23.3-22.2 37.4L1 480.7c-2.5 8.4-.2 17.5 6.1 23.7s15.3 8.5 23.7 6.1l120.3-35.4c14.1-4.2 27-11.8 37.4-22.2L387.7 253.7 410.3 231zM160 399.4l-9.1 22.7c-4 3.1-8.5 5.4-13.3 6.9L59.4 452l23-78.1c1.4-4.9 3.8-9.4 6.9-13.3l22.7-9.1 0 32c0 8.8 7.2 16 16 16l32 0zM362.7 18.7L348.3 33.2 325.7 55.8 314.3 67.1l33.9 33.9 62.1 62.1 33.9 33.9 11.3-11.3 22.6-22.6 14.5-14.5c25-25 25-65.5 0-90.5L453.3 18.7c-25-25-65.5-25-90.5 0zm-47.4 168l-144 144c-6.2 6.2-16.4 6.2-22.6 0s-6.2-16.4 0-22.6l144-144c6.2-6.2 16.4-6.2 22.6 0s6.2 16.4 0 22.6z'/%3E%3C/svg%3E");
> }
> ```

> [!osservazione]+ Osservazione
> 
> ```scss
> &[data-callout="osservazione"] {
>   --color: #7F7F7F;
>   --border: #7F7F7F3F;
>   --bg: #7F7F7F1F;
>   --callout-icon: url("data:image/svg+xml; utf8, %3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 576 512'%3E%3C!--!Font Awesome Free 6.7.1 by @fontawesome - https://fontawesome.com License - https://fontawesome.com/license/free Copyright 2024 Fonticons, Inc.--%3E%3Cpath d='M118.6 80c-11.5 0-21.4 7.9-24 19.1L57 260.3c20.5-6.2 48.3-12.3 78.7-12.3c32.3 0 61.8 6.9 82.8 13.5c10.6 3.3 19.3 6.7 25.4 9.2c3.1 1.3 5.5 2.4 7.3 3.2c.9 .4 1.6 .7 2.1 1l.6 .3 .2 .1c0 0 .1 0 .1 0c0 0 0 0 0 0s0 0 0 0L247.9 288s0 0 0 0l6.3-12.7c5.8 2.9 10.4 7.3 13.5 12.7l40.6 0c3.1-5.3 7.7-9.8 13.5-12.7l6.3 12.7s0 0 0 0c-6.3-12.7-6.3-12.7-6.3-12.7s0 0 0 0s0 0 0 0c0 0 .1 0 .1 0l.2-.1 .6-.3c.5-.2 1.2-.6 2.1-1c1.8-.8 4.2-1.9 7.3-3.2c6.1-2.6 14.8-5.9 25.4-9.2c21-6.6 50.4-13.5 82.8-13.5c30.4 0 58.2 6.1 78.7 12.3L481.4 99.1c-2.6-11.2-12.6-19.1-24-19.1c-3.1 0-6.2 .6-9.2 1.8L416.9 94.3c-12.3 4.9-26.3-1.1-31.2-13.4s1.1-26.3 13.4-31.2l31.3-12.5c8.6-3.4 17.7-5.2 27-5.2c33.8 0 63.1 23.3 70.8 56.2l43.9 188c1.7 7.3 2.9 14.7 3.5 22.1c.3 1.9 .5 3.8 .5 5.7l0 6.7 0 41.3 0 16c0 61.9-50.1 112-112 112l-44.3 0c-59.4 0-108.5-46.4-111.8-105.8L306.6 352l-37.2 0-1.2 22.2C264.9 433.6 215.8 480 156.3 480L112 480C50.1 480 0 429.9 0 368l0-16 0-41.3L0 304c0-1.9 .2-3.8 .5-5.7c.6-7.4 1.8-14.8 3.5-22.1l43.9-188C55.5 55.3 84.8 32 118.6 32c9.2 0 18.4 1.8 27 5.2l31.3 12.5c12.3 4.9 18.3 18.9 13.4 31.2s-18.9 18.3-31.2 13.4L127.8 81.8c-2.9-1.2-6-1.8-9.2-1.8zM64 325.4L64 368c0 26.5 21.5 48 48 48l44.3 0c25.5 0 46.5-19.9 47.9-45.3l2.5-45.6c-2.3-.8-4.9-1.7-7.5-2.5c-17.2-5.4-39.9-10.5-63.6-10.5c-23.7 0-46.2 5.1-63.2 10.5c-3.1 1-5.9 1.9-8.5 2.9zM512 368l0-42.6c-2.6-.9-5.5-1.9-8.5-2.9c-17-5.4-39.5-10.5-63.2-10.5c-23.7 0-46.4 5.1-63.6 10.5c-2.7 .8-5.2 1.7-7.5 2.5l2.5 45.6c1.4 25.4 22.5 45.3 47.9 45.3l44.3 0c26.5 0 48-21.5 48-48z'/%3E%3C/svg%3E");
> }
> ```

> [!trucco]+ Trucco
> 
> ```scss
> &[data-callout="trucco"] {
>   --color: #FFFFFF;
>   --border: #FFFFFF3F;
>   --bg: #FFFFFF1F;
>   --callout-icon: url("data:image/svg+xml; utf8, %3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 576 512'%3E%3C!--!Font Awesome Free 6.7.1 by @fontawesome - https://fontawesome.com License - https://fontawesome.com/license/free Copyright 2024 Fonticons, Inc.--%3E%3Cpath d='M234.7 42.7L197 56.8c-3 1.1-5 4-5 7.2s2 6.1 5 7.2l37.7 14.1L248.8 123c1.1 3 4 5 7.2 5s6.1-2 7.2-5l14.1-37.7L315 71.2c3-1.1 5-4 5-7.2s-2-6.1-5-7.2L277.3 42.7 263.2 5c-1.1-3-4-5-7.2-5s-6.1 2-7.2 5L234.7 42.7zM46.1 395.4c-18.7 18.7-18.7 49.1 0 67.9l34.6 34.6c18.7 18.7 49.1 18.7 67.9 0L529.9 116.5c18.7-18.7 18.7-49.1 0-67.9L495.3 14.1c-18.7-18.7-49.1-18.7-67.9 0L46.1 395.4zM484.6 82.6l-105 105-23.3-23.3 105-105 23.3 23.3zM7.5 117.2C3 118.9 0 123.2 0 128s3 9.1 7.5 10.8L64 160l21.2 56.5c1.7 4.5 6 7.5 10.8 7.5s9.1-3 10.8-7.5L128 160l56.5-21.2c4.5-1.7 7.5-6 7.5-10.8s-3-9.1-7.5-10.8L128 96 106.8 39.5C105.1 35 100.8 32 96 32s-9.1 3-10.8 7.5L64 96 7.5 117.2zm352 256c-4.5 1.7-7.5 6-7.5 10.8s3 9.1 7.5 10.8L416 416l21.2 56.5c1.7 4.5 6 7.5 10.8 7.5s9.1-3 10.8-7.5L480 416l56.5-21.2c4.5-1.7 7.5-6 7.5-10.8s-3-9.1-7.5-10.8L480 352l-21.2-56.5c-1.7-4.5-6-7.5-10.8-7.5s-9.1 3-10.8 7.5L416 352l-56.5 21.2z'/%3E%3C/svg%3E");
> }
> ```

> [!consiglio]+ Consiglio
> 
> ```scss
> &[data-callout="consiglio"] {
>   --color: #3FBFFF;
>   --border: #3FBFFF3F;
>   --bg: #3FBFFF1F;
>   --callout-icon: url("data:image/svg+xml; utf8, %3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 384 512'%3E%3C!--!Font Awesome Free 6.7.2 by @fontawesome - https://fontawesome.com License - https://fontawesome.com/license/free Copyright 2025 Fonticons, Inc.--%3E%3Cpath d='M153.6 29.9l16-21.3C173.6 3.2 180 0 186.7 0C198.4 0 208 9.6 208 21.3V43.5c0 13.1 5.4 25.7 14.9 34.7L307.6 159C356.4 205.6 384 270.2 384 337.7C384 434 306 512 209.7 512H192C86 512 0 426 0 320v-3.8c0-48.8 19.4-95.6 53.9-130.1l3.5-3.5c4.2-4.2 10-6.6 16-6.6C85.9 176 96 186.1 96 198.6V288c0 35.3 28.7 64 64 64s64-28.7 64-64v-3.9c0-18-7.2-35.3-19.9-48l-38.6-38.6c-24-24-37.5-56.7-37.5-90.7c0-27.7 9-54.8 25.6-76.9z'/%3E%3C/svg%3E");
> }
> ```

> [!attenzione]+ Attenzione
> 
> ```scss
> &[data-callout="attenzione"] {
>   --color: #FFBF7F;
>   --border: #FFBF7F3F;
>   --bg: #FFBF7F1F;
>   --callout-icon: url("data:image/svg+xml; utf8, %3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 512 512'%3E%3C!--!Font Awesome Free 6.7.2 by @fontawesome - https://fontawesome.com License - https://fontawesome.com/license/free Copyright 2025 Fonticons, Inc.--%3E%3Cpath d='M256 32c14.2 0 27.3 7.5 34.5 19.8l216 368c7.3 12.4 7.3 27.7 .2 40.1S486.3 480 472 480L40 480c-14.3 0-27.6-7.7-34.7-20.1s-7-27.8 .2-40.1l216-368C228.7 39.5 241.8 32 256 32zm0 128c-13.3 0-24 10.7-24 24l0 112c0 13.3 10.7 24 24 24s24-10.7 24-24l0-112c0-13.3-10.7-24-24-24zm32 224a32 32 0 1 0 -64 0 32 32 0 1 0 64 0z'/%3E%3C/svg%3E");
> }
> ```

> [!esercizio]+ Esercizio
> 
> ```scss
> &[data-callout="esercizio"] {
>   --color: #FFFFFF;
>   --border: #FFFFFF3F;
>   --bg: #FFFFFF1F;
>   --callout-icon: url("data:image/svg+xml; utf8, %3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 640 512'%3E%3C!--!Font Awesome Free 6.7.2 by @fontawesome - https://fontawesome.com License - https://fontawesome.com/license/free Copyright 2025 Fonticons, Inc.--%3E%3Cpath d='M96 64c0-17.7 14.3-32 32-32l32 0c17.7 0 32 14.3 32 32l0 160 0 64 0 160c0 17.7-14.3 32-32 32l-32 0c-17.7 0-32-14.3-32-32l0-64-32 0c-17.7 0-32-14.3-32-32l0-64c-17.7 0-32-14.3-32-32s14.3-32 32-32l0-64c0-17.7 14.3-32 32-32l32 0 0-64zm448 0l0 64 32 0c17.7 0 32 14.3 32 32l0 64c17.7 0 32 14.3 32 32s-14.3 32-32 32l0 64c0 17.7-14.3 32-32 32l-32 0 0 64c0 17.7-14.3 32-32 32l-32 0c-17.7 0-32-14.3-32-32l0-160 0-64 0-160c0-17.7 14.3-32 32-32l32 0c17.7 0 32 14.3 32 32zM416 224l0 64-192 0 0-64 192 0z'/%3E%3C/svg%3E");
> }
> ```

> [!soluzione]- Soluzione
> 
> ```scss
> &[data-callout="soluzione"] {
>   --color: #7F7F7F;
>   --border: #7F7F7F3F;
>   --bg: #7F7F7F1F;
>   --callout-icon: url("data:image/svg+xml; utf8, %3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 384 512'%3E%3C!--!Font Awesome Free 6.7.2 by @fontawesome - https://fontawesome.com License - https://fontawesome.com/license/free Copyright 2025 Fonticons, Inc.--%3E%3Cpath d='M297.2 248.9C311.6 228.3 320 203.2 320 176c0-70.7-57.3-128-128-128S64 105.3 64 176c0 27.2 8.4 52.3 22.8 72.9c3.7 5.3 8.1 11.3 12.8 17.7c0 0 0 0 0 0c12.9 17.7 28.3 38.9 39.8 59.8c10.4 19 15.7 38.8 18.3 57.5L109 384c-2.2-12-5.9-23.7-11.8-34.5c-9.9-18-22.2-34.9-34.5-51.8c0 0 0 0 0 0s0 0 0 0c-5.2-7.1-10.4-14.2-15.4-21.4C27.6 247.9 16 213.3 16 176C16 78.8 94.8 0 192 0s176 78.8 176 176c0 37.3-11.6 71.9-31.4 100.3c-5 7.2-10.2 14.3-15.4 21.4c0 0 0 0 0 0s0 0 0 0c-12.3 16.8-24.6 33.7-34.5 51.8c-5.9 10.8-9.6 22.5-11.8 34.5l-48.6 0c2.6-18.7 7.9-38.6 18.3-57.5c11.5-20.9 26.9-42.1 39.8-59.8c0 0 0 0 0 0s0 0 0 0s0 0 0 0c4.7-6.4 9-12.4 12.7-17.7zM192 128c-26.5 0-48 21.5-48 48c0 8.8-7.2 16-16 16s-16-7.2-16-16c0-44.2 35.8-80 80-80c8.8 0 16 7.2 16 16s-7.2 16-16 16zm0 384c-44.2 0-80-35.8-80-80l0-16 160 0 0 16c0 44.2-35.8 80-80 80z'/%3E%3C/svg%3E");
> }
> ```

> [!vantaggi]+ Vantaggi
> 
> ```scss
> &[data-callout="vantaggi"] {
>   --color: #7FFF7F;
>   --border: #7FFF7F3F;
>   --bg: #7FFF7F1F;
>   --callout-icon: url("data:image/svg+xml; utf8, %3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 320 512'%3E%3C!--!Font Awesome Free 6.7.2 by @fontawesome - https://fontawesome.com License - https://fontawesome.com/license/free Copyright 2025 Fonticons, Inc.--%3E%3Cpath d='M318 177.5c3.8-8.8 2-19-4.6-26l-136-144C172.9 2.7 166.6 0 160 0s-12.9 2.7-17.4 7.5l-136 144c-6.6 7-8.4 17.2-4.6 26S14.4 192 24 192l72 0 0 288c0 17.7 14.3 32 32 32l64 0c17.7 0 32-14.3 32-32l0-288 72 0c9.6 0 18.2-5.7 22-14.5z'/%3E%3C/svg%3E");
> }
> ```

> [!svantaggi]+ Svantaggi
> 
> ```scss
> &[data-callout="svantaggi"] {
>   --color: #FF7F7F;
>   --border: #FF7F7F3F;
>   --bg: #FF7F7F1F;
>   --callout-icon: url("data:image/svg+xml; utf8, %3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 320 512'%3E%3C!--!Font Awesome Free 6.7.2 by @fontawesome - https://fontawesome.com License - https://fontawesome.com/license/free Copyright 2025 Fonticons, Inc.--%3E%3Cpath d='M2 334.5c-3.8 8.8-2 19 4.6 26l136 144c4.5 4.8 10.8 7.5 17.4 7.5s12.9-2.7 17.4-7.5l136-144c6.6-7 8.4-17.2 4.6-26s-12.5-14.5-22-14.5l-72 0 0-288c0-17.7-14.3-32-32-32L128 0C110.3 0 96 14.3 96 32l0 288-72 0c-9.6 0-18.2 5.7-22 14.5z'/%3E%3C/svg%3E");
> }
> ```

### 2.8.2 - Per la matematica

> [!assioma]+ Assioma
> 
> ```scss
> &[data-callout="assioma"] {
>   --color: #BF7FFF;
>   --border: #BF7FFF3F;
>   --bg: #BF7FFF1F;
>   --callout-icon: url("data:image/svg+xml; utf8, %3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 384 512'%3E%3C!--!Font Awesome Free 6.7.2 by @fontawesome - https://fontawesome.com License - https://fontawesome.com/license/free Copyright 2025 Fonticons, Inc.--%3E%3Cpath d='M0 48V487.7C0 501.1 10.9 512 24.3 512c5 0 9.9-1.5 14-4.4L192 400 345.7 507.6c4.1 2.9 9 4.4 14 4.4c13.4 0 24.3-10.9 24.3-24.3V48c0-26.5-21.5-48-48-48H48C21.5 0 0 21.5 0 48z'/%3E%3C/svg%3E");
> }
> ```

> [!definizione]+ Definizione
> 
> ```scss
> &[data-callout="definizione"] {
>   --color: #FF7FFF;
>   --border: #FF7FFF3F;
>   --bg: #FF7FFF1F;
>   --callout-icon: url("data:image/svg+xml; utf8, %3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 448 512'%3E%3C!--!Font Awesome Free 6.7.1 by @fontawesome - https://fontawesome.com License - https://fontawesome.com/license/free Copyright 2024 Fonticons, Inc.--%3E%3Cpath d='M96 0C43 0 0 43 0 96L0 416c0 53 43 96 96 96l288 0 32 0c17.7 0 32-14.3 32-32s-14.3-32-32-32l0-64c17.7 0 32-14.3 32-32l0-320c0-17.7-14.3-32-32-32L384 0 96 0zm0 384l256 0 0 64L96 448c-17.7 0-32-14.3-32-32s14.3-32 32-32zm32-240c0-8.8 7.2-16 16-16l192 0c8.8 0 16 7.2 16 16s-7.2 16-16 16l-192 0c-8.8 0-16-7.2-16-16zm16 48l192 0c8.8 0 16 7.2 16 16s-7.2 16-16 16l-192 0c-8.8 0-16-7.2-16-16s7.2-16 16-16z'/%3E%3C/svg%3E");
> }
> ```

> [!notazione]+ Notazione
> 
> ```scss
> &[data-callout="notazione"] {
>   --color: #7FBFFF;
>   --border: #7FBFFF3F;
>   --bg: #7FBFFF1F;
>   --callout-icon: url("data:image/svg+xml; utf8, %3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 512 512'%3E%3C!--!Font Awesome Free 6.7.2 by @fontawesome - https://fontawesome.com License - https://fontawesome.com/license/free Copyright 2025 Fonticons, Inc.--%3E%3Cpath d='M410.3 231l11.3-11.3-33.9-33.9-62.1-62.1L291.7 89.8l-11.3 11.3-22.6 22.6L58.6 322.9c-10.4 10.4-18 23.3-22.2 37.4L1 480.7c-2.5 8.4-.2 17.5 6.1 23.7s15.3 8.5 23.7 6.1l120.3-35.4c14.1-4.2 27-11.8 37.4-22.2L387.7 253.7 410.3 231zM160 399.4l-9.1 22.7c-4 3.1-8.5 5.4-13.3 6.9L59.4 452l23-78.1c1.4-4.9 3.8-9.4 6.9-13.3l22.7-9.1 0 32c0 8.8 7.2 16 16 16l32 0zM362.7 18.7L348.3 33.2 325.7 55.8 314.3 67.1l33.9 33.9 62.1 62.1 33.9 33.9 11.3-11.3 22.6-22.6 14.5-14.5c25-25 25-65.5 0-90.5L453.3 18.7c-25-25-65.5-25-90.5 0zm-47.4 168l-144 144c-6.2 6.2-16.4 6.2-22.6 0s-6.2-16.4 0-22.6l144-144c6.2-6.2 16.4-6.2 22.6 0s6.2 16.4 0 22.6z'/%3E%3C/svg%3E");
> }
> ```

> [!teorema]+ Teorema
> 
> ```scss
> &[data-callout="teorema"] {
>   --color: #FF3F3F;
>   --border: #FF3F3F3F;
>   --bg: #FF3F3F1F;
>   --callout-icon: url("data:image/svg+xml; utf8, %3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 320 512'%3E%3C!--!Font Awesome Free 6.7.1 by @fontawesome - https://fontawesome.com License - https://fontawesome.com/license/free Copyright 2024 Fonticons, Inc.--%3E%3Cpath d='M80 160c0-35.3 28.7-64 64-64l32 0c35.3 0 64 28.7 64 64l0 3.6c0 21.8-11.1 42.1-29.4 53.8l-42.2 27.1c-25.2 16.2-40.4 44.1-40.4 74l0 1.4c0 17.7 14.3 32 32 32s32-14.3 32-32l0-1.4c0-8.2 4.2-15.8 11-20.2l42.2-27.1c36.6-23.6 58.8-64.1 58.8-107.7l0-3.6c0-70.7-57.3-128-128-128l-32 0C73.3 32 16 89.3 16 160c0 17.7 14.3 32 32 32s32-14.3 32-32zm80 320a40 40 0 1 0 0-80 40 40 0 1 0 0 80z'/%3E%3C/svg%3E");
> }
> ```

> [!proposizione]+ Proposizione
> 
> ```scss
> &[data-callout="proposizione"] {
>   --color: #FF7F7F;
>   --border: #FF7F7F3F;
>   --bg: #FF7F7F1F;
>   --callout-icon: url("data:image/svg+xml; utf8, %3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 320 512'%3E%3C!--!Font Awesome Free 6.7.1 by @fontawesome - https://fontawesome.com License - https://fontawesome.com/license/free Copyright 2024 Fonticons, Inc.--%3E%3Cpath d='M80 160c0-35.3 28.7-64 64-64l32 0c35.3 0 64 28.7 64 64l0 3.6c0 21.8-11.1 42.1-29.4 53.8l-42.2 27.1c-25.2 16.2-40.4 44.1-40.4 74l0 1.4c0 17.7 14.3 32 32 32s32-14.3 32-32l0-1.4c0-8.2 4.2-15.8 11-20.2l42.2-27.1c36.6-23.6 58.8-64.1 58.8-107.7l0-3.6c0-70.7-57.3-128-128-128l-32 0C73.3 32 16 89.3 16 160c0 17.7 14.3 32 32 32s32-14.3 32-32zm80 320a40 40 0 1 0 0-80 40 40 0 1 0 0 80z'/%3E%3C/svg%3E");
> }
> ```

> [!lemma]+ Lemma
> 
> ```scss
> &[data-callout="lemma"] {
>   --color: #FFBFBF;
>   --border: #FFBFBF3F;
>   --bg: #FFBFBF1F;
>   --callout-icon: url("data:image/svg+xml; utf8, %3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 320 512'%3E%3C!--!Font Awesome Free 6.7.1 by @fontawesome - https://fontawesome.com License - https://fontawesome.com/license/free Copyright 2024 Fonticons, Inc.--%3E%3Cpath d='M80 160c0-35.3 28.7-64 64-64l32 0c35.3 0 64 28.7 64 64l0 3.6c0 21.8-11.1 42.1-29.4 53.8l-42.2 27.1c-25.2 16.2-40.4 44.1-40.4 74l0 1.4c0 17.7 14.3 32 32 32s32-14.3 32-32l0-1.4c0-8.2 4.2-15.8 11-20.2l42.2-27.1c36.6-23.6 58.8-64.1 58.8-107.7l0-3.6c0-70.7-57.3-128-128-128l-32 0C73.3 32 16 89.3 16 160c0 17.7 14.3 32 32 32s32-14.3 32-32zm80 320a40 40 0 1 0 0-80 40 40 0 1 0 0 80z'/%3E%3C/svg%3E");
> }
> ```

> [!corollario]+ Corollario
> 
> ```scss
> &[data-callout="corollario"] {
>   --color: #FFCF7F;
>   --border: #FFCF7F3F;
>   --bg: #FFCF7F1F;
>   --callout-icon: url("data:image/svg+xml; utf8, %3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 320 512'%3E%3C!--!Font Awesome Free 6.7.1 by @fontawesome - https://fontawesome.com License - https://fontawesome.com/license/free Copyright 2024 Fonticons, Inc.--%3E%3Cpath d='M80 160c0-35.3 28.7-64 64-64l32 0c35.3 0 64 28.7 64 64l0 3.6c0 21.8-11.1 42.1-29.4 53.8l-42.2 27.1c-25.2 16.2-40.4 44.1-40.4 74l0 1.4c0 17.7 14.3 32 32 32s32-14.3 32-32l0-1.4c0-8.2 4.2-15.8 11-20.2l42.2-27.1c36.6-23.6 58.8-64.1 58.8-107.7l0-3.6c0-70.7-57.3-128-128-128l-32 0C73.3 32 16 89.3 16 160c0 17.7 14.3 32 32 32s32-14.3 32-32zm80 320a40 40 0 1 0 0-80 40 40 0 1 0 0 80z'/%3E%3C/svg%3E");
> }
> ```

> [!congettura]+ Congettura
> 
> ```scss
> &[data-callout="congettura"] {
>   --color: #BF3F3F;
>   --border: #BF3F3F3F;
>   --bg: #BF3F3F1F;
>   --callout-icon: url("data:image/svg+xml; utf8, %3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 320 512'%3E%3C!--!Font Awesome Free 6.7.1 by @fontawesome - https://fontawesome.com License - https://fontawesome.com/license/free Copyright 2024 Fonticons, Inc.--%3E%3Cpath d='M80 160c0-35.3 28.7-64 64-64l32 0c35.3 0 64 28.7 64 64l0 3.6c0 21.8-11.1 42.1-29.4 53.8l-42.2 27.1c-25.2 16.2-40.4 44.1-40.4 74l0 1.4c0 17.7 14.3 32 32 32s32-14.3 32-32l0-1.4c0-8.2 4.2-15.8 11-20.2l42.2-27.1c36.6-23.6 58.8-64.1 58.8-107.7l0-3.6c0-70.7-57.3-128-128-128l-32 0C73.3 32 16 89.3 16 160c0 17.7 14.3 32 32 32s32-14.3 32-32zm80 320a40 40 0 1 0 0-80 40 40 0 1 0 0 80z'/%3E%3C/svg%3E");
> }
> ```

> [!dimostrazione]- Dimostrazione
> 
> ```scss
> &[data-callout="dimostrazione"] {
>   --color: #7FFF7F;
>   --border: #7FFF7F3F;
>   --bg: #7FFF7F1F;
>   --callout-icon: url("data:image/svg+xml; utf8, %3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 128 512'%3E%3C!--!Font Awesome Free 6.7.1 by @fontawesome - https://fontawesome.com License - https://fontawesome.com/license/free Copyright 2024 Fonticons, Inc.--%3E%3Cpath d='M96 64c0-17.7-14.3-32-32-32S32 46.3 32 64l0 256c0 17.7 14.3 32 32 32s32-14.3 32-32L96 64zM64 480a40 40 0 1 0 0-80 40 40 0 1 0 0 80z'/%3E%3C/svg%3E");
> }
> ```

> [!principio]+ Principio
> 
> ```scss
> &[data-callout="principio"] {
>   --color: #7FFFFF;
>   --border: #7FFFFF3F;
>   --bg: #7FFFFF1F;
>   --callout-icon: url("data:image/svg+xml; utf8, %3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 576 512'%3E%3C!--!Font Awesome Free 6.7.2 by @fontawesome - https://fontawesome.com License - https://fontawesome.com/license/free Copyright 2025 Fonticons, Inc.--%3E%3Cpath d='M316.9 18C311.6 7 300.4 0 288.1 0s-23.4 7-28.8 18L195 150.3 51.4 171.5c-12 1.8-22 10.2-25.7 21.7s-.7 24.2 7.9 32.7L137.8 329 113.2 474.7c-2 12 3 24.2 12.9 31.3s23 8 33.8 2.3l128.3-68.5 128.3 68.5c10.8 5.7 23.9 4.9 33.8-2.3s14.9-19.3 12.9-31.3L438.5 329 542.7 225.9c8.6-8.5 11.7-21.2 7.9-32.7s-13.7-19.9-25.7-21.7L381.2 150.3 316.9 18z'/%3E%3C/svg%3E");
> }
> ```

> [!proprieta]+ Proprietà
> 
> ```scss
> &[data-callout="proprieta"] {
>   --color: #FFFF7F;
>   --border: #FFFF7F3F;
>   --bg: #FFFF7F1F;
>   --callout-icon: url("data:image/svg+xml; utf8, %3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 512 512'%3E%3C!--!Font Awesome Free 6.7.2 by @fontawesome - https://fontawesome.com License - https://fontawesome.com/license/free Copyright 2025 Fonticons, Inc.--%3E%3Cpath d='M495.9 166.6c3.2 8.7 .5 18.4-6.4 24.6l-43.3 39.4c1.1 8.3 1.7 16.8 1.7 25.4s-.6 17.1-1.7 25.4l43.3 39.4c6.9 6.2 9.6 15.9 6.4 24.6c-4.4 11.9-9.7 23.3-15.8 34.3l-4.7 8.1c-6.6 11-14 21.4-22.1 31.2c-5.9 7.2-15.7 9.6-24.5 6.8l-55.7-17.7c-13.4 10.3-28.2 18.9-44 25.4l-12.5 57.1c-2 9.1-9 16.3-18.2 17.8c-13.8 2.3-28 3.5-42.5 3.5s-28.7-1.2-42.5-3.5c-9.2-1.5-16.2-8.7-18.2-17.8l-12.5-57.1c-15.8-6.5-30.6-15.1-44-25.4L83.1 425.9c-8.8 2.8-18.6 .3-24.5-6.8c-8.1-9.8-15.5-20.2-22.1-31.2l-4.7-8.1c-6.1-11-11.4-22.4-15.8-34.3c-3.2-8.7-.5-18.4 6.4-24.6l43.3-39.4C64.6 273.1 64 264.6 64 256s.6-17.1 1.7-25.4L22.4 191.2c-6.9-6.2-9.6-15.9-6.4-24.6c4.4-11.9 9.7-23.3 15.8-34.3l4.7-8.1c6.6-11 14-21.4 22.1-31.2c5.9-7.2 15.7-9.6 24.5-6.8l55.7 17.7c13.4-10.3 28.2-18.9 44-25.4l12.5-57.1c2-9.1 9-16.3 18.2-17.8C227.3 1.2 241.5 0 256 0s28.7 1.2 42.5 3.5c9.2 1.5 16.2 8.7 18.2 17.8l12.5 57.1c15.8 6.5 30.6 15.1 44 25.4l55.7-17.7c8.8-2.8 18.6-.3 24.5 6.8c8.1 9.8 15.5 20.2 22.1 31.2l4.7 8.1c6.1 11 11.4 22.4 15.8 34.3zM256 336a80 80 0 1 0 0-160 80 80 0 1 0 0 160z'/%3E%3C/svg%3E");
> }
> ```

> [!algoritmo]+ Algoritmo
> 
> ```scss
> &[data-callout="algoritmo"] {
>   --color: #FF3F3F;
>   --border: #FF3F3F3F;
>   --bg: #FF3F3F1F;
>   --callout-icon: url("data:image/svg+xml; utf8, %3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 512 512'%3E%3C!--!Font Awesome Free 6.7.2 by @fontawesome - https://fontawesome.com License - https://fontawesome.com/license/free Copyright 2025 Fonticons, Inc.--%3E%3Cpath d='M24 56c0-13.3 10.7-24 24-24l32 0c13.3 0 24 10.7 24 24l0 120 16 0c13.3 0 24 10.7 24 24s-10.7 24-24 24l-80 0c-13.3 0-24-10.7-24-24s10.7-24 24-24l16 0 0-96-8 0C34.7 80 24 69.3 24 56zM86.7 341.2c-6.5-7.4-18.3-6.9-24 1.2L51.5 357.9c-7.7 10.8-22.7 13.3-33.5 5.6s-13.3-22.7-5.6-33.5l11.1-15.6c23.7-33.2 72.3-35.6 99.2-4.9c21.3 24.4 20.8 60.9-1.1 84.7L86.8 432l33.2 0c13.3 0 24 10.7 24 24s-10.7 24-24 24l-88 0c-9.5 0-18.2-5.6-22-14.4s-2.1-18.9 4.3-25.9l72-78c5.3-5.8 5.4-14.6 .3-20.5zM224 64l256 0c17.7 0 32 14.3 32 32s-14.3 32-32 32l-256 0c-17.7 0-32-14.3-32-32s14.3-32 32-32zm0 160l256 0c17.7 0 32 14.3 32 32s-14.3 32-32 32l-256 0c-17.7 0-32-14.3-32-32s14.3-32 32-32zm0 160l256 0c17.7 0 32 14.3 32 32s-14.3 32-32 32l-256 0c-17.7 0-32-14.3-32-32s14.3-32 32-32z'/%3E%3C/svg%3E");
> }
> ```

### 2.8.3 - Per l'informatica

> [!sintassi]+ Sintassi
> 
> ```scss
> &[data-callout="sintassi"] {
>   --color: #FFFF7F;
>   --border: #FFFF7F3F;
>   --bg: #FFFF7F1F;
>   --callout-icon: url("data:image/svg+xml; utf8, %3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 640 512'%3E%3C!--!Font Awesome Free 6.7.2 by @fontawesome - https://fontawesome.com License - https://fontawesome.com/license/free Copyright 2025 Fonticons, Inc.--%3E%3Cpath d='M392.8 1.2c-17-4.9-34.7 5-39.6 22l-128 448c-4.9 17 5 34.7 22 39.6s34.7-5 39.6-22l128-448c4.9-17-5-34.7-22-39.6zm80.6 120.1c-12.5 12.5-12.5 32.8 0 45.3L562.7 256l-89.4 89.4c-12.5 12.5-12.5 32.8 0 45.3s32.8 12.5 45.3 0l112-112c12.5-12.5 12.5-32.8 0-45.3l-112-112c-12.5-12.5-32.8-12.5-45.3 0zm-306.7 0c-12.5-12.5-32.8-12.5-45.3 0l-112 112c-12.5 12.5-12.5 32.8 0 45.3l112 112c12.5 12.5 32.8 12.5 45.3 0s12.5-32.8 0-45.3L77.3 256l89.4-89.4c12.5-12.5 12.5-32.8 0-45.3z'/%3E%3C/svg%3E");
> }
> ```

## 2.9 - Icone nei titoli delle note

In questo Giardino Digitale, ogni nota ha associata una icona colorata in formato SVG. Le icone le prendo da [FontAwesome](https://fontawesome.com/) e da [Tabler Icons](https://tablericons.com/) e le inserisco nella cartella `content/_icons` con lo stesso nome della nota a cui fa riferimento.

Per modificare il colore delle icone scaricate, prima le formatto usando lo script `svg-formatter.py` che ho scritto io con le mie manine (e che si trova ovviamente nella cartella `content/scripts`) e poi modifico a mano il codice SVG impostando il colore desiderato nel parametro `fill`.

Per aggiungere le icone affianco ai titoli delle note, ho modificato il file `quartz/components/ArticleTitle.tsx` in questo modo:

```tsx title="quartz/components/ArticleTitle.tsx" {4-16}
const ArticleTitle: QuartzComponent = ({ fileData, displayClass }: QuartzComponentProps) => {
  const title = fileData.frontmatter?.title
  if (title) {
    return <h1 class={classNames(displayClass, "article-title")}>
      <img
        style="display: inline; height: 0.8em; width: auto; margin-right: 0.1em;"
        src={"/digital-garden/_icons/" + title.replaceAll(" ", "-") + ".svg"}
        alt=""
      />
      <img
        style="display: inline; height: 0.8em; width: auto; margin-right: 0.1em;"
        src={"/_icons/" + title.replaceAll(" ", "-") + ".svg"}
        alt=""
      />
      {title}
    </h1>
  } else {
    return null
  }
}
```

Piccolo disclaimer: lo so che questa porzione di codice l'ho scritta col culo, ma non sono un web developer e a malapena so destreggiarmi con il TypeScript. Ci sono sicuramente modi più puliti per realizzare quello che voglio fare, ma ci accontentiamo.

Per aggiungere le icone ai titoli delle note anche all'interno dell'Esplora%% link %% sul lato della pagina, ho chiesto sul [server Discord ufficiale di Quartz](https://discord.com/invite/cRFFHYye7t) un aiutino su come farlo ma nessuno mi ha aiutato. Allora ho chiesto un aiutino al mio caro amico Deepseek, che in un quarto d'ora ha saputo aiutarmi a raggiungere il risultato voluto.

Specifico che ogni componente è duplicato solo perché, hostando il sito sulle GitHub Pages, i percorsi relativi partono dal dominio del sito (cioè `rexus752.github.io`) e non dalla "pagina" del Giardino Digitale (cioè `rexus752.github.io/digital-garden`), ossia da quello che effettivamente dovrebbe essere l'equivalente della cartella `content` del vault di Obsidian. Ciò implica che, buildando il sito in locale, le icone delle note si trovano nella cartella `/_icons/`, mentre buildando il sito online le icone si trovano nella cartella `/digital-notes/_icons/`. Non ho trovato un modo per rendere questi percorsi relativi "dinamici" a seconda della situazione (build in locale od online) e, come soluzione più facile, ho deciso di inserire per ogni icona una coppia di elementi: uno che cerca l'icona al percorso `/_icons/`, l'altro al percorso `/digital-notes/_icons/`. Funziona perché a prescindere uno dei due troverà l'icona al percorso desiderato e l'altro no, quindi comparirà sempre una sola icona.

Quello che ho fatto è stato:
1. Aggiungere nel file `quartz/components/scripts/explorer.inline.ts` sia nella funzione `createFileNode` che nella funzione `createFolderNode` questi pezzi di codice che integrano le icone nei template che Quartz usa per generare le entry dei file e delle cartelle nell'Explorer:
	```tsx title="quartz/components/scripts/explorer.inline.ts" {6-15,38-47}
	function createFileNode(currentSlug: FullSlug, node: FileTrieNode): HTMLLIElement {
	  const template = document.getElementById("template-file") as HTMLTemplateElement
	  const clone = template.content.cloneNode(true) as DocumentFragment
	  const li = clone.querySelector("li") as HTMLLIElement
	
	  const icon_local = li.querySelector(".file-icon-local") as HTMLImageElement
	  if (icon_local) {
	    icon_local.src = `/_icons/${node.displayName.replaceAll(" ", "-")}.svg`
	    icon_local.alt = ""
	  }
	  const icon_sync = li.querySelector(".file-icon-sync") as HTMLImageElement
	  if (icon_sync) {
	    icon_sync.src = `/digital-garden/_icons/${node.displayName.replaceAll(" ", "-")}.svg`
	    icon_sync.alt = ""
	  }
	
	  const a = li.querySelector("a") as HTMLAnchorElement
	  a.href = resolveRelative(currentSlug, node.slug)
	  a.dataset.for = node.slug
	  a.textContent = node.displayName
	
	  if (currentSlug === node.slug) {
		a.classList.add("active")
	  }
	
	  return li
	}
	
	function createFolderNode(
	  currentSlug: FullSlug,
	  node: FileTrieNode,
	  opts: ParsedOptions,
	): HTMLLIElement {
	  const template = document.getElementById("template-folder") as HTMLTemplateElement
	  const clone = template.content.cloneNode(true) as DocumentFragment
	  const li = clone.querySelector("li") as HTMLLIElement
	
	  const icon_local = li.querySelector(".folder-icon-local") as HTMLImageElement
	  if (icon_local) {
	    icon_local.src = `/_icons/${node.displayName.replaceAll(" ", "-")}.svg`
	    icon_local.alt = ""
	  }
	  const icon_sync = li.querySelector(".folder-icon-sync") as HTMLImageElement
	  if (icon_sync) {
	    icon_sync.src = `/digital-garden/_icons/${node.displayName.replaceAll(" ", "-")}.svg`
	    icon_sync.alt = ""
	  }
	
	  const folderContainer = li.querySelector(".folder-container") as HTMLElement
	  const titleContainer = folderContainer.querySelector("div") as HTMLElement
	  const folderOuter = li.querySelector(".folder-outer") as HTMLElement
	  const ul = folderOuter.querySelector("ul") as HTMLUListElement
	  // ...
	}
	```
2. Aggiungere effettivamente nel template delle entry in `quartz/components/Explorer.tsx` i tag `<img>` per inserire le icone:
	```tsx title="quartz/components/Explorer.tsx" {21-32,53-64}
	export default ((userOpts?: Partial<Options>) => {
	  const Explorer: QuartzComponent = ({ cfg, displayClass }: QuartzComponentProps) => {
		const id = `explorer-${numExplorers++}`
	
		return (
		  <div
			class={classNames(displayClass, "explorer")}
			data-behavior={opts.folderClickBehavior}
			data-collapsed={opts.folderDefaultState}
			data-savestate={opts.useSavedState}
			data-data-fns={JSON.stringify({
			  order: opts.order,
			  sortFn: opts.sortFn.toString(),
			  filterFn: opts.filterFn.toString(),
			  mapFn: opts.mapFn.toString(),
			})}
		  >
		  {/* ... */}
			<template id="template-file">
			  <li>
	            <img 
	              class="file-icon-sync"
	              src="" 
	              alt="" 
	              style="display: inline; height: 1em; width: auto; margin-right: 0.15em; vertical-align: middle;"
	            />
	            <img 
	              class="file-icon-local"
	              src="" 
	              alt="" 
	              style="display: inline; height: 1em; width: auto; margin-right: 0.15em; vertical-align: middle;"
	            />
				<a href="#"></a>
			  </li>
			</template>
			<template id="template-folder">
			  <li>
				<div class="folder-container">
				  <svg
					xmlns="http://www.w3.org/2000/svg"
					width="12"
					height="12"
					viewBox="5 8 14 8"
					fill="none"
					stroke="currentColor"
					stroke-width="2"
					stroke-linecap="round"
					stroke-linejoin="round"
					class="folder-icon"
				  >
					<polyline points="6 9 12 15 18 9"></polyline>
				  </svg>
	              <img 
	                class="folder-icon-sync" 
	                src="" 
	                alt="" 
	                style="display: inline; height: 1.2em; width: auto; margin-right: 0.15em; vertical-align: middle;"
	              />
	              <img 
	                class="folder-icon-local" 
	                src="" 
	                alt="" 
	                style="display: inline; height: 1.2em; width: auto; margin-right: 0.15em; vertical-align: middle;"
	              />
				  <div>
					<button class="folder-button">
					  <span class="folder-title"></span>
					</button>
				  </div>
				</div>
				<div class="folder-outer">
				  <ul class="content"></ul>
				</div>
			  </li>
			</template>
		  </div>
		)
	  }
	
	  Explorer.css = style
	  Explorer.afterDOMLoaded = concatenateResources(script, overflowListAfterDOMLoaded)
	  return Explorer
	}) satisfies QuartzComponentConstructor
	```
1. Per evitare che l'icona faccia allineare il nome della cartella a destra, nel file `quartz/components/styles/explorer.scss` ho modificato il tipo di `display`:
	```scss title="quartz/components/styles/explorer.scss" {3}
	.folder-container {
	  flex-direction: row;
	  display: inline-flex;
	  align-items: center;
	  user-select: none;
	  // ...
	}
	```

## 2.10 - `.gitignore`

Nel `.gitignore` ho rimosso le cartelle `.obsidian` e `private` così, in caso di eventi catastrofici, non perdo i loro contenuti e posso tranquillamente recuperarli dal repository del Giardino Digitale.

# 3 - Da fare

Questo è ciò che ho in mente di fare per migliorare il sito:
- Migliorare l'interfaccia grafica
- Trovare un modo per caricare nel repository anche quelle cartelle che Quartz inserisce di default nel `.gitignore` come la `.obsidian` contenente le impostazioni del vault di Obsidian ed eventuali cartelle `private` contenenti note private (che però io non uso) e `templates` contenenti template per le note, in modo da avere un backup completo nel repository nel caso in cui dovesse malauguratamente succedere qualcosa.
- Ridurre lo spazio vuoto in cima alle pagine del sito.
- Integrare le icone delle note anche nel _Breadcrumbs_.
- Rinominare "Vista grafico" in qualcos'altro di più vicino all'italiano corretto.
- Integrare Giscus.
- Sostituire il codice CSS delle tabelle.
- Trasformare la "Reader Mode" in una modalità dyslexic-friendly (es. usando il font [OpenDyslexic](https://opendyslexic.org/)). 
- Renderizzare il LaTeX nei titoli dell'indice sul lato delle pagine.
