#!/usr/bin/env python3
"""Fixed 819-call continuous Gram cover of the unchanged 818-cell pulse prefix.

No adaptive splitting, angular change, new field, or nonlinear solve. The sole
extra split is the exact binary pulse midpoint already proved in R641's finite
extension. Cached setup is checked against two complete cold-run budgets.
"""
import argparse,contextlib,gzip,hashlib,importlib.util,io,json,struct,time,traceback
from fractions import Fraction as F
from pathlib import Path
from types import SimpleNamespace
import numpy as np

INPUT_SHA='26e53e8cdbdf6205a8bd9b2976cd4bcd36ad8734b0aca69512d705d826c5af72'
ENGINE_SHA='d0661f3d4de85ef7370fc1faaf370dd5b41aa58fa0476e67f42962ffd2f17882'
INTERVAL_SHA='f512c96cbc1fb3896fc144c5e9d8d29aaa80e321d08d9cdbf1745beb54a5c57d'
ORACLE_SHA='babd589d07c91d8067f9ef2011ae53712aaf6dbdbe22bed25c29116771b237a0'

def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def load(p,name):
 s=importlib.util.spec_from_file_location(name,p);m=importlib.util.module_from_spec(s);s.loader.exec_module(m);return m
def save(p,data):p.write_text(json.dumps(data,indent=2)+'\n');return sha(p)
def identical(a,b,path=''):
 if type(a)!=type(b):raise ValueError('Budget type differs: '+path)
 if isinstance(a,float):
  if struct.pack('<d',a)!=struct.pack('<d',b):raise ValueError('Budget binary float differs: '+path)
 elif isinstance(a,dict):
  if set(a)!=set(b):raise ValueError('Budget keys differ: '+path)
  for k in a:
   if k!='seconds':identical(a[k],b[k],path+'/'+k)
 elif isinstance(a,list):
  if len(a)!=len(b):raise ValueError('Budget length differs: '+path)
  for j,(x,y)in enumerate(zip(a,b)):identical(x,y,path+'/'+str(j))
 elif a!=b:raise ValueError('Budget value differs: '+path)

