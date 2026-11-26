#!/usr/bin/env python3
"""Actual QQ gate for reduced H3 degenerate Gram, primitive phase,
with the zero H edge {-1,infinity}. No modular computation.
A successful result is an exact rational exclusion on the original physical open set.
"""
import time,json,hashlib,signal
import sympy as S
from flint import fmpz_mpoly_ctx,fmpz_poly,fmpq_poly,fmpq_mat,fmpq
started=time.monotonic()
def out(stage,**kw):
 print(json.dumps(dict(stage=stage,seconds=time.monotonic()-started,**kw),sort_keys=True),flush=True)
def need(v,msg):
 if not v:raise AssertionError(msg)
def alarm_handler(signum,frame):
 raise TimeoutError("bounded QQ zero-edge infinity gate unresolved")
signal.signal(signal.SIGALRM,alarm_handler);signal.alarm(270)
s0,t0,X0=S.symbols("s t X")
def ker(s,t):
 return S.expand(-(t-s)**2*(s**3-5*s*s+(s**3-3*s*s+22*s)*t-(3*s*s+3*s+5)*t*t+(s+1)*t**3))
def pp(t):return 5*t**3+31*t*t+32*t+6
aa=100*s0*s0+400*s0+1003
bb=-75*s0**3-65*s0*s0-480*s0+1196
cc=75*s0**4+465*s0**3+1483*s0*s0+1376*s0+516
Phi=aa*t0*t0+bb*t0+cc
need(S.rem(25*ker(s0,t0)+2*(s0+1)*(t0+1)*Phi,pp(t0)+pp(s0),t0)==0,"original kernel polar quotient modulo p(t)+p(s)")
need(S.expand(ker(-1,t0)-(t0+1)*pp(t0))==0,"original zero-edge polar at -1")
x0=(X0-31)/5;Zh0=X0*X0-31*X0+160;z0=Zh0/25
Eh0=X0*X0-26*X0+30;Dh0=-3*X0*X0+62*X0+321
qpair=x0**3-5*x0*x0+x0*x0*z0-6*x0*z0+32*z0-5*z0*z0
need(S.expand(625*qpair+4*(X0-31)*(X0+9)*Eh0)==0,"original V pair kernel factor")
need(S.expand(25*(x0*x0-4*z0)-Dh0)==0,"original V discriminant factor")
need(S.expand(25*(z0+x0+1)-Eh0)==0,"original nonzero V pair with infinity")
out("original_kernel_identities_complete",count=5,field="QQ",no_modular_computation=True)

ctx=fmpz_mpoly_ctx.get(("s","X"),"lex")
s,X=ctx.gens()
p=5*s**3+31*s**2+32*s+6
Z=X**2-31*X+160
E=X**2-26*X+30
D=-3*X**2+62*X+321
C=X**3-31*X**2+160*X-125*s**3-775*s**2-800*s-300
a=100*s**2+400*s+1003
b=-75*s**3-65*s**2-480*s+1196
c=75*s**4+465*s**3+1483*s**2+1376*s+516
At=25*c-a*Z
Bt=5*b+a*(X-31)
Sh=2*At+Bt*(X-31)
Ph=At**2+At*Bt*(X-31)+Bt**2*Z
Kstar=D*(X-31)*(X+9)
Phase=Sh**2-Ph
Norm=Sh**6+16*Kstar**6
OriginalNorm=Ph**3+16*Kstar**6
need(not(OriginalNorm-Norm+Phase*(Ph**2+Ph*Sh**2+Sh**4)),"exact norm reduction by phase")
U=(s+1)*p*E*D*(X-31)*(X+9)
def sha(f):return hashlib.sha256(str(f).encode()).hexdigest()
def remX(f):
 r=f;q=ctx.from_dict({})
 while r and r.degrees()[1]>=3:
  j=int(r.degrees()[1])
  lc=ctx.from_dict({(i,0):v for (i,k),v in r.to_dict().items() if k==j})
  term=lc*X**(j-3)
  q+=term;r-=term*C
 need(not(f-q*C-r),"exact monic X remainder")
 return r
Rp=remX(Phase);Rn=remX(Norm)
for label,f in [("source_cubic",C),("original_primitive_phase",Phase),("original_norm",Norm),("phase_remainder",Rp),("norm_remainder",Rn),("physical_units",U)]:
 out("original_QQ_equation",label=label,degrees=list(map(int,f.degrees())),terms=len(f.to_dict()),sha256=sha(f))
out("begin_exact_QQ_resultants")
P=C.resultant(Rp,"X");Q=C.resultant(Rn,"X")
def uni(f):
 dic=f.to_dict();need(all(j==0 for (i,j) in dic),"univariate resultant")
 n=max((i for i,j in dic),default=-1)
 return fmpz_poly([int(dic.get((i,0),0)) for i in range(n+1)])
