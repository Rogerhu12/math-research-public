#!/usr/bin/env python3
"""NEW entire alpha=0 last QQ quadratic weight fiber, not old projections.
Input phi(k)=k^2+8k+8, from the actual original cover phi^4.
Only the frozen SAME-POINT original Gram/five-row prefix is rebuilt.
The original EBo has paid V^2 coefficient 4*u*Uhat/M^2.
Positive-power pseudo-reduction yields eight exact original two-column
rows over QQ[k]/phi[e]. True pair cofactors and whole-field Bezout
preserve every e-leading zero. Only original paid factors are removed,
and a POWER of their product must actually return modulo the original
cofactor gcd. Both QQ embeddings and all four cover layers remain.
180s/4GiB. No old V/e determinant, factorization or modular replay.
Only definitions/degrees/SHA and small receipts; no coefficient cache.
"""
import json,time,hashlib,signal,resource,contextlib,io,math,itertools
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
path=Path(__file__).with_name('2026-11-28-unit211-W-alpha-zero-whole-original-single-V-projections-8542.py')
raw=path.read_bytes()
assert hashlib.sha256(raw).hexdigest()=='87abb760a803666ff0ec1e8afeb8c7bdc7737d908b5b8d56625856ad04a2cc61'
marker=b'\ndef vcoeff(p):'
assert raw.count(marker)==1
prefix=raw.split(marker)[0]
assert len(prefix)==8836 and hashlib.sha256(prefix).hexdigest()=='a94137db3b117087205325533fb64cfda913d3dcf1bf1a3485989680b923968e'
env={'__file__':str(path),'__name__':'new_alpha_quadratic_original_rows_only'}
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
  exec(compile(prefix,str(path)+'#necessary_original_five_rows','exec'),env)
finally:
 signal.alarm=old_alarm;signal.setitimer=old_timer
 old_timer(signal.ITIMER_REAL,max(.001,DEADLINE-time.perf_counter()))
original_names=['EWp','EOp','N1p','Lowp','NSp']
original_mpoly=[env[n] for n in original_names]
paid_mpoly=list(env['units'])
def raw_vcoeff(p):
 if not p:return []
 out=[env['zz'] for _ in range(int(p.degrees()[2])+1)]
 for mm,c in p.to_dict().items():
  ie,ik,iv=map(int,mm);out[iv]+=c*env['ep']**ie*env['kp']**ik
 return out
raw_EBo=env['EB'].b
assert all(int(mm[2])==0 for mm in raw_EBo.d.to_dict())
raw_head=env['R'](raw_vcoeff(raw_EBo.n)[2],raw_EBo.d)
assert raw_head==4*env['u']*env['Uhat']/env['M']**2
env['paid_den'](raw_head.n);env['paid_den'](raw_head.d)
primitive_head=raw_vcoeff(env['EOp'])[2]
env['paid_den'](primitive_head)
say(stage='new_entire_alpha_quadratic_original_input',
 originalFiveRows=original_names,
 originalEBoHead='4*u*Uhat/M^2',
 originalHeadIdentityAndPaidSupportReturned=True,
 rebuildPrefixBytes=len(prefix),oldResultantsExecuted=False,
 physicalDNotInvertedOrUsedAsModularTarget=True)
phi=fmpq_poly([8,8,1])
assert digest([str(c) for c in phi.coeffs()])['sha256']=='9526e32c263849d71edfb1f466d3871c3b56b7484047221b42480bb470bf279b'
B=fmpq(8);C=fmpq(8);disc=B*B-4*C
assert disc==32 and math.isqrt(int(disc))**2!=disc
inverse_returns=0;division_returns=0;bezout_returns=0
v_identity_returns=0;original_identity_returns=0;modular_returns=0
class K:
 __slots__=('a','b')
 def __init__(self,a=0,b=0):
  if isinstance(a,K):
   assert b==0;self.a=a.a;self.b=a.b
  else:self.a=fmpq(a);self.b=fmpq(b)
 def __bool__(self):return bool(self.a) or bool(self.b)
 def __neg__(self):return K(-self.a,-self.b)
 def __add__(self,o):o=K(o);return K(self.a+o.a,self.b+o.b)
 __radd__=__add__
 def __sub__(self,o):return self+-K(o)
 def __rsub__(self,o):return K(o)+-self
 def __mul__(self,o):
  o=K(o);return K(self.a*o.a-C*self.b*o.b,self.a*o.b+self.b*o.a-B*self.b*o.b)
 __rmul__=__mul__
 def inv(self):
  global inverse_returns
  assert self
  norm=self.a*self.a-B*self.a*self.b+C*self.b*self.b
  assert norm,'nonzero element of the proved whole QQ quadratic field'
  out=K((self.a-B*self.b)/norm,-self.b/norm)
  assert self*out==K(1) and out*self==K(1)
  inverse_returns+=1;return out
 def __truediv__(self,o):return self*K(o).inv()
 def __pow__(self,n):
  if n<0:return self.inv()**(-n)
  out=K(1);base=self
  while n:
   if n&1:out=out*base
   n//=2
   if n:base=base*base
  return out
 def __eq__(self,o):o=K(o);return self.a==o.a and self.b==o.b
 def data(self):return [str(self.a),str(self.b)]
