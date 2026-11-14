#!/usr/bin/env python3
"""Verify every coefficient relation and summand of a saved R698 zero."""
import argparse
import gzip
import hashlib
import json
from math import isqrt
from pathlib import Path
import time
from flint import nmod_poly


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--certificate',type=Path,required=True)
    parser.add_argument('--output',type=Path,required=True)
    args=parser.parse_args()
    start=time.monotonic();raw=args.certificate.read_bytes()
    value=json.loads(gzip.decompress(raw) if args.certificate.suffix=='.gz' else raw)
    p=value['prime'];N=value['N']
    assert p>=41 and p%9 in (2,5) and all(p%d for d in range(2,isqrt(p)+1))
    assert 6*N+5==p
    coeff=value['coefficients'];c,z,h,t=[coeff[k] for k in ['C','Z','H','T']]
    for key,arr in coeff.items():
        assert len(arr)==N+1 and all(isinstance(a,int) and 0<=a<p for a in arr)
        digest=hashlib.sha256(json.dumps(arr,separators=(',',':')).encode()).hexdigest()
        assert digest==value['coefficient_sha256'][key]
    assert c[0]==z[0]==h[0]==t[0]==1
    for j in range(1,N+1):
        assert (2*j*c[j]-(2*j-1)*c[j-1])%p==0
        assert ((6*j+1)*z[j]-c[j])%p==0
        assert ((6*j-1)*h[j]-(6*j-4)*h[j-1])%p==0
    tp,hp,zp=[nmod_poly(a,p) for a in [t,h,z]]
    assert (tp.derivative().left_shift(1)-tp.mul_low(hp-1,N+1)).truncate(N+1).is_zero()
    z3=zp.mul_low(zp,N+1).mul_low(zp,N+1)
    terms_c=[t[j]*c[N-j]%p for j in range(N+1)]
    terms_z=[t[j]*int(z3[N-j])%p for j in range(N+1)]
    assert terms_c==value['TC_summands'] and terms_z==value['TZ3_summands']
    u,v=sum(terms_c)%p,sum(terms_z)%p
    ell2=pow(2,(p-1)//2,p);ap=-ell2*u%p;aq=2*pow(3,-1,p)*ell2*v%p
    for key,num in [('coefficient_TC',u),('coefficient_TZ3',v),('A_p',ap),('A_p_minus_3',aq),
                    ('C_p',-3*ap*ap%p),('C_p_minus_3',-3*aq*aq%p)]:
        assert value[key]==num
    assert v==0 and u!=0
    result={'result':'R698-full-zero-certificate-check','prime':p,'N':N,
            'prime_and_actual_congruence_checked':True,
            'all_c_z_h_relations_checked':N,'all_T_relations_checked':N,
            'each_TC_summand_checked':N+1,'each_TZ3_summand_checked':N+1,
            'coefficient_TC':u,'coefficient_TZ3':v,'A_p':ap,'A_p_minus_3':aq,
            'C_p':-3*ap*ap%p,'C_p_minus_3':-3*aq*aq%p,
            'certificate_sha256':hashlib.sha256(raw).hexdigest(),
            'checker_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
            'runtime_seconds':time.monotonic()-start,
            'M2_itself_proved_zero':False,'uniform_minimum_valuation_claim_refuted':True}
    args.output.write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result,indent=2))


if __name__=='__main__':main()
