#!/usr/bin/env python3
"""NEW G36 != 0 whole-W chart: actual common F recovery followed by
the full original system in the SAME monic S-cubic environment.
Retain qF(Fp), six original Gram equations, r2/R6, and all three
D-linear individual-value equations. No Bi, A143, H411 or D inverse.
Then two NEW fixed original 3x3 parameter cofactors use NS / full NV.
No old full row, factorization or parameter cofactor gate is replayed.
180 seconds /4 GiB. Construction prefixes alone are regenerated."""
import json,time,hashlib,signal,resource,contextlib,io,math
from pathlib import Path
start=time.perf_counter();deadline=start+180;signal.alarm(180)
resource.setrlimit(resource.RLIMIT_AS,(4*1024**3,4*1024**3))
def say(**r):
 r['seconds']=time.perf_counter()-start
 print(json.dumps(r,separators=(',',':')),flush=True)
dep=Path(__file__).with_name('2026-11-27-unit211-W-coupled-original-Gram-value-four-by-three-minors-8542.py')
raw=dep.read_bytes()
assert hashlib.sha256(raw).hexdigest()=='f5c0226e4dfc8d0f80da5358d3b4a3718e2ad9c834555a2335f1e58162bb0b41'
marker=b"\nvalues={'r2':seed['values']['r2']"
assert raw.count(marker)==1
prefix=raw.split(marker)[0]
assert hashlib.sha256(prefix).hexdigest()=='3db85de82221320b400db83eb824cece88f153f8e7eed7d267406cda930c1559'
inp={'__file__':str(dep),'__name__':'__original_input_only_for_new_three_column_chart__'}
with contextlib.redirect_stdout(io.StringIO()):
 exec(compile(prefix,str(dep),'exec'),inp)
signal.alarm(max(1,math.ceil(deadline-time.perf_counter())))
seed=inp['seed'];ns=seed['ns']
C,P,ctx,F,S,R,AA,BB=[inp[x] for x in ['C','P','ctx','F','S','R','AA','BB']]
e,k,u,Q,ell,M,bc,Phi,P02,J,T0,Pf,d,m,lam,T,qF,q3,q4,D,K=[
 ns[x] for x in ['e','k','u','Q','ell','M','bc','Phi','P02','J','T0','Pf','d','m','lam','T','qF','q3','q4','D','K']]
ep,kp,lp=ctx.gens();zero=ctx.constant(0);one=ctx.constant(1)
old_reduce=ns['reduce_poly'];original=ns['original'];orig=ns['orig'];convert=ns['convert']
prof=seed['prof'];primitive=seed['primitive_row']
def cprofile(cf,include=False):
 cf=C(cf);return dict(numerator=prof(cf.n,include),denominator=prof(cf.d,include))
def pprofile(pp):
 data=P(pp).data();bb=json.dumps(data,separators=(',',':')).encode()
 return dict(degree=P(pp).degree(),terms=len(P(pp).t),bytes=len(bb),sha256=hashlib.sha256(bb).hexdigest(),
  scalarNumeratorMaxDegrees=[max((int(v.n.degrees()[j]) for v in P(pp).t.values()),default=-1) for j in range(3)])
def digest(pp):
 h=hashlib.sha256();n=0
 for p in pp:
  b=json.dumps(P(p).data(),separators=(',',':')).encode()
  h.update(b);h.update(b'\n');n+=len(b)+1
 return dict(bytes=n,sha256=h.hexdigest())
# Exact G36 fixed by the published complete determinant factorization.
gcoeff=[[4096,9216,7680,3072,592,24,-10,-1],
 [-6144,-16128,-14336,-6048,-1416,-186,-9],
 [512,6016,6560,2528,468,50,2],
 [1792,832,-832,-392,-50,-2],
 [-256,-544,-24,24,4],[-192,0,-8],[32]]
