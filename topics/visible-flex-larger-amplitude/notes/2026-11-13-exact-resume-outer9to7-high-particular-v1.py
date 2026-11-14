#!/usr/bin/env python3
"""All-infinite high particular response of the same complete centre source.

Reuses original background material panels and the completed source packet.
Every suffix uses nonnegative diagonal and frame-jump charges. No entry-strip
upgrade or nonlinear solution is inferred from the finite centre's source.
Author: exact_closure (GPT-6 Astra Pro; AI-assisted), 2026-11-13.
"""
import argparse,hashlib,importlib.util,json,resource,time
from fractions import Fraction as F
from pathlib import Path
BASE=Path('/workspace/scratch/d1aa462cfc02/exact-work')
SIGNED=BASE/'2026-11-13-exact-resume-outer8to7-signed-low46-v1.py'
def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
if sha(SIGNED)!='d34c1e1a7c5933921d5aceeab159eab558b7198af8ee68eca86d4aca407bc0ab':raise ArithmeticError('Original helper pin')
spec=importlib.util.spec_from_file_location('same_original',SIGNED);old=importlib.util.module_from_spec(spec);spec.loader.exec_module(old)
from flint import arb,ctx
from closure_split_joint_io import iter_array
load,ball,record,caprec,upper,exact_q=old.load,old.ball,old.record,old.caprec,old.upper,old.exact_q
def up(v):return upper(caprec(v))
def plog(v):
 if not v>0:raise ArithmeticError('Positive frame ratio')
 return max(arb(0),v.log().upper())
