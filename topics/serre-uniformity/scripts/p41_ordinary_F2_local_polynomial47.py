#!/usr/bin/env python3
"""Actual moving third-kind connection and canonical F2 height on ORD_j05."""
import argparse
import gzip
import hashlib
import json
from pathlib import Path
import random
import sys
import time
from types import SimpleNamespace


def read(p):
    b = Path(p).read_bytes()
    return json.loads(gzip.decompress(b) if str(p).endswith(".gz") else b)


def sha(p):
    return hashlib.sha256(Path(p).read_bytes()).hexdigest()


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--script-dir", type=Path, required=True)
    ap.add_argument("--center", type=Path, required=True)
    ap.add_argument("--tiny", type=Path, required=True)
    ap.add_argument("--work-dir", type=Path, required=True)
    ap.add_argument("--output", type=Path, required=True)
    args = ap.parse_args()
    args.script_dir = args.script_dir.resolve()
    args.work_dir.mkdir(parents=True, exist_ok=True)
    sys.path.insert(0, str(args.script_dir))
    import numpy as np
    import p41_r2_matrix as r
    from p41_actual_differentials47 import ActualModel, save
    from p41_native_r2_linear47 import install
    from p41_projective_jet_frames47 import ProjectiveJetFrames, install_exact_float_mm
    from p41_elliptic_coarse_atlas47 import ClassicalInvariants, Series
    install_exact_float_mm(r)
    install(r, args.work_dir / "native")
    a = ActualModel(args.script_dir)
    frames = ProjectiveJetFrames(a)
    Q, q, M, N = r.Q, 47**3, a.M, 3
    started = time.monotonic()
    inputs = {}

    def load(p):
        inputs[str(p)] = sha(p)
        return read(p)

    def standard(name):
        return load(args.script_dir / "data" / name)

    def red(x):
        return a.reduce(x, q)

    def cat(*xs):
        return tuple(np.concatenate([x[k] for x in xs], axis=0) for k in range(2))

    def tr(x):
        return tuple(y.T.copy() for y in x)

    def scalar(n):
        return r.column([[n % q, 0]])

    def smul(xs, ys, length=N):
        out = []
        for n in range(length):
            z = None
            for k in range(n + 1):
                if k < len(xs) and n-k < len(ys):
                    w = r.mul(xs[k], ys[n-k], q)
                    z = w if z is None else r.add(z, w, q)
            assert z is not None
            out.append(z)
        return out

    def sinv(xs, length=N):
        out = [r.inverse_values(xs[0], q)]
        for n in range(1, length):
            v = r.zeros(*xs[0][0].shape)
            for k in range(1, min(n, len(xs)-1) + 1):
                v = r.add(v, r.mul(xs[k], out[n-k], q), q)
            out.append(r.neg(r.mul(out[0], v, q), q))
        return out

    def spow(xs, n, length=N):
        assert n >= 1
        out = xs
        for _ in range(n-1):
            out = smul(out, xs, length)
        return out

    def mmconv(xs, ys, length=N):
        out = []
        for n in range(length):
            v = None
            for k in range(n+1):
                if k < len(xs) and n-k < len(ys):
                    w = r.mm(xs[k], ys[n-k], q)
                    v = w if v is None else r.add(v, w, q)
            assert v is not None
            out.append(v)
        return out

    def kernel(x, rank):
        rr, cc = r.rank_pivots(x)
        assert len(rr) == rank, (len(rr), rank)
        K, _, _ = r.kernel_from_rows(r.rows(x, rr), rr, cc)
        assert r.iszero(r.mm(x, K))
        return K

    center = load(args.center)
    tiny = load(args.tiny)
    atlas = standard("p41_ordinary_rational_atlas47.json.gz")
    ch = next(x for x in atlas["charts"] if "ORD_j05" in x["disk_ids"])
    row = ch["disk_ids"].index("ORD_j05")
    W0 = r.rows(r.from_json(ch["W_coefficients_0to3"][0]), [row])
    frame, coordinate = [r.from_json(ch[k]) for k in ["frame", "coordinate"]]
    assert r.equal(frame, a.fc), "This executor uses the recorded fc chart"
    J = frames.local_jets(W0, frame, coordinate, order=4)
    for name in ["W", "V2", "V3"]:
        for k in range(4):
            assert r.equal(J[name][k], r.rows(r.from_json(ch[name+"_coefficients_0to3"][k]), [row]))
    tchart = next(x for x in tiny["charts"] if "ORD_j05" in x["disk_ids"])
    trow = tchart["disk_ids"].index("ORD_j05")
    assert tchart["frame"] == ch["frame"] and tchart["coordinate"] == ch["coordinate"]
    nu = [red(r.rows(r.from_json(x), [trow])) for x in tchart["nu_coefficients_0to2_mod47four"]]
    gc = [red(r.from_json(center["actual_gradients_original_nu_mod47cubed"]["C"])),
          nu[0], a.scale(nu[1], pow(2, -1, q), q)]
    connection = center["actual_connections"]["C"]
    q0 = r.from_json(connection["denominator_linear_coefficients_mod47four"])
    s0 = r.from_json(connection["numerator_quadratic_coefficients_mod47cubed"], q)
    WZ = r.from_json(connection["finite_pole_coordinates_fc_normalized"])
    assert r.equal(W0, r.rows(WZ, [0]))
    b = r.rows(WZ, [1])
    V2b, V3b = a.evaluate(b)
    Hb = r.mm(V3b, a.H)
    rng = random.Random(4104726201)
    Kb = kernel(b, 1)
    for attempt in range(100):
        xx = r.mm(Kb, r.column([[rng.randrange(47), rng.randrange(47)] for _ in range(72)]))
        ell = r.add(xx, r.mm(M["A1"], r.conjugate(xx)))
        if np.all(r.units(r.mm(W0, ell))):
            break
    else:
        raise AssertionError("No moving denominator correction")
    assert r.iszero(r.mm(b, ell))
    S4 = Series(a, 3)

    def moving_section(g0):
        values = [r.mm(w, g0) for w in J["W"][:3]]
        ellvalues = [r.mm(w, ell) for w in J["W"][:3]]
        ratio = S4.mul(values, S4.inverse(ellvalues))
        assert r.iszero(ratio[0])
        out = [r.sub(g0, r.mul(ell, ratio[0]))]
        out += [r.neg(r.mul(ell, ratio[k])) for k in range(1, 3)]
        for n in range(3):
            val = r.zeros(1, 1)
            for k in range(n+1):
                val = r.add(val, r.mm(J["W"][k], out[n-k]))
            assert r.iszero(val) and r.iszero(r.mm(b, out[n]))
            assert r.equal(r.mm(M["A1"], r.conjugate(out[n])), out[n])
        return out

    qjets_full = moving_section(q0)
    qjets = [red(x) for x in qjets_full]
    qsource = [r.mm(red(M["W"]), x, q) for x in qjets]
    good = np.flatnonzero(r.units(qsource[0])[:, 0]).tolist()
    assert len(good) > 378
    E = red(r.rows(M["V2"], good))
    er, ec = r.rank_pivots(E)
    assert len(er) == 199 and ec == list(range(199))
    Ei = r.inverse_matrix(r.rows(E, er), q)
    iq = sinv([r.rows(x, good) for x in qsource])
    Kpb = kernel(WZ, 2)
    colon = [[] for _ in range(3)]
    colon_tests = []
    for attempt in range(6):
        xx = r.mm(Kpb, r.column([[rng.randrange(47), rng.randrange(47)] for _ in range(71)]))
        gg = r.add(xx, r.mm(M["A1"], r.conjugate(xx)))
        gjets = moving_section(gg)
        gsource = [r.mm(red(r.rows(M["W"], good)), red(x), q) for x in gjets]
        ratios = smul(gsource, iq)
        for k in range(3):
            B = r.mul(ratios[k], E, q)
            residual = r.sub(B, r.mm(E, r.mm(Ei, r.rows(B, er), q), q), q)
            colon[k].append(residual)
        colon_tests.append([r.to_json(x) for x in gjets])
        cr, cc = r.rank_pivots(cat(*colon[0]))
        assert len(cr) <= 124
        if len(cr) == 124:
            break
    else:
        raise AssertionError("Moving colon not saturated")
    colon = [cat(*x) for x in colon]
    print("PASS moving colon rank124 on", len(good), "faithful rows; tests", len(colon_tests), flush=True)
    bases = standard("p41_hecke3_abel_bases_checkpoint.json.gz")
    I2 = [i-1 for i in bases["families"][1]["points_1based"]]
    beta0 = -3 * pow(27652, -1, q) % q
    calA = a.scale(red(r.rows(M["V2"], I2)), beta0, q)
    calB = smul([r.rows(x, I2) for x in qsource], [tr(x) for x in gc])
    HP = [red(r.mm(x, a.H)) for x in J["V3"][:3]]
    resP = mmconv(HP, qjets)
    a.field_setup()
    cusp_blocks = []
    for index in [0, 11]:
        CV2, _ = a.cusp_evaluations(index)
        cusp_blocks.append(a.scale(red(CV2), 41, q))
    A, B = [], []
    for k in range(3):
        A.append(cat(colon[k], red(J["V2"][k]),
                     red(V2b) if k == 0 else r.zeros(1, 199),
                     *[x if k == 0 else r.zeros(*x[0].shape) for x in cusp_blocks],
                     calA if k == 0 else r.zeros(54, 199)))
        B.append(cat(r.zeros(colon[k][0].shape[0], 1), resP[k],
                     r.neg(r.mm(red(Hb), qjets[k], q), q),
                     *[r.zeros(x[0].shape[0], 1) for x in cusp_blocks], calB[k]))
    ar, ac = r.rank_pivots(A[0])
    assert len(ar) == 199 and ac == list(range(199))
    Ai = r.inverse_matrix(r.rows(A[0], ar), q)
    sjets = []
    for n in range(3):
        wanted = B[n]
        for k in range(1, n+1):
            wanted = r.sub(wanted, r.mm(A[k], sjets[n-k], q), q)
        sn = r.mm(Ai, r.rows(wanted, ar), q)
        assert r.equal(r.mm(A[0], sn, q), wanted), ("moving all equations", n)
        assert r.equal(r.mm(red(M["A2"]), r.conjugate(sn, q), q), sn)
        sjets.append(sn)
    assert r.equal(sjets[0], s0)
    moving_cert = {
        "q_linear_coefficients_in_parameter_0to2_mod47four": [r.to_json(x) for x in qjets_full],
        "s_quadratic_coefficients_in_parameter_0to2_mod47cubed": [r.to_json(x) for x in sjets],
        "gradient_original_nu_coefficients_0to2_mod47cubed": [r.to_json(x) for x in gc],
        "colon_test_sections_0to2_mod47four": colon_tests,
        "good_source_rows": good, "full_equation_rows": A[0][0].shape[0],
        "unit_minor_rows": ar, "all_three_coefficient_equations": True,
        "center_matches_R259": True, "Frobenius": True,
    }
    save(args.work_dir / "actual_C_moving_connection47.json.gz", moving_cert)
    print("PASS actual moving C connection all", 3*A[0][0].shape[0], "rows", flush=True)

    # Take the true T2 pullback-trace at fixed global source points.
    hecke = standard("p41_hecke47_full_saved.json.gz")["operators"]["2"]
    permutation = [i-1 for i in hecke["necklace_transport_1based"]]
    totals = [r.zeros(820, 1) for _ in range(3)]
    goodmask = np.ones(820, dtype=bool)
    target_counts = []
    for target in hecke["targets"]:
        Wt = red(r.from_json(target["evaluation_matrix"]))
        V2t, _ = a.evaluate(Wt)
        sv = [r.mm(red(V2t), x, q) for x in sjets]
        qv = [r.mm(Wt, x, q) for x in qjets]
        hit = np.flatnonzero(r.units(qv[0])[:, 0]).tolist()
        values = smul([r.rows(x, hit) for x in sv], sinv([r.rows(x, hit) for x in qv]))
        for k in range(3):
            vv = r.zeros(820, 1)
            for t in range(2):
                vv[t][hit] = values[k][t]
            totals[k] = r.add(totals[k], r.rows(vv, permutation), q)
        goodmask &= r.units(qv[0])[:, 0][permutation]
        target_counts.append(len(hit))
    totals = [a.scale(x, pow(2, -1, q), q) for x in totals]
    tgood = np.flatnonzero(goodmask).tolist()
    assert len(tgood) > 504
    qT = r.from_json(center["actual_connections"]["T2C"]["denominator_linear_coefficients_mod47four"])
    qTs = red(r.mm(M["W"], qT))
    qTcube = r.mul(r.mul(qTs, qTs, q), qTs, q)
    # Honest V4 basis, constructed as selected products W_i V3_j.
    E4 = r.zeros(820, 0)
    pairs = []
    for wi in range(73):
        block = r.mul(red(r.cols(M["W"], [wi])), red(M["V3"]), q)
        joined = r.hcat(E4, block)
        rr, cc = r.rank_pivots(joined)
        assert len(rr) <= 451
        proposed = pairs + [[wi, j] for j in range(325)]
        pairs = [proposed[j] for j in cc]
        E4 = r.cols(joined, cc)
        if len(rr) == 451:
            break
    else:
        raise AssertionError("Actual V4 rank")
    er4, ec4 = r.rank_pivots(r.rows(E4, tgood))
    assert len(er4) == 451 and ec4 == list(range(451))
    selected4 = [tgood[j] for j in er4]
    E4i = r.inverse_matrix(r.rows(E4, selected4), q)
    tcoeff = []
    for k in range(3):
        values = r.mul(qTcube, totals[k], q)
        co = r.mm(E4i, r.rows(values, selected4), q)
        assert r.equal(r.mm(r.rows(E4, tgood), co, q), r.rows(values, tgood)), ("actual T2 V4", k)
        tcoeff.append(co)
    # At order zero, the newly interpolated V4 section must equal qT^2*sT.
    sT = r.from_json(center["actual_connections"]["T2C"]["numerator_quadratic_coefficients_mod47cubed"], q)
    expect = r.mul(r.mul(qTs, qTs, q), r.mm(red(M["V2"]), sT, q), q)
    assert r.equal(r.mm(E4, tcoeff[0], q), expect)
    print("PASS actual T2 moving trace", len(tgood), "rows x3; faithful V4 dimension451", flush=True)
    V4P = []
    for k in range(3):
        row4 = r.zeros(1, 451)
        for h in range(k+1):
            product = r.mul(r.cols(red(J["W"][h]), [p[0] for p in pairs]),
                            r.cols(red(J["V3"][k-h]), [p[1] for p in pairs]), q)
            row4 = r.add(row4, product, q)
        V4P.append(row4)
    tv = mmconv(V4P, tcoeff)
    qtP = [red(r.mm(w, qT)) for w in J["W"][:3]]
    assert np.all(r.units(qtP[0])), "No self T2 intersection in this disk"
    invhc = [red(x) for x in J["inverse_Hc"][:3]]
    t2diag = smul(smul(tv, sinv(spow(qtP, 3))), invhc)

    # Regularize only after subtracting the actual moving simple pole.
    numerator_diag = mmconv([red(x) for x in J["V2"][:3]], sjets)
    numerator_derivative = mmconv([a.scale(red(J["V2"][k+1]), k+1, q) for k in range(3)], sjets)
    h = [red(x) for x in J["Hc"][:3]]
    hp = [a.scale(red(J["Hc"][k+1]), k+1, q) for k in range(3)]
    Avalue = smul(numerator_diag, invhc)
    Apartial = [r.sub(x, y, q) for x, y in zip(
        smul(numerator_derivative, invhc),
        smul(smul(numerator_diag, hp), spow(invhc, 2)))]
    qprime = mmconv([a.scale(red(J["W"][k+1]), k+1, q) for k in range(3)], qjets)
    qsecond = mmconv([a.scale(red(J["W"][k+2]), (k+2)*(k+1), q) for k in range(3)], qjets)
    assert all(r.equal(x, y) for x, y in zip(Avalue, qprime)), "Moving residue +1"
    regular_z = smul([r.sub(x, a.scale(y, pow(2, -1, q), q), q)
                     for x, y in zip(Apartial, qsecond)], sinv(qprime))

    # The true j map uses the coarse-safe homogeneous invariants Av and Bv^3.
    derivative = standard("p41_cleared_serre_derivative47_complete.json.gz")
    v = r.from_json(derivative["chosen_clearing_section"])
    G = r.from_json(derivative["cleared_derivative_coefficients"])
    inv = ClassicalInvariants(SimpleNamespace(a=a, r=r, v=v, G=G))
    iv = inv.series(J["W"])
    S5 = Series(a, 5)
    avv = S5.mul(S5.power(iv["Av"], 3), S5.power(iv["v"], 3))
    denom = S5.add(S5.scale(avv, 4), S5.scale(S5.power(iv["Bv3"], 2), 27))
    jfull = S5.scale(S5.mul(avv, S5.inverse(denom)), 6912)
    assert not np.any(jfull[0][1])
    assert int(jfull[0][0][0, 0]) == center["actual_j_at_ordinary_center_mod47four"]
    j = [red(x) for x in jfull]
    jp = [a.scale(j[k+1], k+1, q) for k in range(3)]
    jpp = [a.scale(j[k+2], (k+2)*(k+1), q) for k in range(3)]
    assert np.all(r.units(jp[0]))
    ratio_jpp = smul(jpp, sinv(jp))
    self_j = [r.sub(a.scale(x, 8, q), a.scale(y, 4, q), q)
              for x, y in zip(regular_z, ratio_jpp)]
    pieces = {"54_T2_eta_C": [a.scale(x, 54, q) for x in t2diag],
              "8_self_regular_j": self_j}
    for name, weight in [("u_minus_b", 162), ("c7_minus_b", -54),
                         ("Z8_minus20b", -27), ("D_minus20b", 64*pow(3, -1, q))]:
        f = center["actual_connections"][name]
        ss = r.from_json(f["numerator_quadratic_coefficients_mod47cubed"], q)
        qq = r.from_json(f["denominator_linear_coefficients_mod47four"], q)
        sv = [r.mm(red(x), ss, q) for x in J["V2"][:3]]
        qv = [r.mm(red(x), qq, q) for x in J["W"][:3]]
        assert np.all(r.units(qv[0])), name
        pieces[name] = [a.scale(x, weight, q) for x in smul(smul(sv, sinv(qv)), invhc)]
    oldeta = standard("p41_eta_calibration47_complete.json.gz")
    sB = r.from_json(oldeta["numerator_coefficients"], q)
    qB = r.from_json(oldeta["denominator_coefficients"], q)
    sv = [r.mm(red(x), sB, q) for x in J["V3"][:3]]
    qv = [r.mm(red(x), qB, q) for x in J["V2"][:3]]
    pieces["minus2_eta_B"] = [a.scale(x, -2, q) for x in smul(smul(sv, sinv(qv)), invhc)]
    pieces["eight_thirds_dlog_j"] = [a.scale(x, 8*pow(3, -1, q), q) for x in smul(jp, sinv(j[:3]))]
    jm = list(j[:3])
    jm[0] = r.sub(jm[0], scalar(1728), q)
    pieces["two_dlog_j_minus1728"] = [a.scale(x, 2, q) for x in smul(jp, sinv(jm))]
    differential = [r.zeros(1, 1) for _ in range(3)]
    for terms in pieces.values():
        for k in range(3):
            differential[k] = r.add(differential[k], terms[k], q)
    assert all(not np.any(x[1]) for x in differential)
    polynomial = [int(center["actual_local_sigma_F2_height_mod47four"])]
    polynomial += [int(x[0][0, 0])*47**(k+1)*pow(k+1, -1, Q) % Q for k, x in enumerate(differential)]
    # Rebuild the global F2 term from the published actual Abel center and
    # the very same projective chart, without importing a running checkpoint.
    abel = standard("ORD_j05_Abel47.json.gz")
    mult = standard("ORD_j05_multiply47.json.gz")
    holo = standard("p41_all129_tiny_Abel47_complete.json.gz")
    global_forms = standard("p41_global_qc_polynomials47_complete.json.gz")
    assert abel["complete_actual_center_Abel_constant"]
    assert abel["input_sha256"]["ORD_j05_multiply47.json.gz"] == sha(args.script_dir/"data/ORD_j05_multiply47.json.gz")
    assert abel["input_sha256"]["p41_all129_tiny_Abel47_complete.json.gz"] == sha(args.script_dir/"data/p41_all129_tiny_Abel47_complete.json.gz")
    assert holo["input_sha256"]["p41_ordinary_rational_atlas47.json.gz"] == sha(args.script_dir/"data/p41_ordinary_rational_atlas47.json.gz")
    assert mult["bits_done"] == mult["target_bits"] == 304
    assert mult["point_sha256"] == abel["actual_multiple_point_sha256"]
    hc = next(x for x in holo["charts"] if "ORD_j05" in x["disk_ids"])
    hi = hc["disk_ids"].index("ORD_j05")
    assert hc["origin"] == "R231_ordinary" and hc["origin_chart_0based"] == ch["chart_0based"]
    assert hc["disk_ids"] == ch["disk_ids"]
    for k in range(3):
        true_holo = r.rows(r.from_json(hc["canonical_differential_coefficients_0to2_mod47four"][k]), [hi])
        same_tiny = a.scale(true_holo, 47**(k+1)*pow(k+1, -1, Q))
        assert r.equal(same_tiny, r.rows(r.from_json(tchart["holomorphic_tiny_coefficients_1to3_in_y_mod47four"][k]), [trow]))
    aa = [abel["actual_center_C_cyclic_coordinates_mod47cubed"]]
    aa += [v[hi] for v in hc["cyclic_coordinate_tiny_coefficients_1to3_in_y_mod47cubed"]]
    F2 = next(f for f in global_forms["directions"] if f["n"] == 2)
    assert F2["F_Tn_coefficient"] == 27 and F2["F_identity_coefficient"] == 4
    based = F2["based_C"]
    assert all(x % 47 == 0 for x in based["linear_vector_mod47four"])
    global_coeff = [0]*7
    for k in range(4):
        global_coeff[k] += sum(x*y for x, y in zip(based["linear_vector_mod47four"], aa[k]))
    global_coeff[0] += based["constant_mod47four"]
    offset = 0
    for block in based["quadratic_blocks_mod47four"]:
        d = len(block)
        assert all(x % 47 == 0 for rowblock in block for x in rowblock)
        for k in range(4):
            for ellidx in range(4):
                global_coeff[k+ellidx] += sum(aa[k][offset+i]*block[i][j]*aa[ellidx][offset+j]
                                             for i in range(d) for j in range(d))
        offset += d
    assert offset == 54
    global_coeff = [x % Q for x in global_coeff]
    assert global_coeff[5:] == [0, 0]
    global_coeff = global_coeff[:5]
    assert global_coeff == [1409295, 1621124, 4618267, 3200841, 2180283]
    assert global_forms["component_order"] == [0, 3, 28, 32]
    indexF2 = global_forms["direction_indices"].index(2)
    targets = [v["QC_defect_target_mod47four"][indexF2] for v in global_forms["component_vectors"]]
    assert targets == [0, 0, 0, 0]
    qc = [(global_coeff[k] - 800*(polynomial[k] if k < 4 else 0)) % Q for k in range(5)]
    assert all(x % 47 == 0 for x in qc)
    reduction = [(x//47) % 47 for x in qc]
    assert reduction == [20, 44, 31, 0, 0]
    values = [sum(c*pow(y,k,47) for k,c in enumerate(reduction)) % 47 for y in range(47)]
    roots = [i for i,vv in enumerate(values) if vv == 0]
    discriminant = (reduction[1]**2 - 4*reduction[0]*reduction[2]) % 47
    assert discriminant == 20 and pow(discriminant, 23, 47) == 46 and roots == []
    out = {
        "result": "R262", "level": 41, "auxiliary_prime": 47,
        "precision": 4, "modulus": Q, "disk_id": "ORD_j05",
        "parameter": "The exact R231 projective coordinate z=Wc-W(P0)c; y=z/47.",
        "complete_actual_local_sigma_F2_polynomial_on_disk": True,
        "complete_all53_local_QC_heights": False, "complete_common_roots": False,
        "canonical_local_sigma_F2_height_coefficients_0to3_in_y_mod47four": polynomial,
        "local_differential_coefficients_0to2_in_z_mod47cubed": [r.to_json(x) for x in differential],
        "differential_pieces_coefficients_mod47cubed": {k: [r.to_json(x) for x in v] for k, v in pieces.items()},
        "actual_moving_connection": moving_cert,
        "actual_T2_parameter_coefficients_in_V4_mod47cubed": [r.to_json(x) for x in tcoeff],
        "V4_selected_W_V3_product_pairs_0based": pairs,
        "actual_T2_common_good_rows": tgood, "actual_T2_branch_good_counts": target_counts,
        "actual_T2_unit_interpolation_rows": selected4,
        "actual_T2_all_three_coefficient_equations": True,
        "actual_T2_center_crosscheck_with_R259": True,
        "actual_j_coefficients_0to4_mod47four": [r.to_json(x) for x in jfull],
        "actual_self_regular_z_coefficients_mod47cubed": [r.to_json(x) for x in regular_z],
        "actual_diagonal_residue_equations": True,
        "same_published_R231_chart_and_all54_holomorphic_tiny_coordinates": True,
        "actual_cyclic_C_coefficients_0to3_in_y_mod47cubed": aa,
        "global_F2_coefficients_0to4_in_y_mod47four": global_coeff,
        "actual_QC_F2_coefficients_0to4_in_y_mod47four": qc,
        "bad_component_labels": global_forms["component_order"],
        "F2_bad_targets_in_same_component_order": targets,
        "QC_divided_by47_reduction_coefficients_mod47": reduction,
        "all47_residual_QC_values": values,
        "residual_QC_roots": roots,
        "residual_quadratic_discriminant": discriminant,
        "residual_discriminant_Euler_symbol": 46,
        "entire_ORD_j05_disk_excluded_for_all_four_bad_components": True,
        "all129_disks_completed": False,
        "tail_bound": "The moving RR inverse and algebraic denominators have integral series. Its only nonintegral input is one primitive of regular nu; the height coefficient of z^n has valuation >=-floor(log_47(n))-v47(n). For n>=4, n-floor(log_47(n))-v47(n)>=4. The global term has divisible-by47 linear and quadratic coefficients; discarded Abel terms and degrees>=5 vanish mod47^4.",
        "source_sha256": sha(__file__), "input_sha256": dict(a.inputs, **inputs),
        "runtime_seconds": round(time.monotonic()-started, 3),
    }
    digest = save(args.output, out)
    print("PASS actual canonical F2 disk polynomial", polynomial, "SHA", digest, flush=True)
    print("PASS whole ORD_j05 disk excluded for all4 bad components; QC/47 mod47", reduction[:3],
          "discriminant", discriminant, "nonsquare", flush=True)


if __name__ == "__main__":
    main()
