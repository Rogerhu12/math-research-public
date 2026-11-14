#!/usr/bin/env python3
"""Same actual node10 field: all finite windows and infinity through signed
full-panel diagonal comparison. Reuse every original14069 background panel.
No ODE, integral, source solve or Fourier widening is performed.
Author: exact_closure (GPT-6 Astra Pro; AI-assisted),2026-11-13.
"""
import argparse,gzip,hashlib,json,resource,time
from pathlib import Path
from flint import arb,ctx,fmpq as Q

B=Path('/workspace/scratch/d1aa462cfc02');E=B/'exact-work'
PINS={
 'ordered':(E/'outer9to7-ordered-high-r1-summary.json.gz','78ffa4f5b7b550578b82d65b4a2c4072ba3fa0b9eb00933448dde596946ae9de'),
 'ordered_resource':(E/'outer9to7-ordered-high-run1-resource.json','63b40c41d0a6508bdbc8562bb85d427654dbbf155e2480f1f054a3a238bc52af'),
 'posterior':(E/'outer-newwide186-logr-batch01-certificate.json.gz','91a1adcb52507f04652ffbcd28c7cb2e509aa7871aa505ada4e1490fa9d62cb1'),
 'posterior_resource':(E/'outer-newwide186-logr-run01-resource.json','981952736123cfe84e40bf3685bb80313888ed2811d8f7d29448b95fc6eeaeb5'),
 'node10':(E/'outer9-signed-low46-r1.json','c19d33f403f42c0b98ada4572aa58f860f17d922cd5e353d680d477d75640c07'),
 'node10_sigma':(B/'root-work/r127/low-frequency-r1-source-block24.json.gz','7cf7df55585edd07a66d0ecc2e97fb41aa414dbdd7701c9f8f4ece708e1cc3c9'),
 'signed_near':(E/'node10-logr-batch01.json','7c6c7ae13b25f5f768d84673f03b47602906ebd80049deae359b78c09edc06fa'),
 'signed_near_resource':(E/'node10-logr-batch01-resource.json','239a4fe6a531d62b2022e55eb3db5934904e06a929cd48f190b3ba2eb4934517'),
}
def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def read(p):
 with (gzip.open(p,'rt') if str(p).endswith('.gz') else open(p)) as f:return json.load(f)
def ex(v):
 if isinstance(v,Q):return v
 if isinstance(v,(int,str)):return Q(v)
 if isinstance(v,dict):
  if 'upper' in v:return ex(v['upper'])
  if 'mantissa' in v:return Q(int(v['mantissa']))*Q(2)**int(v['binary_exponent'])
  return Q(int(v['numerator']),int(v['denominator']))
 return Q(int(v[0]))*Q(2)**v[1] if isinstance(v[1],int) else Q(int(v[0]),int(v[1]))
