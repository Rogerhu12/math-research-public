#!/usr/bin/env python3
"""Actual QQ gate for primitive reduced H3, degenerate Gram, with original
central H source 0. Apply the exact reciprocal curve reparametrization and
the corresponding reversed K matrix; do not assume K is Mobius invariant.
No characteristic-positive input or modular unit extrapolation.
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
 raise TimeoutError("bounded original-central-zero QQ gate unresolved")
signal.signal(signal.SIGALRM,alarm_handler);signal.alarm(330)
A0,B0,t0,r0,X0=S.symbols("A B t r X")
Koriginal=S.Matrix([[0,0,0,0,5,-1],[0,0,0,-32,5,-1],[0,0,54,-4,5,0],[0,-32,-4,-8,0,0],[5,5,5,0,0,0],[-1,-1,0,0,0,0]])
K=S.Matrix(6,6,lambda i,j:Koriginal[5-i,5-j])
def ker(s,t):
 return S.expand(sum(K[i,j]*s**i*t**j for i in range(6) for j in range(6)))
need(S.expand(ker(r0,t0)-sum(Koriginal[i,j]*r0**(5-i)*t0**(5-j) for i in range(6) for j in range(6)))==0,"exact reversed original K under reciprocal chart")
need(S.Poly(ker(r0,t0),t0).nth(5)==5*r0-1,"actual central polar after reciprocal chart")
origQ=(r0+t0)**3+(r0+t0)**2-(5*(r0+t0)**2+6*(r0+t0)+5)*(r0*t0)+32*(r0*t0)**2
need(S.expand(ker(r0,t0)+(r0-t0)**2*origQ)==0,"entire transformed original polar factor")
den=32
prodH=B0/den
Hq=t0*t0-A0*t0+prodH
QH=B0*B0-(5*A0*A0+6*A0+5)*B0+32*A0**3+32*A0*A0
Ebar=25*B0-160*A0+32
powers=[S.Integer(2),A0]
for i in range(2,6):powers.append(S.expand(A0*powers[-1]-prodH*powers[-2]))
# minus[L(b)k(a,t)+L(a)k(b,t)], L(t)=5t-1, leading -2L(a)L(b)
weights=[2-5*A0]+[S.expand(powers[i]-5*prodH*powers[i-1]) for i in range(1,6)]
Nsum=S.expand(sum(K[i,j]*weights[i]*t0**j for i in range(6) for j in range(6)))
Quot,Rema=S.div(Nsum,Hq,t0)
need(S.rem(S.expand(Rema),QH,B0)==0,"original endpoint-polar divisor modulo zero edge")
Craw=S.expand(sum(S.rem(S.Poly(Quot,t0).nth(i),QH,B0)*t0**i for i in range(4)))
scale=int(S.ilcm(*[int(c.q) for c in S.Poly(Craw,A0,B0,t0).coeffs()]))
Craw=S.expand(scale*Craw)
q0=-S.Poly(Craw,t0).nth(3)
a2=S.Poly(Craw,t0).nth(2);a1=S.Poly(Craw,t0).nth(1);a0=S.Poly(Craw,t0).nth(0)
need(S.expand(q0-2*S.Rational(scale,den)*Ebar)==0,"paid leading source cubic factor")
need(S.rem(S.expand(scale*Nsum-Hq*Craw),QH,B0)==0,"entire scaled original cubic identity")
krem=S.rem(ker(r0,t0),r0*r0-A0*r0+prodH,r0)
kr=S.Poly(krem,r0)
F0=kr.nth(0);G0=kr.nth(1)
J0=S.expand((den**5)*(F0*F0+A0*F0*G0+prodH*G0*G0))
need(all(v.q==1 for v in S.Poly(J0,A0,B0,t0).coeffs()),"integer transformed original endpoint-polar product")
Jcoeff=[S.expand(S.Poly(J0,t0).nth(i)) for i in range(11)]
need(S.expand(Jcoeff[10]-(den**4)*Ebar)==0,"leading original endpoint product")
out("original_kernel_identities_complete",count=7,original_center=0,physical_H_parameters="A=a+b,B=32ab in reciprocal chart",J_scale=den**5,cubic_scale=scale,V_scale=str(q0),c2=str(a2),c1=str(a1),c0=str(a0),field="QQ")
ctx=fmpz_mpoly_ctx.get(("A","B","X"),"lex")
A,B,X=ctx.gens()
def cv(ex):
 dic={}
 for mon,c in S.Poly(ex,A0,B0,X0).terms():
  need(c.q==1,"integer original coefficient")
  if c:dic[mon]=int(c)
 return ctx.from_dict(dic)
Qb=cv(QH)
E=25*B-160*A+32
q=cv(q0)
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
Qv=red(32*pw(Z,2)-mul(red(5*pw(Y,2)+6*mul(q,Y)+5*pw(q,2)),Z)+mul(q,pw(Y,3))+mul(pw(q,2),pw(Y,2)))
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
Trace=red(mul(JA,red(25*(Y*Y-2*Z)-10*q*Y+2*q*q))+mul(JB,red(25*Z*Y-20*q*Z+q*q*Y)))
Phase=red(pw(Trace,2)-mul(pw(Eh,2),PJ))
Norm=red((32**12)*mul(pw(E,3),pw(mul(Dh,Qv),6))+4*pw(Trace,3))
U=red(E*(32*A*A-4*B))
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
 out("complete",source_sha256=hashlib.sha256(open(__file__,"rb").read()).hexdigest(),outcome="original rational triangular norms are coprime; full original-central-zero primitive chart excluded",ordinary_isp_claim=False)
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
