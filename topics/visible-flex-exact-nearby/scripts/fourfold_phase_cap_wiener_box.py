#!/usr/bin/env python3
"""Complete-angle cap energy boxes, with exact finite polynomial integration.

The real Wiener majorants below enclose the infinite unit tangent and its
primitive.  No angular samples or Fourier truncation occur.  A chosen constant
2x2 form is integrated against the exact saved finite trial by Parseval and
true three-point Gauss quadrature.  The entire coefficient box radius is paid
against integrated gradient Gram traces.  This is useful where the actual
nonradial perturbation is small; it is not a replacement for an unresolved
inner interval.  Every recorded interval keeps the exact scalar-germ identity.
"""
from __future__ import annotations

import argparse
from bisect import bisect_right
from fractions import Fraction
import json
import math
from pathlib import Path
import time

import numpy as np
from flint import arb,acb,acb_series,ctx

from fourfold_phase_beta_bulk_box import CBox,cstack,zeros
from fourfold_phase_beta_bulk_interval import exact_arb,real_interval
from fourfold_phase_beta_interval import ball_record
from fourfold_phase_cap_energy_interval import (
    FiniteTrial,gauss_rule,matrix_product,conjugate,hermitian_midpoint,sha)
from fourfold_phase_cap_scaled_body import ScaledBodyForm,common_cells


def sym(radius):
    return arb(0,arb(radius).upper())


def sinh(value):
    return (value.exp()-(-value).exp())/2


def cosh(value):
    return (value.exp()+(-value).exp())/2


def cosh_minus_one(value):
    return 2*sinh(value/2)**2


def real_part(value):
    if not value.imag.contains(0):
        raise ValueError('a true real scalar interval lost its real structure')
    return value.real


def upper_abs(value):
    return abs(value).upper()


