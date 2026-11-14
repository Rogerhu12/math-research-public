#!/usr/bin/env python3
"""Actual four T3 branches at the exact CM(-12) point, with full order-four jets."""
import argparse
import gzip
import hashlib
import json
from pathlib import Path
import sys
import time
from types import SimpleNamespace


def read(p):
    b=Path(p).read_bytes()
    return json.loads(gzip.decompress(b) if str(p).endswith('.gz') else b)


def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()


def main():
    ap=argparse.ArgumentParser(description=__doc__)
    for name in ['script-dir','support','basic-anchors','output']:
        ap.add_argument('--'+name,type=Path,required=True)
    args=ap.parse_args();scripts=args.script_dir.resolve();sys.path.insert(0,str(scripts))
    import numpy as np
    import p41_r2_matrix as r
    from p41_actual_differentials47 import ActualModel,save
    from p41_projective_jet_frames47 import ProjectiveJetFrames,install_exact_float_mm
    from p41_elliptic_coarse_atlas47 import Series,ClassicalInvariants
    install_exact_float_mm(r);started=time.monotonic();a=ActualModel(scripts);frames=ProjectiveJetFrames(a)
    Q=r.Q;N=5;S=Series(a,N);inputs={}
    def load(p):inputs[str(p)]=sha(p);return read(p)
    def standard(name):return load(scripts/'data'/name)
    support=load(args.support);anchors=load(args.basic_anchors)
    assert support['source_disk_id']=='SS_j44_02' and support['complete_actual_T3_support']
    assert support['actual_full73_Hecke_value_sum_verified']
    anchor=next(x for x in anchors['records'] if x['label']=='P_minus12')
    assert anchor['discriminant']==-12
    atlas=standard('p41_rational_SS_residue_atlas47_complete.json.gz')
    chart=next(x for x in atlas['charts'] if 'SS_j44_02' in x['disk_ids'])
    sourceframe=r.from_json(chart['frame']);sourcecoordinate=r.from_json(chart['coordinate'])
    WCM=r.from_json([anchor['actual_W_in_original_SS_atlas_frame_mod47four']])
    assert r.equal(r.mm(WCM,sourceframe),r.column([[1,0]]))
    Jsource=frames.local_jets(WCM,sourceframe,sourcecoordinate,order=4)
    assert len(Jsource['W'])==5
    derivative=standard('p41_cleared_serre_derivative47_complete.json.gz')
    invariants=ClassicalInvariants(SimpleNamespace(a=a,r=r,v=r.from_json(derivative['chosen_clearing_section']),G=r.from_json(derivative['cleared_derivative_coefficients'])))
    def const(x):
        first=r.column([x if isinstance(x,(list,tuple)) else [x%Q,0]])
        return [first]+[r.zeros(1,1) for _ in range(N-1)]
    def ellj(AA,BB):
        a3=S.power(AA,3);den=S.add(S.scale(a3,4),S.scale(S.power(BB,2),27))
        assert np.all(r.units(den[0]))
        return S.scale(S.mul(a3,S.inverse(den)),6912)
    def jmap(J,label):
        iv=invariants.series(J['W'])
        av3v3=S.mul(S.power(iv['Av'],3),S.power(iv['v'],3))
        den=S.add(S.scale(av3v3,4),S.scale(S.power(iv['Bv3'],2),27))
        assert np.all(r.units(den[0])),('clearing section not a unit',label)
        out=S.scale(S.mul(av3v3,S.inverse(den)),6912)
        assert np.all(r.units(out[1])),('ordinary j not etale',label)
        return out
    def evalseries(values,t):
        out=r.zeros(*values[0][0].shape)
        for value in reversed(values):out=r.add(r.mul(out,t),value)
        return out
    def centered(series):
        out=list(series);out[0]=r.zeros(*out[0][0].shape);return out
    def dumpjets(J):
        return {name:[r.to_json(x) for x in J[name]] for name in ['W','V2','V3','Hc','inverse_Hc']}
    A,Bcenter=support['source_curve'];ACM,BCM=support['source_curve']
    assert A==ACM and (BCM-Bcenter)%47==0
    assert r.equal(Jsource['W'][0],WCM)
    jsource=jmap(Jsource,'source_CM12')
    assert r.equal(jsource[0],const(anchor['j_integer'])[0])
    physicalB=const(BCM);physicalB[1]=const(1)[0]
    physicalj=ellj(const(A),physicalB)
    source_t=S.compose(S.reversion(centered(physicalj),N),centered(jsource))
    assert r.iszero(source_t[0])
    Bofx=S.add(const(BCM),source_t)
    assert all(r.equal(x,y) for x,y in zip(ellj(const(A),Bofx),jsource))
    records=[];horizontal=[]
    for branch in support['branch_records']:
        index=branch['branch_0based'];root=r.column([branch['kernel_root_in_R2']])
        for _ in range(2):
            root2=r.mul(root,root);root3=r.mul(root2,root);root4=r.mul(root2,root2)
            f=r.add(r.add(a.scale(root4,3),a.scale(root2,6*A)),r.sub(a.scale(root,12*BCM),const(A*A)[0]))
            df=r.add(r.add(a.scale(root3,12),a.scale(root,12*A)),const(12*BCM)[0])
            root=r.sub(root,r.mul(f,r.inverse_values(df)))
        r2=r.mul(root,root);r3=r.mul(r2,root)
        assert r.iszero(r.add(r.add(a.scale(r.mul(r2,r2),3),a.scale(r2,6*A)),r.sub(a.scale(root,12*BCM),const(A*A)[0])))
        targetA=r.sub(const(-9*A)[0],a.scale(r2,30))
        targetB=r.sub(r.sub(const(-27*BCM)[0],a.scale(root,42*A)),a.scale(r3,70))
        target_jcm=ellj([targetA]+const(0)[1:],[targetB]+const(0)[1:])[0]
        raw=r.from_json([branch['W_actual_values_in_R2']])
        basechart=next(frames.iter_charts(raw,order=4,max_points=1,label='CM12_T3_base_'+str(index)))
        frame,coordinate=basechart['frame'],basechart['coordinate']
        jbase=jmap(basechart,'initial_target_'+str(index))
        dj=r.sub(target_jcm,jbase[0]);assert all(not np.any(x%47) for x in dj)
        inverse_j=S.reversion(centered(jbase),N)
        displacement=evalseries(inverse_j,dj)
        assert all(not np.any(x%47) for x in displacement)
        assert r.equal(evalseries(jbase,displacement),target_jcm)
        targetCM=evalseries(basechart['W'],displacement)
        assert r.equal(r.mm(targetCM,frame),const(1)[0])
        is_horizontal=r.iszero(r.sub(target_jcm,jsource[0]))
        if is_horizontal:
            targetCM=r.mul(targetCM,r.inverse_values(r.mm(targetCM,sourceframe)))
            assert r.equal(targetCM,WCM),('j equal but actual level point unequal',index)
            frame,coordinate=sourceframe,sourcecoordinate
            horizontal.append(index)
        Jtarget=frames.local_jets(targetCM,frame,coordinate,order=4)
        jt=jmap(Jtarget,'CM_target_'+str(index));assert r.equal(jt[0],target_jcm)
        rootseries=[root]+const(0)[1:]
        for _ in range(3):
            r2s=S.power(rootseries,2);r3s=S.mul(r2s,rootseries);r4s=S.mul(r2s,r2s)
            f=S.sub(S.add(S.add(S.scale(r4s,3),S.scale(r2s,6*A)),S.scale(S.mul(Bofx,rootseries),12)),const(A*A))
            df=S.add(S.add(S.scale(r3s,12),S.scale(rootseries,12*A)),S.scale(Bofx,12))
            rootseries=S.sub(rootseries,S.mul(f,S.inverse(df)))
        r2s=S.power(rootseries,2);r3s=S.mul(r2s,rootseries);r4s=S.mul(r2s,r2s)
        f=S.sub(S.add(S.add(S.scale(r4s,3),S.scale(r2s,6*A)),S.scale(S.mul(Bofx,rootseries),12)),const(A*A))
        assert all(r.iszero(x) for x in f)
        Ats=S.sub(const(-9*A),S.scale(r2s,30))
        Bts=S.sub(S.sub(S.scale(Bofx,-27),S.scale(rootseries,42*A)),S.scale(r3s,70))
        jimage=ellj(Ats,Bts);assert r.equal(jimage[0],jt[0])
        target_parameter=S.compose(S.reversion(centered(jt),N),centered(jimage))
        assert np.all(r.units(target_parameter[1]))
        assert all(r.equal(x,y) for x,y in zip(S.compose(jt,target_parameter),jimage))
        Wimage=S.compose(Jtarget['W'],target_parameter)
        V2image=S.compose(Jtarget['V2'],target_parameter)
        V3image=S.compose(Jtarget['V3'],target_parameter)
        Himage=S.compose(Jtarget['Hc'],target_parameter)
        factor=Series(a,4).mul([a.scale(target_parameter[k+1],k+1) for k in range(4)],Series(a,4).inverse(Himage[:4]))
        records.append({'branch_0based':index,'horizontal_fixed_point':is_horizontal,
            'kernel_root_at_true_CM_mod47four':r.to_json(root),
            'kernel_root_coefficients_0to4_in_source_CM_x': [r.to_json(x) for x in rootseries],
            'all_kernel_coefficient_equations_verified':True,
            'initial_target_frame':r.to_json(basechart['frame']),'initial_target_coordinate':r.to_json(basechart['coordinate']),
            'initial_target_j_coefficients_0to4': [r.to_json(x) for x in jbase],
            'initial_target_to_true_CM_chart_displacement':r.to_json(displacement),
            'all73_actual_target_coordinates_at_true_CM':r.to_json(targetCM),
            'frame':r.to_json(frame),'coordinate':r.to_json(coordinate),
            'target_j_coefficients_0to4_in_its_chart':[r.to_json(x) for x in jt],
            'image_j_coefficients_0to4_in_source_CM_x':[r.to_json(x) for x in jimage],
            'target_parameter_coefficients_0to4_in_source_CM_x':[r.to_json(x) for x in target_parameter],
            'actual_image_W_coefficients_0to4':[r.to_json(x) for x in Wimage],
            'actual_image_V2_coefficients_0to4':[r.to_json(x) for x in V2image],
            'actual_image_V3_coefficients_0to4':[r.to_json(x) for x in V3image],
            'target_Hc_at_image_coefficients_0to4':[r.to_json(x) for x in Himage],
            'actual_differential_pullback_factor_coefficients_0to3':[r.to_json(x) for x in factor],
            'j_branch_reversion_and_composition_verified':True})
        print('PASS true CM12 T3 branch jets',index,'horizontal',is_horizontal,flush=True)
    assert len(horizontal)==1
    hr=[r.from_json(x['target_parameter_coefficients_0to4_in_source_CM_x'][1]) for x in records if x['horizontal_fixed_point']]
    assert r.equal(hr[0],const(-1)[0])
    fractions=[r.mul(h,r.inverse_values(r.sub(h,const(1)[0]))) for h in hr]
    assert r.equal(fractions[0],const(pow(2,-1,Q))[0])
    hecke=standard('p41_hecke47_full_saved.json.gz')['operators']['3']
    lhs=[r.zeros(1,73) for _ in range(4)]
    for record in records:
        Wimage=[r.from_json(x) for x in record['actual_image_W_coefficients_0to4'][:4]]
        factor=[r.from_json(x) for x in record['actual_differential_pullback_factor_coefficients_0to3']]
        values=Series(a,4).mul(Wimage,factor)
        lhs=[r.add(x,y) for x,y in zip(lhs,values)]
    source_values=Series(a,4).mul(Jsource['W'][:4],Jsource['inverse_Hc'][:4])
    rhs=[r.mm(x,r.from_json(hecke['weight2_operator'])) for x in source_values]
    assert all(r.equal(x,y) for x,y in zip(lhs,rhs)), 'Actual branch pullback full73 T3 normalization'
    canonical_left=[r.mm(x,a.K1) for x in lhs]
    canonical_right=[r.mm(r.mm(x,a.K1),r.from_json(hecke['canonical_operator'])) for x in source_values]
    assert all(r.equal(x,y) for x,y in zip(canonical_left,canonical_right))
    out={'result':'R324','level':41,'auxiliary_prime':47,'precision':4,'modulus':Q,
         'disk_id':'SS_j44_02','source_center_is_exact_CM_minus12':True,
         'source_CM_anchor':anchor,'source_frame':r.to_json(sourceframe),'source_coordinate':r.to_json(sourcecoordinate),
         'parameter':'x=z_R231-z_CM exactly; w=x/47=y_R231-y_CM',
         'source_CM_j_coefficients_0to4':[r.to_json(x) for x in jsource],
         'source_physical_B_displacement_coefficients_0to4_in_x':[r.to_json(x) for x in source_t],
         'source_projective_jets_0to4':dumpjets(Jsource),'branch_records':records,
         'horizontal_branch_indices_0based':horizontal,
         'unique_horizontal_derivative_exactly_minus_one':True,
         'unique_horizontal_residue_exactly_one_half':True,
         'full73_T3_pullback_trace_coefficients_0to3':[r.to_json(x) for x in lhs],
         'all4x73_T3_pullback_trace_coefficients_verified':True,
         'all4x54_canonical_T3_pullback_trace_coefficients_verified':True,
         'complete_actual_local_F3_height':False,
         'input_sha256':dict(a.inputs,**inputs),'source_sha256':sha(__file__),
         'runtime_seconds':round(time.monotonic()-started,3)}
    digest=save(args.output,out);print('PASS complete true CM12 four T3 local branches SHA',digest,flush=True)


if __name__=='__main__':main()
