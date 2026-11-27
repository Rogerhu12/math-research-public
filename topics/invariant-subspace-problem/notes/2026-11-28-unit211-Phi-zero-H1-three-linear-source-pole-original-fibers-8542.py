#!/usr/bin/env python3
"""NEW original H1 fibers u=3/2,12/5,5/2.
Factor the fixed original Q-quartic exactly and keep every factor.
On each constant Q algebra use only paid original weight units.
Construct all four original quadratics R,W,O,N1, choose an actually
invertible three-by-three (T^2,Tz,z^2) head, and derive the true
three-generator lambda module. The leftover original row and actual
T/z commutators give fixed original lambda cofactors and full Bezout.
If needed add the same full F6 and NV, not a new or weakened source.
No old Dixon chart, b1/A0 inverse, source-cover factor or Gaussian replay.
Every unreturned head/component is retained. 120s /1GiB.
2026-11-28 Asia/Taipei. Only small receipts and parameter definitions.
"""
import time,json,hashlib,signal,resource,itertools
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
zero=pol();one=pol(1);qp=pol([0,1])
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
inverse_count=0;reduction_count=0;inverse_cache={}
class Nonunit(Exception):pass
def red(p):
 global reduction_count
 q,r=divmod(p,phi);assert q*phi+r==p
 reduction_count+=1
 return r
