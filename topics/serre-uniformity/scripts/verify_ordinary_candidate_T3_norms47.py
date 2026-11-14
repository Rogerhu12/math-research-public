#!/usr/bin/env python3
"""Independent standard-library arithmetic checks of five actual T3 norms.

For split targets, recompute every saved unit logarithm and the complete
integer-weight Phi product. For the irreducible quartic, re-evaluate all455
true stored numerators and all5 fixed factors in the saved V1/V2/V3 bases,
then recompute Phi by its full integer expression and a unit-pivot norm.
"""
import argparse
import gzip
import hashlib
import json
from pathlib import Path

Q = 47**4


def read(path):
    raw = Path(path).read_bytes()
    return json.loads(gzip.decompress(raw) if str(path).endswith(".gz") else raw)


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def mul(a, b):
    return ((a[0]*b[0]-a[1]*b[1]) % Q, (a[0]*b[1]+a[1]*b[0]) % Q)


def power(a, n):
    a = tuple(a)
    if n < 0:
        inv = pow((a[0]*a[0]+a[1]*a[1]) % Q, -1, Q)
        return power((a[0]*inv % Q, -a[1]*inv % Q), -n)
    value = (1, 0)
    while n:
        if n & 1:
            value = mul(value, a)
        a = mul(a, a)
        n //= 2
    return value


def logunit(a):
    n = 47**2-1
    u = power(a, n)
    z = ((u[0]-1) % Q, u[1])
    assert all(x % 47 == 0 for x in z)
    z2, z3 = mul(z, z), mul(mul(z, z), z)
    inv2, inv3, invn = pow(2, -1, Q), pow(3, -1, Q), pow(n, -1, Q)
    return tuple((z[k]-inv2*z2[k]+inv3*z3[k])*invn % Q for k in range(2))


