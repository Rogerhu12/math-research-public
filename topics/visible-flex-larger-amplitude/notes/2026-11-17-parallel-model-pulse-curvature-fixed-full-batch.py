#!/usr/bin/env python3
"""Prepare, then execute once, a fixed full continuous G-curvature cover.

The unchanged 26e53 pulse field and its q4096 normalization are used. Two
already published complete certificates are consumed, not recomputed. Each
of the other 816 cells receives one finite-node scaling call and one original
component-box curvature call at Q4096 / eight radial subdivisions. Cell 817
uses its published Q8192 / eight-subdivision certificate, including the union
of both exact scalar pieces. There is no adaptive retry, changed field/g,
reach claim, or closed-surface claim. The default only prepares the fixed plan.
"""
import argparse,contextlib,gzip,hashlib,importlib.util,io,json,math,resource,time,traceback
from fractions import Fraction as F
from pathlib import Path
from types import SimpleNamespace

INPUT='26e53e8cdbdf6205a8bd9b2976cd4bcd36ad8734b0aca69512d705d826c5af72'
RAW='459dc01e8e5a7fb2b1910c2f0fb028f196eb0921855386c3858c26ba13a33afc'
NORMALIZED='582b22d61404467dba1d25f448fedcb7907b935995decd53ff2353649249531b'
SCALING='e6ddb8c54093b27b03984dac56f86c2864dac0d167c74f133600d50533427927'
ENGINE='d0661f3d4de85ef7370fc1faaf370dd5b41aa58fa0476e67f42962ffd2f17882'
INTERVAL='f512c96cbc1fb3896fc144c5e9d8d29aaa80e321d08d9cdbf1745beb54a5c57d'
ORACLE='babd589d07c91d8067f9ef2011ae53712aaf6dbdbe22bed25c29116771b237a0'
S_GENERATED='c9f4c46610555cbe351de378fe9bd8355c9407919d75237496e5997a0da44713'
G_GENERATED='a06a2d95a4b8b94e7db53b7adf4262c506dff77b3a72d54965739b0db3d0b2ce'
FIXTURES={
 'parallel-model-pulse-lambda2-nodes-cell458.json':'dcee02943ade86bfd901a683d770624175479f676e440a2e6bd8c942ec9af44d',
 'parallel-model-pulse-lambda2-nodes-cell817-before.json':'c032f182eda7a59d597d6850df684dad417a1cf7f2b1a3b8b76e5753c1c98372',
 'parallel-model-pulse-lambda2-nodes-cell817-after.json':'c2cc44297a9af8b2e700b2b774a40969ccb5c5189e335bca9689cbac42f31453',
 'parallel-root-normalized-component-curvature-cell458-q4096.json':'fd35f72050d8284e3c137123902e0a3f09437db922f62617029e891da43a6043',
 'parallel-root-normalized-component-curvature-cell817-q8192.json':'12b4b170eb121e03558221a954288ccc730e856c843ff6c6dd03b39086eb34b9'}
BOUNDS=('lambda_minus_one_bound','lambda_s_bound','lambda_ss_bound')

def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def load(p,name):
 s=importlib.util.spec_from_file_location(name,p);m=importlib.util.module_from_spec(s);s.loader.exec_module(m);return m
def finite_tree(x):
 if isinstance(x,float)and not math.isfinite(x):raise ValueError('Nonfinite report value')
 if isinstance(x,dict):
  for y in x.values():finite_tree(y)
 elif isinstance(x,list):
  for y in x:finite_tree(y)
def read(p):
 value=json.loads(Path(p).read_bytes());finite_tree(value);return value
def save(p,d):
 p=Path(p);p.parent.mkdir(parents=True,exist_ok=True)
 text=json.dumps(d,indent=2,allow_nan=False)+'\n';temporary=p.with_suffix(p.suffix+'.tmp')
 temporary.write_text(text);temporary.replace(p);return sha(p)
