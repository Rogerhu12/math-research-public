#!/usr/bin/env python3
"""Signed low46 Duhamel response to the complete mean-completed linear centre.

Consumes the same original 3940 saved homogeneous leaves without new ODE.
The complete numerator, mean and infinite inverse tail of N(C) are retained.
This is the zero-initial first source response, not a nonlinear solution tube.
Author: exact_closure (GPT-6 Astra Pro; AI-assisted), 2026-11-13.
"""
import argparse, hashlib, importlib.util, json, resource, time
from fractions import Fraction as F
from pathlib import Path

BASE=Path('/workspace/scratch/d1aa462cfc02/exact-work')
SIGNED=BASE/'2026-11-13-exact-resume-outer8to7-signed-low46-v1.py'
SIGNED_SHA='d34c1e1a7c5933921d5aceeab159eab558b7198af8ee68eca86d4aca407bc0ab'
SOURCE_SHA='8170b161ab7a0bc40acc6b8adb2f2e994cc028cf95d942fb85f3adacf7ab3804'
def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
if sha(SIGNED)!=SIGNED_SHA:raise ArithmeticError('Immutable original signed helper')
spec=importlib.util.spec_from_file_location('same_signed',SIGNED)
old=importlib.util.module_from_spec(spec);spec.loader.exec_module(old)
from flint import arb,ctx
load,ball,record,upper,caprec,exact_q=old.load,old.ball,old.record,old.upper,old.caprec,old.exact_q
MODES=list(range(2,93,2))
PRIMARY_PINS={9:'c19d33f403f42c0b98ada4572aa58f860f17d922cd5e353d680d477d75640c07',8:'062a9ed72fc3a1841691bc8b7b785f8aaa75fb3694501a5ec38e6267e23cc332',7:'90f6ef971b581bd30b73cbcc9085791bb0cf7f27c3e5341e96d6e85fed1cbd72'}
def up(x):return upper(caprec(x))
def matvec(A,v):return [sum((A[i][j]*v[j] for j in range(2)),arb(0)) for i in range(2)]
def allfinite(v):return all(z.is_finite() for z in v)

