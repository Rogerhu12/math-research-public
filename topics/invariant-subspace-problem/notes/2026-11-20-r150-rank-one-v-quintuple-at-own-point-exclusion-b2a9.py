#!/usr/bin/env python3
"""R150: exclude the rank-one V / quintuple-at-its-own-point mean branch.

Author: Astra-ISP-b2a9acde-20261120 / literature; GPT-6 Astra Pro, AI-assisted.
The mathematical conclusion is conditional on a successful frozen-source run.

Original binary quintic curve u(a,b)=(a^5,a^4*b,...,b^5).
In the finite chart s=(1,s), f_s(z)=(z-s)^5.
Set y=K^{-1}coeff_z(f_s), H=(1/6)J2^{-1}coeff_z(f_s^2+eta*k_s^3/f_s),
V=eta*u(s)^3/4. This is the entire indicated branch after nonzero
weighted scaling, with no genericity assumption on s or eta.
The infinity chart uses f=-a^5, hence f(z)=-1 and k_infinity(z)=-1-z.
Every original highest equation holds identically. Because k_s has at
least a double zero at s, all V contributions to the low gradients
vanish identically on this family, including the exceptional polar points.

We construct ALL 11 normalized original second gradients and all 6
normalized original mean gradients over QQ, check two full chain rules,
and use only n_0,n_1,n_2 to attempt the exclusion.
Each n_i has eta-degree <=2 and s-degree <=20.
The formal degree-two eta-resultants R01,R02 have s-degree <=80.
If their reductions both have degree 80 and the FIXED 160-square
Sylvester determinant is nonzero modulo 103, the rational determinant
is nonzero. This is a characteristic-zero exclusion certificate,
not a heuristic modular point test. All rational denominators must be
units modulo 103. Infinity is checked separately without cancellation.

Dependencies: python-flint. All arithmetic before reduction is QQ.
No arrays, matrices, multiplier dumps, or large artifacts are written.
"""
import argparse
import hashlib
import json
import math
import resource
import signal
import time
from fractions import Fraction as Q
from pathlib import Path

P = 103
K = [
    [0,0,0,0,5,-1],
    [0,0,0,-32,5,-1],
    [0,0,54,-4,5,0],
    [0,-32,-4,-8,0,0],
    [5,5,5,0,0,0],
    [-1,-1,0,0,0,0]
]
ONE = {(0,0): Q(1)}
ETA = {(0,1): Q(1)}

def need(ok, msg):
    if not ok:
        raise AssertionError(msg)

def emit(obj):
    print(json.dumps(obj, sort_keys=True, ensure_ascii=False), flush=True)

def clean(p):
    return {e:c for e,c in p.items() if c}

def add(*polys):
    out = {}
    for p in polys:
        for e,c in p.items():
            out[e] = out.get(e,Q(0)) + c
    return clean(out)

def scale(p,c):
    c = Q(c)
    return {e:c*a for e,a in p.items() if c*a}

def mul(a,b):
    out = {}
    for e,c in a.items():
        for f,d in b.items():
            g = (e[0]+f[0],e[1]+f[1])
            out[g] = out.get(g,Q(0)) + c*d
    return clean(out)

def power(a,n):
    out = ONE
    while n:
        if n&1:
            out = mul(out,a)
        a = mul(a,a)
        n //= 2
    return out

def psum(items):
    return add(*list(items))

def dot(a,b):
    return psum(mul(x,y) for x,y in zip(a,b))

def diff(p,i):
    out = {}
    for e,c in p.items():
        if e[i]:
            f = list(e)
            f[i] -= 1
            out[tuple(f)] = c*e[i]
    return out

def degree(p,i):
    return max((e[i] for e in p),default=-1)

def monomial(s_degree,eta_degree=0,c=1):
    return {(s_degree,eta_degree):Q(c)} if c else {}

def conv(a,b):
    out = [{} for _ in range(len(a)+len(b)-1)]
    for i,x in enumerate(a):
        for j,y in enumerate(b):
            out[i+j] = add(out[i+j],mul(x,y))
    return out

def scalar_mv(a,v):
    return [psum(scale(x,c) for c,x in zip(row,v)) for row in a]

def mv(a,v):
    return [dot(row,v) for row in a]

def mm(a,b):
    return [[psum(mul(a[i][k],b[k][j]) for k in range(len(b)))
             for j in range(len(b[0]))] for i in range(len(a))]

def left_k(a):
    return [[psum(scale(a[t][j],K[i][t]) for t in range(6))
             for j in range(len(a[0]))] for i in range(6)]

def right_k(a):
    return [[psum(scale(a[i][t],K[t][j]) for t in range(6))
             for j in range(6)] for i in range(len(a))]

