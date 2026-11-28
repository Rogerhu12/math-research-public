#!/usr/bin/env python3
"""NEW entire true Phi B-curve: all-head gluing and full original I6/12x2.

The former selected H3 chart is not inverted.  All four actual Gram heads
are glued by QQ[x] Bezout.  The sole slope C2 was excluded by the separate
whole-QQ original fixed-t theorem.  No old six-by-two gate is replayed.
120 seconds / 1 GiB; small summaries only.
"""
import hashlib,itertools,json,math,os,pathlib,resource,signal,time
START=time.perf_counter();DEADLINE=START+120
resource.setrlimit(resource.RLIMIT_AS,(1024**3,1024**3))
raw_alarm=signal.alarm
def bounded_alarm(seconds):
 if seconds<=0:return raw_alarm(0)
 return raw_alarm(max(1,min(int(seconds),math.ceil(DEADLINE-time.perf_counter()))))
signal.alarm=bounded_alarm;signal.alarm(120)
BASENAME='2026-11-28-unit211-Phi-zero-corrected-dual-germ-four-original-quadratic-heads-8542.py'
BASE_SHA='5ee86ff89db7c8babaf3a22c7d72570dcdfbbf92646f56adf37bff854a87ace7'
path=pathlib.Path(__file__).with_name(BASENAME)
if not path.exists():path=pathlib.Path(os.environ.get('ISP_INPUT_DIR',''))/BASENAME
full=path.read_text();assert hashlib.sha256(full.encode()).hexdigest()==BASE_SHA
marker='u,Q,lam,Tr=map(R,(up,Qp,Lp,Tp))'
assert full.count(marker)==1
prefix=full[:full.index(marker)]
ns={'__name__':'isp_true_B_rational_arithmetic_only','__file__':str(path)}
exec(compile(prefix,str(path),'exec'),ns)
signal.alarm=bounded_alarm;signal.alarm(120)
from flint import fmpq_poly
R=ns['R'];ctx=ns['ctx'];up,Qp,Lp,Tp,zp=ctx.gens()
zeroP=ctx.constant(0);oneP=ctx.constant(1)
x,lam,ff,tt=map(R,(up,Lp,Tp,zp))
def say(stage,**kw):
 kw.update(stage=stage,seconds=time.perf_counter()-START)
 print(json.dumps(kw,sort_keys=True),flush=True)
def inf(p,small=False):
 out={'degrees':list(map(int,p.degrees())) if p else [-1]*5,
      'terms':len(p.to_dict()),
      'sha256':hashlib.sha256(str(sorted(p.to_dict().items())).encode()).hexdigest()}
 if small and len(p.to_dict())<=40:out['polynomial']=str(p)
 return out
def ir(v):return {'numerator':inf(v.n),'denominator':inf(v.d)}
def pure_x(p):return all(not any(e[1:]) for e in p.to_dict())
def univar(p):
 assert pure_x(p)
 d=int(p.degrees()[0]) if p else -1
 a=[0]*(d+1)
 for e,c in p.to_dict().items():a[int(e[0])]=c
 return fmpq_poly(a)
def multivar(p):
 return ctx.from_dict({(i,0,0,0,0):p[i] for i in range(int(p.degree())+1) if p[i]})
divisions=0
def exact(a,b):
 global divisions
 q,r=divmod(a,b);assert not r and q*b==a
 divisions+=1;return q
F=x*x-x+1;H=2*x-1;J=7*x*x-4*x+1;beta=5*x-1;xp=x+1
u=xp*xp/(3*x);Q=4*F/3;delta=-H*H/3
ell=xp*beta/(6*x*x);aw=1-ell
m=xp*(x-1)*H/(6*x*x);bc=xp*xp*J/(36*x**4)
K0=4*F*xp/(3*x);T0=-K0
P02=4*F*F*xp*beta/(27*x**3)
Pf=16*F**3*xp/(27*x**3)
T=3*(xp-ff)/beta-xp*lam/x-ell
A1=2*F*(ff-xp)/(3*x*x)+2*F*xp*beta*lam/(9*x**3)
V=ff-A1/2+bc*tt;W=-K0/2+2*u*ff
M=4*bc*delta
xm=((u-ell*Q)*V-m*W)/M;ym=(ell*W-u*V)/M
paid0=up*(up*up-up+1)*(up+1)*(2*up-1)*(5*up-1)*(7*up*up-4*up+1)
C2=23*up*up-11*up+2
paid=paid0*C2
def supported(p,support):
 assert pure_x(p);r=p
 while int(r.total_degree())>0:
  g=r.gcd(support)
  if int(g.total_degree())<=0:return False
  r=exact(r,g)
 return bool(r)
