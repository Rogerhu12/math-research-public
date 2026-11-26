#!/usr/bin/env python3
"""R150 unit211: exact L=0, w=1 U-value fiber over Q(sqrt(17)).
All original mean, highest and second-gradient equations are retained.
Only a final exact unit Groebner basis constitutes an exclusion.
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
signal.signal(signal.SIGALRM,alarm_handler)
signal.alarm(900)
# This finite fiber is over one irreducible quadratic number field.
# Its two complex embeddings cover both lambda roots simultaneously.
rr,ff,tt,zz=sp.symbols('rho f t z_sat')
K=QQ.algebraic_field(sp.sqrt(17))
D=K.frac_field(rr)
rho=D.from_sympy(rr)
lam=D.from_sympy((3+sp.sqrt(17))/8)
assert 8*lam*lam-6*lam-1==0
Al=2*lam*lam-2*lam+1
Bl=4*lam**3-6*lam*lam+3*lam-1
R0=lam-2
assert R0 and Al and Bl
assert R0*Bl-Al*Al==3*(7-10*lam)/16
assert R0*Bl-Al*Al
q=(Bl-rho*Al)/(rho*(Al-rho*R0))
u=R0/rho
V2=Al/(rho*rho)
b=(q*u-V2)/(q-1)
c=(V2-u)/(q*(q-1))
a=1-b-c
h=1+rho;k=1+rho*q
P0=(b+c*q**3-3*u*V2+2*u**3)/2
assert rho**3*P0==6*lam-D(11)/2
assert P0 and b and c and q and q-1 and q+1
assert a+1+b*h+c*k==lam
assert a+2+b*h*h+c*k*k==2*lam*lam
assert a+3+b*h**3+c*k**3==4*lam**3
assert q*(h-1)-(k-1)==0
def C(x):
 return sp.Poly(D.to_sympy(D.convert(x)),ff,tt,domain=D)
zero=C(0);onep=C(1);half=C(D.one/2);quarter=C(D.one/4)
f=sp.Poly(ff,ff,tt,domain=D);t=sp.Poly(tt,ff,tt,domain=D)
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
r=x-C(a)-C(c)*t
s=y-C(a*q)-C(b)*t
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
VV=[onep,onep,C(h),C(k)]
assert Ps[0]==C(P0)
assert E[0].is_zero
assert Ns[0]==C(lam*P0)
assert P(VV).is_zero and N(VV).is_zero
conditions=E[1:]+[Ps[1]-C(3*P0),Ps[2]-C(h**3*P0),Ps[3]-C(k**3*P0),Ns[1]-C(2*lam*P0),Ns[2]-C(lam*h*h*P0),Ns[3]-C(lam*k*k*P0)]
labels=['E1','EB','EC','P1-3P0','PB-h3P0','PC-k3P0','N1-2lambdaP0','NB-lambda-h2P0','NC-lambda-k2P0']
# Every introduced denominator below is required to be a product of
# these paid chart units. The rational q graph's exceptional denominator
# was excluded above by R0*Bl-Al^2 != 0.
DR=D.get_ring()
known=DR.one
for v in [rho,q,q-1,q+1,b,c,u,P0,Al-rho*R0,h-1,k-1,h-k]:
 assert v
 known*=v.numer*v.denom
known=sp.Poly(known.as_expr(),rr,domain=K).sqf_part()
def stripsingle(p,unit):
 while not p.is_zero:
  g=p.gcd(unit)
  if g.total_degree()==0:return p.monic()
  p=p.exquo(g)
 return p
def check_denominator(den):
 pp=sp.Poly(den.as_expr(),rr,domain=K)
 assert stripsingle(pp,known).total_degree()==0
known3=sp.Poly(known.as_expr(),ff,tt,rr,domain=K)
def clear_to_three(po):
 co=po.rep.to_dict()
 den=DR.one
 for value in co.values():den=DR.lcm(den,value.denom)
 check_denominator(den)
 out={}
 for ij,value in co.items():
  pp=DR.exquo(den,value.denom)*value.numer
  for (j,),cf in pp.items():
   key=(ij[0],ij[1],j)
   out[key]=out.get(key,K.zero)+cf
 result=sp.Poly.from_dict(out,ff,tt,rr,domain=K)
 return stripsingle(result,known3)
polys=[clear_to_three(p) for p in conditions]
profiles=[{'name':name,'degrees':[int(d) for d in p.degree_list()] if not p.is_zero else [-1,-1,-1],'terms':len(p.terms()) if not p.is_zero else 0} for name,p in zip(labels,polys)]
source_sha=hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
input_sha=hashlib.sha256('\n'.join(sp.srepr(p.as_expr()) for p in polys).encode()).hexdigest()
say({'stage':'original_equations_verified','sourceSha256':source_sha,'inputSha256':input_sha,'field':'QQ(sqrt(17)), lambda=(3+sqrt(17))/8','coversBothEmbeddings':True,'chart':'L=0,w=1','conditions':profiles,'paidUnitDegree':int(known.degree()),'claimExcluded':False})
# Every pass changes the ideal only by multiplication/division by known
# nonzero units. No generic rho field inversion is used in the GB stage.
active=[p for p in polys if not p.is_zero]
excluded=False
rounds=[]
for j in range(4):
 gb=sp.groebner([p.as_expr() for p in active],ff,tt,rr,domain=K,order='grevlex',method='f5b')
 bp=[sp.Poly(p.as_expr(),ff,tt,rr,domain=K) for p in gb.polys]
 rounds.append({'round':j,'basisCount':len(bp),'totalDegrees':[int(p.total_degree()) for p in bp]})
 if len(bp)==1 and bp[0].total_degree()==0:
  excluded=True;break
 simplified=[stripsingle(p,known3) for p in bp]
 if any(p.total_degree()==0 for p in simplified):
  excluded=True;break
 if simplified==bp:
  active=bp;break
 active=simplified
if not excluded:
 # Saturation by exactly the paid unit polynomial retains every valid
 # chart point, including all isolated rho fibers.
 say({'stage':'exact_saturation','rounds':rounds,'claimExcluded':False})
 gb=sp.groebner([p.as_expr() for p in active]+[zz*known.as_expr()-1],zz,ff,tt,rr,domain=K,order='grevlex',method='f5b')
 excluded=len(gb.polys)==1 and gb.polys[0].total_degree()==0
 basis_profiles=[{'totalDegree':int(p.total_degree()),'terms':len(p.terms())} for p in gb.polys]
else:basis_profiles=[{'totalDegree':0,'terms':1}]
signal.alarm(0)
say({'schema':'r150-unit211-U-value-L0-w1-v1','status':'exact_original_fiber_excluded' if excluded else 'exact_candidates_not_excluded','claimExcluded':excluded,'claimLambdaLayerEmpty':False,'ordinaryISPClaim':False,'sourceSha256':source_sha,'inputSha256':input_sha,'rounds':rounds,'finalBasis':basis_profiles,'peakRssKiB':resource.getrusage(resource.RUSAGE_SELF).ru_maxrss})
raise SystemExit(0 if excluded else 2)
