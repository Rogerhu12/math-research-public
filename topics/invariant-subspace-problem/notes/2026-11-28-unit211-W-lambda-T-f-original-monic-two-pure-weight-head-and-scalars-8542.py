#!/usr/bin/env python3
"""NEW W free (lambda,T,f) ORIGINAL mean input.
Explicit globally monic f^2 from the two TRUE singleton means, then all
three independent original mean/N1 remainders and their f multiples.
NEW pure-weight f head, three pair cofactors and three SAME-f norms; every actual four-source
multiplier is returned after content cancellation. No original equation,
new head, f, lambda, T, D or norm is inverted. Every unproved zero face stays.
No native/alpha/chi/old scalar/resultant or old norm gate is replayed.
180 seconds / 4 GiB; self-contained; output definitions/SHA only.
"""
import hashlib,json,resource,signal,time
from pathlib import Path
from flint import fmpq_mpoly_ctx
START=time.perf_counter()
resource.setrlimit(resource.RLIMIT_AS,(4*1024**3,4*1024**3))
signal.setitimer(signal.ITIMER_REAL,180)
def say(stage,**data):
 data.update(stage=stage,seconds=time.perf_counter()-START)
 print(json.dumps(data,separators=(',',':')),flush=True)
ctx=fmpq_mpoly_ctx.get(('e','k','lam','T','f'),'lex')
ep,kp,lp,tp,fp=ctx.gens();Z=ctx.constant(0);O=ctx.constant(1)
def polynomial(v):return v if hasattr(v,'to_dict') else ctx.constant(v)
class R:
 def __init__(self,n=0,d=None,reduce=True):
  if isinstance(n,R):self.n=n.n;self.d=n.d;return
  n=polynomial(n);d=O if d is None else polynomial(d);assert d
  if not n:self.n=Z;self.d=O;return
  if reduce:
   g=n.gcd(d);n=n/g;d=d/g
  s=d.coefficient(0);self.n=n/s;self.d=d/s
 def __bool__(self):return bool(self.n)
 def __add__(self,v):
  v=R(v)
  if not self:return v
  if not v:return self
  g=self.d.gcd(v.d);a=self.d/g;b=v.d/g
  return R(self.n*b+v.n*a,a*v.d)
 __radd__=__add__
 def __neg__(self):return R(-self.n,self.d,False)
 def __sub__(self,v):return self+-R(v)
 def __rsub__(self,v):return R(v)+-self
 def __mul__(self,v):
  v=R(v)
  if not self or not v:return R()
  g=self.n.gcd(v.d);h=v.n.gcd(self.d)
  return R((self.n/g)*(v.n/h),(self.d/h)*(v.d/g),False)
 __rmul__=__mul__
 def __truediv__(self,v):
  v=R(v);assert v
  return self*R(v.d,v.n,False)
 def __rtruediv__(self,v):return R(v)/self
 def __pow__(self,n):
  assert isinstance(n,int) and n>=0
  return R(self.n**n,self.d**n,False)
 def __eq__(self,v):
  v=R(v);return self.n*v.d==v.n*self.d

e,k,lam,T,f=map(R,(ep,kp,lp,tp,fp))
u=e+1;Q=e*k;Vbar=u*k+2;delta=1-Q
ell=u*((k+2)**2-2*e*k)/(k*Vbar)
m=u-ell;theta=u-ell*Q;V2=2*u-ell*Q
M=ell*V2-u*u;bc=M/(4*delta)
T0=V2-2*u*u;J=2*u*(1-u)+ell*Q
Phi=T0+4*u-4+Q;Pf=T0*(J-Q)
P02=(2-3*u)*V2-Q*u+2*u**3
assert M==ell*ell*delta-m*m
assert J*Phi-Pf==2*u*Q*Phi
beta=2*u-J/Q
assert u-beta==-u*e*(k+4)/Vbar
assert u-beta==u*Phi/(2*e)
G=lam*P02-(1-u)*T0
Pc=Q*P02*(ell+T)-G*T0
t=-(Pf*f+Pc)/(bc*Q*Phi)
V=(J*f-G+bc*Q*t)/Q
W1=T0/2+2*u*f
x=(theta*V-m*W1)/M
y=(ell*W1-u*V)/M
A1=2*f-2*V+2*bc*t

