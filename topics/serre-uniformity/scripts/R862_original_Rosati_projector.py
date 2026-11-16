#!/usr/bin/env python3
"""The original A projector from the completed R791 Hom correspondence.

No old Hom, period, degree or Galois solve is repeated.  The new arithmetic is
one exact degree-six norm polynomial and its action on the old 12-row matrix.
"""
import argparse
import gzip
import hashlib
import json
import os
from pathlib import Path
import sys
import time
import traceback

RESULT = "R862-original-Rosati-projector-and-integral-correspondences"
FINAL = "p41-original-Rosati-projector-and-integral-correspondences-certificate.json"
PREFIX = "R862-original-projector-"
REPOSITORY = "Rogerhu12/math-research-public"
BASE = ("result", "run_id", "source_commit", "core_sha256",
        "manifest_sha256", "configuration_sha256")
STRATEGY = {
    "original_p": 41,
    "original_map_index": 4,
    "original_map_degree": 1206,
    "original_real_map_degree": 3618,
    "coefficient_field": "Q[S]/(S^6-S^5-6*S^4+6*S^3+8*S^2-8*S+1)",
    "field_basis": "1,S,S^2,S^3,S^4,S^5",
    "old_aA_basis": "1,s1,s2,s3,s4,s5; sj=t^j+t^(-j)",
    "norm_polynomial": "Norm_F/Q(X-aA), without a primitiveness assumption",
    "new_characteristic_polynomial_algorithm": "exact integral Faddeev-LeVerrier",
    "D": "q_R^dagger*q_R, sum of seven original real-map pull-push correspondences",
    "projector": "1-P_A(D)/P_A(0)=q^dagger*kappa^(-1)*q",
    "integer_multiple": "-(D^6+c5*D^5+...+c1*D)",
    "integer_denominator": "d_A=P_A(0)>0; no minimality claim",
    "original_T7_phase": "zeta^2",
    "whole_JX_equality_source": "R862 proof, not only the 12-row Hom check",
    "Y_active_Hecke_projector_computed": False,
    "non_p_height_support_computed": False,
    "old_arithmetic_recomputed": False,
    "budget_excluded_from_mathematical_identity": True,
}


class BudgetStop(RuntimeError):
    pass


def fingerprint(value):
    return hashlib.sha256(json.dumps(
        value, sort_keys=True, separators=(",", ":")).encode()).hexdigest()


def sha(path):
    out = hashlib.sha256()
    with Path(path).open("rb") as stream:
        for data in iter(lambda: stream.read(1048576), b""):
            out.update(data)
    return out.hexdigest()


def read(path):
    path = Path(path)
    with (gzip.open if path.suffix == ".gz" else open)(
            path, "rt", encoding="utf-8") as stream:
        return json.load(stream)


def atomic(path, value):
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    temporary = path.with_name(path.name + ".tmp")
    encoded = (json.dumps(value, sort_keys=True, separators=(",", ":")) + "\n").encode()
    if path.suffix == ".gz":
        with temporary.open("wb") as raw:
            with gzip.GzipFile(fileobj=raw, mode="wb", filename="", mtime=0) as stream:
                stream.write(encoded)
    else:
        temporary.write_bytes(encoded)
    temporary.replace(path)


def plain(row):
    result = {key: row[key] for key in ("file", "bytes", "sha256")}
    assert Path(result["file"]).name == result["file"]
    assert result["file"] not in ("", ".", "..") and "\\" not in result["file"]
    assert isinstance(result["bytes"], int) and result["bytes"] >= 0
    assert len(result["sha256"]) == 64
    return result


def spec(path):
    path = Path(path)
    return {"file": path.name, "bytes": path.stat().st_size, "sha256": sha(path)}


def bound(folder, row):
    row = plain(row)
    path = Path(folder) / row["file"]
    assert path.is_file() and path.stat().st_size == row["bytes"]
    assert sha(path) == row["sha256"]
    return path


