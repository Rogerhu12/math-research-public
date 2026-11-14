#!/usr/bin/env python3
"""Actual inner low projection LF=Pi_<=92(Cs+Lambda+e), translated to3/5.
Only this known finite46 projection and finite46 far parameter are lifted.
No conditional high fixedpoint or unknown infinite widening is claimed.
Author: exact_closure (GPT-6 Astra Pro; AI-assisted),2026-11-13.
"""
import argparse,gzip,hashlib,json,resource,time
from fractions import Fraction as F
from pathlib import Path
from flint import arb,ctx
B=Path('/workspace/scratch/d1aa462cfc02');E=B/'exact-work';TOP=B/'math-research/topics/visible-flex-larger-amplitude'
PINS={
 'field':(E/'inner-fine53-posterior-r2.json.gz','3053e9cba77da784dfe3760451530c15a53d0366abda9b082276ec9e749ab9a5'),
 'field_resource':(E/'inner-fine53-posterior-run2-resource.json','a872eb692f534db4b3b49b8985188d5e2fcea4b3bd4f86622a03ae668fe2e1b5'),
 'modal':(E/'inner-P1-shift040-modal-r1.json.gz','c23f7f76037247d877a62833f00eb9a96798d4720b8188c5243bc8f128a3c773'),
 'modal_resource':(E/'inner-P1-shift040-modal-run1-resource.json','0b042b5eabf6a78702b07dc33e03608110d2033ba469698bb99f40c03e4dc426'),
 'existence':(E/'inner-P1-shift040-641-cert-r1.json.gz','ade2693eeb64007fdde072a855b7e65c3f125ba294793eb7e78975bd9ccc79c0'),
 'existence_resource':(E/'inner-P1-shift040-641-cert-run1-resource.json','e2caf4e9019a011f00cb5f0ec0067dd1e13598508a07bbb506656c1b67d5c6c7'),
 'density':(TOP/'notes/2026-11-12-tail-r42-strong-same-tau-r1-density.json.gz','e640e3e693ca198460de902fc8d9bb1bd909c2a7051ec099aa930a86789e0700')}
def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def read(p):
 with (gzip.open(p,'rt') if str(p).endswith('.gz') else open(p)) as f:return json.load(f)
def ex(v):
 if isinstance(v,(F,int)):return F(v)
 if isinstance(v,list):return F(int(v[0]))*F(2)**v[1]
 if 'upper' in v:return ex(v['upper'])
 if 'mantissa' in v:return F(int(v['mantissa']))*F(2)**int(v['binary_exponent'])
 return F(int(v['numerator']),int(v['denominator']))
def ab(v):
 v=ex(v);return arb(v.numerator)/v.denominator
def pack(z):
 z=z if isinstance(z,arb) else ab(z)
 if not(z.is_finite() and z.lower()>=0):raise ArithmeticError('finite nonnegative cap')
 if z==0:return ['0',0]
 m,e=map(int,z.upper().man_exp());s=max(0,m.bit_length()-160)
 if s:m,e=(m+(1<<s)-1)>>s,e+s
 if not arb(m)*arb(2)**e>=z.upper():raise ArithmeticError('outward cap')
 return [str(m),e]
def up(z):return ex(pack(z))
def rat(z):return dict(numerator=str(z.numerator),denominator=str(z.denominator))
def support(weights,caps,mass):
 ans=F(0);left=mass
 for k in sorted(range(46),key=lambda k:weights[k],reverse=True):
  t=min(left,caps[k]);ans+=weights[k]*t;left-=t
  if not left:break
 return ans
