#!/usr/bin/env python3
"""Pure Fraction support-cone facts for the frozen Poisson twin-cap envelope."""
import argparse
from pathlib import Path
from fractions import Fraction as Q
from hashlib import sha256
import json


def enc(x):
    if isinstance(x,Q):
        return {"numerator":str(x.numerator),"denominator":str(x.denominator)}
    if isinstance(x,dict):
        return {k:enc(v) for k,v in x.items()}
    if isinstance(x,list):
        return [enc(v) for v in x]
    return x


def q(x):
    return Q(int(x["numerator"]),int(x["denominator"]))


def main():
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--out",required=True)
    args=ap.parse_args()
    topic=Path(__file__).resolve().parents[1]
    specs={
      "notes/2026-11-09-db6f-audit-poisson-twin-marker-bounds.json":
        "9da6b3d013524995a831e5b55fe9d06b017957bbb87fd9b38fe093c7da8207ef",
      "notes/2026-11-09-db6f-audit-poisson-twin-marker-model-v2.md":
        "ca1033e52cab08f2258bd0ef52b0ba7140a6f73193088d56b4065d5881064149",
      "results/R27-poisson-c3-core-and-conditional-held-transfer.md":
        "dd8ddca61e9609f1e0899692015938ff351d61bb9e8e9936d6ba4b236c11849a",
      "results/R29-c3-mechanism-interface-and-convex-held-envelope.md":
        "a4274cb2f6a931b59c7af94945d91eb1e74610fe6d511bfbadae8ae131ab82c1"
    }
    bindings=[]
    for rel,want in specs.items():
        data=(topic/rel).read_bytes()
        assert sha256(data).hexdigest()==want
        bindings.append({"path":rel,"bytes":len(data),"sha256":want})
    j=json.loads((topic/"notes/2026-11-09-db6f-audit-poisson-twin-marker-bounds.json").read_text())
    Hlo=q(j["source_bounds"]["H_lower"]);Hhi=q(j["source_bounds"]["H_upper"])
    z=q(j["model_parameters"]["z"]);b=q(j["model_parameters"]["core_halfheight"])
    a=q(j["model_parameters"]["marker_radius"]);Dstar=q(j["model_parameters"]["Dstar"])
    Lhi=q(j["witness_and_enclosures"]["L0_upper"])
    assert (z,b,a,Dstar)==(Q(3,10),Q(1,100),Q(1,10),Q(251,100))
    RA,RC=Q(6,5),Q(4,3)
    assert Hhi*Hhi+b*b<RA*RA
    assert Hhi*Hhi+z*z<(RC-a)**2
    assert Hlo>1 and Lhi<Q(5,2)
    chi=Q(1,100)
    vzlo=Q(31,250)
    assert vzlo==(z+b)/Q(5,2)
    v_gap_a=a+(z-b)*vzlo-(RA+RC)*chi
    v_gap_c=2*z*(vzlo-chi)
    v_cap_member=1-chi
    assert (v_gap_a,v_gap_c)==(Q(8297,75000),Q(171,2500))
    nx,nz=Q(-24,25),Q(7,25)
    assert nx*nx+nz*nz==1
    n_gap_a=a+(z-b)*nz-(RA+RC)*chi
    n_gap_c=2*z*(nz-chi)
    n_cap_member=Q(96,125)-chi
    assert (n_gap_a,n_gap_c)==(Q(1169,7500),Q(81,500))
    assert Q(96,125)==Q(48,25)/Q(5,2)
    assert min(v_gap_a,v_gap_c,n_gap_a,n_gap_c)>0
    assert min(v_cap_member,n_cap_member)>Q(1,2)
    fixed_span=2*(z+a*nz)
    assert fixed_span==Q(82,125)>Dstar/5
    r=Q(1,10);qq=Q(99,100)
    rho_max=r+(1-r)*(1+qq)/(1-qq)
    assert rho_max==Q(896,5)
    kappa_min=1/rho_max
    assert kappa_min==Q(5,896)
    result={
      "status":"EXACT_FIXED_SPHERICAL_PATCH_SUPPORT_CONES_ONLY",
      "script_sha256":sha256(Path(__file__).read_bytes()).hexdigest(),
      "sources":bindings,
      "normal_cone_chord_radius":chi,
      "ambient_origin_radius_bounds":{"active_band":RA,"each_marker_ball":RC},
      "axis_cones":{"v_z_lower":vzlo,"support_margin_over_active":v_gap_a,
          "support_margin_over_other_marker":v_gap_c,
          "sphere_point_cap_membership_dot_lower":v_cap_member},
      "rational_cones":{"normal_x":nx,"normal_z_abs":nz,
          "support_margin_over_active":n_gap_a,
          "support_margin_over_other_marker":n_gap_c,
          "sphere_point_cap_membership_dot_lower":n_cap_member,
          "fixed_point_pair_span":fixed_span,
          "fixed_span_over_Dstar":fixed_span/Dstar},
      "Poisson_initial_angular_curve":{"rho_max":rho_max,"kappa_min":kappa_min,
        "homothetic_branch_speed_condition_only":"abs(a_prime)<5/896; not a global obstruction for evolving sections"},
      "solver_RK_integration_optimization_calls":0,
      "current_candidate_data_read":False,
      "whole_closed_family_or_common_metric_proved":False
    }
    out=Path(args.out).resolve()
    with out.open("x") as f:
        json.dump(enc(result),f,ensure_ascii=False,indent=2);f.write("\n")
    print(json.dumps({"status":result["status"],"all_four_support_margins_positive":True,
       "fixed_pair_span":"82/125","bytes":out.stat().st_size,
       "sha256":sha256(out.read_bytes()).hexdigest()}))


if __name__=="__main__":
    main()
