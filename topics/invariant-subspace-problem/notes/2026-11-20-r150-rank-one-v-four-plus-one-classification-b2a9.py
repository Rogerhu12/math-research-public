#!/usr/bin/env python3
"""R150: rank-one nonzero V, mean divisor Delta_s^4 Delta_t.

Author: Astra-ISP-b2a9acde-20261120 / literature; GPT-6 Astra Pro, AI-assisted.
This is an UNEXECUTED certificate source until a frozen successful run is recorded.
It preserves the original K, J2, all 16 highest, 11 second and 6 mean equations.
Finite s,t obey the original off-diagonal polar equation q(s,t)=0. No
division by s, s+1, s-t, or a discriminant occurs in the source family.

The exact QQ route is:
  quadratic eta-resultants R01,R02 from original n0,n1,n2;
  exact QQ t-resultants with q(s,t), of expected s-degree 244;
  exact division of BOTH by s^12*(s+1)^12;
  nonzero complete 440-square Sylvester determinant of the two degree-220
  cofactors modulo 1009, with every QQ denominator a unit and degrees preserved.
This certifies over characteristic zero that finite s can only be 0 or -1.
Every exceptional/projective boundary is then checked in the original family.
The surviving (s,t)=(0,5),(infinity,-1) have T3=0 identically and are genuine
critical families. Other divisor patterns are not covered.

No large arrays or coefficient dumps are saved; only a small JSON result.
Dependencies: python-flint. Official exact mpoly resultant API:
https://python-flint.readthedocs.io/en/latest/fmpq_mpoly.html
"""
import argparse
import hashlib
import json
import resource
import signal
import time
from pathlib import Path
from operator import index

MODULUS = 1009
K = [
    [0,0,0,0,5,-1],
    [0,0,0,-32,5,-1],
    [0,0,54,-4,5,0],
    [0,-32,-4,-8,0,0],
    [5,5,5,0,0,0],
    [-1,-1,0,0,0,0]
]

def need(ok,msg):
    if not ok:
        raise AssertionError(msg)

def emit(obj):
    print(json.dumps(obj,sort_keys=True,ensure_ascii=False),flush=True)

def digest(obj):
    return hashlib.sha256(json.dumps(obj,sort_keys=True,ensure_ascii=True,
        separators=(",",":")).encode()).hexdigest()

def prec(poly):
    d = poly.to_dict()
    return [[[index(a) for a in e],str(d[e])] for e in sorted(d)]

def phash(items):
    return digest([prec(p) for p in items])

def deg(poly,i):
    return max((int(e[i]) for e in poly.to_dict()),default=-1)

def coeff(poly,var,j):
    d = {}
    for e,c in poly.to_dict().items():
        if e[var]==j:
            f = list(e)
            f[var] = 0
            d[tuple(f)] = c
    return CTX.from_dict(d)

def zcoeffs(poly,n):
    need(deg(poly,3)<=n,"Complete z coefficient bound")
    return [coeff(poly,3,j) for j in range(n+1)]

def zpoly(seq):
    return sum((v*Z**i for i,v in enumerate(seq)),ZERO)

def dot(a,b):
    return sum((x*y for x,y in zip(a,b)),ZERO)

def scalar_mv(a,v):
    return [sum((c*x for c,x in zip(row,v)),ZERO) for row in a]

def mv(a,v):
    return [dot(row,v) for row in a]

def mm(a,b):
    return [[sum((a[i][k]*b[k][j] for k in range(len(b))),ZERO)
             for j in range(len(b[0]))] for i in range(len(a))]

def left_k(a):
    return [[sum((K[i][t]*a[t][j] for t in range(6)),ZERO)
             for j in range(len(a[0]))] for i in range(6)]

def right_k(a):
    return [[sum((a[i][t]*K[t][j] for t in range(6)),ZERO)
             for j in range(6)] for i in range(len(a))]

def anti(a):
    return [sum((a[i][j] for i in range(6) for j in range(6) if i+j==m),ZERO)
            for m in range(11)]

def trace(a):
    return sum((a[i][i] for i in range(len(a))),ZERO)

def inverse(a,fmpq_mat):
    b = fmpq_mat(a).inv()
    out = [[b[i,j] for j in range(b.ncols())] for i in range(b.nrows())]
    for i in range(len(a)):
        for j in range(len(a)):
            need(sum(a[i][k]*out[k][j] for k in range(len(a)))==int(i==j),
                 "Every original inverse entry is exact")
    return out

