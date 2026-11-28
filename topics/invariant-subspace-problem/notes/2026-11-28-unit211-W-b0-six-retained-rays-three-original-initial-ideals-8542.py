#!/usr/bin/env python3
"""NEW W/b0: original q2,R6,N5 initial ideals over all six retained rays.
A fixed p=1009 and the six already retained weight-valuation rays are input.
Regenerate ONLY the three pinned original polynomial coefficient definitions.
No old scalar, curve gcd, Newton face gcd, or failed gate is replayed.
For each ray, cover every rational lambda valuation by all exact lower-envelope
breakpoints and open intervals; lambda=0 is handled separately.
Use actual initial polynomials, fixed full Sylvester cofactors, and univariate
Bezout, including final three-initial-source return. No input head inverse.
Only a returned Laurent unit excludes a cell; every other cell is retained.
120 seconds /1 GiB, one dependency; no coefficient payload or cache.
"""
import ast,hashlib,json,math,resource,signal,time
from fractions import Fraction
from pathlib import Path
from flint import nmod_poly
START=time.perf_counter();DEADLINE=START+120
resource.setrlimit(resource.RLIMIT_AS,(1024**3,1024**3))
signal.setitimer(signal.ITIMER_REAL,120)
def tick():
 if time.perf_counter()>=DEADLINE:raise TimeoutError('absolute 120-second boundary')
def say(stage,**data):
 data.update(stage=stage,seconds=time.perf_counter()-START)
 print(json.dumps(data,sort_keys=True,separators=(',',':')),flush=True)
MOD=1009
RAYS=[(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0)]
name='2026-11-28-unit211-W-entire-b0-new-full-N5-two-low-original-scalars-8542.py'
full=Path(__file__).with_name(name).read_bytes()
assert hashlib.sha256(full).hexdigest()=='e356e79c8570b34ef3d041f828a3906006d82bc813b3719ef606e7ce068cbfe8'
marker=b'\nq2,R6,N5=basis\n'
assert full.count(marker)==1
prefix=full.split(marker)[0]+marker
assert len(prefix)==6749
assert hashlib.sha256(prefix).hexdigest()=='53a8d55ef6bcc8dd0eb233ef387420f5e2d40c04c0418ff493d82aa605b1eef9'
class DefinitionsOnly(ast.NodeTransformer):
 def visit_FunctionDef(self,node):
  if node.name in ('say','check_source'):return None
  node=self.generic_visit(node)
  if not node.body:node.body=[ast.Pass()]
  return node
 def visit_Assert(self,node):return None
 def visit_Expr(self,node):
  v=node.value
  if isinstance(v,ast.Call):
   if isinstance(v.func,ast.Name) and v.func.id in ('say','check_source','paid','ck'):return None
   if isinstance(v.func,ast.Attribute) and isinstance(v.func.value,ast.Name):
    if v.func.value.id in ('resource','signal') and v.func.attr in ('setrlimit','setitimer'):return None
  return self.generic_visit(node)
 def visit_Assign(self,node):
  if any(isinstance(t,ast.Name) and t.id=='START' for t in node.targets):return None
  return self.generic_visit(node)
 def visit_AugAssign(self,node):
  if isinstance(node.target,ast.Subscript) and isinstance(node.target.value,ast.Name) and node.target.value.id=='statistics':return None
  return self.generic_visit(node)
 def visit_If(self,node):
  node=self.generic_visit(node)
  if not node.body:node.body=[ast.Pass()]
  return node
 def visit_For(self,node):
  node=self.generic_visit(node)
  if not node.body:node.body=[ast.Pass()]
  return node
tree=DefinitionsOnly().visit(ast.parse(prefix.decode()))
ast.fix_missing_locations(tree)
ns={'__name__':'three_original_coefficient_definitions_only','__file__':str(Path(__file__).with_name(name))}
exec(compile(tree,name+'#input-definitions-only','exec'),ns)
tick()
originals=[ns[k].n for k in ('q2','R6','N5')]
expected=['88bf8a85f29cbe0aa6c11c63d322e08f95777247596dc82858df9047c4d54ed8',
 '92840a3ef63d3a606929f43dd88e7eb5d02a5f27407ac6fe3dfddaec531e4421',
 'd3f1f160783983353e5ba1029c55edd80c2430d9ffbb88e0b19019c6f05cb706']
