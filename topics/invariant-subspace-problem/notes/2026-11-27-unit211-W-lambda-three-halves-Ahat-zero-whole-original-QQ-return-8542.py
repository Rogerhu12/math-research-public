#!/usr/bin/env python3
"""Entire current W, lambda=3/2, Ahat=4e(k+1)+3(k+2)=0.
New original monic T2, same-T first degree moment return, full finite QQ
original Gram and individual N/P matrices.  No new weight/geometry pivot
is discarded.  Self-contained; 180 seconds / 4 GiB."""
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
e,k,x0,x1,t,unused,zeta=map(R,ctx.gens()[:7]);e=-3*(k+2)/(4*(k+1));u=e+1;Q=e*k;Vbar=(e+1)*k+2;l=(e+1)*((k+2)**2-2*e*k)/(k*Vbar);Delta=1-Q
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

# New whole Ahat-zero original value reduction. No prior value cover is rerun.
from flint import fmpq_poly
assert lam==fmpq(3,2) and 4*e*(k+1)+3*(k+2)==0
assert 4*u*Q-J==0
m=u-l;dw=1-Q;M=l*l*dw-m*m
D0=3*M/(4*u*dw);tauT=l*A2-D0;qT2=T*T-tauT
K=l*l*B3-3*l*T*A2+2*T**3
K0=l*l*B3;K1=-l*A2-2*D0;Kshort=K0+K1*T
assert K-Kshort==2*T*qT2
ss=(l*zeta-T)/u;vv0=(T+m*ss)/l
qval=M*ss*ss-(l*A2-T*T)
Sval=2*vv0+3-2*lam
Nf=(3-4*lam)*Q-J*zvalue.a+Sval*(2*u*Q*v1+zeta*J)
EDelta=Phi*Nf-Sval*zeta*Pf
assert EDelta/Phi==-3*Q+J*dw*ss*ss
assert -4*u*dw*qT2==M*EDelta/(Phi*Q)-4*u*dw*qval
Vval=[E(1),E(lam-1-T),hh,kk]
vv2=tau(vm(Vval,Vval))-E(2*lam*lam)
vv3=tau(vm(vm(Vval,Vval),Vval))-E(4*lam**3)
assert not vv2.b and not vv3.b
H3=K-2*m*(l*A2-T*T)*ss
assert qval==l*vv2.a
assert H3==l*(2*m*ss+3*l+3*T)*vv2.a-l*l*vv3.a
R6=M*K*K-4*m*m*(l*A2-T*T)**3
assert R6==M*(K+2*m*(l*A2-T*T)*ss)*H3+4*m*m*(l*A2-T*T)**2*qval
R0=M*(K0*K0+K1*K1*tauT)-4*m*m*D0**3
R1=2*M*K0*K1;linT=R0+R1*T
trace=M*(4*T*Kshort+4*T*T*qT2+K1*K1)+4*m*m*(3*D0*D0-3*D0*qT2+qT2*qT2)
assert R6==linT+qT2*trace
norm=R0*R0-tauT*R1*R1
assert norm==R1*R1*qT2-linT*(R1*T-R0) and norm
# Every original value must use this same s; D0 is an actual paid weight unit.
srec=Kshort/(2*m*D0);vrec=(T+m*srec)/l
hrec=E(1+vrec,-srec);krec=hrec.conj()
Vrec=[E(1),E(lam-1-T),hrec,krec]
Nh=N4(rows[2])-E(2*lam*P02)*hrec*hrec
Nk=N4(rows[3])-E(2*lam*P02)*krec*krec
Ph=P2(rows[2])-E(P02)*hrec**3
Pk=P2(rows[3])-E(P02)*krec**3
assert Nk==Nh.conj() and Pk==Ph.conj()
NV=N4(Vrec);assert not NV.b
inputs=[('E1',E1.a),('EBe',EB.a),('EBo',EB.b),('N1',NH.a),
 ('NS',NS.a),('PS',PS.a),('original_T2',qT2),('original_T_linear',linT),
 ('individual_N_even',Nh.a),('individual_N_odd',Nh.b),
 ('individual_P_even',Ph.a),('individual_P_odd',Ph.b),('original_N4_V',NV.a)]
