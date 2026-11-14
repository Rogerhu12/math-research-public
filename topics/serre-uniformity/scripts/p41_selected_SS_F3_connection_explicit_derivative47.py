#!/usr/bin/env python3
"""Actual third-kind connections and a genuine selected supersingular canonical F3 height."""
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
    ap.add_argument("--second-kind", type=Path, required=True)
    ap.add_argument("--principal", type=Path, required=True)
    ap.add_argument("--t3-support", type=Path, required=True)
    ap.add_argument("--full-norm", type=Path, required=True)
    ap.add_argument("--fixed-support", type=Path, required=True)
    ap.add_argument("--cm11-second", type=Path, required=True)
    ap.add_argument("--canonical", type=Path, required=True)
    ap.add_argument("--derivative", type=Path, required=True)
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
    Cdata = load(args.second_kind)
    principal = load(args.principal)
    T3support = load(args.t3_support)
    normdata = load(args.full_norm)
    canonical = load(args.canonical)
    fixed = load(args.fixed_support)
    cm11_second = load(args.cm11_second)
    cm_anchors = standard("p41_three_ordinary_CM_anchors_and_113_global_functions47.json.gz")
    all_tiny = standard("p41_all129_second_kind_tiny47_complete.json.gz")
    assert all(x["disk_id"] == args.disk_id for x in [Cdata, principal, normdata])
    assert T3support["source_disk_id"] == args.disk_id
    assert normdata["input_sha256"][args.second_kind.name] == sha(args.second_kind)
    assert normdata["input_sha256"][args.principal.name] == sha(args.principal)
    assert normdata["input_sha256"][args.canonical.name] == sha(args.canonical)
    I1, I2 = [[i - 1 for i in x["points_1based"]] for x in bases["families"]]
    beta0 = -3 * pow(27652, -1, Q) % Q
    allpoints = {x["label"]: r.from_json([x["normalized_weight2_coefficients"][0]]) for x in cm["records"]}
    b = allpoints["P_minus3"]
    def fixed_group(name):
        group = fixed["groups"][name]
        assert group["actual_Frobenius_stable_mod47four"] and group["all_fc_unit"]
        return r.from_json([x["W_mod47four"] for x in group["points"]])
    v27, c11, z12, z0 = [fixed_group(k) for k in ["v", "c11", "Z12", "Z0fix"]]
    assert z12[0].shape == (22, 73) and z0[0].shape == (8, 73)
    b_indices = [i for i,x in enumerate(fixed["groups"]["Z0fix"]["points"]) if x["is_basepoint_b"]]
    assert len(b_indices) == 1 and r.equal(r.rows(z0, b_indices), b)
    z0_other = r.rows(z0, [i for i in range(8) if i not in b_indices])
    chart=next(c for c in atlas['charts'] if args.disk_id in c['disk_ids'])
    row=chart['disk_ids'].index(args.disk_id)
    assert r.equal(r.from_json(chart['frame']),a.fc)
    Pcenter=r.rows(r.from_json(chart['W_coefficients_0to3'][0]),[row])
    assert T3support['complete_actual_T3_support'] and T3support['source_all73_equals_original_rational_SS_center']
    assert r.equal(Pcenter,r.from_json([T3support['actual_source_W_fc_normalized']]))
    assert r.equal(r.mm(Pcenter,a.fc),r.column([[1,0]]))
    Pchart=frames.local_jets(Pcenter,a.fc,r.from_json(chart['coordinate']),order=1)
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
    for name, W in [("v_minus_b", v27), ("Z12_minus22b", z12), ("Z0fix_minus8b", z0)]:
        U, maps = rational_sum_U_mu(W)
        degree = W[0].shape[0]
        gmu = a.scale(r.sub(U, a.scale(Ub_mu, degree, Q3), Q3), pow(20, -1, Q3), Q3)
        FS = a.reduce(sumrows(Fvalues(W)), Q3)
        assert not np.any(FS[1])
        g = r.mm(r.sub(gmu, r.sub(FS, a.scale(Fb, degree, Q3), Q3), Q3), Ci, Q3)
        gradients[name] = g
        gradient_maps[name] = maps
    # The ordinary CM(-11) point is transported using its original nu,
    # its own ORD_j38 center, and all54 true tiny primitives in that exact chart.
    anchor = next(x for x in cm_anchors["three_ordinary_CM_anchors"] if x["discriminant"] == -11)
    assert cm11_second["disk_id"] == anchor["disk_id"] == "ORD_j38"
    assert r.equal(c11, r.from_json(anchor["physical_CM_W_in_chart_frame_mod47four"]))
    tiny_chart = next(x for x in all_tiny["charts"] if "ORD_j38" in x["disk_ids"])
    ti = tiny_chart["disk_ids"].index("ORD_j38")
    ycm = anchor["rescaled_parameter_y_of_CM_point_mod47cubed"]
    cm11gradient = r.from_json(cm11_second["actual54_second_kind_integrals_of_C_mod47four"])
    for k, data in enumerate(tiny_chart["second_kind_tiny_coefficients_1to3_in_y_mod47four"]):
        cm11gradient = r.add(cm11gradient, a.scale(r.rows(r.from_json(data), [ti]), pow(ycm,k+1,Q)))
    gradients["c11_minus_b"] = a.reduce(cm11gradient, Q3)
    gradient_maps["c11_minus_b"] = {"ordinary_disk_id":"ORD_j38", "y_mod47cubed":ycm,
                                   "all73_actual_CM_coordinates_match":True,
                                   "all54_original_nu_center_and_tiny_used":True}
    gradients["D_minus20b"] = r.neg(Ub_nu, Q3)
    gradients["C"] = a.reduce(r.from_json(Cdata["actual54_second_kind_integrals_of_C_mod47four"]), Q3)
    knownC=next(x for x in large['rational_SS_center_integrals'] if x['disk_id']==args.disk_id)
    assert r.equal(gradients['C'],r.from_json([knownC['C_original_nu_coordinates_mod47cubed']],Q3))
    print('PASS principal-transport second-kind constants equal independent SS Hecke solution',flush=True)
    for name, g in gradients.items():
        assert r.equal(r.conjugate(g, Q3), r.cols(g, second["pole_Frobenius_permutation_0based"])), name
    print("PASS actual rational SS divisor gradients, complete CM transports and selected SS C", flush=True)
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
    construct("v_minus_b", cat(v27, b), [1, -1], 0)
    construct("c11_minus_b", cat(c11, b), [1, -1], 0)
    construct("Z12_minus22b", cat(z12, b), [1] * 22 + [-22], 0)
    construct("Z0fix_minus8b", cat(z0_other, b), [1] * 7 + [-7], 0)
    construct("D_minus20b", b, [-20], 1)

    # The actual T3 trace, evaluated at all original source points first.
    hecke = standard("p41_hecke47_full_saved.json.gz")["operators"]["3"]
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
    total = a.scale(total, pow(3, -1, Q3), Q3)
    good = np.flatnonzero(goodmask).tolist()
    assert len(good) > 504
    WT = [r.from_json([x]) for x in T3support["actual_T3_targets_fc_normalized"]]
    KT = kernel(cat(*WT, b, v27), 6)
    for attempt in range(100):
        x = r.mm(KT, r.column([[rng.randrange(47), rng.randrange(47)] for _ in range(67)]))
        qT = r.add(x, r.mm(M["A1"], r.conjugate(x)))
        assert r.iszero(r.mm(cat(*WT, b, v27), qT))
        qsource = r.mm(M["W"], qT)
        if np.all(r.units(r.rows(qsource, I1 + I2))):
            break
    else:
        raise AssertionError("No actual T3 denominator")
    E = a.reduce(r.rows(M["V2"], good), Q3)
    er, ec = r.rank_pivots(E)
    assert len(er) == 199 and ec == list(range(199))
    values = r.mul(a.reduce(r.rows(qsource, good), Q3), r.rows(total, good), Q3)
    sT = r.mm(r.inverse_matrix(r.rows(E, er), Q3), r.rows(values, er), Q3)
    assert r.equal(r.mm(E, sT, Q3), values)
    assert r.equal(r.mm(a.reduce(M["A2"], Q3), r.conjugate(sT, Q3), Q3), sT)
    for CW, CV2 in cusp_rows:
        assert r.iszero(r.mm(a.reduce(CV2, Q3), sT, Q3))
    forms["T3C"] = (sT, qT)
    form_certificates["T3C"] = {
        "numerator_quadratic_coefficients_mod47cubed": r.to_json(sT),
        "denominator_linear_coefficients_mod47four": r.to_json(qT),
        "actual_T3_target_pole_constraints": True,
        "branch_good_rows": branch_counts,
        "common_good_rows": len(good),
        "all_actual_trace_equations_verified": True,
        "trace_scale": "1/3, actual R131 normalized Velu differential pullbacks",
        "new_denominator_unit_at_all108_calibration_rows": True,
        "removed_old_expression_source_rows": [i for i in I1+I2 if i not in good],
        "T3P_and_b_and_v_constraint_rank":6,
        "complete_cusp_field_equations": True,
        "Frobenius": True,
    }
    save(args.work_dir / "T3C_connection47.json.gz", form_certificates["T3C"])
    print("PASS true T3 connection trace", len(good), "source equations", flush=True)

    # Integrate in precisely the actual family1 physical parameters from R252.
    source = standard("p41_source_cubic47_full_saved.json.gz")
    Wjets = [r.from_json(x) for x in source["evaluation_coefficients"][:4]]
    V2jets, V3jets = section_jets(Wjets, [a.model, a.cusp, a.cm4, a.group], M, r)
    S3, S4 = Series(a, 3), Series(a, 4)
    den = [r.column([[27652, 0]]), r.column([[1728, 0]]), r.column([[27, 0]])]
    beta = [a.scale(x, -3) for x in S3.inverse(den)]
    parameters = r.from_json(principal["combined_function_to_actual_A1_t"]["actual_A1_physical_parameters"])
    if parameters[0].shape == (54, 1):
        parameters = transpose(parameters)
    assert parameters[0].shape == (1, 54)
    assert all(not np.any(x % 47) for x in parameters)

    def integrate(omega):
        power = parameters
        total = r.zeros(1, 1)
        for k, x in enumerate(omega):
            total = r.add(total, a.scale(r.mm(power, x), pow(k + 1, -1, Q)))
            power = r.mul(power, parameters)
        assert not np.any(total[1])
        return int(total[0][0, 0])

    coefficients = {}
    tiny = {}
    for name, (s, q) in forms.items():
        sv = [r.mm(a.reduce(r.rows(x, I1), Q3), s, Q3) for x in V2jets[:3]]
        qv = [r.mm(r.rows(x, I1), q) for x in Wjets[:3]]
        assert np.all(r.units(qv[0])), (name, "family1 denominator")
        omega = S3.mul(S3.mul(sv, S3.inverse(qv)), beta)
        coefficients[name] = omega
        tiny[name] = integrate(omega)
    sB = r.from_json(oldeta["numerator_coefficients"], Q3)
    qB = r.from_json(oldeta["denominator_coefficients"], Q3)
    Bsv = [r.mm(a.reduce(r.rows(x, I1), Q3), sB, Q3) for x in V3jets[:3]]
    Bqv = [r.mm(a.reduce(r.rows(x, I1), Q3), qB, Q3) for x in V2jets[:3]]
    omegaB = S3.mul(S3.mul(Bsv, S3.inverse(Bqv)), beta)
    coefficients["B"] = omegaB
    tiny["B"] = integrate(omegaB)
    g1 = r.mm(a.K1, r.from_json(canonical["canonical_coefficients"]))
    G = [r.mm(r.rows(x, I1), g1) for x in Wjets]
    assert np.all(r.units(G[0])), "Actual canonical divisor intersects family1"
    dlogg = S3.mul([a.scale(G[k + 1], k + 1) for k in range(3)], S3.inverse(G[:3]))
    # At A=1,B=32+t, beta=-3/d and j=6912/d. The exact logarithmic
    # derivative of beta/j' is d'/d-d''/d'.
    dprime = [r.column([[1728, 0]]), r.column([[54, 0]]), r.column([[0, 0]])]
    dlogd = S3.mul(dprime, S3.inverse(den))
    dlogdprime = [a.scale(x, 54) for x in S3.inverse(dprime)]
    j = [a.scale(x, 6912) for x in S4.inverse(den + [r.column([[0, 0]])])]
    jp = [a.scale(j[k + 1], k + 1) for k in range(3)]
    jm = list(j[:3])
    jm[0] = r.sub(jm[0], r.column([[1728, 0]]))
    jlog = S3.mul(jp, S3.inverse(j[:3]))
    jmlog = S3.mul(jp, S3.inverse(jm))
    etaK = []
    for k in range(3):
        x = r.add(dlogg[k], r.sub(dlogd[k], dlogdprime[k]))
        x = r.add(x, a.scale(jlog[k], 2 * pow(3, -1, Q)))
        x = r.add(x, a.scale(jmlog[k], pow(2, -1, Q)))
        x = r.add(x, a.scale(coefficients["D_minus20b"][k], 16 * pow(3, -1, Q)))
        x = r.sub(x, a.scale(omegaB[k], pow(2, -1, Q)))
        etaK.append(x)
    coefficients["K_g1_minus106b"] = etaK
    tiny["K_g1_minus106b"] = integrate(etaK)
    weights = {"T3C": 9, "C": 2, "v_minus_b": 54, "Z12_minus22b": -9,
               "Z0fix_minus8b": -9, "c11_minus_b": -18, "K_g1_minus106b": 2}
    omegaD = [r.zeros(54, 1) for _ in range(3)]
    for name, weight in weights.items():
        for k in range(3):
            omegaD[k] = r.add(omegaD[k], a.scale(coefficients[name][k], weight))
    tinyD = integrate(omegaD)
    assert tinyD == sum(weights[name] * tiny[name] for name in weights) % Q
    # Accurate canonical fibre coordinate in the same j-tangent frames.
    scales = standard("p41_cm12_scales47_certificate.json")
    abf = r.from_json(scales["canonical_source_dj_value"])
    ab = r.mul(abf, r.mm(b, g1))
    derivative=load(args.derivative.resolve(strict=True))
    assert derivative['all820_cubic_derivative_equalities'] and derivative['all820_old_new_derivation_cross_equalities']
    clearing_at_P=r.mm(Pcenter,r.from_json(derivative['chosen_clearing_section']))
    assert np.all(r.units(clearing_at_P))
    from p41_elliptic_coarse_atlas47 import ClassicalInvariants
    from types import SimpleNamespace
    iv=ClassicalInvariants(SimpleNamespace(a=a,r=r,v=r.from_json(derivative['chosen_clearing_section']),G=r.from_json(derivative['cleared_derivative_coefficients']))).series(Pchart['W'])
    S2=Series(a,2)
    A3v3=S2.mul(S2.power(iv['Av'],3),S2.power(iv['v'],3))
    jden=S2.add(S2.scale(A3v3,4),S2.scale(S2.power(iv['Bv3'],2),27))
    assert np.all(r.units(jden[0]))
    sourcej=S2.scale(S2.mul(A3v3,S2.inverse(jden)),6912)
    assert np.all(r.units(sourcej[1]))
    apoint=r.mul(r.mul(r.mm(Pcenter,g1),Pchart['inverse_Hc'][0]),r.inverse_values(sourcej[1]))
    assert not np.any(ab[1]) and not np.any(apoint[1]) and not np.any(sourcej[0][1])
    ab,apoint=int(ab[0][0,0]),int(apoint[0][0,0]);assert ab%47 and apoint%47
    jp0=int(sourcej[0][0][0,0]);assert jp0==T3support['actual_source_j_mod47four']
    assert all((jp0-x)%47 for x in [0,1728])
    actual_fixed=cat(b,v27,c11,z12,z0)
    assert all(keyrow(Pcenter,47)!=keyrow(r.rows(actual_fixed,[i]),47) for i in range(actual_fixed[0].shape[0]))
    for target in T3support['branch_records']:
        wt=r.from_json([target['W_actual_values_in_R2']])
        assert keyrow(Pcenter,47)!=keyrow(wt,47) and keyrow(b,47)!=keyrow(wt,47)
    assert T3support['all_four_targets_separate_from_source']
    tangent_rows=normdata['reused_P_and_b_in_the_same_j_tangents']
    nrP=next(x for x in tangent_rows if x['label']==args.disk_id)
    nrb=next(x for x in tangent_rows if x['label']=='P_minus3')
    assert nrP['j_tangent']['g1_differential_over_dj']==[apoint,0]
    assert nrb['j_tangent']['g1_differential_over_dj']==[ab,0]

    def logunit(x):
        z = (pow(x, 46, Q) - 1) % Q
        assert z % 47 == 0
        return (z - z*z*pow(2, -1, Q) + z*z*z*pow(3, -1, Q)) * pow(46, -1, Q) % Q

    sigma = pow(2, -9, Q) * pow(ab * pow(apoint, -1, Q) % Q, 2, Q) % Q
    assert fixed["sigma_F3_basepoint_factor"]["factor_mod47four"] == pow(2,-9,Q)
    logsigma = logunit(sigma)
    scale = int(normdata["actual_integer_scale"])
    lognorm = int(normdata["actual_log_norm_Phi_on_F3_second_divisor_mod47four"])
    assert scale % 47 == 9
    value = (logsigma + pow(scale, -1, Q) * (tinyD + lognorm)) % Q
    out = {
        "result": args.result_id,
        "level": 41, "auxiliary_prime": 47, "precision": 4, "modulus": Q,
        "disk_id": args.disk_id,
        "complete_actual_local_sigma_F3_center_height": True,
        "complete_all53_local_QC_heights": False, "complete_common_roots": False,
        "actual_connections": form_certificates,
        "actual_SS_divisor_gradient_maps": gradient_maps,
        "actual_gradients_original_nu_mod47cubed": {k: r.to_json(x) for k, x in gradients.items()},
        "physical_family1_parameters": r.to_json(parameters),
        "integrand_coefficients_0to2": {k: [r.to_json(x) for x in v] for k, v in coefficients.items()},
        "all_actual_tiny_integrals_mod47four": tiny,
        "second_divisor_tiny_integral_mod47four": tinyD,
        "actual_j_at_SS_center_mod47four": jp0,
        "same_j_tangent_as_complete_principal_norm_verified": True,
        "explicit_derivative_sha256": sha(args.derivative),
        "actual_clearing_section_value_at_source": r.to_json(clearing_at_P),
        "all_actual_level_pole_separations_verified": True,
        "principal_integrals_match_independent_R247_SS_solution": True,
        "source_j_coefficients_0to1_in_original_chart": [r.to_json(x) for x in sourcej],
        "actual_g1_over_dj_at_base_and_center": [ab, apoint],
        "canonical_sigma_fibre_coordinate_mod47four": sigma,
        "canonical_sigma_coordinate_log_mod47four": logsigma,
        "first_variable_principal_log_norm_mod47four": lognorm,
        "actual_integer_scale": scale,
        "actual_local_sigma_F3_height_mod47four": value,
        "formula": "Lambda(sigma_F3)=log(2^(-9)*(a_b/a_P)^2)+(integral_A1 eta_D+log Phi_C[D])/m",
        "fixed_base_self_intersection_unit_factor":pow(2,-9,Q),
        "second_divisor_connection_weights":weights,
        "canonical_connection_identity": "eta_(Kg1-106b)=dlog(g1/dj)+(2/3)dlogj+(1/2)dlog(j-1728)+(16/3)eta_(D-20b)-(1/2)eta_B",
        "coefficient_precision": 3,
        "tail_bound": "All family1 denominator constants are units. Its54 actual parameters are in47R2, so omitted integration terms n>=4 have valuation at least4.",
        "input_sha256": dict(a.inputs, **source_hashes),
        "source_sha256": sha(__file__),
        "runtime_seconds": round(time.monotonic() - started, 3),
    }
    digest = save(args.output, out)
    print("PASS actual canonical F3 center height", value, "tiny", tinyD, "SHA", digest, flush=True)


if __name__ == "__main__":
    main()
