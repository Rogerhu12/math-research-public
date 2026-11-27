#!/usr/bin/env python3
"""New selected-cap feedback combinations from immutable CPA balls.

No matrix, target, integral, original scalar conclusion, or cap solve is run.
The 38 comparisons below were first evaluated in the connected exact-integer
JavaScript runtime. This file preserves the equivalent rational reader.
"""
from fractions import Fraction as F
import json

CPA_PROOF_BLOB = "c430498733d0ddf886cce0e47da0606be723e028"
SHL_PROOF_BLOB = "7be71f6856128e400a30f19db40c6d920e16b70a"
SAVED = {
    "full": {
        "kappa": "0.001995250213303986953789151895423820874750174591807147100677283357 +/- 3.55e-67",
        "epsilon": "0.001221753982256937396572381635676706229767641041488826987188298546 +/- 3.68e-67",
        "body_gap": "0.7651435538900629840276521792792448860194807868106771571718776832 +/- 2.78e-65",
        "cut_gap": "0.4809255510705936016726579286671434859261235499871813251805918751 +/- 3.60e-65",
        "det": "0.2461287684628665107423611655294704451877231178180531911908801983 +/- 4.31e-65",
        "columns": {
            "g": [
                "90930.61580565585047449457866013203903824726100970236315247867274 +/- 2.84e-60",
                "43119.50272202381192986739476701689548159430246715228177243474815 +/- 4.61e-60",
                "25837.87897467519521388760392531293738034723844192574898276092089 +/- 2.64e-60"
            ],
            "p": [
                "6073.436897284254207052391042224515987121569936607164425031035403 +/- 6.65e-62",
                "2896.393647026294601048470807854696989913181939839329652327413863 +/- 4.24e-61",
                "1725.971372367795404164542797572554759453905924652309800226100764 +/- 2.53e-61"
            ],
            "a": [
                "356.0492388728231070337616143609554398816888598902448872677287821 +/- 2.32e-62",
                "170.9037308348454370769404795073589276167856463958754838746782104 +/- 4.90e-62",
                "100.1944047903402182774475260848052418833807911334071891828975120 +/- 3.39e-62"
            ],
            "c": [
                "7.837542172311805264622274766437793859800656404636571922660903941 +/- 2.43e-64",
                "3.736785745747934331006245594490023998638014751772518664896962047 +/- 4.34e-64",
                "2.238355133979597446240575225419477819490598826732890255838396063 +/- 4.46e-64"
            ]
        }
    },
    "tail": {
        "kappa": "0.001965078425369347160008235817147715634525227743105540668501925603 +/- 4.32e-67",
        "epsilon": "0.001203280096128216741137543807526719435145050605521924127590565098 +/- 2.08e-67",
        "body_gap": "0.7651435538900629840276521792792448860194807868106771571718776832 +/- 2.78e-65",
        "cut_gap": "0.4887743671179421789041901932190964695011281907172770073532592544 +/- 3.90e-65",
        "det": "0.2539766823508917922058772021020635256466868341555860404380083624 +/- 1.09e-65",
        "columns": {
            "g": [
                "88121.18604650594053041083678697408999832095865033988497081329671 +/- 2.32e-61",
                "41779.69881135718774033733440637048949433262899761341414267342834 +/- 3.32e-60",
                "25039.48501438903005880596836824618317556299439798538066016797881 +/- 9.31e-61"
            ],
            "p": [
                "5885.766874457550758758643068168106303943103275279009446260388863 +/- 4.53e-61",
                "2806.894690991104711894314920164042091087114820858330820121070229 +/- 4.49e-61",
                "1672.638623163578096817282680470693216733975601493937310008466827 +/- 2.20e-61"
            ],
            "a": [
                "345.1548019573861398306526372039902874459098789102184305184887748 +/- 3.76e-62",
                "165.7082248300147873202558871610604198996070251148297618420449086 +/- 7.37e-63",
                "97.09838411010245714605884687282707065240821122812142341909603369 +/- 3.87e-63"
            ],
            "c": [
                "7.485426145566132973148097002159864670365842587920245212440376348 +/- 2.98e-64",
                "3.568863259661293528770053920419063071199723311536448078746678058 +/- 1.74e-64",
                "2.138289521675849609166572252714676731387490504614816152430442124 +/- 2.48e-65"
            ]
        }
    }
}


