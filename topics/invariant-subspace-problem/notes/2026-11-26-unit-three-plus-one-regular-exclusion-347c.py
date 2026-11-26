#!/usr/bin/env python3
"""Exact QQ elimination of the original regular unit3+1 critical branch.
AI-assisted GPT-6 Astra Pro, Astra-ISP-347c-20261126 / unit31_general.
Original Frobenius algebra, all active mean coefficients, local cubic/quadratic
jet compatibility and isolated active-point compatibility are rebuilt below.
The previously verified x=0 and L=0 boundaries are not rerun here.
No numerical tests, finite-field lifting, stored polynomial arrays or GB input.
Dependencies: SymPy and python-flint 0.9.0. All generated arrays stay in RAM.
"""
import argparse
import hashlib
import json
import resource
import signal
from pathlib import Path
from time import monotonic
ap=argparse.ArgumentParser()
ap.add_argument('--wall-seconds',type=int,default=180)
ap.add_argument('--memory-mib',type=int,default=1024)
args=ap.parse_args()
assert 1<=args.wall_seconds<=600 and 256<=args.memory_mib<=4096
resource.setrlimit(resource.RLIMIT_AS,(args.memory_mib*1024**2,)*2)
def timed_out(signum,frame):raise TimeoutError('Fixed exact-elimination wall budget')
signal.signal(signal.SIGALRM,timed_out)
signal.alarm(args.wall_seconds)
import sympy as S
from flint import fmpq, fmpq_mpoly_ctx
started=monotonic()
b,x,k,B,q,s=S.symbols("b x kappa B q s")
one=S.Matrix([1,0,0,1])
def clean(z):return S.cancel(S.expand(z))
def eq(z,w=0):assert clean(z-w)==0,(z,w)
def amul(z,w):
    return S.Matrix([z[0]*w[0],z[0]*w[1]+z[1]*w[0],
                     z[0]*w[2]+z[1]*w[1]+z[2]*w[0],z[3]*w[3]])
a=1-b;delta=1-2*b
A=x-b;r=x*(1+k)-delta/2;C=b*(delta+k*(1-2*x))
K=S.Matrix([[0,0,A,1],[0,-2*A,B,q],[A,B,C,r],[1,q,r,0]])
def tau(z):return a*z[0]+z[2]+b*z[3]
def DK(z):return S.Matrix([tau(amul(K.row(i).T,z)) for i in range(4)])
d=DK(one);F=tau(d)/2
def cen(z):return z-tau(z)*one
def pv(z):
    zz=cen(z);return clean(tau(amul(zz,amul(zz,zz)))/2)
def pj(z,w):return clean(3*tau(amul(amul(cen(z),cen(z)),cen(w)))/2)
def nv(z):
    return clean(tau(amul(d-F*one,amul(z,z)))/2
                 -tau(z)*tau(amul(d,z))+F*tau(z)**2
                 +tau(amul(z,DK(z)))/4)
def nj(z,w):
    return clean(tau(amul(d-F*one,amul(z,w)))
                 -tau(z)*tau(amul(d,w))-tau(w)*tau(amul(d,z))
                 +2*F*tau(z)*tau(w)+tau(amul(z,DK(w)))/2)
rows=[K.row(i).T for i in range(4)]
ev=S.Matrix([tau(amul(rows[0],rows[0])),
             2*tau(amul(rows[0],rows[1])),
             2*tau(amul(rows[0],rows[2]))+tau(amul(rows[1],rows[1])),
             tau(amul(rows[3],rows[3]))])
mean=[clean(z) for z in ev-2*DK(d)-2*amul(d,d)+4*F*d]
alpha=x+b*(k-2);beta0=S.Rational(1,2)-k*x
eq(F,x+b*k/2);eq(mean[0])
eq(mean[1],2*(alpha*(B+b*q)+b*beta0*q))
R2=clean(mean[2].subs({B:0,q:0},simultaneous=True))
RP=clean(mean[3].subs({B:0,q:0},simultaneous=True))
eq(mean[2],R2-4*B*B-6*b*B*q+b*delta*q*q)
eq(mean[3],RP-2*B*q+delta*q*q)
p0=pv(K[:,0]);p1=pj(K[:,0],K[:,1])
p2=clean(pj(K[:,0],K[:,2])
         +3*tau(amul(cen(K[:,0]),amul(cen(K[:,1]),cen(K[:,1]))))/2)
