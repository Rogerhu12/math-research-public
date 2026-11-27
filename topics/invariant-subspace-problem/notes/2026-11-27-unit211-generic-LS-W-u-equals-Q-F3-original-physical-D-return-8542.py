#!/usr/bin/env python3
"""New original u=Q five-column Cramer graph; all leading-zero fibers retained.
Input is the eight already verified original three-overlap/product rows.
This is not the frozen expanded-monic-trace probe.
"""
import json,time,hashlib,signal,resource,sys
from pathlib import Path
from flint import fmpq_poly,fmpq
signal.alarm(60)
resource.setrlimit(resource.RLIMIT_AS,(4*1024**3,4*1024**3))
start=time.perf_counter()
here=Path(__file__).resolve().parent
input_path=Path(sys.argv[1]) if len(sys.argv)>1 else here/'uq8542_finite_module_input.json'
out_path=Path(sys.argv[2]) if len(sys.argv)>2 else here/'uq8542_finite_module_output.json'
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
class Nonunit(Exception):
 def __init__(self,g):self.factor=monic(g);super().__init__('NONUNIT_FINITE_QQ')
def finite_algebra(F):
 F=monic(F)
 class K:
  def __init__(self,p=0):
   if isinstance(p,K):self.q=p.q;return
   if not isinstance(p,fmpq_poly):p=P([p])
   a,r=divmod(p,F)
   assert a*F+r==p
   self.q=r
  def __bool__(self):return bool(self.q)
  def __add__(self,v):return K(self.q+K(v).q)
  __radd__=__add__
  def __neg__(self):return K(-self.q)
  def __sub__(self,v):return self+-K(v)
  def __rsub__(self,v):return K(v)+-self
  def __mul__(self,v):return K(self.q*K(v).q)
  __rmul__=__mul__
  def __pow__(self,n):return K(self.q**n)
  def __eq__(self,v):return self.q==K(v).q
  def inv(self):
   gg,s,tb=self.q.xgcd(F)
   assert s*self.q+tb*F==gg
   if gg.degree()!=0:raise Nonunit(gg)
   iv=K(s/gg[0])
   assert self*iv==1
   return iv
  def __truediv__(self,v):return self*K(v).inv()
 return K,F

def ksetup(F):
 K,F=finite_algebra(F)
 def scalar(c):
  dn=K(P(c['d']));iv=dn.inv();assert dn*iv==1
  return K(P(c['n']))*iv
 return K,F,scalar
