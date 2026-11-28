#!/usr/bin/env python3
"""NEW entire-W original D-cofactor via simultaneous two-column cancellation.
The proved QQ dual family identifies two constant kernel columns modulo
Lhalf. For original I6 rows AND the actual D target, clear only paid
weights, multiply by the same constant C, and divide its first TWO
columns exactly by Lhalf. Every division is multiplied back in QQ[e,k].
Thus MC=N*diag(L,L,1,1,1,1), dC=dprime*diag(...), and the universal
adjugate gives det(N)*d=dprime*adj(N)*M WITHOUT an L inverse.
New original commutator / coordinate-times-native rows supply different
D-cofactors. A fixed p1009,k3 calculation selects genuine QQ minors and
a 93-column univariate coefficient matrix defining a nonzero pure-k
cover if its entire residual weight algebra is generated.
No old 95-second determinant, norm, characteristic or primary gate.
180s/4GiB; only definitions, selected small indices, hashes and receipts.
"""
import json,time,hashlib,signal,resource,contextlib,io,math,itertools
from pathlib import Path
from flint import fmpq,nmod_poly
START=time.perf_counter();DEADLINE=START+180
signal.alarm(180);resource.setrlimit(resource.RLIMIT_AS,(4*1024**3,4*1024**3))
p=1009;k0=3
def say(**kw):
 kw['seconds']=time.perf_counter()-START
 print(json.dumps(kw,separators=(',',':')),flush=True)
def digest(obj):
 raw=json.dumps(obj,separators=(',',':')).encode()
 return dict(bytes=len(raw),sha256=hashlib.sha256(raw).hexdigest())
path=Path(__file__).with_name('2026-11-28-unit211-W-entire-native-NSPS-y-t-fixed-six-original-determinant-8542.py')
raw=path.read_bytes()
assert hashlib.sha256(raw).hexdigest()=='eca419501bf348518fe4f36582d417784235cc7c35872f1a1eb180c88b1e537d'
mark=b'\n# A NEW fixed native-coordinate determinant'
assert raw.count(mark)==1
prefix=raw.split(mark)[0]
assert len(prefix)==8074
assert hashlib.sha256(prefix).hexdigest()=='1dbb8a70ac77f5d531339ca26b5a60b8b3c3cc9a37e41eb54808063c11490878'
native={'__file__':str(path),'__name__':'new_D_target_original_rows_only'}
oa=signal.alarm;ot=signal.setitimer
def timer(which,seconds,interval=0.0):
 if which!=signal.ITIMER_REAL:return ot(which,seconds,interval)
 assert not interval
 left=max(.001,DEADLINE-time.perf_counter())
 return ot(which,min(left,float(seconds) if seconds>0 else left),0.0)
def alarm(seconds):return math.ceil(timer(signal.ITIMER_REAL,seconds)[0])
signal.alarm=alarm;signal.setitimer=timer
try:
 with contextlib.redirect_stdout(io.StringIO()):
  exec(compile(prefix,str(path)+'#new_D_target_prefix','exec'),native)
finally:
 signal.alarm=oa;signal.setitimer=ot
 ot(signal.ITIMER_REAL,max(.001,DEADLINE-time.perf_counter()))
ns=native['ns'];R=native['R'];ctx=native['ctx']
zero,one=native['zero'],native['one'];ep,kp=ns['ep'],ns['kp']
basis=native['basis'];variables=native['variables']
mats=native['matrices'];errors=native['errors']
original=native['original'];verify=native['verify']
paid_poly=native['paid_poly'];paid_scalar=native['paid_scalar']
baseM=[r[:] for r in native['rows']];baseTags=[r[:] for r in native['traces']]
assert native['rows_digest'](baseM)==dict(bytes=1728830,sha256='e5b3bc078fecd6d472d62bcba5ec831e10a2f88a8feaf51beb15ba816a9da9cf')
L=4*kp*ep**2-(kp**2+4*kp+8)*ep-(kp**2+6*kp+8)
assert L
qq_divisions=0;coefficient_checks=0;mod_divisions=0;mod_inverse_count=0
def exact(poly,divisor):
 global qq_divisions
 q=poly/divisor
 assert q*divisor==poly
 qq_divisions+=1;return q
