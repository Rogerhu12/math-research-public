#!/usr/bin/env python3
"""NEW correct Phi ell=1/2: physical z-unit blow-up tau=r*z.
The three TRUE means divide by z exactly and become affine in epsilon,z.
Keep N1's epsilon^2 term, the TWO complete raw NS/PS cubics, and every
affine-head-zero fiber. Nine fixed conic/cubic returns plus one determinant
are new original (u,r) necessary polynomials. ONE fixed QQ(u)[r] Bezout
target may give a pure-u cover. All final poles and positive z powers are
returned to SIX full raw equations. No old 20x18 solve, C114/C20 coefficients,
old lambda gcd, old 30 columns, or old z proof is replayed.
The old C20 is used ONLY by its published monic profile if NEW factors
arrive; no preclaimed new cover, gcd, or whole-branch exclusion.
120 seconds / 1 GiB, one dependency, one first mathematical execution.
"""
import hashlib,json,resource,signal,time
from pathlib import Path
from flint import fmpq_mpoly_ctx,fmpq_poly
START=time.perf_counter()
resource.setrlimit(resource.RLIMIT_AS,(1024**3,1024**3))
signal.setitimer(signal.ITIMER_REAL,120)
def say(stage,**kw):
 kw.update(stage=stage,seconds=time.perf_counter()-START)
 print(json.dumps(kw,sort_keys=True,separators=(',',':')),flush=True)
BASE='2026-11-28-unit211-Phi-zero-corrected-ell-half-direct-raw-degree-three-z-certificate-8542.py'
BASE_SHA='32e949c11469da6350c0403e2aead13d3558fce80f64b78021e3f1f65d87b15e'
rawtext=Path(__file__).with_name(BASE).read_text()
assert hashlib.sha256(rawtext.encode()).hexdigest()==BASE_SHA
prefix=rawtext[rawtext.index('ctx=fmpq_mpoly_ctx'):rawtext.index('monomials=')]
assert len(prefix.encode())==6013
assert hashlib.sha256(prefix.encode()).hexdigest()=='17df64c95494142eaae3d137442d464bdc87d7f0d881ca41d0910d50b6abdba9'
# Exactly the raw coefficient definitions, ending before ANY old matrix.
# This prefix has no signal/resource/import/file actions. Its old say is muted.
ns={'fmpq_mpoly_ctx':fmpq_mpoly_ctx,'fmpq_poly':fmpq_poly,
    'json':json,'hashlib':hashlib,'say':lambda *a,**k:None}
exec(compile(prefix,'<necessary-six-raw-definitions-only>','exec'),ns)
ctx=fmpq_mpoly_ctx.get(('u','r','epsilon','z'),'lex')
u,r,e,z=ctx.gens();O=ctx.constant(1);Z=ctx.constant(0)
stats={'newExactProducts':0,'newAffineReturns':0,
       'newHeadFreeReturns':0,'newFixedScalarOriginalReturns':0,
       'newRBezoutReturns':0,'newFinalRawPolynomialReturns':0}
def exact(a,b):
 q,rr=divmod(a,b);assert not rr and q*b==a
 stats['newExactProducts']+=1
 return q
def pure_u(p):return all(not any(int(x) for x in ex[1:]) for ex in p.to_dict())
def pure_ur(p):return all(not int(ex[2]) and not int(ex[3]) for ex in p.to_dict())
def profile(p):
 data=[[list(map(int,ex)),str(co)] for ex,co in sorted(p.to_dict().items())]
 raw=json.dumps(data,separators=(',',':')).encode()
 return {'zero':not bool(p),'degrees_u_r_epsilon_z':list(map(int,p.degrees())) if p else [-1]*4,
         'totalDegree':int(p.total_degree()) if p else -1,
         'terms':len(data),'bytes':len(raw),'sha256':hashlib.sha256(raw).hexdigest()}
def transform(p,blow):
 data={}
 for ex,co in p.to_dict().items():
  a,b,c,d=map(int,ex)
  key=(a,c,b,d+c if blow else d)
  data[key]=data.get(key,0)+co
 return ctx.from_dict(data)
