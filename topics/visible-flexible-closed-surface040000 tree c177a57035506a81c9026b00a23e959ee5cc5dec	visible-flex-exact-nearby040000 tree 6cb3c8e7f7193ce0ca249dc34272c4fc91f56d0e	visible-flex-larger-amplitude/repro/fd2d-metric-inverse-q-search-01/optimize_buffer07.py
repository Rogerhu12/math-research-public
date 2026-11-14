import json
from pathlib import Path
import positive_q as old
from optimize_buffer04 import one
row=next(x for x in json.loads(Path('positive-q-widen-02.json').read_text())['rows'] if x['right']==.65)
base=next(x for x in json.loads(Path('positive-q-hardbg-04.json').read_text())['reports'] if x['result']['right']==.65)
ports=[(2,.3435132337600405,.0021611134196327392,-.002765767408468409),(3,.32979773239101795,.00035195102932240657,-.0005843747292083639)]
reports=[]
for N,a,w,wr in ports:
 old.a=a;old.w0=w;old.k0=wr/w
 seed=base['params']
 for outw in [.1,.03]:
  r=one(row,outer=outw,seed=seed);seed=r['params'];r['replace_outer_cells']=N;r['numerical_inner_port']=dict(left=a,w0=w,wr0=wr)
  reports.append(r);Path('positive-q-inner-ports-07.json').write_text(json.dumps(dict(reports=reports),indent=2)+'\n')
  print(json.dumps({k:v for k,v in r.items()if k not in ['params','coefficients','initial']}),flush=True)
