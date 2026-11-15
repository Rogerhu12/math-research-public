#!/usr/bin/env python3
"""R794: exact finite selection of an original low-degree eta basis.

Read completed R791 operators/polarization and R759 maps.  New arithmetic is
only a twelve-dimensional CM-module calculation and a fixed 149-element
linear-matroid selection.  No period, Hom, SVP, function or height is rerun.
"""
import argparse
import gzip
import hashlib
import json
import os
from pathlib import Path
import sys
import time

import flint
from flint import fmpq, fmpq_mat, fmpq_poly

RESULT = "R794-original-low-degree-eta-basis"
FINAL = "p41-original-low-degree-eta-basis-certificate.json"
DIM, REAL, BASE_INDEX, BASE_DEGREE = 12, 6, 4, 1206
MATRICES = "R791-original-Hom-Galois-matrices.json.gz"
ETA = "R791-original-real-descent-and-eta-basis-inputs.json.gz"
MAPS = "R759-original-integral-maps-and-bounded-recovery-input.json.gz"
R791_CORE = "11068eb00caa71e9c8ed1ffba0277534a52f5cce3402a59b68c7d5d66a8b7a4d"
R759_CORE = "17403f45f74e03e5a138376068e64e54c9bf6b2622a7b91bb178747d407708e0"


def guard():
    if os.environ.get("GITHUB_ACTIONS") != "true" or \
       os.environ.get("GITHUB_REPOSITORY") != "Rogerhu12/math-research-public":
        raise SystemExit("New mathematical execution belongs to public repository Actions.")


def sha(path):
    value = hashlib.sha256()
    with Path(path).open("rb") as stream:
        for block in iter(lambda: stream.read(1024*1024), b""):
            value.update(block)
    return value.hexdigest()


def read(path):
    path = Path(path)
    opener = gzip.open if path.suffix == ".gz" else open
    with opener(path, "rt", encoding="utf-8") as stream:
        return json.load(stream)


def save(path, value):
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    raw = (json.dumps(value, sort_keys=True, separators=(",", ":"))+"\n").encode()
    temporary = path.with_name(path.name+".tmp")
    if path.suffix == ".gz":
        with temporary.open("wb") as stream:
            with gzip.GzipFile(filename="", fileobj=stream, mode="wb", mtime=0) as out:
                out.write(raw)
    else:
        temporary.write_bytes(raw)
    temporary.replace(path)


def spec(path):
    path = Path(path)
    return {"file": path.name, "bytes": path.stat().st_size, "sha256": sha(path)}


def eq(value):
    value = fmpq(value)
    return [str(value.numer()), str(value.denom())]


def dq(value):
    return fmpq(int(value[0]), int(value[1])) if isinstance(value, list) else fmpq(int(value))


def ep(value):
    return {"numerator": [str(x) for x in value.numer().coeffs()],
            "denominator": str(value.denom())}


def dp(value):
    return fmpq_poly([int(x) for x in value["numerator"]], int(value["denominator"]))


def em(A):
    return [[eq(A[i, j]) for j in range(A.ncols())] for i in range(A.nrows())]


def dm(value):
    return fmpq_mat([[dq(x) for x in row] for row in value])


def identity(n):
    return fmpq_mat([[int(i == j) for j in range(n)] for i in range(n)])


def columns(vectors):
    assert vectors
    return fmpq_mat([[v[i] for v in vectors] for i in range(len(vectors[0]))])


def independent_rows(A, required=None):
    pivots, selected = {}, []
    for i in range(A.nrows()):
        row = [A[i, j] for j in range(A.ncols())]
        for col in sorted(pivots):
            if row[col]:
                lead = row[col]
                row = [x-lead*y for x, y in zip(row, pivots[col])]
        if any(row):
            col = next(j for j, x in enumerate(row) if x)
            lead = row[col]
            pivots[col] = [x/lead for x in row]
            selected.append(i)
            if required is not None and len(selected) == required:
                break
    return selected


def rows(A, indices):
    return fmpq_mat([[A[i, j] for j in range(A.ncols())] for i in indices])


def vector_rank(vectors):
    if not vectors:
        return 0
    return len(independent_rows(columns(vectors).transpose()))


