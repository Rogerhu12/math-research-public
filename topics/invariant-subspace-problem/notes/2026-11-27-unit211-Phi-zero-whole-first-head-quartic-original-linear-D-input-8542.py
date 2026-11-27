#!/usr/bin/env python3
"""NEW entire first-quadratic-head ZERO Phi weight curve, not bb35.
The first head has constant Q^4 leading coefficient -1/12. Keep the
whole monic Q-quartic algebra over QQ(u), without choosing a Q root.
The three original means have rank-two homogeneous heads here; their
actual adjugate gives a linear original relation L=a*T+b*z+c.
Homogenize the original quadratics against L by polynomial identities,
never invert b or any lambda polynomial. Return the actual D target
in the fixed three-coefficient module, cancel only exact common factors,
then use complete original quadratic/moment resultants, with every
lambda-leading-zero fiber retained by exact polynomial division.
All genuine weight-algebra inverses are checked on all four components;
every final u denominator support is retained. No field/reduced claim,
no previous cofactor/F6 recurrence/long lambda module is rerun.
2026-11-28 Asia/Taipei. 120 seconds /1 GiB.
Self-contained compact original scalar input.
"""
import time,json,hashlib,zlib,base64,signal,resource
from pathlib import Path
from flint import fmpq,fmpq_poly
signal.alarm(120);resource.setrlimit(resource.RLIMIT_AS,(1024**3,1024**3))
started=time.perf_counter()
def say(stage,**kw):
 kw.update(stage=stage,seconds=time.perf_counter()-started)
 print(json.dumps(kw,separators=(",",":")),flush=True)
def pol(v=()):
 if isinstance(v,fmpq_poly):return v
 if isinstance(v,(int,fmpq)):v=[v]
 return fmpq_poly([fmpq(c) for c in v])
zero=pol();one=pol(1);up=pol([0,1])
def exact(a,b):
 q,r=divmod(a,b);assert not r and q*b==a
 return q
def monic(p):
 assert p
 return p/p[p.degree()]
def coefficients(p):return [str(c) for c in p.coeffs()]
def pdigest(p):
 raw=json.dumps(coefficients(p),separators=(",",":")).encode()
 return dict(degree=int(p.degree()),bytes=len(raw),sha256=hashlib.sha256(raw).hexdigest())
# g=-12*H1, the actual first quadratic-head residual. Its Q head is 1.
g=[pol([64,-272,512,-544,336,-112,16]),
   pol([-112,348,-496,440,-248,80,-12]),
   pol([60,-123,104,-52,13]),
   pol([-13,fmpq(53,4),-3]),one]
cover=one
def record_denominator(p):
 global cover
 if p.degree()<=0:return
 p=monic(p);cover=monic(cover*exact(p,cover.gcd(p)))
class Rat:
 def __init__(self,n=0,d=None):
  if isinstance(n,Rat):self.n=n.n;self.d=n.d;return
  n=pol(n);d=one if d is None else pol(d);assert d
  if not n:self.n=zero;self.d=one;return
  gg=n.gcd(d);n=exact(n,gg);d=exact(d,gg);c=d[d.degree()]
  self.n=n/c;self.d=d/c
 def __bool__(self):return bool(self.n)
 def __neg__(self):return Rat(-self.n,self.d)
 def __add__(self,v):
  v=Rat(v);gg=self.d.gcd(v.d);a=exact(self.d,gg);b=exact(v.d,gg)
  return Rat(self.n*b+v.n*a,a*v.d)
 __radd__=__add__
 def __sub__(self,v):return self+-Rat(v)
 def __rsub__(self,v):return Rat(v)+-self
 def __mul__(self,v):
  v=Rat(v);gg=self.n.gcd(v.d);hh=v.n.gcd(self.d)
  return Rat(exact(self.n,gg)*exact(v.n,hh),exact(self.d,hh)*exact(v.d,gg))
 __rmul__=__mul__
 def __truediv__(self,v):
  v=Rat(v);assert v
  return self*Rat(v.d,v.n)

def reduce_numerators(cc):
 cc=list(cc)
 while len(cc)<4:cc.append(zero)
 for j in range(len(cc)-1,3,-1):
  lead=cc[j]
  if lead:
   for i in range(4):cc[j-4+i]=cc[j-4+i]-lead*g[i]
   cc[j]=zero
 assert not any(cc[4:])
 return tuple(cc[:4]),one
