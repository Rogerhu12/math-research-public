#!/usr/bin/env python3
"""R150 general LS, original two-line determinant zero: global monic value
quadratic and three original linear returns, with no ell/T/equal-weight division.
All reductions are multiplied back; four original Gram quadratics give further
necessary parameter minors. This is a reduction certificate, not exclusion.
"""
import json,time,os,sys,hashlib,subprocess,shutil,tempfile,resource
from pathlib import Path
from flint import fmpq,fmpq_mpoly_ctx
import signal
signal.alarm(240)
resource.setrlimit(resource.RLIMIT_AS,(4*1024**3,4*1024**3))
start=time.perf_counter()
def say(x):x['seconds']=time.perf_counter()-start;print(json.dumps(x),flush=True)
ctx=fmpq_mpoly_ctx.get(('l','u','Q','lam','f','t','eta0','z0'),'lex');lp,up,Qp,Lp,fp,tp,eta0p,z0p=ctx.gens();zz=ctx.constant(0);oo=ctx.constant(1)
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
l,u,Q,lam,f,t=map(R,ctx.gens()[:6]);eta0=R(eta0p);z0=R(z0p);Delta=1-Q
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
W1=E(T0/2+2*u*f);W2=E(u*T0+lam*P02+(V2+2*u*u)*f-bc*Q*t)
X=ivbp*(q*W1-W2);Y=ivcq*(W2-p*W1)
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



# The general prefix above precedes every S0 specialization in its source.
v0c=va(rows[0],vs(-tau(rows[0]),one))
assert tau(vm(vm(v0c,v0c),v0c))==E(P02)
assert N4(rows[0])==E(2*lam*P02)
T=R(eta0p);zeta=R(z0p);v1=(T-l*zeta)/u;v0=v1+zeta
hh=E(1+v0,v1);kk=hh.conj();ww=lam-1-T;VV=[E(1),E(ww),hh,kk]
assert b*(hh-1)+c*(kk-1)==T and tau(VV)==E(lam)
assert q*(hh-1)-p*(kk-1)==E(0,-2*zeta)
A2=2*lam*lam-2*lam+1;B3=4*lam**3-6*lam*lam+3*lam-1;M=l*V2-u*u
assert M==4*bc*(1-Q)
z=v0*v0-(1-Q)*v1*v1;S=2*v0+3-2*lam;D=l*A2-T*T
HA=l*M*zeta*zeta-2*T*M*zeta+V2*T*T-u*u*A2
znum=Q*T*T+2*T*(u-l*Q)*zeta-M*zeta*zeta
assert z*u*u==znum
HB=-T*M*zeta*zeta+(2*T*T*(u-l*Q)-2*u*A2*(u-l))*zeta+Q*T**3-2*u*A2*T+u*u*B3
assert HB==u*u*(B3-2*v0*A2+z*T)
assert tau(vm(VV,VV))-E(2*lam*lam)==E(HA/(u*u))
assert tau(vm(VV,vm(VV,VV)))-E(4*lam**3)==E(((3+2*v0)*HA-HB)/(u*u))
assert E(D+l*HA/(u*u))==E(bc)*(hh-kk)**2
HL=-2*(u-l)*D*zeta+2*T**3-(2*l+u)*A2*T+l*u*B3
assert l*HB+T*HA==u*HL
J=2*u*(1-u)+l*Q;Phi=T0+4*u-4+Q;Pf=T0*(J-Q);Pt=bc*Q*Phi
G=lam*P02-(1-u)*T0;Pc=Q*P02*(l+T)-G*T0
PV=Pj-3*E(ww*P02)
assert PV.a*Q==3*(Pf*f+Pt*t+Pc) and not PV.b
NF=(3-4*lam)*Q-z*J+S*(2*u*Q*v1+zeta*J)
NT=bc*Q*S*zeta
R1=u*(3-2*lam+v0+v1)-l*Q*v1
NC=G*(z-S*zeta)+S*Q*T0*v1/2+Q*ww*R1
NV=N4(VV);assert not NV.b
DIFF=NV.a*Q/2-(NF*f+NT*t+NC)
assert DIFF.n%HA.n==0
trace=R(DIFF.n/HA.n,DIFF.d)*R(HA.d);assert DIFF==trace*HA
assert trace==-Q*f/(u*u)
say({'stage':'generic_zeta_global_original_return','meanMomentIdentities':3,'varianceIdentity':True,'LIdentity':True,'thirdMomentLinearCombination':True,'P1Identity':True,'originalNVIdentityModuloOriginalMomentHA':True,'NVTrace':str(trace.n)+' / '+str(trace.d),'extraPhysicalUnitsUsed':['u'],'claimExcluded':False})
DE=Phi*NF-S*zeta*Pf;CO=Phi*NC-S*zeta*Pc
assert Phi*(NF*f+NT*t+NC)-S*zeta*(Pf*f+Pt*t+Pc)==DE*f+CO

