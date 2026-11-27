#!/usr/bin/env python3
"""NEW complete nonlinear H1 source-pole fibres in finite-free integral models.
The six true QQ factors have degrees 3,4,5,7,8,25. The last is regenerated
only from the immutable old construction prefix; no old Gaussian solve.
First split off paid original weight-unit zero components by exact QQ
Q-polynomial gcds over QQ[u]/phi, keeping all conjugate u embeddings.
Then choose a prime only by integrality and whole regular-matrix units
for the original weights, an actual quadratic head, and a FIXED lambda6
cofactor head. Before any common-root test this gives a whole finite-free
integral algebra, with every nilpotent and root component retained.
Complete multiplication matrices of further original cofactors must span
the entire monic-lambda quotient; an actual invertible selected submatrix
and inverse product pay characteristic zero by finite-free lifting.
No generic/modular emptiness shortcut, no added physical localization.
120s /1GiB, 2026-11-28 Asia/Taipei. Small receipts, no data payloads.
"""
import os,time,json,hashlib,signal,resource,itertools
from pathlib import Path
from flint import fmpq,fmpq_poly,nmod_poly,nmod_mat
started=time.perf_counter();deadline=started+120
signal.alarm(120);resource.setrlimit(resource.RLIMIT_AS,(1024**3,1024**3))
def say(stage,**kw):
 kw.update(stage=stage,seconds=time.perf_counter()-started)
 print(json.dumps(kw,separators=(",",":")),flush=True)
def pol(v=()):
 if isinstance(v,fmpq_poly):return v
 if isinstance(v,(int,fmpq)):v=[v]
 return fmpq_poly([fmpq(c) for c in v])
zero=pol();one=pol(1);up=pol([0,1])
def coeff(p):return [str(c) for c in p.coeffs()]
def monic(p):
 assert p
 return p/p[p.degree()]
def pdigest(p):
 raw=json.dumps(coeff(p),separators=(",",":")).encode()
 return dict(degree=int(p.degree()),bytes=len(raw),sha256=hashlib.sha256(raw).hexdigest())
def exact(p,q):
 a,b=divmod(p,q);assert a*q+b==p and not b
 return a
def digest(obj):
 raw=json.dumps(obj,separators=(",",":")).encode()
 return dict(bytes=len(raw),sha256=hashlib.sha256(raw).hexdigest())
inverse_count=0;reduction_count=0;inverse_cache={}
class Nonunit(Exception):pass
def red(p):
 global reduction_count
 q,r=divmod(p,phi);assert q*phi+r==p
 reduction_count+=1
 return r
class A:
 """Whole QQ[u]/phi, with every inverse verified; no irreducibility assumed."""
 def __init__(self,v=0):
  self.p=v.p if isinstance(v,A) else red(pol(v))
 @staticmethod
 def accepts(v):return isinstance(v,(A,fmpq_poly,fmpq,int,tuple,list))
 def __bool__(self):return bool(self.p)
 def __neg__(self):return A(-self.p)
 def __add__(self,v):
  if not self.accepts(v):return NotImplemented
  return A(self.p+A(v).p)
 __radd__=__add__
 def __sub__(self,v):
  if not self.accepts(v):return NotImplemented
  return A(self.p-A(v).p)
 def __rsub__(self,v):
  if not self.accepts(v):return NotImplemented
  return A(v)-self
 def __mul__(self,v):
  if not self.accepts(v):return NotImplemented
  return A(self.p*A(v).p)
 __rmul__=__mul__
 def __eq__(self,v):return self.accepts(v) and self.p==A(v).p
 def inverse(self,label="whole constant u algebra inverse"):
  global inverse_count
  if not self:raise Nonunit(label+": zero")
  key=tuple(coeff(self.p))
  if key in inverse_cache:return inverse_cache[key]
  gg,a,b=self.p.xgcd(phi)
  assert a*self.p+b*phi==gg
  if gg.degree()!=0:
   say("accurate_constant_u_nonunit_retained",label=label,
       exactCommonWeightFactorAscending=coeff(monic(gg)),
       entireWorkingFactorStillRetained=True)
   raise Nonunit(label)
  ans=A(a/gg[0]);assert self*ans==1
  inverse_cache[key]=ans;inverse_count+=1
  return ans
 def __truediv__(self,v):
  if not self.accepts(v):return NotImplemented
  return self*A(v).inverse()
 def __rtruediv__(self,v):
  if not self.accepts(v):return NotImplemented
  return A(v)*self.inverse()
 def __pow__(self,n):
  if n<0:return self.inverse()**(-n)
  ans=A(1);a=self
  while n:
   if n&1:ans=ans*a
   n//=2
   if n:a=a*a
  return ans
 def data(self):return coeff(self.p)
 def complexity(self):
  return max((len(str(c)) for c in self.p.coeffs()),default=0)
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
division_count=0
def divide(p,q,label):
 global division_count
 assert q
 original=U(p);r=U(p)
 cc=[A() for _ in range(max(0,p.degree()-q.degree()+1))]
 iv=q.c[-1].inverse(label+" leading constant Q element")
 while r and r.degree()>=q.degree():
  k=r.degree()-q.degree();co=r.c[-1]*iv
  cc[k]=cc[k]+co
  r=r-U([A()]*k+[co])*q
 out=U(cc);assert out*q+r==original
 division_count+=1
 return out,r
