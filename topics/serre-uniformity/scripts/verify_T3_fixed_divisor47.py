#!/usr/bin/env python3
"""Independent standard-library checks for the frozen actual T3 divisor.

Checks finite group actions, true CM/kernel identities, all stored point
Frobenius equations, exact graph labels, and all input/source digests.
Does not rerun torsion enumeration or the projective differential engine.
"""
import argparse
from collections import Counter
import gzip
import hashlib
import json
from pathlib import Path

Q = 47**4


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def read(path):
    raw = Path(path).read_bytes()
    return json.loads(gzip.decompress(raw) if str(path).endswith(".gz") else raw)


def add(x, y):
    return ((x[0]+y[0]) % Q, (x[1]+y[1]) % Q)


def mul(x, y):
    return ((x[0]*y[0]-x[1]*y[1]) % Q, (x[0]*y[1]+x[1]*y[0]) % Q)


def scale(x, n):
    return (x[0]*n % Q, x[1]*n % Q)


def conjugate(x):
    return (x[0] % Q, -x[1] % Q)


def power(x, n):
    out = (1, 0)
    for _ in range(n):
        out = mul(out, x)
    return out


def inverse(x):
    d = pow((x[0]*x[0]+x[1]*x[1]) % Q, -1, Q)
    return (x[0]*d % Q, -x[1]*d % Q)


def mm(A, B, modulus=41):
    return [[sum(A[i][k]*B[k][j] for k in range(2)) % modulus for j in range(2)] for i in range(2)]


def det(A):
    return (A[0][0]*A[1][1]-A[0][1]*A[1][0]) % 41


def permutations(g, necklaces):
    d = pow(det(g), -1, 41)
    inv = [[g[1][1]*d % 41, -g[0][1]*d % 41],
           [-g[1][0]*d % 41, g[0][0]*d % 41]]
    lookup = {tuple(v): i for i, v in enumerate(necklaces)}
    result = []
    for x, e in necklaces:
        N = [[x, (e-x*x) % 41], [1, -x % 41]]
        T = mm(mm(g, N), inv)
        c = pow(T[1][0], -1, 41)
        xx = T[0][0]*c % 41
        ee = (xx*xx+T[0][1]*c) % 41
        result.append(lookup[(xx, ee)])
    assert sorted(result) == list(range(820))
    return result


def full_j(A, B):
    numerator = scale(power(A, 3), 4)
    denominator = add(numerator, scale(power(B, 2), 27))
    return scale(mul(numerator, inverse(denominator)), 1728)


def velu3(A, B, x):
    t = add(scale(power(x, 2), 3), A)
    w = add(add(scale(power(x, 3), 5), scale(mul(A, x), 3)), scale(B, 2))
    return add(A, scale(t, -10)), add(B, scale(w, -14))


