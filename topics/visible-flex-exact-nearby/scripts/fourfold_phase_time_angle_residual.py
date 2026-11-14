#!/usr/bin/env python3
"""A strict residual on a continuous initial-angle arc and real time subspan.

Retains both time and angle correlations.  The arc is x=z0+hx*v, |v|<=1
real, usually on a complex-strip boundary.  All time-angle Taylor
coefficients are directed, and a larger bidisk pays both infinite tails.
One arc is not a whole-circle or whole-leg certificate.
"""
from __future__ import annotations
import argparse
from fractions import Fraction
import json
import math
from pathlib import Path
import time
from flint import arb, acb, acb_series, ctx

from fourfold_time_angle_jets import TimeAngleJet as Jet
from fourfold_phase_beta_interval import series_constant, ball_record
from fourfold_phase_beta_bulk_interval import exact_arb
from fourfold_phase_beta_affine import sha
from fourfold_phase_field_time_taylor import FieldTimeModel, pad_series, polynomial, record_complex
from fourfold_phase_reference_time_sample import load_segment


def bernstein_matrix(left, right):
    center, half=(left+right)/2,(right-left)/2
    rows=[]
    for j in range(8):
        row=[]
        for i in range(8):
            value=sum((Fraction(math.comb(7,j)*math.comb(7-j,r-j)*(-1)**(r-j)*math.comb(r,i))
                       *center**(r-i)*half**i for r in range(max(i,j),8)),Fraction(0))
            row.append(exact_arb(value))
        rows.append(row)
    return rows


def fourier_time_coefficients(real, imag, left, right):
    matrix=bernstein_matrix(left,right)
    K=real.shape[-1]-1
    data=[[[acb(0) for k in range(K+1)] for i in range(8)] for field in range(2)]
    for field in range(2):
        for i in range(8):
            for k in range(K+1):
                data[field][i][k]=sum((acb(arb(float(real[j,field,k])),arb(float(imag[j,field,k])))*matrix[j][i]
                                      for j in range(8)),acb(0))
    return data


def reference_jets(data, label, hx, m, n, time_halfwidth):
    K=len(data[0][0])-1
    rows=[[[acb(0) for i in range(m)] for j in range(n)] for f in range(2)]
    for k in range(K+1):
        signs=(1,) if k==0 else (1,-1)
        for sign in signs:
            frequency=sign*k
            phase=(acb(0,frequency)*label).exp()
            factor=acb(1)
            for j in range(n):
                if j:factor*=acb(0,frequency)*hx/j
                for field in range(2):
                    for i in range(8):
                        coefficient=data[field][i][k]
                        if sign<0:coefficient=coefficient.conjugate()
                        rows[field][j][i]+=coefficient*phase*factor
    rows[0][0][0]+=label/4
    if n>1:rows[0][1][0]+=hx/4
    derivatives=[]
    for field in range(2):
        derivatives.append(Jet([[(i+1)*rows[field][j][i+1]/time_halfwidth if i<7 else acb(0)
                                 for i in range(m)] for j in range(n)],time_precision=m,angle_precision=n))
    return [Jet(row,time_precision=m,angle_precision=n) for row in rows],derivatives


def finite_reference_bounds(data, label, hx, Rt, Rx, h):
    """Full finite Fourier bounds, before any angular Taylor truncation."""
    K=len(data[0][0])-1
    angle=abs(hx)*Rx; center_imag=abs(label.imag)
    angular_change=angle/4
    derivative_bounds=[];value_bounds=[]
    for field in range(2):
        derivative=arb(0);value=arb(0)
        for k in range(K+1):
            weight=arb(1) if k==0 else 2*(k*(center_imag+angle)).exp()
            size=sum((abs(data[field][i][k]) for i in range(8)),arb(0))
            derivative+=weight*sum((i*abs(data[field][i][k])/abs(h) for i in range(1,8)),arb(0))
            value+=weight*size
            if field==0 and k:
                time_size=sum((abs(data[0][i][k])*Rt**i for i in range(8)),arb(0))
                angular_change+=2*time_size*(k*center_imag).cosh()*((k*angle).exp()-1)
        derivative_bounds.append(derivative.upper());value_bounds.append(value.upper())
    return dict(theta_angular_variation_on_outer_bidisk=angular_change.upper(),
                derivative_on_real_time_outer_angle=derivative_bounds,
                value_on_real_time_outer_angle=value_bounds)


def lift(model, value, n):
    return Jet.from_time_series(value,time_precision=model.precision,angle_precision=n)


