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
input_path=Path(sys.argv[1]) if len(sys.argv)>1 else here/'uq8542_direct_cramer_input.json'
out_path=Path(sys.argv[2]) if len(sys.argv)>2 else here/'uq8542_complete_native_return_output.json'
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
class R:
 def __init__(self,n=0,d=None):
  if isinstance(n,R):self.n=n.n;self.d=n.d;return
  if not isinstance(n,fmpq_poly):n=P([n])
  if d is None:d=one
  elif not isinstance(d,fmpq_poly):d=P([d])
  assert d
  if not n:self.n=zero;self.d=one;return
  g=n.gcd(d);n=exact(n,g);d=exact(d,g);lc=d[d.degree()]
  self.n=n/lc;self.d=d/lc
 def __bool__(self):return bool(self.n)
 def __add__(self,v):
  v=R(v);g=self.d.gcd(v.d);a=exact(self.d,g);b=exact(v.d,g)
  return R(self.n*b+v.n*a,a*v.d)
 __radd__=__add__
 def __neg__(self):return R(-self.n,self.d)
 def __sub__(self,v):return self+-R(v)
 def __rsub__(self,v):return R(v)+-self
 def __mul__(self,v):
  v=R(v);g=self.n.gcd(v.d);h=v.n.gcd(self.d)
  return R(exact(self.n,g)*exact(v.n,h),exact(self.d,h)*exact(v.d,g))
 __rmul__=__mul__
 def __truediv__(self,v):v=R(v);assert v;return self*R(v.d,v.n)
 def __pow__(self,n):
  if n<0:return R(self.d**(-n),self.n**(-n))
  return R(self.n**n,self.d**n)
 def __eq__(self,v):v=R(v);return self.n*v.d==v.n*self.d
coords=[R(p,delta) for p in numer]
for i,c in enumerate(coords):assert c.n*delta==numer[i]*c.d
allowed=delta
for a in atoms:allowed*=a
def allowed_den(c):
 d=c.d
 while d:
  g=d.gcd(allowed)
  if g.degree()<=0:break
  d=exact(d,g)
 assert d.degree()<=0
for c in coords:allowed_den(c)
x,y,t,yy,yt=coords
consistency=[yy-y*y,yt-y*t]
for c in consistency:allowed_den(c)
def eval_original(ts):
 out=R()
 for mon,cf in ts:
  i,j,k=map(int,mon.split(','))
  cc=R(P(cf['n']),P(cf['d']))
  out+=cc*x**i*y**j*t**k
 return out
returns=[]
for rec in data['original']:
 v=eval_original(rec['poly']);allowed_den(v)
 pp,pr,ph=strip(v.n)
 returns.append(dict(name=rec['name'],value=v,reduced=pp,paid=pr,history=ph))
 say(stage='new_same_Q_original_return_on_Cramer_graph',name=rec['name'],zero=not bool(v),numeratorDegree=v.n.degree(),unpaidDegree=pp.degree(),denominatorDegree=v.d.degree(),claimExcluded=False)
recon={name:eval_original(ts) for name,ts in data['reconstruction'].items()}
for v in recon.values():allowed_den(v)
covers=[p['reduced'] for p in returns if p['reduced']]
covers += [strip(c.n)[0] for c in consistency if c]
g=zero
for p in covers:g=g.gcd(p)

# New certificate for the complete nonzero original Cramer-leading chart.
bezout=[]
cg=zero
for idx,pp in enumerate(covers):
 gg,s,tb=cg.xgcd(pp)
 assert s*cg+tb*pp==gg
 bezout=[s*v for v in bezout]+[tb]
 assert sum((c*covers[j] for j,c in enumerate(bezout)),zero)==gg
 cg=gg
 say(stage='same_Q_original_return_Bezout',inputIndex=idx,gcdDegree=cg.degree(),bothOriginalUnivariateProductsVerified=True,allCombinedOriginalProductsVerified=True,claimWholeUEqualsQExcluded=False)
 if cg.degree()==0:break