def source_identity(source):
    return {**{key: source[key] for key in BASE},
            "selected_files_sha256": fingerprint({
                name: plain(row) for name, row in sorted(source["files"].items())}),
            "certificate": plain(source["certificate"])}


def identity(n):
    return [[int(i == j) for j in range(n)] for i in range(n)]


def zero(n):
    return [[0] * n for _ in range(n)]


def matmul(a, b):
    assert a and b and len(a[0]) == len(b)
    cols = list(zip(*b))
    return [[sum(x * y for x, y in zip(row, col)) for col in cols] for row in a]


def add_diagonal(matrix, value):
    out = [row[:] for row in matrix]
    for i in range(len(out)):
        out[i][i] += value
    return out


def matrix_polynomial(coefficients, matrix):
    out = zero(len(matrix))
    for coefficient in reversed(coefficients):
        out = add_diagonal(matmul(out, matrix), coefficient)
    return out


def trim(poly):
    out = list(poly)
    while len(out) > 1 and out[-1] == 0:
        out.pop()
    return out


def polyadd(a, b):
    n = max(len(a), len(b))
    return trim([(a[i] if i < len(a) else 0) +
                 (b[i] if i < len(b) else 0) for i in range(n)])


def polymul(a, b):
    out = [0] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            out[i + j] += x * y
    return trim(out)


def remainder(poly, monic):
    assert monic[-1] == 1
    out = trim(poly)
    degree = len(monic) - 1
    while len(out) > degree:
        coefficient = out[-1]
        shift = len(out) - len(monic)
        for i, value in enumerate(monic):
            out[i + shift] -= coefficient * value
        out = trim(out)
    return out


class ExactField:
    def __init__(self, polynomial):
        assert len(polynomial) == 7 and polynomial[-1] == 1
        self.polynomial = list(polynomial)
        self.one = [1, 0, 0, 0, 0, 0]

    def canonical(self, values):
        result = remainder(values, self.polynomial)
        return result + [0] * (6 - len(result))

    def mul(self, a, b):
        return self.canonical(polymul(a, b))

    def evaluate(self, polynomial, element):
        out = [0] * 6
        for value in reversed(polynomial):
            out = self.mul(out, element)
            out[0] += value
        return out


def charpoly_integral(matrix):
    """Return ascending coefficients and the exact Newton divisibility data."""
    n = len(matrix)
    assert n == 6 and all(len(row) == n for row in matrix)
    auxiliary = identity(n)
    descending = [1]
    traces = []
    for k in range(1, n + 1):
        product = matmul(matrix, auxiliary)
        trace = sum(product[i][i] for i in range(n))
        assert trace % k == 0
        coefficient = -trace // k
        traces.append({"order": k, "trace": str(trace),
                       "coefficient": str(coefficient), "exact_divisibility_verified": True})
        descending.append(coefficient)
        auxiliary = add_diagonal(product, coefficient)
    assert auxiliary == zero(n)
    return list(reversed(descending)), traces


class Source:
    def __init__(self, config, retained):
        self.item = config["source"]
        self.folder = Path(retained) / "R791"
        self.identity = source_identity(self.item)
        for name, row in self.item["files"].items():
            assert name == row["file"]
            bound(self.folder, row)
        manifest = read(self.folder / "full-outputs-manifest.json")
        assert sha(self.folder / "full-outputs-manifest.json") == self.item["manifest_sha256"]
        entries = {row["file"]: plain(row) for row in manifest["files"]}
        assert len(entries) == len(manifest["files"])
        for name, row in self.item["files"].items():
            if name != "full-outputs-manifest.json":
                assert entries[name] == plain(row)
        self.certificate = self.stage(self.item["certificate"])
        self.configuration = self.certificate["configuration"]
        run = read(self.folder / "run-receipt.json")
        public = read(self.folder / "public-actions-input.json")
        core = read(self.folder / "core-receipt.json")
        assert str(run["workflow_run_id"]) == str(self.item["run_id"])
        assert run["source_commit"] == public["source_commit"] == self.item["source_commit"]
        assert run["complete"] is True and run["process_exit_code"] == 0
        assert core["complete"] is True and core["certificate_sha256"] == self.item["certificate"]["sha256"]
        assert self.configuration["source_sha256"] == self.item["core_sha256"]
        assert self.configuration["p"] == 41

    def stage(self, row):
        row = plain(row)
        assert self.item["files"][row["file"]] == row
        value = read(bound(self.folder, row))
        assert value["complete"] is True and value["result"] == self.item["result"]
        assert fingerprint(value["configuration"]) == self.item["configuration_sha256"]
        return value