k=K(0,1)
assert k*k+B*k+C==K()
def qp(x):
 if hasattr(x,'coeffs'):return fmpq_poly(x)
 if isinstance(x,(list,tuple)):return fmpq_poly(x)
 return fmpq_poly([x])
class P:
 """Whole K[e], represented by two QQ[e] polynomials; never K(e)."""
 __slots__=('a','b')
 def __init__(self,a=0,b=None):
  if isinstance(a,P):
   assert b is None;self.a=a.a;self.b=a.b
  elif isinstance(a,K):
   assert b is None;self.a=qp(a.a);self.b=qp(a.b)
  else:self.a=qp(a);self.b=qp(0 if b is None else b)
 def __bool__(self):return bool(self.a) or bool(self.b)
 def __neg__(self):return P(-self.a,-self.b)
 def __add__(self,o):o=P(o);return P(self.a+o.a,self.b+o.b)
 __radd__=__add__
 def __sub__(self,o):return self+-P(o)
 def __rsub__(self,o):return P(o)+-self
 def __mul__(self,o):
  o=P(o);return P(self.a*o.a-C*self.b*o.b,self.a*o.b+self.b*o.a-B*self.b*o.b)
 __rmul__=__mul__
 def __eq__(self,o):o=P(o);return self.a==o.a and self.b==o.b
 def degree(self):return max(int(self.a.degree()),int(self.b.degree()))
 def lc(self):
  assert self;n=self.degree();return K(self.a[n],self.b[n])
 def monic(self):return self*P(self.lc().inv()) if self else P()
 def shift(self,n):
  assert n>=0
  z=qp([0]*n+[1]);return P(self.a*z,self.b*z)
 def data(self):return [[str(c) for c in self.a.coeffs()],[str(c) for c in self.b.coeffs()]]
def pinfo(p):return dict(degree_e=p.degree(),**digest(p.data()))
def dm(p,q):
 global division_returns
 p=P(p);q=P(q);assert q
 before=p;r=p;out=P();ilc=q.lc().inv()
 while r and r.degree()>=q.degree():
  d=r.degree()-q.degree();term=P(r.lc()*ilc).shift(d)
  out=out+term;r=r-term*q
 assert out*q+r==before
 division_returns+=1;return out,r
def exact(p,q):
 out,r=dm(p,q);assert not r;return out
def xgcd(p,q):
 global bezout_returns
 pp,qq=P(p),P(q);p,q=pp,qq
 s,t,ss,tt=P(1),P(),P(),P(1)
 while q:
  a,r=dm(p,q);p,q=q,r
  s,ss=ss,s-a*ss;t,tt=tt,t-a*tt
 if p:
  c=P(p.lc().inv());p,s,t=p*c,s*c,t*c
 assert s*pp+t*qq==p
 bezout_returns+=1;return p,s,t
def eimage(p):
 n=max((int(mm[0]) for mm in p.to_dict()),default=-1)
 aa=[fmpq(0)]*(n+1);bb=[fmpq(0)]*(n+1);powers=[K(1)]
 for mm,c in p.to_dict().items():
  ie,ik,iv=map(int,mm);assert iv==0
  while len(powers)<=ik:powers.append(powers[-1]*k)
  v=K(c)*powers[ik];aa[ie]+=v.a;bb[ie]+=v.b
 return P(aa,bb)
def vt(p):
 while p and not p[-1]:p.pop()
 return p
