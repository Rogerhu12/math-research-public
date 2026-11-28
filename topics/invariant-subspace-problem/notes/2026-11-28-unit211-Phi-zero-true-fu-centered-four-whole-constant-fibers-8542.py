#!/usr/bin/env python3
"""NEW correct Phi f=u: the four remaining complete QQ weight fibers.
Use the original centered v=t-2 monic quadratic and the monic Q-cubic.
Rebuild only raw N1,NS,PS in each whole finite constant algebra.
No old eighteen-column, C17, cofactor, GB, or residue-prime gate.
All Q components/nilpotents and all embeddings of each original factor
are retained, except components removed by actual paid-unit gcd identities.
Only actual 1 or a positive power of lambda*t*Dval in the original ideal
closes a factor.  120 seconds / 1 GiB, small checkpoint output only.
"""
import gc,hashlib,json,resource,signal,time
from flint import fmpq,fmpq_poly,fmpq_mat
START=time.perf_counter();DEADLINE=START+120
resource.setrlimit(resource.RLIMIT_AS,(1024**3,1024**3))
signal.alarm(120)
def tick():
 if time.perf_counter()>=DEADLINE:raise TimeoutError('absolute 120 second boundary')
def say(stage,**kw):
 kw.update(stage=stage,seconds=time.perf_counter()-START)
 print(json.dumps(kw,sort_keys=True),flush=True)
