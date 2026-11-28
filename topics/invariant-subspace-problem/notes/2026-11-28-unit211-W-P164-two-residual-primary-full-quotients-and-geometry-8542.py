#!/usr/bin/env python3
"""NEW complete residual primary quotients and original geometry actions.
Only the TWO previously unresolved squared linear factors of Pbar97.
Compute their full F_1009 cokernel, retaining weight nilpotents, then
descend e,lambda,Z,T,D,K,ell,f,x,y,t by true original columns.
No rerun of the seven completed unit blocks. No mod-D nilpotence
promotion to QQ. The new full residue lengths give only a Nakayama
generic-dimension upper bound, for a later separate QQ family return.
180 seconds /4GiB. Source/parameters/hash/small receipt only.
"""
import json,time,hashlib,signal,resource,contextlib,io,math
from pathlib import Path
from flint import nmod_poly
START=time.perf_counter();DEADLINE=START+180
signal.alarm(180);resource.setrlimit(resource.RLIMIT_AS,(4*1024**3,4*1024**3))
p=1009
def say(**kw):
 kw['seconds']=time.perf_counter()-START
 print(json.dumps(kw,separators=(',',':')),flush=True)
def digest(obj):
 raw=json.dumps(obj,separators=(',',':')).encode()
 return dict(bytes=len(raw),sha256=hashlib.sha256(raw).hexdigest())
def profile(poly):return dict(degree=int(poly.degree()),**digest([int(c) for c in poly.coeffs()]))
name='2026-11-28-unit211-W-P164-complete-original-local-1164-model-8542.py'
path=Path(__file__).with_name(name);raw=path.read_bytes()
assert hashlib.sha256(raw).hexdigest()=='1dc4ded9c09f191ec06b3844bd8ad021660a90e3c6d966ffc7b6cdb6c0140c8b'
marker=b'\n # Full primary factorization, retaining every power.'
assert raw.count(marker)==1
prefix=raw.split(marker)[0]
assert len(prefix)==14553
assert hashlib.sha256(prefix).hexdigest()=='1eccc0f8803017cec318b633ae172fb0001ca946cd74dda1278331ce481a7ab8'
# Only new coefficient definitions; do not execute any old primary
# factorization, rank loop or seven completed unit returns.
prefix += b'\n return locals()\nnew_environment=run_model()\n'
ns={'__file__':str(path),'__name__':'new_two_residual_primary_quotient_definitions'}
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
  exec(compile(prefix,str(path)+'#new_quotient_geometry_input_only','exec'),ns)
finally:
 signal.alarm=oa;signal.setitimer=ot
 ot(signal.ITIMER_REAL,max(.001,DEADLINE-time.perf_counter()))
env=ns['new_environment'];modulus=ns['modulus'];columns=env['columns']
assert env['matrix_digest']==dict(bytes=599448,sha256='5b3c4d986b673f6a6a30733145793233861a9b305eba6d25b82ad5fd4b1340d7')
assert len(columns)==132 and all(len(c)==12 for c in columns)
C=env['C'];L=env['L'];Z=env['Z']
evar=C(nmod_poly([0,1],p))
fvalue=env['oldeval'](ns['old']['f'])
axes={'e':evar,'lambda':L,'Z':Z,'T':env['T'],'D':env['D'],
      'Kmoment':env['K'],'ell':env['ell'],'f':fvalue,
      'x':env['X'],'y':env['Y'],'t':env['tvalue']}
# These exact small factors were identified by the new original
# ell-half polynomial at k=3, with SHA matching the old residual record.
factors=[
 (2,nmod_poly([653,1],p),'0e2ca59eb1ba5cd7c67221120200547afbaa9f137206e2940fcfe4b608d30dbe'),
 (3,nmod_poly([774,1],p),'7991d9aecc5b33c423608ce58f4809610c92e69b2cdbd3cf9cc9334991f2fe41')]
g=nmod_poly([-35,-29,12],p)
assert 12*factors[0][1]*factors[1][1]==g
residual_product=nmod_poly([1],p)
for index,fac,sha in factors:
 assert profile(fac)['sha256']==sha
 residual_product*=fac**2
