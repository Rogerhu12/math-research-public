#!/usr/bin/env python3
"""Actual eta_(Q-b) at either true CM8 point, calibrated by independent SS nu integrals."""
import argparse,gzip,hashlib,json,random,sys
from pathlib import Path

def read(p):
 p=Path(p);return json.loads(gzip.decompress(p.read_bytes()) if p.suffix=='.gz' else p.read_bytes())
def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()

def main():
    ap=argparse.ArgumentParser(description=__doc__)
    for k in ['script-dir','branches','fixed-reference','work-dir','output']:ap.add_argument('--'+k,type=Path,required=True)
    args=ap.parse_args();args.script_dir=args.script_dir.resolve();args.work_dir.mkdir(parents=True,exist_ok=True);sys.path.insert(0,str(args.script_dir))
    from p41_actual_differentials47 import ActualModel,save
    from p41_projective_jet_frames47 import ProjectiveJetFrames,install_exact_float_mm
    from p41_native_r2_linear47 import install
    from p41_elliptic_coarse_atlas47 import Series
    import p41_r2_matrix as r
    import numpy as np
    install_exact_float_mm(r);install(r,args.work_dir/'native');a=ActualModel(args.script_dir);M,Q,Q3=a.M,r.Q,47**3
    inputs={}
    def load(p):inputs[str(p)]=sha(p);return read(p)
    def standard(n):return load(args.script_dir/'data'/n)
    def cat(*xs):return tuple(np.concatenate([v[k] for v in xs],axis=0) for k in range(2))
    def transpose(v):return tuple(x.T.copy() for x in v)
    def kernel(x,rank):
        rr,cc=r.rank_pivots(x);assert len(rr)==rank
        K,_,_=r.kernel_from_rows(r.rows(x,rr),rr,cc);assert r.iszero(r.mm(x,K));return K
    branches=load(args.branches);reference=load(args.fixed_reference);disk=branches['disk_id']
    assert branches['all4x73_T2_pullback_trace_coefficients_verified'] and branches['exactly_one_true_full_level_horizontal_branch']
    WQ=r.from_json(branches['source_true_CM_W_fc_normalized'])
    J={k:[r.from_json(v) for v in values] for k,values in branches['source_true_CM_projective_jets_0to4'].items()}
    assert r.equal(J['W'][0],WQ)
    fixed_names=['u_minus_b','c7_minus_b','Z8_minus20b','D_minus20b']
    forms={};form_certificates={k:reference['actual_connections'][k] for k in fixed_names}
    gradients={k:r.from_json(reference['actual_gradients_original_nu_mod47cubed'][k],Q3) for k in fixed_names}
    b=r.rows(r.from_json(form_certificates['u_minus_b']['finite_pole_coordinates_fc_normalized']),[1])
    atlas=standard('p41_rational_SS_residue_atlas47_complete.json.gz');ch=next(x for x in atlas['charts'] if disk in x['disk_ids']);row=ch['disk_ids'].index(disk)
    ycm=branches['source_original_y_mod47cubed'];zcm=r.column([[47*ycm,0]])
    coordinate=r.from_json(ch['coordinate']);assert r.equal(coordinate,r.from_json(branches['source_coordinate']))
    WP=r.rows(r.from_json(ch['W_coefficients_0to3'][0]),[row]);assert r.equal(r.sub(r.mm(WQ,coordinate),r.mm(WP,coordinate)),zcm)
    recovered=r.zeros(1,73)
    for vals in reversed(ch['W_coefficients_0to3']):recovered=r.add(r.mul(recovered,zcm),r.rows(r.from_json(vals),[row]))
    assert r.equal(recovered,WQ)
    large=standard('p41_rational_SS_second_kind_integrals47_complete.json.gz');known=next(x for x in large['rational_SS_center_integrals'] if x['disk_id']==disk)
    gP=r.from_json([known['C_original_nu_coordinates_mod47cubed']],Q3)
    tiny=standard('p41_all129_second_kind_tiny47_complete.json.gz');tc=next(x for x in tiny['charts'] if disk in x['disk_ids']);ti=tc['disk_ids'].index(disk)
    assert tc['coordinate']==ch['coordinate'] and tc['frame']==ch['frame']
    delta=r.zeros(1,54);powz=r.column([[1,0]])
    for k,co in enumerate(tc['nu_coefficients_0to2_mod47four']):
        powz=r.mul(powz,zcm);delta=r.add(delta,a.scale(r.mul(r.rows(r.from_json(co),[ti]),powz),pow(k+1,-1,Q)))
    gradients['C_at_CM8']=r.add(gP,a.reduce(delta,Q3),Q3)
    old=standard('p41_second_kind_connection47.json.gz');moved=standard('p41_second_kind_move_poles47.json.gz')
    v=r.from_json(moved['old_pole_denominator_v']);w=r.from_json(moved['new_pole_denominator_w']);Nmu=r.from_json(moved['moved_form_cubic_numerators_rational_basis']);Fn=r.from_json(moved['moving_function_quadratic_numerators_rational_basis']);Ci=r.from_json(moved['rational_to_original_change'])
    S3,S4=Series(a,3),Series(a,4)
    vs=[r.mm(x,v) for x in J['W'][:4]];ws=[r.mm(x,w) for x in J['W'][:4]]
    assert np.all(r.units(vs[0])) and np.all(r.units(ws[0]))
    Fc=S4.mul([r.mm(x,Fn) for x in J['V2'][:4]],S4.inverse(S4.mul(vs,ws)))
    mu=S3.mul([r.mm(x,Nmu) for x in J['V3'][:3]],S3.mul(S3.inverse(S3.mul(ws[:3],ws[:3])),J['inverse_Hc'][:3]))
    nu=[r.mm(r.sub(mu[k],a.scale(Fc[k+1],k+1)),Ci) for k in range(3)]
    ov=[r.mm(x,r.from_json(old['denominator_linear_section'])) for x in J['W'][:3]]
    on=[r.mm(x,r.from_json(old['numerator_cubic_sections'])) for x in J['V3'][:3]]
    lhs=S3.mul(nu,S3.mul(S3.mul(ov,ov),J['Hc'][:3]));assert all(r.equal(x,y) for x,y in zip(lhs,on))
    assert all(r.equal(r.conjugate(x),r.cols(x,old['pole_Frobenius_permutation_0based'])) for x in nu)
    assert r.equal(r.conjugate(gradients['C_at_CM8'],Q3),r.cols(gradients['C_at_CM8'],old['pole_Frobenius_permutation_0based']))
    bases=standard('p41_hecke3_abel_bases_checkpoint.json.gz');I1,I2=[[i-1 for i in f['points_1based']] for f in bases['families']];beta0=-3*pow(27652,-1,Q)%Q
    a.field_setup();cusp_rows=[]
    for index in [0,11]:
        CV2,_=a.cusp_evaluations(index);CW=a.field_coordinates(a.cusp['cusp_values'][index]);cusp_rows.append((CW,CV2))
    rng=random.Random(4104736806)
    def construct(name, WZ, residues, cusp_residue):
        n = WZ[0].shape[0]
        assert len(residues) == n and sum(residues) + 20 * cusp_residue == 0
        assert r.equal(r.mm(WZ, a.fc), r.column([[1, 0] for _ in range(n)])), (name, "finite points must use the actual fc=1 frame")
        V2Z, V3Z = a.evaluate(WZ)
        HZ = r.mm(V3Z, a.H)
        K = kernel(WZ, n)
        for attempt in range(200):
            seed = r.column([[rng.randrange(47), rng.randrange(47)] for _ in range(73 - n)])
            x = r.mm(K, seed)
            q = r.add(x, r.mm(M["A1"], r.conjugate(x)))
            assert r.iszero(r.mm(WZ, q))
            dq = r.mm(HZ, q)
            qsource = r.mm(M["W"], q)
            good = np.flatnonzero(r.units(qsource)[:, 0]).tolist()
            if len(good) < 790 or not all(i in good for i in I1 + I2):
                continue
            if not np.all(r.units(dq)):
                continue
            if any(all(not np.any(y % 47) for y in r.mm(CW, q)) for CW, CV2 in cusp_rows):
                continue
            break
        else:
            raise AssertionError((name, "no denominator"))
        E = r.rows(M["V2"], good)
        er, ec = r.rank_pivots(E)
        assert len(er) == 199 and ec == list(range(199))
        Ei = r.inverse_matrix(r.rows(E, er))
        iq = r.inverse_values(r.rows(qsource, good))
        constraint = r.zeros(0, 199)
        tests = []
        for _ in range(6):
            seed = r.column([[rng.randrange(47), rng.randrange(47)] for _ in range(73 - n)])
            g = r.mm(K, seed)
            scaled = r.mul(r.mul(r.rows(r.mm(M["W"], g), good), iq), E)
            residual = r.sub(scaled, r.mm(E, r.mm(Ei, r.rows(scaled, er))))
            joined = cat(constraint, residual)
            rr, cc = r.rank_pivots(joined)
            assert len(rr) <= 126 - n
            constraint = r.rows(joined, rr)
            tests.append(g)
            if len(rr) == 126 - n:
                break
        else:
            raise AssertionError((name, "colon saturation"))
        S = kernel(constraint, 126 - n)
        assert S[0].shape == (199, 73 + n)
        for g in tests:
            values = r.mul(r.mul(r.rows(r.mm(M["W"], g), good), iq), r.mm(E, S))
            assert r.equal(values, r.mm(E, r.mm(Ei, r.rows(values, er))))
        blocks = [r.mm(V2Z, S)]
        wanted = [r.mul(dq, r.column([[x, 0] for x in residues]))]
        for CW, CV2 in cusp_rows:
            blocks.append(a.scale(r.mm(CV2, S), 41))
            wanted.append(a.scale(r.mm(CW, q), cusp_residue))
        blocks.append(a.scale(r.mm(r.rows(M["V2"], I2), S), beta0))
        wanted.append(r.mul(a.reduce(r.rows(qsource, I2), Q3), transpose(gradients[name]), Q3))
        A = a.reduce(cat(*blocks), Q3)
        B = cat(*[a.reduce(x, Q3) for x in wanted])
        ar, ac = r.rank_pivots(A)
        assert len(ar) == 73 + n and ac == list(range(73 + n)), (name, len(ar))
        co = r.mm(r.inverse_matrix(r.rows(A, ar), Q3), r.rows(B, ar), Q3)
        assert r.equal(r.mm(A, co, Q3), B)
        numerator = r.mm(a.reduce(S, Q3), co, Q3)
        assert r.equal(r.mm(a.reduce(M["A2"], Q3), r.conjugate(numerator, Q3), Q3), numerator)
        forms[name] = (numerator, q)
        form_certificates[name] = {
            "numerator_quadratic_coefficients_mod47cubed": r.to_json(numerator),
            "denominator_linear_coefficients_mod47four": r.to_json(q),
            "finite_pole_coordinates_fc_normalized": r.to_json(WZ),
            "finite_residues": residues,
            "cusp_residue": cusp_residue,
            "denominator_attempt_0based": attempt,
            "good_source_rows": len(good),
            "colon_rank": 126 - n,
            "candidate_dimension": 73 + n,
            "all_residue_and_actual_family2_calibration_equations": True,
            "calibration_gradient_original_nu_mod47cubed": r.to_json(gradients[name]),
            "Frobenius": True,
        }
        save(args.work_dir / (name + "_connection47.json.gz"), form_certificates[name])
        print("PASS actual connection", name, "rank", 73 + n, "good rows", len(good), flush=True)


    construct('C_at_CM8',cat(WQ,b),[1,-1],0)
    out={'result':'R368' if disk.endswith('06') else 'R370','disk_id':disk,
         'complete_actual_C_and_fixed_F2_connections_at_true_CM8':True,
         'actual_connections':form_certificates,
         'actual_gradients_original_nu_mod47cubed':{k:r.to_json(v) for k,v in gradients.items()},
         'actual_CM_nu_coefficients_0to2_mod47four':[r.to_json(x) for x in nu],
         'actual_original_center_C_nu_mod47cubed':r.to_json(gP),
         'actual_original_center_to_CM_nu_tiny_mod47four':r.to_json(delta),
         'actual_all73_CM_transport_from_original_atlas_verified':True,
         'CM_nu_moving_pole_formula_and_old_cross_identities_verified':True,
         'source_CM_original_y_mod47cubed':ycm,
         'complete_actual_local_height':False,'input_sha256':dict(a.inputs,**inputs),'source_sha256':sha(__file__)}
    print('PASS true CM8 C connection and all actual nu jets',save(args.output,out),flush=True)

if __name__=='__main__':main()
