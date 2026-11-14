import json
from pathlib import Path
from optimize_coupled08 import one,cases
low=json.loads(Path('positive-q-low-outerw-06.json').read_text())['reports'];seed=next(x for x in low if x['target_outer']==.01)['params'];out=[]
for w in [.01,.003,.001]:
 r=one(cases[0],seed,outer=w);seed=r['params'];out.append(r)
 Path('positive-q-coupled-low-09.json').write_text(json.dumps(dict(reports=out),indent=2)+'\n');print(json.dumps({k:v for k,v in r.items()if k not in ['params','coefficients']}),flush=True)
