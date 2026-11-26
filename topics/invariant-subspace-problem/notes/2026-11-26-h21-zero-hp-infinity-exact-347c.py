#!/usr/bin/env python3
"""NEW w=infinity Hp0 gate. Complete only if every displayed assertion passes.
Exact QQ structure first; finite-field determinants lift through the proved
number field QQ[e]/G9. No finite-field empty-locus inference is used.
"""
import json,time,hashlib
from fractions import Fraction
import sympy as S
from flint import fmpq,fmpq_poly,fmpz_mpoly_ctx,nmod_poly,nmod_mat
started=time.monotonic()
def need(q,label):
 if not q: raise AssertionError(label)
def out(stage,**kw):print(json.dumps(dict(stage=stage,seconds=time.monotonic()-started,**kw),sort_keys=True),flush=True)
def digest(q):return hashlib.sha256(str(q).encode()).hexdigest()
units=[]
class QQ:
 def __init__(self,G,label):
  self.G=G/G[int(G.degree())];self.n=int(G.degree());self.label=label
  need(self.G.gcd(self.G.derivative()).degree()==0,label+" squarefree")
  self.zero=fmpq_poly([]);self.one=fmpq_poly([1]);self.s=fmpq_poly([0,1])%self.G
 def el(self,a):return (a if isinstance(a,fmpq_poly) else fmpq_poly([a]))%self.G
 def inv(self,a,label):
  a=self.el(a);g,u,v=a.xgcd(self.G)
  need(g.degree()==0 and g[0]!=0,self.label+" "+label+" QQ unit")
  r=(u/g[0])%self.G
  need(a*r%self.G==self.one,self.label+" "+label+" inverse remultiplication")
  units.append(dict(label=self.label+" "+label,value=digest(a),inverse=digest(r)))
  return r
 def trim(self,a):
  a=list(a)
  while a and not a[-1]:a.pop()
  return a
 def add(self,a,b):
  return self.trim([self.el((a[i] if i<len(a) else 0)+(b[i] if i<len(b) else 0)) for i in range(max(len(a),len(b)))])
 def mul(self,a,b):
  if not a or not b:return []
  r=[self.zero]*(len(a)+len(b)-1)
  for i,u in enumerate(a):
   for j,v in enumerate(b):r[i+j]=self.el(r[i+j]+u*v)
  return self.trim(r)
 def div(self,a,b,label):
  a=self.trim(a);b=self.trim(b);old=list(a);need(bool(b),label+" divisor")
  if len(a)<len(b):return [],a
  iv=self.inv(b[-1],label+" leading")
  q=[self.zero]*(len(a)-len(b)+1)
  while a and len(a)>=len(b):
   d=len(a)-len(b);c=self.el(a[-1]*iv);q[d]=self.el(q[d]+c)
   for j,v in enumerate(b):a[d+j]=self.el(a[d+j]-c*v)
   a=self.trim(a)
  q=self.trim(q);need(self.add(self.mul(q,b),a)==old,label+" division identity")
  return q,a
 def monic(self,a,label):
  a=self.trim(a);need(bool(a),label+" nonzero")
  iv=self.inv(a[-1],label+" monic")
  return [self.el(c*iv) for c in a]
 def gcd(self,a,b,label):
  a=self.trim(a);b=self.trim(b);i=0
  while b:
   _,r=self.div(a,b,label+" "+str(i));a,b=b,r;i+=1
  return self.monic(a,label+" gcd")
 def eval(self,a,u):
  r=self.zero
  for c in reversed(a):r=self.el(r*u+c)
  return r
 def remove(self,R,B,label):
  R=self.monic(R,label+" original");removed=[]
  while len(R)>1:
   g=self.gcd(R,B,label+" intersection")
   if len(g)==1:break
   q,r=self.div(R,g,label+" remove")
   need(not r,label+" exact removal")
   removed.append(len(g)-1);R=self.monic(q,label+" residual")
  return R,removed
