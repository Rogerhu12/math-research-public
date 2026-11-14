#!/usr/bin/env python3
"""Finite posterior update on saved true outer9/8/7 columns; no new ODE.
Scale only the complete initial K uncertainty by the exact R148/R119
normalized-radius ratio. Rebuild whole-cell positive component caps from
signed centre + new uncertainty; never subtract rounded aggregate budgets.
"""
from pathlib import Path
from fractions import Fraction as F
import copy,gzip,hashlib,json,resource,time,sys
B=Path('/workspace/scratch/d1aa462cfc02');EW=B/'exact-work'
sys.path.insert(0,str(EW/'python-deps'))
from flint import arb,ctx
P=B/'root-work/r127/sparse-complete-low-r1.json.gz';RES=B/'root-work/r127/sparse-complete-low-r1-resource.json'
EXPECTED='0c7e11319c9f9d4e705a7f3ed742ab0f4239529e7117a4fbaf5b2cd33a15c56f'


def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def read(p):
 with (gzip.open(p,'rt') if str(p).endswith('.gz') else open(p)) as f:return json.load(f)
def q(v):
 if isinstance(v,list):return F(int(v[0]))*F(2)**int(v[1])
 if 'upper' in v:return q(v['upper'])
 if 'numerator' in v:return F(int(v['numerator']),int(v['denominator']))
 return F(int(v['mantissa']))*F(2)**int(v['binary_exponent'])
def rat(v):return {'numerator':str(v.numerator),'denominator':str(v.denominator)}
def pack(v,bits=192):
 if v<0:raise ArithmeticError('A positive saved uncertainty must not become negative')
 if not v:return ['0',0]
 e=v.numerator.bit_length()-v.denominator.bit_length()
 if v<F(2)**e:e-=1
 e-=bits-1;t=v/F(2)**e;m=(t.numerator+t.denominator-1)//t.denominator
 z=F(m)*F(2)**e
 if z<v:raise ArithmeticError('Wrong upward rounding')
 return [str(m),e]
def ab(v):return arb(v.numerator)/v.denominator
def aub(v):
 if not v.is_finite() or not v.upper()>=0:raise ArithmeticError('Finite nonnegative angular weight required')
 m,e=v.upper().man_exp();return F(int(m))*F(2)**int(e)
def abs_interval(d):return max(abs(q(d['lower'])),abs(q(d['upper'])))
def lower_abs_interval(d):
 lo,hi=q(d['lower']),q(d['upper'])
 return lo if lo>0 else -hi if hi<0 else F(0)