def xgcd(p,q,label):
 oldr,r=U(p),U(q);olds,s=U(1),U();oldt,t=U(),U(1)
 while r:
  quo,rem=divide(oldr,r,label)
  oldr,r=r,rem
  olds,s=s,olds-quo*s
  oldt,t=t,oldt-quo*t
 if not oldr:return oldr,olds,oldt
 iv=oldr.c[-1].inverse(label+" final constant normalization")
 gg=oldr*iv;aa=olds*iv;bb=oldt*iv
 assert aa*p+bb*q==gg and gg.c[-1]==1
 return gg,aa,bb
def det3(a):
 return (a[0][0]*(a[1][1]*a[2][2]-a[1][2]*a[2][1])
        -a[0][1]*(a[1][0]*a[2][2]-a[1][2]*a[2][0])
        +a[0][2]*(a[1][0]*a[2][1]-a[1][1]*a[2][0]))
def adj3(a):
 out=[]
 for i in range(3):
  row=[]
  for j in range(3):
   rr=[k for k in range(3) if k!=j];cc=[k for k in range(3) if k!=i]
   value=a[rr[0]][cc[0]]*a[rr[1]][cc[1]]-a[rr[0]][cc[1]]*a[rr[1]][cc[0]]
   row.append(value if (i+j)%2==0 else -value)
  out.append(row)
 return out
def matmul(a,b):
 return [[sum((a[i][k]*b[k][j] for k in range(3)),U())
          for j in range(3)] for i in range(3)]
def mv(a,v):
 return [sum((a[i][j]*v[j] for j in range(3)),U()) for i in range(3)]
def UtoP(p):
 return P.from_terms({(i,0,0):c for i,c in enumerate(p.c) if c})
def vectorP(v):
 return sum((UtoP(c)*b for c,b in zip(v,[P(1),Tr,z])),P())
def qrow(p):
 out=[]
 for tt,zz in [(0,0),(1,0),(0,1),(2,0),(1,1),(0,2)]:
  dd={ll:c for (ll,t0,z0),c in p.v.items() if t0==tt and z0==zz}
  out.append(U([dd.get(i,A()) for i in range(max(dd,default=-1)+1)]))
 assert vectorP(out[:3])+UtoP(out[3])*Tr*Tr+UtoP(out[4])*Tr*z+UtoP(out[5])*z*z==p
 return out


QQA=A
def weight_quartic(u,Q):
 return (64-272*u+512*u*u-544*u**3+336*u**4-112*u**5+16*u**6
  +(-112+348*u-496*u*u+440*u**3-248*u**4+80*u**5-12*u**6)*Q
  +(60-123*u+104*u*u-52*u**3+13*u**4)*Q**2
  +(-13+fmpq(53,4)*u-3*u*u)*Q**3+Q**4)