# Only the already-paid physical factors occur in rational denominators.
unit_atoms=[('u',up),('u-1',up-1),('pq',Qp),('distinct_p_q',1-Qp),('bc',M.n),('P02',P02.n),('Phi_on_original_Delta0',Phi.n),('nonzero_lambda',Lp),('Hankel_D',D.n)]
unit_checks=set()
def paid_denominator(rr):
 rr=R(rr);p=rr.d;key=str(p)
 if key in unit_checks:return
 unit_checks.add(key)
 for name,atom in unit_atoms:
  while p:
   gg=p.gcd(atom)
   if gg.total_degree()==0:break
   q=p/gg;assert q*gg==p;p=q
 assert p.total_degree()==0,('unpaid denominator',str(rr.d),str(p))
for obj in [b,c,a,p,q,hh,kk]+[x for row in rows for x in row]+d+DK(d):
 for rr in [obj.a,obj.b]:paid_denominator(rr)
for rr in [l,u,Q,lam,f,t,T,zeta,v0,v1,HA,HB,HL,DE,CO,NF,NT,NC,Pf,Pt,Pc,DIFF,trace]:paid_denominator(rr)

# This is an equality of the two original moment ideals in the paid localization.
QM=(A2*HA+T*HB)/(M*D)
sn=l*B3-A2*T;zn=T*B3-A2*A2
assert QM==zeta*zeta-2*T*(u-l*Q)*zeta/M-Q*T*T/M+u*u*zn/(M*D)
assert HA==l*M*QM-u*T*HL/D
assert HB==-T*M*QM+u*A2*HL/D
sbar=sn/D;zbar=zn/D;vbar=sbar/2;Sbar=sbar+3-2*lam
vtrace=-HL/(2*u*D);ztrace=-M*QM/(u*u)
assert v0-vbar==vtrace and z-zbar==ztrace
W=(Phi*(J-2*u*Q)-Pf)/2
Wexplicit=l*u*Q*Q+2*l*u*Q-2*l*Q+2*u**3*Q-4*u**3-8*u*u*Q+8*u*u-u*Q*Q+6*u*Q-4*u
assert W==Wexplicit
Dline=Phi*((3-4*lam)*Q-J*zbar+u*Q*Sbar*sbar)+2*Sbar*W*zeta
Dtrace=Phi*J*M*QM/(u*u)+vtrace*(2*u*Q*Phi*(2*(v0+vbar)+3-2*lam)+4*zeta*W)
assert DE-Dline==Dtrace
Cline=Phi*(G*zbar+Sbar*Q*T0*sbar/4+Q*ww*(u*(3-2*lam)+(u-l*Q/2)*sbar))
Cline+=zeta*(Phi*(-G*Sbar-Sbar*Q*T0/2+Q*ww*(l*Q-u))-Sbar*Pc)
Ctrace=Phi*G*ztrace+vtrace*(Phi*(-2*G*zeta+Q*T0*(2*(v0+vbar)+3-2*lam-2*zeta)/2+Q*ww*(2*u-l*Q))-2*zeta*Pc)
assert CO-Cline==Ctrace
for rr in [QM,Dline,Cline,Dtrace,Ctrace,vtrace,ztrace,W]:paid_denominator(rr)
for rr in [HL,Dline,Cline]:assert rr.n.degrees()[7]<=1
assert QM.n.degrees()[7]==2
qm2=ctx.from_dict({tuple(int(x)-(2 if i==7 else 0) for i,x in enumerate(m)):aa for m,aa in QM.n.to_dict().items() if int(m[7])==2})
assert R(qm2,QM.d)==1
say({'stage':'global_monic_zeta_and_three_original_lines','momentIdealBothDirectionsMultipliedBack':True,'monicQuadraticLeadingCoefficient':1,'leadingCoefficientZeroFibersLost':False,'originalDeltaAndCompatibilityTraceIdentities':2,'newUnpaidInversions':[],'WTerms':len(W.n.to_dict()),'WDegrees':list(map(int,W.n.degrees())),'claimExcluded':False})