statistics={'exactPolynomialDivisionProducts':0,
 'originalFCoefficientReturns':0,'paidSupportProducts':0,
 'fourSourceContentCancellations':0,'sameFNormIdentities':0}
def exact(p,g):
 out,rem=divmod(p,g);assert not rem and out*g==p
 statistics['exactPolynomialDivisionProducts']+=1
 return out
def weight(p):
 return all(all(int(ex[j])==0 for j in (2,3,4)) for ex in p.to_dict())
def f_free(p):return all(int(ex[4])==0 for ex in p.to_dict())
def fdeg(v):
 v=R(v);assert weight(v.d)
 return max((int(ex[4]) for ex in v.n.to_dict()),default=-1)
def fc(v,j):
 v=R(v);assert weight(v.d)
 return R(ctx.from_dict({(int(ex[0]),int(ex[1]),int(ex[2]),int(ex[3]),0):c
       for ex,c in v.n.to_dict().items() if int(ex[4])==j}),v.d)
def geomdegree(v):
 v=R(v);assert weight(v.d)
 return max((sum(int(ex[j]) for j in (2,3,4))
      for ex in v.n.to_dict()),default=-1)
def profile(p):
 data=[[list(map(int,ex)),str(c)] for ex,c in sorted(p.to_dict().items())]
 raw=json.dumps(data,separators=(',',':')).encode()
 return {'zero':not bool(p),
  'degrees_e_k_lambda_T_f':list(map(int,p.degrees())) if p else [-1]*5,
  'totalDegree':int(p.total_degree()) if p else -1,'terms':len(data),
  'bytes':len(raw),'sha256':hashlib.sha256(raw).hexdigest()}
# Only the currently proved pure-weight W supports. Neither E1=EW,
# nor any new lambda,T,f head nor D is assumed.
paid_atoms=[('e',ep),('k',kp),('u',ep+1),('delta',ep*kp-1),
 ('Vbar',(ep+1)*kp+2),('Phi_k_plus_four',kp+4),('P02',P02.n),
 ('M',M.n),('whole_equal_weights_k_plus_two',kp+2),
 ('whole_ell_zero',ell.n),('whole_equal_weights_m',m.n),
 ('whole_original_Lhalf',(2*ell-1).n)]
def strip(p):
 if not p:return p,O,[]
 before=p;removed=O;history=[]
 for label,atom in paid_atoms:
  assert atom and weight(atom)
  layers=0
  while p:
   gg=p.gcd(atom)
   if int(gg.total_degree())==0:break
   p=exact(p,gg);removed*=gg;layers+=1
   statistics['paidSupportProducts']+=1
  if layers:history.append({'paidSupport':label,'gcdLayers':layers})
 assert p*removed==before
 return p,removed,history
den_seen=set()
def paid(p):
 assert p and weight(p)
 key=str(p)
 if key in den_seen:return
 rr,_,_=strip(p);assert rr and int(rr.total_degree())==0
 den_seen.add(key)
def ck(v):
 v=R(v);paid(v.d);return v
for v in [u,Q,Vbar,delta,ell,m,M,bc,Phi,P02,t,V,W1,x,y,A1]:
 ck(v)
assert fc(t,1)==beta/bc and fc(V,1)==2*u and fc(W1,1)==2*u
assert fc(x,1)==2*u*ell*delta/M and fc(y,1)==-2*u*m/M

