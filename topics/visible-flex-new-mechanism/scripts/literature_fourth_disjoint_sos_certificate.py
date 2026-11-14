#!/usr/bin/env python3
"""Exact algebra for the disjoint-profile fourth-order positive obstruction.

No geometry, numerical quadrature, optimization, or ODE is evaluated.
"""
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path

import sympy as sp


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument('--out', type=Path, required=True)
    args = parser.parse_args()
    x, f, p, q, r = sp.symbols('x f p q r', real=True)
    Q = 1+x*x
    a = x*q-p
    F = Q*q-2*f
    local_P = F*F/2-Q*a*a
    local_L = x*Q*q*q-2*Q*p*q

    def dx(expr):
        return (sp.diff(expr,x)+sp.diff(expr,f)*p+
                sp.diff(expr,p)*q+sp.diff(expr,q)*r)

    pre = sp.expand(local_L**2+2*local_P*a*(a+Q*r)
                    +2*Q**2*p**2*q**2+4*Q*p**4)
    flux1 = sp.integrate(pre.coeff(r,1),q)
    P = (Q**3*q**4/12 + sp.Rational(2,3)*Q*((x*x-1)*f-Q*x*p)*q**3
         +2*Q*(f*f-2*x*f*p+Q*p*p)*q*q
         +4*Q*f*p*p*q+4*f*f*p*p+2*Q*p**4)
    sos = (2*Q*q*q*((f-x*p+(x*x-1)*q/6)**2+(p-x*q/3)**2)
           +Q**3*q**4/36+4*p*p*(f-x*p/3)**2
           +sp.Rational(2,9)*(x*x+3)*p**4)
    flux2 = sp.Rational(4,3)*Q*f*p**3

    U,V,Vp,J = sp.symbols('U V Vp J', real=True)
    Jp = -Q*U-2*V
    L = x*Q*U-Q*Vp
    tail_flux_derivative = (J*J+2*x*J*Jp+2*Jp*Q*V
                            +2*J*(2*x*V+Q*Vp))
    mu,z,E,Tf,Tg = sp.symbols('mu z E Tf Tg', real=True)
    S = E+2*Tf+2*Tg
    phase = -(mu-z)**2*E+2*(mu-z)*(z*Tf-(1-z)*Tg)
    expected_phase = (mu-z)*(z*S-mu*E-2*Tg)
    checks = {
        'nonlocal_tail_total_derivative': sp.expand(J*J-2*L*J-2*Q**2*U*V-4*Q*V*V-tail_flux_derivative),
        'third_jet_integration_by_parts': sp.expand(pre-dx(flux1)-P),
        'sum_of_squares_total_derivative': sp.expand(P-sos-dx(flux2)),
        'all_mixed_targets_phase_polynomial': sp.expand(phase-expected_phase),
        'phase_degree_two_coefficient': sp.expand(sp.Poly(phase,z).coeff_monomial(z*z)+S),
    }
    for label,value in checks.items():
        if value != 0:
            raise AssertionError((label,value))
    payload = {
        'kind':'exact_symbolic_algebra_only',
        'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        'identities':{label:str(value) for label,value in checks.items()},
        'positive_lower_bound_coefficient':str(sp.Rational(1,128*36)),
        'requires_real_profiles':True,
        'requires_disjoint_supports':True,
        'requires_equal_constant_state_energy':True,
        'constant_geometry_state':{'k':0,'h':1,'omega':0},
        'all_exact_checks_passed':True,
        'geometric_design_evaluated':False,
        'overlapping_profiles_excluded':False,
        'general_finite_families_excluded':False,
    }
    args.out.parent.mkdir(parents=True,exist_ok=True)
    args.out.write_text(json.dumps(payload,indent=2,sort_keys=True)+'\n',encoding='utf-8')
    print(json.dumps({'output':str(args.out),'bytes':args.out.stat().st_size,
                      'sha256':hashlib.sha256(args.out.read_bytes()).hexdigest(),
                      'all_exact_checks_passed':True}))


if __name__=='__main__':
    main()
