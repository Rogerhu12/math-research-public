#!/usr/bin/env python3
"""Original unit211: equal nonzero base pairings, b+c=0, complete exclusion.
AI-assisted GPT-6 Astra Pro, Astra-ISP-347c-20261126 / root.
Only exact QQ identities and complete univariate resultants are used.
The physical germ and projective completeness arguments are in the proof.
"""
import hashlib,json,resource,signal,time
from pathlib import Path
import sympy as S
started=time.monotonic()
resource.setrlimit(resource.RLIMIT_AS,(1024*1024**2,)*2)
def timeout(signum,frame):raise TimeoutError('unit211 equal-pairing zero-weight exact budget')
signal.signal(signal.SIGALRM,timeout);signal.alarm(180)
b,A,r,s,t,x,y,f,j=S.symbols('b A r s t x y f j')
one=S.Matrix([1,0,1,1])
KB=S.Matrix([[0,0,1,1],[0,A,r,s],[1,r,0,t],[1,s,t,0]])
def mul(z,w):return S.Matrix([z[0]*w[0],z[0]*w[1]+z[1]*w[0],z[2]*w[2],z[3]*w[3]])
def tau(z):return z[0]+z[1]+b*z[2]-b*z[3]
def DK(z):return S.Matrix([tau(mul(KB.row(i),z)) for i in range(4)])
def P(z):
 w=z-tau(z)*one
 return tau(mul(mul(w,w),w))/2
def eq(a,b=0):assert S.cancel(a-b)==0
d=DK(one);F=tau(d)/2
e=S.Matrix([tau(mul(KB.row(0),KB.row(0))),2*tau(mul(KB.row(0),KB.row(1))),tau(mul(KB.row(2),KB.row(2))),tau(mul(KB.row(3),KB.row(3)))])
E=[S.expand(v) for v in e-2*DK(d)-2*mul(d,d)+4*F*d]
chart={r:x-1+b*t,s:y-1-b*t,A:2*f-2*b*(x-y)-2*b*b*t}
eq(F.subs(chart,simultaneous=True),f)
eq(E[0].subs(chart,simultaneous=True),-2*b*(x-y))
pjet=P(KB.row(0).T+j*KB.row(1).T)
eq(pjet.subs(j,0))
eq(S.diff(pjet,j).subs(j,0).subs(chart,simultaneous=True).subs(y,x),3*b*b*t)
equal_chart={r:x-1,s:x-1,A:2*f,t:0}
eq(E[1].subs(equal_chart,simultaneous=True),8*f*f)
eq(E[2].subs(equal_chart,simultaneous=True),-2*x*x+2*x-1+4*f*(x-1))
Z=S.Matrix(S.symbols('Z0:4'));epsilon=S.symbols('epsilon')
k0=S.Matrix([0,0,1,1])
germ=P((1+r*epsilon)*k0+epsilon**2*Z)
eq(S.expand(germ).coeff(epsilon,2),3*b*(Z[2]-Z[3])/2)

z,w,a=S.symbols('z w a')
K=S.Matrix([[0,0,0,0,5,-1],[0,0,0,-32,5,-1],[0,0,54,-4,5,0],[0,-32,-4,-8,0,0],[5,5,5,0,0,0],[-1,-1,0,0,0,0]])
def u(q):return S.Matrix([q**i for i in range(6)])
assert K.det()==-25600
eq((u(a).T*K*u(a))[0])
eq((S.diff(u(a),a).T*K*S.diff(u(a),a))[0],-2*a*a*(a-2)*(a+6))
polar=(u(a).T*K*u(z))[0]
q=S.cancel(-(u(z).T*K*u(w))[0]/(z-w)**2)
expected={0:(z**13*(z-5)**3,[22,24]),2:((z-2)**8*(3*z*z-17*z+6)**2/9,[24,24]),-6:((z+6)**8*(5*z*z+65*z+66)**2/25,[24,24]),'infinity':(z+1,[5,9])}
records=[]
for aval in [0,2,-6,'infinity']:
 if aval=='infinity':fs=[sum(K[i,k]*z**k for k in range(6)) for i in [5,4,3]]
 else:fs=[S.diff(polar,a,k).subs(a,aval)/S.factorial(k) for k in range(3)]
 f0,f1,f2=fs
 L=[]
 for fj in [f1,f2]:
  num=S.expand(fj*f0.subs(z,w)-fj.subs(z,w)*f0)
  val,rem=S.div(num,z-w,z,w,domain=S.QQ)
  assert rem==0
  L.append(val)
 rr=[S.Poly(S.resultant(q,li,w),z,domain=S.QQ) for li in L]
 gg=S.gcd(rr[0],rr[1]).monic()
 want,degrees=expected[aval]
 assert gg==S.Poly(want,z,domain=S.QQ)
 assert [ri.degree() for ri in rr]==degrees
 # Every surviving first coordinate would make its original base pairing zero.
 rad=gg.sqf_part().monic()
 assert S.rem(S.Poly(f0,z,domain=S.QQ),rad)==0
 boundary=None
 if aval!='infinity':
  f0inf=S.Poly(f0,z).nth(5);f1inf=S.Poly(f1,z).nth(5)
  gate=S.expand(f1.subs(z,-1)*f0inf-f1inf*f0.subs(z,-1))
  assert gate=={0:-32,2:-1944,-6:-5000}[aval]
  assert f0inf*f0.subs(z,-1)!=0
  boundary=int(gate)
 records.append({'base':aval,'resultantDegrees':degrees,'monicGcd':str(S.factor(gg.as_expr())),'gcdRadicalDividesOriginalBasePolar':True,'finiteInfinityFirstJetGate':boundary})
signal.alarm(0)
print(json.dumps({'schema':'r150-unit211-equal-base-zero-total-weight-20261126-v1','status':'all_exact_QQ_checks_pass','sourceSha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'scope':'p=q nonzero and b+c=0 only; all original physical base points and infinity','originalMeanAndHighestJetVerified':True,'secondOrderPhysicalGermVerified':True,'physicalPolarGates':records,'elapsedSeconds':round(time.monotonic()-started,6),'peakRssKiB':resource.getrusage(resource.RUSAGE_SELF).ru_maxrss,'ordinaryISPClaim':False},sort_keys=True))
