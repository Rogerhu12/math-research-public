#!/usr/bin/env python3
"""New signed modes94..184: full centre source and zero-entry Duhamel.

The saved low46 geometry/centre and complete mean/inverse tails are reused.
Only the46 previously unpaid homogeneous modes are integrated, with the
original precision256/order24/remainder100/root160 gates. Original leaves
may be subdivided; no tolerance or physical input is weakened.
Author: exact_closure (GPT-6 Astra Pro; AI-assisted), 2026-11-13.
"""
import argparse,hashlib,importlib.util,json,resource,time
from fractions import Fraction as F
from pathlib import Path
BASE=Path('/workspace/scratch/d1aa462cfc02/exact-work')
SRC=BASE/'2026-11-13-exact-resume-outer9to7-complete-centre-source-v2.py'
SOURCE_SHA='8170b161ab7a0bc40acc6b8adb2f2e994cc028cf95d942fb85f3adacf7ab3804'
def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
if sha(SRC)!=SOURCE_SHA:raise ArithmeticError('Original complete centre source algorithm')
spec=importlib.util.spec_from_file_location('complete_source',SRC);srcmod=importlib.util.module_from_spec(spec);spec.loader.exec_module(srcmod);old=srcmod.old
from flint import arb,arb_poly,ctx
load,ball,record,upper,caprec,exact_q=old.load,old.ball,old.record,old.upper,old.caprec,old.exact_q
MODES=list(range(94,185,2));LOWMODES=list(range(2,93,2));ORDER=24
def up(x):return upper(caprec(x))
def matvec(A,v):return [sum((A[i][j]*v[j] for j in range(2)),arb(0)) for i in range(2)]
def clone(c):
 d=old.ProjectiveColumn.__new__(old.ProjectiveColumn)
 for k in ('pivot','sign','absolute_lower','absolute_upper','ratio'):setattr(d,k,getattr(c,k))
 return d
