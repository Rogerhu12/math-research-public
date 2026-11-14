#!/usr/bin/env python3
"""Independent exact scalar and source audit of frozen local collar proofs.

Uses only hashlib, JSON, Fraction, integer polynomial coefficients and bisection.
It does not import the author's arithmetic scripts or any geometric solver.
"""
from argparse import ArgumentParser
from fractions import Fraction as F
from hashlib import sha256
from math import comb
from pathlib import Path
import json

TOPIC = Path(__file__).resolve().parents[1]
PREFIX = "2026-11-09-db6f-"


def identity(rel):
    data = (TOPIC / rel).read_bytes()
    return {"path": rel, "bytes": len(data), "sha256": sha256(data).hexdigest()}


def decode(obj):
    if isinstance(obj, dict) and set(obj) == {"numerator", "denominator"}:
        return F(int(obj["numerator"]), int(obj["denominator"]))
    if isinstance(obj, dict):
        return {k: decode(v) for k, v in obj.items()}
    if isinstance(obj, list):
        return [decode(v) for v in obj]
    return obj


def encode(obj):
    if isinstance(obj, F):
        return {"numerator": str(obj.numerator), "denominator": str(obj.denominator)}
    if isinstance(obj, dict):
        return {k: encode(v) for k, v in obj.items()}
    if isinstance(obj, (list, tuple)):
        return [encode(v) for v in obj]
    return obj


def sqrt_bisection(value):
    assert value >= 0
    lo, hi = F(0), F(1)
    while hi * hi < value:
        hi *= 2
    for _ in range(180):
        mid = (lo + hi) / 2
        if mid * mid <= value:
            lo = mid
        else:
            hi = mid
    assert lo * lo <= value <= hi * hi
    return lo, hi