s,t,x,z,e=S.symbols('s t x z e')
K=S.Matrix([[0,0,0,0,5,-1],[0,0,0,-32,5,-1],[0,0,54,-4,5,0],[0,-32,-4,-8,0,0],[5,5,5,0,0,0],[-1,-1,0,0,0,0]])
vec=lambda a:S.Matrix([a**j for j in range(6)])
k=S.expand((vec(s).T*K*vec(t))[0])
qs=s**3-5*s**2+(s**3-3*s**2+22*s)*t-(3*s**2+3*s+5)*t**2+(s+1)*t**3
need(S.expand(k+(t-s)**2*qs)==0,"original K kernel")
need(S.Poly(k,t).nth(5)==-s-1,"original infinity polar")
rr=S.rem(k,t*t-x*t+z,t);L=S.Poly(rr,t).nth(1);E=S.expand(S.Poly(rr,t).nth(0)-L)
ctx=fmpz_mpoly_ctx.get(('s','x','z','e'))
cv=lambda f:ctx.from_dict({m:int(c) for m,c in S.Poly(f,s,x,z,e).terms()})
E0,E01,LL,LD=cv(E),cv(S.diff(E,s)),cv(L),cv((s+1)*S.diff(L,s)-L)
ss,xx,zz,ee=ctx.gens()
res=E0.resultant(E01,2)
base=max((f for f,m in res.factor()[1]),key=lambda f:int(f.degrees()[0]))
q0,r0=divmod(res,base*(ss+1))
need(not r0 and max(map(int,q0.degrees()))==0,"entire original base resultant factor")
def zcoef(f,i):return ctx.from_dict({(m[0],m[1],0,m[3]):int(v) for m,v in f.to_dict().items() if m[2]==i})
A,B,C=[zcoef(E0,j) for j in (2,1,0)];Aa,Bb,Cc=[zcoef(E01,j) for j in (2,1,0)]
J=A*Bb-Aa*B;M=A*Cc-Aa*C
need(A*E01-Aa*E0==J*zz+M,"original linear reconstruction identity")
def subz(f):
 d=int(f.degrees()[2])
 return sum((zcoef(f,i)*(-M)**i*J**(d-i) for i in range(d+1)),ctx.from_dict({}))
Q=4*ee**3-1;D=2*ee**3+1-12*ee**4
bs=-2*ss**2*(ss-2)*(ss+6);delta=xx**2-4*zz
qpair=xx**3-5*xx**2+xx**2*zz-6*xx*zz+32*zz-5*zz**2
F1=3*D*LD**2+2*(2*ee**3+1)*Q*bs*(ss+1)*LL
F2=4*ee**2*Q*LL*(zz+xx+1)-D*(ss+1)*delta*qpair
f1,f2,Lnum=subz(F1),subz(F2),subz(LL)
R1=base.resultant(f1,1);R2=base.resultant(f2,1);G=R1.gcd(R2)
d8=cv(25*s**8+410*s**7+680*s**6-10064*s**5-8768*s**4+62976*s**3+15488*s**2-118016*s+61440)
d12=cv(625*s**12+8500*s**11+46500*s**10+225280*s**9+1204220*s**8+3351264*s**7+177200*s**6-16389344*s**5-25822080*s**4-8725120*s**3+6534144*s**2+4976640*s+884736)
display=ss**25*(ss+1)**10*(ss+2)**12*(ss-2)**3*(ss+6)**3*d8**2*d12**4
cg,rg=divmod(G,display)
need(not rg and max(map(int,cg.degrees()))==0,"entire exceptional-source factorization")
R1r,r1=divmod(R1,G);R2r,r2=divmod(R2,G)
need(not r1 and not r2,"exact residual resultant quotients")
out("integer_resultants",R1s=int(R1.degrees()[0]),R2s=int(R2.degrees()[0]),common_s=int(G.degrees()[0]),residual_s=[int(R1r.degrees()[0]),int(R2r.degrees()[0])])
X=fmpq_poly([0,1])
G9=16*X**9-108*X**8+36*X**7-15*X**6+18*X**4-1
def powmod(a,n,m):
 r=nmod_poly([1],37)
 while n:
  if n&1:r=r*a%m
  a=a*a%m;n//=2
 return r
# Rabin's irreducibility test: the sole prime divisor of degree 9 is 3.
g37=nmod_poly([int(G9[j])%37 for j in range(10)],37);x37=nmod_poly([0,1],37)
r=x37;r3=None
for i in range(1,10):
 r=powmod(r,37,g37)
 if i==3:r3=r
need(r==x37 and (r3-x37).gcd(g37).degree()==0,"G9 irreducible modulo 37")
out("G9_irreducible",prime=37,degree=9)
def pure_s(f):
 need(int(f.degrees()[1])<=0 and int(f.degrees()[2])<=0 and int(f.degrees()[3])<=0,"pure source polynomial")
 a=[fmpq(0)]*(int(f.degrees()[0])+1)
 for m,c in f.to_dict().items():a[m[0]]+=fmpq(int(c))
 return fmpq_poly(a)
