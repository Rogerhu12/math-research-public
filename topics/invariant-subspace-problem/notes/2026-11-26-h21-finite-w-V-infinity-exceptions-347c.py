#!/usr/bin/env python3
"""New exact QQ exceptional fibers; completes only after every assertion succeeds."""
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
s,a,w,e=S.symbols('s a w e')
def q(v):return s**3-5*s**2+(s**3-3*s**2+22*s)*v-(3*s**2+3*s+5)*v*v+(s+1)*v**3
def ker(x,y):
 return S.expand(-(y-x)**2*(x**3-5*x*x+(x**3-3*x*x+22*x)*y-(3*x*x+3*x+5)*y*y+(x+1)*y**3))
ka,kw=ker(s,a),ker(s,w)
J3=5*s*(s+2)*a**3-(11*s**3+18*s*s+8*s+32)*a*a+(4*s**4-6*s**3+34*s*s+76*s)*a+4*s**4-10*s**3-20*s*s
need(S.expand((s+1)*S.diff(ka,s)-ka-(a-s)*J3)==0,"full source derivative divided only by a-s")
E=S.expand((s+1)*ker(w,a)-(w+1)*ka)
C3,rem=S.div(S.Poly(E-(w-s)*(a-s)*J3,w),S.Poly((w-s)**2,w))
need(rem.is_zero,"entire original double-root division")
C3=S.expand(C3.as_expr())
Q=4*e**3-1;D=2*e**3+1-12*e**4;bs=-2*s*s*(s-2)*(s+6)
F1=S.expand(3*D*J3.subs(a,w)**2-2*(2*e**3+1)*Q*bs*(s+1)*(w+1)*q(w))
F2=S.expand(D*(a+1)*kw+4*e*e*Q*(w+1)*ka)
need(S.expand(3*D*(kw-(s+1)*S.diff(kw,s))**2+2*(2*e**3+1)*Q*bs*(s+1)*(w+1)*kw-(w-s)**2*F1)==0,"original scale identity")
ctx=fmpz_mpoly_ctx.get(('s','a','w','e'))
cv=lambda f:ctx.from_dict({m:int(c) for m,c in S.Poly(f,s,a,w,e).terms()})
JJ,CC,FF1,FF2=map(cv,[J3,C3,F1,F2])

# The preceding formulas are exactly the original-input polynomials already
# constructed in run 45799548882. This source does not rerun its nested
# resultants; it pays the entire two exceptional finite-source fibers.
expected={
"J3":"459c0078c4ca43acb5baa333e85f256da00b6f43a43d4ad5d74d6473c7ab0653",
"C3":"e86180dd50b06386ba3c5ff3bc6816b807067a40447ff3f487f0689ffd913fa3",
"F1":"86f45e09a85687d63fd99fa25168c84e925c273a6b5fdcf7cd102c8e92c6f736",
"F2":"f9d5a4f0816e7bd5133befb5f9aa53bb1cf1d32a5f6c7ea478943524198defd2"}
for name,f in zip(("J3","C3","F1","F2"),(JJ,CC,FF1,FF2)):
 need(digest(f)==expected[name],name+" agrees with frozen original input")
X=fmpq_poly([0,1])
D8=25*X**8+410*X**7+680*X**6-10064*X**5-8768*X**4+62976*X**3+15488*X**2-118016*X+61440
D2=15*X**2+62*X+32
phys=cv((a+1)*ka)
def apoly(f,R):
 need(int(f.degrees()[2])<=0 and int(f.degrees()[3])<=0,"QQ a polynomial")
 v=[R.zero]*(max(0,int(f.degrees()[1]))+1)
 for m,c in f.to_dict().items():
  v[m[1]]=R.el(v[m[1]]+fmpq_poly([0]*m[0]+[int(c)]))
 return R.trim(v)
