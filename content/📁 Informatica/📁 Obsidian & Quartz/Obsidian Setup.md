---
icon: SiObsidian
iconColor: "#FF88FF"
---
Questa è la lista delle configurazioni di Obsidian e dei suoi plugin che uso.

# Impostazioni Obsidian

## Editor

- _Readable line length_: ❌
- _Show line number_: ✔️

## Files and links

- _Confirm file deletion_: ❌
- _Automatically update internal links_: ✔️
- _Use Wikilinks_: ❌
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

- _General_:
	- _Recently used icons limit_: `25`
- _Visibility of icons_:
	- _Toggle icon in tabs_: ✔️
	- _Toggle icon in title_: `ON (Next to title)`
	- _Use icon in frontmatter_: ✔️
- _Add predefined icon packs_: **tutti**

## LaTeX Suite

%%

> [!tip] Consiglio
> Per gli Snippets, non usare i miei fin ma parti da zero e createli da te. Poi, eventualmente, prendi spunto dai miei se pensi che siano comodi per te.

%%

- _Snippets_:
	```javascript
	[
	    // Single letter triggers like "\\N" in single dollar signs (i.e. $...$) don't work with "m" option, only with "t" option
	    
	    // Comments in Markdown
		{trigger: "%%", replacement: "%% $0 %%", options: "tA"},
	    
		// Math Mode
		{trigger: "$", replacement: "$$0$", options: "tA"},
		{trigger: "$", replacement: "$\n$0\n$", options: "mA"},
		
		// Text
		{trigger: "\"", replacement: "\\text{$0}$1", options: "mA"},
		
	
		// Colors
		{trigger: "\\red", replacement: "{\\color{#FF8888} $0 }", options: "mA"},
		{trigger: "\\green", replacement: "{\\color{#88FF88} $0 }", options: "mA"},
		{trigger: "\\blue", replacement: "{\\color{#8888FF} $0 }", options: "mA"},
		{trigger: "\\yellow", replacement: "{\\color{#FFFF88} $0 }", options: "mA"},
		{trigger: "\\violet", replacement: "{\\color{#FF88FF} $0 }", options: "mA"},
		{trigger: "\\aqua", replacement: "{\\color{#88FFFF} $0 }", options: "mA"},
		
		// Brackets
		{trigger: "(", replacement: "($0)$1", options: "mA"},
		{trigger: "{", replacement: "{$0}$1", options: "mA"},
		{trigger: "[", replacement: "[$0]$1", options: "mA"},
		{trigger: "\\langle", replacement: "\\langle $0 \\rangle $1", options: "mA"},
		{trigger: "lr(", replacement: "\\left( $0 \\right) $1", options: "mA"},
		{trigger: "lr{", replacement: "\\left\\{ $0 \\right\\} $1", options: "mA"},
		{trigger: "lr[", replacement: "\\left[ $0 \\right] $1", options: "mA"},
		{trigger: "lr|", replacement: "\\left| $0 \\right| $1", options: "mA"},
		{trigger: "lr<", replacement: "\\left< $0 \\right> $1", options: "mA"},
		{trigger: "\\ceil", replacement: "\\lceil $0 \\rceil $1", options: "mA"},
		{trigger: "\\floor", replacement: "\\lfloor $0 \\rfloor $1", options: "mA"},
	
		// Dots & Spaces
		{trigger: "...", replacement: "\\ldots", options: "mA"},
		{trigger: ".*", replacement: "\\cdot", options: "mA"},
		{trigger: "\\q", replacement: "\\quad ", options: "mA"},
	
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
		{trigger: "\\align", replacement: "\\begin{align*}\n$0\n\\end{align*}", options: "mA"},
		{trigger: "\\array", replacement: "\\begin{array}\n$0\n\\end{array}", options: "mA"},
	    
	    // Numeric Sets
		{trigger: "\\N", replacement: "\\mathbb{N}", options: "tmA"},
		{trigger: "\\Z", replacement: "\\mathbb{Z}", options: "tmA"},
		{trigger: "\\Q", replacement: "\\mathbb{Q}", options: "tmA"},
		{trigger: "\\I", replacement: "\\mathbb{I}", options: "tmA"},
		{trigger: "\\R", replacement: "\\mathbb{R}", options: "tmA"},
		{trigger: "\\C", replacement: "\\mathbb{C}", options: "tmA"},
	
	    // Probability
		{trigger: "\\P", replacement: "\\mathbb{P}", options: "tmA"},
	
		// Sets
		{trigger: "\\{", replacement: "\\{ $0 \\}", options: "tmA"},
		{trigger: "\\sube", replacement: "\\subseteq", options: "mA"},
		{trigger: "\\empty", replacement: "\\emptyset", options: "mA"},
	
		// Functions
		{trigger: "\\Dom", replacement: "\\text{Dom}(f)", options: "mA"},
	
	    // Algorithm environment
	    {
		    // Creates the Algorithm environment
		    trigger: "\\algo",
		    replacement: "\\begin{align*} % Algorithm environment\n & \\textbf{$0} \\\\\n & \\rhd \\text{Pre: } $1 \\\\\n & \\rhd \\text{Post: } $2 \\\\\n & $3\n\\end{align*}",
		    options: "mA"
		},
		{
			// Formats an inline comment in Algorithm environment
			trigger: "(Algorithm environment(?:(?!\\$\\$)[\\s\\S])*?)\#",
			replacement: "[[0]]\\quad \\rhd \\text{$0}",
			options: "rmA"
		},
		{
			// Formats "if" in Algorithm environment
			trigger: "(Algorithm environment(?:(?!\\$\\$)[\\s\\S])*?)if",
			replacement: "[[0]]\\text{if } $0 \\text{ then} \\\\\n & \\quad $1",
			options: "rmA"
		},
		{
			// Formats "else" in Algorithm environment
			trigger: "(Algorithm environment(?:(?!\\$\\$)[\\s\\S])*?)else",
			replacement: "[[0]]\\text{else} \\\\\n & \\quad $0",
			options: "rmA"
		},
		{
			// Formats "end if" in Algorithm environment
			trigger: "(Algorithm environment(?:(?!\\$\\$)[\\s\\S])*?)end if",
			replacement: "[[0]]\\text{end if} \\\\\n & $0",
			options: "rmA"
		},
		{
			// Formats "while" in Algorithm environment
			trigger: "(Algorithm environment(?:(?!\\$\\$)[\\s\\S])*?)while",
			replacement: "[[0]]\\text{while } $0 \\text{ do} \\\\\n & \\quad $1",
			options: "rmA"
		},
	    {
		    // Formats "end while" in Algorithm environment
		    trigger: "(Algorithm environment(?:(?!\\$\\$)[\\s\\S])*?)end while",
		    replacement: "[[0]]\\text{end while} \\\\\n & $0",
			options: "rmA"
		},
		{
			// Formats "for" in Algorithm environment
			trigger: "(Algorithm environment(?:(?!\\$\\$)[\\s\\S])*?)for",
			replacement: "[[0]]\\text{for } $0 \\text } $1 \\text{ do} \\\\\n & \\quad $2",
			options: "rmA"
		},
		{
			// Formats "end for" in Algorithm environment
			trigger: "(Algorithm environment(?:(?!\\$\\$)[\\s\\S])*?)end for",
			replacement: "[[0]]\\text{end for} \\\\\n & $0",
			options: "rmA"
		},
		{
			// Formats "and" in Algorithm environment
			trigger: "(Algorithm environment(?:(?!\\$\\$)[\\s\\S])*?)and",
			replacement: "[[0]]\\text{ and } $0 ",
			options: "rmA"
		},
		{
			// Formats "or" in Algorithm environment
			trigger: "(Algorithm environment(?:(?!\\$\\$)[\\s\\S])*?)or",
			replacement: "[[0]]\\text{ or } $0 ",
			options: "rmA"
		},
		{
			// Formats "return" in Algorithm environment
			trigger: "(Algorithm environment(?:(?!\\$\\$)[\\s\\S])*?)return",
			replacement: "[[0]]\\text{return } $0 \\\\\n & $1",
			options: "rmA"
		}
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