def phases_on_jet(model, theta):
    """Reuse exp(+-4iY), rather than forming every mode independently."""
    m,n=theta.m,theta.n
    zero=Jet.constant(0,time_precision=m,angle_precision=n)
    out={key:zero for key in ['B','G','Br','Gr','B1','G1','B2','G2','Br1','Gr1']}
    plus,minus=(theta*acb(0,4)).exp(),(theta*acb(0,-4)).exp()
    ep=em=Jet.constant(1,time_precision=m,angle_precision=n)
    for k,(b,g,br,gr) in enumerate(zip(model.beta,model.gamma,model.beta_r,model.gamma_r),1):
        ep,em=ep*plus,em*minus
        sine,cosine=(ep-em)/acb(0,2),(ep+em)/2
        for key,value in [('B',b),('G',g),('Br',br),('Gr',gr)]:
            term=lift(model,value,n)
            out[key]=out[key]+term*sine
            out[key+'1']=out[key+'1']+term*cosine*(4*k)
            if key in ['B','G']:out[key+'2']=out[key+'2']-term*sine*(4*k)**2
    return out


def initial_X(model, theta0):
    """True v=0 initial jets, with the existing infinite primitive fee."""
    values,_,_,error=model.image_and_X_error(theta0)
    theta=polynomial(values,model.precision)
    X=[series_constant(0,model.precision) for _ in range(3)]
    for k,frequency in enumerate(model.target.frequency):
        phase=(acb(0,frequency)*theta).exp()
        for component in range(3):X[component]+=model.X_coefficient[k,component]*phase
    real=all(v.imag==0 for v in values)
    return [pad_series(value,error,model.outer,real=real) for value in X],error


def angular_X(model, theta, phases):
    """Use the exact rotating-frame angular ODE, not a truncated derivative.

    X_theta=a_r*T+a*T_r-Jrot*X, Jrot(X)=(-X1,X0,0).
    Along the initial-label arc multiply by Y_v, then solve coefficient by
    coefficient in v. Only v=0 requires the infinite Fourier primitive.
    """
    m,n=theta.m,theta.n
    sb,cb=phases['B'].sin_cos();sg,cg=phases['G'].sin_cos()
    T=[-sb*cg,cb*cg,sg]
    Tr=[-cb*cg*phases['Br']+sb*sg*phases['Gr'],
        -sb*cg*phases['Br']-cb*sg*phases['Gr'],cg*phases['Gr']]
    a,ar=lift(model,model.a,n),lift(model,model.ar,n)
    S=[ar*T[k]+a*Tr[k] for k in range(3)]
    first,error=initial_X(model,[theta.coefficient(i,0) for i in range(8)])
    old=ctx.cap;ctx.cap=m
    try:
        Yv=[acb_series([(j+1)*theta.coefficient(i,j+1) for i in range(m)],prec=m) for j in range(n-1)]
        sources=[[acb_series([S[k].coefficient(i,j) for i in range(m)],prec=m)
                  for j in range(n-1)] for k in range(3)]
        X=[[first[k]] for k in range(3)];zero=acb_series([],prec=m)
        for j in range(1,n):
            common=[sum((sources[k][l]*Yv[j-1-l] for l in range(j)),zero) for k in range(3)]
            rotation0=sum((X[1][l]*Yv[j-1-l] for l in range(j)),zero)
            rotation1=sum((X[0][l]*Yv[j-1-l] for l in range(j)),zero)
            X[0].append((common[0]+rotation0)/j)
            X[1].append((common[1]-rotation1)/j)
            X[2].append(common[2]/j)
        jets=[Jet([[X[k][j][i] for i in range(m)] for j in range(n)],time_precision=m,angle_precision=n)
              for k in range(3)]
        return jets,(sb,cb,sg,cg),error
    finally:ctx.cap=old


def first_field(model, X, phase, trigonometry):
    m,n=X[0].m,X[0].n
    sb,cb,s,c=trigonometry
    a,ar=lift(model,model.a,n),lift(model,model.ar,n)
    h=-sb*X[0]+cb*X[1];v=-cb*X[0]-sb*X[1]
    Q,R=c*X[2]-s*h,c*h+s*X[2]
    P,u,p,q=1+phase['B1'],phase['G1'],phase['Br'],phase['Gr']
    Q1=a*q-P*s*v-u*R;v1=a*c*p-P*h
    D=P*c*Q-u*v;M=p*c*Q-q*v;W=Q*Q+v*v
    D1=phase['B2']*c*Q-P*s*u*Q+P*c*Q1-phase['G2']*v-u*v1
    M1=phase['Br1']*c*Q-p*s*u*Q+p*c*Q1-phase['Gr1']*v-q*v1
    W1=2*(Q*Q1+v*v1)
    kappa=lift(model,(-model.K).sqrt(),n)
    A=-M-model.sign*kappa*W;A1=-M1-model.sign*kappa*W1
    inverse=D.inverse();r_tau=lift(model,model.r_tau,n)
    f=r_tau*A*inverse
    ft=r_tau*(A1*inverse-A*D1*inverse**2)
    return f,ft


