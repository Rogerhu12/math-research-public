#!/usr/bin/env python3
"""Exact de Rham dual of the actual R264 cokernel and rational gauge (R268)."""
import json
from pathlib import Path

import sympy as s

root = Path(__file__).parent
data = json.loads((root/'check-normtwo-finite-connection-kernel.json').read_text())
x = s.symbols('x')
U = x*x
f = x**3-x
P8 = sum(s.Rational(c)*U**j for j,c in enumerate(data['kernel_P8_coefficients']))
A8 = sum(s.Rational(c)*U**j for j,c in
         enumerate(data['de_Rham_reduction']['primitive_A8_coefficients']))
a = s.Rational(data['de_Rham_reduction']['period_coefficient'])
ell = list(map(s.Integer,data['left_kernel']))
checks = {}


def check(name,value):
    checks[name]=bool(value)
    if not checks[name]:
        raise AssertionError(name)


def reduce_odd_power(k):
    """x^k dz = c*x dz + d(y*r), for odd k, by exact Laurent reduction."""
    if k == 1:
        return s.Integer(1),s.Integer(0)
    if k > 1:
        c,r=reduce_odd_power(k-2)
        q=s.Rational(2*k-3,2*k-1)
        return q*c,x**(k-2)/s.Integer(2*k-1)+q*r
    c,r=reduce_odd_power(k+2)
    q=s.Rational(2*k+3,2*k+1)
    return q*c,-x**k/s.Integer(2*k+1)+q*r


reductions=[]
for n in range(17):
    coefficient=s.expand(4*P8*(U-1)*x**(2*n-17))
    c=s.Integer(0)
    r=s.Integer(0)
    for term in s.Add.make_args(coefficient):
        b,k=term.as_coeff_exponent(x)
        ck,rk=reduce_odd_power(int(k))
        c+=b*ck
        r+=b*rk
    c=s.cancel(c)
    r=s.expand(r)
    check(f'de_Rham_basis_column_{n}',s.expand(coefficient-c*x
          -(3*x*x-1)*r-2*f*s.diff(r,x))==0)
    reductions.append((c,r))

scale=s.cancel(reductions[0][0]/ell[0])
check('exact_dual_scale',scale==s.Rational(17179869184,644658718275))
check('all_cokernel_coordinates_are_actual_periods',
      all(s.cancel(c-scale*l)==0 for (c,r),l in zip(reductions,ell)))
check('two_period_normalizations',s.cancel(a*scale)==-s.Rational(4,1105))
primitive_denominator=s.ilcm(*[
    s.denom(term.as_coeff_exponent(x)[0])
    for c,r in reductions for term in s.Add.make_args(r)])
primitive_denominator_factors=s.factorint(primitive_denominator)
check('actual_primitives_integral_at_every_inert_prime_above_31',
      all(p%4==1 for p in primitive_denominator_factors if p>31))

# Work in Q(x)[y]/(y^2-x^3+x), with each element encoded as (r(x),s(x)).
zero=(s.Integer(0),s.Integer(0))
one=(s.Integer(1),s.Integer(0))


def add(u,v):
    return (s.cancel(u[0]+v[0]),s.cancel(u[1]+v[1]))


def neg(u):
    return (-u[0],-u[1])


def mul(u,v):
    return (s.cancel(u[0]*v[0]+f*u[1]*v[1]),
            s.cancel(u[0]*v[1]+u[1]*v[0]))


def deriv(u):
    return (s.cancel((3*x*x-1)*u[1]+2*f*s.diff(u[1],x)),
            s.cancel(2*s.diff(u[0],x)))


h=(s.cancel(P8/(U-1)**8),s.Integer(0))
hR=(s.Integer(0),s.cancel(A8/(U-1)**9))
G=[[h,hR],[deriv(h),add(deriv(hR),mul((a,0),h))]]
connection=[[zero,one],[(-1088*x/(U-1),0),(0,-68*x/(U-1))]]
unipotent=[[zero,(a,0)],[zero,zero]]
for i in range(2):
    for j in range(2):
        q=deriv(G[i][j])
        for k in range(2):
            q=add(q,neg(mul(connection[i][k],G[k][j])))
            q=add(q,mul(G[i][k],unipotent[k][j]))
        check(f'complete_rational_gauge_entry_{i}_{j}',q==zero)
det=add(mul(G[0][0],G[1][1]),neg(mul(G[0][1],G[1][0])))
check('exact_rational_gauge_determinant',
      s.cancel(det[0]-1/(U-1)**17)==0 and det[1]==0)


def laurent_terms(r):
    terms={}
    for t in s.Add.make_args(r):
        b,k=t.as_coeff_exponent(x)
        if b:
            terms[str(int(k))]=str(b)
    return dict(sorted(terms.items(),key=lambda q:int(q[0])))


out={
    'status':'PASS','checks':checks,
    'actual_differential':'eta_Q=4*P8(U)*(U-1)*Q(U)/(x*U^8) dz',
    'dual_scale':str(scale),'dual_scale_factorization_denominator':
        {str(int(p)):int(e) for p,e in s.factorint(s.denom(scale)).items()},
    'period_coefficients':[str(c) for c,r in reductions],
    'primitive_denominator_factorization':
        {str(int(p)):int(e) for p,e in primitive_denominator_factors.items()},
    'primitive_Laurent_polynomials':[
        {'input_degree':n,'R_coefficients':laurent_terms(r)}
        for n,(c,r) in enumerate(reductions)],
    'gauge_convention':'(h,h_prime)^t=G*(v,w)^t; v_prime=a*w, w_prime=0',
    'gauge_entries':[[{'rational_part':str(u[0]),'y_part':str(u[1])}
                     for u in row] for row in G],
    'gauge_determinant':'(U-1)^(-17)',
    'unipotent_constant':str(a),
    'scope':'The fixed actual norm-two differential connection; no Mellin or Selmer closure is assumed.'
}
Path(__file__).with_suffix('.json').write_text(
    json.dumps(out,ensure_ascii=False,indent=2)+'\n')
print('PASS:',len(checks),'checks; dual scale=',scale,'; a*scale=',s.cancel(a*scale))
