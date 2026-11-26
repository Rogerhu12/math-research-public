#!/usr/bin/env python3
"""Actual QQ gate: primitive reduced H3, degenerate Gram, central H source infinity.
The two finite H endpoints have zero mutual pairing.
All original source exceptions are retained in a triangular algebra of rank6 over QQ[A].
No characteristic-positive input or modular unit-ideal extrapolation.
"""
import time,json,hashlib,signal
import sympy as S
from flint import fmpz_mpoly_ctx,fmpq_mpoly_ctx,fmpz_poly,fmpq_poly,fmpq_mat,fmpq
started=time.monotonic()
def out(stage,**kw):
 print(json.dumps(dict(stage=stage,seconds=time.monotonic()-started,**kw),sort_keys=True),flush=True)
def need(v,msg):
 if not v:raise AssertionError(msg)
def alarm_handler(signum,frame):
 raise TimeoutError("bounded central-infinity original QQ gate unresolved")
signal.signal(signal.SIGALRM,alarm_handler);signal.alarm(330)
A0,B0,t0,r0,X0=S.symbols("A B t r X")
def ker(s,t):
 return S.expand(-(t-s)**2*(s**3-5*s*s+(s**3-3*s*s+22*s)*t-(3*s*s+3*s+5)*t*t+(s+1)*t**3))
prodH=B0/5
Hq=t0*t0-A0*t0+prodH
QH=B0*B0-(A0*A0-6*A0+32)*B0-5*A0**3+25*A0*A0
Ebar=5*A0+B0+5
q0=10*Ebar
a2=15*A0*B0+75*A0*A0+200*A0+250
a1=(-7*A0*A0+2*A0+306)*B0-35*A0**3-350*A0*A0-550*A0
a0=(-7*A0*A0-88*A0-14)*B0+90*A0**3+350*A0*A0
K=S.Matrix([[0,0,0,0,5,-1],[0,0,0,-32,5,-1],[0,0,54,-4,5,0],[0,-32,-4,-8,0,0],[5,5,5,0,0,0],[-1,-1,0,0,0,0]])
powers=[S.Integer(2),A0]
for i in range(2,6):powers.append(S.expand(A0*powers[-1]-prodH*powers[-2]))
weights=[A0+2]+[S.expand(prodH*powers[i-1]+powers[i]) for i in range(1,6)]
Nsum=S.expand(sum(K[i,j]*weights[i]*t0**j for i in range(6) for j in range(6)))
need(S.rem(S.expand(25*Nsum-Hq*(-q0*t0**3+a2*t0*t0+a1*t0+a0)),QH,B0)==0,"entire original sum-polar cubic modulo the zero-edge polynomial")
krem=S.rem(ker(r0,t0),r0*r0-A0*r0+prodH,r0)
kr=S.Poly(krem,r0)
F0=kr.nth(0);G0=kr.nth(1)
J0=S.expand(3125*(F0*F0+A0*F0*G0+prodH*G0*G0))
need(all(v.q==1 for v in S.Poly(J0,A0,B0,t0).coeffs()),"integer original endpoint-polar product")
Jcoeff=[S.expand(S.Poly(J0,t0).nth(i)) for i in range(11)]
need(S.expand(Jcoeff[10]-625*Ebar)==0,"leading original product factor")
out("original_kernel_identities_complete",count=3,physical_H_parameters="A=a+b,B=5ab",J_scale=3125,V_scale="q=10(5A+B+5)=50(a+1)(b+1)",field="QQ")

ctx=fmpz_mpoly_ctx.get(("A","B","X"),"lex")
A,B,X=ctx.gens()
def cv(ex):
 dic={}
 for mon,c in S.Poly(ex,A0,B0,X0).terms():
  need(c.q==1,"integer original coefficient")
  if c:dic[mon]=int(c)
 return ctx.from_dict(dic)
Qb=cv(QH)
E=5*A+B+5
q=10*E
c2=cv(a2);c1=cv(a1);c0=cv(a0)
def rd(f,rel,var,degree):
 rem=f;quot=ctx.from_dict({})
 while rem and rem.degrees()[var]>=degree:
  n=int(rem.degrees()[var])
  dic={}
  for mon,c in rem.to_dict().items():
   if mon[var]==n:
    key=list(mon);key[var]=0;dic[tuple(key)]=c
  lc=ctx.from_dict(dic)
  term=lc*ctx.gen(var)**(n-degree)
  quot+=term;rem-=term*rel
 need(not(f-quot*rel-rem),"exact original monic triangular remainder")
 return rem