def real_wiener_form(radius,height,L,Lp,C,Cp,beta,gamma):
    """Real all-angle grounded form; beta/gamma are physical radial 0..2 jets.

    The angular Wiener norm of sum b_k sin(4k theta) is at most sum |b_k|.
    For the difference tangent, horizontal primitive row norm is at most one
    and vertical zero-mean primitive norm at most one quarter.  In particular
    the radial zero mode is bounded by cosh(B)cosh(G)-1, not by a linear phase
    norm.  That quadratic mean is necessary in the true curvature estimate.
    """
    if not radius>0 or not height>0:
        raise ValueError('real radial scale or mean height is not positive')
    b=[sum((upper_abs(x) for x in row),arb(0)).upper() for row in beta]
    g=[sum((upper_abs(x) for x in row),arb(0)).upper() for row in gamma]
    B=acb_series([acb(b[j]/math.factorial(j)) for j in range(3)],prec=3)
    G=acb_series([acb(g[j]/math.factorial(j)) for j in range(3)],prec=3)
    dx=cosh(G)*sinh(B)
    dy=cosh_minus_one(G)+cosh_minus_one(B)+cosh_minus_one(G)*cosh_minus_one(B)
    dh=dx+dy
    dz=sinh(G)/4
    extract=lambda series:[(math.factorial(j)*upper_abs(series[j])).upper() for j in range(3)]
    ph,pz,p0=extract(dh),extract(dz),extract(dy)
    la,lpa=upper_abs(L),upper_abs(Lp)
    uh=la*ph[0]+ph[1]
    uz=la*pz[0]+pz[1]
    urh=lpa*ph[0]+la*ph[1]+ph[2]
    urz=lpa*pz[0]+la*pz[1]+pz[2]
    u0=la*p0[0]+p0[1]
    ur0=lpa*p0[0]+la*p0[1]+p0[2]
    # Each component is bounded separately.  Keeping the factor two for the
    # two horizontal components is conservative and avoids a vector convention.
    e0=2*la*u0+2*uh*uh+uz*uz
    e1=2*lpa*u0+2*la*ur0+2*(2*uh*urh+uz*urz)
    Ebar=L*L+radius*radius*C*C+sym(e0)
    correction=(la*e1+2*lpa*e0)/(2*radius*radius)
    numerator=C*C*(L*L-Lp)+L*C*Cp+sym(correction)
    if not Ebar>0 or not numerator>0:
        raise ValueError('the complete Wiener target curvature is not separated positive')
    K=numerator/(Ebar*Ebar)
    bt=sum((4*(j+1)*upper_abs(x) for j,x in enumerate(beta[0])),arb(0)).upper()
    gt=sum((4*(j+1)*upper_abs(x) for j,x in enumerate(gamma[0])),arb(0)).upper()
    bp,gp=sym(b[0]),sym(g[0])
    sb,cb,sg,cg=bp.sin(),bp.cos(),gp.sin(),gp.cos()
    X0=L+sym(uh);X1=sym(uh);Xz=C+sym(uz/radius)
    h1=-sb*X0+cb*X1
    v1=-cb*X0-sb*X1
    Q2=cg*Xz-sg*h1/radius
    D=(1+sym(bt))*cg*Q2-sym(gt)*v1/radius
    M=sym(b[1])*cg*Q2-sym(g[1])*v1/radius
    W=v1*v1+radius*radius*Q2*Q2
    Fh1=-sb*(1+sym(ph[0]))+cb*sym(ph[0])
    Fv1=-cb*(1+sym(ph[0]))-sb*sym(ph[0])
    Fz=height+radius*sym(pz[0])
    Fq=cg*Fz-radius*sg*Fh1
    H=Fq*v1-radius*radius*Fv1*Q2
    if not D>0 or not W>0 or not H>0 or not Fz>0:
        raise ValueError('the complete-angle scaled form has an unresolved real denominator')
    alpha=Fz*Fz*D/(H*H)
    drift=-M/D
    kappa=Fz*Fz*W*W*K/(D*H*H)
    if not alpha>0 or not kappa>0:
        raise ValueError('the actual complete-angle form is not separated positive')
    values=[alpha,alpha*drift,alpha*drift*drift+kappa,
            1/alpha+drift*drift/kappa,-drift/kappa,1/kappa]
    if any(not x.is_finite() for x in values):
        raise ValueError('nonfinite complete-angle form enclosure')
    diagnostics=dict(beta_Wiener_jet=list(map(ball_record,b)),
        gamma_Wiener_jet=list(map(ball_record,g)),
        unit_horizontal_primitive_jet=list(map(ball_record,ph)),
        unit_vertical_primitive_jet=list(map(ball_record,pz)),
        radial_zero_mode_jet=list(map(ball_record,p0)),
        normalized_energy_correction=list(map(ball_record,(e0,e1))),
        true_target_K=ball_record(K),E_over_radius_squared=ball_record(Ebar),
        radius=ball_record(radius),mean_height=ball_record(height),
        L=ball_record(L),Lprime=ball_record(Lp),C=ball_record(C),Cprime=ball_record(Cp))
    return values,diagnostics


class WienerBodyForm(ScaledBodyForm):
    def whole_angle_values(self,left,right):
        radial=acb(real_interval(left,right))
        delta=CBox.from_acb(radial-acb(self.anchor))
        jet=zeros((4,2*self.modes+2))
        for n in range(20,-1,-1):
            jet=jet*delta+cstack([self.scalar_poly[n],jet[0],2*jet[1],3*jet[2]])
        radius,height=jet[:,-2],jet[:,-1]
        L,Lp,C,Cp,_=self.scalar_ratios(radial,radius)
        scalar=lambda v:real_part(v.to_acb())
        beta=[[scalar(jet[j,k]) for k in range(self.modes)] for j in range(3)]
        gamma=[[scalar(jet[j,self.modes+k]) for k in range(self.modes)] for j in range(3)]
        return real_wiener_form(scalar(radius[0]),scalar(height[0]),
            scalar(L),scalar(Lp),scalar(C),scalar(Cp),beta,gamma)


