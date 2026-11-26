#!/usr/bin/env python3
"""Exact original rank-two V/aligned-mean pencil branch, including infinity.
No scalar sampling or changed quadratic form is used.
"""
import argparse, hashlib, json, math, resource, signal, time
from pathlib import Path
from flint import fmpq, fmpq_mat, fmpq_poly, fmpq_mpoly_ctx, nmod_mat

MOD=1009
K=[[0,0,0,0,5,-1],[0,0,0,-32,5,-1],[0,0,54,-4,5,0],
   [0,-32,-4,-8,0,0],[5,5,5,0,0,0],[-1,-1,0,0,0,0]]
C=fmpq_mpoly_ctx.get(("s","t","b","l"),"lex")
S,T,B,L=C.gens();ZERO=C.constant(0)

def need(ok,msg):
    if not ok:raise AssertionError(msg)

def dot(a,b):return sum((x*y for x,y in zip(a,b)),ZERO)
def mv(a,b):return [dot(row,b) for row in a]
def mm(a,b):
    return [[sum((a[i][k]*b[k][j] for k in range(len(b))),ZERO)
             for j in range(len(b[0]))] for i in range(len(a))]
def tr(a):return sum((a[i][i] for i in range(len(a))),ZERO)
def outer(a,b):return [[x*y for y in b] for x in a]
def madd(a,b):return [[x+y for x,y in zip(r,rr)] for r,rr in zip(a,b)]
def mscale(a,c):return [[x*c for x in row] for row in a]
def anti(a):
    return [sum((a[i][j] for i in range(6) for j in range(6) if i+j==m),ZERO)
            for m in range(11)]
def coeff(p,idx,k):
    out={}
    for e,c in p.to_dict().items():
        if e[idx]==k:
            ee=list(e);ee[idx]=0;out[tuple(ee)]=c
    return C.from_dict(out)
def deg(p,idx):return max((int(e[idx]) for e in p.to_dict()),default=-1)
def prec(p):return [[list(map(int,e)),str(c)] for e,c in sorted(p.to_dict().items())]
def phash(polys):
    return hashlib.sha256(json.dumps(list(map(prec,polys)),
        separators=(",",":"),ensure_ascii=True).encode()).hexdigest()
def uhash(polys):
    return hashlib.sha256(json.dumps([[str(c) for c in p.coeffs()] for p in polys],
        separators=(",",":")).encode()).hexdigest()