def ckden(v,support=paid):
 assert supported(v.d,support),('unpaid original coefficient denominator',str(v.d))
def q(v=0,w=0):return [R(v),R(w)]
def qa(a,b):return [a[0]+b[0],a[1]+b[1]]
def qn(a):return [-a[0],-a[1]]
def qs(a,b):return qa(a,qn(b))
def qm(a,b):return [a[0]*b[0]+delta*a[1]*b[1],a[0]*b[1]+a[1]*b[0]]
def qc(a,n):return [n*a[0],n*a[1]]
def qt(c,a):return qc(a,c)
def conj(a):return [a[0],-a[1]]
b=q(ell/2,-xp*(x-1)/(4*x*x*H));c=conj(b)
p=q(1,1);qq=conj(p);unit=[q(1),q(),q(1),q(1)]
X=q(xm,ym);Y=conj(X)
rr=qs(qs(X,qt(aw,p)),qt(tt,c));ss=conj(rr)
rows=[[q(),q(),p,qq],[q(),q(A1),rr,ss],[p,rr,q(),q(tt)],[qq,ss,q(tt),q()]]
def vm(a,b):return [qm(a[0],b[0]),qa(qm(a[0],b[1]),qm(a[1],b[0])),qm(a[2],b[2]),qm(a[3],b[3])]
def va(a,b):return [qa(v,w) for v,w in zip(a,b)]
def vs(a,v):return [qm(a,w) for w in v]
def qsum(*xs):
 out=q()
 for a in xs:out=qa(out,a)
 return out
def tau(v):return qsum(qt(aw,v[0]),v[1],qm(b,v[2]),qm(c,v[3]))
def DK(v):return [tau(vm(row,v)) for row in rows]
dv=DK(unit);F2=tau(dv);Kd=DK(dv);d2=vm(dv,dv)
def iszero(a):return not a[0] and not a[1]
def pure(a):assert not a[1];return a[0]
def mean(j):
 z=qc(tau(vm(rows[0],rows[1])),2) if j==1 else tau(vm(rows[j],rows[j]))
 return qsum(z,qc(Kd[j],-2),qc(d2[j],-2),qc(qm(F2,dv[j]),2))
def centered(v):return va(v,vs(qn(tau(v)),unit))
def P2(v):
 z=centered(v);return tau(vm(vm(z,z),z))
def N4(v):
 tv=tau(v);vv=vm(v,v)
 return qsum(qc(tau(vm(dv,vv)),2),qn(qm(F2,tau(vv))),
             qc(qm(tv,tau(vm(dv,v))),-4),qc(qm(F2,qm(tv,tv)),2),tau(vm(v,DK(v))))
assert iszero(qs(F2,q(2*ff))) and iszero(mean(0))
assert iszero(qs(P2(rows[0]),q(P02)))
N0=N4(rows[0]);w=lam-1-T
assert iszero(qs(N0,q(2*lam*P02)))
Pj=qc(tau(vm(vm(centered(rows[0]),centered(rows[0])),centered(rows[1]))),3)
assert iszero(qs(Pj,q(3*w*P02)))
EB=mean(2);assert iszero(qs(mean(3),conj(EB)))
Nj=qs(qs(N4(va(rows[0],rows[1])),N0),N4(rows[1]))
N1=pure(qs(Nj,q(4*lam*w*P02)))
A2=2*lam*lam-2*lam+1;B3=4*lam**3-6*lam*lam+3*lam-1
NS=pure(qs(qsum(qm(b,N4(rows[2])),qm(c,N4(rows[3]))),q(2*lam*P02*(ell+2*T+A2))))
PS=pure(qs(qsum(qm(b,P2(rows[2])),qm(c,P2(rows[3]))),q(P02*(ell+3*T+3*A2+B3))))
original=[pure(mean(1)),EB[0],EB[1],N1]
def dot(a,b):return sum((v*w for v,w in zip(a,b)),R())
def mm(a,b):return [[dot(row,[b[k][j] for k in range(len(b))]) for j in range(len(b[0]))] for row in a]
def coefficients(value,limit=2):
 assert pure_x(value.d);out={}
 for e,c0 in value.n.to_dict().items():
  assert e[1]==0 and e[3]+e[4]<=limit
  pair=(int(e[3]),int(e[4]));ee=(e[0],0,e[2],0,0)
  out[pair]=out.get(pair,R())+R(ctx.from_dict({ee:c0}),value.d)
 assert sum((a*ff**i*tt**j for (i,j),a in out.items()),R())==value
 return out
