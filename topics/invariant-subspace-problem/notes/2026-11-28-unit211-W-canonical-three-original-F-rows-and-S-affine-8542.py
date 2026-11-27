#!/usr/bin/env python3
"""NEW whole-W canonical transformation of the THREE original F-linear rows.
Use the entire already-paid weight matrix inverse, not the E1/EBe pair
cofactor. Return (F-Fp, p2(S), p3(S)) as the EXACT same ideal as R0,R1,R2.
Reduce p3 only by the existing monic S3, then form one new S-affine row.
All scalar head-zero and C13-zero fibres stay. qF(Fp) and all other
original conditions remain required. No former 12-row/cofactor/resultant
gate replay. 180 seconds / 4 GiB. Exact small new parameter chunks only."""
import json,time,hashlib,zlib,base64,signal,resource,contextlib,io,math
from pathlib import Path
start=time.perf_counter();deadline=start+180;signal.alarm(180)
resource.setrlimit(resource.RLIMIT_AS,(4*1024**3,4*1024**3))
def say(**r):
 r['seconds']=time.perf_counter()-start
 print(json.dumps(r,separators=(',',':')),flush=True)
dep=Path(__file__).with_name('2026-11-28-unit211-W-G36-nonzero-full-original-three-column-return-8542.py')
raw=dep.read_bytes()
assert hashlib.sha256(raw).hexdigest()=='8430b819844aeecf8bd02619f8724e5c9ab75cad3a7c8c601b943cf515f79351'
marker=b"\nsave('original_qF_substituted'"
assert raw.count(marker)==1
prefix=raw.split(marker)[0]
assert hashlib.sha256(prefix).hexdigest()=='8947c21464310d9eaf4fabe179ce333930dc3e6b03f4fd3a65f02412ec2bb7ac'
ns={'__file__':str(dep),'__name__':'__common_F_construction_only_for_new_canonical_three_rows__'}
with contextlib.redirect_stdout(io.StringIO()):
 exec(compile(prefix,str(dep),'exec'),ns)
signal.alarm(max(1,math.ceil(deadline-time.perf_counter())))
C,P,ctx,F,S,lam,q3,R,AA,BB,bm,det,Fp,Flin,prof,paid,ppaid,primitive,reduceS=[
 ns[x] for x in ['C','P','ctx','F','S','lam','q3','R','AA','BB','bm',
 'det','Fp','Flin','prof','paid','ppaid','primitive','reduceS']]
zero=ctx.constant(0);one=ctx.constant(1)
def pdata(p):
 return [[list(map(int,mm)),str(cf)] for mm,cf in sorted(p.to_dict().items())]
def exact_input(label,components):
 obj=dict(variables=['e','k','lambda'],components={k:pdata(v) for k,v in components.items()},
          label=label,scope='whole current paid W; same F and S; every original condition retained',
          allNewParameterHeadZeroAndC13ZeroFibresRetained=True)
 data=json.dumps(obj,separators=(',',':')).encode()
 enc=base64.b64encode(zlib.compress(data,9)).decode()
 assert zlib.decompress(base64.b64decode(enc))==data
 chunks=[enc[j:j+75000] for j in range(0,len(enc),75000)]
 say(stage='new_W_canonical_three_rows_exact_input',label=label,
     rawBytes=len(data),rawSHA256=hashlib.sha256(data).hexdigest(),
     base64Characters=len(enc),chunks=len(chunks),maximumChunkCharacters=75000,
     noRegenerableOriginalMatrixCacheWritten=True)
 for j,ch in enumerate(chunks):
  say(stage='new_W_canonical_three_rows_exact_input_chunk',
      label=label,index=j,total=len(chunks),data=ch)
def matrix_digest(mat):
 data=json.dumps([[dict(numerator=pdata(v.n),denominator=pdata(v.d)) for v in row] for row in mat],separators=(',',':')).encode()
 return dict(bytes=len(data),sha256=hashlib.sha256(data).hexdigest())
# bm has original rows (c_i, alpha_i, beta_i), so B_i=c_i+alpha_i*lambda+beta_i*S.
# Inverting the ENTIRE matrix is already legal on the complete current W:
# results/R150-appendix-unit211-W-G36-entire-original-exclusion-and-global-F-recovery.md
def cofactor(i,j):
 ii=[x for x in range(3) if x!=i];jj=[x for x in range(3) if x!=j]
 return (bm[ii[0]][jj[0]]*bm[ii[1]][jj[1]]-bm[ii[0]][jj[1]]*bm[ii[1]][jj[0]])*((-1)**(i+j))
inverse=[[cofactor(j,i)/det for j in range(3)] for i in range(3)]
for i in range(3):
 for j in range(3):
  paid(inverse[i][j])
  assert sum((inverse[i][h]*bm[h][j] for h in range(3)),C())==C(int(i==j))
  assert sum((bm[i][h]*inverse[h][j] for h in range(3)),C())==C(int(i==j))