class NonUnit(Exception):pass
FACTORS=[
 ('linear_half',[-1,2]),
 ('quadratic',[1,-4,2]),
 ('cubic',[-7,12,-8,2]),
 ('degree_nine',[-763,3296,-6650,8828,-8886,6870,-3848,1440,-320,32])
]
def run_case(name,coeff):
 tick();phi=fmpq_poly(coeff);phi=phi/phi[int(phi.degree())];d=int(phi.degree())
 stats={'constantReductions':0,'constantInverses':0,'QDivisionReturns':0,
        'QBezoutReturns':0,'weightProductReturns':0,'weightInverses':0,
        'vProductReturns':0,'originalValueRows':0,'QQInverseCoordinates':0,
        'allOriginalColumnCoordinates':0,'targetCoordinates':0}
 class K:
  def __init__(self,p=0):
   if isinstance(p,K):self.p=p.p;return
   p=p if isinstance(p,fmpq_poly) else fmpq_poly([p])
   q,r=divmod(p,phi);assert q*phi+r==p
   self.p=r;stats['constantReductions']+=1
  def __bool__(self):return bool(self.p)
  def __add__(self,z):return K(self.p+K(z).p)
  __radd__=__add__
  def __neg__(self):return K(-self.p)
  def __sub__(self,z):return self+-K(z)
  def __rsub__(self,z):return K(z)+-self
  def __mul__(self,z):return K(self.p*K(z).p)
  __rmul__=__mul__
  def __pow__(self,n):
   assert isinstance(n,int) and n>=0
   out=K(1);a=self
   while n:
    if n&1:out=out*a
    n//=2
    if n:a=a*a
   return out
  def inv(self):
   if not self:raise NonUnit('zero original constant algebra element')
   g,a,b=self.p.xgcd(phi);assert a*self.p+b*phi==g
   if int(g.degree())!=0:raise NonUnit('constant algebra nonunit')
   out=K(a/g[0]);assert out*self==K(1)
   stats['constantInverses']+=1;return out
  def __truediv__(self,z):return self*K(z).inv()
  def __eq__(self,z):return self.p==K(z).p
 K0=K();K1=K(1);ku=K(fmpq_poly([0,1]))
 def tr(a):
  a=list(a)
  while a and not a[-1]:a.pop()
  return a
 def pa(a,b):return tr([(a[i] if i<len(a) else K0)+(b[i] if i<len(b) else K0) for i in range(max(len(a),len(b)))])
 def pn(a):return [-c for c in a]
 def ps(a,b):return pa(a,pn(b))
 def pm(a,b):
  if not a or not b:return []
  out=[K0]*(len(a)+len(b)-1)
  for i,x in enumerate(a):
   for j,y in enumerate(b):out[i+j]=out[i+j]+x*y
  return tr(out)
 def pc(a,c):return tr([x*c for x in a])
 def pp(a,n):
  out=[K1]
  for _ in range(n):out=pm(out,a)
  return out
 def pd(a,b):
  """Return (quotient,remainder), with the complete original product."""
  tick();a=tr(a);b=tr(b);assert b
  rem=list(a);quo=[K0]*max(0,len(a)-len(b)+1);inv=b[-1].inv()
  while rem and len(rem)>=len(b):
   j=len(rem)-len(b);c=rem[-1]*inv;quo[j]=quo[j]+c
   for i,x in enumerate(b):rem[i+j]=rem[i+j]-c*x
   rem=tr(rem)
  quo=tr(quo);assert not ps(a,pa(pm(quo,b),rem))
  stats['QDivisionReturns']+=1;return quo,rem
 def pxgcd(a,b):
  aa=tr(a);bb=tr(b);r0,r1=aa,bb;s0,s1=[K1],[];t0,t1=[],[K1]
  while r1:
   q,r=pd(r0,r1)
   r0,r1=r1,r;s0,s1=s1,ps(s0,pm(q,s1));t0,t1=t1,ps(t0,pm(q,t1))
  if not r0:return [],[],[]
  inv=r0[-1].inv();g=pc(r0,inv);ss=pc(s0,inv);tt=pc(t0,inv)
  assert not ps(g,pa(pm(ss,aa),pm(tt,bb)))
  stats['QBezoutReturns']+=1;return g,ss,tt
 C=lambda x:tr([K(x)])
 Qp=[K0,K1];one=[K1];deltaP=ps(one,Qp)
 s=ku-1;hh=2*ku-3
 Lp=ps(Qp,C(2*s*(ku-2)));Kp=pa(Qp,C(4*s))
 Mnp=ps(ps(pc(Lp,2*ku),pm(Lp,Lp)),pc(Qp,ku*ku))
 thetap=ps(C(ku),Lp)
 Hfp=ps(ps(pm(Qp,Qp),pc(Qp,4*ku*ku-11*ku+8)),C(4*s*(ku-2)**2))
 psi=[-32*ku**6+224*ku**5-672*ku**4+1104*ku**3-1040*ku**2+528*ku-112,
      32*ku**4-152*ku**3+276*ku**2-228*ku+72,
      -10*ku*ku+24*ku-15,K1]
 assert len(psi)==4 and psi[-1]==K1
 for title,val in [('u',ku),('u-1',s),('2u-3',hh)]:
  iv=val.inv();assert val*iv==K1
 units=[('Q',Qp),('delta',deltaP),('L',Lp),('K',Kp),('Mn',Mnp),
        ('theta',thetap),('Hf',Hfp)]
 good=list(psi);removed=[K1];removed_records=[]
 for title,p in units:
  while len(good)>1:
   g,a,b=pxgcd(good,p)
   if len(g)==1:break
   ng,rr=pd(good,g);assert not rr
   quotient,rr=pd(p,g);assert not rr
   assert not ps(pm(quotient,g),p)
   good=ng;removed=pm(removed,g)
   assert not ps(pm(good,removed),psi)
   removed_records.append({'paidUnit':title,'removedQDegree':len(g)-1})
  if len(good)==1:break
 assert not ps(pm(good,removed),psi)
 say('new_fu_original_constant_Q_components',factor=name,
     originalFactorDegree=d,originalFactorCoefficients=coeff,
     originalMonicQDegree=3,retainedQDegree=len(good)-1,
     paidRemovedComponents=removed_records,
     completeQQProductAndPaidGCDIdentitiesReturned=True,
     allOtherQComponentsAndNilpotentsKept=True,
     noOldC17OrEighteenColumnGate=True)
 if len(good)==1:
  say('new_fu_whole_factor_complete',factor=name,wholeFactorExcluded=True,
      reason='every Q component removed by complete original paid-unit identities',
      statistics=stats)
  return True
 nq=len(good)-1
 class A:
  def __init__(self,p=0):
   if isinstance(p,A):self.p=p.p;return
   if isinstance(p,list):a=p
   else:a=[K(p)]
   self.p=pd(a,good)[1] if a else []
  def __bool__(self):return bool(self.p)
  def __add__(self,z):return A(pa(self.p,A(z).p))
  __radd__=__add__
  def __neg__(self):return A(pn(self.p))
  def __sub__(self,z):return self+-A(z)
  def __rsub__(self,z):return A(z)+-self
  def __mul__(self,z):
   z=A(z);raw=pm(self.p,z.p);q,r=pd(raw,good)
   assert not ps(raw,pa(pm(q,good),r))
   stats['weightProductReturns']+=1;return A(r)
  __rmul__=__mul__
  def __pow__(self,n):
   assert isinstance(n,int) and n>=0
   out=A(1);a=self
   while n:
    if n&1:out=out*a
    n//=2
    if n:a=a*a
   return out
  def inv(self):
   g,a,b=pxgcd(self.p,good)
   if len(g)!=1:raise NonUnit('whole retained Q-algebra nonunit')
   out=A(pc(a,g[0].inv()));assert self*out==A(1)
   stats['weightInverses']+=1;return out
  def __eq__(self,z):return not ps(self.p,A(z).p)
 A0=A();A1=A(1)
 au=A(ku);aQ=A(Qp);ad=A(deltaP);aL=A(Lp);aK=A(Kp)
 aMn=A(Mnp);atheta=A(thetap);aHf=A(Hfp);ass=A(s);ah=A(hh)
 invs={}
 for title,p in units:
  val=A(p);iv=val.inv();assert val*iv==A1;invs[title]=iv
 IQ,ID,IL,ITH,IH=(invs[k] for k in ['Q','delta','L','theta','Hf'])
 ell=aL*IQ;aw=A1-ell;mm=au-ell;bc=aMn*IQ*ID*A(fmpq(1,4))
 qv=-4*aQ*atheta*ah*IH
 class J:
  def __init__(self,a=0,b=0):
   if isinstance(a,J):assert not b;self.a=a.a;self.b=a.b;return
   self.a=A(a);self.b=A(b)
  def __bool__(self):return bool(self.a) or bool(self.b)
  def __add__(self,z):z=J(z);return J(self.a+z.a,self.b+z.b)
  __radd__=__add__
  def __neg__(self):return J(-self.a,-self.b)
  def __sub__(self,z):return self+-J(z)
  def __rsub__(self,z):return J(z)+-self
  def __mul__(self,z):
   z=J(z);c0=self.a*z.a;c1=self.a*z.b+self.b*z.a;c2=self.b*z.b
   out=J(c0+c2*qv,c1)
   assert out.a-c2*qv==c0 and out.b==c1
   stats['vProductReturns']+=1;return out
  __rmul__=__mul__
  def __pow__(self,n):
   assert isinstance(n,int) and n>=0
   out=J(1);a=self
   while n:
    if n&1:out=out*a
    n//=2
    if n:a=a*a
   return out
  def __eq__(self,z):z=J(z);return self.a==z.a and self.b==z.b
 vv=J(0,1);tt=vv+2
 x=J(au)+tt*J(A(fmpq(1,4)))
 y0=J(A(fmpq(1,2)))-vv*J(au*ITH*A(fmpq(1,4)))
 AA=4*ass*ass-aQ
 Yf=(J(aMn*ah*ID*A(fmpq(1,2)))*tt-J(aL*AA))*J(ITH*A(fmpq(1,2)))
 lam=(Yf-J(AA))*J(IL*A(fmpq(1,2)))
 Tr=-J(ell)-Yf*J(aK*IQ*IL*A(fmpq(1,2)))
 gramA1=Yf*J(2*ass*IQ);ww=lam-1-Tr
 P02=J(2*ass*aL)
 def E(a=0,b=0):return [J(a),J(b)]
 def ea(a,b):return [a[0]+b[0],a[1]+b[1]]
 def en(a):return [-a[0],-a[1]]
 def es(a,b):return ea(a,en(b))
 def em(a,b):return [a[0]*b[0]+J(ad)*a[1]*b[1],a[0]*b[1]+a[1]*b[0]]
 def ec(a,n):return [a[0]*J(n),a[1]*J(n)]
 def conj(a):return [a[0],-a[1]]
 def esum(*xs):
  out=E()
  for z in xs:out=ea(out,z)
  return out
 bw=E(ell*A(fmpq(1,2)),mm*ID*A(fmpq(1,2)));cw=conj(bw)
 p=E(1,1);q=conj(p);X=E(x,y0);Y=conj(X)
 rr=es(es(X,ec(p,aw)),ec(cw,tt));ss=conj(rr)
 rows=[[E(),E(),p,q],[E(),E(gramA1),rr,ss],
       [p,rr,E(),E(tt)],[q,ss,E(tt),E()]]
 unit=[E(1),E(),E(1),E(1)]
 def vm(v,z):
  return [em(v[0],z[0]),ea(em(v[0],z[1]),em(v[1],z[0])),
          em(v[2],z[2]),em(v[3],z[3])]
 def va(v,z):return [ea(a,b) for a,b in zip(v,z)]
 def vs(a,v):return [em(a,z) for z in v]
 def tau(v):return esum(ec(v[0],aw),v[1],em(bw,v[2]),em(cw,v[3]))
 def DK(v):return [tau(vm(row,v)) for row in rows]
 dv=DK(unit);F2=tau(dv)
 def pure(v):
  assert not v[1]
  return v[0]
 assert pure(F2)==J(2*au)
 def N4(v):
  tv=tau(v);v2=vm(v,v)
  return esum(ec(tau(vm(dv,v2)),2),en(em(F2,tau(v2))),
   ec(em(tv,tau(vm(dv,v))),-4),ec(em(F2,em(tv,tv)),2),tau(vm(v,DK(v))))
 def centered(v):return va(v,vs(en(tau(v)),unit))
 def P2(v):
  cv=centered(v);return tau(vm(vm(cv,cv),cv))
 N0=N4(rows[0]);assert pure(N0)==2*lam*P02
 Nj=es(es(N4(va(rows[0],rows[1])),N0),N4(rows[1]))
 N1=pure(Nj)-4*lam*ww*P02
 Al=2*lam*lam-2*lam+1;Bl=4*lam**3-6*lam*lam+3*lam-1
 NS=pure(esum(em(bw,N4(rows[2])),em(cw,N4(rows[3]))))-2*lam*P02*(J(ell)+2*Tr+Al)
 PS=pure(esum(em(bw,P2(rows[2])),em(cw,P2(rows[3]))))-P02*(J(ell)+3*Tr+3*Al+Bl)
 necessary=[N1,NS,PS];stats['originalValueRows']=3
 DIM=2*nq*d
 def flat(z):
  z=J(z);out=[]
  for part in [z.a,z.b]:
   for k in range(nq):
    c=part.p[k] if k<len(part.p) else K0
    out.extend([c.p[j] for j in range(d)])
  assert len(out)==DIM;return out
 basis=[]
 for vpower in range(2):
  for k in range(nq):
   for j in range(d):
    z=A([K0]*k+[K(fmpq_poly([0]*j+[1]))])
    basis.append(J(z) if vpower==0 else J(0,z))
 for j,z in enumerate(basis):
  assert flat(z)==[fmpq(int(i==j)) for i in range(DIM)]
 say('new_fu_centered_complete_original_values',factor=name,
     weightQQDimension=nq*d,fullQQAlgebraDimension=DIM,
     originalRows=['N1','NS','PS'],allThreeRawOriginalRowsReturned=True,
     originalN0AndF2NormalizationsReturned=True,
     centerVMonicDegree=2,QMonicDegree=nq,
     allConstantEmbeddingsAndQAndVNilpotentsKept=True,
     noOriginalEighteenColumnOrC17Reconstruction=True,
     namedPaidWeightUnitsReturned=[title for title,_ in units])
 columns=[];tags=[]
 for i,row in enumerate(necessary):
  for j,z in enumerate(basis):
   columns.append(flat(row*z));tags.append([i,j])
 MAT=fmpq_mat([[columns[j][i] for j in range(len(columns))] for i in range(DIM)])
 RREF,rank=MAT.rref();rank=int(rank)
 selected=[next(j for j in range(len(columns)) if RREF[i,j]) for i in range(rank)]
 if rank:
  N=fmpq_mat([[MAT[i,j] for j in selected] for i in range(DIM)])
  RT,rnk=N.transpose().rref();assert int(rnk)==rank
  I=[next(j for j in range(DIM) if RT[i,j]) for i in range(rank)]
  S=fmpq_mat([[MAT[i,j] for j in selected] for i in I]);INV=S.inv()
  Id=fmpq_mat([[int(i==j) for j in range(rank)] for i in range(rank)])
  assert S*INV==Id and INV*S==Id
  stats['QQInverseCoordinates']+=2*rank*rank
  restricted=fmpq_mat([[MAT[i,j] for j in range(len(columns))] for i in I])
  assert N*INV*restricted==MAT
  stats['allOriginalColumnCoordinates']=DIM*len(columns)
 else:N=None;I=[];INV=None
 def member(target):
  rhs=flat(target)
  if not rank:
   ok=not any(rhs)
   if ok:stats['targetCoordinates']+=DIM
   return ok
  c=INV*fmpq_mat([[rhs[i]] for i in I]);ret=N*c
  ok=all(ret[i,0]==rhs[i] for i in range(DIM))
  if ok:stats['targetCoordinates']+=DIM
  return ok
 Dval=J(ell)*Al-Tr*Tr
 UU=lam*tt*Dval;power=J(1);found=None
 for n in range(DIM+1):
  tick();ok=member(power)
  say('new_fu_actual_positive_physical_unit_return',factor=name,
      QQDimension=DIM,originalIdealRank=rank,
      target='(lambda*t*Dval)^n',power=n,
      allOriginalTargetCoordinatesReturned=ok)
  if ok:found=n;break
  if n<DIM:power=power*UU
 say('new_fu_whole_factor_complete',factor=name,
     originalFactorDegree=d,retainedQDegree=nq,
     completeQQDimension=DIM,originalIdealMatrixShape=[DIM,len(columns)],
     originalIdealRank=rank,quotientQQDimension=DIM-rank,
     selectedOriginalColumns=selected,selectedCoefficientRows=I,
     selectedOriginalColumnTags=[tags[i] for i in selected],
     positivePhysicalUnitPowerReturned=found,wholeFactorExcluded=found is not None,
     noDOrLambdaOrTInverse=True,
     allQQEmbeddingsAndNonreducedComponentsKept=True,
     statistics=stats)
 return found is not None
closed=[];retained=[]
for name,coeff in FACTORS:
 try:done=run_case(name,coeff)
 except NonUnit as exc:
  done=False;say('new_fu_entire_factor_retained',factor=name,
                reason=str(exc),wholeFactorExcluded=False,noRetryOrPrimeChange=True)
 (closed if done else retained).append(name)
 gc.collect()
say('new_fu_complete_four_original_fibers_summary',
 closedFactors=closed,retainedWholeFactors=retained,
 wholeFuExcluded=not retained,
 wholeFuConclusionRequiresAlreadyProvedC17AndEntireUTwoExclusion=True,
 wholePhiExcluded=False,ordinaryISPClaim=False)
