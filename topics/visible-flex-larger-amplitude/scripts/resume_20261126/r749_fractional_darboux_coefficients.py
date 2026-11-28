#!/usr/bin/env python3
"""Exact finite CK coefficients of the R749 C^2 Darboux solution in its actual R744/R746 edge chart."""
import argparse
from fractions import Fraction as Q
from hashlib import sha256
import json
import math
import os
from pathlib import Path
import subprocess


class P:
    """Truncated bivariate rational polynomial in x=s-s0 and v."""
    nx = 0
    nv = 0

    def __init__(self, terms=None):
        self.t = {k:Q(c) for k,c in (terms or {}).items() if c and k[0]<=self.nx and k[1]<=self.nv}

    @classmethod
    def mon(cls,i,j,c=1):
        return cls({(i,j):c})

    def __add__(self,b):
        if not isinstance(b,P):
            b = P.mon(0,0,b)
        r = self.t.copy()
        for k,c in b.t.items():
            r[k] = r.get(k,0)+c
        return P(r)

    __radd__ = __add__

    def __neg__(self):
        return P({k:-v for k,v in self.t.items()})

    def __sub__(self,b):
        return self+(-b)

    def __rsub__(self,b):
        return (-self)+b

    def __mul__(self,b):
        if not isinstance(b,P):
            return P({k:c*b for k,c in self.t.items()})
        out = {}
        for (i,j),a in self.t.items():
            for (k,l),c in b.t.items():
                key = (i+k,j+l)
                if key[0]<=self.nx and key[1]<=self.nv:
                    out[key] = out.get(key,0)+a*c
        return P(out)

    __rmul__ = __mul__

    def diff(self,axis):
        r = {}
        for (i,j),c in self.t.items():
            if axis==0 and i:
                r[i-1,j] = i*c
            if axis==1 and j:
                r[i,j-1] = j*c
        return P(r)

    def move_v(self,n):
        if any(j+n<0 for i,j in self.t):
            raise ValueError("nonanalytic division by a radial power")
        return P({(i,j+n):c for (i,j),c in self.t.items()})

    def integrate_v(self):
        return P({(i,j+1):c/(j+1) for (i,j),c in self.t.items()})

    def row(self,i):
        return [self.t.get((i,j),Q(0)) for j in range(self.nv+1)]


RADIUS = Q(27,250)
BLEND = Q(1,2000)
KAPPA = Q(20,3)
POWER = Q(5,2)


