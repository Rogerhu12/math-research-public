"""Exact symbolic checks for the normalized birth-one middle quartic coefficient.
All variables are formal; no numerical samples are used.
"""
import sympy as s
n,m,u,e,t=s.symbols('n m u e t',positive=True)
a0=n-u*e;b0=m-e;M=m+1;N=n+1
J=u*(e+m+2)-n;K=n+2-u*(m-e);V=1+u*(e+1)
a=(m+2)/a0;c=N/M;d=c*(n+2)/b0
X=1-a*u;Y=d/(c*u)-1
ell=-n*X/(M*u);kap=m*u*Y/N;A=c/u
R=A-ell*t;T=1/A-kap/t
L0=a*c-1;L1=a*d-c;L2=d-c*c
xx=e*X*X/M;yy=e*Y*Y/M;xy=e*X*Y/M
kp=ell*u*u*(L0+L1/c)-xx*u*(c+d/c)
km=kap*(c*L1+L2)-yy*u*u*(a*c+1)
kz=L0*u*u*(1-A)-L1*u*ell*kap+L2*(1-1/A)+xx*d*kap+yy*a*u**3*ell-2*u*(u+c)*xy-u*u*xx*yy
D=b0*M*M*a0;Hp=M+N+e*N;Hm=M+N+e*u*M;C0=V+3*(n+m)+4
Np=u*(2*M+b0)*J*Hp;Nm=(2*N+a0)*K*Hm
Nz=-C0*J*K+V*(J*b0*(u*e+1)+K*u*(m+2)*(e+1))
for label,lhs,rhs in [('outer_plus',D*kp,Np),('outer_minus',D*km,Nm),('constant_positive_split',D*kz,Nz),('feasibility_identity',ell*kap,n*m*J*K/(M*N*u*a0*b0))]:
 assert s.cancel(lhs-rhs)==0,label
 print('PASS',label,flush=True)
# Independently extract the universal P2 coefficient before substitutions.
a_,b_,c_,d_,p,q,r,ss,x2,y2,xy_=s.symbols('a b c d p q r ss x2 y2 xy')
Lc=[a_*c_-b_*b_,a_*d_-b_*c_,b_*d_-c_*c_]
Fc=[p*q*(q*ss-r*r),q*r*(p*ss-q*r),r*ss*(p*r-q*q)]
P2=sum(q*Lc[i]*Fc[2-i] for i in range(3))-p*q**3*r*(c_*ss+d_*r)*x2-q*q*r*r*ss*(a_*q+b_*p)*y2-2*p*q*q*r*ss*(b_*r+c_*q)*xy_-p*q**3*r*r*ss*x2*y2
# Remove the p=1/(uR), q=1, r=u, ss=u²/T monomial denominator first.
RR,TT,aa,cc,dd,XX,YY,XY=s.symbols('RR TT aa cc dd XX YY XY')
normal=s.cancel(P2.subs({a_:aa,b_:1,c_:cc,d_:dd,p:1/(u*RR),q:1,r:u,ss:u*u/TT,x2:XX,y2:YY,xy_:XY})*RR*TT/u)
expected=(aa*cc-1)*u*u*(1-RR)+(aa*dd-cc)*u*(1-RR*TT)+(dd-cc*cc)*(1-TT)-(cc*u+dd*TT)*XX-u*u*(aa*u*RR+1)*YY-2*u*(u+cc)*XY-u*u*XX*YY
assert s.expand(normal-expected)==0
print('PASS universal_middle_coefficient',flush=True)
# Check the Laurent step before the rational physical specialization.
Av,lv,kv,hxv,hyv,hxyv=s.symbols('Av lv kv hxv hyv hxyv',nonzero=True)
rv=Av-lv*t;tv=1/Av-kv/t
l0=aa*cc-1;l1=aa*dd-cc;l2=dd-cc*cc
center=expected.subs({RR:rv,TT:tv,XX:hxv*t,YY:hyv/t,XY:hxyv})
gp=lv*u*u*l0+lv*u*l1/Av-hxv*(cc*u+dd/Av)
gm=kv*u*Av*l1+kv*l2-hyv*u*u*(aa*u*Av+1)
gz=l0*u*u*(1-Av)-l1*u*lv*kv+l2*(1-1/Av)+hxv*dd*kv+hyv*aa*u**3*lv-2*u*(u+cc)*hxyv-u*u*hxv*hyv
assert s.expand(center-(gp*t+gz+gm/t))==0
assert s.cancel(gp.subs(Av,cc/u)-(lv*u*u*(l0+l1/cc)-hxv*u*(cc+dd/cc)))==0
assert s.cancel(gm.subs(Av,cc/u)-(kv*(cc*l1+l2)-hyv*u*u*(aa*cc+1)))==0
print('PASS laurent_identity',flush=True)
print('ALL_PASS: normalized full P2 identities and positive numerator split; strict positivity follows from the analytic inequalities in the proof.',flush=True)
