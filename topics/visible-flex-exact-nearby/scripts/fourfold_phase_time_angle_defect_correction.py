#!/usr/bin/env python3
"""Exact finite time-angle corrections and fresh continuous-arc validation.

Y is the original finite Fourier/Bernstein function plus a finite polynomial
P(u,v), not a truncated angle series substituted for that original function.
Each dyadic correction vanishes identically at u=-1 for every v. All tails,
the complete outer image and the true residual are reverified afterward.
"""
from __future__ import annotations
import argparse
from fractions import Fraction
import gzip
import hashlib
import json
from pathlib import Path
import time
from flint import arb,acb,acb_series,ctx
from fourfold_time_angle_jets import TimeAngleJet as Jet
from fourfold_phase_time_angle_residual import (
    fourier_time_coefficients,reference_jets,finite_reference_bounds,phases_on_jet,
    initial_X,lift,first_field,coefficient_tail,
)
from fourfold_phase_field_time_refined_root import RefinedGermTimeModel
from fourfold_phase_reference_time_sample import load_segment
from fourfold_phase_field_time_taylor import record_complex
from fourfold_phase_beta_bulk_interval import exact_arb
from fourfold_phase_beta_interval import ball_record
from fourfold_phase_time_defect_correction import midpoint_fraction


def sha(path):return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def angular_X_full_time(model,theta,phases):
    """Same exact X_theta identity, retaining every corrected time coefficient."""
    m,n=theta.m,theta.n
    sb,cb=phases['B'].sin_cos();sg,cg=phases['G'].sin_cos()
    T=[-sb*cg,cb*cg,sg]
    Tr=[-cb*cg*phases['Br']+sb*sg*phases['Gr'],
        -sb*cg*phases['Br']-cb*sg*phases['Gr'],cg*phases['Gr']]
    a,ar=lift(model,model.a,n),lift(model,model.ar,n)
    S=[ar*T[k]+a*Tr[k] for k in range(3)]
    first,error=initial_X(model,[theta.coefficient(i,0) for i in range(m)])
    old=ctx.cap;ctx.cap=m
    try:
        Yv=[acb_series([(j+1)*theta.coefficient(i,j+1) for i in range(m)],prec=m) for j in range(n-1)]
        sources=[[acb_series([S[k].coefficient(i,j) for i in range(m)],prec=m) for j in range(n-1)] for k in range(3)]
        X=[[first[k]] for k in range(3)];zero=acb_series([],prec=m)
        for j in range(1,n):
            common=[sum((sources[k][l]*Yv[j-1-l] for l in range(j)),zero) for k in range(3)]
            rotation0=sum((X[1][l]*Yv[j-1-l] for l in range(j)),zero)
            rotation1=sum((X[0][l]*Yv[j-1-l] for l in range(j)),zero)
            X[0].append((common[0]+rotation0)/j)
            X[1].append((common[1]-rotation1)/j)
            X[2].append(common[2]/j)
        jets=[Jet([[X[k][j][i] for i in range(m)] for j in range(n)],time_precision=m,angle_precision=n) for k in range(3)]
        return jets,(sb,cb,sg,cg),error
    finally:ctx.cap=old


def time_derivative(P,h):
    return Jet([[(i+1)*P.coefficient(i+1,j)/h if i+1<P.m else acb(0)
                 for i in range(P.m)] for j in range(P.n)],time_precision=P.m,angle_precision=P.n)


def exact_upper(value):
    a,b=value.upper().man_exp()
    return Fraction(int(a))*Fraction(2)**int(b)


