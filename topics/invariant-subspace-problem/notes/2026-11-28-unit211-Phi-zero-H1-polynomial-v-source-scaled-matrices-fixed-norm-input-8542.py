#!/usr/bin/env python3
"""NEW polynomial original H1 source in v=Jf-G+bc*z, with no head inverse.
All four exact cleared rows multiply back to the original R/W/O/N1;
the scalings use paid original weights only. Three-head ADJUGATE gives
scaled true multiplication columns and fixed polynomial lambda cofactors.
Their necessity holds also where the three-head determinant vanishes.
Add the same full F6/NV, not a generic value surrogate. Primitive removal
uses only actual original units, with complete polynomial products.
Fixed resultant/whole-Q4 norm reductions are new; no Dixon/Gaussian gate,
no cached coefficient payload, and no unproved characteristic-zero lift.
120s/1GiB. 2026-11-28 Asia/Taipei.
"""
import time,json,hashlib,signal,resource,itertools
from pathlib import Path
from flint import fmpq,fmpq_poly,nmod_poly,nmod_mat
started=time.perf_counter();signal.alarm(120)
resource.setrlimit(resource.RLIMIT_AS,(1024**3,1024**3))
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
collect_source_denominators=False
def record_denominator(p):
 global cover
 if not collect_source_denominators:return
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
 original=cc[:];quot=[zero for _ in range(max(0,len(cc)-4))]
 for j in range(len(cc)-1,3,-1):
  lead=cc[j]
  if lead:
   quot[j-4]=quot[j-4]+lead
   for i in range(4):cc[j-4+i]=cc[j-4+i]-lead*g[i]
   cc[j]=zero
 assert not any(cc[4:])
 returned=cc[:]
 for j,co in enumerate(quot):
  for k in range(5):returned[j+k]=returned[j+k]+co*g[k]
 assert returned==original
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


u=A(up);Q=A([0,1])
lam=P.from_terms({(1,0,0):1});Tr=P.from_terms({(0,1,0):1});z=P.from_terms({(0,0,1):1})
def polynomial_identity(p):
 return all(c.d==one for c in P(p).v.values())
def pprofile(p):
 p=P(p)
 raw=json.dumps([(list(e),c.data()) for e,c in sorted(p.v.items())],separators=(",",":")).encode()
 return dict(geometryMonomials=len(p.v),totalGeometryDegree=max((sum(e) for e in p.v),default=-1),
  maximumUCoefficientDegree=max((int(n.degree()) for c in p.v.values() for n in c.n),default=-1),
  bytes=len(raw),sha256=hashlib.sha256(raw).hexdigest())
def exact_polynomial_score(p):
 assert polynomial_identity(p)
 return sum(max(0,int(n.degree())+1) for c in P(p).v.values() for n in c.n)
def primitive_paid(p,label,units):
 original=P(p);p=P(p);factor=A(1);removed=[]
 for name,unit in units:
  iv=unit.inverse("same original paid weight "+name)
  for exponent in range(32):
   candidate=p*iv
   if not polynomial_identity(candidate):break
   if exact_polynomial_score(candidate)>=exact_polynomial_score(p):break
   assert candidate*unit==p
   p=candidate;factor=factor*unit
   if removed and removed[-1]["unit"]==name:removed[-1]["power"]+=1
   else:removed.append(dict(unit=name,power=1))
 assert factor*p==original and polynomial_identity(p)
 say("new_H1_polynomial_same_original_paid_content",label=label,
  removed=removed,primitive=pprofile(p),completePolynomialProductReturned=True,
  noUnpaidCommonFactorRemoved=True,coefficientPayloadTransmitted=False)
 return p
