#!/usr/bin/env python3
"""Original 20-cusp evaluation kernel; new exact arithmetic only in Actions."""
import argparse
from fractions import Fraction as Q
import gzip
import hashlib
import json
import os
from pathlib import Path
import sys
import time
import traceback

RESULT = "R864-original-canonical-cusp-kernel"
FINAL = "p41-original-canonical-cusp-kernel-certificate.json"
PREFIX = "R864-"
BASE = ("result", "run_id", "source_commit", "core_sha256", "manifest_sha256")
PROOF_KEYS = ("R805", "R814", "R820", "R860", "FM")
EPS = [0] + [1] * 144 + [2] * 127
SOURCE_DEFINITIONS = {
    "R805": {"result": "R805-original-affine-pencil-free-basis",
        "core_sha256": "730a7d8f51d76d1153386c63f2e082285ada4573a2baf8d87d1825d3ce75b420",
        "certificate": "p41-original-affine-pencil-free-basis-certificate.json", "count": 7},
    "R820": {"result": "R820-original-cusp-finite-algebra-and-ideals",
        "core_sha256": "25f5582ed0c6dae2cf29d5eb288469067c09d917bfe1f565fb042978ea9b173c",
        "certificate": "p41-original-cusp-finite-algebra-ideals-certificate.json", "count": 9},
}
STRATEGY = {
    "scope": "complete_original_K_holomorphic_differential_basis",
    "cusp_finite_algebra_degree": 20, "domain_dimension": 146,
    "domain_order": "1,z,beta_1,...,beta_144",
    "expected_exact_rank": 19, "expected_kernel_dimension": 127,
    "normal_basis_rank": 272, "original_sigma_V1_indices": [1, 73],
    "original_sigma_coefficients": [1, 1], "original_tau_V1_index": 0,
    "tau_matrix_columns": "E_0,alpha,E_1,...,E_144",
    "sigma_matrix_columns": "alpha_inverse,E_0,E_sigma_1,...,E_sigma_144",
    "sigma_regularity_test": "v*f belongs to original C_sigma",
    "original_nu": "82*tau*dqY/qY", "kernel_check_column_block_size": 8,
    "exact_arithmetic": "Python_Fraction_no_modular_reconstruction",
    "canonical_free_rows_identity": True,
    "original_Q_semilinear_fixed_basis_computed": False,
    "only_transport_resume_budget_directories_excluded_from_mathematical_identity": True,
}


def sha(path):
    h = hashlib.sha256()
    with Path(path).open("rb") as f:
        for b in iter(lambda: f.read(4 * 1024 * 1024), b""):
            h.update(b)
    return h.hexdigest()


def read(path):
    path = Path(path)
    with (gzip.open(path, "rt") if path.suffix == ".gz" else path.open()) as f:
        return json.load(f)


def fingerprint(value):
    return hashlib.sha256(json.dumps(value, sort_keys=True, separators=(",", ":")).encode()).hexdigest()


def save(path, value):
    path = Path(path)
    tmp = path.with_name(path.name + ".tmp")
    data = (json.dumps(value, sort_keys=True, separators=(",", ":")) + "\n").encode()
    if path.suffix == ".gz":
        with tmp.open("wb") as f:
            with gzip.GzipFile(filename="", mode="wb", fileobj=f, mtime=0) as g:
                g.write(data)
    else:
        tmp.write_bytes(data)
    tmp.replace(path)


def plain(value):
    row = {key: value[key] for key in ("file", "bytes", "sha256")}
    assert Path(row["file"]).name == row["file"] and "\\" not in row["file"]
    return row


def spec(path):
    path = Path(path)
    return {"file": path.name, "bytes": path.stat().st_size, "sha256": sha(path)}


def bound(folder, value):
    value = plain(value)
    path = Path(folder) / value["file"]
    assert spec(path) == value, path.name
    return path


def identity(source):
    return {key: source[key] for key in BASE}