def main():
    parser = ArgumentParser(description=__doc__)
    parser.add_argument("--out", required=True)
    args = parser.parse_args()
    out = Path(args.out).resolve()
    assert not out.exists()
    sources = []
    wanted = {
        "notes/" + PREFIX + "audit-positive-collar-publication.json":
        "497d47525bb33b12168fc594d84c693dc205b596661f11b0e83d0b8b4b5ef292",
        "notes/" + PREFIX + "audit-positive-collar-radial-publication.json":
        "67b4e18269a9817656e38db0ce12895821c0372182a2e6feb4b75a9f26d54f82",
    }
    publication_counts = []
    for rel, expected in wanted.items():
        item = identity(rel)
        assert item["sha256"] == expected
        sources.append(item)
        publication = json.loads((TOPIC / rel).read_text())
        for old in publication["files"]:
            item = identity(old["path"])
            assert item["sha256"] == old["sha256"] and item["bytes"] == old["bytes"]
            sources.append(item)
        publication_counts.append(len(publication["files"]))
    ledger = json.loads((TOPIC / "notes" / (PREFIX + "audit-positive-collar-sources.json")).read_text())
    for old in ledger["inputs"]:
        item = identity(old["path"])
        assert item["sha256"] == old["sha256"] and item["bytes"] == old["bytes"]
        sources.append(item)
    old_path = "notes/" + PREFIX + "audit-poisson-twin-marker-bounds.json"
    original = decode(json.loads((TOPIC / old_path).read_text()))
    collar_path = "notes/" + PREFIX + "audit-positive-collar-budget.json"
    radial_path = "notes/" + PREFIX + "audit-positive-collar-radial-interface.json"
    collar = decode(json.loads((TOPIC / collar_path).read_text()))
    radial = decode(json.loads((TOPIC / radial_path).read_text()))
    assert original["all_exact_strict_gates_passed"] is True
    source = original["source_bounds"]
    h0, h1 = source["hmin_lower"], source["hmin_upper"]
    H0, H1 = source["H_lower"], source["H_upper"]
    d0, d1 = source["diameter_lower"], source["diameter_upper"]
    gap, m = source["Delta_lower"], source["rho_min"]
    assert m == F(104, 995)
    b, B, z, a = F(1,100), F(9,100), F(3,10), F(1,10)
    eps, Dstar, goal = F(1,200), F(63,25), F(189,2500)
    Zb, ZB = z+b, z+B
    c = collar["diameter_and_witness"]
    sqrt_specs = [
        (4*H0*H0+Zb*Zb, c["initial_witness_Lb_lower"], "lower"),
        (4*H1*H1+Zb*Zb, c["initial_witness_Lb_upper"], "upper"),
        (4*H1*H1+ZB*ZB, c["initial_envelope_LB_upper"], "upper"),
        (d0*d0+ZB*ZB, c["halfphase_envelope_UB_lower"], "lower"),
        (d1*d1+ZB*ZB, c["halfphase_envelope_UB_upper"], "upper"),
        (d1*d1+4*B*B, c["core_core_diameter_upper"], "upper"),
    ]
    for value, bound, side in sqrt_specs:
        inner_lo, inner_hi = sqrt_bisection(value)
        if side == "lower":
            assert bound*bound <= value and bound <= inner_lo
        else:
            assert bound*bound >= value and bound >= inner_hi
    Llo, Lhi = c["initial_witness_Lb_lower"], c["initial_witness_Lb_upper"]
    LBhi, UBhi = c["initial_envelope_LB_upper"], c["halfphase_envelope_UB_upper"]
    comparisons = []

    def equal(label, actual, expected):
        assert actual == expected, label
        comparisons.append(label)

    Dlo, Dhi, Uhi = Llo+a-2*eps, LBhi+a+2*eps, UBhi+a+2*eps
    equal("D0 lower", c["initial_actual_diameter_lower"], Dlo)
    equal("D0 upper", c["initial_actual_diameter_upper"], Dhi)
    equal("D1 upper", c["halfphase_actual_diameter_upper"], Uhi)
    rigid = (Dlo-Uhi)/(2*Dlo)
    held = (gap-2*eps)/Dhi
    equal("rigid lower", c["rigid_quotient_ratio_lower"], rigid)
    equal("held lower", c["held_ratio_lower"], held)
    assert rigid > F(1,20) and held > F(1,5) and Dhi < Dstar
    assert goal == F(3,100)*Dstar and 2*z > Dstar/5
    normal_x, normal_z = F(9,41), F(40,41)
    assert normal_x*normal_x + normal_z*normal_z == 1
    assert 9*(h0+H0)+40*(b-z)-41*a > 0
    necessary = (1-normal_x)*F(3,100)*Dlo
    assert necessary > normal_z*b+eps > eps
    assert normal_z*(B-b)+eps > (1-normal_x)*goal

    # Construct the endpoint polynomial from its binomial definition.
    p = [F(0)]*7
    for k in range(4):
        p[k+3] = F(64*(-1)**k*comb(3,k))
    derivatives = [p]
    for _ in range(2):
        prev = derivatives[-1]
        derivatives.append([j*prev[j] for j in range(1,len(prev))])
    for poly in derivatives:
        assert poly[0] == 0 and sum(poly) == 0
    def evaluate(poly,t):
        return sum(v*t**i for i,v in enumerate(poly))
    assert evaluate(p,F(1,2)) == 1
    delta, ell = F(1,10**6), F(1,200)
    A, M = 4*delta/ell, 24*delta/(ell*ell)
    assert F(192)**2/F(5)**5 < 16
    assert evaluate(derivatives[2],F(1,2)) == -24
    saddle = delta*evaluate(derivatives[2],F(1,10))/(ell*ell)
    assert saddle == F(2376,3125) > 0
    radius = 1/((1/m+delta/(m*m))*(1+A*A)+M)
    support = (h0-(b+ell)*A)/(1+A*A/2)
    temp = collar["explicit_saddle_template"]
    equal("polynomial",temp["polynomial_coefficients_ascending"],p)
    equal("A",temp["slope_bound_A"],A)
    equal("M",temp["second_derivative_bound_M"],M)
    equal("saddle",temp["saddle_f_second_derivative"],saddle)
    equal("reach",temp["infinite_complete_template_reach_lower"],radius)
    equal("support",temp["radial_support_lower"],support)
    assert radius > F(37,400) > goal and support > F(13,20)
    chi = F(1,100)
    gapA = a+(z-B)*Zb/Lhi-chi*(2*H1+z+B)
    gapC = 2*z*(Zb/Lhi-chi)
    cap_support = (2*H0*H0+z*Zb)/Lhi+a-(H1+z)*chi
    cap = collar["fixed_small_caps"]
    equal("cap A gap",cap["all_phase_support_gap_over_active_envelope"],gapA)
    equal("cap C gap",cap["all_phase_support_gap_over_opposite_cap"],gapC)
    equal("cap support",cap["radial_support_lower"],cap_support)
    assert min(gapA,gapC) > F(7,100) and cap_support > 1
    host = (13*h0-H1-a)/14
    equal("host",collar["fixed_flat_annuli"]["common_envelope_host_slab_disk_radius_lower"],host)
    assert host > F(1,2)
    dist = [z-a-b-ell,h0-F(41,100),H0-a-F(41,100),F(1,5),2*z-2*a]
    assert min(radius,a,min(dist)/2) == F(37,400)

    # Independently reconstruct the exact rational rotation and its ray bounds.
    t=F(1,200)
    ce,se=(1-t*t)/(1+t*t),2*t/(1+t*t)
    assert ce*ce+se*se == 1 and 2*(1-ce) < chi*chi
    Xlo=H0+a*(2*H0*ce-Zb*se)/Lhi
    Xhi=H1+a*(2*H1*ce-Zb*se)/Llo
    Zlo=z+a*(Zb*ce+2*H0*se)/Lhi
    Zhi=z+a*(Zb*ce+2*H1*se)/Llo
    Rlo,Rhi=F(1,10)*Xlo/Zhi,F(1,10)*Xhi/Zlo
    assert Zlo > F(1,10) and F(39,100)<Rlo<Rhi<F(41,100)
    old = radial["old_fixed_annulus"]
    equal("ray lower/upper",old["same_ray_intersection_radius_interval"],[Rlo,Rhi])
    slopeA=F(3,200)/h0
    slopeLo=(z+a*(Zb/Lhi-chi))/(H1+a)
    slopeHi=(z+a*(Zb/Llo+chi))/(H0+a*(2*H0/Lhi-chi))
    assert 0 < slopeA < slopeLo <= slopeHi < F(1,4) < F(5,18)
    new=radial["alternative_fixed_annuli"]
    equal("cap slopes",new["upper_cap_vertical_over_horizontal_interval"],[slopeLo,slopeHi])
    equal("annulus slopes",new["upper_annulus_vertical_over_horizontal_interval"],[F(5,18),F(5,17)])
    new_dist=[z-a-b-ell,h0-F(9,25),H0-a-F(9,25),F(1,5),2*z-2*a]
    assert min(new_dist)/2 == F(37,400) > goal
    equal("new retained pair",new["retained_pair_radius_still"],F(37,400))
    replays=[]
    for author,own in [(collar_path,"notes/"+PREFIX+"tail-positive-collar-budget-replay.json"),
                       (radial_path,"notes/"+PREFIX+"tail-positive-collar-radial-replay.json")]:
        assert (TOPIC/author).read_bytes() == (TOPIC/own).read_bytes()
        replays.append(identity(own))
    result={
        "status":"PASS_INDEPENDENT_EXACT_LOCAL_COLLAR_AND_RADIAL_AUDIT",
        "script":identity("scripts/db6f-tail-review-positive-collar.py"),
        "sources":sources,"author_publication_counts":publication_counts,
        "additional_frozen_input_count":len(ledger["inputs"]),
        "independent_bisection_rounds_per_root":180,"root_endpoints_checked":len(sqrt_specs),
        "exact_formula_comparisons":comparisons,
        "safe_scalar_values":{"complete_noncompact_template_reach":radius,
                              "retained_pair_radius_only":F(37,400),
                              "rigid_conditional_lower":rigid,"held_conditional_lower":held,
                              "old_annulus_duplicate_ray_radius":[Rlo,Rhi],
                              "new_cap_slope_upper":slopeHi},
        "author_replays_byte_identical":replays,
        "does_not_certify_global_R10_feasibility_for_c035":True,
        "retained_pair_bounds_are_not_complete_surface_reach":True,
        "common_metric_and_closed_connectors_unconstructed":True,
        "current_M15_data_read":False,"solver_calls":0}
    with out.open("x") as stream:
        json.dump(encode(result),stream,ensure_ascii=False,indent=2)
        stream.write("\n")
    print(json.dumps({"status":result["status"],"author_files":sum(publication_counts),
                      "source_checks":len(sources),"formula_comparisons":len(comparisons),
                      "bytes":out.stat().st_size,"sha256":sha256(out.read_bytes()).hexdigest()}))


if __name__ == "__main__":
    main()