def cgcd(dd,nn):
 gg=dd
 for p in nn:
  if p:gg=gg.gcd(p)
  if gg.degree()==0:break
 return gg
inverses=[];inverse_cache={}
class Nonunit(Exception):pass
class A:
 """The ENTIRE rank-four algebra, without assuming a field or reduced."""
 def __init__(self,v=0,d=None):
  if isinstance(v,A) and d is None:self.n=v.n;self.d=v.d;return
  if isinstance(v,Rat) and d is None:v,d=v.n,v.d
  if not isinstance(v,(tuple,list)):v=[pol(v)]
  else:v=[pol(c) for c in v]
  nn,rd=reduce_numerators(v);dd=rd*(one if d is None else pol(d));assert dd
  if not any(nn):self.n=(zero,)*4;self.d=one;return
  gg=cgcd(dd,nn)
  if gg.degree()>0:nn=tuple(exact(n,gg) for n in nn);dd=exact(dd,gg)
  c=dd[dd.degree()];self.n=tuple(n/c for n in nn);self.d=dd/c
 @staticmethod
 def accepts(v):return isinstance(v,(A,Rat,fmpq_poly,fmpq,int,tuple,list))
 def __bool__(self):return any(self.n)
 def __neg__(self):return A(tuple(-n for n in self.n),self.d)
 def __add__(self,v):
  if not self.accepts(v):return NotImplemented
  v=A(v)
  if not self:return v
  if not v:return self
  gg=self.d.gcd(v.d);a=exact(self.d,gg);b=exact(v.d,gg)
  return A(tuple(x*b+y*a for x,y in zip(self.n,v.n)),a*v.d)
 __radd__=__add__
 def __sub__(self,v):
  if not self.accepts(v):return NotImplemented
  return self+-A(v)
 def __rsub__(self,v):
  if not self.accepts(v):return NotImplemented
  return A(v)+-self
 def __mul__(self,v):
  if not self.accepts(v):return NotImplemented
  v=A(v)
  if not self or not v:return A()
  gg=cgcd(v.d,self.n);hh=cgcd(self.d,v.n)
  aa=[exact(n,gg) for n in self.n];bb=[exact(n,hh) for n in v.n]
  cc=[pol() for _ in range(7)]
  for i,x in enumerate(aa):
   for j,y in enumerate(bb):
    if x and y:cc[i+j]+=x*y
  return A(cc,exact(self.d,hh)*exact(v.d,gg))
 __rmul__=__mul__
 def __eq__(self,v):
  if not self.accepts(v):return False
  v=A(v);return all(x*v.d==y*self.d for x,y in zip(self.n,v.n))
 def inverse(self,label="actual whole Q-quartic-algebra inverse"):
  if not self:raise Nonunit(label+": zero")
  if self==1:return A(1)
  key=tuple(str(n) for n in self.n)+(str(self.d),)
  if key in inverse_cache:return inverse_cache[key]
  if not any(self.n[1:]):out=A(self.d,self.n[0])
  else:
   cols=[self*A([0]*j+[1]) for j in range(4)]
   mm=[[cols[j].n[i] for j in range(4)]+[one if i==0 else zero] for i in range(4)]
   previous=one
   for j in range(3):
    if not mm[j][j]:
     sw=next((i for i in range(j+1,4) if mm[i][j]),None)
     if sw is None:raise Nonunit(label+": actual multiplication norm zero")
     mm[j],mm[sw]=mm[sw],mm[j]
    pivot=mm[j][j]
    for i in range(j+1,4):
     for h in range(j+1,5):
      mm[i][h]=exact(mm[i][h]*pivot-mm[i][j]*mm[j][h],previous)
     mm[i][j]=zero
    previous=pivot
   if not mm[3][3]:raise Nonunit(label+": actual multiplication norm zero")
   sol=[Rat() for _ in range(4)]
   for i in range(3,-1,-1):
    sol[i]=(Rat(mm[i][4])-sum((Rat(mm[i][j])*sol[j] for j in range(i+1,4)),Rat()))/Rat(mm[i][i])
   sol=[s*Rat(c.d) for s,c in zip(sol,cols)]
   den=one
   for c in sol:den=monic(den*exact(c.d,den.gcd(c.d)))
   out=A([c.n*exact(den,c.d) for c in sol],den)
  assert self*out==1
  record_denominator(self.d);record_denominator(out.d)
  inverse_cache[key]=out
  inverses.append(dict(label=label,inputDenominator=pdigest(self.d),inverseDenominator=pdigest(out.d)))
  return out
 def __truediv__(self,v):
  if not self.accepts(v):return NotImplemented
  return self*A(v).inverse()
 def __rtruediv__(self,v):
  if not self.accepts(v):return NotImplemented
  return A(v)*self.inverse()
 def __pow__(self,n):
  if n<0:return self.inverse()**(-n)
  ans=A(1);v=self
  while n:
   if n&1:ans=ans*v
   n//=2
   if n:v=v*v
  return ans
 def data(self):return dict(n=[coefficients(p) for p in self.n],d=coefficients(self.d))
 def complexity(self):return max([int(p.degree()) for p in self.n]+[int(self.d.degree())])
