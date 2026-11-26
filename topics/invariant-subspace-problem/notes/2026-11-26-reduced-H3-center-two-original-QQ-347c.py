#!/usr/bin/env python3
"""Exact QQ original source gate: primitive reduced H3, degenerate Gram,
Hp=0, essential six, original central H source 2.
The actual basis t=2+1/z changes K. All leading-zero fibers paid.
No modular computation or extrapolation.
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
 raise TimeoutError("bounded original special-central QQ gate unresolved")
signal.signal(signal.SIGALRM,alarm_handler);signal.alarm(600)
center=2
A0,B0,t0,r0,X0=S.symbols("A B t r X")
Koriginal=S.Matrix([[0,0,0,0,5,-1],[0,0,0,-32,5,-1],[0,0,54,-4,5,0],[0,-32,-4,-8,0,0],[5,5,5,0,0,0],[-1,-1,0,0,0,0]])
M=S.Matrix(6,6,lambda i,j:S.binomial(i,5-j)*S.Integer(center)**(i-5+j) if i>=5-j else 0)
need(M.det()**2==1,"original invertible source basis")
K=M.T*Koriginal*M
need(all(S.expand(sum(M[i,j]*t0**j for j in range(6))-t0**(5-i)*(center*t0+1)**i)==0 for i in range(6)),"entire homogeneous original source parametrization")
def ker(s,t):
 return S.expand(sum(K[i,j]*s**i*t**j for i in range(6) for j in range(6)))
if center==2:
 qs=-16*(A0+1)*B0**2-(5*A0*A0+18*A0+5)*B0+3*A0**3+A0*A0
 exceptional_A=S.Integer(-1)
else:
 need(center==-6,"specified original centers only")
 qs=(144*A0-112)*B0**2+(-5*A0*A0+30*A0-5)*B0-5*A0**3+A0*A0
 exceptional_A=S.Rational(7,9)
need(S.expand(ker(r0,t0)+(r0-t0)**2*qs.subs({A0:r0+t0,B0:r0*t0}))==0,"entire transformed original kernel factor")
l0,l1,l2=[K[i,5] for i in range(3)]
need(S.expand(S.Poly(ker(r0,t0),t0).nth(5)-(l0+l1*r0+l2*r0*r0))==0,"actual quadratic central polar")
def powers_h(Ah,ph):
 P=[S.Integer(2),Ah]
 for i in range(2,6):P.append(S.expand(Ah*P[-1]-ph*P[-2]))
 return P
def negative_sum(Ah,ph):
 P=powers_h(Ah,ph)
 W=[-l2*(Ah*Ah-2*ph)-l1*Ah-2*l0,-l2*ph*Ah-2*l1*ph-l0*Ah]
 for i in range(2,6):W.append(-l2*ph*ph*P[i-2]-l1*ph*P[i-1]-l0*P[i])
 return S.expand(sum(K[i,j]*W[i]*t0**j for i in range(6) for j in range(6)))
def endpoint_norm(poly,Ah,ph):
 rr=S.Poly(S.rem(poly,r0*r0-Ah*r0+ph,r0),r0)
 f,g=rr.nth(0),rr.nth(1)
 return S.cancel(f*f+Ah*f*g+ph*g*g)
def fq(v):
 v=S.Rational(v)
 return fmpq(int(v.p),int(v.q))
def rational_poly(ex,var):
 P=S.Poly(ex,var,domain=S.QQ)
 return fmpq_poly([fmpq(int(P.nth(i).p),int(P.nth(i).q)) for i in range(P.degree()+1)]) if P else fmpq_poly([])
qs_coeff=S.Poly(qs,B0)
a0=qs_coeff.nth(2);b0=qs_coeff.nth(1);c0raw=qs_coeff.nth(0)
need(S.expand(a0.subs(A0,exceptional_A))==0,"all transformed zero-edge leading roots identified")
need(S.degree(a0,A0)==1,"only one leading-zero fiber")
boundary_poly=S.Poly(qs.subs(A0,exceptional_A),B0)
need(boundary_poly.degree()==1,"exact leading-zero fiber stays linear in endpoint product")
boundary_product=S.cancel(-boundary_poly.nth(0)/boundary_poly.nth(1))
boundary_discriminant=S.cancel(exceptional_A**2-4*boundary_product)
# The A-leading boundary is paid before the monic rescaling below.
if not boundary_discriminant:
 out("leading_zero_original_boundary_excluded",center=center,A=str(exceptional_A),product=str(boundary_product),reason="the exact zero edge forces repeated H endpoints")
else:
 ph=boundary_product;Ah=exceptional_A
 E0=endpoint_norm(l0+l1*r0+l2*r0*r0,Ah,ph)
 need(E0!=0,"leading-zero original central pairings unexpectedly vanish")
 nh=negative_sum(Ah,ph)
 cc,rr=S.div(nh,t0*t0-Ah*t0+ph,t0)
 need(S.expand(rr)==0,"original boundary endpoint divisor")
 sc=int(S.ilcm(*[int(c.q) for c in S.Poly(cc,t0).coeffs()]))
 cc=S.expand(sc*cc)
 qc=-S.Poly(cc,t0).nth(3)
 c2b=S.Poly(cc,t0).nth(2);c1b=S.Poly(cc,t0).nth(1);c0b=S.Poly(cc,t0).nth(0)
 need(qc==2*sc*E0 and qc!=0,"paid boundary V-source cubic scale")
 Cb=rational_poly(X0**3+c2b*X0**2-qc*c1b*X0+qc*qc*c0b,X0)
 rb=lambda f:f%Cb
 xb=fmpq_poly([0,1]);y=rb(xb+fq(c2b));z=rb(xb*xb+fq(c2b)*xb-fq(qc*c1b));qq=fmpq_poly([fq(qc)])
 def bp(f,n):
  ans=fmpq_poly([1])
  while n:
   if n&1:ans=rb(ans*f)
   n//=2
   if n:f=rb(f*f)
  return ans
 def bm(x,y):return rb(x*y)
 J=endpoint_norm(ker(r0,t0),Ah,ph)
 jscale=int(S.ilcm(*[int(c.q) for c in S.Poly(J,t0).coeffs()]))
 Jc=[fq(S.Poly(S.expand(jscale*J),t0).nth(i)) for i in range(11)]
 aa=[fmpq_poly([1]),fmpq_poly([])];bb=[fmpq_poly([]),fmpq_poly([1])]
 for i in range(2,11):
  aa.append(rb(y*aa[-1]-z*aa[-2]));bb.append(rb(y*bb[-1]-z*bb[-2]))
 ja=fmpq_poly([]);jb=fmpq_poly([])
 for i in range(11):
  ff=bp(qq,10-i)*Jc[i]
  ja=rb(ja+ff*aa[i]);jb=rb(jb+ff*bb[i])
 la=rb(fq(l0)*qq*qq-fq(l2)*z);lb=rb(fq(l1)*qq+fq(l2)*y)
 eh=rb(la*la+y*la*lb+z*lb*lb);dh=rb(y*y-4*z)
 pj=rb(ja*ja+y*ja*jb+z*jb*jb)
 tr=rb(ja*(2*la*la+2*y*la*lb+(y*y-2*z)*lb*lb)+jb*(y*la*la+4*z*la*lb+z*y*lb*lb))
 qv=fmpq_poly([])
 for (ix,iz),coef in S.Poly(qs,A0,B0).terms():
  need(5-ix-2*iz>=0,"original kernel weighted degree")
  qv=rb(qv+fq(coef)*bp(y,ix)*bp(z,iz)*bp(qq,5-ix-2*iz))
 phase=rb(tr*tr-eh*eh*pj)
 norm=rb(fq(jscale**3*E0**3)*bp(bm(dh,qv),6)+4*bp(tr,3))
 unit=rb(fq(E0*boundary_discriminant)*eh*dh*qv*pj)
 target=bp(unit,3)
 mons=[fmpq_poly([0]*i+[1]) for i in range(3)]
 cols=[[rb(g*m)[i] for i in range(3)] for g in (phase,norm) for m in mons]
 tv=[target[i] for i in range(3)]
 Mat=fmpq_mat([[cols[j][i] for j in range(6)] for i in range(3)])
 Aug=fmpq_mat([[cols[j][i] for j in range(6)]+[tv[i]] for i in range(3)])
 RR,rank=Aug.rref();sol=[fmpq(0) for j in range(6)]
 for i in range(3):
  piv=next((j for j in range(6) if RR[i,j]),None)
  need(piv is not None or not RR[i,6],"leading-zero original physical unit identity unresolved")
  if piv is not None:sol[piv]=RR[i,6]
 need(Mat*fmpq_mat([[x] for x in sol])==fmpq_mat([[x] for x in tv]),"original boundary rational matrix identity")
 ca=fmpq_poly(sol[:3]);cb=fmpq_poly(sol[3:])
 need(rb(ca*phase+cb*norm)==target,"entire original boundary identity in full source cubic")
 out("leading_zero_original_boundary_excluded",center=center,A=str(Ah),product=str(ph),E0=str(E0),dimension=3,matrix_rank=int(rank),certificate_sha256=hashlib.sha256("|".join(map(str,sol)).encode()).hexdigest(),identity="U^3=ca*phase+cb*norm modulo original monic Cx")
# General a(A)!=0 source chart: B=a(A)*ab makes the zero-edge equation monic.
prodH=B0/a0
QH=B0*B0+b0*B0+a0*c0raw
need(S.cancel(a0*qs.subs(B0,prodH)-QH)==0,"exact monic original zero edge after paid a(A)")
Ebar=S.cancel(a0*a0*endpoint_norm(l0+l1*r0+l2*r0*r0,A0,prodH))
need(S.Poly(Ebar,A0,B0,domain=S.ZZ) is not None,"integer central-pairing norm")
Hq=t0*t0-A0*t0+prodH
Nsum=negative_sum(A0,prodH)
Quot,Rema=S.div(Nsum,Hq,t0)
need(S.rem(S.cancel(a0**5*Rema),QH,B0)==0,"original endpoint divisor on all generic zero-edge fibers")
Cpre=S.cancel(a0**3*Quot)
need(S.Poly(Cpre,A0,B0,t0,domain=S.ZZ) is not None,"paid cubic scale a(A)^3 suffices")
Craw=S.expand(sum(S.rem(S.Poly(Cpre,t0).nth(i),QH,B0)*t0**i for i in range(4)))
q0=-S.Poly(Craw,t0).nth(3)
a2=S.Poly(Craw,t0).nth(2);a1=S.Poly(Craw,t0).nth(1);a00=S.Poly(Craw,t0).nth(0)
need(S.rem(S.expand(q0-2*a0*Ebar),QH,B0)==0,"paid leading source cubic factor 2*a*Ebar")
need(S.rem(S.cancel(a0**4*Nsum-a0*Hq*Craw),QH,B0)==0,"entire scaled original cubic identity")
J0=S.cancel(a0**5*endpoint_norm(ker(r0,t0),A0,prodH))
need(S.Poly(J0,A0,B0,t0,domain=S.ZZ) is not None,"integer original endpoint polar product")
Jcoeff=[S.expand(S.Poly(J0,t0).nth(i)) for i in range(11)]
need(S.expand(Jcoeff[10]-a0**3*Ebar)==0,"leading original endpoint product")
ll,mm,laa,lbb,jaa,jbb=S.symbols("ll mm laa lbb jaa jbb")
trcheck=jaa*(2*laa**2+2*(ll+mm)*laa*lbb+((ll+mm)**2-2*ll*mm)*lbb**2)+jbb*((ll+mm)*laa**2+4*ll*mm*laa*lbb+ll*mm*(ll+mm)*lbb**2)
need(S.expand(trcheck-(jaa+jbb*ll)*(laa+lbb*mm)**2-(jaa+jbb*mm)*(laa+lbb*ll)**2)==0,"entire symmetric polar trace identity")
out("original_kernel_identities_complete",center=center,field="QQ",a=str(a0),QH=str(QH),central_polar=str(l0+l1*t0+l2*t0*t0),Ebar=str(Ebar),cubic_scale="a(A)^3",J_scale="a(A)^5",V_scale=str(q0))
ctx=fmpz_mpoly_ctx.get(("A","B","X"),"lex")
A,B,X=ctx.gens()
def cv(ex):
 dic={}
 for mon,c in S.Poly(ex,A0,B0,X0).terms():
  need(c.q==1,"integer original coefficient")
  if c:dic[mon]=int(c)
 return ctx.from_dict(dic)
Qb=cv(QH)
aa=cv(a0)
E=cv(Ebar)
q=cv(q0)
c2=cv(a2);c1=cv(a1);c0=cv(a00)
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
LA=red(int(l0)*pw(q,2)-int(l2)*Z)
LB=red(int(l1)*q+int(l2)*Y)
Eh=red(pw(LA,2)+mul(mul(Y,LA),LB)+mul(Z,pw(LB,2)))
Qv=ctx.from_dict({})
for (ix,iz),coef in S.Poly(qs,A0,B0).terms():
 need(5-ix-2*iz>=0,"original transformed kernel weighted degree")
 Qv=red(Qv+int(coef)*mul(mul(pw(Y,ix),pw(Z,iz)),pw(q,5-ix-2*iz)))
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
Trace=red(mul(JA,red(2*pw(LA,2)+2*mul(mul(Y,LA),LB)+mul(red(pw(Y,2)-2*Z),pw(LB,2))))+mul(JB,red(mul(Y,pw(LA,2))+4*mul(mul(Z,LA),LB)+mul(mul(Z,Y),pw(LB,2)))))
Phase=red(pw(Trace,2)-mul(pw(Eh,2),PJ))
Norm=red(mul(mul(pw(aa,9),pw(E,3)),pw(mul(Dh,Qv),6))+4*pw(Trace,3))
U=red(aa*E*(aa*A*A-4*B))
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
out("exact_triangular_norm_gcd",P_degree=PP.degree(),N_degree=NN.degree(),P_sha256=sha(PP),N_sha256=sha(NN),gcd_degree=G.degree(),gcd_sha256=sha(G),bezout_verified=True)
if G.degree()==0:
 out("complete",source_sha256=hashlib.sha256(open(__file__,"rb").read()).hexdigest(),outcome="original rational triangular norms are coprime; full original-special-central primitive chart excluded",ordinary_isp_claim=False)
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
