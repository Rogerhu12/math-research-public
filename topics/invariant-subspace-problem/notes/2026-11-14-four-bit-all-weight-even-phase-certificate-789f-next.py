"""Exact four-independent-weight, full primitive-space even phase certificate.

The first two principal minors use the additive ordered cone.  The determinant
has a manifest positive factor and a degree-16 factor certified on two
multiplicative ordered cones.  Equal weights are an equality case, not strict.
The physical source is
E_i=e_i/b_i-e_4/b_4, with its full metric retained.  Complete-precision C=G^-1
and top Gram L are the actual four-bit formulas, not compressed full inverses.
"""

import argparse
import hashlib
import json
import resource
import time
from pathlib import Path

from flint import fmpz_mpoly_ctx


CTX = fmpz_mpoly_ctx.get(('z1', 'z2', 'z3', 'z4'))
Z = list(CTX.gens())
ZERO, ONE = CTX.constant(0), CTX.constant(1)


def emit(kind, **data):
    print(json.dumps({'kind': kind, **data}, sort_keys=True), flush=True)


def eye():
    return [[ONE if i == j else ZERO for j in range(3)] for i in range(3)]


def transpose(m):
    return [list(x) for x in zip(*m)]


def multiply(*matrices):
    m = matrices[0]
    for n in matrices[1:]:
        m = [[sum((m[i][k]*n[k][j] for k in range(len(n))), ZERO)
              for j in range(len(n[0]))] for i in range(len(m))]
    return m


def scale(m, a):
    return [[a*x for x in row] for row in m]


def add(m, n, factor=1):
    return [[m[i][j]+factor*n[i][j] for j in range(3)] for i in range(3)]


def divide(p, q):
    a, r = divmod(p, q)
    assert not r
    return a


def profile(p):
    c = list(p.coeffs())
    return {'terms': len(p), 'degree': int(p.total_degree()) if p else -1,
            'negative': sum(x < 0 for x in c),
            'positive': sum(x > 0 for x in c)}


def source_numerators():
    z = Z
    S = sum(z, ZERO)
    e = sum((z[i]*z[j] for i in range(4) for j in range(i+1, 4)), ZERO)
    f = sum((z[i]*z[j]*z[k] for i in range(4) for j in range(i+1, 4)
             for k in range(j+1, 4)), ZERO)
    p = z[0]*z[1]*z[2]*z[3]
    p_i = [divide(p, x) for x in z]
    # H^-1 = Hinv_numerator / S.
    hi = [[(S*z[i] if i == j else ZERO)-z[i]*z[j]
           for j in range(3)] for i in range(3)]
    # C = Cn/e, L = Ln/(S*p), Q0 = Qn/(S*p), all as source operators.
    cn = [[(e*(S-2*z[i]) if i == j else ZERO)
           + z[i]*(S-z[i])*(z[j]-z[3])
           for j in range(3)] for i in range(3)]
    ln = [[(S*z[i]**2 if i == j else ZERO)-z[i]*(z[j]**2-z[3]**2)
           for j in range(3)] for i in range(3)]
    qn = [[(S*(f-2*p_i[i]) if i == j else ZERO)
           +(S-2*z[i])*(p_i[j]-p_i[3])
           for j in range(3)] for i in range(3)]
    return S, e, p, hi, cn, ln, qn


