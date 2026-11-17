#!/usr/bin/env python3
"""Observe the original fixed-g driver without changing its mathematics."""
import argparse,hashlib,json,sys
from pathlib import Path
p=argparse.ArgumentParser(add_help=False)
p.add_argument('--runtime',type=Path,required=True)
a,rest=p.parse_known_args();source=a.runtime/'refine_fixed_large_radius.py'
observer=a.runtime/'trace_domain_newton.py'
text=source.read_text();source_hash=hashlib.sha256(source.read_bytes()).hexdigest()
transforms=[('install();started=time.monotonic()',
    "install();from trace_domain_newton import install as trace_install;trace_install(a.out.with_name(a.out.name+'-newton.jsonl'));started=time.monotonic()"),
    ("row=seed['diagnostics'];row['arguments']", "row=seed['diagnostics'];row['observer_provenance']=OBSERVER_PROVENANCE;row['arguments']")]
for before,after in transforms:
    if text.count(before)!=1:raise RuntimeError('Observer installation source mismatch')
    text=text.replace(before,after)
provenance=dict(scope=__doc__,base_sha256=source_hash,observer_sha256=hashlib.sha256(observer.read_bytes()).hexdigest(),
                wrapper_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),transforms=transforms,original_command=sys.argv)
print(json.dumps(dict(event='observer_installed',**provenance)),flush=True)
sys.path.insert(0,str(a.runtime.resolve()));sys.argv=[str(source),*rest]
exec(compile(text,str(source),'exec'),dict(__name__='__main__',__file__=str(source),OBSERVER_PROVENANCE=provenance))
