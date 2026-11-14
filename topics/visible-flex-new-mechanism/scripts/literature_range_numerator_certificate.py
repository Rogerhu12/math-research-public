#!/usr/bin/env python3
"""Exact cancellation checks for the variable-coefficient full range calculus."""
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
    h,z=sp.symbols('h z',nonzero=True)
    k,gamma,nu=sp.symbols('k gamma nu')
    P,Ps,Px,B,Bs,Bx=sp.symbols('P Ps Px B Bs Bx')
    Tx,Ts,Tsx=sp.symbols('T_xi T_s T_sxi')
    W,Wx=sp.symbols('W W_xi')
    J=2*h*B;Js=2*gamma*B+2*h*Bs;Jx=2*h*Bx
    Hxx=Tx/z**2-Jx/z**3+J/z**4
    Hss=Ts/z**2-nu*Js/z**3+nu**2*J/z**4
    Hsx=Tsx/z**2-(Js+nu*Jx)/(2*z**3)+nu*J/z**4
    u=h/z;ux=-h/z**2;c=(gamma*z-h*nu)/z**2
    rho=P+B/z;rhox=Px+Bx/z-B/z**2;rhos=Ps+Bs/z-nu*B/z**2
    K0=k*z*z-(k*k+1)*z/h
    lam=(gamma*z-h*nu)/h**2
    R_original=Hss/(2*u*u)+K0*rho-lam*rhos
    R_expected=Ts/(2*h*h)+K0*P-lam*Ps+(k*z-(k*k+1)/h)*B-gamma*Bs/(h*h)
    eta_original=(Hsx-c*rhox)/(2*ux)-rhos/2
    eta_expected=-Tsx/(2*h)+(gamma*z-h*nu)*Px/(2*h)+gamma*Bx/(2*h)-Ps/2
    eta=eta_original-u*W+h*Wx/2
    p=(u*u*W+u*eta)/(h*h)
    qb=eta-k*p
    A=Wx/2+eta_expected/h
    checks={
        'right_anchored_rho_derivative':sp.factor((rhox-Hxx/(2*ux)).subs(Px,-Tx/(2*h))),
        'full_R_rational_cancellation':sp.factor(R_original-R_expected),
        'full_eta0_rational_cancellation':sp.factor(eta_original-eta_expected),
        'recovered_T_numerator':sp.factor(p-A/z),
        'recovered_N_numerator':sp.factor(rho-(z*P+B)/z),
        'recovered_B_numerator':sp.factor(qb-((h*z-k)*A-h*W)/z),
    }
    for label,value in checks.items():
        if value!=0:
            raise AssertionError((label,value))
    payload={
        'kind':'exact_symbolic_range_algebra_only',
        'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        'identities':{key:str(value) for key,value in checks.items()},
        's_derivative_holds_xi_fixed':True,
        'forcing_matrix_is_symmetric_and_spatially_constant':True,
        'h_and_omega_may_vary_with_s':True,
        'all_exact_checks_passed':True,
        'whole_range_conditions_satisfied':False,
        'profile_basis_independence_certified':False,
        'geometric_design_evaluated':False,
        'finite_family_certified':False,
    }
    args.out.parent.mkdir(parents=True,exist_ok=True)
    args.out.write_text(json.dumps(payload,indent=2,sort_keys=True)+'\n',encoding='utf-8')
    print(json.dumps({'output':str(args.out),'bytes':args.out.stat().st_size,
                     'sha256':hashlib.sha256(args.out.read_bytes()).hexdigest(),
                     'all_exact_checks_passed':True}))


if __name__=='__main__':
    main()