class A:
 """Whole QQ[Q]/phi, with every inverse verified; no irreducibility assumed."""
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
 def inverse(self,label="constant Q algebra inverse"):
  global inverse_count
  if not self:raise Nonunit(label+": zero")
  key=tuple(coeff(self.p))
  if key in inverse_cache:return inverse_cache[key]
  gg,a,b=self.p.xgcd(phi)
  assert a*self.p+b*phi==gg
  if gg.degree()!=0:
   say("accurate_constant_Q_nonunit_retained",label=label,
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

def new_original_component(uvalue,qfactor,index):
 global u,Q,lam,Tr,z,phi,inverse_cache
 phi=monic(qfactor);inverse_cache={}
 u=A(uvalue);Q=A(qp)
 key={"u":str(uvalue),"QFactor":coeff(phi),"QFactorDegree":int(phi.degree()),"factorIndex":index}
 say("new_H1_constant_original_weight_component",**key)
 # Clear numerators of the already-paid original weight units.
 ln=Q-2*(u-1)*(u-2);mn=u*Q-ln
 units=[
  ("original Q",Q),("original rho squared",1-Q),
  ("published whole ell=0 exclusion",ln),
  ("published equal-weight exclusion",mn),
  ("published whole T0=0 exclusion",-Q-4*(u-1)),
  ("original bc nonzero",ln*(2*u-ln)-u*u*Q),
  ("published whole Q=1-u exclusion",Q+u-1),
  ("published whole Phi rho-head-zero exclusion",(ln-Q)*(1-Q)*Q-2*mn*mn)]
 for label,v in units:
  if not v:
   say("new_entire_constant_Q_factor_excluded_by_paid_original_unit",
       **key,originalUnit=label,completeAlgebraElementZeroReturned=True)
   return True
  assert v*v.inverse("paid weight unit "+label)==1
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
 qr=[qrow(p) for p in originals]
 assert all(c.degree()<=0 for row in qr for c in row[3:])
 heads=[[c.c[0] if c.c else A() for c in row[3:]] for row in qr]
 assert det3(heads[:3])==0
 chosen=None
 for subset in itertools.combinations(range(4),3):
  hh=[heads[i] for i in subset];de=det3(hh)
  if de:
   iv=de.inverse("new actual constant quadratic head")
   ad=adj3(hh);hinv=[[c*iv for c in row] for row in ad]
   assert all(sum((hinv[i][k]*hh[k][j] for k in range(3)),A())==(1 if i==j else 0)
              for i in range(3) for j in range(3))
   chosen=(subset,hinv);break
 if chosen is None:
  say("accurate_new_H1_constant_head_rank_at_most_two_retained",**key,
      noDixonPoleInverseUsed=True,originalComponentExcluded=False)
  return False
 subset,hinv=chosen
 rules=[[-sum((hinv[j][i]*qr[subset[i]][k] for i in range(3)),U())
          for k in range(3)] for j in range(3)]
 hmon=[Tr*Tr,Tr*z,z*z]
 for j in range(3):
  assert hmon[j]-vectorP(rules[j])==sum((hinv[j][i]*originals[subset[i]] for i in range(3)),P())
 say("new_constant_H1_three_original_monic_quadratic_rules",**key,
     selectedOriginals=[names[i] for i in subset],
     allThreeFullPolynomialOriginalIdentitiesReturned=True,
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
 say("new_constant_H1_actual_three_column_relations",**key,
     trueTAndZColumnsReturned=6,
     originalRelations=[dict(label=a,lambdaDegrees=[p.degree() for p in b])
                        for a,b in zip(labels,cols)],
     allRelationsVanishAtSameOriginalPoint=True,
     freeLambdaModuleNotAssumed=True)
 current=U();used=[];complete_combo=[]
 def accept_projection(indices):
  nonlocal current,complete_combo
  mat=[[cols[j][i] for j in indices] for i in range(3)]
  pp=det3(mat)
  if not pp:return False
  if not current:
   iv=pp.c[-1].inverse("first original cofactor normalization")
   current=pp*iv;complete_combo=[U(iv)]
  else:
   new,a0,b0=xgcd(current,pp,"new original lambda Bezout")
   complete_combo=[a0*c for c in complete_combo]+[b0]
   current=new
  used.append(pp)
  assert sum((c*p for c,p in zip(complete_combo,used)),U())==current
  say("new_constant_H1_complete_original_cofactor_Bezout",**key,
      sourceColumns=[labels[i] for i in indices],fixedMatrixOrder=3,
      fullPolynomialLambdaDegree=pp.degree(),remainingLambdaDegree=current.degree(),
      completeQQConstantAlgebraBezoutProductReturned=True)
  return current.degree()==0
 done=False
 for inds in itertools.combinations(range(len(cols)),3):
  if accept_projection(inds):done=True;break
 if not done:
  def extra_originals():
   DD=ell*A2-Tr*Tr;B3=4*lam**3-6*lam*lam+3*lam-1
   KK=ell*ell*B3-3*ell*Tr*A2+2*Tr**3
   F6=M*KK*KK-4*m*m*DD**3
   yield F6,"complete_original_F6"
   sn=ell*B3-A2*Tr;zn=Tr*B3-A2*A2
   Znum=u*sn-2*Tr*DD;Snum=sn+(3-2*lam)*DD
   NF4=4*m*((3-4*lam)*Q*DD*DD-J*zn*DD)+2*Snum*(-2*u*Q*KK+J*Znum)
   NC4=(4*m*G*zn*DD-2*G*Snum*Znum-Q*T0*Snum*KK
        +4*m*Q*ww*u*(3-2*lam)*DD*DD
        +2*m*Q*ww*u*sn*DD-2*Q*ww*(u-ell*Q)*KK*DD)
   NV=NF4*ff+NC4+2*bc*Snum*Znum*z
   yield NV,"complete_original_NV"
  for original,label in extra_originals():
   rr=reduceP(original,label)
   for cc,suffix in [(rr,""),(mv(MT,rr),"_T"),(mv(MZ,rr),"_z")]:
    n=len(cols);cols.append(cc);labels.append(label+suffix)
    for i,j in itertools.combinations(range(n),2):
     if accept_projection((i,j,n)):done=True;break
    if done:break
   if done:break
 say("new_H1_constant_original_component_return",**key,
     wholeComponentExcluded=done,
     finalNecessaryLambdaDegree=current.degree(),
     allUnreturnedOriginalValuesRetained=(not done),
     noOldDixonOrBZeroGateReplayed=True)
 return done

all_status=[]
for uvalue in [fmpq(3,2),fmpq(12,5),fmpq(5,2)]:
 gcoeff=[64-272*uvalue+512*uvalue**2-544*uvalue**3+336*uvalue**4-112*uvalue**5+16*uvalue**6,
  -112+348*uvalue-496*uvalue**2+440*uvalue**3-248*uvalue**4+80*uvalue**5-12*uvalue**6,
  60-123*uvalue+104*uvalue**2-52*uvalue**3+13*uvalue**4,
  -13+fmpq(53,4)*uvalue-3*uvalue**2,fmpq(1)]
 gQ=pol(gcoeff);unit,fac=gQ.factor()
 product=pol(unit)
 for p,k in fac:product*=p**int(k)
 assert product==gQ
 status=[]
 for index,(p,mul) in enumerate(fac):
  try:
   excluded=new_original_component(uvalue,p,index)
  except Nonunit as exc:
   say("accurate_new_H1_constant_nonunit_retained",u=str(uvalue),
       QFactor=coeff(monic(p)),reason=str(exc),wholeFactorRetained=True)
   excluded=False
  status.append(dict(QFactor=coeff(monic(p)),multiplicity=int(mul),excluded=excluded))
 all_status.append(dict(u=str(uvalue),wholeOriginalWeightFiberExcluded=all(x["excluded"] for x in status),components=status))
 say("new_H1_constant_weight_all_Q_roots_return",**all_status[-1],
     originalQQuarticFactorProductReturned=True,
     complexQEmbeddingsAndRepeatedRootsAllCovered=True)
say("new_three_linear_H1_original_fiber_input_finished",
 sourceSHA256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
 weights=all_status,allThreeEntireOriginalFibersExcluded=all(x["wholeOriginalWeightFiberExcluded"] for x in all_status),
 actualWholeQAlgebraInverseProducts=inverse_count,
 actualQReductionProducts=reduction_count,actualLambdaDivisionProducts=division_count,
 peakRSSKiB=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss,
 recomputableCoefficientPayloadTransmitted=False,
 encodedOrSplitPayloadCreated=False,wholeH1Excluded=False,ordinaryISPClaim=False)
signal.alarm(0)