P=uni(P);Q=uni(Q)
need(P and Q,"nonzero exact resultants required")
Pq=fmpq_poly(P);Qq=fmpq_poly(Q)
G,Lp,Lq=Pq.xgcd(Qq)
need(Lp*Pq+Lq*Qq==G,"original resultant gcd identity over QQ")
out("exact_resultant_gcd",P_degree=P.degree(),Q_degree=Q.degree(),P_sha256=sha(P),Q_sha256=sha(Q),gcd_degree=G.degree(),gcd=str(G),bezout_verified=True)
Goriginal=G
bad=fmpq_poly([1,1])*fmpq_poly([6,32,31,5])
removed=fmpq_poly([1]);layers=[]
while G.degree()>0:
 h=G.gcd(bad)
 if h.degree()==0:break
 div,rem=divmod(G,h);need(not rem,"delete only complete original nonphysical source factors")
 layers.append(int(h.degree()));removed*=h;G=div
need(removed*G==Goriginal,"complete bad-source factor identity")
out("paid_source_primary_deletion",layers=layers,removed_degree=removed.degree(),remaining_degree=G.degree(),remaining=str(G),only_factors="s+1 and p(s), both original nonzero pairings")
if G.degree()==0:
 out("complete",exclusion="all common resultant roots violate original nonzero s+1 or p(s)",source_sha256=hashlib.sha256(open(__file__,"rb").read()).hexdigest(),ordinary_isp_claim=False)
 signal.alarm(0);raise SystemExit(0)
G=G/G[G.degree()]
m=int(G.degree());dim=3*m
need(0<m<=80,"finite QQ algebra bound exceeded; unresolved")
zq=fmpq_poly([]);oq=fmpq_poly([1])
def red(f):return f%G
def zero():return [zq,zq,zq]
def add(a,b):return [red(a[i]+b[i]) for i in range(3)]
def neg(a):return [-v for v in a]
Ccoeff=[red(fmpq_poly([-300,-800,-775,-125])),fmpq_poly([160]),fmpq_poly([-31])]
def mul(a,b):
 tmp=[zq for i in range(5)]
 for i in range(3):
  for j in range(3):tmp[i+j]=red(tmp[i+j]+a[i]*b[j])
 for k in (4,3):
  ck=tmp[k]
  for j in range(3):tmp[k-3+j]=red(tmp[k-3+j]-ck*Ccoeff[j])
 return [red(tmp[i]) for i in range(3)]
def qp(f,n):
 r=[oq,zq,zq]
 while n:
  if n&1:r=mul(r,f)
  n//=2
  if n:f=mul(f,f)
 return r
def image(f):
 f=remX(f);dic=f.to_dict()
 return [red(fmpq_poly([int(dic.get((i,j),0)) for i in range(int(f.degrees()[0])+1)])) for j in range(3)] if f else zero()
def vec(f):return [f[j][i] for j in range(3) for i in range(m)]
def fromvec(v):return [fmpq_poly(v[j*m:(j+1)*m]) for j in range(3)]
F1=image(Rp);F2=image(Rn);Fu=image(U)
target=qp(Fu,dim)
columns=[]
for f in (F1,F2):
 for j in range(3):
  for i in range(m):
   bas=zero();bas[j]=fmpq_poly([0]*i+[1])
   columns.append(vec(mul(f,bas)))
tv=vec(target)
M=fmpq_mat([[columns[j][i] for j in range(2*dim)] for i in range(dim)])
Aug=fmpq_mat([[columns[j][i] for j in range(2*dim)]+[tv[i]] for i in range(dim)])
out("begin_finite_QQ_original_identity",dimension=dim,columns=2*dim,physical_power=dim)
R,rank=Aug.rref()
solution=[fmpq(0) for j in range(2*dim)]
consistent=True
for i in range(dim):
 piv=next((j for j in range(2*dim) if R[i,j]),None)
 if piv is None:
  if R[i,2*dim]:consistent=False
 else:solution[piv]=R[i,2*dim]
need(consistent,"original finite QQ physical identity not obtained; remaining algebra unresolved")
sol=fmpq_mat([[v] for v in solution]);tar=fmpq_mat([[v] for v in tv])
need(M*sol==tar,"exact rational matrix remultiplication")
Af=fromvec(solution[:dim]);Bf=fromvec(solution[dim:])
need(add(mul(Af,F1),mul(Bf,F2))==target,"exact U^dimension = A*phase + B*norm in original finite QQ algebra")
out("exact_physical_unit_power_identity_verified",dimension=dim,augmented_rank=int(rank),nonzero_coefficients=sum(bool(v) for v in solution),certificate_sha256=hashlib.sha256("|".join(map(str,solution)).encode()).hexdigest(),identity="U^dimension=A*phase+B*norm mod (G(s),C(s,X))",field="QQ",no_modular_computation=True)
out("complete",exclusion="primitive phases with the H zero edge {-1,infinity}, including every original physical source exception through U",source_sha256=hashlib.sha256(open(__file__,"rb").read()).hexdigest(),ordinary_isp_claim=False)
signal.alarm(0)