def primitive(p):
    """Primitive integer polynomial with positive lex-leading coefficient."""
    ds=p.to_dict();need(bool(ds),"Nonzero primitive polynomial")
    den=math.lcm(*[int(c.q) for c in ds.values()])
    gg=math.gcd(*[int(c.p)*(den//int(c.q)) for c in ds.values()])
    scale=fmpq(den,gg)
    if ds[max(ds)]<0:scale=-scale
    out=p*scale
    need(all(int(c.q)==1 for c in out.to_dict().values()),"Integral primitive coefficients")
    need(math.gcd(*[abs(int(c.p)) for c in out.to_dict().values()])==1,"Primitive content one")
    return out
def univariate(p):
    need(all(not any(e[1:]) for e in p.to_dict()),"Exact univariate s polynomial")
    out=[fmpq(0)]*(deg(p,0)+1)
    for e,c in p.to_dict().items():out[int(e[0])]=c
    return fmpq_poly(out)
def modq(c):
    c=fmpq(c);den=int(c.q)%MOD
    need(den!=0,"Every rational coefficient denominator is a 1009 unit")
    return int(c.p)%MOD*pow(den,-1,MOD)%MOD
def sylvester(a,b):
    m,n=len(a)-1,len(b)-1
    need(a[-1] and b[-1],"Both exact degrees preserved after reduction")
    out=[[0]*(m+n) for _ in range(m+n)]
    for j in range(n):
        for i,c in enumerate(a):out[i+j][j]=c
    for j in range(m):
        for i,c in enumerate(b):out[i+j][n+j]=c
    return out
def full_gate(a,b,expected):
    need(a.gcd(b).degree()==0,"Exact QQ gcd is one")
    aa,bb=[[modq(c) for c in p.coeffs()] for p in (a,b)]
    matrix=sylvester(aa,bb)
    det=int(nmod_mat(matrix,MOD).det())
    need(det==expected and det!=0,"Complete Sylvester determinant, no submatrix")
    return {"degrees":[int(a.degree()),int(b.degree())],
            "dimension":len(matrix),"detMod1009":det,
            "QQGcdDegree":0,"polynomialSHA256":uhash([a,b])}

def original_family(Jinverse,infinity=False):
    u=[S**i for i in range(6)]
    v=[ZERO]*5+[C.constant(1)] if infinity else [T**i for i in range(6)]
    pu,pv=mv(K,u),mv(K,v)
    ab=[sum((pu[i]*pv[j] for i in range(6) for j in range(6) if i+j==m),ZERO)
        for m in range(11)]
    bseq=[sum((Jinverse[m,n]*ab[n] for n in range(11)),ZERO) for m in range(11)]
    Hcross=[[bseq[i+j] for j in range(6)] for i in range(6)]
    need(anti(mm(mm(K,Hcross),K))==ab,"All original J2 inverse identities")
    uu,vv=outer(u,u),outer(v,v)
    base=madd(uu,mscale(vv,B*B))
    H=mscale(base,fmpq(1,2)-L)
    H=madd(H,mscale(Hcross,L*B))
    y=[x+B*z for x,z in zip(u,v)];p=mv(K,y)
    hs=[H[min(m,5)][m-min(m,5)] for m in range(11)]
    need(all(H[i][j]==hs[i+j] for i in range(6) for j in range(6)),"Full physical Hankel H")
    c=(1-3*L)/2;d=c*B**3
    V=[]
    for m in range(16):
        i=min(m,5);j=min(m-i,5);k=m-i-j
        V.append(c*u[i]*u[j]*u[k]+d*v[i]*v[j]*v[k])
    need(all(V[i+j+k]==c*u[i]*u[j]*u[k]+d*v[i]*v[j]*v[k]
        for i in range(6) for j in range(6) for k in range(6)),"Full physical rank-two V")
    KH=mm(K,H);KHK=mm(KH,K);HKH=mm(mm(H,K),H)
    F=dot(y,p)/2;hp=mv(H,p);hkhp=mv(HKH,p)
    b0=dot(p,hp);tau2=tr(mm(KH,KH));tau3=tr(mm(mm(KH,KH),KH))
    need(tr(KH)==0,"Original physical trace relation")
    Ps,Pt=dot(p,u),dot(p,v);Gs,Gt=dot(u,mv(KHK,u)),dot(v,mv(KHK,v))
    cross=dot(u,pv)
    need(dot(u,pu)==0 and dot(v,pv)==0,"Original self-isotropy at both projective points")
    Gamma=[(F*F-2*b0+2*tau2)*y[i]-4*F*hp[i]+8*hkhp[i]
        +4*c*(Ps*Ps-2*Gs)*u[i]+4*d*(Pt*Pt-2*Gt)*v[i] for i in range(6)]
    N=[[F*y[i]*y[j]-2*F*H[i][j]-2*(y[i]*hp[j]+hp[i]*y[j])+4*HKH[i][j]
         +4*c*Ps*u[i]*u[j]+4*d*Pt*v[i]*v[j] for j in range(6)] for i in range(6)]
    ns=anti(mm(mm(K,N),K));G=anti(KHK)
    highest=[]
    for m in range(16):
        p3=sum((p[i]*p[j]*p[k] for i in range(6) for j in range(6)
            for k in range(6) if i+j+k==m),ZERO)
        pg=sum((p[i]*G[m-i] for i in range(6) if 0<=m-i<=10),ZERO)
        vp=sum((c*pu[i]*pu[j]*pu[k]+d*pv[i]*pv[j]*pv[k]
            for i in range(6) for j in range(6) for k in range(6) if i+j+k==m),ZERO)
        highest.append(p3-6*pg+4*vp)
    need(not any(highest),"All sixteen original highest equations")
    G6=F**3-6*F*b0+6*F*tau2+12*dot(p,hkhp)-8*tau3
    Q=G6+4*c*(Ps**3-6*Ps*Gs)+4*d*(Pt**3-6*Pt*Gt)+16*c*d*cross**3
    need(Q==G6-16*c*d*cross**3,"Complete Q3, including V-linear and V-quadratic terms")
    for name in ("s","t","b","l"):
        full_chain=3*dot(mv(K,Gamma),[x.derivative(name) for x in y])
        full_chain-=6*dot(ns,[x.derivative(name) for x in hs])
        full_chain+=4*dot(highest,[x.derivative(name) for x in V])
        need(Q.derivative(name)==full_chain,"Complete original chain rule in "+name)
    need(not any(x.subs({"l":0}) for x in Gamma+ns+highest),"All original gradients on lambda zero")
    factor=L*L*B*B*(1 if infinity else (S-T)**4)
    linear=[]
    for x in Gamma:
        q,r=divmod(x,factor)
        need(not r and deg(q,2)<=1 and deg(q,3)<=0,"Exact common mean factor and complete linear b degree")
        linear.append(q)
    aa,bb=[coeff(p,2,0) for p in linear],[coeff(p,2,1) for p in linear]
    minors={}
    for i,j in ((0,1),(0,2),(1,2),(3,4)):
        p=aa[i]*bb[j]-aa[j]*bb[i]
        if not infinity:
            p,rem=divmod(p,S-T);need(not rem,"Exact additional alternating factor")
        minors[i,j]=primitive(p)
    return {"minors":minors,"gradientHash":phash(Gamma+ns+highest),
            "linearMeanHash":phash(linear),"fullQHash":phash([Q])}

def main():
    ap=argparse.ArgumentParser();ap.add_argument("--wall-seconds",type=int,default=240)
    args=ap.parse_args()
    resource.setrlimit(resource.RLIMIT_AS,(1536*1024**2,)*2)
    def timeout(sig,frame):raise TimeoutError("Exact QQ budget exhausted")
    signal.signal(signal.SIGALRM,timeout);signal.alarm(args.wall_seconds)
    start=time.monotonic()
    J=[[0]*11 for _ in range(11)]
    for i in range(6):
     for j in range(6):
      for a in range(6):
       for b in range(6):J[i+a][j+b]+=K[i][j]*K[a][b]
    need(fmpq_mat(K).det()==-25600,"Original det K")
    need(fmpq_mat(J).det()==-64701092257700249600,"Original det J2")
    ji=fmpq_mat(J).inv()
    need(fmpq_mat(J)*ji==fmpq_mat([[int(i==j) for j in range(11)] for i in range(11)]),"Exact original inverse")
    finite=original_family(ji,False);mi=finite["minors"]
    need(all(deg(p,0)==deg(p,1)==16 for p in mi.values()),"All selected primitive minors have bidegree 16,16")
    norms=[univariate(mi[x].resultant(mi[y],"t"))
        for x,y in [((0,1),(0,2)),((1,2),(3,4))]]
    need(all(p.degree()==512 for p in norms),"Both exact norm degrees 512")
    finite_gate=full_gate(norms[0],norms[1],802)
    infinity=original_family(ji,True);imi=infinity["minors"]
    infpair=[univariate(imi[x]) for x in ((0,1),(0,2))]
    need(all(p.degree()==16 for p in infpair),"Both infinity minors have degree 16")
    infinity_gate=full_gate(infpair[0],infpair[1],78)
    print(json.dumps({"stage":"complete","elapsedSeconds":time.monotonic()-start,
      "sourceSHA256":hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
      "finiteMeanGate":finite_gate,"infinityMeanGate":infinity_gate,
      "finiteFullGradientSHA256":finite["gradientHash"],
      "infinityFullGradientSHA256":infinity["gradientHash"],
      "finiteLinearMeanSHA256":finite["linearMeanHash"],
      "infinityLinearMeanSHA256":infinity["linearMeanHash"],
      "completeQ3ChainRuleVerified":True,"allOriginalVTermsRetained":True,
      "allOriginalGradientsAtLambdaZeroVerified":True,
      "alignedRankTwoBranchClassified":True,"allRankTwoVClaim":False,
      "ordinaryISPClaim":False},sort_keys=True),flush=True)
if __name__=="__main__":main()

