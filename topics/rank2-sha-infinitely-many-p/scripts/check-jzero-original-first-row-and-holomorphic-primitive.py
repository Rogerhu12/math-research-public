#!/usr/bin/env python3
"""R305 exact original first-row formulas, holomorphic primitive and CM13 boundary."""
import sympy as s,json
from pathlib import Path
x=s.symbols('x');d=s.sqrt(-3);w=(-1+d)/2
K=s.QQ.algebraic_field(d)
P=lambda q:s.Poly(q,x,domain=K)
g=4+w;gb=4+s.conjugate(w)
q=P(g*(x**6+(8+12*w)*x**3+s.Rational(64,13)+s.Rational(48,13)*w))
qb=P(gb*(x**6+(8+12*s.conjugate(w))*x**3+s.Rational(64,13)+s.Rational(48,13)*s.conjugate(w)))
B=P(x**3+1)
num=P(13*x)*q**2-4*B*(q.diff().diff()*q-q.diff()**2)-P(6*x*x)*q.diff()*q
den=(q**2).mul_ground(g*g)
numb=P(13*x)*qb**2-4*B*(qb.diff().diff()*qb-qb.diff()**2)-P(6*x*x)*qb.diff()*qb
denb=(qb**2).mul_ground(gb*gb)
c=s.polys.polytools.gcd(num,den);num=num.exquo(c);den=den.exquo(c)
c=s.polys.polytools.gcd(numb,denb);numb=numb.exquo(c);denb=denb.exquo(c)

def pw(a,n,f):
 r=P(1)
 while n:
  if n&1:r=(r*a).rem(f)
  a=(a*a).rem(f);n>>=1
 return r

fibers=[]
for a in range(2,9):
 f=(num-den.mul_ground(a)).monic()
 assert f.degree()==13 and s.polys.polytools.gcd(f,f.diff()).degree()==0
 ratio=(qb*s.invert(q,f)).rem(f)
 xb=(numb*s.invert(denb,f)).rem(f)
 step=pw(xb,3,f)
 val=(pw(ratio,34,f)*pw(xb,1,f)).rem(f)
 row=[]
 for j in range(6):
  tr=(val*f.diff()).rem(f).nth(12)
  row.append(tr)
  val=(val*step).rem(f)
 fibers.append(row)
E=s.Matrix([[s.Integer(a)**(3*j+1) for j in range(6)] for a in range(2,8)])
M=(E.inv()*s.Matrix(fibers[:6])).applyfunc(s.expand)
for j in range(6):assert s.simplify(sum(s.Integer(8)**(3*k+1)*M[k,j] for k in range(6))-fibers[6][j])==0

from sympy.polys.matrices import DomainMatrix
checks=[]
def ck(name, condition):
    assert condition, name
    checks.append(name)

t,b,X,n,N,u,zz=s.symbols('t b X n N u zz',nonzero=True)
A=(1-t)*(1+8*t)*(1+s.Rational(4,7)*t+s.Rational(16,7)*t*t)
P4=(X+b)*(X-8*b)*(X*X-s.Rational(4,7)*b*X+s.Rational(16,7)*b*b)
ck('actual_fourth_angular_factor',s.cancel(P4.subs(X,-b/t)/(-b/t)**4-A)==0)
ck('five_term_coefficients',[s.expand(A).coeff(t,j) for j in range(5)]==[1,s.Rational(53,7),-s.Rational(12,7),s.Rational(80,7),-s.Rational(128,7)])
Q=s.symbols('Q')
Q8=(Q-2)**2*(1+Q)*(1-2*Q)*(Q**4+Q**3+6*Q*Q-14*Q+7)
tt=-Q**2/(4*(1-Q))
ck('original_Q8_even_angular_transport',s.cancel(A.subs(t,tt)-Q8/(28*(1-Q)**4))==0)
# The last check is entirely rational: Theta17 = theta_minus34*(1-q)^(17/3),
# while G = theta_minus34*(1-q)^(5/3)*Q8/28.

