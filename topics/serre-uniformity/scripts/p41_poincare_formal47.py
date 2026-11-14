#!/usr/bin/env python3
"""Actual rigidified inverse functions and double-inverse Poincare units.

The double-inverse unit is a genuine biextension operation.  Its logarithm
does not fix the free bilinear term of a local height splitting.
"""
import argparse,gzip,hashlib,json,random,sys
from pathlib import Path


def principal_inverse(Kplus,Kminus,v,other,M,r,rng):
    """Find a/v^2 with divisor E(P)+E(-P)-2 div(v), including multiplicity."""
    import numpy as np
    plus,minus=r.mm(M['V2'],Kplus),r.mm(M['V2'],Kminus)
    pairs=[(i,i) for i in range(73)]+[(i,(i+1)%73) for i in range(73)]
    while True:
        pairs += [(rng.randrange(73),rng.randrange(73)) for _ in range(100)]
        products=r.mul(r.cols(plus,[i for i,j in pairs]),r.cols(minus,[j for i,j in pairs]))
        rr,cc=r.rank_pivots(products)
        if len(rr)==199:break
        assert len(rr)<199 and len(pairs)<746
    U,piv,cols,Ui=r.normalize(products,199);selected=[pairs[i] for i in cols]
    other2=r.mul(other,other);scaled=r.mul(other2,M['V2'])
    residual=r.sub(scaled,r.mm(U,r.rows(scaled,piv)));kr,kc=r.rank_pivots(residual)
    assert len(kr)==198
    coeff,free,block=r.kernel_from_rows(r.rows(residual,kr),kr,kc)
    assert len(free)==1 and r.iszero(r.mm(residual,coeff))
    section=r.mm(M['V2'],coeff);v2=r.mul(v,v)
    good=[i for i in range(820) if M['tau'][i]==i and r.units(r.rows(v,[i]))[0,0] and r.units(r.rows(other,[i]))[0,0]]
    assert good;normal=good[0]
    factor=r.mul(r.rows(v2,[normal]),r.inverse_values(r.rows(section,[normal])))
    coeff=r.mul(coeff,factor);section=r.mm(M['V2'],coeff)
    assert r.equal(r.rows(section,[normal]),r.rows(v2,[normal]))
    assert r.equal(r.mm(M['A2'],r.conjugate(coeff)),coeff)
    # This full199-dimensional containment proves the complete scheme-theoretic sum.
    allproducts=r.mul(section,M['V2'])
    assert r.equal(allproducts,r.mm(U,r.rows(allproducts,piv)))
    assert all(np.all(x%47**2==0) for x in r.sub(section,v2))
    denominator=r.rows(v2,M['P2']);assert all(np.all(x%47**2==0) for x in r.sub(coeff,denominator))
    return coeff,{'product_pairs_1based':[[i+1,j+1] for i,j in selected],
                  'product_pivot_rows_1based':[i+1 for i in piv],
                  'product_basis_inverse':r.to_json(Ui),
                  'colon_rank_rows_1based':[i+1 for i in kr],
                  'colon_rank_columns_1based':[i+1 for i in kc],
                  'colon_free_column_1based':[i+1 for i in free],
                  'colon_kernel_block':r.to_json(block),
                  'normalization_point_1based':normal+1,
                  'numerator_coefficients':r.to_json(coeff),
                  'denominator_square_coefficients':r.to_json(denominator)}


def log_unit(pair,q):
    """Principal logarithm modulo47^4; actual input is1 modulo47^2."""
    assert pair[1]==0 and pair[0]%47**2==1
    return (pair[0]-1)%q


