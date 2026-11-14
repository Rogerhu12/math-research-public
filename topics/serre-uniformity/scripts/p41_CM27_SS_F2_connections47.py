#!/usr/bin/env python3
"""Actual F2 third-kind connections at the rational SS_j9_11 center; the constant is calibrated later at CM(-27)."""
import argparse
import gzip
import hashlib
import json
from pathlib import Path
import random
import sys
import time


def read(path):
    raw = Path(path).read_bytes()
    return json.loads(gzip.decompress(raw) if str(path).endswith(".gz") else raw)


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--script-dir", type=Path, required=True)
    ap.add_argument("--recovery-dir", type=Path, required=True)
    ap.add_argument("--disk-id", required=True)
    ap.add_argument("--result-id", required=True)
    ap.add_argument("--work-dir", type=Path, required=True)
    ap.add_argument("--output", type=Path, required=True)
    args = ap.parse_args()
    args.script_dir = args.script_dir.resolve()
    args.work_dir.mkdir(parents=True, exist_ok=True)
    sys.path.insert(0, str(args.script_dir))
    import numpy as np
    import p41_r2_matrix as r
    from p41_projective_jet_frames47 import install_exact_float_mm, ProjectiveJetFrames
    from p41_native_r2_linear47 import install
    from p41_actual_differentials47 import ActualModel, save
    from p41_elliptic_coarse_atlas47 import Series
    from p41_hecke3_hessian47 import section_jets
    install_exact_float_mm(r)
    install(r, args.work_dir / "native")
    a = ActualModel(args.script_dir)
    M, Q, Q3 = a.M, r.Q, 47**3
    frames = ProjectiveJetFrames(a)
    started = time.monotonic()
    source_hashes = {}

    def load(path):
        source_hashes[str(path)] = sha(path)
        return read(path)

    def standard(name):
        return load(args.script_dir / "data" / name)

    def cat(*xs):
        return tuple(np.concatenate([x[k] for x in xs], axis=0) for k in range(2))

    def transpose(x):
        return tuple(y.T.copy() for y in x)

    def sumrows(x, q=Q):
        return tuple(np.sum(y, axis=0, keepdims=True) % q for y in x)

    def keyrow(x, q=Q):
        return tuple((x[0][0] % q).tolist() + (x[1][0] % q).tolist())

    def kernel(x, rank):
        rr, cc = r.rank_pivots(x)
        assert len(rr) == rank, (len(rr), rank)
        out, _, _ = r.kernel_from_rows(r.rows(x, rr), rr, cc)
        assert r.iszero(r.mm(x, out))
        return out

    second = standard("p41_second_kind_connection47.json.gz")
    moved = standard("p41_second_kind_move_poles47.json.gz")
    large = load(args.recovery_dir / "p41_rational_SS_second_kind_integrals47_complete.json.gz")
    rhs = load(args.recovery_dir / "p41_SS_second_kind_rhs47.json.gz")
    cm = standard("p41_cm_quadratic_jets47_raw.json.gz")
    bases = standard("p41_hecke3_abel_bases_checkpoint.json.gz")
    oldeta = standard("p41_eta_calibration47_complete.json.gz")
    atlas = standard("p41_rational_SS_residue_atlas47_complete.json.gz")
    assert args.disk_id == "SS_j9_11"
    I1, I2 = [[i - 1 for i in x["points_1based"]] for x in bases["families"]]
    beta0 = -3 * pow(27652, -1, Q) % Q
    allpoints = {x["label"]: r.from_json([x["normalized_weight2_coefficients"][0]]) for x in cm["records"]}
    b, u, c7 = [allpoints[k] for k in ["P_minus3", "P_minus12", "P_minus7"]]
    z8 = cat(*[allpoints[k] for k in sorted(allpoints) if k.startswith("Z_minus8_")])
    assert z8[0].shape == (20, 73)
    chart = next(c for c in atlas["charts"] if args.disk_id in c["disk_ids"])
    chart_row = chart["disk_ids"].index(args.disk_id)
    assert r.equal(r.from_json(chart["frame"]), a.fc)
    Pcenter = r.rows(r.from_json(chart["W_coefficients_0to3"][0]), [chart_row])
    source_row = chart["original_input_rows_0based"][chart_row]
    assert chart["reference_key"] == "9" and source_row == 312
    Praw = r.rows(M["W"], [source_row])
    assert r.equal(Pcenter, r.mul(Praw, r.inverse_values(r.mm(Praw, a.fc)))), "Actual SS center must be the same original Hecke source point"
    w = r.from_json(moved["new_pole_denominator_w"])
    v = r.from_json(moved["old_pole_denominator_v"])
    Fn = r.from_json(moved["moving_function_quadratic_numerators_rational_basis"])
    Ci = a.reduce(r.from_json(moved["rational_to_original_change"]), Q3)
    allreal = np.asarray(large["geometric_real_U_mu_integrals_mod47cubed"], dtype=np.int64)
    vertex_map = {}
    chart_data = []
    for entry in rhs["charts"]:
        path = args.recovery_dir / "SS-second-kind-rhs" / entry["file"]
        assert sha(path) == entry["sha256"]
        ch = read(path)
        arr = [r.from_json(x) for x in ch["W_coefficients_0to3"]]
        prim = [r.from_json(x) for x in ch["primitive_coefficients_1to3"]]
        base = r.from_json(ch["coordinate_base_value"])
        coordinate = r.from_json(ch["coordinate"])
        k = len(chart_data)
        chart_data.append((arr, prim, base, coordinate))
        for row, vertex in enumerate(ch["vertices_0based"]):
            key = keyrow(r.rows(arr[0], [row]), 47)
            assert key not in vertex_map
            vertex_map[key] = (vertex, k, row)
    assert len(vertex_map) == 3154

    def Fvalues(W):
        vv, ww = r.mm(W, v), r.mm(W, w)
        assert np.all(r.units(vv)) and np.all(r.units(ww))
        return r.mul(r.mm(a.evaluate(W)[0], Fn), r.inverse_values(r.mul(vv, ww)))

    def rational_sum_U_mu(W):
        normalized = r.mul(W, r.inverse_values(r.mm(W, w)))
        keys = {keyrow(r.rows(normalized, [i])) for i in range(W[0].shape[0])}
        conjugated = r.mm(r.conjugate(W), r.conjugate(M["A1"]))
        conjugated = r.mul(conjugated, r.inverse_values(r.mm(conjugated, w)))
        assert keys == {keyrow(r.rows(conjugated, [i])) for i in range(W[0].shape[0])}
        total = np.zeros((1, 54), dtype=np.int64)
        maps = []
        for j in range(W[0].shape[0]):
            wp = r.rows(normalized, [j])
            vertex, k, row = vertex_map[keyrow(wp, 47)]
            arr, prim, base, coordinate = chart_data[k]
            z = r.sub(r.mm(wp, coordinate), r.rows(base, [row]))
            assert all(not np.any(x % 47) for x in z)
            actual = r.zeros(1, 73)
            for x in reversed(arr):
                actual = r.add(r.mul(actual, z), r.rows(x, [row]))
            assert r.equal(actual, wp), "Complete actual73 CM transport failed"
            tiny = r.zeros(1, 54)
            for x in reversed(prim):
                tiny = r.mul(r.add(tiny, r.rows(x, [row])), z)
            total = (total + allreal[vertex:vertex + 1] + 20 * tiny[0]) % Q3
            maps.append({"vertex_0based": vertex, "parameter": r.to_json(z), "all73_actual_coordinates": True})
        return (total, np.zeros_like(total)), maps

    Ub_mu, base_map = rational_sum_U_mu(b)
    Fb = a.reduce(Fvalues(b), Q3)
    FD = a.reduce(r.from_json(rhs["cusp_F_sum_mod47four"]), Q3)
    assert not np.any(Ub_mu[1]) and not np.any(Fb[1]) and not np.any(FD[1])
    Ub_nu = r.mm(r.add(r.sub(Ub_mu, a.scale(Fb, 20, Q3), Q3), FD, Q3), Ci, Q3)
    gradients = {}
    gradient_maps = {"b": base_map}
    for name, W in [("C", Pcenter), ("u_minus_b", u), ("c7_minus_b", c7), ("Z8_minus20b", z8)]:
        U, maps = rational_sum_U_mu(W)
        degree = W[0].shape[0]
        gmu = a.scale(r.sub(U, a.scale(Ub_mu, degree, Q3), Q3), pow(20, -1, Q3), Q3)
        FS = a.reduce(sumrows(Fvalues(W)), Q3)
        assert not np.any(FS[1])
        g = r.mm(r.sub(gmu, r.sub(FS, a.scale(Fb, degree, Q3), Q3), Q3), Ci, Q3)
        gradients[name] = g
        gradient_maps[name] = maps
    gradients["D_minus20b"] = r.neg(Ub_nu, Q3)
    for name, g in gradients.items():
        assert r.equal(r.conjugate(g, Q3), r.cols(g, second["pole_Frobenius_permutation_0based"])), name
    print("PASS actual rational SS divisor gradients, complete 73-coordinate transport including SS C", flush=True)
    a.field_setup()
    cusp_rows = []
    for index in [0, 11]:
        CV2, _ = a.cusp_evaluations(index)
        CW = a.field_coordinates(a.cusp["cusp_values"][index])
        cusp_rows.append((CW, CV2))
    rng = random.Random(4104725901)
    forms = {}
    form_certificates = {}

    def construct(name, WZ, residues, cusp_residue):
        n = WZ[0].shape[0]
        assert len(residues) == n and sum(residues) + 20 * cusp_residue == 0
        assert r.equal(r.mm(WZ, a.fc), r.column([[1, 0] for _ in range(n)])), (name, "finite points must use the actual fc=1 frame")
        V2Z, V3Z = a.evaluate(WZ)
        HZ = r.mm(V3Z, a.H)
        K = kernel(WZ, n)
        for attempt in range(200):
            seed = r.column([[rng.randrange(47), rng.randrange(47)] for _ in range(73 - n)])
            x = r.mm(K, seed)
            q = r.add(x, r.mm(M["A1"], r.conjugate(x)))
            assert r.iszero(r.mm(WZ, q))
            dq = r.mm(HZ, q)
            qsource = r.mm(M["W"], q)
            good = np.flatnonzero(r.units(qsource)[:, 0]).tolist()
            if len(good) < 790 or not all(i in good for i in I1 + I2):
                continue
            if not np.all(r.units(dq)):
                continue
            if name != "C" and not np.all(r.units(r.mm(Pcenter, q))):
                continue
            if any(all(not np.any(y % 47) for y in r.mm(CW, q)) for CW, CV2 in cusp_rows):
                continue
            break
        else:
            raise AssertionError((name, "no denominator"))
        E = r.rows(M["V2"], good)
        er, ec = r.rank_pivots(E)
        assert len(er) == 199 and ec == list(range(199))
        Ei = r.inverse_matrix(r.rows(E, er))
        iq = r.inverse_values(r.rows(qsource, good))
        constraint = r.zeros(0, 199)
        tests = []
        for _ in range(6):
            seed = r.column([[rng.randrange(47), rng.randrange(47)] for _ in range(73 - n)])
            g = r.mm(K, seed)
            scaled = r.mul(r.mul(r.rows(r.mm(M["W"], g), good), iq), E)
            residual = r.sub(scaled, r.mm(E, r.mm(Ei, r.rows(scaled, er))))
            joined = cat(constraint, residual)
            rr, cc = r.rank_pivots(joined)
            assert len(rr) <= 126 - n
            constraint = r.rows(joined, rr)
            tests.append(g)
            if len(rr) == 126 - n:
                break
        else:
            raise AssertionError((name, "colon saturation"))
        S = kernel(constraint, 126 - n)
        assert S[0].shape == (199, 73 + n)
        for g in tests:
            values = r.mul(r.mul(r.rows(r.mm(M["W"], g), good), iq), r.mm(E, S))
            assert r.equal(values, r.mm(E, r.mm(Ei, r.rows(values, er))))
        blocks = [r.mm(V2Z, S)]
        wanted = [r.mul(dq, r.column([[x, 0] for x in residues]))]
        for CW, CV2 in cusp_rows:
            blocks.append(a.scale(r.mm(CV2, S), 41))
            wanted.append(a.scale(r.mm(CW, q), cusp_residue))
        blocks.append(a.scale(r.mm(r.rows(M["V2"], I2), S), beta0))
        wanted.append(r.mul(a.reduce(r.rows(qsource, I2), Q3), transpose(gradients[name]), Q3))
        A = a.reduce(cat(*blocks), Q3)
        B = cat(*[a.reduce(x, Q3) for x in wanted])
        ar, ac = r.rank_pivots(A)
        assert len(ar) == 73 + n and ac == list(range(73 + n)), (name, len(ar))
        co = r.mm(r.inverse_matrix(r.rows(A, ar), Q3), r.rows(B, ar), Q3)
        assert r.equal(r.mm(A, co, Q3), B)
        numerator = r.mm(a.reduce(S, Q3), co, Q3)
        assert r.equal(r.mm(a.reduce(M["A2"], Q3), r.conjugate(numerator, Q3), Q3), numerator)
        forms[name] = (numerator, q)
        form_certificates[name] = {
            "numerator_quadratic_coefficients_mod47cubed": r.to_json(numerator),
            "denominator_linear_coefficients_mod47four": r.to_json(q),
            "finite_pole_coordinates_fc_normalized": r.to_json(WZ),
            "finite_residues": residues,
            "cusp_residue": cusp_residue,
            "denominator_attempt_0based": attempt,
            "good_source_rows": len(good),
            "colon_rank": 126 - n,
            "candidate_dimension": 73 + n,
            "all_residue_and_actual_family2_calibration_equations": True,
            "calibration_gradient_original_nu_mod47cubed": r.to_json(gradients[name]),
            "Frobenius": True,
        }
        save(args.work_dir / (name + "_connection47.json.gz"), form_certificates[name])
        print("PASS actual connection", name, "rank", 73 + n, "good rows", len(good), flush=True)

    construct("C", cat(Pcenter, b), [1, -1], 0)
    construct("u_minus_b", cat(u, b), [1, -1], 0)
    construct("c7_minus_b", cat(c7, b), [1, -1], 0)
    construct("Z8_minus20b", cat(z8, b), [1] * 20 + [-20], 0)
    construct("D_minus20b", b, [-20], 1)

    # The actual T2 trace, evaluated at all original source points first.
    hecke = standard("p41_hecke47_full_saved.json.gz")["operators"]["2"]
    permutation = [i - 1 for i in hecke["necklace_transport_1based"]]
    sC, qC = forms["C"]
    total = r.zeros(820, 1)
    goodmask = np.ones(820, dtype=bool)
    branch_counts = []
    for target in hecke["targets"]:
        W = r.from_json(target["evaluation_matrix"])
        V2, _ = a.evaluate(W)
        sv = r.mm(a.reduce(V2, Q3), sC, Q3)
        qv = r.mm(W, qC)
        ok = np.flatnonzero(r.units(qv)[:, 0]).tolist()
        val = r.zeros(820, 1)
        vv = r.mul(r.rows(sv, ok), r.inverse_values(a.reduce(r.rows(qv, ok), Q3), Q3), Q3)
        for k in range(2):
            val[k][ok] = vv[k]
        total = r.add(total, r.rows(val, permutation), Q3)
        goodmask &= r.units(qv)[:, 0][permutation]
        branch_counts.append(len(ok))
    total = a.scale(total, pow(2, -1, Q3), Q3)
    good = np.flatnonzero(goodmask).tolist()
    # Trace interpolation needs a faithful set of good source evaluations.
    # Calibration/tiny points may be zeros of the auxiliary qC and need not
    # themselves be evaluated through qC. The globally reconstructed sT/qT
    # below is separately required to have unit qT at every such point.
    assert len(good) > 504
    excluded_calibration_rows = [i for i in I1 + I2 if i not in good]
    WT = [r.rows(r.from_json(target["evaluation_matrix"]), [permutation[source_row]]) for target in hecke["targets"]]
    WT = [r.mul(W, r.inverse_values(r.mm(W, a.fc))) for W in WT]
    graph = standard("p41_SS_Hecke_graph47.json.gz")
    assert graph["vertices"][656]["chosen_reference"]["input_row_0based"] == source_row
    assert 656 not in graph["adjacency"]["2"][656]
    KT = kernel(cat(*WT, u), 4)
    for attempt in range(100):
        x = r.mm(KT, r.column([[rng.randrange(47), rng.randrange(47)] for _ in range(69)]))
        qT = r.add(x, r.mm(M["A1"], r.conjugate(x)))
        assert r.iszero(r.mm(cat(*WT, u), qT))
        qsource = r.mm(M["W"], qT)
        if np.all(r.units(r.rows(qsource, I1 + I2))) and np.all(r.units(r.mm(Pcenter, qT))):
            break
    else:
        raise AssertionError("No actual T2 denominator")
    E = a.reduce(r.rows(M["V2"], good), Q3)
    er, ec = r.rank_pivots(E)
    assert len(er) == 199 and ec == list(range(199))
    values = r.mul(a.reduce(r.rows(qsource, good), Q3), r.rows(total, good), Q3)
    sT = r.mm(r.inverse_matrix(r.rows(E, er), Q3), r.rows(values, er), Q3)
    assert r.equal(r.mm(E, sT, Q3), values)
    assert r.equal(r.mm(a.reduce(M["A2"], Q3), r.conjugate(sT, Q3), Q3), sT)
    for CW, CV2 in cusp_rows:
        assert r.iszero(r.mm(a.reduce(CV2, Q3), sT, Q3))
    forms["T2C"] = (sT, qT)
    form_certificates["T2C"] = {
        "numerator_quadratic_coefficients_mod47cubed": r.to_json(sT),
        "denominator_linear_coefficients_mod47four": r.to_json(qT),
        "actual_T2_target_pole_constraints": True,
        "branch_good_rows": branch_counts,
        "common_good_rows": len(good),
        "calibration_source_rows_not_used_for_trace_interpolation_0based": excluded_calibration_rows,
        "trace_denominator_unit_at_all_calibration_and_tiny_points": True,
        "all_actual_trace_equations_verified": True,
        "trace_scale": "1/2, actual R131 normalized Velu differential pullbacks",
        "complete_cusp_field_equations": True,
        "Frobenius": True,
    }
    save(args.work_dir / "T2C_connection47.json.gz", form_certificates["T2C"])
    print("PASS true T2 connection trace", len(good), "source equations", flush=True)

    # The actual SS center has source model A=1, B=32. All 73 projective
    # coordinates above agree with the original saved Hecke source, not only j.
    jp0 = 6912 * pow(4 + 27*32**2, -1, Q) % Q
    out = {
        "result": args.result_id, "disk_id": args.disk_id, "level": 41,
        "auxiliary_prime": 47, "precision": 4, "modulus": Q,
        "complete_actual_F2_connections_for_SS_disk": True,
        "complete_actual_local_sigma_F2_center_height": False,
        "actual_connections": form_certificates,
        "actual_SS_divisor_gradient_maps": gradient_maps,
        "actual_gradients_original_nu_mod47cubed": {k: r.to_json(x) for k,x in gradients.items()},
        "actual_j_at_SS_center_mod47four": jp0,
        "actual_T2_target_coordinates_fc_normalized": [r.to_json(W)[0] for W in WT],
        "actual_T2_source_row_0based": source_row,
        "actual_T2_target_row_0based": permutation[source_row],
        "actual_all73_SS_center_equals_original_source": True,
        "actual_T2_graph_neighbors": graph["adjacency"]["2"][656],
        "coefficient_precision": 3,
        "input_sha256": dict(a.inputs, **source_hashes),
        "source_sha256": sha(__file__), "runtime_seconds": round(time.monotonic()-started,3),
    }
    digest = save(args.output, out)
    print("PASS actual SS F2 connections", args.disk_id, "SHA", digest, flush=True)


if __name__ == "__main__":
    main()