raw_original=[(transform(v.n,False),transform(v.d,False)) for v in ns['original']]
raw_blow=[(transform(v.n,True),transform(v.d,True)) for v in ns['original']]
paid=transform(ns['paidSupport'],False)
assert pure_u(paid)
def remove_paid(p):
 saved=p;removed=O
 while p and int(p.total_degree())>0:
  gg=p.gcd(paid)
  if int(gg.total_degree())==0:break
  p=exact(p,gg);removed*=gg
 assert p*removed==saved
 return p,removed
for _,d in raw_original:
 assert d and pure_u(d)
 rr,_=remove_paid(d);assert rr and int(rr.total_degree())==0
def geomdegree(p):
 return max((int(ex[2])+int(ex[3]) for ex in p.to_dict()),default=-1)
def coeff(p,aa,bb):
 return ctx.from_dict({(int(ex[0]),int(ex[1]),0,0):co
    for ex,co in p.to_dict().items() if int(ex[2])==aa and int(ex[3])==bb})
J=[];affine=[]
for i in range(3):
 numerator=raw_blow[i][0]
 assert all(int(ex[1]) or int(ex[3]) for ex in raw_original[i][0].to_dict())
 # The actual epsilon degree <=1 is separate from absence of 1,epsilon.
 assert max((int(ex[2]) for ex in numerator.to_dict()),default=-1)<=1
 line=exact(numerator,z)
 assert z*line==numerator and geomdegree(line)<=1
 cc,aa,bb=coeff(line,0,0),coeff(line,1,0),coeff(line,0,1)
 assert cc+aa*e+bb*z==line
 J.append(line);affine.append((aa,bb,cc))
 stats['newAffineReturns']+=1
for i in range(3,6):
 J.append(raw_blow[i][0])
 assert geomdegree(J[-1])<=(2 if i==3 else 3)
assert coeff(J[3],2,0)  # Keep the original N1 epsilon^2 coefficient.
say('new_ell_half_z_blowup_three_true_affine_means',
    transformation='tau=r*z; ONLY the already-paid physical z is divided',
    eachOriginalNumeratorEqualsZTimesNewLine=True,
    originalEpsilonDegreesAtMostOneForFirstThree=True,
    N1EpsilonSquaredExplicitlyRetained=True,
    threeLineProfiles=[profile(v) for v in J[:3]],
    N1LeadingEpsilonSquared=profile(coeff(J[3],2,0)),
    wholeRawNSPSRetained=True,oldTwentyByEighteenGateNotRun=True,
    necessaryPrefixBytes=6013,necessaryPrefixSHA256='17df64c95494142eaae3d137442d464bdc87d7f0d881ca41d0910d50b6abdba9')
def original_return(value,tag):
 assert len(tag)==6
 assert sum((tag[i]*J[i] for i in range(6)),Z)==value
 stats['newFixedScalarOriginalReturns']+=1
def cancel_all(value,tag):
 original_return(value,tag)
 nonzero=[v for v in tag if v]
 if not nonzero:
  assert not value
  return value,tag,O
 common=nonzero[0]
 for v in nonzero[1:]:common=common.gcd(v)
 if int(common.total_degree())>0:
  value=exact(value,common)
  tag=[exact(v,common) if v else Z for v in tag]
 else:common=O
 original_return(value,tag)
 assert pure_ur(value)
 return value,tag,common
rows=[];rowtags=[];labels=[]
aa=[a[0] for a in affine];bb=[a[1] for a in affine];cc=[a[2] for a in affine]
tag=[aa[1]*bb[2]-aa[2]*bb[1],
     aa[2]*bb[0]-aa[0]*bb[2],
     aa[0]*bb[1]-aa[1]*bb[0],Z,Z,Z]
det=sum((tag[i]*cc[i] for i in range(3)),Z)
det,tag,removed=cancel_all(det,tag)
rows.append(det);rowtags.append(tag);labels.append('threeAffineMeans_fixed3')
say('new_ell_half_three_affine_fixed_scalar_return',
    scalar=profile(det),cancelledCommonActualMultipliers=profile(removed),
    noAffineHeadInverse=True,allRankDropFibersRetained=True)
