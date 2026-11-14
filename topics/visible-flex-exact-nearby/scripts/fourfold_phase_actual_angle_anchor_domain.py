#!/usr/bin/env python3
"""Actual single-germ angular anchors and wider whole-angle time domains.

At u=0, directed true D and D_theta grids plus a continuous D_theta_theta
bound prove Re D>0 on both boundaries of a periodic strip. Harmonic minimum
then gives its entire interior. The actual time variation is paid separately
by complete Fourier/time tails. No cross-parameter R59 anchor is reused.
"""
from __future__ import annotations
import argparse
from fractions import Fraction
import gzip
import json
from pathlib import Path
from types import SimpleNamespace
import time

import numpy as np
from flint import arb,acb,ctx

from fourfold_phase_beta_affine import AffineBulkTarget,sha
from fourfold_phase_beta_bulk_interval import exact_arb,complex_pad
from fourfold_phase_beta_interval import ball_record
from fourfold_phase_field_time_refined_root import prepare_refined_root
from fourfold_phase_field_time_turn_collar import PiTime
from fourfold_phase_full_angle_time_domain import document,hashed
from fourfold_phase_full_angle_sine_domain import invariant_enclosures
from fourfold_phase_sharp_time_domain_cover import sharp_cover,write_report
from fourfold_phase_sine_time_geometry import SineGermTimeModel,whole_angle_outer_invariants
from fourfold_phase_time_outer_taylor_gate import time_disk_range


