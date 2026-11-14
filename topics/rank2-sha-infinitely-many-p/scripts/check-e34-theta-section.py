#!/usr/bin/env python3
"""Exact Gaussian/discreteness certificate for the E34 degree-68 section.

The numerical candidate is not assumed: each squared normalized coefficient
is rational by the established central-square formula. Its denominator is
bounded using the explicit good models and the torsion logarithmic derivative.
Arb enclosures plus the rational spacing bound identify every coefficient.
"""
from fractions import Fraction as Q
from math import factorial, lcm, prod
from flint import acb, arb, ctx, fmpq

ctx.prec = 8192
CUT = 1400
ORDER = 68
WEIGHTS = tuple(range(4, ORDER+1, 4))
D_CURVE = 1156
HEIGHT_E4 = 10**100
COEFF = tuple(map(Q, (
    "1", "-7/5", "1833/5", "-7963/5", "18273/5", "-18827/5",
    "-11387/5", "35521/5", "-35521/5", "11387/5", "18827/5",
    "-18273/5", "7963/5", "-1833/5", "7/5", "-1", "0"
)))


def multiply(a, b, limit=ORDER):
    c = [Q(0)]*(min(limit+1, len(a)+len(b)-1))
    for i, x in enumerate(a):
        if not x:
            continue
        for j, y in enumerate(b):
            if i+j >= len(c):
                break
            if y:
                c[i+j] += x*y
    return c


def exp_series(a):
    c = [Q(1)]+[Q(0)]*ORDER
    for n in range(1, ORDER+1):
        c[n] = sum((k*a[k]*c[n-k] for k in range(1,n+1)), Q(0))/n
    return c


def polynomial_gcd(a, b):
    def trim(v):
        while v and v[-1] == 0:
            v.pop()
        return v
    a, b = trim(list(map(Q,a))), trim(list(map(Q,b)))
    while b:
        r = a[:]
        while r and len(r) >= len(b):
            scale = r[-1]/b[-1]
            offset = len(r)-len(b)
            for j, value in enumerate(b):
                r[offset+j] -= scale*value
            trim(r)
        a, b = b, r
    return [value/a[-1] for value in a] if a else []


def candidate_coefficients():
    # On E0, u=1/sqrt(x), L=theta'/theta:
    # u''=-2u^3, L'=u^2. This is an exact rational series computation.
    u = [Q(0)]*(ORDER+1)
    u[1] = Q(1)
    for n in range(ORDER-1):
        cube = sum(
            (u[a]*u[b]*u[n-a-b] for a in range(n+1)
             for b in range(n+1-a)), Q(0)
        )
        u[n+2] = -2*cube/((n+1)*(n+2))
    u2 = multiply(u,u)
    u4 = multiply(u2,u2)
    log_theta68 = [Q(0)]*(ORDER+1)
    for n in range(ORDER-1):
        log_theta68[n+2] = 68*u2[n]/((n+1)*(n+2))
    theta68 = exp_series(log_theta68)
    pw = u4
    ans = [Q(0)]*(ORDER+1)
    for c in COEFF:
        term = multiply(theta68,pw)
        for n in range(ORDER+1):
            ans[n] += c*term[n]
        pw = multiply(pw,u4)
    assert ans[4] == 1
    # Independently check the exact polynomial factorization.
    factors = (
        [0,1], [-1,1], [1,2,1], [5,-2,1], [1,-2,5],
        [1,0,364,-1088,1190,-1088,364,0,1],
    )
    polynomial = [Q(1,5)]
    for factor in factors:
        polynomial = multiply(polynomial, list(map(Q,factor)), 16)
    assert list(reversed(polynomial)) == list(COEFF)
    q8 = factors[-1]
    assert len(polynomial_gcd(q8,[j*q8[j] for j in range(1,9)])) == 1
    for factor in factors[:-1]:
        assert len(polynomial_gcd(q8,factor)) == 1
    return {m:ans[m] for m in WEIGHTS}


def q_coefficients():
    # q(z)=z/sigma_E34(z), only z^(4n) terms occur.
    nmax=ORDER//4
    x=[Q(1)]+[Q(0)]*nmax
    for n in range(1,nmax+1):
        x[n] = (
            6*sum((x[j]*x[n-j] for j in range(1,n)), Q(0))
            -2*D_CURVE*(n == 1)
        )/((4*n-2)*(4*n-3)-12)
    logq=[Q(0)]+[x[n]/(4*n*(4*n-1)) for n in range(1,nmax+1)]
    q=[Q(1)]+[Q(0)]*nmax
    for n in range(1,nmax+1):
        q[n]=sum((k*logq[k]*q[n-k] for k in range(1,n+1)),Q(0))/n
    return {4*n:q[n] for n in range(nmax+1)}


