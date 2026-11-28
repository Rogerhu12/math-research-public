#!/usr/bin/env python3
"""NEW true Phi entire B=0 rational curve and exact original six-by-two charts.

Only the corrected four-original-equation definitions are specialized.
No old bad compact source, old determinant or resource-frozen gate is used.
120 seconds / 1 GiB. All weight zeros of actual heads remain explicit.
"""
import hashlib,itertools,json,math,os,pathlib,resource,signal,time
START=time.perf_counter();DEADLINE=START+120
resource.setrlimit(resource.RLIMIT_AS,(1024**3,1024**3))
original_alarm=signal.alarm
def bounded_alarm(seconds):
 if seconds<=0:return original_alarm(0)
 return original_alarm(max(1,min(int(seconds),math.ceil(DEADLINE-time.perf_counter()))))
signal.alarm=bounded_alarm;signal.alarm(120)
BASENAME='2026-11-28-unit211-Phi-zero-corrected-dual-germ-four-original-quadratic-heads-8542.py'
BASE_SHA='5ee86ff89db7c8babaf3a22c7d72570dcdfbbf92646f56adf37bff854a87ace7'
path=pathlib.Path(__file__).with_name(BASENAME)
if not path.exists():path=pathlib.Path(os.environ.get('ISP_INPUT_DIR',''))/BASENAME
full=path.read_text();assert hashlib.sha256(full.encode()).hexdigest()==BASE_SHA
marker='quads=[extract_quad(p) for p in (Rbar,W4,Obar,N1)]'
assert full.count(marker)==1
prefix=full[:full.index(marker)]
old='u,Q,lam,Tr=map(R,(up,Qp,Lp,Tp))\nz=R(zp)'
new='x=R(up)\nu=(x+1)**2/(3*x)\nQ=4*(x*x-x+1)/3\nlam,Tr,z=map(R,(Lp,Tp,zp))'
assert prefix.count(old)==1
prefix=prefix.replace(old,new)
ns={'__file__':str(path),'__name__':'isp_true_B_rational_original_definitions'}
exec(compile(prefix,str(path),'exec'),ns)
signal.alarm=bounded_alarm;signal.alarm(120)
R=ns['R'];ctx=ns['ctx'];up,Qp,Lp,Tp,zp=ctx.gens()
zeroP=ctx.constant(0);oneP=ctx.constant(1)
x,u,Q,lam,Tr,z=(ns[k] for k in ('x','u','Q','lam','Tr','z'))
quads=[ns['extract_quad'](ns[k]) for k in ('Rbar','W4','Obar','N1')]
names=['corrected_Rbar','original_W4','original_Obar','original_N1']
def say(stage,**kw):
 kw.update(stage=stage,seconds=time.perf_counter()-START)
 print(json.dumps(kw,sort_keys=True),flush=True)
def info(p,small=False):
 ans={'degrees':list(map(int,p.degrees())) if p else [-1]*5,
      'terms':len(p.to_dict()),
      'sha256':hashlib.sha256(str(sorted(p.to_dict().items())).encode()).hexdigest()}
 if small and len(p.to_dict())<=40:ans['polynomial']=str(p)
 return ans
def ir(v):return {'numerator':info(v.n),'denominator':info(v.d)}
def fact(p):
 c,fs=p.factor();prod=ctx.constant(c);out=[]
 for f,n in fs:
  prod*=f**int(n);out.append({'power':int(n),**info(f,True)})
 assert prod==p
 return {'constant':str(c),'factors':out,'fullProductReturned':True}
divisions=0
def exact(a,b):
 global divisions
 q,r=divmod(a,b);assert not r and q*b==a
 divisions+=1;return q
def param(v):
 return all(e[1]==e[2]==e[3]==e[4]==0 for e in v.d.to_dict())
