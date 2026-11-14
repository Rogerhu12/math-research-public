#!/usr/bin/env python3
"""Fixed Poisson-core/twin-marker scalar budget, using frozen R27 rational intervals.

No source solve, integration, angular scan, optimization or candidate-data read.
"""
import argparse
from fractions import Fraction as Q
from hashlib import sha256
import json
from math import isqrt
from pathlib import Path


def enc(x):
    if isinstance(x,Q):
        return {"numerator":str(x.numerator),"denominator":str(x.denominator)}
    if isinstance(x,dict):
        return {k:enc(v) for k,v in x.items()}
    if isinstance(x,list):
        return [enc(v) for v in x]
    return x


def readq(x):
    assert set(x)=={"numerator","denominator"}
    return Q(int(x["numerator"]),int(x["denominator"]))


def bounds(x):
    lo,hi=readq(x["lower"]),readq(x["upper"])
    assert lo<=hi
    return lo,hi


def sqrtbox(x):
    assert x>=0
    scale=1<<120
    n=isqrt((x.numerator*scale*scale)//x.denominator)
    lo=Q(n,scale)
    hi=lo if lo*lo==x else Q(n+1,scale)
    assert lo*lo<=x<=hi*hi
    return lo,hi


def floorstr(x,places=14):
    assert x>=0
    scale=10**places
    n=x.numerator*scale//x.denominator
    return str(n//scale)+"."+str(n%scale).zfill(places)


def ceilstr(x,places=14):
    assert x>=0
    scale=10**places
    n=-((-x.numerator*scale)//x.denominator)
    return str(n//scale)+"."+str(n%scale).zfill(places)


def main():
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--out",required=True)
    args=ap.parse_args()
    topic=Path(__file__).resolve().parents[1]
    source_specs={
      "results/R27-poisson-c3-core-and-conditional-held-transfer.md":
        "dd8ddca61e9609f1e0899692015938ff351d61bb9e8e9936d6ba4b236c11849a",
      "notes/2026-11-09-db6f-prefix-c3-poisson-bounds.json":
        "4d84a5f3533f367fc8acfb2501c20e16c157e0a41d02f5207e0ea05c3fc0908e",
      "scripts/db6f-prefix-c3-poisson-bounds.py":
        "6f804847b44a8395c4abb5b325ed2b83f855c056b8bbc51ed1b7768e7f46c7b9",
      "results/R29-c3-mechanism-interface-and-convex-held-envelope.md":
        "a4274cb2f6a931b59c7af94945d91eb1e74610fe6d511bfbadae8ae131ab82c1"
    }
    sources=[]
    for rel,want in source_specs.items():
        data=(topic/rel).read_bytes()
        assert sha256(data).hexdigest()==want
        sources.append({"path":rel,"bytes":len(data),"sha256":want})
    original=json.loads((topic/"notes/2026-11-09-db6f-prefix-c3-poisson-bounds.json").read_text())
    chosen=[row for row in original["cases"]
            if readq(row["q"])==Q(99,100) and readq(row["r"])==Q(1,10)]
    assert len(chosen)==1
    row=chosen[0]
    hminlo,hminhi=bounds(row["inradius"])
    dlo,dhi=bounds(row["diameter"])
    gaplo,gaphi=bounds(row["delta"])
    Hlo,Hhi=hminlo+gaplo,hminhi+gaphi
    rho_min=readq(row["rho_min"])
    assert rho_min==Q(104,995)

    z=Q(3,10)
    b=Q(1,100)
    a=Q(1,10)
    e0=e1=Q(1,200)
    Dstar=Q(251,100)
    Z=z+b
    assert z>=b>=0
    Llo=sqrtbox(4*Hlo*Hlo+Z*Z)[0]
    Lhi=sqrtbox(4*Hhi*Hhi+Z*Z)[1]
    Ulo=sqrtbox(dlo*dlo+Z*Z)[0]
    Uhi=sqrtbox(dhi*dhi+Z*Z)[1]
    corehi=sqrtbox(dhi*dhi+4*b*b)[1]
    markerhi=2*z+2*a
    assert corehi<=Ulo
    assert markerhi<Ulo+a
    assert max(corehi,markerhi)<Llo+a
    # Thus the exact unperturbed initial diameter is sqrt(4H^2+Z^2)+a.
    D0lo=Llo+a-2*e0
    D0hi=Lhi+a+2*e0
    D1hi=Uhi+a+2*e1
    assert D0lo>0 and D0hi<Dstar
    rigid_ratio=(D0lo-D1hi)/(2*D0lo)
    held=gaplo-e0-e1
    held_ratio=held/D0hi
    thickness_margin=9*Llo-10*Uhi-(a+18*e0+20*e1)
    assert thickness_margin>0 and rigid_ratio>Q(1,20)
    assert held_ratio>Q(1,5) and held>Dstar/5

    # u=(1/2,+/-sqrt(3)/2) are initial minimum-support directions.
    # Both marker centers have u.proj(P)=-H/2.
    marker_support_upper=-Hlo/2+a
    shadow_margin=hminlo-marker_support_upper
    assert shadow_margin>0
    # The cap axes v+/- give fixed q+/- with vertical separation >=2z.
    fixed_grip_diameter_lower=2*z
    assert fixed_grip_diameter_lower>Dstar/5
    rho_goal=3*Dstar/100
    marker_core_gap=z-a-b
    marker_marker_gap=2*z-2*a
    assert min(rho_min,a)>rho_goal
    assert min(marker_core_gap,marker_marker_gap)>2*rho_goal

    result={
      "status":"EXACT_CONDITIONAL_TWIN_MARKER_STRONG_GEOMETRIC_BUDGET",
      "scope":"Disconnected compact-piece model/convex hull; not a connected closed isometric family.",
      "source_script_sha256":sha256(Path(__file__).read_bytes()).hexdigest(),
      "sources":sources,
      "core_parameters":{"q":Q(99,100),"r":Q(1,10),"orientation":"R27 core rotated by pi/3"},
      "source_bounds":{"hmin_lower":hminlo,"hmin_upper":hminhi,
         "Delta_lower":gaplo,"Delta_upper":gaphi,
         "diameter_lower":dlo,"diameter_upper":dhi,
         "H_lower":Hlo,"H_upper":Hhi,
         "origin_radius_equals_H_by_support_extremum":True,"rho_min":rho_min},
      "model_parameters":{"z":z,"core_halfheight":b,"marker_radius":a,
        "epsilon0":e0,"epsilon1":e1,"Dstar":Dstar},
      "witness_and_enclosures":{"L0_lower":Llo,"L0_upper":Lhi,
        "U1_lower":Ulo,"U1_upper":Uhi,
        "initial_unperturbed_diameter_equals_L0_plus_a":True,
        "final_diameter_cases":{"core_core_upper":corehi,
          "all_marker_pairs_upper":markerhi,"core_marker_upper":Uhi+a},
        "all_final_cases_bounded_by_U1_plus_a":True,
        "D0_after_error_lower":D0lo,"D0_after_error_upper":D0hi,
        "D1_after_error_upper":D1hi,
        "strict_rigid_thickness_margin":thickness_margin,
        "rigid_quotient_ratio_lower":rigid_ratio,
        "held_model_equals_Delta":True,
        "held_after_error_lower":held,"held_ratio_after_error_lower":held_ratio,
        "marker_support_upper_in_unshadowed_min_directions":marker_support_upper,
        "strict_marker_nonshadowing_margin":shadow_margin,
        "fixed_cap_pair_diameter_lower":fixed_grip_diameter_lower},
      "local_compatibility_only":{"README_reach_target_at_Dstar":rho_goal,
        "core_curvature_radius_lower":rho_min,
        "fixed_marker_curvature_radius":a,
        "marker_core_vertical_separation_lower":marker_core_gap,
        "marker_marker_vertical_separation_lower":marker_marker_gap,
        "global_closed_surface_reach_claimed":False,
        "Hausdorff_error_preserves_curvature_claimed":False,
        "fixed_material_H_requires_actual_retention_of_both_caps":True},
      "safe_displays":{"H_lower":floorstr(Hlo),"H_upper":ceilstr(Hhi),
        "D0_after_error_upper":ceilstr(D0hi),
        "rigid_ratio_lower":floorstr(rigid_ratio),
        "held_ratio_lower":floorstr(held_ratio),
        "fixed_cap_diameter_ratio_lower":floorstr(fixed_grip_diameter_lower/D0hi)},
      "all_exact_strict_gates_passed":True,
      "current_M15_candidate_data_read":False,
      "new_solver_root_RK_integration_optimization_calls":0,
      "connected_closed_family_or_common_metric_extension_constructed":False
    }
    for key in ("rigid_ratio_lower","held_ratio_lower"):
        val=rigid_ratio if key=="rigid_ratio_lower" else held_ratio
        assert Q(result["safe_displays"][key])<val
    out=Path(args.out).resolve()
    with out.open("x") as f:
        json.dump(enc(result),f,ensure_ascii=False,indent=2)
        f.write("\n")
    print(json.dumps({"status":result["status"],**result["safe_displays"],
       "bytes":out.stat().st_size,"report_sha256":sha256(out.read_bytes()).hexdigest()}))


if __name__=="__main__":
    main()
