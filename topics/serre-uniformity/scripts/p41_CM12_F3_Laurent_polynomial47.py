#!/usr/bin/env python3
"""Actual CM(-12) F3 height: cancel its single horizontal pole against the full Z12 connection."""
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
    for name in ['script-dir','branches','reference-connections','source-connections','t2-branches','basic-anchors','f2-polynomial','f2-audit','work-dir','output']:
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

    branches=load(args.branches);reference=load(args.reference_connections);source_reference=load(args.source_connections);anchors=load(args.basic_anchors)
    assert branches['source_center_is_exact_CM_minus12']
    assert branches['all4x73_T3_pullback_trace_coefficients_verified']
    assert branches['all4x54_canonical_T3_pullback_trace_coefficients_verified']
    assert reference['complete_actual_F3_connections_for_CM_disk']
    J={k:[r.from_json(x) for x in v] for k,v in branches['source_projective_jets_0to4'].items()}
    assert len(J['W'])==5
    W0=J['W'][0]
    frame=r.from_json(branches['source_frame']);coordinate=r.from_json(branches['source_coordinate'])
    assert r.equal(frame,a.fc) and r.equal(r.mm(W0,frame),r.column([[1,0]]))
    assert source_reference['complete_actual_F2_connections_for_SS_disk']
    connection=source_reference['actual_connections']['u_minus_b']
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
    gc=[red(r.from_json(source_reference['actual_gradients_original_nu_mod47cubed']['u_minus_b']))]
    gc += [a.scale(red(nu[k-1]),pow(k,-1,q),q) for k in range(1,4)]
    assert r.equal(gc[0],r.from_json(connection['calibration_gradient_original_nu_mod47cubed'],q))
    assert all(r.equal(r.conjugate(x,q),r.cols(x,original['pole_Frobenius_permutation_0based'])) for x in gc)
    # Reuse the complete R321 family at exactly the same true CM point.
    # The global connection C(x) is independent of which Hecke direction evaluates it.
    f2=load(args.f2_polynomial);t2branches=load(args.t2_branches)
    assert f2['complete_actual_local_sigma_F2_polynomial_on_disk']
    assert f2['disk_id']==t2branches['disk_id']==branches['disk_id']=='SS_j44_02'
    assert branches['source_projective_jets_0to4']==t2branches['source_projective_jets_0to4']
    assert branches['source_frame']==t2branches['source_frame']
    assert branches['source_coordinate']==t2branches['source_coordinate']
    assert sha(args.t2_branches) in [v for k,v in f2['input_sha256'].items() if Path(k).name==args.t2_branches.name]
    assert sha(args.source_connections) in [v for k,v in f2['input_sha256'].items() if Path(k).name==args.source_connections.name]
    assert [r.to_json(x) for x in nu]==f2['actual_CM_center_nu_coefficients_0to2_mod47four']
    moving_cert=f2['actual_moving_connection']
    assert moving_cert['all_four_coefficient_equations'] and moving_cert['center_matches_actual_u_connection'] and moving_cert['Frobenius']
    assert moving_cert['full_equation_rows']==955
    assert [r.to_json(x) for x in gc]==moving_cert['gradient_original_nu_coefficients_0to3_mod47cubed']
    qjets_full=[r.from_json(x) for x in moving_cert['q_linear_coefficients_in_parameter_0to4_mod47four']]
    qjets=[red(x) for x in qjets_full[:N]]
    sjets=[r.from_json(x,q) for x in moving_cert['s_quadratic_coefficients_in_parameter_0to3_mod47cubed']]
    assert r.equal(qjets_full[0],q0) and r.equal(sjets[0],s0)
    print('PASS unchanged R321 moving C family: all3820 equations were verified in its bound certificate',flush=True)

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
    fixedZ12=reference['actual_connections']['Z12_minus22b']
    Z12s=r.from_json(fixedZ12['numerator_quadratic_coefficients_mod47cubed'],q)
    Z12q=r.from_json(fixedZ12['denominator_linear_coefficients_mod47four'],q)
    Z12sv=[r.mm(red(x),Z12s,q) for x in J['V2'][:4]]
    Z12numerator=smul(Z12sv,[red(x) for x in J['inverse_Hc'][:4]],4)
    Z12denominator=[r.mm(red(x),Z12q,q) for x in J['W']]
    assert r.iszero(Z12denominator[0]) and np.all(r.units(Z12denominator[1]))
    Z12laurent=smul(Z12numerator,sinv(Z12denominator[1:5],4),4)
    assert r.equal(Z12laurent[0],scalar(1))
    assert r.equal(horizontal_residue,scalar(pow(2,-1,q)))
    assert r.iszero(r.sub(a.scale(horizontal_residue,18,q),a.scale(Z12laurent[0],9,q),q))
    combined=[]
    for k in range(3):
        value=a.scale(Z12laurent[k+1],-pow(2,-1,q),q)
        for record in branch_values:
            value=r.add(value,r.from_json(record['coefficients_mod47cubed'][k+int(record['horizontal'])],q),q)
        combined.append(value)
    print('PASS actual single horizontal +9 residue and exact -9 full-Z12 cancellation',flush=True)
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
    pieces={'18_T3_eta_C_minus9_eta_Z12':[a.scale(x,18,q) for x in combined],
        '4_self_regular_j':[r.sub(a.scale(x,4,q),a.scale(y,2,q),q) for x,y in zip(regular,mul3(jpp,inv3(jp)))]}
    fixed_fraction_certificates={}
    def regular_fraction(name,f):
        sold=r.from_json(f['numerator_quadratic_coefficients_mod47cubed'],q)
        qold=r.from_json(f['denominator_linear_coefficients_mod47four'])
        if np.all(r.units(r.mm(W0,qold))):return sold,red(qold)
        Wpoles=r.from_json(f['finite_pole_coordinates_fc_normalized'])
        rp,cp=r.rank_pivots(Wpoles)
        Kp,_,_=r.kernel_from_rows(r.rows(Wpoles,rp),rp,cp)
        assert r.iszero(r.mm(Wpoles,Kp))
        rng=random.Random(4104732400+len(fixed_fraction_certificates))
        for attempt in range(100):
            xx=r.mm(Kp,r.column([[rng.randrange(47),rng.randrange(47)] for _ in range(Kp[0].shape[1])]))
            qnew=r.add(xx,r.mm(M['A1'],r.conjugate(xx)))
            if np.all(r.units(r.mm(W0,qnew))):break
        else:raise AssertionError(('no regular fixed denominator',name))
        assert r.iszero(r.mm(Wpoles,qnew))
        assert r.equal(qnew,r.mm(M['A1'],r.conjugate(qnew)))
        qov=r.mm(red(M['W']),red(qold),q);qnv=r.mm(red(M['W']),red(qnew),q)
        sov=r.mm(red(M['V2']),sold,q)
        good=np.flatnonzero(r.units(qov)[:,0]).tolist();assert len(good)>378
        E=red(r.rows(M['V2'],good));er,ec=r.rank_pivots(E)
        assert len(er)==199 and ec==list(range(199))
        wanted=r.mul(r.mul(r.rows(sov,good),r.rows(qnv,good),q),r.inverse_values(r.rows(qov,good),q),q)
        snew=r.mm(r.inverse_matrix(r.rows(E,er),q),r.rows(wanted,er),q)
        assert r.equal(r.mm(E,snew,q),wanted)
        assert r.equal(r.mul(r.mm(red(M['V2']),snew,q),qov,q),r.mul(sov,qnv,q))
        assert r.equal(snew,r.mm(red(M['A2']),r.conjugate(snew,q),q))
        fixed_fraction_certificates[name]={'numerator_quadratic_coefficients_mod47cubed':r.to_json(snew),'denominator_linear_coefficients_mod47four':r.to_json(qnew),'actual_poles_annihilated':True,'source_denominator_is_unit':True,'all820_V3_cross_multiplication_identity':True,'faithful_V3_degree_bound':378,'original_unit_rows':good,'V2_unit_minor_rows_in_good_rows':er,'Frobenius':True}
        print('PASS actual fixed connection unit-denominator replacement',name,'all820 V3 identities',flush=True)
        return snew,red(qnew)
    for name,weight in [('v_minus_b',54),('c11_minus_b',-18),('Z0fix_minus8b',-9),('D_minus20b',32*pow(3,-1,q))]:
        f=reference['actual_connections'][name]
        ss,qq=regular_fraction(name,f)
        sv=[r.mm(red(x),ss,q) for x in J['V2'][:3]]
        qv=[r.mm(red(x),qq,q) for x in J['W'][:3]]
        assert np.all(r.units(qv[0])),('fixed auxiliary denominator at CM12',name)
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
    anchor=next(x for x in anchors['records'] if x['label']=='P_minus12')
    assert anchor==branches['source_CM_anchor']
    globals=standard('p41_global_qc_polynomials47_complete.json.gz');idx=globals['direction_indices'].index(3)
    ycm=anchor['actual_original_y_mod47cubed'];assert ycm==96923
    anchorheight=next(x for x in anchor['all53_local_height_anchors_by_global_reciprocity'] if x['n']==3)
    scaled=anchorheight['scaled_by800_local_height_mod47four']
    constant=scaled*pow(800,-1,Q)%Q
    heightw=[constant]+[int(x[0][0,0])*47**(k+1)*pow(k+1,-1,Q)%Q for k,x in enumerate(differential)]
    heighty=[sum(comb(n,k)*heightw[n]*pow(-ycm,n-k,Q) for n in range(k,4))%Q for k in range(4)]
    known=standard('p41_three_ordinary_CM_anchors_and_113_global_functions47.json.gz')
    diskglobal=next(x for x in known['actual_113_rational_disk_global_polynomials'] if x['disk_id']=='SS_j44_02')
    globaly=next(x for x in diskglobal['global_polynomials'] if x['n']==3)['coefficients_0to4_in_y_mod47four']
    globalw=[sum(comb(n,k)*globaly[n]*pow(ycm,n-k,Q) for n in range(k,5))%Q for k in range(5)]
    qc=[(globaly[k]-800*(heighty[k] if k<4 else 0))%Q for k in range(5)]
    assert all(x%47==0 for x in qc)
    labels=globals['component_order'];assert labels==[0,3,28,32]
    targets=[v['QC_defect_target_mod47four'][idx] for v in globals['component_vectors']]
    assert (globalw[0]-800*constant)%Q==targets[labels.index(anchor['bad_component_at41'])]
    audit=load(args.f2_audit)
    assert f2['disk_id']==audit['disk_id']=='SS_j44_02'
    assert sha(args.f2_polynomial) in [v for k,v in audit['input_sha256'].items() if Path(k).name==args.f2_polynomial.name]
    rootchecks=audit['componentwise_independent_digit_lift_root_checks']
    assert len(rootchecks)==4 and all(x['actual_simple_roots_mod47cubed']==rootchecks[0]['actual_simple_roots_mod47cubed'] for x in rootchecks)
    candidates=[{'y_mod47cubed':y,'derivative_mod47':d} for y,d in zip(rootchecks[0]['actual_simple_roots_mod47cubed'],rootchecks[0]['derivative_mod47'])];assert len(candidates)==2
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
    out={'result':'R324','level':41,'auxiliary_prime':47,'precision':4,'modulus':Q,'disk_id':'SS_j44_02',
        'complete_actual_local_sigma_F3_polynomial_on_disk':True,
        'parameter':'x=z_R228-z_CM and w=x/47=y_R228-96923; exact unit translation of the original disk',
        'known_CM_anchor_scaled_by800_height':scaled,'known_CM_anchor_actual_height':constant,
        'source_CM_original_y_mod47cubed':ycm,
        'canonical_local_sigma_F3_height_coefficients_0to3_in_w_mod47four':heightw,
        'canonical_local_sigma_F3_height_coefficients_0to3_in_y_mod47four':heighty,
        'local_differential_coefficients_0to2_in_x_mod47cubed':[r.to_json(x) for x in differential],
        'differential_pieces_coefficients_mod47cubed':{k:[r.to_json(x) for x in v] for k,v in pieces.items()},
        'actual_CM_center_nu_coefficients_0to2_mod47four':[r.to_json(x) for x in nu],
        'actual_moving_connection':moving_cert,
        'actual_branch_Laurent_data':branch_values,
        'actual_fixed_connection_unit_fraction_replacements':fixed_fraction_certificates,
        'actual_fixed_eta_Z12_Laurent_coefficients_minus1_to2_mod47cubed':[r.to_json(x) for x in Z12laurent],
        'actual_fixed_eta_Z12_numerator_coefficients_0to3_mod47cubed':[r.to_json(x) for x in Z12numerator],
        'actual_fixed_eta_Z12_denominator_coefficients_0to4_mod47cubed':[r.to_json(x) for x in Z12denominator],
        'horizontal_residue_exactly_one_half_and_weighted_plus9_minus9_cancel_before_evaluation':True,
        'unchanged_R321_moving_connection_reused_with_all_input_and_source_jets_matched':True,
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
    print('PASS CM12 actual combined Laurent F3 polynomial in w',heightw,'in original y',heighty,'SHA',digest,flush=True)
    print('PASS actual same-component tests remaining',remaining,flush=True)


if __name__=='__main__':main()