def rb(f):return rd(f,Qb,1,2)
Cx=rb(X**3+c2*X**2-q*c1*X+q*q*c0)
def red(f):return rb(rd(f,Cx,2,3))
def mul(a,b):return red(a*b)
def pw(f,n):
 ans=ctx.from_dict({(0,0,0):1})
 while n:
  if n&1:ans=mul(ans,f)
  n//=2
  if n:f=mul(f,f)
 return ans
q=red(q);E=red(E)
Y=red(X+c2);Z=red(X*X+c2*X-q*c1)
Dh=red(Y*Y-4*Z)
Eh=red(q*q+q*Y+Z)
Qv=red(mul(q,pw(Y,3))-5*mul(pw(q,2),pw(Y,2))+mul(pw(Y,2),Z)-6*mul(mul(q,Y),Z)+32*mul(pw(q,2),Z)-5*pw(Z,2))
# Remainders of T^j modulo T^2-Y*T+Z, always in the original rank6 base algebra.
zero=ctx.from_dict({});one=ctx.from_dict({(0,0,0):1})
ta=[one,zero];tb=[zero,one]
for j in range(2,11):
 ta.append(red(mul(Y,ta[-1])-mul(Z,ta[-2])))
 tb.append(red(mul(Y,tb[-1])-mul(Z,tb[-2])))
Jc=[red(cv(c)) for c in Jcoeff]
JA=zero;JB=zero
for j in range(11):
 f=mul(Jc[j],pw(q,10-j))
 JA=red(JA+mul(f,ta[j]));JB=red(JB+mul(f,tb[j]))
PJ=red(pw(JA,2)+mul(mul(JA,JB),Y)+mul(pw(JB,2),Z))
Trace=red(mul(JA,red(Y*Y-2*Z+2*q*Y+2*q*q))+mul(JB,red(Z*Y+4*q*Z+q*q*Y)))
Phase=red(pw(Trace,2)-mul(pw(Eh,2),PJ))
Norm=red((5**12)*mul(pw(E,3),pw(mul(Dh,Qv),6))+4*pw(Trace,3))
U=red(E*(5*A*A-4*B))
for v in (Eh,Dh,Qv,PJ):U=mul(U,v)
def sha(f):return hashlib.sha256(str(f).encode()).hexdigest()
for label,f in [("H_zero_edge",Qb),("V_source_cubic",Cx),("original_phase",Phase),("original_norm",Norm),("original_physical_units",U)]:
 out("triangular_original_equation",label=label,degrees=list(map(int,f.degrees())),terms=len(f.to_dict()),sha256=sha(f))
out("begin_exact_triangular_QQ_norms")
RP=Cx.resultant(Phase,"X")
RN=Cx.resultant(Norm,"X")
RP=rb(RP);RN=rb(RN)
PP=Qb.resultant(RP,"B");NN=Qb.resultant(RN,"B")
def uni(f):
 dic=f.to_dict();need(all(j==0 and k==0 for i,j,k in dic),"univariate exact triangular norm")
 n=max((i for i,j,k in dic),default=-1)
 return fmpz_poly([int(dic.get((i,0,0),0)) for i in range(n+1)])
PP=uni(PP);NN=uni(NN)
need(PP and NN,"nonzero exact rational norms required")
Pq=fmpq_poly(PP);Nq=fmpq_poly(NN)
G,Lp,Ln=Pq.xgcd(Nq)
need(Lp*Pq+Ln*Nq==G,"exact rational norm gcd remultiplication")
out("exact_triangular_norm_gcd",P_degree=PP.degree(),N_degree=NN.degree(),P_sha256=sha(PP),N_sha256=sha(NN),gcd_degree=G.degree(),gcd=str(G),bezout_verified=True)
if G.degree()==0:
 out("complete",source_sha256=hashlib.sha256(open(__file__,"rb").read()).hexdigest(),outcome="original rational triangular norms are coprime; full central-infinity primitive chart excluded",ordinary_isp_claim=False)
 signal.alarm(0);raise SystemExit(0)
