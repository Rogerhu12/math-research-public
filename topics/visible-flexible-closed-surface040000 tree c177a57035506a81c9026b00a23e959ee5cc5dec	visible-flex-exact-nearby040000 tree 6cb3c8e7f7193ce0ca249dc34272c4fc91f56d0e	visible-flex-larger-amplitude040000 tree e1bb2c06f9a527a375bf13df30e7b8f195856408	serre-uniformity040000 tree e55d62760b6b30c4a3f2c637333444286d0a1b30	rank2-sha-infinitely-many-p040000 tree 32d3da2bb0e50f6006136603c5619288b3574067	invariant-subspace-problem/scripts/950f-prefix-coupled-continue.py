#!/usr/bin/env python3
"""Joint prefix/nonlinear-tail design continuation with complete checkpoint retention."""
import argparse,json,subprocess,sys,time
from pathlib import Path
p=argparse.ArgumentParser();p.add_argument('--source-root',type=Path,required=True);p.add_argument('--amplitudes',nargs='+',type=float,required=True);p.add_argument('--restart',type=Path,required=True);p.add_argument('--tail-state',type=Path,required=True);p.add_argument('--modes',type=int,default=8);p.add_argument('--tail-config',type=Path,required=True);p.add_argument('--tag',default='coupled-v2');a=p.parse_args()
S=Path(__file__).resolve().parent;N=S.parent/'notes';restart=a.restart;tailstate=a.tail_state;rows=[]
for q in a.amplitudes:
 label=f'{q:.5f}'.rstrip('0').replace('.','p');out=N/f'2026-11-09-950f-prefix-{a.tag}-m{a.modes}-q{label}';cfg=json.loads(a.tail_config.read_text());cfg['initialCheckpoint']=str(tailstate.resolve());cfg['traceFile']=str(out.with_name(out.name+'-tail-trace.jsonl'));cfgfile=out.with_name(out.name+'-tail-config.json');cfgfile.write_text(json.dumps(cfg,indent=2)+'\n')
 cmd=[sys.executable,str(S/'950f-prefix-nonlinear-coupling-v2.py'),'--source-root',str(a.source_root),'--profile',str(N/'2026-11-09-950f-prefix-weighted-k6-profile.json'),'--chart',str(N/'2026-11-09-950f-prefix-adaptive-chart.json'),'--linear-port',str(N/'2026-11-09-950f-prefix-weighted-k6-port96-cusp1024.json'),'--tail-config',str(cfgfile),'--out-prefix',str(out),'--restart',str(restart),'--amplitude',str(q),'--warp-reference',str(q),'--modes',str(a.modes),'--angular',str(max(256,32*a.modes)),'--audit-angular',str(max(512,64*a.modes)),'--nodes','601','--max-nodes','2400','--tol','2e-7','--bc-tol','1e-7','--physical-bc-tol','2e-9','--node-heap','1024','--warmup-scales','.5','1']
 start=time.time()
 with out.with_name(out.name+'-run.log').open('w')as f:r=subprocess.run(cmd,stdout=f,stderr=subprocess.STDOUT)
 row=dict(q=q,exit_code=r.returncode,seconds=time.time()-start,command=cmd);sf=out.with_name(out.name+'-summary.json')
 if sf.exists():
  d=json.loads(sf.read_text());row.update(success=d.get('solver_success',False),error=d.get('error'))
  if 'summary'in d:
   z=d['summary'];seam=d['tail_seam'];row.update(delta=d['frozen_profile']['delta'],metric=z['metric_l1'],flow=z['flow_defect'],darboux=z['darboux_l1'],kappa=z['kappa_sample'],first_mean_mismatch=seam['mean_first_mismatch'],second_mean_mismatch=seam['mean_second_mismatch'],cut_c1_metric=seam['cut_metric_c1_fft_l1'],tail_calls=d['tail_calls'])
 rows.append(row);(N/f'2026-11-09-950f-prefix-{a.tag}-continuation-summary.json').write_text(json.dumps(rows,indent=2)+'\n');print(json.dumps({k:v for k,v in row.items()if k!='command'}),flush=True)
 if r.returncode or not row.get('success')or row.get('metric',1)>.001:break
 restart=out.with_suffix('.json.gz');tailstate=N/d['tail_seam']['tail_record']
