#!/usr/bin/env python3
"""Exact 43rd-root extraction in F=Q(i,z), with a finite precision limit.

No class-group or unit-group package is used.  The default demonstration
extracts the root of (sigma(z))^43; that is NOT a norm preimage for R219.
An arbitrary supplied target is accepted only after an exact global identity.
"""
import argparse,hashlib,json,math,sys,time
from fractions import Fraction
from pathlib import Path
from verify_o6_single_real_norm_target import Field44,SIGMA_DENOMINATOR,SIGMA_NUMERATORS
sys.set_int_max_str_digits(0)


class ModField44:
    def __init__(self,f,m):
        self.f=f;self.m=m
        self.zero=[(0,0)]*44
        self.one=[(1,0)]+[(0,0)]*43
        self.z=[(0,0),(1,0)]+[(0,0)]*42
    def add(self,a,b):
        m=self.m
        return [((x+u)%m,(y+v)%m) for (x,y),(u,v) in zip(a,b)]
    def sub(self,a,b):
        m=self.m
        return [((x-u)%m,(y-v)%m) for (x,y),(u,v) in zip(a,b)]
    def scale(self,a,n):
        m=self.m
        return [(x*n%m,y*n%m) for x,y in a]
    def mul(self,a,b):
        m=self.m;out=[[0,0] for _ in range(87)]
        for j,(u,v) in enumerate(a):
            if u==v==0:continue
            for k,(x,y) in enumerate(b):
                if x==y==0:continue
                out[j+k][0]+=u*x-v*y;out[j+k][1]+=u*y+v*x
        for j in range(86,43,-1):
            u,v=out[j][0]%m,out[j][1]%m
            if u==v==0:continue
            for k,c in enumerate(self.f[:-1]):
                out[j-44+k][0]-=c*u;out[j-44+k][1]-=c*v
        return [(u%m,v%m) for u,v in out[:44]]
    def power(self,a,n):
        r=self.one
        while n:
            if n&1:r=self.mul(r,a)
            n//=2
            if n:a=self.mul(a,a)
        return r
    def reduce(self,a):return self.scale(a[:-1],pow(a[-1],-1,self.m))


def rational_reconstruct(a,m):
    bound=math.isqrt(m//2);r0,r1=m,a;t0,t1=0,1
    while abs(r1)>bound:
        q=r0//r1;r0,r1=r1,r0-q*r1;t0,t1=t1,t0-q*t1
    if not t1 or abs(t1)>bound or math.gcd(r1,t1)!=1:return None
    if t1<0:r1,t1=-r1,-t1
    assert (r1-a*t1)%m==0
    return Fraction(r1,t1)


def reconstruct(a,m,K):
    out=[];den=1
    for pair in a:
        row=[]
        for v in pair:
            frac=rational_reconstruct(v,m)
            if frac is None:return None
            den=math.lcm(den,frac.denominator);row.append(frac)
        out.append(row)
    nums=[(x.numerator*(den//x.denominator),y.numerator*(den//y.denominator)) for x,y in out]
    return K.normalize(nums,den)


def prime_candidates():
    for l in range(439,2000,4):
        if math.gcd(43,l*l-1)!=1:continue
        if all(l%d for d in range(2,math.isqrt(l)+1)):yield l


def extract(target,f,max_power=4096,progress=False):
    K=Field44(f);start=time.time();rejected=[]
    for l in prime_candidates():
        if target[-1]%l==0:continue
        R=ModField44(f,l);V=R.reduce(target);order=l*l-1
        # This proves that the residue algebra is a product of copies of F_l^2.
        if R.power(R.z,l*l)!=R.z:
            rejected.append({'prime':l,'reason':'residue_algebra_not_split'});continue
        e=pow(43,-1,order);b=R.power(V,e)
        inv=R.power(b,order-1)
        if R.mul(b,inv)!=R.one:
            rejected.append({'prime':l,'reason':'target_not_a_unit'});continue
        assert R.power(b,43)==V
        break
    else:raise RuntimeError('No good auxiliary prime in the configured finite list.')
    m=l;precision=1;levels=[]
    while True:
        candidate=reconstruct(b,m,K)
        valid=candidate is not None and K.power(candidate,43)==target
        levels.append({'power':precision,'modulus_bits':m.bit_length(),'global_identity':valid})
        if progress:print('root precision',precision,'bits',m.bit_length(),'global',valid,'seconds',round(time.time()-start,3),flush=True)
        if valid:return candidate,{'prime':l,'levels':levels,'rejected_primes':rejected}
        if precision>=max_power:return None,{'prime':l,'levels':levels,'rejected_primes':rejected}
        m*=m;precision*=2;R=ModField44(f,m);V=R.reduce(target)
        # Lift the inverse, then make one Newton root step.  The correction
        # is divisible by the old modulus, so its square vanishes modulo m.
        inv=R.mul(inv,R.sub(R.scale(R.one,2),R.mul(b,inv)))
        error=R.sub(R.mul(V,R.power(inv,43)),R.one)
        oldm=math.isqrt(m)
        assert all(v%oldm==0 for row in error for v in row)
        b=R.mul(b,R.add(R.one,R.scale(error,pow(43,-1,m))))
        inv=R.mul(inv,R.sub(R.scale(R.one,2),R.mul(b,inv)))
        assert R.mul(b,inv)==R.one and R.power(b,43)==V


def serial(a):
    return {'common_denominator':str(a[-1]),
            'Gaussian_numerators_ascending':[[str(x),str(y)] for x,y in a[:-1]]}


def main():
    ap=argparse.ArgumentParser();ap.add_argument('source')
    ap.add_argument('--target');ap.add_argument('--certificate');ap.add_argument('--check')
    ap.add_argument('--root-output');ap.add_argument('--max-power',type=int,default=4096);ap.add_argument('--progress',action='store_true')
    args=ap.parse_args();raw=Path(args.source).read_bytes();C=json.loads(raw)
    f=list(map(int,C['factors'][0]['coefficients']));K=Field44(f)
    sigma=tuple(SIGMA_NUMERATORS)+(SIGMA_DENOMINATOR,)
    if args.target:
        target_raw=Path(args.target).read_bytes();v=json.loads(target_raw)
        target=K.normalize([tuple(map(int,row)) for row in v['Gaussian_numerators_ascending']],int(v['common_denominator']))
    else:
        assert K.evaluate(f,sigma)==K.zero
        target=K.power(sigma,43)
        target_raw=json.dumps(serial(target),separators=(',',':')).encode()
    root,info=extract(target,f,args.max_power,args.progress)
    out={'status':'PASS' if root is not None else 'UNRESOLVED_AT_PRECISION_LIMIT',
         'source_sha256':hashlib.sha256(raw).hexdigest(),
         'target_sha256':hashlib.sha256(target_raw).hexdigest(),
         'demonstration_only':args.target is None,
         'exact_global_43rd_power_identity_verified':root is not None,
         'reconstruction':info,
         'actual_norm_preimage_computed':False,'actual_L_computed':False}
    if root is not None:
        root_json=serial(root)
        out['root_sha256']=hashlib.sha256(json.dumps(root_json,separators=(',',':')).encode()).hexdigest()
        if args.target is None:
            assert root==sigma;out['demonstration_root_is_labeled_sigma_z']=True
        if args.root_output:Path(args.root_output).write_text(json.dumps(root_json,separators=(',',':'))+'\n')
    if args.check:assert json.loads(Path(args.check).read_text())==out
    if args.certificate:Path(args.certificate).write_text(json.dumps(out,separators=(',',':'))+'\n')
    print(json.dumps(out,separators=(',',':')))


if __name__=='__main__':main()
