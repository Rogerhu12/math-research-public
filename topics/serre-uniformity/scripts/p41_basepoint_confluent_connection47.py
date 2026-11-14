#!/usr/bin/env python3
"""Confluent actual C(x)=P(x)-b connection at the true CM(-3) base point."""
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
    for name in ['script-dir','cm-anchors','work-dir','output']:
        ap.add_argument('--'+name,type=Path,required=True)
    args=ap.parse_args();args.script_dir=args.script_dir.resolve();args.work_dir.mkdir(parents=True,exist_ok=True)
    sys.path.insert(0,str(args.script_dir))
    import numpy as np
    import p41_r2_matrix as r
    from p41_actual_differentials47 import ActualModel,save
    from p41_native_r2_linear47 import install
    from p41_projective_jet_frames47 import install_exact_float_mm,ProjectiveJetFrames
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

    anchors=load(args.cm_anchors)
    anchor=next(x for x in anchors['records'] if x['label']=='P_minus3')
    assert anchor['disk_id']=='SS_j0_10'
    assert anchor['actual_original_y_mod47cubed']==0
    assert all(x['canonical_local_sigma_height_mod47four']==0 for x in anchor['all53_local_height_anchors_by_global_reciprocity'])
    b=r.from_json([anchor['actual_W_in_original_SS_atlas_frame_mod47four']])
    frame=r.from_json(anchor['frame']);coordinate=r.from_json(anchor['coordinate'])
    assert r.equal(frame,a.fc) and r.equal(r.mm(b,frame),r.column([[1,0]]))
    J=ProjectiveJetFrames(a).local_jets(b,frame=frame,coordinate=coordinate,order=6)
    assert r.equal(J['W'][0],b)
    V2b,V3b=J['V2'][0],J['V3'][0]
    Hb=r.mm(V3b,a.H)
    assert r.equal(Hb,J['H'][0])
    original=standard('p41_second_kind_connection47.json.gz')
    snu=r.from_json(original['numerator_cubic_sections'])
    vnu=r.from_json(original['denominator_linear_section'])
    sn=[r.mm(x,snu) for x in J['V3'][:4]]
    vn=[r.mm(x,vnu) for x in J['W'][:4]]
    assert np.all(r.units(vn[0])), 'Original nu denominator must be treated exactly if nonunit'
    S4=Series(a,4)
    nu=S4.mul(sn,S4.inverse(S4.mul(S4.mul(vn,vn),J['Hc'][:4])))
    ghat=[a.scale(red(nu[k]),pow(k+1,-1,q),q) for k in range(4)]
    assert all(r.equal(r.conjugate(x,q),r.cols(x,original['pole_Frobenius_permutation_0based'])) for x in ghat)
    rng=random.Random(4104732801)
    Kb=kernel(b,1)
    Ktan=kernel(cat(J['W'][0],J['W'][1]),2)
    def rational_sample(K):
        xx=r.mm(K,r.column([[rng.randrange(47),rng.randrange(47)] for _ in range(K[0].shape[1])]))
        return r.add(xx,r.mm(M['A1'],r.conjugate(xx)))
    for attempt in range(100):
        ell=rational_sample(Kb)
        if np.all(r.units(r.mm(J['W'][1],ell))):break
    else:raise AssertionError('No unit tangent correction')
    assert r.iszero(r.mm(b,ell))
    bases=standard('p41_hecke3_abel_bases_checkpoint.json.gz')
    I2=[i-1 for i in bases['families'][1]['points_1based']]
    for attempt in range(100):
        q0=rational_sample(Ktan)
        if not np.all(r.units(r.mm(J['W'][2],q0))):continue
        qsource0=r.mm(M['W'],q0)
        good=np.flatnonzero(r.units(qsource0)[:,0]).tolist()
        if len(good)>378 and set(I2).issubset(good):break
    else:raise AssertionError('No exact double-zero denominator with unit calibration')
    assert r.iszero(r.mm(b,q0)) and r.iszero(r.mm(J['W'][1],q0))
    S6=Series(a,6)
    def moving_section(g0):
        # The common factor x is removed by an exact coefficient shift.
        assert r.iszero(r.mm(J['W'][0],g0)) and r.iszero(r.mm(J['W'][1],g0))
        values=[r.mm(w,g0) for w in J['W'][1:7]]
        ellvalues=[r.mm(w,ell) for w in J['W'][1:7]]
        assert r.iszero(values[0]) and np.all(r.units(ellvalues[0]))
        ratio=S6.mul(values,S6.inverse(ellvalues))
        assert r.iszero(ratio[0])
        out=[g0]+[r.neg(r.mul(ell,ratio[k])) for k in range(1,6)]
        for n in range(6):
            val=r.zeros(1,1)
            for k in range(n+1):val=r.add(val,r.mm(J['W'][k],out[n-k]))
            assert r.iszero(val) and r.iszero(r.mm(b,out[n]))
            assert r.equal(r.mm(M['A1'],r.conjugate(out[n])),out[n])
        return out
    qfull=moving_section(q0)
    qjets=[red(x) for x in qfull[:4]]
    qsource=[r.mm(red(M['W']),x,q) for x in qjets]
    E=red(r.rows(M['V2'],good))
    er,ec=r.rank_pivots(E)
    assert len(er)==199 and ec==list(range(199))
    Ei=r.inverse_matrix(r.rows(E,er),q)
    iq=sinv([r.rows(x,good) for x in qsource])
    colon=[[] for _ in range(4)];colon_tests=[]
    for attempt in range(8):
        gjets=moving_section(rational_sample(Ktan))[:4]
        gsource=[r.mm(red(r.rows(M['W'],good)),red(x),q) for x in gjets]
        ratios=smul(gsource,iq)
        for k in range(4):
            BB=r.mul(ratios[k],E,q)
            residual=r.sub(BB,r.mm(E,r.mm(Ei,r.rows(BB,er),q),q),q)
            colon[k].append(residual)
        colon_tests.append([r.to_json(x) for x in gjets])
        cr,cc=r.rank_pivots(cat(*colon[0]))
        assert len(cr)<=124,('confluent colon rank',len(cr))
        if len(cr)==124:break
    else:raise AssertionError('Confluent colon not saturated')
    colon=[cat(*x) for x in colon]
    print('PASS confluent moving colon rank124, faithful rows',len(good),'tests',len(colon_tests),flush=True)
    beta0=-3*pow(27652,-1,q)%q
    calA=a.scale(red(r.rows(M['V2'],I2)),beta0,q)
    calB=smul([r.rows(x,I2) for x in qsource],[tr(x) for x in ghat])
    HP=[red(x) for x in J['H'][:6]]
    rqfull=[red(x) for x in qfull]
    resP=mmconv(HP,rqfull,6)
    resb=[r.neg(r.mm(red(Hb),x,q),q) for x in rqfull]
    resdiff=[r.sub(x,y,q) for x,y in zip(resP,resb)]
    assert r.iszero(resdiff[0]) and r.iszero(resdiff[1])
    assert r.iszero(resb[0])
    a.field_setup()
    cusp_blocks=[]
    for index in [0,11]:
        CV2,_=a.cusp_evaluations(index)
        cusp_blocks.append(a.scale(red(CV2),41,q))
    A=[];B=[]
    for k in range(4):
        A.append(cat(colon[k],red(V2b) if k==0 else r.zeros(1,199),red(J['V2'][k+1]),
                     *[x if k==0 else r.zeros(*x[0].shape) for x in cusp_blocks],
                     calA if k==0 else r.zeros(54,199)))
        B.append(cat(r.zeros(colon[k][0].shape[0],1),resb[k+1],resdiff[k+2],
                     *[r.zeros(x[0].shape[0],1) for x in cusp_blocks],calB[k]))
    ar,ac=r.rank_pivots(A[0])
    assert len(ar)==199 and ac==list(range(199)),('confluent total rank',len(ar))
    Ai=r.inverse_matrix(r.rows(A[0],ar),q)
    shat=[]
    for n in range(4):
        wanted=B[n]
        for k in range(1,n+1):wanted=r.sub(wanted,r.mm(A[k],shat[n-k],q),q)
        snn=r.mm(Ai,r.rows(wanted,ar),q)
        assert r.equal(r.mm(A[0],snn,q),wanted),('confluent all equations',n)
        assert r.equal(r.mm(red(M['A2']),r.conjugate(snn,q),q),snn)
        shat.append(snn)
    sjets=[r.zeros(199,1)]+shat
    resP_original=mmconv([red(x) for x in J['V2'][:5]],sjets,5)
    assert all(r.equal(x,y) for x,y in zip(resP_original,resP[:5]))
    assert all(r.equal(r.mm(red(V2b),sjets[k],q),resb[k]) for k in range(5))
    print('PASS confluent connection',4*A[0][0].shape[0],'full equations, original residues, Frobenius',flush=True)
    cert={
      'result':'R328-confluent-connection-work','disk_id':'SS_j0_10','level':41,'auxiliary_prime':47,
      'actual_source_CM_anchor':anchor,'source_frame':r.to_json(frame),'source_coordinate':r.to_json(coordinate),
      'actual_source_projective_jets_0to6':{k:[r.to_json(x) for x in J[k]] for k in ['W','V2','V3','H','Hc','inverse_Hc']},
      'q_linear_coefficients_in_parameter_0to5_mod47four':[r.to_json(x) for x in qfull],
      's_div_x_quadratic_coefficients_0to3_mod47cubed':[r.to_json(x) for x in shat],
      's_quadratic_coefficients_0to4_mod47cubed':[r.to_json(x) for x in sjets],
      'gradient_div_x_original_nu_coefficients_0to3_mod47cubed':[r.to_json(x) for x in ghat],
      'original_nu_coefficients_0to3_mod47four':[r.to_json(x) for x in nu],
      'confluent_residue_at_b_div_x':[r.to_json(resb[k+1]) for k in range(4)],
      'confluent_divided_difference_residue_rhs':[r.to_json(resdiff[k+2]) for k in range(4)],
      'colon_test_sections_0to3_mod47four':colon_tests,'good_source_rows':good,
      'full_equation_rows':A[0][0].shape[0],'unit_minor_rows':ar,
      'confluent_poles_are_exact_symbolic_x_divisions':True,'q0_has_exact_order2_at_b':True,
      'all_four_coefficient_equations_verified':True,'original_two_residue_equations_verified':True,
      'Frobenius_verified':True,'complete_basepoint_F2_height':False,
      'input_sha256':dict(a.inputs,**inputs),'source_sha256':sha(__file__),
      'runtime_seconds':round(time.monotonic()-started,3)}
    print('PASS saved confluent connection',save(args.output,cert),flush=True)


if __name__=='__main__':main()

