import { PageLayout, SharedLayout } from "./quartz/cfg"
import * as Component from "./quartz/components"

// components shared across all pages
export const sharedPageComponents: SharedLayout = {
  head: Component.Head(),
	header: [],
	afterBody: [
		Component.Comments({
			provider: 'giscus',
			options: {
				// from data-repo
				repo: 'Rexus752/digital-garden',
				// from data-repo-id
				repoId: 'R_kgDONHp66Q',
				// from data-category
				category: 'Announcements',
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

// components for pages that display a single page (e.g. a single note)
export const defaultContentPageLayout: PageLayout = {
	beforeBody: [
		Component.Breadcrumbs(),
		Component.MobileOnly(Component.TableOfContents()),
		Component.ArticleTitle(),
		Component.ContentMeta(),
		Component.TagList(),
	],
	left: [
		Component.PageTitle(),
		Component.Search(),
		// Component.Darkmode(),
		Component.DesktopOnly(Component.TableOfContents()),
		
	],
	right: [
		Component.DesktopOnly(Component.Explorer()),
		Component.Graph(),
	],
}

// components for pages that display lists of pages	(e.g. tags or folders)
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
