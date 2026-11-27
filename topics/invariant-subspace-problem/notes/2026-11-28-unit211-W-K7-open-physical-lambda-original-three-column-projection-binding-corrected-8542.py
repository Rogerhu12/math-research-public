#!/usr/bin/env python3
"""BINDING CORRECTION of the unexecuted mathematical gate after ebed line73.
The original degree assertion is unchanged; its XY monomial is now bound
per coefficient, rather than the stale (0,2) left by the head-check loop.
The first failure and frozen source remain intact.
NEW physical-lambda three-generator original input on the explicit K7!=0 chart.
Three original mean quadratics give x^2,xy,y^2 rules over QQ[e,k][lambda].
The original N1, both commutators, NS/PS and same-point products are kept.
Actual three-column cofactors give scalar lambda polynomials. A new fixed
Sylvester determinant of two true original combinations is attempted.
Every unproved coefficient-content zero fibre is retained as a factor.
No old native six-determinant, no old resultant or old generic gate is run.
180 seconds / 4 GiB; no recomputable data cache or encoded payload.
"""
import json,time,hashlib,signal,resource,contextlib,io,math,itertools
from pathlib import Path
from flint import fmpq,fmpq_poly
started=time.perf_counter();deadline=started+180
signal.alarm(180);resource.setrlimit(resource.RLIMIT_AS,(4*1024**3,4*1024**3))
def say(**d):
 d['seconds']=time.perf_counter()-started
 print(json.dumps(d,separators=(',',':')),flush=True)
def meta(p):
 dd=p.to_dict()
 b=json.dumps([[[int(x) for x in mon],str(c)] for mon,c in sorted(dd.items())],separators=(',',':')).encode()
 return dict(degrees=list(map(int,p.degrees()[:5])),totalDegree=int(p.total_degree()),terms=len(dd),
             bytes=len(b),sha256=hashlib.sha256(b).hexdigest())
dep=Path(__file__).with_name('2026-11-28-unit211-W-original-physical-lambda-four-heads-and-affine-identity-8542.py')
raw=dep.read_bytes()
assert hashlib.sha256(raw).hexdigest()=='bc02ab0525d4d32910ecc8a0264af16a089df1f339fb94078a5fb3c1572e3433'
mark=b'\ncof=[(-1)**i*det3'
assert raw.count(mark)==1
prefix=raw.split(mark)[0]
assert len(prefix)==6276
assert hashlib.sha256(prefix).hexdigest()=='36ee65e4032920e33868259dc740696cc70c5dd70cddb94de17a142c2a76dea6'
ns={'__file__':str(dep),'__name__':'necessary_Gram_and_physical_lambda_only'}
with contextlib.redirect_stdout(io.StringIO()):
 exec(compile(prefix,str(dep)+'#necessary_definitions_only','exec'),ns)
signal.alarm(max(1,math.ceil(deadline-time.perf_counter())))
R=ns['R'];ctx=ns['ctx'];zero=ns['zero'];one=ns['one']
ep,kp,xp,yp,Lp=ctx.gens()[:5]
xx,yy,L=map(R,[xp,yp,Lp]);original=ns['new'];polys=ns['polys'];scales=ns['scales']
heads=ns['heads'];det3=ns['det3'];strip=ns['strip'];pay=ns['pay']
K=12*ep**2*kp**2-ep*kp**3+8*ep*kp**2-kp**3-4*kp**2-16*kp-16
# EXPLICIT complement. The entire K7=0 branch is not removed by this source.
ns['paid_atoms'].append(('explicit_K7_nonzero_chart',K))
H=heads[:3];delta=det3(H);assert delta;pay(delta)
def det2(A):return A[0][0]*A[1][1]-A[0][1]*A[1][0]
inv=[]
for j in range(3):
 inv.append([R((-1)**(i+j)*det2([[H[r][c] for c in range(3) if c!=j] for r in range(3) if r!=i]),delta)
             for i in range(3)])