atoms=[e,k,u,Q,dw,Vbar,l,m,M,Phi,P02,bc,2*e+1,k+1,k+2,k+4,T0,J-Q]
names=['e','k','u','Q','d','V','ell','m','M','Phi','P02','bc','2e+1','k+1','k+2','k+4','T0','J-Q']
def unipoly(po):
 data={}
 for mm,cf in po.to_dict().items():
  assert all(mm[j]==0 for j in range(8) if j!=1)
  data[int(mm[1])]=cf
 return fmpq_poly([data.get(j,0) for j in range(max(data,default=-1)+1)])
def scalarR(v):
 v=R(v);return unipoly(v.n),unipoly(v.d)
atoms_uni=[scalarR(a)[0] for a in atoms]
assert all(atoms_uni)
paid_denoms=set()
def checkden(den):
 key=str(den)
 if key in paid_denoms:return
 rem=den
 for ap in atoms_uni:
  while True:
   g=rem.gcd(ap)
   if g.degree()<=0:break
   quo,r=divmod(rem,g);assert not r and quo*g==rem;rem=quo
 assert rem.degree()<=0,'unpaid original scalar denominator'
 paid_denoms.add(key)
def pprofile(p):
 coeff=[str(c) for c in p];bb=json.dumps(coeff,separators=(',',':')).encode()
 r=dict(degree=int(p.degree()),bytes=len(bb),sha256=hashlib.sha256(bb).hexdigest())
 if len(bb)<=8192:r['coefficients']=coeff
 return r
num,den=scalarR(norm);checkden(den);remaining=num;removed=fmpq_poly([1]);removed_records=[]
for name,ap in zip(names,atoms_uni):
 count=0
 while True:
  g=remaining.gcd(ap)
  if g.degree()<=0:break
  quo,rr=divmod(remaining,g);assert not rr and quo*g==remaining
  remaining=quo;removed*=g;count+=1
 if count:removed_records.append(dict(paidWeight=name,passes=count))
lc=remaining[remaining.degree()];remaining=remaining/lc;removed*=lc
assert removed*remaining==num
content,factors=remaining.factor();prod=fmpq_poly([content])
for ff,mult in factors:prod*=ff**mult
assert prod==remaining
def extract(pp):
 pp=R(pp);den=unipoly(pp.d);checkden(den);groups={}
 for mm,cf in pp.n.to_dict().items():
  assert all(mm[j]==0 for j in [0,3,5,6,7])
  key=(int(mm[2]),int(mm[4]));dic=groups.setdefault(key,{})
  dic[int(mm[1])]=dic.get(int(mm[1]),fmpq(0))+cf
 out={}
 for key,dic in groups.items():
  po=fmpq_poly([dic.get(j,0) for j in range(max(dic,default=-1)+1)])
  if po:out[key]=(po,den)
 # Exact original embedding of each whole polynomial is checked.
 def back(po):
  ans=ctx.constant(0)
  for j,c0 in enumerate(po):ans+=c0*kp**j
  return ans
 restored=R()
 for mm,(nn,dd) in out.items():restored+=R(back(nn),back(dd))*Fcoord**mm[0]*Scoord**mm[1]
 assert restored==pp
 return out
original=[(name,extract(pp)) for name,pp in inputs]
say(stage='W_lambda_three_halves_Ahat_zero_original_finite_QQ_cover',
 originalMonicT2DeltaSecondMomentTraceActuallyVerified=True,
 originalThirdMomentAndR6FullTracesActuallyVerified=True,
 sameTLinearRemainderAndNormCombinationActuallyVerified=True,
 sameSReconstructionUsesOnlyPaidD0=True,
 originalWholeGramAndIndividualNPEmbeddingsActuallyVerified=True,
 rawNumerator=pprofile(num),paidRemoved=removed_records,
 entireRemainingKCover=pprofile(remaining),
 completeQQFactorization=[dict(factor=pprofile(ff),multiplicity=int(mm)) for ff,mm in factors],
 noR1OrNormInverse=True,allR1ZeroFibersRetained=True,
 distinctOriginalPaidDenominators=len(paid_denoms),claimExcluded=False)