def vecadd(a,b):return [v+b[j] for j,v in enumerate(a)]
def vecscale(a,c):return [v*c for v in a]
def vecsub(a,b):return [v-b[j] for j,v in enumerate(a)]
def veczero(a):return all(not v for v in a)
def rowprod(a,B,K):return [sum((a[k]*B[k][j] for k in range(6)),K()) for j in range(6)]
def matprod(A,B,K):return [rowprod(row,B,K) for row in A]
def original_same_point_fiber(F):
 K,F,scalar=ksetup(F);km=[[K(v) for v in r] for r in orig];aa=[r[:] for r in km];nr=len(aa);tr=[[K(int(i==j)) for j in range(nr)] for i in range(nr)];pos=0;piv=[]
 for col in range(5):
  opts=[i for i in range(pos,nr) if aa[i][col]]
  if not opts:continue
  sw=min(opts,key=lambda i:aa[i][col].q.degree());aa[pos],aa[sw]=aa[sw],aa[pos];tr[pos],tr[sw]=tr[sw],tr[pos]
  iv=aa[pos][col].inv();aa[pos]=vecscale(aa[pos],iv);tr[pos]=vecscale(tr[pos],iv)
  for i in range(pos+1,nr):
   cf=aa[i][col]
   if cf:aa[i]=vecsub(aa[i],vecscale(aa[pos],cf));tr[i]=vecsub(tr[i],vecscale(tr[pos],cf))
  piv.append(col);pos+=1
 assert pos==5
 for i in range(5):
  for j in range(6):assert sum((tr[i][h]*km[h][j] for h in range(nr)),K())==aa[i][j]
 kv=[K() for _ in range(5)]
 for i in range(4,-1,-1):assert piv[i]==i and aa[i][i]==1;kv[i]=-aa[i][5]-sum((aa[i][j]*kv[j] for j in range(i+1,5)),K())
 for r in km:assert sum((r[j]*kv[j] for j in range(5)),K())+r[5]==0
 tests=[('same_point_y_square',kv[3]-kv[1]**2),('same_point_yt',kv[4]-kv[1]*kv[2])]
 for rec in data['original']:
  vv=K()
  for mon,c in rec['poly']:
   i,j,k=map(int,mon.split(','));vv+=scalar(c)*kv[0]**i*kv[1]**j*kv[2]**k
  tests.append((rec['name'],vv))
 for name,v in tests:
  if v:
   iv=v.inv();assert v*iv==1
   cert=dict(modulus=coeffs(F),trace=[[coeffs(v.q) for v in r] for r in tr[:5]],coordinates=[coeffs(v.q) for v in kv],contradictionRow=name,value=coeffs(v.q),inverse=coeffs(iv.q))
   bs=json.dumps(cert,separators=(',',':')).encode()
   return dict(degree=F.degree(),nonconstantRank=5,contradictionRow=name,allEightOriginalRowsMultipliedBack=True,allFiveOriginalRowTraceProductsVerified=True,actualSamePointNecessaryValueTimesInverseOne=True,certificateBytes=len(bs),certificateSHA256=hashlib.sha256(bs).hexdigest(),excluded=True)
 raise AssertionError('entire original finite Cramer factor not yet excluded')
