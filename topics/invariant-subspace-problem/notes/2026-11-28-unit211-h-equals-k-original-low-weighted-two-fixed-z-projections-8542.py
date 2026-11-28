#!/usr/bin/env python3
"""NEW h=k: original low weighted difference against two mean rows.
Rebuild only bb534 same-Gram definition prefix, not individual N/P or
old NV scalar/cofactor/factorization tails. Entire Delta=0 retained.
180 seconds / 4 GiB; one absolute deadline; summaries only.
"""
import json,time,hashlib,signal,resource,contextlib,io,math
from pathlib import Path
START=time.perf_counter();DEADLINE=START+180
signal.setitimer(signal.ITIMER_REAL,180)
resource.setrlimit(resource.RLIMIT_AS,(4*1024**3,4*1024**3))
def say(stage,**kw):
 kw.update(stage=stage,seconds=time.perf_counter()-START)
 print(json.dumps(kw,separators=(',',':')),flush=True)
path=Path(__file__).with_name('2026-11-28-unit211-h-equals-k-corrected-individual-NP-NV-scalar-returns-8542.py')
raw=path.read_bytes()
assert hashlib.sha256(raw).hexdigest()=='00d513d603f862ef6b484176fe4d9da3b766e0047d46a87ec8f575622aa8ca14'
marker=b'\nNerrB='
assert raw.count(marker)==1
prefix=raw.split(marker)[0]
assert len(prefix)==5116 and hashlib.sha256(prefix).hexdigest()=='eba270645031173eb0fd2c0908a4fb72cda25ce662a4140fb47289ad1b07e192'
env={'__file__':str(path),'__name__':'new_hk_low_weighted_not_old_NV_targets'}
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
  exec(compile(prefix,str(path)+'#necessary_same_Gram_only','exec'),env)
finally:
 signal.alarm=old_alarm;signal.setitimer=old_timer
 old_timer(signal.ITIMER_REAL,max(.001,DEADLINE-time.perf_counter()))
R,U,E,ctx=[env[k] for k in ['R','U','E','ctx']]
lam,u,Q,disc,A,B,ell,T,w,hh=[env[k] for k in ['lam','u','Q','disc','A','B','ell','T','w','hh']]
P02,Pf,bc,M,z,f,t,xx,yy=[env[k] for k in ['P02','Pf','bc','M','z','f','t','xx','yy']]
bb,cc,p,q,X,Y=[env[k] for k in ['bb','cc','p','q','X','Y']]
mean,N4,P2,rows=[env[k] for k in ['mean','N4','P2','rows']]
zeroP=ctx.constant(0);oneP=ctx.constant(1)
EB=mean(2);EC=mean(3)
assert EC==EB.conj()
E1=mean(1)
assert not E1.y
EW2=bb*(2*p-E(u)-X)*EB+cc*(2*q-E(u)-Y)*EC
assert not EW2.y
NS=bb*N4(rows[2])+cc*N4(rows[3])-E(2*lam*P02*ell*hh*hh)
PS=bb*P2(rows[2])+cc*P2(rows[3])-E(P02*ell*hh**3)
assert not NS.y and not PS.y
Kw=2*(t*t+(5*u-4*xx-2)*t+2*(xx*xx-disc*yy*yy)
      +4*xx+4*disc*yy-4*u*xx+2*u*u-6*u+Q)
Loww=2*P02*(2*lam-1)*w-bc*t*(Kw+4*(f-u)*(t-2))
assert E(Loww)==NS-PS+EW2
newrows=[('E1',E1.x),('EBo',EB.y),('Loww',Loww)]
assert all(0<=len(v.c)-1<=3 for _,v in newrows)
say('new_hk_complete_original_low_weighted_input',
 trueOriginalSamePointIdentity='Loww=NS-PS+EW2',
 originalFreeFCorrection='Kw+4*(f-u)*(t-2)',
 noFalseQuadraticAssumption=True,
 originalZDegrees={name:len(v.c)-1 for name,v in newrows},
 noNVOrDeltaInverse=True,noOldIndividualNVScalarOrFiveRowCofactorReplayed=True)
# Existing original p=1 S0/h=k proof and true dual Af=0/lambda-half
# dependencies were statically reread, never reexecuted.
S=2*env['xi']+3-2*lam
assert S==(2*lam-1)*(2*lam*lam-1)/A
atoms=[('A',A.n),('B',B.n),('Q',Q.n),('1-Q',disc.n),
 ('Pf_coordinate',Pf.n),('M_equals_4bc_delta',M.n),
 ('P02_original',P02.n),('lambda_original_mean',lam.n),
 ('lambda_half_original_rank',(2*lam-1).n),
 ('S_zero_old_original_collision_exclusion',S.n)]
