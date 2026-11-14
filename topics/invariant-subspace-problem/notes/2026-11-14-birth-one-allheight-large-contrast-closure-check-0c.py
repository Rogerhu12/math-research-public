"""Exact algebra for the remaining birth-one P1 domain: delta>0, B<0.
This checks polynomial identities and finite positive coefficient decompositions,
not a parameter scan. Standalone; SymPy only; no external or temporary imports.
"""
import sympy as s
M,N,K,de,v=s.symbols('M N K de v')
m,n=M-1,N-1;HH=M+N
u=(N+de)/M
beta=M*(N+1-K)/(N+de)
eta=m-beta
alpha=n-u*eta
J=K+2*de
Hp=HH+N*eta
Hm=HH+M*u*eta
B=m*HH-N*(M+1)*eta
G=2*HH+eta*(2*N-K)

def eq(a,b=0):assert s.cancel(a-b)==0

eq(J,u*(m+2+eta)-n)
eq(K,n+2-u*(m-eta))
eq(u*beta,N+1-K)
eq(M*alpha,N*(M+1)-m*de-M*K)
eq(u*Hp,N*K+(N+1)*de)
eq(Hm,M*K+m*de)
F=M*N*alpha*(N+1-K)-n*m*K*J
F0=(HH-1)*K*K-N*(2*M*N+HH)*K+N*N*(M+1)*(N+1)
eq(F,F0-m*de*(N*(N+1)+(N-2)*K))
eq(F0.subs(K,2*N/3),-N*N*(8*(M-5)+8*(N-5)+3*(M-5)*(N-5))/9)
eq(F0.subs(K,N+1),-n*m*(N+1)**2)
print('FEASIBLE_DOMAIN_AND_TWO_CONVEX_ENDPOINTS_PASS',flush=True)
S=2*(3*m+2)*beta*Hm-M*m*G
S0=K*((4*M*M-M+1)*N+5*M*M-M-(5*M*M-M)*K)
S1=m*((4*M-2)*(N+1)-(5*M-1)*K)
eq(u*S,S0+de*S1)
S0lower=N*(2*M*M-M+3)/3+5*M*M-M
S1lower=(2*M-4)*N/3+4*M-2
eq((S0/K).subs(K,2*N/3),S0lower)
eq((S1/m).subs(K,2*N/3),S1lower)
print('S_POSITIVE_DECOMPOSITION_PASS',flush=True)

# The exact P1 Laurent numerator from the published actual normalization.
t=m*K/(beta*(de+N*v))
Laurent=u*M*beta*J*Hp*t-J*K*B-M*N*de*G+N*(3*m+2)*K*Hm/t
Q2=N**3*(3*m+2)*beta*Hm/m
Q1=N*(-J*K*B+N*de*S/m)
Q0=u*M*m*J*Hp*K-J*K*B*de-M*N*de**2*G+N*(3*m+2)*beta*Hm*de**2/m
eq((de+N*v)*Laurent,Q0+Q1*v+Q2*v*v)
C0=K**3*M*N*N*m*m
C1=K*K*M*N*m*(2*M*K+N*(3*M-5)-M-1)
C2=K*M*N*((4*M*M-8*M+2)*K+(3*M*M-8*M+7)*N+2)
C3=M*N*m*(2*K*(M-2)+m*(N+1))
eq(m*(N+de)*Q0,C0+C1*de+C2*de**2+C3*de**3)
print('FULL_V_QUADRATIC_AND_ALL_FOUR_CONSTANT_COEFFICIENTS_PASS',flush=True)

# All residual brackets are positive for M,N>=5, K>0, with explicit anchors.
x,y=s.symbols('x y')
positive=[S0lower,S1lower,2*M*K+N*(3*M-5)-M-1,4*M*M-8*M+2,3*M*M-8*M+7,2*K*(M-2)+m*(N+1)]
for expr in positive:
 pp=s.Poly(s.expand(expr.subs({M:5+x,N:5+y})),x,y,K)
 assert all(c>0 for c in pp.coeffs())
 assert pp.eval({x:0,y:0,K:0})>0
print('ALL_SIX_RESIDUAL_BRACKETS_STRICTLY_POSITIVE_ON_FULL_ORTHANT',flush=True)
print('ALL_PASS',flush=True)
