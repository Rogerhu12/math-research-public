#!/usr/bin/env python3
"""NEW original Phi highest D2=0 branch, without dividing by D2.
F6 and paid M,ell force ell=1/2,t=1. Substitute the whole weight
curve Q=4(u-1)(u-2) into the four ORIGINAL quadratic highest forms.
One QQ(u)[s] gcd with complete four-source Bezout products, then clear
all final denominators and retain every unpaid u factor. No old
three-rule head, Gaussian highest unit, P6/P9 or norm is executed.
60 seconds / 1 GiB. No coefficient cache, encoding, or split output.
"""
import json,time,hashlib,signal,resource,math,contextlib,io
from pathlib import Path
started=time.perf_counter();deadline=started+60
signal.alarm(60)
resource.setrlimit(resource.RLIMIT_AS,(1024**3,1024**3))
def say(stage,**kw):
 kw.update(stage=stage,seconds=time.perf_counter()-started)
 print(json.dumps(kw,separators=(',',':')),flush=True)
path=Path(__file__).with_name('2026-11-27-unit211-Phi-zero-first-quadratic-head-three-original-rows-D-input-8542.py')
raw=path.read_bytes()
assert hashlib.sha256(raw).hexdigest()=='100ce4dfb7380da1591cd453aae392e2dafcaaceb3a601c4500d07852841ecaf'
marker=b'\nquads=[extract_quad(p) for p in [Rbar,W4,Obar,N1]]\n'
assert raw.count(marker)==1
prefix=raw.split(marker)[0]
ns={'__file__':str(path),'__name__':'original_four_polynomials_only'}
oldalarm=signal.alarm
def bounded_alarm(seconds):
 left=max(.001,deadline-time.perf_counter())
 previous=signal.setitimer(signal.ITIMER_REAL,min(left,float(seconds) if seconds>0 else left))
 return math.ceil(previous[0])
signal.alarm=bounded_alarm
try:
 with contextlib.redirect_stdout(io.StringIO()):
  exec(compile(prefix,str(path)+'#before_any_head_or_row_reduction','exec'),ns)
finally:signal.alarm=oldalarm
signal.setitimer(signal.ITIMER_REAL,max(.001,deadline-time.perf_counter()))
ctx=ns['ctx'];R=ns['R'];up,Qp,Lp,Tp,sp=ctx.gens()
one=ctx.constant(1);zero=ctx.constant(0)
qcurve=4*(up-1)*(up-2);delta=one-qcurve
def prof(p):
 data=str(sorted(p.to_dict().items())).encode()
 return dict(degrees=list(map(int,p.degrees())),terms=len(p.to_dict()),
             bytes=len(data),sha256=hashlib.sha256(data).hexdigest())
def rprof(x):return dict(numerator=prof(x.n),denominator=prof(x.d))
def subweight(p):
 ans=zero
 for e,c in p.to_dict().items():
  assert e[2]==e[3]==e[4]==0
  ans+=c*up**int(e[0])*qcurve**int(e[1])
 return ans
paid=[('u',up),('u_minus_1',up-1),('u_minus_2_from_Q',up-2),('delta',delta)]
def strip_paid(p):
 rest=p;removed=one;hist=[]
 assert rest
 for label,atom in paid:
  count=0
  while True:
   g=rest.gcd(atom)
   if g.total_degree()==0:break
   new=rest/g
   assert new*g==rest
   rest=new;removed*=g;count+=1
  if count:hist.append(dict(unit=label,passes=count))
 assert removed*rest==p
 return rest,removed,hist
def legal_original_den(p):
 rest,removed,hist=strip_paid(p)
 assert rest.total_degree()==0
 return hist
def highest_on_curve(expr):
 assert all(e[2]==e[3]==e[4]==0 for e in expr.d.to_dict())
 den=subweight(expr.d);assert den
 legal_original_den(den)
 grades=[zero,zero,zero]
 for e,c in expr.n.to_dict().items():
  grade=int(e[2]+e[3]+e[4]);assert 0<=grade<=2
  grades[grade]+=c*up**int(e[0])*qcurve**int(e[1])*sp**int(e[4])
 # T=lambda, z=lambda*s: grades give the complete exact substitution.
 full=sum((R(p,den)*R(Lp)**j for j,p in enumerate(grades)),R())
 top=R(grades[2],den)
 assert full-R(Lp)**2*top==R(grades[0],den)+R(Lp)*R(grades[1],den)
 return top
original_names=['Rbar','W4','Obar','N1']
highest=[highest_on_curve(ns[name]) for name in original_names]
ell_on_curve=R(subweight(ns['ell'].n),subweight(ns['ell'].d))
M_on_curve=R(subweight(ns['M'].n),subweight(ns['M'].d))
assert ell_on_curve==R(1)/2 and M_on_curve==-2*R(up-1)**2
say('new_Phi_D2_zero_whole_weight_curve_original_highest_forms',
 originalNames=original_names,curve='Q=4*(u-1)*(u-2)',direction='t=1',
 ellHalfReturned=True,MEqualsMinusTwoUMinusOneSquaredReturned=True,
 allFourFullOriginalDegreeDecompositionsReturned=True,
 originalDenominatorsOnlyPaidOnWholeCurve=True,
 highestForms=[rprof(p) for p in highest],
 noOriginalQuadraticHeadOrOldHighestGaussianExecuted=True,
 D2InverseNeverUsed=True,wholePhiExcluded=False)
def trim(a):
 a=list(a)
 while a and not a[-1]:a.pop()
 return a
