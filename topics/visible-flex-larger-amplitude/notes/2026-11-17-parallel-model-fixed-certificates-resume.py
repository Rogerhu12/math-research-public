#!/usr/bin/env python3
"""Resume only incomplete slots of the two unchanged fixed certificate plans.

Preparation validates every complete original per-cell certificate and freezes
a reuse/missing manifest. Execution writes into a new directory and never
overwrites or recomputes a complete original slot. An unresolved interrupted
slot is explicitly distinguished from subsequent unvisited slots. All frozen
mathematical kernels and their original grids remain unchanged. This source
adds recovery bookkeeping only; it does not claim reach or closed geometry.
"""
import argparse,contextlib,gzip,hashlib,importlib.util,io,json,math,os,resource,sys,time,traceback
from fractions import Fraction as F
from pathlib import Path
from types import SimpleNamespace
sys.dont_write_bytecode=True
INPUT='26e53e8cdbdf6205a8bd9b2976cd4bcd36ad8734b0aca69512d705d826c5af72'
GRAM_BATCH='7bcbb9b2d0e830da172e57026023af2487c76d31f1dfc6ad586123f2ee3fc4a1'
CURV_BATCH='eb2b4e816175e314f54d5e4159318ad2e8a69b7975907673c398ddb1af3cf92f'
ENGINE='d0661f3d4de85ef7370fc1faaf370dd5b41aa58fa0476e67f42962ffd2f17882'
INTERVAL='f512c96cbc1fb3896fc144c5e9d8d29aaa80e321d08d9cdbf1745beb54a5c57d'
ORACLE='babd589d07c91d8067f9ef2011ae53712aaf6dbdbe22bed25c29116771b237a0'
CURV_PLAN='df745a9b3c204aaea2f1fee568282be24a13b1db7245095a743b52690fbf6602'

def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def load(p,name):
 s=importlib.util.spec_from_file_location(name,p);m=importlib.util.module_from_spec(s);s.loader.exec_module(m);return m
def save(p,d):
 p=Path(p);p.parent.mkdir(parents=True,exist_ok=True);q=p.with_suffix(p.suffix+'.tmp');q.write_text(json.dumps(d,indent=2,allow_nan=False)+'\n');q.replace(p);return sha(p)
def finite(d):
 if isinstance(d,float)and not math.isfinite(d):raise ValueError('Nonfinite certificate value')
 if isinstance(d,dict):
  for z in d.values():finite(z)
 elif isinstance(d,list):
  for z in d:finite(z)
def complete_json(p):
 if not p.exists():return None,dict(state='missing',path=str(p),sha256=None)
 raw=p.read_bytes();identity=dict(path=str(p),sha256=hashlib.sha256(raw).hexdigest(),bytes=len(raw))
 try:d=json.loads(raw)
 except (json.JSONDecodeError,UnicodeDecodeError)as e:return None,dict(identity,state='incomplete',parse_error=str(e))
 if not isinstance(d,dict):raise ValueError('Existing JSON is not a complete report object: '+str(p))
 return d,dict(identity,state='complete')
def config(a):
 n=a.topic/'notes';s=a.topic/'scripts';w=a.work
 return SimpleNamespace(input=w/'parallel-pulse-a5-complete-base.json.gz',raw_source=n/'2026-11-17-parallel-root-pulse-curvature-component-box.py',normalized_source=n/'2026-11-17-parallel-root-normalized-component-curvature.py',scaling_source=n/'2026-11-17-parallel-model-arclength-lambda2-node-kernel.py',engine=n/'2026-11-17-parallel-model-pulse-gram-representative-cells.py',interval_source=s/'parallel_20261117_arclength_interval_positive.py',scalar_oracle=n/'2026-11-17-parallel-inward-integral-enclosure.py',existing_reports=w,plan=w/'parallel-pulse-curvature-full-fixed-20261117.plan.json',outdir=w/'parallel-pulse-curvature-full-fixed-20261117',curvature_batch=n/'2026-11-17-parallel-model-pulse-curvature-fixed-full-batch.py',gram_batch=n/'2026-11-17-parallel-model-pulse-gram-fixed-full-batch.py',gram_dir=w/'parallel-pulse-gram-full-fixed-20261117')
