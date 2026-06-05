import urllib.request, xml.etree.ElementTree as ET, time, sys
ns={'a':'http://www.w3.org/2005/Atom'}
ids=[l.strip() for l in open(sys.argv[1]) if l.strip()]
out=open(sys.argv[2],'w')
# 一括で問い合わせ（最大効率）。id_listはカンマ区切りで複数可。
def fetch(idlist):
    url="https://export.arxiv.org/api/query?id_list=%s&max_results=100"%",".join(idlist)
    for att in range(6):
        try:
            req=urllib.request.Request(url,headers={'User-Agent':'survey-librarian/1.0'})
            data=urllib.request.urlopen(req,timeout=60).read()
            r=ET.fromstring(data)
            entries=r.findall('a:entry',ns)
            if entries: return entries
        except Exception as e:
            pass
        time.sleep(10)
    return []
# 10件ずつ
results={}
for i in range(0,len(ids),10):
    chunk=ids[i:i+10]
    for e in fetch(chunk):
        idu=e.find('a:id',ns).text
        aid=idu.split('/abs/')[-1].split('v')[0] if '/abs/' in idu else idu
        # versionサフィックス除去
        import re
        m=re.search(r'(\d{4}\.\d{4,5})',aid)
        aid=m.group(1) if m else aid
        t=e.find('a:title',ns).text or ''
        t=re.sub(r'\s+',' ',t).strip()
        y=e.find('a:published',ns).text[:4]
        au=[a.find('a:name',ns).text for a in e.findall('a:author',ns)]
        results[aid]="%s\t%s\t%s"%(y,au[0] if au else '?',t)
    time.sleep(12)
for iid in ids:
    out.write("%s | %s\n"%(iid, results.get(iid,'!!!NOTFOUND')))
out.write("===DONE=== %d/%d found\n"%(len(results),len(ids)))
out.close()