pairs=[(0,1),(0,2),(1,2)]
# Fixed order: all N1 pairs, then all NS pairs, then all PS pairs.
for original_index in (3,4,5):
 P=J[original_index];degree=2 if original_index==3 else 3
 assert geomdegree(P)<=degree
 pc={(a,b):coeff(P,a,b) for a in range(degree+1) for b in range(degree+1-a)}
 assert sum((v*e**a*z**b for (a,b),v in pc.items()),Z)==P
 for i,j in pairs:
  head=aa[i]*bb[j]-aa[j]*bb[i]
  enum=bb[i]*cc[j]-bb[j]*cc[i]
  znum=aa[j]*cc[i]-aa[i]*cc[j]
  assert head*e-enum==bb[j]*J[i]-bb[i]*J[j]
  assert head*z-znum==-aa[j]*J[i]+aa[i]*J[j]
  stats['newHeadFreeReturns']+=2
  value=Z;ue=Z;uz=Z
  for (a,b),v in pc.items():
   if not v:continue
   hh=head**(degree-a-b)
   value+=v*hh*enum**a*znum**b
   if a:
    ue+=v*hh*(head*z)**b*sum(((head*e)**(a-1-k)*enum**k for k in range(a)),Z)
   if b:
    uz+=v*hh*enum**a*sum(((head*z)**(b-1-k)*znum**k for k in range(b)),Z)
  tag=[Z for _ in range(6)]
  tag[original_index]=head**degree
  tag[i]+=-bb[j]*ue+aa[j]*uz
  tag[j]+=bb[i]*ue-aa[i]*uz
  value,tag,removed=cancel_all(value,tag)
  rows.append(value);rowtags.append(tag);labels.append(['N1','NS','PS'][original_index-3]+'_'+str(i)+str(j))
  say('new_ell_half_original_head_free_value_return',
      originalName=['N1','NS','PS'][original_index-3],meanPair=[i,j],
      degreeUsed=degree,scalar=profile(value),
      cancelledCommonActualMultipliers=profile(removed),
      allSixSourceCoefficientsReturned=True,noHeadInverse=True,
      allAffineRankZeroAndOneFibersRetained=True)
assert len(rows)==10
# QQ(u) coefficients are for a NEW fixed univariate-r original Bezout target.
# They are never physical units unless their FINAL denominators are retained.
class K:
 def __init__(self,n=0,d=None):
  if isinstance(n,K):self.n=n.n;self.d=n.d;return
  n=n if isinstance(n,fmpq_poly) else fmpq_poly([n])
  d=fmpq_poly([1]) if d is None else (d if isinstance(d,fmpq_poly) else fmpq_poly([d]))
  assert d
  if not n:self.n=fmpq_poly();self.d=fmpq_poly([1]);return
  gg=n.gcd(d);n=n/gg;d=d/gg
  lc=d[d.degree()];self.n=n/lc;self.d=d/lc
 def __bool__(self):return bool(self.n)
 def __add__(self,v):
  v=K(v)
  gg=self.d.gcd(v.d);a=self.d/gg;b=v.d/gg
  return K(self.n*b+v.n*a,a*v.d)
 __radd__=__add__
 def __neg__(self):return K(-self.n,self.d)
 def __sub__(self,v):return self+-K(v)
 def __rsub__(self,v):return K(v)+-self
 def __mul__(self,v):
  v=K(v)
  if not self or not v:return K()
  gg=self.n.gcd(v.d);hh=v.n.gcd(self.d)
  return K((self.n/gg)*(v.n/hh),(self.d/hh)*(v.d/gg))
 __rmul__=__mul__
 def __truediv__(self,v):
  v=K(v);assert v
  return self*K(v.d,v.n)
 def __eq__(self,v):
  v=K(v);return self.n*v.d==v.n*self.d
def trim(p):
 p=list(p)
 while p and not p[-1]:p.pop()
 return p
def padd(a,b):
 return trim([(a[i] if i<len(a) else K())+(b[i] if i<len(b) else K()) for i in range(max(len(a),len(b)))])
def pneg(a):return [-v for v in a]
def psub(a,b):return padd(a,pneg(b))
def pscale(a,c):return trim([v*c for v in a])
def pmul(a,b):
 if not a or not b:return []
 out=[K() for _ in range(len(a)+len(b)-1)]
 for i,x in enumerate(a):
  for j,y in enumerate(b):out[i+j]+=x*y
 return trim(out)