acan=[sum((AA[j].scale(inverse[i][j]) for j in range(3)),P()) for i in range(3)]
rcan=[sum((R[j].scale(inverse[i][j]) for j in range(3)),P()) for i in range(3)]
targets=[F,F.scale(lam),S*F]
for i in range(3):
 assert rcan[i]==targets[i]+acan[i]
 assert all(mm[0]==0 for mm in acan[i].t) and acan[i].degree()<=2
 ppaid(acan[i]);ppaid(rcan[i])
assert acan[0]==-Fp and rcan[0]==Flin
p2=acan[1]+Fp.scale(lam)
p3=acan[2]+S*Fp
assert p2==rcan[1]-rcan[0].scale(lam)
assert p3==rcan[2]-S*rcan[0]
assert all(mm[0]==0 for mm in p2.t) and p2.degree()<=2
assert all(mm[0]==0 for mm in p3.t) and p3.degree()<=3
ppaid(p2);ppaid(p3)
back=[Flin,Flin.scale(lam)+p2,S*Flin+p3]
for i in range(3):
 assert R[i]==sum((back[j].scale(bm[i][j]) for j in range(3)),P())
say(stage='new_W_canonical_three_original_rows_exact_ideal_identity',
 originalRows=['E1','EBe','N1'],weightMatrixInverseCertificate=matrix_digest(inverse),
 allEighteenMatrixInverseProductsActuallyReturned=True,
 allThreeFullOriginalPolynomialForwardAndReverseIdentitiesActuallyReturned=True,
 identity='(R0,R1,R2)=(F-Fp,p2,p3); p2=Ac_lambda+lambda*Fp; p3=Ac_S+S*Fp',
 canonicalCoefficientPolynomials=[ns['pprofile'](p) for p in acan],
 p2=ns['pprofile'](p2),p3=ns['pprofile'](p3),
 allScalarInversesOnlyAlreadyPaidWeights=True,
 noC13OrIndividualBOrGeometryOrDInverse=True,
 completeC13ZeroFibreRetained=True,
 qFSubstitutionAndAllOtherOriginalRowsStillRequired=True,
 wholeWExcluded=False)
# This is a new pair of original pure S equations. No qF condition is lost.
g,qq=reduceS(p3)
assert p3==g+qq*q3 and all(mm==(0,0) for mm in qq.t)
f=p2
primitive_rows=[];norms=[]
for name,pol in [('canonical_p2',f),('canonical_p3_mod_q3',g)]:
 row,trace=primitive(pol)
 assert len(row)==3
 rr=sum((P.monomial((0,j),C(row[j])) for j in range(3)),P())
 primitive_rows.append((rr,row));norms.append(trace)
 say(stage='new_W_canonical_three_rows_original_quadratic',
     name=name,coefficients=[prof(v,True) for v in row],paidNormalizationTrace=trace,
     completeCanonicalToOriginalAndMonicSProductsActuallyReturned=True,
     allQuadraticLeadingZeroFibresRetained=True)
(rf,(f0,f1,f2)),(rg,(g0,g1,g2))=primitive_rows
exact_input('new_canonical_original_S_quadratic_pair',
 {'f0':f0,'f1':f1,'f2':f2,'g0':g0,'g1':g1,'g2':g2})
a=g2*f1-f2*g1;b=g2*f0-f2*g0
L=rf.scale(g2)-rg.scale(f2)
assert L==S.scale(a)+P(b) and L.degree()<=1
row,trace=primitive(L);assert not row[2]
b0,a1=row[0],row[1]
say(stage='new_W_canonical_pair_true_S_affine_identity',
 identity='g2*f-f2*g=a*S+b',
 completeOriginalAffinePolynomialProductActuallyReturned=True,
 constant=prof(b0,True),SHead=prof(a1,True),paidNormalizationTrace=trace,
 allOriginalAndNewAffineHeadZeroFibresRetained=True,
 noNewHeadInverseAndNoFixedResultantExpansion=True,
 wholeWExcluded=False)
exact_input('new_canonical_original_S_affine',{'L0':b0,'L1':a1})
if a1 or b0:
 common=a1.gcd(b0)
 qq0=b0/common;qq1=a1/common
 assert common*qq0==b0 and common*qq1==a1
 say(stage='new_W_canonical_pair_exact_common_factor',
     common=prof(common,True),constantQuotient=prof(qq0),headQuotient=prof(qq1),
     bothExactProductsReturned=True,unpaidCommonNotRemoved=True,
     entireCommonZeroFibreRetained=True,noMultivariateGcdEmptinessClaim=True)
say(stage='new_W_canonical_three_original_rows_and_affine_finished',
 sourceSHA256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
 completeForwardAndReverseOriginalIdealIdentitiesReturned=True,
 completeNewPairAndAffineInputsOutput=True,
 qFSubstitutionRetainedAsIndependentOriginalCondition=True,
 allUnpaidHeadAndC13FibresRetained=True,
 noPreviousTwelveRowCofactorOrLargeResultantGateReplayed=True,
 noWholeWOrOrdinaryISPExclusionClaim=True,
 peakRssKiB=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)
signal.alarm(0)
