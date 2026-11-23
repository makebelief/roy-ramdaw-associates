# Legal content plan

**Editorial rule:** A South African employment attorney must review legal statements, current legislation, current CCMA rules and the firm's claimed service scope before a new article is published. The three drafts below are outside `public/`, are absent from the sitemap and are not in the site navigation. This keeps unapproved legal guidance out of the deployment package. The existing short labour consultation guide in `/insights/` was expanded with a primary CCMA source and links to relevant services; review that change in the same release sign-off.

| Priority | Draft / working title | Search question and intent | Related service | Publication gate |
|---|---|---|---|---|
| 1 | `content-drafts/unfair-dismissal-south-africa.md` — What constitutes unfair dismissal? | “Was I dismissed unfairly?”; urgent information before contacting counsel | `/unfair-dismissal/` | Confirm law, dates, examples, forum, remedies; attorney sign-off |
| 2 | `content-drafts/ccma-process-south-africa.md` — How does the CCMA process work? | “How do I refer/prepare, and can a lawyer attend?” | `/ccma-representation/` | Confirm current CCMA rules, Rule 25, deadlines and bargaining council distinction |
| 3 | `content-drafts/retrenchment-rights-south-africa.md` — Retrenchment rights and process | “What should be discussed before retrenchment?” | `/retrenchment-employment-disputes/` | Confirm sections 189/189A, severance and forum wording |

Each draft has a proposed search title, distinct angle, internal service and contact links, official sources and specific legal-review points. After approval, convert it to a standalone static page under `public/insights/<slug>/`, add unique metadata, self-canonical, Article and BreadcrumbList structured data, a link from `/insights/`, reciprocal service links and a sitemap entry. Do not add a date or named author unless verified. Retain a clear general-information disclaimer.

## Next article roadmap

1. **After dismissal: documents and first steps.** Practical checklist linked to unfair dismissal and the existing consultation guide; avoid duplicating the legal-definition draft.
2. **Constructive dismissal: what must be shown?** Narrow question with careful examples and evidence discussion; requires a stronger case-law review.
3. **Disciplinary hearing preparation.** Separate employer and employee checklists, with current Code of Good Practice review.
4. **When does a dispute reach the Labour Court?** Clarify referral versus arbitration, review and court routes; attorney review of deadlines essential.
5. **Employer obligations in workplace disputes.** Address record keeping, consultation and fair process without attempting a complete statutory guide.

Publish gradually based on Search Console query and landing-page evidence, client enquiry themes, legal reviewer availability and the ability to keep pages current. Avoid near-duplicate city or keyword-variant articles.

## Primary references

- [Labour Relations Act 66 of 1995](https://www.labour.gov.za/DocumentCenter/Acts/Labour%20Relations/Labour%20Relations%20Act.pdf)
- [CCMA unfair dismissal guide](https://www.ccma.org.za/wp-content/uploads/2025/08/Unfair-Dismissal-Disputes-info-sheet-2025-01.pdf)
- [CCMA rules information sheet](https://www.ccma.org.za/wp-content/uploads/2025/07/CCMA-Rules-Info-Sheet-2025-01-1.pdf)
- [Google Search Central: helpful, reliable content](https://developers.google.com/search/docs/fundamentals/creating-helpful-content)
