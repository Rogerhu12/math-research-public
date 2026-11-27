#!/usr/bin/env python3
"""R150 general LS, original two-line determinant zero: global monic value
quadratic and three original linear returns, with no ell/T/equal-weight division.
All reductions are multiplied back; four original Gram quadratics give further
necessary parameter minors. The appended certificate closes the entire u=1/2,Q=2 branch of original Delta=0.
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

# W is affine in ell. Its leading-zero intersection is retained and now closed.
Vleading=up*(Qp+2)-2
assert W.n.resultant(Vleading,'u')==2*Qp**3*(Qp-2)
leadell=ctx.from_dict({tuple(0 if i==0 else int(v) for i,v in enumerate(m)):aa for m,aa in W.n.to_dict().items() if int(m[0])==1})
assert leadell==Qp*Vleading
say({'stage':'whole_W_affine_ell_leading_zero_coverage','WLeadingCoefficient':'Q*(u*(Q+2)-2)','fullResultantU':'2*Q^3*(Q-2)','originalQIsUnit':True,'remainingWholeFiber':'u=1/2,Q=2,ell arbitrary','claimExcluded':False})

# Return all eight original constant-column minors to this entire fiber.
wctx=fmpq_mpoly_ctx.get(('l','lam','T'),'lex');wl,wla,wT=wctx.gens();wo=wctx.constant(1);wz=wctx.constant(0)
wA=2*wla*wla-2*wla+1;wD=wl*wA-wT*wT;wM=wl-2*wl*wl-fmpq(1,4);wP02=-wl-fmpq(1,4);wPhi=fmpq(1,2)-2*wl
wunits=[('Phi',wPhi),('P02',wP02),('Hankel_D',wD),('bc',wM)]
w_minor_polys=[]
for kind,data0 in [('Gram',f_minors),('value',zeta_minors)]:
 for ind,rec in enumerate(data0):
  original=wz
  for m,aa in rec['poly']:original+=fmpq(aa)*wl**m[0]*fmpq(1,2)**m[1]*2**m[2]*wla**m[3]*wT**m[4]
  pp=original;paid=wo;history=[]
  for name,atom in wunits:
   count=0
   while pp:
    gg=pp.gcd(atom)
    if gg.total_degree()==0:break
    q0=pp/gg;assert q0*gg==pp;pp=q0;paid*=gg;count+=1
   if count:history.append([name,count])
  assert pp*paid==original;w_minor_polys.append(pp)
  say({'stage':'whole_half_u_Q2_original_parameter_minor','kind':kind,'index':ind,'degrees':list(map(int,pp.degrees())),'terms':len(pp.to_dict()),'paidRemoved':history,'claimExcluded':False})

from flint import fmpq_poly,nmod_poly,nmod_mpoly_ctx
ell=fmpq_poly([0,1]);one=fmpq_poly([1]);zero=fmpq_poly([])
data=f_raw
ats=[('Phi',1-4*ell),('P02',1+4*ell),('bc',8*ell*ell-4*ell+1)]
mons=sorted([(i,j,k) for i in range(5) for j in range(5-i) for k in range(5-i-j)],key=lambda m:(sum(m),m),reverse=True);mults=sorted([m for m in mons if sum(m)<=2],key=lambda m:(sum(m),m),reverse=True)
assert len(mons)==35 and len(mults)==10 and mons[-1]==(0,0,0)
vctx=fmpq_mpoly_ctx.get(('ell','la','Tv','fv'),'lex');ve,vl,vt,vf=vctx.gens();vz=vctx.constant(0)
def embed_univariate(pp):return sum((aa*ve**i for i,aa in enumerate(pp)),vz)
rows=[];labels=[];original_row_returns=0
for rr in data:
 original_quad=vz
 for m,aa in rr['poly']:original_quad+=fmpq(aa)*fmpq(1,2)**m[1]*2**m[2]*ve**m[0]*vl**m[3]*vt**m[6]*vf**m[4]
 co={}
 for m,a in rr['poly']:
  mo=(m[3],m[6],m[4]);assert sum(mo)<=2 and m[5]==m[7]==0
  aa=fmpq(a)*fmpq(1,2)**m[1]*2**m[2];co[mo]=co.get(mo,zero)+aa*ell**m[0]
 common=zero
 for aa in co.values():common=common.gcd(aa)
 paid=one;hist=[]
 for name,at in ats:
  count=0
  while common:
   g=common.gcd(at)
   if g.degree()==0:break
   common=common/g;paid*=g;count+=1
  if count:hist.append([name,count])
 out={m:aa/paid for m,aa in co.items()}
 assert all(out[m]*paid==co[m] for m in co)
 reconstructed_quad=sum((embed_univariate(aa)*vl**m[0]*vt**m[1]*vf**m[2] for m,aa in out.items()),vz)
 assert reconstructed_quad*embed_univariate(paid)==original_quad
 for mm in mults:
  row=[]
  for mo in mons:
   dif=tuple(mo[i]-mm[i] for i in range(3));row.append(out.get(dif,zero) if min(dif)>=0 else zero)
  reconstructed_row=sum((embed_univariate(aa)*vl**m[0]*vt**m[1]*vf**m[2] for m,aa in zip(mons,row)),vz)
  assert reconstructed_row==reconstructed_quad*vl**mm[0]*vt**mm[1]*vf**mm[2];original_row_returns+=1
  rows.append(row);labels.append([rr['name'],mm])
 say({'stage':'W_leading_zero_original_three_variable_quad','name':rr['name'],'maxEllDegree':max(int(aa.degree()) for aa in out.values()),'terms':sum(len(aa) for aa in out.values()),'paidRemoved':hist,'claimExcluded':False})
assert original_row_returns==40
say({'stage':'all40_original_multiplication_rows_reconstructed','rows':40,'originalThreeVariableQuadratics':4,'allPaidContentProductsAndMonomialRowsMultipliedBack':True,'claimExcluded':False})
AA=[list(row) for row in rows];prev=one;steps=[];chosen=list(range(40))
for z in range(34):
 swap=z
 if not AA[z][z]:
  swap=next(i for i in range(z+1,40) if AA[i][z]);AA[z],AA[swap]=AA[swap],AA[z];chosen[z],chosen[swap]=chosen[swap],chosen[z]
 pivot=AA[z][z];assert pivot;lower=[AA[i][z] for i in range(z+1,40)];steps.append((pivot,lower,swap))
 for i in range(z+1,40):
  for j in range(z+1,35):
   num=AA[i][j]*pivot-AA[i][z]*AA[z][j];qq,rem=divmod(num,prev);assert not rem and qq*prev==num;AA[i][j]=qq
  AA[i][z]=zero
 prev=pivot
 if z%3==0 or z>=30:say({'stage':'W_leading_zero_M35_fraction_free_step','index':z,'swap':swap,'degreeEll':int(pivot.degree()),'claimExcluded':False})

assert all(not AA[i][34] for i in range(34,40))
class R1:
 def __init__(self,n=0,d=None):
  if isinstance(n,R1):self.n=n.n;self.d=n.d;return
  n=n if isinstance(n,fmpq_poly) else fmpq_poly([n]);d=one if d is None else d;assert d
  if not n:self.n=zero;self.d=one;return
  g=n.gcd(d);n=n/g;d=d/g;lc=d[d.degree()];self.n=n/lc;self.d=d/lc
 def __add__(self,o):o=R1(o);return R1(self.n*o.d+o.n*self.d,self.d*o.d)
 __radd__=__add__
 def __neg__(self):return R1(-self.n,self.d)
 def __sub__(self,o):return self+-R1(o)
 def __rsub__(self,o):return R1(o)+-self
 def __mul__(self,o):o=R1(o);return R1(self.n*o.n,self.d*o.d)
 __rmul__=__mul__
 def __truediv__(self,o):o=R1(o);assert o.n;return R1(self.n*o.d,self.d*o.n)
 def __pow__(self,n):return R1(self.n**n,self.d**n)
 def __eq__(self,o):o=R1(o);return self.n*o.d==o.n*self.d
vec=[R1(0)]*35;vec[-1]=R1(1)
for j in range(33,-1,-1):vec[j]=-sum((R1(AA[j][k])*vec[k] for k in range(j+1,35)),R1(0))/R1(AA[j][j])
for row in rows:assert sum((R1(a)*b for a,b in zip(row,vec)),R1(0))==0
vv=[vec[mons.index(m)] for m in [(1,0,0),(0,1,0),(0,0,1)]]

needed=[(1,0,0),(0,1,0),(0,0,1),(2,0,0),(1,1,0),(0,2,0),(1,0,1),(0,1,1),(0,0,2)]
det=steps[-1][0];certs={};checks=[]
for mon in needed:
 target=mons.index(mon);alpha=[R1(0)]*40
 for j in range(34):alpha[j]=(R1(det if j==target else 0)-sum((alpha[i]*R1(AA[i][j]) for i in range(j)),R1(0)))/R1(AA[j][j])
 for z in range(33,-1,-1):
  pivot,lower,swap=steps[z];previous=one if z==0 else steps[z-1][0]
  alpha[z]=alpha[z]-sum((alpha[i]*R1(lower[i-z-1],previous) for i in range(z+1,40)),R1(0))
  for i in range(z+1,40):alpha[i]=alpha[i]*R1(pivot,previous)
  if swap!=z:alpha[z],alpha[swap]=alpha[swap],alpha[z]
 assert all(a.d.degree()==0 for a in alpha)
 cp=[a.n/a.d[0] for a in alpha]
 constant=-R1(det)*vec[target];assert constant.d.degree()==0
 for j in range(35):assert sum((cp[i]*rows[i][j] for i in range(40)),zero)==(det if j==target else constant.n/constant.d[0] if j==34 else zero)
 certs[mon]=cp;say({'stage':'W_leading_zero_original_coordinate_cofactor_return','monomial':mon,'all35CoefficientIdentitiesMultipliedBack':True,'cofactorSHA256':hashlib.sha256('|'.join(str(p) for p in cp).encode()).hexdigest(),'claimExcluded':False})
GG=zero;use=[];identityCount=0
for mon in needed[3:]:
 d=vec[mons.index(mon)]-vv[0]**mon[0]*vv[1]**mon[1]*vv[2]**mon[2]
 if not d.n:continue
 div,rem=divmod(det*det,d.d);assert not rem and div*d.d==det*det
 old=GG;GG,aa,bb=GG.xgcd(d.n);assert aa*old+bb*d.n==GG;identityCount+=1
 use.append({'monomial':mon,'numeratorDegree':int(d.n.degree()),'denominatorDegree':int(d.d.degree()),'gcdDegree':int(GG.degree()),'numeratorSHA256':hashlib.sha256(str(d.n).encode()).hexdigest()});say({'stage':'W_leading_zero_actual_quadratic_consistency_gcd',**use[-1],'actualBezoutMultipliedBack':True,'claimExcluded':False})
sc,fac=det.factor();prod=fmpq_poly([sc]);facts=[]
for p,n in fac:prod*=p**n;facts.append({'degree':int(p.degree()),'multiplicity':int(n),'poly':[str(a) for a in p]})
assert prod==det

assert det.degree()==176 and GG.degree()==37
assert hashlib.sha256(str(GG).encode()).hexdigest()=='a2d35edd555b3de5c0a577bcc5382ac7501360f0a5f75c1a9148b5d109530ae9'
say({'stage':'actual_original_one_variable_QQ_cover','rankMinorDegree':176,'rankFactorDegreesAndMultiplicities':[[int(p.degree()),int(nn)] for p,nn in fac],'quadraticConsistencyDegree':37,'quadraticConsistencySHA256':hashlib.sha256(str(GG).encode()).hexdigest(),'polynomialCoordinateCoefficientReturns':315,'actualQuadraticConsistencyBezoutReturns':6,'allReconstructionDenominatorsDivideRankMinorSquared':True,'allRankMinorZeroFibersRetained':True,'claimExcluded':False})
# Strip only the physical Q=2,u=1/2 factors: Phi, P02, bc.
rank_remaining=det;paid_rank=one;rankhist=[]
for name,atom in ats:
 count=0
 while rank_remaining:
  gg=rank_remaining.gcd(atom)
  if gg.degree()==0:break
  qq,rem=divmod(rank_remaining,gg);assert not rem and qq*gg==rank_remaining
  rank_remaining=qq;paid_rank*=gg;count+=1
 if count:rankhist.append([name,count])
assert rank_remaining*paid_rank==det
assert rankhist==[['Phi',46],['P02',24],['bc',22]]
sc,rkf=rank_remaining.factor();rp=fmpq_poly([sc])
for pp,nn in rkf:rp*=pp**nn
assert rp==rank_remaining
assert sorted((int(pp.degree()),int(nn)) for pp,nn in rkf)==[(1,2),(6,1),(11,1),(11,1),(32,1)]
candidates=[('quadratic_consistency37',GG)]+[(f'rank_{i}_degree{pp.degree()}',pp) for i,(pp,nn) in enumerate(rkf) if pp.degree()>1]
assert sum(int(pp.degree()) for name,pp in candidates)==97
squarefree_cover=2*ell-1
for name,pp in candidates:squarefree_cover*=pp
assert squarefree_cover.degree()==98 and squarefree_cover.gcd(squarefree_cover.derivative()).degree()==0
say({'stage':'actual_QQ_cover_after_physical_factors','physicalFactorRemovals':rankhist,'nonhalfWholeCandidateDegrees':[int(pp.degree()) for name,pp in candidates],'remainingHalfWeightMultiplicity':2,'totalSquarefreeCoverDegree':98,'allFullFactorProductsMultipliedBack':True,'claimExcluded':False})

# In the nonhalf weight chart 2ell-1 is a unit. This only excludes ell=1/2
# temporarily; the complete ell=1/2 return is appended below.
z0=w_minor_polys[4]/(2*wl-1);assert z0*(2*wl-1)==w_minor_polys[4]
Tprojs=[]
for idx in [0,1]:
 pp=w_minor_polys[idx]
 assert int(pp.degrees()[2])==3 and int(z0.degrees()[2])==4
 rr=pp.resultant(z0,'T');assert rr
 assert rr.degrees()[2]==0 and rr.degrees()[1]==12
 Tprojs.append(rr)
 say({'stage':'actual_QQ_full_original_T_resultant','GramMinorIndex':idx,'originalFullTDegrees':[3,4],'degrees':list(map(int,rr.degrees())),'terms':len(rr.to_dict()),'sha256':hashlib.sha256(str(sorted(rr.to_dict().items())).encode()).hexdigest(),'allTLeadingZeroFibersRetained':True,'claimExcluded':False})
prime=1009;modctx=nmod_mpoly_ctx.get(('l','lam'),ordering='lex',modulus=prime)
def rmod(aa):
 aa=fmpq(aa);denominator=int(aa.denominator)%prime;assert denominator
 return int(aa.numerator)%prime*pow(denominator,-1,prime)%prime
modinputs=[]
for pp in Tprojs:
 mm=modctx.from_dict({(int(m[0]),int(m[1])):rmod(aa) for m,aa in pp.to_dict().items()})
 assert int(mm.degrees()[1])==int(pp.degrees()[1])==12;modinputs.append(mm)
modres=modinputs[0].resultant(modinputs[1],'lam');assert modres
cc=[0]*(int(modres.degrees()[0])+1)
for m,aa in modres.to_dict().items():assert int(m[1])==0;cc[int(m[0])]=int(aa)
support=nmod_poly(cc,prime);assert support.degree()==1068
say({'stage':'full_original_lambda_resultant_modular_return','actualQQDefinition':'Res_lambda(Res_T(F0,Z0),Res_T(F1,Z0))','fullLambdaDegreesQQAndMod':[12,12],'prime':prime,'resultantModDegree':support.degree(),'resultantModSHA256':hashlib.sha256(str(support).encode()).hexdigest(),'claimExcluded':False})
for name,pp in candidates:
 lc=pp.leading_coefficient();assert rmod(lc)
 monic=pp/lc;assert monic*lc==pp
 for aa in monic:rmod(aa)
 cc=nmod_poly([rmod(aa) for aa in pp],prime);assert cc.degree()==pp.degree()
 gg,aa,bb=cc.xgcd(support);assert gg==1 and aa*cc+bb*support==1
 say({'stage':'whole_actual_QQ_ell_candidate_return','candidate':name,'candidateDegreeQQAndMod':pp.degree(),'QQLeadingCoefficientMod':rmod(lc),'monicQQCoefficientsPrimeIntegral':True,'coefficientDegrees':[aa.degree(),bb.degree()],'coefficientSHA256':hashlib.sha256((str(aa)+'|'+str(bb)).encode()).hexdigest(),'candidateSHA256':hashlib.sha256(str(pp).encode()).hexdigest(),'bothBezoutProductsMultipliedBack':True,'allComplexEmbeddingsExcluded':True,'claimExcluded':True})

# The remaining rational ell=1/2 fiber uses exact QQ identities only.
hctx=fmpq_mpoly_ctx.get(('lam','T'),'lex');hla,hT=hctx.gens();hz=hctx.constant(0)
def half_specialize(pp):
 rr=hz
 for m,aa in pp.to_dict().items():rr+=aa*fmpq(1,2)**int(m[0])*hla**int(m[1])*hT**int(m[2])
 return rr
def scalar_multiple(actual,expected):
 assert actual and expected
 lc=expected.coefficient(0);scale=actual.coefficient(0)/lc
 assert actual==scale*expected and scale
 return scale
hpolys=[half_specialize(pp) for pp in w_minor_polys]
C=9*hla*hla+36*hla*hT+9*hla+54*hT*hT+33*hT+5
F1=12*hla**3+36*hla*hla*hT+4*hla*hla+24*hla*hT*hT-16*hla*hT-9*hla-42*hT*hT-32*hT-6
F2=6*hla*hla*hT+5*hla*hla+48*hla*hT*hT+40*hla*hT+6*hla+108*hT**3+126*hT*hT+47*hT+6
Z=(2*hT+1)*(3*hla-6*hT-4)*(6*hla*hla-8*hla*hT-14*hla+4*hT*hT+12*hT+9)
for actual,expected in [(hpolys[0],(2*hT+1)*C),(hpolys[1],F1),(hpolys[2],F2),(hpolys[6],Z)]:scalar_multiple(actual,expected)
F2minus=hz
for m,aa in F2.to_dict().items():F2minus+=aa*hla**int(m[0])*fmpq(-1,2)**int(m[1])
assert F2minus==(2*hla-1)**2/2
hD=(2*hla*hla-2*hla+1)/2-hT*hT
assert sum((aa*fmpq(1,2)**int(m[0])*fmpq(-1,2)**int(m[1]) for m,aa in hD.to_dict().items()),fmpq(0))==0
say({'stage':'whole_ellhalf_Tminus_half_original_return','TValue':'-1/2','originalF2':'(2lambda-1)^2/2','forcedLambda':'1/2','contradiction':'original Hankel D=0','allExactSpecializationsMultipliedBack':True,'claimExcluded':True})
R1p=C.resultant(F1,'T');R2p=C.resultant(F2,'T');Zp=C.resultant(Z,'T')
C5=432*hla**5-288*hla**4-186*hla**3+108*hla*hla+40*hla-19
assert R1p==162*hla*C5 and R2p==972*(3*hla-1)*C5
assert Zp==576*(27*hla-14)*(10368*hla**3-26496*hla*hla+22065*hla-5929)*(3*hla-2)**2*(3*hla-1)**2
assert R1p*(-3)/162+R2p/972==-C5

def as_qq_poly(pp):
 vals=[fmpq(0)]*(int(pp.degrees()[0])+1)
 for m,aa in pp.to_dict().items():assert int(m[1])==0;vals[int(m[0])]=aa
 return fmpq_poly(vals)
c5=as_qq_poly(C5);zs=as_qq_poly(Zp);gg,aa,bb=c5.xgcd(zs)
assert gg==1 and aa*c5+bb*zs==1
say({'stage':'whole_ellhalf_original_quintic_QQ_return','firstOriginalTDegrees':[2,2],'secondOriginalTDegrees':[2,3],'supportOriginalTDegrees':[2,4],'QQCandidateDegree':5,'QQSupportDegree':zs.degree(),'candidateDerivedByExactOriginalResultantCombination':True,'coefficientDegrees':[aa.degree(),bb.degree()],'coefficientSHA256':hashlib.sha256((str(aa)+'|'+str(bb)).encode()).hexdigest(),'bothQQBezoutProductsMultipliedBack':True,'allComplexRootsExcluded':True,'claimExcluded':True})
signal.alarm(0)
say({'stage':'complete','scope':'entire original general-LS Delta-zero u=1/2 Q=2 branch, hence the affine-ell leading-zero locus of W=0','oneVariableActualQQCoverDegrees':[37,32,11,11,6,1],'allOriginalLeadingZeroFibersRetained':True,'allSamePointMomentAndGramTracesVerified':True,'sourceSha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'peakRssKiB':resource.getrusage(resource.RUSAGE_SELF).ru_maxrss,'wholeSpecialBranchExcluded':True,'wholeDeltaZeroExcluded':False,'ordinaryISPClaim':False,'claimExcluded':True})