class Job:
    def __init__(self, args):
        self.args = args
        self.started = time.monotonic()
        self.deadline = self.started + args.budget_minutes * 60
        self.config = read(args.config)
        assert self.config["result"] == RESULT and self.config["p"] == 41
        assert self.config["core_sha256"] == sha(__file__)
        assert sha(args.proof) == self.config["proof"]["sha256"]
        self.output = Path(args.output)
        self.output.mkdir(parents=True, exist_ok=True)
        self.source = Source(self.config, args.retained)
        self.hom = self.source.stage(self.config["inputs"]["galois"])
        self.descent = self.source.stage(self.config["inputs"]["polarization"])
        assert self.hom["configuration"] == self.descent["configuration"] == self.source.configuration
        assert self.hom["gamma_order"] == 21 and self.hom["gamma_seventh_power"] == "zeta^2"
        assert self.hom["remaining_elliptic_factor_included"] is False
        assert self.descent["selected_real_map_degree"] == "3618"
        assert self.descent["unknown_original_kappa_set_to_one"] is False
        assert self.descent["original_vdagger_v_replaced_by_scalar"] is False
        assert self.descent["original_q_alpha_or_c1_changed"] is False
        assert self.descent["all_original_F0_directions_covered"] is True
        self.tag = {
            "result": RESULT, "source_sha256": self.config["core_sha256"],
            "p": 41, "proof": self.config["proof"], "strategy": STRATEGY,
            "source_identity": self.source.identity,
            "carrier_identity": self.config["carrier_identity"],
            "inputs": self.config["inputs"],
        }

    def budget(self):
        if time.monotonic() >= self.deadline:
            raise BudgetStop("Budget ended between complete original-source stages.")

    def cached(self, name):
        path = self.output / (PREFIX + name + ".json.gz")
        if not path.exists():
            return None
        value = read(path)
        assert value["complete"] is True and value["result"] == RESULT
        assert value["configuration"] == self.tag
        return value

    def put(self, name, data):
        path = self.output / (PREFIX + name + ".json.gz")
        value = {"result": RESULT, "configuration": self.tag, "complete": True, **data}
        if path.exists():
            assert read(path) == value
        else:
            atomic(path, value)
        return value

    def stage_spec(self, name):
        return spec(self.output / (PREFIX + name + ".json.gz"))

    def audit(self):
        name = "source-audit"
        old = self.cached(name)
        if old is not None:
            return old
        self.budget()
        return self.put(name, {
            "source_identity": self.source.identity,
            "original_certificate": self.config["source"]["certificate"],
            "original_galois": self.config["inputs"]["galois"],
            "original_polarization": self.config["inputs"]["polarization"],
            "unchanged_original_source_bytes_verified": True,
            "original_source_configuration_preserved": True,
            "old_period_Hom_Gram_Galois_and_polarization_solves_repeated": False,
        })

    def norm_polynomial(self):
        name = "norm-polynomial"
        old = self.cached(name)
        if old is not None:
            return old
        self.budget()
        polynomial = [int(x) for x in self.hom["real_minimal_polynomial_ascending"]]
        assert polynomial == [1, -8, 8, 6, -6, -1, 1]
        coordinates = self.descent["kappa_times_vdagger_v_in_real_Chebyshev_basis"]
        assert len(coordinates) == 6
        integers = []
        for numerator, denominator in coordinates:
            assert int(denominator) == 1
            integers.append(int(numerator))
        assert integers == [3870, 711, -801, -360, 612, 864]
        field = ExactField(polynomial)
        s = [[2], [0, 1]]
        for _ in range(1, 5):
            s.append(polyadd([0] + s[-1], [-x for x in s[-2]]))
        a = [integers[0]]
        for j in range(1, 6):
            a = polyadd(a, [integers[j] * x for x in s[j]])
        a = field.canonical(a)
        columns = [field.mul(a, [int(i == j) for i in range(6)]) for j in range(6)]
        matrix = [list(row) for row in zip(*columns)]
        coefficients, traces = charpoly_integral(matrix)
        assert coefficients[-1] == 1 and coefficients[0] > 0
        assert field.evaluate(coefficients, a) == [0] * 6
        denominator = coefficients[0]
        inverse_polynomial_numerator = [-x for x in coefficients[1:]]
        inverse_numerator = field.evaluate(inverse_polynomial_numerator, a)
        assert field.mul(a, inverse_numerator) == [denominator, 0, 0, 0, 0, 0]
        return self.put(name, {
            "source_audit": self.stage_spec("source-audit"),
            "field_minimal_polynomial_ascending": [str(x) for x in polynomial],
            "aA_original_Chebyshev_coordinates": coordinates,
            "aA_power_basis": [str(x) for x in a],
            "multiplication_matrix": [[str(x) for x in row] for row in matrix],
            "P_A_ascending": [str(x) for x in coefficients],
            "d_A": str(denominator), "d_A_positive_integer": True,
            "Faddeev_LeVerrier_exact_traces": traces,
            "full_Cayley_Hamilton_in_original_field_verified": True,
            "aA_inverse_numerator_power_basis": [str(x) for x in inverse_numerator],
            "aA_inverse_denominator": str(denominator),
            "inverse_polynomial_numerator_ascending": [str(x) for x in inverse_polynomial_numerator],
            "full_aA_times_inverse_numerator_equals_dA_verified": True,
            "aA_primitiveness_assumed": False,
            "d_A_claimed_minimal": False,
            "kappa_or_vdagger_v_replaced_by_one": False,
        })

    def old_matrix_action(self, norm):
        name = "completed-Hom-matrix-action"
        old = self.cached(name)
        if old is not None:
            assert old["norm_polynomial"] == self.stage_spec("norm-polynomial")
            return old
        self.budget()
        matrix = [[int(x) for x in row]
                  for row in self.descent["kappa_times_vdagger_v_Hom_matrix"]]
        assert len(matrix) == 12 and all(len(row) == 12 for row in matrix)
        polynomial = [int(x) for x in norm["P_A_ascending"]]
        d = int(norm["d_A"])
        assert matrix_polynomial(polynomial, matrix) == zero(12)
        multiple = [0] + [-x for x in polynomial[1:]]
        assert matrix_polynomial(multiple, matrix) == [
            [d * int(i == j) for j in range(12)] for i in range(12)]
        identity_polynomial = polyadd(polymul(multiple, multiple), [-d*x for x in multiple])
        relation_polynomial = [0] + polynomial
        assert remainder(identity_polynomial, relation_polynomial) == [0]
        return self.put(name, {
            "norm_polynomial": self.stage_spec("norm-polynomial"),
            "original_matrix_source": self.config["inputs"]["polarization"],
            "original_matrix_key": "kappa_times_vdagger_v_Hom_matrix",
            "matrix_shape": [12, 12],
            "P_A_of_original_E_exactly_zero": True,
            "integral_multiple_of_original_E_exactly_dA_identity": True,
            "full_polynomial_idempotence_mod_X_times_P_A_verified": True,
            "whole_JX_projection_not_inferred_only_from_12_Hom_rows": True,
            "whole_JX_equality_proof": self.config["proof"],
        })

    def correspondences(self, norm):
        name = "integral-correspondence-program"
        old = self.cached(name)
        if old is not None:
            assert old["norm_polynomial"] == self.stage_spec("norm-polynomial")
            return old
        self.budget()
        polynomial = [int(x) for x in norm["P_A_ascending"]]
        nodes = [{
            "id": "f_R", "op": "original_integral_Hom",
            "source": self.config["inputs"]["polarization"],
            "key": "selected_real_map_Hom_coordinates",
            "original_recipe": self.descent["selected_real_map_recipe"],
            "original_degree": self.descent["selected_real_map_degree"],
            "basepoint": "c0 maps to O",
        }]
        summands = []
        for j in range(7):
            nodes.append({
                "id": "h_" + str(j), "op": "original_T_power_of_Hom",
                "input": "f_R", "exponent": j,
                "source": self.config["inputs"]["galois"], "matrix_key": "gamma_matrix",
                "T_seventh_power": "[zeta^2]",
                "target_transport_preserves_original_O_and_principal_polarization": True,
            })
            summand = "pull_push_" + str(j)
            nodes.append({
                "id": summand, "op": "original_finite_correspondence_pull_push",
                "map": "h_" + str(j),
                "operator_direction": "h^* after h_* on the original Jacobian",
                "cycle": "X fiber-product over the original elliptic target with X",
                "scheme_multiplicities_preserved": True,
                "explicit_fiber_product_equations_materialized": False,
            })
            summands.append(summand)
        nodes.append({
            "id": "D_A", "op": "sum_of_integral_correspondences",
            "inputs": summands, "original_identity": "q_R^dagger*q_R",
            "defined_over_Q": True, "Rosati_self_adjoint": True,
        })
        nodes.append({
            "id": "F_A", "op": "integral_polynomial_in_correspondence", "input": "D_A",
            "coefficients_ascending": ["0"] + [str(-x) for x in polynomial[1:]],
            "scalar_d_A": norm["d_A"],
        })
        nodes.append({
            "id": "epsilon_A", "op": "rational_scalar_multiple",
            "input": "F_A", "scalar": ["1", norm["d_A"]],
            "original_identity": "q^dagger*kappa^(-1)*q",
        })
        outputs = []
        for item in self.descent["degree_zero_basis"]:
            j = item["j"]
            numerator, denominator = map(int, item["degree_zero_coefficient_dj_over_d0"])
            p, q = 2*denominator+numerator, denominator
            assert 1 <= j <= 5 and p > 0 and q > 0
            name = "integral_h_" + str(j)
            nodes.append({
                "id": name, "op": "original_symmetric_correspondence_difference",
                "first": {"coefficient": str(q), "operator":
                          "q_R^dagger*(1+T^j)^dagger*(1+T^j)*q_R", "j": j},
                "second": {"coefficient": str(-p), "operator": "D_A"},
                "original_identity": "q_j*q^dagger*h_j*q",
                "original_degree_zero_basis_source": self.config["inputs"]["polarization"],
                "original_degree_zero_basis_index": j-1,
                "individual_g_R_Lplus_definition_assumed": False,
                "symmetric_operator_defined_over_Q": True,
            })
            outputs.append({"j": j, "p": str(p), "q": str(q), "node": name})
        return self.put(name, {
            "norm_polynomial": self.stage_spec("norm-polynomial"),
            "completed_Hom_matrix_action": self.stage_spec("completed-Hom-matrix-action"),
            "nodes": nodes, "node_count": len(nodes),
            "outputs": {"integer_multiple": "F_A", "canonical_projector": "epsilon_A",
                        "five_original_symmetric_correspondences": outputs},
            "original_kappa_and_polarizations_preserved": True,
            "original_phi_prym_identity": "epsilon_A*phi^*=0; phi_*epsilon_A=0",
            "this_is_the_Y_active_Hecke_projector": False,
            "all_correspondence_cycles_have_finite_original_map_recipes": True,
            "all_fiber_product_equations_materialized": False,
            "global_Hecke_calibration_or_non_p_height_computed": False,
        })

    def finish(self):
        rows = []
        for path in sorted(self.output.glob(PREFIX + "*.json.gz")):
            if path.name.startswith(PREFIX + "stage-manifest-"):
                continue
            value = read(path)
            assert value["complete"] is True and value["configuration"] == self.tag
            rows.append(spec(path))
        assert len(rows) == 4
        digest = fingerprint(rows)
        name = PREFIX + "stage-manifest-" + digest + ".json.gz"
        atomic(self.output / name, {
            "result": RESULT, "complete": True, "configuration": self.tag,
            "files": rows, "completed_math_stage_count": len(rows),
            "only_new_mathematical_stages_listed": True,
        })
        norm = self.cached("norm-polynomial")
        cert = {
            "result": RESULT, "complete": True, "configuration": self.tag,
            "source_audit": self.stage_spec("source-audit"),
            "norm_polynomial": self.stage_spec("norm-polynomial"),
            "completed_Hom_matrix_action": self.stage_spec("completed-Hom-matrix-action"),
            "integral_correspondence_program": self.stage_spec("integral-correspondence-program"),
            "stage_manifest": spec(self.output / name), "completed_math_stage_count": 4,
            "actual_d_A": norm["d_A"],
            "original_canonical_A_Rosati_projector_as_expression_certified": True,
            "actual_positive_integer_multiple_and_norm_polynomial_computed": True,
            "original_full_12_Hom_matrix_action_verified": True,
            "original_whole_JX_equality_bound_to_proof": True,
            "original_five_symmetric_correspondence_recipes_preserved": True,
            "original_kappa_or_polarization_changed": False,
            "Y_active_Hecke_projector_computed": False,
            "Y_torsion_clearing_N_computed": False,
            "non_p_height_support_or_values_computed": False,
            "actual_height_computed": False, "height_nonzero_proved": False,
            "old_Hom_Gram_Galois_or_period_computations_repeated": False,
            "all_p_uniformity_proved": False,
            "seconds": time.monotonic() - self.started,
        }
        atomic(self.output / FINAL, cert)
        return cert

    def run(self):
        self.audit()
        norm = self.norm_polynomial()
        self.old_matrix_action(norm)
        self.correspondences(norm)
        return self.finish()