def cleared_weight_units(u,Q):
 ln=Q-2*(u-1)*(u-2);mn=u*Q-ln
 return [("original u",u),("original u-1",u-1),
  ("original Q",Q),("original rho squared",1-Q),
  ("published ell zero",ln),("published equal weights",mn),
  ("published T0 zero",-Q-4*(u-1)),
  ("original bc",ln*(2*u-ln)-u*u*Q),
  ("published Q=1-u",Q+u-1),
  ("published Phi rho quadratic head",(ln-Q)*(1-Q)*Q-2*mn*mn)]

def original_QQ_weight_model(modulus):
 global A,phi,inverse_cache
 A=QQA;phi=monic(modulus);inverse_cache={}
 uu=A(up);qq=U([A(),A(1)])
 original=weight_quartic(uu,qq);assert original.degree()==4 and original.c[-1]==1
 good=U(original);removed=U(1);cuts=[]
 for label,v in cleared_weight_units(uu,qq):
  v=U(v)
  while good.degree()>0:
   gg,aa,bb=xgcd(good,v,"new exact QQ weight cut "+label)
   assert aa*good+bb*v==gg
   if gg.degree()==0:break
   quotient,rem=divide(good,gg,"new exact QQ removed weight factor")
   assert not rem and quotient*gg==good
   old=good;good=quotient;removed=removed*gg
   assert good*removed==original
   cuts.append(dict(originalPaidUnit=label,removedQDegree=gg.degree(),
                    beforeQDegree=old.degree(),afterQDegree=good.degree()))
  if good.degree()==0:break
 assert good.c[-1]==1 and good*removed==original
 for label,v in cleared_weight_units(uu,qq):
  if good.degree()==0:break
  gg,aa,bb=xgcd(good,U(v),"new QQ good factor actual coprimality "+label)
  assert gg==1 and aa*good+bb*U(v)==1
 qcoeff=[c.p for c in good.c]
 say("new_nonlinear_H1_complete_QQ_physical_weight_model",
  phi=pdigest(phi),originalMonicQDegree=4,goodMonicQDegree=good.degree(),
  exactPaidUnitCuts=cuts,fullOriginalQFactorProductReturned=True,
  allConjugateUValuesAndQRootsPreservedOutsidePaidUnits=True,
  actualGoodQCoefficientIdentity=digest([coeff(c) for c in qcoeff]),
  goodQCoefficientPayloadTransmitted=False,
  wholePhiWeightFactorExcludedByPaidUnits=(good.degree()==0))
 return qcoeff

PRIMES=(1009,1013,1019,1021,1031)
def modq(q,p):
 cs=[]
 for c in q.coeffs():
  den=int(c.denominator)%p
  if not den:return None
  cs.append(int(c.numerator)%p*pow(den,-1,p)%p)
 return nmod_poly(cs,p)
def nr(p0):
 q,r=divmod(p0,UMOD);assert q*UMOD+r==p0
 return r

