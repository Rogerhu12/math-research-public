#!/usr/bin/env python3
"""Rebuild the exact pinned original X/Y scratch inputs for archived probes.
This is a regeneration helper, not an additional exclusion certificate.
"""
from pathlib import Path
import json,hashlib,sys
seed=Path(__file__).with_name('2026-11-27-unit211-L0-V-complete-original-return-8542.py')
assert hashlib.sha256(seed.read_bytes()).hexdigest()=='39efe1cbf347ab72879c0c5fa1e76ab7e082438febaedd5a6fc1a809de627352'
text=seed.read_text();prefix=text.split("full=norm(Vcurve.resultant(X,'w'))",1)[0]
namespace={'__file__':str(seed),'__name__':'__probe_input_regenerator__'}
exec(compile(prefix,str(seed),'exec'),namespace)
cache=Path(sys.argv[1]) if len(sys.argv)>1 else Path('/workspace/scratch/8542378f2b73')
cache.mkdir(parents=True,exist_ok=True)
for name,key,sha in [('P1_N1','X','519fe7c69a0cf7c05283aa66833331b64e7654bb6ec0daec606c49b2c2a02f68'),('P1_EBe','Y','c696ee10ac72763cbc2d9e01cd84cdda6bfd5116faa3262ddbf6f96490c54d33')]:
 pp=namespace[key];assert hashlib.sha256(str(pp).encode()).hexdigest()==sha
 (cache/('L0_XY_'+name+'.json')).write_text(json.dumps([[list(map(int,m)),str(a)] for m,a in pp.to_dict().items()]))
namespace['signal'].alarm(0)
