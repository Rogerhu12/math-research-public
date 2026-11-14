#!/usr/bin/env python3
"""Actual T3 fixed divisor and T3(b) in the published 73-section model.

No second-kind integral is inferred from an uncomputed complex graph value.
The output consists of actual points, exact residue level matrices, true
physical specialization, and Frobenius-stable finite divisors.
"""
import argparse
from collections import Counter
import gzip
import hashlib
import json
from pathlib import Path
import sys
import time

Q = 47**4


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def read(path):
    raw = Path(path).read_bytes()
    return json.loads(gzip.decompress(raw) if str(path).endswith(".gz") else raw)


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--script-dir", type=Path, required=True)
    ap.add_argument("--ss-abel", type=Path, required=True)
    ap.add_argument("--output", type=Path, required=True)
    args = ap.parse_args()
    folder = args.script_dir.resolve()
    sys.path.insert(0, str(folder))
    from p41_dag_level_transport47 import initialize, FullLevelTransport
    from p41_projective_jet_frames47 import ProjectiveJetFrames, ordinary_physical_jets
    from p41_actual_differentials47 import save, digest
    from p41_supersingular_atlas47 import ca, cs, cn, cm, ci, ck, cp
    from p41_coprime_kernel_dag47 import velu_model, R

    started = time.monotonic()
    at = initialize(folder)
    a, r, np = at.a, at.r, at.np
    frames = ProjectiveJetFrames(a)
    level = FullLevelTransport(at)
    F = level.F
    graph_path = folder / "data/p41_SS_Hecke_graph47.json.gz"
    graph = read(graph_path)
    ss = read(args.ss_abel)
    vertex_to_disk = {v["vertex_0based"]: v["disk_id"]
                      for v in ss["rational_SS_center_constants"]}
    member_to_vertex = {}
    for vertex in graph["vertices"]:
        for member in vertex["members"]:
            member_to_vertex[(member["reference_key"], member["necklace_label_1based"])] = vertex["vertex_0based"]
    coarse_path = folder / "data/p41_elliptic_coarse_atlas47_verified.json.gz"
    coarse = read(coarse_path)
    c3 = a.read("p41_cm3_makdisi47_certificate.json")
    b_index = c3["CM_necklace_index_1based"] - 1
    b_raw = r.from_json(next(v for v in coarse["elliptic_charts"] if v["kind"] == "CM3")["coarse_values"][0])
    cm_path = folder / "data/p41_three_ordinary_CM_anchors_and_113_global_functions47.json.gz"
    cm_data = read(cm_path)
    c11 = next(v for v in cm_data["three_ordinary_CM_anchors"] if v["discriminant"] == -11)

    state = {
        "level": 41, "auxiliary_prime": 47, "precision": 4, "modulus": Q,
        "complete": False, "groups": {}, "level_action_certificates": {},
        "source_sha256": sha(__file__),
        "input_sha256": {
            graph_path.name: sha(graph_path), args.ss_abel.name: sha(args.ss_abel),
            coarse_path.name: sha(coarse_path), cm_path.name: sha(cm_path),
        },
        "scope": "Actual finite divisors Q3 and T3(b); no complete F3 height or common-root computation claimed",
    }

    def checkpoint():
        state["input_sha256"].update(a.inputs)
        state["reference_1681_point_tables"] = {
            k: v["certificate"] for k, v in level.lookup_tables.items()
        }
        state["elapsed_seconds"] = round(time.monotonic() - started, 3)
        save(args.output, state)

    def full_j(A, B):
        num = ck(cp(A, 3), 4)
        return ck(cm(num, ci(ca(num, ck(cp(B, 2), 27)))), 1728)

    def scale_point(T, c):
        return F.mul(T[0], F.embed(cp(c, 2, 47))), F.mul(T[1], F.embed(cp(c, 3, 47)))

    def mm2(U, V):
        return [[sum(U[i][k] * V[k][j] for k in range(2)) % 41 for j in range(2)] for i in range(2)]

    def determinant(M):
        return (M[0][0]*M[1][1] - M[0][1]*M[1][0]) % 41

    def unit_normalize(W):
        val = r.mm(W, a.fc)
        if bool(r.units(val)[0, 0]):
            frame, frame_name = a.fc, "fc"
        else:
            values = r.mm(W, frames.candidates)
            k = next(i for i in range(146) if r.units(values)[0, i])
            frame, frame_name = r.cols(frames.candidates, [k]), "rational_candidate_" + str(k)
            val = r.mm(W, frame)
        normalized = r.mul(W, r.inverse_values(val))
        assert r.equal(r.mm(normalized, frame), r.column([[1, 0]]))
        return normalized, frame, frame_name

    def point_key(W, modulus=Q):
        values = r.mm(W, frames.candidates)
        k = next(i for i in range(146) if r.units(values)[0, i])
        values = r.mul(values, r.inverse_values(r.cols(values, [k])))
        return tuple(int(v) % modulus for t in values for v in t[0])

    def decorate(W, label, ref_key=None, ref_index=None, **extra):
        W, frame, frame_name = unit_normalize(W)
        rec = {
            "label": label, "W_mod47four": r.to_json(W)[0],
            "frame": r.to_json(frame), "frame_name": frame_name,
            "fc_is_unit": bool(r.units(r.mm(W, a.fc))[0, 0]),
            "reference_key": ref_key, "necklace_index_1based": ref_index,
        }
        rec.update(extra)
        if ref_key is not None:
            vertex = member_to_vertex[(ref_key, ref_index)]
            rec.update(SS_vertex_0based=vertex, rational_disk_id=vertex_to_disk.get(vertex),
                       reduction_F47_rational=graph["vertices"][vertex]["F47_rational"])
        return rec

    def finalize_group(name, points, expected_count, multiplicity=1):
        assert len(points) == expected_count
        W = r.from_json([v["W_mod47four"] for v in points])
        keys = [point_key(r.rows(W, [i])) for i in range(len(points))]
        assert len(set(keys)) == len(keys)
        conjugate = r.mm(r.conjugate(W), r.conjugate(a.M["A1"]))
        lookup = {key: i for i, key in enumerate(keys)}
        perm = [lookup[point_key(r.rows(conjugate, [i]))] for i in range(len(points))]
        assert all(perm[perm[i]] == i for i in range(len(points)))
        for i, rec in enumerate(points):
            rec["Frobenius_partner_index_0based"] = perm[i]
            rec["Q47_rational"] = perm[i] == i
            rec["fixed_divisor_multiplicity"] = multiplicity
            if "SS_vertex_0based" in rec:
                assert points[perm[i]]["SS_vertex_0based"] == graph["frobenius_permutation_0based"][rec["SS_vertex_0based"]]
                assert rec["Q47_rational"] == rec["reduction_F47_rational"]
        group = {
            "points": points, "point_count": len(points), "total_degree": multiplicity*len(points),
            "Frobenius_permutation_0based": perm,
            "Q47_rational_point_indices_0based": [i for i, j in enumerate(perm) if i == j],
            "R2_conjugate_pairs_0based": [[i, j] for i, j in enumerate(perm) if i < j],
            "actual_Frobenius_stable_mod47four": True,
            "all_fc_unit": all(v["fc_is_unit"] for v in points),
            "all_distinct_actual_projective_points": True,
        }
        state["groups"][name] = group
        checkpoint()
        print("ACTUAL GROUP", name, len(points), "Q47", len(group["Q47_rational_point_indices_0based"]),
              "pairs", len(group["R2_conjugate_pairs_0based"]), "fc", group["all_fc_unit"], flush=True)

    physical_cache = {}

    def physical_values(key, t, c, indices):
        j = int(key)
        if key not in physical_cache:
            obj = ordinary_physical_jets(at, j, order=3, coarse_path=coarse_path)
            physical_cache[key] = obj
            state.setdefault("physical_jet_certificates", {})[key] = {
                "coefficient_count": len(obj["W"]),
                "highest_degree": 3, "all_coefficients_integral": True,
                "ordinary_indices_1based": [i+1 for i in obj["ordinary_indices_0based"]],
                "coefficient_sha256": [digest(r.to_json(v)) for v in obj["W"]],
                "clearing_patches": obj["clearing_patches"],
            }
        obj = physical_cache[key]
        assert set(indices).issubset(obj["ordinary_indices_0based"])
        assert all(v % 47 == 0 for v in t)
        value = r.zeros(len(indices), 73)
        for coeff in reversed(obj["W"]):
            value = r.add(at.matrix_scale(value, t), r.rows(coeff, indices))
        return at.matrix_scale(value, cp(c, 2))

    # The common trace-zero norm3 endomorphism has lambda^2=-3.
    lam = (0, 12)
    for _ in range(2):
        lam = cs(lam, cm(ca(cp(lam, 2), (3, 0)), ci(ck(lam, 2))))
    assert cp(lam, 2) == (-3 % Q, 0)
    omega = ck(cs(lam, (1, 0)), pow(2, -1, Q))
    assert cp(omega, 3) == (1, 0) and omega != (1, 0)
    state["lambda_sqrt_minus3_mod47four"] = lam
    state["omega_cuberoot_mod47four"] = omega

    # Z12: a true model with j=54000, not the unshifted j44 reference.
    A12, B12 = (-15 % Q, 0), (22, 0)
    assert full_j(A12, B12) == (54000 % Q, 0)
    key12, c12, t12 = level.match(A12, B12)
    assert key12 == "44"
    ref12 = level.refs[key12]
    P12, Q12 = [scale_point(F.point(ref12[k]), c12) for k in ("P", "Q")]
    h12 = [(-3 % Q, 0), (1, 0)]
    At12, Bt12 = velu_model(3, h12, A12, B12)
    assert At12 == ck(A12, 9) and Bt12 == ck(B12, -27)
    node12 = {"ell": 3, "source_A": A12, "source_B": B12,
              "A": At12, "B": Bt12, "kernel": h12}
    alphapair12 = [scale_point(T, ci(lam)) for T in level.raw_pair(node12, P12, Q12)]
    M12 = level.matrix(key12, c12, *alphapair12, 3)
    assert determinant(M12) == 3 and (M12[0][0]+M12[1][1]) % 41 == 0
    assert mm2(M12, M12) == [[38, 0], [0, 38]]
    perm12 = at.permute(M12, list(range(820)))
    fixed12 = [i for i, j in enumerate(perm12) if i == j]
    assert len(fixed12) == 22
    state["level_action_certificates"]["CM12"] = {
        "source_model": [A12, B12], "j_integer": 54000, "kernel_x": [3, 0],
        "Velu_target_model": [At12, Bt12], "return_homothety": lam,
        "actual_matrix_mod41": M12, "matrix_square": [[38, 0], [0, 38]],
        "trace_mod41": 0, "determinant_mod41": 3,
        "fixed_necklace_indices_1based": [i+1 for i in fixed12],
        "homothety_to_reference": c12, "reference_parameter": t12,
        "raw_transported_basis_retained": True,
    }
    W12 = physical_values(key12, t12, c12, fixed12)
    pts12 = [decorate(r.rows(W12, [k]), "Z12_"+str(k).zfill(2), key12, idx+1,
                      CM_discriminant=-12, j_integer=54000,
                      exact_CM_model=[[-15, 0], [22, 0]],
                      physical_reference_parameter=t12,
                      local_branch_tangent_ratio=[Q-1, 0],
                      local_intersection_multiplicity=1)
             for k, idx in enumerate(fixed12)]
    finalize_group("Z12", pts12, 22)

    # Z0: first enumerate on the true CM3 torsion basis, then quotient mu3.
    A0, B0 = (0, 0), (1, 0)
    Pc, Qc = [F.point(level.refs["CM3"][k]) for k in ("P", "Q")]
    h0 = [(0, 0), (1, 0)]
    At0, Bt0 = velu_model(3, h0, A0, B0)
    assert At0 == (0, 0) and Bt0 == (-27 % Q, 0)
    node0 = {"ell": 3, "source_A": A0, "source_B": B0, "A": At0, "B": Bt0, "kernel": h0}
    alphapair0 = [scale_point(T, ci(lam)) for T in level.raw_pair(node0, Pc, Qc)]
    M0 = level.matrix("CM3", (1, 0), *alphapair0, 3)
    rhopair = [(F.mul(T[0], F.embed(omega)), T[1]) for T in (Pc, Qc)]
    Mrho = level.matrix("CM3", (1, 0), *rhopair, 1)
    assert mm2(M0, M0) == [[38, 0], [0, 38]]
    assert (M0[0][0]+M0[1][1]) % 41 == 0 and determinant(M0) == 3
    assert mm2(mm2(Mrho, Mrho), Mrho) == [[1, 0], [0, 1]]
    assert Mrho != [[1, 0], [0, 1]] and mm2(M0, Mrho) == mm2(Mrho, M0)
    perm0, permrho = at.permute(M0, list(range(820))), at.permute(Mrho, list(range(820)))
    all_orbits = []
    left = set(range(820))
    while left:
        idx = min(left)
        orbit = sorted({idx, permrho[idx], permrho[permrho[idx]]})
        assert all(permrho[x] in orbit for x in orbit)
        all_orbits.append(orbit)
        left.difference_update(orbit)
    fixed_orbits = [orbit for orbit in all_orbits if perm0[orbit[0]] in orbit]
    assert len(fixed_orbits) == 8 and Counter(map(len, fixed_orbits)) == {1: 1, 3: 7}
    assert [orbit for orbit in fixed_orbits if len(orbit) == 1] == [[b_index]]
    fixed0 = sorted(x for orbit in fixed_orbits for x in orbit)
    assert len(fixed0) == 22 and all(perm0[x] == x for x in fixed0)
    identity0 = level.record(A0, B0, Pc, Qc, 1, fixed0)
    key0, c0, t0 = identity0["reference_key"], tuple(identity0["homothety"]), tuple(identity0["reference_parameter"])
    assert key0 == "0"
    mapped0 = dict(zip(fixed0, [i-1 for i in identity0["image_indices_1based"]]))
    nonell0 = [i for i in fixed0 if i != b_index]
    W0ordinary = physical_values(key0, t0, c0, [mapped0[i] for i in nonell0])
    W0lookup = {i: r.rows(W0ordinary, [k]) for k, i in enumerate(nonell0)}
    state["level_action_certificates"]["CM3"] = {
        "source_model": [A0, B0], "kernel_x": [0, 0],
        "Velu_target_model": [At0, Bt0], "return_homothety": lam,
        "actual_matrix_mod41": M0, "actual_mu3_matrix_mod41": Mrho,
        "fixed_necklace_indices_1based": [i+1 for i in fixed0],
        "fixed_mu3_orbits_1based": [[i+1 for i in orbit] for orbit in fixed_orbits],
        "actual_reference_identification": identity0,
        "raw_transported_basis_retained": True,
        "coarse_singleton_is_b": True,
    }
    pts0 = []
    for k, orbit in enumerate(fixed_orbits):
        if orbit == [b_index]:
            W = b_raw
            ref_key, ref_idx = "CM3", b_index+1
        else:
            W = W0lookup[orbit[0]]
            assert all(point_key(W) == point_key(W0lookup[i]) for i in orbit)
            ref_key, ref_idx = "0", mapped0[orbit[0]]+1
        pts0.append(decorate(W, "Z0fix_"+str(k).zfill(2), ref_key, ref_idx,
                            CM_discriminant=-3, j_integer=0, exact_CM_model=[[0, 0], [1, 0]],
                            actual_CM3_necklace_orbit_1based=[i+1 for i in orbit],
                            ordinary_reference_labels_1based=[mapped0[i]+1 for i in orbit],
                            is_basepoint_b=(orbit == [b_index]),
                            local_intersection_multiplicity=1,
                            coarse_tangent_ratio_at_b=[Q-1, 0] if orbit == [b_index] else None))
    finalize_group("Z0fix", pts0, 8)

    # c11 is the already independently transported true CM point, not its
    # arbitrary ORD_j38 center. Check both horizontal kernels directly.
    W11 = r.from_json(c11["physical_CM_W_in_chart_frame_mod47four"])
    A11, B11 = [(v % Q, 0) for v in c11["actual_elliptic_model_mod47four"]]
    assert full_j(A11, B11) == (-32768 % Q, 0)

    def all_R2_three_roots(A, B):
        def psi(x, modulus):
            return cs(ca(ca(ck(cp(x, 4, modulus), 3, modulus),
                            ck(cm(A, cp(x, 2, modulus), modulus), 6, modulus), modulus),
                         ck(cm(B, x, modulus), 12, modulus), modulus),
                      cp(A, 2, modulus), modulus)
        roots = []
        for x in range(47):
            for y in range(47):
                root = (x, y)
                if psi(root, 47) != (0, 0):
                    continue
                for _ in range(2):
                    derivative = ck(ca(ca(cp(root, 3), cm(A, root)), B), 12)
                    root = cs(root, cm(psi(root, Q), ci(derivative)))
                assert psi(root, Q) == (0, 0)
                roots.append(root)
        return roots

    roots11 = all_R2_three_roots(A11, B11)
    horizontal11 = []
    for root in roots11:
        At, Bt = velu_model(3, [cn(root), (1, 0)], A11, B11)
        if full_j(At, Bt) != full_j(A11, B11):
            continue
        # There is a unique ordinary F47 necklace; exact etale continuation
        # makes a horizontal CM isomorphism preserve that actual lift.
        ratio = cm(At, ci(A11))
        scales = [(x, y) for x in range(47) for y in range(47)
                  if (x or y) and cp((x, y), 4, 47) == tuple(v % 47 for v in ratio)
                  and cm(Bt, ci(cp((x, y), 6, 47), 47), 47) == tuple(v % 47 for v in B11)]
        assert scales
        c = scales[0]
        for _ in range(2):
            c = cs(c, cm(cs(cp(c, 4), ratio), ci(ck(cp(c, 3), 4))))
        assert cm(A11, cp(c, 4)) == At and cm(B11, cp(c, 6)) == Bt
        horizontal11.append({"kernel_x": root, "target_model": [At, Bt], "return_homothety": c})
    assert len(horizontal11) == 2 and all(v["kernel_x"][1] == 0 for v in horizontal11)
    # Endomorphism eigenvalue ratio has nonzero discriminant -11 at 47.
    sqrt11 = (6, 0)
    for _ in range(2):
        sqrt11 = cs(sqrt11, cm(ca(cp(sqrt11, 2), (11, 0)), ci(ck(sqrt11, 2))))
    assert cp(sqrt11, 2) == (-11 % Q, 0)
    alpha = ck(ca((1, 0), sqrt11), pow(2, -1, Q))
    alpha_bar = cs((1, 0), alpha)
    assert cm(alpha, alpha_bar) == (3, 0)
    slopes11 = [cm(alpha, ci(alpha_bar)), cm(alpha_bar, ci(alpha))]
    assert all((s[0]-1) % 47 or s[1] % 47 for s in slopes11)
    state["level_action_certificates"]["CM11"] = {
        "true_CM_input_disk": c11["disk_id"], "j_integer": -32768,
        "two_actual_horizontal_Velu_kernels": horizontal11,
        "norm3_endomorphism_eigenvalues": [alpha, alpha_bar],
        "two_local_branch_tangent_ratios": slopes11,
        "ordinary_unique_F47_necklace_continuation": True,
        "two_intersections_simple": True,
    }
    finalize_group("c11", [decorate(W11, "c11", ordinary_disk_id=c11["disk_id"],
                                    CM_discriminant=-11, j_integer=-32768,
                                    exact_CM_model=[A11, B11],
                                    local_intersection_multiplicity=2)], 1, multiplicity=2)

    # T3(b)=b+3v: all three nonhorizontal branches must return the same
    # actual 73-coordinate point after raw determinant3 level transport.
    roots0 = all_R2_three_roots(A0, B0)
    assert len(roots0) == 4 and (0, 0) in roots0
    v_candidates = []
    b_branch = None
    for root in roots0:
        At, Bt = velu_model(3, [cn(root), (1, 0)], A0, B0)
        node = {"ell": 3, "source_A": A0, "source_B": B0,
                "A": At, "B": Bt, "kernel": [cn(root), (1, 0)]}
        pair = level.raw_pair(node, Pc, Qc)
        rec = level.record(At, Bt, *pair, 3, [b_index])
        if root == (0, 0):
            assert rec["coarse"]["image_indices_1based"] == [b_index+1]
            assert full_j(At, Bt) == (0, 0)
            b_branch = rec
            continue
        assert cp(root, 3) == (-4 % Q, 0)
        assert full_j(At, Bt) == (-12288000 % Q, 0)
        key = rec["reference_key"]
        assert key == "9"
        idx = rec["image_indices_1based"][0]-1
        W = physical_values(key, tuple(rec["reference_parameter"]), tuple(rec["homothety"]), [idx])
        rec["kernel_x"] = root
        rec["target_model"] = [At, Bt]
        v_candidates.append((W, rec))
    assert b_branch is not None and len(v_candidates) == 3
    assert all(point_key(W) == point_key(v_candidates[0][0]) for W, _ in v_candidates)
    vW, vrec = v_candidates[0]
    finalize_group("v", [decorate(vW, "v_CM27", vrec["reference_key"],
                                  vrec["image_indices_1based"][0],
                                  CM_discriminant=-27, j_integer=-12288000,
                                  exact_CM_model=vrec["target_model"])], 1, multiplicity=0)
    state["T3_basepoint_branches"] = {
        "horizontal_branch": b_branch,
        "three_nonhorizontal_branches": [rec for _, rec in v_candidates],
        "all_three_nonhorizontal_actual_points_equal": True,
        "divisor_identity": "T3(b)=b+3v",
    }

    # Verify the whole actual degree32 support in the model's complete
    # quadratic multiplication table, not only selected interpolation rows.
    points = [p for name in ("Z12", "Z0fix", "c11", "v")
              for p in state["groups"][name]["points"]]
    W = r.from_json([v["W_mod47four"] for v in points])
    V2, V3 = a.evaluate(W)
    pa, pb = zip(*[(i, j) for i in range(73) for j in range(i, 73)])
    old_products = r.mul(r.cols(a.M["W"], pa), r.cols(a.M["W"], pb))
    coefficients = r.rows(old_products, a.M["P2"])
    assert r.equal(r.mm(a.M["V2"], coefficients), old_products)
    assert r.equal(r.mm(V2, coefficients), r.mul(r.cols(W, pa), r.cols(W, pb)))
    degree = sum(state["groups"][name]["total_degree"] for name in ("Z12", "Z0fix", "c11"))
    assert degree == 32
    state.update(
        complete=True, actual_fixed_divisor_degree=degree,
        actual_fixed_divisor="Q3=Z12+Z0fix+2c11",
        all_32_distinct_support_rows_quadratic_identity_count=len(points)*2701,
        all_full_quadratic_identities_verified=True,
        sigma_F3_basepoint_factor={"rational_factor": "2^(-9)",
                                  "factor_mod47four": pow(pow(2, 9, Q), -1, Q),
                                  "full_generic_coordinate": "2^(-9)*(a_b/a_P)^2",
                                  "horizontal_T3_at_b_j_tangent_ratio": -1},
        second_kind_integrals_computed=False,
        full_F3_height_computed=False,
        complete_QC_common_roots=False,
    )
    checkpoint()
    print("PASS ACTUAL Q3 degree32 and T3(b)=b+3v", sha(args.output), flush=True)


if __name__ == "__main__":
    main()