assert cg==one
bezout_bytes=json.dumps([coeffs(p) for p in bezout],separators=(',',':')).encode()
bezout_receipt=dict(numberOriginalReturnsUsed=len(bezout),coefficientDegrees=[p.degree() for p in bezout],certificateBytes=len(bezout_bytes),certificateSHA256=hashlib.sha256(bezout_bytes).hexdigest(),allActualUnivariateBezoutProductsOne=True)
say(stage='original_Cramer_nonzero_chart_excluded',**bezout_receipt,leadingZeroFiberRetained=True)

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
def reduce_original(F,mode):
 K,F=finite_algebra(F)
 def scalar(c):
  dn=K(P(c['d']));iv=dn.inv();assert dn*iv==1
  return K(P(c['n']))*iv
 def value(ts,xx,yy,tt):
  s=K()
  for mon,c in ts:
   i,j,k=map(int,mon.split(','))
   s+=scalar(c)*xx**i*yy**j*tt**k
  return s
 km=[[K(v) for v in r] for r in orig]
 aa=[r[:] for r in km];nr=len(aa);trace=[[K(int(i==j)) for j in range(nr)] for i in range(nr)];pos=0;piv=[]
 for col in range(5):
  opts=[i for i in range(pos,nr) if aa[i][col]]
  if not opts:continue
  sw=min(opts,key=lambda i:aa[i][col].q.degree())
  aa[pos],aa[sw]=aa[sw],aa[pos];trace[pos],trace[sw]=trace[sw],trace[pos]
  iv=aa[pos][col].inv()
  aa[pos]=[v*iv for v in aa[pos]];trace[pos]=[v*iv for v in trace[pos]]
  for i in range(pos+1,nr):
   cf=aa[i][col]
   if cf:
    aa[i]=[v-cf*aa[pos][j] for j,v in enumerate(aa[i])]
    trace[i]=[v-cf*trace[pos][j] for j,v in enumerate(trace[i])]
  piv.append(col);pos+=1
 if pos==5:
  for i in range(pos):
   for j in range(6):assert sum((trace[i][h]*km[h][j] for h in range(nr)),K())==aa[i][j]
  kv=[K() for _ in range(5)]
  for i in range(4,-1,-1):
   assert piv[i]==i and aa[i][i]==1
   kv[i]=-aa[i][5]-sum((aa[i][j]*kv[j] for j in range(i+1,5)),K())
  for r in km:assert sum((r[j]*kv[j] for j in range(5)),K())+r[5]==0
  tests=[('y_square_same_point',kv[3]-kv[1]*kv[1]),('yt_same_point',kv[4]-kv[1]*kv[2])]
  tests.extend((rec['name'],value(rec['poly'],*kv[:3])) for rec in data['original'])
  for name,v in tests:
   if v:
    iv=v.inv();assert iv*v==1
    cert=dict(modulus=coeffs(F),linearTrace=[[[str(c) for c in v.q.coeffs()] for v in r] for r in trace[:5]],coordinatePolynomials=[coeffs(v.q) for v in kv],contradictionRow=name,value=coeffs(v.q),inverse=coeffs(iv.q))
    cb=json.dumps(cert,separators=(',',':')).encode()
    return dict(degree=F.degree(),mode='entire_constant_algebra_same_point_original_Cramer_return',nonconstantRank=5,contradictionRow=name,allEightOriginalRowsReturned=True,allFiveLinearTraceProductsVerified=True,actualOriginalNecessaryValueTimesInverseOne=True,certificateBytes=len(cb),certificateSHA256=hashlib.sha256(cb).hexdigest(),excluded=True)
  raise AssertionError('nonzero finite modulus left all original returns zero')
 # A genuine lower-rank fiber: preserve it and return the complete original degree-four Macaulay matrix.
 mons=[]
 for i in range(5):
  for j in range(5-i):
   for k in range(5-i-j):mons.append((i,j,k))
 mons.sort(key=lambda m:(-sum(m),-m[0],-m[1],-m[2]))
 assert len(mons)==35 and mons[-1]==(0,0,0)
 ix={m:i for i,m in enumerate(mons)};mm=[];labels=[]
 for rec in data['original']:
  pp=[(tuple(map(int,mon.split(','))),scalar(c)) for mon,c in rec['poly']]
  deg=max(sum(m) for m,c in pp)
  for shift in (m for m in mons if sum(m)<=4-deg):
   row=[K() for _ in mons]
   for mon,c in pp:
    target=tuple(mon[j]+shift[j] for j in range(3))
    row[ix[target]]+=c
   mm.append(row);labels.append([rec['name'],list(shift)])
 assert len(mm)==48
 aa=[r[:] for r in mm];tr=[[K(int(i==j)) for j in range(48)] for i in range(48)];pos=0
 for col in range(35):
  opts=[i for i in range(pos,48) if aa[i][col]]
  if not opts:continue
  sw=min(opts,key=lambda i:aa[i][col].q.degree())
  aa[pos],aa[sw]=aa[sw],aa[pos];tr[pos],tr[sw]=tr[sw],tr[pos]
  iv=aa[pos][col].inv();aa[pos]=[v*iv for v in aa[pos]];tr[pos]=[v*iv for v in tr[pos]]
  for i in range(pos+1,48):
   cf=aa[i][col]
   if cf:
    aa[i]=[v-cf*aa[pos][j] for j,v in enumerate(aa[i])]
    tr[i]=[v-cf*tr[pos][j] for j,v in enumerate(tr[i])]
  pos+=1
  if col==34:
   alpha=tr[pos-1]
   for j in range(35):assert sum((alpha[i]*mm[i][j] for i in range(48)),K())==int(j==34)
   cert=dict(modulus=coeffs(F),rowLabels=labels,monomials=mons,coefficients=[coeffs(v.q) for v in alpha])
   cb=json.dumps(cert,separators=(',',':')).encode()
   return dict(degree=F.degree(),mode='entire_constant_algebra_full_original_M35',priorOriginalNonconstantRank=len(piv),rank=pos,rows=48,columns=35,all35ActualOriginalProductsEqualConstantOne=True,certificateBytes=len(cb),certificateSHA256=hashlib.sha256(cb).hexdigest(),excluded=True)
 raise AssertionError('whole original finite leading fiber incomplete at M35')