def validate(model,Ybase,L,Ytau,Ltau,P,finite,Rx,tube):
    Y=Ybase+P;m,n=Y.m,Y.n
    variation=sum((abs(P.coefficient(i,j))*model.outer**i*Rx**j
                   for j in range(1,n) for i in range(m)),arb(0))
    full_tube=finite['theta_angular_variation_on_outer_bidisk']+variation+exact_arb(tube)
    domain=model.outer_domain([Y.coefficient(i,0) for i in range(m)],exact_upper(full_tube))
    phases=phases_on_jet(model,Y);X,trig,Xfee=angular_X_full_time(model,Y,phases)
    f,ft=first_field(model,X,phases,trig)
    e0=Ytau+time_derivative(P,model.h)-f;e1=Ltau-ft
    tailfactor=Rx**(-n)/(1-1/Rx)
    tails=[coefficient_tail(domain[key],model.outer,Rx,m,n)+finite['derivative_on_real_time_outer_angle'][j]*tailfactor
           for j,key in enumerate(['f','f_theta'])]
    errors=[(v.bound()+tail).upper() for v,tail in zip([e0,e1],tails)]
    Ltail=finite['value_on_real_time_outer_angle'][1]*tailfactor
    Lvariation=sum((abs(L.coefficient(i,j)) for j in range(n) for i in range(m) if i+j>0),arb(0))+Ltail
    qmin=(L.coefficient(0,0).real-Lvariation).exp().lower();qmax=(L.coefficient(0,0).real+Lvariation).exp().upper()
    length=2*abs(model.h);A=length*errors[0]/qmin;B=length*errors[1];C=length*domain['f_theta2']*qmax/2
    denominator=1-B.exp()*C*A;R=B.exp()*A/denominator
    if not qmin>0 or not denominator>0 or not qmax*R<exact_arb(tube):raise ValueError('actual continuous-arc local tube failed')
    for i in range(m):
        check=f.coefficient(i,1)-sum((ft.coefficient(k,0)*Y.coefficient(i-k,1) for k in range(i+1)),acb(0))
        if not check.real.contains(0) or not check.imag.contains(0):raise ValueError('first-angle chain rule failed')
    report=dict(e0_bound=ball_record(errors[0]),e1_bound=ball_record(errors[1]),
        e0_tail=ball_record(tails[0]),e1_tail=ball_record(tails[1]),
        correction_bound_on_real_bidisk=ball_record(P.bound()),
        correction_outer_angular_variation=ball_record(variation),
        true_X_infinite_time_fee=ball_record(Xfee),
        analytic_outer_domain={k:ball_record(v) for k,v in domain.items()},
        local_R60={k:ball_record(v) for k,v in dict(qmin=qmin,qmax=qmax,A=A,B=B,C=C,denominator=denominator,R=R,physical_error=qmax*R).items()},
        hypothetical_matching_left_flow_proved=True,first_angle_chain_rule_checked=True)
    return e0,report


def choose(model,e0,L):
    m,n=e0.m,e0.n;q=L.exp();density=e0*(-L).exp();rows=[]
    for j in range(n):
        row=[acb(0)]+[-model.h*density.coefficient(i-1,j)/i for i in range(1,m)]
        row[0]=-sum((row[i]*(-1)**i for i in range(1,m)),acb(0));rows.append(row)
    candidate=q*Jet(rows,time_precision=m,angle_precision=n)
    chosen=[]
    for j in range(n):
        row=[(Fraction(0),Fraction(0))]+[(midpoint_fraction(candidate.coefficient(i,j).real),
                                         midpoint_fraction(candidate.coefficient(i,j).imag)) for i in range(1,m)]
        row[0]=tuple(-sum((row[i][c]*(-1)**i for i in range(1,m)),Fraction(0)) for c in range(2))
        if any(sum((row[i][c]*(-1)**i for i in range(m)),Fraction(0)) for c in range(2)):
            raise ValueError('correction does not vanish identically on left time edge')
        chosen.append(row)
    value=Jet([[acb(exact_arb(a),exact_arb(b)) for a,b in row] for row in chosen],time_precision=m,angle_precision=n)
    return value,[[[str(a),str(b)] for a,b in row] for row in chosen]


