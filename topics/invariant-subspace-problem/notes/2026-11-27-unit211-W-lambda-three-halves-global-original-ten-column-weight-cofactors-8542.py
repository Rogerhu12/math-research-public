#!/usr/bin/env python3
"""Whole current W, lambda=3/2: new global fixed ten-column original cofactors.
Three original means times 1,F,S plus N1,NS,PS or original value rT.
Exact polynomial adjugate rows, all 10 columns; no A143 or new head inverse.
180 seconds / 4 GiB.  Self-contained; no old projection gate is rerun."""
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
ctx=fmpq_mpoly_ctx.get(('e','k','F','lambda','S','dummy_t','zeta','dummy'),'lex');ep,kp,Lp,Tp,fp,tp,zp,dp=ctx.gens();zz=ctx.constant(0);oo=ctx.constant(1)
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

# New affine coordinates. Their inverse uses no unpaid head or Cramer factor.
Fcoord,Lcoord,Scoord=map(R,(Lp,Tp,fp));Lcoord=R(fmpq(3,2))
f_target=(Fcoord+u*Lcoord)/2;lambda_target=Lcoord;T_target=Scoord+2*Lcoord
J=2*u*(1-u)+l*Q;Phi=T0+4*u-4+Q;Pf=T0*(J-Q)
Mweight=l*V2-u*u;Cy=2*u-u*Q-l*Q;gy=u-l*Q
assert u*Cy-gy*V2==Q*Mweight
t=(T0*(lambda_target*P02-(1-u)*T0)-Pf*f_target-Q*P02*(T_target+l))/(Phi*bc*Q)
glinear=2*u*f_target+T0/2
W2linear=lambda_target*P02+u*T0+(V2+2*u*u)*f_target-bc*Q*t
x0=(Cy*glinear-gy*W2linear)/(Q*Mweight)
x1=(u*W2linear-V2*glinear)/(Q*Mweight)
assert u*x0+gy*x1==glinear
assert V2*x0+Cy*x1==W2linear
jacobian=-Phi*bc*Q*Mweight/(u*P02*P02)
assert jacobian and Mweight==4*bc*(1-Q)
say(stage='new_original_physical_affine_coordinate_inverse',coordinates=['F=2*f-u*lambda','lambda','S=T-2*lambda'],jacobian='-Phi*bc*Q*M/(u*P02^2)',allInverseDenominatorsPreviouslyPaid=True,allOriginalLinearInverseProductsVerified=True,claimExcluded=False)

X=E(x0,x1);Y=X.conj()
f=(u*x0+(u-l*Q)*x1-T0/2)/(2*u)
W2=V2*x0+(2*u-u*Q-l*Q)*x1
lam=(W2-u*T0-(V2+2*u*u)*f+bc*Q*t)/P02
J=2*u*(1-u)+l*Q;Phi=T0+4*u-4+Q;Pf=T0*(J-Q)
g=lam*P02-(1-u)*T0
T=(g*T0-Pf*f-Phi*bc*Q*t)/(Q*P02)-l
assert f==f_target and lam==lambda_target and T==T_target
say(stage='new_same_original_E0_N0_P1_physical_coordinates',actualOriginalFEqualsAffineTarget=True,actualOriginalLambdaEqualsTarget=True,actualOriginalTEqualsAffineTarget=True,claimExcluded=False)
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

# Whole lambda fiber: all scalar symbols e,k stay independent.
assert lam==fmpq(3,2)
m=u-l;dw=1-Q;M=l*l*dw-m*m
hF=u*u*m*dw*Phi/(e*M)
qF=(m*EB.a+l*dw*EB.b)/hF
astar=4*u*Q-J;cstar=astar*m*m+J*dw*l*l
D=l*A2-T*T;K=l*l*B3-3*l*T*A2+2*T**3
ad=M*l*l*Q*(3-4*lam)+M*astar*T*T+cstar*D
bd=2*M*m*astar*T
R4=M*ad*ad-D*bd*bd;C4=2*m*D*ad+K*bd
qT=C4/(8*m*u*Q*l*l*dw)
# [T^4]R4 equals its S^4 coefficient because T=S+3.
def r_coefficient(pp,fi,sj):
 pp=R(pp);nn=ctx.constant(0)
 for mm,cc in pp.n.to_dict().items():
  if mm[2]==fi and mm[4]==sj:
   assert all(mm[j]==0 for j in [3,5,6,7])
   nn+=cc*ep**int(mm[0])*kp**int(mm[1])
 return R(nn,pp.d)
assert r_coefficient(qF,2,0)==1
assert r_coefficient(qT,0,4)==1
rT=R4-r_coefficient(R4,0,4)*qT
assert r_coefficient(rT,0,4)==0 and r_coefficient(rT,0,3)==0
wctx=fmpq_mpoly_ctx.get(('e','k'),'lex');we,wk=wctx.gens()
wzero=wctx.constant(0);wone=wctx.constant(1)
def scalar(po):
 out=wzero
 for mm,cc in po.to_dict().items():
  assert all(mm[j]==0 for j in [2,3,4,5,6,7])
  out+=cc*we**int(mm[0])*wk**int(mm[1])
 return out
