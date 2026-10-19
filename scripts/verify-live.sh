#!/usr/bin/env bash
# Run only after Cloudflare is active and HTTPS is provisioned.
set -euo pipefail
BASE="${1:-https://royramdaw.co.za}"
BASE="${BASE%/}"
case "$BASE" in https://*) ;; *) echo 'ERROR: supply an https:// URL'; exit 2 ;; esac
fetch_status() {
  local url="$1" expected="$2" status
  status="$(curl -sSL -o /dev/null -w '%{http_code}' --max-time 30 "$url")"
  echo "$status  $url"
  [[ "$status" == "$expected" ]] || { echo "FAILED: expected $expected" >&2; exit 1; }
}
for p in '/' '/about/' '/practice-areas/' '/managing-partner/' '/insights/' '/contact/' '/robots.txt' '/sitemap.xml' '/assets/roy-ramdaw-social-preview-2026.jpg'; do
  fetch_status "$BASE$p" 200
done
fetch_status "$BASE/this-route-should-not-exist-roy-test" 404
headers="$(curl -sSI --max-time 30 "$BASE/")"
echo "$headers" | grep -qi '^content-security-policy:' || { echo 'FAILED: CSP header missing'; exit 1; }
echo "$headers" | grep -qi '^strict-transport-security:' || { echo 'FAILED: HSTS header missing'; exit 1; }
canonical="$(curl -fsSL --max-time 30 "$BASE/")"
echo "$canonical" | grep -q 'https://royramdaw.co.za/' || { echo 'FAILED: canonical not found'; exit 1; }
! echo "$canonical" | grep -q 'roy-ramdaw-associates.vercel.app' || { echo 'FAILED: old Vercel reference'; exit 1; }
redirect_header="$(curl -sSI --max-time 30 'https://www.royramdaw.co.za/about/?ref=verification' || true)"
echo "$redirect_header" | head -n 3
echo "$redirect_header" | grep -Eqi '^HTTP/.* (301|308)' || { echo 'FAILED: www redirect must be 301 or 308'; exit 1; }
echo "$redirect_header" | grep -qi '^location: https://royramdaw.co.za/about/?ref=verification' || { echo 'FAILED: www redirect path/query not preserved'; exit 1; }
echo 'PASS: live deployment and www canonicalization smoke test'
