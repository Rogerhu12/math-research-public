#!/usr/bin/env python3
"""R150 general LS / original Delta=0 / W=0: the whole k=-1 line is empty.
Reconstruct the same original Gram, all six original rows, two QQ[e] cofactor
identities, the complete 12-dimensional cover, and every whole QQ-algebra return.
No cached polynomials or multivariate modular emptiness are used.
"""
import json,time,os,sys,hashlib,subprocess,shutil,tempfile,resource
from pathlib import Path
from flint import fmpq,fmpq_mpoly_ctx
import signal
signal.alarm(180)
resource.setrlimit(resource.RLIMIT_AS,(4*1024**3,4*1024**3))
start=time.perf_counter()
def say(x=None,**kw):
 if x is None:x=kw
 x['seconds']=time.perf_counter()-start;print(json.dumps(x),flush=True)
ctx=fmpq_mpoly_ctx.get(('e','k','x','y','t','dummy_t','zeta','dummy'),'lex');ep,kp,Lp,Tp,fp,tp,zp,dp=ctx.gens();zz=ctx.constant(0);oo=ctx.constant(1)
def poly(v):return v if hasattr(v,'to_dict') else ctx.constant(v)
class R:
 def __init__(self,n=0,d=None,reduce=True):
  if isinstance(n,R):self.n=n.n;self.d=n.d;return
  n=poly(n);d=oo if d is None else poly(d);assert d
  if not n:self.n=zz;self.d=oo;return
  if reduce:
   g=n.gcd(d);n=n/g;d=d/g
  lc=d.coefficient(0);self.n=n/lc;self.d=d/lc
 def __bool__(self):return bool(self.n)
 def __add__(self,o):
  o=R(o)
  if not self:return o
  if not o:return self
  g=self.d.gcd(o.d);a=self.d/g;b=o.d/g
  return R(self.n*b+o.n*a,a*o.d)
 __radd__=__add__
 def __neg__(self):return R(-self.n,self.d,False)
 def __sub__(self,o):return self+-R(o)
 def __rsub__(self,o):return R(o)+-self
 def __mul__(self,o):
  o=R(o)
  if not self or not o:return R()
  g=self.n.gcd(o.d);h=o.n.gcd(self.d)
  return R((self.n/g)*(o.n/h),(self.d/h)*(o.d/g),False)
 __rmul__=__mul__
 def __truediv__(self,o):o=R(o);assert o;return self*R(o.d,o.n,False)
 def __rtruediv__(self,o):return R(o)/self
 def __pow__(self,n):return R(self.d**(-n),self.n**(-n),False) if n<0 else R(self.n**n,self.d**n,False)
 def __eq__(self,o):o=R(o);return self.n*o.d==o.n*self.d
e,k,x0,x1,t,unused,zeta=map(R,ctx.gens()[:7]);u=e+1;Q=e*k;Vbar=(e+1)*k+2;l=(e+1)*((k+2)**2-2*e*k)/(k*Vbar);Delta=1-Q
class E:
 def __init__(self,a=0,b=0):
  if isinstance(a,E):self.a=a.a;self.b=a.b;return
  self.a=R(a);self.b=R(b)
 def __bool__(self):return bool(self.a) or bool(self.b)
 def __add__(self,o):o=E(o);return E(self.a+o.a,self.b+o.b)
 __radd__=__add__
 def __neg__(self):return E(-self.a,-self.b)
 def __sub__(self,o):return self+-E(o)
 def __rsub__(self,o):return E(o)+-self
 def __mul__(self,o):o=E(o);return E(self.a*o.a+Delta*self.b*o.b,self.a*o.b+self.b*o.a)
 __rmul__=__mul__
 def __pow__(self,n):
  out=E(1)
  for _ in range(n):out=out*self
  return out
 def __eq__(self,o):o=E(o);return self.a==o.a and self.b==o.b
 def conj(self):return E(self.a,-self.b)