def phase_defect_numerator(kappa):
    S, e, p, hi, cn, ln, qn = source_numerators()
    # W=C H0=C^2 L+2I-C Q0, with denominator e^2*S*p.
    wn = add(add(multiply(cn, cn, ln), scale(eye(), 2*e**2*S*p)),
             scale(multiply(cn, qn), e), -1)
    # Congruence H^-1 of the physical quadratic form of
    # C(kappa L-H0 H0*)C.  Its positive denominator is e^4*S^3*p^2.
    answer = add(scale(multiply(cn, ln, cn, hi), kappa*e**2*S*p),
                 multiply(wn, hi, transpose(wn)), -1)
    assert answer == transpose(answer)
    common = ZERO
    for row in answer:
        for entry in row:
            common = common.gcd(entry)
    emit('constructed', kappa=kappa, entry_max_terms=max(len(x) for row in answer for x in row),
         common=str(common))
    # Both p*S^2 and positive monomials are manifestly positive on z_i>0.
    if common == p*S**2:
        answer = [[divide(x, common) for x in row] for row in answer]
        emit('removed_positive_factor', factor='(z1*z2*z3*z4)*(z1+z2+z3+z4)^2')
    elif len(common) == 1:
        exponent, coefficient = next(iter(common.to_dict().items()))
        if coefficient > 0:
            answer = [[divide(x, common) for x in row] for row in answer]
            emit('removed_positive_monomial', exponent=list(map(int, exponent)), coefficient=str(coefficient))
    return answer


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--kappa', type=int, default=1)
    parser.add_argument('--output', type=Path)
    parser.add_argument('--cpu-seconds', type=int, default=55)
    parser.add_argument('--verify-original', action='store_true')
    args = parser.parse_args()
    if args.kappa != 1:
        parser.error('The factored determinant certificate below is for kappa=1.')
    resource.setrlimit(resource.RLIMIT_CPU, (args.cpu_seconds, args.cpu_seconds+5))
    resource.setrlimit(resource.RLIMIT_AS, (1536*1024**2, 1536*1024**2))
    start = time.monotonic()
    original = phase_defect_numerator(args.kappa)
    assert all(entry(1, 1, 1, 1) == 0 for row in original for entry in row)
    x, y, z, w = Z
    substitution = (x, x+y, x+y+z, x+y+z+w)
    d = [[entry.compose(*substitution) for entry in row] for row in original]
    assert d == transpose(d)
    m1 = d[0][0]
    m2 = d[0][0]*d[1][1]-d[0][1]**2
    a = original
    determinant = (a[0][0]*(a[1][1]*a[2][2]-a[1][2]**2)
                   -a[0][1]*(a[0][1]*a[2][2]-a[1][2]*a[0][2])
                   +a[0][2]*(a[0][1]*a[1][2]-a[1][1]*a[0][2]))
    S, e, p, *_ = source_numerators()
    residual = divide(determinant, p**2*S**2*e**8)
    assert residual.total_degree() == 16
    chamber0 = residual.compose(ONE, 1+y+z, (1+y+z)*(1+w), (1+y+z)*(1+w)*(1+y))
    chamber1 = residual.compose(ONE, 1+y, (1+y)*(1+w), (1+y)*(1+w)*(1+y+z))
    receipt = {'kappa': args.kappa, 'substitution': ['x', 'x+y', 'x+y+z', 'x+y+z+w'],
               'determinant_factor': 'P^2*S^2*e2^8',
               'multiplicative_chambers': [
                   ['1', '1+a+b', '(1+a+b)*(1+c)', '(1+a+b)*(1+c)*(1+a)'],
                   ['1', '1+a', '(1+a)*(1+c)', '(1+a)*(1+c)*(1+a+b)']],
               'certificates': [],
               'residual_degree16': [[list(map(int, exponent)), str(coefficient)]
                   for exponent, coefficient in sorted(residual.to_dict().items())],
               'equal_weights_defect_zero': True}
    for label, polynomial in [('minor1', m1), ('minor2', m2),
                              ('determinant_chamber0', chamber0),
                              ('determinant_chamber1', chamber1)]:
        data = profile(polynomial)
        entries = [[list(map(int, exponent)), str(coefficient)]
                   for exponent, coefficient in sorted(polynomial.to_dict().items())]
        data.update({'label': label, 'sha256': hashlib.sha256(
            json.dumps(entries, separators=(',', ':')).encode()).hexdigest(),
                     'coefficients': entries})
        receipt['certificates'].append(data)
        emit('certificate', label=label, **profile(polynomial))
    receipt['certificate_passed'] = all(m['negative'] == 0 and m['positive'] > 0
                                        for m in receipt['certificates'])
    if args.verify_original:
        receipt['original_incidence_verified'] = verify_original_incidence(original)
    receipt['elapsed_seconds'] = time.monotonic()-start
    if args.output:
        args.output.write_text(json.dumps(receipt, ensure_ascii=False, separators=(',', ':'))+'\n')
    emit('completed', passed=receipt['certificate_passed'], elapsed_seconds=receipt['elapsed_seconds'])


def verify_original_incidence(numerator):
    """One exact, separate normalization check, not the positivity proof."""
    from itertools import combinations
    import sympy as sp
    b = list(map(sp.Integer, (1, 2, 3, 4)))
    zz = [int(x*x) for x in b]

    def deletion(weights, degree, power=1):
        columns = list(combinations(range(4), degree))
        rows = list(combinations(range(4), degree-power))
        return sp.Matrix([[sp.prod(weights[i] for i in set(I)-set(J))
                           if set(J) <= set(I) else 0 for I in columns] for J in rows])

    basis = sp.Matrix([[1, 0, 0], [0, 1, 0], [0, 0, 1], [-1, -1, -1]])
    E = sp.diag(*[1/x for x in b])*basis
    H = E.T*E
    hi = H.inv()
    d1 = deletion(b, 2)
    d2 = deletion(b, 3, 2)
    G = hi*E.T*(d1*d1.T).inv()*E
    L = hi*E.T*(d2*d2.T).inv()*E
    top = sp.Matrix.hstack(*d1.nullspace())
    dual = deletion([1/x for x in b], 2)
    R0 = hi*E.T*dual*top*(top.T*top).inv()*top.T*dual.T*E
    Q0 = hi*E.T*(dual*dual.T)*E
    C = G.inv()
    H0 = C*L-2*G-R0
    assert H0 == C*L+2*G-Q0
    S, e, p, hin, cn, ln, qn = source_numerators()

    def evaluated(matrix):
        return sp.Matrix([[int(x(*zz)) for x in row] for row in matrix])

    sv, ev, pv = int(S(*zz)), int(e(*zz)), int(p(*zz))
    assert C == evaluated(cn)/ev
    assert L == evaluated(ln)/(sv*pv)
    assert Q0 == evaluated(qn)/(sv*pv)
    assert hi == evaluated(hin)/sv
    W = C*H0
    actual = C*L*C*hi-W*hi*W.T
    assert actual == evaluated(numerator)/(ev**4*sv*pv)
    emit('original_incidence_exact', weights=[1, 2, 3, 4], passed=True)
    return True


if __name__ == '__main__':
    main()
