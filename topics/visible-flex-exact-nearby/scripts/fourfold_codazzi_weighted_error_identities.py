#!/usr/bin/env python3
"""Independent exact identities for R134; no numerical continuation claimed."""
from __future__ import annotations
import argparse,json
from hashlib import sha256
from pathlib import Path
import sympy as s


def run():
    p,q,P,Q,pt,qt,beta,kappa,gamma,U,V=s.symbols('p q P Q pt qt beta kappa gamma U V')
    f=lambda x,y:-beta*y*(1+x*x)+kappa*(x-y)
    g=lambda x,y:-beta*x*(1+y*y)-kappa*(x-y)
    H=beta*(1-p*q)+2*kappa
    w=1/(q-p)
    wr=s.diff(w,p)*(gamma*q*pt+f(p,q))+s.diff(w,q)*(gamma*p*qt+g(p,q))
    wt=s.diff(w,p)*pt+s.diff(w,q)*qt
    u,v=p-P,q-Q
    a=-beta*q*(p+P)+kappa;b=-beta*(1+P*P)-kappa
    c=-beta*(1+Q*Q)-kappa;e=-beta*p*(q+Q)+kappa
    ag=lambda x,y:beta*(1-3*x*y)+3*kappa
    bg=lambda x:-beta*(1+x*x)-kappa
    da=ag(p,q)-ag(P,Q)
    expressions={
        'actual_first_transport_weight':wr-gamma*q*wt-gamma*qt*w+H*w,
        'actual_second_transport_weight':wr-gamma*p*wt-gamma*pt*w+H*w,
        'full_nonlinear_first_source_difference':f(p,q)-f(P,Q)-a*u-b*v,
        'full_nonlinear_second_source_difference':g(p,q)-g(P,Q)-c*u-e*v,
        'first_C0_energy_diagonal':2*a-H+beta*(1+p*q+2*q*P),
        'second_C0_energy_diagonal':2*e-H+beta*(1+p*q+2*p*Q),
        'weighted_gradient_energy_diagonal':2*ag(p,q)-H-(beta*(1-5*p*q)+4*kappa),
        'weighted_gradient_energy_offdiagonal':bg(p)+bg(q)+beta*(2+p*p+q*q)+2*kappa,
        'first_gradient_error_source_matrix':da*U+(bg(p)-bg(P))*V-
            ((-3*beta*q*U-beta*(p+P)*V)*u-3*beta*P*U*v),
        'second_gradient_error_source_matrix':(bg(q)-bg(Q))*U+da*V-
            (-3*beta*q*V*u+(-beta*(q+Q)*U-3*beta*P*V)*v),
    }
    checks={name:bool(s.cancel(expr)==0) for name,expr in expressions.items()}
    if not all(checks.values()):raise ValueError(checks)
    root=Path(__file__).resolve().parents[1]
    files=[Path(__file__).resolve(),root/'results/R134-weighted-error-energy-and-Sobolev-continuation.md',
           root/'results/R131-linear-degenerate-weighted-gradient-and-C0-continuation.md']
    return dict(kind='R134_exact_weighted_error_energy_identity_checks',complete=True,
        engine='SymPy exact rational and polynomial arithmetic',version=s.__version__,checks=checks,
        all_pass=True,retains_full_mean=True,actual_background_must_be_real=True,
        no_numerical_long_interval_barrier_executed=True,closed_surface_complete=False,
        files_sha256={str(p.relative_to(root)):sha256(p.read_bytes()).hexdigest() for p in files})


if __name__=='__main__':
    ap=argparse.ArgumentParser(description=__doc__);ap.add_argument('--out',type=Path,required=True)
    a=ap.parse_args()
    if a.out.exists():raise FileExistsError('new report path required')
    report=run();a.out.write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')
    print(dict(all_pass=report['all_pass'],checks=len(report['checks']),out=str(a.out)))