b=E(l/2,(u-l)/(2*Delta));c=b.conj();a=E(1-l)
p=E(1,1);q=p.conj();bc=(l*l-(u-l)**2/Delta)/4
ivdiff=E(0,-1/(2*Delta));ivbp=c*q*ivdiff*E(1/(bc*Q));ivcq=b*p*ivdiff*E(1/(bc*Q))
assert ivbp*b*p*(q-p)==1 and ivcq*c*q*(q-p)==1
V2=2*u-l*Q;T0=V2-2*u*u;P02=(2-3*u)*V2-Q*u+2*u**3
X=E(x0,x1);Y=X.conj()
f=(u*x0+(u-l*Q)*x1-T0/2)/(2*u)
W2=V2*x0+(2*u-u*Q-l*Q)*x1
lam=(W2-u*T0-(V2+2*u*u)*f+bc*Q*t)/P02
J=2*u*(1-u)+l*Q;Phi=T0+4*u-4+Q;Pf=T0*(J-Q)
g=lam*P02-(1-u)*T0
T=(g*T0-Pf*f-Phi*bc*Q*t)/(Q*P02)-l
r=X-a*p-c*E(t);s=Y-a*q-b*E(t);A=E(2*f)-2*b*X-2*c*Y+E(2*bc*t)
rows=[[E(),E(),p,q],[E(),A,r,s],[p,r,E(),E(t)],[q,s,E(t),E()]]
one=[E(1),E(),E(1),E(1)]
def va(v,z):return [a+b for a,b in zip(v,z)]
def vs(a,v):return [a*b for b in v]
def vm(v,z):return [v[0]*z[0],v[0]*z[1]+v[1]*z[0],v[2]*z[2],v[3]*z[3]]
def tau(v):return a*v[0]+v[1]+b*v[2]+c*v[3]
def DK(v):return [tau(vm(row,v)) for row in rows]
d=DK(one);F2=tau(d);Kd=DK(d)
assert F2==E(2*f)
def mean(j):
 ee=2*tau(vm(rows[0],rows[1])) if j==1 else tau(vm(rows[j],rows[j]))
 return ee-2*Kd[j]-2*vm(d,d)[j]+2*F2*d[j]
assert not mean(0)
E1,EB,EC=mean(1),mean(2),mean(3)
assert not E1.b and EB.conj()==EC

def N4(v):
 return 2*tau(vm(d,vm(v,v)))-F2*tau(vm(v,v))-4*tau(v)*tau(vm(d,v))+2*F2*tau(v)**2+tau(vm(v,DK(v)))
v=rows[0];zzv=rows[1]
Nv=N4(va(v,zzv))-N4(v)-N4(zzv)
vc=va(v,vs(-tau(v),one));zc=va(zzv,vs(-tau(zzv),one))
Pj=3*tau(vm(vm(vc,vc),zc))
NH=Nv-E(lam*fmpq(4,3))*Pj
assert not NH.b




assert N4(rows[0])==E(2*lam*P02)
assert Pj==E(3*(lam-1-T)*P02)
assert (Phi*(J-2*u*Q)-Pf)==0
A2=2*lam*lam-2*lam+1;B3=4*lam**3-6*lam*lam+3*lam-1

def P2(vv):
 cc=va(vv,vs(-tau(vv),one));return tau(vm(vm(cc,cc),cc))
NS=b*N4(rows[2])+c*N4(rows[3])-E(2*lam*P02*(l+2*T+A2))
PS=b*P2(rows[2])+c*P2(rows[3])-E(P02*(l+3*T+3*A2+B3))
assert not NS.b and not PS.b