def main():
    p=argparse.ArgumentParser(description=__doc__);p.add_argument('--time-order',type=int,default=32)
    p.add_argument('--angle-order',type=int,default=31);p.add_argument('--iterations',type=int,default=2)
    p.add_argument('--angle-halfwidth',default='1/4096');p.add_argument('--bits',type=int,default=192)
    p.add_argument('--out',type=Path,required=True);args=p.parse_args();ctx.prec=args.bits
    if args.time_order<8 or args.angle_order<2 or args.iterations<1:raise ValueError('invalid degree/iteration')
    base=Path('data/phase_ring_continuation');mp=base/'r61_step3_shared_forward/manifest.json'
    op=base/'type_fixed_step02_d5_exact_affine_step3_object.json';rp=base/'type_fixed_step02_d5_exact_affine_step3_root_tight.json'
    dependencies=['fourfold_time_angle_jets.py','fourfold_phase_time_angle_residual.py',
        'fourfold_phase_field_time_refined_root.py','fourfold_phase_field_time_taylor.py',
        'fourfold_phase_reference_time_sample.py','fourfold_phase_time_defect_correction.py']
    paths=[Path(__file__),mp,op,rp]+[Path(__file__).with_name(name) for name in dependencies]
    hashes={str(path):sha(path) for path in paths};start=time.monotonic()
    manifest,shard,shard_path,real,imag,a,b=load_segment(mp,419)
    left,right=Fraction(31,64),Fraction(33,64);ta,tb=a+(b-a)*left,a+(b-a)*right
    model=RefinedGermTimeModel(op,rp,(ta+tb)/2,(tb-ta)/2,nodes=512,order=args.time_order,outer_radius=8,
                             branch_sign=manifest['trace_identity']['sign'])
    data=fourier_time_coefficients(real,imag,left,right);m,n=args.time_order+1,args.angle_order+1
    label=acb(exact_arb(Fraction(1,2)),exact_arb(Fraction(1,512)));hx=exact_arb(Fraction(args.angle_halfwidth));Rx=arb(4)
    (Y,L),(Ytau,Ltau)=reference_jets(data,label,hx,m,n,model.h)
    finite=finite_reference_bounds(data,label,hx,model.outer,Rx,model.h)
    P=Jet.constant(0,time_precision=m,angle_precision=n);steps=[];corrections=[]
    for iteration in range(args.iterations+1):
        e0,report=validate(model,Y,L,Ytau,Ltau,P,finite,Rx,Fraction(1,65536))
        report['iteration']=iteration;steps.append(report)
        print(json.dumps(dict(iteration=iteration,e0=report['e0_bound']['ball'],e1=report['e1_bound']['ball'],
                              elapsed_seconds=time.monotonic()-start)),flush=True)
        if iteration<args.iterations:
            delta,definition=choose(model,e0,L);P=P+delta;corrections.append(definition)
    report=dict(kind='true_continuous_time_angle_arc_with_exact_finite_defect_corrections',complete=True,
        provenance=hashes,reference_shard_sha256=sha(shard_path),root_refinement=model.root_package.provenance,
        exact_delta_fraction=str(model.target.affine_delta),segment=419,subspan=['31/64','33/64'],
        exact_time_endpoints=list(map(str,[ta,tb])),label_center={'real':'1/2','imag':'1/512'},
        angle_halfwidth=args.angle_halfwidth,time_outer_radius='8',angle_outer_radius='4',
        time_order=args.time_order,angle_order=args.angle_order,bits=args.bits,
        reference_definition='Exact original R61 finite Fourier/Bernstein function plus the saved finite polynomials',
        correction_axes='outer rows: v degree; inner rows: u degree; pair: exact real and imaginary fractions',
        corrections=corrections,all_corrections_identically_zero_on_left_time_edge=True,
        steps=steps,elapsed_seconds=time.monotonic()-start,
        limitations=['Only the stated continuous real-v arc and real-u time window are certified.',
                     'All local comparisons assume matching left initial family, not full-branch accumulated error.',
                     'No full initial circle, full return, parameter-flow or KAM acceptance is asserted.'])
    raw=(json.dumps(report,indent=2)+'\n').encode()
    if len(raw)>1_000_000 and args.out.suffix!='.gz':raise ValueError('large report requires gzip')
    output=gzip.compress(raw,mtime=0) if args.out.suffix=='.gz' else raw
    if len(output)>5_000_000:raise ValueError('report must be split below 5MB')
    args.out.write_bytes(output)


if __name__=='__main__':main()
