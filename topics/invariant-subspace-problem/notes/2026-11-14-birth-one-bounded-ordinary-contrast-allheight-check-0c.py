"""Exact identities used by the all-height bounded-ordinary-contrast proof.
The positivity proof itself is analytic; this file verifies finite rational identities.
"""
import sympy as s
n,m,u,e,t=s.symbols('n m u e t',positive=True);M=m+1;N=n+1;H=M+N
al=n-u*e;be=m-e;J=u*(m+2+e)-n;K=n+2-u*(m-e);de=M*u-N
Hp=H+N*e;Hm=H+M*u*e;B=m*H-N*(M+1)*e;G=2*H+e*(n+m*u-u*e)
a=(m+2)/al;c=N/M;d=c*(n+2)/be;A=c/u
X=-J/al;Y=K/(u*be);ell=-n*X/(M*u);kap=m*u*Y/N;R=A-ell*t;T=1/A-kap/t
L0=a*c-1;L1=a*d-c
cp=L0*u*u*ell/A-c*u*e*X*X/(M*A)
cm=L0*u*u*A*kap+L1*u*kap-a*u**3*e*Y*Y/M
cz=-L0*u*u*ell*kap+L1*u*(1-1/A)+c*u*e*kap*X*X/M-2*u*u*e*X*Y/M
D1=al*be*M*M*N/u
wanted=u*M*be*J*Hp*t-J*K*B-M*N*de*G+N*(3*m+2)*K*Hm/t
for name,left,right in [("positive_t",D1*cp,u*M*be*J*Hp),("constant",D1*cz,-J*K*B-M*N*de*G),("positive_inverse_t",D1*cm,N*(3*m+2)*K*Hm)]:
 assert s.cancel(left-right)==0
 print("COEFFICIENT_IDENTITY_PASS",name,flush=True)
Remainder=(3*m+2)*be*Hm-M*m*G
assert s.cancel(Remainder-(m*B+2*M*e*(N*m-M*K)))==0
rewritten=u*M*be*J*Hp*t-J*K*B+N*K*Remainder/(be*t)+M*N*N*G*(1-T)
assert s.cancel(de-(m*K/(be*t)-N*(1-T)))==0
assert s.cancel(ell*kap-n*m*J*K/(M*N*u*al*be))==0
# Reduced domain polynomial and its two monotonic parameters.
delta,kk=s.symbols('delta kk',nonnegative=True)
u1=(N+delta)/M;aa=(N*(M+1)-m*delta-M*kk)/M
F=M*N*aa*(N+1-kk)-n*m*kk*(kk+2*delta)
F0=N*N*(M+1)*(N+1)-N*(2*M*N+H)*kk+(H-1)*kk*kk
assert s.expand(F-(F0-m*delta*(N*(N+1)+(N-2)*kk)))==0
at=s.factor(F.subs({kk:N*m/M,delta:0}))
assert s.cancel(at-N*N/M**2*(2*M*H-n*m**3))==0
xx,yy=s.symbols('xx yy',nonnegative=True)
gap=s.Poly(s.expand((n*m**3-2*M*H).subs({n:3+xx,m:3+yy})),xx,yy)
assert all(v>0 for v in gap.coeffs()) and gap.coeff_monomial(1)==17
print('P1_REWRITING_AND_DOMAIN_LEMMA_PASS',len(gap.terms()),flush=True)
# Exact quartic reciprocity for arbitrary formal positive norm variables.
a,c,d,p,u,ss,xx,yy,xy=s.symbols('a c d p u ss xx yy xy',nonzero=True)
def coeffs(a,c,d,p,u,ss,xx,yy,xy):
 la=[a*c-1,a*d-c,d-c*c]
 ph=[p*(ss-u*u),u*(p*ss-u),u*ss*(p*u-1)]
 co=[sum(la[i]*ph[k-i]for i in range(3)if 0<=k-i<3)for k in range(5)]
 for fac,A0,B0 in [(p*u*xx,[c,d],[u,ss]),(u*u*ss*yy,[a,1],[p,1]),(2*p*u*ss*xy,[1,c],[1,u])]:
  for i in range(2):
   for j in range(2):co[i+j+1]-=fac*A0[i]*B0[j]
 co[2]-=p*u*u*ss*xx*yy
 return co
co=coeffs(a,c,d,p,u,ss,xx,yy,xy)
ref=coeffs(d/c,1/c,a/c,ss/u,1/u,p/u,u*yy/c,u*xx/c,u*xy/c)
for k in range(5):assert s.cancel(co[k]-u**4*c*c*ref[4-k])==0
print('ALL_FIVE_COEFFICIENT_RECIPROCITY_IDENTITIES_PASS',flush=True)
print('ALL_PASS',flush=True)