def source_identity(source):
    return {**identity(source), "certificate": plain(source["certificate"]),
        "configuration_sha256": source["configuration_sha256"],
        "selected_files_sha256": fingerprint(source["files"]),
        "selected_file_count": len(source["files"])}


def expected_tag(item):
    return {"result": RESULT, "source_sha256": item["core_sha256"], "p": 41,
        "arithmetic": "stdlib_exact_rational_cusp_kernel",
        "proofs_sha256": {key: item["proofs"][key]["sha256"] for key in PROOF_KEYS},
        "method_sha256": item["method_sha256"],
        "sources": {key: source_identity(item["sources"][key]) for key in sorted(SOURCE_DEFINITIONS)},
        "normal_basis_degrees": EPS, "strategy": STRATEGY}


def rational(value):
    assert isinstance(value, list) and len(value) == 2
    n, d = map(int, value)
    assert d > 0
    q = Q(n, d)
    assert q.numerator == n and q.denominator == d
    return q


def pair(value):
    return [str(value.numerator), str(value.denominator)]


def decode(matrix):
    return [[rational(x) for x in row] for row in matrix]


def encode(matrix):
    return [[pair(x) for x in row] for row in matrix]


def determinant(matrix):
    a = [row[:] for row in matrix]
    n, value = len(a), Q(1)
    assert all(len(row) == n for row in a)
    for k in range(n):
        pivot = next((i for i in range(k, n) if a[i][k]), None)
        assert pivot is not None, "Saved original minor is singular"
        if pivot != k:
            a[k], a[pivot] = a[pivot], a[k]
            value = -value
        t = a[k][k]
        value *= t
        for i in range(k + 1, n):
            if not a[i][k]:
                continue
            q = a[i][k] / t
            for j in range(k + 1, n):
                a[i][j] -= q * a[k][j]
            a[i][k] = Q(0)
    return value


class BudgetStop(Exception):
    pass