def formal_norm_data(K,v,basev,M,divs,r):
    """Restriction quotients with a product basis adapted to E mod47=div(basev)."""
    from p41_poincare_norms47 import quotient,determinant
    S=r.mm(M['V2'],K);desired=r.mul(basev,M['W'])
    rows,cols=r.rank_pivots(desired);assert len(rows)==73 and cols==list(range(73))
    change=r.mm(r.inverse_matrix(r.rows(S,rows)),r.rows(desired,rows));S=r.mm(S,change)
    assert all(__import__('numpy').array_equal(S[j]%47,desired[j]%47) for j in range(2))
    pairs=[(a-1,b-1) for a,b in divs['square_basis_monomials_1based']]
    products=r.mul(r.cols(M['W'],[a for a,b in pairs]),r.cols(S,[b for a,b in pairs]))
    rr,cc=r.rank_pivots(products);assert len(rr)==199 and cc==list(range(199))
    coords=r.rows(products,M['P3']);assert r.equal(r.mm(M['V3'],coords),products)
    Q2,rec2=quotient(K);Q3,rec3=quotient(coords)
    free2=[i-1 for i in rec2['free_rows_1based']]
    full=r.mul(v,M['V2']);c=r.rows(full,M['P3']);assert r.equal(r.mm(M['V3'],c),full)
    assert r.iszero(r.mm(Q3,r.mm(c,K)))
    induced=r.cols(r.mm(Q3,c),free2);det=determinant(induced);assert det is not None
    return {'product_pairs_1based':[[a+1,b+1] for a,b in pairs],
            'formal_basis_change':r.to_json(change),'product_coordinate_matrix':r.to_json(coords),
            'quotient2':rec2,'quotient3':rec3,'numerator_determinant':det,
            'denominator_determinant':det,'norm':[1,0]}


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--script-dir',type=Path,required=True)
    parser.add_argument('--bases',type=Path,default=Path('/tmp/p41_formal47_abel_bases_checkpoint.json.gz'))
    parser.add_argument('--jets',type=Path,default=Path('/tmp/p41_formal47_abel_jets_checkpoint.json.gz'))
    parser.add_argument('--exponential',type=Path,default=Path('/tmp/p41_formal47_exponential_checkpoint.json.gz'))
    parser.add_argument('--principal-only',action='store_true')
    parser.add_argument('--principal',type=Path,default=Path('/tmp/p41_poincare_formal47_principal.json.gz'))
    parser.add_argument('--output',type=Path,default=Path('/tmp/p41_poincare_formal47_checkpoint.json.gz'))
    args=parser.parse_args();folder=args.script_dir.resolve();sys.path.insert(0,str(folder));sys.path.insert(0,str(Path(__file__).parent))
    import p41_r2_matrix as r
    from p41_group_operations47 import load_sources,make_model
    from p41_formal47_multiply import write_checkpoint
    from p41_cm4_divisor47 import kernel
    from p41_formal47_exponential import construct_point
    from p41_poincare_norms47 import pair_mul,pair_inverse
    from p41_poincare_algebras47 import make_algebra,polynomial_norm,polycol
    sources,hashes=load_sources(folder/'data');M=make_model(sources)
    raws=[p.read_bytes() for p in (args.bases,args.jets,args.exponential)]
    base,jets,exp=[json.loads(gzip.decompress(raw)) for raw in raws]
    assert base['source_sha256']==exp['source_sha256']==hashes
    target=r.from_json(exp['exponentials'][0]['target_logarithm']);rng=random.Random(4104713601)
    plus=[r.from_json(x['point_coordinates']) for x in exp['exponentials']]
    vs=[r.mm(M['W'],r.from_json(item['v_coefficients'])) for item in base['families']]
    if args.principal.exists():
        principal=json.loads(gzip.decompress(args.principal.read_bytes()));assert principal['source_sha256']==hashes
        minus=[r.from_json(x['point_coordinates']) for x in principal['negative_exponentials']]
        coeffs=[r.from_json(x['numerator_coefficients']) for x in principal['inverse_functions']]
    else:
        minus=[];negative_records=[];coeffs=[];records=[]
        for j,item in enumerate(base['families']):
            point,A,record=construct_point(r.neg(target),item,jets,sources[1],M,r,kernel)
            minus.append(point);negative_records.append(record)
            coeff,record=principal_inverse(plus[j],minus[j],vs[j],vs[1-j],M,r,rng)
            coeffs.append(coeff);records.append(record)
            print('Actual inverse principal function family',j+1,'full199-dimensional product containment, descent, normalization and1mod47^2 PASS.',flush=True)
        principal={'level':41,'auxiliary_prime':47,'precision':4,'source_sha256':hashes,
                   'input_sha256':{p.name:hashlib.sha256(raw).hexdigest() for p,raw in zip((args.bases,args.jets,args.exponential),raws)},
                   'negative_exponentials':negative_records,'inverse_functions':records,
                   'status':'two actual normalized principal inverse functions; no chosen local height splitting'}
        digest,size=write_checkpoint(args.principal,principal);print('Principal functions',size,digest,flush=True)
    if args.principal_only:return
    D=[r.rows(r.mul(v,M['W']),M['P2']) for v in vs]
    cases=[('E2_plus',plus[1],vs[0],vs[1],coeffs[0]),('D2',D[1],vs[0],vs[1],coeffs[0]),
           ('E1_minus',minus[0],vs[1],vs[0],coeffs[1]),('D1',D[0],vs[1],vs[0],coeffs[1])]
    out={'level':41,'auxiliary_prime':47,'precision':4,'source_sha256':hashes,
         'principal_sha256':hashlib.sha256(args.principal.read_bytes()).hexdigest(),'norms':{},'algebras':{}}
    for label,K,v,basev,coeff in cases:
        rec=formal_norm_data(K,v,basev,M,sources[1],r)
        record,algebra=make_algebra(label,K,rec,M,sources,v,v,rng)
        numerator=polycol(r.mm(algebra[1],coeff),0)
        norm=polynomial_norm(numerator,algebra[3]);assert norm is not None and norm[1]==0 and norm[0]%47**2==1
        out['norms'][label]=norm
        out['algebras'][label]={'restriction':rec,'algebra':record,'numerator_residue_polynomial':list(map(list,zip(*[a.tolist() for a in numerator])))}
        print('Actual Poincare inverse-function norm',label,norm,'PASS.',flush=True)
        write_checkpoint(args.output,out)
    first=pair_mul(out['norms']['E2_plus'],pair_inverse(out['norms']['D2']))
    second=pair_mul(out['norms']['E1_minus'],pair_inverse(out['norms']['D1']))
    delta=pair_mul(first,pair_inverse(second));ld=log_unit(delta,r.Q)
    assert ld%47**3==0
    out['first_inverse_degree_zero_norm']=first;out['second_inverse_degree_zero_norm']=second
    out['double_inverse_unit']=delta;out['log_double_inverse_unit']=ld
    out['odd_total_degree_three_term']=ld*pow(2,-1,r.Q)%r.Q
    out['status']='actual doubly inverted Poincare frame; free quadratic bilinear local-height term is not chosen'
    digest,size=write_checkpoint(args.output,out)
    print('Actual double inverse',delta,'log',ld,'half',out['odd_total_degree_three_term'],flush=True)
    print('Saved actual Poincare formal data',size,digest,flush=True)

if __name__=='__main__':main()