def source_map(c):
 return {str(c.input):INPUT,str(c.engine):ENGINE,str(c.interval_source):INTERVAL,str(c.scalar_oracle):ORACLE,str(c.gram_batch):GRAM_BATCH,str(c.curvature_batch):CURV_BATCH,str(c.raw_source):'459dc01e8e5a7fb2b1910c2f0fb028f196eb0921855386c3858c26ba13a33afc',str(c.normalized_source):'582b22d61404467dba1d25f448fedcb7907b935995decd53ff2353649249531b',str(c.scaling_source):'e6ddb8c54093b27b03984dac56f86c2864dac0d167c74f133600d50533427927'}
def sources_unchanged(c,self_sha):
 for p,s in list(source_map(c).items())+[(str(Path(__file__)),self_sha)]:
  if sha(p)!=s:raise ValueError('Frozen source/input changed: '+p)
def no_same_worker(mode):
 names={'parallel-model-pulse-gram-fixed-full-batch.py','parallel-model-pulse-curvature-fixed-full-batch.py','2026-11-17-parallel-model-pulse-gram-fixed-full-batch.py','2026-11-17-parallel-model-pulse-curvature-fixed-full-batch.py'}
 own_names={Path(__file__).name,'parallel-model-fixed-certificates-resume.py','2026-11-17-parallel-model-fixed-certificates-resume.py'};found=[]
 for p in Path('/proc').iterdir():
  if not p.name.isdigit()or int(p.name)==os.getpid():continue
  try:argv=[z.decode(errors='replace')for z in(p/'cmdline').read_bytes().split(b'\0')if z]
  except OSError:continue
  if not argv or not Path(argv[0]).name.startswith('python'):continue
  rest=argv[1:]
  while rest and rest[0]in('-u','-B','-E','-I','-s','-S','-O','-OO'):rest=rest[1:]
  if not rest or rest[0].startswith('-'):continue
  program=Path(rest[0]).name
  if program in names:found.append(int(p.name))
  elif program in own_names and '--mode'in argv and argv.index('--mode')+1<len(argv)and argv[argv.index('--mode')+1]==mode:found.append(int(p.name))
 if found:raise ValueError('A matching original/recovery worker remains alive: '+repr(found))
def gram_ok(d,call):
 expected=dict(input_sha256=INPUT,source_sha256=ENGINE,cell=call['cell'],part=call['part'],left_exact=call['left_exact'],right_exact=call['right_exact'],construction_angles=4096,audit_angles=16384,scalar_panels=4096,exact_pulse_midpoint='1152921504606846971/1152921504606846976',all_radius_and_angle_covered=True,strict_under_stated_IEEE_arithmetic=True,complete_prefix_covered=False,whole_original_cell_covered=call['part']=='all')
 if any(d.get(k)!=v for k,v in expected.items()):raise ValueError('Complete Gram report has a different object/range/policy')
 finite(d)
 if len(d['dependencies'])!=2 or set(d['dependencies'].values())!={INTERVAL,ORACLE}:raise ValueError('Gram dependency mismatch')
 b=d['gram_operator_bound']
 if b<0 or d['below_1e_minus_6']!=(b<1e-6):raise ValueError('Invalid Gram bound classification')
def gram_exception_ok(d,call):
 if d.get('status')!='exception'or d.get('call')!=call or d.get('input_sha256')!=INPUT or d.get('driver_source_sha256')!=GRAM_BATCH or d.get('engine_source_sha256')!=ENGINE:raise ValueError('Wrong completed Gram exception record')