def coefficient_tail(M,Rt,Rx,m,n):
    # Union bound on omitted rows/columns of the absolutely convergent
    # double Cauchy series. The doubly omitted corner is safely overcounted.
    return M*(Rt**(-m)+Rx**(-n))/((1-1/Rt)*(1-1/Rx))


def main():
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--manifest',type=Path,required=True)
    ap.add_argument('--object',type=Path,required=True)
    ap.add_argument('--root-certificate',type=Path,required=True)
    ap.add_argument('--segment',type=int,required=True)
    ap.add_argument('--sub-left',default='31/64');ap.add_argument('--sub-right',default='33/64')
    ap.add_argument('--label-real',default='1/2');ap.add_argument('--label-imag',default='1/512')
    ap.add_argument('--angle-halfwidth',default='1/4096');ap.add_argument('--angle-outer-radius',default='4')
    ap.add_argument('--angle-order',type=int,default=23);ap.add_argument('--time-order',type=int,default=16)
    ap.add_argument('--time-outer-radius',default='8');ap.add_argument('--quarter-nodes',type=int,default=512)
    ap.add_argument('--state-tube',default='1/65536');ap.add_argument('--bits',type=int,default=160)
    ap.add_argument('--out',type=Path,required=True)
    args=ap.parse_args();start=time.monotonic();ctx.prec=args.bits
    if args.time_order<7 or args.angle_order<2:raise ValueError('insufficient retained reference degree')
    m,n=args.time_order+1,args.angle_order+1
    manifest,shard,shard_path,real,imag,a,b=load_segment(args.manifest,args.segment)
    ident=manifest['trace_identity']
    if ident['angular_scale']!=4 or ident['sign'] not in [-1,1]:raise ValueError('wrong physical-state convention')
    if sha(args.object)!=ident['source_sha256'] or sha(args.root_certificate)!=ident['root_certificate_sha256']:
        raise ValueError('reference/geometry/root identity mismatch')
    left,right=Fraction(args.sub_left),Fraction(args.sub_right)
    if not 0<=left<right<=1:raise ValueError('invalid time subspan')
    ta,tb=a+(b-a)*left,a+(b-a)*right
    tau0,h=(ta+tb)/2,(tb-ta)/2
    hx,Rx=exact_arb(Fraction(args.angle_halfwidth)),exact_arb(Fraction(args.angle_outer_radius))
    if not hx>0 or not Rx>1:raise ValueError('positive angular scale and outer radius greater than one required')
    label=acb(exact_arb(Fraction(args.label_real)),exact_arb(Fraction(args.label_imag)))
    model=FieldTimeModel(args.object,args.root_certificate,tau0,h,nodes=args.quarter_nodes,
                         order=args.time_order,outer_radius=Fraction(args.time_outer_radius),branch_sign=int(ident['sign']))
    print(json.dumps(dict(stage='true time germ',elapsed=time.monotonic()-start)),flush=True)
    data=fourier_time_coefficients(real,imag,left,right)
    (Y,L),(Ytau,Ltau)=reference_jets(data,label,hx,m,n,model.h)
    finite=finite_reference_bounds(data,label,hx,model.outer,Rx,model.h)
    theta0=[Y.coefficient(i,0) for i in range(8)]
    tube=exact_arb(Fraction(args.state_tube))
    full_tube=(finite['theta_angular_variation_on_outer_bidisk']+tube).upper()
    mantissa,exponent=full_tube.man_exp()
    full_tube_exact=Fraction(int(mantissa))*Fraction(2)**int(exponent)
    domain=model.outer_domain(theta0,full_tube_exact)
    print(json.dumps(dict(stage='entire outer bidisk domain',elapsed=time.monotonic()-start)),flush=True)
    phases=phases_on_jet(model,Y)
    X,trig,Xfee=angular_X(model,Y,phases)
    f,ft=first_field(model,X,phases,trig)
    e0,e1=Ytau-f,Ltau-ft
    Rt=model.outer;angle_tail_factor=Rx**(-n)/(1-1/Rx)
    tails=[coefficient_tail(domain[key],Rt,Rx,m,n)+finite['derivative_on_real_time_outer_angle'][j]*angle_tail_factor
           for j,key in enumerate(['f','f_theta'])]
    errors=[(value.bound()+tail).upper() for value,tail in zip([e0,e1],tails)]
    Ltail=finite['value_on_real_time_outer_angle'][1]*angle_tail_factor
    Lvariation=sum((abs(L.coefficient(i,j)) for j in range(n) for i in range(m) if i+j>0),arb(0))+Ltail
    qmin=(L.coefficient(0,0).real-Lvariation).exp().lower()
    qmax=(L.coefficient(0,0).real+Lvariation).exp().upper()
    if not qmin>0:raise ValueError('reference q lower bound unresolved')
    length=2*abs(model.h);A=length*errors[0]/qmin;B=length*errors[1];C=length*domain['f_theta2']*qmax/2
    denominator=1-B.exp()*C*A
    R=B.exp()*A/denominator
    accepted=bool(denominator>0 and qmax*R<tube)
    # Independent chain-rule check in the first angular coefficient:
    # d_v f(t,Y)=f_theta(t,Y) d_vY, at v=0.
    chain=True
    for i in range(m):
        expected=sum((ft.coefficient(k,0)*Y.coefficient(i-k,1) for k in range(i+1)),acb(0))
        difference=f.coefficient(i,1)-expected
        chain=chain and difference.real.contains(0) and difference.imag.contains(0)
    if not chain:raise ValueError('independent first-angle chain-rule check failed')
    report=dict(kind='directed_time_and_initial_angle_arc_residual',complete=True,source_sha256=sha(__file__),
        dependency_sha256={name:sha(Path(__file__).with_name(name)) for name in
            ['fourfold_time_angle_jets.py','fourfold_phase_field_time_taylor.py','fourfold_phase_reference_time_sample.py',
             'fourfold_phase_beta_interval.py','fourfold_phase_beta_bulk_interval.py','fourfold_phase_beta_affine.py']},
        reference_manifest_sha256=sha(args.manifest),reference_manifest=str(args.manifest),reference_shard_sha256=sha(shard_path),
        object_sha256=sha(args.object),root_certificate_sha256=sha(args.root_certificate),exact_delta_fraction=str(model.target.affine_delta),
        segment=args.segment,exact_time_endpoints=[str(ta),str(tb)],normalized_time_subspan=[str(left),str(right)],
        initial_label_center=dict(real=args.label_real,imag=args.label_imag),angle_halfwidth=args.angle_halfwidth,
        real_arc_definition='x=label_center+angle_halfwidth*v, real -1<=v<=1',
        retained_time_order=args.time_order,retained_angle_order=args.angle_order,
        time_outer_radius=args.time_outer_radius,angle_outer_radius=args.angle_outer_radius,
        bits=args.bits,quarter_nodes=args.quarter_nodes,branch_sign=int(ident['sign']),
        radial_common_span=list(map(str,model.cell)),first_angle_chain_rule_checked=chain,
        outer_domain={key:ball_record(value) for key,value in domain.items()},
        reference_outer_angle_variation=ball_record(finite['theta_angular_variation_on_outer_bidisk']),
        initial_X_infinite_primitive_time_error=ball_record(Xfee),
        e0_bound=ball_record(errors[0]),e1_bound=ball_record(errors[1]),
        e0_double_and_reference_tail=ball_record(tails[0]),e1_double_and_reference_tail=ball_record(tails[1]),
        e0_center=record_complex(e0.coefficient(0,0)),e1_center=record_complex(e1.coefficient(0,0)),
        matching_initial_R60={key:ball_record(value) for key,value in
                             dict(qmin=qmin,qmax=qmax,A=A,B=B,C=C,denominator=denominator,R=R,actual_error_upper=qmax*R).items()},
        hypothetical_matching_initial_flow_proved=accepted,elapsed_seconds=time.monotonic()-start,
        limitations=['Only the stated continuous real-v initial-angle arc and time subspan are certified.',
            'No complete boundary-circle coverage, maximum-principle global strip bound or complete leg is claimed.',
            'The R60 initial error is zero by a separate local matching assumption, not by the global trajectory history.',
            'No turning collar or parameter variation is paid by this prototype.'])
    args.out.parent.mkdir(parents=True,exist_ok=True);args.out.write_text(json.dumps(report,indent=2)+'\n')
    print(json.dumps({key:report[key] for key in ['complete','e0_bound','e1_bound','e0_double_and_reference_tail',
                     'e1_double_and_reference_tail','hypothetical_matching_initial_flow_proved','elapsed_seconds']},indent=2),flush=True)


if __name__=='__main__':main()
