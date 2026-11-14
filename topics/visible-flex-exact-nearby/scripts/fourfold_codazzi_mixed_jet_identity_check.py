#!/usr/bin/env python3
"""Independent symbolic check of all 24 mixed Codazzi residual jet entries.

This supplements the formal normalized-jet proof. It is not a substitute
for the complete original-target residual validation.
"""
import argparse
import hashlib
import json
import math
from pathlib import Path
import sympy as s
from flint import arb,ctx
from fourfold_codazzi_residual_taylor import Jet,residual_jets
from fourfold_phase_beta_bulk_box import Box


def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--out',type=Path,required=True);a=p.parse_args();ctx.prec=192
    if a.out.exists():raise FileExistsError(a.out)
    r,t=s.symbols('r t')
    B=r/8+t/4+r**3/64+r*t*t/32+t**4/128
    C=-2+r/8+t/16+r*t/32+r*r*t*t/64
    K=-1+r/16+r*r/32;G=1+r/64+r*r/128;H=r/32+r*r/64
    def point(f):
        return Jet([[Box(float(s.diff(f,r,i,t,j).subs({r:0,t:0})
                               /math.factorial(i)/math.factorial(j)))
                     for j in range(5)] for i in range(4)])
    def exact(v):return arb(int(s.numer(v)))/int(s.denom(v))
    coeff={}
    for name,f in [('K',K),('gamma',G),('beta',H)]:
        for i in range(3):coeff[name+('' if i==0 else str(i))]=exact(s.diff(f,r,i).subs(r,0))
    b,c=residual_jets(point(B),point(C),coeff)
    A=(K+B*B)/C
    original=[s.diff(B,r)-G*s.diff(A,t)+2*H*B,
              s.diff(C,r)-G*s.diff(B,t)-H*(A-C)]
    checks=[]
    for name,jet,f in zip(['RB','RC'],[b,c],original):
        for i in range(3):
            for j in range(4):
                value=s.diff(f,r,i,t,j).subs({r:0,t:0})/math.factorial(i)/math.factorial(j)
                reference=exact(value);box=jet[i,j]
                good=bool(reference>=arb(float(box.lo)) and reference<=arb(float(box.hi)))
                checks.append(dict(field=name,radial=i,angular=j,exact_normalized_value=str(value),
                                   interval=[float(box.lo),float(box.hi)],passed=good))
    if not all(x['passed'] for x in checks):raise ValueError('mixed residual identity check failed')
    sha=lambda path:hashlib.sha256(Path(path).read_bytes()).hexdigest()
    result=dict(kind='independent_exact_symbolic_mixed_Codazzi_jet_check',
        source_sha256=sha(__file__),implementation_sha256=sha(Path(__file__).with_name('fourfold_codazzi_residual_taylor.py')),
        symbolic_inputs={name:str(f) for name,f in [('B',B),('C',C),('K',K),('gamma',G),('beta',H)]},
        checks=checks,all_pass=True,native_original_target_bound_claimed=False)
    a.out.write_text(json.dumps(result,indent=2)+'\n')
    print('passed',len(checks))


if __name__=='__main__':main()