class ModA:
 """Whole finite-free Fp[u,Q]/(phi,monic good Q), never assumed a field."""
 def __init__(self,v=0):
  if isinstance(v,ModA):self.c=v.c[:];return
  if isinstance(v,(int,fmpq)):
   v=fmpq(v);den=int(v.denominator)%MODP
   if not den:raise Nonunit("scalar is not p-integral")
   cc=[nmod_poly([int(v.numerator)%MODP*pow(den,-1,MODP)%MODP],MODP)]
  elif isinstance(v,nmod_poly):cc=[v]
  elif isinstance(v,(list,tuple)):
   cc=[]
   for x in v:
    if isinstance(x,nmod_poly):cc.append(x)
    else:
     y=fmpq(x);den=int(y.denominator)%MODP
     if not den:raise Nonunit("coefficient is not p-integral")
     cc.append(nmod_poly([int(y.numerator)%MODP*pow(den,-1,MODP)%MODP],MODP))
  else:raise TypeError(type(v))
  while len(cc)<NQ:cc.append(nmod_poly([],MODP))
  for j in range(len(cc)-1,NQ-1,-1):
   co=nr(cc[j])
   if co:
    for k in range(NQ):cc[j-NQ+k]=cc[j-NQ+k]-co*QMOD[k]
  self.c=[nr(co) for co in cc[:NQ]]
 @staticmethod
 def accepts(v):return isinstance(v,(ModA,nmod_poly,fmpq,int,list,tuple))
 def __bool__(self):return any(self.c)
 def __neg__(self):return ModA([-co for co in self.c])
 def __add__(self,v):
  if not self.accepts(v):return NotImplemented
  v=ModA(v);return ModA([x+y for x,y in zip(self.c,v.c)])
 __radd__=__add__
 def __sub__(self,v):
  if not self.accepts(v):return NotImplemented
  return self+-ModA(v)
 def __rsub__(self,v):
  if not self.accepts(v):return NotImplemented
  return ModA(v)+-self
 def __mul__(self,v):
  if not self.accepts(v):return NotImplemented
  v=ModA(v);cc=[nmod_poly([],MODP) for _ in range(2*NQ-1)]
  for i,x in enumerate(self.c):
   for j,y in enumerate(v.c):
    if x and y:cc[i+j]=cc[i+j]+x*y
  return ModA(cc)
 __rmul__=__mul__
 def __eq__(self,v):return self.accepts(v) and self.c==ModA(v).c
 def flat(self):return [int(c[i]) for c in self.c for i in range(NU)]
 @classmethod
 def fromflat(cls,vals):
  return cls([nmod_poly(vals[j*NU:(j+1)*NU],MODP) for j in range(NQ)])
 def matrix(self):
  cols=[(self*b).flat() for b in ABASIS]
  return nmod_mat([[cols[j][i] for j in range(NBASE)] for i in range(NBASE)],MODP)
 def inverse(self,label="whole finite-free regular unit"):
  global modular_inverse_count
  key=tuple(self.flat())
  if key in MODCACHE:return MODCACHE[key]
  mat=self.matrix()
  if not mat.det():raise Nonunit(label)
  inv=mat.inv()
  assert mat*inv==nmod_mat(NBASE,NBASE,[1 if i==j else 0 for i in range(NBASE) for j in range(NBASE)],MODP)
  answer=ModA.fromflat([int(inv[i,0]) for i in range(NBASE)])
  assert self*answer==1
  MODCACHE[key]=answer;modular_inverse_count+=1
  return answer
 def __truediv__(self,v):
  if not self.accepts(v):return NotImplemented
  return self*ModA(v).inverse()
 def __rtruediv__(self,v):
  if not self.accepts(v):return NotImplemented
  return ModA(v)*self.inverse()
 def __pow__(self,n):
  if n<0:return self.inverse()**(-n)
  out=ModA(1);v=self
  while n:
   if n&1:out=out*v
   n//=2
   if n:v=v*v
  return out
 def data(self):return self.flat()
 def complexity(self):return 0

def setup_modulus(modulus,qcoeff,p):
 global A,MODP,UMOD,QMOD,NU,NQ,NBASE,ABASIS,MODCACHE,modular_inverse_count
 mp=modq(modulus,p);qs=[modq(q,p) for q in qcoeff]
 if mp is None or any(q is None for q in qs):return False
 assert mp.degree()==modulus.degree() and int(mp[mp.degree()])==1
 assert qs[-1]==nmod_poly([1],p)
 MODP=p;UMOD=mp;QMOD=qs[:-1];NU=int(mp.degree());NQ=len(qs)-1;NBASE=NU*NQ
 A=ModA;MODCACHE={};modular_inverse_count=0
 ABASIS=[]
 for j in range(NQ):
  for i in range(NU):
   cc=[nmod_poly([],p) for _ in range(NQ)]
   cc[j]=nmod_poly([0]*i+[1],p);ABASIS.append(A(cc))
 assert ABASIS[0]==1
 return True

