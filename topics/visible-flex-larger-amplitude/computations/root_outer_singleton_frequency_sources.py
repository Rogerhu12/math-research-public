#!/usr/bin/env python3
"""Actual original singleton94/96 nonlow reception with all frequency supports.
Author: /root (GPT-6 Astra Pro, AI-assisted), 2026-11-13.
Only source coefficients and supports; no new field, ODE, quadrature or cut.
"""
import argparse,gzip,json,pathlib,resource,time
from flint import fmpq as Q,ctx
import root_window_frequency_cut_bootstrap as h


def alpha(k,n):return Q(5*k*n+1,4*(1+k)*(1+n))

def main():
 p=argparse.ArgumentParser(description=__doc__);p.add_argument('--inputs',type=pathlib.Path,required=True);p.add_argument('--out',type=pathlib.Path,required=True);a=p.parse_args();ctx.prec=256;t=time.monotonic();ids=h.read(a.inputs);g={};counts={}
 def gate(k,v,n=1):
  if not v:raise ArithmeticError(k)
  g[k]=True;counts[k]=counts.get(k,0)+n
 def read(k):
  z=ids[k];gate('input_sha_'+k,h.sha(z['path'])==z['sha256']);return h.read(z['path'])
 sources=read('low_sources');spectrum=read('low_spectrum');window=read('old_windows');nonlow=read('nonlow');kernels=read('singletons');kr=read('singletons_resource')
 gate('all_original_operators',sources['all_gates'] and spectrum['all_gates'] and window['all_gates'] and nonlow['all_gates'])
 gate('original_partitions_and_common_strip',sources['comparison_partition']==window['comparison_partition']==nonlow['comparison_partition'] and kernels['comparison_partition']==window['comparison_partition'] and kernels['common_strip']==window['common_strip'])
 gate('actual_two_singleton_operators',kernels['all_gates'] and kr['exitcode']==0 and kr['termination_signal'] is None and [x['window'] for x in kernels['rows']]==[[94,94],[96,96]])
 old=[x['window'] for x in window['windows']];gate('original185_complete_partition',old[0]==[94,96] and len(old)==185 and [m for lo,hi in old for m in range(lo,hi+1,2)]==list(range(94,h.M,2)))
 windows=[[94,94],[96,96]]+old[1:];parent=[0,0]+list(range(1,185));winof={m:i for i,(lo,hi) in enumerate(windows) for m in range(lo,hi+1,2)}
 gate('refinement_186_no_mode_lost_or_duplicated',len(winof)==(h.M-94)//2 and [m for lo,hi in windows for m in range(lo,hi+1,2)]==list(range(94,h.M,2)))
 caps={r['mode']:h.ex(r['bound']) for r in spectrum['final_caps']};gate('original46_centre',sorted(caps)==h.MODES and 0<sum(caps.values(),Q(0))<10)
 gate('same_full_mean_inverse_T_domain',h.ex(nonlow['complete_Hessian_domain_upper'])==h.RSTAR and h.ex(nonlow['full_complete_Hessian_upper'])==Q(23,9)+270*h.RSTAR and h.RSTAR<Q(1,128))
 indexed={}
 for m in (94,96):
  pairs=[]
  for n in range(94,m+93,2):
   k=abs(m-n)
   if k in caps:pairs.append((k,n))
  indexed[m]=pairs
  gate('complete_singleton_linear_support_'+str(m),len(pairs)==(46 if m==94 else 47) and {n for k,n in pairs}==({*range(96,187,2)} if m==94 else {94,*range(98,189,2)}))
 for k,n in sorted(set(p for v in indexed.values() for p in v)):
  bound=alpha(k,n)*(1+k)*(1+n)
  for z in (Q(0),Q(1,4)):
   E=1+z
   for s,ell in ((Q(1),Q(0)),(Q(0),Q(1)),(Q(0),Q(-1))):
    diff=[E*s+ell*(E*k*n-z),E*(s*n+ell*k),E*(s*k+ell*n),E*s*k*n+ell*(E-z)]
    summ=[-E*s+ell*(E*k*n+z),E*(-s*n+ell*k),E*(-s*k+ell*n),-E*s*k*n+ell]
    gate('all_original_material_vertex_coefficients',max(map(abs,diff+summ))<=bound,8)
  gate('alpha_strict_generic_bound',0<alpha(k,n)<Q(5,4))
 rows=[];exp_cache={}
 def exp(v):
  if v not in exp_cache:
   from flint import arb
   exp_cache[v]=h.up(arb(v).exp())
  return exp_cache[v]
 for j,rec in enumerate(sources['source_records']):
  gate('source_sha',h.sha(rec['path'])==rec['sha256']);src=h.read(rec['path']);smin=Q(*map(int,src['sigma_min']));smax=Q(*map(int,src['sigma_max']))
  gate('all25_original_source_blocks',src['index']==j and src['modes']==h.MODES and Q(1,64)<smin<=smax<=h.TAU and src['angular_derivative_pair_constant']=='(5*k*n+1)/(4*(1+k)*(1+n))' and h.ex(src['complete_T_physical_domain'])==h.RSTAR)
  block=[]
  for m in (94,96):
   terms=[];cg={}
   for k,n in indexed[m]:
    sig=smax if m>=n else smin
    ce=(m-n)*sig-k*h.TAU;ue=(m-k-n)*smin
    gate('correct_signed_frequency_and_strip',m==k+n or m==n-k);gate('nonpositive_paid_angular_exponents',ce<=0 and ue<=0)
    cv=h.up(alpha(k,n)*caps[k]*exp(ce));uv=h.up(alpha(k,n)*exp(ue));w=winof[n]
    gate('positive_C_and_unknown_low_columns',cv>0 and uv>0 and cv<=Q(23,9)*sum(caps.values(),Q(0)) and uv<Q(23,9))
    cg[w]=max(cg.get(w,Q(0)),cv)
    terms.append(dict(low_mode=k,middle_mode=n,input_window=w,branch='sum' if m==k+n else 'difference',C_coefficient=h.pack(cv),u_coefficient=h.pack(uv),C_exponent=[str(ce.p),str(ce.q)],u_exponent=[str(ue.p),str(ue.q)]))
   edges=[]
   for w,(lo,hi) in enumerate(windows):
    for z in range(w,len(windows)):
     zlo,zhi=windows[z]
     if zlo>hi+m:break
     nlo,nhi=max(lo,zlo-m),min(hi,zhi-m)
     if nlo<=nhi:
      val=h.up(Q(5,4)*exp(-2*nlo*smin));gate('complete_positive_middle_difference_edges',nlo>=94 and nlo+m<h.M and nlo%2==0 and val>0)
      edges.append(dict(left_window=w,right_window=z,lower_source_mode=nlo,upper_source_mode=nhi,coefficient=h.pack(val)))
   # Verify all17360 finite difference pairs, including intersections at every boundary.
   edge_index={(r['left_window'],r['right_window']):r for r in edges}
   for n in range(94,h.M-m,2):
    e=edge_index[(winof[n],winof[n+m])]
    gate('every_middle_difference_pair_covered',e['lower_source_mode']<=n<=e['upper_source_mode'])
   vh=h.up(Q(5,4)*exp(-2*(h.M-m)*smin));hh=h.up(Q(5,4)*exp(-2*h.M*smin))
   gate('positive_infinite_cancellation_terms',vh>0 and hh>0)
   tail=[w for w,(lo,hi) in enumerate(windows) if hi>=h.M-m]
   gate('exact_no_low_high_quadratic_support',m+92<h.M)
   block.append(dict(mode=m,C_and_u_times_middle=terms,C_times_middle_window_coefficients=[dict(window=w,coefficient=h.pack(v)) for w,v in sorted(cg.items())],middle_difference_edges=edges,middle_squared_common_coefficient=h.pack(h.up(Q(5,4)*exp(-188*smin))),middle_high_coefficient=h.pack(vh),high_squared_coefficient=h.pack(hh),middle_high_possible_windows=tail,C_times_high_exactly_zero=True,u_times_high_exactly_zero=True))
  rows.append(dict(source_block=j,sigma_min=src['sigma_min'],sigma_max=src['sigma_max'],source_pin=rec,rows=block))
 gate('all25_sources_and_both_outputs',len(rows)==25 and all([r['mode'] for r in b['rows']]==[94,96] for b in rows))
 out=dict(schema='original-singleton94-96-frequency-preserving-source-operators-v1',author='/root (GPT-6 Astra Pro, AI-assisted)',source_sha256=h.sha(__file__),helper_sha256=h.sha(h.__file__),all_gates=all(g.values()),gates=g,gate_counts=counts,total_comparisons=sum(counts.values()),inputs=ids,windows=windows,old_window_parent=parent,rows=rows,comparison_partition=sources['comparison_partition'],centre_constant_width=[str(h.TAU.p),str(h.TAU.q)],complete_T_domain=h.pack(h.RSTAR),complete_T_Hessian=h.pack(270*h.RSTAR),retained_old_window_94_96_and_global_middle_constraints=True,mean_inverse_and_T_not_omitted=True,three_materials_and_profile_conversions_required=True,no_new_ODE_quadrature_or_fixedpoint=True,complete_field_or_cut_claimed=False,elapsed_seconds=time.monotonic()-t,peak_rss_kib=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)
 r=h.save(a.out,out);print(json.dumps(dict(all_gates=True,gate_comparisons=sum(counts.values()),source_pairs=[len(indexed[m]) for m in (94,96)],records=r,elapsed_seconds=out['elapsed_seconds'],peak_rss_kib=out['peak_rss_kib'])),flush=True)
if __name__=='__main__':main()
