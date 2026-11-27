#!/usr/bin/env python3
"""R150 general LS / original Delta=0 / W=0 / H!=0: new original
four-quadratic head atlas and cubic-overlap input. All original Gram and
weighted N/P identities are reconstructed. No emptiness is claimed from
multivariate gcds or an unpaid leading coefficient. 180 seconds / 4 GiB.
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


# New original input: head (x^2,xt,y^2,yt) and all six full cubic
# consistency rows. No nonexistent monomial reduction order is assumed.
from itertools import combinations
Hpaid=4*ep*kp-kp*kp-4*kp-8
C9paid=4*ep*ep*kp*kp-ep*(kp**4+9*kp**3+20*kp*kp+16*kp)+kp**3+10*kp*kp+24*kp+16
base_units=units+[('previous_whole_k_minus_one',kp+1),('previous_complete_H_zero',Hpaid),('previous_general_ell_zero',l.n),('previous_general_equal_weights',(l-u).n),('previous_W_u_equals_Q',(u-Q).n),('equal_weights_implied_k_plus_two',kp+2)]
chart_units=base_units+[('explicit_u_half_complement',2*ep+1),('explicit_C9_complement',C9paid)]
raw_xyz=(Lp,Tp,fp);xx,yy,tt=map(R,raw_xyz)
original=[symbolic[n] for n in ['E1','EBe','EBo','N1','NS','PS']]
pivmons=[(2,0,0),(1,0,1),(0,2,0),(0,1,1)]
freemons=[(0,0,0),(1,0,0),(0,1,0),(0,0,1),(1,1,0),(0,0,2)]
fourcubes=[(2,1,0),(1,2,0),(1,1,1),(0,0,3)]
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
  if len(dd)<=80:rec['coefficients_e_k']=[[int(mm[0]),int(mm[1]),str(cc)] for mm,cc in dd.items()]
  outf.append(rec)
 assert back==po
 return dict(content=str(sc),factors=outf,entireProductMultipliedBack=True)


def detR(mat):
 if not mat:return R(1)
 if len(mat)==1:return mat[0][0]
 return sum(((-1)**j*mat[0][j]*detR([[v for z,v in enumerate(row) if z!=j] for row in mat[1:]]) for j in range(len(mat))),R())
def mono(mm):return R(raw_xyz[0]**mm[0]*raw_xyz[1]**mm[1]*raw_xyz[2]**mm[2])
def verify(pp,tg):assert sum((tg[j]*original[j] for j in range(6)),R())==pp
head=[[param_coefficient(cleared_polys[i],mon) for mon in pivmons] for i in range(4)]
d2=determinant(head);assert d2
unpaid,paid,hist=strip_known(d2,base_units)
assert strip_known(d2,chart_units)[0].total_degree()==0
say(stage='new_W_alternative_original_quadratic_head',columns=[0,2,3,4],onlyNotYetGlobalFactorization=factor_profile(unpaid),explicitUHalfComplement=True,ellAndEqualWeightsAndUQUsedOnlyFromWholePriorTheorems=True,claimExcluded=False)
inv=[]
for j in range(4):
 inv.append([R((-1)**(i+j)*determinant([[head[a][b] for b in range(4) if b!=j] for a in range(4) if a!=i]),d2) for i in range(4)])
for i in range(4):
 for j in range(4):assert sum((inv[i][z]*R(head[z][j]) for z in range(4)),R())==int(i==j)
q=[];tags=[]
for i in range(4):
 pp=sum((inv[i][j]*R(cleared_polys[j]) for j in range(4)),R())
 tg=[inv[i][j]*cleared_scales[j] if j<4 else R() for j in range(6)]
 verify(pp,tg);q.append(pp);tags.append(tg)
 cm=coeffmap(pp)
 for j,m in enumerate(pivmons):assert cm.get(m,R())==int(i==j)
 assert all(sum(m)<=1 or m in pivmons+[(1,1,0),(0,0,2)] for m in cm)
 for v in cm.values():assert strip_known(v.d,chart_units)[0].total_degree()==0
free2=[(1,1,0),(0,0,2)]
par=[[-coeffmap(pp).get(m,R()) for m in free2] for pp in q]
(aa,bb),(cc,dd),(ee,ff),(gg,hh)=par
low=[mono(pivmons[i])-par[i][0]*mono(free2[0])-par[i][1]*mono(free2[1])-q[i] for i in range(4)]
for pp in low:assert all(sum(m)<=1 for m in coeffmap(pp))
spec=[[(yy,0),(bb*tt,3)],[(xx,2),(ff*tt,1)],[(yy,1),(dd*tt,3)],[(xx,3),(hh*tt,1)],[(xx+dd*tt,1),(-tt,0)],[(yy+hh*tt,3),(-tt,2)]]
srows=[];stags=[]
for terms in spec:
 pp=sum((cf*q[i] for cf,i in terms),R())
 tg=[sum((cf*tags[i][j] for cf,i in terms),R()) for j in range(6)]
 verify(pp,tg);srows.append(pp);stags.append(tg)
C=[[R(1),-aa,-bb*gg,-bb*hh],[-ee,R(1),-ff*cc,-ff*dd],[R(),-cc,1-dd*gg,-dd*hh],[-gg,R(),1-hh*cc,-hh*dd],[-cc,R(),aa-dd*cc,bb-dd*dd],[R(),-gg,ee-hh*gg,ff-hh*hh]]
rhs=[yy*low[0]+bb*tt*low[3],xx*low[2]+ff*tt*low[1],yy*low[1]+dd*tt*low[3],xx*low[3]+hh*tt*low[1],(xx+dd*tt)*low[1]-tt*low[0],(yy+hh*tt)*low[3]-tt*low[2]]
for i in range(6):
 assert sum((C[i][j]*mono(fourcubes[j]) for j in range(4)),R())-rhs[i]==srows[i]
 cm=coeffmap(srows[i])
 for j,m in enumerate(fourcubes):assert cm.get(m,R())==C[i][j]
 assert all(sum(m)<=2 or m in fourcubes for m in cm)
 for v in cm.values():assert strip_known(v.d,chart_units)[0].total_degree()==0
say(stage='new_W_six_by_four_original_cubic_identity',allSixCompleteOriginalTraceProductsVerified=True,allSixUniversalCoefficientFormulasMultipliedBack=True,allAffineLowerRhsChecked=True,noMonomialOrderingAssumedForQuadraticHead=True,claimExcluded=False)
minor_records=[];candidates=[]
for indices in combinations(range(6),4):
 mat=[C[i] for i in indices];de=detR(mat)
 if not de:
  rec=dict(rows=list(indices),zero=True);minor_records.append(rec);say(stage='new_W_original_six_by_four_cubic_minor',**rec,claimExcluded=False);continue
 assert strip_known(de.d,chart_units)[0].total_degree()==0
 rem,removed,history=strip_known(de.n,chart_units)
 rec=dict(rows=list(indices),numeratorDegrees=list(map(int,de.n.degrees()[:2])),denominatorDegrees=list(map(int,de.d.degrees()[:2])),paidRemoved=history,unpaidFactorization=factor_profile(rem),unitOnCurrentExplicitChart=rem.total_degree()==0)
 minor_records.append(rec);candidates.append((int(rem.total_degree()),len(rem.to_dict()),indices,de))
 say(stage='new_W_original_six_by_four_cubic_minor',**rec,allFactorAndPaidRemovalProductsMultipliedBack=True,claimExcluded=False)
assert candidates
_,_,chosen,de=min(candidates,key=lambda v:(v[0],v[1],v[2]))
mat=[C[i] for i in chosen];iv=[]
for j in range(4):iv.append([((-1)**(i+j))*detR([[mat[a][b] for b in range(4) if b!=j] for a in range(4) if a!=i])/de for i in range(4)])
for i in range(4):
 for j in range(4):assert sum((iv[i][a]*mat[a][j] for a in range(4)),R())==int(i==j)
for i,m in enumerate(fourcubes):
 pp=sum((iv[i][j]*srows[chosen[j]] for j in range(4)),R())
 tg=[sum((iv[i][j]*stags[chosen[j]][z] for j in range(4)),R()) for z in range(6)]
 verify(pp,tg);cm=coeffmap(pp)
 for j,mon in enumerate(fourcubes):assert cm.get(mon,R())==int(i==j)
 assert all(sum(mon)<=2 or mon==m for mon in cm)
rem,_,_=strip_known(de.n,chart_units)
signal.alarm(0)
say(stage='new_W_six_by_four_original_cubic_head_atlas_complete',sourceSHA256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),selectedOriginalRows=list(chosen),chosenCubicMinorUnpaidFactorization=factor_profile(rem),all15CubicMinors=minor_records,all4QuadraticOriginalTracesVerified=True,all6CubicConsistencyOriginalTracesVerified=True,all4SelectedCubicOriginalTracesVerified=True,all16SelectedInverseProductsVerified=True,allDenominatorsPaidOnExplicitQuadraticChart=True,explicitChartExcludesUHalfAndC9=True,newCubicLeadingZeroFibersRetained=rem.total_degree()!=0,globalOnCurrentExplicitChart=rem.total_degree()==0,fullTenCubicRulesAnd18MultiplicationsNotYetBuilt=True,freeModuleClaimed=False,claimExcluded=False,peakRssKiB=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)