du=s.sqrt(1+b*u**6)
V=2*zz-2*du/u
DV=s.diff(V,u)*du+s.diff(V,zz)*(-u**-2)
ck('actual_theta_second_derivative',s.simplify(DV+4*b*u**4)==0)
dt=s.diff(-b*u**6,u)*du
d2t=s.diff(dt,u)*du
ck('theta_angle_first_derivative_square',s.expand(dt**2-36*b*b*u**10*(1+b*u**6))==0)
ck('theta_angle_second_derivative',s.simplify(d2t+6*b*u**4*(5+8*b*u**6))==0)
ck('theta_hypergeometric_recurrence',s.cancel((n-1)*(n-s.Rational(2,3))/(n*(n-s.Rational(1,6)))-(n-1)/n*(s.Rational(1,3)+n-1)/(s.Rational(5,6)+n-1))==0)
ck('theta_hypergeometric_initial_value',s.Rational(1,3)*(s.Rational(1,3)/s.Rational(5,6))==s.Rational(2,15))
# Formal Lagrange powers: 6s=p+1, so Jacobian kernel exponent is -p-2.
ss,pp=s.symbols('s p',integer=True,positive=True)
ck('lagrange_jacobian_exponent',(6*ss+1).subs(ss,(pp+1)/6)==pp+2)
ck('lagrange_derivative_exponent',(6*ss).subs(ss,(pp+1)/6)==pp+1)
ck('first_weight_normalization',s.simplify((-b)**ss*(-1/b)-(-b)**(ss-1))==0)

# Full original covariant primitive, with the five actual rational inputs.
Mb=s.zeros(6,5)
for k in range(5):
    nn=-1-3*k
    Mb[k,k]=2*nn*(2*nn+1)
    Mb[k+1,k]=4*nn*(nn-1)*b
vsrc=s.Matrix([0,1,-s.Rational(53,7)*b,-s.Rational(12,7)*b*b,-s.Rational(80,7)*b**3,-s.Rational(128,7)*b**4])
acoef=s.Matrix([s.Rational(8991,24640)/b,-s.Rational(5911,172480),-s.Rational(801,30184)*b,s.Rational(6,539)*b*b,-s.Rational(16,637)*b**3])
beta=-s.Rational(8991,12320)/b
ck('actual_covariant_primitive_identity',Mb*acoef+beta*s.eye(6)[:,0]==vsrc)
ck('primitive_and_mass_column_unique',s.factor(Mb.row_join(s.eye(6)[:,0]).det())!=0)
ck('complete_origin_mass',2*acoef[0]+beta==0)
ck('beta_exact_factorization',s.cancel(beta+3**5*37/(s.Integer(2)**5*5*7*11*b))==0)
ck('primitive_holomorphic_and_exact_order_two',[17+(-1-3*k) for k in range(5)]==[16,13,10,7,4])

# Full Euler transposition, including all theta connection products.
ww=s.symbols('ww');gg=s.Function('g')(ww);WW=s.Function('W')(ww)
EE=lambda f:6*ww*s.diff(f,ww)
inside=EE(gg)+(2-WW)*gg
trans=EE(inside)+(1-WW)*inside
expanded=EE(EE(gg))+3*EE(gg)+2*gg-2*WW*EE(gg)-(EE(WW)+3*WW-WW**2)*gg
ck('full_Euler_transpose',s.expand(trans-expanded)==0)
ii=s.symbols('i',integer=True)
ck('exact_weight_convolution',12*(n-ii)+6*ii+3==12*n-6*ii+3)
ck('true_first_resonance_cancellation',s.expand((6*ss+1)*(6*ss+2)-6*ss*(6*ss+3)-2)==0)

# Independent fixed CM13 matrix and the original primitive's actual orbit.
DM=DomainMatrix.from_Matrix(M).convert_to(K)
v=s.Matrix([0,-s.Rational(16,637),s.Rational(6,539),-s.Rational(801,30184),-s.Rational(5911,172480),s.Rational(8991,24640)])
dv=DomainMatrix.from_Matrix(v).convert_to(K)
cols=[]
for _ in range(6):
    cols.append(dv.to_Matrix());dv=DM.matmul(dv)
