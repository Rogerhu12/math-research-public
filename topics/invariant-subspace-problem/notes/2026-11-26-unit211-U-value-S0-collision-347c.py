#!/usr/bin/env python3
"""R150 unit211: S=0 and its f coefficient zero on a value-collision chart.
The remaining exact field is QQ(sqrt(2),sqrt(3)); all four embeddings are
covered. A final unit GB is required before claiming this fiber excluded.
"""
import hashlib,json,resource,signal,time
from pathlib import Path
import sympy as sp
from sympy import QQ
started=time.perf_counter()
def say(obj):
 obj['elapsedSeconds']=round(time.perf_counter()-started,6)
 print(json.dumps(obj,sort_keys=True),flush=True)
def alarm_handler(signum,frame):
 say({'status':'timeout_unknown','claimExcluded':False})
 raise SystemExit(124)
signal.signal(signal.SIGALRM,alarm_handler);signal.alarm(300)
K=QQ.algebraic_field(sp.sqrt(2),sp.sqrt(3))
assert K.ext.minpoly.degree()==4
lam=K.from_sympy(sp.sqrt(2)/2)
s3=K.from_sympy(sp.sqrt(3))
assert 2*lam*lam-1==0
b=4*(5+lam)/49;c=b;l=b+c;a=1-l
h=lam-K.one/2;k=h;w=(3*lam+1)/7
q=(23-64*lam+7*s3*(1-4*lam))/(2*(13-17*lam))
assert (13-17*lam)*q*q+(64*lam-23)*q+(13-17*lam)==0
assert b and c and q and q-1 and q+1
u=b+c*q;V2=b+c*q*q
P0=(b+c*q**3-3*u*V2+2*u**3)/2
assert P0 and u
assert a+w+b*h+c*k==lam
assert a+2*w+b*h*h+c*k*k==2*lam*lam
assert a+3*w+b*h**3+c*k**3==4*lam**3
z=(h-1)*(k-1)
assert h+k+1-2*lam==0
assert 3-4*lam-z*(l+u*(q+1-2*u)/q)==0
assert z*((2*u-q-1)*(V2-2*u*u)+4*lam*P0)/q-2*w*(b*(k-1)+c*q*(h-1))==0
ff,tt=sp.symbols('f t')
def C(x):return sp.Poly(K.to_sympy(K.convert(x)),ff,tt,domain=K)
zero=C(0);onep=C(1);half=C(K.one/2);quarter=C(K.one/4)
f=sp.Poly(ff,ff,tt,domain=K);t=sp.Poly(tt,ff,tt,domain=K)
one=[onep,zero,onep,onep]
def add(v,w):return [x+y for x,y in zip(v,w)]
def scale(c0,v):return [c0*x for x in v]
def mul(v,w):return [v[0]*w[0],v[0]*w[1]+v[1]*w[0],v[2]*w[2],v[3]*w[3]]
def tau(v):return C(a)*v[0]+v[1]+C(b)*v[2]+C(c)*v[3]
def P(v):
 z=add(v,scale(-tau(v),one))
 return half*tau(mul(mul(z,z),z))
W1=C(V2/2-u*u)+C(2*u)*f
W2=C(u*V2-2*u**3+2*lam*P0)+C(V2+2*u*u)*f-C(b*c*q)*t
x=C(q/(b*(q-1)))*W1-C(1/(b*(q-1)))*W2
y=C(1/(c*q*(q-1)))*(W2-W1)
r=x-C(a)-C(c)*t;s=y-C(a*q)-C(b)*t
A1=2*f-C(2*b)*x-C(2*c)*y+C(2*b*c)*t
rows=[[zero,zero,onep,C(q)],[zero,A1,r,s],[onep,r,zero,t],[C(q),s,t,zero]]
def DK(v):return [tau(mul(row,v)) for row in rows]
d=DK(one);F=half*tau(d)
assert F==f
def N(v):
 return half*tau(mul(add(d,scale(-F,one)),mul(v,v)))-tau(v)*tau(mul(d,v))+F*tau(v)**2+quarter*tau(mul(v,DK(v)))
def Pjet(v,w):
 z=add(v,scale(-tau(v),one));z1=add(w,scale(-tau(w),one))
 return 3*half*tau(mul(mul(z,z),z1))
def Njet(v,w):return N(add(v,w))-N(v)-N(w)
Ps=[P(rows[0]),Pjet(rows[0],rows[1]),P(rows[2]),P(rows[3])]
Ns=[N(rows[0]),Njet(rows[0],rows[1]),N(rows[2]),N(rows[3])]
ev=[tau(mul(rows[0],rows[0])),2*tau(mul(rows[0],rows[1])),tau(mul(rows[2],rows[2])),tau(mul(rows[3],rows[3]))]
E=add(add(ev,scale(C(-2),DK(d))),add(scale(C(-2),mul(d,d)),scale(4*F,d)))
VV=[onep,C(w),C(h),C(k)]
assert Ps[0]==C(P0) and E[0].is_zero and Ns[0]==C(lam*P0)
assert P(VV).is_zero and N(VV).is_zero
polys=E[1:]+[Ps[1]-C(3*w*P0),Ps[2]-C(h**3*P0),Ps[3]-C(k**3*P0),Ns[1]-C(2*lam*w*P0),Ns[2]-C(lam*h*h*P0),Ns[3]-C(lam*k*k*P0)]
labels=['E1','EB','EC','P1-3wP0','PB-h3P0','PC-k3P0','N1-2lambda*wP0','NB-lambda-h2P0','NC-lambda-k2P0']
source_sha=hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
input_sha=hashlib.sha256('\n'.join(sp.srepr(p.as_expr()) for p in polys).encode()).hexdigest()
profiles=[{'name':name,'degrees':[int(d) for d in p.degree_list()] if not p.is_zero else [-1,-1],'terms':len(p.terms()) if not p.is_zero else 0} for name,p in zip(labels,polys)]
say({'stage':'original_equations_verified','sourceSha256':source_sha,'inputSha256':input_sha,'field':'QQ(sqrt(2),sqrt(3))','coversAllFourEmbeddings':True,'chart':'S=0,Af=0,h=k,2lambda^2=1','conditions':profiles,'claimExcluded':False})
gb=sp.groebner([p.as_expr() for p in polys if not p.is_zero],ff,tt,domain=K,order='grevlex',method='f5b')
excluded=len(gb.polys)==1 and not gb.polys[0].is_zero and gb.polys[0].total_degree()==0
signal.alarm(0)
report={'schema':'r150-unit211-U-value-S0-collision-Af0-v1','status':'exact_original_fiber_excluded' if excluded else 'exact_candidates_not_excluded','claimExcluded':excluded,'claimLambdaLayerEmpty':False,'ordinaryISPClaim':False,'sourceSha256':source_sha,'inputSha256':input_sha,'finalBasis':[{'totalDegree':int(p.total_degree()),'terms':len(p.terms())} for p in gb.polys],'peakRssKiB':resource.getrusage(resource.RUSAGE_SELF).ru_maxrss}
if not excluded:
 text='\n'.join(str(p.as_expr()) for p in gb.polys)
 if len(text.encode())<8000:report['candidateBasis']=text
say(report)
raise SystemExit(0 if excluded else 2)
