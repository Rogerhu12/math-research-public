#!/usr/bin/env python3
"""Independently verify the actual canonical quotient via a companion matrix and integer norm."""
import argparse,gzip,hashlib,json,sys
from pathlib import Path

def main():
    p=argparse.ArgumentParser(description=__doc__);p.add_argument('--script-dir',type=Path,required=True)
    p.add_argument('--input',type=Path,default=Path('/tmp/p41_canonical_restriction47_raw.json.gz'))
    p.add_argument('--output',type=Path,default=Path('/tmp/p41_canonical_restriction47_independent.json'))
    args=p.parse_args();sys.path.insert(0,str(args.script_dir.resolve()))
    import numpy as np
    import p41_r2_matrix as r
    from p41_group_operations47 import load_sources,make_model
    from p41_cm4_divisor47 import kernel
    from p41_poincare_norms47 import quotient_from_record,determinant
    from flint import fmpz_mat
    raw=args.input.read_bytes();d=json.loads(gzip.decompress(raw));sources,hashes=load_sources(args.script_dir/'data')
    assert d['source_sha256']==hashes;M=make_model(sources);divs=sources[1]
    K=r.from_json(kernel(73,divs['cusp_rank_columns_1based'],divs['cusp_free_columns_1based'],divs['canonical_kernel_block']))
    fc=r.from_json(d['denominator_coefficients']);gc=r.mm(K,r.from_json(d['canonical_coefficients']))
    f,g=r.mm(M['W'],fc),r.mm(M['W'],gc)
    Kf=r.from_json(kernel(199,divs['K_rank_columns_1based'],divs['K_free_columns_1based'],divs['K_kernel_block']))
    vv=r.mul(r.mul(g,r.inverse_values(f)),r.mm(M['V2'],Kf));Kg=r.rows(vv,M['P2'])
    assert r.equal(r.mm(M['V2'],Kg),vv) and len(r.rank_pivots(Kg)[0])==93
    pairs=[(a-1,b-1) for a,b in d['ideal3_product_pairs_1based']]
    prod=r.mul(r.cols(M['W'],[a for a,b in pairs]),r.cols(vv,[b for a,b in pairs]));I3=r.rows(prod,M['P3'])
    assert r.equal(r.mm(M['V3'],I3),prod) and len(r.rank_pivots(I3)[0])==219
    Q2=quotient_from_record(d['quotient2']);Q3=quotient_from_record(d['quotient3'])
    assert r.iszero(r.mm(Q2,Kg)) and r.iszero(r.mm(Q3,I3))
    free2=[a-1 for a in d['quotient2']['free_rows_1based']]
    assert r.equal(r.cols(Q2,free2),r.eye(106))
    Phi1,Phi2,Phi3=[r.from_json(d['Phi'+str(i)]) for i in (1,2,3)]
    Ki=r.cols(Phi2,free2);Kr=r.inverse_matrix(Ki)
    assert r.equal(r.mm(Ki,Q2),Phi2)
    def quotient_multiplication(section):
        whole=r.mul(section,M['V2']);coords=r.rows(whole,M['P3'])
        assert r.equal(r.mm(M['V3'],coords),whole)
        assert r.iszero(r.mm(Q3,r.mm(coords,Kg)))
        return r.cols(r.mm(Q3,coords),free2)
    F=quotient_multiplication(f);Fi=r.inverse_matrix(F);df=determinant(F);assert df is not None
    assert r.equal(r.mm(r.mm(Ki,Fi),Q3),Phi3)
    u=r.mm(M['W'],r.from_json(d['primitive_generator_coefficients']));U=quotient_multiplication(u)
    companion=r.mm(r.mm(r.mm(Ki,Fi),U),Kr);H=d['minimal_polynomial_ascending'];expected=r.zeros(106,106)
    expected[0][1:,0:105]=np.eye(105,dtype=np.int64)
    expected[0][:,-1]=(-np.asarray(H[:-1],dtype=np.int64))%r.Q
    assert r.equal(companion,expected)
    for Phi,A in [(Phi1,M['A1']),(Phi2,M['A2']),(Phi3,M['A3'])]:
        assert r.equal(r.mm(Phi,A),r.conjugate(Phi)),'Actual rational finite algebra fails descent'
    pol=r.mm(Phi3,r.from_json(d['comparison_cubic_coefficients']));assert not np.any(pol[1])
    column=[int(x) for x in pol[0][:,0]];cols=[]
    for _ in range(106):
        cols.append(column[:]);top=column[-1]
        column=[(-top*H[0])%r.Q]+[(column[i-1]-top*H[i])%r.Q for i in range(1,106)]
    integer_matrix=[[cols[j][i] for j in range(106)] for i in range(106)]
    actual_norm=int(fmpz_mat(integer_matrix).det())%r.Q
    assert d['comparison_cubic_norm']==[actual_norm,0]
    out={'status':'PASS','source_sha256':hashes,'input_sha256':hashlib.sha256(raw).hexdigest(),
         'verifier_source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
         'canonical_candidate':d['canonical_candidate'],'ideal2_dimension':93,'ideal3_dimension':219,
         'denominator_unit_determinant':df,'companion_identification':True,'complete_Frobenius_descent':True,
         'independent_integer_determinant_norm':actual_norm,
         'method':'reconstruct actual quotient ideals; identify primitive multiplication with companion matrix; exact integer106x106 determinant, independent of resultant'}
    args.output.write_text(json.dumps(out,sort_keys=True,separators=(',',':'))+'\n')
    print('INDEPENDENT CANONICAL RESTRICTION PASS candidate',d['canonical_candidate'],'denominator det',df,
          'norm',actual_norm,'sha',hashlib.sha256(args.output.read_bytes()).hexdigest(),flush=True)

if __name__=='__main__':main()
