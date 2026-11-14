#!/usr/bin/env python3
"""Complete mean and actual two-material source of the same linear centre9..7.
No new ODE. Retains source mean before inverse, all inverse frequencies,
real mean-root enclosures, signed low46 coefficients and analytic high tails.
Author: exact_closure (GPT-6 Astra Pro; AI-assisted), 2026-11-13.
"""
import argparse,gzip,hashlib,importlib.util,json,resource,time
from fractions import Fraction as F
from pathlib import Path
BASE=Path('/workspace/scratch/d1aa462cfc02/exact-work')
SIGNED=BASE/'2026-11-13-exact-resume-outer8to7-signed-low46-v1.py'
def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
if sha(SIGNED)!='d34c1e1a7c5933921d5aceeab159eab558b7198af8ee68eca86d4aca407bc0ab':raise ArithmeticError('Frozen signed producer pin')
spec=importlib.util.spec_from_file_location('same_signed',SIGNED);old=importlib.util.module_from_spec(spec);spec.loader.exec_module(old)
from flint import arb,arb_poly,ctx
load,ball,record,upper,caprec,intersect=old.load,old.ball,old.record,old.upper,old.caprec,old.intersect
MODES=list(range(2,93,2));ORDER=32
PRIMARY_PINS={9:'c19d33f403f42c0b98ada4572aa58f860f17d922cd5e353d680d477d75640c07',8:'062a9ed72fc3a1841691bc8b7b785f8aaa75fb3694501a5ec38e6267e23cc332',7:'90f6ef971b581bd30b73cbcc9085791bb0cf7f27c3e5341e96d6e85fed1cbd72'}
def up(v):return upper(caprec(v))
def shift(p,n):return arb_poly([arb(0)]*n+p.coeffs())
WEIGHTS={}
def weight_array(tau,maximum):
 lo=tau.lower().man_exp();hi=tau.upper().man_exp()
 if lo!=hi:raise ArithmeticError('Exact dyadic source widths required')
 key=tuple(map(int,lo));values=WEIGHTS.setdefault(key,[])
 for i in range(len(values),maximum+1):values.append((2*i*tau).exp())
 return values
def norm(poly,centre,tau):
 ww=weight_array(tau,max(centre,poly.degree()-centre))
 return up(sum((abs(poly[k])*ww[abs(k-centre)] for k in range(poly.degree()+1)),arb(0)))
def save(p,d):
 p=Path(p)
 if p.exists():raise FileExistsError(p)
 raw=(json.dumps(d,separators=(',',':'))+'\n').encode()
 if len(raw)>4_900_000:raise MemoryError('Keep each saved proof packet under5MB')
 if p.suffix=='.gz':p.write_bytes(gzip.compress(raw,mtime=0))
 else:p.write_bytes(raw)
 return dict(path=str(p),sha256=sha(p),bytes=p.stat().st_size,uncompressed_bytes=len(raw))
def complete_mean_remainder(z,E,p,k,t,d):
 A=up(2*(k+d)+(k+d)**2+E*p*p);U=up(z*A);V=up(z*p*p);Y=up((1+d+k)*t)
 if not 0<=U<1 or not 0<=V<1:raise ArithmeticError('Full centre mean series domain')
 r=(1-U).sqrt();f=up(U*(2+r)/(2*r*(1+r)**2));g=up(U/(r*(1+r)))
 return up(A*f+Y*(g+V)/(1-V)),U,V