Kr=DomainMatrix.from_Matrix(s.Matrix.hstack(*cols)).convert_to(K)
krank=len(Kr.rref()[1])
ck('actual_C_full_six_dimensional_CM13_orbit',krank==6)
krdet=K.to_sympy(Kr.det())
row=DomainMatrix.from_Matrix(s.Matrix([[0,0,0,0,0,1]])).convert_to(K)
obs=[]
for _ in range(6):
    obs.append(row.to_Matrix());row=row.matmul(DM)
Ob=DomainMatrix.from_Matrix(s.Matrix.vstack(*obs)).convert_to(K)
orank=len(Ob.rref()[1])
ck('actual_order_two_mass_observation_rank',orank==6)
T=s.symbols('T')
cp=sum(K.to_sympy(c)*T**(6-i) for i,c in enumerate(DM.charpoly()))
ck('exact_CM13_characteristic_polynomial',s.expand(cp-(T**3+g**3)*(T**3+w*g**3))==0)
mv=(M*v).applyfunc(s.expand)
d0=(-s.Integer(1111349706)+s.Integer(4877443430)*d)/59594535
ck('actual_CM13_boundary_coefficient',s.expand(mv[0]-d0)==0)
ck('boundary_inert_unit_gcd',s.igcd(1111349706,4877443430)==2)
ck('boundary_exact_denominator',59594535==3**5*5*7**3*11*13)
ck('true_boundary_pole_order_coefficients',2*(-16)*(-31)==992 and 4*(-16)*(-17)==1088)
ck('primitive_is_not_a_CM13_eigenvector',mv[0]!=0 and v[0]==0)

ans={'status':'PASS','exact_checks':len(checks),'checks':checks,
     'original_first_row':{
       'coordinate':'t=-b/x^3, p=6s-1, S=-t*Theta^17*A(t)/b',
       'angular_coefficients':[str(s.expand(A).coeff(t,j)) for j in range(5)],
       'h_coefficients':'(1/2)_n/(n!*(6*n+1))',
       'log_Theta17_coefficients':'17/(3*n)*(1/3)_n/(5/6)_n',
       'exact_kernel':'(-b)^(s-1)*[t^(s-1)]Theta^17*A(t)*(1-t)^(-1/2)*h^(-p-2)',
       'mod_p2':'s_(p+1)=T_p-p*L_p mod p^2; L_p uses the same original log(h)'},
     'covariant_matrix':[[str(z) for z in rr] for rr in Mb.tolist()],
     'primitive_coefficients':[str(z) for z in acoef],
     'beta':str(beta),'primitive_basis':'F*x^(-1-3k),k0..4; equivalently sigma34*x^(16-3k)',
     'CM13_basis':'sigma34*x^(1+3j),j0..5, b=1',
     'CM13_matrix':[[str(z) for z in rr] for rr in M.tolist()],
     'fit_complete_fibers':list(range(2,8)),'independent_complete_fiber':8,
     'CM13_characteristic_polynomial':'(T^3+gamma13^3)*(T^3+omega*gamma13^3)',
     'C_vector':[str(z) for z in v], 'C_krylov_rank':krank,
     'C_krylov_determinant':str(krdet),'order_two_mass_observability_rank':orank,
     'order_two_mass_observability_determinant':str(K.to_sympy(Ob.det())),
     'actual_CM13_C_image':[str(z) for z in mv],
     'boundary_coefficient':str(d0),'boundary_integer_pair_gcd':2,
     'boundary_after_covariant_square':'d0*sigma34*(992*x^2+1088*b/x)',
     'no_target_prime_scan':True}
Path(__file__).with_suffix('.json').write_text(json.dumps(ans,indent=2)+'\n')
print(json.dumps({'status':'PASS','exact_checks':len(checks),'C_krylov_rank':krank,
                  'order_two_mass_observability_rank':orank,'beta':str(beta),
                  'actual_CM13_boundary':str(d0)},indent=2))

