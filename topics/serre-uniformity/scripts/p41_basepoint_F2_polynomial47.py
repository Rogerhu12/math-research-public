#!/usr/bin/env python3
"""Actual basepoint F2 height from the confluent C connection and faithful global T2 trace."""
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
    for name in ['script-dir','confluent-connection','reference-connections','cm-anchors','work-dir','output']:
        ap.add_argument('--'+name,type=Path,required=True)
    args=ap.parse_args();args.script_dir=args.script_dir.resolve();args.work_dir.mkdir(parents=True,exist_ok=True)
    sys.path.insert(0,str(args.script_dir))
    import numpy as np
    import p41_r2_matrix as r
    from p41_actual_differentials47 import ActualModel,save
    from p41_native_r2_linear47 import install
    from p41_projective_jet_frames47 import install_exact_float_mm,ProjectiveJetFrames
    from p41_elliptic_coarse_atlas47 import Series,ClassicalInvariants
    from types import SimpleNamespace
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

    confluent=load(args.confluent_connection);reference=load(args.reference_connections);anchors=load(args.cm_anchors)
    assert confluent['all_four_coefficient_equations_verified']
    assert confluent['original_two_residue_equations_verified'] and confluent['confluent_poles_are_exact_symbolic_x_divisions']
    banchor=next(x for x in anchors['records'] if x['label']=='P_minus3')
    uanchor=next(x for x in anchors['records'] if x['label']=='P_minus12')
    assert confluent['actual_source_CM_anchor']==banchor
    J={k:[r.from_json(x) for x in v] for k,v in confluent['actual_source_projective_jets_0to6'].items()}
    qfull=[r.from_json(x) for x in confluent['q_linear_coefficients_in_parameter_0to5_mod47four']]
    shat=[r.from_json(x,q) for x in confluent['s_div_x_quadratic_coefficients_0to3_mod47cubed']]
    sjets=[r.from_json(x,q) for x in confluent['s_quadratic_coefficients_0to4_mod47cubed']]
    qjets=[red(x) for x in qfull]
    b=J['W'][0]
    assert r.equal(b,r.from_json([banchor['actual_W_in_original_SS_atlas_frame_mod47four']]))

    # A fourth-order zero at u clears every T2(eta_C/x) pole through order2.
    u=r.from_json([uanchor['actual_W_in_original_SS_atlas_frame_mod47four']])
    uf=r.from_json(uanchor['frame']);uc=r.from_json(uanchor['coordinate'])
    assert r.equal(uf,a.fc)
    UJ=ProjectiveJetFrames(a).local_jets(u,frame=uf,coordinate=uc,order=4)
    Ku=kernel(cat(*UJ['W'][:4]),4)
    rng=random.Random(4104732802)
    for attempt in range(100):
        xx=r.mm(Ku,r.column([[rng.randrange(47),rng.randrange(47)] for _ in range(Ku[0].shape[1])]))
        qT=r.add(xx,r.mm(M['A1'],r.conjugate(xx)))
        if np.all(r.units(r.mm(b,qT))) and np.all(r.units(r.mm(UJ['W'][4],qT))):break
    else:raise AssertionError('No fourth-order trace denominator')
    assert all(r.iszero(r.mm(w,qT)) for w in UJ['W'][:4])
    hecke=standard('p41_hecke47_full_saved.json.gz')['operators']['2']
    permutation=[i-1 for i in hecke['necklace_transport_1based']]
    totals=[r.zeros(820,1) for _ in range(3)];goodmask=np.ones(820,dtype=bool);target_counts=[]
    rawtrace=r.zeros(820,73)
    for target in hecke['targets']:
        Wfull=r.from_json(target['evaluation_matrix']);Wt=red(Wfull)
        rawtrace=r.add(rawtrace,r.rows(Wfull,permutation))
        V2t,_=a.evaluate(Wt)
        sv=[r.mm(red(V2t),x,q) for x in shat[:3]]
        qv=[r.mm(Wt,x,q) for x in qjets[:3]]
        hit=np.flatnonzero(r.units(qv[0])[:,0]).tolist()
        values=smul([r.rows(x,hit) for x in sv],sinv([r.rows(x,hit) for x in qv],3),3)
        for k in range(3):
            vv=r.zeros(820,1)
            for t in range(2):vv[t][hit]=values[k][t]
            totals[k]=r.add(totals[k],r.rows(vv,permutation),q)
        goodmask &= r.units(qv[0])[:,0][permutation]
        target_counts.append(len(hit))
    totals=[a.scale(x,pow(2,-1,q),q) for x in totals]
    # The saved operator normalization is checked against every full coordinate.
    T2=r.from_json(standard('p41_hecke47_compact.json.gz')['operators']['2']['weight2_operator'])
    assert r.equal(a.scale(rawtrace,pow(2,-1,Q)),r.mm(M['W'],T2))
    tgood=np.flatnonzero(goodmask).tolist();assert len(tgood)>504
    qTs=red(r.mm(M['W'],qT));qTcube=r.mul(r.mul(qTs,qTs,q),qTs,q)
    E4=r.zeros(820,0);pairs=[]
    for wi in range(73):
        block=r.mul(red(r.cols(M['W'],[wi])),red(M['V3']),q)
        joined=r.hcat(E4,block);rr,cc=r.rank_pivots(joined);assert len(rr)<=451
        proposed=pairs+[[wi,j] for j in range(325)]
        pairs=[proposed[j] for j in cc];E4=r.cols(joined,cc)
        if len(rr)==451:break
    else:raise AssertionError('Actual V4 rank')
    er4,ec4=r.rank_pivots(r.rows(E4,tgood));assert len(er4)==451 and ec4==list(range(451))
    selected4=[tgood[j] for j in er4];E4i=r.inverse_matrix(r.rows(E4,selected4),q)
    tcoeff=[]
    for k in range(3):
        values=r.mul(qTcube,totals[k],q)
        co=r.mm(E4i,r.rows(values,selected4),q)
        assert r.equal(r.mm(r.rows(E4,tgood),co,q),r.rows(values,tgood)),('actual confluent T2 V4',k)
        tcoeff.append(co)
    print('PASS actual confluent T2 trace',len(tgood),'rows x3, V4 rank451, exact operator',flush=True)
    V4P=[]
    for k in range(3):
        row4=r.zeros(1,451)
        for h in range(k+1):
            row4=r.add(row4,r.mul(r.cols(red(J['W'][h]),[p[0] for p in pairs]),r.cols(red(J['V3'][k-h]),[p[1] for p in pairs]),q),q)
        V4P.append(row4)
    tv=mmconv(V4P,tcoeff,3)
    qtP=[red(r.mm(w,qT)) for w in J['W'][:3]]
    assert np.all(r.units(qtP[0]))
    invhc=[red(x) for x in J['inverse_Hc']]
    t2hat=smul(smul(tv,sinv(spow(qtP,3,3),3),3),invhc[:3],3)
    t2diag=[r.zeros(1,1),t2hat[0],t2hat[1]]
    tracecert={'qT_linear_coefficients_mod47four':r.to_json(qT),
      'u_projective_jets_0to4':{k:[r.to_json(x) for x in UJ[k]] for k in ['W','V2','V3','Hc']},
      'qT_exact_order4_at_u_and_unit_at_b':True,'all820x73_operator_normalization_verified':True,
      'actual_T2_eta_div_x_coefficients_0to2_in_V4_mod47cubed':[r.to_json(x) for x in tcoeff],
      'V4_selected_W_V3_product_pairs_0based':pairs,'actual_T2_common_good_rows':tgood,
      'actual_T2_branch_good_counts':target_counts,'actual_T2_unit_interpolation_rows':selected4,
      'actual_T2_all_three_coefficient_equations':True,
      'actual_T2_eta_div_x_diagonal_coefficients_0to2':[r.to_json(x) for x in t2hat]}
    save(args.work_dir/'basepoint_actual_T2_trace47.json.gz',tracecert)

    # The diagonal regular part has residue -1 because b and P(x) coalesce.
    numerator_diag=mmconv([red(x) for x in J['V2'][:5]],sjets,5)
    numerator_partial=mmconv([a.scale(red(J['V2'][k+1]),k+1,q) for k in range(4)],sjets[:4],4)
    hp=[a.scale(red(J['Hc'][k+1]),k+1,q) for k in range(4)]
    Avalue=smul(numerator_diag,invhc[:5],5)
    Apartial=[r.sub(x,y,q) for x,y in zip(smul(numerator_partial,invhc[:4],4),smul(smul(numerator_diag[:4],hp,4),spow(invhc[:4],2,4),4))]
    qprime=mmconv([a.scale(red(J['W'][k+1]),k+1,q) for k in range(5)],qjets[:5],5)
    qsecond=mmconv([a.scale(red(J['W'][k+2]),(k+2)*(k+1),q) for k in range(4)],qjets[:4],4)
    assert all(r.equal(x,y) for x,y in zip(Avalue,qprime))
    assert r.iszero(qprime[0]) and np.all(r.units(qprime[1]))
    regular_laurent=smul([r.sub(x,a.scale(y,pow(2,-1,q),q),q) for x,y in zip(Apartial,qsecond)],sinv(qprime[1:5],4),4)
    assert r.equal(regular_laurent[0],scalar(-1))

    # Recover the coarse j-map by cancelling the exact common x^2.
    deriv=standard('p41_cleared_serre_derivative47_complete.json.gz')
    inv=ClassicalInvariants(SimpleNamespace(a=a,r=r,v=r.from_json(deriv['chosen_clearing_section']),G=r.from_json(deriv['cleared_derivative_coefficients'])))
    iv=inv.series(J['W']);S7=Series(a,7);S5=Series(a,5)
    avv=S7.mul(S7.power(iv['Av'],3),S7.power(iv['v'],3))
    denom=S7.add(S7.scale(avv,4),S7.scale(S7.power(iv['Bv3'],2),27))
    assert all(r.iszero(x) for x in avv[:3]) and all(r.iszero(x) for x in denom[:2])
    assert np.all(r.units(denom[2]))
    jfull=S5.scale(S5.mul(avv[2:7],S5.inverse(denom[2:7])),6912)
    j=[red(x) for x in jfull];assert r.iszero(j[0]) and np.all(r.units(j[1]))
    jp=[a.scale(j[k+1],k+1,q) for k in range(4)]
    jpp=[a.scale(j[k+2],(k+2)*(k+1),q) for k in range(3)]
    jratio=smul(jpp,sinv(jp[:3],3),3)
    pieces={'54_T2_eta_C':[r.zeros(1,1)]+[a.scale(x,54,q) for x in t2diag],
      '8_self_regular_j':[a.scale(regular_laurent[0],8,q)]+[r.sub(a.scale(regular_laurent[k+1],8,q),a.scale(jratio[k],4,q),q) for k in range(3)]}
    fixed_certs={}
    for name,weight,residue in [('u_minus_b',162,-1),('c7_minus_b',-54,-1),('Z8_minus20b',-27,-20),('D_minus20b',64*pow(3,-1,q),-20)]:
        f=reference['actual_connections'][name]
        ss=r.from_json(f['numerator_quadratic_coefficients_mod47cubed'],q)
        qq=r.from_json(f['denominator_linear_coefficients_mod47four'],q)
        sv=[r.mm(red(x),ss,q) for x in J['V2'][:4]]
        num=smul(sv,invhc[:4],4);den=[r.mm(red(x),qq,q) for x in J['W'][:5]]
        assert r.iszero(den[0]) and np.all(r.units(den[1])),('fixed simple pole denominator',name)
        val=smul(num,sinv(den[1:5],4),4)
        assert r.equal(val[0],scalar(residue)),('fixed residue',name,r.to_json(val[0]))
        pieces[name]=[a.scale(x,weight,q) for x in val]
        fixed_certs[name]={'numerator_0to3':[r.to_json(x) for x in num],'denominator_0to4':[r.to_json(x) for x in den],'Laurent_minus1_to2':[r.to_json(x) for x in val]}
    eta=standard('p41_eta_calibration47_complete.json.gz')
    sB=r.from_json(eta['numerator_coefficients'],q);qB=r.from_json(eta['denominator_coefficients'],q)
    Bnum=smul([r.mm(red(x),sB,q) for x in J['V3'][:4]],invhc[:4],4)
    Bden=[r.mm(red(x),qB,q) for x in J['V2'][:5]]
    assert np.all(r.units(Bden[0])), 'eta_B at b requires actual removable cancellation if nonunit'
    Bvalues=smul(Bnum[:3],sinv(Bden[:3],3),3)
    pieces['minus2_eta_B']=[r.zeros(1,1)]+[a.scale(x,-2,q) for x in Bvalues]
    dlogj=smul(jp,sinv(j[1:5],4),4);assert r.equal(dlogj[0],scalar(1))
    pieces['eight_thirds_dlog_j']=[a.scale(x,8*pow(3,-1,q),q) for x in dlogj]
    jm=list(j[:3]);jm[0]=r.sub(jm[0],scalar(1728),q)
    pieces['two_dlog_j_minus1728']=[r.zeros(1,1)]+[a.scale(x,2,q) for x in smul(jp[:3],sinv(jm,3),3)]
    total=[r.zeros(1,1) for _ in range(4)]
    for name,terms in pieces.items():
        print('Laurent residue',name,r.to_json(terms[0]),flush=True)
        total=[r.add(x,y,q) for x,y in zip(total,terms)]
    assert r.iszero(total[0]),('all basepoint poles must cancel',r.to_json(total[0]))
    differential=total[1:];assert all(not np.any(x[1]) for x in differential)
    height=[0]+[int(x[0][0,0])*47**(k+1)*pow(k+1,-1,Q)%Q for k,x in enumerate(differential)]
    globals=standard('p41_global_qc_polynomials47_complete.json.gz');idx=globals['direction_indices'].index(2)
    known=standard('p41_three_ordinary_CM_anchors_and_113_global_functions47.json.gz')
    glob=next(x for x in known['actual_113_rational_disk_global_polynomials'] if x['disk_id']=='SS_j0_10')
    globaly=next(x for x in glob['global_polynomials'] if x['n']==2)['coefficients_0to4_in_y_mod47four']
    qc=[(globaly[k]-800*(height[k] if k<4 else 0))%Q for k in range(5)]
    assert all(x%47==0 for x in qc) and qc[0]==0
    targets=[v['QC_defect_target_mod47four'][idx] for v in globals['component_vectors']];assert targets==[0,0,0,0]
    divided=[x//47 for x in qc];reduction=[x%47 for x in divided]
    roots=[t for t in range(47) if sum(c*pow(t,k,47) for k,c in enumerate(reduction))%47==0]
    lifts=[]
    for root in roots:
        derivative=sum(k*c*pow(root,k-1,47) for k,c in enumerate(divided) if k)%47
        if derivative==0:
            lifts.append({'residue_y_mod47':root,'derivative_mod47':0,'simple':False});continue
        y=root;mod=47;digits=[root]
        for _ in range(2):
            newmod=mod*47;value=sum(c*pow(y,k,newmod) for k,c in enumerate(divided))%newmod;assert value%mod==0
            digit=-(value//mod)*pow(derivative,-1,47)%47;y+=mod*digit;mod=newmod;digits.append(digit)
        assert sum(c*pow(y,k,Q) for k,c in enumerate(qc))%Q==0
        lifts.append({'y_mod47cubed':y,'z_mod47four':47*y,'y_base47_digits':digits,'derivative_mod47':derivative,'simple':True})
    out={'result':'R328-work','disk_id':'SS_j0_10','level':41,'auxiliary_prime':47,'precision':4,'modulus':Q,
      'complete_actual_local_sigma_F2_polynomial_on_disk':True,
      'canonical_local_sigma_F2_height_coefficients_0to3_in_y_mod47four':height,
      'local_differential_coefficients_0to2_in_x_mod47cubed':[r.to_json(x) for x in differential],
      'all_Laurent_pieces_minus1_to2_mod47cubed':{k:[r.to_json(x) for x in v] for k,v in pieces.items()},
      'actual_self_regular_Laurent_minus1_to2_mod47cubed':[r.to_json(x) for x in regular_laurent],
      'source_coarse_j_coefficients_0to4_mod47four':[r.to_json(x) for x in jfull],
      'fixed_connection_Laurent_certificates':fixed_certs,'actual_T2_trace':tracecert,
      'all_actual_Laurent_poles_cancel_exactly':True,'constant_zero_from_true_basepoint_reciprocity':True,
      'global_F2_coefficients_0to4_in_y_mod47four':globaly,'actual_QC_F2_coefficients_0to4_in_y_mod47four':qc,
      'F2_bad_targets':targets,'QC_div47_reduction':reduction,'residual_roots':roots,'lifted_root_records':lifts,
      'complete_all53_local_QC_heights':False,'complete_common_roots':False,
      'input_sha256':dict(a.inputs,**inputs),'source_sha256':sha(__file__),'runtime_seconds':round(time.monotonic()-started,3)}
    print('PASS actual basepoint F2',height,'global',globaly,'QC',qc,'reduction',reduction,'roots',lifts,flush=True)
    print('PASS saved basepoint F2',save(args.output,out),flush=True)


if __name__=='__main__':main()

