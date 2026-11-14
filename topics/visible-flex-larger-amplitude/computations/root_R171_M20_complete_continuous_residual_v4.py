#!/usr/bin/env python3
"""Full original-equation residual of the exact R170 Hermite centre.

All original real-background leaves, complete nonlinear mean, a finite
Laurent inverse with a positive infinite remainder, and all high modes.
No ODE, source quadrature, Newton solve, or finite-angle sampling is used.
Author: /root (GPT-6 Astra Pro; AI-assisted), 2026-11-13.
"""
import argparse
from fractions import Fraction as F
import gzip
import hashlib
import importlib.util
import json
from pathlib import Path
import resource
import sys
import time
from flint import arb, arb_poly, ctx, fmpq

def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def read(p):
    p=Path(p);b=p.read_bytes();return json.loads(gzip.decompress(b) if p.suffix=='.gz' else b)
def ar(x):return arb(fmpq(x.numerator,x.denominator))
def ep(v):
    return arb((int(v[0]),int(v[1]))) if isinstance(v,list) else arb((int(v['mantissa']),int(v['binary_exponent'])))
def ball(v):return ep(v['lower']).union(ep(v['upper']))
def point(v):
    m,e=v.man_exp();return [str(m),int(e)]
def rec(v):return dict(lower=point(v.lower()),upper=point(v.upper()))
def up(v):return v.upper()
def intersect(a,b):
    lo,hi=max(a.lower(),b.lower()),min(a.upper(),b.upper())
    if lo>hi:raise ArithmeticError('Enclosures of the same root are disjoint')
    return lo.union(hi)
def norm(poly,offset,sigma,degree=0):
    return up(sum((abs(v)*(1+2*abs(i+offset))**degree*(2*abs(i+offset)*sigma).exp()
                   for i,v in enumerate(poly.coeffs())),arb(0)))
def save(p,d):
    if p.exists():raise FileExistsError(p)
    raw=(json.dumps(d,separators=(',',':'))+'\n').encode()
    p.write_bytes(gzip.compress(raw,mtime=0) if p.suffix=='.gz' else raw)
    return dict(path=str(p),sha256=sha(p),bytes=p.stat().st_size,uncompressed_bytes=len(raw))

