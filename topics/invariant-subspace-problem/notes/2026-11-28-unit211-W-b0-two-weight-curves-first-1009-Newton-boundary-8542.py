#!/usr/bin/env python3
"""NEW W/b0: p=1009 Newton boundary of the two existing weight curves.
Regenerate C74,D78 ONLY as pinned coefficient parameters: strip old
proof/output nodes from the fixed definition prefix before compiling.
No old scalar source return, QQ common-factor gate, resultant or fiber
test is replayed. New target: every common Newton edge initial gcd,
with a complete ordinary F_p Bezout return. No weight-empty claim.
120 seconds / 1 GiB, one fixed prime; retain every unpaid boundary.
"""
import ast,hashlib,json,math,resource,signal,time
from fractions import Fraction
from pathlib import Path
START=time.perf_counter();DEADLINE=START+120
resource.setrlimit(resource.RLIMIT_AS,(1024**3,1024**3))
signal.setitimer(signal.ITIMER_REAL,120)
def tick():
 if time.perf_counter()>=DEADLINE:raise TimeoutError('absolute 120 second boundary')
def say(stage,**kw):
 kw.update(stage=stage,seconds=time.perf_counter()-START)
 print(json.dumps(kw,sort_keys=True,separators=(',',':')),flush=True)
name='2026-11-28-unit211-W-entire-b0-new-full-N5-two-low-original-scalars-8542.py'
full=Path(__file__).with_name(name).read_bytes()
assert hashlib.sha256(full).hexdigest()=='e356e79c8570b34ef3d041f828a3906006d82bc813b3719ef606e7ce068cbfe8'
marker=b'\ng=Z\nfor p in retained:'
assert full.count(marker)==1
prefix=full.split(marker)[0]+b'\n'
assert len(prefix)==9855
assert hashlib.sha256(prefix).hexdigest()=='b4211e655c4cc8bba963db0858334a21243285575472fc92ca1cf9aa46d0111d'
# Deterministic parameter-only transform. Existing complete proof gates
# are removed, not executed and re-labelled as new results.
class ParametersOnly(ast.NodeTransformer):
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
tree=ParametersOnly().visit(ast.parse(prefix.decode()))
ast.fix_missing_locations(tree)
ns={'__name__':'existing_weight_coefficient_definitions_only','__file__':str(Path(__file__).with_name(name))}
exec(compile(tree,name+'#necessary_coefficients_only','exec'),ns)
tick()
curves=ns['retained']
expected=['61f94d2de21fb53f992abded0c670a8f7e529319f38396ac904e77824d80b8b9',
          '59387d311d686962932c2d15325bf139b47d9ad6a19fa566c24cdab1f8e7bd2c']
assert len(curves)==2
assert [ns['profile'](p)['sha256'] for p in curves]==expected
say('existing_C74_D78_parameters_defined',
 exactSHA256=expected,onlyNecessaryCoefficientDefinitionsRegenerated=True,
 oldCompleteScalarReturnsRemoved=True,oldQQWeightGCDNotExecuted=True,
 originalDefinitionPrefixBytes=len(prefix),
 originalDefinitionPrefixSHA256=hashlib.sha256(prefix).hexdigest())
MOD=1009
def rational(c):return Fraction(str(c))
data=[]
for p in curves:
 dd={}
 for ex,c in p.to_dict().items():
  assert int(ex[2])==0
  dd[(int(ex[0]),int(ex[1]))]=rational(c)
 data.append(dd)
assert all(c.denominator%MOD for dd in data for c in dd.values())
def residue(c):return c.numerator%MOD*pow(c.denominator%MOD,MOD-2,MOD)%MOD
def cross(o,a,b):return (a[0]-o[0])*(b[1]-o[1])-(a[1]-o[1])*(b[0]-o[0])
def hull(points):
 pts=sorted(set(points));lo=[];hi=[]
 for p in pts:
  while len(lo)>=2 and cross(lo[-2],lo[-1],p)<=0:lo.pop()
  lo.append(p)
 for p in reversed(pts):
  while len(hi)>=2 and cross(hi[-2],hi[-1],p)<=0:hi.pop()
  hi.append(p)
 out=lo[:-1]+hi[:-1]
 assert len(out)>=3
 assert all(cross(out[j-1],out[j],out[(j+1)%len(out)])>0 for j in range(len(out)))
 return out
