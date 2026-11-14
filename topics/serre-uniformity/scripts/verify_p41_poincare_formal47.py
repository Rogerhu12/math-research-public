#!/usr/bin/env python3
"""Independent actual principal-divisor, restriction-algebra, and integer norm checks."""
import argparse,gzip,hashlib,json,sys
from pathlib import Path

def verify_principal(plus,minus,v,other,rec,M,r):
    import numpy as np
    a=r.mm(M['V2'],plus);b=r.mm(M['V2'],minus)
    pairs=[(i-1,j-1) for i,j in rec['product_pairs_1based']]
    products=r.mul(r.cols(a,[i for i,j in pairs]),r.cols(b,[j for i,j in pairs]))
    inv=r.from_json(rec['product_basis_inverse']);rows=[i-1 for i in rec['product_pivot_rows_1based']]
    assert r.equal(r.mm(r.rows(products,rows),inv),r.eye(199));U=r.mm(products,inv)
    scaled=r.mul(r.mul(other,other),M['V2']);residual=r.sub(scaled,r.mm(U,r.rows(scaled,rows)))
    rr=[i-1 for i in rec['colon_rank_rows_1based']];cc=[i-1 for i in rec['colon_rank_columns_1based']]
    r.inverse_matrix(r.cols(r.rows(residual,rr),cc));coeff=r.from_json(rec['numerator_coefficients'])
    assert r.iszero(r.mm(residual,coeff))
    section=r.mm(M['V2'],coeff);allproducts=r.mul(section,M['V2'])
    assert r.equal(allproducts,r.mm(U,r.rows(allproducts,rows)))
    v2=r.mul(v,v);normal=rec['normalization_point_1based']-1
    assert r.equal(r.rows(section,[normal]),r.rows(v2,[normal]))
    assert all(np.all(x%47**2==0) for x in r.sub(section,v2))
    assert r.equal(r.mm(M['A2'],r.conjugate(coeff)),coeff)
    return coeff


