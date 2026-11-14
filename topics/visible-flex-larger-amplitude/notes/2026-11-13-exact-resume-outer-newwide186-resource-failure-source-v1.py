#!/usr/bin/env python3
"""Complete finite posterior on the actual R163 width+2/5 outer field.

The actual finite low projection LF is fixed. New missing Laurent source
coefficients are evaluated once; all original Green kernels are reused.
No old unknown infinite cap is widened, no ODE is repeated, and no new
fixed point is inferred from these finite monotone substitutions.
Author: exact_closure (GPT-6 Astra Pro; AI-assisted), 2026-11-13.
"""
from __future__ import annotations
import argparse, gc, gzip, hashlib, importlib.util, json, resource, sys, time
from fractions import Fraction as F
from pathlib import Path
from flint import arb, ctx, fmpq as Q

M=34816
MODES=list(range(2,93,2))
ZERO=Q(0)
def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def read(p):
 b=Path(p).read_bytes();return json.loads(gzip.decompress(b) if str(p).endswith('.gz') else b)
def ex(v):
 if isinstance(v,Q):return v
 if isinstance(v,F):return Q(v.numerator,v.denominator)
 if isinstance(v,int):return Q(v)
 if isinstance(v,str):return Q(v)
 if isinstance(v,dict):
  if 'upper' in v:return ex(v['upper'])
  return Q(int(v['numerator']),int(v['denominator']))
 return Q(int(v[0]))*Q(2)**v[1] if isinstance(v[1],int) else Q(int(v[0]),int(v[1]))
def ff(v):
 v=ex(v);return F(int(v.p),int(v.q))
def pack(v,bits=160):
 z=v if isinstance(v,arb) else arb(ex(v))
 if not z.is_finite() or z.upper()<0:raise ArithmeticError('finite nonnegative bound required')
 u=z.upper()
 if u==0:return ['0',0]
 m,e=map(int,u.man_exp());s=max(0,m.bit_length()-bits)
 if s:m,e=(m+(1<<s)-1)>>s,e+s
 if not arb(m)*arb(2)**e>=u:raise ArithmeticError('outward serialization')
 return [str(m),e]
def up(v):return ex(pack(v))
def exp(v):return up(arb(ex(v)).exp())
def support(coeff,caps,mass,parent):
 left=mass;group=parent;z=ZERO
 for w,a in sorted(coeff,key=lambda p:p[1],reverse=True):
  if not a or not left:break
  if a<0:raise ArithmeticError('positive support only')
  q=min(caps[w],left,group if w<2 else left)
  z+=a*q;left-=q
  if w<2:group-=q
 return up(z)
def save(p,d):
 if p.exists():raise FileExistsError(p)
 b=(json.dumps(d,separators=(',',':'))+'\n').encode()
 if str(p).endswith('.gz'):b=gzip.compress(b,mtime=0)
 if len(b)>=5000000:raise ArithmeticError('one output exceeds5MB')
 p.write_bytes(b);return dict(path=str(p),sha256=sha(p),bytes=len(b))
def owned0(r):return r.get('exitcode',r.get('exit_code'))==0 and r.get('termination_signal') is None