for i in range(3):
 for j in range(3):
  assert sum((inv[i][h]*R(H[h][j]) for h in range(3)),R())==int(i==j)
def xycoeff(rr):
 rr=R(rr);out={}
 assert all(mon[2]==mon[3]==0 and not any(mon[j] for j in range(5,8)) for mon in rr.d.to_dict())
 for mon,c in rr.n.to_dict().items():
  assert not any(mon[j] for j in range(5,8))
  ij=(int(mon[2]),int(mon[3]))
  out[ij]=out.get(ij,zero)+c*ep**int(mon[0])*kp**int(mon[1])*Lp**int(mon[4])
 return {ij:R(v,rr.d) for ij,v in out.items() if v}
def verify(p,tag):
 assert sum((tag[i]*original[i] for i in range(6)),R())==p
q=[];tags=[];qheads=[(2,0),(1,1),(0,2)]
for j in range(3):
 pp=sum((inv[j][i]*R(polys[i]) for i in range(3)),R())
 tag=[inv[j][i]*scales[i] if i<3 else R() for i in range(6)]
 verify(pp,tag)
 cc=xycoeff(pp)
 for h,mon in enumerate(qheads):assert cc.get(mon,R())==int(j==h)
 assert all(sum(mon)<=1 or mon==qheads[j] for mon in cc)
 # Correct the former stale-loop-variable bug: bind EACH actual XY monomial
 # to ITS coefficient. Keep exactly the same weighted-degree assertion.
 for mon,cf in cc.items():
  pay(cf.d)
  actual_degree=max((int(mm[4]) for mm in cf.n.to_dict()),default=-1)
  say(stage='new_K7_open_actual_rule_coefficient_degree',rule=j,
      xyMonomial=list(mon),lambdaDegree=actual_degree,
      weightedDegree=actual_degree+sum(mon),requiredBound=2,
      claimExcluded=False)
  assert all(int(mm[4])+sum(mon)<=2 for mm in cf.n.to_dict())
 q.append(pp);tags.append(tag)
basis=[R(1),xx,yy];freemons=[(0,0),(1,0),(0,1)]
def monomial(ij):return xx**ij[0]*yy**ij[1]
def reduce_row(inputp,inputtag=None):
 pp=R(inputp);rem=R()
 tag=[R() for _ in range(6)] if inputtag is None else inputtag[:]
 while pp:
  cm=xycoeff(pp);mon=max(cm,key=lambda a:(sum(a),a[0],a[1]));cf=cm[mon]
  if sum(mon)<=1:
   term=cf*monomial(mon);rem+=term;pp-=term;continue
  j=next(j for j,lm in enumerate(qheads) if lm[0]<=mon[0] and lm[1]<=mon[1])
  dif=(mon[0]-qheads[j][0],mon[1]-qheads[j][1]);mul=cf*monomial(dif)
  pp-=mul*q[j];tag=[tag[g]-mul*tags[j][g] for g in range(6)]
 verify(rem-inputp if inputtag is None else rem,tag)
 cm=xycoeff(rem);assert all(m in freemons for m in cm)
 row=[cm.get(m,R()) for m in freemons]
 for cf in row:pay(cf.d)
 return row,tag
matrices=[];errors=[]
for var in [xx,yy]:
 mat=[];err=[]
 for b in basis:
  row,tag=reduce_row(var*b);mat.append(row);err.append([-z for z in tag])
 matrices.append(mat);errors.append(err)
say(stage='new_K7_open_original_three_rules_and_six_multiplication_columns',
 explicitChart='K7 != 0',originalMeanRows=[0,1,2],
 allNineHeadInverseProductsVerified=True,allOriginalRuleAndMultiplicationProductsVerified=True,
 basis=['1','x','y'],coefficientRing='current weight ring with K7 inverted, polynomial in lambda',
 noThreeGeneratorFreenessAssumed=True,noWeightFinitenessInferred=True,
 entireK7ZeroBranchRetainedSeparately=True,claimExcluded=False)