assert [ns['profile'](p)['sha256'] for p in originals]==expected
data=[]
for p in originals:
 dd={tuple(map(int,ex)):Fraction(str(c)) for ex,c in p.to_dict().items()}
 assert all(c.denominator%MOD for c in dd.values())
 data.append(dd)
say('new_original_boundary_inputs_defined',
 fixedPrime=MOD,sixPreviouslyRetainedRays=RAYS,
 exactOriginalInputSHA256=expected,allRationalCoefficientsPIntegral=True,
 parameterPrefixBytes=len(prefix),parameterPrefixSHA256=hashlib.sha256(prefix).hexdigest(),
 noOldWeightScalarOrFaceGCDGateExecuted=True,
 lambdaZeroWillBeHandledSeparately=True)
def residue(c):
 return c.numerator%MOD*pow(c.denominator%MOD,-1,MOD)%MOD
def pp(values=()):return nmod_poly(list(values),MOD)
ZERO=pp();ONE=pp([1])
stats={'newBareissExactProducts':0,'newFullInitialCofactorReturns':0,
 'newEuclideanProducts':0,'newFinalThreeSourceReturns':0,
 'initialFacesWithUnitCoefficient':0,'retainedNonunitInitialFaces':0}
def degree(p):return int(p.degree()) if p else -1
def exact(a,b):
 tick();assert b
 q,r=divmod(a,b);assert not r and q*b==a
 stats['newBareissExactProducts']+=1
 return q
def profile(p):
 aa=[int(p[i]) for i in range(degree(p)+1)]
 raw=json.dumps(aa,separators=(',',':')).encode()
 return {'degree':degree(p),'terms':sum(bool(c) for c in aa),
         'bytes':len(raw),'sha256':hashlib.sha256(raw).hexdigest()}
def btrim(a):
 a=list(a)
 while a and not a[-1]:a.pop()
 return a
def badd(a,b):
 return btrim([(a[j] if j<len(a) else ZERO)+(b[j] if j<len(b) else ZERO)
               for j in range(max(len(a),len(b)))])
def bscale(a,c):return btrim([c*x for x in a])
def bmul(a,b):
 if not a or not b:return []
 out=[ZERO]*(len(a)+len(b)-1)
 for i,x in enumerate(a):
  for j,y in enumerate(b):out[i+j]=out[i+j]+x*y
 return btrim(out)
def bprofile(a):
 raw=json.dumps([[int(p[i]) for i in range(degree(p)+1)] for p in a],
                separators=(',',':')).encode()
 return {'lambdaDegree':len(a)-1,'rDegree':max(map(degree,a),default=-1),
         'bytes':len(raw),'sha256':hashlib.sha256(raw).hexdigest()}
def source_sum(tags,forms):
 out=[]
 for tag,form in zip(tags,forms):out=badd(out,bmul(tag,form))
 return out
def bezout(a,b):
 aa,bb=a,b;r0,r1=a,b;s0,s1=ONE,ZERO;t0,t1=ZERO,ONE
 while r1:
  tick();q,r=divmod(r0,r1);assert q*r1+r==r0
  stats['newEuclideanProducts']+=1
  r0,r1=r1,r;s0,s1=s1,s0-q*s1;t0,t1=t1,t0-q*t1
 if not r0:return ZERO,ZERO,ZERO
 inv=pow(int(r0[degree(r0)]),-1,MOD)
 g,s,t=inv*r0,inv*s0,inv*t0
 assert s*aa+t*bb==g
 return g,s,t
def fixed_cofactor(forms,i,j):
 F,G=forms[i],forms[j];m,n=len(F)-1,len(G)-1
 assert m>=1 and n>=1
 size=m+n;rows=[]
 for form,count in ((F,n),(G,m)):
  for shift in range(count):
   row=[ZERO]*size
   for k,c in enumerate(form):row[shift+k]=c
   rows.append(row)
 # Solve S^T mu=e0 by fraction-free elimination with an augmented RHS.
 a=[[rows[col][row] for col in range(size)]+[ONE if row==0 else ZERO]
    for row in range(size)]
 prev=ONE
 for k in range(size-1):
  tick();pivotrow=next((r for r in range(k,size) if a[r][k]),None)
  if pivotrow is None:return ZERO,[[],[],[]]
  if pivotrow!=k:a[k],a[pivotrow]=a[pivotrow],a[k]
  pivot=a[k][k]
  for r in range(k+1,size):
   ark=a[r][k]
   for c in range(k+1,size+1):
    a[r][c]=exact(pivot*a[r][c]-ark*a[k][c],prev)
   a[r][k]=ZERO
  prev=pivot
 determinant=a[-1][size-1]
 if not determinant:return ZERO,[[],[],[]]
 mu=[ZERO]*size
 for r in range(size-1,-1,-1):
  value=determinant*a[r][size]-sum((a[r][c]*mu[c] for c in range(r+1,size)),ZERO)
  mu[r]=exact(value,a[r][r])
 for col in range(size):
  assert sum((mu[row]*rows[row][col] for row in range(size)),ZERO)==(determinant if col==0 else ZERO)
 tags=[[],[],[]];tags[i]=btrim(mu[:n]);tags[j]=btrim(mu[n:])
 assert source_sum(tags,forms)==[determinant]
 stats['newFullInitialCofactorReturns']+=1
 return determinant,tags
