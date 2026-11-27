#!/usr/bin/env python3
"""NEW fifth P201 block: actual T,v relations and FULL original Gram values.

The completed same-Q/same-lambda/original-geometry quotient has residual
K_phi dimension one. Return T-Tbar and v-vbar from the original last
two coordinate rows, with a whole 10x10 original unit minor. Adjoin
rho^2=1-Q and a MONIC value quadratic for x=h_B-1:
 x^2-(2T/ell)x+(T^2-c*A2)/(b*ell)=0.
All inverses here are explicitly tested WHOLE residual weight units.
No physical D or moment discriminant is inverted; its double-root
specialization is retained. Add the actual cubic moment, all nine
original Gram equations, and the COMPLETE N4(V), in one 20-dimensional
finite original algebra. The full original product ideal must return
a selected matrix times its inverse before any block is excluded.
120s/1GiB. 2026-11-28 Asia/Taipei. No coefficient payload.
"""
import os,time,json,hashlib,signal,resource,contextlib,io
from pathlib import Path
from flint import nmod_poly,nmod_mat
START=time.perf_counter();DEADLINE=START+120;PRIME=1009
signal.alarm(120);resource.setrlimit(resource.RLIMIT_AS,(1024**3,1024**3))
def say(stage,**kw):
 kw.update(stage=stage,seconds=time.perf_counter()-START)
 print(json.dumps(kw,separators=(",",":")),flush=True)
def ident(obj):
 raw=json.dumps(obj,separators=(",",":")).encode()
 return dict(bytes=len(raw),sha256=hashlib.sha256(raw).hexdigest())
def pdigest(poly):
 out=ident([int(c) for c in poly.coeffs()]);out["degree"]=int(poly.degree());return out
def restore_deadline():
 signal.setitimer(signal.ITIMER_REAL,max(.001,DEADLINE-time.perf_counter()))
name="2026-11-28-unit211-Phi-zero-H1-P201-fifth-block-actual-lambda-and-original-Tv-8542.py"
sha="15a58c3d848d866e5feaf89a6a5cd939c265b8fe3c1a3f6788a2252c163ffa5b"
path=Path(os.environ.get("ISP_H1_P201_FIFTH_GEOMETRY_SOURCE",str(Path(__file__).with_name(name))))
raw=path.read_bytes();assert hashlib.sha256(raw).hexdigest()==sha
source=raw.decode();marker='\nsay("new_fifth_P201_actual_original_geometry_finished",'
assert source.count(marker)==1
prefix=source.split(marker,1)[0]
env={"__file__":str(path),"__name__":"__necessary_original_fifth_block_for_complete_Gram_values__"}
with contextlib.redirect_stdout(io.StringIO()):
 exec(compile(prefix,str(path)+":necessary-prefix","exec"),env)
restore_deadline()
assert env["rankK"]==2 and env["actual_rank"]==10 and env["d"]==5
phi=env["phi"];d=5;p=PRIME
zero,one,u=env["zero"],env["one"],env["u"]
kr,kmul,kinv=env["kr"],env["kmul"],env["kinv"]
qbar,lbar=env["qbar"],env["lbar"]
nodes,selected=env["nodes"],env["selected"]
assert len(selected)==2
# The first five rows are constants. The last ten are T and v coordinates.
columns=[]
for idx in selected:
 for a in range(d):
  vec=[kr(co*(u**a)) for co in nodes[idx]["vector"]]
  columns.append([int(c[j]) for c in vec for j in range(d)])
lower=nmod_mat([[columns[j][i] for j in range(10)] for i in range(d,3*d)],p)
inverse=lower.inv()
eye=nmod_mat(10,10,[1 if i==j else 0 for i in range(10) for j in range(10)],p)
assert lower*inverse==eye
full=nmod_mat([[columns[j][i] for j in range(10)] for i in range(3*d)],p)
relations=full*inverse
assert all(int(relations[d+i,j])==(1 if i==j else 0) for i in range(10) for j in range(10))
Tbar=kr(nmod_poly([(-int(relations[a,0]))%p for a in range(d)],p))
vbar=kr(nmod_poly([(-int(relations[a,d]))%p for a in range(d)],p))
for b,co in enumerate([Tbar,vbar]):
 for a in range(d):
  top=nmod_poly([int(relations[i,b*d+a]) for i in range(d)],p)
  assert kr(top+co*(u**a))==zero