def original_physical_unit_module_fiber(F):
 K,F,scalar=ksetup(F);I6=[[K(int(i==j)) for j in range(6)] for i in range(6)];mats=[[[scalar(c) for c in row] for row in mat] for mat in data['multiplicationMatrices']];e0=I6[0]
 assert mats[0][0]==I6[1] and mats[1][0]==I6[2] and mats[2][0]==I6[3]
 assert rowprod(rowprod(e0,mats[1],K),mats[1],K)==I6[4]
 assert rowprod(rowprod(e0,mats[1],K),mats[2],K)==I6[5]
 powers=[[I6,mat] for mat in mats]
 for j in range(3):
  for n in range(2,4):powers[j].append(matprod(powers[j][-1],mats[j],K))
 def evalrow(ts):
  out=[K() for _ in range(6)]
  for mon,c in ts:
   mm=list(map(int,mon.split(',')));row=e0[:]
   for j,n in enumerate(mm):row=rowprod(row,powers[j][n],K)
   out=vecadd(out,vecscale(row,scalar(c)))
  return out
 def evalmat(ts):
  out=[[K() for _ in range(6)] for _ in range(6)]
  for mon,c in ts:
   mm=list(map(int,mon.split(',')));mat=I6
   for j,n in enumerate(mm):mat=matprod(mat,powers[j][n],K)
   cf=scalar(c)
   out=[vecadd(row,vecscale(mat[i],cf)) for i,row in enumerate(out)]
  return out
 generated=[];labels=[];basis=[];tags=[];pivots=[]
 def add(row,label):
  idx=len(generated);generated.append(row[:]);labels.append(label);tag={idx:K(1)};raw=row[:]
  for b,pv,bt in zip(basis,pivots,tags):
   cf=row[pv]
   if not cf:continue
   row=vecsub(row,vecscale(b,cf))
   for key,val in bt.items():tag[key]=tag.get(key,K())-cf*val
  if veczero(row):return False
  pv=next(i for i,v in enumerate(row) if v);iv=row[pv].inv();row=vecscale(row,iv);tag={j:c*iv for j,c in tag.items() if c}
  for j in range(6):assert sum((c*generated[i][j] for i,c in tag.items()),K())==row[j]
  basis.append(row);pivots.append(pv);tags.append(tag)
  return True
 for rec in data['matrix']:add([K(P(c)) for c in rec['row']],['previous_original_three_overlap_row',rec['name']])
 for rec in data['original']:add(evalrow(rec['poly']),['full_original_polynomial_evaluation',rec['name']])
 cursor=0
 while cursor<len(basis):
  for ax in range(3):add(rowprod(basis[cursor],mats[ax],K),['same_point_multiplication',cursor,ax])
  cursor+=1
  assert len(basis)<=6
 def reduce(row):
  trace=[]
  for b,pv in zip(basis,pivots):
   cf=row[pv];trace.append(cf);row=vecsub(row,vecscale(b,cf))
  return row,trace
 for i,b in enumerate(basis):
  for ax in range(3):
   raw=rowprod(b,mats[ax],K);rem,cf=reduce(raw);assert veczero(rem)
   for j in range(6):assert sum((cf[k]*basis[k][j] for k in range(len(basis))),K())==raw[j]
 Dm=evalmat(data['reconstruction']['D']);dp=e0[:];power=None;membership=None
 for n in range(7):
  rem,cf=reduce(dp)
  if veczero(rem):
   for j in range(6):assert sum((cf[k]*basis[k][j] for k in range(len(basis))),K())==dp[j]
   power=n;membership=cf;break
  dp=rowprod(dp,Dm,K)
 say(stage='whole_finite_original_physical_D_module',modulusDegree=F.degree(),necessaryRowRank=len(basis),generatedRows=len(generated),closureProductsVerified=True,DpowerReturned=power,allSixOriginalColumnsChecked=True,claimExcluded=power is not None)
 if power is None:return dict(degree=F.degree(),mode='original_six_generator_D_module',rank=len(basis),generatedRows=len(generated),DpowerReturned=None,allTruePointMultiplicationIdentitiesUsed=True,excluded=False)
 cert=dict(modulus=coeffs(F),labels=labels,basis=[[coeffs(v.q) for v in r] for r in basis],basisTags=[{str(i):coeffs(v.q) for i,v in tt.items()} for tt in tags],Dpower=power,membership=[coeffs(v.q) for v in membership],DpowerRow=[coeffs(v.q) for v in dp])
 bs=json.dumps(cert,separators=(',',':')).encode()
 return dict(degree=F.degree(),mode='whole_original_six_generator_physical_D_unit_return',necessaryRowRank=len(basis),generatedRows=len(generated),DpowerReturned=power,allOriginalEvaluationAndMultiplicationRowsPreserved=True,allActualClosureAndMembershipSixColumnProductsVerified=True,physicalUnitIdentity='D + ell*HA/u^2 = bc*(h-k)^2; HA=0; bc*(h-k) is a physical unit',certificateBytes=len(bs),certificateSHA256=hashlib.sha256(bs).hexdigest(),excluded=True)


F3=monic(P([-10,30,-25,4]));other=exact(lead,F3);assert other.degree()==95 and other*F3==lead
t0=time.perf_counter();rr=original_physical_unit_module_fiber(F3);rr['wallSeconds']=time.perf_counter()-t0
result=dict(stage='whole_u_equals_Q_F3_original_physical_module_return',session='Astra-ISP-8542378f-20261127',sourceSHA256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),inputSHA256=hashlib.sha256(raw_bytes).hexdigest(),finiteReturn=rr,sourceWallSeconds=time.perf_counter()-start,peakRssKiB=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss,wholeUEqualsQExcluded=False,ordinaryISPCompleted=False)
signal.alarm(0);out_path.write_text(json.dumps(result,indent=2)+'\n')
say(stage='whole_F3_original_physical_module_return_saved',**rr,sourceWallSeconds=result['sourceWallSeconds'],peakRssKiB=result['peakRssKiB'],outputBytes=out_path.stat().st_size,outputSHA256=hashlib.sha256(out_path.read_bytes()).hexdigest(),wholeUEqualsQExcluded=False)
assert rr['excluded']