def sources(a):return {a.input:INPUT,a.raw_source:RAW,a.normalized_source:NORMALIZED,a.scaling_source:SCALING,a.engine:ENGINE,a.interval_source:INTERVAL,a.scalar_oracle:ORACLE}
def check_sources(a,self_sha):
 for p,s in list(sources(a).items())+[(Path(__file__),self_sha)]:
  if sha(p)!=s:raise ValueError('Frozen source/input changed: '+str(p))
def require_external_outputs(a):
 canonical=a.interval_source.resolve()
 if canonical.parent.name!='scripts'or canonical.parents[1].name!='visible-flex-larger-amplitude'or canonical.parents[2].name!='topics':raise ValueError('Use the published canonical topic interval-source path')
 repository=canonical.parents[3]
 for path in (a.plan.resolve(),a.outdir.resolve()):
  if repository==path or repository in path.parents:raise ValueError('Regenerable plan/reports must remain outside the research repository')
def scaling_ok(d,row,piece):
 expected=dict(source_sha256=SCALING,engine_sha256=ENGINE,generated_kernel_sha256=S_GENERATED,input_sha256=INPUT,interval_source_sha256=INTERVAL,scalar_oracle_sha256=ORACLE,cell=row['cell'],part=piece['part'],left_exact=piece['left_exact'],right_exact=piece['right_exact'],construction_angles=4096,evaluated_angles=4096,scalar_panels=4096,field_tangent_bandwidth=640,all_radius_covered=True,strict_under_stated_IEEE_arithmetic=True)
 if any(d.get(k)!=v for k,v in expected.items()):raise ValueError('Scaling object, range, or policy mismatch')
 if d['original_left']!=row['left']or d['original_right']!=row['right']:raise ValueError('Scaling original cell mismatch')
 if len(d['dependencies'])!=2 or set(d['dependencies'].values())!={INTERVAL,ORACLE}:raise ValueError('Scaling dependency mismatch')
 b=[d[k]for k in BOUNDS]
 if any(v<0 or not math.isfinite(v)for v in b)or b[0]>=1 or d['mean_speed_lower']<=0 or d['rho_lower_at_nodes']<=0:raise ValueError('Invalid scaling positivity/bounds')
 return b
def curvature_ok(d,row,scaling_records):
 expected=dict(source_sha256=NORMALIZED,input_sha256=INPUT,interval_source_sha256=INTERVAL,angles=row['angles'],radial_subdivisions=8,raw_curvature_source_sha256=RAW,scaling_source_sha256=SCALING,generated_kernel_sha256=G_GENERATED,full_prefix=False)
 if any(d.get(k)!=v for k,v in expected.items())or len(d['records'])!=1:raise ValueError('Curvature object or policy mismatch')
 z=d['records'][0]
 if z['cell']!=row['cell']or z['left']!=row['left']or z['right']!=row['right']:raise ValueError('Curvature range mismatch')
 used=[]
 for cert in d['scaling_certificates']:
  digest=cert['report_sha256'];s=scaling_records[digest]
  expected_cert=dict(cell=s['cell'],part=s['part'],left_exact=s['left_exact'],right_exact=s['right_exact'],bounds=[s[k]for k in BOUNDS],report_sha256=digest)
  if cert!=expected_cert:raise ValueError('Curvature scaling provenance mismatch')
  if cert['cell']==row['cell']:used.append(cert)
 edge=F(row['left_exact'])
 for cert in sorted(used,key=lambda p:F(p['left_exact'])):
  if F(cert['left_exact'])!=edge or F(cert['right_exact'])<=edge:raise ValueError('Scaling union has a gap or overlap')
  edge=F(cert['right_exact'])
 if edge!=F(row['right_exact']):raise ValueError('Scaling union does not cover entire field cell')
 if z['scaling_bounds']!=[max(p['bounds'][j]for p in used)for j in range(3)]:raise ValueError('Incorrect whole-cell scaling union')
 if not math.isfinite(z['normalized_principal_curvature_upper'])or z['normalized_principal_curvature_upper']<0 or z['metric_E_lower']<=0 or z['metric_determinant_lower']<=0:raise ValueError('Unpaid finite curvature/positive metric')
 if set(z['angular_second_bounds'])!={v+str(j)for v in ('V','T','AA','VT','EE')for j in range(3)}or any(v<0 for v in z['angular_second_bounds'].values()):raise ValueError('Incomplete component angle cover')
 return z

