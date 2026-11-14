"""Exact all-profile coefficient certificate for the strict endpoint star limit.

This is a symbolic identity in arbitrary first three weighted moments.
It is not a sample over a fixed number of groups.  A matrix is represented
as D[f] + sum c f(z) g(z)^T, with D[f]=diag(f(z_i)/omega_i).
The product star(A,B)=A G0^{-1} B uses the exact inverse
G0^{-1}=d (diag(omega_i/z_i)-omega omega^T).
Run with Python and SymPy; no data files or network are required.
"""
import sympy as sp

x, y, d, kappa, moment3 = sp.symbols("x y d kappa moment3")
moments = {
    0: sp.Integer(1),
    1: 1-d,
    2: d*kappa + 1-2*d,
    3: moment3,
}

def mean(poly):
    p = sp.Poly(sp.expand(poly), x)
    return sp.expand(sum(coef*moments[powers[0]]
                         for powers, coef in p.terms()))

def canonical(diagonal, outers):
    return (sp.expand(diagonal),
            sp.expand(sum(c*f*g.subs(x, y) for c, f, g in outers)))

def matrix(diagonal, outer_polynomial):
    p = sp.Poly(sp.expand(outer_polynomial), x, y)
    return (sp.expand(diagonal),
            [(c, x**i, x**j) for (i, j), c in p.terms()])

def add(*args):
    return matrix(*canonical(sum(a[0] for a in args),
                             sum((a[1] for a in args), [])))

def scale(c, a):
    return sp.expand(c*a[0]), [(c*b, f, g) for b, f, g in a[1]]

def outer(f, g):
    return 0, [(sp.Integer(1), sp.expand(f), sp.expand(g))]

def diagonal(f):
    return sp.expand(f), []

def apply_to_weighted_vector(a, p):
    """Apply a to the vector omega_i*p(z_i)."""
    dia, outers = a
    return sp.expand(dia*p + sum(c*f*mean(g*p)
                                for c, f, g in outers))

def star(a, b):
    """The exact product a G0^{-1} b."""
    da, oa = a
    db, ob = b
    dia = d*da*db/x
    terms = [(-d, da, db)]
    for c, h, k in ob:
        terms += [(d*c, da*h/x, k), (-d*c*mean(h), da, k)]
    for c, f, g in oa:
        terms += [(d*c, f, g*db/x), (-d*c*mean(g), f, db)]
    for c, f, g in oa:
        for e, h, k in ob:
            terms += [(d*c*e*(mean(g*h/x)-mean(g)*mean(h)), f, k)]
    return matrix(*canonical(dia, terms))

mu = x/d
nu = -2*x*(x+kappa-1)/d**2

g0 = add(diagonal(x/d), outer(x/d, x/d))
g1 = add(
    diagonal(-2*x*(2*x+kappa-1)/d**2),
    scale((8-6*kappa)/d**3, outer(x, x)),
    scale(-4/d**3, add(outer(x*x, x), outer(x, x*x))),
)

r1 = sp.expand(mu - apply_to_weighted_vector(g0, x-1))
r2 = sp.expand(nu - apply_to_weighted_vector(g1, x-1))
s1, s2 = sp.expand(r1/x), sp.expand(r2/x)

a1 = -x*mu
b1 = 1/d
b2 = -2*(x+kappa-1)/d**2
left1 = add(diagonal(x), outer(x, r1))
left2 = add(diagonal(-x*x/d), outer(x, r2), outer(a1, r1))
right2 = add(diagonal(1/d), scale(-1, outer(s1, 1/d)))
right3 = add(diagonal(b2), scale(-1, outer(s1, b2)),
             scale(-1, outer(s2, 1/d)))

j1 = add(outer(1, mu), diagonal(-1), scale(d, outer(mu, mu)),
         outer(1, s1), star(left1, right2))
j2 = add(
    outer(1, nu), scale(-1, outer(mu, mu)), scale(-1, g0),
    scale(d, add(outer(mu, nu), outer(nu, mu))),
    scale(kappa, outer(mu, mu)), outer(1, s2),
    scale(-1, outer(mu, s1)), scale(-1, outer(r1, mu)),
    star(left2, right2), star(left1, right3),
    scale(-1, star(star(left1, g1), right2)),
)

j1_diag, j1_outer = canonical(*j1)
j2_diag, j2_outer = canonical(*j2)
expected = 2*y*(y+kappa-2)/d**2
assert sp.cancel(j1_diag) == 0
assert sp.cancel(j1_outer) == 0
assert sp.cancel(j2_diag) == 0
assert sp.cancel(j2_outer-expected) == 0
assert not sp.expand(j2_outer).has(moment3)

print("J[1] = 0")
print("J[2] diagonal = 0")
print("J[2](x,y) =", sp.factor(j2_outer))
print("Third weighted moment cancels exactly.")

