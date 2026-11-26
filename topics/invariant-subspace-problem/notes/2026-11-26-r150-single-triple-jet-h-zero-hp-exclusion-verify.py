#!/usr/bin/env python3
"""Exact QQ verifier for the single-three-jet H, Hp=0, rankV2 reduced ess6 branch.
Rebuilds the original kernel; no finite-field emptiness inference is used.
All quotient-algebra divisions are verified QQ inverses on the full degree-16 algebra.
The proof of the reduction and the remaining H types are separate manuscript statements.
"""
import hashlib,json,time
import sympy as sy
from flint import fmpq,fmpq_poly,fmpq_mpoly_ctx
started=time.perf_counter()
def need(v,label):
 if not v:raise AssertionError(label)
def rec(f):return [str(f[i]) for i in range(int(f.degree())+1)]
def digest(v):return hashlib.sha256(json.dumps(v,separators=(',',':'),sort_keys=True).encode()).hexdigest()
s,t,w,U,V=sy.symbols('s t w U V')
K=sy.Matrix([[0,0,0,0,5,-1],[0,0,0,-32,5,-1],[0,0,54,-4,5,0],[0,-32,-4,-8,0,0],[5,5,5,0,0,0],[-1,-1,0,0,0,0]])
vec=lambda x:sy.Matrix([x**j for j in range(6)])
q=s**3-5*s*s+(s**3-3*s*s+22*s)*t-(3*s*s+3*s+5)*t*t+(s+1)*t**3
k=sy.expand((vec(s).T*K*vec(t))[0])
need(sy.expand(k+(t-s)**2*q)==0,"original K kernel factor")
f1=sy.diff(k,s);f2=sy.diff(k,s,2)/2
quad=t*t-U*t+V
r1=sy.Poly(sy.rem(f1,quad,t),t);r2=sy.Poly(sy.rem(f2,quad,t),t)
M=sy.expand(r1.nth(0)*r2.nth(1)-r1.nth(1)*r2.nth(0))
a3=s+1;J=(3*s*s+3*s+5)/a3
SS=J-w;TT=(s**3-3*s*s+22*s)/a3-w*SS
num,den=sy.fraction(sy.cancel(M.subs({U:SS,V:TT})))
need(sy.expand(num-den*M.subs({U:SS,V:TT})).cancel()==0,"original determinant numerator identity")
denfac=sy.factor(den)
qw=sy.expand(q.subs(t,w))
R=fmpq_mpoly_ctx.get(('s','w'))
to_m=lambda f:R.from_dict({m:fmpq(str(c)) for m,c in sy.Poly(f,s,w).terms()})
res=to_m(qw).resultant(to_m(num),1)
need(int(res.degrees()[1])==0,"resultant is univariate")
resu=fmpq_poly([0])
for mon,c in res.terms():
 resu+=fmpq_poly([0]*int(mon[0])+[c])
X=fmpq_poly([0,1])
bdry=X**8*(X-2)**2*(X+6)**2*(X+1)**12
raw,rem=divmod(resu,bdry);need(not rem,"exact displayed resultant boundary factor")
G=raw/raw[int(raw.degree())]
need(G.degree()==16,"entire residual algebra degree 16")
need(G.gcd(G.derivative()).degree()==0,"entire residual algebra squarefree")
units=[]
def el(a):
 if isinstance(a,fmpq_poly):return a%G
 return fmpq_poly([a])%G
one=el(1);zero=el(0)
def inv(a,label):
 a=el(a);gg,uu,vv=a.xgcd(G)
 need(gg.degree()==0 and gg[0]!=0,label+": QQ unit")
 out=(uu/gg[0])%G
 need((a*out)%G==one,label+": inverse remultiplication")
 units.append({"label":label,"valueDegree":int(a.degree()),"inverseDegree":int(out.degree()),"valueSHA256":digest(rec(a)),"inverseSHA256":digest(rec(out))})
 return out
def mul(a,b):return a*b%G
def power(a,n):
 out=one
 for _ in range(n):out=mul(out,a)
 return out
def trim(a):
 while a and not a[-1]:a.pop()
 return a
def padd(a,b):
 c=[zero for _ in range(max(len(a),len(b)))]
 for i in range(len(c)):c[i]=el((a[i] if i<len(a) else zero)+(b[i] if i<len(b) else zero))
 return trim(c)
def pmul(a,b):
 if not a or not b:return []
 c=[zero for _ in range(len(a)+len(b)-1)]
 for i,x in enumerate(a):
  for j,y in enumerate(b):c[i+j]=el(c[i+j]+mul(x,y))
 return trim(c)
def pdiv(a,b,label):
 a=list(a);need(bool(b),label+": nonzero divisor")
 if len(a)<len(b):return [],a
 ib=inv(b[-1],label+": leading coefficient")
 quo=[zero for _ in range(len(a)-len(b)+1)]
 original=list(a)
 while a and len(a)>=len(b):
  sh=len(a)-len(b);lead=mul(a[-1],ib);quo[sh]=el(quo[sh]+lead)
  for j,c in enumerate(b):a[sh+j]=el(a[sh+j]-mul(lead,c))
  trim(a)
 need(padd(pmul(b,quo),a)==trim(original),label+": exact polynomial division")
 return trim(quo),a
