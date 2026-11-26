#!/usr/bin/env python3
# Reconstructed from preserved mathematical content after original executor loss.
# This source has a new identity; previous execution hashes are not assigned to it.
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
    for name in ("s","t","r","eta"):
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
    need(all(not any(e[1:]) for e in p.to_dict()),"Exact univariate s norm")
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
    need(not d or set(d)=={(0,0,0,0,0)},"Exact rational scalar")
    return modq(d.get((0,0,0,0,0),FMPQ(0)))

def eta_boundary_gate(fam,nmod_mat,label):
    a,b = fam["second"][:2]
    need(all(e[0]==e[1]==e[3]==e[4]==0 for p in (a,b) for e in p.to_dict()),
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


def inverse_mod_poly(a,m):
    aa,bb=a%m,m
    xx,yy=m*0+1,m*0
    while bb:
        q,rr=divmod(aa,bb)
        aa,bb=bb,rr
        xx,yy=yy,xx-q*yy
    need(aa.degree()==0 and aa[0]!=0,"Exact quotient-algebra element is a unit")
    ans=(xx/aa[0])%m
    need((a*ans)%m==1,"Exact quotient-algebra inverse identity")
    return ans

def evaluate_mod_poly(p,sv,tv,rv,m):
    need(all(e[2]==e[3]==0 for e in p.to_dict()),"No eta or z in quotient evaluation")
    powers={}
    for idx,v in [(0,sv),(1,tv),(4,rv)]:
        powers[idx]=[m*0+1]
        for _ in range(max(0,deg(p,idx))):
            powers[idx].append((powers[idx][-1]*v)%m)
    result=m*0
    for e,c in p.to_dict().items():
        term=m*0+c
        for idx in (0,1,4):term=(term*powers[idx][int(e[idx])])%m
        result=(result+term)%m
    return result

def unihash(p):
    return digest([str(c) for c in p.coeffs()])

def quotient_gate(p,sv,tv,rv,m,label):
    val=evaluate_mod_poly(p,sv,tv,rv,m)
    inv=inverse_mod_poly(val,m)
    need((val*inv)%m==1,label+": complete exact QQ inverse")
    return {"valueDegree":int(val.degree()),"valueSHA256":unihash(val),
        "inverseSHA256":unihash(inv),"exactQQInverseVerified":True}

def main():
    global CTX,S,T,ETA,Z,R,ZERO,FMPQ
    ap=argparse.ArgumentParser()
    ap.add_argument("label",choices=["s2_t2_r","s_t3_r","s_t2_r2","t3_r2"])
    ap.add_argument("--wall-seconds",type=int,default=240)
    args=ap.parse_args()
    resource.setrlimit(resource.RLIMIT_AS,(1536*1024**2,)*2)
    def timeout(signum,frame):raise TimeoutError("Exact QQ budget exhausted")
    signal.signal(signal.SIGALRM,timeout);signal.alarm(args.wall_seconds)
    started=time.monotonic()
    from flint import fmpq,fmpq_mat,fmpq_poly,fmpq_mpoly_ctx,nmod_mat
    FMPQ=fmpq;CTX=fmpq_mpoly_ctx.get(("s","t","eta","z","r"),"lex")
    S,T,ETA,Z,R=CTX.gens();ZERO=CTX.constant(0)
    need(int(fmpq_mat(K).det())==-25600,"Original det K")
    J2=[[0]*11 for _ in range(11)]
    for i in range(6):
     for j0 in range(6):
      for a0 in range(6):
       for b0 in range(6):J2[i+a0][j0+b0]+=K[i][j0]*K[a0][b0]
    need(int(fmpq_mat(J2).det())==-64701092257700249600,"Original det J2")
    ki,ji=inverse(K,fmpq_mat),inverse(J2,fmpq_mat)
    q0=S**3-5*S**2;q1=S**3-3*S**2+22*S
    q2=-3*S**2-3*S-5;q3=S+1
    qz=q0+q1*Z+q2*Z**2+q3*Z**3
    qt=q0+q1*T+q2*T**2+q3*T**3
    d0=q1+q2*T+q3*T*T;d1=q2+q3*T
    dd=d0+d1*Z+q3*Z*Z
    dt=d0+d1*R+q3*R*R
    ee=q2+q3*(T+R)+q3*Z
    residual_root=qt+(Z-T)*dt
    need(qz==(Z-T)*dd+qt,"Original first cubic division")
    need(dd==(Z-R)*ee+dt,"Original second cubic division including t=r")
    need(qz==(Z-T)*(Z-R)*ee+residual_root,"Full two-root divisor constraint")
    u=[S**i for i in range(6)];kexpr=zpoly(scalar_mv(K,u))
    need(kexpr==-(Z-S)**2*qz,"Original K polar")
    exponents={"s2_t2_r":(2,2,1),"s_t3_r":(1,3,1),
               "s_t2_r2":(1,2,2),"t3_r2":(0,3,2)}
    j,a,b=exponents[args.label]
    f=(Z-S)**j*(Z-T)**a*(Z-R)**b
    w=-(Z-S)**(6-j)*(Z-T)**(3-a)*(Z-R)**(3-b)*ee**3
    residual=(Z-S)**6*residual_root*(3*qz*qz-3*qz*residual_root+residual_root**2)
    need(f*w-kexpr**3==residual,"Exact complete two-root highest residual")
    fam=family(ki,ji,f,u,w,-ETA*residual)
    r01=eta_resultant(fam["second"][0],fam["second"][1])
    r02=eta_resultant(fam["second"][0],fam["second"][2])
    first_norms=[dt.resultant(p,"r") for p in (r01,r02)]
    norms=[qt.resultant(p,"t") for p in first_norms]
    A,B=[to_univariate_s(p,fmpq_poly) for p in norms]
    gg=A.gcd(B);gg=gg/gg[gg.degree()]
    sp=fmpq_poly([0,1])
    D=5*sp**8+50*sp**7+153*sp**6-936*sp**5-2888*sp**4+15936*sp**3-3392*sp**2-25472*sp+9600
    expected={"s2_t2_r":sp**24*(sp+1)**156*(D/5)**8,
              "s_t3_r":sp**24*(sp+1)**156,
              "s_t2_r2":(sp+1)**168,"t3_r2":(sp+1)**168}[args.label]
    need(gg==expected,"Exact QQ gcd with every exceptional factor")
    A0,ra=divmod(A,gg);B0,rb=divmod(B,gg)
    need(not ra and not rb,"Exact original cofactor division")
    am,bm=mod_poly(A0),mod_poly(B0)
    need(len(am)==A0.degree()+1 and len(bm)==B0.degree()+1,"Both cofactor degrees preserved mod 1009")
    smat=sylvester(am,bm);det=int(nmod_mat(smat,MODULUS).det())
    ed={"s2_t2_r":(620,376,12),"s_t3_r":(620,440,610),
        "s_t2_r2":(648,480,294),"t3_r2":(648,480,198)}[args.label]
    need(A.degree()==B.degree()==ed[0],"Both original norms have asserted degree")
    need(A0.degree()==B0.degree()==ed[1],"Both original cofactors have asserted degree")
    need(det==ed[2],"Complete full Sylvester determinant")

    # The only finite s with an infinite q_s root is s=-1.
    # Work in the entire QQ[T]/(5T^2+26T+6), without choosing embeddings.
    h=5*sp**2+26*sp+6
    zero=sp*0;one=zero+1;minus=zero-1
    beta=-fmpq(26,5)-sp
    need(evaluate_mod_poly(qt,minus,sp,beta,h)==0,"s=-1 first finite root")
    need(evaluate_mod_poly(dt,minus,sp,beta,h)==0,"s=-1 second finite root")
    bgates={"finite_finite":quotient_gate(r01,minus,sp,beta,h,"s=-1 finite-finite")}
    hh=5*Z**2+26*Z+6;ht=5*T*T+26*T+6;ell=5*Z+26+5*T
    need(hh==(Z-T)*ell+ht,"Exact s=-1 finite root division")
    um=[CTX.constant((-1)**i) for i in range(6)]
    km=zpoly(scalar_mv(K,um));need(km==(Z+1)**2*hh,"Exact s=-1 original polar")
    for label,power,signpower in [("infinity_finite",b,a),("finite_infinity",a,b)]:
        ff=(-1)**signpower*(Z+1)**j*(Z-T)**power
        ww=(-1)**signpower*(Z+1)**(6-j)*(Z-T)**(3-power)*ell**3
        resid=-(Z+1)**6*ht*(3*hh*hh-3*hh*ht+ht**2)
        need(ff*ww-km**3==resid,"Complete s=-1 boundary highest residual")
        ffam=family(ki,ji,ff,um,ww,-ETA*resid)
        for p0 in ffam["highest"]:
            for k0 in range(max(0,deg(p0,2))+1):
                need(evaluate_mod_poly(coeff(p0,2,k0),zero,sp,zero,h)==0,
                     "Every boundary highest coefficient vanishes modulo h")
        rr=eta_resultant(ffam["second"][0],ffam["second"][1])
        bgates[label]=quotient_gate(rr,zero,sp,zero,h,"s=-1 "+label)
    bdegree={"s2_t2_r":[1,1,1],"s_t3_r":[1,1,1],
             "s_t2_r2":[0,1,1],"t3_r2":[1,1,1]}[args.label]
    need([bgates[x]["valueDegree"] for x in ("finite_finite","infinity_finite","finite_infinity")]==bdegree,
         "All exact boundary quotient degrees")

    dgates={}
    if args.label=="s2_t2_r":
        # No irreducibility or separability claim about D is needed for the quotient proof.
        a3=sp+1;a2=-3*sp**2-3*sp-5
        a1=sp**3-3*sp**2+22*sp;a0=sp**3-5*sp**2
        disc=a2*a2*a1*a1-4*a3*a1**3-4*a2**3*a0-27*a3*a3*a0*a0+18*a3*a2*a1*a0
        need(disc==sp*sp*D,"Complete original cubic discriminant")
        inva3=inverse_mod_poly(a3,D)
        denominator=2*(a2*a2-3*a3*a1)
        invden=inverse_mod_poly(denominator,D)
        alpha=((9*a3*a0-a2*a1)*invden)%D
        dbeta=(-a2*inva3-2*alpha)%D
        need((a3*(-2*alpha-dbeta)-a2)%D==0,"D factorization z^2")
        need((a3*(alpha*alpha+2*alpha*dbeta)-a1)%D==0,"D factorization z")
        need((-a3*alpha*alpha*dbeta-a0)%D==0,"D factorization constant")
        for difference in (alpha-dbeta,sp-alpha,sp-dbeta):
            inverse_mod_poly(difference,D)
        for tv,rv,label in [(alpha,alpha,"double_double"),(alpha,dbeta,"double_simple"),(dbeta,alpha,"simple_double")]:
            need(evaluate_mod_poly(qt,sp,tv,rv,D)==0,label+": original first root")
            need(evaluate_mod_poly(dt,sp,tv,rv,D)==0,label+": original second root")
        for zdegree in range(6):
            want=coeff(f,3,zdegree)+coeff(kexpr,3,zdegree)*0
            value=evaluate_mod_poly(coeff(f,3,zdegree),sp,alpha,dbeta,D)
            kvalue=evaluate_mod_poly(coeff(kexpr,3,zdegree),sp,alpha,dbeta,D)
            need((value+kvalue*inva3)%D==0,"D survivor f=-k/a3 at every coefficient")
        dgates={"reversedSimpleDouble":quotient_gate(r01,sp,dbeta,alpha,D,"D reversed simple-double"),
                "factorizationAndAllDenominatorInversesVerified":True,
                "doubleDoubleDelegatesToRegistered23":True,
                "doubleSimpleIsPhysicalSurvivor":True}
        need(dgates["reversedSimpleDouble"]["valueDegree"]==7,"Degree seven reversed D gate")
    # Remaining 0 and infinity fibers are literal divisor reductions listed in
    # the proof; these checks verify the original cubic and their survivor.
    need(qz.subs({"s":0})==Z**2*(Z-5),"Original s=0 cubic")
    need(coeff(qt,0,3)==T+1 and coeff(qt,1,3)==S+1,"Original projective cubic boundaries")
    zero_table={"s2_t2_r":["E5","S","E32"],"s_t3_r":["E5","S","E23"],
                "s_t2_r2":["E5","E32","E32"],"t3_r2":["E5","E32","E23"]}[args.label]
    if zero_table[1]=="S":
        uz=[CTX.constant(1)]+[ZERO]*5;kz=zpoly(scalar_mv(K,uz))
        need(f.subs({"s":0,"t":0,"r":5})==-kz,"s=0 literal physical survivor")
        physical_survivor_gate(family(ki,ji,-kz,uz,-kz*kz,ZERO),"s=0 physical survivor")
    # A generic physical rank-one family is checked directly, not only on
    # the finitely many exceptional roots.
    physical_survivor_gate(family(ki,ji,-kexpr,u,-kexpr*kexpr,ZERO),"generic physical survivor")
    emit({"stage":"complete","label":args.label,"elapsedSeconds":time.monotonic()-started,
      "sourceSHA256":hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
      "QQNormDegrees":[A.degree(),B.degree()],"QQCofactorDegrees":[A0.degree(),B0.degree()],
      "cofactorSylvesterDimension":len(smat),"cofactorSylvesterDetMod1009":det,
      "sMinusOneBoundaryUnitGates":bgates,"DQuotientGates":dgates,
      "sZeroAndInfinityReductionTable":zero_table,
      "fullGradientHash":phash(fam["second"]+fam["mean"]),
      "highestFullResidualHash":phash(fam["highest"]),
      "allOriginalVContributionsRetained":True,"completeRankOneClassificationVerified":True,
      "ordinaryISPClaim":False,"globalMatchedBellClaim":False,
      "recoveryNote":"Reconstructed after executor loss. This execution belongs to this exact source SHA."})
if __name__=="__main__":main()

