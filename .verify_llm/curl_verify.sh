#!/bin/bash
OUT="$2"
: > "$OUT"
while read -r id; do
  [ -z "$id" ] && continue
  line="$id|FAIL"
  for att in 1 2 3 4 5; do
    body=$(curl -sL --max-time 40 "https://export.arxiv.org/api/query?id_list=$id")
    code_ok=$(printf '%s' "$body" | grep -c '<entry>')
    if [ "$code_ok" -ge 1 ]; then
      parsed=$(printf '%s' "$body" | python3 -c "
import sys,re
t=sys.stdin.read()
e=re.search(r'<entry>(.*?)</entry>',t,re.S)
if not e: print('NF'); raise SystemExit
e=e.group(1)
if 'arxiv.org/api/errors' in e: print('NF'); raise SystemExit
tm=re.search(r'<title>(.*?)</title>',e,re.S); pm=re.search(r'<published>(\d{4})',e)
au=re.search(r'<name>(.*?)</name>',e)
ti=re.sub(r'\s+',' ',tm.group(1)).strip() if tm else '?'
print(f\"{pm.group(1) if pm else '?'}|{au.group(1) if au else '?'}|{ti}\")
")
      if [ "$parsed" != "NF" ] && [ -n "$parsed" ]; then line="$id|$parsed"; fi
      break
    fi
    sleep 5
  done
  echo "$line" >> "$OUT"
  sleep 3.5
done < "$1"
echo "===DONE===" >> "$OUT"