def trace(a):
    return psum(a[i][i] for i in range(len(a)))

def anti(a):
    out = [{} for _ in range(11)]
    for i in range(6):
        for j in range(6):
            out[i+j] = add(out[i+j],a[i][j])
    return out

def record_poly(p):
    return [[list(e),str(p[e])] for e in sorted(p)]

def digest(obj):
    return hashlib.sha256(json.dumps(obj,sort_keys=True,
        separators=(",",":"),ensure_ascii=True).encode()).hexdigest()

def matrix_inverse(a,fmpq_mat):
    b = fmpq_mat(a).inv()
    out = [[Q(str(b[i,j])) for j in range(b.ncols())]
           for i in range(b.nrows())]
    for i in range(len(a)):
        for j in range(len(a)):
            need(sum(Q(a[i][k])*out[k][j] for k in range(len(a))) ==
                 int(i==j),"Exact rational inverse, every entry")
    return out

def build_family(ki,ji,infinity=False):
    if infinity:
        f = [scale(ONE,-1)] + [{} for _ in range(5)]
        u = [{} for _ in range(5)] + [ONE]
    else:
        f = [monomial(5-i,c=math.comb(5,i)*(-1)**(5-i))
             for i in range(6)]
        u = [monomial(i) for i in range(6)]
    polar = scalar_mv(K,u)
    k3 = conv(conv(polar,polar),polar)
    fsq = conv(f,f)
    if infinity:
        need(not any(k3[11:]),"Infinity homogeneous quotient has degree <=10")
        w = [scale(k3[i],-1) for i in range(11)]
    else:
        need(f[5]==ONE,"Finite divisor is monic in z, with no s localization")
        remainder = [dict(p) for p in k3]
        w = [{} for _ in range(11)]
        for i in range(15,4,-1):
            w[i-5] = remainder[i]
            for j in range(6):
                remainder[i-5+j] = add(remainder[i-5+j],
                                      scale(mul(w[i-5],f[j]),-1))
        need(not any(remainder),"Exact polynomial quotient k_s^3/f_s")
    need(conv(f,w)==k3,"Binary homogeneous division identity at every coefficient")
    x = [scale(a,Q(1,6)) for a in scalar_mv(ji,fsq)]
    yy = [scale(a,Q(1,6)) for a in scalar_mv(ji,w)]
    y = scalar_mv(ki,f)
    p = scalar_mv(K,y)
    need(p==f,"Original K times mean is exactly the chosen polar")
    hseq = [add(a,mul(ETA,b)) for a,b in zip(x,yy)]
    hmat = [[hseq[i+j] for j in range(6)] for i in range(6)]
    kh = left_k(hmat)
    hphys = anti(right_k(kh))
    expected_hphys = [scale(add(a,mul(ETA,b)),Q(1,6)) for a,b in zip(fsq,w)]
    need(hphys==expected_hphys,"All 11 original J2/Hankel identities")
    ell = [add(a,scale(b,-6)) for a,b in zip(conv(fsq,f),conv(f,hphys))]
    highest = [add(a,mul(ETA,b)) for a,b in zip(ell,k3)]
    need(not any(highest),"All 16 original highest equations")
    need(not trace(kh),"Original Hankel trace tr(KH)=0")
    need(not dot(u,scalar_mv(K,u)),"Original curve is K-isotropic")
    at_point = dot(f,u)
    h_at_point = dot(u,mv(right_k(kh),u))
    need(not at_point and not h_at_point,
         "Both V low-gradient contributions vanish, without genericity")
    need(max(degree(a,0) for a in y)<=5,"Mean s-degree <=5")
    need(max(degree(a,0) for a in x+yy)<=10,"Both Hankel heads s-degree <=10")
    need(max(degree(a,1) for a in hseq)<=1,"H is affine in eta")

    F = scale(dot(y,p),Q(1,2))
    h = mv(hmat,p)
    b = dot(p,h)
    kh2 = mm(kh,kh)
    kh3 = mm(kh2,kh)
    tau2 = trace(kh2)
    tau3 = trace(kh3)
    hkh = mm(right_k(hmat),hmat)
    hkhp = mv(hkh,p)
    c = dot(p,hkhp)
    Q2 = add(mul(F,F),scale(b,-2),scale(tau2,2))
    mean = [add(mul(Q2,y[i]),scale(mul(F,h[i]),-4),scale(hkhp[i],8))
            for i in range(6)]
    N = [[add(mul(F,mul(y[i],y[j])),
              scale(mul(F,hmat[i][j]),-2),
              scale(add(mul(y[i],h[j]),mul(h[i],y[j])),-2),
              scale(hkh[i][j],4))
          for j in range(6)] for i in range(6)]
    second = anti(right_k(left_k(N)))
    G6 = add(power(F,3),scale(mul(F,b),-6),scale(mul(F,tau2),6),
             scale(c,12),scale(tau3,-8))
    # Q3=G6 on this exact highest-equation family; V directional terms vanish.
    eta_chain = scale(dot(second,[diff(a,1) for a in hseq]),-6)
    s_chain = add(scale(dot(scalar_mv(K,mean),[diff(a,0) for a in y]),3),
                  scale(dot(second,[diff(a,0) for a in hseq]),-6))
    need(diff(G6,1)==eta_chain,"Full original eta chain rule")
    need(diff(G6,0)==s_chain,"Full original s chain rule")
    need(all(degree(a,1)<=2 and degree(a,0)<=20 for a in second),
         "Every original second gradient has eta-degree <=2 and s-degree <=20")
    need(all(degree(a,1)<=2 and degree(a,0)<=25 for a in mean),
         "Every original mean gradient has eta-degree <=2 and s-degree <=25")
    return {"x":x,"yy":yy,"mean":y,"H":hseq,
            "second":second,"first":mean,"G6":G6}