class QExt:
 def __init__(self,R,P):
  self.R=R;self.P=P;self.m=len(P)-1
  self.zero=self.el([]);self.one=self.el([R.one])
 def el(self,v):
  v=list(v)
  while len(v)>self.m:
   c=v.pop();j=len(v)-self.m
   for i in range(self.m):v[j+i]=self.R.el(v[j+i]-c*self.P[i])
  return v+[self.R.zero]*(self.m-len(v))
 def const(self,c):return self.el([self.R.el(c)])
 def add(self,v,w):return [self.R.el(x+y) for x,y in zip(v,w)]
 def mul(self,v,w):
  z=[self.R.zero]*(2*self.m-1)
  for i,x in enumerate(v):
   for j,y in enumerate(w):z[i+j]=self.R.el(z[i+j]+x*y)
  return self.el(z)
 def power(self,v,n):
  r=self.one
  while n:
   if n&1:r=self.mul(r,v)
   v=self.mul(v,v);n//=2
  return r
 def eval(self,f):
  need(int(f.degrees()[2])<=0 and int(f.degrees()[3])<=0,"QQ a-only evaluation")
  return self.el(apoly(f,self.R))
gates=[];structures=[]
for label,Dsrc in (("D8",D8),("D2",D2)):
 R=QQ(Dsrc,label)
 R.inv(R.s*(R.s+1)*(R.s+2)*(R.s-2)*(R.s+6),"all ordinary leading sources")
 P=R.monic(apoly(JJ,R),label+" original J3")
 P,removed=R.remove(P,apoly(phys,R),label+" complete nonphysical a primary")
 if len(P)<=1:
  structures.append(dict(label=label,removed_a_primary_degrees=removed,dimension=0,status="all a fibers are nonphysical"))
  continue
 A=QExt(R,P);av=A.el([R.zero,R.one])
 # The physical a+1 inverse follows from exact synthetic division.
 qv,rv=R.div(P,[R.one,R.one],label+" a+1 quotient")
 need(len(rv)==1 and rv[0]==R.eval(P,-R.one),label+" a+1 remainder")
 iv=R.inv(rv[0],label+" a+1 resultant")
 ia=A.el([R.el(-v*iv) for v in qv])
 need(A.mul(A.add(av,A.one),ia)==A.one,label+" a+1 extension inverse")
 def ccoef(i):
  return ctx.from_dict({(m[0],m[1],0,0):int(c) for m,c in CC.to_dict().items() if m[2]==i})
 CP=[A.eval(ccoef(i)) for i in range(4)]
 lc_expected=A.mul(A.const(-R.s-1),A.add(av,A.one))
 need(CP[-1]==lc_expected,label+" exact cubic leading coefficient")
 ilc=A.mul(A.const(-R.inv(R.s+1,label+" isolated cubic source factor")),ia)
 need(A.mul(CP[-1],ilc)==A.one,label+" cubic leading inverse remultiplication")
 CP=[A.mul(v,ilc) for v in CP]
 need(CP[-1]==A.one,label+" monic entire isolated source cubic")
 gate=dict(label=label,R=R,P=P,CP=CP)
 gates.append(gate)
 structures.append(dict(label=label,removed_a_primary_degrees=removed,a_degree=A.m,w_degree=3,dimension=R.n*A.m*3,a_modulus_sha256=digest(P),w_modulus_sha256=digest(CP)))
out("QQ_exceptional_structures",structures=structures,QQ_inverse_count=len(units))
def qmod(q,p):
 q=Fraction(str(q));need(q.denominator%p!=0,"specialization denominator")
 return q.numerator%p*pow(q.denominator,-1,p)%p