Hw=4*e*k-k*k-4*k-8
C9w=4*e*e*k*k-e*(k**4+9*k**3+20*k*k+16*k)+k**3+10*k*k+24*k+16
J19w=16*e**4*k**3-8*e**3*k**4-16*e**3*k**3-96*e**3*k*k-e*e*k**5-8*e*e*k**4+24*e*e*k**3+64*e*e*k*k+192*e*e*k-2*e*k**5-14*e*k**4-12*e*k**3-128*e-k**5-10*k**4-40*k**3-104*k*k-160*k-128
D27w=16*e**5*k**4-4*e**4*k**5+32*e**4*k**4+2*e**3*k**6-12*e**3*k**5-96*e**3*k**4-384*e**3*k**3-384*e**3*k*k+3*e*e*k**6+8*e*e*k**5+60*e*e*k**4+384*e*e*k**3+1088*e*e*k*k+1024*e*e*k-10*e*k**5-28*e*k**4+48*e*k**3+64*e*k*k-512*e*k-768*e-k**6-18*k**5-120*k**4-440*k**3-1008*k*k-1344*k-768
atoms=[e,k,u,Q,dw,Vbar,l,m,M,Phi,P02,bc,2*e+1,k+1,k+2,k+4,T0,J-Q,Hw,C9w,u-Q,J19w,D27w]
names=['e','k','u','Q','d','V','ell','m','M','Phi','P02','bc','2e+1','k+1','k+2','k+4','T0','J-Q','H','C9','u-Q','J19','D27']
unitpolys=[scalar(R(a).n) for a in atoms];assert all(unitpolys)
denchecked=set()
def checkden(den):
 key=str(den)
 if key in denchecked:return
 rem=den
 for atom in unitpolys:
  while True:
   g=rem.gcd(atom)
   if g.total_degree()==0:break
   nxt=rem/g;assert nxt*g==rem;rem=nxt
 assert rem.total_degree()==0,'new scalar denominator is not paid'
 denchecked.add(key)
def prof(po,include=False):
 dd=[[list(map(int,mm)),str(cc)] for mm,cc in sorted(po.to_dict().items())]
 bb=json.dumps(dd,separators=(',',':')).encode()
 r=dict(degrees=list(map(int,po.degrees())),totalDegree=int(po.total_degree()),terms=len(dd),
 bytes=len(bb),sha256=hashlib.sha256(bb).hexdigest())
 if include and len(bb)<=8192:r['coefficients']=dd
 return r
def input_row(pp):
 pp=R(pp);den=scalar(pp.d);checkden(den);groups={}
 for mm,cc in pp.n.to_dict().items():
  assert all(mm[j]==0 for j in [3,5,6,7])
  key=(int(mm[2]),int(mm[4]))
  groups[key]=groups.get(key,wzero)+cc*we**int(mm[0])*wk**int(mm[1])
 groups={mm:v for mm,v in groups.items() if v}
 assert groups
 common=next(iter(groups.values()))
 for p0 in groups.values():common=common.gcd(p0)
 removed=wone
 for atom in unitpolys:
  while True:
   g=common.gcd(atom)
   if g.total_degree()==0:break
   common=common/g;removed*=g
 out={mm:po/removed for mm,po in groups.items()}
 assert all(out[mm]*removed==po for mm,po in groups.items())
 # Full original embedding of normalized rows and their exact paid factor.
 def back(p0):
  val=ctx.constant(0)
  for mm,cc in p0.to_dict().items():val+=cc*ep**int(mm[0])*kp**int(mm[1])
  return val
 rebuilt=R()
 for mm,po in out.items():
  rebuilt+=R(back(po)*back(removed),back(den))*Fcoord**mm[0]*Scoord**mm[1]
 assert rebuilt==pp
 checkden(removed)
 return out,dict(originalDenominator=prof(den),paidContentRemoved=prof(removed),
                 maxGeometryDegree=max(sum(mm) for mm in out),allOriginalProductsActuallyVerified=True)
spec=[('mean_qF',qF),('E1',E1.a),('EBe',EB.a),('N1',NH.a),('NS',NS.a),('PS',PS.a),('original_value_rT',rT)]
polys={};input_profiles={}
for name,pp in spec:
 po,rec=input_row(pp);polys[name]=po;input_profiles[name]=rec
 assert rec['maxGeometryDegree']<=(2 if name not in ['NS','PS'] else 3)
basis=[(i,n-i) for n in range(4) for i in range(n,-1,-1)]
bidx={mm:i for i,mm in enumerate(basis)};assert len(basis)==10
base=[];base_labels=[]
def vector(po,shift=(0,0)):
 row=[wzero for _ in basis]
 for mm,cc in po.items():row[bidx[(mm[0]+shift[0],mm[1]+shift[1])]]+=cc
 return row
for name in ['mean_qF','E1','EBe']:
 for shift in [(0,0),(1,0),(0,1)]:
  base.append(vector(polys[name],shift));base_labels.append(dict(original=name,multiplier=list(shift)))
