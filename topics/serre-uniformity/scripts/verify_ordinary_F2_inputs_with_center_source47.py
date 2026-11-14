#!/usr/bin/env python3
"""Independent hashes and scalar audit of generic ordinary F2 outputs."""
import argparse
import gzip
import hashlib
import json
from pathlib import Path


def sha(p):
    return hashlib.sha256(Path(p).read_bytes()).hexdigest()


def read(p):
    raw = Path(p).read_bytes()
    return json.loads(gzip.decompress(raw) if str(p).endswith(".gz") else raw)


def flat(x):
    if isinstance(x, list):
        return [z for y in x for z in flat(y)]
    return [x]


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--disk-id", required=True)
    ap.add_argument("--qc-dir", type=Path, required=True)
    ap.add_argument("--root-dir", type=Path, required=True)
    ap.add_argument("--output", type=Path, required=True)
    ap.add_argument("--center-source", type=Path, required=True)
    args = ap.parse_args()
    qc, root, d = args.qc_dir.resolve(), args.root_dir.resolve(), args.disk_id
    names = {
        "generic_center_source": args.center_source.resolve(),
        "generic_disk_source": root/"p41_generic_ordinary_F2_local_polynomial47.py",
        "frozen_R259_source": root/"p41_ordinary_F2_connection47.py",
        "frozen_R262_source": root/"p41_ordinary_F2_local_polynomial47.py",
        "center": root/(d+"_actual_canonical_F2_height47.json.gz"),
        "polynomial": root/(d+"_actual_canonical_F2_polynomial47.json.gz"),
        "full_norm": root/(d+"_actual_F2_first_variable_norm47.json.gz"),
        "Abel": qc/"ordinary-abel-with-transports"/(d+"_Abel47.json.gz"),
        "multiply": qc/"ordinary-abel-with-transports"/(d+"_multiply47.json.gz"),
        "second": qc/"ordinary-second-kind"/(d+"_second_kind_complete47.json.gz"),
        "principal": qc/"ordinary-F2-norms"/(d+"_actual_principal_function47.json.gz"),
        "T2_support": qc/"ordinary-F2-norms"/(d+"_actual_T2_support47.json.gz"),
        "T2_norm": qc/"ordinary-F2-norms"/(d+"_actual_T2_principal_norm47.json.gz"),
        "based": qc/"p41_all19_based_points47.json.gz",
    }
    data = {k: read(p) for k, p in names.items() if k not in [
        "generic_center_source", "generic_disk_source", "frozen_R259_source", "frozen_R262_source"]}
    center, poly, fullnorm = [data[k] for k in ["center", "polynomial", "full_norm"]]
    assert center["source_sha256"] == sha(names["generic_center_source"])
    assert poly["source_sha256"] == sha(names["generic_disk_source"])
    assert all(data[k]["disk_id"] == d for k in ["center", "polynomial", "full_norm", "Abel",
        "multiply", "second", "principal", "T2_norm"])
    assert data["T2_support"]["source_disk_id"] == d
    checks = []
    def edge(source, target):
        h = data[source]["input_sha256"]
        matches = [v for k, v in h.items() if Path(k).name == names[target].name]
        assert matches and set(matches) == {sha(names[target])}, (source, target)
        checks.append([source, target])
    for s, t in [("center", "second"), ("center", "principal"), ("center", "T2_support"),
        ("center", "full_norm"), ("polynomial", "center"), ("polynomial", "Abel"),
        ("polynomial", "multiply"), ("Abel", "multiply"), ("second", "Abel"),
        ("second", "multiply"), ("second", "based"), ("principal", "second"),
        ("T2_norm", "principal"), ("T2_norm", "T2_support"), ("full_norm", "T2_norm"),
        ("full_norm", "principal"), ("full_norm", "second"), ("full_norm", "multiply"),
        ("full_norm", "based")]:
        edge(s, t)
    assert data["multiply"]["input_sha256"] == sha(names["based"])
    assert data["multiply"]["bits_done"] == data["multiply"]["target_bits"] == 304
    assert data["multiply"]["point_sha256"] == data["Abel"]["actual_multiple_point_sha256"]
    Q, q = 47**4, 47**3
    # Every tangent value below was independently retained by the fixed-norm executor.
    rows = {x["label"]: x for x in fullnorm["fixed_and_collision_part"]["rows"]}
    ab, apoint = [rows[k]["j_tangent"]["g1_differential_over_dj"] for k in ["P_minus3", d]]
    assert ab[1] == apoint[1] == 0 and ab[0] % 47 and apoint[0] % 47
    assert [ab[0], apoint[0]] == center["actual_g1_over_dj_at_base_and_center"]
    sigma = pow(ab[0] * pow(apoint[0], -1, Q) % Q, 4, Q)
    z = (pow(sigma, 46, Q) - 1) % Q
    assert z % 47 == 0
    log_sigma = (z-z*z*pow(2,-1,Q)+z*z*z*pow(3,-1,Q))*pow(46,-1,Q) % Q
    assert sigma == center["canonical_sigma_fibre_coordinate_mod47four"]
    assert log_sigma == center["canonical_sigma_coordinate_log_mod47four"]
    m = fullnorm["actual_integer_scale"]
    assert m == center["actual_integer_scale"] == data["Abel"]["target_multiplier"]
    assert m % 47 == 9
    normlog = fullnorm["actual_log_norm_Phi_on_F2_second_divisor_mod47four"]
    assert normlog == center["first_variable_principal_log_norm_mod47four"]
    t = center["all_actual_tiny_integrals_mod47four"]
    weights = {"T2C":27,"C":4,"u_minus_b":162,"Z8_minus20b":-27,
               "c7_minus_b":-54,"K_g1_minus106b":4}
    tiny = sum(weights[k]*t[k] for k in weights) % Q
    assert tiny == center["second_divisor_tiny_integral_mod47four"]
    actual_height = (log_sigma + pow(m,-1,Q)*(normlog+tiny)) % Q
    assert actual_height == center["actual_local_sigma_F2_height_mod47four"]
    actual_nu = flat(data["second"]["actual54_second_kind_integrals_of_C_mod47four"])
    center_nu = flat(center["actual_gradients_original_nu_mod47cubed"]["C"])
    assert [x%q for x in actual_nu] == center_nu
    ph = data["principal"]["combined_function_to_actual_A1_t"]["actual_A1_physical_parameters"]
    assert flat(ph) == flat(center["physical_family1_parameters"])
    height_poly = poly["canonical_local_sigma_F2_height_coefficients_0to3_in_y_mod47four"]
    assert height_poly[0] == actual_height
    global_poly = poly["global_F2_coefficients_0to4_in_y_mod47four"]
    qc_poly = [(global_poly[k]-800*(height_poly[k] if k<4 else 0))%Q for k in range(5)]
    assert qc_poly == poly["actual_QC_F2_coefficients_0to4_in_y_mod47four"]
    assert all(x%47==0 for x in qc_poly)
    red = [(x//47)%47 for x in qc_poly]
    assert red == poly["QC_divided_by47_reduction_coefficients_mod47"]
    values = [sum(c*pow(y,k,47) for k,c in enumerate(red))%47 for y in range(47)]
    roots = [y for y,v in enumerate(values) if v==0]
    assert values == poly["all47_residual_QC_values"] and roots == poly["residual_QC_roots"]
    assert poly["entire_disk_excluded_for_all_four_bad_components"] == (roots==[])
    discriminant = (red[1]**2-4*red[0]*red[2])%47
    assert discriminant == poly["residual_quadratic_discriminant"]
    divided = [x//47 for x in qc_poly]
    lifted = []
    for y0 in roots:
        y = y0
        derivative = sum(k*c*pow(y0,k-1,47) for k,c in enumerate(divided) if k)%47
        assert derivative
        digits = [y0]
        modulus = 47
        for _ in range(2):
            next_modulus = 47*modulus
            value = sum(c*pow(y,k,next_modulus) for k,c in enumerate(divided))%next_modulus
            assert value%modulus == 0
            digit = -(value//modulus)*pow(derivative,-1,47)%47
            digits.append(digit)
            y += digit*modulus
            modulus = next_modulus
        assert sum(c*pow(y,k,q) for k,c in enumerate(divided))%q == 0
        lifted.append({"y_mod47cubed":y,"z_mod47four":47*y,
                       "y_base47_digits":digits,"derivative_mod47":derivative})
    out = {
        "disk_id":d,"input_sha256":{str(p):sha(p) for p in names.values()},
        "all19_nested_input_hash_edges_checked":checks,
        "based_point_and_terminal_point_hashes_match":True,
        "fixed_norm_j_tangent_and_sigma_values_match_independently":True,
        "actual_g1_over_dj_base_center":[ab[0],apoint[0]],
        "canonical_sigma":sigma,"canonical_sigma_log":log_sigma,
        "signed_actual_scale":m,"second_divisor_tiny":tiny,"full_first_norm_log":normlog,
        "actual_center_height":actual_height,"local_polynomial":height_poly,
        "global_polynomial":global_poly,"QC_polynomial":qc_poly,
        "QC_div47_reduction":red,"residual_roots":roots,
        "residual_discriminant":discriminant,
        "simple_single_F2_root_candidates_to_available_precision":lifted,
        "scope":"Independent exact scalar arithmetic and input identity checks, plus source-diff review recorded separately; no duplicate RR, T2 or group-chain reexecution.",
        "source_sha256":sha(__file__),
    }
    args.output.write_text(json.dumps(out,ensure_ascii=False,indent=2)+"\n")
    print("PASS generic",d,"nested19hashes,physical parameters,nu,canonical tangent,center and QC scalars",sha(args.output))


if __name__=="__main__":
    main()