class U:
 def __init__(self,v=0):
  if isinstance(v,U):self.c=list(v.c);return
  self.c=[A(c) for c in v] if isinstance(v,(tuple,list)) else [A(v)]
  while self.c and not self.c[-1]:self.c.pop()
 def __bool__(self):return bool(self.c)
 def __neg__(self):return U([-c for c in self.c])
 def __add__(self,v):
  v=U(v);n=max(len(self.c),len(v.c))
  return U([(self.c[i] if i<len(self.c) else A())+(v.c[i] if i<len(v.c) else A()) for i in range(n)])
 __radd__=__add__
 def __sub__(self,v):return self+-U(v)
 def __rsub__(self,v):return U(v)+-self
 def __mul__(self,v):
  v=U(v)
  if not self or not v:return U()
  cc=[A() for _ in range(len(self.c)+len(v.c)-1)]
  for i,x in enumerate(self.c):
   for j,y in enumerate(v.c):
    if x and y:cc[i+j]=cc[i+j]+x*y
  return U(cc)
 __rmul__=__mul__
 def __eq__(self,v):
  v=U(v);return len(self.c)==len(v.c) and all(x==y for x,y in zip(self.c,v.c))
 def __pow__(self,n):
  ans=U(1);v=self
  while n:
   if n&1:ans=ans*v
   n//=2
   if n:v=v*v
  return ans
 def degree(self):return len(self.c)-1
 def complexity(self):return max((c.complexity() for c in self.c),default=-1)
 def data(self):return [c.data() for c in self.c]
 def normalize(self,label):
  if not self:return self
  iv=self.c[-1].inverse(label)
  out=U([c*iv for c in self.c])
  assert out*self.c[-1]==self and out.c[-1]==1
  return out
divisions=0;trace=hashlib.sha256()
def divide(a,b,label):
 global divisions
 a=U(a);b=U(b);assert b;original=U(a)
 iv=b.c[-1].inverse(label+" lambda-leading")
 quotient=[A() for _ in range(max(0,len(a.c)-len(b.c)+1))]
 while a and len(a.c)>=len(b.c):
  shift=len(a.c)-len(b.c);c=a.c[-1]*iv
  quotient[shift]=quotient[shift]+c
  cc=a.c[:]
  for i,v in enumerate(b.c):cc[shift+i]=cc[shift+i]-c*v
  a=U(cc)
 q=U(quotient)
 assert q*b+a==original and a.degree()<b.degree()
 divisions+=1
 # All coefficient products above were actually returned. Retain a compact
 # digest of the composed division identities, not a giant coefficient cache.
 for p in (original,b,q,a):
  trace.update(json.dumps(p.data(),separators=(',',':')).encode());trace.update(b"\n")
 return q,a
def euclid(a,b,label):
 a=U(a);b=U(b);step=0
 while b:
  q,r=divide(a,b,label)
  a,b=b,r;step+=1
  say("new_original_whole_quartic_lambda_division_returned",pair=label,step=step,
      divisorDegree=a.degree(),remainderDegree=b.degree(),
      coefficientUDegree=max(a.complexity(),b.complexity()),
      allFourWeightComponentsOfDivisionIdentityReturned=True,
      retainedUCoverDegree=int(cover.degree()))
 return a.normalize(label+" final actual lambda head")