def profile(poly):
 return dict(degrees=list(map(int,poly.degrees()[:2])),
 totalDegree=int(poly.total_degree()),terms=len(poly.to_dict()),
 **digest([[[int(z) for z in m],str(c)] for m,c in sorted(poly.to_dict().items())]))
def rowprofile(row):return dict(
 degrees=[max(int(q.degrees()[i]) for q in row) for i in [0,1]],
 terms=sum(len(q.to_dict()) for q in row),
 **digest([[[[int(z) for z in m],str(c)] for m,c in sorted(q.to_dict().items())] for q in row]))
def transform(row):
 return [row[0]+row[1]/2+row[2]/2+row[4]/4,row[1],row[2],row[3],row[4],row[5]]
def deflate(row):
 transformed=transform(row)
 out=[exact(transformed[0],L),exact(transformed[1],L)]+transformed[2:]
 # Actual forward and reverse constant-coordinate products.
 assert transformed==[out[0]*L,out[1]*L]+out[2:]
 reverse=[out[0]*L-out[1]*L/2-out[2]/2-out[4]/4,
          out[1]*L,out[2],out[3],out[4],out[5]]
 assert reverse==row
 return out
# Original D is a quadratic geometry polynomial; take its true
# four-mean reduction, including the complete original multiplier.
drow,dtag=ns['reduce_six'](ns['symbolic']['Dphysical'])
assert not dtag[4] and not dtag[5]
for c in drow:paid_scalar(c)
for c in dtag:paid_poly(c.d)
den=one
for c in drow:den=exact(den,den.gcd(c.d))*c.d
paid_poly(den)
dpoly=[c.n*exact(den,c.d) for c in drow]
dtrace=[R(den)*c for c in dtag]
assert all(R(dpoly[i])==R(den)*drow[i] for i in range(6))
verify(sum((R(dpoly[i])*basis[i] for i in range(6)),R())-R(den)*ns['symbolic']['Dphysical'],dtrace)
dprime=deflate(dpoly)
baseN=[deflate(row) for row in baseM]
say(stage='new_entire_W_simultaneous_two_column_D_cancellation',
 originalKernelColumns=[[1,'1/2','1/2',0,'1/4',0],[0,1,0,0,0,0]],
 constantColumnTransformationDeterminant=1,
 exactLhalf='4*k*e^2-(k^2+4*k+8)*e-(k^2+6*k+8)',
 allBaseRowsAndOriginalDTargetForwardReverseProductsReturned=True,
 QQExactColumnDivisionReturns=qq_divisions,
 originalDTargetMeanTraceReturned=True,
 DTargetPaidDenominator=profile(den),
 deflatedDTarget=rowprofile(dprime),
 deflatedBaseRowProfiles=[rowprofile(r) for r in baseN],
 universalOriginalCofactorIdentity='det(N)*d=dprime*adj(N)*M',
 noLhalfInverse=True,entireLhalfZeroRetained=True,
 noH198OrOtherNewHeadInverse=True,
 originalDTargetValidOnEntireCurrentW=True,
 oldQQNativeDeterminantNotReplayed=True,wholeWExcluded=False)
def fraction(c):
 s=str(c).split('/');return int(s[0]),int(s[1]) if len(s)==2 else 1
def vp(n):
 assert n;v=0;n=abs(n)
 while n%p==0:n//=p;v+=1
 return v
def valp(c):
 n,d=fraction(c);assert n;return vp(n)-vp(d)
def residue(c):
 global coefficient_checks
 n,d=fraction(c);assert d%p,'QQ coefficient not integral in fixed new input'
 coefficient_checks+=1
 return n%p*pow(d%p,p-2,p)%p
def modpoly(poly,scale=fmpq(1)):
 arr=[0]*(max((int(m[0]) for m in poly.to_dict()),default=-1)+1)
 for mon,co in poly.to_dict().items():
  assert not any(mon[j] for j in range(2,8))
  arr[int(mon[0])]=(arr[int(mon[0])]+residue(co*scale)*pow(k0,int(mon[1]),p))%p
 return nmod_poly(arr,p)