slots=[(0,0),(1,0),(0,1),(2,0),(1,1),(0,2)]
quads=[[coefficients(v).get(s,R()) for s in slots] for v in original]
for row in quads:
 for a in row:ckden(a,paid0)
heads=[row[3:] for row in quads]
assert all(pure_x(v.n) and pure_x(v.d) for row in heads for v in row)
def det3(a):
 return a[0][0]*(a[1][1]*a[2][2]-a[1][2]*a[2][1])-a[0][1]*(a[1][0]*a[2][2]-a[1][2]*a[2][0])+a[0][2]*(a[1][0]*a[2][1]-a[1][1]*a[2][0])
def adj3(a):
 out=[]
 for i in range(3):
  row=[]
  for j in range(3):
   I=[k for k in range(3) if k!=j];J0=[k for k in range(3) if k!=i]
   row.append((-1)**(i+j)*(a[I[0]][J0[0]]*a[I[1]][J0[1]]-a[I[0]][J0[1]]*a[I[1]][J0[0]]))
  out.append(row)
 return out
triples=list(itertools.combinations(range(4),3));determinants=[det3([heads[i] for i in I]) for I in triples]
assert not determinants[0]
DD=oneP
for v in determinants:
 g=DD.gcd(v.d);DD=exact(DD,g)*v.d
polys=[v.n*exact(DD,v.d) for v in determinants]
g=fmpq_poly([]);bez=[fmpq_poly([]) for _ in polys]
for i,p0 in enumerate(polys):
 if not p0:continue
 n,a,b0=g.xgcd(univar(p0))
 assert a*g+b0*univar(p0)==n
 bez=[a*v for v in bez];bez[i]+=b0;g=n
assert sum((a*univar(p0) for a,p0 in zip(bez,polys)),fmpq_poly([]))==g
gg=multivar(g)
assert gg and supported(gg,paid0),('all-head unclosed support',str(gg))
inv=[[R() for _ in range(4)] for _ in range(3)]
for I,bez0 in zip(triples,bez):
 alpha=R(multivar(bez0)*DD,gg);ad=adj3([heads[i] for i in I])
 for i in range(3):
  for j,k in enumerate(I):inv[i][k]+=alpha*ad[i][j]
assert mm(inv,heads)==[[R(int(i==j)) for j in range(3)] for i in range(3)]
low=[row[:3] for row in quads]
rules=[[-v for v in row] for row in mm(inv,low)]
vv=[R(1),ff,tt];mons=[ff*ff,ff*tt,tt*tt]
for i in range(3):assert mons[i]-dot(rules[i],vv)==dot(inv[i],original)
for row in inv+rules:
 for v in row:ckden(v,paid0)
say('new_true_B_all_original_heads_glued',
 allHeadQQBezoutReturned=True,allThreeGlobalRulesReturned=True,
 noH3Inverted=True,allActualRuleDenominatorsOnlyIntrinsicUnits=True,
 wholeBOriginalThreeGeneratorModel=True,
 allHeadCommonNumerator=inf(gg,True),ordinaryISPClaim=False)
kappa=[-18*x**3*H,2-13*x+54*x*x-79*x**3+68*x**4,H*(-2+15*x-54*x*x+97*x**3-48*x**4)]
Lraw=dot(kappa,original[:3]);coef=coefficients(Lraw)
assert not any(coef.get(s,R()) for s in [(2,0),(1,1),(0,2)])
def lc(v,degree):
 assert pure_x(v.d);ans=[R() for _ in range(degree+1)]
 for e,a in v.n.to_dict().items():
  assert e[1]==e[3]==e[4]==0 and e[2]<=degree
  ans[int(e[2])]+=R(ctx.from_dict({(e[0],0,0,0,0):a}),v.d)
 assert sum((a*lam**j for j,a in enumerate(ans)),R())==v
 return ans
p0=lc(coef.get((0,0),R()),2);fl=lc(coef.get((1,0),R()),1);tl=lc(coef.get((0,1),R()),1)
aa,bb,cc,dd=fl[1],fl[0],tl[1],tl[0]
Delta=aa*dd-bb*cc
assert Delta and supported(Delta.n,paid) and supported(Delta.d,paid0)
ckden(1/Delta)
def add(a,b):
 out=[(a[i] if i<len(a) else R())+(b[i] if i<len(b) else R()) for i in range(max(len(a),len(b)))]
 while out and not out[-1]:out.pop()
 return out