class MExt:
 def __init__(self,g,p):
  self.p=p;self.n=g["R"].n;self.m=len(g["P"])-1;self.l=3
  self.G=nmod_poly([qmod(g["R"].G[i],p) for i in range(self.n+1)],p)
  self.z=nmod_poly([],p);self.o=nmod_poly([1],p)
  def bc(v):return nmod_poly([qmod(v[i],p) for i in range(max(0,int(v.degree())+1))],p)%self.G
  self.P=[bc(v) for v in g["P"]]
  self.CP=[[bc(v) for v in c] for c in g["CP"]]
  need(self.P[-1]==self.o and self.CP[-1]==[self.o]+[self.z]*(self.m-1),"monic tower specialization")
  self.az=[self.z]*self.m;self.ao=[self.o]+[self.z]*(self.m-1)
  self.zero=[self.az]*self.l;self.one=[self.ao]+[self.az]*(self.l-1)
 def ae(self,v):
  v=list(v)
  while len(v)>self.m:
   c=v.pop();j=len(v)-self.m
   for i in range(self.m):v[j+i]=(v[j+i]-c*self.P[i])%self.G
  return v+[self.z]*(self.m-len(v))
 def aa(self,v,w):return [(x+y)%self.G for x,y in zip(v,w)]
 def an(self,v):return [-x%self.G for x in v]
 def am(self,v,w):
  z=[self.z]*(2*self.m-1)
  for i,x in enumerate(v):
   for j,y in enumerate(w):z[i+j]=(z[i+j]+x*y)%self.G
  return self.ae(z)
 def el(self,v):
  v=list(v)
  while len(v)>self.l:
   c=v.pop();j=len(v)-self.l
   for i in range(self.l):v[j+i]=self.aa(v[j+i],self.an(self.am(c,self.CP[i])))
  return v+[self.az]*(self.l-len(v))
 def const(self,c):return self.el([self.ae([nmod_poly([c%self.p],self.p)])])
 def add(self,v,w):return [self.aa(x,y) for x,y in zip(v,w)]
 def mul(self,v,w):
  z=[self.az]*(2*self.l-1)
  for i,x in enumerate(v):
   for j,y in enumerate(w):z[i+j]=self.aa(z[i+j],self.am(x,y))
  return self.el(z)
 def eval(self,f,er):
  sim=self.el([self.ae([nmod_poly([0,1],self.p)%self.G])])
  aim=self.el([self.ae([self.z,self.o])])
  wim=self.el([self.az,self.ao])
  im=[sim,aim,wim,self.const(er)]
  powers=[]
  for j,v in enumerate(im):
   a=[self.one]
   for _ in range(max(0,int(f.degrees()[j]))):a.append(self.mul(a[-1],v))
   powers.append(a)
  r=self.const(0)
  for mon,c in f.to_dict().items():
   v=self.const(int(c))
   for j,n in enumerate(mon):v=self.mul(v,powers[j][n])
   r=self.add(r,v)
  return r
 def matrix(self,v):
  N=self.n*self.m*self.l;rows=[[0]*N for _ in range(N)]
  for kk in range(self.l):
   for jj in range(self.m):
    for ii in range(self.n):
     aa=[self.z]*self.m;aa[jj]=nmod_poly([0]*ii+[1],self.p)
     vv=[self.az]*self.l;vv[kk]=aa
     outv=self.mul(v,vv);col=(kk*self.m+jj)*self.n+ii
     for k in range(self.l):
      for j in range(self.m):
       for i in range(self.n):rows[(k*self.m+j)*self.n+i][col]=int(outv[k][j][i])
  return rows
p,er=1031,700
need((16*er**9-108*er**8+36*er**7-15*er**6+18*er**4-1)%p==0,"original G9 specialization")
norms=[]
for gate in gates:
 B=MExt(gate,p)
 f=B.matrix(B.eval(FF1,er));g=B.matrix(B.eval(FF2,er));N=len(f)
 chosen=None
 for lam in range(64):
  mm=[[(u+lam*v)%p for u,v in zip(fr,gr)] for fr,gr in zip(f,g)]
  det=int(nmod_mat(mm,p).det())
  if det:
   chosen=dict(label=gate["label"],dimension=N,lambda_value=lam,determinant=det);break
 need(chosen is not None,gate["label"]+" complete finite-algebra norm")
 norms.append(chosen);out("exceptional_norm",**chosen)
out("complete",source_sha256=hashlib.sha256(open(__file__,"rb").read()).hexdigest(),scope="exact D8/D2 entire fibers for finite H w and one V source infinity",structures=structures,QQ_inverse_count=len(units),QQ_inverse_records=units,prime=p,e=er,norms=norms,generic_input_run=45799548882,generic_input_job=139838879254)