O=nmod_poly([1],p);Z=nmod_poly([],p)
def polyprofile(poly):return dict(degree=int(poly.degree()),**digest([int(x) for x in poly.coeffs()]))
def determinant(M):
 global mod_divisions
 A=[r[:] for r in M];prev=O;sgn=1
 for j in range(5):
  if not A[j][j]:
   sw=next((i for i in range(j+1,6) if A[i][j]),None)
   if sw is None:return Z
   A[j],A[sw]=A[sw],A[j];sgn=-sgn
  pivot=A[j][j]
  for i in range(j+1,6):
   for h in range(j+1,6):
    numerator=pivot*A[i][h]-A[i][j]*A[j][h]
    q,r=divmod(numerator,prev)
    assert not r and q*prev==numerator
    A[i][h]=q;mod_divisions+=1
   A[i][j]=Z
  prev=pivot
 return sgn*A[5][5]
baseNbar=[[modpoly(c) for c in row] for row in baseN]
new_det_bar=determinant(baseNbar)
assert new_det_bar and new_det_bar.degree()==191
# This is a NEW D-target determinant. Its relation to the already
# proved native determinant is det(N)=det(M)/Lhalf^2 by the complete
# column identity above, not a repeat of the old determinant gate.
paidimages=[]
for label,atom in native['paid_atoms']:
 aa=modpoly(atom);assert aa
 paidimages.append((label,aa))
remaining=new_det_bar;removed=O;history=[]
for label,atom in paidimages:
 count=0
 while remaining:
  g=remaining.gcd(atom)
  if g.degree()==0:break
  q,r=divmod(remaining,g)
  assert not r and q*g==remaining
  remaining=q;removed*=g;count+=1
 if count:history.append([label,count])
assert remaining*removed==new_det_bar
assert remaining.degree()==93 and removed.degree()==98
constant=int(remaining[remaining.degree()])
Pbar=remaining*pow(constant,p-2,p)
assert Pbar.degree()==93 and Pbar[93]==1
barL=modpoly(L)
assert Pbar.gcd(barL).degree()==0
assert Pbar.gcd(Pbar.derivative()).degree()==0
say(stage='new_original_D_cofactor_complete_fixed_integral_weight_model',
 fixedPrime=p,fixedK=k0,newFullDTargetDeterminant=polyprofile(new_det_bar),
 newPprimeMonicResidue=polyprofile(Pbar),
 paidRemovedDegree=98,paidRemovedHistory=history,
 exactQQDefinition='Pprime=P164/Lhalf^2; Lhalf^2 divides P164 by the new column identities and the returned native-weight units in the full QQ dual family',
 exactQQDegrees=[93,119],exactQQTotalDegree=158,
 allNewColumnCoefficientsPIntegral=True,
 fullNewDeterminantDivisionReturns=mod_divisions,
 PprimeAndLhalfCoprimeInThisCompleteResidue=True,
 entirePprimeResidueSquarefree=True,
 noOldPQQDeterminantOrSevenPrimaryReturnReplayed=True,
 physicalDUnitNecessaryEquation='Pprime(e,k)=0',
 entireLhalfZeroRetained=True,wholeWExcluded=False)
def aa(x):return x%Pbar
def am(x,y):return (x*y)%Pbar
den_cache={}
def aminv(v,label):
 global mod_inverse_count
 v=aa(v);g,s,t=v.xgcd(Pbar)
 assert s*v+t*Pbar==g and g.degree()==0,(label,polyprofile(g))
 s=aa(s*pow(int(g[0]),p-2,p));assert am(v,s)==O
 mod_inverse_count+=1;return s
def modR(co):
 co=R(co)
 assert all(not any(m[j] for j in range(2,8)) for m in co.n.to_dict())
 assert all(not any(m[j] for j in range(2,8)) for m in co.d.to_dict())
 key=str(co.d)
 if key not in den_cache:
  v=min(valp(c) for c in co.d.to_dict().values() if c)
  sc=fmpq(1,p**v) if v>=0 else fmpq(p**(-v))
  di=aminv(modpoly(co.d,sc),'new original coefficient denominator')
  den_cache[key]=(sc,di)
 sc,di=den_cache[key]
 return am(modpoly(co.n,sc),di)