def main():
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--inputs',type=Path,required=True)
    ap.add_argument('--out-prefix',type=Path,required=True)
    ap.add_argument('--inverse-order',type=int,default=32)
    ap.add_argument('--start-row',type=int,required=True)
    ap.add_argument('--end-row',type=int,required=True)
    ap.add_argument('--rss-kib',type=int,default=131072)
    a=ap.parse_args();started=time.monotonic();ctx.prec,ctx.threads=256,1
    if any(a.out_prefix.parent.glob(a.out_prefix.name+'*')):raise FileExistsError('Fresh residual prefix required')
    ids=read(a.inputs);counts={}
    def gate(k,v):
        counts[k]=counts.get(k,0)+1
        if not v:raise ArithmeticError(k)
    for k,v in ids['files'].items():gate('input_identity_'+k,sha(v['path'])==v['sha256'])
    get=lambda k:read(ids['files'][k]['path'])
    mean=get('R170');owned=get('R170_resource');mi=get('R170_inputs')
    gate('actual_complete_mean_domain',owned['exitcode']==0 and mean['all_gates'] and mean['gate_count']==40537
         and mean['source_sha256']==ids['files']['R170_source']['sha256']
         and mean['input_manifest_sha256']==ids['files']['R170_inputs']['sha256']
         and mean['original_background_leaves']==3940 and mean['refined_leaves']==3976)
    gate('same_explicit_polynomials',mean['polynomial_file']['sha256']==ids['files']['polynomials']['sha256'])
    spec=importlib.util.spec_from_file_location('same_R170_polynomial',ids['files']['R170_source']['path'])
    h=importlib.util.module_from_spec(spec);spec.loader.exec_module(h)
    original_sources=read(mi['files']['original_source_manifest']['path'])
    for rr in original_sources['source_files']:gate('original_source_file',sha(rr['path'])==rr['sha256'])
    ready_ref=mi['files']['original_ready'];gate('same_original_ready',sha(ready_ref['path'])==ready_ref['sha256'])
    sys.path.insert(0,mi['original_sources_directory'])
    from tail_r33_middle_ordered_physical import SourceValues
    from closure_real_linear_head_enclosure import PositiveKernels
    original_bg=SourceValues(read(ready_ref['path']));kernels=PositiveKernels(original_bg,12,92)
    original_bg.cells={n:kernels.source_cell(n) for n in (7,8,9)}
    polys={}
    for r in get('polynomials')['rows']:
        def unpack(name):return [[F(int(v[0]),int(v[1])) for v in row] for row in r[name]]
        polys[r['cell'],r['segment'],r['part']]=(unpack('exact_P_Bernstein'),unpack('exact_K_Bernstein'))
    domain={(r['cell'],r['segment'],r['left'],r['right']):r for r in mean['rows']}
    gate('all_original3976_domain_rows',len(domain)==3976 and len(polys)==216)
    gate('declared_complete_batch_range',0<=a.start_row<a.end_row<=3976)
    key_of=lambda row:(row['cell'],row['segment'],row['left'],row['right'])
    global_indices={key_of(row):i for i,row in enumerate(mean['rows'])}
    selected=mean['rows'][a.start_row:a.end_row]
    selected_keys={key_of(row) for row in selected}
    needed_chunks={row['source_profile_sha256'] for row in selected}
    seen_keys=set()
    sigma=arb(1)/64;wide=arb(1)/2;delta=wide-sigma;M=20;Q=a.inverse_order
    gate('finite_inverse_and_strict_wider_strip',Q>=1 and delta>0)
    weights=[up((1+m)*(sigma*m).exp()) for m in range(2,93,2)]
    tail_decay=up((-94*delta).exp());all_chunks=[];buffer=[];count=oldcount=0;cell_results=[];maxima={}
    def maxrec(name,v,ident):
        v=up(v)
        if name not in maxima or v>ep(maxima[name]['upper']):maxima[name]=dict(upper=point(v),where=ident)
    def flush():
        if buffer:
            all_chunks.append(save(Path(str(a.out_prefix)+f'-rows-{len(all_chunks):04d}.json.gz'),
                dict(schema='full-original-residual-Hermite-M20-rows-v1',rows=list(buffer))))
            buffer.clear()
    for n in (9,8,7):
        ref=mi['files']['profile_'+str(n)];gate('same_original_profile_'+str(n),sha(ref['path'])==ref['sha256'])
        profile=read(ref['path']);lowL1=highL1=commonL1=arb(0);seen=0
        for chunk in profile['profile_chunks']:
            if chunk['sha256'] not in needed_chunks:continue
            gate('same_original_profile_chunk',sha(chunk['path'])==chunk['sha256'])
            for raw in read(chunk['path'])['rows']:
                lo,hi=F(raw['left']),F(raw['right']);j=raw['segment'];oldcount+=1
                cuts=[lo]+[F(k,8) for k in range(1,8) if lo<F(k,8)<hi]+[hi]
                if not any((n,j,str(ll),str(rr)) in selected_keys for ll,rr in zip(cuts,cuts[1:])):continue
                r=ball(raw['whole_radius']);w=ball(raw['whole_w']);E=1+w*w;z=w*w
                rx=ball(raw['radius_x']);rx_positive_lower=rx.lower()
                if not rx_positive_lower>0:
                    bg=original_bg.cells[n]['segments'][j]
                    q=original_bg.source_point(bg,ar(lo).union(ar(hi)));Eq=1+q['w']**2
                    positive_part=original_bg.alpha*q['ro_x']/Eq
                    rx_positive_lower=max(rx.lower(),positive_part.lower())
                    direct_upper=up(abs(q['w']*q['log_w_x'])/(8*Eq*Eq.sqrt())+positive_part)
                    right_upper=min(rx.upper(),direct_upper)
                    gate('same_real_radius_derivative_positive_intersection',rx_positive_lower>0 and right_upper>=rx_positive_lower)
                    # An Arb midpoint-radius enclosure may straddle zero even
                    # with a strictly positive exact endpoint lower bound.
                    # Keep that enclosure; record/pay positivity separately.
                    rx=rx_positive_lower.union(right_upper)
                s=rx/r;ell=ball(raw['log_w_x']);zmax=up(z);Emax=up(E)
                gate('actual_positive_real_background',r>0 and w>0 and w<arb(1)/2 and rx_positive_lower>0 and Emax<=arb(5)/4)
                for left,right in zip(cuts,cuts[1:]):
                    part=min(7,int(left*8));t0,t1=left*8-part,right*8-part
                    key=(n,j,str(left),str(right))
                    if key not in selected_keys:continue
                    gate('selected_leaf_not_repeated',key not in seen_keys);seen_keys.add(key)
                    dm=domain[key]
                    gate('same_complete_mean_leaf',dm['source_profile_sha256']==chunk['sha256'] and dm['all_domain_gates'])
                    P,K=polys[n,j,part];ps=[];ks=[];pds=[];kds=[];p0=k0=tbar=q0=arb(0)
                    for i,m in enumerate(range(2,41,2)):
                        pv=h.hull([ar(v) for v in h.restrict(P[i],t0,t1)])
                        kv=h.hull([ar(v) for v in h.restrict(K[i],t0,t1)])
                        pd=8*h.hull([ar(v) for v in h.restrict(h.derivative(P[i]),t0,t1)])
                        kd=8*h.hull([ar(v) for v in h.restrict(h.derivative(K[i]),t0,t1)])
                        ps.append(pv);ks.append(kv);pds.append(pd);kds.append(kd)
                        p0+=abs(pv);k0+=abs(kv);tbar+=m*abs(pv);q0+=(kv*kv+E*pv*pv)/4+m*kv*pv/2
                    p0,k0,tbar=map(up,(p0,k0,tbar))
                    # The full mean root is already unique in the R170 disk.
                    # Refine its real interval using the exact scalar identity,
                    # retaining the complete binomial/inverse remainder each time.
                    d=min(arb(1)/8,ep(dm['root_absolute']));c=(-d).union(d);mean_err=arb(0)
                    for iteration in range(4):
                        Ac=up(2*(k0+d)+(k0+d)**2+Emax*p0*p0);U=up(zmax*Ac);V=up(zmax*p0*p0);Y=up((1+d+k0)*tbar)
                        gate('complete_mean_remainder_series',0<=U<1 and 0<=V<1)
                        f,g=h.f_and_g(U);mean_err=up(Ac*f+Y*(g+V)/(1-V));q=q0+(-mean_err).union(mean_err)
                        gate('same_real_quadratic_branch',1-2*q>0)
                        newc=-2*q/(1+(1-2*q).sqrt());c=intersect(c,newc);d=up(abs(c))
                    ka=[arb(0) for _ in range(41)];ta=ka.copy();pa=ka.copy();ua=ka.copy();ka[20]=c
                    for i,m in enumerate(range(2,41,2)):
                        kidx=i+1;ka[20+kidx]=ka[20-kidx]=ks[i]/2;ta[20+kidx]=ta[20-kidx]=m*ps[i]/2
                        pa[20+kidx]=ps[i]/2;pa[20-kidx]=-ps[i]/2
                        ua[20+kidx]=(m*ks[i]+ps[i])/2;ua[20-kidx]=-(m*ks[i]+ps[i])/2
                    KP,TP,PI,UI=map(arb_poly,(ka,ta,pa,ua));LP=KP+E*TP;LP[20]=0
                    scalar=1+c;amin=scalar.lower();ell0=norm(LP,-20,wide)
                    # Use the directly summed derivative norm: subtracting two
                    # unrelated upper endpoints would not be a valid bound.
                    elld=up(sum((2*abs(i-20)*abs(v)*(2*abs(i-20)*wide).exp() for i,v in enumerate(LP.coeffs())),arb(0)))
                    gate('complete_inverse_on_wide_strip',amin>0 and 0<=ell0<amin)
                    x=up(ell0/amin);yd=up(elld/amin)
                    rt0=up(x**(Q+1)/(amin*(1-x)))
                    rt1=up(rt0+((Q+1)*x**Q*yd/(1-x)+x**(Q+1)*yd/(1-x)**2)/amin)
                    gate('positive_infinite_inverse_remainder',rt1>0)
                    GP=LP*(-1/scalar);inv=arb_poly([1]);offset=0
                    for order in range(Q):
                        inv=GP*inv;offset-=20;inv[-offset]+=1
                    inv=inv*(1/scalar)
                    BS=-E*(UI*UI)
                    BL=(KP+TP)*(KP+TP)+z*(2*KP*TP+TP*TP+PI*PI)
                    bs1,bl1=norm(BS,-40,wide,1),norm(BL,-40,wide,1)
                    inverse1=up(1/(amin-ell0)+elld/(amin-ell0)**2)
                    Ns1,Nl1=up(bs1*inverse1),up(bl1*inverse1)
                    remS,remL=up(bs1*rt1),up(bl1*rt1)
                    NS,NL=BS*inv,BL*inv;noff=offset-40
                    low=[];finite_norm=arb(0)
                    for i,m in enumerate(range(2,93,2)):
                        index=m//2-noff;ns=2*NS[index];nl=2*NL[index]
                        pv,kv,pd,kd=(ps[i],ks[i],pds[i],kds[i]) if i<20 else (arb(0),)*4
                        RP=pd+(s+ell)*pv+m*s*kv
                        RK=kd+m*ell*pv+2*ell*kv-s*ns-ell*nl
                        finite_norm+=weights[i]*(abs(RP)+abs(RK))
                        low.append(dict(mode=m,exact_finite_P_residual=rec(RP),finite_inverse_K_residual=rec(RK)))
                    common=up(abs(s)*remS+abs(ell)*remL)
                    low_norm=up(finite_norm+common)
                    high_norm=up((abs(s)*Ns1+abs(ell)*Nl1)*tail_decay)
                    gate('complete_positive_high_source',high_norm>0 and low_norm>=0 and all(v.is_finite() for v in [low_norm,high_norm,common]))
                    dx=ar(right-left);lowL1+=dx*low_norm;highL1+=dx*high_norm;commonL1+=dx*common
                    ident=dict(cell=n,segment=j,part=part,left=str(left),right=str(right),global_leaf_index=global_indices[key]);count+=1;seen+=1
                    buffer.append(dict(**ident,original_profile_sha256=chunk['sha256'],mean_root=rec(c),complete_mean_remainder=point(mean_err),
                        wide_inverse_mass=point(x),inverse_tail_W1=point(rt1),complete_source_s_W1_wide=point(Ns1),complete_source_ell_W1_wide=point(Nl1),
                        finite_inverse_residuals=low,common_complete_low_remainder_W1=point(common),
                        low46_complete_residual_W1=point(low_norm),all_modes94_and_above_residual_W1=point(high_norm),
                        radius=rec(r),w=rec(w),radius_x_positive_lower=point(rx_positive_lower),source_s=rec(s),source_ell=rec(ell)))
                    maxrec('wholeleaf_low_residual',low_norm,ident);maxrec('wholeleaf_high_residual',high_norm,ident);maxrec('wide_inverse_mass',x,ident)
                    if len(buffer)>=32:flush()
                    if count%200==0:print(json.dumps(dict(event='actual_complete_residual',leaves=count,cell=n,elapsed_seconds=time.monotonic()-started,peak_rss_kib=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)),flush=True)
                    if resource.getrusage(resource.RUSAGE_SELF).ru_maxrss>a.rss_kib:raise MemoryError('Preserve declared128MiB resource cap')
        cell_results.append(dict(cell=n,leaves=seen,low46_complete_L1_residual=point(up(lowL1)),high94_infinite_complete_L1_residual=point(up(highL1)),common_inverse_tail_L1=point(up(commonL1))))
        print(json.dumps(dict(event='complete_cell_residual',cell=n,low_L1=float(up(lowL1)),high_L1=float(up(highL1)),elapsed_seconds=time.monotonic()-started)),flush=True)
    flush();gate('all_declared_selected_leaves',count==a.end_row-a.start_row and seen_keys==selected_keys)
    result=dict(schema='R170-full-original-equation-continuous-residual-owned-batch-v1',author='/root (GPT-6 Astra Pro; AI-assisted)',
        inputs=ids,input_manifest_sha256=sha(a.inputs),source_sha256=sha(__file__),all_gates=True,gate_count=sum(counts.values()),gate_categories=counts,
        precision_bits=ctx.prec,finite_inverse_order=Q,output_sigma='1/64',complete_source_sigma='1/2',
        original_leaves_seen_in_selected_files=oldcount,refined_leaves=count,batch_range=[a.start_row,a.end_row],whole_R170_refined_leaves=3976,whole_domain_completion_claimed=False,cell_results=cell_results,maxima=maxima,profile_chunks=all_chunks,
        residual_definition='RP=P_x+(s+ell)P+m*s*K; RK=K_x+m*ell*P+2*ell*K-Pi_perp[(E*s*(Ktheta-P)^2+ell*((K+Ptheta)^2+w^2*(2K*Ptheta+Ptheta^2-P^2)))/(1+K+E*Ptheta)]. K=c+barK and c is the complete original mean root.',
        complete_nontruncated_mean_and_inverse=True,complete_positive_infinite_modes94_and_above=True,
        only_exact_candidate_residual_not_actual_R143_solution_error=True,no_new_ODE_BVP_or_background_quadrature=True,
        unweighted_L1_not_an_evolution_kernel_bound=True,nonlinear_tube_selfmap_and_actual_entry_unpaid=True,
        elapsed_seconds=time.monotonic()-started,peak_rss_kib=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)
    out=Path(str(a.out_prefix)+'-certificate.json.gz');info=save(out,result)
    print(json.dumps(dict(primary=info,all_gates=True,gate_count=result['gate_count'],cell_results=[{**v,'low_display':float(ep(v['low46_complete_L1_residual'])),'high_display':float(ep(v['high94_infinite_complete_L1_residual']))} for v in cell_results],elapsed_seconds=result['elapsed_seconds'],peak_rss_kib=result['peak_rss_kib'])),flush=True)

if __name__=='__main__':main()
