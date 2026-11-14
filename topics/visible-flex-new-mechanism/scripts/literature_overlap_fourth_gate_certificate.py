#!/usr/bin/env python3
"""Exact phase/Jacobian/leading-jet algebra; no profile or geometry evaluation."""
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path

import sympy as sp


def main() -> None:
    parser=argparse.ArgumentParser()
    parser.add_argument('--out',type=Path,required=True)
    args=parser.parse_args()
    rt=sp.sqrt(3)
    z=[sp.S(-1),sp.S(1),(-1+sp.I*rt)/2,(-1-sp.I*rt)/2]
    b=[sp.S(3),sp.Rational(1,2),sp.S(4),sp.S(4)]
    N=[4,48,3,3]
    constraints=[sum(N[j]*b[j]*z[j] for j in range(4)),
                 sum(N[j]*b[j]**2*z[j]**2 for j in range(4)),
                 sum(N[j]*b[j]**2*(z[j]+1)**2 for j in range(4))]
    constraints=[sp.simplify(v) for v in constraints]
    if constraints!=[0,0,0]:
        raise AssertionError(constraints)
    cols=[]
    for j in range(3):
        vals=[N[j]*z[j],2*N[j]*b[j]*z[j]**2,2*N[j]*b[j]*(z[j]+1)**2]
        cols.append(sp.Matrix([v for w in vals for v in (sp.re(w),sp.im(w))]))
    for j in range(3):
        vals=[sp.I*N[j]*b[j]*z[j],2*sp.I*N[j]*b[j]**2*z[j]**2,
              2*sp.I*N[j]*b[j]**2*z[j]*(z[j]+1)]
        cols.append(sp.Matrix([v for w in vals for v in (sp.re(w),sp.im(w))]))
    jac=sp.Matrix.hstack(*cols)
    determinant=sp.factor(jac.det())
    if determinant!=-716636160:
        raise AssertionError(determinant)

    x,c,y,lam,f0,f1,f2,alpha,alpha_bar=sp.symbols('x c y lam f0 f1 f2 alpha alpha_bar')
    Q=1+x*x
    density=(2*Q*f2*f2*((f0-x*f1+(x*x-1)*f2/6)**2+(f1-x*f2/3)**2)
             +Q**3*f2**4/36+4*f1*f1*(f0-x*f1/3)**2
             +sp.Rational(2,9)*(x*x+3)*f1**4)/128
    narrow=density.subs({x:c+lam*y,f0:alpha*f0,f1:alpha*f1/lam,f2:alpha*f2/lam**2},simultaneous=True)
    leading_F=sp.factor(sp.Poly(sp.expand(lam**8*narrow),lam).coeff_monomial(1))
    expected_F=(1+c*c)**3*alpha**4*f2**4/1536
    leading_F_check=sp.factor(leading_F-expected_F)
    if leading_F_check!=0:
        raise AssertionError(leading_F_check)

    f3=sp.symbols('f3')
    Qc=1+c*c
    V2=c*Qc*alpha**2*f2*f3/4
    D2=c*Qc*(alpha**2+alpha_bar**2)*f2*f3/8
    Bq=-c*Qc**2*alpha**2*f2*f3
    Bpolar=-c*Qc**2*alpha*alpha_bar*f2*f3
    E_DV=Qc*D2*V2/4
    C_D=Bq*D2/32
    B_V=Bpolar*V2/16
    leading_K2=sp.factor((E_DV+C_D)/2-B_V/4)
    expected_K2=c*c*Qc**3*alpha**2*(alpha+alpha_bar)**2*f2*f2*f3*f3/512
    leading_K2_check=sp.factor(leading_K2-expected_K2)
    if leading_K2_check!=0:
        raise AssertionError(leading_K2_check)

    payload={
        'kind':'exact_phase_and_jet_algebra_only',
        'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        'group_counts':N,'amplitude_squares':[str(v) for v in b],
        'squared_phases':[str(v) for v in z],
        'three_complex_seed_constraints':[str(v) for v in constraints],
        'jacobian_columns':['b1','b2','b3','theta1','theta2','theta3'],
        'jacobian_rows':['Re C0','Im C0','Re C4','Im C4','Re CK','Im CK'],
        'jacobian_matrix':[[str(v) for v in jac.row(i)] for i in range(6)],
        'jacobian_determinant':str(determinant),
        'F_leading_jet_identity':str(leading_F_check),
        'K2_leading_jet_identity':str(leading_K2_check),
        'all_exact_checks_passed':True,
        'profile_integrals_evaluated':False,'geometric_design_evaluated':False,
        'whole_fourth_range_certified':False,'finite_family_certified':False,
    }
    args.out.parent.mkdir(parents=True,exist_ok=True)
    args.out.write_text(json.dumps(payload,indent=2,sort_keys=True)+'\n',encoding='utf-8')
    print(json.dumps({'output':str(args.out),'bytes':args.out.stat().st_size,
                     'sha256':hashlib.sha256(args.out.read_bytes()).hexdigest(),
                     'all_exact_checks_passed':True}))


if __name__=='__main__':
    main()