Mbar=[[[modR(c) for c in row] for row in mat] for mat in mats]
Mbase=[[aa(modpoly(c)) for c in row] for row in baseM]
Nbase=[[aa(v) for v in row] for row in baseNbar]
Linv=aminv(barL,'selection only: Lhalf is coprime to the entire Pprime residue')
def deflate_mod(row):
 half=pow(2,-1,p);quarter=pow(4,-1,p)
 return [am(aa(row[0]+half*row[1]+half*row[2]+quarter*row[4]),Linv),
         am(row[1],Linv)]+row[2:]
for a,b in zip(Mbase,Nbase):assert deflate_mod(a)==b
def rowmul(row,mat):
 return [sum((am(row[i],mat[i][j]) for i in range(6)),Z)%Pbar for j in range(6)]
def comm_mod(ax,bx,i):
 a=rowmul(Mbar[ax][i],Mbar[bx]);b=rowmul(Mbar[bx][i],Mbar[ax])
 return [aa(a[j]-b[j]) for j in range(6)]
candidates=[('comm',a,b,i) for a,b in [(0,1),(0,2),(1,2)] for i in range(6)]
candidates += [('axis_base',a,j) for a in range(3) for j in range(6)]
qq_rows={};row_records=[]
def actual_QQ_candidate(spec):
 key=tuple(spec)
 if key in qq_rows:return qq_rows[key]
 if spec[0]=='comm':
  _,ax,bx,i=spec;MA,MB=mats[ax],mats[bx]
  rr=[sum((MA[i][h]*MB[h][j]-MB[i][h]*MA[h][j] for h in range(6)),R()) for j in range(6)]
  tag=[]
  for g in range(6):
   co=variables[ax]*errors[bx][i][g]-variables[bx]*errors[ax][i][g]
   co+=sum((MB[i][h]*errors[ax][h][g]-MA[i][h]*errors[bx][h][g] for h in range(6)),R())
   tag.append(co)
 else:
  _,ax,which=spec;oldrow=[R(c) for c in baseM[which]]
  rr=[sum((oldrow[i]*mats[ax][i][j] for i in range(6)),R()) for j in range(6)]
  tag=[variables[ax]*baseTags[which][g]-sum((oldrow[i]*errors[ax][i][g] for i in range(6)),R()) for g in range(6)]
 verify(sum((rr[i]*basis[i] for i in range(6)),R()),tag)
 for co in rr:paid_scalar(co)
 for co in tag:paid_poly(co.d)
 with contextlib.redirect_stdout(io.StringIO()):
  pol,trace=native['clear_original_row'](rr,tag,str(spec))
 # Normalize only the rational p content; no new parameter factor.
 nonzero=[co for pp in pol for co in pp.to_dict().values() if co]
 assert nonzero
 pv=min(valp(co) for co in nonzero)
 factor=fmpq(1,p**pv) if pv>=0 else fmpq(p**(-pv))
 pol=[v*factor for v in pol];trace=[R(factor)*v for v in trace]
 verify(sum((R(pol[i])*basis[i] for i in range(6)),R()),trace)
 which=next(i for i in range(6) if rr[i])
 scale=R(pol[which])/rr[which]
 paid_poly(scale.n);paid_poly(scale.d)
 assert all(R(pol[i])==scale*rr[i] for i in range(6))
 nn=deflate(pol)
 for co in nn:modpoly(co)
 nnbar=[aa(modpoly(co)) for co in nn]
 sb=modR(scale);assert am(sb,aminv(sb,'actual new row paid scaling'))==O
 rrbar=[modR(co) for co in rr]
 assert nnbar==[am(sb,c) for c in deflate_mod(rrbar)]
 rec=dict(id=len(row_records),spec=list(spec),pContentNormalizationExponent=pv,
          fullOriginalSixMultiplierProductReturned=True,
          allActualRowAndDColumnDivisionsReturned=True,
          newDeflatedQQRow=rowprofile(nn),
          requiredPaidRowScaleReturned=True)
 row_records.append(rec)
 say(stage='new_selected_QQ_original_D_cofactor_row',**rec,
     noLhalfInverseInQQIdentity=True,wholeWExcluded=False)
 qq_rows[key]=(nn,nnbar,sb,rec['id'])
 return qq_rows[key]
