#!/usr/bin/env python3
"""Complete nonzero-centre mean domain on every original cell7 leaf.
Replays saved signed endpoint matrices only; no ODE or new source integral.
Author: exact_closure (GPT-6 Astra Pro; AI-assisted), 2026-11-13.
"""
import argparse,gzip,hashlib,importlib.util,json,resource,sys,time
from fractions import Fraction as F
from pathlib import Path
BASE=Path('/workspace/scratch/d1aa462cfc02/exact-work')
SIGNED=BASE/'2026-11-13-exact-resume-outer8to7-signed-low46-v1.py'
SIGNED_SHA='d34c1e1a7c5933921d5aceeab159eab558b7198af8ee68eca86d4aca407bc0ab'
def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
if sha(SIGNED)!=SIGNED_SHA:raise ArithmeticError('Original saved signed-flow producer changed')
spec=importlib.util.spec_from_file_location('same_signed_cell7',SIGNED);old=importlib.util.module_from_spec(spec);spec.loader.exec_module(old)
from flint import arb,ctx
load=old.load;ball=old.ball;record=old.record;upper=old.upper;caprec=old.caprec;intersect=old.intersect
MODES=list(range(2,93,2))
def up(v):return upper(caprec(v))
def finite(v):return v.is_finite()
def pos(v):return finite(v) and v>0

def dump(p,d):
 p=Path(p)
 if p.exists():raise FileExistsError(p)
 raw=(json.dumps(d,separators=(',',':'))+'\n').encode()
 if len(raw)>4_900_000:raise MemoryError('Split proof packet before5MB')
 if p.suffix=='.gz':p.write_bytes(gzip.compress(raw,mtime=0))
 else:p.write_bytes(raw)
 return dict(path=str(p),sha256=sha(p),bytes=p.stat().st_size,uncompressed_bytes=len(raw))

def fg(q):
 if not 0<=q<1:raise ArithmeticError('Mean series majorant needs q<1')
 rt=(1-q).sqrt()
 return up(q*(2+rt)/(2*rt*(1+rt)**2)),up(q/(rt*(1+rt)))

