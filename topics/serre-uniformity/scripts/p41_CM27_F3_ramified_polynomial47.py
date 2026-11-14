#!/usr/bin/env python3
"""Actual CM(-27) F3 height with exact cubic-ramification/basepoint pole cancellation."""
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
    for name in ['script-dir','branches','reference-connections','v-anchor','f2-polynomial','f2-audit','work-dir','output']:
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

    branches=load(args.branches);reference=load(args.reference_connections);anchor=load(args.v_anchor)
    assert branches['complete_actual4_T3_local_branches']
    assert branches['all4x73_actual_Hecke_pullback_coefficients_verified']
    assert branches['all4x54_canonical_Hecke_pullback_coefficients_verified']
    assert reference['complete_actual_F3_connections_for_CM_disk']
    J={k:[r.from_json(x) for x in v] for k,v in branches['source_projective_jets_0to4'].items()}
    assert len(J['W'])==5
    W0=J['W'][0]
    frame=r.from_json(branches['source_frame']);coordinate=r.from_json(branches['source_coordinate'])
    assert r.equal(frame,a.fc) and r.equal(r.mm(W0,frame),r.column([[1,0]]))
    connection=reference['actual_connections']['v_minus_b']
    q0=r.from_json(connection['denominator_linear_coefficients_mod47four'])
    s0=r.from_json(connection['numerator_quadratic_coefficients_mod47cubed'],q)
    WZ=r.from_json(connection['finite_pole_coordinates_fc_normalized'])
    assert r.equal(W0,r.rows(WZ,[0]));b=r.rows(WZ,[1])
    V2b,V3b=a.evaluate(b);Hb=r.mm(V3b,a.H)
    original=standard('p41_second_kind_connection47.json.gz')
    snu=r.from_json(original['numerator_cubic_sections'])
    vnu=r.from_json(original['denominator_linear_section'])
    sn=[r.mm(x,snu) for x in J['V3'][:3]]
    vn=[r.mm(x,vnu) for x in J['W'][:3]]
    assert np.all(r.units(vn[0]))
    S3=Series(a,3)
    nu=S3.mul(sn,S3.inverse(S3.mul(S3.mul(vn,vn),J['Hc'][:3])))
    gc=[red(r.from_json(reference['actual_gradients_original_nu_mod47cubed']['v_minus_b']))]
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
        "center_matches_actual_v_connection": True, "Frobenius": True,
    }
    save(args.work_dir / "actual_C_moving_connection47.json.gz", moving_cert)
    print("PASS actual moving C connection all", N*A[0][0].shape[0], "rows", flush=True)

    # The b branch has q_x(h(x)) of order3.  Its exact residue is -1 in
    # the target coarse j, hence isolate -dlog(j_target) before evaluation.
    branch_values=[];nonbase=[r.zeros(1,1) for _ in range(3)]
    bbranch=next(x for x in branches['branch_records'] if x['ramified_degree3_to_b'])
    assert len([x for x in branches['branch_records'] if x['ramified_degree3_to_b']])==1
    for rec in branches['branch_records']:
        if rec['ramified_degree3_to_b']:continue
        Wt=[red(r.from_json(x)) for x in rec['actual_image_W_coefficients_0to4']]
        Vt=[red(r.from_json(x)) for x in rec['actual_image_V2_coefficients_0to4']]
        factor=[red(r.from_json(x)) for x in rec['actual_differential_pullback_coefficients_0to3']]
        numerator=smul(mmconv(Vt[:4],sjets,4),factor,4)
        denominator=mmconv(Wt[:4],[red(x) for x in qjets_full[:4]],4)
        assert np.all(r.units(denominator[0])),('non-b actual branch auxiliary denominator',rec['branch_0based'])
        values=smul(numerator,sinv(denominator,4),4)
        nonbase=[r.add(x,y,q) for x,y in zip(nonbase,values[:3])]
        branch_values.append({'branch_0based':rec['branch_0based'],'numerator_coefficients_0to3_mod47cubed':[r.to_json(x) for x in numerator],'denominator_coefficients_0to3_mod47cubed':[r.to_json(x) for x in denominator],'pullback_coefficients_0to3_mod47cubed':[r.to_json(x) for x in values],'auxiliary_denominator_is_unit':True})
    BJ={k:[red(r.from_json(x)) for x in v] for k,v in bbranch['target_local_jets_0to4'].items()}
    assert r.equal(BJ['W'][0],red(b))
    bnum=smul([r.mm(x,s0,q) for x in BJ['V2'][:4]],BJ['inverse_Hc'][:4],4)
    bden=[r.mm(x,red(q0),q) for x in BJ['W']]
    assert r.iszero(bden[0]) and np.all(r.units(bden[1]))
    blaurent=smul(bnum,sinv(bden[1:5],4),4)
    assert r.equal(blaurent[0],scalar(-1))
    bj=[red(r.from_json(x)) for x in bbranch['target_local_j_coefficients_0to4']]
    assert r.iszero(bj[0]) and np.all(r.units(bj[1]))
    bregj=r.mul(r.add(blaurent[1],r.mul(bj[2],r.inverse_values(bj[1],q),q),q),r.inverse_values(bj[1],q),q)
    jtarget=[red(r.from_json(x)) for x in bbranch['actual_image_j_coefficients_0to4']]
    assert all(r.iszero(x) for x in jtarget[:3]) and np.all(r.units(jtarget[3]))
    jtprime=[a.scale(jtarget[k+1],k+1,q) for k in range(3)]
    logunit=[red(r.from_json(x)) for x in bbranch['log_of_j_target_over_x_cubed_derivative_coefficients_0to2']]
    vnum=smul([r.mm(red(x),s0,q) for x in J['V2'][:4]],[red(x) for x in J['inverse_Hc'][:4]],4)
    vden=[r.mm(red(x),red(q0),q) for x in J['W']]
    assert r.iszero(vden[0]) and np.all(r.units(vden[1]))
    vlaurent=smul(vnum,sinv(vden[1:5],4),4)
    assert r.equal(vlaurent[0],scalar(1))
    # -18*dlog(j_target) has residue -54; +54*eta_v has residue54.
    assert r.iszero(r.add(scalar(-54),a.scale(vlaurent[0],54,q),q))
    combined=[r.add(a.scale(r.add(r.neg(logunit[k],q),r.mul(bregj,jtprime[k],q),q),18,q),a.scale(vlaurent[k+1],54,q),q) for k in range(3)]
    print('PASS exact degree3 b-branch residue -54 plus fixed eta_v residue54; no 47 inversion',flush=True)
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
    j=[red(r.from_json(x)) for x in branches['source_true_CM_j_coefficients_0to4']]
    jp=[a.scale(j[k+1],k+1,q) for k in range(3)]
    jpp=[a.scale(j[k+2],(k+2)*(k+1),q) for k in range(3)]
    assert np.all(r.units(jp[0]))
    pieces={'18_three_nonbase_T3_branches':[a.scale(x,18,q) for x in nonbase],
            '18_ramified_base_branch_plus54_eta_v':combined,
            '4_self_regular_j':[r.sub(a.scale(x,4,q),a.scale(y,2,q),q) for x,y in zip(regular,mul3(jpp,inv3(jp)))]}
    for name,weight in [('c11_minus_b',-18),('Z12_minus22b',-9),('Z0fix_minus8b',-9),('D_minus20b',32*pow(3,-1,q))]:
        f=reference['actual_connections'][name];ss=r.from_json(f['numerator_quadratic_coefficients_mod47cubed'],q);qq=r.from_json(f['denominator_linear_coefficients_mod47four'],q)
        sv=[r.mm(red(x),ss,q) for x in J['V2'][:3]];qv=[r.mm(red(x),qq,q) for x in J['W'][:3]]
        assert np.all(r.units(qv[0])),('fixed denominator at CM27',name)
        pieces[name]=[a.scale(x,weight,q) for x in mul3(mul3(sv,inv3(qv)),invhc)]
    eta=standard('p41_eta_calibration47_complete.json.gz');sB=r.from_json(eta['numerator_coefficients'],q);qB=r.from_json(eta['denominator_coefficients'],q)
    sv=[r.mm(red(x),sB,q) for x in J['V3'][:3]];qv=[r.mm(red(x),qB,q) for x in J['V2'][:3]];assert np.all(r.units(qv[0]))
    pieces['minus_eta_B']=[a.scale(x,-1,q) for x in mul3(mul3(sv,inv3(qv)),invhc)]
    pieces['four_thirds_dlog_j']=[a.scale(x,4*pow(3,-1,q),q) for x in mul3(jp,inv3(j[:3]))]
    jm=list(j[:3]);jm[0]=r.sub(jm[0],scalar(1728),q);pieces['dlog_j_minus1728']=mul3(jp,inv3(jm))
    differential=[r.zeros(1,1) for _ in range(3)]
    for v in pieces.values():differential=[r.add(x,y,q) for x,y in zip(differential,v)]
    assert all(not np.any(x[1]) for x in differential)
    assert anchor==branches['source_CM_anchor']
    globals=standard('p41_global_qc_polynomials47_complete.json.gz');idx=globals['direction_indices'].index(3)
    aheight=next(v for v in anchor['all53_local_height_anchors_by_global_reciprocity'] if v['n']==3)
    scaled=aheight['scaled_by800_local_height_mod47four'];constant=aheight['canonical_local_sigma_height_mod47four'];assert scaled*pow(800,-1,Q)%Q==constant
    ycm=anchor['actual_original_y_mod47cubed'];assert ycm==75213
    heightw=[constant]+[int(x[0][0,0])*47**(k+1)*pow(k+1,-1,Q)%Q for k,x in enumerate(differential)]
    heighty=[sum(comb(n,k)*heightw[n]*pow(-ycm,n-k,Q) for n in range(k,4))%Q for k in range(4)]
    global_data=standard('p41_three_ordinary_CM_anchors_and_113_global_functions47.json.gz');gcenter=next(v for v in global_data['actual_113_rational_disk_global_polynomials'] if v['disk_id']==anchor['disk_id']);globaly=next(v for v in gcenter['global_polynomials'] if v['n']==3)['coefficients_0to4_in_y_mod47four']
    globalw=[sum(comb(n,k)*globaly[n]*pow(ycm,n-k,Q) for n in range(k,5))%Q for k in range(5)]
    assert globalw[0]==aheight['global_value_mod47four']
    qc=[(globaly[k]-800*(heighty[k] if k<4 else 0))%Q for k in range(5)];assert all(x%47==0 for x in qc)
    labels=globals['component_order'];assert labels==[0,3,28,32];targets=[v['QC_defect_target_mod47four'][idx] for v in globals['component_vectors']]
    assert (globalw[0]-800*constant)%Q==targets[labels.index(anchor['bad_component_at41'])]
    f2=load(args.f2_polynomial);audit=load(args.f2_audit);assert f2['disk_id']==audit['disk_id']==anchor['disk_id'];assert sha(args.f2_polynomial) in [v for k,v in audit['input_sha256'].items() if Path(k).name==args.f2_polynomial.name]
    candidates=audit['simple_single_F2_root_candidates_to_available_precision'];tests=[];remaining=[]
    for candidate in candidates:
        y=candidate['y_mod47cubed'];w=(y-ycm)%q;assert sum(c*pow(y,k,Q) for k,c in enumerate(f2['actual_QC_F2_coefficients_0to4_in_y_mod47four']))%Q==0;assert candidate['derivative_mod47']%47
        assert sum(c*pow(w,k,Q) for k,c in enumerate(heightw))%Q==sum(c*pow(y,k,Q) for k,c in enumerate(heighty))%Q
        value=sum(c*pow(y,k,Q) for k,c in enumerate(qc))%Q;checks=[]
        for label,target in zip(labels,targets):
            difference=(value-target)%Q;checks.append({'bad_component_label':label,'QC_F3_minus_target_mod47four':difference,'excluded':difference!=0})
            if difference==0:remaining.append({'y_mod47cubed':y,'bad_component_label':label})
        tests.append({'F2_y_mod47cubed':y,'w_mod47cubed':w,'F3_QC_value_mod47four':value,'same_bad_component_tests':checks})
    out={'result':'R316','level':41,'auxiliary_prime':47,'precision':4,'modulus':Q,'disk_id':anchor['disk_id'],'complete_actual_local_sigma_F3_polynomial_on_disk':True,
        'parameter':'x=z_R228-z_CM; w=x/47=y_R228-75213',
        'known_CM_anchor_scaled_by800_height':scaled,'known_CM_anchor_actual_height':constant,'source_CM_original_y_mod47cubed':ycm,
        'canonical_local_sigma_F3_height_coefficients_0to3_in_w_mod47four':heightw,'canonical_local_sigma_F3_height_coefficients_0to3_in_y_mod47four':heighty,
        'local_differential_coefficients_0to2_in_x_mod47cubed':[r.to_json(x) for x in differential],'differential_pieces_coefficients_mod47cubed':{k:[r.to_json(x) for x in v] for k,v in pieces.items()},
        'actual_CM_center_nu_coefficients_0to2_mod47four':[r.to_json(x) for x in nu],'actual_moving_connection':moving_cert,'actual_three_nonbase_branch_data':branch_values,
        'base_branch_numerator_coefficients_0to3_mod47cubed':[r.to_json(x) for x in bnum],'base_branch_denominator_coefficients_0to4_mod47cubed':[r.to_json(x) for x in bden],'eta_v_at_base_Laurent_coefficients_minus1_to2':[r.to_json(x) for x in blaurent],'eta_v_at_base_regular_j_coefficient':r.to_json(bregj),
        'fixed_eta_v_numerator_coefficients_0to3_mod47cubed':[r.to_json(x) for x in vnum],'fixed_eta_v_denominator_coefficients_0to4_mod47cubed':[r.to_json(x) for x in vden],'fixed_eta_v_Laurent_coefficients_minus1_to2':[r.to_json(x) for x in vlaurent],
        'ramified_base_pole_residue_minus54_cancels_fixed_v_plus54_before_evaluation':True,'ramified_branch_regular_term_uses_only_center_C0_because_jtarget_prime_starts_degree2':True,'no_nonunit_47_inverse_or_independent_factor_discarded':True,
        'actual_self_regular_x_coefficients_mod47cubed':[r.to_json(x) for x in regular],
        'global_F3_coefficients_0to4_in_y_mod47four':globaly,'global_F3_coefficients_0to4_in_w_mod47four':globalw,'actual_QC_F3_coefficients_0to4_in_y_mod47four':qc,
        'bad_component_labels':labels,'F3_bad_targets_in_same_component_order':targets,'actual_F2_candidates_checked_at_full_available_precision':tests,'remaining_F2_F3_candidate_and_component_pairs':remaining,'extra_non_CM_F2_root_excluded_in_all_four_components':all(x['y_mod47cubed']==ycm for x in remaining),
        'complete_all53_local_QC_heights':False,'complete_common_roots':False,'tail_bound':'The ramified branch is split exactly as -dlog(j_target) plus an analytic target remainder. Its -54/x residue is canceled with54eta_v before any numerical evaluation. Algebraic coefficients and inverse unit matrices are integral; only one primitive nu enters affinely. Thus height coefficient valuation >=-floor(log47(n))-v47(n), and every n>=4 term vanishes afterx47w modulo47^4. The y translation is exact.',
        'input_sha256':dict(a.inputs,**inputs),'source_sha256':sha(__file__),'runtime_seconds':round(time.monotonic()-started,3)}
    digest=save(args.output,out);print('PASS actual CM27 F3 cubic-ramification cancellation; lambda w',heightw,'y',heighty,'SHA',digest,flush=True);print('PASS same-component candidate tests',tests,'remaining',remaining,flush=True)
if __name__=='__main__':main()