# Actual quadratic extension and TRUE dual-number Gram. No compact
# derivative-square replacement is used anywhere in this source.
class E:
 def __init__(self,a=0,b=0):
  if isinstance(a,E):self.a=a.a;self.b=a.b;return
  self.a=R(a);self.b=R(b)
 def __bool__(self):return bool(self.a) or bool(self.b)
 def __add__(self,v):
  v=E(v);return E(self.a+v.a,self.b+v.b)
 __radd__=__add__
 def __neg__(self):return E(-self.a,-self.b)
 def __sub__(self,v):return self+-E(v)
 def __rsub__(self,v):return E(v)+-self
 def __mul__(self,v):
  v=E(v);return E(self.a*v.a+delta*self.b*v.b,self.a*v.b+self.b*v.a)
 __rmul__=__mul__
 def __truediv__(self,v):
  v=R(v);return E(self.a/v,self.b/v)
 def __pow__(self,n):
  assert isinstance(n,int) and n>=0
  out=E(1)
  for _ in range(n):out=out*self
  return out
 def __eq__(self,v):
  v=E(v);return self.a==v.a and self.b==v.b
 def conj(self):return E(self.a,-self.b)
b=E(ell/2,m/(2*delta));c=b.conj();a=E(1-ell)
p=E(1,1);q=p.conj();X=E(x,y);Y=X.conj()
assert b*c==E(bc)
assert b*X+c*Y==E(V)
assert b*p*X+c*q*Y==E(W1)
r=X-a*p-c*E(t);s=Y-a*q-b*E(t)
rows=[[E(),E(),p,q],[E(),E(A1),r,s],
      [p,r,E(),E(t)],[q,s,E(t),E()]]
one=[E(1),E(),E(1),E(1)]
def va(v,z):return [a+b for a,b in zip(v,z)]
def vs(h,v):return [h*a for a in v]
def vm(v,z):
 return [v[0]*z[0],v[0]*z[1]+v[1]*z[0],v[2]*z[2],v[3]*z[3]]
def tau(v):return a*v[0]+v[1]+b*v[2]+c*v[3]
def DK(v):return [tau(vm(row,v)) for row in rows]
d=DK(one);F2=tau(d);Kd=DK(d)
assert d==[E(u),E(2*f-V-(1-ell)*u),X,Y]
assert F2==E(2*f)
def mean(j):
 sq=2*tau(vm(rows[0],rows[1])) if j==1 else tau(vm(rows[j],rows[j]))
 return sq-2*Kd[j]-2*vm(d,d)[j]+2*F2*d[j]
E0=mean(0);E1=mean(1);EB=mean(2);EC=mean(3)
assert not E0 and not E1.b and EC==EB.conj()
# Full singleton expression checks 2*p*r, never r*r.
EB_direct=(a*p*p+2*p*r+c*E(t*t)
 -2*(a*p*E(u)+p*d[1]+r*E(u)+c*E(t)*Y)-2*X*X+4*E(f)*X)
assert EB==EB_direct

def N4(v):
 return (2*tau(vm(d,vm(v,v)))-F2*tau(vm(v,v))
   -4*tau(v)*tau(vm(d,v))+2*F2*tau(v)**2+tau(vm(v,DK(v))))
v0=rows[0];v1=rows[1]
Npolar=N4(va(v0,v1))-N4(v0)-N4(v1)
v0c=va(v0,vs(-tau(v0),one));v1c=va(v1,vs(-tau(v1),one))
Pjet=3*tau(vm(vm(v0c,v0c),v1c))
w=lam-1-T
assert N4(v0)==E(2*lam*P02)
assert Pjet==E(3*w*P02)
N1=Npolar-E(4*lam*w*P02)
assert not N1.b
original=[E1.a,EB.a,EB.b,N1.a]
assert all(geomdegree(v)<=2 for v in original)
for v in original:ck(v)
say('new_free_lambda_T_f_TRUE_original_I4',
 originalNames=['E1','EBe','EBo','N1'],
 originalNumerators=[profile(v.n) for v in original],
 originalDenominators=[profile(v.d) for v in original],
 E0_N0_PjetFullOriginalIdentitiesReturned=True,
 singletonFullMeanDirectTwo_p_rReturned=True,
 E1KeptIndependentOfWeightedMean=True,
 noNativeOrOldScalarReplayed=True)