def qp(f,R,var=1,x0=None):
 need(int(f.degrees()[3])<=0,"QQ polynomial independent of e")
 n=max(0,int(f.degrees()[var]));a=[R.zero]*(n+1)
 for m,c in f.to_dict().items():
  if var==1:need(m[2]==0,"no z in x polynomial");v=R.el(fmpq_poly([0]*m[0]+[int(c)]))
  else:v=R.el(fmpq_poly([0]*m[0]+[int(c)])*(x0**m[1]%R.G))
  a[m[var]]=R.el(a[m[var]]+v)
 return R.trim(a)
gates=[];structures=[]
def addgate(label,R,P,f,g,kind,x0=None):
 if len(P)<=1:
  structures.append(dict(label=label,dimension=0));return
 P=R.monic(P,label+" final")
 gates.append(dict(label=label,R=R,P=P,f=f,g=g,kind=kind,x0=x0))
 structures.append(dict(label=label,dimension=R.n*(len(P)-1),extension_degree=len(P)-1,modulus_hash=digest(P)))
for name,pol in (("D8",d8),("D12",d12)):
 R=QQ(pure_s(pol),name)
 R.inv(R.s*(R.s-2)*(R.s+6)*(R.s+1),"ordinary source")
 P=R.monic(qp(base,R),name+" base")
 JP=qp(J,R);MP=qp(M,R);LP=qp(Lnum,R)
 gj=R.gcd(P,JP,name+" J support")
 good,rj=R.remove(P,JP,name+" J primary")
 good,rl=R.remove(good,LP,name+" physical L primary")
 structures.append(dict(label=name+" removed",J_degrees=rj,L_degrees=rl,J_support_degree=len(gj)-1))
 addgate(name+" J nonzero L nonzero",R,good,f1,f2,"x")
 if len(gj)>1:
  need(len(gj)==2,name+" J-zero support is linear")
  need(gj[1]==R.one,name+" monic J support");x0=R.el(-gj[0])
  need(R.eval(gj,x0)==0,name+" J root")
  mv=R.eval(MP,x0)
  if mv:
   R.inv(mv,name+" J-zero M obstruction")
   structures.append(dict(label=name+" J zero",status="excluded by nonzero M"));continue
  P0=qp(E0,R,var=2,x0=x0);P1=qp(E01,R,var=2,x0=x0)
  Pz=R.gcd(P0,P1,name+" original J-zero equations")
  Lz=qp(LL,R,var=2,x0=x0)
  Pz,rlz=R.remove(Pz,Lz,name+" original J-zero physical L")
  structures.append(dict(label=name+" J zero L removed",degrees=rlz))
  addgate(name+" original J zero L nonzero",R,Pz,F1,F2,"z",x0)
# s=-2: use the original equations, without dividing by J.
need(S.expand((E+S.diff(E,s)).subs(s,-2)-32*(3*x+3*z+4))==0,"s=-2 original linear identity")
zminus=-x-S.Rational(4,3);C3=3*x**3+48*x**2+344*x+512
need(S.expand(E.subs({s:-2,z:zminus})-C3/9)==0,"s=-2 original cubic")
Rminus=QQ(fmpq_poly([512,344,48,3]),"s=-2 cubic")
Lm=S.Poly(S.expand(L.subs({s:-2,z:zminus})),x)
lm=Rminus.el(fmpq_poly([fmpq(str(Lm.nth(i))) for i in range(Lm.degree()+1)]))
Rminus.inv(lm,"physical L")
addgate("s=-2 original cubic",Rminus,[Rminus.zero,Rminus.one],F1,F2,"minus")
out("QQ_structures_complete",structures=structures,verified_inverse_count=len(units))
# The following algebra is the specialization of the displayed finite free
# QQ algebra. Each nonzero norm therefore lifts to a unit after extension to
# the number field QQ[e]/G9; irreducibility was proved above.
def qmod(q,p):
 q=Fraction(str(q));need(q.denominator%p!=0,"specialization denominator")
 return q.numerator%p*pow(q.denominator,-1,p)%p
