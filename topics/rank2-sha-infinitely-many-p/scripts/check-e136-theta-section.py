#!/usr/bin/env python3
"""R243: exact coefficient/discreteness certificate for the actual E136 theta.

Requires python-flint. All candidate coefficients and all height/tail bounds
are rational/integer calculations; Arb encloses the actual original Gaussian
vector of R239. Rationality is used only for the squares of normalized moments.
"""
from fractions import Fraction as Q
from math import factorial, lcm, prod
import json
from flint import acb, arb, ctx, fmpq

ctx.prec = 8192
CUT = 3000
ORDER = 64
WEIGHTS = tuple(range(4, ORDER+1, 4))
D_CURVE = 136
F_CONDUCTOR = 136
HEIGHT_E4 = 10**120
# Q(T)=T^15 P(1/T), so the actual normalized section is
# u'(z) theta(z)^68 u(z)^4 Q(u(z)^4).
COEFF = tuple(map(Q, (
    "1", "-567/55", "5799/55", "-17527/55", "-18057/11", "25927/5",
    "-154733/55", "-8103/11", "94949/55", "-136101/55", "135253/55",
    "-70277/55", "25169/55", "-765/11", "177/55", "-1/55"
)))


def aq(q):
    return fmpq(q.numerator, q.denominator)


def multiply(a, b, limit=ORDER):
    c = [Q(0)]*min(limit+1, len(a)+len(b)-1)
    for i, x in enumerate(a):
        if x:
            for j, y in enumerate(b[:len(c)-i]):
                if y:
                    c[i+j] += x*y
    return c


def exp_series(a):
    c = [Q(1)]+[Q(0)]*ORDER
    for n in range(1, ORDER+1):
        c[n] = sum((k*a[k]*c[n-k] for k in range(1, n+1)), Q(0))/n
    return c


def trim(a):
    a = a[:]
    while a and not a[-1]:
        a.pop()
    return a


def polynomial_gcd(a, b):
    a, b = trim(list(map(Q, a))), trim(list(map(Q, b)))
    while b:
        r = a[:]
        while r and len(r) >= len(b):
            k = len(r)-len(b)
            q = r[-1]/b[-1]
            for j, x in enumerate(b):
                r[k+j] -= q*x
            r = trim(r)
        a, b = b, r
    return [x/a[-1] for x in a] if a else []


def candidate_coefficients():
    u = [Q(0)]*(ORDER+1)
    u[1] = Q(1)
    for n in range(ORDER-1):
        cube = sum((u[a]*u[b]*u[n-a-b]
                    for a in range(n+1) for b in range(n+1-a)), Q(0))
        u[n+2] = -2*cube/((n+1)*(n+2))
    u2 = multiply(u, u)
    u4 = multiply(u2, u2)
    log_theta68 = [Q(0)]*(ORDER+1)
    for n in range(ORDER-1):
        log_theta68[n+2] = 68*u2[n]/((n+1)*(n+2))
    theta68 = exp_series(log_theta68)
    up = [(j+1)*u[j+1] for j in range(ORDER)]+[Q(0)]
    base = multiply(theta68, up)
    pw = u4
    answer = [Q(0)]*(ORDER+1)
    basis_leading_orders = []
    for j, c in enumerate(COEFF):
        term = multiply(base, pw)
        assert term[4*(j+1)] == 1
        assert all(x == 0 for x in term[:4*(j+1)])
        basis_leading_orders.append(4*(j+1))
        for n in range(ORDER+1):
            answer[n] += c*term[n]
        pw = multiply(pw, u4)
    assert answer[4] == 1
    factors = (
        [1,1], [1,-6,1], [1,-2,5],
        [-1,170,-2625,5080,-6114,9500,-9066,1176,899,-54,11]
    )
    polynomial = [Q(1,55)]
    for factor in factors:
        polynomial = multiply(polynomial, list(map(Q, factor)), 15)
    assert list(reversed(polynomial)) == list(COEFF)
    for j, f in enumerate(factors):
        assert len(polynomial_gcd(f, [k*f[k] for k in range(1,len(f))])) == 1
        for g in factors[:j]:
            assert len(polynomial_gcd(f, g)) == 1
    return {m: answer[m] for m in WEIGHTS}, polynomial, basis_leading_orders