class Job:
    def __init__(self, item, out, minutes):
        self.item, self.out = item, Path(out)
        self.out.mkdir(parents=True, exist_ok=True)
        self.started = time.monotonic()
        self.deadline = self.started + 60 * minutes
        assert item["result"] == RESULT and item["p"] == 41
        assert item["core_sha256"] == sha(__file__)
        assert set(item["proofs"]) == set(PROOF_KEYS)
        for value in item["proofs"].values():
            assert sha(value["path"]) == value["sha256"]
        assert sha(item["method"]) == item["method_sha256"]
        assert set(item["sources"]) == set(SOURCE_DEFINITIONS)
        self.tag = expected_tag(item)
        self.certificates = {}
        for label, source in item["sources"].items():
            definition = SOURCE_DEFINITIONS[label]
            assert source["result"] == definition["result"]
            assert source["core_sha256"] == definition["core_sha256"]
            assert len(source["files"]) == definition["count"]
            for name, value in source["files"].items():
                assert name == value["file"]
                bound(source["directory"], value)
            cert = read(bound(source["directory"], source["certificate"]))
            assert cert["complete"] is True and cert["result"] == source["result"]
            assert cert["configuration"]["source_sha256"] == source["core_sha256"]
            assert fingerprint(cert["configuration"]) == source["configuration_sha256"]
            self.certificates[label] = cert

    def budget(self):
        if time.monotonic() >= self.deadline:
            raise BudgetStop("runtime budget reached at an atomic stage boundary")

    def source_stage(self, label, reference):
        source = self.item["sources"][label]
        reference = plain(reference)
        assert source["files"][reference["file"]] == reference
        data = read(bound(source["directory"], reference))
        assert data["complete"] is True
        assert data["configuration"] == self.certificates[label]["configuration"]
        return data

    def load(self, name):
        path = self.out / (PREFIX + name + ".json.gz")
        if not path.exists():
            return None
        value = read(path)
        assert value["complete"] is True and value["result"] == RESULT
        assert value["configuration"] == self.tag
        return value

    def put(self, name, value):
        assert self.load(name) is None
        path = self.out / (PREFIX + name + ".json.gz")
        save(path, {"result": RESULT, "configuration": self.tag, "complete": True, **value})
        print("R864_STAGE=" + name, flush=True)
        return spec(path)

    def ref(self, name):
        assert self.load(name) is not None
        return spec(self.out / (PREFIX + name + ".json.gz"))

    def source_audit(self):
        if self.load("source-audit"):
            return
        c805, c820 = self.certificates["R805"], self.certificates["R820"]
        assert identity(c820["actual_input_producers"]["R805"]) == identity(self.item["sources"]["R805"])
        assert c820["actual_input_producers"]["R805"]["certificate_sha256"] == self.item["sources"]["R805"]["certificate"]["sha256"]
        free = self.source_stage("R805", c805["graded_free_basis_stage"])
        pencil = self.source_stage("R805", c805["pencil_stage"])
        assert free["degree_distribution"] == [1, 144, 127]
        assert free["degree1_original_indices"] == list(range(2, 146))
        assert free["degree1_change_of_basis_determinant"] == 1
        assert free["characteristic_zero_complement_certified"] is True
        assert pencil["n"] == 1 and pencil["original_tau_index"] == 0
        assert pencil["original_sigma_indices"] == [1, 73]
        assert pencil["original_sigma_integer_coefficients"] == [1, 1]
        assert pencil["basepoint_free_certified_by_actual_unit_minor"] is True
        assert c820["normal_basis_degrees"] == EPS and c820["normal_basis_rank"] == 272
        assert c820["finite_field_degree"] == 20 and c820["actual_cusp_colengths"] == {"sigma": 20, "tau": 20}
        assert c820["complete_polynomial_kernels_certified"] is True
        assert c820["same_original_cusp_field_and_two_chart_transitions_verified"] is True
        face = self.source_stage("R820", c820["original_finite_algebra_interface"])
        for key in ("all_272_original_two_chart_evaluation_transitions_verified",
                    "all_base_multiplication_columns_verified_in_original_field",
                    "all_original_frames_and_cusp_conjugates_preserved",
                    "both_original_nonzero_denominators_inverted_and_fully_multiplied_back",
                    "alpha_inverse_product_verified"):
            assert face[key] is True
        assert face["original_common_82_power_cancels_exactly"] == 6
        assert face["finite_field_degree"] == 20
        for chart, value in c820["two_chart_cusp_ideal_indexes"].items():
            index = self.source_stage("R820", value)
            for key in ("all_272_original_relations_verified_in_full_finite_algebra",
                        "complete_polynomial_kernel_certified_by_inclusion_and_equal_colength",
                        "quotient_is_original_separable_cusp_field",
                        "reduced_cusp_multiplicity_one_at_all_20_geometric_cusps"):
                assert index[key] is True
            assert plain(index["source_field_interface"]) == plain(c820["original_finite_algebra_interface"])
        self.put("source-audit", {"source_identities": self.tag["sources"],
            "selected_original_file_count": 16,
            "original_finite_algebra_interface": c820["original_finite_algebra_interface"],
            "original_free_basis": c805["graded_free_basis_stage"],
            "original_pencil": c805["pencil_stage"],
            "all_20_geometric_cusps_in_both_charts_certified_by_original_source": True,
            "old_cusp_ideal_or_inverse_or_W_or_Fourier_arithmetic_recomputed": False})

    def matrices(self):
        if self.load("evaluation-matrices"):
            return
        self.budget()
        face = self.source_stage("R820", self.certificates["R820"]["original_finite_algebra_interface"])
        ev = face["evaluation_vectors"]
        assert set(ev) == {"tau", "sigma"}
        for chart in ev:
            assert len(ev[chart]) == 272 and all(len(x) == 20 for x in ev[chart])
        one = [Q(1)] + [Q(0)] * 19
        assert [rational(x) for x in ev["tau"][0]] == one
        assert [rational(x) for x in ev["sigma"][0]] == one
        tau_cols = [ev["tau"][0], face["alpha"], *ev["tau"][1:145]]
        sigma_cols = [face["alpha_inverse"], ev["sigma"][0], *ev["sigma"][1:145]]
        matrices = {chart: [[columns[j][i] for j in range(146)] for i in range(20)]
                    for chart, columns in (("tau", tau_cols), ("sigma", sigma_cols))}
        for matrix in matrices.values():
            decode(matrix)
        self.put("evaluation-matrices", {"source_audit": self.ref("source-audit"),
            "row_count": 20, "column_count": 146, "matrices": matrices,
            "source_original_interface": self.certificates["R820"]["original_finite_algebra_interface"],
            "domain_order": STRATEGY["domain_order"],
            "sigma_matrix_evaluates_v_times_tau_function": True,
            "original_82_integer_scales_reinserted": False})

    def eliminate(self):
        if self.load("rref-index"):
            return
        source = self.ref("evaluation-matrices")
        matrix = decode(self.load("evaluation-matrices")["matrices"]["tau"])
        labels, pivots, pvalues, column, previous = list(range(20)), [], [], 0, None
        for k in range(20):
            value = self.load("rref-step-%02d" % k)
            if value is None:
                break
            assert value["step"] == k and value["source_matrix"] == source
            assert value["previous_step"] == previous
            assert len(value["pivot_columns"]) == k + 1
            matrix = decode(value["matrix"])
            labels, pivots = value["original_row_labels"], value["pivot_columns"]
            pvalues = [rational(x) for x in value["pivot_values"]]
            column, previous = value["next_column"], self.ref("rref-step-%02d" % k)
        while column < 146 and len(pivots) < 20:
            self.budget()
            k = len(pivots)
            chosen = next((i for i in range(k, 20) if matrix[i][column]), None)
            if chosen is None:
                column += 1
                continue
            matrix[k], matrix[chosen] = matrix[chosen], matrix[k]
            labels[k], labels[chosen] = labels[chosen], labels[k]
            pivot = matrix[k][column]
            matrix[k] = [x / pivot for x in matrix[k]]
            for i in range(20):
                if i == k or not matrix[i][column]:
                    continue
                scalar = matrix[i][column]
                matrix[i] = [x - scalar * y for x, y in zip(matrix[i], matrix[k])]
            pivots.append(column)
            pvalues.append(pivot)
            column += 1
            name = "rref-step-%02d" % k
            previous = self.put(name, {"step": k, "source_matrix": source,
                "previous_step": previous, "matrix": encode(matrix),
                "original_row_labels": labels[:], "pivot_columns": pivots[:],
                "pivot_values": [pair(x) for x in pvalues], "next_column": column,
                "all_elimination_operations_exact": True})
        rank = len(pivots)
        assert rank == 19, ("Actual cusp evaluation rank", rank)
        assert all(not x for row in matrix[rank:] for x in row)
        for k, col in enumerate(pivots):
            assert all(matrix[i][col] == (1 if i == k else 0) for i in range(20))
        original = decode(self.load("evaluation-matrices")["matrices"]["tau"])
        minor = [[original[i][j] for j in pivots] for i in labels[:rank]]
        det = determinant(minor)
        assert det
        product = Q(1)
        for q in pvalues:
            product *= q
        assert det == product
        self.put("rref-index", {"source_matrix": source, "last_step": previous,
            "actual_rank": rank, "pivot_columns": pivots, "original_minor_rows": labels[:rank],
            "original_minor_columns": pivots, "original_minor_matrix": encode(minor),
            "actual_exact_nonzero_minor_determinant": pair(det),
            "determinant_equals_original_elimination_pivot_product": True,
            "all_remaining_rows_exactly_zero": True})

    def kernel(self):
        if self.load("kernel"):
            return
        self.budget()
        index = self.load("rref-index")
        data = read(bound(self.out, index["last_step"]))
        reduced = decode(data["matrix"])
        pivots = index["pivot_columns"]
        free = [i for i in range(146) if i not in pivots]
        assert len(free) == 127
        kernel = [[Q(0)] * 127 for _ in range(146)]
        for j, col in enumerate(free):
            kernel[col][j] = Q(1)
            for k, pivot in enumerate(pivots):
                kernel[pivot][j] = -reduced[k][col]
        assert all(kernel[i][j] == (1 if k == j else 0)
                   for k, i in enumerate(free) for j in range(127))
        self.put("kernel", {"source_rref": self.ref("rref-index"),
            "actual_rank": 19, "kernel_dimension": 127,
            "kernel_matrix": encode(kernel), "kernel_free_rows": free,
            "all_free_rows_identity_verified": True})

    def checks(self):
        source = self.ref("kernel")
        kernel = decode(self.load("kernel")["kernel_matrix"])
        matrices = {key: decode(value) for key, value in self.load("evaluation-matrices")["matrices"].items()}
        for first in range(0, 127, 8):
            stop = min(127, first + 8)
            name = "full-two-chart-check-%03d-%03d" % (first, stop)
            if self.load(name):
                continue
            self.budget()
            for chart, matrix in matrices.items():
                for i in range(20):
                    for j in range(first, stop):
                        value = sum((matrix[i][k] * kernel[k][j]
                                     for k in range(146) if kernel[k][j] and matrix[i][k]), Q(0))
                        assert value == 0, (chart, i, j)
            self.put(name, {"source_kernel": source, "source_matrices": self.ref("evaluation-matrices"),
                "first_kernel_column": first, "stop_kernel_column": stop,
                "full_coordinate_rows_per_chart": 20, "actual_checked_charts": ["tau", "sigma"],
                "all_original_entries_exactly_zero": True})

    def differential_basis(self):
        if self.load("holomorphic-basis"):
            return
        self.budget()
        kernel = decode(self.load("kernel")["kernel_matrix"])
        basis = []
        for j in range(127):
            a = [row[j] for row in kernel]
            original = a[:]
            original[73] += a[1]
            recovered = original[:]
            recovered[73] -= original[1]
            assert recovered == a
            tau, sigma = [], []
            for i in range(145):
                tc = [a[0], a[1]] if i == 0 else [a[i + 1]]
                sc = [a[1], a[0]] if i == 0 else [a[i + 1]]
                if any(tc):
                    tau.append({"normal_basis_index": i, "polynomial_low_to_high": [pair(x) for x in tc]})
                if any(sc):
                    sigma.append({"normal_basis_index": i, "polynomial_low_to_high": [pair(x) for x in sc]})
            basis.append({"basis_index": j, "original_V1_coefficients": [pair(x) for x in original],
                "tau_f_normal_polynomial": tau, "sigma_vf_normal_polynomial": sigma,
                "original_differential": "f*nu = 82*(original_V1_section)*dqY/qY"})
        checks = [self.ref("full-two-chart-check-%03d-%03d" % (i, min(127, i + 8))) for i in range(0, 127, 8)]
        self.put("holomorphic-basis", {"source_kernel": self.ref("kernel"),
            "source_free_basis": self.certificates["R805"]["graded_free_basis_stage"],
            "full_two_chart_checks": checks, "basis": basis,
            "actual_dimension_over_K": 127, "all_original_V1_coordinate_roundtrips_verified": True,
            "complete_original_K_holomorphic_basis_certified": True,
            "tau_functions_in_complete_original_C_tau": True,
            "sigma_v_times_functions_in_complete_original_C_sigma": True,
            "all_degree_two_normal_rows_zero": True,
            "source_rational_coordinates_imply_true_Q_descent": False,
            "original_Q_semilinear_fixed_basis_computed": False,
            "original_82_power_from_nu_only": 1})

    def finish(self, complete, reason):
        files = []
        for path in sorted(self.out.glob(PREFIX + "*.json.gz")):
            if path.name in ("R864-current.json.gz", "R864-exact-stages-manifest.json.gz"):
                continue
            value = read(path)
            assert value["result"] == RESULT and value["configuration"] == self.tag and value["complete"] is True
            files.append(spec(path))
        inventory = self.out / "R864-exact-stages-manifest.json.gz"
        save(inventory, {"result": RESULT, "configuration": self.tag, "complete": True,
            "files": files, "actual_complete_stage_count": len(files)})
        current = self.out / "R864-current.json.gz"
        save(current, {"result": RESULT, "configuration": self.tag, "complete": False,
            "scope_complete": complete, "stop_reason": reason,
            "source_mathematical_stage_manifest": spec(inventory)})
        rref, kernel, basis = self.load("rref-index"), self.load("kernel"), self.load("holomorphic-basis")
        if complete:
            assert basis and rref and kernel
        final = {"result": RESULT, "configuration": self.tag, "p": 41, "complete": complete,
            "stop_reason": reason, "source_audit": self.ref("source-audit") if self.load("source-audit") else None,
            "evaluation_matrices": self.ref("evaluation-matrices") if self.load("evaluation-matrices") else None,
            "rref_certificate": self.ref("rref-index") if rref else None,
            "kernel_certificate": self.ref("kernel") if kernel else None,
            "holomorphic_differential_basis": self.ref("holomorphic-basis") if basis else None,
            "actual_cusp_evaluation_rank": rref["actual_rank"] if rref else None,
            "actual_kernel_dimension": kernel["kernel_dimension"] if kernel else None,
            "complete_original_K_holomorphic_basis_certified": complete,
            "all20_cusps_and_both_original_charts_verified": complete,
            "original_Q_semilinear_fixed_basis_computed": False,
            "original_YP_meromorphic_RR_connections_or_periods_computed": False,
            "old_W_cusp_ideals_Fourier_or_three_conjugates_recomputed": False,
            "stage_manifest": spec(inventory), "resume_state": spec(current),
            "seconds": time.monotonic() - self.started}
        save(self.out / FINAL, final)
        return final

    def run(self):
        if (self.out / FINAL).exists():
            final = read(self.out / FINAL)
            assert final["configuration"] == self.tag and final["result"] == RESULT
            if final["complete"]:
                stages = read(bound(self.out, final["stage_manifest"]))
                for reference in stages["files"]:
                    bound(self.out, reference)
                return final
        self.source_audit()
        self.matrices()
        self.eliminate()
        self.kernel()
        self.checks()
        self.differential_basis()
        return self.finish(True, "complete")