def target(radial):
    # On the actual initial S5 turn, eta'=S5(v/BLEND)/RADIUS.
    P.nv = radial+6
    beta = (P.mon(0,4,Q(5,2)/(RADIUS*BLEND**3))
            -P.mon(0,5,3/(RADIUS*BLEND**4))
            +P.mon(0,6,1/(RADIUS*BLEND**5)))
    sin_beta = P()
    power = beta
    sq = beta*beta
    for m in range(1,2*(P.nv//4)+1,2):
        sin_beta += power*(Q((-1)**((m-1)//2),math.factorial(m)))
        power = power*sq
    d = sin_beta.integrate_v()
    A = 1-KAPPA*d
    a_v_div_v = A.diff(1).move_v(-1)
    curvature = (KAPPA*A*d.diff(1).diff(1)).move_v(-3)
    P.nv = radial
    A, d = P(A.t),P(d.t)
    inv,term = P.mon(0,0),P.mon(0,0)
    for _ in range(1,radial//5+1):
        term = term*(KAPPA*d)
        inv += term
    return A,P(a_v_div_v.t),P(curvature.t),inv


def nonlinear_residue(u, data):
    A, av_v, curvature, inv = data
    us,uv = u.diff(0),u.diff(1)
    T = POWER*u+uv.move_v(1)
    B = POWER*(POWER-1)*u+2*POWER*uv.move_v(1)+uv.diff(1).move_v(2)
    D = POWER*us+us.diff(1).move_v(1)-(av_v*inv*us).move_v(2)
    W = 1-(us*us*inv*inv).move_v(5)-(T*T).move_v(3)
    return B*(us.diff(0)+A*av_v*T)-D*D-curvature*W


def polynomial(height,order,radial):
    P.nx = order
    data = target(radial)
    u = P.mon(0,0,height)
    for i in range(order-1):
        err = nonlinear_residue(u,data).row(i)
        divisor = POWER*(POWER-1)*height*(i+1)*(i+2)
        u += P({(i+2,j):-c/divisor for j,c in enumerate(err) if c})
    residual = nonlinear_residue(u,data)
    nonzero = [[i,j,str(c)] for (i,j),c in sorted(residual.t.items()) if i<=order-2]
    coeff = [[str(x) for x in u.row(i)] for i in range(order+1)]
    return coeff,nonzero


def word(data):
    return (json.dumps(data,sort_keys=True,separators=(",",":"))+"\n").encode()


def main():
    cli = argparse.ArgumentParser(description=__doc__)
    cli.add_argument("--summary",required=True,type=Path)
    cli.add_argument("--raw",required=True,type=Path)
    cli.add_argument("--orders",nargs="+",type=int,default=[4,8,12])
    cli.add_argument("--radial",nargs="+",type=int,default=[8,12,16])
    cli.add_argument("--heights",nargs="+",type=int,default=[1,64])
    args = cli.parse_args()
    if os.environ.get("GITHUB_ACTIONS")!="true" or os.environ.get("GITHUB_REPOSITORY")!="Rogerhu12/math-research-public":
        raise RuntimeError("run in the public project Actions")
    if len(args.orders)!=len(args.radial) or any(n<2 for n in args.orders) or any(n<1 for n in args.radial) or any(h<=0 for h in args.heights):
        raise ValueError("positive heights and compatible finite coefficient boxes required")
    if args.orders!=sorted(args.orders) or args.radial!=sorted(args.radial):
        raise ValueError("coefficient boxes must be nested in both directions")
    all_data, meta = {},[]
    for height in args.heights:
        last = None
        for order,radial in zip(args.orders,args.radial):
            coeff,errors = polynomial(Q(height),order,radial)
            key = f"h{height}-x{order}-v{radial}"
            full = {"u_coefficients_rows_x_cols_v":coeff,"nonzero_checked_darboux_residuals":errors}
            raw = word(full)
            stable = None
            if last is not None:
                stable = all(coef==coeff[i][j] for i,row in enumerate(last)
                             for j,coef in enumerate(row))
            all_data[key] = full
            meta.append({"key":key,"bytes":len(raw),"sha256":sha256(raw).hexdigest(),
                         "checked_residual_rows":order-1,"checked_residual_columns":radial+1,
                         "number_nonzero_residuals":len(errors),"first_nonzero_residuals":errors[:2],
                         "coefficient_count":(order+1)*(radial+1),
                         "nonzero_coefficients":sum(c!="0" for row in coeff for c in row),
                         "previous_box_identical":stable,"u_x2_v0":coeff[2][0],
                         "u_xlast_vlast":coeff[-1][-1]})
            last = coeff
    raw = word(all_data)
    args.raw.parent.mkdir(parents=True,exist_ok=True)
    args.raw.write_bytes(raw)
    script = Path(__file__).read_bytes()
    summary = {"schema":"R749-actual-rational-Darboux-CK-coefficients-v1",
               "run":os.environ["GITHUB_RUN_ID"],"attempt":os.environ["GITHUB_RUN_ATTEMPT"],
               "source_commit":subprocess.check_output(["git","rev-parse","HEAD"],text=True).strip(),
               "trigger_commit":os.environ["GITHUB_SHA"],"rules_read_commit":os.environ["R749_RULES_COMMIT"],
               "source_script":{"bytes":len(script),"sha256":sha256(script).hexdigest()},
               "actual_target":{"r_y":str(RADIUS),"eps_y":str(BLEND),"kappa":str(KAPPA),
                                "d5":str(1/(2*RADIUS*BLEND**3)),"z_power":str(POWER),
                                "material":"s0=s1+eps_x/2+r_x*(pi-.5), right straight-wall trace after s+r_x*theta"},
               "boxes":meta,"whole_raw":{"bytes":len(raw),"sha256":sha256(raw).hexdigest(),"uploaded":False},
               "scope":"Exact truncated coefficient/residual identities. No analytic width, convergence-rate bound, global metric certificate, or mesh is inferred from finite coefficients."}
    args.summary.parent.mkdir(parents=True,exist_ok=True)
    args.summary.write_bytes(word(summary))
    print(json.dumps(summary,separators=(",",":")),flush=True)


if __name__=="__main__":
    main()
