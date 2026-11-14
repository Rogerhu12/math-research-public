#!/usr/bin/env python3
"""True node12 two-material point readout of the same full P1 field at tau+3/5.

Uses all original cell12 panels, exact parent-mass support, and complete
finite reference/inverse/Q/T source budgets. Shared source tails are paid
once after the point columns are combined. No fresh existence or ODE.
Author: exact_closure (GPT-6 Astra Pro; AI-assisted), 2026-11-13.
"""
import argparse,gzip,hashlib,importlib.util,json,resource,time
from pathlib import Path
from fractions import Fraction as F
from flint import arb,ctx
E=Path('/workspace/scratch/d1aa462cfc02/exact-work')
HELP=E/'2026-11-13-exact-resume-inner-actual-LF-shift060-fine67-posterior-v1.py'
HELP_SHA='82191d1119c36e1e731ab9ae76a01d8b32008b26bcd165b99e7eb203ac5efaf0'
PINS={
 'scalar':(E/'inner-cut-endpoint-high-r1.json','8f90a5b5e617c3059736d4b80ba0008f456ad7412e2e9bf9159049ebd873e716'),
 'scalar_resource':(E/'inner-cut-endpoint-high-r1-resource.json','73eb11617c48a86c16b20161f8777b96119c2f958a5f2bcf7b33d050a84bc7f3'),
 'aggregate':(E/'inner-fine67-kernel-aggregate-r3.json.gz','696014d943e1269c6de15c62728990e9165bc2199fdaac17a91de5887a407704'),
 'aggregate_resource':(E/'inner-fine67-kernel-aggregate-r3-resource.json','ee84b84a3bc1660b523347b30e80f468403df3a9e9d48bd937ff745e9aaad709'),
 'near':(E/'inner-cell12-logr-singleton-normalized-r1.json','4b0f610c31dd332c54ebaebe50400a5c4303bbbc0f2bdcbd82fbbd581cdda2be'),
 'near_resource':(E/'inner-cell12-logr-normalization-run1-resource.json','4a4023b4f49b53d9febe4a1c12f6e2ac67111996e09d19a223aff012bf1800fc'),
 'old_point':(E/'inner-fine53-logr-point-r1.json','1905c047655b246283c3374eff763566c8e707e5bd5fc084b480e5d2dc0b2f69'),
 'old_point_resource':(E/'inner-fine53-logr-point-run1-resource.json','12a2c1e7084b62d7b2ac1fe59a4624c027055cfc6df76bf59a2a6e513b238672'),
 'coarse_export':(E/'inner-actual-LF-shift060-head-export-r2.json','856c7580a184779cbf771d989f73a9d0d860d2e24591adbcf6dc241199d5ba5d'),
}
def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def read(p):
 with (gzip.open(p,'rt') if str(p).endswith('.gz') else open(p)) as f:return json.load(f)
