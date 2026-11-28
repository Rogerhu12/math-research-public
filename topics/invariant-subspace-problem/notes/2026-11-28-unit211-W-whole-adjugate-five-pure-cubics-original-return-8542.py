#!/usr/bin/env python3
"""NEW whole W: five original pure (lambda,T) CUBICS, no new head inverse.
Use only the already-published necessary true Gram/qf/three-row/g
definitions. Do not run the old six scalar or full eleven pure-row gate.
The new adjugate uses the whole raw 3x3 weight matrix and never assumes its
determinant a unit. All five NEW pure cubics return complete four/six
original source vectors and all f coefficients. Full existing I11 remains;
these five necessary cubics alone are NOT asserted equivalent.
Only source/parameter definitions/profiles/SHA, no coefficient cache.
180 seconds / 4 GiB, self-contained, no dependencies.
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

statistics.update(newMonicFDivisionProducts=0,newSixSourceCoefficientReturns=0,
                  newElevenSourceCoefficientReturns=0)
# This is the fixed OLD mathematical G36 definition, not a new output cache.
# Original source blob c489948be8e967575417a1e21de51cd5a915dc80,
# SHA256 3ec9b206da1dbde4103ebf7633e725e4cf5b8518055ac8f0945d7ba6a1e24a22.
# Entire original paid theorem:
# R150-appendix-unit211-W-G36-entire-original-exclusion-and-global-F-recovery.md
G36p=4096+9216*kp+7680*kp**2+3072*kp**3+592*kp**4+24*kp**5-10*kp**6-1*kp**7-6144*ep*kp-16128*ep*kp**2-14336*ep*kp**3-6048*ep*kp**4-1416*ep*kp**5-186*ep*kp**6-9*ep*kp**7+512*ep**2*kp**2+6016*ep**2*kp**3+6560*ep**2*kp**4+2528*ep**2*kp**5+468*ep**2*kp**6+50*ep**2*kp**7+2*ep**2*kp**8+1792*ep**3*kp**3+832*ep**3*kp**4-832*ep**3*kp**5-392*ep**3*kp**6-50*ep**3*kp**7-2*ep**3*kp**8-256*ep**4*kp**4-544*ep**4*kp**5-24*ep**4*kp**6+24*ep**4*kp**7+4*ep**4*kp**8-192*ep**5*kp**5-8*ep**5*kp**7+32*ep**6*kp**6
assert profile(G36p)['sha256']=='994fe0821fb8c70e7f82edf8aea19a17ee1ffa99fd5fd4b5b3c065daea84ad78'
paid_atoms += [('whole_J_equals_Q_two_e_plus_one',2*ep+1),
               ('whole_original_G36',G36p)]
# (J-Q)*Vbar=-2e^2*k*(2e+1), same old W domain.
assert (J-Q)*Vbar==-2*e*e*k*(2*e+1)

# Necessary old qf/three remainders/head DEFINITIONS only. No old f-multiple
# generation, old six scalar gate, or old head factorization is repeated.
cf=bc/(2*u*(u-beta))
qtag=[R(),cf,cf*ell*delta/m,R()]
qf=sum((qtag[i]*original[i] for i in range(4)),R())
q0=fc(qf,0);q1=fc(qf,1)
assert qf==f*f+q1*f+q0
rowdata=[]
for j in (0,2,3):
 hh=fc(original[j],2)
 rr=original[j]-hh*qf
 aa=fc(rr,0);bb=fc(rr,1)
 assert rr==aa+bb*f and geomdegree(aa)<=2 and geomdegree(bb)<=1
 tt=[(R(1) if i==j else R())-hh*qtag[i] for i in range(4)]
 rowdata.append(dict(A=aa,B=bb,value=rr,tag=tt,originalIndex=j))
Bmatrix=[]
for rr in rowdata:
 bb=rr['B'];co=[]
 for dl,dT in [(0,0),(1,0),(0,1)]:
  pp=ctx.from_dict({(int(ex[0]),int(ex[1]),0,0,0):cc
       for ex,cc in bb.n.to_dict().items()
       if int(ex[2])==dl and int(ex[3])==dT and int(ex[4])==0})
  co.append(R(pp,bb.d))
 assert bb==co[0]+co[1]*lam+co[2]*T
 Bmatrix.append(co)
mu=[Bmatrix[1][1]*Bmatrix[2][2]-Bmatrix[1][2]*Bmatrix[2][1],
    Bmatrix[2][1]*Bmatrix[0][2]-Bmatrix[2][2]*Bmatrix[0][1],
    Bmatrix[0][1]*Bmatrix[1][2]-Bmatrix[0][2]*Bmatrix[1][1]]
hh=sum((mu[i]*Bmatrix[i][0] for i in range(3)),R())
aa=sum((mu[i]*rowdata[i]['A'] for i in range(3)),R())
assert hh and weight(hh.n)
ck(hh);ck(aa)
# hh may contain a common factor removed from ALL old source multipliers.
# Work as rational functions, cancel exactly, then check the FINAL g/rtag
# denominators as old paid weights and return the whole identity. No
# physical hh!=0 condition is imposed.
g=ck(aa/hh)
rline=f+g
rtag=[ck(sum((mu[i]*rowdata[i]['tag'][j] for i in range(3)),R())/hh)
      for j in range(4)]
assert geomdegree(g)<=2
assert sum((rtag[i]*original[i] for i in range(4)),R())==rline

statistics.update(newAdjugateMatrixCoordinates=0,newAdjugateOriginalRows=0,
 newCubicOriginalReturns=0,newCubicFCoefficientReturns=0,
 newQuadraticDecompositions=0,newNPMonicDivisionProducts=0)
def det2(A):
 return A[0][0]*A[1][1]-A[0][1]*A[1][0]
adj=[]
for ii in range(3):
 row=[]
 for jj in range(3):
  # adj_ij is the cofactor obtained by deleting ORIGINAL row j, column i.
  minor=[[Bmatrix[r][c] for c in range(3) if c!=ii]
         for r in range(3) if r!=jj]
  row.append(ck((1 if (ii+jj)%2==0 else -1)*det2(minor)))
 adj.append(row)
DeltaB=hh
assert adj[0]==mu
for left,right in [(adj,Bmatrix),(Bmatrix,adj)]:
 for ii in range(3):
  for jj in range(3):
   value=sum((left[ii][z]*right[z][jj] for z in range(3)),R())
   assert value==(DeltaB if ii==jj else R())
   statistics['newAdjugateMatrixCoordinates']+=1
C=[];Atag=[]
for ii,axis in enumerate([R(1),lam,T]):
 cc=ck(sum((adj[ii][j]*rowdata[j]['A'] for j in range(3)),R()))
 tag=[ck(sum((adj[ii][j]*rowdata[j]['tag'][z]
             for j in range(3)),R())) for z in range(4)]
 back=sum((tag[z]*original[z] for z in range(4)),R())
 assert back==cc+DeltaB*axis*f
 assert geomdegree(cc)<=2 and fdeg(cc)<=0
 C.append(cc);Atag.append(tag)
 statistics['newAdjugateOriginalRows']+=1
assert C[0]==DeltaB*g
assert geomdegree(q1)<=1 and geomdegree(q0)<=2
say('new_full_weight_adjugate_original_rows',
    determinantNumerator=profile(DeltaB.n),
    determinantDenominator=profile(DeltaB.d),
    determinantNeverAssumedPaid=True,adjugateBothSidesReturned=True,
    allThreeRowsReturnedToOriginalFour=True,
    oldSameFOnlyUsesItsFinalPaidDenominators=True)

def quad_decompose(v):
 v=ck(v)
 assert fdeg(v)<=0 and geomdegree(v)<=2
 coefficients={}
 for ij in [(0,0),(1,0),(0,1),(2,0),(1,1),(0,2)]:
  il,it=ij
  coefficients[ij]=R(ctx.from_dict({
   (int(ex[0]),int(ex[1]),0,0,0):cc
   for ex,cc in v.n.to_dict().items()
   if int(ex[2])==il and int(ex[3])==it and int(ex[4])==0}),v.d)
 back=sum((cv*lam**ij[0]*T**ij[1]
            for ij,cv in coefficients.items()),R())
 assert back==v
 c00=coefficients[(0,0)]
 Ll=coefficients[(2,0)]*lam+coefficients[(1,1)]*T+coefficients[(1,0)]
 Lt=coefficients[(0,2)]*T+coefficients[(0,1)]
 assert v==c00+lam*Ll+T*Lt
 assert geomdegree(Ll)<=1 and geomdegree(Lt)<=1
 for vv in [c00,Ll,Lt]:ck(vv)
 statistics['newQuadraticDecompositions']+=1
 return c00,Ll,Lt

newvalues=[];newtags=[];newnames=[]
def full_original_return(label,value,tag,gens):
 value=ck(value);tag=[ck(v) for v in tag]
 assert len(tag)==len(gens)
 back=sum((tag[j]*gens[j] for j in range(len(gens))),R())
 assert back==value
 for jj in range(max(fdeg(back),fdeg(value),0)+1):
  assert fc(back,jj)==fc(value,jj)
  statistics['newCubicFCoefficientReturns']+=1
 assert fdeg(value)<=0 and geomdegree(value)<=3
 statistics['newCubicOriginalReturns']+=1
 newnames.append(label);newvalues.append(value);newtags.append(tag)
 say('new_entire_W_pure_cubic_original_return',label=label,
     numerator=profile(value.n),denominator=profile(value.d),
     geometryDegree=geomdegree(value),originalSourceCount=len(gens),
     originalMultiplierNumerators=[profile(v.n) for v in tag],
     originalMultiplierDenominators=[profile(v.d) for v in tag],
     allOriginalCoordinatesAndFCoefficientsReturned=True,
     allFinalWeightDenominatorsAlreadyPaid=True,
     rawDeterminantZeroRetained=True)

Ul=ck(C[1]-DeltaB*lam*g)
Ut=ck(C[2]-DeltaB*T*g)
Utagl=[Atag[1][j]-DeltaB*lam*rtag[j] for j in range(4)]
Utagt=[Atag[2][j]-DeltaB*T*rtag[j] for j in range(4)]
full_original_return('U_lambda',Ul,Utagl,original)
full_original_return('U_T',Ut,Utagt,original)
g00,Gl,Gt=quad_decompose(g)
Gq=ck(DeltaB*(g00-q1)*g+Gl*C[1]+Gt*C[2]+DeltaB*q0)
# The identity is valid without dividing by DeltaB, even on DeltaB=0.
assert Gq==DeltaB*(g*g-q1*g+q0)+Gl*Ul+Gt*Ut
Gqtag=[DeltaB*qtag[j]+Gl*Atag[1][j]+Gt*Atag[2][j]
       -DeltaB*(f+q1-g00)*rtag[j] for j in range(4)]
full_original_return('Gamma_qf',Gq,Gqtag,original)

# Only the necessary raw NS/PS definitions for the two NEW cubic targets.
def P2(vv):
 vc=va(vv,vs(-tau(vv),one))
 return tau(vm(vm(vc,vc),vc))
A_lambda=2*lam*lam-2*lam+1
B_lambda=4*lam**3-6*lam*lam+3*lam-1
NB=N4(rows[2]);NC=N4(rows[3])
PB=P2(rows[2]);PC=P2(rows[3])
assert NC==NB.conj() and PC==PB.conj()
NSext=b*NB+c*NC-E(2*lam*P02*(ell+2*T+A_lambda))
PSext=b*PB+c*PC-E(P02*(ell+3*T+3*A_lambda+B_lambda))
assert not NSext.b and not PSext.b
NS=ck(NSext.a);PS=ck(PSext.a)
assert geomdegree(NS)<=3 and geomdegree(PS)<=3
assert geomdegree(NB.b)<=3 and geomdegree(PB.b)<=3
original6=original+[NS,PS]

def new_np_shortdivide(value):
 rem=R(value);quot=R()
 while fdeg(rem)>=2:
  olddeg=fdeg(rem);term=fc(rem,olddeg)*f**(olddeg-2)
  oldrem=rem;rem=rem-term*qf;quot=quot+term
  assert oldrem==term*qf+rem and fdeg(rem)<olddeg
  statistics['newNPMonicDivisionProducts']+=1
 aa=ck(fc(rem,0));bb=ck(fc(rem,1));quot=ck(quot)
 assert rem==aa+bb*f and value==quot*qf+aa+bb*f
 assert geomdegree(aa)<=3 and geomdegree(bb)<=2
 return quot,aa,bb

for sourceindex,(label,value) in enumerate([('Gamma_NS',NS),('Gamma_PS',PS)],4):
 quot,av,bv=new_np_shortdivide(value)
 b00,Bl,Bt=quad_decompose(bv)
 gamma=ck(DeltaB*(av-b00*g)-Bl*C[1]-Bt*C[2])
 assert gamma==DeltaB*(av-bv*g)-Bl*Ul-Bt*Ut
 tag=[]
 for j in range(6):
  entry=DeltaB*int(j==sourceindex)
  if j<4:
   entry=entry-DeltaB*quot*qtag[j]-Bl*Atag[1][j]-Bt*Atag[2][j]
   entry=entry-DeltaB*b00*rtag[j]
  tag.append(entry)
 full_original_return(label,gamma,tag,original6)

assert len(newvalues)==5 and len(newtags)==5
say('new_five_entire_W_necessary_cubics_complete',
    names=newnames,
    numerators=[profile(v.n) for v in newvalues],
    denominators=[profile(v.d) for v in newvalues],
    geometricTotalDegrees=[geomdegree(v) for v in newvalues],
    allFiveFullOriginalCombinationsReturned=True,
    noDeltaBInverseInNewConstruction=True,
    entireDeltaBZeroBranchRetained=True,
    noNewWeightOrGeometryHeadInverted=True,
    noUnpaidContentRemovedFromEquations=True,
    originalElevenPureConditionsStillRetained=True,
    fiveCubicsAloneNotClaimedEquivalent=True,
    noOldFullI11ReturnOrScalarNormGateReplayed=True,
    noResultantFactorizationOrNewRankGateRun=True,
    statistics=statistics,distinctPaidWeightDenominators=len(den_seen),
    sourceSHA256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
    maxRssKiB=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss,
    noLargeCoefficientCacheWritten=True,
    wholeWExcluded=False,ordinaryISPClaim=False)
signal.setitimer(signal.ITIMER_REAL,0)
