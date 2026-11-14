#!/usr/bin/env python3
"""Sequential macro design continuation, retaining every solver and audit outcome."""
import argparse,json,subprocess,sys,time
from pathlib import Path
p=argparse.ArgumentParser();p.add_argument('--source-root',type=Path,required=True);p.add_argument('--modes',type=int,default=8);p.add_argument('--amplitudes',nargs='+',type=float,required=True);p.add_argument('--restart',type=Path,required=True);p.add_argument('--tol',type=float,default=2e-6);p.add_argument('--physical-bc-tol',type=float,default=1e-9);p.add_argument('--nodes',type=int,default=401);p.add_argument('--max-nodes',type=int,default=2000);a=p.parse_args()
S=Path(__file__).resolve().parent;N=S.parent/'notes';restart=a.restart;rows=[]
for q in a.amplitudes:
 label=f'{q:.5f}'.rstrip('0').replace('.','p');out=N/f'2026-11-09-950f-prefix-adaptive-cont-m{a.modes}-q{label}'
 args=[sys.executable,str(S/'950f-prefix-adaptive-chart-bvp.py'),'--source-root',str(a.source_root),'--profile',str(N/'2026-11-09-950f-prefix-weighted-k6-profile.json'),'--chart',str(N/'2026-11-09-950f-prefix-adaptive-chart.json'),'--linear-port',str(N/'2026-11-09-950f-prefix-weighted-k6-port96-cusp1024.json'),'--out-prefix',str(out),'--amplitude',str(q),'--warp-reference',str(q),'--modes',str(a.modes),'--angular',str(max(256,32*a.modes)),'--audit-angular',str(max(512,64*a.modes)),'--nodes',str(a.nodes),'--max-nodes',str(a.max_nodes),'--tol',str(a.tol),'--bc-tol','1e-7','--physical-bc-tol',str(a.physical_bc_tol),'--restart',str(restart)]
 start=time.time()
 with out.with_name(out.name+'-run.log').open('w')as f:r=subprocess.run(args,stdout=f,stderr=subprocess.STDOUT)
 row=dict(q=q,code=r.returncode,seconds=time.time()-start,command=args)
 sf=out.with_name(out.name+'-summary.json')
 if sf.exists():
  data=json.loads(sf.read_text());summary=data['summary'];row.update(success=data['solver_success'],delta=data['frozen_profile']['delta'],nodes=data['nodes'],**{k:summary[k]for k in ('metric_l1','flow_defect','darboux_l1','kappa_sample','root_min','terminal_height_coeff_max')})
 rows.append(row);(N/f'2026-11-09-950f-prefix-continuation-m{a.modes}-summary.json').write_text(json.dumps(rows,indent=2)+'\n');print(json.dumps({k:v for k,v in row.items()if k!='command'}),flush=True)
 if r.returncode or not row.get('success')or row['metric_l1']>.001:break
 restart=out.with_suffix('.json.gz')
