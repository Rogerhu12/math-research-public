#!/usr/bin/env python3
"""Actual CM7 differential and normalized F2 fibre coordinate from verified point jets."""
import argparse,gzip,hashlib,json,math,sys
from fractions import Fraction
from pathlib import Path

def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--script-dir',type=Path,required=True)
    parser.add_argument('--input',type=Path,default=Path('/tmp/p41_cm7_q2_support47_verified.json.gz'))
    parser.add_argument('--base-scales',type=Path,default=Path('/tmp/p41_cm12_scales47_certificate.json'))
    parser.add_argument('--output',type=Path,default=Path('/tmp/p41_cm7_global_fibre47_certificate.json'))
    args=parser.parse_args();folder=args.script_dir.resolve();sys.path.insert(0,str(folder))
    import p41_r2_matrix as r
    from p41_cm4_divisor47 import kernel
    from verify_p41_cm12_hecke47 import local_equation
    from p41_cm12_global_fibre47 import log47_unit
    paths=[args.input,args.base_scales,folder/'data/p41_cusp_divisors47_certificate.json.gz']
    raws=[p.read_bytes() for p in paths];S,base,C=[json.loads(gzip.decompress(b) if p.name.endswith('.gz') else b) for p,b in zip(paths,raws)]
    assert 'independent group-law' in S['status'] and S['CM_discriminant']==-7
    K=r.from_json(kernel(73,C['cusp_rank_columns_1based'],C['cusp_free_columns_1based'],C['canonical_kernel_block']))
    fc=r.mm(K,r.column(C['canonical_coefficients']))
    value=r.mm(r.from_json(S['weight2_evaluation_coefficients'][0]),fc)
    A,B=S['curve_A'],S['curve_B'];beta=Fraction(4*A**3+27*B**2,124416*A*A*B)
    assert beta==Fraction(-1,170100)
    a7=tuple(x*beta.numerator*pow(beta.denominator,-1,r.Q)%r.Q for x in value)
    assert r.to_json(a7)==[[[2865069,0]]] and r.units(a7)[0,0]
    ab=base['canonical_source_dj_value'][0][0];assert ab[1]==0
    rho=ab[0]*pow(int(a7[0][0,0]),-1,r.Q)%r.Q
    terms=local_equation()['Phi2_terms'];j=-3375
    diagonal=[0]*5
    for m,n,c in terms:
        for k in range(m+1):
            for l in range(n+1):diagonal[k+l]+=c*math.comb(m,k)*math.comb(n,l)*j**(m+n-k-l)
    vertical=[sum(c*math.comb(m,k)*j**(m+n-k) for m,n,c in terms if m>=k) for k in range(4)]
    assert diagonal==[0,0,-58046625,16478,-1] and vertical==[0,0,-16584750,1]
    eta=Fraction(diagonal[2],vertical[2]);assert eta==Fraction(7,2)
    eta_mod=eta.numerator*pow(eta.denominator,-1,r.Q)%r.Q
    scalar=pow(eta_mod,27,r.Q)*pow(-rho,4,r.Q)%r.Q;scalar800=pow(scalar,800,r.Q)
    assert (rho,scalar,scalar800)==(2314740,4622835,4776552)
    out={'level':41,'auxiliary_prime':47,'precision':4,'input_sha256':{p.name:hashlib.sha256(b).hexdigest() for p,b in zip(paths,raws)},
         'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
         'CM7_necklace_index_1based':S['fixed_necklace_indices_1based'][0],
         'CM7_canonical_weight2_value':r.to_json(value),'CM7_weight2_to_dj_scale':[beta.numerator,beta.denominator],
         'CM7_actual_canonical_dj_value':r.to_json(a7),'canonical_source_over_CM7_dj_value':rho,
         'T2_diagonal_polynomial_ascending':diagonal,'T2_vertical_polynomial_ascending':vertical,
         'T2_norm_factor_coordinate_rational':[eta.numerator,eta.denominator],
         'divisor_local_orders':{'b':4,'P_minus7':4},
         'norm_frame':'(j+3375)^(-4) tensor (j^(-4))^(-1), in Norm_(P_minus7-b) O(D_F(P_minus7)); fixed R110 canonical divisor',
         'global_sigma_F2_coordinate':scalar,'global_sigma_F2_coordinate_800th_power':scalar800,
         'log_of_coordinate_only':log47_unit(scalar,r.Q),'log_of_coordinate_only_800th_power':log47_unit(scalar800,r.Q),
         'status':'actual CM7 canonical differential and normalized global F2 section coordinates PASS; the norm-frame Poincare height remains separate'}
    data=json.dumps(out,sort_keys=True,indent=2).encode()+b'\n';args.output.write_bytes(data)
    print('ACTUAL CM7 NORMALIZED GLOBAL FIBRE PASS',len(data),hashlib.sha256(data).hexdigest())
if __name__=='__main__':main()

