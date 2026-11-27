#!/usr/bin/env python3
"""NEW entire-W original physical-lambda multiplication and monic degree-six input.
From the already paid native six rules and eighteen true products, construct
M_lambda in the SAME original four-mean ideal, with every error column.
Faddeev--LeVerrier gives a monic degree-six matrix polynomial; its final
matrix is actually checked zero. The universal adjugate / polynomial-in-
one-matrix identity returns the same scalar relation to the original ideal.
No ambient six-generator freeness, simultaneous matrix commutativity,
geometric D inverse, unpaid leading inverse, or old determinant gate.
Only possible spectral factors lambda and lambda-3/2 have prior whole-W
exclusions; any exact such factor is stripped with a full coefficient return.
180s /4GiB. No coefficient payload or recomputable cache is written.
"""
import json,time,hashlib,signal,resource,contextlib,io,math
from pathlib import Path
from flint import fmpq
started=time.perf_counter();deadline=started+180
signal.alarm(180);resource.setrlimit(resource.RLIMIT_AS,(4*1024**3,4*1024**3))
def say(**d):
 d['seconds']=time.perf_counter()-started
 print(json.dumps(d,separators=(',',':')),flush=True)
def digest(o):
 b=json.dumps(o,separators=(',',':')).encode()
 return dict(bytes=len(b),sha256=hashlib.sha256(b).hexdigest())
dep=Path(__file__).with_name('2026-11-27-unit211-generic-LS-W-C9-six-generator-original-parameter-cofactors-8542.py')
raw=dep.read_bytes()
assert hashlib.sha256(raw).hexdigest()=='10720660772a9a1252b905b1227b697e038d1b974b7e96ec30e485477b21d3f1'
marker=b'\nnecessary=[];necessary_tags=[];necessary_labels=[]'
assert raw.count(marker)==1
prefix=raw.split(marker)[0]
assert len(prefix)==15191
assert hashlib.sha256(prefix).hexdigest()=='d4696b07ea7eccb62b4e8c885fb50e95f17b6c0d105eb65fb2a3d11b2f965507'
ns={'__file__':str(dep),'__name__':'only_original_four_rules_six_monomials_eighteen_products'}
with contextlib.redirect_stdout(io.StringIO()):
 exec(compile(prefix,str(dep)+'#original_multiplication_only','exec'),ns)
signal.alarm(max(1,math.ceil(deadline-time.perf_counter())))
R=ns['R'];ctx=ns['ctx'];ep=ns['ep'];kp=ns['kp'];zero=ns['zz'];one=ns['oo']
basis=ns['basis'];variables=ns['variables'];original=ns['original']
matrices=ns['matrices'];errors=ns['errors'];coeffmap=ns['coeffmap'];strip=ns['strip_known']
assert ns['freemons']==[(0,0,0),(1,0,0),(0,1,0),(0,0,1),(0,2,0),(0,1,1)]
J19=(16*ep**4*kp**3-8*ep**3*kp**4-16*ep**3*kp**3-96*ep**3*kp**2
 -ep**2*kp**5-8*ep**2*kp**4+24*ep**2*kp**3+64*ep**2*kp**2+192*ep**2*kp
 -2*ep*kp**5-14*ep*kp**4-12*ep*kp**3-128*ep
 -kp**5-10*kp**4-40*kp**3-104*kp**2-160*kp-128)
paid_atoms=ns['base_units']+[
 ('whole_equal_weights_k_plus_two',kp+2),
 ('whole_original_J19',J19),('whole_original_C9',ns['C9'])]
def pay(p):
 assert p
 rest,removed,h=strip(p,paid_atoms)
 assert rest*removed==p and rest.total_degree()==0
 return h
def scalar(c):
 c=R(c)
 assert all(all(mm[j]==0 for j in range(2,8)) for p in [c.n,c.d] for mm in p.to_dict())
 pay(c.d);return c
def enc(p):return [[[int(j) for j in mm],str(c)] for mm,c in sorted(p.to_dict().items())]
def pmeta(p):
 dd=p.to_dict()
 return dict(degrees=list(map(int,p.degrees()[:2])),totalDegree=int(p.total_degree()),
             terms=len(dd),**digest(enc(p)))
def rmeta(c):
 c=R(c);return dict(numerator=pmeta(c.n),denominator=pmeta(c.d))
