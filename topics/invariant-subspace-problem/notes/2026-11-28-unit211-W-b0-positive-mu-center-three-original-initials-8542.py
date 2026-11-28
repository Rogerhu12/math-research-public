#!/usr/bin/env python3
"""NEW W/b0: the strict positive-valuation mu=2*lambda-3 center.
Only the 6749-byte necessary q2/R6/N5 definition prefix is loaded.
No old C74/D78, old lambda-initial, or eleven-row cell solve is run.
Fixed p=1009; every eta=v(mu)/(-v(e))>0 is covered.  Complete
three-original Laurent sources return a unit or any pure-k center
polynomial found.  All unreturned cells/centers remain.  No D inverse.
180 seconds /4 GiB; one immutable small source dependency; no cache.
"""
import ast,hashlib,json,math,resource,signal,time
from pathlib import Path
from fractions import Fraction
from functools import reduce
from flint import fmpq_mpoly_ctx
START=time.perf_counter();DEADLINE=START+180
resource.setrlimit(resource.RLIMIT_AS,(4*1024**3,4*1024**3))
signal.setitimer(signal.ITIMER_REAL,180)
def tick():
 if time.perf_counter()>=DEADLINE:raise TimeoutError('absolute first 180-second budget')
def say(stage,**kw):
 kw.update(stage=stage,seconds=time.perf_counter()-START)
 print(json.dumps(kw,sort_keys=True,separators=(',',':')),flush=True)
DEP='2026-11-28-unit211-W-entire-b0-new-full-N5-two-low-original-scalars-8542.py'
EXPECTED='e356e79c8570b34ef3d041f828a3906006d82bc813b3719ef606e7ce068cbfe8'
PREFIX_EXPECTED='53a8d55ef6bcc8dd0eb233ef387420f5e2d40c04c0418ff493d82aa605b1eef9'
src=Path(__file__).with_name(DEP).read_text()
assert hashlib.sha256(src.encode()).hexdigest()==EXPECTED
pref=src[:6749]
assert len(pref.encode())==6749 and hashlib.sha256(pref.encode()).hexdigest()==PREFIX_EXPECTED
tree=ast.parse(pref);body=[]
for nd in tree.body:
 if isinstance(nd,ast.Assert):continue
 if isinstance(nd,ast.FunctionDef) and nd.name=='say':continue
 if isinstance(nd,ast.Assign) and any(isinstance(t,ast.Name) and t.id=='START' for t in nd.targets):continue
 if isinstance(nd,ast.For) and isinstance(nd.target,ast.Name) and nd.target.id=='v':continue
 if isinstance(nd,ast.Expr) and isinstance(nd.value,ast.Call):
  fn=nd.value.func
  if isinstance(fn,ast.Name) and fn.id=='say':continue
  if isinstance(fn,ast.Attribute) and isinstance(fn.value,ast.Name) and fn.value.id in ('resource','signal'):continue
 body.append(nd)
tree.body=body
ns={'__name__':'new_mu_center_necessary_definitions','say':lambda *a,**k:None}
exec(compile(tree,DEP+'::necessary-6749','exec'),ns)
assert len(ns['rawbasis'])==len(ns['basis'])==len(ns['basescales'])==3
P=1009
ctx=fmpq_mpoly_ctx.get(('e','k','mu'),'lex')
ee,kk,mm=ctx.gens();O=ctx.constant(1);Z=ctx.constant(0)
# Explicit context transport.  No old-context object is passed as a new R.
lam_mu=(mm+3)/2
def transport(poly):
 out=Z
 for ex,co in poly.to_dict().items():
  i,j,l=map(int,ex)
  out+=ctx.constant(co)*(ee**i)*(kk**j)*(lam_mu**l)
 return out
def transport_weight(poly):
 assert all(int(ex[2])==0 for ex in poly.to_dict())
 return ctx.from_dict({tuple(map(int,ex)):co for ex,co in poly.to_dict().items()})
def profile(poly):
 data=[[list(map(int,ex)),str(co)] for ex,co in sorted(poly.to_dict().items())]
 raw=json.dumps(data,separators=(',',':')).encode()
 return {'degrees_e_k_mu':list(map(int,poly.degrees())) if poly else [-1]*3,
         'totalDegree':int(poly.total_degree()) if poly else -1,'terms':len(data),
         'bytes':len(raw),'sha256':hashlib.sha256(raw).hexdigest()}
