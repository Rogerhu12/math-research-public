#!/usr/bin/env python3
"""R319: actual norm-three return, full conductor and mixed scaling carry."""
import json
from pathlib import Path
import sympy as s

t, X, Y, Z = s.symbols('t X Y Z')
a = 16*t**4-12*t**3+3*t**2-7*t
b0 = 256*t**4+1472*t**3-1200*t**2+200*t+1
c = -128*t**4-832*t**3+1968*t**2-280*t+1
g2 = 8*t*t+20*t-1
d = t*(t-1)*g2*g2
u = 1-4*t
tau = -27*t/u**3
R = u**14*(u**3-216*t)/(1+8*t)**3
K3 = (-48*X+5*Y+4*Z)/9
Kt = (Y+Z)/2
Kdelta = (4608*X**2-1392*X*Y-1776*X*Z
          +41*Y**2+77*Y*Z+44*Z**2)/162
Ks = (24*X+2*Y+Z)/3
Fstar = Z-Y-48*X
checks = []
def ck(name, value):
    assert value, name
    checks.append(name)
def sub(P):
    return s.expand(P.subs({X:a,Y:b0,Z:c}))
def remrat(f, modulus=g2):
    num, den = s.fraction(s.cancel(f))
    return s.rem(num*s.invert(den,modulus,t),modulus,t)
def matrix(n):
    exponents = [(i,j,n-i-j) for i in range(n+1) for j in range(n-i+1)]
    polys = [s.Poly(a**i*b0**j*c**k,t) for i,j,k in exponents]
    return exponents, s.Matrix([[P.nth(r) for P in polys] for r in range(4*n+1)])
def represent(P,n):
    P=s.Poly(s.cancel(P),t)
    assert P.degree()<=4*n
    exponents,M=matrix(n)
    target=s.Matrix([P.nth(r) for r in range(4*n+1)])
    sol,pars=M.gauss_jordan_solve(target)
    sol=sol.subs(dict.fromkeys(pars,0))
    assert M*sol==target
    return s.factor(sum(v*X**i*Y**j*Z**k for v,(i,j,k) in zip(sol,exponents)))

ck('actual_norm_three_parameter',s.cancel(tau+27*t/(1-4*t)**3)==0)
ck('node_second_preimage',s.factor(tau-1-(t-1)*(1+8*t)**2/(1-4*t)**3)==0)
ck('tacnode_branches_are_exchanged',s.expand(remrat(tau)+t+s.Rational(5,2))==0)
ck('actual_linear_unit_K3',sub(K3)==s.expand((1+8*t)**3))
ck('actual_tacnode_unit',sub(Kt)==s.expand(g2*g2))
ck('actual_quadratic_small_angle_unit',sub(Kdelta)==s.expand((1+8*t)*(1+80*t)*g2*g2))
ck('all_three_units_at_origin',all(sub(P).subs(t,0)==1 for P in (K3,Kt,Kdelta)))
ck('special_zero_mass_line',s.expand(sub(Fstar)+144*t*(t-1)*g2)==0)
ck('special_linear_unit',sub(Ks)==s.expand((4*t-1)*(8*t+1)*g2))
ck('special_unit_at_origin',sub(Ks).subs(t,0)==1)

rS=s.cancel(R*a.subs(t,tau))
rDiff=s.cancel(R*(c-b0).subs(t,tau))
numS,denS=s.fraction(rS)
ck('rank_two_scaled_pole_exactly_simple',s.degree(denS,t)==1 and s.cancel(denS/(1+8*t)).is_Rational)
ck('zero_mass_reference_difference_same_pole',s.degree(s.fraction(rDiff)[1],t)==1)
ck('rank_two_scaled_infinity_order',s.degree(numS,t)-s.degree(denS,t)==12)
ck('nonzero_mass_node_discrepancy',s.cancel(R*b0.subs(t,tau)).subs(t,1)==-3**19)
ck('nonzero_mass_node_first_value',s.cancel(R*b0.subs(t,tau)).subs(t,0)==1)

# Full degree-one return, not merely denominator clearing.
_,M4=matrix(4)
den=1+8*t
N=s.Poly(s.cancel(den*rS),t)
lift=s.zeros(18,17)
for i in range(17):
    lift[i,i]=1
    lift[i+1,i]=8
extra=s.Matrix([[s.Poly(N.as_expr()*f,t).nth(i) for f in (a,b0,c)] for i in range(18)])
ck('degree_one_original_rank',M4.rank()==14)
ck('no_nonzero_degree_one_return_for_original_S',(lift*M4).row_join(extra).rank()==17)

Q5=represent(sub(Kdelta)*rS,5)
ck('actual_degree_five_return',s.cancel(sub(Q5)-sub(Kdelta)*rS)==0)
ck('degree_five_return_is_in_full_conductor',s.rem(sub(Q5),d,t)==0)
Q5diff=represent(sub(Kdelta)*rDiff,5)
ck('same_unit_returns_entire_zero_mass_plane',s.cancel(sub(Q5diff)-sub(Kdelta)*rDiff)==0)
Q4=represent(sub(Ks)*R*sub(Fstar).subs(t,tau),4)
ck('special_mass_zero_line_has_degree_one_return',s.cancel(sub(Q4)-sub(Ks)*R*sub(Fstar).subs(t,tau))==0)
ck('product_multiplier_also_returns_original_S',s.rem(s.fraction(s.cancel(sub(K3*Kt)*rS))[0],d,t)==0)

