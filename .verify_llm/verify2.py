import urllib.request, xml.etree.ElementTree as ET, time, sys, re
ns={'a':'http://www.w3.org/2005/Atom'}
ids=[l.strip() for l in open(sys.argv[1]) if l.strip()]
outp=sys.argv[2]
def fetch(idlist):
    url="https://export.arxiv.org/api/query?id_list=%s&max_results=100"%",".join(idlist)
    for att in range(8):
        try:
            req=urllib.request.Request(url,headers={'User-Agent':'survey-librarian/1.0 mailto:s25705@cyberagent.email'})
            data=urllib.request.urlopen(req,timeout=60).read()
            r=ET.fromstring(data)
            entries=r.findall('a:entry',ns)
            if entries: return entries
        except Exception:
            pass
        time.sleep(6)
    return []
results={}
out=open(outp,'w')
for i in range(0,len(ids),8):
    chunk=ids[i:i+8]
    for e in fetch(chunk):
        idu=e.find('a:id',ns).text or ''
        m=re.search(r'(\d{4}\.\d{4,5})',idu)
        aid=m.group(1) if m else idu
        t=re.sub(r'\s+',' ',(e.find('a:title',ns).text or '')).strip()
        y=(e.find('a:published',ns).text or '????')[:4]
        au=[a.find('a:name',ns).text for a in e.findall('a:author',ns)]
        results[aid]="%s\t%s\t%s"%(y,au[0] if au else '?',t)
    # 逐次フラッシュ
    out.seek(0); out.truncate()
    for iid in ids:
        out.write("%s | %s\n"%(iid, results.get(iid,'!!!NOTFOUND')))
    out.write("PROGRESS %d/%d\n"%(min(i+8,len(ids)),len(ids)))
    out.flush()
    time.sleep(4)
out.seek(0); out.truncate()
for iid in ids:
    out.write("%s | %s\n"%(iid, results.get(iid,'!!!NOTFOUND')))
out.write("===DONE=== %d/%d found\n"%(len(results),len(ids)))
out.close()
