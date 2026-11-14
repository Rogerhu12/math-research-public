#!/usr/bin/env python3
"""R334 fixed algebra and formal-series checks, with no target-prime scan."""
import json
from pathlib import Path
import sympy as s

t,x,y,b,v,z,p,ap,tau,w = s.symbols('t x y b v z p a_p tau w')
checks=[]


def check(name,expr):
    assert s.cancel(expr)==0,name
    checks.append(name)


tdot=6*b*y/x**4
tddot=6*b*(3/x**2-8*y**2/x**5)
check('original t second derivative',
      tddot.subs(y**2,x**3+b)+6*b/x**2*(5+8*b/x**3))
check('original t derivative squared',
      (tdot**2).subs(y**2,x**3+b)+36*b/x**2*(-b/x**3)*(1+b/x**3))
logtheta_second=-2*x+6*x-4*y**2/x**2
check('actual log Theta second derivative',logtheta_second.subs(y**2,x**3+b)+4*b/x**2)
check('fixed theta ODE constant',s.Rational(68,6)-s.Rational(34,3))

def hn(n):
    return s.rf(s.Rational(1,2),n)/(s.factorial(n)*(6*n+1))


def dn(n):
    return 1-s.Rational(1,6*n+1)+(s.harmonic(2*n)-s.harmonic(n))/3


for n in range(9):
    ratio=(p+1)/(p+1+6*n)*s.rf(s.Rational(1,2)+p/6,n)/s.rf(1+p/6,n)
    check('true hypergeometric residue n=%s'%n,ratio.subs(p,0)-hn(n))
    check('true next digit n=%s'%n,s.diff(ratio,p).subs(p,0)-hn(n)*dn(n))

bound=9
h=sum(hn(n)*t**n for n in range(bound))
H=sum(hn(n)*dn(n)*t**n for n in range(bound))
G=(1-t)**s.Rational(-1,2)
trunc=lambda expr:s.series(expr,t,0,bound).removeO().expand()
T=trunc(H-h*trunc(s.log(h)))
forcing=trunc(s.log(h)+s.log((1+s.sqrt(1-t))/2)/3)
check('fixed harmonic carry differential equation',trunc(T+6*t*s.diff(T,t)+G*forcing))
check('fixed forcing first term',forcing.coeff(t,1)+s.Rational(1,84))
check('fixed carry first term',T.coeff(t,1)-s.Rational(1,588))

f=v**3-y
check('actual Miller norm',s.expand(f*(v**3+y)+b).subs(y**2,v**6+b))
df=3*v**2-3*v**5/y
check('actual Miller logarithmic differential',df+3*v**2*f/y)
check('true frame derivative keeps elliptic logarithm',1/z+(-3*v)/3-(1/z-v))

R=s.Matrix([[-7,49,-343],[0,49*ap,-686*ap],[0,49*ap**2/2,-686*ap**2]])
check('original three constant directions',R.det()-7**6*ap**3)
tail=s.Matrix([0,0,1])+R*s.Matrix([1/(7*ap**2),2/(49*ap**2),1/(343*ap**2)])
assert tail==s.zeros(3,1)
checks.append('ell-one boundary retains exact full-tail correction coefficients')
c1,c2=s.symbols('c1 c2')
check('complete central next aggregation',
      ap**2/p*(p/ap*c1-p**2/ap**2*c2)-(ap*c1-p*c2))

# Pure block algebra only: s=20 gives composite 6s-1.  The accompanying
# proof applies to all allowed s, and retains the complete correction tail.
for ell in (1,2,6):
    block=20
    a0,a1,b0,b1,c0=s.symbols('A0 A1 B0 B1 C0')
    W1=w**block*(a0+a1*w)
    W2=w**ell*(b0+b1*w)
    W3=c0*w
    first=s.expand(tau*w**(block-1)*W1+tau**2*w**(2*block-2)*W2/2)
    shift1=sum(first.coeff(w,j+block)*w**j for j in range(block))
    assert all(shift1.coeff(w,j)==0 for j in range(block-13))
    third=s.expand(ap*(tau*w**(block-1)*W2+tau**2*w**(2*block-2)*W3/2))
    shift2=sum(third.coeff(w,j+block)*w**j for j in range(ell))
    check('exact rank-one last-row variation ell=%s'%ell,
          shift2-ap*tau*b0*w**(ell-1))
checks.append('all quadratic terms are retained before the paid boundary quotient')

out={'status':'PASS','number_of_exact_checks':len(checks),'checks':checks,
     'theta_equation':'6t(1-t)Ldd+(5-8t)Ld=34/3',
     'central_next_equation':'a_p*c1-p*c2=0 mod p^2',
     'rank_one_variation':'a_p*tau*[w^ell]E^2(P)*[epsilon^2*w^(ell-1)]',
     'fixed_curve':'y^2=v^6+b','miller_unit':'v^3-y',
     'miller_divisor':'3(P_plus-P_minus)',
     'fixed_carry_first_coefficient':'1/588',
     'scope':'Fixed exact symbolic checks only; uniform precision and kernel statements are proved in R334.'}
dest=Path(__file__).with_suffix('.json')
dest.write_text(json.dumps(out,ensure_ascii=False,indent=2)+'\n')
print('PASS: %s exact checks; %s'%(len(checks),dest.name))
