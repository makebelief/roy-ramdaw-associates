# Roy Ramdaw & Associates Inc. website

The production site at **https://royramdaw.co.za/** is a static Cloudflare Pages **Direct Upload** project. Deploy **`public/`** with the Wrangler CLI and label the deployment `cloudflare-production`. The Git branch of that name tracks the production source; pushing it alone does not trigger deployment. There is no npm build step. The repository-root HTML, CSS, robots and sitemap files are an older, unapproved Vercel concept and are **not deployment source**. In particular, their noindex directives and `vercel.app` URLs do not describe the current live site.

## Local preview and checks

```bash
python3 -m http.server 8000 --directory public
python3 scripts/audit.py
```

Open http://localhost:8000/. The audit checks page metadata, canonical URLs, JSON-LD syntax, links, fragments, image alt text, sitemap and robots. New labour service pages can be regenerated with `python3 scripts/generate_service_pages.py`; their content and source references are maintained in that script. Rerun the audit afterward.

## Deployment preparation

Deploy **`public/`**, not the repository root. The existing Cloudflare Pages project is `roy-ramdaw-associates`, with production branch label `cloudflare-production`. `public/_headers` and `public/_redirects` contain Cloudflare Pages-specific rules. After an approved deployment, run `bash scripts/verify-live.sh`, inspect the new URLs, and submit `https://royramdaw.co.za/sitemap.xml` in a verified Google Search Console property.

The contact form prepares a Gmail draft in a new tab; it does not send or store enquiries on the website. A `mailto:` fallback is shown. Test the draft behavior and confirm listed phone numbers, addresses and professional details with the firm before deployment.

Three longer employment-law article drafts are stored in `content-drafts/` outside the deployable directory. They require South African attorney review before publication. See `SEO_IMPLEMENTATION_REPORT.md` for the release checklist, and `CLIENT-CHANGELOG.md` for the provenance of earlier client-supplied professional and office information.
