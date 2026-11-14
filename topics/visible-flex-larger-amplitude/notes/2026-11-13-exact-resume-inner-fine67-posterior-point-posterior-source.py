#!/usr/bin/env python3
"""Finite posterior for the already identified full inner field at tau+3/5.

The old53 parent masses remain joint constraints after splitting to67 windows.
DQ consumes them by exact fractional greedy support. Q is bounded by both
fine and parent positive convolutions. Complete mean, inverse, T, infinity,
and fixed intrinsic far graph are paid without new existence assumptions.
Author: exact_closure (GPT-6 Astra Pro; AI-assisted), 2026-11-13.
"""
from pathlib import Path
from fractions import Fraction as F
import argparse,gzip,hashlib,json,time,resource,gc,sys
from flint import arb,arb_mat,ctx
B=Path('/workspace/scratch/d1aa462cfc02');E=B/'exact-work';TOP=B/'math-research/topics/visible-flex-larger-amplitude'
PINS={
 'LF':(E/'inner-actual-LF-shift060-r1.json.gz','ff1df29ff5f24ffd6ed13dbc80c9f4a96d0e3084bacf03ebce41343d2d0ac811'),
 'LF_resource':(E/'inner-actual-LF-shift060-run1-resource.json','b9e95c4eb67cb109e50fc3b3b63be5b12871dfcff7f50ecacf31dde2e7b8ad83'),
 'source':(E/'inner-actual-LF-shift060-source-r1-summary.json','9f9ba881882e14f633a59fbd1111c7fd0ade9657fee36822f14ad8c495052b38'),
 'source_resource':(E/'inner-actual-LF-shift060-source-run1-resource.json','5a90ea604796167d473b2d2af72432f9f7bbfdb72150986fd859b89c4572da7e'),
 'existence':(E/'inner-actual-LF-shift060-conditional-existence-r1.json.gz','e793121cbc201297960a35bbaa427fe395fb17ba34c7dd96c8a02fd4a1fa4e66'),
 'existence_resource':(E/'inner-actual-LF-shift060-conditional-assemble-run1-resource.json','87cd7bd9719b20b64bae524a72fc9c9dd955c3f7ad0f962d31165c7f267098f9'),
 'identity':(E/'inner-actual-LF-shift060-samefield-r2.json.gz','f8563471233891b8edc6651b7eb375ad94d1c031ebf1a150325a11897e3db710'),
 'identity_resource':(E/'inner-actual-LF-comparison040-assemble-run2-resource.json','3ffd7eb5fba7c1624f800480070229fd033f3aaee75b822e52803414368f598d'),
 'density':(TOP/'notes/2026-11-12-tail-r42-strong-same-tau-r1-density.json.gz','e640e3e693ca198460de902fc8d9bb1bd909c2a7051ec099aa930a86789e0700'),
 'split':(TOP/'notes/2026-11-12-tail-r42-strong-same-tau-r1-split.json.gz','b31ba4868bf825fe19981af820f92d798161df027519992b9380a4b9f7f6b5dd'),
 'Gamma':(B/'geometry-work/inner-window-gamma-r1/output/certificate.json','3033c330ed219a1e87420818df8dd3d7bca44c246afe4f661d68870a783847b1'),
}
WIN=[[m,m] for m in range(94,185,2)]+[[186,192],[194,208],[210,224],[226,240],[242,256],[258,272],[274,288],[290,304],[306,320],[322,336],[338,352],[354,368],[370,384],[386,416],[418,448],[450,480],[482,512],[514,1024],[1026,2048],[2050,4096],[4098,8190]]
PARENT=[[m,m] for m in range(94,185,2)]+[[186,192],[194,256],[258,512],[514,1024],[1026,2048],[2050,4096],[4098,8190]]
GROUPS=[[j for j,(lo,hi) in enumerate(WIN) if pl<=lo<=hi<=ph] for pl,ph in PARENT]
PAR=[next(i for i,g in enumerate(GROUPS) if j in g) for j in range(67)]
def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def read(p):
 with (gzip.open(p,'rt') if str(p).endswith('.gz') else open(p)) as f:return json.load(f)
