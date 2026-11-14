#!/usr/bin/env python3
"""Actual T2/T3 differential traces and tiny integrals in the published frames.

Only the saved actual Hecke matrices are used.  No normalization is inferred
from the desired integrals.  A fresh Frobenius-rational denominator is selected;
the resulting rational differential is checked at every good source row.
"""
import argparse
import gzip
import hashlib
import json
from pathlib import Path
import random
import time

from p41_actual_differentials47 import ActualModel, P, Q, Q3, digest, report, save


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--script-dir', type=Path, default=Path(__file__).resolve().parent)
    ap.add_argument('--eta', type=Path, required=True)
    ap.add_argument('--output', type=Path, required=True)
    args = ap.parse_args()
    started = time.monotonic()
    raw = args.eta.read_bytes()
    eta = json.loads(gzip.decompress(raw) if args.eta.name.endswith('.gz') else raw)
    a = ActualModel(args.script_dir)
    r, np, M = a.r, a.np, a.M
    s = r.from_json(eta['numerator_coefficients'], Q3)
    q = r.from_json(eta['denominator_coefficients'], Q3)
    assert digest(r.to_json(s)) == 'f1be6a6ae4e9cee06e0439d49c02234926099ba7825ee0cbacabe93d072a3e87'
    assert digest(r.to_json(q)) == '26c3d25651a22b75eb3b337c4a35980102ec7529077f5598a1e4a53d767dc5ae'
    compact = a.read('p41_hecke47_compact.json.gz')
    hecke = a.read('p41_hecke47_full_saved.json.gz')
    assert a.inputs['p41_hecke47_full_saved.json.gz'] == compact['full_raw_sha256']
    frame = a.read('p41_hecke3_formal_height47_compact.json.gz')
    log = a.read('p41_formal47_log_compact.json.gz')
    cm16 = a.read('p41_cm16_hecke47_verified.json.gz')
    cm36 = a.read('p41_cm36_hecke47_raw.json.gz')
    cm_values = {
        2: a.cm4['coarse_point_values']+cm16['weight2_values'],
        3: [row for rec in cm36['records'] for row in rec['weight2_values']],
    }
    gradients = {}
    traces = {}
    forms = {1: (s, q)}
    rng = random.Random(194197)
    I0 = [i-1 for i in frame['families'][0]['points_1based']]
    I1 = [i-1 for i in frame['families'][1]['points_1based']]
    gA = r.from_json(eta['Lie_gradient_mod47_cubed'], Q3)
    for ell in (2, 3):
        op = hecke['operators'][str(ell)]
        permutation = [j-1 for j in op['necklace_transport_1based']]
        assert sorted(permutation) == list(range(820))
        total = r.zeros(820, 1)
        good = np.ones(820, dtype=bool)
        counts = []
        for branch, target in enumerate(op['targets']):
            W = r.from_json(target['evaluation_matrix'])
            V2, V3 = a.evaluate(W)
            qv = r.mm(a.reduce(V2, Q3), q, Q3)
            sv = r.mm(a.reduce(V3, Q3), s, Q3)
            unit = r.units(qv)[:, 0]
            counts.append(int(np.sum(unit)))
            values = r.zeros(820, 1)
            ii = np.flatnonzero(unit).tolist()
            for k in range(2):
                values[k][ii] = r.mul(r.rows(sv, ii), r.inverse_values(r.rows(qv, ii), Q3), Q3)[k]
            total = r.add(total, r.rows(values, permutation), Q3)
            good &= unit[permutation]
            del W, V2, V3, qv, sv, values
        total = a.scale(total, pow(ell, -1, Q3), Q3)
        G = np.flatnonzero(good).tolist()
        assert counts == ({2:[820,820,817],3:[817,817,819,790]}[ell])
        assert len(G) == ({2:817,3:786}[ell])
        WZ = r.from_json(cm_values[ell])
        WZ = r.mul(WZ, r.inverse_values(r.mm(WZ, a.fc)))
        V2Z, V3Z = a.evaluate(WZ)
        rr, cc = r.rank_pivots(V2Z)
        assert len(rr) == 40
        K, free, block = r.kernel_from_rows(r.rows(V2Z, rr), rr, cc)
        assert r.iszero(r.mm(V2Z, K)) and len(free) == 159
        HZ = r.mm(V3Z, a.H)
        dqraw = r.add(r.mul(r.cols(WZ, a.a2), r.cols(HZ, a.b2)), r.mul(r.cols(HZ, a.a2), r.cols(WZ, a.b2)))
        for attempt in range(100):
            seed = r.column([[rng.randrange(P), rng.randrange(P)] for _ in free])
            v = r.mm(K, seed)
            qt = r.add(v, r.mm(M['A2'], r.conjugate(v)))
            assert r.iszero(r.mm(V2Z, qt))
            qsource = r.mm(M['V2'], qt)
            dq = r.mm(dqraw, r.mm(a.C2, qt))
            if not np.all(r.units(r.rows(qsource, I0+I1))) or not np.all(r.units(dq)):
                continue
            break
        else:
            raise AssertionError('No unit denominator chart selected')
        qt = a.reduce(qt, Q3)
        values = r.mul(a.reduce(r.rows(qsource, G), Q3), r.rows(total, G), Q3)
        VG = a.reduce(r.rows(M['V3'], G), Q3)
        rr, cc = r.rank_pivots(VG)
        assert len(rr) == 325 and cc == list(range(325))
        st = r.mm(r.inverse_matrix(r.rows(VG, rr), Q3), r.rows(values, rr), Q3)
        assert r.equal(r.mm(VG, st, Q3), values)
        assert r.equal(r.mm(a.reduce(M['A3'], Q3), r.conjugate(st, Q3), Q3), st)
        assert r.equal(r.mm(a.reduce(M['A2'], Q3), r.conjugate(qt, Q3), Q3), qt)
        residues = r.mul(r.mm(a.reduce(V3Z, Q3), st, Q3), r.inverse_values(a.reduce(dq, Q3), Q3), Q3)
        wanted = ([1]*20+[2]*20) if ell == 2 else [2]*40
        assert r.equal(residues, r.column([[v,0] for v in wanted], Q3))
        for index in (0, 11):
            CV2, CV3 = a.cusp_evaluations(index)
            z = r.add(a.scale(r.mm(a.reduce(CV3, Q3), st, Q3), 41, Q3),
                      a.scale(r.mm(a.reduce(CV2, Q3), qt, Q3), ell+1, Q3), Q3)
            assert r.iszero(z)
        CV = a.reduce(r.mm(r.rows(M['W'], I1), a.K1), Q3)
        assert all(good[i] for i in I1)
        gt = r.mm(r.inverse_matrix(CV, Q3), r.rows(total, I1), Q3)
        MT = r.from_json(op['canonical_operator'], Q3)
        bt = r.sub(gt, r.mm(MT, gA, Q3), Q3)
        expected = {2:[[74324,50282],[79216,21972],[9765,2834]],
                    3:[[78958,60738],[21971,103425],[3828,103443]]}[ell]
        assert r.to_json(r.rows(bt, [0,1,2])) == [[x] for x in expected]
        assert np.all(r.units(bt))
        gradients[str(ell)] = {'actual':r.to_json(gt), 'transport_correction':r.to_json(bt)}
        forms[ell] = (st, qt)
        traces[str(ell)] = {'branch_good_rows':counts,'common_good_rows':len(G),
                           'interpolation_unit_minor_source_rows_1based':[G[i]+1 for i in rr],
                           'all_good_rows_checked':True,'CM_residues':wanted,'cusp_residue':-(ell+1),
                           'numerator_coefficients':r.to_json(st),'denominator_coefficients':r.to_json(qt),
                           'numerator_sha256':digest(r.to_json(st)),'denominator_sha256':digest(r.to_json(qt)),
                           'denominator_attempt':attempt,'Frobenius':True}
        report('Actual T'+str(ell)+' trace, all residues and nonzero frame correction verified')
    del hecke, compact, cm16, cm36, cm_values
    target = r.from_json(log['log_of_signed_multiple'])
    assert target[0].shape == (1,54)
    assert all(not np.any(x % P) for x in target)
    family_results = []
    for family, I in enumerate([I0,I1]):
        J = a.local_jets(r.rows(M['W'], I), order=3)
        omega = []
        for n in range(3):
            t = r.zeros(54,54)
            for k in range(n+1):
                t = r.add(t, r.mul(r.mm(J['W'][k], a.K1), J['inverse_Hc'][n-k]))
            omega.append(t)
        assert len(r.rank_pivots(omega[0])[0]) == 54
        z = r.mm(target, r.inverse_matrix(omega[0]))
        def evaluate_abel(z):
            total = r.zeros(1,54)
            jac = r.zeros(54,54)
            power = (np.ones((1,54),dtype=np.int64),np.zeros((1,54),dtype=np.int64))
            for n in range(3):
                jac = r.add(jac, r.mul((power[0].T,power[1].T),omega[n]))
                power = r.mul(power,z)
                total = r.add(total,a.scale(r.mm(power,omega[n]),pow(n+1,-1,Q)))
            return total,jac
        for _ in range(3):
            actual,jac = evaluate_abel(z)
            z = r.add(z,r.mm(r.sub(target,actual),r.inverse_matrix(jac)))
        assert r.equal(evaluate_abel(z)[0],target)
        assert all(not np.any(x % P) for x in z)
        positions = {point:k for k,point in enumerate(I)}
        tau = [positions[M['tau'][point]] for point in I]
        assert r.equal(r.cols(z,tau),r.conjugate(z))
        published = r.from_json(frame['families'][family]['actual_parameters'])
        t0 = r.rows(published,[0])
        scale = a.scale(r.mul(J['f0'],J['Hc'][0]),2880480)
        firstorder = r.mul((scale[0].T,scale[1].T),t0)
        assert r.equal(a.reduce(z,P**2),a.reduce(firstorder,P**2))
        tiny = {}
        coefficients = {}
        for ell in ((1,2,3) if family == 0 else (1,)):
            st,qt = forms[ell]
            sv=[r.mm(a.reduce(V,Q3),st,Q3) for V in J['V3'][:3]]
            qv=[r.mm(a.reduce(V,Q3),qt,Q3) for V in J['V2'][:3]]
            assert np.all(r.units(qv[0]))
            iq=[r.inverse_values(qv[0],Q3)]
            for n in (1,2):
                t=r.zeros(54,1)
                for k in range(1,n+1):t=r.add(t,r.mul(qv[k],iq[n-k],Q3),Q3)
                iq.append(r.neg(r.mul(t,iq[0],Q3),Q3))
            series=[]
            for n in range(3):
                t=r.zeros(54,1)
                for i in range(n+1):
                    for j in range(n-i+1):
                        term=r.mul(r.mul(sv[i],iq[j],Q3),a.reduce(J['inverse_Hc'][n-i-j],Q3),Q3)
                        t=r.add(t,term,Q3)
                series.append(t)
            total=r.zeros(1,1)
            zp=z
            for n in range(3):
                total=r.add(total,a.scale(r.mm(zp,series[n]),pow(n+1,-1,Q)))
                zp=r.mul(zp,z)
            assert total[1][0,0]==0
            tiny[str(ell)]=int(total[0][0,0])
            coefficients[str(ell)]=[r.to_json(c) for c in series]
        assert tiny==({'1':890368,'2':463561,'3':924161} if family==0 else {'1':1730352})
        family_results.append({'family':family,'points_1based':[i+1 for i in I],
                               'rational_coordinate_coefficients':r.to_json(J['coordinate']),
                               'actual_parameters':r.to_json(z),'target_logarithm':r.to_json(target),
                               'all_54_Abel_equations':True,'published_first_order_parameter_check':True,
                               'Frobenius':True,'integrand_coefficients_mod47_cubed':coefficients,
                               'tiny_integrals_mod47_fourth':tiny})
        report('Family '+str(family)+' tiny integrals '+json.dumps(tiny,sort_keys=True))
    out={'status':'complete actual traces and tiny integrals; all previous independent values recovered',
         'level':41,'auxiliary_prime':47,'precision':4,'modulus':Q,'trace_coefficient_precision':3,
         'eta_certificate_sha256':hashlib.sha256(raw).hexdigest(),'traces':traces,'frame_gradients':gradients,
         'families':family_results,'input_sha256':a.inputs,'global_derivation_sha256':a.H_sha,
         'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
         'engine_sha256':hashlib.sha256(Path(__file__).with_name('p41_actual_differentials47.py').read_bytes()).hexdigest(),
         'normalization':'Actual R131 1/ell traces, R145 same Abel frames, R123 KS scale; no Hecke-gradient shortcut'}
    h=save(args.output,out)
    report('Actual differential trace and tiny reconstruction complete; seconds='+str(round(time.monotonic()-started,3)))
    print(str(args.output)+' SHA256 '+h,flush=True)


if __name__=='__main__':
    main()
