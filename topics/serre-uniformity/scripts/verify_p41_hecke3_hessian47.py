#!/usr/bin/env python3
"""Independent actual meromorphic-function verification of the canonical T3 Hessian."""
import argparse,gzip,hashlib,json,sys
from pathlib import Path

def cubic_basis(W,dW,sources,M,C,r):
    """Independent325 cubic generators, normalized by a single original unit minor."""
    from p41_cm4_divisor47 import kernel
    divs=sources[1];ck=sources[3]
    K=r.from_json(kernel(73,divs['cusp_rank_columns_1based'],divs['cusp_free_columns_1based'],divs['canonical_kernel_block']))
    fc=r.mm(K,r.column(divs['canonical_coefficients']));f,df=r.mm(W,fc),r.mm(dW,fc)
    sq=[(a-1,b-1) for a,b in divs['square_basis_monomials_1based']];A=r.cols(W,[a for a,b in sq]);B=r.cols(W,[b for a,b in sq])
    dA=r.cols(dW,[a for a,b in sq]);dB=r.cols(dW,[b for a,b in sq]);V2C=r.from_json(divs['square_basis_inverse'])
    V2=r.mm(r.mul(A,B),V2C);dV2=r.mm(r.add(r.mul(dA,B),r.mul(A,dB)),V2C)
    pairs=[(a-1,b-1) for a,b in ck['cubic_selected_pairs_1based']];aa=[a for a,b in pairs];bb=[b for a,b in pairs]
    G=r.hcat(r.mul(f,V2),r.mul(r.cols(W,aa),r.cols(V2,bb)))
    dG=r.hcat(r.add(r.mul(df,V2),r.mul(f,dV2)),r.add(r.mul(r.cols(dW,aa),r.cols(V2,bb)),r.mul(r.cols(W,aa),r.cols(dV2,bb))))
    if C is None:C=r.inverse_matrix(r.rows(G,M['P3']))
    return r.mm(G,C),r.mm(dG,C),C

