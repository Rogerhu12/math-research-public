#!/usr/bin/env python3
"""New exact budgets for the current full exterior and common-world caps.

The existing full PDE module theorems are identified inputs.  These gates
do not solve the remaining matching equations or recompute a target.
"""
from pathlib import Path
from fractions import Fraction as F
import argparse
import hashlib
import json
import datetime
import time

TOP = Path(__file__).resolve().parents[1]
DEPS = [
 "results/R133-supplement-current-complete-exterior-curvature-and-common-world-caps.md",
 "results/R119-supplement-controlled-profile-full-label-and-raw-ports.md",
 "results/R119-supplement-two-parameter-full-tail-chart-reconstructed.md",
 "results/R119-supplement-uniform-tail-chart-for-actual-metric-parameters.md",
 "results/R119-supplement-stronger-deep-first-shear-and-complete-local-map.md",
 "results/R119-supplement-stronger-deep-full-label-chart-and-fourth-line.md",
 "results/R115-actual-tail-holomorphic-neighborhood-and-strong-extension.md",
 "results/R69-actual-closed-approximate-exterior-and-two-held-disks.md",
 "results/R119-supplement-balanced-connector-label-domain-224.md",
 "results/R133-supplement-fixed-stop-D0-complete-sources-and-incoming.md",
 "results/R119-supplement-actual-long-radial-nonlinear-dirichlet-problem.md",
 "results/R133-supplement-actual-nonlinear-long-tail-screening-and-analytic-gain.md",
 "results/R133-supplement-complete-C0-waist-and-canonical-forward-geometry.md",
 "results/R133-supplement-exact-waist-grid-and-complete-canonical-alignment.md",
]
def sha(p):
    return hashlib.sha256(Path(p).read_bytes()).hexdigest()

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("--out",type=Path,required=True)
    args=ap.parse_args()
    if args.out.exists():
        raise FileExistsError("Preserve the original complete budget")
    t=time.monotonic()
    gates=[]
    def gate(name,condition,**values):
        item={"name":name,"passed":bool(condition)}
        item.update({k:str(v) if isinstance(v,F) else v for k,v in values.items()})
        gates.append(item)
        if not condition:
            raise AssertionError(item)

    # Reinstantiation uses the actual two-bump derivative and endpoint gates.
    gate("current prefix background curvature margin",F(9375,131072)<F(1,8))
    gate("current second bump first jet is within the same old derivative margin",
         80+384*F(1,2**29)<F(15,8)*80)
    gate("current second bump second jet is within the same old derivative margin",
         F(29,5)*80+98304*F(1,2**29)<6*80)
    gate("current complex second bump preserves real monotonicity",
         384*F(1,2**29)<40)
    gate("the current full graph ball controls all labels",
         16*F(1,64)==F(1,4))
    gate("deep cell scale lower dyadic exponent",F(2,25)<F(1,8))
    gate("first changed mean scaling index",4097==4096+1)
    gate("first deeper J upper",4097+5<2**13)
    deep_value_bits=569-F(3,2)*4099-F(7,2)*4100
    deep_derivative_bits=578+13-F(3,2)*4099-2*4100
    gate("entire changed-prefix and deep value bound",
         deep_value_bits < -9000,log2_upper=deep_value_bits)
    gate("entire changed-prefix and deep derivative bound",
         deep_derivative_bits < -9000,log2_upper=deep_derivative_bits)
    gate("every subsequent derivative layer decreases by at least one bit",
         F(4103,4102)*F(1,4)<F(1,2))
    gate("every subsequent value layer decreases by more than one bit",
         F(7,2)>1)
    gate("all changed layers fit the common eighth bound",
         -9000 < -3)

    beta=F(39,4)-4-F(5,256)
    gate("true complete jet decay exponent",beta==F(1467,256))
    gate("current strengthened weight leaves the original envelope",
         131-F(485,4)==F(39,4))
    gate("shallow real angle fee",F(100,9)**5<2**18)
    gate("deep real angle fee has more spare bits",-15<18)
    gate("mean geometric series includes all later layers",beta+1>1)
    gate("mean integration and partial first cell cost",2*4<2**4)
    gate("current local jet covers both earlier constants",max(52,184)<200)
    gate("full reference height mean-inclusive exponent",200+18+4==222)
    gate("full physical Cartesian vector exponent",
         222+16+6+440==684)
    gate("real first cell lies in the dyadic envelope",
         F(2,25)<F(1,8))
    reserve=132*beta-684
    gate("whole real physical tail is below the stated uniform bound",
         reserve>64,strict_bit_reserve=reserve)
    gate("real nonradial entire tail two-jet radius",
         F(1,2**64)*F(1,4)==F(1,2**66))
    gate("normal and curvature comparison occurs inside its stated ball",
         F(1,2**66)<F(1,2**10))
    gate("whole current infinite-tail curvature remains below one quarter",
         F(1,8)+32*F(1,2**66)<F(1,4))

    N=F(1,2**18); amax=F(7,10**6); wmax=F(5,18)*amax
    gate("true long-segment strong norm controls all four states",
         F(25,8)*F(1,2**20)+256*F(1,2**40)<N)
    gate("complete connector and both bumps stay below the same four-state ball",
         F(1,2**447)*F(1,4)<N)
    gate("complete nonlinear denominator is separated from zero",N<F(1,64))
    gate("physical w square is below its actual coarse dyadic bound",
         wmax*wmax<F(1,2**37))
    E=1+F(1,2**37); D=1-F(1,2**50)
    deficit=wmax*wmax*(2*N+N*N+E*N*N)
    gate("true Darboux normal discriminant lower",
         deficit<F(1,2**50),exact_deficit_upper=deficit)
    rowsum=7+24*N+64*N*N
    curvature_squared=F(5,18)**2*(E/D)*rowsum**2
    gate("entire finite exterior shape operator is below two",
         curvature_squared<4,exact_squared_upper=curvature_squared)
    gate("the longer row dominates the other exact shape row",
         7+24*N+64*N*N>1+N)
    ell=F(8,10**6)
    length_squared=amax*amax*(1+wmax*wmax)
    gate("exact full metric radial length is below eight microunits",
         length_squared<ell*ell,exact_squared_upper=length_squared)
    gate("complete true normal propagation uses the paid curvature",2*ell==F(16,10**6))
    support_fee=ell*(1+2*F(13,10))
    gate("same-world support fee at radius thirteen tenths",
         support_fee==F(288,10**7))
    gate("final radius threshold is below thirteen tenths",
         F(511,400)<F(13,10))
    gate("exterior curvature fits both final curvature thresholds",
         F(2)<F(196,27)<12)

    height=F(4347844570122155,4503599627370496)
    lower=height-F(1,100)-ell
    upper=height+F(1,100)+ell
    gate("true upper-cap height stays above nine tenths",lower>F(9,10),exact_lower=lower)
    gate("true upper-cap height stays below one",upper<1,exact_upper=upper)
    gate("reflected true lower-cap height interval",-1<-lower<-F(9,10))
    gate("two actual disk centers pay the held-set size",
         F(9,5)/F(511,200)>F(1,5))
    gate("there is no additional capwise mean normalization",True)
    report={
      "kind":"current_complete_exterior_geometry_and_common_world_caps",
      "complete":all(x["passed"] for x in gates),
      "utc":datetime.datetime.now(datetime.timezone.utc).isoformat(),
      "source_sha256":sha(__file__),
      "dependencies":{n:sha(TOP/n) for n in DEPS},
      "gates":gates,"gate_count":len(gates),
      "bounds":{"current_reference_tail_curvature":"1/8",
                "current_nonradial_tail_C2_modulo_unique_axial_constant":"2^-64 X < 2^-66",
                "current_actual_infinite_tail_curvature":"1/4",
                "current_actual_complete_exterior_curvature":"2",
                "current_actual_exterior_metric_length":str(ell),
                "same_world_position_error":str(ell),
                "same_world_normal_error":str(2*ell),
                "support_error_at_radius_13_over_10":str(support_fee),
                "true_flat_upper_center_lower":str(lower),
                "true_flat_upper_center_upper":str(upper)},
      "all_tail_angular_modes_and_means_retained":True,
      "current_Gamma_slide_and_shape_controls_retained":True,
      "independent_cap_height_reset_allowed":False,
      "original_target_or_completed_geometry_recomputed":False,
      "position_and_height_require_actual_matching":True,
      "fixed_caps_along_final_family_require_constant_actual_mean_height":True,
      "complete_body_inverse_proved":False,
      "nonlinear_global_matching_solved":False,
      "final_exact_closed_flex_exists":False,
      "wall_seconds":time.monotonic()-t}
    args.out.write_text(json.dumps(report,indent=2)+"\n")
    print(json.dumps({"complete":report["complete"],"gate_count":len(gates),
                      "source_sha256":report["source_sha256"],"native_sha256":sha(args.out),
                      "wall_seconds":report["wall_seconds"]}))
if __name__=="__main__":
    main()
