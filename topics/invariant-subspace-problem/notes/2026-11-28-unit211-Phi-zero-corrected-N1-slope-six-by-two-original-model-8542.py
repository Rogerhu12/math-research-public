#!/usr/bin/env python3
"""NEW true Phi first-head chart: original N1 slope and exact six-by-two model.

Only the necessary definitions of the corrected original four quadratics
are rebuilt.  No old wrong head, old cofactor, or four-head exclusion test runs.
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
p=pathlib.Path(__file__).with_name(BASENAME)
if not p.exists():p=pathlib.Path(os.environ.get('ISP_INPUT_DIR',''))/BASENAME
full=p.read_text();assert hashlib.sha256(full.encode()).hexdigest()==BASE_SHA
marker='heads=[row[3:] for row in quads]'
assert full.count(marker)==1
prefix=full[:full.index(marker)]
ns={'__file__':str(p),'__name__':'isp_new_corrected_definitions'}
exec(compile(prefix,str(p),'exec'),ns)
signal.alarm=bounded_alarm;signal.alarm(120)
R=ns['R'];ctx=ns['ctx'];quads=ns['quads']
u,Q,lam,Tr,z=(ns[k] for k in ('u','Q','lam','Tr','z'))
up,Qp,Lp,Tp,zp=(ns[k] for k in ('up','Qp','Lp','Tp','zp'))
zeroP=ns['zeroP'];oneP=ns['oneP'];det3=ns['det3']
def say(stage,**kw):
 kw.update(stage=stage,seconds=time.perf_counter()-START)
 print(json.dumps(kw,sort_keys=True),flush=True)
def infop(poly,small=False):
 ans={'degrees':list(map(int,poly.degrees()))[:3] if poly else [-1]*3,
      'terms':len(poly.to_dict()),
      'sha256':hashlib.sha256(str(sorted(poly.to_dict().items())).encode()).hexdigest()}
 if small and len(poly.to_dict())<=100:ans['polynomial']=str(poly)
 return ans
def infor(v,small=False):return {'numerator':infop(v.n,small),'denominator':infop(v.d,small)}
def dot(a,b):return sum((x*y for x,y in zip(a,b)),R())
def mm(a,b):return [[dot(row,[b[k][j] for k in range(len(b))])
                    for j in range(len(b[0]))] for row in a]
def adj3(a):
 return [[((-1)**(i+j))*(a[[k for k in range(3) if k!=j][0]][[k for k in range(3) if k!=i][0]]
                         *a[[k for k in range(3) if k!=j][1]][[k for k in range(3) if k!=i][1]]
                        -a[[k for k in range(3) if k!=j][0]][[k for k in range(3) if k!=i][1]]
                         *a[[k for k in range(3) if k!=j][1]][[k for k in range(3) if k!=i][0]])
          for j in range(3)] for i in range(3)]
def coeffs_lambda(v,max_degree):
 assert all(e[2]==0 and e[3]==0 and e[4]==0 for e in v.d.to_dict())
 ans=[R() for _ in range(max_degree+1)]
 for e,c in v.n.to_dict().items():
  assert e[3]==e[4]==0 and e[2]<=max_degree
  ee=(e[0],e[1],0,0,0)
  ans[e[2]]=ans[e[2]]+R(ctx.from_dict({ee:c}),v.d)
 assert sum((ans[j]*lam**j for j in range(len(ans))),R())==v
 return ans
def factor(p):
 c,fs=p.factor();out=ctx.constant(c);data=[]
 for f,n in fs:
  out=out*f**int(n);data.append({'power':int(n),**infop(f,True)})
 assert out==p
 return {'constant':str(c),'factors':data,'fullProductReturned':True}
# These are the newly corrected heads.  AB=0 is kept as an exceptional chart.
s=u-1;K=Q+4*s;L=Q-2*s*(u-2);Mn=2*u*L-L*L-u*u*Q
A=4*s*s-Q;B=-Q*Q+(12*u*u-20*u+8)*Q-16*s*s
U=Q*(1-Q)*s*K*L*Mn
heads=[row[3:] for row in quads[:3]]
h=det3(heads);adj=adj3(heads)
assert h==A*B*Mn**3*L**4/(8*K**3*(1-Q)**4)
assert mm(adj,heads)==[[h if i==j else R() for j in range(3)] for i in range(3)]
assert mm(heads,adj)==[[h if i==j else R() for j in range(3)] for i in range(3)]
inv=[[x/h for x in row] for row in adj]
low=[row[:3] for row in quads[:3]]
rules=[[-x for x in row] for row in mm(inv,low)]
mon=[Tr*Tr,Tr*z,z*z];v=[R(1),Tr,z]
mean=[dot(row,[R(1),Tr,z,Tr*Tr,Tr*z,z*z]) for row in quads[:3]]
for i in range(3):assert mon[i]-dot(rules[i],v)==dot(inv[i],mean)
ntrace=[sum((quads[3][3+i]*inv[i][j] for i in range(3)),R()) for j in range(3)]
nlow=[quads[3][j]+sum((quads[3][3+i]*rules[i][j] for i in range(3)),R()) for j in range(3)]
N1=dot(quads[3],[R(1),Tr,z,Tr*Tr,Tr*z,z*z])
assert N1-dot(ntrace,mean)==dot(nlow,v)
p0=coeffs_lambda(nlow[0],2);rt=coeffs_lambda(nlow[1],1);rz=coeffs_lambda(nlow[2],1)
aa,bb,cc,dd=rt[1],rt[0],rz[1],rz[0]
slope=aa*dd-bb*cc
say('true_original_N1_complete_slope',
 correctedFullSourceSHA256=BASE_SHA,
 necessaryPrefixSHA256=hashlib.sha256(prefix.encode()).hexdigest(),
 rebuiltOnlyNecessaryOriginalDefinitions=True,
 threeRuleOriginalIdentitiesReturned=True,
 fullN1OriginalTraceReturned=True,
 originalReducedDegrees=[2,1,1],
 chartAssumptions=['Phi=0','U!=0','A*B!=0'],
 slope=infor(slope),slopeNumeratorFactorization=factor(slope.n) if slope else None,
 slopeDenominatorFactorization=factor(slope.d),
 wholeABZeroChartKept=True,wholeSlopeZeroChartKept=True,
 originalPhiExcluded=False)
if not slope:
 say('true_original_slope_identically_zero',noTwoGeneratorModelClaim=True,
     originalPhiExcluded=False,ordinaryISPClaim=False)
 raise SystemExit(0)
# Check every actual denominator against precisely the declared open chart.
support=U.n*A.n*B.n*slope.n
denominator_returns=0
def check_den(v):
 global denominator_returns
 assert all(e[2]==e[3]==e[4]==0 for e in v.d.to_dict())
 rem=v.d
 while int(rem.total_degree())>0:
  g=rem.gcd(support);assert int(g.total_degree())>0
  q,r=divmod(rem,g);assert not r and q*g==rem
  denominator_returns+=1;rem=q
 assert rem
for row in rules:
 for value in row:check_den(value)
for value in nlow:check_den(value)
check_den(slope)
# Use w= a*T+c*z+p02*lambda+p01.  No new inverse beyond the true slope.
sh=p0[2]*lam+p0[1]
# Each polynomial below is in a NEW formal w, represented by a coefficient list.
def add(a,b):
 out=[(a[i] if i<len(a) else R())+(b[i] if i<len(b) else R())
      for i in range(max(len(a),len(b)))]
 while out and not out[-1]:out.pop()
 return out
def neg(a):return [-x for x in a]
def sub(a,b):return add(a,neg(b))
def scale(a,s):return [x*s for x in a]
def mul(a,b):
 out=[R() for _ in range(max(0,len(a)+len(b)-1))]
 for i,x in enumerate(a):
  for j,y in enumerate(b):out[i+j]=out[i+j]+x*y
 while out and not out[-1]:out.pop()
 return out
def psum(*xs):
 out=[]
 for x in xs:out=add(out,x)
 return out
That=[(-p0[2]*dd*lam+cc*p0[0]-dd*p0[1])/slope,(cc*lam+dd)/slope]
zhat=[(p0[2]*bb*lam+bb*p0[1]-aa*p0[0])/slope,-(aa*lam+bb)/slope]
assert not psum([nlow[0]],scale(That,nlow[1]),scale(zhat,nlow[2]))
assert not sub(psum(scale(That,aa),scale(zhat,cc)),[-sh,R(1)])
weights=[aa*aa,2*aa*cc,cc*cc]
quad_low=[sum((weights[i]*rules[i][j] for i in range(3)),R()) for j in range(3)]
tag=[sum((weights[i]*inv[i][j] for i in range(3)),R()) for j in range(3)]
qw=sub([sh*sh,-2*sh,R(1)],
       psum([quad_low[0]],scale(That,quad_low[1]),scale(zhat,quad_low[2])))
assert len(qw)==3 and qw[2]==1
for value in qw:coeffs_lambda(value,2);check_den(value)
def substitute(row):
 return psum([row[0]],scale(That,row[1]),scale(zhat,row[2]),
             scale(mul(That,That),row[3]),
             scale(mul(That,zhat),row[4]),
             scale(mul(zhat,zhat),row[5]))
transformed=[substitute(row) for row in quads[:3]]
assert not sub(qw,psum(*(scale(transformed[i],tag[i]) for i in range(3))))
linear=[];six=[]
for fi in transformed:
 fi=fi+[R()]*(3-len(fi));assert len(fi)==3
 ri=sub(fi,scale(qw,fi[2]))
 assert len(ri)<=2
 ri=ri+[R()]*(2-len(ri));linear.append(ri)
 wi=[-qw[0]*ri[1],ri[0]-qw[1]*ri[1]]
 assert not sub([R(),ri[0],ri[1]],add(wi,scale(qw,ri[1])))
 six.extend([ri,wi])
 for value in fi+ri+wi:check_den(value)
for value in tag:check_den(value)
def lambda_degree(v):
 assert all(e[2]==e[3]==e[4]==0 for e in v.d.to_dict())
 return max((int(e[2]) for e in v.n.to_dict()),default=-1)
say('true_original_exact_centered_six_by_two_model',
 coordinate='w=a_s*T+c_s*z+A_s*lambda+B_s',
 inverseOriginalN1AndCoordinateBothReturned=True,
 centeredMonicQuadratic=[infor(x) for x in qw],
 quadraticLambdaDegrees=[lambda_degree(x) for x in qw],
 completeThreeOriginalMeanCombinationReturned=True,
 allThreeLinearRemaindersReturned=True,
 allThreeActualWMultiplesReturned=True,
 exactSixRowsLambdaDegrees=[[lambda_degree(x) for x in row] for row in six],
 originalFourEquationIdealExactlyPresented=True,
 exactMeaning='after eliminating original N1 by Delta, I4=(q_w,ell_0,ell_1,ell_2); its module relations are ell_i,w*ell_i',
 noModuleFreenessAssumed=True,
 exactWeightDenominatorDivisionsReturned=denominator_returns,
 ABZeroAndNewSlopeZeroFullyRetained=True,
 noPhysicalDInverted=True,
 noPureWeightExclusionClaim=True,originalPhiExcluded=False,ordinaryISPClaim=False)
