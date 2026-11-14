#!/usr/bin/env python3
"""Fixed cylindrical-cuff local geometry and necessary two-point support gates.

Only frozen Poisson intervals and Fraction arithmetic; no nonlinear solve.
"""
import argparse
from fractions import Fraction as Q
from hashlib import sha256
import json
from pathlib import Path


def q(v):
    assert set(v) == {"numerator", "denominator"}
    return Q(int(v["numerator"]), int(v["denominator"]))


def enc(v):
    if isinstance(v, Q):
        return {"numerator": str(v.numerator), "denominator": str(v.denominator)}
    if isinstance(v, dict):
        return {k: enc(w) for k,w in v.items()}
    if isinstance(v, list):
        return [enc(w) for w in v]
    return v


def main():
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--out",required=True)
    args=ap.parse_args()
    base=Path(__file__).resolve().parents[1]
    specs={
      "notes/2026-11-09-db6f-audit-poisson-twin-marker-bounds.json":
        "9da6b3d013524995a831e5b55fe9d06b017957bbb87fd9b38fe093c7da8207ef",
      "notes/2026-11-09-db6f-audit-positive-collar-budget.json":
        "bbb8619ae88826d9a0c69a7f7ffbbf554eb4a38d560f77ed1f12939094a59f63"
    }
    inputs=[]
    for rel,want in specs.items():
        raw=(base/rel).read_bytes()
        assert sha256(raw).hexdigest()==want
        inputs.append({"path":rel,"bytes":len(raw),"sha256":want})
    old=json.loads((base/next(iter(specs))).read_text())
    budget=json.loads((base/list(specs)[1]).read_text())
    s=old["source_bounds"];w=old["witness_and_enclosures"]
    Hlo,Hhi=q(s["H_lower"]),q(s["H_upper"])
    Llo,Lhi=q(w["L0_lower"]),q(w["L0_upper"])
    m0lo=q(s["hmin_lower"])
    c=Q(1,10); zc=Q(1,10); eta=Q(1,1000)
    a=Q(1,10); zstar=Q(3,10); chi=Q(1,100)
    goal=Q(189,2500)
    hlo,hhi=zc-eta,zc+eta
    host=q(budget["fixed_flat_annuli"]["common_envelope_host_slab_disk_radius_lower"])
    assert c<Q(1,2)<host
    assert Q(95,1000)<hlo<hhi<Q(105,1000)
    assert c>goal
    Xlo,Xhi=Hlo+Hlo/(5*Lhi),Hhi+Hhi/(5*Llo)
    Zlo,Zhi=zstar+Q(31,1000)/Lhi,zstar+Q(31,1000)/Llo
    Rlo,Rhi=Xlo-a*chi,Xhi+a*chi
    Vlo,Vhi=Zlo-a*chi,Zhi+a*chi
    assert Rlo>c and Vlo>hhi>0
    cm=hlo*Rlo-c*Vhi
    cp=hlo*Rlo+c*Vlo
    assert cm>0
    same_minus=cm*cm/((Rhi-c)**2+(Vhi-hlo)**2)
    same_plus=cp*cp/((Rhi+c)**2+(Vhi-hlo)**2)
    opposite_minus=cp*cp/((Rhi-c)**2+(Vhi+hhi)**2)
    reverse_ray_dot=Rlo*Rlo+Vlo*Vlo-c*Rhi-hhi*Vhi
    assert min(same_minus,same_plus)>Q(79,1000)**2>goal*goal
    assert opposite_minus>c*c>goal*goal
    assert reverse_ray_dot>0
    active_error=Q(1,1_000_000)
    active_height=Q(3,200)+active_error
    active_radius=m0lo-active_error
    assert hlo>active_height and hlo>goal
    assert active_radius>c and active_radius>goal
    distances={
      "active_to_caps":zstar-a-active_height,
      "active_to_cylinders":active_radius-c,
      "cylinders_to_caps":Hlo-a-c,
      "opposite_cylinders":2*hlo,
      "opposite_caps":2*zstar-2*a,
    }
    assert min(distances.values())>2*Q(9,100)
    result={
      "status":"EXACT_LOCAL_CYLINDRICAL_CUFF_AND_NECESSARY_KERNEL_GATES",
      "script_sha256":sha256(Path(__file__).read_bytes()).hexdigest(),
      "inputs":inputs,
      "cylindrical_cuffs":{
        "radius":c,"center_height_absolute":zc,"halfheight":eta,
        "slab_height_lower":hlo,"slab_height_upper":hhi,
        "infinite_cylinder_reach":c,"radial_support":c,
        "coordinate_second_fundamental_form_at_cuff":{"L":Q(0),"M":Q(0),"N_inward":c},
        "common_host_radius_lower":host
      },
      "small_upper_cap_bounds":{
        "horizontal_radius_lower":Rlo,"horizontal_radius_upper":Rhi,
        "height_lower":Vlo,"height_upper":Vhi
      },
      "necessary_two_point_kernel_tests":{
        "same_side_line_distance_squared_lower_at_cos_minus_one":same_minus,
        "same_side_line_distance_squared_lower_at_cos_plus_one":same_plus,
        "same_side_all_lines_distance_strictly_above":Q(79,1000),
        "opposite_side_relevant_endpoint_line_distance_squared_lower":opposite_minus,
        "opposite_side_backward_rays_norm_lower":c,
        "cap_based_backward_ray_dot_lower":reverse_ray_dot,
        "active_to_cylinder_cylinder_based_center_height_lower":hlo,
        "active_to_cylinder_active_based_center_horizontal_norm_lower":active_radius,
        "two_cylinder_points_center_horizontal_norm_lower":c,
        "these_tests_are_necessary_not_sufficient_for_global_support":True,
        "all_other_retained_pair_kernel_tests_claimed":False
      },
      "retained_piece_geometry":{
        "cross_piece_distance_lower_bounds":distances,
        "using_only_existential_CK_width_and_C0_conditions":True,
        "combined_point_pair_radius_if_CK_local_lemma_accepted":Q(9,100),
        "global_support_or_closed_reach_claimed":False
      },
      "reach_goal":goal,
      "all_exact_scalar_gates_passed":True,
      "closed_surface_or_common_metric_connection_constructed":False,
      "current_M15_candidate_read":False,
      "solver_root_RK_or_geometry_backend_calls":0
    }
    out=Path(args.out).resolve()
    with out.open("x") as f:
        json.dump(enc(result),f,ensure_ascii=False,indent=2);f.write("\n")
    print(json.dumps({"status":result["status"],
       "same_side_line_squared_lower_approx":float(min(same_minus,same_plus)),
       "opposite_relevant_line_squared_lower_approx":float(opposite_minus),
       "goal_squared":float(goal*goal),
       "report_bytes":out.stat().st_size,"sha256":sha256(out.read_bytes()).hexdigest()}))


if __name__=="__main__":
    main()