class Quartic:
    def __init__(self, poly):
        self.poly = poly

    def mul(self, a, b):
        value = [0]*7
        for i, x in enumerate(a):
            for j, y in enumerate(b):
                value[i+j] += x*y
        for k in range(6, 3, -1):
            for j in range(4):
                value[k-4+j] -= value[k]*self.poly[j]
        return [x % Q for x in value[:4]]

    def matrix(self, a):
        columns = [self.mul(a, [int(i == j) for i in range(4)]) for j in range(4)]
        return [[columns[j][i] for j in range(4)] for i in range(4)]

    def eliminate(self, a, augmented=False):
        matrix = self.matrix(a)
        if augmented:
            matrix = [row+[int(i == 0)] for i, row in enumerate(matrix)]
        determinant = 1
        for k in range(4):
            pivot = next(i for i in range(k, 4) if matrix[i][k] % 47)
            if pivot != k:
                determinant = -determinant
                matrix[k], matrix[pivot] = matrix[pivot], matrix[k]
            pivotvalue = matrix[k][k]
            determinant = determinant*pivotvalue % Q
            inv = pow(pivotvalue, -1, Q)
            matrix[k] = [x*inv % Q for x in matrix[k]]
            for i in range(4):
                if i == k:
                    continue
                z = matrix[i][k]
                matrix[i] = [(x-z*y) % Q for x, y in zip(matrix[i], matrix[k])]
        return determinant % Q, [row[-1] for row in matrix] if augmented else None

    def norm(self, a):
        return self.eliminate(a)[0]

    def power(self, a, n):
        if n < 0:
            inverse = self.eliminate(a, augmented=True)[1]
            assert self.mul(a, inverse) == [1, 0, 0, 0]
            return self.power(inverse, -n)
        result = [1, 0, 0, 0]
        while n:
            if n & 1:
                result = self.mul(result, a)
            a = self.mul(a, a)
            n //= 2
        return result


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--qc-dir", type=Path, required=True)
    ap.add_argument("--output", type=Path, required=True)
    args = ap.parse_args()
    base = args.qc_dir
    results = {}
    inputs = {}
    for j in [12, 15, 19, 27, 32]:
        disk = "ORD_j"+str(j).zfill(2)
        support_path = base/"ordinary-F3-norms"/(disk+"_actual_T3_support47.json.gz")
        norm_path = support_path.with_name(disk+"_actual_T3_principal_norm47.json.gz")
        flat_path = base/"ordinary-F2-norms"/(disk+"_actual_principal_function47.json.gz")
        transport_dir = base/"ordinary-principal-transports"/disk
        manifest_path = transport_dir/"transport_manifest47.json"
        support, norm, flat, manifest = map(read, [support_path, norm_path, flat_path, manifest_path])
        assert support["complete_actual_T3_support"] and norm["complete_actual_principal_norm_on_T3_P"]
        assert support["source_disk_id"] == norm["disk_id"] == flat["disk_id"] == disk
        assert norm["input_sha256"][support_path.name] == sha(support_path)
        assert norm["input_sha256"][flat_path.name] == sha(flat_path)
        assert flat["input_sha256"][manifest_path.name] == sha(manifest_path)
        assert support["T3_full_weight2_trace_left"] == support["T3_full_weight2_trace_right"]
        assert support["T3_canonical_trace_left"] == support["T3_canonical_trace_right"]
        assert support["raw_level_determinant_mod41"] == 3 and support["raw_target_pairing_exponent"] == 3
        ep = flat["combined_function_to_actual_A1_t"]
        assert ep["f0_integer_exponent"] == 0
        inputs[disk] = {p.name: sha(p) for p in [support_path, norm_path, flat_path, manifest_path]}
        if j != 32:
            assert support["kernel_factor_degrees_mod47"] == [[1, 1], [1, 1], [2, 1]]
            branch_values = {}
            checked_logs = 0
            for chart in norm["charts"]:
                pointindices = chart["indices_0based"]
                units = {}
                for group in chart["groups"].values():
                    for row, pointindex in enumerate(pointindices):
                        for column, label in enumerate(group["labels"]):
                            value = group["unit_values"][row][column]
                            logarithm = group["unit_logs"][row][column]
                            assert logunit(value) == tuple(logarithm)
                            units[(pointindex, label)] = tuple(value)
                            checked_logs += 1
                for row in chart["rows"]:
                    index = row["target_branch_0based"]
                    assert index in pointindices and row["final_distinguished_factor_is_one"]
                    value = power(units[(index, "fb")], ep["f_b_integer_exponent"])
                    value = mul(value, power(units[(index, "fc")], ep["f0_integer_exponent"]))
                    for label, exponent in [("v1", 1), ("FP", 1), ("GQ", -1)]:
                        value = mul(value, power(units[(index, label)], exponent))
                    for term in flat["section_factors"]:
                        value = mul(value, power(units[(index, term["label"])], term["signed_integer_exponent"]))
                    assert value == tuple(row["actual_Phi_value"])
                    assert logunit(value) == tuple(row["actual_log_Phi_value"])
                    branch_values[index] = value
            assert sorted(branch_values) == [0, 1, 2, 3]
            actual = (1, 0)
            for i in range(4):
                actual = mul(actual, branch_values[i])
            assert actual == (norm["actual_norm_Phi_T3_P_mod47four"], 0)
            for cache in norm["jet_cache_manifest"]:
                path = base/"ordinary-norm-cache"/cache["basename"]
                assert path.stat().st_size == cache["bytes"] and sha(path) == cache["sha256"]
            results[disk] = {"unit_logarithms_recomputed": checked_logs,
                             "all_four_flat_integer_Phi_products_recomputed": True,
                             "norm": actual[0], "log": logunit(actual)[0]}
        else:
            assert support["kernel_factor_degrees_mod47"] == [[4, 1]]
            field = Quartic(support["kernel_polynomial_ascending"])
            bases = {1: support["W_coefficients_ascending_in_kernel_root"],
                     2: support["V2_coefficients_ascending_in_kernel_root"],
                     3: norm["V3_coefficients_ascending_in_kernel_root"]}

            def evaluate(degree, coefficients):
                co = [x[0] for x in coefficients]
                answer = []
                for k in range(4):
                    values = [mul(x, y) for x, y in zip(bases[degree][k], co)]
                    re = sum(x[0] for x in values) % Q
                    im = sum(x[1] for x in values) % Q
                    assert im == 0
                    answer.append(re)
                return answer

            actual_values = {}
            rows = {v["label"]: v for v in norm["all_function_section_values_and_norms"]}
            checked_functions = 0
            for entry in manifest["functions"]:
                if entry["phase"] == "formal_extraction":
                    continue
                path = transport_dir/entry["filename"]
                assert sha(path) == entry["sha256"]
                f = read(path)
                actual = evaluate(f["line_bundle_power"], f["numerator_coefficients"])
                saved = rows[f["label"]]
                assert actual == saved["actual_section_value_coefficients_in_kernel_root"]
                assert field.norm(actual) == saved["actual_quartic_norm_mod47four"]
                actual_values[f["label"]] = actual
                checked_functions += 1
            assert checked_functions == 455
            fixed = {"fb": (1, flat["f_b_coefficients"]), "fc": (1, flat["f0_coefficients"]),
                     "v1": (1, ep["v1_weight2_coefficients"]),
                     "FP": (2, ep["F_terminal_V2_coefficients"]), "GQ": (2, ep["G_terminal_V2_coefficients"])}
            for label, (degree, co) in fixed.items():
                value = evaluate(degree, co)
                saved = norm["fixed_section_values_and_norms"][label]
                assert saved["value_coefficients"] == value
                assert saved["norm"] == field.norm(value)
                actual_values[label] = value
            Phi = field.power(actual_values["fb"], ep["f_b_integer_exponent"])
            Phi = field.mul(Phi, field.power(actual_values["fc"], ep["f0_integer_exponent"]))
            for label, exponent in [("v1", 1), ("FP", 1), ("GQ", -1)]:
                Phi = field.mul(Phi, field.power(actual_values[label], exponent))
            for term in flat["section_factors"]:
                Phi = field.mul(Phi, field.power(actual_values[term["label"]], term["signed_integer_exponent"]))
            assert Phi == norm["actual_Phi_value_in_quartic_target_algebra"]
            actual_norm = field.norm(Phi)
            assert actual_norm == norm["actual_norm_Phi_T3_P_mod47four"]
            results[disk] = {"all455_numerators_re_evaluated_from_exact_coefficients": True,
                             "all5_fixed_factors_re_evaluated": True,
                             "full_integer_Phi_expression_recomputed_in_quartic_algebra": True,
                             "norm_via_independent_unit_pivot_elimination": True,
                             "norm": actual_norm, "log": logunit((actual_norm, 0))[0]}
        assert results[disk]["log"] == norm["actual_log_norm_Phi_T3_P_mod47four"]
        print("PASS independent actual T3 norm", disk, results[disk]["norm"], results[disk]["log"], flush=True)
    output = {"complete": True, "results": results, "input_sha256": inputs,
              "source_sha256": sha(__file__),
              "scope": "Arithmetic and exact retained numerator checks; no group-chain or torsion-table rerun, no local-height or common-root claim"}
    args.output.write_text(json.dumps(output, sort_keys=True, indent=2)+"\n")
    print("PASS FIVE CANDIDATE T3 NORMS", sha(args.output), flush=True)


if __name__ == "__main__":
    main()