def family(ki,ji,fexpr,ulist,wexpr,expected_highest):
    f = zcoeffs(fexpr,5)
    w = zcoeffs(wexpr,10)
    polar = scalar_mv(K,ulist)
    kexpr = zpoly(polar)
    x = [a/6 for a in scalar_mv(ji,zcoeffs(fexpr**2,10))]
    yy = [a/6 for a in scalar_mv(ji,w)]
    y = scalar_mv(ki,f)
    p = scalar_mv(K,y)
    need(p==f,"Original K times mean")
    hseq = [a+ETA*b for a,b in zip(x,yy)]
    H = [[hseq[i+j] for j in range(6)] for i in range(6)]
    KH = left_k(H)
    G = anti(right_k(KH))
    need(zpoly(G)==(fexpr**2+ETA*wexpr)/6,"All 11 exact original J2 identities")
    highest = fexpr**3-6*fexpr*zpoly(G)+ETA*kexpr**3
    need(highest==expected_highest,"All 16 highest equations with exact q residual")
    highest_seq = zcoeffs(highest,15)
    need(not trace(KH),"Original tr(KH)=0")
    need(not dot(ulist,scalar_mv(K,ulist)),"Original K-isotropic physical point")
    need(not dot(p,ulist),"Mean polar at its own physical point is zero")
    need(not dot(ulist,mv(right_k(KH),ulist)),
         "Second physical value at its own point is zero")
    V = []
    for m in range(16):
        i = min(m,5)
        j = min(m-i,5)
        k = m-i-j
        V.append(ETA*ulist[i]*ulist[j]*ulist[k]/4)
    for i in range(6):
        for j in range(6):
            for k in range(6):
                need(4*V[i+j+k]==ETA*ulist[i]*ulist[j]*ulist[k],
                     "Original merged rank-one third tensor")
    F = dot(y,p)/2
    h = mv(H,p)
    b = dot(p,h)
    KH2 = mm(KH,KH)
    tau2,tau3 = trace(KH2),trace(mm(KH2,KH))
    HKH = mm(right_k(H),H)
    HKHp = mv(HKH,p)
    c = dot(p,HKHp)
    Q2 = F**2-2*b+2*tau2
    mean = [Q2*y[i]-4*F*h[i]+8*HKHp[i] for i in range(6)]
    N = [[F*y[i]*y[j]-2*F*H[i][j]-2*(y[i]*h[j]+h[i]*y[j])+4*HKH[i][j]
          for j in range(6)] for i in range(6)]
    second = anti(right_k(left_k(N)))
    G6 = F**3-6*F*b+6*F*tau2+12*c-8*tau3
    # The complete Q3 equals G6 here because P(s)=G_H(s)=k(s,s)=0.
    # Keep the original V derivative in each chain, even away from q(s,t)=0.
    for name in ("s","t","eta"):
        vterm = 4*dot(highest_seq,[a.derivative(name) for a in V])
        original_chain = (
            3*dot(scalar_mv(K,mean),[a.derivative(name) for a in y])
            -6*dot(second,[a.derivative(name) for a in hseq])+vterm)
        need(G6.derivative(name)==original_chain,
             "Complete original chain rule in "+name)
        need(not vterm,"The retained original V chain term vanishes identically")
    need(all(deg(p,2)<=2 for p in second+mean),"All low gradients eta-degree <=2")
    return {"y":y,"H":hseq,"x":x,"yy":yy,"V":V,"u":ulist,
            "second":second,"mean":mean,"G6":G6,"highest":highest_seq}

def eta_resultant(a,b):
    c,bb,aa = [coeff(a,2,j) for j in range(3)]
    f,e,d = [coeff(b,2,j) for j in range(3)]
    r = (aa*f-c*d)**2-(aa*e-bb*d)*(bb*f-c*e)
    need(deg(r,2)<=0 and deg(r,3)<=0,"Formal quadratic eta-resultant")
    return r

def modq(c):
    c = FMPQ(c)
    num,den = int(c.p),int(c.q)
    need(den%MODULUS!=0,"Every rational coefficient denominator is a 1009 unit")
    return num%MODULUS*pow(den%MODULUS,-1,MODULUS)%MODULUS

def all_units(polys):
    count = 0
    for p in polys:
        for c in p.to_dict().values():
            modq(c)
            count += 1
    return count