G36=sum((sum((C(v)*k**j for j,v in enumerate(row)),C())*Q**i for i,row in enumerate(gcoeff)),C())
assert G36.d.total_degree()==0 and G36.n.degrees()[2]<=0
# We work on the explicitly retained complement G36 != 0.
# No conclusion about its zero fibre is assumed in this input.
seed['atoms'].append(G36.n)
ns['new_atoms'] += list(seed['atoms'])
ppaid=ns['ppaid'];paid=ns['paid'];strip_paid=seed['strip_paid']
def cl(cf,j):
 cf=C(cf);assert cf.d.degrees()[2]<=0
 n=zero
 for mm,v in cf.n.to_dict().items():
  if mm[2]==j:n+=v*ep**int(mm[0])*kp**int(mm[1])
 return C(n,cf.d)
bm=[]
for bb in BB:
 assert all(mm[0]==0 and mm[1]<=1 for mm in bb.t)
 a0=bb.t.get((0,0),C());aS=bb.t.get((0,1),C())
 assert a0.n.degrees()[2]<=1 and aS.n.degrees()[2]<=0 and aS.d.degrees()[2]<=0
 aL=cl(a0,1);aC=cl(a0,0)
 assert bb==P(aC)+P(lam*aL)+S.scale(aS)
 bm.append([aC,aL,aS])
aa,bb,cc=bm
omega=[bb[1]*cc[2]-bb[2]*cc[1],aa[2]*cc[1]-aa[1]*cc[2],aa[1]*bb[2]-aa[2]*bb[1]]
det=sum((omega[i]*bm[i][0] for i in range(3)),C())
assert det and det.n.degrees()[2]<=0 and det.d.degrees()[2]<=0
assert all(sum((omega[i]*bm[i][j] for i in range(3)),C())==(det if j==0 else C()) for j in range(3))
assert sum((BB[i].scale(omega[i]) for i in range(3)),P())==P(det)
paid(1/det)
Fp=-sum((AA[i].scale(omega[i]/det) for i in range(3)),P())
assert all(mm[0]==0 for mm in Fp.t) and Fp.degree()<=2
Flin=F-Fp
assert sum((R[i].scale(omega[i]) for i in range(3)),P())==Flin.scale(det)
ppaid(Fp)
say(stage='new_W_G36_nonzero_actual_common_F_recovery',
 allThreeOriginalCofactorColumnsActuallyReturned=True,
 fullSamePointFLinearIdealIdentityActuallyReturned=True,
 noIndividualFHeadInverted=True,
 scalarDenominatorsOnlyPublishedUnitsAndExplicitG36Chart=True,
 Fp=pprofile(Fp),weightDeterminant=cprofile(det),
 originalQFStillRetained=True,wholeG36ZeroFiberNotDiscarded=True)
rewrite_count=0
def reduceS(pp):
 global rewrite_count
 pp=P(pp);assert all(mm[0]==0 for mm in pp.t)
 original_p=P(pp);rem=P(pp);quo=P()
 while any(mm[1]>=3 for mm in rem.t):
  mm=max((v for v in rem.t if v[1]>=3),key=lambda v:v[1])
  term=P.monomial((0,mm[1]-3),rem.t[mm])
  rem=rem-term*q3;quo=quo+term
 assert rem+quo*q3==original_p
 assert all(mm[0]==0 and mm[1]<3 for mm in rem.t)
 ppaid(rem);rewrite_count+=1
 return rem,quo
def divideF(pp):
 pp=P(pp);rem=P(pp);quo=P()
 while any(mm[0]>=1 for mm in rem.t):
  mm=max((v for v in rem.t if v[0]>=1),key=lambda v:(v[0],v[1]))
  term=P.monomial((mm[0]-1,mm[1]),rem.t[mm])
  rem=rem-term*Flin;quo=quo+term
 assert pp==rem+quo*Flin and all(mm[0]==0 for mm in rem.t)
 return rem,quo
images={};traces={};primitive_rows={}
def original_image(name,pp):
 pp=P(pp);rr,tf,tt=old_reduce(pp)
 sub,fl=divideF(rr);image,qs=reduceS(sub)
 # This is the complete new ORIGINAL ideal identity, not a rank claim.
 assert pp==image+tf*qF+(tt+qs)*q3+fl*Flin
 traces[name]=digest([tf,tt+qs,fl])
 return image
