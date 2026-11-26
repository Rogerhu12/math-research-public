#!/usr/bin/env python3
"""Exact original tangent rank-two V inside-mean exclusion and D8 graph inversion."""
import hashlib,json,resource,signal,time
from pathlib import Path
from flint import fmpq,fmpq_mat,fmpq_poly,fmpq_mpoly_ctx,nmod_mat
K=[[0,0,0,0,5,-1],[0,0,0,-32,5,-1],[0,0,54,-4,5,0],
   [0,-32,-4,-8,0,0],[5,5,5,0,0,0],[-1,-1,0,0,0,0]]
MOD=1009
C=fmpq_mpoly_ctx.get(("s","a","d"),"lex");S,A,D=C.gens();ZERO=C.constant(0)
def need(ok,msg):
    if not ok:raise AssertionError(msg)
def digest(obj):
    return hashlib.sha256(json.dumps(obj,sort_keys=True,separators=(",",":")).encode()).hexdigest()
def prec(p):return [[list(map(int,e)),str(c)] for e,c in sorted(p.to_dict().items())]
def phash(pp):return digest(list(map(prec,pp)))
def dot(a,b):return sum((x*y for x,y in zip(a,b)),ZERO)
def mv(a,b):return [dot(row,b) for row in a]
def mm(a,b):
    return [[sum((a[i][k]*b[k][j] for k in range(len(b))),ZERO)
        for j in range(len(b[0]))] for i in range(len(a))]
def tr(a):return sum((a[i][i] for i in range(len(a))),ZERO)
def anti(a):
    return [sum((a[i][j] for i in range(6) for j in range(6) if i+j==m),ZERO)
        for m in range(11)]
def coeff(p,var,k):
    out={}
    for e,c in p.to_dict().items():
        if e[var]==k:
            ee=list(e);ee[var]=0;out[tuple(ee)]=c
    return C.from_dict(out)
def deg(p,var):return max((int(e[var]) for e in p.to_dict()),default=-1)
def uni(p):
    need(all(e[1]==e[2]==0 for e in p.to_dict()),"Original univariate mean minor")
    out=[fmpq(0)]*(deg(p,0)+1)
    for e,c in p.to_dict().items():out[int(e[0])]=c
    return fmpq_poly(out)
def modq(c):
    c=fmpq(c);den=int(c.q)%MOD
    need(den!=0,"All rational coefficient denominators are 1009 units")
    return int(c.p)%MOD*pow(den,-1,MOD)%MOD
def scalar(p):
    ds=p.to_dict();need(not ds or set(ds)=={(0,0,0)},"Original scalar minor")
    return ds.get((0,0,0),fmpq(0))
def invmod(a,m):
    g,u,v=a.xgcd(m);need(g.degree()==0 and g[0]!=0,"Original QQ quotient unit")
    ans=(u/g[0])%m;need((a*ans)%m==1,"Exact inverse remultiplication")
    return ans
def discriminant_graph_gate():
    t=fmpq_poly([0,1])
    dd=5*t**8+50*t**7+153*t**6-936*t**5-2888*t**4+15936*t**3-3392*t*t-25472*t+9600
    p0=t**3-5*t*t;p1=t**3-3*t*t+22*t;p2=-3*t*t-3*t-5;p3=t+1
    alpha=((9*p3*p0-p2*p1)*invmod(2*(p2*p2-3*p3*p1),dd))%dd
    powers=[t*0+1]
    for _ in range(7):powers.append((powers[-1]*alpha)%dd)
    matrix=fmpq_mat([[powers[j][i] for j in range(8)] for i in range(8)])
    need(matrix.det()!=0,"The first eight alpha powers form an exact QQ basis")
    inverse=matrix.inv()
    need(matrix*inverse==fmpq_mat([[int(i==j) for j in range(8)] for i in range(8)]),
         "All sixty-four inverse matrix identities")
    co=inverse*fmpq_mat([[int(i==1)] for i in range(8)])
    recovery=sum((co[i,0]*powers[i] for i in range(8)),t*0)%dd
    need(recovery==t,"Original double-root graph has polynomial inverse t=R7(alpha)")
    return {"dimension":8,"exactInverseVerified":True,"doubleRootGraphInjectiveAtEveryComplexPoint":True,
        "basisMatrixSHA256":digest([[str(matrix[i,j]) for j in range(8)] for i in range(8)]),
        "inverseMatrixSHA256":digest([[str(inverse[i,j]) for j in range(8)] for i in range(8)]),
        "recoveryPolynomialSHA256":digest([str(co[i,0]) for i in range(8)])}

