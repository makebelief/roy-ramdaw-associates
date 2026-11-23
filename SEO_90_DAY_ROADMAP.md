# First 90 days after an approved SEO deployment

The schedule begins on the **actual deployment date**, not the date this branch was prepared. A verified Google Search Console property is needed for query, indexing and Core Web Vitals data. No ranking or traffic forecast is assumed.

| Window | Action | Evidence / decision |
|---|---|---|
| Days 0–2 | Verify production branch and `public/` output, obtain deployment approval, deploy, then run `scripts/verify-live.sh`. Inspect the six new pages, metadata, HTTP status, sitemap, robots, desktop/mobile layout, navigation and contact draft. | Record deployment URL, commit, screenshots and any fixes. |
| Days 1–7 | Add or confirm a Search Console **Domain property** for `royramdaw.co.za` using DNS verification. If a Domain property cannot be verified, add the `https://royramdaw.co.za/` URL-prefix property and follow Google's supported verification method. Submit `https://royramdaw.co.za/sitemap.xml`. | Confirm ownership and sitemap read status; inspect home and two new service URLs with URL Inspection. Do not claim submission until completed. |
| Days 7–14 | Review Page Indexing coverage for the 12 intended indexable URLs. Check selected canonical, crawl accessibility and unexpected exclusions. | Correct actual errors; keep privacy, terms and 404 out of the index. |
| Days 14–30 | Establish a query × landing-page baseline for labour, unfair dismissal, CCMA and Newcastle terms. Track impressions, clicks, CTR and average position; separate branded and non-branded queries. | Identify pages with impressions but low CTR or mismatched intent. Small counts can fluctuate; avoid premature conclusions. |
| Days 30–45 | Attorney reviews the three article drafts. Publish only signed-off articles, one at a time, with proper structured data and internal links. | Recheck legal sources, sitemap, metadata and indexing for each publication. |
| Days 45–60 | Review actual enquiries and Search Console queries. Improve wording or answers on pages that attract relevant impressions but fail to address the question. | Note the change date and compare like-for-like query groups. |
| Days 60–90 | Recheck technical health, links, Core Web Vitals field reports where available and mobile usability. Decide whether more legal articles or additional verified service pages are justified. | Report changes in qualified organic enquiries, clicks and indexed pages, with a comparable pre/post period. |

## Measurement priorities

1. **Qualified enquiries from organic search:** ask the firm to record source and matter type at intake without collecting sensitive details in analytics. Website form currently opens a Gmail draft, so it does not provide a reliable server-side conversion event.
2. **Search Console query and page performance:** compare brand and non-brand terms separately. A rise in impressions without relevant enquiries may signal weak intent fit.
3. **Indexing and canonical coverage:** confirm that all intended service URLs can be indexed and that no draft or legal pages are unintentionally indexed.
4. **Experience metrics:** use Search Console Core Web Vitals and PageSpeed Insights after deployment; record mobile LCP, INP and CLS with field data when available.
5. **Editorial upkeep:** recheck legal statements and external source links at least quarterly or after material law/rule changes.

[Google Search Console setup guidance](https://developers.google.com/search/docs/monitor-debug/search-console-start) and [sitemap guidance](https://developers.google.com/search/docs/crawling-indexing/sitemaps/build-sitemap) describe the verification, inspection and submission steps. A sitemap helps discovery but does not guarantee indexing or ranking.