# Explicit whole-W monic f^2. No choice of a nonzero unknown head.
cf=bc/(2*u*(u-beta))
qtag=[R(),cf,cf*ell*delta/m,R()]
qf=sum((qtag[i]*original[i] for i in range(4)),R())
hBe=fc(original[1],2);hBo=fc(original[2],2)
assert hBe+ell*delta*hBo/m==2*u*(u-beta)/bc
hB=E(hBe,hBo);hC=hB.conj()
assert b*b*c*hB-b*c*c*hC==2*E(u*(u-beta))*(b-c)
assert fdeg(qf)==2 and fc(qf,2)==1 and geomdegree(qf)<=2
q0=fc(qf,0);q1=fc(qf,1)
assert qf==f*f+q1*f+q0
assert geomdegree(q0)<=2 and geomdegree(q1)<=1
for z in qtag+[qf,q0,q1,cf,1/cf]:ck(z)
def tagval(tag):
 return sum((tag[i]*original[i] for i in range(4)),R())
def original_return(value,tag):
 back=tagval(tag)
 assert back==value
 for j in range(max(fdeg(back),fdeg(value),0)+1):
  assert fc(back,j)==fc(value,j)
  statistics['originalFCoefficientReturns']+=1
original_return(qf,qtag)
# Also the exact reverse change of original generators.
assert original[1]==qf/cf-(ell*delta/m)*original[2]
say('new_global_explicit_monic_f_two',
 qfNumerator=profile(qf.n),qfDenominator=profile(qf.d),
 q0=profile(q0.n),q1=profile(q1.n),
 wholeWOldWeightUnit_uMinusBeta=True,
 exactOriginalFourSourceReturn=True,
 EBeReverseChangeReturned=True,
 noNewLambda_T_f_HeadOrNormInverse=True)

rowdata=[];six=[]
for j in (0,2,3):
 h=fc(original[j],2)
 tag=[(R(1) if i==j else R())-h*qtag[i] for i in range(4)]
 rv=original[j]-h*qf
 A=fc(rv,0);B=fc(rv,1)
 assert rv==A+B*f and geomdegree(A)<=2 and geomdegree(B)<=1
 original_return(rv,tag)
 assert original[j]==rv+h*qf
 # TRUE f multiple in the same monic environment, with original tag.
 mul=-q0*B+(A-q1*B)*f
 mtag=[f*tag[i]-B*qtag[i] for i in range(4)]
 assert mul==f*rv-B*qf
 original_return(mul,mtag)
 for z in [rv,A,B,mul]+tag+mtag:ck(z)
 label=['E1','EBe','EBo','N1'][j]
 rowdata.append({'name':label,'value':rv,'tag':tag,'A':A,'B':B})
 six.extend([(rv,tag),(mul,mtag)])
 say('new_complete_original_mean_row_and_f_multiple',
   name=label,row=[profile(A.n),profile(B.n)],
   fMultiple=[profile((-q0*B).n),profile((A-q1*B).n)],
   originalFourSourceCoefficientsReturned=True,
   reverseOriginalGeneratorReturned=True)
assert len(six)==6
say('new_exact_I4_six_by_two_complete',
 sameMonicFEnvironment=True,fullOriginalI4Equivalent=True,
 rowCount=6,basis=['1','f'],
 originalQuotientNotAssumedFree=True,
 allCoefficientDenominatorsPaidPureWeights=True)


# NEW pure-weight head of the THREE f-linear original rows.
# Their B_i are affine in lambda,T by the proved degree filtration.
# A single exact specialization previously proved this weight determinant
# is not the zero rational function; here its full QQ definition is used.
Bmatrix=[]
for rr in rowdata:
 B=rr['B'];co=[]
 for dl,dT in ((0,0),(1,0),(0,1)):
  pp=ctx.from_dict({(ex[0],ex[1],0,0,0):c for ex,c in B.n.to_dict().items()
                   if int(ex[2])==dl and int(ex[3])==dT and int(ex[4])==0})
  co.append(R(pp,B.d))
 assert B==co[0]+co[1]*lam+co[2]*T
 for v in co:
  ck(v);assert weight(v.n)
 Bmatrix.append(co)