# Fixed total degree 4 in the two actual geometric symbols F,S.
basis=[(i,j) for tdeg in range(5) for i in range(tdeg,-1,-1) for j in [tdeg-i]]
bidx={mm:i for i,mm in enumerate(basis)}
unreturned=[];completed=[]
for fi,(modulus,multiplicity) in enumerate(factors):
 begin=time.perf_counter();inverses=[0]
 def reduce(p):return p%modulus
 class A:
  def __init__(self,v=0):
   self.p=reduce(v.p if isinstance(v,A) else v if isinstance(v,fmpq_poly) else fmpq_poly([v]))
  def __bool__(self):return bool(self.p)
  def __neg__(self):return A(-self.p)
  def __add__(self,v):return A(self.p+A(v).p)
  __radd__=__add__
  def __sub__(self,v):return self+-A(v)
  def __rsub__(self,v):return A(v)+-self
  def __mul__(self,v):return A(self.p*A(v).p)
  __rmul__=__mul__
  def inv(self):
   assert self
   gg,ss0,tt0=self.p.xgcd(modulus)
   assert self.p*ss0+modulus*tt0==gg and gg.degree()==0 and gg[0]
   out=A(ss0/gg[0]);assert self*out==1;inverses[0]+=1;return out
  def __truediv__(self,v):return self*A(v).inv()
  def __eq__(self,v):return self.p==A(v).p
  def data(self):return [str(c) for c in self.p]
 # Paid weights are returned as actual inverses in the entire QQ factor field.
 for ap in atoms_uni:assert A(ap)*A(ap).inv()==1
 field_inputs=[]
 for name,pol in original:
  converted={}
  for mm,(nn,dd) in pol.items():
   v=A(nn)/A(dd)
   if v:converted[mm]=v
  field_inputs.append((name,converted))
 mat=[];rowlabels=[]
 for name,pol in field_inputs:
  if not pol:continue
  degree=max(sum(mm) for mm in pol);assert degree<=4
  for td in range(5-degree):
   for ii in range(td,-1,-1):
    shift=(ii,td-ii);row=[A() for _ in basis]
    for mm,cc in pol.items():
     out=(mm[0]+shift[0],mm[1]+shift[1]);row[bidx[out]]+=cc
    mat.append(row);rowlabels.append(dict(original=name,multiplier=list(shift)))
 nrow=len(mat);piv={}
 for i0,origrow in enumerate(mat):
  row=origrow[:];comb=[A() for _ in range(nrow)];comb[i0]=A(1)
  for jj in sorted(piv):
   if row[jj]:
    fac=row[jj];rr,cc=piv[jj]
    row=[row[h]-fac*rr[h] for h in range(15)]
    comb=[comb[h]-fac*cc[h] for h in range(nrow)]
  j0=next((j for j in range(15) if row[j]),None)
  if j0 is None:continue
  inv=row[j0].inv();row=[x*inv for x in row];comb=[x*inv for x in comb]
  piv[j0]=(row,comb)
  if len(piv)==15:break
 target=[A(1)]+[A() for _ in range(14)];comb=[A() for _ in range(nrow)]
 for jj in sorted(piv):
  if target[jj]:
   fac=target[jj];rr,cc=piv[jj]
   target=[target[h]-fac*rr[h] for h in range(15)]
   comb=[comb[h]+fac*cc[h] for h in range(nrow)]
 unit=not any(target);certificate=None
 if unit:
  product=[sum((comb[i]*mat[i][j] for i in range(nrow)),A()) for j in range(15)]
  assert product==[A(1)]+[A() for _ in range(14)]
  data=dict(factor=[str(c) for c in modulus],basis=[list(mm) for mm in basis],rows=rowlabels,
            originalUnitCombination=[dict(row=i,coefficient=c.data()) for i,c in enumerate(comb) if c])
  bb=json.dumps(data,separators=(',',':')).encode()
  certificate=dict(bytes=len(bb),sha256=hashlib.sha256(bb).hexdigest())
 rec=dict(factorIndex=fi,factor=pprofile(modulus),multiplicity=int(multiplicity),
          QQDimension=int(modulus.degree()),matrixShape=[nrow,15],rank=len(piv),
          originalOneActuallyReturnedAll15Columns=unit,trueInverseCount=inverses[0],
          certificate=certificate,fieldSeconds=time.perf_counter()-begin)
 if unit:completed.append(rec)
 else:unreturned.append(rec)
 say(stage='W_lambda_three_halves_Ahat_zero_whole_QQ_factor_original_return',**rec)
say(stage='W_lambda_three_halves_Ahat_zero_complete',
 sourceSHA256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
 allQQFactorsProcessed=True,completedFactors=len(completed),unreturned=unreturned,
 wholeOriginalAhatZeroFiberExcluded=not unreturned,
 noPhysicalDOrNormInverse=True,originalD0IsPreviouslyPaidWeightUnit=True,
 fullOriginalIndividualNPIncluded=True,largeMatrixCachesWritten=False,
 peakRssKiB=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)
signal.alarm(0)
if unreturned:raise SystemExit(2)