def build_modular_original_module(modulus,qcoeff,p):
 global u,Q,lam,Tr,z
 if not setup_modulus(modulus,qcoeff,p):raise Nonunit("nonintegral defining coefficients")
 u=A(nmod_poly([0,1],p));Q=A([0,1])
 key={"uFactorDegree":int(modulus.degree()),"prime":p,"wholeWeightRank":NBASE}
 for label,v in cleared_weight_units(u,Q):
  assert v*v.inverse("integral original weight unit "+label)==1
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

 originals=[Rbar,W4,Obar,N1];names=["R","W","O","N1"]
 # Universally, every original is total degree at most two in (lambda,T,z).
 # Thus the true lower three coefficient degrees are at most (2,1,1),
 # independently of any reduced coefficient cancellations.
 assert all(sum(e)<=2 for ff0 in originals for e in ff0.v)
 qr=[qrow(p) for p in originals]
 assert all(c.degree()<=0 for row in qr for c in row[3:])
 heads=[[c.c[0] if c.c else A() for c in row[3:]] for row in qr]
 assert det3(heads[:3])==0
 chosen=None
 for subset in itertools.combinations(range(4),3):
  hh=[heads[i] for i in subset];de=det3(hh)
  if de:
   try:iv=de.inverse("new actual whole integral quadratic head")
   except Nonunit:continue
   ad=adj3(hh);hinv=[[c*iv for c in row] for row in ad]
   assert all(sum((hinv[i][k]*hh[k][j] for k in range(3)),A())==(1 if i==j else 0)
              for i in range(3) for j in range(3))
   chosen=(subset,hinv);break
 if chosen is None:
  raise Nonunit("no whole integral quadratic head is a unit")
 subset,hinv=chosen
 rules=[[-sum((hinv[j][i]*qr[subset[i]][k] for i in range(3)),U())
          for k in range(3)] for j in range(3)]
 hmon=[Tr*Tr,Tr*z,z*z]
 for j in range(3):
  assert hmon[j]-vectorP(rules[j])==sum((hinv[j][i]*originals[subset[i]] for i in range(3)),P())
 say("new_nonlinear_H1_original_rules_in_whole_integral_reduction",**key,
     selectedOriginals=[names[i] for i in subset],
     universalOriginalRuleIdentitiesReturnedInWholeReduction=True,
     noLambdaValueOrLambdaHeadInverted=True)
 def reduceP(p,label):
  original=P(p);r=P(p);tags=[P() for _ in range(3)]
  while True:
   eligible=[e for e in r.v if e[1]+e[2]>=2]
   if not eligible:break
   ll,tt,zz=max(eligible,key=lambda e:(e[1]+e[2],e[1],e[2],e[0]))
   co=r.v[(ll,tt,zz)]
   if tt>=2:j,at,az=0,2,0
   elif tt and zz:j,at,az=1,1,1
   else:j,at,az=2,0,2
   mult=P.from_terms({(ll,tt-at,zz-az):co})
   r=r-mult*(hmon[j]-vectorP(rules[j]))
   for i in range(3):tags[i]=tags[i]+mult*hinv[j][i]
  assert original-r==sum((tags[i]*originals[subset[i]] for i in range(3)),P())
  row=qrow(r);assert all(not c for c in row[3:])
  return row[:3]
 MT=[[U(),rules[0][i],rules[1][i]] for i in range(3)]
 MZ=[[U(),rules[1][i],rules[2][i]] for i in range(3)]
 MT[1][0]=U(1);MZ[2][0]=U(1)
 for j,basisP in enumerate([P(1),Tr,z]):
  assert reduceP(Tr*basisP,"actual T column")==[MT[i][j] for i in range(3)]
  assert reduceP(z*basisP,"actual z column")==[MZ[i][j] for i in range(3)]
 left=next(i for i in range(4) if i not in subset)
 r0=reduceP(originals[left],"fourth complete original quadratic")
 commA,commB=matmul(MT,MZ),matmul(MZ,MT)
 comm=[[commA[i][j]-commB[i][j] for i in range(3)] for j in range(3)]
 assert not any(comm[0])
 cols=[r0,mv(MT,r0),mv(MZ,r0),comm[1],comm[2]]
 labels=["remaining_"+names[left],"T_times_remaining","z_times_remaining","actual_commutator_T","actual_commutator_z"]
 # Multiplication and commutators come from total-degree-three identities.
 assert all(c.degree()<=b for c,b in zip(cols[0],(2,1,1)))
 assert all(c.degree()<=b for col in cols[1:] for c,b in zip(col,(3,2,2)))
 say("new_nonlinear_H1_same_original_columns_in_whole_reduction",**key,
     trueTAndZColumnsReturned=6,
     originalRelations=[dict(label=a,lambdaDegrees=[p.degree() for p in b])
                        for a,b in zip(labels,cols)],
     allRelationsVanishAtSameOriginalPoint=True,
     freeLambdaModuleNotAssumed=True)

 projections=[];projection_labels=[]
 for i,j in itertools.combinations(range(1,5),2):
  pp=det3([[cols[k][r] for k in (0,i,j)] for r in range(3)])
  assert pp.degree()<=6
  projections.append(pp);projection_labels.append([labels[k] for k in (0,i,j)])
 chosen=None
 for j,pp in enumerate(projections):
  # Six is the uniform exact QQ upper degree from column profiles
  # (2,1,1),(3,2,2),(3,2,2), not a guessed reduced degree.
  if pp.degree()!=6:continue
  try:iv=pp.c[6].inverse("whole original fixed lambda6 cofactor head")
  except Nonunit:continue
  monicF=pp*iv;assert monicF.degree()==6 and monicF.c[-1]==1
  assert monicF*pp.c[6]==pp
  chosen=(j,monicF);break
 if chosen is None:raise Nonunit("no fixed lambda6 head is a whole unit")
 j,monicF=chosen
 return dict(prime=p,weightRank=NBASE,finiteFreeRank=6*NBASE,
  headOriginals=[names[i] for i in subset],projectionIndex=j,
  projectionOriginalColumns=projection_labels[j],monicF=monicF,
  otherProjections=[(lab,pp) for k,(lab,pp) in enumerate(zip(projection_labels,projections)) if k!=j],
  fixedQQDegreeSixPaidByWholeHeadUnit=True,
  primeChosenBeforeAnyCommonRootTest=True)

