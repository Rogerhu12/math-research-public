#!/usr/bin/env python3
"""Actual three T2 branches at either selected true CM(-8) level point.

The original full-level branch fixes the residue point. Its actual target at
the CM lift is recovered in the same etale j chart, then all four coefficients
of all73 differential pullbacks are checked against the published operator.
"""
import argparse
import gzip
import hashlib
import json
from pathlib import Path
import sys
from types import SimpleNamespace


def read(p):
    p=Path(p)
    return json.loads(gzip.decompress(p.read_bytes()) if p.suffix=='.gz' else p.read_bytes())


def sha(p):
    return hashlib.sha256(Path(p).read_bytes()).hexdigest()


def main():
    ap=argparse.ArgumentParser(description=__doc__)
    for key in ['script-dir','support','work-dir','output']:
        ap.add_argument('--'+key,type=Path,required=True)
    ap.add_argument('--disk-id',required=True)
    args=ap.parse_args()
    folder=args.script_dir.resolve()
    sys.path.insert(0,str(folder))
    from p41_actual_differentials47 import ActualModel,save
    from p41_projective_jet_frames47 import ProjectiveJetFrames,install_exact_float_mm
    from p41_native_r2_linear47 import install
    from p41_elliptic_coarse_atlas47 import ClassicalInvariants,Series
    from p41_CM8_diagonal_cancellation47 import j_coefficients
    import p41_r2_matrix as r
    install_exact_float_mm(r)
    install(r,args.work_dir/'native')
    a=ActualModel(folder)
    frames=ProjectiveJetFrames(a)
    Q,N=r.Q,5
    S=Series(a,N)
    support=read(args.support)
    assert support['source_disk_id']==args.disk_id
    label={'SS_j10_06':'Z_minus8_679','SS_j10_18':'Z_minus8_16'}[args.disk_id]
    cm=a.read('p41_cm_quadratic_jets47_raw.json.gz')
    atlas=a.read('p41_rational_SS_residue_atlas47_complete.json.gz')
    derivative=a.read('p41_cleared_serre_derivative47_complete.json.gz')
    hecke=a.read('p41_hecke47_full_saved.json.gz')['operators']['2']
    invariants=ClassicalInvariants(SimpleNamespace(a=a,r=r,v=r.from_json(derivative['chosen_clearing_section']),G=r.from_json(derivative['cleared_derivative_coefficients'])))
    WQ=r.from_json([next(x for x in cm['records'] if x['label']==label)['normalized_weight2_coefficients'][0]])
    chart=next(c for c in atlas['charts'] if args.disk_id in c['disk_ids'])
    coordinate=r.from_json(chart['coordinate'])
    assert r.equal(r.from_json(chart['frame']),a.fc)
    WP=r.from_json([support['actual_source_W_fc_normalized']])
    zQ=r.sub(r.mm(WQ,coordinate),r.mm(WP,coordinate))
    assert not a.np.any(zQ[1]) and not a.np.any(zQ[0]%47)
    yQ=int(zQ[0][0,0])//47
    J=frames.local_jets(WQ,a.fc,coordinate,order=4)
    jsource=j_coefficients(a,invariants,J['W'])

    def const(c):
        if not isinstance(c,(tuple,list)):c=[int(c)%Q,0]
        return [r.column([c])]+[r.zeros(1,1) for _ in range(N-1)]

    def centered(v):
        return [r.zeros(*v[0][0].shape)]+v[1:]

    def ellj(A,B):
        aa=S.power(A,3)
        return S.scale(S.mul(aa,S.inverse(S.add(S.scale(aa,4),S.scale(S.power(B,2),27)))),6912)

    def evaluate(coefficients,t):
        value=r.zeros(*coefficients[0][0].shape)
        for coefficient in reversed(coefficients):value=r.add(r.mul(value,t),coefficient)
        return value

    def dump(JJ):
        return {k:[r.to_json(v) for v in JJ[k]] for k in ['W','V2','V3','Hc','inverse_Hc']}

    assert r.equal(jsource[0],const(8000)[0])
    A=const(support['actual_source_model'][0])
    Bbase=const(support['actual_source_model'][1])[0]
    wanted_B2=a.scale(r.mul(r.mul(A[0],A[0]),A[0]),(6912*pow(8000,-1,Q)-4)*pow(27,-1,Q))
    BCM=Bbase
    for _ in range(3):BCM=a.scale(r.add(BCM,r.mul(wanted_B2,r.inverse_values(BCM))),pow(2,-1,Q))
    assert r.equal(r.mul(BCM,BCM),wanted_B2)
    assert all(not a.np.any((x-y)%47) for x,y in zip(BCM,Bbase))
    Bphysical=[BCM]+const(0)[1:]
    Bphysical[1]=const(1)[0]
    jp=ellj(A,Bphysical)
    assert r.equal(jp[0],jsource[0])
    tsource=S.compose(S.reversion(centered(jp),N),centered(jsource))
    Bofx=S.add([BCM]+const(0)[1:],tsource)
    assert all(r.equal(v,w) for v,w in zip(ellj(A,Bofx),jsource))
    records=[]
    for branch in support['branch_records']:
        old=branch['actual_saved_full_level_record']
        assert old['ell']==old['degree']==old['determinant_mod41']==2
        root=r.neg(const(old['kernel'][0])[0])
        for _ in range(3):
            f=r.add(r.add(r.mul(r.mul(root,root),root),r.mul(A[0],root)),BCM)
            df=r.add(a.scale(r.mul(root,root),3),A[0])
            root=r.sub(root,r.mul(f,r.inverse_values(df)))
        assert r.iszero(r.add(r.add(r.mul(r.mul(root,root),root),r.mul(A[0],root)),BCM))
        roots=[root]+const(0)[1:]
        for _ in range(3):
            f=S.add(S.add(S.power(roots,3),S.mul(A,roots)),Bofx)
            df=S.add(S.scale(S.power(roots,2),3),A)
            roots=S.sub(roots,S.mul(f,S.inverse(df)))
        assert all(r.iszero(v) for v in S.add(S.add(S.power(roots,3),S.mul(A,roots)),Bofx))
        At=S.sub(S.scale(A,-4),S.scale(S.power(roots,2),15))
        Bt=S.add(S.scale(Bofx,22),S.scale(S.mul(A,roots),14))
        jimage=ellj(At,Bt)
        WT=r.from_json([branch['W_actual_values_in_R2']])
        oldjet=next(frames.iter_charts(WT,order=4,max_points=1,label='CM8_T2_target_old'))
        oldj=j_coefficients(a,invariants,oldjet['W'])
        delta=r.sub(jimage[0],oldj[0])
        assert all(not a.np.any(v%47) for v in delta)
        displacement=evaluate(S.reversion(centered(oldj),N),delta)
        WCM=evaluate(oldjet['W'],displacement)
        assert r.equal(r.mm(WCM,oldjet['frame']),const(1)[0])
        JT=frames.local_jets(WCM,oldjet['frame'],oldjet['coordinate'],order=4)
        jt=j_coefficients(a,invariants,JT['W'])
        assert r.equal(jt[0],jimage[0])
        h=S.compose(S.reversion(centered(jt),N),centered(jimage))
        assert all(r.equal(v,w) for v,w in zip(S.compose(jt,h),jimage))
        Wi=S.compose(JT['W'],h)
        V2i=S.compose(JT['V2'],h)
        V3i=S.compose(JT['V3'],h)
        Hci=S.compose(JT['Hc'],h)
        S4=Series(a,4)
        fac=S4.mul([a.scale(h[k+1],k+1) for k in range(4)],S4.inverse(Hci[:4]))
        WCMfc=r.mul(WCM,r.inverse_values(r.mm(WCM,a.fc)))
        horizontal=r.equal(WCMfc,WQ)
        djratio=r.mul(jimage[1],r.inverse_values(jsource[1]))
        if horizontal:assert r.equal(djratio,const(-1)[0])
        records.append({'branch_0based':branch['branch_0based'],'horizontal_fixed_point':horizontal,
                        'actual_saved_raw_level_record':old,'same_full_level_etale_lift_from_original_target':True,
                        'old_target_frame':r.to_json(oldjet['frame']),'old_target_coordinate':r.to_json(oldjet['coordinate']),
                        'old_target_jets_0to4':dump(oldjet),'old_target_j_coefficients_0to4':[r.to_json(x) for x in oldj],
                        'old_to_true_CM_target_coordinate_displacement':r.to_json(displacement),
                        'target_at_true_CM_W_fc_normalized':r.to_json(WCMfc),
                        'target_frame':r.to_json(JT['frame']) if 'frame' in JT else r.to_json(oldjet['frame']),
                        'target_coordinate':r.to_json(oldjet['coordinate']),
                        'target_local_jets_0to4':dump(JT),
                        'target_local_j_coefficients_0to4':[r.to_json(x) for x in jt],
                        'kernel_coefficients_0to4':[r.to_json(x) for x in roots],
                        'target_A_coefficients_0to4':[r.to_json(x) for x in At],
                        'target_B_coefficients_0to4':[r.to_json(x) for x in Bt],
                        'actual_image_j_coefficients_0to4':[r.to_json(x) for x in jimage],
                        'actual_image_parameter_coefficients_0to4':[r.to_json(x) for x in h],
                        'actual_image_W_coefficients_0to4':[r.to_json(x) for x in Wi],
                        'actual_image_V2_coefficients_0to4':[r.to_json(x) for x in V2i],
                        'actual_image_V3_coefficients_0to4':[r.to_json(x) for x in V3i],
                        'actual_image_Hc_coefficients_0to4':[r.to_json(x) for x in Hci],
                        'actual_differential_pullback_coefficients_0to3':[r.to_json(x) for x in fac],
                        'actual_d_jtarget_over_d_jsource_at_CM':r.to_json(djratio)})
        print('PASS CM8 true T2 branch',args.disk_id,branch['branch_0based'],'horizontal',horizontal,flush=True)
    assert sum(x['horizontal_fixed_point'] for x in records)==1
    trace=[r.zeros(1,73) for _ in range(4)]
    for record in records:
        contribution=Series(a,4).mul([r.from_json(x) for x in record['actual_image_W_coefficients_0to4'][:4]],
                                    [r.from_json(x) for x in record['actual_differential_pullback_coefficients_0to3']])
        trace=[r.add(v,w) for v,w in zip(trace,contribution)]
    source=Series(a,4).mul(J['W'][:4],J['inverse_Hc'][:4])
    assert all(r.equal(v,r.mm(w,r.from_json(hecke['weight2_operator']))) for v,w in zip(trace,source))
    assert all(r.equal(r.mm(v,a.K1),r.mm(r.mm(w,a.K1),r.from_json(hecke['canonical_operator']))) for v,w in zip(trace,source))
    out={'result':'R368' if args.disk_id.endswith('06') else 'R370','disk_id':args.disk_id,
         'exact_CM8_label':label,'source_original_y_mod47cubed':yQ,
         'source_true_CM_W_fc_normalized':r.to_json(WQ),'source_frame':r.to_json(a.fc),
         'source_coordinate':r.to_json(coordinate),'source_true_CM_projective_jets_0to4':dump(J),
         'source_true_CM_physical_A':r.to_json(A[0]),'source_true_CM_physical_B':r.to_json(BCM),
         'source_true_CM_j_coefficients_0to4':[r.to_json(x) for x in jsource],
         'source_physical_B_displacement_coefficients_0to4':[r.to_json(x) for x in tsource],
         'branch_records':records,'all4x73_T2_pullback_trace_coefficients_verified':True,
         'all4x54_canonical_T2_pullback_trace_coefficients_verified':True,
         'exactly_one_true_full_level_horizontal_branch':True,'horizontal_derivative_in_j_is_minus_one':True,
         'complete_actual_height':False,'input_sha256':dict(a.inputs,**{str(args.support):sha(args.support)}),
         'source_sha256':sha(__file__),'helper_sha256':sha(Path(__file__).with_name('p41_CM8_diagonal_cancellation47.py'))}
    print('PASS all actual CM8 branch jets and true Hecke traces',save(args.output,out),flush=True)


if __name__=='__main__':
    main()
