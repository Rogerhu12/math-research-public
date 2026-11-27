#!/usr/bin/env python3
"""New original u=Q five-column Cramer graph; all leading-zero fibers retained.
Input is the eight already verified original three-overlap/product rows.
This is not the frozen expanded-monic-trace probe.
"""
import json,time,hashlib,signal,resource,sys,math
from fractions import Fraction
from pathlib import Path
from flint import fmpq_poly,fmpq,nmod_poly
signal.alarm(60)
resource.setrlimit(resource.RLIMIT_AS,(4*1024**3,4*1024**3))
start=time.perf_counter()
here=Path(__file__).resolve().parent
input_path=Path(sys.argv[1]) if len(sys.argv)>1 else here/'uq8542_finite_module_input.json'
out_path=Path(sys.argv[2]) if len(sys.argv)>2 else here/'uq8542_F95_Gauss_original_module.json'
raw_bytes=input_path.read_bytes();data=json.loads(raw_bytes)
P=lambda a=():fmpq_poly([fmpq(x) for x in a])
zero=P();one=P([1]);w=P([0,1])
def say(**r):
 r['seconds']=time.perf_counter()-start
 print(json.dumps(r),flush=True)
def exact(a,b):
 q,r=divmod(a,b)
 assert not r and q*b==a
 return q
def monic(p):return p/p[p.degree()] if p else p
def det(a):
 n=len(a)
 if n==0:return one
 a=[r[:] for r in a];prev=one;sgn=1
 for k in range(n-1):
  if not a[k][k]:
   sw=next((i for i in range(k+1,n) if a[i][k]),None)
   if sw is None:return zero
   a[k],a[sw]=a[sw],a[k];sgn=-sgn
  pp=a[k][k]
  for i in range(k+1,n):
   for j in range(k+1,n):a[i][j]=exact(a[i][j]*pp-a[i][k]*a[k][j],prev)
   a[i][k]=zero
  prev=pp
 return sgn*a[-1][-1]
atoms=[P(r['poly']) for r in data['atoms']]+[P(data['F9'])]
def strip(p):
 original=p;paid=one;hist=[]
 for i,a in enumerate(atoms):
  ct=0
  while p:
   g=p.gcd(a)
   if g.degree()<=0:break
   p=exact(p,g);paid*=g;ct+=1
  if ct:hist.append([i,ct])
 assert p*paid==original
 return p,paid,hist
def coeffs(p):return [str(c) for c in p.coeffs()]
def profile(name,p):
 if not p:return dict(name=name,zero=True)
 cc,fs=p.factor();back=P([cc]);fac=[]
 for q,m in fs:
  back*=q**m
  rec=dict(degree=q.degree(),multiplicity=int(m),sha256=hashlib.sha256(json.dumps(coeffs(q)).encode()).hexdigest())
  if q.degree()<=40:rec['coefficients']=coeffs(q)
  fac.append(rec)
 assert back==p
 return dict(name=name,degree=p.degree(),content=str(cc),factors=fac,allFactorsMultipliedBack=True,sha256=hashlib.sha256(json.dumps(coeffs(p)).encode()).hexdigest())
rows=[[P(c) for c in r['row']] for r in data['matrix']]
order=[1,2,3,4,5,0];orig=[[r[j] for j in order] for r in rows]
aa=[r[:] for r in orig];sel=list(range(len(aa)));prev=one;pos=0
for col in range(5):
 opts=[i for i in range(pos,len(aa)) if aa[i][col]]
 assert opts
 sw=min(opts,key=lambda i:aa[i][col].degree())
 aa[pos],aa[sw]=aa[sw],aa[pos];sel[pos],sel[sw]=sel[sw],sel[pos]
 pivot=aa[pos][col]
 for i in range(pos+1,len(aa)):
  for j in range(col+1,6):aa[i][j]=exact(aa[i][j]*pivot-aa[i][col]*aa[pos][j],prev)
  aa[i][col]=zero
 prev=pivot;pos+=1
assert pos==5 and all(not v for r in aa[5:] for v in r)
indices=sel[:5];mat=[orig[i][:5] for i in indices];rhs=[-orig[i][5] for i in indices]
delta=det(mat);assert delta
numer=[]
for j in range(5):
 mm=[r[:] for r in mat]
 for i in range(5):mm[i][j]=rhs[i]
 numer.append(det(mm))
for r in orig:assert sum((r[j]*numer[j] for j in range(5)),zero)+delta*r[5]==0
lead,paid,lead_history=strip(delta)
say(stage='new_original_five_column_Cramer_graph',selectedRows=indices,leadingDegree=delta.degree(),unpaidLeadingDegree=lead.degree(),allEightOriginalRowsMultipliedBack=True,leadingZeroFiberRetained=True,claimExcluded=False)