def ints(column):
    values = []
    for i in range(column.nrows()):
        q = column[i, 0]
        assert q.denom() == 1
        values.append(int(q.numer()))
    return values


class Job:
    def __init__(self, args):
        self.args, self.out = args, args.output
        self.out.mkdir(parents=True, exist_ok=True)
        self.started = time.monotonic()
        self.config = read(args.config)
        assert flint.__version__ == "0.9.0"
        assert self.config["result"] == RESULT and self.config["p"] == 41
        assert self.config["producer_inputs_pending"] is False
        assert self.config["core_sha256"] == sha(__file__)
        assert self.config["proof_sha256"] == sha(args.proof)
        assert self.config["candidate_set"] == "12 basis,66 sums,66 differences,5 old g_j caps"
        self.tag = {"result": RESULT, "p": 41, "source_sha256": sha(__file__),
                    "python_flint": flint.__version__, "proof_sha256": sha(args.proof),
                    "retained_artifacts": self.config["retained_artifacts"],
                    "candidate_set": self.config["candidate_set"]}
        data = {}
        assert set(self.config["retained_artifacts"]) == {"R791", "R759"}
        for label, producer in self.config["retained_artifacts"].items():
            directory = args.inputs/label
            manifest = read(directory/"full-outputs-manifest.json")
            assert sha(directory/"full-outputs-manifest.json") == producer["manifest_sha256"]
            assert manifest["result"] == producer["result"]
            entries = {row["file"]: row for row in manifest["files"]}
            group = {}
            for name, digest in producer["files"].items():
                assert Path(name).name == name
                path = directory/name
                assert sha(path) == digest == entries[name]["sha256"]
                assert path.stat().st_size == entries[name]["bytes"]
                group[name] = read(path)
            cert = group[producer["certificate_name"]]
            assert cert["complete"] is True
            tag = cert["configuration"]
            assert tag["source_sha256"] == producer["core_sha256"]
            assert tag["python_flint"] == "0.9.0"
            stages = {row["file"]: row for row in cert["stages"]}
            for name, value in group.items():
                if name != producer["certificate_name"]:
                    assert value["complete"] is True and value["configuration"] == tag
                    assert stages[name]["sha256"] == producer["files"][name]
            data[label] = group
        assert self.config["retained_artifacts"]["R791"]["core_sha256"] == R791_CORE
        assert self.config["retained_artifacts"]["R759"]["core_sha256"] == R759_CORE
        original, eta, maps = data["R791"][MATRICES], data["R791"][ETA], data["R759"][MAPS]
        assert original["gamma_order"] == 21 and original["gamma_seventh_power"] == "zeta^2"
        assert original["basis"] == "R759 unchanged twelve LLL integral maps, columns"
        assert original["all_84_coordinates_verified"] is True
        assert maps["selected_index"] == BASE_INDEX and maps["selected_degree"] == str(BASE_DEGREE)
        assert maps["Z_basis_rank"] == DIM and maps["O_K_rank"] == REAL
        assert original["twice_degree_Gram_matrix"] == maps["twice_degree_Gram_matrix"]
        assert original["zeta_matrix"] == maps["zeta_action_on_this_Z_basis"]
        assert eta["all_original_F0_directions_covered"] is True
        assert eta["unknown_original_kappa_set_to_one"] is False
        assert eta["original_vdagger_v_replaced_by_scalar"] is False
        self.T, self.Gram = dm(original["gamma_matrix"]), dm(original["twice_degree_Gram_matrix"])
        self.I = identity(DIM)
        self.Phi = fmpq_poly(original["Phi21_ascending"])
        assert self.Phi.degree() == DIM and self.Phi[DIM] == 1
        self.z = fmpq_poly([0, 1])
        self.zp = [fmpq_poly([1])]
        for _ in range(20):
            self.zp.append(self.zp[-1]*self.z % self.Phi)
        self.zstar = self.zp[20]
        self.real_basis = [self.zp[0]] + [self.zp[j]+self.zp[21-j] for j in range(1, 6)]
        self.real_matrix = columns([self.pvector(x) for x in self.real_basis])
        self.real_rows = independent_rows(self.real_matrix, REAL)
        assert len(self.real_rows) == REAL
        self.real_inverse = rows(self.real_matrix, self.real_rows).inv()
        self.f = fmpq_mat([[int(i == BASE_INDEX)] for i in range(DIM)])
        cyclic, current = [], self.f
        for _ in range(DIM):
            cyclic.append([current[i, 0] for i in range(DIM)])
            current = self.T*current
        self.cyclic = columns(cyclic)
        assert self.cyclic.det()
        self.cyclic_inverse = self.cyclic.inv()
        assert self.cyclic*self.cyclic_inverse == self.I
        e_coords = [dq(x) for x in eta["kappa_times_vdagger_v_in_real_Chebyshev_basis"]]
        assert len(e_coords) == REAL
        self.e = sum((value*poly for value, poly in zip(e_coords, self.real_basis)), fmpq_poly([]))
        assert self.matrix(self.e) == dm(eta["kappa_times_vdagger_v_Hom_matrix"])
        self.e_trace = self.trace_real(self.e)
        assert self.e_trace == int(eta["degree_E0"]) == 25326
        self.old_h = []
        for item in eta["degree_zero_basis"]:
            j = item["j"]
            ratio = dq(item["degree_zero_coefficient_dj_over_d0"])
            h = self.e*(self.real_basis[j]-ratio) % self.Phi
            assert self.matrix(h) == dm(item["kappa_times_original_hj_Hom_matrix"])
            self.old_h.append(self.real_coordinates(h))
        self.old_h_matrix = columns(self.old_h)
        assert vector_rank(self.old_h) == 5
        self.old_h_rows = independent_rows(self.old_h_matrix, 5)
        self.old_h_inverse = rows(self.old_h_matrix, self.old_h_rows).inv()
        self.original_vectors = maps["all_twelve_integral_map_differential_vectors_in_original_omega_basis"]
        assert len(self.original_vectors) == DIM and all(len(v) == REAL for v in self.original_vectors)
        self.old_eta_stage = eta

    def pvector(self, poly):
        return [poly[i] for i in range(DIM)]

    def matrix(self, poly):
        result = fmpq_mat(DIM, DIM)
        for coefficient in reversed(poly.coeffs()):
            result = result*self.T+coefficient*self.I
        return result

    def star(self, poly):
        result = fmpq_poly([])
        for coefficient in reversed(poly.coeffs()):
            result = (result*self.zstar+coefficient) % self.Phi
        return result

    def trace_real(self, poly):
        assert self.star(poly) == poly
        return ((poly*self.Phi.derivative()) % self.Phi)[DIM-1]/2

    def real_coordinates(self, poly):
        target = fmpq_mat([[poly[i]] for i in range(DIM)])
        value = self.real_inverse*rows(target, self.real_rows)
        assert self.real_matrix*value == target
        return [value[i, 0] for i in range(REAL)]

    def degree(self, vector):
        value = (vector.transpose()*self.Gram*vector)[0, 0]/2
        assert value.denom() == 1 and value > 0
        return int(value.numer())

    def store(self, name, payload):
        path = self.out/name
        save(path, dict(payload, result=RESULT, complete=True, configuration=self.tag))
        print(json.dumps({"stage": name, "complete": True, "sha256": sha(path)}), flush=True)
        return spec(path)

    def candidates(self):
        result = []
        unit = [fmpq_mat([[int(k == i)] for k in range(DIM)]) for i in range(DIM)]
        for i in range(DIM):
            result.append(("basis", [i], unit[i]))
        for i in range(DIM):
            for j in range(i+1, DIM):
                result.append(("sum", [i, j], unit[i]+unit[j]))
        for i in range(DIM):
            for j in range(i+1, DIM):
                result.append(("difference", [i, j], unit[i]-unit[j]))
        power = self.I
        for j in range(1, 6):
            power = power*self.T
            result.append(("old_g_cap", [j], self.f+power*self.f))
        assert len(result) == 149
        return result

    def map_differential(self, vector):
        """Only the NEW integer combination of retained old differential vectors."""
        coefficients = ints(vector)
        output = []
        for j in range(REAL):
            components = []
            for zeta_component in range(2):
                value = fmpq_poly([])
                for i, coefficient in enumerate(coefficients):
                    if coefficient:
                        value += coefficient*dp(self.original_vectors[i][j][zeta_component])
                components.append(ep(value))
            output.append(components)
        return output

    def run(self):
        records, real_vectors, h_vectors, originals = [], [], [], []
        for index, (kind, source_indices, vector) in enumerate(self.candidates()):
            coefficients = self.cyclic_inverse*vector
            assert self.cyclic*coefficients == vector
            a = fmpq_poly([coefficients[i, 0] for i in range(DIM)])
            norm = self.star(a)*a % self.Phi
            assert self.star(norm) == norm
            d = self.degree(vector)
            assert self.trace_real(self.e*norm % self.Phi) == 21*d
            ratio = fmpq(d, BASE_DEGREE)
            centered = norm-ratio
            h = self.e*centered % self.Phi
            assert self.trace_real(h) == 0
            nr, cr, hr = (self.real_coordinates(poly) for poly in (norm, centered, h))
            real_vectors.append(cr)
            h_vectors.append(hr)
            originals.append(vector)
            records.append({"candidate_index": index, "kind": kind, "source_indices": source_indices,
                "original_Hom_integer_column": [str(v) for v in ints(vector)], "map_degree": str(d),
                "a_in_Q_T_mod_Phi21": [eq(a[i]) for i in range(DIM)],
                "norm_in_original_real_basis": [eq(v) for v in nr],
                "degree_ratio_to_original_f4": eq(ratio),
                "centered_norm_in_original_real_basis": [eq(v) for v in cr],
                "kappa_times_h_in_original_real_basis": [eq(v) for v in hr],
                "actual_original_weighted_trace_identity_verified": True})
        base_rank = vector_rank(real_vectors[:12])
        sum_rank = vector_rank(real_vectors[:78])
        all_rank = vector_rank(real_vectors)
        assert sum_rank == all_rank == 5
        selected, selected_vectors = [], []
        for index in sorted(range(len(records)), key=lambda i: (int(records[i]["map_degree"]), i)):
            candidate = real_vectors[index]
            if vector_rank(selected_vectors+[candidate]) > len(selected_vectors):
                selected.append(index)
                selected_vectors.append(candidate)
                if len(selected) == 5:
                    break
        assert len(selected) == 5
        selected_h = columns([h_vectors[i] for i in selected])
        minor_rows = independent_rows(selected_h, 5)
        minor = rows(selected_h, minor_rows)
        assert minor.det()
        change = self.old_h_inverse*rows(selected_h, self.old_h_rows)
        assert self.old_h_matrix*change == selected_h and change.det()
        inverse_change = change.inv()
        assert change*inverse_change == identity(5)
        selected_records = []
        for index in selected:
            row = dict(records[index])
            d = int(row["map_degree"])
            ordinary_power = (d+254+271)//272
            residual = 272*ordinary_power-d
            conditions = (272*ordinary_power+d)//20+1
            assert 254 <= residual <= 525
            row["original_omega_differential_coordinates"] = self.map_differential(originals[index])
            row["differential_coordinate_basis"] = "R759 original b^0..b^6 in 1,zeta for each R745 omega_0..omega_5"
            row["R793_exact_engineering_bounds"] = {
                "ordinary_section_power": ordinary_power, "residual_divisor_degree": residual,
                "complete_Laurent_conditions": conditions, "Laurent_exponents": [-1, conditions-2],
                "basis_highest_qY_exponent": conditions-1, "pole_ideal_dimension": residual-126,
                "residual_V3_ideal_dimension": 690-residual, "two_section_IGS_rank": 690+residual,
                "point_padding_degree": 544-residual, "all_cusp_pole_orders": 1,
                "e_one_source": "R793 theorem793.4, original irreducible Hom and cusp orbit"}
            selected_records.append(row)
        first = self.store("R794-original-CM-module-and-finite-norm-candidates.json.gz", {
            "cyclic_basis": "T^k*f4, k=0..11; original R791 column action",
            "cyclic_basis_matrix": em(self.cyclic), "cyclic_basis_determinant": eq(self.cyclic.det()),
            "Phi21_ascending": [str(v) for v in self.Phi.coeffs()],
            "real_basis": ["1"]+["T^"+str(j)+"+T^-"+str(j) for j in range(1, 6)],
            "real_basis_pivot_rows": self.real_rows,
            "actual_basis_only_centered_rank": base_rank, "actual_basis_and_sums_centered_rank": sum_rank,
            "actual_all_candidates_centered_rank": all_rank, "candidate_count": len(records),
            "candidates": records, "finite_candidate_coverage_proved": True,
            "old_Hom_or_periods_recomputed": False})
        total = sum(int(records[i]["map_degree"]) for i in selected)
        maximum = max(int(records[i]["map_degree"]) for i in selected)
        cap_degrees = [int(records[i]["map_degree"]) for i in range(144, 149)]
        assert vector_rank(real_vectors[144:149]) == 5
        assert total <= sum(cap_degrees) and maximum <= max(cap_degrees)
        second = self.store("R794-selected-original-low-degree-eta-basis.json.gz", {
            "selected_candidate_indices": selected, "selected_maps": selected_records,
            "selected_basis_rank": 5, "selected_total_map_degree": str(total),
            "selected_maximum_map_degree": str(maximum), "old_cap_map_degrees": [str(x) for x in cap_degrees],
            "minimum_total_degree_in_this_149_candidate_set": True,
            "global_Hom_lattice_degree_optimality_claimed": False,
            "tie_break": "map_degree ascending, then fixed candidate_index",
            "nonzero_rank_minor_rows": minor_rows, "nonzero_rank_minor_determinant": eq(minor.det()),
            "original_R791_h_basis_to_selected_columns": em(change),
            "selected_h_basis_to_original_R791_columns": em(inverse_change),
            "basis_change_equation": "H_selected = H_original_R791 * change",
            "both_basis_change_identities_verified": True,
            "original_kappa_e_R_q_c0_c1_preserved": True,
            "eta_recipe": "sum_sigma pole(y_selected^sigma) - (degree/1206)*sum_sigma pole(y_f4^sigma)",
            "eta_recipe_scope": "the original rational Jacobian class, including descent of the symmetric NS class",
            "principal_function_recipe": "Norm(y_selected^2-b)^q / Norm(y_f4^2-b)^p for degree/1206=p/q",
            "principal_function_scope": "exact alpha3-isogeny divisor comparison only",
            "symmetric_representative_rigidification_comparison_computed": False,
            "actual_selected_Laurent_or_polar_divisors_or_eta_or_heights_computed": False})
        stages = [first, second]
        final = {"result": RESULT, "complete": True, "configuration": self.tag, "p": 41,
            "candidate_count": 149, "actual_basis_only_centered_rank": base_rank,
            "actual_basis_and_sums_centered_rank": sum_rank, "actual_all_candidates_centered_rank": all_rank,
            "selected_basis_rank": 5, "selected_candidate_indices": selected,
            "selected_map_degrees": [records[i]["map_degree"] for i in selected],
            "selected_total_map_degree": str(total), "selected_maximum_map_degree": str(maximum),
            "minimum_total_degree_in_this_149_candidate_set": True,
            "global_Hom_lattice_degree_optimality_claimed": False,
            "all_original_F0_directions_preserved": True, "original_R791_basis_change_verified": True,
            "old_Hom_periods_SVP_or_LLL_recomputed": False,
            "actual_polar_divisors_eta_values_or_heights_computed": False,
            "stages": stages, "seconds": time.monotonic()-self.started}
        save(self.out/FINAL, final)
        save(self.out/"core-receipt.json", {"result": RESULT, "complete": True,
            "source_sha256": sha(__file__), "certificate_sha256": sha(self.out/FINAL)})
        print(json.dumps({key: final[key] for key in
            ("result", "complete", "candidate_count", "actual_basis_only_centered_rank",
             "actual_basis_and_sums_centered_rank", "selected_map_degrees",
             "selected_total_map_degree", "selected_maximum_map_degree")}), flush=True)


def main():
    guard()
    sys.set_int_max_str_digits(0)
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--inputs", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--proof", type=Path, required=True)
    parser.add_argument("--config", type=Path, required=True)
    args = parser.parse_args()
    args.output.mkdir(parents=True, exist_ok=True)
    try:
        Job(args).run()
    except Exception as error:
        save(args.output/"core-receipt.json", {"result": RESULT, "complete": False,
            "source_sha256": sha(__file__), "error": type(error).__name__+": "+str(error)})
        raise


if __name__ == "__main__":
    main()