def vadd(p,q):return vt([(p[i] if i<len(p) else P())+(q[i] if i<len(q) else P()) for i in range(max(len(p),len(q)))])
def vneg(p):return [-a for a in p]
def vsub(p,q):return vadd(p,vneg(q))
def vscale(p,c):return vt([a*P(c) for a in p])
def vshift(p,n=1):return [P() for _ in range(n)]+p if p else []
def vmul(p,q):
 if not p or not q:return []
 out=[P() for _ in range(len(p)+len(q)-1)]
 for i,a in enumerate(p):
  for j,b in enumerate(q):out[i+j]=out[i+j]+a*b
 return vt(out)
def veq(p,q):return not vsub(p,q)
def vimage(p):return vt([eimage(c) for c in raw_vcoeff(p)])
def vinfo(p):
 return dict(degree_V=len(p)-1,degree_e=max((c.degree() for c in p),default=-1),
             **digest([c.data() for c in p]))
def pseudorem(p,q):
 global v_identity_returns
 assert q and len(q)==3
 before=p[:];r=p[:];quo=[];sc=P(1);a=q[-1]
 while r and len(r)>=len(q):
  d=len(r)-len(q);c=r[-1]
  r=vsub(vscale(r,a),vscale(vshift(q,d),c))
  quo=vadd(vscale(quo,a),vshift([c],d));sc=sc*a
 assert veq(vscale(before,sc),vadd(vmul(quo,q),r))
 assert len(r)<=2
 v_identity_returns+=1;return sc,quo,r
original=[vimage(p) for p in original_mpoly]
paid=[(name,eimage(p)) for name,p in paid_mpoly]
for name,p in paid:
 if not p:
  say(stage='new_entire_alpha_quadratic_excluded_by_original_unit',
      originalUnitIdenticallyZero=name,phiCoefficients=[8,8,1],
      wholeQQQuadraticBothEmbeddingsKept=True,
      originalProjectionMultiplicity=4,
      wholeAlphaZeroExcluded=True,noOldProjectionExecuted=True)
  raise SystemExit(0)
assert len(original[1])==3 and original[1][-1]==eimage(primitive_head)
q=original[1];a=q[-1]
def strip_paid(p):
 g=P(p);selected=P(1);removed=[]
 for name,atom in paid:
  count=0
  while g.degree()>0:
   h,_,_=xgcd(g,atom)
   if h.degree()==0:break
   g=exact(g,h);count+=1
  if count:
   selected=selected*atom
   removed.append(dict(originalUnit=name,passes=count,unitImage=pinfo(atom)))
  if g.degree()==0:break
 return g,selected,removed
head_remaining,head_product,head_removed=strip_paid(a)
assert head_remaining and head_remaining.degree()==0
def check_original(row,tags):
 global original_identity_returns
 out=[]
 for tag,p in zip(tags,original):out=vadd(out,vmul(tag,p))
 assert veq(out,row)
 original_identity_returns+=1
def tags_scale(tags,c):return [vscale(t,c) for t in tags]
def tags_add(a,b):return [vadd(x,y) for x,y in zip(a,b)]
def tags_sub(a,b):return [vsub(x,y) for x,y in zip(a,b)]
rows=[];alltags=[]
for i,p in enumerate(original):
 if i==1:continue
 sc,quo,r=pseudorem(p,q)
 tag=[[] for _ in original];tag[i]=[sc];tag[1]=vneg(quo)
 check_original(r,tag)
 rr=r+[P() for _ in range(2-len(r))]
 rows.append(rr);alltags.append(tag)
 # a*V*r-r_1*q remains affine. It is a new original combination,
 # and no e-polynomial is inverted in this construction.
 rv=vsub(vscale(vshift(r),a),vscale(q,rr[1]))
 assert len(rv)<=2
 tv=[vscale(vshift(tt),a) for tt in tag]
 tv[1]=vsub(tv[1],[rr[1]])
 check_original(rv,tv)
 rows.append(rv+[P() for _ in range(2-len(rv))]);alltags.append(tv)
assert len(rows)==8 and len(alltags)==8
say(stage='new_entire_alpha_quadratic_original_eight_two_module',
 phiCoefficients=[8,8,1],wholeQQQuadraticBothEmbeddingsKept=True,
 originalSpecializedVDegrees=[len(p)-1 for p in original],
 originalSpecializedEDegrees=[max((c.degree() for c in p),default=-1) for p in original],
 originalPaidQuadraticLeading=pinfo(a),
 originalLeadingPaidRemovals=head_removed,
 eightOriginalRowProfiles=[dict(degrees_e=[c.degree() for c in row]) for row in rows],
 allEightFiveSourceIdentitiesReturned=True,
 everyELeadingDegenerationPreserved=True,
 noGeometricOrEHeadInverse=True)