class ModAlg:
 def __init__(self,gate,p):
  self.p=p;self.n=gate["R"].n;self.m=len(gate["P"])-1
  self.G=nmod_poly([qmod(gate["R"].G[i],p) for i in range(self.n+1)],p)
  self.P=[nmod_poly([qmod(a[i],p) for i in range(max(0,int(a.degree())+1))],p)%self.G for a in gate["P"]]
  need(int(self.G.degree())==self.n and self.P[-1]==nmod_poly([1],p),"monic specialization")
  self.zero=nmod_poly([],p);self.one=nmod_poly([1],p)
 def el(self,a):
  a=list(a)
  while len(a)>self.m:
   c=a.pop();d=len(a)-self.m
   for j in range(self.m):a[d+j]=(a[d+j]-c*self.P[j])%self.G
  return a+[self.zero]*(self.m-len(a))
 def const(self,a):return self.el([nmod_poly([a%self.p],self.p)])
 def base(self,a):return self.el([nmod_poly([qmod(a[i],self.p) for i in range(max(0,int(a.degree())+1))],self.p)%self.G])
 def add(self,a,b):return [(u+v)%self.G for u,v in zip(a,b)]
 def mul(self,a,b):
  r=[self.zero]*(2*self.m-1)
  for i,u in enumerate(a):
   for j,v in enumerate(b):r[i+j]=(r[i+j]+u*v)%self.G
  return self.el(r)
 def eval(self,f,images):
  powers=[]
  for j,v in enumerate(images):
   a=[self.const(1)]
   for _ in range(max(0,int(f.degrees()[j]))):a.append(self.mul(a[-1],v))
   powers.append(a)
  r=self.const(0)
  for mon,c in f.to_dict().items():
   a=self.const(int(c))
   for j,n in enumerate(mon):a=self.mul(a,powers[j][n])
   r=self.add(r,a)
  return r
 def det(self,a):
  N=self.n*self.m;rows=[[0]*N for _ in range(N)]
  for j in range(self.m):
   for i in range(self.n):
    v=[self.zero]*self.m;v[j]=nmod_poly([0]*i+[1],self.p)
    w=self.mul(a,v);col=j*self.n+i
    for jj in range(self.m):
     for ii in range(self.n):rows[jj*self.n+ii][col]=int(w[jj][ii])
  return int(nmod_mat(rows,self.p).det())
def epoly(f):
 a=[fmpq_poly([]) for _ in range(int(f.degrees()[0])+1)]
 for m,c in f.to_dict().items():a[m[0]]+=fmpq_poly([0]*m[3]+[int(c)])
 a=[v%G9 for v in a]
 while a and not a[-1]:a.pop()
 return a
ER1,ER2=epoly(R1r),epoly(R2r)
def especial(a,p,r):
 out=[]
 for q in a:
  v=0
  for i in reversed(range(max(0,int(q.degree())+1))):v=(v*r+qmod(q[i],p))%p
  out.append(v)
 return nmod_poly(out,p)
attempts=[];success=None
for p in S.primerange(1009,1300):
 roots=[]
 for r in range(1,p):
  v=0
  for j in reversed(range(10)):v=(v*r+int(G9[j]))%p
  if v==0:roots.append(r)
 for er in roots:
  try:
   a,b=especial(ER1,p,er),especial(ER2,p,er)
   need(a.degree()==len(ER1)-1 and b.degree()==len(ER2)-1,"generic Sylvester degrees")
   det=int(a.resultant(b));need(det!=0,"generic 107-order Sylvester unit")
   norms=[]
   for gate in gates:
    B=ModAlg(gate,p);R=gate["R"]
    bv=B.base(R.s);Xv=B.el([B.zero,B.one])
    if gate["kind"]=="x":im=[bv,Xv,B.const(0),B.const(er)]
    elif gate["kind"]=="z":im=[bv,B.base(gate["x0"]),Xv,B.const(er)]
    else:im=[B.const(-2),bv,B.base(R.el(-R.s-fmpq(4,3))),B.const(er)]
    f=B.eval(gate["f"],im);g=B.eval(gate["g"],im);chosen=None
    for lam in range(8):
     candidate=B.add(f,B.mul(B.const(lam),g));dd=B.det(candidate)
     if dd:chosen=dict(label=gate["label"],dimension=B.n*B.m,lambda_value=lam,determinant=dd);break
    need(chosen is not None,gate["label"]+" finite-algebra unit")
    norms.append(chosen)
   success=dict(prime=int(p),e=int(er),sylvester_dimension=len(ER1)+len(ER2)-2,sylvester_determinant=det,norms=norms)
   break
  except AssertionError as ex:
   attempts.append(dict(p=int(p),e=int(er),failure=str(ex)));out("modular_attempt_failed",**attempts[-1])
 if success is not None:break
need(success is not None,"no complete finite-algebra lift obtained")
out("complete",source_sha256=hashlib.sha256(open(__file__,"rb").read()).hexdigest(),scope="H 2+1, Hp=0, essT3=6, isolated H point infinity: excluded",irreducible_prime=37,field_degree=9,QQ_inverse_count=len(units),QQ_inverse_records=units,structures=structures,successful_lift=success,unsuccessful_attempts=attempts)