# Explicit original value traces for the two weighted singleton rows.
assert P2(rows[0])==E(P02)
v1=(T-l*zeta)/u;v0=v1+zeta;hh=E(1+v0,v1);kk=hh.conj()
M=l*(2*u-l*Q)-u*u;Dphysical=l*A2-T*T
HA=l*M*zeta*zeta-2*T*M*zeta+V2*T*T-u*u*A2
zvalue=(hh-1)*(kk-1);assert not zvalue.b
HB=u*u*(B3-2*v0*A2+zvalue.a*T)
assert b*(hh-1)+c*(kk-1)==E(T)
assert b*hh*hh+c*kk*kk==E(l+2*T+A2+HA/(u*u))
assert b*hh**3+c*kk**3==E(l+3*T+3*A2+B3+((3+2*v0)*HA-HB)/(u*u))
weightedNB=b*(N4(rows[2])-E(2*lam*P02)*hh*hh)+c*(N4(rows[3])-E(2*lam*P02)*kk*kk)
weightedPB=b*(P2(rows[2])-E(P02)*hh**3)+c*(P2(rows[3])-E(P02)*kk**3)
assert weightedNB==NS-E(2*lam*P02*HA/(u*u))
assert weightedPB==PS-E(P02*((3+2*v0)*HA-HB)/(u*u))
assert E(Dphysical+l*HA/(u*u))==E(bc)*(hh-kk)**2
assert 4*bc*(1-Q)==M
Vlead=u*(Q+2)-2
assert Vlead==e*Vbar
W=(Phi*(J-2*u*Q)-Pf)/2;assert not W
Pp=2*e*k-k*k-5*k-8
M13=4*e**3*k*k-3*e*e*k**3-12*e*e*k*k-16*e*e*k+e*k**4+8*e*k**3+24*e*k*k+32*e*k+16*e-k**3-8*k*k-20*k-16
assert P02==-2*e*e*(e+1)*Pp/Vbar
assert Phi==-2*e*e*(k+4)/Vbar
assert M==-(e+1)**2*M13/(k*Vbar**2)
symbolic={'lam':lam,'T':T,'f':f,'ell':l,'Dphysical':Dphysical,'E1':E1.a,'EBe':EB.a,'EBo':EB.b,'N1':NH.a,'NS':NS.a,'PS':PS.a}
say(stage='same_original_Gram_and_weighted_NP_trace_identities',originalE0N0P1Verified=True,originalMeanAndN1Verified=True,P2BaseIdentityVerified=True,weightedOriginalNAndPTracesThroughHAHBVerified=True,HankelPhysicalUnitIdentityVerified=True,WWeightAndPaidUnitIdentitiesVerified=True,noXMinusUMinusOneInverted=True,claimExcluded=False)

M=l*(2*u-l*Q)-u*u
units=[('e',ep),('k',kp),('u',ep+1),('distinct_p_q',ep*kp-1),('W_paid_leading',ep*kp+kp+2),('Phi',kp+4),('P02',P02.n),('bc',M.n)]
out=[]
for name,rr,deg in [('E1',E1.a,2),('EBe',EB.a,2),('EBo',EB.b,2),('N1',NH.a,2),('weighted_N',NS.a,3),('weighted_P',PS.a,3)]:
 assert all(int(m[2])+int(m[3])+int(m[4])<=deg for m in rr.n.to_dict())
 po=rr.n;paid=oo;hist=[]
 for name0,atom in units:
  ct=0
  while po:
   gg=po.gcd(atom)
   if gg.total_degree()==0:break
   po=po/gg;paid*=gg;ct+=1
  if ct:hist.append([name0,ct])
 assert po*paid==rr.n
 den=rr.d
 for name0,atom in units:
  while den:
   gg=den.gcd(atom)
   if gg.total_degree()==0:break
   den=den/gg
 assert den.total_degree()==0
 rec={'name':name,'poly':[[list(map(int,m)),str(a)] for m,a in po.to_dict().items()],'den':[[list(map(int,m)),str(a)] for m,a in rr.d.to_dict().items()]};out.append(rec)
 say({'stage':'new_W0_original_X_Gram_coordinates','name':name,'degrees':list(map(int,po.degrees())),'terms':len(po.to_dict()),'paidRemoved':hist,'totalDegreeXYt':deg,'originalE0N0P1AndMeanReconstructionVerified':True,'claimExcluded':False})