row=[one,Tbar,vbar]
def pair(v):return kr(sum((a*b for a,b in zip(row,v)),zero))
assert all(pair(nd["vector"])==zero for nd in nodes)
for mat,value in [(env["MT"],Tbar),(env["MV"],vbar)]:
 assert all(kr(sum((row[i]*mat[i][j] for i in range(3)),zero))==kmul(value,row[j])
            for j in range(3))
say("new_fifth_P201_actual_original_T_v_linear_relations",
 actualP201Block=pdigest(phi),originalNonconstantGeometryUnitMinorOrder=10,
 actualSourceNodes=selected,
 unitMinorIdentity=ident([[int(lower[i,j]) for j in range(10)] for i in range(10)]),
 wholeOriginalMinorTimesInverseReturned=True,
 allTAndVTimesUOriginalCombinationFamiliesReturned=True,
 exactResidualT=pdigest(Tbar),exactResidualV=pdigest(vbar),
 allThirteenOriginalSourceNodesReturnedAtSamePoint=True,
 bothTrueMultiplicationEigenrowIdentitiesReturned=True,
 noQQTOrVCoordinateIdentification=True)

# Only explicit original weight inverses. Unexpected nonunits retain this
# entire completion block; there is no change of prime or norm saturation.
class ResidualWeightNonunit(Exception):pass
weight_units=[]
def ku(value,label):
 if not value:raise ResidualWeightNonunit(label)
 out=kinv(value,label);assert kmul(value,out)==one
 weight_units.append(dict(originalWeight=label,residue=pdigest(value),inverseProductReturned=True))
 return out
try:
 U=kr(u);Q=qbar;L=lbar;T=Tbar;V=vbar
 i2=ku(one*2,"integer 2")
 iQ=ku(Q,"original Q")
 ell=kr(one-2*(U-one)*(U-2*one)*iQ)
 delta=kr(one-Q);idelta=ku(delta,"original 1-Q")
 iell=ku(ell,"original ell")
 m=kr(U-ell);V2=kr(2*U-ell*Q)
 T0=kr(V2-2*U*U);J=kr(2*U*(one-U)+ell*Q)
 P02=kr((2*one-3*U)*V2-Q*U+2*U**3)
 Pf=kr(T0*(J-Q));iPf=ku(Pf,"original Pf=T0*(J-Q)")
 M=kr(ell*V2-U*U)
 bc=kr(M*idelta*i2*i2);ibc=ku(bc,"original bc")
 A2=kr(2*L*L-2*L+one);B3=kr(4*L**3-6*L*L+3*L-one)
 G=kr(L*P02+(U-one)*T0)
 f=kr((G*T0-Q*P02*(ell+T))*iPf)
 oldz=kr((V-J*f+G)*ibc);t=kr(oldz*iQ)
 Vmean=kr(V*iQ);Wmean=kr((T0+4*U*f)*i2)
 w=kr(L-one-T)
 Dphysical=kr(ell*A2-T*T)
except ResidualWeightNonunit as exc:
 say("accurate_fifth_P201_complete_Gram_model_retained_at_original_weight_nonunit",
  missingOriginalWholeUnit=str(exc),passedOriginalUnits=weight_units,
  fifthActualCompletionBlockExcluded=False,
  noPhysicalDInverseUsed=True,noDifferentPrimeTried=True,
  characteristicZeroDistinctFiveCoordinatePointUpperBound=5,
  characteristicZeroDistinctFullNormalizedPointUpperBound=10,
  ordinaryISPClaim=False)
 signal.setitimer(signal.ITIMER_REAL,0);raise SystemExit(0)

