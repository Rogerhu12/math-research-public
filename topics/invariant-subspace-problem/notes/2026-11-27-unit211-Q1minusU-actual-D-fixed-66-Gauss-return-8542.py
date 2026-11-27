#!/usr/bin/env python3
"""R150 Q=1-u genuine new G2-chart original four-quadratic input:
multiplication, the two remaining cubic rows, NS/PS, and two original
parameter cofactors. The whole m=1/2 and T0=0 branches are already excluded.
120 seconds / 1 GiB. New paid-linear-unit original-row saturation.
All source DAG edges are exact six-column polynomial identities.
This new target is p(h)*Res_u(C_h,F_37_76) and its actual modular Bezout
return against the already proved 222-degree original input. No complete
QQ resultant or frozen rational closure is run.
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

ctx=fmpq_mpoly_ctx.get(('u','ell','x','y','t','dummy_t','zeta','dummy'),'lex');ep,kp,Lp,Tp,fp,tp,zp,dp=ctx.gens();zz=ctx.constant(0);oo=ctx.constant(1)
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
u,l,x0,x1,t,unused,zeta=map(R,ctx.gens()[:7]);Q=1-u;Delta=u
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

assert P02==(1-u)*((3*u-2)*l-2*u*u+3*u)
assert T0==(1-u)*(2*u-l)
Rt0=u*EB.b+(u-l*Q)/u*EB.a
Ry0=-4*bc*EB.a+l*Rt0
symbolic={'lam':lam,'T':T,'f':f,'ell':l,'Dphysical':Dphysical,'E1':E1.a,'Rt0':Rt0,'Ry0':Ry0,'N1':NH.a,'NS':NS.a,'PS':PS.a}
say(stage='new_Qboundary_G2_chart_same_original_Gram',originalE0N0P1Verified=True,weightedOriginalNPThroughHAHBVerified=True,originalDistinctValueRetained=True,wholeWeightChartExcluded=False)
Mp=(ep-1)*kp**2+2*ep*kp-ep**2
Hp=(2*ep-1)*kp+ep
P0p=(1-ep)*((3*ep-2)*kp-2*ep**2+3*ep)
Kzp=(ep-1)*kp**2+(2*ep-ep**2)*kp+ep**2*(2*ep-1)
G2p=(6*ep-4)*kp**3+2*kp**2+(-2*ep+8*ep**2-8*ep**3)*kp-2*ep**2
units=[('u',ep),('Q',1-ep),('ell',kp),('M',Mp),('H',Hp),('P02',P0p),('paid_T0_ell_minus_2u',kp-2*ep),('paid_uHalf_2u_minus_one',2*ep-1),('paid_Kz_zero_complete',Kzp),('complete_equal_weights_ell_minus_u',kp-ep),('complete_Q_ell_half',2*kp-1)]
out=[];cleared_polys=[];cleared_scales=[]
for name,rr,deg in [('E1',E1.a,2),('Rt0',Rt0,2),('Ry0',Ry0,2),('N1',NH.a,2),('weighted_N',NS.a,3),('weighted_P',PS.a,3)]:
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
 say({'stage':'new_Qboundary_G2_chart_original_X_Gram_coordinates','name':name,'degrees':list(map(int,po.degrees())),'terms':len(po.to_dict()),'paidRemoved':hist,'totalDegreeXYt':deg,'originalE0N0P1AndMeanReconstructionVerified':True,'claimExcluded':False})

from itertools import combinations
base_units=units
raw_xyz=(Lp,Tp,fp)
headmons=[(2,0,0),(1,1,0),(1,0,1),(0,2,0),(0,1,1),(0,0,2)]
freemons=[(0,0,0),(1,0,0),(0,1,0),(0,0,1),(0,2,0),(0,1,1)]
cubemons=[(0,3,0),(0,2,1)]
original=[symbolic[n] for n in ['E1','Rt0','Ry0','N1','NS','PS']]
assert len(cleared_polys)==6 and len(cleared_scales)==6

def coeffmap(rr):
 rr=R(rr);ans={}
 assert all(all(m[j]==0 for j in range(2,8)) for m in rr.d.to_dict())
 for mm,cc in rr.n.to_dict().items():
  assert mm[5]==mm[6]==mm[7]==0
  key=tuple(map(int,mm[2:5]))
  ans[key]=ans.get(key,zz)+cc*ep**int(mm[0])*kp**int(mm[1])
 return {key:R(pp,rr.d) for key,pp in ans.items() if pp}

def param_coefficient(po,mon):
 ans=zz
 for mm,cc in po.to_dict().items():
  assert mm[5]==mm[6]==mm[7]==0
  if tuple(map(int,mm[2:5]))==mon:
   ans+=cc*ep**int(mm[0])*kp**int(mm[1])
 return ans

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
  assert all(all(mm[j]==0 for j in range(2,8)) for mm in dd)
  rec=dict(degrees=list(map(int,ff.degrees()[:2])),totalDegree=int(ff.total_degree()),terms=len(dd),multiplicity=int(mul),sha256=hashlib.sha256(str(ff).encode()).hexdigest())
  if len(dd)<=80:rec['coefficients_u_ell']=[[int(mm[0]),int(mm[1]),str(cc)] for mm,cc in dd.items()]
  outf.append(rec)
 assert back==po
 return dict(content=str(sc),factors=outf,entireProductMultipliedBack=True)

heads=[[param_coefficient(cleared_polys[i],mon) for mon in headmons] for i in range(4)]
cols=[0,1,2,5]
matrix=[[row[j] for j in cols] for row in heads]
delta2=determinant(matrix);assert delta2
d2unpaid,d2paid,d2hist=strip_known(delta2,base_units)
chart_units=base_units+[('selected_quadratic_G2_chart',G2p)]
assert strip_known(delta2,chart_units)[0].total_degree()==0
inverse=[]
for j in range(4):
 row=[]
 for i in range(4):
  minor=[[matrix[r][c] for c in range(4) if c!=j] for r in range(4) if r!=i]
  row.append(R((-1)**(i+j)*determinant(minor),delta2))
 inverse.append(row)
for i in range(4):
 for j in range(4):
  assert sum((inverse[i][k]*R(matrix[k][j]) for k in range(4)),R())==int(i==j)
q=[];tags=[]
for j in range(4):
 qj=sum((inverse[j][i]*R(cleared_polys[i]) for i in range(4)),R())
 tag=[inverse[j][i]*cleared_scales[i] if i<4 else R() for i in range(6)]
 assert sum((tag[i]*original[i] for i in range(6)),R())==qj
 q.append(qj);tags.append(tag)
 cm=coeffmap(qj)
 for h,mon in enumerate([(2,0,0),(1,1,0),(1,0,1),(0,0,2)]):assert cm.get(mon,R())==int(h==j)
 for cf in cm.values():assert strip_known(cf.d,chart_units)[0].total_degree()==0
say(stage='new_Qboundary_G2_chart_paid_or_explicit_chart_four_original_rules',selectedColumns=cols,quadraticHeadUnpaidFactorization=factor_profile(d2unpaid),chartGlobalAfterPreviouslyPaidUnits=d2unpaid.total_degree()==0,all16InverseProductsOne=True,allFourOriginalTraceProductsVerified=True,claimExcluded=False)

def monomial(mm):
 return R(raw_xyz[0]**mm[0]*raw_xyz[1]**mm[1]*raw_xyz[2]**mm[2])
def order(mm):return (sum(mm),mm[0],mm[2],mm[1])
def verify_trace(pp,tag):
 assert sum((tag[i]*original[i] for i in range(6)),R())==pp

qheads=[(2,0,0),(1,1,0),(1,0,1),(0,0,2)]
def reduce_original_overlap(pp,tag):
 rem=R();pp=R(pp);tag=tag[:]
 while pp:
  cm=coeffmap(pp);mm=max(cm,key=order);cf=cm[mm]
  candidates=[j for j,lm in enumerate(qheads) if all(lm[z]<=mm[z] for z in range(3))]
  if not candidates:
   term=cf*monomial(mm);rem+=term;pp-=term;continue
  j=candidates[0];dif=tuple(mm[z]-qheads[j][z] for z in range(3));mult=cf*monomial(dif)
  pp-=mult*q[j];tag=[v-mult*tj for v,tj in zip(tag,tags[j])]
 verify_trace(rem,tag)
 assert all(mm in freemons+cubemons for mm in coeffmap(rem))
 return rem,tag

xx,yy,tt=map(R,raw_xyz)
overlap_specs=[(0,1,yy,xx),(0,2,tt,xx),(1,2,tt,yy),(2,3,tt,xx)]
overlaps=[];overlap_tags=[]
for index,(i,j,aa,bb) in enumerate(overlap_specs):
 pp=aa*q[i]-bb*q[j];tag=[aa*tags[i][g]-bb*tags[j][g] for g in range(6)]
 verify_trace(pp,tag)
 rem,tag=reduce_original_overlap(pp,tag);overlaps.append(rem);overlap_tags.append(tag)
 cm=coeffmap(rem)
 for cf in cm.values():assert strip_known(cf.d,chart_units)[0].total_degree()==0
 say(stage='new_Qboundary_G2_chart_original_cubic_overlap',index=index,remainingMonomials=list(cm),maxWeightNumeratorDegrees=[max((int(cf.n.degrees()[z]) for cf in cm.values()),default=-1) for z in range(2)],allOriginalSixTraceProductsVerified=True,allDenominatorsSupportedByExplicitChart=True,claimExcluded=False)


c0=coeffmap(overlaps[0]);c2=coeffmap(overlaps[2])
aa=c0.get(cubemons[0],R());bb=c0.get(cubemons[1],R())
cc=c2.get(cubemons[0],R());dd=c2.get(cubemons[1],R())
delta3=aa*dd-bb*cc;assert delta3
d3unpaid,d3paid,d3hist=strip_known(delta3.n,chart_units)
assert d3unpaid.total_degree()==0
assert strip_known(delta3.d,chart_units)[0].total_degree()==0
full_chart_units=chart_units
for alpha,beta in [(dd/delta3,-bb/delta3),(-cc/delta3,aa/delta3)]:
 pp=alpha*overlaps[0]+beta*overlaps[2]
 tag=[alpha*overlap_tags[0][g]+beta*overlap_tags[2][g] for g in range(6)]
 verify_trace(pp,tag);q.append(pp);tags.append(tag)
 for cf in coeffmap(pp).values():assert strip_known(cf.d,full_chart_units)[0].total_degree()==0
for j in range(2):
 cm=coeffmap(q[4+j])
 for h,mon in enumerate(cubemons):assert cm.get(mon,R())==int(j==h)
 assert all(mon in freemons+cubemons for mon in cm)
qheads=qheads+cubemons
say(stage='new_Qboundary_G2_Kz_nonzero_six_original_monic_rules',selectedCubicRows=[0,2],explicitUnpaidChart='G2 nonzero; full G2-zero branch retained',allOriginalTraceAndLeadingProductsVerified=True,allLeadingZeroFibresRetained=True,freeModuleClaimed=False,claimExcluded=False)

basis=[monomial(mm) for mm in freemons]
variables=[xx,yy,tt]
def reduce_six(inputp,inputtag=None):
 pp=R(inputp);rem=R()
 tag=[R() for _ in range(6)] if inputtag is None else inputtag[:]
 while pp:
  cm=coeffmap(pp);mm=max(cm,key=order);cf=cm[mm]
  candidates=[j for j,lm in enumerate(qheads) if all(lm[z]<=mm[z] for z in range(3))]
  if not candidates:
   term=cf*monomial(mm);rem+=term;pp-=term;continue
  j=candidates[0];dif=tuple(mm[z]-qheads[j][z] for z in range(3))
  mult=cf*monomial(dif)
  pp-=mult*q[j];tag=[v-mult*tj for v,tj in zip(tag,tags[j])]
 cm=coeffmap(rem);assert all(mm in freemons for mm in cm)
 verify_trace(rem-inputp if inputtag is None else rem,tag)
 row=[cm.get(mm,R()) for mm in freemons]
 for cf in row:assert strip_known(cf.d,full_chart_units)[0].total_degree()==0
 return row,tag

matrices=[];errors=[]
for axis in range(3):
 matrix=[];error=[]
 for i in range(6):
  row,tag=reduce_six(variables[axis]*basis[i])
  matrix.append(row);error.append([-v for v in tag])
 matrices.append(matrix);errors.append(error)
 say(stage='new_Qboundary_G2_Kz_nonzero_original_six_monomial_multiplication',axis=axis,originalMonomialIdentities=6,allOriginalTraceProductsVerified=True,allDenominatorsPaidOnExplicitChart=True,maxCoefficientNumeratorDegrees=[max(int(v.n.degrees()[z]) for row in matrix for v in row) for z in range(2)],claimExcluded=False)

necessary=[];necessary_tags=[];necessary_labels=[]

for oi in [1,3]:
 row,tag=reduce_six(overlaps[oi],overlap_tags[oi])
 necessary.append(row);necessary_tags.append(tag);necessary_labels.append('remaining_cubic_'+str(oi))
 say(stage='new_Qboundary_G2_Kz_nonzero_remaining_original_cubic_row',index=oi,allOriginalSixTraceProductsVerified=True,freeModuleNotAssumed=True,claimExcluded=False)
for gen in [4,5]:
 initial=[R(int(i==gen)) for i in range(6)]
 row,tag=reduce_six(original[gen],initial)
 necessary.append(row);necessary_tags.append(tag);necessary_labels.append(['NS','PS'][gen-4])
 say(stage='new_Qboundary_G2_Kz_nonzero_same_original_cubic_return',name=necessary_labels[-1],maxCoefficientNumeratorDegrees=[max(int(v.n.degrees()[z]) for v in row) for z in range(2)],allOriginalTraceProductsVerified=True,claimExcluded=False)

def clear_row(row,tag):
 den=oo
 for cf in row:den*=cf.d/den.gcd(cf.d)
 assert strip_known(den,full_chart_units)[0].total_degree()==0
 pols=[cf.n*(den/cf.d) for cf in row]
 removed=oo;history=[]
 for name,atom in full_chart_units:
  count=0
  while any(pols):
   gg=atom
   for pol0 in pols:gg=gg.gcd(pol0)
   if gg.total_degree()==0:break
   pols=[pol0/gg for pol0 in pols];removed*=gg;count+=1
  if count:history.append([name,count])
 for pol0,cf in zip(pols,row):assert pol0*removed*cf.d==cf.n*den
 assert strip_known(removed,full_chart_units)[0].total_degree()==0
 scale=R(den,removed);trace=[scale*tt0 for tt0 in tag]
 verify_trace(sum((R(pols[j])*basis[j] for j in range(6)),R()),trace)
 return pols,trace,history

polynomial_rows=[];polynomial_tags=[];poly_labels=[]
for row,tag,label in zip(necessary,necessary_tags,necessary_labels):
 pols,tr,hist=clear_row(row,tag)
 polynomial_rows.append(pols);polynomial_tags.append(tr);poly_labels.append(label)
 say(stage='new_Qboundary_G2_Kz_nonzero_cleared_original_six_column_row',label=label,degrees=[max(int(pol0.degrees()[z]) for pol0 in pols) for z in range(2)],terms=sum(len(pol0.to_dict()) for pol0 in pols),paidRemoved=hist,allOriginalProductsVerified=True,claimExcluded=False)
base_count=len(polynomial_rows)
extra_sources=[0,1]
for src in extra_sources:
 for axis in range(3):
  rawrow=[sum((R(polynomial_rows[src][i])*matrices[axis][i][j] for i in range(6)),R()) for j in range(6)]
  if not any(rawrow):continue
  rawtag=[variables[axis]*polynomial_tags[src][g]-sum((R(polynomial_rows[src][i])*errors[axis][i][g] for i in range(6)),R()) for g in range(6)]
  verify_trace(sum((rawrow[j]*basis[j] for j in range(6)),R()),rawtag)
  pols,tr,hist=clear_row(rawrow,rawtag)
  polynomial_rows.append(pols);polynomial_tags.append(tr);poly_labels.append(poly_labels[src]+'*'+'xyt'[axis])
  say(stage='new_Qboundary_G2_Kz_nonzero_additional_original_same_point_product',sourceRow=src,axis=axis,degrees=[max(int(pol0.degrees()[z]) for pol0 in pols) for z in range(2)],terms=sum(len(pol0.to_dict()) for pol0 in pols),allOriginalTraceAndPaidProductsVerified=True,claimExcluded=False)



# New input: the paid M unit, or one explicitly named alternative.
# No complete QQ C/D projection or repeated 27-group scan is run.
from flint import fmpq_poly
from math import gcd as intgcd
pc=fmpq_mpoly_ctx.get(('u','h'),'lex')
U,H=pc.gens();pzero=pc.constant(0);pone=pc.constant(1)
z1=fmpq_poly([]);o1=fmpq_poly([1]);h1=fmpq_poly([0,1])
def qexact(a,b):
 q,r=divmod(a,b);assert not r and q*b==a
 return q
class F1:
 def __init__(self,n=0,d=None,reduce=True):
  if isinstance(n,F1):self.n=n.n;self.d=n.d;return
  if not isinstance(n,fmpq_poly):n=fmpq_poly([fmpq(n)])
  if d is None:d=o1
  elif not isinstance(d,fmpq_poly):d=fmpq_poly([fmpq(d)])
  assert d
  if not n:self.n=z1;self.d=o1;return
  if reduce:
   g=n.gcd(d);n=qexact(n,g);d=qexact(d,g)
  lc=d.coeffs()[-1];self.n=n*(fmpq(1)/lc);self.d=d*(fmpq(1)/lc)
 def __bool__(self):return bool(self.n)
 def __add__(self,o):
  o=F1(o)
  if not self:return o
  if not o:return self
  g=self.d.gcd(o.d);a=qexact(self.d,g);b=qexact(o.d,g)
  return F1(self.n*b+o.n*a,a*o.d)
 __radd__=__add__
 def __neg__(self):return F1(-self.n,self.d,False)
 def __sub__(self,o):return self+-F1(o)
 def __rsub__(self,o):return F1(o)+-self
 def __mul__(self,o):
  o=F1(o)
  if not self or not o:return F1()
  g=self.n.gcd(o.d);k=o.n.gcd(self.d)
  return F1(qexact(self.n,g)*qexact(o.n,k),qexact(self.d,k)*qexact(o.d,g),False)
 __rmul__=__mul__
 def __truediv__(self,o):
  o=F1(o);assert o
  return self*F1(o.d,o.n)
 def __eq__(self,o):
  o=F1(o);return self.n*o.d==o.n*self.d
def embed(po):
 return pc.from_dict({(0,j):cf for j,cf in enumerate(po.coeffs()) if cf})
def map_weight(po):
 assert all(all(int(mm[j])==0 for j in range(2,8)) for mm in po.to_dict())
 return pc.from_dict({(int(mm[0])+int(mm[1]),int(mm[1])):cf for mm,cf in po.to_dict().items()})
def integer_primitive_row(row):
 den=1
 for po in row:
  for cf in po.to_dict().values():
   pair=str(cf).split('/');d=int(pair[1]) if len(pair)==2 else 1
   den=den//intgcd(den,d)*d
 nums=[]
 for po in row:
  for cf in po.to_dict().values():
   pair=str(cf).split('/');n=int(pair[0]);d=int(pair[1]) if len(pair)==2 else 1
   nums.append(n*(den//d))
 gg=0
 for n in nums:gg=intgcd(gg,abs(n))
 assert gg
 scale=fmpq(den,gg)
 result=[po*scale for po in row]
 for before,after in zip(row,result):
  assert after==before*scale
  assert all('/' not in str(cf) for cf in after.to_dict().values())
 return result,scale
mapped_units=[(name,map_weight(atom)) for name,atom in full_chart_units]
def strip_row_units(row):
 initial=row[:];removed=pone;history=[]
 for name,atom in mapped_units:
  ct=0
  while any(row):
   common=atom
   for po in row:common=common.gcd(po)
   if common.total_degree()==0:break
   row=[po/common for po in row];removed*=common;ct+=1
  if ct:history.append([name,ct])
 assert all(po*removed==initial[j] for j,po in enumerate(row))
 return row,removed,history
def strip_scalar_units(po):
 before=po;paid=pone;history=[]
 for name,atom in mapped_units:
  ct=0
  while po:
   gg=po.gcd(atom)
   if gg.total_degree()==0:break
   q=po/gg;assert q*gg==po
   po=q;paid*=gg;ct+=1
  if ct:history.append([name,ct])
 assert po*paid==before
 return po,paid,history
last_profile2_factorization=None
def profile2(po):
 global last_profile2_factorization
 if not po:return {'zero':True}
 sc,fac=po.factor();last_profile2_factorization=(po,sc,fac)
 back=pc.constant(sc);ans=[]
 for ff,power in fac:
  back*=ff**int(power)
  r={'degrees':list(map(int,ff.degrees())),'totalDegree':int(ff.total_degree()),
     'terms':len(ff.to_dict()),'multiplicity':int(power),
     'sha256':hashlib.sha256(str(ff).encode()).hexdigest()}
  if len(ff.to_dict())<=256:r['coefficients_u_h']=[[int(mm[0]),int(mm[1]),str(cf)] for mm,cf in ff.to_dict().items()]
  ans.append(r)
 assert back==po
 return {'content':str(sc),'factors':ans,'entireFactorProductMultipliedBack':True}

base_rows=[];base_edges=[]
for index,row in enumerate(polynomial_rows):
 mapped=[map_weight(po) for po in row]
 power=min(int(mm[0]) for po in mapped for mm in po.to_dict())
 reduced=[pc.from_dict({(int(mm[0])-power,int(mm[1])):cf for mm,cf in po.to_dict().items()}) for po in mapped]
 assert all(red*U**power==po for red,po in zip(reduced,mapped))
 normalized,scale=integer_primitive_row(reduced)
 assert all(U**power*normalized[j]==scale*mapped[j] for j in range(6))
 base_rows.append(normalized)
 base_edges.append({'originalRow':index,'label':poly_labels[index],'uPowerDivided':power,'scalar':str(scale)})
say(stage='new_Qboundary_unit_source_DAG_roots',
    roots=base_edges,allOriginalSixEquationTagsAlreadyMultipliedBackInThisBuild=True,
    allSixColumnHMapsAndOnlyPaidUDivisionsMultipliedBack=True)

# Actual target row: its difference from a paid nonzero multiple of Dphys
# is an explicitly checked original-six-equation combination.
dr,derr=reduce_six(Dphysical)
dDen=oo
for cf in dr:dDen*=cf.d/dDen.gcd(cf.d)
assert strip_known(dDen,full_chart_units)[0].total_degree()==0
dp=[cf.n*(dDen/cf.d) for cf in dr]
verify_trace(sum((R(dp[j])*basis[j] for j in range(6)),R())-R(dDen)*Dphysical,
             [R(dDen)*v for v in derr])
if not any(dp):
 signal.alarm(0)
 say(stage='new_Qboundary_Dphysical_already_in_original_monic_rule_ideal',
     completeOriginalSixEquationIdentityVerified=True,wholeCurrentQChartExcluded=True)
 raise SystemExit(0)
dm=[map_weight(po) for po in dp]
dPower=min(int(mm[0]) for po in dm for mm in po.to_dict())
dd=[pc.from_dict({(int(mm[0])-dPower,int(mm[1])):cf for mm,cf in po.to_dict().items()}) for po in dm]
assert all(dd[j]*U**dPower==dm[j] for j in range(6))
target_row,target_scale=integer_primitive_row(dd)
assert all(target_row[j]*U**dPower==target_scale*dm[j] for j in range(6))
say(stage='new_Qboundary_unit_source_actual_D_target',
    originalSixEquationIdentityMultipliedBack=True,
    originalWeightDenominatorPaid=True,uPowerDivided=dPower,nonzeroConstantScale=str(target_scale),
    actualTargetAtOriginalPointIsPaidNonzeroMultipleOfDphysical=True)

unit_name=sys.argv[1] if len(sys.argv)>1 else 'M'
units_one={
 'M':(h1*h1,-(h1-o1)**2,map_weight(Mp),U**2),
 'H':(2*h1,o1-h1,map_weight(Hp),U),
 'P02':(3*h1-2*o1,3*o1-2*h1,map_weight(P0p),U*(1-U)),
 'Kz':(h1*h1-h1+2*o1,-(h1-o1)**2,map_weight(Kzp),U**2),
 'ellHalf':(2*h1,-o1,2*U*H-1,pone),
 'Q':(-o1,o1,1-U,pone),
 'uHalf':(2*o1,-o1,2*U-1,pone)
}
assert unit_name in units_one
a1,b1,original_unit,paid_extra=units_one[unit_name]
assert a1 and a1.gcd(b1).degree()==0
L=embed(a1)*U+embed(b1)
assert original_unit==paid_extra*L
say(stage='new_Qboundary_paid_linear_unit_input',unit=unit_name,
    unitCoefficients=[str(a1),str(b1)],allPrimitiveUnitAndOriginalMapProductsVerified=True,
    wholeChartKeptWhenAnyUnivariateKernelPivotVanishes=True)

def u_coefficients(po):
 if not po:return []
 degree=int(po.degrees()[0]);arrays=[[] for _ in range(degree+1)]
 for (i,j),cf in po.to_dict().items():
  i=int(i);j=int(j)
  if len(arrays[i])<=j:arrays[i].extend([fmpq(0)]*(j+1-len(arrays[i])))
  arrays[i][j]=cf
 return [fmpq_poly(ar) for ar in arrays]
pseudo=[];scales=[];true_evaluations=[]
for row in base_rows:
 degree=max((int(po.degrees()[0]) for po in row if po),default=0)
 ap=[a1**j for j in range(degree+1)]
 bp=[(-b1)**j for j in range(degree+1)]
 evaluated=[]
 for po in row:
  co=u_coefficients(po)
  ev=sum((cf*bp[i]*ap[degree-i] for i,cf in enumerate(co)),z1)
  evaluated.append(ev)
 pseudo.append(evaluated);scales.append(ap[degree])
 true_evaluations.append([F1(ev,ap[degree]) for ev in evaluated])

# Exact left kernels over QQ(h); every denominator is cleared before
# constructing an original row. No such denominator is ever inverted
# on the original solution set.
echelon=[];kernels=[];count=len(base_rows)
for index in range(count):
 row=[F1(v) for v in pseudo[index]]
 comb=[F1(scales[index] if j==index else 0) for j in range(count)]
 for entry in echelon:
  cf=row[entry['pivot']]
  if cf:
   row=[v-cf*w for v,w in zip(row,entry['row'])]
   comb=[v-cf*w for v,w in zip(comb,entry['comb'])]
 pivot=next((j for j,v in enumerate(row) if v),None)
 if pivot is not None:
  cf=row[pivot]
  row=[v/cf for v in row];comb=[v/cf for v in comb]
  echelon.append({'pivot':pivot,'row':row,'comb':comb})
  continue
 den=o1
 for cf in comb:den=den*qexact(cf.d,den.gcd(cf.d))
 coef=[cf.n*qexact(den,cf.d) for cf in comb]
 cg=z1
 for v in coef:cg=cg.gcd(v)
 assert cg
 coef=[qexact(v,cg) for v in coef]
 for col in range(6):
  assert not sum((F1(coef[j])*true_evaluations[j][col] for j in range(count)),F1())
 cost=max((int(v.degree()) for v in coef if v),default=-1)
 kernels.append((cost,index,coef))
say(stage='new_Qboundary_exact_QQh_unit_kernel',
    unit=unit_name,rank=len(echelon),kernelRows=len(kernels),
    allSixActualQuotientFieldColumnProductsMultipliedBack=True,
    allKernelCoefficientsClearedToQQhPolynomials=True)

derived=[];derived_edges=[]
for cost,index,coef in sorted(kernels,key=lambda item:(item[0],item[1])):
 coeff=[embed(v) for v in coef]
 combined=[sum((coeff[j]*base_rows[j][col] for j in range(count)),pzero) for col in range(6)]
 if not any(combined):continue
 divided=[po/L for po in combined]
 assert all(divided[j]*L==combined[j] for j in range(6))
 divided,removed,history=strip_row_units(divided)
 normalized,scale=integer_primitive_row(divided)
 den=L*removed
 numerators=[v*scale for v in coeff]
 assert all(den*normalized[col]==sum((numerators[j]*base_rows[j][col] for j in range(count)),pzero) for col in range(6))
 rec={'unit':unit_name,'kernelOrigin':index,'clearedCoefficientDegree':cost,
      'onlyPaidRowDivisorFactorization':profile2(den),
      'removedPaidRowFactors':history,'constantScale':str(scale),
      'sixColumnIdentitySHA256':hashlib.sha256((str(den)+'|'+'|'.join(str(v) for v in numerators)+'|'+'|'.join(str(v) for v in normalized)).encode()).hexdigest(),
      'rowDegrees':[max(int(po.degrees()[j]) for po in normalized if po) for j in range(2)],
      'rowTerms':sum(len(po.to_dict()) for po in normalized),
      'allSixPolynomialDAGEdgeIdentitiesMultipliedBack':True,
      'noUnpaidKernelPivotDividedOnOriginalChart':True}
 derived.append(normalized);derived_edges.append(rec)
 say(stage='new_Qboundary_actual_paid_unit_quotient_row',**rec)
if not derived:
 signal.alarm(0)
 say(stage='new_Qboundary_paid_unit_has_no_nonzero_quotient_row_from_this_input',unit=unit_name,
     allKernelIdentitiesChecked=True,wholeCurrentQChartExcluded=False,ordinaryISPClaim=False)
 raise SystemExit(0)
all_rows=base_rows+derived
new_indices=list(range(len(base_rows),len(all_rows)))

# Choose a genuinely new full row basis by a finite-field evaluation.
# This selects indices only; all later identities are exact QQ identities.
prime=1009
def at_point(po,up,hp):
 ans=0
 for (i,j),cf in po.to_dict().items():
  pair=str(cf).split('/');num=int(pair[0]);den=int(pair[1]) if len(pair)==2 else 1
  assert den%prime
  ans=(ans+(num%prime)*pow(den%prime,-1,prime)*pow(up,int(i),prime)*pow(hp,int(j),prime))%prime
 return ans
def select_rows(order,up,hp):
 selected=[];basis_mod=[]
 for idx in order:
  row=[at_point(po,up,hp) for po in all_rows[idx]]
  for piv,old in basis_mod:
   cf=row[piv]
   if cf:row=[(v-cf*w)%prime for v,w in zip(row,old)]
  piv=next((j for j,v in enumerate(row) if v),None)
  if piv is None:continue
  inv=pow(row[piv],-1,prime);row=[v*inv%prime for v in row]
  basis_mod.append((piv,row));selected.append(idx)
  if len(selected)==6:return selected
 return selected
order=new_indices+list(range(len(base_rows)))
selected=None;sample=None
samples=[(2,3*pow(2,-1,prime)%prime)]+[(u0,h0) for u0 in range(2,7) for h0 in range(3,9)]
for up,hp in samples:
 if any(at_point(atom,up,hp)==0 for _,atom in mapped_units):continue
 inds=select_rows(order,up,hp)
 if len(inds)==6 and any(i in new_indices for i in inds):
  selected=inds;sample=[up,hp];break
assert selected is not None
W=[all_rows[i] for i in selected]
say(stage='new_Qboundary_unit_saturated_actual_basis_selected',
    selectedRows=selected,derivedRowIndices=new_indices,selectionSampleModulo1009=sample,
    sampleUsedOnlyForChoosingIndicesNotForQQExclusion=True)

def det2(matrix):
 n=len(matrix)
 if n==0:return pone
 mm=[row[:] for row in matrix];previous=pone;sign=1
 for j in range(n-1):
  if not mm[j][j]:
   good=[i for i in range(j+1,n) if mm[i][j]]
   if not good:return pzero
   i=good[0];mm[j],mm[i]=mm[i],mm[j];sign=-sign
  pivot=mm[j][j]
  for i in range(j+1,n):
   for k in range(j+1,n):
    numerator=mm[i][k]*pivot-mm[i][j]*mm[j][k]
    quotient=numerator/previous;assert quotient*previous==numerator
    mm[i][k]=quotient
   mm[i][j]=pzero
  previous=pivot
 return sign*mm[-1][-1]
say(stage='new_Qboundary_fraction_free_physical_D_return_started',selectedRows=selected)
detW=det2(W);assert detW
nums=[]
for i in range(6):
 mm=[row[:] for row in W];mm[i]=target_row[:]
 num=det2(mm);nums.append(num)
 say(stage='new_Qboundary_fraction_free_actual_D_adjugate_row',
     row=i,numeratorDegrees=list(map(int,num.degrees())) if num else None)
assert all(detW*target_row[j]==sum((nums[i]*W[i][j] for i in range(6)),pzero) for j in range(6))
common=detW
for po in nums:common=common.gcd(po)
den=detW/common;cleared=[po/common for po in nums]
assert den*common==detW
assert all(cleared[i]*common==nums[i] for i in range(6))
assert all(den*target_row[j]==sum((cleared[i]*W[i][j] for i in range(6)),pzero) for j in range(6))
unpaid,paid,history=strip_scalar_units(den)
assert unpaid*paid==den
say(stage='new_Qboundary_complete_unit_DAG_fraction_free_physical_D_identity',
    unit=unit_name,initialOriginalSourceRows=len(base_rows),newActualUnitQuotientRows=len(derived),
    allInitialOriginalSixEquationTracesVerified=True,
    allDAGEdgesFullSixColumnPolynomialIdentities=True,
    wholeOriginalChartIdealMembershipFollowsByExactDAGComposition=True,
    onlyDAGDivisorsAreExplicitPreviouslyPaidUnits=True,
    allBareissAndAllSixCramerProductsMultipliedBack=True,
    commonCancellationMultipliedBackAfterDivisionAtAllParameterPoints=True,
    DtargetDiffersFromPaidNonzeroMultipleOfDphysicalByOriginalSixIdeal=True,
    denominatorDegrees=list(map(int,den.degrees())),
    denominatorTotalDegree=int(den.total_degree()),
    paidRemoved=history,
    unpaidNecessaryWeightPolynomial=profile2(unpaid),
    necessaryWeightPolynomialSHA256=hashlib.sha256(str(unpaid).encode()).hexdigest(),
    denominatorZeroFibresRetained=True,
    wholeCurrentQChartExcluded=(unpaid.total_degree()==0),
    noFrozenQQProjectionOrFrozenRationalClosureRerun=True,
    ordinaryISPClaim=False)

# The M certificate above is regenerated only to construct the new actual
# necessary polynomial, not as an extra replay gate. The following is a
# new fixed-degree Gauss input. Retain every root of the pure h factor.
from flint import nmod_mpoly_ctx,nmod_poly
assert unit_name=='M'
assert last_profile2_factorization[0]==unpaid
content,fac=last_profile2_factorization[1:]
large=[(ff,int(m)) for ff,m in fac if int(ff.degrees()[0])>0]
small=pone
for ff,m in fac:
 if int(ff.degrees()[0])==0:small*=ff**int(m)
assert len(large)==1 and large[0][1]==1
F=large[0][0]
assert tuple(map(int,F.degrees()))==(37,76)
assert hashlib.sha256(str(F).encode()).hexdigest()=='26012667236b0929b289f3ee81a501401d4e5bbde39628fe446c3d38ef5b0da3'
J7=9*H**7-50*H**6+96*H**5-90*H**4+68*H**3-32*H**2+9*H-2
pweight=(2*H-1)*(H**2-3*H+1)*J7
assert small==pweight and unpaid==pc.constant(content)*pweight*F
Flist,Fscale=integer_primitive_row([F]);Fint=Flist[0]
assert Fint==Fscale*F
say(stage='new_Qboundary_actual_D_source_fixed_66_input',
    Fdegrees=[37,76],FsourceSHA256=hashlib.sha256(str(F).encode()).hexdigest(),
    integerFScale=str(Fscale),pureHFactorDegree=10,
    wholePureHFactorRetained=True,
    physicalDOriginalIdealDAGFullyVerifiedAbove=True,
    noUnpaidFactorInverted=True,wholeQBoundaryExcluded=False)


def bareiss_det(MM):
 n=len(MM)
 if n==0:return oo
 MM=[row[:] for row in MM];prev=oo;sign=1
 for j in range(n-1):
  if not MM[j][j]:
   candidates=[i for i in range(j+1,n) if MM[i][j]]
   if not candidates:return zz
   sw=candidates[0];MM[j],MM[sw]=MM[sw],MM[j];sign=-sign
  pivot=MM[j][j]
  for i in range(j+1,n):
   for k in range(j+1,n):
    num=MM[i][k]*pivot-MM[i][j]*MM[j][k];quo=num/prev
    assert quo*prev==num;MM[i][k]=quo
   MM[i][j]=zz
  prev=pivot
 return sign*MM[-1][-1]


permutation=[1,2,3,4,5,0]
original_pRows=[[row[j] for j in permutation] for row in polynomial_rows]
def original_scalar_input(indices,label,expected_sha=None):
 selected=[original_pRows[i] for i in indices]
 cof=[(-1)**(j+5)*bareiss_det([[row[c] for c in range(5)] for k,row in enumerate(selected) if k!=j]) for j in range(6)]
 products=[sum((cof[i]*selected[i][col] for i in range(6)),zz) for col in range(6)]
 assert all(not v for v in products[:5]) and products[5]
 reduced,paid,hist=strip_known(products[5],full_chart_units)
 assert reduced*paid==products[5]
 source_sha=hashlib.sha256(str(reduced).encode()).hexdigest()
 if expected_sha is not None:assert source_sha==expected_sha
 mapped=map_weight(reduced)
 power=min(int(mm[0]) for mm in mapped.to_dict())
 poly_h=pc.from_dict({(int(mm[0])-power,int(mm[1])):cf for mm,cf in mapped.to_dict().items()})
 assert poly_h*U**power==mapped
 say(stage='new_D_Gauss_reconstructed_fixed_original_input',label=label,
     rows=indices,originalCofactorSHA256=source_sha,uPowerDivided=power,
     transformedDegrees=list(map(int,poly_h.degrees())),
     allOriginalSixColumnProductsAndPaidFactorProductsMultipliedBack=True)
 return poly_h,power

Ch,cpower=original_scalar_input([0,1,2,3,4,6],'paid_original_C',
 'd9ee664678e97aa5a1ebc17f1ba275456137915bb494e2daf0cd4b280f3eb312')
Dh,dpower=original_scalar_input([0,1,2,3,7,9],'paid_original_D',
 '4e16a4461f64280c962bf870aea6161edb455382074525be75a7fc0b3fbd5b3d')
assert cpower==34 and dpower==31
assert tuple(map(int,Ch.degrees()))==(29,43) and tuple(map(int,Dh.degrees()))==(29,42)
prime=1009
mc=nmod_mpoly_ctx.get(('u','h'),prime,'lex')
def mod_input(po):
 data={}
 for mm,cf in po.to_dict().items():
  pair=str(cf).split('/');num=int(pair[0]);den=int(pair[1]) if len(pair)==2 else 1
  assert den%prime
  data[tuple(map(int,mm))]=(num%prime)*pow(den%prime,-1,prime)%prime
 got=mc.from_dict(data)
 assert po and got and int(got.degrees()[0])==int(po.degrees()[0])
 return got
def as_univariate(po):
 assert all(int(mm[0])==0 for mm in po.to_dict())
 degree=int(po.degrees()[1]) if po else -1
 ar=[0]*max(0,degree+1)
 for mm,cf in po.to_dict().items():ar[int(mm[1])]=int(cf)
 out=nmod_poly(ar,prime);assert out.degree()==degree
 return out
def fixed_mod_resultant(first,second,label):
 first_m=mod_input(first);second_m=mod_input(second)
 degs=[int(first.degrees()[0]),int(second.degrees()[0])]
 res=as_univariate(first_m.resultant(second_m,'u'))
 say(stage='new_D_Gauss_true_fixed_Sylvester_reduction',label=label,
     actualQQUdegrees=degs,fixedOrder=sum(degs),bothOriginalUDegreesPreserved=True,
     allQQCoefficientDenominators1009Units=True,modDegree=int(res.degree()),
     modResultantSHA256=hashlib.sha256(str(res).encode()).hexdigest())
 return res
Rbar=fixed_mod_resultant(Ch,Dh,'already_paid_C_D_projection')
assert Rbar.degree()==2265
R0bar=Rbar
for rt,order0 in [(0,304),(1,47),(2,532)]:
 phi=nmod_poly([-rt,1],prime);order=0
 while R0bar:
  q,r=divmod(R0bar,phi)
  if r:break
  assert q*phi==R0bar
  R0bar=q;order+=1
 assert order==order0
assert R0bar.degree()==1382
R0bar*=pow(int(R0bar.coeffs()[-1]),-1,prime)
g222=R0bar

# Reconstruct the four indispensable, previously certified input
# projections. The other 23 unchanged gcd steps are not rerun.
old_specs=[
 ([0,1,2,3,4,7],'paid_old_cofactor_0',
  'de5338c250dbea1f0bd8ba6c89761cf6ce0bbb6df146d556e3b30b01a4b358f7',648),
 ([0,1,2,3,6,9],'paid_old_cofactor_2',
  'c1a6a64818969c53113194c65b9569e4bed4ef68f1303e1ea497bccd8faa9de2',646)]
for source_row,expected_sha,expected_degree in [
 (2,'d8457f689c3fd1b654be2113aedef500b0070538f305cd8ad5a8a15757dd5941',224),
 (3,'e68fa1c08e680a3be38f9be358bcdd1e083f98306829e2bc0789427b6a212510',222)]:
 axis=0
 rawrow=[sum((R(polynomial_rows[source_row][i])*matrices[axis][i][j] for i in range(6)),R()) for j in range(6)]
 rawtag=[variables[axis]*polynomial_tags[source_row][g]
         -sum((R(polynomial_rows[source_row][i])*errors[axis][i][g] for i in range(6)),R())
         for g in range(6)]
 verify_trace(sum((rawrow[j]*basis[j] for j in range(6)),R()),rawtag)
 pols,tr,hist=clear_row(rawrow,rawtag)
 index=len(original_pRows)
 original_pRows.append([pols[j] for j in permutation])
 old_specs.append(([0,1,2,3,4,index],'paid_old_'+('NSx' if source_row==2 else 'PSx'),expected_sha,expected_degree))
for indices,label,expected_sha,degree_after in old_specs:
 e_h,power=original_scalar_input(indices,label,expected_sha)
 proj=fixed_mod_resultant(Ch,e_h,label)
 gg,aa,bb=g222.xgcd(proj)
 assert aa*g222+bb*proj==gg and int(gg.coeffs()[-1])==1
 assert gg.degree()==degree_after
 g222=gg
assert g222.degree()==222
assert hashlib.sha256(str(g222).encode()).hexdigest()=='6765bcda43089672a28b6a25fd3e88de52235088e237f00d6eb6ddb5a9022cd4'
say(stage='new_D_Gauss_reconstructed_paid_222_input',
    degree=222,actualBezoutChainMultipliedBack=True,
    previous27GroupScanNotRerun=True,
    coefficients=[int(v) for v in g222.coeffs()],
    sha256=hashlib.sha256(str(g222).encode()).hexdigest())

new_res=fixed_mod_resultant(Ch,Fint,'new_actual_physical_D_F_37_76')
assert int(Ch.degrees()[0])==29 and int(Fint.degrees()[0])==37
pbar=as_univariate(mod_input(pweight))
assert pbar.degree()==10
newS=pbar*new_res
new_res_quotient,new_res_remainder=divmod(new_res,g222)
assert new_res_quotient*g222+new_res_remainder==new_res
new_gcd,left,right=g222.xgcd(newS)
assert left*g222+right*newS==new_gcd and new_gcd
assert int(new_gcd.coeffs()[-1])==1
factor_content,factors=new_gcd.factor()
back=nmod_poly([int(factor_content)],prime);factor_records=[]
for ff,mul in factors:
 back*=ff**int(mul)
 factor_records.append({'degree':int(ff.degree()),'multiplicity':int(mul),
                        'coefficients':[int(v) for v in ff.coeffs()]})
assert back==new_gcd
signal.alarm(0)
say(stage='new_complete_actual_D_fixed_66_Gauss_return',
    sourceSHA256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
    originalPhysicalDSourceIdealDAGVerified=True,
    originalFixedSylvesterQQUdegrees=[29,37],fixedSylvesterOrder=66,
    pureHFactorRetainedCoefficients=[int(v) for v in pbar.coeffs()],
    pureHFactorNotInverted=True,
    newFResultantRemainderModuloPaid222=[int(v) for v in new_res_remainder.coeffs()],
    newFResultantDivisionByPaid222MultipliedBack=True,
    fullNewModNecessaryProjectionDegree=int(newS.degree()),
    newModNecessaryProjectionSHA256=hashlib.sha256(str(newS).encode()).hexdigest(),
    actualFinalBezoutMultipliedBack=True,
    finalModGCDDegree=int(new_gcd.degree()),
    finalModGCDCoefficients=[int(v) for v in new_gcd.coeffs()],
    finalModGCDCompleteFactorization=factor_records,
    finalFactorizationProductMultipliedBack=True,
    strictQQGaussUsesPublishedMonic1382RemainderAndActualFixedOriginalInputs=True,
    wholeRemainingQChartExcluded=(new_gcd.degree()==0),
    wholeQBoundaryRequiresPreviouslyPublishedCompleteZeroBranchCoverage=True,
    noCompleteQQResultantComputed=True,noFrozenInputRerun=True,
    peakRssKiB=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss,
    ordinaryISPClaim=False)