assert len(base)==9
say(stage='W_lambda_three_halves_global_original_ten_column_input',
 entireLambdaFiber=True,noA143Inverse=True,noNewGeometryHeadInverse=True,
 fixedColumns=[list(mm) for mm in basis],baseRows=base_labels,
 allOriginalNormalizedRowTracesActuallyReturned=True,inputProfiles=input_profiles,
 originalPaidDenominatorCount=len(denchecked),claimExcluded=False)
def constant_cofactor(rows):
 # Solve the transposed system with exact polynomial fraction-free elimination.
 # Back substitution is scaled by the actual determinant, so its output is
 # a polynomial adjugate row, valid even where any intermediate pivot vanishes.
 n=len(rows);assert n==10 and all(len(r)==n for r in rows)
 aa=[[rows[j][i] for j in range(n)]+[wone if i==0 else wzero] for i in range(n)]
 prev=wone;sgn=1
 for j in range(n-1):
  h=next((i for i in range(j,n) if aa[i][j]),None)
  if h is None:return None
  if h!=j:aa[h],aa[j]=aa[j],aa[h];sgn=-sgn
  pv=aa[j][j]
  for i in range(j+1,n):
   for c0 in range(j+1,n+1):
    num=pv*aa[i][c0]-aa[i][j]*aa[j][c0]
    nxt=num/prev;assert nxt*prev==num;aa[i][c0]=nxt
   aa[i][j]=wzero
  prev=pv
 det=sgn*aa[-1][n-1]
 if not det:return None
 out=[wzero for _ in range(n)]
 for i in range(n-1,-1,-1):
  num=aa[i][n]*det-sum((aa[i][j]*out[j] for j in range(i+1,n)),wzero)
  out[i]=num/aa[i][i];assert out[i]*aa[i][i]==num
 assert all(sum((out[i]*rows[i][j] for i in range(n)),wzero)==(det if j==0 else wzero) for j in range(n))
 return det,out
def build_one(name):
 begin=time.perf_counter();rows=base+[vector(polys[name])]
 result=constant_cofactor(rows)
 if result is None:
  rec=dict(name=name,zeroDeterminant=True,allLeadingZeroFibersRetained=True,
           cofactorSeconds=time.perf_counter()-begin)
  say(stage='W_lambda_three_halves_global_original_ten_column_cofactor',**rec)
  return None
 det,cof=result
 say(stage='W_lambda_three_halves_global_original_ten_column_product_verified',name=name,allTenOriginalConstantColumnsActuallyReturned=True,rawCofactor=prof(det),cofactorSeconds=time.perf_counter()-begin)
 remaining=det;removed=wone;parts=[]
 for unitname,atom in zip(names,unitpolys):
  count=0
  while True:
   g=remaining.gcd(atom)
   if g.total_degree()==0:break
   nxt=remaining/g;assert nxt*g==remaining;remaining=nxt;removed*=g;count+=1
  if count:parts.append(dict(paidUnit=unitname,passes=count))
 lc=remaining.coefficient(0);remaining=remaining/lc;removed*=lc
 assert removed*remaining==det
 say(stage='W_lambda_three_halves_global_original_weight_curve_complete',name=name,paidRemoved=parts,remainingNecessaryWeightPolynomial=prof(remaining,True),fullOriginalCofactorAndAllStrippingProductsActuallyVerified=True,cofactorSeconds=time.perf_counter()-begin)
 hh=hashlib.sha256();size=0
 for c0 in cof:
  dd=[[list(map(int,mm)),str(cc)] for mm,cc in sorted(c0.to_dict().items())]
  bb=json.dumps(dd,separators=(',',':')).encode();hh.update(bb);hh.update(b'\n');size+=len(bb)+1
 rec=dict(name=name,zeroDeterminant=False,fixedMatrixShape=[10,10],
          allTenOriginalConstantColumnsActuallyReturned=True,
          originalRawCofactor=prof(det),paidRemoved=parts,
          remainingNecessaryWeightPolynomial=prof(remaining,True),
          completeOriginalAdjugateCertificate=dict(bytes=size,sha256=hh.hexdigest()),
          noUnpaidPivotOrContentRemoved=True,allLeadingZeroFibersRetained=True,
          cofactorSeconds=time.perf_counter()-begin)
 say(stage='W_lambda_three_halves_global_original_ten_column_cofactor',**rec)
 return remaining
if __name__=='__main__':
 final={}
 for name in ['N1','NS','PS','original_value_rT']:
  out=build_one(name);final[name]=None if out is None else prof(out)
 say(stage='W_lambda_three_halves_global_original_ten_column_complete',
     sourceSHA256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
     allFourFixedOriginalCofactorsProcessed=True,remainingProfiles=final,
     allActualCofactorsAreGlobalOnCurrentLambdaFiber=True,
     noA143OrAhatInverse=True,noPhysicalDOrNormInverse=True,
     noFiniteCandidateOrExclusionClaim=True,wholeLambdaFiberExcluded=False,
     largeMatrixCachesWritten=False,peakRssKiB=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)
 signal.alarm(0)
