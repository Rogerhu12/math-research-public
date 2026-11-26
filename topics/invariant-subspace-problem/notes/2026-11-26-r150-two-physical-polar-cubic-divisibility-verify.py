#!/usr/bin/env python3
"""Exact original two-point polar divisibility: all common-factor absorptions excluded."""
import hashlib, heapq, json, math, resource, signal, time
from pathlib import Path
from flint import fmpq,fmpq_mat,fmpq_poly,fmpq_mpoly_ctx

K=[[0,0,0,0,5,-1],[0,0,0,-32,5,-1],[0,0,54,-4,5,0],
   [0,-32,-4,-8,0,0],[5,5,5,0,0,0],[-1,-1,0,0,0,0]]
def need(ok,msg):
    if not ok:raise AssertionError(msg)
def digest(obj):
    return hashlib.sha256(json.dumps(obj,sort_keys=True,separators=(",",":")).encode()).hexdigest()
def urec(p):return [str(c) for c in p.coeffs()]
def mrec(p):return [[list(map(int,e)),str(c)] for e,c in sorted(p.to_dict().items())]
def invmod(a,m):
    aa=a%m;g,u,v=aa.xgcd(m)
    need(g.degree()==0 and g[0]!=0,"Exact QQ quotient element is a unit")
    ans=(u/g[0])%m
    need((aa*ans)%m==1,"Exact QQ quotient inverse remultiplication")
    return ans
def base_unit(a,m,label):
    a=a%m;iv=invmod(a,m)
    return {"label":label,"valueDegree":int(a.degree()),"inverseDegree":int(iv.degree()),
        "valueSHA256":digest(urec(a)),"inverseSHA256":digest(urec(iv)),
        "exactQQInverseVerified":True}
def qfun(s,z):
    return s**3-5*s*s+(s**3-3*s*s+22*s)*z+(-3*s*s-3*s-5)*z*z+(s+1)*z**3
def Cmatrix(x,y):
    a=-22*x*y-2*y*y+110*y
    b=5*x*x+3*x*y-25*x+3*y*y-20*y
    c=-x*x-x*y+5*x+6*y
    d=4*x*x+2*x*y-10*x+3*y*y-74*y+110
    e=-x*x-x*y+3*x+4*y-22
    f=3*x+3*y-2
    return [[a,b,c],[b,d,e],[c,e,f]]
def Dpoly(x):
    return 5*x**8+50*x**7+153*x**6-936*x**5-2888*x**4+15936*x**3-3392*x**2-25472*x+9600

class Quad:
    """Q[x]/mod [S]/(S^2-X*S+Y), retaining all algebraic roots."""
    def __init__(self,mod,X,Y):
        self.mod=mod;self.X=X%mod;self.Y=Y%mod;self.units=[]
    def poly(self,a):
        return (a if isinstance(a,fmpq_poly) else fmpq_poly([fmpq(a)]))%self.mod
    def el(self,a=0,b=0):return Elt(self,self.poly(a),self.poly(b))
    def unit(self,a,label):
        a=self.el(a) if not isinstance(a,Elt) else a
        norm=(a.a*a.a+self.X*a.a*a.b+self.Y*a.b*a.b)%self.mod
        ni=invmod(norm,self.mod)
        iv=self.el((a.a+self.X*a.b)*ni,-a.b*ni)
        need(a*iv==self.el(1),label+": exact extension-algebra inverse")
        self.units.append({"label":label,"valueDegrees":[int(a.a.degree()),int(a.b.degree())],
          "normDegree":int(norm.degree()),"valueSHA256":digest([urec(a.a),urec(a.b)]),
          "inverseSHA256":digest([urec(iv.a),urec(iv.b)]),"exactQQInverseVerified":True})
        return iv