def prepare(a,self_sha):
 check_sources(a,self_sha);clear=gzip.decompress(a.input.read_bytes());d=json.loads(clear)
 x=[F(float(v))for v in d['mesh']];knots=[F(float(k['s']))for k in d['fixed_scalar_profile']['geometry']['knots']]
 origin=F(float(d['analytic_extension_origin']));cut=F(float(d['inward_scalar_profile']['cut']));boundary=cut+F(.005)
 if d['M']!=320 or len(x)!=819 or x[0]!=0 or x[-1]!=1 or any(r<=l for l,r in zip(x,x[1:])):raise ValueError('Fixed complete pulse mesh required')
 rows=[];counts=dict(old_quintic=0,analytic=0,pulse_first=0,pulse_split=0)
 for i,(l,r)in enumerate(zip(x,x[1:])):
  if any(l<k<r for k in knots+[origin,cut]):raise ValueError('Unsupported interior exact scalar knot')
  if r<=origin:kind='old_quintic'
  elif origin<=l and r<=cut:kind='analytic'
  elif cut<=l and r<=boundary:kind='pulse_first'
  elif l<boundary<r:kind='pulse_split'
  else:raise ValueError('Unsupported exact scalar scope')
  counts[kind]+=1;pieces=[]
  for part in (['before','after']if l<boundary<r else['all']):
   pieces.append(dict(part=part,left_exact=str(boundary if part=='after'else l),right_exact=str(boundary if part=='before'else r)))
  rows.append(dict(cell=i,left=float(l),right=float(r),left_exact=str(l),right_exact=str(r),scalar_kind=kind,scaling_pieces=pieces,action='reuse'if i in (458,817)else'compute_once',angles=8192 if i==817 else 4096,radial_subdivisions=8))
 if counts!=dict(old_quintic=481,analytic=17,pulse_first=319,pulse_split=1)or [r['cell']for r in rows if len(r['scaling_pieces'])==2]!=[817]:raise ValueError('Fixed full-cover plan changed')
 if sum(len(r['scaling_pieces'])for r in rows if r['action']=='compute_once')!=816:raise ValueError('New scaling-call count changed')
 fixtures={};scaling_records={}
 for name,digest in FIXTURES.items():
  p=a.existing_reports/name
  if sha(p)!=digest:raise ValueError('Published report changed: '+name)
  fixtures[name]=read(p)
  if 'lambda2-nodes' in name:
   z=fixtures[name];row=rows[z['cell']];piece=next(p for p in row['scaling_pieces']if p['part']==z['part']);scaling_ok(z,row,piece);scaling_records[digest]=z
 for name in FIXTURES:
  if 'normalized-component-curvature' in name:curvature_ok(fixtures[name],rows[fixtures[name]['records'][0]['cell']],scaling_records)
 oldscale=fixtures['parallel-model-pulse-lambda2-nodes-cell458.json']['seconds'];oldcurve=fixtures['parallel-root-normalized-component-curvature-cell458-q4096.json']['seconds']
 plan=dict(schema='fixed-pulse-normalized-curvature-818-plan-v1',source_sha256=self_sha,input_sha256=INPUT,source_identities={str(p):s for p,s in sources(a).items()},reused_report_identities=FIXTURES,construction_angles=4096,scalar_panels=4096,whole_cells=818,new_cells=816,new_scaling_calls=816,new_curvature_calls=816,reused_curvature_cells=[458,817],reused_scaling_pieces=3,exact_pulse_boundary=str(boundary),scalar_cell_counts=counts,adaptive_changes=False,parallel_workers=1,mathematical_kernel_edits=False,curvature_acceptance_threshold=None,uncompressed_input_bytes=len(clear),estimate=dict(basis='Published cell458 scaling and component-box wall times, no new representative computation',scaling_seconds=oldscale,curvature_seconds=oldcurve,sequential_seconds=816*(oldscale+oldcurve),planning_range_hours=[2,4],peak_RAM_MiB_estimate=[512,1024],RAM_estimate_not_measured_for_this_batch=True,new_report_disk_MiB_estimate=20),cells=rows)
 return plan,fixtures