def main():
 ap=argparse.ArgumentParser(description=__doc__);ap.add_argument('--state',type=Path,required=True);ap.add_argument('--state-sha',required=True);ap.add_argument('--state-resource',type=Path,required=True);ap.add_argument('--out',type=Path,required=True);a=ap.parse_args()
 if a.out.exists():raise FileExistsError('fresh point certificate')
 start=time.monotonic();ctx.prec,ctx.threads=256,1;g={};cnt={}
 def gate(k,v):
  if not v:raise ArithmeticError(k)
  g[k]=True;cnt[k]=cnt.get(k,0)+1
 gate('original_posterior_source_pin',sha(HELP)==HELP_SHA);spec=importlib.util.spec_from_file_location('fine67_posterior_formula',HELP);p=importlib.util.module_from_spec(spec);spec.loader.exec_module(p)
 ab,ex,pack,up,support=p.ab,p.ex,p.pack,p.up,p.support;WIN,PARENT,GROUPS,PAR=p.WIN,p.PARENT,p.GROUPS,p.PAR
 for k,(path,pin) in PINS.items():gate('pin_'+k,sha(path)==pin)
 for k in ('aggregate','near','old_point','scalar'):gate('owned_'+k,p.owned(read(PINS[k+'_resource'][0])))
 gate('actual_input_state_pin_owned',sha(a.state)==a.state_sha and p.owned(read(a.state_resource)));state=read(a.state)
 gate('same_actual_identified_field',state['all_gates'] and all(state['gates'].values()) and state['same_original_full_field_identified'] and state['source_sha256']==HELP_SHA and state['windows']==WIN and state['parent_windows']==PARENT and ex(state['angular_weight_translation'])==F(3,5))
 agg,near,old,export=(read(PINS[k][0]) for k in ('aggregate','near','old_point','coarse_export'))
 gate('all_original_readout_gates',agg['all_gates'] and near['all_gates'] and old['all_gates'] and export['all_gates'] and export['same_original_full_field_identified'] and agg['domain']==state['domain']==export['domain'])
 lfpath,lfpin=p.PINS['LF'];srcpath,srcpin=p.PINS['source'];gate('same_actual_LF_source_pins',sha(lfpath)==lfpin and sha(srcpath)==srcpin);lf,src=read(lfpath),read(srcpath)
 gate('full_LF_complete_mean_inverse_identity',lf['finite_LF_is_actual_projection_of_same_existing_field'] and lf['domain']==state['domain'] and src['input_hashes'][str(lfpath)]==lfpin and src['gates']['complete_mean_inverse_zero_mode_and_positive_tail'])
 h=ab(state['infinite_cap']);R=[[ab(x) for x in row['window_caps']] for row in state['rows'][:2]];M=[[ab(x) for x in row['parent_common_caps']] for row in state['rows'][:2]]
 rf=[[ex(x) for x in row['window_caps']] for row in state['rows'][:2]];mf=[[ex(x) for x in row['parent_common_caps']] for row in state['rows'][:2]];hf=ex(state['infinite_cap'])
 C=ab(lf['rows'][0]['finite_LF_common_cap']);aa=ab(lf['rows'][0]['physical_Amax']);tau=ab(lf['rows'][0]['translated_tau_outer_lower']);t=up(sum(M[0],arb(0))+h);physical=up(aa*(C+t));gate('entire_actual_complete_mean_inverse_domain',physical<arb(1)/128)
 rem=up(270*aa*(C+t)*(C*t+t*t/2));eps=ab(export['point_physical_epsilon_prime'])
 gate('same_original_point_units',export['same_original617_units']['sha256']=='617987048c3a599acb42bcafe8dba99155c5cde82d252706769d5e24340ce1b9' and ex(agg['endpoint_metadata']['output_strip_original'])==ex(export['head_strip']))
 scalar=read(PINS['scalar'][0]);gate('original_scalar_kernels_same_units',scalar['all_gates'] and all(scalar['gates'].values()) and ex(scalar['head_strip'])==ex(export['head_strip']) and scalar['input_identities']['density']['sha256']==p.PINS['density'][1] and scalar['no_new_ODE_or_radial_quadrature'])
 kernelrows=near['rows']+agg['endpoint_rows'];gate('exact63_covered_logr_windows',len(kernelrows)==63 and [r['window'] for r in kernelrows]==WIN[:63])
 H=[];Ks=[];Ke=[];kernel_choices=[]
 for w,(lo,hi) in enumerate(WIN):
  srk=next(r for r in scalar['rows'] if r['window'][0]<=lo<=hi<=r['window'][1]);hh=ab(srk['initial_true_cell13_to_cut']);gs=ab(srk['source_two_material_to_cut']['d1']);ge=ab(srk['source_two_material_to_cut']['d_lambda'])
  if w<63:
   rk=kernelrows[w];hh=min(hh,ab(rk['chosen_input_nextcell_Vprime_mass_to_cut']));gs=min(gs,ab(rk['chosen_source_two_material_to_cut']['d1']));ge=min(ge,ab(rk['chosen_source_two_material_to_cut']['d_lambda']))
  H.append(hh);Ks.append(gs);Ke.append(ge);kernel_choices.append(dict(window=WIN[w],scalar_parent_window=srk['window'],logr_available=w<63,H=pack(hh),Ks=pack(gs),Kell=pack(ge)))
 G=[up(x+y) for x,y in zip(Ks,Ke)]
 cr=agg['chunk_records'][0];gate('actual_cell12_DQ_pin',cr['cell']==12 and sha(cr['path'])==cr['sha256']);dq=read(cr['path']);ks=[[ab(v) for v in row] for row in dq['kernels_s_upper']];ke=[[ab(v) for v in row] for row in dq['kernels_ell_upper']];Bfloor=dq['B_floor']
 gate('positive_actual_Bfloor',Bfloor>=120)
 for rs,re in zip(dq['kernels_s_upper'],dq['kernels_ell_upper']):gate('same_coefficient_common_majorant',all(ex(z)>=ex(e) for z,e in zip(rs,re)))
 gate('same_cell12_reference_LF',dq['reference_strong_pair_caps']==lf['rows'][0]['finite_LF_pair_caps'] and dq['reference_common_cap']==lf['rows'][0]['finite_LF_common_cap'])
 part=src['source_parts'][0];gate('full_reference_cell12_part_pin',sha(part['path'])==part['sha256'])
 with gzip.open(part['path'],'rt') as f:sr=json.loads(next(f))
 gate('full_reference_cell12',sr['cell']==12 and sr['complete_mean_and_inverse_retained'] and sr['polynomial_support_max736'])
 tails={k:ab(src['rows'][0]['source_common_mass'][k]['shared_complete_inverse_tail']) for k in ('d1','d_lambda','common_d')}
 qrefS=[arb(0) for _ in WIN];qrefE=[arb(0) for _ in WIN];qrefC=[arb(0) for _ in WIN];which={m:w for w,(lo,hi) in enumerate(WIN) for m in range(lo,hi+1,2)}
 for row in sr['high_polynomial_pair_rows']:
  w=which[row['mode']];qrefS[w]+=ab(row['d1']);qrefE[w]+=ab(row['d_lambda']);qrefC[w]+=ab(row['common_d'])
 qrefS,qrefE,qrefC=([up(v) for v in x] for x in (qrefS,qrefE,qrefC))
 def joint(coeff,cells):
  value=F(0)
  for pi,js in enumerate(GROUPS):value+=support([ex(pack(coeff[j])) for j in js],[rf[cells][j] for j in js],mf[cells][pi])
  return up(ab(value))
 DQs=[up(joint(row[:-1],0)+row[-1]*h) for row in ks];DQe=[up(joint(row[:-1],0)+row[-1]*h) for row in ke]
 def beta(w1,w2):
  kl,kh=w1;nl,nh=w2;kr=F(1) if kh is None else F(kh,1+kh);nr=F(1) if nh is None else F(nh,1+nh)
  bs=F(5,4)*kr*nr;e0=F(1,(1+kl)*(1+nl));e1=F(5,4*Bfloor)*kr/F(1+nl);e2=F(5,4*Bfloor)*nr/F(1+kl)
  e3=F(5,4*Bfloor*Bfloor)*kr*nr
  if kh is not None and nh is not None:e3+=F(1,4*Bfloor*Bfloor*(1+kh)*(1+nh))
  be=max(e0,e1,e2,e3);gate('complete_two_material_corner_bound',0<be<=bs<=F(5,4));return ab(bs),ab(be)
 def vectorQ(inputs,pairs,x):
  qs=[arb(0) for _ in WIN];qe=[arb(0) for _ in WIN];dec=[up((-2*lo*tau).exp()) for lo,_ in inputs]
  for i,j,sm,df,_ in pairs:
   bs,be=beta(inputs[i],inputs[j]);xy=x[i]*x[j];half=arb(1)/2 if i==j else arb(1)
   for w in sm:qs[w]+=half*bs*xy;qe[w]+=half*be*xy
   for w in df:qs[w]+=bs*dec[i]*xy;qe[w]+=be*dec[i]*xy
  bsH,beH=beta([8192,None],[8192,None]);deH=up((-16384*tau).exp())
  for w,(_,hi) in enumerate(WIN):
   for i,(il,ih) in enumerate(inputs):
    if ih>=8192-hi:
     bs,be=beta(inputs[i],[8192,None]);xy=up((-2*max(il,8192-hi)*tau).exp())*x[i]*h;qs[w]+=bs*xy;qe[w]+=be*xy
   qs[w]+=bsH*deH*h*h;qe[w]+=beH*deH*h*h
  return list(map(up,qs)),list(map(up,qe))
 fineS,fineE=vectorQ(WIN,p.FINE_SPECS,R[0]);parentS,parentE=vectorQ(PARENT,p.PARENT_SPECS,M[0])
 # Existing finite point masses can be raised in width; no infinite mass is.
 oldrows=old.get('rows',[])
 oldcaps=old.get('translated_head_window_masses')
 if oldcaps is None:
  oldcaps=[row['chosen'] if 'chosen' in row else row['chosen_point_head'] for row in oldrows]
 gate('complete_old53_finite_point_partition',len(oldcaps)==53 and old.get('windows',PARENT)==PARENT)
 fallback_parent=[min(up(eps*M[0][j]),up(ab(oldcaps[j])*(arb(PARENT[j][1])/5).exp())) for j in range(53)]
 fallback=[min(up(eps*R[0][w]),fallback_parent[PAR[w]]) for w in range(67)]
 raw=[];chosen=[];details=[]
 for w in range(67):
  inc=up(H[w]*R[1][w]);ref=up(Ks[w]*qrefS[w]+Ke[w]*qrefE[w]+min(Ks[w]*tails['d1']+Ke[w]*tails['d_lambda'],G[w]*tails['common_d']));dl=up(Ks[w]*DQs[w]+Ke[w]*DQe[w]);qq=up(min(Ks[w]*fineS[w]+Ke[w]*fineE[w],Ks[w]*parentS[w]+Ke[w]*parentE[w]));tt=up(G[w]*rem);value=up(inc+ref+dl+qq+tt)
  chosen.append(min(value,fallback[w]));raw.append(value);details.append(dict(window=WIN[w],point_kernel_available=True,incoming=pack(inc),full_reference=pack(ref),DQ=pack(dl),Q=pack(qq),complete_T=pack(tt),point_candidate=pack(value),known_whole_or_finite_point=pack(fallback[w]),chosen=pack(chosen[-1]),kernel_choice=kernel_choices[w]))
 def weightedQ(inputs,pairs,x,ws,we):
  v=arb(0);dec=[up((-2*lo*tau).exp()) for lo,_ in inputs]
  for i,j,sm,df,_ in pairs:
   bs,be=beta(inputs[i],inputs[j]);xy=x[i]*x[j]
   if sm:v+=(arb(1)/2 if i==j else arb(1))*xy*max(up(ws[w]*bs+we[w]*be) for w in sm)
   if df:v+=dec[i]*xy*max(up(ws[w]*bs+we[w]*be) for w in df)
  for i,(il,ih) in enumerate(inputs):
   bs,be=beta(inputs[i],[8192,None]);coeff=arb(0)
   for w,(_,hi) in enumerate(WIN):
    if (ws[w]>0 or we[w]>0) and ih>=8192-hi:coeff=max(coeff,up((ws[w]*bs+we[w]*be)*(-2*max(il,8192-hi)*tau).exp()))
   v+=coeff*x[i]*h
  bs,be=beta([8192,None],[8192,None]);v+=up((-16384*tau).exp())*h*h*max(up(ws[w]*bs+we[w]*be) for w in range(67))
  return up(v)
 bands=[];bandparts=[]
 for indices in (list(range(46)),list(range(46,67))):
  selected=[w for w in indices if raw[w]<fallback[w]]
  ws=[Ks[w] if w in selected else arb(0) for w in range(67)];we=[Ke[w] if w in selected else arb(0) for w in range(67)];wg=[up(x+y) for x,y in zip(ws,we)];wh=[H[w] if w in selected else arb(0) for w in range(67)];maxg=max(wg)
  incoming=joint(wh,1);refpoly=up(sum((ws[w]*qrefS[w]+we[w]*qrefE[w] for w in selected),arb(0)));reftail=min(up(max(ws)*tails['d1']+max(we)*tails['d_lambda']),up(maxg*tails['common_d']));reference=up(refpoly+reftail)
  dcoef=[up(sum((ws[w]*ks[w][j]+we[w]*ke[w][j] for w in selected),arb(0))) for j in range(68)];dsource=up(joint(dcoef[:-1],0)+dcoef[-1]*h)
  qfine=weightedQ(WIN,p.FINE_SPECS,R[0],ws,we);qparent=weightedQ(PARENT,p.PARENT_SPECS,M[0],ws,we);qchosen=min(qfine,qparent);tsource=up(maxg*rem)
  outside=arb(0)
  for pi,js in enumerate(GROUPS):outside+=min(fallback_parent[pi],up(sum((fallback[w] for w in js if w in indices and w not in selected),arb(0))))
  aggregate=up(incoming+reference+dsource+qchosen+tsource+outside);separate=up(sum((chosen[w] for w in indices),arb(0)));whole=up(sum((fallback_parent[pi] for pi,js in enumerate(GROUPS) if js[0] in indices),arb(0)))
  value=min(aggregate,separate,whole);bands.append(value);bandparts.append(dict(selected_point_windows=[WIN[w] for w in selected],incoming_joint=pack(incoming),complete_reference_joint=pack(reference),reference_polynomial_joint=pack(refpoly),reference_inverse_tail_joint=pack(reftail),DQ_joint=pack(dsource),Q_fine_joint=pack(qfine),Q_parent_joint=pack(qparent),Q_chosen_joint=pack(qchosen),complete_T_joint=pack(tsource),remaining_known_point_mass=pack(outside),aggregate_candidate=pack(aggregate),separate_window_candidate=pack(separate),known_parent_candidate=pack(whole),chosen=pack(value),shared_reference_inverse_tail_paid_once=True,shared_T_paid_once=True,two_materials_combined_before_frequency_maximum=True))
 bands.append(up(eps*h));gate('all_actual_head_masses_positive_finite',all(v.is_finite() and v>0 for v in bands))
 original=[];at040=[]
 for band,lo,indices in zip(bands,[94,186,8192],[list(range(46)),list(range(46,67)),[]]):
  for dest,drop in ((original,F(3,5)),(at040,F(1,5))):
   value=up(band*(-lo*ab(drop)).exp())
   if indices:value=min(value,up(sum((chosen[w]*(-WIN[w][0]*ab(drop)).exp() for w in indices),arb(0))))
   dest.append(pack(value))
 gate('owned_RSS_below96MiB',resource.getrusage(resource.RUSAGE_SELF).ru_maxrss<98304)
 out=dict(schema='same-P1-shift060-fine67-two-material-true-point-head-v2',author='exact_closure (GPT-6 Astra Pro; AI-assisted)',source_sha256=sha(__file__),all_gates=True,gates=g,gate_categories=cnt,gate_count=sum(cnt.values()),input_identities={k:dict(path=str(path),sha256=pin) for k,(path,pin) in PINS.items()},posterior_formula=dict(path=str(HELP),sha256=HELP_SHA),state=dict(path=str(a.state),sha256=a.state_sha,resource_path=str(a.state_resource),resource_sha256=sha(a.state_resource),round=state['round']),actual_LF=dict(path=str(lfpath),sha256=lfpin),complete_reference_source=dict(path=str(srcpath),sha256=srcpin,cell12_part=part),DQ_chunk=cr,domain=state['domain'],angular_weight_translation=state['angular_weight_translation'],head_strip=export['head_strip'],translated_head_strip=export['translated_head_strip'],head_bands=export['head_bands'],same_original617_units=export['same_original617_units'],readout_position=export['readout_position'],point_physical_epsilon_prime=export['point_physical_epsilon_prime'],windows=WIN,parent_windows=PARENT,parent_point_caps=list(map(pack,fallback_parent)),translated_head_window_masses=list(map(pack,chosen)),translated_head_band_masses=list(map(pack,bands)),actual_R100_head_band_masses=original,head_at040_band_masses=at040,rows=details,band_parts=bandparts,complete_mean_inverse_far=True,complete_infinite_repaid=True,all_Q_two_material_corners_and_infinite_limits_paid=True,same_original_full_field_identified=True,finite_old_point_only_reweighted=True,old_infinite_never_reweighted=True,intrinsic_far_in_true_incoming_mass_not_added_twice=True,physical_units_not_changed=True,wholecell_and_endpoint_norms_kept_distinct=True,outer_new_width_not_claimed=True,precision_bits=256,storage_bits=160,elapsed_seconds=time.monotonic()-start,peak_rss_kib=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)
 rec=p.save(a.out,out);print(json.dumps(dict(all_gates=True,packet=rec,head_bands=[str(v) for v in bands],gate_count=out['gate_count'],elapsed_seconds=out['elapsed_seconds'],peak_rss_kib=out['peak_rss_kib'])),flush=True)
if __name__=='__main__':main()