rows=[];rowtags=[];labels=[]
def addrow(row,tag,label):
 if not any(row):return None
 verify(sum((row[j]*basis[j] for j in range(3)),R()),tag)
 den=one
 for cf in row:
  pay(cf.d);den*=cf.d/den.gcd(cf.d)
 pay(den)
 pp=[cf.n*(den/cf.d) for cf in row];removed=one
 for name,atom in ns['paid_atoms']:
  while any(pp):
   g=atom
   for p in pp:g=g.gcd(p)
   if g.total_degree()==0:break
   nq=[p/g for p in pp]
   assert all(nq[i]*g==pp[i] for i in range(3))
   pp=nq;removed*=g
 pay(removed)
 norm=next(p for p in pp if p).coefficient(0)
 pp=[p/norm for p in pp];factor=R(den,removed)/norm
 trace=[factor*z for z in tag]
 assert all(R(pp[j])==factor*row[j] for j in range(3))
 verify(sum((R(pp[j])*basis[j] for j in range(3)),R()),trace)
 idx=len(rows);rows.append(pp);rowtags.append(trace);labels.append(label)
 say(stage='new_K7_open_original_polynomial_three_column_row',index=idx,label=label,
     maxDegrees=[max(int(p.degrees()[j]) for p in pp) for j in [0,1,4]],
     totalTerms=sum(len(p.to_dict()) for p in pp),allOriginalProductsVerified=True,
     allDenominatorsPaidOnExplicitChart=True,claimExcluded=False)
 return idx
for gen in [3,4,5]:
 row,tag=reduce_row(original[gen],[R(int(i==gen)) for i in range(6)])
 addrow(row,tag,['E1','EBe','EBo','N1','NS','PS'][gen])
A,B=matrices
for i in range(3):
 row=[sum((A[i][h]*B[h][j]-B[i][h]*A[h][j] for h in range(3)),R()) for j in range(3)]
 tag=[xx*errors[1][i][g]-yy*errors[0][i][g]
      +sum((B[i][h]*errors[0][h][g]-A[i][h]*errors[1][h][g] for h in range(3)),R()) for g in range(6)]
 addrow(row,tag,'same_point_commutator_'+str(i))
initial_count=len(rows)
for idx in range(initial_count):
 if labels[idx] not in ['N1','same_point_commutator_1','same_point_commutator_2']:continue
 for axis,var in enumerate([xx,yy]):
  row=[sum((R(rows[idx][i])*matrices[axis][i][j] for i in range(3)),R()) for j in range(3)]
  tag=[var*rowtags[idx][g]-sum((R(rows[idx][i])*errors[axis][i][g] for i in range(3)),R()) for g in range(6)]
  addrow(row,tag,labels[idx]+'*'+'xy'[axis])
def lcoeff(p):
 out={}
 for mon,c in p.to_dict().items():
  assert mon[2]==mon[3]==0 and not any(mon[j] for j in range(5,8))
  h=int(mon[4]);out[h]=out.get(h,zero)+c*ep**int(mon[0])*kp**int(mon[1])
 return {h:p for h,p in out.items() if p}
def specialize(p,ek):
 cm=lcoeff(p);n=max(cm,default=-1);ans=[fmpq(0) for _ in range(n+1)]
 for h,c in cm.items():
  for mon,v in c.to_dict().items():
   assert not any(mon[j] for j in range(2,8))
   ans[h]+=v*ek[0]**int(mon[0])*ek[1]**int(mon[1])
 return fmpq_poly(ans)
def lambda_paid_strip(p,tag):
 # lambda: R150-appendix-essential-four-unit-two-plus-one-plus-one-original-U-value-atlas.md.
 # 3-2lambda: R150-appendix-unit211-W-lambda-three-halves-complete-original-exclusion.md.
 # These are existing whole-W geometric units. Only these
 # two geometric factors may be removed; all weight content stays intact.
 removed=one
 for atom in [Lp,3-2*Lp]:
  while p:
   g=p.gcd(atom)
   if g.total_degree()==0:break
   qq=p/g;assert qq*g==p;p=qq;removed*=g
 trace=[z/R(removed) for z in tag]
 verify(R(p),trace)
 return p,trace
