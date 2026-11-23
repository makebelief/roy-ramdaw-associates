# SEO implementation and deployment handoff

**Prepared:** 23 November 2026<br>
**Baseline:** `origin/cloudflare-production` at `540de93`<br>
**Branch:** `seo/comprehensive-optimization`<br>
**Implementation commit:** `412186b`<br>
**Production status:** Not deployed or pushed. Existing live site remains unchanged.

## What will change on the live site after approval and deployment

The existing visual system, header navigation, footer design, responsive breakpoints, imagery and Gmail-draft enquiry flow remain in use. The homepage and practice index explain labour services more clearly. Six new static service pages offer distinct routes for labour and employment law, unfair dismissal, CCMA processes, retrenchment, Labour Court matters, and contracts/disciplinary matters. The homepage, practice index, bio, Insights guide, contact page and footer link to those pages. The production sitemap will grow from 6 to **12 indexable URLs**.

Three longer article drafts are held outside `public/`, so they will **not** be deployed until a South African attorney reviews and approves them. The current indexed labour consultation guide has been expanded with a CCMA source and contextual links.

## Files changed

| Group | Files |
|---|---|
| New deployable service pages | `public/labour-employment-law/index.html`, `public/unfair-dismissal/index.html`, `public/ccma-representation/index.html`, `public/retrenchment-employment-disputes/index.html`, `public/labour-court/index.html`, `public/employment-contracts-disciplinary/index.html` |
| Existing deployable pages | `public/index.html`, `public/practice-areas/index.html`, `public/managing-partner/index.html`, `public/insights/index.html`, `public/contact/index.html`, plus `public/about/index.html`, `public/privacy/index.html`, `public/terms/index.html`, `public/404.html` for consistent footer/font/schema markup |
| Technical and verification | `public/sitemap.xml`, `public/assets/site.css`, `scripts/audit.py`, `scripts/verify-live.sh`, `scripts/generate_service_pages.py` |
| Documentation and drafts | `README.md`, the five `SEO_*.md` deliverables, and three files in `content-drafts/` |

No repository-root legacy site files, contact-form JavaScript, credentials or unrelated projects were changed. `public/robots.txt` was already correct and remains unchanged.

## Page and keyword targets

| Page | Primary topic | Supporting terms / intent |
|---|---|---|
| `/` | Newcastle attorneys and verified firm services | labour, energy law, African finance, litigation |
| `/labour-employment-law/` | labour and employment attorney in Newcastle | workplace dispute, employment law South Africa |
| `/unfair-dismissal/` | unfair dismissal attorney | dismissal advice, constructive dismissal, referral |
| `/ccma-representation/` | CCMA advice and permitted representation | conciliation, arbitration, CCMA lawyer Newcastle |
| `/retrenchment-employment-disputes/` | retrenchment advice | section 189 consultation, employment dispute |
| `/labour-court/` | Labour Court proceedings | court litigation and review enquiries |
| `/employment-contracts-disciplinary/` | contracts and disciplinary matters | contract review, hearing preparation |

The full intent and competition-evidence mapping is in `SEO_KEYWORD_STRATEGY.md`. No search volume, difficulty or position figures were invented.

## Metadata, local and technical improvements