from flint import fmpq_poly
data=out
e=fmpq_poly([0,1]);zero=fmpq_poly([]);one=fmpq_poly([1])
V=1-e;Pp=-2*e-4
# M13 below is reconstructed from the exact general formula, not assumed.
M13=4*e**3+3*e**2-12*e**2+16*e**2+e-8*e+24*e-32*e+16*e+1-8+20-16
assert M13==4*e**3+7*e**2+e-3
units=[('e',e),('u',e+1),('Vbar',1-e),('P02',e+2),('bc',M13)]
mons=sorted([(i,j,k) for i in range(5) for j in range(5-i) for k in range(5-i-j)],key=lambda m:(sum(m),m),reverse=True)
assert len(mons)==35 and mons[-1]==(0,0,0)
rows=[];labels=[];originals=[]
for rec in data:
 co={}
 for m,a in rec['poly']:
  assert m[5]==m[6]==m[7]==0
  mo=tuple(m[2:5]);co[mo]=co.get(mo,zero)+fmpq(a)*(-1)**m[1]*e**m[0]
 co={mo:a for mo,a in co.items() if a};assert co
 content=zero
 for a in co.values():content=content.gcd(a)
 paid=one;hist=[]
 for name,at in units:
  ct=0
  while content:
   gg=content.gcd(at)
   if gg.degree()==0:break
   qq,rr=divmod(content,gg);assert not rr and qq*gg==content;content=qq;paid*=gg;ct+=1
  if ct:hist.append([name,ct])
 out={mo:a/paid for mo,a in co.items()};assert all(out[mo]*paid==co[mo] for mo in co)
 originals.append(out)
 deg=max(sum(m) for m in out)
 multipliers=[m for m in mons if sum(m)<=4-deg]
 for mm in multipliers:
  row=[]
  for mo in mons:
   dif=tuple(mo[i]-mm[i] for i in range(3));row.append(out.get(dif,zero) if min(dif)>=0 else zero)
  # Reconstruct every polynomial multiplication row as a coefficient dictionary.
  reconstruction={mo:a for mo,a in zip(mons,row) if a}
  assert reconstruction=={tuple(mo[i]+mm[i] for i in range(3)):a for mo,a in out.items()}
  rows.append(row);labels.append([rec['name'],mm])
 say(stage='whole_k_minus_one_original_row',name=rec['name'],degreeXyt=deg,maxDegreeE=max(a.degree() for a in out.values()),paidRemoved=hist,terms=len(out),multipliers=len(multipliers),claimExcluded=False)
n=len(rows);assert n==48
AA=[row[:] for row in rows];previous=one;steps=[];selection=list(range(n))
for z in range(34):
 sw=z
 if not AA[z][z]:
  candidates=[i for i in range(z+1,n) if AA[i][z]]
  if not candidates:raise RuntimeError('missing pivot at '+str(z))
  sw=min(candidates,key=lambda i:AA[i][z].degree());AA[z],AA[sw]=AA[sw],AA[z];selection[z],selection[sw]=selection[sw],selection[z]
 pivot=AA[z][z];assert pivot
 lower=[AA[i][z] for i in range(z+1,n)];steps.append((pivot,lower,sw))
 for i in range(z+1,n):
  for j in range(z+1,35):
   numerator=AA[i][j]*pivot-AA[i][z]*AA[z][j]
   quotient,remainder=divmod(numerator,previous)
   assert not remainder and quotient*previous==numerator;AA[i][j]=quotient
  AA[i][z]=zero
 previous=pivot
 if z%3==0 or z>=30:say(stage='original_M35_fraction_free_step',index=z,degreeE=pivot.degree(),swappedRow=sw,claimExcluded=False)
polys=[]
for i in range(34,n):
 pp=AA[i][34]
 if pp:polys.append((i,pp))
say(stage='whole_k_minus_one_original_M35_constant_rows',count=len(polys),degrees=[p.degree() for i,p in polys],rankMinorDegree=steps[-1][0].degree(),claimExcluded=False)
GG=zero;used=[]
for i,pp in polys:
 old=GG;GG,a,b=old.xgcd(pp);assert a*old+b*pp==GG
 if GG!=old:
  used.append(i);say(stage='actual_QQ_constant_row_gcd',row=i,gcdDegree=GG.degree(),polynomialSHA256=hashlib.sha256(str(GG).encode()).hexdigest(),claimExcluded=False)