n0=nv(K[:,0]);n1=nj(K[:,0],K[:,1])
n2=clean(nv(K[:,1])+nj(K[:,0],K[:,2]))
c0=clean(3*p0*n1-2*n0*p1)
c1=clean(6*p0*n2+p1*n1-4*n0*p2)
cb=clean(S.diff(c0,B));cq=clean(S.diff(c0,q))
eq(c0,cb*B+cq*q)

c0s=clean(c0.subs(B,(s-b)*q)/q)
eq(c0s,3*(p0*(x-b)*(2*x*s-b)+n0*(2*x*x-b)*(x-s)))
cq=S.Poly(clean(c1.subs(B,(s-b)*q)),q,domain=S.QQ.frac_field(b,x,k,s))
assert cq.degree()<=2
eq(cq.nth(1))



# Original scalar values at the active reduced point. Every actual candidate has
# chi = n0^3*ps^2 - ns^3*p0^2 = 0, since p=-u^3 and n=-m*u^2 at both points.
ps=pv(K[:,3]);ns=nv(K[:,3])
pq=S.Poly(clean(ps.subs(B,(s-b)*q)),q,domain=S.QQ.frac_field(b,x,k,s))
nq=S.Poly(clean(ns.subs(B,(s-b)*q)),q,domain=S.QQ.frac_field(b,x,k,s))
assert pq.degree()<=2 and nq.degree()<=2
eq(pq.nth(1));eq(nq.nth(1))

# Work from here in QQ(b,x), using sparse native exact polynomials.
ctx=fmpq_mpoly_ctx.get(('b','x'),'lex')
fb,fx=ctx.gens();onep=ctx.constant(1);zerop=ctx.constant(0)
def poly(expr):
    return ctx.from_dict({e:fmpq(str(c)) for e,c in S.Poly(expr,b,x,domain=S.QQ).terms()})
def rd(n,d=onep):
    assert d
    if not n:return (zerop,onep)
    g=n.gcd(d)
    return (n/g,d/g)
