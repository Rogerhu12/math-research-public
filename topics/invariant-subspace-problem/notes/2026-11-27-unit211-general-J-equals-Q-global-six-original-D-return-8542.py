#!/usr/bin/env python3
"""New entire general J=Q remaining plane after H=0 was excluded.
Use an explicit two-minor Bezout identity to build global six original rules.
Return actual D/one from a bounded original relation input, stopping at full rank.
No W/Q-boundary assumption; no unpaid u-Q inverse, no old timeout replay.
120 seconds / 1 GiB. All source identities retain the original six polynomials.
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
ctx=fmpq_mpoly_ctx.get(('u','Q','x','y','t','dummy_t','zeta','dummy'),'lex');ep,kp,Lp,Tp,fp,tp,zp,dp=ctx.gens();zz=ctx.constant(0);oo=ctx.constant(1)
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
m,qp,x0,x1,t,unused,zeta=map(R,ctx.gens()[:7]);u=m;Q=qp;l=1-2*u*(1-u)/Q;Delta=1-Q
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

assert J==Q and not Pf
assert T0==4*u-4*u*u-Q
assert P02==-2*(u-1)*T0
assert Phi==-4*(u-1)**2
symbolic={'lam':lam,'T':T,'f':f,'ell':l,'Dphysical':Dphysical,'E1':E1.a,'EBe':EB.a,'EBo':EB.b,'N1':NH.a,'NS':NS.a,'PS':PS.a}
say(stage='new_general_J_equals_Q_same_original_Gram',originalE0N0P1Verified=True,weightedOriginalNPThroughHAHBVerified=True,originalDistinctValueRetained=True,wholeWeightChartExcluded=False)
units=[('u',ep),('u_minus_one',ep-1),('Q',kp),('Q_minus_one',kp-1),('original_P02',P02.n),('original_bc_M',M.n),('proved_general_ell_nonzero',l.n),('proved_general_equal_weights',(l-u).n)]
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
 say({'stage':'new_general_J_equals_Q_original_X_Gram_coordinates','name':name,'degrees':list(map(int,po.degrees())),'terms':len(po.to_dict()),'paidRemoved':hist,'totalDegreeXYt':deg,'originalE0N0P1AndMeanReconstructionVerified':True,'claimExcluded':False})

raw_xyz=(Lp,Tp,fp)
headmons=[(2,0,0),(1,1,0),(1,0,1),(0,2,0),(0,1,1),(0,0,2)]
freemons=[(0,0,0),(1,0,0),(0,1,0),(0,0,1),(0,2,0),(0,1,1)]
cubemons=[(0,3,0),(0,2,1)]
original=[symbolic[n] for n in ['E1','EBe','EBo','N1','NS','PS']]
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
  if len(dd)<=80:rec['coefficients_u_Q']=[[int(mm[0]),int(mm[1]),str(cc)] for mm,cc in dd.items()]
  outf.append(rec)
 assert back==po
 return dict(content=str(sc),factors=outf,entireProductMultipliedBack=True)



base_units=units
heads=[[param_coefficient(cleared_polys[i],mon) for mon in headmons] for i in range(4)]
cols=[0,1,2,5]
matrix=[[row[j] for j in cols] for row in heads]
delta2=determinant(matrix);assert delta2
d2unpaid,d2paid,d2hist=strip_known(delta2,base_units)
assert strip_known(d2unpaid,[('explicit_unpaid_H',2*ep+kp-2)])[0].total_degree()==0
chart_units=base_units+[('explicit_unpaid_H',2*ep+kp-2)]
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
say(stage='new_general_J_equals_Q_paid_or_explicit_chart_four_original_rules',selectedColumns=cols,quadraticHeadUnpaidFactorization=factor_profile(d2unpaid),chartGlobalAfterPreviouslyPaidUnits=d2unpaid.total_degree()==0,all16InverseProductsOne=True,allFourOriginalTraceProductsVerified=True,claimExcluded=False)

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
 say(stage='new_general_J_equals_Q_original_cubic_overlap',index=index,remainingMonomials=list(cm),maxWeightNumeratorDegrees=[max((int(cf.n.degrees()[z]) for cf in cm.values()),default=-1) for z in range(2)],allOriginalSixTraceProductsVerified=True,allDenominatorsSupportedByExplicitChart=True,claimExcluded=False)




# Complete explicit cubic coverage, with only the now-proven H unit.
Hpoly=2*ep+kp-2
F11=(15*ep**3*kp-16*ep**3+12*ep**2*kp**2-43*ep**2*kp+
     32*ep**2-8*ep*kp**2+24*ep*kp-16*ep+
     4*kp**3-8*kp**2+4*kp)
E11=4*kp**2+(9*ep**2-ep-8)*kp+12*ep**3-20*ep**2+4*ep+4
Upoly=3*ep*(ep-1)*Hpoly**2
assert F11==Upoly+(kp-ep)*E11
Cmat=[[coeffmap(pp).get(mm,R()) for mm in cubemons] for pp in overlaps]
def det2(i,j):return Cmat[i][0]*Cmat[j][1]-Cmat[i][1]*Cmat[j][0]
dA=det2(0,2);dB=det2(2,3)
sA=dA/R(ep-kp);sB=dB/R(F11)
assert sA*R(ep-kp)==dA and sB*R(F11)==dB
for rr in [sA,1/sA,sB,1/sB,R(Upoly),1/R(Upoly)]:
 assert strip_known(rr.d,chart_units)[0].total_degree()==0
wA=R(E11,Upoly)/sA;wB=R(1,Upoly)/sB
assert wA*dA+wB*dB==1
L=[[R() for _ in range(4)] for _ in range(2)]
for inds,wv in [([0,2],wA),([2,3],wB)]:
 i,j=inds
 adj=[[Cmat[j][1],-Cmat[i][1]],[-Cmat[j][0],Cmat[i][0]]]
 for a0 in range(2):
  for z0,col in enumerate(inds):L[a0][col]+=wv*adj[a0][z0]
for i in range(2):
 for j in range(2):
  assert sum((L[i][z]*Cmat[z][j] for z in range(4)),R())==int(i==j)
for row in L:
 for rr in row:assert strip_known(rr.d,chart_units)[0].total_degree()==0
for j in range(2):
 pp=sum((L[j][i]*overlaps[i] for i in range(4)),R())
 tag=[sum((L[j][i]*overlap_tags[i][g] for i in range(4)),R()) for g in range(6)]
 verify_trace(pp,tag)
 cm=coeffmap(pp)
 for z,mm in enumerate(cubemons):assert cm.get(mm,R())==int(j==z)
 assert all(mm in freemons+cubemons for mm in cm)
 for cf in cm.values():assert strip_known(cf.d,chart_units)[0].total_degree()==0
 q.append(pp);tags.append(tag)
qheads=qheads+cubemons
full_chart_units=chart_units
say(stage='new_general_JQ_global_six_original_rules',
    explicitBezout='F11+(u-Q)*E11=3u(u-1)H^2',
    twoCubicMinors=[['0','2'],['2','3']],
    allGlobalLeftInverseProductsVerified=True,
    allOriginalSixTraceProductsVerified=True,
    uMinusQNotInverted=True,F11NotInverted=True,
    allDenominatorsPreviouslyPaidAfterWholeHZeroExclusion=True,
    freeModuleNotAssumed=True,claimExcluded=False)
basis=[monomial(mm) for mm in freemons];variables=[xx,yy,tt]
def reduce_six(inputp,inputtag=None):
 pp=R(inputp);rem=R()
 tag=[R() for _ in range(6)] if inputtag is None else inputtag[:]
 while pp:
  cm=coeffmap(pp);mm=max(cm,key=order);cf=cm[mm]
  candidates=[j for j,lm in enumerate(qheads) if all(lm[z]<=mm[z] for z in range(3))]
  if not candidates:
   term=cf*monomial(mm);rem+=term;pp-=term;continue
  j=candidates[0];dif=tuple(mm[z]-qheads[j][z] for z in range(3))
  mult=cf*monomial(dif);pp-=mult*q[j]
  tag=[v-mult*tj for v,tj in zip(tag,tags[j])]
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
 say(stage='new_general_JQ_global_original_six_monomial_multiplication',
     axis=axis,allSixOriginalProductsMultipliedBack=True,
     allDenominatorsPaid=True,claimExcluded=False)
necessary=[];necessary_tags=[];necessary_labels=[]
for oi in range(4):
 row,tag=reduce_six(overlaps[oi],overlap_tags[oi])
 necessary.append(row);necessary_tags.append(tag);necessary_labels.append('original_overlap_'+str(oi))
for gen in [4,5]:
 initial=[R(int(i==gen)) for i in range(6)]
 row,tag=reduce_six(original[gen],initial)
 necessary.append(row);necessary_tags.append(tag);necessary_labels.append(['NS','PS'][gen-4])
 say(stage='new_general_JQ_global_same_original_cubic_return',
     name=necessary_labels[-1],allOriginalTraceProductsVerified=True,
     coefficientNumeratorDegrees=[max(int(v.n.degrees()[z]) for v in row) for z in range(2)],
     claimExcluded=False)
echelon=[];candidate_count=0
def add_original_row(row,tag,label):
 global candidate_count
 row=[R(v) for v in row];tag=tag[:];candidate_count+=1
 verify_trace(sum((row[j]*basis[j] for j in range(6)),R()),tag)
 for entry in echelon:
  cf=row[entry['pivot']]
  if cf:
   row=[v-cf*w for v,w in zip(row,entry['row'])]
   tag=[v-cf*w for v,w in zip(tag,entry['tag'])]
 piv=next((j for j,v in enumerate(row) if v),None)
 if piv is None:return False
 cf=row[piv];row=[v/cf for v in row];tag=[v/cf for v in tag]
 verify_trace(sum((row[j]*basis[j] for j in range(6)),R()),tag)
 echelon.append(dict(pivot=piv,row=row,tag=tag,label=label))
 say(stage='new_general_JQ_selected_original_relation_rank',
     rank=len(echelon),pivot=piv,label=label,
     fullOriginalSourceProductVerified=True,
     intermediatePivotZeroFibresNotDiscarded=True)
 return True
for row,tag,label in zip(necessary,necessary_tags,necessary_labels):
 add_original_row(row,tag,label)
 if len(echelon)==6:break
# Exact source products, not arbitrary new coefficient rows.
products_attempted=0
if len(echelon)<6:
 for ri,(row,tag,label) in enumerate(zip(necessary,necessary_tags,necessary_labels)):
  for axis in range(3):
   newrow=[sum((row[i]*matrices[axis][i][j] for i in range(6)),R()) for j in range(6)]
   newtag=[variables[axis]*tag[g]-sum((row[i]*errors[axis][i][g] for i in range(6)),R()) for g in range(6)]
   products_attempted+=1
   add_original_row(newrow,newtag,label+'*'+'xyt'[axis])
   if len(echelon)==6:break
  if len(echelon)==6:break
commutators_attempted=0
if len(echelon)<6:
 from itertools import combinations
 for i,j in combinations(range(3),2):
  for a0 in range(6):
   row=[sum((matrices[i][a0][k]*matrices[j][k][z]-matrices[j][a0][k]*matrices[i][k][z] for k in range(6)),R()) for z in range(6)]
   tag=[variables[i]*errors[j][a0][g]-variables[j]*errors[i][a0][g]+sum((matrices[j][a0][k]*errors[i][k][g]-matrices[i][a0][k]*errors[j][k][g] for k in range(6)),R()) for g in range(6)]
   commutators_attempted+=1;add_original_row(row,tag,'comm_'+str(i)+str(j)+'_'+str(a0))
   if len(echelon)==6:break
  if len(echelon)==6:break
say(stage='new_general_JQ_selected_original_relation_input_complete',
    rank=len(echelon),candidateRows=candidate_count,
    actualOriginalProductsAttempted=products_attempted,
    actualOriginalCommutatorsAttempted=commutators_attempted,
    stoppedAfterFullRankIfReached=True,
    uncomputedFullMultiplicationClosureNotClaimed=True)
for label,target in [('Dphysical',Dphysical),('one',R(1))]:
 row,err=reduce_six(target);comb=[R() for _ in range(6)]
 for entry in echelon:
  cf=row[entry['pivot']]
  if cf:
   row=[v-cf*w for v,w in zip(row,entry['row'])]
   comb=[v+cf*w for v,w in zip(comb,entry['tag'])]
 if any(row):
  say(stage='new_general_JQ_original_target_residual',
      target=label,residualNonzeroColumns=[j for j,v in enumerate(row) if v],
      wholePlaneExcluded=False)
  continue
 source=[comb[g]-err[g] for g in range(6)]
 verify_trace(target,source)
 den=oo
 for cf in source:den*=cf.d/den.gcd(cf.d)
 assert all(all(int(mm[j])==0 for j in range(2,8)) for mm in den.to_dict())
 remainder,paid,history=strip_known(den,full_chart_units)
 assert remainder*paid==den
 say(stage='new_general_JQ_complete_original_target_identity',
     target=label,fullOriginalSixProductIdentityVerified=True,
     denominatorDegrees=list(map(int,den.degrees()[:2])),
     denominatorTotalDegree=int(den.total_degree()),paidRemoved=history,
     unpaidDenominator=factor_profile(remainder),
     denominatorZeroFibresRetained=True,
     sourceIdentitySHA256=hashlib.sha256('|'.join(str(v.n)+'/'+str(v.d) for v in source).encode()).hexdigest(),
     wholeCurrentJQChartExcludedByThisIdentity=remainder.total_degree()==0,
     genericChartOnlyIfUnpaidDenominatorNonconstant=True)
signal.alarm(0)
say(stage='new_general_JQ_global_six_selected_original_target_return_end',
    sourceSHA256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
    peakRssKiB=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss,
    ordinaryISPClaim=False)
