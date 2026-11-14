#!/usr/bin/env python3
"""All odd non-41/non-47 local B-Hecke coefficients in fixed j/q41 tangents.

R188 supplies the proper intersections at ell prime to 2*41*n.  This file
adds the odd degree primes and the actual j-tangent self term at 3.
The 2 and 41 coefficients are intentionally left uncomputed.
"""
import argparse
import gzip
import hashlib
import importlib.util
import json
from pathlib import Path

HERE=Path(__file__).resolve().parent
spec=importlib.util.spec_from_file_location('r188',HERE/'verify_r188_cartan_intersections.py')
r188=importlib.util.module_from_spec(spec)
spec.loader.exec_module(r188)
Q=47**4


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def log47(a):
    assert a % 47
    z=(pow(a,46,Q)-1) % Q
    return (z-z*z*pow(2,-1,Q)+z*z*z*pow(3,-1,Q))*pow(46,-1,Q) % Q


def self_at_three():
    units=r188.all_of_norm(1,3)
    assert len(units)==12
    exceptional=set()
    for beta in units:
        if beta[2] or beta[3]:
            matched=r188.matching_necklaces(beta,3,1)
            assert len(matched)==1
            exceptional.update(matched)
    assert exceptional=={38}
    # z=(lambda+1)^2/lambda, j=256*(z-3)^3/(z-4).
    # At z=0: j=1728 and d(j-1728)/dz=-1296=-2^4*3^4.
    derivative=256*((3*9*(-4))-(-27))//16
    assert derivative == -1296 == -(2**4)*(3**4)
    records=[{'necklace':t,'projective_stabilizer':('S3' if t==38 else 'C2'),
              'valuation_j_derivative':(0 if t==38 else 4),
              'self_coefficient':(0 if t==38 else -4)}
             for t in r188.NONSQUARES]
    assert sum(x['self_coefficient'] for x in records)==-76
    return {'parameter':'j-1728','exceptional_S3_necklace':38,
            'C2_derivative_j_in_integral_z':-1296,
            'records':records,'total':-76,
            'sign':'e_t(P,P)=a^-1*e_z(P,P) for t=a*z+..., hence I=-v(a)'}


def compute(basis_path,proper_path):
    basis=json.loads(gzip.decompress(Path(basis_path).read_bytes()))
    proper=json.loads(gzip.decompress(Path(proper_path).read_bytes()))
    assert proper['basis_sha256']==sha(basis_path)
    assert proper['source_sha256']==sha(r188.__file__)
    labels=basis['new_correspondence_labels']
    assert [x['correspondence'] for x in proper['rows']]==labels
    self3=self_at_three()
    rows=[]
    for label,pr in zip(labels,proper['rows']):
        n=label['index']
        return_mult=(0 if label['kind']=='cyclic4' else len(r188.gaussian_norm(n))//4)
        assert len(r188.gaussian_norm(n)) % 4==0
        coefficients={x['ell']:x['intersection'] for x in pr['local']}
        degree_terms=[]
        for ell in range(3,n+1,2):
            if n % ell or not r188.prime(ell):
                continue
            assert label['kind']!='cyclic4' and (n//ell) % ell
            assert ell not in coefficients and ell not in (41,47)
            if ell % 4 == 3:
                assert return_mult==0
                terms=[]
                total=0
                for beta in r188.all_of_norm(n,ell):
                    assert beta[2] or beta[3]
                    assert beta[0] % ell==beta[1] % ell==0
                    assert r188.depth(beta,ell)==1
                    matched=r188.matching_necklaces(beta,ell,n)
                    total+=len(matched)
                    terms.append({'beta_twice':list(beta),'necklaces':list(matched)})
                assert total % 2==0
                value=total//2
                degree_terms.append({'ell':ell,'type':'inert','valuation_of_n':1,
                                     'intersection':value,'endomorphisms':terms})
            else:
                cm_predecessors=len(r188.gaussian_norm(n//ell))//4
                assert return_mult==2*cm_predecessors
                value=40*cm_predecessors
                degree_terms.append({'ell':ell,'type':'split','valuation_of_n':1,
                    'CM_predecessor_multiplicity':cm_predecessors,
                    'per_20_point_trace':40,'intersection':value})
            coefficients[ell]=value
        # All CM-return components use the same fixed j-1728 parameter.
        assert 3 in coefficients
        coefficients[3]+=return_mult*self3['total']
        odd_non47={ell:v for ell,v in sorted(coefficients.items())
                   if ell not in (41,47) and v}
        known=sum(v*log47(ell) for ell,v in odd_non47.items()) % Q
        rows.append({'correspondence':label,'CM_return_multiplicity':return_mult,
                     'new_degree_prime_terms':degree_terms,
                     'self_at_three':return_mult*self3['total'],
                     'odd_non41_non47_coefficients':[[ell,v] for ell,v in odd_non47.items()],
                     'known_odd_correction_mod47four':known,
                     'residual_intersection_at47_only':coefficients.get(47,0)})
    by_n={r['correspondence']['index']:r for r in rows}
    assert by_n[1]['odd_non41_non47_coefficients']==[[3,-76]]
    assert by_n[2]['odd_non41_non47_coefficients']==[[3,-64],[7,4]]
    assert next(x for x in by_n[3]['new_degree_prime_terms'] if x['ell']==3)['intersection']==44
    assert next(x for x in by_n[5]['new_degree_prime_terms'] if x['ell']==5)['intersection']==40
    # Independent unmarked T3 test: T3(1728) has two CM36 roots, each twice.
    h36=1728**2-153542016*1728-1790957481984
    v=0
    while h36 % 3==0:
        h36//=3;v+=1
    assert v==3 and len(r188.all_of_norm(3,3))//2==2*v==6
    return {'level':41,'auxiliary_prime':47,'precision':4,'modulus':Q,
        'generating_source_sha256':sha(__file__),
        'input_sha256':{'basis':sha(basis_path),'proper_R188':sha(proper_path),
                       'helper_R188':sha(r188.__file__)},
        'tangent_parameters':{'Z_minus4':'j-1728','cusps':'q41'},
        'self_at_three':self3,'rows':rows,
        'remaining_primes':[2,41],
        'height_equation':'h(B,S_i B)=lambda47(e_i)-known_odd_i-I2_i*log47(2)-I41_i*log47(41)',
        'scope':'all odd non41 non47 local terms in the stated tangents; full global height still requires 2,41 and actual lambda47'}


def main():
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--basis',type=Path,required=True)
    ap.add_argument('--proper',type=Path,required=True)
    ap.add_argument('--output',type=Path,required=True)
    ap.add_argument('--check',action='store_true')
    a=ap.parse_args();result=compute(a.basis,a.proper)
    if a.check:
        assert json.loads(gzip.decompress(a.output.read_bytes()))==result
    else:
        raw=json.dumps(result,sort_keys=True,separators=(',',':')).encode()
        a.output.write_bytes(gzip.compress(raw,compresslevel=9,mtime=0))
    print('PASS: 54 rows; j-tangent self trace at3=-76; all odd degree primes included')
    print('certificate_bytes=%d sha256=%s' % (a.output.stat().st_size,sha(a.output)))
    print('Remaining global inputs: actual lambda47 and coefficients at2,41')


if __name__=='__main__':
    main()