def pdiv(a,b):
 assert b
 rr=trim(a);quot=[K() for _ in range(max(0,len(rr)-len(b)+1))]
 while len(rr)>=len(b):
  at=len(rr)-len(b);vv=rr[-1]/b[-1];quot[at]+=vv
  for j,co in enumerate(b):rr[at+j]-=vv*co
  rr=trim(rr)
 quot=trim(quot)
 assert padd(pmul(quot,b),rr)==trim(a)
 stats['newRBezoutReturns']+=1
 return quot,rr
def pxgcd(a,b):
 oldg,gg=trim(a),trim(b)
 olds,ss=[K(1)],[]
 oldt,tt=[],[K(1)]
 while gg:
  quo,rem=pdiv(oldg,gg)
  oldg,gg=gg,rem
  olds,ss=ss,psub(olds,pmul(quo,ss))
  oldt,tt=tt,psub(oldt,pmul(quo,tt))
 assert padd(pmul(olds,a),pmul(oldt,b))==oldg
 if not oldg:return [],[],[]
 lc=oldg[-1]
 oldg,olds,oldt=pscale(oldg,K(1)/lc),pscale(olds,K(1)/lc),pscale(oldt,K(1)/lc)
 assert padd(pmul(olds,a),pmul(oldt,b))==oldg
 stats['newRBezoutReturns']+=1
 return oldg,olds,oldt
def as_poly_r(p):
 assert pure_ur(p)
 dd=int(p.degrees()[1]) if p else -1
 out=[]
 for j in range(dd+1):
  entries={int(ex[0]):co for ex,co in p.to_dict().items() if int(ex[1])==j}
  high=max(entries,default=-1)
  out.append(K(fmpq_poly([entries.get(k,0) for k in range(high+1)])))
 return trim(out)
def from_u_poly(p):
 return ctx.from_dict({(j,0,0,0):p[j] for j in range(p.degree()+1) if p[j]})
def from_r_integral(p,den):
 out=Z
 for j,co in enumerate(p):
  qq,rr=divmod(den,co.d);assert not rr and qq*co.d==den
  np=co.n*qq
  out+=from_u_poly(np)*r**j
 return out
rp=[as_poly_r(p) for p in rows]
g=[];bez=[[] for _ in rows];used=[]
for j,pp in enumerate(rp):
 if not pp:continue
 if not g:
  lc=pp[-1];g=pscale(pp,K(1)/lc);bez[j]=[K(1)/lc]
 else:
  g,aa0,bb0=pxgcd(g,pp)
  bez=[pmul(aa0,vv) for vv in bez]
  bez[j]=padd(bez[j],bb0)
 used.append(j)
 back=[]
 for b0,p0 in zip(bez,rp):back=padd(back,pmul(b0,p0))
 assert back==g
 stats['newRBezoutReturns']+=1
 say('new_ell_half_blowup_fixed_original_r_gcd',
     inputIndex=j,inputLabel=labels[j],actualRdegree=len(g)-1,
     allTenOriginalScalarCoefficientsReturned=True,
     pureUDenominatorsNotDiscarded=True)
 if len(g)==1:break
def finish():
 say('new_ell_half_blowup_input_finished',
     sourceSHA256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
     statistics=stats,maxRssKiB=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss,
     noOldTwentyByEighteenZProofOrOldGcdReplayed=True,
     noCoefficientPayloadOrChunksWritten=True,ordinaryISPClaim=False)
 signal.setitimer(signal.ITIMER_REAL,0)
if len(g)!=1:
 say('new_ell_half_blowup_r_curve_retained',
     actualRdegree=len(g)-1,allOriginalC20ConstantFieldsRetained=True,
     noPureUCoverOrWholeExclusionClaim=True)
 finish()