def main():
 ap=argparse.ArgumentParser(description=__doc__)
 ap.add_argument('--out-prefix',type=Path,required=True);ap.add_argument('--rss-kib',type=int,default=98304)
 a=ap.parse_args();start=time.monotonic();ctx.prec=256;ctx.threads=1
 prefix=str(a.out_prefix)
 if any(a.out_prefix.parent.glob(a.out_prefix.name+'*')):raise FileExistsError('Fresh actual complete-mean prefix required')
 a.out_prefix.parent.mkdir(parents=True,exist_ok=True)
 primary=BASE/'outer7-signed-low46-r1.json';pr=BASE/'outer7-signed-low46-run1-resource.json'
 previous=BASE/'outer8-signed-low46-r1.json';prevres=BASE/'outer8-signed-low46-run1-resource.json'
 frozen=BASE/'outer9-low46-inputs/manifest.json'
 data=load(primary);prev=load(previous);fm=load(frozen)
 counts={};failures=[]
 def gate(k,v):
  if not bool(v):raise ArithmeticError('Original input/readout identity failed: '+k)
  counts[k]=counts.get(k,0)+1
 def mathgate(k,v,identity):
  if not bool(v):failures.append(dict(gate=k,**identity))
  counts[k]=counts.get(k,0)+1
  return bool(v)
 gate('primary_pin',sha(primary)=='90f6ef971b581bd30b73cbcc9085791bb0cf7f27c3e5341e96d6e85fed1cbd72')
 gate('previous_pin',sha(previous)=='062a9ed72fc3a1841691bc8b7b785f8aaa75fb3694501a5ec38e6267e23cc332')
 gate('old_formal_zero',old.resource_gate(load(pr)) and old.resource_gate(load(prevres)))
 gate('old_all_gates',data['all_gates'] and all(data['gates'].values()) and prev['all_gates'] and all(prev['gates'].values()))
 gate('same_original_saved_arithmetic',all(data['config'][k]==v for k,v in [('precision',256),('order',24),('root_bits',160),('remainder_bits',100)]))
 gate('same_frozen_original_source_manifest',sha(frozen)==old.MANIFEST)
 for ent in fm['source_files']:gate('original_source_file_pin',sha(ent['path'])==ent['sha256'])
 ready_path=Path(fm['inputs']['ready']['path']);gate('original_ready_pin',sha(ready_path)==fm['inputs']['ready']['sha256'])
 ready={k:old.read_field(ready_path,k) for k in ('rationalDeepModel','shallowSourceParameters')}
 raw=old.raw_cell_identity(ready,7);gate('true_raw_cell7_cap_identity',raw['cap_strictly_inactive'])
 h=old.SourceValues(ready);del ready
 ker=old.PositiveKernels(h,12,92);h.cells={7:ker.source_cell(7)}
 modes=prev['endpoint_modes'];gate('all46_input_modes',[x['mode'] for x in modes]==MODES)
 columns=[old.restore_column(row['columns'][0]) for row in modes]
 lambdas=[ball(row['lambda_true_far_linear']) for row in data['input_rows']]
 gate('true_original_coordinates',data['config']['coordinates']=='Y=sqrt(r*w^3)*(P_sine,K_cosine)')
 eta=arb(1)/16;d=arb(1)/8;sigma=arb(1)/64
 weights=[(m*sigma).exp() for m in MODES]
 segments={j:load(ent['path']) for j,ent in enumerate(data['completed_segments'])}
 for ent in data['completed_segments']:gate('old_segment_pin',sha(ent['path'])==ent['sha256'])
 seen=0;coverage=[];segment=None;last=None;chunks=[];buffer=[];summary_rows=[]
 worst={};best={};tight_improvements=[]
 def record_upper(key,value,ident):
  vv=up(value)
  if key not in worst or vv>upper(worst[key]['upper']):worst[key]=dict(upper=caprec(vv),where=ident)
 def record_lower(key,value,ident):
  vv=value.lower()
  if key not in best or vv<old.endpoint(best[key]['lower']):best[key]=dict(lower=old.record(arb(vv))['lower'],where=ident)
 def flush():
  if buffer:
   chunks.append(dump(prefix+f'-leaves-part{len(chunks)+1:03d}.json.gz',dict(schema='original-cell7-refined-readout-complete-mean-leaves-v1',rows=list(buffer))))
   buffer.clear()
 def finish(j):
  nonlocal columns
  ep=segments[j]
  gate('whole_segment_coverage_'+str(j),last==F(1))
  gate('same_segment_endpoint_mode_order',[z['mode'] for z in ep['modes']]==MODES)
  for idx in range(46):
   saved=old.restore_column(ep['modes'][idx]['columns'][0]);val=columns[idx].values();savedval=saved.values()
   for v,w in zip(val,savedval):gate('saved_endpoint_intersection',finite(intersect(v,w)))
  columns=[old.restore_column(row['columns'][0]) for row in ep['modes']]
 for entry in data['profile_chunks']:
  gate('saved_profile_pin',sha(entry['path'])==entry['sha256'])
  packet=load(entry['path'])
  for row in packet['rows']:
   j=row['segment'];lo=F(row['left']);hi=F(row['right']);ident=dict(cell=7,segment=j,left=str(lo),right=str(hi))
   if j!=segment:
    if segment is not None:finish(segment)
    gate('segment_order',j==len(coverage));coverage.append(j);segment=j;last=F(0)
   gate('all_original_leaves_cover',lo==last and hi>lo);last=hi;seen+=1
   gate('all_saved_original46_modes',[z['mode'] for z in row['whole_homogeneous_profiles']]==[z['mode'] for z in row['local_signed_flow']]==MODES)
   bg=h.cells[7]['segments'][j];wl=h.source_point(bg,old.exact_q(lo))['w'];wr=h.source_point(bg,old.exact_q(hi))['w']
   dx=old.exact_q(hi-lo);ell=ball(row['log_w_x']);r=ball(row['whole_radius']);wold=ball(row['whole_w'])
   gate('real_endpoints_positive',pos(wl) and pos(wr))
   forward=wl*(arb(0).union(dx)*ell).exp();backward=wr*(-arb(0).union(dx)*ell).exp()
   w=intersect(wold,intersect(forward,backward))
   gate('complete_positive_refined_w',pos(w) and pos(r) and w<arb(1)/2)
   # The old ell interval is a proved wholeleaf integral bound. Its two
   # endpoint exponential tubes enclose every actual w in the leaf.
   ss=dx*ball(row['radius_x'])/r;ee=dx*ell;dd=(ee-ss)/2
   q=ball(row['integral_norm']);B=ball(row['balance'])
   gate('old_partial_tail_domain',0<=q<1 and pos(B))
   error=up(q*q/(1-q));rem=[[error,up(error/B)],[up(error*B),error]]
   den=(r*w*w*w).sqrt();gate('true_physical_readout_positive',pos(den))
   centres=[];new_cols=[]
   p0=k0=t0=ps=ks=ts=l0=ls=us=arb(0);q0=arb(0);E=1+w*w
   for idx,m in enumerate(MODES):
    M=[[dd,-m*ss],[-m*ee,-dd]]
    part=[[old.add_error(arb(0).union(M[a0][b0])+(1 if a0==b0 else 0),rem[a0][b0]) for b0 in range(2)] for a0 in range(2)]
    y=columns[idx].values()
    z=[lambdas[idx]*sum((part[a0][b0]*y[b0] for b0 in range(2)),arb(0))/den for a0 in range(2)]
    z=[intersect(v,ball(row['whole_homogeneous_profiles'][idx]['linear_PK'][a0])) for a0,v in enumerate(z)]
    gate('all_refined_signed_entries_finite',all(finite(v) for v in z))
    P,K=z;pa=up(abs(P));ka=up(abs(K));ta=m*pa;la=up(abs(K+E*m*P));ua=up(abs(m*K+P));weight=weights[idx]
    p0+=pa;k0+=ka;t0+=ta;ps+=pa*weight;ks+=ka*weight;ts+=ta*weight;l0+=la;ls+=la*weight;us+=ua*weight
    q0+=(K*K+E*P*P)/4+m*K*P/2
    centres.append(dict(mode=m,linear_PK=list(map(record,z))))
    T=[[ball(v) for v in rr] for rr in row['local_signed_flow'][idx]['matrix']]
    col=old.restore_column(old.column_record(columns[idx]));col.advance(T);new_cols.append(col)
   columns=new_cols
   p0,k0,t0,ps,ks,ts,l0,ls,us=[up(v) for v in (p0,k0,t0,ps,ks,ts,l0,ls,us)]
   zmax=up(w*w);Emax=up(E)
   # RP+RK<=eta: weak P/K<=R/3, delta Ptheta<=RP. The
   # complete quadratic perturbation is <=31 eta^2/270<eta^2/8.
   dq=up(eta*max(up(Emax*p0/3+k0),up((k0+t0)/3))+eta*eta/8)
   qb=up(abs(q0)+dq)
   pu=up(p0+eta/3);ku=up(k0+eta/3);tu=up(t0+eta)
   pstrip=up(ps+eta/3);kstrip=up(ks+eta/3);tstrip=up(ts+eta)
   Ac=up(2*(ku+d)+(ku+d)**2+Emax*pu*pu);U=up(zmax*Ac);V=up(zmax*pu*pu);Y=up((1+d+ku)*tu)
   As=up(2*(kstrip+d)+(kstrip+d)**2+Emax*pstrip*pstrip);Us=up(zmax*As);Vs=up(zmax*pstrip*pstrip)
   prelim=mathgate('complete_mean_series_domains',0<=U<1 and 0<=V<1 and 0<=Us<1 and 0<=Vs<1,ident)
   if not prelim:raise ArithmeticError('Unpaid mean-series domain; cannot compute complete remainder')
   f,g=fg(U);err=up(Ac*f+Y*(g+V)/(1-V));rouche=up(qb+d*d/2+err)
   root_cap=up((qb+err)/(1-d/2))
   ymin=1-d-ku;Lmin=1-d-l0-Emax*eta;Nmin=1-zmax*Y/(1-V);stripgap=1-d-ls-Emax*eta
   checks={
    'complete_complex_Rouche_one_simple_root':rouche<d,
    'real_S_positive':1-V>0,'real_D_positive':1-U>0,
    'real_y_positive':ymin>0,'real_L_positive':Lmin>0,'real_N_positive':Nmin>0,
    'complete_angle_weak_Wiener_inverse':stripgap>0,
    'complete_strip_S_D_positive_series_domains':Us<1 and Vs<1}
   for name,ok in checks.items():mathgate(name,ok,ident)
   mu=Lmin/(1+U)**(arb(3)/2)
   Ns=Nell=None
   if stripgap>0:
    Ns=up(Emax*(us+eta)**2/stripgap)
    fullK=kstrip+d
    Nell=up(((fullK+tstrip)**2+zmax*(2*fullK*tstrip+tstrip*tstrip+pstrip*pstrip))/stripgap)
   small=dict(**ident,refined_w=record(w),old_w=record(wold),centre_weak_P=caprec(p0),centre_weak_K=caprec(k0),centre_weak_Ptheta=caprec(t0),centre_correlated_lambda=caprec(l0),centre_correlated_lambda_weak_strip=caprec(ls),centre_exact_quadratic_mean=record(q0),complete_q0_upper=caprec(qb),mean_remainder_upper=caprec(err),Rouche_left_upper=caprec(rouche),root_absolute_upper=caprec(root_cap),S_lower=record(1-V)['lower'],D_lower=record(1-U)['lower'],y_lower=record(ymin)['lower'],L_lower=record(Lmin)['lower'],N_lower=record(Nmin)['lower'],angle_weak_inverse_gap_lower=record(stripgap)['lower'],mean_real_derivative_lower=record(mu)['lower'],complete_N_s_material_weak_strip=None if Ns is None else caprec(Ns),complete_N_ell_material_weak_strip=None if Nell is None else caprec(Nell),all_domain_gates=all(checks.values()))
   summary_rows.append(small)
   buffer.append(dict(**small,refined_signed_centre_modes=centres,original_profile_chunk_sha256=entry['sha256'],old_T_matrices_reused=True,complete_infinite_perturbation_in_eta_ball=True))
   for key,value in [('centre_weak_K',k0),('centre_correlated_lambda_weak_strip',ls),('Rouche_left',rouche),('mean_remainder',err),('root_absolute',root_cap)]:record_upper(key,value,ident)
   for key,value in [('y',ymin),('L',Lmin),('N',Nmin),('S',1-V),('D',1-U),('angle_inverse_gap',stripgap),('mean_derivative',mu)]:record_lower(key,value,ident)
   if Ns is not None:record_upper('complete_N_s_material',Ns,ident);record_upper('complete_N_ell_material',Nell,ident)
   if len(buffer)>=16:flush()
   if seen%100==0:print(json.dumps(dict(event='actual_nonzero_mean',leaves=seen,failures=len(failures),elapsed_seconds=time.monotonic()-start,peak_rss_kib=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)),flush=True)
   if resource.getrusage(resource.RUSAGE_SELF).ru_maxrss>a.rss_kib:raise MemoryError('Preserve original owned96MiB cap')
  del packet
 finish(segment);flush()
 gate('all_nine_original_segments',coverage==list(range(9)))
 gate('all_original_successful_leaves_only',seen==data['counts']['taylor']+data['counts']['root_brackets'])
 out=dict(schema='same-original-cell7-nonzero-centre-complete-mean-domain-v1',author='exact_closure (GPT-6 Astra Pro; AI-assisted)',all_gates=not failures,gates={k:not any(failure['gate']==k for failure in failures) for k in counts},gate_count=sum(counts.values()),gate_categories=counts,failures=failures,
  source_sha256=sha(__file__),source_signed_producer_sha256=sha(SIGNED),inputs={name:dict(path=str(path),sha256=sha(path)) for name,path in [('primary',primary),('resource',pr),('previous',previous),('previous_resource',prevres),('original_frozen_manifest',frozen),('original_ready',ready_path)]},
  precision_bits=ctx.prec,original_ODE_order_and_remainder_unchanged=data['config'],cell=7,complete_original_leaf_count=seen,original_all46_modes=MODES,
  centre='Same actual signed full linear reference L_R; every saved original endpoint propagator is reused, with full pointwise original background.',
  tube=dict(strong_angular_sigma='1/64',complete_complex_nonmean_even_strong_radius='1/16',mean_root_disk_radius='1/8',all_infinite_frequencies_in_the_perturbation=True),
  mathematical_identity='M(c)=c+c^2/2+q0+R; complete R64 binomial and inverse remainder is retained uniformly on the whole c disk. Strict Rouche count is one, hence the root is simple and holomorphic. Real data give a real root by conjugation; all original R75 real positive-branch gates are separate.',
  refined_w_method='Intersection of old wholeleaf w with true endpoint w_left*exp([0,dx]*ell) and w_right*exp([-dx,0]*ell); old whole ell bounds and actual endpoint formula, no new integration.',
  strongest_upper_bounds=worst,strict_lower_bounds=best,rows=summary_rows,profile_parts=chunks,
  two_material_source_bounds_are_separate=True,existing_nonlinear_field_in_tube_not_claimed=True,new_ODE_or_source_integral=False,new_full_nonlinear_outer_extension=False,new_closed_surface_or_all_t_claimed=False,
  elapsed_seconds=time.monotonic()-start,peak_rss_kib=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)
 info=dump(prefix+'-certificate.json.gz',out)
 print(json.dumps(dict(all_gates=not failures,gate_count=out['gate_count'],failure_count=len(failures),primary=info,elapsed_seconds=out['elapsed_seconds'],peak_rss_kib=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)),flush=True)
 if failures:raise SystemExit(1)
if __name__=='__main__':main()
