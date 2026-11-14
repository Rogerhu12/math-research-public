import sympy as s
M,N,K,delta=s.symbols("M N K delta",positive=True)
m=M-1;n=N-1;H=M+N
u=(N+delta)/M;beta=(N+1-K)/u;eta=m-beta;alpha=n-u*eta
J=K+2*delta;Hp=H+N*eta;Hm=H+M*u*eta
B=m*H-N*(M+1)*eta;G=2*H+eta*(n+m*u-u*eta)
S=2*(3*m+2)*beta*Hm-M*m*G
Snum=K*((4*M*M-M+1)*N+5*M*M-M-(5*M*M-M)*K)+m*delta*((4*M-2)*(N+1)-(5*M-1)*K)
assert s.cancel(u*S-Snum)==0
F0=N*N*(M+1)*(N+1)-N*(2*M*N+H)*K+(H-1)*K*K
assert s.factor(F0.subs(K,2*N/3)+N*N*(8*(M-5)+8*(N-5)+3*(M-5)*(N-5))/9)==0
assert s.factor(F0.subs(K,N+1)+n*m*(N+1)**2)==0
Q0=u*M*m*J*Hp*K-J*K*B*delta-M*N*delta**2*G+N*(3*m+2)*beta*Hm*delta**2/m
C=[K**3*M*N*N*m*m,K*K*M*N*m*(2*M*K+N*(3*M-5)-M-1),K*M*N*((4*M*M-8*M+2)*K+(3*M*M-8*M+7)*N+2),M*N*m*(2*K*(M-2)+m*(N+1))]
assert s.cancel(m*(N+delta)*Q0-sum(C[i]*delta**i for i in range(4)))==0
v=s.symbols("v",nonnegative=True)
t=m*K/(beta*(delta+N*v))
raw=u*M*beta*J*Hp*t-J*K*B-M*N*delta*G+N*(3*m+2)*K*Hm/t
q1=N*(-J*K*B+N*delta*S/m);q2=N**3*(3*m+2)*beta*Hm/m
assert s.cancel((delta+N*v)*raw-(Q0+q1*v+q2*v*v))==0
print("ALL_PASS: strong K bound, full S identity, four constant coefficients, complete v quadratic")
