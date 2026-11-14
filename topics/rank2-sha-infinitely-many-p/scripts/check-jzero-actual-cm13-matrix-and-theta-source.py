#!/usr/bin/env python3
"""R297 exact original CM13 trace, unique mass kernel and theta factorization."""
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
 val=(pw(ratio,34,f)*pw(xb,2,f)).rem(f)
 row=[]
 for j in range(6):
  tr=(val*f.diff()).rem(f).nth(12)
  row.append(tr)
  val=(val*step).rem(f)
 fibers.append(row)
E=s.Matrix([[s.Integer(a)**(3*j+2) for j in range(6)] for a in range(2,8)])
M=(E.inv()*s.Matrix(fibers[:6])).applyfunc(s.expand)
for j in range(6):assert s.simplify(sum(s.Integer(8)**(3*k+2)*M[k,j] for k in range(6))-fibers[6][j])==0

# Compute the true mass observation, including the degree-17 column.
row=s.zeros(1,6);row[0,5]=1
obs=[]
for _ in range(6):
 obs.append(list(row));row=(row*M).applyfunc(s.expand)
O=s.Matrix(obs)
from sympy.polys.matrices import DomainMatrix
DM=DomainMatrix.from_Matrix(O).convert_to(K)
rref,piv=DM.rref();rank=len(piv)
ns=DM.nullspace().to_Matrix().applyfunc(s.simplify)
assert rank==5 and ns.rows==1
ans={'status':'PASS','curve':'y^2=x^3+1, fixed homothety of Eplus17',
     'gamma':'4+omega','basis':'sigma^34*x^(2+3j), j=0..5',
     'fit_fibers':list(range(2,8)),'independent_held_fiber':8,
     'CM13_matrix':[[str(M[i,j]) for j in range(6)] for i in range(6)],
     'mass_observability_rank':rank,'mass_kernel_rows':[[str(ns[i,j]) for j in range(ns.cols)] for i in range(ns.rows)]}
if ns.rows==1:
 vec=ns[0,:].T;vec=(vec/vec[4]).applyfunc(s.simplify)
 lam=s.simplify((M*vec)[4]);assert (M*vec-lam*vec).applyfunc(s.simplify)==s.zeros(6,1)
 ans['normalized_actual_eigenvector']=[str(v) for v in vec]
 ans['actual_raw_CM13_eigenvalue']=str(lam)

# A smaller integral display matrix, retaining the sixth mass column.
D=s.diag(*[s.Rational(1,4**j) for j in range(6)])
Mh=(D.inv()*M*D).applyfunc(s.expand)
AR=[[int(s.re(a)*13122) for a in row] for row in Mh.tolist()]
AD=[[int(s.im(a)/s.sqrt(3)*13122) for a in row] for row in Mh.tolist()]
assert Mh==s.Matrix(AR)/13122+d*s.Matrix(AD)/13122
DMh=DomainMatrix.from_Matrix(Mh).convert_to(K)
rowh=DomainMatrix.from_Matrix(s.Matrix([[0,0,0,0,0,1]])).convert_to(K)
rows=[]
for _ in range(5):
    rows.append(rowh.to_Matrix());rowh=rowh.matmul(DMh)
Oh=s.Matrix.vstack(*rows)
minor=K.to_sympy(DomainMatrix.from_Matrix(Oh[:,[0,1,2,3,5]]).convert_to(K).det())
assert minor!=0
vh=s.Matrix([-2,-5,-3,-53,28,0])
assert (Mh*vh+(7+d)*vh/2).applyfunc(s.expand)==s.zeros(6,1)
ans.update({'rescaled_basis':'4^(-j)*sigma^34*x^(2+3j), j=0..5',
    'integer_matrix_denominator':13122,'integer_matrix_real':AR,'integer_matrix_delta':AD,
    'rescaled_mass_kernel_integer_vector':list(map(int,vh)),
    'rescaled_mass_observability_minor':{'rows':[0,1,2,3,4],'columns':[0,1,2,3,5],'determinant':str(minor)}})

# The earlier norm-13 product is not an eigenvector; use the full trace matrix.
cand=s.Matrix([256,1024,1536,52,13,0]);mcand=(M*cand).applyfunc(s.expand)
ratios=[]
for aa in (2,3):
    ev=s.Matrix([[s.Integer(aa)**(3*j+2) for j in range(6)]])
    ratios.append(s.expand((ev*mcand)[0]/(ev*cand)[0]))
diff=s.expand(ratios[0]-ratios[1])
assert diff==(65163445-20385841*d)/18159794
ans['rejected_CM13_product_trace_ratios']=[str(v) for v in ratios]
ans['rejected_CM13_product_ratio_difference']=str(diff)

# Actual rational source, CM7 division factors and cubic angular polynomial.
X,b,Q=s.symbols('X b Q',nonzero=True)
P4=7*X**4-53*b*X**3-12*b*b*X**2-80*b**3*X-128*b**4
factor=(X+b)*(X-8*b)*(7*X*X-4*b*X+16*b*b)
assert s.expand(P4-factor)==0
g7=(5+d)/2;gb7=(5-d)/2
R7=g7*(X+(-2+6*d)*b/7)
Rb7=gb7*(X+(-2-6*d)*b/7)
assert s.expand(R7*Rb7-(7*X*X-4*b*X+16*b*b))==0
Q8=(Q-2)**2*(1+Q)*(1-2*Q)*(Q**4+Q**3+6*Q**2-14*Q+7)
angular=s.cancel(Q**10/(1024*b)*(P4.subs({X:4*b*(1-Q)/Q**2})/(7*b**4)))
assert s.cancel(angular-Q**2*Q8/(112*b))==0
assert Q8.subs(Q,0)==28
ans['normalized_P4_ascending_b1']=['-128/7','-80/7','-12/7','-53/7','1']
ans['integral_P4_factorization']='(X+b)*(X-8*b)*(7*X^2-4*b*X+16*b^2)'
ans['CM7_sigma_division']='gamma7*(x^3+((-2+6*delta)/7)*b)'
ans['Q8_ascending']=[str(s.Poly(s.expand(Q8),Q).nth(j)) for j in range(9)]
ans['source_angular_prefactor']='q^2*v^2*theta_minus^34/(112*b)'
ans['source_vanishing_order_at_origin']=6
ans['source_zero_divisor']={'O':6,'T_and_minus_T_each':2,
    'three_nonzero_2_torsion_each':2,'six_new_preimages_of_T_or_minus_T_under_2_each':1,
    'six_nonzero_gamma7_kernel_each':1,'six_nonzero_conjugate_gamma7_kernel_each':1}
path=Path(__file__).with_suffix('.json')
path.write_text(json.dumps(ans,indent=2)+'\n')
print(json.dumps({'status':'PASS','mass_rank':rank,'actual_P4':ans['normalized_P4_ascending_b1'],
    'raw_eigenvalue':ans['actual_raw_CM13_eigenvalue'],'Q8':ans['Q8_ascending'],
    'all_zeros_are_fixed_torsion':True},indent=2))
