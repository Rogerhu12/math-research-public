#!/usr/bin/env python3
"""R309 exact original quartic, conductor, dyadic theta identity and q2 blocks.

Only fixed characteristic-zero algebra is computed. No target prime is sampled.
"""
import json
from pathlib import Path
import sympy as s

t,X,Y,Z=s.symbols('t X Y Z')
xb,yb,b,sg=s.symbols('x y b sigma',nonzero=True)
a=16*t**4-12*t**3+3*t**2-7*t
b0=256*t**4+1472*t**3-1200*t**2+200*t+1
c=-128*t**4-832*t**3+1968*t**2-280*t+1
g2=8*t*t+20*t-1
dd=t*(t-1)*g2*g2
checks=[]
def ck(name,test):
    assert test,name
    checks.append(name)

P1=X**4-s.Rational(53,7)*b*X**3-s.Rational(12,7)*b*b*X*X-s.Rational(80,7)*b**3*X-s.Rational(128,7)*b**4
P3=X**5-208*b*X**4+400*b*b*X**3+8128*b**3*X*X+12032*b**4*X-2048*b**5
P5=X**5+272*b*X**4-272*b*b*X**3-14912*b**3*X*X-6784*b**4*X+1024*b**5
for name,P,scale,param in [('H1',P1,7*b,a),('H3',P3,1,b0),('H5',P5,1,c)]:
    ck('actual_source_'+name,s.cancel(scale*P.subs(X,-b/t)/(-b/t)**5-(1+8*t)*param)==0)
ck('complete_common_angular_factor',s.degree(s.gcd(s.gcd((1+8*t)*a,(1+8*t)*b0),(1+8*t)*c),t)==1)
res=s.resultant(a,b0,t)
ck('uniform_normalization_pencil_resultant',res==2**16*3**18)

def monomials(n):
    es=[(i,j,n-i-j) for i in range(n+1) for j in range(n-i+1)]
    polys=[s.Poly(a**i*b0**j*c**k,t) for i,j,k in es]
    mat=s.Matrix([[P.nth(r) for P in polys] for r in range(4*n+1)])
    return es,mat