def entry(row,p,d):
 z=d['records'][0]
 return dict(cell=row['cell'],left_exact=row['left_exact'],right_exact=row['right_exact'],action=row['action'],status='certified',angles=row['angles'],radial_subdivisions=8,report_path=str(p),report_sha256=sha(p),normalized_principal_curvature_upper=z['normalized_principal_curvature_upper'],metric_E_lower=z['metric_E_lower'],metric_determinant_lower=z['metric_determinant_lower'],scaling_bounds=z['scaling_bounds'])
def execute(a,plan,fixtures,self_sha):
 if a.outdir.exists()and any(a.outdir.iterdir()):raise ValueError('Execution directory must be new or empty; no silent restart')
 a.outdir.mkdir(parents=True,exist_ok=True);started=time.perf_counter();plan_sha=sha(a.plan)
 scaling=load(a.scaling_source,'fixed818_scaling');curvature=load(a.normalized_source,'fixed818_curvature')
 entries={};scaling_records={};counts=dict(new_scaling_calls=0,new_curvature_calls=0,processed_new_cells=0,failed_new_cells=0);fatal=None
 for name,digest in FIXTURES.items():
  p=a.outdir/'reused'/name;p.parent.mkdir(exist_ok=True);p.write_bytes((a.existing_reports/name).read_bytes())
  if sha(p)!=digest:raise ValueError('Reused report byte copy failed')
  d=fixtures[name]
  if 'lambda2-nodes' in name:scaling_records[digest]=d
  else:
   i=d['records'][0]['cell'];entries[i]=entry(plan['cells'][i],p,d)
 def progress(final=False):
  certified=[e for e in entries.values()if e['status']=='certified'];worst=max(certified,key=lambda e:e['normalized_principal_curvature_upper'])
  report=dict(schema='fixed-pulse-normalized-curvature-818-result-v1'if final else'fixed-pulse-normalized-curvature-818-progress-v1',source_sha256=self_sha,plan_sha256=plan_sha,input_sha256=INPUT,construction_angles=4096,adaptive_changes=False,whole_cells=818,already_published_reused_cells=2,covered_cells=len(certified),unvisited_new_cells=816-counts['processed_new_cells'],counts=dict(counts),maximum=worst,continuous_full_prefix_curvature_certified=bool(final and len(certified)==818 and not counts['failed_new_cells']and fatal is None),reach_certified=False,closed_surface=False,fixed_metric_solve_refinement=False,fatal=fatal,seconds=time.perf_counter()-started,maximum_RSS_kib=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)
  if final:report['entries']=[entries[i]for i in sorted(entries)]
  digest=save(a.outdir/('result.json'if final else'progress.json'),report)
  print(json.dumps(dict(event='curvature_complete'if final else'curvature_progress',report_sha256=digest,**{k:report[k]for k in ('covered_cells','unvisited_new_cells','counts','maximum','seconds','maximum_RSS_kib')})),flush=True)
 progress()
 try:
  for row in plan['cells']:
   if row['action']=='reuse':continue
   check_sources(a,self_sha)
   if sha(a.plan)!=plan_sha:raise ValueError('Prepared fixed plan changed during execution')
   i=row['cell'];stage='scaling';part=None;paths=[]
   try:
    for piece in row['scaling_pieces']:
     part=piece['part'];p=a.outdir/f'lambda-cell-{i:04d}-{part}.json';counts['new_scaling_calls']+=1
     args=SimpleNamespace(input=a.input,engine=a.engine,interval_source=a.interval_source,scalar_oracle=a.scalar_oracle,out=p,reference=None,cell=i,part=part)
     with contextlib.redirect_stdout(io.StringIO()):scaling.main(args)
     d=read(p);scaling_ok(d,row,piece);scaling_records[sha(p)]=d;paths.append(p)
    stage='curvature';p=a.outdir/f'curvature-cell-{i:04d}.json';counts['new_curvature_calls']+=1
    args=SimpleNamespace(input=a.input,interval_source=a.interval_source,raw_source=a.raw_source,out=p,scaling_reports=paths,cells=[i],angles=row['angles'],radial_subdivisions=8)
    with contextlib.redirect_stdout(io.StringIO()):curvature.main(args)
    d=read(p);curvature_ok(d,row,scaling_records);entries[i]=entry(row,p,d)
   except Exception as exc:
    available={};tb=exc.__traceback__
    while tb:
     for key in ('minE','minW2','worst','Amin','Amax','rho_min','rho_max','U','Dn','Rn','Sn','mD','mR','mS','ld','ls','lss','bmin'):
      value=tb.tb_frame.f_locals.get(key)
      if isinstance(value,(int,float))and math.isfinite(value):available[key]=value
     tb=tb.tb_next
    failure=dict(cell=i,stage=stage,part=part,exception_type=type(exc).__name__,message=str(exc),traceback=traceback.format_exc(),available_budgets=available,input_sha256=INPUT,source_sha256=self_sha,plan_sha256=plan_sha,retry=False)
    p=a.outdir/f'failure-cell-{i:04d}.json';digest=save(p,failure);entries[i]=dict(cell=i,left_exact=row['left_exact'],right_exact=row['right_exact'],action='compute_once',status='failed',stage=stage,failure_path=str(p),failure_sha256=digest);counts['failed_new_cells']+=1
   counts['processed_new_cells']+=1
   if counts['processed_new_cells']%8==0:progress()
 except Exception as exc:fatal=dict(exception_type=type(exc).__name__,message=str(exc),traceback=traceback.format_exc())
 try:
  check_sources(a,self_sha)
  if sha(a.plan)!=plan_sha:raise ValueError('Prepared plan changed before final report')
 except Exception as exc:
  final_identity=dict(exception_type=type(exc).__name__,message=str(exc),traceback=traceback.format_exc())
  fatal=final_identity if fatal is None else dict(previous=fatal,final_identity=final_identity)
 progress(final=True)

