#!/usr/bin/env python3
"""Current W, lambda=3/2: new same-value ratio R2/H6 fixed 8-column cover.
Both original second/third moments and Delta use the same v0,s.
The ratio chart is whole physical lambda=3/2 since Sval=2v0 and s are units.
Full eight-column original cofactor identity; only paid weight factors removed.
180 seconds / 4 GiB. No old qT/rT six-column cover is recomputed.
"""
import json,time,hashlib,signal,resource
from pathlib import Path
from flint import fmpq_mpoly_ctx
start=time.perf_counter();signal.alarm(180)
resource.setrlimit(resource.RLIMIT_AS,(4*1024**3,4*1024**3))
def say(**r):
 r['seconds']=time.perf_counter()-start;print(json.dumps(r),flush=True)
ctx=fmpq_mpoly_ctx.get(('e','k'),'lex');e,k=ctx.gens()
zero=ctx.constant(0);one=ctx.constant(1)
u=e+1;Q=e*k;d=1-Q;V=u*k+2
Lh=(k+2)**2-2*e*k;mh=(k+2)*(Q-2);Jh=k+2-4*e
Ah=4*V-Jh
M13=4*e**3*k*k-3*e*e*k**3-12*e*e*k*k-16*e*e*k+e*k**4+8*e*k**3+24*e*k*k+32*e*k+16*e-k**3-8*k*k-20*k-16
Pp=2*e*k-k*k-5*k-8
def trim(a):
 while a and not a[-1]:a.pop()
 return a
def add(a,b):
 c=[zero for _ in range(max(len(a),len(b)))]
 for i,v in enumerate(a):c[i]+=v
 for i,v in enumerate(b):c[i]+=v
 return trim(c)
def scale(a,c):return trim([v*c for v in a])
def mul(a,b):
 if not a or not b:return []
 c=[zero for _ in range(len(a)+len(b)-1)]
 for i,v in enumerate(a):
  for j,w in enumerate(b):c[i+j]+=v*w
 return trim(c)
def power(a,n):
 out=[one]
 for _ in range(n):out=mul(out,a)
 return out
U=[Ah,zero,Jh*d]
P2h=[Lh,-2*mh,Lh*d]
P3h=[Lh,-3*mh,3*Lh*d,-mh*d]
R=add(scale(P2h,6),scale(U,-5*k))
expected=[-(20*e+9)*k*k-(32*e+6)*k+24,-12*(k+2)*(e*k-2),
 d*(k*k+(8*e+14)*k+24)]
assert R==expected and len(R)==3
H=add(scale(power(U,3),49*u*k*k),scale(power(P3h,2),-108*V))
assert len(H)==7
# At a physical point: R=0 and H=0 by the already published exact same-value
# moment/Delta combinations; neither Az nor P3 nor z is separately inverted here.
mat=[]
for j in range(6):mat.append([zero]*j+R+[zero]*(5-j))
for j in range(2):mat.append([zero]*j+H+[zero]*(1-j))
assert len(mat)==8 and all(len(row)==8 for row in mat)
def det(mat):
 a=[row[:] for row in mat];n=len(a);prev=one;sgn=1
 if n==0:return one
 for j in range(n-1):
  h=next((i for i in range(j,n) if a[i][j]),None)
  if h is None:return zero
  if h!=j:a[h],a[j]=a[j],a[h];sgn=-sgn
  pivot=a[j][j]
  for i in range(j+1,n):
   for c in range(j+1,n):
    num=pivot*a[i][c]-a[i][j]*a[j][c]
    nxt=num/prev;assert nxt*prev==num;a[i][c]=nxt
   a[i][j]=zero
  prev=pivot
 return a[-1][-1]*sgn
res=det(mat);assert res
cof=[]
for i in range(8):
 minor=[[mat[j][c] for c in range(1,8)] for j in range(8) if j!=i]
 cof.append(det(minor)*((-1)**i))
assert all(sum((cof[i]*mat[i][j] for i in range(8)),zero)==(res if j==0 else zero) for j in range(8))
atoms=[e,k,u,Q,d,V,Lh,Q-2,M13,Pp,2*e+1,k+1,k+2,k+4]
names=['e','k','u','Q','d','V','ell_numerator','Q-2','M_numerator','P02_numerator','2e+1','k+1','k+2','k+4']
remaining=res;removed=one;paid=[]
for name,ap in zip(names,atoms):
 count=0;deg=0
 while True:
  g=remaining.gcd(ap)
  if g.total_degree()==0:break
  nxt=remaining/g;assert nxt*g==remaining
  removed*=g;remaining=nxt;count+=1;deg+=int(g.total_degree())
 if count:paid.append(dict(atom=name,passes=count,totalDegreeRemoved=deg))
lc=remaining.coefficient(0);remaining=remaining/lc;removed*=lc
assert res==removed*remaining
def prof(p,include=True):
 dd=[[list(map(int,mm)),str(cc)] for mm,cc in sorted(p.to_dict().items())]
 bb=json.dumps(dd,separators=(',',':')).encode()
 r=dict(degrees=list(map(int,p.degrees())),totalDegree=int(p.total_degree()),terms=len(dd),
 bytes=len(bb),sha256=hashlib.sha256(bb).hexdigest())
 if include and len(bb)<=8192:r['coefficients']=dd
 return r
content,factors=remaining.factor();product=ctx.constant(content);fs=[]
for f,m in factors:
 product*=f**m
 fs.append(dict(multiplicity=int(m),factor=prof(f),
 matchesPreviousCompleteF18CanonicalSHA256=prof(f,False)['sha256']=='b40c388d98930dd5196694c7accbd23a1670268aeaf7449b842f060e8acc6bee'))
assert product==remaining
say(stage='W_lambda_three_halves_same_value_R2_H6_original_cover_complete',
 inputDegreesZ=[2,6],fixedMatrixShape=[8,8],
 allEightOriginalConstantCofactorColumnsActuallyVerified=True,
 fullFixedDegreeAndAllLeadingZeroFibersRetained=True,
 sameV0SOriginalMomentDeltaInput=True,
 noUseOfOldSixColumnCoverAsNewInput=True,
 rawResultant=prof(res,False),paidFactorsRemoved=paid,
 remainingNecessaryWeightPolynomial=prof(remaining),
 completeQQFactorization=fs,
 originalCofactorProfiles=[prof(c,False) for c in cof],
 noUnpaidFactorRemoved=True,noNormInverse=True,noAhatPaymentUsed=True,
 wholeLambdaFiberExcluded=False,largeCachesWritten=False,
 sourceSHA256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
 peakRssKiB=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)
signal.alarm(0)