def from_sym(f,var):
 pp=sy.Poly(f,var)
 out=[]
 for j in range(pp.degree()+1):
  sj=sy.Poly(pp.nth(j),s)
  out.append(el(fmpq_poly([fmpq(str(sj.nth(i))) for i in range(sj.degree()+1)])) if sj else zero)
 return trim(out)
def peval(a,x):
 r=zero
 for c in reversed(a):r=el(mul(r,x)+c)
 return r
qpol=from_sym(qw,w);mpol=from_sym(num,w)
aa,bb=mpol,qpol;seq=[];step=0
while bb:
 seq.append([len(aa)-1,len(bb)-1])
 _,rr=pdiv(aa,bb,"common-root gcd step "+str(step));aa,bb=bb,rr;step+=1
need(len(aa)==2,"unique common cubic cofactor root on entire residual algebra")
wi=inv(aa[1],"common root linear coefficient")
ww=el(-mul(aa[0],wi))
need(peval(qpol,ww)==zero and peval(mpol,ww)==zero,"original two source polynomials vanish at recovered root")
sx=el(X)
a3i=inv(sx+one,"s+1")
b=el(-2*X**2*(X-2)*(X+6))
inv(b,"ordinary self-contact coefficient")
S0=el(mul(el(3*X*X+3*X+5),a3i)-ww)
T0=el(mul(el(X**3-3*X*X+22*X),a3i)-mul(ww,S0))
qp=[T0,el(-S0),one]
reconstruct=pmul([el(-ww),one],qp)
reconstruct=[mul(sx+one,c) for c in reconstruct]
need(reconstruct==qpol,"original q factorization into cofactor root and two-root quadratic")
disc=el(mul(S0,S0)-4*T0)
inv(disc,"two selected physical roots distinct")
inv(peval(qp,ww),"third cubic root distinct from selected pair")
_,rf1=pdiv(from_sym(f1,t),qp,"first-source-derivative remainder")
_,rf2=pdiv(from_sym(f2,t),qp,"second-source-derivative remainder")
rf1=(rf1+[zero,zero])[:2];rf2=(rf2+[zero,zero])[:2]
need(el(mul(rf1[0],rf2[1])-mul(rf1[1],rf2[0]))==zero,"original two-root Wronskian zero")
fp=el(mul(rf1[0],rf1[0])+mul(mul(rf1[0],rf1[1]),S0)+mul(mul(rf1[1],rf1[1]),T0))
fpi=inv(fp,"two first source derivatives product")
qsym=el(power(S0,3)-5*power(S0,2)+mul(power(S0,2),T0)-6*mul(S0,T0)+32*T0-5*power(T0,2))
inv(qsym,"nonzero pairing of selected physical roots")
xi=mul(mul(mul(b,disc),qsym),fpi)
obstruction=el(9*power(xi,6)+24*power(xi,3)+64*one)
inv(obstruction,"critical trace obstruction 9Xi6+24Xi3+64")
# The leading-degree boundary s=-1 is handled in the original physical infinity chart.
Qminus=5*t*t+26*t+6
a=sy.Poly(sy.rem(f1.subs(s,-1),Qminus,t),t)
bb=sy.Poly(sy.rem(f2.subs(s,-1),Qminus,t),t)
finite_det=sy.factor(a.nth(0)*bb.nth(1)-a.nth(1)*bb.nth(0))
need(finite_det!=0,"s=-1, two finite polar roots")
top=sy.Poly(k,t).nth(5)
need(sy.diff(top,s)==-1 and sy.diff(top,s,2)==0,"original infinity first/second source derivatives")
infinity_res=sy.resultant(Qminus,f2.subs(s,-1),t)
need(infinity_res!=0,"s=-1, one infinite selected root")
output={"status":"complete","scope":"H single three-jet, Hp=0, rankV2 reduced, essT3=6: branch excluded",
 "originalKernelVerified":True,"sourceSecondDerivativeNormalization":"one half of source second derivative",
 "wronskianNumeratorDenominator":str(denfac),"fullResultantDegree":int(resu.degree()),
 "boundaryFactor":"s^8*(s-2)^2*(s+6)^2*(s+1)^12",
 "residualDegree":int(G.degree()),"residualPolynomialSHA256":digest(rec(G)),
 "residualSquarefree":True,"commonRootEuclideanDegreePairs":seq,
 "recoveredCofactorRootSHA256":digest(rec(ww)),
 "XiSHA256":digest(rec(xi)),"obstructionSHA256":digest(rec(obstruction)),
 "allQQInverseCount":len(units),"allQQInverseRemultiplicationsVerified":True,
 "units":units,"sMinusOneFinitePairDeterminant":str(finite_det),
 "sMinusOneInfinityPairResultant":str(infinity_res),
 "elapsedSeconds":time.perf_counter()-started}
print(json.dumps(output,separators=(',',':'),sort_keys=True),flush=True)