cofactors=[];cofactor_tags=[];triples=[];selected=None
for tri in itertools.combinations(range(len(rows)),3):
 # Use a new original minor only. Its three constant-column cofactors
 # and complete six-equation trace are multiplied back.
 C=[rows[i] for i in tri];d=det3(C)
 if not d:continue
 c=[(-1)**i*det2([[C[r][j] for j in [1,2]] for r in range(3) if r!=i]) for i in range(3)]
 for j in range(3):
  assert sum((c[i]*C[i][j] for i in range(3)),zero)==d*int(j==0)
 tag=[sum((R(c[i])*rowtags[tri[i]][g] for i in range(3)),R()) for g in range(6)]
 verify(R(d),tag)
 d,tag=lambda_paid_strip(d,tag)
 cofactors.append(d);cofactor_tags.append(tag);triples.append(tri)
 say(stage='new_K7_open_original_scalar_lambda_cofactor',
     index=len(cofactors)-1,originalRows=tri,profile=meta(d),
     allThreeColumnAndSixOriginalTraceProductsVerified=True,
     everyTemporaryZeroFibrePreserved=True,claimExcluded=False)
 # Numeric rational evaluation selects a potentially efficient pair only.
 # It does NOT certify any original fibre empty. The actual QQ[e,k]
 # fixed Sylvester determinant is subsequently computed and returned.
 if int(d.degrees()[4])==0:
  selected=(len(cofactors)-1,None,0,(3,5));break
 if len(cofactors)<2:continue
 selected=None
 for ek in [(3,5),(4,7),(5,3)]:
  values=[specialize(p,ek) for p in cofactors]
  if any(v.degree()!=int(p.degrees()[4]) for v,p in zip(values,cofactors)):continue
  gs=next(v for v in values if v)
  for v in values:gs=gs.gcd(v)
  if gs.degree()!=0:continue
  base=min(range(len(cofactors)),key=lambda i:values[i].degree())
  if values[base].degree()==0:
   selected=(base,None,0,ek);break
  limit=(len(cofactors)-1)*max(1,values[base].degree())+2
  for scalar in range(1,limit+1):
   other=sum((v*scalar**i for i,v in enumerate(values)),fmpq_poly())
   if other.degree()!=max(int(p.degrees()[4]) for p in cofactors):continue
   if values[base].gcd(other).degree()==0:
    selected=(base,None,scalar,ek);break
  if selected is not None:break
 if selected is not None:break
 if len(cofactors)>=16:break
if not cofactors:
 say(stage='accurate_K7_open_three_column_all_attempted_cofactors_zero',noUnitOrProjectionClaimed=True)
 raise SystemExit(2)
if selected is None:
 say(stage='accurate_K7_open_original_scalar_cofactors_without_selected_projection',
     cofactorCount=len(cofactors),allOriginalInputsRetained=True,noUnitOrProjectionClaimed=True)
 raise SystemExit(2)
base,_,scalar,ek=selected
C0=cofactors[base];tau0=cofactor_tags[base]
if scalar==0:
 assert int(C0.degrees()[4])==0
 say(stage='new_K7_open_original_weight_cofactor_direct',weightCurve=meta(C0),
     fullOriginalTraceAlreadyReturned=True,entireK7ZeroBranchRetainedSeparately=True,
     originalWeightCurveOnly=C0.total_degree()>0,
     wholeExplicitK7NonzeroChartExcluded=C0.total_degree()==0,claimExcluded=C0.total_degree()==0)
 raise SystemExit(0)
