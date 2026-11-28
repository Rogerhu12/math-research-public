#!/usr/bin/env python3
"""NEW two complete QQ quadratic fibers of the t=0 original F12 cover.
The only rebuilt prefix constructs the original SAME-POINT four scalar
rows. It stops BEFORE all old factorization and fixed resultants.
Use QQ[k]/(k^2-2k-16) and QQ[k]/(k^2+8k+8), retaining both complex
embeddings and every e-leading degeneration. All e Euclid combinations
are returned in the complete exact coefficient field.
Only actual paid weight/geometry factors may be saturated; a final
POWER of the selected original paid product must return to the
original four-row ideal. No numeric/modular vanishing is promoted.
The original projection multiplicities 2 and 4 are recovered by the
nilpotent-ideal lift in the monic e^7 finite model.
180s/4GiB. No prior resultants, factorization or parameter gate replay.
Only source/definitions/degrees/SHA and small receipts.
"""
import json,time,hashlib,signal,resource,contextlib,io,math
from pathlib import Path
from flint import fmpq,fmpq_poly
START=time.perf_counter();DEADLINE=START+180
signal.setitimer(signal.ITIMER_REAL,180)
resource.setrlimit(resource.RLIMIT_AS,(4*1024**3,4*1024**3))
def say(**kw):
 kw['seconds']=time.perf_counter()-START
 print(json.dumps(kw,separators=(',',':')),flush=True)
def digest(x):
 raw=json.dumps(x,separators=(',',':')).encode()
 return dict(bytes=len(raw),sha256=hashlib.sha256(raw).hexdigest())
path=Path(__file__).with_name('2026-11-28-unit211-W-t-zero-V2-nonzero-same-original-fixed-projections-8542.py')
raw=path.read_bytes()
assert hashlib.sha256(raw).hexdigest()=='a6b1a22ac3ced79f4a032df4e990b0158ea7219656fcf78b31826d77c12a8008'
marker=b'\ndef factor_profile(p):'
assert raw.count(marker)==1
prefix=raw.split(marker)[0]
assert len(prefix)==8038 and hashlib.sha256(prefix).hexdigest()=='106524d7d5d73ae4a824d4c416d4778b39119b41c15f14013432a50afe384b79'
env={'__file__':str(path),'__name__':'new_two_constant_fields_original_rows_only'}
old_alarm=signal.alarm;old_timer=signal.setitimer
def timer(which,seconds,interval=0.0):
 if which!=signal.ITIMER_REAL:return old_timer(which,seconds,interval)
 assert not interval
 left=max(.001,DEADLINE-time.perf_counter())
 return old_timer(which,min(left,float(seconds) if seconds>0 else left),0.0)
def alarm(seconds):return math.ceil(timer(signal.ITIMER_REAL,seconds)[0])
signal.alarm=alarm;signal.setitimer=timer
try:
 with contextlib.redirect_stdout(io.StringIO()):
  exec(compile(prefix,str(path)+'#necessary_original_scalar_prefix','exec'),env)
finally:
 signal.alarm=old_alarm;signal.setitimer=old_timer
 old_timer(signal.ITIMER_REAL,max(.001,DEADLINE-time.perf_counter()))