s=u-1;K=Q+4*s;L=Q-2*s*(u-2);Mn=2*u*L-L*L-u*u*Q
B=-Q*Q+(12*u*u-20*u+8)*Q-16*s*s
assert not B
assert Q==4*s*x and x==Q/(4*s)
assert u==(x+1)**2/(3*x) and Q==4*(x*x-x+1)/3
assert 1-Q==-(2*x-1)**2/3
assert ns['ell']==(x+1)*(5*x-1)/(6*x*x)
assert ns['bc']==(x+1)**2*(7*x*x-4*x+1)/(36*x**4)
A=4*s*s-Q
assert A==-4*s*(2*x-1)*(x+1)/(3*x)
paid=up*(up*up-up+1)*(up+1)*(2*up-1)*(5*up-1)*(7*up*up-4*up+1)
def strip_paid(p):
 out=p
 while int(out.total_degree())>0:
  g=out.gcd(paid)
  if int(g.total_degree())<=0:break
  out=exact(out,g)
 return out
def base_den(v):
 assert param(v);rem=v.d
 while int(rem.total_degree())>0:
  g=rem.gcd(paid);assert int(g.total_degree())>0
  rem=exact(rem,g)
 assert rem
for row in quads:
 for c in row:base_den(c)
say('true_whole_B_original_rational_parameter',
 originalInverse='x=Q/(4(u-1))',
 u='(x+1)^2/(3x)',Q='4(x^2-x+1)/3',
 allRationalParameterIdentitiesReturned=True,
 originalFourQuadraticsRebuiltWithoutOldHeadTests=True,
 originalCoefficientDenominatorsOnlyIntrinsicPaidUnits=True,
 originalHeadAAutomaticallyNonzero=True,
 originalPhiExcluded=False)
def dot(a,b):return sum((v*w for v,w in zip(a,b)),R())
def mm(a,b):return [[dot(row,[b[k][j] for k in range(len(b))])
                    for j in range(len(b[0]))] for row in a]
det3=ns['det3']
def adj3(a):
 out=[]
 for i in range(3):
  row=[]
  for j in range(3):
   I=[k for k in range(3) if k!=j];J=[k for k in range(3) if k!=i]
   row.append((-1)**(i+j)*(a[I[0]][J[0]]*a[I[1]][J[1]]-a[I[0]][J[1]]*a[I[1]][J[0]]))
  out.append(row)
 return out
heads=[row[3:] for row in quads]
assert not det3(heads[:3])
selected=None
for triple in ((0,1,3),(0,2,3),(1,2,3)):
 h=det3([heads[i] for i in triple])
 if h:selected=triple;break
assert selected is not None
omitted=next(i for i in range(4) if i not in selected)
H=[heads[i] for i in selected];ad=adj3(H)
unit=[[h if i==j else R() for j in range(3)] for i in range(3)]
assert mm(ad,H)==unit and mm(H,ad)==unit
base_den(h);hcore=strip_paid(h.n)
inv=[[a/h for a in row] for row in ad]
rules=[[-c for c in row] for row in mm(inv,[quads[i][:3] for i in selected])]
v=[R(1),Tr,z];mon=[Tr*Tr,Tr*z,z*z]
original=[dot(row,v+mon) for row in quads]
chosen=[original[i] for i in selected]
for i in range(3):assert mon[i]-dot(rules[i],v)==dot(inv[i],chosen)
trace=[sum((quads[omitted][3+i]*inv[i][j] for i in range(3)),R()) for j in range(3)]
low=[quads[omitted][j]+sum((quads[omitted][3+i]*rules[i][j] for i in range(3)),R()) for j in range(3)]
assert original[omitted]-dot(trace,chosen)==dot(low,v)
def coeffs(v,degree):
 assert param(v);ans=[R() for _ in range(degree+1)]
 for e,c in v.n.to_dict().items():
  assert e[1]==e[3]==e[4]==0 and e[2]<=degree
  ee=(e[0],0,0,0,0);ans[e[2]]=ans[e[2]]+R(ctx.from_dict({ee:c}),v.d)
 assert sum((ans[j]*lam**j for j in range(len(ans))),R())==v
 return ans
c0=coeffs(low[0],2);t0=coeffs(low[1],1);z0=coeffs(low[2],1)
aa,bb,cc,dd=t0[1],t0[0],z0[1],z0[0]
Delta=aa*dd-bb*cc
say('new_true_B_original_linear_remainder',
 selectedOriginalRows=[names[i] for i in selected],
 omittedOriginalRow=names[omitted],head=ir(h),headUnpaidSupport=fact(hcore),
 completeThreeRuleAndOmittedOriginalTraceReturned=True,
 originalLinearDegrees=[2,1,1],slope=ir(Delta),
 slopeFullNumerator=fact(Delta.n) if Delta else None,
 wholeHeadZeroFibersRetained=True,
 wholeSlopeZeroFibersRetained=True,
 noParameterOnlyExclusionClaim=True)