def padd(a,b):
 return trim([(a[i] if i<len(a) else R())+(b[i] if i<len(b) else R()) for i in range(max(len(a),len(b)))])
def pneg(a):return [-x for x in a]
def psub(a,b):return padd(a,pneg(b))
def pmul(a,b):
 if not a or not b:return []
 out=[R() for _ in range(len(a)+len(b)-1)]
 for i,x in enumerate(a):
  for j,y in enumerate(b):out[i+j]=out[i+j]+x*y
 return trim(out)
def pscale(a,c):return trim([x*c for x in a])
def peq(a,b):
 a=trim(a);b=trim(b)
 return len(a)==len(b) and all(x==y for x,y in zip(a,b))
def pdiv(a,b):
 assert b
 q=[R() for _ in range(max(0,len(a)-len(b)+1))]
 r=list(a)
 while r and len(r)>=len(b):
  j=len(r)-len(b);c=r[-1]/b[-1];q[j]=q[j]+c
  r=psub(r,[R()]*j+pscale(b,c))
 assert peq(a,padd(pmul(q,b),r))
 return trim(q),r
def pgcd(a,b):
 r0,r1=a,b;s0,s1=[R(1)],[];t0,t1=[],[R(1)]
 while r1:
  q,r=pdiv(r0,r1)
  r0,r1=r1,r;s0,s1=s1,psub(s0,pmul(q,s1));t0,t1=t1,psub(t0,pmul(q,t1))
 if not r0:return [],[],[]
 lead=1/r0[-1]
 g,aa,bb=pscale(r0,lead),pscale(s0,lead),pscale(t0,lead)
 assert peq(g,padd(pmul(aa,a),pmul(bb,b)))
 return g,aa,bb
def coeffs(p):
 assert all(e[2]==e[3]==e[4]==0 for e in p.d.to_dict())
 out=[zero for _ in range(max(0,int(p.n.degrees()[4]))+1)]
 for e,c in p.n.to_dict().items():
  assert e[1]==e[2]==e[3]==0
  out[int(e[4])]+=c*up**int(e[0])
 rr=trim([R(v,p.d) for v in out])
 assert sum((c*R(sp)**j for j,c in enumerate(rr)),R())==p
 return rr
rows=[coeffs(p) for p in highest]
g=rows[0];tags=[[R(1)],[],[],[]]
for i in range(1,4):
 gnew,a,b=pgcd(g,rows[i])
 tags=[pmul(a,t) for t in tags]
 tags[i]=padd(tags[i],b);g=gnew
 check=[]
 for tag,row in zip(tags,rows):check=padd(check,pmul(tag,row))
 assert peq(check,g)
 say('new_original_highest_curve_four_source_gcd_step',
     includedOriginals=original_names[:i+1],gcdSDegree=len(g)-1,
     allFourSourcePolynomialProductsReturned=True)
if len(g)!=1:
 say('new_original_highest_curve_nonconstant_gcd_retained',
     gcdSDegree=len(g)-1,wholeGenericDirectionNotExcluded=True,
     gcdCoefficients=[rprof(v) for v in g],wholePhiExcluded=False)
else:
 assert g[0]==1
 C=one
 for tag in tags:
  for co in tag:
   assert all(e[1]==e[2]==e[3]==e[4]==0 for e in co.d.to_dict())
   C*=co.d/C.gcd(co.d)
 beta=[[co.n*(C/co.d) for co in tag] for tag in tags]
 check=[]
 for tag,row in zip(beta,rows):check=padd(check,pmul([R(v) for v in tag],row))
 assert peq(check,[R(C)])
 rest,unit,removed=strip_paid(C)
 scalar=rest.coefficient(0);rest=rest/scalar;unit*=scalar
 assert unit*rest==C
 fact_scalar,factors=rest.factor()
 product=ctx.constant(fact_scalar)
 for factor,multiplicity in factors:product*=factor**int(multiplicity)
 assert product==rest
 distinct_degree=sum(int(p.degrees()[0]) for p,m in factors)
 say('new_original_highest_curve_exact_C_return_and_complete_support',
     identity='C(u)=sum_i beta_i(u,s)*top2(original_i)(u,Qcurve,1,1,s)',
     allFourOriginalSourceCoefficientProductsReturned=True,
     actualClearedC=prof(C),removedOnlyPaidFactors=removed,
     retainedCompleteUSupport=prof(rest),
     factorProductReturned=True,
     factors=[dict(definition=prof(p),multiplicity=int(m)) for p,m in factors],
     maximumDistinctExceptionalUValues=distinct_degree,
     entireD2ZeroHighestOriginalPointBranchExcluded=(rest.total_degree()==0),
     unpaidExceptionalUFibresRetained=(rest.total_degree()!=0),
     fullOriginalAffinePointCountNotClaimed=True,
     wholePhiExcluded=False)
say('new_original_Phi_D2_zero_direction_source_finished',
 sourceSHA256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
 necessaryOriginalDefinitionPrefixBytes=len(prefix),
 necessaryOriginalDefinitionPrefixSHA256=hashlib.sha256(prefix).hexdigest(),
 noOldHeadGaussianP6P9NormOrFullModuleReplayed=True,
 noCoefficientPayloadEncodedOrSplitSaved=True,
 peakRSSKiB=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss,
 wholePhiExcluded=False,ordinaryISPClaim=False)
signal.setitimer(signal.ITIMER_REAL,0);signal.alarm(0)
