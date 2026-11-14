#!/usr/bin/env python3
"""Exact original-kernel obstruction for the six reduced basepoint supports.
SymPy is used only for rational polynomial arithmetic and integer resultants.
"""
import json
import sympy as S
s,z=S.symbols('s z')
q=lambda a,b:a**3*b+a*b**3-3*a*a*b*b+a**3+b**3-3*a*a*b-3*a*b*b-5*a*a-5*b*b+22*a*b
out=[]
for name,e1,e2,ps,tau,C,den,sign,res_expected in [
 ('plus',5,S.Rational(32,5),5*s**3-25*s*s+32*s-8,(4*s*s-s)/(s+1),606665*s*s-652964*s+232916,6860,-1,5930013732223926800),
 ('minus',-27,S.Rational(864,5),5*s**3+135*s*s+864*s+864,(4*s*s+31*s+32)/(s+1),8954105*s*s+80605252*s+99846172,43940,1,12326789196383727288230800)]:
    def red(f):
        n,d=S.fraction(S.cancel(f))
        return S.rem(S.rem(n,ps,s)*S.invert(d,ps,s),ps,s)
    assert ps.subs(s,-1)!=0
    pz=ps.subs(s,z)
    divided,rem=S.div(pz-ps,z-s,z);assert rem==0
    L=(s+1)*z+s-4*s*s if name=='plus' else (s+1)*z-4*s*s-31*s-32
    quotient=4*(s+z) if name=='plus' else 4*(s+z+8)
    assert S.expand(5*q(s,z)-L*divided-quotient*ps)==0
    polar=S.Poly(q(tau,z),z)
    alpha=polar.nth(3);beta=polar.nth(2)+s*alpha;gamma=polar.nth(1)+s*beta
    assert red(polar.nth(0)+s*gamma)==0
    total=e1-s;prod=e2-s*total
    chi=red(2*gamma+beta*total+2*alpha*prod)
    assert S.expand(chi-sign*C/den)==0
    res=S.resultant(ps,C,s)
    assert res==res_expected and int(res)%103!=0
    out.append({'branch':name,'chi':str(chi),'denominator':den,
                'integer_resultant':str(res),'resultant_mod103':int(res)%103})
# Scalar pole-value identity, independent of normalization of the conic.
a,b,c,tau,total,prod=S.symbols('a b c tau total prod')
AA=a*tau*tau+b*tau+c;BB=2*a*tau+b;CC=a
DD=tau*tau-total*tau+prod;EE=2*tau-total
assert S.expand(2*AA+2*DD*CC-BB*EE-(2*c+b*total+2*a*prod))==0
# Cubic normal form forced by the two actual contraction identities.
x0,x1,x2,A,B,kap,t=S.symbols('x0 x1 x2 A B kap t')
conic=x0*x2-x1*x1
cubic=-S.Rational(3,2)*A*x0*x1*x1+B*x1**3-3*kap*x1*x1*x2+S.Rational(3,2)*kap*x0*x2*x2
second=A*x1*x1-kap*x2*x2
assert S.diff(cubic,x0,2)==0
assert S.expand(S.diff(cubic,x2)-3*kap*conic)==0
assert S.expand(-S.Rational(2,3)*S.diff(cubic,x0)-second)==0
assert S.expand(cubic.subs({x0:1,x1:t,x2:t*t})-t*t*(-S.Rational(3,2)*A+B*t-S.Rational(3,2)*kap*t*t))==0
print(json.dumps({'all_pass':True,'original_polar_factor_identities':True,
 'exact_conic_normal_form':True,'exact_pole_value_identity':True,'branches':out},indent=2))
