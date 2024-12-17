---
icon: SiObsidian
iconColor: "#CC88CC"
---
Questa è la lista delle configurazioni di Obsidian e dei suoi plugin che uso.

# Impostazioni Obsidian

## Editor

- _Readable line length_: ❌
- _Show line number_: ✔️

## Files and links

- _Confirm file deletion_: ❌
- _Automatically update internal links_: ✔️
- _Use \[\[Wikilinks]]_: ❌
- _Detect all file extensions_: ✔️
- _Default location for new attachments_: `In subfolder under current folder`
- _Subfolder name_: `attachments`

## Appearance

- _Themes_: `GitHub Theme`
- _Font Size_: `14`
- _Quick font size adjustment_: ✔️
- _CSS Snippets_:
	- `aligned-callout-header-titles.css`:
		```css
		body:not(.pt-disable-callout-styling) .callout .callout-title {
			align-items: center;
		}
		```
	- `bold-folders.css`:
		```css
		.nav-folder-title {
			font-weight: 1000;
		}
		```
	- `justified-text.css`:
		```css
		/* Reading Mode */
		.markdown-preview-view p {
			text-align: justify;
			text-justify: inter-word;
		}
		
		/* Source View and Live Preview */
		.markdown-source-view.mod-cm6 .cm-line {
			text-align: justify;
			text-justify: inter-word;
		}
		```
	- `mermaid-center.css`:
		```css
		div.mermaid {
		  text-align: center;
		}
		```

## Hotkeys

- _Insert code block_: `Ctrl + Shift + M`
- _Toggle code_: `Ctrl + M`

# Core Plugins

- _Random note_: ✔️
- _Slash commands_: ✔️

# Community Plugins

## Admonition

- _Use CSS Snippet for Custom Callout_: ✔️
- _Import Admonitions_: `seleziona file JSON`
- _Add Copy Button_: ✔️
	- _Load Additional Icons_: **tutte**

#### Hotkeys

- _Admonition: Insert Callout_: `Ctrl + Shift + P`

### Advanced Tables

## Broken links

- _Ignore folders_:
	```
	docs
	node_modules
	private
	public
	quartz
	```

### Hotkeys

- _Advanced Tables: Delete column_: `Alt + Shift + C`
- _Advanced Tables: Delete row_: `Alt + Shift + R`

## Callout Integrator

### Hotkeys

- _Callout Integrator: Integrate_: `Ctrl + >`
- _Callout Integrator: Un-integrate_: `Ctrl + <`

## Colored Tags

## Iconize

- _Recently used icons limit_: `25`
- _Toggle icon in tabs_: ✔️
- _Toggle icon in title_: `ON (Next to title)`
- _Use icon in frontmatter_: ✔️
- _Add predefined icon packs_: **tutti**

## LaTeX Suite