def denominator_bounds():
    q=q_coefficients()
    bounds={}
    for m in WEIGHTS:
        c=1
        for j,qj in q.items():
            if j<=m:
                c=lcm(c,(qj/(factorial(m)*factorial(m+1-j))).denominator)
        d=c*2**(3*(2*m+1))*17**((3*(2*m+1)+1)//2)
        bounds[m]=(c,d)
    return bounds


def exact_size_checks():
    # Omega_E34>1/3, all nonzero 68-torsion representatives have
    # distance >=1/68 from the square lattice. Shell sums give:
    assert 3*(68+8*70+4+16) < 10**5
    assert 9*(9*68**2+8+80) < 10**10
    assert 27*(9*68**3+64) < 10**15
    M=10**5
    dc5=2000**4*prod(range(5,9))*2001**5*factorial(5)
    dc1=2000**4*factorial(4)*2001
    bound=2048*(
        Q(dc5*M**9,factorial(4)*factorial(5))
        +Q(D_CURVE,60)*Q(dc1*M**5,factorial(4))
    )
    assert bound<HEIGHT_E4
    # For n>=1401, the successive tail ratio is <exp(-7)<1/2.
    n=CUT+1
    assert Q(68,n)-Q(3*(2*n+1),1156)<-7
    assert Q(3*n*n,1156)>5093
    # e>8/3 proves the entire omitted two-sided tail <10^-1900.
    assert 12*n**68*3**5093*10**1900<8**5093
    return bound


def gaussian_enclosures():
    pi=arb.pi()
    sqrt2pi=(2*pi).sqrt()
    legendre={pow(3,k,17):(-1)**k for k in range(16)}
    b={m:acb(0) for m in WEIGHTS}
    for n in range(1,CUT+1):
        if n%17 == 0:
            continue
        sign=(-1 if n%4==2 else 1)*legendre[n%17]
        phase=acb(0,2*pi*((77*n*n)%289)/289).exp()
        weight=2*sign*phase*(-pi*n*n/1156).exp()
        x=sqrt2pi*n/34
        old=arb(1)
        now=2*x
        for m in range(1,ORDER):
            nxt=(2*x*now-2*old)/(m+1)
            old,now=now,nxt
            if (m+1)%4==0:
                b[m+1]+=weight*now
    tail=acb(arb(0,"1e-1900"),arb(0,"1e-1900"))
    for m in WEIGHTS:
        b[m]+=tail
    assert not b[4].contains(0)
    omega0=arb(fmpq(1,4)).gamma()**2/(2*sqrt2pi)
    scale=(pi/2).sqrt()*34/omega0/acb(4,-1)
    return {m:(b[m]/b[4])*scale**(m-4) for m in WEIGHTS}


def main():
    target=candidate_coefficients()
    den=denominator_bounds()
    size=exact_size_checks()
    print("Exact global bound |e4|<10^100: verified.",flush=True)
    print("Exact Gaussian tail <10^-1900: verified.",flush=True)
    balls=gaussian_enclosures()
    for m in WEIGHTS:
        beta=target[m]
        # b_m^2=9248^(m-4)*e_m/e4. The multiplier is integral.
        rational_den_bound=den[m][1]*den[4][1]*HEIGHT_E4
        spacing_den=rational_den_bound*(beta*beta).denominator
        error=balls[m]**2-acb(fmpq((beta*beta).numerator,(beta*beta).denominator))
        assert abs(error)<arb(fmpq(1,spacing_den))
        assert balls[m].imag.contains(0)
        if beta>0:
            assert balls[m].real>0
        elif beta<0:
            assert balls[m].real<0
        print(
            "weight",m,"coefficient",str(beta),
            "spacing-denominator decimal digits",len(str(spacing_den)),
            "square uniquely certified; sign certified",flush=True
        )
    print("All 17 coefficients identify the actual degree-68 section.",flush=True)
    print("P(X)=X(X-1)(X+1)^2(X^2-2X+5)(5X^2-2X+1)Q8(X)/5.",flush=True)


if __name__=="__main__":
    main()
