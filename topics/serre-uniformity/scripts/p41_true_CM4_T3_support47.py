#!/usr/bin/env python3
"""Actual T3 divisor at SS_j36_06, the original CM4 coarse row zero.

Use the original A=1, B=0 source and necklace 5.  All four saved kernel
branches survive, including the two pairs with equal coarse targets.
This is deliberately not the shifted reference-j36 construction.
"""
import argparse
from collections import Counter
import gzip
import hashlib
import json
from pathlib import Path
import sys
import time


def read(path):
    raw = Path(path).read_bytes()
    return json.loads(gzip.decompress(raw) if str(path).endswith(".gz") else raw)


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    for name in ["script-dir", "work-dir", "output"]:
        ap.add_argument("--" + name, type=Path, required=True)
    ap.add_argument("--disk-id", choices=["SS_j36_06"], required=True)
    ap.add_argument("--result-id", required=True)
    args = ap.parse_args()
    scripts = args.script_dir.resolve()
    sys.path.insert(0, str(scripts))

    from p41_dag_level_transport47 import initialize
    from p41_projective_jet_frames47 import ProjectiveJetFrames, ordinary_physical_jets
    from p41_native_r2_linear47 import install
    from p41_coprime_kernel_dag47 import velu_model
    from p41_supersingular_atlas47 import ca, cm, ci, ck, cp, cn
    from p41_actual_differentials47 import save, digest

    started = time.monotonic()
    at = initialize(scripts)
    a, r, np = at.a, at.r, at.np
    install(r, args.work_dir / "native")
    frames = ProjectiveJetFrames(a)
    data = scripts / "data"
    inputs = {}

    def load(name):
        path = data / name
        inputs[name] = sha(path)
        return read(path)

    atlas = load("p41_rational_SS_residue_atlas47_complete.json.gz")
    graph = load("p41_SS_Hecke_graph47.json.gz")
    coarse = load("p41_elliptic_coarse_atlas47_verified.json.gz")
    bases = load("p41_hecke3_abel_bases_checkpoint.json.gz")
    assert graph["complete"] and graph["all_Frobenius_equivariant"]
    disk = args.disk_id
    chart = next(c for c in atlas["charts"] if disk in c["disk_ids"])
    row = chart["disk_ids"].index(disk)
    assert chart["reference_key"] == "CM4"
    coarse_source = next(c for c in coarse["elliptic_charts"] if c["kind"] == "CM4")
    coarse_row = chart["original_input_rows_0based"][row]
    source_row = coarse_source["indices_1based"][coarse_row] - 1
    assert coarse_row == 0 and source_row == 4
    assert coarse_source["curve_A"] == 1 and coarse_source["curve_B"] == 0
    assert r.equal(r.from_json(chart["frame"]), a.fc)
    W0 = r.rows(r.from_json(chart["W_coefficients_0to3"][0]), [row])
    Wraw0 = r.rows(r.from_json(coarse_source["coarse_values"][0]), [coarse_row])
    assert r.equal(W0, r.mul(Wraw0, r.inverse_values(r.mm(Wraw0, a.fc))))

    members = {(m["reference_key"], m["necklace_label_1based"]): v["vertex_0based"]
               for v in graph["vertices"] for m in v["members"]}
    source_vertex = members[("CM4", source_row + 1)]
    source_pos = graph["source_input_labels_0based"]["CM4"].index(source_row)
    assert source_vertex == 2069
    physical, physical_certs = {}, {}

    def point_key(W, modulus=r.Q):
        values = r.mm(W, frames.candidates)
        column = next(j for j in range(146) if r.units(values)[0, j])
        values = r.mul(values, r.inverse_values(r.cols(values, [column])))
        return tuple(int(v) % modulus for part in values for v in part[0])

    def physical_coefficients(key, index):
        if key not in physical:
            obj = ordinary_physical_jets(
                at, int(key), order=3,
                coarse_path=data / "p41_elliptic_coarse_atlas47_verified.json.gz")
            physical[key] = obj
            physical_certs[key] = {
                "coefficient_sha256": [digest(r.to_json(v)) for v in obj["W"]],
                "clearing_patches": obj["clearing_patches"], "degree": 3}
        obj = physical[key]
        assert index in obj["ordinary_indices_0based"]
        return [r.rows(v, [index]) for v in obj["W"]]

    def evaluate(coefficients, parameter):
        assert all(v % 47 == 0 for v in parameter)
        out = r.zeros(1, 73)
        for coefficient in reversed(coefficients):
            out = r.add(at.matrix_scale(out, parameter), coefficient)
        return out

    def polynomial_value(coefficients, argument):
        result = (0, 0)
        for coefficient in reversed(coefficients):
            result = ca(cm(result, argument), coefficient)
        return result

    A, B = (1, 0), (0, 0)
    division_coefficients = [ck(cp(A, 2), -1), ck(B, 12),
                             ck(A, 6), (0, 0), (3, 0)]
    expected_vertices = [1152, 1152, 276, 276]
    expected_labels = [("10", 102), ("10", 102), ("9", 19), ("9", 19)]
    targets, records, kernels = [], [], []
    for branch in range(4):
        frozen = graph["constant_branches"]["CM4/3/" + str(branch)]
        assert tuple(frozen["source_A"]) == A and tuple(frozen["source_B"]) == B
        assert frozen["source_reference_key"] == "CM4"
        assert frozen["ell"] == frozen["degree"] == frozen["determinant_mod41"] == 3
        matrix = frozen["raw_level_matrix_mod41"]
        assert (matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]) % 41 == 3
        assert frozen["kernel"][1] == [1, 0]
        root = cn(tuple(frozen["kernel"][0]))
        assert polynomial_value(division_coefficients, root) == (0, 0)
        kernel = [cn(root), (1, 0)]
        target_A, target_B = velu_model(3, kernel, A, B)
        assert tuple(target_A) == tuple(frozen["A"]) and tuple(target_B) == tuple(frozen["B"])
        kernels.append(tuple(frozen["kernel"][0]))

        key = frozen["reference_key"]
        label = frozen["image_indices_1based"][source_pos]
        assert (key, label) == expected_labels[branch]
        # These original four branches are all regular, not CM coarse targets.
        assert (key, label) in members and key in {"9", "10"}
        parameter = tuple(frozen["reference_parameter"])
        Wraw = evaluate(physical_coefficients(key, label - 1), parameter)
        # Keep the saved isogeny's actual differential homothety before projectivising.
        Wraw = at.matrix_scale(Wraw, cp(tuple(frozen["homothety"]), 2))
        frame_value = r.mm(Wraw, a.fc)
        assert np.all(r.units(frame_value))
        W = r.mul(Wraw, r.inverse_values(frame_value))
        expected_vertex = frozen["target_vertices_0based"][source_pos]
        assert expected_vertex == expected_vertices[branch]
        vertex = graph["vertices"][expected_vertex]
        assert point_key(W, 47) == tuple(
            vertex["projective_146_mod47_real"] + vertex["projective_146_mod47_imag"])
        assert r.equal(r.mm(W, a.fc), r.column([[1, 0]]))
        targets.append(W)
        records.append({
            "branch_0based": branch,
            "actual_saved_full_level_record": frozen,
            "target_vertex_0based": expected_vertex,
            "used_true_elliptic_coarse_chart": False,
            "all146_projective_reduction_coordinates_match_graph": True,
            "W_actual_values_in_R2": r.to_json(W)[0],
            "target_reference_key": key, "target_necklace_label_1based": label,
            "actual_kernel_root_in_R2": list(root),
            "saved_graph_raw_level_branch_preserved": True,
            "actual_Velu_model_recomputed_from_original_CM4_source": True})
        print("PASS actual CM4 T3 branch", branch, key, label, expected_vertex, flush=True)

    keys = [point_key(W) for W in targets]
    residue_keys = [point_key(W, 47) for W in targets]
    assert len(set(keys)) == 2
    assert keys[0] == keys[1] and keys[2] == keys[3] and keys[0] != keys[2]
    assert r.equal(targets[0], targets[1]) and r.equal(targets[2], targets[3])
    multiplicities = [keys.count(keys[j]) for j in [0, 2]]
    assert multiplicities == [2, 2] and sum(multiplicities) == 4

    # Frobenius permutes kernel branches, not a list obtained by deduplication.
    kernel_frobenius = [
        kernels.index((v[0] % r.Q, (-v[1]) % r.Q)) for v in kernels]
    assert kernel_frobenius == [1, 0, 2, 3]
    conjugated = [point_key(r.mm(r.conjugate(W), r.conjugate(a.M["A1"])))
                  for W in targets]
    assert Counter(keys) == Counter(conjugated)
    assert all(conjugated[i] == keys[kernel_frobenius[i]] for i in range(4))
    assert point_key(W0, 47) not in residue_keys

    # I1 and I2 are the original 54-point families in the reference-j9 820-row model.
    # Check actual projective values, rather than inferring separation from labels alone.
    assert r.equal(at.refs[9]["W"], a.M["W"])
    family_checks = []
    for number, family in enumerate(bases["families"], start=1):
        labels = family["points_1based"]
        assert len(labels) == 54
        family_keys = {
            point_key(r.rows(a.M["W"], [label - 1]), 47): label for label in labels}
        assert len(family_keys) == 54
        collisions = [[family_keys[key]] if key in family_keys else [] for key in residue_keys]
        assert all(not hits for hits in collisions)
        source_collisions = ([family_keys[point_key(W0, 47)]]
                             if point_key(W0, 47) in family_keys else [])
        assert not source_collisions
        family_checks.append({
            "family": "I" + str(number), "points_1based": labels,
            "branch_collision_labels_1based": collisions,
            "source_collision_labels_1based": source_collisions,
            "all_four_branches_disjoint_by_actual146_mod47_coordinates": True})
    assert len(family_checks) == 2

    numerator = ck(cp(A, 3), 4)
    j_value = ck(cm(numerator, ci(ca(numerator, ck(cp(B, 2), 27)))), 1728)
    assert j_value == (1728, 0) and j_value[0] % 47 == 36
    out = {
        "result": args.result_id, "source_disk_id": disk, "level": 41,
        "auxiliary_prime": 47, "precision": 4, "modulus": r.Q,
        "source_reference_key": "CM4", "source_row_0based": source_row,
        "source_vertex_0based": source_vertex,
        "original_CM4_coarse_row_0based": coarse_row,
        "actual_source_W_fc_normalized": r.to_json(W0)[0],
        "actual_source_model": [A, B], "actual_source_j_mod47four": j_value[0],
        "actual_source_physical_parameter": [0, 0],
        "source_raw_reference_center_identical": True,
        "actual_T3_targets_fc_normalized": [r.to_json(W)[0] for W in targets],
        "actual_target_vertices_0based": expected_vertices,
        "actual_distinct_target_vertices_0based": [1152, 276],
        "actual_coarse_target_multiplicities": multiplicities,
        "actual_target_Frobenius_permutation_0based": kernel_frobenius,
        "all_four_kernel_branches_retained_including_repeated_targets": True,
        "both_repeated_pairs_equal_in_all73_coordinates_mod47four": True,
        "all_four_true_targets_Frobenius_stable": True,
        "all_four_targets_separate_from_source": True,
        "all_four_targets_separate_from_I1_and_I2": True,
        "I1_I2_collision_checks": family_checks,
        "source_all73_equals_original_rational_SS_center": True,
        "physical_jet_certificates": physical_certs,
        "actual_branches": records, "branch_records": records,
        "complete_actual_T3_support": True,
        "raw_level_determinant_mod41": 3, "total_target_degree": 4,
        "kernel_polynomial_ascending": [list(v) for v in division_coefficients],
        "kernel_polynomial_coefficient_ring": "R2=Z/47^4[i], i^2=-1",
        "input_sha256": dict(a.inputs, **inputs), "source_sha256": sha(__file__),
        "dependency_sources_sha256": {
            name: sha(scripts / name) for name in [
                "p41_dag_level_transport47.py", "p41_projective_jet_frames47.py",
                "p41_coprime_kernel_dag47.py", "p41_supersingular_atlas47.py"]},
        "runtime_seconds": round(time.monotonic() - started, 3)}
    print("PASS true CM4 complete T3 support", save(args.output, out), flush=True)


if __name__ == "__main__":
    main()