names=['same_original_q2','same_original_R6','same_complete_NV_N5']
stats={'newCenteredOriginalReturns':0,'integerPrimitiveReturns':0,
 'originalInitialNormalizations':0,'LaurentSourceReturns':0,
 'composedThreeOriginalReturns':0,'newSPairs':0,'newBasisElements':0,
 'LaurentProducts':0,'excludedCells':0,'pureKCenterReturns':0,
 'minimumFacesWithoutPUnit':0}
data=[];profiles=[]
for index,(normal,scale,raw) in enumerate(zip(ns['basis'],ns['basescales'],ns['rawbasis'])):
 tick();assert normal.d==ns['O']
 poly=transport(normal.n)
 rn=transport(raw.n);rd=transport_weight(raw.d)
 sn=transport_weight(scale.n);sd=transport_weight(scale.d)
 assert poly*sd*rd==sn*rn
 stats['newCenteredOriginalReturns']+=1
 if not poly:
  data.append({});profiles.append(profile(Z));continue
 qq={tuple(map(int,ex)):Fraction(str(co)) for ex,co in poly.to_dict().items()}
 den=1
 for co in qq.values():den=math.lcm(den,co.denominator)
 ints={ex:co.numerator*(den//co.denominator) for ex,co in qq.items()}
 content=reduce(math.gcd,(abs(co) for co in ints.values()))
 assert content
 pp=ctx.from_dict({ex:co//content for ex,co in ints.items()})
 assert pp*content==poly*den
 assert pp*(sd*rd*content)==sn*rn*den
 assert all(Fraction(str(co)).denominator==1 for co in pp.to_dict().values())
 stats['integerPrimitiveReturns']+=1
 data.append({tuple(map(int,ex)):int(Fraction(str(co))) for ex,co in pp.to_dict().items()})
 profiles.append(profile(pp))
say('new_mu_center_three_original_polynomials',
 originalNames=names,originalProfiles=profiles,prime=P,
 originalLambdaDefinition='lambda=(mu+3)/2',muNonzeroByWholeWLambdaThreeHalvesExclusion=True,
 muValuationStrictlyPositiveByRun46162974839=True,
 originalDefinitionSourceBlob='47281af16fdd0ad7500ecda377c3cb9f9d65e725',
 dependencySHA256=EXPECTED,necessaryPrefixBytes=6749,necessaryPrefixSHA256=PREFIX_EXPECTED,
 allThreeOriginalContextTransportsAndScalesReturned=True,
 noPhysicalFZeroSpecialization=True,noNewWeightInverse=True,noDInverse=True,
 noOldC74D78OrLambdaOrElevenRowAlgorithmRun=True)

# Exact sparse Fp Laurent source arithmetic in (k_lead,mu_lead).
ONE={(0,0):1}
def clean(poly):return {ex:co%P for ex,co in poly.items() if co%P}
def add(a,b):
 out=dict(a)
 for ex,co in b.items():out[ex]=(out.get(ex,0)+co)%P
 return clean(out)
def sub(a,b):return add(a,{ex:-co%P for ex,co in b.items()})
def shift(a,ex,co=1):
 return {tuple(x+y for x,y in zip(m,ex)):v*co%P for m,v in a.items() if v*co%P}
def mul(a,b):
 tick();out={}
 for x,c in a.items():
  for y,d in b.items():
   m=tuple(i+j for i,j in zip(x,y));out[m]=(out.get(m,0)+c*d)%P
 stats['LaurentProducts']+=1
 return clean(out)
def order(ex):return (ex[1],ex[0]) # lex elimination of mu, with k retained
def lead(poly):return max(poly,key=order)
def lp_profile(poly):
 raw=json.dumps([[list(ex),co] for ex,co in sorted(poly.items())],separators=(',',':')).encode()
 return {'terms':len(poly),'minExponents':[min((e[i] for e in poly),default=0) for i in range(2)],
 'maxExponents':[max((e[i] for e in poly),default=0) for i in range(2)],
 'bytes':len(raw),'sha256':hashlib.sha256(raw).hexdigest()}
def tag_return(poly,tags,forms):
 assert len(tags)==len(forms)==3
 answer={}
 for x,y in zip(tags,forms):answer=add(answer,mul(x,y))
 assert answer==poly
 stats['LaurentSourceReturns']+=1
def normalized(poly,tags):
 if not poly:return {},tags
 low=tuple(min(ex[i] for ex in poly) for i in range(2))
 exp=tuple(-x for x in low);unit=pow(poly[lead(poly)],-1,P)
 return shift(poly,exp,unit),[shift(t,exp,unit) for t in tags]
def reduce_row(poly,tags,basis):
 while poly:
  tick();work=dict(poly);rem={}
  while work:
   exp=lead(work);co=work[exp];used=False
   for row,rtag in basis:
    lm=lead(row)
    if all(a>=b for a,b in zip(exp,lm)):
     dif=tuple(a-b for a,b in zip(exp,lm));sc=co*pow(row[lm],-1,P)%P
     work=sub(work,shift(row,dif,sc))
     tags=[sub(x,shift(y,dif,sc)) for x,y in zip(tags,rtag)]
     used=True;break
   if not used:rem[exp]=co;del work[exp]
  if not rem:return {},tags
  low=tuple(min(ex[i] for ex in rem) for i in range(2))
  poly,tags=normalized(rem,tags)
  if not any(low):return poly,tags
 return {},tags
def original_return(poly,tags,forms,raw_forms,normalizers):
 tag_return(poly,tags,forms)
 actual=[mul(x,y) for x,y in zip(tags,normalizers)]
 tag_return(poly,actual,raw_forms)
 stats['composedThreeOriginalReturns']+=1
 return [lp_profile(x) for x in actual]
def solve(forms,raw_forms,normalizers):
 basis=[];pairs=[];unit_tags=None
 def append(poly,tags):
  nonlocal unit_tags
  poly,tags=normalized(poly,tags);poly,tags=reduce_row(poly,tags,basis)
  tag_return(poly,tags,forms)
  if not poly:return
  if poly==ONE:
   unit_tags=tags;return
  ix=len(basis);lm=lead(poly)
  for j,(rp,rt) in enumerate(basis):
   rm=lead(rp)
   if all(min(a,b)==0 for a,b in zip(lm,rm)):continue
   common=tuple(max(a,b) for a,b in zip(lm,rm))
   pairs.append((sum(common),j,ix))
  basis.append((poly,tags));stats['newBasisElements']+=1
 for i in range(3):
  append(forms[i],[dict(ONE) if j==i else {} for j in range(3)])
  if unit_tags is not None:break
 while pairs and unit_tags is None:
  tick();pairs.sort();_,i,j=pairs.pop(0)
  ap,at=basis[i];bp,bt=basis[j]
  am,bm=lead(ap),lead(bp);cm=tuple(max(a,b) for a,b in zip(am,bm))
  da=tuple(a-b for a,b in zip(cm,am));db=tuple(a-b for a,b in zip(cm,bm))
  ca=pow(ap[am],-1,P);cb=pow(bp[bm],-1,P)
  sp=sub(shift(ap,da,ca),shift(bp,db,cb))
  tags=[sub(shift(x,da,ca),shift(y,db,cb)) for x,y in zip(at,bt)]
  stats['newSPairs']+=1;append(sp,tags)
 if unit_tags is not None:
  stats['excludedCells']+=1
  return {'excluded':True,'completeThreeOriginalUnitReturn':True,
          'originalUnitMultiplierProfiles':original_return(ONE,unit_tags,forms,raw_forms,normalizers),
          'newBasisCount':len(basis)}
 centers=[]
 # Every returned polynomial is an actual new three-source necessary
 # center, not the assertion that these alone define the remaining ideal.
 for row,tags in basis:
  if row and all(ex[1]==0 for ex in row):
   centers.append({'centerProfile':lp_profile(row),
     'originalMultiplierProfiles':original_return(row,tags,forms,raw_forms,normalizers)})
   stats['pureKCenterReturns']+=1
 return {'excluded':False,'completeThreeOriginalUnitReturn':False,
   'newBasisCount':len(basis),'newBasisProfiles':[lp_profile(x) for x,t in basis],
   'completeThreeOriginalPureKCenters':centers,
   'noResiduePointExistenceClaim':True,'noCompleteIdealClaimFromCenterList':True}
def breakpoints(dd):
 heights={}
 for (i,j,r) in dd:heights[r]=min(heights.get(r,-i),-i)
 out=set();powers=sorted(heights)
 for i in powers:
  for j in powers:
   if i>=j:continue
   x=Fraction(heights[i]-heights[j],j-i)
   if x<=0:continue
   vals=[Fraction(h)+r*x for r,h in heights.items()]
   if vals.count(min(vals))>=2:out.add(x)
 return out
cuts=sorted(set().union(*(breakpoints(dd) for dd in data)))
cells=[];edges=[Fraction(0)]+cuts+[None]
for lo,hi in zip(edges,edges[1:]):
 point=lo+1 if hi is None else (lo+hi)/2
 cells.append({'kind':'open interval','lo':str(lo),'hi':None if hi is None else str(hi),'sample':point})
for x in cuts:cells.append({'kind':'point','value':str(x),'sample':x})
def desc(cell):return {k:str(v) if k=='sample' else v for k,v in cell.items()}
def initial(dd,eta):
 if not dd:return {},{'identicallyZeroInput':True},{},dict(ONE)
 minimum=min(-ex[0]+eta*ex[2] for ex in dd)
 out={}
 for ex,co in dd.items():
  if -ex[0]+eta*ex[2]==minimum:
   key=(ex[1],ex[2]);out[key]=(out.get(key,0)+co)%P
 raw=clean(out)
 if not raw:
  stats['minimumFacesWithoutPUnit']+=1
  return None,{'minimumGeometricWeight':str(minimum),'hasPUnitCoefficient':False},None,None
 low=tuple(min(ex[i] for ex in raw) for i in range(2))
 co=raw[lead(raw)];norm=shift(ONE,tuple(-x for x in low),pow(co,-1,P))
 out=mul(norm,raw);assert out==normalized(raw,[])[0]
 stats['originalInitialNormalizations']+=1
 return out,{'minimumGeometricWeight':str(minimum),'hasPUnitCoefficient':True,
   'removedTorusMonomial':list(low),'removedNonzeroScalar':co,
   'normalizedProfile':lp_profile(out),'unscaledProfile':lp_profile(raw)},raw,norm
say('new_positive_mu_center_partition',ray=[-1,0],etaStrictlyPositive=True,
 cuts=[str(x) for x in cuts],cells=[desc(c) for c in cells],
 allPositiveRationalEtaCovered=True,exactMuZeroAlreadyExcluded=True,
 noTVariableOrTValuationAssumed=True)
results=[]
for index,cell in enumerate(cells):
 tick();forms=[];meta=[];raw_forms=[];normalizers=[]
 for dd in data:
  f,md,raw,norm=initial(dd,cell['sample'])
  forms.append(f);meta.append(md);raw_forms.append(raw);normalizers.append(norm)
 if any(x is None for x in forms):
  answer={'excluded':False,'reason':'entire minimum face p-nonunit; whole cell retained'}
 else:answer=solve(forms,raw_forms,normalizers)
 row={'cell':index,'partition':desc(cell),'originalFaceMetadata':meta,**answer}
 say('new_mu_center_three_original_cell_return',**row);results.append(row)
say('new_mu_center_three_original_boundary_finished',
 ray=[-1,0],etaStrictlyPositive=True,cellCount=len(results),
 excludedCellCount=sum(x['excluded'] for x in results),
 wholeRemainingRayExcluded=all(x['excluded'] for x in results),
 allUnreturnedCellsAndKCentersRetained=True,noKPlusTwoAssumption=True,
 noCharacteristicZeroLiftOfResidueIdeal=True,noFiniteDVRModelClaim=True,
 noWholeWOrOrdinaryISPClaim=True,physicalDNotInverted=True,
 noOldProjectionOrLambdaOrElevenRowGateRun=True,noCoefficientPayloadSaved=True,
 statistics=stats,peakRSSKiB=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss,
 sourceSHA256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest())
signal.setitimer(signal.ITIMER_REAL,0)
