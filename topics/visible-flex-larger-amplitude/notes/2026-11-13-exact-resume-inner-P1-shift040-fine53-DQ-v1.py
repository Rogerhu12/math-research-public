#!/usr/bin/env python3
"""Actual P1+.4 DQ: 46 near singletons, seven rest windows, full high input.

Same accepted Cs+Lambda centre, same two material coefficients, and exact
even membership partitions. One compressed chunk per original cell avoids
holding the large regenerable table in memory. No new ODE or integration.
Author: exact_closure (GPT-6 Astra Pro; AI-assisted), 2026-11-13.
"""
from fractions import Fraction as F
import argparse,gzip,hashlib,importlib.util,json,resource,time
from pathlib import Path
from flint import arb,ctx

B=Path('/workspace/scratch/d1aa462cfc02');E=B/'exact-work'
PINS={
 'modal':(E/'inner-P1-shift040-modal-r1.json.gz','c23f7f76037247d877a62833f00eb9a96798d4720b8188c5243bc8f128a3c773'),
 'modal_resource':(E/'inner-P1-shift040-modal-run1-resource.json','0b042b5eabf6a78702b07dc33e03608110d2033ba469698bb99f40c03e4dc426'),
 'density':(B/'math-research/topics/visible-flex-larger-amplitude/notes/2026-11-12-tail-r42-strong-same-tau-r1-density.json.gz','e640e3e693ca198460de902fc8d9bb1bd909c2a7051ec099aa930a86789e0700'),
 'base_formula':(E/'inner-fine53-dq-inputs/inner_CsLambda_DQ_window_kernels.py','ecd091b4400b21d66dcc78b0933fe09689ae65473d287f0b119f8782a5e1b673'),
 'low_formula':(E/'inner-fine53-dq-inputs/inner_restricted_DQ_windows_and_low_modes_v2.py','58083926d2cbfcc2800f4b694eb59f5aad20cd68fbfc3115dadab15b51aedd22'),
}
WINDOWS=[[m,m] for m in range(94,185,2)]+[[186,192],[194,256],[258,512],[514,1024],[1026,2048],[2050,4096],[4098,8190]]
INPUTS=[[2,92]]+WINDOWS+[[8192,None]]
def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def read(p):
 b=Path(p).read_bytes();return json.loads(gzip.decompress(b) if str(p).endswith('.gz') else b)
def load(name,p):
 s=importlib.util.spec_from_file_location(name,p);m=importlib.util.module_from_spec(s);s.loader.exec_module(m);return m
def save(p,d):
 if p.exists():raise FileExistsError(p)
 b=gzip.compress((json.dumps(d,separators=(',',':'))+'\n').encode(),mtime=0)
 if len(b)>=5000000:raise ArithmeticError('strict chunk size')
 p.write_bytes(b);return dict(path=str(p),sha256=sha(p),bytes=len(b))