class R:
 """Whole quadratic rho algebra over K; no chosen square root."""
 __slots__=("c",)
 def __init__(self,a=0,b=None):
  if isinstance(a,R) and b is None:self.c=a.c;return
  def kk(v):
   if isinstance(v,nmod_poly):return kr(v)
   return kr(one*int(v))
  self.c=(kk(a),kk(0 if b is None else b))
 def __bool__(self):return any(self.c)
 def __eq__(self,v):
  if not isinstance(v,(R,nmod_poly,int)):return False
  return self.c==R(v).c
 def __neg__(self):return R(-self.c[0],-self.c[1])
 def __add__(self,v):
  if not isinstance(v,(R,nmod_poly,int)):return NotImplemented
  v=R(v);return R(self.c[0]+v.c[0],self.c[1]+v.c[1])
 __radd__=__add__
 def __sub__(self,v):
  if not isinstance(v,(R,nmod_poly,int)):return NotImplemented
  return self+-R(v)
 def __rsub__(self,v):
  if not isinstance(v,(R,nmod_poly,int)):return NotImplemented
  return R(v)+-self
 def __mul__(self,v):
  if not isinstance(v,(R,nmod_poly,int)):return NotImplemented
  v=R(v);a,b=self.c;c,e=v.c
  return R(a*c+delta*b*e,a*e+b*c)
 __rmul__=__mul__
 def __pow__(self,n):
  assert n>=0
  out=R(1);base=self
  while n:
   if n&1:out=out*base
   n//=2
   if n:base=base*base
  return out
rho=R(0,one);assert rho*rho==R(delta)
rho_inverse=rho*R(idelta);assert rho*rho_inverse==1
b=R(ell*i2)+rho*R(m*idelta*i2)
c=R(ell*i2)-rho*R(m*idelta*i2)
assert b+c==R(ell) and (b-c)*rho==R(m) and b*c==R(bc)
ib=c*R(ibc);ic=b*R(ibc)
assert b*ib==1 and c*ic==1
pr=R(1)+rho;qr=R(1)-rho
assert pr*qr==R(Q)
i_difference=rho*R(idelta*i2)
assert (pr-qr)*i_difference==1
a=R(1)-R(ell)
# The following coordinates are in the entire rho algebra.
Xmean=(R(Wmean)-qr*R(Vmean))*ib*i_difference
Ymean=(pr*R(Vmean)-R(Wmean))*ic*i_difference
r=Xmean-a*pr-c*R(t);s=Ymean-a*qr-b*R(t)
A1=R(2*f)-2*b*Xmean-2*c*Ymean+R(2*bc*t)
assert b*Xmean+c*Ymean==R(Vmean)
assert b*pr*Xmean+c*qr*Ymean==R(Wmean)
value_q1=R(-2*T*iell)
value_q0=(R(T*T)-c*R(A2))*ib*R(iell)

class E:
 """Whole monic value quadratic over the rho algebra, including double roots."""
 __slots__=("c",)
 def __init__(self,a=0,b=None):
  if isinstance(a,E) and b is None:self.c=a.c;return
  self.c=(R(a),R(0 if b is None else b))
 def __bool__(self):return any(self.c)
 def __eq__(self,v):
  if not isinstance(v,(E,R,nmod_poly,int)):return False
  return self.c==E(v).c
 def __neg__(self):return E(-self.c[0],-self.c[1])
 def __add__(self,v):
  if not isinstance(v,(E,R,nmod_poly,int)):return NotImplemented
  v=E(v);return E(self.c[0]+v.c[0],self.c[1]+v.c[1])
 __radd__=__add__
 def __sub__(self,v):
  if not isinstance(v,(E,R,nmod_poly,int)):return NotImplemented
  return self+-E(v)
 def __rsub__(self,v):
  if not isinstance(v,(E,R,nmod_poly,int)):return NotImplemented
  return E(v)+-self
 def __mul__(self,v):
  if not isinstance(v,(E,R,nmod_poly,int)):return NotImplemented
  v=E(v);aa,bb=self.c;cc,dd=v.c;bd=bb*dd
  return E(aa*cc-value_q0*bd,aa*dd+bb*cc-value_q1*bd)
 __rmul__=__mul__
 def __pow__(self,n):
  assert n>=0
  out=E(1);base=self
  while n:
   if n&1:out=out*base
   n//=2
   if n:base=base*base
  return out