def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--script-dir',type=Path,required=True)
    parser.add_argument('--input',type=Path,default=Path('/tmp/p41_hecke3_hessian47_checkpoint.json.gz'))
    parser.add_argument('--hecke',type=Path,default=Path('/tmp/p41_hecke47_checkpoint.json.gz'))
    parser.add_argument('--jets',type=Path,default=Path('/tmp/p41_hecke3_jets47_checkpoint.json.gz'))
    parser.add_argument('--balancing',type=Path,default=Path('/tmp/p41_hecke_balancing47_certificate.json.gz'))
    parser.add_argument('--output',type=Path,default=Path('/tmp/p41_hecke3_hessian47_compact.json.gz'))
    args=parser.parse_args();folder=args.script_dir.resolve();sys.path.insert(0,str(folder))
    import numpy as np
    import p41_r2_matrix as r
    from p41_group_operations47 import load_sources,make_model
    from p41_cm4_divisor47 import kernel
    from p41_formal47_multiply import write_checkpoint
    from p41_poincare_norms47 import determinant
    sources,hashes=load_sources(folder/'data');M=make_model(sources)
    raw=args.input.read_bytes();data=json.loads(gzip.decompress(raw));assert data['source_sha256']==hashes
    hr=args.hecke.read_bytes();jr=args.jets.read_bytes();pr=args.balancing.read_bytes()
    h,j,p=[json.loads(gzip.decompress(b)) for b in (hr,jr,pr)]
    assert data['raw_hecke_sha256']==hashlib.sha256(hr).hexdigest() and data['hecke_jets_sha256']==hashlib.sha256(jr).hexdigest()
    op=h['operators']['3'];permutation=[x-1 for x in op['necklace_transport_1based']]
    targets=[r.rows(r.from_json(a['evaluation_matrix']),permutation) for a in op['targets']]
    dtargets=[r.rows(r.from_json(a['evaluation_derivatives']),permutation) for a in j['targets']]
    first_raw=(folder/'data/p41_evaluation_jets47_checkpoint.json.gz').read_bytes();dw=r.from_json(json.loads(gzip.decompress(first_raw))['evaluation_derivatives'])
    assert data['first_jets_sha256']==hashlib.sha256(first_raw).hexdigest()
    V3,dV3,C3=cubic_basis(M['W'],dw,sources,M,None,r);assert r.equal(V3,M['V3'])
    targetc=[cubic_basis(a,b,sources,M,C3,r)[:2] for a,b in zip(targets,dtargets)]
    divs=sources[1];K=r.from_json(kernel(73,divs['cusp_rank_columns_1based'],divs['cusp_free_columns_1based'],divs['canonical_kernel_block']))
    T=r.from_json(op['canonical_operator']);derivatives=[];Omegas=[];compact=[]
    for index,rec in enumerate(data['families']):
        points=[i-1 for i in rec['points_1based']];remaining=[i for i in range(820) if i not in set(points)]
        other=[i-1 for i in data['families'][1-index]['points_1based']]
        EV=(np.concatenate([r.rows(V3,points)[0]]+[r.rows(a,points)[0] for a,b in targetc]),np.concatenate([r.rows(V3,points)[1]]+[r.rows(a,points)[1] for a,b in targetc]))
        dEV=(np.concatenate([r.rows(dV3,points)[0]]+[r.rows(b,points)[0] for a,b in targetc]),np.concatenate([r.rows(dV3,points)[1]]+[r.rows(b,points)[1] for a,b in targetc]))
        rr,cc=r.rank_pivots(EV);assert len(rr)==270 and [i+1 for i in cc]==rec['pole_evaluation_rank_columns_1based']
        BS,free,block=r.kernel_from_rows(r.rows(EV,rr),rr,cc)
        assert r.to_json(block)==rec['pole_evaluation_kernel_block']
        b=r.from_json(rec['denominator_coefficients']);a=r.from_json(rec['numerator_coefficients'])
        assert r.iszero(r.mm(EV,b)) and r.equal(r.mm(BS,r.from_json(rec['denominator_small_coefficients'])),b)
        bvalues=r.mm(V3,b);bd=r.mm(dEV,b)
        assert np.all(r.units(r.rows(bvalues,remaining))) and np.all(r.units(bd))
        g=r.mm(BS,r.from_json(rec['auxiliary_small_coefficients']));gvalues=r.mm(V3,g)
        small_inverse=r.from_json(rec['restricted_V3_basis_inverse']);small=r.mm(r.rows(V3,remaining),small_inverse)
        piv=[i-1 for i in rec['restricted_V3_pivot_rows_1based']];assert r.equal(r.rows(small,piv),r.eye(325))
        ratio=r.mul(r.rows(gvalues,remaining),r.inverse_values(r.rows(bvalues,remaining)))
        scaled=r.mul(ratio,small);residual=r.sub(scaled,r.mm(small,r.rows(scaled,piv)))
        cr=[i-1 for i in rec['residual_rank_rows_1based']];ccol=[i-1 for i in rec['residual_rank_columns_1based']]
        r.inverse_matrix(r.cols(r.rows(residual,cr),ccol));assert len(cr)==108
        # Directly verify all54 numerators have no poles on the108-degree residual divisor.
        aval=r.rows(r.mm(V3,a),remaining);g_over_b_a=r.mul(ratio,aval)
        assert r.equal(g_over_b_a,r.mm(small,r.rows(g_over_b_a,piv)))
        Omega=tuple(x*(-3*pow(27652,-1,r.Q)%r.Q)%r.Q for x in r.mm(r.rows(M['W'],points),K));Omegas.append(Omega)
        TP=r.mm(r.mm(Omega,T),r.inverse_matrix(Omega));assert r.to_json(TP)==rec['T3_parameter_matrix']
        actual=r.mm(EV,a)
        expectedsource=r.mul(r.rows(bd,list(range(54))),(TP[0].T,TP[1].T))
        assert r.equal(r.rows(actual,list(range(54))),expectedsource)
        for k in range(4):
            indices=list(range(54*(k+1),54*(k+2)));v=r.rows(bd,indices)
            expected=(-np.eye(54,dtype=np.int64)*v[0]%r.Q,-np.eye(54,dtype=np.int64)*v[1]%r.Q)
            assert r.equal(r.rows(actual,indices),expected)
        normal=rec['normalization_point_1based']-1;assert r.iszero(r.mm(r.rows(V3,[normal]),a))
        perm=[points.index(M['tau'][x]) for x in points]
        assert r.equal(r.mm(M['A3'],r.conjugate(a)),r.cols(a,perm)) and r.equal(r.mm(M['A3'],r.conjugate(b)),b)
        aa,da=r.mm(r.rows(V3,other),a),r.mm(r.rows(dV3,other),a)
        bb,db=r.mm(r.rows(V3,other),b),r.mm(r.rows(dV3,other),b)
        iv=r.inverse_values(bb);div=r.neg(r.mul(db,r.mul(iv,iv)))
        deriv=r.add(r.mul(da,iv),r.mul(aa,div));derivatives.append(deriv)
        assert r.to_json(deriv)==rec['derivatives_at_other_chart']
        compact.append({'points_1based':rec['points_1based'],'abel_tangent_determinant':determinant(Omega),
                        'denominator_coefficients':rec['denominator_coefficients'],'normalization_point_1based':normal+1,
                        'actual_numerator_matrix_sha256':hashlib.sha256(json.dumps(rec['numerator_coefficients'],separators=(',',':')).encode()).hexdigest()})
        print('Chart',index+1,': independent cubic basis, all54 genuine principal functions, all270 principal parts and cross derivatives PASS.',flush=True)
    cp=r.sub(derivatives[1],(derivatives[0][0].T,derivatives[0][1].T));i1=r.inverse_matrix(Omegas[0]);i2=r.inverse_matrix(Omegas[1])
    C=r.mm(r.mm(i1,cp),(i2[0].T,i2[1].T));D=r.neg(C)
    assert r.to_json(C)==data['canonical_scalar_mixed_hessian'] and r.to_json(D)==data['T3_defect_matrix']
    TT=T[0].T,T[1].T;right=[];cur=D
    for k in range(54):right.append(cur);cur=r.mm(cur,TT)
    R=[np.array([a[k] for a in right],dtype=np.int64).reshape(54,-1) for k in range(2)]
    def apply(coeffs):
        coeffs=np.array(coeffs,dtype=np.int64)%r.Q;rows=[(coeffs@rr%r.Q).reshape(54,54,54) for rr in R];out=r.zeros(54,54)
        for k in range(53,-1,-1):out=r.add(r.mm(T,out),(rows[0][k],rows[1][k]))
        return out
    assert r.iszero(apply(p['separability_projector_coefficients_XY']))
    B=r.neg(apply(p['off_diagonal_inverse_coefficients_XY']));assert r.equal(r.sub(r.mm(T,B),r.mm(B,TT)),r.neg(D))
    out={'level':41,'auxiliary_prime':47,'precision':4,'source_sha256':hashes,
         'raw_hessian_sha256':hashlib.sha256(raw).hexdigest(),'raw_hecke_sha256':hashlib.sha256(hr).hexdigest(),
         'hecke_jets_sha256':hashlib.sha256(jr).hexdigest(),'balancing_sha256':hashlib.sha256(pr).hexdigest(),
         'families':compact,'canonical_scalar_mixed_hessian':r.to_json(C),'hecke_correction_matrix':r.to_json(B),
         'coordinate_convention':'row logarithms: log(c_T)_(1,1)=x C y^T; D_T=-C; correction=x B y^T',
         'generating_source_sha256':{name:hashlib.sha256(Path(__file__).with_name(name).read_bytes()).hexdigest() for name in ['p41_hecke3_jets47.gp','p41_hecke3_jets47.py','p41_hecke3_hessian47.py','verify_p41_hecke3_hessian47.py']},
         'status':'all108 actual principal functions independently verified; eD=0 and the actual integral Hecke correction PASS'}
    digest,size=write_checkpoint(args.output,out);print('Actual canonical Hecke Hessian: independent full verification PASS.',flush=True)
    print('Small final canonical Hessian/correction certificate',size,digest,flush=True)

if __name__=='__main__':main()
