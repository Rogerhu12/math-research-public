#!/usr/bin/env python3
"""Actual warm .25 stage 0: the shared physical-R map and true metric.

Uses the frozen stage127 exact polynomial library, without changing its
shared-node rule. All Fourier modes stay in the map and in the linear Gram
terms. Only the quadratic Gram expansion is split into exact low-mode
polynomials and an explicitly bounded high-mode remainder.
"""
import argparse
from fractions import Fraction as Q
import hashlib
import importlib.util
import json
import math
from pathlib import Path
import sys
import time


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def product(a, b):
    out = [Q(0)] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            out[i+j] += x*y
    return out


def physical_background_box(o, data):
    """Cut is exact; strictly enclose the inner literal R knot in (0,8)."""
    rlo = Q.from_float(data['nodes'][0]['radiusJS'])
    rhi = Q.from_float(data['nodes'][-1]['radiusJS'])
    rc = Q.from_float(o.constants['parameters']['rCut'])
    if rhi != rc:
        raise ValueError('Cut radius differs: explicit canonicalization is required')
    delta = Q(1, 10**6)
    for _ in range(16):
        left_x = Q(15,16)-delta
        left = o.primitives(0,8,left_x)['r']
        if o.hi(left) < o.lo(o.qi(rlo)):
            break
        delta *= 2
    else:
        raise ArithmeticError('Could not cover the inner literal R knot')
    if delta >= Q(1,100):
        raise ArithmeticError('Unexpectedly large source cover')
    j = o.local_jets(0,8,left_x,1)
    w = j['w']
    monotone = o.hi(j['w_x']) < 0
    if monotone:
        w = o.k.hull([o.local_jets(0,8,left_x)['w'],o.local_jets(0,8,1)['w']])
    from q060_true_background_oracle import mpf_fraction
    w0 = Q.from_float(float((o.lo(w)+o.hi(w))/2))
    dw = max(abs(mpf_fraction(o.lo(w))-w0),abs(mpf_fraction(o.hi(w))-w0))
    return {
        'literal_R_bounds_exact':[str(rlo),str(rhi)],
        'source_cover':[0,8,str(left_x),'1'],
        'left_true_radius':o.bounds(left),
        'cut_radius_matches_true_Rc_exactly':True,
        'strict_monotone_radius_cover':True,
        'w_x_negative_on_source_cover':monotone,
        'w_range':o.bounds(w),
        'auxiliary_w0_exact':str(w0),'absolute_w_minus_w0_upper_exact':str(dw),
        'w0_scope':'Exact decomposition center only; true w(R), alpha and target g stay unchanged'
    },w0,dw


