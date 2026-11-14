#!/usr/bin/env python3
"""Actual same P1+.4 field: singleton cell12 endpoint readout.

Use the entire fine53 source/field, original point13 localV norm and new
1873-panel constant-logr kernels. Full reference inverse tail/Q/T masses
are paid once after output columns are combined for the near band.
Author: exact_closure (GPT-6 Astra Pro; AI-assisted),2026-11-13.
"""
import argparse,gzip,hashlib,json,resource,time
from fractions import Fraction as F
from pathlib import Path
from flint import arb,ctx
B=Path('/workspace/scratch/d1aa462cfc02');E=B/'exact-work'
PINS={
 'field':(E/'inner-fine53-posterior-r2.json.gz','3053e9cba77da784dfe3760451530c15a53d0366abda9b082276ec9e749ab9a5'),
 'field_resource':(E/'inner-fine53-posterior-run2-resource.json','a872eb692f534db4b3b49b8985188d5e2fcea4b3bd4f86622a03ae668fe2e1b5'),
 'head':(E/'inner-fine53-head-export-r1.json','2952b65dd8050bfb8cbd15dd20a067ad3ab2881dbb1a1febf66513ce6c02472f'),
 'head_resource':(E/'inner-fine53-head-export-run1-resource.json','e151299eb2a580eb21aa176d2cd9dd5feb8f20728adbb7f88848c4c7e8d47cbe'),
}
def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def read(p):
 p=Path(p)
 with (gzip.open(p,'rt') if p.suffix=='.gz' else p.open()) as f:return json.load(f)
def ex(v):
 if isinstance(v,(F,int)):return F(v)
 if isinstance(v,list):return F(int(v[0]))*F(2)**v[1]
 if 'upper' in v:return ex(v['upper'])
 if 'mantissa' in v:return F(int(v['mantissa']))*F(2)**v['binary_exponent']
 return F(int(v['numerator']),int(v['denominator']))
def ab(v):
 v=ex(v);return arb(v.numerator)/v.denominator
def pack(v):
 v=v if isinstance(v,arb) else ab(v)
 if not(v.is_finite() and v.lower()>=0):raise ArithmeticError('Finite positive bound required')
 if v==0:return ['0',0]
 m,e=map(int,v.upper().man_exp());s=max(0,m.bit_length()-160)
 if s:m,e=(m+(1<<s)-1)>>s,e+s
 if not arb(m)*arb(2)**e>=v.upper():raise ArithmeticError('Outward readout serialization')
 return [str(m),e]
def up(v):return ex(pack(v))
def support(weights,caps,mass):
 z=F(0);left=mass
 for i in sorted(range(len(weights)),key=lambda i:weights[i],reverse=True):
  if not left:break
  take=min(left,caps[i]);z+=weights[i]*take;left-=take
 return z