def main(a):
 start=time.perf_counter();require_external_outputs(a);self_sha=sha(__file__);plan,fixtures=prepare(a,self_sha)
 if a.execute:
  if not a.plan.exists()or read(a.plan)!=plan:raise ValueError('Execute requires the previously frozen identical preparation plan')
  execute(a,plan,fixtures,self_sha);return
 if a.plan.exists()or a.plan.with_suffix('.preparation.json').exists():raise ValueError('Preparation outputs already exist')
 digest=save(a.plan,plan);check_sources(a,self_sha)
 report=dict(schema='fixed-pulse-normalized-curvature-818-preparation-v1',source_sha256=self_sha,plan_path=str(a.plan),plan_sha256=digest,policy={k:v for k,v in plan.items()if k not in ('cells','source_identities')},new_scaling_calls_executed=0,new_curvature_calls_executed=0,published_reports_fully_validated=5,unsupported_interior_scalar_boundaries=0,reused_curvature_bounds={str(i):fixtures[f'parallel-root-normalized-component-curvature-cell{i}-q{8192 if i==817 else 4096}.json']['records'][0]['normalized_principal_curvature_upper']for i in (458,817)},seconds=time.perf_counter()-start,maximum_RSS_kib=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)
 p=a.plan.with_suffix('.preparation.json');digest=save(p,report);print(json.dumps(dict(event='prepared_only',report=str(p),report_sha256=digest,plan_sha256=report['plan_sha256'],new_geometry_calls=0,seconds=report['seconds'])),flush=True)

if __name__=='__main__':
 p=argparse.ArgumentParser(description=__doc__)
 for name in ('input','raw-source','normalized-source','scaling-source','engine','interval-source','scalar-oracle','existing-reports','plan','outdir'):p.add_argument('--'+name,type=Path,required=True)
 p.add_argument('--execute',action='store_true')
 main(p.parse_args())