class Elt:
    def __init__(self,A,a,b):self.A=A;self.a=a;self.b=b
    def cv(self,o):
        if isinstance(o,Elt):need(o.A is self.A,"Same exact quotient algebra");return o
        return self.A.el(o)
    def __add__(self,o):
        o=self.cv(o);return self.A.el(self.a+o.a,self.b+o.b)
    __radd__=__add__
    def __neg__(self):return self.A.el(-self.a,-self.b)
    def __sub__(self,o):return self+(-self.cv(o))
    def __rsub__(self,o):return self.cv(o)+(-self)
    def __mul__(self,o):
        o=self.cv(o);A=self.A
        return A.el(self.a*o.a-A.Y*self.b*o.b,
                    self.a*o.b+self.b*o.a+A.X*self.b*o.b)
    __rmul__=__mul__
    def __pow__(self,n):
        need(n>=0,"Nonnegative exact algebra power")
        a=self;r=self.A.el(1)
        while n:
            if n&1:r=r*a
            a=a*a;n//=2
        return r
    def __truediv__(self,o):
        need(not isinstance(o,Elt),"Only explicit rational division")
        return self*fmpq(1)/fmpq(o) if not isinstance(o,fmpq) else self.A.el(self.a/o,self.b/o)
    def __eq__(self,o):
        o=self.cv(o);return self.a==o.a and self.b==o.b

def kernel_derivatives(s,r):
    q=qfun(s,r)
    qp=(s**3-3*s*s+22*s)+2*(-3*s*s-3*s-5)*r+3*(s+1)*r*r
    qpp=2*(-3*s*s-3*s-5)+6*(s+1)*r
    delta=r-s
    return -2*delta*q-delta*delta*qp,-2*q-4*delta*qp-delta*delta*qpp

def reconstruct_bezout():
    C=fmpq_mpoly_ctx.get(("s","t","z","w"),"lex")
    s,t,z,w=C.gens();zero=C.constant(0)
    us=[s**i for i in range(6)];uz=[z**i for i in range(6)]
    original=sum((K[i][j]*us[i]*uz[j] for i in range(6) for j in range(6)),zero)
    need(original==-(z-s)**2*qfun(s,z),"Original integer K polar")
    cm=Cmatrix(s+t,s*t)
    bez=sum((cm[i][j]*z**i*w**j for i in range(3) for j in range(3)),zero)
    need((z-w)*(s-t)*bez==qfun(s,z)*qfun(t,w)-qfun(s,w)*qfun(t,z),
         "Every original Bezout entry in symmetric coordinates")
    need(fmpq_mat([[0,0,-5,1],[0,22,-3,1],[-5,-3,-3,0],[1,1,0,0]]).det()==70,
         "The cubic polar q_s map is projectively injective")

def ideal_membership_certificate():
    """Buchberger reductions with full original-nine-minor source vectors."""
    C=fmpq_mpoly_ctx.get(("y","x"),"lex");y,x=C.gens();zero=C.constant(0)
    cm=Cmatrix(x,y);pairs=[(0,1),(0,2),(1,2)]
    original=[cm[i][k]*cm[j][l]-cm[i][l]*cm[j][k]
        for i,j in pairs for k,l in pairs]
    R=5625*x**6+133500*x**5-4199425*x**4-20097000*x**3+552703580*x*x-2368188240*x+2670407168
    Y=25936129306752*y-6180112125*x**5-180053635650*x**4+3709363462025*x**3+40817348451590*x*x-381660394838648*x+543614604518656
    n=len(original);basis=[];reps=[];leads=[];queue=[];processed=0
    def term(e,c):return C.from_dict({tuple(e):c})
    def lead(p):
        d=p.to_dict();e=max(d);return tuple(map(int,e)),d[e]
    def divides(a,b):return all(i<=j for i,j in zip(a,b))
    def reduce_poly(p,rep):
        work=p;out=zero;rep=list(rep)
        while work:
            e,c=lead(work)
            for j,(ee,cc) in enumerate(leads):
                if divides(ee,e):
                    q=term([e[k]-ee[k] for k in range(2)],c/cc)
                    work-=q*basis[j]
                    rep=[a-q*b for a,b in zip(rep,reps[j])]
                    break
            else:
                lt=term(e,c);out+=lt;work-=lt
        return out,rep
    def add_poly(p,rep):
        p,rep=reduce_poly(p,rep)
        if not p:return
        lc=lead(p)[1];p=p/lc;rep=[a/lc for a in rep]
        need(p==sum((a*b for a,b in zip(rep,original)),zero),"Every new basis row has original-minor source identity")
        k=len(basis);basis.append(p);reps.append(rep);leads.append(lead(p))
        for j in range(k):
            ee=tuple(max(a,b) for a,b in zip(leads[j][0],leads[k][0]))
            heapq.heappush(queue,(sum(ee),ee,j,k))
    for i,p in enumerate(original):
        rep=[zero]*n;rep[i]=C.constant(1);add_poly(p,rep)
    def target_rep(p):
        rem,negative=reduce_poly(p,[zero]*n)
        return rem,[-v for v in negative]
    done=None
    while True:
        rr,rc=target_rep(R);yr,yc=target_rep(Y)
        if not rr and not yr:
            need(R==sum((a*b for a,b in zip(rc,original)),zero),"Original-nine-minor identity for sextic R6")
            need(Y==sum((a*b for a,b in zip(yc,original)),zero),"Original-nine-minor identity for linear Y relation")
            done=(rc,yc);break
        need(queue and len(basis)<80 and processed<1600,"Finite source-certificate budget")
        _,ee,i,j=heapq.heappop(queue);processed+=1
        ei,ci=leads[i];ej,cj=leads[j]
        if all(min(a,b)==0 for a,b in zip(ei,ej)):continue
        mi=term([ee[k]-ei[k] for k in range(2)],1/ci)
        mj=term([ee[k]-ej[k] for k in range(2)],1/cj)
        add_poly(mi*basis[i]-mj*basis[j],[mi*a-mj*b for a,b in zip(reps[i],reps[j])])
    return {"originalMinorCount":n,"basisRowsUsed":len(basis),"pairsProcessed":processed,
        "sexticMembershipVerified":True,"linearRelationMembershipVerified":True,
        "sourceMultipliersSHA256":digest([[mrec(p) for p in seq] for seq in done]),
        "noSpecializationOrRootEnumeration":True}