def new_original_polynomials():
 ell=1-2*(u-1)*(u-2)/Q
 delta=1-Q;m=u-ell;V2=2*u-ell*Q;T0=V2-2*u*u
 J=2*u*(1-u)+ell*Q
 P02=(2-3*u)*V2-Q*u+2*u**3;Pf=T0*(J-Q)
 M=ell*V2-u*u;bc=M/(4*delta)
 A2=2*lam*lam-2*lam+1
 G=lam*P02+(u-1)*T0
 Pc=Q*P02*(ell+Tr)-G*T0
 ff=-Pc/Pf
 oldz=(z-J*ff+G)/bc
 assert T0+4*u-4+Q==0
 assert T0==-Q-4*(u-1) and J-Q==-4*(u-1)**2
 assert P02==2*(u-1)*ell*Q
 assert Pf*ff+Pc==0
 aa=1-ell
 vn=J*ff-G+bc*oldz
 wstar=T0+4*u*ff
 nn=Q*wstar-2*vn
 ww=lam-1-Tr
 ii=((vn+aa*u*Q)**2-2*u*Q*vn+2*aa*u*u*Q*Q
     -4*aa*u*Q*Q*ff+bc*oldz*oldz+oldz*(4*bc*u*Q-ell*vn))
 Rbar=ii+(m/(2*delta))*oldz*nn
 W4=(8*bc*delta*Q*Q*ell*T0-4*ell*delta*vn*vn-ell*nn*nn
     +4*m*vn*nn+32*bc*delta*Q*ff*vn+16*bc*bc*delta*oldz*oldz
     +32*bc*bc*delta*Q*(u-1)*oldz-8*bc*ell*delta*oldz*vn+4*bc*m*oldz*nn)
 s0=2*ell*vn-(m/delta)*nn
 d0=-2*m*vn+ell*nn
 Obar=(32*bc*bc*aa*Q*Q*delta*(u-1)+4*bc*Q*delta*s0
       +32*bc*bc*Q*delta*vn-64*bc*bc*Q*Q*delta*ff
       +4*bc*Q*(1-u+2*ff)*d0-s0*d0-8*bc*bc*m*oldz*oldz
       -16*bc*bc*Q*oldz*(m*(u-1)+ell*delta)+8*bc*bc*oldz*nn)
 al=ell*(1-u)-m
 ber=ell*delta-m*(1-u)
 av=(2*u-1)*ell+3*m
 bur=(2*u-1)*m+3*ell*delta
 Nstar=(al*(4*delta*vn*vn+nn*nn)+4*ber*vn*nn
        +8*bc*delta*Q*vn*wstar-24*bc*delta*Q*Q*ff*wstar
        +16*aa*bc*delta*Q*Q*(u-1)*wstar+64*bc*delta*Q*Q*u*ff*ff
        -32*bc*delta*Q*u*ff*vn+16*bc*delta*Q*Q*(1+aa)*T0*ff
        +16*bc*delta*Q*(aa*Q-T0)*vn+4*bc*delta*av*oldz*vn
        -2*bc*bur*oldz*nn+16*bc*bc*delta*Q*oldz*(2*ff+T0-aa*Q)
        -8*u*bc*bc*delta*oldz*oldz)
 N1=Nstar-16*bc*delta*Q*Q*lam*P02*ww

 assert vn==z
 ln=Q-2*(u-1)*(u-2);mn=u*Q-ln;an=Q-ln
 Mn=ln*(2*u-ln)-u*u*Q
 assert ln==Q*ell and mn==Q*m and Mn==Q*M
 FN=G*T0-P02*(ln+Q*Tr)
 VV=z*Pf;WW=T0*Pf+4*u*FN
 NN=Q*WW-2*VV;ZZ=VV-J*FN+G*Pf
 assert FN==Pf*ff and ZZ==Pf*bc*oldz and NN==Pf*nn
 SH=2*ln*delta*VV-mn*NN;DH=-2*mn*VV+ln*NN
 AL=ln*(1-u)-mn;BE=ln*delta-mn*(1-u)
 AV=(2*u-1)*ln+3*mn;BU=(2*u-1)*mn+3*ln*delta
 Rnew=(4*Mn*((VV+an*u*Pf)**2-2*u*Q*VV*Pf
       +2*an*u*u*Q*Pf*Pf-4*an*u*Q*FN*Pf+4*u*Q*ZZ*Pf)
       +16*delta*Q*ZZ*ZZ-16*delta*ln*VV*ZZ+8*mn*ZZ*NN)
 Wnew=(2*Mn*ln*Q*T0*Pf*Pf-4*ln*delta*VV*VV-ln*NN*NN
       +4*mn*VV*NN+8*Mn*Q*FN*VV+16*delta*Q*ZZ*ZZ
       +8*Mn*Q*(u-1)*ZZ*Pf-8*ln*delta*ZZ*VV+4*mn*ZZ*NN)
 Onew=(2*Mn*Mn*an*Q*(u-1)*Pf*Pf+Mn*SH*Q*Pf
       +2*Mn*Mn*Q*VV*Pf-4*Mn*Mn*Q*Q*FN*Pf
       +Mn*DH*Q*((1-u)*Pf+2*FN)-SH*DH-8*mn*delta*Q*ZZ*ZZ
       -4*Mn*Q*ZZ*Pf*(mn*(u-1)+ln*delta)+2*Mn*Q*ZZ*NN)
 Nnew=(AL*(4*delta*VV*VV+NN*NN)+4*BE*VV*NN
       +2*Mn*Q*VV*WW-6*Mn*Q*Q*FN*WW
       +4*an*Mn*Q*(u-1)*WW*Pf+16*Mn*Q*Q*u*FN*FN
       -8*Mn*Q*u*FN*VV+4*Mn*(Q+an)*Q*T0*FN*Pf
       +4*Mn*Q*(an-T0)*VV*Pf+4*delta*AV*ZZ*VV-2*BU*ZZ*NN
       +4*Mn*Q*ZZ*(2*FN+(T0-an)*Pf)-8*u*delta*Q*ZZ*ZZ
       -4*Mn*Q*Q*lam*P02*ww*Pf*Pf)
 originals=[Rbar,W4,Obar,N1]
 cleared=[Rnew,Wnew,Onew,Nnew]
 scales=[4*Mn*Pf*Pf,Q*Pf*Pf,delta*Q*Q*Pf*Pf,Q*Pf*Pf]
 for label,reference,new,scale in zip(["R","W","O","N1"],originals,cleared,scales):
  assert new==scale*reference and polynomial_identity(new)
  assert all(sum(e)<=2 for e in new.v)
  say("new_H1_v_coordinate_complete_original_clearing_identity",original=label,
   actualCleared=pprofile(new),fullOriginalPolynomialProductReturned=True,
   scaleOnlyOriginalPaidUnits=True,allThreeHeadZeroWeightsRetained=True)
 units=[("u",u),("u-1",u-1),("Q",Q),("1-Q",delta),
        ("T0",T0),("J-Q",J-Q),("ell_n",ln),("m_n",mn),("M_n",Mn)]
 cleared=[primitive_paid(p,"original_"+label,units)
          for label,p in zip(["R","W","O","N1"],cleared)]
 DD=ell*A2-Tr*Tr;B3=4*lam**3-6*lam*lam+3*lam-1
 KK=ell*ell*B3-3*ell*Tr*A2+2*Tr**3
 F6=M*KK*KK-4*m*m*DD**3
 sn=ell*B3-A2*Tr;zn=Tr*B3-A2*A2
 Znum=u*sn-2*Tr*DD;Snum=sn+(3-2*lam)*DD
 NF4=4*m*((3-4*lam)*Q*DD*DD-J*zn*DD)+2*Snum*(-2*u*Q*KK+J*Znum)
 NC4=(4*m*G*zn*DD-2*G*Snum*Znum-Q*T0*Snum*KK
      +4*m*Q*ww*u*(3-2*lam)*DD*DD
      +2*m*Q*ww*u*sn*DD-2*Q*ww*(u-ell*Q)*KK*DD)
 NV=NF4*ff+NC4+2*bc*Snum*Znum*oldz
 F6new=Q**5*F6
 NVnew=Q*Q*((NF4-2*J*Snum*Znum)*FN+Pf*NC4+2*Pf*Snum*Znum*(z+G))
 assert NVnew==Q*Q*Pf*NV
 assert polynomial_identity(F6new) and polynomial_identity(NVnew)
 extras=[primitive_paid(F6new,"same_full_F6",units),primitive_paid(NVnew,"same_full_NV",units)]
 say("new_H1_v_coordinate_same_complete_value_polynomials",
  F6=pprofile(extras[0]),NV=pprofile(extras[1]),
  sameOriginalPointAndAllPhysicalDUnitsPreserved=True,
  noNormOrHeadInverted=True)
 return cleared,extras,units

