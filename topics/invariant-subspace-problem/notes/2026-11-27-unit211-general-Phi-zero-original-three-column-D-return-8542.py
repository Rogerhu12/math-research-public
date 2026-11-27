#!/usr/bin/env python3
"""New exact full Phi=0 face of the original general LS system.
Use the proved original three rules, then specialize exactly in the Phi
quotient before all new three-column operations. Preserve the full u,Q
surface, all original traces and physical D. No generic-module replay gate
and no old Q-boundary resultant. 120 seconds / 1 GiB.
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
ctx=fmpq_mpoly_ctx.get(('u','Q','ell','x','y','t','zeta','dummy'),'lex');ep,kp,Lp,Tp,fp,tp,zp,dp=ctx.gens();zz=ctx.constant(0);oo=ctx.constant(1)
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
m,qp,l,x0,x1,t,zeta=map(R,ctx.gens()[:7]);u=m;Q=qp;Delta=1-Q
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

symbolic={'lam':lam,'T':T,'f':f,'ell':l,'Dphysical':Dphysical,'E1':E1.a,'EBe':EB.a,'EBo':EB.b,'N1':NH.a,'NS':NS.a,'PS':PS.a}
say(stage='new_full_general_LS_same_original_Gram',originalE0N0P1Verified=True,weightedOriginalNPThroughHAHBVerified=True,originalDistinctValueRetained=True,wholeWeightChartExcluded=False)
units=[('u',ep),('u_minus_one',ep-1),('Q',kp),('Q_minus_one',kp-1),('original_P02',P02.n),('original_bc_M',M.n),('proved_general_ell_nonzero',Lp),('proved_general_equal_weights',Lp-ep)]
out=[];cleared_polys=[];cleared_scales=[]
for name,rr,deg in [('E1',E1.a,2),('EBe',EB.a,2),('EBo',EB.b,2),('N1',NH.a,2),('weighted_N',NS.a,3),('weighted_P',PS.a,3)]:
 assert all(int(m[3])+int(m[4])+int(m[5])<=deg for m in rr.n.to_dict())
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
 say({'stage':'new_full_general_LS_original_X_Gram_coordinates','name':name,'degrees':list(map(int,po.degrees())),'terms':len(po.to_dict()),'paidRemoved':hist,'totalDegreeXYt':deg,'originalE0N0P1AndMeanReconstructionVerified':True,'claimExcluded':False})

def determinant(matrix):
 n=len(matrix)
 if n==0:return oo
 if n==1:return matrix[0][0]
 outp=zz
 for j in range(n):
  minor=[row[:j]+row[j+1:] for row in matrix[1:]]
  outp+=(-1)**j*matrix[0][j]*determinant(minor)
 return outp

def strip_known(po,atoms):
 previous=po;paid=oo;hist=[]
 for name,atom in atoms:
  count=0
  while po:
   gg=po.gcd(atom)
   if gg.total_degree()==0:break
   quotient=po/gg
   assert quotient*gg==po
   po=quotient;paid*=gg;count+=1
  if count:hist.append([name,count])
 assert po*paid==previous
 return po,paid,hist

def factor_profile(po):
 if not po:return dict(zero=True)
 sc,fac=po.factor();back=ctx.constant(sc);outf=[]
 for ff,mul in fac:
  back*=ff**int(mul)
  dd=ff.to_dict()
  assert all(all(mm[j]==0 for j in range(3,8)) for mm in dd)
  rec=dict(degrees=list(map(int,ff.degrees()[:3])),totalDegree=int(ff.total_degree()),terms=len(dd),multiplicity=int(mul),sha256=hashlib.sha256(str(ff).encode()).hexdigest())
  if len(dd)<=80:rec['coefficients_u_Q_ell']=[[int(mm[0]),int(mm[1]),int(mm[2]),str(cc)] for mm,cc in dd.items()]
  outf.append(rec)
 assert back==po
 return dict(content=str(sc),factors=outf,entireProductMultipliedBack=True)


from itertools import combinations
def pc(po,mon):
 ans=zz
 for mm,cc0 in po.to_dict().items():
  assert all(int(mm[j])==0 for j in range(6,8))
  if tuple(map(int,mm[3:6]))==mon:ans+=cc0*ep**int(mm[0])*kp**int(mm[1])*Lp**int(mm[2])
 return ans
headmons=[(2,0,0),(1,1,0),(1,0,1),(0,2,0),(0,1,1),(0,0,2)]
heads=[[pc(po,mon) for mon in headmons] for po in cleared_polys[:4]]

# The entire T0=0 and J=Q faces are already independently excluded.
units=units+[('proved_whole_general_T0',T0.n),('proved_whole_general_J_minus_Q',(J-Q).n)]
fixed_columns=[0,2,3,4]
Hmat=[[row[j] for j in fixed_columns] for row in heads]
hd=determinant(Hmat);assert hd
assert strip_known(hd,units)[0].total_degree()==0
Hinverse=[]
for i in range(4):
 row=[]
 for j in range(4):
  minor=[[Hmat[r][c] for c in range(4) if c!=i] for r in range(4) if r!=j]
  row.append(R(((-1)**(i+j))*determinant(minor),hd))
 Hinverse.append(row)
for i in range(4):
 for j in range(4):
  assert sum((Hinverse[i][k]*R(Hmat[k][j]) for k in range(4)),R())==int(i==j)
quad=[];quad_traces=[]
for i in range(4):
 pp=sum((Hinverse[i][j]*R(cleared_polys[j]) for j in range(4)),R())
 tr=[Hinverse[i][j]*cleared_scales[j] for j in range(4)]
 assert sum((tr[j]*[E1.a,EB.a,EB.b,NH.a][j] for j in range(4)),R())==pp
 assert strip_known(pp.d,units)[0].total_degree()==0
 quad.append(pp);quad_traces.append(tr)
def rcoef(rr,mon):
 assert all(all(int(mm[j])==0 for j in range(3,8)) for mm in rr.d.to_dict())
 return R(pc(rr.n,mon),rr.d)
qcoeff=[[rcoef(rr,mm) for mm in headmons] for rr in quad]
for i in range(4):
 for j,col in enumerate(fixed_columns):
  assert qcoeff[i][col]==int(i==j)
aH,bH=-qcoeff[0][1],-qcoeff[0][5]
cH,dH=-qcoeff[1][1],-qcoeff[1][5]
eH,fH=-qcoeff[2][1],-qcoeff[2][5]
gH,hH=-qcoeff[3][1],-qcoeff[3][5]
say(stage='new_Phi0_specialized_global_four_original_quadratic_rules',
    fixedHeadColumns=fixed_columns,
    headEquations=['x^2=a*xy+b*t^2','x*t=c*xy+d*t^2',
                   'y^2=e*xy+f*t^2','y*t=g*xy+h*t^2'],
    all16InverseProductsVerified=True,
    allFourCompleteOriginalRowTracesVerified=True,
    allDenominatorsPreviouslyPaidByEntireT0AndJQTheorems=True,
    noMonomialDescentOrderAssumed=True,noSixGeneratorClaim=True)


Uunit=cH.n-gH.n
assert Uunit==-(kp**2*Lp*T0.n*(J-Q).n)/2
assert strip_known(Uunit,units)[0].total_degree()==0
for vv in [cH.d,gH.d]:
 assert strip_known(vv,units)[0].total_degree()==0
original=[E1.a,EB.a,EB.b,NH.a,NS.a,PS.a]
qtags=[tag+[R(),R()] for tag in quad_traces]
def trace_check(pp,tag):
 assert sum((tag[i]*original[i] for i in range(6)),R())==pp
xy_rule=-(R(cH.d)*quad[1]-R(gH.d)*quad[3])/R(Uunit)
xy_tag=[-(R(cH.d)*qtags[1][i]-R(gH.d)*qtags[3][i])/R(Uunit) for i in range(6)]
xx_rule=quad[0]+aH*xy_rule
xx_tag=[qtags[0][i]+aH*xy_tag[i] for i in range(6)]
yy_rule=quad[2]+eH*xy_rule
yy_tag=[qtags[2][i]+eH*xy_tag[i] for i in range(6)]
rules=[xx_rule,xy_rule,yy_rule];tags=[xx_tag,xy_tag,yy_tag]

# New exact full Phi=0 parameter input. The already-paid general rules
# are formed before specialization, so their normalized numerator identity
# is never incorrectly re-inferred after a cancellation in this face.
Phi_relation=kp*Lp-(kp-2*(ep-1)*(ep-2))
Phi_ell_numerator=kp-2*(ep-1)*(ep-2)
Phi_sub_count=0
Phi_sub_cache={}
def Phi_map_poly(po):
 global Phi_sub_count
 key=str(po)
 if key in Phi_sub_cache:return Phi_sub_cache[key]
 if not po:
  result=R();Phi_sub_cache[key]=result;return result
 degree=max(int(mm[2]) for mm in po.to_dict())
 den=kp**degree;mapped=zz;quotient=zz
 powers=[oo]
 for j in range(degree):powers.append(powers[-1]*Phi_ell_numerator)
 for mm,cf in po.to_dict().items():
  k=int(mm[2])
  other=cf*ep**int(mm[0])*kp**int(mm[1])
  for j in range(3,8):other*=ctx.gens()[j]**int(mm[j])
  mapped+=other*kp**(degree-k)*powers[k]
  if k:
   geometric=sum(((kp*Lp)**(k-1-j)*powers[j] for j in range(k)),zz)
   quotient+=other*kp**(degree-k)*geometric
 assert po*den-mapped==Phi_relation*quotient
 result=R(mapped,den);Phi_sub_cache[key]=result;Phi_sub_count+=1
 return result
def Phi_map(rr):
 rr=R(rr);return Phi_map_poly(rr.n)/Phi_map_poly(rr.d)
phi_ell=Phi_map(l);phi_t0=Phi_map(T0);phi_j=Phi_map(J)
assert not Phi_map(Phi)
assert phi_ell==1-2*(u-1)*(u-2)/Q
assert Phi_map(P02)==2*(u-1)*phi_ell*Q
assert phi_t0==-Q-4*(u-1)
assert phi_j-Q==-4*(u-1)**2
assert phi_ell-u==-(u-1)*(Q+2*u-4)/Q
original=[Phi_map(vv) for vv in original]
rules=[Phi_map(vv) for vv in rules]
tags=[[Phi_map(vv) for vv in tag] for tag in tags]
Dphysical=Phi_map(Dphysical)
phi_units=[]
for label,atom in units:
 rr=Phi_map(R(atom));assert rr
 assert strip_known(rr.d,[('Q',kp)])[0].total_degree()==0
 phi_units.append((label,rr.n))
# This whole branch has a completed independent original theorem.
phi_units.append(('proved_whole_general_Q1minusU',ep+kp-1))
units=phi_units
assert all(all(int(mm[2])==0 for mm in rr.n.to_dict()) and
           all(int(mm[2])==0 for mm in rr.d.to_dict())
           for rr in original+rules+[Dphysical])
say(stage='new_general_Phi0_exact_original_parameter_map',
    parameterEquation='Q*ell=Q-2*(u-1)*(u-2)',
    completePhiZeroSurfaceRetained=True,onlyParameterMapDivisor='Q',
    originalRuleSpecializationIsExactQuotientIdentity=True,
    allMapDifferencesMultipliedByExactPhiRelation=True,
    originalP02Identity='2*(u-1)*ell*Q',
    originalJMinusQIdentity='-4*(u-1)^2',
    originalT0Identity='-Q-4*(u-1)',
    originalEqualWeightsFactor='-(u-1)*(Q+2*u-4)/Q',
    alreadyPaidQ1minusUBoundaryRetainedAsOriginalUnit=True,
    ordinaryISPClaim=False)

leadmons=[(2,0),(1,1),(0,2)]
raw_xy=[Tp,fp]
def monxy(mm):return R(raw_xy[0]**mm[0]*raw_xy[1]**mm[1])
def xycoeffs(pp):
 pp=R(pp)
 assert all(int(mm[3])==int(mm[4])==int(mm[6])==int(mm[7])==0 for mm in pp.d.to_dict())
 result={}
 for mm,cc in pp.n.to_dict().items():
  assert mm[6]==mm[7]==0
  key=(int(mm[3]),int(mm[4]))
  term=cc*ep**int(mm[0])*kp**int(mm[1])*Lp**int(mm[2])*tp**int(mm[5])
  result[key]=result.get(key,R())+R(term,pp.d)
 assert sum((cf*monxy(mm) for mm,cf in result.items()),R())==pp
 return {mm:cf for mm,cf in result.items() if cf}
for j,(rule,tag) in enumerate(zip(rules,tags)):
 trace_check(rule,tag)
 cm=xycoeffs(rule)
 assert cm.get(leadmons[j],R())==1
 assert all(mm==leadmons[j] or sum(mm)<=1 for mm in cm)
 for cf in cm.values():assert strip_known(cf.d,units)[0].total_degree()==0
 say(stage='new_Phi0_specialized_global_monic_xy_rule',
     leadingMonomial=leadmons[j],allSixOriginalTraceProductsVerified=True,
     strictXYDegreeDescent=True,tIsPolynomialCoefficientNotInverted=True,
     coefficientMaxTDegree=max((int(cf.n.degrees()[5]) for cf in cm.values()),default=-1),
     allCoefficientDenominatorsPreviouslyPaid=True)
basis_mons=[(0,0),(1,0),(0,1)];basis=[monxy(mm) for mm in basis_mons]
def normal(pp,tag=None):
 pp=R(pp);initial=R(pp)
 tr=[R() for _ in range(6)] if tag is None else tag[:]
 has_original_trace=tag is not None;rem=R()
 while pp:
  cm=xycoeffs(pp)
  mm=max(cm,key=lambda m:(sum(m),m[0],m[1]));cf=cm[mm]
  choices=[i for i,lm in enumerate(leadmons) if all(mm[j]>=lm[j] for j in range(2))]
  if not choices:
   term=cf*monxy(mm);rem+=term;pp-=term;continue
  i=choices[0];diff=tuple(mm[j]-leadmons[i][j] for j in range(2))
  mult=cf*monxy(diff);pp-=mult*rules[i]
  tr=[v-mult*w for v,w in zip(tr,tags[i])]
 trace_check(rem if has_original_trace else rem-initial,tr)
 cm=xycoeffs(rem)
 assert all(mm in basis_mons for mm in cm)
 row=[cm.get(mm,R()) for mm in basis_mons]
 for cf in row:
  assert strip_known(cf.d,units)[0].total_degree()==0
  assert all(int(mm[j])==0 for mm in cf.d.to_dict() for j in [3,4,5,6,7])
 return row,tr
matrices=[];errors=[]
for axis,var in enumerate(map(R,raw_xy)):
 matrix=[];err=[]
 for i,basis_entry in enumerate(basis):
  row,tr=normal(var*basis_entry);matrix.append(row);err.append([-v for v in tr])
  trace_check(var*basis_entry-sum((row[j]*basis[j] for j in range(3)),R()),err[-1])
 matrices.append(matrix);errors.append(err)
 say(stage='new_Phi0_specialized_actual_three_generator_multiplication',
     variable=['x','y'][axis],allThreeOriginalProductsMultipliedBack=True,
     maxCoefficientTDegree=max(int(cf.n.degrees()[5]) for row in matrix for cf in row),
     freeModuleNotAssumed=True,tInverseNeverUsed=True)
returned=[]
for gi,pp in enumerate(original):
 tr=[R(int(i==gi)) for i in range(6)]
 row,tag=normal(pp,tr)
 trace_check(sum((row[j]*basis[j] for j in range(3)),R()),tag)
 data=dict(name=['E1','EBe','EBo','N1','NS','PS'][gi],
     rowCoefficientNumeratorDegrees=[[int(cf.n.degrees()[j]) for j in [0,1,2,5]] if cf else None for cf in row],
     rowCoefficientTerms=[len(cf.n.to_dict()) for cf in row],
     allSixOriginalTraceProductsMultipliedBack=True,
     allCoefficientDenominatorsPreviouslyPaid=True)
 returned.append((gi,row,tag));say(stage='new_Phi0_specialized_complete_original_three_column_return',**data)
drow,dtag=normal(Dphysical)
trace_check(sum((drow[j]*basis[j] for j in range(3)),R())-Dphysical,dtag)
say(stage='new_Phi0_specialized_same_original_physical_D_three_column_return',
    allSixOriginalTraceProductsMultipliedBack=True,
    originalPhysicalUnitStillRequired=True,
    coefficientTDegrees=[int(cf.n.degrees()[5]) if cf else -1 for cf in drow],
    noParameterProjectionSubstitutedForPhysicalD=True)
phi_ambiguities=[]
# Two genuine ambiguity rows. They add relations, never an unproved
# confluence or freeness hypothesis.
for name,i,j,a0,b0 in [('x2_y_vs_xy_x',0,1,R(fp),R(Tp)),
                       ('xy_y_vs_y2_x',1,2,R(fp),R(Tp))]:
 pp=a0*rules[i]-b0*rules[j]
 tr=[a0*tags[i][g]-b0*tags[j][g] for g in range(6)]
 row,tag=normal(pp,tr)
 trace_check(sum((row[j]*basis[j] for j in range(3)),R()),tag)
 phi_ambiguities.append((name,row,tag))
 say(stage='new_Phi0_specialized_three_generator_original_ambiguity',
     name=name,coefficientTDegrees=[int(cf.n.degrees()[5]) if cf else -1 for cf in row],
     originalTraceProductsMultipliedBack=True,notAssumedZeroCoefficientRow=True)


# A new same-source physical-D certificate on the Phi=0 face.
# Initial specialized rows already have complete original six-equation
# traces above. The following edges are exact free-three-column identities,
# so no repeated expanded trace gate is inserted.
def clear_three(row,label):
 den=oo
 for cf in row:
  gg=den.gcd(cf.d);den=(den/gg)*cf.d
 assert strip_known(den,units)[0].total_degree()==0
 pols=[]
 for cf in row:
  pp=cf.n*(den/cf.d);assert R(pp)==cf*R(den);pols.append(pp)
 nonzero=[pp for pp in pols if pp]
 if not nonzero:return pols,R(den),[]
 common=nonzero[0]
 for pp in nonzero[1:]:common=common.gcd(pp)
 _,paid,hist=strip_known(common,units)
 reduced=[]
 for pp,cf in zip(pols,row):
  qq=pp/paid;assert qq*paid==pp
  assert R(qq)==cf*R(den,paid);reduced.append(qq)
 return reduced,R(den,paid),hist
phi_rows=[];phi_row_labels=[];phi_row_origin=[]
for gi,row,tag in returned:
 if not any(row):continue
 label=['E1','EBe','EBo','N1','NS','PS'][gi]
 pols,scale,hist=clear_three(row,label)
 phi_rows.append(pols);phi_row_labels.append(label);phi_row_origin.append(('original',gi,scale))
 say(stage='new_Phi0_cleared_original_three_column_relation',
     label=label,rowIndex=len(phi_rows)-1,
     coefficientDegrees_u_Q_t=[[int(pp.degrees()[i]) for i in [0,1,5]] if pp else None for pp in pols],
     coefficientTerms=[len(pp.to_dict()) for pp in pols],paidRemoved=hist,
     allThreeScalarClearingProductsMultipliedBack=True,
     originalSixEquationTraceAlreadyVerified=True)
for label,row,tag in phi_ambiguities:
 if not any(row):continue
 pols,scale,hist=clear_three(row,label)
 phi_rows.append(pols);phi_row_labels.append(label);phi_row_origin.append(('ambiguity',label,scale))
 say(stage='new_Phi0_cleared_original_ambiguity_relation',
     label=label,rowIndex=len(phi_rows)-1,
     coefficientDegrees_u_Q_t=[[int(pp.degrees()[i]) for i in [0,1,5]] if pp else None for pp in pols],
     coefficientTerms=[len(pp.to_dict()) for pp in pols],paidRemoved=hist,
     allThreeScalarClearingProductsMultipliedBack=True,
     originalSixEquationTraceAlreadyVerified=True)
Dpol,Dscale,Dhist=clear_three(drow,'original_Dphysical')
assert strip_known(Dscale.n,units)[0].total_degree()==0
assert strip_known(Dscale.d,units)[0].total_degree()==0
assert all(all(int(mm[2])==int(mm[3])==int(mm[4])==int(mm[6])==int(mm[7])==0 for mm in pp.to_dict()) for pp in Dpol)
def three_variable_profile(po):
 if not po:return {'zero':True}
 content,factors=po.factor();back=ctx.constant(content);data=[]
 for ff,mult in factors:
  back*=ff**int(mult)
  assert all(all(int(mm[i])==0 for i in [2,3,4,6,7]) for mm in ff.to_dict())
  rec={'degrees_u_Q_t':[int(ff.degrees()[i]) for i in [0,1,5]],
       'totalDegree':int(ff.total_degree()),'terms':len(ff.to_dict()),
       'multiplicity':int(mult),'SHA256':hashlib.sha256(str(ff).encode()).hexdigest()}
  if len(ff.to_dict())<=120:
   rec['coefficients_u_Q_t']=[[int(mm[0]),int(mm[1]),int(mm[5]),str(cf)] for mm,cf in ff.to_dict().items()]
  data.append(rec)
 assert back==po
 return {'content':str(content),'factors':data,'fullFactorProductMultipliedBack':True}
# Select an actual QQ-independent row set by exact minors. There is no
# numerical rank claim, no localization at this determinant, and no
# repeated scan of the general projective-head minors.
selected=[];pivot_columns=[];selected_det=None
for i,row in enumerate(phi_rows):
 if len(selected)==3:break
 trial=selected+[i]
 found=False
 for cols in combinations(range(3),len(trial)):
  dd=determinant([[phi_rows[j][k] for k in cols] for j in trial])
  if dd:
   selected=trial;pivot_columns=list(cols);selected_det=dd;found=True;break
say(stage='new_Phi0_exact_original_relation_row_rank',
    actualGenericRowRank=len(selected),selectedRows=selected,
    selectedLabels=[phi_row_labels[i] for i in selected],
    selectedColumns=pivot_columns,originalAllParameterFibresRetained=True)
whole_excluded=not any(Dpol)
paid_D_identity=False
necessary=None
if not any(Dpol):
 say(stage='new_Phi0_original_physical_D_is_in_six_equation_ideal',
     fullActualOriginalTraceAlreadyVerified=True,wholePhiZeroFaceExcluded=True)
elif selected:
 selected_matrix=[[phi_rows[i][j] for j in pivot_columns] for i in selected]
 denominator=determinant(selected_matrix);assert denominator
 cramer=[]
 for rr in range(len(selected)):
  mm=[row[:] for row in selected_matrix];mm[rr]=[Dpol[j] for j in pivot_columns]
  cramer.append(determinant(mm))
 residual=[denominator*Dpol[j]-sum((cramer[i]*phi_rows[rr][j] for i,rr in enumerate(selected)),zz) for j in range(3)]
 if not any(residual):
  common=denominator
  for cp in cramer:common=common.gcd(cp)
  d0=denominator/common;coefs=[cp/common for cp in cramer]
  assert d0*common==denominator
  for cp,cc0 in zip(cramer,coefs):assert cc0*common==cp
  for j in range(3):
   assert d0*Dpol[j]==sum((coefs[i]*phi_rows[rr][j] for i,rr in enumerate(selected)),zz)
  necessary,paid,history=strip_known(d0,units)
  assert necessary*paid==d0
  paid_D_identity=True
  whole_excluded=necessary.total_degree()==0
  say(stage='new_Phi0_complete_original_physical_D_cofactor_identity',
      selectedRows=selected,selectedLabels=[phi_row_labels[i] for i in selected],
      determinantSize=len(selected),
      fullRawAndCancelledFreeThreeColumnIdentitiesMultipliedBack=True,
      commonPolynomialCancellationBeforeAnyParameterEvaluation=True,
      allCancelledZeroFibresRetainedByVerifiedPolynomialIdentity=True,
      targetIsPaidUnitTimesOriginalSamePointDphysicalModuloOriginalSixIdeal=True,
      targetWeightScaleHasOnlyPaidFactors=True,
      onlyPaidParameterFactorsStrippedFromNecessaryPolynomial=history,
      originalNecessaryPolynomial=three_variable_profile(necessary),
      necessarySHA256=hashlib.sha256(str(necessary).encode()).hexdigest(),
      completePhiZeroFaceExcluded=whole_excluded,
      allRemainingUQTZeroFibresRetained=True)
 else:
  say(stage='new_Phi0_original_physical_D_not_in_selected_generic_row_span',
      residualDegrees=[[int(pp.degrees()[i]) for i in [0,1,5]] if pp else None for pp in residual],
      noDIdentityOrEmptinessClaim=True)
signal.alarm(0)
say(stage='new_general_Phi0_original_three_column_D_input_complete',
    sourceSHA256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
    exactOriginalParameterSubstitutionsMultipliedBack=Phi_sub_count,
    originalCoefficientRing='paid QQ[u,Q] localization[t]',
    completePhiZeroSurfaceRetained=True,allOriginalTraceAndLocalColumnDAGEdgesVerified=True,
    allSixOriginalEquationsAndSamePointPhysicalDRetained=True,
    genericThreeParameterModuleNotRecomputedAfterSpecialization=True,
    actualOriginalDIdentity=paid_D_identity,
    wholePhiZeroFaceExcluded=whole_excluded,
    noOriginalValueSufficiencyClaimFromOnlyNecessaryRows=True,
    peakRssKiB=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss,
    ordinaryISPClaim=False)