original=[env[x] for x in ['Pmean','PN','PSN','PSP']]
paid=list(env['units'])+[('original_physical_D',env['Dphysical'].n)]
env['paid_den'](env['Dphysical'].d)
inverse_returns=0;division_returns=0;bezout_returns=0;mod_product_returns=0
field_B=fmpq(0);field_C=fmpq(0)
class K:
 __slots__=('a','b')
 def __init__(self,a=0,b=0):
  if isinstance(a,K):
   assert b==0;self.a=a.a;self.b=a.b
  else:self.a=fmpq(a);self.b=fmpq(b)
 def __bool__(self):return bool(self.a) or bool(self.b)
 def __neg__(self):return K(-self.a,-self.b)
 def __add__(self,o):
  o=K(o);return K(self.a+o.a,self.b+o.b)
 __radd__=__add__
 def __sub__(self,o):return self+-K(o)
 def __rsub__(self,o):return K(o)+-self
 def __mul__(self,o):
  o=K(o)
  return K(self.a*o.a-field_C*self.b*o.b,
           self.a*o.b+self.b*o.a-field_B*self.b*o.b)
 __rmul__=__mul__
 def inv(self):
  global inverse_returns
  assert self
  norm=self.a*self.a-field_B*self.a*self.b+field_C*self.b*self.b
  assert norm,'nonzero element unexpectedly nonunit in proved QQ quadratic field'
  out=K((self.a-field_B*self.b)/norm,-self.b/norm)
  assert self*out==K(1) and out*self==K(1)
  inverse_returns+=1;return out
 def __truediv__(self,o):return self*K(o).inv()
 def __rtruediv__(self,o):return K(o)*self.inv()
 def __pow__(self,n):
  if n<0:return self.inv()**(-n)
  r=K(1);b=self
  while n:
   if n&1:r=r*b
   n//=2
   if n:b=b*b
  return r
 def __eq__(self,o):
  o=K(o);return self.a==o.a and self.b==o.b
 def data(self):return [str(self.a),str(self.b)]
def trim(p):
 while p and not p[-1]:p.pop()
 return p
def add(p,q):
 return trim([(p[i] if i<len(p) else K())+(q[i] if i<len(q) else K())
              for i in range(max(len(p),len(q)))])
def neg(p):return [-a for a in p]
def sub(p,q):return add(p,neg(q))
def mul(p,q):
 if not p or not q:return []
 r=[K() for _ in range(len(p)+len(q)-1)]
 for i,a in enumerate(p):
  for j,b in enumerate(q):r[i+j]=r[i+j]+a*b
 return trim(r)
def scale(p,c):
 c=K(c);return trim([a*c for a in p])
def eq(p,q):return not sub(p,q)
def dm(p,q):
 global division_returns
 assert q
 before=p[:];r=p[:];a=[K() for _ in range(max(0,len(p)-len(q)+1))]
 ilc=q[-1].inv()
 while r and len(r)>=len(q):
  d=len(r)-len(q);c=r[-1]*ilc;a[d]=a[d]+c
  for j in range(len(q)):r[d+j]=r[d+j]-c*q[j]
  trim(r)
 a=trim(a)
 assert eq(add(mul(a,q),r),before)
 division_returns+=1;return a,r
def exact(p,q):
 a,r=dm(p,q);assert not r;return a
def xgcd(p,q):
 global bezout_returns
 pp,qq=p[:],q[:]
 s,t=[K(1)],[]
 ss,tt=[],[K(1)]
 while q:
  a,r=dm(p,q);p,q=q,r
  s,ss=ss,sub(s,mul(a,ss));t,tt=tt,sub(t,mul(a,tt))
 if p:
  c=p[-1].inv();p=scale(p,c);s=scale(s,c);t=scale(t,c)
 assert eq(add(mul(s,pp),mul(t,qq)),p)
 bezout_returns+=1;return p,s,t
def eimage(p):
 k=K(0,1);powers=[K(1)]
 n=max((int(m[0]) for m in p.to_dict()),default=-1)
 out=[K() for _ in range(n+1)]
 for mm,c in p.to_dict().items():
  ie,ik=map(int,mm)
  while len(powers)<=ik:powers.append(powers[-1]*k)
  out[ie]=out[ie]+K(c)*powers[ik]
 return trim(out)
def info(p):
 return dict(degree_e=len(p)-1,**digest([a.data() for a in p]))
def modular_power(p,n,g):
 global mod_product_returns
 p=dm(p,g)[1];out=dm([K(1)],g)[1]
 while n:
  if n&1:
   before=mul(out,p);quo,out=dm(before,g)
   assert eq(add(mul(quo,g),out),before);mod_product_returns+=1
  n//=2
  if n:
   before=mul(p,p);quo,p=dm(before,g)
   assert eq(add(mul(quo,g),p),before);mod_product_returns+=1
 return out