def main():
 ap=argparse.ArgumentParser(description=__doc__)
 ap.add_argument('--source',required=True,type=Path)
 ap.add_argument('--source-resource',required=True,type=Path)
 ap.add_argument('--out-prefix',required=True,type=Path)
 ap.add_argument('--rss-kib',type=int,default=98304)
 args=ap.parse_args();start=time.monotonic();ctx.prec=256;ctx.threads=1
 prefix=str(args.out_prefix)
 if any(args.out_prefix.parent.glob(args.out_prefix.name+'*')):raise FileExistsError('Fresh source-response output required')
 args.out_prefix.parent.mkdir(parents=True,exist_ok=True)
 categories={}
 def gate(k,v):
  if not bool(v):raise ArithmeticError('Unpaid complete Duhamel gate: '+k)
  categories[k]=categories.get(k,0)+1
 def guard():
  if resource.getrusage(resource.RUSAGE_SELF).ru_maxrss>args.rss_kib:raise MemoryError('Unchanged96MiB guard')
 def identified(p):return dict(path=str(p),sha256=sha(p))
 def rows(entries):
  for ent in entries:
   gate('saved_chunk_sha',sha(ent['path'])==ent['sha256'])
   packet=load(ent['path'])
   for row in packet['rows']:yield row
   del packet
 source=load(args.source)
 gate('actual_complete_source_formal_zero',old.resource_gate(load(args.source_resource)))
 gate('actual_source_algorithm_pin',source['source_sha256']==SOURCE_SHA)
 gate('actual_complete_source_all_gates',source['all_gates'] and all(source['gates'].values()))
 gate('actual_complete_source_3940_leaves',source['total_leaves']==3940 and source['cell_leaf_counts']=={'9':1377,'8':1316,'7':1247})
 gate('source_complete_mean_inverse_retained',source['same_true_linear_centre_with_complete_mean'] and source['full_source_zero_kept_before_full_inverse'] and source['complete_infinite_inverse_tail'])
 gate('source_exact_sigma',source['source_sigma']=='1/64')
 fm=load(old.FROZEN/'manifest.json')
 gate('original_background_manifest',sha(old.FROZEN/'manifest.json')==old.MANIFEST)
 for ent in fm['source_files']:gate('original_background_source_pin',sha(ent['path'])==ent['sha256'])
 ready_path=Path(fm['inputs']['ready']['path'])
 gate('original_background_ready_pin',sha(ready_path)==fm['inputs']['ready']['sha256'])
 ready={k:old.read_field(ready_path,k) for k in ('rationalDeepModel','shallowSourceParameters')}
 h=old.SourceValues(ready);del ready;kernel=old.PositiveKernels(h,12,92)
 h.cells={n:kernel.source_cell(n) for n in (9,8,7)}
 primaries={};inputs={'source':identified(args.source),'source_resource':identified(args.source_resource)}
 for n in (9,8,7):
  p=BASE/f'outer{n}-signed-low46-r1.json';r=BASE/f'outer{n}-signed-low46-run1-resource.json';data=load(p)
  gate('original_cell_pin',sha(p)==PRIMARY_PINS[n]);gate('original_cell_actual_formal_zero',old.resource_gate(load(r)))
  gate('original_cell_all_gates',data['all_gates'] and all(data['gates'].values()))
  gate('same_tracezero_coordinates',data['config']['coordinates']=='Y=sqrt(r*w^3)*(P_sine,K_cosine)')
  gate('same_complete_source_input',source['inputs'][f'cell{n}']['sha256']==PRIMARY_PINS[n])
  inputs[f'cell{n}']=identified(p);inputs[f'cell{n}_resource']=identified(r);primaries[n]=data
 gate('same_fixed_centre',primaries[9]['input_rows']==primaries[8]['input_rows']==primaries[7]['input_rows'])
 sigma=arb(1)/64;weights=[(1+m)*(m*sigma).exp() for m in MODES]
 srciter=iter(rows(source['source_parts']));Y=[[arb(0),arb(0)] for m in MODES]
 cells=[];checkpoints=[];total=0;wide_tail_improved=0
 peak_partial=arb(0);peak_peano=arb(0);minimum_det=arb(1)
 for n in (9,8,7):
  cellcaps=[[arb(0),arb(0)] for m in MODES];sourcecaps=[[arb(0),arb(0)] for m in MODES]
  leafmax=arb(0);leafwhere=None;segments=[];last=F(0);segment=-1;count=0
  segcaps=[[arb(0),arb(0)] for m in MODES];segcount=0
  for row in rows(primaries[n]['profile_chunks']):
   src=next(srciter);ident={k:row[k] for k in ('cell','segment','left','right')}
   gate('complete_identical_leaf_order',all(src[k]==row[k] for k in ident))
   j=row['segment'];lo=F(row['left']);hi=F(row['right']);dx=exact_q(hi-lo)
   if j!=segment:
    gate('complete_previous_segment',segment==-1 or last==1)
    gate('actual_segment_order',j==segment+1);segment=j;last=F(0);segcount=0
    segcaps=[[arb(0),arb(0)] for m in MODES]
   gate('complete_original_leaf_coverage',lo==last and hi>lo);last=hi;total+=1;count+=1;segcount+=1
   gate('all46_signed_flow_modes',[z['mode'] for z in row['local_signed_flow']]==MODES)
   gate('all46_complete_source_modes',[z['mode'] for z in src['low46_signed_source_rows']]==MODES)
   rr=ball(row['whole_radius']);w=ball(src['actual_original_w']);rx=ball(row['radius_x']);ell=ball(row['log_w_x'])
   # Original whole-leaf |w*ell| enclosures may have a negative lower
   # endpoint although the true derivative is strictly positive. Retain
   # the independent exact background lower bound, not a false ball sign.
   background=h.source_point(h.cells[n]['segments'][j],exact_q(lo).union(exact_q(hi)))
   rxlo=(h.alpha*background['ro_x']/(1+w*w)).lower()
   rxup=rx.upper()
   gate('positive_complete_background',rr>0 and w>0 and h.alpha>0 and rxlo>0 and rxup>=rxlo)
   rx=old.intersect(rx,rxlo.union(rxup))
   gate('same_radius_derivative_interval_finite',rx.is_finite())
   den=(rr*w**3).sqrt();s=rx/rr;ss=dx*s;ee=dx*ell;dd=(ee-ss)/2
   B=ball(row['balance']);q=ball(row['integral_norm']);gate('original_partial_neumann_domain',B>0 and 0<=q<1)
   err=up(q*q/(1-q));rem=[[err,up(err/B)],[up(err*B),err]]
   d=up(abs(dd));one=1-d;gate('suffix_comparison_positive_diagonal',one>0)
   tau=exact_q(F(src['source_wide_sigma']));rhow=upper(src['inverse_wide_sigma_norm'])
   gate('source_wide_analytic_domain',tau>=sigma and 0<=rhow<1)
   wide_tails={name:up(upper(src['materials'][name]['complete_all_frequency_wide_source'])*rhow**33) for name in ('s','ell')}
   gate('all_complete_wide_inverse_tails_finite',allfinite(list(wide_tails.values())))
   wr=h.source_point(h.cells[n]['segments'][j],exact_q(hi))['w'];re=ball(row['radius_right'])
   denend=(re*wr**3).sqrt();gate('positive_true_endpoint_conversion',denend>0)
   leafcaps=[];endpoint=[]
   for k,m in enumerate(MODES):
    data=src['low46_signed_source_rows'][k];coeff={}
    for name in ('s','ell'):
     saved=ball(data[name]['complete_cosine_coefficient']);finite=ball(data[name]['finite32_cosine_coefficient'])
     oldtail=upper(data[name]['shared_tail_to_this_coefficient_upper'])
     newtail=min(oldtail,up(wide_tails[name]*(-m*tau).exp()))
     if newtail<oldtail:wide_tail_improved+=1
     coeff[name]=old.intersect(saved,old.add_error(finite,newtail))
     gate('complete_material_source_finite',coeff[name].is_finite())
    force=den*(s*coeff['s']+ell*coeff['ell']);force_mass=up(dx*abs(force))
    a=up(m*abs(ss));b=up(m*abs(ee));det=one*one-a*b
    gate('suffix_positive_Peano_resolvent',det>0);minimum_det=min(minimum_det,det.lower())
    R12=up(a/det);R22=up((d*one+a*b)/det)
    gate('complete_suffix_remainders_finite',allfinite([R12,R22,force_mass]))
    J=[old.add_error(arb(0),up(R12*force_mass)),old.add_error(dx*force,up(R22*force_mass))]
    Jpartial=[J[0],old.add_error(arb(0).union(dx)*force,up(R22*force_mass))]
    M=[[dd,-m*ss],[-m*ee,-dd]]
    partial=[[old.add_error(arb(0).union(M[i][t])+(1 if i==t else 0),rem[i][t]) for t in range(2)] for i in range(2)]
    whole0=matvec(partial,Y[k]);whole=[(whole0[i]+Jpartial[i])/den for i in range(2)]
    T=[[ball(v) for v in line] for line in row['local_signed_flow'][k]['matrix']]
    advanced=matvec(T,Y[k]);Y[k]=[advanced[i]+J[i] for i in range(2)]
    point=[v/denend for v in Y[k]]
    gate('complete_response_every_entry_finite',allfinite(whole+Y[k]+point))
    caps=[up(abs(v)) for v in whole];leafcaps.append(caps)
    for i in range(2):
     cellcaps[k][i]=max(cellcaps[k][i],caps[i]);segcaps[k][i]=max(segcaps[k][i],caps[i])
     sourcecaps[k][i]=max(sourcecaps[k][i],up(abs(Jpartial[i])/den))
    endpoint.append(dict(mode=m,tracezero_Y=[record(v) for v in Y[k]],physical_PK=[record(v) for v in point]))
    peak_partial=max(peak_partial,up(q));peak_peano=max(peak_peano,R12,R22)
   leafmass=up(sum((weights[k]*sum(leafcaps[k],arb(0)) for k in range(46)),arb(0)))
   if leafmass>leafmax:leafmax=leafmass;leafwhere=ident
   if hi==1:
    segmass=up(sum((weights[k]*sum(segcaps[k],arb(0)) for k in range(46)),arb(0)))
    checkpoint=dict(schema='same-original-complete-centre-Duhamel-segment-v1',cell=n,segment=j,leaves=segcount,
      source_primary_sha256=sha(args.source),source_algorithm_sha256=SOURCE_SHA,
      endpoint_modes=endpoint,whole_segment_radial_first_strong_mass=caprec(segmass),
      whole_segment_component_caps=[dict(mode=m,P=caprec(segcaps[k][0]),K=caprec(segcaps[k][1])) for k,m in enumerate(MODES)],
      zero_initial_at_node10=True,complete_source_only=True,nonlinear_feedback_paid=False,infinite_initial_field_paid=False)
    entry=old.dump(prefix+f'-cell{n:02d}-segment{j}.json.gz',checkpoint);checkpoints.append(entry);segments.append(entry)
   if total%100==0:print(json.dumps(dict(event='actual_complete_Duhamel',leaves=total,cell=n,elapsed_seconds=time.monotonic()-start,peak_rss_kib=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss,block_mass=str(leafmax))),flush=True)
   guard()
  expected=primaries[n]['counts']['taylor']+primaries[n]['counts']['root_brackets']
  gate('all_original_cell_leaves',count==expected and segment==8 and last==1 and len(segments)==9)
  mass=up(sum((weights[k]*sum(cellcaps[k],arb(0)) for k in range(46)),arb(0)))
  cells.append(dict(cell=n,leaves=count,source_sigma='1/64',whole_cell_radial_first_strong_mass=caprec(mass),
    whole_cell_component_caps=[dict(mode=m,P=caprec(cellcaps[k][0]),K=caprec(cellcaps[k][1])) for k,m in enumerate(MODES)],
    whole_leaf_block_max_strong_mass=caprec(leafmax),block_max_where=leafwhere,
    original_eta_example='1/16',within_eta_for_this_first_response_only=bool(mass<arb(1)/16),
    endpoint_modes=endpoint,segments=segments))
  print(json.dumps(dict(event='complete_cell_source_response',cell=n,radial_first_mass=str(mass),block_max_mass=str(leafmax),within_eta=bool(mass<arb(1)/16))),flush=True)
 gate('all3940_original_leaves',total==3940)
 try:next(srciter);raise ArithmeticError('Unused source leaf')
 except StopIteration:pass
 summary=dict(schema='same-original9to7-complete-centre-low46-Duhamel-v1',author='exact_closure (GPT-6 Astra Pro; AI-assisted)',
  source_sha256=sha(__file__),signed_helper_sha256=SIGNED_SHA,inputs=inputs,precision_bits=ctx.prec,
  all_gates=True,gates={k:True for k in categories},gate_count=sum(categories.values()),gate_categories=categories,
  total_leaves=total,cells=cells,checkpoints=checkpoints,wide_inverse_tail_improvement_count=wide_tail_improved,
  minimum_suffix_resolvent_determinant=record(minimum_det),maximum_saved_partial_integral_norm=caprec(peak_partial),maximum_suffix_entry_remainder=caprec(peak_peano),
  coordinates='Y=sqrt(r*w^3)*(P_sine,K_cosine)',source_x_identity='e2*sqrt(r*w^3)*(s*N_s+ell*N_ell)',
  complete_mean_and_infinite_inverse_retained=True,finite_response_modes=MODES,zero_initial_particular_at_node10=True,
  no_new_ODE=True,new_interval_source_integration=True,not_a_nonlinear_solution_tube=True,
  complete_infinite_response_or_initial_strip_extension_claimed=False,
  elapsed_seconds=time.monotonic()-start,peak_rss_kib=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)
 entry=old.dump(prefix+'-summary.json.gz',summary)
 print(json.dumps(dict(all_gates=True,gate_count=summary['gate_count'],primary=entry,elapsed_seconds=summary['elapsed_seconds'],peak_rss_kib=summary['peak_rss_kib'])),flush=True)

if __name__=='__main__':main()