def q_coefficients():
    # z/sigma for the original E136 differential dx/(2y).
    nmax = ORDER//4
    x = [Q(1)]+[Q(0)]*nmax
    for n in range(1, nmax+1):
        x[n] = (6*sum((x[j]*x[n-j] for j in range(1,n)), Q(0))
                -2*D_CURVE*(n == 1))/((4*n-2)*(4*n-3)-12)
    logq = [Q(0)]+[x[n]/(4*n*(4*n-1)) for n in range(1,nmax+1)]
    q = [Q(1)]+[Q(0)]*nmax
    for n in range(1,nmax+1):
        q[n] = sum((k*logq[k]*q[n-k] for k in range(1,n+1)), Q(0))/n
    return {4*n:q[n] for n in range(nmax+1)}


def denominator_bounds():
    q = q_coefficients()
    out = {}
    for m in WEIGHTS:
        c = 1
        for j, qj in q.items():
            if j <= m:
                c = lcm(c, (qj/(factorial(m)*factorial(m+1-j))).denominator)
        # Safe original local bounds: U >= -2 at 2 and >= -1 at 17;
        # x,y integral; division by f^(2m+1), f=136, adds 3 and 1.
        out[m] = c*2**(5*(2*m+1))*17**(2*(2*m+1))
    return out


