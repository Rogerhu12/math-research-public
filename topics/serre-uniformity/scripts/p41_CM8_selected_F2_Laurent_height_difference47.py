#!/usr/bin/env python3
"""Actual CM(-8) F2 differential: combine the unique horizontal pole with Z_minus8 before evaluation.
No global CM reciprocity anchor or height constant is assigned by this program.
"""
import argparse
import gzip
import hashlib
import json
from pathlib import Path
import random
import sys
import time
from math import comb


def read(p):
    b=Path(p).read_bytes()
    return json.loads(gzip.decompress(b) if str(p).endswith('.gz') else b)


def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()


def main():
    ap=argparse.ArgumentParser(description=__doc__)
    for name in ['script-dir','branches','reference-connections','work-dir','output']:
        ap.add_argument('--'+name,type=Path,required=True)
    args=ap.parse_args();args.script_dir=args.script_dir.resolve();args.work_dir.mkdir(parents=True,exist_ok=True)
    sys.path.insert(0,str(args.script_dir))
    import numpy as np
    import p41_r2_matrix as r
    from p41_actual_differentials47 import ActualModel,save
    from p41_native_r2_linear47 import install
    from p41_projective_jet_frames47 import install_exact_float_mm
    from p41_elliptic_coarse_atlas47 import Series
    install_exact_float_mm(r);install(r,args.work_dir/'native')
    a=ActualModel(args.script_dir);Q,q,M,N=r.Q,47**3,a.M,4
    started=time.monotonic();inputs={}
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

    branches=load(args.branches);reference=load(args.reference_connections);args.disk_id=branches['disk_id']
    assert branches['exactly_one_true_full_level_horizontal_branch'] and branches['horizontal_derivative_in_j_is_minus_one']
    assert branches['all4x73_T2_pullback_trace_coefficients_verified']
    assert branches['all4x54_canonical_T2_pullback_trace_coefficients_verified']
    assert reference['complete_actual_C_and_fixed_F2_connections_at_true_CM8']
    assert reference['disk_id']==args.disk_id
    J={k:[r.from_json(x) for x in v] for k,v in branches['source_true_CM_projective_jets_0to4'].items()}
    assert len(J['W'])==5
    W0=J['W'][0]
    frame=r.from_json(branches['source_frame']);coordinate=r.from_json(branches['source_coordinate'])
    assert r.equal(frame,a.fc) and r.equal(r.mm(W0,frame),r.column([[1,0]]))
    connection=reference['actual_connections']['C_at_CM8']
    q0=r.from_json(connection['denominator_linear_coefficients_mod47four'])
    s0=r.from_json(connection['numerator_quadratic_coefficients_mod47cubed'],q)
    WZ=r.from_json(connection['finite_pole_coordinates_fc_normalized'])
    assert r.equal(W0,r.rows(WZ,[0]));b=r.rows(WZ,[1])
    V2b,V3b=a.evaluate(b);Hb=r.mm(V3b,a.H)
    original=standard('p41_second_kind_connection47.json.gz')
    assert reference['CM_nu_moving_pole_formula_and_old_cross_identities_verified']
    nu=[r.from_json(x) for x in reference['actual_CM_nu_coefficients_0to2_mod47four']]
    gc=[red(r.from_json(reference['actual_gradients_original_nu_mod47cubed']['C_at_CM8']))]
    gc += [a.scale(red(nu[k-1]),pow(k,-1,q),q) for k in range(1,4)]
    assert r.equal(gc[0],r.from_json(connection['calibration_gradient_original_nu_mod47cubed'],q))
    assert all(r.equal(r.conjugate(x,q),r.cols(x,original['pole_Frobenius_permutation_0based'])) for x in gc)
    rng=random.Random(4104726201)
    Kb=kernel(b,1)
    for attempt in range(100):
        xx=r.mm(Kb,r.column([[rng.randrange(47),rng.randrange(47)] for _ in range(72)]))
        ell=r.add(xx,r.mm(M['A1'],r.conjugate(xx)))
        if np.all(r.units(r.mm(W0,ell))):break
    else:raise AssertionError('No actual moving denominator correction')
    assert r.iszero(r.mm(b,ell))
    Sfull=Series(a,5)
    def moving_section(g0):
        values=[r.mm(w,g0) for w in J['W']]
        ellvalues=[r.mm(w,ell) for w in J['W']]
        ratio=Sfull.mul(values,Sfull.inverse(ellvalues));assert r.iszero(ratio[0])
        out=[r.sub(g0,r.mul(ell,ratio[0]))]
        out += [r.neg(r.mul(ell,ratio[k])) for k in range(1,5)]
        for n in range(5):
            val=r.zeros(1,1)
            for k in range(n+1):val=r.add(val,r.mm(J['W'][k],out[n-k]))
            assert r.iszero(val) and r.iszero(r.mm(b,out[n]))
            assert r.equal(r.mm(M['A1'],r.conjugate(out[n])),out[n])
        return out
    qjets_full = moving_section(q0)
    qjets = [red(x) for x in qjets_full[:N]]
    qsource = [r.mm(red(M["W"]), x, q) for x in qjets]
    good = np.flatnonzero(r.units(qsource[0])[:, 0]).tolist()
    assert len(good) > 378
    E = red(r.rows(M["V2"], good))
    er, ec = r.rank_pivots(E)
    assert len(er) == 199 and ec == list(range(199))
    Ei = r.inverse_matrix(r.rows(E, er), q)
    iq = sinv([r.rows(x, good) for x in qsource])
    Kpb = kernel(WZ, 2)
    colon = [[] for _ in range(N)]
    colon_tests = []
    for attempt in range(6):
        xx = r.mm(Kpb, r.column([[rng.randrange(47), rng.randrange(47)] for _ in range(71)]))
        gg = r.add(xx, r.mm(M["A1"], r.conjugate(xx)))
        gjets = moving_section(gg)[:N]
        gsource = [r.mm(red(r.rows(M["W"], good)), red(x), q) for x in gjets]
        ratios = smul(gsource, iq)
        for k in range(N):
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
    HP = [red(r.mm(x, a.H)) for x in J["V3"][:N]]
    resP = mmconv(HP, qjets)
    a.field_setup()
    cusp_blocks = []
    for index in [0, 11]:
        CV2, _ = a.cusp_evaluations(index)
        cusp_blocks.append(a.scale(red(CV2), 41, q))
    A, B = [], []
    for k in range(N):
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
    for n in range(N):
        wanted = B[n]
        for k in range(1, n+1):
            wanted = r.sub(wanted, r.mm(A[k], sjets[n-k], q), q)
        sn = r.mm(Ai, r.rows(wanted, ar), q)
        assert r.equal(r.mm(A[0], sn, q), wanted), ("moving all equations", n)
        assert r.equal(r.mm(red(M["A2"]), r.conjugate(sn, q), q), sn)
        sjets.append(sn)
    assert r.equal(sjets[0], s0)
    moving_cert = {
        "q_linear_coefficients_in_parameter_0to4_mod47four": [r.to_json(x) for x in qjets_full],
        "s_quadratic_coefficients_in_parameter_0to3_mod47cubed": [r.to_json(x) for x in sjets],
        "gradient_original_nu_coefficients_0to3_mod47cubed": [r.to_json(x) for x in gc],
        "colon_test_sections_0to3_mod47four": colon_tests,
        "good_source_rows": good, "full_equation_rows": A[0][0].shape[0],
        "unit_minor_rows": ar, "all_four_coefficient_equations": True,
        "center_matches_actual_CM8_C_connection": True, "Frobenius": True,
    }
    save(args.work_dir / "actual_C_moving_connection47.json.gz", moving_cert)
    print("PASS actual moving C connection all", N*A[0][0].shape[0], "rows", flush=True)

    # Exact x=0 is the true CM point.  Divide each horizontal denominator
    # by x symbolically, retaining its Laurent residue before any cancellation.
    branch_values=[];horizontal_residue=r.zeros(1,1)
    qfull=[red(x) for x in qjets_full]
    for record in branches['branch_records']:
        Wt=[red(r.from_json(x)) for x in record['actual_image_W_coefficients_0to4']]
        V2t=[red(r.from_json(x)) for x in record['actual_image_V2_coefficients_0to4']]
        factor=[red(r.from_json(x)) for x in record['actual_differential_pullback_coefficients_0to3']]
        sv=mmconv(V2t[:4],sjets,4)
        numerator=smul(sv,factor,4)
        denominator=mmconv(Wt,qfull,5)
        horizontal=record['horizontal_fixed_point']
        if horizontal:
            assert r.iszero(denominator[0]) and np.all(r.units(denominator[1]))
            values=smul(numerator,sinv(denominator[1:5],4),4)
            assert r.equal(Wt[0],red(W0)) and r.equal(r.from_json(record['target_frame']),frame)
            hp=r.mm(Wt[1],red(coordinate),q)
            assert r.equal(hp,scalar(-1))
            expected=r.mul(hp,r.inverse_values(r.sub(hp,scalar(1),q),q),q)
            assert r.equal(values[0],expected)
            horizontal_residue=r.add(horizontal_residue,values[0],q)
            exponents=[-1,0,1,2]
        else:
            assert np.all(r.units(denominator[0]))
            values=smul(numerator,sinv(denominator,4),4)
            exponents=[0,1,2,3]
        branch_values.append({'branch_0based':record['branch_0based'],'horizontal':horizontal,
            'numerator_coefficients_0to3_mod47cubed':[r.to_json(x) for x in numerator],
            'denominator_coefficients_0to4_mod47cubed':[r.to_json(x) for x in denominator],
            'exponents':exponents,'coefficients_mod47cubed':[r.to_json(x) for x in values],
            'exact_zero_then_unit_linear_coefficient':horizontal})
    fixedz=reference['actual_connections']['Z8_minus20b']
    zss=r.from_json(fixedz['numerator_quadratic_coefficients_mod47cubed'],q)
    zqq=r.from_json(fixedz['denominator_linear_coefficients_mod47four'],q)
    z8sv=[r.mm(red(x),zss,q) for x in J['V2'][:4]]
    z8numerator=smul(z8sv,[red(x) for x in J['inverse_Hc'][:4]],4)
    z8denominator=[r.mm(red(x),zqq,q) for x in J['W']]
    assert r.iszero(z8denominator[0]) and np.all(r.units(z8denominator[1]))
    z8laurent=smul(z8numerator,sinv(z8denominator[1:5],4),4)
    assert r.equal(z8laurent[0],scalar(1)) and r.equal(horizontal_residue,scalar(pow(2,-1,q)))
    weighted_residue=r.sub(a.scale(horizontal_residue,54,q),a.scale(z8laurent[0],27,q),q)
    assert r.iszero(weighted_residue)
    combined=[]
    for k in range(3):
        value=r.neg(a.scale(z8laurent[k+1],27,q),q)
        for record in branch_values:
            value=r.add(value,a.scale(r.from_json(record['coefficients_mod47cubed'][k+int(record['horizontal'])],q),54,q),q)
        combined.append(value)
    print('PASS actual CM8 Laurent residues +27 and -27 cancel before evaluation',flush=True)
    def mul3(x,y):return smul(x,y,3)
    def inv3(x):return sinv(x,3)
    def pow3(x,n):return spow(x,n,3)
    def conv3(x,y):return mmconv(x,y,3)
    invhc=[red(x) for x in J['inverse_Hc'][:3]]
    numerator_diag=conv3([red(x) for x in J['V2'][:3]],sjets[:3])
    numerator_derivative=conv3([a.scale(red(J['V2'][k+1]),k+1,q) for k in range(3)],sjets[:3])
    hp=[a.scale(red(J['Hc'][k+1]),k+1,q) for k in range(3)]
    Avalue=mul3(numerator_diag,invhc)
    Apartial=[r.sub(x,y,q) for x,y in zip(mul3(numerator_derivative,invhc),mul3(mul3(numerator_diag,hp),pow3(invhc,2)))]
    qprime=conv3([a.scale(red(J['W'][k+1]),k+1,q) for k in range(3)],qjets[:3])
    qsecond=conv3([a.scale(red(J['W'][k+2]),(k+2)*(k+1),q) for k in range(3)],qjets[:3])
    assert all(r.equal(x,y) for x,y in zip(Avalue,qprime))
    regular=mul3([r.sub(x,a.scale(y,pow(2,-1,q),q),q) for x,y in zip(Apartial,qsecond)],inv3(qprime))
    jfull=[r.from_json(x) for x in branches['source_true_CM_j_coefficients_0to4']]
    j=[red(x) for x in jfull]
    jp=[a.scale(j[k+1],k+1,q) for k in range(3)]
    jpp=[a.scale(j[k+2],(k+2)*(k+1),q) for k in range(3)]
    assert np.all(r.units(jp[0]))
    fixed_fraction_replacements={}
    def fixed_fraction(name):
        f = reference["actual_connections"][name]
        ss = r.from_json(f["numerator_quadratic_coefficients_mod47cubed"], q)
        qq = r.from_json(f["denominator_linear_coefficients_mod47four"])
        if np.all(r.units(r.mm(W0, qq))):
            return ss, red(qq)
        # The pole support is still the exact original divisor.  Only the
        # global auxiliary expression changes; no nonunit is numerically divided.
        WZ = r.from_json(f["finite_pole_coordinates_fc_normalized"])
        nn = WZ[0].shape[0]
        assert len(r.rank_pivots(cat(WZ, W0))[0]) == nn + 1, (name, "a true pole needs geometric cancellation")
        KK = kernel(WZ, nn)
        rrng = random.Random(4104733601 + sum((i+1)*ord(c) for i,c in enumerate(args.disk_id+name)))
        for attempt in range(200):
            seed = r.column([[rrng.randrange(47), rrng.randrange(47)] for _ in range(73-nn)])
            xx = r.mm(KK, seed)
            qnew = r.add(xx, r.mm(M["A1"], r.conjugate(xx)))
            assert r.iszero(r.mm(WZ, qnew))
            if np.all(r.units(r.mm(W0, qnew))):
                break
        else:
            raise AssertionError((name, "no new unit auxiliary denominator"))
        oldq = r.mm(red(M["W"]), red(qq), q)
        newq = r.mm(red(M["W"]), red(qnew), q)
        oldn = r.mm(red(M["V2"]), ss, q)
        good = np.flatnonzero(r.units(oldq)[:, 0]).tolist()
        assert len(good) > 378
        EE = red(r.rows(M["V2"], good))
        er, ec = r.rank_pivots(EE)
        assert len(er) == 199 and ec == list(range(199))
        values = r.mul(r.mul(r.rows(oldn, good), r.rows(newq, good), q),
                       r.inverse_values(r.rows(oldq, good), q), q)
        snew = r.mm(r.inverse_matrix(r.rows(EE, er), q), r.rows(values, er), q)
        assert r.equal(r.mm(EE, snew, q), values)
        newn = r.mm(red(M["V2"]), snew, q)
        assert r.equal(r.mul(newn, oldq, q), r.mul(oldn, newq, q))
        assert r.equal(r.mm(red(M["A2"]), r.conjugate(snew, q), q), snew)
        assert r.equal(r.mm(M["A1"], r.conjugate(qnew)), qnew)
        fixed_fraction_replacements[name] = {
            "original_numerator_quadratic_mod47cubed": r.to_json(ss),
            "original_denominator_linear_mod47four": r.to_json(qq),
            "new_numerator_quadratic_mod47cubed": r.to_json(snew),
            "new_denominator_linear_mod47four": r.to_json(qnew),
            "actual_unchanged_pole_support": r.to_json(WZ),
            "source_center_separate_from_all_true_poles_by_unit_minor": True,
            "attempt_0based": attempt, "old_expression_unit_source_rows": good,
            "unit_V2_interpolation_rows": er,
            "all820_cross_multiplication_identities_mod47cubed": True,
            "degree_bound_3L": 378, "new_denominator_unit_at_source_center": True,
            "Frobenius_both_actual_sections": True,
            "division_by_nonunit_or47_used": False,
        }
        print("PASS actual global removable fixed fraction", name, "good", len(good),
              "all820 degree378 cross identities", flush=True)
        return snew, red(qnew)

    pieces={'54_T2_eta_C_minus27_eta_Z8':combined,
        '8_self_regular_j':[r.sub(a.scale(x,8,q),a.scale(y,4,q),q) for x,y in zip(regular,mul3(jpp,inv3(jp)))]}
    for name,weight in [('u_minus_b',162),('c7_minus_b',-54),('D_minus20b',64*pow(3,-1,q))]:
        ss,qq=fixed_fraction(name)
        sv=[r.mm(red(x),ss,q) for x in J['V2'][:3]]
        qv=[r.mm(red(x),qq,q) for x in J['W'][:3]]
        assert np.all(r.units(qv[0])),('fixed auxiliary denominator at CM8',name)
        pieces[name]=[a.scale(x,weight,q) for x in mul3(mul3(sv,inv3(qv)),invhc)]
    oldeta = standard("p41_eta_calibration47_complete.json.gz")
    sB = r.from_json(oldeta["numerator_coefficients"], q)
    qB = r.from_json(oldeta["denominator_coefficients"], q)
    eta_B_fraction_replacement = None
    if not np.all(r.units(r.mm(red(J["V2"][0]), qB, q))):
        # eta_B has precisely Z_{-4} minus the cusp divisor as its poles.
        # The fc-unit source is not a cusp; preserve all20 actual CM roots.
        WZB = r.from_json(a.cm4['coarse_point_values'])
        WZB = r.mul(WZB, r.inverse_values(r.mm(WZB, a.fc)))
        V2ZB, _ = a.evaluate(WZB)
        assert len(r.rank_pivots(cat(V2ZB, J['V2'][0]))[0]) == 21
        assert r.equal(r.mm(W0, a.fc), r.column([[1,0]]))
        KB = kernel(V2ZB, 20)
        rngB = random.Random(4104733508 + sum((i+1)*ord(c) for i,c in enumerate(args.disk_id)))
        for attemptB in range(200):
            xx = r.mm(KB, r.column([[rngB.randrange(47),rngB.randrange(47)] for _ in range(179)]))
            qBnew = r.add(xx, r.mm(M['A2'], r.conjugate(xx)))
            assert r.iszero(r.mm(V2ZB, qBnew))
            if np.all(r.units(r.mm(J['V2'][0], qBnew))):
                break
        else:
            raise AssertionError('No actual eta_B unit denominator')
        oq = r.mm(red(M['V2']), qB, q)
        nq = r.mm(red(M['V2']), red(qBnew), q)
        os = r.mm(red(M['V3']), sB, q)
        goodB = np.flatnonzero(r.units(oq)[:,0]).tolist()
        assert len(goodB) > 630
        E = red(r.rows(M['V3'], goodB))
        erB, ecB = r.rank_pivots(E)
        assert len(erB)==325 and ecB==list(range(325))
        valuesB = r.mul(r.mul(r.rows(os,goodB),r.rows(nq,goodB),q),r.inverse_values(r.rows(oq,goodB),q),q)
        sBnew = r.mm(r.inverse_matrix(r.rows(E,erB),q),r.rows(valuesB,erB),q)
        assert r.equal(r.mm(E,sBnew,q),valuesB)
        ns = r.mm(red(M['V3']),sBnew,q)
        assert r.equal(r.mul(ns,oq,q),r.mul(os,nq,q))
        assert r.equal(r.mm(red(M['A3']),r.conjugate(sBnew,q),q),sBnew)
        assert r.equal(r.mm(M['A2'],r.conjugate(qBnew)),qBnew)
        eta_B_fraction_replacement = {
            'original_numerator_cubic_mod47cubed':r.to_json(sB),
            'original_denominator_quadratic_mod47cubed':r.to_json(qB),
            'new_numerator_cubic_mod47cubed':r.to_json(sBnew),
            'new_denominator_quadratic_mod47four':r.to_json(qBnew),
            'actual20_CM4_pole_coordinates_fc_normalized':r.to_json(WZB),
            'true_cusp_support_excluded_by_fc_unit':True,
            'CM4_V2_plus_source_rank_mod47':21,
            'old_expression_unit_source_rows':goodB,'unit_V3_interpolation_rows':erB,
            'attempt_0based':attemptB,'all820_degree5L_cross_identities_mod47cubed':True,
            'degree_bound_5L':630,'Frobenius_both_actual_sections':True,
            'new_denominator_unit_at_source':True,'division_by_nonunit_or47_used':False}
        sB,qB=sBnew,red(qBnew)
        print('PASS actual global removable eta_B fraction',len(goodB),'good rows; all820 degree630 cross identities',flush=True)
    sv = [r.mm(red(x), sB, q) for x in J["V3"][:3]]
    qv = [r.mm(red(x), qB, q) for x in J["V2"][:3]]
    pieces["minus2_eta_B"] = [a.scale(x, -2, q) for x in mul3(mul3(sv, inv3(qv)), invhc)]
    pieces['eight_thirds_dlog_j']=[a.scale(x,8*pow(3,-1,q),q) for x in mul3(jp,inv3(j[:3]))]
    jm=list(j[:3]);jm[0]=r.sub(jm[0],scalar(1728),q)
    pieces['two_dlog_j_minus1728']=[a.scale(x,2,q) for x in mul3(jp,inv3(jm))]
    differential=[r.zeros(1,1) for _ in range(3)]
    for v in pieces.values():differential=[r.add(x,y,q) for x,y in zip(differential,v)]
    assert all(not np.any(x[1]) for x in differential)
    ycm=branches['source_original_y_mod47cubed']
    assert ycm==reference['source_CM_original_y_mod47cubed']
    heightw=[0]+[int(x[0][0,0])*47**(k+1)*pow(k+1,-1,Q)%Q for k,x in enumerate(differential)]
    translated=[sum(comb(n,k)*heightw[n]*pow(-ycm,n-k,Q) for n in range(k,4))%Q for k in range(4)]
    height_difference=[0]+translated[1:]
    # Subtract the value at the original atlas center.  This is a difference,
    # not a height anchor for a possibly nonrational global CM8 point.
    assert sum(c*pow(0,k,Q) for k,c in enumerate(height_difference))%Q==0
    out={'result':branches['result'],'level':41,'auxiliary_prime':47,'precision':4,'modulus':Q,'disk_id':args.disk_id,
        'complete_actual_local_sigma_F2_differential_and_height_difference':True,
        'complete_actual_local_sigma_F2_polynomial_on_disk':False,
        'actual_height_constant_computed':False,'CM_global_reciprocity_anchor_used':False,
        'parameter':'x=z_original-z_CM8 and w=x/47=y_original-yCM; the original atlas origin has y=0',
        'source_CM_original_y_mod47cubed':ycm,
        'actual_F2_height_difference_from_CM_coefficients_0to3_in_w_mod47four':heightw,
        'actual_F2_height_difference_from_original_center_coefficients_0to3_in_y_mod47four':height_difference,
        'local_differential_coefficients_0to2_in_x_mod47cubed':[r.to_json(x) for x in differential],
        'differential_pieces_coefficients_mod47cubed':{k:[r.to_json(x) for x in v] for k,v in pieces.items()},
        'actual_CM_center_nu_coefficients_0to2_mod47four':[r.to_json(x) for x in nu],
        'actual_moving_connection':moving_cert,
        'actual_branch_Laurent_data':branch_values,
        'actual_fixed_eta_Z8_Laurent_coefficients_minus1_to2_mod47cubed':[r.to_json(x) for x in z8laurent],
        'actual_fixed_eta_Z8_numerator_coefficients_0to3_mod47cubed':[r.to_json(x) for x in z8numerator],
        'actual_fixed_eta_Z8_denominator_coefficients_0to4_mod47cubed':[r.to_json(x) for x in z8denominator],
        'horizontal_residue_one_half_and_weighted_residue_plus27':True,
        'fixed_CM8_weighted_residue_minus27':True,
        'all_poles_cancel_before_evaluation':True,
        'all_divisions_by_horizontal_parameter_are_exact_x_coefficient_shifts':True,
        'no_independent_47_factor_discarded':True,
        'actual_self_regular_x_coefficients_mod47cubed':[r.to_json(x) for x in regular],
        'fixed_fraction_replacements':fixed_fraction_replacements,
        'eta_B_fraction_replacement':eta_B_fraction_replacement,
        'complete_all53_local_QC_heights':False,'complete_common_roots':False,
        'tail_bound':'After exact x division the horizontal regular term needs the C family through order n for height coefficient x^n. The unique nonintegral input remains one primitive of integral nu; valuation>=-floor(log_47(n))-v47(n). Thus n>=4 terms vanish after x=47w modulo47^4. Translation w=y-yCM is exact and integral; the omitted additive height constant must come from the actual principal Norm.',
        'input_sha256':dict(a.inputs,**inputs),'source_sha256':sha(__file__),'runtime_seconds':round(time.monotonic()-started,3)}
    digest=save(args.output,out)
    print('PASS CM8 actual jointly cancelled Laurent F2 differential, original-y height difference',height_difference,'SHA',digest,flush=True)


if __name__=='__main__':main()