exact_products=0
def dex(a,b):
 global exact_products
 q0,r0=divmod(a,b);assert not r0 and q0*b==a
 exact_products+=1;return q0
def strip(p):
 original=p;removed=oneP;history=[]
 if not p:return p,removed,history
 for name,atom in atoms:
  count=0
  while True:
   g=p.gcd(atom)
   if int(g.total_degree())<=0:break
   p=dex(p,g);removed*=g;count+=1
  if count:history.append([name,count])
 assert p*removed==original
 return p,removed,history
def paid(d):
 p,_,hist=strip(d)
 assert p and int(p.total_degree())==0
 return hist
def info(p):
 if not p:return dict(zero=True,degrees_lambda_u_Q=[-1,-1,-1],terms=0)
 data=[[list(map(int,mm)),str(c)] for mm,c in sorted(p.to_dict().items())]
 raw0=json.dumps(data,separators=(',',':')).encode()
 return dict(zero=False,degrees_lambda_u_Q=list(map(int,p.degrees())),
  totalDegree=int(p.total_degree()),terms=len(data),bytes=len(raw0),
  sha256=hashlib.sha256(raw0).hexdigest())
def clear(name,v):
 den=oneP
 for r in v.c:
  paid(r.d);den=dex(den,den.gcd(r.d))*r.d
 paid(den)
 coeff=[r.n*dex(den,r.d) for r in v.c]
 content=zeroP
 for c0 in coeff:content=content.gcd(c0)
 _,removed,hist=strip(content)
 coeff=[dex(c0,removed) for c0 in coeff]
 norm=next(c0 for c0 in coeff if c0).coefficient(0)
 coeff=[c0/norm for c0 in coeff];removed*=norm
 assert U([R(c0*removed,den) for c0 in coeff])==v
 say('new_hk_original_low_row_clearing',name=name,
  zDegree=len(coeff)-1,coefficientProfiles=[info(c0) for c0 in coeff],
  onlyPaidContentRemoved=hist,completeOriginalRowReturned=True)
 return coeff
cleared={name:clear(name,v) for name,v in newrows}
def fixed_sylvester(f0,g0):
 m0=len(f0)-1;n0=len(g0)-1
 assert m0>=1 and n0>=1
 size=m0+n0;mat=[]
 for j in range(n0):mat.append([zeroP]*j+f0[::-1]+[zeroP]*(n0-1-j))
 for j in range(m0):mat.append([zeroP]*j+g0[::-1]+[zeroP]*(m0-1-j))
 assert all(len(row)==size for row in mat)
 return mat
def bareiss(mat):
 a=[row[:] for row in mat];n=len(a);old=oneP;sign=1
 for k in range(n-1):
  pivot=next((i for i in range(k,n) if a[i][k]),None)
  if pivot is None:return zeroP
  if pivot!=k:a[k],a[pivot]=a[pivot],a[k];sign=-sign
  p=a[k][k]
  for i in range(k+1,n):
   for j in range(k+1,n):
    a[i][j]=dex(p*a[i][j]-a[i][k]*a[k][j],old)
   a[i][k]=zeroP
  old=p
 return sign*a[-1][-1]
records=[]
for anchor in ['E1','EBo']:
 left=cleared[anchor];right=cleared['Loww']
 matrix=fixed_sylvester(left,right);det=bareiss(matrix)
 core,removed,hist=strip(det)
 if core:
  norm=core.coefficient(0);core/=norm;removed*=norm
 assert core*removed==det
 rec=dict(anchor=anchor,other='Loww',
  fixedZDegrees=[len(left)-1,len(right)-1],
  fixedSylvesterSize=len(matrix),originalResultant=info(det),
  necessaryCore=info(core),onlyOriginalPaidRemoval=hist,
  allBareissDivisionProductsReturned=True,
  everySpecializedZLeadingZeroFiberKept=True,
  noNVOrDeltaInverse=True,sameFiniteZRootNecessary=True)
 records.append(rec);say('new_hk_original_low_weighted_fixed_projection',**rec)
say('new_hk_original_low_weighted_two_fixed_projections_finished',
 sourceSHA256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
 actualPolynomialDivisionProducts=exact_products,
 nonzeroNewNecessaryConditions=sum(not r['necessaryCore']['zero'] for r in records),
 wholeCollisionExcluded=any(not r['necessaryCore']['zero'] and r['necessaryCore']['totalDegree']==0 for r in records),
 noUnknownParameterHeadInverted=True,noPhysicalDInverse=True,
 noFiniteOrEmptyClaimWithoutReturnedUnit=True,originalDeltaZeroStillIncluded=True,
 noOldFrozenOrCompletedProjectionReplayed=True,
 peakRSSKiB=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss,
 ordinaryISPClaim=False)
