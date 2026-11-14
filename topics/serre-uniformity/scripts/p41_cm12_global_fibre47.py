#!/usr/bin/env python3
"""Exact CM12 normalized global F2 section coordinates in the stated norm frame."""
import argparse,hashlib,json
from pathlib import Path

def log47_unit(u,q):
    t=(pow(u,46,q)-1)%q
    assert t%47==0
    return (t-t*t*pow(2,-1,q)+t*t*t*pow(3,-1,q))*pow(46,-1,q)%q

def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--input',type=Path,default=Path('/tmp/p41_cm12_scales47_certificate.json'))
    parser.add_argument('--output',type=Path,default=Path('/tmp/p41_cm12_global_fibre47_certificate.json'))
    args=parser.parse_args();raw=args.input.read_bytes();S=json.loads(raw)
    assert (S['level'],S['auxiliary_prime'],S['precision'])==(41,47,4)
    q=47**4
    ab=S['canonical_source_dj_value'][0][0]
    au=S['canonical_target_dj_value'][0][0]
    ratio=S['canonical_dj_value_ratio'][0][0]
    assert ab[1]==au[1]==ratio[1]==0 and ab[0]*pow(au[0],-1,q)%q==ratio[0]
    c=6549518250000
    assert c==118800**3//256
    degree_T=3+3-22;degree_diag=1+1+106
    assert degree_T==-16 and degree_diag==108 and 27*degree_T+4*degree_diag==0
    orders={'b':27+4,'u':27*3+4}
    scalar=pow(c,27,q)*pow(-ratio[0],4,q)%q
    scalar800=pow(scalar,800,q)
    assert (scalar,scalar800)==(3987767,4053094)
    ls=log47_unit(scalar,q);ls800=log47_unit(scalar800,q)
    assert ls800==800*ls%q
    out={'level':41,'auxiliary_prime':47,'precision':4,'modulus':q,
         'input_sha256':hashlib.sha256(raw).hexdigest(),
         'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
         'point':'u=P_minus12, b=P_minus3',
         'direction':{'T2':27,'identity':4},
         'degree_T2_norm_factor':degree_T,'degree_diagonal_norm_factor':degree_diag,
         'divisor_local_orders':orders,
         'source_parameter':'x=j at b','target_parameter':'w=j-54000 at u',
         'norm_frame':'w^(-85) tensor (x^(-31))^(-1) in Norm_(u-b) O(D_F(u)); K represented by the fixed R110 canonical differential',
         'T2_collision_unit_integer':c,'T2_collision_unit_mod47four':c%q,
         'diagonal_norm_factor_coordinate':(-ratio[0])%q,
         'global_sigma_F2_coordinate':scalar,'global_sigma_F2_coordinate_800th_power':scalar800,
         'log_of_coordinate_only':ls,'log_of_coordinate_only_800th_power':ls800,
         'status':'exact normalized global algebraic section coordinates in the specified local norm frame PASS; these logarithms are not the Poincare height of that frame'}
    data=json.dumps(out,sort_keys=True,indent=2).encode()+b'\n';args.output.write_bytes(data)
    print('CM12 ACTUAL GLOBAL F2 SECTION COORDINATE PASS',len(data),hashlib.sha256(data).hexdigest())
if __name__=='__main__':main()