class P:
 """Finite polynomial in (lambda,T,z) with whole Q-quartic coefficients."""
 def __init__(self,v=0):
  if isinstance(v,P):self.v=dict(v.v);return
  c=A(v);self.v={(0,0,0):c} if c else {}
 @classmethod
 def from_terms(cls,terms):
  ans=cls();ans.v={tuple(k):A(c) for k,c in terms.items() if A(c)}
  return ans
 def __bool__(self):return bool(self.v)
 def __add__(self,v):
  v=P(v);out=dict(self.v)
  for k,c in v.v.items():
   out[k]=out.get(k,A())+c
   if not out[k]:del out[k]
  return P.from_terms(out)
 __radd__=__add__
 def __neg__(self):return P.from_terms({k:-c for k,c in self.v.items()})
 def __sub__(self,v):return self+-P(v)
 def __rsub__(self,v):return P(v)+-self
 def __mul__(self,v):
  v=P(v);out={}
  for e,c in self.v.items():
   for f,d in v.v.items():
    k=tuple(i+j for i,j in zip(e,f));out[k]=out.get(k,A())+c*d
  return P.from_terms(out)
 __rmul__=__mul__
 def __truediv__(self,v):return self*A(v).inverse("original scalar weight divisor")
 def __pow__(self,n):
  assert n>=0
  ans=P(1);v=self
  while n:
   if n&1:ans=ans*v
   n//=2
   if n:v=v*v
  return ans
 def __eq__(self,v):return self.v==P(v).v
def from_lambda(v):
 v=U(v)
 return P.from_terms({(i,0,0):c for i,c in enumerate(v.c) if c})
def quadelements(p):
 slots={(0,0):0,(1,0):1,(0,1):2,(2,0):3,(1,1):4,(0,2):5}
 rows=[{} for _ in range(6)]
 for (l,t,z),c in p.v.items():
  assert (t,z) in slots
  idx=slots[(t,z)];rows[idx][l]=c
 out=[]
 for row in rows:
  out.append(U([row.get(i,A()) for i in range(max(row,default=-1)+1)]))
 return out
def det3(a):
 return a[0][0]*(a[1][1]*a[2][2]-a[1][2]*a[2][1])-a[0][1]*(a[1][0]*a[2][2]-a[1][2]*a[2][0])+a[0][2]*(a[1][0]*a[2][1]-a[1][1]*a[2][0])
def adj3(a):
 out=[]
 for i in range(3):
  row=[]
  for j in range(3):
   rr=[k for k in range(3) if k!=j];cc=[k for k in range(3) if k!=i]
   v=a[rr[0]][cc[0]]*a[rr[1]][cc[1]]-a[rr[0]][cc[1]]*a[rr[1]][cc[0]]
   row.append(v if (i+j)%2==0 else -v)
  out.append(row)
 return out
def rowmul(row,M):
 return [sum((row[i]*M[i][j] for i in range(3)),U()) for j in range(3)]
def exactU(a,b,label):
 q,r=divide(a,b,label)
 assert not r and q*U(b)==U(a)
 return q
def gcdU(a,b,label):return euclid(a,b,label)

