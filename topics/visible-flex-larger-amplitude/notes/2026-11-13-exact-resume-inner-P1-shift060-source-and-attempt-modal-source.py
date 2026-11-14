#!/usr/bin/env python3
"""Actual P1 finite-reference and enlarged far-domain ledger for delta=3/5.

The previous2^-30 lift workspace is reported diagnostically. The new
finite lift cap1/64, physical mean domain and every subsequent complete
641 fixedpoint/comparison gate are paid afresh; no old claim is enlarged.

Only Cs and Lambda are finite46 and may be reweighted directly. Exact greedy objectives are retained; active indices are saved without huge redundant rational allocation strings. No old
infinite error cap is reweighted. The new complete fixedpoint remains a
separate task; linear kernels are invariant under the simultaneous shift.
Author: exact_closure (GPT-6 Astra Pro; AI-assisted), 2026-11-13.
"""
import argparse,gzip,hashlib,json,resource,time
from fractions import Fraction as F
from pathlib import Path
from flint import arb,ctx
BASE=Path('/workspace/scratch/d1aa462cfc02')
TOP=BASE/'math-research/topics/visible-flex-larger-amplitude'
MODES=list(range(2,93,2))
def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def read(p):
 with (gzip.open(p,'rt') if str(p).endswith('.gz') else open(p)) as f:return json.load(f)
def ex(v):
 if isinstance(v,list):return F(int(v[0]))*F(2)**int(v[1])
 if 'upper' in v:return ex(v['upper'])
 if 'mantissa' in v:return F(int(v['mantissa']))*F(2)**int(v['binary_exponent'])
 return F(int(v['numerator']),int(v['denominator']))
def ab(v):
 v=ex(v) if not isinstance(v,F) else v
 return arb(v.numerator)/v.denominator
def pack(v,bits=160):
 if isinstance(v,F):
  if v<0:raise ArithmeticError('Nonnegative rational cap')
  if not v:return ['0',0]
  e=v.numerator.bit_length()-v.denominator.bit_length()
  if v<F(2)**e:e-=1
  e-=bits-1;r=v/F(2)**e;m=(r.numerator+r.denominator-1)//r.denominator
 else:
  v=v.upper()
  if not(v.is_finite() and v>=0):raise ArithmeticError('Finite nonnegative Arb cap')
  if v==0:return ['0',0]
  m,e=map(int,v.man_exp());cut=max(0,m.bit_length()-bits)
  if cut:m,e=(m+(1<<cut)-1)>>cut,e+cut
 out=[str(m),e]
 if isinstance(v,F):
  if ex(out)<v:raise ArithmeticError('Rational outward rounding')
 elif not ab(out)>=v:raise ArithmeticError('Arb outward rounding')
 return out
def rat(v):return dict(numerator=str(v.numerator),denominator=str(v.denominator))
def support(weights,caps,mass):
 left=mass;value=F(0);used=[]
 for i in sorted(range(len(weights)),key=lambda j:weights[j],reverse=True):
  amount=min(left,caps[i])
  if amount>0:value+=weights[i]*amount;left-=amount;used.append(MODES[i])
  if left==0:break
 return value,used
