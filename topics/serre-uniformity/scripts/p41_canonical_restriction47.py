#!/usr/bin/env python3
"""Actual degree106 restriction algebra of a canonical divisor, with cubic-section norms."""
import argparse,gzip,hashlib,json,random,sys
from pathlib import Path

def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--script-dir',type=Path,required=True)
    parser.add_argument('--canonical-candidate',type=int,default=0)
    parser.add_argument('--raw-output',type=Path,default=Path('/tmp/p41_canonical_restriction47_raw.json.gz'))
    parser.add_argument('--compact-output',type=Path,default=Path('/tmp/p41_canonical_restriction47_compact.json.gz'))
    args=parser.parse_args();folder=args.script_dir.resolve();sys.path.insert(0,str(folder))
    import numpy as np
    import p41_r2_matrix as r
    from p41_cm4_divisor47 import kernel
    from p41_group_operations47 import load_sources,make_model,vector_json
    from p41_poincare_norms47 import quotient,determinant,pair_mul,pair_inverse
    from p41_poincare_algebras47 import polynomial_product,polycol,polynomial_norm
    from p41_formal47_multiply import write_checkpoint
    from flint import nmod_poly,fmpz_poly
    sources,hashes=load_sources(folder/'data');M=make_model(sources);divs=sources[1];d=106
    K1=r.from_json(kernel(73,divs['cusp_rank_columns_1based'],divs['cusp_free_columns_1based'],divs['canonical_kernel_block']))
    fc=r.mm(K1,r.column(divs['canonical_coefficients']));f=r.mm(M['W'],fc)
    gc=r.column(divs['second_canonical_coefficients']);seed_record=divs['second_canonical_trace_seed']
    if args.canonical_candidate:
        rg=random.Random(4104715400+args.canonical_candidate)
        seed,gc=r.rational_trace(r.from_json(divs['canonical_frobenius_matrix']),rg);seed_record=vector_json(seed)
    gcfull=r.mm(K1,gc);g=r.mm(M['W'],gcfull)
    assert r.equal(r.mm(M['A1'],r.conjugate(gcfull)),gcfull)
    KI=r.from_json(kernel(199,divs['K_rank_columns_1based'],divs['K_free_columns_1based'],divs['K_kernel_block']))
    values=r.mul(r.mul(g,r.inverse_values(f)),r.mm(M['V2'],KI));Kg=r.rows(values,M['P2'])
    assert r.equal(r.mm(M['V2'],Kg),values) and len(r.rank_pivots(Kg)[0])==93
    Q2,rec2=quotient(Kg);free2=[j-1 for j in rec2['free_rows_1based']]
    rng=random.Random(4104715410)
    pairs=[]
    while True:
        pairs += [(rng.randrange(73),rng.randrange(93)) for _ in range(100)]
        products=r.mul(r.cols(M['W'],[a for a,b in pairs]),r.cols(values,[b for a,b in pairs]))
        rr,cc=r.rank_pivots(products)
        if len(rr)==219:break
        assert len(rr)<219 and len(pairs)<800
    products=r.cols(products,cc);coords=r.rows(products,M['P3']);assert r.equal(r.mm(M['V3'],coords),products)
    Q3,rec3=quotient(coords)
    def mult(section):
        prod=r.mul(section,M['V2']);c=r.rows(prod,M['P3'])
        assert r.equal(r.mm(M['V3'],c),prod)
        return r.cols(r.mm(Q3,c),free2)
    Fv=mult(f);Fvi=r.inverse_matrix(Fv);den_det=determinant(Fv)
    assert den_det is not None
    one=r.mm(Q2,r.rows(r.mul(f,f),M['P2']))
    for attempt in range(1,101):
        seed,uc=r.rational_trace(M['A1'],rng);u=r.mm(M['W'],uc)
        Mu=r.mm(Fvi,mult(u));Krylov=r.zeros(d,d);current=one
        for j in range(d):
            Krylov[0][:,j],Krylov[1][:,j]=current[0][:,0],current[1][:,0]
            current=r.mm(Mu,current)
        if len(r.rank_pivots(Krylov)[0])==d:break
    else:raise RuntimeError('No actual monogenic canonical restriction generator')
    Ki=r.inverse_matrix(Krylov);coef=r.mm(Ki,current)
    relation=(np.concatenate((-coef[0][:,0]%r.Q,[1])),np.concatenate((-coef[1][:,0]%r.Q,[0])))
    assert not np.any(relation[1]),'The actual rational primitive generator must have a rational polynomial'
    Phi2=r.mm(Ki,Q2);Phi3=r.mm(r.mm(Ki,Fvi),Q3)
    fW=r.mul(f,M['W']);c=r.rows(fW,M['P2']);assert r.equal(r.mm(M['V2'],c),fW)
    Phi1=r.mm(Phi2,c)
    unit=r.zeros(d,1);unit[0][0,0]=1
    assert r.equal(r.mm(Phi1,fc),unit)
    sq=divs['square_basis_monomials_1based'];products=r.zeros(d,199)
    for j,(a,b) in enumerate(sq):
        v=polynomial_product(polycol(Phi1,a-1),polycol(Phi1,b-1),relation)
        products[0][:,j],products[1][:,j]=v
    assert r.equal(r.mm(products,r.from_json(divs['square_basis_inverse'])),Phi2)
    actual=r.mm(Phi3,r.rows(r.mul(f,M['V2']),M['P3']))
    assert r.equal(actual,Phi2)
    cpairs=sources[3]['cubic_selected_pairs_1based']
    actual=r.mm(Phi3,r.rows(r.mul(r.cols(M['W'],[a-1 for a,b in cpairs]),r.cols(M['V2'],[b-1 for a,b in cpairs])),M['P3']))
    for j,(a,b) in enumerate(cpairs):
        v=polynomial_product(polycol(Phi1,a-1),polycol(Phi2,b-1),relation)
        assert all(np.array_equal(v[k],actual[k][:,j]) for k in range(2))
    Hp=nmod_poly([int(x%47) for x in relation[0]],47)
    factors=Hp.factor()[1];factor_degrees=[(factor.degree(),int(exponent)) for factor,exponent in factors]
    etale=Hp.gcd(Hp.derivative()).degree()==0
    print('Actual canonical restriction degree106 complete; generator attempt',attempt,'factor degrees',factor_degrees,'etale',etale,flush=True)
    # Cross-check one full cubic norm by the real106-dimensional determinant and an integer resultant.
    HZ=fmpz_poly([int(x) for x in relation[0]])
    for tries in range(1,101):
        seed,cubic=r.rational_trace(M['A3'],rng);pol=r.mm(Phi3,cubic)
        assert not np.any(pol[1])
        val=polynomial_norm(polycol(pol,0),relation)
        if val is not None:break
    else:raise RuntimeError('No unit comparison cubic on the canonical divisor')
    exact=int(HZ.resultant(fmpz_poly([int(x) for x in pol[0][:,0]])))%r.Q
    assert val==[exact,0]
    enc=lambda A:hashlib.sha256(json.dumps(r.to_json(A),separators=(',',':')).encode()).hexdigest()
    result={'level':41,'auxiliary_prime':47,'precision':4,'degree':d,'source_sha256':hashes,
      'canonical_candidate':args.canonical_candidate,'canonical_trace_seed':seed_record,'canonical_coefficients':r.to_json(gc),
      'actual_ideal2_dimension':93,'actual_ideal3_dimension':219,'quotient2':rec2,'quotient3':rec3,
      'ideal3_product_pairs_1based':[[pairs[j][0]+1,pairs[j][1]+1] for j in cc],
      'denominator_coefficients':r.to_json(fc),'primitive_generator_coefficients':r.to_json(uc),
      'primitive_attempt':attempt,'krylov_unit_determinant':determinant(Krylov),
      'minimal_polynomial_ascending':[int(x) for x in relation[0]],
      'factor_degrees_mod47':factor_degrees,'etale_mod47':etale,
      'Phi1':r.to_json(Phi1),'Phi2':r.to_json(Phi2),'Phi3':r.to_json(Phi3),
      'Phi_sha256':{'1':enc(Phi1),'2':enc(Phi2),'3':enc(Phi3)},
      'comparison_cubic_coefficients':r.to_json(cubic),'comparison_cubic_norm':val,
      'generating_source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
      'status':'actual degree106 canonical restriction algebra; all199 quadratic and325 spanning cubic identities PASS; integer resultant norm agrees with actual determinant'}
    digest,size=write_checkpoint(args.raw_output,result)
    compact={k:v for k,v in result.items() if k not in ['quotient2','quotient3','Phi1','Phi2','Phi3']}
    compact['raw_rebuild_sha256']=digest
    digest2,size2=write_checkpoint(args.compact_output,compact)
    print('ACTUAL CANONICAL RESTRICTION PASS raw',size,digest,'compact',size2,digest2,flush=True)
if __name__=='__main__':main()