def run_new_input():
 u=A(up);Q=A([0,1])
 assert sum((A(c0)*(Q**i) for i,c0 in enumerate(g)),A())==0
 lam=P.from_terms({(1,0,0):1})
 Tr=P.from_terms({(0,1,0):1});z=P.from_terms({(0,0,1):1})
 ell=1-2*(u-1)*(u-2)/Q
 delta=1-Q;m=u-ell;V2=2*u-ell*Q;T0=V2-2*u*u
 J=2*u*(1-u)+ell*Q
 P02=(2-3*u)*V2-Q*u+2*u**3;Pf=T0*(J-Q)
 M=ell*V2-u*u;bc=M/(4*delta)
 A2=2*lam*lam-2*lam+1
 G=lam*P02+(u-1)*T0
 Pc=Q*P02*(ell+Tr)-G*T0
 ff=-Pc/Pf
 assert T0+4*u-4+Q==0
 assert T0==-Q-4*(u-1) and J-Q==-4*(u-1)**2
 assert P02==2*(u-1)*ell*Q
 assert Pf*ff+Pc==0
 aa=1-ell
 vn=J*ff-G+bc*z
 wstar=T0+4*u*ff
 nn=Q*wstar-2*vn
 ww=lam-1-Tr
 ii=((vn+aa*u*Q)**2-2*u*Q*vn+2*aa*u*u*Q*Q
     -4*aa*u*Q*Q*ff+bc*z*z+z*(4*bc*u*Q-ell*vn))
 Rbar=ii+(m/(2*delta))*z*nn
 W4=(8*bc*delta*Q*Q*ell*T0-4*ell*delta*vn*vn-ell*nn*nn
     +4*m*vn*nn+32*bc*delta*Q*ff*vn+16*bc*bc*delta*z*z
     +32*bc*bc*delta*Q*(u-1)*z-8*bc*ell*delta*z*vn+4*bc*m*z*nn)
 s0=2*ell*vn-(m/delta)*nn
 d0=-2*m*vn+ell*nn
 Obar=(32*bc*bc*aa*Q*Q*delta*(u-1)+4*bc*Q*delta*s0
       +32*bc*bc*Q*delta*vn-64*bc*bc*Q*Q*delta*ff
       +4*bc*Q*(1-u+2*ff)*d0-s0*d0-8*bc*bc*m*z*z
       -16*bc*bc*Q*z*(m*(u-1)+ell*delta)+8*bc*bc*z*nn)
 al=ell*(1-u)-m
 ber=ell*delta-m*(1-u)
 av=(2*u-1)*ell+3*m
 bur=(2*u-1)*m+3*ell*delta
 Nstar=(al*(4*delta*vn*vn+nn*nn)+4*ber*vn*nn
        +8*bc*delta*Q*vn*wstar-24*bc*delta*Q*Q*ff*wstar
        +16*aa*bc*delta*Q*Q*(u-1)*wstar+64*bc*delta*Q*Q*u*ff*ff
        -32*bc*delta*Q*u*ff*vn+16*bc*delta*Q*Q*(1+aa)*T0*ff
        +16*bc*delta*Q*(aa*Q-T0)*vn+4*bc*delta*av*z*vn
        -2*bc*bur*z*nn+16*bc*bc*delta*Q*z*(2*ff+T0-aa*Q)
        -8*u*bc*bc*delta*z*z)
 N1=Nstar-16*bc*delta*Q*Q*lam*P02*ww
 
 quads=[quadelements(p) for p in [Rbar,W4,Obar,N1]]
 basisP=[P(1),Tr,z,Tr*Tr,Tr*z,z*z]
 for p,row in zip([Rbar,W4,Obar,N1],quads):
  assert sum((from_lambda(c)*v for c,v in zip(row,basisP)),P())==p
 for row in quads:assert all(c.degree()<=0 for c in row[3:])
 head=[[c.c[0] if c.c else A() for c in row[3:]] for row in quads[:3]]
 assert det3(head)==0
 adj=adj3(head);alpha=next((row for row in adj if any(row)),None)
 if alpha is None:
  say("new_H1_mean_head_has_no_rank_two_row",noComponentDiscarded=True,noGenericExclusionClaim=True)
  return False
 assert all(sum((alpha[i]*head[i][j] for i in range(3)),A())==0 for j in range(3))
 c,a,b=[sum((alpha[i]*quads[i][j] for i in range(3)),U()) for j in range(3)]
 L=from_lambda(c)+from_lambda(a)*Tr+from_lambda(b)*z
 assert L==sum((alpha[i]*p for i,p in enumerate([Rbar,W4,Obar])),P())
 say("new_entire_H1_original_mean_linear_relation",
  wholeQAlgebraRank=4,originalHeadExactlyZero=True,
  originalAdjugateRowActuallyNonzero=True,lambdaDegrees=[a.degree(),b.degree(),c.degree()],
  noCoefficientOfThisLinearRelationInverted=True,
  allThreeOriginalMeansActuallyMultipliedBack=True,
  coefficientData=[p.data() for p in [a,b,c]],allWeightDenominatorZeroFibersRetained=True)
 if not L:
  say("new_H1_original_linear_relation_is_zero",noGenericExclusionClaim=True)
  return False
 def homogenized_quad(row,p,label):
  q0,qt,qz,qtt,qtz,qzz=row
  rr=[b*b*q0-b*c*qz+c*c*qzz,
      b*b*qt-b*(a*qz+c*qtz)+2*a*c*qzz,
      b*b*qtt-a*b*qtz+a*a*qzz]
  ptilde=sum((from_lambda(v)*(Tr**i) for i,v in enumerate(rr)),P())
  multiplier=from_lambda(b)*(from_lambda(qtz)*Tr+from_lambda(qz)+2*from_lambda(qzz)*z)-from_lambda(qzz)*L
  assert from_lambda(b*b)*p-ptilde==L*multiplier
  say("new_H1_original_linear_homogenization",original=label,TMaxDegree=2,
      lambdaCoefficientDegrees=[v.degree() for v in rr],
      completePolynomialIdentityReturned=True,originalBZeroBranchRetainedWithoutAnyInverse=True)
  return rr
 mat=[homogenized_quad(row,p,label) for row,p,label in
  [(quads[0],Rbar,"mean_R"),(quads[1],W4,"mean_W"),(quads[3],N1,"original_N1")]]
 drow=[U([1,-2,2])*ell,U(),U(-1)]
 det=det3(mat)
 if not det:
  say("new_H1_original_D_target_fixed_matrix_singular",noGenericExclusionClaim=True)
  return False
 ad=adj3(mat);num=rowmul(drow,ad)
 assert rowmul(num,mat)==[det*v for v in drow]
 gamma=det
 for i,p in enumerate(num):gamma=gcdU(gamma,p,"new D common cancellation "+str(i))
 den=exactU(det,gamma,"new D reduced determinant")
 multipliers=[exactU(p,gamma,"new D reduced multiplier "+str(i)) for i,p in enumerate(num)]
 assert rowmul(multipliers,mat)==[den*v for v in drow]
 say("complete_new_H1_original_same_point_D_lambda_necessary_polynomial",
  lambdaDegree=den.degree(),cancelledCommonDegree=gamma.degree(),
  completeThreeCoefficientOriginalIdentityReturned=True,
  actualIdentity="den(lambda)*D is a polynomial combination of three homogenized ORIGINAL quadratics",
  allTemporaryLambdaZeroFibersPreservedByExactPolynomialCancellation=True,
  noBLinearHeadOrPhysicalDInverseUsed=True,exactPolynomial=den.data())
 current=den.normalize("actual D lambda leading")
 initial_degree=current.degree()
 A2l=U([1,-2,2]);B3l=U([-1,3,-6,4])
 moment=[M*ell**4*(B3l**2)-4*m**2*ell**3*(A2l**3),
  -6*M*ell**3*A2l*B3l,(9*M+12*m**2)*ell**2*(A2l**2),
  4*M*ell**2*B3l,-12*(M+m*m)*ell*A2l,U(),U(4*ell*ell*delta)]
 formalD=ell*A2-Tr*Tr
 formalK=ell**2*(4*lam**3-6*lam**2+3*lam-1)-3*ell*Tr*A2+2*Tr**3
 formalF6=M*(formalK**2)-4*m*m*(formalD**3)
 assert sum((from_lambda(v)*(Tr**i) for i,v in enumerate(moment)),P())==formalF6
 say("new_H1_original_moment_coefficients",fixedTDegree=6,
  lambdaCoefficientDegrees=[v.degree() for v in moment],
  completeOriginalF6IdentityReturned=True,noOldThreeGeneratorF6RecurrenceReplayed=True)
 def ttrim(v):
  v=list(v)
  while v and not v[-1]:v.pop()
  return v
 def tadd(p,q):
  out=[U() for _ in range(max(len(p),len(q)))]
  for i,v in enumerate(p):out[i]=out[i]+v
  for i,v in enumerate(q):out[i]=out[i]+v
  return ttrim(out)
 def tmul(p,q):
  if not p or not q:return []
  out=[U() for _ in range(len(p)+len(q)-1)]
  for i,v in enumerate(p):
   for j,w0 in enumerate(q):out[i+j]=out[i+j]+v*w0
  return ttrim(out)
 def quadratic_resultant(row,p,label):
  cc,bb,aa=row;p=ttrim(p);n=len(p)-1
  assert aa and n>=0
  if n==0:return p[0]*p[0]
  Uk,Vk=U(1),U();Hk=[]
  accumU=U();accumV=(aa**(n-1))*p[0];accumH=[]
  for k in range(1,n+1):
   left=[U() for _ in range(k+1)]
   left[k]=aa**(k-1);left[1]=left[1]-Uk;left[0]=left[0]-Vk
   assert ttrim(left)==tmul(row,Hk)
   weight=(aa**(n-k))*p[k]
   accumU=accumU+weight*Uk;accumV=accumV+weight*Vk
   accumH=tadd(accumH,[weight*v for v in Hk])
   if k<n:
    Hk=tadd([Uk],tmul([U(),aa],Hk))
    Uk,Vk=aa*Vk-bb*Uk,-cc*Uk
  scaled=[(aa**(n-1))*v for v in p]
  assert ttrim(scaled)==tadd([accumV,accumU],tmul(row,accumH))
  numerator=aa*accumV*accumV-bb*accumU*accumV+cc*accumU*accumU
  answer=exactU(numerator,aa**(n-1),"new universal a-power division "+label)
  assert answer*(aa**(n-1))==numerator
  say("new_complete_original_fixed_quadratic_resultant",
      label=label,fixedDegrees=[2,n],fixedSylvesterOrder=2+n,lambdaDegree=answer.degree(),
      completePseudoRemainderAndExactNormDivisionProductsReturned=True,
      noLambdaLeadingZeroFiberInvertedOrDiscarded=True,
      universalFormula="Res(q,p)=(a*V^2-b*U*V+c*U^2)/a^(n-1)")
  return answer
 projection_stages=[]
 for row,label in zip(mat,["mean_R","mean_W","original_N1"]):
  if current.degree()==0:break
  if not row[2]:
   say("new_quad_T2_coefficient_identically_zero",original=label,allFibersRetained=True)
   continue
  proj=quadratic_resultant(row,moment,label+" and original F6")
  if not proj:
   say("new_F6_resultant_identically_zero",original=label,noCoverFromThisProjection=True)
   continue
  current=gcdU(current,proj,"new D equation and "+label+" F6 resultant")
  projection_stages.append([label,proj.degree(),current.degree()])
  say("new_H1_original_lambda_common_constraint",usedOriginal=label,
      remainingLambdaDegree=current.degree(),genericWholeH1CurveExcluded=(current.degree()==0))
 if current.degree()>0:
  Dr=formalD;Kr=formalK;B3=4*lam**3-6*lam**2+3*lam-1
  sn=ell*B3-A2*Tr;zn=Tr*B3-A2*A2
  Znum=u*sn-2*Tr*Dr;Snum=sn+(3-2*lam)*Dr
  NF4=4*m*((3-4*lam)*Q*Dr*Dr-J*zn*Dr)+2*Snum*(-2*u*Q*Kr+J*Znum)
  NC4=(4*m*G*zn*Dr-2*G*Snum*Znum-Q*T0*Snum*Kr
       +4*m*Q*ww*u*(3-2*lam)*Dr*Dr
       +2*m*Q*ww*u*sn*Dr-2*Q*ww*(u-ell*Q)*Kr*Dr)
  NV=NF4*ff+NC4+2*bc*Snum*Znum*z
  assert all(j<=1 for l,t,j in NV.v)
  Nvz=P.from_terms({(l,t,0):v for (l,t,j),v in NV.v.items() if j==1})
  NVh=from_lambda(b)*NV-L*Nvz
  assert all(j==0 for l,t,j in NVh.v)
  tmax=max((t for l,t,j in NVh.v),default=-1);nvcols=[]
  for t in range(tmax+1):
   ll={l:v for (l,k,j),v in NVh.v.items() if k==t}
   nvcols.append(U([ll.get(l,A()) for l in range(max(ll,default=-1)+1)]))
  assert sum((from_lambda(v)*(Tr**i) for i,v in enumerate(nvcols)),P())==NVh
  assert from_lambda(b)*NV-NVh==L*Nvz
  say("new_H1_full_original_NV_homogenized_without_geometric_inverse",
      TMaxDegree=len(nvcols)-1,completeOriginalIdentityReturned=True,originalBZeroBranchRetained=True)
  for row,label in zip(mat,["mean_R","mean_W","original_N1"]):
   if current.degree()==0:break
   if not row[2] or not nvcols:continue
   proj=quadratic_resultant(row,nvcols,label+" and complete NV")
   if not proj:continue
   current=gcdU(current,proj,"new remaining lambda equation and "+label+" NV")
   projection_stages.append([label+"_NV",proj.degree(),current.degree()])
   say("new_H1_original_NV_lambda_common_constraint",usedOriginal=label,
       remainingLambdaDegree=current.degree(),genericWholeH1CurveExcluded=(current.degree()==0))
 for row in quads:
  for p in row:
   for c0 in p.c:record_denominator(c0.d)
 for p in [a,b,c,current,den]:
  for c0 in p.c:record_denominator(c0.d)
 say("complete_new_H1_whole_quartic_original_parameter_return",
  wholeQWeightAlgebraRank=4,initialOriginalDLambdaDegree=initial_degree,
  remainingLambdaDegree=current.degree(),genericOriginalH1CurveExcluded=(current.degree()==0),
  exactRemainingLambdaEquation=current.data(),actualOriginalProjectionDegrees=projection_stages,
  allBZeroAndLambdaTLeadingZeroFibersRetained=True,temporaryWeightDenominatorCover=pdigest(cover),
  onlySomePowerOfCoverNeededForComposedIdentities=True,entireH1CurveExcluded=False,
  wholePhiFaceExcluded=False,ordinaryISPClaim=False)
 return current.degree()==0
 
