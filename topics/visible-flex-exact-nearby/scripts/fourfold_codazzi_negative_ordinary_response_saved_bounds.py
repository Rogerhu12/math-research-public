"""Exact new raw-state consequences of the complete saved SP, root, NW and strong graph.

Each input is a small original result, execution, or operator definition.
No numerical producer, certificate restoration or past target is called.
"""
from fractions import Fraction as F
from hashlib import sha256
import json
from pathlib import Path
import re

TOPIC = Path(__file__).resolve().parents[1]
SP = "notes/primitive_mean_strict_propagation_ci/run-43731464771-1/"
ROOT = "notes/large_root_Cauchy_ci/run-43621934843-1-full-real-large-root-Cauchy/"
NW = "notes/negative_nu_waist_ci/run-45781137624-1/"
PG = "notes/full_delta_positive_root_graph_ci/run-43617150971-1-full-real-delta-positive-root-graph/"
COLLAR = "notes/full_delta96_root_collar_ci/run-43606747196-1/consumers/"
FILES = {
    "sp": (SP+"execution.json", 35259, "a3a02969178e5e8b3b040fafd51d08b25d75b3f3922f2ae2e9ee0d4a8ab18a12"),
    "root": (ROOT+"evidence/full-real-large-root-Cauchy-summary.json", 50621, "238a85156791fac2516a23c5f9a6ea1253e648c341bedae139d1c2c5c47cbee5"),
    "root_run": (ROOT+"process.json", 11652, "82bf0467ccaaece38dcb606e537552e5c59dedf6ac8cb9cd4375458fab951c1c"),
    "nw": (NW+"actual-negative-nu-waist.json", 15210, "1a06d01060a63eac98aeaa330f130a8ee766ab5ac878634e637f9cea30e1cb70"),
    "nw_run": (NW+"execution.json", 13970, "eeb4ed157912e742e8d773ca32b04570296973b924f4a92b1a4ec153c30efe2b"),
    "nw_manifest": ("notes/2026-11-26-negative-nu-waist-inputs.json", 11815, "b697e8665801a6e4d5120ca312d72a339cc28a2516d6dabd255f56ee79690f2d"),
    "graph": (PG+"evidence/full-real-delta-positive-root-high-graph-summary.json", 27047, "410e8f07545c862425673a2c0cc37eebfc6f950217167f2b72c44d5a7b5676e7"),
    "graph_run": (PG+"process.json", 7437, "d35bb44e4cd7d933778d3234b6b0fe6c271fa9a8e744466a3fa9fd40f0e1f454"),
    "collar": (COLLAR+"process.json", 11340, "f919ecd9da5d447cf8950d1b267c28c7c33c2c396b21318b64a45317646745ae"),
    "SP_definition": ("results/R133-supplement-complete-primitive-and-mean-strict-propagation-to-the-waist.md", 20730, "ae01c213b63ae618e4657b5966604e7fbec4acb4763ea4b8aae848e1a40a40b4"),
    "root_definition": ("results/R133-supplement-actual-full-real-large-root-Cauchy-energies.md", 7516, "00393be45915d687f80270be2fe993f9206a1cb77db6e7587f0755e3daff4ddd"),
    "source_definition": ("results/R133-supplement-exact-selected-parameter-core-differences-and-finite193-transfer.md", 15214, "92fd222bbcc4495cce091cedee2628f83d014be23a40328a7292d47616621635"),
    "graph_definition": ("results/R133-supplement-full-real-delta-positive-high-root-to-regular-graph.md", 10473, "5c4b3e1ba50b96e1955c24e560627bb7efc01c447b35ed9352373febb9a09e6e"),
    "collar_definition": ("results/R133-supplement-full-real-delta96-positive-root-collar.md", 11453, "4a2a4f04009258cb9b794068c49fd5b31c77146fc14b4c8f115609055421c23a"),
}


def require(ok, message):
    if not ok:
        raise ValueError(message)