def to_univariate_s(p,fmpq_poly):
    need(all(e[1]==e[2]==e[3]==0 for e in p.to_dict()),"Exact univariate s norm")
    data = [FMPQ(0)]*(deg(p,0)+1)
    for e,c in p.to_dict().items():
        data[int(e[0])] = c
    return fmpq_poly(data)

def mod_poly(p):
    out = [modq(c) for c in p.coeffs()]
    while out and not out[-1]:
        out.pop()
    return out

def sylvester(a,b):
    m,n = len(a)-1,len(b)-1
    need(m>=0 and n>=0,"Nonzero Sylvester inputs")
    out = [[0]*(m+n) for _ in range(m+n)]
    for j in range(n):
        for i,c in enumerate(a):
            out[i+j][j] = c
    for j in range(m):
        for i,c in enumerate(b):
            out[i+j][n+j] = c
    return out

def constant_mod(p):
    d = p.to_dict()
    need(not d or set(d)=={(0,0,0,0)},"Exact rational scalar")
    return modq(d.get((0,0,0,0),FMPQ(0)))

def eta_boundary_gate(fam,nmod_mat,label):
    a,b = fam["second"][:2]
    need(all(e[0]==e[1]==e[3]==0 for p in (a,b) for e in p.to_dict()),
         label+": two scalar eta polynomials")
    ar = [constant_mod(coeff(a,2,j)) for j in range(3)]
    br = [constant_mod(coeff(b,2,j)) for j in range(3)]
    need(ar[2] and br[2],label+": both eta degrees preserved")
    r = eta_resultant(a,b)
    det = int(nmod_mat(sylvester(ar,br),MODULUS).det())
    need(det==constant_mod(r) and det!=0,label+": complete fixed four-square gate")
    return {"detMod1009":det,"resultantHash":phash([r])}

def physical_survivor_gate(fam,label):
    u = fam["u"]
    need(all(a==-b for a,b in zip(fam["y"],u)),label+": y=-u")
    for i in range(6):
        for j in range(6):
            need(fam["H"][i+j]==(1-ETA)*u[i]*u[j]/6,
                 label+": original H=(1-eta)u^2/6")
    need(not any(fam["second"]+fam["mean"]+fam["highest"]),
         label+": all original critical equations hold for every eta")
    # Then y^3-6yH+4V=-u^3+(1-eta)u^3+eta*u^3=0.
    return {"allOriginalGradientsIdenticallyZero":True,
            "thirdOrdinaryMomentIdenticallyZero":True}