polygons=[hull(dd) for dd in data]
def edges(vertices):
 ans={}
 for a,b in zip(vertices,vertices[1:]+vertices[:1]):
  dx=b[0]-a[0];dy=b[1]-a[1];gg=math.gcd(abs(dx),abs(dy))
  v=(-dy//gg,dx//gg)
  ans[v]={'endpoints':[a,b],'latticeLength':gg}
 return ans
edge_sets=[edges(h) for h in polygons]
vertex_units=all(residue(dd[p]) for dd,hh in zip(data,polygons) for p in hh)
say('new_fixed_prime_Newton_polygons_and_integral_vertices',
 prime=MOD,polygons=polygons,
 allRationalCoefficientsPIntegral=True,allVerticesPUnits=vertex_units,
 commonPrimitiveInwardNormals=sorted(set(edge_sets[0])&set(edge_sets[1])),
 noFullWeightAlgebraOrOriginalFiberConclusion=True)
def trim(a):
 a=[int(c)%MOD for c in a]
 while a and not a[-1]:a.pop()
 return a
def add(a,b):
 return trim([(a[j] if j<len(a) else 0)+(b[j] if j<len(b) else 0) for j in range(max(len(a),len(b)))])
def neg(a):return trim([-x for x in a])
def sub(a,b):return add(a,neg(b))
def mul(a,b):
 if not a or not b:return []
 c=[0]*(len(a)+len(b)-1)
 for i,x in enumerate(a):
  for j,y in enumerate(b):c[i+j]=(c[i+j]+x*y)%MOD
 return trim(c)
def scale(a,c):return trim([x*c for x in a])
stats={'exactDivisionProducts':0,'completeFaceBezoutReturns':0}
def divide(a,b):
 tick();a=trim(a);b=trim(b);assert b
 original=a[:];q=[0]*max(0,(len(a)-len(b)+1));iv=pow(b[-1],MOD-2,MOD)
 assert b[-1]*iv%MOD==1
 while len(a)>=len(b) and a:
  d=len(a)-len(b);c=a[-1]*iv%MOD;q[d]=c
  for j,y in enumerate(b):a[d+j]=(a[d+j]-c*y)%MOD
  a=trim(a)
 q=trim(q)
 assert add(mul(q,b),a)==original
 stats['exactDivisionProducts']+=1
 return q,a
def bezout(a,b):
 r0,r1=a[:],b[:];s0,s1=[1],[];t0,t1=[],[1]
 while r1:
  q,rr=divide(r0,r1)
  r0,r1=r1,rr;s0,s1=s1,sub(s0,mul(q,s1));t0,t1=t1,sub(t0,mul(q,t1))
 assert r0
 iv=pow(r0[-1],MOD-2,MOD)
 g=scale(r0,iv);ss=scale(s0,iv);tt=scale(t0,iv)
 assert add(mul(ss,a),mul(tt,b))==g
 assert not divide(a,g)[1] and not divide(b,g)[1]
 stats['completeFaceBezoutReturns']+=1
 return g,ss,tt
def profile(a):
 raw=json.dumps(a,separators=(',',':')).encode()
 return {'degree':len(a)-1,'bytes':len(raw),'sha256':hashlib.sha256(raw).hexdigest()}
def face(dd,v):
 val=min(v[0]*i+v[1]*j for i,j in dd)
 pts=[p for p in dd if v[0]*p[0]+v[1]*p[1]==val]
 d=(v[1],-v[0]);anchor=pts[0];indices=[]
 for p in pts:
  if d[0]:
   assert (p[0]-anchor[0])%d[0]==0
   k=(p[0]-anchor[0])//d[0]
  else:
   assert (p[1]-anchor[1])%d[1]==0
   k=(p[1]-anchor[1])//d[1]
  assert (anchor[0]+k*d[0],anchor[1]+k*d[1])==p
  indices.append((k,residue(dd[p])))
 minimum=min(k for k,c in indices);maximum=max(k for k,c in indices)
 out=[0]*(maximum-minimum+1)
 for k,c in indices:out[k-minimum]=c
 assert out[0] and out[-1]
 return out,val
results=[]
if vertex_units:
 for v in sorted(set(edge_sets[0])&set(edge_sets[1])):
  aa,va=face(data[0],v);bb,vb=face(data[1],v)
  g,sa,sb=bezout(aa,bb)
  row={'primitiveInwardNormal':v,'minimalWeights':[va,vb],
       'facePolynomials':[profile(aa),profile(bb)],
       'actualCommon':profile(g),'ordinaryBezoutReturned':True,
       'noCommonNonzeroFaceRoot':len(g)==1,
       'remainingBoundaryRetained':len(g)>1}
  say('new_common_Newton_boundary_original_face_result',**row)
  results.append(row)
else:
 say('new_Newton_boundary_test_stops_at_unpaid_vertex',
     fixedPrimeNotChanged=True,noIntegralityClaim=True)
all_boundary=vertex_units and all(r['noCommonNonzeroFaceRoot'] for r in results)
say('new_fixed_prime_Newton_boundary_input_finished',
 prime=MOD,results=results,
 allNonzeroValuationDirectionsExcluded=all_boundary,
 eAndKUnitsAtEvery1009PlaceOfFiniteWeightPoints=all_boundary,
 oldOtherPaidDenominatorsNotYetProvedIntegralUnits=True,
 noWholeWOrB0OriginalUnitClaim=True,
 noNewFiniteOriginalIntegralModelClaim=True,
 statistics=stats,peakRSSKiB=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss,
 sourceSHA256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
 noOldScalarOrGCDProofGateReplayed=True,noCoefficientPayloadSaved=True,
 ordinaryISPClaim=False)
signal.setitimer(signal.ITIMER_REAL,0)
