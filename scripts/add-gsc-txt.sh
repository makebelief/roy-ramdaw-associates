#!/usr/bin/env bash
# Optional terminal alternative to adding the Google verification TXT in Cloudflare's dashboard.
# Requires a *scoped* Cloudflare API token with Zone > DNS > Edit for royramdaw.co.za.
# Usage: export CLOUDFLARE_API_TOKEN=... CF_ZONE_ID=... ; bash scripts/add-gsc-txt.sh
set -euo pipefail
: "${CLOUDFLARE_API_TOKEN:?Export a scoped Cloudflare token with DNS Edit permission (do not paste it into chat)}"
: "${CF_ZONE_ID:?Export the Cloudflare Zone ID for royramdaw.co.za}"
read -r -p 'Paste the complete Google Search Console TXT value (google-site-verification=...): ' GSC_TXT
if [[ ! "$GSC_TXT" =~ ^google-site-verification=[A-Za-z0-9_-]+$ ]]; then
  echo 'ERROR: invalid format. No DNS changes made.' >&2; exit 1
fi
payload="$(GSC_TXT="$GSC_TXT" python3 - <<'PY'
import json, os
print(json.dumps({'type':'TXT','name':'royramdaw.co.za','content':os.environ['GSC_TXT'],'ttl':1,'comment':'Google Search Console ownership verification'}))
PY
)"
response="$(curl --fail-with-body -sS --max-time 30 \
  -X POST "https://api.cloudflare.com/client/v4/zones/${CF_ZONE_ID}/dns_records" \
  -H "Authorization: Bearer ${CLOUDFLARE_API_TOKEN}" \
  -H 'Content-Type: application/json' -d "$payload")"
CF_RESULT="$response" python3 - <<'PY'
import json, os, sys
try: result=json.loads(os.environ['CF_RESULT'])
except Exception as e:print('ERROR: invalid API response');sys.exit(1)
if not result.get('success'):
 print('ERROR: Cloudflare DNS record creation failed:',result.get('errors',[]));sys.exit(1)
print('SUCCESS: Google TXT record created in Cloudflare DNS. Return to Search Console and click Verify.')
PY
unset GSC_TXT payload response