complement,remainder=divmod(modulus,residual_product)
assert not remainder and complement*residual_product==modulus
assert complement.degree()==93 and complement.gcd(residual_product).degree()==0
say(stage='new_two_complete_residual_primary_input',
 original132ColumnDefinition=env['matrix_digest'],
 exactResidualDegree=4,alreadyReturnedComplementDegree=93,
 twoSquaredLinearFactorsActuallyMatchOldHashes=True,
 originalEllHalfAtFixedK3=[-35,-29,12],
 noQQCurveFactorIdentificationClaim=True,
 sevenOldUnitBlocksNotReplayed=True,wholeWExcluded=False)
def matmul(A,B):
 if not A:return []
 return [[sum(A[i][h]*B[h][j] for h in range(len(B)))%p
          for j in range(len(B[0]))] for i in range(len(A))]
def matvec(A,v):return [sum(a*b for a,b in zip(row,v))%p for row in A]
def ident(n):return [[int(i==j) for j in range(n)] for i in range(n)]
def charpoly(A):
 n=len(A);B=ident(n);descending=[1]
 for j in range(1,n+1):
  AB=matmul(A,B);cc=-sum(AB[i][i] for i in range(n))*pow(j,-1,p)%p
  B=[[(AB[i][h]+cc*int(i==h))%p for h in range(n)] for i in range(n)]
  descending.append(cc)
 assert not any(x for row in B for x in row)
 return list(reversed(descending))