mu=[Bmatrix[1][1]*Bmatrix[2][2]-Bmatrix[1][2]*Bmatrix[2][1],
    Bmatrix[2][1]*Bmatrix[0][2]-Bmatrix[2][2]*Bmatrix[0][1],
    Bmatrix[0][1]*Bmatrix[1][2]-Bmatrix[0][2]*Bmatrix[1][1]]
rawhead=sum((mu[i]*Bmatrix[i][0] for i in range(3)),R())
assert rawhead and weight(rawhead.n)
assert not sum((mu[i]*Bmatrix[i][1] for i in range(3)),R())
assert not sum((mu[i]*Bmatrix[i][2] for i in range(3)),R())
rawline=sum((mu[i]*rowdata[i]['value'] for i in range(3)),R())
rawtag=[sum((mu[i]*rowdata[i]['tag'][j] for i in range(3)),R())
        for j in range(4)]
assert fc(rawline,1)==rawhead
original_return(rawline,rawtag)
den=O
for v in rawtag:
 ck(v);assert weight(v.n)
 den=exact(den,den.gcd(v.d))*v.d
paid(den)
nums=[v.n*exact(den,v.d) for v in rawtag]
common=Z
for pp in nums:common=common.gcd(pp)
assert common and weight(common)
lin_tag=[R(exact(pp,common)) for pp in nums]
lin_value=tagval(lin_tag)
assert R(common)*lin_value==R(den)*rawline
assert fdeg(lin_value)==1
original_return(lin_value,lin_tag)
fhead=fc(lin_value,1);fconstant=fc(lin_value,0)
assert fhead and weight(fhead.n)
assert geomdegree(fconstant)<=2
for v in [fhead,fconstant]+lin_tag:ck(v)
core,removed,history=strip(fhead.n)
assert core and core*removed==fhead.n
lc=core.coefficient(0);core/=lc;removed*=lc
head_constant,head_factors=core.factor()
head_back=ctx.constant(head_constant)
for ff,nn in head_factors:head_back*=ff**int(nn)
assert head_back==core
say('new_full_QQ_pure_weight_f_head_original_cofactor',
 rawHead=profile(rawhead.n),rawHeadDenominator=profile(rawhead.d),
 allThreeCoefficientMatrixCoordinatesReturned=True,
 actualFourOriginalMultiplierCommon=profile(common),
 finalHeadNumerator=profile(fhead.n),finalHeadDenominator=profile(fhead.d),
 retainedWeightHead=profile(core),
 onlyOldPaidWeightGcdLayers=history,
 completeQQFactorization=[{'factor':profile(ff),'multiplicity':int(nn)}
                          for ff,nn in head_factors],
 allFourOriginalSourceCoefficientsReturned=True,
 originalRelation='fhead*f+fconstant is in original I4',
 entireRetainedHeadZeroLocusKept=True,
 fullHeadIsAlreadyPaid=int(core.total_degree())==0)
if int(core.total_degree())==0:
 paid(fhead.n)
 g=fconstant/fhead
 monic_tag=[v/fhead for v in lin_tag]
 original_return(f+g,monic_tag)
 # This is an exact elimination, only in the proven full paid-head case.
 # The same f is used for qf AND all three original mean/N1 remainders.
 residuals=[]
 value=g*g-q1*g+q0
 qres_tag=[qtag[j]-(f+q1-g)*monic_tag[j] for j in range(4)]
 original_return(value,qres_tag);residuals.append(value)
 for rr in rowdata:
  value=rr['A']-rr['B']*g
  tag=[rr['tag'][j]-rr['B']*monic_tag[j] for j in range(4)]
  original_return(value,tag);residuals.append(value)
 say('new_whole_W_unique_f_and_exact_four_pure_mean_conditions',
  originalRelation='f=-g(lambda,T)',gNumerator=profile(g.n),gDenominator=profile(g.d),
  allOriginalFourSourceIdentitiesReturned=True,
  allRemainingScalarProfiles=[profile(v.n) for v in residuals],
  exactI4EliminationNotOnlyPairCompatibility=True,
  noNewUnpaidHeadOrGeometryInverse=True)

