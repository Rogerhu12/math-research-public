#!/usr/bin/env python3
"""Exact conditional cuff-height/reach obstruction in the twin-cap envelope."""
import argparse,json
from pathlib import Path
from hashlib import sha256
from fractions import Fraction as Q


def q(x):return Q(int(x["numerator"]),int(x["denominator"]))
def enc(x):
    if isinstance(x,Q):return {"numerator":str(x.numerator),"denominator":str(x.denominator)}
    if isinstance(x,dict):return {k:enc(v) for k,v in x.items()}
    return x


def main():
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--out",required=True)
    a=ap.parse_args()
    topic=Path(__file__).resolve().parents[1]
    rel="notes/2026-11-09-db6f-audit-poisson-twin-marker-bounds.json"
    src=topic/rel;raw=src.read_bytes()
    want="9da6b3d013524995a831e5b55fe9d06b017957bbb87fd9b38fe093c7da8207ef"
    assert sha256(raw).hexdigest()==want
    j=json.loads(raw)
    s=j["source_bounds"];p=j["model_parameters"]
    mlo,mhi=q(s["hmin_lower"]),q(s["hmin_upper"]);Hlo=q(s["H_lower"])
    b,z,rad,eps=q(p["core_halfheight"]),q(p["z"]),q(p["marker_radius"]),q(p["epsilon1"])
    Dlo=q(j["witness_and_enclosures"]["D0_after_error_lower"])
    assert (b,z,rad,eps)==(Q(1,100),Q(3,10),Q(1,10),Q(1,200))
    assert 9**2+40**2==41**2
    cap_dominance_gap=9*(mlo+Hlo)+40*(b-z)-41*rad
    Z40=b+Q(9,40)*(mhi-Q(2,5))+Q(41,40)*eps
    rho_required=Q(3,100)*Dlo
    radius_limit=mhi-Q(40,9)*(rho_required-b)+Q(41,9)*eps
    assert cap_dominance_gap>0
    assert Z40<rho_required and radius_limit<Q(2,5)
    result={
      "status":"EXACT_CONDITIONAL_EQUAL_RADIUS_HORIZONTAL_TANGENT_CUFF_OBSTRUCTION",
      "script_sha256":sha256(Path(__file__).read_bytes()).hexdigest(),
      "source":{"path":rel,"bytes":len(raw),"sha256":want},
      "unit_support_direction":{"x":Q(9,41),"z_abs":Q(40,41)},
      "core_minus_all_marker_support_gap_times_41_lower":cap_dominance_gap,
      "actual_initial_diameter_lower_from_required_point_pair":Dlo,
      "reach_required_from_actual_diameter_lower":rho_required,
      "cuff_height_abs_upper_when_radius_is_two_fifths":Z40,
      "necessary_common_cuff_radius_upper":radius_limit,
      "strict_common_cuff_radius_ge_two_fifths_obstruction":True,
      "hypotheses":"Both complete circles have the same radius about the z-axis, distinct heights, and horizontal surface tangent planes; the halfphase complete image satisfies the frozen one-sided envelope and the initial point-pair condition.",
      "not_a_statement_about_R29_tail_cut_c_or_current_M15":True,
      "solver_backend_or_optimization_calls":0
    }
    out=Path(a.out).resolve()
    with out.open("x") as f:json.dump(enc(result),f,ensure_ascii=False,indent=2);f.write("\n")
    print(json.dumps({"status":result["status"],"strict_radius_ge_0_4_rejection":True,
      "bytes":out.stat().st_size,"sha256":sha256(out.read_bytes()).hexdigest()}))


if __name__=="__main__":main()