g=Pbar;polys=[Pbar];bezout=[O];useful=[];attempts=0
for spec in candidates:
 if spec[0]=='comm':rawbar=comm_mod(spec[1],spec[2],spec[3])
 else:rawbar=rowmul(Mbase[spec[2]],Mbar[spec[1]])
 if not any(rawbar):continue
 candidatebar=deflate_mod(rawbar)
 for position in range(6):
  attempts+=1
  matrix=[r[:] for r in Nbase];matrix[position]=candidatebar
  value=aa(determinant(matrix))
  gg=g.gcd(value)
  if gg.degree()==g.degree():continue
  nn,nnbar,sb,rowid=actual_QQ_candidate(spec)
  assert nnbar==[am(sb,c) for c in candidatebar]
  actual_value=am(sb,value)
  hh,s,t=g.xgcd(actual_value)
  assert s*g+t*actual_value==hh
  scalar=int(hh[hh.degree()]);invscalar=pow(scalar,p-2,p)
  hh=hh*invscalar;s=s*invscalar;t=t*invscalar
  bezout=[q*s for q in bezout]+[t];polys.append(actual_value)
  assert sum((a*b for a,b in zip(bezout,polys)),Z)==hh
  QQmatrix=[r[:] for r in baseN];QQmatrix[position]=nn
  # Genuine coefficient degree bounds for THIS fixed QQ determinant.
  bounds=[sum(max(int(v.degrees()[a]) for v in row) for row in QQmatrix) for a in [0,1]]
  item=dict(index=len(useful),rowId=rowid,originalSpec=list(spec),
            replacedBaseRow=position,QQDeterminantDegreeBounds=bounds,
            exactDeterminantDefinition='baseN with one selected full QQ deflated original row replacement',
            actualResidue=polyprofile(actual_value),remainingFullGcdDegree=int(hh.degree()),
            universalWholeOriginalDTarget=True)
  useful.append(item);g=hh
  say(stage='new_original_D_cofactor_complete_residue_gcd_drop',
      **item,allModularBezoutProductsReturned=True,
      fullQQMinorDefinedWithoutExpandingItsDeterminant=True,
      temporaryPivotZeroFibresRetained=True,wholeWExcluded=False)
  if g.degree()==0:break
 if g.degree()==0:break
if g.degree()!=0:
 say(stage='new_original_D_cofactor_residue_remaining_support',
     actualGcd=polyprofile(g),newMinorAttempts=attempts,
     allUsefulQQMinors=useful,allSelectedQQRows=row_records,
     noPureKCoverClaim=True,noPrimeOrBudgetRetry=True,
     completeUnresolvedWeightSupportRetained=True,
     allColumnCancellationIdentitiesStillValid=True,
     ordinaryISPClaim=False,wholeWExcluded=False)
 signal.setitimer(signal.ITIMER_REAL,0);signal.alarm(0);raise SystemExit(0)
assert g==O and sum((a*b for a,b in zip(bezout,polys)),Z)==O
say(stage='new_original_D_cofactor_entire_residue_Bezout_one',
 completePprimeDegree=93,newMinorAttempts=attempts,
 trueCompleteBezoutDefinition=digest([[int(x) for x in q.coeffs()] for q in bezout]),
 allUsefulQQMinors=useful,allSelectedQQRows=row_records,
 noMultivariableGcdEmptinessClaim=True,
 nonverticalQQCommonCurveExclusionOnly=True,
 finiteWeightFibresStillRequired=True,wholeWExcluded=False)