x=E(0,R(1))
assert x*x+E(value_q1)*x+E(value_q0)==0
y=(E(T)-E(b)*x)*E(ic)
h=E(1)+x;k=E(1)+y
assert E(b)*x+E(c)*y==E(T)
assert E(b)*x*x+E(c)*y*y==E(A2)
moment3=E(b)*x**3+E(c)*y**3-E(B3)
# Universal original Gram definitions from the published U-value atlas:
# 2026-11-26-unit211-U-value-small-identities-347c.py,
# blob 91fad0d4be319fe57760ac51f7ee2a6b448bbb5a,
# SHA da790bddccce690e0e12cbe3941b6c02c2912319f646c5195834408b4bde965f.
# Here the original first-row values are BOTH retained, p=1+rho,q=1-rho.
I=[E(1),E(),E(1),E(1)]
rows=[[E(),E(),E(pr),E(qr)],
      [E(),E(A1),E(r),E(s)],
      [E(pr),E(r),E(),E(t)],
      [E(qr),E(s),E(t),E()]]
def va(v,z):return [x+y for x,y in zip(v,z)]
def vs(v,z):return [x-y for x,y in zip(v,z)]
def scale(z,v):return [z*x for x in v]
def vm(v,z):
 return [v[0]*z[0],v[0]*z[1]+v[1]*z[0],v[2]*z[2],v[3]*z[3]]
def tau(v):return E(a)*v[0]+v[1]+E(b)*v[2]+E(c)*v[3]
def DK(v):return [tau(vm(row,v)) for row in rows]
dd=DK(I);F2=tau(dd)
def P2(v):
 centered=vs(v,scale(tau(v),I))
 return tau(vm(vm(centered,centered),centered))
def N4(v):
 return (2*tau(vm(dd,vm(v,v)))-F2*tau(vm(v,v))
         -4*tau(v)*tau(vm(dd,v))+2*F2*tau(v)**2+tau(vm(v,DK(v))))
def Pjet(v,z):
 vc=vs(v,scale(tau(v),I));zc=vs(z,scale(tau(z),I))
 return 3*tau(vm(vm(vc,vc),zc))
def Njet(v,z):return N4(va(v,z))-N4(v)-N4(z)
assert F2==E(2*f)
assert P2(rows[0])==E(P02)
ev=[tau(vm(rows[0],rows[0])),2*tau(vm(rows[0],rows[1])),
    tau(vm(rows[2],rows[2])),tau(vm(rows[3],rows[3]))]
means=va(vs(vs(ev,scale(E(2),DK(dd))),scale(E(2),vm(dd,dd))),scale(2*F2,dd))
assert means[0]==0
assert N4(rows[0])-E(2*L*P02)==0
VV=[E(1),E(w),h,k]
assert tau(VV)==E(L)
assert tau(vm(VV,VV))==E(2*L*L)
assert P2(VV)==moment3
generators=list(zip(["original_E0","original_E1","original_EB","original_EC"],means))
generators+=[
 ("original_Pjet_minus_3wP02",Pjet(rows[0],rows[1])-E(3*w*P02)),
 ("original_Njet_minus_4lambda_wP02",Njet(rows[0],rows[1])-E(4*L*w*P02)),
 ("original_NB_minus_2lambda_h2P02",N4(rows[2])-E(2*L*P02)*h*h),
 ("original_NC_minus_2lambda_k2P02",N4(rows[3])-E(2*L*P02)*k*k),
 ("original_PB_minus_h3P02",P2(rows[2])-E(P02)*h**3),
 ("original_PC_minus_k3P02",P2(rows[3])-E(P02)*k**3),
 ("original_third_shifted_value_moment",moment3),
 ("same_complete_original_N4_V",N4(VV))]
def coeffs(v):return [co for rr in v.c for co in rr.c]
def flat(v):return [int(co[j]) for co in coeffs(v) for j in range(d)]
def eid(v):return ident([[int(q) for q in co.coeffs()] for co in coeffs(v)])
basis=[E(1),E(rho),x,E(rho)*x]
assert [flat(v) for v in basis]==[
 [1 if i==j*d else 0 for i in range(20)] for j in range(4)]
# Product matrices are the full finite monic algebra, not a selected value root.
for aa in basis:
 for bb in basis:assert aa*bb==bb*aa