if not Delta:
 say('true_B_slope_identically_zero',noTwoGeneratorModelClaim=True,
     originalPhiExcluded=False,ordinaryISPClaim=False)
 raise SystemExit(0)
support=paid*h.n*Delta.n
def check_den(v):
 assert param(v);rem=v.d
 while int(rem.total_degree())>0:
  g=rem.gcd(support);assert int(g.total_degree())>0
  rem=exact(rem,g)
 assert rem
def add(a,b):
 out=[(a[i] if i<len(a) else R())+(b[i] if i<len(b) else R()) for i in range(max(len(a),len(b)))]
 while out and not out[-1]:out.pop()
 return out
def scale(a,c):return [v*c for v in a]
def sub(a,b):return add(a,scale(b,-1))
def mul(a,b):
 out=[R() for _ in range(max(0,len(a)+len(b)-1))]
 for i,v in enumerate(a):
  for j,w in enumerate(b):out[i+j]=out[i+j]+v*w
 while out and not out[-1]:out.pop()
 return out
def sm(*xs):
 out=[]
 for a in xs:out=add(out,a)
 return out
shift=c0[2]*lam+c0[1]
That=[(-c0[2]*dd*lam+cc*c0[0]-dd*c0[1])/Delta,(cc*lam+dd)/Delta]
zhat=[(c0[2]*bb*lam+bb*c0[1]-aa*c0[0])/Delta,-(aa*lam+bb)/Delta]
assert not sm([low[0]],scale(That,low[1]),scale(zhat,low[2]))
assert not sub(sm(scale(That,aa),scale(zhat,cc)),[-shift,R(1)])
weights=[aa*aa,2*aa*cc,cc*cc]
quadlow=[sum((weights[i]*rules[i][j] for i in range(3)),R()) for j in range(3)]
tag=[sum((weights[i]*inv[i][j] for i in range(3)),R()) for j in range(3)]
qw=sub([shift*shift,-2*shift,R(1)],sm([quadlow[0]],scale(That,quadlow[1]),scale(zhat,quadlow[2])))
assert len(qw)==3 and qw[2]==1
for a in qw:coeffs(a,2);check_den(a)
def substitute(row):
 return sm([row[0]],scale(That,row[1]),scale(zhat,row[2]),
           scale(mul(That,That),row[3]),scale(mul(That,zhat),row[4]),
           scale(mul(zhat,zhat),row[5]))
changed=[substitute(quads[i]) for i in selected]
assert not sub(qw,sm(*(scale(changed[i],tag[i]) for i in range(3))))
six=[]
for fi in changed:
 fi=fi+[R()]*(3-len(fi));assert len(fi)==3
 lin=sub(fi,scale(qw,fi[2]));assert len(lin)<=2
 lin=lin+[R()]*(2-len(lin));wl=[-qw[0]*lin[1],lin[0]-qw[1]*lin[1]]
 assert not sub([R(),lin[0],lin[1]],add(wl,scale(qw,lin[1])))
 six.extend([lin,wl])
 for v0 in fi+lin+wl:check_den(v0)
for row in rules:
 for v0 in row:check_den(v0)
for v0 in low+That+zhat+tag:check_den(v0)
def deg(v):return max((e[2] for e in v.n.to_dict()),default=-1)
say('new_true_B_exact_six_by_two_original_model',
 selectedOriginalRows=[names[i] for i in selected],omittedOriginalRow=names[omitted],
 centeredMonicQuadraticLambdaDegrees=[deg(a) for a in qw],
 sixOriginalRowLambdaDegrees=[[deg(a) for a in row] for row in six],
 originalIdealExactlyPresented=True,
 wholeUnpaidHeadSupport=fact(hcore),
 wholeUnpaidSlopeNumerator=fact(strip_paid(Delta.n)),
 allActualWeightDenominatorsReturned=True,exactDivisions=divisions,
 noPhysicalDInverted=True,noModuleFreenessAssumed=True,
 wholeHeadAndSlopeZeroFibersStillKept=True,
 originalPhiExcluded=False,ordinaryISPClaim=False)