def polynomial_norm(a):
 assert a.d==one
 cols=[a*A([0]*j+[1]) for j in range(4)]
 assert all(c.d==one for c in cols)
 return polynomial_det([[cols[j].n[i] for j in range(4)] for i in range(4)])
def polynomial_det(mat):
 mm=[r[:] for r in mat];n=len(mm);prev=one;sgn=1
 if not n:return one
 for j in range(n-1):
  if not mm[j][j]:
   swap=next((i for i in range(j+1,n) if mm[i][j]),None)
   if swap is None:return zero
   mm[j],mm[swap]=mm[swap],mm[j];sgn=-sgn
  pivot=mm[j][j]
  for i in range(j+1,n):
   for h in range(j+1,n):
    mm[i][h]=exact(mm[i][h]*pivot-mm[i][j]*mm[j][h],prev)
   mm[i][j]=zero
  prev=pivot
 return sgn*mm[-1][-1]
def lambda_scalar(pp):
 assert all(t==v==0 for ll,t,v in pp.v)
 dd={ll:c for (ll,t,v),c in pp.v.items()}
 return U([dd.get(i,A()) for i in range(max(dd,default=-1)+1)])
def primitive_column(column,label,units):
 pp=primitive_paid(vectorP(column),label,units)
 rr=qrow(pp);assert all(not c for c in rr[3:])
 return rr[:3]