assert GG
sc,ff=GG.factor();product=fmpq_poly([sc])
for p,m in ff:product*=p**m
assert product==GG
say(stage='original_M35_cover_factorization',factors=[dict(degree=p.degree(),multiplicity=m,coefficients=[str(a) for a in p]) for p,m in ff],usedRows=used,claimExcluded=False)

class Rat:
 def __init__(self,n=0,d=None):
  if isinstance(n,Rat):self.n=n.n;self.d=n.d;return
  n=n if isinstance(n,fmpq_poly) else fmpq_poly([n]);d=one if d is None else d;assert d
  if not n:self.n=zero;self.d=one;return
  g=n.gcd(d);n=n/g;d=d/g;lc=d.leading_coefficient();self.n=n/lc;self.d=d/lc
 def __add__(self,o):o=Rat(o);return Rat(self.n*o.d+o.n*self.d,self.d*o.d)
 __radd__=__add__
 def __neg__(self):return Rat(-self.n,self.d)
 def __sub__(self,o):return self+-Rat(o)
 def __rsub__(self,o):return Rat(o)+-self
 def __mul__(self,o):o=Rat(o);return Rat(self.n*o.n,self.d*o.d)
 __rmul__=__mul__
 def __truediv__(self,o):o=Rat(o);assert o.n;return Rat(self.n*o.d,self.d*o.n)
 def __eq__(self,o):o=Rat(o);return self.n*o.d==o.n*self.d
for target in [40,41]:
 alpha=[Rat(int(i==target)) for i in range(n)]
 for z in range(33,-1,-1):
  pivot,lower,sw=steps[z];previous=one if z==0 else steps[z-1][0]
  alpha[z]=alpha[z]-sum((alpha[i]*Rat(lower[i-z-1],previous) for i in range(z+1,n)),Rat(0))
  for i in range(z+1,n):alpha[i]=alpha[i]*Rat(pivot,previous)
  if sw!=z:alpha[z],alpha[sw]=alpha[sw],alpha[z]
 assert all(a.d.degree()==0 for a in alpha)
 cp=[a.n/a.d[0] for a in alpha]
 for j in range(35):assert sum((cp[i]*rows[i][j] for i in range(n)),zero)==(AA[target][34] if j==34 else zero)
 say(stage='complete_original_35_column_constant_cofactor',row=target,degreeE=AA[target][34].degree(),cofactorMaxDegree=max(a.degree() for a in cp),cofactorSHA256=hashlib.sha256('|'.join(str(a) for a in cp).encode()).hexdigest(),all35ProductsMultipliedBack=True,claimExcluded=False)

actual_cover,bez0,bez1=AA[40][34].xgcd(AA[41][34])
assert bez0*AA[40][34]+bez1*AA[41][34]==actual_cover and actual_cover==GG
say(stage='complete_original_two_constant_row_Bezout',inputDegrees=[AA[40][34].degree(),AA[41][34].degree()],gcdDegree=GG.degree(),coefficientDegrees=[bez0.degree(),bez1.degree()],allProductsMultipliedBack=True,identitySHA256=hashlib.sha256('|'.join(map(str,[bez0,bez1])).encode()).hexdigest(),claimExcluded=False)

cover=GG
for name,at in units:
 while cover:
  gg=cover.gcd(at)
  if gg.degree()==0:break
  previous_cover=cover;cover=cover/gg;assert cover*gg==previous_cover
