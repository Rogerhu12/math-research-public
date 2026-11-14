import sympy as s
z,w=s.symbols('z w')
T=lambda p:s.expand(z*s.diff(p,z))
V=3*z+4*z*z+3*z**3;W=1+z+z*z+z**3;R=3+4*z+3*z*z
TW=s.expand(W*T(T(W))-T(W)**2)
U=s.det(s.Matrix([[T(T(W)) if i+j==2 else sum(r**(i+j)*z**r for r in range(4)) for j in range(3)] for i in range(3)]))
TV=s.expand(V*T(T(V))-T(V)**2);TR=s.expand(R*T(T(R))-T(R)**2)
a=12*z*z*(1+z);b=TV/V;c=U/TW;d=TR/R
p=V;q=TW/W;r=R
x=1-2*T(V)/V+T(TW)/TW
y=2*T(TW)/TW-T(V)/V-T(R)/R-3
Lam=[a*c-b*b,a*d-b*c,b*d-c*c]
F=[p*(p*r-q*q),p*q*r,q*q*r]
P=[sum(p*Lam[j]*F[k-j] for j in range(3) if 0<=k-j<3) for k in range(5)]
# subtract w p^3 q(c+wd)(q+wr)x^2
# subtract w p^2 q^2 r(a+wb)y^2
# subtract 2w p^2 q r(b+wc)(p+wq)xy
# subtract w^2 p^3 q^2 r x^2y^2
P[1]-=p**3*q*c*q*x*x+p*p*q*q*r*a*y*y+2*p*p*q*r*b*p*x*y
P[2]-=p**3*q*(c*r+d*q)*x*x+p*p*q*q*r*b*y*y+2*p*p*q*r*(b*q+c*p)*x*y+p**3*q*q*r*x*x*y*y
P[3]-=p**3*q*d*r*x*x+2*p*p*q*r*c*q*x*y
for i,e in enumerate(P):
 ee=s.cancel(e);num,den=s.fraction(ee);pn=s.Poly(num,z);pd=s.Poly(den,z)
 print('i',i,'numdeg',pn.degree(),'dendeg',pd.degree(),'negative',sum(1 for c in pn.all_coeffs() if c<0),'dennegative',sum(1 for c in pd.all_coeffs() if c<0),flush=True)
 print('num=',s.factor(num),flush=True);print('den=',s.factor(den),flush=True)
 assert all(c>=0 for c in pn.all_coeffs()) and any(c>0 for c in pn.all_coeffs())
 assert all(c>=0 for c in pd.all_coeffs()) and any(c>0 for c in pd.all_coeffs())
print('PASS q3 delta1 h3 all z,w',flush=True)