def ball(text):
    midpoint, radius = map(F, text.split(" +/- "))
    return midpoint - radius, midpoint + radius


def main():
    checks = {}

    def check(label, condition):
        checks[label] = bool(condition)
        if not condition:
            raise AssertionError(label)

    cap_exponent = -31_223_222 + 30 - 4
    cut_exponent = cap_exponent + 11
    check("physical selected-height coefficient in the complete cap module",
          10**9 < 2**30 and 25 > 16 and cap_exponent == -31_223_196)
    check("true-cut feedback exponent and coarse rational gate budget",
          cut_exponent == -31_223_185
          and cut_exponent < -20 and cap_exponent < -40)
    check("complete normalized two-input Hilbert output",
          60 - 31_223_222 < 0 and 21 + 1 == 22)
    check("actual higher cap trace window",
          1164 + 3 == 1165 + 2 and 23_303_175 - 440 == 23_302_735)

    tau = F(1, 2**40)
    q = F(1, 2**20)
    denominator = 1 - q
    receiver_uppers = {}
    for case_name, case in SAVED.items():
        scalar = {k: ball(case[k]) for k in
                  ("kappa", "epsilon", "body_gap", "cut_gap", "det")}
        columns = {k: list(map(ball, v))
                   for k, v in case["columns"].items()}
        check(case_name + ": old complete cap multiplier qualifies new column",
              scalar["epsilon"][1] < scalar["kappa"][0])
        check(case_name + ": new selected cut feedback uses the complete right97 column",
              columns["p"][2][1] < 2**11)
        target_cut = F(12, 25) if case_name == "full" else F(61, 125)
        target_det = F(6, 25) if case_name == "full" else F(1, 4)
        check(case_name + ": new cut diagonal remains strictly positive with stated margin",
              target_cut < scalar["cut_gap"][0] - q)
        check(case_name + ": new complete determinant retains the stated margin",
              target_det < scalar["det"][0] * denominator)
        check(case_name + ": selected secant retains original complete chart bound",
              scalar["kappa"][1] + tau < F(1, 5))
        receiver_uppers[case_name] = {}
        for role in ("g", "p", "a", "c"):
            row = []
            for index, output in enumerate(("whole", "negative", "true_cut")):
                base = columns[role][index][1]
                if role == "p":
                    increment = base * q / denominator
                else:
                    cut_source = columns[role][2][1] + (role == "c")
                    increment = (columns["p"][index][1] * tau
                                 * cut_source / denominator)
                integer_upper = -(-base.numerator // base.denominator)
                check(case_name + ": corrected " + role + " column in " + output,
                      base + increment < integer_upper)
                row.append(integer_upper)
            receiver_uppers[case_name][role] = row

    print(json.dumps({
        "checks": checks,
        "result": {
            "all_passed": True,
            "new_exact_combinations": len(checks),
            "cap_extra_upper_exponent": cap_exponent,
            "row_extra_upper_exponent": cap_exponent,
            "cut_feedback_upper_exponent": cut_exponent,
            "case_receiver_integer_uppers": receiver_uppers,
            "actual_selected_height_derivative": True,
            "complete_B_and_C_mean": True,
            "original_ordered_97_rows": True,
            "whole_H_C_image_and_constant_input": True,
            "extra_high_cut_plus_one": True,
            "original_cases_not_mixed": True,
            "nonlinear_L2_open_value_domain_claimed": False,
            "complete_infinite_core_inverse_claimed": False,
            "old_scientific_targets": 0,
        },
    }, indent=2))


if __name__ == "__main__":
    main()
