#!/usr/bin/env python3
"""New general LS: the same physical D in two original three-column spans.
Cramer identities are verified in all three free columns before and after
common-polynomial cancellation; no determinant or canceled factor is inverted.
The necessary old five-row reconstruction is reused, without old projections.
180 seconds / 4 GiB.
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
say(stage='new_general_LS_global_four_original_quadratic_rules',
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
 say(stage='new_general_LS_global_monic_xy_rule',
     leadingMonomial=leadmons[j],allSixOriginalTraceProductsVerified=True,
     strictXYDegreeDescent=True,tIsPolynomialCoefficientNotInverted=True,
     coefficientMaxTDegree=max((int(cf.n.degrees()[5]) for cf in cm.values()),default=-1),
     allCoefficientDenominatorsPreviouslyPaid=True)

# New input starts here. The preceding three monic rules are the necessary
# reconstruction of the published module, not a rerun of its old atlas.
units=units+[('proved_entire_Q_equals_one_minus_u',ep+kp-1)]
basis_mons=[(0,0),(1,0),(0,1)]
basis=[monxy(mm) for mm in basis_mons]
def paid(rr):
 return strip_known(R(rr).d,units)[0].total_degree()==0
def brief(rr):
 rr=R(rr);bb=(str(rr.n)+' / '+str(rr.d)).encode()
 data=dict(degrees_u_Q_ell_t=[int(rr.n.degrees()[j]) for j in [0,1,2,5]] if rr else None,
           terms=len(rr.n.to_dict()),bytes=len(bb),sha256=hashlib.sha256(bb).hexdigest())
 if len(bb)<=2048:data['exactExpression']=bb.decode()
 return data
def reduce_three(pp):
 initial=R(pp);pp=R(pp);rem=R();quot=[R() for _ in range(3)]
 while pp:
  cm=xycoeffs(pp);mm=max(cm,key=lambda m:(sum(m),m[0],m[1]));cf=cm[mm]
  choices=[i for i,lm in enumerate(leadmons) if all(mm[j]>=lm[j] for j in range(2))]
  if not choices:
   term=cf*monxy(mm);rem+=term;pp-=term;continue
  i=choices[0];diff=tuple(mm[j]-leadmons[i][j] for j in range(2))
  mult=cf*monxy(diff);pp-=mult*rules[i];quot[i]+=mult
 assert initial==rem+sum((quot[i]*rules[i] for i in range(3)),R())
 assert paid(rem) and all(paid(q) for q in quot)
 assert all(mm in basis_mons for mm in xycoeffs(rem))
 return rem,quot
derived=[]
def add_original_row(name,initial,origin):
 rem,quot=reduce_three(initial)
 po,removed,hist=strip_known(rem.n,units)
 scale=R(rem.d,removed)
 normalized=R(po)
 assert normalized==scale*rem and paid(scale) and paid(1/scale)
 cm=xycoeffs(normalized)
 row=[cm.get(mm,R()) for mm in basis_mons]
 assert all(cf.d==oo for cf in row)
 assert sum((row[j]*basis[j] for j in range(3)),R())==normalized
 record=dict(name=name,origin=origin,normalization=brief(scale),
             originalLocalQuotients=[brief(q) for q in quot],
             coefficients=[brief(cf) for cf in row],paidRemoved=hist,
             completeThreeRuleDifferenceIdentityVerified=True,
             publishedSixOriginalTraceTheoremUsed=True,
             noUnpaidInverse=True)
 derived.append(dict(name=name,poly=normalized,row=[cf.n for cf in row],record=record))
 say(stage='new_general_LS_original_three_column_relation',**record)
 return normalized
r0=quad[3]+gH*xy_rule
assert all(mm in basis_mons for mm in xycoeffs(r0))
trace_check(r0,[qtags[3][i]+gH*xy_tag[i] for i in range(6)])
R0=add_original_row('remaining_qyt',r0,'qyt+gH*rxy, with its actual full six-original trace')
add_original_row('x_remaining_qyt',R(Tp)*R0,'x times the preceding complete original row')
add_original_row('y_remaining_qyt',R(fp)*R0,'y times the preceding complete original row')
add_original_row('ambiguity_x2_y_xy_x',R(fp)*rules[0]-R(Tp)*rules[1],
                 'y*rxx-x*rxy in the same three original rules')
add_original_row('ambiguity_xy_y_y2_x',R(fp)*rules[1]-R(Tp)*rules[2],
                 'y*rxy-x*ryy in the same three original rules')

# New target: the actual physical D, not the constant column or a norm of D.
Drem,Dquot=reduce_three(Dphysical)
Dpoly,Dpaid,Dhist=strip_known(Drem.n,units)
Dscale=R(Drem.d,Dpaid)
assert R(Dpoly)==Dscale*Drem
assert paid(Dscale) and paid(1/Dscale)
Dcm=xycoeffs(R(Dpoly))
Drow=[Dcm.get(mm,R()) for mm in basis_mons]
assert all(cf.d==oo for cf in Drow)
Drow=[cf.n for cf in Drow]
say(stage='new_general_three_column_physical_D_local_original_target',
    exactOriginalDminusThreeRuleCombinationVerified=True,
    scale=brief(Dscale),localQuotients=[brief(v) for v in Dquot],
    coefficientProfiles=[brief(R(v)) for v in Drow],
    paidRemoved=Dhist,physicalDUnitNotReplacedByAnyNorm=True,
    originalPhysicalDHasZeroRemainder=not any(Drow))
profiles=[]
if any(Drow):
 for indices in [(0,1,2),(0,3,4)]:
  mat=[derived[i]['row'] for i in indices]
  delta=determinant(mat);assert delta
  cofs=[]
  for i in range(3):
   replace=[row[:] for row in mat];replace[i]=Drow[:]
   cofs.append(determinant(replace))
  for j in range(3):
   assert delta*Drow[j]==sum((cofs[i]*mat[i][j] for i in range(3)),zz)
  common=delta
  for cf in cofs:common=common.gcd(cf)
  reduced=delta/common
  newcofs=[cf/common for cf in cofs]
  assert reduced*common==delta
  for cf,newcf in zip(cofs,newcofs):assert newcf*common==cf
  for j in range(3):
   assert reduced*Drow[j]==sum((newcofs[i]*mat[i][j] for i in range(3)),zz)
  necessary,removed,hist=strip_known(reduced,units)
  assert necessary*removed==reduced
  assert all(mm[3]==mm[4]==mm[6]==mm[7]==0 for mm in necessary.to_dict())
  tdeg=int(necessary.degrees()[5])
  lead=zz
  for mm,cc in necessary.to_dict().items():
   if int(mm[5])==tdeg:lead+=cc*ep**int(mm[0])*kp**int(mm[1])*Lp**int(mm[2])
  leadrem,leadpaid,leadhist=strip_known(lead,units)
  profile=dict(rows=[derived[i]['name'] for i in indices],
      originalTarget='paidUnit*Dphysical modulo the original three rules',
      commonCanceled=brief(R(common)),necessary=brief(R(necessary)),
      tDegree=tdeg,onlyPaidFactorsRemoved=hist,leadingRemaining=brief(R(leadrem)),
      leadingPaidRemoved=leadhist,
      allThreeRawAndCanceledColumnIdentitiesMultipliedBack=True,
      allCommonZeroFibersRetainedByPolynomialIdentity=True,
      noDeterminantOrCommonFactorInverted=True,
      fullOriginalPhysicalDNonzeroUsed=True,
      wholeOriginalAdmissibleChartExcluded=necessary.total_degree()==0)
  profiles.append(profile)
  say(stage='new_general_original_D_primitive_three_column_cofactor',**profile)
signal.alarm(0)
say(stage='new_general_original_D_two_primitive_cofactors_complete',
 sourceSHA256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
 originalDHadZeroRemainder=not any(Drow),numberOfCofactors=len(profiles),
 wholeOriginalAdmissibleChartExcluded=(not any(Drow)) or any(p['wholeOriginalAdmissibleChartExcluded'] for p in profiles),
 allUnpaidLeadingZeroFacesRetained=True,allIndividualOriginalValueConditionsStillRequired=True,
 peakRssKiB=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss,ordinaryISPClaim=False)
