"""Outward coefficient intervals of the R643 homogeneous finite source, in its three charts."""
import math
from decimal import Decimal, localcontext
from fractions import Fraction

import r611_circular_reference_global_geometry_20261127 as iv

I, exp, sin, cos = iv.I, iv.exp_i, iv.sin_i, iv.cos_i


def rat(q):
    q = Fraction(q)
    x = float(q)
    f = Fraction.from_float(x)
    return I(iv.down(x) if f > q else x, iv.up(x) if f < q else x)


def hull(x, y):
    return I(min(x.lo, y.lo), max(x.hi, y.hi))


def mag(x):
    return max(abs(x.lo), abs(x.hi))


def log(x):
    if x.lo <= 0:
        raise ArithmeticError('positive log argument not proved')
    with localcontext() as ctx:
        ctx.prec = 90
        lo = Decimal.from_float(x.lo).ln().next_minus()
        hi = Decimal.from_float(x.hi).ln().next_plus()
        return I(iv.down(float(lo)), iv.up(float(hi)))


def power(x, m, n):
    if x.lo < 0:
        raise ArithmeticError('positive real power domain not established')
    def at(v):
        if v == 0:
            return I(0)
        with localcontext() as ctx:
            ctx.prec = 90
            # Correctly rounded Decimal ln, then outward arithmetic and exp in interval backend.
            lv = Decimal.from_float(v).ln()
            a = I(iv.down(float(lv.next_minus())), iv.up(float(lv.next_plus())))
        return exp(a * rat(Fraction(m, n)))
    return I(at(x.lo).lo, at(x.hi).hi)


RC, ELL, AMP = (rat(s) for s in ('0.22', '0.2', '0.8'))
R0, R, C, D = (rat(s) for s in ('0.3', '0.85', '0.55', '0.55'))
M, ALPHA = rat('20/9'), rat('11/20')


def flat_parts(u, mu):
    r = RC + ELL / u
    eps = mu * (mu-1) * ELL**2 / (r**2 * u**4)
    g = u*cos(u) - (2-sin(u)) + 2/u - 2*mu*ELL/(r*u**2)
    elog = -4/u + 2*ELL/(r*u**2)
    return r, eps, g, elog


def flat(u, mu, c):
    _, e, g, el = flat_parts(u, mu)
    return (I(0), e/c, -c, -g-el)


def seed_alpha(alpha, mu):
    pi = iv.original.DECIMAL_PI
    with localcontext() as ctx:
        ctx.prec = 80
        center = Decimal('34.5')*pi
        guard = Decimal('1e-65')
        if not (center+guard-Decimal('.04') < Decimal.from_float(alpha) < center-guard):
            raise ArithmeticError('stored alpha outside the original peak-17 bracket')
    residual = mag(flat_parts(I(alpha), mu)[2])
    error = (I(residual)/98).hi
    return I(iv.down(alpha-error), iv.up(alpha+error)), error


def finite_initial_z(a, mu):
    cells = 256
    # Green comparison uses only the first unit of the already specified coefficient.
    ar = RC+ELL/a
    accum = I(0)
    for i in range(cells):
        s = I(i/cells, (i+1)/cells)   # cells fixed to a power of two below
        u = a+s
        r = RC+ELL/u
        # Integer exponent via exp/log keeps shared positive ratios bounded even for j=22.
        weight = (a/u)**2 * exp((2*mu-2)*log(r/ar) + a*(2-sin(a))-u*(2-sin(u)))
        accum = accum + weight/cells
    delta = rat('1e-14')
    return I((accum-delta).lo, (accum*rat('25/24')+delta).hi)