# Every factor, with its original multiplicity, is retained in this cover.
lc,fac=lead.factor();back=P([lc])
for ff,mm in fac:back*=ff**mm
assert back==lead
pending=[monic(ff) for ff,mm in fac];finite=[];splits=[]
while pending:
 F=pending.pop(0);ft=time.perf_counter()
 try:
  rr=reduce_original(F,'original finite leading')
  rr['wallSeconds']=time.perf_counter()-ft;finite.append(rr)
  say(stage='entire_original_Cramer_leading_fiber_return',**rr)
 except Nonunit as err:
  left=err.factor;right=exact(F,left)
  assert left*right==F and 0<left.degree()<F.degree()
  splits.append(dict(parent=coeffs(F),left=coeffs(left),right=coeffs(right),actualFactorProductVerified=True))
  pending[:0]=[left,monic(right)]
  say(stage='entire_original_constant_algebra_nonunit_pivot_split',parentDegree=F.degree(),leftDegree=left.degree(),rightDegree=right.degree(),allFibersRetained=True)
assert all(r['excluded'] for r in finite)
signal.alarm(0)
result=dict(stage='COMPLETE_U_EQUALS_Q_ORIGINAL_REMAINING_CRAMER_COVER_EXCLUDED',session='Astra-ISP-8542378f-20261127',sourceSHA256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),inputSHA256=hashlib.sha256(raw_bytes).hexdigest(),limits=dict(seconds=60,addressSpaceBytes=4*1024**3),leadingProfile=profile('original_CramerLeadingUnpaid',lead),nonzeroLeadingOriginalBezout=bezout_receipt,wholeLeadingFactorReturns=finite,allNonunitSplits=splits,allOriginalCramerRowsSamePoint=True,allPhysicalDenominatorsAndNewLeadingFibersHandled=True,priorF9ReturnRequiredAndSeparatelyRecorded=True,ordinaryISPCompleted=False,wholeWZeroExcluded=False,wholeUEqualsQExcludedConditionalOnRecordedOriginalInputs=True,sourceWallSeconds=time.perf_counter()-start,peakRssKiB=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)
out_path.write_text(json.dumps(result,indent=2)+'\n')
say(stage='COMPLETE_U_EQUALS_Q_ORIGINAL_REMAINING_RETURN_SAVED',sourceWallSeconds=result['sourceWallSeconds'],peakRssKiB=result['peakRssKiB'],outputBytes=out_path.stat().st_size,outputSHA256=hashlib.sha256(out_path.read_bytes()).hexdigest(),allLeadingFiniteFactorsExcluded=True,originalNonzeroLeadingChartBezoutOne=True,wholeUEqualsQExcludedWithRecordedF9Inputs=True,ordinaryISPCompleted=False)

