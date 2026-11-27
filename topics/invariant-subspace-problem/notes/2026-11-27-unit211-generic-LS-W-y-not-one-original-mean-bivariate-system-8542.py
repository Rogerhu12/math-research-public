#!/usr/bin/env python3
"""R150 W: new y!=1 exact original mean solved chart.
Full same-point three quadratics/two cubics in (w,Y), with no leading inverse.
R150 W: whole finite Gram y=1 original same-point recovery.
Use the original singleton-mean identity and the original E1 t coefficient
to determine x and t on y=1 using already paid ell and H only.
Return the same original N1, weighted N/P and physical D in two weights.
No multivariate gcd-one emptiness claim. No old cofactor or GB is repeated.
180 seconds / 4 GiB. Self-contained exact original Gram identities.
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
C9paid=4*ep*ep*kp*kp-ep*(kp**4+9*kp**3+20*kp*kp+16*kp)+kp**3+10*kp*kp+24*kp+16
known=units+[('previous_whole_k_minus_one',kp+1),('previous_complete_H_zero',Hpaid),('previous_general_ell_zero',l.n),('previous_general_equal_weights',(l-u).n),('previous_W_u_equals_Q',(u-Q).n),('equal_weights_implied_k_plus_two',kp+2),('previous_whole_C9',C9paid),('previous_whole_u_half',2*ep+1)]
def strip(po):
 initial=po;removed=oo;hist=[]
 for name,atom in known:
  count=0
  while po:
   gg=po.gcd(atom)
   if gg.total_degree()==0:break
   quotient=po/gg;assert quotient*gg==po
   po=quotient;removed*=gg;count+=1
  if count:hist.append([name,count])
 assert po*removed==initial
 return po,removed,hist
def paid_den(rr):return strip(R(rr).d)[0].total_degree()==0
def coeffmap(rr):
 rr=R(rr);outc={}
 assert all(all(mm[j]==0 for j in range(2,8)) for mm in rr.d.to_dict())
 for mm,cc in rr.n.to_dict().items():
  assert mm[5]==mm[6]==mm[7]==0
  mon=tuple(map(int,mm[2:5]))
  outc[mon]=outc.get(mon,zz)+cc*ep**int(mm[0])*kp**int(mm[1])
 return {mon:R(pp,rr.d) for mon,pp in outc.items() if pp}
xx,yy,tt=map(R,(Lp,Tp,fp))
def sub(rr,xv,yv,tv):
 outv=sum((cf*xv**mm[0]*yv**mm[1]*tv**mm[2] for mm,cf in coeffmap(rr).items()),R())
 assert paid_den(outv)
 return outv
def factor_info(po):
 if not po:return dict(zero=True)
 sc,fac=po.factor();back=ctx.constant(sc);facts=[]
 for ff,mul in fac:
  back*=ff**int(mul);dd=ff.to_dict()
  assert all(all(mm[j]==0 for j in range(2,8)) for mm in dd)
  rec=dict(degrees=list(map(int,ff.degrees()[:2])),totalDegree=int(ff.total_degree()),terms=len(dd),multiplicity=int(mul),sha256=hashlib.sha256(str(ff).encode()).hexdigest())
  if len(dd)<=120:rec['coefficients_e_k']=[[int(mm[0]),int(mm[1]),str(cc)] for mm,cc in dd.items()]
  facts.append(rec)
 assert back==po
 return dict(content=str(sc),factors=facts,allFactorProductsMultipliedBack=True)
def param_report(name,rr):
 rr=R(rr);assert paid_den(rr)
 assert all(mm==(0,0,0) for mm in coeffmap(rr))
 rem,paid,hist=strip(rr.n)
 say(stage='new_W_y_one_complete_original_parameter_return',name=name,numeratorDegrees=list(map(int,rr.n.degrees()[:2])),denominatorDegrees=list(map(int,rr.d.degrees()[:2])),paidRemoved=hist,remainingFactorization=factor_info(rem),sha256=hashlib.sha256((str(rr.n)+' / '+str(rr.d)).encode()).hexdigest(),constantNonzero=bool(rem) and rem.total_degree()==0,claimExcluded=False)
 return rem
Nweight=u*(2-2*u-Q)+l*Q*(2*u-1)
assert Nweight==-e*e*u*R(Hpaid)/Vbar
assert paid_den(Nweight) and paid_den(1/Nweight)
meancombo=(u-l)*symbolic['EBe']+l*(1-Q)*symbolic['EBo']
xstar=1+u-u/l
assert paid_den(xstar)
assert sub(meancombo,xx,R(1),tt)==-l*Nweight/u*(xx-xstar)
tc=sum((cf*xx**mm[0]*yy**mm[1] for mm,cf in coeffmap(meancombo).items() if mm[2]==1),R())
assert tc==M*(yy-1)
assert all(mm[2]<=1 for mm in coeffmap(meancombo))
e1=symbolic['E1']
tcE=sum((cf*xx**mm[0]*yy**mm[1] for mm,cf in coeffmap(e1).items() if mm[2]==1),R())
assert tcE==4*bc*(xx-u-1)
assert all(mm[2]<=1 for mm in coeffmap(e1))
pE=sub(e1,xstar,R(1),tt)
alpha=-4*bc*u/l
beta=sub(e1,xstar,R(1),R())
assert pE==alpha*tt+beta
assert paid_den(alpha) and paid_den(1/alpha)
tstar=-beta/alpha
assert paid_den(tstar)
assert not sub(e1,xstar,R(1),tstar)
assert not sub(meancombo,xstar,R(1),tstar)
say(stage='new_W_y_one_original_mean_and_E1_reconstruction',y=1,recoveredX='1+u-u/ell',recoveredT='-E1(xstar,1,0)/(-4bc*u/ell)',fullSingletonMeanCombinationIdentityVerified=True,fullGeneralMeanTcoefficient='M*(y-1)',fullGeneralE1Tcoefficient='4bc*(x-u-1)',allOriginalPaidInverseProductsVerified=True,noUnpaidXMinusUMinusOneInverted=True,claimExcluded=False)

# New mathematical input: solve the complete original singleton mean on y!=1.
# This chart becomes the entire remaining W once the separate y=1 F4 return
# is published complete. No D27 or B239 head, or geometric leading term,
# is divided here.
Yv=R(Tp);wv=R(Lp)
newx=xstar+Yv*wv;newy=1+Yv
beta0=sub(meancombo,newx,newy,R())
newt=-beta0/(M*Yv)
assert paid_den(newt)
assert sub(meancombo,newx,newy,newt)==0
assert beta0==-M*Yv*newt
ct=coeffmap(newt)
assert all(mm[0]<=1 and mm[1]<=1 and mm[2]==0 for mm in ct)
compact_t=2*newx/u-2*(1-Q)*newy/u+2*e/u+T0*l*(1-Q)/(u*M)+l*Nweight*wv/(u*M)
compact_verified=(newt==compact_t)
def smallrr(rr):
 rr=R(rr);b0=(str(rr.n)+' / '+str(rr.d)).encode()
 ans=dict(numeratorDegrees=list(map(int,rr.n.degrees()[:5])),denominatorDegrees=list(map(int,rr.d.degrees()[:5])),numeratorTerms=len(rr.n.to_dict()),bytes=len(b0),sha256=hashlib.sha256(b0).hexdigest())
 if len(b0)<=4096:ans['exactExpression']=b0.decode()
 return ans
say(stage='new_W_y_not_one_complete_original_mean_reconstruction',coordinateDefinitions=dict(Y='y-1',w='(x-xstar)/(y-1)',x='xstar+Y*w',y='1+Y',t='-meancombo(xstar+Y*w,1+Y,0)/(M*Y)'),originalMeanTcoefficient='M*(y-1)',exactYFactorCanceledBeforeAnyGeometricInverse=True,remainingDenominatorsAllPreviouslyPaid=True,newT_Bidegree_w_Y=[max(mm[0] for mm in ct),max(mm[1] for mm in ct)],newTCoefficients=[dict(w=mm[0],Y=mm[1],value=smallrr(cf)) for mm,cf in sorted(ct.items())],compactWorkingFormulaVerified=compact_verified,chartAssumption='y!=1; separate entire y=1 finite theorem is required for global use',D27AndB239NeverInverted=True,claimExcluded=False)
new_rows=[];new_names=['E1','EBe','N1','NS','PS'];scales=[];raw_rows=[]
for name in new_names:
 raw=sub(symbolic[name],newx,newy,newt);assert paid_den(raw)
 pp,paid,hist=strip(raw.n);scale=R(raw.d,paid)
 normalized=R(pp)
 assert normalized==scale*raw and paid_den(scale) and paid_den(1/scale)
 cc=coeffmap(normalized)
 assert all(mm[2]==0 and mm[0]<=(2 if name in ['E1','EBe','N1'] else 3) and mm[1]<=(2 if name in ['E1','EBe','N1'] else 3) for mm in cc)
 new_rows.append(normalized);scales.append(scale);raw_rows.append(raw)
 say(stage='new_W_y_not_one_original_bivariate_row',name=name,summary=smallrr(normalized),degrees_w_Y=[max((mm[0] for mm in cc),default=-1),max((mm[1] for mm in cc),default=-1)],paidRemoved=hist,fullSamePointOriginalSubstitutionVerified=True,allPaidNormalizationProductsVerified=True,claimExcluded=False)
assert sub(symbolic['EBo'],newx,newy,newt)==-(u-l)*raw_rows[1]/(l*(1-Q))
Dnew=sub(symbolic['Dphysical'],newx,newy,newt)
assert paid_den(Dnew)
say(stage='new_W_y_not_one_original_D_unit_return',summary=smallrr(Dnew),identity='Dphysical+ell*HA/u^2=bc*(hU-kU)^2',sameNewCoordinates=True,unitStillRequired=True,claimExcluded=False)
def Ycoeffs(rr,n):
 cc=coeffmap(rr);answer=[R() for _ in range(n+1)]
 for mm,cf in cc.items():
  assert mm[2]==0 and mm[1]<=n
  answer[mm[1]]=answer[mm[1]]+cf*wv**mm[0]
 assert sum((answer[j]*Yv**j for j in range(n+1)),R())==rr
 return answer
C=[Ycoeffs(row,2) for row in new_rows[:3]]
def det2(a0,b0,c0,d0):return a0*d0-b0*c0
cof=[det2(C[1][1],C[1][2],C[2][1],C[2][2]),-det2(C[0][1],C[0][2],C[2][1],C[2][2]),det2(C[0][1],C[0][2],C[1][1],C[1][2])]
delta0=sum((cof[i]*C[i][0] for i in range(3)),R())
for j in range(3):assert sum((cof[i]*C[i][j] for i in range(3)),R())==(delta0 if j==0 else R())
assert sum((cof[i]*new_rows[i] for i in range(3)),R())==delta0
assert sum((cof[i]*scales[i]*raw_rows[i] for i in range(3)),R())==delta0

def bounded_factor_info(pp):
 info=factor_info(pp)
 for fr in info.get('factors',[]):
  data=fr.get('coefficients_e_k')
  if data is None:continue
  enc=json.dumps(data,separators=(',',':')).encode()
  fr['coefficientBytes']=len(enc)
  fr['coefficientSHA256']=hashlib.sha256(enc).hexdigest()
  if len(enc)>8192:
   del fr['coefficients_e_k']
   fr['exactCoefficientsOmittedForOutputCap']=True
 return info

def univariate_w_report(name,rr,identity):
 rr=R(rr);assert paid_den(rr)
 cc=coeffmap(rr);assert all(mm[1]==mm[2]==0 for mm in cc)
 pp,paid,hist=strip(rr.n);assert pp*paid==rr.n
 degw=max((int(mm[2]) for mm in pp.to_dict()),default=-1)
 lc=zz
 for mm,cf in pp.to_dict().items():
  assert all(mm[j]==0 for j in range(3,8))
  if int(mm[2])==degw:lc+=cf*ep**int(mm[0])*kp**int(mm[1])
 leading,removed,lchist=strip(lc)
 ans=dict(name=name,degrees_e_k_w=list(map(int,pp.degrees()[:3])),terms=len(pp.to_dict()),sha256=hashlib.sha256(str(pp).encode()).hexdigest(),paidRemoved=hist,rawLeadingDegrees=list(map(int,lc.degrees()[:2])),leadingPaidRemoved=lchist,remainingLeadingFactorization=bounded_factor_info(leading),originalIdentity=identity,allOriginalProductsMultipliedBack=True,allNewLeadingZeroFibersRetained=True)
 say(stage='new_W_y_not_one_original_parameter_w_constraint',**ans,claimExcluded=False)
 return pp
det_poly=univariate_w_report('three_original_quadratic_coefficient_determinant',delta0,'sum_i cofactor(i,constant)*normalized_original_row_i = determinant')
pair_polys=[]
for ia,ib in [(0,1),(0,2),(1,2)]:
 A0,B0=C[ia],C[ib]
 cross=[det2(A0[1],A0[2],B0[1],B0[2]),det2(A0[2],A0[0],B0[2],B0[0]),det2(A0[0],A0[1],B0[0],B0[1])]
 K0,K1,K2=cross
 # Exact consequences of the same two quadratics; no leading coefficient inverse.
 lin=K0*Yv-K1
 quad=K0*Yv*Yv-K2
 assert lin==B0[2]*new_rows[ia]-A0[2]*new_rows[ib]
 assert quad==A0[1]*new_rows[ib]-B0[1]*new_rows[ia]
 pair=K1*K1-K0*K2
 assert pair==K0*quad-(K0*Yv+K1)*lin
 pp=univariate_w_report('fixed_quadratic_pair_'+new_names[ia]+'_'+new_names[ib],pair,'K1^2-K0*K2 = K0*(K0Y^2-K2)-(K0Y+K1)*(K0Y-K1), each parenthesis is an original pair combination')
 pair_polys.append(pp)
signal.alarm(0)
say(stage='new_W_y_not_one_full_mean_bivariate_system_complete',sourceSHA256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),chartAssumption='y!=1',allOriginalQuadraticsAndNSPSReturned=True,remainingGeometricVariables=['w','Y'],originalRowBidegreeBounds=[[2,2],[2,2],[2,2],[3,3],[3,3]],allExplicitCofactorAndPairProductsVerified=True,noNewGeometricOrParameterLeadingInverse=True,D27AndB239WholeZeroFacesRetained=True,physicalDOriginalUnitRetained=True,newLeadingZeroFibersNotPaid=True,fullOriginalSystemExclusionClaim=False,claimExcluded=False,peakRssKiB=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)
