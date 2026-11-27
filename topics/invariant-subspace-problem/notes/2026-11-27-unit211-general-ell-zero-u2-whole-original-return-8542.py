BRANCH='ell=0, whole u2 weight line'
#!/usr/bin/env python3
"""R150 general ell=0: new whole u2 line original Macaulay return.
No W=0 or Q=1-u assumption. The already closed Q=1-u/ell=0 curve is a paid boundary.
120 seconds / 1 GiB. No previously frozen elimination is rerun.
"""
import json,time,os,sys,hashlib,subprocess,shutil,tempfile,resource
from pathlib import Path
from flint import fmpq,fmpq_mpoly_ctx
import signal
signal.alarm(120)
resource.setrlimit(resource.RLIMIT_AS,(1024**3,1024**3))
start=time.perf_counter()
def say(x=None,**kw):
 if x is None:x=kw
 x['seconds']=time.perf_counter()-start;print(json.dumps(x),flush=True)
ctx=fmpq_mpoly_ctx.get(('Q','unused_weight','x','y','t','dummy_t','zeta','dummy'),'lex');ep,kp,Lp,Tp,fp,tp,zp,dp=ctx.gens();zz=ctx.constant(0);oo=ctx.constant(1)
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
m,qp,x0,x1,t,unused,zeta=map(R,ctx.gens()[:7]);u=R(2);Q=m;l=R(0);Delta=1-Q
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

assert P02==u*(2*u*u-6*u+4-Q)
assert T0==-2*u*(u-1)
assert M==-u*u
assert Dphysical==-T*T
symbolic={'lam':lam,'T':T,'f':f,'ell':l,'Dphysical':Dphysical,'E1':E1.a,'EBe':EB.a,'EBo':EB.b,'N1':NH.a,'NS':NS.a,'PS':PS.a}
say(stage='new_general_ell_zero_same_original_Gram',originalE0N0P1Verified=True,weightedOriginalNPThroughHAHBVerified=True,originalDistinctValueRetained=True,wholeWeightChartExcluded=False)
units=[('Q',ep),('Q_minus_one',ep-1),('paid_Qboundary_ell0_Qplus1',ep+1),('paid_H1_Qplus2',ep+2),('paid_H3_Qminus2',ep-2)]
out=[];cleared_polys=[];cleared_scales=[]
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
 rec={'name':name,'poly':[[list(map(int,m)),str(a)] for m,a in po.to_dict().items()],'den':[[list(map(int,m)),str(a)] for m,a in rr.d.to_dict().items()]};out.append(rec);cleared_polys.append(po);cleared_scales.append(R(rr.d,paid))
 say({'stage':'new_general_ell_zero_original_X_Gram_coordinates','name':name,'degrees':list(map(int,po.degrees())),'terms':len(po.to_dict()),'paidRemoved':hist,'totalDegreeXYt':deg,'originalE0N0P1AndMeanReconstructionVerified':True,'claimExcluded':False})
# New whole Kz=0 degree-four original Macaulay input. No G2 chart inverse.
from fractions import Fraction
from flint import fmpq_poly
def mons_upto(d):
 return [(i,j,k) for n in range(d+1) for i in range(n,-1,-1) for j in range(n-i,-1,-1) for k in [n-i-j]]
allmons=mons_upto(4);assert len(allmons)==35
allmons=allmons[1:]+allmons[:1]
posmon={mm:i for i,mm in enumerate(allmons)}
def mxyz(mm):return Lp**mm[0]*Tp**mm[1]*fp**mm[2]
def coefdict(po):
 out={}
 for mm,cc in po.to_dict().items():
  assert mm[1]==mm[5]==mm[6]==mm[7]==0
  key=tuple(map(int,mm[2:5]))
  out[key]=out.get(key,zz)+cc*ep**int(mm[0])
 return out
matrix=[];labels=[]
for gi,po in enumerate(cleared_polys):
 cmap=coefdict(po)
 for multiplier in mons_upto(2 if gi<4 else 1):
  row=[zz for _ in range(35)]
  for mm,cf in cmap.items():
   target=tuple(mm[j]+multiplier[j] for j in range(3));row[posmon[target]]+=cf
  ret=sum((row[j]*mxyz(allmons[j]) for j in range(35)),zz)
  assert ret==mxyz(multiplier)*po
  assert R(ret)==R(mxyz(multiplier))*cleared_scales[gi]*symbolic[['E1','EBe','EBo','N1','NS','PS'][gi]]
  matrix.append(row);labels.append([gi,list(multiplier)])
assert len(matrix)==48
inputhash=hashlib.sha256('|'.join(str(po) for row in matrix for po in row).encode()).hexdigest()
say(stage='new_whole_ellZero_head_boundary_original_Macaulay4',rows=48,columns=35,
    originalSixRows=6,all48OriginalMonomialProductsMultipliedBack=True,constantColumn=34,inputSHA256=inputhash,
    G2Inverted=False,cubicMinorInverted=False,claimExcluded=False)

