#!/usr/bin/env python3
"""NEW true Phi f=u after the whole u=3/2 exclusion.
One original coordinate y=A+2*L*lambda, all raw Gram values, and new fixed
3/4-column original scalar cofactors.  No former GB, old heads, or old
cofactors are executed.  120 seconds / 1 GiB, small output only.
"""
import hashlib,itertools,json,math,os,pathlib,resource,signal,time
START=time.perf_counter();DEADLINE=START+120
resource.setrlimit(resource.RLIMIT_AS,(1024**3,1024**3))
_RAW_ALARM=signal.alarm
def bounded_alarm(seconds):
 if seconds<=0:return _RAW_ALARM(0)
 if time.perf_counter()>=DEADLINE:raise TimeoutError('absolute 120 second boundary')
 return _RAW_ALARM(max(1,min(int(seconds),math.ceil(DEADLINE-time.perf_counter()))))
signal.alarm=bounded_alarm;signal.alarm(120)
BASENAME='2026-11-28-unit211-Phi-zero-corrected-dual-germ-four-original-quadratic-heads-8542.py'
BASE_SHA='5ee86ff89db7c8babaf3a22c7d72570dcdfbbf92646f56adf37bff854a87ace7'
path=pathlib.Path(__file__).with_name(BASENAME)
if not path.exists():path=pathlib.Path(os.environ.get('ISP_INPUT_DIR',''))/BASENAME
full=path.read_text();assert hashlib.sha256(full.encode()).hexdigest()==BASE_SHA
MARKER='u,Q,lam,Tr=map(R,(up,Qp,Lp,Tp))';assert full.count(MARKER)==1
prefix=full[:full.index(MARKER)]
ns={'__name__':'isp_true_fu_y_arithmetic_only','__file__':str(path)}
exec(compile(prefix,str(path),'exec'),ns)
signal.alarm=bounded_alarm;signal.alarm(120)
R=ns['R'];ctx=ns['ctx'];up,Qp,yp,Tp,zp=ctx.gens()
zeroP=ctx.constant(0);oneP=ctx.constant(1)
u,Q,y=map(R,(up,Qp,yp));ss=u-1;hh=2*u-3
delta=1-Q;L=Q-2*ss*(u-2);K=Q+4*ss;A=4*ss*ss-Q
ell=L/Q;aw=1-ell;theta=u-L;mm=u-ell
Mn=2*u*L-L*L-u*u*Q;M=Mn/Q;bc=Mn/(4*Q*delta)
T0=-K;P02=2*ss*L;Pf=4*ss*ss*K
lam=(y-A)/(2*L);ff=u
tt=2*delta*(2*theta*y+L*A)/(Mn*hh)
A1=2*ss*y/Q
T=-L/Q-K*y/(2*Q*L);w=lam-1-T
V=u-ss*y/Q+bc*tt;W=(4*u*u-K)/2
xm=(theta*V-mm*W)/M;ym=(ell*W-u*V)/M
z=Q*tt;vn=Q*V;nn=Q*(T0+4*u*u)-2*vn
paid=Qp*(1-Qp)*(up-1)*(Qp+4*up-4)*(Qp-2*(up-1)*(up-2))
paid*=2*up*(Qp-2*(up-1)*(up-2))-(Qp-2*(up-1)*(up-2))**2-up*up*Qp
paid*=2*up-3
def say(stage,**kw):
 kw.update(stage=stage,seconds=time.perf_counter()-START)
 print(json.dumps(kw,sort_keys=True),flush=True)
def weight(p):return all(e[2]==e[3]==e[4]==0 for e in p.to_dict())
def info(p):
 out={'degrees':list(map(int,p.degrees())) if p else [-1]*5,
      'terms':len(p.to_dict()),
      'sha256':hashlib.sha256(str(sorted(p.to_dict().items())).encode()).hexdigest()}
 if p and len(p.to_dict())<=36:out['polynomial']=str(p)
 return out
divisions=0
def exact(a,b):
 global divisions
 q,r=divmod(a,b);assert not r and q*b==a
 divisions+=1;return q
def supported(p):
 assert weight(p)
 r=p
 while r and int(r.total_degree())>0:
  g=r.gcd(paid)
  if int(g.total_degree())<=0:return False
  r=exact(r,g)
 return bool(r)
checks=0
def ck(a):
 global checks
 if isinstance(a,list):assert all(not b for b in a)
 else:assert not a
 checks+=1
