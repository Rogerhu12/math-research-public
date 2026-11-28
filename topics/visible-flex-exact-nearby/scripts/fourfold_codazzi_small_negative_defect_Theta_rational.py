"""Exact rational comparisons for the proved zero-root negative defect component."""
import hashlib
import json
import re
from fractions import Fraction as Q
from pathlib import Path


INPUTS = {
    'PA': ('notes/strict_nu_amplitude_border_ci/run-45906257068-1/actual-strict-nu-amplitude-border.json', 8966,
        '04d09519aeeaaf7d63d1efcc6ee38481a3cdbf25dfaa9868dd8558ecd4e35387'),
    'NP': ('notes/strict_nu_particular_ci/run-45893562391-1/actual-strict-nu-particular.json', 34252,
        '76f00af5bac4a3c64c414844fe31878bb188af9553bb824b92c0071674fd8e2a'),
    'BFP': ('notes/full_target_nu_forward_ci/run-46118996598-1/actual-full-target-nu-forward.json', 40099,
        '5ab3a6ed22e4f40b47777f0bdbdfef50f5e52f50f211ef889ebb3ecc406dac16'),
    'UACT': ('notes/unit_disk_operator_Theta_low_square_ci/run-45933303391-1/actual-unit-disk-operator-Theta-low-square.json', 42477,
        '17c721993bb6488ec48918c50caf70c84785ca54cb004fbc51d11de1c6eb14bc'),
    'NW': ('notes/negative_nu_waist_ci/run-45781137624-1/actual-negative-nu-waist.json', 15210,
        '1a06d01060a63eac98aeaa330f130a8ee766ab5ac878634e637f9cea30e1cb70'),
    'NHT': ('results/R149-supplement-selected-complete-high-Newton-and-nu-from-the-Z-tail.md', 8003,
        '6b4202ede35ed025bb52cd5abcb5a60089353436866a6e32dfac54f0ee5140d9'),
    'NRO': ('results/R149-supplement-ordinary-negative-response-from-the-strong-positive-root.md', 8294,
        'fb1e034f04c79c4a893cdd1407b7a590959f5383dddb1ea786abb34366dfa91d'),
    'ASQ18': ('results/R149-supplement-actual-signed-Theta-trial-and-finite-inverse-by-primitive-residual.md', 7319,
        '82d2beb80d2023c0747c6c0927f0c98dd3fcebcb9376333496e05e55b38ce0f4'),
    'ASQ12': ('results/R149-supplement-all-positive-i-safe-modes-in-the-physical-waist-square.md', 10003,
        '600d29ecbd9fdc0ee1271280edb0e7e3d53def8a5d021127246c9debaa434876'),
    'ASQ10': ('results/R149-supplement-practical-high-cut-with-paid-coordinate-errors.md', 12500,
        'd38cda8483ac691f69bb4c77f809fa072a6b0640cf35d6ffb7e580d39954b641'),
    'ASQ8': ('results/R149-supplement-selected-physical-phase-fibre-summable-analytic-iteration.md', 10863,
        '334bbee162d0e3de0f7d3f88f0de8dad8c9474d432b1d6b5657501c2e167764a'),
    'W': ('results/R133-supplement-actual-physical-Wiener-conjugacy-strip.md', 6138,
        '1e8d001a5878da2894b4c9ab88baf00555ca8364b23f49df8c827c23a7da88c3'),
    'WEA': ('results/R133-supplement-actual-paid-waist-strong-error-assembly.md', 18914,
        'c85797c5aefdf2bec6e0c5bca74e972d01c68245cd1a193c7e3b7c867a1b696b'),
    'BNC': ('results/R147-supplement-target-normalized-strict-parameter-column.md', 11301,
        'dbeeb26b45cb3e14c5edd7526907af4ac55b4207c44987502a16bbf718d1a7ae'),
    'ASQ22': ('results/R149-supplement-small-true-Theta-reception-of-the-negative-parameter-defect.md', 8278,
        '6a3568c62ba7bfff45d2a5509f2721d7581c312602d47afc47f7ab3825f218ee'),
}


def require(ok, message):
    if not ok:
        raise ValueError(message)


def interval(record):
    match = re.fullmatch(r"\[([^ ]+) \+/- ([^\]]+)\]", record["ball"])
    require(match is not None, "the entire original signed or upper decimal ball")
    middle, width = map(Q, match.groups())
    require(width >= 0, "outward original radius")
    return middle-width, middle+width