def inspect_gram(c):
 path=c.gram_dir/'fixed-plan.json';original=json.loads(path.read_bytes());data=json.loads(gzip.decompress(c.input.read_bytes()));x=[F(float(z))for z in data['mesh']];boundary=F(float(data['inward_scalar_profile']['cut']))+F(.005);plan=[]
 for i,(l,r)in enumerate(zip(x,x[1:])):
  for part in (['before','after']if l<boundary<r else['all']):plan.append(dict(cell=i,part=part,left_exact=str(boundary if part=='after'else l),right_exact=str(boundary if part=='before'else r)))
 if len(plan)!=819 or original['plan']!=plan or original['driver_source_sha256']!=GRAM_BATCH or original['input_sha256']!=INPUT or original['construction_angles']!=4096 or original['audit_angles']!=16384 or original['scalar_panels']!=4096 or original['adaptive_changes']:raise ValueError('Original fixed Gram plan mismatch')
 if (c.gram_dir/'result.json').exists():raise ValueError('Original Gram has a terminal report; do not resume it')
 records=[];pending_seen=False;first=True
 for call in plan:
  p=c.gram_dir/f"cell-{call['cell']:04d}-{call['part']}.json";d,identity=complete_json(p)
  if d is None:
   pending_seen=True;state='interrupted_or_unresolved_next_call'if first else'not_reached';first=False
   records.append(dict(call=call,old=identity,action='compute_once',reason=state));continue
  if pending_seen:raise ValueError('Original sequential Gram reports have a gap before a later complete report')
  if d.get('status')=='exception':gram_exception_ok(d,call);status='exception'
  else:gram_ok(d,call);status='certified'if d['below_1e_minus_6']else'bound_failure'
  records.append(dict(call=call,old=identity,action='reuse',status=status,bound=d.get('gram_operator_bound')))
 expected={f"cell-{p['cell']:04d}-{p['part']}.json"for p in plan}
 if any(p.name not in expected for p in c.gram_dir.glob('cell-*.json')):raise ValueError('Unplanned original Gram report')
 counts=dict(planned_calls=819,reused_complete=sum(r['action']=='reuse'for r in records),reused_bound_failures=sum(r.get('status')=='bound_failure'for r in records),reused_exceptions=sum(r.get('status')=='exception'for r in records),remaining_calls=sum(r['action']=='compute_once'for r in records))
 return dict(original_plan_path=str(path),original_plan_sha256=sha(path),records=records,counts=counts),None