assert supported(lam.d) and supported(tt.d) and supported(T.d)
Rtrue=bc*z*z+z*(4*bc*u*Q-ell*vn)+(mm/(2*delta))*z*nn
ck(Rtrue)
# Complete identity before the t substitution: its numerator is linear in t.
tfree=R(zp);vfree=u*Q-ss*y+bc*Q*tfree
nfree=Q*(T0+4*u*u)-2*vfree;zfree=Q*tfree
Rfree=bc*zfree*zfree+zfree*(4*bc*u*Q-ell*vfree)+(mm/(2*delta))*zfree*nfree
ck(Rfree-zfree*(ss/delta)*(-bc*hh*zfree+theta*y+L*A/2))
ck(A1-(2*u-2*V+2*bc*tt))
G=lam*P02+(u-1)*T0
ck(Pf*ff+Q*P02*(ell+T)-G*T0)
say('new_true_fu_single_y_recovery_defined',fullCorrectedRLinearIdentityReturned=True,originalP1Returned=True,onlyNewHeadUnit='2u-3, exclusively on f=u after its whole fiber exclusion',noOldAOrBOrSlopeUnitUsed=True)
def q(v=0,w0=0):return [R(v),R(w0)]
def qa(a,b):return [a[0]+b[0],a[1]+b[1]]
def qn(a):return [-a[0],-a[1]]
def qs(a,b):return qa(a,qn(b))
def qm(a,b):return [a[0]*b[0]+delta*a[1]*b[1],a[0]*b[1]+a[1]*b[0]]
def qc(a,n):return [n*a[0],n*a[1]]
def conj(a):return [a[0],-a[1]]
def qsum(*xs):
 out=q()
 for a in xs:out=qa(out,a)
 return out
b=q(ell/2,mm/(2*delta));c=conj(b)
p=q(1,1);qq=conj(p);unit=[q(1),q(),q(1),q(1)]
X=q(xm,ym);Y=conj(X)
rr=qs(qs(X,qc(p,aw)),qc(c,tt));cc=conj(rr)
rows=[[q(),q(),p,qq],[q(),q(A1),rr,cc],[p,rr,q(),q(tt)],[qq,cc,q(tt),q()]]
def vm(a,b):
 return [qm(a[0],b[0]),qa(qm(a[0],b[1]),qm(a[1],b[0])),qm(a[2],b[2]),qm(a[3],b[3])]
def va(a,b):return [qa(v,z0) for v,z0 in zip(a,b)]
def vs(a,v):return [qm(a,z0) for z0 in v]
def tau(v):return qsum(qc(v[0],aw),v[1],qm(b,v[2]),qm(c,v[3]))
def DK(v):return [tau(vm(row,v)) for row in rows]
dv=DK(unit);F2=tau(dv);Kd=DK(dv);d2=vm(dv,dv)
def pure(a):ck(a[1]);return a[0]
def mean(j):
 vv=qc(tau(vm(rows[0],rows[1])),2) if j==1 else tau(vm(rows[j],rows[j]))
 return qsum(vv,qc(Kd[j],-2),qc(d2[j],-2),qc(qm(F2,dv[j]),2))
def centered(v):return va(v,vs(qn(tau(v)),unit))
def P2(v):
 zz=centered(v);return tau(vm(vm(zz,zz),zz))
def N4(v):
 tv=tau(v);vv=vm(v,v)
 return qsum(qc(tau(vm(dv,vv)),2),qn(qm(F2,tau(vv))),
             qc(qm(tv,tau(vm(dv,v))),-4),qc(qm(F2,qm(tv,tv)),2),tau(vm(v,DK(v))))
ck(qs(qm(b,c),q(bc)));ck(qs(qsum(qm(b,p),qm(c,qq)),q(u)))
ck(mean(0));ck(qs(F2,q(2*u)));ck(qs(P2(rows[0]),q(P02)))
N0=N4(rows[0]);ck(qs(N0,q(2*lam*P02)))
Pj=qc(tau(vm(vm(centered(rows[0]),centered(rows[0])),centered(rows[1]))),3)
ck(qs(Pj,q(3*w*P02)))
EB=mean(2);EC=mean(3);ck(qs(EC,conj(EB)))
ck(qs(mean(1),qsum(qm(b,EB),qm(c,EC))))
Nj=qs(qs(N4(va(rows[0],rows[1])),N0),N4(rows[1]))
N1=pure(qs(Nj,q(4*lam*w*P02)))
A2=2*lam*lam-2*lam+1;B3=4*lam**3-6*lam*lam+3*lam-1
NS=pure(qs(qsum(qm(b,N4(rows[2])),qm(c,N4(rows[3]))),q(2*lam*P02*(ell+2*T+A2))))
PS=pure(qs(qsum(qm(b,P2(rows[2])),qm(c,P2(rows[3]))),q(P02*(ell+3*T+3*A2+B3))))
original=[EB[0],EB[1],N1,NS,PS];names=['EBe','EBo','N1','NS','PS']
def degree_y(p):return max((int(e[2]) for e in p.to_dict()),default=-1)
def coef(p,i):
 assert all(e[3]==e[4]==0 for e in p.to_dict())
 return ctx.from_dict({(e[0],e[1],0,0,0):a for e,a in p.to_dict().items() if int(e[2])==i})