def step(x):
    """The same C-infinity cutoff; enclose its value and derivative in its own coordinate."""
    if x.hi <= 0:
        return I(0), I(0)
    if x.lo >= 1:
        return I(1), I(0)
    l, h = max(0., x.lo), min(1., x.hi)
    def endpoint(t):
        if t == 0 or t == 1:
            return I(t)
        if t > .5:
            v = I(1)-I(t)
            z = exp(-1/v+1/(1-v))
            return 1/(1+z)
        v = I(t)
        z = exp(-1/v+1/(1-v))
        return z/(1+z)
    val = I(max(0., endpoint(l).lo), min(1., endpoint(h).hi))
    # At a zero endpoint, s' <= e^(2-1/h)(h^-2+4), by monotonicity for h<=1/2.
    # Use global 8 at ultra-small h to avoid multiplying an artificial exp floor by h^-2.
    if l == 0 or h == 1:
        far = h if l == 0 else (I(1)-l).hi
        if 1e-40 < far <= .5:
            v = I(far)
            top = (exp(2-1/v)*(v**-2+4)).hi
            return val, I(0, min(8., top))
        return val, I(0, 8)
    z = I(l, h)
    first = val*(1-val)*(z**-2+(1-z)**-2)
    return val, I(max(0., first.lo), min(8., first.hi))


def finite_part(r, gain):
    u = ELL/(r-RC)
    w = AMP*exp(-u*(2-sin(u)))
    wr = w*(u**2*(2-sin(u))-u**3*cos(u))/ELL
    drop, dr = step((r-R0)/rat('.04'))
    left, dl = step((r-rat('.37'))/rat('.11'))
    right, dq = step((rat('.61')-r)/rat('.13'))
    sup = exp(-6*drop)
    val = w*sup + gain*left*right
    der = sup*(wr-6*w*dr/rat('.04')) + gain*(dl*right/rat('.11')-left*dq/rat('.13'))
    return val, der


def body_slope(r, gain):
    w, wr = finite_part(r, gain)
    t = (r-C)/(R-C)
    if t.hi <= 0:
        return w, wr
    t = I(max(0., t.lo), t.hi)
    chi, dchi = step(t/rat('.1'))
    rem = 1-t**2
    base = rat('.5')*power(t, 11, 10)/power(rem, 11, 20)
    db = (rat('.5')*rat('1.1')*power(t, 1, 10)/power(rem, 11, 20)
          +base*2*ALPHA*t/rem)/(R-C)
    return w+chi*base, wr+chi*db+dchi*base/(rat('.1')*(R-C))


def body(r, mu, gain):
    w, wr = body_slope(r, gain)
    l = wr/w
    return 1/r, -mu/r, -l, l


def core_r(x):
    return R-D*power(x, 20, 9)


def core(x, mu, gain):
    # Domain of this exact regularization extends a little beyond the paid switch at .79.
    x = I(max(0., x.lo), x.hi)
    a = core_r(x)
    ax = -D*M*power(x, 11, 9)
    gamma = D/(R-C)
    u = gamma*power(x, 20, 9)
    t = 1-u
    if a.lo <= .7 or t.lo <= .2:
        raise ArithmeticError('core interval exceeds the fully-on core cutoff and vanished gain')
    wf = finite_part(a, gain)[0]
    zx = D*M*rat('.5')*power(t, 11, 10)/(power(gamma, 11, 20)*power(2-u, 11, 20))-ax*wf
    aa, ab = -(mu-1)*ax/a, -mu*zx/a
    return aa, ab, -ax*aa/zx, -ax*ab/zx


def check_profile(par):
    expected = dict(R=.85, log_suppression=6., core_scale=.5, drop_end=.34,
                    gain_start=.37, gain_peak=.48, gain_end=.61, core_start=.55,
                    alpha=.55, beta=1.1)
    if any(float(getattr(par, k)) != v for k, v in expected.items()):
        raise ValueError('fixed finite-source profile parameters differ')
    h = float(par.gain_height)
    if not math.isfinite(h):
        raise ValueError('nonfinite gain')
    return hull(I(h), rat(str(h)))


def flat_derivatives(u, mu, c):
    B = flat(u, mu, c)
    den = RC*u+ELL
    de = -2/u-2*RC/den
    T = 2*(mu-1)*ELL/(den*u)
    t = 1/u+RC/den
    b1 = u*sin(u)-2*cos(u)-2/u**2-T*t
    b2 = 3*sin(u)+u*cos(u)+4/u**3+T*(t**2+1/u**2+RC**2/den**2)
    zero = I(0)
    return (B,(zero, B[1]*de, zero, b1),
            (zero, B[1]*(de**2+2/u**2+2*RC**2/den**2), zero, b2))
