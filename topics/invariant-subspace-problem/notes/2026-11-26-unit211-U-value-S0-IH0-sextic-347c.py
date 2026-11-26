#!/usr/bin/env python3
"""R150 unit211: S=0, Af=0, three distinct V values, I=H=0.
The finite lambda locus is derived again over QQ. All roots of its
irreducible sextic and all x/q fibers are kept. Only an exact unit basis
of the original equations yields an exclusion.
"""
import hashlib,json,resource,signal,time
from pathlib import Path
import sympy as sp
from sympy import QQ
started=time.perf_counter()
def say(o):
 o['elapsedSeconds']=round(time.perf_counter()-started,6)
 print(json.dumps(o,sort_keys=True),flush=True)
def alarm_handler(signum,frame):
 say({'status':'timeout_unknown','claimExcluded':False})
 raise SystemExit(124)
signal.signal(signal.SIGALRM,alarm_handler);signal.alarm(900)
ll,zz=sp.symbols('lambda z')
AA=2*ll**2-2*ll+1;CC=-4*ll**2+5*ll-2
ss=2*ll-3;RR=3-4*ll;jj=2*ll-1;DD=ss*CC-AA*zz
II=sp.expand(2*(4*ll-1)*CC*DD+zz*(2*CC*(1-ll)*RR-2*(4*ll**2-7*ll+2)*DD)+zz**2*(-2*ll*CC+ss*jj*RR))
HH=sp.expand(DD*((4*ll*(1-ll)+2*ll*zz)*zz-4*jj*DD-2*ss*CC)-2*(ll-1)*CC*zz**2+2*CC**2*zz-2*jj*RR*zz**3+4*jj*DD*zz**2)
M=1280*ll**6-1344*ll**5-8496*ll**4+21020*ll**3-17150*ll**2+5810*ll-693
res=sp.Poly(sp.resultant(II,HH,zz),ll,domain=QQ)
expect=(2*ll-1)**3*(4*ll-1)*(2*ll-3)*CC**4*(2*ll**2-1)*M
assert res.monic()==sp.Poly(expect,ll,domain=QQ).monic()
assert sp.Poly(M,ll,modulus=41).degree()==6
assert sp.Poly(M,ll,modulus=41).is_irreducible
for lam0,root in [(sp.Rational(1,4),0),(sp.Rational(3,2),0),(sp.Rational(1,2),1)]:
 gi=sp.Poly(II.subs(ll,lam0),zz,domain=QQ).gcd(sp.Poly(HH.subs(ll,lam0),zz,domain=QQ)).monic()
 assert gi==sp.Poly(zz-root,zz,domain=QQ)
assert sp.Poly(CC,ll,domain=QQ).gcd(sp.Poly(II,zz).nth(2).as_poly(ll)).degree()==0
K2=QQ.algebraic_field(sp.sqrt(2))
gi=sp.Poly(II.subs(ll,sp.sqrt(2)/2),zz,domain=K2).gcd(sp.Poly(HH.subs(ll,sp.sqrt(2)/2),zz,domain=K2)).monic()
assert gi==sp.Poly(zz-sp.Rational(11,4)+3*sp.sqrt(2)/2,zz,domain=K2)
# At lambda=1/2 or 2lambda^2=1, these common z values are
# z=(2lambda-3)^2/4, i.e. x=y, outside the present distinct-value chart.
alpha=sp.CRootOf(M,0)
K=QQ.algebraic_field(alpha)
assert K.ext.minpoly.degree()==6
lam=K.from_sympy(alpha)
ip=sp.Poly(II.subs(ll,alpha),zz,domain=K)
hp=sp.Poly(HH.subs(ll,alpha),zz,domain=K)
gz=ip.gcd(hp).monic()
assert gz.degree()==1
z0=-K.from_sympy(gz.nth(0))
s0=2*lam-3;A0=2*lam*lam-2*lam+1;C0=-4*lam*lam+5*lam-2;R0=3-4*lam
assert z0 and s0*s0-4*z0
assert A0*A0*z0-A0*C0*s0+C0*C0
l0=(s0*C0-A0*z0)/(z0*z0)
Tm=C0/z0;w0=lam-1-Tm
xx,qq,ff,tt,inv=sp.symbols('x q f t z_sat')
D=K.frac_field(xx,qq)
xv=D.from_sympy(xx);q=D.from_sympy(qq)
def cv(v):return D.convert(v,K)
lamd=cv(lam);zv=cv(z0);sv=cv(s0);lv=cv(l0);tm=cv(Tm);w=cv(w0)
yv=sv-xv
b=(tm-lv*yv)/(xv-yv);c=lv-b;a=1-lv
h=1+xv;k=1+yv
u=b+c*q;V2=b+c*q*q
P0=(b+c*q**3-3*u*V2+2*u**3)/2
X=sp.Poly(xx*xx-K.to_sympy(s0)*xx+K.to_sympy(z0),qq,xx,domain=K)
af=cv(R0)-zv*(lv+u*(q+1-2*u)/q)
Af=sp.Poly(af.numer.as_expr(),qq,xx,domain=K)
DR=D.get_ring()
known=DR.one
for v in [q,q-1,q+1,b,c,u,P0,xv,yv,xv-yv]:
 assert v
 known*=v.numer*v.denom