def strip_paid(p):
 assert weight(p);removed=oneP;rem=p
 while rem and int(rem.total_degree())>0:
  g=rem.gcd(paid)
  if int(g.total_degree())<=0:break
  rem=exact(rem,g);removed*=g
 assert removed*rem==p
 return rem,removed
prepared=[];input_scales=[]
for i,value in enumerate(original):
 assert supported(value.d)
 content=zeroP
 for j in range(degree_y(value.n)+1):content=content.gcd(coef(value.n,j))
 rest,removed=strip_paid(content)
 pp=exact(value.n,removed)
 assert R(pp)*R(removed,value.d)==value
 assert degree_y(pp)<= (2 if i<3 else 3)
 prepared.append(pp);input_scales.append(R(removed,value.d))
say('new_true_fu_single_y_original_values',
 actualCoordinate='y=4*(u-1)^2-Q+2*ell*Q*lambda',
 fullCorrectedRLinearIdentityReturned=True,
 originalE0N0P1AndGermMinusWeightedMeansReturned=True,
 allFiveRawOriginalRowsReturned=True,
 rowYDegrees=[degree_y(p0) for p0 in prepared],
 rowProfiles=[info(p0) for p0 in prepared],
 everyCoefficientDenominatorOnlyIntrinsicAndFuHalfHead=True,
 noOldAOrBOrSlopeUnitUsed=True,noDInverse=True,
 originalChecks=checks,exactDivisions=divisions)
def det(a):
 n=len(a)
 if n==0:return oneP
 if n==1:return a[0][0]
 return sum(((-1)**j*a[0][j]*det([r[:j]+r[j+1:] for r in a[1:]]) for j in range(n)),zeroP)
targets=[]
specs=[[(0,0),(1,0),(2,0)],
       [(0,0),(0,1),(1,0),(3,0)],
       [(0,0),(0,1),(1,0),(4,0)]]
for si,spec in enumerate(specs):
 polys=[yp**j*prepared[i] for i,j in spec];size=len(polys)
 assert all(degree_y(p0)<size for p0 in polys)
 matrix=[[coef(p0,j) for j in range(size)] for p0 in polys]
 # First row of adjugate: (adj M)[0,i], not a leading-head inverse.
 cof=[(-1)**i*det([[matrix[r][c0] for c0 in range(1,size)] for r in range(size) if r!=i]) for i in range(size)]
 value=sum((cof[i]*matrix[i][0] for i in range(size)),zeroP)
 assert value==det(matrix)
 combo=[zeroP for _ in prepared]
 for (i,j),v in zip(spec,cof):combo[i]+=v*yp**j
 assert sum((combo[i]*prepared[i] for i in range(5)),zeroP)==value
 if not value:
  say('new_true_fu_fixed_original_scalar_zero',spec=spec,size=size,
      fullOriginalCombinationReturned=True)
  continue
 g=zeroP
 for v in combo:g=g.gcd(v)
 assert g and weight(g)
 new_combo=[exact(v,g) for v in combo];value=exact(value,g)
 assert sum((new_combo[i]*prepared[i] for i in range(5)),zeroP)==value
 retained,paidpart=strip_paid(value)
 original_multipliers=[R(new_combo[i],paidpart)/input_scales[i] for i in range(5)]
 assert all(supported(v.d) for v in original_multipliers)
 assert sum((original_multipliers[i]*original[i] for i in range(5)),R())==R(retained)
 targets.append(retained)
 say('new_true_fu_original_scalar_cofactor',spec=spec,size=size,
     allActualOriginalMultipliersCommonContentRemoved=info(g),
     retainedNecessaryWeightPolynomial=info(retained),
     wholeOriginalFiveTermCombinationReturned=True,
     onlyPaidFactorsRemovedFromFinalTarget=True,
     noLeadingHeadInverted=True,
     wholeFuExcluded=int(retained.total_degree())==0)
 if int(retained.total_degree())==0:break
pairs=[]
for i,j in itertools.combinations(range(len(targets)),2):
 g=targets[i].gcd(targets[j])
 exact(targets[i],g);exact(targets[j],g)
 pairs.append({'targets':[i,j],'exactQQGCD':info(g),
               'finiteWeightSupportProved':int(g.total_degree())==0,
               'BezoutDifferentWeightPointUpperBound':int(targets[i].total_degree())*int(targets[j].total_degree()) if int(g.total_degree())==0 else None})
say('new_true_fu_single_y_new_scalar_interfaces_complete',
 originalChecks=checks,exactDivisions=divisions,
 numberOfNonzeroOriginalScalarTargets=len(targets),
 actualPairGCDs=pairs,
 wholeFuExcluded=any(int(p0.total_degree())==0 for p0 in targets),
 allRetainedWeightAndYLeadingZeroFibersKept=True,
 fixedWeightYFinitenessClaim=False,wholePhiExcluded=False,ordinaryISPClaim=False)