def main():
 ap=argparse.ArgumentParser(description=__doc__)
 ap.add_argument('--out-prefix',type=Path,required=True);ap.add_argument('--rss-kib',type=int,default=98304)
 a=ap.parse_args();start=time.monotonic();ctx.prec=256;ctx.threads=1
 prefix=str(a.out_prefix)
 if any(a.out_prefix.parent.glob(a.out_prefix.name+'*')):raise FileExistsError('Fresh actual source prefix required')
 a.out_prefix.parent.mkdir(parents=True,exist_ok=True)
 counts={}
 def gate(k,v):
  if not bool(v):raise ArithmeticError('Unpaid complete-centre source gate: '+k)
  counts[k]=counts.get(k,0)+1
 fm=load(old.FROZEN/'manifest.json');gate('original_frozen_manifest',sha(old.FROZEN/'manifest.json')==old.MANIFEST)
 for ent in fm['source_files']:gate('original_source_pin',sha(ent['path'])==ent['sha256'])
 ready_path=Path(fm['inputs']['ready']['path']);gate('original_ready_pin',sha(ready_path)==fm['inputs']['ready']['sha256'])
 ready={k:old.read_field(ready_path,k) for k in ('rationalDeepModel','shallowSourceParameters')}
 h=old.SourceValues(ready);del ready;ker=old.PositiveKernels(h,12,92);h.cells={n:ker.source_cell(n) for n in (9,8,7)}
 input_ids={};primaries={}
 for n in (9,8,7):
  p=BASE/f'outer{n}-signed-low46-r1.json';r=BASE/f'outer{n}-signed-low46-run1-resource.json';d=load(p)
  gate('original_cell_primary_pin',sha(p)==PRIMARY_PINS[n]);gate('original_cell_formal_zero',old.resource_gate(load(r)))
  gate('original_cell_all_gates',d['all_gates'] and all(d['gates'].values()))
  gate('same_original_true_linear_coordinates',d['config']['coordinates']=='Y=sqrt(r*w^3)*(P_sine,K_cosine)')
  input_ids[f'cell{n}']=dict(path=str(p),sha256=sha(p));input_ids[f'cell{n}_resource']=dict(path=str(r),sha256=sha(r));primaries[n]=d
 gate('same_complete_initial_true_linear_reference',primaries[9]['input_rows']==primaries[8]['input_rows']==primaries[7]['input_rows'])
 meanpath=BASE/'outer7-nonzero-mean-r1-certificate.json.gz';meanres=BASE/'outer7-nonzero-mean-run1-resource.json';mean=load(meanpath)
 gate('cell7_complete_mean_pin',sha(meanpath)=='d9c11913cacae77751cf45c42b862970626e4c72ec32e9614111c96f3745eff3')
 gate('cell7_complete_mean_formal_zero',old.resource_gate(load(meanres)) and mean['all_gates'] and all(mean['gates'].values()))
 input_ids['cell7_complete_mean']=dict(path=str(meanpath),sha256=sha(meanpath));input_ids['cell7_mean_resource']=dict(path=str(meanres),sha256=sha(meanres))
 sigma=arb(1)/64;sigma_weights=weight_array(sigma,34*46);weights=[sigma_weights[m//2] for m in MODES]
 minimum_width={9:F(1,2),8:F(3,8),7:F(1,4)}
 width_options=[F(1,4),F(3,8),F(1,2),F(3,4),F(1),F(3,2),F(2),F(3),F(4),F(6),F(8)]
 chunks=[];buffer=[];brief=[];seen=0;cell_counts={};maxima={};minimum_chosen={};support_counts={};mean_steps=4
 def flush():
  if buffer:
   chunks.append(save(prefix+f'-sources-part{len(chunks)+1:03d}.json.gz',dict(schema='same-original-linear-centre-complete-source-leaves-v1',rows=list(buffer))));buffer.clear()
 def globalmax(k,v,ident):
  v=up(v)
  if k not in maxima or v>upper(maxima[k]['upper']):maxima[k]=dict(upper=caprec(v),where=ident)
 for n in (9,8,7):
  data=primaries[n];entries=mean['profile_parts'] if n==7 else data['profile_chunks'];segment=None;last=None;segments_seen=[];cell_count=0
  for ent in entries:
   gate('actual_saved_profile_pin',sha(ent['path'])==ent['sha256']);packet=load(ent['path'])
   for row in packet['rows']:
    j=row['segment'];lo=F(row['left']);hi=F(row['right']);ident=dict(cell=n,segment=j,left=str(lo),right=str(hi))
    if j!=segment:
     if segment is not None:gate('complete_source_segment',last==F(1))
     gate('original_segment_order',j==len(segments_seen));segments_seen.append(j);segment=j;last=F(0)
    gate('original_leaf_coverage',lo==last and hi>lo);last=hi;seen+=1;cell_count+=1
    bg=h.cells[n]['segments'][j]
    if n==7:
     recs=row['refined_signed_centre_modes'];w=ball(row['refined_w']);dstart=upper(row['root_absolute_upper'])
    else:
     recs=row['whole_homogeneous_profiles'];w=ball(row['whole_w']);ell=ball(row['log_w_x']);dx=old.exact_q(hi-lo)
     wl=h.source_point(bg,old.exact_q(lo))['w'];wr=h.source_point(bg,old.exact_q(hi))['w']
     w=intersect(w,intersect(wl*(arb(0).union(dx)*ell).exp(),wr*(-arb(0).union(dx)*ell).exp()))
     dstart=None
    gate('all46_source_modes',[v['mode'] for v in recs]==MODES)
    gate('original_positive_background',w>0 and w<arb(1)/2)
    z=w*w;E=1+z;zmax=up(z);Emax=up(E)
    P=[ball(v['linear_PK'][0]) for v in recs];K=[ball(v['linear_PK'][1]) for v in recs]
    p=up(sum((abs(v) for v in P),arb(0)));k=up(sum((abs(v) for v in K),arb(0)));t=up(sum((m*abs(v) for m,v in zip(MODES,P)),arb(0)))
    R=up(sum(((1+m)*ww*(abs(pv)+abs(kv)) for m,ww,pv,kv in zip(MODES,weights,P,K)),arb(0)))
    if n!=7:
     gate('actual_centre_small_root_R106_domain',R<arb(1)/64);dstart=up(4*R*R)
    q0=sum(((kv*kv+E*pv*pv)/4+m*kv*pv/2 for m,pv,kv in zip(MODES,P,K)),arb(0))
    if n==7:q0=intersect(q0,ball(row['centre_exact_quadratic_mean']))
    gate('same_actual_root_start_radius',0<dstart<arb(1)/8)
    cr=dstart;posterior=[]
    for it in range(mean_steps):
     err,U,V=complete_mean_remainder(zmax,Emax,p,k,t,cr)
     newcr=min(cr,up((abs(q0)+err)/(1-cr/2)))
     gate('true_mean_finite_posterior',0<=newcr<=cr)
     posterior.append(dict(radius_in=caprec(cr),complete_remainder=caprec(err),radius_out=caprec(newcr)));cr=newcr
    err,U,V=complete_mean_remainder(zmax,Emax,p,k,t,cr)
    Q=old.add_error(q0,err);disc=1-2*Q;gate('true_centre_mean_quadratic_branch',disc>0)
    cc=-2*Q/(1+disc.sqrt());cc=intersect(cc,(-cr).union(cr));gate('actual_centre_mean_finite',cc.is_finite())
    D0=1+cc;gate('actual_positive_one_plus_mean',D0>0)
    # Drop only exactly zero outer finite-centre modes. This changes no
    # actual finite field and is never an infinite-source truncation.
    active=[i+1 for i,(pv,kv) in enumerate(zip(P,K)) if not(pv==0 and kv==0)]
    q=max(active) if active else 0;gate('finite_centre_support_valid',q>0 and all(P[i]==0 and K[i]==0 for i in range(q,46)))
    support_counts[str(2*q)]=support_counts.get(str(2*q),0)+1
    pa=[arb(0)]*(2*q+1);ua=[arb(0)]*(2*q+1);ka=[arb(0)]*(2*q+1);ta=[arb(0)]*(2*q+1)
    ka[q]=cc
    for i in range(1,q+1):
     m=2*i;pv=P[i-1];kv=K[i-1]
     pa[q+i]=-pv/2;pa[q-i]=pv/2
     ua[q+i]=(m*kv+pv)/2;ua[q-i]=-(m*kv+pv)/2
     ka[q+i]=ka[q-i]=kv/2;ta[q+i]=ta[q-i]=m*pv/2
    Pi=arb_poly(pa);Ui=arb_poly(ua);KK=arb_poly(ka);TT=arb_poly(ta)
    lam=arb_poly([arb(0) if i==q else ka[i]+E*ta[i] for i in range(2*q+1)])
    A=-lam/D0
    rhos=norm(A,q,sigma);gate('full_inverse_small_sigma',rhos<1)
    chosen=None;wide_rows=[]
    for tauF in width_options:
     if tauF<minimum_width[n]:continue
     tau=old.exact_q(tauF);rho=norm(A,q,tau)
     # The bound1/2 is an explicit source-analyticity working gate, not
     # a precondition for the existing real mean branch.
     if rho<arb(1)/2:
      chosen=(tauF,tau,rho);wide_rows.append(dict(width=str(tauF),rho=caprec(rho),passed=True))
     else:wide_rows.append(dict(width=str(tauF),rho=caprec(rho),passed=False))
    gate('required_source_analytic_width',chosen is not None)
    tauF,tau,rhow=chosen;minimum_chosen[n]=min(minimum_chosen.get(n,tauF),tauF)
    numerators={'s':-E*(Ui*Ui),'ell':KK*KK+2*E*(KK*TT)+E*(TT*TT)+z*(Pi*Pi)}
    # Exact geometric polynomial through degree32 by doubling. Sum_N
    # has Laurent centre (N-1)q, power_N has centre Nq.
    S=arb_poly([1]);power=A;count=1
    while count<32:
     one=arb_poly([arb(0)]*(count*q)+[arb(1)])
     S=S*(one+power);power=power*power;count*=2
    inv=(shift(S,q)+power)/D0
    ic=32*q;outc=34*q;parts={};low=[]
    for name,num in numerators.items():
     finitepoly=num*inv
     n0=norm(num,2*q,sigma);nw=norm(num,2*q,tau)
     tail=up(n0*rhos**33/(D0.lower()*(1-rhos)))
     wide=up(nw/(D0.lower()*(1-rhow)))
     gate('full_source_tail_finite_nonnegative',tail.is_finite() and tail>=0 and wide.is_finite() and wide>=0)
     finite_pairs=[]
     for i in range(1,outc+1):
      plus=finitepoly[outc+i];minus=finitepoly[outc-i]
      coeff=2*intersect(plus,minus)
      finite_pairs.append(coeff)
     finite_total=up(sum((abs(v)*sigma_weights[i+1] for i,v in enumerate(finite_pairs)),arb(0)))
     nonlow=up(sum((abs(v)*sigma_weights[i+1] for i,v in enumerate(finite_pairs) if i+1>46),arb(0)))
     common=up(min(n0/(D0.lower()*(1-rhos)),finite_total+tail))
     high=up(min(nonlow+tail,wide*(-94*(tau-sigma)).exp()))
     parts[name]=dict(zero_mode_before_projection=record(finitepoly[outc]),small_sigma_numerator_norm=caprec(n0),small_sigma_complete_inverse_tail=caprec(tail),whole_nonzero_small_sigma_source=caprec(common),complete_nonlow94up_small_sigma_source=caprec(high),complete_all_frequency_wide_source=caprec(wide),finite_polynomial_max_physical_mode=2*outc)
     for idx,m in enumerate(MODES):
      if name=='s':low.append(dict(mode=m))
      val=finite_pairs[idx] if idx<len(finite_pairs) else arb(0)
      rem=up(tail/sigma_weights[m//2]);complete=old.add_error(val,rem)
      low[idx][name]=dict(finite32_cosine_coefficient=record(val),shared_tail_to_this_coefficient_upper=caprec(rem),complete_cosine_coefficient=record(complete))
     globalmax(name+'_full_small_sigma_source',common,ident);globalmax(name+'_full_nonlow94up_small_sigma_source',high,ident);globalmax(name+'_full_wide_source',wide,ident)
    item=dict(**ident,actual_original_w=record(w),actual_centre_mean=record(cc),complete_mean_radius_start=caprec(dstart),complete_mean_finite_posterior=posterior,complete_mean_remainder=caprec(err),actual_signed_quadratic_mean=record(q0),centre_all46_modes_retained=True,actual_finite_centre_support=2*q,source_sigma='1/64',source_wide_sigma=str(tauF),inverse_degree=32,inverse_small_sigma_norm=caprec(rhos),inverse_wide_sigma_norm=caprec(rhow),source_analytic_width_gates=wide_rows,materials=parts,low46_signed_source_rows=low,source_x_definition='N=Pi_perp(s*N_s+ell*N_ell); N_s=E U^2/L, N_ell=(K^2+2E K T+E T^2-z P^2)/L; complete mean K=c+Kbar retained.',complete_mean_inverse_and_infinite_source=True,actual_nonlinear_solution_claimed=False)
    buffer.append(item)
    globalmax('complete_centre_mean_absolute',abs(cc),ident)
    if len(buffer)>=8:flush()
    if seen%50==0:print(json.dumps(dict(event='actual_complete_centre_source',leaves=seen,cell=n,elapsed_seconds=time.monotonic()-start,peak_rss_kib=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)),flush=True)
    if resource.getrusage(resource.RUSAGE_SELF).ru_maxrss>a.rss_kib:raise MemoryError('Owned96MiB cap unchanged')
   del packet
  gate('all_nine_segments_cell'+str(n),segments_seen==list(range(9)) and last==F(1))
  gate('all_original_leaves_cell'+str(n),cell_count==data['counts']['taylor']+data['counts']['root_brackets']);cell_counts[n]=cell_count
 flush()
 summary=dict(schema='same-original9to7-actual-complete-centre-mean-and-source-v1',author='exact_closure (GPT-6 Astra Pro; AI-assisted)',all_gates=True,gates={k:True for k in counts},gate_count=sum(counts.values()),gate_categories=counts,inputs=input_ids,source_sha256=sha(__file__),signed_producer_sha256=sha(SIGNED),precision_bits=ctx.prec,inverse_degree=32,mean_finite_posterior_steps=4,source_sigma='1/64',minimum_required_source_wide_sigmas={str(k):str(v) for k,v in minimum_width.items()},minimum_actual_source_wide_sigmas={str(k):str(v) for k,v in minimum_chosen.items()},finite_centre_support_counts=support_counts,cells=[9,8,7],cell_leaf_counts=cell_counts,total_leaves=seen,source_parts=chunks,complete_leaf_records_are_in_source_parts=True,strongest_per_leaf_source_bounds=maxima,source_norm='Each leaf separately uses sum of coefficient suprema, before summing angular modes. Block maxima are not global whole-cell radial-first norms.',same_true_linear_centre_with_complete_mean=True,full_source_zero_kept_before_full_inverse=True,complete_infinite_inverse_tail=True,no_new_ODE_or_source_integral=True,true_nonlinear_solution_or_leave_tube_not_claimed=True,new_high_input_analyticity_not_claimed=True,elapsed_seconds=time.monotonic()-start,peak_rss_kib=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)
 info=save(prefix+'-summary.json.gz',summary);print(json.dumps(dict(all_gates=True,gate_count=summary['gate_count'],primary=info,elapsed_seconds=summary['elapsed_seconds'],peak_rss_kib=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)),flush=True)
if __name__=='__main__':main()