def gram_matrices(trial,element,left,right,nodes,weights):
    center=exact_arb((left+right)/2);half=exact_arb((right-left)/2)
    result=[[zeros((trial.d,trial.d)) for _ in range(3)] for _ in range(2)]
    for node,weight in zip(nodes,weights):
        fields=trial.coefficients(element,acb(center+half*node))
        for index,(X,Y) in enumerate((fields[:2],fields[2:])):
            XX=matrix_product(conjugate(X).transpose(1,0),X)
            XY=matrix_product(conjugate(X).transpose(1,0),Y)+matrix_product(conjugate(Y).transpose(1,0),X)
            YY=matrix_product(conjugate(Y).transpose(1,0),Y)
            for j,matrix in enumerate((XX,XY,YY)):
                result[index][j]+=matrix*CBox.from_acb(acb(half*weight))
    return result


def integrate_box(values,trial,element,left,right,nodes,weights):
    # For radial P2, every displayed Gram entry has degree at most four;
    # true GL3 is exact through degree five.  For P3 use GL4 or higher.
    if 2*len(nodes)-1<2*trial.degree:
        raise ValueError('the selected true Gauss rule does not exactly integrate the finite Gram polynomial')
    grams=gram_matrices(trial,element,left,right,nodes,weights)
    answer=[]
    for index in range(2):
        matrices=grams[index]
        chosen=[float(v.mid()) for v in values[3*index:3*index+3]]
        fees=[abs(v-arb(c)).upper() for v,c in zip(values[3*index:3*index+3],chosen)]
        enclosed=sum((c*m for c,m in zip(chosen,matrices)),zeros((trial.d,trial.d)))
        middle,rounding=hermitian_midpoint(enclosed)
        trace=[]
        for matrix in (matrices[0],matrices[2]):
            bound=sum((arb(float(matrix.real.hi[j,j])) for j in range(trial.d)),arb(0)).upper()
            if not bound>=0:
                raise ValueError('a finite Gram trace is not nonnegative')
            trace.append(bound)
        variation=fees[0]*trace[0]+2*fees[1]*(trace[0]*trace[1]).sqrt()+fees[2]*trace[1]
        answer.append(dict(
            matrix_middle=[[[float(z.real),float(z.imag)] for z in row] for row in middle],
            full_operator_error=ball_record((rounding+variation).upper()),
            complete_form_box_variation=ball_record(variation.upper()),
            finite_Gram_directed_rounding=ball_record(rounding),
            chosen_constant_form=chosen,full_coefficient_radii=list(map(ball_record,fees)),
            complete_Fourier_Gram_trace=list(map(ball_record,trace))))
    return answer


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--trial',type=Path,default=Path('notes/2026-11-12-cap-space-boundary4-interior16-P2.json'))
    parser.add_argument('--element',type=int,default=40)
    parser.add_argument('--span',type=int,default=0)
    parser.add_argument('--bits',type=int,default=160)
    parser.add_argument('--max-depth',type=int,default=0)
    parser.add_argument('--error-per-length',type=Fraction,default=Fraction(1,10000))
    parser.add_argument('--out',type=Path,required=True)
    args=parser.parse_args();ctx.prec,ctx.cap=args.bits,4
    wall,cpu=time.monotonic(),time.process_time()
    trial=FiniteTrial(args.trial)
    # These small unused angle grids only initialize the shared exact scalar
    # object.  No angle grid or primitive FFT enters this certificate.
    target=WienerBodyForm(trial.object_path,128,128,arb('.003'),arb('.0025'),arb('.32'))
    common=common_cells(target)
    l,r=map(lambda x:Fraction(float(x)),trial.mesh[args.element:args.element+2])
    if not Fraction(1,4)<=l<r<=3:
        raise ValueError('select a body element; graft is a distinct analytic object')
    points=sorted({l,r}|{q for q in common if l<q<r})
    left,right=points[args.span:args.span+2]
    k=bisect_right(common,(left+right)/2)-1
    target.set_cell(common[k],common[k+1])
    nodes,weights=gauss_rule(trial.degree+1)
    rows,failures,subdivisions=[],[],[]
    report=dict(kind='complete_infinite_Wiener_body_trial_energy',complete=False,
        source_sha256=sha(__file__),object_sha256=trial.report['object_sha256'],
        exact_delta_fraction=trial.report['exact_delta_fraction'],
        trial_report_path=str(args.trial),trial_report_sha256=sha(args.trial),bits=args.bits,
        requested_exact_radial_interval=[str(left),str(right)],
        actual_common_span=list(map(str,target.cell)),finite_element=args.element,
        angular_sampling_used=False,radial_Gram_quadrature_degree=len(nodes),
        gauss_nodes=list(map(ball_record,nodes)),gauss_weights=list(map(ball_record,weights)),
        error_density_target=str(args.error_per_length),full_positive_cap_complete=False,
        intervals=rows,unresolved_intervals=failures,rejected_parent_boxes=subdivisions,
        dependency_sha256={name:sha(Path(__file__).with_name(name)) for name in (
            'fourfold_phase_cap_scaled_body.py','fourfold_phase_cap_energy_interval.py',
            'fourfold_phase_beta_affine.py','fourfold_phase_beta_bulk_box.py')},
        scope='Only the listed actual body interval. The entire infinite angular primitive is enclosed analytically; finite trial Gram integration is exact up to paid directed rounding. No whole cap or inverse claim.')
    def save():
        report['CPU_seconds']=time.process_time()-cpu
        report['wall_seconds']=time.monotonic()-wall
        args.out.parent.mkdir(parents=True,exist_ok=True)
        tmp=args.out.with_suffix(args.out.suffix+'.tmp')
        tmp.write_text(json.dumps(report,indent=2)+'\n');tmp.replace(args.out)
    pending=[(left,right,0)]
    while pending:
        a,b,depth=pending.pop()
        try:
            values,diagnostics=target.whole_angle_values(a,b)
            energies=integrate_box(values,trial,args.element,a,b,nodes,weights)
            error=max(arb(x['full_operator_error']['ball']).upper() for x in energies)
            density=error/exact_arb(b-a)
            if not density<=exact_arb(args.error_per_length):
                raise ValueError('full energy error per radial length exceeds the requested budget: '+density.str(16))
            row=dict(exact_radial_interval=[str(a),str(b)],subdivision_depth=depth,
                true_form_and_inverse_boxes=list(map(ball_record,values)),
                infinite_Wiener_diagnostics=diagnostics,primal_energy=energies[0],dual_energy=energies[1])
            rows.append(row)
            print(json.dumps(dict(accepted=row['exact_radial_interval'],
                error_density=density.str(15),depth=depth)),flush=True)
        except (ValueError,ZeroDivisionError) as exc:
            item=dict(exact_radial_interval=[str(a),str(b)],depth=depth,reason=str(exc))
            if depth==args.max_depth:failures.append(item)
            else:
                subdivisions.append(item);mid=(a+b)/2
                pending.extend([(mid,b,depth+1),(a,mid,depth+1)])
        report['pending']=[[str(a),str(b),d] for a,b,d in pending];save()
    rows.sort(key=lambda row:Fraction(row['exact_radial_interval'][0]))
    cursor=left
    for row in rows:
        a,b=map(Fraction,row['exact_radial_interval'])
        if a!=cursor:break
        cursor=b
    report['complete']=not failures and cursor==right
    save()
    print(json.dumps(dict(complete=report['complete'],failures=failures,
        CPU_seconds=report['CPU_seconds'],wall_seconds=report['wall_seconds'])),flush=True)
    if not report['complete']:raise SystemExit('the complete-angle energy box did not pay the requested interval')


if __name__=='__main__':main()