def main():
 ctx.prec=256;ctx.threads=1;start=time.monotonic();g={}
 def ck(k,v):
  if not v:raise ArithmeticError(k)
  g[k]=True
 ck('R148_exact_input',sha(P)==EXPECTED);sp=read(P);res=read(RES)
 ck('R148_actual_success',sp['all_gates'] and all(sp['gates'].values()) and res['exitcode']==0 and res['termination_signal'] is None)
 ck('R148_independent_saved_audit',read(EW/'r148-saved-fraction-audit-r1.json')['all_gates'])
 modes=list(range(2,93,2));r0=q(sp['common_original_h_radius']);caps=list(map(q,sp['all92_component_caps']))
 weights=[aub((1+m)*(arb(m)/64).exp()) for m in modes]
 cells=[]
 for cell in [9,8,7]:
  src=EW/f'outer{cell}-signed-low46-r1.json';sr=EW/f'outer{cell}-signed-low46-run1-resource.json'
  out=EW/f'outer{cell}-signed-low46-r148-update-r1.json'
  if out.exists():raise FileExistsError(out)
  old=read(src);ores=read(sr)
  ck(f'cell{cell}_actual_linear_source',old['all_gates'] and all(old['gates'].values()) and ores['exitcode']==0 and ores['termination_signal'] is None)
  ck(f'cell{cell}_original_expanded_subdomain',old['config']['parameter_domain']['name']=='expanded_profile' and q(old['config']['parameter_domain']['S_product_radius'])<=1 and q(old['config']['parameter_domain']['T_l1_radius'])<=F(1,32))
  ratios=[]
  for j,row in enumerate(old['input_rows']):
   m=modes[j];kold=q(row['CL_minus_LR_K_normalized_cap']);knew=caps[2*j+1];u=q(row['u_block24_pair_normalized_cap'])
   ck(f'cell{cell}_same_nonnegative_mode_{m}',row['mode']==m and row['initial_P_error_exact_zero'] and 0<knew<=kold and u>=0)
   ratio=(min(knew,r0)+u)/(min(kold,r0)+u)
   ck(f'cell{cell}_exact_ratio_{m}',0<ratio<=1);ratios.append(ratio)
  positive=[[F(0),F(0)] for m in modes];centreonly=[[F(0),F(0)] for m in modes];erroronly=[[F(0),F(0)] for m in modes]
  seen=0;previous=None
  for piece in old['profile_chunks']:
   ck(f'cell{cell}_profile_pin_{seen}',sha(piece['path'])==piece['sha256']);data=read(piece['path'])
   for row in data['rows']:
    seen+=1
    ck(f'cell{cell}_step_modes_{seen}',[z['mode'] for z in row['whole_homogeneous_profiles']]==modes)
    for j,z in enumerate(row['whole_homogeneous_profiles']):
     for c in range(2):
      centre=abs_interval(z['linear_PK'][c]);unc=q(z['initial_error_PK'][c])*ratios[j]
      centreonly[j][c]=max(centreonly[j][c],centre);erroronly[j][c]=max(erroronly[j][c],unc)
      positive[j][c]=max(positive[j][c],centre+unc)
   del data
   if resource.getrusage(resource.RUSAGE_SELF).ru_maxrss>98304:raise MemoryError('Keep original96MiB consumption guard')
  ck(f'cell{cell}_all_original_steps',seen==old['counts']['taylor']+old['counts']['root_brackets'])
  oldcaps=old['whole_cell_component_caps']
  for j,m in enumerate(modes):
   for c,key in enumerate(['P','K']):ck(f'cell{cell}_new_valid_component_min_{m}_{key}',positive[j][c]<=q(oldcaps[j][key]))
  new=copy.deepcopy(old)
  new['schema']='same-signed-low46-outer-flow-R148-initial-error-update-v1'
  new['posterior_source_sha256']=sha(__file__);new['original_flow_primary']=str(src);new['original_flow_sha256']=sha(src)
  new['posterior_input_sha256']=EXPECTED;new['posterior_resource_sha256']=sha(RES)
  new['no_new_ODE_or_integration']=True
  new['old_profile_chunks_remain_valid_conservative_upper_bounds']=True
  new['actual_updated_complete_initial_K_errors']=True
  for j,row in enumerate(new['input_rows']):
   row['R119_original_K_normalized_cap']=row['CL_minus_LR_K_normalized_cap']
   row['CL_minus_LR_K_normalized_cap']=pack(min(caps[2*j+1],q(row['CL_minus_LR_K_normalized_cap'])),bits=256)
   row['R148_exact_K_normalized_cap']=rat(caps[2*j+1]);row['exact_initial_error_scale_ratio']=rat(ratios[j])
   row['complete_initial_K_error']=pack(q(row['complete_initial_K_error'])*ratios[j],bits=256)
  erows=new.get('endpoint_modes',new.get('node9_modes'))
  for j,row in enumerate(erows):row['initial_error_PK']=[pack(q(v)*ratios[j],bits=256) for v in row['initial_error_PK']]
  new['whole_cell_component_caps']=[{'mode':m,'P':pack(positive[j][0]),'K':pack(positive[j][1])} for j,m in enumerate(modes)]
  strong=sum((weights[j]*(positive[j][0]+positive[j][1]) for j in range(46)),F(0))
  strong=min(strong,q(old['whole_cell_homogeneous_strong_mass_at_sigma1over64']))
  new['whole_cell_homogeneous_strong_mass_at_sigma1over64']=pack(strong,bits=256)
  cs=sum((weights[j]*sum(centreonly[j],F(0)) for j in range(46)),F(0))
  es=sum((weights[j]*sum(erroronly[j],F(0)) for j in range(46)),F(0))
  new['whole_cell_linear_reference_only_strong_mass']=pack(cs)
  new['whole_cell_initial_error_only_strong_mass']=pack(es)
  new['posterior_rebuilt_positive_component_caps_before_mode_sum']=True
  new['all_gates']=True;new['posterior_gates']={k:v for k,v in g.items() if k.startswith(f'cell{cell}_')}
  out.write_text(json.dumps(new,separators=(',',':'))+'\n')
  cells.append(dict(cell=cell,primary=str(out),sha256=sha(out),old_primary_sha256=sha(src),profiles=seen,
    whole_homogeneous=pack(strong),linear_reference_only=pack(cs),initial_error_only=pack(es),
    still_only_homogeneous_not_full_nonlinear_field=True))
  print(json.dumps(dict(cell=cell,whole_homogeneous=float(strong),reference_only=float(cs),initial_error_only=float(es),profiles=seen,elapsed_seconds=time.monotonic()-start)),flush=True)
 # A pointwise signed linear-reference lower bound separates the new
 # numerical small-domain obstruction from a possible loose uncertainty.
 cp=read(EW/'outer7-signed-low46-r1-completed-segment4.json');centre2=cp['modes'][0]
 kmin=lower_abs_interval(centre2['linear_PK'][1])
 ck('cell7_exact_linear_K2_lower_exceeds1over128',kmin>F(1,128))
 result=dict(schema='same-outer9to7-signed-flows-R148-initial-error-update-v1',source_sha256=sha(__file__),input_primary_sha256=EXPECTED,input_resource_sha256=sha(RES),all_gates=True,gate_count=len(g),gates=g,cells=cells,
  cell7_segment4_endpoint_linear_K2_absolute_lower=rat(kmin),
  linear_reference_small_domain_obstruction_only=True,actual_nonlinear_PDE_failure_claimed=False,
  exact_domain='Original R141 expanded profile, a subset of S<=1 and T_l1<=1/32',
  mean_and_all_nonlow_sources_not_removed_or_claimed_paid=True,elapsed_seconds=time.monotonic()-start,peak_rss_kib=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)
 out=EW/'outer9to7-r148-update-r1.json'
 if out.exists():raise FileExistsError(out)
 out.write_text(json.dumps(result,separators=(',',':'))+'\n')
 print(json.dumps(dict(all_gates=True,gates=len(g),sha256=sha(out),elapsed_seconds=result['elapsed_seconds'],peak_rss_kib=result['peak_rss_kib'])),flush=True)
if __name__=='__main__':main()