# qF cannot be lost by reducing it to zero in the old six-column tower.
sub,fl=divideF(qF);qFimage,qs=reduceS(sub)
assert qF==qFimage+qs*q3+fl*Flin
traces['original_qF_substituted']=digest([qs,fl])
class A3:
 def __init__(self,v=0):
  if isinstance(v,A3):self.p=P(v.p);return
  p=P(v);assert all(mm[0]==0 for mm in p.t)
  self.p=reduceS(p)[0] if any(mm[1]>=3 for mm in p.t) else p
 def __bool__(self):return bool(self.p)
 def __neg__(self):return A3(-self.p)
 def __add__(self,v):return A3(self.p+A3(v).p)
 __radd__=__add__
 def __sub__(self,v):return self+-A3(v)
 def __rsub__(self,v):return A3(v)+-self
 def __mul__(self,v):return A3(self.p*A3(v).p)
 __rmul__=__mul__
 def scale(self,v):return A3(self.p.scale(C(v)))
 def __pow__(self,n):
  assert n>=0
  out=A3(1);v=self
  while n:
   if n&1:out=out*v
   n//=2
   if n:v=v*v
  return out
 def __eq__(self,v):return self.p==A3(v).p
def save(name,p,origin):
 p=A3(p).p;ppaid(p);images[name]=p
 row,record=primitive(p)
 primitive_rows[name]=row
 say(stage='new_W_G36_nonzero_original_three_column_row_returned',
     name=name,origin=origin,normalForm=pprofile(p),
     allThreePrimitiveCoefficientProductsActuallyReturned=True,
     primitiveTrace=record,oldOriginalTrace=traces.get(name),
     noNewGeometryOrPhysicalDInverse=True,claimExcluded=False)
save('original_qF_substituted',qFimage,'qF=QFimage+q3*quot+(F-Fp)*quot')
for name in ['E1','EBe','EBo','N1','NS','PS']:
 save(name,original_image(name,original[name]),'full original Gram equation with qF, q3 and F-Fp multipliers')
save('r2',original_image('r2',q4),'the entire original q4 remains')
R6=(K*K).scale(M)-(D**3).scale(4*m*m)
save('R6',original_image('R6',R6),'same original second/third moment relation')
DQ=A3(original_image('D',D));TQ=A3(original_image('T',T));KQ=A3(original_image('K',K))
D2=DQ*DQ;A0=A3(1)+TQ.scale(1/ell)
Nold,Pold=orig['N4'],orig['P2'];gram=orig['rows']
nbp,pbp=convert(Nold(gram[2]).b),convert(Pold(gram[2]).b)
nb=A3(original_image('original_individual_N_odd_coefficient',nbp))
pb=A3(original_image('original_individual_P_odd_coefficient',pbp))
Nlow=DQ*nb+(KQ*A0).scale(2*lam*P02/m)+D2.scale(4*lam*P02*m/(ell*M))
save('D_linear_individual_N_odd',Nlow,
 'published complete D-linear original identity; all new products reduced with actual monic S3 identities')
Plow=DQ*pb+(KQ*A0*A0).scale(3*P02/(2*m))+(KQ*DQ).scale(P02*(3*m*m/(ell*ell)+d)/(2*m*M))+(A0*D2).scale(6*P02*m/(ell*M))
save('D_linear_individual_P_odd',Plow,
 'published complete D-linear original identity; PS and R6 kept at the same point')
Eold=orig['E'];l0=orig['l'];m0=orig['u']-l0;t0=orig['T'];lamb0=orig['lam']
V0=[Eold(1),Eold(lamb0-1-t0),Eold(1+t0/l0),Eold(1+t0/l0)]
V1=[Eold(),Eold(),Eold(m0/l0,-1),Eold(m0/l0,1)]
Z0raw=Nold(V0);Z2raw=Nold(V1)
Z1raw=Nold([V0[j]+V1[j] for j in range(4)])-Z0raw-Z2raw
assert not Z0raw.b and not Z1raw.b and not Z2raw.b
zz=[]
for i,z in enumerate([Z0raw,Z1raw,Z2raw]):
 zz.append(A3(original_image('full_original_N4_V_coefficient_'+str(i),convert(z.a))))
Z0,Z1,Z2=zz
Vlow=DQ*Z0+(KQ*Z1).scale(1/(2*m))+(D2*Z2).scale(1/M)
save('D_linear_entire_original_N4_V',Vlow,
 'entire N4(V0+sV1) quadratic, not weighted trace or Phi multiple')
