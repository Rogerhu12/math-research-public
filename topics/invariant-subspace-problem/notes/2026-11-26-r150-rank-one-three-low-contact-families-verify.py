#!/usr/bin/env python3
"""Complete original three low-contact rank-one families.
AI-assisted GPT-6 Astra Pro / Astra-ISP-347c05929dd3.
Reconstructed after executor loss; new source and execution identities are separate.
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
    Ps=dot(p,ulist)
    Gs=dot(ulist,mv(right_k(KH),ulist))
    need(Gs==Ps**2/6,"Complete original value G(s)=P(s)^2/6")
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
    mean = [Q2*y[i]-4*F*h[i]+8*HKHp[i]+ETA*(Ps**2-2*Gs)*ulist[i] for i in range(6)]
    N = [[F*y[i]*y[j]-2*F*H[i][j]-2*(y[i]*h[j]+h[i]*y[j])+4*HKH[i][j]+ETA*Ps*ulist[i]*ulist[j]
          for j in range(6)] for i in range(6)]
    second = anti(right_k(left_k(N)))
    G6 = F**3-6*F*b+6*F*tau2+12*c-8*tau3
    # Complete Q3 equals G6 because P(s)^3-6P(s)G(s)=0 and k(s,s)=0.
    need(Ps**3-6*Ps*Gs==0,"The complete V-linear term is retained and vanishes")
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
    ap=argparse.ArgumentParser()
    ap.add_argument("label",choices=["s_q_t","q_t2","q2_over_t"])
    ap.add_argument("--wall-seconds",type=int,default=240)
    args=ap.parse_args()
    resource.setrlimit(resource.RLIMIT_AS,(1536*1024**2,)*2)
    def timeout(signum,frame):raise TimeoutError("Exact QQ budget exhausted")
    signal.signal(signal.SIGALRM,timeout);signal.alarm(args.wall_seconds)
    started=time.monotonic()
    from flint import fmpq,fmpq_mat,fmpq_poly,fmpq_mpoly_ctx,nmod_mat
    FMPQ=fmpq;CTX=fmpq_mpoly_ctx.get(("s","t","eta","z"),"lex")
    S,T,ETA,Z=CTX.gens();ZERO=CTX.constant(0)
    need(int(fmpq_mat(K).det())==-25600,"Original det K")
    J2=[[0]*11 for _ in range(11)]
    for i in range(6):
     for j in range(6):
      for a in range(6):
       for b in range(6):J2[i+a][j+b]+=K[i][j]*K[a][b]
    need(int(fmpq_mat(J2).det())==-64701092257700249600,"Original det J2")
    ki,ji=inverse(K,fmpq_mat),inverse(J2,fmpq_mat)
    q0=S**3-5*S**2;q1=S**3-3*S**2+22*S
    q2=-3*S**2-3*S-5;q3=S+1
    qz=q0+q1*Z+q2*Z**2+q3*Z**3;qt=q0+q1*T+q2*T**2+q3*T**3
    dd=(q1+q2*T+q3*T*T)+(q2+q3*T)*Z+q3*Z*Z
    need(qz==(Z-T)*dd+qt,"Original cubic division")
    u=[S**i for i in range(6)];kexpr=zpoly(scalar_mv(K,u))
    need(kexpr==-(Z-S)**2*qz,"Original K polar")
    if args.label=="s_q_t":
        f=(Z-S)*qz*(Z-T);w=-(Z-S)**5*qz*dd
        residual=(Z-S)**6*qz*qz*qt
    elif args.label=="q_t2":
        f=qz*(Z-T)**2;w=-(Z-S)**6*dd*dd
        residual=(Z-S)**6*qz*qt*(2*qz-qt)
    else:
        f=qz*dd;w=-(Z-S)**6*qz*(Z-T)
        residual=(Z-S)**6*qz*qz*qt
    need(f*w-kexpr**3==residual,"Exact complete highest residual")
    fam=family(ki,ji,f,u,w,-ETA*residual)
    r01=eta_resultant(fam["second"][0],fam["second"][1])
    r02=eta_resultant(fam["second"][0],fam["second"][2])
    norms=[qt.resultant(p,"t") for p in (r01,r02)]
    A,B=[to_univariate_s(p,fmpq_poly) for p in norms]
    gg=A.gcd(B);gg=gg/gg[gg.degree()]
    sp=fmpq_poly([0,1])
    expected={"s_q_t":sp**24*(sp-2)**8*(sp+6)**8*(sp+1)**12,
      "q_t2":sp**24*(sp-2)**8*(sp+6)**8*(sp+1)**24,
      "q2_over_t":sp**12*(sp+1)**24}[args.label]
    need(gg==expected,"Exact QQ gcd equals the complete displayed divisor")
    A0,ra=divmod(A,gg);B0,rb=divmod(B,gg)
    need(not ra and not rb,"Exact QQ cofactor division")
    am,bm=mod_poly(A0),mod_poly(B0)
    need(len(am)==A0.degree()+1 and len(bm)==B0.degree()+1,"Reduced degrees preserved")
    smat=sylvester(am,bm);det=int(nmod_mat(smat,MODULUS).det())
    expected_degrees={"s_q_t":(236,184,240),"q_t2":(248,184,255),"q2_over_t":(256,220,621)}[args.label]
    need(A.degree()==B.degree()==expected_degrees[0],"Both original QQ norms have asserted degree")
    need(A0.degree()==B0.degree()==expected_degrees[1],"Both original cofactors have asserted degree")
    need(det==expected_degrees[2],"Complete full Sylvester determinant")
    fibers={}
    for sval in ([0,-1] if args.label=="q2_over_t" else [0,2,-6,-1]):
        qs=qt.subs({"s":sval});rs=r01.subs({"s":sval})
        if sval==-1:removed=CTX.constant(1)
        elif args.label=="q2_over_t":removed=T-5
        else:removed=(T-sval)**(2 if sval==0 else 1)
        remaining,remainder=divmod(qs,removed)
        need(not remainder,"Exact original exceptional-fiber factorization")
        norm=remaining.resultant(rs,"t");value=constant_mod(norm)
        need(value!=0,"Every nonsurviving finite root excluded over QQ")
        fibers[str(sval)]={"originalQDegree":deg(qs,1),"originalR01Degree":deg(rs,1),
             "normDetMod1009":value,"normHash":phash([norm])}
    uinf=[ZERO]*5+[CTX.constant(1)]
    uminus=[CTX.constant((-1)**i) for i in range(6)]
    hh=5*Z**2+26*Z+6
    boundary_definitions={
      "s_q_t":[(uinf,-(1+Z)**2,1+Z,"sInfinity_tMinus1"),
               (uminus,(1+Z)*hh,(1+Z)**5*hh**2,"sMinus1_tInfinity")],
      "q_t2":[(uinf,(1+Z)**3,CTX.constant(-1),"sInfinity_tMinus1"),
               (uminus,-hh,-(1+Z)**6*hh**2,"sMinus1_tInfinity")],
      "q2_over_t":[(uinf,-(1+Z)**2,1+Z,"sInfinity_tInfinity"),
               (uminus,-hh**2,-(1+Z)**6*hh,"sMinus1_tInfinity")]
    }
    bgates={}
    for uu,ff,ww,label in boundary_definitions[args.label]:
        ffam=family(ki,ji,ff,uu,ww,ZERO)
        all_units(ffam["second"]+ffam["mean"]+ffam["H"]+ffam["y"])
        bgates[label]=eta_boundary_gate(ffam,nmod_mat,label)
    survivors={}
    for sval in ([0] if args.label=="q2_over_t" else [0,2,-6]):
        tval=5 if args.label=="q2_over_t" else sval
        us=[CTX.constant(sval**i) for i in range(6)]
        ks=zpoly(scalar_mv(K,us))
        need(f.subs({"s":sval,"t":tval})==-ks,"Actual normalized survivor")
        ffam=family(ki,ji,-ks,us,-ks**2,ZERO)
        survivors[f"{sval},{tval}"]=physical_survivor_gate(ffam,f"{sval},{tval}")
    ffam=family(ki,ji,1+Z,uinf,-(1+Z)**2,ZERO)
    lab="infinity,-1" if args.label=="q2_over_t" else "infinity,infinity"
    survivors[lab]=physical_survivor_gate(ffam,lab)
    need(coeff(qt,0,3)==T+1 and coeff(qt,1,3)==S+1,"Every projective boundary of original cubic")
    emit({"stage":"complete","label":args.label,"elapsedSeconds":time.monotonic()-started,
      "sourceSHA256":hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
      "QQNormDegrees":[A.degree(),B.degree()],"QQCofactorDegrees":[A0.degree(),B0.degree()],
      "cofactorSylvesterDimension":len(smat),"cofactorSylvesterDetMod1009":det,
      "finiteExceptionalFiberGates":fibers,"projectiveBoundaryGates":bgates,
      "survivingOriginalCriticalFamilies":survivors,
      "fullGradientHash":phash(fam["second"]+fam["mean"]),
      "allOriginalVContributionsRetained":True,"characteristicZeroClassificationVerified":True,
      "ordinaryISPClaim":False,"globalMatchedBellClaim":False,
      "recoveryNote":"Reconstructed after executor loss. This execution belongs to this exact source SHA."})
if __name__=="__main__":main()