- _Snippets_:
	```javascript
	[
	    // Single letter triggers like "\\N" in single dollar signs (i.e. $...$) don't work with "m" option, only with "t" option
	    
		// Math mode
		{trigger: "$", replacement: "$$0$", options: "tA"},
		{trigger: "$", replacement: "$\n$0\n$", options: "mA"},
	
		// Brackets
		{trigger: "(", replacement: "($0)$1", options: "mA"},
		{trigger: "{", replacement: "{$0}$1", options: "mA"},
		{trigger: "[", replacement: "[$0]$1", options: "mA"},
		{trigger: "lr(", replacement: "\\left( $0 \\right) $1", options: "mA"},
		{trigger: "lr{", replacement: "\\left\\{ $0 \\right\\} $1", options: "mA"},
		{trigger: "lr[", replacement: "\\left[ $0 \\right] $1", options: "mA"},
		{trigger: "lr|", replacement: "\\left| $0 \\right| $1", options: "mA"},
		{trigger: "lr<", replacement: "\\left< $0 \\right> $1", options: "mA"},
	
		// Dots & Spaces
		{trigger: "...", replacement: "\\ldots", options: "mA"},
		{trigger: ".*", replacement: "\\cdot", options: "mA"},
		{trigger: "\\q", replacement: "\\quad", options: "mA"},
	
		// Arrows
		{trigger: "<->", replacement: "\\leftrightarrow", options: "mA"},
		{trigger: "->", replacement: "\\to", options: "mA"},
		{trigger: "<-", replacement: "\\gets", options: "mA"},
		{trigger: "!>", replacement: "\\mapsto", options: "mA"},
		{trigger: "=>", replacement: "\\implies", options: "mA"},
		{trigger: "=<", replacement: "\\impliedby", options: "mA"},
	
		// Equals
		{trigger: "!=", replacement: "\\neq", options: "mA"},
		{trigger: ">=", replacement: "\\ge", options: "mA"},
		{trigger: "<=", replacement: "\\le", options: "mA"},
	
		// Environments
		{trigger: "\\matrix", replacement: "\\begin{matrix}\n$0\n\\end{matrix}", options: "mA"},
		{trigger: "\\cases", replacement: "\\begin{cases}\n$0\n\\end{cases}", options: "mA"},
		{trigger: "\\align", replacement: "\\begin{align}\n$0\n\\end{align}", options: "mA"},
		{trigger: "\\array", replacement: "\\begin{array}\n$0\n\\end{array}", options: "mA"},
	    
	    // Numeric Sets
		{trigger: "\\N", replacement: "\\mathbb{N}", options: "tmA"},
		{trigger: "\\Z", replacement: "\\mathbb{Z}", options: "tmA"},
		{trigger: "\\Q", replacement: "\\mathbb{Q}", options: "tmA"},
		{trigger: "\\I", replacement: "\\mathbb{I}", options: "tmA"},
		{trigger: "\\R", replacement: "\\mathbb{R}", options: "tmA"},
		{trigger: "\\C", replacement: "\\mathbb{C}", options: "tmA"},
	
	    // Probability
		{trigger: "\\P", replacement: "\\mathbb{P}", options: "tmA"}, // Power set
	
		// Sets
		{trigger: "\\p", replacement: "\\mathcal{P}", options: "tmA"}, // Power set
		{trigger: "\\sube", replacement: "\\subseteq", options: "mA"},
		{trigger: "\\empty", replacement: "\\emptyset", options: "mA"},
	
		// Functions
		{trigger: "\\Dom", replacement: "\\text{Dom}(f)", options: "mA"},
	
	    // Algorithms
	    {trigger: "\\algo", replacement: "\\begin{align*}\n & \\textbf{$0} \\quad \\rhd \\\\\n & \n\\end{align*}", options: "mA"},
		{trigger: "if", replacement: "\\textrm{if } $0 \\textrm{ then} \\\\\n & ", options: "mA"},
		{trigger: "else", replacement: "\\textrm{else} \\\\\n & ", options: "mA"},
		{trigger: "end if", replacement: "\\textrm{end if} \\\\\n & ", options: "mA"},
		{trigger: "while", replacement: "\\textrm{while } $0 \\textrm{ do} \\\\\n & ", options: "mA"},
	    {trigger: "end while", replacement: "\\textrm{end while} \\\\\n & ", options: "mA"},
		{trigger: "for", replacement: "\\textrm{for } $0 \\textrm{ to } $1 \\textrm{ do} \\\\\n & ", options: "mA"},
		{trigger: "end for", replacement: "\\textrm{end for} \\\\\n & ", options: "mA"},
		{trigger: "return", replacement: "\\textrm{return } $0 \\\\\n & ", options: "mA"},
	]
	```
- _Matrix Shortcuts_:
	- _Environments_:
		```
		pmatrix, cases, align, align*, bmatrix, Bmatrix, vmatrix, Vmatrix, array, matrix
		```

## Link Favicons

- _Icon provider_: `Google`
- _Fallback icon provider_: `DuckDuckGo`
- _Ignored domains_: `photos.app.goo.gl`

## Paste URL into selection

## Quiet Outline

- _Set Primary Color Light/Dark_: ❌
- _Ellipsis_: ✔️
- _Default level_: `H1`

## Settings Search

## Style Settings

- _GitHub theme settings_
	- _Colorblind variants_
		- _Protanopia & Deuteranopia_: ✔️
		- _Tritanopia_: ✔️