def main():
    sys.set_int_max_str_digits(0)
    assert os.environ.get("GITHUB_ACTIONS") == "true", "New exact arithmetic is restricted to public Actions"
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--config", type=Path, required=True)
    parser.add_argument("--out", type=Path, required=True)
    parser.add_argument("--budget-minutes", type=float, required=True)
    args = parser.parse_args()
    args.out.mkdir(parents=True, exist_ok=True)
    job, final, code, error = None, None, 1, None
    try:
        job = Job(read(args.config), args.out, args.budget_minutes)
        final = job.run()
        code = 0
    except BudgetStop as exc:
        error = str(exc)
        final = job.finish(False, "budget")
        code = 124
    except Exception as exc:
        error = type(exc).__name__ + ": " + str(exc)
        traceback.print_exc()
        if job is not None:
            final = job.finish(False, "error")
    finally:
        save(args.out / "core-receipt.json", {"result": RESULT, "source_sha256": sha(__file__),
            "complete": code == 0, "process_exit_code": code, "error": error,
            "certificate_sha256": sha(args.out / FINAL) if final else None,
            "complete_original_K_holomorphic_basis_certified": code == 0,
            "actual_cusp_evaluation_rank": final["actual_cusp_evaluation_rank"] if final else None,
            "actual_kernel_dimension": final["actual_kernel_dimension"] if final else None,
            "original_Q_semilinear_fixed_basis_computed": False})
    if final is not None:
        print("R864_RESULT=" + json.dumps({key: final[key] for key in
            ("complete", "actual_cusp_evaluation_rank", "actual_kernel_dimension", "seconds")}), flush=True)
    raise SystemExit(code)


if __name__ == "__main__":
    main()