def main():
    ap=argparse.ArgumentParser(description=__doc__)
    for name in ('data','packet','constants','normalization-certificate','library','out'):
        ap.add_argument('--'+name,type=Path,required=True)
    ap.add_argument('--quadratic-mode-cutoff',type=int,default=12)
    a=ap.parse_args();started=time.monotonic()
    sys.path.insert(0,str(a.library.parent))
    spec=importlib.util.spec_from_file_location('stage127_frozen_library',a.library)
    lib=importlib.util.module_from_spec(spec);spec.loader.exec_module(lib)
    from q060_true_background_oracle import Q060TrueBackgroundOracle
    o=Q060TrueBackgroundOracle(a.constants,a.normalization_certificate)
    d=json.loads(a.data.read_text());p=json.loads(a.packet.read_text())
    if (d['stage'],d['rawCell'],d['rawSegment'],d['rawLeft'],d['rawRight'])!=(0,0,8,15/16,1):
        raise ValueError('This certificate is only for saved stage 0')
    assert d['inputSHA256']==sha(a.packet)
    assert p['all_stage_input_maximum_difference']==0
    assert p['checkpoint']['sha256']=='302662026a7e213647d8bfb2813f970174c8c919bb6f4d406e073ef9f3c110de'
    assert p['checkpoint']['converged'] and p['checkpoint']['residual']<2e-9
    assert d['finiteScope']['M']==24 and d['finiteScope']['quadrature']==512
    assert all(d['physicalParameters'].get(k)==v for k,v in o.constants['parameters'].items())
    assert a.quadratic_mode_cutoff>=0
    cover,w0,dw=physical_background_box(o,d)
    print(json.dumps({'phase':'true_background_cover','cover':cover,'seconds':time.monotonic()-started}),flush=True)
    pm,hm=list(map(int,d['planarModes'])),list(map(int,d['heightModes']))
    P=len(pm);modes=pm+hm;C=len(modes)
    nodes,mids=d['nodes'],d['midpoints']
    radii=[Q.from_float(n['radiusJS']) for n in nodes]
    assert len(mids)==len(nodes)-1 and all(y>x for x,y in zip(radii,radii[1:]))
    low_p=[i for i,m in enumerate(pm) if abs(m)<=a.quadratic_mode_cutoff]
    low_h=[j for j,m in enumerate(hm) if m<=a.quadratic_mode_cutoff]
    low=set(low_p+[P+j for j in low_h]);high=set(range(C))-low
    rows=[];identities=0;maximum_metric=Q(0);maximum_eta_sq=Q(0);maximum_beta_sq=Q(0);maximum_v=Q(0)
    midpoint_max=[Q(0)]*3
    for index,(left,right,mid) in enumerate(zip(nodes,nodes[1:],mids)):
        r0,r1=radii[index:index+2];h=r1-r0
        deriv=[[],[],[]];norm=[[],[],[]]
        for c in range(C):
            l=[Q.from_float(v[c]) for v in left['coefficients']]
            r=[Q.from_float(v[c]) for v in right['coefficients']]
            poly=lib.hermite(*l,*r,h)
            for order in range(3):
                pp=lib.derivative(poly,h,order)
                assert lib.evaluate(pp,Q(0))==l[order] and lib.evaluate(pp,Q(1))==r[order]
                identities+=2;deriv[order].append(pp);norm[order].append(lib.bernstein_abs(pp))
        # Entire linear Gram numerator, same frequencies merged exactly.
        aa,bb,cc={},{},{}
        for i,m in enumerate(pm):
            lib.harmonic_add(aa,m-1,lib.scale(deriv[1][i],2))
            lib.harmonic_add(bb,m-1,lib.add(lib.radius_product(deriv[1][i],r0,h),lib.scale(deriv[0][i],-m)),sine=True)
            lib.harmonic_add(cc,m-1,lib.scale(lib.radius_product(deriv[0][i],r0,h),2*m))
        for j,m in enumerate(hm):
            lib.harmonic_add(aa,m,lib.scale(deriv[1][P+j],2*w0))
            lib.harmonic_add(bb,m,lib.scale(deriv[0][P+j],-w0*m),sine=True)
        linear_only=[sum((lib.bernstein_abs(v) for v in z.values()),Q(0)) for z in (aa,bb,cc)]
        # Exact quadratic low-mode terms; all pairs, including both orders.
        for i in low_p:
            m=pm[i]
            for j in low_p:
                n=pm[j]
                lib.harmonic_add(aa,m-n,product(deriv[1][i],deriv[1][j]))
                lib.harmonic_add(bb,m-n,lib.scale(product(deriv[1][i],deriv[0][j]),n),sine=True)
                lib.harmonic_add(cc,m-n,lib.scale(product(deriv[0][i],deriv[0][j]),m*n))
        for i in low_h:
            m=hm[i]
            for j in low_h:
                n=hm[j]
                aij=lib.scale(product(deriv[1][P+i],deriv[1][P+j]),Q(1,2))
                bij=lib.scale(product(deriv[1][P+i],deriv[0][P+j]),-Q(n,2))
                cij=lib.scale(product(deriv[0][P+i],deriv[0][P+j]),Q(m*n,2))
                lib.harmonic_add(aa,m-n,aij);lib.harmonic_add(aa,m+n,aij)
                lib.harmonic_add(bb,n+m,bij,sine=True);lib.harmonic_add(bb,n-m,bij,sine=True)
                lib.harmonic_add(cc,m-n,cij);lib.harmonic_add(cc,m+n,lib.scale(cij,-1))
        merged=[sum((lib.bernstein_abs(v) for v in z.values()),Q(0)) for z in (aa,bb,cc)]
        v=sum(norm[0],Q(0));vr=sum(norm[1],Q(0));vt=sum((abs(m)*n for m,n in zip(modes,norm[0])),Q(0))
        vrr=sum(norm[2],Q(0));vrt=sum((abs(m)*n for m,n in zip(modes,norm[1])),Q(0));vtt=sum((m*m*n for m,n in zip(modes,norm[0])),Q(0))
        rl=sum((norm[1][i] for i in low),Q(0));rh=sum((norm[1][i] for i in high),Q(0))
        tl=sum((abs(modes[i])*norm[0][i] for i in low),Q(0));th=sum((abs(modes[i])*norm[0][i] for i in high),Q(0))
        hz_r=sum(norm[1][P:],Q(0));hz_t=sum((m*n for m,n in zip(hm,norm[0][P:])),Q(0))
        remainder=[2*rl*rh+rh*rh,rl*th+rh*tl+rh*th,2*tl*th+th*th]
        A=merged[0]+2*dw*hz_r+remainder[0]
        B=(merged[1]+dw*hz_t+remainder[1])/r0
        Cbound=(merged[2]+remainder[2])/(r0*r0)
        metric=max(A,Cbound)+B
        eta_sq=vr*vr+(vt/r0)**2
        h11=vrr+Q(82,25)*vr;h12=(vrt+vt/r0)/r0;h22=vtt/(r0*r0)+vr/r0
        beta_sq=h11*h11+2*h12*h12+h22*h22
        t=(Q.from_float(mid['radiusJS'])-r0)/h
        assert 0<t<1
        md=[]
        for order in range(3):
            gap=sum((abs(lib.evaluate(deriv[order][i],t)-Q.from_float(mid['coefficients'][order][i])) for i in range(C)),Q(0))
            md.append(gap);midpoint_max[order]=max(midpoint_max[order],gap)
        maximum_metric=max(maximum_metric,metric);maximum_eta_sq=max(maximum_eta_sq,eta_sq)
        maximum_beta_sq=max(maximum_beta_sq,beta_sq);maximum_v=max(maximum_v,v)
        rows.append({'span':index,'R_exact':[str(r0),str(r1)],'metric_upper_exact':str(metric),
            'linear_only_numerator_l1_exact':list(map(str,linear_only)),
            'merged_linear_and_low_quadratic_numerator_l1_exact':list(map(str,merged)),
            'high_quadratic_remainders_exact':list(map(str,remainder)),
            'relative_Gram_component_upper_exact':list(map(str,(A,B,Cbound))),
            'eta_squared_exact':str(eta_sq),'beta_squared_exact':str(beta_sq),
            'midpoint_jet_gap_exact':list(map(str,md))})
        print(json.dumps({'span':index,'metric_upper':float(metric),'eta_upper_proxy':math.sqrt(float(eta_sq)),
            'beta_upper_proxy':math.sqrt(float(beta_sq)),'seconds':time.monotonic()-started}),flush=True)
    eta=o.iv.sqrt(o.qi(maximum_eta_sq));beta=o.iv.sqrt(o.qi(maximum_beta_sq))
    assert o.hi(eta)<1
    curvature=(8+beta)/(1-eta)**2
    href=Q(7446320975220351,288230376151711744)
    rbg=o.iv.sqrt(o.qi(Q(3,10)**2+(Q(32,25)+href)**2))
    radius=rbg+o.qi(maximum_v)
    support=o.qi(Q(1,11))-rbg*o.iv.sqrt(o.qi(2))*eta-o.qi(maximum_v)
    result={'status':'actual_stage0_shared_R_continuous_metric_certified' if maximum_metric<Q(1,10**6) else 'actual_stage0_metric_gate_not_proved',
        'source_sha256':sha(__file__),'data_sha256':sha(a.data),'packet_sha256':sha(a.packet),'library_sha256':sha(a.library),
        'checkpoint_sha256':p['checkpoint']['sha256'],'native_record_sha256':p['native_record']['sha256'],
        'oracle_provenance':o.provenance,'background_cover':cover,
        'source_stage':0,'M':24,'spacing':3,'spans':len(rows),'shared_two_jet_scalar_equalities':identities,
        'all_nodes_retained':True,'all_Fourier_modes_retained':True,'quadratic_mode_cutoff':a.quadratic_mode_cutoff,
        'exact_quadratic_low_terms':len(low),'bounded_quadratic_high_terms':len(high),
        'continuous_metric_operator_upper':o.bounds(o.qi(maximum_metric)),
        'normalized_first_jet_upper':o.bounds(eta),'normalized_covariant_Hessian_upper':o.bounds(beta),
        'principal_curvature_upper':o.bounds(curvature),'position_perturbation_upper':o.bounds(o.qi(maximum_v)),
        'conditional_radius_upper':o.bounds(radius),'conditional_support_lower':o.bounds(support),
        'background_cut_height_window_exact':['1/10','32/25'],
        'mean_definition':d['meanDefinition'],'upper_map':'Reflect all height terms and the true background together; metric/curvature unchanged',
        'inner_node_canonical':'Exact stage0 node0 selected also for stage1 outer endpoint; no re-evaluation or mean reset',
        'outer_cut_radius_canonical':'Same exact binary .3 as the true background',
        'midpoint_literal_jet_gaps':[o.bounds(o.qi(x)) for x in midpoint_max],
        'planar_rr_scope':'Finite FD outputs selected as the new shared-Hermite nodal parameters; no exact original PDE derivative claim',
        'new_nonlinear_solves':0,'global_tail_completed':False,'full_H':False,'Cartesian_prefix_seam':False,
        'rows':rows,'seconds':time.monotonic()-started}
    a.out.write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({'status':result['status'],'metric':result['continuous_metric_operator_upper'],
        'K':result['principal_curvature_upper'],'radius':result['conditional_radius_upper'],'support':result['conditional_support_lower'],
        'seconds':result['seconds'],'output_sha256':sha(a.out)}),flush=True)


if __name__=='__main__':
    main()