def original_family(ji,J3,infinity=False):
    u=[ZERO]*5+[C.constant(1)] if infinity else [S**i for i in range(6)]
    w=[ZERO]*4+[C.constant(1),ZERO] if infinity else [ZERO]+[i*S**(i-1) for i in range(1,6)]
    pu,pw=mv(K,u),mv(K,w)
    sq=[sum((pw[i]*pw[j] for i in range(6) for j in range(6) if i+j==m),ZERO)
        for m in range(11)]
    cseq=[sum((ji[m,n]*sq[n] for n in range(11)),ZERO) for m in range(11)]
    H=[[(A*A/6+2*D)*u[i]*u[j]+A*(u[i]*w[j]+w[i]*u[j])/6+cseq[i+j]/6
        for j in range(6)] for i in range(6)]
    hs=[H[min(m,5)][m-min(m,5)] for m in range(11)]
    need(all(H[i][j]==hs[i+j] for i in range(6) for j in range(6)),"All original Hankel H entries")
    y=[A*u[i]+w[i] for i in range(6)];p=mv(K,y);c=3*D*A
    V=[]
    for m in range(16):
        i=min(m,5);j=min(m-i,5);k=m-i-j
        V.append(c*u[i]*u[j]*u[k]+D*(u[i]*u[j]*w[k]+u[i]*w[j]*u[k]+w[i]*u[j]*u[k]))
    need(all(V[i+j+k]==c*u[i]*u[j]*u[k]+D*(u[i]*u[j]*w[k]+u[i]*w[j]*u[k]+w[i]*u[j]*u[k])
        for i in range(6) for j in range(6) for k in range(6)),"All original tangent Hankel V entries")
    F=dot(y,p)/2;hp=mv(H,p);KH=mm(K,H);HKH=mm(mm(H,K),H);KHK=mm(KH,K)
    b0=dot(p,hp);tau2=tr(mm(KH,KH));tau3=tr(mm(mm(KH,KH),KH));hkhp=mv(HKH,p)
    P0,P1=dot(p,u),dot(p,w);G00=dot(u,mv(KHK,u));G01=dot(u,mv(KHK,w))
    need(P0==G00==G01==0,"Exact self-contact values, after retaining all original terms")
    Gamma=[(F*F-2*b0+2*tau2)*y[i]-4*F*hp[i]+8*hkhp[i]+4*c*(P0*P0-2*G00)*u[i]
        +4*D*((2*P0*P1-4*G01)*u[i]+(P0*P0-2*G00)*w[i]) for i in range(6)]
    N=[[F*y[i]*y[j]-2*F*H[i][j]-2*(y[i]*hp[j]+hp[i]*y[j])+4*HKH[i][j]
        +4*(c*P0+D*P1)*u[i]*u[j]+4*D*P0*(u[i]*w[j]+w[i]*u[j]) for j in range(6)] for i in range(6)]
    ns=anti(mm(mm(K,N),K));G=anti(KHK)
    ell=[]
    for m in range(16):
        p3=sum((p[i]*p[j]*p[k] for i in range(6) for j in range(6)
            for k in range(6) if i+j+k==m),ZERO)
        pg=sum((p[i]*G[m-i] for i in range(6) if 0<=m-i<=10),ZERO)
        ell.append(p3-6*pg)
    jv=mv(J3,V);highest=[ell[i]+4*jv[i] for i in range(16)]
    need(not any(highest),"All sixteen original tangent highest equations")
    G6=F**3-6*F*b0+6*F*tau2+12*dot(p,hkhp)-8*tau3
    Q=G6+4*dot(ell,V)+8*dot(V,jv)
    need(dot(V,jv)==0 and Q==G6,"Original complete V-linear and V-quadratic values")
    for name in ("s","a","d"):
        chain=3*dot(mv(K,Gamma),[x.derivative(name) for x in y])
        chain-=6*dot(ns,[x.derivative(name) for x in hs])
        chain+=4*dot(highest,[x.derivative(name) for x in V])
        need(Q.derivative(name)==chain,"Complete original tangent chain rule in "+name)
    need(all(deg(p,1)<=1 and deg(p,2)<=0 for p in Gamma),"All six complete mean equations affine in a and independent of d")
    aa=[coeff(p,1,0) for p in Gamma];bb=[coeff(p,1,1) for p in Gamma]
    minors=[aa[0]*bb[j]-aa[j]*bb[0] for j in (1,2)]
    return {"minors":minors,"fullGradientSHA256":phash(Gamma+ns+highest),
        "meanAffineCoefficientsSHA256":phash(aa+bb),"fullQSHA256":phash([Q])}
