#!/usr/bin/env python3
"""Actual R698 roots by two scalar coefficients at N=(p-5)/6.

All series are truncated before the first denominator p.  This is an exact
finite computation and does not assert all-prime nonvanishing.
"""
import argparse,json,time
from pathlib import Path
from hashlib import sha256
from math import isqrt

def run(p):
    assert p>=41 and p%6==5 and all(p%d for d in range(2,isqrt(p)+1))
    start=time.monotonic();N=(p-5)//6
    c=[1];z=[1];h=[1];t=[1]
    for j in range(1,N+1):
        c.append(c[-1]*(2*j-1)*pow(2*j,-1,p)%p)
        z.append(c[-1]*pow(6*j+1,-1,p)%p)
        h.append(h[-1]*(6*j-4)*pow(6*j-1,-1,p)%p)
        t.append(sum(h[a]*t[j-a] for a in range(1,j+1))*pow(j,-1,p)%p)
    z2=[sum(z[a]*z[j-a] for a in range(j+1))%p for j in range(N+1)]
    z3=[sum(z2[a]*z[j-a] for a in range(j+1))%p for j in range(N+1)]
    terms_c=[t[j]*c[N-j]%p for j in range(N+1)]
    terms_z=[t[j]*z3[N-j]%p for j in range(N+1)]
    u=sum(terms_c)%p;v=sum(terms_z)%p;l2=pow(2,(p-1)//2,p)
    ap=-l2*u%p;aq=2*pow(3,-1,p)*l2*v%p
    return {'result':'R698','prime':p,'N':N,'legendre_2':l2,
            'coefficient_TC':u,'coefficient_TZ3':v,'A_p':ap,'A_p_minus_3':aq,
            'C_p':-3*ap*ap%p,'C_p_minus_3':-3*aq*aq%p,
            'C_coefficients':c,'Z_coefficients':z,'H_coefficients':h,'T_coefficients':t,
            'TC_summands':terms_c,'TZ3_summands':terms_z,
            'first_excluded_H_denominator':6*(N+1)-1,
            'division_by_p_used':False,'all_prime_unit_claimed':False,
            'runtime_seconds':time.monotonic()-start,
            'source_sha256':sha256(Path(__file__).read_bytes()).hexdigest()}

if __name__=='__main__':
    ap=argparse.ArgumentParser(description=__doc__);ap.add_argument('--prime',type=int,required=True)
    ap.add_argument('--output',type=Path,required=True);a=ap.parse_args();r=run(a.prime)
    a.output.write_text(json.dumps(r,indent=2)+'\n')
    print(json.dumps({k:r[k] for k in ['prime','N','coefficient_TC','coefficient_TZ3','A_p','A_p_minus_3','C_p','C_p_minus_3','runtime_seconds']}))