lengths=[]
for index,fac,sha in factors:
 h=fac**2;degree=int(h.degree());assert degree==2
 def flatten(value):
  vv=value.vector() if hasattr(value,'vector') else value
  out=[]
  for co in vv:
   rr=co%h;out.extend([int(rr[j]) for j in range(degree)])
  assert len(out)==24
  return out
 sourcecols=[];source_definitions=[]
 ep=nmod_poly([0,1],p)
 for j,col in enumerate(columns):
  for q in range(2):
   sourcecols.append(flatten([(co*(ep**q))%h for co in col]))
   source_definitions.append([j,q])
 assert len(sourcecols)==264
 selected=[];basis={}
 for column_index,rawcol in enumerate(sourcecols):
  w=rawcol[:];comb=[0]*24;comb[len(selected)]=1
  for pos in sorted(basis):
   bv,bc=basis[pos];co=w[pos]
   if co:
    w=[(w[i]-co*bv[i])%p for i in range(24)]
    comb=[(comb[i]-co*bc[i])%p for i in range(24)]
  pos=next((i for i,x in enumerate(w) if x),None)
  if pos is None:continue
  iv=pow(w[pos],-1,p);w=[iv*x%p for x in w];comb=[iv*x%p for x in comb]
  selected.append(column_index)
  for op,(bv,bc) in list(basis.items()):
   co=bv[pos]
   if co:basis[op]=([(bv[i]-co*w[i])%p for i in range(24)],
                    [(bc[i]-co*comb[i])%p for i in range(24)])
  basis[pos]=(w,comb)
  if len(selected)==24:break
 rank=len(selected);free=[i for i in range(24) if i not in basis]
 qdim=len(free);lengths.append(qdim)
 for pos,(v,co) in basis.items():
  assert all(v[j]==int(j==pos) for j in basis)
  actual=[sum(co[j]*sourcecols[selected[j]][i] for j in range(rank))%p for i in range(24)]
  assert actual==v
 def project(vector):
  w=vector[:];comb=[0]*rank
  for pos in sorted(basis):
   v,co=basis[pos];a=w[pos]
   if a:
    w=[(w[i]-a*v[i])%p for i in range(24)]
    comb=[(comb[j]+a*co[j])%p for j in range(rank)]
  assert all(w[i]==0 for i in basis)
  re=[w[i] for i in free]
  returned=[sum(comb[j]*sourcecols[selected[j]][i] for j in range(rank))%p for i in range(24)]
  for j,i in enumerate(free):returned[i]=(returned[i]+re[j])%p
  assert returned==[x%p for x in vector]
  return re,comb
 for col in sourcecols:assert not any(project(col)[0])
 unit,_=project(flatten(C(1)))
 assert qdim>0 and any(unit)
 # e^q times the twelve true lambda/Z monomials is a full basis of
 # this original 24-dimensional primary environment.
 ambient=[]
 for mon in env['monomials']:
  ambient.extend([mon,mon*evar])
 assert len(ambient)==24
 for j,mon in enumerate(ambient):
  assert flatten(mon)==[int(i==j) for i in range(24)]
 induced={};stability=[]
 for name,axis in axes.items():
  cols=[flatten(axis*mon) for mon in ambient]
  A=[[cols[j][i] for j in range(24)] for i in range(24)]
  # Ideal closure is checked on a full actual relation-space basis,
  # with exact membership witnesses back to the original 264 columns.
  witnesses=[]
  for ci in selected:
   rem,witness=project(matvec(A,sourcecols[ci]))
   assert not any(rem);witnesses.append(witness)
  actioncols=[project(cols[j])[0] for j in free]
  action=[[actioncols[j][i] for j in range(qdim)] for i in range(qdim)]
  assert matvec(action,unit)==project(flatten(axis))[0]
  induced[name]=action
  stability.append(dict(axis=name,
    allOriginalRelationImagesActuallyReturned=True,
    relationMembershipWitness=digest(witnesses),
    quotientMatrix=digest(action),
    characteristicCoefficientsAscending=charpoly(action)))
 for a in ['e','lambda','Z']:
  for b in ['e','lambda','Z']:
   assert matmul(induced[a],induced[b])==matmul(induced[b],induced[a])
 half=pow(2,-1,p)
 diagnostic_elements={
  'ell_minus_half':env['ell']-C(half),
  'lambda_minus_half':L-C(half),
  'T_plus_half':env['T']+C(half),
  'D':env['D'],'Kmoment':env['K']}
 diagnostics=[]
 for name,element in diagnostic_elements.items():
  first=None;last=None;value=C(1)
  for exponent in range(1,qdim+1):
   value=value*element
   remainder,witness=project(flatten(value));last=remainder
   if not any(remainder):
    first=exponent
    diagnostics.append(dict(name=name,
       firstZeroPower=exponent,fullPrimaryOriginalCombinationReturned=True,
       exactOriginal264ColumnWitness=digest(witness)))
    break
  if first is None:
   diagnostics.append(dict(name=name,firstZeroPower=None,
       lastTestedPower=qdim,lastExactRemainder=last,
       noNilpotenceClaim=True))
 say(stage='new_full_residual_original_quotient_and_geometry_return',
  index=index,weightPrimary=profile(h),ambientFpDimension=24,
  completeOriginal264ColumnRank=rank,
  actualFullPrimaryCokernelFpDimension=qdim,
  allSelectedOriginalColumnProductsAndAll264ProjectionsReturned=True,
  freeCoordinateIndices=free,quotientUnitCoordinates=unit,
  samePointOriginalGeometryActions=stability,
  allThreeCoordinateActionsCommuteAfterActualIdealClosure=True,
  fullPrimaryOriginalAnnihilatorDiagnostics=diagnostics,
  exactSourceColumnMatrixDefinition=digest(sourcecols),
  nilpotentWeightDirectionsNeverDiscarded=True,
  noQQDOrEllHalfIdentityInferred=True,wholeWExcluded=False)
say(stage='new_two_residual_complete_original_quotients_finished',
 sourceSHA256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
 exactTwoFullPrimaryFpDimensions=lengths,
 newGenericQQkI11DimensionUpperBound=sum(lengths),
 proofOfBound='previous seven unit blocks plus exact full residual lengths give the local A cokernel generator bound by Nakayama',
 oldSevenSuccessfulBlocksNotReplayed=True,
 noModD0OrModNilpotencePromotionToQQ=True,
 QQFamilyIdentificationAndQQDReturnStillRequired=True,
 noQQGenericEmptinessOrWholeWExclusionClaim=True,
 noCoefficientCacheOrEncodedSplitPayloadSaved=True,
 peakRssKiB=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss,
 ordinaryISPClaim=False)
signal.setitimer(signal.ITIMER_REAL,0);signal.alarm(0)