def dq_geometry(window,inputs):
 """Every membership interval; alpha(k,n) increases with even n.

 Return the exact segment-end candidates. All weights on one segment
 are positive constants times alpha(k,n), so these endpoints suffice.
 """
 lo,hi=window;out=[]
 for w,(a,b) in enumerate(inputs):
  intervals=[]
  for k in MODES:
   for branch,l,h in ((0,lo-k,hi-k),(1,lo+k,hi+k)):
    l=max(l,a);h=min(h,b)
    if l<=h:intervals.append((k,branch,l,h))
  if not intervals:continue
  candidates=[]
  for n in sorted({h for k,t,l,h in intervals}):
   terms=[(k//2-1,t,Q(5*k*n+1,4*(1+k)*(1+n))) for k,t,l,h in intervals if l<=n<=h]
   if terms:candidates.append((n,terms))
  out.append((w,candidates))
 return out

def main():
 p=argparse.ArgumentParser(description=__doc__);p.add_argument('--inputs',type=Path,required=True);p.add_argument('--out-prefix',type=Path,required=True);p.add_argument('--cycles',type=int,default=16);a=p.parse_args()
 if not 1<=a.cycles<=64:raise ValueError('explicit finite iteration count')
 if list(a.out_prefix.parent.glob(a.out_prefix.name+'-*')):raise FileExistsError('fresh prefix required')
 a.out_prefix.parent.mkdir(parents=True,exist_ok=True)
 ctx.prec,ctx.threads=512,1;start=time.monotonic();ids=read(a.inputs);gates={};counts={}
 def gate(k,v,n=1):
  if not v:raise ArithmeticError(k)
  gates[k]=True;counts[k]=counts.get(k,0)+n
 def get(k):
  q=ids[k];gate('pin_'+k,sha(q['path'])==q['sha256']);return read(q['path'])
 def rss():gate('owned_RSS_below96MiB',resource.getrusage(resource.RUSAGE_SELF).ru_maxrss<98304)
 wide=get('R163');old=get('R156');r160=get('R160');head=get('head')
 for k in ('R163_resource','R156_resource','R160_resource','head_resource','singleton_resource'):gate('owned0_'+k,owned0(get(k)))
 gate('actual_R163_same_full_field',wide['all_gates'] and wide['actual_complete_new_width_nonlow_field'] and wide['same_original_actual_full_field_identified'] and not wide['old_unknown_infinite_caps_reweighted'] and wide['complete_mean_inverse_far_and_shared_T_retained'])
 gate('old186_same_actual_field',old['all_gates'] and old['same_existing_R127_field'] and old['all186_refinement_and_parent94_constraint_retained'])
 delta=ex(wide['angular_shift']);gate('shift040',delta==Q(2,5))
 gate('same_actual_translated_head',head['all_gates'] and head['complete_mean_inverse_far'] and head['complete_infinite_repaid'] and head['domain']==wide['parameter_domain'] and ex(head['angular_weight_translation'])==delta and head['same_original617_units']['sha256']=='617987048c3a599acb42bcafe8dba99155c5cde82d252706769d5e24340ce1b9')
 gate('R163_used_same_complete_LF_source',wide['inputs']['R160_primary']['sha256']==ids['R160']['sha256'] and r160['low_projection_is_actual_existing_field_not_redefined_CL'] and r160['complete_mean_inverse_and_infinite_positive_sources'])
 windows=old['windows'];gate('complete186_partition',len(windows)==186 and windows[:2]==[[94,94],[96,96]] and sum((list(range(lo,hi+1,2)) for lo,hi in windows),[])==list(range(94,M,2)))
 old={k:old[k] for k in ('windows','window_caps','retained_parent94_mass_caps')}
 r160={'source_rows':r160['source_rows']}
 outputs=windows+[[94,96]]
 nr=get('nonlow');near=get('near');single=get('singleton_kernels')
 gate('same25_original_geometry',nr['all_gates'] and near['all_gates'] and single['all_gates'] and nr['comparison_partition']==wide['comparison_partition']==single['comparison_partition'] and single['common_strip']==nr['fixed_common_strip'])
 for k in ('source_helper','nonlow_helper'):gate('pin_'+k,sha(ids[k]['path'])==ids[k]['sha256'])
 sys.path.insert(0,str(Path(ids['nonlow_helper']['path']).parent))
 from nonlow_interface import NonlowInterface
 ni=NonlowInterface(nr,near);V=list(map(ex,ni.V));B=ex(nr['physical_high_conversion']);S=ex(nr['profile_to_V_upper']);Rp=ex(nr['profile_physical_upper'])
 Hphys=[Rp if j==21 else B if j==5 else V[j] for j in range(25)]
 highcoeff=[[tuple(map(ex,ni.coefficients(i,j)[3:])) for j in range(i+1)] for i in range(25)]
 highhead0=get('high');balanced=get('balanced');Bcut=ex(balanced['balanced_B_lower'])
 del ni,nr,near;gc.collect()
 mats=[None]*187;gains=[None]*187
 positions={tuple(w):i for i,w in enumerate(outputs)}
 def add_kernel(w,row):
  gate('unique_window_kernel',mats[w] is None)
  gate('same_original_row_'+str(w),row['window']==outputs[w] and row['common_strip_already_paid'] and len(row['rows'])==25)
  wm=[];wg=[]
  for i,target in enumerate(row['rows']):
   gate('complete_causal_target',target['target_block']==i)
   g,one,zero=[[ex(v) for v in target['three_materials'][str(p)]] for p in (2,1,0)]
   gate('three_complete_materials',all(len(v)==i+1 and all(x>=0 for x in v) for v in (g,one,zero)))
   c=[];s=[]
   for j in range(i+1):
    if j==5:c.append(B*one[j]);s.append(B*B*zero[j])
    elif j==21:c.append(min(S*g[j],Rp*one[j]));s.append(min(S*S*g[j],S*Rp*one[j],Rp*Rp*zero[j]))
    else:c.append(g[j]);s.append(g[j])
   wm.append((g,c,s));wg.append(ex(target['head_gain']))
  mats[w]=wm;gains[w]=wg
 for w,row in enumerate(single['rows']):add_kernel(w,row)
 count=0
 for rec in ids['window_kernel_records']:
  gate('kernel_part_pin',sha(rec['path'])==rec['sha256'])
  with gzip.open(rec['path'],'rt') as f:
   for line in f:
    row=json.loads(line);add_kernel(positions[tuple(row['window'])],row);count+=1
 gate('all185_parent_kernels',count==185 and all(x is not None for x in mats))
 del single,row;gc.collect();rss()
 hm=list(map(ex,head['translated_head_band_masses']));hw=head['windows'];hwm=list(map(ex,head['translated_head_window_masses']))
 headm=[]
 for lo,hi in outputs:
  band=0 if hi<=184 else 1 if hi<=8190 else 2
  mass=hm[2] if band==2 else min(hm[band],sum((v for (l,h),v in zip(hw,hwm) if l<=hi and lo<=h),ZERO))
  gate('positive_real_head_window',mass>0);headm.append(mass)
 split=head['shift040_tail_split']
 gate('actual_complete34816_projection',split['physical_mode_bands']==[[8192,34814],[34816,None]] and ex(split['parent_shared_mass_at040'])==hm[2])
 h34816=ex(split['upper_masses'][1])
 hh=[]
 for j,row in enumerate(highhead0['rows']):
  if j==21:c=row['initial_profile_balanced_column_sups'];gain=max(ex(c[0])/Bcut,ex(c[1]))
  elif j==5:c=row['initial_balanced_column_sups'];gain=max(ex(c[0])/Bcut,ex(c[1]))
  else:c=row['initial_localV_separate_component_sups'];gain=max(sum(map(ex,c[0]),ZERO)/Bcut,sum(map(ex,c[1]),ZERO))
  hh.append(up(gain*h34816))
 lowcaps=[[ex(v) for v in row] for row in wide['actual_low_new_width_caps']];C=[sum(row,ZERO) for row in lowcaps]
 gate('all25_actual_finite_LF',len(lowcaps)==25 and all(len(r)==46 for r in lowcaps))
 r=list(map(ex,wide['finite_caps']));h=list(map(ex,wide['high_caps']));seedr=r[:];seedh=h[:]
 oldparent=list(map(ex,old['retained_parent94_mass_caps']))
 v=[[min(r[j],up(ex(cap)*exp(hi*delta))) for cap,(lo,hi) in zip(old['window_caps'][j],windows)] for j in range(25)]
 parent=[min(r[j],v[j][0]+v[j][1],up(oldparent[j]*exp(96*delta))) for j in range(25)]
 lowsrc=get('low_sources');sigma=[];source_records=[];pure=[];purehigh=[]
 spec=importlib.util.spec_from_file_location('complete_finite_source',ids['source_helper']['path']);src=importlib.util.module_from_spec(spec);spec.loader.exec_module(src)
 for j,rec in enumerate(lowsrc['source_records']):
  gate('low_block_pin',sha(rec['path'])==rec['sha256']);block=read(rec['path'])
  gate('same_low_source_block',block['index']==j and block['modes']==MODES)
  sig=ex(block['sigma_min'])+delta;sigma.append(sig)
  original=r160['source_rows'][j]
  gate('same_R160_fixed_LF',original['block']==j and original['new_actual_finite_pair_caps']==wide['actual_low_new_width_caps'][j] and original['exact_finite_source_extra_width']=='1/2')
  plus=[ff(up(c*exp(Q(m,2)))) for m,c in zip(MODES,lowcaps[j])]
  positive=src.complete_source(plus,ff(V[j]),32)
  gate('same_complete_source_mean_inverse_tail',positive['mean_zero_cap']==original['source_mean_zero_cap'] and positive['inverse_leading_mass']==original['source_inverse_leading_mass'] and positive['shared_complete_inverse_tail']==original['complete_inverse_tail'])
  pairs=[(p['mode'],ex(p['bound'])) for p in positive['polynomial_pair_rows']];tail=ex(positive['shared_complete_inverse_tail'])
  gate('strict_positive_full_tail',tail>0 and positive['tail_is_one_mass_for_any_joint_frequency_partition'])
  row=[up(sum((q*exp(Q(-m,2)) for m,q in pairs if lo<=m<=hi),ZERO)+tail*exp(Q(-lo,2))) for lo,hi in outputs]
  high=up(sum((q*exp(Q(-m,2)) for m,q in pairs if m>=M),ZERO)+tail*exp(Q(-M,2)))
  oldmid=up(sum((q*exp(Q(-m,2)) for m,q in pairs if 94<=m<M),ZERO)+tail*exp(-Q(94,2)))
  gate('same_R160_source_band_totals',oldmid==ex(original['complete_middle_source']) and high==ex(original['complete_infinite_high_source']))
  pure.append(row);purehigh.append(high)
  source_records.append(dict(block=j,source_pin=rec,shifted_sigma_min=pack(sig),fixed_LF_pair_caps=list(map(pack,lowcaps[j])),fixed_LF_mass=pack(C[j]),V_max=pack(V[j]),extra_source_width='1/2',complete_mean_zero_cap=positive['mean_zero_cap'],complete_inverse_leading=positive['inverse_leading_mass'],full_positive_inverse_tail=positive['shared_complete_inverse_tail'],window_source_masses=list(map(pack,row)),infinite_high_source=pack(high),source_polynomial_support=positive['support_max_mode']))
  print(json.dumps(dict(event='actual_missing_LF_window_source',block=j,tail_log2=float(arb(tail).log()/arb(2).log()))),flush=True);rss()
 source_rec=save(Path(str(a.out_prefix)+'-complete-source.json.gz'),dict(schema='same-R163-actual-LF-complete187-source-masses-v1',inputs=ids,source_sha256=sha(__file__),all_gates=True,windows=outputs,rows=source_records))
 del source_records,positive,pairs,block,lowsrc,highhead0,balanced,r160,old;gc.collect();rss()
 ctx.prec=256
 dq=[[] for j in range(25)];dqhigh=[[] for j in range(25)]
 correlations=[[exp(-2*k*sigma[j]) for k in MODES] for j in range(25)]
 # One common coefficient beyond1024 is larger than every actual weight
 # there. This is a stated positive coarsening, not a Fourier truncation.
 difference_weights=[]
 for j in range(25):
  far_weight=exp(-2048*sigma[j])
  difference_weights.append([(w,exp(-2*lo*sigma[j]) if lo<1024 else far_weight) for w,(lo,hi) in enumerate(windows)])
 for outindex,window in enumerate(outputs):
  geometry=dq_geometry(window,windows+[[M,M+90]])
  for j in range(25):
   coefficients=[];hc=ZERO;corr=correlations[j]
   for w,candidates in geometry:
    val=up(max(sum((alpha*lowcaps[j][k]*(corr[k] if branch else 1) for k,branch,alpha in terms),ZERO) for n,terms in candidates))
    if w==186:hc=val
    else:coefficients.append((w,val))
   dq[j].append(coefficients);dqhigh[j].append(hc)
  if outindex%20==0:print(json.dumps(dict(event='actual_full_LF_DQ_windows',output_window=outindex)),flush=True)
  rss()
 gate('actual_DQ_full_windows_and_high_boundary',all(len(dj)==187 and all(len(x)>0 for x in dj) for dj in dq))
 del geometry;gc.collect();rss()
 # These sets overinclude whole boundary windows, never partial mass without proof.
 sums=[];sumbig=[];vhtail=[]
 for lo,hi in outputs:
  sums.append([(w,Q(1)) for w,(l,u) in enumerate(windows) if l<=hi-94])
  sumbig.append([(w,Q(1)) for w,(l,u) in enumerate(windows) if l<=hi-94 and 2*u>=lo])
  vhtail.append([(w,Q(1)) for w,(l,u) in enumerate(windows) if u>=max(94,M-hi)])
 high_linear=[(w,Q(1)) for w,(lo,hi) in enumerate(windows) if hi>=M-92]
 high_square=[(w,Q(1)) for w,(lo,hi) in enumerate(windows) if 2*hi>=M]
 vh_factors=[[pack(arb(-2*max(94,M-hi)*sigma[j]).exp()) for lo,hi in outputs] for j in range(25)]
 hh_factors=[exp(-2*M*sigma[j]) for j in range(25)]
 states=[];history=[]
 for it in range(a.cycles):
  dom=[up((C[j]+r[j])*V[j]+h[j]*Hphys[j]) for j in range(25)]
  KT=[270*d for d in dom]
  gate('complete_whole_ball_R_le_1over128',all(0<q<Q(1,128) for q in dom),25)
  fsrc=[];csrc=[];ssrc=[];highsrc=[]
  for j in range(25):
   def su(coeff):return support(coeff,v[j],r[j],parent[j])
   t2=KT[j]*(C[j]*r[j]+r[j]*r[j]/2);tc=KT[j]*(C[j]+r[j])*h[j];ts=KT[j]*h[j]*h[j]/2
   qdiff=Q(5,4)*r[j]*su(difference_weights[j]);a2=[];ac=[];az=[]
   for w,(lo,hi) in enumerate(outputs):
    small=su(sums[w]);big=min(small,su(sumbig[w]));qsum=Q(23,9)*small*big
    vv=min(Q(23,18)*r[j]*r[j],qsum+qdiff)
    vh=Q(5,4)*ex(vh_factors[j][w])*su(vhtail[w])*h[j]
    hh0=Q(5,4)*hh_factors[j]*h[j]*h[j]
    a2.append(up(pure[j][w]+su(dq[j][w])+vv+t2))
    ac.append(up(dqhigh[j][w]*h[j]+vh+tc));az.append(up(hh0+ts))
   fsrc.append(a2);csrc.append(ac);ssrc.append(az)
   highsrc.append((up(purehigh[j]+Q(23,9)*C[j]*su(high_linear)+min(Q(23,18)*r[j]*r[j],Q(23,9)*r[j]*su(high_square))+t2),up((Q(23,9)+KT[j])*(C[j]+r[j])*h[j]),up((Q(23,18)+KT[j]/2)*h[j]*h[j])))
  images=[[ZERO]*187 for j in range(25)]
  for w in range(187):
   for i,(g,c,s) in enumerate(mats[w]):
    images[i][w]=up(gains[w][i]*headm[w]+sum((g[j]*fsrc[j][w]+c[j]*csrc[j][w]+s[j]*ssrc[j][w] for j in range(i+1)),ZERO))
  hi_image=[]
  for i in range(25):hi_image.append(up(hh[i]+sum((aa*highsrc[j][0]+bb*highsrc[j][1]+cc*highsrc[j][2] for j,(aa,bb,cc) in enumerate(highcoeff[i])),ZERO)))
  nv=[[min(v[j][w],images[j][w],r[j]) for w in range(186)] for j in range(25)]
  nr0=[min(r[j],sum(nv[j],ZERO)) for j in range(25)];nh=[min(h[j],hi_image[j]) for j in range(25)]
  np=[min(parent[j],images[j][186],nr0[j],nv[j][0]+nv[j][1]) for j in range(25)]
  nv=[[min(x,nr0[j],np[j] if w<2 else nr0[j]) for w,x in enumerate(row)] for j,row in enumerate(nv)]
  gate('finite_monotone_samefield_images',all(0<x<=y for row,prev in zip(nv,v) for x,y in zip(row,prev)) and all(0<x<=y for x,y in zip(nr0,r)) and all(0<x<=y for x,y in zip(nh,h)),25*188)
  record=dict(schema='same-R163-newwide186-actual-finite-posterior-state-v1',iteration=it+1,windows=windows,angular_weight_translation='2/5',fixed_LF_pair_caps=[[pack(x) for x in row] for row in lowcaps],finite_caps=list(map(pack,nr0)),high_caps=list(map(pack,nh)),window_caps=[[pack(x) for x in row] for row in nv],parent94_mass_caps=list(map(pack,np)),whole_ball_physical_domains=list(map(pack,dom)),complete_T_Hessian_by_block=list(map(pack,KT)),window_images=[[pack(x) for x in row] for row in images],high_images=list(map(pack,hi_image)),complete_source_material2=[[pack(x) for x in row] for row in fsrc],complete_source_cross=[[pack(x) for x in row] for row in csrc],complete_source_square=[[pack(x) for x in row] for row in ssrc],complete_high_source_materials=[[pack(x) for x in row] for row in highsrc],full_mean_inverse_and_positive_infinite_retained=True,same_existing_actual_R163_field=True)
  sr=save(Path(str(a.out_prefix)+f'-state{it+1:02d}.json.gz'),record);states.append(sr)
  hist=dict(iteration=it+1,finite24=pack(nr0[24]),high24=pack(nh[24]),near94_24=pack(nv[24][0]),near184_24=pack(nv[24][windows.index([184,184])]),source_T2_24=pack(KT[24]*(C[24]*r[24]+r[24]*r[24]/2)))
  history.append(hist);print(json.dumps(dict(event='actual_newwide186_posterior',iteration=it+1,r24=float(nr0[24]),h24=float(nh[24]),q94=float(nv[24][0]),q184=float(nv[24][windows.index([184,184])]))),flush=True)
  r,h,v,parent=nr0,nh,nv,np;del record;rss()
 final=dict(schema='same-R163-newwide186-complete-finite-posterior-v1',author='exact_closure (GPT-6 Astra Pro; AI-assisted)',source_sha256=sha(__file__),inputs=ids,input_manifest_sha256=sha(a.inputs),all_gates=all(gates.values()),gates=gates,gate_categories=counts,gate_count=sum(counts.values()),precision_bits=ctx.prec,complete_finite_source_precision_bits=512,parameter_domain=wide['parameter_domain'],actual_scope=wide['actual_scope'],angular_weight_translation='2/5',high_cutoff=M,difference_weight_saturation_mode=1024,comparison_partition=wide['comparison_partition'],windows=windows,complete_source_record=source_rec,state_records=states,history=history,finite_cycles=a.cycles,actual_low_new_width_caps=[[pack(x) for x in row] for row in lowcaps],finite_caps=list(map(pack,r)),high_caps=list(map(pack,h)),window_caps=[[pack(x) for x in row] for row in v],parent94_mass_caps=list(map(pack,parent)),same_existing_actual_R163_field=True,full_mean_inverse_and_positive_infinite_retained=True,all187_original_window_operators_retained=True,unknown_old_infinite_caps_reweighted=False,new_ODE_or_fixedpoint_claimed=False,no_new_ODE=True,elapsed_seconds=time.monotonic()-start,peak_rss_kib=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)
 rec=save(Path(str(a.out_prefix)+'-certificate.json.gz'),final);print(json.dumps(dict(all_gates=True,primary=rec,gate_count=final['gate_count'],elapsed_seconds=final['elapsed_seconds'],peak_rss_kib=final['peak_rss_kib'])),flush=True)
if __name__=='__main__':main()
