#!/usr/bin/env python3
"""New exploration: H 2+1, Hp=0, finite isolated H source, one V source infinity.
Only prints exact eliminant structure and a bounded modular residual probe.
This source makes NO characteristic-zero exclusion claim.
"""
import json,time,hashlib
import sympy as S
from flint import fmpz_mpoly_ctx,nmod_poly
T=time.monotonic()
def out(stage,**kw):
 print(json.dumps(dict(stage=stage,seconds=time.monotonic()-T,**kw),sort_keys=True),flush=True)
def need(b,s):
 if not b:raise AssertionError(s)
s,a,w,e=S.symbols('s a w e')
def q(v):return s**3-5*s**2+(s**3-3*s**2+22*s)*v-(3*s**2+3*s+5)*v*v+(s+1)*v**3
def ker(x,y):
 return S.expand(-(y-x)**2*(x**3-5*x*x+(x**3-3*x*x+22*x)*y-(3*x*x+3*x+5)*y*y+(x+1)*y**3))
ka,kw=ker(s,a),ker(s,w)
J3=5*s*(s+2)*a**3-(11*s**3+18*s*s+8*s+32)*a*a+(4*s**4-6*s**3+34*s*s+76*s)*a+4*s**4-10*s**3-20*s*s
need(S.expand((s+1)*S.diff(ka,s)-ka-(a-s)*J3)==0,"full source derivative divided only by a-s")
E=S.expand((s+1)*ker(w,a)-(w+1)*ka)
C3,rem=S.div(S.Poly(E-(w-s)*(a-s)*J3,w),S.Poly((w-s)**2,w))
need(rem.is_zero,"entire original double-root division")
C3=S.expand(C3.as_expr())
Q=4*e**3-1;D=2*e**3+1-12*e**4;bs=-2*s*s*(s-2)*(s+6)
F1=S.expand(3*D*J3.subs(a,w)**2-2*(2*e**3+1)*Q*bs*(s+1)*(w+1)*q(w))
F2=S.expand(D*(a+1)*kw+4*e*e*Q*(w+1)*ka)
need(S.expand(3*D*(kw-(s+1)*S.diff(kw,s))**2+2*(2*e**3+1)*Q*bs*(s+1)*(w+1)*kw-(w-s)**2*F1)==0,"original scale identity")
ctx=fmpz_mpoly_ctx.get(('s','a','w','e'))
cv=lambda f:ctx.from_dict({m:int(c) for m,c in S.Poly(f,s,a,w,e).terms()})
JJ,CC,FF1,FF2=map(cv,[J3,C3,F1,F2])
def meta(f):
 return dict(degrees=list(map(int,f.degrees())),terms=len(f.to_dict()),sha256=hashlib.sha256(str(f).encode()).hexdigest())
out("inputs",J3=meta(JJ),C3=meta(CC),F1=meta(FF1),F2=meta(FF2))
R1=CC.resultant(FF1,2);out("R1_w",**meta(R1))
R2=CC.resultant(FF2,2);out("R2_w",**meta(R2))
N1=JJ.resultant(R1,1);out("N1_a",**meta(N1))
N2=JJ.resultant(R2,1);out("N2_a",**meta(N2))
G=N1.gcd(N2);out("common",**meta(G))
fac=G.factor();out("common_factorization",content=str(fac[0]),factors=[dict(multiplicity=int(m),polynomial=str(f),**meta(f)) for f,m in fac[1]])
A,r=N1.divmod(G) if hasattr(N1,'divmod') else divmod(N1,G)
B,r2=N2.divmod(G) if hasattr(N2,'divmod') else divmod(N2,G)
need(not r and not r2,"exact residual quotients")
p,ee=1031,700
def spec(f):
 n=max(0,int(f.degrees()[0]));v=[0]*(n+1)
 for m,c in f.to_dict().items():
  need(m[1]==m[2]==0,"only s and e")
  v[m[0]]=(v[m[0]]+int(c)*pow(ee,m[3],p))%p
 return nmod_poly(v,p)
AA,BB=spec(A),spec(B)
out("residual_specialization_probe",prime=p,e=ee,residual_A=meta(A),residual_B=meta(B),specialized_degrees=[int(AA.degree()),int(BB.degree())],resultant=int(AA.resultant(BB)),gcd_degree=int(AA.gcd(BB).degree()))
# One exact lowered-source boundary; still no exclusion asserted here.
need(S.expand(J3.subs(s,-2)-32*(3*a+2))==0,"s=-2 original finite V source")
out("complete_exploration",source_sha256=hashlib.sha256(open(__file__,'rb').read()).hexdigest(),scope="structure only; no full exclusion theorem")
