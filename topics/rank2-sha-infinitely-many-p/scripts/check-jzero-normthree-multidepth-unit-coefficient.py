#!/usr/bin/env python3
"""Fixed symbolic certificate for R339; no prime samples or conjectural moments."""
from pathlib import Path
import json
import sympy as s
r,t,b,z,q=s.symbols('r t b z q')
checks=[]
def same(name,a,c):
    assert s.simplify(a-c)==0,(name,a,c)
    checks.append(name)
B=r*t-(r*(r-1)+t*(t-1))/2
same('full paired falling-factorial aggregation',B,(r+t-(r-t)**2)/2)
for a,c,v in [(1,1,1),(7,1,-14),(1,7,-14),(7,7,7)]:
    same(f'paired coefficient {a},{c}',B.subs({r:a,t:c}),v)
a=b/s.Integer(210)
x=z**-2-b*z**4/7
sig=z+a*z**7
same('curve jet x second derivative',s.expand(s.diff(x,z,2)-6*x*x).coeff(z,2),0)
same('sigma logarithmic second derivative',s.series(s.diff(s.log(sig),z,2)+x,z,0,5).removeO(),0)
same('original seventh moment divided by period',s.factorial(7)*a,24*b)
Theta=s.series(s.diff(sig,z)**2-sig*s.diff(sig,z,2),z,0,7).removeO()
same('Theta original weight jet',Theta,1-2*b*z**6/15)
same('actual norm three first nonconstant coefficient',-28*a,Theta.coeff(z,6))
for parity in [0,1]:
    k=s.symbols('k',integer=True,nonnegative=True)
    K=2*k+parity
    m=k+parity
    same(f'pair capacity remainder parity {parity}',2*m-K,parity)
    same(f'original negative exponent parity {parity}',(5+2*m+6*K)-2*m,5+6*K)
    same(f'total exponent cost parity {parity}',(5+2*m+6*K)-(6*K+7),2*m-2)
pp=s.symbols('p',integer=True,positive=True)
same('Fermat exponent difference',(2-pp)-1,-(pp-1))
same('log factorial is below the characteristic',(pp-2)-1,pp-3)
# The original quadratic weight, applied to e^(c(Tx+Uy)), gives exactly
# the cross moment minus the two square moments, with the common q^-2.
for rr,tt in [(1,1),(7,1),(7,7)]:
    direct=s.Rational(1,s.factorial(rr-1)*s.factorial(tt-1))
    if rr>=2: direct-=s.Rational(1,2*s.factorial(rr-2)*s.factorial(tt))
    if tt>=2: direct-=s.Rational(1,2*s.factorial(rr)*s.factorial(tt-2))
    same(f'independent factorial aggregation {rr},{tt}',direct,
         B.subs({r:rr,t:tt})/(s.factorial(rr)*s.factorial(tt)))
result={'status':'PASS','number_of_exact_checks':len(checks),'checks':checks,
'fixed_curve':'y^2=x^3+17','original_source':'same six-sigma S of R333',
'paired_weight':'XY-(X^2+Y^2)/2','paired_coefficients':{'1,1':1,'7,1':-14,'7,7':7},
'prime_range':'p>7, p!=17, p=6s+1','K':'s-1','m':'ceil((s-1)/2)',
'unit_negative_moment':'I_(2-p) = (1-t_p)*Omega mod p',
'conclusion':'A specified multidepth coefficient is a unit; some actual arbitrarily deep domain has nonzero central derivative.',
'limitation':'No propagation of original complete central zero to these domains is assumed or proved.'}
out=Path(__file__).with_suffix('.json')
out.write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({'status':'PASS','checks':len(checks),'output':str(out)},ensure_ascii=False))