def source_coefficients(P,K,source):
 """Same exact finite inverse polynomial, now only the unpaid coefficients."""
 q=max(i+1 for i,(p,k) in enumerate(zip(P,K)) if not(p==0 and k==0))
 if source['actual_finite_centre_support']!=2*q:raise ArithmeticError('Same actual finite centre support')
 cc=ball(source['actual_centre_mean']);w=ball(source['actual_original_w']);z=w*w;E=1+z;D0=1+cc
 if not D0>0:raise ArithmeticError('Actual mean positive inverse constant')
 pa=[arb(0)]*(2*q+1);ua=pa.copy();ka=pa.copy();ta=pa.copy();ka[q]=cc
 for i in range(1,q+1):
  m=2*i;p=P[i-1];k=K[i-1]
  pa[q+i]=-p/2;pa[q-i]=p/2;ua[q+i]=(m*k+p)/2;ua[q-i]=-(m*k+p)/2
  ka[q+i]=ka[q-i]=k/2;ta[q+i]=ta[q-i]=m*p/2
 Pi,Ui,KK,TT=map(arb_poly,(pa,ua,ka,ta));lam=arb_poly([arb(0) if i==q else ka[i]+E*ta[i] for i in range(2*q+1)])
 A=(-1/D0)*lam;S=arb_poly([1]);power=A;count=1
 while count<32:
  one=arb_poly([arb(0)]*(count*q)+[arb(1)]);S=S*(one+power);power=power*power;count*=2
 inv=(1/D0)*(srcmod.shift(S,q)+power);centre=34*q
 nums={'s':-E*(Ui*Ui),'ell':KK*KK+2*E*KK*TT+E*TT*TT+z*Pi*Pi}
 sigma=arb(1)/64;tau=exact_q(F(source['source_wide_sigma']));rho=upper(source['inverse_wide_sigma_norm']);answer={};saved=[]
 if not 0<=rho<1:raise ArithmeticError('Existing complete wide inverse domain')
 for name,num in nums.items():
  poly=num*inv;mat=source['materials'][name]
  tail=upper(mat['small_sigma_complete_inverse_tail']);wtail=up(upper(mat['complete_all_frequency_wide_source'])*rho**33)
  for k,m in enumerate(MODES):
   if name=='s':saved.append(dict(mode=m))
   finite=2*old.intersect(poly[centre+m//2],poly[centre-m//2])
   rem=min(up(tail*(-m*sigma).exp()),up(wtail*(-m*tau).exp()))
   full=old.add_error(finite,rem)
   if not(full.is_finite() and rem.is_finite() and rem>=0):raise ArithmeticError('Finite complete new-mode source')
   saved[k][name]=dict(finite32_cosine_coefficient=record(finite),complete_cosine_coefficient=record(full),complete_inverse_remainder_upper=caprec(rem))
  answer[name]=[ball(row[name]['complete_cosine_coefficient']) for row in saved]
 return answer,saved
def main():
 p=argparse.ArgumentParser(description=__doc__);p.add_argument('--out-prefix',type=Path,required=True);p.add_argument('--resume',type=Path);p.add_argument('--rss-kib',type=int,default=98304);a=p.parse_args()
 start=time.monotonic();ctx.prec=256;ctx.cap=26;ctx.threads=1;prefix=str(a.out_prefix)
 if any(a.out_prefix.parent.glob(a.out_prefix.name+'*')):raise FileExistsError('Fresh actual near-mode output prefix')
 a.out_prefix.parent.mkdir(parents=True,exist_ok=True);counts={}
 def gate(k,b):
  if not bool(b):raise ArithmeticError('Unpaid new-mode source/flow gate '+k)
  counts[k]=counts.get(k,0)+1
 def guard():
  if resource.getrusage(resource.RUSAGE_SELF).ru_maxrss>a.rss_kib:raise MemoryError('Unchanged96MiB actual guard')
 def rows(entries):
  for entry in entries:
   gate('actual_input_part_pin',sha(entry['path'])==entry['sha256']);packet=load(entry['path'])
   for row in packet['rows']:yield row
   del packet
 def identified(path):return dict(path=str(path),sha256=sha(path))
 sp=BASE/'outer9to7-centre-source-r2-summary.json.gz';sr=BASE/'outer9to7-centre-source-run2-resource.json';source=load(sp)
 gate('same_complete_source_pin',sha(sp)=='e4e4bf14d08cb6a6221d31e2da25fb315f9d342bc88d12cff7aa8ef775b020d2')
 gate('complete_source_formal_zero',old.resource_gate(load(sr)) and source['all_gates'] and all(source['gates'].values()))
 gate('complete_source_original_3940',source['total_leaves']==3940 and source['cell_leaf_counts']=={'9':1377,'8':1316,'7':1247})
 inputs={'source':identified(sp),'source_resource':identified(sr)};primaries={}
 for n in (9,8,7):
  pp=BASE/f'outer{n}-signed-low46-r1.json';pr=BASE/f'outer{n}-signed-low46-run1-resource.json';dat=load(pp)
  gate('original_low46_primary_pin',sha(pp)==srcmod.PRIMARY_PINS[n]);gate('original_low46_complete',dat['all_gates'] and all(dat['gates'].values()) and old.resource_gate(load(pr)))
  primaries[n]=dat;inputs[f'cell{n}']=identified(pp);inputs[f'cell{n}_resource']=identified(pr)
 mp=BASE/'outer7-nonzero-mean-r1-certificate.json.gz';mean=load(mp)
 gate('cell7_actual_tight_centre_pin',sha(mp)=='d9c11913cacae77751cf45c42b862970626e4c72ec32e9614111c96f3745eff3');inputs['cell7_refined_centre']=identified(mp)
 frozen=load(old.FROZEN/'manifest.json');gate('original_frozen_background',sha(old.FROZEN/'manifest.json')==old.MANIFEST)
 for ent in frozen['source_files']:gate('original_background_source_pin',sha(ent['path'])==ent['sha256'])
 ready=Path(frozen['inputs']['ready']['path']);gate('same_original_ready',sha(ready)==frozen['inputs']['ready']['sha256'])
 h=old.SourceValues({k:old.read_field(ready,k) for k in ('rationalDeepModel','shallowSourceParameters')});ker=old.PositiveKernels(h,12,92);h.cells={n:ker.source_cell(n) for n in (9,8,7)}
 F0=(ball(primaries[9]['initial_radius'])*ball(primaries[9]['initial_w'])**3).sqrt();gate('true_node10_F0_positive',F0>0)
 sigma=arb(1)/64;weights=[(1+m)*(m*sigma).exp() for m in MODES];Y=[[arb(0),arb(0)] for m in MODES]
 columns=[[old.ProjectiveColumn([arb(1),arb(0)]),old.ProjectiveColumn([arb(0),arb(1)])] for m in MODES]
 completed=[];cells=[];chunks=[];buffer=[];total=0;steps=0;rejected=0;resume_index=-1;resume=None;cellcaps=None;homcaps=None
 order=[(n,j) for n in (9,8,7) for j in range(9)]
 if a.resume:
  resume=load(a.resume);gate('resume_same_producer',resume['producer_sha256']==sha(__file__));gate('resume_same_actual_inputs',resume['inputs']==inputs)
  resume_index=order.index((resume['cell'],resume['segment']));Y=[[ball(v) for v in row] for row in resume['tracezero_particular_state']]
  columns=[[old.restore_column(v) for v in row] for row in resume['projective_homogeneous_columns']]
  completed=resume['completed_segments'];cells=resume['completed_cells'];total=resume['original_leaves_completed'];steps=resume['new_subleaves_completed'];rejected=resume['rejected_new_proposals']
  chunks=resume['source_flow_parts'];counts.update(resume['gate_categories'])
 def flush():
  if buffer:
   chunks.append(old.dump(prefix+f'-newmodes-part{len(chunks)+1:04d}.json.gz',dict(schema='new-original94to184-source-flow-leaves-v1',rows=list(buffer))));buffer.clear()
 srcit=iter(rows(source['source_parts']));refit=iter(rows(mean['profile_parts']))
 maxerr=upper(resume['maximum_actual_remainder']) if resume else arb(0)
 maxq=upper(resume['maximum_actual_partial_norm']) if resume else arb(0)
 mindet=ball(resume['minimum_suffix_determinant']) if resume else arb(1)
 for n in (9,8,7):
  if resume and resume['cell']==n and resume['segment']<8:
   cellcaps=[[upper(v) for v in row] for row in resume['current_cell_component_caps']]
   homcaps=[[[upper(v) for v in pair] for pair in row] for row in resume['current_cell_homogeneous_caps']]
   cellcount=resume['current_cell_leaf_count'];cellsteps=resume['current_cell_new_subleaves']
  else:cellcaps=[[arb(0),arb(0)] for m in MODES];homcaps=[[[arb(0),arb(0)],[arb(0),arb(0)]] for m in MODES];cellcount=0;cellsteps=0
  for row in rows(primaries[n]['profile_chunks']):
   src=next(srcit);ref=next(refit) if n==7 else row;ident={k:row[k] for k in ('cell','segment','left','right')}
   gate('same_original_leaf_identifiers',all(src[k]==row[k] and ref[k]==row[k] for k in ident))
   j=row['segment'];idx=order.index((n,j))
   if idx<=resume_index:continue
   lo=F(row['left']);hi=F(row['right']);bg=h.cells[n]['segments'][j];bg['_monotone_sign']=row['monotone_sign'];sign=row['monotone_sign']
   # The already proved monotone physical radius endpoints enclose this
   # entire old leaf and every new subleaf. No old radius ODE is repeated.
   bg['physical_inner_radius']=ball(row['radius_left']);bg['physical_outer_radius']=ball(row['radius_right'])
   recs=ref['refined_signed_centre_modes'] if n==7 else ref['whole_homogeneous_profiles'];gate('same_all46_finite_centre_modes',[v['mode'] for v in recs]==LOWMODES)
   coeff,saved=source_coefficients([ball(v['linear_PK'][0]) for v in recs],[ball(v['linear_PK'][1]) for v in recs],src)
   radius=ball(row['radius_left']);pending=[(lo,hi,0)];local=[];oldleft=lo
   while pending:
    left,right,depth=pending.pop();gate('new_subleaf_contiguous',left==oldleft)
    try:
     T,nr,err,qt=(old.root_physical(h,bg,left,right,radius,MODES) if sign==0 else old.taylor_physical(h,bg,left,right,radius,MODES,ORDER,old.power2(-100)))
     rr,_=old.rough_radius(h,bg,left,right,radius);x=exact_q(left).union(exact_q(right));sub=h.source_point(bg,x);w=old.intersect(ball(src['actual_original_w']),sub['w']);ell=sub['log_w_x'];E=1+w*w
     rx=abs(w*ell)/(8*E*E.sqrt())+h.alpha*sub['ro_x']/E;rxlo=(h.alpha*sub['ro_x']/E).lower();rx=old.intersect(rx,rxlo.union(rx.upper()))
     gate('positive_actual_subleaf_background',rr>0 and w>0 and rx>0)
     den=(rr*w**3).sqrt();dx=exact_q(right-left);s=rx/rr;ss=dx*s;ee=dx*ell;dd=(ee-ss)/2
     B,qp,major=old.balanced_majorant(dd,ss,ee,184)
     if sign==0 and not err<old.power2(-100):raise ArithmeticError('New-root remainder remains below original2^-100')
     newcols=[]
     for k in range(46):
      pair=[clone(v) for v in columns[k]]
      for c in pair:c.advance(T[k])
      newcols.append(pair)
    except ArithmeticError:
     rejected+=1
     if depth>=24:raise
     mid=(left+right)/2;pending.extend([(mid,right,depth+1),(left,mid,depth+1)]);continue
    # No already-completed state is changed before all local gates pass.
    gate('new_flow_original_remainder_gate',err<old.power2(-100));gate('new_balanced_partial_domain',0<=qp<arb(1)/2)
    remerr=up(qp*qp/(1-qp));rem=[[remerr,up(remerr/B)],[up(remerr*B),remerr]];d=up(abs(dd));one=1-d;gate('positive_suffix_diagonal',one>0)
    wr=h.source_point(bg,exact_q(right))['w'];denend=(nr*wr**3).sqrt();gate('positive_subleaf_endpoint',denend>0)
    subcaps=[]
    for k,m in enumerate(MODES):
     aa=up(m*abs(ss));bb=up(m*abs(ee));det=one*one-aa*bb;gate('new_mode_full_suffix_resolvent',det>0);mindet=min(mindet,det.lower())
     R12=up(aa/det);R22=up((d*one+aa*bb)/det);force=den*(s*coeff['s'][k]+ell*coeff['ell'][k]);mass=up(dx*abs(force))
     J=[old.add_error(arb(0),up(R12*mass)),old.add_error(dx*force,up(R22*mass))]
     JP=[J[0],old.add_error(arb(0).union(dx)*force,up(R22*mass))]
     M=[[dd,-m*ss],[-m*ee,-dd]];partial=[[old.add_error(arb(0).union(M[i][t])+(1 if i==t else 0),rem[i][t]) for t in range(2)] for i in range(2)]
     pv=matvec(partial,Y[k]);whole=[(pv[i]+JP[i])/den for i in range(2)];advanced=matvec(T[k],Y[k]);Y[k]=[advanced[i]+J[i] for i in range(2)]
     gate('every_new_mode_state_finite',all(v.is_finite() for v in whole+Y[k]));caps=[up(abs(v)) for v in whole];subcaps.append(caps)
     for i in range(2):cellcaps[k][i]=max(cellcaps[k][i],caps[i])
     for c in range(2):
      hp=matvec(partial,columns[k][c].values())
      for i in range(2):homcaps[k][c][i]=max(homcaps[k][c][i],up(abs(F0*hp[i]/den)))
    columns=newcols;radius=nr;oldleft=right;steps+=1;cellsteps+=1;maxerr=max(maxerr,up(err));maxq=max(maxq,up(qp))
    local.append(dict(left=str(left),right=str(right),radius_right=record(nr),balanced_integral_norm=caprec(qp),balanced_Taylor_remainder=caprec(err),
      signed_mode_flows=[dict(mode=m,matrix=[[record(v) for v in line] for line in T[k]]) for k,m in enumerate(MODES)],
      strong_particular_leaf_mass=caprec(sum((weights[k]*sum(subcaps[k],arb(0)) for k in range(46)),arb(0)))))
    guard()
   gate('all_original_leaf_covered_by_new_modes',oldleft==hi);gate('original_radius_right_overlap',old.intersect(radius,ball(row['radius_right'])).is_finite())
   total+=1;cellcount+=1;buffer.append(dict(**ident,actual_source_primary_sha256=sha(sp),new_mode_source_rows=saved,subleaves=local))
   if len(buffer)>=2:flush()
   if total%25==0:print(json.dumps(dict(event='actual_signed94to184',original_leaves=total,new_subleaves=steps,rejected=rejected,cell=n,segment=j,elapsed_seconds=time.monotonic()-start,peak_rss_kib=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)),flush=True)
   if hi==1:
    flush();cm=up(sum((weights[k]*sum(cellcaps[k],arb(0)) for k in range(46)),arb(0)))
    endpoint=[dict(mode=m,physical_particular_PK=[record(v/denend) for v in Y[k]],physical_node10_fundamental=[[record(F0*columns[k][c].values()[i]/denend) for c in range(2)] for i in range(2)]) for k,m in enumerate(MODES)]
    if j==8:
     expected=primaries[n]['counts']['taylor']+primaries[n]['counts']['root_brackets'];gate('every_original_leaf_in_cell',cellcount==expected)
     cells.append(dict(cell=n,original_leaves=cellcount,new_subleaves=cellsteps,whole_cell_radial_first_strong_particular=caprec(cm),component_caps=[dict(mode=m,P=caprec(cellcaps[k][0]),K=caprec(cellcaps[k][1])) for k,m in enumerate(MODES)],homogeneous_whole_component_caps=[dict(mode=m,physical_P_initial=list(map(caprec,homcaps[k][0])),physical_K_initial=list(map(caprec,homcaps[k][1]))) for k,m in enumerate(MODES)],endpoint_modes=endpoint))
    cp=dict(schema='same-original94to184-source-flow-checkpoint-v1',producer_sha256=sha(__file__),inputs=inputs,cell=n,segment=j,
      tracezero_particular_state=[[record(v) for v in row] for row in Y],projective_homogeneous_columns=[[old.column_record(v) for v in row] for row in columns],
      completed_segments=completed+[[n,j]],completed_cells=cells,original_leaves_completed=total,new_subleaves_completed=steps,rejected_new_proposals=rejected,
      source_flow_parts=chunks,gate_categories=counts,current_cell_component_caps=[list(map(caprec,row)) for row in cellcaps],current_cell_homogeneous_caps=[[list(map(caprec,pair)) for pair in row] for row in homcaps],current_cell_leaf_count=cellcount,current_cell_new_subleaves=cellsteps,
      current_radial_first_strong_particular=caprec(cm),endpoint_modes=endpoint,maximum_actual_remainder=caprec(maxerr),maximum_actual_partial_norm=caprec(maxq),minimum_suffix_determinant=record(mindet),zero_entry_particular=True,complete_source_mean_and_inverse=True,nonlinear_feedback_paid=False)
    ent=old.dump(prefix+f'-checkpoint-cell{n:02d}-segment{j}.json.gz',cp);completed.append([n,j]);print(json.dumps(dict(event='complete_new_mode_segment',cell=n,segment=j,particular_mass=str(cm),checkpoint=ent,elapsed_seconds=time.monotonic()-start)),flush=True)
 gate('complete_original3940',total==3940 and [tuple(v) for v in completed]==order);gate('all_three_cells',len(cells)==3)
 try:next(srcit);raise ArithmeticError('Unused complete source leaf')
 except StopIteration:pass
 summary=dict(schema='same-original9to7-signed94to184-complete-source-response-v1',author='exact_closure (GPT-6 Astra Pro; AI-assisted)',source_sha256=sha(__file__),complete_source_producer_sha256=SOURCE_SHA,
   all_gates=True,gates={k:True for k in counts},gate_count=sum(counts.values()),gate_categories=counts,inputs=inputs,cells=cells,modes=MODES,original_leaves=total,new_subleaves=steps,rejected_new_proposals=rejected,
   original_numeric_gates=dict(precision_bits=256,Taylor_order=24,remainder_bits=100,original_root_bits=160,rss_kib=a.rss_kib),maximum_actual_remainder=caprec(maxerr),maximum_actual_partial_norm=caprec(maxq),minimum_suffix_determinant=record(mindet),source_flow_parts=chunks,
   zero_entry_particular=True,actual_same_linear_centre=True,complete_mean_inverse_and_positive_infinite_source_tail=True,only_new94to184_homogeneous_modes_integrated=True,old_low46_modes_not_reintegrated=True,
   unknown_initial_high_field_paid=False,nonlinear_feedback_paid=False,full_outer_continuation_claimed=False,elapsed_seconds=time.monotonic()-start,peak_rss_kib=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)
 ent=old.dump(prefix+'-summary.json.gz',summary);print(json.dumps(dict(all_gates=True,primary=ent,gate_count=summary['gate_count'],elapsed_seconds=summary['elapsed_seconds'],peak_rss_kib=summary['peak_rss_kib'])),flush=True)
if __name__=='__main__':main()
