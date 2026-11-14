#!/usr/bin/env python3
"""Exact reconstruction of the actual five-site primitive Green quadratic form.
This source was rebuilt after the research environment disconnected. Its
identities are proved in the accompanying note; no new execution is claimed.
"""
import json
import sympy as sp

x = sp.symbols("x")
w = [x + a for a in [1, 4, 9, 16, 25]]
a = [sum(w) - 2 * wi for wi in w]
N = 36*x**5 + 1470*x**4 + 22861*x**3 + 165585*x**2 + 535743*x + 601825
P = 54*x**5 + 2970*x**4 + 63657*x**3 + 662695*x**2 + 3318689*x + 6220735
q = 1/(w[0]*a[0]) + 1/(w[1]*a[1]) - (1/a[0]-1/a[1])**2/(1+sum(wi/ai for wi,ai in zip(w,a)))
assert sp.cancel(q-N/((x+1)*(x+4)*P)) == 0
det_formula = sp.prod(wi*ai for wi,ai in zip(w,a))*(1+sum(wi/ai for wi,ai in zip(w,a)))
assert sp.cancel(det_formula-12*sp.prod(w)*P) == 0
disc = sp.discriminant(P,x)
assert disc == -405178286708678821590712320000
left,right = sp.Poly(P,x, modulus=11),sp.Poly(N,x, modulus=11)
chain = []
while not right.is_zero:
    quotient,remainder = sp.div(left,right)
    chain.append({"quotient":str(quotient.as_expr()),"remainder":str(remainder.as_expr())})
    left,right = right,remainder
assert left.degree() == 0
print(json.dumps({"exact_primitive_form":True,"determinant_identity":True,
    "discriminant":str(disc),"gcd_mod_11_degree":left.degree(),"euclid_chain":chain},indent=2))