MAT_PINS={9:'78dc58b9c8173e1ba5d4dafc8fc8225ab5c987411b100b99f15ea476929ae82e',8:'8ab1f327963f0c2a7970ec3e9a8146aa5780ede17294cefc52744eaea63001ec',7:'3e627c279d490dcf79cb06edc1985402717e42a47836c487f20674a705ae8e8c'}
def main():
 ap=argparse.ArgumentParser(description=__doc__);ap.add_argument('--out',type=Path,required=True);ap.add_argument('--rss-kib',type=int,default=98304)
 args=ap.parse_args();start=time.monotonic();ctx.prec=256;ctx.threads=1
 if args.out.exists():raise FileExistsError('Fresh all-infinite particular ledger required')
 counts={}
 def gate(k,v):
  if not bool(v):raise ArithmeticError('Unpaid high particular gate '+k)
  counts[k]=counts.get(k,0)+1
 sourcep=BASE/'outer9to7-centre-source-r2-summary.json.gz';sourcer=BASE/'outer9to7-centre-source-run2-resource.json';src=load(sourcep)
 gate('same_complete_actual_source',sha(sourcep)=='e4e4bf14d08cb6a6221d31e2da25fb315f9d342bc88d12cff7aa8ef775b020d2')
 gate('actual_complete_source_formal0',old.resource_gate(load(sourcer)) and src['all_gates'] and all(src['gates'].values()))
 tau=arb(1)/2;sigma=arb(1)/64
 gate('uniform_source_half_strip',all(F(v)>=F(1,2) for v in src['minimum_actual_source_wide_sigmas'].values()))
 As=upper(src['strongest_per_leaf_source_bounds']['s_full_wide_source']['upper'])
 Ae=upper(src['strongest_per_leaf_source_bounds']['ell_full_wide_source']['upper'])
 inputs={'complete_source':{'path':str(sourcep),'sha256':sha(sourcep)},'complete_source_resource':{'path':str(sourcer),'sha256':sha(sourcer)}}
 minimum=arb(1)/256;previous=None;bmin=None;bmax=arb(0)
 phase=arb(0);diag=arb(0);jumps=arb(0);Sint=arb(0);Eint=arb(0);total=0;cells=[]
 for n in (9,8,7):
  mp=BASE/f'outer-cell{n}-material-r1-manifest.json';rp=BASE/f'outer-cell{n}-material-r1-resource.json';mat=load(mp)
  gate('original_material_pin',sha(mp)==MAT_PINS[n]);gate('original_material_formal0',old.resource_gate(load(rp)))
  gate('all_material_source_gates',all(mat['checks'].values()) and mat['cell']==n)
  gate('original_background_identity',set(mat['original_metadata']['input_hashes'].values())=={'563a99973230a7f15d1c1ba8537edae34bc02158a0cfff90160d37f57e3ab2f6','28d491b998174029a80daf41e9365de6ab2c54757419de7b64f54445047b717f'})
  gate('all_nine_segments',[z['source_segment'] for z in mat['groups']]==list(range(9)))
  inputs[f'cell{n}_material']={'path':str(mp),'sha256':sha(mp)};inputs[f'cell{n}_resource']={'path':str(rp),'sha256':sha(rp)}
  nc=0;cp=arb(0);cd=arb(0);cj=arb(0);cs=arb(0);ce=arb(0)
  for group in mat['groups']:
   p=Path(group['path']);gate('original_panel_sha',sha(p)==group['sha256']);last=F(0);ng=0
   for row in iter_array(p,'panels'):
    lo,hi=F(row['x_left']),F(row['x_right']);gate('complete_original_panel_order',lo==last and hi>lo and row['segment']==group['source_segment']);last=hi
    rr,rx,ell,w=[ball(row[k]) for k in ('radius','radius_x','log_w_x','w')]
    gate('positive_complete_background',rr>0 and rx>0 and w>0 and w.upper()<=arb(1)/2)
    gate('all_background_entries_finite',all(v.is_finite() for v in (rr,rx,ell,w)))
    dx=exact_q(hi-lo);s=rx/rr;sl,su,el,eu=s.lower(),s.upper(),ell.lower(),ell.upper()
    sq=max(minimum*minimum,(eu/su).upper(),(-(el+eu)/(sl+su)).upper());b=up(sq.sqrt())
    gamma=up(abs(s*b+ell/b)/2);d=max(arb(0),(-s-ell).upper(),(-2*ell).upper())
    jump=plog(previous/b) if previous is not None else arb(0);previous=b
    bmin=b if bmin is None else min(bmin,b);bmax=max(bmax,b)
    cp=up(cp+gamma*dx);cd=up(cd+d*dx);cj=up(cj+jump);cs=up(cs+s*dx);ce=up(ce+abs(ell)*dx)
    gate('full_suffix_nonnegative_charges',b>=minimum and gamma>=0 and d>=0 and jump>=0)
    ng+=1;nc+=1;total+=1
    if total%256==0 and resource.getrusage(resource.RUSAGE_SELF).ru_maxrss>args.rss_kib:raise MemoryError('Unchanged96MiB bound')
   gate('whole_original_segment',last==1 and ng==group['panels'])
  gate('whole_original_cell',nc==mat['panels'])
  phase=up(phase+cp);diag=up(diag+cd);jumps=up(jumps+cj);Sint=up(Sint+cs);Eint=up(Eint+ce)
  cells.append(dict(cell=n,original_panels=nc,phase=caprec(cp),nonnegative_diagonal=caprec(cd),nonnegative_forward_frame_jumps=caprec(cj),s_integral=caprec(cs),absolute_ell_integral=caprec(ce)))
 delta=(tau-sigma-phase).lower();gate('positive_full_source_strip_reserve',delta>0)
 D=up(diag+jumps);source_mass=up(As*Sint+Ae*Eint)
 conversion=up(2*max(arb(1),bmax)/bmin)
 prefactor=up(conversion*D.exp()*source_mass)
 gate('finite_all_frequency_prefactor',prefactor.is_finite() and prefactor>=0)
 estimates=[]
 for M in (8192,34816):
  gate('tail_sup_monotone',delta*(1+M)>1)
  bound=up(prefactor*(1+M)*(-M*delta).exp())
  gate('complete_positive_infinite_tail_finite',bound.is_finite() and bound>0)
  estimates.append(dict(minimum_physical_even_mode=M,whole_original9to7_radial_first_strong_sigma1over64=caprec(bound),bound_log2_upper=record((bound.log()/arb(2).log()).upper()),below_2minus40=bool(bound<arb((1,-40)))))
 gate('all_original_14069_panels',total==4985+4697+4387)
 out=dict(schema='same-original9to7-complete-infinite-high-particular-source-response-v1',author='exact_closure (GPT-6 Astra Pro; AI-assisted)',source_sha256=sha(__file__),inputs=inputs,
  actual_source_leaf_counts=src['cell_leaf_counts'],actual_source_total_leaves=3940,original_material_panels=total,precision_bits=ctx.prec,
  source_uniform_strip='1/2',output_strip='1/64',source_wide_s_block_max=caprec(As),source_wide_ell_block_max=caprec(Ae),
  cells=cells,complete_phase=caprec(phase),complete_nonnegative_diagonal=caprec(diag),complete_nonnegative_frame_jumps=caprec(jumps),
  minimum_frame=record(bmin),maximum_frame=record(bmax),all_suffix_physical_conversion=caprec(conversion),complete_material_source_integral=caprec(source_mass),
  source_strip_reserve=record(delta),estimates=estimates,
  full_complete_mean_inverse_and_all_infinite_source=True,zero_initial_particular=True,no_new_ODE_or_background_quadrature=True,
  whole_radial_first_output_norm=True,unknown_entry_infinite_homogeneous_field_not_paid=True,nonlinear_feedback_or_solution_tube_not_claimed=True,
  all_gates=True,gates={k:True for k in counts},gate_count=sum(counts.values()),gate_categories=counts,
  elapsed_seconds=time.monotonic()-start,peak_rss_kib=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)
 ent=old.dump(args.out,out)
 print(json.dumps(dict(all_gates=True,primary=ent,gate_count=out['gate_count'],estimates=[{'m':r['minimum_physical_even_mode'],'bound_log2':r['bound_log2_upper']} for r in estimates],elapsed_seconds=out['elapsed_seconds'],peak_rss_kib=out['peak_rss_kib'])),flush=True)
if __name__=='__main__':main()