def whole_polynomial_module():
 originals,extras,units=new_original_polynomials()
 qr=[qrow(p) for p in originals]
 assert all(c.degree()<=0 for row in qr for c in row[3:])
 heads=[[c.c[0] if c.c else A() for c in row[3:]] for row in qr]
 assert det3(heads[:3])==0
 indices=[0,1,3];hh=[heads[i] for i in indices]
 head=det3(hh);assert head and head.d==one
 adj=adj3(hh)
 assert all(sum((adj[i][k]*hh[k][j] for k in range(3)),A())==(head if i==j else 0)
            for i in range(3) for j in range(3))
 rules=[[-sum((adj[j][i]*qr[indices[i]][k] for i in range(3)),U())
          for k in range(3)] for j in range(3)]
 hmon=[Tr*Tr,Tr*z,z*z]
 for j in range(3):
  assert head*hmon[j]-vectorP(rules[j])==sum((adj[j][i]*originals[indices[i]] for i in range(3)),P())
 MT=[[U(),rules[0][i],rules[1][i]] for i in range(3)]
 MZ=[[U(),rules[1][i],rules[2][i]] for i in range(3)]
 MT[1][0]=U(head);MZ[2][0]=U(head)
 for col,basisP in enumerate([P(1),Tr,z]):
  assert polynomial_identity(vectorP([MT[i][col] for i in range(3)]))
  assert polynomial_identity(vectorP([MZ[i][col] for i in range(3)]))
 other=qr[2]
 r=[head*other[k]+sum((other[j+3]*rules[j][k] for j in range(3)),U()) for k in range(3)]
 assert head*originals[2]-vectorP(r)==sum((UtoP(other[j+3])*(head*hmon[j]-vectorP(rules[j])) for j in range(3)),P())
 CA,CB=matmul(MT,MZ),matmul(MZ,MT)
 comm=[[CA[i][j]-CB[i][j] for i in range(3)] for j in range(3)]
 assert not any(comm[0])
 cols=[r,mv(MT,r),mv(MZ,r),comm[1],comm[2]]
 labels=["scaled_original_O","scaled_T_original_O","scaled_v_original_O",
         "scaled_original_commutator_T","scaled_original_commutator_v"]
 say("new_H1_no_head_inverse_polynomial_module",
  headNorm= pdigest(polynomial_norm(head)),
  weightHeadActuallyInverted=False,
  sixScaledTrueMultiplicationColumnsReturned=True,
  exactSamePoint='vrow*MT=head*T*vrow; vrow*Mv=head*v*vrow',
  completeOriginalAdjugateProductsReturned=True,
  allHeadZeroWeightsRetained=True,
  originalColumns=[dict(label=n,profiles=[p.degree() for p in c]) for n,c in zip(labels,cols)])
 def scaled_value_column(p,label):
  geometry=max(t+v for ll,t,v in p.v)
  cache={(0,0):[U(1),U(),U()]}
  def power_column(t,v):
   if (t,v) not in cache:
    cache[(t,v)]=mv(MT,power_column(t-1,v)) if t else mv(MZ,power_column(0,v-1))
   return cache[(t,v)]
  column=[U(),U(),U()]
  for (ll,t,v),co in p.v.items():
   scale=U([A()]*ll+[co*head**(geometry-t-v)])
   pc=power_column(t,v)
   column=[c+scale*a for c,a in zip(column,pc)]
  assert polynomial_identity(vectorP(column))
  column=primitive_column(column,"same_"+label+"_actual_scaled_column",units)
  say("new_H1_same_value_polynomial_column",original=label,
   uniformHeadPower=geometry,
   necessaryIdentity='vrow*column=head^power*original, up to actually removed paid weights',
   headZeroFibresNotDiscarded=True,
   polynomial=pprofile(vectorP(column)))
  return column
 projections=[];names=[]
 def accept(indices,label):
  ff=det3([[cols[j][i] for j in indices] for i in range(3)])
  ff=lambda_scalar(primitive_paid(UtoP(ff),label,units))
  assert all(c.d==one for c in ff.c)
  if not ff:
   say("accurate_new_H1_cofactor_identically_zero",original=label);return
  projections.append(ff);names.append(label)
  say("new_H1_fixed_QQ_original_polynomial_lambda_cofactor",
   original=label,fixedOrder=3,exactLambdaDegree=ff.degree(),
   polynomial=pprofile(UtoP(ff)),completeQQCoefficientConstruction=True,
   necessaryIncludingThreeHeadZero=True,
   noUnpaidAlgebraElementOrParameterFactorRemoved=True)
 accept((0,1,2),"RWN_O_scaled_T_v")
 accept((0,1,3),"RWN_O_scaled_T_commutator")
 if len(projections)>=2:yield projections[:],names[:]
 for p,label in zip(extras,["complete_F6","complete_NV"]):
  n=len(cols);cols.append(scaled_value_column(p,label));labels.append(label)
  before=len(projections)
  accept((0,1,n),"RWN_O_scaled_T_"+label)
  if len(projections)>before and len(projections)>=2:
   yield [projections[0],projections[-1]],[names[0],names[-1]]

