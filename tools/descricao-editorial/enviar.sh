#!/bin/bash
# Uso: enviar.sh <variants|products> <id> <novo.html> <esperado.html>
# Só envia se a descrição atual na loja for igual à esperada (ignora espaço no fim). Usa If-Match.
T=$(mktemp -d)
curl -sS -m 30 -D $T/h -H "x-api-key: proxy-injected" https://api.ereemby.app/api/v2/$1/$2 -o $T/a.json
etag=$(grep -i '^etag:' $T/h | cut -d' ' -f2- | tr -d '\r')
python3 - "$T/a.json" "$4" <<'PY' || { echo " -> pulei $2"; exit 1; }
import json,sys
d=json.load(open(sys.argv[1])); ok=(d.get('description') or '').rstrip()==open(sys.argv[2]).read().rstrip()
print(d.get('name'),'| igual ao esperado:',ok, end=' ')
sys.exit(0 if ok else 1)
PY
python3 -c "import json,sys;json.dump({'description':open(sys.argv[1]).read()},open(sys.argv[2],'w'))" "$3" $T/p.json
curl -sS -m 60 -X PATCH -H "x-api-key: proxy-injected" -H "Content-Type: application/json" -H "If-Match: $etag" --data-binary @$T/p.json https://api.ereemby.app/api/v2/$1/$2 -o $T/r.json -w "| PATCH %{http_code} | "
python3 -c "import json,sys;d=json.load(open(sys.argv[1]));print('salvo igual:',(d.get('description') or '').rstrip()==open(sys.argv[2]).read().rstrip(), d.get('error',''))" $T/r.json "$3"