say("new_fifth_P201_whole_twenty_dimensional_original_Gram_model",
 actualP201Block=pdigest(phi),wholeOriginalWeightUnits=weight_units,
 originalPhysicalD=pdigest(Dphysical),
 physicalDIsZeroModuloPrime=(not Dphysical),physicalDActuallyInverted=False,
 wholeRhoQuadraticIdentityReturned=True,
 wholeMonicValueQuadraticIdentityReturned=True,
 noMomentDiscriminantOrValueDifferenceInverted=True,
 sameFirstTwoValueMomentsReturned=True,
 sameOriginalF2P02E0N0Returned=True,
 sameOriginalTraceAndFullP2VIdentityReturned=True,
 completeOriginalGeneratorCount=len(generators),
 originalGeneratorIdentities=[dict(original=label,identity=eid(value),zeroModuloPrime=(not value))
                              for label,value in generators],
 wholeFiniteOriginalGeneratorBound=20,
 oldNineEquationSymbolicAtlasReplayed=False,
 noQQModularFactorIdentification=True)
columns=[];tags=[]
for label,value in generators:
 for j,base in enumerate(basis):
  product=value*base
  for a_power in range(d):
   actual=product*E(kr(u**a_power))
   columns.append(flat(actual));tags.append(dict(original=label,rhoPower=j%2,valuePower=j//2,uPower=a_power))
size=20
matrix=nmod_mat([[columns[j][i] for j in range(len(columns))] for i in range(size)],p)
rr,rank=matrix.rref();rank=int(rank)
assert rank%d==0
quotient=size-rank
detail={}
closed=(rank==size)
if closed:
 pivots=[]
 for i in range(size):
  j=next(j for j in range(len(columns)) if int(rr[i,j]))
  assert int(rr[i,j])==1;pivots.append(j)
 square=nmod_mat([[columns[j][i] for j in pivots] for i in range(size)],p)
 inverse=square.inv()
 eye=nmod_mat(size,size,[1 if i==j else 0 for i in range(size) for j in range(size)],p)
 assert square*inverse==eye
 unit=[int(inverse[j,0]) for j in range(size)]
 assert all(sum(columns[pivots[j]][i]*unit[j] for j in range(size))%p==(1 if i==0 else 0)
            for i in range(size))
 detail=dict(selectedOriginalProductColumns=[tags[j] for j in pivots],
  selectedOriginalSquareIdentity=ident([[int(square[i,j]) for j in range(size)] for i in range(size)]),
  originalUnitCombinationIdentity=ident(unit),
  completeOriginalSquareTimesInverseReturned=True,
  completeOriginalConstantOneCombinationReturned=True)
say("new_fifth_P201_complete_original_Gram_value_return",
 sourceSHA256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
 actualP201Block=pdigest(phi),wholeFiniteEnvironmentGeneratorBound=20,
 actualOriginalIdealMatrixShape=[size,len(columns)],
 actualFullOriginalIdealRank=rank,actualResidualOriginalQuotientDimension=quotient,
 fifthActualCompletionBlockExcluded=closed,
 characteristicZeroDistinctWeightPairUpperBound=(0 if closed else 5),
 characteristicZeroDistinctWeightLambdaUpperBound=(0 if closed else 5),
 characteristicZeroDistinctFiveCoordinatePointUpperBound=(0 if closed else 5),
 characteristicZeroDistinctFullNormalizedPointUpperBound=(0 if closed else 10),
 firstFourCompletedBlocksAlreadyClosedByOriginalF9Theorem=True,
 firstFourCompletedBlocksNotRecomputed=True,
 noPhysicalDOrValueDifferenceInverseUsed=True,
 allQuadraticRootsAndNilpotentsRetained=True,
 noNormOnlyOrDifferentValueSourceUsed=True,
 completedFiniteOriginalModuleNakayamaOnly=True,
 wholeOriginalH1GraphExcludedUsingPriorF9Theorem=closed,ordinaryISPClaim=False,
 coefficientPayloadTransmitted=False,encodedOrSplitPayloadCreated=False,
 peakRSSKiB=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss,**detail)
signal.setitimer(signal.ITIMER_REAL,0);signal.alarm(0)