def qq_regular_matrix(a):
 assert a.d==one
 cols=[a*A([0]*j+[1]) for j in range(4)]
 assert all(c.d==one for c in cols)
 return [[cols[j].n[i] for j in range(4)] for i in range(4)]
def fixed_norm_sylvester_degree_certificate(F,H,p):
 m=F.degree();n=H.degree();size=4*(m+n)
 zero_poly=fmpq_poly([])
 blocks=[]
 for ff,shifts in [(F,n),(H,m)]:
  for shift in range(shifts):
   col=[]
   for degree in range(m+n):
    k=degree-shift
    aa=ff.c[k] if 0<=k<=ff.degree() else A()
    col.append(qq_regular_matrix(aa))
   blocks.append(col)
 matrix=[[blocks[j//4][i//4][i%4][j%4] for j in range(size)] for i in range(size)]
 weights=[[int(c.degree()) if c else None for c in row] for row in matrix]
 BIG=10**8
 costs=[[BIG if d is None else -d for d in row] for row in weights]
 upot=[0]*(size+1);vpot=[0]*(size+1);matching=[0]*(size+1);way=[0]*(size+1)
 for i in range(1,size+1):
  matching[0]=i;j0=0;dist=[BIG*size]*(size+1);seen=[False]*(size+1)
  while True:
   seen[j0]=True;i0=matching[j0];best=BIG*size;j1=0
   for j in range(1,size+1):
    if not seen[j]:
     cur=costs[i0-1][j-1]-upot[i0]-vpot[j]
     if cur<dist[j]:dist[j]=cur;way[j]=j0
     if dist[j]<best:best=dist[j];j1=j
   for j in range(size+1):
    if seen[j]:upot[matching[j]]+=best;vpot[j]-=best
    else:dist[j]-=best
   j0=j1
   if matching[j0]==0:break
  while True:
   j1=way[j0];matching[j0]=matching[j1];j0=j1
   if j0==0:break
 assignment=[0]*size
 for j in range(1,size+1):assignment[matching[j]-1]=j-1
 if any(weights[i][assignment[i]] is None for i in range(size)):
  return dict(normSylvesterOrder=size,structuralZero=True,upperDegree=-1)
 row_dual=[-upot[i] for i in range(1,size+1)]
 col_dual=[-vpot[j] for j in range(1,size+1)]
 bound=sum(row_dual)+sum(col_dual)
 assert bound==sum(weights[i][assignment[i]] for i in range(size))
 assert all(d is None or row_dual[i]+col_dual[j]>=d
            for i,row in enumerate(weights) for j,d in enumerate(row))
 leading=[]
 for i,row in enumerate(matrix):
  rr=[]
  for j,a in enumerate(row):
   if not a or a.degree()!=row_dual[i]+col_dual[j]:rr.append(0);continue
   c=a[a.degree()];den=int(c.denominator)%p
   assert den
   rr.append(int(c.numerator)%p*pow(den,-1,p)%p)
  leading.append(rr)
 ld=int(nmod_mat(leading,p).det())
 return dict(normSylvesterOrder=size,fixedLambdaDegrees=[m,n],upperDegree=bound,
  completeMaximumAssignmentAndDualReturned=True,
  rowDual=row_dual,columnDual=col_dual,leadingDualDeterminantModuloPrime=ld,
  characteristicZeroDegreeAndModularLeadingKept=(ld!=0),
  structuralZero=False)

def modular_fixed_original_returns(projections,names):
 p=1009
 def mp(v=()):
  if isinstance(v,nmod_poly):return v
  if isinstance(v,fmpq_poly):v=v.coeffs()
  if isinstance(v,(int,fmpq)):v=[v]
  out=[]
  for co in v:
   c=fmpq(co);den=int(c.denominator)%p
   if not den:raise Nonunit("new exact QQ input coefficient is not 1009-integral")
   out.append(int(c.numerator)%p*pow(den,-1,p)%p)
  return nmod_poly(out,p)
 mz=mp();mo=mp(1);mg=[mp(c) for c in g]
 def mexact(a,b):
  q,r=divmod(a,b);assert q*b+r==a and not r
  return q
 def mreduce(cc):
  cc=list(cc)
  while len(cc)<4:cc.append(mz)
  original=cc[:];quot=[mz for _ in range(max(0,len(cc)-4))]
  for j in range(len(cc)-1,3,-1):
   co=cc[j];quot[j-4]=quot[j-4]+co
   for k in range(4):cc[j-4+k]=cc[j-4+k]-co*mg[k]
   cc[j]=mz
  returned=cc[:]
  for j,co in enumerate(quot):
   for k in range(5):returned[j+k]=returned[j+k]+co*mg[k]
  assert returned==original
  return cc[:4]
 def mdet(mat):
  aa=[row[:] for row in mat];n=len(aa);prev=mo;sign=1
  if not n:return mo
  for j in range(n-1):
   if not aa[j][j]:
    sw=next((i for i in range(j+1,n) if aa[i][j]),None)
    if sw is None:return mz
    aa[j],aa[sw]=aa[sw],aa[j];sign=-sign
   pivot=aa[j][j]
   for i in range(j+1,n):
    for k in range(j+1,n):
     aa[i][k]=mexact(aa[i][k]*pivot-aa[i][j]*aa[j][k],prev)
    aa[i][j]=mz
   prev=pivot
  return sign*aa[-1][-1]
 cache={}
 class MA:
  def __init__(self,v=0,d=None):
   if isinstance(v,MA) and d is None:self.n=v.n[:];self.d=v.d;return
   nn=mreduce([mp(co) for co in v] if isinstance(v,(tuple,list)) else [mp(v)])
   dd=mo if d is None else mp(d);assert dd
   gg=dd
   for co in nn:gg=gg.gcd(co)
   dd=mexact(dd,gg);nn=[mexact(co,gg) for co in nn]
   inv=pow(int(dd[dd.degree()]),-1,p)
   self.n=[co*inv for co in nn];self.d=dd*inv
  def __bool__(self):return any(self.n)
  def __neg__(self):return MA([-co for co in self.n],self.d)
  def __add__(self,v):
   v=MA(v);gg=self.d.gcd(v.d);l=mexact(v.d,gg);r=mexact(self.d,gg)
   return MA([a*l+b*r for a,b in zip(self.n,v.n)],self.d*l)
  __radd__=__add__
  def __sub__(self,v):return self+-MA(v)
  def __rsub__(self,v):return MA(v)+-self
  def __mul__(self,v):
   v=MA(v);cc=[mz for _ in range(7)]
   for i,a in enumerate(self.n):
    for j,b in enumerate(v.n):
     if a and b:cc[i+j]=cc[i+j]+a*b
   return MA(cc,self.d*v.d)
  __rmul__=__mul__
  def __eq__(self,v):
   v=MA(v);return self.n==v.n and self.d==v.d
  def regular_numerator(self):
   cols=[mreduce([mz]*j+self.n[:]) for j in range(4)]
   return [[cols[j][i] for j in range(4)] for i in range(4)]
  def inverse(self):
   key=tuple(tuple(int(c) for c in n.coeffs()) for n in self.n)+(tuple(int(c) for c in self.d.coeffs()),)
   if key in cache:return cache[key]
   mat=self.regular_numerator();de=mdet(mat)
   if not de:raise Nonunit("actual whole Q4 Euclidean pivot is a nonunit")
   nums=[]
   for j in range(4):
    co=mdet([[mat[r][c] for c in range(4) if c!=j] for r in range(1,4)])
    nums.append(((-1)**j)*co*self.d)
   out=MA(nums,de);assert self*out==1
   cache[key]=out;return out
  def __pow__(self,n):
   assert n>=0
   out=MA(1);a=self
   while n:
    if n&1:out=out*a
    n//=2
    if n:a=a*a
   return out
 class MU:
  def __init__(self,v=0):
   if isinstance(v,MU):self.c=v.c[:];return
   self.c=[MA(c) for c in v] if isinstance(v,(list,tuple)) else [MA(v)]
   while self.c and not self.c[-1]:self.c.pop()
  def __bool__(self):return bool(self.c)
  def __neg__(self):return MU([-c for c in self.c])
  def __add__(self,v):
   v=MU(v);n=max(len(self.c),len(v.c))
   return MU([(self.c[i] if i<len(self.c) else MA())+(v.c[i] if i<len(v.c) else MA()) for i in range(n)])
  __radd__=__add__
  def __sub__(self,v):return self+-MU(v)
  def __rsub__(self,v):return MU(v)+-self
  def __mul__(self,v):
   v=MU(v)
   if not self or not v:return MU()
   cc=[MA() for _ in range(len(self.c)+len(v.c)-1)]
   for i,a in enumerate(self.c):
    for j,b in enumerate(v.c):
     if a and b:cc[i+j]=cc[i+j]+a*b
   return MU(cc)
  __rmul__=__mul__
  def __eq__(self,v):
   v=MU(v);return self.c==v.c
  def degree(self):return len(self.c)-1
 def mdivide(f,h):
  assert h
  rem=MU(f);cc=[MA() for _ in range(max(0,f.degree()-h.degree()+1))]
  iv=h.c[-1].inverse()
  while rem and rem.degree()>=h.degree():
   j=rem.degree()-h.degree();co=rem.c[-1]*iv
   cc[j]=cc[j]+co;rem=rem-MU([MA()]*j+[co])*h
  out=MU(cc);assert out*h+rem==f
  return out,rem
 def fixed_resultant(f,h,label):
  a,b=MU(f),MU(h);factor=MA(1);steps=[]
  while True:
   m=a.degree();n=b.degree()
   if not a or not b:return MA(),steps
   if n==0:return factor*b.c[0]**m,steps
   if m<n:
    if m*n%2:factor=-factor
    a,b=b,a;continue
   quotient,r=mdivide(a,b)
   steps.append(dict(firstDegree=m,secondDegree=n,remainderDegree=r.degree()))
   if not r:return MA(),steps
   factor=factor*((-1)**(m*n))*b.c[-1]**(m-r.degree())
   a,b=b,r
   say("new_H1_fixed_original_lambda_resultant_modular_step",
    label=label,originalEuclideanDegrees=[m,n],actualRemainderDegree=r.degree(),
    completeDivisionProductReturned=True,temporaryPivotsNotUsedAsGeometricUnits=True)
 converted=[]
 for ff in projections:
  assert all(c.d==one for c in ff.c)
  mm=MU([MA([mp(c) for c in a.n]) for a in ff.c])
  assert mm.degree()==ff.degree()
  converted.append(mm)
 common=None;returns=[]
 for j in range(1,len(converted)):
  label=names[j];bound=fixed_norm_sylvester_degree_certificate(projections[0],projections[j],p)
  say("new_H1_fixed_QQ_norm_sylvester_degree_bound",label=label,**bound)
  res,steps=fixed_resultant(converted[0],converted[j],label)
  assert res.d==mo
  nn=mdet(res.regular_numerator())
  raw=json.dumps([int(c) for c in nn.coeffs()],separators=(",",":")).encode()
  identity=dict(degree=int(nn.degree()),bytes=len(raw),sha256=hashlib.sha256(raw).hexdigest())
  if bound["structuralZero"]:assert not nn
  else:
   assert nn.degree()<=bound["upperDegree"]
   if bound["characteristicZeroDegreeAndModularLeadingKept"]:assert nn.degree()==bound["upperDegree"]
  if nn:
   nn=nn*pow(int(nn[nn.degree()]),-1,p)
   common=nn if common is None else common.gcd(nn)
  rec=dict(label=label,fixedQQNormSylvesterOrder=bound["normSylvesterOrder"],
   symbolicLambdaDegrees=[projections[0].degree(),projections[j].degree()],
   prime=p,actualModularNormPolynomial=identity,
   trueQQUpperDegree=bound["upperDegree"],
   QQDegreeActuallyPaidByUncanceledLeading=(bound.get("characteristicZeroDegreeAndModularLeadingKept",False)),
   originalQQuotientNormIsPolynomial=True,allEuclideanDivisionsActuallyMultipliedBack=True,
   noQQFactorOrP201ExclusionFromModularResult=True,
   currentActualModularCommonDegree=(common.degree() if common is not None else None))
  returns.append(rec);say("new_H1_fixed_original_polynomial_norm_return",**rec)
 return returns,common


all_projections=[];all_names=[];all_modular_returns=[];common=None
for projections,names in whole_polynomial_module():
 for ff,label in zip(projections,names):
  if label not in all_names:all_projections.append(ff);all_names.append(label)
 try:
  modular_returns,nn=modular_fixed_original_returns(projections,names)
  all_modular_returns.extend(modular_returns)
  if nn is not None:common=nn if common is None else common.gcd(nn)
  say("new_H1_original_norms_actual_common_checkpoint",
   completedNecessaryInputs=len(all_modular_returns),
   actualCommonModularDegree=(int(common.degree()) if common is not None else None),
   noCharacteristicZeroFactorOrExclusionClaim=True)
 except Nonunit as exc:
  say("accurate_new_H1_modular_structural_nonunit",
   reason=str(exc),allOriginalWeightFibresRetained=True,noNewQQExclusion=True)
if common is not None:
 unit,factors=common.factor();product=nmod_poly([int(unit)],1009);info=[]
 for ff,e in factors:
  product=product*ff**e
  rb=json.dumps([int(c) for c in ff.coeffs()],separators=(",",":")).encode()
  info.append(dict(degree=int(ff.degree()),multiplicity=int(e),
                   bytes=len(rb),sha256=hashlib.sha256(rb).hexdigest()))
 assert product==common
 say("new_H1_exact_modular_common_factor_profile",
  prime=1009,degree=int(common.degree()),factors=info,
  completeModularFactorProductReturned=True,
  noCharacteristicZeroFactorClaim=True,noQQP201ReductionClaim=True,
  coefficientPayloadTransmitted=False)
say("new_H1_polynomial_original_fixed_input_finished",
 sourceSHA256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
 exactQQOriginalCofactors=[dict(label=label,lambdaDegree=f.degree(),definition=pprofile(UtoP(f))) for label,f in zip(all_names,all_projections)],
 modularReturns=all_modular_returns,oldDixonGaussianReplayed=False,
 oldC256OrC55SupportGateReplayed=False,
 coefficientPayloadTransmitted=False,encodedOrSplitPayloadCreated=False,
 P201CoefficientsKnown=False,wholeH1Excluded=False,ordinaryISPClaim=False,
 peakRSSKiB=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)
signal.alarm(0)
