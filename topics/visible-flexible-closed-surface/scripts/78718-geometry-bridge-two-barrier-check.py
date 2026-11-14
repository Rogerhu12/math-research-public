#!/usr/bin/env python3
"""Exact author checks for fixed-bridge signs and two-module feedback.
Uses the already audited R21 exact-root existence as a dependency.
No root solve, candidate arrays, PDE, tail request, or new geometry certificate.
"""
import argparse
from fractions import Fraction as F
import hashlib
import json
from math import factorial
from pathlib import Path
import sympy as s

TOPIC = Path(__file__).resolve().parent.parent
PROOF = TOPIC/"notes/2026-11-10-78718-geometry-bridge-two-barrier-feedback-v1.md"
PROOF_SHA = "9336712dd04a7fc8ecd29b72997a3284074a11b4f4b65bea2da8ef3de075fbaa"


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--out",type=Path,required=True)
    args=parser.parse_args()
    if sha(PROOF)!=PROOF_SHA:
        raise ValueError("Frozen proof identity mismatch")
    p,d,t,L=s.symbols("p d t L",positive=True)
    aa=3*p+d;bb=2*p+d
    phi=aa*t**2-bb*t**3
    peak_t=2*aa/(3*bb)
    symbolic={}

    def zero(name,expr):
        value=s.cancel(expr)
        if value!=0:
            raise AssertionError((name,str(value)))
        symbolic[name]=True

    zero("turn_at_end",phi.subs(t,1)-p)
    zero("turn_slope_at_end",s.diff(phi,t).subs(t,1)/L+d/L)
    zero("unique_derivative_factor",s.diff(phi,t)-t*(6*p+2*d-(6*p+3*d)*t))
    zero("critical_point",s.diff(phi,t).subs(t,peak_t))
    zero("peak_value",phi.subs(t,peak_t)-4*aa**3/(27*bb**2))
    zero("left_simple_coefficient",s.diff(phi,t,2).subs(t,0)/L**2-2*(3*p+d)/L**2)
    a,b=s.symbols("a b")
    zero("transmission_AMGM_square",
         ((2-a-b)/2)**2-(1-a)*(1-b)-(a-b)**2/4)
    rb,rc,tc,tb,il,ir,fc,fb,u=s.symbols("rb rc tc tb il ir fc fb u")
    v=tc*il+rc*u+fc
    rhs=rb*v+tb*ir+fb
    zero("interface_source_elimination",
         (u-rhs)-((1-rb*rc)*u-(rb*tc*il+tb*ir+rb*fc+fb)))

    cut=F.from_float(.6)
    atan_lower=F(1,2)-F(1,2)**3/3+F(1,2)**5/5-F(1,2)**7/7
    peak=F(4,27)*F(633,100)**3/F(261,50)**2
    cos_lower=1-F(7,5)**2/2+F(7,5)**4/24-F(7,5)**6/720
    exponent=F(21,20);count=22
    exp_upper=sum((exponent**k/F(factorial(k)) for k in range(count+1)),F(0))
    exp_upper+=(exponent**(count+1)/F(factorial(count+1)))/(1-exponent/F(count+2))
    rational={
        "actual_cut":F(599,1000)<cut<F(601,1000),
        "pt_upper":F(11,7)-atan_lower<F(111,100),
        "sqrt_E_lower":F(11,10)**2<F(5,4),
        "ps_upper":F(28000,6589)<F(17,4),
        "d_upper":F(19600,6589)<3,
        "phase_peak":peak<F(7,5),
        "cos_lower":cos_lower>F(1,6),
        "omega_lower":F(59,100)**3>F(1,5),
        "sturm_length":F(7,10)/F(59,100)**2<F(21,10),
        "phase_slope":F(1266,100)/(4*F(3,5))<F(53,10),
        "potential_full":216*F(53,10)<1200,
        "potential_positive":216*F(17,4)==918,
        "S_bound":919<31**2,
        "reverse_log_bound":1080<33**2,
        "exponential":exp_upper<3,
        "outer_constant":31*33*3<3100,
    }
    if not all(rational.values()):
        raise AssertionError([k for k,v in rational.items() if not v])
    source_names=[
        "results/R21-m12-whole-map-and-actual-metric-decrease.md",
        "scripts/db6f-root-exact-bridge.py",
        "repro/source-root/topics/large-amplitude-twist-flex/scripts/f6curve_bidirectional_bridge.py",
    ]
    sources=[{"path":name,"bytes":(TOPIC/name).stat().st_size,"sha256":sha(TOPIC/name)}
             for name in source_names]
    report={
        "scope":__doc__.strip(),
        "proof":str(PROOF.relative_to(TOPIC)),
        "proof_sha256":PROOF_SHA,
        "checker_sha256":sha(Path(__file__).resolve()),
        "symbolic_checks":symbolic,
        "rational_checks":rational,
        "symbolic_count":len(symbolic),
        "rational_count":len(rational),
        "source_bindings":sources,
        "exp_upper":str(exp_upper),
        "root_solves":0,
        "pde_runs":0,
        "tail_calls":0,
        "candidate_arrays_read":0,
        "passed":True,
    }
    args.out.write_text(json.dumps(report,indent=2,ensure_ascii=False)+"\n")
    print(json.dumps({
        "passed":True,"symbolic_count":len(symbolic),"rational_count":len(rational),
        "report_bytes":args.out.stat().st_size,"report_sha256":sha(args.out),
        "root_solves":0,"pde_runs":0,"tail_calls":0,
    },sort_keys=True))


if __name__=="__main__":
    main()

