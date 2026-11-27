#!/usr/bin/env python3
"""R150 centered physical F=2f-u*lambda, S=T-2lambda original structure.
Reconstruct the entire original Gram by a globally paid affine inverse.
Build original two-mean combinations and test the actual N1/E1 cancellation
of S^2 using only physical parameter units. No old cofactor or GB is run.
180 seconds / 4 GiB. All remaining coefficient-zero faces are retained.
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
Fcoord,Lcoord,Scoord=map(R,(Lp,Tp,fp))
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

M=l*(2*u-l*Q)-u*u
units=[('e',ep),('k',kp),('u',ep+1),('distinct_p_q',ep*kp-1),('W_paid_leading',ep*kp+kp+2),('Phi',kp+4),('P02',P02.n),('bc',M.n)]
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
 say({'stage':'new_W0_original_X_Gram_coordinates','name':name,'degrees':list(map(int,po.degrees())),'terms':len(po.to_dict()),'paidRemoved':hist,'totalDegreeXYt':deg,'originalE0N0P1AndMeanReconstructionVerified':True,'claimExcluded':False})

Hpaid=4*ep*kp-kp*kp-4*kp-8
base_units=units+[('previous_k_minus_one',kp+1),('previous_complete_H_zero',Hpaid)]
def strip_known(po):
 initial=po;paid=oo;history=[]
 for name,atom in base_units:
  count=0
  while po:
   gg=po.gcd(atom)
   if gg.total_degree()==0:break
   quotient=po/gg;assert quotient*gg==po
   po=quotient;paid*=gg;count+=1
  if count:history.append([name,count])
 assert po*paid==initial
 return po,paid,history
def paid_denominator(rr):
 rem,paid,hist=strip_known(R(rr).d)
 return rem.total_degree()==0
def coefficient_map(rr):
 rr=R(rr);ans={}
 assert all(all(mm[j]==0 for j in range(2,8)) for mm in rr.d.to_dict())
 for mm,cc in rr.n.to_dict().items():
  assert mm[5]==mm[6]==mm[7]==0
  mon=tuple(map(int,mm[2:5]))
  ans[mon]=ans.get(mon,zz)+cc*ep**int(mm[0])*kp**int(mm[1])
 return {mon:R(pp,rr.d) for mon,pp in ans.items() if pp}
def profile(po):
 if not po:return dict(zero=True)
 sc,fac=po.factor();back=ctx.constant(sc);facts=[]
 for ff,mul in fac:
  back*=ff**int(mul);dd=ff.to_dict()
  assert all(all(mm[j]==0 for j in range(2,8)) for mm in dd)
  rec=dict(degrees=list(map(int,ff.degrees()[:2])),terms=len(dd),multiplicity=int(mul),sha256=hashlib.sha256(str(ff).encode()).hexdigest())
  if len(dd)<=40:rec['coefficients_e_k']=[[int(mm[0]),int(mm[1]),str(cc)] for mm,cc in dd.items()]
  facts.append(rec)
 assert back==po
 return dict(content=str(sc),factors=facts,allFactorProductsMultipliedBack=True)
def report_row(name,rr):
 rr=R(rr);assert paid_denominator(rr)
 primitive,paid,hist=strip_known(rr.n)
 normalized=R(primitive)
 scale=R(rr.d,paid);assert scale*rr==normalized and paid_denominator(scale) and paid_denominator(1/scale)
 cm=coefficient_map(normalized)
 coeffs=[]
 for mon,cf in sorted(cm.items(),reverse=True):
  assert paid_denominator(cf)
  unpaid,paid_cf,hist_cf=strip_known(cf.n)
  coeffs.append(dict(monomial=mon,parameterDegrees=list(map(int,cf.n.degrees()[:2])),paidRemoved=hist_cf,unpaidFactorization=profile(unpaid)))
 say(stage='new_centered_physical_original_row',name=name,totalCoordinateDegree=max((sum(mon) for mon in cm),default=-1),support=list(cm),Sdegree=max((mon[2] for mon in cm),default=-1),lambdaDegree=max((mon[1] for mon in cm),default=-1),Fdegree=max((mon[0] for mon in cm),default=-1),coefficients=coeffs,onlyPreviouslyPaidRowNormalization=True,allOriginalScaleProductsVerified=True,claimExcluded=False)
 return normalized,scale

Eraw=symbolic['E1'];Nraw=symbolic['N1'];Braw=symbolic['EBe'];Oraw=symbolic['EBo']
dpar=1-Q;nu=(u-l*Q)/u
Rt=u*(Oraw+nu*Braw/dpar)/(2*bc)
Ry=-Braw+l*Rt/2
assert Braw==-Ry+l*Rt/2
assert Oraw==2*bc*Rt/u-nu*Braw/dpar
assert paid_denominator(Rt) and paid_denominator(Ry)
cmE=coefficient_map(Eraw);cmN=coefficient_map(Nraw)
eS2=cmE.get((0,0,2),R());nS2=cmN.get((0,0,2),R())
assert eS2
ratio=nS2/eS2
assert ratio*eS2==nS2
global_cancellation=paid_denominator(ratio)
say(stage='new_centered_original_N1_E1_S2_ratio',globallyPaidDenominator=global_cancellation,numeratorFactorization=profile(ratio.n),denominatorUnpaidFactorization=profile(strip_known(ratio.d)[0]),actualCoefficientRatioProductVerified=True,claimExcluded=False)
rows=[('E1',Eraw),('Ry_original_mean_combination',Ry),('Rt_original_mean_combination',Rt)]
if global_cancellation:
 RN=Nraw-ratio*Eraw
 assert RN+ratio*Eraw==Nraw
 assert not coefficient_map(RN).get((0,0,2),R())
 rows.append(('N1_minus_paid_ratio_E1',RN))
else:
 rows.append(('N1_original_unmodified',Nraw))
normalized=[]
for name,rr in rows:normalized.append(report_row(name,rr)[0])
axis=[]
for name,rr in rows:
 cf=coefficient_map(rr).get((0,2,0),R())
 assert paid_denominator(cf)
 unpaid,paid,hist=strip_known(cf.n)
 axis.append(dict(name=name,zero=not bool(cf),paidRemoved=hist,unpaidFactorization=profile(unpaid)))
say(stage='new_centered_original_lambda_axis_coefficients',center=['F=2*f-u*lambda','S=T-2*lambda'],rows=axis,allOriginalCoefficientsExactlyExtracted=True,entireAxisZeroAlreadyClassifiedByPreviousHighestTheorem=True,noSingleAxisCoefficientInverted=True,claimExcluded=False)
signal.alarm(0)
say(stage='new_centered_physical_original_low_structure_complete',wholeOriginalAffineInverseVerified=True,wholeOriginalGramE0N0P1AndWeightedNPVerified=True,globalOriginalS2Cancellation=global_cancellation,allFourReturnedRowsOriginalIdealEquivalent=True,onlyPhysicalUnitsUsed=True,allCoefficientZeroFacesRetained=True,noOldParameterCofactorExpansion=True,sourceSHA256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),peakRssKiB=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss,claimExcluded=False)