# For each new scalar, cancel only the common factor of ALL FOUR actual
# original multipliers, then return the full original f identity.
def primitive_scalar(label,value,tag,geomcap):
 original_return(value,tag)
 assert fdeg(value)<=0 and geomdegree(value)<=geomcap
 den=O
 for h in tag:
  ck(h);den=exact(den,den.gcd(h.d))*h.d
 paid(den)
 nums=[h.n*exact(den,h.d) for h in tag]
 common=Z
 for h in nums:common=common.gcd(h)
 if not common:
  assert not value
  say('new_scalar_identically_zero',label=label,
      noEmptyOrFiniteConclusion=True)
  return R(),[R() for _ in range(4)]
 prim=[R(exact(h,common)) for h in nums]
 out=tagval(prim)
 assert R(common)*out==R(den)*value
 assert fdeg(out)<=0 and geomdegree(out)<=geomcap
 original_return(out,prim)
 statistics['fourSourceContentCancellations']+=1
 ck(out)
 pp,removed,hist=strip(out.n)
 if pp:
  lc=pp.coefficient(0);pp/=lc;removed*=lc
 assert pp*removed==out.n
 paid(removed)
 final=R(pp);finaltag=[R(out.d,removed)*h for h in prim]
 original_return(final,finaltag)
 say('new_necessary_lambda_T_original_scalar',
    label=label,numerator=profile(pp),
    geometryDegree=geomdegree(final),
    actualFourMultiplierCommon=profile(common),
    onlyPaidWeightSupportRemoved=hist,
    originalFourSourceReturn=True,
    allUnpaidCommonAndHeadZeroFacesKept=True,
    noNewGeometryInverse=True)
 return final,finaltag

targets=[]
for i,j in ((0,1),(0,2),(1,2)):
 ri,rj=rowdata[i],rowdata[j]
 value=rj['B']*ri['value']-ri['B']*rj['value']
 tag=[rj['B']*ri['tag'][h]-ri['B']*rj['tag'][h] for h in range(4)]
 assert value==ri['A']*rj['B']-rj['A']*ri['B']
 scalar,stag=primitive_scalar('pair_'+ri['name']+'_'+rj['name'],value,tag,3)
 targets.append((scalar,stag))

# Same-f compatibility is retained explicitly: these norms come from qf
# and the very same row, not a different chosen f root for each equation.
for rr in rowdata:
 A=rr['A'];B=rr['B'];mult=A-q1*B-B*f
 value=A*A-q1*A*B+q0*B*B
 assert value==mult*rr['value']+B*B*qf
 tag=[mult*rr['tag'][h]+B*B*qtag[h] for h in range(4)]
 statistics['sameFNormIdentities']+=1
 scalar,stag=primitive_scalar('same_f_norm_'+rr['name'],value,tag,4)
 targets.append((scalar,stag))
assert len(targets)==6
say('new_original_I4_two_column_and_six_scalars_complete',
 statistics=statistics,distinctPaidDenominatorsChecked=len(den_seen),
 necessaryScalarProfiles=[profile(v.n) for v,_ in targets],
 actualFullSixRowOriginalPresentation=True,
 allThreePairsAndAllThreeSameFNormsReturned=True,
 pairOrNormListAloneNotClaimedSufficient=True,
 noNewWeightProjectionOrEmptyConclusion=True,
 noPureValueResultantOrOldNormReplayed=True,
 maxRssKiB=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)
signal.setitimer(signal.ITIMER_REAL,0)