g=P();gtags=[[] for _ in original];processed=0
def modular_power(p,n,mod):
 global modular_returns
 _,p=dm(p,mod);_,out=dm(P(1),mod)
 while n:
  if n&1:
   before=out*p;quo,out=dm(before,mod)
   assert quo*mod+out==before;modular_returns+=1
  n//=2
  if n:
   before=p*p;quo,p=dm(before,mod)
   assert quo*mod+p==before;modular_returns+=1
 return out
closed=False;remaining=P();selected=P(1);removed=[]
def include_scalar(c,tag,definition):
 global g,gtags,processed,closed,remaining,selected,removed
 if not c:return False
 check_original([c],tag)
 gg,s,t=xgcd(g,c)
 gtags=tags_add(tags_scale(gtags,s),tags_scale(tag,t));g=gg
 check_original([g],gtags);processed+=1
 remaining,selected,removed=strip_paid(g)
 say(stage='new_whole_quadratic_original_scalar_Bezout',
     scalarDefinition=definition,processed=processed,
     sourceScalar=pinfo(c),originalScalarGCD=pinfo(g),
     remainingAfterOnlyOriginalPaidFactors=pinfo(remaining),
     wholeFiveOriginalCombinationReturned=True)
 if remaining and remaining.degree()==0:
  power=max(0,g.degree())
  if power==0:assert g==P(1)
  else:assert not modular_power(selected,power,g)
  closed=True
  say(stage='new_complete_alpha_quadratic_original_fiber_excluded',
      originalFiveRowScalarGCD=pinfo(g),
      originalPaidRemovals=removed,selectedOriginalPaidProduct=pinfo(selected),
      actualPaidProductPowerReturned=power,
      completeOriginalCombinationCertificate=digest([[c.data() for c in tag] for tag in gtags]),
      phiCoefficients=[8,8,1],allFourProjectionMultiplicityLayersRetained=True,
      nilpotentLift='phi^4 in I; unit return modulo phi implies unit in I',
      noNumericOrModularLifting=True)
 return closed
for i,row in enumerate(rows):
 if not row[1] and row[0]:
  if include_scalar(row[0],alltags[i],dict(kind='original_constant_module_row',row=i)):break
if not closed:
 for i,j in itertools.combinations(range(8),2):
  ai,bj=rows[i],rows[j]
  if not ai[1] and not bj[1]:continue
  hh,_,_=xgcd(ai[1],bj[1]);assert hh
  si=exact(bj[1],hh);sj=-exact(ai[1],hh)
  assert si*ai[1]+sj*bj[1]==P()
  scalar=si*ai[0]+sj*bj[0]
  tags=tags_add(tags_scale(alltags[i],si),tags_scale(alltags[j],sj))
  # Only the common factor of the ACTUAL two multipliers is cancelled;
  # the two-column and five-original polynomial identities are returned.
  if include_scalar(scalar,tags,dict(kind='original_pair_common_multiplier_cancelled',
                  rows=[i,j],cancelledMultiplierGCD=pinfo(hh))):break
assert g,'all original scalar cofactors vanished; no empty-fiber claim available'
if not closed:
 say(stage='new_complete_alpha_quadratic_original_fiber_retained',
     originalScalarGCD=pinfo(g),remaining=pinfo(remaining),
     originalPaidRemovals=removed,
     wholeRemainingERootsAndMultiplicitiesKept=True,
     claimExcluded=False,noUnpaidFactorOrHeadRemoved=True)
say(stage='new_entire_alpha_quadratic_original_return_finished',
 sourceSHA256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
 wholeAlphaZeroExcluded=closed,phiCoefficients=[8,8,1],projectionMultiplicity=4,
 actualQuadraticFieldDoubleInverseProducts=inverse_returns,
 actualWholeK_eDivisionProducts=division_returns,
 actualWholeK_eBezoutProducts=bezout_returns,
 actualPositivePowerVReductionProducts=v_identity_returns,
 actualCompleteFiveOriginalIdentityProducts=original_identity_returns,
 actualPaidProductPowerProducts=modular_returns,
 noOldFixedResultantOrProjectionFactorizationExecuted=True,
 noCoefficientPayloadSaved=True,
 peakRSSKiB=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss,
 ordinaryISPClaim=False)