def scalar_normalize(value):
 assert value
 shift=next(i for i in range(degree(value)+1) if value[i])
 leading=int(value[degree(value)])
 unit=pp([0]*shift+[leading])
 normalized=exact(value,unit)
 assert normalized*unit==value
 return normalized,unit
def torus_unit(forms):
 for i,F in enumerate(forms):
  if len(F)==1 and degree(F[0])==0:
   tags=[[],[],[]];tags[i]=[pp([pow(int(F[0][0]),-1,MOD)])]
   assert source_sum(tags,forms)==[ONE]
   stats['newFinalThreeSourceReturns']+=1
   return {'excluded':True,'reason':'actual initial monomial unit','sourceIndex':i}
 rawscalars=[];alltags=[]
 for i,F in enumerate(forms):
  if len(F)==1 and F[0]:
   tag=[[],[],[]];tag[i]=[ONE]
   rawscalars.append(F[0]);alltags.append(tag)
 pairs=[(0,1),(0,2),(1,2)]
 # Fixed order, without selecting a different polynomial after a failure.
 for i,j in pairs:
  if len(forms[i])>1 and len(forms[j])>1:
   value,tags=fixed_cofactor(forms,i,j)
   if value:rawscalars.append(value);alltags.append(tags)
 normalized=[];units=[];weights=[];g=ZERO
 for value in rawscalars:
  target,unit=scalar_normalize(value)
  newg,a,b=bezout(g,target)
  weights=[a*x for x in weights]+[b]
  normalized.append(target);units.append(unit);g=newg
  assert sum((x*y for x,y in zip(weights,normalized)),ZERO)==g
 # Return the actual THREE initial sources after clearing only r monomials.
 if normalized:
  common=ONE
  for unit in units:common=common*unit
  total=[[],[],[]]
  for weight,unit,tags in zip(weights,units,alltags):
   scale=weight*exact(common,unit)
   for i in range(3):total[i]=badd(total[i],bscale(tags[i],scale))
  assert source_sum(total,forms)==[common*g]
  stats['newFinalThreeSourceReturns']+=1
  tag_profiles=[bprofile(a) for a in total]
 else:
  common=ONE;tag_profiles=[]
 return {'excluded':bool(g) and degree(g)==0,
         'reason':'fixed initial cofactors and whole r Bezout',
         'nonzeroFixedScalarCount':len(rawscalars),
         'actualCommon':profile(g),'clearingRMonomial':profile(common),
         'completeThreeSourceReturn':bool(normalized),
         'returnedOriginalMultiplierProfiles':tag_profiles}
def lower_breakpoints(dd,w):
 heights={}
 for (a,b,j) in dd:
  v=w[0]*a+w[1]*b
  heights[j]=min(heights.get(j,v),v)
 out=set();indices=sorted(heights)
 for i,j in ((i,j) for i in indices for j in indices if i<j):
  z=Fraction(heights[i]-heights[j],j-i)
  vals={k:Fraction(h)+k*z for k,h in heights.items()}
  minimum=min(vals.values())
  if sum(v==minimum for v in vals.values())>=2:out.add(z)
 return out
def cells_for(w):
 breaks=sorted(set().union(*(lower_breakpoints(dd,w) for dd in data)))
 result=[]
 edges=[None]+breaks+[None]
 for a,b in zip(edges,edges[1:]):
  if a is None and b is None:z=Fraction(0)
  elif a is None:z=b-1
  elif b is None:z=a+1
  else:z=(a+b)/2
  result.append({'kind':'open interval','lo':str(a) if a is not None else None,
                 'hi':str(b) if b is not None else None,'representative':z})
 for z in breaks:result.append({'kind':'point','value':str(z),'representative':z})
 return result