else:
 assert g==[K(1)]
 denominator=fmpq_poly([1])
 for pp in bez:
  for vv in pp:
   denominator=denominator/denominator.gcd(vv.d)*vv.d
 multipliers=[from_r_integral(pp,denominator) for pp in bez]
 rhs=from_u_poly(denominator)
 assert sum((multipliers[i]*rows[i] for i in range(10)),Z)==rhs
 combined=[sum((multipliers[j]*rowtags[j][i] for j in range(10)),Z) for i in range(6)]
 assert sum((combined[i]*J[i] for i in range(6)),Z)==rhs
 # Return to tau,z; the r symbol below now labels the unblown tau coordinate.
 power=max([0]+[int(ex[1])-int(ex[3])+(1 if i<3 else 0)
       for i,pp in enumerate(combined) for ex in pp.to_dict()])
 def unblow(pp,i):
  data={}
  for ex,co in pp.to_dict().items():
   a,b,c,d=map(int,ex);zz=d-b+power-(1 if i<3 else 0)
   assert zz>=0
   key=(a,b,c,zz);data[key]=data.get(key,0)+co
  return ctx.from_dict(data)
 omega=[unblow(combined[i],i)*raw_original[i][1] for i in range(6)]
 # Only final SIX raw-original coefficients are used for cancellation.
 common=rhs
 for oo in omega:common=common.gcd(oo)
 if int(common.total_degree())>0:
  rhs=exact(rhs,common)
  omega=[exact(v,common) if v else Z for v in omega]
 assert rhs and pure_u(rhs)
 common_paid_den=O
 for _,dd in raw_original:
  common_paid_den=exact(common_paid_den,common_paid_den.gcd(dd))*dd
 back=sum((omega[i]*raw_original[i][0]*exact(common_paid_den,raw_original[i][1])
              for i in range(6)),Z)
 assert back==rhs*z**power*common_paid_den
 stats['newFinalRawPolynomialReturns']+=1
 cover,paid_part=remove_paid(rhs)
 lc=cover.coefficient(0);cover=exact(cover,ctx.constant(lc));paid_part*=lc
 assert cover*paid_part==rhs and pure_u(cover)
 rr,_=remove_paid(paid_part);assert rr and int(rr.total_degree())==0
 assert back==paid_part*cover*z**power*common_paid_den
 stats['newFinalRawPolynomialReturns']+=1
 say('new_ell_half_blowup_six_raw_original_positive_z_cover',
     usedScalarIndices=used,targetPositiveZpower=power,
     cancelledSixFinalOriginalCommon=profile(common),
     retainedCover=profile(cover),
     completeSixRawOriginalPolynomialReturned=True,
     exactClaim='Cnew(u)*z^N belongs to the six original raw equations over only OLD paid coefficients',
     allAffineRankDropsAndAllPureUZeroFibersRetained=True,
     onlyOldPaidFactorsRemoved=True,noNewGeometryInverse=True)
 OLD_C20_SHA='01e360b988892d68755864adae1520933535e6c79faf79bb667f1eec33eeb3cb'
 if int(cover.total_degree())==0:
  say('new_ell_half_blowup_whole_physical_branch_excluded',
      actualOldPaidPureUCover=True,noUseOfC20Coefficients=True)
 else:
  dd=int(cover.degrees()[0]);entries=cover.to_dict()
  cp=fmpq_poly([entries.get((j,0,0,0),0) for j in range(dd+1)])
  unit,factors=cp.factor();ret=fmpq_poly([unit]);small=[];matched=[]
  for fac,multiplicity in factors:
   ret*=fac**int(multiplicity)
   monic=fac/fac[fac.degree()]
   fp=from_u_poly(monic);pr=profile(fp)
   same=int(fac.degree())==20 and pr['sha256']==OLD_C20_SHA
   small.append({'monicFactor':pr,'multiplicity':int(multiplicity),
                 'matchesPublishedC20':same})
   if same:matched.append(fp)
  assert ret==cp
  say('new_ell_half_blowup_original_cover_complete_QQ_factors',
      factors=small,completeFactorProductReturned=True,
      publishedC20MonicProfile=OLD_C20_SHA,
      publishedC20IsQQIrreducibleOfDegree20=True,
      wholePhysicalEllHalfExcludedByC20AndNewCover=not bool(matched),
      allUnclosedC20FibersRetained=bool(matched),
      noOldC20CoefficientPayloadOrOldTargetGateRegenerated=True)
 finish()