def static_grid(model,N,y):
    """True X and exact finite phases at u=0, on a physical angular circle."""
    if N<model.nodes or N&(N-1):raise ValueError('power-of-two grid at least as long as primitive required')
    y=exact_arb(y)
    _,_,_,error=model.image_and_X_error([acb(0,y)])
    coefficients=np.empty((N,3),object)
    for key in np.ndindex(coefficients.shape):coefficients[key]=acb(0)
    for j,frequency in enumerate(model.target.frequency):
        if frequency%4:raise ValueError('quarter-period cylindrical primitive required')
        weight=(-frequency*y).exp()
        for c in range(3):coefficients[(frequency//4)%N,c]=model.X_coefficient[j,c][0]*weight
    X=model.target.fourier.fft(coefficients,inverse=True)*N
    for key in np.ndindex(X.shape):X[key]=complex_pad(X[key],error)
    # The phase derivatives are derivatives of known finite phase polynomials;
    # no spectral derivative of a sampled primitive or D is substituted.
    fields=[(0,0),(1,0),(2,0),(3,0),(0,1),(1,1),(0,2),(1,2)]
    coefficients=np.empty((N,len(fields)),object)
    for key in np.ndindex(coefficients.shape):coefficients[key]=acb(0)
    for k,values in enumerate(zip(model.beta,model.gamma,model.beta_r,model.gamma_r),1):
        if k>=N//2:raise ValueError('finite phase modes leave the unaliased grid')
        for sign in (-1,1):
            frequency=4*sign*k;weight=acb(0,-sign)*(-frequency*y).exp()/2
            for col,(base,order)in enumerate(fields):
                coefficients[(sign*k)%N,col]=values[base][0]*weight*acb(0,frequency)**order
    phase=model.target.fourier.fft(coefficients,inverse=True)*N
    return X,phase,error


def D_and_first(X,phase,a):
    beta,gamma,p,q,bt,u,btt,ut=phase
    sb,cb=beta.sin_cos();s,c=gamma.sin_cos()
    h=-sb*X[0]+cb*X[1];v=-cb*X[0]-sb*X[1]
    Q=c*X[2]-s*h;A=c*h+s*X[2];P=1+bt
    Q1=a*q-P*s*v-u*A;v1=a*c*p-P*h
    D=P*c*Q-u*v
    D1=btt*c*Q-P*s*u*Q+P*c*Q1-ut*v-u*v1
    return D,D1


def actual_anchor(model,N,width):
    """Periodic harmonic minimum, using rigorous real-direction grid gaps."""
    started=time.monotonic()
    # A constant-radial-point domain; the zero h is an explicit static object,
    # not an assertion that the actual time interval has vanishing width.
    point=SimpleNamespace(target=model.target,root=model.root,tau0=model.tau0,
        h=arb(0),center=model.center,R0=model.R0,RE=model.RE,sigma=model.sigma,nodes=model.nodes)
    coarse,_,_,info=whole_angle_outer_invariants(point,Fraction(1),width)
    B2=coarse['D2'];gap=(arb.pi()/(4*N)).upper()
    X,phase,Xerror=static_grid(model,N,width)
    node_min=arb.pos_inf();first_max=arb(0);linear_min=arb.pos_inf();critical=None
    for j in range(N):
        D,D1=D_and_first(X[j],phase[j],model.a[0])
        a=D.real.lower();b=abs(D1.real).upper();local=(a-gap*b).lower()
        node_min=min(node_min,a);first_max=max(first_max,b)
        if local<linear_min:
            linear_min=local;critical=dict(index=j,D_real_lower=ball_record(a),D_first_real_modulus=ball_record(b))
    quadratic=(B2*gap**2/2).upper();lower=(linear_min-quadratic).lower()
    return lower,dict(kind='actual_single_germ_periodic_harmonic_D_anchor',proved=bool(lower>0),
        actual_germ_span=list(map(str,model.cell)),physical_theta_strip=str(width),nodes=N,
        exact_grid='theta_j=pi*j/(2*N), nearest real displacement at most pi/(4*N)',
        radial_center=ball_record(model.center),primitive_infinite_error=ball_record(Xerror),
        minimum_node_ReD=ball_record(node_min),maximum_node_abs_ReDtheta=ball_record(first_max),
        minimum_node_linear_gap_lower=ball_record(linear_min),whole_strip_Dtheta2_modulus=ball_record(B2),
        real_grid_half_gap=ball_record(gap),quadratic_real_grid_fee=ball_record(quadratic),
        continuous_boundary_and_interior_ReD_lower=ball_record(lower),critical_grid_node=critical,
        both_boundaries_by_exact_reality=True,
        actual_holomorphy_without_D_division=True,
        coarse_static_inputs={k:ball_record(v)for k,v in info.items()},elapsed_seconds=time.monotonic()-started)


def widened_gate(model,N,K,R,S,width,wide,anchor_nodes):
    started=time.monotonic();base,anchor=actual_anchor(model,anchor_nodes,width)
    row=dict(common_span=list(map(str,model.cell)),anchor=anchor,passed=False)
    if not base>0:
        row['failure']='actual continuous angular anchor did not prove Re D positive'
        return row
    rows,coarse,KM,analytic_K,fees=invariant_enclosures(model,N,K,R,S,width,wide)
    Rb,Sb=exact_arb(R),exact_arb(S);D=rows[0]
    variation=(sum((D['full'][i]*Rb**i for i in range(1,model.precision)),arb(0))+D['time_tail']).upper()
    lower=(base-variation).lower()
    row.update(D_lower=ball_record(lower),actual_anchor_time_variation=ball_record(variation),
        time_and_Fourier_fees=fees,
        invariant_bounds={r['name']:dict(whole_strip_time_modulus=ball_record(r['modulus']),
            true_time_coefficient_norms=[ball_record(v)for v in r['full']],
            retained_DFT_coefficient_norms=[ball_record(v)for v in r['retained']],
            larger_time_narrow_angle_modulus=ball_record(r['narrow_modulus']),
            larger_time_wide_angle_modulus=ball_record(r['wide_modulus']),
            full_time_tail=ball_record(r['time_tail']))for r in rows})
    if not analytic_K:
        row['failure']='true K not holomorphic on the larger time disk';return row
    Krange,Ktail=time_disk_range(model.K,Rb,Sb,KM);positive=(-Krange).real.lower()
    row['curvature']=dict(kind='ordinary_negative_curvature',minus_K_real_lower=ball_record(positive),
        K_modulus=ball_record(abs(Krange).upper()),K_time_tail=ball_record(Ktail),K_outer_modulus=ball_record(KM))
    passed=bool(lower>0 and positive>0);row['passed']=passed
    if passed:
        rt=(abs(model.root)*(abs(model.h)*Rb).cosh()).upper();wave=abs(Krange).sqrt().upper()
        M,W=rows[1]['modulus'],rows[2]['modulus']
        f=(rt*(M+wave*W)/lower).upper()
        f1=(rt*((coarse['M1']+wave*coarse['W1'])/lower+(M+wave*W)*coarse['D1']/lower**2)).upper()
        f2=(rt*((coarse['M2']+wave*coarse['W2'])/lower+
            (2*(coarse['M1']+wave*coarse['W1'])*coarse['D1']+(M+wave*W)*coarse['D2'])/lower**2+
            2*(M+wave*W)*coarse['D1']**2/lower**3)).upper()
        row['true_field_moduli']={k:ball_record(v)for k,v in dict(f=f,f_theta=f1,f_theta2=f2).items()}
    row['elapsed_seconds']=time.monotonic()-started
    return row


def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--retarget',type=Path,required=True);p.add_argument('--leg',default='forward',choices=['forward','backward'])
    p.add_argument('--segment',type=int,default=419);p.add_argument('--widths',default='1/32,1/20')
    p.add_argument('--wide-widths',default='1/20,1/16');p.add_argument('--anchor-nodes',type=int,default=4096)
    p.add_argument('--angles',type=int,default=1024);p.add_argument('--cutoff',type=int,default=383)
    p.add_argument('--primitive-nodes',type=int,default=512);p.add_argument('--bits',type=int,default=192)
    p.add_argument('--time-order',type=int,default=40);p.add_argument('--time-radius',default='3')
    p.add_argument('--larger-time-radius',default='4');p.add_argument('--radial-radius',default='3/1000')
    p.add_argument('--E-radius',default='1/400');p.add_argument('--out',type=Path,required=True)
    args=p.parse_args();ctx.prec=args.bits;ctx.cap=max(21,args.time_order+4);started=time.monotonic()
    desc=document(args.retarget);op,obj=hashed(desc['target_object']);rp,_=hashed(desc['target_root'])
    gp,grid=hashed(desc['old_'+args.leg+'_reference'])
    a,b=map(PiTime.from_record,grid['exact_time_endpoints'][args.segment:args.segment+2]);c,h=(a+b)/2,(b-a)/2
    if c.p or h.p:raise ValueError('this ordinary actual-anchor driver requires interior rational times')
    R,S,R0,RE=map(Fraction,(args.time_radius,args.larger_time_radius,args.radial_radius,args.E_radius))
    widths=list(map(Fraction,args.widths.split(',')));wides=list(map(Fraction,args.wide_widths.split(',')))
    if len(widths)!=len(wides) or not S>R>1:raise ValueError('invalid analytic domains')
    package=prepare_refined_root(op,rp,nodes=args.primitive_nodes)
    target=AffineBulkTarget(op,args.primitive_nodes,args.primitive_nodes,exact_arb(R0),exact_arb(RE),exact_arb(Fraction(8,25)))
    cells,cover=sharp_cover(target,package.root,a,b)
    report=dict(kind='actual_single_germ_angular_anchors_and_wider_full_time_domains',complete=False,
        source_sha256=sha(__file__),retarget_descriptor_sha256=sha(args.retarget),target_object_sha256=sha(op),
        target_root_sha256=sha(rp),time_grid_sha256=sha(gp),exact_delta_fraction=str(package.exact_delta),
        exact_time_endpoints=[a.record(),b.record()],leg=args.leg,segment=args.segment,
        time_radius=str(R),larger_time_radius=str(S),radial_radius=str(R0),E_radius=str(RE),
        time_order=args.time_order,angles=args.angles,cutoff=args.cutoff,anchor_nodes=args.anchor_nodes,
        primitive_nodes=args.primitive_nodes,bits=args.bits,refined_root=package.provenance,
        sharp_real_germ_cover=cover,required_common_spans=[list(map(str,cell))for cell in cells],cases=[],
        dependency_sha256={name:sha(Path(__file__).with_name(name))for name in
            ['fourfold_phase_sharp_time_domain_cover.py','fourfold_phase_full_angle_sine_domain.py',
             'fourfold_phase_sine_time_geometry.py','fourfold_phase_uniform_field_time_grid.py',
             'fourfold_phase_uniform_field_time_grid_fast.py','fourfold_phase_time_outer_taylor_gate.py']},
        limitations=['A single exact affine point, the listed complete real time interval and true germs only',
            'Actual D anchor uses no transfer of a narrower parameter-box angular strip',
            'Continuous angular grid gaps and all infinite primitive/Fourier/time tails are paid',
            'Domain coefficients, not a true-flow, residual, KAM or PDE certificate'])
    def save():report['elapsed_seconds']=time.monotonic()-started;write_report(args.out,report)
    save()
    for width,wide in zip(widths,wides):
        if not 0<width<wide<Fraction(2,25):raise ValueError('angles leave the paid primitive source strip')
        case=dict(physical_theta_strip=str(width),wider_physical_theta_strip=str(wide),germs=[],complete=False)
        report['cases'].append(case);save()
        for cell in cells:
            model=SineGermTimeModel(op,rp,c.q,h.q,refined_root=package,cell=cell,nodes=args.primitive_nodes,
                order=args.time_order,outer_radius=R,radial_radius=R0,E_radius=RE,branch_sign=int(grid['trace_identity']['sign']))
            result=widened_gate(model,args.angles,args.cutoff,R,S,width,wide,args.anchor_nodes)
            case['germs'].append(result);save()
            print(json.dumps(dict(width=str(width),span=list(map(str,cell)),passed=result['passed'],
                actual_anchor=result['anchor']['continuous_boundary_and_interior_ReD_lower']['ball'],
                D_lower=result.get('D_lower',{}).get('ball'),elapsed=report['elapsed_seconds'])),flush=True)
        case['complete']=True;case['proved_full_physical_angle_and_complex_time_domain']=all(r['passed']for r in case['germs']);save()
    report['complete']=True;save();print(json.dumps(dict(complete=True,sha256=sha(args.out))),flush=True)


if __name__=='__main__':main()