def main():
 p=argparse.ArgumentParser(description=__doc__);p.add_argument('--kernel',type=Path,required=True);p.add_argument('--kernel-sha256',required=True);p.add_argument('--kernel-resource',type=Path,required=True);p.add_argument('--out',type=Path,required=True);a=p.parse_args()
 if a.out.exists():raise FileExistsError('Fresh actual point result')
 ctx.prec,ctx.threads=256,1;start=time.monotonic();g={};docs={};ids={}
 def gate(k,b):
  if not b:raise ArithmeticError(k)
  g[k]=True
 for k,(path,pin) in PINS.items():gate('pin_'+k,sha(path)==pin);docs[k]=read(path);ids[k]=dict(path=str(path),sha256=pin)
 for k in ('field_resource','head_resource'):gate('actual0_'+k,docs[k]['exitcode']==0 and docs[k]['termination_signal'] is None)
 gate('actual_kernel_pin',sha(a.kernel)==a.kernel_sha256);ker=read(a.kernel);kr=read(a.kernel_resource);ids['kernel']=dict(path=str(a.kernel),sha256=a.kernel_sha256);ids['kernel_resource']=dict(path=str(a.kernel_resource),sha256=sha(a.kernel_resource))
 gate('actual_full_logr_kernel',ker['all_gates'] and ker['schema']=='inner-cell12-true-singleton-logr-exponential-endpoint-normalized-v2' and ker['original_panels']==1873 and ker['modes']==list(range(94,185,2)) and ker['uniform_angular_translation_invariant'] and ker['complete_current_panel_sources_paid'] and ker['complete_source_two_materials_retained'] and kr['exitcode']==0 and kr['termination_signal'] is None)
 rawrec=ker['original_actual_resource'];gate('actual_heavy_kernel_resource_pin',sha(rawrec['path'])==rawrec['sha256']);rawusage=read(rawrec['path']);gate('actual_heavy_kernel0',rawusage['exitcode']==0 and rawusage['termination_signal'] is None and rawusage['peak_rss_kib']<98304)
 field,old=docs['field'],docs['head'];gate('same_existing_complex_P1',field['all_gates'] and old['all_gates'] and field['domain']==old['domain'] and field['complete_mean_inverse_far'] and field['only_same_existing_complex_P1_field'] and not field['old_infinite_reweighted'])
 gate('same_shift040_point_units',ex(field['angular_weight_translation'])==F(2,5) and ex(ker['output_strip_original'])==ex(old['head_strip']) and field['same_original617_units']==old['same_original617_units'])
 W=field['windows'];pm=field['parent_window_of_fine'];r=field['rows'][0];incoming=field['rows'][1];gate('actual_cells12and13',r['cell']==12 and incoming['cell']==13 and W[:46]==[[m,m] for m in range(94,185,2)])
 def nested(weights,row,indices,region):
  caps=list(map(ex,row['window_caps']));groups=list(map(ex,row['retained_parent13_mass_caps']));left=ex(row['near_rest_common_caps'][region]);ans=F(0)
  for w in sorted(indices,key=lambda w:weights[w],reverse=True):
   if not left:break
   take=min(left,caps[w],groups[pm[w]]);ans+=weights[w]*take;left-=take;groups[pm[w]]-=take
  return ans
 srcid=field['input_identities']['source'];gate('complete_reference_source_pin',sha(srcid['path'])==srcid['sha256']);source=read(srcid['path']);gate('same_source_domain',source['domain']==field['domain'] and source['all213_original_cells'] and all(source['gates'].values()))
 ids['reference_source']=srcid
 rec=field['source_parts'][0];gate('reference_polynomial_chunk_pin',sha(rec['path'])==rec['sha256'])
 with gzip.open(rec['path'],'rt') as f:ref=json.loads(next(f))
 gate('full_cell12_reference_poly',ref['cell']==12 and ref['complete_mean_and_inverse_retained'] and ref['polynomial_support_max736'])
 poly={x['mode']:ex(x['common_d']) for x in ref['high_polynomial_pair_rows']};refmass=source['rows'][0]['source_common_mass']['common_d'];tail=ex(refmass['shared_complete_inverse_tail']);fullref=ex(refmass['near94to184']);gate('positive_complete_inverse_tail',tail>0 and fullref>0)
 ids['reference_polynomial_part']=rec
 dqrec=field['DQ_chunks'][0];gate('actual_DQ_chunk_pin',dqrec['cell']==12 and sha(dqrec['path'])==dqrec['sha256']);dq=read(dqrec['path']);ids['DQ_cell12']=dqrec
 gate('same_exact_actual_DQ_centre',dq['cell']==12 and dq['B_floor']>=120 and len(dq['kernels_s_upper'])==53 and len(dq['low_singleton_kernels_s_upper'])==53)
 for w in range(46):
  gate('common_material_pointwise_domination_'+str(w),all(ex(x)>=ex(y)>=0 for x,y in zip(dq['kernels_s_upper'][w],dq['kernels_ell_upper'][w])) and all(ex(x)>=ex(y)>=0 for x,y in zip(dq['low_singleton_kernels_s_upper'][w],dq['low_singleton_kernels_ell_upper'][w])))
 gamma=[];hin=[];rows=[];newcaps=list(map(ex,old['translated_head_window_masses']));oldcaps=newcaps[:]
 for w,m in enumerate(range(94,185,2)):
  k=ker['rows'][w];gate('every_true_singleton_kernel_'+str(m),k['window']==[m,m])
  Gs=ex(k['chosen_source_two_material_to_cut']['d1']);Gl=ex(k['chosen_source_two_material_to_cut']['d_lambda']);G=Gs+Gl;H=ex(k['chosen_input_nextcell_Vprime_mass_to_cut']);gamma.append(G);hin.append(H)
  qr=min(poly[m]+tail,fullref);dd=ex(r['DQ_common_source'][w]);sq=ex(r['full_quadratic_window_sources'][w]);tt=ex(r['full_mean_inverse_difference_source'])
  hi=H*ex(incoming['window_caps'][w]);refout=G*qr;dqout=G*dd;sqout=G*sq;tout=G*tt;image=up(hi+refout+dqout+sqout+tout);newcaps[w]=min(newcaps[w],image)
  rows.append(dict(mode=m,input_cell13=pack(hi),reference_full_inverse=pack(refout),DQ_complete=pack(dqout),Q_error_complete=pack(sqout),T_mean_inverse_complete=pack(tout),complete_point_image=pack(image),old_point_cap=pack(oldcaps[w]),chosen_point_cap=pack(newcaps[w]),homogeneous_input_kernel=pack(H),source_material_kernels={'d1':pack(Gs),'d_lambda':pack(Gl)}))
 # Combine each genuine readout column BEFORE taking a shared-input support.
 weights=hin+[F(0)]*7;incoming_band=nested(weights,incoming,range(46),0);maxG=max(gamma)
 finite_ref=sum((gamma[w]*poly[m] for w,m in enumerate(range(94,185,2))),F(0));reference_band=min(finite_ref+maxG*tail,maxG*fullref)
 lowcoef=[sum((gamma[w]*ex(dq['low_singleton_kernels_s_upper'][w][j]) for w in range(46)),F(0)) for j in range(46)]
 allcoef=[sum((gamma[w]*ex(dq['kernels_s_upper'][w][j]) for w in range(46)),F(0)) for j in range(55)]
 dq_low=support(lowcoef,list(map(ex,r['low_mode_caps'])),ex(r['fixed_low_cap']))
 dq_near=nested(allcoef[1:54],r,range(46),0);dq_rest=nested(allcoef[1:54],r,range(46,53),1);dq_inf=allcoef[54]*ex(r['complete_infinite_cap'])
 square_band=maxG*ex(r['full_quadratic_window_sources'][0]);T_band=maxG*ex(r['full_mean_inverse_difference_source'])
 near_image=up(incoming_band+reference_band+dq_low+dq_near+dq_rest+dq_inf+square_band+T_band)
 head=list(map(ex,old['translated_head_band_masses']));head[0]=min(head[0],near_image,up(sum(newcaps[:46],F(0))))
 original=list(map(ex,old['actual_R100_head_band_masses']));original[0]=min(original[0],up(sum((up(ab(v)*ab(-F(2*m,5)).exp()) for m,v in zip(range(94,185,2),newcaps[:46])),F(0))))
 gate('all_actual_point_caps_only_shrink',all(0<x<=y for x,y in zip(newcaps,oldcaps)) and all(0<x<=ex(y) for x,y in zip(head,old['translated_head_band_masses'])))
 gate('same96MiB_resource_gate',resource.getrusage(resource.RUSAGE_SELF).ru_maxrss<98304)
 result=dict(schema='same-P1-shift040-fine53-true-logr-cell12-point-v1',author='exact_closure (GPT-6 Astra Pro; AI-assisted)',source_sha256=sha(__file__),all_gates=all(g.values()),gates=g,gate_count=len(g),input_identities=ids,domain=field['domain'],head_strip=old['head_strip'],translated_head_strip=old['translated_head_strip'],angular_weight_translation=old['angular_weight_translation'],head_bands=old['head_bands'],windows=W,same_original617_units=old['same_original617_units'],readout_position=old['readout_position'],translated_head_band_masses=list(map(pack,head)),translated_head_window_masses=list(map(pack,newcaps)),actual_R100_head_band_masses=list(map(pack,original)),shift040_tail_split=old['shift040_tail_split'],rows=rows,near_complete_shared_budget=dict(incoming13=pack(incoming_band),reference=pack(reference_band),reference_shared_inverse_tail_once=pack(maxG*tail),DQ_low46=pack(dq_low),DQ_near46=pack(dq_near),DQ_rest7=pack(dq_rest),DQ_infinite=pack(dq_inf),full_Q_once=pack(square_band),full_T_mean_inverse_once=pack(T_band),complete_image=pack(near_image)),complete_mean_inverse_far=True,complete_infinite_repaid=True,old_rest_and_complete_infinite_unchanged=True,only_same_existing_complex_P1_field=True,new_fixedpoint_or_outer_continuation_claimed=False,no_new_ODE_or_integral=True,all_shared_mass_constraints_retained=True,precision_bits=256,elapsed_seconds=time.monotonic()-start,peak_rss_kib=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)
 a.out.write_text(json.dumps(result,separators=(',',':'))+'\n');print(json.dumps(dict(all_gates=True,sha256=sha(a.out),gate_count=len(g),elapsed_seconds=time.monotonic()-start,peak_rss_kib=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss,head=[str(float(x)) if x>F(1,10**300) else 'strictly positive dyadic' for x in head],m166=str(float(newcaps[36])),m184=str(float(newcaps[45])),near_terms={k:str(float(ex(v))) for k,v in result['near_complete_shared_budget'].items()})),flush=True)
if __name__=='__main__':main()