C1=sum((p*scalar**i for i,p in enumerate(cofactors)),zero)
tau1=[sum((R(scalar**i)*cofactor_tags[i][g] for i in range(len(cofactors))),R()) for g in range(6)]
verify(R(C1),tau1)
assert specialize(C0,ek).gcd(specialize(C1,ek)).degree()==0
# Content extraction introduces no geometric division: all its zero
# fibres are explicitly factors of the final NECESSARY weight cover.
def primitive_in_lambda(p):
 cc=lcoeff(p);h=next(iter(cc.values()))
 for cf in cc.values():h=h.gcd(cf)
 assert h
 out=p/h;assert out*h==p
 return h,out
h0,P0=primitive_in_lambda(C0);h1,P1=primitive_in_lambda(C1)
d0=int(P0.degrees()[4]);d1=int(P1.degrees()[4])
assert d0>=1 and d1>=1
assert specialize(P0,ek).degree()==d0 and specialize(P1,ek).degree()==d1
assert specialize(P0,ek).gcd(specialize(P1,ek)).degree()==0
cc0=lcoeff(P0);cc1=lcoeff(P1);n=d0+d1
# Ascending-power multiplication map (A,B)->A*P0+B*P1.
S=[[zero for j in range(n)] for i in range(n)]
for j in range(d1):
 for h,c in cc0.items():S[h+j][j]=c
for j in range(d0):
 for h,c in cc1.items():S[h+j][d1+j]=c
say(stage='new_K7_open_fixed_original_lambda_Sylvester_input',
     cofactorIndices=triples,baseCofactor=base,integerCombinationBase=scalar,
     selectionPoint=ek,selectionIsNotAnEmptinessTest=True,
     degrees=[d0,d1],matrixOrder=n,
     unprovedWeightContentFactors=[meta(h0),meta(h1)],
     allOriginalCofactorCombinationsVerified=True,
     allContentDivisionProductsVerified=True,
     completeLeadingZeroFibresRetained=True,claimExcluded=False)
def bareiss(A):
 A=[r[:] for r in A];prev=one;sign=1;count=0
 for col in range(len(A)-1):
  sw=next((i for i in range(col,len(A)) if A[i][col]),None)
  if sw is None:return zero,count
  if sw!=col:A[col],A[sw]=A[sw],A[col];sign=-sign
  pv=A[col][col]
  for i in range(col+1,len(A)):
   for j in range(col+1,len(A)):
    num=pv*A[i][j]-A[i][col]*A[col][j]
    qq=num/prev;assert qq*prev==num
    A[i][j]=qq;count+=1
   A[i][col]=zero
  prev=pv
  say(stage='new_K7_open_fixed_original_lambda_Sylvester_exact_step',
      step=col,exactDivisionProducts=count,pivot=meta(pv),
      pivotZeroFibresRetainedByPolynomialIdentity=True,claimExcluded=False)
 return sign*A[-1][-1],count
resultant,division_count=bareiss(S)
assert resultant
# The fixed full resultant is h0^d1*h1^d0*resultant. For point coverage,
# h0*h1*resultant has the identical zero set. No unproved factor is stripped.
# Output profiles and the exact source definition, not coefficient caches.
say(stage='new_K7_open_complete_original_weight_projection',
     primitiveFixedSylvesterDeterminant=meta(resultant),
     unprovedContentFactors=[meta(h0),meta(h1)],
     fullFixedResultantDefinition='h0**d1 * h1**d0 * det(S)',
     necessaryWeightCoverDefinition='h0 * h1 * det(S)',
     lambdaDegrees=[d0,d1],exactPolynomialDivisionProducts=division_count,
     allOriginalConstantCofactorsAndCombinationsVerified=True,
     originalFiniteCommonRootImpliesFixedDeterminantZero=True,
     allLambdaLeadingAndWeightContentZeroFibresRetained=True,
     explicitChart='K7 != 0',entireK7ZeroBranchRetainedSeparately=True,
     noIrreducibilityFinitenessOrWholeWEmptinessClaim=True,
     noDataCacheOrEncodedPayloadWritten=True)
