"""Exact original P certificate in QQ[q]/q^N with a^3 = 17.

This changes the representation of the R870/R906 characteristic-zero identity,
not its bound, basis, coefficients, parameter, differential, or cusp branch.
Products of basis forms are grouped before evaluating the two numerators.
No dense high-precision matrix of all product forms is materialized.
"""
import os
if (os.environ.get("GITHUB_ACTIONS") != "true" or
        os.environ.get("GITHUB_REPOSITORY") != "Rogerhu12/math-research-public"):
    raise SystemExit("Run only in the public research repository Actions.")

import hashlib
from collections import defaultdict
from pathlib import Path
from sage.all import QQ, ZZ, PolynomialRing, lcm


def original_polynomial_rings():
    """Use Sage 10.6's default QQ FLINT backend; check the actual API early."""
    R = PolynomialRing(QQ, "q")
    Z = PolynomialRing(ZZ, "q", implementation="FLINT")
    q = R.gen()
    assert "polynomial_rational_flint" in type(q).__module__
    p = (q + QQ(1)/2)**2
    assert p.denominator() == 4
    ip = Z([ZZ(4*c) for c in p.list()])
    assert R(ip)/4 == p
    assert (q*p.derivative()).truncate(2) == q
    return R, Z


def strict_original_cubic_certificate(weight, sol, qrows, *, field, vnew,
                                      original_f, forms2, low_m2, recipes,
                                      progress, digest, coords):
    dim = len(qrows)
    assert len(sol) == 2 * dim and len(recipes) == dim
    assert all(len(r) == weight // 2 for r in recipes)
    assert field.degree() == 3 and field.gen() ** 3 == 17
    bound = 612 * (weight + 1)
    precision = bound + 3
    R, Z = original_polynomial_rings()
    q = R.gen()

    def trunc(p):
        return p.truncate(precision)

    def split(z):
        cc = field(z).list()
        return tuple(QQ(cc[i]) if i < len(cc) else QQ.zero() for i in range(3))

    def constant(z):
        return tuple(R(c) for c in split(z))

    def add(a, b):
        return tuple(a[i] + b[i] for i in range(3))

    def sub(a, b):
        return tuple(a[i] - b[i] for i in range(3))

    def mul(a, b):
        # Six exact QQ polynomial products; then reduce a^3=17.
        d0, d1, d2 = [trunc(a[i] * b[i]) for i in range(3)]
        e01 = trunc((a[0] + a[1]) * (b[0] + b[1])) - d0 - d1
        e02 = trunc((a[0] + a[2]) * (b[0] + b[2])) - d0 - d2
        e12 = trunc((a[1] + a[2]) * (b[1] + b[2])) - d1 - d2
        return (d0 + 17 * e12, e01 + 17 * d2, e02 + d1)

    def theta(a):
        # q*d/dq preserves (q^precision), so no digit is lost here.
        return tuple(trunc(q * c.derivative()) for c in a)

    def coefficient(a, j):
        return sum((a[i][j] * field.gen() ** i for i in range(3)), field.zero())

    def valuation(a):
        return min((int(c.valuation()) for c in a if c), default=precision)

    def poly_hash(polys):
        h = hashlib.sha256()
        for p in polys:
            for j in range(precision):
                h.update(str(QQ(p[j])).encode())
                h.update(b"\n")
            h.update(b";\n")
        return h.hexdigest()

    progress("grouped certificate: extend the same complete M2 basis",
             precision=precision, product_dimension=dim)
    two = []
    int_two = []
    den_two = []
    for i, g in enumerate(forms2):
        e = g.q_expansion(precision)
        p = R(e.list()).truncate(precision)
        assert all(p[j] == low_m2[i][j] for j in range(len(low_m2[i])))
        d = ZZ(p.denominator())
        ip = Z([ZZ(d * c) for c in p.list()])
        assert R(ip) / d == p
        two.append(p)
        int_two.append(ip)
        den_two.append(d)
    high_basis_hash = poly_hash(two)
    progress("grouped certificate: full basis prefixes retained",
             precision=precision, M2_high_basis_sha256=high_basis_hash)

    # Verify every old product-prefix gate without constructing its high row.
    # A base-form prefix through LOW_PREC determines each product prefix.
    low_precision = len(qrows[0])
    assert all(len(r) == low_precision for r in qrows)
    for recipe, row in zip(recipes, qrows):
        pp = R.one()
        for j in recipe:
            pp = (pp * two[j].truncate(low_precision)).truncate(low_precision)
        assert all(pp[j] == row[j] for j in range(low_precision))
    progress("grouped certificate: every original product prefix checked",
             rows=dim, prefix=low_precision)

    prefix_products = {}

    def evaluate_original(coefficients, label):
        groups = defaultdict(list)
        for recipe, c in zip(recipes, coefficients):
            if c:
                groups[tuple(recipe[:-1])].append((recipe[-1], split(c)))
        out = [R.zero(), R.zero(), R.zero()]
        progress("grouped certificate: numerator evaluation start",
                 label=label, groups=len(groups), nonzero_coefficients=sum(
                     len(items) for items in groups.values()))
        for number, (prefix, items) in enumerate(sorted(groups.items()), 1):
            if prefix not in prefix_products:
                pp = R.one()
                for j in prefix:
                    pp = trunc(pp * two[j])
                prefix_products[prefix] = pp
            pp = prefix_products[prefix]
            for k in range(3):
                terms = [(j, c[k] / den_two[j]) for j, c in items if c[k]]
                if not terms:
                    continue
                d = ZZ(lcm([c.denominator() for _, c in terms]))
                ip = Z.zero()
                for j, c in terms:
                    ip += ZZ(d * c) * int_two[j]
                out[k] += trunc(pp * (R(ip) / d))
            if number % 8 == 0 or number == len(groups):
                progress("grouped certificate: numerator groups evaluated",
                         label=label, groups_done=number, groups_total=len(groups))
        return tuple(out)

    A = evaluate_original(sol[:dim], "A")
    B = evaluate_original(sol[dim:], "B")
    b_order = valuation(B)
    assert 1 <= b_order < precision and valuation(A) == b_order - 1
    b0 = coefficient(B, b_order)
    yminus1 = coefficient(A, b_order - 1) / b0
    yzero = (coefficient(A, b_order) - yminus1 * coefficient(B, b_order + 1)) / b0
    assert yminus1 == -1 and yzero == -(vnew + 3) / 2
    progress("grouped certificate: original complete cusp branch checked",
             B_order_at_infinity=b_order, A_sha256=poly_hash(A), B_sha256=poly_hash(B))

    C = sub(mul(theta(A), B), mul(A, theta(B)))
    fcoords = [split(c) for c in original_f[:precision]]
    ff = tuple(R([c[i] for c in fcoords]) for i in range(3))
    f3 = mul(mul(ff, ff), ff)
    h = tuple(trunc(q * c) for c in f3)
    AvB = add(A, mul(constant(vnew), B))
    progress("grouped certificate: original weight identity start", bound=bound)
    C3 = mul(mul(C, C), C)
    product = mul(mul(A, AvB), B)
    residual = sub(C3, mul(h, mul(product, product)))
    first = valuation(residual)
    passed = first > bound
    info = {
        "bound": bound,
        "full_0_through_bound_identity": passed,
        "coordinate_coefficients_sha256": digest([coords(x) for x in sol]),
        "M2_high_basis_sha256": high_basis_hash,
        "product_recipes_sha256": digest(recipes),
        "every_original_product_prefix_checked": True,
        "B_order_at_infinity": b_order,
        "exact_representation": "three FLINT QQ polynomials modulo q^N, a^3=17",
        "original_identity_residual_sha256": poly_hash(residual),
        "grouped_certificate_dependency_sha256": hashlib.sha256(
            Path(__file__).read_bytes()).hexdigest(),
    }
    if not passed:
        info["first_nonzero_index"] = first
        info["first_nonzero_value"] = coords(coefficient(residual, first))
    progress("grouped certificate: original weight identity completed",
             bound=bound, passed=passed, first_nonzero_index=None if passed else first)
    return passed, info