def nonorthogonal_gate():
    x=fmpq_poly([0,1])
    R=5625*x**6+133500*x**5-4199425*x**4-20097000*x**3+552703580*x*x-2368188240*x+2670407168
    Y=(6180112125*x**5+180053635650*x**4-3709363462025*x**3-40817348451590*x*x+381660394838648*x-543614604518656)/fmpq(25936129306752)
    Y%=R;A=Quad(R,x,Y);s=A.el(0,1);t=A.el(x,-1)
    cm=Cmatrix(x,Y);ci=invmod(cm[2][2],R)
    g0=(cm[0][2]*ci)%R;g1=(cm[1][2]*ci)%R
    A.unit(s-t,"distinct physical points")
    A.unit(A.el(cm[2][2]),"nonzero quadratic Bezout pivot")
    A.unit(A.el(x**3-5*x*x+x*x*Y-6*x*Y-5*Y*Y+32*Y),"nonorthogonal pairing")
    A.unit(A.el(g1*g1-4*g0),"two distinct common roots")
    def remnants(v):
        qa=v+1;qb=-3*v*v-3*v-5
        ell0=qb-qa*A.el(g1);ell1=qa
        want=[v**3-5*v*v,v**3-3*v*v+22*v,qb,qa]
        got=[A.el(g0)*ell0,A.el(g1)*ell0+A.el(g0)*ell1,
             ell0+A.el(g1)*ell1,ell1]
        need(want==got,"Full common quadratic divides each original q")
        # The remainder of (z-v)^2*(ell0+ell1*z) modulo z^2+g1*z+g0.
        R0=ell1*A.el(g1*g0)-(ell0-2*v*ell1)*A.el(g0)+v*v*ell0
        R1=ell1*A.el(g1*g1-g0)-(ell0-2*v*ell1)*A.el(g1)+v*v*ell1-2*v*ell0
        return R0,R1
    G0,G1=remnants(s);H0,H1=remnants(t)
    det=G0*H1-G1*H0
    A.unit(det,"residual cubic remainder determinant")
    return {"allOriginalCommonFactorIdentitiesVerified":True,"units":A.units}