repeat=cover.gcd(cover.derivative());squarefree=cover/repeat;assert squarefree*repeat==cover;cover=squarefree/squarefree.leading_coefficient();assert cover.degree()==12 and cover.gcd(cover.derivative()).degree()==0
say(stage='complete_whole_weight_cover',degree=12,allPaidFactorDivisionsMultipliedBack=True,allLeadingZeroFibersRetained=True,coverSHA256=hashlib.sha256(str(cover).encode()).hexdigest(),claimExcluded=False)
sc,fac=cover.factor();complete_product=fmpq_poly([sc])
for phi,mul in fac:complete_product*=phi**mul
assert complete_product==cover
last_fiber=None;closed_degree=0
for phi,mul in fac:
 assert mul==1
 def red(p):return p%phi
 def inv(p):
  gg,a,b=p.xgcd(phi);assert gg==1 and a*p+b*phi==1;return red(a)
 MM=[[red(a) for a in row] for row in rows]
 comb=[[one if i==j else zero for j in range(n)] for i in range(n)]
 pos=0;pivots=[]
 for j in range(35):
  candidates=[i for i in range(pos,n) if MM[i][j]]
  if not candidates:continue
  sw=candidates[0];MM[pos],MM[sw]=MM[sw],MM[pos];comb[pos],comb[sw]=comb[sw],comb[pos]
  pivot=MM[pos][j];iv=inv(pivot)
  MM[pos]=[red(a*iv) for a in MM[pos]];comb[pos]=[red(a*iv) for a in comb[pos]]
  for i in range(n):
   if i==pos or not MM[i][j]:continue
   z=MM[i][j];MM[i]=[red(a-z*b) for a,b in zip(MM[i],MM[pos])];comb[i]=[red(a-z*b) for a,b in zip(comb[i],comb[pos])]
  pivots.append(j);pos+=1
  if pos==n:break
 for i in range(pos):
  for j in range(35):assert red(sum((comb[i][z]*rows[z][j] for z in range(n)),zero))==MM[i][j]
 constant=34 in pivots
 say(stage='whole_QQ_algebra_original_M35_return',factor=[str(a) for a in phi],dimension=phi.degree(),rank=pos,pivotColumns=pivots,constantInRowSpace=constant,allOriginalRowCombinationsMultipliedBack=True,claimExcluded=constant)
 if constant:
  closed_degree+=phi.degree()
  unitrow=comb[pivots.index(34)]
  assert all(red(sum((unitrow[z]*rows[z][j] for z in range(n)),zero))==(one if j==34 else zero) for j in range(35))
  say(stage='whole_QQ_algebra_original_constant_unit_certificate',dimension=phi.degree(),unitCombinationSHA256=hashlib.sha256('|'.join(str(a) for a in unitrow).encode()).hexdigest(),all35ColumnsActuallyMultipliedBack=True,claimExcluded=True)
 if not constant:
  assert phi==fmpq_poly([3,5,4])
  last_fiber=(phi,MM,pivots,comb)
  free=[j for j in range(35) if j not in pivots]
  say(stage='whole_QQ_algebra_original_kernel_columns',factorDegree=phi.degree(),freeMonomials=[mons[j] for j in free],claimExcluded=False)

assert last_fiber is not None
phi,MM,pivots,comb=last_fiber
xi=mons.index((1,0,0));ci=mons.index((0,0,0));yi=mons.index((0,1,0));ti=mons.index((0,0,1));x2i=mons.index((2,0,0))
assert [mons[i] for i in range(35) if i not in pivots]==[(1,0,0),(0,0,0)]
yrow=MM[pivots.index(yi)];trow=MM[pivots.index(ti)];xrow=MM[pivots.index(x2i)]
quad=[xrow[ci],xrow[xi],one]
def trim(p):
 p=[red(a) for a in p]
 while p and not p[-1]:p.pop()
 return p
def add(p,q):return trim([(p[i] if i<len(p) else zero)+(q[i] if i<len(q) else zero) for i in range(max(len(p),len(q)))])
def neg(p):return [-a for a in p]
def sub(p,q):return add(p,neg(q))
def rawmul(p,q):
 if not p or not q:return []
 out=[zero]*(len(p)+len(q)-1)
 for i,a in enumerate(p):
  for j,b in enumerate(q):out[i+j]=red(out[i+j]+a*b)
 return trim(out)
