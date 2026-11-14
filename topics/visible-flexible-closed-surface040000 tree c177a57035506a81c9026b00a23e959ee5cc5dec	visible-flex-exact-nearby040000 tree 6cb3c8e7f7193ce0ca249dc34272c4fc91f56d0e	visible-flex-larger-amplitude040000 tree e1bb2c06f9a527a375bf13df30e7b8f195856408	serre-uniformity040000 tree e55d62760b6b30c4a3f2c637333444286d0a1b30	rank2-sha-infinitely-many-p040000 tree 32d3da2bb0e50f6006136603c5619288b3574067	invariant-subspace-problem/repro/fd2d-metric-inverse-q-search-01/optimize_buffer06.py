import json
from pathlib import Path
from optimize_buffer04 import one
old=json.loads(Path('positive-q-widen-02.json').read_text())['rows'];row=next(x for x in old if x['right']==.65)
prev=json.loads(Path('positive-q-hardbg-04.json').read_text())['reports'];seed=next(x for x in prev if x['result']['right']==.65)['params'];reports=[]
for w in [.03,.01]:
 r=one(row,outer=w,seed=seed);seed=r['params'];reports.append(r)
 Path('positive-q-low-outerw-06.json').write_text(json.dumps(dict(reports=reports),indent=2)+'\n')
 print(json.dumps({k:v for k,v in r.items()if k not in ['params','coefficients','initial']}),flush=True)