- Refined unique homepage, practice index and Insights titles/descriptions and made their H1 wording more descriptive. New pages each have one H1, unique title and description, a self-referencing canonical, matching Open Graph URL and social metadata.
- Added descriptive internal routes from high-visibility entry points and related service links on each new page. Existing practice fragments continue to work.
- New pages use `LegalService`, `Service` and `BreadcrumbList` JSON-LD with a stable provider ID. Existing business data was normalized to use that ID and to describe the Newcastle head office and Durban firm office without treating the Johannesburg associated office as a branch. The attorney page now has a `Person` entity based on the existing documented profile.
- Updated the sitemap to list the 12 intended indexable production URLs only. Existing privacy, terms and 404 `noindex` directives remain; the new service pages allow indexing. Robots still allows appropriate crawling and names the sitemap.
- Moved the existing Google Fonts CSS request from an `@import` in `site.css` to HTML heads to eliminate one stylesheet-discovery step. Existing font family and display mode remain. Local production assets total about **682 KiB before transfer compression**, compared with **604 KiB** at baseline; new HTML causes the increase. This is **not** an LCP, INP or CLS measurement.
- Updated the post-deploy live smoke script to check all six new URLs. The static audit now checks unique titles/descriptions, OG fields and service structured-data presence in addition to links, fragments, canonicals, sitemap, robots and JSON validity.

## Verification performed

| Check | Result |
|---|---|
| Pre-change live smoke test | Six original pages, robots, sitemap and social image: HTTP 200; nonexistent route: 404; `www` redirect: 301; slash redirect on `/practice-areas`: 308. |
| Static audit after changes | `python3 scripts/audit.py`: **PASS**, 15 HTML pages, 12 indexable, no broken local links/anchors, no unexpected noindex, correct sitemap and canonical metadata. |
| Browser check | Headless Chrome loaded all 12 indexable routes at 1440px and 390px; each had expected H1/title/CSS and no horizontal page overflow. Mobile navigation opened. |
| Contact behavior | On the local contact page, a valid test submission with `?area=labour` prepared a Gmail compose URL addressed to the published email and displayed the existing “not sent” message. `window.open` was intercepted during the test; no email was sent. |
| Source checks | `python3 -m py_compile` for audit/generator, `node --check public/assets/site.js`, `git diff --check`: PASS. JSON-LD syntax and required local service links checked by the static audit. |
| Build | Static site: no package/build command. The deployment artifact is the checked `public/` directory. |

Screenshots of the local home desktop and unfair-dismissal mobile views were reviewed. A full Google Rich Results Test, real-user Core Web Vitals report and post-deployment live check have **not** been run. Google may choose different canonical or snippet text after crawling.

## Items requiring confirmation or legal review

1. The firm should reconfirm the Newcastle and Durban addresses, phone numbers, published email, WhatsApp availability and director credentials/profile claims before approving deployment. The site already carried these details; this branch does not invent them.
2. A South African attorney should review all six new service pages and the updated labour Insights guide for current law, CCMA representation rules, referral wording and the firm's precise scope of work.
3. The three article drafts require attorney sign-off before they are moved into `public/`, linked and added to the sitemap.
4. No authenticated Google Search Console data was available. Verification, sitemap submission, indexing inspection and query analysis remain post-deployment actions.
5. External Pexels photos and Google Fonts remain network dependencies. Browser checks showed responsive rendering, but no reliable before/after Core Web Vitals data was available. Obtain field data through Search Console or PageSpeed Insights after launch.

## Deployment instructions and measurement

After client and legal approval, review the branch diff against `origin/cloudflare-production` and fast-forward the approved work into that branch. The Cloudflare Pages project uses **Direct Upload**, with `cloudflare-production` as its production branch label. Deploy **`public/`** to the existing `roy-ramdaw-associates` project using Wrangler and the current commit hash. Do not deploy the legacy repository root. Run `bash scripts/verify-live.sh` after the new deployment; inspect the six new pages and the contact draft on real desktop/mobile browsers. Check production robots, sitemap, canonicals, HTTP status and structured data using Google's supported tools. If a defect is found, fix it before submitting the sitemap.

Then verify the Search Console property for `royramdaw.co.za` (prefer a Domain property with DNS verification), submit the sitemap and inspect representative URLs. Compare qualified organic enquiries and Search Console query × page impressions, clicks, CTR and positions against a recorded pre-deployment baseline. The prioritized weekly actions are in `SEO_90_DAY_ROADMAP.md`. Search visibility and ranking outcomes cannot be guaranteed.