def full_gate(a,b):
    need(a.degree()==b.degree()==32,"Both exact mean minors have degree 32")
    need(a.gcd(b).degree()==0,"Exact QQ gcd of two mean minors is one")
    am,bm=[[modq(c) for c in p.coeffs()] for p in (a,b)]
    need(am[-1] and bm[-1],"Both degree-32 leading terms survive")
    matrix=[[0]*64 for _ in range(64)]
    for j in range(32):
        for i,c in enumerate(am):matrix[i+j][j]=c
        for i,c in enumerate(bm):matrix[i+j][32+j]=c
    det=int(nmod_mat(matrix,MOD).det())
    need(det==618,"Original entire 64-order Sylvester determinant")
    return {"degrees":[32,32],"dimension":64,"detMod1009":det,
        "QQGcdDegree":0,"leadingCoefficientsMod1009":[am[-1],bm[-1]],
        "polynomialSHA256":digest([[str(c) for c in p.coeffs()] for p in (a,b)])}
def main():
    resource.setrlimit(resource.RLIMIT_AS,(1536*1024**2,)*2)
    def timeout(sig,frame):raise TimeoutError("Exact QQ budget exhausted")
    signal.signal(signal.SIGALRM,timeout);signal.alarm(240);start=time.monotonic()
    J2=[[0]*11 for _ in range(11)]
    for i in range(6):
     for j in range(6):
      for a in range(6):
       for b in range(6):J2[i+a][j+b]+=K[i][j]*K[a][b]
    need(fmpq_mat(J2).det()==-64701092257700249600,"Original det J2")
    ji=fmpq_mat(J2).inv()
    J3=[[0]*16 for _ in range(16)]
    for i in range(11):
     for j in range(11):
      for a in range(6):
       for b in range(6):J3[i+a][j+b]+=J2[i][j]*K[a][b]
    need(fmpq_mat(J3).det()==23366320238786911411830138211362846399922176000,"Original det J3")
    graph=discriminant_graph_gate()
    finite=original_family(ji,J3,False)
    gate=full_gate(*[uni(p) for p in finite["minors"]])
    infinity=original_family(ji,J3,True)
    im=modq(scalar(infinity["minors"][0]))
    need(im==45,"Original infinity two-mean coefficient determinant")
    print(json.dumps({"stage":"complete","elapsedSeconds":time.monotonic()-start,
        "sourceSHA256":hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        "doubleRootGraphGate":graph,"finiteMeanGate":gate,"infinityMeanDetMod1009":im,
        "finiteFullGradientSHA256":finite["fullGradientSHA256"],
        "infinityFullGradientSHA256":infinity["fullGradientSHA256"],
        "allOriginalVTermsRetained":True,"allOriginalChainRulesVerified":True,
        "genuineTangentMeanExcluded":True,"allRankTwoVInsideMeanNowClassified":True,
        "allRankTwoVClaim":False,"ordinaryISPClaim":False},sort_keys=True),flush=True)
if __name__=="__main__":main()