def eta_coeff(p,j):
    return {(s,0):c for (s,e),c in p.items() if e==j}

def formal_eta_resultant(a,b):
    c,bb,aa = [eta_coeff(a,j) for j in range(3)]
    f,e,d = [eta_coeff(b,j) for j in range(3)]
    afcd = add(mul(aa,f),scale(mul(c,d),-1))
    aebd = add(mul(aa,e),scale(mul(bb,d),-1))
    bfce = add(mul(bb,f),scale(mul(c,e),-1))
    out = add(mul(afcd,afcd),scale(mul(aebd,bfce),-1))
    need(degree(out,1)<=0 and degree(out,0)<=80,"Formal eta-resultant degree bounds")
    return out

def mod_coeff(q):
    q = Q(q)
    need(q.denominator%P!=0,"Every rational denominator is a unit modulo 103")
    return (q.numerator%P)*pow(q.denominator%P,-1,P)%P

def mod_s_poly(p):
    need(degree(p,1)<=0,"Univariate s polynomial")
    out = [0]*(degree(p,0)+1)
    for (s,e),c in p.items():
        out[s] = mod_coeff(c)
    while out and not out[-1]:
        out.pop()
    return out

def sylvester_columns(a,b):
    m,n = len(a)-1,len(b)-1
    need(m>=0 and n>=0,"Nonzero univariate resultant arguments")
    out = [[0]*(m+n) for _ in range(m+n)]
    for j in range(n):
        for i,c in enumerate(a):
            out[i+j][j] = c
    for j in range(m):
        for i,c in enumerate(b):
            out[i+j][n+j] = c
    return out