def scale(a,c):return [v*c for v in a]
def sub(a,b):return add(a,scale(b,-1))
def mul(a,b):
 out=[R() for _ in range(max(0,len(a)+len(b)-1))]
 for i,v in enumerate(a):
  for j,w0 in enumerate(b):out[i+j]+=v*w0
 while out and not out[-1]:out.pop()
 return out
def sm(*xs):
 out=[]
 for a in xs:out=add(out,a)
 return out
def pw(a,n):
 out=[R(1)]
 for _ in range(n):out=mul(out,a)
 return out
shift=p0[2]*lam+p0[1]
fhat=[(-p0[2]*dd*lam+cc*p0[0]-dd*p0[1])/Delta,(cc*lam+dd)/Delta]
that=[(p0[2]*bb*lam+bb*p0[1]-aa*p0[0])/Delta,-(aa*lam+bb)/Delta]
assert not sm([coef.get((0,0),R())],scale(fhat,coef.get((1,0),R())),scale(that,coef.get((0,1),R())))
assert not sub(sm(scale(fhat,aa),scale(that,cc)),[-shift,R(1)])
weights=[aa*aa,2*aa*cc,cc*cc]
qlow=[sum((weights[i]*rules[i][j] for i in range(3)),R()) for j in range(3)]
tag=[sum((weights[i]*inv[i][j] for i in range(3)),R()) for j in range(4)]
qw=sub([shift*shift,-2*shift,R(1)],sm([qlow[0]],scale(fhat,qlow[1]),scale(that,qlow[2])))
assert len(qw)==3 and qw[2]==1
for v in qw:lc(v,2);ckden(v)
def substitute(value,limit):
 dd0=coefficients(value,limit)
 return sm(*(scale(mul(pw(fhat,i),pw(that,j)),a) for (i,j),a in dd0.items()))
changed=[substitute(v,2) for v in original]
assert not sub(qw,sm(*(scale(v,a) for v,a in zip(changed,tag))))
linear=[]
for fi in changed:
 fi=fi+[R()]*(3-len(fi));assert len(fi)==3
 r=sub(fi,scale(qw,fi[2]));assert len(r)<=2
 linear.append(r+[R()]*(2-len(r)))
def reduce_omega(poly):
 r=poly[:];quo=[]
 while len(r)>2:
  a=r[-1];k=len(r)-3;t0=[R()]*k+[a];quo=add(quo,t0);r=sub(r,mul(t0,qw))
 assert not sub(poly,add(mul(quo,qw),r))
 return r+[R()]*(2-len(r)),quo
newValues=[];quotients=[]
for value in [NS,PS]:
 changedValue=substitute(value,3);rem,quot=reduce_omega(changedValue)
 newValues.append(rem);quotients.append(quot);linear.append(rem)
twelve=[]
for row in linear:
 wr=[-qw[0]*row[1],row[0]-qw[1]*row[1]]
 assert not sub([R(),row[0],row[1]],add(wr,scale(qw,row[1])))
 twelve.extend([row,wr])
for values in [fhat,that,tag,qw,*linear,*twelve,*quotients]:
 for v in values:ckden(v)
def deg(v):return max((int(e[2]) for e in v.n.to_dict()),default=-1)
cofactors=[]
for i,j in [(0,4),(0,5),(4,5)]:
 val=linear[i][0]*linear[j][1]-linear[i][1]*linear[j][0]
 ckden(val)
 lcP=zeroP;d=deg(val)
 for e,c0 in val.n.to_dict().items():
  if int(e[2])==d:lcP+=ctx.from_dict({(e[0],0,0,0,0):c0})
 cofactors.append({'originalRows':[i,j],'lambdaDegree':d,'value':ir(val),'leadingNumerator':inf(lcP,True)})
say('new_whole_true_B_exact_original_I6_twelve_by_two',
 originalGeometricVariables='lambda,f,t',
 scalarCoefficientRing='QQ[x,1/(x F (x+1) H beta J C2)][lambda]',
 noH3Inverted=True,wholeC2OriginalExclusionUsed=True,
 monicQuadraticLambdaDegrees=[deg(v) for v in qw],
 fourOriginalQuadraticsAndFullWeightedNPReturned=True,
 exactI6Meaning='I6=(q_omega,ell_0,ell_1,ell_2,ell_3,n_omega,p_omega)',
 fullTwelveRowsLambdaDegrees=[[deg(v) for v in row] for row in twelve],
 allActualWeightDenominatorsReturned=True,
 fixedNewTwoColumnCofactors=cofactors,exactDivisions=divisions,
 noModuleFreenessAssumed=True,noPhysicalDInverted=True,
 wholeBExcluded=False,wholePhiExcluded=False,ordinaryISPClaim=False)
