#!/usr/bin/env python3
"""Verify exact local failures of ordinary norm candidates recorded by the probe."""
import argparse,hashlib,json,math,sys
from pathlib import Path
sys.set_int_max_str_digits(0)

def evalpoly(f,x,m):
    value=0
    for c in reversed(f):value=(value*x+c)%m
    return value

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument('z_source');ap.add_argument('theta_source');ap.add_argument('unit_source');ap.add_argument('certificate')
    args=ap.parse_args()
    rz=Path(args.z_source).read_bytes();rt=Path(args.theta_source).read_bytes()
    cert=json.loads(Path(args.certificate).read_text())
    assert hashlib.sha256(rz).hexdigest()==cert['source_z_sha256']
    assert hashlib.sha256(rt).hexdigest()==cert['source_theta_sha256']
    ru=Path(args.unit_source).read_bytes()
    assert hashlib.sha256(ru).hexdigest()==cert['source_unit_target_sha256']
    z=json.loads(rz);theta=json.loads(rt)
    f=list(map(int,z['factors'][0]['coefficients']))
    assert theta['coefficient_order']=='descending'
    P=list(map(int,theta['polynomial']))[::-1]
    assert len(P)==44 and P[-1]==1 and len(f)==45 and f[-1]==1
    derivative=[j*f[j] for j in range(1,45)]
    for row in cert['excluded_candidates']:
        a=row['a'];b=row['b'];l=row['prime'];r=row['z_residue'];rr=row['z_Hensel_mod_prime_squared']
        assert l>2 and all(l%d for d in range(2,math.isqrt(l)+1))
        assert l%4==3 and math.gcd(a,l)==1 and rr%l==r
        assert evalpoly(f,r,l)==0 and evalpoly(derivative,r,l)!=0
        assert evalpoly(f,rr,l*l)==0
        actual=pow(a,43,l*l)*evalpoly(P,(rr-b)*pow(a,-1,l*l)%(l*l),l*l)%(l*l)
        assert actual==row['norm_mod_prime_squared']
        assert actual!=0 and actual%l==0 and row['local_valuation']==1
    probe=cert['power_residue_probe'];l=probe['prime']
    assert l>2 and all(l%d for d in range(2,math.isqrt(l)+1))
    assert l%4==3 and (l*l-1)%43==0
    zero=(0,0);one=(1,0)
    def mul(a,b):return ((a[0]*b[0]-a[1]*b[1])%l,(a[0]*b[1]+a[1]*b[0])%l)
    def power(a,n):
        out=one
        while n:
            if n&1:out=mul(out,a)
            a=mul(a,a);n//=2
        return out
    def inverse(a):
        r=pow((a[0]*a[0]+a[1]*a[1])%l,-1,l)
        return (a[0]*r%l,-a[1]*r%l)
    def ev(poly,x):
        out=zero
        for c in reversed(poly):
            out=mul(out,x);out=((out[0]+c)%l,out[1])
        return out
    r=tuple(probe['z_residue'])
    assert ev(f,r)==zero and ev(derivative,r)!=zero
    target=json.loads(ru)['ordinary_real_norm_target_exact']
    u=mul(ev(list(map(int,target['numerators_ascending'])),r),
          (pow(int(target['common_denominator']),-1,l),0))
    assert u==tuple(probe['unit_target_residue']) and u!=zero
    seen=set()
    for row in probe['candidates']:
        a=row['a'];seen.add(a)
        n=mul((pow(a,43,l),0),ev(P,mul(r,(pow(a,-1,l),0))))
        assert n==tuple(row['norm_residue']) and n!=zero
        symbol=power(mul(u,inverse(n)),(l*l-1)//43)
        assert symbol==tuple(row['quotient_power_symbol']) and symbol!=one
        assert power(symbol,43)==one
    assert seen=={-3,-2,-1,1,2,3}
    print(json.dumps({'status':'PASS','exact_local_failures':len(cert['excluded_candidates']),
                      'exact_power_residue_failures':len(seen),
                      'actual_norm_preimage_computed':False,'actual_L_computed':False},separators=(',',':')))

if __name__=='__main__':main()