def initial_form(dd,w,z,lambda_zero=False):
 if lambda_zero:dd={ex:c for ex,c in dd.items() if ex[2]==0}
 if not dd:return [],{'identicallyZeroAtLambdaZero':True}
 weights={ex:w[0]*ex[0]+w[1]*ex[1]+z*ex[2] for ex in dd}
 minimum=min(weights.values())
 face={ex:c for ex,c in dd.items() if weights[ex]==minimum}
 if not any(residue(c) for c in face.values()):
  stats['retainedNonunitInitialFaces']+=1
  return None,{'minimum':str(minimum),'hasPUnitOnMinimumFace':False}
 stats['initialFacesWithUnitCoefficient']+=1
 # Normalize e=1 if its weight is nonzero, otherwise k=1. The integral
 # rescaling of (w0,w1,z) gives a torus action over the algebraic closure.
 raxis=1 if w[0] else 0
 out={}
 for ex,c in face.items():
  v=residue(c)
  if v:
   key=(ex[raxis],ex[2]);out[key]=(out.get(key,0)+v)%MOD
 out={key:c for key,c in out.items() if c};assert out
 rshift=min(a for a,j in out);lshift=min(j for a,j in out)
 rows={}
 for (a,j),c in out.items():rows.setdefault(j-lshift,{})[a-rshift]=c
 result=[]
 for j in range(max(rows)+1):
  co=rows.get(j,{})
  result.append(pp([co.get(i,0) for i in range(max(co,default=-1)+1)]))
 result=btrim(result);assert result and result[0]
 return result,{'minimum':str(minimum),'hasPUnitOnMinimumFace':True,
                'normalizedCoordinate':'e' if w[0] else 'k',
                'remainingCoordinate':'k' if w[0] else 'e',
                'removedTorusMonomial':[rshift,lshift],
                'initialPolynomial':bprofile(result)}
results=[]
for w in RAYS:
 tick();cells=cells_for(w)
 say('new_original_initial_ray_partition',ray=w,
     lambdaValuationRatioCells=[{k:str(v) if k=='representative' else v for k,v in cell.items()} for cell in cells],
     allRationalRatiosCovered=True,lambdaZeroSeparate=True)
 cell_results=[]
 for number,cell in enumerate(cells):
  forms=[];profiles=[];valid=True
  for dd in data:
   form,meta=initial_form(dd,w,cell['representative'])
   forms.append(form);profiles.append(meta);valid=valid and form is not None
  answer=torus_unit(forms) if valid else {'excluded':False,'reason':'unpaid p-nonunit minimum face'}
  row={'ray':w,'cell':number,'partition':{k:str(v) if k=='representative' else v for k,v in cell.items()},
       'originalInitialProfiles':profiles,**answer}
  say('new_three_original_initial_cell_result',**row);cell_results.append(row)
 forms=[];profiles=[];valid=True
 for dd in data:
  form,meta=initial_form(dd,w,Fraction(0),True)
  forms.append(form);profiles.append(meta);valid=valid and form is not None
 answer=torus_unit(forms) if valid else {'excluded':False,'reason':'unpaid lambda-zero minimum face'}
 zero_row={'ray':w,'originalInitialProfiles':profiles,**answer}
 say('new_original_lambda_exactly_zero_boundary_result',**zero_row)
 closed=all(row['excluded'] for row in cell_results) and zero_row['excluded']
 item={'ray':w,'cellCount':len(cell_results),'excludedCellCount':sum(row['excluded'] for row in cell_results),
       'lambdaExactlyZeroExcluded':zero_row['excluded'],'wholeRetainedRayNowExcluded':closed}
 results.append(item);say('new_original_initial_entire_ray_result',**item)
say('new_three_original_initial_boundary_input_finished',
 fixedPrime=MOD,results=results,
 allSixPreviouslyRetainedRaysExcluded=all(item['wholeRetainedRayNowExcluded'] for item in results),
 noOriginalPointExistenceClaimFromRetainedCells=True,
 noPaidDenominatorIntegralityClaim=True,noFiniteDVRModelClaim=True,
 noWholeWOrB0ExclusionClaim=True,ordinaryISPClaim=False,
 noOldScalarCurveOrFaceGCDGateReplayed=True,noCoefficientPayloadSaved=True,
 statistics=stats,peakRSSKiB=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss,
 sourceSHA256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest())
signal.setitimer(signal.ITIMER_REAL,0)