def lambda_rem(p,F):
 quotient,remainder=divide(p,F,"new monic lambda quotient reduction")
 assert quotient*F+remainder==p and remainder.degree()<6
 return remainder

def complete_original_projection_ideal(model,modulus):
 F=model["monicF"];dim=model["finiteFreeRank"];weight_rank=model["weightRank"]
 selected=[];history=[];reg_cache={}
 def regular(a):
  key=tuple(a.flat())
  if key not in reg_cache:
   mm=a.matrix()
   reg_cache[key]=[[int(mm[i,j]) for j in range(weight_rank)] for i in range(weight_rank)]
  return reg_cache[key]
 for label,H in model["otherProjections"]:
  if not H:continue
  # Block j consists of all original H * lambda^j * weight_basis.
  coefficients=[]
  for j in range(6):
   rr=lambda_rem(H*U([A()]*j+[A(1)]),F)
   coefficients.append([rr.c[i] if i<len(rr.c) else A() for i in range(6)])
  blocks=[[regular(coefficients[j][i]) for j in range(6)] for i in range(6)]
  newcols=[]
  for j in range(6):
   for k in range(weight_rank):
    newcols.append([blocks[i][j][r][k] for i in range(6) for r in range(weight_rank)])
  allcols=selected+newcols
  matrix=nmod_mat([[allcols[j][i] for j in range(len(allcols))] for i in range(dim)],MODP)
  rr,rank=matrix.rref()
  pivots=[]
  for i in range(rank):
   pivot=next(j for j in range(len(allcols)) if int(rr[i,j])!=0)
   assert int(rr[i,pivot])==1
   pivots.append(pivot)
  assert len(set(pivots))==rank
  selected=[allcols[j] for j in pivots]
  history.append(dict(originalColumns=label,rank=int(rank),ambientRank=dim,
                      lambdaCoefficientDegree=H.degree()))
  say("new_nonlinear_H1_original_finite_free_ideal_rank",
      uFactorDegree=int(modulus.degree()),prime=MODP,
      wholeWeightRank=weight_rank,wholeLambdaQuotientRank=dim,
      originalProjectionColumns=label,actualOriginalIdealRank=int(rank),
      allWeightAndLambdaMultiplicitiesRetained=True,
      sourceOnlyCompleteOriginalCofactors=True)
  if rank==dim:
   sq=nmod_mat([[selected[j][i] for j in range(dim)] for i in range(dim)],MODP)
   inv=sq.inv()
   eye=nmod_mat(dim,dim,[1 if i==j else 0 for i in range(dim) for j in range(dim)],MODP)
   assert sq*inv==eye
   say("new_nonlinear_H1_complete_finite_free_original_unit",
       uFactorDegree=int(modulus.degree()),prime=MODP,
       wholeFiniteFreeRank=dim,actualSelectedMatrixInverseProductReturned=True,
       noNormOrIndividualResidueRootLocalization=True,
       integralHeadsChosenBeforeCommonRootTests=True,
       characteristicZeroOriginalWholeWeightFactorExcluded=True,
       matrixIdentity=digest([[int(sq[i,j]) for j in range(dim)] for i in range(dim)]),
       coefficientMatrixPayloadTransmitted=False)
   return True,history
 return False,history