def main():
 p=argparse.ArgumentParser(description=__doc__);p.add_argument('--out',type=Path,required=True);a=p.parse_args()
 if a.out.exists():raise FileExistsError('fresh actual LF input')
 ctx.prec,ctx.threads=256,1;start=time.monotonic();d={};ids={};g={}
 def gate(k,b):
  if not b:raise ArithmeticError(k)
  g[k]=True
 for k,(path,pin) in PINS.items():gate('pin_'+k,sha(path)==pin);d[k]=read(path);ids[k]=dict(path=str(path),sha256=pin)
 for k in ('field_resource','modal_resource','existence_resource'):gate('owned0_'+k,d[k]['exitcode']==0 and d[k]['termination_signal'] is None)
 field,modal,cert,density=d['field'],d['modal'],d['existence'],d['density'];modes=list(range(2,93,2));extra=F(1,5)
 gate('same_existing_actual_inner_field',field['all_gates'] and field['complete_mean_inverse_far'] and field['only_same_existing_complex_P1_field'] and not field['old_infinite_reweighted'] and cert['all_gates'] and cert['new_complete_fixedpoint_proved'] and cert['same_original_full_field_identified'])
 gate('same_exact_domain_and_reference',field['domain']==modal['domain']==cert['domain'] and ex(field['angular_weight_translation'])==ex(modal['angular_weight_translation'])==ex(cert['angular_weight_translation'])==F(2,5) and field['input_identities']['modal']['sha256']==PINS['modal'][1] and cert['input_identities']['modal_input']['sha256']==PINS['modal'][1])
 gate('actual_LF_not_auxiliary_Cs_or_outer_CL',modal['C_S_is_low46_auxiliary'] and modal['cells']==list(range(12,225)) and modal['modes']==modes and len(field['rows'])==213)
 weights=[up((m*ab(extra)).exp()) for m in modes];rows=[];maxphys=F(0);maxLF=F(0)
 for i,(mr,er,dr) in enumerate(zip(modal['rows'],field['rows'],density['rows'])):
  n=12+i;gate('order_'+str(n),mr['cell']==er['cell']==dr['cell']==n)
  cc=list(map(ex,mr['Cs_plus_Lambda_pair_caps']));ee=list(map(ex,er['low_mode_caps']));cm=ex(mr['Cs_plus_Lambda_common_cap']);em=ex(er['fixed_low_cap'])
  gate('all_known_low_pairs_'+str(n),len(cc)==len(ee)==46 and all(x>=0 for x in cc+ee) and cm>0 and em>0)
  pair=[up(w*(c+e)) for w,c,e in zip(weights,cc,ee)]
  common=up(min(support(weights,cc,cm)+support(weights,ee,em),sum(pair,F(0)),support(weights,[c+e for c,e in zip(cc,ee)],cm+em)))
  aa=up(F(257,256)*ex(dr['V_over_w_upper']));phys=up(aa*common);maxphys=max(maxphys,phys);maxLF=max(maxLF,common)
  gate('complete_finite_LF_physical_domain_'+str(n),0<phys<F(1,128))
  rows.append(dict(cell=n,finite_LF_pair_caps=list(map(pack,pair)),finite_LF_common_cap=pack(common),known_Cs_plus_Lambda_pair_caps_at040=mr['Cs_plus_Lambda_pair_caps'],known_complete_e_low_pair_caps_at040=er['low_mode_caps'],known_Cs_plus_Lambda_common_at040=mr['Cs_plus_Lambda_common_cap'],known_complete_e_low_common_at040=er['fixed_low_cap'],translated_tau_inner_upper=rat(ex(mr['translated_tau_inner_upper'])+extra),translated_tau_outer_lower=rat(ex(mr['translated_tau_outer_lower'])+extra),original_tau_inner_upper=mr['original_tau_inner_upper'],original_tau_outer_lower=mr['original_tau_outer_lower'],physical_Amax=pack(aa),relative_physical_LF_cap=pack(phys)))
 far040=ex(cert['far']['whole_new_graph_argument']);far060=up(weights[-1]*far040);Zdom=F(2)**-2142
 gate('finite46_far_parameter_new_width_domain',0<far060<Zdom/4 and Zdom<=F(2)**-1948)
 gate('same96MiB',resource.getrusage(resource.RUSAGE_SELF).ru_maxrss<98304)
 result=dict(schema='same_actual_inner_LF_finite46_fixed_far_shift060_v1',author='exact_closure (GPT-6 Astra Pro; AI-assisted)',source_sha256=sha(__file__),all_gates=True,gates=g,gate_count=len(g),input_identities=ids,domain=field['domain'],parent_full_domain=modal['parent_full_domain'],cells=list(range(12,225)),modes=modes,angular_weight_translation=rat(F(3,5)),additional_from_known_field_translation=rat(extra),R100_envelope_scale=modal['R100_envelope_scale'],finite_LF_is_actual_projection_of_same_existing_field=True,LF_identity='Pi_even_2to92 F=Cs+Lambda+Pi_even_2to92 e, all from the same already identified P1 inner field at width+2/5. Neither Cs nor outerCL is relabeled.',normalization='Complete physical balanced strong pair mass/Vprime on each original inner cell; same Vprime and geometry; new width originaltau+3/5.',rows=rows,fixed_far_parameter=dict(modes=modes,known_width='38+2/5',new_width='38+3/5',known_actual_upper=pack(far040),finite_translation_factor_max=pack(weights[-1]),new_actual_upper=pack(far060),evaluation_graph_domain=pack(Zdom),original_unshifted_argument_upper=cert['far']['whole_lowered_original_argument'],finite46_only=True,unknown_graph_output_not_reweighted=True),maximum_physical_LF=pack(maxphys),maximum_dimensionless_LF=pack(maxLF),all_mean_and_inverse_to_be_recomputed_in_source=True,conditional_nonlow_fixedpoint_proved=False,conditional_samefield_identification_paid=False,no_unknown_infinite_reweight=True,no_new_ODE_or_integral=True,precision_bits=256,elapsed_seconds=time.monotonic()-start,peak_rss_kib=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)
 raw=(json.dumps(result,separators=(',',':'))+'\n').encode();gate('split_file_gate',len(raw)<4900000);a.out.write_bytes(gzip.compress(raw,mtime=0))
 print(json.dumps(dict(all_gates=True,path=str(a.out),sha256=sha(a.out),gate_count=len(g),maximum_physical=float(maxphys),maximum_LF=float(maxLF),far_log2=str(ab(far060).log()/arb(2).log()),elapsed_seconds=time.monotonic()-start,peak_rss_kib=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)),flush=True)
if __name__=='__main__':main()