def main():
 ap=argparse.ArgumentParser(description=__doc__);ap.add_argument('--out-dir',type=Path,required=True);a=ap.parse_args()
 if a.out_dir.exists() and any(a.out_dir.iterdir()):raise FileExistsError('fresh output directory')
 a.out_dir.mkdir(exist_ok=True);ctx.prec,ctx.threads=256,1;start=time.monotonic();g={};counts={}
 def gate(k,b):
  if not b:raise ArithmeticError(k)
  # Check every coefficient; compact only the bookkeeping keys.
  category=k.split('_')[0] if k.startswith(('membership_','partition_')) else k
  g[category]=True;counts[category]=counts.get(category,0)+1
 for k,(p,s) in PINS.items():gate('pin_'+k,sha(p)==s)
 base=load('fine53_original_DQ',PINS['base_formula'][0]);low=load('fine53_original_low_DQ',PINS['low_formula'][0])
 base.OUTPUT_WINDOWS=WINDOWS;base.INPUT_WINDOWS=INPUTS
 ex,ab,pack=base.fraction,base.ab,base.pack
 modal=read(PINS['modal'][0]);usage=read(PINS['modal_resource'][0]);density=read(PINS['density'][0]);domain=modal['domain']
 gate('formal_actual_modal',modal['all_gates'] and all(modal['gates'].values()) and usage['exitcode']==0 and usage['termination_signal'] is None)
 gate('complete_same_P1_shift',domain['name']=='R156_actual_full_cut_posterior' and ex(domain['S_product_radius'])==F(3,8) and ex(domain['T_l1_radius'])==F(1,64) and ex(modal['angular_weight_translation'])==F(2,5) and len(domain['T_coordinate_caps_by_mode'])==46 and not modal['full_error_or_infinite_tail_reweighted'])
 gate('same_original_units_and_density',modal['input_identities']['density']['sha256']==PINS['density'][1] and ex(modal['R100_envelope_scale'])==F(257,256) and all(density['gates'].values()) and modal['original_common_kernel_strip_difference_identity'] and modal['original_high_frame_strip_derivative_unchanged'])
 gate('complete53_output_cover',len(WINDOWS)==53 and sum((list(range(l,h+1,2)) for l,h in WINDOWS),[])==list(range(94,8191,2)))
 gate('complete55_input_cover',len(INPUTS)==55 and INPUTS[-1]==[8192,None] and sum((list(range(l,h+1,2)) for l,h in INPUTS[:-1]),[])==list(range(2,8191,2)))
 partition,intervals=base.partitions(gate);chunks=[];dominance=0
 for r,d in zip(modal['rows'],density['rows']):
  cell=r['cell'];B0=ex(d['B']).numerator//ex(d['B']).denominator;tau=ex(r['translated_tau_outer_lower'])
  gate('original_cell_units',cell==d['cell']==len(chunks)+12 and B0>=120 and ex(r['original_tau_outer_lower'])==ex(d['tau_outer']) and tau==ex(d['tau_outer'])+F(2,5))
  gate('exact_ell_reduction',5*92<=4*B0 and 10*(B0-92)>=1)
  caps=list(map(ab,r['Cs_plus_Lambda_pair_caps']));gate('all46_actual_reference_modes',len(caps)==46 and all(x>0 and x.is_finite() for x in caps))
  decay=[(-2*k*ab(tau)).exp().upper() for k in base.MODES]
  weights=[]
  for k,c,e in zip(base.MODES,caps,decay):
   z=(c/(1+k)).upper();weights.append((z,(k*z).upper(),(z*e).upper(),(k*z*e).upper()))
  sums=base.interval_sums(weights);ks=[];ke=[];ns=[];ne=[]
  for wi,window in enumerate(WINDOWS):
   rs=[];re=[];rns=[];rne=[]
   for part in partition[wi]:
    bs=arb(0);be=arb(0);ats=ate=None
    for n in part['candidate_modes']:
     plus,minus=base.ranges(window,n);s0=arb(0);s1=arb(0)
     if plus:s0+=sums[plus][0];s1+=sums[plus][1]
     if minus:s0+=sums[minus][2];s1+=sums[minus][3]
     vs=(5*n*s1/(4*(1+n))).upper()
     ve=(s0/(1+n) if 5*n<=4*B0 else s0*5*n/(4*B0*(1+n))).upper()
     if vs>bs:bs=vs;ats=n
     if ve>be:be=ve;ate=n
    gate('every_exact_zero_support',(bs==0 and be==0)==part['strict_zero'])
    gate('every_material_domination',bs>=be);dominance+=1
    rs.append(pack(bs));re.append(pack(be));rns.append(ats);rne.append(ate)
   ks.append(rs);ke.append(re);ns.append(rns);ne.append(rne)
  ls,le=low.low_singletons(WINDOWS,sums,B0,lambda k,v:gate('low_singleton_all46',v),cell,base.ranges,pack,arb)
  row=dict(cell=cell,B_floor=B0,tau_outer_lower=dict(numerator=str(tau.numerator),denominator=str(tau.denominator)),reference_strong_pair_caps=r['Cs_plus_Lambda_pair_caps'],reference_common_cap=r['Cs_plus_Lambda_common_cap'],difference_weight_upper=list(map(pack,decay)),kernels_s_upper=ks,kernels_ell_upper=ke,low_singleton_kernels_s_upper=ls,low_singleton_kernels_ell_upper=le,maximizing_candidate_mode_s=ns,maximizing_candidate_mode_ell=ne)
  rec=save(a.out_dir/f'cell{cell:03d}.json.gz',row);chunks.append(dict(cell=cell,**rec))
  gate('owned_RSS_below96MiB',resource.getrusage(resource.RUSAGE_SELF).ru_maxrss<98304)
  if len(chunks)%24==0 or cell==224:print(json.dumps(dict(event='actual_fine53_DQ_cell',cell=cell,completed=len(chunks),elapsed_seconds=time.monotonic()-start,peak_rss_kib=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)),flush=True)
 gate('complete_all213_cells',[r['cell'] for r in chunks]==list(range(12,225)))
 result=dict(schema='inner-P1-shift040-fine53-DQ-two-material-chunks-v1',author='exact_closure (GPT-6 Astra Pro; AI-assisted)',source_sha256=sha(__file__),all_gates=all(g.values()),gates=g,gate_categories=counts,gate_count=sum(counts.values()),input_identities={k:dict(path=str(p),sha256=s) for k,(p,s) in PINS.items()},domain=domain,angular_weight_translation=modal['angular_weight_translation'],normalization=modal['normalization'],cells=list(range(12,225)),modes_center=base.MODES,low_singleton_input_modes=base.MODES,windows_out=WINDOWS,windows_in=INPUTS,chunk_records=chunks,membership_partition=partition,membership_intervals=intervals,actual_material_domination_comparisons=dominance,full_DQ_matrix_shape=[213,2,53,55],low_singleton_matrix_shape=[213,2,53,46],precision_bits=256,coefficient_storage_significant_bits=160,operator_contract='Each input window is one joint strong signed-pair mass. The source output is weak and carries no additional1+m. All source modes above output_max+92 have exactly zero DQ coefficient, not a truncated infinite mass.',material_units='relative N: s*(Vprime/w)^2 and abs(ell)*(Vprime/w)^2; physical kappa source: s*Vprime^2/w and abs(ell)*Vprime^2/w',complete_mean_inverse_and_quadratic_remainders_not_in_DQ=True,no_new_ODE_or_Green_or_integral=True,new_fixedpoint_claimed=False,elapsed_seconds=time.monotonic()-start,peak_rss_kib=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)
 rec=save(a.out_dir/'certificate.json.gz',result);print(json.dumps(dict(all_gates=True,certificate=rec,gate_count=result['gate_count'],elapsed_seconds=result['elapsed_seconds'],peak_rss_kib=result['peak_rss_kib'])),flush=True)
if __name__=='__main__':main()
