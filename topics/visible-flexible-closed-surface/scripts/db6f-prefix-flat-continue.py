#!/usr/bin/env python3
"""Continuation of nonlinear flat-profile prefixes with finite linear tail port.
Changing amplitude in this design phase permits the meridian delta to change;
this is not a fixed-metric convergence experiment.
"""
import argparse,json,subprocess,sys,time
from pathlib import Path
p=argparse.ArgumentParser();p.add_argument('--source-root',type=Path,required=True);p.add_argument('--profile',type=Path,required=True);p.add_argument('--amplitudes',type=float,nargs='+',required=True);p.add_argument('--modes',type=int,default=4);p.add_argument('--restart',type=Path);p.add_argument('--tag',required=True);a=p.parse_args()
S=Path(__file__).resolve().parent;N=S.parent/'notes';restart=a.restart;rows=[]
for q in a.amplitudes:
 label=f'{q:.6f}'.rstrip('0').replace('.','p');out=N/f'2026-11-09-db6f-prefix-{a.tag}-m{a.modes}-q{label}'
 cmd=[sys.executable,str(S/'db6f-prefix-flat-linear.py'),'--source-root',str(a.source_root),'--profile',str(a.profile),'--chart',str(N/'2026-11-09-950f-prefix-adaptive-chart.json'),'--linear-port',str(N/'2026-11-09-950f-prefix-weighted-k6-port96-cusp1024.json'),'--out-prefix',str(out),'--amplitude',str(q),'--warp-reference',str(q),'--modes',str(a.modes),'--angular',str(max(128,32*a.modes)),'--audit-angular',str(max(384,64*a.modes)),'--nodes','401','--max-nodes','3200','--tol','2e-7','--bc-tol','1e-7','--physical-bc-tol','2e-9']
 if restart:cmd+=['--restart',str(restart)]
 start=time.time()
 with out.with_name(out.name+'-run.log').open('w')as f:r=subprocess.run(cmd,stdout=f,stderr=subprocess.STDOUT)
 row=dict(q=q,command=cmd,exit_code=r.returncode,seconds=time.time()-start);summary=out.with_name(out.name+'-summary.json')
 if summary.exists():
  d=json.loads(summary.read_text());z=d.get('summary',{});row.update(success=d.get('solver_success'),delta=d.get('frozen_profile',{}).get('delta'),metric=z.get('metric_l1'),flow=z.get('flow_defect'),darboux=z.get('darboux_l1'),curvature=z.get('kappa_sample'),tail_height=z.get('terminal_height_coeff_max'),core=z.get('core'))
 rows.append(row);(N/f'2026-11-09-db6f-prefix-{a.tag}-continuation-summary.json').write_text(json.dumps(rows,indent=2)+'\n');print(json.dumps({k:v for k,v in row.items()if k not in ('command','core')}),flush=True)
 if r.returncode or not row.get('success'):break
 restart=out.with_suffix('.json.gz')
