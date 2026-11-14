#!/usr/bin/env python3
"""Exact finite positive-kernel section bounds; no prefix/tail or geometry solve."""
from __future__ import annotations
import argparse
import hashlib
import json
from fractions import Fraction as Q
from pathlib import Path

SCALE = 10**12


def rational(x):
    return {"numerator": str(x.numerator), "denominator": str(x.denominator)}


def down(x):
    return Q((x.numerator*SCALE)//x.denominator, SCALE)


def up(x):
    return -down(-x)


def decimal(x):
    n = x.numerator*(SCALE//x.denominator)
    sign = "-" if n < 0 else ""
    n = abs(n)
    return f"{sign}{n//SCALE}.{n%SCALE:012d}"


def interval(lo,hi):
    assert lo <= hi
    a,b = down(lo),up(hi)
    return {"lower":rational(a), "upper":rational(b),
            "lower_decimal":decimal(a), "upper_decimal":decimal(b)}


def build(N,r,D,height):
    assert isinstance(N,int) and N >= 1 and 0 < r < 1
    a = {k:Q(N+1-abs(k),N+1) for k in range(-N,N+1)}
    c = {j:sum((a[k]*a.get(j-k,Q(0)) for k in a),Q(0))
         for j in range(-2*N,2*N+1)}
    assert c[0] == Q(2*N*N+4*N+3,3*(N+1))
    b = {j:c[j]/c[0] for j in range(1,2*N+1)}
    assert all(0 < x < 1 for x in b.values())
    assert all(c[j] == c[-j] for j in c)
    rho_max = r+(1-r)*(N+1)**2/c[0]
    delta = 4*(1-r)*sum((b[j]/(9*j*j-1) for j in b if j%2),Q(0))
    diameter_upper = 2+4*(1-r)*sum((b[j]/(9*j*j-1) for j in b if not j%2),Q(0))
    inradius = 1-2*(1-r)*sum((b[j]/(9*j*j-1) for j in b),Q(0))
    # Acceptance uses only the outward rounded published endpoints.
    dl,du = down(delta),up(diameter_upper)
    margins = {
        "whole_diameter_squared":D*D-du*du-height*height,
        "held_target":dl-D/5,
        "core_reach_target_only":r-3*D/100,
        "unconstructed_grip_disk_projection":down(inradius)-Q(3,10),
        "unconstructed_grip_disk_diameter":Q(3,5)-D/5,
    }
    assert all(x > 0 for x in margins.values())
    return {
        "Fejer_order":N, "rho_and_support_C3_harmonics":2*N,
        "rho_and_support_max_normal_angle_frequency":6*N,
        "Cartesian_max_normal_angle_frequency":6*N+1,
        "finite_in_arclength_Fourier_basis_asserted":False,
        "r":rational(r), "normalization_c0":rational(c[0]),
        "positive_fourier_b":[{"j":j,**rational(b[j])} for j in b],
        "rho_min_exact":rational(r), "rho_max_exact":rational(rho_max),
        "delta_exact":rational(delta), "delta":interval(delta,delta),
        "diameter_upper_exact":rational(diameter_upper),
        "diameter_upper":interval(diameter_upper,diameter_upper),
        "inradius_exact":rational(inradius), "inradius":interval(inradius,inradius),
        "plane_ratio_lower":interval(delta/diameter_upper,delta/diameter_upper),
        "whole_D_budget":rational(D), "z_span_budget":rational(height),
        "projection_leakage":rational(Q(0)),
        "strict_margins":{k:interval(x,x) for k,x in margins.items()},
        "all_strict_rational_checks_passed":True,
        "whole_budget_scope":"CONDITIONAL; no closed surface, fixed grip or whole reach asserted",
    }


def bind(f,root):
    b=f.read_bytes()
    return {"path":str(f.relative_to(root)),"bytes":len(b),
            "sha256":hashlib.sha256(b).hexdigest()}


def main():
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--out",type=Path,required=True)
    args=ap.parse_args()
    if args.out.exists():
        raise FileExistsError(args.out)
    rows=[
        build(3,Q(1,10),Q(43,20),Q(27,50)),
        build(4,Q(3,20),Q(107,50),Q(23,50)),
        build(7,Q(3,20),Q(23,10),Q(9,10)),
        build(7,Q(1,10),Q(12,5),Q(11,10)),
    ]
    script=Path(__file__).resolve()
    root=script.parents[3]
    topic=root/"topics/visible-flexible-closed-surface"
    sources=[script,topic/"notes/2026-11-09-db6f-prefix-c3-poisson-core.md",
             topic/"README.md",topic/"results/R10-positive-support-offset-reach.md"]
    report={
        "status":"EXACT_FINITE_POSITIVE_TRIGONOMETRIC_AUXILIARY_CORE_ONLY",
        "same_as_current_frozen_g":False,
        "new_closed_surface_or_flexible_family_asserted":False,
        "rounding_scale":SCALE,
        "rounding":"integer floor/ceiling of exact Fraction; no binary floating arithmetic",
        "source_bindings":[bind(f,root) for f in sources],
        "cases":rows,
        "solver_root_RK_geometry_backend_calls":0,
    }
    args.out.write_text(json.dumps(report,ensure_ascii=False,indent=2)+"\n")
    data=args.out.read_bytes()
    print(json.dumps({"status":"PASS","cases":len(rows),"bytes":len(data),
                      "sha256":hashlib.sha256(data).hexdigest(),"solver_calls":0}))


if __name__=="__main__":
    main()