def pdiv(p,q):
 p=trim(p);q=trim(q);initial=p[:];assert q;out=[zero]*max(0,len(p)-len(q)+1);iq=inv(q[-1])
 while len(p)>=len(q):
  j=len(p)-len(q);z=red(p[-1]*iq);out[j]=z
  p=sub(p,[zero]*j+[red(z*a) for a in q])
 quotient,remainder=trim(out),trim(p)
 assert add(rawmul(quotient,q),remainder)==initial
 return quotient,remainder
def mod(p):return pdiv(p,quad)[1]
def mul(p,q):return mod(rawmul(p,q))
def power(p,n):
 out=[one]
 for _ in range(n):out=mul(out,p)
 return out
def scale(p,q):return [red(a*q) for a in p]
xx=[zero,one];yy=neg([yrow[ci],yrow[xi]]);tt=neg([trow[ci],trow[xi]])
say(stage='last_quadratic_same_point_reconstruction',factor=[str(a) for a in phi],y=[str(a) for a in yy],t=[str(a) for a in tt],monicXQuadratic=[str(a) for a in quad],claimExcluded=False)
ns=symbolic
def evaluate_raw(pp):
 out=[]
 for m,a in pp.to_dict().items():
  assert m[5]==m[6]==m[7]==0
  term=[red(fmpq(a)*(-1)**m[1]*e**m[0])]
  for v,n0 in zip([xx,yy,tt],m[2:5]):term=mul(term,power(v,int(n0)))
  out=add(out,term)
 return mod(out)
def peval(rr):
 nn=evaluate_raw(rr.n);dd=evaluate_raw(rr.d);assert len(dd)==1
 return scale(nn,inv(dd[0]))
lamv=peval(ns['lam']);Tv=peval(ns['T']);fv=peval(ns['f'])
for name,rr in [(name,ns[name]) for name in ['E1','EBe','EBo','N1','NS','PS']]:
 val=peval(rr);assert not val;say(stage='last_quadratic_exact_original_row_return',name=name,remainder=[str(a) for a in val],claimExcluded=False)
say(stage='last_quadratic_same_lambda_T_f',lam=[str(a) for a in lamv],T=[str(a) for a in Tv],f=[str(a) for a in fv],claimExcluded=False)


assert quad==[fmpq_poly([fmpq(1,4)]),-one,one]
assert trim(yy)==[fmpq_poly([fmpq(1,2)])] and not trim(tt)
assert peval(ns['ell'])==[fmpq_poly([fmpq(1,2)])]
assert Tv==[fmpq_poly([fmpq(-1,2)])]
slope=red(e/6+fmpq(3,8))
assert lamv==[red(fmpq(1,2)-slope/2),slope]
assert not peval(ns['Dphysical'])
say(stage='last_whole_quadratic_algebra_original_Hankel_contradiction',baseFactor='4e^2+5e+3',baseDimension=2,actualOriginalY='1/2',actualOriginalTGram='0',actualOriginalMonicXRelation='(x-1/2)^2',sameEll='1/2',sameValueT='-1/2',sameLambda='1/2+(e/6+3/8)*(x-1/2)',originalHankelDExactlyZeroInNonReducedQuadraticAlgebra=True,originalHankelDIsPreviouslyPaidPhysicalUnit=True,allAlgebraEmbeddingsAndNilpotentsRetained=True,claimExcluded=True)
assert closed_degree==10 and last_fiber[0].degree()==2
signal.alarm(0)
say(stage='complete_W0_k_minus_one_original_line_exclusion',wholeW0KMinusOneExcluded=True,totalQQCoverDegree=12,fourEntireAlgebrasExcludedByOriginalUnitCombinations=10,lastEntireAlgebraExcludedByOriginalHankelUnit=2,noCachedPolynomialInputs=True,noMultivariateModularEmptyInference=True,noXMinusUMinusOneInverted=True,wholeW0Excluded=False,ordinaryISPClaim=False,sourceSHA256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),peakRssKiB=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)