def ex(v):
 if isinstance(v,list):return F(int(v[0]))*F(2)**int(v[1])
 if 'upper' in v:return ex(v['upper'])
 if 'mantissa' in v:return F(int(v['mantissa']))*F(2)**int(v['binary_exponent'])
 return F(int(v['numerator']),int(v['denominator']))
def ab(v):
 if isinstance(v,arb):return v
 if isinstance(v,list):return arb(int(v[0]))*arb(2)**int(v[1])
 f=v if isinstance(v,F) else ex(v)
 return arb(f.numerator)/f.denominator
def pack(v,bits=160):
 if not v.is_finite():raise ArithmeticError('every_entry_finite')
 t=v.upper()
 if t<0:raise ArithmeticError('positive_cap')
 if t==0:return ['0',0]
 m,e=t.man_exp();m,e=int(m),int(e);s=max(0,m.bit_length()-bits)
 if s:m,e=(m+(1<<s)-1)>>s,e+s
 if not arb(m)*arb(2)**e>=t:raise ArithmeticError('outward_storage')
 return [str(m),e]
def up(v):return ab(pack(v))
def owned(r):return r['exitcode']==0 and r['termination_signal'] is None and r['peak_rss_kib']<98304 and r['resource_wrapper_sha256']=='bbf6c8ac8cb32cbc0f5c1e1c1c1e110ca1744c7839de0f272c172837a4ba3f59'
def save(p,d):
 if p.exists():raise FileExistsError('immutable fresh actual packet')
 raw=gzip.compress((json.dumps(d,separators=(',',':'))+'\n').encode(),mtime=0)
 if len(raw)>=5000000:raise ArithmeticError('split actual packet')
 p.write_bytes(raw);return dict(path=str(p),sha256=sha(p),bytes=len(raw))
def support(coeff,caps,mass):
 """Exact nonnegative box plus one joint mass support."""
 remain=mass;value=F(0)
 for c,x in sorted(zip(coeff,caps),key=lambda z:z[0],reverse=True):
  if remain<=0:break
  used=min(remain,x);value+=c*used;remain-=used
 return value
def specs(inputs,outputs):
 out=[]
 for i,(il,ih) in enumerate(inputs):
  for j in range(i,len(inputs)):
   jl,jh=inputs[j];sm=[w for w,(lo,hi) in enumerate(outputs) if max(il+jl,lo)<=min(ih+jh,hi)]
   df=[w for w,(lo,hi) in enumerate(outputs) if (i<j and max(jl-ih,lo)<=min(jh-il,hi)) or (i==j and ih-il>=lo)]
   out.append((i,j,sm,df,ih+jh>=8192))
 return out
FINE_SPECS=specs(WIN,WIN);PARENT_SPECS=specs(PARENT,WIN)
def qbounds(windows,pairs,x,tau,h):
 q=[arb(0) for _ in WIN];hq=arb(0);dec=[up((-2*lo*tau).exp()) for lo,_ in windows]
 for i,j,sm,df,tohigh in pairs:
  xy=x[i]*x[j];sv=arb(5)/(8 if i==j else 4)*xy
  for w in sm:q[w]+=sv
  if df:
   dv=arb(5)/4*dec[i]*xy
   for w in df:q[w]+=dv
  if tohigh:hq+=sv
 eh=up((-16384*tau).exp())
 for w,(_,whi) in enumerate(WIN):
  for i,(il,ih) in enumerate(windows):
   if ih>=8192-whi:q[w]+=arb(5)/4*up((-2*max(il,8192-whi)*tau).exp())*x[i]*h
  q[w]+=arb(5)/4*eh*h*h
 return list(map(up,q)),up(hq)