def main():
    global CTX,S,T,ETA,Z,ZERO,FMPQ
    ap = argparse.ArgumentParser()
    ap.add_argument("--preflight-only",action="store_true")
    ap.add_argument("--wall-seconds",type=int,default=180)
    ap.add_argument("--memory-mib",type=int,default=1024)
    ap.add_argument("--output",default=None)
    args = ap.parse_args()
    need(1<=args.wall_seconds<=600,"Fixed wall budget")
    need(256<=args.memory_mib<=4096,"Fixed memory budget")
    resource.setrlimit(resource.RLIMIT_AS,(args.memory_mib*1024**2,)*2)
    def timeout(signum,frame):
        raise TimeoutError("Fixed rank-one four-plus-one wall budget exhausted")
    signal.signal(signal.SIGALRM,timeout)
    signal.alarm(args.wall_seconds)
    started = time.monotonic()
    from flint import fmpq,fmpq_mat,fmpq_poly,fmpq_mpoly_ctx,nmod_mat
    FMPQ = fmpq
    CTX = fmpq_mpoly_ctx.get(("s","t","eta","z"),"lex")
    S,T,ETA,Z = CTX.gens()
    ZERO = CTX.constant(0)
    need(int(fmpq_mat(K).det())==-25600,"Original det K")
    J2 = [[0]*11 for _ in range(11)]
    for i in range(6):
        for j in range(6):
            for a in range(6):
                for b in range(6):
                    J2[i+a][j+b] += K[i][j]*K[a][b]
    need(int(fmpq_mat(J2).det())==-64701092257700249600,"Original det J2")
    ki,ji = inverse(K,fmpq_mat),inverse(J2,fmpq_mat)

    q0 = S**3-5*S**2
    q1 = S**3-3*S**2+22*S
    q2 = -3*S**2-3*S-5
    q3 = S+1
    qz = q0+q1*Z+q2*Z**2+q3*Z**3
    qst = q0+q1*T+q2*T**2+q3*T**3
    qdiv = (q1+q2*T+q3*T**2)+(q2+q3*T)*Z+q3*Z**2
    need(qz==(Z-T)*qdiv+qst,"Exact polynomial division by z-t")
    u = [S**i for i in range(6)]
    kexpr = zpoly(scalar_mv(K,u))
    need(kexpr==-(Z-S)**2*qz,"Original K polar factorization")
    fexpr = (Z-S)**4*(Z-T)
    wexpr = -(Z-S)**2*qz**2*qdiv
    need(fexpr*wexpr-kexpr**3==(Z-S)**6*qz**2*qst,
         "Exact quotient identity modulo the original bicubic")
    mainfam = family(ki,ji,fexpr,u,wexpr,-ETA*(Z-S)**6*qz**2*qst)
    for n in mainfam["second"]:
        need(deg(n,1)<=4,"Each original second gradient t-degree <=4")
        for j in range(3):
            need(deg(coeff(n,2,j),0)<=16+3*j,
                 "Each eta coefficient has its exact s-degree upper bound")
    r01 = eta_resultant(mainfam["second"][0],mainfam["second"][1])
    r02 = eta_resultant(mainfam["second"][0],mainfam["second"][2])
    for r in (r01,r02):
        need(deg(r,0)<=76 and deg(r,1)<=16,"Resultant bidegree upper bounds")
        need(deg(r,1)==16,"Exact t-degree of each eta-resultant is 16")
    # Native exact QQ resultants are full algebraic operations, not interpolation.
    norm01 = qst.resultant(r01,"t")
    norm02 = qst.resultant(r02,"t")
    A,B = to_univariate_s(norm01,fmpq_poly),to_univariate_s(norm02,fmpq_poly)
    need(A.degree()==B.degree()==244,"Both exact QQ norms have s-degree 244")
    sp = fmpq_poly([0,1])
    common_factor = (sp*(sp+1))**12
    A0,ra = divmod(A,common_factor)
    B0,rb = divmod(B,common_factor)
    need(not ra and not rb,"Both displayed degree-24 factors divide exactly over QQ")
    need(A0.degree()==B0.degree()==220,"Both exact cofactors have degree 220")
    allpolys = []
    for key in ("y","H","x","yy","V","second","mean","highest"):
        allpolys.extend(mainfam[key])
    allpolys.extend([mainfam["G6"],r01,r02,norm01,norm02])
    units = all_units(allpolys)
    for row in ki+ji:
        for c in row:
            modq(c)
    am,bm = mod_poly(A0),mod_poly(B0)
    need(len(am)==len(bm)==221,"Both degree-220 leading terms survive modulo 1009")
    record = {
        "schema":"r150-rank-one-V-four-plus-one-20261120-v1",
        "author":"Astra-ISP-b2a9acde-20261120 / literature",
        "sourceSha256":hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        "modulus":MODULUS,
        "allOriginalSecondGradients":11,"allOriginalMeanGradients":6,
        "allOriginalHighestEquations":16,
        "fullOriginalChainsPassed":["s","t","eta"],
        "allQQDenominatorsAreUnits":True,"checkedQQCoefficients":units,
        "QQNormDegrees":[244,244],"QQCofactorDegrees":[220,220],
        "commonFactor":"s^12*(s+1)^12",
        "fullLowGradientHash":phash(mainfam["second"]+mainfam["mean"]),
        "originalHankelFamilyHash":phash(mainfam["x"]+mainfam["yy"]),
        "etaResultantPairHash":phash([r01,r02]),
        "QQNormPairHash":phash([norm01,norm02]),
        "QQCofactorPairHash":digest([[str(c) for c in A0.coeffs()],
                                   [str(c) for c in B0.coeffs()]]),
        "ordinaryISPClaim":False,"globalMatchedBellClaim":False
    }
    emit({"stage":"exact_QQ_source_and_norms_constructed",
          "elapsedSeconds":round(time.monotonic()-started,6),
          "QQNormDegrees":[244,244],"QQCofactorDegrees":[220,220]})
    if args.preflight_only:
        record.update({"status":"preflight_only_no_exclusion_claim",
                       "characteristicZeroClassificationVerified":False})
    else:
        smat = sylvester(am,bm)
        need(len(smat)==440 and all(len(r)==440 for r in smat),
             "Complete FIXED 440-square cofactor Sylvester matrix")
        sdet = int(nmod_mat(smat,MODULUS).det())
        need(sdet!=0,"Nonzero cofactor Sylvester determinant modulo 1009")
        # Finite s=-1: the actual t polynomial has degree two. Use that
        # separate fiber, never the cubic formal norm with a lost leading term.
        qminus = qst.subs({"s":-1})
        rminus = r01.subs({"s":-1})
        need(deg(qminus,1)==2 and deg(rminus,1)==16,"Finite -1 fiber degrees")
        minusnorm = qminus.resultant(rminus,"t")
        need(constant_mod(minusnorm)!=0,"Finite s=-1 has no common original roots")

        # Every remaining projective boundary is built from original K,J2.
        u0 = [CTX.constant(1)]+[ZERO]*5
        uinf = [ZERO]*5+[CTX.constant(1)]
        uminus = [CTX.constant((-1)**i) for i in range(6)]
        # s=0,t=0: f=z^5. This is the already-closed quintuple branch,
        # but its complete two-gradient gate is independently retained here.
        zero_diag = family(ki,ji,Z**5,u0,Z**7*(5-Z)**3,ZERO)
        # s=infinity,t=infinity: binary f=-a^5.
        inf_diag = family(ki,ji,CTX.constant(-1),uinf,(1+Z)**3,ZERO)
        # s=-1,t=infinity: binary f=-a*(a+b)^4.
        mixed_inf = family(ki,ji,-(1+Z)**4,uminus,
                           -(1+Z)**2*(5*Z**2+26*Z+6)**3,ZERO)
        boundary_gates = {}
        for label,fam in (
            ("s0_t0",zero_diag),("sInfinity_tInfinity",inf_diag),
            ("sMinus1_tInfinity",mixed_inf)):
            all_units(fam["second"]+fam["mean"]+fam["H"]+fam["y"])
            boundary_gates[label] = eta_boundary_gate(fam,nmod_mat,label)
        # Genuine survivors: f=-k_s at s=0 and s=infinity.
        surv0 = family(ki,ji,Z**4*(Z-5),u0,-Z**8*(Z-5)**2,ZERO)
        survi = family(ki,ji,1+Z,uinf,-(1+Z)**2,ZERO)
        survivors = {
            "s0_t5":physical_survivor_gate(surv0,"s=0,t=5"),
            "sInfinity_tMinus1":physical_survivor_gate(survi,"s=infinity,t=-1")
        }
        # Original projective bicubic boundary equations, with no omitted root.
        need(qst.subs({"s":0})==T**2*(T-5),"All finite t at s=0")
        need(qst.subs({"s":-1})==-(5*T**2+26*T+6),"All finite t at s=-1")
        # Highest s^3 coefficient is t+1; highest t^3 coefficient is s+1.
        need(coeff(qst,0,3)==T+1 and coeff(qst,1,3)==S+1,
             "Both infinity charts of the original bihomogeneous bicubic")
        record.update({
            "status":"exact_characteristic_zero_four_plus_one_classification",
            "characteristicZeroClassificationVerified":True,
            "cofactorSylvesterDimension":440,
            "cofactorSylvesterDetMod1009":sdet,
            "cofactorSylvesterHash":digest(smat),
            "finiteSMinus1NormDetMod1009":constant_mod(minusnorm),
            "finiteSMinus1NormHash":phash([minusnorm]),
            "projectiveBoundaryGates":boundary_gates,
            "survivingOriginalCriticalFamilies":survivors,
            "interpretation":(
                "In the full original rank-one-V branch with mean polar "
                "proportional to Delta_s^4*Delta_t and q(s,t)=0, the only "
                "critical families have (s,t)=(0,5) or (infinity,-1), after "
                "the displayed normalization. They have T3=0, hence every "
                "matched Bell cubic value is zero. All finite, coincident, "
                "and infinite boundary parameters are covered. No other "
                "divisor pattern or general V!=0 locus is declared closed.")
        })
    record["elapsedSeconds"] = round(time.monotonic()-started,6)
    record["peakRssKiB"] = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
    signal.alarm(0)
    if args.output:
        target = Path(args.output)
        target.parent.mkdir(parents=True,exist_ok=True)
        target.write_text(json.dumps(record,sort_keys=True,ensure_ascii=False,indent=2)
                          +"\n",encoding="utf-8")
    emit({"stage":"complete",**record})

if __name__=="__main__":
    main()
