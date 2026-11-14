from pathlib import Path
import json,gzip,subprocess,hashlib,os,datetime
B=Path('/workspace/scratch/d1aa462cfc02');T=B/'math-research/topics/visible-flex-larger-amplitude';W=B/'root-work/R176-owned-cells';W.mkdir(exist_ok=True);plan=B/'root-work/r127/R176-v2-owned-cells-plan.json';p=json.loads(plan.read_text());source=Path(p['source']);assert hashlib.sha256(source.read_bytes()).hexdigest()==p['source_sha256'];prior=None;rows=[]
for cell in (9,8,7):
 ready=[]
 for q in W.glob(f'cell{cell}-attempt*-resource.json'):
  r=json.loads(q.read_text());pref=Path(str(q).removesuffix('-resource.json'));primary=Path(str(pref)+'-result-certificate.json.gz')
  if r['exitcode']==0 and primary.exists():
   d=json.loads(gzip.decompress(primary.read_bytes()))
   if d['source_sha256']==p['source_sha256'] and d['all_gates'] and d['finished_cell']==cell:ready.append((q,primary))
 if ready:
  assert len(ready)==1;res,primary=ready[0]
 else:
  attempt=1
  while any(W.glob(f'cell{cell}-attempt{attempt:02d}*')):attempt+=1
  pref=W/f'cell{cell}-attempt{attempt:02d}';res=Path(str(pref)+'-resource.json');primary=Path(str(pref)+'-result-certificate.json.gz');log=Path(str(pref)+'.log')
  cmd=['python',str(T/'computations/strong_resource_run.py'),'--out',str(res),'--','python',str(source),'--residual',str(B/'root-work/r127/R174-complete-continuous-residual-r1-certificate.json.gz'),'--resource',str(B/'root-work/r127/R174-composition-run1-resource.json'),'--out-prefix',str(pref)+'-result','--cell',str(cell),'--rss-kib','196608']
  if prior:cmd+=['--previous',str(prior[1]),'--previous-resource',str(prior[0])]
  with log.open('xb') as f:r=subprocess.run(cmd,cwd=B,stdout=f,stderr=subprocess.STDOUT)
  print(json.dumps(dict(cell=cell,wrapper_exit=r.returncode,resource=str(res),primary=str(primary))),flush=True)
  if r.returncode:raise SystemExit(r.returncode)
  assert json.loads(res.read_text())['exitcode']==0
 prior=(res,primary);rows.append(dict(cell=cell,resource=str(res),resource_sha256=hashlib.sha256(res.read_bytes()).hexdigest(),primary=str(primary),primary_sha256=hashlib.sha256(primary.read_bytes()).hexdigest()))
(W/'complete.json').write_text(json.dumps(dict(schema='R176-three-owned-cells-complete',cells=rows,all_owned_zero=True,source_sha256=p['source_sha256'],completed_utc=datetime.datetime.now(datetime.timezone.utc).isoformat()),indent=2)+'\n');print('R176_ALL_THREE_OWNED_ZERO',flush=True)