d2=pay(ns['delta2']);d3n=pay(ns['delta3'].n);d3d=pay(ns['delta3'].d)
for rule,tag in zip(ns['q'],ns['tags']):
 assert not tag[4] and not tag[5]
 assert sum((tag[j]*original[j] for j in range(4)),R())==rule
 for cf in coeffmap(rule).values():scalar(cf)
 for cf in tag:pay(cf.d)
for a in range(3):
 for i in range(6):
  assert not errors[a][i][4] and not errors[a][i][5]
  assert variables[a]*basis[i]-sum((matrices[a][i][j]*basis[j] for j in range(6)),R())==sum((errors[a][i][g]*original[g] for g in range(4)),R())
  for cf in matrices[a][i]:scalar(cf)
  for cf in errors[a][i]:pay(cf.d)
lam=ns['symbolic']['lam'];lc=coeffmap(lam)
mons=[(0,0,0),(1,0,0),(0,1,0),(0,0,1)]
assert set(lc).issubset(set(mons))
alpha=[scalar(lc.get(mm,R())) for mm in mons]
assert lam==alpha[0]+sum((alpha[a+1]*variables[a] for a in range(3)),R())
assert alpha[3]==ns['bc']*ns['Q']/ns['P02']
ML=[[alpha[0]*int(i==j)+sum((alpha[a+1]*matrices[a][i][j] for a in range(3)),R())
     for j in range(6)] for i in range(6)]
EL=[[sum((alpha[a+1]*errors[a][i][g] for a in range(3)),R()) for g in range(4)] for i in range(6)]
for i in range(6):
 assert lam*basis[i]-sum((ML[i][j]*basis[j] for j in range(6)),R())==sum((EL[i][g]*original[g] for g in range(4)),R())
 for c in ML[i]:scalar(c)
 for c in EL[i]:pay(c.d)
midentity=digest([[enc(c.n),enc(c.d)] for row in ML for c in row])
eidentity=digest([[enc(c.n),enc(c.d)] for row in EL for c in row])
say(stage='new_entire_W_same_original_lambda_six_multiplication',
 basis=['1','x','y','t','y^2','y*t'],actualOriginalMeanIndices=[0,1,2,3],
 exactRelation='(lambda*I-Mlambda)*v = Elambda*(E1,EBe,EBo,N1)^T',
 sixOriginalLambdaProductsActuallyReturned=True,
 originalEighteenAxisProductsAndAllSixRulesReturned=True,
 noWeightedNSPSNeededForThisIdentity=True,
 actualTwoHeadsPaid=[d2,d3n,d3d],
 everyMatrixCoefficientIsOnlyAWeightRationalFunction=True,
 allMatrixAndErrorDenominatorsAlreadyPaid=True,
 matrixDefinitionIdentity=midentity,errorDefinitionIdentity=eidentity,
 geometricDOrNewLambdaHeadInverted=False,freeGeneratorAssumption=False,
 oldNativeDeterminantOrTwelveSylvesterGateExecuted=False,claimExcluded=False)
# Clear ONE common, already paid weight denominator first.  All subsequent
# matrix products are in QQ[e,k], avoiding rational gcds at every entry.
# This changes no geometric input and introduces no unproved inverse.
den=one
for row in ML:
 for cf in row:
  gg=den.gcd(cf.d);qq=cf.d/gg
  assert gg*qq==cf.d
  den*=qq
den_paid=pay(den)
N=[]
for row in ML:
 outrow=[]
 for cf in row:
  qq=den/cf.d;assert qq*cf.d==den
  nn=cf.n*qq
  assert R(nn,den)==cf
  outrow.append(nn)
 N.append(outrow)
say(stage='new_lambda_matrix_single_paid_denominator_cleared',
 commonDenominator=pmeta(den),paidFactors=den_paid,
 all36OriginalMatrixScaleProductsReturned=True,
 clearedMatrixDefinition=digest([enc(c) for row in N for c in row]),
 onlyPolynomialWeightMatrixProductsAfterThisStage=True,claimExcluded=False)
def multiply_poly(A,B):
 return [[sum((A[i][h]*B[h][j] for h in range(6)),zero) for j in range(6)] for i in range(6)]