known2=sp.Poly(known.as_expr(),qq,xx,domain=K).sqf_part()
# Saturate exactly the original nonzero conditions at the parameter
# stage; no generic x or q specialization is made.
param_sat=sp.groebner([X.as_expr(),Af.as_expr(),inv*known2.as_expr()-1],inv,qq,xx,domain=K,order='lex',method='f5b')
source_sha=hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
if len(param_sat.polys)==1 and param_sat.polys[0].total_degree()==0:
 say({'schema':'r150-unit211-S0-IH0-sextic-v1','status':'exact_parameter_fiber_excluded','claimExcluded':True,'claimLambdaLayerEmpty':False,'sourceSha256':source_sha,'sexticIrreduciblePrime':41,'ordinaryISPClaim':False,'peakRssKiB':resource.getrusage(resource.RUSAGE_SELF).ru_maxrss})
 raise SystemExit(0)
parameter_equations=[p.as_expr() for p in param_sat.polys if not p.as_expr().has(inv)]
assert parameter_equations
pg=sp.groebner(parameter_equations,qq,xx,domain=K,order='lex',method='f5b')
say({'stage':'exact_finite_parameter_ideal','sourceSha256':source_sha,'sexticIrreduciblePrime':41,'parameterZeroDimensional':bool(pg.is_zero_dimensional),'basisDegrees':[int(p.total_degree()) for p in pg.polys],'claimExcluded':False})
def C(v):return sp.Poly(D.to_sympy(D.convert(v)),ff,tt,domain=D)
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
W2=C(u*V2-2*u**3+2*lamd*P0)+C(V2+2*u*u)*f-C(b*c*q)*t
bx=C(q/(b*(q-1)))*W1-C(1/(b*(q-1)))*W2
cy=C(1/(c*q*(q-1)))*(W2-W1)
r=bx-C(a)-C(c)*t;s=cy-C(a*q)-C(b)*t
A1=2*f-C(2*b)*bx-C(2*c)*cy+C(2*b*c)*t
rows=[[zero,zero,onep,C(q)],[zero,A1,r,s],[onep,r,zero,t],[C(q),s,t,zero]]
def DK(v):return [tau(mul(row,v)) for row in rows]
d=DK(one);F=half*tau(d)
assert (F-f).is_zero
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
assert (Ps[0]-C(P0)).is_zero and E[0].is_zero and (Ns[0]-C(lamd*P0)).is_zero
pg4=sp.groebner(parameter_equations,ff,tt,qq,xx,domain=K,order='lex',method='f5b')
known4=sp.Poly(known2.as_expr(),ff,tt,qq,xx,domain=K)
def strip(p,unit):
 while not p.is_zero:
  g=p.gcd(unit)
  if g.total_degree()==0:return p.monic()
  p=p.exquo(g)
 return p
def clear_four(po,do_strip=False):
 co=po.rep.to_dict();den=DR.one
 for v in co.values():den=DR.lcm(den,v.denom)
 denp=sp.Poly(den.as_expr(),qq,xx,domain=K)
 assert strip(denp,known2).total_degree()==0
 out={}
 for ij,v in co.items():
  pp=DR.exquo(den,v.denom)*v.numer
  for (xi,qi),cf in pp.items():
   key=(ij[0],ij[1],qi,xi)
   out[key]=out.get(key,K.zero)+cf
 po=sp.Poly.from_dict(out,ff,tt,qq,xx,domain=K)
 rem=sp.Poly(pg4.reduce(po.as_expr())[1],ff,tt,qq,xx,domain=K)
 return strip(rem,known4) if do_strip else rem
VV=[onep,C(w),C(h),C(k)]
for p in [tau(VV)-C(lamd),tau(mul(VV,VV))-C(2*lamd*lamd),tau(mul(mul(VV,VV),VV))-C(4*lamd**3),P(VV),N(VV)]:
 assert clear_four(p).is_zero
conditions=E[1:]+[Ps[1]-C(3*w*P0),Ps[2]-C(h**3*P0),Ps[3]-C(k**3*P0),Ns[1]-C(2*lamd*w*P0),Ns[2]-C(lamd*h*h*P0),Ns[3]-C(lamd*k*k*P0)]
labels=['E1','EB','EC','P1-3wP0','PB-h3P0','PC-k3P0','N1-2lambda*wP0','NB-lambda-h2P0','NC-lambda-k2P0']
polys=[clear_four(p,True) for p in conditions]
input_sha=hashlib.sha256('\n'.join(sp.srepr(p.as_expr()) for p in polys).encode()).hexdigest()
say({'stage':'all_original_equations_verified','sourceSha256':source_sha,'inputSha256':input_sha,'fieldDegree':6,'coversAllSexticEmbeddings':True,'allXandQFibersRetained':True,'conditions':[{'name':n,'degrees':[int(d) for d in p.degree_list()] if not p.is_zero else [-1]*4,'terms':len(p.terms()) if not p.is_zero else 0} for n,p in zip(labels,polys)],'claimExcluded':False})
gb=sp.groebner(parameter_equations+[p.as_expr() for p in polys if not p.is_zero],ff,tt,qq,xx,domain=K,order='grevlex',method='f5b')
excluded=len(gb.polys)==1 and not gb.polys[0].is_zero and gb.polys[0].total_degree()==0
signal.alarm(0)
say({'schema':'r150-unit211-S0-IH0-sextic-v1','status':'exact_original_fiber_excluded' if excluded else 'exact_candidates_not_excluded','claimExcluded':excluded,'claimLambdaLayerEmpty':False,'ordinaryISPClaim':False,'sourceSha256':source_sha,'inputSha256':input_sha,'finalBasis':[{'totalDegree':int(p.total_degree()),'terms':len(p.terms())} for p in gb.polys],'peakRssKiB':resource.getrusage(resource.RUSAGE_SELF).ru_maxrss})
raise SystemExit(0 if excluded else 2)
