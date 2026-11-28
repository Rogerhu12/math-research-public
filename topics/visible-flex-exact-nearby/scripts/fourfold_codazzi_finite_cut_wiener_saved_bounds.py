"""Nineteen new exact-rational FWT consequences; no old target is evaluated.

The original whole cut and NG scientific objects are read only for their
unchanged byte identities. This script does not reconstruct any old coefficient,
select a new geometry, form a cut state or assign unknown receivers a value.
"""
from __future__ import annotations
import argparse, hashlib, json
from fractions import Fraction as F
from pathlib import Path

TOPIC="topics/visible-flex-exact-nearby"
INPUTS=[
    (TOPIC+"/notes/selected_cut_shape_mean_ci/run-43715426316-1-selected-cut-shape-mean/actual-cut-shape-mean-conclusion.json",
     "5d74a0f24afe7d490cd17f04f0c0ea5efb671fd277ced502269f4d94c748a413"),
    (TOPIC+"/notes/adaptive_collar_geometry_ci/run-43736004806-1-adaptive-collar-geometry/actual-adaptive-collar-geometry.json",
     "3730af35411d29fee3b55f2dee86a93378b7a81dcd3340e5d39e80614a4738f5")]


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repo",type=Path,default=Path("."));parser.add_argument("--output",type=Path,required=True)
    args=parser.parse_args();root=args.repo.resolve();receipts=[]
    if args.output.exists():
        raise ValueError("retain the first genuine whole FWT consequence output; do not replay")
    for path,digest in INPUTS:
        raw=(root/path).read_bytes();actual=hashlib.sha256(raw).hexdigest()
        if actual!=digest:
            raise ValueError("whole original saved object identity: "+path)
        json.loads(raw)
        receipts.append({"path":path,"bytes":len(raw),"sha256":actual,
                         "scientific_targets_called":0})
    d=F(1,10**10);eps=F(1,10**11);ds=F(9368259853002,10**23)
    A=F("1.012e-11");Bs=F("1.74e-11");Bu=F("1.08e-11")
    r0=F(20,63);E=F(13,200)*d+4*eps;rows=[]
    def compare(name,left,right,relation="<"):
        passed=left<right if relation=="<" else left>right
        rows.append({"name":name,"left_exact":str(left),"relation":relation,
                     "right_exact":str(right),"passed":passed})
    compare("complete_both_signed_frequency_Wiener_lift37",1+F(40960,31),37**2)
    compare("mean_aware_finite_j_difference13",F(8,25)*(37+F(507,500)),13)
    compare("same_finite_reference_mean_lower",F(16,5)-eps,F(25,8),">")
    compare("same_finite_reference_j_shape",F(7,500)+13*eps,F(1,64))
    compare("whole_inverse_angle_self_map",F(7,2000)+F(13,4)*eps,F(15,4096))
    compare("whole_finite_reference_reciprocal",r0/(1-r0*37*eps),F(159,500))
    compare("known_selected_real_j_derivative",F(".054056879")+d*F(5,16)*F("2.456636503"),F(".054057"))
    compare("known_selected_strip_j_derivative",F(5,3)*F(".054057")+F(5,16)*13*d,F(91,1000))
    compare("known_selected_complete_reciprocal_derivative",F(5,16)*F(64,63)**2*F(91,1000),F(3,100))
    coefficient=37*F(20,63)*F(159,500)+F(3,100)*F(208,63)
    if coefficient!=F(671,175):
        raise ValueError("the exact complete finite curvature coefficient")
    compare("complete_finite_physical_curvature_coefficient4",coefficient,4)
    compare("same_finite_reference_real_j_derivative",F(".054057")+384*13*eps,F(1,16))
    compare("same_finite_reference_physical_first_derivative",F(".020269146")+4096*E,F(1,48))
    compare("same_finite_reference_physical_second_derivative",24*F(".020269146")+2*4096**2*E,F(1,2))
    compare("selected_NG_gate_implies_finite_domain",Bs/64,eps)
    compare("selected_NG_gate_implies_real_high_domain",A+Bs,F(1,2**10))
    compare("selected_complete_NG_physical_low_entry",F(13,200)*ds+(A+Bs)/16,F(1,10**9*128))
    compare("uniform_complete_NG_physical_low_entry",F(13,200)*d+(A+Bu)/16,F(1,10**9*128))
    compare("selected_zero_shell_cut_allowance_over_eleven_old",Bs/64,11*F("9.5e-12")/385,">")
    compare("selected_gate_retains_original_real_low_neighbourhood",4*ds+385*Bs/64+A+Bs,F(1,10**9))
    if len(rows)!=19:
        raise ValueError("all nineteen new comparisons required")
    result={"kind":"R133_new_FWT_complete_saved_rational_consequences_v1",
        "complete":True,"proved":all(x["passed"] for x in rows),"complete_new_comparison_count":19,
        "source_sha256":hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        "whole_original_input_receipts":receipts,"complete_new_comparisons":rows,
        "same_original_selected_member":True,"both_means_and_reflection_angle_retained":True,
        "finite_high_H8193_requirement_unchanged":True,"whole_two_sided_collar_domain_required":True,
        "unknown_low_or_shell_receivers_assigned_values":False,"original_scientific_targets_recomputed":0,
        "old_upper_subtraction_or_coefficient_reconstruction":False,"full_core_or_topic_completion_proved":False}
    args.output.parent.mkdir(parents=True,exist_ok=True)
    raw=(json.dumps(result,sort_keys=True,separators=(",",":"))+"\n").encode()
    args.output.write_bytes(raw)
    if args.output.read_bytes()!=raw or not result["proved"]:
        raise ValueError("whole new consequence readback or gate failed")
    print(json.dumps({"proved":result["proved"],"new_comparisons":19,"bytes":len(raw),
                      "sha256":hashlib.sha256(raw).hexdigest(),"old_scientific_targets":0},sort_keys=True))


if __name__=="__main__":
    main()