def verify_algebra(label,K,rec,alg,M,r):
    from p41_poincare_norms47 import quotient_from_record
    from verify_p41_poincare_algebras47 import integer_determinant,mul,inv
    Q2=quotient_from_record(rec['quotient2']);Q3=quotient_from_record(rec['quotient3'])
    S=r.mm(r.mm(M['V2'],K),r.from_json(rec['formal_basis_change']))
    pairs=rec['product_pairs_1based'];products=r.mul(r.cols(M['W'],[a-1 for a,b in pairs]),r.cols(S,[b-1 for a,b in pairs]))
    U=r.from_json(rec['product_coordinate_matrix']);assert r.equal(r.mm(M['V3'],U),products)
    for basis,Q,record in [(K,Q2,rec['quotient2']),(U,Q3,rec['quotient3'])]:
        pp=[i-1 for i in record['pivot_rows_1based']];iv=r.from_json(record['kernel_basis_inverse'])
        assert r.equal(r.mm(r.rows(basis,pp),iv),r.eye(len(pp))) and r.iszero(r.mm(Q,basis))
    free=[i-1 for i in rec['quotient2']['free_rows_1based']]
    def action(coeff):
        values=r.mul(r.mm(M['W'],r.column(coeff)),M['V2']);coordinates=r.rows(values,M['P3'])
        assert r.equal(r.mm(M['V3'],coordinates),values)
        return r.cols(r.mm(Q3,coordinates),free)
    Fv=action(alg['denominator_coefficients']);det=integer_determinant(r.to_json(Fv))
    assert list(det)==rec['denominator_determinant']==rec['numerator_determinant']
    assert rec['norm']==[1,0]
    Fvi=r.inverse_matrix(Fv);Mg=r.mm(Fvi,action(alg['generator_coefficients']))
    v=r.mm(M['W'],r.column(alg['denominator_coefficients']));current=r.mm(Q2,r.rows(r.mul(v,v),M['P2']))
    Krylov=r.zeros(126,126)
    for j in range(126):
        Krylov[0][:,j],Krylov[1][:,j]=current[0][:,0],current[1][:,0];current=r.mm(Mg,current)
    Ki=r.from_json(alg['krylov_inverse']);assert r.equal(r.mm(Ki,Krylov),r.eye(126))
    relation=alg['minimal_polynomial_ascending'];last=r.mm(Ki,current)
    assert relation[-1]==[1,0] and relation[:-1]==[[int(-last[0][i,0])%r.Q,int(-last[1][i,0])%r.Q] for i in range(126)]
    print(label,'full actual quotient, multiplicative primitive operator and unit Krylov basis PASS.',flush=True)
    return r.mm(Ki,Q2)


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--script-dir',type=Path,required=True)
    parser.add_argument('--input',type=Path,default=Path('/tmp/p41_poincare_formal47_checkpoint.json.gz'))
    parser.add_argument('--output',type=Path,default=Path('/tmp/p41_poincare_formal47_compact.json.gz'))
    args=parser.parse_args();folder=args.script_dir.resolve();sys.path.insert(0,str(folder))
    import p41_r2_matrix as r
    from p41_group_operations47 import load_sources,make_model
    from p41_formal47_multiply import write_checkpoint
    from verify_p41_poincare_algebras47 import polynomial_norm,mul,inv,sub
    sources,hashes=load_sources(folder/'data');M=make_model(sources)
    names=['p41_formal47_abel_bases_checkpoint.json.gz','p41_formal47_exponential_checkpoint.json.gz','p41_poincare_formal47_principal.json.gz']
    raws=[Path('/tmp',name).read_bytes() for name in names];base,exp,pr=[json.loads(gzip.decompress(raw)) for raw in raws]
    raw=args.input.read_bytes();data=json.loads(gzip.decompress(raw));assert data['source_sha256']==hashes
    assert data['principal_sha256']==hashlib.sha256(raws[2]).hexdigest()
    vs=[r.mm(M['W'],r.from_json(rec['v_coefficients'])) for rec in base['families']]
    plus=[r.from_json(item['point_coordinates']) for item in exp['exponentials']]
    minus=[r.from_json(item['point_coordinates']) for item in pr['negative_exponentials']]
    coeffs=[]
    for j in range(2):
        coeffs.append(verify_principal(plus[j],minus[j],vs[j],vs[1-j],pr['inverse_functions'][j],M,r))
        print('Actual principal inverse family',j+1,'independent full ideal and normalization PASS.',flush=True)
    D=[r.rows(r.mul(v,M['W']),M['P2']) for v in vs]
    cases=[('E2_plus',plus[1],coeffs[0]),('D2',D[1],coeffs[0]),('E1_minus',minus[0],coeffs[1]),('D1',D[0],coeffs[1])]
    compact={};norms={}
    for label,K,coeff in cases:
        rec=data['algebras'][label];Phi2=verify_algebra(label,K,rec['restriction'],rec['algebra'],M,r)
        value=r.mm(Phi2,coeff);poly=[[int(value[0][j,0]),int(value[1][j,0])] for j in range(126)]
        assert poly==rec['numerator_residue_polynomial']
        relation=rec['algebra']['minimal_polynomial_ascending'];norm=polynomial_norm(relation,poly)
        assert list(norm)==data['norms'][label];norms[label]=norm
        compact[label]={'minimal_polynomial_ascending':relation,'numerator_residue_polynomial':poly,'norm':list(norm)}
        print(label,'independent integer resultant norm',norm,'PASS.',flush=True)
    first=mul(norms['E2_plus'],inv(norms['D2']));second=mul(norms['E1_minus'],inv(norms['D1']))
    delta=mul(first,inv(second));assert list(delta)==data['double_inverse_unit']
    ld=sub(delta,(1,0));assert ld[1]==0 and ld[0]%47**3==0 and ld[0]==data['log_double_inverse_unit']
    out={'level':41,'auxiliary_prime':47,'precision':4,'source_sha256':hashes,
         'raw_sha256':hashlib.sha256(raw).hexdigest(),
         'input_sha256':{name:hashlib.sha256(b).hexdigest() for name,b in zip(names,raws)},
         'generating_source_sha256':{name:hashlib.sha256(Path(__file__).with_name(name).read_bytes()).hexdigest() for name in ['p41_poincare_formal47.py','verify_p41_poincare_formal47.py']},
         'principal_numerators':[rec['numerator_coefficients'] for rec in pr['inverse_functions']],
         'normalization_points_1based':[rec['normalization_point_1based'] for rec in pr['inverse_functions']],
         'restriction_algebras':compact,'first_inverse_degree_zero_norm':list(first),
         'second_inverse_degree_zero_norm':list(second),'double_inverse_unit':list(delta),
         'log_double_inverse_unit':ld[0],'odd_total_degree_three_term':data['odd_total_degree_three_term'],
         'status':'independent principal divisors, actual restriction algebras and integer resultant norms PASS; no bilinear height term chosen'}
    digest,size=write_checkpoint(args.output,out)
    print('Actual formal double inverse: independent full verification PASS.',flush=True)
    print('Small final certificate',size,digest,flush=True)

if __name__=='__main__':main()