def double_cross_gate():
    t=fmpq_poly([0,1]);D=Dpoly(t)
    a0=t**3-5*t*t;a1=t**3-3*t*t+22*t;a2=-3*t*t-3*t-5;a3=t+1
    inva3=invmod(a3,D);den=2*(a2*a2-3*a3*a1);idn=invmod(den,D)
    s=((9*a3*a0-a2*a1)*idn)%D;r=(-a2*inva3-2*s)%D
    need((a3*(-2*s-r)-a2)%D==0,"Original D8 double-root z^2 coefficient")
    need((a3*(s*s+2*s*r)-a1)%D==0,"Original D8 double-root z coefficient")
    need((-a3*s*s*r-a0)%D==0,"Original D8 double-root constant coefficient")
    disc=a2*a2*a1*a1-4*a3*a1**3-4*a2**3*a0-27*a3*a3*a0*a0+18*a3*a2*a1*a0
    need(disc==t*t*D,"Complete original q discriminant")
    q0=(s**3-5*s*s)%D;q1=(s**3-3*s*s+22*s)%D
    q2=(-3*s*s-3*s-5)%D;q3=(s+1)%D
    need((q0+q1*t+q2*t*t+q3*t**3)%D==0,"Symmetric original orthogonality")
    G0=-(q1+q2*t+q3*t*t)%D;G1=-(q2+q3*t)%D;G2=-q3%D
    H0=-a3*t*r%D;H1=a3*(t+r)%D;H2=-a3%D
    Gs=(G0+G1*s+G2*s*s)%D;Hs=(H0+H1*s+H2*s*s)%D
    Gp=(G1+2*G2*s)%D;Hp=(H1+2*H2*s)%D
    W=(Gs*Hp-Gp*Hs)%D
    entries=[(a3,"original cubic leading coefficient"),(den,"double-root formula denominator"),
        (s-t,"double root differs from source"),(s-r,"double root differs from simple root"),
        (r-t,"simple root differs from source"),(s*s*(s-2)*(s+6),"double root has ordinary self-contact"),
        (Gs,"first residual at double root"),(Hs,"second residual at double root"),
        (G0+G1*t+G2*t*t,"first residual at the other physical point"),
        (W,"residual quadratic Wronskian at double root")]
    return {"units":[base_unit(a,D,label) for a,label in entries],
        "allOriginalFactorIdentitiesVerified":True}

def orthogonal_triple_gate(label):
    r=fmpq_poly([0,1])
    if label=="plus":F=5*r**3-25*r*r+32*r-8;a2=-25;a1=32
    else:F=5*r**3+135*r*r+864*r+864;a2=135;a1=864
    X=-fmpq(a2,5)-r;Y=r*r+fmpq(a2,5)*r+fmpq(a1,5)
    A=Quad(F,X,Y);rr=A.el(r);s=A.el(0,1);t=A.el(X,-1)
    for a,b in [(s,t),(s,rr),(t,rr)]:
        need(qfun(a,b)==A.el(0),"Every original physical triple pairing")
        A.unit(a-b,"different physical roots")
    for v in (s,t,rr):
        A.unit(v*v*(v-2)*(v+6),"ordinary self-contact in physical triple")
    us1,us2=kernel_derivatives(s,rr);ut1,ut2=kernel_derivatives(t,rr)
    A.unit(us1,"first polar simple zero at third point")
    A.unit(ut1,"second polar simple zero at third point")
    A.unit(kernel_derivatives(s,t)[0],"first polar simple zero at second point")
    A.unit(kernel_derivatives(t,s)[0],"second polar simple zero at first point")
    A.unit(us1*ut2-us2*ut1,"residual quadratic Wronskian numerator at third point")
    return {"label":label,"allOriginalTripleIdentitiesVerified":True,"units":A.units}

def main():
    resource.setrlimit(resource.RLIMIT_AS,(1536*1024**2,)*2)
    def timeout(sig,frame):raise TimeoutError("Exact QQ budget exhausted")
    signal.signal(signal.SIGALRM,timeout);signal.alarm(240)
    start=time.monotonic();reconstruct_bezout()
    source=ideal_membership_certificate()
    nonorth=nonorthogonal_gate();double=double_cross_gate()
    triples=[orthogonal_triple_gate(label) for label in ("plus","minus")]
    print(json.dumps({"stage":"complete","elapsedSeconds":time.monotonic()-start,
        "sourceSHA256":hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        "nineMinorSourceCertificate":source,"nonorthogonalSexticGate":nonorth,
        "doubleCrossD8Gate":double,"orthogonalTripleGates":triples,
        "everyGateUsesExactQQInverseRemultiplication":True,
        "allCommonFactorAbsorptionsExcluded":True,
        "allReducedRankTwoVInsideMeanClassified":True,
        "allRankTwoVClaim":False,"ordinaryISPClaim":False},sort_keys=True),flush=True)
if __name__=="__main__":main()