def original_nonlinear_factors():
 factors=[
  pol([fmpq(-15,4),8,-5,1]),
  pol([4,-9,10,-5,1]),
  pol([fmpq(-52,9),20,fmpq(-995,36),fmpq(349,18),fmpq(-83,12),1]),
  pol([-8,fmpq(124,3),fmpq(-187,2),fmpq(709,6),fmpq(-4279,48),fmpq(319,8),fmpq(-39,4),1]),
  pol([fmpq(-864,11),fmpq(4464,11),fmpq(-7408,11),fmpq(6026,11),fmpq(-5255,22),fmpq(426,11),fmpq(291,22),fmpq(-81,11),1])]
 basename="2026-11-28-unit211-Phi-zero-whole-H1-original-biquadratic-Dixon-unit-target-syntax-fix-8542.py"
 base=Path(os.environ.get("ISP_H1_DIXON_SOURCE",str(Path(__file__).with_name(basename))))
 raw=base.read_bytes()
 assert hashlib.sha256(raw).hexdigest()=="ef9e285512e1eddcbac0512f853f0b2ac58b57546f9a4bfa7e5621a9eaf8ddcc"
 marker="# All Gaussian rational parameter poles may cancel."
 text=raw.decode();assert text.count(marker)==1
 prefix=text.split(marker,1)[0]
 assert "def add_column" not in prefix and "success=None" not in prefix
 ns={"__file__":str(base),"__name__":"__h25_original_definition_only__"}
 exec(compile(prefix,str(base)+"::<source-only>","exec"),ns)
 signal.setitimer(signal.ITIMER_REAL,max(0.001,deadline-time.perf_counter()))
 S=ns["source_cover"]
 support=monic(exact(S,S.gcd(S.derivative())))
 for q in [up,up-1]:
  gg=support.gcd(q)
  if gg.degree()>0:support=monic(exact(support,gg))
 assert support.degree()==55
 known=(up-fmpq(3,2))*(up-fmpq(12,5))*(up-fmpq(5,2))
 for q in factors:known*=q
 H25=monic(exact(support,known))
 assert H25*known==support and H25.degree()==25
 assert pdigest(H25)["sha256"]=="98fe71762eb2c2d0fd5a4e5ed09066704be36b65ee2e81ae88aa8a9f7a56b4cc"
 factors.append(H25)
 assert sum(int(f.degree()) for f in factors)==52
 say("new_nonlinear_H1_six_original_factor_definitions",
  factors=[pdigest(f) for f in factors],degreeSum=52,
  H25ObtainedByShortExactDivisionOfSourceSupport=True,
  noOldGaussianTargetOrQQFactorGateReplayed=True,
  coefficientPayloadTransmitted=False)
 return factors

