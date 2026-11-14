#!/usr/bin/env python3
"""Record source hashes used by the prefix and actual-tail continuation tools.

The prior Python runtime import snapshot is retained as the seed. Literal
local JavaScript imports and the explicit sourceURL/loadClosingTailSource
references are followed transitively. This is a source manifest, not a claim
that arbitrary dynamic imports were discovered or that external data exist.
"""
import argparse,datetime,hashlib,json,re,sys
from pathlib import Path
import numpy,scipy

def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--source-root',type=Path,required=True)
    p.add_argument('--prior',type=Path,required=True)
    p.add_argument('--out',type=Path,required=True)
    a=p.parse_args();here=Path(__file__).resolve().parent
    prior=json.loads(a.prior.read_text());external=a.source_root/'topics/large-amplitude-twist-flex/scripts'
    pending={Path(name)for name in prior['files']}
    pending.update(here.glob('db6f-prefix-*.py'));pending.update(here.glob('db6f-prefix-*.mjs'))
    for name in ('950f-tail-stage-port-v3.mjs','950f-tail-client-v3.py'):
        pending.add(here/name)
    files={};missing=[]
    while pending:
        file=pending.pop().resolve()
        if str(file)in files:continue
        if not file.is_file():missing.append(str(file));continue
        data=file.read_bytes();files[str(file)]=dict(bytes=len(data),sha256=hashlib.sha256(data).hexdigest())
        if file.suffix not in ('.mjs','.js'):continue
        text=data.decode()
        for rel in re.findall(r'''(?:from\s*|import\s*\()?["'](\./[^"']+\.(?:mjs|js))["']''',text):
            pending.add(file.parent/rel)
        for name in re.findall(r'''(?:sourceURL|loadClosingTailSource)\(["']([^"']+)["']\)''',text):
            pending.add(external/name)
        for name in re.findall(r'''path\.join\(sourceRoot,["']topics/large-amplitude-twist-flex/scripts/([^"']+)["']\)''',text):
            pending.add(external/name)
    result=dict(scope=__doc__,time_utc=datetime.datetime.now(datetime.timezone.utc).isoformat(),
      python=sys.version,numpy=numpy.__version__,scipy=scipy.__version__,source_root=str(a.source_root),
      prior_manifest=str(a.prior),prior_manifest_sha256=hashlib.sha256(a.prior.read_bytes()).hexdigest(),
      files=dict(sorted(files.items())),missing=sorted(set(missing)))
    a.out.write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(dict(files=len(files),source_bytes=sum(v['bytes']for v in files.values()),
                         missing=len(result['missing']),out=str(a.out))))
    if missing:raise SystemExit(1)

if __name__=='__main__':main()