def main(a):
 begin=time.perf_counter();driver_sha=sha(__file__)
 for p,s in [(a.engine,ENGINE_SHA),(a.interval_source,INTERVAL_SHA),(a.scalar_oracle,ORACLE_SHA)]:
  if sha(p)!=s:raise ValueError('Frozen source changed: '+str(p))
 raw=a.input.read_bytes()
 if hashlib.sha256(raw).hexdigest()!=INPUT_SHA:raise ValueError('Fixed pulse input required')
 clear=gzip.decompress(raw);data=json.loads(clear)
 x=[F(float(v))for v in data['mesh']];knots=[F(float(k['s']))for k in data['fixed_scalar_profile']['geometry']['knots']]
 origin=F(float(data['analytic_extension_origin']));cut=F(float(data['inward_scalar_profile']['cut']));boundary=cut+F(.005)
 plan=[];counts=dict(old_quintic=0,analytic=0,pulse_first=0,pulse_split=0)
 for i,(l,r)in enumerate(zip(x,x[1:])):
  if any(l<k<r for k in knots+[cut]):raise ValueError('Unplanned exact scalar knot inside field cell')
  if r<=origin:counts['old_quintic']+=1
  elif origin<=l and r<=cut:counts['analytic']+=1
  elif cut<=l and r<=boundary:counts['pulse_first']+=1
  elif l<boundary<r:counts['pulse_split']+=1
  else:raise ValueError('Unplanned scalar scope')
  for part in (['before','after']if l<boundary<r else['all']):
   left=boundary if part=='after'else l;right=boundary if part=='before'else r
   plan.append(dict(cell=i,part=part,left_exact=str(left),right_exact=str(right)))
 if len(plan)!=819 or counts!=dict(old_quintic=481,analytic=17,pulse_first=319,pulse_split=1):raise ValueError('Fixed 819-call plan differs')
 if a.outdir.exists()and any(a.outdir.iterdir()):raise ValueError('Output directory must be new or empty')
 a.outdir.mkdir(parents=True,exist_ok=True)
 metadata=dict(driver_source_sha256=driver_sha,engine_source_sha256=ENGINE_SHA,input_sha256=INPUT_SHA,interval_source_sha256=INTERVAL_SHA,scalar_oracle_sha256=ORACLE_SHA,construction_angles=4096,audit_angles=16384,scalar_panels=4096,whole_cells=818,planned_calls=819,counts=counts,exact_pulse_boundary=str(boundary),adaptive_changes=False)
 plan_sha=save(a.outdir/'fixed-plan.json',dict(metadata,plan=plan))
 engine=load(a.engine,'fixed_gram_engine');engine_load=engine.load
 def args_for(cell,part,out,input_value):return SimpleNamespace(input=input_value,interval_source=a.interval_source,scalar_oracle=a.scalar_oracle,out=out,cell=cell,part=part,angles=16384,scalar_panels=4096)
 def invoke(cell,part,out,input_value):
  with contextlib.redirect_stdout(io.StringIO()):engine.main(args_for(cell,part,out,input_value))
  return json.loads(out.read_bytes())
 golden={};golden_shas={}
 for cell,name in [(381,'parallel-model-pulse-wide381-gram.json'),(514,'parallel-model-pulse-bridge514-gram.json')]:
  if a.validation_reports:
   p=a.validation_reports/name;g=json.loads(p.read_bytes());golden_shas[str(cell)]=sha(p)
  else:
   p=a.outdir/f'validation-cold-{cell}.json';g=invoke(cell,'all',p,a.input);golden_shas[str(cell)]=sha(p)
  if g['input_sha256']!=INPUT_SHA or g['source_sha256']!=ENGINE_SHA or g['cell']!=cell or g['part']!='all':raise ValueError('Wrong existing validation report')
  golden[cell]=g
 # Only immutable setup is cached. The actual interval cell calculation,
 # arithmetic order, scalar budgets, finite projection and cover are unchanged.
 for key in ('mesh','states','rhs','d2'):
  z=np.asarray(data[key],dtype=float);z.flags.writeable=False;data[key]=z
 class FrozenInput:
  def read_bytes(self):return raw
 frozen_input=FrozenInput()
 engine.gzip=SimpleNamespace(decompress=lambda value:clear if value is raw else gzip.decompress(value))
 engine.json=SimpleNamespace(loads=lambda value:data if value is clear else json.loads(value),dumps=json.dumps)
 module_cache={};transform_cache={}
 def cached_load(path,name):
  key=str(Path(path).resolve())
  if key not in module_cache:
   m=engine_load(path,name)
   if Path(path).resolve()==a.interval_source.resolve():
    transform_class=m.Transform
    def fixed_transform(size):
     if size not in transform_cache:
      value=transform_class(size);value.cos.flags.writeable=False;value.sin.flags.writeable=False;transform_cache[size]=value
     return transform_cache[size]
    m.Transform=fixed_transform
   module_cache[key]=m
  return module_cache[key]
 engine.load=cached_load
 validation=[]
 for cell in (381,514):
  p=a.outdir/f'validation-cached-{cell}.json';g=invoke(cell,'all',p,frozen_input);identical(golden[cell],g)
  validation.append(dict(cell=cell,cold_report_sha256=golden_shas[str(cell)],cached_report_sha256=sha(p),all_non_time_fields_binary_identical=True,gram_operator_bound=g['gram_operator_bound']))
 validation_sha=save(a.outdir/'cache-validation.json',dict(metadata,validation=validation))
 print(json.dumps(dict(event='cache_validation_passed',validation=validation,planned_calls=819)),flush=True)
 entries=[];max_entry=None;failure_count=0;exception_count=0;compute_begin=time.perf_counter()
 for call in plan:
  cell,part=call['cell'],call['part'];p=a.outdir/f'cell-{cell:04d}-{part}.json'
  try:
   g=invoke(cell,part,p,frozen_input)
   entry=dict(call,report_sha256=sha(p),gram_operator_bound=g['gram_operator_bound'],below_1e_minus_6=g['below_1e_minus_6'],status='complete')
   if not g['below_1e_minus_6']:failure_count+=1
   if max_entry is None or entry['gram_operator_bound']>max_entry['gram_operator_bound']:max_entry=entry
  except Exception as error:
   partial={};tb=error.__traceback__
   while tb:
    local=tb.tb_frame.f_locals
    if tb.tb_frame.f_globals.get('__file__')==str(a.engine):
     for key in ('cover_stats','Amin','Amax','ea','eap','U','Vrel','mD','mR','En','Dn','Rn','Pfn','Pgn','er','gr','fr'):
      if key in local:
       value=local[key]
       if isinstance(value,(str,int,float,bool,dict)):partial[key]=value
    tb=tb.tb_next
   failure=dict(metadata,call=call,status='exception',exception_type=type(error).__name__,message=str(error),traceback=traceback.format_exc(),available_budgets=partial)
   save(p,failure);entry=dict(call,report_sha256=sha(p),status='exception',exception_type=type(error).__name__,message=str(error));exception_count+=1
  entries.append(entry)
  if len(entries)%8==0 or len(entries)==len(plan):
   if sha(__file__)!=driver_sha or sha(a.engine)!=ENGINE_SHA:raise ValueError('Source changed during fixed batch')
   progress=dict(metadata,completed_calls=len(entries),unvisited_calls=len(plan)-len(entries),bound_failures=failure_count,exceptions=exception_count,maximum=max_entry,elapsed_seconds=time.perf_counter()-begin,compute_seconds=time.perf_counter()-compute_begin)
   save(a.outdir/'progress.json',progress);print(json.dumps(dict(event='progress',**progress)),flush=True)
 result=dict(metadata,plan_sha256=plan_sha,cache_validation_sha256=validation_sha,completed_calls=len(entries),unvisited_calls=0,bound_failures=failure_count,exceptions=exception_count,maximum=max_entry,complete_prefix_gram_below_1e_minus_6=bool(failure_count==0 and exception_count==0),closed_surface=False,fixed_metric_solve_refinement=False,elapsed_seconds=time.perf_counter()-begin,entries=entries)
 if sha(__file__)!=driver_sha or sha(a.engine)!=ENGINE_SHA:raise ValueError('Source changed before final result')
 result_sha=save(a.outdir/'result.json',result);print(json.dumps(dict(event='complete',result_sha256=result_sha,maximum=max_entry,bound_failures=failure_count,exceptions=exception_count,complete_prefix_gram_below_1e_minus_6=result['complete_prefix_gram_below_1e_minus_6'])),flush=True)

if __name__=='__main__':
 p=argparse.ArgumentParser(description=__doc__)
 for key in ('input','engine','interval-source','scalar-oracle','outdir'):p.add_argument('--'+key,type=Path,required=True)
 p.add_argument('--validation-reports',type=Path)
 main(p.parse_args())
