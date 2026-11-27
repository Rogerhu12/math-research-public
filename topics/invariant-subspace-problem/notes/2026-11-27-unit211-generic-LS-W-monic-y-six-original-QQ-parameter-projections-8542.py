#!/usr/bin/env python3
"""New whole-W original QQ weight projections from the now-monic y sextic.
Regenerate the frozen original three-column cofactors, then cancel the exact
y^6 term by its paid weight leading and form two full fixed-degree resultants.
No new leading inverse, no numerical sampling, no multivariate gcd-one emptiness.
180 seconds / 4 GiB. Only small coefficient profiles, no large cache output.
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
say(stage='new_W_Ay_original_Gram_regeneration',originalE0N0P1Verified=True,originalMeanAndN1Verified=True,P2BaseIdentityVerified=True,weightedOriginalNAndPTracesThroughHAHBVerified=True,HankelPhysicalIdentityVerified=True,WWeightAndPaidUnitIdentitiesVerified=True,noXMinusUMinusOneInverted=True,claimExcluded=False)

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
 say({'stage':'new_W_Ay_original_regenerated_row','name':name,'degrees':list(map(int,po.degrees())),'terms':len(po.to_dict()),'paidRemoved':hist,'totalDegreeXYt':deg,'originalE0N0P1AndMeanReconstructionVerified':True,'claimExcluded':False})


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

# This original Gram prefix is only regeneration, not a repeated result gate.
# The complete J19 exclusion supplies one new WEIGHT unit on this W chart.
J19=16*e**4*k**3+e**3*(-8*k**4-16*k**3-96*k*k)+e*e*(-k**5-8*k**4+24*k**3+64*k*k+192*k)+e*(-2*k**5-14*k**4-12*k**3-128)-k**5-10*k**4-40*k**3-104*k*k-160*k-128
original=[symbolic[n] for n in ['E1','EBe','EBo','N1','NS','PS']]
original_names=['E1','EBe','EBo','N1','NS','PS']
gindices=[0,1,3];G=[original[j] for j in gindices]
xx,yy,tt=map(R,(Lp,Tp,fp))
def xtcoeffs(rr):
 rr=R(rr)
 assert all(all(mm[j]==0 for j in range(2,8)) for mm in rr.d.to_dict())
 ans={}
 for mm,cc in rr.n.to_dict().items():
  assert mm[5]==mm[6]==mm[7]==0
  ij=(int(mm[2]),int(mm[4]))
  ans[ij]=ans.get(ij,zz)+cc*ep**int(mm[0])*kp**int(mm[1])*Tp**int(mm[3])
 out={ij:R(vv,rr.d) for ij,vv in ans.items() if vv}
 assert sum((cc*xx**ij[0]*tt**ij[1] for ij,cc in out.items()),R())==rr
 return out
def ydegree(rr):
 rr=R(rr)
 assert all(mm[2]==mm[4]==mm[5]==mm[6]==mm[7]==0 for mm in rr.n.to_dict())
 assert all(all(mm[j]==0 for j in range(2,8)) for mm in rr.d.to_dict())
 return max((int(mm[3]) for mm in rr.n.to_dict()),default=-1)
def det3(a):
 return (a[0][0]*(a[1][1]*a[2][2]-a[1][2]*a[2][1])
        -a[0][1]*(a[1][0]*a[2][2]-a[1][2]*a[2][0])
        +a[0][2]*(a[1][0]*a[2][1]-a[1][1]*a[2][0]))
def detminor(a,i,j):
 ri=[h for h in range(3) if h!=i];cj=[h for h in range(3) if h!=j]
 return a[ri[0]][cj[0]]*a[ri[1]][cj[1]]-a[ri[0]][cj[1]]*a[ri[1]][cj[0]]
heads=[(2,0),(1,1),(0,2)]
HC=[[xtcoeffs(row).get(mon,R()) for mon in heads] for row in G]
assert all(ydegree(c0)<=0 for row in HC for c0 in row)
HD=det3(HC)
Z=4*bc*Q*(Q+2*e)+T0*(Q+2*e+l*Q)
assert HD==4*l*bc*((1-2*l)*Z-l*T0*T0)/P02
assert HD==-4*l*bc*e**4*u*(k+2)*J19/(k*Vbar**3*(1-Q)*P02)
assert paid_den(HD/J19) and paid_den(J19/HD)
known=known+[('previous_complete_J19_original_exclusion',J19.n),
             ('previous_general_T0_zero',T0.n),
             ('previous_general_J_equals_Q',(J-Q).n)]
assert paid_den(1/HD)
HI=[[R((-1)**(i+j))*detminor(HC,j,i)/HD for j in range(3)] for i in range(3)]
for i in range(3):
 for j in range(3):
  assert sum((HI[i][h]*HC[h][j] for h in range(3)),R())==(1 if i==j else 0)
  assert sum((HC[i][h]*HI[h][j] for h in range(3)),R())==(1 if i==j else 0)
assert all(paid_den(vv) for row in HI for vv in row)
qrules=[sum((HI[i][j]*G[j] for j in range(3)),R()) for i in range(3)]
tails=[xx**heads[i][0]*tt**heads[i][1]-qrules[i] for i in range(3)]
for i in range(3):
 assert qrules[i]==sum((HI[i][j]*G[j] for j in range(3)),R())
 cc=xtcoeffs(tails[i])
 assert all(sum(mon)<=1 for mon in cc)
 assert all(ydegree(cf)<=2-sum(mon) for mon,cf in cc.items())
say(stage='new_W_whole_J19_paid_original_binary_three_generator_rules',
 originalRows=['E1','EBe','N1'],headColumns=['x^2','x*t','t^2'],
 determinantOriginalIdentity='-4*ell*bc*e^4*u*(k+2)*J19/(k*Vbar^3*(1-Q)*P02)',
 bothMatrixInverseProductsActuallyIdentity=True,
 everyRuleOriginalCombinationActuallyMultipliedBack=True,
 everyDenominatorPreviouslyPaidIncludingCompleteJ19=True,
 baseRing='current paid weight ring A, then A[y]',
 generators=['1','x','t'],freeBasisClaim=False,
 noYMinusOneOrPhysicalDOrD27OrB239Inverse=True,claimExcluded=False)
B=[R(1),xx,tt]
def normal(rr):
 initial=R(rr);work=initial;rem=R();tag=[R() for _ in range(3)];steps=0
 while work:
  cc=xtcoeffs(work);ij=max(cc,key=lambda a:(sum(a),a[0],a[1]));cf=cc[ij]
  term=cf*xx**ij[0]*tt**ij[1]
  if sum(ij)<=1:
   rem=rem+term;work=work-term
  else:
   ri=0 if ij[0]>=2 else (1 if ij[0] else 2)
   hh=heads[ri];mult=cf*xx**(ij[0]-hh[0])*tt**(ij[1]-hh[1])
   work=work-mult*qrules[ri]
   tag=[tag[j]+mult*HI[ri][j] for j in range(3)]
   if work:
    top=max(xtcoeffs(work),key=lambda a:(sum(a),a[0],a[1]))
    assert (sum(top),top[0],top[1])<(sum(ij),ij[0],ij[1])
  steps+=1
  assert steps<=100
 assert initial==rem+sum((tag[j]*G[j] for j in range(3)),R())
 cr=xtcoeffs(rem);row=[cr.get(ij,R()) for ij in [(0,0),(1,0),(0,1)]]
 assert rem==sum((row[j]*B[j] for j in range(3)),R())
 return row,tag
def eqcombo(rr,tag):
 assert len(tag)==6 and R(rr)==sum((tag[j]*original[j] for j in range(6)),R())
def raw_reduction(rr,basecombo):
 row,rt=normal(rr);tag=basecombo[:]
 for j,h in enumerate(gindices):tag[h]=tag[h]-rt[j]
 rem=sum((row[j]*B[j] for j in range(3)),R());eqcombo(rem,tag)
 return row,tag
def mprofile(rr,cap=2048):
 rr=R(rr);nrows=[[list(map(int,mm)),str(cc)] for mm,cc in sorted(rr.n.to_dict().items())]
 drows=[[list(map(int,mm)),str(cc)] for mm,cc in sorted(rr.d.to_dict().items())]
 bb=json.dumps(dict(n=nrows,d=drows),separators=(',',':')).encode()
 ans=dict(numeratorDegrees=list(map(int,rr.n.degrees()[:5])),
          denominatorDegrees=list(map(int,rr.d.degrees()[:5])),
          numeratorTerms=len(nrows),denominatorTerms=len(drows),
          exactCoefficientBytes=len(bb),exactCoefficientSHA256=hashlib.sha256(bb).hexdigest())
 if len(bb)<=cap:ans['exactCoefficients']=json.loads(bb)
 return ans
Mx=[];Mt=[]
for symbol,variable,mat in [('x',xx,Mx),('t',tt,Mt)]:
 for j in range(3):
  row,tag=normal(variable*B[j]);mat.append(row)
  assert variable*B[j]==sum((row[h]*B[h] for h in range(3)),R())+sum((tag[h]*G[h] for h in range(3)),R())
  assert all(paid_den(cf) for cf in row+tag)
say(stage='new_W_three_generator_six_true_multiplication_rows',
 generators=['1','x','t'],sixFullOriginalTracesActuallyVerified=True,
 Mx=[[mprofile(c0,0) for c0 in row] for row in Mx],
 Mt=[[mprofile(c0,0) for c0 in row] for row in Mt],
 actionOnActualNonzeroValueColumnOnly=True,freeModuleNotAssumed=True,claimExcluded=False)
def matmul(a,b):
 return [[sum((a[i][h]*b[h][j] for h in range(3)),R()) for j in range(3)] for i in range(3)]
mtx=matmul(Mx,Mt);mxt=matmul(Mt,Mx)
comm=[[mtx[i][j]-mxt[i][j] for j in range(3)] for i in range(3)]
assert not any(comm[0])
rowdata=[];labels=[]
def addrow(label,row,tag):
 rem=sum((row[j]*B[j] for j in range(3)),R());eqcombo(rem,tag)
 if not rem:
  say(stage='new_W_three_column_zero_original_row',name=label,originalTraceVerified=True,claimExcluded=False)
  return
 pp,removed,hist=strip(rem.n);scale=R(rem.d,removed)
 assert paid_den(scale) and paid_den(1/scale)
 nrow=[scale*cf for cf in row];ntag=[scale*cf for cf in tag]
 assert sum((nrow[j]*B[j] for j in range(3)),R())==R(pp)
 eqcombo(R(pp),ntag)
 assert all(paid_den(cf) for cf in nrow+ntag)
 rowdata.append((nrow,ntag));labels.append(label)
 say(stage='new_W_actual_three_column_original_row',name=label,
     coefficientYDegrees=[ydegree(cf) for cf in nrow],
     row=mprofile(R(pp)),paidRemoved=hist,
     fullSixOriginalGeneratorCombinationVerified=True,claimExcluded=False)
L=(u-l)*original[1]+l*(1-Q)*original[2]
assert all(sum(ij)<=1 for ij in xtcoeffs(L))
Lcombo=[R(),u-l,l*(1-Q),R(),R(),R()]
Lrow,Ltag=raw_reduction(L,Lcombo);addrow('singleton_mean_L',Lrow,Ltag)
for variable,label in [(xx,'x_times_L'),(tt,'t_times_L')]:
 row,tag=raw_reduction(variable*L,[variable*cf for cf in Lcombo]);addrow(label,row,tag)
for i,(ia,ib) in enumerate([(0,1),(1,2)]):
 S=tt*qrules[ia]-xx*qrules[ib]
 parent=[R() for _ in range(6)]
 for j,h in enumerate(gindices):parent[h]=tt*HI[ia][j]-xx*HI[ib][j]
 row,tag=raw_reduction(S,parent)
 assert all(row[j]==-comm[i+1][j] for j in range(3))
 addrow('original_overlap_'+str(i+1),row,tag)
for gi in [2,4,5]:
 parent=[R() for _ in range(6)];parent[gi]=R(1)
 row,tag=raw_reduction(original[gi],parent)
 if gi==2:
  assert all(l*(1-Q)*row[j]==Lrow[j] for j in range(3))
  say(stage='new_W_original_EBo_same_three_column_return',
      originalTraceActuallyVerified=True,
      exactRelation='ell*(1-Q)*NF(EBo)=singleton_mean_L',
      allDenominatorsPaid=True,claimExcluded=False)
 else:addrow(original_names[gi],row,tag)
say(stage='new_W_complete_original_three_column_small_system',
 rowNames=labels,allOriginalSixRowsReturned=True,
 twoCommutatorOverlapRowsActOnActualValueColumn=True,
 sixTrueMultiplicationsVerified=True,originalIdealMembershipOfEveryRowVerified=True,
 noFreenessAssumption=True,noNewLeadingInverse=True,claimExcluded=False)
def rowindex(label):return labels.index(label)
new_constraints=[]
fixed=[['singleton_mean_L','x_times_L','t_times_L'],
       ['singleton_mean_L','original_overlap_1','original_overlap_2'],
       ['singleton_mean_L','NS','PS']]
for selection in fixed:
 if any(s not in labels for s in selection):
  say(stage='new_W_three_column_fixed_cofactor_zero_row',selection=selection,fullCoverageRetained=True,claimExcluded=False)
  continue
 inds=[rowindex(s) for s in selection];mat=[rowdata[j][0] for j in inds]
 cof=[R((-1)**i)*detminor(mat,i,0) for i in range(3)]
 value=sum((cof[i]*mat[i][0] for i in range(3)),R())
 assert value==det3(mat)
 for j in range(3):assert sum((cof[i]*mat[i][j] for i in range(3)),R())==(value if j==0 else 0)
 full=[sum((cof[i]*rowdata[inds[i]][1][j] for i in range(3)),R()) for j in range(6)]
 eqcombo(value,full)
 assert paid_den(value) and ydegree(value)<=6
 if not value:
  say(stage='new_W_original_fixed_three_column_constant_cofactor_zero',
      selection=selection,allThreeColumnAndOriginalProductsVerified=True,claimExcluded=False)
  continue
 pp,removed,hist=strip(value.n);scale=R(value.d,removed)
 assert R(pp)==scale*value and paid_den(scale) and paid_den(1/scale)
 normalized_full=[scale*cf for cf in full];eqcombo(R(pp),normalized_full)
 assert all(paid_den(cf) for cf in normalized_full)
 new_constraints.append((selection,pp,normalized_full))
 deg=ydegree(R(pp));lead=zz
 for mm,cc in pp.to_dict().items():
  assert mm[2]==mm[4]==mm[5]==mm[6]==mm[7]==0
  if int(mm[3])==deg:lead+=cc*ep**int(mm[0])*kp**int(mm[1])
 leading,leadpaid,leadhist=strip(lead);assert lead==leading*leadpaid
 certbytes=json.dumps([mprofile(cf,0) for cf in normalized_full],separators=(',',':')).encode()
 say(stage='new_W_original_fixed_three_column_constant_cofactor',
     selection=selection,primitive=mprofile(R(pp),0),degreeY=deg,
     paidRemoved=hist,leadingPaidRemoved=leadhist,
     unpaidLeading=mprofile(R(leading),8192),
     originalSixCoefficientProfileBytes=len(certbytes),
     originalSixCoefficientProfileSHA256=hashlib.sha256(certbytes).hexdigest(),
     allThreeColumnProductsAndAllSixOriginalCombinationProductsActuallyVerified=True,
     allLeadingZeroFibersRetained=True,constantNonzeroWeightPolynomial=deg==0,claimExcluded=False)

# New mathematical input starts here. The first earlier cofactor has globally
# paid y leading, so this step retains every specialization of the other rows.
ctx3=fmpq_mpoly_ctx.get(('e','k','y'),'lex');e3,k3,y3=ctx3.gens()
def shrink3(pp):
 rows={}
 for mm,cf in pp.to_dict().items():
  assert mm[2]==mm[4]==mm[5]==mm[6]==mm[7]==0
  rows[(int(mm[0]),int(mm[1]),int(mm[3]))]=cf
 ans=ctx3.from_dict(rows)
 assert expand3(ans)==pp
 return ans
def expand3(pp):
 return ctx.from_dict({(int(mm[0]),int(mm[1]),0,int(mm[2]),0,0,0,0):cf for mm,cf in pp.to_dict().items()})
def ypcoef(pp,j):
 return ctx3.from_dict({(int(mm[0]),int(mm[1]),0):cf for mm,cf in pp.to_dict().items() if int(mm[2])==j})
def ydeg3(pp):return max((int(mm[2]) for mm in pp.to_dict()),default=-1)
def profile3(pp,cap=8192):
 data=[[list(map(int,mm)),str(cf)] for mm,cf in sorted(pp.to_dict().items())]
 bb=json.dumps(data,separators=(',',':')).encode()
 out=dict(degrees=list(map(int,pp.degrees())),terms=len(data),totalDegree=int(pp.total_degree()),
          exactCoefficientBytes=len(bb),exactCoefficientSHA256=hashlib.sha256(bb).hexdigest())
 if len(bb)<=cap:out['exactCoefficients']=data
 return out
def weight_strip3(pp):
 old=expand3(pp);rem,paid,hist=strip(old)
 out=shrink3(rem);factor=shrink3(paid)
 assert out*factor==pp
 return out,factor,hist
assert len(new_constraints)==3
polys=[shrink3(v[1]) for v in new_constraints]
assert all(ydeg3(v)==6 for v in polys)
a0=ypcoef(polys[0],6)
aa0,paid0,hist0=weight_strip3(a0)
assert aa0==ctx3.constant(-1024)
assert paid_den(1/R(expand3(a0)))
say(stage='new_W_exact_monic_y_six_parameter_projection_input',
 monicDefinition='F0/lc_y(F0)',originalF0=profile3(polys[0],0),
 completeLeading=profile3(a0,0),paidLeadingRemoved=hist0,
 remainingLeadingConstant=str(aa0),firstDegreeSixMaintainedOnEntirePaidChart=True,
 bothOtherLeadingZeroFacesRetained=True,claimExcluded=False)
projected=[]
for i in [1,2]:
 ai=ypcoef(polys[i],6)
 raw=polys[i]*a0-polys[0]*ai
 assert ydeg3(raw)<=5
 pi,removed,hist=weight_strip3(raw)
 assert pi*removed==raw and paid_den(1/R(expand3(removed)))
 assert polys[i]*a0==pi*removed+polys[0]*ai
 n=ydeg3(pi);m=6
 say(stage='new_W_exact_original_degree_five_parameter_input',
     index=i,sourceRows=new_constraints[i][0],profile=profile3(pi,0),
     exactPseudoRemainderIdentity='paid*a_i_remainder = lc(F0)*Fi-lc(Fi)*F0',
     paidRemoved=hist,fullOldOriginalTracesRetainedByExactLinearCombination=True,
     noOtherLeadingInverse=True,allOtherLeadingZeroFacesRetained=True,claimExcluded=False)
 if not pi:
  say(stage='new_W_parameter_projection_zero_remainder',index=i,
      polynomialIdentityActuallyZero=True,weightCurveNotObtained=True,claimExcluded=False)
  continue
 assert n>=0
 # Full fixed-degree Sylvester construction. At any common original y value,
 # the same powers (1,y,...,y^(m+n-1)) annihilate this entire square row matrix.
 # The first polynomial's leading is a paid unit, so its degree stays six.
 bcols=[y3**j for j in range(m+n)]
 syrows=[]
 for original_poly,count in [(polys[0],n),(pi,m)]:
  for shift in range(count):
   pp=original_poly*y3**shift
   rr=[ypcoef(pp,j) for j in range(m+n)]
   assert sum((rr[j]*bcols[j] for j in range(m+n)),ctx3.constant(0))==pp
   syrows.append(rr)
 assert len(syrows)==m+n
 say(stage='new_W_original_fixed_Sylvester_QQ_begin',index=i,
     inputDegrees=[m,n],matrixSize=m+n,
     allFixedRowsExactlyReturnedToOriginalUnivariateInputs=True,
     coefficientsOnly_e_k=True,library='python-flint 0.9.0 fmpq_mpoly.resultant',
     noBezoutCoefficientCertificateClaim=True,claimExcluded=False)
 started=time.perf_counter()
 res=polys[0].resultant(pi,'y')
 elapsed=time.perf_counter()-started
 assert all(int(mm[2])==0 for mm in res.to_dict())
 if not res:
  say(stage='new_W_original_fixed_Sylvester_QQ_resultant_zero',index=i,
      secondsInResultant=elapsed,exactResultantZero=True,
      parameterEmptinessNotClaimed=True,claimExcluded=False)
  continue
 rem,paid,hist=weight_strip3(res)
 assert rem*paid==res
 lc=rem.coefficient(0);normalized=rem/lc
 assert normalized*lc==rem
 projected.append((i,normalized))
 say(stage='new_W_original_full_QQ_weight_parameter_curve',
     index=i,inputDegrees=[m,n],fixedSylvesterSize=m+n,
     secondsInResultant=elapsed,raw=profile3(res,0),
     paidRemoved=hist,remaining=profile3(normalized),
     exactContentNormalization=(str(lc) if len(str(lc))<=2048 else dict(bytes=len(str(lc)),sha256=hashlib.sha256(str(lc).encode()).hexdigest())),
     allPaidRemovalProductsActuallyVerified=True,
     originalSamePointCommonRootImpliesThisCurve=True,
     noNewLeadingZeroFaceRemoved=True,noFinitePointEmptinessClaim=True,claimExcluded=False)
if len(projected)==2:
 p1=projected[0][1];p2=projected[1][1]
 gg=p1.gcd(p2)
 assert (p1/gg)*gg==p1 and (p2/gg)*gg==p2
 # GCD=1 gives finite parameter intersection, never emptiness.
 say(stage='new_W_two_original_parameter_curves_intersection',
     curveIndices=[projected[0][0],projected[1][0]],
     gcd=profile3(gg),gcdConstant=gg.total_degree()==0,
     totalDegreeBounds=[int(p1.total_degree()),int(p2.total_degree())],
     finiteIntersectionIfGcdConstant=True,
     multivariateGcdOneNotUsedAsEmptiness=True,claimExcluded=False)
signal.alarm(0)
say(stage='new_W_monic_y_six_new_original_QQ_parameter_projection_complete',
     sourceSHA256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
     numberOfNonzeroFullQQParameterCurves=len(projected),
     allSourceCofactorTracesPreserved=True,
     allUnpaidLeadingZeroFacesRetained=True,
     noDPhysicalOrNewNormInverse=True,fullOriginalExclusionClaim=False,
     claimExcluded=False,peakRssKiB=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)