definitions=[
 dict(coefficients=[-16,-2,1],multiplicity=2,discriminant=68,
      sha256='c8d1a4fe6ca448230576fef6aecfcb7dcb0bcd5ae381e9bb7fb7d4886dbe92dd'),
 dict(coefficients=[8,8,1],multiplicity=4,discriminant=32,
      sha256='9526e32c263849d71edfb1f466d3871c3b56b7484047221b42480bb470bf279b')]
closed=[]
for index,defn in enumerate(definitions):
 phi=fmpq_poly(defn['coefficients'])
 assert digest([str(c) for c in phi.coeffs()])['sha256']==defn['sha256']
 field_C=phi[0];field_B=phi[1]
 disc=field_B**2-4*field_C
 assert disc==defn['discriminant'] and math.isqrt(int(disc))**2!=disc
 k=K(0,1)
 assert k*k+K(field_B)*k+K(field_C)==K()
 assert k*k.inv()==K(1)
 images=[eimage(p) for p in original]
 assert len(images[0])==8 and images[0][-1]==k**4
 # Every original polynomial is actually specialized before its degree
 # or leading coefficient is examined; no generic e degree is forced.
 g=[];tags=[[] for _ in images]
 for j,row in enumerate(images):
  gg,s,t=xgcd(g,row)
  tags=[mul(s,a) for a in tags];tags[j]=add(tags[j],t);g=gg
  total=[]
  for tt,rr in zip(tags,images):total=add(total,mul(tt,rr))
  assert eq(total,g)
  say(stage='new_entire_quadratic_same_original_e_Bezout',
      fieldIndex=index,processedOriginalRows=j+1,
      originalSpecializedDegrees=[len(p)-1 for p in images],
      remainingCommonPolynomial=info(g),
      allOriginalCombinationProductsReturned=True)
  if len(g)==1:break
 assert g
 original_g=g[:]
 selected_product=[K(1)];removed=[]
 for name,atom in paid:
  if len(g)==1:break
  image=eimage(atom);count=0
  while len(g)>1:
   h,_,_=xgcd(g,image)
   if len(h)==1:break
   g=exact(g,h);count+=1
  if count:
   selected_product=mul(selected_product,image)
   removed.append(dict(originalUnit=name,passes=count,
       unitImage=info(image),remaining=info(g)))
 if len(g)==1:
  if len(original_g)==1:
   assert original_g==[K(1)];power=0
  else:
   power=len(original_g)-1
   assert not modular_power(selected_product,power,original_g)
  closed.append(True)
  say(stage='new_complete_constant_original_fiber_excluded',
      fieldIndex=index,phiDefinition=defn,
      wholeQQQuadraticBothEmbeddingsKept=True,
      originalMeanMonicEDegree=7,
      originalFourRowGCD=info(original_g),
      originalPaidRemovals=removed,
      exactOriginalPaidProductPowerReturned=power,
      selectedPaidProduct=info(selected_product),
      actualELeadingDegenerationsPreserved=True,
      allProjectionMultiplicityLayers=defn['multiplicity'],
      nilpotentLiftUsesMonicFiniteEModel=True,
      noModularOrNumericPointReturn=True)
 else:
  closed.append(False)
  say(stage='new_complete_constant_original_fiber_retained',
      fieldIndex=index,phiDefinition=defn,
      originalFourRowGCD=info(original_g),
      originalPaidRemovals=removed,remaining=info(g),
      allRemainingERootsAndMultiplicitiesKept=True,
      claimExcluded=False)
say(stage='new_two_complete_quadratic_original_fibers_finished',
 sourceSHA256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
 fieldResults=closed,whole_t_zero_Excluded=all(closed),
 originalMeanLeadingCoefficient='k^4',
 originalProjectionMultiplicities=[2,4],
 actualQuadraticInverseProducts=inverse_returns,
 actualExactPolynomialDivisionProducts=division_returns,
 actualWholeBezoutProducts=bezout_returns,
 actualPaidProductModularPowerProducts=mod_product_returns,
 allFiniteLeadingZeroAndDZeroFibersKeptUntilOriginalUnitReturn=True,
 noOldFixedResultantsOrFactorizationExecuted=True,
 noLargeCoefficientPayloadSaved=True,
 peakRSSKiB=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss,
 ordinaryISPClaim=False)