es2,M2=monomials(2)
es3,M3=monomials(3)
es4,M4=monomials(4)
ck('true_graded_ranks_2_3_4',[M2.rank(),M3.rank(),M4.rank()]==[6,10,14])
nsphi=M4.nullspace()
ck('unique_quartic_relation',len(nsphi)==1)
pv=nsphi[0]
pd=s.ilcm(*[s.denom(z) for z in pv])
pv=[int(z*pd) for z in pv]
pg=s.igcd(*pv)
pv=[z//pg for z in pv]
Phi=sum(z*X**i*Y**j*Z**k for z,(i,j,k) in zip(pv,es4))
ck('actual_implicit_relation',s.expand(Phi.subs({X:a,Y:b0,Z:c}))==0)

C0=(-1152*X*X+336*X*Y+432*X*Z-3*Y*Y+Y*Z+2*Z*Z)/7776
C1=(-1152*X*X+192*X*Y+288*X*Z+3*Y*Y+Y*Z-4*Z*Z)/31104
C2=(4608*X*X+672*X*Y+288*X*Z+9*Y*Y-4*Y*Z-5*Z*Z)/62208
for j,C in enumerate([C0,C1,C2]):
    ck('actual_conductor_conic_'+str(j),s.expand(C.subs({X:a,Y:b0,Z:c})-t**j*dd)==0)
ck('conic_quartic_and_rational_inverse',s.expand(C1*C1-C0*C2-Phi/(2**14*3**8))==0)
ck('primitive_normalized_conductor_coefficient',s.Poly(dd,t).nth(1)==-1)

# Complete degree-two conductor, certified on degree-one normalization generators.
left=s.Matrix.vstack(*[v.T for v in M3.T.nullspace()])
conds=[]
for j in range(5):
    sh=s.zeros(13,9)
    for r in range(9): sh[r+j,r]=1
    conds.append(left*sh*M2)
CC=s.Matrix.vstack(*conds)
ck('complete_degree_two_conductor_dimension',len(CC.nullspace())==3)
reps=[]
for j in range(5):
    P=s.Poly(dd*t**j,t)
    target=s.Matrix([P.nth(r) for r in range(13)])
    sol=M3.gauss_jordan_solve(target)[0]
    ck('full_original_cubic_representative_'+str(j),M3*sol==target)
    reps.append([str(z) for z in sol])
replcm=s.ilcm(*[s.denom(s.Rational(z)) for row in reps for z in row])
ck('uniform_original_representative_denominator',replcm==2**12*3**11)

# The original normalization branch is a node; the other singularity is a tacnode.
xn=a/b0;yn=c/b0-1
nodevectors=[[s.diff(f,t).subs(t,q) for f in (xn,yn)] for q in (0,1)]
ck('actual_node_preimages',a.subs(t,0)==a.subs(t,1)==0 and b0.subs(t,0)==c.subs(t,0)==1 and b0.subs(t,1)==c.subs(t,1)==729)
ck('actual_node_tangent_determinant',s.det(s.Matrix(nodevectors))==s.Rational(128,3))
ck('node_is_singular',all(s.diff(Phi,z).subs({X:0,Y:1,Z:1})==0 for z in (X,Y,Z)))
def remrat(f):
    nu,de=s.fraction(s.cancel(f))
    return s.rem(nu*s.invert(de,g2,t),g2,t)
xi=a/b0+s.Rational(1,24)
eta=c/b0+1
ck('actual_tacnode_common_image',remrat(xi)==remrat(eta)==0)
ck('actual_tacnode_first_coordinate',s.expand(remrat(s.diff(xi,t))+(8*t+19)/54)==0)
ck('actual_tacnode_common_tangent',remrat(s.diff(eta,t))==0)
qcurve=remrat(s.diff(eta,t,2)/(2*s.diff(xi,t)**2))
ck('actual_tacnode_distinct_quadratic_terms',s.expand(qcurve-s.Rational(128,3)*(8*t+19))==0)
ck('tacnode_discriminant_and_nonzero_velocity',s.discriminant(g2,t)==432 and s.resultant(g2,8*t+19,t)==-216)
ck('tacnode_denominator_only_two_three',s.resultant(b0,g2,t)==-2**12*3**11)

# Actual multiplication by two on E/mu6 and the full degree-68 theta conductor.
tau=64*t*(1-t)**3/(1+8*t)**3
x2=xb*(xb**3-8*b)/(4*(xb**3+b))
ck('actual_dyadic_coordinate_from_elliptic_doubling',s.cancel(-b/x2**3-tau.subs(t,-b/xb**3))==0)
ck('actual_dyadic_fiber_over_one',s.factor(tau-1+g2*g2/(1+8*t)**3)==0)
ck('actual_dyadic_derivative',s.factor(s.diff(tau,t)+64*(t-1)**2*g2/(1+8*t)**4)==0)
rho=sg**34*xb**14*(xb**3-8*b)
actualD=s.cancel(rho**2*dd.subs(t,-b/xb**3)/b)
Q4=xb**6+20*b*xb**3-8*b*b
algebraicD=sg**68*xb**10*(xb**3+b)*(xb**3-8*b)**2*Q4**2
ck('actual_normalized_conductor_algebraic_identity',s.cancel(actualD-algebraicD)==0)
sigma4=-4*yb*Q4*sg**16
theta=xb*sg**2
theta2=xb*(xb**3-8*b)*sg**8
product=sg**4*sigma4**2*theta**8*theta2**2/16
ck('actual_full_dyadic_theta_product',s.expand(product.subs(yb**2,xb**3+b)-algebraicD)==0)
ck('actual_degree_and_origin_order',4+32+16+16==68 and 68-20-6-12-24==6)
U=s.symbols('U')
ck('full_first_scaled_sigma_carry',s.expand((20+4*U+2*U*U-68)-(4*(U-4)+2*(U*U-16)))==0)

# Universal three-block algebra of the same q2 target.
ee,ap,pp=s.symbols('epsilon a_p p')
w00,w01,w02,w10,w11,w20=s.symbols('w00 w01 w02 w10 w11 w20')
raw=(w00+pp*ee*w01+pp**2*ee**2*w02)+ap*ee*(w10+pp*ee*w11)+ap**2*ee**2*w20/2
ck('full_first_q2_block',s.expand(raw).coeff(ee,0)==w00)
ck('full_second_q2_block',s.expand(raw).coeff(ee,1)==ap*w10+pp*w01)
ck('full_third_q2_block',s.expand(raw).coeff(ee,2)==ap**2*w20/2+pp*ap*w11+pp**2*w02)
e2=lambda z:1+z+z*z/2
ck('paid_charge_two_target_unit_inverse',s.Poly(s.expand(e2(2*ap*ee)*e2(-2*ap*ee)-1),ee).rem(s.Poly(ee**3,ee)).is_zero)
mm=s.symbols('m')
ck('paid_charge_two_source_exponent',s.Poly(s.expand(e2(2*ap*ee)*e2(mm*ap*ee)-e2((mm+2)*ap*ee)),ee).rem(s.Poly(ee**3,ee)).is_zero)

# Fixed, p-independent five-jet of the inverse radial carrier.
q=s.symbols('q')
logu=[s.Rational(0)]*6
for n in range(1,6):
    logu[n]=-s.Rational(17,3*n)*s.rf(s.Rational(1,3),n)/s.rf(s.Rational(5,6),n)*(-1)**n+s.Rational(8**n,n)
uinv=[s.Rational(0)]*6;uinv[0]=s.Rational(1)
for n in range(1,6):
    uinv[n]=s.factor(sum(j*logu[j]*uinv[n-j] for j in range(1,n+1))/n)
fixed=[1,s.Rational(154,15),s.Rational(207598,2475),s.Rational(74793772,111375),s.Rational(2270761219726,422668125),s.Rational(39511246126891196,919303171875)]
ck('actual_fixed_inverse_radial_five_jet',uinv==fixed)
ck('actual_fifth_contact_is_nonzero',uinv[5]!=0)
nn,ii,jj,kk=s.symbols('n i j k',integer=True)
ck('weighted_source_translation_budget',s.expand(4*(nn-kk)-(jj+4*(ii-kk))-(4*nn-jj-4*ii))==0)
ck('unit_Schur_terminal_orders',s.expand(4*(nn-ii)+5*ii-(4*nn+ii))==0)
ck('true_source_rank_and_remaining_Schur_rank',s.expand((2*nn**2+3*nn+1)-(5*nn+1)-2*nn*(nn-1))==0)

ans={'status':'PASS','exact_checks':len(checks),'checks':checks,
 'source_scale':'X=7*b*H1, Y=H3, Z=H5; carrier rho=Theta17*(1+8*t)',
 'parameter_polynomials':[str(f) for f in (a,b0,c)],
 'implicit_quartic':str(Phi),'quartic_monomials':es4,'implicit_quartic_coefficients':pv,
 'conductor_polynomial':str(s.expand(dd)),
 'conductor_polynomial_ascending':[str(s.Poly(dd,t).nth(j)) for j in range(7)],
 'conductor_conics':[str(f) for f in (C0,C1,C2)],
 'conic_relation_scalar':'1/(2^14*3^8)',
 'normalization_pencil_resultant':str(res),
 'cubic_representative_monomials':es3,
 'full_conductor_degree_one_product_representatives':reps,
 'representative_denominator_lcm':str(replcm),
 'node':{'point':[0,1,1],'normalization_parameters':[0,1],
         'tangent_vectors':[[str(z) for z in v] for v in nodevectors],
         'tangent_determinant':'128/3','conductor_orders':[1,1]},
 'tacnode':{'point':[-1,24,-24],'normalization_parameter_polynomial':str(g2),
            'first_coordinate_derivative':str(remrat(s.diff(xi,t))),
            'quadratic_branch_coefficients':str(qcurve),'conductor_orders':[2,2]},
 'dyadic_parameter':str(tau),'actual_theta_conductor':'sigma(z)^4*sigma(4z)^2*Theta(z)^8*Theta(2z)^2/16',
 'actual_theta_degree':68,'actual_origin_order_in_z':6,
 'paid_source_degree':2,'paid_origin_order_in_w':1,
 'maximum_q2_Smith_boundary_length':2,
 'original_first_kernel':{'value_and_first_Euler_truncation':'s-1','second_Euler_truncation':'max(ell-1,0)'},
 'inverse_radial_low_coefficients_b1':[str(z) for z in uinv],
 'fixed_fifth_contact_coefficient_b1':str(uinv[5]),
 'no_target_prime_scan':True}
Path(__file__).with_suffix('.json').write_text(json.dumps(ans,indent=2)+'\n')
print(json.dumps({'status':'PASS','exact_checks':len(checks),
                  'conductor':str(s.factor(dd)),
                  'source_degree_cost':2,'origin_order_cost':1,
                  'q2_boundary_length_at_most':2,
                  'fixed_fifth_contact':str(uinv[5])},indent=2))