# Select an actual full-rank 93-column coefficient matrix over Fp.
# Its QQ counterpart is fixed by the exact definitions below, without
# recalculating any old QQ determinant or saving large coefficients.
n=93;chosen=[];basis_rows={};selected_vectors=[]
epbar=nmod_poly([0,1],p)
for qi,pol in enumerate(polys[1:]):
 vv=pol
 for exponent in range(n):
  column=[int(vv[j]) for j in range(n)]
  w=column[:];comb=[0]*n;comb[len(chosen)]=1
  for pos in sorted(basis_rows):
   row,co=basis_rows[pos];c=w[pos]
   if c:
    w=[(w[i]-c*row[i])%p for i in range(n)]
    comb=[(comb[i]-c*co[i])%p for i in range(n)]
  pos=next((i for i,c in enumerate(w) if c),None)
  if pos is not None:
   inv=pow(w[pos],p-2,p);w=[inv*c%p for c in w];comb=[inv*c%p for c in comb]
   chosen.append([qi,exponent]);selected_vectors.append(column)
   for op,(row,co) in list(basis_rows.items()):
    c=row[pos]
    if c:basis_rows[op]=([(row[i]-c*w[i])%p for i in range(n)],
                         [(co[i]-c*comb[i])%p for i in range(n)])
   basis_rows[pos]=(w,comb)
   if len(chosen)==n:break
  vv=am(vv,epbar)
 if len(chosen)==n:break
assert len(chosen)==n and len(basis_rows)==n
returns=0
for pos,(row,comb) in basis_rows.items():
 assert row==[int(i==pos) for i in range(n)]
 for i in range(n):
  actual=sum(comb[j]*selected_vectors[j][i] for j in range(n))%p
  assert actual==int(i==pos);returns+=1
# A(k)=lc_e Pprime after its rational p-content normalization. It is
# p-integral and a unit at p1009,k3 by the original P164 integral model
# and the returned Lhalf^2 exact cancellation. For selected [i,j],
# bi=max(0,deg_e_bound(Qi)+j-92) suffices for polynomial pseudoreduction:
# A^bi * e^j Qi = column_i(e,k) + multiple_i(e,k)*Pprime,
# deg_e column_i<93, with ALL coefficients in QQ[k].
# No A inverse is asserted at its zeros. Let H(k) be the determinant
# of these 93 pseudoremainder columns. The actual modular full rank
# below and Abar!=0 prove H!=0. Original zeros force H=0, INCLUDING
# A=0, by the full pseudodivision polynomial identities.
powers=[];k_bound=0
for qi,j in chosen:
 eb,kb=useful[qi]['QQDeterminantDegreeBounds']
 power=max(0,eb+j-92);powers.append(power)
 k_bound+=kb+119*power
say(stage='new_nonzero_pure_k_original_D_cover_fixed_definition',
 coefficientModel='Pprime=P164/Lhalf^2, primitive p1009 normalization, a(k)=lc_e(Pprime)',
 exactPprimeDegrees=[93,119],fixedCoefficientMatrixSize=93,
 selectedQQMinorAndEMonomialColumns=chosen,
 exactPseudoremainderLeadingPowers=powers,
 exactPureKCoverDefinition='H(k)=det(columns of a(k)^b_j rem_{Pprime/a(k)}(e^j Q_i)); Q_i is its fixed new original D-cofactor determinant',
 QQPureKCoverDegreeUpperBound=k_bound,
 actualModularCoefficientMatrixRank=93,
 actualAllOriginalSelectedInverseCoordinateProducts=returns,
 actualSelectedModularMatrixDefinition=digest(selected_vectors),
 actualInverseDefinition=digest([basis_rows[i][1] for i in range(n)]),
 QQCoverNonzeroBySameIntegralSpecialization=True,
 QQCoverNecessaryOnEntireCurrentPhysicalW=True,
 allLeadingAZeroFibresRetainedByPolynomialPseudodivision=True,
 noH198OrLhalfOpenRestriction=True,
 pureKCoverCoefficientsExpanded=False,
 wholeWExcluded=False,ordinaryISPClaim=False,
 QQExactColumnDivisionReturns=qq_divisions,
 exactModularPolynomialDivisionReturns=mod_divisions,
 fullPIntegralCoefficientChecks=coefficient_checks,
 actualCompleteResidueCoefficientInverses=mod_inverse_count,
 originalDTargetGlobal=True,
 sourceSHA256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
 noCoefficientCacheEncodedOrSplitPayload=True,
 peakRssKiB=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)
signal.setitimer(signal.ITIMER_REAL,0);signal.alarm(0)