def evalmod(po,hv,p):
 out=0
 for mm,cc in po.to_dict().items():
  assert all(mm[j]==0 for j in range(1,8))
  cf=Fraction(str(cc));assert cf.denominator%p
  out=(out+(cf.numerator%p)*pow(cf.denominator%p,-1,p)*pow(hv,int(mm[0]),p))%p
 return out
modulus=1009;sample=7
A=[[evalmod(pp,sample,modulus) for pp in row] for row in matrix]
selection=list(range(48));pr=0
for col in range(34):
 options=[i for i in range(pr,48) if A[i][col]]
 
 if not options:
  say(stage='new_original_head_boundary_Macaulay_selector_rank_incomplete',branch=BRANCH,observedNonconstantRank=pr,originalRows=48,originalColumns=35,claimExcluded=False)
  raise SystemExit(0)
 sw=options[0];A[pr],A[sw]=A[sw],A[pr];selection[pr],selection[sw]=selection[sw],selection[pr]
 inv=pow(A[pr][col],-1,modulus);A[pr]=[(v*inv)%modulus for v in A[pr]]
 for i in range(pr+1,48):
  cf=A[i][col]
  if cf:A[i]=[(A[i][j]-cf*A[pr][j])%modulus for j in range(35)]
 pr+=1
targets=[i for i in range(34,48) if A[i][34]]
assert targets
say(stage='new_whole_ellZero_head_boundary_numeric_row_selector_only',p=modulus,h=sample,selectedOriginalRows=selection[:34],targetCount=len(targets),numericEmptinessNotInferred=True)

def bareiss_det(MM):
 MM=[row[:] for row in MM];prev=oo;sign=1;n=len(MM);checks=0
 for j in range(n-1):
  if not MM[j][j]:
   candidates=[i for i in range(j+1,n) if MM[i][j]]
   if not candidates:return zz,checks
   sw=candidates[0];MM[j],MM[sw]=MM[sw],MM[j];sign=-sign
  pivot=MM[j][j]
  for i in range(j+1,n):
   for k in range(j+1,n):
    num=MM[i][k]*pivot-MM[i][j]*MM[j][k];quo=num/prev
    assert quo*prev==num;checks+=1;MM[i][k]=quo
   MM[i][j]=zz
  prev=pivot
 return sign*MM[-1][-1],checks

def strip_original_units(po):
 previous=po;paid=oo;hist=[]
 for name,atom in units:
  n=0
  while po:
   gg=po.gcd(atom)
   if gg.total_degree()==0:break
   quotient=po/gg;assert quotient*gg==po;po=quotient;paid*=gg;n+=1
  if n:hist.append([name,n])
 assert po*paid==previous
 return po,hist

def univariate(po):
 d=int(po.degrees()[0]);ar=[fmpq(0) for _ in range(max(0,d+1))]
 for mm,cc in po.to_dict().items():
  assert all(mm[j]==0 for j in range(1,8));ar[int(mm[0])]+=cc
 return fmpq_poly(ar)
records=[];gcd_all=None;excluded=False
for tr in targets:
 indices=selection[:34]+[selection[tr]]
 det,nchecks=bareiss_det([matrix[j] for j in indices]);assert det
 reduced,hist=strip_original_units(det);pol=univariate(reduced);assert pol
 if gcd_all is None:gcd_all=pol
 else:
  old=gcd_all
  gg,aa,bb=old.xgcd(pol)
  assert aa*old+bb*pol==gg
  gcd_all=gg
 rec=dict(originalRows=indices,lastOriginalRow=selection[tr],fullDegree=int(det.degrees()[0]),remainingDegree=int(reduced.degrees()[0]),paidRemoved=hist,
          exactBareissDivisionProducts=nchecks,originalFixed35By35Determinant=True,
          determinantSHA256=hashlib.sha256(str(det).encode()).hexdigest(),
          remainingSHA256=hashlib.sha256(str(reduced).encode()).hexdigest(),
          runningQQGCDDegree=int(gcd_all.degree()),runningQQGCD=str(gcd_all) if gcd_all.degree()<=20 else None)
 records.append(rec)
 say(stage='new_whole_ellZero_head_boundary_original_QQ_Macaulay_determinant',**rec,claimExcluded=False)
 if gcd_all.degree()==0:excluded=True;break
signal.alarm(0)
say(stage='new_whole_ellZero_head_boundary_original_Macaulay_return_complete',sourceSHA256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
    inputSHA256=inputhash,fullParameterBranchRationalization=BRANCH,
    allPhysicalUnitsCovered=True,onlyOriginalPaidFactorsDivided=True,QQBezoutProductsMultipliedBack=len(records)>1,
    fullellZero_head_boundaryExcluded=excluded,determinantCount=len(records),runningQQGCDDegree=int(gcd_all.degree()),
    peakRssKiB=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss,ordinaryISPClaim=False)

