#!/usr/bin/env python3
"""Actual CM(-11) F3 height: combine two horizontal Laurent poles at the exact CM center."""
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
    for name in ['script-dir','branches','reference-connections','cm-anchors','f2-polynomial','f2-audit','work-dir','output']:
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

    branches=load(args.branches);reference=load(args.reference_connections);anchors=load(args.cm_anchors)
    assert branches['source_center_is_exact_CM_minus11']
    assert branches['all4x73_T3_pullback_trace_coefficients_verified']
    assert branches['all4x54_canonical_T3_pullback_trace_coefficients_verified']
    assert reference['complete_actual_F3_connections_for_CM_disk']
    J={k:[r.from_json(x) for x in v] for k,v in branches['source_projective_jets_0to4'].items()}
    assert len(J['W'])==5
    W0=J['W'][0]
    frame=r.from_json(branches['source_frame']);coordinate=r.from_json(branches['source_coordinate'])
    assert r.equal(frame,a.fc) and r.equal(r.mm(W0,frame),r.column([[1,0]]))
    connection=reference['actual_connections']['c11_minus_b']
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
    gc=[red(r.from_json(reference['actual_gradients_original_nu_mod47cubed']['c11_minus_b']))]
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
        "center_matches_actual_c11_connection": True, "Frobenius": True,
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
        factor=[red(r.from_json(x)) for x in record['actual_differential_pullback_factor_coefficients_0to3']]
        sv=mmconv(V2t[:4],sjets,4)
        numerator=smul(sv,factor,4)
        denominator=mmconv(Wt,qfull,5)
        horizontal=record['horizontal_fixed_point']
        if horizontal:
            assert r.iszero(denominator[0]) and np.all(r.units(denominator[1]))
            values=smul(numerator,sinv(denominator[1:5],4),4)
            hp=red(r.from_json(record['target_parameter_coefficients_0to4_in_source_CM_x'][1]))
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
    c11sv=[r.mm(red(x),s0,q) for x in J['V2'][:4]]
    c11numerator=smul(c11sv,[red(x) for x in J['inverse_Hc'][:4]],4)
    c11denominator=[r.mm(red(x),red(q0),q) for x in J['W']]
    assert r.iszero(c11denominator[0]) and np.all(r.units(c11denominator[1]))
    c11laurent=smul(c11numerator,sinv(c11denominator[1:5],4),4)
    assert r.equal(c11laurent[0],scalar(1)) and r.equal(horizontal_residue,scalar(1))
    assert r.iszero(r.sub(horizontal_residue,c11laurent[0],q))
    combined=[]
    for k in range(3):
        value=r.neg(c11laurent[k+1],q)
        for record in branch_values:
            value=r.add(value,r.from_json(record['coefficients_mod47cubed'][k+int(record['horizontal'])],q),q)
        combined.append(value)
    print('PASS both actual horizontal Laurent residues and exact cancellation with eta_c11',flush=True)
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
    jfull=[r.from_json(x) for x in branches['source_CM_j_coefficients_0to4']]
    j=[red(x) for x in jfull]
    jp=[a.scale(j[k+1],k+1,q) for k in range(3)]
    jpp=[a.scale(j[k+2],(k+2)*(k+1),q) for k in range(3)]
    assert np.all(r.units(jp[0]))
    pieces={'18_T3_eta_C_minus_eta_c11':[a.scale(x,18,q) for x in combined],
        '4_self_regular_j':[r.sub(a.scale(x,4,q),a.scale(y,2,q),q) for x,y in zip(regular,mul3(jpp,inv3(jp)))]}
    for name,weight in [('v_minus_b',54),('Z12_minus22b',-9),('Z0fix_minus8b',-9),('D_minus20b',32*pow(3,-1,q))]:
        f=reference['actual_connections'][name]
        ss=r.from_json(f['numerator_quadratic_coefficients_mod47cubed'],q)
        qq=r.from_json(f['denominator_linear_coefficients_mod47four'],q)
        sv=[r.mm(red(x),ss,q) for x in J['V2'][:3]]
        qv=[r.mm(red(x),qq,q) for x in J['W'][:3]]
        assert np.all(r.units(qv[0])),('fixed auxiliary denominator at CM11',name)
        pieces[name]=[a.scale(x,weight,q) for x in mul3(mul3(sv,inv3(qv)),invhc)]
    eta=standard('p41_eta_calibration47_complete.json.gz')
    sB=r.from_json(eta['numerator_coefficients'],q);qB=r.from_json(eta['denominator_coefficients'],q)
    sv=[r.mm(red(x),sB,q) for x in J['V3'][:3]]
    qv=[r.mm(red(x),qB,q) for x in J['V2'][:3]]
    assert np.all(r.units(qv[0]))
    pieces['minus_eta_B']=[a.scale(x,-1,q) for x in mul3(mul3(sv,inv3(qv)),invhc)]
    pieces['four_thirds_dlog_j']=[a.scale(x,4*pow(3,-1,q),q) for x in mul3(jp,inv3(j[:3]))]
    jm=list(j[:3]);jm[0]=r.sub(jm[0],scalar(1728),q)
    pieces['dlog_j_minus1728']=mul3(jp,inv3(jm))
    differential=[r.zeros(1,1) for _ in range(3)]
    for v in pieces.values():differential=[r.add(x,y,q) for x,y in zip(differential,v)]
    assert all(not np.any(x[1]) for x in differential)
    anchor=next(x for x in anchors['three_ordinary_CM_anchors'] if x['disk_id']=='ORD_j38')
    assert anchor==branches['source_CM_anchor']
    globals=standard('p41_global_qc_polynomials47_complete.json.gz');idx=globals['direction_indices'].index(3)
    ycm=anchor['rescaled_parameter_y_of_CM_point_mod47cubed'];assert ycm==94227
    scaled=anchor['local_global_section_heights_at_CM_point_by_global_reciprocity'][idx]
    constant=scaled*pow(800,-1,Q)%Q
    heightw=[constant]+[int(x[0][0,0])*47**(k+1)*pow(k+1,-1,Q)%Q for k,x in enumerate(differential)]
    heighty=[sum(comb(n,k)*heightw[n]*pow(-ycm,n-k,Q) for n in range(k,4))%Q for k in range(4)]
    globaly=next(x for x in anchor['global_polynomials_at_rational_center'] if x['n']==3)['coefficients_0to4_in_y_mod47four']
    globalw=[sum(comb(n,k)*globaly[n]*pow(ycm,n-k,Q) for n in range(k,5))%Q for k in range(5)]
    qc=[(globaly[k]-800*(heighty[k] if k<4 else 0))%Q for k in range(5)]
    assert all(x%47==0 for x in qc)
    labels=globals['component_order'];assert labels==[0,3,28,32]
    targets=[v['QC_defect_target_mod47four'][idx] for v in globals['component_vectors']]
    assert (globalw[0]-800*constant)%Q==targets[labels.index(anchor['bad_component_at41'])]
    f2=load(args.f2_polynomial);audit=load(args.f2_audit)
    assert f2['disk_id']==audit['disk_id']=='ORD_j38'
    assert sha(args.f2_polynomial) in [v for k,v in audit['input_sha256'].items() if Path(k).name==args.f2_polynomial.name]
    candidates=audit['simple_single_F2_root_candidates_to_available_precision'];assert len(candidates)==2
    tests=[];remaining=[]
    for candidate in candidates:
        y=candidate['y_mod47cubed'];w=(y-ycm)%q
        assert sum(c*pow(y,k,Q) for k,c in enumerate(f2['actual_QC_F2_coefficients_0to4_in_y_mod47four']))%Q==0
        assert candidate['derivative_mod47']%47
        hv=sum(c*pow(w,k,Q) for k,c in enumerate(heightw))%Q
        assert hv==sum(c*pow(y,k,Q) for k,c in enumerate(heighty))%Q
        value=sum(c*pow(y,k,Q) for k,c in enumerate(qc))%Q
        checks=[]
        for label,target in zip(labels,targets):
            difference=(value-target)%Q
            checks.append({'bad_component_label':label,'QC_F3_minus_target_mod47four':difference,'excluded':difference!=0})
            if difference==0:remaining.append({'y_mod47cubed':y,'bad_component_label':label})
        tests.append({'F2_y_mod47cubed':y,'w_mod47cubed':w,'F3_QC_value_mod47four':value,'same_bad_component_tests':checks})
    out={'result':'R310','level':41,'auxiliary_prime':47,'precision':4,'modulus':Q,'disk_id':'ORD_j38',
        'complete_actual_local_sigma_F3_polynomial_on_disk':True,
        'parameter':'x=z_R231-z_CM and w=x/47=y_R231-94227; exact unit translation of the original disk',
        'known_CM_anchor_scaled_by800_height':scaled,'known_CM_anchor_actual_height':constant,
        'source_CM_original_y_mod47cubed':ycm,
        'canonical_local_sigma_F3_height_coefficients_0to3_in_w_mod47four':heightw,
        'canonical_local_sigma_F3_height_coefficients_0to3_in_y_mod47four':heighty,
        'local_differential_coefficients_0to2_in_x_mod47cubed':[r.to_json(x) for x in differential],
        'differential_pieces_coefficients_mod47cubed':{k:[r.to_json(x) for x in v] for k,v in pieces.items()},
        'actual_CM_center_nu_coefficients_0to2_mod47four':[r.to_json(x) for x in nu],
        'actual_moving_connection':moving_cert,
        'actual_branch_Laurent_data':branch_values,
        'actual_fixed_eta_c11_Laurent_coefficients_minus1_to2_mod47cubed':[r.to_json(x) for x in c11laurent],
        'actual_fixed_eta_c11_numerator_coefficients_0to3_mod47cubed':[r.to_json(x) for x in c11numerator],
        'actual_fixed_eta_c11_denominator_coefficients_0to4_mod47cubed':[r.to_json(x) for x in c11denominator],
        'horizontal_residue_sum_exactly_one_and_all_poles_cancel_before_evaluation':True,
        'all_divisions_by_horizontal_parameter_are_exact_x_coefficient_shifts':True,
        'no_independent_47_factor_discarded':True,
        'actual_self_regular_x_coefficients_mod47cubed':[r.to_json(x) for x in regular],
        'global_F3_coefficients_0to4_in_y_mod47four':globaly,
        'global_F3_coefficients_0to4_in_w_mod47four':globalw,
        'actual_QC_F3_coefficients_0to4_in_y_mod47four':qc,
        'bad_component_labels':labels,'F3_bad_targets_in_same_component_order':targets,
        'actual_F2_candidates_checked_at_full_available_precision':tests,
        'remaining_F2_F3_candidate_and_component_pairs':remaining,
        'extra_non_CM_F2_root_excluded_in_all_four_components':all(x['y_mod47cubed']==ycm for x in remaining),
        'complete_all53_local_QC_heights':False,'complete_common_roots':False,
        'tail_bound':'After exact x division each horizontal regular term needs the C family through order n for height coefficient x^n. The unique nonintegral input remains one primitive of integral nu; valuation>=-floor(log_47(n))-v47(n). Thus n>=4 terms vanish after x=47w modulo47^4. Translation w=y-yCM is exact and integral.',
        'input_sha256':dict(a.inputs,**inputs),'source_sha256':sha(__file__),'runtime_seconds':round(time.monotonic()-started,3)}
    digest=save(args.output,out)
    print('PASS CM11 actual combined Laurent F3 polynomial in w',heightw,'in original y',heighty,'SHA',digest,flush=True)
    print('PASS actual same-component tests remaining',remaining,flush=True)


if __name__=='__main__':main()