closed=False
try:
 closed=bool(run_new_input())
except Nonunit as exc:
 say("accurate_new_H1_whole_weight_nonunit_retained",
     reason=str(exc),noAlgebraComponentDiscarded=True,
     noGenericOrWholeCurveExclusionClaim=True)
sf=monic(exact(cover,cover.gcd(cover.derivative())))
removed=[]
for label,p in [("u",up),("u-1",up-one)]:
 gg=sf.gcd(p)
 if gg.degree()>0:
  old=sf;sf=monic(exact(sf,gg));assert monic(sf*gg)==monic(old)
  removed.append([label,int(gg.degree())])
raw=json.dumps(coefficients(sf),separators=(",",":")).encode()
encoded=base64.b64encode(zlib.compress(raw,9)).decode()
assert zlib.decompress(base64.b64decode(encoded))==raw
chunks=[encoded[i:i+75000] for i in range(0,len(encoded),75000)]
say("new_H1_original_final_weight_cover_status",
    actualGenericOriginalExclusionReturned=closed,
    allWholeQQuarticComponentsRetained=True,
    exactSquarefreeUCover=pdigest(sf),
    onlyPreviouslyPaidScalarWeightUnitsRemoved=removed,
    coversEveryOriginalH1WeightPair=closed,
    upperBoundDifferentWeightPairs=(4*int(sf.degree()) if closed else None),
    wholeH1CurveExcluded=(closed and sf.degree()==0),
    allUnpaidUCoverZeroFibersRemainForOriginalReturn=True,
    ordinaryISPClaim=False)
say("new_H1_original_exact_U_cover_encoding",
    rawBytes=len(raw),rawSHA256=hashlib.sha256(raw).hexdigest(),
    chunks=len(chunks),base64Characters=len(encoded),maximumChunkCharacters=75000)
for i,chunk in enumerate(chunks):
 say("new_H1_original_exact_U_cover_chunk",index=i,total=len(chunks),data=chunk)
say("new_H1_whole_weight_actual_attempt_finished",
    sourceSHA256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
    actualWholeAlgebraInverseProducts=len(inverses),
    actualOriginalPolynomialDivisionProducts=divisions,
    actualOriginalDivisionTraceSHA256=trace.hexdigest(),
    genericOriginalH1ExclusionReturned=closed,
    wholePhiFaceExcluded=False,ordinaryISPClaim=False,
    peakRssKiB=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)
signal.alarm(0)