def main():
    assert os.environ.get("GITHUB_ACTIONS") == "true"
    assert os.environ.get("GITHUB_REPOSITORY") == REPOSITORY
    if hasattr(sys, "set_int_max_str_digits"):
        sys.set_int_max_str_digits(0)
    parser = argparse.ArgumentParser()
    for flag in ("config", "proof", "retained", "output"):
        parser.add_argument("--" + flag, required=True)
    parser.add_argument("--budget-minutes", type=float, required=True)
    args = parser.parse_args()
    assert 0 < args.budget_minutes <= 300
    output = Path(args.output)
    output.mkdir(parents=True, exist_ok=True)
    started = time.monotonic()
    job, cert, error, code = None, None, None, 1
    try:
        job = Job(args)
        cert = job.run()
        code = 0
    except BudgetStop as exc:
        error, code = str(exc), 124
    except Exception:
        error = traceback.format_exc()
        print(error, flush=True)
    receipt = {
        "result": RESULT, "source_sha256": sha(__file__),
        "complete": code == 0, "process_exit_code": code, "error": error,
        "configuration": None if job is None else job.tag,
        "certificate_sha256": None if cert is None else sha(output / FINAL),
        "seconds": time.monotonic() - started,
    }
    atomic(output / "core-receipt.json", receipt)
    print("R862_PROJECTOR_CORE_RECEIPT=" + json.dumps(receipt, sort_keys=True), flush=True)
    return code


if __name__ == "__main__":
    raise SystemExit(main())