def psi3(A, B, x):
    return add(add(add(scale(power(x, 4), 3), scale(mul(A, power(x, 2)), 6)),
                   scale(mul(B, x), 12)), scale(power(A, 2), -1))


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--script-dir", type=Path, required=True)
    ap.add_argument("--certificate", type=Path, required=True)
    ap.add_argument("--source", type=Path, required=True)
    ap.add_argument("--ss-abel", type=Path, required=True)
    ap.add_argument("--output", type=Path, required=True)
    args = ap.parse_args()
    data_dir = args.script_dir / "data"
    d = read(args.certificate)
    assert d["complete"] and d["source_sha256"] == sha(args.source)
    checked_hashes = {}
    for name, expected in d["input_sha256"].items():
        path = args.ss_abel if name == args.ss_abel.name else data_dir / name
        assert sha(path) == expected, name
        checked_hashes[name] = expected
    model = read(data_dir / "p41_makdisi47_certificate.json.gz")
    graph = read(data_dir / "p41_SS_Hecke_graph47.json.gz")
    cm3 = read(data_dir / "p41_cm3_makdisi47_certificate.json")
    inventory = read(data_dir / "p41_residue47_inventory.json")
    assert next(v for v in inventory["fibres"] if v["j"] == 38)["coarse_F47_points"] == 1
    necklaces = model["necklaces"]
    M12 = d["level_action_certificates"]["CM12"]["actual_matrix_mod41"]
    M0 = d["level_action_certificates"]["CM3"]["actual_matrix_mod41"]
    Munit = d["level_action_certificates"]["CM3"]["actual_mu3_matrix_mod41"]
    assert M12 == [[10, 4], [5, 31]] and M0 == [[8, 3], [5, 33]]
    for matrix in [M12, M0]:
        assert det(matrix) == 3 and sum(matrix[i][i] for i in range(2)) % 41 == 0
        assert mm(matrix, matrix) == [[38, 0], [0, 38]]
    assert det(Munit) == 1 and mm(mm(Munit, Munit), Munit) == [[1, 0], [0, 1]]
    assert mm(M0, Munit) == mm(Munit, M0)
    perm12, perm0, permu = [permutations(g, necklaces) for g in [M12, M0, Munit]]
    fixed12 = [i+1 for i, j in enumerate(perm12) if i == j]
    fixed0 = [i+1 for i, j in enumerate(perm0) if i == j]
    assert len(fixed12) == len(fixed0) == 22
    assert fixed12 == d["level_action_certificates"]["CM12"]["fixed_necklace_indices_1based"]
    assert fixed0 == d["level_action_certificates"]["CM3"]["fixed_necklace_indices_1based"]
    orbits = d["level_action_certificates"]["CM3"]["fixed_mu3_orbits_1based"]
    assert sorted(x for orbit in orbits for x in orbit) == fixed0
    assert Counter(map(len, orbits)) == {1: 1, 3: 7}
    for orbit in orbits:
        assert sorted(permu[i-1]+1 for i in orbit) == sorted(orbit)
    assert [o for o in orbits if len(o) == 1] == [[cm3["CM_necklace_index_1based"]]]
    lam = d["lambda_sqrt_minus3_mod47four"]
    omega = d["omega_cuberoot_mod47four"]
    assert power(lam, 2) == (Q-3, 0)
    assert power(omega, 3) == (1, 0) and tuple(omega) != (1, 0)
    group_summary = {}
    basis_frob = model["frobenius_basis_matrix"]
    all_points = []
    ss = read(args.ss_abel)
    disks = {v["vertex_0based"]: v["disk_id"] for v in ss["rational_SS_center_constants"]}
    frobenius_scalar_checks = 0
    for name in ["Z12", "Z0fix", "c11", "v"]:
        group = d["groups"][name]
        points = group["points"]
        W = [p["W_mod47four"] for p in points]
        perm = group["Frobenius_permutation_0based"]
        assert sorted(perm) == list(range(len(points)))
        assert all(perm[perm[i]] == i for i in range(len(points)))
        for i, point in enumerate(points):
            assert point["frame_name"] == "fc" and point["fc_is_unit"]
            assert len(W[i]) == 73
            actual = []
            for j in range(73):
                z = (0, 0)
                for k in range(73):
                    z = add(z, mul(conjugate(W[i][k]), conjugate(basis_frob[k][j])))
                actual.append(list(z))
            assert actual == W[perm[i]], (name, i, "actual semilinear Frobenius")
            frobenius_scalar_checks += 73
            assert point["Q47_rational"] == (perm[i] == i)
            if point["reference_key"] is not None:
                vertex = point["SS_vertex_0based"]
                wanted = (point["reference_key"], point["necklace_index_1based"])
                assert wanted in {(m["reference_key"], m["necklace_label_1based"])
                                  for m in graph["vertices"][vertex]["members"]}
                assert points[perm[i]]["SS_vertex_0based"] == graph["frobenius_permutation_0based"][vertex]
                assert point["rational_disk_id"] == disks.get(vertex)
            all_points.append(point)
        group_summary[name] = {
            "count": len(points), "degree": group["total_degree"],
            "rational_count": sum(i == j for i, j in enumerate(perm)),
            "conjugate_pair_count": sum(i < j for i, j in enumerate(perm)),
        }
    assert group_summary == {
        "Z12": {"count": 22, "degree": 22, "rational_count": 2, "conjugate_pair_count": 10},
        "Z0fix": {"count": 8, "degree": 8, "rational_count": 2, "conjugate_pair_count": 3},
        "c11": {"count": 1, "degree": 2, "rational_count": 1, "conjugate_pair_count": 0},
        "v": {"count": 1, "degree": 0, "rational_count": 1, "conjugate_pair_count": 0},
    }
    assert sum(v["degree"] for v in group_summary.values()) == 32
    CM12 = d["level_action_certificates"]["CM12"]
    A, B = map(tuple, CM12["source_model"])
    assert full_j(A, B) == (54000, 0)
    assert psi3(A, B, (3, 0)) == (0, 0)
    assert velu3(A, B, (3, 0)) == (scale(A, 9), scale(B, -27))
    p11 = d["groups"]["c11"]["points"][0]
    A, B = map(tuple, p11["exact_CM_model"])
    assert full_j(A, B) == (-32768 % Q, 0) and p11["ordinary_disk_id"] == "ORD_j38"
    branches11 = d["level_action_certificates"]["CM11"]["two_actual_horizontal_Velu_kernels"]
    assert len({tuple(v["kernel_x"]) for v in branches11}) == 2
    for rec in branches11:
        x, c = rec["kernel_x"], rec["return_homothety"]
        assert x[1] == c[1] == 0 and psi3(A, B, x) == (0, 0)
        At, Bt = velu3(A, B, x)
        assert [list(At), list(Bt)] == rec["target_model"]
        assert full_j(At, Bt) == full_j(A, B)
        assert mul(A, power(c, 4)) == At and mul(B, power(c, 6)) == Bt
        assert add(add(power(c, 2), scale(c, -1)), (3, 0)) == (0, 0) or \
               add(add(power(c, 2), c), (3, 0)) == (0, 0)
    for rec in d["T3_basepoint_branches"]["three_nonhorizontal_branches"]:
        x = rec["kernel_x"]
        assert power(x, 3) == (Q-4, 0)
        assert psi3((0, 0), (1, 0), x) == (0, 0)
        At, Bt = velu3((0, 0), (1, 0), x)
        assert [list(At), list(Bt)] == rec["target_model"]
        assert full_j(At, Bt) == (-12288000 % Q, 0)
        assert det(rec["raw_level_matrix_mod41"]) == 3
    assert d["sigma_F3_basepoint_factor"]["factor_mod47four"] == pow(512, -1, Q) == 3040270
    output = {
        "complete": True, "certificate_sha256": sha(args.certificate),
        "executor_sha256": sha(args.source), "verifier_sha256": sha(__file__),
        "checked_input_sha256": checked_hashes, "groups": group_summary,
        "standard_library_finite_group_actions_verified": True,
        "actual_semilinear_Frobenius_scalar_equalities": frobenius_scalar_checks,
        "all_true_CM_and_Velu_kernel_identities_verified": True,
        "all_exact_graph_labels_verified": True,
        "torsion_enumeration_or_projective_jet_engine_rerun": False,
        "scope": "Independent algebra and stored point checks; actual full1681 lookup, physical jets and full2701 products are the executor's recorded computation.",
    }
    args.output.write_text(json.dumps(output, sort_keys=True, indent=2)+"\n")
    print("PASS standard-library finite actions,32 actual point Frobenius rows,CM kernels and all digests", sha(args.output))


if __name__ == "__main__":
    main()