def inspect_curvature(c):
 H=load(c.curvature_batch,'recovery_old_curvature_batch');plan,fixtures=H.prepare(c,CURV_BATCH)
 if sha(c.plan)!=CURV_PLAN or json.loads(c.plan.read_bytes())!=plan:raise ValueError('Original fixed curvature plan mismatch')
 if(c.outdir/'result.json').exists():raise ValueError('Original curvature has a terminal report; do not resume it')
 scaling={};scale_info={};records=[];pending_seen=False;first=True
 for name,digest in H.FIXTURES.items():
  p=c.outdir/'reused'/name
  if sha(p)!=digest:raise ValueError('Reused original report was changed')
  if 'lambda2-nodes'in name:scaling[digest]=fixtures[name]
 for row in plan['cells']:
  i=row['cell']
  if row['action']=='reuse':
   p=c.outdir/'reused'/f"parallel-root-normalized-component-curvature-cell{i}-q{row['angles']}.json";d=H.read(p);H.curvature_ok(d,row,scaling);records.append(dict(row=row,action='reuse',status='certified',curvature=dict(state='complete',path=str(p),sha256=sha(p)),scaling=[]));continue
  failed=c.outdir/f'failure-cell-{i:04d}.json'
  if failed.exists():
   d=H.read(failed)
   if d.get('cell')!=i or d.get('source_sha256')!=CURV_BATCH or d.get('input_sha256')!=INPUT or d.get('plan_sha256')!=CURV_PLAN:raise ValueError('Wrong completed curvature failure')
   if pending_seen:raise ValueError('Original curvature has a gap before a later failure')
   records.append(dict(row=row,action='reuse',status='failed',failure=dict(path=str(failed),sha256=sha(failed)),scaling=[]));continue
  pieces=[]
  for piece in row['scaling_pieces']:
   p=c.outdir/f"lambda-cell-{i:04d}-{piece['part']}.json";d,identity=complete_json(p)
   if d is not None:H.scaling_ok(d,row,piece);finite(d);scaling[identity['sha256']]=d
   pieces.append(dict(piece=piece,old=identity,action='reuse'if d is not None else'compute_once'))
  p=c.outdir/f'curvature-cell-{i:04d}.json';d,identity=complete_json(p)
  if d is not None:
   if pending_seen or any(z['action']!='reuse'for z in pieces):raise ValueError('Complete curvature lacks its original preceding scaling evidence')
   H.curvature_ok(d,row,scaling);finite(d);records.append(dict(row=row,action='reuse',status='certified',curvature=identity,scaling=pieces))
  else:
   if pending_seen and any(z['action']=='reuse'for z in pieces):raise ValueError('A later scaling report follows an unresolved earlier cell')
   pending_seen=True;reason='interrupted_or_unresolved_next_call'if first else'not_reached';first=False
   records.append(dict(row=row,action='compute_once',reason=reason,curvature=identity,scaling=pieces))
 counts=dict(planned_cells=818,reused_complete_cells=sum(r['action']=='reuse'for r in records),reused_failed_cells=sum(r.get('status')=='failed'for r in records),remaining_cells=sum(r['action']=='compute_once'for r in records),reused_new_scaling_calls=sum(z['action']=='reuse'for r in records for z in r['scaling']),remaining_scaling_calls=sum(z['action']=='compute_once'for r in records for z in r['scaling']),remaining_curvature_calls=sum(r['action']=='compute_once'for r in records))
 return dict(original_plan_path=str(c.plan),original_plan_sha256=CURV_PLAN,records=records,counts=counts),H

def inspect(a,c,self_sha):
 sources_unchanged(c,self_sha);no_same_worker(a.mode)
 data,H=inspect_gram(c)if a.mode=='gram'else inspect_curvature(c)
 return dict(schema='fixed-certificate-interruption-recovery-manifest-v1',mode=a.mode,source_sha256=self_sha,source_identities=source_map(c),input_sha256=INPUT,mathematical_parameters_changed=False,complete_original_slots_recomputed=False,interruption_cause='unknown; original OS workers absent and no terminal reports',**data),H
def journal(folder,event):
 event=dict(event,utc_time=time.time());save(folder/'active-call.json',event)
 with(folder/'journal.jsonl').open('a')as out:out.write(json.dumps(event,allow_nan=False)+'\n');out.flush()
 print(json.dumps(event,allow_nan=False),flush=True)