F3=monic(P([-10,30,-25,4]));F95=monic(exact(lead,F3));assert F95.degree()==95
fractions=[Fraction(str(c)) for c in F95.coeffs()];dd=1
for c in fractions:dd=math.lcm(dd,c.denominator)
ints=[c.numerator*(dd//c.denominator) for c in fractions];ct=0
for c in ints:ct=math.gcd(ct,c)
if ints[-1]<0:ct=-ct
ints=[c//ct for c in ints]
primitive95=P(ints);assert monic(primitive95)==F95 and math.gcd(*ints)==1
prime=1009
assert ints[-1]%prime
MP=lambda a=():nmod_poly([int(x)%prime for x in a],prime)
FF=MP(ints);assert FF.degree()==95
def mcoeff(p):return [int(c) for c in p.coeffs()]
def meq(a,b):return a==b
# Every original coefficient denominator and every paid physical atom is checked
# against the entire degree-95 polynomial before any component split.
denominators={}
for rec in data['original']:
 for mon,c in rec['poly']:denominators[tuple(c['d'])]=c['d']
for mat in data['multiplicationMatrices']:
 for row in mat:
  for c in row:denominators[tuple(c['d'])]=c['d']
for at in data['atoms']:denominators[tuple(at['poly'])]=at['poly']
denominators[tuple(data['F9'])]=data['F9']
for coeff in denominators.values():
 pp=MP(coeff);gg,ss,tt=pp.xgcd(FF)
 assert ss*pp+tt*FF==gg and gg.degree()==0
 scale=pow(int(gg[0]),-1,prime);ss*=scale;tt*=scale
 assert ss*pp+tt*FF==MP([1])
say(stage='F95_original_univariate_good_reduction_and_all_denominators',prime=prime,QQDegree=95,modularDegree=FF.degree(),primitiveQQLeadingModPrime=int(ints[-1]%prime),distinctOriginalDenominatorsAndPaidAtoms=len(denominators),allWholeF95BezoutTwoProductsOne=True,noMultivariateModularEmptinessClaim=True)
unit,factors=FF.factor();back=MP([unit])
for f,m in factors:back*=f**m
assert back==FF and sum(f.degree()*m for f,m in factors)==95

def component(f,multiplicity):
 def rem(p):
  q,r=divmod(p,f);assert q*f+r==p
  return r
 class K:
  def __init__(self,v=0):
   if isinstance(v,K):self.q=v.q;return
   if not isinstance(v,nmod_poly):v=MP([v])
   self.q=rem(v)
  def __bool__(self):return bool(self.q)
  def __add__(self,v):return K(self.q+K(v).q)
  __radd__=__add__
  def __neg__(self):return K(-self.q)
  def __sub__(self,v):return self+-K(v)
  def __rsub__(self,v):return K(v)+-self
  def __mul__(self,v):return K(self.q*K(v).q)
  __rmul__=__mul__
  def __eq__(self,v):return self.q==K(v).q
  def inv(self):
   gg,ss,tt=self.q.xgcd(f);assert ss*self.q+tt*f==gg and gg.degree()==0
   iv=K(ss*pow(int(gg[0]),-1,prime));assert self*iv==1
   return iv
 def scalar(c):
  dn=K(MP(c['d']));iv=dn.inv();assert dn*iv==1
  return K(MP(c['n']))*iv
 I6=[[K(int(i==j)) for j in range(6)] for i in range(6)];e0=I6[0]
 mats=[[[scalar(c) for c in row] for row in mat] for mat in data['multiplicationMatrices']]
 def add(a,b):return [v+b[j] for j,v in enumerate(a)]
 def scale(a,c):return [v*c for v in a]
 def sub(a,b):return [v-b[j] for j,v in enumerate(a)]
 def rp(a,B):return [sum((a[k]*B[k][j] for k in range(6)),K()) for j in range(6)]
 def mm(A,B):return [rp(row,B) for row in A]
 powers=[[I6,mat] for mat in mats]
 for j in range(3):
  for n in range(2,4):powers[j].append(mm(powers[j][-1],mats[j]))
 assert mats[0][0]==I6[1] and mats[1][0]==I6[2] and mats[2][0]==I6[3]
 assert rp(rp(e0,mats[1]),mats[1])==I6[4] and rp(rp(e0,mats[1]),mats[2])==I6[5]
 def evalrow(ts):
  out=[K() for _ in range(6)]
  for mon,c in ts:
   deg=list(map(int,mon.split(',')));row=e0[:]
   for j,n in enumerate(deg):row=rp(row,powers[j][n])
   out=add(out,scale(row,scalar(c)))
  return out
 generated=[];labels=[];basis=[];tags=[];piv=[]
 def addrow(row,label):
  ii=len(generated);generated.append(row[:]);labels.append(label);tag={ii:K(1)}
  for b,pv,bt in zip(basis,piv,tags):
   cf=row[pv]
   if not cf:continue
   row=sub(row,scale(b,cf))
   for key,val in bt.items():tag[key]=tag.get(key,K())-cf*val
  if not any(row):return False
  pv=next(i for i,v in enumerate(row) if v);iv=row[pv].inv();row=scale(row,iv);tag={j:c*iv for j,c in tag.items() if c}
  for j in range(6):assert sum((c*generated[i][j] for i,c in tag.items()),K())==row[j]
  basis.append(row);piv.append(pv);tags.append(tag)
  return True
 for rec in data['matrix']:addrow([K(MP(c)) for c in rec['row']],['actual_QQ_original_three_overlap_product_row',rec['name']])
 for rec in data['original']:addrow(evalrow(rec['poly']),['actual_QQ_original_polynomial_via_true_multiplication',rec['name']])
 cursor=0
 while cursor<len(basis) and len(basis)<6:
  for ax in range(3):
   addrow(rp(basis[cursor],mats[ax]),['right_multiply_prior_QQ_necessary_row',cursor,ax])
   if len(basis)==6:break
  cursor+=1
 assert len(basis)==6
 # The six row formulas lift to QQ(Q) necessary rows: every residue coefficient
 # in tags is lifted by its least nonnegative coefficient polynomial; each
 # generated multiplication node uses the already verified original M matrices.
 # No unreduced residue vector is declared itself to be a QQ necessary row.
 for i in range(6):
  assert basis[i][piv[i]]==1
  for j in range(i):assert basis[i][piv[j]]==0
 out=e0[:];cf=[]
 for b,pv in zip(basis,piv):
  c=out[pv];cf.append(c);out=sub(out,scale(b,c))
 assert not any(out)
 for j in range(6):assert sum((cf[i]*basis[i][j] for i in range(6)),K())==e0[j]
 cert=dict(factor=mcoeff(f),multiplicity=int(multiplicity),sourceRowLabels=labels,basis=[[mcoeff(v.q) for v in row] for row in basis],basisTags=[{str(i):mcoeff(c.q) for i,c in tt.items()} for tt in tags],pivots=piv,constantRowCombination=[mcoeff(v.q) for v in cf],coefficientLift='least nonnegative integer coefficient polynomial',QQRowLifts='recursive original-row combination and right multiplication formulas; no residue-vector-only lift')
 bs=json.dumps(cert,separators=(',',':')).encode()
 return dict(factorDegree=f.degree(),multiplicity=int(multiplicity),originalNecessaryRank=6,generatedRows=len(generated),allSixOriginalColumnCombinationProductsVerified=True,liftedNecessaryRowDeterminantResidueUnit=True,allInverseBezoutAndProductsVerified=True,certificateBytes=len(bs),certificateSHA256=hashlib.sha256(bs).hexdigest())

records=[]
for f,m in factors:
 t0=time.perf_counter();r=component(f,m);r['wallSeconds']=time.perf_counter()-t0;records.append(r)
 say(stage='F95_entire_modular_factor_original_necessary_rank',**r)
assert sum(r['factorDegree']*r['multiplicity'] for r in records)==95
signal.alarm(0)
result=dict(stage='COMPLETE_F95_UNIVARIATE_GAUSS_ORIGINAL_EXCLUSION',session='Astra-ISP-8542378f-20261127',sourceSHA256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),inputSHA256=hashlib.sha256(raw_bytes).hexdigest(),prime=prime,QQPrimitiveDegree=95,QQPrimitiveLeadingModPrime=int(ints[-1]%prime),QQPrimitivePolynomialSHA256=hashlib.sha256(json.dumps(ints).encode()).hexdigest(),allOriginalDenominatorsBezoutOneModuloWholeF95=True,wholeModularFactorizationProductVerified=True,wholeFactorReturns=records,GaussScope='single univariate parameter Q: any positive QQ common factor of F95 and all necessary six-row determinants has degree-preserving reduction and contradicts its matching modular-factor determinant unit',allNecessaryQQRowsDefinedByOriginalRowAndTruePointMultiplicationFormulas=True,allLeadingZeroFactorsRetained=True,multivariateModularEmptinessUsed=False,physicalDSaturationNotUsedInModularLift=True,F95Excluded=True,wholeUEqualsQRequiresSeparatelyRecordedComplementF3F9=True,sourceWallSeconds=time.perf_counter()-start,peakRssKiB=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss,ordinaryISPCompleted=False)
out_path.write_text(json.dumps(result,indent=2)+'\n')
say(stage='COMPLETE_F95_ORIGINAL_GAUSS_RETURN_SAVED',sourceWallSeconds=result['sourceWallSeconds'],peakRssKiB=result['peakRssKiB'],outputBytes=out_path.stat().st_size,outputSHA256=hashlib.sha256(out_path.read_bytes()).hexdigest(),QQDegreePreserved=95,allOriginalUnivariateFactorsCovered=True,F95Excluded=True,ordinaryISPCompleted=False)