def poly_hash(items):
    return digest([record_poly(p) for p in items])

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--preflight-only",action="store_true")
    ap.add_argument("--wall-seconds",type=int,default=180)
    ap.add_argument("--memory-mib",type=int,default=1024)
    ap.add_argument("--output",default=None)
    args = ap.parse_args()
    need(1<=args.wall_seconds<=600,"Bounded wall budget")
    need(256<=args.memory_mib<=4096,"Bounded memory budget")
    resource.setrlimit(resource.RLIMIT_AS,(args.memory_mib*1024**2,)*2)
    def timeout(signum,frame):
        raise TimeoutError("Fixed rank-one/quintuple source wall budget exhausted")
    signal.signal(signal.SIGALRM,timeout)
    signal.alarm(args.wall_seconds)
    started = time.monotonic()
    from flint import fmpq_mat,nmod_mat

    need(int(fmpq_mat(K).det())==-25600,"Original det K")
    J2 = [[0]*11 for _ in range(11)]
    for i in range(6):
        for j in range(6):
            for a in range(6):
                for b in range(6):
                    J2[i+a][j+b] += K[i][j]*K[a][b]
    need(int(fmpq_mat(J2).det())==-64701092257700249600,"Original det J2")
    ki,ji = matrix_inverse(K,fmpq_mat),matrix_inverse(J2,fmpq_mat)
    affine = build_family(ki,ji)
    infinity = build_family(ki,ji,infinity=True)
    # Unit-denominator guard applies to the entire rational source, not only
    # the two selected resultants, and to both projective parameter charts.
    allpolys = []
    for family in (affine,infinity):
        for key in ("x","yy","mean","H","second","first"):
            allpolys.extend(family[key])
        allpolys.append(family["G6"])
    for row in ki+ji:
        for c in row:
            mod_coeff(c)
    checked = 0
    for poly in allpolys:
        for c in poly.values():
            mod_coeff(c)
            checked += 1
    r01 = formal_eta_resultant(affine["second"][0],affine["second"][1])
    r02 = formal_eta_resultant(affine["second"][0],affine["second"][2])
    ar,br = mod_s_poly(r01),mod_s_poly(r02)
    ri = formal_eta_resultant(infinity["second"][0],infinity["second"][1])
    ir = mod_s_poly(ri)
    record = {
        "schema":"r150-rank-one-V-quintuple-mean-at-s-20261120-v1",
        "author":"Astra-ISP-b2a9acde-20261120 / literature",
        "sourceSha256":hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        "modulus":P,
        "allOriginalSecondGradients":11,
        "allOriginalMeanGradients":6,
        "allOriginalHighestEquations":16,
        "bothProjectiveParameterCharts":True,
        "genericityAssumptionOnS":False,
        "allQQSourceDenominatorsAre103Units":True,
        "checkedQQCoefficients":checked,
        "affineSecondGradientEtaDegreeBound":2,
        "affineSecondGradientSDegreeBound":20,
        "affineFormalResultantSDegreeBound":80,
        "affineRationalResultantDegrees":[degree(r01,0),degree(r02,0)],
        "affineReducedResultantDegrees":[len(ar)-1,len(br)-1],
        "affineFullLowGradientHash":poly_hash(affine["second"]+affine["first"]),
        "infinityFullLowGradientHash":poly_hash(infinity["second"]+infinity["first"]),
        "affineHankelFamilyHash":poly_hash(affine["x"]+affine["yy"]),
        "QQResultantPairHash":poly_hash([r01,r02]),
        "modResultantPairHash":digest([ar,br]),
        "infinityResultantHash":poly_hash([ri]),
        "fullOriginalChainRulesPassed":True,
        "ordinaryISPClaim":False,
        "globalMatchedBellClaim":False
    }
    emit({"stage":"original_rational_source_constructed",
          "elapsedSeconds":round(time.monotonic()-started,6),
          "resultantDegrees":record["affineRationalResultantDegrees"],
          "allSourceDenominatorsAreUnits":True,
          "bothOriginalChainRulesPassed":True})
    if args.preflight_only:
        record.update({"status":"preflight_only_no_determinant_claim",
                       "characteristicZeroExclusionVerified":False})
    else:
        need(degree(r01,0)==degree(r02,0)==80,"Exact QQ degrees are both 80")
        need(len(ar)==len(br)==81,"Reduction preserves both degree-80 leading terms")
        syl = sylvester_columns(ar,br)
        need(len(syl)==160 and all(len(row)==160 for row in syl),
             "FIXED complete 160-square Sylvester matrix")
        det = int(nmod_mat(syl,P).det())
        need(det!=0,"Nonzero fixed Sylvester determinant modulo 103")
        need(degree(ri,0)==0 and len(ir)==1 and ir[0]!=0,
             "Infinity formal eta-resultant is a nonzero rational constant")
        # Cross-check the infinity result as its complete degree-two Sylvester.
        ia = [mod_coeff(eta_coeff(infinity["second"][0],j).get((0,0),Q(0)))
              for j in range(3)]
        ib = [mod_coeff(eta_coeff(infinity["second"][1],j).get((0,0),Q(0)))
              for j in range(3)]
        need(ia[2] and ib[2],"Infinity eta-degree-two leading terms survive")
        idet = int(nmod_mat(sylvester_columns(ia,ib),P).det())
        need(idet==ir[0] and idet!=0,"Infinity full 4-square Sylvester identity")
        record.update({
            "status":"exact_characteristic_zero_exclusion_entire_quintuple_at_s_branch",
            "characteristicZeroExclusionVerified":True,
            "affineSylvesterDimension":160,
            "affineSylvesterDetMod103":det,
            "infinitySylvesterDimension":4,
            "infinitySylvesterDetMod103":idet,
            "affineSylvesterHash":digest(syl),
            "interpretation":(
                "The full original critical locus has no point with nonzero "
                "rank-one V supported at s and mean polar proportional to Delta_s^5. "
                "This includes every projective s, all exceptional polar root "
                "multiplicities, and every finite eta. No other divisor pattern "
                "and no general V!=0 stratum is declared closed.")
        })
    signal.alarm(0)
    record["elapsedSeconds"] = round(time.monotonic()-started,6)
    record["peakRssKiB"] = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
    if args.output:
        target = Path(args.output)
        target.parent.mkdir(parents=True,exist_ok=True)
        target.write_text(json.dumps(record,sort_keys=True,ensure_ascii=False,indent=2)
                          +"\n",encoding="utf-8")
    emit({"stage":"complete",**record})

if __name__=="__main__":
    main()