assert len(images)==12
multcols=[]
for j in range(3):
 rr,qq=reduceS(P.monomial((0,j+1)))
 assert rr+qq*q3==P.monomial((0,j+1))
 multcols.append(rr)
say(stage='new_W_G36_nonzero_complete_original_three_column_input',
 sourceSHA256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
 scalarVariables=['e','k','lambda'],actualBasis=['1','S','S^2'],
 allTwelveOriginalRows=list(images),
 allTwelveRowsAndThreeActualMultiplicationColumnsReturned=True,
 qFSubstitutionRetained=True,
 individualNPAndWholeN4VKeptWithSameOriginalFAndValues=True,
 originalPhysicalDNonzeroScopeForEquivalenceRetained=True,
 allOriginalFHeadZeroFibersCoveredByTrueCommonWeightDeterminant=True,
 allG36ZeroFibersStillRequireTheirIndependentOriginalReturn=True,
 fullParameterLeadingZerosNotRemoved=True,
 rawCoefficientCertificate=digest(list(images.values())+multcols),
 originalTraceCertificates=traces,
 exactMonicSRewriteProducts=rewrite_count,
 noBHeadA143H411OrDInverse=True,wholeWExcluded=False)
# Each new determinant below uses at least one original equation omitted
# by the previous r2/Gram-only parameter cofactors.
for label,names in [
 ('new_full_NS_parameter_constraint',['E1','EBe','NS']),
 ('new_entire_NV_parameter_constraint',['E1','EBe','D_linear_entire_original_N4_V'])]:
 begun=time.perf_counter()
 a,b,c=[primitive_rows[n] for n in names]
 cof=[b[1]*c[2]-b[2]*c[1],a[2]*c[1]-a[1]*c[2],a[1]*b[2]-a[2]*b[1]]
 determinant=sum((cof[j]*[a,b,c][j][0] for j in range(3)),zero)
 assert all(sum((cof[i]*[a,b,c][i][j] for i in range(3)),zero)==(determinant if j==0 else zero) for j in range(3))
 say(stage='new_W_G36_nonzero_true_original_constant_cofactor_returned',
     label=label,originalRows=names,
     allThreeOriginalConstantColumnsActuallyMultipliedBack=True,
     determinantZero=not bool(determinant),rawProfile=prof(determinant),
     claimExcluded=False)
 if not determinant:continue
 remain,removed=strip_paid(determinant)
 scalar=remain.coefficient(0);remain=remain/scalar;removed*=scalar
 assert remain*removed==determinant
 hd=zero;ld=int(remain.degrees()[2])
 for mm,cf in remain.to_dict().items():
  if int(mm[2])==ld:hd+=cf*ep**int(mm[0])*kp**int(mm[1])
 uh,ph=strip_paid(hd);assert uh*ph==hd
 cb=json.dumps([[[list(map(int,mm)),str(cf)] for mm,cf in sorted(po.to_dict().items())] for po in cof],separators=(',',':')).encode()
 say(stage='new_W_G36_nonzero_complete_parameter_constraint',
     label=label,originalRows=names,
     necessaryPolynomial=prof(remain,True),
     remainingLambdaDegree=ld,
     completeLambdaHeadRemainingUnpaid=prof(uh,True),
     lambdaHeadZeroEntireFiberRetained=True,
     onlyPublishedUnitsAndExplicitG36ChartStripped=True,
     fullOriginalCofactorCertificate=dict(bytes=len(cb),sha256=hashlib.sha256(cb).hexdigest()),
     elapsedSeconds=time.perf_counter()-begun,wholeWExcluded=False)
say(stage='new_W_G36_nonzero_full_original_three_column_attempt_finished',
 sourceSHA256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
 bothNewOriginalParameterCofactorsProcessed=True,
 exactMonicSRewriteProducts=rewrite_count,
 noEarlierParameterCofactorOrFullSixColumnGateReplayed=True,
 largeRegenerableCachesWritten=False,wholeWExcluded=False,ordinaryISPClaim=False,
 peakRssKiB=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)
signal.alarm(0)