all_results=[]
for modulus in original_nonlinear_factors():
 key=pdigest(modulus)
 try:qcoeff=original_QQ_weight_model(modulus)
 except Nonunit as exc:
  rec=dict(phi=key,excluded=False,reason="exact QQ weight model nonunit: "+str(exc),
           allOriginalComponentsRetained=True)
  all_results.append(rec);say("new_nonlinear_H1_factor_retained",**rec)
  continue
 if len(qcoeff)==1:
  rec=dict(phi=key,excluded=True,reason="whole original Q fibre lies in already paid weight-unit zeros")
  all_results.append(rec);say("new_nonlinear_H1_factor_result",**rec)
  continue
 eligibility=[];model=None
 for p in PRIMES:
  try:
   candidate=build_modular_original_module(modulus,qcoeff,p)
  except Nonunit as exc:
   eligibility.append(dict(prime=p,eligible=False,reason=str(exc),
      criterionOnlyIntegralCoefficientsAndWholeOriginalHeads=True))
   continue
  eligibility.append(dict(prime=p,eligible=True,
    criterionOnlyIntegralCoefficientsAndWholeOriginalHeads=True))
  model=candidate;break
 if model is None:
  rec=dict(phi=key,excluded=False,eligibility=eligibility,
      reason="no integral whole-head model among the fixed eligibility primes",
      allOriginalComponentsRetained=True)
  all_results.append(rec);say("new_nonlinear_H1_factor_retained",**rec)
  continue
 say("new_nonlinear_H1_whole_integral_finite_free_environment",
  phi=key,prime=model["prime"],eligibility=eligibility,
  originalWeightRank=model["weightRank"],fixedMonicLambdaDegree=6,
  entireFiniteFreeRank=model["finiteFreeRank"],
  selectedOriginalQuadraticHead=model["headOriginals"],
  selectedOriginalLambdaCofactor=model["projectionOriginalColumns"],
  fixedQQDegreeSixPaidByWholeOriginalHeadUnit=True,
  allOriginalQQPhysicalComponentsActuallySplitBeforePrimeChoice=True,
  primeChosenBeforeAnyCommonRootOrIdealRank=True)
 passed,history=complete_original_projection_ideal(model,modulus)
 rec=dict(phi=key,excluded=passed,prime=model["prime"],
  wholeIntegralFiniteFreeRank=model["finiteFreeRank"],
  originalIdealRankHistory=history,
  characteristicZeroWholeFactorLiftApplicable=passed,
  allUnreturnedQQWeightComponentsRetained=not passed,
  noPrimeChangedAfterCommonRootTesting=True)
 all_results.append(rec);say("new_nonlinear_H1_factor_result",**rec)
paid=sum(x["phi"]["degree"] for x in all_results if x["excluded"])
assert paid<=52
say("new_nonlinear_H1_integral_original_input_finished",
 sourceSHA256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
 factors=all_results,newPaidWholeUFactorDegree=paid,
 remainingUCoverDegree=253-paid,differentWeightPairUpperBound=4*(253-paid),
 allSixOriginalSourcePoleFactorsExcluded=(paid==52),
 remainingP201CoefficientsNotComputedOrClaimedKnown=True,
 actualQQWeightReductionProducts=reduction_count,
 actualQQAndMonicLambdaDivisionProducts=division_count,
 peakRSSKiB=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss,
 polynomialPayloadTransmitted=False,encodedOrSplitPayloadCreated=False,
 wholeH1Excluded=False,wholePhiFaceExcluded=False,ordinaryISPClaim=False)
signal.alarm(0)