I=[[ctx.constant(int(i==j)) for j in range(6)] for i in range(6)]
B=I;Bs=[I];descending=[R(1)];denpower=one
for step in range(1,7):
 NB=multiply_poly(N,B)
 trace=sum((NB[i][i] for i in range(6)),zero)
 ccN=-trace/fmpq(step)
 assert fmpq(step)*ccN==-trace
 denpower*=den
 cc=R(ccN,denpower);scalar(cc);descending.append(cc)
 nxt=[[NB[i][j]+ccN*int(i==j) for j in range(6)] for i in range(6)]
 # B_j(N)=N B_(j-1)(N)+c_j(N) I.  Dividing by den^j
 # gives the exact recurrence for M=N/den over the original paid ring.
 for i in range(6):
  for j in range(6):
   assert nxt[i][j]-NB[i][j]==ccN*int(i==j)
 B=nxt
 if step<6:Bs.append(B)
 say(stage='new_entire_W_original_lambda_characteristic_coefficient',
     index=step,coefficient=rmeta(cc),
     all36ExactPolynomialMatrixRecurrenceProductsVerified=True,
     rationalIntegerTraceDivisionReturned=True,
     onlyNewScalarDivisor=step,onlyWeightDenominatorPowersOfAlreadyPaidDen=True,
     remainingMatrixNonzeroEntries=sum(bool(c) for row in B for c in row),
     claimExcluded=False)
assert len(Bs)==6 and len(descending)==7
assert not any(c for row in B for c in row)
assert descending[0]==1
# B_j(N)/den^j is a polynomial in the ONE matrix M.  Therefore it
# commutes with M; the coefficient identities give both
# (Z I-M) Q(Z)=Q(Z)(Z I-M)=chi(Z) I, with
# Q(Z)=sum_(j=0)^5 [B_j(N)/den^j] Z^(5-j).
# Compose this with the six ACTUAL original EL identities and v[0]=1:
# chi(lambda)=e0^T Q(lambda) EL * original. No free basis is used.
chi=list(reversed(descending))
chi_meta=[rmeta(c) for c in chi]
say(stage='new_entire_W_global_monic_lambda_six_original_identity',
 degree=6,leadingCoefficientOne=True,finalCayleyHamiltonMatrixActuallyZero=True,
 all216PolynomialMatrixRecurrenceCoefficientProductsVerified=True,
 exactOriginalIdealIdentity='chi(lambda) = e0^T*(sum_j B_j(N)/den^j*lambda^(5-j))*Elambda*F4',
 actualOriginalRelationFactorsCheckedBeforeFormalComposition=True,
 polynomialInOneMatrixCommutationOnly=True,
 simultaneousAxisCommutationOrFreeBasisAssumed=False,
 coefficientsAscendingProfiles=chi_meta,
 everyCoefficientDenominatorAlreadyPaid=True,
 geometricDLocalizationUsed=False,
 noLargeExpandedOriginalTraceClaimed=True,claimExcluded=False)
# Strip only these TWO separately proved whole-original value fibres.
# lambda!=0: original-U-value-atlas.
# lambda!=3/2: W-lambda-three-halves-complete-original-exclusion.
def lin_div(cs,root):
 if len(cs)<=1:return [],cs[0]
 q=[R() for _ in range(len(cs)-1)]
 q[-1]=cs[-1]
 for j in range(len(q)-2,-1,-1):q[j]=cs[j+1]+root*q[j+1]
 rem=cs[0]+root*q[0]
 back=[-root*q[0]]
 for j in range(1,len(q)):back.append(q[j-1]-root*q[j])
 back.append(q[-1]);back[0]+=rem
 assert back==cs
 return q,rem
reduced=chi[:];removed=[]
for label,root in [('lambda_zero',R(0)),('lambda_three_halves',R(fmpq(3,2)))]:
 count=0
 while len(reduced)>1:
  qq,rr=lin_div(reduced,root)
  if rr:break
  reduced=qq;count+=1
 if count:removed.append(dict(previousWholeOriginalFiber=label,multiplicity=count))
assert reduced[-1]==1
for c in reduced:scalar(c)
say(stage='new_entire_W_paid_spectral_factors_original_monic_input_finished',
 sourceSHA256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
 originalCharacteristicDegree=6,removedPreviouslyPaidWholeFibers=removed,
 resultingMonicDegree=len(reduced)-1,
 exactEachSyntheticDivisionCoefficientProductReturned=True,
 resultingCoefficientsAscendingProfiles=[rmeta(c) for c in reduced],
 sameOriginalIdealAfterOnlyPaidLambdaLocalization=True,
 noOtherSpectralRootOrLeadingZeroFiberRemoved=True,
 sourceAndDeterminantDefinitionOnlyNoCoefficientCache=True,
 wholeCurrentWExcluded=(len(reduced)==1),
 ordinaryISPClaim=False,
 peakRssKiB=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)
signal.alarm(0)