def execute(a,c,manifest,H,self_sha):
 if a.outdir.exists()and any(a.outdir.iterdir()):raise ValueError('Recovery output directory must be new/empty; no silent second attempt')
 a.outdir.mkdir(parents=True,exist_ok=True);manifest_sha=sha(a.manifest);start=time.perf_counter();entries=[];counts=dict(new_gram_calls=0,new_scaling_calls=0,new_curvature_calls=0,new_exceptions=0);fatal=None
 engine=load(c.engine,'recovery_frozen_gram')if a.mode=='gram'else None
 scale=load(c.scaling_source,'recovery_frozen_scaling')if a.mode=='curvature'else None
 curve=load(c.normalized_source,'recovery_frozen_curvature')if a.mode=='curvature'else None
 scaling={}
 if H is not None:
  for r in manifest['records']:
   for z in r['scaling']:
    if z['action']=='reuse':scaling[z['old']['sha256']]=H.read(Path(z['old']['path']))
  for name,digest in H.FIXTURES.items():
   if 'lambda2-nodes'in name:scaling[digest]=H.read(c.outdir/'reused'/name)
 def progress(final=False):
  ok=[e for e in entries if e['status']=='certified'];key='gram_operator_bound'if a.mode=='gram'else'normalized_principal_curvature_upper';maximum=max(ok,key=lambda e:e[key])if ok else None
  failures=sum(e['status']!='certified'for e in entries);total=819 if a.mode=='gram'else 818
  d=dict(schema='fixed-certificate-recovery-result-v1'if final else'fixed-certificate-recovery-progress-v1',mode=a.mode,source_sha256=self_sha,manifest_sha256=manifest_sha,original_plan_sha256=manifest['original_plan_sha256'],input_sha256=INPUT,planned=total,completed=len(entries),remaining=total-len(entries),failures=failures,counts=dict(counts),maximum=maximum,complete_scope_certified=bool(final and len(entries)==total and failures==0 and fatal is None),reach_certified=False,closed_surface=False,fixed_metric_solve_refinement=False,fatal=fatal,seconds=time.perf_counter()-start,maximum_RSS_kib=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)
  if final:d['entries']=sorted(entries,key=lambda e:(e['cell'],{'all':0,'before':0,'after':1,None:0}[e['part']]))
  save(a.outdir/('result.json'if final else'progress.json'),d)
 try:
  for rec in manifest['records']:
   if rec['action']!='reuse':continue
   i=rec['call']['cell']if a.mode=='gram'else rec['row']['cell'];part=rec['call']['part']if a.mode=='gram'else None
   evidence=rec['old']if a.mode=='gram'else rec['failure']if rec['status']=='failed'else rec['curvature'];p=Path(evidence['path'])
   if sha(p)!=evidence['sha256']:raise ValueError('Previously verified original report changed')
   if a.mode=='gram':d=json.loads(p.read_bytes());key='gram_operator_bound';value=d.get(key)
   elif rec['status']=='failed':key='normalized_principal_curvature_upper';value=None
   else:d=H.read(p);key='normalized_principal_curvature_upper';value=d['records'][0][key]
   entries.append(dict(cell=i,part=part,status=rec['status'],action='original_report_reused',report_path=str(p),report_sha256=sha(p),**({key:value}if value is not None else{})))
  progress()
  for rec in manifest['records']:
   if rec['action']=='reuse':continue
   sources_unchanged(c,self_sha)
   if sha(a.manifest)!=manifest_sha:raise ValueError('Frozen recovery manifest changed')
   i=rec['call']['cell']if a.mode=='gram'else rec['row']['cell'];part=rec['call']['part']if a.mode=='gram'else None;stage='start'
   try:
    if a.mode=='gram':
     stage='gram';p=a.outdir/f'cell-{i:04d}-{part}.json';journal(a.outdir,dict(event='call_started',mode=a.mode,cell=i,part=part,stage=stage,reason=rec['reason']));counts['new_gram_calls']+=1
     arg=SimpleNamespace(input=c.input,interval_source=c.interval_source,scalar_oracle=c.scalar_oracle,out=p,cell=i,part=part,angles=16384,scalar_panels=4096)
     with contextlib.redirect_stdout(io.StringIO()):engine.main(arg)
     d=json.loads(p.read_bytes());gram_ok(d,rec['call']);status='certified'if d['below_1e_minus_6']else'bound_failure';values=dict(gram_operator_bound=d['gram_operator_bound'])
    else:
     row=rec['row'];paths=[]
     for z in rec['scaling']:
      part=z['piece']['part']
      if z['action']=='reuse':
       p=Path(z['old']['path'])
       if sha(p)!=z['old']['sha256']:raise ValueError('Previously verified scaling report changed')
      else:
       stage='scaling';p=a.outdir/f'lambda-cell-{i:04d}-{part}.json';journal(a.outdir,dict(event='call_started',mode=a.mode,cell=i,part=part,stage=stage,reason=rec['reason']));counts['new_scaling_calls']+=1
       arg=SimpleNamespace(input=c.input,engine=c.engine,interval_source=c.interval_source,scalar_oracle=c.scalar_oracle,out=p,reference=None,cell=i,part=part)
       with contextlib.redirect_stdout(io.StringIO()):scale.main(arg)
      d=H.read(p);H.scaling_ok(d,row,z['piece']);scaling[sha(p)]=d;paths.append(p)
      if z['action']!='reuse':journal(a.outdir,dict(event='call_finished',mode=a.mode,cell=i,part=part,stage=stage,report_sha256=sha(p)))
     stage='curvature';p=a.outdir/f'curvature-cell-{i:04d}.json';journal(a.outdir,dict(event='call_started',mode=a.mode,cell=i,part=None,stage=stage,reason=rec['reason']));counts['new_curvature_calls']+=1
     arg=SimpleNamespace(input=c.input,interval_source=c.interval_source,raw_source=c.raw_source,out=p,scaling_reports=paths,cells=[i],angles=row['angles'],radial_subdivisions=8)
     with contextlib.redirect_stdout(io.StringIO()):curve.main(arg)
     d=H.read(p);v=H.curvature_ok(d,row,scaling);status='certified';values={k:v[k]for k in ('normalized_principal_curvature_upper','metric_E_lower','metric_determinant_lower','scaling_bounds')}
    digest=sha(p);entries.append(dict(cell=i,part=part if a.mode=='gram'else None,status=status,action='missing_slot_executed_once',report_path=str(p),report_sha256=digest,**values));journal(a.outdir,dict(event='call_finished',mode=a.mode,cell=i,part=part,stage=stage,report_sha256=digest))
   except Exception as exc:
    p=a.outdir/f'failure-{i:04d}-{part or "cell"}.json';failure=dict(cell=i,part=part,stage=stage,exception_type=type(exc).__name__,message=str(exc),traceback=traceback.format_exc(),source_sha256=self_sha,input_sha256=INPUT,manifest_sha256=manifest_sha,retry=False);digest=save(p,failure);counts['new_exceptions']+=1;entries.append(dict(cell=i,part=part,status='exception',report_path=str(p),report_sha256=digest));journal(a.outdir,dict(event='call_failed',mode=a.mode,cell=i,part=part,stage=stage,report_sha256=digest))
   progress()
 except Exception as exc:fatal=dict(exception_type=type(exc).__name__,message=str(exc),traceback=traceback.format_exc())
 try:
  sources_unchanged(c,self_sha)
  if sha(a.manifest)!=manifest_sha:raise ValueError('Recovery manifest changed before final report')
 except Exception as exc:fatal=dict(previous=fatal,final_identity_error=str(exc))
 progress(final=True);journal(a.outdir,dict(event='recovery_terminal',mode=a.mode,result_sha256=sha(a.outdir/'result.json'),completed=len(entries),counts=counts,fatal=fatal))

def main(a):
 repository=a.topic.resolve().parent.parent
 if any(repository==p.resolve()or repository in p.resolve().parents for p in (a.manifest,a.outdir)):raise ValueError('Recovery manifests and raw reports must stay outside the research repository')
 c=config(a);self_sha=sha(__file__);manifest,H=inspect(a,c,self_sha)
 if a.execute:
  if not a.manifest.exists()or json.loads(a.manifest.read_bytes())!=manifest:raise ValueError('Execution requires the unchanged pre-reviewed recovery manifest')
  execute(a,c,manifest,H,self_sha)
 else:
  if a.manifest.exists():raise ValueError('Recovery manifest already exists')
  digest=save(a.manifest,manifest);print(json.dumps(dict(event='recovery_prepared_only',mode=a.mode,source_sha256=self_sha,manifest_sha256=digest,counts=manifest['counts'],new_geometry_calls=0)),flush=True)

if __name__=='__main__':
 p=argparse.ArgumentParser(description=__doc__);p.add_argument('--mode',choices=['gram','curvature'],required=True)
 for n in ('topic','work','manifest','outdir'):p.add_argument('--'+n,type=Path,required=True)
 p.add_argument('--execute',action='store_true');main(p.parse_args())
