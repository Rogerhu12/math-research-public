#!/usr/bin/env python3
"""Recover actual T3 transport functions and certify second-kind compatibility."""
import argparse,gzip,hashlib,json,random,sys,time
from pathlib import Path

def read(p):
    raw=Path(p).read_bytes()
    return json.loads(gzip.decompress(raw) if str(p).endswith('.gz') else raw)
def sha(p): return hashlib.sha256(Path(p).read_bytes()).hexdigest()

def main():
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--script-dir',type=Path,required=True)
    ap.add_argument('--native-dir',type=Path)
    ap.add_argument('--second-kind',type=Path,required=True)
    ap.add_argument('--work-dir',type=Path,required=True)
    ap.add_argument('--output',type=Path,required=True)
    args=ap.parse_args();args.work_dir.mkdir(parents=True,exist_ok=True)
    sys.path.insert(0,str(args.script_dir.resolve()))
    if args.native_dir:sys.path.insert(0,str(args.native_dir.resolve()))
    import numpy as np
    import p41_r2_matrix as r
    from p41_projective_jet_frames47 import install_exact_float_mm
    install_exact_float_mm(r)
    from p41_native_r2_linear47 import install
    native=install(r,args.work_dir/'native')
    from p41_actual_differentials47 import ActualModel,save,digest
    from p41_hecke3_hessian47 import section_jets,select_charts,solve_transport
    a=ActualModel(args.script_dir);M=a.M;q=r.Q;t0=time.monotonic()
    sources=[a.model,a.cusp,a.cm4,a.group]
    scale=a.scale
    def tr(x):return tuple(y.T.copy() for y in x)
    h=a.read('p41_hecke47_full_saved.json.gz');op=h['operators']['3']
    old=a.read('p41_hecke3_hessian47_compact.json.gz')
    deriv=a.read('p41_cleared_serre_derivative47_complete.json.gz')
    jets=a.read('p41_evaluation_jets47_checkpoint.json.gz')
    dw=r.from_json(jets['evaluation_derivatives'])
    V2,V3=section_jets([M['W'],dw],sources,M,r)
    assert r.equal(V2[0],M['V2']) and r.equal(V3[0],M['V3'])
    v0=r.from_json(deriv['chosen_clearing_section'])
    G0=r.from_json(deriv['cleared_derivative_coefficients'])
    K=r.from_json(deriv['elliptic_kernel_coefficients'])
    delta=r.add(scale(dw,-27652*pow(3,-1,q)),scale(M['W'],96))
    permutation=[i-1 for i in op['necklace_transport_1based']]
    targets=[r.rows(r.from_json(x['evaluation_matrix']),permutation) for x in op['targets']]
    families=select_charts(M,targets,a.K1,r)
    assert [[j+1 for j in I] for I in families]==[x['points_1based'] for x in old['families']]
    needed=sorted(set(families[0]+families[1]))
    targetd=[];coverage=[]
    beta=-3*pow(27652,-1,q)%q
    aa=-144*pow(27652,-1,q)%q
    rng=random.Random(242000041)
    for branch,(target,W) in enumerate(zip(op['targets'],targets)):
        vt=a.evaluate(W)[1]
        eligible=np.flatnonzero(np.any(r.units(W),axis=1)).tolist()
        assert set(needed)<=set(eligible)
        remaining=set(eligible);deltat=r.zeros(820,73);patches=[]
        for attempt in range(30):
            if attempt==0:v,G=v0,G0
            else:
                small=r.column([[rng.randrange(47),rng.randrange(47)] for _ in range(52)])
                tmp=r.mm(K,small);v=r.add(tmp,r.mm(M['A1'],r.conjugate(tmp)))
                values=r.mul(r.mm(M['W'],v),delta);G=r.rows(values,M['P3'])
                assert r.equal(r.mm(M['V3'],G),values)
            value=r.mm(W,v);unit=r.units(value)[:,0]
            I=[i for i in sorted(remaining) if unit[i]]
            if not I:continue
            dd=r.mul(r.mm(r.rows(vt,I),G),r.inverse_values(r.rows(value,I)))
            for k in range(2):deltat[k][I]=dd[k]
            patches.append({'rows_1based':[i+1 for i in I],
                            'v_coefficients':r.to_json(v),'G_sha256':digest(r.to_json(G))})
            remaining.difference_update(I)
            if not remaining:break
        assert not remaining
        u=r.column([[2*int(x)%q for x in target['kernel_x']]])
        at=r.add(r.column([[aa,0]]),scale(u,beta*pow(3,-1,q)))
        dW=r.sub(scale(deltat,beta*pow(3,-1,q)),r.mul(W,scale(at,2)))
        targetd.append(dW)
        coverage.append({'branch':branch,'regular_row_count':len(eligible),
                         'all108_transport_points_covered':True,'patches':patches,
                         'degree':3,'de_Rham_u':r.to_json(u),'target_GM_a':r.to_json(at)})
        print('Actual T3 first derivative branch',branch+1,'regular rows',len(eligible),flush=True)
    targetjets=[section_jets([W,D],sources,M,r)[1] for W,D in zip(targets,targetd)]
    tv=[x[0] for x in targetjets];td=[x[1] for x in targetjets]
    rng=random.Random(4104714101);records=[];ders=[];omegas=[]
    for i,I in enumerate(families):
        rec,dd,om=solve_transport(I,M['W'],V3[0],V3[1],tv,td,families[1-i],M,a.K1,
                                 r.from_json(op['canonical_operator']),r,rng)
        assert rec['denominator_coefficients']==old['families'][i]['denominator_coefficients']
        assert digest(rec['numerator_coefficients'])==old['families'][i]['actual_numerator_matrix_sha256']
        assert rec['normalization_point_1based']==old['families'][i]['normalization_point_1based']
        records.append(rec);ders.append(dd);omegas.append(om)
        save(args.work_dir/('family'+str(i+1)+'_transport.json.gz'),rec)
        print('Restored all54 original R141 numerators and denominator; exact original SHA matches, family',i+1,flush=True)
    Cparam=r.sub(ders[1],tr(ders[0]))
    C=r.mm(r.mm(r.inverse_matrix(omegas[0]),Cparam),tr(r.inverse_matrix(omegas[1])))
    assert r.equal(C,r.from_json(old['canonical_scalar_mixed_hessian']))
    nu=read(args.second_kind)
    assert nu['pole_indices_1based']==[i+1 for i in families[1]]
    sn=r.from_json(nu['numerator_cubic_sections']);vn=r.from_json(nu['denominator_linear_section'])
    rec=records[1];fn=r.from_json(rec['numerator_coefficients']);fd=r.from_json(rec['denominator_coefficients'])
    vals=r.mm(M['W'],vn);b0=r.mm(V3[0],fd);b1=r.mm(V3[1],fd)
    targetvals=[r.mm(W,vn) for W in targets]
    mask=r.units(vals)[:,0]&r.units(b0)[:,0]
    for vv in targetvals:mask&=r.units(vv)[:,0]
    I=np.flatnonzero(mask).tolist()
    source_nu=r.mul(scale(r.mm(r.rows(V3[0],I),sn),beta),r.inverse_values(r.mul(r.rows(vals,I),r.rows(vals,I))))
    lhs=r.zeros(len(I),54)
    for VV,vv in zip(tv,targetvals):
        part=r.mul(scale(r.mm(r.rows(VV,I),sn),beta*pow(3,-1,q)),r.inverse_values(r.mul(r.rows(vv,I),r.rows(vv,I))))
        lhs=r.add(lhs,part)
    av,ad=r.mm(r.rows(V3[0],I),fn),r.mm(r.rows(V3[1],I),fn)
    bb0,bb1=r.rows(b0,I),r.rows(b1,I)
    df=r.mul(r.sub(r.mul(ad,bb0),r.mul(av,bb1)),r.inverse_values(r.mul(bb0,bb0)))
    TP=r.from_json(rec['T3_parameter_matrix'])
    residual=r.sub(lhs,r.add(r.mm(source_nu,tr(TP)),df))
    assert r.iszero(residual),('second-kind T3 transport mismatch',len(I),int(np.count_nonzero(residual[0])+np.count_nonzero(residual[1])))
    assert len(I)>646,('insufficient faithful regular point evaluations',len(I))
    out={'result':'R242','level':41,'auxiliary_prime':47,'precision':4,'modulus':q,
         'complete_actual_T3_transport':True,'complete_second_kind_Hecke_identity':True,
         'complete_second_kind_large_integrals':False,'complete_local_QC_heights':False,
         'families':records,'recovered_original_numerator_SHA_checks':[True,True],
         'actual_target_first_derivative_coverage':coverage,
         'T3_second_kind_formula':'T3(nu_row)=nu_row*TP^transpose+d(f_row)',
         'identity_regular_point_indices_1based':[i+1 for i in I],
         'identity_checked_scalar_equations':len(I)*54,'identity_pole_degree_bound':540,
         'identity_line_bundle_degree_bound':646,'identity_residual_all_zero':True,
         'second_kind_SHA256':sha(args.second_kind),'input_sha256':a.inputs,
         'source_sha256':sha(__file__),'native':native,'runtime_seconds':round(time.monotonic()-t0,3)}
    outsha=save(args.output,out)
    print('PASS actual second-kind T3 transport, all54 functions and faithful equations',len(I)*54,outsha,flush=True)

if __name__=='__main__':main()