# An exact factorization covers every A-root. Replacing f^k by f below is used
# only for pointwise exclusion, not a claim that primary quotient ideals coincide.
factor_content,factors=G.factor()
check=fmpq_poly([factor_content])
for f,k in factors:check*=fmpq_poly(f)**int(k)
need(check==G,"full QQ factorization remultiplication")
out("all_elimination_fibers",factors=[{"factor":str(f),"degree":f.degree(),"multiplicity":int(k)} for f,k in factors],scope="all complex A-roots retained; no quotient-primary equivalence claimed")

qctx=fmpq_mpoly_ctx.get(("A","B","X"),"lex")
qa,qb,qx=qctx.gens()
def qcv(f):return qctx.from_dict({mon:fmpq(c) for mon,c in f.to_dict().items()})
Qbb=qcv(Qb);Cxx=qcv(Cx);Rphase=qcv(Phase);Rnorm=qcv(Norm);Runit=qcv(U)
def qrd(f,rel,var,degree):
 rem=f;quot=qctx.from_dict({})
 while rem and rem.degrees()[var]>=degree:
  n=int(rem.degrees()[var]);dic={}
  for mon,c in rem.to_dict().items():
   if mon[var]==n:
    key=list(mon);key[var]=0;dic[tuple(key)]=c
  term=qctx.from_dict(dic)*qctx.gen(var)**(n-degree)
  quot+=term;rem-=term*rel
 need(not(f-quot*rel-rem),"exact finite rational triangular remainder")
 return rem
for fi,(ff,multiplicity) in enumerate(factors):
 f=fmpq_poly(ff);f=f/f[f.degree()]
 m=int(f.degree());dim=6*m
 need(0<m<=32,"finite original QQ fiber degree bound exceeded; unresolved")
 fa=qctx.from_dict({(i,0,0):f[i] for i in range(m+1) if f[i]})
 def rf(v):return qrd(qrd(qrd(v,Cxx,2,3),Qbb,1,2),fa,0,m)
 def qm(v,w):return rf(v*w)
 def qp(v,n):
  ans=qctx.from_dict({(0,0,0):fmpq(1)})
  while n:
   if n&1:ans=qm(ans,v)
   n//=2
   if n:v=qm(v,v)
  return ans
 r1=rf(Rphase);r2=rf(Rnorm);ru=rf(Runit)
 target=qp(ru,dim)
 mons=[(i,j,k) for k in range(3) for j in range(2) for i in range(m)]
 def vec(v):
  dic=v.to_dict();return [dic.get(mon,fmpq(0)) for mon in mons]
 columns=[]
 for v in (r1,r2):
  for mon in mons:columns.append(vec(qm(v,qctx.from_dict({mon:fmpq(1)}))))
 tv=vec(target)
 Mat=fmpq_mat([[columns[j][i] for j in range(2*dim)] for i in range(dim)])
 Aug=fmpq_mat([[columns[j][i] for j in range(2*dim)]+[tv[i]] for i in range(dim)])
 out("begin_finite_QQ_fiber",index=fi,factor=str(ff),original_multiplicity=int(multiplicity),dimension=dim,physical_power=dim)
 R,rank=Aug.rref()
 sol=[fmpq(0) for j in range(2*dim)];consistent=True
 for i in range(dim):
  piv=next((j for j in range(2*dim) if R[i,j]),None)
  if piv is None:
   if R[i,2*dim]:consistent=False
  else:sol[piv]=R[i,2*dim]
 need(consistent,"original physical power identity not obtained in this QQ fiber")
 sv=fmpq_mat([[v] for v in sol]);tvmat=fmpq_mat([[v] for v in tv])
 need(Mat*sv==tvmat,"rational matrix identity remultiplication")
 af=qctx.from_dict({mon:sol[i] for i,mon in enumerate(mons) if sol[i]})
 bf=qctx.from_dict({mon:sol[dim+i] for i,mon in enumerate(mons) if sol[dim+i]})
 need(rf(af*r1+bf*r2)==target,"exact original physical-unit power identity in full rank6 fiber")
 out("finite_QQ_fiber_verified",index=fi,dimension=dim,rank=int(rank),nonzero_coefficients=sum(bool(v) for v in sol),certificate_sha256=hashlib.sha256("|".join(map(str,sol)).encode()).hexdigest(),identity="U^dimension=af*original_phase+bf*original_norm modulo (f(A),Qb,Cx)")
out("complete",source_sha256=hashlib.sha256(open(__file__,"rb").read()).hexdigest(),outcome="all exact QQ necessary source fibers contradict original physical U!=0",ordinary_isp_claim=False)
signal.alarm(0)