# A reduced scalar row is always an original scalar row divided only by paid units.
def strip_paid_poly(pp):
 original=pp;paid=oo;history=[]
 for name,at in unit_atoms:
  count=0
  while pp:
   gg=pp.gcd(at)
   if gg.total_degree()==0:break
   qq=pp/gg;assert qq*gg==pp;pp=qq;paid*=gg;count+=1
  if count:history.append([name,count])
 assert pp*paid==original
 return pp,paid,history

def serialize(pp):return [[list(map(int,m)),str(a)] for m,a in pp.to_dict().items()]
# Keep the four original value rows as well: their coefficients are small.
zeta_raw=[]
for name,rr in [('moment_A',HA),('moment_B',HB),('Delta',DE),('compatibility',CO)]:
 paid_denominator(rr);assert rr.n.degrees()[7]<=2
 zeta_raw.append({'name':name,'poly':serialize(rr.n),'den':serialize(rr.d)})
 say({'stage':'original_value_quadratic','name':name,'degrees':list(map(int,rr.n.degrees())),'terms':len(rr.n.to_dict()),'sha256':hashlib.sha256(str(sorted(rr.n.to_dict().items())).encode()).hexdigest(),'claimExcluded':False})

# P_t is a unit on original Delta=0: N_t=bc*Q*S*zeta is a physical unit,
# and P_t=0 would force P_f=0, already excluded by the whole P1-double-zero theorem.
ts=-(Pf*f+Pc)/Pt
assert Pf*f+Pt*ts+Pc==0;paid_denominator(ts)
f_raw=[]
for name,p0 in [('E1',E1.a),('EBe',EB.a),('EBo',EB.b),('N1',NH.a)]:
 vals=[]
 for j in range(3):
  part=ctx.from_dict({tuple(int(v)-(j if i==5 else 0) for i,v in enumerate(m)):aa for m,aa in p0.n.to_dict().items() if int(m[5])==j});vals.append(part)
 assert sum((vals[j]*tp**j for j in range(3)),zz)==p0.n
 rr=sum((R(vals[j],p0.d)*ts**j for j in range(3)),R());paid_denominator(rr)
 pp,paid,hist=strip_paid_poly(rr.n);assert pp.degrees()[4]<=2 and pp.degrees()[5]==0 and pp.degrees()[7]==0
 f_raw.append({'name':name,'poly':serialize(pp),'den':serialize(rr.d),'paid':serialize(paid)})
 say({'stage':'original_Pt_solved_Gram_quadratic','name':name,'degrees':list(map(int,pp.degrees())),'terms':len(pp.to_dict()),'paidRemoved':hist,'originalSubstitutionMultipliedBack':True,'claimExcluded':False})

pctx=fmpq_mpoly_ctx.get(('l','u','Q','lam','T'),'lex');pl,pu,pQ,pla,pT=pctx.gens();pz=pctx.constant(0);po=pctx.constant(1)
def project_parameter(pp):
 assert all(int(m[4])==int(m[5])==int(m[7])==0 for m in pp.to_dict())
 return pctx.from_dict({tuple(map(int,m[:4]))+(int(m[6]),):aa for m,aa in pp.to_dict().items()})
punits=[(name,project_parameter(at)) for name,at in unit_atoms]
def pstrip(pp):
 original=pp;paid=po;hist=[]
 for name,at in punits:
  cc=0
  while pp:
   gg=pp.gcd(at)
   if gg.total_degree()==0:break
   qq=pp/gg;assert qq*gg==pp;pp=qq;paid*=gg;cc+=1
  if cc:hist.append([name,cc])
 assert pp*paid==original
 return pp,hist