def main():
 ap=argparse.ArgumentParser(description=__doc__);ap.add_argument('--stage',choices=['init','sources','assemble'],required=True);ap.add_argument('--kernels',type=Path,required=True);ap.add_argument('--kernels-sha',required=True);ap.add_argument('--kernels-resource',type=Path,required=True);ap.add_argument('--state',type=Path);ap.add_argument('--state-sha');ap.add_argument('--state-resource',type=Path);ap.add_argument('--first-cell',type=int);ap.add_argument('--last-cell',type=int);ap.add_argument('--batch-manifest',type=Path);ap.add_argument('--out',type=Path,required=True);a=ap.parse_args()
 if a.out.exists():raise FileExistsError('fresh exact field posterior')
 ctx.prec,ctx.threads=256,1;start=time.monotonic();g={};counts={}
 def gate(k,v):
  if not v:raise ArithmeticError(k)
  g[k]=True;counts[k]=counts.get(k,0)+1
 def rss():gate('owned_RSS_below96MiB',resource.getrusage(resource.RUSAGE_SELF).ru_maxrss<98304)
 for k,(p,s) in PINS.items():gate('pin_'+k,sha(p)==s)
 for k in ('LF','source','existence','identity'):gate('owned_original_'+k,owned(read(PINS[k+'_resource'][0])))
 lf=read(PINS['LF'][0]);exist=read(PINS['existence'][0]);identity=read(PINS['identity'][0])
 gate('actual_same_complete_field_at060',lf['finite_LF_is_actual_projection_of_same_existing_field'] and lf['no_unknown_infinite_reweight'] and exist['new_conditional_nonlow_exists'] and identity['lower_width_same_field_identified'] and identity['fixed_far_graph_restriction_is_same_intrinsic_R18_map'] and exist['domain']==identity['domain']==lf['domain'] and ex(lf['angular_weight_translation'])==F(3,5))
 gate('actual_full_original_gates',all(d['all_gates'] and all(d['gates'].values()) for d in (lf,exist,identity)))
 gate('new_kernel_pin_owned',sha(a.kernels)==a.kernels_sha and owned(read(a.kernels_resource)));kernel=read(a.kernels)
 gate('all_actual_new_DQ',kernel['all_gates'] and all(kernel['gates'].values()) and kernel['all213_source_cells'] and kernel['windows_out']==WIN and kernel['windows_in']==WIN+[[8192,None]] and kernel['input_identities']['modal']['sha256']==PINS['LF'][1] and kernel['domain']==lf['domain'])
 inputids={k:dict(path=str(p),sha256=s) for k,(p,s) in PINS.items()};inputids['fine67_kernels']=dict(path=str(a.kernels),sha256=a.kernels_sha,resource_path=str(a.kernels_resource),resource_sha256=sha(a.kernels_resource))
 gate('exact_full_partition',len(WIN)==67 and len(PARENT)==53 and sum((list(range(lo,hi+1,2)) for lo,hi in WIN),[])==list(range(94,8191,2)) and all(GROUPS))
 if a.stage=='init':
  gate('same_original_existence_partition',exist['windows']==PARENT)
  rows=[]
  for row in exist['rows']:
   pc=row['radius'];fc=[pc[PAR[w]] for w in range(67)]
   rows.append(dict(cell=row['cell'],window_caps=fc,parent_common_caps=pc))
  out=dict(schema='same-actual-LF-shift060-fine67-posterior-v1',stage='init',round=0,rows=rows,infinite_cap=exist['infinite_radius'],all_existing_original_parent_constraints_kept=True)
 else:
  gate('actual_preceding_state_pin',a.state is not None and a.state_resource is not None and sha(a.state)==a.state_sha and owned(read(a.state_resource)))
  state=read(a.state);gate('same_field_preceding_actual_state',state['schema']=='same-actual-LF-shift060-fine67-posterior-v1' and state['all_gates'] and all(state['gates'].values()) and state['same_original_full_field_identified'] and state['windows']==WIN and state['parent_windows']==PARENT and state['domain']==lf['domain'] and state['source_sha256']==sha(__file__) and state['input_identities']==inputids)
  inputstate=dict(path=str(a.state),sha256=a.state_sha,resource_path=str(a.state_resource),resource_sha256=sha(a.state_resource),round=state['round'])
  R=[[ab(v) for v in row['window_caps']] for row in state['rows']];M=[[ab(v) for v in row['parent_common_caps']] for row in state['rows']];h=ab(state['infinite_cap'])
  gate('all_original_cells_of_state',[r['cell'] for r in state['rows']]==list(range(12,225)) and len(R)==len(M)==213 and all(len(v)==67 for v in R) and all(len(v)==53 for v in M))
  for n in range(213):
   for w in range(67):gate('fine_cap_below_parent',R[n][w]<=M[n][PAR[w]])
  C=[ab(row['finite_LF_common_cap']) for row in lf['rows']];aa=[ab(row['physical_Amax']) for row in lf['rows']];tau=[ab(row['translated_tau_outer_lower']) for row in lf['rows']]
  del identity,exist;gc.collect();rss()
  if a.stage=='sources':
   gate('declared_source_range',a.first_cell is not None and a.last_cell is not None and 12<=a.first_cell<=a.last_cell<=224)
   src=read(PINS['source'][0]);gate('complete_source_identity',src['all_gates'] and src['all213_original_cells'] and src['gates']['complete_mean_inverse_zero_mode_and_positive_tail'] and src['input_hashes'][str(PINS['LF'][0])]==PINS['LF'][1])
   qref=[[arb(0) for _ in WIN] for _ in range(213)];which={m:w for w,(lo,hi) in enumerate(WIN) for m in range(lo,hi+1,2)};seen=0
   for part in src['source_parts']:
    p=Path(part['path']);gate('complete_source_chunk_pin',sha(p)==part['sha256'])
    with gzip.open(p,'rt') as stream:
     for line in stream:
      row=json.loads(line);n=row['cell']-12;gate('complete_source_order',n==seen and row['complete_mean_and_inverse_retained'] and row['polynomial_support_max736']);seen+=1
      for pair in row['high_polynomial_pair_rows']:qref[n][which[pair['mode']]]+=ab(pair['common_d'])
   gate('all213_reference_sources',seen==213)
   qhi=[]
   for n,row in enumerate(src['rows']):
    tail=ab(row['source_common_mass']['common_d']['shared_complete_inverse_tail']);qhi.append(ab(row['source_common_mass']['common_d']['infinite8192up']))
    for w in range(67):qref[n][w]=min(up(qref[n][w]+tail),ab(row['source_common_mass']['common_d']['near94to184' if w<46 else 'rest186to8190']))
   rows=[];chunks=[]
   for cell in range(a.first_cell,a.last_cell+1):
    n=cell-12;cr=kernel['chunk_records'][n];p=Path(cr['path']);gate('actual_DQ_chunk_pin',cr['cell']==cell and sha(p)==cr['sha256']);dr=read(p);chunks.append(cr)
    gate('same_fixed_actual_LF',dr['reference_common_cap']==lf['rows'][n]['finite_LF_common_cap'] and dr['reference_strong_pair_caps']==lf['rows'][n]['finite_LF_pair_caps'])
    caps=[ex(v) for v in state['rows'][n]['window_caps']];mass=[ex(v) for v in state['rows'][n]['parent_common_caps']];hf=ex(state['infinite_cap']);lin=[]
    for ks,ke in zip(dr['kernels_s_upper'],dr['kernels_ell_upper']):
     coeff=list(map(ex,ks));gate('complete_DQ_entry_majorant',len(coeff)==68 and all(c>=ex(e) for c,e in zip(coeff,ke)))
     value=coeff[-1]*hf
     for pi,js in enumerate(GROUPS):value+=support([coeff[j] for j in js],[caps[j] for j in js],mass[pi])
     lin.append(up(ab(value)))
    t=up(sum(M[n],arb(0))+h);physical=up(aa[n]*(C[n]+t));gate('whole_actual_domain_complete_mean_inverse',physical<arb(1)/128)
    fineq,finehi=qbounds(WIN,FINE_SPECS,R[n],tau[n],h);parentq,parenthi=qbounds(PARENT,PARENT_SPECS,M[n],tau[n],h)
    sq=[min(x,y) for x,y in zip(fineq,parentq)];mixedhi=up(arb(23)/9*sum(M[n],arb(0))*h+arb(23)/18*h*h);hiQ=up(min(finehi,parenthi)+mixedhi)
    rem=up(270*aa[n]*(C[n]+t)*(C[n]*t+t*t/2));insDQ=up(arb(23)/9*C[n]*(M[n][-1]+h));ins=up(qhi[n]+insDQ+hiQ+rem)
    ss=[up(qref[n][w]+lin[w]+sq[w]+rem) for w in range(67)]
    for v in ss+[ins]:gate('every_complete_source_finite_positive',v.is_finite() and v>0)
    rows.append(dict(cell=cell,source=list(map(pack,ss)),constant_source=list(map(pack,qref[n])),DQ_joint_support_source=list(map(pack,lin)),Q_fine_source=list(map(pack,fineq)),Q_parent_source=list(map(pack,parentq)),Q_chosen_source=list(map(pack,sq)),complete_T_source=pack(rem),infinite_source=pack(ins),infinite_parts=dict(constant=pack(qhi[n]),DQ=pack(insDQ),Q=pack(hiQ),complete_T=pack(rem)),total_nonlow_common=pack(t),whole_actual_physical_domain=pack(physical)))
    rss()
    if len(rows)%12==0 or cell==a.last_cell:print(json.dumps(dict(event='actual_fine67_source',cell=cell,round=state['round']+1,elapsed_seconds=time.monotonic()-start,peak_rss_kib=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)),flush=True)
   out=dict(schema='same-actual-LF-shift060-fine67-posterior-source-batch-v1',stage='sources',round=state['round']+1,preceding_state=inputstate,first_cell=a.first_cell,last_cell=a.last_cell,rows=rows,DQ_chunks=chunks,reference_source_parts=src['source_parts'],original_parent_constraints_consumed_by_exact_support=True,Q_two_complete_majorants_intersected=True)
  else:
   gate('actual_source_manifest_given',a.batch_manifest is not None);bm=read(a.batch_manifest);s=arb_mat(213,67);ins=[];physical=[];expected=12;batches=[]
   for br in bm['batches']:
    p=Path(br['path']);rp=Path(br['resource_path']);gate('actual_batch_pins_owned',sha(p)==br['sha256'] and sha(rp)==br['resource_sha256'] and owned(read(rp)));bd=read(p)
    gate('same_source_batch_state',bd['schema']=='same-actual-LF-shift060-fine67-posterior-source-batch-v1' and bd['source_sha256']==sha(__file__) and bd['all_gates'] and all(bd['gates'].values()) and bd['preceding_state']==inputstate and bd['input_identities']==inputids and bd['first_cell']==expected);batches.append(br)
    for row in bd['rows']:
     gate('all_source_cells_in_order',row['cell']==expected);n=expected-12;expected+=1
     for w in range(67):s[n,w]=ab(row['source'][w])
     ins.append(ab(row['infinite_source']));physical.append(ab(row['whole_actual_physical_domain']))
    del bd;gc.collect();rss()
   gate('complete213_sources',expected==225 and len(ins)==213)
   gamma=read(PINS['Gamma'][0]);gate('original_complete_Green',gamma['original_maximum_bitwise_identity'] and gamma['original_complete_far_and_pure_identity'] and gamma['new_ODE_integrations']==0 and gamma['Vprime_scale']==[257,256])
   image=arb_mat(213,67);covered=[];gpins=[]
   for ix,gr in enumerate(gamma['files']):
    p=PINS['Gamma'][0].parent/gr['path'];gate('Green_chunk_pin',sha(p)==gr['sha256']);gg=read(p);matrix=arb_mat(213,213);visited=set()
    for k,n,m,e in gg['entries']:
     gate('all_causal_vertices',12<=k<=n<=224 and (k,n) not in visited);visited.add((k,n));matrix[k-12,n-12]=ab([m,e])
    gate('complete_causal_triangle',len(visited)==22791);ixs=[w for w,(lo,hi) in enumerate(WIN) if gr['first_mode']<=lo<=hi<=gr['last_mode']];covered+=ixs
    ss=arb_mat([[s[n,w] for w in ixs] for n in range(213)]);pp=matrix*ss
    for j,w in enumerate(ixs):
     for n in range(213):image[n,w]=pp[n,j]
    gpins.append(dict(path=str(p),sha256=gr['sha256']));del gg,matrix,ss,pp,visited;gc.collect();rss();print(json.dumps(dict(event='actual_fine67_Green',window=ix,round=state['round']+1,elapsed_seconds=time.monotonic()-start)),flush=True)
   gate('all67_Green_windows',sorted(covered)==list(range(67)))
   sys.path.insert(0,str(TOP/'computations'));from closure_split_joint_io_v2 import metadata_without_array
   sp=metadata_without_array(PINS['split'][0],'gamma_rows');density=read(PINS['density'][0]);gi=up(arb(257)/256*ab(density['gamma_high']));z=ab(lf['fixed_far_parameter']['new_actual_upper']);zdom=ab(lf['fixed_far_parameter']['evaluation_graph_domain']);gate('same_actual_intrinsic_far_graph_domain',z<zdom/4 and 2*zdom<arb(2)**-1948 and lf['fixed_far_parameter']['finite46_only'] and lf['fixed_far_parameter']['unknown_graph_output_not_reweighted'])
   far_ratio=up((z/(arb(2)**-2200))**2/(arb(257)/256));himage=up(gi*sum(ins,arb(0))+ab(sp['deep_high_boundary'])*far_ratio);newh=min(h,himage)
   rows=[];improved=0
   for n,row in enumerate(sp['cells']):
    im=[];caps=[]
    for w in range(67):
     v=up(image[n,w]+ab(row['far_boundary_near' if w<46 else 'far_boundary_rest'])*far_ratio);gate('every_actual_image_finite_positive',v.is_finite() and v>0);im.append(v);caps.append(min(R[n][w],v))
    parent=[min(M[n][p],up(sum((caps[w] for w in js),arb(0)))) for p,js in enumerate(GROUPS)]
    caps=[min(v,parent[PAR[w]]) for w,v in enumerate(caps)]
    for w,v in enumerate(caps):gate('finite_posterior_only_decreases',0<v<=R[n][w] and v<=parent[PAR[w]]);improved+=int(v<R[n][w])
    for p,v in enumerate(parent):gate('shared_parent_mass_only_decreases',0<v<=M[n][p])
    rows.append(dict(cell=n+12,window_caps=list(map(pack,caps)),parent_common_caps=list(map(pack,parent)),complete_image=list(map(pack,im)),whole_actual_physical_domain=pack(physical[n])))
   gate('infinite_posterior_only_decreases',0<newh<=h)
   out=dict(schema='same-actual-LF-shift060-fine67-posterior-v1',stage='assemble',round=state['round']+1,preceding_state=inputstate,source_batches=batches,batch_manifest=dict(path=str(a.batch_manifest),sha256=sha(a.batch_manifest)),Green_chunks=gpins,rows=rows,infinite_cap=pack(newh),complete_infinite_image=pack(himage),infinite_Green_gain=pack(gi),actual_far_forcing_ratio=pack(far_ratio),improved_finite_components=improved,all_existing_original_parent_constraints_kept=True)
 rss();out.update(author='exact_closure (GPT-6 Astra Pro; AI-assisted)',source_sha256=sha(__file__),all_gates=True,gates=g,gate_categories=counts,gate_count=sum(counts.values()),input_identities=inputids,domain=lf['domain'],angular_weight_translation=lf['angular_weight_translation'],windows=WIN,parent_windows=PARENT,child_to_parent=PAR,parent_groups=GROUPS,same_original_full_field_identified=True,actual_LF_is_low_projection_not_auxiliary=True,actual_LF_and_same_intrinsic_far_parameter_fixed=True,complete_mean_inverse_Q_T_and_infinite=True,unknown_infinite_never_reweighted=True,finite_min_induction_only=True,new_fixedpoint_not_claimed=True,original_existence_radii_not_relabelled=True,no_new_ODE_Green_or_integral=True,precision_bits=256,storage_bits=160,elapsed_seconds=time.monotonic()-start,peak_rss_kib=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)
 rec=save(a.out,out);print(json.dumps(dict(all_gates=True,packet=rec,stage=a.stage,round=out['round'],gate_count=out['gate_count'],elapsed_seconds=out['elapsed_seconds'],peak_rss_kib=out['peak_rss_kib'])),flush=True)
if __name__=='__main__':main()