def pack(z,positive=True):
 z=z if isinstance(z,arb) else arb(ex(z))
 if not z.is_finite() or (positive and z.lower()<0):raise ArithmeticError('finite saved bound')
 u=z.upper()
 if u==0:return ['0',0]
 m,e=map(int,u.man_exp());bits=max(0,abs(m).bit_length()-160)
 if bits:m,e=-((-m)//(1<<bits)),e+bits
 if not arb(m)*arb(2)**e>=u:raise ArithmeticError('outward save')
 return [str(m),e]
def up(z,positive=True):return ex(pack(z,positive))
def support(coef,caps,mass,parent):
 z=Q(0);left=mass;group=parent
 for w in sorted(range(len(coef)),key=lambda k:coef[k],reverse=True):
  if not coef[w] or not left:break
  take=min(caps[w],left,group if w<2 else left)
  z+=coef[w]*take;left-=take
  if w<2:group-=take
 return z

def main():
 p=argparse.ArgumentParser(description=__doc__);p.add_argument('--out',type=Path,required=True);a=p.parse_args()
 if a.out.exists():raise FileExistsError('fresh actual initial-field budget')
 ctx.prec,ctx.threads=256,1;start=time.monotonic();g={};docs={};ids={}
 def gate(k,b):
  if not b:raise ArithmeticError(k)
  g[k]=True
 for k,(path,pin) in PINS.items():gate('pin_'+k,sha(path)==pin);docs[k]=read(path);ids[k]=dict(path=str(path),sha256=pin)
 for k in ('ordered_resource','posterior_resource','signed_near_resource'):gate('owned0_'+k,docs[k]['exitcode']==0 and docs[k]['termination_signal'] is None)
 order,post=docs['ordered'],docs['posterior'];near=docs['signed_near']
 gate('all_actual_inputs_complete',order['all_gates'] and post['all_gates'] and near['all_gates'] and post['same_existing_actual_R163_field'] and post['full_mean_inverse_and_positive_infinite_retained'] and not post['unknown_old_infinite_caps_reweighted'])
 gate('same_real_node10_projection',post['comparison_partition'][24]['cell']==10 and post['comparison_partition'][24]['segment']==8 and near['node10_P_nonlow_exactly_zero'] and near['inputs']['posterior']['sha256']==PINS['posterior'][1])
 shift=ex(post['angular_weight_translation']);gate('same_actual_shift040',shift==Q(2,5))
 sigma_in=ex(docs['node10_sigma']['sigma_min'])+shift;sigma_out=Q(1,64);gap=sigma_in-sigma_out
 V=ex(docs['node10']['config']['local_V_node10']);gate('same_actual_point_V',V==ex(near['node10_local_V']) and V>0)
 W=post['windows'];caps=list(map(ex,post['window_caps'][24]));mass=ex(post['finite_caps'][24]);high=ex(post['high_caps'][24]);parent=min(ex(post['parent94_mass_caps'][24]),mass,sum(caps[:2],Q(0)))
 gate('all186_physical_finite_windows',len(W)==len(caps)==186 and sum((list(range(lo,hi+1,2)) for lo,hi in W),[])==list(range(94,34816,2)))
 modes=sorted({lo for lo,hi in W}|{186,194,258,514,1026,2050,4098,8192,16384,24576,28672,32768,34816})
 maxima={n:[None]*len(modes) for n in (9,8,7)};where={n:[None]*len(modes) for n in (9,8,7)}
 G=D=Q(0);first_b=None;index=0;cell_counts={9:0,8:0,7:0};coverage=[];current=None;right=Q(0);max_b=Q(0);positive_diag=Q(0);jumps=Q(0);parts=[]
 for part in order['kernel_parts']:
  gate('part_pin_'+str(part['first_index']),sha(part['path'])==part['sha256']);data=read(part['path']);parts.append(part)
  for row in data['rows']:
   gate('index_'+str(index),row['index']==index)
   n,j=row['cell'],row['segment'];left,end=Q(row['left']),Q(row['right']);key=(n,j)
   if key!=current:
    if current is not None:gate('end_'+str(current),right==1)
    gate('start_'+str(key),left==0 and key not in coverage);coverage.append(key);current=key
   else:gate('continuity_'+str(index),left==right)
   gate('positive_length_'+str(index),0<=left<end<=1);right=end
   b=ex(row['frame']);gamma=ex(row['full_panel_phase']);diag=ex(row['signed_full_panel_diagonal']);jump=ex(row['forward_next_frame_jump'])
   gate('positive_comparison_inputs_'+str(index),b>0 and gamma>=0 and jump>=0)
   if first_b is None:first_b=b
   # Pure K input has balanced norm |K|/b0. Both physical components
   # use separate radial sup, hence 2max(1,b) at this actual panel.
   logc=up(arb(2*max(Q(1),b)/first_b).log(),positive=False)
   Gend,Dend=G+gamma,D+diag
   for k,m in enumerate(modes):
    # This is the propagated positive comparison endpoint, not a
    # possibly smaller actual endpoint value. The fixed-rate bound
    # attains its maximum at one of the two comparison endpoints.
    value=max(m*G+D,m*Gend+Dend)+logc
    if maxima[n][k] is None or value>maxima[n][k]:maxima[n][k]=value;where[n][k]=index
   G,D=Gend,Dend+jump;positive_diag+=max(Q(0),diag);jumps+=jump;max_b=max(max_b,b);index+=1;cell_counts[n]+=1
  del data
  if index%1024<32:
   gate('resource_'+str(index),resource.getrusage(resource.RUSAGE_SELF).ru_maxrss<98304)
   print(json.dumps(dict(event='actual_ordered_initial_prefix',panels=index,peak_rss_kib=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)),flush=True)
 gate('all14069_original_panels',index==order['total_original_material_panels']==14069 and right==1 and coverage==[(n,j) for n in (9,8,7) for j in range(9)])
 gate('entire_entry_to_output_strip_reserve',gap>G>0)
 lookup={m:i for i,m in enumerate(modes)};answers=[]
 for n in (9,8,7):
  coefficients={m:up(arb(maxima[n][k]-m*gap).exp()*arb(V)) for k,m in enumerate(modes)}
  window_coeff=[coefficients[lo] for lo,hi in W]
  rest_coeff=[z if lo>=186 else Q(0) for (lo,hi),z in zip(W,window_coeff)]
  full=up(support(window_coeff,caps,mass,parent));rest=up(support(rest_coeff,caps,mass,parent));hi=up(coefficients[34816]*high)
  near_saved=next(r for r in near['rows'] if r['cell']==n);near_cap=ex(near_saved['best_paid_initial']);combined=up(near_cap+rest+hi)
  tails=[]
  for M in (186,194,258,514,1026,2050,4098,8192,16384,24576,28672,32768,34816):
   # One constant at M bounds every frequency >=M, including a
   # boundary-straddling finite window whose full mass is retained.
   selected=[Q(1) if h>=M else Q(0) for l,h in W];fm=support(selected,caps,mass,parent)
   tails.append(dict(minimum_physical_even_mode=M,finite_mass_cap=pack(fm),infinite_mass_cap=pack(high),whole_tail_upper=pack(up(coefficients[M]*(fm+high))),input_to_output_coefficient=pack(coefficients[M]),maximizing_original_panel=where[n][lookup[M]]))
  top=sorted([(up(window_coeff[w]*caps[w]),w) for w in range(186) if W[w][0]>=186],reverse=True)[:12]
  answers.append(dict(cell=n,finite_all_94to34814=pack(full),finite_rest186to34814=pack(rest),complete_infinite34816up=pack(hi),existing_signed_near94to184=pack(near_cap),combined_all_nonlow_initial=pack(combined),window_input_coefficients=list(map(pack,window_coeff)),tails=tails,largest_separate_rest_window_terms=[dict(window=W[w],upper=pack(z)) for z,w in top],full_mean_inverse_and_infinite_entry_retained=True,combined_below1over16=bool(combined<Q(1,16))))
  print(json.dumps(dict(cell=n,finite_rest_log2=str(arb(rest).log()/arb(2).log()),infinite_log2=str(arb(hi).log()/arb(2).log()),combined_log2=str(arb(combined).log()/arb(2).log()))),flush=True)
 gate('final96MiB',resource.getrusage(resource.RUSAGE_SELF).ru_maxrss<98304)
 result=dict(schema='same_actual_node10_signed_diagonal_ordered_all_window_homogeneous_budget_v1',author='exact_closure (GPT-6 Astra Pro; AI-assisted)',source_sha256=sha(__file__),inputs=ids,original_panel_parts=parts,all_gates=True,gates=g,gate_count=len(g),actual_scope=post['actual_scope'],angular_weight_translation='2/5',input_sigma=pack(sigma_in),output_sigma='1/64',complete_phase=pack(G),entry_strip_reserve=pack(gap-G),input_frame=pack(first_b),maximum_frame=pack(max_b),positive_diagonal_for_comparison=pack(positive_diag),complete_frame_jumps=pack(jumps),signed_final_diagonal_and_jumps=pack(D,positive=False),node10_localV=pack(V),original_panels=index,original_cell_panel_counts=cell_counts,windows=W,input_window_caps=list(map(pack,caps)),input_finite_common_mass=pack(mass),input_complete_high_mass=pack(high),input_parent94_mass=pack(parent),rows=answers,complete_input_frequency_coverage=True,finite_lowest_mode_monotonicity_paid=True,all_partial_output_points_paid_by_comparison_endpoints=True,physical_two_component_radial_sup_and_initial_frame_paid=True,nonlinear_feedback_paid=False,new_ODE_or_source_or_integral=False,positive_budget_failure_is_not_PDE_obstruction=True,precision_bits=256,elapsed_seconds=time.monotonic()-start,peak_rss_kib=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)
 a.out.write_text(json.dumps(result,separators=(',',':'))+'\n')
 print(json.dumps(dict(all_gates=True,path=str(a.out),sha256=sha(a.out),gate_count=len(g),elapsed_seconds=time.monotonic()-start,peak_rss_kib=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)),flush=True)
if __name__=='__main__':main()