def endpoints(record):
    s = record["ball"]
    if not s.startswith("["):
        return F(s), F(s)
    m = re.fullmatch(r"\[([^\s]+) \+/- ([^\s]+)\]", s)
    require(m is not None, "complete finite ball")
    a,b = map(F,m.groups())
    require(b >= 0, "nonnegative radius")
    return a-b,a+b


def exponential_upper(x):
    """Positive exact Taylor sum through degree 20 with a geometric tail."""
    require(0 <= x < 2, "range of exponential inequality")
    term = total = F(1)
    for k in range(1,21):
        term *= x/k
        total += term
    return total+(term*x/21)/(1-x/22)


def main():
    docs = {}
    for key,(relative,size,digest) in FILES.items():
        raw = (TOPIC/relative).read_bytes()
        require(len(raw) == size and sha256(raw).hexdigest() == digest, "whole "+key)
        if relative.endswith(".json"):
            docs[key] = json.loads(raw)
    sp_doc,nw,root,pg,collar = (docs[k] for k in ("sp","nw","root","graph","collar"))
    sp_native = sp_doc["actual_scientific_receipt"]
    sp = sp_native["complete_strict_propagation_conclusion"]
    params = nw["parameters"]
    cut,radius = F(params["exact_strict_interval"][1]),F(params["exact_root_Cauchy_radius"])
    lower,upper = map(F,params["exact_root_interval"])
    width = upper-lower
    ids = (("sp",43731464771),("root_run",43621934843),("nw_run",45781137624),
           ("graph_run",43617150971),("collar",43606747196))
    for key,run in ids:
        doc = docs[key]
        require(doc["complete"] and str(doc["run_id"]) == str(run) and str(doc["run_attempt"]) == "1",
                "whole completed process "+key)
    for doc,key,n in ((sp_native,"gates",20),(root,"gates",8),(pg,"gates",10),
                      (collar,"mathematical_gates",19)):
        require(len(doc[key]) == n and all(g["passed"] is True for g in doc[key]), "whole gates")
    require(sp_doc["actual_returncode"] == 0 and sp_native["proved"] and nw["proved"]
            and nw["saved_record_count"] == 4 and docs["nw_run"]["actual_child_returncode"] == 0
            and docs["nw_run"]["scientific_files"][0]["sha256"] == FILES["nw"][2]
            and docs["nw_run"]["manifest_sha256"] == FILES["nw_manifest"][2], "old actual admissions")
    require(root["native_sha256"] == docs["root_run"]["complete_native_sha256"]
            and pg["native_sha256"] == docs["graph_run"]["complete_native_sha256"]
            and pg["original_collar_native_sha256"] == collar["native_sha256"], "original whole native bindings")
    require(sp_native["exact_family_identity"] == nw["reference_identity"]
            and root["background_definition_sha256"] == pg["derived_definition_sha256"]
            == params["continuous_centre_definition_sha256"]
            and root["explicit_direction_definition_sha256"] == pg["explicit_direction_definition_sha256"]
            == params["continuous_direction_definition_sha256"], "one centre and direction")
    require(sp["complete_mean_coordinates"] == 2 and sp["exact_interval"] == params["exact_strict_interval"]
            and sp["all_shorter_ordered_products_and_source_insertions_included"]
            and sp["affine_jumps_are_independent_without_radial_length_factor"]
            and root["all_frequencies_and_independent_even_mean_retained"]
            and pg["unknown_head_is_supplied_as_a_source_not_set_to_zero"]
            and pg["given_complete_head_positive_high_inverse_and_root_graph_proved"]
            and pg["exact_same_global_Z_reference"] and F(pg["fixed_body_cut"]) > upper
            and F(root["exact_real_delta_radius"]) == F(pg["exact_real_delta_radius"]) == F("1e-8")
            and F(nw["selected_member_identity"]["absolute_delta_upper"]) < F("1e-10")
            and root["exact_root_interval"] == params["exact_root_interval"]
            and params["exact_original_negative_window"] == ["0",str(upper)]
            and cut == upper-radius and radius == F("1/200") and width == F("9e-13"),
            "complete spaces, parameters and physical cuts")
    cases = [case for case in root["cases"] if F(case["exact_radius"]) == radius]
    require(len(cases) == 1 and cases[0]["passed"], "original complete root radius")
    row = sp["reverse_nonradial_product"]
    require(len(row) == 2 and all(len(v) == 2 for v in row), "whole comparison product")
    checks = {}

    def check(name, lhs, rhs):
        require(lhs < rhs,name)
        checks[name] = True

    check("original_q_lower",F(".5338"),endpoints(sp["new_entire_q_lower"])[0])
    check("original_q_upper",endpoints(sp["new_entire_q_upper"])[1],F("1.03"))
    check("reverse_nonradial_22",endpoints(row[1][1])[1],F("1.164"))
    check("positive_log_variation",endpoints(sp["new_complete_forward_log_upper"])[1],F(".847"))
    check("full_rank",endpoints(sp["complete_selected_scalar_maxima"]["N_gamma_upper"])[1],F("3.844"))
    U,A,W,D = map(F,("8.22","25.943","10.484","19.29"))
    C,S = F("6.531704"),F("1.307204e-6")
    check("raw_reverse_gain",F("1.03")/F(".5338")*F("1.164")*
          exponential_upper(F(".847")+F("3.844")*cut/2),U)
    check("actual_C0",endpoints(cases[0]["bounds"]["H0"]["full_root_to_state"])[1],C)
    check("known_same_window",endpoints(nw["new_records"]["selected_negative_source_from_same_fixed_window_upper"])[1],S)
    check("all_288",1+1152**2,W**6)
    check("whole_root_and_strict",C**2*(radius+cut*U**2),A**2)
    check("strict_atoms",cut*U**2,F("3.972")**2)
    check("disjoint_source_gain",(cut*U)**2/2+A**2*radius*W**2,D**2)
    check("known_negative_contribution",D*S,F("2.522e-5"))
    check("bessel_high_mixed",9**6*(1+F(1,388**2)),F("9.00002")**6)
    rc = collar["exact_rational_contract"]
    E,cross = F(rc["low_propagator_upper"]),F(rc["high_to_low_L2"])
    require(E == F("201/200") and cross == F("58/5") and F(rc["low_generator_upper"]) < 500,
            "complete raw low generator and whole high-to-low crossing")
    check("sliver_exponential",exponential_upper(500*width),E)
    check("sliver_low_initial_and_atoms",width*E**2,F("9.54e-7")**2)
    check("sliver_high_sup",width*9*(1+E*cross*width)**2,F("2.85e-6")**2)
    check("root_and_narrow_head",A+F("9.54e-7"),F("25.95"))
    check("known_full_window_contribution",F("2.522e-5")+width*E*S,F("2.523e-5"))
    check("sufficient_continuous_trace_example",F("25.95")*F(".00019")+F("2.85e-6")+F("2.523e-5"),F(".005"))

    roles = ("full_root_outgoing_unstable_port","collar_Z_sup")
    require(len(pg["input_order"]) == 7 and len(pg["response_rows"]) == 7
            and all(len(row) == 7 for row in pg["response_rows"].values()), "all seven complete strong rows")
    print(json.dumps(dict(proved=True,whole_inputs={key:v[2] for key,v in FILES.items()},
        comparisons=checks,raw_strict_reverse_upper=str(U),root_to_negative_ordinary_upper=str(A),
        zero_root_zero_jump_negative_ordinary_source_upper="0.00002522",
        strong_positive_inputs=pg["input_order"],strong_actual_rows={k:pg["response_rows"][k] for k in roles},
        full_window_coefficients={"root_mixed":"25.95","collar_high_sup":"0.00000285",
            "known_negative_ordinary":"0.00002523","root_atoms":"25.943",
            "strict_atoms":"3.972","sliver_low_atoms":"0.000000954"},
        actual_square_head_and_incoming_closed=False,actual_qnu_full_threshold_proved=False,
        nonlinear_family_proved=False,old_science_target_calls=0),sort_keys=True))


if __name__ == "__main__":
    main()
