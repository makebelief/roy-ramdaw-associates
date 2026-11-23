# SEO audit — Roy Ramdaw & Associates Inc.

**Audit date:** 23 November 2026<br>
**Production URL:** https://royramdaw.co.za/<br>
**Production Git baseline:** `origin/cloudflare-production` at `540de93`<br>
**Working branch:** `seo/comprehensive-optimization`

## Scope and architecture

The live site is a static HTML/CSS/JavaScript site deployed from `public/` through Cloudflare Pages. There is no package manifest or compile step. The repository root contains an older Vercel concept with stale `noindex` tags and `vercel.app` canonicals; **those root files are not the current deployed website**. SEO changes in this project target `public/`. Existing `public/_headers` and `_redirects` contain Cloudflare Pages rules. The initial working tree was clean, and the branch was created from the deployed source branch.

The baseline has six indexable pages: home, about, practice areas, managing partner, insights and contact. Privacy, terms and the 404 page use `noindex`. No dedicated labour subservice pages or standalone legal articles existed. Existing Insights guides were short sections under `/insights/` with fragment links.

The fetched live homepage and `540de93:public/index.html` matched in visible page content and metadata. Cloudflare's email-obfuscation feature rewrote two `mailto:` links and injected its decoder script in the live response, explaining the byte-level difference.

## Findings

| Area | Baseline finding | Assessment / action |
|---|---|---|
| Homepage | Unique title/description and one H1; labour appears below energy and finance. | Relevant but labour enquiries lacked a direct landing path. Improve copy and links while keeping layout. |
| Titles/descriptions | Unique across nine deployed HTML pages; generally descriptive. | Retain good metadata; refine home, practice index and Insights for labour intent. |
| Canonicals/social | Self-referencing `https://royramdaw.co.za/` canonicals, matching `og:url`, first-party OG image and Twitter cards. | Correct. Continue for new pages. |
| Heading hierarchy | One H1 per page; H2/H3 sections mostly coherent. | Improve broad home/practice/Insights H1 wording. |
| URL structure | Human-readable trailing slash paths. | Correct. Add distinct service paths only where the existing service list supports them. |
| Internal links | Header/footer and practice fragments work; labour card points to a broad section. | Add dedicated links from home, practice, bio, Insights, contact and footer. |
| Images/alt | Deployed logos are optimized WebP; portraits are supplied WebP/JPEG; image elements have alt text and dimensions. Photography loads from Pexels. | Good baseline. External photography remains a latency/dependency risk; no image replacement needed. |
| robots/sitemap/indexing | `public/robots.txt` allows crawling and names the production sitemap. Sitemap initially contained six indexable URLs; `noindex` is limited to privacy, terms and 404. | Correct baseline; expand sitemap with new indexable service pages. |
| Structured data | LegalService on pages, WebSite on home, breadcrumbs on internal pages. Baseline LegalService repeated a generic `memberOf` relationship and listed Johannesburg among service areas despite its associated-office status. | Remove unsupported/generic relationship, use stable business `@id`, keep verified Newcastle/Durban details, add Person and service-specific data. |
| Local details | Newcastle head office: 29 Bird Street; Durban office: 114C Northway Centre, 17 Kenneth Kuanda Road. Johannesburg is labelled an associated office with Ramkussan Juglal Inc. | Keep distinctions. Do not create separate city doorway pages. Location and phone details derive from the site's recorded client instructions and contact page; client should reconfirm before deployment. |
| Mobile/rendering | Responsive CSS includes 1050, 850, 600 and 390px breakpoints. Main copy and links are present in server-delivered HTML; JS supports menu and enquiry form. | Search content does not depend on JS. Visual QA still required on representative desktop/mobile widths. |
| Performance | Static site, deferred `site.js`, dimensions on images, lazy loading on lower-page photos, optimized logos. CSS imported Google Fonts, adding a font-discovery chain; hero/other Pexels images depend on external requests. | Move font stylesheet discovery to HTML head. No reliable field Core Web Vitals measurements were available, so no LCP/INP/CLS claim is made. |
| Broken links/404/redirects | Repository audit passed on all nine pages before changes. Live old-style `/practice-areas` redirected to slash; `www` redirected to apex; a nonexistent path returned 404. | Continue link/fragment audit after changes. HTTP/HTTPS and all domain variants need a post-deploy check. |
| Contact | Newcastle/Durban details visible. Form prepares a Gmail draft; it does not transmit or store an enquiry. | Preserve behavior and clarify in QA. |
| Content/duplication | Practice page covers many services; three short Insights sections. Labour terms share one broad page, limiting distinct intent coverage. | Build six useful, differentiated labour service pages; improve existing guide; keep longer article drafts out of production until legal review. |
| Search Console | No deployed Google verification token was found in source; no authenticated Search Console access was available. | Provide connection and measurement steps. Do not infer indexed counts, rankings or query metrics. |

## Live checks performed before changes

`scripts/verify-live.sh` returned HTTP 200 for the six indexable pages, robots, sitemap and social image; 404 for a nonexistent path; and a 301 from `www` to the apex domain. A HEAD request to `/practice-areas` returned 308 to `/practice-areas/`. The live robots file allowed `/` and named the production sitemap. The live sitemap listed six canonical URLs. Live response headers included HSTS, CSP and content-type protections. The live HTML response was retrievable and its text was visible to a public search crawler, but no authenticated Google index data was accessed.

## Source references

- [Google Search Central SEO Starter Guide](https://developers.google.com/search/docs/fundamentals/seo-starter-guide)
- [Google: Build and submit a sitemap](https://developers.google.com/search/docs/crawling-indexing/sitemaps/build-sitemap)
- [Google: Local Business structured data](https://developers.google.com/search/docs/appearance/structured-data/local-business)
- [Official Labour Relations Act](https://www.labour.gov.za/DocumentCenter/Acts/Labour%20Relations/Labour%20Relations%20Act.pdf)
- [CCMA rules information sheet](https://www.ccma.org.za/wp-content/uploads/2025/07/CCMA-Rules-Info-Sheet-2025-01-1.pdf)

This is a source and HTTP audit, not a Google ranking or Core Web Vitals field-data audit. Browser and post-deployment results are recorded in `SEO_IMPLEMENTATION_REPORT.md`.
