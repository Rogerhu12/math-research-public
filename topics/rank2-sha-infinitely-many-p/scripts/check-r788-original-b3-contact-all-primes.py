#!/usr/bin/env python3
"""R788: all-prime b=3 contact gate, on the original five profiles.
Mathematics runs only in public Actions. No data files are written.
Stage I: exact rational maximal minors, a common-prime certificate.
Stage II: all remaining primes and all actual nineteen-angle classes.
"""
from fractions import Fraction as Q
from functools import lru_cache
import argparse, hashlib, itertools, json, math, sys
sys.set_int_max_str_digits(200000)

PROFILES=[
 ("1",0,0,0,1),
 ("t-1",0,1,0,0),
 ("(t-1)^2",0,2,0,0),
 ("h7",2,0,0,0),
 ("d^2",0,0,1,0)]

def primes_to(B):
    sieve=[True]*(B+1)
    sieve[0:2]=[False,False]
    for n in range(2,math.isqrt(B)+1):
        if sieve[n]:
            for k in range(n*n,B+1,n): sieve[k]=False
    return [n for n in range(2,B+1) if sieve[n]]

def ceildiv(a,b): return -((-a)//b)

def mul(a,b,cap):
    out=[Q(0)]*min(cap,len(a)+len(b)-1)
    for i,x in enumerate(a[:cap]):
        if x:
            for j,y in enumerate(b[:cap-i]):
                if y: out[i+j]+=x*y
    return out

def power(a,n,cap):
    if n<0: raise ValueError("Only paid polynomial exponents are used")
    z=[Q(1)]
    while n:
        if n&1: z=mul(z,a,cap)
        n//=2
        if n: a=mul(a,a,cap)
    return z

def exp_scale(logtheta,n,cap):
    out=[Q(1)]+[Q(0)]*(cap-1)
    for k in range(1,cap):
        out[k]=sum(Q(j*n)*logtheta[j]*out[k-j] for j in range(1,k+1))/k
    return out

def theta_powers(M):
    q=[Q(0)]*(M+1)
    q[1]=Q(-2,5)
    for j in range(2,M+1): q[j]=q[j-1]*Q(6*j-4,6*j-1)
    lt=[Q(0)]+[-q[j]/(3*j) for j in range(1,M+1)]
    out={n:exp_scale(lt,17*n,M+1) for n in range(1,4)}
    rho=mul([1,8],out[1],M+1)
    assert rho[0]==1 and rho[1]==Q(154,15)
    return out

def pad(v,cap): return v+[Q(0)]*(cap-len(v))

def det_bareiss(A):
    A=[r[:] for r in A];n=len(A)
    if n==0: return 1
    sign=1;prev=1
    for k in range(n-1):
        j=next((j for j in range(k,n) if A[j][k]),None)
        if j is None: return 0
        if j!=k: A[k],A[j]=A[j],A[k];sign=-sign
        pivot=A[k][k]
        for i in range(k+1,n):
            for j in range(k+1,n):
                val=A[i][j]*pivot-A[i][k]*A[k][j]
                quo,rem=divmod(val,prev)
                assert rem==0
                A[i][j]=quo
            A[i][k]=0
        prev=pivot
    return sign*A[-1][-1]

def strip_small(n,primes):
    n=abs(n);factors=[]
    if not n: return 0,factors
    for p in primes:
        e=0
        while n%p==0: n//=p;e+=1
        if e: factors.append([p,e])
    return n,factors

def row_integral(rows,small):
    out=[];denmax=0
    for row in rows:
        d=1
        for v in row: d=math.lcm(d,v.denominator)
        assert strip_small(d,small)[0]==1
        out.append([v.numerator*(d//v.denominator) for v in row])
        denmax=max(denmax,d.bit_length())
    return out,denmax

def field_rows(rows,p):
    out=[]
    for row in rows:
        rr=[]
        for x in row:
            assert x.denominator%p
            rr.append(x.numerator%p*pow(x.denominator,-1,p)%p)
        out.append(rr)
    return out

def solve_affine(rows,rhs,p,labels,values0):
    n=len(labels)
    A=[[(v%p) for v in row]+[b%p] for row,b in zip(rows,rhs)]
    r=0;piv=[]
    for c in range(n):
        z=next((i for i in range(r,len(A)) if A[i][c]),None)
        if z is None: continue
        A[r],A[z]=A[z],A[r]
        inv=pow(A[r][c],-1,p)
        A[r]=[v*inv%p for v in A[r]]
        for i in range(len(A)):
            if i!=r and A[i][c]:
                u=A[i][c]
                A[i]=[(x-u*y)%p for x,y in zip(A[i],A[r])]
        piv.append(c);r+=1
        if r==len(A): break
    consistent=all(any(row[:n]) or row[n]==0 for row in A)
    report={"rank":r,"augmented_rank":r+int(not consistent),
            "consistent":consistent}
    if not consistent: return report
    x=[0]*n
    for i,c in enumerate(piv): x[c]=A[i][n]
    free=[c for c in range(n) if c not in piv]
    def nonzero_possible(v):
        if sum(a*b for a,b in zip(v,x))%p: return True
        return any((v[f]-sum(v[c]*A[i][f] for i,c in enumerate(piv)))%p
                   for f in free)
    f3=[(values0[j]%p if lab==(3,0) else 0) for j,lab in enumerate(labels)]
    fy=[(lab[0]*values0[j]%p if lab[1]==0 else 0) for j,lab in enumerate(labels)]
    report.update({"affine_dimension":len(free),
                   "b0_three_possible":nonzero_possible(f3),
                   "smooth_possible":nonzero_possible(fy),
                   "rref_sha256":hashlib.sha256(json.dumps(A,separators=(",",":")).encode()).hexdigest()})
    return report

@lru_cache(None)
def partitions(total,length,ceiling=3):
    if length==0: return ((),) if total==0 else ()
    ans=[]
    for a in range(min(total,ceiling)+1):
        for z in partitions(total-a,length-1,a):
            ans.append((a,)+z)
    return tuple(ans)

def cumul(v):
    z=[];s=0
    for x in v: s+=x;z.append(s)
    return tuple(z)

def geometry_classes():
    out={}
    for name,mhmax,m1max,ddmax,dimax in PROFILES:
        for mh in range(mhmax+1):
          for m1 in range(m1max+1):
           for dd in range(ddmax+1):
            for di in range(dimax+1):
             if dd+di>1: continue
             for c in range((3+dd)//2+1):
              vd=2*c-dd
              if vd<0 or vd>3: continue
              for u in range(c,c+3):
               vi=2*(u-c)-di
               if vi<0 or vi>3: continue
               for mhv in partitions(3-mh,4):
                for m1v in partitions(3-m1,3):
                 for mdv in partitions(vd,2):
                  for miv in partitions(vi,2):
                   vh,v1,vdt,vin=map(cumul,(mhv,m1v,mdv,miv))
                   # f0=d^c must obey all the chosen center and infinity inequalities.
                   if any(j*c<v for j,v in enumerate(vdt,1)): continue
                   if any(j*(u-c)<v for j,v in enumerate(vin,1)): continue
                   kappa=36+6*u-2*sum(x*x for x in mhv)-sum(x*x for x in m1v+mdv+miv)
                   chi=9+2*mh+m1+dd+di
                   if kappa<chi-2 or (kappa-chi)%2: continue
                   specs=[]
                   for n in range(1,4):
                       bh=max([0]+[ceildiv(v-3+n,j) for j,v in enumerate(vh,1)])
                       ct=max([0]+[ceildiv(v-3+n,j) for j,v in enumerate(v1,1)])
                       zd=max([0]+[ceildiv(v-n,j) for j,v in enumerate(vdt,1)])
                       K=min([u+4*n]+[(j*u+(4*j+1)*n-v)//j for j,v in enumerate(vin,1)])
                       E=K-2*bh-ct-zd
                       specs.append((n,bh,ct,zd,E))
                   key=(c,u,mhv,m1v,mdv,miv)
                   out[key]={"c":c,"u":u,"mu_h":mhv,"mu_1":m1v,"mu_d":mdv,"mu_inf":miv,
                             "kappa":kappa,"chi":chi,"specs":specs}
    return list(out.values())

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("--max-order",type=int,default=48)
    args=ap.parse_args()
    M=args.max_order
    if not 36<=M<=72: raise ValueError("Bounded original b=3 certificate only")
    cap=M+1;bound=12*M+11;small=primes_to(bound)
    tp=theta_powers(M)

    @lru_cache(None)
    def base_series(n,bh,ct,dp,a=0):
        v=mul(mul(power([7,4,16],bh,cap),power([-1,1],ct,cap),cap),
              power([1,8],dp,cap),cap)
        v=mul(v,tp[n],cap)
        return tuple(pad(([Q(0)]*a+v)[:cap],cap))

    def matrix_from_specs(specs,normalized):
        cols=[];labels=[];v0=[]
        for n,bh,ct,z,E in specs:
            if E<0: continue
            # normalized: z is allowed pole, so rho^n contributes d^(n-z).
            # polynomial F: z is required zero, so rho^n contributes d^(n+z).
            v=list(base_series(n,bh,ct,n-z if normalized else n+z))
            for j in range(E+1):
                cols.append(pad(([Q(0)]*j+v)[:cap],cap))
                labels.append((n,j))
                v0.append(int(v[0]) if j==0 else 0)
        rows=[[col[i] for col in cols] for i in range(cap)]
        return rows,labels,v0

    profiles=[];uniform=True;finite_profiles={}
    for name,mh,m1,dd,di in PROFILES:
        specs=[]
        for n in range(1,4):
            a=n//4
            assert a==0
            bh=max(0,ceildiv(n-mh,4));ct=max(0,ceildiv(n-m1,3))
            z=(n+dd)//2;K=(9*n+di)//2
            E=K+z-a-2*bh-ct
            specs.append((n,bh,ct,z,E))
        rows,labels,v0=matrix_from_specs(specs,True)
        N=len(labels)
        assert N<M
        ints,denbits=row_integral(rows,small)
        g=0;minors=[]
        for first in range(1,M-N+2):
            inds=list(range(first,first+N))
            v=det_bareiss([ints[i] for i in inds])
            if not v: continue
            g=math.gcd(g,abs(v))
            remaining,factors=strip_small(g,small)
            minors.append({"rows":[0]+inds,"det_sha256":hashlib.sha256(str(v).encode()).hexdigest(),
                           "det_bits":abs(v).bit_length()})
            print("R788 profile=%s first=%s surviving_bits=%s"%(name,first,remaining.bit_length()),
                  file=sys.stderr,flush=True)
            if remaining==1: break
        remaining,factors=strip_small(g,small)
        paid=remaining==1
        uniform=uniform and paid
        profiles.append({"mask":name,"columns_without_constant":N,"specs":specs,
                         "minor_count":len(minors),"max_row":max((max(x["rows"]) for x in minors),default=None),
                         "minors":minors,"common_gcd":str(g),"gcd_factorization_below_cutoff":factors,
                         "surviving_large_part":str(remaining),"uniform_gate_paid":paid,
                         "row_denominator_max_bits":denbits})
        for p in small:
            if p<=101 or p%12!=11: continue
            h=(p-11)//12
            if h<21: continue
            rr=field_rows(rows[:h],p)
            report=solve_affine(rr,[-1]+[0]*(h-1),p,labels,v0)
            finite_profiles.setdefault(p,[]).append({"mask":name,**report})

    classes=geometry_classes()
    cache={};finite=[];remaining_candidates=[]
    for p,pr in sorted(finite_profiles.items()):
        h=(p-11)//12
        eligible=[c for c in classes if c["kappa"]+14<=h]
        checked=0;consistent=0;possible=0;relevant=[]
        for c in eligible:
            key=(p,c["c"],tuple(c["specs"]))
            if key not in cache:
                rows,labels,v0=matrix_from_specs(c["specs"],False)
                rr=field_rows(rows[:h],p)
                target=pad(power([1,8],c["c"],h),h)
                rhs=[-int(x)%p for x in target]
                cache[key]=solve_affine(rr,rhs,p,labels,v0)
            report=cache[key];checked+=1
            if report["consistent"]:
                consistent+=1
                if report["b0_three_possible"] and report["smooth_possible"]:
                    possible+=1
                    relevant.append({**c,**report})
        finite.append({"prime":p,"h":h,"profiles":pr,"eligible_geometry_classes":checked,
                       "consistent_geometry_classes":consistent,"possibly_smooth_b0_three_classes":possible,
                       "remaining_classes":relevant})
        remaining_candidates.extend([{"prime":p,"h":h,**x} for x in relevant])
        print("R788 p=%s h=%s classes=%s remaining=%s"%(p,h,checked,possible),
              file=sys.stderr,flush=True)
    all_excluded=uniform and not remaining_candidates
    result={"format":"R788 original b=3 all-prime contact certificate",
            "max_order":M,"large_prime_cutoff":bound,"profiles":profiles,
            "geometry_class_total":len(classes),"distinct_finite_matrices":len(cache),
            "finite_prime_reports":finite,"all_strong_b3_excluded":all_excluded,
            "remaining_candidates":remaining_candidates,
            "scope":"Only F_p, b=b0=3, r=2, mq=0, p=12h+11>101, original angular lattice and h>=kappa+14. No higher b or central conclusion.",
            "outputs_persisted":False}
    encoded=json.dumps(result,separators=(",",":"))
    assert len(encoded.encode())<=59000
    print(encoded)

if __name__=="__main__": main()