def add(A,B):return rd(A[0]*B[1]+B[0]*A[1],A[1]*B[1])
def mul(A,B):return rd(A[0]*B[0],A[1]*B[1])
def inv(A):return rd(A[1],A[0])
def neg(A):return (-A[0],A[1])
def pw(A,n):return (A[0]**n,A[1]**n)
def scale(A,c):return (fmpq(c)*A[0],A[1])
def integer_num(A):
    # Unique primitive integer numerator, with positive lex leading coefficient.
    dd=A[0].to_dict();den=1
    from math import lcm,gcd
    for v in dd.values():den=lcm(den,int(v.q))
    vals={e:int(v.p)*(den//int(v.q)) for e,v in dd.items()}
    content=0
    for v in vals.values():content=gcd(content,abs(v))
    assert content
    if vals[max(vals)]<0:content=-content
    return ctx.from_dict({e:v//content for e,v in vals.items()})
def degree(P,j):return max((int(e[j]) for e in P.to_dict()),default=-1)
def sh(P):return hashlib.sha256(str(P).encode()).hexdigest()
L=poly(-4*b**3+(16*x*x+x+1)*b*b-20*x**3*b+4*x**4*(x+1))
Cb=poly((S.Rational(5,2)-4*x)*b*b+(6*x*x-4*x)*b-6*x**4+4*x**3)
SR=rd(-fb*Cb,L)
# All divisions here are the already-paid b != 0, s-x != 0 and 1-2s != 0.
KR=mul(add(mul(SR,rd(2*fb-fx)),rd(-fb/2)),
       inv(mul(rd(fb),add(SR,rd(-fx)))))

def evaluate(expr):
    P=S.Poly(expr,b,x,k,s,domain=S.QQ)
    terms=P.terms();ak=max((e[2] for e,c in terms),default=0)
    ass=max((e[3] for e,c in terms),default=0)
    kp=[KR[0]**i for i in range(ak+1)]
    kd=[KR[1]**i for i in range(ak+1)]
    sp=[SR[0]**i for i in range(ass+1)]
    sd=[SR[1]**i for i in range(ass+1)]
    out=zerop
    for (ib,ix,ik,is_),c in terms:
        out+=fmpq(str(c))*fb**ib*fx**ix*kp[ik]*kd[ak-ik]*sp[is_]*sd[ass-is_]
    return rd(out,KR[1]**ak*SR[1]**ass)
R2r,RPr=evaluate(R2),evaluate(RP)
gamma_ratio=add(rd(onep),scale(SR,-2))
Q2=mul(neg(RPr),inv(gamma_ratio))
M=integer_num(add(R2r,mul(evaluate(b*(1+2*s)-4*s*s),Q2)))
C=integer_num(add(evaluate(cq.nth(0)),mul(evaluate(cq.nth(2)),Q2)))
Psr=add(evaluate(pq.nth(0)),mul(evaluate(pq.nth(2)),Q2))
Nsr=add(evaluate(nq.nth(0)),mul(evaluate(nq.nth(2)),Q2))
Chi=add(mul(pw(evaluate(n0),3),pw(Psr,2)),
        neg(mul(pw(Nsr,3),pw(evaluate(p0),2))))
Xfull=integer_num(Chi)
# p0 is already nonzero. Exact division reduces the degree; it is a verified
# identity over QQ[b,x], not removal of an unverified resultant factor.
P0=integer_num(evaluate(p0))
Xraw,rem=divmod(Xfull,P0**2)
assert not rem
X=integer_num((Xraw,onep))
assert [(degree(P,0),degree(P,1)) for P in (M,C,X)]==[(13,22),(15,26),(42,75)]
print(json.dumps({'stage':'original_polynomials_constructed','degrees':[[degree(P,0),degree(P,1)] for P in (M,C,X)],'elapsedSeconds':round(monotonic()-started,6)}),flush=True)
# Complete native characteristic-zero resultants. A common finite b-root gives
# zero even in fibers where the formal b-degree drops; only necessity is used.
RMC=M.resultant(C,'b')
RMX=M.resultant(X,'b')
assert degree(RMC,0)==degree(RMX,0)==0
assert (degree(RMC,1),degree(RMX,1))==(395,1142)
GG=RMC.gcd(RMX)
expected=fx**193*(fx-fmpq(1,2))**172*(fx+1)**6*(fx+fmpq(15,8))
assert GG==expected
fibers=[]
for xv,want in [(fmpq(0),fb**9),(fmpq(1,2),(fb-fmpq(1,2))**11),
                (fmpq(-1),fb**2),(fmpq(-15,8),fb+fmpq(25,64))]:
    mm=M.subs({'x':xv});cc=C.subs({'x':xv});xx=X.subs({'x':xv})
    gg=mm.gcd(cc).gcd(xx)
    assert gg==want
    fibers.append({'x':str(xv),'monicBPolynomial':str(gg),'sha256':sh(gg)})
# The only nonforbidden b-value returns to the already-excluded gamma=0 boundary.
def value(A,bv,xv):
    nn=A[0].subs({'b':bv,'x':xv});dd=A[1].subs({'b':bv,'x':xv})
    assert dd
    val=nn/dd
    assert all(e==(0,0) for e in val.to_dict())
    return val.to_dict().get((0,0),fmpq(0))
bv,xv=fmpq(-25,64),fmpq(-15,8)
assert value(SR,bv,xv)==fmpq(1,2)
assert value(KR,bv,xv)==fmpq(-4,5)
assert value(evaluate(alpha),bv,xv)==fmpq(-25,32)
assert value(gamma_ratio,bv,xv)==0
record={
 'schema':'r150-unit31-regular-characteristic-zero-exclusion-20261126-v1',
 'sourceSha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
 'status':'all_pass_original_regular_unit31_branch_empty',
 'scope':'Prior p0/half/alpha0/q0/gamma0/x0/L0 exclusions plus this general chart close the complete active-unit-3+1 isolated-zero rank-four branch.',
 'inputDegrees':[[degree(P,0),degree(P,1)] for P in (M,C,X)],
 'resultantDegrees':[degree(RMC,1),degree(RMX,1)],
 'resultantGcd':'x^193*(x-1/2)^172*(x+1)^6*(x+15/8)',
 'polynomialSha256':{k:sh(v) for k,v in [('M',M),('C',C),('X',X),('RMC',RMC),('RMX',RMX),('gcd',GG)]},
 'fiberChecks':fibers,
 'lastCandidate':{'b':'-25/64','x':'-15/8','s':'1/2','kappa':'-4/5','alpha':'-25/32','gamma':'0'},
 'ordinaryISPClaim':False,
 'globalMatchedBellClaim':False,
 'elapsedSeconds':round(monotonic()-started,6),
 'peakRssKiB':resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
}
signal.alarm(0)
print(json.dumps(record,sort_keys=True,ensure_ascii=False),flush=True)
