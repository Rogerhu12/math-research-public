"""Exact arithmetic reception of the complete SP, GLW and GIC scalar bounds at the true cut."""
from fractions import Fraction as Q
from hashlib import sha256
from math import factorial
from pathlib import Path
import json

PINS={
 "notes/primitive_mean_strict_propagation_ci/run-43731464771-1/execution.json":"a3a02969178e5e8b3b040fafd51d08b25d75b3f3922f2ae2e9ee0d4a8ab18a12",
 "notes/genuine_collar_laurent_ci/run-46146513475-1/whole-scientific-conclusion.json":"034c7d25da0149f16dd5270d4daf1a3a11c052976b2bc2e3427fdddf851ea260",
 "notes/genuine_infinite_local_collar_ci/run-46144088993-1/whole-scientific-conclusion.json":"d4be3220759ccfffa9dbe8f4d44d9dc51d74ebfbb18fb053884897b3b288fdd3",
 "results/R149-supplement-small-true-Theta-reception-of-the-negative-parameter-defect.md":"6a3568c62ba7bfff45d2a5509f2721d7581c312602d47afc47f7ab3825f218ee",
 "results/R149-supplement-ordinary-negative-response-from-the-strong-positive-root.md":"fb1e034f04c79c4a893cdd1407b7a590959f5383dddb1ea786abb34366dfa91d",
 "results/R133-supplement-actual-piecewise-root-radius-one-over-fifty-and-full-seams.md":"cd8c28e0213facba6309ae2478259c2617928f4609ff6668429acdc49c91089f"}


def ends(r):
    ls=r["ball"].strip("[]").split(" +/- ")
    x=Q(ls[0]);d=Q(ls[1]) if len(ls)==2 else Q(0)
    return x-d,x+d


def main():
    root=Path(__file__).resolve().parent.parent
    inputs={}
    for path,h in PINS.items():
        b=(root/path).read_bytes()
        if sha256(b).hexdigest()!=h:
            raise ValueError("entire original "+path)
        if path.endswith(".json"):
            inputs[path]=json.loads(b,parse_float=lambda v:Q.from_float(float(v)))
    sp,glw,gic=inputs.values()
    s=sp["actual_scientific_receipt"]
    comp=s["complete_strict_propagation_conclusion"]
    end=s["complete_endpoint_readout_conclusion"]
    w,c=end["waist_complete_radial_factors"],end["cut_complete_radial_factors"]
    bound=[[Q("1.461990"),Q(".275255")],[Q("1.055655"),Q("1.163902")]]
    x=Q(".847")
    ex=sum(x**k/factorial(k) for k in range(13))+x**13/factorial(13)/(1-x/14)
    reverse=ex*ends(w["q_upper"])[1]/ends(c["q_lower"])[0]
    pre=Q(".719")*Q("1.041")*reverse*Q("1.488")*Q("11.272695")
    weak=pre*Q("1.978737")
    length=Q(gic["physical_root_interval"][1])-Q(gic["cut"])
    nat2=(weak*Q(".091848"))**2*length
    right2=(Q("10.611")*Q("1.061")/Q("1.1"))**2*(Q(".097")**2+Q(".022")**2)
    checks={
        "strict_original_true":sp["complete"] and s["proved"] and s["actual_returncode"]==0 and
            all(g["passed"] is True for g in s["gates"]) and comp["exact_interval"]==["0","2333968743003/10000000000000"],
        "two_original_terminal_sources":all(v["complete"] and v["proved"] and v["completed_subpieces"]==n and v["run"]==run
                  for v,n,run in ((glw,656,"46146513475"),(gic,4,"46144088993"))),
        "positive_variation":ends(comp["new_complete_forward_log_upper"])[1]<Q(".846949")<x,
        "true_q_ends":ends(w["q_upper"])[1]<Q(".92510") and ends(c["q_lower"])[0]>Q(".66812") and ends(c["q_upper"])[1]<1,
        "exponential_on_actual_cut":ex<Q("2.333") and reverse<Q("3.24"),
        "actual_two_by_two":all(ends(v)[1]<upper for row,L in zip(comp["reverse_nonradial_product"],bound) for v,upper in zip(row,L)),
        "first_row":sum(z*z for z in bound[0])<Q("1.488")**2,
        "joint_row":sum(z*z for row in bound for z in row)<Q("2.165")**2,
        "waist_radial":ends(w["density_radial_factor_upper"])[1]**2<Q("1.041")**2*ends(w["q_lower"])[0],
        "instant_mixed":ends(end["saved_primitive_root_and_jump_gain"])[1]<Q("11.272695"),
        "physical":pre<Q("40.72"),
        "joint":Q("1.041")*Q("3.24")*Q("2.165")*Q("11.272695")<Q("82.4"),
        "before_J_weak":weak<Q("80.58"),
        "before_J_strong_high":Q(".00238")*Q("8.22")*Q("6.531704")*Q(".982800")<Q(".126"),
        "GLW_complete":glw["full_completed_slab_integral_L1"][0]<Q("2.936765") and glw["full_completed_slab_integral_L1"][1]<Q("5.623473"),
        "GLW_new_natural_pair":Q("80.58")*Q("2.936765")<237 and Q("80.58")*Q("5.623473")<454,
        "GIC_source":gic["infinite_local_original_density_ordinary_Hminus5over3_upper"]<Q(".091848") and length>0,
        "GIC_natural":nat2<Q(".0146")**2,
        "GIC_common":nat2*Q("12.4")**2<Q(".182")**2,
        "GIC_true_high":nat2*right2<Q(".015")**2}
    if not all(checks.values()):
        raise ValueError({k:v for k,v in checks.items() if not v})
    print(json.dumps(dict(complete=True,input_count=len(PINS),old_targets_called=0,
                          original_runs=[43731464771,46146513475,46144088993],exact_comparisons=checks),
                     separators=(",",":"),sort_keys=True))


if __name__=="__main__":
    main()