def main():
    topic = Path(__file__).resolve().parent.parent
    data = {}
    for name,(relative,size,digest) in INPUTS.items():
        raw = (topic/relative).read_bytes()
        require(len(raw)==size and hashlib.sha256(raw).hexdigest()==digest, "whole input "+name)
        if relative.endswith(".json"):
            obj=json.loads(raw)
            require(obj["complete"] is obj["proved"] is True and obj["actual_returncode"]==0
                    and obj["failure"] is None and obj["saved_record_count"]==len(obj["completed_targets"])>0
                    and set(obj["completed_targets"])==set(obj["new_records"]), "actual completed "+name)
            data[name]=obj
    def upper(name, key):
        return interval(data[name]["new_records"][key])[1]
    U,C,W,c,R=Q("8.22"),Q("6.531704"),Q("7.269"),Q(2333968743003,10**13),Q(1,200)
    F,H=Q(".000001307204"),Q(".000000001254870")
    pa=data["PA"]["new_amplitude_input_receipts"]
    amin,amax=interval(pa["whole_waist_a"])
    klo,khi=interval(pa["whole_waist_K"])
    mlo,mhi=interval(data["NP"]["new_records"]["complete_signed_strict_nu_waist_column"]["whole_selected_waist_mean_enclosure"])
    ng=(amax/(-mhi))**2
    checks={}
    def test(name, ok):
        require(ok,name)
        checks[name]=True
    test("whole_source_NW",upper("NW","selected_negative_source_from_same_fixed_window_upper")<F)
    test("negative_ordinary_endpoint_gain",U**2*(c+C**2*R*W**2)<Q("27.882")**2)
    test("root_high_endpoint_gain",(U*C)**2*R<Q("3.797")**2)
    test("full_raw_endpoint",Q("27.882")*F+Q("3.797")*H<Q(".0000365"))
    test("waist_signs",0<amin<amax and klo<khi<0 and mlo<mhi<0)
    test("nonmean_waist_factor",ng**4 < Q(".737")**4*4*(-khi))
    test("each_independent_mean",ng**4*(-klo) < 4*Q(".681")**4)
    test("true_B_inverse",upper("BFP","complete_forward_nu_true_B_inverse_L2_upper")<Q("1.334"))
    test("full_original_Frobenius",upper("BFP","complete_original_Theta_trial_Frobenius_upper")<Q("10.124"))
    test("original_low_inverse_Frobenius",upper("UACT","trial_inverse_complete_Frobenius_candidate")<Q("9.857"))
    test("original_low_residual_operator",upper("UACT","trial_residual_complete_Schur_two_candidate")<Q("1e-15"))
    low=96*(1-Q("1e-15"))/Q("9.857")
    test("orthogonal_high_input",Q("10.124")**2-low**2<(Q("3.04")-Q(".26"))**2)
    test("low_true_operator",Q("1.11")*(1+Q("1.43")/4)<Q("1.51"))
    test("whole_true_operator",Q("1.51")**2+Q("3.04")**2<Q("3.395")**2)
    test("inverse_phase_first_derivative",1/Q(".983")<Q("1.018") and Q("1.017")<Q("1.01")**2)
    # e > 8/3 from its positive series.
    test("inverse_phase_second_derivative",Q(".017")*128*Q(3,8)<Q(".82")
         and Q(".017")*128/Q("2.7")<Q(".81") and Q(".81")/Q(".983")**3<Q(".854")
         and sum((Q(1,1), Q(1,1), Q(1,2), Q(1,6), Q(1,24)))>Q("2.7"))
    test("physical_to_target",Q(".737")*Q("1.01601")*Q("1.334")/4<Q(".251"))
    test("high_pushforward",Q("1.018")**3<Q("1.028")**2
         and Q(".737")*(Q(".854")*Q("1.01")/4+Q("1.028"))/388<Q(".00238"))
    test("true_high_target",Q("1.414")**2<2 and Q(".00238")+Q(".251")*(
        Q("2.51")/196+(Q(".491")+Q(".008"))/8+Q(".06524")*Q(".322")/Q("1.414"))<Q(".025"))
    endpoint=Q(".0000365")
    test("full_target_gate",Q(".251")*endpoint<Q(".00000917"))
    test("full_high_target_gate",Q(".025")*endpoint<Q(".000000913"))
    test("whole_true_Theta_gate",(Q("1.51")*Q(".251")+Q("3.04")*Q(".025"))*endpoint<Q(".0000167"))
    test("whole_true_recovery_gate",(Q(".251")+Q("2.694")*Q("3.04")*Q(".025"))*endpoint<Q(".0000167"))
    test("two_independent_mean_gates",Q(".681")*endpoint<Q(".000025"))
    print(json.dumps({"whole_inputs":len(INPUTS),"exact_comparisons":checks,"old_numerical_targets_called":0,
                      "new_arrays":0,"complete_physical_root_or_Schur_proved":False},sort_keys=True))


if __name__ == "__main__":
    main()