def main():
 p=argparse.ArgumentParser(description=__doc__)
 p.add_argument('--out-prefix',type=Path,required=True);p.add_argument('--shift',default='3/5');p.add_argument('--rss-kib',type=int,default=98304)
 args=p.parse_args();start=time.monotonic();ctx.prec=256;ctx.threads=1;delta=F(args.shift)
 if delta!=F(3,5):raise ValueError('This fresh space declares exactly delta=3/5')
 out=Path(str(args.out_prefix)+'.json.gz')
 if out.exists():raise FileExistsError('Fresh translated norm ledger required')
 mp=BASE/'root-work/r127/R157-P1-modal-r1.json.gz';mr=BASE/'root-work/r127/R157-P1-modal-r1-resource.json'
 dp=TOP/'notes/2026-11-12-tail-r42-strong-same-tau-r1-density.json.gz'
 modal,usage,density=read(mp),read(mr),read(dp);counts={}
 def gate(k,v):
  if not bool(v):raise ArithmeticError('Unpaid new-strip centre gate '+k)
  counts[k]=counts.get(k,0)+1
 gate('same_current_P1_modal_pin',sha(mp)=='b6449aa97ea25e1f26760867fe1916efa2eb71cbce910658632473940435f8a0')
 gate('same_original_density_pin',sha(dp)=='e640e3e693ca198460de902fc8d9bb1bd909c2a7051ec099aa930a86789e0700')
 gate('completed_actual_P_input',modal['all_gates'] and all(modal['gates'].values()) and usage['exitcode']==0 and usage['termination_signal'] is None)
 gate('all213_all46_finite_reference',modal['cells']==list(range(12,225)) and modal['modes']==MODES and modal['C_S_is_low46_auxiliary'])
 gate('same_original_Vprime',ex(modal['R100_envelope_scale'])==F(257,256))
 domain=modal['domain'];R=ex(domain['T_l1_radius']);tcaps=[ex(v) for v in domain['T_coordinate_caps_by_mode']]
 gate('same_actual_P1_domain',domain['name']=='R156_actual_full_cut_posterior' and domain['simultaneous_original_coordinates'] and len(tcaps)==46)
 weights=[ex(pack((m*ab(delta)).exp())) for m in MODES]
 rows=[];maxC=(F(0),None);maxL=(F(0),None);maxphys=(F(0),None)
 for row,dr in zip(modal['rows'],density['rows']):
  n=row['cell'];gate('same_cell_order',n==dr['cell']==12+len(rows))
  ccap=[ex(v) for v in row['Cs_complete_pair_caps']];lcap=[ex(v) for v in row['Lambda_pair_caps_on_domain']]
  cups=[cap*w for cap,w in zip(ccap,weights)];lups=[cap*w for cap,w in zip(lcap,weights)]
  C,Cwit=support(weights,ccap,ex(row['Cs_common_cap']))
  direct=[ex(v)*w for v,w in zip(row['transverse_unit_axis_pairs'],weights)]
  L,Lwit=support(direct,tcaps,R)
  L=min(L,sum(lups,F(0)),ex(row['Lambda_common_cap_on_domain'])*max(weights))
  C=min(C,sum(cups,F(0)))
  combined=[min(a+b,ex(old)*w) for a,b,old,w in zip(cups,lups,row['Cs_plus_Lambda_pair_caps'],weights)]
  B0,_=support(weights,[ex(v) for v in row['Cs_plus_Lambda_pair_caps']],ex(row['Cs_plus_Lambda_common_cap']))
  B=min(C+L,sum(combined,F(0)),B0)
  A=F(257,256)*ex(dr['V_over_w_upper']);physical=A*B
  gate('all_reweighted_finite_caps_nonnegative',all(v>=0 for v in cups+lups+combined))
  gate('complete_new_centre_mean_domain',0<physical<F(1,128))
  gate('translated_lift_fits_declared_new_finite_work_cap',0<L<F(1,64))
  oldin,oldout=ex(row['tau_inner_upper']),ex(row['tau_outer_lower'])
  newin,newout=oldin+delta,oldout+delta
  gate('exact_original_drop_unchanged',newin-newout==oldin-oldout)
  if C>maxC[0]:maxC=(C,n)
  if L>maxL[0]:maxL=(L,n)
  if physical>maxphys[0]:maxphys=(physical,n)
  rows.append(dict(cell=n,original_tau_inner_upper=rat(oldin),original_tau_outer_lower=rat(oldout),
    translated_tau_inner_upper=rat(newin),translated_tau_outer_lower=rat(newout),
    Cs_complete_pair_caps=list(map(pack,cups)),Cs_common_cap=pack(C),
    Lambda_pair_caps_on_domain=list(map(pack,lups)),Lambda_common_cap_on_domain=pack(L),
    Cs_plus_Lambda_pair_caps=list(map(pack,combined)),Cs_plus_Lambda_common_cap=pack(B),
    Cs_support_active_modes=Cwit,Lambda_support_active_modes=Lwit,
    physical_Amax=pack(A),relative_physical_centre_cap=pack(physical),
    original_reference_tau=row['tau_reference_lower']))
  if resource.getrusage(resource.RUSAGE_SELF).ru_maxrss>args.rss_kib:raise MemoryError('Owned96MiB guard')
 farcols=[ex(v)*w for v,w in zip(modal['far_unit_axis_pairs_unscaled_by_S'],weights)]
 far,farwit=support(farcols,tcaps,R)
 far=min(far,ex(modal['far_common_on_domain'])*max(weights))
 aux=F(1,2**2224)*max(weights);Zold=F(1,2**2200);Znew=F(1,2**2112);R18=F(1,2**1947)
 gate('full_finite46_auxiliary_far_reweight',aux>0 and max(weights)==weights[-1])
 gate('new_far_domain_with_strict_centre_margin',aux+far<Znew/4)
 gate('R18_same_graph_defined_at_new_width',Znew<=R18/2)
 # R18 section5 permits every tau_F>0. The entire tail sequence is shifted,
 # so all Green exponents use exactly the same width differences.
 farstrip=F(38)+delta
 gate('same_far_to_head_strip_gaps',farstrip-(ex(density['tau_deep'])+delta)==F(38)-ex(density['tau_deep']))
 result=dict(schema='inner-R100-uniformly-shifted-Cs-Lambda-modal-v1',author='exact_closure (GPT-6 Astra Pro; AI-assisted)',
  source_sha256=sha(__file__),all_gates=True,gates={k:True for k in counts},gate_count=sum(counts.values()),gate_categories=counts,
  input_identities={'parent_modal':dict(path=str(mp),sha256=sha(mp)),'parent_modal_resource':dict(path=str(mr),sha256=sha(mr)),'density':dict(path=str(dp),sha256=sha(dp))},
  cells=list(range(12,225)),modes=MODES,domain=domain,parent_full_domain=modal['parent_full_domain'],
  angular_weight_translation=rat(delta),old_and_new_weight_definitions='tau_new(r)=tau_original_q(r)+delta on all213cells; tail tau_F_new=38+delta; same physical background and Vprime.',
  finite_reweight_factors=list(map(pack,weights)),R100_envelope_scale=modal['R100_envelope_scale'],
  normalization='Strong pair masses of physical(Bp,kappa_perp)/Vprime in NEW translated strip, with separate radial suprema; Vprime=(257/256)Vs unchanged.',
  C_S_is_low46_auxiliary=True,C_S_domain_contained_in_R121_R74=True,rows=rows,
  original_common_kernel_strip_difference_identity=True,original_high_frame_strip_derivative_unchanged=True,
  full_error_or_infinite_tail_reweighted=False,new_complete_fixedpoint_proved=False,same_existing_solution_identification_paid=False,
  far_common_on_domain=pack(far),far_parameter_support_active_modes=farwit,
  far_domain=dict(original_width='38',translated_width=rat(farstrip),original_graph_ball=pack(Zold),
    proposed_new_graph_ball=pack(Znew),R18_allowed_graph_radius=pack(R18),original_auxiliary_far_bound=pack(F(1,2**2224)),
    finite46_auxiliary_far_bound_in_new_width=pack(aux),complete_finite_reference_far_bound=pack(aux+far),
    remaining_unknown_far_radius_not_yet_paid=True,R18_quadratic_remainder_constant_log2=1967),
  maxima=dict(Cs=dict(upper=pack(maxC[0]),cell=maxC[1]),Lambda=dict(upper=pack(maxL[0]),cell=maxL[1]),physical_reference=dict(upper=pack(maxphys[0]),cell=maxphys[1])),
  previous_lift_work_radius_diagnostic=dict(old_threshold='2^-30',passes=bool(maxL[0]<F(1,2**30)),not_a_new_space_mean_or_fixedpoint_gate=True,new_finite_lift_cap='1/64'),
  new_far_graph_choice='2^-2112; every original source and derivative scale must be recomputed with this exact radius; all complete641 gates remain separate',
  elapsed_seconds=time.monotonic()-start,peak_rss_kib=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)
 raw=(json.dumps(result,separators=(',',':'))+'\n').encode()
 if len(raw)>=4_900_000:raise MemoryError('Compact complete translated-reference packet')
 out.parent.mkdir(parents=True,exist_ok=True);out.write_bytes(gzip.compress(raw,mtime=0))
 print(json.dumps(dict(all_gates=True,path=str(out),sha256=sha(out),bytes=out.stat().st_size,gate_count=result['gate_count'],elapsed_seconds=result['elapsed_seconds'],peak_rss_kib=result['peak_rss_kib'])),flush=True)
if __name__=='__main__':main()