# All minimal quadratic multipliers: g2^2*(1+8t)*P3, P3(1)=81 P3(0).
minimal_basis = [(1+8*t)*g2*g2*P for P in (1+80*t,t*(t-1),t*t*(t-1))]
minimal_reps = [represent(P,2) for P in minimal_basis]
_,M5=matrix(5)
_,M2=matrix(2)
lift5=s.zeros(22,21)
for i in range(21):
    lift5[i,i]=1
    lift5[i+1,i]=8
extra2=s.Matrix([[s.Poly(N.as_expr()*sum(M2[j,k]*t**j for j in range(9)),t).nth(i)
                 for k in range(M2.cols)] for i in range(22)])
ck('complete_quadratic_return_dimension',M5.rank()==18 and (lift5*M5).row_join(extra2).rank()==21)
for j,(P,K) in enumerate(zip(minimal_basis,minimal_reps)):
    ck('full_quadratic_multiplier_'+str(j),sub(K)==s.expand(P))
    returned=represent(P*rS,5)
    ck('full_quadratic_return_'+str(j),s.cancel(sub(returned)-P*rS)==0)

# The fixed three conics give the entire conductor, including two terminal angles.
C0=(-1152*X*X+336*X*Y+432*X*Z-3*Y*Y+Y*Z+2*Z*Z)/7776
C1=(-1152*X*X+192*X*Y+288*X*Z+3*Y*Y+Y*Z-4*Z*Z)/31104
C2=(4608*X*X+672*X*Y+288*X*Z+9*Y*Y-4*Y*Z-5*Z*Z)/62208
for j,Cj in enumerate((C0,C1,C2)):
    ck('full_conductor_conic_'+str(j),sub(Cj)==s.expand(d*t**j))
terminal = [represent(d*t**j,3) for j in (5,6)]
ck('terminal_angle_denominators_only_two_three',
   all(s.denom(v).is_Integer and s.denom(v)>0
       and set(s.factorint(int(s.denom(v)))) <= {2,3}
       for P in terminal for v in s.Poly(P,X,Y,Z).coeffs()))

# Exact physical sigma/Theta descriptions.
x,y,b,sg=s.symbols('x y b sigma',nonzero=True)
rho=sg**34*x**14*(x**3-8*b)
theta=x*sg**2
theta2=x*(x**3-8*b)*sg**8
ck('linear_unit_is_actual_five_theta_product',
   s.cancel(rho*(1+8*t)**3).subs(t,-b/x**3).expand()==s.expand(theta*theta2**4))
Q=x**6+20*b*x**3-8*b*b
ck('tacnode_unit_actual_divisor',
   s.cancel((rho*g2*g2).subs(t,-b/x**3)-sg**34*x*x*(x**3-8*b)*Q*Q)==0)

# Mixed return dimensions and all q^2 carry, with no sampled target prime.
q,m,e=s.symbols('q m e',integer=True)
ck('actual_infinity_budget',
   s.expand(4*(q+m+e)-((14*q-6)/3+3*m+4*e))==s.Rational(1,3)*(3*m-2*q+6))
ck('mixed_return_degree',s.expand(q+(2*q/3-2)-(5*q/3-2))==0)
ck('pure_ramified_return_degree',s.expand(q+(2*q/3-2)+1-(5*q/3-1))==0)
ck('first_ramified_return_degree',3+1+1==5)
ap,pp,Delta,ee=s.symbols('a_p p Delta epsilon')
e2=lambda z:1+z+z*z/2
carry=s.Poly(s.expand(e2(-pp*ap*Delta*ee)*e2(ap*(q+pp*Delta)*ee)-e2(q*ap*ee)),ee)
ck('complete_three_block_scaled_carry',carry.rem(s.Poly(ee**3,ee)).is_zero)
ck('complete_target_multiplier_inverse',
   s.Poly(s.expand(e2((m+e)*ap*ee)*e2(-(m+e)*ap*ee)-1),ee).rem(s.Poly(ee**3,ee)).is_zero)

answer={
 'status':'PASS','exact_checks':len(checks),'checks':checks,
 'parameter':str(tau),'carrier_return':str(R),
 'K3':str(K3),'Ktac':str(Kt),'minimal_quadratic_unit':str(Kdelta),
 'original_scaled_X_return_degree5':str(Q5),
 'reference_difference_return_degree5':str(Q5diff),
 'special_line':str(Fstar),'special_linear_unit':str(Ks),'special_return_degree4':str(Q4),
 'complete_quadratic_multiplier_basis':[str(P) for P in minimal_reps],
 'terminal_conductor_cubics':[str(P) for P in terminal],
 'mixed_return':{'alpha':'2^a*(sqrt(-3))^b','q':'4^a*3^b',
   'a_ge_1_b_ge_1':'K3^(2*q/3-2)*S(alpha*z) in A_(5*q/3-2)',
   'a_0_b_1':'K3*Ktac*S(sqrt(-3)*z) in A_5',
   'a_0_b_ge_2':'K3^(2*q/3-2)*Ktac*S(alpha*z) in A_(5*q/3-1)'},
 'no_target_prime_scan':True,
 'scope':'Scaled central zeros are true; independence or deep Smith gain is not asserted.'
}
Path(__file__).with_suffix('.json').write_text(json.dumps(answer,indent=2)+'\n')
print(json.dumps({'status':'PASS','exact_checks':len(checks),
                  'minimal_original_return_degree':2,'mixed_degree':'5*q/3-2'},indent=2))
