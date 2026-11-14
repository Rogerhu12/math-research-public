#!/usr/bin/env python3
"""Source-position ordered all-infinite particular tails, original cells9..7.

Actual background panels and actual complete source leaves are overlaid
without new ODE or background integration. Signed complete-panel diagonal
costs are retained only on full future panels; a current partial panel gets
no free negative contribution. All displayed cutoffs include infinity.
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
MODES=[94,96,98,106,114,130,186,194,258,514,1026,2050,4098,8192,34816]
MAT_PINS={9:'78dc58b9c8173e1ba5d4dafc8fc8225ab5c987411b100b99f15ea476929ae82e',8:'8ab1f327963f0c2a7970ec3e9a8146aa5780ede17294cefc52744eaea63001ec',7:'3e627c279d490dcf79cb06edc1985402717e42a47836c487f20674a705ae8e8c'}
def up(x):return upper(caprec(x))
def plog(x):
 if not x>0:raise ArithmeticError('Positive frame ratio')
 return max(arb(0),x.log().upper())
def main():
 ap=argparse.ArgumentParser(description=__doc__);ap.add_argument('--out-prefix',type=Path,required=True);ap.add_argument('--rss-kib',type=int,default=98304)
 a=ap.parse_args();start=time.monotonic();ctx.prec=256;ctx.threads=1;prefix=str(a.out_prefix)
 if any(a.out_prefix.parent.glob(a.out_prefix.name+'*')):raise FileExistsError('Fresh ordered source ledger required')
 a.out_prefix.parent.mkdir(parents=True,exist_ok=True);counts={}
 def gate(k,v):
  if not bool(v):raise ArithmeticError('Unpaid ordered tail gate '+k)
  counts[k]=counts.get(k,0)+1
 def guard():
  if resource.getrusage(resource.RUSAGE_SELF).ru_maxrss>a.rss_kib:raise MemoryError('Unchanged96MiB guard')
 def ident(p):return dict(path=str(p),sha256=sha(p))
 def stream(entries):
  for ent in entries:
   gate('saved_proof_part_pin',sha(ent['path'])==ent['sha256']);packet=load(ent['path'])
   for row in packet['rows']:yield row
   del packet
 sp=BASE/'outer9to7-centre-source-r2-summary.json.gz';sr=BASE/'outer9to7-centre-source-run2-resource.json';src=load(sp)
 gate('same_actual_complete_source',sha(sp)=='e4e4bf14d08cb6a6221d31e2da25fb315f9d342bc88d12cff7aa8ef775b020d2')
 gate('complete_source_formal0',old.resource_gate(load(sr)) and src['all_gates'] and all(src['gates'].values()))
 gate('complete_mean_and_inverse',src['complete_infinite_inverse_tail'] and src['same_true_linear_centre_with_complete_mean'] and src['full_source_zero_kept_before_full_inverse'])
 inputs={'complete_source':ident(sp),'complete_source_resource':ident(sr)};groups=[];offset=0
 for cell in (9,8,7):
  p=BASE/f'outer-cell{cell}-material-r1-manifest.json';r=BASE/f'outer-cell{cell}-material-r1-resource.json';mat=load(p)
  gate('same_background_material',sha(p)==MAT_PINS[cell] and mat['cell']==cell)
  gate('original_material_formal0',old.resource_gate(load(r)) and all(mat['checks'].values()))
  gate('all_nine_original_segments',[v['source_segment'] for v in mat['groups']]==list(range(9)))
  inputs[f'cell{cell}_material']=ident(p);inputs[f'cell{cell}_resource']=ident(r)
  for group in mat['groups']:
   groups.append(dict(cell=cell,segment=group['source_segment'],first_index=offset,**group));offset+=group['panels']
 gate('all14069_original_panels',offset==14069)
 # Backward exact positive recurrence for the maximum future response.
 # Z(M) bounds start-of-next-panel to every later point, in that frame.
 Z=[arb(0) for M in MODES];nextb=None;future_bmax=arb(0);gamma_tail=arb(0)
 kernel_parts=[];total=0;minimum=arb(1)/256
 for group in reversed(groups):
  p=Path(group['path']);gate('original_panel_data_pin',sha(p)==group['sha256'])
  material=[];last=F(0)
  for row in iter_array(p,'panels'):
   lo,hi=F(row['x_left']),F(row['x_right']);gate('complete_original_panel_coverage',lo==last and hi>lo and row['segment']==group['segment']);last=hi
   rr,rx,ell,w=[ball(row[k]) for k in ('radius','radius_x','log_w_x','w')]
   gate('original_positive_finite_background',all(v.is_finite() for v in (rr,rx,ell,w)) and rr>0 and rx>0 and w>0)
   dx=exact_q(hi-lo);s=rx/rr;sl,su,el,eu=s.lower(),s.upper(),ell.lower(),ell.upper()
   square=max(minimum*minimum,(eu/su).upper(),(-(el+eu)/(sl+su)).upper());b=up(square.sqrt())
   gamma=up(abs(s*b+ell/b)/2*dx);diagonal=(max((-s-ell).upper(),(-2*ell).upper())*dx).upper()
   material.append((lo,hi,b,gamma,diagonal,up(s),up(abs(ell))))
  gate('complete_panel_group',last==1 and len(material)==group['panels'])
  buffer=[]
  def flush():
   if buffer:
    packet=list(reversed(buffer));first=packet[0]['index'];ent=old.dump(prefix+f'-kernels-{first:05d}.json.gz',dict(schema='same-original-ordered-suffix-tail-kernel-part-v1',minimum_modes=MODES,rows=packet))
    ent['first_index']=first;ent['last_index']=packet[-1]['index'];kernel_parts.append(ent);buffer.clear()
  for local in range(len(material)-1,-1,-1):
   lo,hi,b,gamma,diagonal,sup_s,sup_ell=material[local]
   jump=plog(b/nextb) if nextb is not None else arb(0)
   gamma_tail=up(gamma_tail+gamma);future_bmax=max(future_bmax,b)
   arbitrary=[];starts=[]
   for k,M in enumerate(MODES):
    rate=(M*gamma+diagonal).upper();future=up(jump+Z[k])
    arbitrary.append(up(max(arb(0),rate)+future))
    starts.append(up(max(arb(0),(rate+future).upper())))
   Z=starts;nextb=b;total+=1
   gate('all_suffix_kernel_values_finite',all(v.is_finite() and v>=0 for v in arbitrary+starts+[gamma_tail,future_bmax]))
   buffer.append(dict(index=group['first_index']+local,cell=group['cell'],segment=group['segment'],left=str(lo),right=str(hi),
     frame=caprec(b),future_maximum_frame=caprec(future_bmax),complete_remaining_phase=caprec(gamma_tail),
     source_s_upper=caprec(sup_s),source_absolute_ell_upper=caprec(sup_ell),
     signed_full_panel_diagonal=record(diagonal),full_panel_phase=caprec(gamma),forward_next_frame_jump=caprec(jump),
     every_source_position_peak_log_by_minimum_mode=[caprec(v) for v in arbitrary],
     left_endpoint_peak_log_by_minimum_mode=[caprec(v) for v in starts]))
   if len(buffer)>=32:flush()
   if total%128==0:guard()
  flush();del material
  print(json.dumps(dict(event='ordered_suffix_group',cell=group['cell'],segment=group['segment'],panels_processed=total,elapsed_seconds=time.monotonic()-start)),flush=True)
 gate('complete_backward_suffix_coverage',total==14069)
 kernel_parts.sort(key=lambda v:v['first_index']);last=0
 for ent in kernel_parts:
  gate('complete_saved_kernel_order',ent['first_index']==last);last=ent['last_index']+1
 gate('complete_saved_kernel_count',last==14069)
 # Exact overlay of two independently complete original partitions.
 kernels=iter(stream(kernel_parts));current=next(kernels);fine_seen=0;source_seen=0;pieces=0
 totals=[arb(0) for M in MODES];bycell={n:[arb(0) for M in MODES] for n in (9,8,7)}
 largest=[dict(cap=arb(0),where=None) for M in MODES];minimum_reserve=None
 sigma=arb(1)/64
 for source in stream(src['source_parts']):
  n,j=source['cell'],source['segment'];lo,hi=F(source['left']),F(source['right']);cursor=lo;source_seen+=1
  tau=exact_q(F(source['source_wide_sigma']));As=upper(source['materials']['s']['complete_all_frequency_wide_source']);Ae=upper(source['materials']['ell']['complete_all_frequency_wide_source'])
  leaf_total=[arb(0) for M in MODES]
  while cursor<hi:
   gate('same_exact_source_and_material_domain',current['cell']==n and current['segment']==j)
   fl,fr=F(current['left']),F(current['right']);gate('exact_overlay_no_gap',fl<=cursor<fr)
   end=min(hi,fr);dx=exact_q(end-cursor);gate('positive_overlay_length',end>cursor)
   remaining=upper(current['complete_remaining_phase']);reserve=(tau-sigma-remaining).lower()
   gate('all_tail_frequency_monotonicity',reserve*(1+MODES[0])>1)
   minimum_reserve=reserve if minimum_reserve is None else min(minimum_reserve,reserve)
   b=upper(current['frame']);bmax=upper(current['future_maximum_frame'])
   factor=up(2*max(arb(1),bmax)/b)
   mass=up(dx*(upper(current['source_s_upper'])*As+upper(current['source_absolute_ell_upper'])*Ae))
   for k,M in enumerate(MODES):
    peak=upper(current['every_source_position_peak_log_by_minimum_mode'][k])
    term=up(factor*mass*(1+M)*(peak-M*(tau-sigma)).exp())
    gate('every_complete_infinite_response_piece_finite',term.is_finite() and term>=0)
    totals[k]=up(totals[k]+term);bycell[n][k]=up(bycell[n][k]+term);leaf_total[k]=up(leaf_total[k]+term)
   pieces+=1;cursor=end
   if end==fr:
    fine_seen+=1
    try:current=next(kernels)
    except StopIteration:current=None
  for k in range(len(MODES)):
   if leaf_total[k]>largest[k]['cap']:largest[k]=dict(cap=leaf_total[k],where={z:source[z] for z in ('cell','segment','left','right','source_wide_sigma')})
  if source_seen%200==0:
   print(json.dumps(dict(event='ordered_source_overlay',source_leaves=source_seen,overlap_pieces=pieces,tail94=str(totals[0]),elapsed_seconds=time.monotonic()-start)),flush=True);guard()
 gate('all_original_source_leaves_consumed',source_seen==3940)
 gate('all_original_fine_materials_consumed',fine_seen==14069 and current is None)
 oldp=BASE/'outer9to7-high-particular-r1.json';oldr=BASE/'outer9to7-high-particular-run1-resource.json';prior=load(oldp)
 gate('prior_complete_high_formal0',old.resource_gate(load(oldr)) and sha(oldp)=='cbe554421c2f74ee99934cd1a59db21416202a0093c23d04ea9f8a22855db69c')
 inputs['previous_all_high']=ident(oldp);inputs['previous_all_high_resource']=ident(oldr)
 estimates=[]
 for k,M in enumerate(MODES):
  previous=next((upper(v['whole_original9to7_radial_first_strong_sigma1over64']) for v in prior['estimates'] if v['minimum_physical_even_mode']==M),None)
  bound=min(totals[k],previous) if previous is not None else totals[k]
  estimates.append(dict(minimum_physical_even_mode=M,ordered_complete_tail_upper=caprec(totals[k]),complete_tail_intersect_prior_upper=caprec(bound),
    log2_upper=record((bound.log()/arb(2).log()).upper()),below_eta1over16=bool(bound<arb(1)/16),
    source_cell_contributions={str(n):caprec(bycell[n][k]) for n in (9,8,7)},largest_source_leaf_contribution=dict(upper=caprec(largest[k]['cap']),where=largest[k]['where'])))
 out=dict(schema='same-original9to7-source-position-ordered-complete-infinite-particular-v1',author='exact_closure (GPT-6 Astra Pro; AI-assisted)',source_sha256=sha(__file__),inputs=inputs,
  minimum_modes=MODES,precision_bits=ctx.prec,total_original_source_leaves=source_seen,total_original_material_panels=fine_seen,exact_partition_overlap_pieces=pieces,
  kernel_parts=kernel_parts,minimum_source_strip_reserve=record(minimum_reserve),estimates=estimates,
  source_x_units='f=s*N_s+ell*N_ell in physical K equation; source frame factor1/b, output separate-radial-sup factor2max(1,b)',
  zero_initial_particular=True,complete_mean_inverse_and_infinite_source=True,signed_future_diagonal_only_on_complete_panels=True,
  unknown_infinite_entry_and_nonlinear_feedback_unpaid=True,no_new_ODE_or_background_quadrature=True,
  all_gates=True,gates={k:True for k in counts},gate_count=sum(counts.values()),gate_categories=counts,elapsed_seconds=time.monotonic()-start,peak_rss_kib=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)
 ent=old.dump(prefix+'-summary.json.gz',out)
 print(json.dumps(dict(all_gates=True,primary=ent,gate_count=out['gate_count'],elapsed_seconds=out['elapsed_seconds'],peak_rss_kib=out['peak_rss_kib'])),flush=True)
if __name__=='__main__':main()
