#!/usr/bin/env python3
"""Actual inner full LF+.6 DQ: 46 near singletons,21 rest windows, full nonlow input; low LF fixed.

Same actual LF=Pi_low46 F finite input, same two material coefficients, and exact
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
 'modal':(E/'inner-actual-LF-shift060-r1.json.gz','ff1df29ff5f24ffd6ed13dbc80c9f4a96d0e3084bacf03ebce41343d2d0ac811'),
 'modal_resource':(E/'inner-actual-LF-shift060-run1-resource.json','b9e95c4eb67cb109e50fc3b3b63be5b12871dfcff7f50ecacf31dde2e7b8ad83'),
 'density':(B/'math-research/topics/visible-flex-larger-amplitude/notes/2026-11-12-tail-r42-strong-same-tau-r1-density.json.gz','e640e3e693ca198460de902fc8d9bb1bd909c2a7051ec099aa930a86789e0700'),
 'base_formula':(E/'inner-fine53-dq-inputs/inner_CsLambda_DQ_window_kernels.py','ecd091b4400b21d66dcc78b0933fe09689ae65473d287f0b119f8782a5e1b673'),
 'low_formula':(E/'inner-fine53-dq-inputs/inner_restricted_DQ_windows_and_low_modes_v2.py','58083926d2cbfcc2800f4b694eb59f5aad20cd68fbfc3115dadab15b51aedd22'),
}
WINDOWS=[[94, 94], [96, 96], [98, 98], [100, 100], [102, 102], [104, 104], [106, 106], [108, 108], [110, 110], [112, 112], [114, 114], [116, 116], [118, 118], [120, 120], [122, 122], [124, 124], [126, 126], [128, 128], [130, 130], [132, 132], [134, 134], [136, 136], [138, 138], [140, 140], [142, 142], [144, 144], [146, 146], [148, 148], [150, 150], [152, 152], [154, 154], [156, 156], [158, 158], [160, 160], [162, 162], [164, 164], [166, 166], [168, 168], [170, 170], [172, 172], [174, 174], [176, 176], [178, 178], [180, 180], [182, 182], [184, 184], [186, 192], [194, 208], [210, 224], [226, 240], [242, 256], [258, 272], [274, 288], [290, 304], [306, 320], [322, 336], [338, 352], [354, 368], [370, 384], [386, 416], [418, 448], [450, 480], [482, 512], [514, 1024], [1026, 2048], [2050, 4096], [4098, 8190]]
INPUTS=WINDOWS+[[8192,None]]
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
 ap=argparse.ArgumentParser(description=__doc__);ap.add_argument('--out-dir',type=Path,required=True);ap.add_argument('--first-cell',type=int,required=True);ap.add_argument('--last-cell',type=int,required=True);a=ap.parse_args()
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
 gate('complete_same_P1_shift',domain['name']=='R156_actual_full_cut_posterior' and ex(domain['S_product_radius'])==F(3,8) and ex(domain['T_l1_radius'])==F(1,64) and ex(modal['angular_weight_translation'])==F(3,5) and len(domain['T_coordinate_caps_by_mode'])==46 and modal['no_unknown_infinite_reweight'] and modal['finite_LF_is_actual_projection_of_same_existing_field'])
 gate('same_original_units_and_density',modal['input_identities']['density']['sha256']==PINS['density'][1] and ex(modal['R100_envelope_scale'])==F(257,256) and all(density['gates'].values()) and modal['schema']=='same_actual_inner_LF_finite46_fixed_far_shift060_v1')
 gate('complete67_output_cover',len(WINDOWS)==67 and sum((list(range(l,h+1,2)) for l,h in WINDOWS),[])==list(range(94,8191,2)))
 gate('complete68_nonlow_input_cover',len(INPUTS)==68 and INPUTS[-1]==[8192,None] and sum((list(range(l,h+1,2)) for l,h in INPUTS[:-1]),[])==list(range(94,8191,2)));gate('declared_original_cells',12<=a.first_cell<=a.last_cell<=224)
 partition,intervals=base.partitions(gate);chunks=[];dominance=0
 for r,d in zip(modal['rows'],density['rows']):
  cell=r['cell']
  if not a.first_cell<=cell<=a.last_cell:continue
  B0=ex(d['B']).numerator//ex(d['B']).denominator;tau=ex(r['translated_tau_outer_lower'])
  gate('original_cell_units',cell==d['cell']==len(chunks)+a.first_cell and B0>=120 and ex(r['original_tau_outer_lower'])==ex(d['tau_outer']) and tau==ex(d['tau_outer'])+F(3,5))
  gate('exact_ell_reduction',5*92<=4*B0 and 10*(B0-92)>=1)
  caps=list(map(ab,r['finite_LF_pair_caps']));gate('all46_actual_reference_modes',len(caps)==46 and all(x>0 and x.is_finite() for x in caps))
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
  row=dict(cell=cell,B_floor=B0,tau_outer_lower=dict(numerator=str(tau.numerator),denominator=str(tau.denominator)),reference_strong_pair_caps=r['finite_LF_pair_caps'],reference_common_cap=r['finite_LF_common_cap'],difference_weight_upper=list(map(pack,decay)),kernels_s_upper=ks,kernels_ell_upper=ke,maximizing_candidate_mode_s=ns,maximizing_candidate_mode_ell=ne)
  rec=save(a.out_dir/f'cell{cell:03d}.json.gz',row);chunks.append(dict(cell=cell,**rec))
  gate('owned_RSS_below96MiB',resource.getrusage(resource.RUSAGE_SELF).ru_maxrss<98304)
  if len(chunks)%16==0 or cell==a.last_cell:print(json.dumps(dict(event='actual_fine67_DQ_cell',cell=cell,completed=len(chunks),elapsed_seconds=time.monotonic()-start,peak_rss_kib=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)),flush=True)
 gate('complete_declared_source_cells',[r['cell'] for r in chunks]==list(range(a.first_cell,a.last_cell+1)))
 result=dict(schema='inner-actual-LF-shift060-fine67-nonlow-DQ-chunks-batch-v1',author='exact_closure (GPT-6 Astra Pro; AI-assisted)',source_sha256=sha(__file__),all_gates=all(g.values()),gates=g,gate_categories=counts,gate_count=sum(counts.values()),input_identities={k:dict(path=str(p),sha256=s) for k,(p,s) in PINS.items()},domain=domain,angular_weight_translation=modal['angular_weight_translation'],normalization=modal['normalization'],cells=list(range(a.first_cell,a.last_cell+1)),first_cell=a.first_cell,last_cell=a.last_cell,modes_center=base.MODES,low_projection_fixed=True,windows_out=WINDOWS,windows_in=INPUTS,chunk_records=chunks,membership_partition=partition,membership_intervals=intervals,actual_material_domination_comparisons=dominance,full_DQ_matrix_shape=[len(chunks),2,67,68],no_low_input_perturbation_columns_needed=True,precision_bits=256,coefficient_storage_significant_bits=160,operator_contract='Each input window is one joint strong signed-pair mass. The source output is weak and carries no additional1+m. All source modes above output_max+92 have exactly zero DQ coefficient, not a truncated infinite mass.',material_units='relative N: s*(Vprime/w)^2 and abs(ell)*(Vprime/w)^2; physical kappa source: s*Vprime^2/w and abs(ell)*Vprime^2/w',complete_mean_inverse_and_quadratic_remainders_not_in_DQ=True,no_new_ODE_or_Green_or_integral=True,actual_LF_is_full_same_field_projection=True,conditional_nonlow_fixedpoint_claimed=False,elapsed_seconds=time.monotonic()-start,peak_rss_kib=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)
 rec=save(a.out_dir/'certificate.json.gz',result);print(json.dumps(dict(all_gates=True,certificate=rec,gate_count=result['gate_count'],elapsed_seconds=result['elapsed_seconds'],peak_rss_kib=result['peak_rss_kib'])),flush=True)
if __name__=='__main__':main()