def exact_size_and_tail_checks():
    f = F_CONDUCTOR
    # Omega_E136 > 1/3, all nonzero f-torsion points have distance >=1/f
    # from the normalized square lattice. The explicit shell bounds are:
    assert 3*(f+8*(f+2)+4+16) < 10**6
    assert 9*(9*f*f+8+80) < 10**12
    assert 27*(9*f**3+64) < 10**18
    M = 10**6
    dc5 = 2000**4*prod(range(5,9))*2001**5*factorial(5)
    dc1 = 2000**4*factorial(4)*2001
    bound = f*f*(Q(dc5*M**9, factorial(4)*factorial(5))
                 +Q(D_CURVE,60)*Q(dc1*M**5, factorial(4)))
    assert bound < HEIGHT_E4
    n = CUT+1
    assert Q(64,n)-Q(3*(2*n+1),4624) < -3
    assert Q(3*n*n,4624) > 5840
    # Hermite coefficient <= 2 n^64; two-sided weight <=2;
    # successive tail ratio < exp(-3) < 1/2. Use e>8/3.
    assert 8*n**64*3**5840*10**2200 < 8**5840
    # The ratio b_m^2 / (e_m/e_4) is an integer at every retained weight.
    multipliers = {}
    for m in WEIGHTS:
        k = m-4
        multiplier = 2**(13*k//2)*17**(5*k//2)
        assert multiplier**2 * D_CURVE**k == (18496*68)**(2*k)
        multipliers[m] = multiplier
    return bound, multipliers


def gaussian_enclosures():
    pi = arb.pi()
    sqrt2pi = (2*pi).sqrt()
    t = (pi/16).tan()
    assert t > 0 and t < 1
    v = [arb(0),arb(1),arb(0),t,arb(0),-t,arb(0),arb(-1),
         arb(0),arb(-1),arb(0),-t,arb(0),t,arb(0),arb(1)]
    lam = {pow(3,k,17):acb(0,-1)**k for k in range(16)}
    phase = [acb(0,2*pi*k/289).exp() for k in range(289)]
    b = {m:acb(0) for m in WEIGHTS}
    for n in range(1,CUT+1,2):
        if n%17 == 0:
            continue
        weight = 2*v[n%16]*lam[n%17]*phase[(236*n*n)%289]*(-pi*n*n/4624).exp()
        x = sqrt2pi*n/68
        old, now = arb(1), 2*x
        for m in range(1,ORDER):
            nxt = (2*x*now-2*old)/(m+1)
            old, now = now, nxt
            if (m+1)%4 == 0:
                b[m+1] += weight*now
    tail = acb(arb(0,"1e-2200"), arb(0,"1e-2200"))
    for m in WEIGHTS:
        b[m] += tail
    assert not b[4].contains(0)
    omega0 = arb(fmpq(1,4)).gamma()**2/(2*sqrt2pi)
    # R239 z -> z/2 passes from degree272 to the degree68 twisted line.
    scale = (pi/2).sqrt()*34/omega0/acb(4,-1)
    return {m:(b[m]/b[4])*scale**(m-4) for m in WEIGHTS}


def projective_coordinate_checks(P):
    def pm(a,b):
        return trim(multiply(a,b,64))
    def prodp(fs,c=Q(1)):
        r=[c]
        for f in fs:
            r=pm(r,list(map(Q,f)))
        return r
    def pp(a,n):
        return prodp([a]*n)
    def plus(a,b):
        r=[Q(0)]*max(len(a),len(b))
        for j,x in enumerate(a):r[j]+=x
        for j,x in enumerate(b):r[j]+=x
        return trim(r)
    def hom(P,n):
        r=[]
        for j,c in enumerate(P):
            r=plus(r,[c*x for x in pp([1,0,-1],n-j)])
        return r
    PA=prodp(([0,1],[-1,1],[-1,1],[1,1],[5,-2,1],[1,-2,5],
              [1,4,70,4,1],[1,20,-26,20,1]),Q(1,5))
    PB=prodp(([0,1],[-1,1],[1,2,1],[5,-2,1],[1,-2,5],
              [1,0,364,-1088,1190,-1088,364,0,1]),Q(1,5))
    PH=pm([0,1],P)
    raw=[hom(PA,17),hom(PB,17),pm([0,1],hom(PH,17))]
    g=prodp(([0,1],[-1,0,1],[-2,0,1],[4,0,0,0,1]))
    a=prodp(([0,0,0,1],[4,0,-8,0,5],
             [16,0,-32,0,40,0,-24,0,1],
             [80,0,-160,0,88,0,-8,0,1]),Q(1,5))
    b=prodp(([0,1],[-2,0,1],[4,0,-8,0,5],
             [-256,0,1024,0,-1152,0,-128,0,1280,0,-1152,0,392,0,-8,0,1]),Q(-1,5))
    h=prodp(([-4,0,4,0,1],
             [1024,0,-4096,0,7424,0,-17408,0,38016,0,-46336,0,29984,0,
              -9920,0,1140,0,160,0,1]),Q(-1,55))
    for n,q in zip(raw,[a,b,h]):
        assert n==pm(g,q)
    assert polynomial_gcd(a,polynomial_gcd(b,h))==[Q(1)]
    assert [len(q)-1 for q in [a,b,h]]==[23,23,24]
    abg=polynomial_gcd(a,b)
    assert len(a)-len(abg)==len(b)-len(abg)==18
    return {"primitive_degrees":[23,23,24],"old_ratio_degree_in_t":18,
            "exact_common_factor":[str(c) for c in g],
            "primitive_a":[str(c) for c in a],
            "primitive_b":[str(c) for c in b],
            "primitive_h":[str(c) for c in h],
            "all_three_original_identities":True}


def main():
    target, polynomial, orders = candidate_coefficients()
    denominator = denominator_bounds()
    _, multipliers = exact_size_and_tail_checks()
    balls = gaussian_enclosures()
    projective = projective_coordinate_checks(polynomial)
    certificates = []
    for m in WEIGHTS:
        beta = target[m]
        H = denominator[m]*denominator[4]*HEIGHT_E4
        spacing = H*(beta*beta).denominator
        error = balls[m]**2-acb(aq(beta*beta))
        assert abs(error) < arb(fmpq(1,spacing))
        assert balls[m].imag.contains(0)
        if beta > 0:
            assert balls[m].real > 0
        elif beta < 0:
            assert balls[m].real < 0
        certificates.append({
            "weight":m, "exact_coefficient":str(beta),
            "spacing_denominator_digits":len(str(spacing)),
            "rational_square_multiplier":str(multipliers[m]),
            "square_and_sign_certified":True
        })
    print(json.dumps({
        "theorem":"R243", "status":"PASS", "precision_bits":ctx.prec,
        "gaussian_cutoff":CUT, "uniform_raw_tail_bound":"1e-2200",
        "height_e4_bound":"10^120", "weights":WEIGHTS,
        "basis_leading_orders":orders,
        "polynomial_P_ascending":[str(x) for x in polynomial],
        "polynomial_Q_ascending":[str(x) for x in COEFF],
        "all_factors_squarefree_and_pairwise_coprime":True,
        "projective_coordinate_checks":projective,
        "certificates":certificates
    },indent=2))


if __name__ == "__main__":
    main()