def pprofile(pp):return {'degrees':list(map(int,pp.degrees())),'terms':len(pp.to_dict()),'sha256':hashlib.sha256(str(sorted(pp.to_dict().items())).encode()).hexdigest()}
def scalar_quadratic_minors(data,variable_index,kind):
 import itertools
 mat=[]
 for row in data:
  mat.append([pctx.from_dict({tuple(m[:4]+[m[6]]):fmpq(a) for m,a in row['poly'] if m[variable_index]==j}) for j in [2,1,0]])
 answer=[]
 for inds in itertools.combinations(range(4),3):
  a0,b0,c0=[mat[i] for i in inds]
  cf=[b0[0]*c0[1]-b0[1]*c0[0],a0[1]*c0[0]-a0[0]*c0[1],a0[0]*b0[1]-a0[1]*b0[0]]
  det=sum((cf[i]*mat[inds[i]][2] for i in range(3)),pz)
  for j in [0,1]:assert sum((cf[i]*mat[inds[i]][j] for i in range(3)),pz)==0
  pp,hist=pstrip(det);answer.append({'indices':list(inds),'poly':serialize(pp)})
  say({'stage':'original_three_column_parameter_minor','kind':kind,'rows':list(inds),**pprofile(pp),'paidRemoved':hist,'allThreeCoefficientIdentitiesMultipliedBack':True,'noQuadraticLeadingCoefficientInverted':True,'claimExcluded':False})
 return answer
f_minors=scalar_quadratic_minors(f_raw,4,'four_original_Gram_quadratics')
zeta_minors=scalar_quadratic_minors(zeta_raw,7,'four_original_value_quadratics')

# Three linear rows plus one monic quadratic admit a complete scalar projection.
def zcoef(rr,j):
 pp=ctx.from_dict({tuple(int(x)-(j if i==7 else 0) for i,x in enumerate(m)):aa for m,aa in rr.n.to_dict().items() if int(m[7])==j})
 return R(pp,rr.d)
lin=[(name,zcoef(rr,1),zcoef(rr,0)) for name,rr in [('moment_linear',HL),('Delta_linear',Dline),('compatibility_linear',Cline)]]
for (name,a0,b0),rr in zip(lin,[HL,Dline,Cline]):assert a0*zeta+b0==rr
Bq=zcoef(QM,1);Cq=zcoef(QM,0);assert QM==zeta*zeta+Bq*zeta+Cq
value_complete=[]
import itertools
for i,j in itertools.combinations(range(3),2):
 name,a0,b0=lin[i];name1,a1,b1=lin[j];val=a0*b1-a1*b0
 assert a0*(a1*zeta+b1)-a1*(a0*zeta+b0)==val
 paid_denominator(val);pp,hist=pstrip(project_parameter(val.n));value_complete.append(pp)
 say({'stage':'complete_value_projection_pair_minor','rows':[name,name1],**pprofile(pp),'paidRemoved':hist,'originalLinearCombinationMultipliedBack':True,'claimExcluded':False})
for name,a0,b0 in lin:
 val=b0*b0-a0*Bq*b0+a0*a0*Cq
 assert a0*a0*QM-(a0*zeta+a0*Bq-b0)*(a0*zeta+b0)==val
 paid_denominator(val);pp,hist=pstrip(project_parameter(val.n));value_complete.append(pp)
 say({'stage':'complete_value_projection_monic_quadratic_resultant','row':name,**pprofile(pp),'paidRemoved':hist,'fullPolynomialCombinationMultipliedBack':True,'linearLeadingZeroFibersRetained':True,'claimExcluded':False})
say({'stage':'general_Delta0_complete_value_projection_verified','geometricParameters':['ell','u','Q','lambda','T'],'projectedValueVariable':'zeta','exactValueProjectionGenerators':6,'originalGramNecessaryMinors':4,'originalValueThreeColumnMinorsAlsoChecked':4,'rationalDenominatorsChecked':len(unit_checks),'wholePhiZeroOnDelta0PreviouslyExcluded':True,'fullOriginalNineEquationIdealNotClaimedEquivalentToMinors':True,'sourceSha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'claimExcluded':False})

signal.alarm(0)
say({'stage':'complete','scope':'global original Delta0 value reduction and original necessary Gram minors','wholeDeltaZeroExcluded':False,'ordinaryISPClaim':False,'claimExcluded':False})
